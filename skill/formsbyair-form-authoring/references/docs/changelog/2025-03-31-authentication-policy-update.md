---
title: Authentication Policy update
type: platform
---

**Two Factor Authentication**

Where Two Factor Authentication is enabled, we'll now save successful authentication to a separate cookie with a 30 day expiry. This is more convenient for users logging back in on the same device, as they'll only need to complete 2FA if it's been at least 30 days since they last completed 2FA.

Username/password authentication continues to use a sliding 5 day expiry by default.

**Session Timeout**

If the option *Must log in every session* is enabled then Username/password authentication uses a session-based cookie.

We've enhanced this option to now include a timeout after 60 minutes of inactivity. As such, if a user leaves our portal open in a browser for more than an hour, and then attempts to take some action, they'll be forced to log in again.


For maximum protection we recommend enabling both *Must log in every session* and *Must use Two Factor Authentication* for your account.