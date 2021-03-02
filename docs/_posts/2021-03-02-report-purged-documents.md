---
title: Report purged documents
type: platform
---

We've updated **Report** integrations so they will now include purged documents by default.

&lt;&lt;[Document]&gt;&gt; tags in report templates will return data for *all* documents, but tags referring to form data will only be populated for documents that haven't been purged.

Purged documents can be excluded from reports by adding the following condition to your report integration.

&lt;&lt;[DocumentPurgedDateTime]&gt;&gt; == ''