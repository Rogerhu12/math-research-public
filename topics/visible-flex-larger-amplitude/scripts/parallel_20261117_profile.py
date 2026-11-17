#!/usr/bin/env python3
"""Exact-rational-jet scalar prefix plus a C2 analytic turn extension."""
from fractions import Fraction
import numpy as np


class Profile:
    def __init__(self, geometry, start, angular_curvature=None):
        self.geometry = geometry
        self.law = geometry['initial_law']
        self.knots = geometry['knots']
        self.x = np.array([k['s'] for k in self.knots])
        self.coeff = []
        jets = [tuple(Fraction(float(k[v])) for v in ('a','ap','app')) for k in self.knots]
        L, v, k = (Fraction(float(self.law[a])) for a in ('length','velocity','k0'))
        s = Fraction(float(self.x[0])); u=s/L; b=k*L; c=3*v-2*b; d=b-2*v
        jets[0] = (1+L*(b*u*u/2+c*u**3/3+d*u**4/4), b*u+c*u*u+d*u**3, (b+2*c*u+3*d*u*u)/L)
        for i in range(len(self.x)-1):
            h=Fraction(float(self.x[i+1]))-Fraction(float(self.x[i]))
            left,right=jets[i],jets[i+1]
            c0,c1,c2=left[0],h*left[1],h*h*left[2]/2
            aa=right[0]-c0-c1-c2;bb=h*right[1]-c1-2*c2;cc=h*h*right[2]-2*c2
            self.coeff.append(np.array([float(q) for q in (c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2)]))
        self.start=start
        self.a0,self.v0,self.u0=self.old(start)
        self.angle0=np.arcsin(self.v0)
        self.K=-self.u0/np.sqrt(1-self.v0**2) if angular_curvature is None else angular_curvature
        if angular_curvature is not None and abs(self.u0+self.K*np.cos(self.angle0))>1e-10:
            raise ValueError('Requested extension must preserve the actual initial acceleration')

    def old(self,s):
        if s<=self.x[0]:
            L,v,k=(self.law[a] for a in ('length','velocity','k0'))
            if s>=L:
                return 1+L*v/2+k*L*L/12+v*(s-L),v,0.
            u=s/L;b=k*L;c=3*v-2*b;d=b-2*v
            return 1+L*(b*u*u/2+c*u**3/3+d*u**4/4),b*u+c*u*u+d*u**3,(b+2*c*u+3*d*u*u)/L
        i=min(len(self.x)-2,np.searchsorted(self.x,s,side='right')-1)
        h=self.x[i+1]-self.x[i];u=(s-self.x[i])/h;c=self.coeff[i]
        return (float(np.polynomial.polynomial.polyval(u,c)),
                float(np.polynomial.polynomial.polyval(u,np.arange(1,6)*c[1:])/h),
                float(np.polynomial.polynomial.polyval(u,np.arange(2,6)*np.arange(1,5)*c[2:])/(h*h)))

    def __call__(self,s):
        if s<=self.start:return self.old(s)
        angle=self.angle0-self.K*(s-self.start)
        return self.a0+(np.cos(angle)-np.cos(self.angle0))/self.K,np.sin(angle),-self.K*np.cos(angle)

