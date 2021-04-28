---
title: Default repeater from repeater
type: platform
---

You can now set the Default Value for a Repeater to use the contents of another repeater with syntax as follows:

&lt;&lt;[ForEach:RepeaterTag{Filter}]&gt;&gt;

This is useful where you need to edit and extend the contents of a previous repeater, perhaps in a subsequent form stage. This is different to Linked Repeaters, which don't allow you to independently add or remove items.