---
title: Properties > Autocomplete
category: Questions
order: 1
---

This property can be used to control the "Autocomplete" behaviour of web browsers whereby contact and payment details in a form can be populated automatically.

Most modern web browsers will try to infer the type of data being requested by parsing the name or associated label for each input. The [HTML autocomplete attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) was introduced to let developers specify a particular data type and in some cases disable Autocomplete, however the implementation across web browsers is inconsistent. FormsByAir supports several common autocomplete data types, and can disable Autocomplete as follows:

* Append "search" to the **name** attribute of the input (this is currently the only working solution for Safari)
* Set the autocomplete attribute for the input to "new-password" for Chrome/Edge and "off" for all others

FormsByAir allows you to set a specific data type or disable Autocomplete for the question types below:

#### Email

|Autocomplete|Result|
|---|---|
|Auto|No autocomplete attribute (default)|
|None|Disable Autocomplete|
|Email|Set autocomplete attribute to **email**|

#### Phone

|Autocomplete|Result|
|---|---|
|Auto|No autocomplete attribute (default)|
|None|Disable Autocomplete|
|Phone|Set autocomplete attribute to **tel**|

#### Text

|Autocomplete|Result|
|---|---|
|Auto|No autocomplete attribute (default)|
|None|Disable Autocomplete|
|Name|Set autocomplete attribute to **name**|
|First Name|Set autocomplete attribute to **given-name**|
|Last Name|Set autocomplete attribute to **family-name**|

#### Card

|Format|Result|
|---|---|
|Name|Set autocomplete attribute to **cc-name**|
|Number|Set autocomplete attribute to **cc-number**|
|Expiry|Set autocomplete attribute to **cc-exp**|
|CVV|Set autocomplete attribute to **cc-csc**|

Autocomplete is disabled for all of these questions when Kiosk Mode is enabled for a device or form.

All other question types do not implement the autocomplete HTML attribute.