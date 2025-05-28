---
title: Workflow Authorisation
type: platform
---

We've made a few improvements to Authorisation, which is an optional feature of workflow.

* If your form is configured with an **Authorisation Assignment Expression** (meaning the current workflow user must request authorisation from a different person) then the "Decline" button will now appear as "Revert". The functionality behind this button hasn't changed, we've just made it more obvious that the form will be sent back to the person that requested authorisation if it can't be authorised.

* The system will now prevent you from assigning a form to someone that doesn't have permission to authorise it during **Authorisation**

* If your form is *not* configured with an **Authorised Assignment Expression** (meaning the person authorising the form can also approve it) we'll now automatically Approve the form on Authorisation, saving an additional click (and potential confusion)