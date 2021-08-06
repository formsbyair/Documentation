---
title: Preserve JSON data values
type: fix
---

FormsByAir had previously "flattened" JSON values for **Data Source**, **Lookup** and **Typeahead** elements to the Name property only when merging third party requests or returning a document.

This meant any subsequent reference to properties within tags e.g. &lt;&lt;Country.Code&gt;&gt; would return an empty string.

JSON values are now never flattened.