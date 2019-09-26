---
title: Preserve form data line breaks in emails
type: fix
---

FormsByAir will now convert newline characters to HTML &lt;br&gt; tags when evaluating form &lt;&lt;tags&gt;&gt; in email templates, for example, where you are outputting the contents of a **Comment** question that may contain several paragraphs.