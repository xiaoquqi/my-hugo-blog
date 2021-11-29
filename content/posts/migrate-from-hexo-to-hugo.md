---
title: "将博客从Hexo迁移至Hexo"
date: 2021-11-29T20:23:54+08:00
draft: true
---

自从了解了Github Pages这种静态博客后，开始喜欢上这种技术人员才能鼓捣明白的协作方式。自己的博客系统也从最初的Octopress，切换到Hexo，直到最近看到Hugo这种号称全球最快的静态博客系统，被适合技术人员的风格样式所吸引。于是在经历了三天的折腾后，顺利的将Hexo迁移至Hugo中。同时，利用github workflows在提交后，将博客自动发布到腾讯的云开发中。其实这三种不同的博客系统也恰好了代表了每一个时代流行的语言，Octopress(Ruby)，Hexo(Node.js)，Hugo(Go)。时代在发展社会在进步，唯一不变的是开发人员追去完美的心，记录下这一过程，也作为切换至Hugo后的第一篇博文。

<!-- more -->

## 安装Hugo

因为Hugo是Go语言开发的，所以安装起来比较简单，不过在我的Mac上，我最终还是选择brew方式进行安装。由于之前运行的brew是x86版本的，为了安装Hugo也对brew重新进行了安装。brew配置好了之后，直接安装命令即可。

```
brew install hugo
```

后续的流程相对简单，根据Hugo官网的Quick Start按照步骤即可。

### 创建站点

```
hugo new site quickstart
```

### 添加一个主题

经过对比，我选择了相对低调、灵活的LoveIt作为博客主题。这个主题非常灵活，基本把要预留的内容都留出来了，所以不需要将themes中的文件存放于博客版本库中，只需要以submodule形式存在即可。

```
cd quickstart
git init
git submodule add https://github.com/dillonzq/LoveIt themes/LoveIt
```

## 配置Hugo

Hugo每个主题都会有一个exampleSite的目录，比如LoveIt，就是在themes/LoveIt/exampleSite。这里面存放了主题配置的基本样例，我们至少需要将config.toml拷贝至你的Blog根目录，之后就可以进行配置了。其他资源文件可以视实际需要拷贝至相应的目录中。

```
.
├── assets
│   ├── css
│   ├── images
│   └── music
├── config.toml
├── content
│   ├── about
│   ├── categories
│   ├── posts
│   └── tags
└── static
    ├── _redirects
    ├── android-chrome-192x192.png
    ├── android-chrome-512x512.png
    ├── apple-touch-icon.png
    ├── browserconfig.xml
    ├── favicon-16x16.png
    ├── favicon-32x32.png
    ├── favicon.ico
    ├── mstile-150x150.png
    ├── safari-pinned-tab.svg
    └── site.webmanifest
```

在配置文件中，有比较详细的中文注释，根据实际内容进行调整就可以了，我删除掉了英语和法语部分的配置，其他配置按照我的实际需要进行了配置。由于配置内容过多，这里就不一一列举了，这里面只把一些特殊的选项和大家分享一下。

### 如何配置百度统计？

在params.footer中保留了一个custom的参数，只需要将百度统计写入其中就可以，例如：

```
[params.footer]
......
    custom = '<script> var _hmt = _hmt || []; (function() { var hm = document.createElement("script"); hm.src = "https://hm.baidu.com/hm.js?08e49a207e75eef254a959d4b9dede90"; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(hm, s); })(); </script><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3492265208608388" crossorigin="anonymous"></script>'
......
```

### 如何配置ICP及备案信息？

仍然在params.footer中保留了一个icp参数，只需要将备案信息写入其中即可，例如：

```
[params.footer]
......
    icp = '<br /><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502042680" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img src="/images/beian.png" style="float:left;"/>京公网安备 11010502042680号</a> | <a target="_blank" href="https://beian.miit.gov.cn/">京ICP备2020039231号-1</a>'
......
```

## 从Hexo迁移至Hugo

因为Hexo本质上也是使用Markdown方式进行管理，所以迁移上也比较方便，但是由于每个人遇到的问题并不相同，所以这里分享一下我自己遇到的实际问题。

### 如何迁移？

### 格式问题


## Hugo博客编写