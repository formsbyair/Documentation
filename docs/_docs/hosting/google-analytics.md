---
title: Google Analytics
category: Hosting
order: 2
---

We emit the following events for Google Analytics (GA4) and Google Tag Manager.

All events include the GA4 parameters **form_name** and **form_id**. These populate the built-in *Form name* and *Form id* dimensions in GA4, so no custom dimension setup is required. The legacy Universal Analytics style parameters (**category** and **label**) are still included for backwards compatibility.

We also populate **userId** with our unique DocumentId so you can track user activity across sessions.

|Event|form_name (GA4)|form_id (GA4)|category (legacy)|label (legacy)|
|---|---|---|---|---|
|start|{Tracking Label} or {Form Title}|{Form Reference}|form|{Tracking Label} or {Form Title}|
|open|{Tracking Label} or {Form Title}|{Form Reference}|form|{Tracking Label} or {Form Title}|
|section|{Tracking Label} or {Form Title}|{Form Reference}|form|{Tracking Label} or {Form Title} – {Section Title}|
|save|{Tracking Label} or {Form Title}|{Form Reference}|form|{Tracking Label} or {Form Title} – {Section Title}|
|submit|{Tracking Label} or {Form Title}|{Form Reference}|form|{Tracking Label} or {Form Title}|
