#!/usr/bin/env python3
"""R622 scalar consequence of one already-complete continuous geometry input.

No material, ODE, mean, angular or curvature evaluation is performed here.
The public caller must bind all constants to one actual complete certificate;
this function does not manufacture those hypotheses from finite samples.
"""
import hashlib
import math
import os
from pathlib import Path

BACKEND_SHA256 = 'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f'
backend_path = Path(__file__).with_name('r611_circular_reference_global_geometry_20261127.py')
if hashlib.sha256(backend_path.read_bytes()).hexdigest() != BACKEND_SHA256:
    raise RuntimeError('the exact outward scalar backend changed')
from r611_circular_reference_global_geometry_20261127 import I


def long_near_consequence(*, delta, nu, derivative_upper, curvature_upper,
                          reference_reach_lower, reference_diameter_upper):
    """Evaluate only the NEW complete implication, without mixing old terms.

    Every scalar is the exact binary64 value of the corresponding certified
    upper/lower bound. Completeness, common q/reference/material identity and
    all caller-side geometric hypotheses must already have been established.
    Scientific execution belongs to a separately declared public scope.
    """
    if (os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'
            or not os.environ.get('GITHUB_RUN_ID')):
        raise RuntimeError('new scalar scientific evaluation requires public Actions')
    entries = (delta, nu, derivative_upper, curvature_upper,
               reference_reach_lower, reference_diameter_upper)
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in entries):
        raise TypeError('finite actual scalar bounds required')
    if (min(delta, nu) < 0 or
            min(derivative_upper, curvature_upper,
                reference_reach_lower, reference_diameter_upper) <= 0):
        raise ValueError('R604 complete scalar input hypotheses are not satisfied')
    d, n, lam, K, rho, D0 = map(I, entries)
    near_limit = I(5)/(2*K)
    calls = 0

    def path_upper(x):
        nonlocal calls
        calls += 1
        point = I(x)
        square, power, value = point*point, point, I(0)
        for j in range(64):
            value = value+power/(2*j+1)
            power = power*square
        # This expression is an UPPER series bound; only its upper endpoint
        # is used to qualify the path condition.
        value = value+power/(129*(1-square))
        return 2*lam*rho*value

    lo, hi = 0., .875
    last_path_upper = 0.
    for _ in range(40):
        middle = (lo+hi)/2
        path = path_upper(middle)
        if path.hi <= near_limit.lo:
            lo, last_path_upper = middle, path.hi
        else:
            hi = middle
    threshold = I((2*rho*I(lo)).lo)
    result = {
        'schema':'r622-longer-intrinsic-near-pair-complete-scalar-consequence-v1',
        'conditional_on_same_complete_continuous_input_hypotheses':True,
        'inputs':dict(zip(('delta','nu','derivative_upper','curvature_upper',
                          'reference_reach_lower','reference_diameter_upper'), entries)),
        'artanh_positive_terms':64, 'scalar_path_enclosure_calls':calls,
        'actual_x_search_upper':.875, 'actual_qualified_x':lo,
        'qualified_path_upper':last_path_upper,
        'near_length_limit_lower':near_limit.lo,
        'near_pair_threshold_lower':threshold.lo,
        'new_field_or_local_geometry_queries':0,
        'old_near_radius_not_mixed_with_new_threshold':True,
        'fixed_g_metric_or_README_completion_claim':False,
    }
    if threshold.lo <= (2*d).hi:
        result.update(established=False, reason='far-pair displacement budget not positive')
        return result
    near = I(9)/(10*K)
    far = (threshold-2*d)**2/(threshold**2/rho+2*n*threshold+4*d)
    tau = min(near.lo, far.lo)
    diameter = D0+2*d
    ratio = I(tau)/diameter
    result.update(established=tau>0,
        near_pair_reach_lower=near.lo, far_pair_reach_lower=far.lo,
        whole_surface_reach_lower=tau, whole_surface_diameter_upper=diameter.hi,
        whole_surface_reach_over_D_lower=ratio.lo,
        reach_ratio_point03_met=ratio.lo >= (I(3)/100).hi)
    return result
