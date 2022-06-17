---
title: Types > Email Address
category: Questions
order: 7
---

Free text entry of an email address. 

An "email" keyboard with @ symbol will be displayed on focus where available.

#### Validation Errors

The following error conditions are evaluated when the user attempts to move to the next section, or submit.

* No value provided and question is Required
* Value doesn't satisfy regex pattern mailbox@domain

#### Validation Warnings

The following warning conditions are evaluated as an email address is entered.

* MX record for domain not found
* Domain matches a common misspelling of a major email service provider

|Email Address|Condition|Warning Message|
|---|---|---|
|me@extra.co.nz|Domain not found and matches common misspelling|extra.co.nz not found, did you mean xtra.co.nz?|
|me@gamil.com|Domain found but matches common misspelling|Did you mean gmail.com?|
|me@formsxyzbyair.com|Domain not found|formsxyzbyair.com not found, please check|

A "tick" icon is displayed in the right margin of an email address that satisfies all validation.