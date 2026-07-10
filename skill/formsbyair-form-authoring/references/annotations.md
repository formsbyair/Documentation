# FormsByAir XSD Annotation Property Reference

Form behaviour is defined in `<xs:documentation source="PROPERTY">VALUE</xs:documentation>`
elements inside each element's `<xs:annotation>`. The XSD types define data shape;
annotations define UI and logic.

Properties observed in production templates, grouped by purpose.
Items marked ⚠ are inferred from examples — verify semantics before relying on them
in unusual contexts.

## Display & labelling

| Property | Meaning |
|---|---|
| `title` | Heading for a section or group. On the root `Form` element, the form's display name. |
| `prompt` | Question/field label shown to the user. |
| `note` | Help/informational text. On `fba:note` elements it is the content itself (may contain HTML links). |
| `popupnote` | `True` = note displays as a popup instead of inline. |
| `hint` | On input fields: helper/placeholder text. On `fba:formula` fields: the formula expression itself. Context-dependent — check the element type. |
| `width` | Grid width of the field (12-column grid). |
| `format` | Rendering/formatting mode. Observed values: `titleCase`, `upperCase`, `post`, `inline`, `international-mobile`. `inline` on a repeating group renders rows inline. |
| `section` | Value `section` marks a top-level section (form page). |
| `inline` | ⚠ Inline rendering flag (rare). |

## Structure & conditionality

| Property | Meaning |
|---|---|
| `visibility` | Conditional display. On a group that follows a controlling option field, the value matches one of that option's enumeration values — the group shows only when that option is selected (e.g. Investor Type branches: `Trust`, `Company`, `Estate`). |
| `hidden` | `True` = element not shown during form-fill. Used for computed `fba:formula` fields and validation switches. Visible in Workflow via the "Formulas" toggle. |
| `readonly` | `True` = display-only field. |
| `arrayexpression` | ⚠ Expression controlling repeater rows from data. |
| `linkedrepeater` | ⚠ Links a repeater to another repeater's rows. |

## Data & identity

| Property | Meaning |
|---|---|
| `autofillkey` | The logical field name. Used in `<<Tag>>` references, data binding, document templates, and export. This is the "real" field name; element names are opaque IDs. |
| `default` | Pre-populated value. Often a tag expression, e.g. `'<<ClientName.CompanyNumber>>'`. |
| `subscriptionid` | GUID linking a typeahead/lookup to an external data source (e.g. Companies Office). |
| `tableid` | GUID linking a field to a lookup table. |
| `getextendeddata` | `True` = lookup returns extended data fields accessible as `<<Key.SubField>>`. |
| `matchstart` | Typeahead matching from start of string (`True`/`False`). |
| `allowmanualentry` | `True` = user may type a value not in the lookup. |
| `attachresponse` | ⚠ `True` = attach the lookup/validation service response to the document. |
| `validationService` | ⚠ Invokes a validation service on the group (seen alongside Companies Office lookup). |
| `autocomplete` | Browser autocomplete hint (e.g. `email`). |

## Selection lists

| Property | Meaning |
|---|---|
| `listtype` | How an enumerated field renders: `dropdown`, `radio`, `toggle`. Options are `xs:enumeration` values in an `xs:restriction`; each may carry a `name` annotation when display label differs from stored value. |
| `name` | On an `xs:enumeration`: the display label for that option. |

## Validation

| Property | Meaning |
|---|---|
| (element) `minOccurs="1"` | Required field (attribute, not annotation). |
| `validationmethod` | `expression` = validate via the element's formula (`hint`); a `<<CountryTag.Code>>` value = country-specific validation (addresses, phone). |
| `validationmessage` | Custom error text when validation fails. |
| `validationinline` | Whether the error shows inline (`True`/`False`). |
| `min` / `max` | Numeric/date bounds. |
| `decimals` | Decimal places for currency/number fields. |

## Numbers & money

`fba:currency` with `decimals`; `min`/`max` for bounds.

## Form-level (root `Form` element only)

`documentreference` (document reference template using tags and `[ForEach:...]`),
`owner`, `ownerId`, `hiderestart`, `request`, `workflow`,
and the `save*` flags (`savecompletedsections`, `savedocumentdeliveryid`,
`saverequestdocumentid`, `saverequestcompleted`, `savesectionvalidationdata`,
`savesectionvalidationmessage`, `savesectionvalidationreference`, `savetrycount`).
Do not modify these unless explicitly asked.

## Element types

FormsByAir types (namespace `fba:`, imported from `https://formsbyair.com/schema/1/fba.xsd`):

`fba:formula` (computed/hidden expression), `fba:lookup` (table lookup),
`fba:comment` (multi-line text), `fba:attachment` (file upload), `fba:option`
(selection), `fba:note` (display content), `fba:typeahead` (search-as-you-type
against a subscription), `fba:addressPicker`, `fba:email`, `fba:phone`,
`fba:currency`, `fba:nzird` (NZ IRD number), `fba:nzbank` (NZ bank account).

Standard types: `xs:string`, `xs:boolean` (checkbox), `xs:date`, `xs:int`.

See `references/docs/questions/` for official per-type documentation.
