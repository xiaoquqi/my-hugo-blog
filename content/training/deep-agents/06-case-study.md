---
title: 第 6 章 · 实战复盘：一个真实的上下文丢失 bug
date: 2026-07-20T07:25:00+08:00
author: Ray Sun
tags:
  - Deep Agent
  - LangChain
  - SourceLens
  - AI
categories:
  - AI应用开发
weight: 7
---

第 3 章留了一个伏笔：`afac535`（2026-06-15）第一次给 harness 加上压缩安全网时，留下了一个"workspace 内容都能重新搜到"的假设；`7854b8d`（2026-06-24）又因为一次超时故障把触发阈值从 8 万调低到 4.8 万。这一章讲的就是这个伏笔一个月后是怎么兑现成一次真实故障的——[SourceLens issue #60](https://github.com/HyperBDR/sourcelens/issues/60) 和修复它的 [PR #61](https://github.com/HyperBDR/sourcelens/pull/61)，2026-07-19。团队一开始对压缩机制的理解就踩在第 4 章那两个坑上，从现象定位到修复的完整过程，比抽象讲概念更有说服力——也再次印证第 3 章的道理：harness 是被真实场景一步步逼出来、逼对的，这次修复本身也是"逼近"的一部分。

## 现象：答案变成一句空壳

生产会话 `d06f44c1-2bb2-4524-8919-e601da442508`（助手 `AI_AGIOne`）里：

1. 用户粘贴了一段 8305 字符的提案原文，要求"对照我们的文档核对这份提案有没有错误"。
2. 助手只回了 153 个字符："以上是完整的核查报告，优先处理 🔴 一级问题……"——但报告正文从未出现过。运行日志里其实能看到中间产生过 `## 第4.3节…`、`## 第8节容量规划核查结论…` 这些分节分析，只是它们被压缩成了摘要，从未进入最终答案。
3. 用户追问"你没有返回完整信息"。
4. 助手的回答变成"我浏览的工作区文档里……"——已经不再是对照那份粘贴提案，因为提案原文已经不在上下文里了。

## 定位：压缩机制的一个隐藏假设不成立

日志（run `b59357b1-1105-40c0-ac69-a09a4e865762`）显示 `deepagents.summarization.enabled TriggerTokens: 48000 KeepTokens: 16000`，prompt token 数一路从 `12065 → 16777 → 37606 → 69052`，一次 47496 字符的检索步骤把上下文推过了触发线，压缩被触发。

根因写在 `LensSummarizationMiddleware` 当时的文档注释里（正是 `afac535` 那次提交留下的原话）："workspace 始终可以重新搜索，所以从摘要里丢掉的证据都可以再查一次"——**这个前提只对 workspace 检索出来的工具结果成立，对用户在聊天里手打/粘贴的内容不成立**。`CONTINUATION_SUMMARY_PROMPT` 当时只保证"原始问题"逐字保留，但一段 8300 字的粘贴提案不是一个简短的问题，摘要模型把它压成一句"核对这份提案"，正文就这样丢了——这正是第 4 章讲的**模式①**。

还有一个次要因素：后端历史构建逻辑会把每条历史消息截到 `HISTORY_MAX_MESSAGE_CHARS = 2000`（总量上限 `HISTORY_MAX_TOTAL_CHARS = 8000`），所以哪怕当次压缩没触发，下一轮这段长粘贴内容也会被截断——这个问题被判定为次要因素，在这次修复里刻意推迟处理，没有一并解决。

## 修复 A：给用户输入一个"压缩豁免"

对应第 4 章的模式①。`LensSummarizationMiddleware._partition_messages`（`agent_runtime.py:108-136`）覆写了基类的切分逻辑：

```python
def _partition_messages(self, conversation_messages, cutoff_index):
    """Keep human input verbatim; summarize only re-queryable turns."""
    to_summarize = conversation_messages[:cutoff_index]
    preserved = conversation_messages[cutoff_index:]
    human_anchors = [
        message
        for message in to_summarize
        if isinstance(message, HumanMessage)
    ]
    if not human_anchors:
        return to_summarize, preserved
    non_human = [
        message
        for message in to_summarize
        if not isinstance(message, HumanMessage)
    ]
    # Anchors are clustered ahead of the preserved tail, not kept in their
    # original positions. The stream stays valid (no orphaned ToolMessages;
    # only HumanMessages move) and the user turns survive verbatim.
    return non_human, human_anchors + preserved
```

思路很直接：基类原本会把 `cutoff_index` 之前的所有消息（包括用户消息）都送进摘要，这次改成把其中的 `HumanMessage` 挑出来，移到"保留"那一侧，逐字保留、不进摘要；只有真正可以从 workspace 重新查到的工具/AI 轮次才会被摘要掉。配套地，`CONTINUATION_SUMMARY_PROMPT` 也去掉了"原始问题"小节——不用再让摘要模型复述问题，因为用户原话已经原封不动地留在了上下文里。

## 修复 B：别等攒到压缩线才处理

对应模式②。这次复现用的是"哈利波特系列全文时间线核查"这种小问题、大语料库的场景——检索量涨得比压缩能处理的还快，压缩被反复触发却始终没能收敛出结果，整个任务打转在"搜索 → 压缩 → 遗忘"的循环里。

`deepagents` 自带的 `FilesystemMiddleware` 本来就有主动卸载超大工具结果的能力，但 `create_deep_agent` 把阈值硬编码在 `20000` token，没有开放配置入口。`_apply_offload_thresholds`（`agent_runtime.py:202-243`）用一个 monkeypatch 把这个默认值改成可配置：

```python
_OFFLOAD_PATCH_LOCK = threading.Lock()


def _apply_offload_thresholds(config):
    if getattr(FilesystemMiddleware.__init__, "_lens_offload_wrapped", False):
        return
    with _OFFLOAD_PATCH_LOCK:
        if getattr(FilesystemMiddleware.__init__, "_lens_offload_wrapped", False):
            return
        tool_tokens = config.offload_tool_tokens
        human_tokens = config.offload_human_tokens
        original_init = FilesystemMiddleware.__init__

        def init_with_offload_defaults(self, *args, **kwargs):
            kwargs.setdefault("tool_token_limit_before_evict", tool_tokens)
            if human_tokens is not None:
                kwargs.setdefault(
                    "human_message_token_limit_before_evict", human_tokens
                )
            original_init(self, *args, **kwargs)

        init_with_offload_defaults._lens_offload_wrapped = True
        FilesystemMiddleware.__init__ = init_with_offload_defaults
```

几个设计细节值得留意，都是为了让 monkeypatch 本身不引入新问题：

- 用 `setdefault` 注入而不是强制覆盖，任何调用方显式传的参数依然优先生效。
- 类身份不变（还是原来的 `FilesystemMiddleware`），要求中间件/`isinstance` 检查的地方不受影响。
- 用锁 + 一个自定义属性标记只安装一次，因为 lensnode 在多个 worker 线程上跑运行，防止并发场景下重复包装。
- 工具阈值默认降到 `5000`（`LENSNODE_OFFLOAD_TOOL_TOKENS`），人类消息阈值维持库默认 `50000` 不动——因为修复 A 已经把人类消息挪出压缩范围了，不需要再额外卸载它。

配置知识本身在 `config.py:89-94`（第 4 章提过对应的环境变量默认值）。

## A/B 实证：同一个任务，两种配置

修复合并前，团队用同一个"哈利波特时间线"任务（DeepSeek-V4-Pro）跑了对照：

| | offload 关闭 | offload 开启（5000） |
|---|---|---|
| 触发压缩次数 | **4 次** | **0 次** |
| 耗时 | 16 分钟以上 | 4 分钟 |
| 结果 | 反复打转，未收敛，坍缩成单一场景 | **完整的时间线** |

修复 A 那条路径的效果同样明确：粘贴提案的核查任务从 153 字符的空壳答案，变成完整的、按小节排列的核查报告。

## 一个刻意的决定：没有调高触发线

看到"压缩太频繁"，直觉的修法是把 `summary_trigger_tokens` 调高。这个数字本身也有一段历史：`afac535`（2026-06-15）第一次引入压缩安全网时，默认值是 `80000`；`7854b8d`（2026-06-24）因为一次超时故障（一次 9K token 的调用因为模型端点响应慢、litellm 重试，拖到运行整体超时）把它调低到了 `48000`——这次调整的动机是"更早触发压缩、避免单轮拖太久"，和 issue #60 没有直接关系，但方向是一致的：**触发线只降不升**。PR #61 里明确说明了为什么这次也没有反过来调高：

第 4 章讲过，SourceLens 用的近似计数器对 `LensGatewayChatModel` 走的是通用默认比例（`chars_per_token=4.0`），而且因为网关从不填充 `AIMessage.usage_metadata`，`use_usage_metadata_scaling` 的自我校准分支从未真正生效过——这两点在我们重新对照容器内实际安装的库源码核实时得到了确认。中文场景下"4 字符 = 1 token"的估算本来就偏保守（低估），也就是说 `48000` 这个计数器读数，对应的中文真实 token 消耗比表面数字要高不少——已经在逼近模型可用输入的上限附近。调高触发线换来的不是"压缩变少"，而是"距离真正的上下文溢出更近"；卸载解决的是同一个"上下文涨得太快"的问题，但它按真实内容大小卸载，不依赖这个偏差的计数器，所以是更安全的那条路。**因此触发线被刻意维持在 `48000` 不动，靠卸载去解决压缩过频的问题。**

（这里多说一句：PR 描述里当时记录的判断依据是 `chars_per_token=3.3`；这次写这篇教程时对照容器内实际安装的 `deepagents 0.6.8`/`langchain 1.3.7` 源码重新核实，确认 `3.3` 只在模型 `_llm_type` 以 `anthropic-chat` 开头时才生效，`LensGatewayChatModel` 走的其实是通用默认值 `4.0`——不影响这条决策本身的结论，反而让"中文被低估"这件事更严重，但这是一个值得记下来的认知偏差：即使是刚合并不久的分析，也值得在下次改动前对照当前安装的库版本重新核实一遍，而不是照抄上一次的记忆。）

## Review 里的一个小插曲：`"0" or "5000"` 到底对不对

自动 review 机器人对 `offload_tool_tokens=int(os.getenv("LENSNODE_OFFLOAD_TOOL_TOKENS") or "5000")` 这行提了一个"重要 bug"：认为 `or` 写法会把显式设置的 `"0"` 误判为空、退回到 `5000`，建议改成 `int(os.getenv(key, "5000"))`。

作者的回复澄清了这是一次误报，理由拆开来看很值得记住：

- `os.getenv()` 返回的是**字符串**，Python 里只有空字符串 `""` 是假值，`"0"` 是非空字符串、天然为真——所以 `"0" or "5000"` 求值结果是 `"0"`，`int("0") == 0` 会被正确采纳（`0` 在 `FilesystemMiddleware` 里语义就是关闭卸载，`filesystem.py:1808` 有 `if not self._tool_token_limit_before_evict` 的判断）。
- 机器人建议的 `getenv(key, "5000")` 反而有个更隐蔽的问题：SourceLens 的开发 compose 文件传的是 `${LENSNODE_OFFLOAD_TOOL_TOKENS:-}`——宿主机没设这个变量时，容器收到的是**被设置成空字符串**的环境变量，不是"未设置"。这种情况下 `getenv(key, "5000")` 返回的是 `""`，`int("")` 会直接抛 `ValueError`，容器起不来。

对照表：

| 环境变量取值 | `int(getenv(...) or "5000")`（现用写法） | `int(getenv(..., "5000"))`（机器人建议） |
|---|---|---|
| 未设置（`None`） | 5000 | 5000 |
| `""`（compose 的 `:-` 默认展开） | 5000 | **抛 `ValueError`，启动失败** |
| `"0"`（显式关闭） | **0（生效）** | 0 |
| `"8000"` | 8000 | 8000 |

这个小插曲的价值不在于"机器人错了"，而在于：**同一个环境变量在"未设置"和"被设置成空字符串"之间的区别，只有结合实际部署方式（这里是 compose 的 `:-` 默认值语法）才能判断清楚**——脱离部署上下文单看这一行代码，两种写法看起来都"更安全"，但只有其中一种跟这个项目的真实 compose 配置兼容。

## 留下的尾巴

这次修复承认了两个未处理项：次要因素——跨轮次历史截断（`HISTORY_MAX_MESSAGE_CHARS`）——被判定为次要因素，推迟处理；针对 `_partition_messages`（人类消息保留）和卸载阈值注入的自动化回归测试也被列为后续待办，没有随这次修复一起补上。计数器精度的改进方向也留作后续——让触发线真正测量的是模型真实 token 数（比如让网关正确回填 `usage_metadata`，或者换一个对语言更敏感的计数器），在那之前，`summary_trigger_tokens` 这个数字都不建议手动调大。

下一章把这几章的内容收拢成一份可执行的 checklist。
