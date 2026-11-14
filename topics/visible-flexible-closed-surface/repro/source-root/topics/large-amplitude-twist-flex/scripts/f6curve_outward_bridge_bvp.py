"""Complete spatial strong-cycle/bridge BVP with physical tail boundary data.
Astra curve_transition, AI-assisted 2026-11-08. Linear response is explicitly
marked when used. Nonlinear mode uses the actual finite compact-tail response;
neither mode alone supplies the infinite tail, caps, or full closed flex.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,time,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly
from f6curve_outward_bridge_linear import OutwardBridgeLinear,read_port
from f6curve_inward_bridge_bvp import InwardBridgeBVP
from curve_stable_prefix_bvp import save_checkpoint,load_checkpoint
from f6curve_domain_newton import install,STATS
from f6curve_outward_bvp import with_profile_breaks

class OutwardTailBVP(OutwardBridgeLinear):
    def __init__(self,port_data,port=None,**kwargs):
        self.port=port
        super().__init__(port_data,**kwargs)
        # Projecting an O(1) background velocity gives a float64 noise floor
        # around 1e-15 in the tiny high-mode physical slopes. A 1e-6 weight
        # puts their requested absolute BC tolerance near 3e-14, well below
        # any geometric tolerance, without demanding a sub-roundoff residual.
        self.bcweights=np.maximum(self.bscale,1e-6)
    def terminal(self,y,jac=True):
        derivative=self.fun(np.array([self.end]),y[:,None],np.zeros(self.M))[:,0]
        if self.port is None:slope=self.linearD*(self.sigma*self.q*y[self.iz:])
        else:slope=np.asarray(self.port.solve(self.sigma*self.q*y[self.iz:],jacobian=jac)['jets']['slope'])
        return (self.q*derivative[self.iz:]-slope/math.sqrt(self.port_data['cut']['E']))/self.bcweights
    def bc(self,ya,yb,p):return np.r_[ya-self.initial(p),self.terminal(yb)]
    def bc_jac(self,ya,yb,p):
        A=np.zeros((self.n+self.M,self.n));A[:self.n]=np.eye(self.n);B=np.zeros_like(A);P=np.zeros((self.n+self.M,self.M))
        if self.port is None:TJ=np.diag(self.linearD)
        else:TJ=np.array(self.port.solve(self.sigma*self.q*yb[self.iz:],jacobian=True)['heightJetJacobian']).reshape(3*self.M+2,self.M)[:self.M]
        FJ,_=self.fun_jac(np.array([self.end]),yb[:,None],p);J=self.q*FJ[self.iz:,:,0]
        J[:,self.iz:]-=self.sigma*self.q*TJ/math.sqrt(self.port_data['cut']['E']);B[self.n:]=J/self.bcweights[:,None]
        if hasattr(self,'initial_parameter_jacobian'):P[:self.n]=-self.initial_parameter_jacobian(p)
        else:
            for j in range(self.M):
                step=2e-5 if j==0 else 2e-6/(self.pscale[j]*(j+1)**2);v=np.zeros(self.M);v[j]=step
                P[:self.n,j]=-(-self.initial(p+2*v)+8*self.initial(p+v)-8*self.initial(p-v)+self.initial(p-2*v))/(12*step)
        return A,B,P
    def seam_audit(self,sol):
        if self.port is not None:
            result=InwardBridgeBVP.seam_audit(self,sol)
            if hasattr(self.port,'lowM'):
                y=sol.sol(np.array([self.end]));H=self.sigma*self.q*y[self.iz:,0]
                tail=self.port.solve(H,jacobian=True);actual=tail['actual_tail_jets'];E=actual['E'];rss=-actual['Ep']/(2*E*E)
                Cp=self.base(np.array([self.end]),1)+self.q*sol.sol(np.array([self.end]),1)
                Cpp=self.base(np.array([self.end]),2)+self.q*sol.sol(np.array([self.end]),2)
                result['mixed_boundary_jets']=result.pop('tail_jets');result['tail_jets']=actual
                result['mixed_boundary_nonmean_first_jet_mismatch']=result['nonmean_first_jet_mismatch']
                result['mixed_boundary_nonmean_second_jet_mismatch']=result['nonmean_second_jet_mismatch']
                result['nonmean_height_mismatch']=float(np.max(abs(H-np.asarray(actual['height']))))
                result['nonmean_first_jet_mismatch']=float(np.max(abs(Cp[self.iz:,0]-np.asarray(actual['slope'])/math.sqrt(E))))
                expected2=self.sigma*(np.asarray(actual['second'])/E+np.asarray(actual['slope'])*rss)
                result['nonmean_second_jet_mismatch']=float(np.max(abs(Cpp[self.iz:,0]-expected2)))
                result['mixed_truncation']=tail['mixed_truncation'];result['tail_audit_scope']=tail['audit_scope']
                result['seam_scope']='Literal low-mode tail height jets, before any Cartesian jet repair. Mixed closure mismatch is recorded separately; no exact C2 seam assertion.'
            return result
        end=sol.sol(np.array([self.end]));H=self.sigma*self.q*end[self.iz:,0]
        return dict(scope='Physical linear finite-far tail response only; no nonlinear seam certificate.',terminal_physical_height=H.tolist(),nonmean_slope_residual=float(np.max(abs(self.terminal(end[:,0])*self.bcweights))),tail_linear_slope=(self.linearD*H).tolist())
    def restart(self,path,nodes):
        old=load_checkpoint(path);oc=old['config'];M0=oc['modes'];q0=oc['amplitude']
        for k,expected in [('delta',self.delta),('v_up',self.vu),('v_down',self.vd),('ramp',self.eps),('cycles',self.cycles),('base_mode',self.base_mode)]:
            if oc[k]!=expected:raise ValueError('Restart profile mismatch: '+k)
        ox=np.asarray(old['mesh']);P=PPoly.construct_fast(np.asarray(old['pp_coefficients']),ox,extrapolate=True,axis=1)
        full=abs(ox[-1]-self.end)<1e-10
        if not full and abs(ox[-1]-self.prefix_end)>1e-10:raise ValueError('Restart has incompatible endpoint')
        x=with_profile_breaks(ox,self.breaks,self.period) if full else with_profile_breaks(np.r_[ox,np.linspace(self.prefix_end,self.end,max(81,nodes//2))],self.breaks,self.period);sx=np.minimum(x,ox[-1]);oy=P(sx);y=np.zeros((self.n,len(x)));y[0]=oy[0]*self.q/q0
        for j in range(min(M0,self.M)):
            scale=(self.q/q0)**j
            for i,k in [(1+j,1+j),(self.M+1+j,M0+1+j),(self.iz+j,2*M0+1+j)]:y[i]=oy[k]*scale
        p=np.zeros(self.M);p[0]=old['parameters'][0]*(self.q/q0)**2+old['h0']-self.h0
        for j in range(1,min(M0,self.M)):p[j]=old['parameters'][j]*max(q0**(j+1),1e-8)*(self.q/q0)**(j+1)/self.pscale[j]
        if not full:
            # The new physical endpoint changes the second cycle only by its
            # tiny decaying input. Use the complete linear shape in the bridge
            # and join continuously at prefix_end; Newton solves all its jets.
            mask=x>=self.prefix_end;f,g=self.linear[0].sol(x[mask]);y[:,mask]=0.;y[1,mask]=f;y[self.M+1,mask]=-f/self.base_mode;y[self.iz,mask]=g
            ix=np.flatnonzero(mask)[0];oldend=np.zeros(self.n);oldv=P(np.array([self.prefix_end]))[:,0]
            oldend[0]=oldv[0]*self.q/q0
            for j in range(min(M0,self.M)):
                sc=(self.q/q0)**j
                for i,k in [(1+j,1+j),(self.M+1+j,M0+1+j),(self.iz+j,2*M0+1+j)]:oldend[i]=oldv[k]*sc
            y[:,mask]+=(oldend-y[:,ix])[:,None]*(1-(x[mask]-self.prefix_end)/self.bridge.L)[None,:]**3
        return x,y,p
    def audit_streamed(self,*args,**kwargs):
        out=super().audit_streamed(*args,**kwargs)
        out['collar_scope']='Finite strong cycles + turning bridge, with '+('explicit mixed low nonlinear/high linear finite-tail closure; literal tail contains only low modes.' if hasattr(self.port,'lowM') else ('actual nonlinear finite-depth compact DN.' if self.port else 'actual-profile linear finite-far Robin port only.'))+' No infinite-tail/closed-flex assertion.'
        return out

def main():
    pa=argparse.ArgumentParser();pa.add_argument('--linear-port',required=True);pa.add_argument('--tail-config');pa.add_argument('--out',required=True);pa.add_argument('--modes',type=int,default=6);pa.add_argument('--amplitude',type=float,default=.005);pa.add_argument('--delta',type=float,default=.2571428571428571);pa.add_argument('--v-up',type=float,default=.8);pa.add_argument('--v-down',type=float,default=.999);pa.add_argument('--ramp',type=float,default=.05);pa.add_argument('--cycles',type=int,default=2);pa.add_argument('--base-mode',type=int,default=6);pa.add_argument('--angular',type=int,default=384);pa.add_argument('--nodes',type=int,default=181);pa.add_argument('--max-nodes',type=int,default=10000);pa.add_argument('--tol',type=float,default=3e-7);pa.add_argument('--bc-tol',type=float,default=3e-8);pa.add_argument('--audit-points',type=int,default=401);pa.add_argument('--audit-angular',type=int,default=768);pa.add_argument('--restart');pa.add_argument('--local-frame',action='store_true');pa.add_argument('--analytic-core-jac',action='store_true');pa.add_argument('--mixed-tail',action='store_true');args=pa.parse_args();start=time.time();port=None;install()
    out=None;stage='initialization'
    try:
        data=read_port(args.linear_port)
        if args.tail_config:
            from f6curve_compact_tail_port import CompactTailPort
            port=CompactTailPort(args.tail_config,args.linear_port)
            if args.mixed_tail:
                from f6curve_mixed_tail_port import MixedTailPort
                port=MixedTailPort(port,data,args.modes,args.base_mode)
            if port.M!=args.modes:raise ValueError('Tail and prefix modes must match unless explicit --mixed-tail is selected')
            data['cut']=port.cut;data['linearSlope']=port.linearD.tolist()
        obj=OutwardTailBVP(data,port=port,modes=args.modes,amplitude=args.amplitude,delta=args.delta,vu=args.v_up,vd=args.v_down,eps=args.ramp,cycles=args.cycles,angular=args.angular,base_mode=args.base_mode)
        if args.local_frame:
            from f6curve_local_frame import install_local_frame
            install_local_frame(obj)
        if args.analytic_core_jac:
            from f6curve_core_variation import install_analytic_core_jacobian
            install_analytic_core_jacobian(obj)
        x,y,p=obj.restart(args.restart,args.nodes) if args.restart else obj.seed(args.nodes)
        print(json.dumps(dict(event='start',M=obj.M,q=obj.q,h0=obj.h0,Lbeforetail=2*(obj.h0+obj.end),bridge_length=obj.bridge.L,tail_mode='nonlinear' if port else 'linear',fundamental_linear_gain=obj.linear[0].gain)),flush=True)
        stage='boundary_solve';sol=solve_bvp(obj.fun,obj.bc,x,y,p,tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,fun_jac=obj.fun_jac,bc_jac=obj.bc_jac,verbose=2);sol.sol=obj.c2_interpolant(sol)
        out=dict(author='Astra curve_transition; AI-assisted',scope=__doc__,config=vars(args),success=False,solver_success=bool(sol.success),audit_success=False,message=sol.message,seconds=time.time()-start,parameters=sol.p.tolist(),core=obj.parameters(sol.p),h0=obj.h0,rhos=obj.rhos.tolist(),linear_directions=obj.rows,newton_domain_audit=dict(STATS),analytic_core_jac_audit=getattr(obj,'analytic_core_jac_audit',None),nodes=len(sol.x),max_rms_collocation_residual=float(np.max(sol.rms_residuals)),mesh=sol.x.tolist(),pp_coefficients=sol.sol.c)
        # Persist the complete numerical geometry before an expensive diagnostic
        # can fail. save_checkpoint consumes pp_coefficients and retains chunks.
        out=save_checkpoint(args.out,out);stage='prefix_audit';out['summary']=obj.audit_streamed(sol,args.audit_points,args.audit_angular);stage='tail_seam_audit';out['seam']=obj.seam_audit(sol);out['audit_success']=True;out['success']=bool(sol.success);out['seconds']=time.time()-start
    except Exception as e:
        if out is None:out=dict(author='Astra curve_transition; AI-assisted',config=vars(args),success=False,newton_domain_audit=dict(STATS))
        out.update(success=False,message=repr(e),seconds=time.time()-start,failure_stage=stage)
    finally:
        if port is not None:port.close()
    out=save_checkpoint(args.out,out);print(json.dumps({k:v for k,v in out.items() if k in ['success','message','seconds','nodes','summary','seam','newton_domain_audit']},indent=2),flush=True)
if __name__=='__main__':main()
