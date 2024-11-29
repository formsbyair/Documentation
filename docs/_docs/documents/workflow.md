---
title: Workflow
category: Documents
order: 5
---

Workflow is an optional feature of the FormsByAir platform that can be used where form submissions need manual review and approval before delivery to external systems, often for compliance with internal processes or regulatory standards.

When enabled, workflow can apply to all submissions, or only those that meet certain criteria, for example, where the form filler is an “entity”, and you need to check that all people related to the entity have been captured in the form.

Submitted forms (documents) are automatically added to the workflow queue, and email notifications are sent to your team. Documents can be assigned to specific people based on rules that you define, or self-assigned. Managers can review the queue to ensure that documents are reviewed and processed in a timely manner, and re-assign as required.

![]({{ site.baseurl }}/images/workflow/workflow1.png)

When opening a document in workflow, our system will display a read-only view of the submitted information, along with any workflow-specific content - essentially the “for office use only” part of traditional forms. Workflow content is only visible to your team, and is useful for check-lists or additional information that should be delivered alongside the document to external systems.

![]({{ site.baseurl }}/images/workflow/workflow2.png)

After reviewing a document, workflow users can take one of the following actions:
* If the document meets all criteria, it can be **Approved**, which will trigger delivery to external systems.
* If the document requires more information or changes, it can be **Returned** to the form filler so they can update and re-submit it.
* If the document needs review by another person, it can be **Assigned** to them with a comment.
* If the review process has started but is going to take more time, the form can be set to **Reviewed** status to differentiate it from documents that haven’t been looked at yet.
* If a document can’t be processed for a specific period of time, it can be **Snoozed** which will hide it from the workflow queue until the end of the snooze period.
* In rare cases where the document cannot proceed, it can be **Declined**, which will remove it from the workflow queue, and prevent delivery to external systems.

![]({{ site.baseurl }}/images/workflow/workflow3.png)

All workflow actions can trigger email notifications to your team or form fillers.

**Authorisation** can be enabled if certain documents require sign-off from a senior manager in addition to operational approval.

Reminders can be setup to flag documents that have been in workflow beyond a certain threshold. 

Documents in workflow are subject to rolling expiry. The default workflow expiry period is 60 days but this can be adjusted per form between 10 and 90 days. A “rolling expiry” means that the expiry period will reset every time you take some action e.g. reassign, comment, authorise, so a document will never expire while you’re actively working on it. On expiry, our system will send an automated email notification to the assignee, or users that have interacted with the document, or all workflow/admin users. The document can then be restored if necessary within the data retention period for your account.

An audit log provides a permanent record of all workflow actions over time.

![]({{ site.baseurl }}/images/workflow/workflow4.png)

### Workflow status diagram


![]({{ site.baseurl }}/images/workflow/workflowcycle.svg)