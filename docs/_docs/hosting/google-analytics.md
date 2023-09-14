---
title: Google Analytics
category: Hosting
order: 2
---

We emit the following events for Google Analytics (GA4) and Google Tag Manager.

We also populate **userId** with our unique DocumentId so you can track user activity across sessions.

|Event|Category|Label|
|---|---|---|---|
|start|form|{Tracking Label} or {Form Title}|
|open|form|{Tracking Label} or {Form Title}|
|section|form|{Tracking Label} or {Form Title – Section Title}|
|save|form|{Tracking Label} or {Form Title – Section Title}|
|submit|form|{Tracking Label} or {Form Title}|