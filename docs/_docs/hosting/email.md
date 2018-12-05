---
title: Email
category: Hosting
order: 1
---

By default, emails we send on your behalf are "from" @yourdomain.formsbyair.com

To authorise us to send email from @yourdomain.com, you will need to arrange for CNAME records similar to below to be added to your DNS.

Please contact your domain registrar or IT support partner if you need assistance with this.

|Host|Value|
|---|---|
|emXXXX.yourdomain.com|u1435474.wl225.sendgrid.net|
|s1._domainkey.yourdomain.com|s1.domainkey.u1435474.wl225.sendgrid.net|
|s2._domainkey.yourdomain.com|s2.domainkey.u1435474.wl225.sendgrid.net|