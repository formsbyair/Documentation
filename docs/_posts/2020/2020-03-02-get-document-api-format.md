---
title: GET Document API format
type: feature
---

Added new **Data** format option to [GET /api/v1/Documents/{id}](https://formsbyair.com/swagger/ui/index#/Documents/Documents_GetDocument)

This returns a document object with minimal schema information (compared to the **Form** format option)

This may be useful where you need to directly edit document data in an external system without rendering the form.