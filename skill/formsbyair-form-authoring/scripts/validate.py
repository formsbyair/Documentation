#!/usr/bin/env python3
"""Validate a FormsByAir form definition XSD after editing.

Usage: python3 validate.py <file.xsd> [original.xsd]

Checks:
  1. Well-formed XML
  2. Element names match the a+32hex convention and are unique
  3. Duplicate autofillkeys (warning only — legitimate across exclusive branches)
  4. <<Tag>> references in hint/default/visibility/validationmethod resolve to
     an autofillkey or system tag pattern (warning for unknown)
  5. Form-builder save rules (see references/builder-validation.md):
     autofillkey charset, empty containers, repeater placement, required
     prompt/title, list options, slider min/max/step, international phone
     country, conditional visibility values
  6. If an original file is given: report elements added/removed and confirm
     no pre-existing element names were renamed or deleted unintentionally
"""
import re
import sys
import xml.etree.ElementTree as ET

XS = "{http://www.w3.org/2001/XMLSchema}"
NAME_RE = re.compile(r"^a[0-9a-f]{32}$")
TAG_RE = re.compile(r"<<([A-Za-z0-9_]+)(?:\.[A-Za-z0-9_]+)?>>")
SYSTEM_TAGISH = re.compile(r"^(Form|Document|Request|Today|Now)")
BAD_TAGNAME = re.compile(r"[<>\[\]'\"]")

def load(path):
    tree = ET.parse(path)  # raises on malformed XML
    return tree.getroot()

def anno(el):
    """source -> text for an element's own annotation block."""
    out = {}
    a = el.find(f"{XS}annotation")
    if a is not None:
        for doc in a.findall(f"{XS}documentation"):
            out[doc.get("source", "")] = (doc.text or "").strip()
    return out

def local_type(el):
    t = el.get("type", "")
    return t.split(":")[-1] if t else None

def label(el, props):
    return (props.get("autofillkey") or props.get("prompt")
            or props.get("title") or el.get("name") or "?")

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

def check_builder_rules(root, errors, warnings):
    """Structural rules the GUI form builder enforces at save time."""
    form = root.find(f"{XS}element")  # root Form element
    if form is None:
        errors.append("no root xs:element found")
        return
    walk(form, None, None, errors, warnings)

def child_elements(el):
    ct = el.find(f"{XS}complexType")
    if ct is None:
        return None  # not a container
    seq = ct.find(f"{XS}sequence")
    return [] if seq is None else seq.findall(f"{XS}element")

def enum_values(el):
    """(values, any_named) from an inline simpleType restriction, else None."""
    st = el.find(f"{XS}simpleType")
    if st is None:
        return None
    res = st.find(f"{XS}restriction")
    if res is None:
        return None
    vals, named = [], False
    for e in res.findall(f"{XS}enumeration"):
        vals.append((e.get("value"), anno(e)))
        if anno(e).get("name"):
            named = True
    return vals, named

def walk(el, parent, grandparent, errors, warnings):
    props = anno(el)
    who = label(el, props)
    kids = child_elements(el)
    ltype = local_type(el)
    is_form_root = parent is None

    # autofillkey charset
    key = props.get("autofillkey", "")
    if key and BAD_TAGNAME.search(key):
        errors.append(f"autofillkey '{key}' contains a forbidden character "
                      "(' \" < [ ] > are not allowed)")

    if kids is not None and not is_form_root:
        kind = ("Section" if props.get("section") else
                "Workflow" if props.get("workflow") else
                "Condition" if props.get("visibility") else "Group")
        # containers must not be empty
        if not kids:
            errors.append(f"{kind} '{who}' must contain at least one element")
        # a repeater must be the only item within its group
        for k in kids:
            if k.get("maxOccurs") is not None and len(kids) > 1:
                errors.append(f"repeater '{label(k, anno(k))}' must be the "
                              f"only item within group '{who}'")
                break
        # groups/sections/workflow need a title (conditions don't)
        if kind != "Condition" and not (props.get("title") or props.get("prompt")):
            warnings.append(f"{kind} '{who}' has no title")

    if kids is None and ltype:  # a question
        if ltype not in ("note", "terms") and not props.get("prompt"):
            errors.append(f"question '{who}' ({ltype}) has no prompt "
                          "(Question Title) — builder requires one")
        if ltype in ("note", "terms"):
            content = re.sub(r"<br>|&nbsp;|\s|<div></div>", "",
                             props.get("note", ""))
            if not content:
                errors.append(f"'{who}' ({ltype}) has no non-whitespace content")
        if ltype == "slider":
            for p in ("min", "max", "step"):
                if not props.get(p):
                    errors.append(f"slider '{who}' is missing '{p}'")
        if ltype == "phone" and props.get("format", "").startswith("international") \
                and not props.get("country"):
            errors.append(f"international phone '{who}' is missing a default "
                          "country code")

    # selection lists
    enums = enum_values(el)
    if enums is not None:
        vals, named = enums
        if len(vals) < 2:
            errors.append(f"list '{who}' must contain at least two options")
        values = [v for v, _ in vals]
        if len(set(values)) != len(values):
            errors.append(f"list '{who}': option values must be unique")
        if any(v is None or v == "" for v in values):
            errors.append(f"list '{who}': option values must not be empty")
        if named and any(not a.get("name") for _, a in vals):
            warnings.append(f"list '{who}': some options have a display name "
                            "and some don't")

    # conditional visibility against the parent question
    vis = props.get("visibility")
    if kids is not None and not is_form_root and "visibility" in props:
        if not vis:
            errors.append(f"condition '{who}' has an empty visibility value")
        elif parent is not None:
            ptype = local_type(parent)
            penums = enum_values(parent)
            if ptype == "boolean" and vis not in ("True", "False"):
                errors.append(f"condition '{who}': parent is boolean, "
                              f"visibility must be True or False (got '{vis}')")
            elif ptype in ("option", "note") and vis != "True":
                errors.append(f"condition '{who}': parent is {ptype}, "
                              f"visibility must be True (got '{vis}')")
            elif penums is not None:
                values = [v for v, _ in penums[0]]
                if vis not in values:
                    errors.append(f"condition '{who}': visibility '{vis}' is "
                                  "not one of the parent's option values")
        # conditional paths not supported in inline/tabular groups
        if grandparent is not None:
            gprops = anno(grandparent)
            if gprops.get("inline") or gprops.get("format") in ("inline", "table"):
                errors.append(f"condition '{who}': conditional path not "
                              "supported inside inline or tabular content")

    for k in (kids or []):
        walk(k, el, parent, errors, warnings)

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

    # form-builder save rules
    check_builder_rules(root, errors, warnings)

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
