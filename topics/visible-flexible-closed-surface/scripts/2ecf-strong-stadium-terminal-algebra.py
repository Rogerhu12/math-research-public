"""Exact Fourier identities for terminal comparands; all saved high modes retained."""
from fractions import Fraction as Q
import math
import numpy as np


class Poly:
    def __init__(self,re,im,b):
        self.re=list(re);self.im=list(im);self.b=b;self.d=(len(self.re)-1)//2
    @classmethod
    def scalar(cls,q):
        q=Q(q);n=q.denominator
        if n&(n-1):raise ValueError("Dyadic multiplier required")
        return cls([q.numerator],[0],n.bit_length()-1)
    def pair(self,d,b):
        p=d-self.d
        return [[0]*p+[v<<(b-self.b) for v in a]+[0]*p for a in (self.re,self.im)]
    def __add__(self,b):
        if not isinstance(b,Poly):b=Poly.scalar(b)
        n=max(self.b,b.b);d=max(self.d,b.d);a=self.pair(d,n);bp=b.pair(d,n)
        return Poly(*[[v+w for v,w in zip(i,j)] for i,j in zip(a,bp)],n)
    __radd__=__add__
    def __neg__(self):return Poly([-v for v in self.re],[-v for v in self.im],self.b)
    def __sub__(self,b):return self+(-b)
    def __mul__(self,b):
        if not isinstance(b,Poly):b=Poly.scalar(b)
        a=self
        if b.d==0 and b.im[0]==0:return Poly([v*b.re[0] for v in a.re],[v*b.re[0] for v in a.im],a.b+b.b)
        if a.d==0 and a.im[0]==0:return b*a
        bits=max(max(abs(v).bit_length() for v in x) for x in (a.re,a.im))+max(max(abs(v).bit_length() for v in x) for x in (b.re,b.im))+(4*min(len(a.re),len(b.re))).bit_length()+2
        n=len(a.re)+len(b.re)-1
        v=GRAM.cmul((GRAM.pack(a.re,bits),GRAM.pack(a.im,bits)),(GRAM.pack(b.re,bits),GRAM.pack(b.im,bits)))
        return Poly(*[GRAM.unpack(i,bits,n) for i in v],a.b+b.b)
    __rmul__=__mul__
    def der(self):
        ks=range(-self.d,self.d+1)
        return Poly([-k*v for k,v in zip(ks,self.im)],[k*v for k,v in zip(ks,self.re)],self.b)
    def norm(self,j=0,cut=-1):
        return Q(sum((abs(a)+abs(b))*abs(k)**j for k,a,b in zip(range(-self.d,self.d+1),self.re,self.im) if abs(k)>cut),1<<self.b)


def setup(gram,pp,m,co,si,f0):
    global GRAM
    GRAM=gram
    d=len(co)-1;b=max(gram.dyadic_bits(q/2) for row in co+si for q in row)
    G=[]
    for i in range(3):
        re=[0]*(2*d+1);im=re.copy();re[d]=gram.scaled(co[0][i],b)
        for k in range(1,d+1):
            re[d+k]=re[d-k]=gram.scaled(co[k][i]/2,b);im[d+k]=gram.scaled(-si[k][i]/2,b);im[d-k]=-im[d+k]
        G.append(Poly(re,im,b))
    X,V,A=[[Poly(x[0],x[1],m.input_bits) for x in row] for row in m.port(64)]
    der=lambda v:[a.der() for a in v]
    p=der(G);q=der(p)
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    cross=lambda a,b:[a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3] for i in range(3)]
    E=dot(p,p);B=dot(p,q);Rt=dot(V,p);vp=dot(V,q);length=dot(V,V)-Poly.scalar(1)
    normalResidual=f0*(E*vp-B*Rt)+m.v*E*E
    W=cross(V,p);wp=dot(der(V),W);aw=dot(A,W);qw=dot(q,W);rank=aw*qw-wp*wp
    R=dict(Rt=Rt,Rn=normalResidual,Rl=length,At=dot(A,p),Ad=dot(A,V),Ra=rank)
    return G,V,A,R


def spectral_box(src,pp,cert,cut,orders):
    powers=[p for p in src];maxd=max(p.d for p in powers);cut=min(cut,maxd)
    co=[[Q(0) for _ in range(3)] for _ in range(cut+1)]
    si=[[Q(0) for _ in range(3)] for _ in range(cut+1)]
    for i,p in enumerate(src):
        co[0][i]=Q(p.re[p.d],1<<p.b)
        for j in range(1,min(cut,p.d)+1):
            co[j][i]=Q(2*p.re[p.d+j],1<<p.b);si[j][i]=Q(-2*p.im[p.d+j],1<<p.b)
    four=pp.Fourier(co,si,cert,max_order=orders+4)
    tail=[[p.norm(j,cut) for p in src] for j in range(orders+1)]
    def box(k,n,phase,pi):
        pt=four.point(k,n,phase,order=orders+3);h=pi/n
        v=[]
        for j in range(orders+1):
            rr=[]
            for i in range(3):
                bound=sum((cert.I.raw(0,pt[j+a][i].absupper())*h**a/math.factorial(a) for a in (1,2,3)),cert.I(0))
                bound+=cert.I(four.absolute[j+4][i])*h**4/24
                rr.append(pt[j][i]+cert.I.raw(-bound.hi,bound.hi))
            v.append(rr)
        for j in range(orders+1):
            for i,p in enumerate(src):
                e=cert.I(tail[j][i]);v[j][i]+=cert.I.raw(-e.hi,e.hi)
        return [row[:len(src)] for row in v]
    return box
