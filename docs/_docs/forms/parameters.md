---
title: Parameters
category: Forms
order: 1
---

Query string parameters can be used to pass data to a form, and modify behaviour around submission.

## Form Tag Parameters

Values can be passed to any text-based question with a tag including hidden formulas using standard query string syntax:

?tag=value&anotherTag=anotherValue

There is no limit to the number of values that can be passed. Tag names are not case sensitive, but must not contain spaces. 

Questions within a repeater will only be set if the **At Least One** option is enabled, and only for the **first** item in the repeater.

This feature is useful for defaulting values where it's not critical if they're changed, as query string parameters can be easily modified. For more complex prefill options, or where values should not be modifiable, consider prefilling form requests in the portal or via our API.

## System Parameters

|Parameter Name|Value|Result|
|---|---|---|
|ReturnOnSubmit|1|When a form is submitted, show the confirmation message in a modal. When the user dismisses the message, redirectly immediately to either the website address or the return url|
|SubmitOnLoad|1|Submit the form as soon as it has loaded. Should be used in conjunction with form tag parameters|
|ReturnUrl|formsbyair.com|Redirect to this URL when the user clicks "Close" after submit, this overrides the website address for the account|
|SubmitUrl|formsbyair.com|Redirect to this URL immediately after submit, no confirmation message will be shown|
|Note|This is urgent|Add or override the instructional note that appears at the start of the form|

