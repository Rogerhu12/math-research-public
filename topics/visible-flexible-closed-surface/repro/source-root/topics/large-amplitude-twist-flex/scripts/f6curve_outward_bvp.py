"""Complete spatial BVP on outward-first cycles at an arbitrary m=2 mod4.
Astra curve_transition, AI-assisted 2026-11-08. Finite stable cylinder endpoint;
no rotational collar, cap or closed-surface certification is provided here.
Stable directions use backward normalized vectors, never a small eigenvalue of
a large transfer matrix. The output retains all complete physical modes.
"""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import argparse,json,time,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp,solve_bvp
from scipy.interpolate import PPoly
from f6curve_inward_bvp import InwardPrefix
from curve_linear_control import ramp
from curve_stable_prefix_bvp import save_checkpoint,load_checkpoint
from f6curve_domain_newton import install,STATS

class OutwardPrefix(InwardPrefix):
    def __init__(self,modes=4,amplitude=.001,delta=.2571428571428571,vu=.8,vd=.999,eps=.05,cycles=2,angular=192,base_mode=6,compute_stable=True,direction_data=None):
        super().__init__(modes,amplitude,delta,vu,vd,eps,cycles,angular,base_mode,compute_stable=False)
        self.delta=delta;self.Tu=delta/(vu*(1-eps));self.Td=delta/(vd*(1-eps));self.period=self.Tu+self.Td;self.end=self.period*cycles
        self.breakpoints=np.unique(np.concatenate([j*self.period+np.array([0,eps*self.Tu,(1-eps)*self.Tu,self.Tu,self.Tu+eps*self.Td,self.Tu+(1-eps)*self.Td,self.period]) for j in range(cycles)]))
        self.direction_audit=[];self.rhos=[];self.multipliers=[]
        cache=None
        if compute_stable and direction_data:
            cache=json.loads(Path(direction_data).read_text());cfg=cache['source_config']
            for key,value in [('delta',delta),('v_up',vu),('v_down',vd),('ramp',eps),('base_mode',base_mode)]:
                if abs(cfg[key]-value)>1e-14:raise ValueError('Independent direction data profile mismatch: '+key)
            if not cache.get('converged') or len(cache['rhos'])<modes:raise ValueError('Insufficient independently converged direction data')
        if compute_stable:
            for j,m in enumerate(self.even):
                if cache is not None:
                    rho=cache['rhos'][j];v=np.array([1.,rho]);v/=np.linalg.norm(v)
                    z=solve_ivp(lambda s,y:self.linear_rhs(s,y,int(m)),[self.period,0],v,method='DOP853',rtol=3e-12,atol=3e-14,max_step=self.period/240)
                    w=z.y[:,-1];norm=np.linalg.norm(w);change=abs(v[0]*w[1]-v[1]*w[0])/norm;lam=float(np.sign(np.dot(v,w))/norm)
                    if change>3e-8 or abs(lam)>=1:raise ValueError('Independent physical one-period direction check failed')
                    self.rhos.append(float(rho));self.multipliers.append(lam);self.direction_audit.append(dict(mode=int(m),method='Independent angle-chart direction plus one physical backward-period check',source=str(direction_data),projective_change=float(change),inverse_growth=lam));continue
                v=np.array([0.,1.]);last=None
                for it in range(16):
                    z=solve_ivp(lambda s,y:self.linear_rhs(s,y,int(m)),[self.period,0],v,method='DOP853',rtol=3e-12,atol=3e-14,max_step=self.period/240)
                    t=z.y[:,-1];norm=np.linalg.norm(t);sign=1 if np.dot(t,v)>=0 else -1;nextv=sign*t/norm;angle=abs(v[0]*nextv[1]-v[1]*nextv[0]);v=nextv;last=(sign/norm,angle)
                    if it>=2 and angle<2e-13:break
                if last[1]>2e-9 or abs(last[0])>=1:raise ValueError(f'Mode {m} has no resolved contracting direction: {last}')
                self.rhos.append(float(v[1]/v[0]));self.multipliers.append(float(last[0]));self.direction_audit.append(dict(mode=int(m),iterations=it+1,projective_change=float(last[1]),inverse_growth=float(last[0])))
            self.rhos=np.asarray(self.rhos);self.h0=-1/(base_mode**2*self.rhos[0])
            if self.h0<=0:raise ValueError('Exact reflected core needs h>0')
    def profile(self,s):
        s=np.asarray(s);t=np.mod(s,self.period);up=t<self.Tu;u=np.where(up,t/self.Tu,(t-self.Tu)/self.Td);w,I=ramp(u,self.eps)
        wp=np.where(u<self.eps,np.pi/(2*self.eps)*np.sin(np.pi*u/self.eps),np.where(u>1-self.eps,-np.pi/(2*self.eps)*np.sin(np.pi*(1-u)/self.eps),0.))
        a=np.where(up,1+self.delta*I/(1-self.eps),1+self.delta-self.delta*I/(1-self.eps));ap=np.where(up,self.vu*w,-self.vd*w);app=np.where(up,self.vu*wp/self.Tu,-self.vd*wp/self.Td)
        return a,ap,app
    def linear_rhs(self,s,y,m):
        a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
        return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],(m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a
    def bc_jac(self,ya,yb,p):
        if not hasattr(self,'initial_parameter_jacobian'):return super().bc_jac(ya,yb,p)
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n)
        B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        fm,gm=self.modal(np.eye(self.n));f,g=self.modal(yb);J=self.q*(gm-self.rhos[:,None]*fm)
        if self.M>=2:J[1]-=2*self.c4*self.q**2*g[0]*gm[0]
        B[self.n:]=J/(np.hypot(1,self.rhos)*self.bscale)[:,None]
        P[:self.n]=-self.initial_parameter_jacobian(p)
        return A,B,P
    def seed(self,nodes):
        p=np.zeros(self.M);x=np.unique(np.r_[np.concatenate([j*self.period+np.linspace(0,self.period,nodes) for j in range(self.cycles)]),self.breakpoints]);m=self.base_mode
        terminal=np.array([1/self.rhos[0],1.]);lin=solve_ivp(lambda s,y:self.linear_rhs(s,y,m),[self.end,0],terminal,method='DOP853',rtol=2e-12,atol=2e-14,dense_output=True,max_step=self.period/200)
        f,g=lin.sol(x)/lin.y[1,-1];y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/m;y[self.iz]=g
        cutoff=self.Tu/2
        y+=(self.initial(p)-y[:,0])[:,None]*np.maximum(0,1-x/cutoff)[None,:]**3
        return x,y,p

def with_profile_breaks(x,breaks,period):
    x=np.asarray(x)
    for b in breaks:x=x[abs(x-b)>1e-10*period]
    return np.unique(np.r_[x,breaks])

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--out',required=True);pa.add_argument('--modes',type=int,default=4);pa.add_argument('--amplitude',type=float,default=.002);pa.add_argument('--delta',type=float,default=.2571428571428571);pa.add_argument('--v-up',type=float,default=.8);pa.add_argument('--v-down',type=float,default=.999);pa.add_argument('--ramp',type=float,default=.05);pa.add_argument('--cycles',type=int,default=2);pa.add_argument('--base-mode',type=int,default=6);pa.add_argument('--angular',type=int,default=256);pa.add_argument('--nodes',type=int,default=181);pa.add_argument('--max-nodes',type=int,default=8000);pa.add_argument('--tol',type=float,default=3e-7);pa.add_argument('--bc-tol',type=float,default=3e-8);pa.add_argument('--audit-points',type=int,default=401);pa.add_argument('--audit-angular',type=int,default=768);pa.add_argument('--restart');pa.add_argument('--restart-stride',type=int,default=1);pa.add_argument('--restart-remesh',type=int,default=0);pa.add_argument('--local-frame',action='store_true');pa.add_argument('--analytic-core-jac',action='store_true');pa.add_argument('--direction-data');args=pa.parse_args();start=time.time()
    install()
    try:
        obj=OutwardPrefix(args.modes,args.amplitude,args.delta,args.v_up,args.v_down,args.ramp,args.cycles,args.angular,args.base_mode,direction_data=args.direction_data);x,y,p=obj.seed(args.nodes)
        if args.local_frame:
            from f6curve_local_frame import install_local_frame
            install_local_frame(obj)
        if args.analytic_core_jac:
            from f6curve_core_variation import install_analytic_core_jacobian
            install_analytic_core_jacobian(obj)
        if args.restart:
            old=load_checkpoint(args.restart);oc=old['config'];M0=oc['modes'];q0=oc['amplitude']
            for k in ['delta','v_up','v_down','ramp','cycles','base_mode']:
                if oc[k]!=getattr(args,k):raise ValueError('Restart profile mismatch: '+k)
            if args.restart_stride<1:raise ValueError('Restart stride must be positive')
            ox=np.asarray(old['mesh']);P=PPoly.construct_fast(np.asarray(old['pp_coefficients']),ox,extrapolate=True,axis=1)
            if args.restart_remesh:
                if args.restart_remesh<3:raise ValueError('Restart remesh needs at least three points per cycle')
                initial_mesh=np.concatenate([j*obj.period+np.linspace(0,obj.period,args.restart_remesh) for j in range(obj.cycles)])
            else:initial_mesh=ox[::args.restart_stride]
            x=with_profile_breaks(initial_mesh,obj.breakpoints,obj.period);oy=P(x);y=np.zeros((obj.n,len(x)));y[0]=oy[0]*obj.q/q0
            for j in range(min(M0,obj.M)):
                scale=(obj.q/q0)**j
                for i,k in [(1+j,1+j),(obj.M+1+j,M0+1+j),(obj.iz+j,2*M0+1+j)]:y[i]=oy[k]*scale
            p=np.zeros(obj.M);p[0]=old['parameters'][0]*(obj.q/q0)**2+old['h0']-obj.h0
            for j in range(1,min(M0,obj.M)):p[j]=old['parameters'][j]*max(q0**(j+1),1e-8)*(obj.q/q0)**(j+1)/obj.pscale[j]
        print(json.dumps(dict(event='start',M=obj.M,q=obj.q,h0=obj.h0,Lfinite=2*(obj.h0+obj.end),multipliers=obj.multipliers,direction_audit=obj.direction_audit)),flush=True)
        sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2);sol.sol=obj.c2_interpolant(sol);audit=obj.audit_streamed(sol,args.audit_points,args.audit_angular)
        out=dict(author='Astra curve_transition; AI-assisted',scope=__doc__,config=vars(args),success=bool(sol.success),message=sol.message,seconds=time.time()-start,parameters=sol.p.tolist(),core=obj.parameters(sol.p),h0=obj.h0,rhos=obj.rhos.tolist(),multipliers=obj.multipliers,direction_audit=obj.direction_audit,newton_domain_audit=dict(STATS),analytic_core_jac_audit=getattr(obj,'analytic_core_jac_audit',None),nodes=len(sol.x),max_rms_collocation_residual=float(np.max(sol.rms_residuals)),summary=audit,mesh=sol.x.tolist(),pp_coefficients=sol.sol.c)
    except Exception as e:out=dict(author='Astra curve_transition',config=vars(args),success=False,message=repr(e),seconds=time.time()-start,newton_domain_audit=dict(STATS))
    out=save_checkpoint(args.out,out);print(json.dumps({k:v for k,v in out.items() if k not in ['mesh','pp_coefficients','scope']},indent=2),flush=True)
if __name__=='__main__':main()
