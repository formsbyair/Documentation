---
title: .NET Core Upgrade
type: platform
---

We've been working on a code framework upgrade for our application for some time, which we're now ready to apply to production.

This upgrade will take us from .NET Framework 4.8.1 to .NET Core 8, which is the latest LTS version of .NET, and will keep us current with all security and performance improvements, and potential new features.

We're aiming to apply the upgrade on **Saturday 1st March 3pm NZT.**

**There will be no downtime during the upgrade.**

There are no functional changes to forms, our portal, or our API **except** for the minor items listed below. The only noticeable difference should be a performance improvement!

* The API endpoints below return a string instead of JSON, our new application will correctly return a Content-Type header of text/plain instead of application/json for these:

DELETE /api/v1/documents/deliveries/{id}  
PUT /api/v1/documents/{id}/return  
PUT /api/v1/documents/{id}/restore

* All API endpoints that return JSON will now **exclude** null properties by default, in line with modern REST API standards

* Existing API keys will be deprecated, and you will need to generate new API Keys soon after the upgrade. That's because .NET Core doesn't natively support the original OWIN-based bearer tokens from .NET Framework. We have migrated to encrypted JWT bearer tokens with .NET Core. New API Keys will work exactly the same way with our API, and have the same 3 year expiry. We'll continue to support existing API Keys until we've confirmed that the last API user has migrated to a new key.