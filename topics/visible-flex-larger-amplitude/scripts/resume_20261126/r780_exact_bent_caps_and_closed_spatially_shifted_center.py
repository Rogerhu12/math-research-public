#!/usr/bin/env python3
"""R780 full two-jets: closed displaced developable center, two exactly isometric finite curved caps and genuine lips."""
from functools import lru_cache
import numpy as np
import r777_bent_complete_caps_and_true_terminal_collars as prior
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

c=prior.c;base,old,m=c.base,c.old,c.m
E,B,OLD_L=c.E,c.B,c.L
LIP=.006
L=OLD_L+LIP
T=E+L
PITCH=.26
WIDTH=.30
DWELL=.18
RAMP=.0005
FULL=2*WIDTH+DWELL
MODES={"down55":(1.,.55),"up55":(-1.,.55),"down85":(1.,.85),"up85":(-1.,.85)}

def inputs(chart,a,b):
    return J(np.asarray(a),s=1.),J(np.asarray(b),a=1.)

def fold_angle(t,turn):
    rate=turn/(WIDTH-RAMP)
    def stroke(t):
        d=np.clip(np.minimum(t,WIDTH-t)/RAMP,0.,1.)
        return m.old.disk.softened_angle(t,WIDTH,RAMP,rate),rate*m.old.disk.s5(d)
    a,ap=stroke(t);b,bp=stroke(t-WIDTH-DWELL)
    return a-b,ap-bp

FCUT=(0.,RAMP,WIDTH-RAMP,WIDTH,WIDTH+DWELL,WIDTH+DWELL+RAMP,FULL-RAMP,FULL)

@lru_cache(maxsize=256)
def full_fold(turn,order):
    cs,sn=m.old.disk.integrals(np.asarray(FULL),FCUT,lambda t:fold_angle(t,turn)[0],order)
    return FULL-float(cs),float(sn)

def material_x(s,order):
    half=old.material(order,True)[-1];u=np.mod(s.v,2*half);low=u>half
    start=float(m.flat_material_s(np.array([0.]),order=order)[0])
    x=np.where(low,2*half-u,u)-start
    return unary(s,x,np.where(low,-1.,1.),0.)

def central_shift(s,y,ph,order,mode):
    turn=MODES[mode][0]*2.16*prior.smooth(ph/.90)
    cp,sp=np.cos(PITCH),np.sin(PITCH);x=material_x(s,order)
    v=cp*(x+.35)+sp*y+FULL/2
    w=np.clip(v.v,0.,FULL)
    ch,sh=m.old.disk.integrals(w,FCUT,lambda z:fold_angle(z,turn)[0],order)
    a,k=fold_angle(w,turn);D,S=full_fold(turn,order)
    h=unary(v,D-w+ch,np.cos(a)-1.,-k*np.sin(a))
    z=unary(v,sh-S,np.sin(a),k*np.cos(a))
    return cp*h,sp*h,z

def roll_offsets(chart,v,order):
    if chart.startswith("preband"):return base.initial_turn(v,order)
    t=v.v;vp=unary(v,np.minimum(t,OLD_L),(t<=OLD_L).astype(float),0.)
    p,d=m.end(vp,order)
    lip=unary(v,np.maximum(t-OLD_L,0.),(t>OLD_L).astype(float),0.)
    return base.axial(order)+p,d+lip

def crown(x,z):
    total=J(np.zeros_like(z.v))
    for h in (-.40,.40):
        xx=(x+.5)/.09;zz=(z-h)/.09;r=1-xx*xx-zz*zz
        t=np.maximum(0.,r.v)
        total=total+.0015*unary(r,t**4,4*t**3,12*t*t)
    return total

def physical_cap(chart,a,b,order):
    if chart.startswith(("cap-cartesian","cap-island")):return inputs(chart,a,b)
    v=J(b,a=1.);w=v if chart.startswith("cap-normal") else 1-v
    raww=w+LIP*(1-cap_s7((w-.0004)/.035))
    q=1-raww;sg=chart[-1]
    oldj=base.chart_jet("cap"+sg,a,q.v,0.,order,.14,False)
    def compose(j):
        x,ds,dv,dss,dsv,dvv=j.T
        return J(x,ds,dv*q.a,dss,dsv*q.a,dvv*q.a*q.a+dv*q.aa)
    return compose(oldj[:,:,0]),compose(oldj[:,:,2])

def endpoints(s,ph,order,side,mode):
    q,_=c.section(s,ph,order);y=J(np.full(len(s.v),side*B))
    dx,dy,dz=central_shift(s,y,ph,order,mode)
    return q[0]+dx,y+dy,q[1]+dz

def initial_rim(s,order):
    q,n=old.profile(s,0.,order,True);d=m.terminal(order)[1]+LIP
    return q[0]-d*n[0],q[1]-d*n[1]

def orientation(ph,order,mode):
    oldr=old.data(np.asarray([prior.wall_label(order)]),0.,order,True)[0][0]
    _,db=m.terminal(order);d=oldr[0]-db-LIP-.30
    zl=.71-db-LIP;zr=oldr[1];k=prior.smooth(ph/.90)
    y,z,_,_=prior.bent(J(np.array([zl,zr])),k,order)
    delta=np.arctan2(y.v[1]-y.v[0],d)*MODES[mode][1]
    return np.cos(delta),np.sin(delta),y.v[0],d,zl,zr

@lru_cache(maxsize=256)
def pose(ph,order,mode):
    co,si,Yl,d,zl,zr=orientation(ph,order,mode)
    pb=m.terminal(order)[0];b0=base.axial(order)+pb
    ramp=prior.smooth(ph/.35);separation=(1-ramp)*b0+ramp*.065
    if not ph:return (co,si,Yl,0.,0.,0.,separation,0.,d,zl,zr)
    grid=c.stations(order);half=old.material(order,True)[-1]
    a=np.unique(np.r_[grid,2*half-grid,np.arange(512)*2*half/512])
    s=J(a,s=1.);rx,rz=initial_rim(s,order);k=prior.smooth(ph/.90)
    yy,zz,_,_=prior.bent(rz,k,order);A=rx.v-.30;V=yy.v-Yl
    bx=.30+co*A+si*V;by=-si*A+co*V
    costs=[]
    for sg in (1,-1):
        x,y,z=endpoints(s,ph,order,sg,mode)
        costs.append(np.column_stack((bx-x.v,by+sg*(B+separation)-y.v,zz.v-z.v)))
    D=np.vstack(costs)
    # The same actual three-dimensional translation is used by both caps.
    power=40.;t=-np.mean(D,axis=0)
    def ev(t):
        r=D+t;y=np.einsum("ij,ij->i",r,r);high=np.max(y)
        w=np.exp(power*(y-high));total=np.sum(w);w/=total
        g=w@r;v=r-g
        return high+np.log(total/len(y))/power,2*g,2*np.eye(3)+4*power*(v.T@(w[:,None]*v))
    for _ in range(40):
        f,g,H=ev(t)
        if np.linalg.norm(g)<2e-12:break
        step=np.linalg.solve(H,g);l=1.
        for _ in range(22):
            if ev(t-l*step)[0]<=f-.0001*l*(g@step):break
            l*=.5
        t-=l*step
    residual=float(np.linalg.norm(ev(t)[1]));t*=prior.smooth(ph/.20)
    return (co,si,Yl,*t,separation,residual,d,zl,zr)

def warp(x,eta,z,ph,order,mode,side):
    co,si,Yl,tx,ty,tz,b,*_=pose(ph,order,mode)
    Y,Z,cb,sb=prior.bent(z,prior.smooth(ph/.90),order)
    dx=x-.30;dy=Y-Yl+eta*cb
    return .30+tx+co*dx+si*dy,ty+side*(B+b)-si*dx+co*dy,tz+Z-eta*sb

def components(chart,a,b,ph,order,mode):
    s,v=inputs(chart,a,b);side=1 if chart.endswith("+") else -1
    if chart=="cylinder":
        raw=c.chart_jet(chart,a,b,ph,order,"left",False)
        rr=prior.rawparts(raw);delta=central_shift(s,v,ph,order,mode)
        return tuple(x+y for x,y in zip(rr,delta))
    if chart.startswith("cap"):
        x,z=physical_cap(chart,a,b,order)
        return warp(x,side*crown(x,z),z,ph,order,mode,side)
    p,d=roll_offsets(chart,v,order);q,n=c.section(s,ph,order);q0,n0=old.profile(s,0.,order,True)
    yy=side*(B+p);delta=central_shift(s,yy,ph,order,mode)
    left=(q[0]-d*n[0]+delta[0],yy+delta[1],q[1]-d*n[1]+delta[2])
    x,z=q0[0]-d*n0[0],q0[1]-d*n0[1]
    ptop=base.axial(order)+m.terminal(order)[0]
    right=warp(x,side*(p-ptop),z,ph,order,mode,side)
    u=v+E if chart.startswith("round") else v
    gate=cap_s7((u-.012)/(E+OLD_L-.012))
    return tuple(l+gate*(r-l) for l,r in zip(left,right))

def chart_jet(chart,a,b,phase,order,mode,rotate=False):
    m.old.disk._public();ph=float(phase)
    if mode not in MODES or not 0.<=ph<=.90000000000001:raise ValueError("R780 registered whole field")
    a,b=np.broadcast_arrays(np.asarray(a,float),np.asarray(b,float));sh=a.shape;a,b=a.ravel(),b.ravel()
    pieces=[]
    for i in range(0,len(a),192):
        a1,b1=a[i:i+192],b[i:i+192]
        pieces.append(gather(components(chart,a1,b1,ph,order,mode),len(a1)))
    j=np.concatenate(pieces)
    if rotate:
        ax=np.asarray(m.axis(order));p=j[:,:,[0,2]].copy();p[:,0]-=ax
        p=c.oldgeom.parent.rot(p,ph);p[:,0]+=ax;j[:,:,0]=p[:,:,0];j[:,:,2]=p[:,:,1]
    return j.reshape(sh+(6,3))

def gate(kind,s,v,order,release=False):
    if release:return base.gate(kind,s,v,order)
    if kind=="cylinder" or kind.startswith("cap"):return J(np.zeros_like(s.v))
    if kind=="preband":return cap_s7(v/.075)
    if kind=="round":return cap_s7((OLD_L-v)/.10)
    raise ValueError(kind)
