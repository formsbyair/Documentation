---
title: Block third party request on prefill
type: fix
---

We've applied a change to block the generation of third party requests during prefill, as this is not required, and would result in documents with an invalid status.