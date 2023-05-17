---
title: ChatGPT初学者最佳实践
date: 2023-05-17T07:07:40+08:00
slug: "chatgpt-beginner-best-practice"
author: 老孙正经胡说
tags:
  - ChatGPT
  - OpenAI
  - gpt
  - ai
categories:
  - ChatGPT
draft: false
---


2022年11月底，ChatGPT引爆了新一轮AI的革命，也让人们意识到AI真的能够大幅度提高人们的工作效率，甚至有人担心自己的工作会因为AI不保。这种居安思危的意识是正确的，但是正如锛凿斧锯的出现，并没有让木匠这个行业消失，而是让这个行业以更高效的方式工作。所以作为一种工具，我们应当对ChatGPT有一个正确认知，我们不要把自己定位成ChatGPT，而是要站在更为宏观的角度上，将自己定位成利用工具的人，才不会出现被AI淘汰的局面。

那么如何才能更好的利用chatGPT呢？为什么同时利用这种工具，有的人效率高，有的人却感觉没什么用呢？秘密就在如何写好提示词上，本文通过一些最佳实践，帮助大家更好的掌握ChatGPT提示词的使用技巧，让你效率提升，以一敌十。

## 与ChatGPT交互的基本常识

”工欲善其事必先利其器“，在我们使用前，还是要对ChatGPT的一些基本原理进行了解，这样才能更好的利用他。

ChatGPT已经通过许多语言的数据进行了训练，但是训练材料中，英语文本的数量要高得多。如果有一定的英语基础，可以直接用英语进行查询，再利用ChatGPT进行翻译成中文，这样得到的结果可能会更准确。虽然如此，但在实际中文处理能力上，ChatGPT表现一点也不弱，所以即使你的英文不好，也不用过分担心，直接用中文进行交流即可。

ChatGPT在输入中可以处理多达4,096个令牌(GPT-3.5，如果是GPT-4可以更多)，超过此限制的任何字符都将被忽略，不会有任何消息。一个令牌大致相当于一个单词，具体取决于用例。

如果您注意到ChatGPT正在走错方向，可以随时使用停止按钮停止响应生成。 

如果在聊天期间交换了太多的知识，可以启动一个新的聊天，以便后续的回复不会受到破坏。 

虽然与ChatGPT聊天有时会感觉几乎像是与人类交流，但“请”和“谢谢”之类的礼貌用语并不必要。 与ChatGPT对话并不需要很高的语言造诣，唯一要做的就是把你的需求说清楚，如果连你自己都说不清楚需求，没有人能知道你想干什么。

## 技巧一：角色扮演

ChatGPT可以扮演Linux终端、哲学家、品茶师或圣经翻译等多种角色。

这些提示的结构总是相同的：

首先，ChatGPT接收一个提示，告诉它AI应该扮演什么角色。然后提示说明用户提供了什么信息，接着说明AI应该如何处理这些信息，包括大致的指引方向。最后，开发人员在引号中放置第一个具体的指令。

我们以翻译为例，ChatGPT不但可以帮助我们准确的进行翻译，还可以进行优化，比如我们可以这样提问：

> 我希望你能充当英语翻译、拼写纠正和改进者。我会用任何语言和你交流，你会检测语言、翻译并用修正和改进后的中文回答我的文本。我希望你能用更美丽、更优雅、更高级的中文词汇和句子代替我的简化的A0级词汇和句子。保持意思不变，但使它们更具文学性。我希望你只回复纠正、改进，不要写解释。我的第一句话是“We’ve trained a model called ChatGPT which interacts in a conversational way. The dialogue format makes it possible for ChatGPT to answer follow-up questions, admit its mistakes, challenge incorrect premises, and reject inappropriate requests.”。

通过下面的截图，我们很清楚的看到ChatGPT帮助我们准确的翻译了英文，同时，利用上下文能力，你无须再发出相同的指令，只需要输入新的要翻译的语句，很高效的可以完成大批量翻译工作。

![chatgpt-beginner-best-practice-32.png](/images/chatgpt-beginner-best-practice-32.png)## 技巧二：明确回复内容的使用目标

明确文本使用的目标，例如，ChatGPT在输出文本作为博客文章、商店页面、LinkedIn帖子、推文、TikTok或YouTube脚本时会有很大的区别，这样ChatGPT能更有效的提供相关信息。例如：

> 我需要一个有关ChatGPT机会和风险的抖音脚本。使用简短的句子。直接面向观众。要求使用幽默一些的语言，更容易理解

![chatgpt-beginner-best-practice-37.png](/images/chatgpt-beginner-best-practice-37.png)## 技巧三：合理利用上下文，分批输出

ChatGPT不同于传统AI聊天机器人的一个显著特点就是对于上下文的理解能力，这样可以将一个超级大的问题，分成多次提问，多次返回，避免了由于模型的参数限制导致的输出不完整，最近流行的AutoGPT也是基于这样的思路实现的。

我们以一篇文章为例，可能最简单的连锁提示形式是首先询问文章的结构。然后您可以告诉ChatGPT制定相应的要点。这种方法还可以节省时间：如果您发现AI在大纲中走了错误的路，您可以在生成完整文本之前进行必要的调整。例如：

> 写一篇关于ChatGPT的文章。首先给我一个由标题、引语和几个副标题组成的大纲。
> [输出]
> 现在为每个副标题编写五个关键信息。
> [输出]
> 为每个副标题的关键信息添加五个关键词。
> [输出]
> ......

![chatgpt-beginner-best-practice-49.png](/images/chatgpt-beginner-best-practice-49.png)![chatgpt-beginner-best-practice-50.png](/images/chatgpt-beginner-best-practice-50.png)![chatgpt-beginner-best-practice-51.png](/images/chatgpt-beginner-best-practice-51.png)## 技巧四：修改输出内容

利用ChatGPT的上下文能力，您还可以修改已经输出的内容，当然这不会覆盖之前的回答，只会在之前的基础上再作答，甚至一些基本替换操作都可以命令ChatGPT帮你完成。

例如，我们可以利用ChatGPT为不同渠道生成相同的内容，并且表明不同的语气和格式：

> 示例新浪微博： 将生成的文本分成多个推文。记住每个推文的最大长度为140个中文字符。使用简短的句子，不要将其跨越多个推文。以一致的编号方案开始推文。

![chatgpt-beginner-best-practice-57.png](/images/chatgpt-beginner-best-practice-57.png)> 示例今日头条： 将生成的文本制作成今日头条帖子。请注意，最大长度为3000个字符。将文本的主要要点结构化为一个项目列表。以一个令人兴奋的引子句开始，以一个呼吁更多参与的行动结束。

![chatgpt-beginner-best-practice-60.png](/images/chatgpt-beginner-best-practice-60.png)> 修改文本示例：
> 为以上内容生成标签
> [回答]
> 关键词格式为 #开头 关键词之间有逗号
> [回答]

![chatgpt-beginner-best-practice-67.png](/images/chatgpt-beginner-best-practice-67.png)## 技巧五：格式化输出

默认情况下，ChatGPT以纯文本回复。但是，AI工具实际上使用Markdown标记语言处理格式，例如标题、粗体或斜体文本、有序（编号）或无序列表，甚至是表格。您可以使用这些功能来生成自己的文本。但是，在大多数情况下，ChatGPT本身不会想出这个想法，因此需要适当的格式提示。当然，您可以使用上下文来进行格式化。

> 例如Markdown： 我需要一篇关于ChatGPT的博客文章。写一个标题、一个引语、一个副标题和一个段落。用Markdown格式化所有内容。

![chatgpt-beginner-best-practice-72.png](/images/chatgpt-beginner-best-practice-72.png)> 例如按照表格输出：用表格展现ChatGPT不同模型的Token限制

![chatgpt-beginner-best-practice-75.png](/images/chatgpt-beginner-best-practice-75.png)> 例如：用PlantUML语法生成一个用户登陆的时序图

![chatgpt-beginner-best-practice-78.png](/images/chatgpt-beginner-best-practice-78.png)我们在PlantUML在线编辑器上就能看到预览效果

![chatgpt-beginner-best-practice-80.jpeg](/images/chatgpt-beginner-best-practice-80.jpeg)## 技巧六：指令提示

如果您确实比较词穷，无法准确描述您的需求，我们可以反向让ChatGPT扮演提问者，反向向我们提问。例如：

> 你是一个用于创建提示的机器人。您需要收集有关用户目标、首选输出示例和任何其他相关上下文信息的信息。
> 提示应包含您提供的所有必要信息。询问用户更多问题，直到您确定可以创建最佳提示为止。
> 您的答案应该明确地格式化并针对ChatGPT交互进行优化。确保首先询问用户关于目标、所需结果以及可能需要的任何其他信息。
> 请一条一条的提问。

![chatgpt-beginner-best-practice-88.png](/images/chatgpt-beginner-best-practice-88.png)## 技巧七：文本制作脑图、PPT、架构图等

其实上面已经提到，利用ChatGPT可以很轻松的生成PlantUML时序图。同样，对于很多图形化的表达方式，为了更好的共享，都可以用文本来描述，那么这样就可以要求ChatGPT按照这种方式生成格式，我们直接在相关软件中导入即可完成。

这里有一个小技巧，无论是官方的ChatGPT还是29gpt的ChatGPT，都会对Markdown进行解析后展现，此时在生成时，我们需要要求ChatGPT在Markdown的```生成，避免我们的WEB客户端进行解析后展现，方便我们后续复制使用。

> 生成研发管理流程思维导图，使用markmap格式，生成内容包含在```

![chatgpt-beginner-best-practice-94.jpeg](/images/chatgpt-beginner-best-practice-94.jpeg)接着我们把生成的内容倒入mindmap中：https://markmap.js.org/repl

![chatgpt-beginner-best-practice-96.jpeg](/images/chatgpt-beginner-best-practice-96.jpeg)我们再来看一下mermaid的例子，例如：

> 使用mermaid生成一个用户登陆的流程图，生成的内容包含在```

![chatgpt-beginner-best-practice-100.jpeg](/images/chatgpt-beginner-best-practice-100.jpeg)我们再讲生成的内容倒入到mermaid中(https://mermaid.live/edit)，注意粘贴后生成的```mermaid需要去掉。

![chatgpt-beginner-best-practice-102.jpeg](/images/chatgpt-beginner-best-practice-102.jpeg)## 技巧八：一次性提示，模拟写作

从上面的例子我们看到，我们对于ChatGPT的指令越清晰，就能得到更精准的答案，反之则会不尽如人意，这就是为什么同样是工具，个体在使用上产生差异的原因。有的时候，我们需要一些特定前提，让ChatGPT进行学习后，按照指定的格式进行输出。例如：

> 以下列语言描述开发语言特点：例如：语言名称：Java 开发时间：xxxx年 需要编译：是 学习难度：中 运用广泛程度：广泛

![chatgpt-beginner-best-practice-107.jpeg](/images/chatgpt-beginner-best-practice-107.jpeg)因为没有在指令中明确说明要输出哪些，所以第一次只给我们输出的一条，我们可以让ChatGPT继续输出相关内容

![chatgpt-beginner-best-practice-109.jpeg](/images/chatgpt-beginner-best-practice-109.jpeg)## 技巧九：对已有内容的改写

这种方式仍然是对上下文的应用，通过表明自己的观点和态度，引导ChatGPT优化或创造出更多的内容，提问的基本句式：


- 问题一：

   - 表明自己的态度，例如：针对以下的文本进行分析，指出不好的点，并一步一步列出

   - 给出文本内容

- 问题二：非常好的观点，根据分析结果重写文本并加以改进


![chatgpt-beginner-best-practice-118.jpeg](/images/chatgpt-beginner-best-practice-118.jpeg)![chatgpt-beginner-best-practice-119.jpeg](/images/chatgpt-beginner-best-practice-119.jpeg)## 技巧十：提问中使用明确的动词

从上述这些技巧来看，有一个共同的特点就是动词一定要明确，尽可能清晰地给ChatGPT明确的指令，尽量使用有意义的动词，例如：上面例子中，重写文本或者优化文本。另外，尽可能使用正向的表达，例如：要说“正式表达”，而不是“不要非正式表达”。

## 总结

其实使用ChatGPT没有什么密码可言，最重要的是对需求的描述，如果你平时能对自己的目标比较清晰，能够准确描述自己的需求，则ChatGPT会让你如鱼得水，而反之，如果你只是将ChatGPT理解成普通的问答机器人，那么你可能会觉得这个工具对你的帮助并不大。

这些技巧是对初次使用ChatGPT用户的一些建议，我相信随着使用的熟练，你能在更多的实践中总结出更多的技巧来提高工作效率。我们不必神话ChatGPT可能产生的颠覆性，对于普通人来说，将工具为我所用，不被时代的洪流淘汰才是硬道理。

