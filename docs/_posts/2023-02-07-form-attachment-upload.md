---
title: Form attachment upload
type: platform
---

We've made a change to how form attachments are uploaded to our servers when a form is saved or submitted.

Previously all attachments and form data were combined in to **one** request, this has worked well for the vast majority of form users. 

However we occasionally see problems with forms that have a large number of attachments, submitted over slower internet connections e.g. insurance claims with photos submitted on mobile data.

To help improve reliability, our system will now split out each file attachment to a separate request, and then upload form data at the end. We'll also now show a progress meter while attachments are uploading so users have an indication of how long the process is going to take.