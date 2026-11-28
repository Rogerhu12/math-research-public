"""Nonplanar unit-speed transverse deformation of the R772 material sphere.
The four true horizontal seam endpoints, both developed disks and rounded heads share their R772 positions up to the new axial motion.
"""
from functools import lru_cache
import numpy as np
import r772_coherent_developing_tube as g
from r742_tilted_disk_two_jets import J,unary,trig,gather,cap_s7
from r767_preloaded_cap_atlas import root
P=g.P
L=g.L
HALF_WIDTH=g.HALF_WIDTH
SIDE=.06
RATIO=96.
LIFT=.001
profile_marks=g.profile_marks
axial_marks=g.axial_marks
offset=g.offset
disk_world=g.disk_world
end_limits=g.end_limits
normal_to_disk_material=g.normal_to_disk_material

def ctrl(x,t):
    return (1-1/RATIO)*np.sin(t)**2*cap_s7(x/SIDE)*cap_s7((1-x)/SIDE)

def heading0(x):
    q,k=g.rate(x.v,0.)
    return unary(x,np.sin(q),np.cos(q)*k,
                 rate2(x.v)*np.cos(q)-np.sin(q)*k*k)

def rate2(x):
    y,yp,ypp=g.guard.clock(x);tt=2*np.pi*y;h=np.sin(tt);c=np.cos(tt)
    hp=2*np.pi*c*yp;hpp=2*np.pi*c*ypp-h*(2*np.pi*yp)**2
    z=g.X0*h*(1.5-.5*h*h)
    zp=g.X0*1.5*(1-h*h)*hp;zpp=g.X0*(1.5*(1-h*h)*hpp-3*h*hp*hp)
    return zpp/(1+z*z)-2*z*zp*zp/(1+z*z)**2

def tangent(s):
    v=np.mod(s.v,P);b=np.floor(v/g.BLOCK).astype(int);u=v-b*g.BLOCK
    d=np.clip(u-g.FLAT,0.,g.QUARTER)
    th=np.pi*b/2+g.softened_angle(d,g.QUARTER,g.SM,1/g.R)
    z=np.clip(np.minimum(d,g.QUARTER-d)/g.SM,0.,1.)
    k=g.s5(z)/g.R
    kp=30*z*z*(1-z)*(1-z)*np.where(d<g.QUARTER/2,1.,-1.)/(g.SM*g.R)
    C,H=trig(unary(s,th,k,kp))
    return C,-H

def windows(h):
    z=h*h
    def step(a,b):return cap_s7((z-a*a)/(b*b-a*a))
    return 1-step(.16,.26),step(.32,.42)*(1-step(.68,.78))

@lru_cache(maxsize=32)
def cuts(order):
    # All four mask break angles occur strictly on the constant-curvature subarc.
    alpha=g.softened_angle(np.array([g.SM]),g.QUARTER,g.SM,1/g.R)[0]
    arc=[g.SM+g.R*(np.arcsin(z)-alpha) for z in (.16,.26,.32,.42,.68,.78)]
    arc+=list(g.QUARTER-np.array(arc))
    u=np.unique(np.r_[0.,g.FLAT,g.FLAT+g.SM,g.FLAT+np.array(arc),g.BLOCK-g.SM,g.BLOCK])
    return np.unique(np.concatenate([i*g.BLOCK+u for i in range(4)]))

@lru_cache(maxsize=32)
def compensation(order):
    n,w=g.rule(order);a=cuts(order);a=a[a<=g.BLOCK+1.e-12];d=np.diff(a)
    uu=a[:-1,None]+d[:,None]*n;C,h=tangent(J(uu))
    paid,extra=windows(h)
    return (d@((abs(h.v)*paid.v)@w))/(d@((abs(h.v)*extra.v)@w))

def corrected(s,p,order):
    c,h=tangent(s);paid,extra=windows(h)
    h1=h*(1+p*(compensation(order)*extra-paid));y=LIFT*p*extra*c
    den=c*c
    safe=J(*(np.where(den.v>.31,v if i else den.v,0. if i else 1.) for i,v in enumerate(den.parts())))
    # Unchanged for |h|>=.78, covering every zero and sign reversal of c.
    f=c*root(1+(h*h-h1*h1-y*y)/safe)
    return [f-c,y,h1-h]

def axial_speed(x,t):
    p=ctrl(x,t);h=heading0(x)/(1-p)
    return root(1-h*h),h

@lru_cache(maxsize=160)
def axis_table(t,order):
    k=np.array([0.,.015,.03,.045,.06,.265,.5,.735,.94,.955,.97,.985,1.])
    n,w=g.rule(order);d=np.diff(k);v=k[:-1,None]+d[:,None]*n
    c,h=axial_speed(J(v),t)
    return k,np.vstack((np.zeros(2),np.cumsum(d[:,None]*np.c_[c.v@w,h.v@w],axis=0)))

def axis(x,t,order):
    k,tab=axis_table(t,order);i=np.clip(np.searchsorted(k,x.v,side="right")-1,0,len(k)-2)
    d=x.v-k[i];n,w=g.rule(order)
    c,h=axial_speed(J(k[i,None]+d[:,None]*n),t)
    q=tab[i]+d[:,None]*np.c_[c.v@w,h.v@w]
    c,h=axial_speed(J(x.v,s=1.),t)
    return unary(x,.5-tab[-1,0]+q[:,0],c.v,c.s),unary(x,q[:,1],h.v,h.s)

def ring(s,p,order):
    # Counterpart of the integral definition with a split material primitive;
    # chain the upper-limit and p derivatives as actual two-variable jets.
    c,_=g.section(s,order);n,w=g.rule(order);kn=cuts(order)
    uq=np.mod(s.v,P);shape=uq.shape
    sums=np.zeros((3,3,len(uq)))
    unique,inv=np.unique(p.v,return_inverse=True);k=np.diff(kn)
    v=J((kn[:-1,None]+k[:,None]*n).ravel());pp=J(unique[:,None],s=1.)
    delta=corrected(v,pp,order);idx=np.clip(np.searchsorted(kn,uq,side="right")-1,0,len(k)-1)
    for i,z in enumerate(delta):
        for j,part in enumerate((z.v,z.s,z.ss)):
            arr=np.broadcast_to(part,(len(unique),len(k)*order)).reshape(len(unique),len(k),order)
            tab=np.concatenate((np.zeros((len(unique),1)),np.cumsum(k*(arr@w),axis=1)),axis=1)
            sums[i,j]=tab[inv,idx]
    d=uq-kn[idx];v=J(kn[idx,None]+d[:,None]*n);pp=J(p.v[:,None],s=1.)
    dV=corrected(v,pp,order);edge=corrected(J(uq,s=1.),J(p.v,a=1.),order)
    ans=[]
    for i,(z,h) in enumerate(zip(dV,edge)):
        for j,part in enumerate((z.v,z.s,z.ss)):
            sums[i,j]+=d*(np.broadcast_to(part,v.v.shape)@w)
        val,fp,fpp=sums[i]
        # here s is transverse and p is a function of axial coordinate only
        q=J(val,h.v,fp*p.a,h.s,h.a*p.a,fpp*p.a*p.a+fp*p.aa)
        ans.append(q+(c[0] if i==0 else c[1] if i==2 else 0.))
    return ans

def chart_jet(chart,u,v,phase=0.,order=20):
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    t=float(phase)
    if not t:return g.chart_jet(chart,aa,bb,0.,order)
    if chart!="cylinder":
        f=g.chart_jet(chart,aa,bb,0.,order)
        if chart.endswith("-"):f[...,0,1]+=g.path_table(0.,order)[1][-1,0]-axis_table(t,order)[1][-1,0]
        return f
    s=J(aa.ravel(),s=1.);x=J(bb.ravel()+.5,a=1.)
    a,z=axis(x,t,order)
    out=np.empty((len(s.v),6,3))
    for j in range(0,len(s.v),128):
        ix=slice(j,j+128);ee=J(s.v[ix],s=1.);xx=J(x.v[ix],a=1.)
        delta=ring(ee,ctrl(xx,t),order)
        def sub(q):return J(*(np.broadcast_to(k,x.v.shape)[ix] for k in q.parts()))
        out[ix]=gather((delta[0],sub(a)+delta[1],sub(z)+delta[2]),len(ee.v))
    return out.reshape(sh+(6,3))
