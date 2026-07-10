# Form builder validation rules

Distilled from the form-builder portal source
(`FormsByAirWeb8/portal/app/form*.component.{ts,html}` in the private
FormsByAir.Web repository, July 2026 snapshot). These are the rules the GUI
form builder enforces before a form can be **saved** — a hand-edited XSD
that violates them will surface as errors the next time someone opens the
form in the builder, so treat them as invariants when editing XSD directly.

`scripts/validate.py` enforces the structural subset of these rules; the
expression-compilation and account-scoped rules (marked ✋) can only be
checked by the builder itself.

## Save gate

The form cannot be saved at all when:

- The form contains no elements — *"Form must contain at least one element"*.
- Any element below fails — *"Can't save form, one or more elements have
  missing or invalid property values"* (the builder opens the offending
  element and shows the specific message).

## Structural rules (all element kinds)

| Rule | Builder message |
|---|---|
| Group, Condition, Workflow, Section, and Validation Service containers must contain at least one child element. | *"Group must contain at least one element"* / *"Condition must contain at least one element"* |
| A repeater (group with `maxOccurs`) must be the **only** item within its parent group. | *"Repeater must be the only item within a group"* |
| Groups, Workflow steps, Sections, and Validation Services require a `title`. | *"Required"* |
| Every question requires a `prompt` (Question Title), except display content (`note`) and `terms`. | *"Required"* |
| `note`/`terms` require content with at least some non-whitespace (after stripping `<br>`, `&nbsp;`, empty divs). | *"You must include some non-whitespace content"* |

## Tag names and form settings

| Rule | Builder message |
|---|---|
| Tag Name (`autofillkey`) must not contain `'` `"` `<` `[` `]` `>`. | *"Can't contain ' " < [ ] >"* |
| Form Short Name must not contain spaces. | *"Can't contain spaces"* |
| Form Title is required. | *"Required"* |

## Selection lists (`list` / `nameValueList`)

| Rule | Builder message |
|---|---|
| At least two options. | *"List must contain at least two options"* |
| Option values must be unique. | *"Option values must be unique"* |
| No empty option values; for `nameValueList`, no empty option names. | (blocks save) |

## Conditional branches (`visibility`)

| Rule | Builder message |
|---|---|
| `visibility` value is required on a condition. | *"Required"* |
| Parent is a `list`/`nameValueList` question → value must be one of the option **values** (not names). | *"Required"* |
| Parent is `boolean` → value must be `True` or `False`. | *"Required"* |
| Parent is `option` or `note` → value must be `True`. | *"Required"* |
| Parent is a `formula` → value matches the formula's possible outputs (not checkable statically). | — |
| Conditional paths are **not supported** inside inline or tabular groups (group with `inline` or `format`=`inline`/`table`). | *"Conditional path not supported for inline or tabular content"* |

## Per-type property requirements

| Rule | Builder message |
|---|---|
| `slider` requires `min`, `max`, and `step`. | *"Required"* |
| `phone` with format `international` / `international-mobile` requires a default `country` (ISO 2-char code or `<<tag>>`). | *"Required"* |

## Expressions ✋ (validated by JS compilation in the builder)

Formula `hint` expressions, `default` values containing `<<tags>>`, and the
form-level expressions (spam, workflow bypass/assignment, authorisation
bypass/assignment/authorised-assignment) are compiled as **JavaScript** with
`moment` and `momentBusiness` in scope; tags are mocked as the number `2`
during compilation, and syntax errors are shown verbatim. Additional rules:

- Aggregate wrappers over repeater tags are recognised: `sum(<<Tag>>)`,
  `average(<<Tag>>)`, `join(<<Tag>>)`, `unique(<<Tag>>)`, `any(<<Tag>>)`.
- A formula whose entire expression is one bare tag needs a numeric format —
  *"Set numeric format or add quotes around tag"* — because an unquoted tag
  substitutes as text. Quote it (`'<<Tag>>'`) or set the formula's format to
  a numeric type.
- Same for defaults: a bare-tag default on a string-typed question
  (`string`, `email`, `typeahead`, `lookup`, or format `string`) →
  *"Set numeric question type/format or add quotes around tag"*.

## Account-scoped references ✋

| Rule | Builder message |
|---|---|
| `subscriptionid` must reference an existing subscription of the right kind for the element (validation service, payment service, data service for `dataService`/`lookup`/`typeahead`, attached-template service for `attachment`). | *"Current service not found, select a different service or None to disable"* |
| `tableid` must reference an existing data table in the account. | *"Current table not found, select a different table or None to disable"* |
| `validationmethod` must be the literal `expression` or the name of a `$scope.<name>` function defined in the form's Validation Script. Not checked for `addressPicker` or international phone formats. | *"Validation method doesn't exist"* |

These depend on the account the form lives in, so when hand-editing: never
invent `subscriptionid`/`tableid` GUIDs — reuse ones already in the form or
ask the user (also stated in SKILL.md).
