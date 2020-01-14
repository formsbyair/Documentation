---
title: Email editor encoding expressions
type: fix
---

Fixed an issue where the *and* operator (&&) within expressions was being HTML-encoded by the email editor, causing expression evaluation to fail.