---
title: Format
category: Tags
order: 7
---

Applies a custom format to the value of an element

## Syntax

&lt;&lt;Tag\|Format&gt;&gt; <span class="badge platform">Server</span>

#### Tag <span class="badge platform">Required</span>
Tag name of element

#### Format
Custom format string, see [Numeric](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings) and [Date/Time](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings)

## Examples

|Format|Result|
|---|---|
|&lt;&lt;Amount\|000000&gt;&gt;|000100|
|&lt;&lt;OrderDate\|ddMMyyyy&gt;&gt;|20012021|
