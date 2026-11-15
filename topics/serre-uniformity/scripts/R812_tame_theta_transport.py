#!/usr/bin/env sage-python
"""R812: exact, fixed-size CM level-six Heisenberg/Frobenius transport.

Run only in Rogerhu12/math-research-public GitHub Actions:
    sage -python topics/serre-uniformity/scripts/R812_tame_theta_transport.py

No prime loop and no sigma Taylor window is computed.  The six cases are
the three actual tame Frobenius automorphisms at p = 5 mod 12, crossed
with the two normalized Gaussian-prime residues 1 +/- 2i modulo 6.
All arithmetic is exact in Q(cuberoot(4), sqrt(3), i).
"""
import os

if (os.environ.get("GITHUB_ACTIONS") != "true"
        or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit(
        "R812 formal arithmetic is authorized only in "
        "Rogerhu12/math-research-public GitHub Actions."
    )

# Metadata and source hashing only.  No Sage import or mathematical work
# occurs before the repository/Actions contract above has passed.
from pathlib import Path
import hashlib
import json
import platform

SOURCE_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
RUN_METADATA = {
    "repository": os.environ["GITHUB_REPOSITORY"],
    "github_actions": os.environ["GITHUB_ACTIONS"],
    "workflow": os.environ.get("GITHUB_WORKFLOW"),
    "event_name": os.environ.get("GITHUB_EVENT_NAME"),
    "run_id": os.environ.get("GITHUB_RUN_ID"),
    "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
    "source_commit": os.environ.get("GITHUB_SHA"),
    "source_ref": os.environ.get("GITHUB_REF"),
    "source_path": str(Path(__file__).resolve()),
    "source_sha256": SOURCE_SHA256,
    "python_version": platform.python_version(),
}
print("EXECUTION_METADATA=" + json.dumps(RUN_METADATA, sort_keys=True), flush=True)

from sage.all import (
    QQ, ZZ, QuadraticField, PolynomialRing, matrix, vector,
    identity_matrix, diagonal_matrix, zero_matrix, lcm
)
import sage.version
print("SAGE_VERSION=" + sage.version.version, flush=True)

K0 = QuadraticField(3, "sqrt3")
R0 = PolynomialRing(K0, "I")
K1 = K0.extension(R0.gen()**2 + 1, "ii")
R1 = PolynomialRing(K1, "A")
K = K1.extension(R1.gen()**3 - 4, "alpha")
rt = K(K0.gen())
ii = K(K1.gen())
aa = K.gen()
zeta = (-1 + ii*rt)/2
rho = (1 + ii*rt)/2

assert rt**2 == 3 and ii**2 == -1 and aa**3 == 4
assert zeta**2 + zeta + 1 == 0 and rho**2 == zeta and rho**6 == 1

RX = PolynomialRing(K, "x")
KF = RX.fraction_field()
xx = KF(RX.gen())
curve_rhs = xx**3 - 1

class EF:
    """The exact field K(x)[y]/(y^2-x^3+1), represented by a+b*y."""
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        if isinstance(a, EF):
            assert b == 0
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = KF(a), KF(b)
    @staticmethod
    def cv(v):
        return v if isinstance(v, EF) else EF(v)
    def __add__(self, other):
        other = EF.cv(other)
        return EF(self.a+other.a, self.b+other.b)
    __radd__ = __add__
    def __neg__(self):
        return EF(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-EF.cv(other))
    def __rsub__(self, other):
        return EF.cv(other) - self
    def __mul__(self, other):
        other = EF.cv(other)
        return EF(self.a*other.a + self.b*other.b*curve_rhs,
                  self.a*other.b + self.b*other.a)
    __rmul__ = __mul__
    def inverse(self):
        den = self.a**2 - curve_rhs*self.b**2
        assert den != 0
        return EF(self.a/den, -self.b/den)
    def __truediv__(self, other):
        return self * EF.cv(other).inverse()
    def __rtruediv__(self, other):
        return EF.cv(other) * self.inverse()
    def __pow__(self, n):
        n = int(n)
        if n < 0:
            return self.inverse()**(-n)
        ans, cur = EF(1), self
        while n:
            if n & 1:
                ans = ans*cur
            cur = cur*cur
            n >>= 1
        return ans
    def __eq__(self, other):
        other = EF.cv(other)
        return self.a == other.a and self.b == other.b

X = EF(xx)
Y = EF(0, 1)
assert Y**2 == X**3 - 1

def polynomial_part(frac):
    den = RX(frac.denominator())
    assert den.degree() == 0
    return RX(frac.numerator()) * K(den[0])**(-1)

def original_coordinates(fun):
    """Coordinates in (S,F,H,R,J,G)/sigma^6=(1,x,x^2,x^3+2,y,-xy)."""
    pa, pb = polynomial_part(fun.a), polynomial_part(fun.b)
    assert pa.degree() <= 3 and pb.degree() <= 1
    out = vector(K, [pa[0]-2*pa[3], pa[1], pa[2], pa[3], pb[0], -pb[1]])
    rebuilt = (
        EF(out[0]) + out[1]*X + out[2]*X**2
        + out[3]*(X**3+2) + out[4]*Y - out[5]*X*Y
    )
    assert rebuilt == fun
    return out

def translation_matrix(u, v, multiplier):
    """Rows H satisfy T_P Phi = H Phi; T_P f = multiplier * f(.+P)."""
    assert v*v == u*u*u - 1
    slope = (Y-v)/(X-u)
    xt = slope**2 - X - u
    yt = -Y + slope*(X-xt)
    assert yt**2 == xt**3 - 1
    translated = [EF(1), xt, xt**2, xt**3+2, yt, -xt*yt]
    return matrix(K, [list(original_coordinates(multiplier*f)) for f in translated])

def real_line_operators(xi):
    # Points xi*(Omega/2)=(xi,0), xi*(Omega/3)=(xi*alpha,-sqrt(3)).
    # The constants are fixed by canonical sigma translation and positive
    # real normalization on the original real period; CM transports them.
    h2 = translation_matrix(xi, K(0), (X-xi)**3/(3*rt))
    u3 = xi*aa
    line_minus_p3 = Y + rt - (rt*u3**2/2)*X
    h3 = translation_matrix(u3, -rt, line_minus_p3**2/12)
    ident = identity_matrix(K, 6)
    assert h2**2 == ident
    assert h3**3 == ident
    assert h2*h3 == h3*h2
    # Q = Omega/6 = Omega/2 - Omega/3.
    h6 = h3.inverse()*h2
    assert h6**2 == h3 and h6**3 == h2 and h6**6 == ident
    return h6, h2, h3

HQ, HQ2, HQ3 = real_line_operators(K(1))
HP, HP2, HP3 = real_line_operators(zeta)
ident = identity_matrix(K, 6)

# P=zeta*Omega/6, Q=Omega/6.  The displayed row convention reverses
# composition matrices, so canonical T_Q T_P=rho T_P T_Q is the check below.
assert HP*HQ == rho*HQ*HP

ker = (HQ-ident).right_kernel()
assert ker.dimension() == 1
u0 = vector(K, ker.basis()[0])
first_nonzero = next(j for j in range(6) if u0[j] != 0)
u0 = u0/u0[first_nonzero]
U = matrix(K, [list(HP**(-r)*u0) for r in range(6)]).transpose()
assert U.det() != 0
diag = diagonal_matrix(K, [rho**r for r in range(6)])
shift = matrix(K, 6, 6, lambda r, c: K(1) if c == (r+1) % 6 else K(0))
assert HQ*U == U*diag and HP*U == U*shift
V = U.inverse()

# Fifth derivative at z=0 of Phi(z) Phi(-i*z)^t, at the ORIGINAL CM point.
# Basis order S,F,H,R,J,G.  This is a low jet identity, not a computed p jet.
K5 = zero_matrix(K, 6)
K5[5, 1] = 120
K5[4, 2] = 120
K5[1, 5] = -120*ii
K5[2, 4] = -120*ii
Theta5 = V*K5*V.transpose()

def padded(seq, n):
    return list(seq) + [0]*(n-len(seq))

def rational_coordinates(value):
    """Integral power basis alpha^a i^b sqrt(3)^c, a<3,b<2,c<2."""
    out = []
    for ca in padded(K(value).list(), 3):
        for cb in padded(K1(ca).list(), 2):
            for cc in padded(K0(cb).list(), 2):
                out.append(QQ(cc))
    assert len(out) == 12
    return out

power_basis = [aa**a * ii**b * rt**c
               for a in range(3) for b in range(2) for c in range(2)]

def rebuild(coords):
    return sum((K(q)*b for q, b in zip(coords, power_basis)), K(0))

for b in power_basis:
    assert rebuild(rational_coordinates(b)) == b

def tau(value, j):
    # At p=5 mod12: i^p=i, sqrt(3)^p=-sqrt(3),
    # alpha^p=zeta^j alpha for exactly one j in {0,1,2}.
    coords = rational_coordinates(value)
    out = K(0)
    idx = 0
    for a in range(3):
        for b in range(2):
            for c in range(2):
                out += coords[idx]*(zeta**j*aa)**a*ii**b*(-rt)**c
                idx += 1
    return out

for j in range(3):
    assert tau(aa, j)**3 == 4
    assert tau(rt, j) == -rt and tau(ii, j) == ii
    assert tau(tau(aa, j), j) == aa
    for a in power_basis:
        for b in power_basis:
            assert tau(a*b, j) == tau(a, j)*tau(b, j)

def norm_to_Q(value):
    mul = matrix(QQ, [rational_coordinates(K(value)*b) for b in power_basis]).transpose()
    return QQ(mul.det())

def integral_certificate(value):
    coords = rational_coordinates(value)
    den = ZZ(lcm([q.denominator() for q in coords]))
    num_value = den*K(value)
    norm = norm_to_Q(num_value)
    assert norm.denominator() == 1
    return {
        "zero": bool(value == 0),
        "power_basis_denominator": str(den),
        "integral_norm": str(ZZ(norm)),
        "denominator_factors": str(den.factor()),
        "nonzero_integral_norm_factors": None if norm == 0 else str(abs(ZZ(norm)).factor()),
    }

cases = []
all_nonzero = True
for gaussian_sign in (1, -1):
    # pi mod6=1+2*gaussian_sign*i, determinant 5.
    # Its inverse on theta characteristics is
    # (r,s) -> (-r-2*sign*s, 2*sign*r-s) mod6.
    for frobenius_j in range(3):
        twisted = matrix(K, 6, 6,
            lambda r, s: tau(Theta5[r, s], frobenius_j))
        permuted = matrix(K, 6, 6,
            lambda r, s: twisted[(-r-2*gaussian_sign*s) % 6,
                                 (2*gaussian_sign*r-s) % 6])
        transported = U*permuted*U.transpose()
        fg = transported[1, 5]
        cert = integral_certificate(fg)
        all_nonzero = all_nonzero and not cert["zero"]
        cases.append({
            "gaussian_sign": gaussian_sign,
            "frobenius_j": frobenius_j,
            "FG": cert,
            # Audit coordinates are emitted to the public run only, not
            # proposed as repository data.
            "FG_power_basis": [str(x) for x in rational_coordinates(fg)],
        })

# Nonzero norm alone does not certify local integrality; record all U
# coordinate denominators and an integral norm certificate for det(U).
u_den = ZZ(lcm([q.denominator() for a in U.list()
               for q in rational_coordinates(a)]))
result = {
    "result": "R812-fixed-tame-theta-transport",
    "source_sha256": SOURCE_SHA256,
    "scope": "six exact algebraic cases; no prime scan; no sigma high-jet calculation",
    "field": "Q(alpha,sqrt3,i), alpha^3=4, sqrt3^2=3, i^2=-1",
    "basis": ["S","F","H","R","J","G"],
    "all_identity_checks_passed": True,
    "normalization_pivot": first_nonzero,
    "U_entry_common_denominator": str(u_den),
    "U_entry_denominator_factors": str(u_den.factor()),
    "det_U": integral_certificate(U.det()),
    "all_six_FG_outputs_nonzero": all_nonzero,
    "cases": cases,
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":"))
print(json.dumps(result, indent=2, sort_keys=True), flush=True)
print("RESULT_SHA256=" + hashlib.sha256(encoded.encode()).hexdigest(), flush=True)
