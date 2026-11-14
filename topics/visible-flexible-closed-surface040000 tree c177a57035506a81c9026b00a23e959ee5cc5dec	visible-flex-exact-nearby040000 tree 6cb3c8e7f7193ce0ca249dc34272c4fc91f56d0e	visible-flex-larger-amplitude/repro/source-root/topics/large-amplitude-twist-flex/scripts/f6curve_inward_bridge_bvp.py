"""Joint inward-cycle + directional bridge + actual nonlinear tail-DN BVP.
Astra curve_transition, AI-assisted, 2026-11-08. Finite Fourier/depth only;
not an infinite-tail, exact-circle, closed-flex or all-phase certificate.
"""
import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import argparse,json,time,math
import numpy as np
from scipy.integrate import solve_bvp,solve_ivp
from scipy.interpolate import PPoly
from f6curve_inward_bvp import InwardPrefix
from f6curve_bidirectional_bridge import DirectionalBridge
from f6curve_bridge_bvp import TailPort
from curve_stable_prefix_bvp import save_checkpoint,load_checkpoint

class InwardBridgeBVP(InwardPrefix):
    def __init__(self,port,amplitude=.0001,delta_raw=.2,vu=.85,vd=.85,eps=.2,cycles=1,angular=128):
        self.bridge=None;self.port=port
        super().__init__(port.M,amplitude,delta_raw,vu,vd,eps,cycles,angular,2,compute_stable=False)
        self.prefix_end=self.end;self.bridge=DirectionalBridge(port.cut);self.end=self.prefix_end+self.bridge.L;self.sigma=self.bridge.sigma
        self.linear=[]
        for j,D in enumerate(port.linearD):
            m=2*(j+1);a=port.cut['radius'];w=port.cut['backgroundSlope'];terminal=np.array([self.sigma*w*(a*D-m*m)/(m*m-1),1.])
            def rhs(s,y):
                a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
                return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],(m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a
            z=solve_ivp(rhs,[self.end,0],terminal,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True,max_step=.005)
            self.linear.append(z)
        self.rhos=np.array([z.y[1,-1]/z.y[0,-1] for z in self.linear]);self.h0=-1/(4*self.rhos[0])
        if self.h0<=0:raise ValueError('Complete core/cycle/bridge/tail linear direction has h<=0')
        self.bcweights=np.maximum(self.bscale,1e-9);self._tail_last=None
    def profile(self,s):
        s=np.atleast_1d(s)
        if self.bridge is None:return super().profile(s)
        a,v,acc=super().profile(np.minimum(s,self.prefix_end));mask=s>self.prefix_end
        if np.any(mask):a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc
    def terminal(self,y,jac=True):
        tail=self.port.solve(self.sigma*self.q*y[self.iz:],jacobian=jac);self._tail_last=tail
        derivative=self.fun(np.array([self.end]),y[:,None],np.zeros(self.M))[:,0]
        residual=self.q*derivative[self.iz:]-np.asarray(tail['jets']['slope'])/math.sqrt(self.port.cut['E'])
        return residual/self.bcweights
    def bc(self,ya,yb,p):return np.r_[ya-self.initial(p),self.terminal(yb)]
    def bc_jac(self,ya,yb,p):
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n);B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        tail=self.port.solve(self.sigma*self.q*yb[self.iz:],jacobian=True);TJ=np.array(tail['heightJetJacobian']).reshape(3*self.M+2,self.M)[:self.M]
        FJ,_=self.fun_jac(np.array([self.end]),yb[:,None],p);J=self.q*FJ[self.iz:,:,0]
        J[:,self.iz:]-=self.sigma*self.q*TJ/math.sqrt(self.port.cut['E']);B[self.n:]=J/self.bcweights[:,None]
        for j in range(self.M):
            step=2e-5 if j==0 else 2e-6/(self.pscale[j]*(j+1)**2);v=np.zeros(self.M);v[j]=step
            P[:self.n,j]=-(-self.initial(p+2*v)+8*self.initial(p+v)-8*self.initial(p-v)+self.initial(p-2*v))/(12*step)
        return A,B,P
    def seed(self,nodes):
        x=np.unique(np.r_[np.linspace(0,self.prefix_end,nodes),np.linspace(self.prefix_end,self.end,max(51,nodes//2))]);p=np.zeros(self.M)
        f,g=self.linear[0].sol(x)/self.linear[0].y[1,-1];y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/2;y[self.iz]=g
        y+=(self.initial(p)-y[:,0])[:,None]*(1-x/self.end)[None,:]**3;return x,y,p
    def seam_audit(self,sol):
        s=np.array([self.end]);y=sol.sol(s);C=self.base(s)+self.q*y;Cp=self.base(s,1)+self.q*sol.sol(s,1);Cpp=self.base(s,2)+self.q*sol.sol(s,2)
        B,B1,B2=self.basis(max(256,self.nt));fr=self.frame(s,C,B1,B2);dV=self.frame_jvp(fr,self.values(Cp,B1),self.values(Cp,B2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap']);be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        mean1=float(np.mean(fr['V'][:,:,2]));mean2=float(np.mean(dV[:,:,2]));tail=self.port.solve(self.sigma*self.q*y[self.iz:,0],jacobian=True,audit=True);j=tail['jets'];E=j['E'];app=-j['Ep']/(2*E**2)
        em1=j['meanSlope']/math.sqrt(E);em2=self.sigma*(j['meanSecond']/E+j['meanSlope']*app);e2=self.sigma*(np.asarray(j['second'])/E+np.asarray(j['slope'])*app)
        return dict(finite_depth_only=True,tail_calls=self.port.calls,tail_converged=tail['converged'],tail_residual=tail['residual'],tail_jets=j,tail_audit=tail.get('audit'),tail_checkpoint=tail.get('checkpoint'),
                    mean_first_jet_actual=mean1,mean_first_jet_expected=em1,mean_first_jet_mismatch=mean1-em1,mean_second_jet_actual=mean2,mean_second_jet_expected=em2,mean_second_jet_mismatch=mean2-em2,
                    nonmean_first_jet_mismatch=float(abs(Cp[self.iz:,0]-np.asarray(j['slope'])/math.sqrt(E)).max()),nonmean_second_jet_mismatch=float(abs(Cpp[self.iz:,0]-e2).max()),terminal_root=float(np.min(fr['margin'])),terminal_height_modes=(self.sigma*self.q*y[self.iz:,0]).tolist())
    def audit_streamed(self,*args,**kwargs):
        out=super().audit_streamed(*args,**kwargs);out['collar_scope']='Finite prefix + bridge, matched to actual nonlinear finite-depth DN. No infinite-tail or exact-circle assertion.';return out

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--tail-config',required=True);pa.add_argument('--out',required=True);pa.add_argument('--amplitude',type=float,default=.0001);pa.add_argument('--delta-raw',type=float,default=.2);pa.add_argument('--v-up',type=float,default=.85);pa.add_argument('--v-down',type=float,default=.85);pa.add_argument('--ramp',type=float,default=.2);pa.add_argument('--cycles',type=int,default=1);pa.add_argument('--angular',type=int,default=128);pa.add_argument('--nodes',type=int,default=151);pa.add_argument('--max-nodes',type=int,default=4000);pa.add_argument('--tol',type=float,default=1e-7);pa.add_argument('--bc-tol',type=float,default=1e-7);pa.add_argument('--audit-points',type=int,default=301);pa.add_argument('--audit-angular',type=int,default=384);pa.add_argument('--restart');args=pa.parse_args();start=time.time();port=TailPort(args.tail_config)
    try:
        obj=InwardBridgeBVP(port,args.amplitude,args.delta_raw,args.v_up,args.v_down,args.ramp,args.cycles,args.angular);x,y,p=obj.seed(args.nodes)
        if args.restart:
            old=load_checkpoint(args.restart);oc=old['config'];M0=oc['modes'];q0=oc['amplitude']
            for k in ['tail_config','delta_raw','v_up','v_down','ramp','cycles']:
                if oc[k]!=getattr(args,k):raise ValueError('Restart profile mismatch: '+k)
            x=np.asarray(old['mesh']);P=PPoly.construct_fast(np.asarray(old['pp_coefficients']),x,extrapolate=True,axis=1);oy=P(x);y=np.zeros((obj.n,len(x)));y[0]=oy[0]*obj.q/q0
            for j in range(min(M0,obj.M)):
                scale=(obj.q/q0)**j
                for i,k in [(1+j,1+j),(obj.M+1+j,M0+1+j),(obj.iz+j,2*M0+1+j)]:y[i]=oy[k]*scale
            p=np.zeros(obj.M);p[0]=old['parameters'][0]*(obj.q/q0)**2
            for j in range(1,min(M0,obj.M)):p[j]=old['parameters'][j]*max(q0**(j+1),1e-8)*(obj.q/q0)**(j+1)/obj.pscale[j]
        print(json.dumps(dict(event='start',q=obj.q,M=obj.M,h0=obj.h0,Lwithouttail=2*(obj.h0+obj.end),bridge_sigma=obj.sigma,bridge_length=obj.bridge.L)),flush=True)
        sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2);sol.sol=obj.c2_interpolant(sol);audit=obj.audit_streamed(sol,args.audit_points,args.audit_angular);seam=obj.seam_audit(sol)
        out=dict(author='Astra curve_transition; AI-assisted',scope=__doc__,config={**vars(args),'modes':obj.M},success=bool(sol.success),message=sol.message,seconds=time.time()-start,parameters=sol.p.tolist(),core=obj.parameters(sol.p),h0=obj.h0,linear_rhos=obj.rhos.tolist(),summary=audit,seam=seam,mesh=sol.x.tolist(),pp_coefficients=sol.sol.c)
    except Exception as e:out=dict(author='Astra curve_transition',config=vars(args),success=False,message=repr(e),seconds=time.time()-start,tail_calls=port.calls)
    finally:port.close()
    out=save_checkpoint(args.out,out);print(json.dumps({k:v for k,v in out.items() if k not in ['mesh','pp_coefficients','scope']},indent=2),flush=True)
if __name__=='__main__':main()
