---
title: 老孙正经胡说
layout: hextra-home
---

<div class="hero-split hx:flex hx:flex-wrap hx:items-center hx:gap-8 hx:mb-12">
  <div class="hero-text hx:flex-1 hx:min-w-0">
    {{< hextra/hero-badge link="/about" >}}
      <span>👋 欢迎来访</span>
      {{< icon name="arrow-circle-right" attributes="height=14" >}}
    {{< /hextra/hero-badge >}}

    <div class="hx:mt-6 hx:mb-4">
    {{< hextra/hero-headline >}}
      老孙正经胡说<span class="hero-headline-dot">.</span>
    {{< /hextra/hero-headline >}}
    </div>

    <div class="hx:mb-6">
    {{< hextra/hero-subtitle >}}
      万博智云联合创始人 & CTO，Ceph 中国社区联合创始人，阿里云 MVP，腾讯云 TVP
    {{< /hextra/hero-subtitle >}}
    </div>

    <p class="hero-intro hx:text-base hx:text-gray-600 hx:dark:text-gray-400 hx:leading-relaxed hx:max-w-2xl">
      从 OpenStack 到 Ceph，从云原生到 AI 大模型，十多年来始终站在技术浪潮的最前沿。
      深耕 <strong class="hx:text-gray-800 hx:dark:text-gray-200">To B 产品化</strong> 与 <strong class="hx:text-gray-800 hx:dark:text-gray-200">软件出海</strong>，
      将云迁移、灾备、跨云数据交换等产品推向全球市场。
      这里记录着我的技术思考、产品实践和对未来的探索。
    </p>
  </div>

  <div class="hero-avatar hx:flex-shrink-0 hx:flex hx:justify-center">
    <div class="hx:w-48 hx:h-48 hx:rounded-full hx:border-2 hx:border-dashed hx:border-gray-300 hx:dark:border-neutral-600 hx:flex hx:items-center hx:justify-center hx:text-gray-400 hx:dark:text-gray-500 hx:text-sm">
      📷<br>添加头像
    </div>
  </div>
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="AI 洞察"
    subtitle="大语言模型、AI Agent、机器学习等前沿技术的研究与思考"
    icon="sparkles"
    link="ai"
  >}}
  {{< hextra/feature-card
    title="云迁移&容灾"
    subtitle="云原生迁移、灾备方案设计与跨云数据交换技术实践"
    icon="cloud"
    link="docs"
  >}}
  {{< hextra/feature-card
    title="培训课程"
    subtitle="Go 语言、Python 微服务、OpenStack/Ceph、Serverless 实战教程"
    icon="academic-cap"
    link="training"
  >}}
  {{< hextra/feature-card
    title="技术博客"
    subtitle="云计算、存储、DevOps 领域的实践经验与深度思考"
    icon="pencil"
    link="blog"
  >}}
  {{< hextra/feature-card
    title="关于我"
    subtitle="万博智云联合创始人 & CTO，十年以上研发与团队管理经验"
    icon="user"
    link="about"
  >}}
  {{< hextra/feature-card
    title="RSS 订阅"
    subtitle="第一时间获取最新文章推送，随时保持同步"
    icon="rss"
    link="index.xml"
  >}}
{{< /hextra/feature-grid >}}

{{< recent-posts >}}