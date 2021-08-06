---
title: Object tag value
type: feature
---

FormsByAir will now return the value of the Display property for tags that reference an object within a form, and don't specify a property.

For example, if you had a Typeahead based on the Country system table, you would need to use &lt;&lt;Country.Name&gt;&gt; to return the name of the selected country, &lt;&lt;Country&gt;&gt; on it's own would return [object Object]

Now &lt;&lt;Country&gt;&gt; will return the value of the Name property, consistent with server-side tag evaluation.
