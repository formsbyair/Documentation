---
title: Expressions in Word templates
type: fix
---

When typing expressions in to Word templates, single quote marks (&apos;) are rendered as "curly" opening and closing quotes (&lsquo;&rsquo;), for example:

&lt;&lt;[Expression:&lsquo;Type&rsquo; == &lsquo;Custom&rsquo; ? &lsquo;Custom text&rsquo; : &lsquo;Standard text&rsquo;]&gt;&gt;

This caused errors with expression evaluation, requiring templates to be updated, usually by copying unformatted text from a text editor like Notepad.

FormsByAir will now automatically convert curly quotes to regular quotes during evaluation, so expressions can be entered directly in Word without issue.