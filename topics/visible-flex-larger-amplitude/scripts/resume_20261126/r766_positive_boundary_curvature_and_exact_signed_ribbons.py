#!/usr/bin/env python3
"""R766 planar unit-arclength closure with a positive turning profile at every original nonzero curvature label."""
from functools import lru_cache
import numpy as np
import r764_corrugated_pre_roll_and_movable_complete_caps as base
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather
old=base.old;m=base.m
EPS=.025
E=base.E


def preload(ph):
    return EPS+(1-EPS)*np.exp(-(float(ph)/.025)**2)


def rot(v,ang):
    c,h=np.cos(ang),np.sin(ang);x,z=v[...,0],v[...,1]
    return np.stack((c*x-h*z,h*x+c*z),axis=-1)


def knob(s,order):
    lo=float(m.flat_material_s(np.asarray([-.95]),order=order)[0]);w=1.10
    z=J(s,s=1.);b=cap_s7((z-lo)/.22)*cap_s7((lo+w-z)/.22)
    return b.v,b.s,b.ss


def joining_clock(x):
    left=1.05;right=np.pi-.38;edge=.14;length=right-left
    z=np.clip(x-left,0.,length)
    def primitive(t):
        return 2.5*t**4-3*t**5+t**6
    v=np.clip(z/edge,0.,1.);w=np.clip((length-z)/edge,0.,1.)
    u=np.where(z<edge,edge*primitive(v),np.where(z<=length-edge,z-edge/2,
         length-edge-edge*primitive(w)))
    speed=np.where(z<edge,10*v**3-15*v**4+6*v**5,
          np.where(z<=length-edge,1.,10*w**3-15*w**4+6*w**5))
    der=np.where(z<edge,30*v*v*(1-v)**2/edge,
          np.where(z<=length-edge,0.,-30*w*w*(1-w)**2/edge))
    return 1-u/(length-edge),-speed/(length-edge),-der/(length-edge)


def right_data(order):
    lh,_,m1,_,_,_,_,_,start,stop,_,_=m.constants(order)
    return m.LEFT_LENGTH/2+start+m1-lh,m.LEFT_LENGTH/2+stop


def rigid_weight(s,order):
    half=old.material(order,True)[-1];top=np.mod(s.v,2*half);lo=top>half
    u=unary(s,np.where(lo,2*half-top,top),np.where(lo,-1.,1.),0.)
    start,end=right_data(order)
    # The exact constant-rate turn is x=(s-start-blend/2)/R in this region.
    edge=start+m.old.PLANAR_BLEND/2+m.old.PLANAR_TURN*(np.pi-.38)
    return cap_s7((u-edge+.012)/.012)




def cuts(order,ph):
    lh,m0,m1,rtop,_,_,_,_,a,stop,_,_=m.constants(order)
    left=m.LEFT_LENGTH/2;cut,_,half=old.material(order,True)
    pos=left+a-lh;bl=m.old.PLANAR_BLEND
    t=np.r_[lh,lh+bl,m0-bl,m0,m0+1+np.array([-.95,-.73,-.50,-.07,.15,.30,.3325,.5275,.56,1.]),
            m1+bl,rtop-bl,rtop]
    origins=pos+t;crit=np.r_[0.,left-m.CLOCK_EDGE*m.LEFT_LENGTH,left,origins,origins-.15*ph,
        cut+np.asarray(old.clock_spec(True)[1]),m.grip_s(.55,order),
        pos+m1+bl/2+.15*np.array([1.05,1.19,np.pi-.52,np.pi-.38]),half]
    use=np.unique(crit[(crit>=0.)&(crit<=half)])
    use=use[np.r_[True,np.diff(use)>3e-13]];use[-1]=half
    return use


def angles(s,ph,order,b):
    sh=s.shape;ss=np.asarray(s,float).ravel();eps=preload(ph)
    out=[]
    for lo in range(0,len(ss),2048):
        a=ss[lo:lo+2048]
        _,t,_,k,kp=old.data(a,ph,order,True)
        _,t0,_,k0,kp0=old.data(a,0.,order,True)
        delta=np.arctan2(t[:,0]*t0[:,1]-t[:,1]*t0[:,0],np.einsum("ij,ij->i",t,t0))
        f,fs,fss=knob(a,order);ang=eps*delta+b*f
        tang=rot(t,ang);curv=(1-eps)*k+eps*k0-b*fs
        curvp=(1-eps)*kp+eps*kp0-b*fss
        start,end=right_data(order);active=a>=start+.0005+.15*1.05
        if np.any(active):
            local=np.clip(a[active]-start,0.,end-start)
            xx=m.old.disk.softened_angle(local,end-start,m.old.PLANAR_BLEND,1/m.old.PLANAR_TURN)
            w,ws,wss=joining_clock(xx);omega=(1-eps)*ph
            tang[active]=rot(t0[active],-omega*w)
            curv[active]=k0[active]*(1+omega*ws)
            curvp[active]=kp0[active]*(1+omega*ws)+omega*wss*k0[active]**2
        out.append(np.column_stack((tang,curv,curvp)))
    return np.concatenate(out).reshape(sh+(4,))


@lru_cache(maxsize=128)
def state(order,ph):
    grid=cuts(order,ph);nodes,weights=m.old.disk.rule(order);width=np.diff(grid)
    u=grid[:-1,None]+width[:,None]*nodes
    raw=angles(u,ph,order,0.)[...,:2]
    initial=float(np.sum(width*(raw[:,:,1]@weights)))
    bell=knob(u,order)[0]
    def end(b):
        return float(np.sum(width*(rot(raw,b*bell)[...,1]@weights)))
    if ph==0.:
        b=0.
    else:
        low,hi=-.45,.45
        if end(low)>0 or end(hi)<0:
            raise ValueError("original signed closure bracket")
        for _ in range(58):
            mid=(low+hi)/2
            if end(mid)>0:hi=mid
            else:low=mid
        b=(low+hi)/2
    tt=rot(raw,b*bell);deltas=width[:,None]*np.einsum("ijk,j->ik",tt,weights)
    start=old.data(np.array([0.]),ph,order,True)[0][0]
    Q=start+np.vstack((np.zeros(2),np.cumsum(deltas,axis=0)))
    anchor=m.grip_s(.55,order);idx=np.argmin(np.abs(grid-anchor))
    original,t,*_=old.data(np.array([anchor]),ph,order,True)
    tangent=angles(np.array([anchor]),ph,order,b)[0,:2]
    phi=float(np.arctan2(tangent[0]*t[0,1]-tangent[1]*t[0,0],tangent@t[0]))
    shift=original[0]-rot(Q[idx],phi)
    return grid,Q,b,phi,shift,[initial,float(Q[-1,1]),float(b)]


def curve(s,ph,order=32,aligned=True):
    arr=np.asarray(s,float);shape=arr.shape
    if float(ph)==0.:
        raw=old.data(arr.ravel(),0.,order,True)
        return tuple(a.reshape(shape+a.shape[1:]) for a in raw)
    ss,ii=np.unique(arr.ravel(),return_inverse=True)
    half=old.material(order,True)[-1];z=np.mod(ss,2*half)
    lower=z>half;u=np.where(lower,2*half-z,z);grid,Q,b,phi,tr,_=state(order,float(ph))
    j=np.clip(np.searchsorted(grid,u,side="right")-1,0,len(grid)-2);ds=u-grid[j]
    nodes,weights=m.old.disk.rule(order)
    t=angles(grid[j,None]+ds[:,None]*nodes,ph,order,b)[...,:2]
    pos=Q[j]+ds[:,None]*np.einsum("ijk,j->ik",t,weights)
    h=angles(u,ph,order,b);t=h[:,:2].copy()
    pos[lower,1]*=-1;t[lower,0]*=-1;h[lower,3]*=-1
    if aligned:
        pos=rot(pos,phi)+tr;t=rot(t,phi)
    n=np.stack((-t[:,1],t[:,0]),axis=-1)
    return tuple(a[ii].reshape(shape+a.shape[1:]) for a in (pos,t,n,h[:,2],h[:,3]))


def curve_jet(s,ph,order):
    q,t,n,k,kp=curve(s.v,ph,order)
    return ([unary(s,q[:,i],t[:,i],-k*n[:,i]) for i in range(2)],
            [unary(s,n[:,i],k*t[:,i],kp*t[:,i]-k*k*n[:,i]) for i in range(2)])


def central(s,y,ph,order,side=1):
    a,b=np.broadcast_arrays(np.asarray(s,float),np.asarray(y,float));shape=a.shape
    a,b=a.ravel(),b.ravel();u,v=J(a,s=1.),J(b,a=1.)
    q,n=curve_jet(u,ph,order);h=m.marks(u,v,order)
    return gather((q[0]+h*n[0],v,q[1]+h*n[1]),len(a)).reshape(shape+(6,3))


def exact_scaled_ribbon(s,v,ph,order,ratio,side):
    """Whole E ribbon on a true sector satisfying k_new=ratio*k0, including both zero continuations."""
    a,b=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float));shape=a.shape
    a,b=a.ravel(),b.ravel();u,vj=J(a,s=1.),J(b,a=1.)
    q,n=curve_jet(u,ph,order);_,d=base.initial_turn(vj,order)
    nodes,weights=m.old.disk.rule(order)
    def alpha(r):
        return base.EPS*np.sin(2*np.pi*r/E)*np.sin(np.pi*r/E)**2
    def slope(r):
        return np.sqrt(1-(np.sin(alpha(r))/ratio)**2)
    p=np.zeros_like(b)
    for lo,hi in zip((0.,E/4,E/2,3*E/4),(E/4,E/2,3*E/4,E)):
        span=np.clip(b-lo,0.,hi-lo)
        p+=span*(slope(lo+span[:,None]*nodes)@weights)
    w=np.pi*b/E;av=alpha(b);ad=base.EPS*np.pi/E*(2*np.cos(2*w)*np.sin(w)**2+np.sin(2*w)**2)
    pv=slope(b);pp=-np.sin(av)*np.cos(av)*ad/(ratio**2*pv)
    y=unary(vj,p,pv,pp)
    return gather((q[0]-d*n[0]/ratio,side*(base.HALF+y),q[1]-d*n[1]/ratio),len(a)).reshape(shape+(6,3))

@lru_cache(maxsize=128)
def right_motion(order,ph):
    end=old.material(order,True)[-1];q=curve(np.array([end]),ph,order)[0][0]
    q0=old.data(np.array([end]),0.,order,True)[0][0]
    angle=state(order,ph)[3] if ph else 0.
    return angle,q-rot(q0,angle)


def moved_whole(chart,s,v,ph,order):
    j=base.chart_jet(chart,s,v,0.,order,.14,False)
    angle,tr=right_motion(order,ph);q=rot(j[...,[0,2]],angle)
    j[...,0]=q[...,0];j[...,2]=q[...,1];j[...,0,0]+=tr[0];j[...,0,2]+=tr[1]
    return j
