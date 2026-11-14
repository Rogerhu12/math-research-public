#!/usr/bin/env python3
"""Nonlinear planar ellipse-core to finite Robin-port BVP.

Unknowns: cycle excursion (one metric-design parameter) and M-1 higher
planar inlet coefficients.  The latter keep the two principal-axis vertices
in the prescribed ratio.  The geometric Frenet equation is not linearized.
After solving, the profile is frozen and the actual C2 polynomial map is
audited independently in Cartesian coordinates.  A finite linear Robin port
is NOT a circular collar or an infinite-tail closure.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly


def install_source(root):
    sys.path.insert(0,str(Path(root)/'topics/large-amplitude-twist-flex/scripts'))


def make_flow_class():
    from f6curve_outward_bvp import OutwardPrefix
    from f6curve_local_frame import install_local_frame
    class FrozenFlow(OutwardPrefix):
        def __init__(self,cfg,port,bridge,modes,q,angular):
            self.bridge=None
            super().__init__(modes,q,cfg['delta'],cfg['vu'],cfg['vd'],cfg['ramp'],
                             cfg['cycles'],angular,2,compute_stable=False)
            self.prefix_end=self.end
            self.bridge=bridge
            self.end=self.prefix_end+bridge.L
            self.port_data=port
            self.breaks=np.unique(np.r_[self.breakpoints,self.end])
            install_local_frame(self)
        def profile(self,s):
            s=np.atleast_1d(s)
            if self.bridge is None:
                return super().profile(s)
            a,v,acc=super().profile(np.minimum(s,self.prefix_end))
            mask=s>self.prefix_end
            if np.any(mask):
                a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
            return a,v,acc
    return FrozenFlow


class EllipseBVP:
    def __init__(self,cfg,port,aspect=1.02,modes=4,angular=128,arc_nodes=2048):
        from f6curve_bidirectional_bridge import DirectionalBridge
        from repo_scan_ellipse_core import PlanarEllipseCore
        self.cfg=dict(cfg);self.port=port;self.aspect=aspect
        self.M=modes;self.n=3*modes+1;self.iz=2*modes+1
        self.nt=angular;self.arc_nodes=arc_nodes
        self.bridge=DirectionalBridge(port['cut'])
        self.Flow=make_flow_class()
        temporary=self.Flow(self.cfg,port,self.bridge,modes,.01,angular)
        inlet=PlanarEllipseCore(aspect,arc_nodes=arc_nodes)
        C,_=inlet.inlet(temporary,max(1024,64*modes))
        self.q=float(C[1])
        if self.q<1e-5:
            raise ValueError('Use an aspect ratio measurably larger than one')
        self.pscale=np.array([max(self.q**j,1e-9) for j in range(2,modes+1)])
        self.bcweights=np.maximum(self.q**np.arange(1,modes+1),1e-6)
        self._flow_key=None;self._flow=None
        self._core_key=None;self._core=None;self._initial=None;self._inlet_metrics=None

    def flow(self,p0):
        if self._flow_key!=float(p0):
            delta=self.cfg['delta']+float(p0)
            if not .005<delta<2.:
                raise FloatingPointError('Cycle excursion left the positive design domain')
            self._flow=self.Flow({**self.cfg,'delta':delta},self.port,self.bridge,
                                self.M,self.q,self.nt)
            self._flow_key=float(p0)
        return self._flow

    def initial(self,p):
        from repo_scan_ellipse_core import PlanarEllipseCore
        key=tuple(np.asarray(p[1:],float))
        if key!=self._core_key:
            core=PlanarEllipseCore(self.aspect,np.asarray(p[1:])*self.pscale,self.arc_nodes)
            flow=self.flow(p[0])
            C,metrics=core.inlet(flow,max(1024,64*self.M))
            self._initial=(C-flow.base(np.array([0.]))[:,0])/self.q
            self._core=core;self._inlet_metrics=metrics;self._core_key=key
        return self._initial

    def fun(self,t,y,p):
        flow=self.flow(p[0]);L=flow.end
        return L*flow.fun(np.asarray(t)*L,y,p)

    def fun_jac(self,t,y,p):
        flow=self.flow(p[0]);L=flow.end
        J,_=flow.fun_jac(np.asarray(t)*L,y,p)
        PJ=np.zeros((self.n,self.M,len(t)))
        step=2e-6*max(.1,self.cfg['delta']+p[0])
        plus=p.copy();minus=p.copy();plus[0]+=step;minus[0]-=step
        PJ[:,0,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
        self.flow(p[0])
        return L*J,PJ

    def terminal(self,y,p):
        flow=self.flow(p[0])
        s=np.array([flow.end])
        dy=flow.fun(s,y[:,None],p)[:,0]
        D=np.asarray(self.port['linearSlope'][:self.M])
        return self.q*(dy[self.iz:]-self.bridge.sigma*D*y[self.iz:]/
                       math.sqrt(self.port['cut']['E']))/self.bcweights

    def bc(self,ya,yb,p):
        return np.r_[ya-self.initial(p),self.terminal(yb,p)]

    def bc_jac(self,ya,yb,p):
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n)
        B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        flow=self.flow(p[0]);s=np.array([flow.end])
        J,_=flow.fun_jac(s,yb[:,None],p)
        TJ=self.q*J[self.iz:,:,0]
        D=np.asarray(self.port['linearSlope'][:self.M])
        TJ[:,self.iz:]-=self.q*self.bridge.sigma*np.diag(D)/math.sqrt(self.port['cut']['E'])
        B[self.n:]=TJ/self.bcweights[:,None]
        for j in range(1,self.M):
            step=2e-6/(self.pscale[j-1]*(j+1)**2)
            v=np.zeros(self.M);v[j]=step
            P[:self.n,j]=-(-self.initial(p+2*v)+8*self.initial(p+v)-
                           8*self.initial(p-v)+self.initial(p-2*v))/(12*step)
        self.initial(p);self.flow(p[0])
        return A,B,P

    def seed(self,nodes):
        from repo_scan_ellipse_line import backward
        profile,line=backward(self.cfg,self.port)
        flow=self.flow(0.)
        s=np.unique(np.r_[np.linspace(0,flow.end,nodes),flow.breaks])
        fg=np.empty((2,len(s)))
        for j,(lo,hi,solution,scale) in enumerate(line.segments):
            mask=(s>=lo)&((s<hi) if j+1<len(line.segments) else (s<=hi))
            if np.any(mask):
                fg[:,mask]=solution(s[mask])*math.exp(scale-line.logscale)/line.core[0]
        y=np.zeros((self.n,len(s)))
        y[1]=fg[0];y[self.M+1]=-fg[0]/2;y[self.iz]=fg[1]
        p=np.zeros(self.M)
        correction=self.initial(p)-y[:,0]
        y+=correction[:,None]*np.maximum(0,1-s/(flow.prefix.Tu/2 if hasattr(flow,'prefix') else flow.Tu/2))[None,:]**3
        return s/flow.end,y,p

    def restart(self,path):
        from curve_stable_prefix_bvp import load_checkpoint
        old=load_checkpoint(path);M0=old['config']['modes'];q0=old['gauge_amplitude']
        p=np.zeros(self.M);p[0]=old['frozen_profile']['delta']-self.cfg['delta']
        oldscale=np.asarray(old['central_correction_scales'])
        for j in range(1,min(M0,self.M)):
            p[j]=old['parameters'][j]*oldscale[j-1]/self.pscale[j-1]*(self.q/q0)**(j+1)
        flow=self.flow(p[0]);ox=np.asarray(old['mesh']);oldL=old['meridian_length']
        op=PPoly.construct_fast(np.asarray(old['pp_coefficients']),ox,extrapolate=True,axis=1)
        t=np.unique(np.r_[ox/oldL,flow.breaks/flow.end])
        oy=op(t*oldL);y=np.zeros((self.n,len(t)));ratio=self.q/q0
        y[0]=oy[0]*ratio
        for j in range(min(M0,self.M)):
            scale=ratio**j
            for ni,oi in [(1+j,1+j),(self.M+1+j,M0+1+j),(self.iz+j,2*M0+1+j)]:
                y[ni]=oy[oi]*scale
        return t,y,p


def audit(obj,sol,points=201,angular=256):
    flow=obj.flow(sol.p[0]);obj.initial(sol.p);core=obj._core
    s=np.unique(np.r_[np.linspace(0,flow.end,points),sol.x,(sol.x[:-1]+sol.x[1:])/2])
    heights=flow.height_integral(sol,s,angular,6)
    B,B1,B2=flow.basis(angular)
    theta=2*np.pi*np.arange(angular)/angular
    exact=core.evaluate(theta)
    result=dict(metric_l1=0.,flow_defect=0.,darboux_l1=0.,kappa_sample=0.,
                root_min=1.,radius_max=0.,height_max=0.,cylindrical_projection_min=math.inf)
    for first in range(0,len(s),64):
        t=s[first:first+64];C=flow.base(t)+obj.q*sol.sol(t)
        Cp=flow.base(t,1)+obj.q*sol.sol(t,1)
        Cpp=flow.base(t,2)+obj.q*sol.sol(t,2)
        fr=flow.frame(t,C,B1,B2)
        Fs=flow.values(Cp,B);Fs[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        dV=flow.frame_jvp(fr,flow.values(Cp,B1),flow.values(Cp,B2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
        be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        Fss=flow.values(Cpp,B);Fss[:,:,2]+=np.mean(dV[:,:,2],axis=1)[:,None]
        Ft=fr['d'];Ftt=fr['dd'];Fst=flow.values(Cp,B1);a=fr['a'][:,None]
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/a,G/a**2-1),axis=2)
        l1=np.sum(abs(np.fft.fft(errors,axis=1)/angular),axis=1)
        normal=np.cross(Fs,Ft);normal/=np.linalg.norm(normal,axis=2)[:,:,None]
        L=np.sum(Fss*normal,axis=2);M=np.sum(Fst*normal,axis=2);N=np.sum(Ftt*normal,axis=2)
        detI=E*G-F*F;tr=(L*G-2*M*F+N*E)/detI;detII=(L*N-M*M)/detI
        kap=(abs(tr)+np.sqrt(np.maximum(0.,tr*tr-4*detII)))/2
        Hst=(Fst-(fr['ap']/fr['a'])[:,None,None]*Ft)/a[:,:,None]
        Htt=(Ftt+(fr['a']*fr['ap'])[:,None,None]*Fs)/a[:,:,None]**2
        gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-(Ft/a[:,:,None])[:,:,:,None]*(Ft/a[:,:,None])[:,:,None,:]
        tensor=.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]
        tensor+=(fr['app']/fr['a'])[:,None,None,None]*gram
        tc=np.fft.fft(tensor,axis=1)/angular
        actual=flow.values(C,B);actual[:,:,2]+=heights[first:first+len(t),None]
        cross=lambda x,y:x[:,:,0]*y[:,:,1]-x[:,:,1]*y[:,:,0]
        projection=cross(actual,Ft)*Fs[:,:,2]-cross(actual,Fs)*Ft[:,:,2]
        result['metric_l1']=max(result['metric_l1'],float(np.max(l1)))
        result['flow_defect']=max(result['flow_defect'],float(np.max(np.linalg.norm(Fs-fr['V'],axis=2))))
        result['darboux_l1']=max(result['darboux_l1'],float(np.max(np.sum(np.sqrt(np.sum(abs(tc)**2,axis=(2,3))),axis=1))))
        result['kappa_sample']=max(result['kappa_sample'],float(np.max(kap)))
        result['root_min']=min(result['root_min'],float(np.min(fr['margin'])))
        result['radius_max']=max(result['radius_max'],float(np.max(np.linalg.norm(actual[:,:,:2],axis=2))))
        result['height_max']=max(result['height_max'],float(np.max(abs(actual[:,:,2]))))
        result['cylindrical_projection_min']=min(result['cylindrical_projection_min'],float(np.min(projection)))
        if first==0:
            result['inlet_position_error']=float(np.max(np.linalg.norm(actual[0]-exact['F'],axis=1)))
            result['inlet_first_jet_error']=float(np.max(np.linalg.norm(Fs[0]-[0,0,1],axis=1)))
            result['inlet_second_jet_error']=float(np.max(np.linalg.norm(Fss[0],axis=1)))
    end=sol.sol(np.array([flow.end]))[:,0]
    physical=obj.q*end
    result.update(sample_s=len(s),sample_theta=angular,
        reflected_prefix_cylinder_diagonal=2*math.hypot(result['radius_max'],result['height_max']),
        terminal_height_max=float(np.max(abs(physical[obj.iz:]))),
        terminal_noncircle_coeff_max=float(np.max(abs(physical[1:]))),
        central_aspect=obj.aspect,central_major_radius=core.major_radius,
        central_minor_radius=core.minor_radius,central_curvature_min=core.minimum_sampled_curvature,
        central_curvature_max=core.maximum_sampled_curvature,
        central_corrections=list(core.corrections),inlet_projection_diagnostics=obj._inlet_metrics,
        meridian_length=flow.end,
        scope='Actual C2 finite-prefix map sampled in s, whole-angle polynomial l1 metric/Darboux diagnostics. Linear Robin port is not circular; no closed-surface assertion.')
    result['sampled_kappa_times_diagonal']=result['kappa_sample']*result['reflected_prefix_cylinder_diagonal']
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--aspects',type=float,nargs='+',default=[1.02,1.05,1.1,1.2])
    parser.add_argument('--modes',type=int,default=4)
    parser.add_argument('--angular',type=int,default=128)
    parser.add_argument('--audit-angular',type=int,default=256)
    parser.add_argument('--nodes',type=int,default=151)
    parser.add_argument('--max-nodes',type=int,default=4000)
    parser.add_argument('--tol',type=float,default=2e-7)
    parser.add_argument('--bc-tol',type=float,default=2e-8)
    parser.add_argument('--restart',type=Path)
    args=parser.parse_args();install_source(args.source_root)
    from f6curve_outward_bridge_linear import read_port
    from repo_scan_gentle import scaled_port,finite_value
    from f6curve_domain_newton import install,STATS
    from curve_stable_prefix_bvp import save_checkpoint
    cfg=json.loads(args.config.read_text())
    source=read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    port=scaled_port(source,cfg['cut_radius'],cfg.get('cut_slope'),cfg.get('dimensionless_D'))
    install()
    report=dict(scope=__doc__,candidate_config=cfg,rows=[],source_hashes={})
    for name in ['repo_scan_ellipse_bvp.py','repo_scan_ellipse_core.py','repo_scan_ellipse_line.py']:
        p=Path(__file__).with_name(name);report['source_hashes'][name]=hashlib.sha256(p.read_bytes()).hexdigest()
    previous=args.restart;start=time.time()
    for aspect in args.aspects:
        row=dict(aspect=aspect,modes=args.modes,solver_success=False)
        begin=time.time();out=None
        name=f'{args.out_prefix.name}_m{args.modes}_ratio{aspect:g}'.replace('.','p')+'.json.gz'
        checkpoint=args.out_prefix.with_name(name)
        try:
            obj=EllipseBVP(cfg,port,aspect,args.modes,args.angular)
            x,y,p=obj.restart(previous) if previous else obj.seed(args.nodes)
            print(json.dumps(dict(event='start',aspect=aspect,modes=obj.M,q=obj.q,
                                  nodes=len(x),initial_parameters=p.tolist())),flush=True)
            sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,
                max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=0)
            flow=obj.flow(sol.p[0]);L=flow.end
            physical=SimpleNamespace(x=sol.x*L,y=sol.y,p=sol.p)
            physical.sol=flow.c2_interpolant(physical)
            obj.initial(sol.p)
            out=dict(scope=__doc__,config=dict(modes=obj.M,aspect=aspect,angular=args.angular,
                tol=args.tol,bc_tol=args.bc_tol),frozen_profile={**cfg,'delta':cfg['delta']+sol.p[0]},
                gauge_amplitude=obj.q,meridian_length=L,parameters=sol.p.tolist(),
                central_correction_scales=obj.pscale.tolist(),nodes=len(sol.x),
                solver_success=bool(sol.success),message=sol.message,
                max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
                newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
            out=save_checkpoint(checkpoint,out)
            summary=audit(obj,physical,201,args.audit_angular)
            out['summary']=summary;out['seconds']=time.time()-begin
            save_checkpoint(checkpoint,out)
            row.update(solver_success=bool(sol.success),message=sol.message,
                checkpoint=checkpoint.name,nodes=len(sol.x),profile_delta=cfg['delta']+sol.p[0],
                parameters=sol.p.tolist(),metric_l1=summary['metric_l1'],
                darboux_l1=summary['darboux_l1'],flow_defect=summary['flow_defect'],
                kappa_sample=summary['kappa_sample'],
                kappaD=summary['sampled_kappa_times_diagonal'],
                radius=summary['radius_max'],height=summary['height_max'],
                cylinder_diagonal=summary['reflected_prefix_cylinder_diagonal'],
                root=summary['root_min'],projection_min=summary['cylindrical_projection_min'],
                terminal_noncircle=summary['terminal_noncircle_coeff_max'],
                central_major_radius=summary['central_major_radius'],central_minor_radius=summary['central_minor_radius'],
                inlet_position_error=summary['inlet_position_error'],
                inlet_first_jet_error=summary['inlet_first_jet_error'],
                inlet_second_jet_error=summary['inlet_second_jet_error'])
            if sol.success:
                previous=checkpoint
        except Exception as exc:
            row['error']=repr(exc)
            if out is not None:
                out['audit_error']=repr(exc);save_checkpoint(checkpoint,out)
        row['seconds']=time.time()-begin
        report['rows'].append(finite_value(row));report['elapsed_seconds']=time.time()-start
        args.out_prefix.with_name(args.out_prefix.name+'_summary.json').write_text(
            json.dumps(finite_value(report),indent=2,allow_nan=False)+'\n')
        print(json.dumps(finite_value(dict(event='result',**row))),flush=True)
        if not row['solver_success']:
            break


if __name__=='__main__':
    main()
