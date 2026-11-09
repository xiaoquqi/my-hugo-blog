# 精读栏目工作流

栏目地址 `/reading/`；中文名称“精读”。它与普通博客文章并列，使用既有 Hugo/Hextra、站内搜索、栏目 RSS，以及主分支预览与版本标签正式发布流程。

## 新增一篇

```bash
hugo new content reading/文章英文短名/index.md --kind reading
```

使用叶子页面包：`content/reading/slug/index.md`，图片放在同目录 `images/`，可选封面为 `cover.svg`。新增文章后，栏目列表和首页最新精读自动更新，不需要再次改导航或模板。

前置字段包括标题、日期、简介、主题 `topics`、原作信息 `source`、核对状态 `review_status`、核对日期 `reviewed_at` 和读者问题 `questions`。`interactive` 和 `stats` 可选；没有交互版的文章不会显示交互入口。草稿默认 `draft: true`，内容准备好后再改成 `false` 或移除此字段。

保留这条阅读路径：原文主张 → 推理环节 → 关键英文与中文 → 证据口径与反例 → 自己的判断。明确区分作者观点、已观察数据、未来情景、教学假设与独立推导。不要用“已核对”代替具体核对范围。

## 双语摘录

如使用 `reading-quote` shortcode，在页面包中保存 `quotes.json` 数组，每项包含 `id`、`title`、`page`、`en`、`zh`。`source.pdf` 应指向原作者公开的 PDF。引用方式：

```text
{{< reading-quote id="q1" >}}
```

模板会为英文和中文提供原文页码链接；缺少摘录或资源时构建会报错。摘录应检查原文上下文，中文应校译；没有 PDF 页码时直接在 Markdown 中使用双语段落和原网页链接。

## 可选交互版

交互版放在 `static/reading/slug/explore/`，正文仍保留 Hugo 原生文章，以便搜索、RSS、分享预览和无 JavaScript 阅读。

可以将已审阅的独立 HTML 导出为公开版：

```bash
python3 scripts/import-reading.py \
  --html '/绝对路径/已审阅的精读.html' \
  --slug commanding-heights \
  --source-url 'https://commanding-heights.com/' \
  --pdf-url 'https://commanding-heights.com/commanding-heights.pdf' \
  --published-at 2026-11-09
```

脚本将内嵌图片提取为可缓存文件，去重，并把本地 PDF/Markdown 链接改成公开原作或文章锚点。它仅导出指定 HTML，不会复制同目录的全文翻译、原始文档或个人笔记。脚本面向本项目当前精读 HTML 格式；其他结构需核对映射后再使用。公开版日期须显式提供，站点域名可通过 `--site-url` 修改。

原作提供公开链接时优先链接原站。公开版删去个人文件路径与对话语境；图表注明页码、单位、实际/预测区间、数据来源和复现限制。不要把整个 Obsidian 文件夹直接复制到公开目录。

## 复核与发布

1. 回查原文：重要限定、反方向论据、结尾、图表与脚注都要覆盖。
2. 对关键数值追溯一次来源；无法确认的部分明确标注，并记录核对截止日期。
3. 运行 `hugo --gc --minify`；检查 `/reading/`、文章、交互版、`/reading/index.xml`、搜索与深色/移动布局。
4. 查看 `git diff`，确认只包含本次内容和栏目改动。仓库中已有其他未提交内容，勿顺带提交。
5. 按本次任务已授权的发布范围提交与推送。远端现有流程在 `main` 收到 push 后发布预览，推送 `v*` 标签才发布正式站点；使用现有流程，不新增部署渠道。

需要修改已发布判断时，在文末记录日期、改了什么及依据，保留未确认事项。`reviewed_at` 表示实际复核日期，不要自动随构建刷新。
