---
title: Properties > Filename Format
category: Questions
order: 3
---

Custom filename format for an attachment, can include the original filename, static text and other form data.

The default filename format is "{Question text} - {Original filename}" so that attachments can be correlated to attachment question(s) within the form.

The examples below assume the Attachment element has a tag of "Attachment", and a file "BankStmtSep2019.pdf" has been attached.

|Filename Format|Resulting Filename|
|--|--|
||Please attach your bank statement - BankStmtSep2019.pdf|
|&lt;&lt;Firstname&lt;&lt; Statement|Joe Statement.pdf|
|Statement - &lt;&lt;Attachment&gt;&gt;|Statement - BankStmtSep2019.pdf|
|&lt;&lt;Attachment&gt;&gt;|BankStmtSep2019.pdf|