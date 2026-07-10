# Integration map format — exact semantics

Distilled from the map evaluation engine (`FormsByAir.SDK/Extensions.cs`,
`ParseTags(Entity)` / `ToObject`) in the private FormsByAir.Web repository,
July 2026 snapshot. Maps drive "JSON From Map" / "XML From Map" file
deliveries and connector deliveries (e.g. the Adminis wealth platform).
Official samples: `references/docs/samples/json-map.json` →
`json-map-output.json`; worked production example:
`assets/example-integration-map.json`.

## Structure

A map is a JSON entity tree:

```json
{
  "Entities": [ { ...entity... } ],
  "Attributes": [ { ...attribute... } ]
}
```

**Entity**: `Name`, optional `Filter`, optional `ForEach`, optional
`Setter`, optional `Id`/`Getter` (connector-specific), `Attributes[]`,
nested `Entities[]`.

**Attribute**: `Name`, `Value`, optional `Filter`, optional `ForEach`,
optional `Setter`.

`Value` and `Filter` use the full tag syntax — see `tag-engine.md`. Filters
are NCalc boolean expressions with tags interpolated first.

## Evaluation order (what the engine actually does)

For each entity, attributes are processed first, then child entities:

1. **Attribute with `Filter`** — the filter is evaluated against the current
   scope. False → the attribute is **removed from the output entirely**
   (not emitted as null/empty).
2. **Attribute with `ForEach` + `Filter`** — scans the rows of the named
   repeater in order; `<<[Index]>>` in the filter is the **1-based** row
   number. The **first row whose filter passes** supplies the value (tags
   resolve against that row). No row passes → attribute removed.
3. **Attribute without filter** — always emitted; tags resolve against the
   current scope.
4. **Child entity with `Filter`** — false → the whole entity (and subtree)
   is removed.
5. **Child entity with `ForEach`** — the entity is a template: one clone is
   emitted per repeater row (per-row `Filter` optional), with tags inside
   resolving against that row (parent-scope escalation applies). Clones are
   appended **after** the non-ForEach siblings, in row order. Zero matching
   rows → nothing emitted.

### Conditional (if/else-if) attributes

Repeat the attribute `Name` with different `Filter`s; each is evaluated
independently and the failing ones are removed. Two rules:

- **Filters must be mutually exclusive.** If two variants both pass, both
  survive, and JSON output fails on the duplicate property name.
- **Cover the else case explicitly** (e.g. a final variant with the negated
  condition) or accept that the attribute is absent when nothing matches.

## Output shaping (`Setter`)

When the resolved entity tree is serialised to JSON:

| Setter | On | Effect |
|---|---|---|
| *(none)* | attribute | String property; empty string stays `""`. |
| `float` | attribute | Numeric property; empty value → `null`. |
| `boolean` | attribute | Boolean property; empty value → `false`. |
| *(none)* | entity | Nested object keyed by `Name`. |
| `array` | entity | All same-`Name` entities collected into a JSON array — required on `ForEach` entities when the target expects an array. |

## Scope and tag resolution

- At the top level, tags resolve against the whole document.
- Inside a `ForEach` entity or attribute row, tags resolve against that row
  first, escalating to parent scope for anything not defined at row level
  (see `tag-engine.md` — Scope escalation).
- Delivery-time system tags (`<<[DocumentId]>>`, `<<[DocumentReference]>>`,
  `<<[DocumentDeliveryDateTime]>>`, ...) are valid in `Value`s.

## Connector maps vs file maps

The evaluation engine is identical; the difference is what consumes the
result. Generic file deliveries emit exactly the structure the map defines.
Connector deliveries (e.g. Adminis) read specific entity/attribute names
from the resolved map and translate them to the target API — so the set of
meaningful `Name`s is fixed by the connector, and inventing new names has no
effect. Reuse names from a working map for the same connector (see
`assets/example-integration-map.json`); don't guess.
