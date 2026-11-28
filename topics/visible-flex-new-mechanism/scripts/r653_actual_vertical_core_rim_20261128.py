#!/usr/bin/env python3
"""Same-field R653 vertical rim bounds from the full actual finite core fluxes.

Index i of each real cosine list denotes mode 2*i, including its full mean.
C0=W(Z_r+W) at R, C1=its r derivative there. Inputs are outward bounds for
the actual coefficients including the fixed seed's mean and all source
errors with their original status. Finite observations are not enclosures.
"""
import hashlib
from pathlib import Path

BACKEND = Path(__file__).with_name('r649_complete_offsolution_curvature_20261128.py')
BACKEND_SHA = 'a2f765c580d7209b8549f10547d17c39b71a84b33dcbb0d9008311017e2a23fb'
if hashlib.sha256(BACKEND.read_bytes()).hexdigest() != BACKEND_SHA:
    raise ValueError('the original actual curvature interval source differs')
from r649_complete_offsolution_curvature_20261128 import I, sqrt_i, abs_i, evidence, public_only, tree_intervals

SCHEMA = 'r653-actual-vertical-core-two-traces-and-open-graph-collar-v1'


def laurent(cosines):
    out = {0: cosines[0]}
    for i, value in enumerate(cosines[1:], 1):
        out[-2*i] = out[2*i] = value / 2
    return out


def convolution(a, b):
    result = {}
    for i, x in a.items():
        for j, y in b.items():
            key = i+j
            result[key] = result.get(key, I(0))+x*y
    return result


def certified_turning(energy, squared_range, order):
    """Mean of (e+2*C0)^(-1/2) by true finite Laurent powers and a real tail."""
    if type(order) is not int or order < 0:
        raise ValueError('a nonnegative integer expansion order is required')
    mid = I(squared_range.lo)/2+I(squared_range.hi)/2
    rho = abs_i(squared_range/mid-1)
    if rho.hi >= 1:
        return None
    delta = {k: v/mid for k,v in energy.items()}
    delta[0] -= 1
    power = {0:I(1)}
    coefficient, total = I(1), I(1)
    for k in range(1, order+1):
        power = convolution(power,delta)
        coefficient = -coefficient*(2*k-1)/(2*k)
        total += coefficient*power[0]
    err = (rho**(order+1))/(1-rho)
    return (total+I(-err.hi,err.hi))/sqrt_i(mid)


def intersection(a,b):
    lo,hi = max(a.lo,b.lo),min(a.hi,b.hi)
    if hi < lo:
        raise ArithmeticError('the supplied same-field enclosures are incompatible')
    return I(lo,hi)


def endpoint_from_actual_traces(*, radius, alpha, e, er, C0, C1, input_evidence,
                                paid_squared_speed=None, paid_continuous_A=None,
                                mean_order=6):
    public_only()
    src = evidence(input_evidence)
    if (not isinstance(C0,(list,tuple)) or not C0 or not isinstance(C1,(list,tuple)) or not C1
            or any(not isinstance(x,I) for x in [radius,alpha,e,er,*C0,*C1])
            or radius.lo <= 0 or alpha.lo <= .5 or alpha.hi >= 1):
        raise ValueError('bounds for the two full signed even cosine fluxes and background are required')
    if not src.get('complete_true_core_cosine_fluxes_and_conormal_source_hypotheses'):
        raise ValueError('the original complete true-core data and conormal hypotheses are required')
    if (paid_squared_speed is not None and not isinstance(paid_squared_speed,I)
            or paid_continuous_A is not None and not isinstance(paid_continuous_A,I)):
        raise TypeError('existing continuous bounds must use the same outward interval type')
    base, slope = laurent(C0), laurent(C1)
    energy = {k:2*v for k,v in base.items()}
    energy[0] += e
    beta = alpha/(1+alpha)
    D = {k:-radius*v for k,v in slope.items()}
    D[0] -= radius*er/2
    for k,v in base.items():
        D[k] = D.get(k,I(0))-beta*e*k*k*v
        for j,w in base.items():
            D[k+j] = D.get(k+j,I(0))+(j*k-2*beta*k*k)*v*w
    Dabs = sum((abs_i(v) for v in D.values()), I(0))
    oscillation = sum((2*abs_i(v) for v in C0[1:]),I(0))
    sq = energy[0]+I(-oscillation.hi,oscillation.hi)
    if paid_squared_speed is not None:
        sq = intersection(sq,paid_squared_speed)
    result = {'schema':SCHEMA,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'actual_same_field_evidence':src,'radius':radius,'alpha':alpha,
              'highest_supplied_C0_mode':2*(len(C0)-1),'highest_supplied_C1_mode':2*(len(C1)-1),
              'actual_rim_D_Laurent_coefficients':D,'all_angle_absolute_rim_D_upper':Dabs,
              'actual_squared_rim_speed_range':sq,'global_reach_or_collar_width_claimed':False}
    if sq.lo <= 0:
        result['status']='positive core speed unresolved in the supplied full-angle box'
        return tree_intervals(result)
    speed = sqrt_i(sq)
    A = 1/speed
    if paid_continuous_A is not None:
        A = intersection(A,paid_continuous_A)
        method = 'supplied same-field continuous A'
    else:
        enclosure = certified_turning(energy,sq,mean_order)
        method = 'positive speed range alone'
        if enclosure is not None:
            A = intersection(A,enclosure)
            method = 'zero modes of exact finite powers with a uniform analytic remainder'
    inverse_speed_spread = (1/I(speed.lo)-1/I(speed.hi)).hi
    pa = (I(22)/28)*I(0,max(0.,inverse_speed_spread))
    absR = I(0,Dabs.hi)/(radius*I(speed.lo)**3)
    ut = sum((2*i*abs_i(v) for i,v in enumerate(C0[1:],1)), I(0))/I(speed.lo)
    Q = (I(22)/28)*absR+pa*absR/I(A.lo)
    H = abs_i(A-1)*(1+ut)/I(A.lo)+radius*Q/I(A.lo)
    defect = (I(22)/14)*H
    support = I(speed.lo)-I(0,defect.hi)
    result.update(status='continuous rim inequalities under supplied source status',
        actual_turning_range=A,turning_bound_method=method,
        actual_rim_connection_absolute_upper=absR,
        actual_rim_physical_position_defect_norm_upper=I(0,defect.hi),
        same_field_outward_r_speed_lower=support.lo,
        nonzero_open_positive_projection_collar_proved_under_input_status=support.lo>0,
        actual_vertical_cylinder_absolute_nonzero_principal_curvature=1/(radius*A*speed),
        second_cylinder_principal_curvature=0,
        whole_collar_curvature_supremum_or_numeric_radial_width_produced=False,
        no_new_ODE_germ_root_FFT_position_or_scientific_samples=True)
    return tree_intervals(result)
