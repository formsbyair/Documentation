---
title: Functions > ForEach
category: Tags
order: 1
---
<span class="badge platform">Client</span>&nbsp;<span class="badge platform">Server</span>

Iterate through a repeater and parse the output for each item

## Syntax

&lt;&lt;[ForEach:Repeater{Filter}[Separator]:Output]&gt;&gt;

#### Repeater <span class="badge platform">Required</span>
Tag name of repeater

#### Filter
Boolean expression to filter each repeater item e.g. {&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}

#### Separator
Custom separator between the output for each item e.g. [ and ] (defaults to a space)

#### Output <span class="badge platform">Required</span>
Text and &lt;&lt;tags&gt;&gt; e.g. &lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;

## Examples

|Function|Result|
|---|---|
|&lt;&lt;[ForEach:Contact:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;|Joe Bloggs Mary Bloggs Tim Bloggs|
|&lt;&lt;[ForEach:Contact[ and ]:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;|Joe Bloggs and Mary Bloggs and Tim Bloggs|
|&lt;&lt;[ForEach:Contact{&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}[ and ]:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;|Joe Bloggs and Mary Bloggs|

