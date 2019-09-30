---
title: Elements > Request
category: Forms
order: 2
---

A request element can be used to manage the process of a third party completing *part* of a form where the other party is unavailable or in a different location to the main form filler. This is particularly useful for forms with multiple applicants including company directors and trustees where details and identity verification are required for each person.

## Add a request to a form

Request elements can be added to any part of a form including repeaters and conditional paths. Elements *within* the request will be available for completion by the third party.

## Send a message on request generation

By default, FormsByAir will generate a unique link for a request, which the main form filler must communicate to the third party themselves.

FormsByAir can send an automated message by adding a form integration to Send an email **On Third Party Request**

We recommend the following settings:

|Setting|Definition|Example|
|---|---|---|
|Recipient Email Address (BCC)|Tag for email address question within the Request element|&lt;&lt;ApplicantEmailAddress&gt;&gt;
|Copy Email Address (CC)|Tag for email address question of the main form filler (outside of the request)|&lt;&lt;ContactEmailAddress&gt;&gt;
|Subject||Request to complete Application form from &lt;&lt;ContactName&gt;&gt;
|Reply Email Address|Tag for email address question of the main form filler, so the other party can easily *reply* if they need more information|&lt;&lt;ContactEmailAddress&gt;&gt;

The email template should include information about the form and a link to open the request, the URL for which is:

&lt;&lt;[BaseUrl]&gt;&gt;/forms/requests/&lt;&lt;[DocumentId]&gt;&gt;

The template can also include a custom message from the form filler, which they enter when they generate the request. 

&lt;&lt;RequestEmailMessage&gt;&gt;

Note - You must include a hidden formula question within the Request element with tag **RequestEmailMessage** to store the message, and make it available for the request message.

## Send a message on request submission

By default, a third party would need to notify the main form filler when they've submitted their request.

FormsByAir can send an automated message by adding a form integration to Send an email **On Third Party Submit**

We recommend the following settings:

|Setting|Definition|Example|
|---|---|---|
|Recipient Email Address (BCC)|Tag for email address of the main form filler (outside of the request)|&lt;&lt;ContactEmailAddress&gt;&gt;
|Copy Email Address (CC)|Tag for email address within the request element|&lt;&lt;ApplicantEmailAddress&gt;&gt;
|Subject||Request has been completed by &lt;&lt;ApplicantName&gt;&gt;

The email template should include a link to open the main form, the URL for which is:

&lt;&lt;[BaseUrl]&gt;&gt;/forms/requests/&lt;&lt;[DocumentId]&gt;&gt;

Note - the syntax for this URL is the same as the request email above, however &lt;&lt;[DocumentId]&gt;&gt; will resolve to the main document in this case.





