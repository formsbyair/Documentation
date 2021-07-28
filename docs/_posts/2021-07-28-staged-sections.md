---
title: Staged sections
type: platform
---

We've applied an update so that sections within a **staged** form can now be configured to behave like they do in a non-staged form with a progress bar and Back/Next buttons.

This may be useful where you have a large form that needs to be split in to sections for the main form filler, but the final section for manager approval needs to be completed as a separate stage for example.

You can configure a section to proceed directly to the next section by setting **Next Stage Expression** to **true**. Any section where **Next Stage Expression* is left blank will be treated as a stage, with discrete submission.

You can also continue to set **Next Stage Expression** to a boolean expression. In this case, the form won't show a Next button or progress bar, but will still proceed directly to the next section if the expression evaluates to true.