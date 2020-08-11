---
title: Repeater Minimum Rows expression
type: fix
---

You can now specify an *expression* for the **Minimum Rows** property of repeaters. Previously you could only use a fixed value for Minimum Rows. **Maximum Rows** has always allowed a fixed value or an expression.

When a minimum has been set, FormsByAir will pre-load empty rows, and prevent the user from removing rows when at the minimum.

FormsByAir will evaluate an expression for Minimum Rows when a form, section, or conditional path containing the repeater is loaded.