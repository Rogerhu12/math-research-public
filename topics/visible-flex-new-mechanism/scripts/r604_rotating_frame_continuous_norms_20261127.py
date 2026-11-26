#!/usr/bin/env python3
"""Outward R604 norm bounds consuming complete same-field radial boxes.

This is a pure interval interface, not a certification of any unprovided
97q state.  A declared public Actions scope must supply interval enclosures
of the same continuous u/v, a/z and reference jets on every radial block,
including all angular values.  The core, caps, source interpretation and
full coverage are obligations of that caller; no sample is upgraded here.
"""
from dataclasses import dataclass
import hashlib
from pathlib import Path

REFERENCE_SOURCE_SHA = 'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f'
reference_path = Path(__file__).with_name('r611_circular_reference_global_geometry_20261127.py')
if hashlib.sha256(reference_path.read_bytes()).hexdigest() != REFERENCE_SOURCE_SHA:
    raise RuntimeError('the certified exact circular-reference source changed')
from r611_circular_reference_global_geometry_20261127 import I, sqrt_i, sin_i, cos_i


def absolute(x):
    return I(max(abs(x.lo), abs(x.hi)))


def norm(*components):
    total = I(0)
    for component in components:
        total = total + component ** 2
    # A sum of real squares is nonnegative. Only a rounded lower endpoint
    # can have crossed zero; intersect with this proved real constraint.
    return sqrt_i(I(max(0., total.lo), total.hi))


def upper_sum(*terms):
    value = I(0)
    for term in terms:
        value = value + term
    return value


@dataclass(frozen=True)
class Jet:
    """Value, first/second radial derivatives, first angular derivative."""
    value: object
    s: object
    ss: object
    theta: object

    @staticmethod
    def constant(value):
        x = value if isinstance(value, I) else I(value)
        return Jet(x, I(0), I(0), I(0))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Jet) else Jet.constant(value)

    def __add__(self, other):
        b = self.coerce(other)
        return Jet(self.value+b.value, self.s+b.s, self.ss+b.ss, self.theta+b.theta)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.s, -self.ss, -self.theta)

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        b = self.coerce(other)
        return Jet(self.value*b.value,
            self.s*b.value+self.value*b.s,
            self.ss*b.value+2*self.s*b.s+self.value*b.ss,
            self.theta*b.value+self.value*b.theta)

    __rmul__ = __mul__

    def inverse(self):
        inverse = 1/self.value
        return self.compose(inverse, -inverse**2, 2*inverse**3)

    def __truediv__(self, other):
        return self*self.coerce(other).inverse()

    def compose(self, value, first, second):
        return Jet(value, first*self.s,
            second*self.s**2+first*self.ss, first*self.theta)

    def sin(self):
        sine, cosine = sin_i(self.value), cos_i(self.value)
        return self.compose(sine, cosine, -sine)


def rotating_difference(u, v):
    """Exact small coefficients of T-e_theta in its rotating orthonormal frame.

The stable A formula avoids subtracting two near-unit interval values.
All radial and angular derivatives differentiate that SAME exact identity.
R504 supplies the normalization derivatives and the primitive norm.
"""
    if not isinstance(u, Jet) or not isinstance(v, Jet):
        raise TypeError('both actual angular fields need complete interval jets')
    c0 = 1/sqrt_i(1+v.value**2)
    c = v.compose(c0, -v.value*c0**3, (2*v.value**2-1)*c0**5)
    half_sine = (u/2).sin()
    A = -2*c*half_sine*half_sine - v*v*c*c/(1+c)
    B = -c*u.sin()
    C = v*c
    return A, B, C


def radial_block_bounds(current, reference, u, v, *, difference=None):
    """Bound delta, alpha and reference-covariant beta on one COMPLETE circle band.

current/reference are dictionaries with a, a_s, a_ss, z, z_s, z_ss I-values.
u/v enclosures must hold for every theta and every s in the SAME interval.
    Optional difference supplies the exact same-field current-reference jets,
    algebraically grouped before enclosure; it is never an unrelated field.
    The original closed-circle symmetry must give mean(T)=0 (and its two
    radial derivatives); a generic nonclosed T is not an eligible input.
    Only exact continuous zero-mean primitives are used.  FFT/ODE/Hermite
approximation errors must already be represented by the chosen input field.
"""
    names = ('a', 'a_s', 'a_ss', 'z', 'z_s', 'z_ss')
    if any(not isinstance(d[k], I) for d in (current, reference) for k in names):
        raise TypeError('complete exact-current and reference interval jets required')
    a, as_, ass, z, zs, zss = [current[k] for k in names]
    a0, a0s, a0ss, z0, z0s, z0ss = [reference[k] for k in names]
    if min(a.lo, a0.lo) <= 0:
        raise ArithmeticError('nonpositive circle radius; Cartesian cap chart required')
    speed0_squared = a0s**2+z0s**2
    if speed0_squared.lo <= 0:
        raise ArithmeticError('reference immersion speed is not yet enclosed away from zero')
    speed0 = sqrt_i(speed0_squared)
    radial_connection = (a0s*a0ss+z0s*z0ss)/speed0_squared
    angular_connection = a0s/a0
    second_angular_connection = a0*a0s/speed0_squared
    if difference is None:
        da, das, dass = a-a0, as_-a0s, ass-a0ss
        dz, dzs, dzss = z-z0, zs-z0s, zss-z0ss
    else:
        if any(not isinstance(difference[k], I) for k in names):
            raise TypeError('same-field exact difference needs all six interval jets')
        da, das, dass, dz, dzs, dzss = [difference[k] for k in names]
    A, B, C = rotating_difference(u, v)
    m0 = norm(A.value, B.value, C.value)
    m1 = norm(A.s, B.s, C.s)
    m2 = norm(A.ss, B.ss, C.ss)
    # pi/2 < 11/7 is an exact rational overestimate of the paid R504 norm.
    # Using this rational avoids an additional unvalidated library pi value.
    primitive_bound = I(11)/7
    p0, p1, p2 = [primitive_bound*m for m in (m0, m1, m2)]

    displacement = norm(da, dz)+absolute(a)*p0
    radial_difference = upper_sum(norm(das, dzs), absolute(as_)*p0, absolute(a)*p1)
    angular_difference = norm(da+a*A.value, a*B.value, a*C.value)
    # Frobenius dominates the operator norm of the two-column differential.
    alpha = norm(radial_difference/speed0, angular_difference/a0)

    h11 = upper_sum(
        norm(dass-radial_connection*das, dzss-radial_connection*dzs),
        absolute(ass-radial_connection*as_)*p0,
        absolute(2*as_-radial_connection*a)*p1,
        absolute(a)*p2)/speed0_squared
    first_coefficient = as_-angular_connection*a
    h12 = norm(
        das-angular_connection*da+first_coefficient*A.value+a*A.s,
        first_coefficient*B.value+a*B.s,
        first_coefficient*C.value+a*C.s)/(a0*speed0)
    h22 = upper_sum(
        norm(a*(A.theta+B.value),
             -da+a*(B.theta-A.value)+second_angular_connection*das,
             a*C.theta+second_angular_connection*dzs),
        absolute(second_angular_connection*as_)*p0,
        absolute(second_angular_connection*a)*p1)/(a0**2)
    beta = norm(h11, h12, h12, h22)
    return {'C0_upper': displacement.hi,
        'C1_difference_upper': alpha.hi,
        'reference_covariant_C2_difference_upper': beta.hi,
        'rotating_T_difference_uppers': [m0.hi, m1.hi, m2.hi],
        'normalized_covariant_blocks_upper': [h11.hi, h12.hi, h22.hi],
        'primitive_bound': [primitive_bound.lo, primitive_bound.hi],
        'complete_radial_angular_input_hypothesis_is_callers_obligation': True,
        'core_cap_and_full_domain_coverage_not_proved_by_this_call': True,
        'sampled_values_are_not_accepted_as_continuous_inputs': True}


def curvature_from_uniform_bounds(alpha_upper, beta_upper, reference_rho):
    """R604(20), only after the caller has supplied complete uniform bounds."""
    alpha, beta = I(alpha_upper), I(beta_upper)
    if not (0 <= alpha.lo < 1 and beta.lo >= 0 and reference_rho.lo > 0):
        raise ArithmeticError('uniform immersion/curvature hypotheses unresolved')
    curvature = (1/reference_rho+beta)/(1-alpha)**2
    return {'derivative_upper': (1+alpha).hi,
        'normal_projection_difference_upper': alpha.hi,
        'principal_curvature_upper': curvature.hi,
        'continuous_bounds_must_cover_entire_closed_material_surface': True}
