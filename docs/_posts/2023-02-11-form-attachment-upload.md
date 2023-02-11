---
title: Form attachment upload
type: platform
---

We've made a couple of changes to help improve the reliability of submitting forms with multiple/large attachments, particularly over slower internet connections.

Our system will now split out each file attachment to a separate request, and then upload form data at the end. In addition, we'll automatically retry requests several times if the connection is interrupted part way through.

We'll also now show percent complete while attachments are uploading so users have an indication of how long the process will take.