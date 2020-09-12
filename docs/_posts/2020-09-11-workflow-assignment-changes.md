---
title: Workflow Assignment Changes
type: platform
---

The behaviour of documents in relation to **Authorisation Assignment Expression** has changed as follows:

If this expression was left blank, or evaluated to an empty string, documents would previously require authorisation by the Manager of the current workflow user.

Instead, documents with no authorisation assignment will now advance directly to **Authorisation** status, and can be authorised by the current workflow user.

If the expression evaluates to a valid user, submitted documents will default to pending status, and the current user will need to **Request Authorisation** as before.

The previous behaviour of assigning to a manager can be replicated by setting Authorisation Assignment Expression to '&lt;&lt;[DocumentWorkflowUserManagerEmail]&gt;&gt'


In addition, the workflow option "Assign document to form user's manager for approval" has been removed. This can be replicated by setting **Assignment Expression** to '&lt;&lt;[DocumentUserManagerEmail]&gt;&gt'