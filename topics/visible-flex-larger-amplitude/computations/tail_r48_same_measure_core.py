#!/usr/bin/env python3
"""R48 same-measure interval kernel; complete ordinary Fraction arithmetic.

All interval operations round outwards at128 significant binary bits, without
an exponent cutoff. The old coordinate is u=8x, never the new physical u_r.
This module makes no source, ODE, root or integration call.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
from fractions import Fraction as Q
from math import comb, isqrt

BITS = 128
KEYS = ("00", "10", "01", "11", "b")
BASIS = {
    "00": (1, 0, -3, 2),
    "10": (0, 1, -2, 1),
    "01": (0, 0, 3, -2),
    "11": (0, 0, 1, -1),  # positive -q11
    "b": (0, 0, 1, -2, 1),
}


def rounded(value, upper, bits=BITS):
    value = Q(value)
    if not value:
        return Q(0)
    negative = value < 0
    x = abs(value)
    n, d = x.numerator, x.denominator
    e = n.bit_length()-d.bit_length()
    below = n < d*(1 << e) if e >= 0 else n*(1 << -e) < d
    if below:
        e -= 1
    unit = Q(2)**(e-bits+1)
    v = x/unit
    use_ceil = upper != negative
    k = ((v.numerator+v.denominator-1)//v.denominator
         if use_ceil else v.numerator//v.denominator)
    result = k*unit
    return -result if negative else result


def dyadic_record(value):
    value = Q(value)
    if not value:
        return ["0", 0]
    n, d = value.numerator, value.denominator
    if d & (d-1):
        raise ValueError("First round a rational before writing an exact dyadic")
    e = -(d.bit_length()-1)
    while not n & 1:
        n //= 2
        e += 1
    return [str(n), e]


def upper_record(value):
    return dyadic_record(rounded(value, True, 96))


def lower_record(value):
    return dyadic_record(rounded(value, False, 96))


class I:
    def __init__(self, lo=0, hi=None):
        lo, hi = Q(lo), Q(lo if hi is None else hi)
        if lo > hi:
            raise ValueError("Empty interval")
        self.lo, self.hi = rounded(lo, False), rounded(hi, True)

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = I.cast(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-I.cast(other)

    def __rsub__(self, other):
        return I.cast(other)+(-self)

    def __mul__(self, other):
        other = I.cast(other)
        values = (self.lo*other.lo, self.lo*other.hi,
                  self.hi*other.lo, self.hi*other.hi)
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.cast(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("A true denominator interval contains zero")
        return self*I(1/other.hi, 1/other.lo)

    def __rtruediv__(self, other):
        return I.cast(other)/self

    def meet(self, other):
        other = I.cast(other)
        return I(max(self.lo, other.lo), min(self.hi, other.hi))

    def nonnegative(self):
        if self.hi < 0:
            raise ValueError("A proved nonnegative integral has a negative upper end")
        return I(max(Q(0), self.lo), self.hi)

    def absmax(self):
        return max(abs(self.lo), abs(self.hi))

    def record(self):
        return [dyadic_record(self.lo), dyadic_record(self.hi)]


def sum_i(values):
    out = I(0)
    for value in values:
        out = out+value
    return out


def polynomial_range(coefficients, left, right):
    """Bernstein convex hull on a real interval; coefficients may be intervals."""
    left, right = Q(left), Q(right)
    if left > right:
        raise ValueError("Reversed polynomial argument")
    coeff = list(map(I.cast, coefficients))
    degree = len(coeff)-1
    if degree < 0:
        raise ValueError("Empty polynomial")
    width = right-left
    power = [sum_i(coeff[k]*comb(k, j)*left**(k-j)*width**j
                   for k in range(j, degree+1))
             for j in range(degree+1)]
    bernstein = [sum_i(power[k]*Q(comb(j, k), comb(degree, k))
                      for k in range(j+1))
                 for j in range(degree+1)]
    return I(min(v.lo for v in bernstein), max(v.hi for v in bernstein))


def positive_basis_range(key, left, right):
    if key not in BASIS or not 0 <= Q(left) <= Q(right) <= 1:
        raise ValueError("Old basis coordinate must stay in[0,1]")
    # Every one of these five fixed functions is in[0,1] there.
    return polynomial_range(BASIS[key], left, right).meet(I(0, 1))


def endpoint(H, Hr, Hrr, w, wr, rx, source_width=Q(1, 8)):
    if w.lo <= 0 or rx.lo <= 0:
        raise ValueError("Actual endpoint geometry must be positive")
    K = Hr/w
    D = source_width*rx*(Hrr/w-wr*Hr/(w*w))
    return {"H": H, "K": K, "D": D}


def old_candidate(left, right, total, old_lambda):
    if total["b"].lo <= 0:
        raise ValueError("The same true bubble integral has no positive lower bound")
    a, ad, b, bd = left["K"], left["D"], right["K"], right["D"]
    lam = ((right["H"]-left["H"]-a*total["00"]-ad*total["10"]
            -b*total["01"]+bd*total["11"])/total["b"]).meet(old_lambda)
    coeff = [a, ad, -3*a-2*ad+3*b-bd+lam,
             2*a+ad-2*b+bd-2*lam, lam]
    return dict(left=left, right=right, lam=lam,
                weights=(a, ad, b, -bd, lam), coeff=coeff)


def evaluate_old(candidate, uleft, uright, pre, post, source_rx):
    if source_rx.lo <= 0:
        raise ValueError("Physical derivative conversion lost positive rx")
    coeff = candidate["coeff"]
    K = polynomial_range(coeff, uleft, uright)
    Ku = polynomial_range([k*coeff[k] for k in range(1, 5)], uleft, uright)
    Kr = 8*Ku/source_rx
    Hleft = candidate["left"]["H"]+sum_i(
        z*pre[k] for k, z in zip(KEYS, candidate["weights"]))
    Hright = candidate["right"]["H"]-sum_i(
        z*post[k] for k, z in zip(KEYS, candidate["weights"]))
    return {"H": Hleft.meet(Hright), "Kbar": K, "Kbar_r": Kr}


def sqrt_upper(q):
    q = Q(q)
    if q < 0:
        raise ValueError("Negative square-root input")
    scale = 1 << 128
    numerator = q.numerator*scale*scale
    n = isqrt(numerator//q.denominator)
    if n*n*q.denominator < numerator:
        n += 1
    return Q(n, scale)


def centred_geometry(r, w, E, A, D, pnorm, knorm, tnorm, eP, eK, eT, dc):
    """R103 for two actual candidate references in a shared centred gauge."""
    if min(r, w, A, D) <= 0:
        raise ValueError("Complete real geometry margins are required")
    A, nu2 = min(Q(1), A), min(Q(1), D/E)
    p = min(w*(1+knorm), sqrt_upper(1-nu2))
    q = min(w*pnorm, sqrt_upper(1-A))
    qt = w*tnorm
    dp, dq, dqt = w*(eK+dc), w*eP, w*eT
    # A<=sqrt(A) and nu2<=sqrt(nu2), so both are safe lower bounds.
    s, nu = A, nu2
    v = p*dp+q*dq
    dnu, inv = v/nu, v/nu**3
    g = (inv+(dp*qt+p*dqt)/(s*s*nu)
         +p*qt*(2*q*dq/(s**4*nu)+inv/(s*s)))
    da = r*q*dq/s
    pi = Q(22, 7)
    phase = pi*g/4
    xy = pi*da/2+pi*pi*r*g/16
    component = dnu*(1+q/s)+(dp+dq)/s+(q*q+p*q)*dq/s**3
    normal = component+min(Q(1), p+q)*min(Q(2), phase)
    return dict(centred_xy=xy, reference_vector=normal, angle=phase,
                p=p, q=q, qt=qt, dp=dp, dq=dq, dqt=dqt,
                A=A, nu_squared=nu2, turn_rate=g)


def exact_basis_checks():
    """Finite exact algebra checks, not an actual-data or solution certificate."""
    def value(c, x):
        return sum((Q(v)*x**j for j, v in enumerate(c)), Q(0))
    def deriv(c, x):
        return sum((Q(j*v)*x**(j-1) for j, v in enumerate(c) if j), Q(0))
    expected = {"00": (1, 0, 0, 0), "10": (0, 0, 1, 0),
                "01": (0, 1, 0, 0), "11": (0, 0, 0, -1), "b": (0, 0, 0, 0)}
    for key, c in BASIS.items():
        actual = value(c, Q(0)), value(c, Q(1)), deriv(c, Q(0)), deriv(c, Q(1))
        if actual != expected[key]:
            raise ArithmeticError("A fixed positive basis endpoint identity changed")
    a = list(BASIS["00"])+[0]
    b = list(BASIS["01"])+[0]
    if [x+y for x,y in zip(a,b)] != [1, 0, 0, 0, 0]:
        raise ArithmeticError("I00+I01 is not the full true mass")
    for power in range(5):
        c = [I(int(j == power)) for j in range(5)]
        box = polynomial_range(c, Q(1, 7), Q(5, 8))
        for x in (Q(1, 7), Q(1, 4), Q(1, 3), Q(1, 2), Q(5, 8)):
            if not box.lo <= x**power <= box.hi:
                raise ArithmeticError("A power basis escaped its Bernstein interval")
    for sign in (-1, 1):
        for x in (Q(1, 3), Q(1, 2**300), Q(2**300, 3)):
            if not rounded(sign*x, False) <= sign*x <= rounded(sign*x, True):
                raise ArithmeticError("Directed rounding lost its exact number")
    return dict(five_endpoint_value_and_derivative_identities=True,
                positive_basis_partition_of_unity=True,
                five_power_basis_Bernstein_enclosures=True,
                signed_rounding_small_and_large_exponents=True)
