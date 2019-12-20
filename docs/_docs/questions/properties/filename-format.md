---
title: Properties > Filename Format
category: Questions
order: 3
---

Custom filename format for delivery of attachments, this can include the original filename, static text and other form data.

The default filename format is "{Question text} - {Original filename}" so that files can be related back to specific question(s) within the form.

The examples below assume an attachment element has a tag of "Attachment", and a file "BankStmtSep2019.pdf" has been attached.

|Filename Format|Resulting Filename|
|--|--|
||Please attach your bank statement - BankStmtSep2019.pdf|
|&lt;&lt;Firstname&gt;&gt; Statement|Joe Statement.pdf|
|Statement - &lt;&lt;Attachment&gt;&gt;|Statement - BankStmtSep2019.pdf|
|&lt;&lt;Attachment&gt;&gt;|BankStmtSep2019.pdf|
|Bank-&lt;&lt;[FileNumber]&gt;&gt;|Bank-1.pdf|