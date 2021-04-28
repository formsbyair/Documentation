---
title: Option name
type: platform
---

We've extended the functionality described [here]({{ site.baseurl }}/changelog/#/2020/07/15/boolean-option-tag-values) to support a Name property for **Option** questions as follows:

|Tag|State|Client result|Server result|
|---|---|---|---|
|&lt;&lt;Option.Name&gt;&gt;|Selected|Question Title|Question Title|
|&lt;&lt;Option.Value&gt;&gt;|Selected|true|true|
|&lt;&lt;Option&gt;&gt;|Selected|true|Question Title|
|&lt;&lt;Option.Name&gt;&gt;|Not Selected|&lt;blank&gt;|&lt;blank&gt;|
|&lt;&lt;Option.Value&gt;&gt;|Not Selected|false|false|
|&lt;&lt;Option&gt;&gt;|Not Selected|false|&lt;blank&gt;|