# FormsByAir changelog

Dated release notes, newest first, merged from the documentation site's posts.

## 2026-07-11 — Attachment image tags (platform)

We've added support for displaying attached images in template-driven document output.

A template tag for an attachment question normally outputs the attachment filename e.g. &lt;&lt;Photo&gt;&gt;.

You can now include a width to display the attached image at that size instead e.g. &lt;&lt;Photo\|500&gt;&gt; - the same syntax as signature and diagram tags today.

This also works inside &lt;&lt;[ForEach:...]&gt;&gt; table rows, so a repeating list of photos can be output as images.

Supported image types are png, jpg, jpeg, gif and bmp. If the attached file isn't a supported image, or the image can't be rendered, the tag falls back to outputting the filename as usual.

## 2026-07-02 — Auto-collapse repeaters (platform)

We've made a couple of changes to Auto-collapse repeaters as follows:

* Improved performance for large repeaters by "pausing" collapsed repeater content, similar to inactive sections.

* When opening a saved or prefilled form that contains existing repeater rows, we'll now expand the first row by default - previously all rows were collapsed

## 2026-06-24 — Multiple email recipients (platform)

We've addressed a long-standing quirk/bug for email integrations with multiple recipients.

Historically, an email integration with multiple recipients would result in a separate email being sent for each recipient. If the integration included a CC or BCC list, those people would receive the email multiple times, once for each recipient.

We've changed it to work how most people would expect, where a single email is sent to all recipients.

If a recipient needs to be hidden from others they should be added to the BCC list.

## 2026-06-18 — Form assets url filename (platform)

We've resolved a minor issue with the URL path for form asset files.

The previous path for an asset file was /forms/{formId}/assets?filename={filename}

This works fine for images and other files that display inline, but for PDF files, which are often downloaded, it meant the default filename was "assets".

We've updated the path to /forms/{formId}/assets/{filename} so that web browsers use *filename* for download.

The old format is still supported so there's no impact on existing forms.

## 2026-06-16 — API Key Scope (platform)

We've added a new **Scope** option when generating API Keys.

You can now optionally restrict the scope of an API key to POST /api/v1/Documents/request only, which may be useful where a third-party needs to generate requests for your forms, but should not have any other access.

## 2026-05-18 — Delivery validation (platform)

We've added a new validation type **Delivery** for validations that need to run as the last step before a form is delivered.

For forms that *don't* use Workflow this type of validation is no differerent to **Post-Submit**

If Workflow is enabled, validation is triggered when a form is *Approved* or *Bypassed*

We added this validation type to support our Docusign integration, where signing a document must happen *after* any review or change in Workflow, but it may be useful for other integrations in future.

## 2026-05-09 — Minor bug fixes and updates (platform)

We've applied the following minor bug fixes and updates:

* Fixed the Preview option for forms with Access Mode set to *Request-Only*
* Fixed scroll issue when adding a new item to *Auto Collapse* repeaters
* Fixed issue where Document Reference was not updated when merging a completed third party request with its parent document
* Added validation when saving a form to check if the Short Name is already used by another form
* Added validation to block Workflow Bypass if any validation element has a status of *Cancelled* or *Error*

## 2026-03-30 — IRD number validation upper limit (platform)

We've updated our IRD number validation to support the new upper limit of 200,000,000 as per <https://www.ird.govt.nz/updates/news-folder/2026/increase-to-ird-number-validation-upper-limit>

## 2026-03-22 — .NET 10.0 / Angular 20 upgrade (platform)

In order to keep within the respective support windows, we have upgraded our code base from .NET version 9.0 to 10.0, and Angular 19 to 20.

This was a minor upgrade requiring minimal code change, and offers additional performance and stability improvements.

## 2026-03-01 — API rate limiting (platform)

As planned, we have now updated our production API to include rate limiting, and removed support for legacy OWIN API Keys.

## 2026-02-23 — Form Status change protection (platform)

We've updated our portal to prevent accidental status changes to Published forms, which could affect access to live forms. These forms must now be *Disabled* first before any other status changes can be made.

We've also added stronger confirmation prompts when Disabling or Deleting a form.

## 2026-02-20 — Webhook system tags date format (platform)

We've updated Webhook integrations to use ISO 8601 format (YYYY-MM-DD) for all date-based **system** tags to be consistent with form data tags, which already use this format for Webhook integrations.

## 2026-02-17 — API rate limiting (platform)

We are planning to introduce rate limiting to our API from **1 March 2026** to protect against unintended overuse.

This means there will be limits on the number of API requests that can be made within a certain time frame, but these limits will be sufficiently high to allow for *normal* usage.

Rate limits will apply per API Key, and default to **100 requests per minute.** If you exceed that limit we'll return a "429 Too Many Requests" response.

We'll be monitoring this change after it goes live and may adjust the limits as needed.

We will also be removing support for legacy OWIN API Keys at the same time, and will reach out directly if you are still using an old key that needs to be replaced.

## 2026-02-07 — Stack Internal migration (platform)

We have decommissioned our Stack Internal portal (previously Stack Overflow for Teams) and migrated the content [here]({{ site.baseurl }}/kb/) so it is searchable and accessible to all users.

Please use **Get Help** in our portal or email support@formsbyair.com for all technical support questions.

## 2026-02-04 — Docusign (platform)

We've added a new integration with Docusign to support forms that require a more formal signing process.

When enabled, FormsByAir will generate a PDF of a submitted form and automatically create a Docusign envelope, including recipients and signature tags. Docusign then manage the signing workflow and return the fully signed PDF to us once all parties have completed signing, triggering delivery of the form.

This integration complements our existing "in form" electronic signature capture feature, which is sufficient for most forms. Docusign may be appropriate where a form is a deed or contract, and legal or other requirements call for a traditional signing workflow.

This integration requires FormsByAir clients to have their own Docusign account, transactions are billed directly by Docusign.

## 2026-01-29 — Email form attachments only (platform)

We've added a new option for email integrations to include only the attachments to a form with the email, no file integration required.

## 2026-01-29 — Rework Saved document (platform)

We've modified permissions around the **Rework** option in our portal for Delivered and Saved documents.

Reworking a **Delivered** document is rare, and is still only available to users in the Administrator or Controller roles.

Reworking a **Saved** document is more common, for example, where a form was Returned in error, or the form filler no longer needs to update it, and you want to move the form back in to Workflow without triggering any integrations. This option is now available to users in the **Supervisor** role in addition to Administrators and Controllers.

## 2026-01-28 — Cancel Requesting validation (platform)

We've added a new **Cancel** option for validation elements in **Requesting** status, typically in relation to ID verification.

This may be useful where verification has since been completed outside of the form, and the form doesn't need to go back to the form filler with **Reset &amp; Return**

Once cancelled, the form will move to Workflow where it can be edited, for example, to select manual ID verification and attach the relevant documents.

## 2026-01-12 — FSPR (platform)

We've added a new integration with the NZ Financial Service Providers Register (FSPR) to lookup registered individuals and entities by name and return their details.

## 2026-01-07 — Copy Form Integrations (platform)

We've updated our portal so you can now copy individual form integrations to another form in the same account, or a different account if you have access to multiple accounts.

## 2026-01-05 — GBG Cloudcheck Result Missing Verification (platform)

GBG Cloudcheck **Live** and **IDscan** verification usually includes validation of identity details with a document issuer in addition to biometric checks.

Sometimes this validation may not happen, for example, where the identity document was issued by a foreign country that GBG doesn't support, or the API for the issuer is temporarily unavailable.

In those cases we receive a biometric result, but no verified identity details.

In the past we treated this as a completed (but **Failed**) verification, with the expectation that a workflow user would arrange for re-verification or edit the form to use manual identity verification.

However, we didn't stop users from just approving the form anyway, and doing so led to downstream integration issues where identity details are usually required.

As such we've changed it so a verification result where identity details are expected but not received is now treated as an **Error**, blocking approval until resolved.

This doesn't affect verifications that are configured for Biometric checks only.

## 2025-12-24 — 2 million submissions (platform)

We've hit 2 million total production form submissions through our platform!!

## 2025-12-15 — Fallback tag function (platform)

We've added a new tag function **Fallback** to return the first non empty value from a list of tags and optional literal value.

This may be useful if you need to provide a default value where a tag is empty.

See [Fallback]({{ site.baseurl }}/tags/functions/fallback/)

## 2025-12-14 — Validate email address on prefill (platform)

We now validate email addresses entered anywhere in a form on prefill, as these are often used with **On Request** email integrations, which will fail if the email address is invalid.

**Prefill-only** sections will continue to be validated in their entirety on prefill.

## 2025-12-09 — Country Risk Rating update (platform)

We've updated our shared **Country** data table to reflect the latest Basel AML Index data for 2025.

Check the following links for more information:

<https://docs.formsbyair.com/changelog/#/2025/08/27/country-risk-rating>
<https://index.baselgovernance.org/news/basel-aml-index-2025-reveals-uneven-progress-global-fight-against-financial-crime>

## 2025-11-28 — Autocomplete (platform)

We've added additional **Autocomplete** options for Address and Date Of Birth to improve accuracy for web browser autofill.

## 2025-10-29 — Skip connected service credentials (platform)

We've added a new option to **Skip** entering credentials for a connected service when adding or editing an integration.

This may be useful for initial setup of a new form or when copying a form between accounts where the credentials aren't available yet.

The connected service will still be listed under Administration > Connected Services, but won't show a CONNECTED status until credentials have been entered.

## 2025-10-25 — Angular 19 upgrade complete (platform)

Our forms and portal have now been upgraded from Angular 18 to 19, all systems are running normally.

## 2025-10-19 — Angular 19 upgrade timeline (platform)

We have scheduled the upgrade of our forms and portal from Angular 18 to 19 for **Saturday 25th October 3pm NZT**

There is no downtime associated with this change, and we'll be monitoring our logs closely after the upgrade for any unforeseen problems.

## 2025-10-05 — Angular 19 upgrade (platform)

We are planning to upgrade our forms and portal from Angular 18 to 19 in the coming weeks to stay within Google's support window.

This is a moderate upgrade which will require some code changes to our platform, but there are no anticipated breaking changes for any forms.

We will provide a separate test environment for partners to test their forms against the new version before we switch our production environment, and will advise on a timeline for the upgrade once testing is complete.

## 2025-10-04 — .NET 9.0 upgrade (platform)

We've upgraded our codebase from .NET version 8.0 to 9.0.

This was a minor upgrade requiring no code changes, but offers additional performance and stability improvements.

## 2025-09-22 — System tags date format (platform)

We've updated the following file integrations to use ISO 8601 format (YYYY-MM-DD) for all date-based **system** tags.

CSV  
Text From Template  
JSON From Map  
XML From Map  

For example &lt;&lt;[DocumentReceivedDateTime]&gt;&gt; will now return "2025-09-22" instead of "22-Sep-2025".

This brings system tags in to line with form data tags, which already use this format for the integrations above.

## 2025-09-16 — PIR/RWT income threshold changes (compliance)

The income thresholds used to determine PIR (Prescribed Investor Rate) and RWT (Resident Withholding Tax) have changed, see links below...

<https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir800---ir899/ir861/ir861.pdf>

<https://www.ird.govt.nz/income-tax/withholding-taxes/resident-withholding-tax-rwt/using-the-right-rwt-tax-rate>

We've updated our PIR and RWT helpers in our Investment form templates to accommodate these changes.

## 2025-09-01 — Source Referrer (platform)

We'll now record the value of the **utm_source** query string parameter if present in a form link as the &lt;&lt;[DocumentReferrer]&gt;&gt;, otherwise we'll fallback to document.referrer if available.

This will enable tracking of an explicit referral source where required.

## 2025-08-29 — Comment (platform)

We've added a **Comment** option to the Document Information page in our portal, so you can now record a comment for any document at any status.

## 2025-08-29 — Copy forms with tables (platform)

We've made the following changes to improve the process of copying forms that use tables

* When you copy a form to another account, we'll now check that the tables used by your form exist in the target account, and copy over any that are missing. We'll then update all table links in your form to use the corresponding tables in the target account.

* When you copy a form to update an existing form, the target form will now retain its existing table links. This is especially useful where you have a production and a test version of a form that link to production and test tables, and you don't want these links to change when you copy back and forth.

## 2025-08-27 — Country Risk Rating (platform)

In order to support AML/CFT requirements for risk rating, we've added a new **Risk** property to our shared **Country** data table.

This property is a number from 0 - 10 where 10 is high risk, and is based on the Basel AML Index published annually here <https://index.baselgovernance.org/>

Any form that uses our Country data table for address can now use this property to help risk-rate new clients, for example:

&lt;&lt;Country.Risk&gt;&gt; &gt; 5 ? 'High Risk Country' : 'Low Risk Country'

## 2025-08-08 — Validation Hide (platform)

Similar to the "Lock" option we added recently, we've added a new Format option **Hide** to Validation elements.

This option won't trigger any validation, instead it allows a Validation element to act as a container of other elements that can be hidden when a button in the form is clicked.

This may be useful where you have an element or elements that capture sensitive information that should be hidden from other form users while a form is being filled out. These elements will still appear in Workflow and all output as normal.

## 2025-07-29 — Collapsible sections in Workflow (platform)

Form sections in Workflow are now collapsible, which may be useful where you need to focus on a specific section for review.

All form sections will open expanded by default, but can be closed/opened by clicking the title or the up/down arrow in the header.

Hidden sections will automatically expand to reveal validation errors on Authorisation or Approval.

## 2025-07-24 — External email form attachments (platform)

We've updated Email integrations to support sending of form attachments to third parties.

The "External" option for "Attach Email Files" still excludes form attachments by default, but you can now include specific attachments by using the tag name of the relevant attachment in the body of the email.

## 2025-07-01 — Revalidate (platform)

We've updated the "Send New Request" button within validation elements in Workflow.

This button appears when a validation is in Requesting, Check or Fail status.

The original intent was for it be used with biometric identity verifications where a form user had lost their request link or needed to re-verify.

We've since found that this feature is useful for other validation types that don't involve sending a request e.g. where form data has been edited post submit

As such the button now appears for all validation types as **Revalidate** except biometric identity verification where it will remain as **Send New Request**

## 2025-05-30 — Auto Generate Tag Names (platform)

We've updated the **Auto Generate Tag Names** option to **exclude** hidden formulas, sections, and groups. These are generally not required for templates or mapping, and can cause confusion if they're included.

## 2025-05-20 — Sentence Case (platform)

We've added a new format option **Sentence Case** for Text questions.

This will auto-capitalise the first letter of any text entered, and leave the rest unchanged.

This is different to **Title Case** which auto-capitalises the first letter of each word entered, and forces other letters to lower case.

Sentence Case may be useful for capturing Names where you always want the first letter capitalised, but don't want to interfere with subsequent capitalisation around names like O'Shay or MacDonald.

## 2025-05-19 — Workflow Authorisation (platform)

We've made a few improvements to Authorisation, which is an optional feature of workflow.

* If your form is configured with an **Authorisation Assignment Expression** (meaning the current workflow user must request authorisation from someone else) then the "Decline" button will now appear as "Revert". The functionality behind this button hasn't changed, we've just made it more obvious that the form will be sent back to the person that requested authorisation if it can't be authorised.

* The system will now prevent you from assigning a form to someone that doesn't have permission to authorise it during **Authorisation**

* If your form is *not* configured with an **Authorised Assignment Expression** (meaning the person authorising the form can also approve it) we'll now automatically Approve the form on Authorisation, saving an additional click (and potential confusion)

## 2025-05-01 — Validation Lock (platform)

We've added a new Format option **Lock** to Validation elements.

This option is slighly counter-intuitive, as it won't actually trigger any validation. Instead it allows a Validation element to act as a container of other elements that can be locked for edit when a button in the form is clicked.

This may be useful where you have an element or elements that heavily influence content in the rest of the form, and you don't want users to switch values once selected.

We offer similar fuctionality with the **Forward-Only** option for sections, but that applies to a whole section, and doesn't allow you to go back and view those details once you have moved to the next section.

## 2025-04-13 — Malware detection (platform)

FormsByAir has been scanning file attachments for viruses using ClamAV for some time.

We've now extended our scanning to detect the **type** of a file irrespective of its extension or mime type. If the detected type doesn't match with an allowed type, we flag the file as potential malware.

In addition, if the detected file type is .html or .svg we scan the contents for javascript, and if present the file is also flagged as potential malware.

This change applies to both attachments in forms and uploads to our portal.

## 2025-04-11 — Checkbox outline (platform)

FormsByAir uses the popular **Bootstrap** library to style our forms.

In recent versions, the Bootstrap team have moved towards a low-contrast aesthetic, which among other things, has seen them lighten the border colour of checkbox and radio buttons.

We've had feedback from multiple customers that the border colour is now too light, and difficult for form fillers to distinguish.

As such we've restored the previous (darker) grey by default. This can still be overridden with custom CSS.

It's worth noting that the click area for checkboxes and radio buttons has always included the corresponding *label* in addition to the actual control.

## 2025-04-09 — Document max lifetime (platform)

We've added a new, optional account level setting **Max Lifetime** which defines the maximum number of days that we will hold form data for each document.

When set, any document that was started before the max lifetime threshold will be purged without notification, irrespective of status.

Our system is designed for all documents to be delivered or eventually expire, however documents that are **Saved** or in **Workflow** use *rolling* expiries, and can be retained indefinitely with continuous engagement.

This new feature serves as a hard limit to guarantee that we only hold form data for a specific period, which may be useful for compliance with privacy policies.

Reminders can be set for any document status to avoid unintended loss of data.

## 2025-04-03 — Attachment filename validation (platform)

Our forms have always had validation to check that the filename for an **Attachment** question inside of a repeater is unique within that repeater.

The original intent behind this was to block accidental attachment of the same file for inline or tabular style repeaters.

However the validation also applied to regular content repeaters, where it can be valid to attach the same file, meaning form users would sometimes need to rename a file in order to attach it.

To address this we've changed the validation so it now only applies to repeaters where Format is **Inline** or **Table**

## 2025-03-31 — Authentication Policy update (platform)

**Two Factor Authentication**

Where Two Factor Authentication is enabled, we'll now save successful authentication to a separate cookie with a 30 day expiry. This is more convenient for users logging back in on the same device, as they'll only need to complete 2FA if it's been at least 30 days since they last completed 2FA.

Username/password authentication continues to use a sliding 5 day expiry by default.

**Session Timeout**

If the option *Must log in every session* is enabled then Username/password authentication uses a session-based cookie.

We've enhanced this option to now include a timeout after 60 minutes of inactivity. As such, if a user leaves our portal open in a browser for more than an hour, and then attempts to take some action, they'll be forced to log in again.


For maximum protection we recommend enabling both *Must log in every session* and *Must use Two Factor Authentication* for your account.

## 2025-03-31 — Block restricted file types (platform)

When attaching files to a form, we automatically apply a filter to the file selection dialog so that only acceptable file types are listed e.g. PDF or JPG

Users can however change this to show *all files*, and could attach a file with a restricted type e.g. EXE or BAT

We already scan all file attachments for viruses and malware, but to further protect against malicious or accidental attachment of restricted files, we now block any file that doesn't match our list of [acceptable file types]({{ site.baseurl }}/questions/types/attachment/) - both in forms and our API.

## 2025-03-01 — IP address masking (platform)

For additional privacy, we will now mask out the end of IP addresses in our logs when a document is purged.

For example, 123.123.123.123 will become 123.123.\*\*\*\*\*\*\*

## 2025-03-01 — .NET Core Upgrade (platform)

Our .NET Core Upgrade is complete, all systems are running normally.

## 2025-02-24 — .NET Core Upgrade (platform)

We've been working on a code framework upgrade for our application for some time, which we're now ready to apply to production.

This upgrade will take us from .NET Framework 4.8.1 to .NET Core 8, which is the latest LTS version of .NET, and will keep us current with all security and performance improvements, and potential new features.

We're aiming to apply the upgrade on **Saturday 1st March 3pm NZT.**

**There will be no downtime during the upgrade.**

There are no functional changes to forms, our portal, or our API **except** for the minor items listed below. The only noticeable difference should be a performance improvement!

* The API endpoints below return a string instead of JSON, our new application will correctly return a Content-Type header of text/plain instead of application/json for these:

DELETE /api/v1/documents/deliveries/{id}  
PUT /api/v1/documents/{id}/return  
PUT /api/v1/documents/{id}/restore

* All API endpoints that return JSON will now **exclude** null properties by default, in line with modern REST API standards

* Existing API keys will be deprecated, and you will need to generate new API Keys soon after the upgrade. That's because .NET Core doesn't natively support the original OWIN-based bearer tokens from .NET Framework. We have migrated to encrypted JWT bearer tokens with .NET Core. New API Keys will work exactly the same way with our API, and have the same 3 year expiry. We'll continue to support existing API Keys until we've confirmed that the last API user has migrated to a new key.

## 2025-02-09 — Third party request shared (platform)

By default, the information submitted in third-party requests is hidden from other people completing requests in the same form.

This is good for the typical use-case where you're capturing personal details for multiple people that don't need to be shared with the group.

However, in some cases, you may need to share this information, so we've added a new **Shared** option to Request elements.

## 2025-02-06 — Third party request prompt (platform)

We've updated the prompt within the "blue box" for non-mandatory third party requests to clarify that users have a choice for us to send the request link, or they can send it themselves.

**Previous Message**  
Add an email address &amp; message below if you want us to send the request automatically, then click Generate Request.

**New Message**  
Add an Email Address below if you want us to send the request link for you, otherwise leave blank if you'd prefer to send it yourself, then click Generate Request.

## 2025-02-02 — Country name update (platform)

We've updated the FormsByAir Countries data table renaming "Viet Nam" to "Vietnam".

"Viet Nam" is the official ISO-3166 country name as per <https://www.iso.org/iso-3166-country-codes.html> but "Vietnam" is more widely recognised amongst our clients.

## 2025-01-13 — User downloads (platform)

"User download" file integrations have previously only been available *after* form submission to download a copy of what was submitted.

We've now extended these integrations to support "portal" style forms, which typically *display* information, often from an external data source.

If you configure a User Download integration for a form with **Submission Mode = None** we'll now automatically render a Download button at the bottom of the page. Clicking the button will trigger the form to save, and then immediately return the corresponding file.

In making this change we've updated the original file purpose description from "Download on submission" to "User Download" to cover the extended capability.

## 2024-12-23 — Popup alerts (platform)

We've switched all popup alerts to use modal dialogs instead of the native alert() and confirm() Javascript functions.

Some web browsers prompt users to *suppress* repeated native alerts, leading to possible confusion.

In addition, modal dialogs offer a consistent user experience across devices and browsers, and incorporate custom styling for your form e.g. font, button colour

## 2024-12-15 — Display content lists (platform)

We've made the following changes to bullet and numbered lists for **Display Content** and **Terms** elements in both form view and auto-generated Word/PDF output.

The intent is to make it easier to display complex text or legal terms in a clean format without needing custom styling in the form, or a custom template for Word/PDF output.

* Bullets and numbers are now centered within their margin to appear less "gappy"
* We've reduced the vertical space between each item slightly
* We now support up to 5 levels of indentation

See [Display Content]({{ site.baseurl }}/questions/types/display-content/)

## 2024-12-02 — Validation method validation (platform)

We've updated the form builder to check that **Validation Methods** for elements have been defined in the **Script** section.

## 2024-12-01 — Workflow expiry is live (platform)

All documents in **Workflow** now have a 60 day rolling expiry. Documents in **Requesting** status after 30 days will now move to Workflow for review if enabled, otherwise they will expire.

## 2024-11-09 — ID verification support (platform)

We've made a couple of changes to help teams that are supporting ID verification requests:

* We'll now show a list of reasons for a **Check** status alongside the status indicator e.g. "Address Not Verified"

* A new "Copy Link" button will retrieve the unique link for pending ID verification requests. This may be useful where a form filler didn't receive the link via text or email.

## 2024-11-04 — Workflow expiry (platform)

As part of our data retention policy to minimise the time that form data is held in our system, we're planning to introduce rolling expiry to Workflow effective **1 December 2024**

The default workflow expiry period will be **60 days** but this can be adjusted per form between 10 and 90 days. A "rolling expiry" means that the expiry period will reset every time you take some action e.g. reassign, comment, authorise, so a document will never expire while you're actively working on it.

In addition, we're adding a **Snooze** function so you can hold a document in Workflow for a specific period of time if it can't be processed immediately. Snoozed documents will be hidden by default unless you specifically filter for them, and will reappear at the end of the snooze period, triggering a notification to the user that initiated the snooze.

We'll display the expiry date for all workflow documents in our portal and allow you to filter for documents that are expiring soon.

On expiry, our system will send an automated email notification to the assignee, or users that have interacted with the document, or all workflow/admin users. The document can then be restored if necessary within the data retention period for your account. You can continue to set custom reminder emails at any frequency for documents in Workflow.

We also plan to make the following related changes:

* Documents in **Requesting** status after 30 days will now automatically move to Workflow Pending status for review if workflow is enabled for the form, otherwise they will expire. "Requesting" means a form has been submitted but is waiting on post-submit ID verification. You can continue to set custom reminders at any frequency for documents in Requesting status.

* The **Edited** workflow status will be retired, as this masks a document's true status, and we already record edits in the Workflow log

We'll reset the expiry clock on all documents in Workflow when we apply this change on 1 December, even if they've already been in workflow for some time. As such the earliest that any document in Workflow will expire (assuming the 60 day default) is 30 January 2025.

We'll be in touch directly if you have a large number of very old documents in workflow so we can discuss options to bulk export or expire them.

## 2024-10-07 — Portal pagination (platform)

We've made a couple of changes to our portal to improve pagination of lists

* Automatically show more items per page on larger screens
* Indicate how many items are displayed and the total number of items available

## 2024-09-13 — Prefill confirmation (platform)

We'll now display a confirmation message instead of the normal share links when manually prefilling a form that includes an "On Request" email.

This may be useful where the prefiller of the form should not have access to the resulting document after it's been generated and sent to the person that needs to complete it.

## 2024-09-06 — Workflow block same authoriser (platform)

We've added a new Workflow option if Authorisation is enabled to block users from **approving** submissions that they've **authorised.**

This may be useful if you need to ensure that two different people have checked a submission before it's delivered.

## 2024-09-02 — Workflow updates (platform)

In order to quickly understand the current status of a document in workflow, we'll now display any comment associated with the last workflow action at the top of the **Document** page. Users can continue to see *all* workflow actions and comments on the **Information** page.

We've also added the following metrics to the Workflow section of our Analytics page:

* Workflow Rate  
* Approval Rate
* Throughput

## 2024-08-26 — Form assets (platform)

Added the ability to upload and manage file assets e.g. images and PDFs that will be hosted by FormsByAir for use in forms and email templates.

## 2024-08-26 — Search by delivery reference (platform)

You can now search for an integration delivery reference e.g. an email address or confirmation code to find a document in the Log.

## 2024-08-11 — Form design validation (platform)

Added validation to the form designer to block conditional paths within inline or tabular groups. These aren't supported because they'd potentially cause column alignment issues.

Also added validation to ensure that Tag Names don't contain &#39; &quot; &lt; [ ] &gt;

## 2024-06-19 — Join function (platform)

The &lt;&lt;[Join]&gt;&gt; function is now available client-side (in-form), see [Join Function]({{ site.baseurl }}/tags/functions/join/)

## 2024-06-05 — Stage 2 AML/CFT regulation changes (compliance)

Additional AML/CFT regulations have come in to force for NZ reporting entities as of 1 June 2024, please see link below...

<https://www.fma.govt.nz/assets/Guidance/Supervisory-approach_new-AMLCFT-Regs_17-May-2024.pdf>

We've updated our CDD & Investment form templates to accommodate these changes as follows:

* Capture constitution and shareholder agreement for companies. FormsByAir can automatically pull a Company Extract from MBIE, but these other documents will need to be manually attached
* Capture source of wealth for entities related to client e.g. a trust that owns more than 25% of a company
* Capture settlors and protectors for trusts
* Mandatory affirmation for entities that all relevant people have been included in the form

## 2024-06-05 — HubSpot (integration)

We've added a new integration with [HubSpot](https://www.hubspot.com/)

## 2024-05-21 — Form element class names (platform)

We've added explicit class names to key form elements so you can customize, move or hide them with CSS

form-background  
form-status  
form-status-left  
form-status-right  
form-button-back  
form-button-next  
form-button-submit  
form-button-file-select  
form-button-file-cancel  
form-button-request-share  
form-button-request-copy  
form-button-request-open  
form-button-repeater-add  
form-button-repeater-add-another

## 2024-05-14 — Disable save until start (platform)

The **Save & Finish Later** button in all *blank* forms will now be disabled until the form is **started** (by entering data or making a selection in the form)

This does not apply to requested or previously saved forms.

Saving a blank form meant that any "On Start" integrations could be bypassed.

## 2024-05-14 — Two Factor Submit (platform)

We've added support for email-based two factor authentication when submitting prefilled forms.

This can be enabled and used as follows:

* Set Submission Mode to **Code**
* Add a new "On Submit Code" email integration. The recipient of the email should be &lt;&lt;[DocumentRequestedEmail]&gt;&gt; and the body of the message should contain &lt;&lt;[DocumentSubmitCode]&gt;&gt;
* Prefill the form using our API, set **RequestedEmailAddress** to the email address you hold for the form-filler
* When the form is submitted, FormsByAir will send your "On Submit Code" email to **RequestedEmailAddress** including a 6-character short-lived code
* A valid code must be entered in to the form to complete submission
* This does not affect the ability to save forms

## 2024-04-17 — Bulk Export/Import integration support (platform)

We've updated our portal so you can now **Cancel** a bulk export or import integration that you consider has been running too long or may have errored.

In addition, the Integration Log now displays the name of the user that triggered an integration to start processing.

## 2024-04-10 — Generate JSON Map (platform)

We've added an option to *generate* a default map for **JSON From Map** integrations to provide a more convenient starting point for data mapping. Note - this will only include elements that have a tag name.

## 2024-03-26 — New Portal (platform)

Our new management portal is operating well so we've gone ahead and removed the temporary switch back to the original portal. Any further issues that arise will be addressed in the new portal.

## 2024-03-25 — Signature instructions (platform)

We've updated the instructions for Signature and Diagram elements (below). We previously checked for the presence of a touchscreen and displayed different instructions for mouse-only devices, but this was confusing on devices with multiple display types. We've also re-positioned the text above the signature box so it's visible while signing.

*Use your touchscreen or hold your mouse button down and move the pointer in the box below to sign*

## 2024-03-21 — Third-party request instructions (platform)

We've updated the instructions for third-party requests (below) to clarify the intent that they be used to capture information from other people that are **not located with the main form filler.**

*If you need someone else to help with this part and they're not with you right now, add what you can, then send them a request to complete on their own device.*

## 2024-03-20 — File Import user (platform)

We've updated File Import integrations so the user that initiates an import will now be associated with the corresponding document(s) that are created.

This may be useful if you want submissions of those documents in workflow to be assigned to the user that imported them for example.

## 2024-03-12 — New Portal (platform)

Our new management portal is now live, users can temporarily switch back to the original portal if something is not working as expected.

## 2024-03-08 — Phone number validation (platform)

We've updated phone number validation so that error messages for invalid **International Mobile** numbers are no longer dismissable.

We previously allowed form fillers to continue with invalid mobile numbers to manage potential false positives.

The problem is that mobile numbers are often captured so they can be used for text messaging, and without strict validation, too many people mistakenly enter landline numbers.

Errors for **International** phone number validation (where landline or mobile numbers are acceptable) can still be ignored.

## 2024-03-05 — New Portal (platform)

Our new management portal will become the default option from 12 Mar 2024, we'll offer a temporary opt-out to the original portal as a backup.

## 2024-02-19 — Import form data (platform)

Forms that contain a single, active **Import** integration will now include an Import option on the Forms page of the portal, allowing non-Administrators to import form data. This is available to all roles except Workflow.

The Import and Log options are still available for individual Import integrations on the Form Integrations page for Administrators.

We recommend you review the roles assigned to users that were only given Administrator access because they needed to import data, in most cases you should be able to reduce their access to a non-Administrator role.

## 2024-02-19 — Independent Role (platform)

We've added a new **Independent** role as a combination of the **User** and **Workflow** roles for users that need to submit forms and manage their own workflow.

## 2024-02-13 — Hidden formula visibility (platform)

Hidden formulas are now hidden by default when viewing a document in our new portal to reduce unnecessary "noise".

They can be toggled on/off with a switch at the bottom of the page, hidden formulas that are also set to **read-only** will remain hidden.

## 2024-02-12 — New Portal (platform)

Our new management portal is available to preview from today for all partner administrators.

Next time you log in you'll see an option at the top "Try New Portal" where you can enable it, and also switch back to the original portal if required.

Most features appear and operate the same as they did before, but with a fresher look, better performance, and more consistency.

Here is a detailed list of what has changed:

**General**

* Upgraded to the latest underlying browser frameworks including Angular 17.x and Bootstrap 5.3
* Updated WSYWIG HTML and template editor to TinyMCE
* Updated Code editor to the latest ACE Editor with syntax highlighting
* Workflow > Log menu moved to Documents menu
* All admin functions including Profile, Tables, Users and API keys moved to a single Administration menu
* All pages listing multiple items now include the ability to filter those items
* Unique identifiers for items are now hidden, replaced with a "Copy Id" menu option

**Form Builder**

* Replaced drag-and-drop with cut-and-paste for more accuracy when moving elements around
* Added Group/Ungroup options to easily move a block of elements
* Additional validation to check for issues when saving a form design

**Document View**

* Uses the same display engine as when you fill out a form for a more consistent view
* Workflow elements can now leverage the full range of form functionality, the previous Document View used a cut-down display engine
* Hidden formulas are hidden by default, but can be toggled on/off with a switch at the bottom of the page


Assuming all goes well we plan to continue the rollout as follows...

* Extend the opt-in preview to all portal users in a couple of weeks
* Make the new portal the default option in early March, but retain an opt-out
* Remove the opt-out option later in March

## 2023-09-15 — Monday.com file attachments (integration)

We've updated our Monday.com integration to support file attachments.

Our system can now create an "Update" against a new or existing board item, which will include the output of File integrations and form attachments.

## 2023-09-12 — Dynamics 365 Sales (integration)

We've added a new integration with [Dynamics 365 Sales](https://dynamics.microsoft.com/sales/overview/)

## 2023-09-12 — Log document access (platform)

We now log all access to form data made via our portal or API while it's temporarily held by us (prior to purge)

## 2023-09-12 — New email reminder triggers (platform)

We've added new triggers for email reminders as follows:

|**After Start**|Prompt users that may have abandonded a form to see if they need help. Requires **Auto Save** to be enabled for the form.|
|**In Workflow**|Keep track of documents that have been in workflow for an extended period of time by emailing the assignee or an administor.|

## 2023-06-29 — Saved Documents filter (platform)

We've added the ability to filter the list of Saved Documents in our portal by Form, Stage and Reference. This replaces the previous Search by Reference function.

## 2023-06-27 — Default Value validation (platform)

We've updated our form builder to validate Default Values if an expression with &lt;&lt;tags&gt;&gt; has been entered.

For example, if you have a Text element and enter a Default Value of &lt;&lt;Name&gt;&gt; you'll receive an error *Set numeric question type/format or add quotes around tag*

This validation does not apply if the Default Value is a function or static value.

## 2023-06-21 — Prompt to save (platform)

In order to minimize dropouts when form fillers are missing information, we've extended the popup message that appears when attempting to submit or move to the next section as follows:

Can't submit form, one or more questions have missing or invalid entries. *If you need to pause to gather more information, use Save & Finish Later at the bottom of the form and resume when ready.*

This additional text will only appear the first time you attempt to submit, and only if saving is enabled for the form.

## 2023-06-16 — Form Analytics (platform)

We've added new per-form analytics to provide insights in to how form fillers and your team are using your forms including:

* Median completion time
* Drop outs per section
* Conversion Ratio
* Median time in workflow
* Return rate

Administrators can access this information by selecting Action > Analytics against a form in our portal. In addition, we've renamed Documents > Analytics to Documents > Activity and added a click through to form analytics from there. This is available to everyone in the Operations role or higher.

## 2023-05-25 — Controller role (platform)

We've added a new **Controller** role with the permissions of a Supervisor plus the ability to delete and restore documents, see [Roles]({{ site.baseurl }}/account/roles/)

## 2023-05-19 — Attachment filenames on iOS (platform)

We've updated the **Attachment** question type so that files attached with the **Take Photo** option on iOS are renamed from the default "image.jpg" to a unique filename e.g. "image20230519T125236.jpg" to avoid warnings about duplicate files.

This does not affect the attachment of existing image files.

## 2023-05-04 — Phone number validation (platform)

We've updated our default phone number validation (where **Format** is Auto) to check that the input contains at least 5 digits.

This does not apply if **Format** is set to International or International Mobile for country-specific validation.

## 2023-05-01 — Workflow export (platform)

You can now export workflow data for all of your forms including comments to a CSV file for your records.

To access, go to Workflow > Log then click the Export button.

## 2023-04-21 — Cloudcheck Go inline verification (platform)

We've extended our Cloudcheck Go integration to support **inline** identity verification in addition to post-submit verification.

This may be useful where you have very complex forms completed over a period of several weeks or months.

Post-submit verification is useful where you want to minimise the upfront effort for submission.

## 2023-03-05 — Element Id (platform)

The unique Id for form elements now appears bottom-right when you expand an element in the form designer. This may be useful where you need to refer to an element by Id with our API.

**List Type** for Option Lists has moved up slightly and is now labelled **Format** to be consistent with other element types.

## 2023-02-27 — Validation Reset & Return (platform)

We've added an additional action to help manage incomplete validation requests as follows:

|Action|Description|Use When|
|---|---|---|
|**Reset & Return**|Delete outstanding request, return the document|Form user can't complete validation or failed validation and should retry or choose a different path through the form|

The existing actions remain as follows:

|Action|Description|Use When|
|---|---|---|
|**Resend Request**|Delete outstanding request, create & send new request|Form user can complete validation, but lost the original request|
|**Cancel**|Delete outstanding request, continue with form processing|You no longer require validation, no form changes required|

## 2023-02-23 — Document log third party requests (platform)

The Document > Log view in our portal now excludes third party requests to avoid confusion around duplicates.

Third Party requests are still accessible from the Information page of requesting documents, or if you search the log using the Document Id for a request.

## 2023-02-11 — Form attachment upload (platform)

We've made a few changes to help improve the reliability of submitting forms with multiple/large attachments, particularly over slower internet connections.

Our system will now split out each file attachment to a separate request, then upload form data at the end. Failed requests will be retried automatically, for example, where the connection is interrupted part way through.

We'll also now show percent complete while attachments are uploading so users have an indication of how long the process will take.

## 2023-02-02 — Google Analytics (platform)

We've updated our Google Analytics integration to align with our own built-in analytics, see [Google Analytics]({{ site.baseurl }}/hosting/google-analytics/)

## 2023-01-26 — WebHooks (platform)

We've added two new webhook triggers in addition to **On Submission**

* On Save
* On Requesting

## 2023-01-26 — Workflow Authorised Only (platform)

We've added a new option **Authorised Only** for Workflow elements, which is available when **Requires Authorisation** has been enabled for a form.

Content within a Workflow element with this option enabled will only be displayed when a document's workflow status is **Authorized**

This may be useful where you have additional information that should only be captured or mandatory once a form has been authorised.

## 2023-01-19 — Third Party Review Request (platform)

We've extended the functionality of requests to support the mandatory review of a form before submit with a **user selectable third party**, for example, a financial adviser.

To enable, the request should be located at the end of the form with both **Required** and **Lock Form** selected.

The form will force the generation of a request before it can be submitted, and will then lock all content to ensure it can't be changed after review. The main form filler can **Cancel** the request if they need to make additional changes, or send the request to someone else.

Once the third party has completed their part the main form filler can then submit the form.

Forms needing review by a *specific* person or group should continue to use a mandatory third party request in a staged form.

## 2022-12-06 — Malware detection (platform)

FormsByAir will now automatically scan all form attachments for malware including viruses using [ClamAV](https://www.clamav.net/) immediately after submission.

If a document containing an infected file is detected, the document will be quarantined and account administrators will be notified by email. Quarantined documents can then be viewed and deleted in our portal.

## 2022-11-23 — Return document in requesting status (platform)

We've updated our portal so users in the [Workflow]({{ site.baseurl }}/account/roles/) role or higher can now Return a document in [Requesting]({{ site.baseurl }}/documents/status/) status.

This may be useful where you need the form filler to add or remove verification requests without interrupting other outstanding verification requests.

## 2022-11-16 — Microsoft Sharepoint Document Library (integration)

We've extended our Microsoft Sharepoint integration to support file delivery to Document Libraries.

## 2022-11-02 — Copy connected service credentials (platform)

We've added the ability to copy the credentials for a connected service from Production to Test and vice versa where there is no requirement for these to be different.

We'll also display an arrow icon next to each service to indicate that Production and Test are using the same credentials.

See how [Form Status]({{ site.baseurl }}/forms/status/) relates to Production/Test credentials.

## 2022-11-02 — Manage verification requests (platform)

We've added two new options to assist with outstanding verification requests:

* **Cancel Request** is available for requests in **Requesting** status, and can be used where verification has been completed by some other means, or is no longer required. If there are no other outstanding requests the document will move on to workflow or delivery.
* **New Request** is available for requests in **Requesting** or **Fail** status, and will trigger a new request to the original recipient. This may be useful where a previous request has been lost, or has expired, or the recipient completed verification but failed and will retry.

## 2022-11-02 — Purge now (platform)

We've added the ability for **Administrators** to **Purge** individual documents in **Deleted** status to immediately remove form data from our system.

This feature is also available via a new [API](https://formsbyair.com/swagger/ui/index#/Documents/Documents_Purge)

## 2022-11-02 — Retry integration (platform)

We've added a new option to force a **Retry** for an integration in **Check** status, which is more intuitive than having to Disable/Enable the integration.

## 2022-10-20 — Upgrade document (platform)

We've updated our portal so **Administrators** can now upgrade a document to the latest form version.

This may be useful where you need to make an urgent change to a form, and have that change apply to a **Requested** or **Saved** document.

## 2022-10-18 — Workflow for supervisors (platform)

We've updated the Documents &gt; Workflow view in our portal to include documents assigned to other people or teams for users in the **Supervisor** role, see [Roles]({{ site.baseurl }}/account/roles/)

## 2022-09-27 — Filename tag format (platform)

We've added a new **filename** tag format to sanitize tag values with the same rules we use for filenames. e.g. strip out characters like *, \, /, ?

## 2022-09-15 — Cliniko custom fields (integration)

We've extended our [Cliniko](https://www.cliniko.com/) integration to support custom fields.

## 2022-09-09 — ActiveCampaign (integration)

We've added a new integration with [ActiveCampaign](https://www.activecampaign.com/) CRM and email marketing software.

## 2022-09-07 — Linked repeaters (fix)

We've resolved an issue where linked repeaters within other repeaters were not reloading correctly in saved forms.

## 2022-08-29 — Requesting documents (platform)

We've added a new view to our portal for **Requesting** documents.

These are documents that have been submitted, but are waiting on post-submit identity verification or a staged third party request.

Requesting documents will also appear in Workflow if enabled for the form.

## 2022-08-19 — Mandatory 2FA for partners (platform)

Two Factor Authentication is now mandatory for all FormsByAir partner accounts.

## 2022-08-15 — Cloudcheck IDscan (integration)

We've updated our Cloudcheck integration to support [IDscan](https://www.verifidentity.com/cloudcheck/#idscan) for biometric identity verification with Cloudcheck Go.

## 2022-08-12 — Switch format (platform)

We've added a new **Switch** format for **True/False** questions to display a more modern sliding switch icon instead of a checkbox.

## 2022-08-05 — LegalOffice (integration)

We've added a new integration with [LegalOffice](https://legaloffice.co.nz/) practice management software.

## 2022-06-15 — Attachment File Types (platform)

We've changed **Attachment** questions to filter for specific file types by default. The intent is to:

* Reduce the chance of us accepting and delivering potentially dangerous files
* Trigger conversion (automatic or manual) of HEIF and HEVC files on iOS & macOS devices, as these formats have limited support outside of Apple's ecosystem.

The default file types are listed below:

|File Type|
|---|
|application/pdf|
|application/msword|
|application/vnd.openxmlformats-officedocument.wordprocessingml.document|
|application/vnd.ms-excel|
|application/vnd.openxmlformats-officedocument.spreadsheetml.sheet|
|application/vnd.ms-powerpoint|
|application/vnd.openxmlformats-officedocument.presentationml.presentation|
|text/plain|
|text/csv|
|image/jpeg|
|image/png|
|image/gif|
|image/tiff|
|audio/mpeg|
|video/mp4|
|video/mpeg|
|application/zip|
|.msg|
|.eml|

## 2022-06-15 — Form View Upgrade (platform)

All forms are now running with our new view engine. Please advise us if you notice any issues.

## 2022-06-01 — Form View Upgrade (platform)

We've now applied the first update for our form view engine as mentioned in the previous post. Any form you open from our portal will now use the new view engine.

Forms opened on public links e.g. https://your-company.formsbyair.com/... will continue to use the existing view engine for now. Please check your forms and advise us if you notice any issues.

We're planning to update the view engine for all form links and users on **Wednesday 15th June 2022.**

## 2022-05-25 — Form View Upgrade (platform)

As part of our mission to always provide the best online forms experience, we are announcing an upgrade to our form view engine to incorporate the very latest web technologies.

Your forms will look and behave almost exactly the same as they do today, they'll just be a little sharper, faster and even more secure.

A big part of the efficiency and performance improvements come from us being able to leverage functionality now built-in to modern web browsers like Chrome, Edge, Safari & Firefox, but it does mean we'll need to end support for all versions of Internet Explorer.

Microsoft has been phasing out IE in favour of Edge for some time. It's currently running at ~0.5% global use, and will be officially retired by Microsoft on 15 June 2022. Any users that do access your forms with IE will be presented with the following message:

* Our forms require a modern web browser to run.
* Internet Explorer has been retired by Microsoft, please upgrade using the link below.
* [Get Started with Microsoft Edge](https://go.microsoft.com/fwlink/?linkid=2192466)

We're planning to execute this upgrade in two phases beginning **Wednesday 1st June 2022**. You will receive more details about the process via email.

Here is a summary of the technical changes in our form view upgrade:

* Upgrade from AngularJS 1.8.2 to [Angular 13.3.9](https://angular.io/)
* Upgrade from Bootstrap 3.4.1 to [Bootstrap 5.1.3](https://getbootstrap.com/)
* Upgrade from Angular UI Bootstrap 2.5.0 to [Angular Bootstrap 12.1.2](https://ng-bootstrap.github.io/#/home)
* Drop support for all versions of Internet Explorer
* Default font size has been increased by 1pt for desktop and mobile view
* Removed drop-shadow from form border
* Improved Date Picker
* Slight colour change to buttons (unless overridden with custom styling)
* Slimmer progress bar
* New "outline style" icons for warning & validation messages

Try sample forms here...

* [New Patient](https://fba.formsbyair.com/forms/new-patient)
* [Customer Due Diligence](https://financialservices.formsbyair.com/forms/cdd)

## 2022-04-06 — Save Workflow (platform)

We've moved the **Save** button for documents with workflow from the Options popup menu to the main menu bar. The intent is to make it more obvious that workflow changes can be saved without having to approve the document.

## 2022-03-01 — REST API Validation (platform)

We've added a new integration option to validate form data with a generic **REST API** and populate the result back into the form.

## 2022-01-21 — Preview Mode (platform)

We've added a new **Preview Mode** option so you can quickly review all of a form's content without validation.

Forms can be opened in preview mode from our portal, or by adding a querystring parameter "preview=1" to the URL for any form.

Preview Mode does not require authentication, so can used with Published (Public) and Test (Public) forms.

## 2021-11-23 — Cloudcheck Go (integration)

We've updated our Cloudcheck integration to support [Cloudcheck Go](https://www.verifidentity.com/cloudcheck/#cloudcheck-go) for combined biometric and data source identity verification.

## 2021-11-13 — Encrypted PDF (platform)

We've added a new file format option **PDF From Template Encrypted**

The resulting file will be encrypted with a randomly generated Owner password and will not allow edits.

## 2021-10-29 — ClaimControl (integration)

We've added an integration with [Alphatec ClaimControl](https://www.alphatec.net/software-solutions/insurance-management/) to create claim records from forms.

## 2021-10-13 — Form designer improvements (platform)

We've made a couple of changes to our form designer as follows:

* We've removed the "Advanced Settings" toggle so that all settings for the selected element are always displayed.
* We now check for missing integrations on form save. You may see this error if you've copied individual elements from another form, or you've deleted an integration.

## 2021-10-05 — Confirmation Type (platform)

We've consolidated the form settings **Hide Form After Submit** and **Submit URL** in to a new setting "Confirmation Type" to better describe the behaviour of the form on submit. The options for this setting are as follows:

* Disable form and show confirmation message at the bottom of the page
* Hide form and show confirmation message at the top of the page
* Redirect to a custom confirmation page

**Return URL** is only available for the first two options, as this relates to redirection *after* a confirmation message has been displayed when a user clicks the "Close" or "X" buttons.

## 2021-09-25 — Two factor authentication policy (platform)

We've added a new account level setting for two-factor authentication so you can now make it mandatory for all of your users. Once enabled, users that haven't previously setup two-factor authentication will be prompted to do so the next time they login.

In addition, some newer integrations will automatically enable this setting when added to your account, for example Xero Practice Manager.

## 2021-09-25 — Xero Practice Manager (integration)

We've added an integration with [Xero Practice Manager](https://www.xero.com/nz/xero-practice-manager/) to create Client and Contact records from onboarding forms.

## 2021-09-20 — Address Picker data (platform)

We've updated our default Google Places Address Picker to bring it in to alignment with our other Address Lookup services.

It will now store the component parts of an address in a common address model, which can be accessed with tag properties both in-form and in integration templates e.g. &lt;&lt;Address.City&gt;&gt;

See [Address Model](https://formsbyair.com/swagger/ui/index?urls.primaryName=schema%2Fintegrations%2Fswagger.json%3Fv%3D101)

## 2021-09-15 — Google Sheets picker (platform)

We've updated our Google Sheets integration to use Google's "Picker" in our portal to make it easier to select a target spreadsheet.

## 2021-09-13 — MBIE Beneficial Owners (integration)

We've added a new option to our NZ MBIE integration to return Beneficial Owners as follows:

* All current directors for the entity; plus
* All individual shareholders with > 25% effective holding calculated by parsing the full ownership structure of the entity

## 2021-08-29 — Conditional last section (platform)

Previously, forms with *conditional* sections would always need a final section that was *not* conditional in order to function correctly.

We've applied a change so that this is no longer required.

The last non-conditional section will show a Submit button as before. On Submit, if the condition for the next section is not met, the form is submitted. If the condition is met, the next section is displayed, and the progress bar is updated accordingly. If the user moves back and updates the form so the condition is no longer met, then clicks Next, the form will recognise that the next section is no longer applicable, and will stay in place, change the Next button to Submit, and update the progress bar.

## 2021-08-23 — Build Form (platform)

We've updated the "Build Form" option in the portal to better reflect our intent for how clients and partners should use the platform.

The new option allows Administrators to add a blank form, copy another form, import a schema to a new form, or create a Work Request for FormsByAir to action.

## 2021-08-18 — Pattern mask (platform)

We've updated the **Pattern** question type so you can now define an input mask in addition to regex-based validation, see [Pattern]({{ site.baseurl }}/questions/types/pattern)

## 2021-08-16 — Analytics (platform)

We've applied the following changes as part of an on-going effort to improve analytics within FormsByAir.

* We've renamed Documents &gt; Statistics to Documents &gt; Analytics in the portal.

* We now capture a "Start" event for blank forms after they've been open for 10 seconds, as we previously had no way to track forms that were opened, started, and then abandonded.

* "Started" and "Expired" statuses are now included in Documents > Analytics to provide information on the rate of completion.

We'll be expanding the Analytics section further in future to show statistics like "Average time to complete" and "drop off" sections for incomplete forms.

Forms can still be configured to log to a Google Analytics or Google Tag Manager account where you need to integrate with marketing campaigns for example.

## 2021-08-10 — Copy form integrations (fix)

We've improved the error handling around copying forms so the system will now warn you if it can't find a direct match for lookup, validation and payment integrations used in the source form.

## 2021-08-06 — Active (Private) form status (platform)

We've renamed the form status **Active (Private)** to **Published (Private)** for better consistency across the platform.

## 2021-08-06 — Form filters (platform)

We've added the ability for Administrators to filter forms by title and status in the portal to make it easier to navigate when you've got a lot of forms.

## 2021-08-05 — FormsByAir document access (platform)

The foundation of our approach to security is that we don't keep form submission data. Form submissions are held temporarily during validation, workflow & delivery, and then permanently deleted subject to the Data Retention Period for your account.

Form data can be accessed via our portal and API while it's temporarily held by us. To limit access during this time, we've made a change so that FormsByAir staff only have access to metadata (the Information page in the portal) by default. If staff do need access to form data, for example, to diagnose an issue, they must now request access for a specific document, which is then logged with a comment.

## 2021-08-02 — Conditional table row (platform)

We've updated our Word Document template engine to support conditional table rows using &lt;&lt;[Condition:Expression]&gt;&gt;

The Condition tag can be included in any cell but must only appear once per row.

If the expression evaluates to true, the Condition tag is removed and the row is preserved. If the expression evaluates to false then the entire row is removed.

This may be useful where you need to show/hide chunks of formatted content within a Word document.

## 2021-07-30 — ANZSIC (integration)

We've added an integration to search for ANZSIC codes by business activity.

## 2021-07-30 — MBIE entity types (integration)

We've updated our NZ MBIE integration as follows:

* Sole traders are now excluded from the default company search
* We're added a few additional filters to return registered societies, registered trusts, or all registered entities.

## 2021-07-28 — Staged sections (platform)

We've applied an update so that sections within a **Staged** form can now be configured to behave like they do in a non-staged form with a progress bar and Back/Next buttons.

This is useful where you need a *combination* of regular sections and stages within one form. For example, you may have a large form that needs to be split in to sections for the main form filler, but the final section for manager approval needs to be completed as a separate stage.

You can configure a section to proceed directly to the next section by setting **Next Stage Expression** to **true**. Any section where **Next Stage Expression** is left blank will be treated as a stage, with discrete submission.

You can also continue to set **Next Stage Expression** to a boolean expression. In this case, the form won't show a Next button or progress bar, but will still proceed directly to the next section if the expression evaluates to true.

## 2021-07-22 — Integration data models (platform)

We've added documentation for the data models returned by Lookup and Validation integrations

[FormsByAir Integration Models](https://formsbyair.com/swagger/ui/index?urls.primaryName=schema%2Fintegrations%2Fswagger.json)

## 2021-07-19 — Report purged documents (platform)

We made a previous change [here]({{ site.baseurl }}/changelog/#/2021/03/02/report-purged-documents) so that purged documents would be included in reports by default, and could be excluded with a conditional expression.

We've since determined that including purged documents is a special case that shouldn't be the default option, and doesn't need to be run on a recurring basis.

As such we've reverted the previous change so the option **Document report, sent daily** will now exclude purged documents.

We've added a new option **Document log (including purged), sent once** that will include purged documents, and only run once unless manually triggered again.

## 2021-07-15 — MBIE API update (integration)

We've updated our NZ Ministry of Business, Innovation and Employment lookup integration to use their latest v4 API, which includes more data for incorporated societies.

## 2021-07-14 — Connectivity (platform)

We've applied the following changes to better manage slow and intermittent internet connections when submitting forms

* Increased the browser connection timeout for form submissions containing file attachments
* Display a warning message on submit if no internet connection is detected

## 2021-07-09 — Block third party request on prefill (fix)

We've applied a change to block the generation of third party requests during prefill, as this is not required, and would result in documents with an invalid status.

## 2021-07-09 — Repeater title tags (fix)

We've updated repeaters that use &lt;&lt;tags&gt;&gt; for dynamic titles as follows:

* Blank titles will now default to the **Tag Name** of the repeater or the word "Item" along with the item number e.g. Person #1 or Item #1
* Labels for **Add** buttons will use the **Tag Name** of the repeater or the word "Item" instead of the title e.g. Add Person or Add Item

## 2021-07-08 — finPOWER Connect (integration)

We've added a new integration with [finPOWER Connect](https://www.intersoft.co.nz/Products/Product.aspx?product=finpowerconnect) to automatically populate client records from form submissions.

## 2021-07-05 — Escape angle brackets in text values (fix)

Angle brackets (&lt; and &gt;) in Text values will now be HTML-encoded for email and PDF output so that they are not interpreted as HTML tags.

## 2021-06-24 — Equifax (integration)

We've added an integration with [Equifax](https://www.equifax.co.nz/) for automated consumer credit checks in New Zealand.

## 2021-06-20 — Status page (platform)

We've migrated our status page to a new platform to provide both availability metrics as well as incident information, including the ability to subscribe for updates, see [https://status.formsbyair.com](https://status.formsbyair.com)

## 2021-06-19 — Multi stage requests (platform)

We've further extended [Mandatory third party requests for staged forms]({{ site.baseurl }}/changelog/#/2020/10/02/mandatory-third-party-requests-staged) to now support **multiple** stages with mandatory requests.

This may be useful where you need multiple sets of people to review or approve a document.

## 2021-06-15 — Sharepoint lists (platform)

We've updated our Sharepoint integration so we can now update existing list items, and attach files to list items.

## 2021-06-14 — Authorise comment (platform)

FormsByAir will now prompt for an optional comment when authorising a document in workflow.

## 2021-06-11 — Cloudcheck Live (integration)

We've updated our Cloudcheck Live integration to help improve the rate of successful verifications.

FormsByAir will now check the status of a facial match immediately after capture. If a match could not be made, users will be prompted to try again up to a total of 3 times, after which they can continue with the form either way.

## 2021-06-04 — Private download links (platform)

Updated private download links to support hash code matching on full URL or Hostname. See [Private download links]({{ site.baseurl }}/forms/private-download-links/)

## 2021-06-02 — Generate map for import (platform)

FormsByAir can now generate maps for import integrations based on the current version of a form.

Click **Generate Map** while editing an Import integration to generate and download a map that you can use as the basis of a custom map.

Alternatively, FormsByAir will generate a map automatically when you import a data file for an integration that doesn't have a map, effectively providing a straight match on JSON property names and Tag names.

## 2021-05-31 — Mandatory third party requests for staged forms (platform)

We've updated [Mandatory third party requests for staged forms]({{ site.baseurl }}/changelog/#/2020/10/02/mandatory-third-party-requests-staged) so the original document will now be set to **Requesting** status when we generate and send the third party requests. This will prevent the original form filler from accessing the document while waiting for the requests to be submitted.

## 2021-05-27 — Defer section validation (platform)

We've added a new setting to defer the validation of individual sections until a form is submitted. By default, sections are validated as you move to the next section.

This may be useful for very large forms where users can move ahead and complete as much as they can without being blocked by a few mandatory questions that they can answer later.

This is not recommended for any section that drives significant conditional content later in the form.

## 2021-05-25 — Document form version warning (platform)

FormsByAir will now display a warning with the form version that a document is based on if it's not the current version when viewing a document in the portal, this applies to users in the Administrator role only.

## 2021-05-21 — Edit last stage (platform)

FormsByAir portal users in the Operations role or higher can now edit the last submitted stage for saved (staged) documents, which may be useful to correct issues that prevent the form from moving forward.

## 2021-05-19 — Repeater custom function (platform)

You can now specify a custom JavaScript function as the **Default Value** (data source) for a repeater. This may be useful where you need to filter and combine data from multiple sources.

## 2021-05-18 — Document Workflow tags (platform)

We've genercised our document workflow system tags so you can now return all workflow details for any status.

See [System Tags]({{ site.baseurl }}/tags/system-tags)

## 2021-05-17 — Import with attachments (platform)

We've updated our API for **Import** integrations so you can now include file attachments using a multipart/form-data request

For more information see our [Swagger Documentation](https://formsbyair.com/swagger/ui/index#/Subscriptions/Subscriptions_ImportData)

Note - multipart/form-data requests are only supported when importing data for a *single* document.

## 2021-05-14 — Cliniko contact preferences (platform)

We've changed our Cliniko integration to *always* update contact preferences for existing patient records where provided. Previously we would only update these details if they were not set.

## 2021-05-12 — ReturnUrl (platform)

Added **ReturnUrl** form setting to override the account-level **Website Address** setting for redirection when closing a form.

This setting can itself be overriden using the ReturnUrl querystring parameter, see [System Parameters]({{ site.baseurl }}/forms/parameters)

## 2021-05-07 — Debug mode (platform)

We've added a new **Debug** option to the portal for form **Administrators**. Forms opened in debug mode will display validation messages by default, but not enforce them, allowing navigation throughout the form. Prefill-only content and hidden formulas will also be visible.

Forms can't be saved or submitted in debug mode.

## 2021-05-07 — Email delivery failure notifications (fix)

By default, FormsByAir will send email delivery failure notifications to:

* The Reply Email Address of the corresponding email integration if specified; or
* The Notification Email Address for the account; or
* All administrators for the account

If the email address we're sending a notification to matches the email address that failed, FormsByAir will now automatically escalate the recipient(s) to the next level.

We've also updated how email failures are represented in the portal. An email integration is marked as OK when successfully delivered to our email provider (SendGrid). If we subsequently receive a failure notification, which could be up to 48 hours later, the integration will now show with a CHECK status in the portal. This is in additon to the notification above. The integration will continue to be classified as "complete" in terms of setting the overall status of the document.

## 2021-05-07 — Prefill private forms (fix)

We've removed the option to **Prefill** forms in **Active/Private** status, as any request would only be available to the person that generated it, which defeats the purpose of a request.

## 2021-05-06 — Ignore empty rows on import (fix)

When importing a CSV or other delimited text file to a form, FormsByAir will now ignore rows where all fields in the row are blank (in addition to the existing check for completely blank rows)

Empty rows are sometimes included when editing and saving a CSV file with Microsoft Excel.

## 2021-05-06 — Save file integrations (platform)

File integrations with no conditional expression, or a conditional expression that only uses system tags, are now loaded when a form is saved, meaning they can be included as attachments for save emails.

## 2021-05-06 — Typeahead Data Array (platform)

Added **Data Array** source option to **Typeahead** questions.

## 2021-05-04 — Edit Workflow (platform)

**Workflow** elements in FormsByAir are the "for office use only" equivalent of traditional forms. Content contained within a Workflow element is hidden from form users, and only available when a document is in Workflow status.

By default, workflow content can be edited directly in the portal where it is flagged with a blue background.

However, the Document viewer only supports basic form functionality like Text and Option questions. If you have more advanced requirements for workflow data capture, FormsByAir now offers the ability to edit workflow content like a regular form.

To enable this option, change the **Format** setting for your Workflow element from Workflow to Form. Workflow content in the Document viewer is then read-only, and a new **Edit Workflow** button will appear at the bottom of the page. Edit Workflow is available for any user in the Workflow role or higher. The existing **Edit** button will also appear for Administrators and Supervisors to edit submitted form data.

After clicking Edit Workflow we'll open the document for edit, but only render the content within your Workflow element. The data model for the whole form is available, so workflow content can reference anything in the rest of the form with tags as normal.

When you Save Changes we'll update your workflow content and return to the document viewer.

## 2021-05-04 — Lookup array nested tags (fix)

**Lookup** questions now support nested tags in the **Data Array** setting, for example:

&lt;&lt;&lt;DataSource.Rows.filter(function(row) { return row.Something == &apos;&lt;&lt;Something&gt;&gt;&apos;})&gt;&gt;&gt;

## 2021-04-30 — System downloads (fix)

We've updated the manual **Download** document function in the portal to support *multiple* **System Download** File integrations. 

You've always been able to set the **System Download** flag on multiple File integrations, but FormsByAir would only return the first one. Now it will return all System Download files in a ZIP.

As before, if the document has client or server side attachments, these will be included in the ZIP. If there are no System Download File integrations configured then FormsByAir will return an auto-generated PDF with no attachments.

The intent behind the Download function remains the same in that it is a convenience feature for adhoc use. Any files you rely on should be delivered via other, automated channels.

## 2021-04-29 — Default repeater from repeater (platform)

You can now set the Default Value for a Repeater to use the contents of another repeater with syntax as follows:

&lt;&lt;[ForEach:RepeaterTag{Filter}]&gt;&gt;

This is useful where you need to edit and extend the contents of a previous repeater, perhaps in a subsequent form stage. Linked Repeaters are similar but don't allow you to independently add or remove items.

You can refer to content in the first repeater with tags like this &lt;&lt;SecondRepeater.TagNameOfElementInFirstRepeater&gt;&gt;

If the first repeater was populated from a data source, you can refer to that data with tags like this &lt;&lt;SecondRepeater.FirstRepeater.PropertyName&gt;&gt;

## 2021-04-28 — Option name (platform)

We've extended the functionality described [here]({{ site.baseurl }}/changelog/#/2020/07/15/boolean-option-tag-values) to support a Name property for **Option** questions as follows:

|Tag|State|Client result|Server result|
|---|---|---|---|
|&lt;&lt;Option.Name&gt;&gt;|Selected|Question Title|Question Title|
|&lt;&lt;Option.Name&gt;&gt;|Not Selected|&lt;blank&gt;|&lt;blank&gt;|
|&lt;&lt;Option.Value&gt;&gt;|Selected|true|true|
|&lt;&lt;Option.Value&gt;&gt;|Not Selected|false|false|
|&lt;&lt;Option&gt;&gt;|Selected|true|Question Title|
|&lt;&lt;Option&gt;&gt;|Not Selected|false|&lt;blank&gt;|

## 2021-04-28 — Salesforce update (integration)

Our Salesforce integration now supports *updating* existing records in addition to adding new records.

## 2021-04-27 — Workflow Deauthorise (platform)

You can now **Deauthorise** a document that has been authorised by selecting Options > Deauthorise in workflow.

This will move the document back to **Pending** status so it can be edited or returned to the form filler. It will also be re-assigned to either the user that requested authorisation (if any), or the user that authorised it.

The document will need to be re-authorised before it can be approved.

## 2021-04-14 — Form log (platform)

We've changed the Form > Action > **Submissions** menu option in the portal to Form > Action > **Log**, and updated the corresponding page to display *all* documents for the selected form instead of only those that have been submitted.

## 2021-04-14 — Saved documents (fix)

We've updated the Documents > Saved page in the portal to display *all* saved documents for users in the **Workflow** role or higher. 

Previously it would filter out any documents that had been saved by a different FormsByAir user. This behaviour now only applies to users in the **User** role.

## 2021-04-12 — Saved Section (platform)

FormsByAir will now capture and display the last Section that forms were saved at to provide more visibility on progression through larger forms.

This information is available in the portal when viewing a list of saved documents, or as part of the event log for an individual document, which is similar to the existing behaviour for forms using Staged Submission.

## 2021-04-07 — Date validation (fix)

FormsByAir will now enforce a minimum date of 1/1/1111 for **all** Date questions unless overridden with a custom Minimum Value. For example, the *Date Of Birth* shortcut will add a Date question with a Minimum Value of 1/1/1900.

## 2021-04-07 — Generate missing tags (platform)

We've added a new form-level setting **Auto generate missing tags on save design** which is *disabled* by default.

When enabled, FormsByAir will automatically generate tag names (based on Title) for all questions that don't have a tag when you save the form.

This is useful if you're planning to include **all** form data in a data integration, for example, an auto generated JSON file.

## 2021-04-07 — JSON system properties (platform)

FormsByAir will now include the following system properties in auto generated (non-mapped) JSON for all output types including File, Webhook and Azure CosmosDB.

|Property|Equivalent to|
|---|---|
|_DocumentId|&lt;&lt;[DocumentId]&gt;&gt;|
|_DocumentFormName|&lt;&lt;[DocumentFormName]&gt;&gt;|
|_DocumentOwnerName|&lt;&lt;[DocumentOwnerName]&gt;&gt;|

If you're generating *custom* JSON you can reference [System Tags]({{ site.baseurl }}/tags/system-tags) directly in your map.

## 2021-04-01 — SubmitUrl Redirection (fix)

We've applied an update so that redirection to a SubmitURL does *not* apply to third party requests, as this can interfere with form analytics, and the messaging for custom submission pages is generally targetted at the *main* form filler.

## 2021-03-31 — Expire on close (platform)

**Requested** and **Saved** documents normally expire on a rolling basis as follows:

* 30 days (or as configured for form) after request was generated; or
* 30 days after last save

We've applied an update so that forms with a fixed **Close Date/Time** will now override this behaviour and requested/saved documents will remain active up until the form closes.

## 2021-03-29 — Prefill Staged forms (platform)

We've updated **Staged** forms so you can now specify where the form should start while generating a request.

This means you can hide earlier stages in a form where that information has already been collected or is not required.

## 2021-03-25 — Test (Public) form status (platform)

Added new form status **Test (Public)**

Forms set to this status can be opened by anyone. A warning will be displayed at the top of the page "This form is available for testing only", and all integrations will use **Test** credentials.

See [Form Status]({{ site.baseurl }}/forms/status)

## 2021-03-02 — Report purged documents (platform)

We've updated **Report** integrations so they will now include purged documents by default.

&lt;&lt;[Document]&gt;&gt; tags in report templates will return data for *all* documents, but tags referring to form data will only be populated for documents that haven't been purged.

Purged documents can be excluded from reports by adding the following condition to your report integration: &apos;&lt;&lt;[DocumentPurgedDateTime]&gt;&gt;&apos; == &apos;&apos;

## 2021-02-28 — Expression evaluation (platform)

Replaced Javascript eval() statements with Function("use strict") to improve the performance and security of expression evaluation in forms.

## 2021-02-26 — Third Party Request reminders (platform)

Added support for Third Party Request reminder emails, which are useful in combination with [mandatory third party requests]({{ site.baseurl }}/changelog/#/2020/10/02/mandatory-third-party-requests-staged)

## 2021-02-22 — Filter Typeahead table data (platform)

You can now specify a Filter expression for Typeahead questions that use a FormsByAir data table, which was already possible with Lookups.

## 2021-02-15 — Batch integration processing (platform)

We've improved the user experience and information in the portal for **Import** and **Report** integrations as follows:

* The portal will now display a PROCESSING status next to an integration while it is actively running, and prevent further execution until the current process has completed
* If a process completes successfully the PROCESSING status will be removed
* You can view a log of previous executions by clicking Action > Log against an integration
* If a process fails the portal will display a CHECK status next to the integration, which you can click to display the log and associated error message
* A CHECK status will remain in place until the next successful execution, or the integration is disabled

## 2021-02-08 — SuiteCRM integration (integration)

Added new integration with [SuiteCRM](https://suitecrm.com/) to add records for any module using form data.

## 2021-02-05 — Lookup/Validation mapping (platform)

Mapping files for **Lookup** and **Validation** integrations now support multiple criteria groups when used with FormsByAir or CosmosDB data tables.

This allows you to query data where (Condition1 AND Condition2) OR (Condition3) for example.

## 2021-02-01 — Slider precision (platform)

Sliders have been updated to support **Step** values of less than 1, so a slider with Min 0 Max 10 Step 0.5 will have 21 possible values e.g. 3.5

## 2021-01-26 — Form size limit (platform)

We've increased the total size limit for a form submission from 100MB to 200MB to allow for many, large attachments.

The maximum size for any single file attachment remains at 20MB.

## 2021-01-25 — Existing document version check (platform)

FormsByAir will now check the version of existing documents when saving or submitting. If a user attempts to save or submit a document that has been updated outside of their current browser window they'll receive a warning message instructing them to *Reload* to get the latest version. FormsByAir will continue to display an error message if the document has already been submitted.

This may occur where:

* A request is updated in our portal (e.g. to correct a mistake) while the user has the form open in their browser
* An existing document is opened in multiple windows or on multiple devices at the same time

## 2021-01-21 — ElementAt (platform)

Added tag function to return output for an item with specified index from a filtered repeater, see [ElementAt]({{ site.baseurl }}/tags/functions/elementat)

## 2021-01-19 — Validate prefill-only sections (platform)

Form validation for Required fields in **Prefill Only** sections will now be enforced during prefill, previously this could be ignored.

## 2021-01-12 — Email delivery failure notifications (platform)

Email delivery failure notifications will now be sent to the **Reply Email Address** of the corresponding email integration if specified, otherwise they will default to the **Notification Email Address** for the account as before.

This effectively allows customisation of bounce notifications at the form and individual email level.

## 2021-01-11 — Mobile phone validation (platform)

Added new option to validate **mobile** phone numbers (as opposed to fixed line) which may be useful where the number will be used to send a TXT/SMS, see [Phone]({{ site.baseurl }}/questions/types/phone)

## 2021-01-07 — Private download links (platform)

Added the ability to authenticate access to private online resources e.g. files stored in a private Amazon S3 bucket, see [Private download links]({{ site.baseurl }}/forms/private-download-links)

## 2021-01-05 — Autocomplete (platform)

Added Autocomplete property for Text, Email &amp; Phone questions, see [Autocomplete]({{ site.baseurl }}/questions/properties/autocomplete)

## 2021-01-05 — Nested tags in Javascript (platform)

Nested tags are now supported in client-side javascript expressions using the number of &lt;&lt;&gt;&gt;'s to indicate depth.

This is particuarly useful for array functions with JSON data from a Data Source element, for example:

&lt;&lt;&lt;CustomerData.Orders.filter(function(order) { return &apos;&lt;&lt;SelectedProductCode&gt;&gt;&apos;.indexOf(order.ProductCodes) >= 0 })[0].ProductCode&gt;&gt;&gt;

The outer tag for CustomerData has 3 &lt;&lt;&lt;&gt;&gt;&gt;'s whereas the inner tag for SelectedProductCode has 2 &lt;&lt;&gt;&gt;'s;

## 2020-12-23 — Delivery validation (platform)

Added validation to ensure that at least one delivery integration has been queued and processed *after* a form was last submitted to help identify any "gaps" in conditional integrations.

## 2020-12-21 — Addy integration (platform)

Added new integration with [Addy](https://www.addy.co.nz/) for NZ address lookup.

## 2020-12-07 — Document Delivery filter (platform)

Added the ability to filter documents by **Delivery** date in the Document Status page. This represents the number of documents that were approved (if workflow is enabled) and *delivered* within a given time period, which can be different to the number of documents *received* in the same period.

## 2020-12-03 — UAT/Test Labels (platform)

Changed all "UAT" labels in the system to "Test" for consistency and to avoid confusion.

## 2020-11-30 — Trello integration (platform)

Added new integration with [Trello](https://trello.com/) to add cards to lists using form data.

## 2020-11-27 — Data Retention Period (platform)

We've reduced the default and recommended Data Retention Period from 20 days to 10 days. This does not affect existing accounts, which can be manually updated at any time via the FormsByAir portal.

## 2020-11-27 — System Tags (platform)

Added support for parsing [System Tags]({{ site.baseurl }}/tags/system-tags) in Excel templates.

Added new system tag &lt;&lt;[DocumentBatchReference]&gt;&gt;

## 2020-11-26 — Flatten JSON output (platform)

Added option to **flatten** auto-generated (non-mapped) JSON output to exclude section and group elements.

## 2020-11-23 — System Tags (platform)

Added support for parsing the system tag &lt;&lt;[DocumentId]&gt;&gt; within a form. All other system tags are currently server-side only.

## 2020-11-20 — Workflow Block Approval (platform)

Added **Block Approval** option for workflow elements.

The intent is for this to be used in conjunction with conditional paths to block the approval of submissions in certain situations. e.g. where a form user has indicated that they want to query something before proceeding.

When this happens, the **Approve** action in workflow will be unavailable, with **Return** taking it's place as the default action.

A form administrator can address the query and/or edit the form, then Return it to the user to re-submit, such that the approval-blocking workflow element is no longer active.

## 2020-11-19 — Cancel file attachment (platform)

Added the ability to *cancel* a file attachment after selection of a file in a form. A user can then select another file, or leave the question empty if it's not mandatory.

## 2020-11-17 — Nested Systems Tags (platform)

Added the ability to nest system tags within the Condition tag using the number of &lt;&lt;&gt;&gt;'s to indicate depth, for example:

&lt;&lt;&lt;[Condition:&apos;&lt;&lt;[ForEach:Contact{&apos;&lt;&lt;ContactAccept&gt;&gt;&apos; != &apos;Accept&apos;}:&lt;&lt;ContactAccept&gt;&gt;]&gt;&gt;&apos; == &apos;&apos;:&apos;Accept&apos;]&gt;&gt;&gt;

The outer Condition tag has 3 &lt;&lt;&lt;&gt;&gt;&gt;'s whereas the inner ForEach tag has 2 &lt;&lt;&gt;&gt;

This only applies to server-side Condition tags with 2 levels of depth for now, we're looking to extend this syntax to all other system tags with additional levels of depth in future.

## 2020-11-09 — Merged Copy and Copy To (platform)

We've merged the **Copy** and **Copy To** form actions in the portal to avoid confusion. When you select **Copy** you can now choose to create a *new* form or update an *existing* form, in either the current account or another partner account.

## 2020-11-02 — Azure Front Door Network Upgrade (platform)

In order to scale the performance of our platform and keep pace with security threats, we are moving all public FormsByAir endpoints from Azure Application Gateways to Azure Front Door. Front Door provides a CDN (Content Distribution Network) for static content at 130 POPs around the world and an advanced WAF (Web Application Firewall) to help mitigate attacks including DDoS. In addition, we are taking this opportunity to increase our minimum TLS version from 1.1 to 1.2.

The upgrade to TLS 1.2 means that very old browsers like Internet Explorer 9 or lower may not be able to connect to FormsByAir, but this represents less than 0.4% of global web traffic based on current statistics.

All forms hosted on *.formsbyair.com are now running with Front Door and TLS 1.2.

All forms hosted on a custom domain are being migrated in consultation with each client/partner.

formsbyair.com (which includes our portal and API) will be migrated once all partner endpoints have been migrated.

## 2020-10-02 — Mandatory third party requests for staged forms (platform)

We've made the following changes for **Mandatory Third Party [Requests]({{ site.baseurl }}/forms/elements/request)** located in the last stage of forms configured for **Staged** submission.

* FormsByAir will automatically generate the requests on submit of the second-to-last stage. This ensures the requests are sent directly to the third parties. The main form filler has no ability to access or cancel the requests, they can only view the status of them.
* Submission of the *last* request will automatically trigger submission of the main form

Combined, these features are useful where a form request for an existing group of people is sent to a primary contact for general completion, but must be viewed/authorised by *all* parties.

## 2020-09-26 — Next Stage Expression (platform)

When a form is configured for **Staged** submission, each submit will cause the form to either enter workflow for review, or revert to saved status for someone else to complete the next stage.

**Next Stage Expression** provides a mechanism to conditionally progress directly to the next stage where the expression evaluates to true.

## 2020-09-23 — Repeater Read-Only options (platform)

Added new Read-Only options for Repeaters that are populated with a Default Value

|Option|Repeater behaviour|
|---|---|
|None|Can add new rows, remove any row|
|Defaults|Can add/remove *new* rows only|
|All|Can't add or remove rows|

## 2020-09-11 — Workflow Assignment Changes (platform)

#### Authorisation Assignment Expression

If this expression is left blank or evaluates to an empty string, documents can now be authorised directly by the current workflow user. 

Previously, documents with no authorisation assignment would require authorisation by the *manager* of the current workflow user. This can be replicated by setting **Authorisation Assignment Expression** to &apos;&lt;&lt;[DocumentWorkflowUserManagerEmail]&gt;&gt;&apos;

#### Assign document to form user's manager for approval

This workflow option has been removed. It can be replicated by setting **Assignment Expression** to &apos;&lt;&lt;[DocumentUserManagerEmail]&gt;&gt;&apos;

## 2020-08-21 — Authorisation Bypass (platform)

Added the ability to specify an **Authorisation Bypass Expression** where *Requires Authorisation* is enabled for a form.

If this expression evaluates to True then a submitted document will skip Authorisation and only require Approval in workflow.

## 2020-08-09 — Scroll anchoring (fix)

Several web browsers including Chrome, Edge and Firefox have recently enabled scroll anchoring by default, a feature that automatically adjusts scroll position to compensate for dynamically added content.

This was conflicting with our functionality to scroll newly added repeater items in to view, making it appear that an item had not been added.

As such we've disabled scroll anchoring by adding the following style tag to the body element of our forms: overflow-anchor: none;

## 2020-08-07 — Hide first third party request (feature)

Added new option **Hide First** for Third Party [Requests]({{ site.baseurl }}/forms/elements/request)

When enabled on a Request element within a repeater, FormsByAir will hide the prompt to create a request for the *first* repeater item.

This may help to avoid confusion with forms that require completion by multiple people, where the first person is generally the main form filler (so a request is not required for them)

## 2020-07-31 — Login IP Address Whitelist (platform)

To further enhance security, FormsByAir now supports IP Address Whitelisting for login to the portal and private forms.

This is particularly useful for large clients that operate on a corporate network and wish to restrict access to FormsByAir from that network only.

To enable, log in to the FormsByAir portal, go to Settings &gt; Profile and enter one or more IP addresses for **Login IP Address Whitelist**, then Save Changes.

All login attempts from that point forward will be checked against the whitelist. If a user's IP address doesn't match they won't be able to log in.

This feature can be used in conjunction with **Two Factor Authentication** for strict access control over form data that we (temporarily) hold.

Login IP Address Whitelisting does not apply to API Key access.

Users that are already logged in and subsequently switch to a different network will remain logged in.

## 2020-07-27 — Repeater Minimum Rows expression (platform)

You can now specify an *expression* for the **Minimum Rows** property of repeaters, previously you could only use a fixed value. **Maximum Rows** has always allowed a fixed value or expression.

When using a minimum, FormsByAir will pre-load empty rows, and prevent the user from removing rows when at the minimum.

FormsByAir will evaluate an expression for Minimum Rows when a form, section, or conditional path containing the repeater is loaded.

## 2020-07-23 — Default values in conditional paths (platform)

FormsByAir will now evaluate default values within a conditional path every time the path is activated. Previously they would only be evaluated on form or section load.

## 2020-07-23 — Repeater element data changes (platform)

FormsByAir will now add/remove repeater elements in response to changes in an underlying data source, preserving manually entered data for elements that are still part of the data set.

Previously we would clear and reload all elements, removing manually entered data.

## 2020-07-20 — Portal links after login redirect (fix)

FormsByAir will now correctly navigate to links within the portal if redirected to login first.

## 2020-07-15 — Boolean/Option Tag Values (platform)

Tags for **True/False** and **Option** type questions are evaluated as follows:

|Tag|Client result|Server result|
|---|---|---|
|&lt;&lt;MyTrueFalseQuestion&gt;&gt;|true or false|Yes or No|
|&lt;&lt;MyOption&gt;&gt;|true or false|Question Title or &lt;blank&gt;|

The intent is to display a user-friendly value by default, however this can lead to confusion when you want to use these tags in expressions.

To make it more explicit, you can now include the **Value** tag property to refer to the underlying value for true/false or option questions.

|Expression with Value property (outside of a form)|Equivalent to|
|---|---|
|&apos;&lt;&lt;MyTrueFalseQuestion.Value&gt;&gt;&apos; == &apos;true&apos;|&apos;&lt;&lt;MyTrueFalseQuestion&gt;&gt;&apos; == &apos;Yes&apos;|
|&apos;&lt;&lt;MyOption.Value&gt;&gt;&apos; == &apos;true&apos;|&apos;&lt;&lt;MyOption&gt;&gt;&apos; != &apos;&apos;|

## 2020-07-14 — Expressions in Word templates (fix)

When typing expressions in to Word templates, single quote marks (&apos;) are rendered as "curly" opening and closing quotes (&lsquo;&rsquo;), for example:

&lt;&lt;[Expression:&lsquo;Type&rsquo; == &lsquo;Custom&rsquo; ? &lsquo;Custom text&rsquo; : &lsquo;Standard text&rsquo;]&gt;&gt;

This has previously caused errors with expression evaluation, requiring templates to be updated, usually by copying unformatted text from a text editor like Notepad.

FormsByAir will now automatically convert curly quotes to regular quotes during evaluation, so expressions can be entered directly in Word without issue.

## 2020-06-24 — APLY integration (platform)

Added new integration with [APLY](https://www.aplyid.com/) for AML identity verification services.

## 2020-06-23 — Two Factor Authentication (platform)

For enhanced security, FormsByAir now supports Two Factor Authentication using the Google Authenticator app (available for iOS and Android)

Users can setup Two Factor Authentication as follows...

* Log in to the FormsByAir portal
* Click the button top-right and select **Change Password**
* Click the button **Setup Two Factor Authentication** and follow the instructions

Once enabled, users will be prompted for an additional verification code (provided by the app) when they log in.

Users with Two Factor Authentication enabled are tagged **2FA** in the **Manage Users** section of the portal.

We recommend that all users in the Administrator role enable Two Factor Authentication.

## 2020-06-17 — Form designer updates (platform)

In order to improve performance and navigation when editing large forms, FormsByAir will now load section content on-demand, and only expand one section at a time by default.

This means that elements within each section will not be loaded until you click on them. You may notice the loading indicator appear while this is happening. Once loaded, sections will remain cached, but only one section will expand and display at a time.

A new button "Expand all sections" is available to load and display all sections at the same time if required.

This does not impact forms that don't use sections.

The form designer will also now validate items within an **Option List** or **Option Name/Value List** to ensure they are unique.

## 2020-06-10 — Custom width for image tags (platform)

You can now specify a custom width for **Signature** and **Diagram** tags in Word document templates.

For example &lt;&lt;Signature&#124;150&gt;&gt; or &lt;&lt;Diagram&#124;300&gt;&gt;

Height will be calculated automatically to maintain the same aspect ratio.

## 2020-06-02 — Preserve JSON data values (fix)

FormsByAir had previously "flattened" JSON values for **Data Source**, **Lookup** and **Typeahead** elements to the Name property only when merging third party requests or returning a document.

This meant any subsequent reference to properties within tags e.g. &lt;&lt;Country.Code&gt;&gt; would return an empty string.

JSON values are now never flattened.

## 2020-05-28 — Save signature/diagram on resize (fix)

FormsByAir will now save an active **Signature** or **Diagram** if the browser window is resized during edit to prevent image scaling issues.

## 2020-05-27 — Repeater title tags (platform)

Repeaters using the **Auto** format option would previously display values for the first several elements within each repeater alongside the title when collapsed.

This was useful for previewing and differenting data for multiple, collapsed repeaters, but there was no control over which values should appear.

This "auto preview" feature has been removed. You can now use tags in the Title property of a repeater to refer to specific child elements (within each repeater) and parent elements.

## 2020-05-25 — Condition system tag (platform)

Added new **Condition** system tag with usage as follows:

&lt;&lt;[Condition:{condition}:{output if condition is true}]&gt;&gt;

For example: 

&lt;&lt;[Condition:&apos;&lt;&lt;Description&gt;&gt;&apos; != &apos;&apos;:Description &lt;&lt;Description&gt;&gt;]&gt;&gt;

This is useful where the ouput contains formatting including new-line characters.

A similar result can be achieved with an **Expression** system tag and a conditional operator, for example:

&lt;&lt;[Expression:&apos;&lt;&lt;Description&gt;&gt;&apos; != &apos;&apos; ? &apos;Description &lt;&lt;Description&gt;&gt;&apos; : &apos;&apos;]&gt;&gt;

However in this case the whole expression is **evaluated**, so new-line and other characters are removed.

## 2020-05-21 — Validation retry timeout (platform)

The retry timeout for outages of Delivery Channels used in validation has been reduced from 60 to 30 minutes.

## 2020-05-20 — Return Third Party Requests (platform)

You can now **Return** a submitted Third Party Request where the requesting form is either **Saved** or in **Workflow** pre-authorisation.

This is particularly useful where third party requests include post-submit validation, which is only processed when the main requesting form is submitted.

When a third party request is re-submitted, and the main form is in workflow, the main form will automatically revalidate the data for that particular request.

Requests can be returned multiple times if required.

## 2020-05-01 — Open Request-Only forms to prefill (fix)

For non-administrators: Clicking the title of a form in the portal with Access Mode **Request Only** will now open the form in prefill mode instead of returning a 404 Not Found error.

## 2020-04-28 — Azure AD Private Form Authentication (feature)

Added Microsoft Azure Active Directory option for **Private Form Authentication** in Settings &gt; Profile.

This allows users with a Microsoft organizational account in a specific tenant to access private forms without a FormsByAir user account. It does not allow access to the FormsByAir portal.

Azure AD logins are session based.

If the Azure AD account matches a FormsByAir user account, form submissions are tagged to the FormsByAir user. This is relevant where you want to block users from approving their own submissions (using the **Block Same User** workflow option)

If the Azure AD account does *not* match to a FormsByAir user account, form submissions are not tagged to a user.

## 2020-04-17 — Block Same User workflow option (feature)

Added new form-level workflow option to prevent a FormsByAir user from actioning workflow on a document they've submitted.

Users in the Workflow role or higher, including Administrators, can only **view** and **comment** on their own documents.

## 2020-04-16 — Document Access List (feature)

Added new form-level option to specify a list of FormsByAir users that can access documents (saves/requests/submissions) for a form.

If this is blank (the default), all FormsByAir users in the Workflow role or higher can access documents for the form.

If you specify a list of users, documents will be omitted from all portal views and access via direct link blocked for all users that are *not* in the Document Access List.

This is useful where you need to limit access and workflow actions for sensitive documents to a subset of your users.

This does *not* apply to Administrators, who can access all documents.

## 2020-04-15 — Autocapitlize Words iOS (fix)

Removed the HTML5 tag autocapitalize="words" when using the **Title Case** Format for Text questions due to inconsistent behaviour on iOS devices, which is yet to be [resolved by Apple](https://forums.developer.apple.com/thread/18634)

Title Case text is now capitalized correctly on all devices using our own script.

autocapitalize="characters" continues to be used with the **Upper Case** Format, which behaves correctly on all devices.

## 2020-04-14 — Decline Authorisation (feature)

Changed the behaviour of **Decline** during Authorisation to revert the document to pending status and assign it to the person that requested authorisation, rather than *Deleting* the document.

Also added the ability to specify a comment when you Decline a document at any stage.

## 2020-04-13 — Delivery links (feature)

FormsByAir will now store the absolute URL for a record or file that we've created or updated in an external system.

Delivery References on the Document Information page will now appear as hyperlinks where this is available.

In addition, you can access delivery links using the new system tag &lt;&lt;[DocumentDeliveryLink]&gt;&gt; which can be used to include links in email notifications.

## 2020-04-07 — Fillable PDF Flattened (feature)

Added new **PDF From Fillable PDF Flattened** file format option to flatten a fillable PDF after populating it so that form fields can't be edited further.

## 2020-04-06 — Staged Submission without workflow (feature)

Staged Submission is now supported for forms that don't use workflow. This may be helpful for forms that require progressive review and completion by multiple external users.

When a stage is submitted, the document will advance to the next stage and revert to **Saved** status. Emails can be triggered at each stage to notify the relevant party to access the document and complete their stage.

## 2020-04-05 — Validate Signature size (feature)

FormsByAir will now check the size of a signature image and display a validation error if it's too small e.g. a single dot

## 2020-03-31 — Data Source table (feature)

Data Source elements can now reference a Data Table instead of a Data Service. This may be useful where you need to lookup data from a table and filter it using other data in the form.

## 2020-03-10 — Server side tag properties (feature)

FormsByAir will now evaluate **properties** in server-side tags to be consistent with client-side (in-form) evaluation.

For example, you may now refer to a Data Source or Lookup element with &lt;&lt;Product.Name&gt;&gt; in a data integration map.

Previously you would have had to create a hidden formula element with expression '&lt;&lt;Product.Name&gt;&gt;' and refer to that element in your data integration map.

## 2020-03-08 — Account level style (feature)

You can now apply CSS style attributes to **all** of your forms at the account level in Settings &gt; Profile.

You can still apply CSS style attributes to individual forms at Action &gt; Design &gt; Style tab.

## 2020-03-08 — Save link messaging (feature)

We've improved the messaging for forms that *don't* have an **On Save** email to make it more obvious that users must copy or share the unique link before they close the page, otherwise they won't be able to access their saved form.

## 2020-03-04 — Email BCC (feature)

You can now specify BCC recipients for email integrations in addition the main recipients, and CC recipients.

## 2020-03-03 — Previous versions (feature)

You can now view previous versions of a document (before an edit) from the Document Information page.

## 2020-03-02 — GET Document API format (feature)

Added new **Data** format option to [GET /api/v1/Documents/{id}](https://formsbyair.com/swagger/ui/index#/Documents/Documents_GetDocument)

This returns a document object with minimal schema information (compared to the **Form** format option)

This may be useful where you need to directly edit document data in an external system without rendering the form.

## 2020-02-28 — Import from JSON (feature)

You can now import data from a JSON file in to a form request using a data map.

## 2020-02-27 — REST API Lookup (fix)

Fixed REST API lookup to return the same data type as the source API i.e. an object, or an array.

## 2020-02-24 — Data service parameters (feature)

Added new **Parameters** property for Data Service elements to pass form data to a service instead of querystring values.

Parameters are defined in querystring syntax, and can reference form data with &lt;&lt;tags&gt;&gt;, for example:

category=&lt;&lt;Category&gt;&gt;&amount=&lt;&lt;Amount&gt;&gt;

You can reference these parameters in a REST API integration endpoint as follows:

https://sampleservice/api/v1/categories/{category}/products?amount={amount}

## 2020-02-22 — Object tag value (feature)

FormsByAir will now return the value of the Display property for tags that reference an object within a form, and don't specify a property.

For example, if you had a Typeahead based on the Country system table, you would need to use &lt;&lt;Country.Name&gt;&gt; to return the name of the selected country, &lt;&lt;Country&gt;&gt; on it's own would return [object Object]

Now &lt;&lt;Country&gt;&gt; will return the value of the Name property, consistent with server-side tag evaluation.

## 2020-02-22 — Search saved documents (feature)

Added the ability to search saved documents by reference.

## 2020-02-20 — Mandatory third party requests (feature)

Third party request elements can now be flagged as **Required** meaning a request must be generated for someone else to complete that part of the form. All elements within the request are read-only for the main form filler.

This is useful where third parties are required to check existing information and update it, or provide consent.

## 2020-02-17 — Inline dropdown placeholder text (platform)

Updated the default placeholder text for inline dropdown lists to "Select XXX..." to differentiate it from actual list items.

## 2020-02-16 — Log conditional expression errors (fix)

FormsByAir will now write an integration record and log an error against it when evaluation of a conditional expression fails, making it more obvious that a problem exists, and requires attention.

## 2020-02-08 — Ignore attachments for excluded elements (fix)

FormsByAir will now ignore attachments for elements that have been excluded from file-based integrations in the Exclusion List.

## 2020-01-21 — Salesforce attachments (platform)

Updated Salesforce integration to attach files via the ContentVersion object instead of Attachment to ensure compatibility with Lightning Experience.

## 2020-01-20 — Save & Prefill (platform)

We've updated the Save & Prefill actions to be easier to use, and consistent with third party requests.

* The unique form link that we generate is now hidden to avoid confusion
* **Share** allows you to quickly share the form link via the Share panel on iOS and Android, or in a new email
* **Copy Link** copies the form link to the clipboard

## 2020-01-17 — Staged submissions in workflow (fix)

Forms configured for staged submission will now remain in workflow view between stage approval and the next submission.

## 2020-01-15 — Document Form Version Tag (feature)

Added Document Form Version tag

Useful where you need to make integrations conditional on form version

See [System Tags]({{ site.baseurl }}/tags/system-tags)

## 2020-01-15 — Email editor encoding expression operators (fix)

Fixed an issue where the *and* operator (&&) within expressions was being HTML-encoded by the email template editor, causing expression evaluation to fail.

## 2020-01-13 — Third party requests (platform)

We've updated third party requests to make them easier to use.

* The unique request link that we generate is now hidden to avoid confusion
* **Share** allows you to quickly share the request link via the Share panel on iOS and Android, or in a new email
* **Copy Link** copies the request link to the clipboard
* The date/time that a request was generated is now displayed
* Added instruction to save the form and wait for a request to be completed

## 2020-01-10 — Integration priority (feature)

You can now specify a **Priority** for delivery integrations such that all integrations with a higher priority will always be completed first.

This can be used in conjunction with the Document Delivery Reference tag, where a delivery reference from one integration is required for a subsequent integration - or where a particular integration should only be executed once all other integrations have been completed.

## 2020-01-10 — Save form messaging (platform)

The confirmation message that appears when you **Save** a form has been updated to advise that you can continue to make changes and save again or submit, it is also hidden automatically when/if further changes are made.

The option to automatically display a saved form when you open the corresponding blank form has been removed. This was rarely used, and represented an unnecessary security risk.

## 2019-12-30 — Incomplete request validation (feature)

FormsByAir will now show a validation message for incomplete requests advising users to save and wait for the requests to be completed if they attempt to move to the next section or submit.

## 2019-12-30 — Lock form on submit (feature)

Form content is now *locked* for edit once a form has been submitted to avoid any confusion around making further changes.

You can optionally *hide* form content using the form setting **Hide form after submit**

## 2019-12-20 — File Number tag (feature)

Added File Number tag to return a sequential number for a file attachment, for use with the Filename Format property.

See [System Tags]({{ site.baseurl }}/tags/system-tags) and [Filename Format]({{ site.baseurl }}/questions/properties/filename-format)

## 2019-12-17 — JSON File Formats (feature)

Added **JSON** & **JSON From Map** file formats.

See [File Integrations]({{ site.baseurl }}/integrations/file)

## 2019-12-11 — Document Delivery Reference tag (feature)

Added Document Delivery Reference tag to return the last successful delivery reference for a given subscription. Useful where the delivery reference from one integration needs to be included in another integration.

See [System Tags]({{ site.baseurl }}/tags/system-tags)

## 2019-12-09 — Azure Cosmos DB (feature)

Added read/write integration with [Azure Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/)

Cosmos is Microsoft's premiere NoSQL database service with global scale, high availability, and native encryption.

Our integration allows you and/or your clients to securely interact with data in your own Azure account.

## 2019-12-09 — Open documents from log (feature)

Added the ability to open **Saved** and **Requested** documents directly from the Log.

## 2019-11-28 — Time question (feature)

Added new Time question to capture and validate a time of day in 12 or 24 hour format.

See [Time]({{ site.baseurl }}/questions/types/time)

## 2019-11-25 — Document Form Name tag (feature)

Added Document Form Name tag

See [System Tags]({{ site.baseurl }}/tags/system-tags)

## 2019-11-21 — Address Picker country tag (feature)

You can now use a tag value for Country Code with an Address Picker to *dynamically* filter addresses to a given country. You could previously only set a static Country Code as part of the form design.

## 2019-11-15 — Email Attachment form attachments (fix)

**Email Attachment** integrations now include form attachment files, consistent with storage provider integrations.

## 2019-11-14 — CSV & Text From Template data formatting (fix)

FormsByAir will no longer format form data in **CSV From Template** and **Text From Template** integrations, as these generally need to be machine rather than human readable files.

Note - Form data was already unformatted in *Batch* CSV and Text files, the change applies to files generated for individual submissions.

## 2019-11-09 — Kiosk Mode per form (platform)

You can now enable Kiosk Mode per form in addition to per device, which is useful for forms that will only be used on-premise. For example, an in-clinic patient consent form.

See [Access Mode]({{ site.baseurl }}/forms/settings/access-mode)

## 2019-11-07 — Bambora integration (platform)

Added new integration with [Bambora](https://www.bambora.com/) for card payments in North America.

## 2019-11-07 — Monday integration (platform)

Added new integration with [Monday](https://monday.com/) - Sales CRM & Project Management Software.

## 2019-11-04 — Email & Phone Number Validation (platform)

Email domain validation messages have previously been displayed as passive warnings, which enabled users to continue if the validation of their domain was incorrect, but it also meant that many legitimate warnings were ignored.

In order to further improve data quality and minimize email bouncebacks, email validation messages will now appear as errors that must be resolved or dismissed by clicking "Ignore".

We have applied similar validation to phone numbers where **Format** is set to International. A validation error will be displayed if the number is invalid for a given Country, which must be resolved or dismissed by clicking "Ignore".

## 2019-11-01 — XML From Template data formatting (fix)

FormsByAir will no longer format form data in **XML From Template** integrations, as these generally need to be machine rather than human readable files.

## 2019-10-28 — Data Retention Period & Region Settings (feature)

Data Retention Period & Region (Country) have always been in the platform, but you can now self-configure these via Settings > Profile at the account level.

## 2019-10-28 — Filename format tag (feature)

You can now use the tag of an attachment element in the **Filename Format** property to refer to the original filename of the attachment.

See [Filename Format]({{ site.baseurl }}/questions/properties/filename-format)

## 2019-10-28 — Pipes in attachment filenames (fix)

FormsByAir will now replace the pipe (\|) character with an underscore (_) if present in attachment filenames on Mac OSX and iOS.

## 2019-10-26 — Wider Question text for Inline Options (feature)

FormsByAir will now adjust the width of question text for **Inline Radio** and **Inline Toggle** Option questions based on the Width specified for the options.

For example, if the options are Yes and No and you set a Width of 2, the question text will occupy 10 columns. Question text is normally restricted to 4 columns.

This is useful for survey-type questions with larger descriptions, and a small set of available options or scores.

## 2019-10-22 — Slashes in expressions (fix)

Fixed an issue where literal slashes (\\) in an expression would cause evaluation to fail.

## 2019-10-14 — Attachment filenames (platform)

Updated filenames for attachments as follows:

* You can now specify a custom filename format for validation service attachments
* FormsByAir will no longer prefix attachment filenames with the name of the document

## 2019-10-09 — Display Text html editor (fix)

Updated the Code/HTML editor for Display Text so you no longer have to revert back to the formatted view to save your changes.

## 2019-10-08 — Decimal places without formatting (fix)

FormsByAir will now always round values to the specified number of decimal places, even where the **Format** is not being applied, for example, in text-based files used for import in to other systems.

## 2019-10-07 — Conditional expression for report integrations (fix)

Fixed issue where the conditional expression for submission report integrations was not being evaluated for **CSV From Template** and **Text From Template** file formats.

## 2019-10-07 — More CDNJS (platform)

Changed source for more client-side javascript libraries to cdnjs.cloudflare.com for improved performance.

## 2019-10-07 — Partner logs (feature)

Added partner-level document and exception logs for improved visibility of activity and issues across multiple accounts.

## 2019-10-04 — Add week days (feature)

Added a new System Default to add week days to the current date. See [Default Value]({{ site.baseurl }}/questions/properties/default-value)

## 2019-10-03 — Table validation (fix)

Added validation on table uploads to check for missing or duplicated column headers.

## 2019-10-01 — Display workflow assignment (feature)

FormsByAir will now display the current workflow assignee (if any) next to workflow status at the top of the Document and Document Information pages.

## 2019-09-27 — Default Value for Comment & Diagram questions (fix)

Updated the **Default Value** setting in the form designer as follows:

* **Comment** questions now support multi-line defaults
* **Diagram** questions now display a thumbnail of the current default image, and allow you to upload/remove an image

## 2019-09-26 — Preserve form data line breaks in emails (fix)

FormsByAir will now convert newline characters to HTML &lt;br&gt; tags when evaluating form &lt;&lt;tags&gt;&gt; in email templates, for example, where you are outputting the contents of a **Comment** question that may contain several paragraphs.

## 2019-09-26 — Small diagram format (feature)

Added new *Small* format option for diagrams, which is half the height of the regular size.

## 2019-09-24 — Document referrer (feature)

FormsByAir will now record the domain of the HTTP referrer (where available) for new submissions, this will appear at the top of the document information page. Additional analytics continue to be available via Google Analytics.

## 2019-09-24 — Redundant third party requests (fix)

FormsByAir will now automatically delete any open third party requests that have been indirectly removed from the requesting document, for example, a repeater item that contained a request. This will prevent unneccessary completion and submission of requests that can't be merged back in to the requesting document.

## 2019-09-23 — Repeat template limit (feature)

Added ability to limit the number of repeater entries in file integrations that repeat a template, useful for previewing large files.

## 2019-09-19 — Save & Request Reminder Updates (feature)

Updated Save & Request Reminder emails as follows:

* You can now send **multiple** save and request reminders
* You can specify the timing for each save and request reminder at the integration level
* Save reminders will now reset when a form is re-saved, previously you would only receive one save reminder after the first save.

## 2019-09-18 — Data Service querystring parameters (fix)

Fixed table-based Data Service to ignore querystring parameters that do not match to columns in the underlying table.

## 2019-09-17 — Auto save completed sections (feature)

Added new form level option to automatically save completed sections during form fill.

The purpose of this feature is to provide insight in to abandoned forms (those that have been started, but then closed without saving or submitting)

Form users will continue to receive a warning that their changes haven't been saved when abandoning a form, even if the form has been auto saved.

Save reminders are not sent for auto saved forms unless the form is explicitly saved.

Auto saved forms will appear in the Document Log with CREATED status.

## 2019-09-16 — Filter table lookup for current user (platform)

Added ability to filter a table lookup integration for the current FormsByAir user.

When used in conjunction with a **Data Service** component, you can effectively extend and customise properties for users to drive logic in private forms and integrations.

## 2019-09-12 — Twilio (platform)

Added new integration with [Twilio](https://www.twilio.com) to enable global SMS messaging.

## 2019-09-05 — Block submit on Enter (feature)

Added new form level option to disable the default behaviour of an Enter key press submitting the form.

## 2019-09-02 — Custom submission confirmation (feature)

Select **Hide form after submit** to hide form content and display a formatted message on submit instead of the default green alert at the bottom of the page.

## 2019-09-02 — Third party request purge (fix)

Third party request documents will now only be purged if the requesting document has been purged.

## 2019-08-22 — Multi-select validation (feature)

Extended multi-select validation so you can now specifiy the minimum number of options that must be selected.

## 2019-08-16 — Harmony RightAddress (platform)

Added new integration with [Harmony RightAddress](https://harmonyrightaddress.com) for address lookup in Australia and New Zealand.

## 2019-08-15 — Restore Third Party Request (feature)

Added the ability to Restore an Expired (but not Purged) Third Party Request as long as the requesting document status is Saved or Requested.

## 2019-08-14 — Content Security Policy Whitelist (platform)

Added **Content Security Policy Whitelist** to Settings > Profile allowing connections to, and iframes from a list of trusted domains for all forms within an account.

## 2019-08-13 — Escape tag data in XML files (fix)

Fixed an issue with **XML From Template** file integrations where tag data was not being escaped, potentially resulting in invalid XML files.

## 2019-08-12 — Filter table data in Lookups with expressions (feature)

Added the ability to dynamically filter table data in a Lookup question using an expression. The expression can refer to multiple table columns and tags, and must evaluate to true or false, for example:

table.PaymentType == &apos;&lt;&lt;PaymentType&gt;&gt;&apos; && table.Location == &apos;&lt;&lt;Location&gt;&gt;&apos;

## 2019-08-08 — Repeater default values (fix)

Fixed an issue where default values containing tag references were not being evaluated when adding a new repeater row.

## 2019-08-07 — CreditorWatch (platform)

Added new integration with [CreditorWatch](https://creditorwatch.com.au/) to perform credit checks on Australian businesses.

## 2019-08-06 — PDF Performance (platform)

Upgraded DOCX/PDF component for improved performance when generating very large PDF documents.

## 2019-07-29 — CDNJS (platform)

Updated Javascript CDN source from ajax.googleapis.com and ajax.aspnetcdn.com to cdnjs.cloudflare.com for improved performance, and access from China.

## 2019-07-08 — Email validation warnings (feature)

Added email validation warnings if MX record not found for domain, or domain matches a common misspelling of a major email service provider.

See [Email Address]({{ site.baseurl }}/questions/types/email-address)

## 2019-07-05 — Google Sheets list (feature)

Updated Google Sheets integration to list the available spreadsheets for your Google account, rather than prompting for the Sheet Id.

## 2019-07-03 — Reset Password (fix)

Fixed **Reset Password** so it doesn't clear the user's team and manager.

## 2019-07-02 — Rework document (feature)

Added ability to return a document to workflow after delivery if it was approved in error.

See [Rework]({{ site.baseurl }}/documents/actions/rework)

## 2019-07-01 — Expression validation (feature)

Added design-time validation of expressions in Formula questions and Integration conditions to catch syntax errors.

## 2019-06-27 — NZ Charities Services integration (platform)

Added new integration with [NZ Charities Services](https://www.charities.govt.nz/) to lookup charities by name.

## 2019-06-25 — iCloud attachments in iOS Safari (fix)

Resolved issue where iCloud form attachments in iOS Safari are sometimes submitted as empty (0 byte) files.

## 2019-06-20 — Pattern question type (feature)

Added new **Pattern** question type to validate entry against a specific pattern.

See [Pattern Question Type]({{ site.baseurl }}/questions/types/pattern)

## 2019-06-14 — Generate request with data from another form submission (feature)

Added **Submission Type** option to the **FormsByAir** integration so that target documents can now be saved as a request, instead of being submitted.

See [FormsByAir Integration]({{ site.baseurl }}/integrations/formsbyair)

## 2019-06-12 — Post submit form settings (feature)

* Added **Hide form after submit** setting to hide form content after a form has been submitted so only the confirmation message is displayed.

* Removed **Hide on submit** Display Text property, this is superseded by the **Hide form after submit** setting.

* Added **Submit Url** setting to redirect a form after submit, this can also be specified using a [Form System Parameter]({{ site.baseurl }}/forms/parameters/)

* The **Hide restart button after submit** setting is now enabled by default for new forms, as most forms aren't filled out multiple times in succession.

## 2019-06-08 — REST Connector (platform)

Added generic REST connector to lookup data with just a REST API endpoint. You can also specify an Authorizarion header and a filter parameter for use with typeaheads.

## 2019-06-06 — Timezone (platform)

Set the timezone for your account in Settings > Profile. This applies to dates displayed in the management portal and form output.

## 2019-06-03 — Average function (feature)

Added new function to calculate the average of repeated question values with the same tag.

See [Question Aggregate Functions]({{ site.baseurl }}/questions/aggregate-functions)

## 2019-06-03 — Collapsed group (feature)

Added **Collapsed** property for groups so the contents of a group can be hidden by default, and then expanded or collapsed by clicking the group header or collapse icon.

## 2019-05-31 — Documents By Status filter and export (feature)

Updated **Documents By Status** page to allow filtering by Requested or Received date, and added the ability to export results to CSV.

## 2019-05-28 — Edit advanced mapping files (feature)

Added ability to upload and download JSON mapping files for integrations that support advanced mapping. All other integrations will continue to support basic mapping via our GUI mapping tool.

## 2019-05-27 — Sharepoint integration (platform)

Added new integration with Sharepoint using the Microsoft Graph API. FormsByAir can lookup data from, and push submissions to Sharepoint Lists.

## 2019-05-24 — User Team default (feature)

Added new system default for the current user's team.

See [Question Properties > Default Value]({{ site.baseurl }}/questions/properties/default-value)

## 2019-05-21 — Less Annoying CRM integration (platform)

Added new integration with Less Annoying CRM.

## 2019-05-17 — Hide date calendar popup (feature)

Added option to hide the calendar popup for **Date** questions. Date validation will still apply.

## 2019-05-10 — Submit form on load (feature)

Added new form parameter to automatically submit a form when it's opened.

See [Form Parameters]({{ site.baseurl }}/forms/parameters)

## 2019-05-08 — Revalidate document (feature)

Added ability to revalidate a document in workflow after it's been edited.

See [Revalidate]({{ site.baseurl }}/documents/actions/revalidate)

## 2019-05-06 — Copy form to account (feature)

Added ability to copy a form to a different account if you have access to multiple accounts.

See [Form Copy]({{ site.baseurl }}/forms/actions/copy)

## 2019-04-29 — Read-Only prefill option (feature)

Added new **Prefill** option for the **Read-Only** question property to disable sensitive items during prefill that must be completed by the form filler.

See [Read-Only Property]({{ site.baseurl }}/questions/properties/read-only)

## 2019-04-24 — Data Zoo integration (platform)

Added new integration with Data Zoo for identity verification and AML compliance in Asia-Pacific and beyond.

## 2019-04-23 — Check for empty files, form header versioning & copying (fix)

* Added check for empty (0 byte) files when attaching a file in a form

* Changing a form header image now forces a version increment

* "Copy To" now copies a form header image

## 2019-04-19 — Supervisor role, Reason for edit (feature)

* Added new **Supervisor** role similar to **Operations** but with ability to override workflow assignments and edit documents, see [Roles]({{ site.baseurl }}/account/roles)

* Added prompt to capture "Reason for edit" when saving changes to a submitted document. If provided this comment is stored in the workflow log.

## 2019-04-17 — Copy integration templates (feature)

The "Copy To" function now allows you to (optionally) copy email and file templates to the corresponding integrations in the target form.

## 2019-04-16 — Typeahead exact match (feature)

Added new **Match** Format option for Typeahead questions. FormsByAir will query the data source as you type but partial matches will not be displayed. If an exact match is made the item is auto-selected, which can be used to trigger a conditional path.

## 2019-04-13 — Cancel an integration (feature)

Added ability to **Cancel** an outstanding integration, which will prevent any further delivery attempts. **Disable** is still available if you want to temporarily pause an integration.

## 2019-04-12 — Assignment emails (feature)

[Send custom emails on workflow assignment]({{ site.baseurl }}/integrations/assignment-emails)

## 2019-03-23 — Hosting platform update (platform)

Updated solution to .NET Framework 4.7.2 and Azure OS Family 6 (Windows Server 2019)
