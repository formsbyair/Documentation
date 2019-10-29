---
title: Filename format tag
type: feature
---

You can now use the tag of an attachment element in **Filename Format** to refer to the original filename of the attachment.

The examples below assume the Attachment element has a tag of "Attachment", and a file "BankStmtSep2019.pdf"

|Filename Format|Resulting Filename|
|--|--|
||Please attach your bank statement - BankStmtSep2019.pdf|
|Statement - &lt;&lt;Attachment&gt;&gt;|Statement - BankStmtSep2019.pdf|
|&lt;&lt;Attachment&gt;&gt;|BankStmtSep2019.pdf|