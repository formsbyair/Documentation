---
title: Parameters
category: Forms
order: 1
---

Query string parameters can be used to pass data to a form, and modify behaviour around submission.

## Form Tag Parameters

Any text-based question with a tag can receive a value including hidden formulas.

Tag Names are not case sensitive, but must not contain spaces.

```
For example:

https://fba.formsbyair.com/forms/new-patient?FirstName=Joe&LastName=Bloggs
```

## System Parameters

|Parameter Name|Value|Result|
|---|---|---|
|ReturnOnSubmit|1|When a form is submitted, show the confirmation message in a modal. When the user dismisses the message, redirectly immediately to either the website address or the return url|
|SubmitOnLoad|1|Submit the form as soon as it has loaded. Should be used in conjunction with form tag parameters|
|ReturnUrl|formsbyair.com|Redirect to this URL when the user clicks "Close" after submit, this overrides the website address for the account|
|SubmitUrl|formsbyair.com|Redirect to this URL immediately after submit, no confirmation message will be shown|
|Note|This is urgent|Add or override the instructional note that appears at the start of the form|

