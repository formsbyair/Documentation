---
title: Private download links
category: Forms
order: 5
---

Private download links can be used to authenticate access to private online resources. We currently support Amazon S3, more services will be added in future.

The following sample URL points to a PDF in a private Amazon S3 bucket. The file is an annual statement for a particular client that only they should be able to access.

Because the bucket is private, the link on it's own does not allow access to the file.

https://formsbyair-testing.s3-ap-southeast-2.amazonaws.com/statement_20200101_123456789.pdf

To allow access, links to private resouces should be prefixed as follows:

**/forms/downloads?url=**https://formsbyair-testing.s3-ap-southeast-2.amazonaws.com/statement_20200101_123456789.pdf

This a relative URL for use within a form, but an absolute url can also be used, for example, in an email.

When accessing the link, FormsByAir will check for a valid "Private Form" authentication ticket. If one does not exist the user will be redirected to the login page for the account.

On login, FormsByAir parses the resulting data from the validation request (from a data table or API) and stores a hash of each link to a file storage service against the authentication ticket.

This allows us to compare a hash of the filename being requested in the URL to hash codes in the ticket. If there's a match, FormsByAir reads the file using credentials for the relevant Connected Service, and returns it to the user.

"Private Form" authentication cookies are session-based and expire after 2 hours.