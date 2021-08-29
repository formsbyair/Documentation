---
title: Conditional last section
type: platform
---

Previously, forms with *conditional* sections would always need a final section that was *not* conditional in order to function correctly.

We've applied a change so that this is no longer required.

The last non-conditional section will show a Submit button as before. On Submit, if the condition for the next section is not met, the form is submitted. If the condition is met, the next section is displayed, and the progress bar is updated accordingly. If the user moves back and updates the form so the condition is no longer met, then clicks Next, the form will recognise that the next section is no longer applicable, and will stay in place, change the Next button to Submit, and update the progress bar.