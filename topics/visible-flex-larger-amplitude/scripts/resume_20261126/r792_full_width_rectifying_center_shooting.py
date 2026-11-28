#!/usr/bin/env python3
"""Run 55. Rectifying strips on both full nonplanar central arcs of the fixed R787 sphere."""
from functools import lru_cache
import numpy as np
from scipy.interpolate import BSpline,BPoly
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation
import r787_preloaded_two_complete_caps_and_four_returning_meridians as g
from r742_tilted_disk_two_jets import J,unary,cap_s7

Y=np.array([0.,1.,0.])
I=np.eye(3)
def map3(x):return np.column_stack(x)
def unit(x):return x/np.linalg.norm(x,axis=-1,keepdims=True)
def cross_matrix(w):
    a,b,c=w.T;z=np.zeros_like(a)
    return np.stack((z,-c,b,c,z,-a,-b,a,z),axis=-1).reshape(-1,3,3)
def left_jac(w):
    z=np.linalg.norm(w,axis=1);a=np.empty_like(z);b=np.empty_like(z);small=z<.001
    x=z[small]**2;a[small]=.5-x/24+x*x/720;b[small]=1/6-x/120+x*x/5040
    q=z[~small];a[~small]=2*(np.sin(q/2)/q)**2;b[~small]=(q-np.sin(q))/q**3
    h=cross_matrix(w)
    return I+a[:,None,None]*h+b[:,None,None]*(h@h)

def reference(s,o):
    arr=np.asarray(s);sh=arr.shape
    if arr.size>768:
        p=arr.ravel();return np.concatenate([reference(p[i:i+768],o) for i in range(0,len(p),768)]).reshape(sh+(3,3))
    q,_=g.wall.parts(J(arr.ravel(),s=1.),o);x,z=g.profile(q[0],0.,o)[:2];z=z+q[1]
    return np.stack([map3((getattr(x,k),np.zeros_like(x.v),getattr(z,k))) for k in ("v","s","ss")],axis=1).reshape(sh+(3,3))

@lru_cache(maxsize=24)
def domain(o):
    P=2*g.old.old.material(o,True)[-1]
    hi=float(g.m.flat_material_s(np.array([.30]),order=o)[0])
    lo=float(g.m.flat_material_s(np.array([-1.]),order=o)[0])
    return P,((float(g.m.grip_s(1.15,o)),P-hi),(P-lo,P+lo))

def control_knots(length,n):
    # Four vanishing interior/endpoint control words on each open end.
    k=3;count=n+8
    return np.r_[np.zeros(4),np.linspace(0.,length,count-k+1)[1:-1],np.full(4,length)]

class Controls:
    def __init__(self,length,n):
        self.n=n;self.length=length
        knots=control_knots(length,n);words=np.pad(np.eye(n),((4,4),(0,0)))
        self.b=BSpline(knots,words,3,axis=0)
        self.db=self.b.derivative();self.db2=self.b.derivative(2)
        self.d=self.db.c[:len(self.db.t)-self.db.k-1]
    def words(self,x):
        n=self.n;raw=x[n:];d=self.d@raw
        # The derivative spline is a convex combination of its real coefficients.
        b=g.B/.98;u=b*d;scale=(1+np.sum(u**8))**(-1/8)
        ds=-scale**9*b*(u**7@self.d)
        return x[:n],raw*scale,scale*np.eye(n)+np.outer(raw,ds)
    def evaluate(self,r,x):
        a,e,j=self.words(x);b=self.b(r)
        return b@a,b@e,b,self.b(r)@j
    def bound(self,x):
        return float(np.max(abs(self.d@self.words(x)[1])))

def stations(start,end,o,n):
    P=domain(o)[0];old=g.old.c.stations(o);half=g.m.LEFT_LENGTH/2
    ell,slack,_=g.wall.spec(o)
    dest=np.unique(np.r_[0.,slack,slack+np.array(g.wall.CLOCK),ell]);l=[]
    for t in dest:
        a,b=0.,half
        for _ in range(54):
            u=(a+b)/2
            if u+(ell-half)*cap_s7(J(np.asarray(u/half))).v<ell-t:a=u
            else:b=u
        l.append((a+b)/2)
    # Include the support/plateau crossings of the actual Cartesian preloading clock.
    edges=np.unique(np.r_[0.,l,old,P/2])
    extra=[]
    for a,b in zip(edges[:-1],edges[1:]):
        q=g.wall.parts(J(np.array([a,b])),o)[0][0].v
        for x in g.CUT:
            if (x-q[0])*(x-q[1])<0.:
                lo,hi=a,b
                for _ in range(44):
                    u=(lo+hi)/2;v=float(g.wall.parts(J(np.array([u])),o)[0][0].v[0])
                    if (v<x)==(q[0]<q[1]):lo=u
                    else:hi=u
                extra.append((lo+hi)/2)
    t=np.r_[edges,extra];t=np.mod(np.r_[t,P-t],P)
    aug=np.r_[start,end,np.linspace(start,end,n+1),t,t+P]
    a=np.unique(aug[(aug>=start)&(aug<=end)]);return np.r_[a[:-1][np.diff(a)>5e-12],end]

class Arc:
    def __init__(self,side,order,n,bases,keep_sign):
        self.keep_sign=keep_sign;self.side=side;self.o=order;a,b=domain(order)[1][side]
        self.s=stations(a,b,order,n);self.ref=reference(self.s,order)
        v=self.ref[:,1];self.speed=np.linalg.norm(v,axis=1);self.t0=unit(v)
        self.n0=np.cross(Y,self.t0);self.k0=np.einsum("ij,ij->i",self.ref[:,2],self.n0)/self.speed**2
        ds=np.diff(self.s);nl,w=g.m.old.disk.rule(order)
        ga=self.s[:-1,None]+ds[:,None]*nl
        self.h=ds*(np.linalg.norm(reference(ga,order)[...,1,:],axis=-1)@w)
        self.r=np.r_[0.,np.cumsum(self.h)];self.length=self.r[-1]
        self.ctrl=Controls(self.length,bases)
        acc=np.einsum("ij,ij->i",v,self.ref[:,2])/self.speed
        self.rmap=BPoly.from_derivatives(self.s,list(zip(self.r,self.speed,acc)))
        # Preserve a C2 increasing arclength chart even on widely unequal imported cells.
        if np.min(self.rmap.derivative().c)<=0:
            # Positive quartic Bernstein speed, matched value and zero derivative at both ends.
            # The cell increment is unchanged and the alternate clock is charged by the real Gram.
            low=min(np.min(self.h/ds),np.min(self.speed))*.5;coef=[]
            for r,h,w in zip(self.r[:-1],self.h,ds):
                speed=np.array([low,low,5*h/w-4*low,low,low]);coef.append(r+np.r_[0.,np.cumsum(w*speed/5)])
            self.rmap=BPoly(np.column_stack(coef),self.s)
        s_mid=(self.s[1:]+self.s[:-1])*.5
        v=reference(s_mid,order);self.tm=unit(v[:,1]);self.km=np.einsum("ij,ij->i",v[:,2],np.cross(Y,self.tm))/np.sum(v[:,1]**2,axis=1)
        self.rm=self.rmap(s_mid);self.dq=np.diff(self.ref[:,0],axis=0)
        self.r0=self.ref[:,0]
    def curvatures(self,r,k0,x):
        raw,e,b,je=self.ctrl.evaluate(r,x)
        if self.keep_sign:
            d=np.hypot(1.,raw);t=np.where(raw>=0.,d+raw,1/(d-raw+np.where(raw>=0.,1.,0.)))
            return k0*t,e,(k0*t/d)[:,None]*b,je
        return k0+raw,e,b,je
    def integrate(self,x,jac=False):
        c=self.ctrl;k,eta,b,je=self.curvatures(self.rm,self.km,x);dk=k-self.km
        w=self.h[:,None]*(dk[:,None]*Y+(eta*k)[:,None]*self.tm)
        ro=Rotation.from_rotvec(w).as_matrix();half=Rotation.from_rotvec(w*.5).as_matrix()
        A=np.empty((len(self.r),3,3));A[0]=I
        for j,R in enumerate(ro):A[j+1]=A[j]@R
        amid=A[:-1]@half;ch=np.einsum("ijk,ik->ij",amid,self.dq)
        displacement=np.vstack((np.zeros(3),np.cumsum(ch-self.dq,axis=0)))
        if not jac:return A,displacement
        # Every interval's oriented screw and midpoint subincrement act on all remaining chords.
        n=c.n;dw=np.concatenate(((Y+eta[:,None]*self.tm)[:,:,None]*b[:,None,:],
                               (k[:,None]*self.tm)[:,:,None]*je[:,None,:]),axis=2)*self.h[:,None,None]
        full=A[:-1]@left_jac(w)@dw;mid=.5*(A[:-1]@left_jac(.5*w)@dw)
        rest=np.cumsum(ch[::-1],axis=0)[::-1]-ch
        jp=np.sum(np.cross(full.transpose(0,2,1),rest[:,None,:])+np.cross(mid.transpose(0,2,1),ch[:,None,:]),axis=0).T
        jw=full.sum(axis=0)
        jr=np.stack([np.cross(jw.T,A[-1,:,i]).T for i in range(3)],axis=1)
        return A,displacement,np.vstack((jp,jr.reshape(9,2*n)))
    def goal(self,ph):
        p=g.pose(ph,self.o);return (1 if self.side==0 else -1)*np.array([0.,p[4],p[5]])
    def shoot(self,ph,x0,it,shape):
        target=self.goal(ph);n=self.ctrl.n;last=[None,None,None]
        def obj(x):
            if last[0] is not None and np.array_equal(x,last[0]):return last[1:]
            A,d,J0=self.integrate(x,True)
            rr=np.r_[d[-1]-target,(A[-1]-I).ravel()]
            pen=2e-5 if not shape else .0004
            vals=[rr,pen*x];jm=[J0,pen*np.eye(2*n)]
            if shape:
                k,e,b,je=self.curvatures(self.rm,self.km,x)
                w0,w1,Jw=self.ctrl.words(x);bp=self.ctrl.db(self.rm);de=bp@w1
                den=1-g.B*np.abs(de);ks=np.abs(k)*(1+e*e)/den
                val=np.maximum(ks-7.54,0.)*.006*np.sqrt(self.h)
                deriv=np.concatenate((np.sign(k)[:,None]*(1+e*e)[:,None]*b/den[:,None],
                      np.abs(k)[:,None]*(2*e[:,None]*je/den[:,None]+
                      ((1+e*e)*g.B*np.sign(de)/den**2)[:,None]*(bp@Jw))),axis=1)
                vals.append(val);jm.append((.006*np.sqrt(self.h)*(ks>7.54))[:,None]*deriv)
            last[:]=[x.copy(),np.concatenate(vals),np.vstack(jm)]
            return last[1:]
        if not ph:return x0*0.,[0,0,0.,0.]
        z=least_squares(lambda x:obj(x)[0],x0,jac=lambda x:obj(x)[1],max_nfev=it,
                        ftol=1e-13,gtol=1e-13,xtol=1e-13,x_scale=1.)
        return z.x,[int(z.status),int(z.nfev),float(z.cost),float(z.optimality)]
