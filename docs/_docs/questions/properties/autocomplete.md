---
title: Properties > Autocomplete
category: Questions
order: 1
---

Used to control the "Autocomplete" behaviour of web browsers for populating contact and payment details automatically.

Most modern web browsers will try to infer the type of data being requested in a form by parsing the name or associated label for each input. The [HTML autocomplete attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete) was introduced to let developers specify data types and in some cases disable Autocomplete, however the implementation across web browsers is inconsistent. FormsByAir supports the most common autocomplete data types, and can disable Autocomplete in all browsers as follows:

* Append "search" to the **name** attribute of the input (this is currently the only working solution for Safari)
* Set the autocomplete attribute for the input to "new-password" for Chrome/Edge and "off" for all others

FormsByAir allows you to specify a data type or disable Autocomplete for the following question types:

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

Autocomplete is disabled for the question types above when Kiosk Mode is enabled for a device or form.

Autocomplete is always disabled for Typeahead questions.

All other question types do not implement the autocomplete HTML attribute.