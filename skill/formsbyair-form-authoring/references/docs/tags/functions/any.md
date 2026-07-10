---
title: Functions > Any
category: Tags
order: 2
---

Returns true if there is at least one occurence of a Repeater item, otherwise false

## Syntax

&lt;&lt;[**Any**:Repeater{Filter}]&gt;&gt; <span class="badge platform">Client</span>&nbsp;<span class="badge platform">Server</span>

#### Repeater <span class="badge platform">Required</span>
Tag name of repeater

#### Filter
Boolean expression to filter repeater items e.g. {&apos;&lt;&lt;Type&gt;&gt;&apos; == &apos;Primary&apos;}

## Examples

|Function|Result|
|---|---|
|&lt;&lt;[Any:Contact]&gt;&gt;|true|
|&lt;&lt;[Any:Contact{&apos;&lt;&lt;Type&gt;&gt;&apos; != &apos;Primary&apos;}]&gt;&gt;|false|