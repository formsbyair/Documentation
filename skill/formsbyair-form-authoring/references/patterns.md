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

## Repeating group (repeater)

`maxOccurs="unbounded"` on the repeated group element. `format` `inline`
renders rows inline. Repeated groups end with the standard attribute trio.

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
  </xs:complexType>
</xs:element>
```

For a full worked example see `assets/example-retail-investment-v5.xsd`
(Retail Investment Application v5 — sections, branches per entity type,
repeaters, lookups, FATCA/CRS validation switches).
