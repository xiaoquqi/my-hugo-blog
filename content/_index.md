---
title: 老孙正经胡说
layout: hextra-home
---

<div class="home-hero">
{{< hextra/hero-badge link="/about" >}}
  <span>👋 欢迎来访</span>
  {{< icon name="arrow-circle-right" attributes="height=14" >}}
{{< /hextra/hero-badge >}}

<div class="hx:mt-6 hx:mb-4">
{{< hextra/hero-headline >}}
  老孙正经胡说
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-8">
{{< hextra/hero-subtitle >}}
  云计算技术布道者 · Ceph 中国社区联合创始人 · 阿里云 MVP · 腾讯云 TVP
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:flex hx:flex-wrap hx:gap-3 hx:justify-center hx:mb-12">
{{< hextra/hero-button text="阅读博客" link="blog" >}}
{{< hextra/hero-button text="技术教程" link="training" >}}
{{< hextra/hero-button text="Github 趋势" link="github" >}}
</div>
</div>

<!-- Stats Row -->
<div class="home-stats hx:mb-12">
  <div class="home-stat-item">
    <span class="home-stat-number">36</span>
    <span class="home-stat-label">技术博客</span>
  </div>
  <div class="home-stat-item">
    <span class="home-stat-number">68</span>
    <span class="home-stat-label">开发教程</span>
  </div>
  <div class="home-stat-item">
    <span class="home-stat-number">492</span>
    <span class="home-stat-label">趋势分析</span>
  </div>
  <div class="home-stat-item">
    <span class="home-stat-number">10+</span>
    <span class="home-stat-label">热点专题</span>
  </div>
</div>

<!-- Section Cards -->
<div class="hx:mb-6">
{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="技术博客"
    subtitle="记录技术成长的点滴，涵盖云计算、存储、DevOps、AI 等领域的实践经验与思考。"
    icon="pencil"
    link="blog"
    class="hx:aspect-auto md:hx:aspect-[1.1/1] max-md:hx:min-h-[340px]"
    style="background: linear-gradient(135deg, rgba(59,130,246,0.08), rgba(147,51,234,0.06));"
  >}}
  {{< hextra/feature-card
    title="编程开发"
    subtitle="系统的编程开发教程，从 Go 语言入门到 Python gRPC，再到 OpenStack/Ceph 实战。"
    icon="code"
    link="training"
    class="hx:aspect-auto md:hx:aspect-[1.1/1] max-md:hx:min-h-[340px]"
    style="background: linear-gradient(135deg, rgba(34,197,94,0.08), rgba(6,182,212,0.06));"
  >}}
  {{< hextra/feature-card
    title="Github 趋势"
    subtitle="每日自动更新 Github 热门开源项目，助你把握技术潮流，发现优质开源工具。"
    icon="trending-up"
    link="github"
    class="hx:aspect-auto md:hx:aspect-[1.1/1] max-lg:hx:min-h-[340px]"
    style="background: linear-gradient(135deg, rgba(249,115,22,0.08), rgba(239,68,68,0.06));"
  >}}
{{< /hextra/feature-grid >}}
</div>

<!-- Second row -->
<div class="hx:mb-6">
{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="热点趋势"
    subtitle="关注云计算、AI 等前沿技术趋势，深度分析行业动态与技术演进方向。"
    icon="sparkles"
    link="docs"
    class="hx:aspect-auto md:hx:aspect-[1.1/1] max-md:hx:min-h-[340px]"
    style="background: linear-gradient(135deg, rgba(168,85,247,0.08), rgba(236,72,153,0.06));"
  >}}
  {{< hextra/feature-card
    title="关于我"
    subtitle="万博智云联合创始人 & CTO，十年以上软件研发及团队管理经验。"
    icon="user"
    link="about"
    class="hx:aspect-auto md:hx:aspect-[1.1/1] max-md:hx:min-h-[340px]"
    style="background: linear-gradient(135deg, rgba(20,184,166,0.08), rgba(16,185,129,0.06));"
  >}}
  {{< hextra/feature-card
    title="RSS 订阅"
    subtitle="通过 RSS 第一时间获取最新文章推送，不错过任何一篇技术分享。"
    icon="rss"
    link="index.xml"
    class="hx:aspect-auto md:hx:aspect-[1.1/1] max-lg:hx:min-h-[340px]"
    style="background: linear-gradient(135deg, rgba(251,146,60,0.08), rgba(251,191,36,0.06));"
  >}}
{{< /hextra/feature-grid >}}
</div>
