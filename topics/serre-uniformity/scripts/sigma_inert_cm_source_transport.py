#!/usr/bin/env sage-python
"""Fixed Gaussian harmonic-seven ray-class source transport.

Run only in Rogerhu12/math-research-public GitHub Actions.
The original six-dimensional Miller/Heisenberg normalization below is
the required R812 input.  This consumer does not execute R812's six
Frobenius cases, recompute sigma jets, or loop over primes.

New arithmetic: the exact eight constant harmonic source matrices,
their integral invertibility, and their original FG/HJ transport.
Unknown scaled Eichler CM values are not evaluated or called units.
"""
import os

if (os.environ.get("GITHUB_ACTIONS") != "true"
        or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit(
        "Gaussian source transport is authorized only in "
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


# Everything above through U is the original R812 normalization.
# Pin its complete source bytes, rather than claiming an unrelated theta basis.
R812_UPSTREAM_SOURCE_SHA256 = "e7bac15678e6d0d30a30e54edd41a2d34a053b766da97efa7771278827e87ab2"

R2 = PolynomialRing(K, "sqrt2_polynomial")
L = K.extension(R2.gen()**2 - 2, "sqrt2")
sqrt2 = L.gen()
iL = L(ii)
pi2 = L(1) + iL
xi8 = pi2/sqrt2
UL = U.change_ring(L)
assert sqrt2**2 == 2 and xi8**2 == iL and xi8**8 == 1
assert pi2**7 == 8*(1-iL)

# Gaussian multiplication in the fixed ring O/3; there is no p parameter.
def mul3(x, y):
    a, b = x
    c, d = y
    return ((a*c-b*d) % 3, (a*d+b*c) % 3)

log3 = {}
cur = (1, 0)
for exponent in range(8):
    assert cur not in log3
    log3[cur] = exponent
    cur = mul3(cur, (1, 1))
assert cur == (1, 0) and len(log3) == 8
assert log3[(0, 1)] == 6

def eps3(pair, exponent):
    residue = (int(pair[0]) % 3, int(pair[1]) % 3)
    assert residue != (0, 0)
    return xi8**(exponent*log3[residue])

alpha2 = {b: eps3((1, 1), b)*pi2**7 for b in (3, 7)}
assert alpha2[3] == 8*iL*sqrt2
assert alpha2[7] == -8*iL*sqrt2
assert all(alpha2[b]**2 == -2**7 for b in (3, 7))

labels = [
    {"form": "F3", "level": 36, "oldform_exponent": 1},
    {"form": "F3", "level": 36, "oldform_exponent": 2},
    {"form": "F3", "level": 36, "oldform_exponent": 4},
    {"form": "F7", "level": 36, "oldform_exponent": 1},
    {"form": "F7", "level": 36, "oldform_exponent": 2},
    {"form": "F7", "level": 36, "oldform_exponent": 4},
    {"form": "G1", "level": 144, "oldform_exponent": 1},
    {"form": "G5", "level": 144, "oldform_exponent": 1},
]

def plus_coefficients(r, s):
    """Exact GC12/GC14/GC15 coefficients in the eight GC16 series."""
    r, s = int(r) % 6, int(s) % 6
    ans = vector(L, [0]*8)
    if r % 3 == 0 and s % 3 == 0:
        return ans
    if (r+s) % 2 == 1:
        for offset, b in ((0, 3), (3, 7)):
            q = eps3((r, s), b)**(-1)/4
            ans[offset] = q
            ans[offset+1] = -alpha2[b]*q
        delta = L(1 if r % 2 else -1)
        for offset, b in ((6, 1), (7, 5)):
            ans[offset] = (delta*eps3((r, s), b))**(-1)/4
    elif r % 2 == 1:
        # c/(1+i) = (r+s)/2 + i*(s-r)/2; both quotients are integers.
        d = ((r+s)//2, (s-r)//2)
        for offset, b in ((0, 3), (3, 7)):
            q = pi2**7*eps3(d, b)**(-1)/2
            ans[offset+1] = q
            ans[offset+2] = -alpha2[b]*q
    else:
        d = (r//2, s//2)
        for offset, b in ((0, 3), (3, 7)):
            ans[offset+2] = L(2)**6*eps3(d, b)**(-1)
    return ans

def harmonic_coefficients(r, s):
    return (plus_coefficients(r, s)-plus_coefficients(r, -s))/(2*iL)

# Checks are fixed 36-character algebra, not q-expansion matching.
for r in range(6):
    for s in range(6):
        assert plus_coefficients(-s, r) == -iL*plus_coefficients(r, s)
        h = harmonic_coefficients(r, s)
        assert harmonic_coefficients(-r, s) == h
        assert harmonic_coefficients(r, -s) == -h
        assert plus_coefficients(r, s) == iL*h-harmonic_coefficients(-s, r)

source_matrices = [
    matrix(L, 6, 6, lambda r, s: harmonic_coefficients(r, s)[nu])
    for nu in range(8)
]
theta_eo_coordinates = [(r, s) for r in range(4) for s in (1, 2)]
source_basis_matrix = matrix(L, [
    [mat[r, s] for mat in source_matrices]
    for r, s in theta_eo_coordinates
])
assert source_basis_matrix.det() != 0

# The R812 canonical theta indexing is even in the first four original
# rows and odd in the last two.  Verify it before doing this new transport.
for a in range(6):
    parity = 1 if a < 4 else -1
    for r in range(6):
        assert UL[a, (-r) % 6] == parity*UL[a, r]

transported = [UL*mat*UL.transpose() for mat in source_matrices]
original_eo_coordinates = [(a, b) for a in range(4) for b in (4, 5)]
transport_matrix = matrix(L, [
    [mat[a, b] for mat in transported]
    for a, b in original_eo_coordinates
])
assert transport_matrix.det() != 0

def padded_local(seq, n):
    return list(seq) + [0]*(n-len(seq))

def rational_coordinates(value):
    """Integral power basis sqrt2^d alpha^a i^b sqrt3^c, in that order."""
    out = []
    for cd in padded_local(L(value).list(), 2):
        for ca in padded_local(K(cd).list(), 3):
            for cb in padded_local(K1(ca).list(), 2):
                for cc in padded_local(K0(cb).list(), 2):
                    out.append(QQ(cc))
    assert len(out) == 24
    return out

power_basis = [
    sqrt2**d*L(aa)**a*L(ii)**b*L(rt)**c
    for d in range(2) for a in range(3)
    for b in range(2) for c in range(2)
]

def rebuild(coords):
    return sum((L(q)*b for q, b in zip(coords, power_basis)), L(0))

for b in power_basis:
    assert rebuild(rational_coordinates(b)) == b

def norm_to_Q(value):
    mul = matrix(QQ, [
        rational_coordinates(L(value)*b) for b in power_basis
    ]).transpose()
    return QQ(mul.det())

def integral_certificate(value):
    coords = rational_coordinates(value)
    den = ZZ(lcm([q.denominator() for q in coords]))
    norm = norm_to_Q(den*L(value))
    assert norm.denominator() == 1
    integral_norm = ZZ(norm)
    return {
        "zero": bool(value == 0),
        "power_basis_denominator": str(den),
        "denominator_factors": str(den.factor()),
        "integral_norm": str(integral_norm),
        "integral_norm_factors":
            None if integral_norm == 0 else str(abs(integral_norm).factor()),
        "power_basis_coordinates": [str(x) for x in coords],
    }

source_det_certificate = integral_certificate(source_basis_matrix.det())
source_det_den = ZZ(source_det_certificate["power_basis_denominator"])
source_det_norm = abs(ZZ(source_det_certificate["integral_norm"]))
assert all(prime == 2 for prime, exponent in source_det_den.factor())
assert all(prime == 2 for prime, exponent in source_det_norm.factor())

rows = []
for nu, label in enumerate(labels):
    rows.append({
        **label,
        "primitive_convention": "J_nu(t)=J_form(t^d)/d; theta_t J_nu=f_nu",
        "FG": integral_certificate(transported[nu][1, 5]),
        "HJ": integral_certificate(transported[nu][2, 4]),
    })

def serialize_matrix(mat, row_labels, column_labels):
    """Serialize already computed entries; no new arithmetic target."""
    return {
        "row_labels": row_labels,
        "column_labels": column_labels,
        "entries_in_power_basis": [
            [[str(q) for q in rational_coordinates(mat[r, c])]
             for c in range(mat.ncols())]
            for r in range(mat.nrows())
        ],
    }

original_names = ["S", "F", "H", "R", "J", "G"]
column_labels = [dict(label) for label in labels]

result = {
    "result": "fixed-inert-Gaussian-rayclass-source-transport",
    "source_sha256": SOURCE_SHA256,
    "R812_upstream_source_sha256": R812_UPSTREAM_SOURCE_SHA256,
    "scope": "eight exact source transports; no primes; no sigma high jets; no CM-value computation",
    "field": "Q(alpha,sqrt3,i,sqrt2), alpha^3=4, sqrt3^2=3, i^2=-1, sqrt2^2=2",
    "original_basis": ["S", "F", "H", "R", "J", "G"],
    "power_basis_order": "sqrt2^d alpha^a i^b sqrt3^c; d<2,a<3,b<2,c<2",
    "all_fixed_character_and_parity_checks_passed": True,
    "source_basis_det": source_det_certificate,
    "transport_matrix_det": integral_certificate(transport_matrix.det()),
    "normalization_pivot": first_nonzero,
    "common_scale_not_removed": "actual U(P0)=c*Uhat, so each coefficient has common c^2",
    "unknowns": "e_nu,p are the original scaled once-primitive CM values; this run does not prove any nonzero combination",
    "source_channels": rows,
    # Full exact inputs for the next consumer.  Every matrix entry uses
    # the same 24 rational coordinates listed in power_basis_order.
    "Uhat_matrix": serialize_matrix(
        UL, original_names,
        [{"theta_characteristic_r": r, "section": "Psi"} for r in range(6)]
    ),
    "source_basis_matrix": serialize_matrix(
        source_basis_matrix,
        [{"theta_first_r": r, "theta_second_s": s}
         for r, s in theta_eo_coordinates],
        column_labels
    ),
    "transport_matrix": serialize_matrix(
        transport_matrix,
        [{"original_even": original_names[a], "original_odd": original_names[b]}
         for a, b in original_eo_coordinates],
        column_labels
    ),
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":"))
print(json.dumps(result, indent=2, sort_keys=True), flush=True)
print("RESULT_SHA256=" + hashlib.sha256(encoded.encode()).hexdigest(), flush=True)
