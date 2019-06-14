---
title: FormsByAir
category: Integrations
order: 2
---

Send form data to another FormsByAir form using this integration.

## Settings

#### Form Id

The unique Id of the target form. This can be a public form from any FormsByAir account, or a private form in your account.

You can find the Id for a form by opening it in the designer, then copy the part after "https://formsbyair.com/manage#/forms/" in your web browser's address bar e.g. ce93650f-214b-485a-a96e-a60ee3920866

#### Submission Type

|Submit|Target document is submitted straight away, mapping must include data for all mandatory questions.|
|Request|Target document is saved as a request, which can then be opened, updated and submitted.|

#### Map

A JSON file mapping data in the source form to the target form using tags.