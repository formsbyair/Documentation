---
title: Nested Systems Tags
type: platform
---

Added the ability to nest system tags within the Condition Tag using the number of &lt;&lt;&gt;&gt;'s to indicate depth, for example:

&lt;&lt;&lt;[Condition:&apos;&lt;&lt;[ForEach:Contact{&apos;&lt;&lt;ContactAccept&gt;&gt;&apos; != &apos;Accept&apos;}:&lt;&lt;ContactAccept&gt;&gt;]&gt;&gt;&apos; == &apos;&apos;:&apos;Accept&apos;]&gt;&gt;&gt;

This only applies to server-side Condition tags with 2 levels of depth for now, we're looking to extend this syntax to all other system tags with additional levels of depth in future.