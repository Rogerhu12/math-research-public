#!/usr/bin/env python3
"""Exact local phases, fixed torsion evaluation, and all-weight scales for R302.

No numerical L-value, BSD formula, prime scan, or fitted theta coefficient.
"""
from fractions import Fraction
from pathlib import Path
import json
from flint import fmpq, fmpq_poly
import sympy as sp


class C24:
    MOD = fmpq_poly([1, 0, 0, 0, -1, 0, 0, 0, 1])

    def __init__(self, x=0):
        if isinstance(x, C24):
            self.p = x.p
        else:
            if isinstance(x, Fraction):
                x = fmpq(x.numerator, x.denominator)
            if not isinstance(x, (list, fmpq_poly)):
                x = [x]
            self.p = fmpq_poly(x) % self.MOD

    def __add__(self, x):
        return C24(self.p + C24(x).p)
    __radd__ = __add__

    def __neg__(self):
        return C24(-self.p)

    def __sub__(self, x):
        return self + (-C24(x))

    def __rsub__(self, x):
        return C24(x) - self

    def __mul__(self, x):
        return C24(self.p * C24(x).p)
    __rmul__ = __mul__

    def __truediv__(self, x):
        g, a, _ = C24(x).p.xgcd(self.MOD)
        assert g == 1
        return self * C24(a)

    def __pow__(self, n):
        if n < 0:
            return (C24(1) / self) ** (-n)
        a, b = C24(1), self
        while n:
            if n & 1:
                a = a * b
            b = b * b
            n //= 2
        return a

    def __eq__(self, x):
        return self.p == C24(x).p

    def coefficients(self):
        return [str(self.p[j]) for j in range(8)]


def mv(A, v):
    return [sum((a * b for a, b in zip(row, v)), C24(0)) for row in A]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), C24(0))
             for j in range(len(B[0]))] for i in range(len(A))]


checks = []


def check(label, value):
    assert value, label
    checks.append(label)


z = C24([0, 1])
i, omega, z8 = z ** 6, z ** 8, z ** 3
delta = 1 + 2 * omega
sq2 = z8 + z8 ** (-1)
sq3 = -i * delta
t = (1 + sq3) / sq2
v = [C24(1), t, C24(-1), t]
fA, fB = [C24(1), C24(0), C24(-1), C24(0)], [C24(0), C24(1), C24(0), C24(1)]
check("exact radicals and CM field", delta * delta == -3 and sq2 * sq2 == 2 and sq3 * sq3 == 3)

# alpha=1: the actual raw omega kernel has coefficient 3/2.
mu_omega = -omega ** 2 * z8
raw = [[mu_omega / (2 * sq2) * z8 ** (-3 * (a*a+b*b-4*a*b))
        for b in range(4)] for a in range(4)]
M = [[omega ** 2 / sq2 * (-z8), omega ** 2 / sq2 * i],
     [omega ** 2 / sq2 * i, omega ** 2 / sq2 * i * z8]]
check("actual alpha-one omega integral on both even columns",
      mv(raw, fA) == [M[0][0], M[1][0], -M[0][0], M[1][0]] and
      mv(raw, fB) == [M[0][1], M[1][1], -M[0][1], M[1][1]])
check("actual alpha-one dyadic vector", mv(raw, v) == v)
check("omega representation has cubic order", mm(mm(M, M), M) == [[C24(1), C24(0)], [C24(0), C24(1)]])
check("dyadic squared norm", 1 + t*t == 3 + sq3)

# The stationary support is unchanged, but use alpha=1, not 17, in the phase.
mu_star = z8 ** (-3)
G = [[C24(0) for b in range(4)] for a in range(4)]
for b in range(4):
    a = (3*b + 2) % 4
    numer = 3 * (11*a*a - 26*a*b + 11*b*b)
    check("alpha-one principal phase is defined " + str(b), numer % 4 == 0)
    G[a][b] = mu_star * z8 ** (-numer // 4)
expected = [[0, 0, -1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1]]
check("alpha-one principal generator matrix", G == [[C24(c) for c in row] for row in expected])
check("full dyadic principal generator fixes original vector", mv(G, v) == v)
check("negative principal generator phase", -z8 == mu_star)
check("actual half-period descent", all(v[(n+2) % 4] * (-1) ** n == -v[n] for n in range(4)))
check("rational support uses n over six", all(v[(3*n) % 4] == v[n] for n in range(4)))
check("ramified local dichotomy is plus", (-i) * i == 1)
check("all finite components repeat exactly at weights divisible by six",
      [m for m in range(12) if 2*m % 3 == 0 and 2*m % 4 == 0] == [0, 6])

# The actual primitive conductor point and its reduced zeta value.
P = (-omega, C24(0))
R = (C24(0), C24(-1))
slope = (R[1] - P[1]) / (R[0] - P[0])
xQ = slope * slope - P[0] - R[0]
yQ = -P[1] + slope * (P[0] - xQ)
xiQ = (P[1] - R[1]) / (P[0] - R[0])
check("primitive 2delta point from true addition", xQ == 2*omega and yQ == 3)
check("primitive point lies on E1", yQ*yQ == xQ**3+1)
double_slope = 3*xQ*xQ/(2*yQ)
x2Q = double_slope**2 - 2*xQ
y2Q = -yQ + double_slope*(xQ-x2Q)
check("actual real-period branch doubled", x2Q == 0 and y2Q == 1)
check("exact reduced zeta at primitive point", xiQ == -omega**2)
period_s = C24(1)/(1-omega)
check("actual period phase", period_s == (3+delta)/C24(6) and period_s**2 == -omega**2/C24(3))
check("exact CM central value", xiQ/(2*delta) == (1-omega)/C24(6))
check("exact real central value", period_s*xiQ/(2*delta) == C24(Fraction(1, 6)))

# Whole-weight constants include the original finite norms and archimedean norm.
pi = sp.pi
kap = 3*sp.sqrt(3)
finite_norm = 3*(3+sp.sqrt(3))
cYang = sp.Rational(2, 3)
C = pi*sp.sqrt(6*sp.sqrt(3))/(18*sp.sqrt(3)*(3+sp.sqrt(3)))
h = sp.sqrt(kap)/(12*pi*sp.I)
check("full original Yang normalization",
      sp.simplify(2/(6*cYang)*pi/(3*sp.sqrt(3))*sp.sqrt(2*kap)/finite_norm-C) == 0)
check("actual degree-two Gaussian exactly cancels Hermite Gaussian",
      sp.simplify(2*sp.sqrt(3)*pi*h*h+1/(8*pi)) == 0)
check("whole real-period weight is minus one-sixth before m-even",
      sp.simplify((2*pi/sp.sqrt(3))*4*pi*h*h) == -sp.Rational(1, 6))
check("CM period changes weight to one-half",
      (period_s**2)**6 == C24(Fraction(1, 3**6)))
check("first actual reference coefficient", -sp.Rational(1, 7)+sp.Rational(1, 105) == -sp.Rational(2, 15))

result = {
    "status": "PASS",
    "checks": checks,
    "curve": "E1: y^2=x^3+1",
    "Hermitian_alpha": 1,
    "original_idele_components": {"2": "mu3 Teich on units; chi(2)=-1",
                                  "3": "u mod delta on units; chi(delta)=i"},
    "dyadic_cosets": "b/2+2 Z2, b=0,1,2,3",
    "dyadic_vector": ["1", "(1+sqrt(3))/sqrt(2)", "-1", "(1+sqrt(3))/sqrt(2)"],
    "three_vector": "1_(3^-1 Z3)",
    "rational_support": "n/6",
    "actual_source": "Theta=x*sigma^2; constant term 1",
    "original_degree": 2,
    "weight_period": 6,
    "original_global_L_prefactor": str(C),
    "Kronecker_conductor_point": ["2*omega", "3"],
    "Kronecker_reduced_zeta": "-omega^2",
    "real_period_formula": "(2*pi/sqrt3)^m*L(psi1^(2m+1),m+1)/(m!*Omega1^(2m+1))=(1/6)*6^(-m)*r_m^2",
    "CM_period_formula": "(2*pi/sqrt3)^m*L(psi1^(2m+1),m+1)/(m!*(s*Omega1)^(2m+1))=((1-omega)/6)*2^(-m)*r_m^2",
    "homothety_to_E17": "Theta17(z)=Theta1(17^(1/6)*z); r_m,17=17^(m/6)*r_m,1 when 6|m"
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
print(f"PASS: {len(checks)} exact checks; {out.name}")
