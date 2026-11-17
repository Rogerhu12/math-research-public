#!/usr/bin/env python3
"""Explicit finite m3 perturbation, exact C2 collar, and planar disk.

The finite binary Fourier/radial data define the functions with exact real
arithmetic. Floating methods evaluate those definitions approximately. The
unchanged rotational background is supplied as h(r),w(r),w_r(r), with h(a)=0;
it is not replaced by an interpolant of saved height samples.

An upper piece has X=(r*e_theta+V_xy, Zcap-h-V_z). It has one outer boundary;
a full closed sphere also needs a common-two-jet prefix and its lower mirror.
"""
from pathlib import Path
import importlib.util
import json
import numpy as np


class FiniteClosedTail:
    def __init__(self, manifest, reader_source):
        spec = importlib.util.spec_from_file_location('closure_integrated_tail', reader_source)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.finite = module.IntegratedTail(manifest)
        self.meta = self.finite.meta
        if self.meta['parameters']['spacing'] != 3:
            raise ValueError('This frozen exporter uses m3 symmetry')
        self.a = np.longdouble(self.meta['parameters']['rCuff'])
        self.b = np.longdouble(self.meta['radialGeometry']['innerAnchor'])
        self.c = np.longdouble(self.meta['radialGeometry']['outerAnchor'])
        self.L = self.b-self.a
        if not 0 < self.L <= self.a:
            raise ValueError('Positive collar of width at most its radius required')
        self.A = [self.finite.value_nodes[0], self.finite.first[0], self.finite.second[0]]

    def coefficients(self, radius):
        r = np.asarray(radius, dtype=np.longdouble)
        if np.any(r < 0) or np.any(r > self.c):
            raise ValueError('Outside the capped tail')
        shape = r.shape
        rr = r.reshape(-1)
        out = [np.zeros((rr.size, self.finite.C), dtype=np.longdouble) for _ in range(3)]
        collar = (rr >= self.a) & (rr < self.b)
        outer = rr >= self.b
        if np.any(outer):
            values = self.finite.coefficients(rr[outer])
            for j in range(3): out[j][outer] = values[j]
        if np.any(collar):
            t = ((rr[collar]-self.a)/self.L)[:,None]
            p0 = t**3*(10+t*(-15+6*t))
            p1 = t**3*(-4+t*(7-3*t))
            p2 = t**3*(np.longdouble('.5')+t*(-1+np.longdouble('.5')*t))
            d0 = 30*t*t*(1-t)*(1-t)
            d1 = t*t*(-12+t*(28-15*t))
            d2 = t*t*(np.longdouble('1.5')+t*(-4+np.longdouble('2.5')*t))
            e0 = 60*t*(1+t*(-3+2*t))
            e1 = t*(-24+t*(84-60*t))
            e2 = t*(3+t*(-12+10*t))
            A0,A1,A2 = self.A
            out[0][collar] = p0*A0+self.L*p1*A1+self.L*self.L*p2*A2
            out[1][collar] = d0/self.L*A0+d1*A1+self.L*d2*A2
            out[2][collar] = e0/(self.L*self.L)*A0+e1/self.L*A1+e2*A2
        return tuple(v.reshape(shape+(self.finite.C,)) for v in out)

    def perturbation_jets(self, radius, theta):
        r,t = np.broadcast_arrays(np.asarray(radius,dtype=np.longdouble),
                                   np.asarray(theta,dtype=np.longdouble))
        value,first,second = self.coefficients(r)
        mp,mh,P = self.finite.planar_modes,self.finite.height_modes,self.finite.P
        ep = np.exp(1j*t[...,None]*mp)
        ch,sh = np.cos(t[...,None]*mh),np.sin(t[...,None]*mh)
        def apply(c,order):
            xy = np.sum(c[...,:P]*(1j*mp)**order*ep,axis=-1)
            if order == 0: z = np.sum(c[...,P:]*ch,axis=-1)
            elif order == 1: z = -np.sum(c[...,P:]*mh*sh,axis=-1)
            else: z = -np.sum(c[...,P:]*mh*mh*ch,axis=-1)
            return np.stack([xy.real,xy.imag,z],axis=-1)
        return (apply(value,0),apply(first,0),apply(value,1),
                apply(second,0),apply(first,1),apply(value,2))

    def upper_jets(self, radius, theta, background_height, w, wr, cap_height):
        """Return X,Xr,Xtheta,Xrr,Xrtheta,Xthetatheta in the upper gauge.

        background_height is the same fixed integral int_a^r w, not an
        independently fitted function. Use zero h,w,wr inside the disk.
        """
        r,t,h,w,wr = np.broadcast_arrays(*[np.asarray(x,dtype=np.longdouble)
            for x in [radius,theta,background_height,w,wr]])
        if np.any((r < self.a)&((h != 0)|(w != 0)|(wr != 0))):
            raise ValueError('The disk background is exactly flat')
        V = self.perturbation_jets(r,t)
        co,si,zero = np.cos(t),np.sin(t),np.zeros_like(t)
        bg = [np.stack([r*co,r*si,cap_height-h],axis=-1),
              np.stack([co,si,-w],axis=-1),
              np.stack([-r*si,r*co,zero],axis=-1),
              np.stack([zero,zero,-wr],axis=-1),
              np.stack([-si,co,zero],axis=-1),
              np.stack([-r*co,-r*si,zero],axis=-1)]
        sign = np.array([1,1,-1],dtype=np.longdouble)
        return tuple(b+v*sign for b,v in zip(bg,V))

    def upper_disk_xy(self, x, y, cap_height):
        """Regular Cartesian pole chart, including the axis itself."""
        x,y = np.broadcast_arrays(np.asarray(x,dtype=np.longdouble),np.asarray(y,dtype=np.longdouble))
        if np.any(x*x+y*y > self.a*self.a): raise ValueError('Outside disk')
        z = np.full_like(x,cap_height)
        X = np.stack([x,y,z],axis=-1)
        J = np.broadcast_to(np.array([[1,0],[0,1],[0,0]],dtype=np.longdouble),x.shape+(3,2))
        Hess = np.zeros(x.shape+(3,2,2),dtype=np.longdouble)
        return X,J,Hess
