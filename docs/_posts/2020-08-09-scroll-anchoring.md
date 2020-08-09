---
title: Scroll anchoring
type: fix
---

Several web browsers including Chrome, Edge and Firefox have recently enabled scroll anchoring by default, a feature that automatically adjusts scroll position to compensate for dynamically added content.

This was conflicting with our functionality to scroll newly added repeater items in to view, making it appear that an item had not been added.

As such we've disabled scroll anchoring by adding the following style tag to the body element of our forms: overflow-anchor: none;