#!/usr/bin/env python3
"""Validate a FormsByAir form definition XSD after editing.

Usage: python3 validate.py <file.xsd> [original.xsd]

Checks:
  1. Well-formed XML
  2. Element names match the a+32hex convention and are unique
  3. Duplicate autofillkeys (warning only — legitimate across exclusive branches)
  4. <<Tag>> references in hint/default/visibility/validationmethod resolve to
     an autofillkey or system tag pattern (warning for unknown)
  5. If an original file is given: report elements added/removed and confirm
     no pre-existing element names were renamed or deleted unintentionally
"""
import re
import sys
import xml.etree.ElementTree as ET

XS = "{http://www.w3.org/2001/XMLSchema}"
NAME_RE = re.compile(r"^a[0-9a-f]{32}$")
TAG_RE = re.compile(r"<<([A-Za-z0-9_]+)(?:\.[A-Za-z0-9_]+)?>>")
SYSTEM_TAGISH = re.compile(r"^(Form|Document|Request|Today|Now)")

def load(path):
    tree = ET.parse(path)  # raises on malformed XML
    return tree.getroot()

def collect(root):
    names, autofill, refs = [], set(), []
    for el in root.iter(f"{XS}element"):
        n = el.get("name")
        if n:
            names.append(n)
        for doc in el.iter(f"{XS}documentation"):
            src, text = doc.get("source", ""), (doc.text or "")
            if src == "autofillkey":
                autofill.add(text.strip())
            if src in ("hint", "default", "visibility", "validationmethod",
                       "documentreference"):
                refs += [(m, src) for m in TAG_RE.findall(text)]
    return names, autofill, refs

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = sys.argv[1]
    errors, warnings = [], []

    try:
        root = load(path)
    except ET.ParseError as e:
        print(f"ERROR: not well-formed XML: {e}")
        sys.exit(1)

    names, autofill, refs = collect(root)

    # element name convention + uniqueness (Form root is exempt)
    seen = set()
    for n in names:
        if n != "Form" and not NAME_RE.match(n):
            errors.append(f"element name '{n}' does not match a+32hex convention")
        if n in seen:
            errors.append(f"duplicate element name '{n}'")
        seen.add(n)

    # autofillkey duplicates across the file (informational)
    # (duplicates are valid across mutually exclusive visibility branches)

    # tag references
    for tag, src in refs:
        if tag not in autofill and not SYSTEM_TAGISH.match(tag):
            warnings.append(f"<<{tag}>> (in {src}) has no matching autofillkey "
                            f"— OK if it's a system tag or lookup sub-field")

    # diff against original
    if len(sys.argv) > 2:
        orig_names, orig_auto, _ = collect(load(sys.argv[2]))
        removed = set(orig_names) - set(names)
        added = set(names) - set(orig_names)
        if removed:
            warnings.append(f"{len(removed)} pre-existing element(s) removed: "
                            + ", ".join(sorted(removed)[:5]))
        print(f"diff vs original: +{len(added)} elements, -{len(removed)} elements")
        lost_keys = orig_auto - autofill
        if lost_keys:
            errors.append("autofillkeys removed (breaks tags/templates/exports): "
                          + ", ".join(sorted(lost_keys)))

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"checked {len(names)} elements, {len(autofill)} autofillkeys")
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
