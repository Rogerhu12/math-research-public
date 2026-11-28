#!/usr/bin/env python3
"""Physical-azimuth interval test shared by accurate upper-disk pieces."""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def outward(x,direction):
    if direction<0:return float(np.nextafter(float(np.min(x)),-np.inf))
    return float(np.nextafter(float(np.max(x)),np.inf))


def iabs(I,x):
    return I(x.abs_upper())


class SectorCheck:
    def __init__(self,K,candidate,central_a):
        self.K=K;self.I=K.I;self.central_a=central_a
        self.parameters=np.asarray(candidate['coefficients'])
        self.monomials=candidate['monomials']
        self.n=len(self.parameters)
        if candidate['degree']!=3:raise ValueError('Expected cubic potentials')
        self.sn,self.cs=K.sincos(K.PI*K.I(2*np.arange(self.n))/self.n)
        self.rows=0;self.worst={}
        self.limits=dict(positiveRayNumerator=np.inf,angularJacobian=np.inf,minimumHeight=np.inf,
                         minimumHeldDistanceSquared=np.inf,maximumRadiusSquared=-np.inf,
                         maximumAbsoluteY=-np.inf)
        self.sectors=np.full(self.n,np.inf)

    def lower(self,name,q,tag):
        v=outward(q.lo,-1)
        if v<self.limits[name]:self.limits[name]=v;self.worst[name]=tag

    def upper(self,name,q,tag):
        v=outward(q.hi,1)
        if v>self.limits[name]:self.limits[name]=v;self.worst[name]=tag

    def cartesian(self,p,v,u,tag):
        x,y,z=p;vx,vy,vz=v;ux,uy,uz=u
        q=x.square()+y.square();J=x*uy-y*ux;K=x*vy-y*vx;D=vx*uy-vy*ux
        self.test(x,y,q,z,J,3*q*D,4*(vz*J-uz*K),tag,x,y)

    def test(self,xangle,yangle,q,z,J,xd,yd,tag,xphys,yphys):
        I=self.I;sec=self.n;sn,cs=self.sn,self.cs
        X=(q-F(7,8))*F(3,2);Y=4*(z-F(3,8))
        self.lower('angularJacobian',J,tag)
        self.lower('minimumHeight',z,tag)
        self.lower('minimumHeldDistanceSquared',xphys.square()+(iabs_box(I,yphys)-self.central_a).square()+z.square(),tag)
        self.upper('maximumRadiusSquared',q+z.square(),tag)
        self.upper('maximumAbsoluteY',iabs(I,yphys),tag)
        ref=np.floor(np.mod(np.arctan2((yangle.lo+yangle.hi)/2,(xangle.lo+xangle.hi)/2),2*np.pi)*sec/(2*np.pi)).astype(int)%sec
        loidx=(ref-1)%sec;hiidx=(ref+2)%sec
        if np.any((cs[loidx]*yangle-sn[loidx]*xangle).lo<0) or np.any((xangle*sn[hiidx]-yangle*cs[hiidx]).lo<0):
            raise ArithmeticError('Three-sector cover too coarse '+str(tag))
        possible=np.zeros(ref.shape,dtype=int)
        for key in (-1,0,1):
            s=(ref+key)%sec;e=(s+1)%sec
            ok=((cs[s]*yangle-sn[s]*xangle).hi>=0)&((xangle*sn[e]-yangle*cs[e]).hi>=0)
            if not np.any(ok):continue
            possible+=ok
            co={(i,j):I(self.parameters[s[ok],v]) for v,(i,j) in enumerate(self.monomials)}
            x=X[ok];y=Y[ok]
            x0=I((x.lo+x.hi)/2);y0=I((y.lo+y.hi)/2);ex=x-x0;ey=y-y0
            c=lambda i,j:co[i,j]
            gx=c(1,0)+2*c(2,0)*x0+c(1,1)*y0+3*c(3,0)*x0.square()+2*c(2,1)*x0*y0+c(1,2)*y0.square()
            gy=c(0,1)+c(1,1)*x0+2*c(0,2)*y0+c(2,1)*x0.square()+2*c(1,2)*x0*y0+3*c(0,3)*y0.square()
            gxx=2*c(2,0)+6*c(3,0)*x0+2*c(2,1)*y0
            gxy=c(1,1)+2*c(2,1)*x0+2*c(1,2)*y0
            gyy=2*c(0,2)+2*c(1,2)*x0+6*c(0,3)*y0
            gx+=gxx*ex+gxy*ey+3*c(3,0)*ex.square()+2*c(2,1)*ex*ey+c(1,2)*ey.square()
            gy+=gxy*ex+gyy*ey+c(2,1)*ex.square()+2*c(1,2)*ex*ey+3*c(0,3)*ey.square()
            val=gx*xd[ok]+gy*yd[ok]
            self.lower('positiveRayNumerator',val,tag)
            np.minimum.at(self.sectors,s[ok],np.nextafter(val.lo.astype(float),-np.inf))
        if np.any(possible==0):raise ArithmeticError('Uncovered physical angle')
        self.rows+=ref.size

    def json(self):
        return dict(closedBoxes=self.rows,bounds=self.limits,worst=self.worst,sectorLower=self.sectors.tolist())


def iabs_box(I,z):
    return I(np.maximum(np.longdouble(0),np.maximum(z.lo,-z.hi)),z.abs_upper())
