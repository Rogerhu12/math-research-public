#!/usr/bin/env python3
"""Couple the dual core prefix to an actual nonlinear finite tail D-N map.

All root_dual_core_bvp.py arguments remain available. --tail-config supplies
the actual tail discretization. Each true tail request uses the complete
represented cut height. The outer algorithm solves the nonlinear prefix
against an affine tail tangent, then accepts only after a new solve of
the original nonlinear tail confirms its physical boundary residual.
The nested option requests the true tail at each boundary evaluation.
Mean and second jets are measured separately. This finite joined
problem is not an infinite tail, a cap, or a complete closed surface.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import numpy as np
HERE=Path(__file__).resolve().parent


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--tail-config',type=Path,required=True)
    parser.add_argument('--node-heap',type=int,default=1024)
    parser.add_argument('--client',choices=['source','analytic-first','stored-bounded','stored-resumable'],default='analytic-first')
    parser.add_argument('--coupling',choices=['nested','outer'],default='outer')
    parser.add_argument('--actual-tail-tol',type=float,default=1e-10)
    parser.add_argument('--defer-tail-start',action='store_true')
    options,remaining=parser.parse_known_args()
    def argument(name):return Path(remaining[remaining.index(name)+1])
    source=argument('--source-topic');out=argument('--out-prefix')
    cfg=json.loads(options.tail_config.read_text())
    # Numerical algorithm selection is separate from the physical metric.
    os.environ['VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND']='fourier-root'
    os.environ['VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND']='tangent'
    client_file=({'analytic-first':HERE/'numerical-tail-analytic-client.py',
                  'stored-bounded':HERE/'tail_stored_client.py',
                  'stored-resumable':HERE/'tail_resumable_client.py',
                  'source':source/'scripts/78718-prefix-tail-geometric-client.py'}[options.client])
    client=module('root_actual_tail_client',client_file)
    root=module('root_actual_dual',HERE/'root_dual_core_bvp.py')
    original=root.make_dual;clients=[]

    def make_actual(*args,**kwargs):
        Base=original(*args,**kwargs)
        class Actual(Base):
            def __init__(self,*a,**kw):
                super().__init__(*a,**kw)
                if int(cfg['modes'])!=self.M or int(cfg['spacing'])!=2:
                    raise ValueError('Actual tail and prefix must use the same complete m2 spectrum')
                for key,value in self.port['parameters'].items():
                    if cfg.get(key)!=value:raise ValueError('Physical tail parameter mismatch: '+key)
                self.tail=None
                self.raw_recovery_context=dict(actual_nonlinear_tail=True,
                    tail_config_sha256=hashlib.sha256(options.tail_config.read_bytes()).hexdigest(),
                    client=options.client,coupling=options.coupling,
                    actual_tail_tolerance=options.actual_tail_tol)
                self.anchor=None;self.outer_history=[]
                if not options.defer_tail_start:self.ensure_tail()

            def ensure_tail(self):
                if self.tail is not None:return
                import root_raw_collocation
                root_raw_collocation.release_memory('before_actual_tail_worker_start')
                self.tail=client.WeightedTailPort(options.tail_config,
                    source/'repro/source-root',out.with_name(out.name+'-tail-response'),
                    node_heap=options.node_heap)
                clients.append(self.tail)
                for key in ('radius','backgroundSlope','backgroundSecond','E','Ep'):
                    if not np.isclose(self.tail.cut[key],self.port['cut'][key],rtol=2e-11,atol=2e-13):
                        raise ValueError('Actual nonlinear cut mismatch: '+key)

            def tail_height(self,y):
                return self.bridge.sigma*self.q*np.asarray(y[self.iz:],float)

            def tail_boundary(self,y):
                self.ensure_tail()
                height=self.tail_height(y)
                if options.coupling=='outer' and self.anchor is not None:
                    H,K,J=self.anchor
                    return K+J@(height-H),J
                response=self.tail.solve(height,jacobian=True,audit=False)
                J=np.asarray(response['heightJetJacobian']).reshape(-1,self.M)
                if J.shape!=(3*self.M+2,self.M):raise ValueError('Unexpected physical height-jet Jacobian layout')
                return np.asarray(response['jets']['slope']),J[:self.M]

            def solve_coupled(self,fun,bc,x,y,p,**kw):
                from scipy.integrate import solve_bvp
                self.ensure_tail()
                if options.coupling=='nested':return solve_bvp(fun,bc,x,y,p,**kw)
                for iteration in range(8):
                    H=self.tail_height(y[:,-1]);response=self.tail.solve(H,jacobian=True,audit=False)
                    J=np.asarray(response['heightJetJacobian']).reshape(-1,self.M)[:self.M]
                    self.anchor=(H.copy(),np.asarray(response['jets']['slope']),J)
                    sol=solve_bvp(fun,bc,x,y,p,**kw)
                    row=dict(iteration=iteration,inner_success=bool(sol.success),nodes=len(sol.x),
                        inner_residual=float(np.max(sol.rms_residuals)))
                    self.outer_history.append(row)
                    if not sol.success:return sol
                    # Preserve a successful affine-inner state before a true
                    # tail request. It is only a restart, never an accepted
                    # coupled solution or a physical surface.
                    import root_raw_collocation
                    from types import SimpleNamespace
                    pending=SimpleNamespace(**{key:getattr(sol,key) for key in
                        ('x','y','p','sol','rms_residuals','status','niter')},
                        success=False,message='Affine inner solve complete; actual nonlinear tail acceptance pending')
                    recovery=root_raw_collocation.write(
                        out.with_name(out.name+f'-outer-{iteration:02d}-raw-collocation.json.gz'),
                        pending,self,SimpleNamespace(tol=kw['tol']),
                        dict(actual_nonlinear_coupling_pending=True,
                             affine_inner_success=True,outer_iteration=iteration,
                             outer_history=list(self.outer_history)))
                    row['pending_raw_checkpoint']=recovery
                    print(json.dumps(dict(event='actual_tail_pending_inner_saved',**recovery)),flush=True)
                    root_raw_collocation.release_memory('before_actual_tail_outer_recheck')
                    self.select(sol.p);flow=self.flow(sol.p[0]);Hnew=self.tail_height(sol.y[:,-1])
                    actual=self.tail.solve(Hnew,jacobian=True,audit=False)
                    dy=flow.fun(np.array([flow.end]),np.asarray(sol.y[:,-1],np.longdouble)[:,None],sol.p)[:,0]
                    residual=np.asarray(self.q*dy[self.iz:]-np.asarray(actual['jets']['slope'])/math.sqrt(self.port['cut']['E']),float)
                    row.update(actual_physical_bc_max=float(np.max(abs(residual))),
                        height_change_max=float(np.max(abs(Hnew-H))),tail_residual=actual['residual'])
                    print(json.dumps(dict(event='actual_tail_outer_check',**row)),flush=True)
                    # The acceptance test is the original nonlinear D-N map,
                    # never the affine inner boundary or an expanded cache hit.
                    self.anchor=(Hnew.copy(),np.asarray(actual['jets']['slope']),
                        np.asarray(actual['heightJetJacobian']).reshape(-1,self.M)[:self.M])
                    if np.max(abs(residual))<=options.actual_tail_tol:return sol
                    x,y,p=sol.x,sol.y,sol.p
                sol.success=False;sol.message='Eight actual nonlinear tail outer corrections exhausted'
                return sol

            def terminal(self,y,p):
                self.select(p);flow=self.flow(p[0])
                dy=flow.fun(np.array([flow.end]),np.asarray(y,np.longdouble)[:,None],p)[:,0]
                slope,_=self.tail_boundary(y)
                return np.asarray((self.q*dy[self.iz:]-slope/math.sqrt(self.port['cut']['E']))/self.bcweights,float)

            def bc_jac(self,ya,yb,p):
                self.select(p);self.initial(p);flow=self.flow(p[0])
                A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n)
                B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
                P[:self.n]=-self._initial_jac
                J,_=flow.fun_jac(np.array([flow.end]),np.asarray(yb,np.longdouble)[:,None],p)
                _,height_jac=self.tail_boundary(yb)
                T=self.q*J[self.iz:,:,0]
                T[:,self.iz:]-=self.q*self.bridge.sigma*height_jac/math.sqrt(self.port['cut']['E'])
                B[self.n:]=T/self.bcweights[:,None]
                # In the fixed-g adapter, every parameter is an inlet support
                # coefficient and the fixed terminal flow has no parameter
                # dependence. Its complete analytic inlet Jacobian is above.
                for j in (() if getattr(self,'fixed',False) else (0,1)):
                    step=2e-6*max(.1,abs(self.cfg['delta']+p[0]) if j==0 else abs(self.cfg[self.second_control]+p[1]))
                    pp=p.copy();pm=p.copy();pp[j]+=step;pm[j]-=step
                    P[:,j]=(self.bc(ya,yb,pp)-self.bc(ya,yb,pm))/(2*step)
                self.select(p);self.flow(p[0]);self.initial(p)
                return A,B,P

            def prepare_recovery_output(self,data):
                data['scope']=__doc__
                data['config']['actual_nonlinear_tail']=True
                data['actual_tail_recovery']=dict(context=self.raw_recovery_context,
                    defer_tail_start=options.defer_tail_start,outer_history=self.outer_history,
                    note='Accepted coupled BVP state; final audited jets and seam are pending.')

            def finalize_output(self,data,physical):
                self.ensure_tail()
                data['scope']=__doc__;data['config']['actual_nonlinear_tail']=True
                data['actual_tail']=dict(config=cfg,config_sha256=hashlib.sha256(options.tail_config.read_bytes()).hexdigest(),
                    client_kind=options.client,client_sha256=hashlib.sha256(client_file.read_bytes()).hexdigest(),
                    coupling=options.coupling,actual_physical_bc_tolerance=options.actual_tail_tol,
                    outer_history=self.outer_history,
                    source_sha256=self.tail.sources,ready=self.tail.ready,requests=self.tail.calls,
                    adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
                if not data['solver_success']:return
                y=physical.y[:,-1];f=self.flow(physical.p[0]);L=f.end
                response=self.tail.solve(self.tail_height(y),jacobian=True,audit=True)
                tail=data['actual_tail'];tail.update(requests=self.tail.calls,
                    final_response=str(self.tail.record_prefix.with_name(self.tail.record_prefix.name+f'_{self.tail.calls:04d}.json.gz')),
                    residual=response['residual'],jets=response['jets'],audit=response.get('audit'))
                E=float(self.port['cut']['E']);Ep=float(self.port['cut']['Ep']);sigma=self.bridge.sigma
                slope=np.asarray(response['jets']['slope']);second=np.asarray(response['jets']['second'])
                # Z_prefix = sigma Z_tail + constant, r_s = sigma/sqrt(E).
                prefix_first=self.q*physical.sol(L,1)[self.iz:]
                prefix_second=self.q*physical.sol(L,2)[self.iz:]
                target_first=slope/math.sqrt(E)
                target_second=sigma*(second/E-Ep*slope/(2*E*E))
                tail['seam_nonmean']=dict(height_max=float(abs(self.tail_height(y)).max()),
                    first_max=float(abs(prefix_first-target_first).max()),
                    second_max=float(abs(prefix_second-target_second).max()),
                    scope='Physical PPoly derivatives versus actual finite-tail jets. Height means and Cartesian frame closure remain separate.')
                if tail['seam_nonmean']['first_max']>options.actual_tail_tol:
                    data['solver_success']=False
                    data['message']='Final audited actual nonlinear slope failed the specified boundary tolerance'
                data['summary']['scope']='Sampled physical prefix metric with actual nonlinear finite-tail height slope boundary. Infinite closure, full Cartesian seam, cap and all-time geometry remain open.'
        return Actual

    root.make_dual=make_actual;sys.argv=[sys.argv[0]]+remaining
    try:root.main()
    finally:
        for tail in clients:
            before=tail.proc.poll()
            try:tail.close()
            finally:print(json.dumps(dict(event='actual_tail_worker_closed',
                returncode_before_close=before,returncode_after_close=tail.proc.poll())),flush=True)


if __name__=='__main__':main()
