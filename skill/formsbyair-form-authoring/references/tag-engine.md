# Tag engine — exact semantics

Distilled from the server tag engine (`FormsByAir.SDK/Extensions.cs`,
`ParseTags`) in the private FormsByAir.Web repository, July 2026 snapshot.
This is ground truth for how `<<...>>` tags resolve in document references,
templates, integration maps, and delivery filters. The official docs under
`references/docs/tags/` describe the same behaviour informally.

## Tag forms

| Form | Use |
|---|---|
| `<<Name>>` | Simple tag — resolves an autofillkey. |
| `<<[Function:...]>>` | Function or system tag. |
| `<<<[...]>>>` | Same as `<<[...]>>`, but for content that itself contains `]>>` — e.g. an `[Expression:...]` whose body nests other `<<[...]>>` tags. Without the triple brackets the tag would be cut off at the first inner `]>>`. |

Tags are matched non-greedily in order of appearance and each is replaced
once. A tag that matches nothing resolves to an **empty string, never an
error**. System tags the engine doesn't recognise (e.g. `<<[DocumentId]>>`,
`<<[DocumentReceivedDateTime]>>`) are left in place for a later stage —
they're resolved at delivery time, so they survive this pass untouched.

## Simple tag resolution

- The document tree is flattened (conditional branches only contribute the
  selected path) and **every** element whose `autofillkey` matches the tag
  (case-insensitive) contributes its value, concatenated with the separator
  (default: one space). Empty values are skipped. Duplicate autofillkeys
  across repeater rows therefore concatenate — use `Name[i].`, `[First:...]`
  or `[ForEach:...]` to pick specific rows.
- `<<Repeater[0].Tag>>` — indexed row access, **zero-based**; out-of-range
  resolves to empty.
- `<<[This]>>` — the current repeater row's own value (inside `[ForEach:...]`
  / `[First:...]` templates).
- **Scope escalation**: inside a repeater row template, tags resolve within
  that row first. If the tag doesn't exist at the current level at all (not
  merely empty or hidden behind an unselected conditional branch / empty
  repeater), resolution escalates to the parent scope, and so on upward.
  Linked repeaters (`linkedrepeater`) escalate to their linked parent row.

## Suffixes

- `<<Tag|format>>` — .NET format string (e.g. `<<DOB|yyyy>>`,
  `<<Amount|N2>>`). `|filename` sanitises the value for use in file names.
  `|0` on `nzird`/`nzbank` strips the dashes.
- `<<Tag.Property>>` — a sub-property:
  - For lookup/typeahead/validation elements with extended data, `Property`
    is a JSON path into the stored response token (e.g.
    `<<ClientName.CompanyNumber>>`, `<<TaxCountry.Code>>`).
  - `<<Tag.Value>>` — the raw stored value, bypassing display formatting
    (useful for `nameValueList` and `boolean`).
  - `<<Tag.Name>>` — the display name of a `nameValueList` value.
  - Section validation data: `<<Section.[SectionValidationData.path]>>`,
    `<<Section.[SectionValidationMessage]>>`, `...Reference]>>`,
    `...DateTime]>>`, `...Result]>>`, `<<Section.[DocumentDeliveryId]>>`.

## Default output formatting by element type

Applied when the output is "formatted" (documents, templates) or when an
explicit `|format` is given; raw contexts (expressions, filters, XML maps)
get the stored value:

| Type | Formatted output |
|---|---|
| `date` | `dd-MMM-yyyy` (element format `year` → `yyyy`, `month` → `MMM-yyyy`) |
| `time` | `HH:mm`, or `hh:mm tt` when element format is `12` |
| `currency` | `C{decimals}` (e.g. `$1,234.50`) |
| `number` | `N{decimals}` (default 0 dp) |
| `percent` | `P{decimals}` |
| `slider` | `N1` if step < 1 else `N0` |
| `boolean` | `Yes` / `No` (raw: `true`/`false`) |
| `option` | The option's prompt text when ticked, else empty |
| `nameValueList` | The display Name (raw/.Value: the stored value) |
| `formula` | Per the formula's declared format (date/number/percent/currency) |
| `nzird` | Keeps dashes when formatted; `|0` strips them |

## Functions

Filters `{...}` are boolean expressions evaluated per row (see *Expressions*
below). `Repeater` means the autofillkey of the repeating group.

- `<<[ForEach:Repeater{filter}[sep]:template]>>` — renders `template` once
  per (matching) row, joined by `sep`. `sep` supports escapes (`[\n]`);
  placing `[sep]` **before** the repeater name emits a leading separator when
  there is output. `@Index` inside the template is the **1-based** row
  number. Template defaults to `<<[This]>>`. Default separator: space.
- `<<[First:Repeater{filter}:template]>>` — first matching row only.
- `<<[ElementAt(n):Repeater{filter}:template]>>` — the *n*-th matching row,
  **zero-based** (counted after filtering).
- `<<[Condition:filter:content]>>` — `content` if `filter` is true, else
  empty. `content` may nest other `<<[...]>>` tags.
- `<<[Any:Repeater{filter}]>>` — `"true"` if any row matches; `{filter}`
  optional (then: any row exists). **Empty repeater → `"false"`.**
- `<<[All:Repeater{filter}]>>` — `"true"` if every row matches; `{filter}`
  required. **Empty repeater → `"true"`** (vacuous truth) — combine with
  `[Any:...]` if that matters.
- `<<[Count:Repeater{filter}]>>` — number of matching rows. Optional second
  part `:expression` evaluates an expression with `@Count` substituted.
- `<<[Expression:expr]>>` — evaluates `expr` (see *Expressions*).
- `<<[Join:[sep] <<A>> <<B>> ...]>>` — joins the non-empty tag values with
  `sep`; skips empties so you don't get doubled separators.
- `<<[Fallback: <<A>> <<B>> ...]>>` — the first tag (left to right) that
  resolves non-empty; later tags are not evaluated.
- `<<[Stage]>>` — autofillkey of the last completed section.

## Expressions and filters

`[Expression:...]`, `[Condition:...]` filters, `{...}` row filters, map
`Filter` properties, and delivery filters are all evaluated by **NCalc**
(a .NET expression library) — *not* JavaScript. Tags are interpolated as
text **before** evaluation, with single quotes in values escaped, so:

- Quote string comparisons: `'<<ClientType>>' == 'Trust'`.
- Leave numeric comparisons unquoted: `<<Amount>> > 1000` — but this fails
  if the value is empty, so guard with `'<<Amount>>' != '' && ...`.
- Supported: arithmetic, comparison, `&&`/`||`/`!`, ternary `? :`, and NCalc
  built-ins. **No JavaScript objects, no moment.js here.** (Client-side
  `fba:formula` hints are a separate JavaScript evaluator — those *do*
  support moment.js. Don't confuse the two.)
- Values are interpolated raw (unformatted) in expression context.

## Gotchas worth remembering

- A misspelled tag silently becomes an empty string — validate output.
- Trailing separators are trimmed; leading separator only with the
  `[sep]`-before-name form and only when output is non-empty.
- Multiple elements sharing an autofillkey concatenate in simple-tag context.
- Curly/smart quotes (`‘’`) in filters are normalised to `'` — but write
  straight quotes anyway.
- Newlines and tabs are stripped from expressions before evaluation.
