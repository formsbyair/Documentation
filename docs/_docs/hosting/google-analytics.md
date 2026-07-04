---
title: Google Analytics
category: Hosting
order: 2
---

We emit the following events for Google Analytics (GA4) and Google Tag Manager.

All events include the GA4 parameters **form_name**, set to {Tracking Label} or {Form Title}, and **form_id**, set to our unique form reference. These populate the built-in *Form name* and *Form id* dimensions in GA4, so no custom dimension setup is required. The legacy Universal Analytics style parameters (category and label) are still included for backwards compatibility.

We also populate **userId** with our unique DocumentId so you can track user activity across sessions.

|Event|Category|Label|
|---|---|---|
|start|form|{Tracking Label} or {Form Title}|
|open|form|{Tracking Label} or {Form Title}|
|section|form|{Tracking Label} or {Form Title} – {Section Title}|
|save|form|{Tracking Label} or {Form Title} – {Section Title}|
|submit|form|{Tracking Label} or {Form Title}|
