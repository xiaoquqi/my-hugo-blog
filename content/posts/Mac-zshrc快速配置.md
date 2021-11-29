---
title: Mac iTerm2 zshrc快速配置
author: 孙琦(Ray)
tags:
  - 常用命令
categories: []
date: 2021-02-02 11:26:00
---
zsh基本上已经成为Mac上的标配了，界面美观还有点缀的小图标，非常漂亮。但是网上配置zsh文章很多，配置方法也是五花八门，并且由于github被墙的原因，经过由于网络问题安装失败。经过反复测试，在国内的代码托管网站进行了Github部分关键项目定时缓存后，提高配置效率。这里写一篇自用的配置方法，留给有需要的人。

我的环境：iTerm2 + oh-my-zsh + powerlevel10k，这是我的配置效果：

![upload successful](/images/pasted-123.png)

<!-- more -->

## 原理解析

我们开始配置前，还是有必要讲一下这几个项目的关系，以便了解其工作原理。

* iTerm2不用说了，MacOS上必备的Terminal工具，替代原有系统自带的工具。
* ohmyzsh(https://github.com/ohmyzsh/ohmyzsh/) 是一套基于zsh深度定制的插件及主题管理的框架，方便定制适合你的zsh环境。
* Nerd Fonts(https://www.nerdfonts.com/) 我们在截图中看到的那些可爱的小图标就是来自这个项目，让我们原本枯燥的Terminal增添了几分乐趣。
* powerlevel10k(https://github.com/romkatv/powerlevel10k) 是一套zsh皮肤，也是目前我个人比较喜欢的一套皮肤，同时提供了较强的配置能力，包括字体下载，iTerm2的配置都自动完成了，所以也是目前使用最顺手的一套皮肤。

### 安装流程

由于以上各个项目帮我们做了大量的优化，所以让zsh的安装过程变得简单了很多，大体的流程为：
* 安装oh-my-zsh，其实就是clone回来
* 安装powerlevel10k，其实也是clone回来
* powerlevel10k的基本配置，根据我们喜欢进行定制
* 最后是zsh的配置，也就是修改.zshrc文件

## oh-my-zsh安装

官方的方法是通过curl或wget，执行github上的install.sh文件，但是由于raw.githubusercontent.com已经属于常年被墙的状态，所以并不推荐这种方式，这里采用的方式是将oh-my-zsh下载回来后，再执行install.sh。

```
export WORKSPACE=$HOME/workspace/zsh
mkdir -p $WORKSPACE

cd $WORKSPACE
git clone https://e.coding.net/xiaoquqi/github/ohmyzsh.git
```

安装脚本在ohmyzsh/tools/install.sh中，这里我们通过环境变量设置本地源

```
export REMOTE=https://e.coding.net/xiaoquqi/github/ohmyzsh.git

$WORKSPACE/ohmyzsh/tools/install.sh
```

## powerlevel10k安装

powerlevel10k已经被gitee缓存了，所以我就没再做单独的缓存源，直接利用官方提供的命令获取。powerlevel10k会被clone到ohmyzsh的custom路径中。

```
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

替换默认的zsh主题

```
sed -i '' "s/^ZSH_THEME=.*/ZSH_THEME=\"powerlevel10k\/powerlevel10k\"/g" $HOME/.zshrc
```

在正式启用主题前，还需要对powerlevel下载字体的文件进行优化。由于是从github下载字体，所以powerlevel10k配置一定会失败，必须要进行替换后，才能安装正常。

```
sed -i '' "s#^local -r font_base_url=.*#local -r font_base_url='https://xiaoquqi.coding.net/p/github/d/powerlevel10k-media/git/raw/master'#g" $HOME/.oh-my-zsh/custom/themes/powerlevel10k/internal/wizard.zsh
```

source zshrc会自动触发配置，按照向导和喜欢的样式来就好，这里就不再赘述了

```
source ~/.zshrc
```

如果想重新配置，也可以使用命令：

```
p10k configure
```

## 加载插件

通过修改.zshrc中的plugins变量可以实现插件加载的效果，比如使用virtualenv插件。
```
plugins=(git virtualenv)
```