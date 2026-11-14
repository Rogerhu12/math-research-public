"""Full spatial Frenet BVP on a short inward-first return cycle.
Astra curve_transition; AI-assisted 2026-11-08. Linear stable endpoint only;
this finite-prefix experiment constructs neither a rotational collar nor caps.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,json,time,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp,solve_bvp
from scipy.interpolate import PPoly
from curve_stable_prefix_bvp import CylindricalPrefix,save_checkpoint,load_checkpoint
from curve_linear_control import ramp,upward
from construct_general_reflected_core import curve_geometry,ReflectedCore

class InwardPrefix(CylindricalPrefix):
    def __init__(self,modes=4,amplitude=.01,delta_raw=.3,vu=.4,vd=.6,eps=.2,cycles=1,angular=128,base_mode=2,compute_stable=True):
        if base_mode%4!=2:raise ValueError('Exact inherited reflection family requires fundamental mode 2 modulo 4')
        self.M=modes;self.q=amplitude;self.delta_raw=delta_raw;self.delta=delta_raw/(1+delta_raw);self.vu=vu;self.vd=vd;self.eps=eps;self.cycles=cycles;self.nt=angular;self.arc_nodes=max(1024,128*modes*base_mode);self.base_mode=base_mode
        self.c4=0.;self.Tu=self.delta/(vu*(1-eps));self.Td=self.delta/(vd*(1-eps));self.period=self.Tu+self.Td;self.end=self.period*cycles
        self.even=base_mode*np.arange(1,modes+1);self.odd=np.arange(1,2*modes+2,2);self.n=3*modes+1;self.ix=0;self.iy=modes+1;self.ir=1;self.it=modes+1;self.iz=2*modes+1
        self.B,self.B1,self.B2=self.basis(angular);self.rhos=[];self.multipliers=[];D=np.diag([1.,-1.])
        for m in (self.even if compute_stable else []):
            U=upward(int(m),delta_raw,vu,eps)['U'];V=upward(int(m),delta_raw,vd,eps)['U'];T=U@D@np.linalg.inv(V)@D;tr=float(np.trace(T))
            if abs(tr)<=2:raise ValueError(f'Mode {m} is not hyperbolic')
            lam=2/(tr+np.sign(tr)*np.sqrt(tr*tr-4));vals,vec=np.linalg.eig(T);z=vec[:,np.argmin(abs(vals))].real
            self.rhos.append(float(z[1]/z[0]));self.multipliers.append(float(lam))
        self.rhos=np.asarray(self.rhos);self.h0=-1/(base_mode**2*self.rhos[0]) if compute_stable else 0.
        if compute_stable and self.h0<=0:raise ValueError('Reflected core requires positive halfwidth')
        self.pscale=np.array([1.]+[max(amplitude**j,1e-8) for j in range(2,modes+1)]);self.bscale=np.array([max(amplitude**j,1e-8) for j in range(1,modes+1)])
        self._cache=None;self._cached=None;self.calls=0
    def profile(self,s):
        s=np.asarray(s);t=np.mod(s,self.period);down=t<self.Td;u=np.where(down,t/self.Td,(t-self.Td)/self.Tu);w,I=ramp(u,self.eps)
        wp=np.where(u<self.eps,np.pi/(2*self.eps)*np.sin(np.pi*u/self.eps),np.where(u>1-self.eps,-np.pi/(2*self.eps)*np.sin(np.pi*(1-u)/self.eps),0.))
        a=np.where(down,1-self.delta*I/(1-self.eps),1-self.delta+self.delta*I/(1-self.eps));ap=np.where(down,-self.vd*w,self.vu*w);app=np.where(down,-self.vd*wp/self.Td,self.vu*wp/self.Tu)
        return a,ap,app
    def parameters(self,p):
        h=self.h0+p[0];maxmode=int(self.even[-1]);rad=np.zeros(maxmode//4);hei=np.zeros((maxmode+2)//4);hei[(self.base_mode-2)//4]=self.q
        for j,m in enumerate(self.even[1:],start=1):
            val=p[j]*self.pscale[j]
            if m%4==0:rad[m//4-1]=val
            else:hei[(m-2)//4]=val
        phi=2*np.pi*np.arange(self.arc_nodes)/self.arc_nodes;R=max(.2,math.sqrt(max(.04,1-(self.base_mode*self.q)**2/2)))
        for it in range(20):
            g=curve_geometry(phi,R,rad,hei);a0=float(np.mean(g['speed']))
            if abs(a0-1)<3e-15:break
            erp=np.c_[-np.sin(phi),np.cos(phi),np.zeros(len(phi))];d=float(np.mean(np.sum(g['d1']*erp,axis=1)/g['speed']));R-=(a0-1)/d
            if R<=.05:raise FloatingPointError('Core perimeter normalization left positive radius range')
        return dict(R=float(R),radial=rad.tolist(),height=hei.tolist(),halfwidth=float(h))
    def initial(self,p):
        if self._cache is not None and np.array_equal(p,self._cache):return self._cached
        par=self.parameters(p);core=ReflectedCore(par['R'],par['radial'],par['height'],self.arc_nodes);nt=max(256,16*int(self.even[-1]));theta=2*np.pi*np.arange(nt)/nt;exact=core.evaluate(par['halfwidth'],theta)
        if np.min(exact['den'])<=0:raise FloatingPointError('Exact rectifying core loses regularity')
        B,_,_=self.basis(nt);C=self.project(exact['F'][None,:,:],B)[:,0];out=(C-self.base(np.array([0.]))[:,0])/self.q;self._cache=p.copy();self._cached=out;return out
    def seed(self,nodes):
        p=np.zeros(self.M);x=np.linspace(0,self.end,nodes);m=self.base_mode
        def rhs(s,y):
            a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return [(-(m*m-1)*v*y[0]-m*m*b*y[1])/a,((m*m-1)*v*v*y[0]/b+m*m*v*y[1])/a]
        lin=solve_ivp(rhs,[0,self.end],[1/self.rhos[0],1],method='DOP853',rtol=1e-12,atol=1e-14,dense_output=True,max_step=self.period/100)
        f,g=lin.sol(x);y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/m;y[self.iz]=g
        left=self.initial(p)-y[:,0];y+=left[:,None]*(1-x/self.end)[None,:]**3
        return x,y,p
    def audit_streamed(self,sol,points=401,angular=256,block=96):
        K=int(self.even[-1])+1
        if angular<=6*K:raise ValueError(f'Angular audit needs N>6K={6*K} for cubic projection diagnostics; got {angular}')
        out=super().audit_streamed(sol,points,angular,block)
        ec,fc,gc=out['metric_component_bounds']
        out['metric_relative_operator_bound_from_components']=math.sqrt(ec*ec+2*fc*fc+gc*gc)
        out['metric_relative_operator_scope']='At the sampled radial positions, the target-orthonormal relative metric error has entries (E-1,F/a,G/a^2-1). The Frobenius bound from its three whole-angle component bounds also bounds its operator norm. Radial and floating-point enclosures remain unpaid.'
        par=self.parameters(sol.p); lower=2*abs(sum(par['height']))
        out['central_PV_two_point_lower']=lower
        out['central_PV_two_point_lower_over_Lband']=lower/out['Lband']
        out['central_PV_two_point_lower_over_Wr']=lower/self.delta
        out['PV_lower_justification']='On the same exact central material circle, phi=0 and phi=pi/2 give heights plus/minus sum(height coefficients). No triangle upper bound is used.'
        out['angular_polynomial_degree_bounds']={'coordinate_K':K,'metric_degree':2*K,'full_Darboux_tensor_degree':2*K,'projection_Jacobian_degree':3*K,'samples':angular,'quadratic_no_alias':bool(angular>4*K),'cubic_no_alias':bool(angular>6*K)}
        out['angular_DFT_scope']='At each sampled s with the numerical mean jets held fixed, metric and full Darboux tensor have degree<=2K and projection scalars degree<=3K. N>6K prevents angular aliasing, so DFT l1 gives whole-angle upper bounds in exact arithmetic. Floating-point, radial sampling, and mean-integration errors are not interval-enclosed. Frenet root and actual curvature remain sampled nonpolynomial diagnostics.'
        out['radial_representation']='Piecewise quintic C2 Hermite interpolant of collocation positions, first jets from the projected geometric flow, and second jets from its analytic derivative, plus the prescribed exact background profile. Coefficients retained without rounding.'
        out['radial_sampling']={'uniform_points_requested':points,'all_collocation_knots':True,'all_collocation_midpoints':True,'distinct_evaluated_points':out['samples_s'],'interval_enclosure':False,'mean_height_positive_Gauss_order':out['height_integral_quadrature_order']}
        out['curvature_scope']='Maximum over the stated radial/angular sample grid of the actual induced first and second fundamental forms. This sampled value is not a global upper bound.'
        out['collar_scope']='Finite cycle ending on linear modal Robin data; terminal noncircle is not a rotational collar.'
        return out

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--out',required=True);pa.add_argument('--modes',type=int,default=4);pa.add_argument('--amplitude',type=float,default=.01);pa.add_argument('--delta-raw',type=float,default=.3);pa.add_argument('--v-up',type=float,default=.4);pa.add_argument('--v-down',type=float,default=.6);pa.add_argument('--ramp',type=float,default=.2);pa.add_argument('--cycles',type=int,default=1);pa.add_argument('--base-mode',type=int,default=2);pa.add_argument('--angular',type=int,default=128);pa.add_argument('--nodes',type=int,default=151);pa.add_argument('--max-nodes',type=int,default=4000);pa.add_argument('--tol',type=float,default=3e-7);pa.add_argument('--bc-tol',type=float,default=3e-7);pa.add_argument('--audit-points',type=int,default=301);pa.add_argument('--audit-angular',type=int,default=256);pa.add_argument('--restart');args=pa.parse_args();start=time.time();obj=InwardPrefix(args.modes,args.amplitude,args.delta_raw,args.v_up,args.v_down,args.ramp,args.cycles,args.angular,args.base_mode)
    x,y,p=obj.seed(args.nodes)
    if args.restart:
        old=load_checkpoint(args.restart);oc=old['config']
        for k in ['delta_raw','v_up','v_down','ramp','cycles','base_mode']:
            if oc[k]!=getattr(args,k):raise ValueError('Restart fixed-profile mismatch: '+k)
        M0=oc['modes'];q0=oc['amplitude'];x=np.asarray(old['mesh']);P=PPoly.construct_fast(np.asarray(old['pp_coefficients']),x,extrapolate=True,axis=1);oy=P(x);y=np.zeros((obj.n,len(x)));y[0]=oy[0]*(obj.q/q0)
        for j in range(min(M0,obj.M)):
            scale=(obj.q/q0)**j
            for i,k in [(1+j,1+j),(obj.M+1+j,M0+1+j),(2*obj.M+1+j,2*M0+1+j)]:y[i]=oy[k]*scale
        p=np.zeros(obj.M);p[0]=old['parameters'][0]*(obj.q/q0)**2
        for j in range(1,min(M0,obj.M)):p[j]=old['parameters'][j]*max(q0**(j+1),1e-8)*(obj.q/q0)**(j+1)/obj.pscale[j]
    print(json.dumps(dict(event='start',M=obj.M,q=obj.q,h0=obj.h0,L0=2*(obj.h0+obj.end),lambdas=obj.multipliers)),flush=True)
    try:
        sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        sol.sol=obj.c2_interpolant(sol);audit=obj.audit_streamed(sol,args.audit_points,args.audit_angular)
        out=dict(author='Astra curve_transition; AI-assisted',scope=__doc__,config=vars(args),success=bool(sol.success),message=sol.message,seconds=time.time()-start,parameters=sol.p.tolist(),core=obj.parameters(sol.p),h0=obj.h0,rhos=obj.rhos.tolist(),multipliers=obj.multipliers,nodes=len(sol.x),max_rms_collocation_residual=float(np.max(sol.rms_residuals)),summary=audit,mesh=sol.x.tolist(),pp_coefficients=sol.sol.c)
    except Exception as e:out=dict(author='Astra curve_transition',config=vars(args),success=False,message=repr(e),seconds=time.time()-start,calls=obj.calls)
    out=save_checkpoint(args.out,out);print(json.dumps({k:v for k,v in out.items() if k not in ('mesh','scope','pp_coefficients')},indent=2),flush=True)
if __name__=='__main__':main()
