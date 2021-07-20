---
title: Charities Services
category: Integrations
order: 2
---

Lookup a New Zealand charity by name

## Data Model

#### Entity

|Name|Type|
|---|---|
|Name|string|
|NZBN|string|
|CharityRegistrationNumber|string|
|OrganisationId|string|
|RegistrationDate|DateTime|
|StatusDescription|string|
|TypeDescription|string|
|AnnualReturnFilingMonth|int?|
|PhysicalAddress|Address|
|PostalAddress|Address|
|CurrentOfficers|List&lt;Officer&gt;|
|PreviousOfficers|List&lt;Officer&gt;|

#### Address

|Name|Type|
|---|---|
|Address1|string|
|Address2|string|
|City|string|
|State|string|
|PostalCode|string|
|Country|string|

#### Officer

|Name|Type|
|---|---|
|Name|string|
|FirstName|string|
|MiddleNames|string|
|LastName|string|
|Address|Address|
|StartDate|DateTime|
|EndDate|DateTime?|
|EntityName|string|
|Role|string|
