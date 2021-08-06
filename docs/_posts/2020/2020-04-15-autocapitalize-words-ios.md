---
title: Autocapitlize Words iOS
type: fix
---

Removed the HTML5 tag autocapitalize="words" when using the **Title Case** Format for Text questions due to inconsistent behaviour on iOS devices, which is yet to be [resolved by Apple](https://forums.developer.apple.com/thread/18634)

Title Case text is now capitalized correctly on all devices using our own script.

autocapitalize="characters" continues to be used with the **Upper Case** Format, which behaves correctly on all devices.