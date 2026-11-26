#!/usr/bin/env python3
"""New exact rational combinations of completed QN/UH bounds; no science."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

PINS = {
    "results/R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md":
        "1fe88442bb35d0280a54dc416014f59773f1777a1b74998eb9513052b2f5a15e",
    "results/R144-supplement-uniform-real-physical-boundary-Hessian-near-compact-centres.md":
        "196f4b73184100e0399b89f1317071a8dffccb80c142f899b4fd64fa4d9bf64f",
    "results/R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md":
        "8a117376a5ad3f20c5cadb3521bd7a893987933e431329de394c929ffee8c94a",
    "results/R133-supplement-actual-regular-R25over8-vector-and-long-ports.md":
        "288245decc9aa64b1bfa5baff77731e0cd6a09e117bbf3ac61a3235a3ee5c779",
}


def main():
    topic = Path(__file__).resolve().parents[1]
    for relative, expected in PINS.items():
        assert hashlib.sha256((topic / relative).read_bytes()).hexdigest() == expected, relative
    checks = []

    def less(name, value, upper):
        assert value < upper, (name, value, upper)
        checks.append({"name": name, "exact_rational": str(value),
                       "strict_upper": str(upper)})

    z, b, eps = F("1e-10"), F("1e-11"), F(1, 2**512)
    total = 10*(z+b)+b
    kappa = 36*4096*total
    less("wide kappa", kappa, F("0.001"))
    jf = 9/(1-kappa)
    jb = (eps+kappa)/(1-kappa)
    t = eps+4*16384*total*jf
    c = (t-eps)/8
    u = eps+4*16384*total*(1+jb)
    v = (u-eps)/8
    less("wide full Z operator", t+c, F("0.001"))
    less("wide full height operator", u+v, F("0.0001"))
    rz, rb = F("5e-11"), F("9e-12")
    less("actual Z plus complex radius", F("4e-11")+rz, z)
    less("actual height plus complex radius", F(1, 2**60)+rb, b)
    er, p = F("1e-9"), F("1.480385e-11")
    ml = F("5.84461145233")-er
    e1 = 8*p+er*(1+8*p)/ml
    comp = F("1.000001")
    less("direct L2 composition squared", 1+e1, comp**2)
    less("direct inverse L2 composition squared", 1/(1-e1), comp**2)
    v1 = 3336*F("9.603792e-9")+er
    wa = 145*F("9.603792e-9")+er
    dc = comp*(F("5.84")**-2+v1*F("5.84")**-3*(2+wa/ml)/4)
    less("same direct L2 and H2 DC", dc, F("0.03"))
    zeta_tail = sum((F(1,j*j) for j in range(1,6)),F(0))+F(1,5)
    less("fourfold A0 embedding squared", 1+zeta_tail/8, F(11,10)**2)
    less("raw state Cauchy rate", F(11,10)*dc/rz, F(660000000))
    less("height Cauchy rate", F(11,10)/rb, F(660000000)*200)
    less("raw state second module coefficient", F("0.001")*dc, F(3,100000))
    less("height second module coefficient", F("0.0001"), 4*F(3,100000))
    symmetric = F(660000000)*F(3,100000)/2
    assert symmetric == 9900
    checks.append({"name": "symmetric Cauchy coefficient", "exact_rational": str(symmetric)})
    chain = 2*(F("0.0012")+F("0.00015"))
    less("full curvature Hessian coefficient", symmetric+4+chain, F(10000))
    remainder = F(10000)*F("1e-9")**2
    assert remainder == F("1e-14")
    checks.append({"name": "full fixed-height A3 remainder", "exact_rational": str(remainder)})
    print(json.dumps({"complete": True, "comparisons": len(checks),
                      "scientific_producers_called": 0, "bounds": checks},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
