---
title: Types > Email Address
category: Questions
order: 1
---

Free text entry of an email address. Triggers "Email" keyboard with @ symbol where available.

#### Validation Errors

* Regex syntax check for mailbox@domain

#### Validation Warnings

* DNS lookup of MX record for domain
* Check for common typos of major email service domain names

|Email Address|Result|Warning Message|
|me@extra.co.nz|Domain not found and matches common typo|extra.co.nz not found, did you mean xtra.co.nz?|
|me@gamil.com|Domain found but matches common typo|Did you mean gmail.com?|
|me@formsxyzbyair.com|Domain not found|formsxyzbyair.com not found|