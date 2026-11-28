#!/usr/bin/env python3
"""R752 delayed positive-curvature turns on the full R747 closed material atlas.
The phase-zero tensor belongs to this new body.  All reported derivatives are
material derivatives of the actual maps (F,Fu,Fv,Fuu,Fuv,Fvv).
"""
from functools import lru_cache
import numpy as np
import r748_developable_axial_caps as cap
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

ar=cap.ar
old=ar.old
ax=ar.axial
HALF_WIDTH=.37
EXTRA=.81
SMALL_ANGLE=1./1024.
END_LENGTH=old.END_LENGTH+EXTRA
BEND=1./4096

def cumulative(alpha):
    z=np.clip(alpha/SMALL_ANGLE,0.,1.)
    # 1-(1-z)^4 in its stable small-z form
    return z*(4+z*(-6+z*(4-z)))

def clock_at(v0):
    a=old.disk.softened_angle(v0,old.END_LENGTH,old.END_BLEND,1/old.END_TURN)
    return v0+EXTRA*cumulative(a)

def original_parameter(v):
    # Scalar inverse by monotone interval contraction, including the retimed tiny ramp.
    lo=np.zeros_like(v);hi=np.full_like(v,old.END_LENGTH)
    for _ in range(53):
        mid=(lo+hi)/2;left=clock_at(mid)<v
        lo=np.where(left,mid,lo);hi=np.where(left,hi,mid)
    return np.where(v<=0,0.,np.where(v>=END_LENGTH,old.END_LENGTH,(lo+hi)/2))

def end_offsets(v,order):
    if np.any((v.v<0)|(v.v>END_LENGTH+2e-14)):raise ValueError("outside R752 rolled end")
    v0=original_parameter(v.v)
    a,k,_,p0,d0=old.turn(v0,np.pi/2,old.END_TURN,old.END_BLEND,order)
    nodes,weights=cap.rule(order)
    t=np.clip(a/SMALL_ANGLE,0.,1.);z=t[:,None]*(1+nodes)/2
    mass=4*(1-z)**3;angle=SMALL_ANGLE*z
    p=p0+.5*EXTRA*t*((mass*np.cos(angle))@weights)
    d=d0+.5*EXTRA*t*((mass*np.sin(angle))@weights)
    ap=k/(1+EXTRA*(4/SMALL_ANGLE)*(1-t)**3*k)
    return unary(v,p,np.cos(a),-np.sin(a)*ap),unary(v,d,np.sin(a),np.cos(a)*ap)

@lru_cache(maxsize=None)
def end_limits(order=32):
    p,d=end_offsets(J(np.array([END_LENGTH])),order)
    return float(p.v[0]),float(d.v[0])

def sphere_chart(chart,u,v,t,order,method):
    if chart=="cylinder":
        if np.any(abs(v.v)>HALF_WIDTH+2e-14):raise ValueError("outside central cylinder")
        q,n=old.profile(u+ax.RADIUS*t,order)
        return q[0],v,q[1]
    sg=1 if chart.endswith("+") else -1
    if chart in ("end+","end-"):
        p,d=end_offsets(v,order)
        if method=="legacy":
            s=u+ax.RADIUS*t*(1-cap_s7(v/END_LENGTH))
        else:
            s=ar.angular_shift(u,d,t,J(1.),order)
        q,n=old.profile(s,order)
        return q[0]-d*n[0],sg*(HALF_WIDTH+p),q[1]-d*n[1]
    if chart not in ("cap+","cap-","cap-normal+","cap-normal-","cap-cartesian+","cap-cartesian-"):
        raise ValueError("unknown closed R752 material chart")
    pb,db=end_limits(order)
    if chart.startswith("cap-cartesian"):
        x,z=u,v
    else:
        w=v if chart.startswith("cap-normal") else 1-v
        maximum=ar.JOIN if chart.startswith("cap-normal") else 1.
        if np.any((w.v<0)|(w.v>maximum+2e-14)):raise ValueError("outside cap chart")
        d,rho=ar.cap_leaf(w,order);d=d+db-old.end_limits(order)[1]
        s=u if method=="legacy" else ar.angular_shift(u,d,t,1-cap_s7((w-.25)/.50),order)
        x,z=ar.polar_point(s,d,rho,order)
    return x,sg*J(HALF_WIDTH+pb),z

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
