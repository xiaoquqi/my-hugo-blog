---
title: Github开源项目趋势周报2023-09-11
date: 2023-09-12T09:02:56+08:00
slug: "github-trendings-weekly-20230911"
author: 老孙正经胡说
tags:
  - Github
  - OpenSource
categories:
  - Github
  - ChatGPT
draft: false
---

根据Github Trendings的统计，本周(2023年9月11日至2023年9月17日)共有25个项目上榜。根据开发语言中项目的数量，汇总情况如下：

* Python项目：KillianLucas/open-interpreter，XPixelGroup/DiffBIR，OpenBMB/ChatDev，guoyww/AnimateDiff，baichuan-inc/Baichuan2，microsoft/promptflow，facebookresearch/nougat，aigc-apps/sd-webui-EasyPhoto，ECTO-1A/AppleJuice，fishaudio/Bert-VITS2，srbhr/Resume-Matcher
* C++项目：oven-sh/bun，godotengine/godot，facebook/react-native，SoftFever/OrcaSlicer
* TypeScript项目：openai-translator/openai-translator，srbhr/Resume-Matcher，tldraw/tldraw
* 非开发语言项目：krahets/hello-algo，modularml/mojo
* Java项目：FIRST-Tech-Challenge/FtcRobotController，facebook/react-native
* Zig项目：oven-sh/bun
* Dart项目：mylxsw/aidea
* Rust项目：aripiprazole/rinha-de-compiler
* JavaScript项目：microsoft/Web-Dev-For-Beginners
* C项目：Flipper-XFW/Xtreme-Firmware
* Go项目：apernet/hysteria

## facebook/react-native

* 主要开发语言：Java, C++
* 当前Star数量：111986
* 贡献者数量：321
* Open Issues数量：1654


这是一个使用React构建原生应用的框架。React Native将React的声明式UI框架引入iOS和Android。使用React Native，您可以使用原生UI控件，并完全访问原生平台。它具有声明性、组件化、开发速度和可移植性的特点。React Native由许多公司和个人核心贡献者开发和支持。

该项目的使用场景包括：
- 构建跨平台的移动应用程序：React Native允许开发人员使用相同的代码库构建iOS和Android应用程序，从而节省开发时间和成本。
- 快速迭代和调试：React Native支持实时重新加载，使开发人员能够在几秒钟内查看本地更改，加快开发速度。
- 组件化开发：React Native采用组件化开发的方式，使开发人员可以构建可重用的UI组件，并通过组合这些组件来创建复杂的用户界面。
- 原生性能：React Native使用原生UI控件，可以获得与原生应用程序相似的性能和用户体验。
- 社区支持和生态系统：React Native拥有庞大的开发者社区和丰富的生态系统，可以获取支持和共享开源组件。

该项目的要求是目标iOS 13.4和Android 5.0（API 21）或更高版本，开发操作系统可以是Windows、macOS或Linux。可以使用工具如Expo来解决在macOS上构建和运行iOS应用程序的限制。

要开始构建React Native应用程序，请按照[入门指南](https://reactnative.dev/docs/getting-started)进行操作。根据项目需求，可以选择不同的安装方式。文档提供了对React Native的完整介绍和详细的API文档。升级React Native可以获得更多的API、视图和开发工具。

如果您希望贡献React Native项目，可以阅读贡献指南和行为准则，了解开发流程和如何提交bug修复和改进建议。同时，项目还提供了一些适合初学者的问题，可以帮助他们熟悉贡献过程和获取开发经验。更大范围的讨论和提案可以在社区讨论中进行。

React Native是使用MIT许可证的开源项目，文档使用创作共用许可证。

## microsoft/Web-Dev-For-Beginners

* 主要开发语言：JavaScript
* 当前Star数量：75792
* 贡献者数量：208
* Open Issues数量：66


这个项目是一个为期12周的网页开发入门课程，总共包含24个课程。学习者将学习JavaScript、CSS和HTML的基础知识，并通过实践项目来提高实际技能。课程包括预课和后课测验、详细的书面说明、解决方案、作业等。学生可以通过自学来充分利用这个课程，也可以与同学一起组成学习小组。这个项目的目标是帮助初学者快速入门网页开发，并通过实践项目来加深理解。

这个项目适合学生、教师和自学者。学生可以通过自学这个课程来学习网页开发的基础知识，并获得免费的证书凭证。教师可以使用这个课程来教授学生网页开发的基础知识，并在讨论论坛上提供反馈。自学者可以通过自学这个课程来提高自己的网页开发技能。

这个项目采用项目化学习和频繁测验的教学方法。学生将通过构建项目来实践所学知识，并通过频繁的测验来加深对概念的理解。课程涵盖了JavaScript、HTML和CSS的基础知识，以及当今网页开发者使用的最新工具和技术。学生将有机会通过构建打字游戏、虚拟温室、环保浏览器扩展、太空入侵游戏和面向企业的银行应用程序等项目来获得实际经验。通过这个系列课程，学生将对网页开发有深入的了解。

这个项目的描述中还提到了其他相关的课程，包括AI for Beginners、Data Science for Beginners、IoT for Beginners、Machine Learning for Beginners和XR Development for Beginners。这些课程可以帮助学习者进一步扩展他们的技能。该项目使用MIT许可证。

## godotengine/godot

* 主要开发语言：C++
* 当前Star数量：70536
* 贡献者数量：458
* Open Issues数量：10266


Godot Engine是一个跨平台的2D和3D游戏引擎，提供了一套全面的常用工具，使用户可以专注于制作游戏而不必重新发明轮子。可以将游戏一键导出到多个平台，包括主要的桌面平台（Linux，macOS，Windows），移动平台（Android，iOS），以及基于Web的平台和游戏机。Godot是完全免费和开源的，用户的游戏完全属于他们自己，开发由社区驱动，由Software Freedom Conservancy非营利组织支持。

使用场景：Godot Engine适用于开发2D和3D游戏的开发者。它提供了一套全面的工具，使开发者能够轻松创建游戏，而不必从头开始。它支持多个平台的导出，包括桌面平台、移动平台和Web平台，以及游戏机。Godot Engine是免费和开源的，可以自由使用和修改，用户可以完全控制自己的游戏。它还有一个活跃的社区，提供了文档、示例和其他学习资源，以帮助开发者更好地使用和学习该引擎。无论是个人开发者还是团队开发者，都可以使用Godot Engine来创建各种类型的游戏，从简单的2D游戏到复杂的3D游戏。

![](https://cdn.jsdelivr.net/gh/filess/img8@main/2023/09/18/1695013325299-d587a0e7-2c5d-4239-abb1-957bacc9789a.png)

## oven-sh/bun

* 主要开发语言：Zig, C++
* 当前Star数量：54729
* 贡献者数量：295
* Open Issues数量：1431


Bun是一个非常快速的JavaScript运行时、打包工具、测试运行器和包管理器，集一身。它是一个用于JavaScript和TypeScript应用的全能工具包，以一个名为`bun`的可执行文件的形式提供。它的核心是Bun运行时，它是一个快速的JavaScript运行时，被设计为可以替代Node.js。它使用Zig编写，底层由JavaScriptCore驱动，大大减少了启动时间和内存使用量。Bun的命令行工具还实现了一个测试运行器、脚本运行器和与Node.js兼容的包管理器。与使用1000个`node_modules`的开发环境相比，你只需要使用`bun`。Bun的内置工具比现有的选项快得多，并且在现有的Node.js项目中几乎不需要进行任何更改。

Bun可以在Linux（x64和arm64）和macOS（x64和Apple Silicon）上运行。对于Linux用户，强烈建议使用5.6或更高版本的内核，但最低要求是5.1。对于Windows用户，Bun目前不提供本机的Windows版本，但正在努力开发中。目前可以在Windows子系统中使用以下安装方法。要升级到Bun的最新版本，运行`bun upgrade`命令。Bun会自动发布每个提交到`main`分支的新版本。要升级到最新的测试版本，运行`bun upgrade --canary`命令。

Bun的文档提供了详细的介绍、安装指南、快速入门和命令行工具的使用方法。此外，Bun还提供了运行时、生态系统和API的文档。如果你想贡献代码给Bun项目，可以参考开发指南。Bun的许可证信息可以在许可证页面中找到。

这个项目可以用于加快开发工作流程，或在资源受限的环境（如无服务器函数）中运行简单的生产代码。它的快速启动时间和低内存使用量使其成为一种理想的选择。你可以使用它来构建和管理JavaScript和TypeScript应用，并且它的内置工具比其他选项快得多。它还提供了与现有框架的集成，使你可以在现有的Node.js项目中使用它，而几乎不需要进行任何更改。无论是开发新项目还是迁移现有项目，Bun都可以提供更好的性能和更高效的开发体验。

## krahets/hello-algo

* 主要开发语言：
* 当前Star数量：23171
* 贡献者数量：93
* Open Issues数量：13


《Hello 算法》是一本动画图解、一键运行的数据结构与算法教程，支持多种编程语言。该教程旨在打造一本开源免费、新手友好的数据结构与算法入门教程。通过动画图解和一键运行的源代码，帮助读者理解算法工作原理和数据结构底层实现，并提升编程技能。读者可以在学习过程中互相交流和提问，通常能够在两天内得到回复。如果对读者有帮助，请给项目点个Star支持一下。

## KillianLucas/open-interpreter

* 主要开发语言：Python
* 当前Star数量：23281
* 贡献者数量：27
* Open Issues数量：180


Open Interpreter是OpenAI的代码解释器在您的本地运行的开源实现。它允许语言模型在您的计算机上运行代码，您可以通过终端中的类似ChatGPT的界面与Open Interpreter进行交互。它提供了一个自然语言界面，可以利用计算机的通用功能，如创建和编辑照片、视频、PDF等，控制Chrome浏览器进行研究，绘制、清理和分析大型数据集等。在运行代码之前，您需要批准代码的执行。Open Interpreter克服了OpenAI的Code Interpreter的一些限制，它在您的本地环境中运行，具有完全的互联网访问权限，没有时间或文件大小限制，并且可以使用任何包或库。它将GPT-4的代码解释器的强大功能与您本地开发环境的灵活性相结合。

Open Interpreter的使用场景非常广泛。您可以通过自然语言界面执行各种任务，如图像和视频处理、数据分析、浏览器自动化等。它可以帮助您提高工作效率，简化工作流程，并使编程的好处面向更广泛的受众。无论是初学者还是有经验的开发者，都可以通过Open Interpreter在终端中进行代码交互，从而实现更加直观和便捷的编程体验。无论是进行日常工作还是进行研究和实验，Open Interpreter都可以为您提供强大的支持和灵活的开发环境。

## tldraw/tldraw

* 主要开发语言：TypeScript
* 当前Star数量：19852
* 贡献者数量：119
* Open Issues数量：133


这是一个非常好的白板项目，名为tldraw。它是一个协作性的数字白板，可在[tldraw.com](https://tldraw.com)上使用。该项目的编辑器、用户界面和其他底层库都是开源的，并在此存储库中提供。您可以使用tldraw为您的产品创建一个即插即用的白板，或者作为构建自己的无限画布应用程序的基础。您可以在[tldraw.dev](https://tldraw.dev)上了解更多信息。

使用tldraw在React应用程序中的安装和使用方法，请参考我们的指南[here](https://tldraw.dev/installation)或查看[examples sandbox](https://stackblitz.com/github/tldraw/tldraw/tree/examples?file=src%2F1-basic%2FBasicExample.tsx)。

本地开发时，可以克隆此存储库并安装依赖项。然后运行本地开发服务器，打开`localhost:5420`查看示例项目。开发服务器包含几个示例，演示了自定义tldraw或使用其API的不同方式。要了解更多关于使用tldraw的信息，请访问我们的文档网站[tldraw.dev](https://tldraw.dev)。

该存储库包含四个主要部分：`/apps`包含我们应用程序的源代码，`/packages`包含我们的公共包的源代码，`/scripts`包含用于构建和发布的脚本，`/assets`包含应用程序所依赖的图标和翻译，`/docs`包含[tldraw.dev](https://tldraw.dev)文档网站的内容。

## openai-translator/openai-translator

* 主要开发语言：TypeScript
* 当前Star数量：18313
* 贡献者数量：67
* Open Issues数量：265


基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用是一个使用 ChatGPT API 进行翻译的浏览器插件和跨平台桌面应用。它不仅仅是一个翻译工具，还具有词语润色和摘要功能。它支持三种模式：翻译、润色和摘要，可以在55种不同的语言之间进行相互翻译、润色和摘要。它支持流式传输模式，允许用户自定义翻译文本，并提供一键复制、文本转语音、截图翻译等功能。它适用于所有平台（Windows、macOS 和 Linux），支持浏览器和桌面应用。用户需要先申请一个 OpenAI API 密钥或 Azure OpenAI Service API 密钥，并进行安装和配置，然后就可以使用了。

该项目是一个功能强大的翻译工具，不仅仅是一个简单的翻译插件或应用。它利用了 ChatGPT API 的强大功能，提供了更多的翻译、润色和摘要功能，可以帮助用户更好地进行语言交流和理解。无论是在浏览器上还是在桌面上，用户都可以轻松使用该工具进行翻译和润色，提高工作效率和语言能力。

该项目适用于各种场景，比如在浏览器上阅读外文网页时进行实时翻译、在写作和翻译工作中进行词语润色和摘要、在学习外语时进行互译和语音转文本等。它的功能丰富，操作简单，适用于不同的用户群体，包括学生、翻译工作者、外语学习者等。无论是在学习、工作还是日常生活中，该工具都可以为用户提供便利和帮助，提高语言交流和理解的效率和质量。

## modularml/mojo

* 主要开发语言：
* 当前Star数量：13135
* 贡献者数量：8
* Open Issues数量：182


Mojo是一种新的编程语言，通过将Python语法和生态系统与系统编程和元编程功能结合起来，弥合了研究和生产之间的差距。Mojo还很年轻，但它被设计为随着时间的推移成为Python的超集。我们计划逐步开源Mojo，但它目前变化非常快。我们相信，一个小而紧密的工程师团队在共同愿景下可以比社区努力更快地前进，因此我们将继续在Modular内孵化它，直到它更完整。请参阅[Mojo FAQ](https://docs.modular.com/mojo/faq.html)获取有关此及其他常见问题的更多信息。我们现在已经开放了这个仓库，因为我们希望收集问题并从有权访问Mojo Playground（我们托管的JupyterHub，您可以在其中尝试使用早期版本的Mojo进行编码）的用户那里获得反馈。要访问Mojo Playground，请[在此处注册](https://docs.modular.com/mojo/get-started.html)。然后，当您想报告问题或请求功能时，请[在此处创建GitHub问题](https://github.com/modularml/mojo/issues)。如需一般问题或与其他Mojo开发人员聊天，请查看我们的[Discord](https://discord.gg/modular)。否则，您可以：阅读[Mojo的灵感来源](https://docs.modular.com/mojo/why-mojo.html)、查看[Mojo编程手册](https://docs.modular.com/mojo/programming-manual.html)、阅读我们在[docs.modular.com/mojo](https://docs.modular.com/mojo)上的其他文档。

Mojo是一种新的编程语言，旨在弥合研究和生产之间的差距。它将Python的语法和生态系统与系统编程和元编程功能结合在一起。Mojo的目标是成为Python的超集，并逐步开源。目前，Mojo正在快速变化中，我们鼓励用户通过Mojo Playground提供反馈和问题。Mojo Playground是一个托管的JupyterHub，用户可以在其中尝试使用早期版本的Mojo进行编码。用户可以通过注册来访问Mojo Playground，并在GitHub上创建问题或请求功能。Mojo的灵感来源和编程手册可以帮助用户更好地了解和使用Mojo。此外，用户还可以查看Mojo的其他文档，以获取更多信息。我们相信，通过小而紧密的工程师团队的努力，Mojo可以更快地发展，并在未来实现更完整的功能。

## apernet/hysteria

* 主要开发语言：Go
* 当前Star数量：6994
* 贡献者数量：12
* Open Issues数量：96


Hysteria是一个强大、高速且抗审查的代理工具。它提供了多种模式，包括SOCKS5、HTTP代理、TCP/UDP转发和Linux TProxy，并且不断添加额外功能。它采用自定义的QUIC协议，能够在不稳定和丢包的网络环境下提供卓越的性能。Hysteria的协议伪装成标准的HTTP/3流量，使得检测和封锁变得非常困难。它支持多平台和架构，可以在任何地方部署和使用。Hysteria内置了自定义认证、流量统计和访问控制的支持，易于集成到基础设施中。此外，Hysteria提供了详细的规范和开发者可以贡献和构建自己的应用程序的代码。如果您觉得Hysteria有用，请考虑给它一个星星！

## OpenBMB/ChatDev

* 主要开发语言：Python
* 当前Star数量：5778
* 贡献者数量：9
* Open Issues数量：16


ChatDev是一个通过多智能体协作来创建定制化软件的虚拟软件公司。它由担任不同角色的智能体组成，包括首席执行官、首席技术官、程序员、测试员等。这些智能体通过参加专业的功能研讨会进行协作，包括设计、编码、测试和文档编写等任务。ChatDev的主要目标是提供一个易于使用、高度可定制和可扩展的框架，基于大型语言模型（LLMs），并作为研究集体智能的理想场景。

ChatDev可以通过克隆GitHub存储库、设置Python环境、安装依赖项、设置OpenAI API密钥、构建软件和运行软件来快速开始使用。用户还可以根据自己的需求自定义ChatDev，包括自定义软件开发流程、自定义阶段和自定义角色。

用户可以通过创建自己的定制化ChatDev公司来分享他们的软件。生成的软件包含所有必要的信息，并可以通过创建拉取请求与其他人分享。

ChatDev是一个开源项目，用户可以报告问题、提出疑问、分享工作和做出贡献。项目的代码使用Apache 2.0许可，数据集使用CC BY NC 4.0许可。用户可以通过电子邮件与项目团队联系。

该项目的描述限制为100个字以内，描述了ChatDev是一个通过多智能体协作来创建定制化软件的虚拟软件公司。

该项目的使用场景描述限制为300个字以内，介绍了用户如何通过克隆GitHub存储库、设置Python环境、安装依赖项、设置OpenAI API密钥、构建软件和运行软件来快速开始使用ChatDev。用户还可以根据自己的需求自定义ChatDev，包括自定义软件开发流程、自定义阶段和自定义角色。用户可以通过创建自己的定制化ChatDev公司来分享他们的软件，并可以与其他人分享他们的工作。用户还可以参与项目的开发和贡献。

## facebookresearch/nougat

* 主要开发语言：Python
* 当前Star数量：5029
* 贡献者数量：10
* Open Issues数量：30


Nougat是一个用于学术文档的神经光学理解的实现。它是一个官方的Nougat存储库，用于理解LaTeX数学和表格的学术文档PDF解析器。可以通过pip安装nougat-ocr或从存储库安装。它还提供了一个API，可以生成数据集。通过CLI可以获取PDF的预测结果。可以使用不同的model tag来选择不同的模型。还提供了一个用于生成数据集的命令。可以使用train.py进行训练，使用test.py进行评估。Nougat在英文论文上效果最好，不适用于中文、俄文和日文等其他语言。模型权重使用MIT许可，模型代码使用CC-BY-NC许可。

## mylxsw/aidea

* 主要开发语言：Dart
* 当前Star数量：4669
* 贡献者数量：3
* Open Issues数量：10


AIdea是一款全能型APP，集成了主流大语言模型和绘图模型，支持GPT-3.5/4问答聊天、国产模型通义千问、文心一言、讯飞星火、商汤日日新，以及开源模型Llama2、ChatGLM2、AquilaChat 7B、Bloomz 7B等。此外，AIdea还支持文生图、图生图、超分辨率、黑白图片上色等功能，集成了Stable Diffusion模型，支持SDXL 1.0。该项目使用Flutter开发，代码完全开源。

AIdea的使用场景广泛，可以用于智能问答、语言聊天、图像生成等多种情景。用户可以通过AIdea与AI模型进行对话，提问问题并获得回答。同时，AIdea还支持绘图功能，用户可以使用AI模型生成文生图、图生图等图像，并进行超分辨率处理和图片上色。此外，AIdea还支持稳定扩散模型，可以应用于图像生成领域。

AIdea的开源代码分为客户端和服务端两部分，用户可以根据需要自行下载和使用。此外，AIdea还提供了微信技术交流群、微信公众号和电报群等渠道，方便用户进行技术交流和获取最新信息。

用户可以通过以下链接下载和安装AIdea的Android/IOS APP、Mac/Windows桌面端和Web端。对于IOS国区用户，目前仅Android/IOS APP可用。

AIdea还提供福利活动，用户可以以低于官方价格的优惠价使用GPT-4模型。此外，用户还可以通过微信或支付宝赞助开发者。

总结：AIdea是一款集成了主流大语言模型和绘图模型的全能型APP，支持问答聊天、绘图功能和图像生成等多种应用场景。用户可以通过AIdea与AI模型进行对话，并生成文生图、图生图等图像。AIdea提供了多个平台的下载安装地址，并提供福利活动和技术交流渠道。

## Flipper-XFW/Xtreme-Firmware

* 主要开发语言：C
* 当前Star数量：4325
* 贡献者数量：313
* Open Issues数量：21


该项目是Flipper Zero固件的一个全面改版，集成了许多来自Unleashed的优秀代码。它具有丰富的功能、稳定性和可定制性。用户可以自定义Flipper的界面、协议和其他选项，还可以使用自定义的Asset Packs加载动画和图标。此外，该固件还添加了Bad Keyboard应用程序、更高级的等级系统和许多其他改进和修复。用户可以通过Web Updater、qFlipper Package或Zipped Archive等方式安装该固件。如果用户愿意，还可以自行构建该固件。

该项目的使用场景包括但不限于：
- Flipper Zero用户想要提升设备性能和稳定性，以及获得更多功能和定制选项的用户。
- 需要使用Bad Keyboard应用程序进行USB和蓝牙模式切换的用户。
- 希望通过等级系统解锁更多动画和功能的用户。
- 希望定制Flipper界面、协议和其他选项的用户。
- 希望使用自定义Asset Packs加载动画和图标的用户。

该项目可以满足用户对Flipper Zero固件的各种需求，并提供了更多的功能和定制选项，使用户能够充分发挥设备的潜力。用户可以根据自己的需求选择不同的安装方式，并可以自行构建固件。

## guoyww/AnimateDiff

* 主要开发语言：Python
* 当前Star数量：3586
* 贡献者数量：4
* Open Issues数量：102


AnimateDiff实现了个性化的文本到图像扩散模型的动画效果。该项目提供了GPU内存优化、用户界面、Google Colab等功能，可以用于生成动画。它还提供了训练和推断的设置步骤，并展示了一些最佳结果和社区案例。该项目的论文引用和联系方式也在README中提供。

## srbhr/Resume-Matcher

* 主要开发语言：Python
* 当前Star数量：2484
* 贡献者数量：20
* Open Issues数量：15


该项目是一个开源的ATS工具，用于比较简历和职位描述，并创建一个评分以对其进行排序。它使用Python解析简历和职位描述，提取关键字和关键术语，并使用Qdrant进行向量相似度计算。该项目提供了数据可视化功能和安装指南，还包括Docker支持和贡献者列表。

该项目的使用场景包括：
1.求职者可以使用该工具来优化简历，使其更符合ATS的筛选要求，提高通过率。
2.招聘人员可以使用该工具快速比较候选人的简历和职位描述，找到最匹配的候选人。
3.开发人员可以基于该项目进行二次开发，添加新的功能或改进现有功能。

该项目的主要优势是免费开源、使用简单、功能强大，可以帮助求职者和招聘人员节省时间和精力，提高招聘效率和准确性。

## SoftFever/OrcaSlicer

* 主要开发语言：C++
* 当前Star数量：1982
* 贡献者数量：240
* Open Issues数量：1032


Orca Slicer是一款用于FDM打印机的G代码生成器，支持多种型号的打印机，如Bambu、Prusa、Voron、VzBot、RatRig和Creality等。它具有自动校准、三明治模式、精确壁厚、Klipper支持和更多细粒度控制等主要特点。Orca Slicer是Bambu Studio的分支，它又是PrusaSlicer的分支，PrusaSlicer又是Slic3r的分支。Orca Slicer还包含了来自SuperSlicer的许多功能，并由社区成员设计了Logo。可以通过GitHub发布页面下载Orca Slicer，并且有一个官方的Discord服务器供用户参与社区讨论。

Orca Slicer的安装方法因操作系统而异。在Windows上，需要安装一些运行库；在Mac上，需要下载相应的DMG文件并将应用程序拖到应用程序文件夹中；在Linux（Ubuntu）上，可以通过终端命令进行安装。对于Klipper用户，建议在打印机配置文件中添加一些配置。Orca Slicer采用GNU Affero General Public License第3版许可，感谢所有的赞助商和支持者。

Orca Slicer可以帮助用户生成适用于各种3D打印机的G代码，并具有丰富的功能和灵活的控制选项。用户可以通过下载和安装Orca Slicer来开始使用，并且可以通过参与社区讨论来获取帮助和支持。

## microsoft/promptflow

* 主要开发语言：Python
* 当前Star数量：1232
* 贡献者数量：33
* Open Issues数量：43


Prompt flow是一个开发工具套件，旨在简化基于LLM的AI应用的端到端开发周期，从构思、原型、测试、评估到生产部署和监控。它使得prompt工程变得更加容易，并使您能够构建具有生产质量的LLM应用。

使用Prompt flow，您将能够：
- 创建可执行的工作流，将LLM、提示、Python代码和其他工具链接在一起。
- 轻松调试和迭代您的流程，特别是与LLM的交互。
- 使用更大的数据集评估流程的质量和性能。
- 将测试和评估集成到CI/CD系统中，以确保流程的质量。
- 将流程部署到您选择的服务平台，或轻松集成到您的应用程序代码库中。

## baichuan-inc/Baichuan2

* 主要开发语言：Python
* 当前Star数量：1664
* 贡献者数量：6
* Open Issues数量：79

Baichuan 2 是百川智能推出的新一代开源大语言模型，采用2.6万亿Tokens的高质量语料训练。Baichuan 2 在多个权威的中文、英文和多语言的通用、领域benchmark上取得同尺寸最佳的效果。本次发布包含有7B、13B的Base和Chat版本，并提供了Chat版本的4bits量化。所有版本对学术研究完全开放。同时，开发者通过邮件申请并获得官方商用许可后，即可免费商用。

推理所需的模型权重、源码、配置已发布在Hugging Face，可以通过命令行工具或Python代码的方式进行推理。命令行工具方式可以使用`python cli_demo.py`命令运行，网页demo方式可以使用`streamlit run web_demo.py`命令运行。Baichuan2-13B-Chat模型的示例输出可以在网页demo中查看。

## XPixelGroup/DiffBIR

* 主要开发语言：Python
* 当前Star数量：1652
* 贡献者数量：3
* Open Issues数量：24


这是一个名为DiffBIR的项目，旨在实现具有生成扩散先验的盲图像恢复。它包括两个阶段的模型，第一个阶段使用SwinIR模型去除图像退化，第二个阶段使用稳定扩散模型对细节进行修复。该项目提供了预训练模型和推理代码，可以用于一般图像恢复和人脸图像恢复。你可以通过提供的链接访问论文和项目主页了解更多信息。

## aigc-apps/sd-webui-EasyPhoto

* 主要开发语言：Python
* 当前Star数量：1580
* 贡献者数量：6
* Open Issues数量：22


EasyPhoto是一个用于生成AI肖像的Webui UI插件，可用于训练与您相关的数字替身。推荐使用5到20张肖像照片进行训练，最好是半身照片，不要戴眼镜（如果几张照片中的角色戴眼镜也没关系）。训练完成后，我们可以在推理部分生成它。我们支持使用预设模板图像或上传您自己的图像进行推理。

EasyPhoto的使用场景包括但不限于：
- 生成个性化的AI肖像，用于数字替身训练。
- 生成艺术作品或设计素材。
- 生成虚拟角色或游戏角色的形象。
- 用于人脸识别和图像处理研究。

您可以通过阿里云DSW、AutoDL或Docker来使用EasyPhoto。具体的安装和使用方法可以参考项目的README文件。

项目的架构概述如下：首先进行人脸检测，然后使用稳定扩散模型进行训练和推理，最后生成个性化的肖像图像。训练过程中，使用模板图像进行验证，以确保生成的肖像与用户相似。推理过程中，使用用户的数字替身和期望的生成场景进行图像生成。

该项目还提供了相关的参考项目和联系方式，可以进一步了解和交流。

## ECTO-1A/AppleJuice

* 主要开发语言：Python
* 当前Star数量：657
* 贡献者数量：4
* Open Issues数量：15


这个项目是一个使用蓝牙低功耗（BLE）向苹果设备发送接近配对消息的实验性概念验证（PoC）。该项目仅用于教育目的，不能用于违法行为或个人获利。项目的作者对该项目的材料可能造成的任何可能的损害不负任何责任。

这个项目是为了回应DEF CON 31期间发送的各种AppleTV欺骗消息而创建的。在亲身经历之后，作者不得不弄清楚发生了什么。作者找到的现有研究项目（参见*credits*）提供了很多有用的信息，但是由于包依赖关系的问题，这些项目都已经过时了几年，所以作者决定从中汲取所能，并从那里开始构建。

要运行这些脚本，您需要一台带有内置蓝牙适配器或USB蓝牙适配器的Linux机器。所有原始测试都是在一台带有内置蓝牙适配器的Lenovo T480上进行的。后来在运行Kali Linux的Raspberry Pi 3B+和Raspberry Pi Zero W上进行了测试，使用了[Zexmte长距离USB蓝牙5.1适配器](https://zexmte.com/collections/bluetooth-adapter/products/plug-play-long-range-bluetooth-5-1-usb-adapter)。

要安装这些脚本，您需要一台带有内置蓝牙适配器或USB蓝牙适配器的Linux机器。所有原始测试都是在一台带有内置蓝牙适配器的Lenovo T480上进行的。后来在运行Kali Linux的Raspberry Pi 3B+和Raspberry Pi Zero W上进行了测试，使用了[Zexmte长距离USB蓝牙5.1适配器](https://zexmte.com/collections/bluetooth-adapter/products/plug-play-long-range-bluetooth-5-1-usb-adapter)。

在运行脚本之前，请检查您的蓝牙适配器是否连接并显示为`hci0`。运行`hcitool dev`命令以获取已连接适配器的列表。可以使用`app.py`脚本运行可用选项的列表。

这个项目的使用场景是用于教育目的，了解和学习如何使用蓝牙低功耗（BLE）向苹果设备发送接近配对消息。它不应该被用于违法行为或个人获利。用户可以使用这个项目来了解蓝牙低功耗技术和苹果设备的安全性，并在合法的环境中进行测试和研究。这个项目可以帮助用户了解如何保护自己的苹果设备免受恶意接近配对消息的攻击。

## aripiprazole/rinha-de-compiler

* 主要开发语言：Rust
* 当前Star数量：699
* 贡献者数量：112
* Open Issues数量：14


这个项目是一个编译器（或解释器）的竞赛，要求在一台具有2个核心和2G内存的机器上运行。编译器或解释器需要处理存储在JSON格式中的"抽象语法树"。你的任务是接收包含抽象语法树的JSON，并根据提供的信息解释或编译程序。简单来说，我们给你一个包含树的JSON，你运行它，然后看到结果。项目要求每个项目都有自己的`Dockerfile`，以便我们可以运行它们。测试时可以使用`files/fib.rinha`文件并使用我们提供的程序生成JSON，或者直接使用`files/fib.json`中的JSON。语言必须基于某个文件运行，该文件是竞赛规定的AST的JSON。项目有一个解析JSON的"解释器"，返回一个AST，代码必须以不同的方式进行测试，如斐波那契数列以外的其他算法。竞赛截止日期为9月23日，之后将拒绝项目。在测试发布后，将允许进行调整和修正实现。一些有用的资源来学习如何编写自己的解释器或编译器的链接已经提供。

这个项目是一个编译器（或解释器）的竞赛，要求在一台具有2个核心和2G内存的机器上运行。编译器或解释器需要处理存储在JSON格式中的"抽象语法树"。你的任务是接收包含抽象语法树的JSON，并根据提供的信息解释或编译程序。简单来说，我们给你一个包含树的JSON，你运行它，然后看到结果。项目要求每个项目都有自己的`Dockerfile`，以便我们可以运行它们。测试时可以使用`files/fib.rinha`文件并使用我们提供的程序生成JSON，或者直接使用`files/fib.json`中的JSON。语言必须基于某个文件运行，该文件是竞赛规定的AST的JSON。项目有一个解析JSON的"解释器"，返回一个AST，代码必须以不同的方式进行测试，如斐波那契数列以外的其他算法。竞赛截止日期为9月23日，之后将拒绝项目。在测试发布后，将允许进行调整和修正实现。一些有用的资源来学习如何编写自己的解释器或编译器的链接已经提供。

## fishaudio/Bert-VITS2

* 主要开发语言：Python
* 当前Star数量：686
* 贡献者数量：9
* Open Issues数量：3


这个项目是一个使用Bert作为VITS2（Vision-and-Text-Driven Speech Synthesis）骨干网络的实现。VITS2是一种基于视觉和文本的语音合成方法。该项目提供了代码和示例，供用户学习如何训练模型。然而，使用该项目进行任何违反中国法律的活动是严格禁止的，包括违反宪法、刑法、治安管理处罚法和民法典。同时，禁止将该项目用于任何政治相关的用途。项目中提供了一些参考资料，包括其他相关项目的链接。

## FIRST-Tech-Challenge/FtcRobotController

* 主要开发语言：Java
* 当前Star数量：500
* 贡献者数量：2
* Open Issues数量：40


该项目是FTC（FIRST Tech Challenge）的公共SDK，用于构建控制FTC竞赛机器人的Android应用程序。该SDK需要使用Android Studio 2021.2或更高版本。如果您是Android Studio开发人员，可以通过克隆或下载ZIP文件的方式获取项目。该项目包含了大量的示例OpModes，您可以将这些示例代码复制到您的项目中使用，或根据需要进行修改。此外，该项目还提供了用户文档、教程和在线论坛等帮助资源。最新版本的更新包括对Vuforia和TensorFlow Object Detection的支持，以及一些性能改进和错误修复。
