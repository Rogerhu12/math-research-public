#!/usr/bin/env python3
"""New R1154 section 11 quantities; execute only in this public repository's Actions."""
import argparse
import hashlib
import json
import math
import os

def prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))

def row(p):
    cap = p - 1
    inv = [0] + [pow(i, -1, p) for i in range(1, p)]
    def trim(a):
        a = [x % p for x in a[:cap + 1]]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a
    def add(a, b, scale=1):
        c = a[:] + [0] * max(0, len(b) - len(a))
        for i, x in enumerate(b):
            if i <= cap:
                c[i] = (c[i] + scale * x) % p
        return trim(c)
    def mul(a, b):
        c = [0] * min(cap + 1, len(a) + len(b) - 1)
        aa = [(i, x) for i, x in enumerate(a) if x]
        bb = [(i, x) for i, x in enumerate(b) if x]
        for i, x in aa:
            for j, y in bb:
                if i + j > cap:
                    break
                c[i+j] = (c[i+j] + x*y) % p
        return trim(c)
    def shift(a):
        return trim([0] + a)
    def at(a, n):
        return a[n] if n < len(a) else 0
    def R(a):
        return sum(a[::2]) % p
    nu = (p - 1) // 6 if p % 12 == 7 else (p - 5) // 6
    assert nu % 2 == 1 and p % 12 in (7, 11)
    leg = [[1], [0, 1]]
    for n in range(1, nu):
        leg.append(trim([x * inv[n+1] for x in
                         add([(2*n+1)*x for x in shift(leg[n])],
                             leg[n-1], -n)]))
    P = leg[nu]
    W = [0]
    for j in range(1, nu+1):
        W = add(W, mul(leg[j-1], leg[nu-j]), inv[j])
    assert sum(P) % p == 1
    H = [0]
    for i in range(1, p):
        H.append((H[-1] + inv[i]) % p)
    assert sum(W) % p == H[nu]
    M = (p - 1) // 2
    odd = [0]
    for s in range(1, M+1):
        odd.append((odd[-1] + inv[2*s-1]) % p)
    AA = [0]
    for s in range(1, M+1):
        AA.append((AA[-1] + odd[s]*inv[s]) % p)
    def cut(a, hi):
        return sum(at(a, 2*s) for s in range(hi+1)) % p
    def weighted(a, weights, hi):
        return sum(at(a, 2*s)*weights[s] for s in range(hi+1)) % p
    P2 = mul(P, P)
    P3 = mul(P2, P)
    P4 = mul(P2, P2)
    P5 = mul(P4, P)
    P6 = mul(P4, P2)
    P7 = mul(P6, P)
    P8 = mul(P4, P4)
    L = [0] * p
    for i in range(1, p, 2):
        L[i] = inv[i]
    V = add(W, mul(P, L), -1)
    V2 = mul(V, V)
    V3 = mul(V2, V)
    boldB = R(mul(P4, V2))
    boldU = R(shift(mul(P7, V)))
    boldV = R(shift(mul(P5, V3)))
    q = ((pow(2, p-1, p*p) - 1) // p) % p
    Q = (H[nu] - inv[2] * weighted(P4, H, M-1)) % p
    assert R(shift(mul(P3, V))) == (Q-q) % p
    beta3 = (-inv[2] * sum(pow(b, p-4, p) for b in range(1, M+1))) % p
    D1, D2 = cut(P8, M-1), cut(P8, M-2)
    B1 = (-2*H[nu] + 2*weighted(P6, odd, M-1)) % p
    W2 = mul(W, W)
    V1 = (-3*cut(mul(P6, W2), M-1)
          + 6*weighted(shift(mul(P7, W)), odd, M-1)
          - 3*weighted(P8, AA, M-2)) % p
    dq = (Q-q) % p
    C_Q = (3*(boldB+B1*dq)*(boldU-D1*dq)
           - boldV - V1*dq - 3*inv[8]*beta3*D2) % p
    numerator_actual = (3*boldB*boldU-boldV) % p
    residual_Q = (C_Q+3*inv[8]*beta3*D2) % p
    return dict(p=p, nu=nu, q=q, Q=Q, beta3=beta3, D1=D1, D2=D2,
                C_Q=C_Q, residual_Q=residual_Q,
                actual_minor_numerator=numerator_actual,
                actual_joint=(q == Q and numerator_actual == 0))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    args = parser.parse_args()
    with open(args.request, encoding="utf-8") as f:
        request = json.load(f)
    selected = [p for p in range(request["lower"]+1, request["upper"])
                if p % 4 == 3 and prime(p)][:request["max_primes"]]
    rows = []
    for p in selected:
        rr = row(p)
        rows.append(rr)
        print("PROBE_ROW " + json.dumps(rr, sort_keys=True), flush=True)
    output = dict(schema="serre-legendre-weighted-probe-v1",
                  source_sha=os.environ.get("GITHUB_SHA"),
                  request=request, rows=rows)
    body = json.dumps(output, sort_keys=True, separators=(",", ":"))
    print("SERRE_LEGENDRE_WEIGHTED " + body)
    print("SERRE_LEGENDRE_WEIGHTED_SHA256 " +
          hashlib.sha256(body.encode("utf-8")).hexdigest())

if __name__ == "__main__":
    main()
