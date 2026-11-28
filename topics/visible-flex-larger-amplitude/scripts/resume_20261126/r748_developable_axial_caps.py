#!/usr/bin/env python3
"""R748 exact developable end caps, direct physical two-jets on the R747 material atlas."""
import numpy as np
from functools import lru_cache
import r747_offset_arclength_closed_two_jets as ar
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

X0=.595
AMPLITUDE=1/4096

@lru_cache(maxsize=None)
def rule(order):
    return np.polynomial.legendre.leggauss(order)

def development(x,phase,bend,order=24):
    # Curve derivative (cos(beta), -sin(beta)) has exactly unit length.
    t=np.maximum(X0-x.v,0.);a=bend*np.sin(phase)
    z,w=rule(order);p=t[:,None]*(z+1.)/2.
    angles=a[:,None]*p*p
    dx=(np.sin(angles/2)**2 @ w)*t
    lift=(np.sin(angles)@w)*t/2
    beta=a*t*t
    dxj=unary(x,dx,-2*np.sin(beta/2)**2,2*a*t*np.sin(beta))
    hj=unary(x,lift,-np.sin(beta),2*a*t*np.cos(beta))
    return dxj,hj

def chart_jet(chart,u,v,phase=0.,order=32,method="legacy",bend=AMPLITUDE,
              fade_start=.71,fade_stop=1.09,rotate=True):
    ar.old.disk._public()
    a,b,t=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    sh=a.shape;t=t.ravel()
    if np.any((t<0)|(t>np.pi/2+2e-14)) or method not in ("legacy","arc"):
        raise ValueError("outside R748 method or physical phase range")
    if not 0<fade_start<fade_stop or bend<0:raise ValueError("invalid end development")
    x,y,z=ar.sphere_chart(chart,J(a.ravel(),s=1.),J(b.ravel(),a=1.),t,ar.axial.ZERO_ENDS,order,method=="legacy")
    sg=np.where(y.v>=0,1.,-1.)
    blend=cap_s7((y*sg-fade_start)/(fade_stop-fade_start))
    dx,h=development(x,t,bend,24)
    x=x+blend*dx;y=y+sg*blend*h
    if rotate:
        ox,oz=ar.axial.axis(order);co,si=np.cos(t),np.sin(t)
        xx,zz=x-ox,z-oz;x,z=ox+co*xx-si*zz,oz+si*xx+co*zz
    return gather((x,y,z),len(t)).reshape(sh+(6,3))
