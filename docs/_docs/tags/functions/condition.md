---
title: Functions > Condition
category: Tags
order: 3
---

Evaluates a boolean expression and returns the output if true

## Syntax

&lt;&lt;[**Condition**:Expression:Output]&gt;&gt; <span class="badge platform">Server</span>

#### Expression <span class="badge platform">Required</span>
Boolean expression e.g. &apos;&lt;&lt;Option&gt;&gt;&apos; == &apos;A&apos;

#### Output <span class="badge platform">Required</span>
Text and &lt;&lt;tags&gt;&gt; e.g. Option A

## Examples

|Function|Result|
|---|---|
|&lt;&lt;[Condition:&apos;&lt;&lt;Option&gt;&gt;&apos; == &apos;A&apos;:Option A]&gt;&gt;|Option A|
|&lt;&lt;&lt;[Condition:&lt;&lt;[All:Contact{&apos;&lt;&lt;Type&gt;&gt;&apos; != &apos;Primary&apos;}]&gt;&gt;:All contacts are primary]&gt;&gt;&gt;|All contacts are primary|
