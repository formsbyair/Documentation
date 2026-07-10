---
title: Functions > Fallback
category: Tags
order: 7
---

Return the first non-empty tag value or optional literal value

## Syntax

&lt;&lt;[**Fallback**:&lt;&lt;Tag1&gt;&gt;&lt;&lt;Tag2&gt;&gt;LiteralValue]&gt;&gt; <span class="badge platform">Server</span>

#### Tags <span class="badge platform">Required</span>
One or more tags

#### Literal Value
Literal value to return if all tags are empty (optional)

## Examples

|Function|Result|
|---|---|
|&lt;&lt;[Fallback:&lt;&lt;PreferredFirstName&gt;&gt;&lt;&lt;FirstName&gt;&gt;]&gt;&gt;|Jimmy|
|&lt;&lt;[Fallback:&lt;&lt;PhoneNumber&gt;&gt;None]&gt;&gt;|None|