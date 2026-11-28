#!/usr/bin/env python3
"""R740 closed rolled shoulder and genuinely bent Euclidean disk, horizontal mirror.

Import field(material,theta,phase,side,order,markers) on the public project runner.
The integral formulas in R740 are the exact reference. order controls only their
evaluation. Disk material is 0..1; shoulder material is 1..1+SHOULDER_LENGTH.
"""
from functools import lru_cache
import argparse
import json
import os
from pathlib import Path

import numpy as np


H, HOLD, BEND, EDGE = .17, .30, .26, .125
TURN, BLEND, ETA, COLLAR = .09, .001, .01, .01
A_LENGTH = TURN*np.pi/2+BLEND
SHOULDER_LENGTH = A_LENGTH+ETA+2*COLLAR
MARKERS = ((-.10,-.08,.010),(.06,-.08,.012),(0.,.09,.014))


def _public():
    if os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public" or os.environ.get("GITHUB_ACTIONS")!="true":
        raise RuntimeError("Evaluate the reference on the public project Actions runner")


def s5(v):
    return v**3*(10+v*(-15+6*v))


def i5(v):
    return v**4*(2.5+v*(-3+v))


def s7(v):
    return v**4*(35+v*(-84+v*(70-20*v)))


def softened_angle(x, width, ramp, gain):
    z=np.clip(x,0,width)
    end=width-ramp
    return gain*np.where(z<ramp,ramp*i5(z/ramp),
        np.where(z<=end,z-ramp/2,width-ramp-ramp*i5((width-z)/ramp)))


def beta(x):
    return softened_angle(np.asarray(x)-HOLD,BEND,EDGE*BEND,np.pi/(2*BEND*(1-EDGE)))


def curvature(x):
    v=(np.asarray(x)-HOLD)/BEND
    t=np.minimum(np.minimum(v,1-v)/EDGE,1)
    return (np.pi/(2*BEND*(1-EDGE)))*s5(np.clip(t,0,1))


@lru_cache(maxsize=None)
def rule(n):
    x,w=np.polynomial.legendre.leggauss(n)
    return (x+1)/2,w/2


def integrals(x, cuts, angle, order):
    x=np.asarray(x)
    nodes,weights=rule(order)
    cs=np.zeros_like(x,dtype=float)
    sn=np.zeros_like(x,dtype=float)
    for lo,hi in zip(cuts,cuts[1:]):
        d=np.clip(x-lo,0,hi-lo)
        a=angle(lo+d[...,None]*nodes)
        cs+=d*(np.cos(a)@weights)
        sn+=d*(np.sin(a)@weights)
    return cs,sn


def bent_curve(x, order):
    x=np.asarray(x)
    a=HOLD; b=BEND; e=EDGE*b
    c,s=integrals(x,(a,a+e,a+b-e,a+b),beta,order)
    return np.minimum(x,a)+c,s+np.maximum(0,x-a-b)


def angle_a(s):
    return softened_angle(s,A_LENGTH,BLEND,1/TURN)


def rolled_radii(s,order):
    u,v=integrals(np.asarray(s),(0,BLEND,A_LENGTH-BLEND,A_LENGTH),angle_a,order)
    return 1+u,v


def disk_xy(x,y,order=32,markers=True):
    _public()
    x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
    u,v=bent_curve(x,order)
    z=H+v+(bumps(x,y) if markers else 0)
    return np.stack((u,y,z),axis=-1)


def bumps(x,y):
    z=np.zeros_like(x,dtype=float)
    for cx,cy,radius in MARKERS:
        q=np.maximum(0,1-((x-cx)**2+(y-cy)**2)/radius**2)
        z+=1e-4*radius**2*q**3
    return z


def rim_jets(theta,order=32):
    _public()
    th=np.asarray(theta,dtype=float); x=np.cos(th); y=np.sin(th)
    pt=disk_xy(x,y,order,False)
    b=beta(x)
    radial=np.stack((x*np.cos(b),y,x*np.sin(b)),axis=-1)
    weight=x*x*curvature(x)
    rr=np.stack((-weight*np.sin(b),0*x,weight*np.cos(b)),axis=-1)
    return pt,radial,rr


def a_surface(s,theta,order):
    R,t=rolled_radii(s,order)
    x=R*np.cos(theta); y=R*np.sin(theta); b=beta(x)
    u,v=bent_curve(x,order)
    return np.stack((u+t*np.sin(b),y,H+v-t*np.cos(b)),axis=-1)


def b_surface(s,theta,order):
    s,theta=np.broadcast_arrays(s,theta)
    rb,tb=rolled_radii(A_LENGTH,order)
    x=rb*np.cos(theta);y=rb*np.sin(theta);b=beta(x)
    u,v=bent_curve(x,order)
    nodes,weights=rule(order)
    af=b[...,None]*(1-s7(s[...,None]*nodes/ETA))
    f=1-s7(s/ETA)
    X=u+tb*np.sin(b)+TURN*(np.cos(b*f)-np.cos(b))+s*(np.sin(af)@weights)
    Z=H+v-tb*np.cos(b)-TURN*(np.sin(b)-np.sin(b*f))-s*(np.cos(af)@weights)
    return np.stack((X,y,Z),axis=-1)


def projected_ring_speed(theta,order):
    rb,tb=rolled_radii(A_LENGTH,order)
    x=rb*np.cos(theta); b=beta(x); k=curvature(x)
    nodes,weights=rule(order); f=1-s7(nodes)
    dX=np.cos(b)+k*(tb*np.cos(b)+TURN*np.sin(b)+ETA*((f*np.cos(b[...,None]*f))@weights))
    return rb*np.hypot(np.sin(theta)*dX,np.cos(theta))


@lru_cache(maxsize=None)
def angular_breaks(order):
    rb=float(rolled_radii(A_LENGTH,order)[0])
    thresholds=(HOLD,HOLD+BEND*EDGE,HOLD+BEND*(1-EDGE),HOLD+BEND)
    half=sorted([0.,np.pi]+[float(np.arccos(x/rb)) for x in thresholds])
    return tuple(half+[2*np.pi-a for a in half[-2::-1]])


def arc(theta,order):
    theta=np.asarray(theta,dtype=float)
    a=np.zeros_like(theta)
    nodes,weights=rule(order)
    cuts=angular_breaks(order)
    for lo,hi in zip(cuts,cuts[1:]):
        d=np.clip(theta-lo,0,hi-lo)
        a+=d*(projected_ring_speed(lo+d[...,None]*nodes,order)@weights)
    return a


@lru_cache(maxsize=None)
def ring_period(order):
    return float(arc(2*np.pi,order))


def _ring_angle(theta,order):
    # Lift of the normalized arclength inverse. Use monotone brackets and
    # safeguarded Newton. An exact point has a zero displacement under Newton.
    theta=np.asarray(theta,dtype=float)
    offset=np.floor(theta/(2*np.pi))*2*np.pi
    th=theta-offset
    want=th*(ring_period(order)/(2*np.pi))
    lo=np.zeros_like(th);hi=np.full_like(th,2*np.pi)
    a=th.copy()
    for _ in range(48):
        res=arc(a,order)-want
        done=np.abs(res)<=8*np.finfo(float).eps*np.maximum(1,want)
        if np.all(done):
            break
        lo=np.where(res<0,a,lo);hi=np.where(res>0,a,hi)
        nxt=a-res/projected_ring_speed(a,order)
        nxt=np.where((nxt>=lo)&(nxt<=hi),nxt,(lo+hi)/2)
        a=np.where(done,a,nxt)
    return offset+a

def ring_angle(theta,order):
    values,inverse=np.unique(np.asarray(theta),return_inverse=True)
    out=np.empty_like(values)
    for at in range(0,len(values),128):
        out[at:at+128]=_ring_angle(values[at:at+128],order)
    return out[inverse].reshape(np.shape(theta))


def shoulder(s,theta,order=32):
    _public()
    ss,th=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(theta,dtype=float))
    shape=ss.shape; s=ss.ravel();th=th.ravel()
    if np.any((s<0)|(s>SHOULDER_LENGTH+2e-14)):
        raise ValueError("outside the R740 material shoulder")
    out=np.empty((len(s),3))
    mask=s<=A_LENGTH
    if np.any(mask):
        out[mask]=a_surface(s[mask],th[mask],order)
    bmask=(~mask)&(s<=A_LENGTH+ETA)
    if np.any(bmask):
        out[bmask]=b_surface(np.clip(s[bmask]-A_LENGTH,0,ETA),th[bmask],order)
    vmask=~(mask|bmask)
    if np.any(vmask):
        d=np.clip(s[vmask]-A_LENGTH-ETA,0,2*COLLAR)
        chi=s7(np.clip(d/COLLAR,0,1))
        theta0=th[vmask]
        theta1=theta0+chi*(ring_angle(theta0,order)-theta0)
        result=b_surface(ETA,theta1,order)
        z=result[:,2].copy()
        result[:,2]=np.where(d<=COLLAR,z-d-(z-2*COLLAR)*chi,2*COLLAR-d)
        out[vmask]=result
    return out.reshape(shape+(3,))




ELL_LENGTH, ELL_Z, ELL_SCALE, ELL_SHIFT = .025, .025, 1.01, .12
ELL_SHOULDER_LENGTH = A_LENGTH+ELL_LENGTH+ELL_Z


def ellipse_shoulder(s,theta,order=32):
    _public()
    ss,tt=np.broadcast_arrays(np.asarray(s,dtype=float),np.asarray(theta,dtype=float))
    shape=ss.shape;s=ss.ravel();th=tt.ravel()
    if np.any((s<0)|(s>ELL_SHOULDER_LENGTH+2e-14)):
        raise ValueError("outside the ellipse shoulder")
    out=np.empty((len(s),3))
    mask=s<=A_LENGTH
    if np.any(mask):
        out[mask]=a_surface(s[mask],th[mask],order)
    bmask=(~mask)&(s<=A_LENGTH+ELL_LENGTH)
    rb,tb=rolled_radii(A_LENGTH,order)
    if np.any(bmask):
        v=np.clip((s[bmask]-A_LENGTH)/ELL_LENGTH,0,1)
        S=s7(v)
        # D=integral(1-S7), G=D-S/2 in a nonnegative factored form.
        G=v*(1-v)**4*(1+v*(4+v*(10+2.5*v)))
        D=G+S/2
        x=rb*np.cos(th[bmask]);y=rb*np.sin(th[bmask]);b=beta(x)
        u,z=bent_curve(x,order)
        xa=u+tb*np.sin(b);za=H+z-tb*np.cos(b)
        xe=ELL_SCALE*x+ELL_SHIFT
        X=(1-S)*xa+S*xe+ELL_LENGTH*G*np.sin(b)
        Z=(1-S)*za+S*ELL_Z+ELL_LENGTH*(S/2-(v-D)-G*np.cos(b))
        out[bmask]=np.stack((X,y,Z),axis=-1)
    end=~(mask|bmask)
    if np.any(end):
        d=np.clip(s[end]-A_LENGTH-ELL_LENGTH,0,ELL_Z)
        tt=th[end]
        th1=tt+s7(np.clip(2*d/ELL_Z,0,1))*(ellipse_angle(tt,order)-tt)
        out[end]=np.stack((ELL_SHIFT+ELL_SCALE*rb*np.cos(th1),rb*np.sin(th1),ELL_Z-d),axis=-1)
    return out.reshape(shape+(3,))


def ellipse_angle(theta,order):
    values,inv=np.unique(np.asarray(theta),return_inverse=True)
    off=np.floor(values/(2*np.pi))*2*np.pi;th=values-off
    nodes,weights=rule(order)
    def speed(x):
        return np.hypot(ELL_SCALE*np.sin(x),np.cos(x))
    def length(a):
        return a*(speed(a[...,None]*nodes)@weights)
    want=th*float(length(np.asarray(2*np.pi)))/(2*np.pi)
    a=th.copy()
    for _ in range(8):
        a=np.clip(a-(length(a)-want)/speed(a),0,2*np.pi)
    return (a+off)[inv].reshape(np.shape(theta))


def field(material,theta,phase=0.,side=1,order=32,markers=True,design="rolled"):
    """Set design='ellipse' for the replacement with a controlled equatorial radius."""
    _public()
    m,th,phase,side=np.broadcast_arrays(np.asarray(material,dtype=float),
        np.asarray(theta,dtype=float),np.asarray(phase,dtype=float),np.asarray(side))
    shape=m.shape;m=m.ravel();th=th.ravel();phase=phase.ravel();side=side.ravel()
    if design not in ("rolled","ellipse"):
        raise ValueError("choose rolled or ellipse")
    length=ELL_SHOULDER_LENGTH if design=="ellipse" else SHOULDER_LENGTH
    if np.any((m<0)|(m>1+length+2e-14)) or np.any((side!=1)&(side!=-1)):
        raise ValueError("invalid material or side")
    a=th-phase
    p=np.empty((len(m),3))
    disk=m<=1
    if np.any(disk):
        p[disk]=disk_xy(m[disk]*np.cos(a[disk]),m[disk]*np.sin(a[disk]),order,False)
    if np.any(~disk):
        evaluate=ellipse_shoulder if design=="ellipse" else shoulder
        p[~disk]=evaluate(m[~disk]-1,a[~disk],order)
    cs=np.cos(phase);sn=np.sin(phase);x=p[:,0].copy();y=p[:,1].copy()
    p[:,0]=cs*x-sn*y;p[:,1]=sn*x+cs*y;p[:,2]*=side
    if markers:
        mark=disk&(side==1)&(m<=HOLD)
        p[mark,2]+=bumps(m[mark]*np.cos(th[mark]),m[mark]*np.sin(th[mark]))
    return p.reshape(shape+(3,))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",required=True,type=Path,
        help="JSON list of [material,theta,phase,side] requests")
    parser.add_argument("--output",required=True,type=Path)
    parser.add_argument("--order",default=32,type=int)
    parser.add_argument("--design",choices=("rolled","ellipse"),default="ellipse")
    args=parser.parse_args()
    data=np.asarray(json.loads(args.input.read_text()),dtype=float)
    points=field(*data.T,order=args.order,design=args.design)
    args.output.write_text(json.dumps(points.tolist(),separators=(",",":"),allow_nan=False)+"\n")
