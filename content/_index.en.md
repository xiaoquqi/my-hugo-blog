---
title: 老孙正经胡说
layout: hextra-home
---

<div class="hero-split hx:flex hx:flex-wrap hx:items-center hx:gap-8 hx:mb-12">
  <div class="hero-text hx:flex-1 hx:min-w-0">
    {{< hextra/hero-badge link="/about" >}}
      <span>👋 Welcome</span>
      {{< icon name="arrow-circle-right" attributes="height=14" >}}
    {{< /hextra/hero-badge >}}

    <div class="hx:mt-6 hx:mb-4">
    {{< hextra/hero-headline >}}
      老孙正经胡说<span class="hero-headline-dot">.</span>
    {{< /hextra/hero-headline >}}
    </div>

    <div class="hx:mb-6">
    {{< hextra/hero-subtitle >}}
      Co-founder & CTO of Wanbozhichi, Ceph China Community Co-founder, Alibaba Cloud MVP, Tencent Cloud TVP
    {{< /hextra/hero-subtitle >}}
    </div>

    <p class="hero-intro hx:text-base hx:text-gray-600 hx:dark:text-gray-400 hx:leading-relaxed hx:max-w-2xl">
      From OpenStack to Ceph, from cloud-native to AI LLMs — over a decade at the forefront of technology.
      Deep expertise in <strong class="hx:text-gray-800 hx:dark:text-gray-200">To B productization</strong> and <strong class="hx:text-gray-800 hx:dark:text-gray-200">global SaaS</strong>,
      bringing cloud migration, disaster recovery, and cross-cloud solutions to the world stage.
      This is where I share my thoughts on tech, product, and what's next.
    </p>
  </div>

  <div class="hero-avatar hx:flex-shrink-0 hx:flex hx:justify-center">
    <div class="hx:w-48 hx:h-48 hx:rounded-full hx:border-2 hx:border-dashed hx:border-gray-300 hx:dark:border-neutral-600 hx:flex hx:items-center hx:justify-center hx:text-gray-400 hx:dark:text-gray-500 hx:text-sm">
      📷<br>Add photo
    </div>
  </div>
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="AI Insights"
    subtitle="LLMs, AI agents, machine learning — research and practical insights"
    icon="sparkles"
    link="ai"
  >}}
  {{< hextra/feature-card
    title="Cloud DR"
    subtitle="Cloud-native migration, disaster recovery, and cross-cloud data exchange"
    icon="cloud"
    link="docs"
  >}}
  {{< hextra/feature-card
    title="Training"
    subtitle="Go, Python microservices, OpenStack/Ceph, Serverless — hands-on tutorials"
    icon="academic-cap"
    link="training"
  >}}
  {{< hextra/feature-card
    title="Tech Blog"
    subtitle="Insights on cloud computing, storage, DevOps, and AI"
    icon="pencil"
    link="blog"
  >}}
  {{< hextra/feature-card
    title="About Me"
    subtitle="Co-founder & CTO, 10+ years in software development"
    icon="user"
    link="about"
  >}}
  {{< hextra/feature-card
    title="RSS Feed"
    subtitle="Stay in sync with the latest articles delivered instantly"
    icon="rss"
    link="index.xml"
  >}}
{{< /hextra/feature-grid >}}

{{< recent-posts >}}