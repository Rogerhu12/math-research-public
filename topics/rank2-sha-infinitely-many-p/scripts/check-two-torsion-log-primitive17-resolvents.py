#!/usr/bin/env python3
"""Exact ray-scalar character resolvents for 1/(x^2-1) on E[4-i].

All arithmetic is in Q(i)[U]/K(U), using the already proved CM division
polynomial of R59.  No numerical roots, p-adic periods or prime search occur.
"""
import json
import sympy as sp


def main():
    U = sp.symbols("U")
    ii = sp.I
    K = ((4-ii)*U**4 + (-12+20*ii)*U**3 + (28+10*ii)*U**2
         + (-20-12*ii)*U - ii)
    kp = sp.Poly(K, U, domain=sp.QQ_I)

    def rem(q):
        return sp.Poly(q, U, domain=sp.QQ_I).rem(kp).as_expr().expand()

    def inv(q):
        return sp.invert(q, K, U, domain=sp.QQ_I).expand()

    def compose(f, g):
        return rem(sum(c*rem(g**j) for (j,), c in sp.Poly(f, U).terms()))

    c3 = 3*U**2 - 6*U - 1
    d3 = U**4 + 12*U**3 + 30*U**2 - 36*U + 9
    g = rem(U*d3**2*inv(c3**4))
    expected_g = ((1+4*ii)*U**3 - (20+12*ii)*U**2
                  + (-11+28*ii)*U + 14-20*ii)/4
    assert rem(g-expected_g) == 0
    assert compose(K, g) == 0
    gg = U
    for _ in range(4):
        gg = compose(gg, g)
    assert rem(gg-U) == 0

    b = inv(U-1)
    bs = [b]
    for _ in range(3):
        bs.append(compose(bs[-1], g))
    assert rem(sum(bs)-(-4+ii)) == 0

    expected_norms = [256*(-89+52*ii), 256*(-15+8*ii),
                      256*(47+52*ii)]
    data = []
    for k in (1, 2, 3):
        r = rem(4*sum(ii**(k*j)*bs[j] for j in range(4)))
        rp = sp.Poly(r, U, domain=sp.QQ_I)
        assert sp.gcd(kp, rp).degree() == 0
        assert rem(compose(r, g)-ii**(-k)*r) == 0
        norm = sp.expand(kp.resultant(rp)/(4-ii)**rp.degree())
        norm = sp.simplify(norm)
        assert sp.expand(norm-expected_norms[k-1]) == 0
        rational_norm = sp.expand(norm*sp.conjugate(norm))
        data.append({"k": k, "resolvent": str(r), "norm_over_Qi": str(norm),
                     "norm_over_Q_factorization": str(sp.factorint(rational_norm))})
    print(json.dumps({"status": "PASS", "division_polynomial": str(K),
                      "triplication_on_U": str(g),
                      "trace_over_nonzero_kernel": "-16+4*I",
                      "resolvents": data}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
