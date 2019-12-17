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
* Data referenced by &lt;&lt;tags&gt;&gt; in a Template (in the format of the target file); or
* Data referenced by &lt;&lt;tags&gt;&gt; in a FormsByAir JSON Data Map

|Format|Description|Template/Map|Output|
|---|---|
|CSV From Template|Comma Separated Values file|||
|Excel Workbook|||[Sample]({{ site.baseurl }}/samples/excel-output.xlsx)|
|Excel Workbook From Template||||
|JSON|Uses Question Tags for property names if set, otherwise Question Id||[Sample]({{ site.baseurl }}/samples/json-output.json)|
|JSON From Map||[Sample]({{ site.baseurl }}/samples/json-map.json)|[Sample]({{ site.baseurl }}/samples/json-map-output.json)|
|PDF|||[Sample]({{ site.baseurl }}/samples/pdf-output.pdf)|
|PDF From Template||||
|PDF From Attached Template|Uses template from Attachment within a document|||
|PDF From Fillable PDF|Populates PDF fields by name|||
|Text||||
|Text From Template||||
|Web Page|HTML file||[Sample]({{ site.baseurl }}/samples/web-page-output.html)|
|Word Document|||[Sample]({{ site.baseurl }}/samples/word-output.docx)|
|Word Document From Template||||
|XML Document|Native FormsByAir XML document||[Sample]({{ site.baseurl }}/samples/xml-output.xml)|
|XML From Template|||||
|XML From Map||[Sample]({{ site.baseurl }}/samples/xml-map.json)|[Sample]({{ site.baseurl }}/samples/xml-map-output.xml)|

#### Exclusion List

List of tags to exclude from files that output all form data, for example:
&lt;&lt;Introduction&gt;&gt;&lt;&lt;RiskRating&gt;&gt;