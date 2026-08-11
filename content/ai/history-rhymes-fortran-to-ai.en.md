---
title: "History Rhymes: 70 Years Ago, We Didn't Trust Machines to Write Good Code Either"
description: "Seventy years ago, programmers didn't trust compilers to generate usable code either. Today's trust crisis around AI-written code is nearly the same story playing out again. From FORTRAN's origin story to the cost-driven organizational shift and the rise of software engineering itself, history has already given us the answer."
author: Old Sun's Straight-faced Nonsense
date: 2026-08-10T08:00:00+08:00
categories:
  - AI Industry Insights
tags:
  - AI
  - Software Engineering
  - FORTRAN
  - Compilers
draft: false
---

{{< figure src="/images/history-rhymes-fortran-to-ai/cover-machine-reliable.webp" alt="1950s programmer checking a compiler's punch-tape output with a magnifying glass, weighing a checkmark against a question mark; 2020s programmer looking at AI-generated code with a question mark of their own — same question, seventy years apart" caption="1950s vs. 2020s: can we actually trust what the machine wrote?" >}}

## 01 · AI Can Write Code, But Do We Actually Trust It?

There's a strange contradiction playing out in the programmer community right now: everyone can't stop using AI to write code, while also complaining about the flood of AI-generated code that nobody has actually understood or verified.

Open-source communities like Rust, LLVM, and Godot have all started raising the same concern, and "AI slop" has become a common term for it.

So the real argument today isn't whether AI can write code. It's this:

> **Can we actually trust what AI writes enough to ship it?**

More and more people are landing on the same answer: AI can write the code, but someone still has to be able to read it, review it, verify it, and ultimately be accountable for the outcome.

Here's the interesting part: almost 70 years ago, programmers went through a nearly identical crisis of trust — with the compiler.

---

## 02 · 70 Years Ago, the Real Cost Was Manual Translation

In the 1950s, writing a program looked nothing like it does today.

Say you wanted to do something simple: add A and B, and if the result is greater than 100, move on to the next step.

Today, that's simple to write:

```
C = A + B

if C > 100:
    do_something()
```

On an early computer, what a programmer actually had to write looked closer to this:

```
CLA A
ADD B
STO C
SUB HUNDRED
TPL NEXT
```

Programmers weren't just expressing logic — they had to know exactly where data lived in memory, what instructions the machine supported, and how each one worked. Switch to a different machine, and much of that had to be relearned and rewritten from scratch.

So back then, programmers spent most of their time not on "what problem am I solving," but on:

> Translating a human idea into the exact actions one specific machine could execute.

That's the economic backdrop FORTRAN emerged from. John Backus later recalled that at the time, a computing center's programmer costs were often already comparable to the cost of the computer itself — and the machine still spent a quarter to half its time just debugging programs.

Computers kept getting faster. People became the bottleneck.

{{< figure src="/images/history-rhymes-fortran-to-ai/manual-translation-to-compiler.webp" alt="1950s programmer manually translating ADD A+B into LOAD/ADD/STORE/JUMP instruction cards; 1960s+ programmer just writes C=A+B and lets the compiler spit out the binary automatically" caption="From manual translation to letting the compiler do it automatically" >}}

---

## 03 · Why Not Let the Machine Do Its Own Translating?

The real turning point came from a question that sounds obvious today but was genuinely bold at the time:

> If programmers were spending all their time translating, why not let the computer do that translation itself?

Around 1954, John Backus and his team at IBM set out to build FORTRAN.

That whole string of low-level operations could now be written closer to how a person actually thinks:

```fortran
C = A + B

IF (C .GT. 100) GO TO 20
```

The programmer only had to express what they wanted to compute.

Generating the machine instructions, reading the data, handling the jumps — all of that was now the compiler's job.

The division of labor between human and machine shifted:

> **The person's job is to express intent. The machine's job is to translate that into code it can execute.**

---

## 04 · Back Then, Programmers Didn't Trust the Machine Either

Professional programmers didn't buy into it at first.

And honestly, that skepticism made sense.

Early automatic programming systems tended to produce code that just wasn't fast enough. Computers were so expensive back then that if the generated code ran noticeably slower than what a skilled programmer wrote by hand, the whole idea had no real value.

So the question the FORTRAN team actually had to answer wasn't "can we generate code automatically" — it was:

> Could machine-generated code be good enough that a professional programmer would actually trust it?

{{< figure src="/images/history-rhymes-fortran-to-ai/we-shipped.webp" alt="1957 programmer holding a tape from the FORTRAN compiler, hesitantly asking 'does this actually work? do we just ship it?'; 2026 programmer watching Codex finish running tests, shouting 'tests pass? ship it!'" caption="Then: we didn't know. But we shipped." >}}

In the end, they pulled it off. FORTRAN I's code generation was optimized well enough to compete with what a strong programmer would write by hand.

We're asking a version of the same question about AI today: it can write the code, but can what it writes be understood, verified, maintained over time — and can someone actually take responsibility for it?

Seventy years ago, we were building trust in the compiler.

Today, we're building trust in AI.

---

## 05 · When a Technology Proves Its Value, Organizations Change

What actually changed things wasn't just the compiler maturing as a technology — it was the compiler proving its economic value.

The first FORTRAN compiler shipped in 1957. The numbers showed it had cut programming and debugging costs to roughly a quarter of what they'd been.

To a business, that wasn't just a new piece of technology anymore — it was a genuinely more efficient way to produce software.

A survey of 26 IBM 704 sites in April 1958 found that more than half of them were already using FORTRAN for more than half their workload — and at many sites, FORTRAN usage had already passed 80%.

From the first attempt in 1954, to something actually usable in 1957, to rapid adoption by 1958 — the whole process took just a few years.

What's really worth noticing here is that the thing driving the change was no longer individual programmers' preferences. Cost and efficiency had entered management's decision-making.

> **Once a technology stops being about whether it's nice to use, and starts being about whether skipping it hurts your costs and your competitiveness, organizational change happens fast.**

{{< figure src="/images/history-rhymes-fortran-to-ai/value-to-business-adoption-en.webp" alt="Technology emerges, engineers evaluate, value gets validated, business decides, adoption scales, industry accelerates: 1950s programmers doubting whether the compiler really beats manual coding, then adopting it once cost and efficiency gains were proven; 2020s team looking at AI coding data — development time -60%, engineering effort -50%, delivery speed +80% — and adopting it organization-wide" caption="Technology creates the possibility. Value drives adoption. Business scales the future." >}}

Assembly didn't disappear. But fewer and fewer people needed to write it by hand — the machine had taken over work that used to require a person doing the translating.

---

## 06 · When Writing Code Gets Easy, Engineering Judgment Becomes the Scarce Resource

The history that followed FORTRAN already gave us one answer to this.

As writing programs got easier, software didn't get simpler — it got bigger and more complex. The hard problem shifted from "how do I write this code" to how you design systems, organize collaboration, ensure quality, and maintain things over the long run.

By 1968, software engineering had emerged as a discipline in its own right, taken seriously as an engineering problem.

And a lot of the new problems automation created ended up getting solved by more automation: compilers needed optimizing, so we got automatic optimization; programs got more complex, so we got static analysis, automated testing, and a whole family of verification tools.

What beats magic, more often than not, is more magic.

The same is probably true today. AI is making code production faster and faster, but the new bottlenecks it creates — quality, testing, verification — won't stay dependent on someone reading every line by hand forever. Those will get automated further too.

So what's actually going to be scarce in the future probably isn't writing code, or even just reviewing it. It's this:

> **Defining the problem, understanding the business, designing the system, setting the standard, judging the outcome — and ultimately owning the result.**

Whenever a technology rapidly democratizes some capability, the real opportunity tends to show up in whatever new problem it exposes next.
