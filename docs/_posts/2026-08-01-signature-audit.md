---
title: Signature audit
type: platform
---

We've improved the audit trail for **Signature** questions.

Previously, we displayed IP address and user agent for each signature during form fill, and output the date/time, IP address and user agent for the whole document in the properties of a generated PDF.

We've extended the audit message shown under each signature to include date/time, and we now store it per signature in the document e.g.

*Captured 1 Aug 2026 9:15:32 am +12:00 from 203.0.113.7 using Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X)*

This means the audit message for each signature remains available after submission:

* It appears under the signature when viewing a document in workflow
* It's output under the signature image in auto-generated Word/PDF output
* It can be output in any template using a property tag e.g. &lt;&lt;Signature.[Audit]&gt;&gt;

Existing forms will begin storing per-signature audit information the next time they're saved.

If you use a custom template for auto-generated output, the audit line uses a new **Form Audit** style, which you can override by adding a style with that name to your template.
