---
title: Report purged documents
type: platform
---

We made a previous change [here]({{ site.baseurl }}/changelog/#/2021/03/02/report-purged-documents) so that purged documents would be included in reports by default, and could be excluded with a conditional expression.

We've since determined that including purged documents is a special case that shouldn't be the default option, and doesn't need to be run on a recurring basis.

As such we've reverted the previous change so the option **Document report, sent daily** will now exclude purged documents.

We've added a new option **Document log (including purged), sent once** that will include purged documents, and only run once unless manually triggered again.