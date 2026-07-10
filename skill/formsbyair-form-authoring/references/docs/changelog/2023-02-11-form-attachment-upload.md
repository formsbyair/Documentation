---
title: Form attachment upload
type: platform
---

We've made a few changes to help improve the reliability of submitting forms with multiple/large attachments, particularly over slower internet connections.

Our system will now split out each file attachment to a separate request, then upload form data at the end. Failed requests will be retried automatically, for example, where the connection is interrupted part way through.

We'll also now show percent complete while attachments are uploading so users have an indication of how long the process will take.