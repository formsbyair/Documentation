---
title: Form design validation
type: platform
---

Added validation to the form designer to block hidden formulas and conditional paths within inline or tabular groups. These aren't supported because they'd potentially cause column alignment issues.

Also added validation to ensure that Tag Names don't contain &#39; &quot; &lt; [ ] &gt;