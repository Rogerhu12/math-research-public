#!/usr/bin/env python3
"""Independent integer-lattice checks of R293's complete finite Tor.

This uses the true cyclic group ring in its T basis, not a truncated
dual-number ring.  Smith computations determine the orders of the two
actual generators and of their combined subgroup.  The full kernel order
is independently obtained from the cokernel of the theta endomorphism.
These algebra examples are not arithmetic certificates for the target E.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def valuation(a: int, p: int) -> int:
    assert a
    a = abs(int(a))
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def index_length(columns: sp.Matrix, p: int) -> int:
    sm = smith_normal_form(columns, domain=ZZ)
    ds = [int(sm[j, j]) for j in range(sm.rows)]
    assert all(ds)
    assert all(abs(x) == p ** valuation(x, p) for x in ds)
    return sum(valuation(x, p) for x in ds)


def residue(a: sp.Rational, modulus: int) -> int:
    a = sp.Rational(a)
    return int(a.p) * pow(int(a.q), -1, modulus) % modulus


def one(p: int, n: int, d: int, r: int) -> dict:
    assert 0 <= r <= d < n
    m = p ** (n - 1)
    T = sp.Symbol("T")
    omega = sp.Poly((1 + T) ** m - 1, T)
    a_n = int(omega.eval(p))
    assert valuation(a_n, p) == n
    bpoly = sp.Poly(-sp.Rational(p**n, a_n) * sp.div(omega.as_expr() - a_n, T - p, T)[0], T)
    bcentre = bpoly.eval(p)
    assert valuation(int(bcentre.p), p) - valuation(int(bcentre.q), p) == n - 1
    ypoly = sp.Poly(sp.div(bpoly.as_expr() - bcentre, T - p, T)[0], T)
    assert sp.rem((T-p)*bpoly.as_expr() - p**n, omega.as_expr(), T) == 0
    assert sp.expand((T-p)*ypoly.as_expr() - bpoly.as_expr() + bcentre) == 0

    theta = sp.zeros(m)
    for j in range(m):
        rem = sp.Poly(sp.rem((T-p)*T**j, omega.as_expr(), T), T)
        for k in range(m):
            theta[k, j] = rem.nth(k)
    modulus = p**d
    if d == 0:
        return {"p": p, "n": n, "d": d, "r": r, "kernel_lengths": [0, 0], "status": "PASS"}

    b = sp.Matrix([residue(bpoly.nth(k), modulus) for k in range(m)])
    y = sp.Matrix([residue(ypoly.nth(k), modulus) for k in range(m)])
    g1, g2 = b, p**(d-r)*y
    lattice = (modulus*sp.eye(m)).row_join(p**(d-r)*b)
    base_length = index_length(lattice, p)
    full_kernel_length = index_length(lattice.row_join(theta), p)
    assert full_kernel_length == d

    # Each image under theta belongs to the original relation lattice.
    for g in (g1, g2):
        assert index_length(lattice.row_join(theta*g), p) == base_length
    orders = [base_length-index_length(lattice.row_join(g), p) for g in (g1,g2)]
    assert orders == [d-r, r]
    joint = base_length-index_length(lattice.row_join(g1).row_join(g2), p)
    assert joint == d == sum(orders) == full_kernel_length

    # The annihilator (theta,p^(n-r)) has the prescribed centre quotient.
    ann_length = index_length(theta.row_join(p**(n-r)*sp.eye(m)), p)
    assert ann_length == n-r
    return {"p":p,"n":n,"d":d,"r":r,"dimension":m,
            "kernel_lengths":orders,"full_kernel_length":full_kernel_length,
            "joint_length":joint,"annihilator_quotient_length":ann_length,
            "status":"PASS"}


def main() -> None:
    cases = [(3,2,0,0)]
    for p,n,d in [(3,2,1),(3,3,1),(3,3,2),(3,4,3),(5,2,1)]:
        cases.extend((p,n,d,r) for r in range(d+1))
    results = [one(*c) for c in cases]
    output = {"result":"R293", "checks":len(results), "status":"PASS", "cases":results,
              "scope":"Exact cyclic-group-ring algebra only; no new arithmetic prime certificate."}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
    print(f"{len(results)} exact group-ring lattice checks PASS; wrote {target.name}")


if __name__ == "__main__":
    main()
