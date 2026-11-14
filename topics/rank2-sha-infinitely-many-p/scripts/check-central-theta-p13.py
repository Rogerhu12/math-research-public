#!/usr/bin/env python3
"""Exact p=13 calculation of the central Kronecker coefficient d_12.

Requires python-flint.  No floating-point arithmetic is used.
The residue field is F_(13^16); its displayed defining polynomial is lifted
coefficientwise to Z/13^5.  Every division in that ring is by a unit.
The four possible primitive f-torsion orbits are calibrated by the independently
published old moment lambda_13/13^2 = 6 mod 13 (CLS II, corrected Table I).
The new central coefficient is then computed independently from equation (33)
of notes/2026-11-12-anticyclotomic-theta-diagonal.md.
"""

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
import json
import time

from flint import fq_default_ctx, fmpz_mod_poly_ctx, fmpz_poly


P = 13
PREC = 5
MOD = P**PREC
DEG = 16
START = time.monotonic()

# A fixed irreducible polynomial, so the certificate is reproducible.
FIELD_POLY = [2, 6, 12, 9, 12, 2, 8, 12, 3] + [0] * 7 + [1]
Fp_poly = fmpz_mod_poly_ctx(P)
FF = fq_default_ctx(modulus=Fp_poly(FIELD_POLY), var="a")
RP = fmpz_mod_poly_ctx(MOD)
R_MODULUS = RP(FIELD_POLY)


class R:
    """The finite unramified ring (Z/13^5)[a]/FIELD_POLY."""

    __slots__ = ("v",)

    def __init__(self, value=0):
        if isinstance(value, R):
            self.v = value.v
        elif isinstance(value, int):
            self.v = RP([value % MOD])
        else:
            self.v = RP(value) % R_MODULUS

    @staticmethod
    def coerce(value):
        return value if isinstance(value, R) else R(value)

    def __add__(self, other):
        other = self.coerce(other)
        return R(self.v + other.v)

    __radd__ = __add__

    def __neg__(self):
        return R(-self.v)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return R((self.v * other.v) % R_MODULUS)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert exponent >= 0
        ans, base = R(1), self
        while exponent:
            if exponent & 1:
                ans *= base
            base *= base
            exponent >>= 1
        return ans

    def inverse(self):
        residue = FF([int(c) % P for c in self.v.coeffs()])
        assert residue, "nonunit denominator"
        b = R([int(c) for c in residue.inverse().to_list()])
        # Initial accuracy p, followed by p^2, p^4, p^8.
        for _ in range(3):
            b = b * (2 - self * b)
        assert self * b == 1
        return b

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def __eq__(self, other):
        return self.v == self.coerce(other).v

    def __bool__(self):
        return bool(self.v)

    def coeffs(self):
        a = [int(c) for c in self.v.coeffs()]
        return a + [0] * (DEG - len(a))

    def scalar(self):
        a = self.coeffs()
        assert not any(a[1:]), "trace did not descend to the base ring"
        return a[0]

    def residue(self):
        return FF([int(c) % P for c in self.v.coeffs()])


def ring_lift(a):
    return R([int(c) for c in a.to_list()])


def neg(A):
    return None if A is None else (A[0], -A[1])


def add(A, B):
    """Usual group law; used only when the slope denominator is a unit."""
    if A is None:
        return B
    if B is None:
        return A
    x, y = A
    xx, yy = B
    if x == xx:
        if y == -yy:
            return None
        assert y == yy
        slope = (3*x*x - 17)/(2*y)
    else:
        slope = (yy-y)/(xx-x)
    X = slope*slope-x-xx
    Y = -y+slope*(x-X)
    return X, Y


def mul(n, A):
    if n < 0:
        return mul(-n, neg(A))
    out = None
    while n:
        if n & 1:
            out = add(out, A)
        A = add(A, A)
        n >>= 1
    return out


def cm_i(A, i):
    return None if A is None else (-A[0], i*A[1])


def curve_check(A):
    if A is not None:
        x, y = A
        assert y*y == x*x*x-17*x


def cocycle_add(A, B):
    """Add (x,y,U), using E1*(A+B)=E1*(A)+E1*(B)+slope."""
    if A is None:
        return B
    if B is None:
        return A
    x, y, u = A
    xx, yy, uu = B
    if x == xx:
        if y == -yy:
            return None
        assert y == yy
        slope = (3*x*x-17)/(2*y)
    else:
        slope = (yy-y)/(xx-x)
    X = slope*slope-x-xx
    Y = -y+slope*(x-X)
    return X, Y, u+uu+slope


def cocycle_mul(n, A):
    assert n >= 0
    out = None
    while n:
        if n & 1:
            out = cocycle_add(out, A)
        A = cocycle_add(A, A)
        n >>= 1
    return out


def normalized_u(A):
    """[34]A=(0,0) and U((0,0))=0, hence U(A)=-r_34/34."""
    x, y = A
    B = cocycle_mul(34, (x, y, R(0)))
    assert B is not None and B[0] == 0 and B[1] == 0
    return -B[2]/34


def gen_minus3(A):
    B = cocycle_add(cocycle_add(A, A), A)
    return B[0], -B[1], -B[2]


def gen_minus2_plus_i(A, i):
    B = cocycle_add(A, A)
    minus2 = (B[0], -B[1], -B[2])
    iA = (-A[0], i*A[1], -i*A[2])
    return cocycle_add(minus2, iA)


# Integral division polynomial psi_17.  For even n, f_n=psi_n/(2y).
X = fmpz_poly([0, 1])
Y2 = X**3-17*X


@lru_cache(None)
def division_part(n):
    if n == 0:
        return fmpz_poly([0])
    if n in (1, 2):
        return fmpz_poly([1])
    if n == 3:
        return 3*X**4-102*X**2-289
    if n == 4:
        return 2*(X**6-85*X**4-1445*X**2+4913)
    if n % 2 == 0:
        m = n//2
        return division_part(m)*(
            division_part(m+2)*division_part(m-1)**2
            - division_part(m-2)*division_part(m+1)**2)
    m = (n-1)//2
    left = division_part(m+2)*division_part(m)**3
    right = division_part(m-1)*division_part(m+1)**3
    return 16*Y2**2*left-right if m % 2 == 0 else left-16*Y2**2*right


def polynomial_eval(coefficients, x):
    ans = R(0)
    for c in reversed(coefficients):
        ans = ans*x+int(c)
    return ans


def lift_17_point(A):
    coeff = division_part(17).coeffs()
    deriv = division_part(17).derivative().coeffs()
    x, y = map(ring_lift, A)
    for _ in range(3):
        x -= polynomial_eval(coeff, x)/polynomial_eval(deriv, x)
    assert not polynomial_eval(coeff, x)
    for _ in range(3):
        y -= (y*y-x*x*x+17*x)/(2*y)
    curve_check((x, y))
    assert mul(17, (x, y)) is None
    return x, y


# Produce a primitive f-point in the residue field.
a0, a1 = 2, -6
for n in range(2, 17):
    a0, a1 = a1, -6*a1-13*a0
group_order = 13**16+1-a1
assert group_order % 17**2 == 0 and group_order % 17**3 != 0
ii = FF(8)
assert ii*ii == -1
for seed in range(1, 100):
    x = FF.gen()+seed
    rhs = x**3-17*x
    if not rhs.is_square():
        continue
    A = (x, rhs.sqrt())
    A17 = mul(group_order//17**2, A)
    if A17 is None:
        continue
    assert mul(17, A17) is None
    if add(mul(4, A17), cm_i(A17, ii)) is None:
        continue
    if add(mul(4, A17), neg(cm_i(A17, ii))) is None:
        continue
    break
else:
    raise AssertionError("no primitive 17-torsion seed found")

fourth_root = FF(17).sqrt().sqrt()
assert fourth_root**4 == 17
Q0 = (ii*fourth_root**2, (1-ii)*fourth_root**3)
assert mul(2, Q0) == (FF(0), FF(0))

# Check the actual Frobenius direction, not just its characteristic polynomial.
for A in (A17, Q0):
    frob = (A[0]**13, A[1]**13)
    assert frob == add(mul(-3, A), mul(2, cm_i(A, ii)))

iroot = 8
for _ in range(3):
    iroot = (iroot-(iroot*iroot+1)*pow(2*iroot, -1, MOD)) % MOD
i = R(iroot)
assert i*i == -1
a = ring_lift(fourth_root)
for _ in range(3):
    a -= (a**4-17)/(4*a**3)
assert a**4 == 17
Q = (i*a*a, (1-i)*a**3)
curve_check(Q)
assert mul(2, Q) == (R(0), R(0))
R17 = lift_17_point(A17)
S = add(Q, R17)
curve_check(S)
assert mul(34, S) == (R(0), R(0))
assert mul(68, S) is None
S0 = (*S, normalized_u(S))


# Polynomial arithmetic in Z[U,X,Y]/(Y^2-X^3+17X).
# Keys are (degree_U, degree_X, degree_Y), with degree_Y in {0,1}.
def tidy(poly):
    return {key: value for key, value in poly.items() if value}


def derivation(poly):
    out = defaultdict(int)
    for (a, b, c), v in poly.items():
        if a:
            out[a-1, b+1, c] -= a*v
        if b:
            if c == 0:
                out[a, b-1, 1] += 2*b*v
            else:
                out[a, b+2, 0] += 2*b*v
                out[a, b, 0] -= 34*b*v
        if c:
            out[a, b+2, 0] += 3*v
            out[a, b, 0] -= 17*v
    return tidy(out)


C = [{(0, 0, 0): 1}]
for n in range(13):
    new = defaultdict(int, derivation(C[-1]))
    for (a, b, c), v in C[-1].items():
        new[a+1, b, c] += v
    C.append(tidy(new))
assert C[4] == {
    (4, 0, 0): 1, (2, 1, 0): -6, (1, 0, 1): -8,
    (0, 2, 0): -3, (0, 0, 0): 34}

q4 = Fraction(17, 60)
q8 = Fraction(289, 4200)+q4*q4/2
q12 = Fraction(4913, 321750)+Fraction(17*289, 60*4200)+q4**3/6
q = {0: Fraction(1), 4: q4, 8: q8, 12: q12}

# W=13*d_12 has coefficients integral at 13.  Compute it before division.
W_rat = defaultdict(Fraction)
for j, qj in q.items():
    poly = C[13-j]
    for _ in range(12):
        poly = derivation(poly)
    factor = 13*qj/Fraction(factorial(12)*factorial(13-j))
    for key, value in poly.items():
        W_rat[key] += factor*value
W_rat = tidy(W_rat)
assert all(v.denominator % 13 for v in W_rat.values())
W_mod = {
    key: (v.numerator*pow(v.denominator, -1, MOD)) % MOD
    for key, v in W_rat.items()}


def evaluate(poly, point):
    x, y, u = point
    max_u = max(a for a, _, _ in poly)
    max_x = max(b for _, b, _ in poly)
    up, xp = [R(1)], [R(1)]
    for _ in range(max_u):
        up.append(up[-1]*u)
    for _ in range(max_x):
        xp.append(xp[-1]*x)
    answer = R(0)
    for (a, b, c), value in poly.items():
        term = up[a]*xp[b]*value
        answer += term*y if c else term
    return answer


def evaluate_direct_jet(point):
    """Independent coefficient extraction from F(z+w)/(F(z)*sigma(w)).

    Raw derivatives solve X'=2Y, Y'=3X^2-17, U'=-X, F'=UF.
    Only inverse-F coefficients of degrees <=12 are needed, so their
    factorial denominators are units.  The displayed factor 13 cancels
    the sole possible p-denominator in each of the four w-contributions.
    This does not evaluate the polynomials D^12 C_k used above.
    """
    x, y, u = point
    xx, yy, uu = [x], [y], [u]
    for n in range(25):
        xx.append(2*yy[n])
        yy.append(3*sum(
            (comb(n, j)*xx[j]*xx[n-j] for j in range(n+1)), R(0))
            - (17 if n == 0 else 0))
        uu.append(-xx[n])
    ff = [R(1)]
    for n in range(25):
        ff.append(sum(
            (comb(n, j)*uu[j]*ff[n-j] for j in range(n+1)), R(0)))
    inv_factorial = [pow(factorial(n), -1, MOD) for n in range(13)]
    inverse_f = [R(1)]
    for n in range(1, 13):
        inverse_f.append(-sum(
            (ff[j]*inv_factorial[j]*inverse_f[n-j]
             for j in range(1, n+1)), R(0)))
    out = R(0)
    for j, qj in q.items():
        k = 13-j
        coefficient = sum(
            (ff[k+l]*inv_factorial[l]*inverse_f[12-l]
             for l in range(13)), R(0))
        scale = 13*qj/Fraction(factorial(k))
        assert scale.denominator % 13
        scale_mod = scale.numerator*pow(scale.denominator, -1, MOD) % MOD
        out += scale_mod*coefficient
    return out


# Independent old moment lambda_13=4 Tr(y B_5(x)).
B = {0: 1}
for n in range(5):
    new = defaultdict(int)
    for k, v in B.items():
        new[k+1] += (2*k+3)*(2*k+4)*v
        if k:
            new[k-1] -= 17*2*k*(2*k+1)*v
    B = tidy(new)
old_poly = {(0, k, 1): 4*v for k, v in B.items()}

trace_W, trace_W_jet, trace_old, trace_U = R(0), R(0), R(0), R(0)
seen = set()
row = S0
for b in range(16):
    point = row
    for a in range(16):
        key = tuple(point[0].coeffs()+point[1].coeffs())
        assert key not in seen
        seen.add(key)
        if (a, b) in ((0, 0), (3, 7), (15, 15)):
            assert point[2] == normalized_u(point[:2])
        polynomial_value = evaluate(W_mod, point)
        jet_value = evaluate_direct_jet(point)
        assert polynomial_value == jet_value, "independent jet check failed"
        trace_W += polynomial_value
        trace_W_jet += jet_value
        trace_old += evaluate(old_poly, point)
        trace_U += point[2]
        point = gen_minus3(point)
    assert point == row, "the first Galois generator did not close"
    row = gen_minus2_plus_i(row, i)
assert row == S0, "the second Galois generator did not close"
assert len(seen) == 256 and trace_U == 0 and trace_W == trace_W_jet

old_value = trace_old.scalar()
raw_W = trace_W.scalar()
assert raw_W % 13 == 0
uncalibrated_central = raw_W//13 % (13**4)
assert uncalibrated_central % 169 == 0
assert old_value % 169 == 0
old_lead = old_value//169 % 13
assert old_lead != 0
rotation_residue = 6*pow(old_lead, -1, 13) % 13
units = (R(1), i, R(-1), -i)
rotation = next(u for u in units if u.scalar() % 13 == rotation_residue)
calibrated_old = (rotation*trace_old).scalar()
assert calibrated_old//169 % 13 == 6
W_value = (rotation*trace_W).scalar()
assert W_value % 13 == 0
central = W_value//13 % (13**4)
assert central % 169 == 0


def valuation_capped(value, cap):
    if value == 0:
        return cap
    out = 0
    while out < cap and value % 13 == 0:
        value //= 13
        out += 1
    return out


certificate = {
    "modulus": MOD,
    "field_degree": DEG,
    "field_polynomial_low_to_high": FIELD_POLY,
    "i_mod_13_power_5": iroot,
    "field_curve_order": group_order,
    "seed": seed,
    "primitive_17_point_residue": [
        [int(c) for c in coord.to_list()] for coord in A17],
    "fourth_root_17_residue": [int(c) for c in fourth_root.to_list()],
    "galois_orbit_size": len(seen),
    "trace_U_mod_13_power_5": trace_U.scalar(),
    "old_moment_uncalibrated_mod_13_power_5": old_value,
    "old_moment_uncalibrated_div_13_squared_mod_13": old_lead,
    "CM_rotation_of_trace_mod_13_power_5": rotation.scalar(),
    "old_moment_calibrated_div_13_squared_mod_13": calibrated_old//169 % 13,
    "q4": str(q4),
    "q8": str(q8),
    "q12": str(q12),
    "polynomial_terms_for_13_d12": len(W_mod),
    "independent_direct_jet_matches_all_orbit_points": True,
    "central_uncalibrated_mod_13_power_4": uncalibrated_central,
    "central_uncalibrated_valuation_capped_at_4":
        valuation_capped(uncalibrated_central, 4),
    "central_d12_mod_13_power_4": central,
    "central_d12_p_adic_digits": [(central//13**j) % 13 for j in range(4)],
    "central_d12_valuation_capped_at_4": valuation_capped(central, 4),
    "elapsed_seconds": round(time.monotonic()-START, 3),
}
print(json.dumps(certificate, indent=2))
