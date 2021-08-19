---
title: Types > Pattern
category: Questions
order: 8
---

Masked input and/or regular expression validation.

Questions will display the mask format (if provided) in the right margin so that users are aware of the specific input required.

A tick is displayed when the input is valid for the mask and/or validation expression.

A validation error is displayed on Submit or Next for invalid input.

## Properties

#### Input Mask
Use A for letters and 9 for digits, or a &lt;&lt;tag&gt;&gt; referencing a mask. For example...

* 999
* AA-9999

#### Validation Expression
A regular expression or a &lt;&lt;tag&gt;&gt; referencing a regular expression. For example...

* [0-9][0-9][0-9]
* [a-Z][a-Z]-[0-9][0-9][0-9][0-9]

For help with regular expressions see <https://regex101.com>