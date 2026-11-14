"""Strong outward cycles followed by a physical turning bridge and true linear tail port.
Astra curve_transition, AI-assisted 2026-11-08. Every line is propagated in physical
curve variables with normalization at each smooth radial subsegment. Finite-far
tail data remain numerical data; no rotational-collar or nonlinear assertion.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,json,math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from f6curve_outward_bvp import OutwardPrefix
from f6curve_bidirectional_bridge import DirectionalBridge

class BackwardLine:
    def __init__(self,rhs,breaks,terminal):
        terminal=np.asarray(terminal,float);v=terminal/np.linalg.norm(terminal)
        self.terminal=v.copy();self.segments=[];logscale=0.
        for lo,hi in reversed(list(zip(breaks[:-1],breaks[1:]))):
            z=solve_ivp(rhs,[hi,lo],v,method='DOP853',rtol=3e-12,atol=3e-14,dense_output=True,max_step=(hi-lo)/24)
            if not z.success:raise RuntimeError(z.message)
            self.segments.append((lo,hi,z.sol,logscale))
            end=z.y[:,-1];n=np.linalg.norm(end)
            if not np.isfinite(n) or n<=0:raise FloatingPointError('Backward physical line lost scale')
            logscale+=math.log(n);v=end/n
        self.core=v;self.logscale=logscale;self.rho=float(v[1]/v[0]);self.segments.reverse()
        self.gain=float(self.terminal[1]*math.exp(-logscale)/v[1])
    def sol(self,s):
        s=np.atleast_1d(s);out=np.empty((2,len(s)))
        for k,(lo,hi,z,scale) in enumerate(self.segments):
            mask=(s>=lo)&((s<hi) if k+1<len(self.segments) else (s<=hi))
            if np.any(mask):out[:,mask]=z(s[mask])*math.exp(scale-self.logscale)/self.core[1]
        return out

class OutwardBridgeLinear(OutwardPrefix):
    def __init__(self,port,modes=6,amplitude=.0075,delta=.2571428571428571,vu=.8,vd=.999,eps=.05,cycles=2,angular=384,base_mode=6):
        self.bridge=None;self.port_data=port
        super().__init__(modes,amplitude,delta,vu,vd,eps,cycles,angular,base_mode,compute_stable=False)
        self.prefix_end=self.end;self.bridge=DirectionalBridge(port['cut']);self.end=self.prefix_end+self.bridge.L;self.sigma=self.bridge.sigma
        self.linearD=np.asarray(port['linearSlope'][:modes]);self.linear=[]
        if len(self.linearD)!=modes:raise ValueError('Not enough physical linear tail modes')
        self.breaks=[]
        for c in range(cycles):
            b=c*self.period
            self.breaks.extend(b+np.array([0,self.eps*self.Tu,(1-self.eps)*self.Tu,self.Tu,self.Tu+self.eps*self.Td,self.Tu+(1-self.eps)*self.Td,self.period]))
        self.breaks=np.unique(np.r_[self.breaks,self.end]);self.rows=[]
        for m,D in zip(self.even,self.linearD):
            r=port['cut']['radius'];w=port['cut']['backgroundSlope'];terminal=np.array([self.sigma*w*(r*D-m*m)/(m*m-1),1.])
            line=BackwardLine(lambda s,y:self.linear_rhs(s,y,int(m)),self.breaks,terminal);self.linear.append(line)
            self.rows.append(dict(mode=int(m),physical_tail_D=float(D),rho=line.rho,terminal_g_over_core_g=line.gain,bridge_entry=line.sol(np.array([self.prefix_end]))[:,0].tolist(),logscale=line.logscale))
        self.rhos=np.array([line.rho for line in self.linear]);self.h0=-1/(base_mode**2*self.rhos[0])
        if self.h0<=0:raise ValueError('Complete core-to-tail line requires h<=0')
        for row in self.rows:
            m=row['mode'];rho=row['rho'];v=np.array([1.,0.]) if m%4==0 else np.array([-m*m*self.h0,1.])
            row['core_transversality']=float(abs(v[1]-rho*v[0])/(np.linalg.norm(v)*math.hypot(1,rho)))
    def profile(self,s):
        s=np.atleast_1d(s)
        if self.bridge is None:return super().profile(s)
        a,v,acc=super().profile(np.minimum(s,self.prefix_end));mask=s>self.prefix_end
        if np.any(mask):a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc
    def seed(self,nodes):
        x=np.unique(np.r_[np.linspace(0,self.prefix_end,nodes*self.cycles),np.linspace(self.prefix_end,self.end,max(61,nodes//2)),self.breaks]);p=np.zeros(self.M)
        f,g=self.linear[0].sol(x);y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/self.base_mode;y[self.iz]=g
        y+=(self.initial(p)-y[:,0])[:,None]*np.maximum(0,1-x/(self.Tu/2))[None,:]**3
        return x,y,p
    def linear_summary(self):
        x=np.unique(np.r_[np.linspace(0,self.end,4097),self.breaks]);a,v,acc=self.profile(x);B,B1,B2=self.basis(768)
        f,g=self.linear[0].sol(x);y=np.zeros((self.n,len(x)));y[1]=f;y[self.M+1]=-f/self.base_mode;y[self.iz]=g
        margin=math.inf;where=None
        for start in range(0,len(x),96):
            sl=slice(start,start+96);C=self.base(x[sl])+self.q*y[:,sl];fr=self.frame(x[sl],C,B1,B2);mins=np.min(fr['margin'],axis=1);j=int(np.argmin(mins))
            if mins[j]<margin:margin=float(mins[j]);where=float(x[sl][j])
        z=np.trapezoid(np.sqrt(1-v*v),x)
        return dict(scope=__doc__,q=self.q,h0=self.h0,period=self.period,prefix_length=self.prefix_end,bridge_length=self.bridge.L,right_length_before_tail=self.end,Lband_without_tail=2*(self.h0+self.end),height_before_tail=float(z+self.h0),first_order_root=margin,worst_s=where,background_kappa=float(np.max(abs(acc)/np.sqrt(1-v*v))),cut=self.port_data['cut'],modes=self.rows,first_order_terminal_physical_height=float(self.q*self.linear[0].gain))

def read_port(path):
    d=json.loads(Path(path).read_text());p=d['parameters'];w=p['wCut'];r=p['rCut'];wr=-7*w/r
    return dict(cut=dict(radius=r,backgroundSlope=w,backgroundSecond=wr,E=1+w*w,Ep=2*w*wr),linearSlope=[v['slope'] for v in d['rows'][-1]['modes']],linearModes=[v['mode'] for v in d['rows'][-1]['modes']],linearRadialComparison=d.get('radial_comparison'),linearParameters=p,geometry=d['geometry'],source=str(path))

if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('--port',required=True);pa.add_argument('--out',required=True);pa.add_argument('--modes',type=int,default=12);pa.add_argument('--amplitude',type=float,default=.0075);a=pa.parse_args()
    obj=OutwardBridgeLinear(read_port(a.port),modes=a.modes,amplitude=a.amplitude);out=obj.linear_summary();Path(a.out).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
