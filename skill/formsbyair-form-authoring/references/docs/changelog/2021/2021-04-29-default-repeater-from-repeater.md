---
title: Default repeater from repeater
type: platform
---

You can now set the Default Value for a Repeater to use the contents of another repeater with syntax as follows:

&lt;&lt;[ForEach:RepeaterTag{Filter}]&gt;&gt;

This is useful where you need to edit and extend the contents of a previous repeater, perhaps in a subsequent form stage. Linked Repeaters are similar but don't allow you to independently add or remove items.

You can refer to content in the first repeater with tags like this &lt;&lt;SecondRepeater.TagNameOfElementInFirstRepeater&gt;&gt;

If the first repeater was populated from a data source, you can refer to that data with tags like this &lt;&lt;SecondRepeater.FirstRepeater.PropertyName&gt;&gt;