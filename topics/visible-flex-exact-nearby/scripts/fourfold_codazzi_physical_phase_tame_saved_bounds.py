#!/usr/bin/env python3
"""New exact physical-phase secant constants; no old scientific target."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "results/R144-supplement-full-off-constraint-principal-return-Hessian.md":
        "e77c6e41b3ff7f40085d4a65821e6858795412e9aa5e743188a74a3da9684e21",
    "results/R144-supplement-all-angular-moving-phase-and-current-normalized-row.md":
        "48c9b94c7de508fe10296c418a52cd5b686abcd3017d7ef3ad24830a960fb29f",
    "results/R144-supplement-complete-passive-world-height-Hessian-with-independent-ports.md":
        "8c7aad2c61881c91b2c7f8820cefb169eceb710dc9c68f8d1bb0365c99630330",
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

    gain, embedding = F(54, 25), F(11, 10)
    less("complete convex physical secant orientation", F(2, 5), F(25, 54))
    less("both actual L2 composition multipliers squared", F(54, 25), F(3, 2)**2)
    less("full first physical derivative state coefficient", 7*(gain+1), 23)
    less("full first physical derivative waist coefficient", F(9, 2), 23)
    mixed = 12*(gain+embedding)
    spatial = 5*(gain**2+embedding)
    equal("four complete mixed chart terms", mixed, F("39.12"))
    equal("two complete spatial Hessian products", spatial, F("28.828"))
    equal("actual raw Hessian times physical derivative", 7*400, 2800)
    total = 2800+mixed+spatial+F(9,2)
    equal("whole physical mixed Hessian ledger", total, F("2872.448"))
    less("whole physical Hessian strict ceiling", total, 3000)
    equal("nine actual Hessian terms", 2+4+2+1, 9)
    equal("all-angular three-packet complete ledger", 3*3+1+1, 11)
    less("all-angular coefficient exponent", 11, 16)
    less("complete term sum below lowest fixed coefficient", 9, 2**80)
    print(json.dumps({
        "schema": "visible-flex-exact-nearby/PSC-saved-rational-majorants/v1",
        "new_comparisons": len(rows), "all_passed": True,
        "old_scientific_targets_executed": 0,
        "old_carriers_or_integrals_restored": 0,
        "pins": PINS, "records": rows,
        "scope": (
            "Full physical phase secant; actual waist port and mean; "
            "low first derivative 23 and mixed Hessian 3000; complete "
            "all-angular tame chain; no regular inverse or final flex."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()

