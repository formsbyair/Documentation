---
title: Private download links
category: Forms
order: 5
---

Private download links can be used to authenticate access to private online resources. We currently support Amazon S3 only but more storage services will be added in future.

The sample URL below points to a PDF in a private Amazon S3 bucket. The file is an annual statement for a particular client that only they should be able to access.

Because the bucket is private, the URL on it's own cannot be used to download the file.

https://formsbyair-testing.s3-ap-southeast-2.amazonaws.com/statement_20200101_123456789.pdf

To allow access, URLs for private resouces should be prefixed as follows:

**/forms/downloads?url=**https://formsbyair-testing.s3-ap-southeast-2.amazonaws.com/statement_20200101_123456789.pdf

This example is a relative link for use within a form, but an absolute link can also be used e.g. in an email

When accessing the link, FormsByAir will check for a valid "Private Form" authentication ticket. If one does not exist the user will be redirected to the login page for the account.

On login, FormsByAir scans the resulting data from the validation request (from a data table or API) for URLs from supported storage services, and stores a hash of each one against the authentication ticket.

This allows us to compare a hash of the URL being requested to hash codes in the ticket. If there's a match, FormsByAir reads the file from the storage service using credentials in the account, and returns it to the user.

"Private Form" authentication cookies are session-based and expire after 2 hours.