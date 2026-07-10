---
title: Multiple email recipients
type: platform
---

We've addressed a long-standing quirk/bug for email integrations with multiple recipients.

Historically, an email integration with multiple recipients would result in a separate email being sent for each recipient. If the integration included a CC or BCC list, those people would receive the email multiple times, once for each recipient.

We've changed it to work how most people would expect, where a single email is sent to all recipients.

If a recipient needs to be hidden from others they should be added to the BCC list.