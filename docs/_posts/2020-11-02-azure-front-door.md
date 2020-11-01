---
title: Azure Front Door
type: platform
---

In order to scale the performance of our platform and keep pace with security threats, we are moving all public FormsByAir endpoints from Azure Application Gateways to Azure Front Door. Front Door provides a CDN for static content at 130 POPs around the world and an advanced WAF (Web Application Firewall) to help mitigate attacks including DDoS. In addition, we are taking this opportunity to increase our minimum TLS version from 1.1 to 1.2.

All forms hosted on *.formsbyair.com are now running with Front Door and TLS 1.2.

All forms hosted on a custom domain are being migrated in consultation with each client/partner.

formsbyair.com (which includes our portal and API) will be migrated once all partner endpoints have been migrated.