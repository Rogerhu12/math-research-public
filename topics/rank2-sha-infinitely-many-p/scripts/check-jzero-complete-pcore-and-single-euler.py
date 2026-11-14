#!/usr/bin/env python3
"""Exact fixed certificates for R300; no prime scan or numerical fitting.

The input is the already proved, full CM13 matrix of R297.  All new
calculations take place in Q[delta]/(delta^2+3), using rational arithmetic.
The variable-prime trace and measure arguments are proved in the text.
"""
from fractions import Fraction as F
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "check-jzero-actual-cm13-matrix-and-theta-source.json").read_text())
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[0], -a[1]


def scale(a, b):
    return a[0] * b, a[1] * b


def mul(a, b):
    return a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def power(a, n):
    r = ONE
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r


def inverse(a):
    norm = a[0] ** 2 + 3 * a[1] ** 2
    return a[0] / norm, -a[1] / norm


def total(xs):
    r = ZERO
    for a in xs:
        r = add(r, a)
    return r


def mm(a, b):
    return [[total(mul(a[i][k], b[k][j]) for k in range(6))
             for j in range(6)] for i in range(6)]


def ma(a, b):
    return [[add(a[i][j], b[i][j]) for j in range(6)] for i in range(6)]


def ms(a, c):
    return [[mul(v, c) for v in row] for row in a]


def mv(a, v):
    return [total(mul(a[i][j], v[j]) for j in range(6)) for i in range(6)]


def mat_poly(a, descending):
    out = [[ZERO for j in range(6)] for i in range(6)]
    for c in descending:
        out = ma(mm(out, a), ms(ID, c))
    return out


def poly_mul(a, b):
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] = add(out[i + j], mul(c, d))
    return out


def evaluate(descending, x):
    out = ZERO
    for c in descending:
        out = add(mul(out, x), c)
    return out


def field17_mul(a, b):
    return ((a[0] * b[0] - 3 * a[1] * b[1]) % 17,
            (a[0] * b[1] + a[1] * b[0]) % 17)


def field17_pow(a, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = field17_mul(out, a)
        a = field17_mul(a, a)
        n //= 2
    return out


def pair17(a):
    return tuple(int(v.numerator * pow(v.denominator, -1, 17) % 17) for v in a)


def serial(a):
    return [str(v) for v in a]


checks = []


def check(label, condition):
    assert condition, label
    checks.append(label)


A, B = data["integer_matrix_real"], data["integer_matrix_delta"]
den = data["integer_matrix_denominator"]
M = [[(F(A[i][j], den), F(B[i][j], den)) for j in range(6)] for i in range(6)]
ID = [[ONE if i == j else ZERO for j in range(6)] for i in range(6)]
gamma = F(7, 2), F(1, 2)
omega = F(-1, 2), F(1, 2)
lam = neg(gamma)
v = [(F(a), F(0)) for a in [-2, -5, -3, -53, 28, 0]]
check("actual R297 source eigenvector", mv(M, v) == [mul(lam, a) for a in v])

# Newton identities compute the entire characteristic polynomial.
traces = [ZERO]
C = ID
for k in range(1, 7):
    C = mm(C, M)
    traces.append(total(C[i][i] for i in range(6)))
char = [ONE]
for k in range(1, 7):
    char.append(scale(total(mul(char[k - i], traces[i]) for i in range(1, k + 1)), F(-1, k)))
expected = [ONE, ZERO, ZERO, (F(89, 2), F(-17, 2)), ZERO, ZERO,
            (F(3527, 2), F(-1513, 2))]
check("complete six-dimensional characteristic polynomial", char == expected)
g3 = power(gamma, 3)
factor = poly_mul([ONE, ZERO, ZERO, g3],
                  [ONE, ZERO, ZERO, mul(power(omega, 2), g3)])
check("two exact cubic factors", factor == char)
der = [scale(c, 6 - j) for j, c in enumerate(char[:-1])]
dl = evaluate(der, lam)
check("simple actual eigenline", dl == (F(522), F(-1803)))
check("only 3 and 13 divide projector norm denominator",
      dl[0] ** 2 + 3 * dl[1] ** 2 == 27 * 13 ** 5)

quotient = poly_mul([ONE, neg(gamma), power(gamma, 2)],
                    [ONE, ZERO, ZERO, mul(power(omega, 2), g3)])
check("actual projector numerator", poly_mul([ONE, gamma], quotient) == char)
Proj = ms(mat_poly(M, quotient), inverse(dl))
check("projector is idempotent", mm(Proj, Proj) == Proj)
check("projector has trace one", total(Proj[i][i] for i in range(6)) == ONE)
check("projector image is actual CM13 eigenline", mm(M, Proj) == ms(Proj, lam))
check("projector fixes original source", mv(Proj, v) == v)

# The p=13 scalar is fixed by all three finite factors, not by a bare torus
# eigenvalue.  At 2, gamma=omega; at delta, gamma=-1.
chi17 = field17_pow(pair17(gamma), 48)
check("positive original 17-adic residue exponent", chi17 == pair17(power(omega, 2)))
epsilon = mul(neg(omega), power(omega, 2))
check("complete finite epsilon at gamma13 is -1", epsilon == neg(ONE))
check("actual Frobenius is -gamma13", mul(gamma, inverse(epsilon)) == lam)
for j in range(6):
    zeta = power(neg(omega), j)
    check("17 character is trivial on mu6, j=" + str(j),
          field17_pow(pair17(zeta), 48) == (1, 0))

result = {
    "status": "PASS",
    "checks": checks,
    "field_basis": ["1", "delta; delta^2=-3"],
    "characteristic_polynomial_descending": [serial(a) for a in char],
    "actual_eigenvalue": serial(lam),
    "derivative_at_actual_eigenvalue": serial(dl),
    "derivative_norm": str(dl[0] ** 2 + 3 * dl[1] ** 2),
    "projector_numerator_descending": [serial(a) for a in quotient],
    "projector": [[serial(a) for a in row] for row in Proj],
    "gamma13_finite_factors": {"at_2": "omega", "at_3": "-1", "at_17": "omega^2"},
    "original_moment_formula": "(1-pi^m/barpi^(m+1))*Omega_p^m*m!*s_m, all m>=0",
    "proof_scope": "The variable-prime full trace, integral eigenvalue, and measure identities are proved in R300; no finite prime experiment is used."
}
out = HERE / "check-jzero-complete-pcore-and-single-euler.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(f"PASS: {len(checks)} exact fixed checks; {out.name}")
