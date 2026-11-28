"""R781. Circular three-lobe physical sphere and free two-/three-fold spatial ring jets."""
from functools import lru_cache
from math import factorial
import numpy as np
from r742_tilted_disk_two_jets import J,unary,trig,gather
from r767_negative_track_profile import clock,smooth_curve,ROUND
from r740_rolled_disk_seed import rule
from r767_preloaded_cap_atlas import root

R=.45
P=2*np.pi*R
HALF_WIDTH=.5
RH=.09
SM=.001
L=RH*np.pi/2+SM
Q0=.60
Q1=1.50
ELL=.073
HALF=1/6

def wave(x):
    # Work with local folded half-wave labels. The full world period contains three periods.
    a=np.mod(3*x,1.)
    h=np.minimum(a,1-a)/3
    sg=np.where(a<.5,1.,-1.)
    u,du,ddu=clock(h/ELL);v,dv,ddv=clock((HALF-h)/ELL)
    return sg*u*v,(du*v-u*dv)/ELL,sg*(ddu*v-2*du*dv+u*ddv)/ELL**2

def dq(t):return (Q1-Q0)*np.sin(t)**2

def rates(x,t):
    u=wave(x)[0]
    return np.stack((np.cos((Q0+dq(t))*u),np.sin(Q0*u),
                2*np.sin(dq(t)*u/2)*np.cos((Q0+dq(t)/2)*u)))

@lru_cache(maxsize=192)
def half_table(t,order):
    sh=ELL*ROUND
    k=np.array([0.,sh,ELL-sh,ELL,HALF-ELL,HALF-ELL+sh,HALF-sh,HALF])
    n,w=rule(order);h=np.diff(k)
    rows=(rates(k[:-1,None]+h[:,None]*n,t)@w).T
    return k,np.vstack((np.zeros(3),np.cumsum(h[:,None]*rows,axis=0)))

def axis(x,t,order):
    frac=np.mod(3*x.v,1.)
    z=np.minimum(frac,1-frac)/3
    k,tab=half_table(t,order)
    i=np.clip(np.searchsorted(k,z,side="right")-1,0,len(k)-2);h=z-k[i]
    n,w=rule(order)
    v=tab[i]+h[:,None]*(rates(k[i,None]+h[:,None]*n,t)@w).T
    cum=2*np.floor(3*x.v)*tab[-1,0]+np.where(frac>.5,2*tab[-1,0]-v[:,0],v[:,0])
    wv,wp,wpp=wave(x.v)
    a=dq(t);q=(Q0+a)*wv;cq,sq=np.cos(q),np.sin(q);sm,cm=np.sin(Q0*wv),np.cos(Q0*wv)
    sd=2*np.sin(a*wv/2)*np.cos((Q0+a/2)*wv)
    cd=-2*np.sin(a*wv/2)*np.sin((Q0+a/2)*wv)
    A=unary(x,.5-6*tab[-1,0]+cum,cq,-sq*(Q0+a)*wp)
    z0=unary(x,v[:,1],sm,cm*Q0*wp)
    delta=unary(x,v[:,2],sd,(a*cq+Q0*cd)*wp)
    unit=unary(x,wv,wp,wpp)
    return A,z0,delta,unit

def offset(s,d,order=20):
    c,z=trig(s/R)
    return [(R-d)*c,(R-d)*z]

@lru_cache(maxsize=16)
def end_limits(order=20):
    p,d=smooth_curve(J(np.array([L])),L,RH,SM,order)
    return float(p.v[0]),float(d.v[0])

def disk_world(x,z,order=20):return x,z

def normal_to_disk_material(e,w,order=20):
    db=end_limits(order)[1]
    return e,1-w/(R-db)

@lru_cache(maxsize=192)
def diameter(t,order=20):
    # Exact maximizing point is on the common constant-curvature part of the two head meridians.
    p,d=smooth_curve(J(np.array([SM])),L,RH,SM,order)
    beta=SM/(2*RH)
    axial=3*half_table(float(t),order)[1][-1,0]+float(p.v[0])-RH*np.sin(beta)
    radial=R-float(d.v[0])-RH*np.cos(beta)
    return 2*(RH+np.hypot(axial,radial))

def profile_marks():return list(P*np.arange(12)/12)

def axial_marks():
    h=ELL*ROUND
    a=np.array([0.,h,ELL-h,ELL,HALF-ELL,HALF-ELL+h,HALF-h,HALF])
    return np.unique(np.concatenate([j*HALF+a-.5 for j in range(6)])).tolist()

def series(z,co):
    v=co[-1]
    for a in co[-2::-1]:v=v*z+a
    return v

def amplitude(d,delta,r0,xi):
    coeff=[(-1.)**(j+1)/(4.**j*factorial(j)**2) for j in range(1,16)]
    def fun(h,u):return h*series(h*u,coeff)-1
    lo,hi=np.full(d.v.shape,3.9),np.full(d.v.shape,5.)
    for _ in range(48):
        m=(lo+hi)*.5;pos=fun(m,d.v)>0
        lo,hi=np.where(pos,lo,m),np.where(pos,m,hi)
    hv=.5*(lo+hi);j=fun(J(hv,s=1.),J(d.v,a=1.))
    dx=-j.a/j.s;dxx=-(j.aa+2*j.sa*dx+j.ss*dx*dx)/j.s
    h=unary(d,hv,dx,dxx)
    positive=delta.v>0;r=np.sqrt(np.where(positive,delta.v,1.))
    rd=unary(delta,np.where(positive,r,0.),np.where(positive,.5/r,0.),np.where(positive,-.25/r**3,0.))
    return rd*root(h*(1-xi)/r0),d*h

@lru_cache(maxsize=64)
def bessel_series(j):
    return [(-1.)**k/(2.**(j+2*k)*factorial(k)*factorial(k+j)) for k in range(14)]

def central(e,x,t,order,mode,m,xi,mix):
    A,z0,delta,u=axis(x,t,order)
    th=e/R;ct,st=trig(th);r0=R-z0
    # At all phases the balanced and ring fields share the exact same initial tensor.
    rt=r0-(1-xi)*delta
    xw,zw=rt*ct,rt*st
    if mode!="ring" or mix==0. or t==0.:return [xw,A,zw]
    co,si=trig((Q0+dq(t))*u);co0,si0=trig(Q0*u)
    sz=(1-xi)*si+xi*si0
    speed=root(co*co+sz*sz)
    c,s=co/speed,sz/speed
    d=(1-xi)*delta/r0
    angle,G=amplitude(d,delta,r0,xi)
    power=J(np.ones_like(d.v))
    dx=J(np.zeros_like(d.v));dz=J(np.zeros_like(d.v));dy=J(np.zeros_like(d.v))
    for j in range(1,17):
        power=power*angle
        Jj=power*series(G,bessel_series(j))
        k=j*m
        cp,sp=trig((1+k)*th);cm,sm=trig((1-k)*th)
        if j%2:
            dx=dx-c*Jj*(cp/(1+k)-cm/(1-k))
            dz=dz-c*Jj*(sp/(1+k)-sm/(1-k))
            # The section-centered periodic lift has a nonnegative physical axial correction.
            dy=dy+2*Jj*(1-s*trig(k*th)[0])/k
        else:
            dx=dx+Jj*(cp/(1+k)+cm/(1-k))
            dz=dz+Jj*(sp/(1+k)+sm/(1-k))
    return [xw+mix*r0*dx,A+mix*r0*dy,zw+mix*r0*dz]

def chart_jet(chart,u,v,phase=0.,order=20,mode="short",m=2,xi=0.,mix=1.):
    if mode not in ("short","balanced","ring") or not (0<=xi<=.06 and 0<=mix<=1):
        raise ValueError("invalid R781 physical design")
    if mode=="short":xi=0.
    if mode=="ring" and (int(m)!=m or m not in (2,3)):raise ValueError("m must be two or three")
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float))
    e=J(aa.ravel(),s=1.);v=J(bb.ravel(),a=1.);t=float(phase)
    if chart=="cylinder":coords=central(e,v+.5,t,order,mode,int(m),xi,mix)
    else:
        sg=1 if chart.endswith("+") else -1
        y=.5 if sg>0 else .5-6*half_table(t,order)[1][-1,0]
        if chart.startswith("end"):
            p,d=smooth_curve(v,L,RH,SM,order);u,w=offset(e,d,order)
            coords=[u,y+sg*p,w]
        elif chart.startswith("cap"):
            p,d=end_limits(order)
            if "cartesian" in chart:u,w=e,v
            elif "normal" in chart:u,w=offset(e,d+v,order)
            else:u,w=offset(e,d,order);u,w=v*u,v*w
            coords=[u,J(np.full_like(e.v,y+sg*p)),w]
        else:raise ValueError(chart)
    return gather(coords,len(e.v)).reshape(aa.shape+(6,3))
