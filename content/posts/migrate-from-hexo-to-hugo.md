---
title: "将博客从Hexo迁移至Hugo"
date: 2021-11-29T20:23:54+08:00
draft: false
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

这是我在Hexo中的文档目录

```
|-- source
|   |-- _drafts -> 草稿目录，在Hugo中是通过模板中的draft参数控制，可以先拷贝至Hugo /content/posts目录中
|   |-- _posts -> 文章目录，拷贝至/content/posts目录中
|   |-- about -> 关于目录，拷贝至/content/about目录中
|   |-- favicon.ico -> 浏览器favorite icon图标
|   `-- images -> 静态文件，拷贝至/static/images目录中
```

### 文章结构

之前在编写Hexo时候，使用了Hexo Admin插件，不知道为什么生成的文章是这个样子的：

```
title: "将博客从Hexo迁移至Hexo"
date: 2021-11-29T20:23:54+08:00
---
```

由于缺少了顶部的---，导致Hugo无法正确识别标题和创建时间。于是用Python写了一个简单的脚本进行替换。

```
import glob
import re

files = glob.glob("../content/posts/*")
for f in files:
    with open(f, "r") as rfhd:
        lines = rfhd.readlines()
        first_line = lines[0].strip()
        if not first_line == "---":
            print(f)
            lines.insert(0, "---\n")
            with open(f, "w+") as wfhd:
                wfhd.writelines(lines)
```

### 部分图片无法显示

在我早期写的博客中，我使用了{% img ...}来引用图片，但是这种方式在Hugo中是无法正确显示的。于是仍然使用Python脚本进行了全局性替换。由于只是作为临时替换，所以在代码规范性上差了一点，但是能解决我的问题了。

```
for f in files:
    with open(f, "r") as rfhd:
        lines = rfhd.readlines()

        for index, line in enumerate(lines):

            line = line.strip()
            if re.match(r"{\s*%\s*img", line):
                print("Found line:", line)

                image_path = None
                m1 = re.match(r"{\s*%\s*img\s*(\/images\/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+)\s+", line)
                if m1:
                    image_path = m1.group(1)
                    print(m1.group(1))

                m2 = re.match(r"{\s*%\s*img\s+\w+\s+(\/images\/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+)\s+", line)
                if m2:
                    image_path = m2.group(1)
                    print(m2.group(1))

                new_image_path = "![](%s)\n" % image_path
                print(new_image_path)
                lines[index] = new_image_path
                print(lines)

        with open(f, "w+") as wfhd:
            wfhd.writelines(lines)
```

### 目录结构问题

在我完成了以上两步后，发现我的部分文章中的右侧目录显示不够完整，正常的显示逻辑应该是这样的效果。

![](/images/2021-11-30-10-00-24.png)

我发现我的文章中一级标题都没有显示，经过调查，发现之前存在一个误区，在一篇文档中，其实title部分才是一级标题，正常文章中的标题要从二级写起，这样目录才能正常生成出来。这意味着，我需要将原有文档中不规范的标题都加一个#才可以，所以仍然采用Python批量替换方式完成。

```
for f in files:
    with open(f, "r") as rfhd:
        lines = rfhd.readlines()
        print("Reading file:", f)

        # If we need to do replace in the file
        if_replace = False

        # In code area, ignore start #
        if_code_start = False

        for index, line in enumerate(lines):

            if re.match(r"^\s*```", line):
                if_code_start = not if_code_start
            print("if code start: [%s]%s" % (index, if_code_start))

            if re.match(r"^\s*#\s+\S+", line):
                if not if_code_start:
                    if_replace = True
            print("if file need to replace: %s" % if_replace)

            if re.match(r"^\s*#", line) and if_replace:
                print("Orig replace line is: %s" % line)
                print("Will replace line to: #%s" % line)
                lines[index] = "#%s" % line

        with open(f, "w+") as wfhd:
            wfhd.writelines(lines)
```

至此，所有的文章已经能够在Hugo中按照顺序显示了。

### 保持链接格式

在原有Hexo中，文章基本是按照时间格式进行命名，例如/year/month/day/title方式，但是在Hugo默认的方式中则是采用了直接命名的方式，这就需要我们在配置中进行修改，以达到上线后和原有链接保持一致的效果。在config.toml中修改如下内容：

```
[permalinks]
  # posts = ":year/:month/:filename"
  posts = "/:year/:month/:day/:slug/"
```

### 利用Github Action自动上线

配置到了这里，基本具备了上线条件，之前我在Github上使用了Travis CI方式进行编译上线，但是随着Github Workflow越来越成熟，所以这次决定采用Github方式进行部署。由于Github Pages在国内访问越来越慢，大概在前年将博客迁移至腾讯的云开发中。腾讯默认提供的云开发Action不太好用，于是我还是用执行命令方式完成，以下是我的github workflow yaml，供大家参考。

```
name: Deploy to Tecent Cloudbase # 名字自取

on:
  push:
    branches:
      - master  # 这里的意思是当 main分支发生push的时候，运行下面的jobs，这里先改为github-actions

jobs:
  deploy: # 任务名自取
    runs-on: ubuntu-18.04	# 在什么环境运行任务
    steps:
      - uses: actions/checkout@v2	# 引用actions/checkout这个action，与所在的github仓库同名
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive) 获取submodule主题
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo	# 步骤名自取
        uses: peaceiris/actions-hugo@v2	# hugo官方提供的action，用于在任务环境中获取hugo
        with:
          hugo-version: 'latest'	# 获取最新版本的hugo
          # extended: true

      - name: Build
        run: hugo --minify	# 使用hugo构建静态网页

      - uses: actions/setup-node@v2
        with:
          node-version: '14'
      - run: npm i -g @cloudbase/cli
      - run: tcb login --apiKeyId ${{secrets.secretId}} --apiKey ${{secrets.secretKey}}
      - run: cd public && tcb hosting deploy -e ${{secrets.envId}} --verbose
```

需要替换的secrets变量，需要在Github中进行创建。

![](/images/2021-11-30-10-13-55.png)

### 添加评论系统

LoveIt主题中支持多种评论系统，最终我使用的是valine，不过需要注册一个LeanCloud账号，建立一个开发板的应用程序后，再更新配置文件才行。

![Lean Cloud](/images/2021-11-30-13-21-40.png)

建立好应用后，在应用详情中找到”应用凭证“，获取相关鉴权信息。

![](/images/2021-11-30-13-24-01.png)

最后在Hugo config.toml中进行更新

```
[params.page.comment.valine]
  enable = true
  appId = "your_appId"
  appKey = "your_appKey"
  ......
  serverURLs = "https://your_leancloud_url"
```

配置好的效果如下：

![](/images/2021-11-30-13-28-35.png)

## 总结

其实Hugo LoveIt中还提供了很多功能，暂未深入研究，也欢迎大家共同交流。

到这里，我的全新Hugo样式的Blog已经发布上线，这是整体的效果，也欢迎大家经常访问我的博客——老孙正经胡说（https://sunqi.site）。

![](/images/2021-11-30-10-15-29.png)
