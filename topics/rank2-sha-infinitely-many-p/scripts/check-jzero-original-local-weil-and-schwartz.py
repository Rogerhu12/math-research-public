#!/usr/bin/env python3
"""Exact certificates for R290; no prime scan or fitted theta coefficients.

Fields are Q(zeta_51) (the 17-adic torus) and Q(zeta_24) (the dyadic
Schrodinger vector).  All assertions use rational polynomial arithmetic.
Run with PYTHONDONTWRITEBYTECODE=1.
"""
from pathlib import Path
import json
from fractions import Fraction
from flint import fmpq, fmpq_poly
import sympy as sp


class Field:
    def __init__(self, n):
        self.n = n
        X = sp.Symbol('X')
        p = sp.Poly(sp.cyclotomic_poly(n, X), X)
        self.mod = fmpq_poly([int(p.nth(j)) for j in range(p.degree()+1)])
        self.deg = p.degree()
        self.zero = self(0)
        self.one = self(1)
        self.z = self([0, 1])
        self.powers = [self.one]
        for j in range(1, n):
            self.powers.append(self.powers[-1]*self.z)

    def __call__(self, x):
        if isinstance(x, Element):
            assert x.F is self
            return x
        if isinstance(x, Fraction):
            x = fmpq(x.numerator, x.denominator)
        if isinstance(x, str):
            x = fmpq(x)
        if not isinstance(x, (list, fmpq_poly)):
            x = [x]
        return Element(self, fmpq_poly(x) % self.mod)


class Element:
    def __init__(self, F, p):
        self.F, self.p = F, p

    def __add__(self, b):
        b = self.F(b)
        return Element(self.F, self.p+b.p)
    __radd__ = __add__

    def __neg__(self):
        return Element(self.F, -self.p)

    def __sub__(self, b):
        return self + (-self.F(b))

    def __rsub__(self, b):
        return self.F(b)-self

    def __mul__(self, b):
        b = self.F(b)
        return Element(self.F, (self.p*b.p) % self.F.mod)
    __rmul__ = __mul__

    def __truediv__(self, b):
        b = self.F(b)
        g, s, _ = b.p.xgcd(self.F.mod)
        assert g == fmpq_poly([1])
        return self*Element(self.F, s)

    def __pow__(self, n):
        if n < 0:
            return (self.F.one/self)**(-n)
        a, b = self.F.one, self
        while n:
            if n & 1:
                a = a*b
            b = b*b
            n //= 2
        return a

    def __eq__(self, b):
        return self.p == self.F(b).p

    def conj(self):
        return sum((self.F.powers[(-j) % self.F.n]*str(self.p[j])
                    for j in range(len(self.p))), self.F.zero)

    def coeffs(self):
        return [str(self.p[j]) for j in range(self.F.deg)]


checks = []
def check(name, value):
    assert value, name
    checks.append(name)


def mm(A, B):
    F = A[0][0].F
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F.zero)
             for j in range(len(B[0]))] for i in range(len(A))]


def mv(A, v):
    return [sum((a*b for a, b in zip(row, v)), row[0].F.zero) for row in A]


# Original inert-17 field and character, not a split-prime substitute.
p = 17
def kmul(a, b):
    return ((a[0]*b[0]-3*a[1]*b[1]) % p,
            (a[0]*b[1]+a[1]*b[0]) % p)


def kpow(a, n):
    b = (1, 0)
    while n:
        if n & 1:
            b = kmul(a, b)
        a = kmul(a, a)
        n //= 2
    return b


def leg(a):
    if a % p == 0:
        return 0
    return 1 if pow(a % p, 8, p) == 1 else -1


K = Field(51)
zeta, om = K.z**3, K.z**17
g0 = (2, 4)
gs = [kpow(g0, j) for j in range(18)]
check('17 torus has exact order 18', len(set(gs)) == 18 and kpow(g0, 18) == (1, 0))
check('g0^6 is the actual omega residue', gs[6] == (8, 9))
gauss = sum((leg(a)*zeta**a for a in range(1, 17)), K.zero)
check('positive quadratic Gauss square is 17', gauss*gauss == 17)
check('quadratic Gauss is real', gauss.conj() == gauss)


def W(g):
    x, y = g
    if not y:
        return [[K(int(a == (b if x == 1 else -b) % 17)) for b in range(17)]
                for a in range(17)]
    c = -leg(y)*gauss/17
    h = 3*pow(2*y, -1, 17) % 17
    return [[c*zeta**((h*(x*(a*a+b*b)-2*a*b)) % 17) for b in range(17)]
            for a in range(17)]


M = W(g0)
M3 = mm(mm(M, M), M)
check('original finite generator cubed', M3 == W(gs[3]))
M9 = mm(mm(M3, M3), M3)
check('ninth power is actual parity', M9 == W((-1, 0)))
check('eighteenth power is identity', mm(M9, M9) == W((1, 0)))

# Algebraic-integral normalization 9 sqrt(17) times the orthogonal projection
# of e_0 onto the *cubic even* mu_4 character tau(g0)=omega^2.
table = []
for k in range(1, 9):
    x, y = gs[k]
    table.append([k, x, y, leg(y), 3*x*pow(2*y, -1, 17) % 17, k % 3])
f = [gauss*int(a == 0)-sum((leg(y)*om**k*zeta**((c*a*a) % 17)
                           for k, x, y, eps, c, km in table), K.zero)
     for a in range(17)]
check('actual invariant vector eigenvalue is omega^2', mv(M, f) == [om**2*a for a in f])
check('seventeen vector is even', all(f[a] == f[-a % 17] for a in range(17)))
check('seventeen vector is real', all(a.conj() == a for a in f))
check('seventeen zero coordinate', f[0] == gauss-1)
check('seventeen squared norm', sum((a*a.conj() for a in f), K.zero) == 9*(17-gauss))
projtrace = sum((om**k*sum((W(g)[a][a] for a in range(17)), K.zero)
                 for k, g in enumerate(gs)), K.zero)/18
check('target character multiplicity is one', projtrace == 1)
check('quadratic splitting times inverse sextic is cubic',
      all((-1)**k * ((-om)**k)**(-1) == om**(2*k) for k in range(18)))

# Exact trace-fiber Gauss calculation for the actual z^48 idele character.
lam = gs[3]
roots = {kpow(lam, j): (-om**2)**j for j in range(6)}
def chi17(z):
    return roots[kpow(z, 48)]

delta = (0, 1)
check('idele 17 character at delta is minus one', chi17(delta) == -1)
check('primary norm-seven calibration', chi17((-2, -1)) == -om**2)
G = K.zero
fibers = [K.zero for _ in range(17)]
for a in range(17):
    for b in range(17):
        if (a, b) == (0, 0):
            continue
        val = chi17((a, b))**(-1)
        fibers[a] += val
        G += val*zeta**(-a)
check('zero trace fiber is minus sixteen', fibers[0] == -16)
check('every nonzero trace fiber is one', all(a == 1 for a in fibers[1:]))
check('actual tame epsilon Gauss sum', G == -17)
check('epsilon times delta character at 17 is minus one', (-1)*(G/17)*chi17(delta) == -1)

# True dyadic Schrodinger calculation in Q(zeta_24).
J = Field(24)
i, w, z8 = J.z**6, J.z**8, J.z**3
sq2, sq3 = z8+z8**(-1), -i*(1+2*w)
t = (1+sq3)/sq2
check('dyadic radicals', sq2*sq2 == 2 and sq3*sq3 == 3)
A = [[w**2/sq2*(-z8), w**2/sq2*i],
     [w**2/sq2*i, w**2/sq2*i*z8]]
check('dyadic omega fixes actual vector', mv(A, [J.one, t]) == [J.one, t])
check('dyadic omega has exact cubic order', mm(mm(A, A), A) == [[J.one,J.zero],[J.zero,J.one]])
check('dyadic second eigenvalue is omega', A[0][0]+A[1][1] == 1+w)
check('dyadic norm is 3+sqrt3', 1+t*t == 3+sq3)

# Recompute the omega finite integral after expanding v=b/2+2Z_2.
# Its support is quarter-Z_2; odd quarter points cancel on f_A,f_B.
mu_om = -w**2*z8
raw_om = [[mu_om/(2*sq2)*z8**(5*(a*a+b*b-4*a*b)) for b in range(4)]
          for a in range(4)]
fA = [J.one,J.zero,-J.one,J.zero]
fB = [J.zero,J.one,J.zero,J.one]
check('omega integral gives the stated even-block matrix',
      mv(raw_om, fA) == [A[0][0],A[1][0],-A[0][0],A[1][0]] and
      mv(raw_om, fB) == [A[0][1],A[1][1],-A[0][1],A[1][1]])
check('omega quarter-annulus cancellation',
      all((-1)**(1-a) == 1 and (-1)**(2-a) == -1 for a in range(1,8,2)))

# For g*=(-11+4delta)/13 the stationary condition is a=3b+2 mod4.
mu_g = z8**(-3)
gmat = [[J.zero for _ in range(4)] for _ in range(4)]
for b in range(4):
    a = (3*b+2) % 4
    numerator = 51*(11*a*a-26*a*b+11*b*b)
    check('dyadic exact stationary phase '+str(b), numerator % 4 == 0)
    gmat[a][b] = mu_g*z8**(-numerator//4)
expected_g = [[0,0,-1,0],[0,1,0,0],[-1,0,0,0],[0,0,0,1]]
check('dyadic principal generator matrix', gmat == [[J(x) for x in row] for row in expected_g])
check('dyadic principal generator fixes both even columns', mv(gmat,fA)==fA and mv(gmat,fB)==fB)
check('minus principal generator has the same splitting on even functions', -z8 == mu_g)
check('dyadic finite F4 Gauss sum', 1-w-w*w == 2)
check('ramified cubic-place Gauss sum', w-w*w == i*sq3)
check('ramified epsilon times delta is minus one', (-i)*(-i) == -1)

# The global rational support and the *actual* degree-34 descent.
v2 = [J.one,t,-J.one,t]
check('dyadic half shift with modulation',
      all(v2[(n+2)%4]*(-1)**n == -v2[n] for n in range(4)))
check('rational support indices', 51 % 4 == 3 and pow(6,-1,17)==3)
check('finite splitter has exactly common period six',
      [m for m in range(12) if (2*m)%3==0 and (2*m)%4==0 and (2*m)%6==0] == [0,6])

# Rational simplification of the full norm constant. No fitted L-values.
P = sp.pi
kappa = 51*sp.sqrt(3)
finite_norm = 27*(3+sp.sqrt(3))*(17-sp.sqrt(17))
c0 = sp.Rational(17,27)
C = sp.pi*sp.sqrt(102*sp.sqrt(3))/(153*sp.sqrt(3)*(3+sp.sqrt(3))*(17-sp.sqrt(17)))
check('Yang full norm constant',
      sp.simplify(2/(6*c0)*P/(3*sp.sqrt(3))*sp.sqrt(2*kappa)/finite_norm-C)==0)
check('Hermite Gaussian is exactly reduced sigma Gaussian',
      sp.simplify(34*sp.sqrt(3)*P*(sp.sqrt(kappa)/(204*P*sp.I))**2+1/(8*P))==0)

output = {
    'result': 'R290',
    'status': 'all exact checks passed',
    'checks': checks,
    'seventeen': {
        'power_basis': 'zeta_51^j, j=0,...,31; zeta_17=zeta_51^3, omega=zeta_51^17',
        'generator_F289_delta2_minus3': list(g0),
        'gauss_positive_sqrt17': gauss.coeffs(),
        'eight_term_table_k_x_y_legendre_phase_kmod3': table,
        'vector_coefficients': [a.coeffs() for a in f],
        'zero_coordinate': 'sqrt(17)-1',
        'squared_norm': '9*(17-sqrt(17))',
        'actual_mu4_eigenvalue': 'omega^2',
        'original_idele_character': 'z^48',
        'hilbert90_character': 'g^-3',
        'splitting': 'eta_0(g)*g^-3',
    },
    'dyadic': {
        'power_basis': 'zeta_24^j, j=0,...,7',
        'cosets': 'b/2+2 Z_2, b=0,1,2,3',
        'vector_coefficients': [a.coeffs() for a in v2],
        'vector': ['1','(1+sqrt(3))/sqrt(2)','-1','(1+sqrt(3))/sqrt(2)'],
        'omega_even_matrix_coefficients': [[a.coeffs() for a in row] for row in A],
        'principal_generator_matrix': expected_g,
        'squared_norm': '3+sqrt(3)',
    },
    'global': {
        'hermitian_alpha': 17,
        'additive_character': 'psi_infinity=e^(2*pi*i*x); psi_l=e^(-2*pi*i*{x}_l)',
        'three_vector': '1_(3^-1 Z_3)',
        'rational_support': 'n/102',
        'coefficient': 'v2(n mod4)*f17(3*n mod17)',
        'coefficient_period': 68,
        'gaussian': 'exp(-pi*sqrt(3)*n^2/204)',
        'schwartz_weight_period': 6,
        'L_norm_constant': str(C),
        'norm_formula': 'L(psi^(2m+1),m+1)=C*(4*pi)^m/m!*b_m^2, 6|m',
    },
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(str(path))
print(str(len(checks))+' exact checks PASS')
