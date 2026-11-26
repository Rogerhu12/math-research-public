#!/usr/bin/env python3
"""Complete R713 exact-profile moment fees and conditional actual-seed angular/node bounds.

Only public Actions may execute the scientific bounds. The actual completed
mean batch is strictly bound by the complete pure reader and every raw hash.
Accurate input fee enclosures remain an explicit external obligation: a small
printed working residual is not accepted in their place. This component does
not certify all angles, the outer normal chain, metric, or geometry.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
from functools import lru_cache
import json
import math
import os
from pathlib import Path
import sys

SCHEMA = "complete-supported-smooth-triangle-seed-angular-and-node-error-bounds-v1"
REQUEST_SCHEMA = "actual-supported-smooth-triangle-seed-accurate-fee-request-v1"
PROVIDER_SHA = "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"
KERNEL_SHA = "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
READER_SHA = "3914004ac39b838c33411bd11660bb8fbec1372630c3569f3ea4ad5ae16c0f97"
DRIVER_SHA = "fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f"
MEAN_VECTOR_KEYS = ("v", "v_phi", "v_phiphi", "d", "d_phi", "d_phiphi",
                    "w", "w_phi", "w_phiphi")
MEAN_SCALAR_KEYS = ("lambda", "lambda_phi", "lambda_phiphi",
    "profile_moment", "profile_moment_first_derivative",
    "profile_moment_second_derivative")
FIELD_KEYS = ("T", "Tp", "Tpp", "Ts")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific fee evaluation requires the actual public repository Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
        allow_nan=False).encode()).hexdigest()


def fraction(value):
    if isinstance(value, bool):
        raise TypeError("A boolean is not a rational bound")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, str):
        raise TypeError("Bounds must be explicit rational strings or integers")
    return Fraction(value)


def nonnegative(value, name):
    result = fraction(value)
    if result < 0:
        raise ValueError("A fee or norm upper bound is negative: "+name)
    return result


def word(value):
    if isinstance(value, str):
        parsed = float.fromhex(value)
        if not math.isfinite(parsed) or parsed.hex() != value:
            raise ValueError("Use a finite canonical binary64 hex word")
        return Fraction.from_float(parsed)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("A working binary64 value is nonfinite")
        return Fraction.from_float(value)
    if isinstance(value, (int, Fraction)) and not isinstance(value, bool):
        return Fraction(value)
    raise TypeError("Working values must be exact binary words, not decimal guesses")


def lower_dyadic(value, bits):
    q = fraction(value)
    scale = 1 << bits
    return Fraction(q.numerator*scale//q.denominator, scale)


def upper_dyadic(value, bits):
    q = fraction(value)
    scale = 1 << bits
    return Fraction(-((-q.numerator*scale)//q.denominator), scale)


def sqrt_bounds(value, bits):
    q = fraction(value)
    if q < 0:
        raise ValueError("Square root of a negative exact rational")
    scale = 1 << bits
    n = math.isqrt(q.numerator*scale*scale//q.denominator)
    lo = Fraction(n, scale)
    hi = lo if lo*lo == q else Fraction(n+1, scale)
    return lo, hi


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction
    bits: int = 160

    def __post_init__(self):
        lo, hi = fraction(self.lo), fraction(self.hi)
        if lo > hi:
            raise ValueError("Reversed interval")
        if not isinstance(self.bits, int) or not 64 <= self.bits <= 1024:
            raise ValueError("Use 64..1024 bits of outward dyadic interval precision")
        object.__setattr__(self, "lo", lower_dyadic(lo, self.bits))
        object.__setattr__(self, "hi", upper_dyadic(hi, self.bits))

    def other(self, value):
        if isinstance(value, Interval):
            if value.bits != self.bits:
                raise ValueError("One calculation must retain its declared precision")
            return value
        return Interval(fraction(value), fraction(value), self.bits)

    def __add__(self, value):
        q = self.other(value)
        return Interval(self.lo+q.lo, self.hi+q.hi, self.bits)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo, self.bits)

    def __sub__(self, value):
        return self+-self.other(value)

    def __rsub__(self, value):
        return self.other(value)+-self

    def __mul__(self, value):
        q = self.other(value)
        values = (self.lo*q.lo, self.lo*q.hi, self.hi*q.lo, self.hi*q.hi)
        return Interval(min(values), max(values), self.bits)

    __rmul__ = __mul__

    def reciprocal(self):
        if self.lo <= 0 <= self.hi:
            raise ValueError("Division interval contains zero")
        return Interval(1/self.hi, 1/self.lo, self.bits)

    def __truediv__(self, value):
        return self*self.other(value).reciprocal()

    def __rtruediv__(self, value):
        return self.other(value)*self.reciprocal()

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise TypeError("Only nonnegative integer interval powers")
        if power == 0:
            return self.other(1)
        if power % 2:
            return Interval(self.lo**power, self.hi**power, self.bits)
        maximum = max(abs(self.lo), abs(self.hi))**power
        minimum = 0 if self.lo <= 0 <= self.hi else min(abs(self.lo), abs(self.hi))**power
        return Interval(minimum, maximum, self.bits)

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def intersect(self, low, high):
        lo, hi = max(self.lo, fraction(low)), min(self.hi, fraction(high))
        if lo > hi:
            raise ValueError("Independent claimed accurate enclosures are inconsistent")
        # Rounding can only enlarge a valid intersection; never round inward.
        return Interval(lo, hi, self.bits)

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("Square root requires a nonnegative interval")
        return Interval(sqrt_bounds(self.lo, self.bits)[0],
                        sqrt_bounds(self.hi, self.bits)[1], self.bits)

    def json(self):
        return [str(self.lo), str(self.hi)]


def box(value, bits):
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("Supply both endpoints of every accurate interval")
    return Interval(fraction(value[0]), fraction(value[1]), bits)


def vector_box(value, bits):
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise ValueError("World vector intervals have exactly three components")
    return [box(item, bits) for item in value]


def point_vector(value):
    if len(value) != 3:
        raise ValueError("Working world vectors have exactly three components")
    return [word(item) for item in value]


def centered_vector(values, error, bits):
    return [Interval(v-error, v+error, bits) for v in values]


def vadd(a, b):
    return [x+y for x, y in zip(a, b)]


def vsub(a, b):
    return [x-y for x, y in zip(a, b)]


def vscale(a, scale):
    return [x*scale for x in a]


def dot(a, b):
    if len(a) != len(b) or not a:
        raise ValueError("Nonempty equal vector dimensions required")
    result = a[0]*b[0]
    for x, y in zip(a[1:], b[1:]):
        result = result+x*y
    return result


def norm_box(values):
    return sum((v**2 for v in values), Interval(0, 0, values[0].bits)).sqrt()


def point_norm(values, bits):
    return sqrt_bounds(sum(v*v for v in values), bits)


def vector_error(values, working, bits):
    actual = point_vector(working)
    component = [max(abs(item.lo-v), abs(item.hi-v)) for item, v in zip(values, actual)]
    return dict(component=[upper_dyadic(q, bits) for q in component],
        norm=upper_dyadic(sqrt_bounds(sum(q*q for q in component), bits)[1], bits))


def cap_floor(zeta, bits):
    z = fraction(zeta)
    if not 0 < z <= 1:
        raise ValueError("Use a proved positive unit-direction vertical lower bound")
    # Rationalized formula avoids subtracting nearly equal square roots.
    inner_upper = sqrt_bounds(1-z*z, bits)[1]
    lower = sqrt_bounds(z*z/(2*(1+inner_upper)), bits)[0]
    if lower <= 0:
        raise ValueError("Current outward precision cannot resolve the positive cap floor")
    return lower


def normalized_jets(v0, v1, v2, *, norm_lower, norm_upper=None):
    """All accurate angle jets; interval dependence is retained conservatively."""
    radius = norm_box(v0)
    upper = radius.hi if norm_upper is None else fraction(norm_upper)
    radius = radius.intersect(norm_lower, upper)
    if radius.lo <= 0:
        raise ValueError("No paid positive normalization denominator")
    alpha = dot(v0, v1)
    beta = dot(v1, v1)+dot(v0, v2)
    d0 = vscale(v0, 1/radius)
    d1 = vsub(vscale(v1, 1/radius), vscale(v0, alpha/(radius**3)))
    d2 = vadd(vsub(vscale(v2, 1/radius),
        vscale(vadd(vscale(v1, 2*alpha), vscale(v0, beta)), 1/(radius**3))),
        vscale(v0, 3*alpha*alpha/(radius**5)))
    r1 = dot(d0, v1)
    r2 = dot(d0, v2)+dot(v1, v1)/radius-alpha*alpha/(radius**3)
    return [d0, d1, d2], [radius, r1, r2]


def trig_boxes(value, order=48):
    """Rational Taylor enclosure; global real derivative remainder <= 1."""
    if not isinstance(order, int) or order < 4:
        raise ValueError("Taylor order must be at least four")
    bits = value.bits
    sine = Interval(0, 0, bits)
    cosine = Interval(0, 0, bits)
    for j in range(order, -1, -1):
        sine = sine*value
        cosine = cosine*value
        if j % 2:
            sine = sine+Fraction((-1)**((j-1)//2), math.factorial(j))
        else:
            cosine = cosine+Fraction((-1)**(j//2), math.factorial(j))
    remainder = upper_dyadic(value.abs_upper()**(order+1)/math.factorial(order+1), bits)
    error = Interval(-remainder, remainder, bits)
    return (sine+error).intersect(-1, 1), (cosine+error).intersect(-1, 1)


@lru_cache(maxsize=16)
def pi_bounds(bits):
    """Machin identity, with alternating arctangent tails proved by integration.

    tan(4 atan(1/5)-atan(1/239))=1 by exact rational tangent
    addition, and that angle is in (0,pi/2), so it equals pi/4.
    """
    def atan_inverse(denominator):
        x = Fraction(1, denominator)
        total, power, n = Fraction(0), x, 0
        threshold = Fraction(1, 1 << (bits+12))
        while True:
            term = power/Fraction(2*n+1)
            total += term if n % 2 == 0 else -term
            power *= x*x
            n += 1
            tail = power/Fraction(2*n+1)
            if tail <= threshold:
                lo, hi = (total, total+tail) if n % 2 == 0 else (total-tail, total)
                return Interval(lo, hi, bits)
    return 16*atan_inverse(5)-4*atan_inverse(239)



@lru_cache(maxsize=32)
def _complete_absolute_profile_moments(delta, maximum_degree):
    """Exact Fraction moments of all twelve R711 pieces, with no quadrature.

    I5(u)=(5/2)u^4-3u^5+u^6.  Its nth power is advanced by exact
    polynomial convolution.  Both ramps and the complete linear middle of
    every quarter are included before the four-quarter symmetry is used.
    """
    delta = fraction(delta)
    if not 0 < delta < Fraction(1, 8):
        raise ValueError('Use the full R711 profile delta in (0,1/8)')
    if (isinstance(maximum_degree, bool) or not isinstance(maximum_degree, int)
            or maximum_degree < 0):
        raise ValueError('Use a nonnegative exact moment degree')
    c = Fraction(1, 4)-delta
    k = delta/c
    polynomial = [Fraction(1)]
    integrals = []
    for degree in range(maximum_degree+1):
        integrals.append(sum((value/Fraction(j+1)
                              for j, value in enumerate(polynomial)), Fraction(0)))
        if degree < maximum_degree:
            following = [Fraction(0)]*(len(polynomial)+6)
            for j, value in enumerate(polynomial):
                following[j+4] += Fraction(5, 2)*value
                following[j+5] -= 3*value
                following[j+6] += value
            polynomial = following
    moments = []
    for degree in range(maximum_degree+1):
        first_ramp = delta*k**degree*integrals[degree]
        last_ramp = delta*sum((Fraction((-1)**j*math.comb(degree, j))
                    *k**j*integrals[j] for j in range(degree+1)), Fraction(0))
        middle = c*((1-k/2)**(degree+1)-(k/2)**(degree+1))/Fraction(degree+1)
        moment = 4*(first_ramp+middle+last_ramp)
        if not 0 <= moment <= 1 or (degree == 0 and moment != 1):
            raise ValueError('The exact complete profile moment identity was not retained')
        moments.append(moment)
    return tuple(moments)


def complete_profile_moment_enclosures(seed, lambda_word, *, bits=160, series_order=48):
    """All three accurate A/A'/A'' boxes at this literal working amplitude.

    These are integrals of the exact R711 profile, not enclosures obtained by
    assuming the working 192-node moment quadrature is exact.  The full moment
    difference to those actual words is computed by the consuming function.
    """
    require_actions()
    if (seed.get('schema') != 'complete-supported-smooth-triangle-meridian-seed-reference-v1'
            or seed.get('source_sha256') != PROVIDER_SHA
            or seed.get('mean_kernel_source_sha256') != KERNEL_SHA
            or seed.get('mathematical_profile_piece_count') != 12
            or seed.get('mathematical_amplitude_interval') != '(0,pi)'):
        raise ValueError('Bind the complete independent R711 profile definition')
    delta = Fraction(seed['exact_profile_delta'])
    if (isinstance(series_order, bool) or not isinstance(series_order, int)
            or series_order < 2 or series_order % 2):
        raise ValueError('The complete simultaneous derivative series uses one even L>=2')
    if not isinstance(lambda_word, str):
        raise TypeError('Bind the actual canonical binary64 amplitude word')
    x = word(lambda_word)
    moments = _complete_absolute_profile_moments(delta, series_order+1)
    x_box = Interval(x, x, bits)
    x2 = x_box*x_box
    values = []
    remainders = []
    for derivative in range(3):
        first_even = 0 if derivative == 0 else 2
        total = Interval(0, 0, bits)
        for degree in range(series_order, first_even-1, -2):
            coefficient = (Fraction((-1)**(degree//2))*moments[degree]
                           /math.factorial(degree-derivative))
            total = total*x2+coefficient
        if derivative == 1:
            total = x_box*total
        power = series_order+1-derivative
        remainder = moments[series_order+1]*abs(x)**power/math.factorial(power)
        values.append(total+Interval(-remainder, remainder, bits))
        remainders.append(remainder)
    proof_identity = dict(exact_profile_delta=str(delta), maximum_absolute_moment_degree=series_order+1,
        absolute_moments=[str(value) for value in moments])
    return dict(intervals=values, derivative_orders=[0, 1, 2],
        exact_profile_delta=str(delta), actual_lambda_binary64_hex=lambda_word,
        even_series_order=series_order, precision_bits=bits,
        exact_absolute_moment_identity_sha256=canonical(proof_identity),
        exact_mass=moments[0], exact_remainder_moment=moments[series_order+1],
        exact_Taylor_remainder_upper=remainders,
        all_twelve_profile_pieces_in_exact_moments=True,
        exact_Fraction_polynomial_integrals=True,
        polynomial_evaluation_outward_dyadic=True,
        working_quadrature_or_trigonometric_accuracy_assumed=False,
        accurate_moment_enclosures_computed_here=True)


def central_profile_enclosures(t, delta, physical_length):
    """Exact-profile h and physical h_s on the supplied accurate t interval.

    The caller still owns the association of that interval to the declared
    actual node address; this function proves the profile evaluation itself.
    """
    require_actions()
    bits = t.bits
    delta = fraction(delta)
    if (not 0 < delta < Fraction(1, 8) or t.lo < 0 or t.hi > 1
            or physical_length.lo <= 0 or physical_length.bits != bits):
        raise ValueError('Use a complete positive R711 profile length and t subset [0,1]')
    a = Fraction(1, 4)
    c = a-delta
    values, derivatives, pieces = [], [], []

    def I5(u):
        return u**4*(Fraction(5, 2)+u*(-3+u))

    def S5(u):
        return u**3*(10+u*(-15+6*u))

    for quarter in range(4):
        left, right = quarter*a, (quarter+1)*a
        sign = 1 if quarter < 2 else -1
        orientation = 1 if quarter % 2 == 0 else -1
        edges = (left, left+delta, right-delta, right)
        for index in range(3):
            lo, hi = max(t.lo, edges[index]), min(t.hi, edges[index+1])
            if lo > hi:
                continue
            local = Interval(lo, hi, bits)
            x = local-left if orientation == 1 else right-local
            # The x-region is determined by the exact piece label, not by a
            # rounded interval comparison at a shared endpoint.
            x_piece = index if orientation == 1 else 2-index
            if x_piece == 0:
                u = (x/delta).intersect(0, 1)
                H, g = delta*I5(u)/c, S5(u)
            elif x_piece == 1:
                H, g = (x-delta/2)/c, Interval(1, 1, bits)
            else:
                u = ((a-x)/delta).intersect(0, 1)
                H, g = 1-delta*I5(u)/c, S5(u)
            H, g = H.intersect(0, 1), g.intersect(0, 1)
            values.append(sign*H)
            derivatives.append(sign*orientation*g/c)
            pieces.append(dict(quarter=quarter, piece=index, normalized_interval=[lo, hi]))
    if not pieces:
        raise ValueError('The full declared central coordinate has no profile piece')
    h = Interval(min(v.lo for v in values), max(v.hi for v in values), bits).intersect(-1, 1)
    ht = Interval(min(v.lo for v in derivatives), max(v.hi for v in derivatives), bits)
    return dict(h=h, normalized_derivative=ht, h_s=ht/physical_length,
        exact_profile_delta=str(delta), complete_intersecting_pieces=pieces,
        accurate_normalized_coordinate=t, accurate_physical_length=physical_length,
        profile_and_derivative_enclosures_computed_here=True,
        external_node_address_to_coordinate_association_verified=False)


def exact_relative_lengths(seed, S, bits):
    support = seed["exact_relative_support_intervals"]
    if len(support) != 2:
        raise ValueError("This complete seed has its two declared supports")
    pieces = [[Fraction(x) for x in pair] for pair in support]
    if any(len(pair) != 2 or not 0 < pair[0] < pair[1] < 1 for pair in pieces):
        raise ValueError("Malformed accurate support")
    if not pieces[0][1] < pieces[1][0]:
        raise ValueError("Keep the original separated supports")
    beta = Fraction(seed["exact_relative_boundary_total_length"])
    profile_delta = Fraction(seed["exact_profile_delta"])
    total = sum(pair[1]-pair[0] for pair in pieces)
    if beta <= 0 or any(pair[1]-pair[0] <= beta/2 for pair in pieces):
        raise ValueError("All declared central intervals must be positive")
    if S.lo <= 0:
        raise ValueError("Supply a positive accurate physical S enclosure")
    central = (S*(total-beta))
    return dict(central_lower=central.lo, central_upper=central.hi,
        boundary_upper=(S*beta).hi, profile_delta=profile_delta,
        relative_central_intervals=[[left+beta/4, right-beta/4] for left, right in pieces],
        relative_boundary=beta, relative_support_length=total)


def mean_jet_bounds(seed, working, fees, *, bits=160, taylor_order=48, profile_series_order=48):
    """Evaluate the full conditional theorem at one actual completed batch angle."""
    require_actions()
    U = lambda q: upper_dyadic(q, bits)
    S = box(fees["accurate_S_enclosure"], bits)
    length = exact_relative_lengths(seed, S, bits)
    lc, lcu, b = length["central_lower"], length["central_upper"], length["boundary_upper"]
    km = fraction(fees["K_norm_lower"])
    kp = fraction(fees["K_norm_upper"])
    kz = fraction(fees["K_vertical_lower"])
    if (fees.get("accurate_reference_unit_and_nonnegative_vertical_on_complete_boundary") is not True
            or not 0 < km <= kp or not b < km or not b < kz or not kp+b < lc):
        raise ValueError("R709 accurate global hypotheses have not been supplied consistently")
    rminus, rplus = (km-b)/lcu, (kp+b)/lc
    zeta = (kz-b)/(kp+b)
    if not 0 < rminus <= rplus < 1 or not 0 < zeta <= 1:
        raise ValueError("Invalid accurate root range")
    profile_delta = length["profile_delta"]
    if not 0 < profile_delta < Fraction(1, 8):
        raise ValueError("The complete independent R711 profile delta is invalid")
    candidate = [point_vector(working[name]) for name in ("v", "v_phi", "v_phiphi")]
    v0, v1, v2 = candidate
    amin, amax = point_norm(v0, bits)
    if amin <= 0 or v0[2] <= 0:
        raise ValueError("The actual candidate direction must have a paid positive vertical component")
    zhat = v0[2]/amax
    zstar = min(zhat, zeta)
    nu = cap_floor(zstar, bits)
    residual = [nonnegative(q, "accurate centered equation residual")
                for q in fees["accurate_centered_total_equation_residual_norms"]]
    if len(residual) != 3:
        raise ValueError("Keep zero, first and second centered accurate total-equation residuals")
    E0, R1, R2 = residual
    Ed = min(Fraction(2), U(2*E0/(lc*(amin+rminus))))
    LB = U(b/zstar)
    Er = U((E0+LB*Ed)/lc)
    Ev = U(E0/lc+(LB/lc+rplus)*Ed)
    U1 = nonnegative(fees["boundary_reference_phi_norm_upper"], "T0 phi")
    U2 = nonnegative(fees["boundary_reference_phiphi_norm_upper"], "T0 phiphi")
    M0, C0, C1 = U(b/nu), U(6*b/nu**2), U(36*b/nu**3)
    N0, Nd = U(6*b*U1/nu**2), U(36*b*U1/nu**3)
    Qd = U(6*b*U2/nu**2+36*b*U1**2/nu**3)
    delta1 = U(Er/(rminus*amin)+Ed/amin)
    delta2 = U(6*Er*(rplus+amax)/(rminus**2*amin**2)+12*Ed/amin**2)
    eta = U((1+M0/(lc*rminus))/lc)
    DJ = U(C0*Ed/rminus+M0*delta1)
    h1, h2 = point_norm(v1, bits)[1], point_norm(v2, bits)[1]
    Ev1 = U(eta*(R1+DJ*h1+N0*Ed))
    c1, c2 = U(h1/amin), U(6*h1*h1/(amin*amin))
    e1, e2 = U(delta1*h1), U(delta2*h1*h1)
    move0 = U(DJ*h2+Qd*Ed+2*(Nd*Ed*c1+N0*e1)
        +C1*Ed*c1*c1+C0*(2*c1*e1+e1*e1)+C0*Ed*c2+M0*e2)
    move1 = U(2*N0*Ev1/rminus
        +(C0+6*M0)*(2*h1*Ev1+Ev1*Ev1)/(rminus*rminus))
    Ev2 = U(eta*(R2+move0+move1))
    vboxes = [centered_vector(values, error, bits)
        for values, error in zip(candidate, (Ev, Ev1, Ev2))]
    vboxes[0] = [v.intersect(-rplus, rplus) for v in vboxes[0]]
    vboxes[0][2] = vboxes[0][2].intersect(rminus*zeta, rplus)
    dboxes, rboxes = normalized_jets(*vboxes, norm_lower=rminus, norm_upper=rplus)
    candidate_radius = Interval(amin, amax, bits)
    dcenter = [Interval(q, q, bits)/candidate_radius for q in v0]
    dboxes[0] = [v.intersect(max(Fraction(-1), c.lo-Ed), min(Fraction(1), c.hi+Ed))
        for v, c in zip(dboxes[0], dcenter)]
    dboxes[0][2] = dboxes[0][2].intersect(zeta, 1)
    # Recompute radius jets with the stronger zero-direction enclosure.
    rboxes[1] = dot(dboxes[0], vboxes[1])
    rboxes[2] = (dot(dboxes[0], vboxes[2])+dot(vboxes[1], vboxes[1])/rboxes[0]
        -dot(vboxes[0], vboxes[1])**2/(rboxes[0]**3))
    ejets = [vector_box(fees["accurate_fixed_chart_radial_jets"][name], bits)
             for name in ("e", "ep", "epp")]
    if fees.get("fixed_chart_e_is_the_accurate_horizontal_unit_radial_vector") is not True:
        raise ValueError("The projected frame needs the actual fixed horizontal unit radial vector")
    e0, ep, epp = ejets
    d0, dp, dpp = dboxes
    ed = dot(e0, d0)
    edp = dot(ep, d0)+dot(e0, dp)
    edpp = dot(epp, d0)+2*dot(ep, dp)+dot(e0, dpp)
    y0 = vsub(e0, vscale(d0, ed))
    yp = vsub(vsub(ep, vscale(d0, edp)), vscale(dp, ed))
    ypp = vsub(vsub(vsub(epp, vscale(d0, edpp)), vscale(dp, 2*edp)), vscale(dpp, ed))
    wboxes, _ = normalized_jets(y0, yp, ypp, norm_lower=zeta, norm_upper=1)
    lam = [word(working[name]) for name in ("lambda", "lambda_phi", "lambda_phiphi")]
    pi = pi_bounds(bits)
    if not 0 < lam[0] < pi.lo:
        raise ValueError("Actual R711 amplitude candidate is not proved inside (0,pi)")
    sinhat = trig_boxes(Interval(lam[0], lam[0], bits), taylor_order)[0]
    full_branch_floor = min(sinhat.lo, sqrt_bounds(1-rplus*rplus, bits)[0],
        2*rminus*sqrt_bounds(1-rminus*rminus, bits)[0])
    m = lower_dyadic(full_branch_floor/3, bits)
    if m <= 0:
        raise ValueError("Current outward data cannot resolve the positive full-profile derivative")
    moment_names = ("profile_moment", "profile_moment_first_derivative",
                    "profile_moment_second_derivative")
    moment_proof = complete_profile_moment_enclosures(seed, working["lambda"],
        bits=bits, series_order=profile_series_order)
    moments = moment_proof["intervals"]
    moment_fees = [max(abs(v.lo-word(working[name])), abs(v.hi-word(working[name])))
        for v, name in zip(moments, moment_names)]
    moment_proof["actual_working_moment_binary64_hex"] = [working[name] for name in moment_names]
    moment_proof["complete_working_moment_error_upper"] = moment_fees
    moment_proof["external_profile_moment_error_inputs_used"] = False
    El0 = U((moments[0]-rboxes[0]).abs_upper()/m)
    El1 = U(((moments[1]*lam[1]-rboxes[1]).abs_upper()+El0*abs(lam[1]))/m)
    El2 = U(((moments[1]*lam[2]+moments[2]*lam[1]*lam[1]-rboxes[2]).abs_upper()
        +El0*(abs(lam[2])+lam[1]*lam[1])
        +2*abs(lam[1])*El1+El1*El1)/m)
    lboxes = [Interval(value-error, value+error, bits)
        for value, error in zip(lam, (El0, El1, El2))]
    lboxes[0] = lboxes[0].intersect(0, pi.hi)
    intervals = dict(v=vboxes[0], v_phi=vboxes[1], v_phiphi=vboxes[2],
        d=dboxes[0], d_phi=dboxes[1], d_phiphi=dboxes[2],
        w=wboxes[0], w_phi=wboxes[1], w_phiphi=wboxes[2],
        **{"lambda": lboxes[0], "lambda_phi": lboxes[1], "lambda_phiphi": lboxes[2]})
    errors = {name: vector_error(intervals[name], working[name], bits)
              for name in MEAN_VECTOR_KEYS}
    for name in ("lambda", "lambda_phi", "lambda_phiphi"):
        actual = word(working[name])
        errors[name] = max(abs(intervals[name].lo-actual), abs(intervals[name].hi-actual))
    return dict(seed_model_identity_sha256=canonical(seed),
        literal_phi_hex=working["literal_phi_hex"], provider_sha256=PROVIDER_SHA,
        intervals=intervals, norm_error_upper=errors,
        radius_intervals=rboxes, accurate_root_radius_range=[rminus, rplus],
        accurate_root_vertical_lower=zeta,
        bounds=dict(direction_error=Ed, radius_error=Er, vector_error=Ev,
            first_angular_vector_error=Ev1, second_angular_vector_error=Ev2,
            common_segment_vertical_lower=zstar, common_segment_normalization_lower=nu,
            normalization_first_derivative_difference=delta1,
            normalization_second_derivative_difference=delta2,
            complete_root_J_inverse_upper=eta, complete_root_J_difference=DJ,
            second_equation_zero_root_motion=move0,
            second_equation_first_jet_motion=move1,
            M0=M0, C0=C0, C1=C1, N0=N0, Nd=Nd, Qd=Qd,
            amplitude_derivative_lower=m,
            amplitude_errors=[El0, El1, El2]),
        length_bounds=length, accurate_S_interval=S,
        complete_central_profile_moment_proof=moment_proof,
        central_profile_moment_errors_certified_by_this_module=True,
        precision_bits=bits, taylor_order=taylor_order, profile_series_order=profile_series_order,
        input_fees_certified_by_this_module=False,
        continuous_uniform_field_certificate=False)


def bound_reference_node(mean, node):
    """Full T/Tp/Tpp/Ts accurate interval formulas against supplied actual words.

    Caller owns the same-field exact s/phi address and the accurate scalar,
    cutoff/profile and original-reference input intervals. No fee defaults.
    """
    require_actions()
    bits, order = mean["precision_bits"], mean["taylor_order"]
    binding = node["same_field_node_binding"]
    if (binding.get("supported_unit_seed_identity_sha256") != mean["seed_model_identity_sha256"]
            or binding.get("literal_phi_hex") != mean["literal_phi_hex"]
            or binding.get("provider_sha256") != PROVIDER_SHA
            or node["address"].get("literal_phi_hex") != mean["literal_phi_hex"]):
        raise ValueError("The requested node, full mean jet and frozen seed must have one actual identity and angle")
    fields = mean["intervals"]
    d, dp, dpp = fields["d"], fields["d_phi"], fields["d_phiphi"]
    w, wp, wpp = fields["w"], fields["w_phi"], fields["w_phiphi"]
    region = node["region"]
    if region == "central":
        index = node["central_interval_index"]
        if isinstance(index, bool) or not isinstance(index, int) or index not in (0, 1):
            raise ValueError("Bind one actual complete central support interval")
        left, right = mean["length_bounds"]["relative_central_intervals"][index]
        t = box(node["accurate_normalized_central_coordinate"], bits)
        profile = central_profile_enclosures(t, mean["length_bounds"]["profile_delta"],
            mean["accurate_S_interval"]*(right-left))
        h, hs = profile["h"], profile["h_s"]
        alpha, ap, app, ass = (h*fields["lambda"], h*fields["lambda_phi"],
            h*fields["lambda_phiphi"], hs*fields["lambda"])
        sine, cosine = trig_boxes(alpha, order)
        tangent = vadd(vscale(d, -sine), vscale(w, cosine))
        value = vadd(vscale(d, cosine), vscale(w, sine))
        first = vadd(vadd(vscale(dp, cosine), vscale(wp, sine)), vscale(tangent, ap))
        second = vadd(vadd(vscale(dpp, cosine), vscale(wpp, sine)),
            vscale(vadd(vscale(dp, -sine), vscale(wp, cosine)), 2*ap))
        second = vsub(vadd(second, vscale(tangent, app)), vscale(value, ap*ap))
        values = dict(T=value, Tp=first, Tpp=second, Ts=vscale(tangent, ass))
    elif region in ("boundary", "outside"):
        original = {name: vector_box(node["accurate_original_reference"][name], bits)
                    for name in FIELD_KEYS}
        if region == "outside":
            values = original
        else:
            chi, chis = box(node["accurate_chi"], bits), box(node["accurate_chi_s"], bits)
            if chi.lo < 0 or chi.hi > 1:
                raise ValueError("The accurate boundary cutoff must be enclosed in [0,1]")
            om = 1-chi
            Y = vadd(vscale(original["T"], om), vscale(d, chi))
            Yp = vadd(vscale(original["Tp"], om), vscale(dp, chi))
            Ypp = vadd(vscale(original["Tpp"], om), vscale(dpp, chi))
            Ys = vadd(vscale(original["Ts"], om), vscale(vsub(d, original["T"]), chis))
            nu = cap_floor(mean["accurate_root_vertical_lower"], bits)
            jets, radii = normalized_jets(Y, Yp, Ypp, norm_lower=nu, norm_upper=1)
            radius = radii[0]
            Ts = vsub(vscale(Ys, 1/radius), vscale(Y, dot(Y, Ys)/(radius**3)))
            values = dict(T=jets[0], Tp=jets[1], Tpp=jets[2], Ts=Ts)
    else:
        raise ValueError("Node region must be the actual outside, boundary, or central piece")
    if set(node["actual_working_fields"]) != set(FIELD_KEYS):
        raise ValueError("Compare all four actual provider jets")
    errors = {name: vector_error(values[name], node["actual_working_fields"][name], bits)
        for name in FIELD_KEYS}
    return dict(address=node["address"], region=region, intervals=values,
        norm_error_upper=errors,
        complete_central_profile_enclosures=profile if region == "central" else None,
        caller_same_field_node_binding=node["same_field_node_binding"],
        external_node_values_and_accurate_input_enclosures_verified_by_this_module=False,
        requested_node_not_uniform_whole_field_certificate=True)


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, Interval):
        return value.json()
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_text(json.dumps(encode(value), sort_keys=True, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def bind_actual_batch(repo, report_path, batch_index, array_override=None):
    """Bind all source/model identities through the existing complete pure reader."""
    require_actions()
    topic = Path(repo)/"topics/visible-flex-larger-amplitude"
    reader_path = topic/"scripts/resume_20261126/read_supported_smooth_triangle_normal_lift_so3_report.py"
    if sha(reader_path) != READER_SHA:
        raise ValueError("The complete actual source reader changed")
    spec = importlib.util.spec_from_file_location("_actual_supported_seed_full_fee_reader", reader_path)
    reader = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = reader
    spec.loader.exec_module(reader)
    report_bytes = Path(report_path).read_bytes()
    report_digest = hashlib.sha256(report_bytes).hexdigest()
    pure = reader.read_report(Path(repo), Path(report_path), verify_final_bundle=False)
    if pure.get("report_sha256") != report_digest or sha(report_path) != report_digest:
        raise ValueError("The complete reader and captured actual report are different byte snapshots")
    raw = json.loads(report_bytes)
    if raw.get("source_sha256") != DRIVER_SHA:
        raise ValueError("Do not relabel another complete scientific driver as this actual field")
    seed = raw["supported_unit_seed_definition"]
    identity = raw["supported_unit_seed_identity_sha256"]
    if (canonical(seed) != identity or seed["source_sha256"] != PROVIDER_SHA
            or seed["mean_kernel_source_sha256"] != KERNEL_SHA):
        raise ValueError("The actual fixed supported seed source/model changed")
    diag = pure.get("seed_diagnostics")
    if diag is None:
        raise ValueError("No actual fixed seed evaluation metadata is present")
    batches = diag["mean_batch_records"]
    captured_batches = raw["latest_operator_metadata"]["base_complete_metadata"]["fixed_supported_unit_seed"]["mean_batch_records"]
    if batches != captured_batches:
        raise ValueError("The actual complete mean records changed across the source-reader snapshot")
    if not 0 <= batch_index < len(batches):
        raise ValueError("The requested actual completed mean batch does not exist")
    batch = batches[batch_index]
    record = batch["runner_raw_arrays"]
    path = Path(record["path"] if array_override is None else array_override)
    if sha(path) != record["sha256"]:
        raise ValueError("The actual mean raw bytes changed; explicit paths cannot change their identity")
    import numpy as np
    with np.load(path, allow_pickle=False) as data:
        if str(data["seed_model_identity"].item()) != identity:
            raise ValueError("The actual raw mean arrays belong to another fixed seed")
        phi = data["phi"].copy()
        angles = [float(x).hex() for x in phi]
        if angles != batch["literal_angle_hex"]:
            raise ValueError("Keep every actual batch angle in its literal original order")
        arrays = {}
        for name in MEAN_VECTOR_KEYS+MEAN_SCALAR_KEYS:
            array = data[name]
            shape = (len(angles), 3) if name in MEAN_VECTOR_KEYS else (len(angles),)
            if (array.shape != shape or array.dtype.kind != "f" or array.dtype.itemsize != 8
                    or not np.isfinite(array).all()):
                raise ValueError("Missing/nonfinite complete mean array: "+name)
            arrays[name] = array.copy()
    if sha(path) != record["sha256"] or sha(report_path) != report_digest:
        raise ValueError("The captured actual report or raw batch changed while its complete arrays were read")
    working = []
    for i, angle in enumerate(angles):
        row = {"literal_phi_hex": angle}
        for name in MEAN_VECTOR_KEYS:
            row[name] = [float(v).hex() for v in arrays[name][i]]
        for name in MEAN_SCALAR_KEYS:
            row[name] = float(arrays[name][i]).hex()
        working.append(row)
    binding = dict(report_sha256=report_digest, actual_driver_sha256=DRIVER_SHA,
        actual_complete_reader_sha256=READER_SHA, supported_unit_seed_identity_sha256=identity,
        provider_sha256=PROVIDER_SHA, mean_kernel_sha256=KERNEL_SHA,
        fixed_scalar_metric_identity_sha256=seed["fixed_scalar_metric_identity_sha256"],
        fixed_chart_core_sha256=seed["fixed_chart_core_sha256"],
        actual_completed_batch_index=batch_index, actual_raw_batch_sha256=record["sha256"],
        actual_raw_batch_path=str(path), literal_angle_hex=angles,
        complete_actual_batch_metadata=batch)
    return seed, working, binding


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--batch-index", type=int, required=True)
    parser.add_argument("--batch-arrays", type=Path)
    parser.add_argument("--fees", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--precision-bits", type=int, default=160)
    parser.add_argument("--taylor-order", type=int, default=48)
    parser.add_argument("--profile-series-order", type=int, default=48)
    return parser.parse_args()


def main():
    args = parse_args()
    require_actions()
    args.repo, args.output = args.repo.resolve(), args.output.resolve()
    if args.output == args.repo or args.repo in args.output.parents:
        raise ValueError("All scientific raw enclosures must stay outside the repository")
    if args.output.exists():
        raise FileExistsError("Use a fresh actual fee output")
    seed, working, binding = bind_actual_batch(args.repo, args.report,
        args.batch_index, args.batch_arrays)
    fee_bytes = args.fees.read_bytes()
    fee_digest = hashlib.sha256(fee_bytes).hexdigest()
    request = json.loads(fee_bytes)
    if request.get("schema") != REQUEST_SCHEMA:
        raise ValueError("Supply the full accurate-fee request schema")
    for key in ("report_sha256", "supported_unit_seed_identity_sha256",
                "actual_raw_batch_sha256", "fixed_scalar_metric_identity_sha256",
                "fixed_chart_core_sha256"):
        if request["binding"].get(key) != binding[key]:
            raise ValueError("Accurate fees and actual working batch are different objects: "+key)
    rows = request["angles"]
    if [row["literal_phi_hex"] for row in rows] != binding["literal_angle_hex"]:
        raise ValueError("Every actual completed batch angle needs its own full accurate fees")
    if not isinstance(request.get("external_fee_provenance"), dict):
        raise ValueError("Retain the external complete fee producer and its proof scope")
    report = dict(schema=SCHEMA, source_sha256=sha(__file__), complete=False,
        binding=binding, complete_seed_model=seed,
        fee_request_sha256=fee_digest, external_fee_provenance=request["external_fee_provenance"],
        external_fee_enclosures_certified_by_this_module=False,
        exact_or_uniform_geometry_certificate=False, full_outer_normal_certificate=False,
        all_requested_actual_batch_angles_retained=True, actual_completed_angles=0,
        requested_angles=len(rows), precision_bits=args.precision_bits,
        taylor_order=args.taylor_order, profile_series_order=args.profile_series_order,
        exact_profile_moment_fees_computed_from_all_pieces=True,
        external_profile_moment_errors_used=False, results=[])
    write_json(args.output, report)
    for values, inputs in zip(working, rows):
        try:
            bound = mean_jet_bounds(seed, values, inputs["fees"],
                bits=args.precision_bits, taylor_order=args.taylor_order,
                profile_series_order=args.profile_series_order)
            nodes = [bound_reference_node(bound, node) for node in inputs.get("nodes", [])]
            report["results"].append(dict(literal_phi_hex=values["literal_phi_hex"],
                actual_working_words=values, complete=True, mean=bound, requested_nodes=nodes))
            report["actual_completed_angles"] += 1
            write_json(args.output, report)
        except (ValueError, TypeError, KeyError, ZeroDivisionError, OverflowError) as error:
            report["failure"] = dict(literal_phi_hex=values["literal_phi_hex"],
                error=repr(error), complete=False,
                missing_or_inconsistent_fee_is_not_physical_nonexistence=True)
            write_json(args.output, report)
            raise
    report["complete"] = True
    report["scope"] = "Complete conditional arithmetic for the bound actual batch and supplied nodes; external accurate fees remain explicit"
    write_json(args.output, report)


if __name__ == "__main__":
    main()
