---
title: Workflow Assignment Changes
type: platform
---

#### Authorisation Assignment Expression

Previously, if this expression was left blank or evaluated to an empty string, documents would require authorisation by the *manager* of the current workflow user.

A blank or empty assignment expression now means a document will advance directly to **Authorisation** status so it can be authorised by the current workflow user.

If a form still needs authorisation from the current user's manager, **Authorisation Assignment Expression** should be set to &apos;&lt;&lt;[DocumentWorkflowUserManagerEmail]&gt;&gt;&apos;

#### Assign document to form user's manager for approval

The workflow option **Assign document to form user's manager for approval** has been removed. This can be replicated by setting **Assignment Expression** to &apos;&lt;&lt;[DocumentUserManagerEmail]&gt;&gt;&apos;