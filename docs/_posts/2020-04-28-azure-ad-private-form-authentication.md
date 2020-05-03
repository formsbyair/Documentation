---
title: Azure AD Private Form Authentication
type: feature
---

Added Microsoft Azure Active Directory option for **Private Form Authentication** in Settings &gt; Profile.

This allows users with a Microsoft organizational account in a specific tenant to access private forms without a FormsByAir user account. It does not allow access to the FormsByAir portal.

Azure AD logins are session based.

If the Azure AD account matches a FormsByAir user account, form submissions are tagged to the FormsByAir user. This is relevant where you want to block users from approving their own submissions (using the **Block Same User** workflow option)

If the Azure AD account does *not* match to a FormsByAir user account, form submissions are not tagged to a user.