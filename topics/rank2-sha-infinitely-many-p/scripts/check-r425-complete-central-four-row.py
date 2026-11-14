#!/usr/bin/env python3
"""Check R425 on the entire original P134 carrier and actual three blocks.

The two-parameter family is only a finite coordinate identity; its changed
parameters are not asserted to be new arithmetic theta sources.
"""
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("actual_three_blocks", ROOT / "explore-rank2-actual-small-source-smith.py")
actual = importlib.util.module_from_spec(spec)
spec.loader.exec_module(actual)


def series(p, ell, length):
    G = actual.ThreeBlocks.__new__(actual.ThreeBlocks)
    G.p, G.s, G.ell, G.L, G.mod = p, (p+1)//6, ell, length, p**3
    G.one, G.zero = [1]+[0]*(length-1), [0]*length
    G.initialize()
    return G


def nullspace(rows, p):
    A = [[x % p for x in row] for row in rows]
    nr, nc, r, pivots = len(A), len(A[0]), 0, []
    for c in range(nc):
        pos = next((i for i in range(r, nr) if A[i][c]), None)
        if pos is None:
            continue
        A[r], A[pos] = A[pos], A[r]
        inverse = pow(A[r][c], -1, p)
        A[r] = [x*inverse % p for x in A[r]]
        for i in range(nr):
            if i != r and A[i][c]:
                v = A[i][c]
                A[i] = [(x-v*y) % p for x, y in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == nr:
            break
    basis = []
    for f in range(nc):
        if f in pivots:
            continue
        v = [0]*nc
        v[f] = 1
        for i, c in enumerate(pivots):
            v[c] = -A[i][f] % p
        basis.append(v)
    return basis


def scalar_exp_gamma(G, h, q):
    out, power = G.one[:], G.one[:]
    for j in range(1, 5):
        power = G.gamma_mul(power, h)
        out = G.add(out, G.scale(power, pow(q, j, G.mod)*pow(factorial(j), -1, G.mod)))
    return out


def carrier_and_ordinary_columns(G, D, J):
    coeffs = json.loads((ROOT / "check-jzero-full-canonical-conductor-basis.json").read_text())["fixed_numerator_coefficients"]
    poly = G.zero[:]
    for value in reversed(coeffs):
        poly = G.add(G.mul(poly, G.t), G.scale(G.one, int(value)))
    h0 = G.mul(G.mul(G.mul(G.mul(poly, G.power(G.t, 13)), G.power(G.tm1, 15)), G.power(G.h, 13)), G.power(G.d, -17))
    carrier = G.gamma_mul(G.power(G.R, 40, True), G.to_gamma(h0))
    carrier_reg = G.mul(G.power(G.g, 40), h0)
    assert not any(carrier_reg[:13]) and carrier_reg[13] % G.p
    Ureg = carrier_reg[13:] + [0]*13
    cols, labels = G.columns(D, J)
    full = [G.gamma_mul(carrier, col) for col in cols]
    ordinary = []
    gp = [G.power(G.g, n) for n in range(D+1)]
    tp = [G.power(G.Treg, j) for j in range(J+1)]
    for n, k, j in labels:
        A, B, C = (n+1)//4, (n+1)//3, n//2
        qn = G.mul(G.mul(G.power(G.mul(G.t, G.h), A), G.power(G.tm1, B)), G.power(G.d, -C))
        angular = G.mul(qn, G.power(G.t, k))
        ordinary.append(G.mul(Ureg, G.mul(G.mul(gp[n], angular), tp[j])))
    return full, labels, ordinary, carrier


def check_full_carrier():
    p, ell, D, J = 101, 1, 1, 2
    s, length = (p+1)//6, 2*((p+1)//6)+ell+13
    G = series(p, ell, length)
    cols, labels, ordinary, carrier = carrier_and_ordinary_columns(G, D, J)
    h = G.zero[:]
    h[s-2], h[s-1] = 2, 3
    hg = G.to_gamma(h)
    alpha = 36*pow(17, -1, G.mod) % G.mod
    oldR, oldT = G.R, G.T
    G.R = G.gamma_mul(oldR, scalar_exp_gamma(G, hg, 1))
    G.T = G.gamma_mul(oldT, scalar_exp_gamma(G, hg, alpha))
    changed_rel, changed_labels = G.columns(D, J)
    assert changed_labels == labels
    changed_carrier = G.gamma_mul(carrier, scalar_exp_gamma(G, hg, 40))
    changed = [G.gamma_mul(changed_carrier, col) for col in changed_rel]
    G.R, G.T = oldR, oldT
    h2 = G.gamma_mul(hg, hg)
    for old, new, (n, k, j) in zip(cols, changed, labels):
        Q = n+40+alpha*j
        predicted = G.add(old, G.add(G.scale(G.gamma_mul(hg, old), Q), G.scale(G.gamma_mul(h2, old), Q*Q*pow(2, -1, G.mod))))
        assert new == predicted
        assert all((x-y) % p == 0 for x, y in zip(new, old))
    rows = [[col[r] for col in cols] for r in range(length)]
    basis = nullspace(rows, p)
    nonzero = 0
    for P in basis:
        W1, W2 = [0]*length, [0]*length
        for c, (n, k, j), A in zip(P, labels, ordinary):
            Q = (n+40+alpha*j) % p
            for r in range(length):
                W1[r] = (W1[r]+c*Q*A[r]) % p
                W2[r] = (W2[r]+c*Q*Q*A[r]) % p
        assert not any(W1[:s-13]) and not any(W2[:ell])
        expected = [0]*length
        expected[2*s-2] = 2*W1[s-13] % p
        expected[2*s-1] = (2*W1[s-12]+3*W1[s-13]) % p
        expected[2*s+ell+11] = G.ap*2*W2[ell] % p
        expected[2*s+ell+12] = G.ap*(2*W2[ell+1]+3*W2[ell]) % p
        delta = [sum(c*(new[r]-old[r]) for c, new, old in zip(P, changed, cols)) % (p*p) for r in range(length)]
        assert all(x % p == 0 for x in delta)
        assert [x//p for x in delta] == expected
        nonzero += bool(any(expected))
    return {"p": p, "ell": ell, "D": D, "J": J,
            "actual_first_kernel_dimension": len(basis), "nonzero_four_tail_checks": nonzero}


def check_central_hensel():
    p, s = 101, 17
    G = series(p, 1, 3*s+1)
    ang = G.scale(G.mul(G.mul(G.t, G.tm1), G.h), pow(7, -1, G.mod))
    S, T = G.mul(G.g, ang), G.Treg
    alpha = 36*pow(17, -1, G.mod) % G.mod
    ap = G.ap

    def coefficient(A, q, k, u, v):
        total = 0
        for m in range(k+1):
            for j in range(m+1):
                index = k*s-m*(s-2)-j
                if index >= 0:
                    total += pow(q,m,G.mod)*pow(factorial(m),-1,G.mod)*comb(m,j)*pow(u,m-j,G.mod)*pow(v,j,G.mod)*A[index]
        return total % G.mod

    def F(u, v):
        c = [coefficient(S, 1, k, u, v) for k in (1,2,3)]
        d = [coefficient(T, alpha, k, u, v) for k in (1,2,3)]
        fs = c[0]-p*pow(ap,-1,G.mod)*c[1]+2*p*p*pow(ap*ap,-1,G.mod)*c[2]
        ft = pow(alpha,-1,G.mod)*d[0]-p*pow(alpha*alpha*ap,-1,G.mod)*d[1]+2*p*p*pow(alpha**3*ap*ap,-1,G.mod)*d[2]
        return fs % G.mod, ft % G.mod

    h = G.zero[:]
    h[s-2], h[s-1] = 2, 3
    for A, q in ((S,1),(T,alpha)):
        changed = G.mul(A,G.exp(G.scale(h,q)))
        for k in (1,2,3):
            assert coefficient(A,q,k,2,3) == changed[k*s]
    beta = (T[2]-S[2]) % p
    assert beta == -1118*pow(15,-1,p) % p and beta
    fs, ft = F(0,0)
    u = ((fs-ft)*pow(beta,-1,p)) % p
    v = (-fs-S[2]*u) % p
    for r in (1,2):
        fs, ft = F(u,v)
        assert fs % (p**r) == ft % (p**r) == 0
        a, b = (fs//(p**r)) % p, (ft//(p**r)) % p
        du = ((a-b)*pow(beta,-1,p)) % p
        dv = (-a-S[2]*du) % p
        u += p**r*du
        v += p**r*dv
    assert F(u,v) == (0,0)
    return {"p":p, "unique_formal_hensel_pair_mod_p3":[u,v],
            "actual_reference_pair":[0,0], "arithmetic_source_claim":False}


if __name__ == "__main__":
    print(check_full_carrier())
    print(check_central_hensel())
    print("R425: full P134, four actual tail rows, and complete three-weight Hensel checks passed")
