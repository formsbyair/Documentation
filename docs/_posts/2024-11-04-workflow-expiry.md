---
title: Workflow expiry
type: platform
---

As part of our data retention policy to minimise the time that form data is held in our system, we're planning to introduce rolling expiry to Workflow effective **1 December 2024**

The default workflow expiry period will be **60 days** but this can be adjusted per form between 10 and 90 days. A "rolling expiry" means that the expiry period will reset every time you take some action e.g. reassign, comment, authorise, so a document will never expire while you're actively working on it.

In addition, we're adding a **Snooze** function so you can hold a document in Workflow for a specific period of time if it can't be processed immediately. Snoozed documents will be hidden by default unless you specifically filter for them, and will reappear at the end of the snooze period, triggering a notification to the user that initiated the snooze.

We'll display the expiry date for all workflow documents in our portal and allow you to filter for documents that are expiring soon.

On expiry, our system will send an automated email notification to the relevant assignee or team. The document can then be restored if necessary within the data retention period for your account. You can continue to set custom reminder emails at any frequency for documents in Workflow.

We also plan to make the following related changes:

* Documents in **Requesting** status after 30 days will now automatically move to Workflow Pending status for review if workflow is enabled for the form, otherwise they will expire. "Requesting" means a form has been submitted but is waiting on post-submit ID verification. You can continue to set custom reminders at any frequency for documents in Requesting status.

* The **Edited** workflow status will be retired, as this masks a document's true status, and we already record edits in the Workflow log

We'll reset the expiry clock on all documents in Workflow when we apply this change on 1 December, even if they've already been in workflow for some time. As such the earliest that any document will expire (assuming the 60 day default) is 30 January 2025.

We'll be in touch directly if you have a large number of very old documents in workflow so we can discuss options to bulk export or expire them.