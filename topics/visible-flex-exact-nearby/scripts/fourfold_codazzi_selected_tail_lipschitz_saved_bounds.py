#!/usr/bin/env python3
"""New exact SLIP exponent combinations from complete SREG/GF bounds."""
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "results/R119-supplement-higher-regularity-of-selected-tail-and-local-uniqueness.md":
        "98724a93f890a0a33efefac41b5ba90eaf3e74df88433b55b6655790854a9b7c",
    "results/R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md":
        "22324541319baf7ab565cdbff922e35bf56904ffa8827083c0fcbaf4e54d0f81",
}

def main():
    for name, digest in PINS.items():
        assert sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
    rows = []
    def eq(name, left, right):
        assert left == right, (name, left, right)
        rows.append(dict(name=name, left=left, right=right, relation="="))
    def lt(name, left, right):
        assert left < right, (name, left, right)
        rows.append(dict(name=name, left=left, right=right, relation="<"))
    lt("other selected height in actual-reference low ball", -49999998+1, -49000000)
    eq("complete low absorption exponent", 16777216+25165824+3-49000000, -7056957)
    lt("complete low absorption below half", -7056957, -1)
    eq("complete high low-source absorption exponent", 16777216+25165824+5-49000000, -7056955)
    lt("complete high low-source absorption below one", -7056955, 0)
    lt("first inverse coefficient below second", 16777216, 71303172)
    eq("largest high source order", 1164+1734, 2898)
    eq("largest high parameter order", 1164+1735, 2899)
    lt("parameter cost inside actual value domain", 2899, 8193)
    lt("full source below actual height order", 2898, 2960)
    eq("actual low Lipschitz exponent", 16777216+1-44000000, -27222783)
    eq("common low Lipschitz exponent", -27222783+1, -27222782)
    eq("common high first exponent", 16777216-44000000+1, -27222783)
    eq("common high second exponent", 71303172+1-44000000+1, 27303174)
    eq("actual endpoint lift exponent", 6291456-57000000, -50708544)
    lt("complete endpoint lift below physical low budget", -50708544+2, -27222782+3)
    eq("physical nonmean height exponent", -27222782+3+1, -27222778)
    eq("normalized B-height exponent", -27222782-440, -27223222)
    print(json.dumps({
        "schema": "visible-flex-exact-nearby/SLIP-saved-exponents/v1",
        "all_passed": True, "new_comparisons": len(rows), "records": rows,
        "pins": PINS, "old_scientific_targets_executed": 0,
        "old_carriers_or_integrals_restored": 0,
        "scope": "Actual selected-tail Lipschitz estimates on original parameter domain; no parameter C1 or arbitrary-source inverse."
    }, indent=2))

if __name__ == "__main__":
    main()
