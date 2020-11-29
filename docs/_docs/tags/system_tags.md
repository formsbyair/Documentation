---
title: System Tags
category: Tags
order: 1
---

These tags reference system or document information, and can be used in integration tasks and templates.

### Document Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[DocumentId]&gt;&gt;|Unique Document Id|0745807e-5d2e-4cfb-9f80-85351223bd92|
|&lt;&lt;[DocumentFormId]&gt;&gt;|Unique Form Id|9115689f-ce57-492b-9e14-6dc6bb239dbf|
|&lt;&lt;[DocumentFormName]&gt;&gt;|Form name|Application Form|
|&lt;&lt;[DocumentFormShortName]&gt;&gt;|Form short name|application-form|
|&lt;&lt;[DocumentFormVersion]&gt;&gt;|Form version for document|10|
|&lt;&lt;[ParentDocumentId]&gt;&gt;|Unique Document Id for parent of third party request|281daeee-494c-4ef3-b90b-1a05374d22cb|
|&lt;&lt;[DocumentReference]&gt;&gt;|Document reference|ABC123 Joe Bloggs|
|&lt;&lt;[DocumentBatchReference]&gt;&gt;|Batch reference for imported documents|Batch001|
|&lt;&lt;[DocumentStatus]&gt;&gt;|Current document status|Workflow|
|&lt;&lt;[DocumentWorkflowStatus]&gt;&gt;|Current document workflow status|Pending|
|&lt;&lt;[DocumentReceivedDateTime]&gt;&gt;|Local DateTime that document was received|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentRequestedUserEmail]&gt;&gt;|Email address of User that requested document|joe@bloggs.com|
|&lt;&lt;[DocumentRequestedDateTime]&gt;&gt;|Local DateTime that document was requested|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentExpiryDateTime]&gt;&gt;|Local DateTime that requested document will expire|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentOwnerName]&gt;&gt;|Account name|FormsByAir|
|&lt;&lt;[DocumentUserName]&gt;&gt;|Name of User that submitted document|Joe Bloggs|
|&lt;&lt;[DocumentUserEmail]&gt;&gt;|Email address of User that submitted document|joe@bloggs.com|
|&lt;&lt;[DocumentUserManagerEmail]&gt;&gt;|Email address of Manager for User that submitted document|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowUserName]&gt;&gt;|Name of User that document is currently assigned to|Jane Bloggs|
|&lt;&lt;[DocumentWorkflowUserEmail]&gt;&gt;|Email address of User that document is currently assigned to|jane@bloggs.com|
|&lt;&lt;[DocumentWorkflowUserManagerEmail]&gt;&gt;|Email address of Manager for User that document is currently assigned to|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowAssignmentUserName]&gt;&gt;|Name of User that assigned document|Mary Bloggs|
|&lt;&lt;[DocumentWorkflowAssignmentUserEmail]&gt;&gt;|Email address of User that assigned document|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowAssignmentComment]&gt;&gt;|Comment associated with assignment of document to current user|Please review|
|&lt;&lt;[DocumentWorkflowApprovalUserName]&gt;&gt;|Name of User that approved document|Mary Bloggs|
|&lt;&lt;[DocumentWorkflowApprovalUserEmail]&gt;&gt;|Email address of User that approved document|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowApprovalDateTime]&gt;&gt;|Local DateTime that document was approved|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentWorkflowDeclineComment]&gt;&gt;|Comment associated with declining a document|Does not meet our criteria|
|&lt;&lt;[DocumentWorkflowReturnComment]&gt;&gt;|Comment associated with returning a document|Please correct your information|
|&lt;&lt;[DocumentStage]&gt;&gt;|Last submitted stage where form is configured for staged submission|Enquiry|

### Document Delivery Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[DocumentDeliveryId]&gt;&gt;|Unique Document Delivery Id|3a09db8d-4582-45b3-8c67-40b1fdb95298|
|&lt;&lt;[DocumentDeliveryDateTime]&gt;&gt;|Local DateTime that document delivery was queued|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentDeliveryReference: *DeliveryChannelName* or *SubscriptionId*]&gt;&gt;|Last successful delivery reference for a given delivery channel or subscription|132345564|
|&lt;&lt;[DocumentDeliveryLink: *DeliveryChannelName* or *SubscriptionId*]&gt;&gt;|Last successful delivery link for a given delivery channel or subscription|https://s.com/r/132345564|

### Aggregate Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[BatchId]&gt;&gt;|Unique Batch Id|0745807e-5d2e-4cfb-9f80-85351223bd92|
|&lt;&lt;[BatchRunDateTime]&gt;&gt;|Local DateTime that batch started running|1 Nov 2018 11:00.00|
|&lt;&lt;[DetailLineCount]&gt;&gt;|Number of detail lines in batch|10|
|&lt;&lt;[TotalLineCount]&gt;&gt;|Total number of lines in batch including header, detail and footer|12|
|&lt;&lt;[Filename]&gt;&gt;|Batch file name|batch.txt|

### Miscellaneous Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[BaseURL]&gt;&gt;|Base URL for account|https://fba.formsbyair.com|
|&lt;&lt;[FileNumber]&gt;&gt;|Sequential number for a file attachment|1|
|&lt;&lt;RequestEmailMessage&gt;&gt;|Third party request message|Hi Joe, please add your details to this form|
