---
title: "Software Engineering in the AI Era: The Bottleneck Is No Longer Development, It's Quality"
description: "Drawing from interview observations of three types of developers, this article explores how AI is restructuring software engineering: the bottleneck has shifted from generation to quality, testing is evolving into quality engineering, and product thinking is becoming every engineer's core competency."
date: 2026-06-27T08:00:00+08:00
slug: "ai-era-quality-engineering"
author: Ray Sun
categories:
  - AI Industry Insights
tags:
  - Software Engineering
  - Quality Engineering
  - AI Development
  - Testing
  - Product Thinking
draft: false
---

{{< figure src="/images/ai-era-quality-engineering/hero-quality-gate.webp" alt="Software engineering in the AI era: from code generation to quality assurance" caption="AI has dramatically increased generation throughput — but the quality gate has become the new bottleneck. That's the real challenge of software engineering in the AI era." >}}

I've spent the past few days interviewing candidates for QA positions.

To be precise: there are no longer any traditional "frontend," "backend," "QA," or "design" roles in the conventional sense.

Starting last year, we restructured all engineering-related positions into a single title — **Software Engineer** — with people taking on different responsibilities based on their focus. Earlier this year, we went a step further and eliminated our dedicated design role entirely.

The reason is simple.

The old model of software development looked like this:

> **AI assists humans in getting work done.**

Today, we believe the truly effective model has become:

> **AI is the primary executor. Humans handle planning, judgment, and quality.**

This shift is happening faster than most people realize.

<!-- more -->

---

## The Hardest Problem Is No Longer Writing Code — It's Knowing Whether the Code Is Correct

Today's large language models can write code at remarkable speed — generating frontend pages, database schemas, and API implementations in minutes. But the truly difficult problem has shifted to something else entirely:

> **You don't know if what it wrote is correct.**

AI can produce hundreds of lines of code in a minute, but because its generation mechanism is fundamentally probabilistic, errors are always possible:

> **It can always be wrong.**

The bottleneck in future software engineering is therefore no longer *generation*, but:

**How do you ensure the quality of what was generated?**

Traditional software engineering relied on human code review, manual testing, and human acceptance. But AI has pushed development velocity up by an order of magnitude. If testing still relies on manual execution and case-by-case verification, the entire development pipeline will inevitably become a bottleneck.

This is why I keep coming back to one idea:

> **Only magic can defeat magic.**

Future software quality must itself be guaranteed by AI. But there's an easy misconception here: that simply handing testing over to AI solves everything.

In reality, AI excels at *execution*, not *thinking*. It can efficiently generate test cases, run regression suites, and cover a large number of scenarios automatically — but it doesn't truly understand system boundaries. It can't proactively surface the questions that *should* be asked but haven't been thought of yet.

This is analogous to product development. AI can quickly implement features from requirements, but the genuinely hard part is defining what a "correct requirement" actually is. The same is true for testing.

The real value isn't in *running* tests — it's in asking:

* Where is this system most likely to fail?
* What scenarios are users most likely to hit unexpectedly?
* Which edge cases could bring the system down?
* Which hidden assumptions are actually false?

These questions can't be answered by generation alone.

Future quality engineering, then, is less about execution and more about **the ability to design the right questions**.

AI handles execution. Humans define the problems, set the standards, and build the verification framework. The people truly responsible for quality no longer run tests themselves — they keep asking:

*What haven't we tested yet?*

---

# Three Types of Developers I Encountered in Interviews

## Type 1: Still Resisting AI

{{< figure src="/images/ai-era-quality-engineering/engineer-type-1-resistant.webp" alt="Type 1 engineer: still resisting AI" caption="Psychological inertia keeps them facing away from change — accepting AI means unlearning years of accumulated working habits" >}}

This type is the easiest to spot.

They're unwilling to accept that AI has already changed software engineering.

They'll ask things like:

> Why is this interview testing AI knowledge?

Why not just evaluate traditional development skills?

They're not trying to understand the change — they're denying it.

This resistance comes from psychological inertia.

Accepting AI means that years of accumulated working methods need to be relearned.

And change is always uncomfortable.

---

## Type 2: Aware of AI, but Stuck at the Dabbling Stage

{{< figure src="/images/ai-era-quality-engineering/engineer-type-2-dabbling.webp" alt="Type 2 engineer: dabbling with AI but not truly integrating it" caption="Looks like they're using AI — but nothing has fundamentally changed. They try it once, then drift back to the old way." >}}

This is the largest group.

They're aware of the shift and have tried a few tools, but they remain at the surface level. After experimenting, they return to their old workflows. AI never gets truly integrated into their process. They don't rethink how they work through an AI lens. They never build consistent habits around it.

The result: they look like AI users, but nothing has actually changed. Until one day, they discover that the environment has completely transformed — and they're still standing in the same place. By then, it's often too late. They weren't awakened by AI. They were displaced by it.

---

## Type 3: Already Ahead of AI

{{< figure src="/images/ai-era-quality-engineering/engineer-type-3-leading.webp" alt="Type 3 engineer: confidently directing AI as the primary executor" caption="They conduct AI like an orchestra — they understand Agents, Workflows, Context, and Prompts, and have AI doing real engineering work" >}}

These people have started to genuinely understand AI. They know core concepts like Agents, Workflows, Context, and Prompts. They've already handed meaningful engineering tasks over to AI in their actual work.

But what surprised me is that many of them still haven't realized that what AI brings isn't simply a tool upgrade — it's a restructuring of roles at the organizational level.

I always ask one question in interviews: *If there are no QA roles in the future, what's your plan?*

Most people have never seriously considered this. Because what AI is changing isn't just how we work — it's how entire organizational roles are being redefined.

---

# This Is No Longer the Boiling Frog Scenario

Many people didn't start paying serious attention to AI until this year. Even plenty of top-university graduates and master's degree holders — people with real work experience — only recently began engaging seriously. Ironically, it's the younger generation, those still in school or freshly graduated, who have embraced AI with far more openness.

But reality is moving much faster than most people expect.

Over the past year, AI felt like warm water. People thought: *it's fine, I'll learn gradually, there's still time.* But now, heading into this year, I increasingly feel the water has boiled. Many role changes aren't happening in the future — they're happening right now. And when people finally realize it, they're often already facing a new competitive landscape they weren't ready for.

---

# One Piece of Advice and Two Shifts: Models, Quality, and Product Thinking

### One Piece of Advice: Experience the Best Models First

I give every candidate the same advice at the end of an interview: regardless of whether we end up working together, please go try the best AI models in the world.

The reason is simple. Most people's mental model of AI is built from free models, open-source models, or domestic platforms. That's not a knock on those tools — but if your first impression of AI came from a model that's not yet fully mature, it's very easy to reach a wrong conclusion:

> *AI isn't that impressive.*

In reality, the gap between truly frontier models and average models is much larger than most people imagine. Without having used the best models, it's very hard to understand where AI is actually taking software engineering.

---

### Shift 1: Testing Is Becoming Quality Engineering

{{< figure src="/images/ai-era-quality-engineering/quality-engineer-white-hat.webp" alt="Quality engineer: designing verification systems like a white-hat hacker" caption="Future quality engineers won't run tests — they'll design problems. Constantly finding where the system is most likely to fail. This skill only becomes more valuable in the AI era." >}}

The first shift I see clearly is in testing itself.

A lot of people like to debate whether QA roles will disappear. My answer: traditional testing will shrink, but quality won't disappear.

What will truly matter going forward isn't Testing — it's **Quality Engineering**. QA engineers won't just execute tests; they'll build an entire quality assurance system through development skills, automation capabilities, and AI.

AI writes the code, AI generates the tests, AI runs the regression, AI validates the results. Quality engineers define the verification standards, design the test architecture, build the automation infrastructure, and find the things AI missed.

They're more like white-hat hackers standing on the opposite side of the product — constantly probing where the system is most likely to break. This skill becomes *more* valuable in the AI era, not less.

---

### Shift 2: Product Thinking Becomes a Core Competency

The second shift is the growing importance of product thinking.

Going forward, both developers and QA engineers need to think like product people. Not just write code. Not just complete tasks. But genuinely understand the product from the user's perspective — the business, the experience, why things are designed a certain way, and what problem actually needs to be solved.

AI will become increasingly capable at execution. What remains genuinely difficult to replace is judgment, planning, product understanding, and systems thinking. These will become the most important competitive advantages for every software engineer going forward.

---

## Final Thoughts

These interviews have reinforced something I increasingly believe: AI is reshaping software engineering, but what ultimately determines success isn't how fast it can write code — it's whether it can support the delivery of genuinely high-quality products.

AI can dramatically increase generation throughput. But if the output quality is unstable or unreliable, speed means nothing.

Especially in enterprise environments, a customer-facing product that lacks rigor makes trust impossible to build — let alone revenue.

That's why rigor, stability, and verifiability are the first priority.

The fundamental problem of future software engineering is this: given that AI is now a massive participant in production, how do we build a system that actually guarantees product quality?

Future software engineers won't just be the ones who write code. They'll be the ones who direct AI, design quality systems, and serve as the gatekeepers of high-quality products.

That's the true core of software engineering in the AI era.
