#!/usr/bin/env python3
"""New actual gauge-budget combinations; no old conjugacy target."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "results/R133-supplement-actual-conjugacy-density-transfer-for-complete-first-coefficient.md":
        "6527fa46ddc21ed3d3e8c6ce4bb1f39f2db816d9fff5684e6daf4f30951c46f4",
    "results/R133-supplement-strong-sign-density-conjugation-and-global-Cayley-return.md":
        "715f28768139356001ef66840939e4defa547f953a59caea613f3fc6d6841a76",
    "results/R144-supplement-all-angular-moving-phase-and-current-normalized-row.md":
        "48c9b94c7de508fe10296c418a52cd5b686abcd3017d7ef3ad24830a960fb29f",
    "results/R144-supplement-complete-physical-phase-secant-and-tame-Hessian.md":
        "150ab1f82954acfa146d4c8b448c4f841290ece5ad9b315a5c7bbfaa9337b373",
}


def main():
    for name, digest in PINS.items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    rows = []

    def less(label, a, b):
        a, b = F(a), F(b)
        assert a < b, (label, a, b)
        rows.append(dict(label=label, left=str(a), right=str(b), strict=True))

    def equal(label, a, b):
        a, b = F(a), F(b)
        assert a == b, (label, a, b)
        rows.append(dict(label=label, left=str(a), right=str(b), equal=True))

    r = F(32, 31)
    less("whole inverse second derivative", 4*r**3, F(9,2))
    less("whole inverse third derivative", 48*r**5+1024*r**4, 1280)
    less("complete H2 derivative norm squared",
         F(1,31)**2+2*F(9,2)**2+1280**2, 1281**2)
    equal("primitive and A1 embedding coefficient", F(5,4)*4, 5)
    equal("actual centre complete nonconstant A2 budget", 1+5*1281, 6406)
    equal("whole H3-radius-one budget", 6406+4, 6410)
    less("fixed common gauge budget ceiling", 6410, 8192)
    less("actual nearby gauge lower orientation",
         F(1,2), F(32,33)-F(1,10**8))
    less("actual nearby gauge upper orientation",
         F(32,31)+F(1,10**8), 2)
    less("same neighbourhood retains CP lower derivative",
         F(24,25), F(32,33)-F(1,10**8))
    print(json.dumps({
        "schema": "visible-flex-exact-nearby/GGB-saved-rational-majorants/v1",
        "new_comparisons": len(rows), "all_passed": True,
        "old_scientific_targets_executed": 0,
        "old_carriers_or_integrals_restored": 0,
        "pins": PINS, "records": rows,
        "scope": (
            "Actual nonempty PCT/PSC low gauge domain with L=8192; "
            "full actual lift and constant direction retained; independent "
            "H3 radius one plus CP C1 neighbourhood; no full core inverse."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()

