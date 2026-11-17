#!/usr/bin/env python3
"""Refine one genuine n4 prefix--tail checkpoint at its fixed physical metric.

The full parameter-defined core and mapped prefix are embedded by build_seed.
The original TailMixin, actual outer checks, finite tail gates and final audit
are used unchanged. Cross-mode tail data are only a nested-remesh initial
state; they must satisfy the new full nonlinear M-mode problem afterwards.
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
import subprocess
import sys
import time
from types import SimpleNamespace
import numpy as np


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_tail_checkpoint(path):
    raw = Path(path).read_bytes()
    rec = json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)
    prior = (rec.get('response', {}).get('checkpoint') or
             rec.get('seam', {}).get('tail_checkpoint') or
             rec.get('checkpoint') or rec)
    if not all(k in prior for k in ('parameters', 'states', 'cutHeight')):
        raise ValueError('A complete actual finite-tail checkpoint is required')
    return prior


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('prefix-loader-dir', 'source-topic', 'tail-source',
                'sparse-helper', 'checkpoint', 'tail-initial', 'config', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--modes', type=int, default=20)
    p.add_argument('--angular', type=int, default=1280)
    p.add_argument('--quadrature', type=int, default=512)
    p.add_argument('--steps', type=int, default=16)
    p.add_argument('--parts', type=int, default=8)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--tol', type=float, default=1e-8)
    p.add_argument('--bc-tol', type=float, default=1e-8)
    p.add_argument('--physical-bc-tol', type=float, default=1e-10)
    p.add_argument('--node-heap', type=int, default=2304)
    a = p.parse_args()
    a.lagged_tail = True
    if a.quadrature <= 16 * a.modes or a.quadrature & (a.quadrature - 1):
        raise ValueError('Original tail requires power-of-two N > 4*M*spacing')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(a.prefix_loader_dir.resolve()))
    source = a.tail_source.resolve()
    coupler = module('n4_frozen_actual_original_coupler',
                     source / 'scripts/db6f-prefix-coupled.py')
    from refine_fixed_large_radius import build_seed
    seed = build_seed(
        a.source_topic, a.checkpoint, a.modes, a.angular,
        bvp_transform=lambda B: type('N4FrozenActualTailBVP',
                                     (coupler.TailMixin, B), {}),
        configure_obj=lambda obj: setattr(
            obj, 'bcweights', np.full(obj.M, a.physical_bc_tol / a.bc_tol)),
        evaluate_boundary=False)
    obj, par, x, y = (seed[k] for k in ('obj', 'par', 'x', 'y'))
    rec = seed['record']
    if not rec['solver_success'] or not rec['config'].get('actual_nonlinear_tail'):
        raise ValueError('Input must be a genuinely accepted actual-tail checkpoint')
    frozen = dict(rec['physical_profile'])
    if obj.cfg != frozen or not obj.fixed:
        raise ValueError('The true checkpoint physical metric was not frozen')
    cfg = json.loads(a.config.read_text())
    for key in ('initialCheckpoint', 'designInitialCheckpoint',
                'secantCheckpoint', 'traceFile'):
        cfg.pop(key, None)
    cfg.update(modes=obj.M, spacing=4, shootingParts=a.parts,
               quadrature=a.quadrature, steps=a.steps)
    for key, value in rec['physical_port']['parameters'].items():
        if cfg.get(key) != value:
            raise ValueError('Physical tail parameter mismatch: ' + key)
    prior = read_tail_checkpoint(a.tail_initial)
    old = prior['parameters']
    if old['modes'] > obj.M or old['spacing'] != 4:
        raise ValueError('Tail refinement cannot discard modes or change spacing')
    if (old.get('physicalDepth', old.get('depth')) > cfg['depth'] or
            a.parts % old.get('shootingParts', 1)):
        raise ValueError('Tail refinement needs nested physical depth and parts')
    cfg['initialCheckpoint'] = str(a.tail_initial.resolve())
    cfg['traceFile'] = str(a.out.with_name(a.out.name + '-worker-trace.jsonl'))
    config = a.out.with_name(a.out.name + '-config.json')
    config.write_text(json.dumps(cfg, indent=2) + '\n')
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER'] = str(a.sparse_helper.resolve())
    os.environ['VISIBLE_FLEX_SPARSE_TRACE'] = str(
        a.out.with_name(a.out.name + '-linear-trace.jsonl'))
    client = module('n4_frozen_actual_original_client',
                    source / 'scripts/950f-tail-client-v3.py')
    stderr = a.out.with_name(a.out.name + '-worker-stderr.log').open('w')
    original_popen = subprocess.Popen
    def logged_popen(*args, **kwargs):
        kwargs['stderr'] = stderr
        return original_popen(*args, **kwargs)
    client.subprocess = SimpleNamespace(Popen=logged_popen, PIPE=subprocess.PIPE)
    summary = dict(
        scope=__doc__, command=sys.argv, solver_success=False,
        input_checkpoint_sha256=digest(a.checkpoint),
        input_tail_sha256=digest(a.tail_initial), script_sha256=digest(__file__),
        fixed_physical_profile=frozen, seed=seed['diagnostics'],
        original_coupler_sha256=digest(source / 'scripts/db6f-prefix-coupled.py'),
        sparse_helper_sha256=digest(a.sparse_helper),
        periodic_engine_sha256={f.name: digest(f) for f in
                                (source / 'scripts/periodic-quadrature').glob('*.mjs')},
        tail_initialization=dict(
            source_modes=old['modes'], target_modes=obj.M,
            source_parts=old.get('shootingParts'), target_parts=a.parts,
            source_depth=old.get('physicalDepth', old.get('depth')),
            target_depth=cfg['depth'],
            remesh_sha256=digest(source / 'scripts/950f-tail-warm-remesh.mjs'),
            scope='Original nested remesh and complete new-height correction; initialization only'))
    print(json.dumps(dict(event='frozen_seed_ready', modes=obj.M,
                          input_modes=rec['config']['modes'], nodes=len(x),
                          physical_profile=frozen,
                          identity={k: seed['diagnostics'][k] for k in
                                    ('complete_core_identity_error',
                                     'complete_map_projection_error',
                                     'input_mesh_nodes', 'seed_mesh_nodes',
                                     'input_mesh_coverage_max')})), flush=True)
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
        response = tail.solve(height, jacobian=False, audit=True)
        summary['initial_actual_tail'] = dict(
            converged=response['converged'], residual=response['residual'],
            tail_calls=tail.calls)
        print(json.dumps(dict(event='full_height_actual_warmup',
                              **summary['initial_actual_tail'])), flush=True)
        from f6curve_domain_newton import install, STATS
        from curve_stable_prefix_bvp import save_checkpoint
        install()
        sol, outer = coupler.solve_with_actual_tail(obj, tail, x, y, par, a)
        obj.initial(sol.p)
        flow = obj.flow(sol.p[0])
        if obj.cfg != frozen:
            raise ValueError('The frozen physical profile changed during refinement')
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
                         'core_kind': 'n4_fixed_local_circle',
                         'actual_nonlinear_tail': True, 'fixed_metric': True,
                         'tol': a.tol, 'bc_tol': a.bc_tol,
                         'physical_bc_tol': a.physical_bc_tol}
        if seed['core_projection_order'] is not None:
            out['core_projection_order'] = seed['core_projection_order']
        if sol.success:
            out['summary'] = seed['adaptive'].audit(obj, physical, max(512, obj.nt))
            out['summary']['scope'] = (
                'Sampled complete prefix metric and Cartesian Darboux tensor at '
                'the frozen true coupled metric; the original actual nonlinear '
                'DN and mean/nonmean two-jet audit are in tail_seam. No circle, '
                'closed family or arbitrary-epsilon theorem is asserted.')
            out['tail_seam'] = obj.seam_audit(physical)
            if out['max_bc'] > a.bc_tol or not out['tail_seam']['tail_converged']:
                raise FloatingPointError('Original actual terminal gate is not satisfied')
        out['seconds'] = time.monotonic() - started
        out['tail_calls'] = tail.calls
        save_checkpoint(a.out.with_suffix('.json.gz'), out)
        summary.update({k: v for k, v in out.items()
                        if k not in ('mesh', 'pp_coefficients', 'physical_port')})
        print(json.dumps(dict(event='result', success=out['solver_success'],
                              nodes=out['nodes'], rms=out['max_rms'],
                              actual_bc=out['max_bc'], actual_q=obj.support_amplitude,
                              tail_calls=tail.calls)), flush=True)
    except Exception as exc:
        summary.update(solver_success=False, error=repr(exc),
                       tail_calls=tail.calls if tail else 0)
        print(json.dumps(dict(event='failure', error=repr(exc))), flush=True)
    finally:
        if tail:
            summary['worker_returncode_before_close'] = tail.proc.poll()
            summary['tail_source_sha256'] = tail.sources
            tail.close()
            summary['worker_returncode_after_close'] = tail.proc.returncode
        stderr.close()
        summary['seconds'] = time.monotonic() - started
        a.out.with_name(a.out.name + '-summary.json').write_text(
            json.dumps(summary, indent=2) + '\n')


if __name__ == '__main__':
    main()
