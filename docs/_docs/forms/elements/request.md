---
title: Elements > Request
category: Forms
order: 2
---

A request element can be used to enable a third party to complete *part* of a form where the other party is unavailable or in a different location to the main form filler. This is particularly useful for forms with multiple applicants including company directors and trustees where details and identity verification are required for each person.

## Add a request to a form

Request elements can be added to any part of a form including repeaters and conditional paths. Elements *within* the request will be available for completion by the third party.

![]({{ site.baseurl }}/images/request.png)

## Send a message on request generation

FormsByAir generates a unique link for each request, which the main form filler must communicate to the third party themselves by default. FormsByAir can send an automated message by adding a form integration to Send an email **On Third Party Request**

We recommend the following settings:

|Setting|Description|Example|
|---|---|---|
|Recipient Email Address (BCC)|Tag for email address of the third party (within the Request)|&lt;&lt;ApplicantEmailAddress&gt;&gt;
|Copy Email Address (CC)|Tag for email address of the main form filler (outside of the Request)|&lt;&lt;ContactEmailAddress&gt;&gt;
|Subject|Include tag to reference main form filler's name (outside of the Request)|Request to complete form from &lt;&lt;ContactName&gt;&gt;
|Reply Email Address|Tag for email address of the main form filler, so the other party can easily *reply* if they need more information|&lt;&lt;ContactEmailAddress&gt;&gt;

The email template should include information about the form and a link to open the request, the URL for which is:

&lt;&lt;[BaseUrl]&gt;&gt;/forms/requests/&lt;&lt;[DocumentId]&gt;&gt;

The template can also include a custom message from the main form filler, which they enter when they generate a request. 

&lt;&lt;RequestEmailMessage&gt;&gt;

You must include a hidden formula question within the Request element with tag **RequestEmailMessage** to store this message.

## Send a message on request submission

By default, a third party will need to notify the main form filler themselves when they've submitted their request. FormsByAir can send an automated message by adding a form integration to Send an email **On Third Party Submit**

We recommend the following settings:

|Setting|Description|Example|
|---|---|---|
|Recipient Email Address (BCC)|Tag for email address of the main form filler (outside of the Request)|&lt;&lt;ContactEmailAddress&gt;&gt;
|Copy Email Address (CC)|Tag for email address of the third party (within the Request)|&lt;&lt;ApplicantEmailAddress&gt;&gt;
|Subject|Include tag to reference third party's name (within the Request)|Request has been completed by &lt;&lt;ApplicantName&gt;&gt;

The email template should include a link to open the main document, the URL for which is:

&lt;&lt;[BaseUrl]&gt;&gt;/forms/requests/&lt;&lt;[DocumentId]&gt;&gt;

The syntax for this URL is the same as the request email above, however &lt;&lt;[DocumentId]&gt;&gt; will resolve to the main document in this case.





