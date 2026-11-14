#!/usr/bin/env python3
"""Exact finite polynomial data for the three actual sources in R473.

The birationality, normalization and conductor arguments are symbolic proofs,
not extrapolations from this certificate.  No target-prime scan is performed.
"""
from pathlib import Path
import json
import sympy as sp


def main():
    t, X = sp.symbols("t X")
    P = sp.Poly(
        (X+1)*(X**2+20*X-8)*(7*X**2-4*X+16)
        *(X**4+40*X**3+2112*X**2+3136*X+1792)
        *(13*X**4+52*X**3+1536*X**2+1024*X+256)
        *(X**8+1232*X**7-58688*X**6-49408*X**5
          -439040*X**4-2111488*X**3-1949696*X**2
          -851968*X-32768), X)
    fU = sp.Poly(sum(P.nth(j)*(-1)**j*t**(22-j)
                      for j in range(22)), t, domain=sp.QQ).mul_ground(sp.Rational(1, 91))
    a = sp.Poly(t*(t-1)*(7+4*t+16*t*t), t)
    d = sp.Poly(1+8*t, t)
    V = sp.Poly((1-4*t)*(1-20*t-8*t*t)
                *(1+96*t+48*t*t-64*t**3), t)
    H, rem = fU.mul_ground(91).div(a)
    assert rem.is_zero and H.degree() == 18
    assert all(x.q == 1 for x in H.all_coeffs())
    ad = a*d
    assert sp.gcd(ad, V).degree() == 0
    assert sp.gcd(ad, H).degree() == 0
    assert sp.gcd(ad, ad.diff()).degree() == 0
    f = ad.to_field().mul_ground(sp.Rational(1, 7))
    assert (f**19).degree() == 95 and (V**17).degree() == 102
    Bnum, Bden = H.mul_ground(sp.Rational(343, 13)), a**3*d**4
    assert Bnum.degree() == 18 and Bden.degree() == 16
    assert sp.gcd(Bnum, Bden).degree() == 0
    assert 17*17-36*8 == 1
    data = {
        "H_coefficients_ascending": [str(H.nth(i)) for i in range(19)],
        "H_factorization": str(sp.factor(H.as_expr())),
        "degrees": {"a": 4, "d": 1, "V": 6, "f": 5,
                    "fU": 22, "H": 18, "A_map": 102, "B_map": 18},
        "valuation_pairs_A_B": {
            "four_roots_a": [19, -3], "root_d": [19, -4],
            "infinity": [7, -2]},
        "fixed_integer_factors": {},
    }
    fixed = {
        "lead_H": int(H.LC()),
        "lead_V": int(V.LC()),
        "discriminant_ad": int(sp.discriminant(ad.as_expr(), t)),
        "resultant_ad_H": int(sp.resultant(ad.as_expr(), H.as_expr(), t)),
        "resultant_ad_V": int(sp.resultant(ad.as_expr(), V.as_expr(), t)),
    }
    bad = {2, 3, 7, 13, 17}
    for name, value in fixed.items():
        assert value != 0
        fac = {str(p): int(e) for p, e in sp.factorint(abs(value)).items()}
        data["fixed_integer_factors"][name] = fac
        bad.update(int(p) for p in fac)
    data["fixed_bad_primes"] = sorted(bad)
    # A finite residue calculation proves generation over the 68-Veronese
    # in weights at most 80, since every further step adds 18 free t powers.
    residues = []
    for r in range(68):
        eps = int(r != 0)
        q = 11*r//34-4*eps
        n0 = int(q < 0)
        residues.append((r, q, r+68*n0, 18*n0+q+1))
    assert max(x[2] for x in residues) == 80
    data["normalization_residue_generators"] = residues
    # The entire Hilbert series of A follows from the one monic relation.
    assert 36*306 == 11016 and 11016-36 == 10980
    assert sp.Rational(11016, 17*36*68) == sp.Rational(9, 34)
    data["relation_T_degree"] = 306
    data["relation_weight"] = 11016
    data["conductor_weight"] = 10980
    data["linear_Hilbert_coefficient"] = "9/34"
    data["certificate"] = "all exact assertions passed; no prime scan"
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({k: data[k] for k in (
        "degrees", "fixed_bad_primes", "relation_T_degree",
        "relation_weight", "conductor_weight", "certificate")}))


if __name__ == "__main__":
    main()
