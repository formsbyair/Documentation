---
title: Functions > First
category: Tags
order: 6
---

Returns output for the first item in a repeater with optional filter

## Syntax

&lt;&lt;[**First**:Repeater{Filter}:Output]&gt;&gt; <span class="badge platform">Server</span>

#### Repeater <span class="badge platform">Required</span>
Tag name of repeater

#### Filter
Boolean expression to filter repeater items e.g. {&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}

#### Output <span class="badge platform">Required</span>
Text and &lt;&lt;tags&gt;&gt; for repeater item e.g. &lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;

## Examples

|Function|Result|
|---|---|
|&lt;&lt;[First:Contact{&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;|Mary Bloggs|
