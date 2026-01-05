---
title: GBG Cloudcheck Result Missing Verification
type: platform
---

GBG Cloudcheck **Live** and **IDscan** verification usually includes validation of identity details with a document issuer in addition to biometric checks.

Sometimes this validation may not happen, for example, where the identity document was issued by a foreign country that GBG doesn't support, or the API for the issuer is temporarily unavailable.

In those cases we receive a biometric result, but no verified identity details.

In the past we treated this as a completed (but **Failed**) verification, with the expectation that a workflow user would arrange for re-verification or edit the form to use manual identity verification.

However, we didn't stop users from just approving anyway, and doing so led to downstream integration issues where identity details are usually required.

As such we've changed it so a verification result where identity details are expected but not received is now treated as an **Error**, blocking approval until resolved.

This doesn't affect verifications that are configured for Biometric checks only.