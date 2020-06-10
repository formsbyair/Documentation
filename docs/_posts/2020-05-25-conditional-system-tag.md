---
title: Conditional system tag
type: platform
---

Added new **Conditional** system tag with usage as follows:

&lt;&lt;[Conditional:{condition}:{output if condition is true}]&gt;&gt;

For example: 

&lt;&lt;[Conditional:&apos;<<Description>>&apos; != &apos;&apos;:Description&lt;br&gt;&lt;&lt;Description&gt;&gt;]&gt;&gt;

This is useful where the ouput contains formatting including new-line characters.

A similar result can be achieved with an **Expression** system tag, and an expression that contains a ternary operator, for example:

&lt;&lt;[Expression:&apos;<<Description>>&apos; != &apos;&apos; ? &apos;Description&lt;br&gt;&lt;&lt;Description&gt;&gt;&apos; : &apos;&apos;]&gt;&gt;

The problem with this approach is that the whole expression is **evaluated**, so new-line and other characters are removed.