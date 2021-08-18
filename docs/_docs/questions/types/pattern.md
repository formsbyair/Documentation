---
title: Types > Pattern
category: Questions
order: 8
---

Free text or masked input validated against a regular expression.

Questions will display the mask format in the right margin for reference, which is replaced with a tick when the validation expression is satisfied.

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