#!/usr/bin/env python3
"""Adaptive-chart prefix coupled to the actual weighted finite-tail DN.

Derived db6f continuation runner, using v3 warm remeshing.
This changes a finite linear port to a finite nonlinear one. Every physical
parameter, numerical cutoff, tail response, mean jet and failure is retained.
Finite-depth convergence and complete closed-surface reach remain separate.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
S=Path(__file__).resolve().parent;N=S.parent/'notes'
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
adaptive=module('adaptive_coupled',S/'950f-prefix-adaptive-chart-bvp-v2.py')
client=module('weighted_client',S/'950f-tail-client-v3.py')

class TailMixin:
    def terminal(self,y,p):
        f=self.flow(p[0]);dy=f.fun(np.array([f.end]),y.astype(np.longdouble)[:,None],p)[:,0]
        H=self.bridge.sigma*self.q*y[self.iz:];r=self.tail.solve(H,jacobian=False)
        return np.asarray((self.q*dy[self.iz:]-np.asarray(r['jets']['slope'])/math.sqrt(self.port['cut']['E']))/self.bcweights,float)
    def bc_jac(self,ya,yb,p):
        A,B,P=super().bc_jac(ya,yb,p);f=self.flow(p[0]);H=self.bridge.sigma*self.q*yb[self.iz:];r=self.tail.solve(H,jacobian=True)
        TJ=np.asarray(r['heightJetJacobian']).reshape(3*self.M+2,self.M)[:self.M]
        J,_=f.fun_jac(np.array([f.end]),yb.astype(np.longdouble)[:,None],p);T=self.q*J[self.iz:,:,0]
        T[:,self.iz:]-=self.bridge.sigma*self.q*TJ/math.sqrt(self.port['cut']['E']);B[self.n:]=T/self.bcweights[:,None];return A,B,P
    def seam_audit(self,sol):
        f=self.flow(sol.p[0]);s=np.array([f.end]);Y=sol.sol(s);Yp=sol.sol(s,1);Ypp=sol.sol(s,2);n=max(512,64*self.M);B,B1,B2=f.basis(n);fr,sp,dW=f.velocity_s(s,Y,Yp,B1,B2);g=fr['geo']
        Fs=g['s1']+self.q*f.values(Yp,B);Fs[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fss=g['s2']+self.q*f.values(Ypp,B);Fss[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None];Ft=fr['d'];Ftt=fr['dd'];Fst=sp
        aa,ap,app=f.profile(s);E0=np.sum(Fs*Fs,axis=2);F0=np.sum(Fs*Ft,axis=2);G0=np.sum(Ft*Ft,axis=2)
        metric=np.stack((E0-1,F0/aa[:,None],G0/aa[:,None]**2-1),axis=2)
        Es=2*np.sum(Fs*Fss,axis=2);Et=2*np.sum(Fs*Fst,axis=2);Fsmetric=np.sum(Fss*Ft+Fs*Fst,axis=2);Ftmetric=np.sum(Fst*Ft+Fs*Ftt,axis=2);Gs=2*np.sum(Ft*Fst,axis=2);Gt=2*np.sum(Ft*Ftt,axis=2)
        c1=np.stack((Es,Et,Fsmetric/aa[:,None]-ap[:,None]*F0/aa[:,None]**2,Ftmetric/aa[:,None],Gs/aa[:,None]**2-2*ap[:,None]*G0/aa[:,None]**3,Gt/aa[:,None]**2),axis=2)
        H=self.bridge.sigma*self.q*Y[self.iz:,0];response=self.tail.solve(H,jacobian=True,audit=True);j=response['jets'];E=j['E'];r_ss=-j['Ep']/(2*E**2);sig=self.bridge.sigma
        means=(float(np.mean(fr['V'][:,:,2])),float(np.mean(dW[:,:,2])));expected=(j['meanSlope']/math.sqrt(E),sig*(j['meanSecond']/E+j['meanSlope']*r_ss))
        second=sig*(np.asarray(j['second'])/E+np.asarray(j['slope'])*r_ss)
        return dict(scope='Actual finite nonlinear DN and full mean/nonmean height two-jet. Cut chart is identity through order two. Sampled C1 metric defect is explicit; full Cartesian alignment and infinite closure remain separate.',tail_record=self.tail.record_prefix.with_name(self.tail.record_prefix.name+f'_{self.tail.calls:04d}.json.gz').name,tail_converged=response['converged'],tail_shooting_residual=response['residual'],tail_jets=j,
            mean_first_actual=means[0],mean_first_expected=expected[0],mean_first_mismatch=means[0]-expected[0],mean_second_actual=means[1],mean_second_expected=expected[1],mean_second_mismatch=means[1]-expected[1],nonmean_first_mismatch=float(abs(self.q*Yp[self.iz:,0]-np.asarray(j['slope'])/math.sqrt(E)).max()),nonmean_second_mismatch=float(abs(self.q*Ypp[self.iz:,0]-second).max()),cut_metric_fft_l1=float(np.sum(abs(np.fft.fft(metric,axis=1)/n),axis=1).max()),cut_metric_c1_fft_l1=float(np.sum(abs(np.fft.fft(c1,axis=1)/n),axis=1).max()),angular_samples=n)

class AffineTailForInnerBVP:
    """Temporary slope linearization only; never an audited nonlinear response."""
    def __init__(self,height,response,M):
        self.height=np.asarray(height,float).copy();self.response=response
        self.J=np.asarray(response['heightJetJacobian']).reshape(3*M+2,M)[:M]
    def solve(self,height,jacobian=True,audit=False):
        if audit:raise RuntimeError('An affine DN cannot provide a nonlinear seam audit')
        jets=dict(self.response['jets'])
        jets['slope']=(np.asarray(jets['slope'])+self.J@(np.asarray(height)-self.height)).tolist()
        return dict(jets=jets,heightJetJacobian=self.response['heightJetJacobian'],
                    scope='Temporary affine slope DN for an inner BVP; not an actual tail solve')

def solve_with_actual_tail(o,tail,x,y,par,a):
    """Optional outer correction, accepted only after checking the original BC."""
    options=dict(tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=o.fun_jac,bc_jac=o.bc_jac)
    if not a.lagged_tail:return solve_bvp(o.fun,o.bc,x,y,par,**options),[]
    height=o.bridge.sigma*o.q*y[o.iz:,-1]
    response=tail.solve(height,jacobian=True,audit=False);history=[]
    for outer in range(8):
        o.tail=AffineTailForInnerBVP(height,response,o.M)
        try:sol=solve_bvp(o.fun,o.bc,x,y,par,**options)
        finally:o.tail=tail
        if not sol.success:
            history.append(dict(outer=outer,inner_success=False,message=sol.message))
            return sol,history
        candidate=o.bridge.sigma*o.q*sol.y[o.iz:,-1]
        actual=tail.solve(candidate,jacobian=True,audit=False)
        defect=float(np.max(np.abs(o.bc(sol.y[:,0],sol.y[:,-1],sol.p))))
        row=dict(outer=outer,inner_success=True,actual_boundary_residual=defect,
                 actual_tail_residual=actual['residual'],tail_calls=tail.calls)
        history.append(row);print(json.dumps(dict(event='actual_outer_check',**row)),flush=True)
        if defect<=a.bc_tol:return sol,history
        x,y,par=sol.x,sol.y,sol.p;height=candidate;response=actual
    raise FloatingPointError('Outer true-DN boundary residual did not reach the original tolerance')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--profile',type=Path,required=True);p.add_argument('--chart',type=Path,required=True);p.add_argument('--linear-port',type=Path,required=True);p.add_argument('--tail-config',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--restart',type=Path,required=True)
    p.add_argument('--amplitude',type=float,default=.08);p.add_argument('--warp-reference',type=float,default=.08);p.add_argument('--modes',type=int,default=8);p.add_argument('--angular',type=int,default=256);p.add_argument('--audit-angular',type=int,default=512);p.add_argument('--nodes',type=int,default=601);p.add_argument('--max-nodes',type=int,default=2400);p.add_argument('--tol',type=float,default=2e-7);p.add_argument('--bc-tol',type=float,default=1e-7);p.add_argument('--physical-bc-tol',type=float,default=2e-9);p.add_argument('--node-heap',type=int,default=1536);p.add_argument('--fixed',action='store_true');p.add_argument('--warmup-scales',type=float,nargs='*',default=[.1,.2,.4,.6,.8,1.]);p.add_argument('--probe-only',action='store_true');p.add_argument('--lagged-tail',action='store_true');p.add_argument('--preserve-restart-mesh',action='store_true');a=p.parse_args()
    adaptive.old.install_source(a.source_root)
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install,STATS
    cfg=json.loads(a.profile.read_text());chart=json.loads(a.chart.read_text());port=json.loads(a.linear_port.read_text());port['_sha256']=hashlib.sha256(a.linear_port.read_bytes()).hexdigest();tcfg=json.loads(a.tail_config.read_text())
    for k,v in port['parameters'].items():
        if tcfg.get(k)!=v:raise ValueError('Physical tail parameter mismatch: '+k)
    if tcfg['modes']!=a.modes or tcfg['spacing']!=3:raise ValueError('Nonlinear tail modes mismatch')
    _,Base=adaptive.build_classes(chart)
    class BVP(TailMixin,Base):pass
    o=BVP(cfg,port,a.amplitude,a.modes,a.angular,a.fixed,a.warp_reference);o.restart_remesh=a.nodes;o.bcweights=np.full(o.M,a.physical_bc_tol/a.bc_tol)
    restart_info=None
    if a.preserve_restart_mesh:
        initializer=module('db6f_preserve_restart',S/'db6f-prefix-preserve-restart.py')
        x,y,par,restart_info=initializer.restart(o,a.restart,chart)
    else:x,y,par=o.restart(a.restart)
    tail=None;begin=time.time();summary=dict(scope=__doc__,tail_config_sha256=hashlib.sha256(a.tail_config.read_bytes()).hexdigest(),solver_success=False)
    try:
        active_client=module('db6f_shared_client',S/'db6f-prefix-tail-shared-client.py')if tcfg.get('sharedEngines',False)else client
        tail=active_client.WeightedTailPort(a.tail_config,a.source_root,a.out_prefix.with_name(a.out_prefix.name+'_tail'),node_heap=a.node_heap);o.tail=tail
        summary['linear_dn_ready_max_difference']=float(abs(tail.linearD-np.asarray(port['linearSlope'][:o.M])).max());H=o.bridge.sigma*o.q*y[o.iz:,-1]
        for scale in a.warmup_scales:
            request=H*np.asarray(scale)**np.arange(1,o.M+1);r=tail.solve(request,jacobian=False,audit=True)
            print(json.dumps(dict(event='tail_warmup',scale=scale,converged=r['converged'],shoot=r['residual'],first_height=float(request[0]))),flush=True)
        if a.probe_only:
            r=tail.solve(H,jacobian=True,audit=True);summary.update(probe_only=True,tail_converged=r['converged'],tail_shooting_residual=r['residual'],tail_jets=r['jets'],height_vector=H.tolist(),tail_calls=tail.calls);return
        install();print(json.dumps(dict(event='start_coupled',q=a.amplitude,M=o.M,nodes=len(x),fixed=a.fixed)),flush=True)
        sol,outer_checks=solve_with_actual_tail(o,tail,x,y,par,a)
        f=o.flow(sol.p[0]);o.initial(sol.p);physical=SimpleNamespace(x=o.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=f.c2_interpolant(physical);frozen=cfg if a.fixed else {**cfg,'delta':cfg['delta']+sol.p[0]}
        out=dict(scope=__doc__,angular_chart='frozen-spline-adaptive-v1',chart=chart,warp_reference_q=a.warp_reference,config=dict(modes=o.M,base_mode=3,core_kind='adaptive_warped_support',angular=o.nt,tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,fixed_metric=a.fixed,actual_nonlinear_tail=True),frozen_profile=frozen,gauge_amplitude=o.q,actual_primary_amplitude=o.support_amplitude,meridian_length=f.end,physical_port_sha256=port['_sha256'],physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],tail_config=tcfg,parameters=sol.p.tolist(),central_correction_scales=o.pscale.tolist(),nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals)),newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
        out['dn_solver']='outer_actual_inner_affine'if a.lagged_tail else'actual_dn_at_every_query';out['actual_outer_checks']=outer_checks
        out['restart_mesh_diagnostics']=restart_info
        cp=a.out_prefix.with_suffix('.json.gz');save_checkpoint(cp,out);out['summary']=adaptive.audit(o,physical,a.audit_angular)
        out['summary']['scope']='Sampled physical prefix metric and Cartesian Darboux tensor after exact chain rule. Finite FFT l1 is not a continuous-angle proof. The actual nonlinear tail and mean/nonmean seam are recorded separately in tail_seam; full Cartesian closure and infinite-limit certification remain separate.'
        out['tail_seam']=o.seam_audit(physical);out['seconds']=time.time()-begin;out['tail_calls']=tail.calls;save_checkpoint(cp,out)
        summary={k:v for k,v in out.items()if k not in ('mesh','pp_coefficients')}
        print(json.dumps(dict(event='result',success=out['solver_success'],delta=frozen['delta'],q=o.support_amplitude,metric=out['summary']['metric_l1'],darboux=out['summary']['darboux_l1'],first_mean_mismatch=out['tail_seam']['mean_first_mismatch'],second_mean_mismatch=out['tail_seam']['mean_second_mismatch'],tail_calls=tail.calls)),flush=True)
    except Exception as exc:summary.update(error=repr(exc),tail_calls=tail.calls if tail else 0);print(json.dumps(dict(event='failure',error=repr(exc))),flush=True)
    finally:
        if tail:tail.close()
        summary['seconds']=time.time()-begin;a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')

if __name__=='__main__':main()
