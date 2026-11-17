#!/usr/bin/env python3
"""Couple a complete frozen raw n4 core to its original nonlinear finite tail.

The input's physical profile, raw anchor J, full material core, and chart are
preserved by refine_fixed_raw_n4.build_seed.  The unknowns are the primary
amplitude and all raw controls, including c8.  Eta and the primary/control
transition widths stay fixed.  The original TailMixin, actual outer loop,
finite-tail residual gate and final two-jet audit are used unchanged.

Replacing a linear DN by the actual DN is a new coupled finite solve.  Uniform
height warmups are initial guesses, not orders of an amplitude expansion.
No exact circular arc, infinite tail, closed family or reach is inferred.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def read_tail_checkpoint(path):
    raw = Path(path).read_bytes()
    rec = json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)
    prior = (rec.get('response', {}).get('checkpoint') or
             rec.get('seam', {}).get('tail_checkpoint') or
             rec.get('checkpoint') or rec)
    if not all(k in prior for k in ('parameters', 'states', 'cutHeight')):
        raise ValueError('A complete actual finite-tail initial state is required')
    return prior


def checked_input_audit(path, rec):
    """Bind the finite prefix audit to the solved checkpoint parameters."""
    audit = json.loads(Path(path).read_text())
    if (audit.get('success') is not True or
            audit.get('nodes') != len(rec['mesh']) or
            audit.get('physical_profile') != rec['physical_profile'] or
            audit.get('parameters') != rec['parameters']):
        raise ValueError('The input prefix audit and complete checkpoint disagree')
    metric = audit.get('summary', {}).get('metric_l1')
    if metric is None or not np.isfinite(metric) or metric > 1e-6:
        raise ValueError('The sampled complete input prefix metric has not passed 1e-6')
    return dict(path=str(Path(path).resolve()), sha256=digest(path),
                metric_l1=metric, nodes=audit['nodes'],
                scope='Matching solved parameters, mesh size and physical profile; sampled prefix gate only.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('prefix-loader-dir', 'source-topic', 'tail-source',
                'sparse-helper', 'checkpoint', 'input-audit', 'config', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--tail-initial', type=Path)
    p.add_argument('--modes', type=int, default=20)
    p.add_argument('--angular', type=int, default=1280)
    p.add_argument('--quadrature', type=int, default=512)
    p.add_argument('--steps', type=int, default=16)
    p.add_argument('--parts', type=int, default=16)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--tol', type=float, default=1e-8)
    p.add_argument('--bc-tol', type=float, default=1e-8)
    p.add_argument('--physical-bc-tol', type=float, default=1e-10)
    p.add_argument('--node-heap', type=int, default=1536)
    p.add_argument('--scales', type=float, nargs='+', default=[.2, .5, 1.])
    p.add_argument('--check-only', action='store_true')
    a = p.parse_args()
    a.lagged_tail = True
    if a.quadrature <= 16 * a.modes or a.quadrature & (a.quadrature - 1):
        raise ValueError('Original tail requires power-of-two N > 4*M*spacing')
    if (any(not np.isfinite(t) or t <= 0 or t > 1 for t in a.scales) or
            a.scales[-1] != 1 or any(t >= u for t, u in zip(a.scales, a.scales[1:]))):
        raise ValueError('Uniform initialization scales must increase to full height 1')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    summary_path = a.out.with_name(a.out.name + '-summary.json')
    if summary_path.exists() or a.out.with_suffix('.json.gz').exists():
        raise FileExistsError('Use a new output prefix; completed records are immutable')
    sys.path.insert(0, str(a.prefix_loader_dir.resolve()))
    source = a.tail_source.resolve()
    coupler = module('n4_raw_actual_original_coupler',
                     source / 'scripts/db6f-prefix-coupled.py')
    from refine_fixed_raw_n4 import build_seed
    seed = build_seed(
        a.source_topic, a.checkpoint, a.modes, a.angular,
        bvp_transform=lambda B: type('N4RawActualTailBVP',
                                     (coupler.TailMixin, B), {}),
        configure_obj=lambda obj: setattr(
            obj, 'bcweights', np.full(obj.M, a.physical_bc_tol / a.bc_tol)),
        evaluate_boundary=False)
    obj, par, x, y = (seed[k] for k in ('obj', 'par', 'x', 'y'))
    rec = seed['record']
    if (not rec['solver_success'] or not rec.get('fixed_metric') or
            'raw_control_anchor_modes' not in rec):
        raise ValueError('Input must be a solved full raw fixed-profile checkpoint')
    frozen = dict(rec['physical_profile'])
    if obj.cfg != frozen or not obj.fixed:
        raise ValueError('The actual checkpoint physical profile was not frozen')
    audit = checked_input_audit(a.input_audit, rec)
    cfg = json.loads(a.config.read_text())
    for key in ('initialCheckpoint', 'designInitialCheckpoint',
                'secantCheckpoint', 'traceFile'):
        cfg.pop(key, None)
    cfg.update(modes=obj.M, spacing=4, shootingParts=a.parts,
               quadrature=a.quadrature, steps=a.steps)
    for key, value in rec['physical_port']['parameters'].items():
        if cfg.get(key) != value:
            raise ValueError('Physical tail parameter mismatch: ' + key)
    if cfg.get('solveTolerance') != 2e-9:
        raise ValueError('The recorded original 2e-9 finite-tail gate is required')
    initialization = dict(
        kind='cold original linear stage graph',
        scope='No state from a different physical tail is substituted; uniform H scaling is initialization only.')
    if a.tail_initial:
        prior = read_tail_checkpoint(a.tail_initial)
        old = prior['parameters']
        if old['modes'] > obj.M or old['spacing'] != 4:
            raise ValueError('Tail initialization cannot discard modes or change spacing')
        if (old.get('physicalDepth', old.get('depth')) > cfg['depth'] or
                a.parts % old.get('shootingParts', 1)):
            raise ValueError('Tail initialization requires nested depth and parts')
        # The original worker checks every physical geometry parameter again.
        for key, value in rec['physical_port']['parameters'].items():
            if old.get(key) != value:
                raise ValueError('Initial tail has different physical geometry: ' + key)
        cfg['initialCheckpoint'] = str(a.tail_initial.resolve())
        initialization.update(
            kind='original nested remesh', input_sha256=digest(a.tail_initial),
            source_modes=old['modes'], target_modes=obj.M,
            source_parts=old.get('shootingParts'), target_parts=a.parts,
            source_depth=old.get('physicalDepth', old.get('depth')),
            target_depth=cfg['depth'],
            remesh_sha256=digest(source / 'scripts/950f-tail-warm-remesh.mjs'))
    cfg['traceFile'] = str(a.out.with_name(a.out.name + '-worker-trace.jsonl'))
    config = a.out.with_name(a.out.name + '-config.json')
    config.write_text(json.dumps(cfg, indent=2) + '\n')
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER'] = str(a.sparse_helper.resolve())
    os.environ['VISIBLE_FLEX_SPARSE_TRACE'] = str(
        a.out.with_name(a.out.name + '-linear-trace.jsonl'))
    client = module('n4_raw_actual_original_client',
                    source / 'scripts/950f-tail-client-v3.py')
    if not hasattr(client.WeightedTailPort, '_record_exit'):
        raise ValueError('Use the native observed client with stderr and return-code records')
    summary = dict(
        scope=__doc__, command=sys.argv, solver_success=False,
        status='seed_checked', input_checkpoint_sha256=digest(a.checkpoint),
        input_audit=audit, script_sha256=digest(__file__),
        fixed_physical_profile=frozen, seed=seed['diagnostics'],
        plateau_settings=dict(seed['settings']),
        raw_control_anchor_modes=rec['raw_control_anchor_modes'],
        raw_c8='free physical control; preserved from input parameters',
        original_coupler_sha256=digest(source / 'scripts/db6f-prefix-coupled.py'),
        sparse_helper_sha256=digest(a.sparse_helper),
        config_sha256=digest(config), input_config_sha256=digest(a.config),
        periodic_engine_sha256={f.name: digest(f) for f in
                                (source / 'scripts/periodic-quadrature').glob('*.mjs')},
        tail_initialization=initialization,
        warmup_path='Uniform scaling of every component of actual H; initialization only.',
        warmup=[])
    def persist():
        temporary = summary_path.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(summary, indent=2) + '\n')
        temporary.replace(summary_path)
    persist()
    print(json.dumps(dict(event='raw_actual_seed_checked', modes=obj.M,
                          nodes=len(x), physical_profile=frozen,
                          plateau_settings=seed['settings'],
                          core_anchor=rec['raw_control_anchor_modes'],
                          identity={k: seed['diagnostics'][k] for k in
                                    ('complete_core_identity_error',
                                     'complete_map_projection_error',
                                     'input_mesh_nodes', 'seed_mesh_nodes',
                                     'input_mesh_coverage_max')})), flush=True)
    if a.check_only:
        return
    tail = None
    started = time.monotonic()
    try:
        tail = client.WeightedTailPort(
            config, source / 'repro/source-root',
            a.out.with_name(a.out.name + '-tail'), node_heap=a.node_heap)
        obj.tail = tail
        summary['linear_dn_difference'] = float(abs(
            tail.linearD - np.asarray(rec['physical_port']['linearSlope'][:obj.M])).max())
        height = obj.bridge.sigma * obj.q * y[obj.iz:, -1]
        print(json.dumps(dict(event='actual_tail_ready', modes=obj.M,
                              linear_dn_difference=summary['linear_dn_difference'],
                              first_height=float(height[0]),
                              second_height=float(height[1]))), flush=True)
        for scale in a.scales:
            response = tail.solve(height * scale, jacobian=False, audit=True)
            row = dict(scale=scale, residual=response['residual'],
                       converged=response['converged'], tail_calls=tail.calls)
            summary['warmup'].append(row)
            summary['status'] = 'warmup'
            persist()
            print(json.dumps(dict(event='actual_height_warmup', **row)), flush=True)
        from f6curve_domain_newton import install, STATS
        from trace_domain_newton import install as observe_newton
        from curve_stable_prefix_bvp import save_checkpoint
        install()
        observe_newton(a.out.with_name(a.out.name + '-newton.jsonl'))
        sol, outer = coupler.solve_with_actual_tail(obj, tail, x, y, par, a)
        obj.initial(sol.p)
        flow = obj.flow(sol.p[0])
        if obj.cfg != frozen or seed['settings'] != rec['plateau_settings']:
            raise ValueError('The frozen physical profile or raw-core settings changed')
        physical = SimpleNamespace(
            x=obj.chart(sol.x, sol.p[0])[0], y=sol.y, p=sol.p)
        physical.sol = flow.c2_interpolant(physical)
        out = {**rec, 'scope': __doc__, 'profile': frozen,
               'physical_profile': frozen, 'frozen_profile': frozen,
               'fixed_metric': True, 'tail_config': cfg,
               'parameters': sol.p.tolist(),
               'central_correction_scales': obj.pscale.tolist(),
               'gauge_amplitude': obj.q,
               'actual_primary_amplitude': obj.support_amplitude,
               'core_summary': obj._core.summary(),
               'solver_success': bool(sol.success), 'message': sol.message,
               'nodes': len(sol.x), 'mesh': physical.x.tolist(),
               'pp_coefficients': physical.sol.c, 'meridian_length': flow.end,
               'actual_outer_checks': outer,
               'max_rms': float(np.max(sol.rms_residuals)),
               'max_bc': float(np.max(abs(obj.bc(sol.y[:, 0], sol.y[:, -1], sol.p)))),
               'domain_newton': dict(STATS)}
        out['config'] = {**rec['config'], 'modes': obj.M, 'angular': obj.nt,
                         'core_kind': 'n4_fixed_raw_mean_circle',
                         'actual_nonlinear_tail': True, 'fixed_metric': True,
                         'tol': a.tol, 'bc_tol': a.bc_tol,
                         'physical_bc_tol': a.physical_bc_tol}
        out['raw_control_anchor_modes'] = rec['raw_control_anchor_modes']
        out['core_projection_order'] = seed['core_projection_order']
        if sol.success:
            out['summary'] = seed['adaptive'].audit(obj, physical, max(512, obj.nt))
            out['summary']['scope'] = (
                'Sampled complete raw-core prefix metric and Cartesian Darboux '
                'tensor at the fixed physical profile. Original nonlinear DN '
                'and full mean/nonmean two-jet audit are in tail_seam. No '
                'continuous-angle, infinite closure or reach theorem is asserted.')
            out['complete_metric_pass'] = bool(out['summary']['metric_l1'] <= 1e-6)
            out['tail_seam'] = obj.seam_audit(physical)
            if out['max_bc'] > a.bc_tol or not out['tail_seam']['tail_converged']:
                raise FloatingPointError('Original actual terminal gate is not satisfied')
        out['seconds'] = time.monotonic() - started
        out['tail_calls'] = tail.calls
        save_checkpoint(a.out.with_suffix('.json.gz'), out)
        summary.update({k: v for k, v in out.items()
                        if k not in ('mesh', 'pp_coefficients', 'physical_port')})
        summary['status'] = 'completed'
        print(json.dumps(dict(event='result', success=out['solver_success'],
                              complete_metric_pass=out.get('complete_metric_pass'),
                              nodes=out['nodes'], rms=out['max_rms'],
                              actual_bc=out['max_bc'], actual_q=obj.support_amplitude,
                              tail_calls=tail.calls)), flush=True)
    except Exception as exc:
        summary.update(solver_success=False, status='exception', error=repr(exc),
                       tail_calls=tail.calls if tail else 0)
        print(json.dumps(dict(event='failure', error=repr(exc))), flush=True)
    finally:
        if tail:
            summary['worker_returncode_before_close'] = tail.proc.poll()
            summary['tail_source_sha256'] = tail.sources
            tail.close()
            summary['worker_returncode_after_close'] = tail.proc.returncode
            summary['native_worker_exit_path'] = str(tail.exit_path)
            summary['native_worker_stderr_path'] = str(tail.stderr_path)
        summary['seconds'] = time.monotonic() - started
        persist()


if __name__ == '__main__':
    main()
