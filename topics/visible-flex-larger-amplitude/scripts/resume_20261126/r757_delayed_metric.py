#!/usr/bin/env python3
"""R757 new fixed metric and two-jets. R752's delayed v-law, R757's true planar section."""
import sys
import numpy as np
import r752_delayed_turn_closed_two_jets as prior
import r757_curved_profile_two_jets as old
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather
ar=sys.modules[__name__]
axial=old
ax=axial
cap=prior.cap
RADIUS=old.PLANAR_TURN
HALF_WIDTH=prior.HALF_WIDTH
EXTRA=prior.EXTRA
SMALL_ANGLE=prior.SMALL_ANGLE
END_LENGTH=prior.END_LENGTH
BEND=prior.BEND
JOIN=prior.ar.JOIN
RAMP=prior.ar.RAMP
end_offsets=prior.end_offsets
end_limits=prior.end_limits
original_parameter=prior.original_parameter
clock_at=prior.clock_at
angular_data=old.angular_data
cap_leaf=prior.ar.cap_leaf

CAP_JOIN=.00025
CAP_BACKGROUND=1.e-8
CAP_BUMP=.00035
CAP_RADIUS=.04

def cap_height(x,z,w):
    """Nonflat on both complete initial caps; w=None selects the Cartesian core."""
    q=.1+.1*((x-old.CENTER_X)*(x-old.CENTER_X)+z*z)
    gate=J(1.) if w is None else cap_s7(w/CAP_JOIN)
    h=1-((x+.35)*(x+.35)+z*z)/CAP_RADIUS**2
    p=np.maximum(h.v,0.)
    return CAP_BACKGROUND*q*gate+CAP_BUMP*unary(h,p**4,4*p**3,12*p*p)

def polar_point(u,d,rho,order):
    q,n=old.profile(u,order)
    return (old.CENTER_X+rho*(q[0]-d*n[0]-old.CENTER_X),rho*(q[1]-d*n[1]))
def lifted(u, order):
    a,k,kp = angular_data(u.v,order)
    return unary(u,a,k,kp)


def angular_shift(u, d, theta, weight, order):
    """Invert the monotone lifted arclength, then implicitly differentiate twice."""
    a0 = lifted(u,order)
    advance = theta*(RADIUS-d)*weight
    if np.all(advance.v==0.) and np.all(theta==0.):
        return u
    # The derivative of s-d*Theta is >=1-.109/.15>.27 throughout this atlas.
    lo = np.asarray(u.v,dtype=float).copy()
    hi = lo+advance.v/.26
    pos = np.minimum(hi,np.maximum(lo,lo+advance.v))
    active = np.ones_like(pos,dtype=bool)
    for _ in range(58):
        if not np.any(active):
            break
        ang,k,_ = angular_data(pos,order)
        err = pos-u.v-d.v*(ang-a0.v)-advance.v
        active &= (np.abs(err)>7e-15*(1+np.abs(pos)))
        lo = np.where(active&(err<0),pos,lo)
        hi = np.where(active&(err>0),pos,hi)
        new = pos-err/(1-d.v*k)
        new = np.where((new>lo)&(new<hi),new,(lo+hi)/2)
        pos = np.where(active,new,pos)
    ang,k,kp = angular_data(pos,order)
    denom = 1-d.v*k
    rhs = u-d*a0+advance
    su = (rhs.s+d.s*ang)/denom
    sv = (rhs.a+d.a*ang)/denom
    first = J(pos,su,sv)
    residue = first-d*unary(first,ang,k,kp)-rhs
    return J(pos,su,sv,-residue.ss/denom,-residue.sa/denom,-residue.aa/denom)


def sphere_chart(chart,u,v,t,order,method):
    if chart=="cylinder":
        if np.any(abs(v.v)>HALF_WIDTH+2e-14):raise ValueError("outside central cylinder")
        q,n=old.profile(u+RADIUS*t,order)
        return q[0],v,q[1]
    sg=1 if chart.endswith("+") else -1
    if chart in ("end+","end-"):
        p,d=end_offsets(v,order)
        if method=="legacy":
            s=u+RADIUS*t*(1-cap_s7(v/END_LENGTH))
        else:
            s=ar.angular_shift(u,d,t,J(1.),order)
        q,n=old.profile(s,order)
        return q[0]-d*n[0],sg*(HALF_WIDTH+p),q[1]-d*n[1]
    if chart not in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
        raise ValueError("unknown closed R757 material chart")
    pb,db=end_limits(order)
    if chart.startswith("cap-cartesian"):
        x,z=u,v;w=None
    else:
        w=v if chart.startswith("cap-normal") else 1-v
        maximum=ar.JOIN if chart.startswith("cap-normal") else 1.
        if np.any((w.v<0)|(w.v>maximum+2e-14)):raise ValueError("outside cap chart")
        d,rho=ar.cap_leaf(w,order);d=d+db-old.original.end_limits(order)[1]
        s=u if method=="legacy" else ar.angular_shift(u,d,t,1-cap_s7((w-.25)/.50),order)
        x,z=ar.polar_point(s,d,rho,order)
    return x,sg*(J(HALF_WIDTH+pb)+cap_height(x,z,w)),z

def chart_jet(chart,u,v,phase=0.,order=32,method="legacy",bend=BEND,free_field=None,rotate=True):
    """Coordinates are those of R747, with |v|<=.37 on the cylinder and
    v in [0,END_LENGTH] on either rolled annulus.  The caps span their full disks.
    free_field(chart,u,v,t,x,y,z) supplies three optional C2 material two-jets."""
    old.disk._public()
    aa,bb,th=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    sh=aa.shape;t=th.ravel();a=J(aa.ravel(),s=1.);b=J(bb.ravel(),a=1.)
    if method not in ("legacy","arc") or np.any((t<0)|(t>np.pi/2+2e-14)) or bend<0:
        raise ValueError("invalid angle rule, phase, or bending magnitude")
    x,y,z=sphere_chart(chart,a,b,t,order,method)
    sg=np.where(y.v>=0,1.,-1.)
    if bend:
        weight=cap_s7((y*sg-HALF_WIDTH)/.38)
        dx,h=cap.development(x,t,bend,order)
        x,y=x+weight*dx,y+sg*weight*h
    if free_field is not None:
        dx,dy,dz=free_field(chart,a,b,t,x,y,z)
        x,y,z=x+dx,y+dy,z+dz
    if rotate:
        ox,oz=ax.axis(order);co=np.cos(t);si=np.sin(t);X=x-ox;Z=z-oz
        x,z=ox+co*X-si*Z,oz+si*X+co*Z
    return gather((x,y,z),len(t)).reshape(sh+(6,3))
