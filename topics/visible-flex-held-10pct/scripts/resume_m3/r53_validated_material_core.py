#!/usr/bin/env python3
"""Independent interval oracle for the true R53 material support core.

The original support coefficients, lambda, S,b,k are frozen binary rationals.
The period is the true 2*pi/3; arc inverse and all primitives are mathematical
ones. Taylor coefficients of the support inverse are enclosed by outward
arithmetic; a complex-strip Cauchy estimate pays the tails. No source float
inverse, cached lift, or quadrature output is treated as an exact true value.
"""
import bisect,hashlib,importlib.util,json,math,sys,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import mpmath as mp

def module(name,path):
    sp=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
def fq(x):return Q.from_float(float(x))
def mplo(x):return mp.make_mpf(x._mpi_[0])
def mphi(x):return mp.make_mpf(x._mpi_[1])
def mpq(x):x=Q(x);return mp.iv.mpf(x.numerator)/x.denominator
def qeval(c,x):
    v=Q(0)
    for a in c[::-1]:v=v*x+a
    return v
def qder(c):return [(j+1)*c[j+1] for j in range(len(c)-1)]

class ValidatedMaterialCore:
    def __init__(self, core, mean_kernel, interval_kernel, degree=24, cells_per_unit=128,progress=None):
        self.started=time.monotonic();self.core=core
        self.base=module("_r53_validated_mean_base",mean_kernel)
        self.K=module("_r53_validated_interval_kernel",interval_kernel);self.base.K=self.K
        self.I=self.base.I
        mp.mp.dps=90;mp.iv.dps=75
        self.degree=degree;self.cells_per_unit=cells_per_unit
        assert degree>=8 and cells_per_unit>0 and cells_per_unit&(cells_per_unit-1)==0
        self.h=Q(1,2*cells_per_unit)
        self.a=[fq(x) for x in core.original.coefficients]
        self.m=[int(x) for x in core.original.frequencies]
        self.b=[(1-m*m)*a for m,a in zip(self.m,self.a)]
        self.rho_min=1-sum(map(abs,self.b))
        self.lam=fq(core.homotopy);self.S=fq(core.halfwidth)
        self.width=fq(core.transition);self.k=fq(core.k)
        assert core.base_mode==3 and core.curvature_blend==1
        assert self.S==Q(1,2) and Q(199,1000)<self.width<Q(201,1000)
        assert Q(199,1000)<self.k<Q(201,1000) and 0<self.lam<Q(1,499)
        assert self.rho_min>Q(49,100)
        assert self.k<1/(2-self.rho_min)
        self.Tmp=2*mp.iv.pi/3;self.Lmp=mp.iv.pi/3
        self.T,self.L=self.from_mp(self.Tmp),self.from_mp(self.Lmp)
        self.r=Q(7,100);self.R=Q(29,1000)
        B=sum((mpq(abs(b))*(mp.iv.exp(m*mpq(self.r))+mp.iv.exp(-m*mpq(self.r)))/2
               for b,m in zip(self.b,self.m)),mp.iv.mpf(0))
        assert mphi(B)<mp.mpf(581)/1000
        self.strip_B=self.from_mp(B)
        assert self.R<self.r*(1-Q(581,1000))
        t=self.R/Q(199,1000);sig=Q(1,4)+t+t*t
        W=1+t*630*sig**4;oldK=Q(1000,419)
        K=oldK+self.lam*((1+W)*(self.k+oldK)+3*W)
        assert K<Q(5,2)
        self.complex_kappa_bound=Q(5,2)
        # A separate coarse real integral bound proves beta<3 before quadrature.
        D=self.L-self.rat(self.S+self.width/2)
        beta_max=self.rat((self.S+self.width/2)*(1/self.rho_min-self.k))/D
        assert float(beta_max.x[1])<3
        self.beta_coarse_upper=float(beta_max.x[1])
        self._inverse_taylor()
        if progress:progress({"stage":"inverse_taylor","seconds":time.monotonic()-self.started})
        self._build_omega()
        if progress:progress({"stage":"weighted_primitive","seconds":time.monotonic()-self.started})
        self._gauss_rule()
        self._build_position()
        self.seconds=time.monotonic()-self.started

    def rat(self,x):return self.I.rational(Q(x))
    def from_mp(self,x):
        return self.I(self.K.dn(float(mplo(x))),self.K.up(float(mphi(x))))
    def arr_mp(self,x):
        return self.I(np.array([self.K.dn(float(mplo(z))) for z in x]),
                      np.array([self.K.up(float(mphi(z))) for z in x]))
    def stack(self,x,axis=0):return self.I.raw(self.K.stack([z.x for z in x],axis))
    def hull(self,a,b):return self.I(np.minimum(a.x[0],b.x[0]),np.maximum(a.x[1],b.x[1]))
    def sym(self,x):
        y=float(self.rat(x).x[1]);return self.I(-y,y)
    def sincos(self,x):
        x=self.I(x);mid=(x.x[0]+x.x[1])/2
        quadrant=np.rint(mid/(np.pi/2)).astype(int)
        y=x-self.I(quadrant)*self.from_mp(mp.iv.pi/2)
        s,c=self.base.sincos_i(y)
        q=quadrant%4
        return (self.I(np.choose(q,[s.x[0],c.x[0],-s.x[1],-c.x[1]]),
                       np.choose(q,[s.x[1],c.x[1],-s.x[0],-c.x[0]])),
                self.I(np.choose(q,[c.x[0],-s.x[1],-c.x[1],s.x[0]]),
                       np.choose(q,[c.x[1],-s.x[0],-c.x[0],s.x[1]])))
    def _arc_mp(self,p):
        return p+sum((mpq(b)/m*mp.iv.sin(m*p) for b,m in zip(self.b,self.m)),mp.iv.mpf(0))
    def _rho_mp(self,p):
        return 1+sum((mpq(b)*mp.iv.cos(m*p) for b,m in zip(self.b,self.m)),mp.iv.mpf(0))
    def _inverse_point_mp(self,target,seed):
        c=mp.iv.mpf(float(seed));res=self._arc_mp(c)-target
        rad=mphi(mp.iv.mpf(max(abs(mplo(res)),abs(mphi(res))))/mpq(self.rho_min))
        box=c+mp.iv.mpf([-1,1])*mp.iv.mpf(rad)
        for _ in range(3):
            center=(mplo(box)+mphi(box))/2
            rho=self._rho_mp(box)
            assert mplo(rho)>0
            nb=mp.iv.mpf(center)-(self._arc_mp(mp.iv.mpf(center))-target)/rho
            lo,hi=max(mplo(box),mplo(nb)),min(mphi(box),mphi(nb))
            assert lo<=hi
            box=mp.iv.mpf([lo,hi])
        return box
    def _inverse_taylor(self):
        # Rational cells cover the whole true sector, with one spare terminal cell.
        self.count=math.ceil(float(mphi(self.Tmp))*self.cells_per_unit)+1
        centers=[Q(2*j+1,2*self.cells_per_unit) for j in range(self.count)]
        self.centers=centers
        seeds=self.core.original.evaluate(np.array(list(map(float,centers))))["phi"]
        phi=[self._inverse_point_mp(mpq(t),s) for t,s in zip(centers,seeds)]
        A=[self.arr_mp(phi)]
        co=self.I(np.array([[self.K.dn(float(mplo(mp.iv.cos(m*p)))) for p in phi] for m in self.m]),
                  np.array([[self.K.up(float(mphi(mp.iv.cos(m*p)))) for p in phi] for m in self.m]))
        sn=self.I(np.array([[self.K.dn(float(mplo(mp.iv.sin(m*p)))) for p in phi] for m in self.m]),
                  np.array([[self.K.up(float(mphi(mp.iv.sin(m*p)))) for p in phi] for m in self.m]))
        weights=self.stack([self.rat(b) for b in self.b]).expand()
        freq=self.I(np.array(self.m)[:,None])
        rho=[1+(weights*co).sum(0)];recip=[1/rho[0]]
        A.append(self.rat(self.h)*recip[0])
        er=[self.I(np.ones((len(self.m),self.count)))];ei=[self.I(np.zeros((len(self.m),self.count)))]
        for n in range(1,self.degree):
            rr=self.I(np.zeros_like(er[0].x[0]));ii=self.I(np.zeros_like(ei[0].x[0]))
            for k in range(1,n+1):
                factor=k*self.I(A[k].x[0][None,:],A[k].x[1][None,:])
                rr=rr+factor*er[n-k];ii=ii+factor*ei[n-k]
            er.append(-freq*ii/n);ei.append(freq*rr/n)
            cn=co*er[n]-sn*ei[n]
            rho.append((weights*cn).sum(0))
            rec=self.I(np.zeros(self.count))
            for k in range(1,n+1):rec=rec+rho[k]*recip[n-k]
            recip.append(-rec/rho[0]);A.append(self.rat(self.h)*recip[-1]/(n+1))
        self.A=A
        self.inverse_seed_max_width=max(float(mphi(p)-mplo(p)) for p in phi)
    def _tail(self,tmax,j):
        # Cauchy |a_n| <= r/R^n, summed as a decreasing-ratio geometric tail.
        v=Q(tmax);n=self.degree+1
        assert v<1 and j<n
        ratio=v*Q(n+1,n+1-j)
        return self.r/self.R**j*math.prod(range(n-j+1,n+1))*v**(n-j)/(1-ratio)
    def inverse(self,theta,order=0):
        theta=self.I(theta)
        mid=(theta.x[0]+theta.x[1])/2
        index=np.clip(np.floor(mid*self.cells_per_unit).astype(int),0,self.count-1)
        origin=self.I((index+.5)/self.cells_per_unit)
        x=(theta-origin)/self.rat(self.h)
        radius=self.K.up(np.maximum(abs(theta.x[0]-origin.x[0]),abs(theta.x[1]-origin.x[1])))
        tmax=fq(float(np.max(radius)))/self.R
        coeff=[]
        for n in range(order,self.degree+1):
            val=self.A[n].item(index)*math.prod(range(n-order+1,n+1))/self.rat(self.h**order)
            coeff.append(val)
        out=self.I(np.zeros_like(mid))
        for val in coeff[::-1]:out=out*x+val
        return out+self.sym(self._tail(tmax,order))
    def _pmul(self,a,b):
        c=[self.I(0) for _ in range(len(a)+len(b)-1)]
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
        return c
    def _ppower(self,a,n):
        c=[self.I(1)]
        for _ in range(n):c=self._pmul(c,a)
        return c
    def _pvalue(self,a,x):
        v=self.I(0)
        for c in a[::-1]:v=v*x+c
        return v
    def _weighted_piece(self,left,right):
        mid=float((left.x[0]+left.x[1]+right.x[0]+right.x[1])/4)
        idx=min(self.count-1,max(0,int(math.floor(mid*self.cells_per_unit))))
        origin=self.rat(self.centers[idx])
        v0=(origin-self.L-self.rat(self.S))/self.rat(self.width)
        vh=self.rat(self.h/self.width)
        high=mid>float((self.L+self.rat(self.S+self.width/2)).x[1])
        affine=[1-v0,-vh] if high else [v0,vh]
        step=[self.I(0) for _ in range(10)]
        for factor,power in [(126,5),(-420,6),(540,7),(-315,8),(70,9)]:
            for k,x in enumerate(self._ppower(affine,power)):step[k]=step[k]+factor*x
        chi=step if high else [1-step[0]]+[-v for v in step[1:]]
        curv=[-(j+1)*self.A[j+1].item(idx)/self.rat(self.h) for j in range(self.degree)]
        curv[0]=curv[0]+self.rat(self.k)
        integrand=self._pmul(chi,curv)
        anti=[self.I(0)]+[c/(j+1) for j,c in enumerate(integrand)]
        return origin,anti
    def _weighted_part(self,piece,right):
        left,origin,anti=piece
        lo=(left-origin)/self.rat(self.h);hi=(right-origin)/self.rat(self.h)
        out=self.rat(self.h)*(self._pvalue(anti,hi)-self._pvalue(anti,lo))
        # The true integration interval lies in the transition, where 0<=chi<=1.
        radius=max((left-origin).absolute_upper(),(right-origin).absolute_upper())
        tail=self._tail(fq(radius)/self.R,1)
        length=(right-left).absolute_upper()
        return out+self.sym(fq(length)*tail)
    def _build_omega(self):
        first=self.L+self.rat(self.S);last=first+self.rat(self.width)
        middle=first+self.rat(self.width/2)
        grid=[first,middle,last]
        for j in range(self.count+1):
            q=Q(j,self.cells_per_unit)
            if float(first.x[1])<float(q)<float(last.x[0]):grid.append(self.rat(q))
        grid.sort(key=lambda x:float((x.x[0]+x.x[1])/2))
        assert all(float(a.x[1])<float(b.x[0]) for a,b in zip(grid[:-1],grid[1:]))
        self.og=grid;self.opieces=[];self.ocumulative=[self.I(0)]
        for left,right in zip(grid[:-1],grid[1:]):
            origin,anti=self._weighted_piece(left,right)
            piece=(left,origin,anti);self.opieces.append(piece)
            self.ocumulative.append(self.ocumulative[-1]+self._weighted_part(piece,right))
        self.omegaS=self.rat(self.k*self.S)-(self.inverse(first)-self.L)
        self.omegaEnd=self.omegaS+self.ocumulative[-1]
        self.beta=-self.omegaEnd/(self.L-self.rat(self.S+self.width/2))
        assert float(self.beta.x[0])>0 and float(self.beta.x[1])<3
    def _window_scalar(self,z):
        z=self.I(z);lo,hi=float(z.x[0]),float(z.x[1])
        S,b=float(self.S),float(self.width)
        # Crossing a boundary is enclosed by its globally valid Lipschitz bound.
        for boundary,value in [(self.S,0),(self.S+self.width,1)]:
            x=self.rat(boundary)
            if lo<=float(x.x[1]) and hi>=float(x.x[0]):
                gap=(z-x).absolute_upper()
                W=self.I(value)+self.sym(fq(gap)*Q(630,256)/self.width)
                C=self.rat(self.S if value==0 else self.S+self.width/2)+self.sym(fq(gap))
                return W,C
        if hi<float(self.rat(self.S).x[0]):return self.I(0),z
        if lo>float(self.rat(self.S+self.width).x[1]):return self.I(1),self.rat(self.S+self.width/2)
        t=(z-self.rat(self.S))/self.rat(self.width)
        if float((t.x[0]+t.x[1])/2)<=.5:
            small=t;step=self.I(0);integ=self.I(0)
            for factor,power in [(126,5),(-420,6),(540,7),(-315,8),(70,9)]:
                step=step+factor*small**power;integ=integ+self.rat(Q(factor,power+1))*small**(power+1)
            return step,self.rat(self.S)+self.rat(self.width)*(t-integ)
        small=1-t;step=self.I(0);integ=self.I(0)
        for factor,power in [(126,5),(-420,6),(540,7),(-315,8),(70,9)]:
            step=step+factor*small**power;integ=integ+self.rat(Q(factor,power+1))*small**(power+1)
        return 1-step,self.rat(self.S)+self.rat(self.width)*(self.rat(Q(1,2))-integ)
    def _omega_scalar(self,z):
        z=self.I(z);lo,hi=float(z.x[0]),float(z.x[1])
        S,b=float(self.S),float(self.width)
        for boundary,anchor in [(self.S,self.omegaS),(self.S+self.width,self.omegaEnd)]:
            q=self.rat(boundary)
            if lo<=float(q.x[1]) and hi>=float(q.x[0]):
                return anchor+self.sym(fq((z-q).absolute_upper())*(1/self.rho_min+self.k))
        if hi<=S:return self.rat(self.k)*z-(self.inverse(self.L+z)-self.L)
        if lo>=S+b:return self.omegaEnd
        u=self.L+z;mid=float((u.x[0]+u.x[1])/2)
        idx=min(len(self.opieces)-1,max(0,bisect.bisect_right(
            [float((x.x[0]+x.x[1])/2) for x in self.og],mid)-1))
        return self.omegaS+self.ocumulative[idx]+self._weighted_part(self.opieces[idx],u)
    def phase(self,theta):
        theta=self.I(theta);shape=np.shape(theta.x[0])
        flat=self.I(np.ravel(theta.x[0]),np.ravel(theta.x[1]))
        p=self.inverse(flat);kap=self.inverse(flat,1)
        phases=[];curves=[]
        for j in range(np.size(flat.x[0])):
            x=flat.item(j)-self.L;mid=float((x.x[0]+x.x[1])/2)
            sign=-1 if mid<0 else 1;z=sign*x
            W,C=self._window_scalar(z);omega=self._omega_scalar(z)
            phases.append(p.item(j)+self.rat(self.lam)*sign*(omega+self.beta*(z-C)))
            curves.append(kap.item(j)+self.rat(self.lam)*((1-W)*(self.rat(self.k)-kap.item(j))+self.beta*W))
        return (self.I(np.array([float(x.x[0]) for x in phases]).reshape(shape),
                       np.array([float(x.x[1]) for x in phases]).reshape(shape)),
                self.I(np.array([float(x.x[0]) for x in curves]).reshape(shape),
                       np.array([float(x.x[1]) for x in curves]).reshape(shape)))
    def _gauss_rule(self):
        n=12
        p0,p1=[Q(1)],[Q(0),Q(1)]
        for j in range(1,n):
            pp=[Q(0)]+[(2*j+1)*x for x in p1]
            for k,x in enumerate(p0):pp[k]-=j*x
            pp=[x/(j+1) for x in pp];p0,p1=p1,pp
        dp=qder(p1);nodes,weights=np.polynomial.legendre.leggauss(n)
        gaps=[];wgaps=[];brackets=[]
        for x,w in zip(nodes,weights):
            center=fq(x);step=Q(1,2**60)
            while qeval(p1,center-step)*qeval(p1,center+step)>=0:step*=2
            # Exact rational interval polynomial evaluation on the root bracket.
            lo,hi=center-step,center+step
            assert -1<lo<hi<1
            if brackets:assert brackets[-1][1]<lo
            brackets.append((lo,hi))
            def qi(poly):
                a,b=Q(0),Q(0)
                for c in poly[::-1]:
                    vv=[a*lo,a*hi,b*lo,b*hi];a,b=min(vv)+c,max(vv)+c
                return a,b
            dl,dh=qi(dp);assert dl*dh>0
            x2lo=0 if lo<=0<=hi else min(lo*lo,hi*hi);x2hi=max(lo*lo,hi*hi)
            d2lo=min(dl*dl,dh*dh);d2hi=max(dl*dl,dh*dh)
            wl=2/((1-x2lo)*d2hi);wh=2/((1-x2hi)*d2lo)
            gaps.append(step);wgaps.append(max(abs(fq(w)-wl),abs(fq(w)-wh)))
        self.gx,self.gw=nodes,weights
        self.gauss_node_gap=max(gaps);self.gauss_weight_l1=sum(wgaps)
        self.gauss_C=Q(math.factorial(n)**4,(2*n+1)*math.factorial(2*n)**2)

    def curvature_jets(self,theta,known_kappa=None):
        """Scalar-interval kappa, kappa_u, kappa_uu for a small material box."""
        theta=self.I(theta)
        old=self.inverse(theta,1);old_u=self.inverse(theta,2);old_uu=self.inverse(theta,3)
        x=theta-self.L;mid=float((x.x[0]+x.x[1])/2)
        sign=-1 if mid<0 else 1;z=sign*x
        W,_=self._window_scalar(z)
        tl=(z-self.rat(self.S))/self.rat(self.width)
        lo=max(0.,float(tl.x[0]));hi=min(1.,float(tl.x[1]))
        if lo>hi:
            w1,w2=self.I(0),self.I(0)
        else:
            t=self.I(lo,hi)
            w1=sign*630*t**4*(1-t)**4/self.rat(self.width)
            w2=2520*t**3*(1-t)**3*(1-2*t)/self.rat(self.width**2)
            if float(tl.x[0])<0 or float(tl.x[1])>1:
                w1=self.hull(w1,self.I(0));w2=self.hull(w2,self.I(0))
        l=self.rat(self.lam);gap=old-self.rat(self.k)+self.beta
        kk=known_kappa if known_kappa is not None else old+l*((1-W)*(self.rat(self.k)-old)+self.beta*W)
        ku=(1-l*(1-W))*old_u+l*w1*gap
        kuu=(1-l*(1-W))*old_uu+2*l*w1*old_u+l*w2*gap
        return kk,ku,kuu
    def _quad_error(self,length,maxwidth=None):
        length=Q(length);width=length if maxwidth is None else Q(maxwidth)
        analytic=length*2*self.gauss_C*(width/self.R)**24
        rule=length*self.gauss_weight_l1/2+Q(5,2)*length*width*self.gauss_node_gap/2
        return analytic+rule
    def _integrate_position(self,left,right):
        mid=(left+right)/2;half=(right-left)/2
        theta=mid.expand()+half.expand()*self.I(self.gx)
        phi,_=self.phase(theta)
        sin,cos=self.sincos(phi)
        re=(self.I(self.gw)*(-sin)).sum(-1)*half
        im=(self.I(self.gw)*cos).sum(-1)*half
        length=fq((right-left).absolute_upper())
        error=self._quad_error(length)
        return re+self.sym(error),im+self.sym(error)
    def _build_position(self):
        grid=[self.I(0),self.T,self.L]
        for j in range(1,self.count+1):
            x=Q(j,self.cells_per_unit)
            if float(x)<float(self.T.x[0]):grid.append(self.rat(x))
        for x in [self.L-self.rat(self.S+self.width),self.L-self.rat(self.S),
                  self.L+self.rat(self.S),self.L+self.rat(self.S+self.width),
                  self.L-self.rat(self.S+self.width/2),self.L+self.rat(self.S+self.width/2)]:
            grid.append(x)
        grid.sort(key=lambda x:float((x.x[0]+x.x[1])/2))
        assert all(float(a.x[1])<float(b.x[0]) for a,b in zip(grid[:-1],grid[1:]))
        self.pg=grid;self.pc=[(self.I(0),self.I(0))]
        for left,right in zip(grid[:-1],grid[1:]):
            re,im=self._integrate_position(left,right)
            self.pc.append((self.pc[-1][0]+re,self.pc[-1][1]+im))
        st,ct=self.sincos(self.T);dr,di=ct-1,st;den=dr.sq()+di.sq()
        Jr,Ji=self.pc[-1]
        self.origin=(Jr*dr+Ji*di)/den
        # Reflection proves the true normalized origin is real; no float
        # imaginary part is silently discarded.
        self.origin_imag_check=(Ji*dr-Jr*di)/den
        assert float(self.origin_imag_check.x[0])<=0<=float(self.origin_imag_check.x[1])
    def point(self,theta):
        """True F,Ft,Ftt enclosure for a narrow real input interval."""
        theta=self.I(theta);mid=float((theta.x[0]+theta.x[1])/2)
        sector=int(math.floor(mid/(2*math.pi/3)))
        local=theta-sector*self.T
        lm=float((local.x[0]+local.x[1])/2)
        idx=min(len(self.pg)-2,max(0,bisect.bisect_right(
            [float((x.x[0]+x.x[1])/2) for x in self.pg],lm)-1))
        touching=[j for j,x in enumerate(self.pg)
                  if float(local.x[0])<=float(x.x[1]) and float(local.x[1])>=float(x.x[0])]
        if touching:
            j=touching[0];gap=fq((local-self.pg[j]).absolute_upper())
            zr=self.origin+self.pc[j][0]+self.sym(gap)
            zi=self.pc[j][1]+self.sym(gap)
        else:
            re,im=self._integrate_position(self.pg[idx],local)
            zr=self.origin+self.pc[idx][0]+re;zi=self.pc[idx][1]+im
        phi,kap=self.phase(local);ss,cc=self.sincos(phi+sector*self.T)
        rs,rc=self.sincos(sector*self.T)
        kap,ku,kuu=self.curvature_jets(local,kap)
        F=[zr*rc-zi*rs,zr*rs+zi*rc,self.I(0)]
        Ft=[-ss,cc,self.I(0)];Ftt=[-kap*cc,-kap*ss,self.I(0)]
        Fttt=[-ku*cc+kap.sq()*ss,-ku*ss-kap.sq()*cc,self.I(0)]
        Ftttt=[(kap**3-kuu)*cc+3*kap*ku*ss,(kap**3-kuu)*ss-3*kap*ku*cc,self.I(0)]
        return {"F":F,"Ft":Ft,"Ftt":Ftt,"Fttt":Fttt,"Ftttt":Ftttt,
                "phi":phi+sector*self.T,"kappa":kap,"kappa_u":ku,"kappa_uu":kuu}

    def all_angle_curvature_bounds(self):
        """Continuous range on the complete true sector, including both limits."""
        out={key:0. for key in ("kappa","kappa_u","kappa_uu","Gamma3","Gamma4")}
        for left,right in zip(self.pg[:-1],self.pg[1:]):
            box=self.I(float(left.x[0]),float(right.x[1]))
            k,ku,kuu=self.curvature_jets(box)
            for key,val in (("kappa",k),("kappa_u",ku),("kappa_uu",kuu)):
                out[key]=max(out[key],val.absolute_upper())
            g3=(ku.sq()+k**4).sqrt()
            g4=((k**3-kuu).sq()+9*k.sq()*ku.sq()).sqrt()
            out["Gamma3"]=max(out["Gamma3"],g3.absolute_upper())
            out["Gamma4"]=max(out["Gamma4"],g4.absolute_upper())
        return out

