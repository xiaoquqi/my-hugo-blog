---
layout: post
title: "为什么叫Monkey Patch？"
date: 2015-08-18 18:51:21 +0800
comments: true
categories: 
---

在程序运行时给代码加补丁的方法被称为Monkey Patch，这种方式多见于脚本类语言中(Dynamic Programming Languages)，例如: Ruby/Python等。国内很多人翻译为猴子补丁，但是为什么叫猴子补丁而不叫老虎补丁、狮子补丁呢？

估计刚刚看到这个表述的开发人员可能很难理解到底这是什么意思，其实Monkey Patch本与猴子无关，这个词原来为Guerrilla Patch，这样看着好像能明白一些了，游击队嘛，神出鬼没的，好像和运行状态打补丁这个功能贴近点了，但是为什么又变成猴子了。原来老外们都是很顽皮的，他们喜欢一些玩笑式的表述，就像很多技术的文档中一样。在英文里，Guerrilla和Gorilla读音是几乎一样的，Gorilla当什么讲呢？大猩猩。但是大猩猩有点吓人，所以干脆换成了大猩猩的近亲——猴子。就这样Monkey Patch形成了。

当然这并不是这个词的唯一解释，还有一种解释是说由于这种方式将原来的代码弄乱了(messing with it)，在英文里叫monkeying about(顽皮的)，所以叫做Monkey Patch。这种描述应该是和Monkey Test有异曲同工之妙。但是无论这个词从哪里来，我们只要正确理解Monkey Patch的含义就好了。

相同的表述还有Duck Typing，描述的是动态类型的一种风格。
