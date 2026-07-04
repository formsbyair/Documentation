---
title: Google Analytics
category: Hosting
order: 2
---

We emit the following events for Google Analytics (GA4) and Google Tag Manager.

We also populate **userId** with our unique DocumentId so you can track user activity across sessions.

|Event|form_name (GA4)|form_id (GA4)|category (legacy)|label (legacy)|
|---|---|---|---|---|
|start|{Tracking Label} or {Form Title}|{Form Id}|form|{Tracking Label} or {Form Title}|
|open|{Tracking Label} or {Form Title}|{Form Id}|form|{Tracking Label} or {Form Title}|
|section|{Tracking Label} or {Form Title}|{Form Id}|form|{Tracking Label} or {Form Title} – {Section Title}|
|save|{Tracking Label} or {Form Title}|{Form Id}|form|{Tracking Label} or {Form Title} – {Section Title}|
|submit|{Tracking Label} or {Form Title}|{Form Id}|form|{Tracking Label} or {Form Title}|
