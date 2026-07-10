---
name: formsbyair-form-authoring
version: 2026.7.10
description: Author and edit FormsByAir form definitions (XSD schema files). Use this skill whenever the user wants to create, modify, review, or understand a FormsByAir form — adding/removing questions, sections, dropdown options, conditional visibility, repeating groups, formulas, validation rules, lookups, or document tags — or mentions FormsByAir, a form schema/XSD, form builder output, or files like "*_Form_*.xsd". Also use it when asked how a FormsByAir feature (questions, tags, workflow, templates) works.
---

# FormsByAir Form Authoring

FormsByAir forms are defined as XML Schema (XSD) files. The GUI form builder
generates them, but they can be edited directly. The XSD structure defines the
data shape; the form's UI and logic live in
`<xs:documentation source="PROPERTY">VALUE</xs:documentation>` annotations.

## Before any edit

1. Read `references/annotations.md` — the property vocabulary.
2. Read `references/patterns.md` — canonical XML shapes for every field/structure type.
3. If the task involves formulas, tags (`<<...>>`), question types, or document
   templates, read the matching official doc under `references/docs/`
   (mirrors https://docs.formsbyair.com/):
   - `docs/questions/types/*.md` — per-question-type behaviour
   - `docs/questions/properties/*.md` — default value, read-only, autocomplete
   - `docs/tags/*.md` — tag syntax, functions (ForEach, Condition, Join...), format
   - `docs/forms/*.md` — form settings, parameters, status
   - `docs/build-form.md` — end-to-end form building tutorial

For live/latest documentation, docs.formsbyair.com is the authoritative source;
the bundled copies are a snapshot.

## Reading a form

- Element names (`a` + 32 hex chars) are opaque IDs. Locate fields by their
  `prompt`, `title`, or `autofillkey` annotations, never by element name.
- `autofillkey` is the logical field name; `<<AutofillKey>>` tags reference it
  in formulas, defaults, validation, and document templates.
- Structure: root `Form` → sections (`source="section"`) → groups → fields.
  Groups with `visibility` are conditional branches; `maxOccurs="unbounded"`
  marks repeaters.

## Editing rules

- NEVER rename or delete existing element names or autofillkeys unless
  explicitly asked — tags, document templates, integrations, and saved
  documents depend on them.
- New elements: generate a fresh ID
  (`python3 -c "import uuid; print('a'+uuid.uuid4().hex)"`), copy the exact
  shape from `references/patterns.md`, keep `nillable="true"`, and place the
  element inside the correct `<xs:sequence>`.
- Required = `minOccurs="1"` attribute, not an annotation.
- Never invent `subscriptionid` or `tableid` GUIDs — reuse ones already in the
  form or ask the user.
- Preserve the file's existing conventions: CRLF line endings, two-space
  indentation, HTML-encoded entities inside annotation text
  (`&lt;&lt;Tag&gt;&gt;` for `<<Tag>>`).
- Do not touch the root `Form` element's `save*`/owner/workflow annotations or
  the schema `version` attribute unless asked.
- Formulas (`fba:formula` `hint`) are JavaScript-compatible expressions;
  string comparisons quote tag references: `'<<ClientType>>' == 'Trust'`.
  Date math uses moment.js: `moment().diff(moment('<<DOB>>'), 'years')`.

## After every edit

Run the validator (works with `xml.etree` from the standard library, no
dependencies):

```bash
python3 scripts/validate.py edited.xsd original.xsd
```

Fix any ERRORs before returning the file. Report WARNINGs to the user with a
one-line explanation. Always return the complete edited file and summarise
what changed and where (section/group titles, not element IDs).

## Worked example

`assets/example-retail-investment-v5.xsd` is a complete production-style
template (Retail Investment Application v5): sections, entity-type branches
via `visibility`, repeaters, Companies Office typeahead lookups, FATCA/CRS
validation switches, and a document reference using `[ForEach:...]`. When
unsure how a construct fits together, find a live instance in this file.

---
Skill version: 2026.7.10 — when reporting issues with this skill, quote this version.
