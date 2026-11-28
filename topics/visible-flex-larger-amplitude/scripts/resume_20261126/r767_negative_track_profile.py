"""R767 unit-speed closed planar profile, two negative preloaded tracks and two fixed-shape heads."""
from functools import lru_cache
import numpy as np
import r740_rolled_disk_seed as old
from r742_tilted_disk_two_jets import J,unary,trig
A=.08
B=.88
DELTA=.01
TRACK=1.
RAMP=.13
ROUND=.06
ANGLE=.78
HEAD_R=.23
HEAD_BLEND=.001
HEAD_TURN=np.pi+A+B
HEAD_L=HEAD_R*HEAD_TURN+HEAD_BLEND
P=2*(1+HEAD_L)
CANT=(B-A)/2
E=np.array([np.cos(CANT),np.sin(CANT)])
N=np.array([-E[1],E[0]])

def clock(x):
    t=np.clip(x,0.,1.);d=ROUND
    # Integrate a smoothed unit-plateau speed at both endpoints. Reflection
    # gives the right piece without subtracting high-order polynomials.
    val=np.where(t<d,d*old.i5(t/d),
          np.where(t<=1-d,t-d/2,1-d-d*old.i5((1-t)/d)))/(1-d)
    s=np.clip(np.minimum(t,1-t)/d,0,1)
    der=old.s5(s)/(1-d);d2=30*s**2*(1-s)**2*np.where(t<.5,1.,-1.)/((1-d)*d)
    return val,der,d2

def heading(x,theta):
    h,hp,hpp=clock(x/RAMP);k,kp,kpp=clock((x-1+RAMP)/RAMP)
    a=A-DELTA+theta;b=B-DELTA-theta
    y=-A+2*DELTA*(x-np.sin(2*np.pi*x)/(2*np.pi))+a*h+b*k
    dy=2*DELTA*(1-np.cos(2*np.pi*x))+(a*hp+b*kp)/RAMP
    d2=4*np.pi*DELTA*np.sin(2*np.pi*x)+(a*hpp+b*kpp)/RAMP**2
    return y,dy,d2

def head_angle(x):
    z=old.softened_angle(x,HEAD_L,HEAD_BLEND,1/HEAD_R)
    b=np.clip(np.minimum(x,HEAD_L-x)/HEAD_BLEND,0,1)
    k=old.s5(b)/HEAD_R
    dk=30*b*b*(1-b)**2*np.where(x<HEAD_L/2,1.,-1.)/(HEAD_R*HEAD_BLEND)
    return B-z,-k,-dk

def quad_angle(x,cuts,fn,order):
    return np.stack(old.integrals(x,cuts,fn,order),axis=-1)

@lru_cache(maxsize=320)
def track_integrator(theta,order):
    knots=np.unique(np.r_[0,RAMP*ROUND,RAMP*(1-ROUND),RAMP,.5,
                       1-RAMP,1-RAMP*(1-ROUND),1-RAMP*ROUND,1.])
    n,w=old.rule(order);d=np.diff(knots)
    ang=heading(knots[:-1,None]+d[:,None]*n,theta)[0]
    vals=np.c_[np.cos(ang)@w,np.sin(ang)@w]
    return knots,np.vstack((np.zeros(2),np.cumsum(d[:,None]*vals,axis=0)))

def track(x,theta,order):
    knots,tab=track_integrator(theta,order);i=np.clip(np.searchsorted(knots,x,side="right")-1,0,len(knots)-2)
    d=x-knots[i];n,w=old.rule(order);ang=heading(knots[i,None]+d[:,None]*n,theta)[0]
    return tab[i]+d[:,None]*np.c_[np.cos(ang)@w,np.sin(ang)@w]

def head(x,order):
    return quad_angle(x,(0.,HEAD_BLEND,HEAD_L-HEAD_BLEND,HEAD_L),
                    lambda q:head_angle(q)[0],order)

@lru_cache(maxsize=24)
def head_half(order):return -.5*head(np.array([HEAD_L]),order)[0]

def coordinates(s,theta=0.,order=32):
    sh=np.shape(s);u,inv=np.unique(np.mod(s,P),return_inverse=True);left=head_half(order)
    Jtot=track_integrator(theta,order)[1][-1]
    Q=np.zeros((len(u),2));ang=np.zeros(len(u));d=ang.copy();d2=ang.copy()
    knots=[0.,1.,1+HEAD_L,2+HEAD_L,P]
    for i,(l,r) in enumerate(zip(knots[:-1],knots[1:])):
        take=(u>=l)&(u<r);x=u[take]-l
        if not len(x):continue
        if i%2==0:
            a,k,kp=heading(x,theta);q=track(x,theta,order)
            Q[take]=left-Jtot+q if not i else -left-q
        else:
            a,k,kp=head_angle(x);q=head(x,order)
            Q[take]=left+q if i==1 else -left-Jtot-q
        ang[take]=a+(np.pi if i>=2 else 0.);d[take]=k;d2[take]=kp
    T=np.stack((np.cos(ang),np.sin(ang)),axis=-1);n=np.stack((-T[:,1],T[:,0]),axis=-1)
    def out(v):return v[inv].reshape(sh+v.shape[1:])
    return tuple(out(v) for v in (Q,T,n,-d,-d2))

def section(s,theta=0.,order=32):
    q,t,n,k,kp=coordinates(s.v,theta,order)
    point=[unary(s,q[...,i],t[...,i],-k*n[...,i]) for i in range(2)]
    normal=[unary(s,n[...,i],k*t[...,i],kp*t[...,i]-k*k*n[...,i]) for i in range(2)]
    tang=[unary(s,t[...,i],-k*n[...,i],-kp*n[...,i]-k*k*t[...,i]) for i in range(2)]
    return point,normal,tang

def smooth_curve(v,L,r,e,order):
    alpha=old.softened_angle(v.v,L,e,1/r)
    b=np.clip(np.minimum(v.v,L-v.v)/e,0,1)
    k=old.s5(b)/r
    co,si=old.integrals(v.v,(0.,e,L-e,L),lambda z:old.softened_angle(z,L,e,1/r),order)
    return unary(v,co,np.cos(alpha),-k*np.sin(alpha)),unary(v,si,np.sin(alpha),k*np.cos(alpha))
