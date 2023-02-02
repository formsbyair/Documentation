---
title: Google Analytics
category: Hosting
order: 2
---

We emit the following events for Google Analytics and Google Tag Manager.

We also populate user_id/userId with our unique DocumentId so you can track user activity across sessions.

|Event|Category|Action|Label|
|---|---|---|---|
|eventTracking|form|start|{Tracking Label} or {Form Title}|
|eventTracking|form|open|{Tracking Label} or {Form Title – Section Title}|
|eventTracking|form|section|{Tracking Label} or {Form Title – Section Title}|
|eventTracking|form|save|{Tracking Label} or {Form Title – Section Title}|
|eventTracking|form|submit|{Tracking Label} or {Form Title}|