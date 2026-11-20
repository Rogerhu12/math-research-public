#!/usr/bin/env python3
"""Original n4 Frenet BVP with a new exact material-curvature circle core.

This is a physical design solve: q is fixed, delta and vd are unknown, and
the remaining M-2 parameters are material-curvature controls.  The first
control slot is identically zero and serves only as the vd coordinate.
An identity material-angle chart avoids normal-angle inversion.  The full
integral core is retained in the reference lift.  Only the perturbation is
Fourier represented; a linear tail, finite solve or exact inlet circle does
not assert a closed isometric family or a fixed-parameter refinement.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'loader', 'core-source', 'definition', 'port', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--q', type=float, default=.01)
    p.add_argument('--modes', type=int, default=12)
    p.add_argument('--halfwidth', type=float, default=.2)
    p.add_argument('--transition', type=float, default=.25)
    p.add_argument('--angular', type=int, default=512)
    p.add_argument('--nodes', type=int, default=301)
    p.add_argument('--max-nodes', type=int, default=3000)
    p.add_argument('--tol', type=float, default=1e-7)
    p.add_argument('--restart', type=Path)
    p.add_argument('--check-only', action='store_true')
    a = p.parse_args()
    if a.modes < 3:
        raise ValueError('Two design coordinates and at least one core control are required')
    source = a.source_topic.resolve()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    if a.out.with_suffix('.json').exists() or a.out.with_suffix('.json.gz').exists():
        raise FileExistsError('Use a fresh output prefix')
    sys.path.insert(0, str(a.loader.resolve()))
    sys.path[:0] = [str(source/'notes'), str(source/'repro/source-root/topics/large-amplitude-twist-flex/scripts')]
    material = module('held10_material_curvature_n4', a.core_source.resolve())
    settings = dict(halfwidth=a.halfwidth, transition=a.transition)

    class Core(material.MaterialCurvatureCore):
        def __init__(self, q, corrections=(), base_mode=4):
            physical = np.array(corrections, float)
            if len(physical):
                physical[0] = 0.
            super().__init__(q, physical, base_mode, **settings)
        def parameter_derivatives(self, theta):
            ans = super().parameter_derivatives(theta).copy()
            if len(ans) > 1:
                ans[1] = 0.
            return ans
        def jet_parameter_derivatives(self, theta):
            ans = tuple(x.copy() for x in super().jet_parameter_derivatives(theta))
            for x in ans:
                if len(x) > 1:
                    x[1] = 0.
            return ans

    from bimodal_chart_loader import load
    ad = load(source, 4, 0.)
    module('held10_material_n4_bridge', source.parent/'visible-flex-larger-amplitude/computations/root_short_bridge.py').install()
    coremod = __import__('fixed_metric_mode3_core')
    coremod.PlanarSupportCore = Core
    module('held10_material_n4_fourier', source/'scripts/78718-prefix-fourier-jacobian.py').install(ad)
    Flow, BVP = ad.build_classes(dict(knots=[0.,1.], values=[1.,1.], final_derivative=0.))
    from exact_core_lift import install_core_lift
    BVP = install_core_lift(Flow, BVP)
    import analytic_adaptive_core_jac as analytic
    analytic.parameter_jets = lambda core, theta: core.jet_parameter_derivatives(theta)
    analytic.install(BVP)
    from dual_design_bvp import install as dual_install
    BVP = dual_install(Flow, BVP, 0.)
    definition = json.loads(a.definition.read_text())
    cfg = dict(definition['fixed_physical_profile'])
    port = json.loads(a.port.read_text())
    port['cut']['_prefix_bridge'] = cfg['prefix_bridge']
    from curve_stable_prefix_bvp import load_checkpoint, save_checkpoint
    from fixed_metric_mode3_bvp import merge_profile_mesh
    obj = BVP(cfg, port, a.q, a.modes, a.angular, False, 0.)
    obj.pscale = np.full(a.modes-1, a.q)
    obj.bcweights = np.full(a.modes, .01)
    par = np.zeros(a.modes)
    if a.restart:
        old = load_checkpoint(a.restart)
        if old['config']['core_kind'] != 'material_curvature_integral_n4' or old['core_settings'] != settings:
            raise ValueError('Restart must use this exact material core family/settings')
        if old['physical_port']['parameters'] != port['parameters']:
            raise ValueError('Physical tail changed in material continuation')
        M0 = old['config']['modes']
        if M0 > a.modes:
            raise ValueError('Do not discard old modes')
        par[:2] = [old['physical_profile']['delta']-cfg['delta'], old['physical_profile']['vd']-cfg['vd']]
        oldc = np.asarray(old['parameters'][2:]) * np.asarray(old['central_correction_scales'][1:])
        par[2:M0] = oldc/a.q*(a.q/old['gauge_amplitude'])
    obj.initial(par)
    f = obj.flow(par[0])
    x = merge_profile_mesh(np.linspace(0, 1, a.nodes), obj.chart_breaks)
    s, _ = obj.chart(x, par[0])
    N = max(2048, 64*a.modes)
    B = f.basis(N)[0]
    if a.restart:
        pp = PPoly.construct_fast(np.asarray(old['pp_coefficients']), np.asarray(old['mesh']), extrapolate=True, axis=1)
        oldy = pp(s/f.end*old['meridian_length'])
        y = np.zeros((obj.n, len(x)))
        factor = old['gauge_amplitude']/a.q
        y[0] = factor*oldy[0]
        for j in range(M0):
            for ni, oi in ((1+j,1+j),(a.modes+1+j,M0+1+j),(2*a.modes+1+j,2*M0+1+j)):
                y[ni] = factor*oldy[oi]
        # The integral lift is new with q. This only constructs a fresh
        # initial guess; all new residuals and parameter changes are solved.
        initialization = 'old physical perturbation plus new exact inlet repair; new design, not identity'
    else:
        theta = 2*np.pi*np.arange(N)/N
        g0 = obj._core.evaluate(theta)
        er0 = np.c_[np.cos(theta), np.sin(theta), np.zeros(N)]
        radial = np.sum((g0['F']-er0)*er0, axis=1)
        amplitudes = [float(2*np.mean(radial*np.cos(4*(j+1)*theta))) for j in range(2)]
        lines = []
        for j in range(2):
            line = f.backward_line(j)
            fg = np.empty((2,len(s)))
            for k,(lo,hi,sol,scale) in enumerate(line.segments):
                mask=(s>=lo)&((s<hi) if k+1<len(line.segments) else (s<=hi))
                if np.any(mask):
                    fg[:,mask]=sol(s[mask])*np.exp(scale-line.logscale)/line.core[0]
            lines.append(fg)
        y = np.empty((obj.n,len(s)))
        for first in range(0,len(s),32):
            sl=slice(first,first+32)
            g=f.geo(s[sl],N);theta=g['theta']
            er=np.stack((np.cos(theta),np.sin(theta),np.zeros_like(theta)),axis=-1)
            et=np.stack((-np.sin(theta),np.cos(theta),np.zeros_like(theta)),axis=-1)
            field=np.zeros_like(er)
            for j,(amplitude,fg) in enumerate(zip(amplitudes,lines)):
                mode=4*(j+1)
                field+=amplitude/a.q*fg[0,sl,None,None]*(np.cos(mode*theta)[:,:,None]*er-np.sin(mode*theta)[:,:,None]*et/mode)
                field[:,:,2]+=amplitude/a.q*fg[1,sl,None]*np.cos(mode*theta)
            field-=(g['pos']-f.profile(s[sl])[0][:,None,None]*er)/a.q
            y[:,sl]=f.project(field,B)
        initialization = dict(method='two true radial core Fourier coefficients, original physical backward lines', amplitudes=amplitudes)
    u=np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end),0.,1.)
    taper=f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    y+=(obj.initial(par)-y[:,0])[:,None]*taper[None,:]
    row=dict(scope=__doc__, command=sys.argv, script_sha256=sha(__file__), core_source_sha256=sha(a.core_source),
             definition_sha256=sha(a.definition), physical_port_sha256=sha(a.port), q=a.q, modes=a.modes,
             settings=settings, reference_profile=cfg, initialization=initialization,
             initial_core=obj._core.summary(), parameters=par.tolist(), status='seed', success=False)
    summary=a.out.with_suffix('.json')
    def persist():
        tmp=summary.with_suffix('.json.tmp');tmp.write_text(json.dumps(row,indent=2)+'\n');tmp.replace(summary)
    persist()
    begin=time.monotonic()
    try:
        rhs=obj.fun(x,y,par)
        row.update(initial_bc=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()), initial_rhs_max=float(abs(rhs).max()))
        print(json.dumps(dict(event='material_seed',q=a.q,modes=a.modes,nodes=len(x),initial_bc=row['initial_bc'],initial_rhs_max=row['initial_rhs_max'],core=row['initial_core'])),flush=True)
        persist()
        if a.check_only:
            return
        from f6curve_domain_newton import install, STATS
        from trace_domain_newton import install as observe
        install();observe(a.out.with_name(a.out.name+'-newton.jsonl'))
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=1e-8,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        np.savez(a.out.with_name(a.out.name+'-raw.npz'),x=sol.x,y=sol.y,p=sol.p,c=sol.sol.c,rms_residuals=sol.rms_residuals)
        row.update(status='inner_returned',success=bool(sol.success),nodes=len(sol.x),max_rms=float(sol.rms_residuals.max()),parameters=sol.p.tolist(),message=sol.message,domain_newton=dict(STATS),seconds=time.monotonic()-begin)
        persist();print(json.dumps(dict(event='material_inner',success=row['success'],nodes=row['nodes'],max_rms=row['max_rms'],seconds=row['seconds'])),flush=True)
        obj.initial(sol.p);f=obj.flow(sol.p[0])
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=f.c2_interpolant(physical)
        frozen={**cfg,'delta':cfg['delta']+float(sol.p[0]),'vd':cfg['vd']+float(sol.p[1])}
        saved=dict(config=dict(modes=a.modes,base_mode=4,core_kind='material_curvature_integral_n4',angular=a.angular),
                   fixed_metric=False,solver_success=bool(sol.success),angular_chart='identity',core_settings=settings,
                   profile=cfg,physical_profile=frozen,physical_port=port,physical_port_sha256=sha(a.port),
                   gauge_amplitude=a.q,parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),
                   mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,meridian_length=f.end,core_summary=obj._core.summary())
        save_checkpoint(a.out.with_suffix('.json.gz'),saved)
        row.update(physical_profile=frozen,checkpoint_sha256=sha(a.out.with_suffix('.json.gz')),core=obj._core.summary())
        if sol.success:
            row['summary']=ad.audit(obj,physical,512)
        row.update(status='completed',seconds=time.monotonic()-begin)
    except Exception as exc:
        row.update(status='exception',error=repr(exc),seconds=time.monotonic()-begin)
        persist();print(json.dumps(dict(event='material_exception',error=repr(exc))),flush=True)
        raise
    persist();print(json.dumps(dict(event='material_terminal',success=row['success'],metric=row.get('summary',{}).get('metric_l1'),seconds=row['seconds'])),flush=True)


if __name__=='__main__':
    main()
