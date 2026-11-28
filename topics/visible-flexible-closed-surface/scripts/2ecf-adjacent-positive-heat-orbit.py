#!/usr/bin/env python3
"""A positive planar inverse-curvature heat orbit with an exact physical inlet and a compensated radial height."""
import numpy as np
from scipy.fft import dct
from numpy.polynomial import chebyshev as Ch

def S5(t):
    t=np.clip(t,0.,1.)
    return t**3*(10+t*(-15+6*t))

def step(x,lo,hi):
    z=np.clip((x-lo)/(hi-lo),0,1);d=hi-lo
    return S5(z),30*z**2*(1-z)**2/d,60*z*(1-z)*(1-2*z)/d**2

class HeatOrbit:
    def __init__(self,phys,geo,a,src,api,theta,order,height_order,amplitude,late):
        self.c=a.full_sleeve;self.d=a.full_gate;self.anchor=a.anchor;self.amplitude=amplitude;self.late=late
        self.half=phys.HALF;self.period=phys.PERIOD;self.theta=theta;self.u=src.center.arc(theta)
        orig,diff,self.sp=api.central_delta(src,geo,None,theta,1.,a.anchor)
        self.uu=np.sum(orig[1]*orig[2],axis=-1)/self.sp
        self.true=orig+diff;self.api=api
        j=np.arange(1,2*order-1);self.n=3*j
        tri=1-abs(np.arange(-order+1,order))/order
        filt=np.convolve(tri,tri);wt=filt[len(filt)//2+j]/filt[len(filt)//2]
        gx,gw=np.polynomial.legendre.leggauss(12)
        r=np.zeros(len(j))
        for le,re in zip((0,phys.V0,phys.V1),(phys.V0,phys.V1,self.half)):
            cells=max(1,int(np.ceil((re-le)*self.n[-1]/2)))
            br=np.linspace(le,re,cells+1);t=(br[:-1,None]+np.diff(br)[:,None]*(1+gx)/2).ravel()
            q=(np.diff(br)[:,None]*gw/2).ravel()
            b=phys.sw((t-phys.V0)/(phys.V1-phys.V0))
            radius=(1-b)/phys.LOW+b*geo.scale*phys.base_radius(t)
            r+=2/self.half*((q*radius)@np.cos(t[:,None]*self.n))
        self.co=wt*r
        p=self.packet(0.)
        self.delta=np.stack((self.true[0]-api.xyz(p[0]),self.true[1]-api.xyz(p[1]*self.sp),
                             self.true[2]-api.xyz(p[2]*self.sp**2+p[1]*self.uu)))
        # The radial polynomial interpolates the smooth divided vertical speed,
        # explicitly multiplying by tau_q squared to keep the exact inlet jets.
        xs=np.cos(np.pi*np.arange(height_order+1)/height_order)
        L=[]
        for x in xs:
            t,t1,_=self.clock(self.c+self.d*(x+1)/2)
            _,_,_,_,_,_,rad,ru,ruu=self.packet(t)
            h2=1-t1**2*rad**2
            if min(h2)<=0:raise ValueError('Prescribed physical meridian speed is outside the positive real domain')
            h=np.sqrt(h2)
            L.append(np.stack((-rad**2/(1+h),-rad*ru/h,-(ru**2+rad*ruu)/h-t1**2*rad**2*ru**2/h**3)))
        coeff=dct(np.asarray(L),type=1,axis=0)/height_order;coeff[[0,-1]]/=2
        # On [-1,1], tau_q = A*30*(1-x^2)^2/(16*d).
        qpoly=np.array([1.,0.,-2.,0.,1.])*amplitude*30/(16*self.d)
        mpoly=Ch.chebmul(Ch.poly2cheb(qpoly),Ch.poly2cheb(qpoly))
        W=np.zeros((height_order+9,height_order+1))
        for n in range(height_order+1):
            basis=np.eye(1,height_order+1,n).ravel()
            b=Ch.chebmul(mpoly,basis);W[:len(b),n]=b
        self.hc=np.einsum('ij,jkl->ikl',W,coeff)
        self.hd=Ch.chebder(self.hc,axis=0)*2/self.d
        self.hi=Ch.chebint(self.hc,axis=0,lbnd=-1)*self.d/2
    def clock(self,q):
        s,s1,s2=step(q,self.c,self.c+self.d)
        return self.amplitude*s,self.amplitude*s1,self.amplitude*s2
    def packet(self,tau):
        e=np.exp(tau);n=self.n
        coef=self.co*np.exp(-n*n*tau)
        # Only terms that underflow to exact binary zero are omitted.
        active=coef!=0;n=n[active];coef=coef[active];hcoef=coef/(1-n*n)
        k=np.floor((self.u+self.anchor+self.half)/self.period)
        u=self.u+self.anchor-k*self.period
        lo=np.full_like(u,-self.half);hi=-lo;v=u.copy()
        for _ in range(48):
            co=np.cos(v[:,None]*n);si=np.sin(v[:,None]*n)
            r=1+co@coef
            err=v+si@(coef/n)-u
            done=abs(err)<5e-15
            if np.all(done):break
            lo=np.where(err<0,v,lo);hi=np.where(err>0,v,hi);p=v-err/r
            v=np.where(done,v,np.where((p>lo)&(p<hi),p,(lo+hi)/2))
        else:raise ArithmeticError('Positive spectral radius: area-clock inverse did not converge')
        if r.min()<=0:raise ArithmeticError('Nonpositive heat radius')
        normal=np.exp(1j*(v+k*self.period-self.anchor));tan=1j*normal
        rr=e*r;rp=-e*(si@(n*coef));rpp=-e*(co@(n*n*coef))
        H=e*(1+co@hcoef);Hp=-e*(si@(n*hcoef))
        P=H*normal+Hp*tan
        Pu=e*tan;Puu=-e**2/rr*normal
        Pt=rr*normal
        Ptu=e*(tan+rp/rr*normal)
        Ptt=(rr+rpp-rp**2/rr)*normal-rp*tan
        ru=e*rp/rr;ruu=e**2*(rpp/rr**2-rp**2/rr**3)
        return P,Pu,Puu,Pt,Ptu,Ptt,rr,ru,ruu
    def jets(self,q):
        J=np.zeros((len(q),6,len(self.u),3))
        for i,s in enumerate(q):
            tau,t1,t2=self.clock(s)
            p,pu,puu,pt,ptu,ptt,*_=self.packet(tau)
            xy=(p,t1*pt,pu*self.sp,t1**2*ptt+t2*pt,t1*ptu*self.sp,puu*self.sp**2+pu*self.uu)
            for c,v in enumerate(xy):J[i,c]=self.api.xyz(v)
            g,g1,g2=step(s,self.c,self.c+self.d)
            for j,(r,d) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
                J[i,j]+=(1-g,-g1,-g2)[r]*self.delta[d]
            x=2*(s-self.c)/self.d-1
            zi=Ch.chebval(x,self.hi);zh=Ch.chebval(x,self.hc);zd=Ch.chebval(x,self.hd)
            J[i,0,:,2]=s+zi[0];J[i,1,:,2]=1+zh[0];J[i,2,:,2]=zi[1]*self.sp
            J[i,3,:,2]=zd[0];J[i,4,:,2]=zh[1]*self.sp;J[i,5,:,2]=zi[2]*self.sp**2+zi[1]*self.uu
        return J
    def correction(self,q,base):
        D=np.zeros_like(base);take=(q>self.c)&(q<self.c+self.d)
        if not np.any(take):return D
        x=q[take];h=self.jets(x)-base[take]
        b,b1,b2=step(x,self.c+self.late*self.d,self.c+self.d)
        y=(1-b)[:,None,None,None]*h
        y[:,1]-=b1[:,None,None]*h[:,0]
        y[:,3]-=2*b1[:,None,None]*h[:,1]+b2[:,None,None]*h[:,0]
        y[:,4]-=b1[:,None,None]*h[:,2]
        D[take]=y
        return D
