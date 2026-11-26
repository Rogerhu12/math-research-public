#!/usr/bin/env python3
"""R621 one-pass complete norm and normal-projected curvature interface.

All original R604 C0/C1/covariant-C2 algebra is preserved. The SAME complete
radial/angular jets additionally bound the reference-normal component of
each covariant block, then account for the actual normal tilt. A declared
public Actions scope must supply actual q, material identity and complete
closed-surface coverage. This source neither creates nor runs such a scope.
"""
import hashlib
from pathlib import Path

FRAME_SHA = '2fa3a89f2bc2bc0e739ae69f391b06f3b44cb3033d236df632205a3c357516e0'
if hashlib.sha256(Path(__file__).with_name(
        'r604_rotating_frame_continuous_norms_20261127.py').read_bytes()).hexdigest() != FRAME_SHA:
    raise RuntimeError('the original complete covariant frame algebra changed')
from r604_rotating_frame_continuous_norms_20261127 import (
    I, Jet, sqrt_i, absolute, norm, upper_sum, rotating_difference,
)


def radial_block_with_normal_curvature(current, reference, u, v, *, difference=None):
    """Bound the same complete norms and R621 normal-projected actual curvature.

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
    # R621: use the same boxes and already assembled three full blocks.
    # Horizontal and vertical primitives are separated BEFORE projecting
    # onto the reference normal. No second field or point traversal occurs.
    alpha_bound = I(alpha.hi)
    if not 0 <= alpha_bound.lo <= alpha_bound.hi < 1:
        raise ArithmeticError('same-cell C1 enclosure does not yet prove immersion')
    normal_r = -z0s/speed0
    normal_z = a0s/speed0
    # Both exact components belong to [-1,1]; intersect with that identity.
    normal_r = I(max(-1., normal_r.lo), min(1., normal_r.hi))
    normal_z = I(max(-1., normal_z.lo), min(1., normal_z.hi))
    horizontal = [norm(getattr(A,key), getattr(B,key)) for key in ('value','s','ss')]
    vertical = [absolute(getattr(C,key)) for key in ('value','s','ss')]
    normal_primitive = [primitive_bound*(absolute(normal_r)*x+absolute(normal_z)*y)
                        for x,y in zip(horizontal,vertical)]
    n0_h11 = upper_sum(
        absolute(normal_r*(dass-radial_connection*das)
                 +normal_z*(dzss-radial_connection*dzs)),
        absolute(ass-radial_connection*as_)*normal_primitive[0],
        absolute(2*as_-radial_connection*a)*normal_primitive[1],
        absolute(a)*normal_primitive[2])/speed0_squared
    n0_h12 = absolute(
        normal_r*(first_coefficient*B.value+a*B.s)
        +normal_z*(first_coefficient*C.value+a*C.s))/(a0*speed0)
    n0_h22 = upper_sum(
        absolute(normal_r*(-da+a*(B.theta-A.value)+second_angular_connection*das)
                 +normal_z*(a*C.theta+second_angular_connection*dzs)),
        absolute(second_angular_connection*as_)*normal_primitive[0],
        absolute(second_angular_connection*a)*normal_primitive[1])/(a0**2)
    cosine2 = 1-alpha_bound**2
    if cosine2.lo <= 0:
        raise ArithmeticError('normal-alignment square root requires finer C1 enclosure')
    normal_difference = alpha_bound*sqrt_i(2/(1+sqrt_i(cosine2)))
    full_blocks = [I(h11.hi), I(h12.hi), I(h22.hi)]
    reference_normal_blocks = [I(n0_h11.hi), I(n0_h12.hi), I(n0_h22.hi)]
    current_normal_blocks = [normal+normal_difference*full
                             for normal,full in zip(reference_normal_blocks,full_blocks)]
    km = absolute(a0s*z0ss-z0s*a0ss)/(speed0_squared*speed0)
    ko = absolute(z0s)/(a0*speed0)
    diagonal1 = I(km.hi)+current_normal_blocks[0]
    diagonal2 = I(ko.hi)+current_normal_blocks[2]
    off_diagonal = current_normal_blocks[1]
    numerator = (diagonal1+diagonal2+sqrt_i(
        (diagonal1-diagonal2)**2+4*off_diagonal**2))/2
    projected_curvature = numerator/(1-alpha_bound)**2
    return {'C0_upper': displacement.hi,
        'C1_difference_upper': alpha.hi,
        'reference_covariant_C2_difference_upper': beta.hi,
        'rotating_T_difference_uppers': [m0.hi, m1.hi, m2.hi],
        'normalized_covariant_blocks_upper': [h11.hi, h12.hi, h22.hi],
        'primitive_bound': [primitive_bound.lo, primitive_bound.hi],
        'R621_principal_curvature_upper': projected_curvature.hi,
        'R621_reference_normal_blocks_upper': [x.hi for x in reference_normal_blocks],
        'R621_current_normal_blocks_upper': [x.hi for x in current_normal_blocks],
        'R621_oriented_normal_difference_upper': normal_difference.hi,
        'R621_reference_principal_curvatures_upper': [km.hi, ko.hi],
        'R621_normal_primitive_component_bounds_upper': [x.hi for x in normal_primitive],
        'one_rotating_jet_assembly_and_same_material_boxes': True,
        'complete_radial_angular_input_hypothesis_is_callers_obligation': True,
        'core_cap_and_full_domain_coverage_not_proved_by_this_call': True,
        'sampled_values_are_not_accepted_as_continuous_inputs': True}
