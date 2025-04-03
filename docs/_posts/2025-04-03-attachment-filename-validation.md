---
title: Attachment filename validation
type: platform
---

Our forms have always had validation to check that the filename for an **Attachment** question inside of a repeater is unique within that repeater.

The original intent behind this was to block accidental attachment of the same file for inline or tabular style repeaters.

However the validation also applied to regular content repeaters, where it can be valid to attach the same file, meaning form users would sometimes need to rename a file in order to attach it.

To address this we've changed the validation so it now only applies to repeaters where Format is **Inline** or **Table**