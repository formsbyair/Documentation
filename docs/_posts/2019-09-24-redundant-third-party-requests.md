---
title: Redundant third party requests
type: fix
---

FormsByAir will now automatically delete any open third party requests that have been indirectly removed from the requesting document, for example, a repeater item that contained a request. This will prevent unneccessary completion and submission of requests that can't be merged back in to the requesting document.