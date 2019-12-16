---
title: File
category: Integrations
order: 2
---

Send form data in a file.

## Settings

#### File Format

Files will contain either:

* All non-hidden form data apart from Exclusions; or
* Data referenced by &lt;&lt;tags&gt;&gt; in a Template (in the format of the target file)
* Data referenced by &lt;&lt;tags&gt;&gt; in a FormsByAir JSON Data Map

|Format|Description|Output Sample|Template/Map Sample|
|---|---|
|CSV From Template|Comma Separated Values file|||
|Excel Workbook||||
|Excel Workbook From Template||||
|JSON||[Sample]({{ site.baseurl }}/samples/json-output.json)||
|JSON From Map||[Sample]({{ site.baseurl }}/samples/json-map-output.json)|[Sample]({{ site.baseurl }}/samples/json-map.json)|
|PDF||||
|PDF From Template||||
|PDF From Attached Template|Uses template from Attachment within a document|||
|PDF From Fillable PDF|Populates PDF fields by name|||
|Text||||
|Text From Template||||
|Web Page|HTML file|||
|Word Document||||
|Word Document From Template||||
|XML Document|Native FormsByAir XML document|||
|XML From Template|||||
|XML From Map||||

#### Exclusion List

List of tags to exclude from files that output all form data, for example &lt;&lt;Introduction&gt;&gt;&lt;&lt;RiskRating&gt;&gt;