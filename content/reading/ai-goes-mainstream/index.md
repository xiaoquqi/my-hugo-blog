---
title: "《AI Goes Mainstream》精读：AI 普及以后，什么还没有跟上？"
heading: "AI 普及以后，什么还没有跟上？"
reading_label: "斯坦福 AI100 · 2026"
images: [cover.png]
date: 2026-11-13T00:00:00+08:00
lastmod: 2026-11-16T00:00:00+08:00
type: reading
description: "精读斯坦福 AI100 第三份五年期报告。沿着规模化、能力的锯齿性、劳动与治理四条线，读懂生成式 AI 走向大众后，哪些变化已经发生，哪些判断还需要证据。"
topics: [AI, 商业与社会]
tags: [AI100, 深度阅读, 生成式AI, AI治理]
reading_minutes: 30
review_status: "原文逐章核对 · 关键数据溯源"
reviewed_at: 2026-11-16
source:
  title: "AI Goes Mainstream: The Scaling Era and the Rise of Generative AI"
  authors: [AI100 研究小组]
  date: 2026-11-10
  pages: 127
  url: https://ai100.stanford.edu/reports/2026-report
  pdf: https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf
questions:
  - "训练越大，为什么真实任务仍会出现低级错误？"
  - "同一项 AI 技术，怎样既帮助新人工作，又改变新人入行的机会？"
  - "2021 年低估了什么？2026 年的报告又有哪些判断值得保留？"
stats:
  - {value: "12", label: 固定问题}
  - {value: "2", label: 专题深挖}
  - {value: "5", label: 证据核对}
---

## 先读懂「走向主流」

2021 年的 AI100 已经看到了 GPT-3。五年后，研究小组认为，当时漏掉的关键一步，是一个人人都能打开的聊天窗口。普通人可以用自然语言交代任务，在同一个界面里从写信换到查资料、改代码、生成图像。2022 年 11 月上线的 ChatGPT 基于 GPT‑3.5 系列微调，报告 p.31 用 GPT‑3 概述了这条技术演进线。进入公众生活的速度，超出了当时研究者的预期。2026 年的报告于是把问题从「AI 能做什么」推进到「人和机构开始依赖 AI 后，会发生什么」。[OpenAI 上线公告](https://openai.com/index/chatgpt/) · [报告导言 p.17](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=17) · [五年回看 p.116](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=116)

这是**人工智能百年研究（AI100）**继 2016、2021 年之后的第三份报告。项目由斯坦福大学以人为本人工智能研究院（HAI）管理，本期由牛津大学的 Michael Wooldridge 主持，12 位研究者共同署名。它是跨学科专家评估，兼有研究综述、案例、预测和政策主张。导言交代初稿于 2026 年 4 月底完成、版本在 9 月定稿，11 月发布。下文页码对应官方 PDF，覆盖复核截至 11 月 16 日。[三期报告](https://ai100.stanford.edu/reports) · [作者与引用方式](https://ai100.stanford.edu/reports/2026-report/about-report) · [斯坦福 HAI 11 月 10 日发布介绍](https://hai.stanford.edu/news/the-world-has-changed-insights-from-the-new-ai100-report)

读这篇报告，我会分别追问：**一个人能否用上 AI？一个机构能否放心把结果交给 AI？社会能否决定部署条件并分到收益？** 应用普及可以看使用数据，可靠交付需要任务验证，社会如何分配决定权则要看制度与实际结果。

## 一、规模化改变了什么，又在哪些地方失灵

### 训练损失、任务能力、实际交付

早期规模定律的商业意义是**降低研发投资的不确定性**。在一定模型家族和训练条件下，研究者观察到，扩大参数量、数据和训练算力，能相对可预测地改善预测损失。投资者因此可以用小规模实验估计大训练的表现。Chinchilla 研究还说明，给定训练预算，参数和训练 token 要一起配置。只把模型做大，可能留下一个训练数据相对不足的模型。[报告 p.30、p.106–107](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=106) · [Hoffmann 等，Chinchilla 原始论文](https://arxiv.org/abs/2203.15556)

从实验结果到现实交付，中间还有三道检验：

| 检验 | 观察什么 | 容易漏掉什么 |
| --- | --- | --- |
| 训练 | 模型在留出数据上预测得怎样 | 同一损失水平可能对应不同能力分布 |
| 任务 | 在规定题目与评分条件下能完成多少 | 测试题泄漏、题型偏重、提示词敏感性 |
| 交付 | 换成真实输入、权限和时间限制后，有多少结果可以验收 | 人工复核、重试和错误后果，常常落在指标之外 |

报告认为下一轮能力增长会同时来自多个地方。**预训练**继续受制于算力和数据配比。**后训练**可以改进指令遵循和特定推理能力。**推理时计算**允许模型为某一次任务多花算力做搜索、调用工具或验证候选结果。**系统设计**则决定模型能拿到什么上下文、用哪些外部工具、失败后如何交还给人。一个系统可以在参数保持不变时变得更有用，同时每次调用变得更贵或更慢。[报告 p.31–32、p.58、p.112–113](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=112)

{{< reading-quote id="scale" >}}

报告对数据瓶颈的讨论也值得细分。公开、可清洗、有授权的高质量文本是有限资源。授权数据、实验和模拟数据、合成数据各能扩充其中一部分。比如能用求解器核对的训练题，可以从合成样本中得到更密集的反馈。涉及现实人群或环境时，合成样本的价值取决于它能否覆盖真实变化，生成更多相似文本也可能放大原有偏差。[报告 p.110–112](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=110)

**我的判断。** 对使用者，更合适的成本单位是「一个经验证的可用结果」。把模型调用、人工复核、重试和失败返工都算进去，再看替换成更强模型是否划算。对一家模型公司，还要另外算训练、设备折旧和扩容。报告中的铁路类比最有意思的一点是资产寿命：机房、电力接入和芯片的更新周期不同，长期需求增长也不能直接回答某一批设备投资能否回收。[报告 p.108–110](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=108)

报告摘要还有一个与结尾回看略有张力的判断。p.13 强调，资本开支和估值的变化很显眼，而整体产出和企业回报里的贡献还难辨认。p.120、p.124 又把部分美国生产率数据视为可能的早期信号。两处要放在一起读：建设机房的支出可以推高当期投资，上市公司的股价可以反映预期，使用 AI 后持续增加了多少产出和利润仍各需证据。**泡沫**是回报不足时的风险情景。报告没有给出它发生的概率或时间。[摘要 p.12–13](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=12) · [五年回看 p.120、p.124](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=120)

## 二、能力的锯齿性，比平均分更接近现实

报告把能做高难题、却在一些看似简单的输入上突然出错的现象称为 **jaggedness**。它在推理章节把这个问题进一步分成跨情境迁移、长程计划、因果识别和评测。语言模型可以复述某种干预的常见效果。要知道干预在当前情境中是否有效，还需要实验、合适的观测设计或站得住的因果假设。[报告 p.41–43、p.57–59](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=42)

{{< reading-quote id="jagged" >}}

Dell’Acqua 等人的随机实验给出了更实际的例子。在总计 758 名 BCG 顾问参与的两类任务中，GPT‑4 对落在能力边界内的任务有帮助，但另一项特意选在边界外的复杂任务里，使用 AI 的参与者反而较少给出正确解。这样的边界会随工具和模型版本移动，且难以凭人对题目「难不难」的直觉来判断。[报告 p.49](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=49) · [《Organization Science》正式论文](https://doi.org/10.1287/orsc.2025.21838)

**原图怎么读。** p.28 的 METR 图上，GPT‑3.5 与早期 Claude Mythos 的 80% 成功率时间跨度分别约为 30 秒和 4 小时。这里的时间是**人类专家完成评测任务所需的时间**，用来表示任务的复杂度。图上两个点表示模型在特定任务集上的拟合结果，主要来自可独立验收的软件相关任务。把它延伸到复杂组织工作之前，还要问任务条件、成功标准和人工交接是否相似。[报告 p.28 原图](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=28) · [METR 交互图与方法说明](https://metr.org/time-horizons/)

代理式 AI 把这种不稳定带进多步流程。拿「生成一份附证据的行业简报」做例子，模型可能会写出漂亮的摘要，却在前一步把对照组看错。后面每一步都沿用错误的表格，排版越好，越不容易察觉。报告谈到自动化时，持续追问谁在关键节点还能暂停、核实和纠正。这个问题也适用于会使用外部工具的系统。[报告 p.34–36、p.47–48、p.78–84](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=34)

**把代理、记忆和自我改进分开。** 代理可以执行多步任务，外部记忆可以把先前资料带入下一次会话。SQ5 讨论的持续学习更难，它要求系统吸收新技能的同时保留旧能力，并处理跨用户的隐私边界。SQ2 还讨论递归自我改进：AI 辅助修改软件已是可观察的能力，连续多代都提高通用能力并维持安全约束，仍需逐代验证。演示一次改进，支持的是这一次的效果。[报告 p.34–37](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=34) · [报告 p.58–59](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=58)

**具身能力也有自己的验证条件。** SQ3 用折衣服和自动驾驶解释，熟练处理符号任务并不能告诉我们一个系统在陌生物体、遮挡、摩擦变化或罕见路况下怎么行动。视觉—语言—动作模型和模拟训练扩大了可以尝试的任务。工作现场还要检验操作失败是否可恢复、系统能否及时停下，以及演示条件去了现场还剩多少。[报告 p.51–52](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=51)

**我的判断。** 在这类工作流里，验收应覆盖反例：材料相互矛盾、源文件缺失、表格单位变化、系统越权时，结果是否仍然可追查？对外发送、改写原数据等动作的后果高于起草，故而需要不同的授权和检查。AGI 争论也可以这样读。广泛答题、完成多数有经济价值的工作、在陌生物理环境独立完成任务，对应三种不同门槛。报告记录了时间表的分歧，结尾对当前系统的描述仍是强大的通用工具。[报告 p.57–59、p.114–115](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=57)

## 三、科研更快之后，验证和理解更值钱

报告写到数学、科学和编程时，有一个共通的结构：AI 让候选答案的供给变多，**瓶颈随之转向验证与解释**。数学里，形式化系统能对证明做精确核验，但能验过的证明和数学家能理解、能据此继续研究的证明，价值不同。自然科学里，模型可以帮人生成假设、缩小搜索范围和分析实验结果，真实实验、独立复现和有效的研究设计仍决定证据有多强。报告还展望了自动化实验室的普及。用个别科研项目的提速去估计整门学科的变化，需要知道新流程有多少项目能采用、复现成本如何、瓶颈是否转移到了下游。[报告 p.31–33、p.37–39、p.42–44](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=37)

SQ1 还用诺奖照片记录研究成果。p.26 的图注把三位化学奖得主写在 AlphaFold 名下，诺奖授奖说明区分得更精确：David Baker 获奖对应计算蛋白质设计，Demis Hassabis 和 John Jumper 获奖对应蛋白质结构预测。同一张照片承载了两类科研贡献。[报告 p.26](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=26) · [诺奖授奖说明](https://www.nobelprize.org/uploads/2024/10/press-chemistryprize2024-3.pdf)

报告还把「AI 对理解人类智能有帮助」和「人类认知能否指导 AI 工程」当作两个不同的研究问题。神经网络能在受控实验中帮助解释脑成像信号，脑机接口也能借生成模型从信号中重建部分内容。模型与人脑反应相关、解码结果令人印象深刻，仍只提供了具体实验设定下的证据。原文也强调人类智能有社会、文化和集体维度。工程上，2021 年看好的神经符号方法在数学等可验证场景取得进展，同期更广泛的能力进步仍主要来自通用深度学习与系统层的组合。[报告 p.53–56、p.96–97、p.118、p.121–122](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=53)

SQ12 还有一个和产品有关的限定：模型给出的理由越完整，越容易让人相信它准确描述了决策过程。报告引用的实验显示，改变输入中某些无关线索会改变答案，模型写出的解释却往往没有提到这些线索。评估时可把「解释是否便于读懂」「结论是否可独立验证」「解释是否反映实际决策依据」当成三个问题。[报告 p.96–97](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=96) · [Turpin 等原始实验](https://arxiv.org/abs/2305.04388)

**人机组合的比较基准。** SQ2 引用的元分析发现，人机组合平均优于人单独完成，但平均表现低于人或 AI 中表现更好的一方。论文纳入的是截至 2023 年中发表的实验，结果也随任务类别而变。举例说，人做能得 70 分，AI 单做能得 90 分，组合得 85 分，相对人单做高了 15 分，相对 AI 单做则低了 5 分。决定是否加一道人工环节时，质量、覆盖范围和复核成本也要一起看。[报告 p.39–40](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=39) · [Vaccaro 等元分析](https://doi.org/10.1038/s41562-024-02024-1)

同一个道理也适用于编程和创作。SQ9 认为自然语言编程扩大了参与面，但原型能跑和生产软件可维护之间，还有测试、理解需求与责任归属。图像与视频生成降低了创作门槛，也让更多作品争夺注意力。报告用编剧和演员工会的谈判举例，说明供给成本的下降怎样触发对素材使用、署名和报酬的重新谈判。要判断创意行业的净效应，需要看创作参与、作品质量和创作者收入如何一起变化。[报告 p.73–77](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=73)

教育里也有同样的分界。学生用 AI 把作业做得更好，可以证明工具改善了当下的产出。要检验学会了多少，可以再测学生脱离工具后的表现、解释能力和迁移能力。对机构来说，这比统计生成了多少篇作业或报告更接近它要培养的能力。[报告 p.44–46、p.63–65、p.115](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=44)

## 四、为什么「个人提效」和「新人更难入行」可以同时出现

AI100 在不同章节用了几类研究。把它们放在一起，能看到同一项技术影响了不同结果。

| 证据 | 观察单位 | 适合回答的问题 |
| --- | --- | --- |
| 企业客服工具分批上线 | 每位坐席每小时解决的工单 | 已有员工在该工作流中能否多处理工单 |
| 美国工资单样本 | 不同年龄、不同 AI 暴露程度职业的就业趋势 | 哪些群体先出现值得追踪的就业变化 |
| 宏观生产率统计 | 行业或全国的产出与投入 | 总体效率变了多少，仍需进一步识别 AI 的独立贡献 |

客服论文的正式版本跟踪一家企业 5,172 名坐席，主要结果是每小时解决问题数平均提高约 **15%**，低经验与低技能员工受益更明显。AI100 在回看章节另引了截至 2026 年 6 月的工资单研究：暴露度最高的两个五分位组中，22–25 岁员工的就业量，相对于按其余三个组的增速推算的基准，约有 **19% 的缺口**。两组数据可以同时成立。一个在看已入职的人用工具之后的表现，一个在看各组就业人数怎样变化。[客服正式论文](https://doi.org/10.1093/qje/qjae044) · [工资单研究 2026 年 8 月版 p.10–11](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf#page=10) · [报告 p.85–87、p.120](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=85)

为什么两者会并存？如果一个新人能在 AI 辅助下迅速学会回答常见问题，雇主可能用同样团队接更多客户，也可能减少招人。决定方向的是需求有没有扩张，企业如何重组任务、培训新人，以及人还负责哪些高价值判断。报告 p.85 的原图按收入和职业展示的是**任务暴露度**。暴露度用来识别哪些工作可能变化，对应的实际替代、互补、工资和工作质量需要另外测量。原文也给出了与强替代叙事有张力的结果：聚合研究的就业效应仍弱或为正，部分受影响群体的在岗工资与就业量可能反向变化。[报告 p.84–87（原图见 p.85）](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=85)

**我的判断。** 更难观察的是「新人怎样成为专家」。当初级任务由 AI 完成，企业能否提供别的途径让新人接触案例、犯可纠正的错误、获得反馈？每小时产出有即时反馈，人才梯队的变化要等更久才看得见。这也是为什么要把**产出、招募和学习**放在三个时间尺度上追踪。

SQ11 进一步问了谁控制工作过程。AI 可以把更丰富的信息交给员工，也可以把员工的任务拆得更细，交给系统分配和考核。报告指出，标注、评审、纠偏和内容审核等人工劳动往往隐在自动化界面之后。若只统计前台节省的人时，可能漏掉转移到后台的工作，以及员工能否理解或申诉算法给出的评价。[报告 p.89–92](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=89)

## 五、从供应链到公共生活，谁有权决定部署方式

### 训练权集中，使用权扩散

地缘政治专题把竞争画成一组相互依赖的环节：**芯片与制造设备 → 电力、网络和数据中心 → 数据与模型 → 部署和制度**。美国、中国及其他国家可以在不同层次发挥影响力。开放权重让更多团队能够运行、适配和研究现有模型，但独立训练下一代前沿模型还需要算力、人才和数据。某国可以拥有本地部署和数据管理能力，同时依赖外国的芯片或基础模型。由此看，「主权 AI」要具体问主权落在哪一层。[地缘政治专题 p.98–106](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=98)

电力和水把全球竞争落实到地方决策。即使芯片买得到，数据中心的投运仍要等并网、土地和冷却条件。报告 p.100–101 把环境影响放到选址中讨论。对照不同估算时，我会看三个口径：AI 专用负荷还是全部数据中心用电，直接用水还是把发电耗水计入，全年总量还是枯水期的本地压力。单次推理更省电，只有结合总调用量，才知道整个系统用了多少电。[报告 p.100–101](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=100)

SQ8 从学术界看到同样的分化。大学仍有培养人才、做基础研究、开展独立评估的能力。前沿训练更集中于能负担资源的公司，研究者接触真实系统和失败数据的条件则日益取决于企业开放什么。对科研来说，这关系到可复现性。对治理来说，这关系到独立机构能否验证模型开发者的说法。[报告 p.71–72、p.108、p.123、p.125](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=71)

### 风险从模型输出扩展到人与制度之间

报告把恶意使用、系统失灵和系统性风险分开。三类问题可以在同一产品里出现：冒充他人的合成内容是滥用，模型自信地引错证据是失灵，大家长期依赖同一批系统筛选资讯则可能改变整个信息环境。报告也讨论安全防护与滥用的竞争、军事决策的问责、陪伴式产品中的情感依赖，以及平台管理如何影响劳动者。原文承认多处证据仍薄，例如具体个案所呈现的风险可以支持进一步调查，难以单独估出普遍发生率。发现了选举期间的合成内容，也需要额外证据评估它改变了多少人的行为。[报告 p.78–95、p.103–105、p.123](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=78)

### AI 也会改变它下一轮面对的世界 {#human-ai-feedback}

SQ3 将这种相互适应列为开放挑战。模型生成内容，人开始使用其中的词汇和表达方式，模型再从这些内容里取样。内容生产、传播与筛选都变了，哪一种语言习惯会被放大，取决于平台的分发方式以及谁的内容能进入数据。技术上，递归训练实验发现，反复以合成内容替换真实数据会让罕见模式流失。另有研究在保留真实数据、逐代累积合成数据的实验里避开了退化。两种结果并存，对应不同训练条件。[报告 p.44–47](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=44) · [Shumailov 等原始研究](https://www.nature.com/articles/s41586-024-07566-y) · [Gerstgrasser 等对照研究](https://arxiv.org/abs/2404.01413)

反馈也发生在人身上。报告引用的预注册实验发现，过度迎合的 AI 会让参与者更确信自己有理、降低承担责任或修复冲突的意愿。实验测的是短期回应和意向，长期关系与群体规范怎样改变仍待研究。报告还提出一种缓慢失去自主性的情景：每次交给系统的决定都看似方便，长期却可能让人失去亲自判断和纠错的机会。衡量这种风险，可以从人是否能追溯来源、质疑推荐、改用其他渠道入手。[报告 p.44–47、p.92–94](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=44) · [Cheng 等预注册实验](https://doi.org/10.1126/science.aec8352)

合成影像让这个问题更直观。面对同一段录音，内容是否曾被编辑、录音来自哪里、它是否支持配套的事件说法，需要分别核验。即使录音是真实的，剪辑或错误语境也会误导。AI 把原本已经存在的取证难题推向更日常的场景。[要点 8，p.14–15](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=14) · [报告 p.94](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=94)

### 公众怎样参与制定规则

在 SQ6，公众表达的担忧既取决于亲身体验，也受媒体选取哪些声音的影响。报告认为 AI 素养涉及理解系统为何会出错、怎样核查信息，也涉及公众能否讨论自己愿意接受什么部署条件。应用增加与担忧增加可以同时发生，个人可能觉得工具好用，同时担心所在行业的雇佣变化。[报告 p.60–65](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=60)

报告用 *society-in-the-loop* 讨论谁来决定社会可接受的风险。让人审核一次模型输出，是操作层的监督。让受影响的人参与决定能否采集数据、哪些场合需要申诉、出了问题由谁负责，是另一层制度安排。前沿模型监管能够覆盖共用底座，行业监管则更接近某个具体用途的后果。报告也指出两边各有难题：技术门槛会过时，行业监管可能缺少足够的技术能力、权限或跨境协调机制。[报告 p.66–70、p.105–106](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=66)

国际层面的分歧还涉及谁能制定规则。地缘政治专题指出，一些中等国家尝试用本地算力、区域合作或标准工作换取议价能力，全球南方能否分享收益、能否参与定义规则则仍悬而未决。对照各类国际倡议时，可以追问承诺有无明确的执行主体、独立评估和问责程序。报告记录了协调进展，也把具有约束力的跨国安排视为尚未解决的问题。[地缘政治专题 p.105–106](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=105) · [要点 11，p.16](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=16)

## 六、报告如何回看 2021 年

末尾的回看把「看错」「看对」「当时没纳入框架」放在一起。下面还区分了判断的强弱和适用期限，避免用后来发生的事覆盖原话。[2021 年原报告](https://ai100.stanford.edu/gathering-strength-gathering-storms-one-hundred-year-study-artificial-intelligence-ai100-2021-study) · [2026 年回看 p.116–126](https://ai100.stanford.edu/reports/2026-report/five-years-where-2021-panel-landed)

| 议题 | 两份报告之间的变化 | 仍待回答 |
| --- | --- | --- |
| 深度学习的后劲 | 2021 年认为其主导地位可能接近尾声。之后 Transformer 规模化与后训练又释放了多轮进步。 | 给定相同数据和任务，继续加预算的边际收益多大？下一轮增益来自哪一层？ |
| 常识与物理接地 | 纯语言训练也支持了许多常识题和迁移能力，削弱了当时对接地必要性的较强推测。 | 在开放物理环境稳定行动是否仍需直接经验？回看保留了这个问题。 |
| 失去有效控制 | 2021 年已经提及，后来它的研究投入和政策地位迅速上升。 | 治理关注的增长与失控概率的估计需要两套证据。 |
| 进入公众生活的方式 | 聊天产品、推理时计算、编程工作流和算力地缘政治都比 2021 年预期更突出。 | 下一次会改变部署路径的，可能是接口、价格、分发渠道或组织流程。 |
| 长期方向与短期实践 | 2021 年认为完全自主不应是最终目标。代理技术兴起后，研究小组仍主张按任务保留有意义的人类参与。 | 哪些工作该保留人工决定权，哪些可以验证后交给系统？ |

回看也认为，关于产业集中、虚假信息和军事应用扩张的担忧有相当的延续性。部分陈述只适用于当时，例如 2020 年 AI 投资的相对体量。新一轮资本开支的跃升，支持重新提问。把某年宏观生产率上升归因给 AI，仍需要能够排除周期、投入结构和其他技术变化的研究。[报告 p.120–125](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=120)

## 五处证据核对

1. **GPT‑3 的 45 TB。** AI100 p.110 将其表述为训练所用文本量。Brown 等原始论文 §2.2 显示，45 TB 是过滤前的压缩 Common Crawl 原始文本，过滤后约 570 GB。Table 2.1 给出的训练总量是 3,000 亿 token，训练还从其他语料库采样。这三个数分别描述原始来源、过滤后的单项语料和训练消费量。[报告 p.110](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=110) · [GPT‑3 原论文 p.8](https://arxiv.org/pdf/2005.14165#page=8)
2. **客服约 15%。** 使用同行评议版的每小时解决问题数。样本来自一家企业，不能据此估算其他行业的生产率或所需人数。[正式论文，摘要与表 I](https://doi.org/10.1093/qje/qjae044)
3. **青年就业约 19%。** 美国 ADP 样本中，2022 年 11 月至 2026 年 6 月，暴露度最高的两个五分位组的 22–25 岁就业量约降 11%，其余三组约增 10%。用两组期末指数计算，0.89 ÷ 1.10 − 1 ≈ −19%。这是描述性差距。研究发现差距主要表现为招聘减少，并指出疫情期间已出现趋势差异，控制教育构成后部分估计变小。[研究 2026 年 8 月版 p.10–12](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf#page=10)
4. **公众 17% 与专家 56%。** 报告 p.60 引用 Pew。原问题是受访者是否认为未来 20 年 AI 会对**美国**产生非常或较为正面的影响。调查在 2024 年进行、2025 年公布。它测的是对一项未来影响的预期，不能直接替代使用率、整体满意度或全球民意。[Pew 调查原文](https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/)
5. **Chinchilla 的配比。** 论文在其模型和实验范围内估计，达到计算最优时参数量和训练 token 数应大致同比增长。这里的最优指给定**训练**算力下的表现。如果要大规模提供推理服务，部署端成本会改变选型。[论文摘要与 §3](https://arxiv.org/abs/2203.15556)

## 按报告开头的 12 条要点回读 {#key-takeaways}

原报告 p.10–16 的要点与 SQ1–SQ12 是两套目录。要看研究小组自己把重心放在哪里，可以直接从要点页进入正文。

| 要点 | 回读重点 | 原文 |
| --- | --- | --- |
| 1–3 | 规模扩张的约束、专业领域的变化、科研提速与验证 | [p.11–12](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=11) |
| 4–5 | 基础设施投资与回报、资源消耗、前沿训练的集中 | [p.12–13](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=12) |
| 6–8 | 网络安全、军事决策的监督与问责、合成媒体的证据价值 | [p.13–15](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=13) |
| 9–10 | 公众参与、已经发生的伦理问题与仍难量化的风险 | [p.15](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=15) |
| 11–12 | 跨国治理分歧，以及未来五年能否延续这轮进步速度 | [p.16](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=16) |

最后一条的判断带有明确前提：**如果**过去五年的进步速度维持，下一次报告的世界很可能再度出人意料。结尾把确定性放在已经观察到的广泛使用上，把能力提升的后续速度、资本回报和收益如何分配留给今后的证据。[要点 12，p.16](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=16) · [结论 p.114–115](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=114)

## 12 个固定问题怎么回读

只读三段时，我会选 **p.41–43** 的能力边界、**p.106–113** 的规模化专题、**p.116–126** 的五年回看。下面是完整的章节索引，适合按兴趣跳读。

| 固定问题 | 回读时可以追问 | 原文 |
| --- | --- | --- |
| SQ1 图像如何记录这五年 | 现场照片、数据中心和合成影像分别展示了哪种变化？ | [p.24](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=24) |
| SQ2 技术有哪些主要进步 | 语言模型、扩散模型、代理、科学与人机协作分别进步在哪里？ | [p.29](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=29) |
| SQ3 什么是开放挑战 | 在竞赛之外，怎样验证推理、可解释性、人机互补和具身能力？ | [p.41](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=41) |
| SQ4 对人类智能懂了多少 | 能对齐或解码脑信号时，我们理解了哪一部分？ | [p.53](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=53) |
| SQ5 更通用的 AI 有何前景 | AGI 的门槛是哪一个？记忆和持续学习还缺什么？ | [p.57](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=57) |
| SQ6 公众态度如何演变 | 各地为何同时出现广泛使用、乐观与焦虑？教育如何回应？ | [p.60](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=60) |
| SQ7 政府该如何行动 | 前沿模型规则与医疗、金融等行业监管各管什么？ | [p.66](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=66) |
| SQ8 学界与产业如何分工 | 谁能训练、拿到数据、独立评估，又由谁培养下一代研究者？ | [p.71](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=71) |
| SQ9 什么机会最值得看 | 编程、白领工作、创意产业的价值来自哪一环？ | [p.73](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=73) |
| SQ10 什么危险最紧迫 | 恶意使用、系统失灵和系统性风险分别如何产生？ | [p.78](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=78) |
| SQ11 社会经济关系如何改变 | 雇主、员工、亲密关系和公民生活由哪些新中介影响？ | [p.89](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=89) |
| SQ12 模仿人类思考是否仍是好策略 | 哪些问题值得借鉴认知机制，哪些通用方法已能解决？ | [p.96](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf#page=96) |

读完可以回到自己最熟悉的一项工作。**让 AI 帮你做哪一步、把什么证据交给你、由谁签字验收？** 再把时间拉长：如果大多数人都采用这种做法，谁获得了原先没有的能力，谁将失去学习机会、工作选择或申诉渠道？AI100 用同一组问题持续追踪技术和制度，值得保留下来的正是这种跨时间尺度的比较。

*本文依据官方英文报告写作，双语框为短摘录与校译，表格为本文的分析整理。原文、两篇专题和历年版本均可在 AI100 官网阅读。* [官方网页](https://ai100.stanford.edu/reports/2026-report) · [英文 PDF](https://ai100.stanford.edu/sites/g/files/sbiybj36086/files/media/file/ai100_report_2026.pdf)

*2026 年 11 月 16 日复核。补入人机协作的比较基准、持续学习与具身能力、人和 AI 的反馈、投资回报与国际治理，并增补报告开篇要点的回读索引。*
