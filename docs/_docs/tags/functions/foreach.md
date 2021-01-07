---
title: Functions > ForEach
category: Tags
order: 1
---

Iterate through a repeater and parse the output for each item
<span class="badge platform">Client</span>&nbsp;<span class="badge platform">Server</span>

#### Syntax

&lt;&lt;[ForEach:Repeater{Filter}[Separator]:Output]&gt;&gt;

##### Repeater (Required)
Tag name of repeater

##### Filter (Optional)
Boolean expression to filter each repeater item e.g. {&apos;&lt;&lt;Type&gt;&gt;&apos; != &apos;Main&apos;}

##### Separator (Optional)
Custom separator between the output for each item e.g. [ and ] (defaults to a space)

##### Output (Required)
Text and &lt;&lt;tags&gt;&gt; e.g. &lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;

Example: &lt;&lt;[ForEach:Client{&apos;&lt;&lt;Type&gt;&gt;&apos; != &apos;Main&apos;}[ and ]:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;

Result: Joe Bloggs and Tim Apple