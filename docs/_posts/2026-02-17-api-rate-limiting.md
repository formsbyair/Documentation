---
title: API rate limiting
type: platform
---

We are planning to introduce rate limiting to our API from **1 March 2026** to protect against unintended overuse.

This means there will be limits on the number of API requests that can be made within a certain time frame, but these limits will be sufficiently high to allow for *normal* usage.

Rate limits will apply per API Key, and default to **100 requests per minute.** If you exceed that limit we'll return a "429 Too Many Requests" response.

We'll be monitoring this change after it goes live and may adjust the limits as needed.

We will also be removing support for legacy OWIN API Keys at the same time, and will reach out directly if you are still using an old key that needs to be replaced.