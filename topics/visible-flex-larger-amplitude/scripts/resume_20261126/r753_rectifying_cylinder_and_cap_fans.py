#!/usr/bin/env python3
"""Exact rectifying flat central cylinder and two independent developable cap fans.
Direct six physical jets in the complete R747 material atlas.  The two joining
rolls carry three free physical channels.  The named reference uses none.
"""
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
import r752_delayed_turn_closed_two_jets as delay
ar=delay.ar
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7,gather

LEFT=-1.125
RIGHT=-1.045
VERTEX=3.
OLD=ar.old
AX=ar.axial
R=OLD.PLANAR_TURN

@dataclass(frozen=True)
class Shape:
    middle:float=2.**-38
    # Latitude coefficients of u_+^3, sin(u), sin(2u), one independent row per cap.
    plus:tuple=(2.**-27,0.,0.)
    minus:tuple=(-2.**-28,2.**-29,0.)
    # Independent rotation vectors and translations of the cap about its own center.
    plus_pose:tuple=(0.,0.,0.,0.,0.,0.)
    minus_pose:tuple=(0.,0.,0.,0.,0.,0.)

REFERENCE=Shape()

@lru_cache(maxsize=None)
def gauss(order):
    return np.polynomial.legendre.leggauss(order)

def bend(x,amplitude):
    w=RIGHT-LEFT
    t=np.clip((x-LEFT)/w,0.,1.)
    s=np.sin(np.pi*t);c=np.cos(np.pi*t)
    live=(x>LEFT)&(x<RIGHT)
    b=np.where(live,amplitude,0.)
    return (b*s**8,b*8*(np.pi/w)*s**7*c,
            b*8*(np.pi/w)**2*(7*s**6*c*c-s**8),
            b*8*(np.pi/w)**3*(42*s**5*c**3-22*s**7*c))

def frame(a,amplitude,order,position=False):
    q,t,n,k,ks=OLD.profile_coordinates(a,order)
    x=q[:,0];zero=np.zeros(len(x))
    al,b1,b2,b3=bend(x,amplitude);co=np.cos(al);si=np.sin(al)
    def vec(d,e,h):
        return np.stack([d*co-e*si,d*si+e*co,h],axis=-1)
    xp,zp=t.T
    xpp,zpp=(-k[:,None]*n).T
    T=vec(xp,zero,zp)
    acc=vec(xpp,b1*xp*xp,zpp)
    B=np.stack([zero,zero+1.,zero],axis=-1)
    eta=zero.copy();ep=zero.copy()
    live=(x>LEFT)&(x<RIGHT)
    if np.any(live):
        # The entire active window intersects only the two constant positive left arcs.
        # In particular all Frenet divisions below have denominator >=1/R on this mask.
        xxx=-k*k*xp;zzz=-k*k*zp
        g3=vec(xxx-b1*b1*xp**3,b2*xp**3+3*b1*xp*xpp,zzz)
        g4=vec(-k*k*xpp-3*b1*b2*xp**4-6*b1**2*xp*xp*xpp,
              b3*xp**4+6*b2*xp*xp*xpp+3*b1*xpp*xpp+4*b1*xp*xxx-b1**3*xp**4,
              -k*k*zpp)
        C=np.cross(T[live],acc[live]);kg=np.linalg.norm(C,axis=1)
        B[live]=C/kg[:,None]
        det=np.sum(C*g3[live],axis=1)
        eta[live]=det/kg**3
        ep[live]=(np.sum(C*g4[live],axis=1)/kg**3
              -3*eta[live]*np.sum(acc[live]*g3[live],axis=1)/kg**2)
    if not position:return eta,ep
    nodes,weights=gauss(order)
    delta=np.clip(x,LEFT,RIGHT)-RIGHT
    grid=RIGHT+delta[:,None]*(1+nodes)/2
    aa,_b,_c,_d=bend(grid,amplitude[:,None])
    dx=-delta*(np.sin(aa/2)**2@weights)
    dy=.5*delta*(np.sin(aa)@weights)
    gamma=np.stack([x+dx,dy,q[:,1]],axis=-1)
    return eta,ep,gamma,T,acc,B

def compose2(u,v,F,Fu,Fv,Fuu,Fuv,Fvv):
    def one(i):
        f,h,k,hh,hk,kk=[a[:,i] for a in (F,Fu,Fv,Fuu,Fuv,Fvv)]
        return J(f,h*u.s+k*v.s,h*u.a+k*v.a,
                 h*u.ss+k*v.ss+hh*u.s**2+2*hk*u.s*v.s+kk*v.s**2,
                 h*u.sa+k*v.sa+hh*u.s*u.a+hk*(u.s*v.a+u.a*v.s)+kk*v.s*v.a,
                 h*u.aa+k*v.aa+hh*u.a**2+2*hk*u.a*v.a+kk*v.a**2)
    return tuple(one(i) for i in range(3))

def cylinder(u,y,amplitude,order):
    a=np.asarray(u.v).copy();yv=np.broadcast_to(y.v,a.shape)
    for _ in range(30):
        e,ep=frame(a,amplitude,order)
        delta=a-u.v+yv*e
        if np.all(np.abs(delta)<8.e-15*(1.+np.abs(a))):break
        den=1+yv*ep
        if np.min(den)<=0:raise ValueError("rectifying chart lost orientation")
        a=a-delta/den
    e,ep,g,T,acc,B=frame(a,amplitude,order,True)
    den=1+yv*ep
    if np.any(den<=0) or np.any(np.abs(a-u.v+yv*e)>3.e-13*(1.+np.abs(a))):
        raise ValueError("rectifying inverse did not converge")
    P=g+yv[:,None]*(B+e[:,None]*T)
    ss=acc/den[:,None]
    return compose2(u,y,P,T,B,ss,-e[:,None]*ss,e[:,None]**2*ss)

def latitude(u,coeff,phase):
    a,b,c=coeff;pos=np.maximum(u,0.)
    return (phase*(a*pos**3+b*np.sin(u)+c*np.sin(2*u)),
            phase*(3*a*pos**2+b*np.cos(u)+2*c*np.cos(2*u)),
            phase*(6*a*pos-b*np.sin(u)-4*c*np.sin(2*u)))

def fan_delta(x,z,coeff,ph,order):
    # Polar fan in the material cap plane.  The pole (3,0) lies outside both disks.
    h=VERTEX-x;v=z/h
    u=unary(v,np.arctan(v.v),1/(1+v.v**2),-2*v.v/(1+v.v**2)**2)
    sq=h*h+z*z;r=np.sqrt(sq.v);r=unary(sq,r,.5/r,-.25/r**3)
    u0=u.v;phase=np.sin(ph)
    nodes,w=gauss(order);g=u0[:,None]*(nodes+1.)/2.
    lat,l1,_=latitude(g,coeff,phase[:,None])
    if np.any(abs(l1)>=1) or np.any(abs(lat)>=np.pi/2):raise ValueError("singular spherical fan")
    cs=np.cos(lat);root=np.sqrt(1-l1*l1)
    corr=(np.sin(lat)**2-l1*l1)/(cs*(root+cs))
    dq=.5*u0*(corr@w)
    lat,l1,l2=latitude(u0,coeff,phase)
    cs=np.cos(lat);sn=np.sin(lat);root=np.sqrt(1-l1*l1)
    q1=root/cs
    q2=-l1*l2/(root*cs)+q1*np.tan(lat)*l1
    q=unary(u,u0+dq,q1,q2);l=unary(u,lat,l1,l2)
    cq,sq=trig(q);cl,sl=trig(l);cu,su=trig(u)
    return (r*(cu-cq*cl),r*sl,r*(sq*cl-su))

def transport_weight(b,method):
    q=b/delay.END_LENGTH
    if method in ("legacy","arc"):return 1-cap_s7(q)
    if method!="plateau":raise ValueError("unknown R753 angular transport")
    edge=.08;u=np.clip(q.v,0,1);t=np.clip(np.minimum(u,1-u)/edge,0,1)
    area=edge*(2.5*t**4-3*t**5+t**6)
    lo=np.where(u<edge,area,u-edge/2)
    a=np.where(u>1-edge,1-edge-area,lo)
    f=OLD.disk.s5(t)
    fp=30*t*t*(1-t)**2*np.where(u<.5,1.,-1.)/edge
    return unary(q,1-a/(1-edge),-f/(1-edge),-fp/(1-edge))

def posed_fan(x,z,shape,sg,ph,order):
    coeff=shape.plus if sg==1 else shape.minus
    pose=shape.plus_pose if sg==1 else shape.minus_pose
    d=fan_delta(x,z,coeff,ph,order)
    if not any(pose):return d
    a=np.asarray(pose[:3]);norm=np.linalg.norm(a);s=np.sin(ph)
    pc=(x-OLD.CENTER_X+d[0],d[1],z+d[2])
    ret=list(d)
    if norm:
        k=a/norm
        cross=(k[1]*pc[2]-k[2]*pc[1],k[2]*pc[0]-k[0]*pc[2],k[0]*pc[1]-k[1]*pc[0])
        cross2=(k[1]*cross[2]-k[2]*cross[1],k[2]*cross[0]-k[0]*cross[2],k[0]*cross[1]-k[1]*cross[0])
        ret=[v+np.sin(norm*s)*c+2*np.sin(norm*s/2)**2*cc for v,c,cc in zip(ret,cross,cross2)]
    return tuple(v+s*h for v,h in zip(ret,pose[3:]))

def chart_jet(chart,u,v,phase=0.,order=32,shape=REFERENCE,roll_field=None,rotate=True,method="legacy"):
    """roll_field(sign,s,v,phase) returns three C2 J values in the actual material
    coordinates, with value and first two transverse jets zero at both joins."""
    OLD.disk._public()
    a,b,t=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float),np.asarray(phase,float))
    sh=a.shape;t=t.ravel();a=J(a.ravel(),s=1.);b=J(b.ravel(),a=1.)
    if np.any((t<0)|(t>np.pi/2+2.e-14)):raise ValueError("phase outside the closed interval")
    amp=shape.middle*np.sin(t)
    if chart=="cylinder":
        if np.any(abs(b.v)>delay.HALF_WIDTH+2.e-14):raise ValueError("outside central cylinder")
        x,y,z=cylinder(a+R*t,b,amp,order)
    elif chart in ("end+","end-"):
        sg=1 if chart.endswith("+") else -1
        if np.any((b.v<0)|(b.v>delay.END_LENGTH+2.e-14)):raise ValueError("outside roll")
        w=cap_s7(b/delay.END_LENGTH);gate=transport_weight(b,method)
        p,d=delay.end_offsets(b,order);y=sg*(delay.HALF_WIDTH+p)
        s=a+R*t*gate if method=="legacy" else ar.angular_shift(a,d,t,gate,order)
        q,n=OLD.profile(s,order);x,z=[q[i]-d*n[i] for i in range(2)]
        C=cylinder(s,y,amp,order);fan=posed_fan(x,z,shape,sg,t,order)
        base=(x,y,z);central=(q[0],y,q[1])
        x,y,z=[base[i]+(1-w)*(C[i]-central[i])+w*fan[i] for i in range(3)]
        if roll_field is not None:
            dx,dy,dz=roll_field(sg,a,b,t)
            x,y,z=x+dx,y+dy,z+dz
    else:
        x,y,z=delay.sphere_chart(chart,a,b,t,order,"legacy")
        fan=posed_fan(x,z,shape,1 if chart.endswith("+") else -1,t,order)
        x,y,z=x+fan[0],y+fan[1],z+fan[2]
    if rotate:
        ox,oz=AX.axis(order);co=np.cos(t);si=np.sin(t);X=x-ox;Z=z-oz
        x,z=ox+co*X-si*Z,oz+si*X+co*Z
    return gather((x,y,z),len(t)).reshape(sh+(6,3))
