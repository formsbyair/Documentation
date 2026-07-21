# FormsByAir XSD Annotation Property Reference

Form behaviour is defined in `<xs:documentation source="PROPERTY">VALUE</xs:documentation>`
elements inside each element's `<xs:annotation>`. The XSD types define data shape;
annotations define UI and logic.

This is the complete vocabulary, verified against the XSD serializer
(`FormsByAir.Factory/FormFactory.cs` in the private FormsByAir.Web
repository, July 2026 snapshot). Boolean properties take the literal string
`True` (absence means false).

## Element kind (how a complex element is classified)

A complex (container) element's role is decided by the **first** of these
annotations present: `workflow` → workflow step; `section` → form
section/page; `validationService` → section-validation service call;
`paymentService` → payment step; `request` → third-party request block;
none of them → plain group. A group nested under an option/boolean question
with a `visibility` annotation is a conditional branch — it renders only
when the parent question's value equals the `visibility` value
(case-insensitive). `maxOccurs="unbounded"` (any explicit `maxOccurs`)
marks a repeater; `minOccurs="1"` means required.

Sections are normally direct children of the root `Form` element, but a
section may also sit inside the condition branch of a **top-level** hidden
formula switch (itself a direct child of `Form`, alongside the other
sections) — a *dynamic section*: the whole wizard step appears only when
the formula result matches the branch's `visibility` value. See
"Conditional (dynamic) section" in `references/patterns.md`.

## Display & labelling

| Property | Meaning |
|---|---|
| `title` | Heading for a section or group. On the root `Form` element, the form's display name. |
| `prompt` | Question/field label shown to the user. |
| `note` | Help/informational text. On `fba:note` elements it is the content itself. May contain HTML, but keep it to simple inline tags (`<strong>`, `<em>`, `<u>`, `<a>`): layout HTML (tables, spacer rows, styled div grids) renders in form view but breaks the generated PDF output, which stacks each block with large vertical gaps. Use markdown `*` bullets and group structure instead. |
| `popupnote` | `True` = note displays as a popup instead of inline. |
| `hint` | On input fields: helper/placeholder text. On `fba:formula` fields: the formula expression itself. Context-dependent — check the element type. |
| `width` | Grid width of the field (12-column grid). |
| `format` | Rendering/formatting mode. Per-type: e.g. `titleCase`/`upperCase` (text), `year`/`month` (date), `12` (time), `post`, `inline`, `international-mobile` (phone), `date`/`number`/`percent`/`currency` (formula output type). |
| `inline` | Inline rendering flag. |
| `cssclass` | Custom CSS class(es) applied to the element. |
| `sort` | Sort order for list/lookup options. |
| `autocollapse` | `True` on a repeater = rows auto-collapse (first row expanded on open). |

## Structure & conditionality

| Property | Meaning |
|---|---|
| `visibility` | Conditional display. On a group nested **as a child of** the controlling question, the value matches one of that question's enumeration values (`True`/`False` for a boolean parent) — the group shows only when selected. The controlling question hosts its branches in its `<xs:sequence>` and moves its own value to an `<xs:attribute name="value">`; see the conditional-branch patterns. |
| `hidden` | `True` = element not shown during form-fill. Used for computed `fba:formula` fields and validation switches. |
| `readonly` | `True` = display-only field. |
| `readonlyprefill` | `True` = field becomes read-only when prefilled. |
| `arrayexpression` | Expression producing/controlling repeater rows from data. |
| `linkedrepeater` | Autofillkey of another repeater whose rows this repeater's rows pair with (row *n* links to row *n*). Affects tag scope escalation. |
| `canduplicate` | `True` = user can duplicate a repeater row. |
| `cansubmitpartial` | `True` on a section = section can be submitted partially complete. |
| `defervalidation` | `True` on a section = validation deferred. |
| `limit` | Maximum rows / selection count / attachment limit. |

## Data & identity

| Property | Meaning |
|---|---|
| `autofillkey` | The logical field name. Used in `<<Tag>>` references, data binding, document templates, and export. Element names are opaque IDs. |
| `default` | Pre-populated value; may be a tag expression. |
| `subscriptionid` | GUID linking a typeahead/lookup/validation/payment element to an external service subscription. Never invent — reuse or ask. |
| `tableid` | GUID linking a field to a lookup table. Never invent — reuse or ask. |
| `getextendeddata` | `True` = lookup stores the full response; sub-fields readable as `<<Key.SubField>>`. |
| `matchstart` | Typeahead matches from start of string. |
| `allowmanualentry` | `True` = user may type a value not in the lookup. |
| `forcedropdown` | Deprecated. |
| `attachresponse` | `True` = attach the validation-service response to the document. |
| `autocomplete` | Browser autocomplete hint (e.g. `email`). |
| `displayproperty` | Which property of a lookup result to display. |
| `filter` | Filter expression applied to lookup/typeahead results. |
| `filenameformat` | Filename template for attachments (tag syntax allowed). |
| `postsubmit` | Deprecated (equivalent to `format` = `post` on validation services). |

## Selection lists

| Property | Meaning |
|---|---|
| `listtype` | How an enumerated field renders: `dropdown`, `radio`, `toggle`. Options are `xs:enumeration` values in an `xs:restriction`. |
| `name` | On an `xs:enumeration`: the display label when it differs from the stored value. |
| `note` | On an `xs:enumeration`: help text for that option. |

## Validation

| Property | Meaning |
|---|---|
| (attribute) `minOccurs="1"` | Required field (XSD attribute, not annotation). |
| `validationmethod` | `expression` = validate via the element's formula (`hint`); a country code/tag = country-specific validation (addresses, phone). On sections: the section-validation method. |
| `validationmessage` | Custom error text when validation fails. |
| `validationinline` | Error shows inline. |
| `min` / `max` | Numeric/date bounds. |
| `step` | Slider step increment. |
| `decimals` | Decimal places for currency/number/percent fields. |
| `country` | Country context for address/phone validation. |
| `confirmationmessage` | On sections/validation services: message shown on completion. |

## Form-level (root `Form` element only)

Identity/metadata: `title`, `note`, `owner`, `ownerId`, `name`.
Behaviour: `documentreference` (document reference template using tag
syntax), `style`, `header`, `footer`, `validationscript`, `trackingscript`,
`trackinglabel`, `confirmationmessage`, `submiturl`, `returnurl`,
`documentnotfoundmessage`, `closedmessage`, `hidetitle`, `hiderestart`,
`hidenavfirstsection`, `hideformaftersubmit`, `blocksave`,
`blocksavecookie`, `blocksubmitonenter`, `autosavesections`,
`autogeneratemissingtags`.
Save flags: `savecompletedsections`, `savedocumentdeliveryid`,
`saverequestdocumentid`, `saverequestcompleted`, `savesectionvalidationdata`,
`savesectionvalidationmessage`, `savesectionvalidationreference`,
`savetrycount`.
Workflow/request markers: `workflow`, `request`, `section`.

Do not modify form-level annotations unless explicitly asked.

## Question types

FormsByAir types (namespace `fba:`, imported from
`https://formsbyair.com/schema/1/fba.xsd`) — complete list from the
serializer: `name` (**deprecated** — the builder no longer offers it as a
question type; use `xs:string` with `autocomplete` = `name` instead),
`email`, `phone`, `comment` (multi-line text),
`address`, `signature`, `attachment`, `rating`, `note` (display content),
`caps`, `option` (selection), `lookup` (table lookup — renders as a
drop-down, so only suits lists up to the hundreds of rows; for large
datasets like addresses use `typeahead`), `formula`
(computed expression), `diagram`, `number`, `addressPicker`, `currency`,
`percent`, `map`, `typeahead` (search-as-you-type against a subscription),
`terms`, `optionText`, `nzird` (NZ IRD number), `nzbank` (NZ bank account),
`slider`, `nzpassportNumber`, `nzdriverlicenceNumber`,
`nzdriverlicenceVersion`, `dataService`, `card`, `pattern`, `placeholder`.

Standard XSD types: `xs:string`, `xs:boolean` (checkbox), `xs:date`,
`xs:time`, `xs:int`. Enumerated fields use a named `xs:simpleType` with an
`xs:restriction` (`nameValueList` behaviour when enumerations carry `name`
annotations).

See `references/docs/questions/` for official per-type documentation and
`references/tag-engine.md` for how each type formats in tag output.
