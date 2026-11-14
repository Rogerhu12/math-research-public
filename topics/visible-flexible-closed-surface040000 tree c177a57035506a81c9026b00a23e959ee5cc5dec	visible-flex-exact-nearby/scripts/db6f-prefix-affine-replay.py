#!/usr/bin/env python3
"""Tighten only prefix collocation with a frozen, previously solved DN/Jacobian.

This is a causal numerical diagnostic, NOT a new actual nonlinear coupled
solution. The physical metric, chart, Fourier order and angular quadrature
are unchanged. A subsequent original-DN correction is mandatory before
the output can be called a coupled solution.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', type=Path, required=True)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--linear-port', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--tol', type=float, default=1e-11)
    p.add_argument('--max-nodes', type=int, default=14000)
    a = p.parse_args()
    begin = time.monotonic()
    runner = module('affine_replay_runner', HERE/'db6f-prefix-flat-coupled.py').m
    runner.adaptive.old.install_source(a.source_root)
    from curve_stable_prefix_bvp import load_checkpoint, save_checkpoint
    from f6curve_domain_newton import install, STATS
    rec = load_checkpoint(a.checkpoint)
    assert rec['solver_success'] and rec['config']['actual_nonlinear_tail']
    tailpath = a.checkpoint.parent/rec['tail_seam']['tail_record']
    actual = json.load(gzip.open(tailpath, 'rt'))
    assert actual['response']['converged']
    assert actual['response']['heightJetJacobian'] is not None
    port = json.loads(a.linear_port.read_text())
    port['_sha256'] = hashlib.sha256(a.linear_port.read_bytes()).hexdigest()
    _, Base = runner.adaptive.build_classes(rec['chart'])
    class BVP(runner.TailMixin, Base):
        pass
    cfg = rec['config']
    obj = BVP(rec['frozen_profile'], port, rec['gauge_amplitude'],
              cfg['modes'], cfg['angular'], True, rec['warp_reference_q'])
    obj.bcweights = np.full(obj.M, cfg['physical_bc_tol']/cfg['bc_tol'])
    initializer = module('affine_replay_initializer', HERE/'db6f-prefix-preserve-restart.py')
    x, y, par, restart = initializer.restart(obj, a.checkpoint, rec['chart'])
    obj.tail = runner.AffineTailForInnerBVP(actual['request']['height'],
                                         actual['response'], obj.M)
    startheight = obj.bridge.sigma*obj.q*y[obj.iz:, -1]
    initial_error = float(np.max(abs(obj.bc(y[:, 0], y[:, -1], par))))
    manifest = dict(scope=__doc__, checkpoint=str(a.checkpoint),
                    checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
                    frozen_actual_tail=str(tailpath),
                    frozen_actual_tail_sha256=hashlib.sha256(tailpath.read_bytes()).hexdigest(),
                    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    modes=obj.M, angular=obj.nt, tolerance=a.tol,
                    maximum_nodes=a.max_nodes, initial_nodes=len(x),
                    initial_affine_boundary_residual=initial_error,
                    actual_nonlinear_tail=False, restart=restart)
    a.out_prefix.with_name(a.out_prefix.name+'-reproduction.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(dict(event='start_affine_diagnostic', modes=obj.M,
                          angular=obj.nt, nodes=len(x), tol=a.tol,
                          original_bc=initial_error)), flush=True)
    install()
    try:
        sol = solve_bvp(obj.fun, obj.bc, x, y, par, tol=a.tol,
                        bc_tol=cfg['bc_tol'], max_nodes=a.max_nodes,
                        fun_jac=obj.fun_jac, bc_jac=obj.bc_jac, verbose=2)
        flow = obj.flow(sol.p[0]); obj.initial(sol.p)
        physical = SimpleNamespace(x=obj.chart(sol.x, sol.p[0])[0],
                                    y=sol.y, p=sol.p)
        physical.sol = flow.c2_interpolant(physical)
        out = {k:rec[k] for k in ('angular_chart', 'chart', 'warp_reference_q',
                                  'frozen_profile', 'gauge_amplitude',
                                  'physical_port_sha256', 'physical_tail_parameters',
                                  'physical_tail_cut', 'tail_config')}
        out.update(scope=__doc__, config=dict(cfg, tol=a.tol,
                    actual_nonlinear_tail=False, frozen_affine_dn=True),
                   actual_primary_amplitude=obj.support_amplitude,
                   meridian_length=flow.end, parameters=sol.p.tolist(),
                   central_correction_scales=obj.pscale.tolist(), nodes=len(sol.x),
                   solver_success=bool(sol.success), message=sol.message,
                   max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
                   newton_domain_audit=dict(STATS), mesh=physical.x.tolist(),
                   pp_coefficients=physical.sol.c, restart_mesh_diagnostics=restart,
                   frozen_actual_tail=manifest['frozen_actual_tail'],
                   frozen_actual_tail_sha256=manifest['frozen_actual_tail_sha256'])
        save_checkpoint(a.out_prefix.with_suffix('.json.gz'), out)
        out['summary'] = runner.adaptive.audit(obj, physical, max(1024, 64*obj.M))
        out['summary']['scope'] = __doc__
        out['frozen_dn_height_change_linf'] = float(np.max(abs(
            obj.bridge.sigma*obj.q*physical.y[obj.iz:, -1]-startheight)))
        out['seconds'] = time.monotonic()-begin
        save_checkpoint(a.out_prefix.with_suffix('.json.gz'), out)
        summary = {k:v for k,v in out.items() if k not in ('mesh', 'pp_coefficients')}
        manifest.update(success=bool(sol.success), nodes=len(sol.x),
                        metric=out['summary']['metric_l1'],
                        actual_amplitude=obj.support_amplitude,
                        max_rms=out['max_rms_collocation_residual'],
                        cut_height_change=out['frozen_dn_height_change_linf'])
        print(json.dumps(dict(event='result_affine_diagnostic', **{
            k:manifest[k] for k in ('success', 'nodes', 'metric', 'max_rms',
                                    'actual_amplitude', 'cut_height_change')})), flush=True)
    except Exception as e:
        manifest.update(success=False, error=repr(e))
        summary = dict(manifest)
        print(json.dumps(dict(event='failure_affine_diagnostic', error=repr(e))), flush=True)
    manifest['seconds'] = time.monotonic()-begin
    a.out_prefix.with_name(a.out_prefix.name+'-reproduction.json').write_text(json.dumps(manifest, indent=2)+'\n')
    a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary, indent=2)+'\n')


if __name__ == '__main__':
    main()
