---
title: Document max lifetime
type: platform
---

We've added a new, optional account level setting **Max Lifetime** which defines the maximum number of days that we will hold form data for each document.

When set, any document that was started before the max lifetime threshold will be purged without notification, irrespective of status.

Our system is designed for all documents to be delivered or eventually expire, however documents that are **Saved** or in **Workflow** use *rolling* expiries, and can be retained indefinitely with continuous engagement.

This new feature serves as a hard limit to guarantee that we only hold form data for a specific period, which may be useful for compliance with privacy policies.

Reminders can be set for any document status to avoid unintended loss of data.