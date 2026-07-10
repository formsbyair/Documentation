---
title: Delivery validation
type: platform
---

We've added a new validation type **Delivery** for validations that need to run as the last step before a form is delivered.

For forms that *don't* use Workflow this type of validation is no differerent to **Post-Submit**

If Workflow is enabled, validation is triggered when a form is *Approved* or *Bypassed*

We added this validation type to support our Docusign integration, where signing a document must happen *after* any review or change in Workflow, but it may be useful for other integrations in future.