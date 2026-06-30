---
title: "How AI Made Us Rethink Team Collaboration"
description: "A real internal experiment: the same product, built by a four-person team versus one person with AI. The results surprised everyone — and forced us to rethink how we think about division of labor, collaboration, and judgment in the age of AI."
author: Old Sun's Straight-faced Nonsense
date: 2026-06-30T08:00:00+08:00
categories:
  - AI Team Management
tags:
  - AI
  - Team Collaboration
  - Engineering Efficiency
  - Software Engineering
  - Product Thinking
draft: false
---

We recently ran a real internal experiment.

The target was the same product: a **file-level disaster recovery tool**. This wasn't a toy project — it was built on top of real experience accumulated from our HyperBDR and other DR products, re-abstracting our understanding of DR systems into a brand-new recovery object. Real business context. Real product complexity.

We approached this requirement with two completely different organizational structures.

**The first** was the familiar team-based development model: a Lead broke the requirements into modules (file sync, version management, recovery strategy, task scheduling, etc.), with two frontend and two backend engineers collaborating with AI assistance. The Lead also served as product manager, with UI handled collaboratively by the team.

**The second** was the exact opposite: a single colleague — someone with long-term experience in customer delivery and frontline service — independently used AI to go from requirements analysis and solution design all the way through implementation, without task decomposition, completing the entire product end-to-end.

In the end, we didn't compare development time or lines of code. We only looked at the product itself — how usable it was, how it looked, how smooth the experience felt.

{{< figure src="/images/ai-era-team-collaboration/experiment-comparison.webp" alt="Experiment comparison: traditional team vs solo × AI" caption="Same product, two organizational approaches — the result surprised everyone" >}}

**The result surprised everyone.**

The solo approach was clearly superior in delivery speed, overall consistency, and product experience. The differences were especially stark in the coherence of the recovery flow, consistency of error handling, and the logical unity of the overall product.

## Why Was One Person More Efficient?

The immediate reaction is: with AI assistance, can one person really replace a small team?

But the problem may not be the headcount — it's **the task decomposition model itself**.

The way software engineering organizes work has always been changing. Early on, there was no fine-grained distinction between frontend, backend, design, QA, and product. One person could often own the full cycle from understanding requirements to shipping features. As systems grew more complex and tech stacks more specialized, individual execution capacity became the bottleneck, and division of labor gradually emerged and solidified.

This division of labor didn't arise because it was "inherently more efficient." It was a compensation for **individual capability limits** under the production conditions of its time.

AI changes that premise. When AI significantly amplifies individual execution capacity, the task boundaries that were forced apart in the past become unstable again.

The premise of modular decomposition is that inter-module coupling can be resolved through interfaces and communication. But in real products, many problems are inherently cross-module — take the "recovery flow" as an example: it simultaneously involves frontend interaction, backend state machines, data consistency, error handling, and overall UX. Splitting it across different people inevitably requires a huge amount of alignment. **That alignment itself is the cost.**

Looking back at the experiment, we observed a clear divergence between the two groups:

- The traditional dev group operated in a classic **process-driven** mode: requirements analysis → detailed design → module decomposition → implementation → integration testing. Complete process, clear stages.
- The delivery colleague operated in a classic **outcome-driven** mode: no emphasis on process completeness, no focus on intermediate steps, with the final deliverable as the north star, continuously using AI to correct drift from the goal.

When AI reduces the cost of execution, the value of process itself diminishes — and the ability to iterate toward outcomes becomes more important. That gap was amplified further.

## Rethinking Team Collaboration

This experiment made me revisit a more fundamental question: what kinds of tasks belong to one person, and what belongs to many?

A fairly direct heuristic: **if a piece of work requires frequent business-level communication, it's probably better suited for one person.**

Because that communication isn't really collaboration — it's repeatedly syncing on "what is this thing, exactly?" When constant sync becomes the norm, multi-person collaboration amplifies the cost of understanding rather than reducing it.

Conversely, if the collaboration is purely interface-based — clear boundaries, no need to repeatedly explain the business itself — then it makes sense to split across multiple people.

In other words, the criteria for task decomposition are undergoing a fundamental shift:

**From functional boundaries, toward cognitive communication cost.**

{{< figure src="/images/ai-era-team-collaboration/task-split-evolution.webp" alt="The evolution of task decomposition: from functional boundaries to cognitive communication cost" caption="AI changes the underlying logic of division of labor — as execution costs fall, comprehension costs become the real bottleneck" >}}

To push this further: if someone still needs others to help them understand the business context while doing their work, they're still operating in the old collaboration model. When AI can handle most of the execution, the ability that truly matters is no longer "can you complete the task" — it's "can you independently form a complete understanding and make judgments."

## AI Turned Development from Essay Questions into Multiple Choice

There's another observation that hit hard during this experiment.

**AI doesn't make product development easier — it just makes the first 80% faster.**

Prototypes, basic flows, page structures, API sketches — with AI you can stand these up quickly. But what actually determines product quality is usually the last 20% of the productization process.

People who move fast through the first 80% don't necessarily think clearly through the last 20%.

The first 80% is more about execution density — in a sense, "diligence" is enough. The last 20% demands judgment, trade-offs, and taste — it requires "intelligence," or more precisely, depth of thinking and aesthetic sensibility.

{{< figure src="/images/ai-era-team-collaboration/ai-8020-rule.webp" alt="The 80/20 rule in the AI era: 80% execution, 20% judgment" caption="AI massively accelerates the first 80%, but the last 20% that determines product quality still depends on judgment and taste" >}}

In the past, writing code was more like an essay question: could you work out the solution?

With AI in the picture, development increasingly feels like multiple choice and true/false: AI presents you with options, code, interfaces, and paths. The hard part becomes — can you judge what's right, what merely "works," and what is actually *good*?

As for best practices for that last 20%, we're honestly still figuring it out ourselves. But one thing is clear: AI has already converted many problems that once depended on execution ability into problems of judgment ability.

## Conclusion

If we abstract this experiment, what we're seeing isn't just an efficiency story — it's an organizational shift.

The value AI brings won't only show up in local optimizations like "writing code faster." It will gradually converge on a more practical question:

Given the same objective, do you use fewer people to achieve the same output — or do you use the same people to multiply output by five or ten times?

This experiment just made that question a little more concrete.

And what will actually separate people in the AI era may no longer be execution ability in the traditional sense. It may come down to two things:

**Depth of thinking, and taste.**
