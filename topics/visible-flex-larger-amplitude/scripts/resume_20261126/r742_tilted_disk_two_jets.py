#!/usr/bin/env python3
"""Complete nonprojected physical two-jet of R740 ellipse and R742 tilted designs.

All arrays broadcast. Output shape is (...,6,3) in the published order
F, F_u, F_theta, F_uu, F_u_theta, F_theta_theta. u is normalized to [0,1]
by default; with normalized=False it is physical shoulder material distance.
"""
from dataclasses import dataclass
import numpy as np
import r740_rolled_disk_seed as base


@dataclass(frozen=True)
class Design:
    gamma: float
    height: float
    shift: float
    join: float
    end_height: float
    # Physical shape parameter, additional handle length in the left sector.
    left_handle: float=0.
    # Smooth interior deformations, x and z channels in the mirror frame.
    lateral: float=0.
    vertical: float=0.

    @property
    def length(self):
        return base.A_LENGTH+self.join+self.end_height


HORIZONTAL=Design(0.,.17,.12,.025,.025)
TILT32=Design(.32,.32,.16,.006,.006)
TILT44=Design(.44,.37,.19,.006,.006)
SOFT32=Design(.32,.32,.16,.006,.006,.09)
SOFT44=Design(.44,.37,.19,.006,.006,.09)
DESIGNS={"R740-ellipse":HORIZONTAL,"tilt32":TILT32,"tilt44":TILT44,
         "tilt32-soft":SOFT32,"tilt44-soft":SOFT44}
ORDER=("F","F_u","F_theta","F_uu","F_u_theta","F_theta_theta")


class J:
    """Scalar two-variable jet in unnormalized derivative coordinates."""
    __array_priority__=1000
    def __init__(self,v,s=0.,a=0.,ss=0.,sa=0.,aa=0.):
        self.v,self.s,self.a,self.ss,self.sa,self.aa=v,s,a,ss,sa,aa

    def parts(self):
        return self.v,self.s,self.a,self.ss,self.sa,self.aa

    def __add__(self,o):
        if not isinstance(o,J):
            return J(self.v+o,*self.parts()[1:])
        return J(*(x+y for x,y in zip(self.parts(),o.parts())))
    __radd__=__add__

    def __neg__(self):
        return J(*(-x for x in self.parts()))

    def __sub__(self,o):
        return self+(-o)

    def __rsub__(self,o):
        return (-self)+o

    def __mul__(self,o):
        if not isinstance(o,J):
            return J(*(x*o for x in self.parts()))
        return J(self.v*o.v,self.s*o.v+self.v*o.s,self.a*o.v+self.v*o.a,
                 self.ss*o.v+2*self.s*o.s+self.v*o.ss,
                 self.sa*o.v+self.s*o.a+self.a*o.s+self.v*o.sa,
                 self.aa*o.v+2*self.a*o.a+self.v*o.aa)
    __rmul__=__mul__

    def __truediv__(self,o):
        if not isinstance(o,J):
            return self*(1/o)
        v=1/o.v
        return self*unary(o,v,-v*v,2*v*v*v)


def unary(x,v,d,dd):
    return J(v,d*x.s,d*x.a,dd*x.s*x.s+d*x.ss,
             dd*x.s*x.a+d*x.sa,dd*x.a*x.a+d*x.aa)


def trig(x):
    c=np.cos(x.v);s=np.sin(x.v)
    return unary(x,c,-s,-c),unary(x,s,c,-s)


def cap_s7(x):
    v=np.clip(x.v,0,1)
    p=v*(1-v)
    return unary(x,base.s7(v),140*p**3,420*p*p*(1-2*v))


def clock(t,handle,material):
    # Lift of atan2(a*sin(pi*t),cos(pi*t)). Use the angle differential
    # (X dY-Y dX)/|X+iY|^2; this is regular even where cos(pi*t)=0.
    c,s=trig(t*np.pi)
    y=s*(J(material)/handle)
    h=c.v*c.v+y.v*y.v
    ps=(c.v*y.s-y.v*c.s)/h
    pa=(c.v*y.a-y.v*c.a)/h
    hs=2*(c.v*c.s+y.v*y.s)
    ha=2*(c.v*c.a+y.v*y.a)
    return J(np.arctan2(y.v,c.v),ps,pa,
        (c.v*y.ss-y.v*c.ss-ps*hs)/h,
        (c.a*y.s+c.v*y.sa-y.a*c.s-y.v*c.sa-ps*ha)/h,
        (c.v*y.aa-y.v*c.aa-pa*ha)/h)/np.pi


def disk_curve(x,order):
    b=base.beta(x.v);k=base.curvature(x.v)
    t=(x.v-base.HOLD)/base.BEND
    d=np.clip(np.minimum(t,1-t)/base.EDGE,0,1)
    dk=(np.pi/(2*base.BEND*(1-base.EDGE)))*(30*d*d*(1-d)**2)
    dk*=np.where(t<.5,1.,-1.)/(base.BEND*base.EDGE)
    u,v=base.bent_curve(x.v,order)
    c=np.cos(b);sn=np.sin(b)
    return unary(x,u,c,-k*sn),unary(x,v,sn,k*c),unary(x,b,k,dk)


def radii(s,order):
    a=base.angle_a(s.v)
    d=np.clip(np.minimum(s.v,base.A_LENGTH-s.v)/base.BLEND,0,1)
    k=base.s5(d)/base.TURN
    r,t=base.rolled_radii(s.v,order)
    c=np.cos(a);sn=np.sin(a)
    return unary(s,r,c,-k*sn),unary(s,t,sn,k*c)


def first(r,t,angle,design,order):
    co,si=trig(angle)
    x=r*co;y=r*si
    u,v,beta=disk_curve(x,order)
    cg,sg=np.cos(design.gamma),np.sin(design.gamma)
    c,b=trig(beta-design.gamma)
    h=v+design.height
    return u*cg+h*sg+t*b,y,h*cg-u*sg-t*c,x,c,b


def angle_inverse(th,order):
    phi=base.ellipse_angle(th.v,order)
    j=base.ELL_SCALE
    g=np.hypot(j*np.sin(phi),np.cos(phi))
    nodes,weights=base.rule(order)
    mean=np.hypot(j*np.sin(2*np.pi*nodes),np.cos(2*np.pi*nodes))@weights
    dp=mean/g
    d2p=-(j*j-1)*np.sin(phi)*np.cos(phi)*(dp/g)**2
    return unary(th,phi,dp,d2p)


def gather(components,n):
    zeros=np.zeros(n)
    return np.stack([np.stack([x.parts()[i]+zeros for x in components],axis=-1)
                     for i in range(6)],axis=-2)


def mirror_coordinates(X,Y,Z,design,side):
    cg,sg=np.cos(design.gamma),np.sin(design.gamma)
    z=Z*side
    return X*cg-z*sg,Y,X*sg+z*cg


def regular_jet(p,th,u_scale,design,order,side,stage):
    s=J(p,s=u_scale)
    a=J(th,a=1.)
    cg,sg=np.cos(design.gamma),np.sin(design.gamma)
    if stage=="A":
        r,t=radii(s,order)
        xa,y,za,*_=first(r,t,a,design,order)
    elif stage=="B":
        rb,tb=base.rolled_radii(base.A_LENGTH,order)
        x0,y,z0,x,c,b=first(rb,tb,a,design,order)
        time=(s-base.A_LENGTH)/design.join
        time.v=np.clip(time.v,0,1)
        # Positive, variable physical handles; the material seam speed stays
        # one. The weight is constant near the entire right half.
        left=cap_s7((-x-.20)/.55)
        handle=design.join+design.left_handle*left
        if design.left_handle!=0:
            time=clock(time,handle,design.join)
        S=cap_s7(time)
        gv=time.v*(1-time.v)**4*(1+time.v*(4+time.v*(10+2.5*time.v)))
        sv=base.s7(time.v)
        sv1=140*(time.v*(1-time.v))**3
        sv2=420*(time.v*(1-time.v))**2*(1-2*time.v)
        G=unary(time,gv,1-sv-sv1/2,-sv1-sv2/2)
        xe=base.ELL_SCALE*x+design.shift
        xa=(1-S)*x0+S*xe+handle*G*b
        za=(1-S)*z0+S*design.end_height+handle*(S-time+G-G*c)
        # Genuine spatial shape controls: zero through second order at both
        # ends. They are distinct from the material clock.
        if design.lateral or design.vertical:
            hv=time*(1-time)
            window=256*hv*hv*hv*hv
            xa+=design.lateral*left*window
            za+=design.vertical*left*window
    else:
        d=s-base.A_LENGTH-design.join
        chi=cap_s7(d*(2/design.end_height))
        new=a+chi*(angle_inverse(a,order)-a)
        cx,sy=trig(new)
        rb,_=base.rolled_radii(base.A_LENGTH,order)
        xa=design.shift+base.ELL_SCALE*rb*cx
        y=rb*sy;za=design.end_height-d
    return gather(mirror_coordinates(xa,y,za,design,side),len(p))


def _rotate(out,phase):
    c=np.cos(phase)[:,None];s=np.sin(phase)[:,None]
    x=out[:,:,0].copy();y=out[:,:,1].copy()
    out[:,:,0]=c*x-s*y
    out[:,:,1]=s*x+c*y
    return out


def shoulder_jet(u,theta,design=TILT32,normalized=True,phase=0.,side=1,order=32):
    base._public()
    t,a,phase,side=np.broadcast_arrays(np.asarray(u,dtype=float),np.asarray(theta,dtype=float),
        np.asarray(phase,dtype=float),np.asarray(side))
    shape=t.shape;t=t.ravel();a=a.ravel();phase=phase.ravel();side=side.ravel()
    factor=design.length if normalized else 1.
    s=t*factor
    if np.any((s<0)|(s>design.length+2e-14)) or np.any((side!=1)&(side!=-1)):
        raise ValueError("material shoulder or side outside the design")
    out=np.empty((len(s),6,3))
    a=a-phase
    for tag,mask in (("A",s<=base.A_LENGTH),
                     ("B",(s>base.A_LENGTH)&(s<=base.A_LENGTH+design.join)),
                     ("wall",s>base.A_LENGTH+design.join)):
        if np.any(mask):
            out[mask]=regular_jet(s[mask],a[mask],factor,design,order,side[mask],tag)
    return _rotate(out,phase).reshape(shape+(6,3))


def disk_jet(rho,theta,design=TILT32,phase=0.,side=1,order=32,markers=True):
    base._public()
    r,th,phase,side=np.broadcast_arrays(np.asarray(rho,dtype=float),np.asarray(theta,dtype=float),
        np.asarray(phase,dtype=float),np.asarray(side))
    shape=r.shape;r=r.ravel();th=th.ravel();phase=phase.ravel();side=side.ravel()
    if np.any((r<0)|(r>1+2e-14)) or np.any((side!=1)&(side!=-1)):
        raise ValueError("material disk or side outside the design")
    radius=J(r,s=1.);a=J(th-phase,a=1.)
    cs,sn=trig(a);x=radius*cs;y=radius*sn
    u,v,_=disk_curve(x,order)
    h=v+design.height
    cg,sg=np.cos(design.gamma),np.sin(design.gamma)
    out=gather(mirror_coordinates(u*cg+h*sg,y,h*cg-u*sg,design,side),len(r))
    out=_rotate(out,phase)
    if markers:
        c0,s0=trig(J(th,a=1.))
        x0,y0=radius*c0,radius*s0
        for px,py,rad in base.MARKERS:
            dx,dy=x0-px,y0-py
            q=1-(dx*dx+dy*dy)/(rad*rad)
            v=np.maximum(q.v,0)
            z=unary(q,1e-4*rad**2*v**3,3e-4*rad**2*v*v,6e-4*rad**2*v)
            out[:,:,2]+=np.stack([p+np.zeros(len(r)) for p in z.parts()],axis=-1)*(side==1)[:,None]
    return out.reshape(shape+(6,3))


def costs(jet,center):
    """Actual two first forms, normal support, oriented principal curvatures.
    The orientation here is material meridional x angular on the upper half.
    """
    F,Fu,Fa,Fuu,Fua,Faa=np.moveaxis(jet,-2,0)
    def dot(x,y):
        return np.sum(x*y,axis=-1)
    n=np.cross(Fu,Fa)
    area=np.linalg.norm(n,axis=-1)
    n=n/area[...,None]
    E,M,G=dot(Fu,Fu),dot(Fu,Fa),dot(Fa,Fa)
    e,f,g=dot(Fuu,n),dot(Fua,n),dot(Faa,n)
    trace=(e*G-2*f*M+g*E)/area**2
    det=(e*g-f*f)/area**2
    spread=np.sqrt(np.maximum(0,trace**2/4-det))
    return {"E":E,"mixed":M,"G":G,"area":area,"support":dot(F-center,n),
            "k1":trace/2-spread,"k2":trace/2+spread}
