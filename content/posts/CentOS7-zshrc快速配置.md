---
title: CentOS7 zshrc快速配置
author: 孙琦(Ray)
tags:
  - 常用命令
categories: []
date: 2021-02-02 17:15:00
---
大部分时间里，我还是习惯于ssh到远程的CentOS7服务器上工作，因为Mac配置了漂亮zsh的缘故，所以也想把我的CentOS7切换到zsh模式。这是最终配置好的效果：

![upload successful](/images/pasted-124.png)

原理部分不再赘述，有兴趣可以参照MacOS的zsh配置篇。

CentOS7配置zsh与Mac上还是有一定区别的，因为版本要求，zsh需要自己安装编译，字体也需要自己安装，接下来是详细的步骤。

<!-- more -->

## 安装zsh

虽然通过yum方式可以安装zsh，但是无法满足powerlevel10k的要求，所以先使用zsh源码进行编译后安装。

```
WORKSPACE=$HOME/workspace/zsh
mkdir -p $WORKSPACE

cd $WORKSPACE
curl -o zsh.tar.xz https://jaist.dl.sourceforge.net/project/zsh/zsh/5.8/zsh-5.8.tar.xz
tar -xvf zsh-5.8.tar.xz

cd zsh
make
make install
```

zsh会安装在用户目录中/usr/local/bin/zsh中，将zsh设置为默认的系统shell，配置成功后，需要关闭Terminal重新登陆。

```
chsh -s /usr/local/bin/zsh
```

### 安装流程

接下来的流程与MacOS上安装类似，由于以上各个项目帮我们做了大量的优化，所以让zsh的安装过程变得简单了很多，大体的流程为：

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
sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"powerlevel10k\/powerlevel10k\"/g" $HOME/.zshrc
```

在正式启用主题前，还需要对powerlevel下载字体的文件进行优化。由于是从github下载字体，所以powerlevel10k配置一定会失败，必须要进行替换后，才能安装正常。

```
sed -i "s#^local -r font_base_url=.*#local -r font_base_url='https://xiaoquqi.coding.net/p/github/d/powerlevel10k-media/git/raw/master'#g" $HOME/.oh-my-zsh/custom/themes/powerlevel10k/internal/wizard.zsh
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