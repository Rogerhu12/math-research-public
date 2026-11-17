#!/usr/bin/env python3
"""Export an accepted actual m3 integral-core prefix and audit finite samples.

The source integral reference is retained exactly once.  No original solver
gate is relaxed, no nonlinear equation is solved, and no continuous metric,
whole closed embedding, reach or ten-percent certificate is produced here.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys
import time

from m3_integral_prefix import (
    load_integral_prefix, M3IntegralCartesianPrefix, M3SharedPrefix, PAIRS,
    CLOSED, ROUND, sha)
import numpy as np
sys.path.insert(0, str(CLOSED))
from m3_shared_prefix import TailCutTarget, CartesianCutLift
from phase_angle_chart import PhaseAngleChart


def maximum_norm(array):
    return float(np.linalg.norm(array, axis=-1).max())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'short-bridge', 'checkpoint', 'port', 'outdir'):
        parser.add_argument('--'+key, type=Path, required=True)
    for key in ('tail-manifest', 'tail-reader', 'cap-source'):
        parser.add_argument('--'+key, type=Path)
    parser.add_argument('--library', type=Path,
                        help='Optional source snapshot; otherwise dispatched by exact core_kind/path')
    parser.add_argument('--angular', type=int, default=512)
    parser.add_argument('--radial', type=int, default=513)
    parser.add_argument('--center-width', type=float, default=.04)
    parser.add_argument('--cut-width', type=float, default=.04)
    parser.add_argument('--side-modes', type=int, default=32)
    args = parser.parse_args()
    tail_inputs = (args.tail_manifest, args.tail_reader, args.cap_source)
    if any(tail_inputs) and not all(tail_inputs):
        parser.error('The three optional tail inputs must be supplied together')
    if args.angular < 2*(3*args.side_modes+2) or args.radial < 2:
        parser.error('The sample grids are too small for this numerical audit')
    started = time.monotonic()
    record, obj, flow, sol, _ = load_integral_prefix(
        args.source_topic, args.short_bridge, args.checkpoint, args.port,
        args.angular, args.library)
    model = M3IntegralCartesianPrefix(obj, flow, sol, args.center_width, args.side_modes)
    source = M3SharedPrefix(obj, flow, sol, args.center_width)
    phase = PhaseAngleChart(model)
    psi = 2*np.pi*np.arange(args.angular)/args.angular
    center_delta = model.center_delta(psi)
    target = None
    if args.tail_manifest:
        spec = importlib.util.spec_from_file_location('integral_core_cap_source', args.cap_source)
        capmod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(capmod)
        tail = capmod.FiniteClosedTail(args.tail_manifest, args.tail_reader)
        target = TailCutTarget(model, tail)
        model.end_lift = CartesianCutLift(model, target, args.cut_width)
    points = np.unique(np.r_[np.linspace(0, flow.end, args.radial), model.rep.x,
                             (model.rep.x[:-1]+model.rep.x[1:])/2,
                             np.linspace(0, args.center_width, 65)])
    names = ('pos', 's1', 's2', 'p1', 'p2', 'sp')
    identity = {key: 0. for key in (*names, 'spp')}
    source_added = dict(identity)
    raw_change = dict.fromkeys(names, 0.)
    repaired_change = dict(raw_change)
    radial_change = np.zeros(3)
    metric = 0.
    curvature = 0.
    min_support, min_area = float('inf'), float('inf')
    max_radius = 0.
    for first in range(0, len(points), 16):
        s = points[first:first+16]
        old, g = source.raw_grid(s, args.angular)
        base_geo = obj.integral_unlifted_geo(flow, s, args.angular)
        source_reference = model.reference_correction(s, psi, source_radial=True)
        reference_pairs = list(zip(names, source_reference))
        fprime = model.source_lift_radial_jets(s)[1]
        reference_pairs.append(('spp', fprime[:, None, None]
                                *model.reference_angular_jets(psi)[2][None, :, :]))
        for key, value in reference_pairs:
            actual = g[key]-base_geo[key]
            identity[key] = max(identity[key], maximum_norm(actual-value))
            source_added[key] = max(source_added[key], maximum_norm(actual))
        raw, full = model.raw_evaluate(s, psi), model.evaluate(s, psi)
        for key, before, finite, repaired in zip(names, old, raw, full):
            raw_change[key] = max(raw_change[key], maximum_norm(finite-before))
            repaired_change[key] = max(repaired_change[key], maximum_norm(repaired-before))
        rj = np.stack([model.lift_rep(s, j)[0] for j in range(3)])
        radial_change = np.maximum(radial_change,
                                  abs(rj-model.source_lift_radial_jets(s)).max(axis=1))
        _, rho, _, ts, _, _ = phase.angular(s[:, None], psi[None, :])
        X, Xs, Xss, Xp, Xpp, Xsp = full
        Fs, Ft = Xs-ts[:, :, None]/rho[:, :, None]*Xp, Xp/rho[:, :, None]
        rad = flow.profile(s)[0]
        errors = np.stack((np.sum(Fs*Fs, axis=2)-1,
                           np.sum(Fs*Ft, axis=2)/rad[:, None],
                           np.sum(Ft*Ft, axis=2)/rad[:, None]**2-1), axis=2)
        metric = max(metric, float(np.sum(abs(np.fft.fft(errors, axis=1)
                                             /args.angular), axis=1).max()))
        cross = np.cross(Xp, Xs)
        area = np.linalg.norm(cross, axis=2)
        normal = cross/area[:, :, None]
        E, F, G = [np.sum(U*V, axis=2) for U, V in ((Xs, Xs), (Xs, Xp), (Xp, Xp))]
        L, M, N = [np.sum(U*normal, axis=2) for U in (Xss, Xsp, Xpp)]
        determinant = E*G-F*F
        trace = (L*G-2*M*F+N*E)/determinant
        gauss = (L*N-M*M)/determinant
        curvature = max(curvature, float(((abs(trace)
                        +np.sqrt(np.maximum(0, trace*trace-4*gauss)))/2).max()))
        min_area = min(min_area, float(area.min()))
        min_support = min(min_support, float(np.sum(X*normal, axis=2).min()))
        max_radius = max(max_radius, maximum_norm(X))
    center = model.evaluate([0.], psi)
    _, rho, rhop, ts, tss, rhos = phase.angular(np.zeros_like(psi), psi)
    v = ts/rho
    vp, vs = (rhos*rho-ts*rhop)/rho**2, (tss*rho-ts*rhos)/rho**2
    X, Xs, Xss, Xp, Xpp, Xsp = [x[0] for x in center]
    theta = psi-model.E0*np.sin(3*psi)/3
    core = model.core.evaluate(theta)
    ez = np.zeros_like(X)
    ez[:, 2] = 1.
    center_check = dict(
        X=maximum_norm(X-core['F']),
        Fs=maximum_norm(Xs-v[:, None]*Xp-ez),
        Fss=maximum_norm(Xss-2*v[:, None]*Xsp+v[:, None]**2*Xpp
                         +(v*vp-vs)[:, None]*Xp))
    seam_check = None
    if target is not None:
        endpoint = model.evaluate([flow.end], psi)
        wanted = target.angular_jets(psi)
        seam_check = {key: maximum_norm(value[0]-wanted[j][i])
                      for key, value, (i, j) in zip(names, endpoint, PAIRS)}
    args.outdir.mkdir(parents=True, exist_ok=False)
    packet = args.outdir/'integral-prefix-shared-data.npz'
    np.savez_compressed(packet, knots=model.rep.x, jets=model.rep.jets,
                        planar_modes=model.pm, height_modes=model.hm,
                        reference_radial_jets=model.lift_rep.jets,
                        reference_initial_projection=model.reference_initial,
                        mean_knots=sol.mean_spline.x, mean_jets=sol.mean_spline.jets,
                        phase_jets=phase.rep.jets)
    result = dict(
        scope=__doc__, argv=sys.argv, source=obj.integral_reader_provenance,
        definition=model.definition_record(), core_numerical_summary=model.core.summary(),
        packet_sha256=sha(packet), reader_sha256=sha(Path(__file__).with_name('m3_integral_prefix.py')),
        phase_chart_source_sha256=sha(CLOSED/'phase_angle_chart.py'),
        audit_sha256=sha(__file__), radial_samples=len(points), angular_samples=args.angular,
        sampled_single_source_lift_identity_errors=identity,
        sampled_source_lift_sizes=source_added,
        sampled_source_to_raw_finite_jet_changes=raw_change,
        sampled_source_to_repaired_finite_jet_changes=repaired_change,
        sampled_source_to_shared_radial_lift_changes=radial_change.tolist(),
        center_delta_angular_by_radial_sample_norms=[
            [maximum_norm(d) for d in angular] for angular in center_delta],
        center_numerical_identity=center_check, cut_numerical_identity=seam_check,
        explicit_phase_chart=phase.report(),
        numerical_profile_metric_fft_component_l1=metric,
        sampled_curvature=curvature, sampled_support_minimum=min_support,
        sampled_area_minimum=min_area, sampled_radius_maximum=max_radius,
        exact_circle_only_at_lambda_one=record['core_round_settings']['homotopy'] == 1,
        true_integral_g_error_budget_complete=False,
        continuous_core_inversion_and_quadrature_error_complete=False,
        whole_closed_embedding_or_reach_certified=False, bvp_solves=0,
        seconds=time.monotonic()-started)
    file = args.outdir/'integral-prefix-audit.json'
    file.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='done', output=str(file),
                          source_lift_identity=identity, center=center_check,
                          cut=seam_check, sampled_metric=metric,
                          seconds=result['seconds'])), flush=True)


if __name__ == '__main__':
    main()
