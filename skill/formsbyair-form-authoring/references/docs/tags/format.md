---
title: Format
category: Tags
order: 10
---

Applies a custom format to the value of an element

## Syntax

&lt;&lt;Tag\|Format&gt;&gt; <span class="badge platform">Client</span>&nbsp;<span class="badge platform">Server</span>

#### Tag <span class="badge platform">Required</span>
Tag name of element

#### Format

Client-side tags only support [Date/Time](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) formats, or leave Format blank to force the value to be formatted using the underlying Type or Format of the element.

Server-side tags support [Numeric](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings) and [Date/Time](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) formats.

For attachment questions in template-driven documents, provide a width to output the attached image at that size instead of the filename e.g. &lt;&lt;Photo\|500&gt;&gt;. Supported image types are png, jpg, jpeg, gif and bmp - for any other file type the filename is output as usual.

## Examples

|Context|Format|Result|
|---|---|---|
|Client|&lt;&lt;Total\|&gt;&gt;|$100.00|
|Server|&lt;&lt;Amount\|000000&gt;&gt;|000100|
|Both|&lt;&lt;OrderDate\|ddMMyyyy&gt;&gt;|20012021|
|Server|&lt;&lt;Photo\|500&gt;&gt;|Attached image displayed at width 500|
