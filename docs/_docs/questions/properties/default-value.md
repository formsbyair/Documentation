---
title: Properties > Default Value
category: Questions
order: 2
---

Defaults are evaluated when a form, or section that hasn't been visited before, is loaded. Defaults can be static values, expressions, or system values.

Defaults never override a non-blank value, for example, where a question has been prefilled.

## System Defaults

A list of system defaults is displayed in the form designer when editing a Default Value for convenience.

|Default|Definition|Example|
|---|---|---|
|=DateTime.Today|The current date as a JavaScript date object (for Date Questions) or ISO 8601 string|2019-06-03|
|=DateTime.Today.AddDays(days)|The current date plus the specified number of *days* as a JavaScript date object (for Date Questions) or ISO 8601 string|2019-09-03|
|=DateTime.Today.AddMonths(months)|The current date plus the specified number of *months* as a JavaScript date object (for Date Questions) or ISO 8601 string|2019-09-03|
|=DateTime.Now|The current date and time as an ISO 8601 string|2019-06-03T10:30:00+12:00|
|=DateTime.Time|The current time as a string|10:30 am|
|=GenerateCode(length)|A random alpha-numeric code of *length* characters|3bb188a0|
|=Manager.Email|The current user's, manager's email address, blank if not logged in or no manager defined|manager@formsbyair.com|
|=Manager.Name|The current user's, manager's name, blank if not logged in or no manager defined|Joe Bloggs|
|=Referrer|The URL of the document that loaded the current document (document.referrer)|https://formsbyair.com|
|=User.Email|The current user's email address, blank if not logged in|user@formsbyair.com|
|=User.Name|The current user's name, blank if not logged in|Joe Bloggs|
|=User.Team|The current user's team, blank if not logged in or no team defined|Customer Service|