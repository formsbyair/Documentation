---
title: Email editor encoding expression operators
type: fix
---

Fixed an issue where the *and* operator (&&) within expressions was being HTML-encoded by the email template editor, causing expression evaluation to fail.