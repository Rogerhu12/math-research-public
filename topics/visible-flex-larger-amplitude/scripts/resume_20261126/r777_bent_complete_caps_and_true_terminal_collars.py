#!/usr/bin/env python3
"""R777 bent complete original caps, their exact common ambient seam jets and full free roll seeds."""
from functools import lru_cache
import numpy as np
import r774_common_left_body_and_complete_caps as c
from r742_tilted_disk_two_jets import J,unary,cap_s7,trig,gather

base,old,m=c.base,c.old,c.m
E,L,B,T=c.E,c.L,c.B,c.T
PLATE=.58
RISE=.245
RAMP=.015
RETAIN=2.**-12
EDGE=.00013
MODES=("pair","balanced")

def smooth(x):
    x=np.clip(x,0.,1.)
    return x**3*(10-15*x+6*x*x)

def clocks(ph):
    return 1-(1-RETAIN)*smooth(ph/.075),smooth((ph-.075)/.825)

def angular(r,k):
    # Actual physical signed angles. The derivative is with respect to the true z coordinate.
    r=np.asarray(r,float);a=np.abs(r);sg=np.sign(r)
    speed=np.pi/(2*(RISE-RAMP))
    def stroke(x):
        angle=m.old.disk.softened_angle(x,RISE,RAMP,speed)
        d=np.clip(np.minimum(x,RISE-x)/RAMP,0.,1.)
        return angle,speed*m.old.disk.s5(d),speed*30*(d*(1-d))**2*np.where(x<RISE/2,1.,-1.)/RAMP
    be,bp,bpp=stroke(a);fall,fp,fpp=stroke(a-PLATE)
    return -k*sg*(be-fall),-k*(bp-fp),-k*sg*(bpp-fpp)

def bent(z,k,order):
    # Y is even, Z is odd, and the end straight tails have unlimited analytic continuation.
    cuts=(0.,RAMP,RISE-RAMP,RISE,PLATE,PLATE+RAMP,PLATE+RISE-RAMP,PLATE+RISE)
    v=np.asarray(z.v);r=np.abs(v)
    cz,sy=m.old.disk.integrals(np.minimum(r,cuts[-1]),cuts,lambda a:angular(a,k)[0],order)
    sy=sy+np.zeros_like(v);cz=np.sign(v)*(cz+np.maximum(0.,r-cuts[-1]))
    a,ap,app=angular(v,k);co,si=np.cos(a),np.sin(a)
    return (unary(z,sy,si,ap*co),unary(z,cz,co,-ap*si),
            unary(z,co,-ap*si,-app*si-ap*ap*co),unary(z,si,ap*co,app*co-ap*ap*si))

@lru_cache(maxsize=128)
def wall_label(order):
    return old.material(order,True)[0]+sum(old.clock_spec(True)[0][1][:2])

def centerdata(order,ph):
    w=wall_label(order);qo=old.data(np.asarray([w]),0.,order,True)[0][0]
    tr=c.state(order,ph)[3] if ph else np.zeros(2)
    q=c.curve(np.asarray([w]),ph,order)[0][0]-tr
    return qo,q,tr

def positive_floor(x):
    # A smooth maximum with .10; all registered phases have the same cap separation lower bound.
    return .10+np.logaddexp(0.,60*(x-.10))/60

def translation_center(delta):
    # Strongly convex log-sum-exp of the full set of sampled true squared meridian chords.
    # Hessian = 2I + 4m covariance of their horizontal/axial residual vectors.
    mexp=48.;p=-np.mean(delta[:,:2],axis=0)
    def calculate(q):
        r=delta[:,:2]+q
        y=np.sum(r*r,axis=1)+delta[:,2]**2;top=np.max(y)
        w=np.exp(mexp*(y-top));total=np.sum(w);w/=total
        center=w@r;r0=r-center
        return top+np.log(total/len(y))/mexp,2*center,2*np.eye(2)+4*mexp*(r0.T@(w[:,None]*r0))
    for _ in range(36):
        loss,g,H=calculate(p)
        if np.linalg.norm(g)<1e-12:break
        d=np.linalg.solve(H,g);a=1.
        for _ in range(22):
            if calculate(p-a*d)[0]<=loss-.0001*a*(g@d):break
            a*=.5
        p-=a*d
    return p,calculate(p)[1]

@lru_cache(maxsize=256)
def pose(order,ph,mode):
    if mode not in MODES:raise ValueError("unregistered R777 complete cap")
    _,k=clocks(ph);pb,db=m.terminal(order);b0=base.axial(order)+pb
    oldr,newr,tr=centerdata(order,ph)
    zl=.71-db;zr=oldr[1];dx=oldr[0]-db-.30
    Y,Z,_,_=bent(J(np.asarray([zl,zr])),k,order)
    delta=Y.v[1]-Y.v[0];span=np.hypot(dx,delta)
    co,si=dx/span,delta/span
    C,Bend=.30,b0;res=np.zeros(2)
    if ph:
        t=smooth(ph/.35);b=(1-t)*b0+t*.105
        l=np.sqrt(1.30**2+T*T-b*b-(.71-Z.v[0])**2)
        r=np.sqrt(T*T-b*b-(newr[1]-Z.v[1])**2)
        x=.5*((-1+l)+(newr[0]-r-span))
        if mode=="balanced":
            grid=c.stations(order);half=old.material(order,True)[-1]
            s=np.unique(np.r_[grid,2*half-grid,np.arange(512)*2*half/512])
            qo,_,no,*_=old.data(s,0.,order,True)
            qc=c.curve(s,ph,order)[0]-tr
            rim=qo-db*no;yy,zz,_,_=bent(J(rim[:,1]),k,order)
            rx=rim[:,0]-.30;ry=yy.v-Y.v[0]
            pts=np.column_stack((co*rx+si*ry-qc[:,0],-si*rx+co*ry,zz.v-qc[:,1]))
            P,res=translation_center(pts);x,b=P[0],positive_floor(P[1])
        mix=smooth(ph/.20);C=(1-mix)*.30+mix*x;Bend=(1-mix)*b0+mix*b
    return [co,si,Y.v[0],C,Bend,tr[0],tr[1],span,dx,zl,zr,Z.v[0],Z.v[1],
            newr[0],newr[1],float(np.linalg.norm(res)),float(k)]

def warp(x,eta,z,order,ph,mode):
    co,si,Yl,C,b,tx,tz,*_=pose(order,ph,mode)
    _,k=clocks(ph);Y,Z,v,w=bent(z,k,order)
    A=x-.30;V=Y-Yl+eta*v
    return C+tx+co*A+si*V,B+b-si*A+co*V,tz+Z-eta*w

def rawparts(j):
    return tuple(J(*j[:,:,i].T) for i in range(3))

def block(chart,a,b,ph,order,mode):
    raw=base.chart_jet(chart,a,b,0.,order,.14,False)
    if not ph:return raw
    if chart=="cylinder":
        return c.chart_jet(chart,a,b,ph,order,"left",False)
    side=1 if chart.endswith("+") else -1
    x,y,z=rawparts(raw);y0=B+base.axial(order)+m.terminal(order)[0]
    if chart.startswith("cap"):
        scale,_=clocks(ph)
        xx,yy,zz=warp(x,scale*(side*y-y0),z,order,ph,mode)
        return gather((xx,side*yy,zz),len(a))
    s=J(a,s=1.);v=J(b,a=1.);roundpart=chart.startswith("round")
    u=v+E if roundpart else v
    qo,no=c.section(s,ph,order)
    if roundpart:
        p,d=m.end(v,order);p=p+base.axial(order)
    else:
        p,d=base.initial_turn(v,order)
    left=(qo[0]-d*no[0],B+p,qo[1]-d*no[1])
    right=warp(x,side*y-y0,z,order,ph,mode)
    # The entire shared final open collar is the same ambient image as the cap rim.
    h=cap_s7((u-.012)/(T-EDGE-.012))
    f=tuple(l+h*(r-l) for l,r in zip(left,right))
    return gather((f[0],side*f[1],f[2]),len(a))

def gate(kind,s,v,order,free=False):
    original=base.gate(kind,s,v,order)
    if free or kind=="cylinder" or kind=="preband":return original
    if kind=="round":return original*cap_s7((L-EDGE-v)/.095)
    return J(np.zeros_like(s.v))

def chart_jet(chart,a,b,ph,order,mode,rotate=False):
    m.old.disk._public()
    if not 0<=ph<=.90000000000001 or mode not in MODES:raise ValueError("registered R777 material field")
    a,b=np.broadcast_arrays(np.asarray(a,float),np.asarray(b,float));sh=a.shape;a,b=a.ravel(),b.ravel()
    j=np.concatenate([block(chart,a[i:i+192],b[i:i+192],float(ph),order,mode) for i in range(0,len(a),192)])
    if rotate:
        axis=np.asarray(m.axis(order));q=j[:,:,[0,2]].copy();q[:,0]-=axis
        q=c.oldgeom.parent.rot(q,ph);q[:,0]+=axis;j[:,:,0]=q[:,:,0];j[:,:,2]=q[:,:,1]
    return j.reshape(sh+(6,3))
