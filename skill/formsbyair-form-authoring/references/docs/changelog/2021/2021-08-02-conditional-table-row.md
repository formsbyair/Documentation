---
title: Conditional table row
type: platform
---

We've updated our Word Document template engine to support conditional table rows using &lt;&lt;[Condition:Expression]&gt;&gt;

The Condition tag can be included in any cell but must only appear once per row.

If the expression evaluates to true, the Condition tag is removed and the row is preserved. If the expression evaluates to false then the entire row is removed.

This may be useful where you need to show/hide chunks of formatted content within a Word document.