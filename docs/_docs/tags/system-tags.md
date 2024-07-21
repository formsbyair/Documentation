---
title: System Tags
category: Tags
order: 11
---

These tags reference system and document information as opposed to form data.

System tag names are enclosed in &lt;&lt;[ and ]&gt;&gt; to differentiate from form tags.

&lt;&lt;[DocumentId]&gt;&gt; can be used client and server side, all other system tags can only be used server side.

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
|&lt;&lt;[DocumentReceivedDateTime]&gt;&gt;|Local DateTime that document was received|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentRequestedUserEmail]&gt;&gt;|Email address of User that requested document|joe@bloggs.com|
|&lt;&lt;[DocumentRequestedDateTime]&gt;&gt;|Local DateTime that document was requested|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentStartedDateTime]&gt;&gt;|Local DateTime that document was started|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentExpiryDateTime]&gt;&gt;|Local DateTime that requested document will expire|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentPurgedDateTime]&gt;&gt;|Local DateTime that document was purged|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentOwnerName]&gt;&gt;|Account name|FormsByAir|
|&lt;&lt;[DocumentUserName]&gt;&gt;|Name of User that submitted document|Joe Bloggs|
|&lt;&lt;[DocumentUserEmail]&gt;&gt;|Email address of User that submitted document|joe@bloggs.com|
|&lt;&lt;[DocumentUserManagerEmail]&gt;&gt;|Email address of Manager for User that submitted document|mary@bloggs.com|
|&lt;&lt;[DocumentStage]&gt;&gt;|Last submitted stage where form is configured for staged submission|Enquiry|
|&lt;&lt;[DocumentReferrer]&gt;&gt;|First Referrer header to access the document|https://anotherwebsite.com|
|&lt;&lt;[DocumentIpAddress]&gt;&gt;|Last IP address to access the document|1.2.3.4|
|&lt;&lt;[DocumentUserAgent]&gt;&gt;|Last Useragent to access the document|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36|
|&lt;&lt;[DocumentRequestedEmail]&gt;&gt;|Email address that document was requested for|joe@bloggs.com|
|&lt;&lt;[DocumentSubmitCode]&gt;&gt;|Current submit code|ABC123|

### Document Workflow Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[DocumentWorkflowStatus]&gt;&gt;|Current document workflow status|Pending|
|&lt;&lt;[DocumentWorkflowUserName]&gt;&gt;|Name of User that document is currently assigned to|Jane Bloggs|
|&lt;&lt;[DocumentWorkflowUserEmail]&gt;&gt;|Email address of User that document is currently assigned to|jane@bloggs.com|
|&lt;&lt;[DocumentWorkflowUserManagerEmail]&gt;&gt;|Email address of Manager for User that document is currently assigned to|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowUserName: *WorkflowStatus*]&gt;&gt;|Name of User that document was last assigned to for a given status|Jane Bloggs|
|&lt;&lt;[DocumentWorkflowUserEmail: *WorkflowStatus*]&gt;&gt;|Email address of User that document was last assigned to for a given status|jane@bloggs.com|
|&lt;&lt;[DocumentWorkflowByUserName: *WorkflowStatus*]&gt;&gt;|Name of User that last changed document to a given status|Joe Bloggs|
|&lt;&lt;[DocumentWorkflowByUserEmail: *WorkflowStatus*]&gt;&gt;|Email address of User that last changed document to a given status|joe@bloggs.com|
|&lt;&lt;[DocumentWorkflowComment: *WorkflowStatus*]&gt;&gt;|Last Comment for a given status|Please review|
|&lt;&lt;[DocumentWorkflowDateTime: *WorkflowStatus*]&gt;&gt;|Last Local DateTime for a given status|1 Nov 2018 11:00.00|

See [Document Workflow Status]({{ site.baseurl }}/documents/workflow-status) for a list of workflow status names

### Document Workflow Tags (Deprecated)

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[DocumentWorkflowAssignmentUserName]&gt;&gt;|Name of User that assigned document|Mary Bloggs|
|&lt;&lt;[DocumentWorkflowAssignmentUserEmail]&gt;&gt;|Email address of User that assigned document|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowAssignmentComment]&gt;&gt;|Comment associated with assignment of document to current user|Please review|
|&lt;&lt;[DocumentWorkflowApprovalUserName]&gt;&gt;|Name of User that approved document|Mary Bloggs|
|&lt;&lt;[DocumentWorkflowApprovalUserEmail]&gt;&gt;|Email address of User that approved document|mary@bloggs.com|
|&lt;&lt;[DocumentWorkflowApprovalDateTime]&gt;&gt;|Local DateTime that document was approved|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentWorkflowDeclineComment]&gt;&gt;|Comment associated with declining a document|Does not meet our criteria|
|&lt;&lt;[DocumentWorkflowDeauthoriseComment]&gt;&gt;|Comment associated with deauthorising a document|Something has changed|
|&lt;&lt;[DocumentWorkflowReturnComment]&gt;&gt;|Comment associated with returning a document|Please correct your information|
|&lt;&lt;[DocumentWorkflowComment]&gt;&gt;|Latest workflow comment for a document|Waiting for feedback|

### Document Delivery Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;[DocumentDeliveryId]&gt;&gt;|Unique Document Delivery Id|3a09db8d-4582-45b3-8c67-40b1fdb95298|
|&lt;&lt;[DocumentDeliveryDateTime]&gt;&gt;|Local DateTime that document delivery was queued|1 Nov 2018 11:00.00|
|&lt;&lt;[DocumentDeliveryFileId]&gt;&gt;|Last queued file delivery id|bfef5a5f-bd0b-464f-a219-b689fdfcbe85|
|&lt;&lt;[DocumentDeliveryReference: *DeliveryChannelName* or *SubscriptionId*]&gt;&gt;|Last successful delivery reference for a given delivery channel or subscription|132345564|
|&lt;&lt;[DocumentDeliveryLink: *DeliveryChannelName* or *SubscriptionId*]&gt;&gt;|Last successful delivery link for a given delivery channel or subscription|https://s.com/r/132345564|
|&lt;&lt;[DocumentDeliveryException: *DeliveryChannelName* or *SubscriptionId*]&gt;&gt;|Last exception (if any) for a given delivery channel or subscription|Email bounce joe@bloggs.com|

### Section/Validation Property Tags

|Tag|Definition|Example|
|---|---|---|
|&lt;&lt;Element.[SectionValidationResult]&gt;&gt;|Current status of validation|Pass, Fail, Check, Ok, Requesting, Captured|
|&lt;&lt;Element.[SectionValidationDateTime]&gt;&gt;|Local DateTime that status changed|1 Nov 2018 11:00.00|
|&lt;&lt;Element.[SectionValidationReference]&gt;&gt;|Unique reference returned from validation service|e6a267fa-ebc7-4d65-b506-8cad4e835aa8|
|&lt;&lt;Element.[SectionValidationMessage]&gt;&gt;|Message returned from validation service|Partial pass, facial match needs review|
|&lt;&lt;Element.[SectionValidationData]&gt;&gt;|Data returned from validation service|{&quot;name&quot;: &quot;test&quot;}|
|&lt;&lt;Element.[DocumentDeliveryId]&gt;&gt;|Associated Document Delivery Id|b664b162-78c3-49da-b4aa-2c69f3cf6f4e|

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
|&lt;&lt;[Filter]&gt;&gt;|Used to filter the response in a Lookup integration for a Typeahead|joe bl|
|&lt;&lt;RequestEmailMessage&gt;&gt;|Third party request message|Hi Joe, please add your details to this form|
