# FormsByAir XSD Canonical Patterns

Copy these shapes when adding elements. Every element name is an opaque ID:
lowercase `a` followed by 32 hex characters, unique within the file.
Generate new ones with `python3 -c "import uuid; print('a'+uuid.uuid4().hex)"`.
The human-meaningful identity lives in `prompt`/`title`/`autofillkey`.

All elements are `nillable="true"`. Required fields add `minOccurs="1"`.

## Simple text field (required)

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true" type="xs:string">
  <xs:annotation>
    <xs:documentation source="prompt">Name of Trust</xs:documentation>
    <xs:documentation source="autofillkey">ClientName</xs:documentation>
  </xs:annotation>
</xs:element>
```

## Checkbox (boolean acknowledgement)

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true" type="xs:boolean">
  <xs:annotation>
    <xs:documentation source="prompt">I have read and understand the terms</xs:documentation>
    <xs:documentation source="autofillkey">AcknowledgePDS</xs:documentation>
  </xs:annotation>
</xs:element>
```

## Dropdown / radio / toggle

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">Investor Type</xs:documentation>
    <xs:documentation source="autofillkey">ClientType</xs:documentation>
    <xs:documentation source="listtype">dropdown</xs:documentation>
  </xs:annotation>
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:enumeration value="Trust">
        <xs:annotation>
          <xs:documentation source="name">Trust</xs:documentation>
        </xs:annotation>
      </xs:enumeration>
      <!-- more enumerations -->
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

## Yes/No question list (right-aligned options via width 2)

For a list of several yes/no questions rendered as an inline radio or
inline toggle with longer text prompts, set `width` to `2` on each
question. This aligns the Yes/No options to the right-hand side of the
12-column grid and minimises text wrapping of the question prompt.

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">Omitted income that ought to have been included in a return</xs:documentation>
    <xs:documentation source="autofillkey">IncomeTax1</xs:documentation>
    <xs:documentation source="listtype">toggle</xs:documentation>
    <xs:documentation source="width">2</xs:documentation>
  </xs:annotation>
  <xs:simpleType>
    <xs:restriction base="xs:string">
      <xs:enumeration value="Yes">
        <xs:annotation>
          <xs:documentation source="name">Yes</xs:documentation>
        </xs:annotation>
      </xs:enumeration>
      <xs:enumeration value="No">
        <xs:annotation>
          <xs:documentation source="name">No</xs:documentation>
        </xs:annotation>
      </xs:enumeration>
    </xs:restriction>
  </xs:simpleType>
</xs:element>
```

## Attachment question with a longer prompt (full-width via width 12)

For one or more attachment questions with a longer text prompt, set
`width` to `12` so the "select file" button and the selected filename
always appear on the next line below the prompt.

```xml
<xs:element name="aNEWID" nillable="true" type="fba:attachment">
  <xs:annotation>
    <xs:documentation source="prompt">Proof of residential address (dated within the last 3 months)</xs:documentation>
    <xs:documentation source="autofillkey">DocProofOfResidentialAddress</xs:documentation>
    <xs:documentation source="width">12</xs:documentation>
  </xs:annotation>
</xs:element>
```

## Conditional branch (visibility)

A group shown only when a controlling question has a given value.
The condition group must be a **child of the question it switches on** —
not a sibling. The controlling question becomes a complex element: its
condition branches go in the `<xs:sequence>`, and its own value moves to
an `<xs:attribute name="value">` (which carries the enumerated simpleType
for a list question, or `xs:boolean` for a checkbox). `visibility` holds
the matching enumeration value (or `True`/`False` for a boolean parent).

List question with condition branches as children:

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">Investor Type</xs:documentation>
    <xs:documentation source="autofillkey">ClientType</xs:documentation>
    <xs:documentation source="listtype">toggle</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element name="aNEWID2" nillable="true">
        <xs:annotation>
          <xs:documentation source="visibility">Trust</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence>
            <!-- fields shown only for Trust -->
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <!-- more branches -->
    </xs:sequence>
    <xs:attribute name="value">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="Trust">
            <xs:annotation>
              <xs:documentation source="name">Trust</xs:documentation>
            </xs:annotation>
          </xs:enumeration>
          <!-- more enumerations -->
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
</xs:element>
```

Boolean (checkbox) question with a condition branch as child:

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">Street address is different from postal address</xs:documentation>
    <xs:documentation source="autofillkey">StreetAddressDifferent</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element name="aNEWID2" nillable="true">
        <xs:annotation>
          <xs:documentation source="visibility">True</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence><!-- fields shown when ticked --></xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="value" type="xs:boolean" />
  </xs:complexType>
</xs:element>
```

## Formula-driven switch (conditional on an expression)

When the condition is an expression rather than an option's value: a hidden
group evaluates a formula, and child branch groups carry `visibility` values
matching the formula result (`true`/`false`).

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">hide if no middle name</xs:documentation>
    <xs:documentation source="hint">'&lt;&lt;NoMiddleName&gt;&gt;' != 'true'</xs:documentation>
    <xs:documentation source="hidden">True</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element name="aNEWID2" nillable="true">
        <xs:annotation>
          <xs:documentation source="visibility">true</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence><!-- shown when formula is true --></xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="aNEWID3" nillable="true">
        <xs:annotation>
          <xs:documentation source="visibility">false</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence><!-- shown when formula is false --></xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="value" type="fba:formula" />
  </xs:complexType>
</xs:element>
```

The same autofillkey may legitimately appear once per mutually exclusive
branch (e.g. `PersonMiddleNames` as a visible field in the `true` branch and
a hidden formula in the `false` branch) so downstream tags always resolve.

## Hidden formula field

Computed value; expression in `hint`, JavaScript-compatible, `<<Tag>>`
references resolve to autofillkey values (quote string comparisons).

```xml
<xs:element name="aNEWID" nillable="true" type="fba:formula">
  <xs:annotation>
    <xs:documentation source="prompt">Mandatory Role</xs:documentation>
    <xs:documentation source="autofillkey">MandatoryRole</xs:documentation>
    <xs:documentation source="hint">'Trustee'</xs:documentation>
    <xs:documentation source="hidden">True</xs:documentation>
  </xs:annotation>
</xs:element>
```

Date-difference example (age check): `moment().diff(moment('<<PersonDateOfBirth>>'), 'years') >= 75`

## Validation switch (hidden formula that must evaluate true)

```xml
<xs:element name="aNEWID" nillable="true" type="fba:formula">
  <xs:annotation>
    <xs:documentation source="prompt">Validate TIN</xs:documentation>
    <xs:documentation source="hint">'&lt;&lt;ENoTIN&gt;&gt;' == 'true'</xs:documentation>
    <xs:documentation source="validationmethod">expression</xs:documentation>
    <xs:documentation source="validationmessage">You must enter a TIN or select "No TIN Number"</xs:documentation>
    <xs:documentation source="validationinline">False</xs:documentation>
    <xs:documentation source="hidden">True</xs:documentation>
  </xs:annotation>
</xs:element>
```

## Eligibility hard-stop (blocking validation)

The standard pattern for blocking a user who gives a disqualifying answer —
typically an eligibility question. Nest a validation switch whose expression
is the literal `false` inside the condition branch of the disqualifying
answer. When the branch becomes visible the validation can never pass, so
the red alert shows **immediately** (not on Next/submit) and the user is
blocked from moving forward or submitting. The `validationmessage` is the
text shown in the alert.

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">Are you eligible</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element name="aNEWID2" nillable="true">
        <xs:annotation>
          <xs:documentation source="visibility">No</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence>
            <xs:element name="aNEWID3" nillable="true" type="fba:formula">
              <xs:annotation>
                <xs:documentation source="prompt">Validation</xs:documentation>
                <xs:documentation source="hint">false</xs:documentation>
                <xs:documentation source="validationmethod">expression</xs:documentation>
                <xs:documentation source="validationmessage">You can't proceed with the form</xs:documentation>
                <xs:documentation source="validationinline">False</xs:documentation>
                <xs:documentation source="hidden">True</xs:documentation>
              </xs:annotation>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="value">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:enumeration value="Yes" />
          <xs:enumeration value="No" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
</xs:element>
```

## Repeating group (repeater)

`maxOccurs="unbounded"` on the repeated group element. Repeated groups end
with the standard attribute trio.

**A repeater's direct parent must be a group** (with the repeater as the
group's only child — the builder enforces the only-child part). The form
renderer takes each row's index from the parent group's iteration, so a
repeater placed directly inside a condition branch renders every row
header as *"Title #NaN"*. When a repeater belongs inside a condition
branch, wrap it in a group with `hidden` = `True`: on a **group**,
`hidden` suppresses only the heading (title, rule, note) — the children
still render and the row index is supplied. This is the canonical shape in
the production templates (the hidden "Relationships" / "Documents" wrapper
groups in the investment examples).

```xml
<xs:element minOccurs="1" maxOccurs="unbounded" name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="title">Document</xs:documentation>
    <xs:documentation source="format">inline</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="1" name="aNEWID2" nillable="true" type="fba:attachment">
        <xs:annotation>
          <xs:documentation source="prompt">Attachment</xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="value" type="xs:string" />
    <xs:attribute name="documentdeliveryid" type="xs:string" />
    <xs:attribute name="trycount" type="xs:string" />
  </xs:complexType>
</xs:element>
```

### Row-count bounds — `min` / `limit` accept expressions

`min` and `limit` annotations on the repeater element are evaluated as
JavaScript expressions (tags allowed), not just constants. `min` auto-adds
rows up to the result and blocks Remove below it; `limit` trims excess
rows and hides the Add button at the cap. Set both to the same expression
to pin the row count to another answer:

```xml
<xs:documentation source="min">'&lt;&lt;ApplicationType&gt;&gt;' == 'Joint' ? 2 : 1</xs:documentation>
<xs:documentation source="limit">'&lt;&lt;ApplicationType&gt;&gt;' == 'Joint' ? 2 : 1</xs:documentation>
```

### Row layout — `format` `inline` vs `table`

`format` `inline` lays row fields out with narrow default columns (a lone
field gets 8 of the 12 grid columns, two fields get 6 each, three or more
get only 2 each — per-field `width` overrides), so rows with three or more
fields wrap onto extra lines. `format` `table` uses the full 12-column
grid driven by each field's `width` annotation and renders the field
prompts once as column headers above the first row — prefer it for rows
of three or more fields (e.g. three fields at `width` 4). Conditional
paths are not supported inside either format (builder rule).

## Linked repeater (rows track another repeater)

A repeater with `linkedrepeater` = the **autofillkey of another repeater**
keeps its rows in lockstep with that repeater: row *n* pairs with row *n*,
rows are created and removed automatically, and the user gets no
Add/Remove controls. Inside a row, tags escalate to the **linked parent
row**, so a tag like `<<ApplicantFirstName>>` resolves to that row's
person. A `title` containing `<<tags>>` is parsed per row (falling back to
`AutofillKey #n` while empty), so the row header can show the person's
name. Use `maxOccurs="unbounded"` without `minOccurs`, wrapped in a
(hidden) group as usual. Canonical use: one signature block per applicant
at the end of a form — the rows automatically match the number of
applicants.

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="title">Applicants</xs:documentation>
    <xs:documentation source="hidden">True</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element maxOccurs="unbounded" name="aNEWID2" nillable="true">
        <xs:annotation>
          <xs:documentation source="autofillkey">ApplicantSignature</xs:documentation>
          <xs:documentation source="title">&lt;&lt;ApplicantFirstName&gt;&gt; &lt;&lt;ApplicantLastName&gt;&gt;</xs:documentation>
          <xs:documentation source="linkedrepeater">Applicant</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="1" name="aNEWID3" nillable="true" type="fba:signature">
              <xs:annotation>
                <xs:documentation source="prompt">Signature</xs:documentation>
                <xs:documentation source="autofillkey">Signature</xs:documentation>
              </xs:annotation>
            </xs:element>
            <xs:element minOccurs="1" name="aNEWID4" nillable="true" type="xs:date">
              <xs:annotation>
                <xs:documentation source="prompt">Date</xs:documentation>
                <xs:documentation source="autofillkey">SignatureDate</xs:documentation>
                <!-- no default — populated automatically on signing -->
              </xs:annotation>
            </xs:element>
          </xs:sequence>
          <xs:attribute name="value" type="xs:string" />
          <xs:attribute name="documentdeliveryid" type="xs:string" />
          <xs:attribute name="trycount" type="xs:string" />
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## Third-party request block

A Request element lets a third party complete part of the form via a
unique link (`docs/forms/elements/request.md`). It wraps the content the
third party completes; in a multi-person repeater, place it at the top of
the row wrapping the per-person content. On a Request element `hidden` =
`True` is the builder's **Hide First** option: within a repeater it
suppresses the "send them a request" prompt on the first row only, since
the first person is generally the main form filler. `minOccurs="1"` makes
the request mandatory (the main filler cannot complete that part
themselves) — usually omitted. Include a hidden formula with autofillkey
`RequestEmailMessage` so the filler's optional message reaches the
On-Third-Party-Request email integration; the email-address prefill comes
from that integration's recipient tag setting, not the XSD. Requests end
with a value / requestdocumentid / completed attribute trio.

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="title">Request</xs:documentation>
    <xs:documentation source="hidden">True</xs:documentation>
    <xs:documentation source="request">request</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <!-- content the third party completes -->
      <xs:element name="aNEWID2" nillable="true" type="fba:formula">
        <xs:annotation>
          <xs:documentation source="prompt">Request Email Message</xs:documentation>
          <xs:documentation source="autofillkey">RequestEmailMessage</xs:documentation>
          <xs:documentation source="hidden">True</xs:documentation>
        </xs:annotation>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="value" type="xs:string" />
    <xs:attribute name="requestdocumentid" type="xs:string" />
    <xs:attribute name="completed" type="xs:string" />
  </xs:complexType>
</xs:element>
```

## Validation service block (identity verification etc.)

A validation-service element posts its contents to a connected service —
identity verification (Cloudcheck, APLYiD), bank account checks, and
similar. `format` `post` sends after submit rather than on section
navigation; `attachresponse` `True` attaches the service response to the
document. Wrap the fields the service needs (names, date of birth,
address...) inside the element's sequence — in a multi-person form, put
one at the root of each person's content (inside the Request block when
there is one). Leave `subscriptionid` off when authoring; the service is
connected in the builder. Validation services end with an extended
attribute set.

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="autofillkey">Verification</xs:documentation>
    <xs:documentation source="title">Verification</xs:documentation>
    <xs:documentation source="format">post</xs:documentation>
    <xs:documentation source="attachresponse">True</xs:documentation>
    <xs:documentation source="validationService">validationService</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <!-- fields the service validates -->
    </xs:sequence>
    <xs:attribute name="value" type="xs:string" />
    <xs:attribute name="documentdeliveryid" type="xs:string" />
    <xs:attribute name="trycount" type="xs:string" />
    <xs:attribute name="data" type="xs:string" />
    <xs:attribute name="message" type="xs:string" />
    <xs:attribute name="reference" type="xs:string" />
    <xs:attribute name="datetime" type="xs:string" />
  </xs:complexType>
</xs:element>
```

## Signature with date

A Date field that immediately follows a Signature element must be left
**blank by default** — do NOT set `default` to `=DateTime.Today` or any
other value. The form app has logic that populates the date automatically
when a signature is entered.

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true" type="fba:signature">
  <xs:annotation>
    <xs:documentation source="prompt">Signature</xs:documentation>
    <xs:documentation source="autofillkey">Signature</xs:documentation>
  </xs:annotation>
</xs:element>
<xs:element minOccurs="1" name="aNEWID2" nillable="true" type="xs:date">
  <xs:annotation>
    <xs:documentation source="prompt">Date</xs:documentation>
    <xs:documentation source="autofillkey">SignatureDate</xs:documentation>
    <!-- no default — populated automatically on signing -->
  </xs:annotation>
</xs:element>
```

## Single-line address — addressPicker (Google lookup)

The default for any non-NZ single-line address question. Needs no service
subscription. (NZ addresses instead use a `fba:typeahead` connected to an
NZ address service — see the address principle in SKILL.md.)

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true" type="fba:addressPicker">
  <xs:annotation>
    <xs:documentation source="prompt">Residential address</xs:documentation>
    <xs:documentation source="autofillkey">ResidentialAddress</xs:documentation>
  </xs:annotation>
</xs:element>
```

## Country question — typeahead on the built-in Countries table

Any country / jurisdiction question (country of incorporation,
tax-residency jurisdiction, country of organisation) is a typeahead bound
to FormsByAir's built-in Countries table. This `tableid` is present in
every account and is the one GUID that may be hardcoded without asking.
Nationality questions ("Singaporean") stay plain text.

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true" type="fba:typeahead">
  <xs:annotation>
    <xs:documentation source="prompt">Country of incorporation</xs:documentation>
    <xs:documentation source="autofillkey">IncorporationCountry</xs:documentation>
    <xs:documentation source="tableid">4a263fa0-06a7-41c9-a2bb-34cce4d0258c</xs:documentation>
  </xs:annotation>
</xs:element>
```

## Typeahead with external lookup (e.g. Companies Office)

```xml
<xs:element minOccurs="1" name="aNEWID" nillable="true" type="fba:typeahead">
  <xs:annotation>
    <xs:documentation source="prompt">Company Name</xs:documentation>
    <xs:documentation source="autofillkey">ClientName</xs:documentation>
    <xs:documentation source="hint">Start typing a company name to lookup, or enter manually</xs:documentation>
    <xs:documentation source="allowmanualentry">True</xs:documentation>
    <xs:documentation source="matchstart">False</xs:documentation>
    <xs:documentation source="getextendeddata">True</xs:documentation>
    <xs:documentation source="subscriptionid">EXISTING-SUBSCRIPTION-GUID</xs:documentation>
  </xs:annotation>
</xs:element>
```

Extended data from the lookup is referenced as `'<<Key.SubField>>'`,
e.g. a sibling field defaulting to `'<<ClientName.NZBN>>'`. The available
sub-property names per integration are defined in
`references/integration-models.swagger.json` — check there rather than
guessing (for MBIE entities prefer `NZBN` over `CompanyNumber`, which only
exists for companies).
Never invent `subscriptionid`/`tableid` GUIDs — reuse ones already in the
form or ask the user for the correct ID.

## Section (top-level page)

Sections end with a `value` / `completed` / `data` attribute trio (the
platform serializer emits these on every section).

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="title">Application</xs:documentation>
    <xs:documentation source="section">section</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <!-- groups and fields -->
    </xs:sequence>
    <xs:attribute name="value" type="xs:string" />
    <xs:attribute name="completed" type="xs:string" />
    <xs:attribute name="data" type="xs:string" />
  </xs:complexType>
</xs:element>
```

## Conditional (dynamic) section — wizard steps that appear per answer

Whole sections can be conditional. Place a hidden formula switch **at the
top level of the form** (a direct child of the root `Form` element's
`<xs:sequence>`, alongside the other sections) and nest the section(s)
inside its condition branch. The section renders as a wizard step only
when the formula result matches the branch's `visibility` value — this is
how one form shows different steps per applicant/investor type.

```xml
<xs:element name="aNEWID" nillable="true">
  <xs:annotation>
    <xs:documentation source="prompt">Wholesale Investor</xs:documentation>
    <xs:documentation source="hint">'&lt;&lt;InvestorType&gt;&gt;' == 'wholesale'</xs:documentation>
    <xs:documentation source="hidden">True</xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:sequence>
      <xs:element name="aNEWID2" nillable="true">
        <xs:annotation>
          <xs:documentation source="visibility">true</xs:documentation>
        </xs:annotation>
        <xs:complexType>
          <xs:sequence>
            <!-- one or more full sections, shown only when the formula matches -->
            <xs:element name="aNEWID3" nillable="true">
              <xs:annotation>
                <xs:documentation source="title">Certification</xs:documentation>
                <xs:documentation source="section">section</xs:documentation>
              </xs:annotation>
              <xs:complexType>
                <xs:sequence><!-- groups and fields --></xs:sequence>
                <xs:attribute name="value" type="xs:string" />
                <xs:attribute name="completed" type="xs:string" />
                <xs:attribute name="data" type="xs:string" />
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="value" type="fba:formula" />
  </xs:complexType>
</xs:element>
```

A branch may hold multiple sections (several consecutive steps switched
together), and one switch may carry several branches showing different
sections per value (e.g. a group flag routing an individual step vs. two
entity steps). Live instances: the top-level "Wholesale Investor" and
"Other Investor" switches wrapping the Certification sections in
`assets/example-wholesale-investment-v1.xsd`.

For a full worked example see `assets/example-retail-investment-v5.xsd`
(Retail Investment Application v5 — sections, branches per entity type,
repeaters, lookups, FATCA/CRS validation switches) and
`assets/example-wholesale-investment-v1.xsd` (Wholesale Investment
Application v1 — dynamic sections via top-level formula switches,
certification categories per investor type).
