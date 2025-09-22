---
title: System tags date format
type: platform
---

We've updated the following file-based integrations to use ISO 8601 format (YYYY-MM-DD) for all date-based **system** tags.

CSV  
Text From Template  
JSON From Map  
XML From Map  

For example &lt;&lt;[DocumentReceivedDateTime]&gt;&gt; will now return "2025-09-22" instead of "22-Sep-2025".

This brings system tags in to line with form data tags, which already use this format for the file types above.