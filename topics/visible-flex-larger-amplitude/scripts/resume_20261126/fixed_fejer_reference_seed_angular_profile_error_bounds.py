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

SCHEMA = 'complete-fixed-fejer-reference-actual-seed-angular-profile-node-fees-v1'
REQUEST_SCHEMA = 'actual-fixed-fejer-reference-seed-accurate-fee-request-v1'
PROVIDER_SHA = "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a"
KERNEL_SHA = "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
READER_SHA = "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b"
DRIVER_SHA = "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
ADAPTER_SOURCE_CONTRACT = {"stem": "fixed_fejer_reference",
 "report_schema": "complete-fixed-fejer-immutable-point-material-envelope-SO3-QP-v1",
 "driver_name": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
 "driver_sha256": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
 "reader_name": "read_fixed_fejer_immutable_point_so3_report.py",
 "reader_sha256": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
 "field_schema": "complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1",
 "field_name": "fixed_fejer_normal_lift_operator.py",
 "field_sha256": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
 "calibration_name": "fixed_fejer_reference_calibration.py",
 "calibration_sha256": "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c",
 "C1_role": "frame_C1",
 "C1_sha256": "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca"}
MATERIAL_ENVELOPE_SOURCE_CONTRACT = {"memory_role": "independent_envelope_memory",
 "memory_name": "complete_fixed_fejer_material_envelope_memory.py",
 "memory_sha256": "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a",
 "rows_name": "complete_material_envelope_rows.py",
 "rows_sha256": "729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7",
 "geometry_name": "so3_fixed_fejer_complete_geometry.py",
 "geometry_sha256": "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26",
 "memory_schema": "complete-fixed-fejer-new-target-material-envelope-memory-v1",
 "policy_schema": "literal-reinterpreted-history-fixed-fejer-complete-grid-policy-v1",
 "complete_reader_validates_every_recorded_scan_and_row_scope": True,
 "protected_history_roles_or_order_reconstructed": False,
 "fixed_seed_fees_pay_material_envelope_geometry": False,
 "historical_literals_reinterpreted_not_same_physical_points": True}
FIXED_REFERENCE_SOURCE_CONTRACT = {"target_schema": "complete-fixed-fejer-reference-definition-v1",
 "preparation_schema": "R690-fixed-fejer-axisymmetric-SO3-preparation-v1",
 "reference_schema": "R690-fixed-fejer-axisymmetric-SO3-reference-input-v1",
 "entry_binding_source_sha256": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
 "pure_input_binding_source_sha256": "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f",
 "input_maker_source_sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
 "reference_source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
 "scalar_parameters_identity_sha256": "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa",
 "working_scalar_integral_leaf_target": 2218,
 "mathematical_target_source_schema": "fixed-rn64-fejer-R690-mathematical-target-v1",
 "actual_reference_model_or_file_identity_prefilled": False,
 "old_carrier_is_not_current_reference_value_input": True}
DERIVED_FROM_COMPLETE_R713_SOURCE_SHA256 = '82e6f1a714c241b1e445304017613cc0fab8874520ef7d6904acf3ae62904f76'
DERIVED_FROM_COMPLETE_CACHED_CONSUMER_SHA256 = 'a7f1862362d729f29fba2b41ad040a5961b8cedb5eb729d8d6bbdc5bc36120c9'
DERIVED_FROM_COMPLETE_MATERIAL_ENVELOPE_CONSUMER_SHA256 = '2859943d522cd764b686112acd0acdb065dc6a893625f4a8e237641caf041d36'
DERIVED_FROM_COMPLETE_RUN09_CONSUMER_SHA256 = '7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1'
DERIVED_FROM_COMPLETE_RUN10_CONSUMER_SHA256 = '91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1'
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
    if (seed.get('schema') != 'complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1'
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





def recheck_fixed_fejer_reference_attribution(value):
    """Recheck every actually captured source/input byte without new values."""
    for record in value["complete_snapshot_input_records"]:
        path = Path(record["path"]).resolve()
        if path.stat().st_size != record["bytes"] or sha(path) != record["sha256"]:
            raise ValueError("A complete fixed-Fejer source or actual reference input changed: "+str(path))


def bind_fixed_fejer_reference_attribution(raw, pure):
    """Bind the declared recipe and the actually returned reference; no future identities."""
    expected = FIXED_REFERENCE_SOURCE_CONTRACT
    roles = raw.get("source_sha256_by_role", {})
    target = raw.get("independent_fixed_target_definition")
    identity = raw.get("independent_fixed_target_definition_identity_sha256")
    checked = pure.get("independent_fixed_target_binding")
    actual = pure.get("actual_fixed_reference_input_binding")
    base = raw["representation"]["base_complete_model"]
    reference = base["complete_axisymmetric_reference_model"]
    seed = raw["supported_unit_seed_definition"]
    path_binding = raw["material_envelope"]["historical_address_binding"]["actual_path_binding"]
    if (roles.get("analytic_J3_binding") != expected["entry_binding_source_sha256"]
            or roles.get("actual_public_input_binding") != expected["pure_input_binding_source_sha256"]
            or roles.get("independent_input_projection_producer") != expected["reference_source_sha256"]
            or roles.get("reference") != expected["reference_source_sha256"]
            or roles.get("fixed_input_producer") != expected["input_maker_source_sha256"]
            or not isinstance(target, dict) or not isinstance(checked, dict)
            or not isinstance(actual, dict)
            or target.get("schema") != expected["target_schema"]
            or canonical(target) != identity
            or target != path_binding.get("fixed_target_definition")
            or path_binding.get("fixed_target_definition_identity_sha256") != identity
            or checked.get("definition_identity_sha256") != identity
            or checked.get("actual_fixed_recipe_input_binding") != actual
            or raw.get("actual_fixed_reference_input_binding") != actual
            or checked.get("complete_target_and_actual_report_reference_equal") is not True
            or checked.get("actual_full_chart_words_verified") is not True
            or checked.get("predeclared_new_target") is not True
            or checked.get("same_original_fixed_chart") is not False
            or checked.get("same_mathematical_g_claimed") is not False
            or checked.get("old_values_or_certificates_inherited") is not False
            or target.get("declared_new_target") is not True
            or target.get("same_previous_mathematical_g_claimed") is not False
            or target.get("previous_target_fields_roots_or_certificates_inherited") is not False):
        raise ValueError("Retain the actual complete declared Fejer target and its own input family")
    mathematical = target.get("mathematical_target_recipe")
    math_identity = target.get("mathematical_target_identity_sha256")
    if (not isinstance(mathematical, dict)
            or mathematical.get("schema") != expected["mathematical_target_source_schema"]
            or canonical(mathematical) != math_identity
            or mathematical.get("complete_scalar_parameters_identity_sha256") != expected["scalar_parameters_identity_sha256"]
            or reference.get("mathematical_target_recipe") != mathematical
            or reference.get("mathematical_target_identity_sha256") != math_identity
            or checked.get("mathematical_target_identity_sha256") != math_identity
            or actual.get("mathematical_target_identity_sha256") != math_identity
            or pure.get("predeclared_mathematical_target_identity_sha256") != math_identity
            or pure.get("historical_literal_requests_reinterpreted_not_same_physical_points") is not True
            or pure.get("previous_target_completion_or_unknown_typed_history_reconstructed") is not False):
        raise ValueError("The entire exact-dyadic chart/scalar recipe and history scope must agree")
    if (reference.get("schema") != expected["reference_schema"]
            or reference.get("source_sha256") != expected["reference_source_sha256"]
            or target.get("complete_current_reference_model") != reference
            or seed.get("complete_axisymmetric_reference_model") != reference
            or target.get("current_reference_model_identity_sha256") != canonical(reference)
            or checked.get("actual_reference_model_identity_sha256") != canonical(reference)
            or target.get("complete_current_reference_bundle_sha256") != raw["bundle_sha256"]
            or base.get("initial_reference_bundle_sha256") != raw["bundle_sha256"]
            or seed.get("initial_reference_bundle_sha256") != raw["bundle_sha256"]
            or checked.get("actual_reference_bundle_sha256") != raw["bundle_sha256"]
            or target.get("fixed_chart_core_array_record", {}).get("sha256") != reference["fixed_chart_core_sha256"]
            or base.get("fixed_chart_core_sha256") != reference["fixed_chart_core_sha256"]
            or seed.get("fixed_chart_core_sha256") != reference["fixed_chart_core_sha256"]
            or checked.get("actual_fixed_chart_core_sha256") != reference["fixed_chart_core_sha256"]
            or reference.get("warm_or_BVP_core_consumed") is not False
            or reference.get("same_previous_target_claimed") is not False
            or reference.get("predeclared_fixed_chart_from_rational_recipe") is not True):
        raise ValueError("Keep the complete generated reference, rounded chart and fixed seed")
    files = actual.get("complete_current_input_files")
    file_roles = {"current_fixed_input_bundle", "current_node_report", "current_scalar_input",
        "current_carrier", "current_preparation_report", "current_reference_bundle"}
    validation = actual.get("complete_input_validation")
    input_record = actual.get("actual_binding_file")
    if (actual.get("source_sha256") != expected["entry_binding_source_sha256"]
            or actual.get("actual_input_producer_source_sha256") != expected["reference_source_sha256"]
            or actual.get("actual_pure_input_binding_source_sha256") != expected["pure_input_binding_source_sha256"]
            or actual.get("actual_fixed_input_maker_source_sha256") != expected["input_maker_source_sha256"]
            or actual.get("actual_reference_model_identity_sha256") != canonical(reference)
            or actual.get("actual_fixed_target_definition_identity_sha256") != identity
            or actual.get("all_six_current_whole_files_reread") is not True
            or actual.get("predeclared_new_target") is not True
            or actual.get("same_original_fixed_chart") is not False
            or actual.get("same_mathematical_g_claimed") is not False
            or actual.get("physical_values_roots_or_certificates_inherited") is not False
            or not isinstance(validation, dict)
            or validation != raw.get("independent_fixed_target_validation")
            or validation.get("source_sha256") != expected["pure_input_binding_source_sha256"]
            or validation.get("complete_current_six_files_verified") is not True
            or validation.get("complete_generated_fixed_chart_verified") is not True
            or validation.get("historical_literal_addresses_are_reinterpreted_not_same_physical_points") is not True
            or validation.get("unknown_previous_target_history_reconstructed") is not False
            or validation.get("fixed_target_definition_identity_sha256") != identity
            or validation.get("mathematical_target_identity_sha256") != math_identity
            or validation.get("actual_current_model_identity_sha256") != canonical(reference)
            or validation.get("current_input_records") != files
            or validation.get("actual_binding_file") != input_record
            or input_record != path_binding.get("binding_file")
            or not isinstance(files, dict) or set(files) != file_roles):
        raise ValueError("All six actual files and the complete source-bound input validation are required")
    required_files = dict(current_fixed_input_bundle=reference["fixed_input_bundle_sha256"],
        current_reference_bundle=raw["bundle_sha256"],
        current_carrier=raw["observation_carrier_sha256"],
        current_node_report=raw["exact_tail_node_report_sha256"],
        current_scalar_input=raw["exact_tail_scalar_input_sha256"],
        current_preparation_report=raw["independent_preparation_report"]["sha256"])
    if any(files[key]["sha256"] != digest for key, digest in required_files.items()):
        raise ValueError("Current scientific inputs cannot be replaced by older target/carrier values")
    records = [input_record]+[files[key] for key in sorted(file_roles)]
    snapshot = dict(complete_snapshot_input_records=records)
    recheck_fixed_fejer_reference_attribution(snapshot)

    def captured_record(record, name):
        path = Path(record["path"]).resolve()
        data = path.read_bytes()
        if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise ValueError("Captured complete bytes changed: "+name)
        return json.loads(data)

    payload = captured_record(input_record, "fixed input binding")
    preparation = captured_record(files["current_preparation_report"], "complete reference preparation")
    if (payload.get("fixed_target_definition") != target
            or payload.get("fixed_target_definition_identity_sha256") != identity
            or payload.get("mathematical_target_identity_sha256") != math_identity
            or payload.get("current_files") != files
            or payload.get("all_current_six_files_are_actual") is not True
            or preparation.get("schema") != expected["preparation_schema"]
            or preparation.get("source_sha256") != expected["reference_source_sha256"]
            or preparation.get("complete") is not True
            or preparation.get("reference_definition") != reference
            or preparation.get("reference_model_identity_sha256") != canonical(reference)
            or preparation.get("fixed_target_definition") != target
            or preparation.get("fixed_target_definition_identity_sha256") != identity
            or preparation.get("mathematical_target_identity_sha256") != math_identity
            or preparation.get("fixed_input_definition") != target["working_input_definition"]
            or preparation.get("fixed_input_definition_identity_sha256") != target["working_input_definition_identity_sha256"]
            or preparation.get("fixed_input_bundle") != files["current_fixed_input_bundle"]
            or preparation.get("no_warm_BVP_or_optimized_old_chart_required") is not True
            or preparation.get("complete_scalar_tail_included") is not True):
        raise ValueError("The captured preparation, whole recipe and six files differ")
    execution = preparation.get("execution", {})
    if (execution != payload.get("producer", {}).get("execution")
            or str(execution.get("run_id")) != actual.get("actual_run_id")
            or str(execution.get("run_attempt")) != actual.get("actual_run_attempt")
            or execution.get("repository") != "Rogerhu12/math-research-public"):
        raise ValueError("Retain actual reference execution separately from the field's own report")
    scalar = preparation.get("true_scalar", {})
    leaves = scalar.get("integral_leaves")
    if (scalar.get("all_tail_domain_included") is not True
            or scalar.get("unresolved_oscillations_dropped") is not False
            or scalar.get("definition") != reference["fixed_scalar_profile_definition"]
            or scalar.get("model_identity_sha256") != reference["fixed_scalar_metric_identity_sha256"]
            or leaves != expected["working_scalar_integral_leaf_target"]
            or type(leaves) is not int
            or type(scalar.get("requested_integral_accuracy_reached")) is not bool
            or preparation.get("deterministic_scalar_work") != dict(
                leaf_target=leaves, actual_leaves=leaves, wall_clock_decides_leaf_count=False,
                all_original_integer_leaf_operations_retained=True)):
        raise ValueError("Read the complete fixed-work scalar table and its real accuracy status")
    maker_record = payload["fixed_input_preparation_report"]
    if preparation.get("fixed_input_preparation_report") != maker_record:
        raise ValueError("The actual fixed input construction report changed")
    maker = captured_record(maker_record, "complete deterministic input construction")
    maker_outputs = {key:files[role] for key,role in (
        ("fixed_input","current_fixed_input_bundle"),("node_report","current_node_report"),
        ("scalar_input","current_scalar_input"))}
    if (maker.get("source_sha256") != expected["input_maker_source_sha256"]
            or maker.get("complete") is not True or maker.get("status") != "complete"
            or maker.get("all_input_and_source_output_records_rechecked") is not True
            or maker.get("outputs") != maker_outputs
            or maker.get("mathematical_target_recipe") != mathematical
            or maker.get("mathematical_target_identity_sha256") != math_identity
            or maker.get("definition") != target["working_input_definition"]
            or maker.get("definition_identity_sha256") != target["working_input_definition_identity_sha256"]
            or maker.get("complete_scalar_parameters_identity_sha256") != expected["scalar_parameters_identity_sha256"]):
        raise ValueError("No solved warm/core or another mathematical input can replace the fixed recipe")
    records.append(maker_record)
    records.extend(maker["source_records"].values())
    records.extend(maker["input_records"].values())
    records.extend(payload[name] for name in (
        "fixed_target_definition_file", "new_locations", "complete_supplied_location_provenance"))
    for role,path in preparation["source_paths"].items():
        expected_sha = preparation["source_sha256_by_role"][role]
        if roles.get(role) != expected_sha:
            raise ValueError("The actual reference source closure differs from the full field: "+role)
        actual_path = Path(path).resolve()
        records.append(dict(path=str(actual_path),bytes=actual_path.stat().st_size,sha256=expected_sha))
    result = dict(
        actual_run_id=actual["actual_run_id"], actual_run_attempt=actual["actual_run_attempt"],
        actual_field_run_id=raw.get("github_run_id"),
        fixed_target_definition_identity_sha256=identity,
        mathematical_target_identity_sha256=math_identity,
        complete_mathematical_target_recipe=mathematical,
        actual_reference_model_identity_sha256=canonical(reference),
        actual_reference_bundle_sha256=raw["bundle_sha256"],
        actual_current_carrier_sha256=raw["observation_carrier_sha256"],
        actual_fixed_chart_core_sha256=reference["fixed_chart_core_sha256"],
        actual_current_preparation_report=files["current_preparation_report"],
        actual_returned_input_binding=input_record,
        actual_fixed_input_maker_report=maker_record,
        actual_fixed_reference_input_binding=actual,
        complete_snapshot_input_records=records,
        current_reference_tail_integral_leaves=leaves,
        current_reference_tail_requested_accuracy_reached=scalar["requested_integral_accuracy_reached"],
        current_reference_tail_integral_width_exact=scalar["integral_enclosure_width_exact"],
        current_radius_complete_enclosure=reference["radius_complete_enclosure"],
        actual_seed_initial_height_hex=seed["initial_height_hex"],
        historical_carrier_restoration_leaves_declared_by_bound_producer=None,
        historical_carrier_used_as_current_reference_value_input=False,
        current_reference_values_or_paid_fees_inherited_from_old_batch=False,
        same_original_fixed_chart=False, same_mathematical_g_claimed=False,
        exact_current_mathematical_recipe_and_generated_binary_chart_verified=True,
        ideal_unrounded_Fejer_coefficients_used_as_actual_chart=False,
        old_literals_reinterpreted_not_same_physical_points=True,
        unknown_previous_target_history_reconstructed=False,
        actual_outer_analytic_frame_J3_and_cache_are_source_attribution_only=True,
        original_complete_R709_R713_formulas_retained=True,
        continuous_angle_or_current_normal_or_field_fees_paid=False)
    recheck_fixed_fejer_reference_attribution(result)
    return result


def bind_material_envelope_attribution(raw, pure):
    """Preserve the actual finite policy; its scan status is not a fee."""
    expected = MATERIAL_ENVELOPE_SOURCE_CONTRACT
    roles = raw.get("source_sha256_by_role", {})
    actual = raw.get("material_envelope")
    definition = raw.get("material_envelope_definition")
    checked = pure.get("material_envelope_binding")
    if (roles.get(expected["memory_role"]) != expected["memory_sha256"]
            or roles.get("envelope_rows") != expected["rows_sha256"]
            or roles.get("geometry") != expected["geometry_sha256"]
            or not isinstance(actual, dict)
            or actual.get("schema") != expected["memory_schema"]
            or not isinstance(definition, dict)
            or definition.get("schema") != expected["policy_schema"]
            or actual.get("definition") != definition
            or raw.get("material_envelope_source", {}).get("sha256") != expected["memory_sha256"]
            or raw.get("material_envelope_rows_source", {}).get("sha256") != expected["rows_sha256"]
            or raw.get("material_envelope_new_working_set_policy") is not True
            or raw.get("unknown_historical_protected_labels_reconstructed") is not False
            or raw.get("old_protected_required_priority_equivalence_claimed") is not False
            or raw.get("full_material_envelope_nonlinear_responsibility") is not True):
        raise ValueError("Bind the exact complete material-envelope source and declared policy")
    if (not isinstance(checked, dict)
            or checked.get("definition") != definition
            or checked.get("definition_identity_sha256") != canonical(definition)
            or checked.get("source_sha256") != expected["memory_sha256"]
            or checked.get("rows_source_sha256") != expected["rows_sha256"]
            or checked.get("old_unknown_protected_tags_reconstructed") is not False
            or checked.get("old_required_row_priority_equivalence_claimed") is not False
            or checked.get("nonlinear_responsibility_is_complete_permanent_envelope") is not True
            or checked.get("continuous_geometry_or_metric_certificate") is not False
            or not isinstance(checked.get("actual_metadata"), dict)
            or pure.get("material_envelope_diagnostics") != checked["actual_metadata"]):
        raise ValueError("Retain the complete pure-reader envelope attribution including pending/partial status")
    return dict(
        complete_policy_definition=definition,
        policy_identity_sha256=canonical(definition),
        memory_source_sha256=expected["memory_sha256"],
        rows_source_sha256=expected["rows_sha256"],
        geometry_source_sha256=expected["geometry_sha256"],
        actual_observation_carrier_sha256=raw["observation_carrier_sha256"],
        actual_material_envelope_snapshot_sha256=canonical(actual),
        complete_pure_envelope_attribution_sha256=canonical(checked),
        complete_pure_envelope_metadata=checked["actual_metadata"],
        old_unknown_protected_roles_or_order_reconstructed=False,
        finite_nonlinear_screen_is_not_accurate_seed_error=True,
        seed_error_computation_is_not_an_envelope_or_geometry_certificate=True)


def bind_outer_report_scope(raw, pure):
    """Exact NEW source/model attribution; fixed seed fees are not outer-field fees."""
    model = raw.get("representation")
    roles = raw.get("source_sha256_by_role",{})
    expected = ADAPTER_SOURCE_CONTRACT
    if (raw.get("schema") != expected["report_schema"]
            or raw.get("source_sha256") != expected["driver_sha256"]
            or pure.get("actual_driver_sha256") != expected["driver_sha256"]
            or pure.get("actual_endpoint_source_sha256") != expected["field_sha256"]
            or not isinstance(model,dict)
            or model.get("schema") != expected["field_schema"]
            or model.get("source_sha256") != expected["field_sha256"]
            or canonical(model) != raw.get("model_identity_sha256")
            or raw.get("model_identity_sha256") != pure.get("model_identity_sha256")
            or roles.get("endpoint") != expected["field_sha256"]
            or roles.get("reference_calibration") != expected["calibration_sha256"]
            or roles.get("seed_reference") != PROVIDER_SHA
            or roles.get("seed_mean") != KERNEL_SHA
            or roles.get("meridian") != "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3"):
        raise ValueError("This independent fee consumer requires its exact complete NEW outer source/model")
    center = model.get("reference_centering_definition")
    attribution = pure.get("reference_centering")
    if (not isinstance(center,dict) or not isinstance(attribution,dict)
            or center.get("source_sha256") != expected["calibration_sha256"]
            or center.get("endpoint_source_sha256") != expected["field_sha256"]
            or raw.get("reference_centering_definition") != center
            or attribution.get("definition") != center
            or attribution.get("definition_identity_sha256") != canonical(center)
            or center.get("original_reference_point_sha256") != raw.get("actual_reference_initial_full_point_sha256")
            or center.get("original_reference_point_sha256") != raw.get("frozen_original_reference_point_sha256")
            or center.get("base_model_identity_sha256") != model.get("base_model_identity_sha256")
            or center.get("fixed_supported_reference_identity_sha256") != raw.get("supported_unit_seed_identity_sha256")
            or raw.get("radial_metric_error_identically_zero") is not False
            or raw.get("radial_Gram_uses_complete_hprime_Delta") is not True
            or pure.get("working_radial_metric_error_identically_zero") is not False):
        raise ValueError("Retain the exact frozen baseline and complete WORKING physical calibration scope")
    C1_identity = None
    if expected["C1_role"] is None:
        if "normal_frame_C1_reuse" in model:
            raise ValueError("A cached field cannot be relabelled as the independent plain-centred model")
    else:
        C1 = model.get("normal_frame_C1_reuse")
        if (roles.get(expected["C1_role"]) != expected["C1_sha256"]
                or not isinstance(C1,dict) or C1.get("source_sha256") != expected["C1_sha256"]
                or C1.get("complete_first_outer_parameter_derivative_retained") is not True
                or C1.get("original_normal_stages_and_implicit_matrices_retained") is not True
                or C1.get("root_or_stage_or_control_variable_deleted") is not False):
            raise ValueError("Bind the complete actual cached-C1 source and its full-stage derivative contract")
        complete_C1_binding = pure.get("normal_frame_C1_binding")
        if (not isinstance(complete_C1_binding,dict)
                or complete_C1_binding.get("definition") != C1
                or complete_C1_binding.get("definition_identity_sha256") != canonical(C1)
                or complete_C1_binding.get("source_sha256") != expected["C1_sha256"]
                or complete_C1_binding.get("all_original_outer_variables_and_all_normal_stages_retained") is not True
                or complete_C1_binding.get("actual_speedup_or_rounding_certificate") is not False):
            raise ValueError("Keep the complete cached pure-reader attribution, without promoting C1 timing to a certificate")
        C1_identity = canonical(C1)
    return dict(outer_report_schema=expected["report_schema"],
        outer_model_identity_sha256=raw["model_identity_sha256"],
        outer_operator_source_sha256=expected["field_sha256"],
        outer_calibration_source_sha256=expected["calibration_sha256"],
        outer_reference_centering_definition_identity_sha256=canonical(center),
        outer_frozen_original_reference_point_sha256=center["original_reference_point_sha256"],
        outer_C1_definition_identity_sha256=C1_identity,
        material_envelope_attribution=bind_material_envelope_attribution(raw,pure),
        actual_fixed_fejer_reference_attribution=bind_fixed_fejer_reference_attribution(raw,pure),
        fixed_seed_is_not_reselected_from_current_outer_point=True,
        outer_report_identity_is_attribution_not_an_outer_error_certificate=True,
        raw_calibration_or_centered_normal_or_full_physical_lift_error_computed=False)


def bind_actual_batch(repo, report_path, batch_index, array_override=None):
    """Bind all source/model identities through the existing complete pure reader."""
    require_actions()
    topic = Path(repo)/"topics/visible-flex-larger-amplitude"
    reader_path = topic/"scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py"
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
    outer = bind_outer_report_scope(raw,pure)
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
        complete_actual_batch_metadata=batch,complete_outer_attribution=outer)
    recheck_fixed_fejer_reference_attribution(outer["actual_fixed_fejer_reference_attribution"])
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
    if request["binding"].get("complete_outer_attribution") != binding["complete_outer_attribution"]:
        raise ValueError("Do not move fee inputs between distinct complete centred/cached representations")
    if request["binding"].get("actual_completed_batch_index") != binding["actual_completed_batch_index"]:
        raise ValueError("Keep the exact actual completed batch index in its own report")
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
        external_profile_moment_errors_used=False,
        complete_outer_source_attribution=binding["complete_outer_attribution"],
        fixed_seed_reference_fees_only=True,
        numerical_raw_reference_calibration_paid=False,
        complete_outer_normal_root_and_implicit_error_paid=False,
        complete_R715_physical_lift_and_sixjet_error_paid=False,
        outer_history_or_field_certificates_transferred=False, results=[])
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
    recheck_fixed_fejer_reference_attribution(
        binding["complete_outer_attribution"]["actual_fixed_fejer_reference_attribution"])
    if (sha(args.report) != binding["report_sha256"]
            or sha(binding["actual_raw_batch_path"]) != binding["actual_raw_batch_sha256"]
            or sha(args.fees) != fee_digest):
        raise ValueError("The complete captured report, raw batch or accurate-fee request changed")
    report["all_actual_input_and_fee_request_records_rechecked"] = True
    report["complete"] = True
    report["scope"] = "Complete conditional arithmetic for the bound actual batch and supplied nodes; external accurate fees remain explicit"
    write_json(args.output, report)


if __name__ == "__main__":
    main()
