---
title: "Label Your Tech Debt"
date: 2022-03-29T15:41:21-05:00
draft: false
---

Tech debt is unavoidable. Today's solution might not be what you need in 12 months or even next week if you have rapidly evolving requirements. Those outdated solutions should be met with understanding and a corrective course of action.

It's okay to choose a solution that will likely end up in the Fix Later™ pile as there are many reasons to go with an approach that will be heavily modified or completely replaced. Here are three:

#### Time Crunch

If you need something tomorrow, the 3 month approach simply won't work. You have to act... quickly. This is obviously not ideal but you should learn to cope then start documenting. Make it known why you chose the unoptimal solution. I'd rather read someone rant in a comment about not having enough time/energy to do what they want instead of being thrown into the void and left to Just Figure it Out™.

#### Shifting Requirements

Requirements _will_ change. If you're astute/lucky enough, you'll have some idea of how they _could_ change and will be able to side-step major headaches. With experience, potential hotspots or areas of concern will reveal themselves before they become a problem. If you don't have a clear understanding of what lies ahead then reach out to colleagues/friends, use the resources available to you in order to prevent future headaches. You won't always wind up where you wanted but you've most certainly learned a lot getting there.

#### Proof of Concept

Proving an idea doesn't necessarily require complete solutions. However, PoC's (Proof of Concepts) often find themselves running on prod, tech debt included. Combating this is hard. You're likely getting pushed to pump out new features while simultaneously plugging holes that have opened or knowingly been left to Fix Later™.

### Labeling Tech Debt

We can dull the sharper edges of these scenarios by taking note of key points while fully engaged in the problem at hand. This is very important. The goal is to provide as much context for our future selves by outlining where we want to be, why we aren't there, and why we chose the solution at hand. I suffer from habitual context switching which is detrimental to remembering the finer and important details behind decision making. To counter this, it's imperative that I jot down my thoughts before the context switch happens.

Let's run through an example.

Some decisions aren't ready to be made.

That's Okay. Keep going. You will turn heads by showing off the unoptimized features you've implemented versus attracting unwanted attention by holding back releases or demos because you need to hit O(n log n). No one cares about O(n^3) on your list of 1000.
