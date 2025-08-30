---
title: Copy forms with tables
type: platform
---

We've made the following changes to improve the process of copying forms that use tables

* When you copy a form to another account, we'll now check that the tables used by your form exist in the target account, and copy over any that are missing. We'll then update all table links in your form to use the corresponding tables in the target account.

* When you copy a form to update an existing form, the target form will now retain its existing table links. This is especially useful where you have a production and a test version of a form that link to production and test tables, and you don't want these links to change when you copy back and forth.

