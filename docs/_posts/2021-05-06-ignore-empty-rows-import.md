---
title: Ignore empty rows on import
type: fix
---

When importing a CSV or other delimited text file to a form, FormsByAir will now ignore rows where all fields in the row are blank (in addition to the existing check for completely blank rows)

Empty rows are sometimes included when editing and saving a CSV file with Microsoft Excel.