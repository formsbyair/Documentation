---
title: JSON system properties
type: platform
---

FormsByAir will now include the following system properties in auto generated (non-mapped) JSON for all output types including File, Webhook and Azure CosmosDB.

|Property|Equivalent to|
|---|---|
|_DocumentId|&lt;&lt;[DocumentId]&gt;&gt;|
|_DocumentFormName|&lt;&lt;[DocumentFormName]&gt;&gt;|
|_DocumentOwnerName|&lt;&lt;[DocumentOwnerName]&gt;&gt;|

If you're generating *custom* JSON you can reference any [System Tag]({{ site.baseurl }}/tags/system_tags) in your map.