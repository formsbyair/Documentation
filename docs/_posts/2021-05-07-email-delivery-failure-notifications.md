---
title: Email delivery failure notifications
type: fix
---

By default, FormsByAir will send email delivery failure notifications to:

* The Reply Email Address of the corresponding email integration if specified; or
* The Notification Email Address for the account; or
* All administrators for the account

If the email address we're sending a bounce notification to matches the email address that bounced, FormsByAir will now automatically escalate the recipient(s) to the next level.

We've also updated how email failures are represented in the portal.

An email integration is marked as OK when successfully delivered to our email provider (SendGrid). If we subsequently receive a failure notification, which could be up to 48 hours later, the integration will now show with a CHECK status in the portal. This is in additon to the notification above. The integration will continue to be classified as "complete" in terms of setting the overall status of the document.