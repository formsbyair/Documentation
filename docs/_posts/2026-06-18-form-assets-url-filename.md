---
title: Form assets url filename
type: platform
---

We've resolved a minor issue with the URL path for form asset files.

The previous path for an asset file was /forms/{formId}/assets?filename={filename}

This works fine for images and other files that display inline, but for PDF files, which are often downloaded, it meant the default filename was "assets".

We've updated the path to /forms/{formId}/assets/{filename} so that web browsers use *filename* for download.

The old format is still supported so there's no impact on existing forms.