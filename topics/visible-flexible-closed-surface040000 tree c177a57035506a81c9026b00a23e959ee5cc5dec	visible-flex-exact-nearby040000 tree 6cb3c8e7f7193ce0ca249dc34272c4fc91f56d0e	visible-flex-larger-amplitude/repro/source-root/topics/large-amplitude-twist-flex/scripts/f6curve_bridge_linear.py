"""Linear matching of an exact rectifying core to a turning bridge and tail DN.
Astra / curve_transition; AI-assisted, 2026-11-08. Finite-depth diagnostic only.
"""
from pathlib import Path
import sys, subprocess, json, math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
sys.path.insert(0,str(Path(__file__).parent))
from curve_stable_prefix_bvp import CylindricalPrefix

class TurningBridge:
    def __init__(self,cut,a_start=1.):
        self.cut=cut;self.astart=a_start;self.at=cut['radius'];self.w=cut['backgroundSlope'];self.wr=cut['backgroundSecond']
        self.pt=math.atan2(1,self.w);self.ps=self.wr/(1+self.w*self.w)**1.5
        self.g,self.gw=np.polynomial.legendre.leggauss(48)
        def drop(L):return L*self.integral(np.array([1.]),L)[0]
        self.L=brentq(lambda L:drop(L)-(a_start-self.at),.01,2.)
    def turn(self,t,L=None):
        if L is None:L=self.L
        t=np.asarray(t);p=self.pt*(3*t*t-2*t**3)+L*self.ps*(t**3-t*t)
        dp=(self.pt*(6*t-6*t*t)+L*self.ps*(3*t*t-2*t))/L
        return p,dp
    def integral(self,t,L=None):
        if L is None:L=self.L
        x=np.asarray(t)[:,None]*(1+self.g[None,:])/2
        p,_=self.turn(x,L)
        return np.asarray(t)/2*(np.sin(p)@self.gw)
    def profile(self,s):
        t=np.asarray(s)/self.L;p,dp=self.turn(t)
        a=self.astart-self.L*self.integral(t)
        return a,-np.sin(p),-np.cos(p)*dp


def get_tail(config):
    exe=Path(__file__).with_name('f6curve_tail_port.mjs')
    z=subprocess.run(['node',str(exe),str(config)],input='',capture_output=True,text=True,check=True)
    return json.loads(z.stdout.splitlines()[0])


def run(config,cycles=1,delta=.8,velocity=.7,eps=.1):
    port=get_tail(config);cut=port['cut'];bridge=TurningBridge(cut)
    M=len(port['linearSlope']);obj=CylindricalPrefix(M,.001,delta,velocity,velocity,eps,cycles,128,0.)
    def profile(s):
        z=np.atleast_1d(s);a,v,acc=obj.profile(np.minimum(z,obj.end))
        mask=z>obj.end
        if np.any(mask):a[mask],v[mask],acc[mask]=bridge.profile(z[mask]-obj.end)
        return a,v,acc
    rows=[]
    for j,D in enumerate(port['linearSlope']):
        m=2*(j+1);a=cut['radius'];w=cut['backgroundSlope'];terminal=np.array([-w*(a*D-m*m)/(m*m-1),1.])
        def rhs(s,y):
            a,v,_=profile(s);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],(m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a
        end=obj.end+bridge.L
        sol=solve_ivp(rhs,[end,0],terminal,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True,max_step=.01)
        core=sol.y[:,-1];rho=core[1]/core[0];h=-1/(4*rho) if m==2 else None
        vinterface=sol.sol(obj.end);interface_rho=vinterface[1]/vinterface[0]
        rows.append(dict(mode=m,terminal_f_over_g=float(terminal[0]),initial_rho=float(rho),core_h_if_m2=h,bridge_entry_rho=float(interface_rho),terminal_amplitude_for_core_g1=float(1/core[1]),max_linear_amplitude=float(np.max(np.abs(sol.y)))))
    h=rows[0]['core_h_if_m2']
    for row in rows:
        m=row['mode'];rho=row['initial_rho'];direction=np.array([1.,0.]) if m%4==0 else np.array([-m*m*h,1.])
        row['core_transversality']=abs(direction[1]-rho*direction[0])/(math.hypot(1,rho)*np.linalg.norm(direction))
    return dict(scope='Finite-depth linear tail matching; no nonlinear or infinite-tail result',config=str(config),cut=cut,bridge_length=bridge.L,bridge_turn_terminal=bridge.pt,bridge_turn_slope_terminal=bridge.ps,profile_terminal=tuple(float(x[0]) for x in bridge.profile(np.array([bridge.L]))),prefix_length=obj.end,total_right_length=obj.end+bridge.L,modes=rows)

if __name__=='__main__':
    out=run(sys.argv[1],int(sys.argv[3]) if len(sys.argv)>3 else 1)
    Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
