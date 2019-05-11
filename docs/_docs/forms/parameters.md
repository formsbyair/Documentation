---
title: Parameters
category: Forms
order: 1
---

Query string parameters can be used to pass data to a form, and modify behaviour around submission.

## Form Tag Parameters

Values can be passed to any text-based question with a tag including hidden formulas using standard query string syntax:

https://formsbyair.com/forms/my-form?tag=value&anotherTag=anotherValue

There is no limit to the number of values that you can pass. Tag names are not case sensitive, but must not contain spaces. 

Questions within a repeater will only be set if the **At Least One** option is enabled, and only for the **first** item in the repeater.

This feature is useful for **defaulting** values since query string parameters can be easily modified. To populate information that can't be modified, or for more complex prefill requirements, consider generating a request using **Prefill** in the portal or via our API.

## System Parameters

System parameters can be passed to a form using standard query string syntax as follows:

|Name|Value|Purpose|
|---|---|---|
|ReturnOnSubmit|1|Show the form's confirmation message in a modal popup on submit. When the user dismisses the message, redirect immediately to either the Account's website address or the ReturnUrl.
|SubmitOnLoad|1|Automatically submit the form as soon as it's loaded, this should be used in conjunction with form tag parameters to populate data.|
|ReturnUrl|formsbyair.com|Redirect to this URL when the user clicks **Close** after submit, this overrides the Account's website address|
|SubmitUrl|formsbyair.com|Redirect to this URL immediately after submit, no confirmation message will be shown.|
|Note|This is urgent|Add or override the instructional note that appears at the start of the form|

