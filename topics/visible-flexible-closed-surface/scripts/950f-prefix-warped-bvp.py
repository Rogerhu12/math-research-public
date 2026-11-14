#!/usr/bin/env python3
"""Fixed angular-chart Frenet prefix. This is a finite-port numerical experiment.

The material angle is theta(psi)=psi-e*sin(3psi)/3, e=8*q_reference.
The exact round background a(s)*exp(i*theta(psi)) is never truncated.
Only its perturbation is represented in a Fourier basis in psi. The physical
metric remains ds^2+a(s)^2*dtheta^2. The tail DN is conjugated from theta
Fourier coordinates; its finite physical-mode cutoff is recorded separately.
No closed-surface, infinite-tail, or reach assertion is made.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,json,math,sys,time,types
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly

HERE=Path(__file__).resolve().parent
NOTES=HERE.parent/'notes'
sys.path.insert(0,str(NOTES))

def install_source(root):
    sys.path.insert(0,str(Path(root)/'topics/large-amplitude-twist-flex/scripts'))


def build_classes():
    from fixed_metric_mode3_flow import PlanarSymmetryFlow
    from fixed_metric_mode3_bvp import SupportBVP,merge_profile_mesh
    from fixed_metric_mode3_core import PlanarSupportCore
    from curve_stable_prefix_bvp import CylindricalPrefix,load_checkpoint

    class WarpedFlow(PlanarSymmetryFlow):
        def __init__(self,*args,warp_q=.08,**kwargs):
            self.warp_e=8*float(warp_q);self.background_cache={}
            if not 0<=self.warp_e<1:raise ValueError('The fixed angle map must be invertible')
            super().__init__(*args,**kwargs)
            self.fun=types.MethodType(WarpedFlow.warp_fun,self)
            self.fun_jac=types.MethodType(WarpedFlow.warp_fun_jac,self)
            self.c2_interpolant=types.MethodType(WarpedFlow.warp_c2_interpolant,self)
            self.arithmetic='long-double-exact-warped-background'
        def angular(self,N):
            if N not in self.background_cache:
                psi=2*np.pi*np.arange(N)/N;e=self.warp_e
                theta=psi-e*np.sin(3*psi)/3;rho=1-e*np.cos(3*psi);rho1=3*e*np.sin(3*psi)
                z=np.exp(1j*theta);z1=1j*rho*z;z2=(1j*rho1-rho*rho)*z
                vec=lambda a:np.stack((a.real,a.imag,np.zeros_like(a.real)),axis=-1)
                self.background_cache[N]=(psi,theta,rho,rho1,vec(z),vec(z1),vec(z2))
            return self.background_cache[N]
        def base(self,s,derivative=0):return np.zeros((self.n,len(np.atleast_1d(s))))
        def physical_base(self,s,N,derivative=0):
            a=self.profile(s)[derivative]
            return a[:,None,None]*self.angular(N)[4][None,:,:]
        def frame(self,s,C,B1=None,B2=None):
            B1=self.B1 if B1 is None else B1;B2=self.B2 if B2 is None else B2
            a,ap,app=self.profile(s);Npts=B1.shape[1];ang=self.angular(Npts)
            d=self.values(C,B1)+a[:,None,None]*ang[5][None,:,:]
            dd=self.values(C,B2)+a[:,None,None]*ang[6][None,:,:]
            lam=np.sqrt(np.sum(d*d,axis=2));T=d/lam[:,:,None]
            dt=np.sum(dd*T,axis=2);nvec=dd-dt[:,:,None]*T;nn=np.sqrt(np.sum(nvec*nvec,axis=2))
            N=nvec/nn[:,:,None];kap=nn/lam**2;Bin=np.cross(T,N)
            alpha=-ap[:,None]/(a[:,None]*kap);margin=1-alpha**2
            if np.min(margin.real)<=0 or np.min(lam.real)<=0 or np.min(nn.real)<=0:raise FloatingPointError('Warped Frenet domain failure: '+str(np.min(margin.real)))
            beta=np.sqrt(margin);V=alpha[:,:,None]*N+beta[:,:,None]*Bin
            return dict(d=d,dd=dd,lam=lam,T=T,dt=dt,nn=nn,N=N,kap=kap,Bin=Bin,a=a,ap=ap,app=app,alpha=alpha,beta=beta,margin=margin,V=V)
        def warp_fun(self,s,y,p):
            s=np.asarray(s);out=np.empty(y.shape,dtype=y.dtype);self.calls+=1
            for first in range(0,len(s),64):
                sl=slice(first,first+64);yy=np.asarray(y[:,sl],np.clongdouble if np.iscomplexobj(y)else np.longdouble)
                fr=self.frame(s[sl],self.q*yy);V=fr['V']-self.physical_base(s[sl],self.nt,1)
                out[:,sl]=np.asarray(self.project(V,self.B)/self.q,dtype=y.dtype)
            return out
        def warp_fun_jac(self,s,y,p):
            s=np.asarray(s);out=np.empty((self.n,self.n,len(s)))
            for first in range(0,len(s),64):
                sl=slice(first,first+64);fr=self.frame(s[sl],self.q*y[:,sl])
                for j in range(self.n):
                    dv=self.frame_jvp(fr,self.B1[j][None,:,:],self.B2[j][None,:,:]);out[:,j,sl]=self.project(dv,self.B)
            return out,np.zeros((self.n,self.M,len(s)))
        def warp_c2_interpolant(self,sol):
            s=sol.x;y=np.asarray(sol.y,np.longdouble);dy=self.warp_fun(s,y,sol.p);ddy=np.empty_like(y)
            for first in range(0,len(s),64):
                sl=slice(first,first+64);t=s[sl];fr=self.frame(t,self.q*y[:,sl]);ang=self.angular(self.nt)
                d1=self.q*self.values(dy[:,sl],self.B1)+fr['ap'][:,None,None]*ang[5][None,:,:]
                d2=self.q*self.values(dy[:,sl],self.B2)+fr['ap'][:,None,None]*ang[6][None,:,:]
                dV=self.frame_jvp(fr,d1,d2)
                ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap'])
                be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
                dV-=self.physical_base(t,self.nt,2);ddy[:,sl]=self.project(dV,self.B)/self.q
            Y=y.T;D=dy.T;Q=ddy.T;h=np.diff(s).astype(np.longdouble)[:,None]
            e0=Y[1:]-Y[:-1]-h*D[:-1]-h*h*Q[:-1]/2;e1=D[1:]-D[:-1]-h*Q[:-1];e2=Q[1:]-Q[:-1]
            u=10*e0-4*h*e1+h*h*e2/2;v=-15*e0+7*h*e1-h*h*e2;w=6*e0-3*h*e1+h*h*e2/2
            c=np.stack((w/h**5,v/h**4,u/h**3,Q[:-1]/2,D[:-1],Y[:-1])).astype(float)
            return PPoly.construct_fast(c,s,extrapolate=True,axis=1)

    class WarpedBVP(SupportBVP):
        def __init__(self,cfg,port,q=.08,M=8,angular=256,fixed=False,warp_q=.08):
            # Parent setup requires a type with the same established interface.
            self.warp_q=float(warp_q)
            super().__init__(cfg,port,q,M,angular,3,fixed,'support')
            self.Flow=lambda *a,**kw:WarpedFlow(*a,warp_q=self.warp_q,**kw)
            self._flow_key=None;self._flow=None
            self.fixed_flow=self.Flow(self.cfg,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge) if self.fixed else None
            self.Dmatrix,self.Dmatrix_diagnostics=self.make_dn_matrix(port['linearSlope'])
            self.pscale=np.maximum(q**np.arange(2,M+1),1e-9)
        def make_dn_matrix(self,D):
            K=len(D);N=max(4096,128*(K+self.M));flow=self.flow(0);_,theta,rho,*_=flow.angular(N)
            psi=2*np.pi*np.arange(N)/N;physical=np.cos(np.arange(1,K+1)[:,None]*3*theta)
            warped=np.cos(np.arange(1,self.M+1)[:,None]*3*psi)
            to_physical=2/N*np.einsum('kp,jp,p->kj',physical,warped,rho)
            from_physical=2/N*(warped@physical.T)
            mat=(from_physical*np.asarray(D)[None,:])@to_physical
            half=(from_physical[:,:K//2]*np.asarray(D[:K//2])[None,:])@to_physical[:K//2]
            return mat,dict(physical_modes=K,psi_modes=self.M,quadrature=N,half_cutoff_matrix_difference=float(abs(mat-half).max()))
        def initial(self,p):
            key=tuple(np.asarray(p,float))if self.fixed else tuple(np.asarray(p[1:],float))
            if key!=self._core_key:
                q=self.seed_support_amplitude*math.exp(float(p[0]))if self.fixed else self.seed_support_amplitude
                if not 1e-7<q<.124:raise FloatingPointError('Support amplitude left positive search domain')
                core=PlanarSupportCore(q,np.asarray(p[1:])*self.pscale,3)
                flow=self.flow(p[0]);N=max(2048,128*self.M);ang=flow.angular(N);B,B1,B2=flow.basis(N);g=core.evaluate(ang[1])
                self._initial=flow.project((g['F']-ang[4])[None,:,:],B)[:,0]/self.q
                deriv=core.parameter_derivatives(ang[1]);J=flow.project(deriv,B)
                self._initial_jac=np.zeros((self.n,self.M))
                if self.fixed:self._initial_jac[:,0]=q*J[:,0]/self.q
                self._initial_jac[:,1:]=J[:,1:]*self.pscale[None,:]/self.q
                mapped=flow.values((self.q*self._initial)[:,None],B)[0]+ang[4]
                first=flow.values((self.q*self._initial)[:,None],B1)[0]+ang[5]
                second=flow.values((self.q*self._initial)[:,None],B2)[0]+ang[6]
                exactfirst=g['Ft']*ang[2][:,None]
                exactsecond=g['Ftt']*ang[2][:,None]**2+g['Ft']*ang[3][:,None]
                metric=np.sum(first*first,axis=1)/ang[2]**2-1
                self._inlet_metrics=dict(position=float(np.linalg.norm(mapped-g['F'],axis=1).max()),first=float(np.linalg.norm(first-exactfirst,axis=1).max()),second=float(np.linalg.norm(second-exactsecond,axis=1).max()),metric_l1=float(np.sum(abs(np.fft.fft(metric)/N))))
                self._core=core;self._core_key=key;self.support_amplitude=q
            return self._initial
        def terminal(self,y,p):
            flow=self.flow(p[0]);dy=flow.fun(np.array([flow.end]),y.astype(np.longdouble)[:,None],p)[:,0]
            return np.asarray(self.q*(dy[self.iz:]-self.bridge.sigma*(self.Dmatrix@y[self.iz:])/math.sqrt(self.port['cut']['E']))/self.bcweights,float)
        def bc_jac(self,ya,yb,p):
            A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n);B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
            self.initial(p);P[:self.n]=-self._initial_jac
            flow=self.flow(p[0]);J,_=flow.fun_jac(np.array([flow.end]),yb.astype(np.longdouble)[:,None],p)
            T=self.q*J[self.iz:,:,0];T[:,self.iz:]-=self.q*self.bridge.sigma*self.Dmatrix/math.sqrt(self.port['cut']['E'])
            B[self.n:]=T/self.bcweights[:,None];return A,B,P
        def seed(self,nodes):
            flow=self.flow(0);line=flow.backward_line();t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks);s,_=self.chart(t,0)
            fg=np.empty((2,len(s)))
            for j,(lo,hi,sol,scale)in enumerate(line.segments):
                mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
                if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
            N=max(2048,64*self.M);ang=flow.angular(N);theta=ang[1];er=ang[4];et=np.c_[-er[:,1],er[:,0],np.zeros(N)]
            fshape=np.cos(3*theta)[:,None]*er-np.sin(3*theta)[:,None]*et/3
            zshape=np.c_[np.zeros(N),np.zeros(N),np.cos(3*theta)]
            B,_,_=flow.basis(N);c=flow.project(np.stack((fshape,zshape)),B)
            y=c[:,0,None]*fg[0]+c[:,1,None]*fg[1];p=np.zeros(self.M)
            difference=self.initial(p)-y[:,0];cutoff=(flow.Tu if flow.direction=='outward'else flow.Td)/2
            y+=difference[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
            return t,y,p
        def restart(self,path):
            old=load_checkpoint(path)
            if old.get('warp_reference_q')!=self.warp_q:raise ValueError('Restart angle chart differs')
            if old['physical_tail_parameters']!=self.port['parameters']or old['physical_tail_cut']!=self.port['cut']:raise ValueError('Restart physical port metric differs')
            M0=old['config']['modes'];q0=old['gauge_amplitude'];qa=old['actual_primary_amplitude'];p=np.zeros(self.M)
            if self.fixed:
                if old['frozen_profile']!=self.cfg:raise ValueError('Restart metric differs')
                p[0]=math.log(qa/self.seed_support_amplitude);ratio=1
            else:p[0]=old['frozen_profile']['delta']-self.cfg['delta'];ratio=self.q/qa
            for j in range(1,min(M0,self.M)):p[j]=old['parameters'][j]*old['central_correction_scales'][j-1]*ratio**(j+1)/self.pscale[j-1]
            flow=self.flow(p[0]);ox=np.asarray(old['mesh']);pp=PPoly.construct_fast(np.asarray(old['pp_coefficients']),ox,extrapolate=True,axis=1)
            t=merge_profile_mesh(np.linspace(0,1,self.restart_remesh),self.chart_breaks);s,_=self.chart(t,p[0]);oy=pp(s);y=np.zeros((self.n,len(t)))
            y[0]=oy[0]*q0/self.q
            for j in range(min(M0,self.M)):
                for ni,oi in [(1+j,1+j),(self.M+1+j,M0+1+j),(self.iz+j,2*M0+1+j)]:y[ni]=oy[oi]*q0/self.q*ratio
            return t,y,p
    return WarpedFlow,WarpedBVP


def audit(obj,sol,N=512):
    flow=obj.flow(sol.p[0]);obj.initial(sol.p);N=max(N,16*(obj.M*3+1))
    B,B1,B2=flow.basis(N);ang=flow.angular(N);rho=ang[2];rho1=ang[3]
    ss=np.unique(np.r_[np.linspace(0,flow.end,151),sol.x,(sol.x[:-1]+sol.x[1:])/2])
    hh=flow.height_integral(sol,ss,N,6)
    out=dict(metric_l1=0.,flow_defect=0.,darboux_l1=0.,kappa_sample=0.,radius_max=0.,height_max=0.,root_min=1.,support_amplitude=obj.support_amplitude)
    for first in range(0,len(ss),32):
        s=ss[first:first+32];Y=sol.sol(s);Yp=sol.sol(s,1);Ypp=sol.sol(s,2);a,ap,app=flow.profile(s);fr=flow.frame(s,obj.q*Y,B1,B2)
        Fs=flow.physical_base(s,N,1)+obj.q*flow.values(Yp,B);Fs[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fsp=ap[:,None,None]*ang[5][None,:,:]+obj.q*flow.values(Yp,B1)
        Fspp=ap[:,None,None]*ang[6][None,:,:]+obj.q*flow.values(Yp,B2)
        dV=flow.frame_jvp(fr,Fsp,Fspp);ae=-app[:,None]/(a[:,None]*fr['kap'])+ap[:,None]**2/(a[:,None]**2*fr['kap']);be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        Fss=flow.physical_base(s,N,2)+obj.q*flow.values(Ypp,B);Fss[:,:,2]+=np.mean(dV[:,:,2],axis=1)[:,None]
        Ft=fr['d']/rho[None,:,None];Ftt=fr['dd']/rho[None,:,None]**2-fr['d']*rho1[None,:,None]/rho[None,:,None]**3;Fst=Fsp/rho[None,:,None]
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/a[:,None],G/a[:,None]**2-1),axis=2)
        out['metric_l1']=max(out['metric_l1'],float(np.max(np.sum(abs(np.fft.fft(errors,axis=1)/N),axis=1))))
        out['flow_defect']=max(out['flow_defect'],float(np.linalg.norm(Fs-fr['V'],axis=2).max()))
        nn=np.cross(Fs,Ft);nn/=np.linalg.norm(nn,axis=2)[:,:,None]
        L=np.sum(Fss*nn,axis=2);M=np.sum(Fst*nn,axis=2);NN=np.sum(Ftt*nn,axis=2);detI=E*G-F*F;tr=(L*G-2*M*F+NN*E)/detI;detII=(L*NN-M*M)/detI
        kap=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*detII)))/2
        Hst=(Fst-ap[:,None,None]/a[:,None,None]*Ft)/a[:,None,None]
        Htt=(Ftt+(a*ap)[:,None,None]*Fs)/a[:,None,None]**2
        gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-(Ft/a[:,None,None])[:,:,:,None]*(Ft/a[:,None,None])[:,:,None,:]
        tensor=.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]+(app/a)[:,None,None,None]*gram
        ft=np.fft.fft(tensor,axis=1)/N
        out['darboux_l1']=max(out['darboux_l1'],float(np.max(np.sum(np.sqrt(np.sum(abs(ft)**2,axis=(2,3))),axis=1))))
        pos=flow.physical_base(s,N,0)+obj.q*flow.values(Y,B);pos[:,:,2]+=hh[first:first+len(s),None]
        out['kappa_sample']=max(out['kappa_sample'],float(kap.max()));out['root_min']=min(out['root_min'],float(fr['margin'].min()))
        out['radius_max']=max(out['radius_max'],float(np.linalg.norm(pos[:,:,:2],axis=2).max()));out['height_max']=max(out['height_max'],float(abs(pos[:,:,2]).max()))
    out['core']=obj._core.summary();out['inlet']=obj._inlet_metrics;out['dn_matrix']=obj.Dmatrix_diagnostics
    out['terminal_height_psi_coeff_max']=float(obj.q*abs(sol.y[obj.iz:,-1]).max());out['physical_bc_max']=float(abs(obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights).max())
    out['samples_s']=len(ss);out['samples_psi']=N
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--profile',type=Path,required=True);p.add_argument('--linear-port',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--amplitude',type=float,default=.08);p.add_argument('--warp-reference',type=float,default=.08);p.add_argument('--modes',type=int,default=8);p.add_argument('--angular',type=int,default=256);p.add_argument('--audit-angular',type=int,default=512)
    p.add_argument('--nodes',type=int,default=301);p.add_argument('--max-nodes',type=int,default=1200);p.add_argument('--tol',type=float,default=2e-7);p.add_argument('--bc-tol',type=float,default=1e-8);p.add_argument('--physical-bc-tol',type=float,default=1e-10)
    p.add_argument('--fixed',action='store_true');p.add_argument('--restart',type=Path);p.add_argument('--check-only',action='store_true');a=p.parse_args();install_source(a.source_root)
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install,STATS
    _,BVP=build_classes();cfg=json.loads(a.profile.read_text());port=json.loads(a.linear_port.read_text());port['_sha256']=hashlib.sha256(a.linear_port.read_bytes()).hexdigest()
    obj=BVP(cfg,port,a.amplitude,a.modes,a.angular,a.fixed,a.warp_reference);obj.restart_remesh=a.nodes;obj.bcweights=np.full(obj.M,a.physical_bc_tol/a.bc_tol)
    x,y,par=obj.restart(a.restart)if a.restart else obj.seed(a.nodes)
    if a.check_only:
        flow=obj.flow(par[0]);rng=np.random.default_rng(20261109);s=np.linspace(.001,flow.end,7);Y=np.zeros((obj.n,len(s)));Y[1]=.001;vec=rng.normal(size=Y.shape);J=flow.fun_jac(s,Y,par)[0];cs=flow.fun(s,Y.astype(complex)+1e-25j*vec,par).imag/1e-25;pred=np.einsum('ijk,jk->ik',J,vec)
        checks=dict(jvp_relative=float(abs(cs-pred).max()/max(1,abs(cs).max())),background_flow=float(abs(flow.fun(s,np.zeros_like(Y),par)).max()),inlet=obj._inlet_metrics,dn=obj.Dmatrix_diagnostics)
        a.out_prefix.with_suffix('.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks));return
    install();start=time.time();print(json.dumps(dict(event='start',M=obj.M,nodes=len(x),q=a.amplitude,warp_reference=a.warp_reference,initial_inlet=obj._inlet_metrics,dn=obj.Dmatrix_diagnostics)),flush=True)
    sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac)
    flow=obj.flow(sol.p[0]);obj.initial(sol.p);physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=flow.c2_interpolant(physical)
    frozen=cfg if a.fixed else {**cfg,'delta':cfg['delta']+sol.p[0]}
    out=dict(scope=__doc__,warp_reference_q=a.warp_reference,config=dict(modes=obj.M,base_mode=3,core_kind='warped_support',angular=obj.nt,tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,fixed_metric=a.fixed),frozen_profile=frozen,gauge_amplitude=obj.q,actual_primary_amplitude=obj.support_amplitude,meridian_length=flow.end,physical_port_sha256=port['_sha256'],physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals)),newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
    cp=a.out_prefix.with_suffix('.json.gz');save_checkpoint(cp,out);out['summary']=audit(obj,physical,a.audit_angular);out['seconds']=time.time()-start;save_checkpoint(cp,out)
    summary={k:v for k,v in out.items()if k not in ('mesh','pp_coefficients')};a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(success=out['solver_success'],delta=frozen['delta'],nodes=out['nodes'],seconds=out['seconds'],**out['summary'])),flush=True)

if __name__=='__main__':main()
