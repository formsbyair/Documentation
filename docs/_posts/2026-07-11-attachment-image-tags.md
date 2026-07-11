---
title: Attachment image tags
type: platform
---

We've added support for displaying attached images in template-driven document output.

A template tag for an attachment question normally outputs the attachment filename e.g. &lt;&lt;Photo&gt;&gt;.

You can now include a width to display the attached image at that size instead e.g. &lt;&lt;Photo\|500&gt;&gt; - the same syntax as signature and diagram tags today.

This also works inside &lt;&lt;[ForEach:...]&gt;&gt; table rows, so a repeating list of photos can be output as images.

Supported image types are png, jpg, jpeg, gif and bmp. If the attached file isn't a supported image, or the image can't be rendered, the tag falls back to outputting the filename as usual.
