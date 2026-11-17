#!/usr/bin/env python3
"""Join the recorded n4 two-parameter prefix to the original nonlinear tail.

The existing n4 core, angular chart, Frenet residual, parameter guards and
analytic state Jacobian remain in the loaded prefix object.  The original
TailMixin supplies the full physical terminal height response.  This is a
new finite physical design, not a fixed-metric refinement or closed family.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
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


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('prefix-loader-dir', 'source-topic', 'tail-source',
                'sparse-helper', 'checkpoint', 'config', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--tail-initial', type=Path)
    p.add_argument('--quadrature', type=int, default=256)
    p.add_argument('--steps', type=int, default=16)
    p.add_argument('--parts', type=int, default=8)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--tol', type=float, default=3e-7)
    p.add_argument('--bc-tol', type=float, default=1e-8)
    p.add_argument('--physical-bc-tol', type=float, default=1e-10)
    p.add_argument('--scales', type=float, nargs='+', default=[.2, .5, 1.])
    p.add_argument('--node-heap', type=int, default=2304)
    p.add_argument('--lagged-tail', action='store_true', default=True)
    a = p.parse_args()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(a.prefix_loader_dir.resolve()))
    from diagnose_bimodal_chart import load
    rec, obj, flow, par, mesh, pp = load(a)
    if not rec['solver_success'] or rec['config']['base_mode'] != 4:
        raise ValueError('A genuinely accepted n4 prefix is required')
    if a.quadrature <= 16 * obj.M or a.quadrature & (a.quadrature - 1):
        raise ValueError('Original tail requires power-of-two N > 4*M*spacing')
    adaptive = sys.modules['even_mode_adaptive']
    source = a.tail_source.resolve()
    coupler = module('n4_actual_original_coupler',
                     source / 'scripts/db6f-prefix-coupled.py')
    # A mixin changes only the terminal DN.  No prefix restart guard or
    # physical residual is edited to disguise an incompatible initial field.
    original_type = type(obj)
    obj.__class__ = type('N4ActualTailBVP',
                         (coupler.TailMixin, original_type), {})
    obj.bcweights = np.full(obj.M, a.physical_bc_tol / a.bc_tol)
    x = obj.inverse_chart(mesh, par[0])
    y = pp(mesh)
    cfg = json.loads(a.config.read_text())
    for key in ('initialCheckpoint', 'designInitialCheckpoint',
                'secantCheckpoint', 'traceFile'):
        cfg.pop(key, None)
    cfg.update(modes=obj.M, spacing=4, shootingParts=a.parts,
               quadrature=a.quadrature, steps=a.steps)
    for key, value in rec['physical_port']['parameters'].items():
        if cfg.get(key) != value:
            raise ValueError('Physical tail parameter mismatch: ' + key)
    if a.tail_initial:
        cfg['initialCheckpoint'] = str(a.tail_initial.resolve())
    cfg['traceFile'] = str(a.out.with_name(a.out.name + '-worker-trace.jsonl'))
    config = a.out.with_name(a.out.name + '-config.json')
    config.write_text(json.dumps(cfg, indent=2) + '\n')
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER'] = str(a.sparse_helper.resolve())
    os.environ['VISIBLE_FLEX_SPARSE_TRACE'] = str(
        a.out.with_name(a.out.name + '-linear-trace.jsonl'))
    client = module('n4_actual_original_client',
                    source / 'scripts/950f-tail-client-v3.py')
    stderr_path = a.out.with_name(a.out.name + '-worker-stderr.log')
    stderr = stderr_path.open('w')
    original_popen = subprocess.Popen
    def logged_popen(*args, **kwargs):
        kwargs['stderr'] = stderr
        return original_popen(*args, **kwargs)
    client.subprocess = SimpleNamespace(Popen=logged_popen, PIPE=subprocess.PIPE)
    summary = dict(scope=__doc__, command=sys.argv, solver_success=False,
                   input_checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   prefix_loader_sha256=hashlib.sha256(
                       (a.prefix_loader_dir / 'diagnose_bimodal_chart.py').read_bytes()).hexdigest(),
                   prefix_replay_sources={name: hashlib.sha256(
                       (a.prefix_loader_dir / name).read_bytes()).hexdigest()
                       for name in ('diagnose_bimodal_chart.py', 'run_bimodal_chart.py',
                                    'bimodal_chart_loader.py', 'dual_design_bvp.py',
                                    'large_radius_local_core.py', 'local_flatten_core.py',
                                    'exact_core_lift.py', 'analytic_adaptive_core_jac.py',
                                    'plateau_core.py')},
                   warmup_path='Uniform scaling of the complete actual H; initialization only.',
                   warmup=[])
    tail = None
    started = time.monotonic()
    try:
        tail = client.WeightedTailPort(
            config, source / 'repro/source-root',
            a.out.with_name(a.out.name + '-tail'), node_heap=a.node_heap)
        obj.tail = tail
        summary['linear_dn_difference'] = float(abs(
            tail.linearD - np.asarray(rec['physical_port']['linearSlope'][:obj.M])).max())
        H = obj.bridge.sigma * obj.q * y[obj.iz:, -1]
        print(json.dumps(dict(event='ready', q=obj.q, modes=obj.M,
                              first_height=float(H[0]), second_height=float(H[1]),
                              linear_dn_difference=summary['linear_dn_difference'])), flush=True)
        for scale in a.scales:
            response = tail.solve(H * scale, jacobian=False, audit=True)
            row = dict(scale=scale, residual=response['residual'],
                       converged=response['converged'], tail_calls=tail.calls)
            summary['warmup'].append(row)
            print(json.dumps(dict(event='warmup', **row)), flush=True)
        from f6curve_domain_newton import install, STATS
        from curve_stable_prefix_bvp import save_checkpoint
        install()
        sol, outer = coupler.solve_with_actual_tail(obj, tail, x, y, par, a)
        obj.initial(sol.p)
        flow = obj.flow(sol.p[0])
        physical = SimpleNamespace(
            x=obj.chart(sol.x, sol.p[0])[0], y=sol.y, p=sol.p)
        physical.sol = flow.c2_interpolant(physical)
        frozen = {**rec['profile'],
                  'delta': rec['profile']['delta'] + float(sol.p[0]),
                  'vd': rec['profile']['vd'] + float(sol.p[1])}
        out = {**rec, 'scope': __doc__, 'profile': rec['profile'],
               'physical_profile': frozen, 'frozen_profile': frozen,
               'tail_config': cfg, 'parameters': sol.p.tolist(),
               'solver_success': bool(sol.success), 'message': sol.message,
               'nodes': len(sol.x), 'mesh': physical.x.tolist(),
               'pp_coefficients': physical.sol.c, 'meridian_length': flow.end,
               'actual_outer_checks': outer,
               'max_rms': float(np.max(sol.rms_residuals)),
               'max_bc': float(np.max(abs(obj.bc(sol.y[:, 0], sol.y[:, -1], sol.p)))),
               'domain_newton': dict(STATS)}
        out['config'] = {**rec['config'], 'actual_nonlinear_tail': True,
                         'fixed_metric': False, 'tol': a.tol,
                         'bc_tol': a.bc_tol, 'physical_bc_tol': a.physical_bc_tol}
        if sol.success:
            out['summary'] = adaptive.audit(obj, physical, max(512, obj.nt))
            out['summary']['scope'] = (
                'Sampled physical prefix metric and Cartesian Darboux tensor. '
                'The terminal condition uses the original actual nonlinear DN; '
                'its mean and nonmean two-jet audit is in tail_seam. '
                'Full Cartesian closure, continuous metric bounds, and the '
                'closed-surface requirements remain separate.')
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
                              actual_bc=out['max_bc'], tail_calls=tail.calls)), flush=True)
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
