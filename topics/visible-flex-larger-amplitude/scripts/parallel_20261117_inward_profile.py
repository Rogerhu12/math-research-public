#!/usr/bin/env python3
"""Explicit C2 inward scalar extension of an accepted Frenet prefix.

The mathematical definition uses the displayed curvature and exact position
integrals. Gauss quadrature evaluates the two short transition integrals; it
does not redefine those integrals or certify an actual nonaxisymmetric field.
The final inward planar two-jet permits a disk in the reference geometry.
"""
import numpy as np
from parallel_20261117_profile import Profile


def smoothstep(u):
    return u**3*(10+u*(-15+6*u))


def primitive(u):
    return u**4*(2.5+u*(-3+u))


class InwardProfile:
    def __init__(self, geometry, origin, cut, curvature=1.5,
                 ramp_in=.02, ramp_out=.02, quadrature=32):
        self.base=Profile(geometry,origin)
        self.cut=float(cut);self.curvature=float(curvature)
        self.ramp_in=float(ramp_in);self.ramp_out=float(ramp_out)
        self.quadrature=int(quadrature)
        if min(self.curvature,self.ramp_in,self.ramp_out)<=0:
            raise ValueError('Positive curvature and ramp lengths required')
        self.ac,self.vc,self.uc=self.base(self.cut)
        if not -1<self.vc<1:
            raise ValueError('Cut must precede a radial coordinate pole')
        self.alpha0=float(np.arcsin(self.vc))
        self.kappa0=float(-self.uc/np.cos(self.alpha0))
        if self.kappa0<=0:raise ValueError('Positive initial meridian curvature required')
        self.alpha1=self.alpha0-self.ramp_in*(self.kappa0+self.curvature)/2
        self.plateau=(self.alpha1+np.pi/2-self.curvature*self.ramp_out/2)/self.curvature
        if self.plateau<=0:raise ValueError('Transition ramps exceed the required turn')
        self.alpha2=self.alpha1-self.curvature*self.plateau
        self.end=self.cut+self.ramp_in+self.plateau+self.ramp_out
        self.nodes,self.weights=np.polynomial.legendre.leggauss(self.quadrature)
        self.shift1=self.transition_integral(self.ramp_in,False)
        self.shift2=self.shift1+np.array([
            (np.cos(self.alpha2)-np.cos(self.alpha1))/self.curvature,
            (np.sin(self.alpha1)-np.sin(self.alpha2))/self.curvature])
        self.shift3=self.shift2+self.transition_integral(self.ramp_out,True)
        self.radius=self.ac+self.shift3[0]
        if self.radius<=0:raise ValueError('Reference turns through the rotation axis')
        # These are compatibility fields used by the unchanged finite solver;
        # the complete new definition is always stored separately in spec().
        self.start=self.base.start;self.a0=self.base.a0
        self.v0=self.base.v0;self.u0=self.base.u0;self.K=self.base.K

    def transition_angle(self,t,final):
        if final:
            u=t/self.ramp_out
            return self.alpha2-self.curvature*self.ramp_out*(u-primitive(u))
        u=t/self.ramp_in
        return self.alpha0-self.kappa0*t-(self.curvature-self.kappa0)*self.ramp_in*primitive(u)

    def transition_integral(self,t,final):
        at=self.transition_angle(t*(self.nodes+1)/2,final)
        return t/2*np.array([self.weights@np.sin(at),self.weights@np.cos(at)])

    def meridian(self,s):
        t=float(s)-self.cut
        if t<0 or s>self.end+1e-12:raise ValueError('Outside the new inward interval')
        if t<=self.ramp_in:
            alpha=self.transition_angle(t,False)
            kappa=self.kappa0+(self.curvature-self.kappa0)*smoothstep(t/self.ramp_in)
            shift=self.transition_integral(t,False)
        elif t<=self.ramp_in+self.plateau:
            u=t-self.ramp_in;alpha=self.alpha1-self.curvature*u
            kappa=self.curvature
            shift=self.shift1+np.array([(np.cos(alpha)-np.cos(self.alpha1))/kappa,
                                      (np.sin(self.alpha1)-np.sin(alpha))/kappa])
        else:
            u=min(self.ramp_out,t-self.ramp_in-self.plateau)
            alpha=self.transition_angle(u,True)
            kappa=self.curvature*(1-smoothstep(u/self.ramp_out))
            shift=self.shift2+self.transition_integral(u,True)
        ap,hs=np.sin(alpha),np.cos(alpha)
        if s==self.end:
            ap,hs,kappa=-1.,0.,0.
            shift=self.shift3
        return dict(a=self.ac+shift[0],ap=ap,app=-kappa*hs,
                    height_increment=shift[1],height_s=hs,height_ss=kappa*ap,
                    curvature=kappa,angle=alpha)

    def __call__(self,s):
        if s<=self.cut:return self.base(s)
        if s>self.end:
            a=self.radius-(s-self.end)
            if a<=0:raise ValueError('Use a Cartesian chart at the disk center')
            return a,-1.,0.
        z=self.meridian(s)
        return float(z['a']),float(z['ap']),float(z['app'])

    def spec(self):
        return dict(cut=self.cut,curvature=self.curvature,ramp_in=self.ramp_in,
                    ramp_out=self.ramp_out,quadrature=self.quadrature,
                    exact_definition='curvature ramps and exact meridian integrals',
                    end=self.end,planar_radius=float(self.radius),
                    reference_height_increment=float(self.shift3[1]))
