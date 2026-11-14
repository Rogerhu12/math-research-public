"""Independent planar-core Frenet flow with any integer rotational symmetry.

This class initializes the general cylindrical basis directly. It does not
alter or bypass the reflected nonplanar-core constructors' m=2 mod4 guard;
those constructors and their initial-data formulas are never invoked.
"""
import math
import types
from types import SimpleNamespace
import numpy as np
from curve_stable_prefix_bvp import CylindricalPrefix
from curve_linear_control import ramp
from f6curve_local_frame import install_local_frame,local_fun,local_fun_jac,local_c2_interpolant
from f6curve_bidirectional_bridge import DirectionalBridge
from f6curve_outward_bridge_linear import BackwardLine

def extended_fun(self,s,y,p):
    dtype=np.clongdouble if np.iscomplexobj(y) else np.longdouble
    return np.asarray(local_fun(self,s,np.asarray(y,dtype=dtype),p),dtype=y.dtype)

def extended_fun_jac(self,s,y,p):
    return local_fun_jac(self,s,np.asarray(y,dtype=np.longdouble),p)

def extended_c2_interpolant(self,sol):
    work=SimpleNamespace(x=sol.x,y=np.asarray(sol.y,dtype=np.longdouble),p=sol.p)
    return local_c2_interpolant(self,work)

class PlanarSymmetryFlow(CylindricalPrefix):
    def __init__(self,cfg,port,modes=4,gauge_amplitude=.001,angular=128,base_mode=3,bridge=None):
        self.M=int(modes);self.q=float(gauge_amplitude);self.base_mode=int(base_mode)
        if self.M<1 or self.base_mode<2 or self.q<=0:raise ValueError('Invalid mode or gauge amplitude')
        self.cfg=dict(cfg);self.delta=float(cfg['delta']);self.vu=float(cfg['vu']);self.vd=float(cfg['vd'])
        self.eps=float(cfg['ramp']);self.cycles=int(cfg['cycles']);self.direction=cfg.get('direction','outward')
        if not (0<self.delta and 0<self.vu<1 and 0<self.vd<1 and 0<self.eps<.5 and self.cycles>=1):
            raise ValueError('Profile lies outside the positive meridian design domain')
        if self.direction not in ('outward','inward'):raise ValueError('Unknown cycle direction')
        if self.direction=='inward' and self.delta>=1:raise ValueError('Inward excursion must stay below one')
        self.Tu=self.delta/(self.vu*(1-self.eps));self.Td=self.delta/(self.vd*(1-self.eps))
        self.period=self.Tu+self.Td;self.prefix_end=self.period*self.cycles
        first,second=(self.Tu,self.Td) if self.direction=='outward' else (self.Td,self.Tu)
        self.breakpoints=np.unique(np.concatenate([j*self.period+np.array([0,self.eps*first,(1-self.eps)*first,first,first+self.eps*second,first+(1-self.eps)*second,first+second]) for j in range(self.cycles)]))
        self.bridge=DirectionalBridge(port['cut']) if bridge is None else bridge
        self.end=self.prefix_end+self.bridge.L
        self.breaks=np.unique(np.r_[self.breakpoints,self.end])
        self.nt=max(int(angular),8*(self.base_mode*self.M+1))
        self.even=self.base_mode*np.arange(1,self.M+1)
        self.n=3*self.M+1;self.ix=0;self.iy=self.M+1;self.ir=1;self.it=self.M+1;self.iz=2*self.M+1
        self.B,self.B1,self.B2=self.basis(self.nt)
        self.calls=0;self.port_data=port
        install_local_frame(self)
        self.fun=types.MethodType(extended_fun,self);self.fun_jac=types.MethodType(extended_fun_jac,self)
        self.c2_interpolant=types.MethodType(extended_c2_interpolant,self)
        self.arithmetic='long-double-local-frame'

    def prefix_profile(self,s):
        s=np.asarray(s);t=np.mod(s,self.period)
        outward=self.direction=='outward';first=self.Tu if outward else self.Td;second=self.Td if outward else self.Tu
        on_first=t<first;u=np.where(on_first,t/first,(t-first)/second);w,I=ramp(u,self.eps)
        wp=np.where(u<self.eps,np.pi/(2*self.eps)*np.sin(np.pi*u/self.eps),np.where(u>1-self.eps,-np.pi/(2*self.eps)*np.sin(np.pi*(1-u)/self.eps),0.))
        sign=1 if outward else -1;vfirst=self.vu if outward else self.vd;vsecond=self.vd if outward else self.vu
        a=np.where(on_first,1+sign*self.delta*I/(1-self.eps),1+sign*self.delta-sign*self.delta*I/(1-self.eps))
        ap=np.where(on_first,sign*vfirst*w,-sign*vsecond*w)
        app=np.where(on_first,sign*vfirst*wp/first,-sign*vsecond*wp/second)
        return a,ap,app

    def profile(self,s):
        s=np.atleast_1d(s);a,v,acc=self.prefix_profile(np.minimum(s,self.prefix_end))
        mask=s>self.prefix_end
        if np.any(mask):a[mask],v[mask],acc[mask]=self.bridge.profile(s[mask]-self.prefix_end)
        return a,v,acc

    def linear_rhs(self,s,y,m=None):
        m=self.base_mode if m is None else int(m)
        a,v,_=self.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
        return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],(m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a

    def linear_terminal(self,mode_index=0):
        m=int(self.even[mode_index]);r=self.port_data['cut']['radius'];w=self.port_data['cut']['backgroundSlope'];D=self.port_data['linearSlope'][mode_index]
        return np.array([self.bridge.sigma*w*(r*D-m*m)/(m*m-1),1.])

    def backward_line(self,mode_index=0):
        m=int(self.even[mode_index])
        return BackwardLine(lambda s,y:self.linear_rhs(s,y,m),self.breaks,self.linear_terminal(mode_index))
