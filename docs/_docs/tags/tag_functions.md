---
title: Tag Functions
category: Tags
order: 2
---

### &lt;&lt;[ForEach]&gt;&gt;
<span class="badge platform">Client</span><span class="badge platform">Server</span>

Iterate through a repeater and parse the output for each item

#### Syntax

&lt;&lt;[ForEach:Repeater{Filter}[Separator]:Output]&gt;&gt;

##### Repeater (Required)
Tag name of repeater

##### Filter (Optional)
Boolean expression to filter each repeater item e.g. {&lt;&lt;Amount&gt;&gt; > 0}

##### Separator (Optional)
Custom separator between the output for each item e.g. [ and ] (defaults to a space)

##### Output (Required)
Text and &lt;&lt;tags&gt;&gt; e.g. &lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;

Example: &lt;&lt;[ForEach:Client{&lt;&lt;Amount&gt;&gt; &gt; 0}[ and ]:&lt;&lt;FirstName&gt;&gt; &lt;&lt;LastName&gt;&gt;]&gt;&gt;
Result: Joe Bloggs and Tim Apple