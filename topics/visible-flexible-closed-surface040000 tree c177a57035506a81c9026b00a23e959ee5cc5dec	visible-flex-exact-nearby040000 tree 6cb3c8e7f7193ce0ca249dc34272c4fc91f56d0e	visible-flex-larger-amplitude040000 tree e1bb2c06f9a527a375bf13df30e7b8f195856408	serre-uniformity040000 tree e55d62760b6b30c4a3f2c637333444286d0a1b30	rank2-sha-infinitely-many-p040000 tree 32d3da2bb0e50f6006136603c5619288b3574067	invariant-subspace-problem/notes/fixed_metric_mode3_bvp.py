#!/usr/bin/env python3
"""Planar mode3 support-core Frenet prefix with a recorded actual physical port.

Design mode fixes q and varies delta plus higher support coefficients.
Fixed mode freezes the entire meridian profile and varies q plus higher
support coefficients. Neither a finite linear port nor a finite nonlinear
DN is an exact rotational collar. No closed-surface claim is made.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
os.environ.setdefault('NODE_OPTIONS','--max-old-space-size=384')
import argparse,hashlib,json,math,sys,time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from fixed_metric_mode3_core import PlanarSupportCore
from repo_scan_gentle import finite_value

def install_source(root):
    sys.path.insert(0,str(Path(root)/'topics/large-amplitude-twist-flex/scripts'))

def merge_profile_mesh(points,breaks):
    """Keep exact physical break locations and avoid floating near-duplicates."""
    points=np.asarray(points,float);breaks=np.asarray(breaks,float)
    points=points[(points>=-1e-12)&(points<=1+1e-12)]
    for b in breaks:points=points[abs(points-b)>2e-11]
    trial=np.sort(np.r_[points,breaks]);return trial[np.r_[True,np.diff(trial)>2e-12]]

class SupportBVP:
    def __init__(self,cfg,port,support_amplitude=.001,modes=4,angular=128,base_mode=3,fixed=False,core_kind='support'):
        from f6curve_bidirectional_bridge import DirectionalBridge
        from fixed_metric_mode3_flow import PlanarSymmetryFlow
        self.cfg=dict(cfg);self.port=port;self.M=int(modes);self.base_mode=int(base_mode);self.fixed=bool(fixed);self.core_kind=core_kind
        if core_kind not in ('support','tangent'):raise ValueError('Unknown planar core kind')
        if len(port['linearSlope'])<self.M:raise ValueError('Actual physical port has too few modes')
        if port.get('modes',list(self.base_mode*np.arange(1,self.M+1)))[:self.M]!=list(self.base_mode*np.arange(1,self.M+1)):
            raise ValueError('Physical linear port frequencies do not match the core basis')
        self.q=float(support_amplitude);self.seed_support_amplitude=self.q;self.support_amplitude=self.q
        if not 0<self.q<.2:raise ValueError('Positive support seed amplitude below .2 required')
        self.n=3*self.M+1;self.iz=2*self.M+1;self.nt=max(int(angular),8*(self.base_mode*self.M+1))
        self.bridge=DirectionalBridge(port['cut']);self.Flow=PlanarSymmetryFlow
        if self.core_kind=='tangent':
            self.pscale=np.array([max(((self.base_mode**2-1)*self.q)**j/(j*j),1e-10)for j in range(2,self.M+1)])
        else:self.pscale=np.array([max(self.q**j,1e-10)for j in range(2,self.M+1)])
        self.bcweights=np.maximum(self.q**np.arange(1,self.M+1),1e-8)
        self._flow_key=None;self._flow=None;self._core_key=None;self._core=None;self._initial=None;self._inlet_metrics=None;self._initial_jac=None
        self.fixed_flow=self.Flow(self.cfg,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge) if self.fixed else None
        reference=self.fixed_flow if self.fixed else self.Flow(self.cfg,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)
        self.chart_reference_prefix=reference.prefix_end
        self.chart_join=reference.prefix_end/reference.end
        self.chart_breaks=np.unique(np.r_[reference.breakpoints/reference.prefix_end*self.chart_join,1.])

    def flow(self,p0):
        if self.fixed:return self.fixed_flow
        p0=float(p0)
        if self._flow_key!=p0:
            delta=self.cfg['delta']+p0
            if not .002<delta<2:raise FloatingPointError('Excursion outside design domain')
            self._flow=self.Flow({**self.cfg,'delta':delta},self.port,self.M,self.q,self.nt,self.base_mode,self.bridge);self._flow_key=p0
        return self._flow

    def initial(self,p):
        key=tuple(np.asarray(p,float)) if self.fixed else tuple(np.asarray(p[1:],float))
        if key!=self._core_key:
            q=self.seed_support_amplitude*math.exp(float(p[0])) if self.fixed else self.seed_support_amplitude
            if not 1e-7<q<.2:raise FloatingPointError('Extrinsic support amplitude left search domain')
            if self.core_kind=='tangent':
                from fixed_metric_mode3_tangent_core import PlanarTangentCore
                core=PlanarTangentCore(q,np.asarray(p[1:])*self.pscale,self.base_mode)
            else:core=PlanarSupportCore(q,np.asarray(p[1:])*self.pscale,self.base_mode)
            flow=self.flow(p[0]);N=max(2048,64*self.M);C,metrics=core.inlet(flow,N)
            self._initial=(C-flow.base(np.array([0.]))[:,0])/self.q
            if hasattr(core,'inlet_jacobian'):J=core.inlet_jacobian(flow)
            else:
                theta=2*np.pi*np.arange(N)/N;B,_,_=flow.basis(N)
                derivatives=core.parameter_derivatives(theta);J=flow.project(derivatives,B)
            self._initial_jac=np.zeros((self.n,self.M))
            if self.fixed:self._initial_jac[:,0]=q*J[:,0]/self.q
            if self.M>1:self._initial_jac[:,1:]=J[:,1:]*self.pscale[None,:]/self.q
            self._core=core;self._inlet_metrics=metrics;self._core_key=key;self.support_amplitude=q
        return self._initial

    def chart(self,t,p0):
        """Smooth numerical coordinate that fixes every physical profile break."""
        flow=self.flow(p0);t=np.asarray(t,float);join=self.chart_join;a=flow.prefix_end/self.chart_reference_prefix
        if not 0<a<2.:raise FloatingPointError('Design excursion left the smooth chart range')
        u=np.clip((t-join)/(1-join),0.,1.);S=u**3*(10-15*u+6*u*u);Sp=30*u*u*(1-u)**2
        s=np.where(t<=join,t*flow.prefix_end/join,flow.prefix_end+self.bridge.L*(a*u+(1-a)*S))
        ds=np.where(t<=join,flow.prefix_end/join,self.bridge.L/(1-join)*(a+(1-a)*Sp))
        return s,ds

    def inverse_chart(self,s,p0):
        flow=self.flow(p0);s=np.asarray(s,float);a=flow.prefix_end/self.chart_reference_prefix
        target=np.clip((s-flow.prefix_end)/self.bridge.L,0.,1.);u=target.copy()
        for _ in range(12):
            S=u**3*(10-15*u+6*u*u);Sp=30*u*u*(1-u)**2
            d=(a*u+(1-a)*S-target)/(a+(1-a)*Sp);u-=d
            if np.max(abs(d))<2e-15:break
        check=a*u+(1-a)*u**3*(10-15*u+6*u*u)-target
        if float(abs(check).max())>2e-13:raise FloatingPointError('Numerical chart inversion did not converge')
        return np.where(s<=flow.prefix_end,s*self.chart_join/flow.prefix_end,self.chart_join+(1-self.chart_join)*u)

    def fun(self,t,y,p):
        flow=self.flow(p[0]);s,ds=self.chart(t,p[0])
        return ds[None,:]*flow.fun(s,y,p)

    def fun_jac(self,t,y,p):
        flow=self.flow(p[0]);s,ds=self.chart(t,p[0]);J,_=flow.fun_jac(s,y,p)
        PJ=np.zeros((self.n,self.M,len(t)))
        if not self.fixed:
            step=2e-6*max(.1,self.cfg['delta']+p[0]);plus=p.copy();minus=p.copy();plus[0]+=step;minus[0]-=step
            PJ[:,0,:]=(self.fun(t,y,plus)-self.fun(t,y,minus))/(2*step)
            self.flow(p[0])
        return ds[None,None,:]*J,PJ

    def terminal(self,y,p):
        flow=self.flow(p[0]);dy=flow.fun(np.array([flow.end]),y.astype(np.longdouble)[:,None],p)[:,0]
        D=np.asarray(self.port['linearSlope'][:self.M])
        return np.asarray(self.q*(dy[self.iz:]-self.bridge.sigma*D*y[self.iz:]/math.sqrt(self.port['cut']['E']))/self.bcweights,float)

    def bc(self,ya,yb,p):return np.r_[ya-self.initial(p),self.terminal(yb,p)]

    def bc_jac(self,ya,yb,p):
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n);B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        self.initial(p);P[:self.n]=-self._initial_jac
        flow=self.flow(p[0]);J,_=flow.fun_jac(np.array([flow.end]),yb.astype(np.longdouble)[:,None],p)
        T=self.q*J[self.iz:,:,0];D=np.asarray(self.port['linearSlope'][:self.M])
        T[:,self.iz:]-=self.q*self.bridge.sigma*np.diag(D)/math.sqrt(self.port['cut']['E'])
        B[self.n:]=T/self.bcweights[:,None]
        return A,B,P

    def seed(self,nodes):
        flow=self.flow(0);line=flow.backward_line();t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks);s,_=self.chart(t,0);fg=np.empty((2,len(s)))
        for j,(lo,hi,solution,scale) in enumerate(line.segments):
            mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
            if np.any(mask):fg[:,mask]=solution(s[mask])*math.exp(scale-line.logscale)/line.core[0]
        y=np.zeros((self.n,len(s)));y[1]=fg[0];y[self.M+1]=-fg[0]/self.base_mode;y[self.iz]=fg[1]
        p=np.zeros(self.M);difference=self.initial(p)-y[:,0]
        cutoff=(flow.Tu if flow.direction=='outward' else flow.Td)/2
        y+=difference[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
        return t,y,p

    def restart(self,path):
        from curve_stable_prefix_bvp import load_checkpoint
        old=load_checkpoint(path);M0=old['config']['modes'];q0=old['gauge_amplitude'];qa=old.get('actual_primary_amplitude',old.get('actual_support_amplitude'))
        if old['config'].get('core_kind','support')!=self.core_kind:raise ValueError('Restart core family differs')
        if old['config']['base_mode']!=self.base_mode:raise ValueError('Restart symmetry differs')
        if old['physical_port_sha256']!=self.port['_sha256']:
            if old.get('physical_tail_parameters')!=self.port['parameters'] or old.get('physical_tail_cut')!=self.port['cut']:
                raise ValueError('Restart actual physical tail metric differs')
        p=np.zeros(self.M)
        if self.fixed:
            if old['frozen_profile']!=self.cfg:raise ValueError('Restart metric differs from frozen metric')
            p[0]=math.log(qa/self.seed_support_amplitude);ratio=1.
        else:
            p[0]=old['frozen_profile']['delta']-self.cfg['delta'];ratio=self.seed_support_amplitude/qa
        oldscale=np.asarray(old['central_correction_scales'])
        for j in range(1,min(M0,self.M)):
            p[j]=old['parameters'][j]*oldscale[j-1]*ratio**(j+1)/self.pscale[j-1]
        flow=self.flow(p[0]);L=old['meridian_length']
        if self.fixed and L!=flow.end:raise ValueError('Restart meridian length differs')
        ox=np.asarray(old['mesh']);op=PPoly.construct_fast(np.asarray(old['pp_coefficients']),ox,extrapolate=True,axis=1)
        mesh_source=np.linspace(0,1,self.restart_remesh) if getattr(self,'restart_remesh',0)>2 else self.inverse_chart(ox,p[0])
        t=merge_profile_mesh(mesh_source,self.chart_breaks);sphysical,_=self.chart(t,p[0]);oy=op(sphysical);y=np.zeros((self.n,len(t)))
        y[0]=oy[0]*q0/self.q*(ratio**2 if not self.fixed else 1)
        for j in range(min(M0,self.M)):
            factor=q0/self.q*(ratio**(j+1)if not self.fixed else 1)
            for ni,oi in [(1+j,1+j),(self.M+1+j,M0+1+j),(self.iz+j,2*M0+1+j)]:y[ni]=factor*oy[oi]
        return t,y,p


def audit(obj,sol,points=201,angular=256):
    angular=max(int(angular),8*(obj.base_mode*obj.M+1))
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
        actual_support_amplitude=obj.support_amplitude,core_summary=core.summary(),
        central_curvature_min=core.minimum_sampled_curvature,
        central_curvature_max=core.maximum_sampled_curvature,
        central_corrections=list(core.corrections),inlet_projection_diagnostics=obj._inlet_metrics,
        meridian_length=flow.end,
        scope='Actual C2 finite-prefix map sampled in s, whole-angle polynomial l1 metric/Darboux diagnostics. The finite recorded port is not a circular collar; no closed-surface assertion.')
    result['sampled_kappa_times_diagonal']=result['kappa_sample']*result['reflected_prefix_cylinder_diagonal']
    if obj.core_kind=='tangent':result['actual_tangent_q_eff']=result.pop('actual_support_amplitude')
    result['core_kind']=obj.core_kind
    return result



def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--linear-port',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--amplitudes',nargs='+',type=float,default=[.001,.003,.01]);p.add_argument('--modes',type=int,default=4)
    p.add_argument('--core',choices=['support','tangent'],default='support');p.add_argument('--angular',type=int,default=128);p.add_argument('--audit-angular',type=int,default=256);p.add_argument('--nodes',type=int,default=101)
    p.add_argument('--physical-bc-tol',type=float);p.add_argument('--max-nodes',type=int,default=2400);p.add_argument('--tol',type=float,default=2e-7);p.add_argument('--bc-tol',type=float,default=2e-8)
    p.add_argument('--fixed',action='store_true');p.add_argument('--restart',type=Path);p.add_argument('--restart-remesh',type=int,default=0);p.add_argument('--tail-config',type=Path)
    a=p.parse_args();install_source(a.source_root)
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install,STATS
    cfg=json.loads(a.profile.read_text());port=json.loads(a.linear_port.read_text());port['_sha256']=hashlib.sha256(a.linear_port.read_bytes()).hexdigest()
    if a.fixed and len(a.amplitudes)!=1:raise ValueError('One seed amplitude only in fixed-metric mode')
    if a.tail_config:
        from fixed_metric_actual_tail_bvp import ActualTailMixin
        from fixed_metric_cut_tail_port import CutPreservingTailPort
        class ActualSupportBVP(ActualTailMixin,SupportBVP):pass
        cls=ActualSupportBVP
    else:cls=SupportBVP
    report=dict(scope=__doc__,core_kind=a.core,fixed_metric=a.fixed,source_profile=cfg,physical_port=port,rows=[])
    code_files=['fixed_metric_mode3_bvp.py','fixed_metric_mode3_flow.py','fixed_metric_mode3_core.py','fixed_metric_mode3_tangent_core.py']
    code_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()for name in code_files}
    report['code_sha256']=code_sha256
    previous=a.restart;begin=time.time();install()
    for q in a.amplitudes:
        start=time.time();row=dict(requested_primary_amplitude=q,core_kind=a.core,modes=a.modes,solver_success=False);tail=None
        name=a.out_prefix.name+f'_m{a.modes}_q{q:g}'.replace('.','p');checkpoint=a.out_prefix.with_name(name+'.json.gz')
        try:
            obj=cls(cfg,port,q,a.modes,a.angular,3,a.fixed,a.core);obj.restart_remesh=a.restart_remesh
            if a.physical_bc_tol is not None:
                if a.physical_bc_tol<=0:raise ValueError('Positive physical boundary tolerance required')
                obj.bcweights=np.full(obj.M,a.physical_bc_tol/a.bc_tol)
            if a.tail_config:
                tailcfg=json.loads(a.tail_config.read_text())
                for key,value in port['parameters'].items():
                    if tailcfg.get(key)!=value:raise ValueError('Nonlinear tail physical parameter mismatch: '+key)
                if tailcfg['modes']!=a.modes or tailcfg['spacing']!=3:raise ValueError('Nonlinear tail basis mismatch')
                tail=CutPreservingTailPort(a.tail_config,a.source_root,a.out_prefix.with_name(name+'_tail'))
                if not np.allclose(tail.linearD,port['linearSlope'][:a.modes],rtol=2e-5,atol=1e-8):raise ValueError('Actual tail linear DN mismatch')
                obj.tail=tail
            x,y,v=obj.restart(previous)if previous else obj.seed(a.nodes)
            print(json.dumps(dict(event='start',q=q,M=a.modes,mesh=len(x),fixed=a.fixed,delta=obj.flow(v[0]).delta,nonlinear_tail=bool(tail))),flush=True)
            sol=solve_bvp(obj.fun,obj.bc,x,y,v,tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac)
            flow=obj.flow(sol.p[0]);L=flow.end;obj.initial(sol.p)
            physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=flow.c2_interpolant(physical)
            frozen=cfg if a.fixed else {**cfg,'delta':cfg['delta']+sol.p[0]}
            out=dict(scope=__doc__,code_sha256=code_sha256,config=dict(modes=a.modes,base_mode=3,core_kind=a.core,flow_arithmetic=flow.arithmetic,computational_chart='prefix-scaled-smooth-bridge-v1',primary_seed=q,angular=obj.nt,tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,fixed_metric=a.fixed),
                frozen_profile=frozen,gauge_amplitude=obj.q,actual_primary_amplitude=obj.support_amplitude,meridian_length=L,
                physical_port_sha256=port['_sha256'],physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),
                nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals)),
                newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
            out['bc_weights']=obj.bcweights.tolist()
            out=save_checkpoint(checkpoint,out);out['summary']=audit(obj,physical,151,a.audit_angular)
            if tail:out['tail_seam']=obj.tail_seam_audit(physical)
            out['seconds']=time.time()-start;save_checkpoint(checkpoint,out)
            row.update(solver_success=bool(sol.success),message=sol.message,checkpoint=checkpoint.name,nodes=len(sol.x),delta=frozen['delta'],
                parameters=sol.p.tolist(),bc_max=float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max()),**out['summary'])
            physical_bc=obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights
            row['bc_physical_components']=physical_bc.tolist();row['bc_physical_max']=float(abs(physical_bc).max());row['bc_weights']=obj.bcweights.tolist()
            if tail:row['tail_seam']={k:v for k,v in out['tail_seam'].items()if k!='response'}
            if sol.success:previous=checkpoint
        except Exception as e:row['error']=repr(e)
        finally:
            if tail:tail.close()
        row['seconds']=time.time()-start;report['rows'].append(finite_value(row));report['seconds']=time.time()-begin
        a.out_prefix.with_name(a.out_prefix.name+'_summary.json').write_text(json.dumps(finite_value(report),indent=2)+'\n')
        print(json.dumps({k:v for k,v in finite_value(row).items()if k in ['requested_primary_amplitude','solver_success','delta','metric_l1','flow_defect','darboux_l1','kappa_sample','root_min','height_max','terminal_height_max','nodes','error','seconds']}),flush=True)
        if not row['solver_success']:break

if __name__=='__main__':main()
