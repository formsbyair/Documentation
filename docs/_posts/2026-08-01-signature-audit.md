---
title: Signature audit
type: platform
---

We've added an audit trail to **Signature** questions.

When a signature is captured we record the signer's local date and time (including timezone offset), IP address and browser user agent, and display this in small print under the signature in the form e.g.

*Captured 1 Aug 2026 9:15:32 am +12:00 from 203.0.113.7 using Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X)*

This audit information is now also stored with the submitted document, so it remains available after submission:

* It appears under the signature when viewing a document in workflow
* It's output under the signature image in auto-generated Word/PDF output
* It can be output in any template using a property tag e.g. &lt;&lt;Signature.[Audit]&gt;&gt;

Existing forms will begin storing audit information the next time they're saved.

If you use a custom template for auto-generated output, the audit line uses a new **Form Audit** style, which you can override by adding a style with that name to your template.
