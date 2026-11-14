"""Match exact reflected rectifying core + Frenet flow to a nonlinear tail port.
Astra / curve_transition; AI-assisted, 2026-11-08. Finite Fourier/depth experiment;
a positive result additionally needs true-tail convergence and complete embedding.
"""
from pathlib import Path
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,subprocess,time,math,argparse,hashlib
import numpy as np
from scipy.integrate import solve_ivp,solve_bvp
from scipy.interpolate import PPoly
sys.path.insert(0,str(Path(__file__).parent))
from curve_stable_prefix_bvp import CylindricalPrefix,save_checkpoint,load_checkpoint
from f6curve_bridge_linear import TurningBridge

class TailPort:
    def __init__(self,config):
        self.config=str(config);self.calls=0;self.cache_key=None;self.cache_value=None
        self.proc=subprocess.Popen(['node',str(Path(__file__).with_name('f6curve_tail_port.mjs')),str(config)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1)
        self.ready=json.loads(self.proc.stdout.readline())
        self.cut=self.ready['cut'];self.linearD=np.array(self.ready['linearSlope']);self.M=len(self.linearD)
    def solve(self,height,jacobian=True,audit=False):
        h=np.asarray(height,float)
        if self.cache_key is not None and np.array_equal(h,self.cache_key) and (not audit):return self.cache_value
        self.calls+=1;self.proc.stdin.write(json.dumps(dict(height=h.tolist(),jacobian=jacobian,audit=audit))+'\n');self.proc.stdin.flush()
        row=self.proc.stdout.readline()
        if not row:raise RuntimeError('Tail port subprocess stopped')
        out=json.loads(row)
        if out.get('failed') or not out.get('converged'):raise RuntimeError('Tail solve failed '+str({k:v for k,v in out.items() if k!='heightJetJacobian'}))
        self.cache_key=h.copy();self.cache_value=out
        return out
    def close(self):
        if self.proc.poll() is None:
            self.proc.stdin.write('{"stop":true}\n');self.proc.stdin.flush();self.proc.stdin.close()
            try:self.proc.wait(timeout=15)
            except subprocess.TimeoutExpired:self.proc.terminate();self.proc.wait(timeout=5)

class BridgeBVP(CylindricalPrefix):
    def __init__(self,port,amplitude=.001,delta=.8,velocity=.7,eps=.1,cycles=1,angular=128):
        self.bridge=None;self.port=port
        super().__init__(port.M,amplitude,delta,velocity,velocity,eps,cycles,angular,0.)
        self.prefix_end=self.end;self.bridge=TurningBridge(port.cut);self.end=self.prefix_end+self.bridge.L
        self.linear=[]
        for j,D in enumerate(port.linearD):
            m=2*(j+1);a=port.cut['radius'];w=port.cut['backgroundSlope'];terminal=np.array([-w*(a*D-m*m)/(m*m-1),1.])
            def rhs(s,y):
                a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
                return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],(m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a
            z=solve_ivp(rhs,[self.end,0],terminal,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True,max_step=.01)
            self.linear.append(z)
        self.rhos=np.array([z.y[1,-1]/z.y[0,-1] for z in self.linear]);self.h0=-1/(4*self.rhos[0])
        if self.h0<=0:raise ValueError('Core reflection matching needs positive h')
        self.bcweights=np.maximum(self.bscale,1e-9)
        self._tail_last=None
    def profile(self,s):
        s=np.atleast_1d(s)
        if self.bridge is None:return super().profile(s)
        a,v,acc=super().profile(np.minimum(s,self.prefix_end))
        mask=s>self.prefix_end
        if np.any(mask):a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc
    def terminal(self,y,jac=True):
        tail=self.port.solve(-self.q*y[self.iz:],jacobian=jac);self._tail_last=tail
        derivative=self.fun(np.array([self.end]),y[:,None],np.zeros(self.M))[:,0]
        residual=self.q*derivative[self.iz:]-np.asarray(tail['jets']['slope'])/math.sqrt(self.port.cut['E'])
        return residual/self.bcweights
    def bc(self,ya,yb,p):return np.r_[ya-self.initial(p),self.terminal(yb)]
    def bc_jac(self,ya,yb,p):
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n);B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        tail=self.port.solve(-self.q*yb[self.iz:],jacobian=True);TJ=np.array(tail['heightJetJacobian']).reshape(3*self.M+2,self.M)[:self.M]
        FJ,_=self.fun_jac(np.array([self.end]),yb[:,None],p);J=self.q*FJ[self.iz:,:,0]
        J[:,self.iz:]+=self.q*TJ/math.sqrt(self.port.cut['E']);B[self.n:]=J/self.bcweights[:,None]
        for j in range(self.M):
            step=2e-5 if j==0 else 2e-6/(self.pscale[j]*(j+1)**2);v=np.zeros(self.M);v[j]=step
            P[:self.n,j]=-(-self.initial(p+2*v)+8*self.initial(p+v)-8*self.initial(p-v)+self.initial(p-2*v))/(12*step)
        return A,B,P
    def seed(self,nodes):
        x=np.unique(np.r_[np.linspace(0,self.prefix_end,nodes),np.linspace(self.prefix_end,self.end,max(41,nodes//3))])
        f,g=self.linear[0].sol(x)/self.linear[0].y[1,-1]
        y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/2;y[self.iz]=g;p=np.zeros(self.M)
        left=self.initial(p)-y[:,0];y+=left[:,None]*(1-x/self.end)[None,:]**3
        return x,y,p
    def seam_audit(self,sol):
        y=sol.sol(np.array([self.end]));C=self.base(np.array([self.end]))+self.q*y
        Cp=self.base(np.array([self.end]),1)+self.q*sol.sol(np.array([self.end]),1)
        Cpp=self.base(np.array([self.end]),2)+self.q*sol.sol(np.array([self.end]),2)
        B,B1,B2=self.basis(max(256,self.nt));fr=self.frame(np.array([self.end]),C,B1,B2)
        dV=self.frame_jvp(fr,self.values(Cp,B1),self.values(Cp,B2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap']);be=-fr['alpha']*ae/fr['beta']
        dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin']
        mean1=float(np.mean(fr['V'][:,:,2]));mean2=float(np.mean(dV[:,:,2]))
        tail=self.port.solve(-self.q*y[self.iz:,0],jacobian=True,audit=True);jets=tail['jets'];E=jets['E'];Ep=jets['Ep'];v=-1/math.sqrt(E);vprime=-Ep/(2*E**2)
        # For z_curve=-z_tail, z_s=+z_tail,r/sqrt(E) and z_ss=-z_tail,rr/E-z_tail,r*a''.
        expected_mean1=jets['meanSlope']/math.sqrt(E)
        expected_mean2=-jets['meanSecond']/E-jets['meanSlope']*vprime
        expected_mode2=-np.asarray(jets['second'])/E-np.asarray(jets['slope'])*vprime
        return dict(finite_depth_only=True,tail_calls=self.port.calls,tail_converged=tail['converged'],tail_residual=tail['residual'],tail_jets=jets,tail_audit=tail.get('audit'),
            mean_first_jet_actual=mean1,mean_first_jet_expected=expected_mean1,mean_first_jet_mismatch=mean1-expected_mean1,
            mean_second_jet_actual=mean2,mean_second_jet_expected=expected_mean2,mean_second_jet_mismatch=mean2-expected_mean2,
            nonmean_first_jet_mismatch=float(np.max(abs(Cp[self.iz:,0]-np.asarray(jets['slope'])/math.sqrt(E)))),
            nonmean_second_jet_mismatch=float(np.max(abs(Cpp[self.iz:,0]-expected_mode2))),
            terminal_curvature_root=float(np.min(fr['margin'])),terminal_height_modes=(-self.q*y[self.iz:,0]).tolist())

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--tail-config',required=True);pa.add_argument('--out',required=True);pa.add_argument('--amplitude',type=float,default=.0001)
    pa.add_argument('--delta',type=float,default=.8);pa.add_argument('--velocity',type=float,default=.7);pa.add_argument('--ramp',type=float,default=.1);pa.add_argument('--cycles',type=int,default=1)
    pa.add_argument('--angular',type=int,default=96);pa.add_argument('--nodes',type=int,default=121);pa.add_argument('--max-nodes',type=int,default=4000);pa.add_argument('--tol',type=float,default=1e-6);pa.add_argument('--bc-tol',type=float,default=1e-6)
    pa.add_argument('--restart');pa.add_argument('--audit-points',type=int,default=301);pa.add_argument('--audit-angular',type=int,default=256)
    args=pa.parse_args();port=TailPort(args.tail_config);start=time.time();out=None
    try:
        obj=BridgeBVP(port,args.amplitude,args.delta,args.velocity,args.ramp,args.cycles,args.angular)
        x,y,p=obj.seed(args.nodes)
        if args.restart:
            old=load_checkpoint(args.restart);oldM=old['config']['modes'];oq=old['config']['amplitude'];Pold=PPoly.construct_fast(np.asarray(old['pp_coefficients']),np.asarray(old['mesh']),extrapolate=True,axis=1)
            x=np.asarray(old['mesh']);oy=Pold(x);y=np.zeros((obj.n,len(x)))
            y[0]=oy[0]*(obj.q/oq)
            for j in range(min(oldM,obj.M)):
                factor=(obj.q/oq)**j
                for i,k in [(1+j,1+j),(obj.M+1+j,oldM+1+j),(2*obj.M+1+j,2*oldM+1+j)]:y[i]=oy[k]*factor
            p=np.zeros(obj.M);p[0]=old['parameters'][0]*(obj.q/oq)**2
            for j in range(1,min(oldM,obj.M)):p[j]=old['parameters'][j]*max(oq**(j+1),1e-8)*(obj.q/oq)**(j+1)/obj.pscale[j]
        print(json.dumps(dict(event='initial',modes=obj.M,amplitude=obj.q,h0=obj.h0,bridge_length=obj.bridge.L,profile_cut=port.cut)),flush=True)
        sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2)
        sol.sol=obj.c2_interpolant(sol)
        audit=obj.audit_streamed(sol,args.audit_points,args.audit_angular);seam=obj.seam_audit(sol)
        out=dict(author='Astra / curve_transition; AI-assisted 2026-11-08',scope=__doc__,config={**vars(args),'modes':obj.M},success=bool(sol.success),message=sol.message,seconds=time.time()-start,
            parameters=sol.p.tolist(),core=obj.parameters(sol.p),h0=obj.h0,initial_linear_rhos=obj.rhos.tolist(),tail_parameters=port.ready['parameters'],bridge_length=obj.bridge.L,prefix_length=obj.prefix_end,
            nodes=len(sol.x),max_rms_residual=float(np.max(sol.rms_residuals)),summary=audit,seam=seam,mesh=sol.x.tolist(),pp_coefficients=sol.sol.c)
    except Exception as e:out=dict(author='Astra / curve_transition',config=vars(args),success=False,message=repr(e),seconds=time.time()-start,tail_calls=port.calls)
    finally:port.close()
    out=save_checkpoint(args.out,out)
    print(json.dumps({k:v for k,v in out.items() if k not in ('mesh','pp_coefficients','scope')},indent=2),flush=True)

if __name__=='__main__':main()
