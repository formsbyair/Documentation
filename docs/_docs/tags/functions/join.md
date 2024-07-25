---
title: Functions > Join
category: Tags
order: 9
---

Join multiple tag values with optional separator

## Syntax

&lt;&lt;[**Join**:[Leading Separator]&lt;&lt;Tag1&gt;&gt;&lt;&lt;Tag2&gt;&gt;[Trailing Separator]]&gt;&gt; <span class="badge platform">Client</span>&nbsp;<span class="badge platform">Server</span>

#### Tags <span class="badge platform">Required</span>
Two or more tags to join

#### Separator
Leading or trailing separator between the output for each tag e.g. [, ] defaults to a trailing space


## Examples

|Function|Result|
|---|---|
|&lt;&lt;[Join:&lt;&lt;FirstName&gt;&gt;&lt;&lt;MiddleName&gt;&gt;&lt;&lt;LastName&gt;&gt;]&gt;&gt;|Joe Bloggs|
|&lt;&lt;[Join:&lt;&lt;Address1&gt;&gt;&lt;&lt;Address2&gt;&gt;&lt;&lt;City&gt;&gt;&lt;&lt;PostalCode&gt;&gt;[, ]]&gt;&gt;|100 Queen Street, Auckland, 1000|