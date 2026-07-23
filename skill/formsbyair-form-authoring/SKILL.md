---
name: formsbyair-form-authoring
version: 2026.7.23
metadata:
  author: FormsByAir
description: Author and edit FormsByAir form definitions (XSD schema files). Use this skill whenever the user wants to create, modify, review, or understand a FormsByAir form — adding/removing questions, sections, dropdown options, conditional visibility, repeating groups, formulas, validation rules, lookups, or document tags — or mentions FormsByAir, a form schema/XSD, form builder output, or files like "*_Form_*.xsd". Also use it when asked how a FormsByAir feature (questions, tags, workflow, templates) works.
---

# FormsByAir Form Authoring

FormsByAir forms are defined as XML Schema (XSD) files. The GUI form builder
generates them, but they can be edited directly. The XSD structure defines the
data shape; the form's UI and logic live in
`<xs:documentation source="PROPERTY">VALUE</xs:documentation>` annotations.

## Before any edit

1. Read `references/annotations.md` — the complete property vocabulary
   (verified against the platform source).
2. Read `references/patterns.md` — canonical XML shapes for every field/structure type.
3. If the task involves tags (`<<...>>`), read `references/tag-engine.md` —
   exact resolution semantics distilled from the platform's tag engine.
   For integration maps, read `references/integration-map-format.md`.
   For "does FormsByAir integrate with X?", see `references/connectors.md`.
   When referencing extended data from a data-service lookup/typeahead
   (`<<Key.SubField>>`), get the exact property names from
   `references/integration-models.swagger.json` — the platform's external
   integration models (MBIE/Companies Office entities, NZ Charities,
   Australian Business Register, FSPR, CarJam, Equifax, CreditorWatch,
   and the shared Address/Officer/Shareholder/BeneficialOwner shapes).
   Don't guess property names; a misspelled sub-property silently resolves
   to an empty string.
   Before structural edits (adding/moving groups, repeaters, conditions,
   lists), read `references/builder-validation.md` — the rules the GUI form
   builder enforces at save time; a hand-edited form that breaks them will
   error when next opened in the builder.
4. If the task involves formulas, question types, or document templates,
   read the matching official doc under `references/docs/`
   (mirrors https://docs.formsbyair.com/):
   - `docs/questions/types/*.md` — per-question-type behaviour
   - `docs/questions/properties/*.md` — default value, read-only, autocomplete
   - `docs/tags/*.md` — tag syntax, functions (ForEach, Condition, Join...), format
   - `docs/forms/*.md` — form settings, parameters, status
   - `docs/build-form.md` — end-to-end form building tutorial
   - `docs/changelog.md` — dated release notes (2019–present, newest first)
     describing how the system has changed over time; check here when a
     feature's behaviour seems version-dependent or a doc mentions something
     that used to work differently
   - `docs/integrations/*.md` — sending form data to other applications
     (file formats, JSON/XML maps); `docs/samples/` — official map samples
     with their outputs
   - `docs/kb.md` — Q&A troubleshooting articles from the knowledge base

For live/latest documentation, docs.formsbyair.com is the authoritative source;
the bundled copies are a snapshot.

## Form design principles

When building a form from scratch or converting an existing form (uploaded
PDF/Word/paper form or a description), apply good digital form design rather
than copying the source layout literally:

- **Repeating elements → repeater.** If the source has numbered duplicates
  ("Person 1", "Person 2", "Beneficiary 1/2/3"...), model it once as a
  repeating group (`maxOccurs="unbounded"`), not as copies. Users add rows
  as needed.
- **"If yes, please provide detail" → conditional path.** Put the follow-up
  question(s) in a conditional branch (`visibility`) **as a child of** the
  controlling question that displays only when Yes (or the relevant option)
  is selected, and **omit the "if yes" wording** from the follow-up's
  prompt — the condition already expresses it. A condition group must be
  nested inside the question it switches on, never placed as a sibling —
  see the conditional-branch patterns in `references/patterns.md`.
- **Type-dependent steps → dynamic sections.** When a source form shows or
  hides whole steps based on an early choice (e.g. investor type routing to
  different certification steps), don't fold everything into shared static
  sections — sections themselves can be conditional. Wrap the section(s) in
  a hidden formula switch placed at the top level of the form (a sibling of
  the other sections), and the wizard step appears only when the formula
  matches — see "Conditional (dynamic) section" in `references/patterns.md`
  and the live instances in `assets/example-wholesale-investment-v1.xsd`.
- **Email and phone get their specific types.** If a question is clearly an
  email address or a phone number, use `fba:email` / `fba:phone` (not
  `xs:string`) so input is validated as the user types.
- **Person names are plain text.** `fba:name` is deprecated — use
  `xs:string` with `autocomplete` = `name`.
- **"About this form" guidance → the form Instruction, not content.** Put
  any about-this-form / how-to-use text in the root `Form` element's `note`
  annotation (the builder's Instruction setting) rather than creating
  `fba:note` content elements for it. It renders at the start of the form,
  may contain basic HTML tags such as `<br>` and `<strong>`, and can be
  added to or overridden per-link with the `Note` URL parameter
  (`docs/forms/parameters.md`). Reserve `fba:note` elements for guidance
  tied to a specific section, group, or question.
- **Addresses: addressPicker by default, Typeahead for NZ — never a
  Lookup.** A Lookup (`fba:lookup`) renders as a drop-down, so it only
  suits lists up to the hundreds of rows; addresses number in the
  millions. Any non-NZ single-line address question defaults to
  `fba:addressPicker` (Google address lookup — no service subscription
  needed). NZ addresses use a Typeahead (`fba:typeahead`) with
  `allowmanualentry` and `getextendeddata`, so an NZ address service
  (e.g. NZ Post) can be connected. Leave `subscriptionid` off —
  the user connects the service in the builder.
- **Always set a Document Reference.** On any new form, set the form-level
  `documentreference` annotation to a tag holding a relevant unique
  identifier for the submission — generally a name of some kind (e.g. the
  applicant, company, or vendor name) — so submitted documents are
  identifiable in the workflow list.
- **Company/registered names get a typeahead.** Model them as
  `fba:typeahead` with `getextendeddata` so a companies-register service
  (e.g. MBIE/Companies Office in NZ) can prefill sibling fields such as
  the business number via `'<<Key.SubField>>'` defaults — e.g.
  `'<<ClientName.NZBN>>'` for an NZ Business Number (prefer `NZBN` over
  `CompanyNumber`, which only exists for companies). Property names come
  from `references/integration-models.swagger.json`. Leave
  `subscriptionid` off for the user to connect.
- **Most fields are required by default.** Mark fields required
  (`minOccurs="1"`) unless they are clearly optional; don't leave
  requiredness off just because the source form didn't state it.
- **Preserve source-document formatting in display content.** When form
  content originates from a Word/PDF/HTML source, never extract plain text
  only — read run-level formatting (for docx: `w:b`, `w:i`, `w:u`,
  `w:highlight` in `word/document.xml`) and carry it into `note`
  (Display Content) values as inline HTML: `<strong>` for bold, `<em>` for
  italic, `<u>` for underline, `<a href="...">` for hyperlinks, XML-escaped
  in the XSD (`&lt;strong&gt;`), matching the builder's Editor toolbar
  output. Keep bullets/numbering in the markdown-style `*` syntax, not
  `<ul>`/`<ol>`, since HTML lists don't translate to auto-generated output
  documents. Formatting is also data: highlighting, strikethrough, or
  colour in a change-request document often encodes which items an
  instruction applies to, so inspect it before acting.
- **No layout HTML in display content — the PDF output can't render it.**
  The form view renders arbitrary pasted HTML, but the auto-generated PDF
  of a submitted document does not translate HTML layout: `<table>`-based
  layouts, spacer rows/cells (`&nbsp;` with fixed heights), and
  inline-styled `<div>` grids come out as each cell/block stacked on its
  own line with large vertical gaps. Express structure with form
  structure instead — groups (titles), separate `note` elements, and
  markdown `*` bullets — and keep HTML inside a note to simple inline
  tags (`<strong>`, `<em>`, `<u>`, `<a>`). When editing an existing form
  that contains pasted layout HTML (a common artefact of copying from
  Word/web), expect its PDF output to be broken and rebuild the content
  as group + display content rather than patching the HTML.

## Reading a form

- Element names (`a` + 32 hex chars) are opaque IDs. Locate fields by their
  `prompt`, `title`, or `autofillkey` annotations, never by element name.
- `autofillkey` is the logical field name; `<<AutofillKey>>` tags reference it
  in formulas, defaults, validation, and document templates.
- Autofillkeys are not unique per submission: if the element sits inside a
  repeater, or several elements share the same autofillkey, a simple
  `<<Tag>>` outputs **every** instance value separated by spaces — e.g.
  `<<PhoneNumber>>` in a two-row repeater renders `021123123 021345122`.
  This surprises form authors constantly. When one value is wanted, use
  `<<Repeater[0].Tag>>`, `[First:...]` or `[ForEach:...]` — see
  `references/tag-engine.md`.
- Structure: root `Form` → sections (`source="section"`) → groups → fields.
  Sections can also sit inside the condition branch of a top-level hidden
  formula switch — a dynamic section: the whole wizard step appears only
  when the formula matches the branch's `visibility` value.
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
- Formulas (`fba:formula` `hint`) are JavaScript-compatible expressions
  evaluated client-side; string comparisons quote tag references:
  `'<<ClientType>>' == 'Trust'`. Date math uses moment.js:
  `moment().diff(moment('<<DOB>>'), 'years')`. Server-side expressions —
  `[Expression:...]` tags, `[Condition:...]`/`{...}` filters, map filters —
  use NCalc instead (no moment.js, no JS objects); see
  `references/tag-engine.md`.

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

`assets/example-wholesale-investment-v1.xsd` (Wholesale Investment
Application v1) additionally shows **dynamic sections**: top-level hidden
formula switches (e.g. "Wholesale Investor", "Other Investor") whose
condition branches wrap whole Certification sections, so the wizard steps
themselves change with the selected investor type.

`assets/example-integration-map.json` is a production-style integration map
(investment application → wealth-administration platform) showing entity
nesting, conditional attribute filters (if/else-if chains), `ForEach` over
repeating groups, and full document-tag syntax in mapped values. The exact
evaluation semantics are in `references/integration-map-format.md`; simpler
official samples with their outputs are in `references/docs/samples/`.

---
Skill version: 2026.7.23 — when reporting issues with this skill, quote this version.
