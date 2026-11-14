#!/usr/bin/env python3
"""R162: saved-state raw fade plus local current-radius reference checks.

This never constructs a DAE/BVP, evaluates its whole objective/Jacobian,
reprojects angular fields, or changes any saved physical parameter.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
from scipy.integrate import quad
from fd2d_gc_existing_tail_reference import (
    zero_tail_plateau_corrections, existing_tail_weight,
    existing_tail_reference, existing_tail_reference_interior,
    existing_tail_exact_cut_jet)
from fd2d_gc_positive_trace_branch import positive_trace_delta
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily


def identity(path):
    p = Path(path)
    return dict(path=str(p), bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def maxabs(a):
    return float(np.max(np.abs(a)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--fade-start', type=float, default=1.3)
    args = p.parse_args()
    if args.output.exists() or args.report.exists():
        raise RuntimeError('Use new output/report paths')
    started = time.perf_counter()
    root = Path(__file__).resolve().parent
    with np.load(args.input, allow_pickle=False) as archive:
        old = {k: np.array(archive[k], copy=True) for k in archive.files}
    definition = json.loads(str(old['positive_trace_definition']))
    seed = json.loads(str(old['seed_weight_definition']))
    coast = json.loads(str(old['coast_reference_definition']))
    gauss = json.loads(str(old['gauss_l_definition']))
    mesh, y, parameters = (old[k] for k in ('mesh', 'corrections', 'parameters'))
    stop, cut = definition['ramp_stop'], definition['cut']
    mode_count = int(old['modes'])
    profile_count = int(old['profile_count'])
    tail_count = len(parameters)-mode_count-profile_count
    assert tail_count >= 1 and y.shape == (len(mesh), 3*mode_count+2)
    assert old['candidate_sha256'].item() == identity(args.candidate)['sha256']
    assert definition['provider_source_sha256'] == identity(root/'fd2d_gc_raw_bump_positive_trace.py')['sha256']
    assert seed['end'] < args.fade_start
    assert coast['support'][1] < args.fade_start
    assert gauss['support'][1] < args.fade_start
    assert np.max(old['profile_supports'][:, 1]) <= definition['start'] <= stop
    assert mesh[-1] == cut and np.all(y[-1] == 0.)
    assert mesh[np.searchsorted(mesh, stop)] == stop
    tails = parameters[mode_count:mode_count+tail_count]
    assert np.all(tails >= 0) and np.all(tails <= 1.2)

    result = zero_tail_plateau_corrections(mesh, y, fade_start=args.fade_start,
                                          plateau_start=stop)
    new = {k: v.copy() for k, v in old.items()}
    new['corrections'] = result['corrections']
    info = result['info']
    info.update(input=identity(args.input), helper=identity(root/'fd2d_gc_existing_tail_reference.py'),
        original_representation_kind=str(old['representation_kind']),
        saved_positive_trace_definition_unchanged=True,
        existing_eta='S5((s-.42*cut)/(cut-.42*cut)), clipped',
        exact_reference_on_complete_plateau_cells='eta(s)*kappa(a(s)*sin(u))*B(u)+b(s,u)*I after the unchanged R155 window',
        local_formal_curvature_scope='Only protected K>0 trace plateau, not the earlier fade or full core',
        full_objective_not_evaluated=True)
    new['existing_tail_zero_initializer_definition'] = np.array(json.dumps(info, sort_keys=True))
    untouched = [k for k in old if k != 'corrections']
    copied_all = all(new[k].dtype == old[k].dtype and new[k].shape == old[k].shape
                     and new[k].tobytes() == old[k].tobytes() for k in untouched)
    assert copied_all
    assert new['parameters'].tobytes() == parameters.tobytes()
    assert new['corrections'][mesh <= args.fade_start].tobytes() == y[mesh <= args.fade_start].tobytes()
    zero_cells = np.array(info['complete_zero_raw_cells'], int)
    assert np.all(new['corrections'][zero_cells] == 0.)
    assert np.all(new['corrections'][zero_cells+1] == 0.)
    pairs = old['trace_gauge_pairs']
    gauge_error = maxabs(new['corrections'].ravel()[pairs[:,0]]+new['corrections'].ravel()[pairs[:,1]]) if len(pairs) else 0.
    assert gauge_error == 0.

    # Independent smooth scalar metric/weight/curvature, with both eta_s
    # and a_s terms nonzero.  These finite checks are not continuous bounds.
    ss = np.linspace(.1, .8, 17)[:, None]
    uu = np.linspace(0, 2*np.pi, 33, endpoint=False)[None, :]
    def synthetic(s, u, with_jet=False):
        a = 1-.1*s*s
        ap = -.2*s
        K = .2/a
        Ks = .04*s/(a*a)
        eta, etas = .3+.2*s*s, .4*s
        yy = a*np.sin(u)
        q, qy = .3+.2*yy*yy, .4*yy
        if with_jet:
            return existing_tail_reference_interior(a, ap, K, Ks, u, eta, etas, q, kappa_y=qy)
        return existing_tail_reference(a, K, u, eta, q, kappa_y=qy)
    syn = synthetic(ss, uu, True)
    step = 2e-6
    ds = (synthetic(ss+step, uu)['values']-synthetic(ss-step, uu)['values'])/(2*step)
    du = (synthetic(ss, uu+step)['values']-synthetic(ss, uu-step)['values'])/(2*step)
    radius = 1-.1*ss*ss
    c = -.2*ss/radius
    n, m, l = (syn['values'][...,j] for j in range(3))
    cod = np.stack((ds[...,0]-du[...,1]/radius-c*(l-n),
                    ds[...,1]-du[...,2]/radius+2*c*m), axis=-1)
    derivative_errors = dict(radial=maxabs(ds-syn['radial']), angular=maxabs(du-syn['angular']),
                             codazzi=maxabs(cod-syn['codazzi']))

    # Use exactly this candidate's cubic bridge and this saved tail vector.
    # Quad is only a finite numerical reader here; the proof uses the exact
    # defining integral and rational inequalities, not this error estimate.
    cfg = json.loads(args.candidate.read_text())
    piece = cfg['segments'][-1]
    assert piece['kind'] == 'phase_bridge' and piece['exact_endpoint_phase'] == '-pi/2'
    assert piece['ps0'] == piece['ps1'] == 0
    length, pd = float(piece['L']), -float(piece['p0'])
    assert F.from_float(length) > F(1,40)
    assert F.from_float(pd) > F(14499,10000)
    D = np.pi/2-pd
    points = np.unique(np.r_[mesh[zero_cells], .5*(mesh[zero_cells]+mesh[zero_cells+1]), cut])
    r = cut-points
    ep = D*(3*(r/length)**2-2*(r/length)**3)
    epr = 6*D*r*(1-r/length)/(length*length)
    eprr = 6*D*(1-2*r/length)/(length*length)
    radius = np.array([.8+quad(lambda z: np.cos(D*(3*(z/length)**2-2*(z/length)**3)),
                               0., float(rr), epsabs=1e-14, epsrel=1e-14)[0] for rr in r])
    ap = -np.cos(ep)
    K = np.sin(ep)*epr/radius
    Ks = -(np.cos(ep)*epr*epr/radius+np.sin(ep)*eprr/radius-
           np.sin(ep)*epr*np.cos(ep)/(radius*radius))
    eta, etas = existing_tail_weight(points, cut)
    u = np.arange(128)*2*np.pi/128
    family = PositiveFlatDevelopableFamily(tails)
    curve = family.angle_jets(radius[:,None]*np.sin(u)[None,:])
    q, qy = curve['kappa'], curve['kappa_y']
    ref = existing_tail_reference(radius[:,None], K[:,None], u[None,:], eta[:,None], q, kappa_y=qy)
    actual = positive_trace_delta(ref['base_values'], ref['base_angular'], K[:,None],
                                  np.ones_like(q), exact_tail_mask=(points==cut)[:,None])
    trace_error = maxabs(actual['actual']-ref['values'])
    trace_angle_error = maxabs(actual['actual_angular']-ref['angular'])
    interior = existing_tail_reference_interior(radius[:-1,None], ap[:-1,None], K[:-1,None], Ks[:-1,None],
        u[None,:], eta[:-1,None], etas[:-1,None], q[:-1], kappa_y=qy[:-1])
    nn, mm, ll = (ref['values'][...,j] for j in range(3))
    gauss_error = maxabs(nn*ll-mm*mm-K[:,None])
    cut_curve = family.angle_jets(.8*np.sin(u))
    cut_ref = existing_tail_exact_cut_jet(.8, u, cut_curve['kappa'], kappa_y=cut_curve['kappa_y'])
    true_cut = family.cut_port(u, position_jets=False)
    cut_values = np.stack([true_cut[k] for k in ('n','m','l')], axis=-1)
    cut_radial = np.stack([true_cut[k] for k in ('n_s','m_s','l_s')], axis=-1)
    cut_value_error, cut_radial_error = maxabs(cut_values-cut_ref['values']), maxabs(cut_radial-cut_ref['radial'])
    cap, ku, Ku = F(33,5), F(4725,736), F(75,64)
    margin = cap*(cap-ku)-Ku
    assert margin == F(633,36800)
    passed = max(derivative_errors.values()) < 1e-7 and max(trace_error, trace_angle_error) < 1e-10
    passed = passed and max(gauss_error,cut_value_error,cut_radial_error) < 1e-11
    passed = passed and float(np.max(ref['lambda_max'])) < float(cap)
    np.savez_compressed(args.output, **new)
    report = dict(schema='fd2d-existing-tail-zero-initializer-check-v1', passed=bool(passed),
        source=identity(__file__), helper=identity(root/'fd2d_gc_existing_tail_reference.py'),
        input=identity(args.input), candidate=identity(args.candidate), output=identity(args.output),
        bound_sources={name:identity(root/name) for name in (
            'fd2d_gc_raw_lifted_dae.py','fd2d_gc_raw_bump_dae.py','fd2d_gc_raw_bump_coast_reference.py',
            'fd2d_gc_raw_bump_positive_trace.py','fd2d_gc_positive_trace_branch.py',
            'fd2d_positive_flat_developable_family.py','fd2d_flat_developable_family.py')},
        modes=mode_count, tail_count=tail_count, profile_count=profile_count,
        copied_unchanged_array_keys=untouched, copied_arrays_byte_identical=copied_all,
        parameter_bytes_unchanged=True, upstream_correction_bytes_unchanged=True,
        trace_gauge_error=gauge_error, initializer=info,
        tail_control_min=float(tails.min()), tail_control_max=float(tails.max()),
        independent_jet_points=int(n.size), independent_jet_max_errors=derivative_errors,
        actual_local_points=int(q.size), actual_radial_points=points.tolist(),
        existing_trace_value_max_difference=trace_error,
        existing_trace_angular_max_difference=trace_angle_error,
        actual_local_gauss_arithmetic_error=gauss_error,
        actual_local_formal_curvature_max=float(np.max(ref['lambda_max'])),
        actual_local_pointwise_codazzi_max=float(np.max(np.abs(interior['codazzi']))),
        exact_cut_value_finite_error=cut_value_error, exact_cut_radial_jet_finite_error=cut_radial_error,
        exact_uniform_budget=dict(K_strict_upper=str(Ku), tail_curvature_upper=str(ku),
            formal_curvature_strict_cap=str(cap), rational_margin=str(margin),
            scope='R156 protected positive-K plateau only, all R132 nonnegative controls'),
        no_full_objective=True, no_Jacobian=True, no_BVP=True,
        same_field_refinement=False, physical_metric_unchanged=True,
        wall_seconds=time.perf_counter()-started,
        maximum_resident_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.report.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('passed','output','wall_seconds',
        'actual_local_formal_curvature_max','actual_local_pointwise_codazzi_max',
        'existing_trace_value_max_difference','independent_jet_max_errors')}))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
