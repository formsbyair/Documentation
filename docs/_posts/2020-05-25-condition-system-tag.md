---
title: Condition system tag
type: platform
---

Added new **Condition** system tag with usage as follows:

&lt;&lt;[Condition:{condition}:{output if condition is true}]&gt;&gt;

For example: 

&lt;&lt;[Condition:&apos;&lt;&lt;Description&gt;&gt;&apos; != &apos;&apos;:Description&lt;br&gt;&lt;&lt;Description&gt;&gt;]&gt;&gt;

This is useful where the ouput contains formatting including new-line characters.

A similar result can be achieved with an **Expression** system tag and a conditional operator, for example:

&lt;&lt;[Expression:&apos;&lt;&lt;Description&gt;&gt;&apos; != &apos;&apos; ? &apos;Description&lt;br&gt;&lt;&lt;Description&gt;&gt;&apos; : &apos;&apos;]&gt;&gt;

However in this case the whole expression is **evaluated**, so new-line and other characters are removed.