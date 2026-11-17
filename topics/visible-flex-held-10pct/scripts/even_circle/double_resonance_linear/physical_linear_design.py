"""Independent physical-profile linear resonance diagnostics.

This module imports the original flat law and ShortBridge without changing
them. Every design uses the literal frequencies and DN of one actual tail.
No linear design is a nonlinear isometric surface or a geometry certificate.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp,quad


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


class PhysicalDesign:
    def __init__(self,source_root,port_file):
        self.source=Path(source_root);self.port_path=Path(port_file)
        self.port=json.loads(self.port_path.read_text())
        self.flat_path=self.source/'topics/visible-flexible-closed-surface/scripts/950f-prefix-flat-accel-screen.py'
        self.bridge_path=self.source/'topics/visible-flex-larger-amplitude/computations/root_short_bridge.py'
        self.ramp=module('resonance_original_flat',self.flat_path).ramp
        self.ShortBridge=module('resonance_original_short_bridge',self.bridge_path).ShortBridge
        modes=self.port['modes']
        if modes!=[4*(j+1)for j in range(len(modes))]:raise ValueError('Actual m4 physical DN required')
        self.bridge_cache={}
        self.provenance={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in
                         (Path(__file__),self.flat_path,self.bridge_path,self.port_path)}

    def profile(self,parameters):return FlatLoop(self,parameters)

    def bridge_entry(self,curvature,peak_fraction,count,rtol):
        key=(curvature,peak_fraction,count,rtol)
        if key in self.bridge_cache:return self.bridge_cache[key]
        b=self.ShortBridge(self.port['cut'],curvature=curvature,peak_fraction=peak_fraction)
        result=backward_linear(b.profile,b.breakpoints,self.port,count,rtol)
        self.bridge_cache[key]=(b,result)
        return b,result

    def linear(self,parameters,count=2,rtol=2e-10):
        f=self.profile(parameters)
        b,entry=self.bridge_entry(f.bridge_curvature,f.peak_fraction,count,rtol)
        result=backward_linear(f.prefix_profile,f.prefix_breaks,self.port,count,rtol,
                               initial=entry['core'],logs=entry['logs'])
        result['H_per_unit_core_support']=entry['terminal'][:,1]*np.exp(-result['logs'])/result['core'][:,0]
        return result


class FlatLoop:
    def __init__(self,design,parameters):
        self.design=design;self.parameters=dict(parameters)
        p=self.parameters
        self.delta=float(p['delta']);self.vu=float(p['vu']);self.vd=float(p['vd'])
        self.eps=float(p.get('ramp',.45));self.eta=float(p.get('ramp_eta',.05))
        self.cycles=int(p.get('cycles',1));self.direction=p.get('direction','outward')
        if not(0<self.delta and 0<self.vu<1 and 0<self.vd<1 and 0<self.eps<.5 and 0<self.eta<.5 and self.cycles>=1):raise ValueError('Invalid physical profile')
        if self.direction!='outward':raise ValueError('Only the current outward family is implemented')
        bridge=p.get('prefix_bridge',{})
        self.bridge_curvature=float(bridge.get('curvature',4.));self.peak_fraction=float(bridge.get('peak_fraction',.2))
        self.bridge=design.ShortBridge(design.port['cut'],curvature=self.bridge_curvature,peak_fraction=self.peak_fraction)
        self.Tu=self.delta/(self.vu*(1-self.eps));self.Td=self.delta/(self.vd*(1-self.eps))
        self.period=self.Tu+self.Td;self.prefix_end=self.period*self.cycles;self.end=self.prefix_end+self.bridge.L
        u=np.array([0.,self.eps*self.eta,self.eps*(1-self.eta),self.eps,1-self.eps,
                    1-self.eps*(1-self.eta),1-self.eps*self.eta,1.])
        self.prefix_breaks=np.unique(np.concatenate([np.r_[j*self.period+self.Tu*u,j*self.period+self.Tu+self.Td*u]for j in range(self.cycles)]))
        self.breaks=np.unique(np.r_[self.prefix_breaks,self.prefix_end+self.bridge.breakpoints])
        self.first_positive_K=(1-self.eps)*self.Tu

    def prefix_profile(self,s):
        s=np.asarray(s);t=np.mod(s,self.period);first=t<self.Tu
        u=np.where(first,t/self.Tu,(t-self.Tu)/self.Td)
        w,I,wp=self.design.ramp(u,self.eps,self.eta)
        return (np.where(first,1+self.delta*I/(1-self.eps),1+self.delta-self.delta*I/(1-self.eps)),
                np.where(first,self.vu*w,-self.vd*w),
                np.where(first,self.vu*wp/self.Tu,-self.vd*wp/self.Td))

    def profile(self,s):
        s=np.atleast_1d(s);a,v,k=self.prefix_profile(np.minimum(s,self.prefix_end))
        mask=s>self.prefix_end
        if np.any(mask):a[mask],v[mask],k[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,k


def backward_linear(profile,breaks,port,count=2,rtol=2e-10,initial=None,logs=None):
    m=np.asarray(port['modes'][:count],float);r=port['cut']['radius'];w=port['cut']['backgroundSlope']
    D=np.asarray(port['linearSlope'][:count]);terminal=np.stack((-w*(r*D-m*m)/(m*m-1),np.ones(count)),axis=1)
    terminal/=np.linalg.norm(terminal,axis=1)[:,None]
    state=terminal.copy()if initial is None else initial.copy()
    logs=np.zeros(count)if logs is None else logs.copy()
    def rhs(s,y):
        a,v,_=profile([s]);a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
        z=y.reshape(count,2);F=z[:,0];G=z[:,1]
        return (np.stack((-(m*m-1)*v*F-m*m*b*G,
                           (m*m-1)*v*v*F/b+m*m*v*G),axis=1)/a).ravel()
    evaluations=0
    for lo,hi in reversed(list(zip(breaks[:-1],breaks[1:]))):
        if hi-lo<1e-14:continue
        sol=solve_ivp(rhs,(hi,lo),state.ravel(),rtol=rtol,atol=rtol*.01,method='DOP853',max_step=(hi-lo)/3)
        if not sol.success:raise RuntimeError(sol.message)
        evaluations+=sol.nfev;state=sol.y[:,-1].reshape(count,2)
        scale=np.linalg.norm(state,axis=1);state/=scale[:,None];logs+=np.log(scale)
    return dict(core=state,logs=logs,terminal=terminal,evaluations=evaluations)


def geometry(f,circle_radius=.1,halfwidth=.145,cylinder_length=.51,nominal_tail_rise=.02):
    s=np.unique(np.r_[np.linspace(0,f.end,6001),f.breaks]);a,v,k=f.profile(s);root=1-v*v
    if min(root)<=0:raise ValueError('Profile leaves positive meridian chart')
    b=np.sqrt(root);g,gw=np.polynomial.legendre.leggauss(8)
    ss=(s[:-1]+s[1:])[:,None]/2+(s[1:]-s[:-1])[:,None]/2*g
    vv=f.profile(ss.ravel())[1].reshape(-1,len(g))
    dz=(s[1:]-s[:-1])/2*(np.sqrt(1-vv*vv)@gw);z=np.r_[0,np.cumsum(dz)]
    ball=np.hypot(a,z+cylinder_length/2)
    tail=np.hypot(f.design.port['cut']['radius'],z[-1]+cylinder_length/2+nominal_tail_rise)
    def integrand(t):
        aa,vv,kk=[float(x[0])for x in f.profile([t])]
        return math.sqrt(max(kk,0)/(aa*(1-circle_radius**2*vv**2)))
    bounds=np.r_[f.breaks[f.breaks<f.first_positive_K],f.first_positive_K]
    chi=error=0.
    for lo,hi in zip(bounds[:-1],bounds[1:]):
        q,e=quad(integrand,lo,hi,epsabs=2e-12,epsrel=2e-12,limit=100);chi+=q;error+=e
    A0=self_acceleration=f.vu/(f.eps*f.Tu*(1-f.eta))
    aramp=1+f.delta*f.eps/(2*(1-f.eps))
    # asin(R v)/R >= v, so this is an elementary conservative lower bound.
    lower=f.vu/math.sqrt(aramp*A0)
    return dict(background_height=float(z[-1]),sample_ball_radius_with_cylinder=float(ball.max()),
        sample_ball_D_with_nominal_tail=float(2*max(ball.max(),tail)),nominal_tail_rise=nominal_tail_rise,
        background_curvature_sample=float(np.max(np.maximum(abs(k)/b,b/a))),
        elementary_background_curvature_upper=max(f.vu**2*(1-f.eps)/(f.eps*f.delta*(1-f.eta)*math.sqrt(1-f.vu**2)),
            f.vd**2*(1-f.eps)/(f.eps*f.delta*(1-f.eta)*math.sqrt(1-f.vd**2)),
            f.bridge_curvature,abs(f.bridge.ps),1/f.design.port['cut']['radius']),
        minimum_root=float(root.min()),radius_max=float(a.max()),length=f.end,
        first_positive_K=f.first_positive_K,circle_loss_div_R=chi,circle_loss_quad_error=error,
        circle_loss_div_R_elementary_lower=lower,required_halfwidth=halfwidth,
        characteristic_window_consumed_sample=chi>halfwidth,
        characteristic_window_consumed_elementary=lower>halfwidth,
        scope='Round-background diagnostics only; positive tests do not certify finite-amplitude diameter, curvature, support or a closed surface.')
