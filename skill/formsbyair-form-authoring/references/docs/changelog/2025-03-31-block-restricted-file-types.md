---
title: Block restricted file types
type: platform
---

When attaching files to a form, we automatically apply a filter to the file selection dialog so that only acceptable file types are listed e.g. PDF or JPG

Users can however change this to show *all files*, and could attach a file with a restricted type e.g. EXE or BAT

We already scan all file attachments for viruses and malware, but to further protect against malicious or accidental attachment of restricted files, we now block any file that doesn't match our list of [acceptable file types]({{ site.baseurl }}/questions/types/attachment/) - both in forms and our API.