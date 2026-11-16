#!/usr/bin/env python3
"""Complete original U136*Theta^4 norm-three trace.

Public GitHub Actions only.  Original defining polynomials, exact Fraction
Newton traces over ALL three fibres, and the actual [2] normalization.
No target-prime sampling, generated data files, or previously computed input.
"""
from __future__ import annotations

import json
import os
import hashlib
from pathlib import Path
from fractions import Fraction as Q
from math import comb


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("Public GitHub Actions execution is required.")
    if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("This producer is restricted to the public research repository.")


def trim(a):
    a = [Q(x) for x in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(*vectors):
    a = [Q(0)] * max(map(len, vectors))
    for v in vectors:
        for i, x in enumerate(v):
            a[i] += Q(x)
    return trim(a)


def scale(a, c):
    return trim([Q(c) * x for x in a])


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += Q(x) * Q(y)
    return trim(c)


def power(a, n):
    b = [Q(1)]
    for _ in range(n):
        b = mul(b, a)
    return b


def qstr(x):
    x = Q(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def vector(a, length=None):
    if length is not None:
        a = a + [Q(0)] * (length - len(a))
    return [qstr(x) for x in a]


def trace_three_powers():
    # A=a^3; X_i=x_i^3 on the actual norm-three fibre:
    # (X+4)^3+27*A*X^2=0.
    c2, c1, c0 = [Q(12), Q(27)], [Q(48)], Q(64)
    pos = {
        0: [Q(3)],
        1: scale(c2, -1),
        2: add(mul(c2, c2), [-Q(96)]),
    }
    for n in range(3, 8):
        pos[n] = add(scale(mul(c2, pos[n - 1]), -1),
                     scale(pos[n - 2], -48), scale(pos[n - 3], -64))
    # Reciprocal polynomial:
    # v^3+(3/4)v^2+(12+27*A)v/64+1/64=0.
    nc1 = scale(c2, Q(1, 64))
    neg = {
        0: [Q(3)],
        1: [-Q(3, 4)],
        2: add([Q(9, 16)], scale(nc1, -2)),
    }
    for n in range(3, 15):
        neg[n] = add(scale(neg[n - 1], -Q(3, 4)),
                     scale(mul(nc1, neg[n - 2]), -1),
                     scale(neg[n - 3], -Q(1, 64)))
    out = dict(pos)
    out.update({-n: v for n, v in neg.items() if n})
    return out


def la_add(*vectors):
    c = {}
    for v in vectors:
        for k, x in v.items():
            c[k] = c.get(k, Q(0)) + Q(x)
    return {k: x for k, x in c.items() if x}


def la_shift(v, k=0, c=Q(1)):
    return {j + k: Q(c) * x for j, x in v.items() if x and c}


def trace_two_powers():
    # Actual [2] fibre x^4-4*a*x^3-8*x-4*a=0, b=1.
    pos = {
        0: {0: Q(4)},
        1: {1: Q(4)},
        2: {2: Q(16)},
        3: {3: Q(64), 0: Q(24)},
        4: {4: Q(256), 1: Q(144)},
    }
    for n in range(5, 25):
        pos[n] = la_add(la_shift(pos[n - 1], 1, 4),
                        la_shift(pos[n - 3], 0, 8),
                        la_shift(pos[n - 4], 1, 4))
    neg = {
        0: {0: Q(4)},
        1: {-1: -Q(2)},
        2: {-2: Q(4)},
        3: {-3: -Q(8), 0: -Q(3)},
        4: {-4: Q(16), -1: Q(9)},
    }
    for n in range(5, 7):
        neg[n] = la_add(la_shift(neg[n - 1], -1, -2),
                        la_shift(neg[n - 3], 0, -1),
                        la_shift(neg[n - 4], -1, Q(1, 4)))
    out = dict(pos)
    out.update({-n: v for n, v in neg.items() if n})
    return out


def trace_two_degree48(poly, moments):
    # sigma^48 * poly(X) / sigma(2z)^12 = poly(X)/(2^12*(X+1)^6).
    # (x-4a)(X+1)=9*x keeps the ENTIRE four-fibre trace.
    out = {}
    common = Q(1, (2 ** 12) * (9 ** 6))
    for i, c in enumerate(poly):
        for j in range(7):
            k = 3 * i - 6 + j
            coefficient = common * c * comb(6, j) * ((-4) ** (6 - j))
            out = la_add(out, la_shift(moments[k], 6 - j, coefficient))
    assert all(0 <= k <= 6 and k % 3 == 0 for k in out)
    return trim([out.get(3 * k, Q(0)) for k in range(3)])


def main():
    guard()
    # Original U136 input, R884(C5)-(C6), b=1.
    q7 = trim([16, -4, 7])
    a2 = trim([-8, 20, 1])
    f4 = trim([1792, 3136, 2112, 40, 1])
    g4 = trim([256, 1024, 1536, 52, 13])
    h8 = trim([-32768, -851968, -1949696, -2111488,
               -439040, -49408, -58688, 1232, 1])
    p21 = [Q(1)]
    for a in ([1, 1], q7, a2, f4, g4, h8):
        p21 = mul(p21, a)
    assert len(p21) == 22

    # U*Theta^4 = sigma^144 * X^2*(X+1)*Q7*A2*F4*G4*H8/91.
    # Divide by (delta*x)^48=3^24*X^16.
    moments = trace_three_powers()
    q48 = [Q(0)]
    for j, c in enumerate(p21):
        q48 = add(q48, scale(moments[j - 14], c / Q(91 * (3 ** 24))))
    assert len(q48) <= 8, "The original norm-three trace lost its center-zero scope."
    assert q48[0] == -Q(1024, 819), "The complete x=0 boundary does not agree."

    # R3=sigma^3*y; [4]^*R3=-sigma^48*K8 with the ORIGINAL doubling maps.
    X = trim([0, 1])
    f = trim([1, 1])
    d = trim([-8, 1])
    k8 = add(mul(power(X, 2), power(d, 6)),
             scale(mul(mul(X, power(d, 3)), power(f, 3)), 1280),
             scale(power(f, 6), -32768))
    pull4_r3 = scale(k8, -1)
    w48 = add(q48, scale(pull4_r3, -Q(1, 78624)))

    # R884: Unew=U*Theta^4+[4]^*C9/19656,
    # Tr_delta(C9)=-R3/4. Hence Tr_delta(Unew)=W48.
    assert len(w48) == 9 and w48[8] == Q(1, 78624)
    assert w48[0] == -Q(4096, 2457)

    # Independently keep the full [2] trace and canonical commutation:
    # Tr_2(Q48)=[2]^*R3/19656=-sigma^12*A2/19656, Tr_2(W48)=0.
    m2 = trace_two_powers()
    tq = trace_two_degree48(q48, m2)
    tw = trace_two_degree48(w48, m2)
    assert tq == scale(a2, -Q(1, 19656))
    assert tw == [Q(0)]
    assert all(isinstance(c, Q) for v in (q48, w48, tq, tw) for c in v)

    result = {
        "source": "Original U136*Theta^4; all three norm-three fibres, b=1",
        "target": "sigma^48 * q(X), X=x^3",
        "Q48_X_ascending": vector(q48, 9),
        "Tr_delta_original_Unew144_X_ascending": vector(w48, 9),
        "Q48_mass": "0",
        "Tr_delta_Unew_mass": "1/78624",
        "Tr_2_Q48": vector(tq),
        "Tr_2_Tr_delta_Unew": vector(tw),
        "general_b_scaling": "coefficient j is b^(7-j), including j=8",
        "actual_whole_degree48_first_jet": "j_(p+1)(Tr_delta_Unew) = c_p/(1638*b) mod p",
        "scope": "Characteristic-zero source identity and exact whole-jet normalization; no new central zero or target-prime sampling",
    }
    result["source_commit"] = os.environ.get("RANK2_SOURCE_SHA")
    result["run_id"] = os.environ.get("RANK2_RUN_ID")
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["readme_blobs"] = {
        "root": os.environ.get("RANK2_ROOT_README_SHA"),
        "topic": os.environ.get("RANK2_TOPIC_README_SHA"),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print("RANK2_U_THETA4_DELTA_RESULT " + payload, flush=True)
    print("RANK2_U_THETA4_DELTA_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
