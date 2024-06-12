---
title: Two Factor Submit
type: platform
---

We've added support for email-based two factor authentication when submitting prefilled forms.

This can be enabled and used as follows:

* Set Submission Mode to **Code**
* Add a new "On Submit Code" email integration. The recipient of the email should be &lt;&lt;[DocumentRequestedEmail]&gt;&gt; and the body of the message should contain &lt;&lt;[DocumentSubmitCode]&gt;&gt;
* Prefill the form using our API, set **RequestedEmailAddress** to the email address you hold for the form-filler
* When the form is submitted, FormsByAir will send your "On Submit Code" email to **RequestedEmailAddress** including a 6-character short-lived code
* A valid code must be entered in to the form to complete submission
* This does not affect the ability to save forms