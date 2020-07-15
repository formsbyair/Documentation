---
title: Expressions in Word templates
type: fix
---

When typing expressions in to Word templates, single quote marks (&apos;) are rendered as "curly" opening and closing quote marks (&lsquo;&rsquo;), for example:

&lt;&lt;[Expression:&lsquo;Type&rsquo; == &lsquo;Custom&rsquo; ? &lsquo;Custom text&rsquo; : &lsquo;Standard text&rsquo;]&gt;&gt;

This causes errors with expression evaluation, and templates had to be updated, usually by copying unformatted text from a text editor like Notepad.

FormsByAir will now automatically convert curly quotes to regular quotes, so expressions can be entered directly in Word without issue.

&lt;&lt;[Expression:&apos;Type&apos; == &apos;Custom&apos; ? &apos;Custom text&apos; : &apos;Standard text&apos;]&gt;&gt;