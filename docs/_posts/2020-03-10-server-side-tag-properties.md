---
title: Server side tag properties
type: feature
---

FormsByAir will now evaluate **properties** in server-side tags to be consistent with client-side (in-form) evaluation.

For example, you may now refer to a Data Source or Lookup element with &lt;&lt;Product.Name&gt;&gt; in a data integration map.

Previously you would have had to create a hidden formula element with expression '&lt;&lt;Product.Name&gt;&gt;' and refer to that element in your data integration map.