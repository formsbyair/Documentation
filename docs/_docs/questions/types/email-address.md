---
title: Types > Email Address
category: Questions
order: 4
---

Free text entry of an email address. 

An "email" keyboard with @ symbol will be displayed on focus where available.

#### Validation Errors

The following errors are displayed when the user attempts to submit or move forward.

* No value provided and question is Required
* Value doesn't satisfy regex pattern mailbox@domain

#### Validation Warnings

The following warnings are displayed as an email address is entered.

* MX record for domain not found
* Domain matches a common mis-spelling of a major email service provider

|Email Address|Result|Warning Message|
|---|---|---|
|me@extra.co.nz|Domain not found and matches common typo|extra.co.nz not found, did you mean xtra.co.nz?|
|me@gamil.com|Domain found but matches common typo|Did you mean gmail.com?|
|me@formsxyzbyair.com|Domain not found|formsxyzbyair.com not found, please check|

A "tick" icon will be displayed in the right margin of an email address that satisfies all validation.