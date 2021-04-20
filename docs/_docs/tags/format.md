---
title: Format
category: Tags
order: 7
---

Applies a custom format to the value of an element

## Syntax

&lt;&lt;Tag\|Format&gt;&gt; <span class="badge platform">Client</span>&nbsp;<span class="badge platform">Server</span>

#### Tag <span class="badge platform">Required</span>
Tag name of element

#### Format

Client-side tags only support [Date/Time](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) formats. Format can be left blank, which will force the value to be formatted using the underlying Type or Format of the element.

Server-side tags support [Numeric](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings) and [Date/Time](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) formats.

## Examples

|Context|Format|Result|
|---|---|---|
|Client|&lt;&lt;Total\|&gt;&gt;|$100.00|
|Server|&lt;&lt;Amount\|000000&gt;&gt;|000100|
|Both|&lt;&lt;OrderDate\|ddMMyyyy&gt;&gt;|20012021|
