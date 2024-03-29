---
title: Validation Reset & Return
type: platform
---

We've added an additional action to help manage incomplete validation requests as follows:

|Action|Description|Use When|
|---|---|---|
|**Reset & Return**|Delete outstanding request, return the document|Form user can't complete validation or failed validation and should retry or choose a different path through the form|

The existing actions remain as follows:

|Action|Description|Use When|
|---|---|---|
|**Resend Request**|Delete outstanding request, create & send new request|Form user can complete validation, but lost the original request|
|**Cancel**|Delete outstanding request, continue with form processing|You no longer require validation, no form changes required|