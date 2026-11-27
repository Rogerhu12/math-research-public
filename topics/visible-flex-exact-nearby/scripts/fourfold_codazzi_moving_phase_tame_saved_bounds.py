#!/usr/bin/env python3
"""New exact coefficient comparisons for PCT; no old scientific targets."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    "results/R144-supplement-all-angular-principal-return-tame-derivatives.md":
        "c1e8f82c3c319af2dafbbe0c563e51830740aaf807aae85dfd56111b0a14094b",
    "results/R133-supplement-complete-phase-row-approximate-inverse-and-quadratic-defect.md":
        "58bdf1739e1b3c98c50e096657502d30b14033f9ee2b81bbfda89652ddf14278",
    "results/R147-supplement-uniform-positive-phase-pivot-near-the-mean-exact-centre.md":
        "456269b6b9a53cfca2139b374d84adf6e650fe4a3a04b590535cd03731166775",
}


def main():
    for path, digest in PINS.items():
        assert sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    records = []

    def less(label, left, right):
        left, right = F(left), F(right)
        assert left < right, (label, left, right)
        records.append(dict(label=label, left=str(left), right=str(right),
                            strict=True))

    def equal(label, left, right):
        left, right = F(left), F(right)
        assert left == right, (label, left, right)
        records.append(dict(label=label, left=str(left), right=str(right),
                            equal=True))

    # sqrt(5) < 3 and pi < 4 are used in the complete lift bound.
    omega_upper = F(2*(5831714953207175+3), 21212218271020390)
    less("actual fixed lifted target rotation upper", omega_upper, 2)
    less("composition L2 change-of-variables squared", 2, 4)
    less("composition H1 real Jacobian multiplier squared", 8, 16)
    equal("A2 to H3 complete embedding coefficient", 2*2, 4)
    less("largest raw Hessian term count", 4, 8)
    less("complete normalized-row derivative term count", 7, 8)
    equal("largest complete product factor count", 5, 5)
    equal("five elementary-packet exponent cost", 5*3, 15)
    equal("product and complete-sum total exponent", 15+1+1, 17)
    less("total exponent within declared Cn", 17, 32)

    # Symbolic all-order exponent differences. Each is a*n+b with
    # a >= 0 and b > 0 for every integer n >= 0; not a finite-n test.
    for name, a, b in [
        ("Tn versus composition power of two", 8-1, 64-4),
        ("Tn versus reciprocal power of two", 8-4, 64-12),
        ("Tn versus complete q<=5 product power of two", 8-3, 64-7),
        ("Tn versus reciprocal low-L power", 2-1, 16-3),
    ]:
        assert a >= 0 and b > 0
        records.append(dict(label=name, coefficient=a, constant=b,
                            every_integer_n_ge_zero=True))
    less("sum of all seven literal normalized terms fits T0", 8, 2**64)

    print(json.dumps({
        "schema": "visible-flex-exact-nearby/PCT-saved-rational-majorants/v1",
        "new_comparisons": len(records),
        "all_passed": True,
        "old_scientific_targets_executed": 0,
        "old_carriers_or_integrals_restored": 0,
        "pins": PINS,
        "records": records,
        "scope": (
            "All-angular raw E value/first/full second derivative and "
            "current PD left-row first background derivative; declared "
            "independent low gauge A2 budget; no full regular inverse."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()

