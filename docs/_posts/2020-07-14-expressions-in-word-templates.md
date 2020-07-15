---
title: Expressions in Word templates
type: fix
---

When typing expressions in to Word templates, single quote marks (') are rendered as formatted opening and closing quote marks (‘’), for example:

&lt;&lt;[Expression:‘Type’ == ‘Custom’ ? ‘Custom text’ : ‘Standard text’]&gt;&gt;

This causes errors with expression evaluation, and the templates had to be updated, usually by copying unformatted text from a text editor like Notepad.

FormsByAir will now automatically convert these formatted quotes to regular quotes, so expressions can be entered directly in Word without issue.

&lt;&lt;[Expression:'Type' == 'Custom' ? 'Custom text' : 'Standard text']&gt;&gt;