#!/usr/bin/env python3
"""R787 physical two-jet on one new preloaded metric: both complete crowns and four conjugate meridian panels."""
from functools import lru_cache
import numpy as np
import r780_exact_bent_caps_and_closed_spatially_shifted_center as old
import r787_long_left_wall_and_complete_initial_disks as wall
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

m=old.m
B,E,L,T,OLD_L=old.B,old.E,old.L,old.T,old.OLD_L
H=.71
EPS=2.**-16
CUT=(-1.34,-1.29,-1.095,-1.045)
MAXDELTA=np.arccos(.25)
FIRST=.132
NEG=.93
EDGE=.001
RANGES=(0.,EDGE,FIRST-EDGE,FIRST,FIRST+EDGE,E-EDGE,E,E+m.END_E,E+OLD_L-m.END_E,E+OLD_L,T)

def smooth5(z):
    t=np.clip(z,0.,1.)
    return t**3*(10+t*(-15+6*t))

def softened(x,length,ramp,angle):
    q=np.clip(np.minimum(x,length-x)/ramp,0.,1.)
    return m.old.disk.softened_angle(x,length,ramp,angle/(length-ramp)),angle/(length-ramp)*smooth5(q)

def axial_clock(ph):
    d=MAXDELTA*old.prior.smooth(ph/.90)
    return float(d),float(np.cos(d)),float(np.sin(d))

def slope(x):
    return EPS*cap_s7((x-CUT[0])/(CUT[1]-CUT[0]))*cap_s7((CUT[3]-x)/(CUT[3]-CUT[2]))

def sqrtj(q):
    x=np.sqrt(q.v)
    return unary(q,x,.5/x,-.25/x**3)

def integrate(x,cuts,fn,order):
    # Vector-valued displayed primitive; true knots are always included.
    x=np.asarray(x);sh=x.shape;u,iv=np.unique(x,return_inverse=True);nodes,wt=m.old.disk.rule(order)
    z=np.zeros((len(u),2))
    for a,b in zip(cuts[:-1],cuts[1:]):
        w=np.clip(u-a,0.,b-a)
        f=fn(a+w[:,None]*nodes)
        z+=w[:,None]*np.einsum("iqk,q->ik",f,wt)
    return z[iv].reshape(sh+(2,))

def profile(x,ph,order):
    _,c,_=axial_clock(ph)
    h=slope(x)*(1/c);k=sqrtj(1-h*h)
    def vec(xv):
        w=slope(J(xv)).v/c
        return np.stack((w*w/(1+np.sqrt(1-w*w)),w),axis=-1)
    v=integrate(x.v,CUT,vec,order);whole=profile_total(ph,order)
    # Fixed right end. The exact left continuation is a single translation.
    X=unary(x,x.v+whole[0]-v[...,0],k.v,-h.v*(slope(J(x.v,s=1.)).s/c)/k.v)
    Z=unary(x,v[...,1]-whole[1],h.v,slope(J(x.v,s=1.)).s/c)
    return X,Z,h,k

@lru_cache(maxsize=256)
def profile_total(ph,order):
    _,c,_=axial_clock(ph)
    def val(xv):
        w=slope(J(xv)).v/c
        return np.stack((w*w/(1+np.sqrt(1-w*w)),w),axis=-1)
    return integrate(np.asarray(CUT[-1]),CUT,val,order)

def angles(u,ph):
    delta,c,s=axial_clock(ph);u=np.asarray(u);v=np.clip(u,0.,E)
    w=np.pi*v/E;pre=.0025*np.sin(2*w)*np.sin(w)**2
    preder=.0025*np.pi/E*(2*np.cos(2*w)*np.sin(w)**2+np.sin(2*w)**2)
    root,rd=softened(u-E,OLD_L,m.END_E,np.pi/2)
    a=np.where(u<E,pre,root);ap=np.where(u<E,preder,rd)
    a=np.where(u>=E+OLD_L,np.pi/2,a)
    ca=np.cos(a);sa=np.sin(a);ca=np.where(u>=E+OLD_L,0.,ca);sa=np.where(u>=E+OLD_L,1.,sa)
    z=c*sa;y=np.hypot(ca,s*sa)
    if not ph:g=a;gp=ap
    else:
        g=np.arctan2(z,y);gp=np.divide(c*ca*ap,y,out=np.zeros_like(a,dtype=float),where=y>0)
    down,dp=softened(v,FIRST,EDGE,-NEG);back,bp=softened(v-FIRST,E-FIRST,EDGE,MAXDELTA+NEG)
    t=delta/MAXDELTA
    return g,gp,a+t*(down+back),ap+t*(dp+bp)

def meridians(u,ph,order):
    def val(v):
        ag,_,ab,_=angles(v,ph)
        return (np.stack((np.cos(ag),np.sin(ag)),axis=-1),np.stack((np.cos(ab),np.sin(ab)),axis=-1))
    def compute(index):
        return integrate(u.v,RANGES,lambda v:val(v)[index],order)
    vg,vb=compute(0),compute(1);ag,ap,ab,bp=angles(u.v,ph)
    return tuple(t for v,a,k in ((vg,ag,ap),(vb,ab,bp)) for t in (
        unary(u,v[...,0],np.cos(a),-k*np.sin(a)),unary(u,v[...,1],np.sin(a),k*np.cos(a))))

@lru_cache(maxsize=256)
def pose(ph,order):
    _,c,s=axial_clock(ph);pg,dg,pb,db=(float(f.v) for f in meridians(J(np.asarray(T)),ph,order))
    dt=m.terminal(order)[1]+old.LIP;zl=H-dt
    return pg,dg,pb,db,2*s*zl+pg-pb,2*H*(1-c)+dg-db,zl

def lower_weight(z):
    k=1/(1.38-.04);a,ap=softened(z.v+.69,1.38,.04,1.)
    t=z.v+.69;q=np.clip(np.minimum(t,1.38-t)/.04,0.,1.)
    dd=k*30*q*q*(1-q)**2*np.where(t<.69,1.,-1.)/.04
    return 1-unary(z,a,ap,dd)

BEND_START=.65
BEND_LENGTH=.25
BEND_RAMP=.005

def cap_curve(z,ph,order):
    delta,c,s=axial_clock(ph);a=np.abs(z.v);sg=np.sign(z.v)
    clock,rate=softened(a-BEND_START,BEND_LENGTH,BEND_RAMP,1.)
    beta=-delta*(1-clock);kp=delta*rate*sg
    def value(w):
        b=-delta*(1-softened(w-BEND_START,BEND_LENGTH,BEND_RAMP,1.)[0])
        return np.stack((np.sin(b),np.cos(b)),axis=-1)
    top=BEND_START+BEND_LENGTH
    base=integrate(a,(0.,BEND_START,BEND_START+BEND_RAMP,top-BEND_RAMP,top),value,order)
    yy=sg*base[...,0];zz=sg*(base[...,1]+np.maximum(a-top,0.))
    si,co=np.sin(beta),np.cos(beta)
    return unary(z,yy,si,co*kp),unary(z,zz,co,-si*kp)

def cap_fields(x,z,side,ph,order):
    X,G,h,k=profile(x,ph,order)
    d,c,s=axial_clock(ph);pg,dg,pb,db,dy,dz,zl=pose(ph,order)
    by=(B+pg+s*zl) if side==1 else (-B-pb+s*zl)
    bz=H*(1-c)-(db-dg if side==-1 else 0.)
    f=side*old.crown(x,z);den=sqrtj(1-slope(x)*slope(x))
    Y,Z=cap_curve(z,ph,order)
    return X-s*h*f/den,by+Y+c*k*f/den,G+Z+bz+s*k*f/den

def compose(chart,a,b,ph,order):
    side=1 if chart.endswith("+") else -1
    sj,v=old.inputs(chart,a,b);_,c,s=axial_clock(ph)
    pg,dg,pb,db,dy,dz,zl=pose(ph,order)
    if chart=="cylinder":
        xx,yy,zz=wall.central(chart,a,b,order);X,G,_,_=profile(xx,ph,order);lo=lower_weight(zz)
        return X,yy+dy*lo,G+zz+dz*lo
    if chart.startswith("cap"):
        x,z=wall.cap_projection(chart,a,b,order)
        return cap_fields(x,z,side,ph,order)
    u=v+E if chart.startswith("round") else v
    q,n=wall.parts(sj,order);qx,qz=q;nx,nz=n
    _,d0=old.roll_offsets(chart,v,order)
    w=(1-side*nz)*.5;lo=lower_weight(qz)
    pg0,dg0,pb0,db0=meridians(u,ph,order)
    pu=pg0+w*(pb0-pg0);du=dg0+w*(db0-dg0);pickup=cap_s7(u/.10)
    dt=m.terminal(order)[1]+old.LIP
    by=(B+pg+s*zl) if side==1 else (-B-pb+s*zl)
    bz=H*(1-c)-(db-dg if side==-1 else 0.)
    corrY=by-s*(qz-dt*nz)-side*(B+pg+w*(pb-pg))-dy*lo
    corrZ=(c-1)*qz+bz-dz*lo+w*(db-dg)*nz
    X,G,_,_=profile(qx-d0*nx,ph,order)
    zr=qz-dt*nz;zc=qz-d0*nz;Yc,Zc=cap_curve(zc,ph,order)
    price=cap_s7((zr*zr-.576**2)/(.65**2-.576**2))*cap_s7((u-(E+OLD_L-.09))/.09)
    return X,side*(B+pu)+dy*lo+pickup*corrY+price*(Yc+s*zc),G+qz-du*nz+dz*lo+pickup*corrZ+price*(Zc-c*zc)

def chart_jet(chart,a,b,phase,order,mode=None,rotate=False):
    # The physical upper-right marked grip is stationary; the raw world is the final world.
    m.old.disk._public()
    if not 0<=phase<=.90000000000001:raise ValueError("registered R787 time interval")
    a,b=np.broadcast_arrays(np.asarray(a,float),np.asarray(b,float));shape=a.shape;a,b=a.ravel(),b.ravel()
    pieces=[]
    for start in range(0,len(a),192):
        x,y=a[start:start+192],b[start:start+192]
        pieces.append(gather(compose(chart,x,y,float(phase),order),len(x)))
    return np.concatenate(pieces).reshape(shape+(6,3))
