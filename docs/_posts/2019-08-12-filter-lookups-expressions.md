---
title: Filter table data in Lookups with expressions
type: feature
---

Added the ability to dynamically filter table data in a Lookup question using an expression. The expression can refer to multiple table columns and tags, and must evaluate to true or false, for example:

table.PaymentType == &apos;&lt;&lt;PaymentType&gt;&gt;&apos; && table.Location == &apos;&lt;&lt;Location&gt;&gt;&apos;