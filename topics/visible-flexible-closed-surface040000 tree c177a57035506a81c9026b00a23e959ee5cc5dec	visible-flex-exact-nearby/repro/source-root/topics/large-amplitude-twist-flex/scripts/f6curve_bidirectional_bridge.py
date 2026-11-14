"""Directional meridian bridge and full physical linear tail matching.
Astra curve_transition, AI-assisted 2026-11-08. Finite-depth linear diagnostics;
no claim of a nonlinear solution, a true collar, or a completed flex.
"""
from pathlib import Path
import argparse,json,math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
from f6curve_bridge_linear import get_tail
from f6curve_inward_bvp import InwardPrefix

class DirectionalBridge:
    def __init__(self,cut,a_start=1.):
        self.cut=cut; self.astart=a_start; self.at=cut['radius']; self.w=cut['backgroundSlope']; self.wr=cut['backgroundSecond']
        self.sigma=float(np.sign(self.at-a_start))
        if self.sigma==0:raise ValueError('Bridge requires distinct endpoint radii')
        self.pt=math.atan2(1.,self.w);self.ps=-self.sigma*self.wr/(1+self.w*self.w)**1.5
        self.g,self.gw=np.polynomial.legendre.leggauss(64)
        def gap(L):return L*self.integral(np.array([1.]),L)[0]-abs(self.at-a_start)
        vals=np.geomspace(1e-5,10.,300); left=None
        for u,v in zip(vals[:-1],vals[1:]):
            if gap(u)*gap(v)<=0:left=(u,v);break
        if left is None:raise ValueError('No positive bridge length in checked interval')
        self.L=brentq(gap,*left,xtol=2e-14)
        phi,dphi=self.turn(np.linspace(0,1,1001)); self.min_angle=float(phi.min()); self.max_angle=float(phi.max())
        if self.min_angle<-1e-9 or self.max_angle>math.pi/2+1e-9:raise ValueError('Hermite bridge leaves positive meridian chart')
    def turn(self,t,L=None):
        if L is None:L=self.L
        t=np.asarray(t);p=self.pt*(3*t*t-2*t**3)+L*self.ps*(t**3-t*t)
        dp=(self.pt*(6*t-6*t*t)+L*self.ps*(3*t*t-2*t))/L
        return p,dp
    def integral(self,t,L=None):
        if L is None:L=self.L
        t=np.asarray(t);x=t[:,None]*(1+self.g[None,:])/2;p,_=self.turn(x,L)
        return t/2*(np.sin(p)@self.gw)
    def profile(self,s):
        t=np.asarray(s)/self.L;p,dp=self.turn(t)
        a=self.astart+self.sigma*self.L*self.integral(t)
        return a,self.sigma*np.sin(p),self.sigma*np.cos(p)*dp

class LinearBridgePrefix:
    def __init__(self,port,delta_raw=.3,vu=.4,vd=.6,eps=.2,cycles=1):
        self.port=port;self.bridge=DirectionalBridge(port['cut']);self.M=len(port['linearSlope'])
        self.prefix=InwardPrefix(self.M,.001,delta_raw,vu,vd,eps,cycles,128,compute_stable=False)
        self.prefix_end=self.prefix.end;self.end=self.prefix_end+self.bridge.L;self.solutions=[];self.rows=[]
        for j,D in enumerate(port['linearSlope']):
            m=2*(j+1);a=port['cut']['radius'];w=port['cut']['backgroundSlope'];terminal=np.array([self.bridge.sigma*w*(a*D-m*m)/(m*m-1),1.])
            def rhs(s,y):
                a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
                return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],(m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a
            z=solve_ivp(rhs,[self.end,0],terminal,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True,max_step=.005)
            self.solutions.append(z);p=z.y[:,-1];interface=z.sol(self.prefix_end);rho=float(p[1]/p[0]);
            self.rows.append(dict(mode=m,initial_rho=rho,core_h_if_m2=-1/(4*rho) if m==2 else None,terminal_f_over_g=float(terminal[0]),bridge_entry_rho=float(interface[1]/interface[0]),terminal_g_over_core_g=float(1/p[1]),maximum_raw_amplitude=float(abs(z.y).max())))
        self.h0=self.rows[0]['core_h_if_m2']
        for row in self.rows:
            m=row['mode'];rho=row['initial_rho'];core=np.array([1.,0.]) if m%4==0 else np.array([-m*m*self.h0,1.])
            row['core_transversality']=abs(core[1]-rho*core[0])/(math.hypot(1,rho)*np.linalg.norm(core))
    def profile(self,s):
        s=np.atleast_1d(s);a,v,acc=self.prefix.profile(np.minimum(s,self.prefix_end));mask=s>self.prefix_end
        if np.any(mask):a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc
    def summary(self):
        return dict(scope=__doc__,cut=self.port['cut'],bridge_sigma=self.bridge.sigma,bridge_length=self.bridge.L,bridge_angle_range=[self.bridge.min_angle,self.bridge.max_angle],profile_terminal=[float(x[0]) for x in self.bridge.profile(np.array([self.bridge.L]))],prefix_length=self.prefix_end,total_right_length=self.end,h0=self.h0,Lband_without_tail=2*(self.h0+self.end),modes=self.rows)

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--tail-config',required=True);pa.add_argument('--out',required=True);pa.add_argument('--delta-raw',type=float,default=.3);pa.add_argument('--v-up',type=float,default=.4);pa.add_argument('--v-down',type=float,default=.6);pa.add_argument('--ramp',type=float,default=.2);pa.add_argument('--cycles',type=int,default=1);args=pa.parse_args()
    port=get_tail(args.tail_config)
    try:z=LinearBridgePrefix(port,args.delta_raw,args.v_up,args.v_down,args.ramp,args.cycles).summary()
    except Exception as e:z=dict(failed=True,error=repr(e),config=vars(args),cut=port['cut'])
    Path(args.out).write_text(json.dumps(z,indent=2)+'\n'); print(json.dumps(z,indent=2))
