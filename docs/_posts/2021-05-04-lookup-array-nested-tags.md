---
title: Lookup array nested tags
type: fix
---

**Lookup** questions now support nested tags in the **Data Array** setting, for example:

&lt;&lt;&lt;[DataSource.Rows.filter(function(row) { return row.Something == &apos;&lt;&lt;Something&gt;&gt;&apos;})]&gt;&gt;&gt;