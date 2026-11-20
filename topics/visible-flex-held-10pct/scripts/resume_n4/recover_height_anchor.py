#!/usr/bin/env python3
"""Regenerate an initial field using two historically observed cut heights.

The original compact record retains H4 and H8 but not the whole prefix field.
This recovery-only BVP replaces the first two linear DN equations by those
tail-oriented physical heights H = bridge.sigma*q*y_z. Remaining modes use
the original linear DN. Its numerical
success is neither the original nonlinear-tail acceptance nor a closed family.
The regenerated field must subsequently solve every original nonlinear DN
condition. All physical profile/core definitions and Frenet gates are retained.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace, MethodType
import numpy as np
from scipy.integrate import solve_bvp
from recover_compact_anchor import build_model, initial_two_mode_field, digest


def install_height_boundary(obj, heights):
    """Replace only two declared equations, with their exact derivatives."""
    original_terminal = obj.terminal
    original_jacobian = obj.bc_jac
    heights = np.asarray(heights, float)
    def terminal(self, y, par):
        residual = original_terminal(y, par)
        residual[:2] = (self.bridge.sigma*self.q*y[self.iz:self.iz+2]-heights)/self.bcweights[:2]
        return residual
    def jacobian(self, ya, yb, par):
        A, B, P = original_jacobian(ya, yb, par)
        for j in range(2):
            B[self.n+j] = 0.
            B[self.n+j, self.iz+j] = self.bridge.sigma*self.q/self.bcweights[j]
            P[self.n+j] = 0.
        return A, B, P
    obj.terminal = MethodType(terminal, obj)
    obj.bc_jac = MethodType(jacobian, obj)
    return original_terminal


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'loader', 'definition', 'port', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--modes', type=int, default=20)
    p.add_argument('--angular', type=int, default=1280)
    p.add_argument('--nodes', type=int, default=601)
    p.add_argument('--max-nodes', type=int, default=6000)
    p.add_argument('--tol', type=float, default=1e-8)
    p.add_argument('--check-only', action='store_true')
    a = p.parse_args()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    if a.out.with_suffix('.json').exists() or a.out.with_suffix('.json.gz').exists():
        raise FileExistsError('Use a fresh output prefix')
    record = json.loads(a.definition.read_text())
    port = json.loads(a.port.read_text())
    last = record['saved_tail_responses']['4']
    if not last['accepted'] or not record['final_prefix']['solver_success']:
        raise ValueError('Recorded final actual tail/prefix must have genuinely accepted')
    heights = [last['first_height'], last['second_height']]
    obj, ad, par, cfg, settings = build_model(a.source_topic.resolve(), a.loader.resolve(), record, port, a.modes, a.angular)
    original_terminal = install_height_boundary(obj, heights)
    x, y = initial_two_mode_field(obj, par, a.nodes, settings['bimodal_eta'])
    row = dict(scope=__doc__, command=sys.argv, script_sha256=digest(__file__),
               model_loader_sha256=digest(Path(__file__).with_name('recover_compact_anchor.py')),
               definition_sha256=digest(a.definition), port_sha256=digest(a.port),
               physical_profile=cfg, settings=settings, modes=a.modes,
               prescribed_physical_height=heights, initial_parameters=par.tolist(),
               initial_nodes=len(x), initial_bc=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()),
               initial_tail_height=(obj.bridge.sigma*obj.q*y[obj.iz:obj.iz+2,-1]).tolist(),
               bridge_sigma=float(obj.bridge.sigma),
               original_field_available=False, original_nonlinear_dn_solved=False,
               status='seed_ready', success=False)
    summary = a.out.with_suffix('.json')
    def persist():
        tmp=summary.with_suffix('.json.tmp');tmp.write_text(json.dumps(row,indent=2)+'\n');tmp.replace(summary)
    persist();print(json.dumps({k:v for k,v in row.items() if k!='initial_parameters'}),flush=True)
    if a.check_only:
        return
    from f6curve_domain_newton import install, STATS
    from trace_domain_newton import install as observe
    from curve_stable_prefix_bvp import save_checkpoint
    install();observe(a.out.with_name(a.out.name+'-newton.jsonl'))
    begin=time.monotonic()
    try:
        sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=1e-8,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        np.savez(a.out.with_name(a.out.name+'-raw.npz'),x=sol.x,y=sol.y,p=sol.p,c=sol.sol.c,rms_residuals=sol.rms_residuals)
        row.update(status='inner_returned',success=bool(sol.success),message=sol.message,nodes=len(sol.x),parameters=sol.p.tolist(),max_rms=float(sol.rms_residuals.max()),max_bc=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max()),domain_newton=dict(STATS),seconds=time.monotonic()-begin)
        persist();print(json.dumps(dict(event='height_inner',**{k:row[k] for k in ('success','nodes','max_rms','max_bc','seconds')})),flush=True)
        obj.initial(sol.p);f=obj.flow(sol.p[0])
        physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol=f.c2_interpolant(physical)
        saved=dict(config=dict(modes=a.modes,base_mode=4,core_kind='n4_fixed_raw_mean_circle',angular=a.angular),fixed_metric=True,raw_control_anchor_modes=record['raw_control_anchor_modes'],solver_success=bool(sol.success),angular_chart_eta=settings['bimodal_eta'],profile=cfg,physical_profile=cfg,physical_port=port,physical_port_sha256=digest(a.port),plateau_settings=settings,gauge_amplitude=obj.q,parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c,meridian_length=f.end,core_summary=obj._core.summary(),recovery_definition_sha256=digest(a.definition),recovery_boundary='H4/H8 observed; linear DN on higher modes',prescribed_physical_height=heights,original_nonlinear_dn_solved=False)
        save_checkpoint(a.out.with_suffix('.json.gz'),saved)
        row.update(checkpoint_sha256=digest(a.out.with_suffix('.json.gz')),actual_q=float(obj.support_amplitude),central_correction_scales=obj.pscale.tolist(),unreplaced_linear_dn_residual=original_terminal(sol.y[:,-1],sol.p).tolist())
        if sol.success:
            row['summary']=ad.audit(obj,physical,512)
        row.update(status='completed',seconds=time.monotonic()-begin)
    except Exception as exc:
        row.update(status='exception',error=repr(exc),seconds=time.monotonic()-begin,domain_newton=dict(STATS));persist();print(json.dumps(dict(event='height_exception',error=repr(exc))),flush=True);raise
    persist();print(json.dumps(dict(event='height_terminal',success=row['success'],metric=row.get('summary',{}).get('metric_l1'),actual_q=row.get('actual_q'),seconds=row['seconds'])),flush=True)


if __name__=='__main__':
    main()
