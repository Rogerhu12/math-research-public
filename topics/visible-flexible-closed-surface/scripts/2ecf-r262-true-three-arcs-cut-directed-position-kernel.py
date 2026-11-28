#!/usr/bin/env python3
"""Outward two-jets of the complete original R262 prefix and the true-arc/height/XYZ surgery."""
from fractions import Fraction as F
import math
import numpy as np

def setup(core):
    global base,k,I,Jet,Tr,LD
    base=core.base;k=core.kern;I=k.I;Jet=k.Jet;Tr=base.Trig;LD=k.LD

def zero():return [I(0) for _ in range(3)]
def add(*v):return [sum((row[i] for row in v),I(0)) for i in range(3)]
def mul(v,a):return [x*a for x in v]
def sub(v,w):return add(v,mul(w,-1))
def dot(v,w):return sum((x*y for x,y in zip(v,w)),I(0))
def cross(v,w):return [v[(i+1)%3]*w[(i+2)%3]-v[(i+2)%3]*w[(i+1)%3] for i in range(3)]
def sq(v):return sum((x.square() for x in v),I(0))
def clamp(v,lo,hi):return I(np.clip(v.lo,lo,hi),np.clip(v.hi,lo,hi))
class BoxTrig:
    """One checked central sine/cosine, exact angle addition and a Lipschitz enclosure for each whole box."""
    def __init__(self,theta):
        self.theta=theta
        mid=theta.lo/2+theta.hi/2
        self.radius=I((theta-I(mid)).abs_upper())
        self.points={0:(I(0),I(1)),1:k.sincos(I(mid))}
        self.values={0:self.points[0]}
    @staticmethod
    def unit(z):return I(np.maximum(z.lo,LD(-1)),np.minimum(z.hi,LD(1)))
    def point(self,n):
        if n not in self.points:
            a,b=self.point(n//2)
            s=self.unit(2*a*b);c=self.unit(b.square()-a.square())
            if n%2:
                sa,ca=self.points[1]
                s,c=self.unit(s*ca+c*sa),self.unit(c*ca-s*sa)
            self.points[n]=(s,c)
        return self.points[n]
    def __call__(self,n):
        n=int(n)
        if n<0:
            a,b=self(-n);return -a,b
        if n not in self.values:
            s,c=self.point(n);d=n*self.radius
            self.values[n]=(self.unit(s.widen(d)),self.unit(c.widen(d)))
        return self.values[n]

def bern16(x,d):
    # S=I_x(8,8) (d=15); its integral has control max(j-8,0)/16 (d=16).
    co=[F(int(j>=8)) if d==15 else F(max(0,j-8),16) for j in range(d+1)]
    a=1-x
    return sum((c*math.comb(d,j)*x**j*a**(d-j) for j,c in enumerate(co) if c),I(0))

class TrueArc:
    def __init__(self,low,div=8192):
        self.div=div;self.half=k.PI/3
        self.a=I(F(183,400));self.tau=(2*self.half-F(183,200)-F(109,100))/2
        self.lo=I(low);self.hi=(2*self.half-self.lo*(F(183,200)+self.tau))/(F(109,100)+self.tau)
        self.si,self.co=k.sincos(self.half)
        ts=self.half*I(np.arange(div+1, dtype=LD))/div
        b,_=self.angles(ts);ss,cc=k.sincos(b)
        # beta increases over [0,pi/3]. Paired left/right Darboux sums give
        # true directed position primitives without numerical quadrature assumptions.
        step=self.half/div
        ds=step*I(ss.lo[:-1],ss.hi[1:]);dc=step*I(cc.lo[1:],cc.hi[:-1])
        self.S=self.accumulate(ds);self.C=self.accumulate(dc)
        self.A=self.S[-1]+self.co/self.si*self.C[-1]
    @staticmethod
    def accumulate(x):
        lo=np.zeros(len(x.lo)+1,dtype=LD);hi=lo.copy()
        for j in range(len(x.lo)):lo[j+1]=k.down(lo[j]+x.lo[j]);hi[j+1]=k.up(hi[j]+x.hi[j])
        return I(lo,hi)
    def angles(self,m):
        x=clamp((m-self.a)/self.tau,0,1)
        extra=I(np.maximum((m-self.a-self.tau).lo,LD(0)),np.maximum((m-self.a-self.tau).hi,LD(0)))
        # Use monotonicity before interval evaluation of Bernstein sums.
        def E(j):
            v=bern16(I(x.lo),j);w=bern16(I(x.hi),j)
            return I(v.lo,w.hi)
        return self.lo*m+(self.hi-self.lo)*(self.tau*E(16)+extra),self.lo+(self.hi-self.lo)*E(15)
    def jets(self,u,up,upp):
        m=self.half-u
        m=I(np.maximum(0,m.lo),np.minimum(self.half.hi,m.hi))
        a=m/self.half*self.div
        left=np.clip(np.floor(a.lo).astype(int),0,self.div)
        right=np.clip(np.ceil(a.hi).astype(int),0,self.div)
        sx=I(self.S.lo[left],self.S.hi[right]);cy=I(self.C.lo[left],self.C.hi[right])
        x=self.A-sx;y=-cy
        P=[self.co*x-self.si*y,self.si*x+self.co*y,I(0)]
        b,cur=self.angles(m);ss,cc=k.sincos(self.half-b)
        N=[cc,ss,I(0)];T=[-ss,cc,I(0)]
        return [P,mul(T,up),add(mul(T,upp),mul(N,-cur*up**2))]

def polar_coeff(c,M):
    v={1:c[...,0]}
    for j in range(1,M+1):
        v[1+3*j]=(c[...,j]+c[...,M+j])/2
        v[1-3*j]=(c[...,j]-c[...,M+j])/2
    h={0:c[...,-1]}
    h.update({3*j:c[...,2*M+j] for j in range(1,M+1)})
    return v,h

def fourier(v,h,tr,d):
    x,y,z=zero()
    for m,c in v.items():
        s,co=tr(m);g=c*m**d
        x=x+g*(co,-s,-co)[d];y=y+g*(s,co,-s)[d]
    for m,c in h.items():
        s,co=tr(m);z=z+c*m**d*(co,-s,-co)[d]
    return [x,y,z]

def horn(c,x,w):
    # x is native or saved normalized coordinate in the chosen physical span.
    d=I(np.stack([(c[j]*j).lo for j in range(1,6)]),np.stack([(c[j]*j).hi for j in range(1,6)]))
    dd=I(np.stack([(c[j]*j*(j-1)).lo for j in range(2,6)]),np.stack([(c[j]*j*(j-1)).hi for j in range(2,6)]))
    return [base.horner_rows(c,x),base.horner_rows(d,x)/w,base.horner_rows(dd,x)/(w*w)]

def angular(C,lam,arc,theta):
    t=Jet.variable(theta,2)
    tr=Tr(t);u=C.u(t,tr);p0=k.implicit_angle(C.e0,u);pr=Tr(p0)
    den=1-C.e0*pr(3)[1]
    native=C.gamma(t,0,tr);old=C.gamma(p0,0,pr)
    n0=mul(native,1/C.a);d0=sub(n0,old)
    d2=mul(C.second(p0,0,pr),-lam*lam/den)
    def parts(V):
        return [[(a.c[d]*(2 if d==2 else 1) if isinstance(a,Jet) else (a if d==0 else I(0))) for a in V] for d in range(3)]
    up=u.c[1];upp=2*u.c[2]
    new=arc.jets(u.c[0],up,upp);p=parts(n0)
    return dict(u=u.c[0],up=up,upp=upp,tr=Tr(theta),d0=parts(d0),d2=parts(d2),
                delta=[sub(z,v) for z,v in zip(new,p)],newArc=new)

def native_jets(D,cell,n,ch,ang,height):
    z=n/D.end-ch['origin'];e=k.poly(ch['coefficients'],z)
    ec=ch['coefficients']
    eg=k.poly([j*v for j,v in enumerate(ec) if j],z)*D.lam/D.end if len(ec)>1 else I(0)
    egg=k.poly([j*(j-1)*v for j,v in enumerate(ec) if j>=2],z)*(D.lam/D.end)**2 if len(ec)>2 else I(0)
    psi=k.implicit_angle(e,ang['u']);tr=BoxTrig(psi);s,co=tr(3);rho=1-e*co
    ps=eg*s/(3*rho);pt=ang['up']/rho
    pss=(egg*s/3+2*eg*co*ps-3*e*s*ps**2)/rho
    pst=(eg*co*pt-3*e*s*ps*pt)/rho
    ptt=(ang['upp']-3*e*s*pt**2)/rho
    row=D.native_piece(cell);v=horn(row.c,(n-row.left)/row.width,row.width/D.lam)
    V,H=polar_coeff(v[0],row.M);V1,H1=polar_coeff(v[1],row.M);V2,H2=polar_coeff(v[2],row.M)
    X=fourier(V,H,tr,0);X[2]=X[2]+height
    b=fourier(V,H,tr,1);bb=fourier(V,H,tr,2);a=fourier(V1,H1,tr,0);ab=fourier(V1,H1,tr,1);aa=fourier(V2,H2,tr,0)
    return [X,add(a,mul(b,ps)),mul(b,pt),
       add(aa,mul(ab,2*ps),mul(bb,ps**2),mul(b,pss)),
       add(mul(ab,pt),mul(bb,ps*pt),mul(b,pst)),add(mul(bb,pt**2),mul(b,ptt))]

def cpolys(p,s,h):
    d=[j*v for j,v in enumerate(p) if j];dd=[j*(j-1)*v for j,v in enumerate(p) if j>=2]
    return [k.poly(p,s/h),k.poly(d,s/h)/h,k.poly(dd,s/h)/h**2]
ORD=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))

def apply_lift(out,angular,radial):
    for j,(r,d) in enumerate(ORD):out[j]=add(out[j],mul(angular[d],radial[r]))

def source(D,cell,n,ch,ang,mean,central):
    s=n/D.lam;out=native_jets(D,cell,n,ch,ang,mean)
    if central:
        h=D.h
        apply_lift(out,ang['d0'],cpolys([1,0,0,-10,15,-6],s,h))
        apply_lift(out,[[I(0),I(0),1-D.lam],zero(),zero()],cpolys([0,h,0,-6*h,8*h,-3*h],s,h))
        apply_lift(out,ang['d2'],cpolys([0,0,h*h/2,-3*h*h/2,3*h*h/2,-h*h/2],s,h))
    return out

def spectral(c,t,left,width,scale,pm,hm,tr,new=False):
    rows=horn(c,(t-left)/width,width*scale)
    out=[]
    for r,d in ORD:
        a=rows[r]
        if new:
            m=(a.shape[-1]-2)//3
            # D3/reﬂection coefficient relations are verified at input.
            V={i:a[...,i] for i in range(1,m+1) if i%3==1}
            V.update({-i:a[...,i] for i in range(1,m+1) if i%3==2})
            H={i:a[...,2*m+1+i] for i in range(0,m+1,3)}
        else:
            V={j:a[...,i] for i,j in enumerate(pm)}
            H={j:a[...,len(pm)+i] for i,j in enumerate(hm)}
        out.append(fourier(V,H,tr,d))
    return out

def power(ctrl):
    return base.arrq([[math.comb(5,j)*sum(((-1)**(j-t)*math.comb(j,t)*ctrl[t][i] for t in range(j+1)),F(0)) for i in range(len(ctrl[0]))] for j in range(6)])

def geometry(J,K):
    P,A,B,AA,AB,BB=J;normal=cross(B,A);ar2=sq(normal)
    if np.any(ar2.lo<=0):return None
    ar=ar2.sqrt()
    E=sq(A);F0=dot(A,B);G=sq(B)
    # N is not normalized. K*|N| g +/- II_N is positive semidefinite.
    l=dot(normal,AA);m=dot(normal,AB);nn=dot(normal,BB)
    h=K*ar
    records=[]
    for sign in (-1,1):
        a=h*E+sign*l;d=h*G+sign*nn;b=h*F0+sign*m
        records.extend((a.lo,d.lo,(a*d-b.square()).lo))
    return dict(height=P[2].lo,support=(dot(P,normal)/ar).lo,area2=ar2.lo,
                curvatureFormMin=np.minimum.reduce(np.broadcast_arrays(*records)))

def cut_blend(J,ang,q,c,width,gate_on):
    if not gate_on:return J
    g,g1,g2=cpolys([0,0,0,10,-15,6],q-c,width)
    C=[[v for v in ang['newArc'][0]],[I(0),I(0),I(1)],ang['newArc'][1],zero(),zero(),ang['newArc'][2]]
    C[0][2]=C[0][2]+q
    delta=[sub(x,y) for x,y in zip(J,C)]
    Z=[add(x,mul(y,g)) for x,y in zip(C,delta)]
    Z[1]=add(Z[1],mul(delta[0],g1))
    Z[3]=add(Z[3],mul(delta[1],2*g1),mul(delta[0],g2))
    Z[4]=add(Z[4],mul(delta[2],g1))
    return Z
