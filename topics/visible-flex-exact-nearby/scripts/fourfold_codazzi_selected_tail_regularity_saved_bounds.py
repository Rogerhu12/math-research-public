#!/usr/bin/env python3
"""New exact SREG exponent arithmetic, without any old scientific work."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "results/R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md":
        "aba52db835e318f65dd9bf40c77e084eae28d804a4b8669b503b9f663bf7f736",
    "results/R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md":
        "0ada0f964d63212362f02c1f050da271d88ac6f585dc595bb779287c76b0e226",
    "results/R119-supplement-reference-graph-approximate-right-inverse-and-exact-port-defects.md":
        "2bcb7d4eadd4c08efb9a0c2ffab3d0943411d8357cbd824c2b6c2e38c0103e26",
    "results/R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md":
        "0103391542006e68070dddd936d1d498dab3810da2f6525010da842e5fccaf81",
}


def main():
    for name, digest in PINS.items():
        assert sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    rows = []

    def equal(label, a, b):
        a, b = F(a), F(b)
        assert a == b, (label, a, b)
        rows.append(dict(label=label, left=str(a), right=str(b), equal=True))

    def less(label, a, b):
        a, b = F(a), F(b)
        assert a < b, (label, a, b)
        rows.append(dict(label=label, left=str(a), right=str(b), strict=True))

    equal("whole graph interpolation index gap", 6396-1856, 4540)
    equal("whole correction exponent gap", 3274+1266, 4540)
    equal("actual convergence-order endpoint", 1856+1266, 3122)
    equal("order2960 decay exponent", 3122-2960, 162)
    equal("order2960 complete tail logarithm",
          1+184549390-162*1500000, -58450609)
    less("tail smaller than common seed budget exponent",
         -58450609, -49999999)
    equal("common seed plus tail dyadic ceiling exponent",
          -49999999+1, -49999998)
    less("geometric ratio exponent versus one half", -1500000//4, -1)
    less("Cstar above reference and high-sum allowance",
         184549388-4+2, 184549390)
    less("selected solution strictly inside local uniqueness ball",
         -49999998, -49000000)
    less("local uniqueness ball inside original half low ball",
         -49000000, -33554433)
    equal("full low inverse and quadratic coefficients",
          16777216+25165824, 41943040)
    less("quadratic sum coefficient below dyadic allowance", 5, 8)
    equal("complete absorption exponent",
          41943040+3-49000000, -7056957)
    less("complete absorption strictly below one half", -7056957, -1)
    equal("highest new background order", 1164+1796, 2960)
    equal("highest complete external state order", 1164+1780, 2944)
    equal("highest actual physical-height order", 1164+1782, 2946)
    equal("highest residual-sensitive source order", 1164+1734+1, 2899)
    less("physical height below actual direction budget", 2946, 2960)
    equal("complete higher inverse coefficient exponent",
          67108864+2*(2097152+1)+1, 71303171)
    less("chosen higher inverse coefficient ceiling", 71303171, 71303172)
    print(json.dumps({
        "schema": "visible-flex-exact-nearby/SREG-saved-rational-majorants/v1",
        "new_comparisons": len(rows), "all_passed": True,
        "old_scientific_targets_executed": 0,
        "old_carriers_or_integrals_restored": 0,
        "pins": PINS, "records": rows,
        "scope": (
            "Same selected tail: higher finite graph regularity and continuity, "
            "exact-limit a priori linear estimates and fixed-gamma local "
            "uniqueness; no gamma differentiability or core existence."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()

