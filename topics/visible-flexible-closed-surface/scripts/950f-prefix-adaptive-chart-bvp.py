#!/usr/bin/env python3
"""Frozen s-dependent angular chart, with exact coordinate derivatives.

Same physical metric, theta=psi-e(s)sin(3psi)/3; e(s) is fixed by a recorded
C2 spline in normalized physical arclength and vanishes with two derivatives
at the tail cut. The Frenet velocity includes (theta_s/theta_psi) F_psi.
All FFT l1 numbers are finite-sampling diagnostics, not continuous enclosures.
This experiment is a finite linear-port prefix, not a complete closed surface.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,hashlib,importlib.util,json,math,sys,time,types
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import CubicSpline,PPoly
HERE=Path(__file__).resolve().parent;NOTES=HERE.parent/'notes';sys.path.insert(0,str(NOTES))
spec=importlib.util.spec_from_file_location('prefixwarp',HERE/'950f-prefix-warped-bvp.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)


def build_classes(chart):
    BaseFlow,BaseBVP=old.build_classes()
    from fixed_metric_mode3_bvp import merge_profile_mesh
    class Flow(BaseFlow):
        def __init__(self,*args,**kwargs):
            self.spline=CubicSpline(np.asarray(chart['knots']),np.asarray(chart['values']),bc_type=((1,0.),(1,chart['final_derivative'])))
            super().__init__(*args,**kwargs)
            self.fun=types.MethodType(Flow.adapt_fun,self);self.fun_jac=types.MethodType(Flow.adapt_fun_jac,self);self.c2_interpolant=types.MethodType(Flow.adapt_c2_interpolant,self)
        def angular(self,N):
            # The parent inlet is evaluated at s=0.
            return BaseFlow.angular(self,N)
        def geo(self,s,N):
            s=np.asarray(s);x=s/self.end;psi=2*np.pi*np.arange(N)/N
            h0=self.spline(x);h1=self.spline(x,1)/self.end;h2=self.spline(x,2)/self.end**2
            start=.75;u=np.clip((x-start)/(1-start),0.,1.);fac=1/((1-start)*self.end)
            S=u**3*(10-15*u+6*u*u);Sp=30*u*u*(1-u)**2;Spp=60*u*(1-u)*(1-2*u)
            c=1-S;cp=-Sp*fac;cpp=-Spp*fac**2
            e=self.warp_e*h0*c;ep=self.warp_e*(h1*c+h0*cp);epp=self.warp_e*(h2*c+2*h1*cp+h0*cpp)
            sn=np.sin(3*psi)[None,:];co=np.cos(3*psi)[None,:]
            theta=psi[None,:]-e[:,None]*sn/3;rho=1-e[:,None]*co;rho_p=3*e[:,None]*sn
            theta_s=-ep[:,None]*sn/3;theta_ss=-epp[:,None]*sn/3;rho_s=-ep[:,None]*co;rho_ps=3*ep[:,None]*sn
            if float(rho.min())<=0:raise FloatingPointError('Adaptive angle chart is not invertible')
            v=theta_s/rho;vs=(theta_ss*rho-theta_s*rho_s)/rho**2;vp=(rho_s*rho-theta_s*rho_p)/rho**2
            z=np.exp(1j*theta);a,ap,app=self.profile(s);aa=a[:,None];aa1=ap[:,None];aa2=app[:,None]
            vec=lambda w:np.stack((w.real,w.imag,np.zeros_like(w.real)),axis=-1)
            pos=aa*z;p1=1j*aa*rho*z;p2=aa*(1j*rho_p-rho*rho)*z
            s1=(aa1+1j*aa*theta_s)*z
            s2=(aa2-aa*theta_s**2+1j*(2*aa1*theta_s+aa*theta_ss))*z
            sp=(1j*aa1*rho+1j*aa*rho_s-aa*theta_s*rho)*z
            spp=(aa1*(1j*rho_p-rho*rho)+aa*(1j*rho_ps-2*rho*rho_s)+1j*aa*theta_s*(1j*rho_p-rho*rho))*z
            return dict(theta=theta,rho=rho,rhop=rho_p,v=v,vs=vs,vp=vp,pos=vec(pos),p1=vec(p1),p2=vec(p2),s1=vec(s1),s2=vec(s2),sp=vec(sp),spp=vec(spp),e=e)
        def physical_base(self,s,N,derivative=0):return self.geo(s,N)[('pos','s1','s2')[derivative]]
        def frame(self,s,C,B1=None,B2=None):
            B1=self.B1 if B1 is None else B1;B2=self.B2 if B2 is None else B2;g=self.geo(s,B1.shape[1]);a,ap,app=self.profile(s)
            d=self.values(C,B1)+g['p1'];dd=self.values(C,B2)+g['p2'];lam=np.sqrt(np.sum(d*d,axis=2));T=d/lam[:,:,None]
            dt=np.sum(dd*T,axis=2);nv=dd-dt[:,:,None]*T;nn=np.sqrt(np.sum(nv*nv,axis=2));N=nv/nn[:,:,None];kap=nn/lam**2;Bin=np.cross(T,N)
            alpha=-ap[:,None]/(a[:,None]*kap);margin=1-alpha**2
            if np.min(margin.real)<=0 or np.min(lam.real)<=0 or np.min(nn.real)<=0:raise FloatingPointError('Adaptive Frenet domain failure: '+str(float(np.min(margin.real))))
            beta=np.sqrt(margin);Vnormal=alpha[:,:,None]*N+beta[:,:,None]*Bin;W=Vnormal+g['v'][:,:,None]*d
            return dict(d=d,dd=dd,lam=lam,T=T,dt=dt,nn=nn,N=N,kap=kap,Bin=Bin,a=a,ap=ap,app=app,alpha=alpha,beta=beta,margin=margin,V=W,Vnormal=Vnormal,geo=g)
        def adapt_fun(self,s,y,p):
            s=np.asarray(s);out=np.empty(y.shape,dtype=y.dtype);self.calls+=1
            for first in range(0,len(s),64):
                sl=slice(first,first+64);yy=np.asarray(y[:,sl],np.clongdouble if np.iscomplexobj(y)else np.longdouble);fr=self.frame(s[sl],self.q*yy)
                out[:,sl]=np.asarray(self.project(fr['V']-fr['geo']['s1'],self.B)/self.q,dtype=y.dtype)
            return out
        def adapt_fun_jac(self,s,y,p):
            s=np.asarray(s);out=np.empty((self.n,self.n,len(s)))
            for first in range(0,len(s),64):
                sl=slice(first,first+64);fr=self.frame(s[sl],self.q*y[:,sl])
                for j in range(self.n):
                    dv=self.frame_jvp(fr,self.B1[j][None,:,:],self.B2[j][None,:,:])+fr['geo']['v'][:,:,None]*self.B1[j][None,:,:]
                    out[:,j,sl]=self.project(dv,self.B)
            return out,np.zeros((self.n,self.M,len(s)))
        def velocity_s(self,s,y,dy,B1=None,B2=None):
            B1=self.B1 if B1 is None else B1;B2=self.B2 if B2 is None else B2;fr=self.frame(s,self.q*y,B1,B2);g=fr['geo']
            sp=self.q*self.values(dy,B1)+g['sp'];spp=self.q*self.values(dy,B2)+g['spp'];dV=self.frame_jvp(fr,sp,spp)
            ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap']);be=-fr['alpha']*ae/fr['beta']
            dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
            dW=dV+g['vs'][:,:,None]*fr['d']+g['v'][:,:,None]*sp
            return fr,sp,dW
        def adapt_c2_interpolant(self,sol):
            s=sol.x;y=np.asarray(sol.y,np.longdouble);dy=self.adapt_fun(s,y,sol.p);ddy=np.empty_like(y)
            for first in range(0,len(s),64):
                sl=slice(first,first+64);fr,_,dW=self.velocity_s(s[sl],y[:,sl],dy[:,sl]);ddy[:,sl]=self.project(dW-fr['geo']['s2'],self.B)/self.q
            Y=y.T;D=dy.T;Q=ddy.T;h=np.diff(s).astype(np.longdouble)[:,None];e0=Y[1:]-Y[:-1]-h*D[:-1]-h*h*Q[:-1]/2;e1=D[1:]-D[:-1]-h*Q[:-1];e2=Q[1:]-Q[:-1]
            u=10*e0-4*h*e1+h*h*e2/2;v=-15*e0+7*h*e1-h*h*e2;w=6*e0-3*h*e1+h*h*e2/2
            return PPoly.construct_fast(np.stack((w/h**5,v/h**4,u/h**3,Q[:-1]/2,D[:-1],Y[:-1])).astype(float),s,extrapolate=True,axis=1)

    class BVP(BaseBVP):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs);self.Flow=lambda *a,**kw:Flow(*a,warp_q=self.warp_q,**kw);self._flow_key=None;self._flow=None
            self.fixed_flow=self.Flow(self.cfg,self.port,self.M,self.q,self.nt,self.base_mode,self.bridge)if self.fixed else None
            self.Dmatrix=np.diag(self.port['linearSlope'][:self.M]);self.Dmatrix_diagnostics=dict(physical_modes=len(self.port['linearSlope']),psi_modes=self.M,scope='Exact identity of angles at cut; truncated represented height has M physical modes.')
        def make_dn_matrix(self,D):return np.diag(D[:self.M]),dict(physical_modes=len(D),psi_modes=self.M,scope='Identity chart at cut')
        def seed(self,nodes):
            flow=self.flow(0);line=flow.backward_line();t=merge_profile_mesh(np.linspace(0,1,nodes),self.chart_breaks);s,_=self.chart(t,0);fg=np.empty((2,len(s)))
            for j,(lo,hi,sol,scale)in enumerate(line.segments):
                mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
                if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
            N=max(2048,64*self.M);g=flow.geo(s,N);theta=g['theta'];er=g['pos']/flow.profile(s)[0][:,None,None];et=np.stack((-er[:,:,1],er[:,:,0],np.zeros_like(er[:,:,0])),axis=-1)
            shape=fg[0,:,None,None]*(np.cos(3*theta)[:,:,None]*er-np.sin(3*theta)[:,:,None]*et/3);shape[:,:,2]+=fg[1,:,None]*np.cos(3*theta)
            B,_,_=flow.basis(N);y=flow.project(shape,B);p=np.zeros(self.M);difference=self.initial(p)-y[:,0];cutoff=(flow.Tu if flow.direction=='outward'else flow.Td)/2;y+=difference[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
            return t,y,p
        def restart(self,path):
            # A change of numerical angle chart is handled by an explicit
            # material-angle pullback. It is an initial guess only.
            from curve_stable_prefix_bvp import load_checkpoint
            rec=load_checkpoint(path)
            if rec.get('angular_chart')!='frozen-spline-adaptive-v1':raise ValueError('Adaptive-chart checkpoint required')
            if rec['chart']!=chart:raise ValueError('Reference spline differs')
            if rec['physical_tail_parameters']!=self.port['parameters']or rec['physical_tail_cut']!=self.port['cut']:raise ValueError('Physical tail metric differs')
            M0=rec['config']['modes'];q0=rec['gauge_amplitude'];qa=rec['actual_primary_amplitude'];p=np.zeros(self.M)
            if self.fixed:
                if rec['frozen_profile']!=self.cfg:raise ValueError('Frozen physical profile differs')
                if rec['warp_reference_q']!=self.warp_q:raise ValueError('Frozen convergence keeps its angle chart fixed')
                p[0]=math.log(qa/self.seed_support_amplitude);ratio=1.
            else:p[0]=rec['frozen_profile']['delta']-self.cfg['delta'];ratio=self.q/qa
            for j in range(1,min(M0,self.M)):p[j]=rec['parameters'][j]*rec['central_correction_scales'][j-1]*ratio**(j+1)/self.pscale[j-1]
            f=self.flow(p[0]);oldf=Flow(rec['frozen_profile'],self.port,M0,q0,max(64,self.nt),3,warp_q=rec['warp_reference_q'])
            t=merge_profile_mesh(np.linspace(0,1,self.restart_remesh),self.chart_breaks);s,_=self.chart(t,p[0]);sold=s/f.end*oldf.end
            pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),np.asarray(rec['mesh']),extrapolate=True,axis=1);oy=pp(sold)
            N=max(2048,64*max(M0,self.M));B,_,_=f.basis(N);y=np.empty((self.n,len(s)));ms=3*np.arange(1,M0+1)
            for start in range(0,len(s),32):
                sl=slice(start,start+32);target=f.geo(s[sl],N)['theta'];eold=oldf.geo(sold[sl],1)['e'][:,None];psi=target.copy()
                for _ in range(32):
                    residual=psi-eold*np.sin(3*psi)/3-target;update=residual/(1-eold*np.cos(3*psi));psi-=update
                    if float(abs(update).max())<2e-14:break
                if float(abs(psi-eold*np.sin(3*psi)/3-target).max())>1e-12:raise FloatingPointError('Restart chart pullback failed')
                phases=psi[:,:,None]*ms[None,None,:];co=np.cos(phases);si=np.sin(phases);c=oy[:,sl].T
                R=c[:,0,None]+np.einsum('npk,nk->np',co,c[:,1:M0+1]);T=np.einsum('npk,nk->np',si,c[:,M0+1:2*M0+1]);Z=np.einsum('npk,nk->np',co,c[:,2*M0+1:])
                value=np.stack((R*np.cos(psi)-T*np.sin(psi),R*np.sin(psi)+T*np.cos(psi),Z),axis=-1)
                y[:,sl]=f.project(value,B)*q0/self.q*ratio
            correction=self.initial(p)-y[:,0];cutoff=(f.Tu if f.direction=='outward'else f.Td)/2;y+=correction[:,None]*np.maximum(0,1-s/cutoff)[None,:]**3
            return t,y,p
    return Flow,BVP


def audit(obj,sol,N=512):
    flow=obj.flow(sol.p[0]);obj.initial(sol.p);N=max(N,16*(obj.M*3+1));B,B1,B2=flow.basis(N)
    ss=np.unique(np.r_[np.linspace(0,flow.end,151),sol.x,(sol.x[:-1]+sol.x[1:])/2]);hh=flow.height_integral(sol,ss,N,6)
    out=dict(metric_l1=0.,flow_defect=0.,darboux_l1=0.,kappa_sample=0.,radius_max=0.,height_max=0.,root_min=1.,chart_rho_min=1.,support_amplitude=obj.support_amplitude)
    for first in range(0,len(ss),32):
        s=ss[first:first+32];Y=sol.sol(s);Yp=sol.sol(s,1);Ypp=sol.sol(s,2);a,ap,app=flow.profile(s);fr,Fsp,dW=flow.velocity_s(s,Y,Yp,B1,B2);g=fr['geo'];rho=g['rho'];v=g['v']
        Fsc=g['s1']+obj.q*flow.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fssc=g['s2']+obj.q*flow.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
        Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
        Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2);errors=np.stack((E-1,F/a[:,None],G/a[:,None]**2-1),axis=2)
        out['metric_l1']=max(out['metric_l1'],float(np.max(np.sum(abs(np.fft.fft(errors,axis=1)/N),axis=1))));out['flow_defect']=max(out['flow_defect'],float(np.linalg.norm(Fs-fr['Vnormal'],axis=2).max()))
        nn=np.cross(Fs,Ft);nn/=np.linalg.norm(nn,axis=2)[:,:,None];L=np.sum(Fss*nn,axis=2);M=np.sum(Fst*nn,axis=2);NN=np.sum(Ftt*nn,axis=2);detI=E*G-F*F;tr=(L*G-2*M*F+NN*E)/detI;detII=(L*NN-M*M)/detI
        kap=(abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*detII)))/2
        Hst=(Fst-ap[:,None,None]/a[:,None,None]*Ft)/a[:,None,None];Htt=(Ftt+(a*ap)[:,None,None]*Fs)/a[:,None,None]**2
        gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-(Ft/a[:,None,None])[:,:,:,None]*(Ft/a[:,None,None])[:,:,None,:]
        tensor=.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]+(app/a)[:,None,None,None]*gram;ft=np.fft.fft(tensor,axis=1)/N
        out['darboux_l1']=max(out['darboux_l1'],float(np.max(np.sum(np.sqrt(np.sum(abs(ft)**2,axis=(2,3))),axis=1))))
        pos=g['pos']+obj.q*flow.values(Y,B);pos[:,:,2]+=hh[first:first+len(s),None]
        out['kappa_sample']=max(out['kappa_sample'],float(kap.max()));out['root_min']=min(out['root_min'],float(fr['margin'].min()));out['chart_rho_min']=min(out['chart_rho_min'],float(rho.min()))
        out['radius_max']=max(out['radius_max'],float(np.linalg.norm(pos[:,:,:2],axis=2).max()));out['height_max']=max(out['height_max'],float(abs(pos[:,:,2]).max()))
    out['core']=obj._core.summary();out['inlet']=obj._inlet_metrics;out['dn_matrix']=obj.Dmatrix_diagnostics;out['terminal_height_coeff_max']=float(obj.q*abs(sol.y[obj.iz:,-1]).max());out['physical_bc_max']=float(abs(obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights).max());out['samples_s']=len(ss);out['samples_psi']=N
    out['scope']='Sampled physical metric and Cartesian Darboux tensor after exact chain rule. Finite FFT l1 is not a continuous-angle proof. Linear finite port only; full nonlinear mean and Cartesian seam are unpaid.'
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--profile',type=Path,required=True);p.add_argument('--chart',type=Path,required=True);p.add_argument('--linear-port',type=Path,required=True);p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--amplitude',type=float,default=.08);p.add_argument('--warp-reference',type=float,default=.08);p.add_argument('--modes',type=int,default=8);p.add_argument('--angular',type=int,default=256);p.add_argument('--audit-angular',type=int,default=512)
    p.add_argument('--nodes',type=int,default=301);p.add_argument('--max-nodes',type=int,default=1200);p.add_argument('--tol',type=float,default=2e-7);p.add_argument('--bc-tol',type=float,default=1e-8);p.add_argument('--physical-bc-tol',type=float,default=1e-10);p.add_argument('--fixed',action='store_true');p.add_argument('--restart',type=Path);p.add_argument('--check-only',action='store_true');a=p.parse_args();old.install_source(a.source_root)
    from curve_stable_prefix_bvp import save_checkpoint
    from f6curve_domain_newton import install,STATS
    chart=json.loads(a.chart.read_text());_,BVP=build_classes(chart);cfg=json.loads(a.profile.read_text());port=json.loads(a.linear_port.read_text());port['_sha256']=hashlib.sha256(a.linear_port.read_bytes()).hexdigest()
    obj=BVP(cfg,port,a.amplitude,a.modes,a.angular,a.fixed,a.warp_reference);obj.restart_remesh=a.nodes;obj.bcweights=np.full(obj.M,a.physical_bc_tol/a.bc_tol);x,y,par=obj.restart(a.restart)if a.restart else obj.seed(a.nodes)
    if a.check_only:
        f=obj.flow(par[0]);rng=np.random.default_rng(20261109);s=np.linspace(.001,f.end,7);Y=np.zeros((obj.n,len(s)));Y[1]=.001;vec=rng.normal(size=Y.shape);J=f.fun_jac(s,Y,par)[0];cs=f.fun(s,Y.astype(complex)+1e-25j*vec,par).imag/1e-25;pred=np.einsum('ijk,jk->ik',J,vec)
        out=dict(jvp_relative=float(abs(cs-pred).max()/max(1,abs(cs).max())),background_flow=float(abs(f.fun(s,np.zeros_like(Y),par)).max()),inlet=obj._inlet_metrics,cut_chart_max=max(float(abs(f.geo(np.array([f.end]),512)[k]).max())for k in ('v','vs','vp','e')))
        a.out_prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return
    install();start=time.time();print(json.dumps(dict(event='start',M=obj.M,nodes=len(x),q=a.amplitude,warp_reference=a.warp_reference,initial_inlet=obj._inlet_metrics)),flush=True)
    sol=solve_bvp(obj.fun,obj.bc,x,y,par,tol=a.tol,bc_tol=a.bc_tol,max_nodes=a.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac)
    f=obj.flow(sol.p[0]);obj.initial(sol.p);physical=SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p);physical.sol=f.c2_interpolant(physical);frozen=cfg if a.fixed else {**cfg,'delta':cfg['delta']+sol.p[0]}
    out=dict(scope=__doc__,angular_chart='frozen-spline-adaptive-v1',chart=chart,warp_reference_q=a.warp_reference,config=dict(modes=obj.M,base_mode=3,core_kind='adaptive_warped_support',angular=obj.nt,tol=a.tol,bc_tol=a.bc_tol,physical_bc_tol=a.physical_bc_tol,fixed_metric=a.fixed),frozen_profile=frozen,gauge_amplitude=obj.q,actual_primary_amplitude=obj.support_amplitude,meridian_length=f.end,physical_port_sha256=port['_sha256'],physical_tail_parameters=port['parameters'],physical_tail_cut=port['cut'],parameters=sol.p.tolist(),central_correction_scales=obj.pscale.tolist(),nodes=len(sol.x),solver_success=bool(sol.success),message=sol.message,max_rms_collocation_residual=float(np.max(sol.rms_residuals)),newton_domain_audit=dict(STATS),mesh=physical.x.tolist(),pp_coefficients=physical.sol.c)
    cp=a.out_prefix.with_suffix('.json.gz');save_checkpoint(cp,out);out['summary']=audit(obj,physical,a.audit_angular);out['seconds']=time.time()-start;save_checkpoint(cp,out);summary={k:v for k,v in out.items()if k not in ('mesh','pp_coefficients')};a.out_prefix.with_name(a.out_prefix.name+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(dict(success=out['solver_success'],delta=frozen['delta'],nodes=out['nodes'],seconds=out['seconds'],**out['summary'])),flush=True)

if __name__=='__main__':main()
