#!/usr/bin/env python3
"""C2 inward bridge with bounded turning angle, plus linear design screening.

The angle rises by a cubic smoothstep, stays constant, and finishes with a
quadratic decrease. A positive plateau length pays the exact radial drop.
This defines an actual smooth metric profile; the linear search does not
solve its nonlinear isometric embedding or establish a closed surface.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,importlib.util,json,math,time
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

class ShortBridge:
    def __init__(self,cut,a_start=1.,curvature=8.,peak_fraction=.5):
        self.cut=cut;self.astart=float(a_start);self.at=float(cut['radius'])
        self.w=float(cut['backgroundSlope']);self.wr=float(cut['backgroundSecond']);self.sigma=-1.
        if not(0<self.at<self.astart and self.w>0 and self.wr<0 and curvature>0 and 0<peak_fraction<1):
            raise ValueError('ShortBridge requires an inward positive-slope cut and valid bounds')
        self.pt=math.atan2(1.,self.w);self.ps=self.wr/(1+self.w*self.w)**1.5
        self.peak=self.pt+peak_fraction*(math.pi/2-self.pt);self.eps=self.peak-self.pt
        self.L1=1.5*self.peak/curvature;self.L3=2*self.eps/(-self.ps)
        self.g,self.gw=np.polynomial.legendre.leggauss(64)
        radial1=self.L1*self.integral(np.array([1.]),0,'sin')[0]
        radial3=self.L3*self.integral(np.array([1.]),2,'sin')[0]
        self.L2=(self.astart-self.at-radial1-radial3)/math.sin(self.peak)
        if self.L2<0:raise ValueError('No positive plateau at this curvature bound')
        self.L=self.L1+self.L2+self.L3
        self.breakpoints=np.array([0.,self.L1,self.L1+self.L2,self.L])
        self.min_angle=0.;self.max_angle=self.peak
        self.parameters=dict(kind='turn_plateau_v1',curvature=curvature,peak_fraction=peak_fraction)

    def integral(self,u,part,trig='sin'):
        u=np.atleast_1d(np.asarray(u,float));x=u[:,None]*(1+self.g)/2
        phi=self.peak*(3*x*x-2*x*x*x)if part==0 else self.peak-self.eps*x*x
        fun=np.sin if trig=='sin'else np.cos
        return u/2*(fun(phi)@self.gw)

    def angle(self,s):
        s=np.asarray(s,float);u=np.clip(s/self.L1,0.,1.);v=np.clip((s-self.L1-self.L2)/self.L3,0.,1.)
        phi=np.where(s<=self.L1,self.peak*(3*u*u-2*u*u*u),np.where(s<=self.L1+self.L2,self.peak,self.peak-self.eps*v*v))
        derivative=np.where(s<=self.L1,6*self.peak*u*(1-u)/self.L1,np.where(s<=self.L1+self.L2,0.,-2*self.eps*v/self.L3))
        return phi,derivative

    def profile(self,s):
        s=np.atleast_1d(np.asarray(s,float));u=np.clip(s/self.L1,0.,1.);v=np.clip((s-self.L1-self.L2)/self.L3,0.,1.)
        drop=self.L1*self.integral(u,0)+np.clip(s-self.L1,0.,self.L2)*math.sin(self.peak)+self.L3*self.integral(v,2)
        phi,derivative=self.angle(s)
        return self.astart-drop,-np.sin(phi),-np.cos(phi)*derivative

    def linear(self,mode,slope):
        self.mode=mode;m2=mode*mode;w=self.w;r=self.at
        terminal=np.array([-w*(r*slope-m2)/(m2-1),1.]);terminal/=np.linalg.norm(terminal)
        def rhs(s,y):
            a,v,_=self.profile(s);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return np.array([-(m2-1)*v*y[0]-m2*b*y[1],(m2-1)*v*v*y[0]/b+m2*v*y[1]])/a
        self.solution=solve_ivp(rhs,(self.L,0.),terminal,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True,max_step=self.L/120)
        if not self.solution.success:raise RuntimeError(self.solution.message)
        self.initial=self.solution.y[:,-1];self.initial/=np.linalg.norm(self.initial)
        return self

    def summary(self):
        height=self.L1*self.integral(np.array([1.]),0,'cos')[0]+self.L2*math.cos(self.peak)+self.L3*self.integral(np.array([1.]),2,'cos')[0]
        return dict(parameters=self.parameters,cut=self.cut,length=self.L,pieces=[self.L1,self.L2,self.L3],height=float(height),
            angle_max=self.peak,minimum_cosine=math.cos(self.peak),meridian_curvature_bound=max(self.parameters['curvature'],abs(self.ps)),
            parallel_curvature_bound=1/self.at,initial_jets=[float(z[0])for z in self.profile([0.])],
            terminal_jets=[float(z[0])for z in self.profile([self.L])],scope=__doc__)

def install():
    """Dispatch only explicitly tagged cuts; leave legacy cut behavior intact."""
    import f6curve_bidirectional_bridge as bridge_module
    import fixed_metric_mode3_flow as flow_module
    if not hasattr(bridge_module,'_larger_original_bridge'):
        bridge_module._larger_original_bridge=bridge_module.DirectionalBridge
    original=bridge_module._larger_original_bridge
    def factory(cut,a_start=1.):
        spec=cut.get('_prefix_bridge')
        if spec is None:return original(cut,a_start)
        if spec['kind']!='turn_plateau_v1':raise ValueError('Unknown prefix bridge')
        return ShortBridge(cut,a_start,spec['curvature'],spec['peak_fraction'])
    bridge_module.DirectionalBridge=factory;flow_module.DirectionalBridge=factory
    if not getattr(flow_module.PlanarSymmetryFlow,'_larger_short_breaks_installed',False):
        old_init=flow_module.PlanarSymmetryFlow.__init__
        def init(self,*args,**kwargs):
            old_init(self,*args,**kwargs)
            if hasattr(self.bridge,'breakpoints'):
                self.breaks=np.unique(np.r_[self.breaks,self.prefix_end+self.bridge.breakpoints])
        flow_module.PlanarSymmetryFlow.__init__=init
        flow_module.PlanarSymmetryFlow._larger_short_breaks_installed=True

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--port',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--curvature',type=float,default=8.);p.add_argument('--vu',type=float,default=.55)
    p.add_argument('--search',action='store_true');a=p.parse_args();started=time.time()
    port=json.loads(a.port.read_text());b=ShortBridge(port['cut'],curvature=a.curvature);report=dict(bridge=b.summary(),rows=[])
    if a.search:
        path=Path(__file__).with_name('root_profile_scan.py');spec=importlib.util.spec_from_file_location('short_design',path);d=importlib.util.module_from_spec(spec);spec.loader.exec_module(d)
        bridges=[ShortBridge(port['cut'],curvature=a.curvature).linear(m,port['linearSlope'][port['modes'].index(m)])for m in (2,4)]
        def cfg(x):return dict(direction='outward',vu=a.vu,vd=float(x[1]),delta=float(x[0]),ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=1,prefix_bridge=b.parameters)
        def residual(x):return np.array([d.Design(cfg(x),bb).core_line(rtol=3e-10)[0][1]for bb in bridges])
        for seed in ((.16,.45),(.12,.6),(.22,.3)):
            z=least_squares(residual,seed,bounds=([.005,.05],[.6,.94]),xtol=2e-10,gtol=2e-10,ftol=2e-10,max_nfev=70)
            rr=residual(z.x);row=dict(profile=cfg(z.x),residual=rr.tolist(),linear_candidate=bool(max(abs(rr))<1e-6))
            if row['linear_candidate']:row['mode2']=d.Design(cfg(z.x),bridges[0]).summary()
            report['rows'].append(row);report['seconds']=time.time()-started;a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(row),flush=True)
    report['seconds']=time.time()-started;a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(bridge=report['bridge'],seconds=report['seconds'])),flush=True)

if __name__=='__main__':main()
