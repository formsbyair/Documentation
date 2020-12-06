---
title: Nested Systems Tags
type: platform
---

Added the ability to nest system tags within the Condition Tag using the number of &lt;&lt;&gt;&gt;'s to indicate depth, for example:

&lt;&lt;&lt;[Condition:'&lt;&lt;[ForEach:Contact{'&lt;&lt;ContactAccept&gt;&gt;' != 'Accept'}:&lt;&lt;ContactAccept&gt;&gt;]&gt;&gt;' == '':'Accept']&gt;&gt;&gt;

This only applies to server-side Condition tags with 2 levels of depth for now, we're looking to extend this syntax to all other system tags with additional levels of depth in future.