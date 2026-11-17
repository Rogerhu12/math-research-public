#!/usr/bin/env python3
"""Uniform radial budget for R36/R37 angular core remainders.

Only shared scalar quintics, the true fixed atlas and explicit Hermite
coefficients are bounded.  No principal-map metric, BVP or closed-surface
geometry is computed.  An allowed principal-metric threshold is conditional.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

from certify_protected_arc_curvature_dual import decimal
from prefix_true_profile import TruePrefix, float_bound
from certify_background_sharp import lower, upper, q


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ff(x):
    return F.from_float(float(x))


def quintic(left, right, jets):
    h = ff(right)-ff(left)
    assert h > 0
    y0, d0, q0 = (ff(jets[j, 0]) for j in range(3))
    y1, d1, q1 = (ff(jets[j, 1]) for j in range(3))
    e0, e1, e2 = y1-y0-h*d0-h*h*q0/2, h*(d1-d0)-h*h*q0, h*h*(q1-q0)
    return [y0, h*d0, h*h*q0/2, 10*e0-4*e1+e2/2, -15*e0+7*e1-e2, 6*e0-3*e1+e2/2], h


def derivative(co, scale=F(1)):
    return [F(j)*v/scale for j, v in enumerate(co) if j]


def bernstein_absolute(co, left=F(0), right=F(1)):
    degree = len(co)-1
    span = right-left
    transformed = [sum((co[j]*math.comb(j, k)*left**(j-k)*span**k
                        for j in range(k, degree+1)), F(0)) for k in range(degree+1)]
    values = [sum((transformed[j]*F(math.comb(k, j), math.comb(degree, j))
                   for j in range(k+1)), F(0)) for k in range(degree+1)]
    return max(abs(v) for v in values)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('data', 'prefix-audit', 'checkpoint', 'core-certificate', 'angular-certificate', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--circle-degree', type=int, default=16)
    args = p.parse_args()
    began = time.monotonic()
    audit = json.loads(args.prefix_audit.read_text())
    core = json.loads(args.core_certificate.read_text())
    angular = json.loads(args.angular_certificate.read_text())
    checkpoint = json.load(gzip.open(args.checkpoint, 'rt'))
    data = np.load(args.data)
    cp_hash = sha(args.checkpoint)
    assert cp_hash == audit['source']['checkpoint_sha256'] == core['checkpoint_sha256'] == angular['checkpoint_sha256']
    assert sha(args.data) == audit['packet_sha256'] == angular['packet_input_sha256']
    assert core['observed_exit_code'] == angular['observed_exit_code'] == 0
    assert angular['continuous_core_C1_remainder_certified']
    assert audit['cut_numerical_identity'] is None
    command = audit['argv']
    width = ff(command[command.index('--center-width')+1] if '--center-width' in command else .04)
    knots = data['knots']
    phase_source = Path(__file__).resolve().parent.parent/'finite_closure/m3_m8_closed_map/phase_angle_chart.py'
    assert sha(phase_source) == audit['phase_chart_source_sha256']
    # The recorded PhaseAngleChart constructor uses prefix.rep.x literally;
    # this packet intentionally stores that common knot array only once.
    assert data['phase_jets'].shape == data['reference_radial_jets'].shape == (3, 1, len(knots))
    assert np.any(knots == float(width))
    assert np.array_equal(data['reference_radial_jets'][:, 0, 0], [1., 0., 0.])
    er = F(angular['reference_phase_exact'])
    ec, epp = ff(data['phase_jets'][0, 0, 0]), ff(data['phase_jets'][2, 0, 0])
    assert er == ff(audit['definition']['theta0_e'])
    assert ec == F(angular['center_phase_exact'])
    f0 = f1 = phase0 = phase1 = F(0)
    active_end = width
    for j in range(len(knots)-1):
        span = slice(j, j+2)
        f, h = quintic(knots[j], knots[j+1], data['reference_radial_jets'][:, 0, span])
        e, _ = quintic(knots[j], knots[j+1], data['phase_jets'][:, 0, span])
        a, b = bernstein_absolute(f), bernstein_absolute(derivative(f, h))
        f0, f1 = max(f0, a), max(f1, b)
        phase0 = max(phase0, bernstein_absolute(e))
        phase1 = max(phase1, bernstein_absolute(derivative(e, h)))
        if a or b:
            active_end = max(active_end, ff(knots[j+1]))
    phase_rho = 1-phase0
    assert phase_rho > 0
    h00, h01 = F(1), F(15, 8)/width
    h20 = F(54, 3125)*width*width
    h2_unit = [F(0), F(0), F(1, 2), F(-3, 2), F(3, 2), F(-1, 2)]
    h21 = width*max(bernstein_absolute(derivative(h2_unit), F(j, 64), F(j+1, 64)) for j in range(64))
    b0, b1 = abs(epp)/3, abs(epp)
    m = F(core['global_true_core_bounds']['rho_lower'])
    assert m > 0
    d = abs(ec-er)
    delta0, delta1 = d/3, d+(1+abs(er))*d/(3*m)
    G0, G1, T0, T1 = (F(angular['uniform_true_remainder_bounds'][key])
                       for key in ('G_value', 'G_first_psi', 'T_value', 'T_first_psi'))
    degree = args.circle_degree
    assert degree >= 1
    z = abs(er)/3
    circle0 = z**(degree+1)/math.factorial(degree+1)
    circle1 = circle0+abs(er)*z**degree/math.factorial(degree)
    value = f0*G0+(f0+h00)*circle0+h00*delta0+h20*b0*T0
    radial = f1*G0+(f1+h01)*circle0+h01*delta0+h21*b0*T0
    angular_error = f0*G1+(f0+h00)*circle1+h00*delta1+h20*(b1*T0+b0*T1)
    physical = checkpoint['physical_tail_parameters']
    true = TruePrefix(checkpoint['frozen_profile'],
                      dict(radius=physical['rCut'], backgroundSlope=physical['wCut']),
                      checkpoint['meridian_length'])
    assert active_end < ff(checkpoint['meridian_length'])-ff(true.cut_width)
    assert upper(true.lam*q(float(active_end))) < lower(true.prefix)
    # On this whole support, sigma=lam*s lies in the true flat out-and-back
    # prefix.  Its radius is >=1.  The actual tiny cut atlas correction is
    # disjoint from the error support, so only lam enters the radial factor.
    radius_lower = F(1)
    sigma_lower = ff(float_bound(true.lam)[0])
    assert sigma_lower > 0
    normalized_s = (radial+phase1*angular_error/(3*phase_rho))/sigma_lower
    normalized_theta = angular_error/(radius_lower*phase_rho)
    epsilon = normalized_s+normalized_theta
    target = F(1, 10**6)
    allowed = (target-2*epsilon-epsilon*epsilon)/(1+2*epsilon)
    assert allowed > 0
    epsilon_declared = F('5.940838571e-9')
    principal_declared = F('9.88118311e-7')
    assert epsilon < epsilon_declared
    declared_total = principal_declared+2*(1+principal_declared)*epsilon_declared+epsilon_declared**2
    assert declared_total < target
    here = Path(__file__).resolve().parent
    source_files = [Path(__file__), phase_source, here/'prefix_true_profile.py', here/'certify_background_sharp.py',
                    here/'certify_protected_arc_curvature_dual.py']
    result = dict(
        scope=__doc__, command=sys.argv,
        source_sha256={str(f): sha(f) for f in source_files},
        input_sha256={str(f): sha(f) for f in (args.data, args.prefix_audit, args.checkpoint,
                                               args.core_certificate, args.angular_certificate)},
        scalar_shared_spans=len(knots)-1, exact_fraction_Bernstein_on_every_span=True,
        scalar_bounds={key: decimal(v, True) for key, v in dict(
            f=f0, f_s=f1, phase_e=phase0, phase_e_s=phase1, h0=h00, h0_s=h01,
            h2=h20, h2_s=h21, b_psi=b0, b_psi_first=b1).items()},
        phase_rho_lower=decimal(phase_rho),
        active_error_support_end=str(active_end),
        active_error_support_end_upper=decimal(active_end, True),
        true_flat_prefix_end=float_bound(true.prefix),
        support_in_true_flat_region_verified=True,
        radius_lower_on_error_support=str(radius_lower),
        sigma_prime_lower_on_error_support=str(sigma_lower),
        circle_principal_degree=degree,
        circle_exact_remainder_bounds=dict(value=decimal(circle0, True), first_psi=decimal(circle1, True)),
        center_angle_difference_exact=str(d),
        center_curve_shift_bounds=dict(value=decimal(delta0, True), first_psi=decimal(delta1, True)),
        map_remainder_bounds=dict(value=decimal(value, True), s_derivative=decimal(radial, True),
                                  psi_derivative=decimal(angular_error, True)),
        normalized_differential_bounds=dict(s_column=decimal(normalized_s, True),
                                            theta_column=decimal(normalized_theta, True),
                                            sum_epsilon=decimal(epsilon, True)),
        sufficient_principal_metric_threshold=decimal(allowed),
        declared_rational_sufficient_budget=dict(epsilon_upper=str(epsilon_declared),
            principal_metric_upper=str(principal_declared),
            transferred_metric_upper=str(declared_total),
            target_minus_transferred_positive=str(target-declared_total)),
        target_complete_metric=str(target),
        metric_increment_if_principal_eta_le_target=decimal(2*(1+target)*epsilon+epsilon*epsilon, True),
        true_atlas_definition= true.report(),
        bvp_solves=0, principal_map_metric_computed=False,
        whole_closed_metric_or_geometry_certified=False,
        physical_parameters_or_map_changed=False,
        limitations='A proved differential budget for the core approximation error. The principal finite-map metric is still unpaid; the recorded raw M8 finite audit is above the metric gate, and an actual tail/cut lift is not included.',
        seconds=time.monotonic()-began)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'scalar_shared_spans', 'scalar_bounds', 'phase_rho_lower', 'active_error_support_end_upper',
        'map_remainder_bounds', 'normalized_differential_bounds', 'sufficient_principal_metric_threshold',
        'metric_increment_if_principal_eta_le_target', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
