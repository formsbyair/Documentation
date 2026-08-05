---
title: Repeater and prefill fixes
type: platform
---

We've fixed a group of issues reported through form testing, along with a couple of small improvements:

* Repeaters with Format set to Inline or Table and Maximum Rows set to 1 rendered no fields at all, while the hidden row still failed section validation — blocking Next with no visible "Required" marker. The row now renders like any other repeater row.

* Inline and Table repeaters allowed rows to be removed below the Minimum Rows setting; the remove control now respects Minimum Rows, matching the default repeater format.

* Clicking a tracked document link during prefill marked it as read for the form filler. Prefill users can still open the documents, but the read receipt is now only recorded when the form filler clicks the link.

* Credentials are now optional when editing an existing connected service, allowing you to change specific values only, and leave others as they were.

* Form build now validates that a linked repeater's tag name doesn't conflict with the repeater it links to. This conflict previously caused the form to fail when filling.