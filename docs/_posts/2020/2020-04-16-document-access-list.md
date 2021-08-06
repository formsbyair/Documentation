---
title: Document Access List
type: feature
---

Added new form-level option to specify a list of FormsByAir users that can access documents (saves/requests/submissions) for a form.

If this is blank (the default), all FormsByAir users in the Workflow role or higher can access documents for the form.

If you specify a list of users, documents will be omitted from all portal views and access via direct link blocked for all users that are *not* in the Document Access List.

This is useful where you need to limit access and workflow actions for sensitive documents to a subset of your users.

This does *not* apply to Administrators, who can access all documents.