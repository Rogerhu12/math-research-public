#!/usr/bin/env python3
"""Ellipse-core prefix matched to the actual nonlinear finite-depth tail DN.
Design mode varies delta. Fixed mode freezes every profile parameter and instead
solves the extrinsic core aspect. Neither mode certifies infinite-tail closure.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
os.environ.setdefault('NODE_OPTIONS','--max-old-space-size=384')
import argparse,gzip,hashlib,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from repo_scan_ellipse_bvp import EllipseBVP,install_source,audit
from fixed_metric_ellipse_bvp import FixedMetricBVP
from repo_scan_gentle import finite_value

class ActualTailMixin:
    def terminal(self,y,p):
        flow=self.flow(p[0]);dy=flow.fun(np.array([flow.end]),y[:,None],p)[:,0]
        H=self.bridge.sigma*self.q*y[self.iz:]
        slope=np.asarray(self.tail.solve(H,jacobian=False)['jets']['slope'])
        return (self.q*dy[self.iz:]-slope/math.sqrt(self.port['cut']['E']))/self.bcweights
    def bc_jac(self,ya,yb,p):
        A,B,P=super().bc_jac(ya,yb,p)
        flow=self.flow(p[0]);H=self.bridge.sigma*self.q*yb[self.iz:]
        response=self.tail.solve(H,jacobian=True)
        TJ=np.asarray(response['heightJetJacobian']).reshape(3*self.M+2,self.M)[:self.M]
        FJ,_=flow.fun_jac(np.array([flow.end]),yb[:,None],p)
        J=self.q*FJ[self.iz:,:,0]
        J[:,self.iz:]-=self.bridge.sigma*self.q*TJ/math.sqrt(self.port['cut']['E'])
        B[self.n:]=J/self.bcweights[:,None]
        return A,B,P
    def tail_seam_audit(self,sol):
        flow=self.flow(sol.p[0]);s=np.array([flow.end]);y=sol.sol(s)
        C=flow.base(s)+self.q*y
        Cp=flow.base(s,1)+self.q*sol.sol(s,1)
        Cpp=flow.base(s,2)+self.q*sol.sol(s,2)
        B,B1,B2=flow.basis(max(256,self.nt));fr=flow.frame(s,C,B1,B2)
        dV=flow.frame_jvp(fr,flow.values(Cp,B1),flow.values(Cp,B2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
        be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        response=self.tail.solve(self.bridge.sigma*self.q*y[self.iz:,0],jacobian=True,audit=True)
        j=response['jets'];E=j['E'];app=-j['Ep']/(2*E**2)
        m1=float(np.mean(fr['V'][:,:,2]));m2=float(np.mean(dV[:,:,2]))
        e1=j['meanSlope']/math.sqrt(E)
        e2=self.bridge.sigma*(j['meanSecond']/E+j['meanSlope']*app)
        n2=self.bridge.sigma*(np.asarray(j['second'])/E+np.asarray(j['slope'])*app)
        return dict(response=response,scope='Finite-tail nonlinear height Cauchy data and both mean jets. Full planar Cartesian seam and infinite closure still require separate verification.',
            mean_first_jet_actual=m1,mean_first_jet_expected=e1,mean_first_jet_mismatch=m1-e1,
            mean_second_jet_actual=m2,mean_second_jet_expected=e2,mean_second_jet_mismatch=m2-e2,
            nonmean_first_jet_mismatch=float(abs(Cp[self.iz:,0]-np.asarray(j['slope'])/math.sqrt(E)).max()),
            nonmean_second_jet_mismatch=float(abs(Cpp[self.iz:,0]-n2).max()))

class DesignActualTail(ActualTailMixin,EllipseBVP):pass
class FixedActualTail(ActualTailMixin,FixedMetricBVP):pass

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',required=True,type=Path)
    p.add_argument('--profile',required=True,type=Path)
    p.add_argument('--tail-config',required=True,type=Path)
    p.add_argument('--linear-port',required=True,type=Path)
    p.add_argument('--out',required=True,type=Path)
    p.add_argument('--aspect',default=1.02,type=float)
    p.add_argument('--modes',default=4,type=int)
    p.add_argument('--angular',default=128,type=int)
    p.add_argument('--audit-angular',default=256,type=int)
    p.add_argument('--tol',default=2e-6,type=float)
    p.add_argument('--bc-tol',default=2e-7,type=float)
    p.add_argument('--max-nodes',default=1600,type=int)
    p.add_argument('--nodes',default=101,type=int)
    p.add_argument('--restart',type=Path)
    p.add_argument('--linear-only',action='store_true')
    p.add_argument('--fixed',action='store_true')
    p.add_argument('--split-flux',action='store_true')
    p.add_argument('--cut-preserving',action='store_true')
    a=p.parse_args();install_source(a.source_root)
    from curve_stable_prefix_bvp import save_checkpoint,load_checkpoint
    from f6curve_domain_newton import install,STATS
    if a.split_flux:
        import f6root_recording_split_tail_port as recording
        recording.install(a.out.with_name(a.out.name.removesuffix('.json.gz')+'_tail'))
    from f6curve_compact_tail_port import CompactTailPort
    cfg=json.loads(a.profile.read_text());raw=json.loads(a.linear_port.read_text())
    port=dict(cut=raw['cut'],linearSlope=[m['slope'] for m in raw['rows'][-1]['modes']])
    tailcfg=json.loads(a.tail_config.read_text())
    if tailcfg['modes']!=a.modes:raise ValueError('tail modes mismatch')
    if any(tailcfg[k]!=raw['parameters'][k] for k in ['rCut','wCut','width','curvatureBound','orientation','slopeCap','capTransition','prefixR','prefixReturnStart','prefixEnd','protectCell','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature']):raise ValueError('actual tail geometry mismatch with linear port')
    begin=time.time();tail=None;out={}
    try:
        cls=(FixedMetricBVP if a.fixed else EllipseBVP) if a.linear_only else (FixedActualTail if a.fixed else DesignActualTail)
        obj=cls(cfg,port,a.aspect,a.modes,a.angular)
        if not a.linear_only:
            if a.cut_preserving:
                from fixed_metric_cut_tail_port import CutPreservingTailPort
                tail=CutPreservingTailPort(a.tail_config,a.source_root,a.out.with_name(a.out.name.removesuffix('.json.gz')+'_tail'))
            else:tail=CompactTailPort(a.tail_config)
            if not np.allclose(tail.linearD,port['linearSlope'][:a.modes],rtol=2e-5,atol=1e-8):
                raise ValueError('Actual nonlinear worker linear DN differs from supplied physical port')
            obj.tail=tail
        if a.restart:x,y,v=obj.restart(a.restart)
        else:x,y,v=obj.seed(a.nodes)
        print(json.dumps(dict(event='start',mode='fixed' if a.fixed else 'design',aspect=a.aspect,M=a.modes,q=obj.q,tail=not a.linear_only,mesh=len(x),linear_height=obj.q*float(y[obj.iz,-1]),L=obj.flow(v[0]).end)),flush=True)
        install()
        s=solve_bvp(obj.fun,obj.bc,x,y,v,tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac)
        flow=obj.flow(s.p[0]);L=flow.end;obj.initial(s.p)
        physical=SimpleNamespace(x=s.x*L,y=s.y,p=s.p);physical.sol=flow.c2_interpolant(physical)
        frozen=cfg if a.fixed else dict(cfg,delta=cfg['delta']+s.p[0])
        out=dict(scope=__doc__,config=dict(modes=a.modes,aspect=a.aspect,angular=a.angular,tol=a.tol,bc_tol=a.bc_tol),
            frozen_profile=frozen,gauge_amplitude=obj.q,meridian_length=L,parameters=s.p.tolist(),
            actual_core_aspect=obj.aspect,central_correction_scales=obj.pscale.tolist(),nodes=len(s.x),
            solver_success=bool(s.success),message=s.message,max_rms_collocation_residual=float(np.max(s.rms_residuals)),
            newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
        out=save_checkpoint(a.out,out)
        out['summary']=audit(obj,physical,151,a.audit_angular)
        if tail is not None:
            out['tail_seam']=obj.tail_seam_audit(physical)
        out['seconds']=time.time()-begin
        save_checkpoint(a.out,out)
    except Exception as e:
        out.update(solver_success=False,error=repr(e),seconds=time.time()-begin)
        if tail is not None:out['tail_calls']=tail.calls
    finally:
        if tail is not None:tail.close()
    summary={k:v for k,v in out.items() if k not in ['mesh','pp_coefficients','tail','scope']}
    summary.update(tail_config=str(a.tail_config),tail_config_sha256=hashlib.sha256(a.tail_config.read_bytes()).hexdigest(),profile_config=str(a.profile),linear_port_sha256=hashlib.sha256(a.linear_port.read_bytes()).hexdigest())
    if 'tail' in out:
        z=out['tail'];summary['tail']={k:v for k,v in z.items() if k not in ['checkpoint','heightJetJacobian','jets','history']};summary['tail_height']=z['jets']['height'];summary['tail_slope']=z['jets']['slope']
    a.out.with_name(a.out.name.removesuffix('.json.gz')+'_summary.json').write_text(json.dumps(finite_value(summary),indent=2,allow_nan=False)+'\n')
    print(json.dumps(finite_value(summary)),flush=True)

if __name__=='__main__':main()
