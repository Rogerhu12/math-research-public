#!/usr/bin/env python3
"""Small actual checks of the optional R93 reference interface, without solving.

The saved input remains UNSOLVED. Reprojected states are new numerical warm
representations only. This report is finite floating evidence, not a complete
continuous metric certificate or a solved prefix/tail.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import time

for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import numpy as np

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def identity(path):
    path = Path(path).resolve()
    value = path.read_bytes()
    return dict(path=str(path), bytes=len(value), sha256=hashlib.sha256(value).hexdigest())


def maximum(value):
    return float(np.max(abs(value)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--linear-port', type=Path, required=True)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    started = time.monotonic()
    loader_path = HERE/'db6f-prefix-flat-geometry-source.py'
    implementation_path = HERE/'78718-geometry-support-reference-interface.py'
    loader = module('support_reference_actual_source', loader_path)
    implementation = module('support_reference_interface', implementation_path)
    rec, old_obj, old_flow, old_sol = loader.source(args.checkpoint, args.linear_port, args.source_root)
    unused_rec, obj, flow, unused_sol = loader.source(args.checkpoint, args.linear_port, args.source_root)
    parameters = old_sol.p.copy()
    reference = implementation.coefficients_from_checkpoint(rec)
    if not np.array_equal(reference, old_obj._core.coefficients):
        raise ValueError('The declared saved support is not the literal replayed core')
    old_inlet = dict(old_obj._inlet_metrics)
    implementation.attach_bvp(obj, reference)
    initial = obj.initial(parameters).copy()
    reference_inlet = dict(obj._inlet_metrics)
    if not np.array_equal(initial, np.zeros_like(initial)):
        raise AssertionError('The stable anchored reference inlet must be exactly zero')
    N = 2048
    endpoint = np.array([flow.end])
    before = old_flow.geo(endpoint, N)
    after = flow.geo(endpoint, N)
    cut_keys = ('theta', 'rho', 'rhop', 'v', 'vs', 'vp', 'pos', 'p1', 'p2', 's1', 's2', 'sp', 'spp')
    cut = {k: maximum(after[k]-before[k]) for k in cut_keys}
    if max(cut.values()) != 0:
        raise AssertionError('Cut chart and complete background jets changed')

    # These are evaluations of one saved unsolved curve, not a new trajectory.
    s = flow.end*np.array([0., .071, .143, .251, .379, .507, .631, .719, .811, .917, 1.])
    transport = implementation.transport_state_jets(old_flow, old_sol.sol, flow, s, N)
    Y, DY, DDY = transport['state_jets']
    B, B1, B2 = flow.basis(N)
    projection = []
    for key, d in (('pos', Y), ('s1', DY), ('s2', DDY)):
        reconstructed = flow.values(flow.q*d, B)+transport['new_geometry'][key]
        j = ('pos', 's1', 's2').index(key)
        reconstructed[:, :, 2] += transport['mean_shift_jets'][j, :, None]
        projection.append(maximum(reconstructed-transport['jets'][key]))
    cut_state = [maximum(j[:, -1]-old_sol.sol(flow.end, k))
                 for k, j in enumerate((Y, DY, DDY))]
    a = flow.profile(s)[0][:, None]
    exact_tangent = transport['jets']['p1']/transport['new_geometry']['rho'][:, :, None]
    projected_tangent = (flow.values(flow.q*Y, B1)+transport['new_geometry']['p1'])/transport['new_geometry']['rho'][:, :, None]
    G_exact = np.sum(exact_tangent**2, axis=2)/a**2-1
    G_projected = np.sum(projected_tangent**2, axis=2)/a**2-1
    G = dict(transported_saved_curve_FFT_l1=float(np.max(np.sum(abs(np.fft.fft(G_exact, axis=1)/N), axis=1))),
             projected_new_warm_FFT_l1=float(np.max(np.sum(abs(np.fft.fft(G_projected, axis=1)/N), axis=1))),
             new_warm_minus_exact_transport_max_sampled=maximum(G_projected-G_exact))

    # One meaningful state derivative check: the unchanged full finite
    # Jacobian must differentiate the new background/chart RHS correctly.
    use = np.array([1, 3, 5, 7, 9])
    ss, yy = s[use], Y[:, use]
    rng = np.random.default_rng(20261110)
    direction = rng.normal(size=yy.shape)
    J, parameter_J = flow.fun_jac(ss, yy, parameters)
    analytic = np.einsum('ijk,jk->ik', J, direction)
    step = 1e-25
    numerical = flow.fun(ss, yy.astype(complex)+1j*step*direction, parameters).imag/step
    jacobian = dict(relative_l2=float(np.linalg.norm(numerical-analytic)/max(np.linalg.norm(numerical), 1e-30)),
                    max_absolute=maximum(numerical-analytic),
                    parameter_block_max=maximum(parameter_J), points=len(ss), complex_step=step)
    if jacobian['relative_l2'] > 1e-10:
        raise AssertionError('Anchored finite RHS/Jacobian disagree')

    # Test the explicit s derivative against an actual curve-valued path,
    # with points separated from all polynomial/spline changes.
    dy = flow.fun(ss, yy, parameters)
    fr, unused_sp, velocity_s = flow.velocity_s(ss, yy, dy)
    h = 2e-6
    plus = flow.frame(ss+h, flow.q*(yy+h*dy))['V']
    minus = flow.frame(ss-h, flow.q*(yy-h*dy))['V']
    dW_fd = (plus-minus)/(2*h)
    time_derivative = dict(central_difference_step=h,
                          absolute=maximum(dW_fd-velocity_s),
                          relative_l2=float(np.linalg.norm(dW_fd-velocity_s)/max(np.linalg.norm(velocity_s), 1e-30)))

    # Geometry derivative check at arbitrary non-grid angles. Each check
    # couples distinct provided jets, rather than re-evaluating one formula.
    geometry = flow._support_reference_geometry
    psi = np.array([.067, .289, .527, .941, 1.487])
    t = flow.end*np.array([.091, .233, .419, .613, .883])
    center = geometry.evaluate(t, psi)
    h_s, h_p = 1e-6, 1e-6
    gp, gm = geometry.evaluate(t+h_s, psi), geometry.evaluate(t-h_s, psi)
    pp, pm = geometry.evaluate(t, psi+h_p), geometry.evaluate(t, psi-h_p)
    jets = dict(pos_s=maximum((gp['pos']-gm['pos'])/(2*h_s)-center['s1']),
                p1_s=maximum((gp['p1']-gm['p1'])/(2*h_s)-center['sp']),
                p2_s=maximum((gp['p2']-gm['p2'])/(2*h_s)-center['spp']),
                s1_s=maximum((gp['s1']-gm['s1'])/(2*h_s)-center['s2']),
                pos_p=maximum((pp['pos']-pm['pos'])/(2*h_p)-center['p1']),
                p1_p=maximum((pp['p1']-pm['p1'])/(2*h_p)-center['p2']))

    # Finite neighboring coefficient points illustrate the proven quadratic
    # remainder. They are not optimized or solved candidates.
    change = np.zeros_like(reference)
    change[0] = 1e-4
    change[-1] = 1e-6
    quadratic = []
    for scale in (1., .5, .25, .125, .0625):
        c = reference+scale*change
        p = np.r_[math.log(c[0]/obj.seed_support_amplitude), c[1:]/obj.pscale]
        obj.initial(p)
        row = dict(scale=scale, **obj._inlet_metrics)
        row['metric_l1_over_scale_squared'] = row['metric_l1']/scale**2
        quadratic.append(row)
    obj.initial(parameters)
    inputs = [identity(args.checkpoint), identity(args.linear_port)]
    for part in rec.get('pp_coefficient_chunks', []):
        inputs.append(identity(args.checkpoint.parent/part['file']))
    report = dict(schema='78718-actual-support-reference-interface-v1', scope=__doc__,
                  inputs=inputs, implementation=identity(implementation_path),
                  script=identity(__file__), loader=identity(loader_path),
                  original_solver_success=rec.get('solver_success'), original_status=rec.get('status'),
                  reference_kind=flow._support_reference_record['kind'],
                  reference_coefficient_sha256_f64=hashlib.sha256(reference.astype('<f8').tobytes()).hexdigest(),
                  reference_triangle_rho_lower=geometry.radius_lower,
                  old_inlet=old_inlet, reference_inlet=reference_inlet,
                  exact_zero_initial_state=True, cut_background_two_jet_differences=cut,
                  radial_evaluations=len(s), angular_evaluations=N,
                  pullback_coordinate_residual=transport['coordinate_residual'],
                  projection_position_first_second_max=projection,
                  cut_projected_state_first_second_max_difference=cut_state,
                  mean_shift_value_first_second_max=[maximum(x) for x in transport['mean_shift_jets']],
                  angular_metric_finite_diagnostic=G,
                  finite_RHS_jacobian=jacobian, velocity_s_difference=time_derivative,
                  background_jet_difference=jets,
                  neighboring_quadratic_inlet_diagnostics=quadratic,
                  BVP_calls=0, DN_calls=0, radial_integrations=0, production_changed=False,
                  continuous_metric_certificate=False, actual_closed_surface=False,
                  seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps(dict(output=identity(args.out), exact_zero_initial=True,
                          anchored_inlet_metric_fft_l1=reference_inlet['metric_l1'],
                          cut_jet_difference=max(cut.values()),
                          jacobian_relative=jacobian['relative_l2'],
                          radial_velocity_relative=time_derivative['relative_l2'],
                          quadratic_metric=[x['metric_l1'] for x in quadratic],
                          seconds=report['seconds']), sort_keys=True))


if __name__ == '__main__':
    main()
