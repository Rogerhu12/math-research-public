#!/usr/bin/env python3
"""Continue a saved high-core BVP to the actual end of its same turn law.

The profile a(s) is retained. The high core coefficients remain unknown, so
successive stages are candidate design continuation, not same-g refinement.
The original BVP source is imported without editing it. Its solve_bvp entry
is wrapped only to retain the accepted adaptive warm mesh. A homothetic
extension is an initial guess; every accepted stage solves the unmodified
Frenet/collocation equations and is separately checked.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
from fractions import Fraction
import numpy as np
from scipy.integrate import solve_bvp as scipy_solve_bvp
from scipy.interpolate import CubicHermiteSpline

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('geometry_r225_continue_native', P/'geometry_20261114_r225_high_core_bvp.py')
native = importlib.util.module_from_spec(spec)
spec.loader.exec_module(native)


def write_gzip(path, value):
    path.write_bytes(gzip.compress((json.dumps(value, indent=2)+'\n').encode(), mtime=0))


def merge_nodes(*arrays):
    """Merge a few-ulp duplicate; earlier arrays (accepted mesh) take priority."""
    tagged = sorted((float(value), priority) for priority, values in enumerate(arrays) for value in values)
    scale = max(1., max(abs(v) for v, _ in tagged))
    tolerance = 8*np.finfo(float).eps*scale
    groups = []
    for value, priority in tagged:
        if not groups or value-groups[-1][-1][0] > tolerance:
            groups.append([])
        groups[-1].append((value, priority))
    return np.array([min(group, key=lambda pair: pair[1])[0] for group in groups])


def uniform_mesh(end, settings, join):
    split = float(settings.get('refined_start', .7))
    base = float(settings.get('base_step', .0125))
    fine = float(settings.get('prefix_refined_step', .003125))
    turn = float(settings.get('turn_step', .001))
    return merge_nodes(np.linspace(0, split, int(np.ceil(split/base))+1),
                       np.linspace(split, join, int(np.ceil((join-split)/fine))+1),
                       np.linspace(join, end, int(np.ceil((end-join)/turn))+1))


def prepare_warm(current, target, settings, seed):
    ident = current['original_metric_identity']
    law = ident['law']
    M, N = current['M'], current['N']
    profile, turn = native.make_profile(law, settings['coast'], settings['target_speed'], settings['curvature'])
    core = np.array([float(Fraction(v)) for v in ident['coefficients_rational']])
    q = native.outward.FullCoreProbe(core, M, N, law['velocity'], law['length'], law['k0'])
    q.profile = profile
    oldx = np.asarray(current['mesh'])
    oldy = np.asarray(current['states'])
    oldf = np.asarray(current['rhs'])
    pp = CubicHermiteSpline(oldx, oldy, oldf, axis=0)
    extra = uniform_mesh(target, settings, turn['join'])
    mesh = merge_nodes(oldx, extra, [law['length'], target])
    values = pp(np.minimum(mesh, oldx[-1]))
    anchor = oldy[-1].copy()
    mean_index = 2*M+1
    mean = anchor[mean_index]
    anchor[mean_index] = 0.
    aa = profile(float(oldx[-1]))[0]
    gx, gw = np.polynomial.legendre.leggauss(32)
    for i in np.flatnonzero(mesh > oldx[-1]):
        s = mesh[i]
        value = (profile(float(s))[0]/aa)*anchor
        length = s-oldx[-1]
        ss = oldx[-1]+length*(gx+1)/2
        speeds = np.array([profile(float(v))[1] for v in ss])
        value[mean_index] = mean+length/2*float(gw @ np.sqrt(1-speeds*speeds))
        values[i] = value
    rhs = np.array([q.fun(float(s), y) for s, y in zip(mesh, values)])
    h = np.diff(mesh)
    midpoint = .5*(values[:-1]+values[1:])-(h[:, None]/8)*(rhs[1:]-rhs[:-1])
    for s, y in zip(.5*(mesh[:-1]+mesh[1:]), midpoint):
        q.frame(float(s), y)
    return dict(scope='Warm initial guess only; includes original accepted cubic field and a homothetic extension.',
                M=M, N=N, mesh=mesh.tolist(), states=values.tolist(), rhs=rhs.tolist(),
                previous_end=float(oldx[-1]), target_end=target,
                original_metric_identity=ident, turn=turn)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--initial', type=Path, required=True)
    ap.add_argument('--seed', type=Path, required=True)
    ap.add_argument('--out-dir', type=Path, required=True)
    ap.add_argument('--initial-step', type=float, default=.005)
    ap.add_argument('--maximum-step', type=float, default=.015)
    ap.add_argument('--minimum-step', type=float, default=.00015625)
    ap.add_argument('--max-stages', type=int, default=100)
    ap.add_argument('--max-nodes', type=int, default=1600)
    ap.add_argument('--tol', type=float, default=2e-6)
    ap.add_argument('--goal', type=float)
    ap.add_argument('--prepare-only', action='store_true')
    a = ap.parse_args()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    native_hash = hashlib.sha256((P/'geometry_20261114_r225_high_core_bvp.py').read_bytes()).hexdigest()
    current = native.read(a.initial)
    seed = native.read(a.seed)
    settings = current.get('parameters', {})
    required = ('coast', 'target_speed', 'curvature')
    if any(k not in settings for k in required):
        raise ValueError('Initial file must retain the original BVP profile parameters')
    if not np.all(np.isfinite(np.asarray(current['states']))):
        raise ValueError('Cannot use a nonfinite warm field')
    fixed_turn_end = float(current['turn']['whole_turn_end'])
    goal = fixed_turn_end if a.goal is None else float(a.goal)
    if goal > fixed_turn_end or goal <= current['mesh'][-1]:
        raise ValueError('Goal must extend the saved domain within the same complete turn')
    a.out_dir.mkdir(parents=True, exist_ok=True)
    progress = dict(scope=__doc__, source_sha256=source_hash, native_source_sha256=native_hash,
                    initial_file=str(a.initial), initial_sha256=hashlib.sha256(a.initial.read_bytes()).hexdigest(),
                    initial_solver_success=bool(current.get('success', False)),
                    same_scalar_profile=True, same_full_metric_claimed=False,
                    goal=goal, current_end=float(current['mesh'][-1]),
                    complete_turn=False, accepted=[], attempts=[])
    progress_path = a.out_dir/'progress.json'
    step = a.initial_step
    attempt = 0
    while progress['current_end'] < goal and len(progress['accepted']) < a.max_stages:
        target = min(goal, progress['current_end']+step)
        attempt += 1
        stem = f'stage-{attempt:03d}-s{target:.12f}'
        warm_path = a.out_dir/(stem+'-warm.json.gz')
        result_path = a.out_dir/(stem+'-result.json.gz')
        record = dict(attempt=attempt, from_s=progress['current_end'], target_s=target,
                      warm=str(warm_path), result=str(result_path), stage_status='pending')
        try:
            warm = prepare_warm(current, target, settings, seed)
            write_gzip(warm_path, warm)
            record['warm_nodes'] = len(warm['mesh'])
            terminal = 'cone' if target == fixed_turn_end else 'wkb'
            argv = [str(P/'geometry_20261114_r225_high_core_bvp.py'),
                    '--seed', str(a.seed), '--M', str(current['M']), '--N', str(current['N']),
                    '--end', repr(target), '--coast', str(settings['coast']),
                    '--target-speed', str(settings['target_speed']), '--curvature', str(settings['curvature']),
                    '--terminal', terminal, '--tol', str(a.tol),
                    '--max-nodes', str(max(a.max_nodes, len(warm['mesh'])+64)),
                    '--warm', str(warm_path), '--out', str(result_path)]
            for key in ('base_step', 'refined_start', 'prefix_refined_step', 'turn_step'):
                if key in settings:
                    argv += ['--'+key.replace('_', '-'), str(settings[key])]
            record['argv'] = ['python']+argv
            print(json.dumps(dict(event='continuation_stage', **record)), flush=True)
            if a.prepare_only:
                record['stage_status'] = 'prepared_only'
                progress['attempts'].append(record)
                progress_path.write_text(json.dumps(progress, indent=2)+'\n')
                return

            def merged_solver(fun, bc, x, y, *args, **kwargs):
                wx = np.asarray(warm['mesh'])
                wy = np.asarray(warm['states'])
                wf = np.asarray(warm['rhs'])
                xx = merge_nodes(wx, x)
                pp = CubicHermiteSpline(wx, wy, wf, axis=0)
                yy = pp(xx).T
                kwargs['max_nodes'] = max(kwargs['max_nodes'], len(xx)+64)
                return scipy_solve_bvp(fun, bc, xx, yy, *args, **kwargs)

            native.solve_bvp = merged_solver
            old_argv = sys.argv
            sys.argv = argv
            try:
                native.main()
            finally:
                sys.argv = old_argv
            result = native.read(result_path)
            result['continuation_adapter_sha256'] = source_hash
            result['continuation_initial_file'] = str(a.initial)
            result['adaptive_warm_mesh_preserved'] = True
            write_gzip(result_path, result)
            passed = bool(result['success']) and result['status'] == 0
            passed &= np.isfinite(result['collocation_rms_max']) and result['collocation_rms_max'] <= a.tol*1.001
            passed &= result['boundary_residual_max'] <= 1e-10
            passed &= result['core']['rho_sample_min'] > 0 and result['summary']['valid_sample_rows'] == len(result['mesh'])
            record.update(stage_status='accepted_finite_bvp' if passed else 'not_converged',
                          summary=result['summary'], core=result['core'],
                          collocation_rms_max=result['collocation_rms_max'],
                          boundary_residual_max=result['boundary_residual_max'])
            if passed:
                current = result
                progress['current_end'] = target
                progress['accepted'].append(dict(s=target, file=str(result_path),
                                                  sha256=hashlib.sha256(result_path.read_bytes()).hexdigest()))
                step = min(a.maximum_step, step*1.25)
            else:
                step *= .5
        except Exception as exc:
            record.update(stage_status='exception', error=repr(exc))
            step *= .5
        progress['attempts'].append(record)
        progress['complete_turn'] = progress['current_end'] == fixed_turn_end
        progress_path.write_text(json.dumps(progress, indent=2)+'\n')
        print(json.dumps(dict(event='continuation_progress', current_s=progress['current_end'],
                              complete_turn=progress['complete_turn'], next_step=step,
                              last_status=record['stage_status'])), flush=True)
        if step < a.minimum_step:
            progress['stopped_reason'] = 'No converged continuation at the minimum step; retain every actual failed attempt and change the design.'
            break
    if progress['current_end'] < goal and 'stopped_reason' not in progress:
        progress['stopped_reason'] = 'Finite stage budget reached; resume from the latest accepted file.'
    progress_path.write_text(json.dumps(progress, indent=2)+'\n')


if __name__ == '__main__':
    main()
