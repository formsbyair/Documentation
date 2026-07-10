---
title: Functions > ElementAt
category: Tags
order: 5
---

Iterates through a repeater with optional filter and returns output for the item with specified index

To return a single value for an item from an unfiltered repeater use: &lt;&lt;Repeater[Index].Tag&gt;&gt;

## Syntax

&lt;&lt;[**ElementAt(Index)**:Repeater{Filter}:Output]&gt;&gt; <span class="badge platform">Server</span>

#### Index <span class="badge platform">Required</span>
Zero based index of item

#### Repeater <span class="badge platform">Required</span>
Tag name of repeater

#### Filter
Boolean expression to filter repeater items e.g. {&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}

#### Output <span class="badge platform">Required</span>
Text and &lt;&lt;tags&gt;&gt; for repeater item e.g. &lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;

## Examples

|Function|Result|
|---|---|
|&lt;&lt;[ElementAt(1):Contact{&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;|Mary Bloggs|
