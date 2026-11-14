#!/usr/bin/env python3
"""R414: exact finite-field certificate for one actual auxiliary source.

This is not a target-prime scan. One exact reduction of two complete CM7
fibers disproves a characteristic-zero scalar-eigenvector assertion.
Only Python's standard library is used.
"""

import json

P = 1009
DELTA = 260
assert all(P % divisor for divisor in range(2, 32))
assert (DELTA * DELTA + 3) % P == 0


def trim(a):
    a = [c % P for c in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)
                 + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * x for x in a])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def power(a, n):
    out = [1]
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out


def divide(a, b):
    a = trim(a)
    b = trim(b)
    assert b != [0]
    q = [0] * max(1, len(a) - len(b) + 1)
    leading_inverse = pow(b[-1], -1, P)
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] * leading_inverse % P
        q[k] = c
        for j, x in enumerate(b):
            a[k + j] -= c * x
        a = trim(a)
    return trim(q), a


def invert(a, f):
    r0, r1, s0, s1 = f, trim(a), [0], [1]
    while r1 != [0]:
        q, r2 = divide(r0, r1)
        s2 = add(s0, scale(mul(q, s1), -1))
        r0, r1, s0, s1 = r1, r2, s1, s2
    assert len(r0) == 1 and r0[0] != 0
    out = divide(scale(s0, pow(r0[0], -1, P)), f)[1]
    assert divide(mul(a, out), f)[1] == [1]
    return out


def evaluate(a, x):
    out = 0
    for c in a[::-1]:
        out = (out * x + c) % P
    return out


# Actual normalized A = sigma^136 * x^2 Q(x^3), at b=1.
X, ONE = [0, 1], [1]
xp1, xm8 = [1, 1], [-8, 1]
R = [-8, 20, 1]
A4 = add(mul(X, power(xm8, 3)), scale(power(xp1, 3), -512))
B8 = add(add(scale(mul(power(X, 2), power(xm8, 6)), 7),
             scale(mul(mul(X, power(xm8, 3)), power(xp1, 3)), -256)),
         scale(power(xp1, 6), 65536))
L = [64, 192, -24, 10]
Q = [pow(70, -1, P)]
for factor in [power(xp1, 2), power(xm8, 2), R, A4, B8, L]:
    Q = mul(Q, factor)
assert len(Q) == 22 and Q[-1] == 1

gamma = (5 + DELTA) * pow(2, -1, P) % P
gamma_bar = (5 - DELTA) * pow(2, -1, P) % P
r = (2 - 6 * DELTA) * pow(7, -1, P) % P
r_bar = (2 + 6 * DELTA) * pow(7, -1, P) % P
assert gamma * gamma_bar % P == 7


def fiber(target):
    ga = gamma * gamma * target % P
    f = trim([-ga * r * r, r * (7 * r + 24), 0,
              2 * ga * r, 28 * r + 12, 0, -ga, 1])
    red = lambda a: divide(a, f)[1]
    rm = lambda a, b: red(mul(a, b))

    def rp(a, n):
        out = [1]
        while n:
            if n & 1:
                out = rm(out, a)
            a = rm(a, a)
            n //= 2
        return out

    q, qb = trim([-r, 0, 0, 1]), trim([-r_bar, 0, 0, 1])
    iq, iqb = invert(q, f), invert(qb, f)
    df = trim([i * f[i] for i in range(1, len(f))])
    idf = invert(df, f)
    numerator = [0, r_bar * (7 * r_bar + 24), 0, 0,
                 28 * r_bar + 12, 0, 0, 1]
    xb = scale(rm(red(numerator), rp(iqb, 2)),
               pow(gamma_bar * gamma_bar % P, -1, P))
    xb3 = rp(xb, 3)
    out = [0]
    for c in Q[::-1]:
        out = add(rm(out, xb3), [c])
    out = rm(out, rp(xb, 2))
    frame = scale(rp(rm(qb, iq), 136),
                  pow(gamma_bar * pow(gamma, -1, P) % P, 136, P))
    out = rm(out, frame)
    trace_polynomial = rm(out, df)
    trace = trace_polynomial[6] if len(trace_polynomial) > 6 else 0
    value = target * target * evaluate(Q, pow(target, 3, P)) % P
    assert value
    return {
        "target_x": target,
        "fiber_polynomial_ascending": f,
        "q_inverse_ascending": iq,
        "qbar_inverse_ascending": iqb,
        "fiber_derivative_inverse_ascending": idf,
        "trace": trace,
        "source_value": value,
        "trace_divided_by_source": trace * pow(value, -1, P) % P,
    }


rows = [fiber(1), fiber(3)]
assert [row["trace_divided_by_source"] for row in rows] == [507, 490]
report = {
    "scope": "Exact two-fiber counterexample to a CM7 scalar eigenline; no target-prime scan.",
    "prime": P,
    "delta": DELTA,
    "gamma7": gamma,
    "gamma7_bar": gamma_bar,
    "source": "A=sigma^136*x^2*Q(x^3), b=1; Q is the actual R414 polynomial.",
    "Q_coefficients_ascending": Q,
    "fibers": rows,
    "ratio_difference": (507 - 490) % P,
    "interpretation": "The characteristic-zero actual source A is not a CM7 eigenvector."
}
print(json.dumps(report, indent=2))
