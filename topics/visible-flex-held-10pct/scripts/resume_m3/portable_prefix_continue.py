#!/usr/bin/env python3
"""Portable finite m3 BVP continuation with original physical gates.

Inputs are actual source, physical profile, generated chart/port, and optional
raw checkpoint.  This deliberately does not require an old absolute-path
launch-plan chain.  Every solve saves its raw return before C2 export/audit.
Linear-port and true-tail results are labelled separately.  Numerical finite
acceptance never asserts closure, exact isometry, reach, or the 10% target.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import traceback
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


def install_rms_domain_guard():
    """Check the same two off-midpoint RHS samples used by original RMS.

    The collocation tuple, original Jacobian, merit function, and convergence
    tolerances stay unchanged. Domain-invalid Newton trials get rejected by
    the existing domain-aware Newton instead of escaping later in RMS.
    """
    import scipy.integrate._bvp as bvp
    original = bvp.prepare_sys
    def prepare(n,m,k,fun,bc,fun_jac,bc_jac,x,h):
        col, jac = original(n,m,k,fun,bc,fun_jac,bc_jac,x,h)
        def guarded(y,p):
            result = col(y,p)
            spline = bvp.create_spline(y,result[2],x,h)
            middle = x[:-1]+.5*h
            offset = .5*h*(3/7)**.5
            fun(middle+offset,spline(middle+offset),p)
            fun(middle-offset,spline(middle-offset),p)
            return result
        return guarded, jac
    bvp.prepare_sys = prepare


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'short-bridge', 'profile', 'chart', 'port', 'outdir'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--tail-config', type=Path)
    p.add_argument('--raw-restart', type=Path)
    p.add_argument('--restart-checkpoint', type=Path)
    p.add_argument('--control-record', type=Path)
    p.add_argument('--core-module', type=Path)
    p.add_argument('--core-config', type=Path)
    p.add_argument('--amplitude', type=float, default=.06)
    p.add_argument('--warp-reference', type=float, default=.06)
    p.add_argument('--modes', type=int, default=8)
    p.add_argument('--angular', type=int, default=256)
    p.add_argument('--audit-angular', type=int, default=512)
    p.add_argument('--nodes', type=int, default=401)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--tol', type=float, default=1e-6)
    p.add_argument('--bc-tol', type=float, default=1e-7)
    p.add_argument('--physical-bc-tol', type=float, default=2e-9)
    p.add_argument('--probe-only', action='store_true')
    p.add_argument('--skip-audit', action='store_true')
    p.add_argument('--verbose', type=int, default=2)
    p.add_argument('--tail-warmup', type=float, nargs='*', default=[])
    a = p.parse_args()
    a.outdir.mkdir(parents=True, exist_ok=False)
    cfg = json.loads(a.profile.read_text())
    chart = json.loads(a.chart.read_text())
    port = json.loads(a.port.read_text())
    port['cut']['_prefix_bridge'] = cfg['prefix_bridge']
    port['_sha256'] = sha(a.port)
    scripts = a.source_topic / 'scripts'
    c = module('portable_m3_coupler', scripts / 'db6f-prefix-coupled.py')
    module('portable_m3_flat', scripts / 'db6f-prefix-flat-profile.py').install(c.adaptive)
    c.adaptive.old.install_source(a.source_topic / 'repro/source-root')
    module('portable_m3_short', a.short_bridge).install()
    module('portable_m3_fourier_jac', scripts / '78718-prefix-fourier-jacobian.py').install(c.adaptive)
    core_settings = None
    if a.core_module:
        core_settings = json.loads(a.core_config.read_text()) if a.core_config else {}
        core = module('portable_m3_custom_core', a.core_module)
        factory = core.make_factory(core_settings)
        __import__('fixed_metric_mode3_core').PlanarSupportCore = factory
        __import__('fixed_metric_mode3_bvp').PlanarSupportCore = factory
    Flow, Base = c.adaptive.build_classes(chart)
    if a.core_module:
        lib = Path(__file__).with_name('round_raw_lib')
        sys.path.insert(0, str(lib))
        from exact_core_lift import install_core_lift
        Base = install_core_lift(Flow, Base)
        if hasattr(factory,'jet_parameter_derivatives'):
            import analytic_adaptive_core_jac as analytic
            analytic.parameter_jets = lambda core,theta: core.jet_parameter_derivatives(theta)
            analytic.install(Base)
    BVP = type('PortableBVP', (c.TailMixin, Base), {}) if a.tail_config else Base
    o = BVP(cfg, port, a.amplitude, a.modes, a.angular, False, a.warp_reference)
    o.bcweights = np.full(o.M, a.physical_bc_tol / a.bc_tol)
    tail = None
    begin = time.monotonic()
    rec = dict(scope=__doc__, command=[sys.executable, *sys.argv],
               source_hashes={str(x.resolve()): sha(x) for x in
                              [Path(__file__), a.short_bridge, scripts/'db6f-prefix-coupled.py',
                               scripts/'950f-prefix-adaptive-chart-bvp-v2.py',
                               scripts/'78718-prefix-fourier-jacobian.py']},
               inputs={str(x.resolve()): sha(x) for x in
                       [a.profile, a.chart, a.port, *([a.control_record] if a.control_record else []),
                        *([a.raw_restart] if a.raw_restart else []),
                        *([a.restart_checkpoint] if a.restart_checkpoint else []),
                        *([a.tail_config] if a.tail_config else []),
                        *([a.core_module] if a.core_module else []),
                        *([a.core_config] if a.core_config else [])]},
               physical_profile=cfg, physical_tail_parameters=port['parameters'],
               physical_tail_cut=port['cut'], angular_chart=chart,
               gauge_q=a.amplitude, warp_reference=a.warp_reference,
               modes=o.M, angular=o.nt, core_settings=core_settings,
               parameter_scales=o.pscale.tolist(), fixed_metric_refinement=False,
               actual_tail_requested=bool(a.tail_config), solver_success=False,
               gates=dict(tol=a.tol, bc_tol=a.bc_tol, physical_bc_tol=a.physical_bc_tol,
                          max_nodes=a.max_nodes, original_outer_budget=8))
    dump(a.outdir/'run.json', rec)
    def event(name, **fields):
        row = dict(event=name, elapsed=time.monotonic()-begin, **fields)
        with (a.outdir/'events.jsonl').open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False) + '\n')
        print(json.dumps(row, allow_nan=False), flush=True)
    def save_raw(sol, index):
        file = a.outdir/f'inner-{index:02d}.npz'
        np.savez_compressed(file, x=sol.x, y=sol.y, p=sol.p, cubic_c=sol.sol.c,
                            cubic_x=sol.sol.x, rms=sol.rms_residuals, pscale=o.pscale)
        o.initial(sol.p)
        core_summary = o._core.summary()
        row = dict(file=file.name, sha256=sha(file), success=bool(sol.success),
                   status=int(sol.status), message=sol.message, nodes=len(sol.x),
                   rms=float(np.max(sol.rms_residuals)), parameters=sol.p.tolist(),
                   legacy_input_controls=(sol.p[1:]*o.pscale).tolist(),
                   actual_core_corrections=list(o._core.corrections),
                   actual_core_control_meaning=core_summary.get('correction_meaning','normal-angle support coefficients'),
                   core_summary=core_summary,
                   candidate_H=(o.bridge.sigma*o.q*sol.y[o.iz:,-1]).tolist())
        dump(a.outdir/f'inner-{index:02d}.json', row)
        event('inner_return', **row)
        return row
    try:
        if a.raw_restart and a.restart_checkpoint:
            raise ValueError('Choose one restart representation')
        if a.restart_checkpoint:
            if a.core_module:
                raise ValueError('Legacy support continuation requires original support core')
            o.restart_remesh=a.nodes
            x,y,par=o.restart(a.restart_checkpoint)
            rec['restart_scope']='Original support-family physical-angle pullback and published amplitude initial-guess scaling; subsequent equations and gates unchanged.'
        elif a.raw_restart:
            r = np.load(a.raw_restart)
            x, y, par = r['x'].copy(), r['y'].copy(), r['p'].copy()
            if y.shape != (o.n, len(x)) or par.shape != (o.M,):
                raise ValueError('Raw restart dimension mismatch')
            if not np.array_equal(r['pscale'], o.pscale):
                raise ValueError('Raw restart parameter scales differ')
            o.initial(par)
        else:
            x, y, par = o.seed(a.nodes)
            if a.control_record:
                b = json.loads(a.control_record.read_text())
                controls = np.asarray(b['full_actual_controls'])
                par[1:] = controls[:o.M-1] / o.pscale
                # The supplied physical profile already contains historical p0.
                par[0] = 0.
                f = o.flow(0.)
                s, _ = o.chart(x, 0.)
                correction = o.initial(par)-y[:,0]
                cutoff = (f.Tu if f.direction=='outward' else f.Td)/2
                y += correction[:,None] * np.maximum(0,1-s/cutoff)[None,:]**3
        rhs = o.fun(x,y,par)
        event('initial_domain_pass', nodes=len(x), max_rhs=float(abs(rhs).max()),
              p=par.tolist(), inlet=o._inlet_metrics)
        if a.probe_only:
            rec['probe_passed'] = True
            return
        from f6curve_domain_newton import install, STATS
        install()
        install_rms_domain_guard()
        domain_errors={}
        original_fun=o.fun
        def traced_fun(t,y,p):
            try:
                return original_fun(t,y,p)
            except FloatingPointError as exc:
                name=str(exc).split(':')[0]
                count=domain_errors.get(name,0)+1
                domain_errors[name]=count
                if count<=3 or count & (count-1)==0:
                    event('domain_rejection',kind=name,count=count,error=str(exc),parameters=p.tolist())
                raise
        o.fun=traced_fun
        options = dict(tol=a.tol, bc_tol=a.bc_tol, max_nodes=a.max_nodes,
                       fun_jac=o.fun_jac, bc_jac=o.bc_jac,verbose=a.verbose)
        history = []
        if a.tail_config:
            tail = c.client.WeightedTailPort(a.tail_config,
                    a.source_topic/'repro/source-root', a.outdir/'tail',node_heap=2048)
            o.tail = tail
            H = o.bridge.sigma*o.q*y[o.iz:,-1]
            for factor in a.tail_warmup:
                r = tail.solve(H*factor**np.arange(1,o.M+1),jacobian=False,audit=True)
                event('tail_warmup',factor=factor,residual=r['residual'])
            response = tail.solve(H,jacobian=True,audit=True)
            for outer in range(8):
                o.tail = c.AffineTailForInnerBVP(H,response,o.M)
                try:
                    sol = solve_bvp(o.fun,o.bc,x,y,par,**options)
                finally:
                    o.tail = tail
                rec['raw_return'] = save_raw(sol,outer)
                if not sol.success: break
                candidate = o.bridge.sigma*o.q*sol.y[o.iz:,-1]
                actual = tail.solve(candidate,jacobian=True,audit=True)
                defect = float(abs(o.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max())
                row = dict(outer=outer, actual_bc=defect, actual_tail=actual['residual'])
                history.append(row)
                event('actual_outer',**row)
                if defect <= a.bc_tol: break
                x,y,par,H,response = sol.x,sol.y,sol.p,candidate,actual
            else:
                raise FloatingPointError('Original 8-outer actual boundary gate failed')
        else:
            sol = solve_bvp(o.fun,o.bc,x,y,par,**options)
            rec['raw_return'] = save_raw(sol,0)
        rec.update(solver_success=bool(sol.success), actual_outer_checks=history,
                   domain_newton_stats=dict(STATS),
                   domain_error_counts=domain_errors,
                   frozen_profile={**cfg,'delta':cfg['delta']+float(sol.p[0])})
        dump(a.outdir/'run.json',rec)
        if not sol.success or a.skip_audit: return
        o.initial(sol.p); f = o.flow(sol.p[0])
        physical = SimpleNamespace(x=o.chart(sol.x,sol.p[0])[0], y=sol.y, p=sol.p)
        physical.sol = f.c2_interpolant(physical)
        np.savez_compressed(a.outdir/'physical.npz',x=physical.x,c=physical.sol.c,p=sol.p)
        rec['physical_sha256'] = sha(a.outdir/'physical.npz')
        rec['prefix_audit'] = c.adaptive.audit(o,physical,a.audit_angular)
        if not a.core_module:
            from curve_stable_prefix_bvp import save_checkpoint
            checkpoint=dict(angular_chart='frozen-spline-adaptive-v1',chart=chart,
                config=dict(modes=o.M,base_mode=3,core_kind='adaptive_warped_support'),
                frozen_profile=rec['frozen_profile'],gauge_amplitude=o.q,
                actual_primary_amplitude=o.support_amplitude,warp_reference_q=a.warp_reference,
                physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],
                parameters=sol.p.tolist(),central_correction_scales=o.pscale.tolist(),
                mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,
                solver_success=bool(sol.success),summary=rec['prefix_audit'],
                scope='Numerical finite-prefix checkpoint; actual-tail status is recorded in run.json.')
            save_checkpoint(a.outdir/'checkpoint.json.gz',checkpoint)
            rec['checkpoint_sha256']=sha(a.outdir/'checkpoint.json.gz')
        dump(a.outdir/'run.json',rec)
        event('prefix_audit',metric=rec['prefix_audit']['metric_l1'],
              darboux=rec['prefix_audit']['darboux_l1'])
        if tail:
            rec['tail_seam'] = o.seam_audit(physical)
    except Exception as exc:
        rec['error'] = repr(exc)
        rec['traceback'] = traceback.format_exc()
        event('error',error=repr(exc))
    finally:
        if tail:
            tail.close()
            rec['tail_calls'] = tail.calls
        rec['seconds'] = time.monotonic()-begin
        dump(a.outdir/'run.json',rec)


if __name__ == '__main__':
    main()
