---
title: Source Referrer
type: platform
---

We'll now record the value of the **utm_source** query string parameter if present in a form link as the &lt;&lt;[DocumentReferrer]&gt;&gt;, otherwise we'll fallback to document.referrer if available.

This enables you to track an explicit referral where required.