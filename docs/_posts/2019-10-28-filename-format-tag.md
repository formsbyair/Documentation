---
title: Filename format tag
type: feature
---

You can now use the tag of an attachment element in **Filename Format** to refer to the original filename of the attachment.

The examples below assume the Attachment element has a tag of "Attachment"

|Filename Format|Attachment|Resulting Filename|
|--|--|--|
||XYZ Bank Sep 2019.pdf|Please attach your bank statement - XYZ Bank Sep 2019.pdf|
|Statement - <<Attachment>>|XYZ Bank Sep 2019.pdf|Statement - XYZ Bank Sep 2019.pdf|
|<<Attachment>>|XYZ Bank Sep 2019.pdf|XYZ Bank Sep 2019.pdf|