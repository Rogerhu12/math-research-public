#!/usr/bin/env python3
"""m3 full-circle interval Taylor enclosure of the analytic core lift.

The core is defined by its finite support coefficients and the unique inverse
of its strictly increasing arclength function. Root enclosures are validated
by strict interval signs at two endpoints, independently of findroot success.
Only one-dimensional angular second derivatives enter the Taylor remainders.
"""
import math
import numpy as np
import mpmath as mp
from interval_geometry_kernel import exact,add,mul,scale,square,div,dn,up,stack

H=[[1,0,0,-10,15,-6],[0,1,0,-6,8,-3],[0,0,.5,-1.5,1.5,-.5]]

def lower(x):return mp.make_mpf(x._mpi_[0])
def upper(x):return mp.make_mpf(x._mpi_[1])
def midpoint(x):return (lower(x)+upper(x))/2
def to_float(x):return float(dn(float(lower(x)))),float(up(float(upper(x))))

class CoreLiftIntervals:
    def __init__(self,data,N):
        mp.mp.dps=80;mp.iv.dps=70
        self.iv=mp.iv;self.N=N
        self.coeff=[mp.mpf(float(x))for x in data['core_coefficients']]
        self.freq=[int(x)for x in data['core_frequencies']]
        self.odd=[int(x)for x in data['odd']];self.even=[int(x)for x in data['even']]
        self.iz=2*len(self.odd)
        self.jets=[[mp.mpf(float(v))for v in row]for row in data['jets'][:,:,0]]
        self.E0=mp.mpf(float(data['chart_E0']));self.Epp=mp.mpf(float(data['chart_Epp']))
        assert abs(self.E0)<1
        rho_lower=mp.iv.mpf(1)
        for c,m in zip(self.coeff,self.freq):rho_lower-=abs(mp.iv.mpf((1-m*m)*c))
        assert lower(rho_lower)>mp.mpf('0.3')
        self.rho_lower=to_float(rho_lower)[0]
        self.bracket_checks=0

    def arc(self,phi):
        out=phi
        for c,m in zip(self.coeff,self.freq):out+=self.iv.mpf(c)*(1-m*m)/m*self.iv.sin(m*phi)
        return out

    def theta(self,psi):return psi-self.iv.mpf(self.E0)*self.iv.sin(3*psi)/3

    def phi_point(self,psi):
        theta=self.theta(psi);target=midpoint(theta)
        def f(phi):
            return phi+sum(c*(1-m*m)*mp.sin(m*phi)/m for c,m in zip(self.coeff,self.freq))-target
        root=mp.findroot(f,target,tol=mp.mpf('1e-68'),maxsteps=60)
        eps=mp.mpf('1e-45');lo=root-eps;hi=root+eps
        left=self.arc(self.iv.mpf(lo));right=self.arc(self.iv.mpf(hi))
        assert upper(left)<lower(theta) and lower(right)>upper(theta)
        self.bracket_checks+=1
        return self.iv.mpf([lo,hi])

    def tensor_start(self,psi,order):
        iv=self.iv;out=[]
        for c in self.jets:
            X=iv.mpf(0);Y=iv.mpf(0);Z=iv.mpf(c[self.iz])if order==0 else iv.mpf(0)
            for j,k in enumerate(self.odd):
                if order==0:bx=iv.cos(k*psi);by=iv.sin(k*psi)
                elif order==1:bx=-k*iv.sin(k*psi);by=k*iv.cos(k*psi)
                else:bx=-k*k*iv.cos(k*psi);by=-k*k*iv.sin(k*psi)
                X+=iv.mpf(c[j])*bx;Y+=iv.mpf(c[len(self.odd)+j])*by
            for j,k in enumerate(self.even):
                b=iv.cos(k*psi)if order==0 else(-k*iv.sin(k*psi)if order==1 else-k*k*iv.cos(k*psi))
                Z+=iv.mpf(c[self.iz+1+j])*b
            out.append([X,Y,Z])
        return out

    def delta(self,psi,phi,order):
        iv=self.iv
        h=iv.mpf(1);hp=iv.mpf(0);rho=iv.mpf(1);rhop=iv.mpf(0)
        for c,m in zip(self.coeff,self.freq):
            cc=iv.mpf(c);co=iv.cos(m*phi);si=iv.sin(m*phi)
            h+=cc*co;hp-=m*cc*si;rho+=(1-m*m)*cc*co;rhop-=m*(1-m*m)*cc*si
        assert lower(rho)>0
        er=[iv.cos(phi),iv.sin(phi),iv.mpf(0)]
        et=[-iv.sin(phi),iv.cos(phi),iv.mpf(0)]
        gamma=[h*x+hp*y for x,y in zip(er,et)]
        gt=et;gtt=[-x/rho for x in er]
        gttt=[-y/rho**2+x*rhop/rho**3 for x,y in zip(er,et)]
        r=1-iv.mpf(self.E0)*iv.cos(3*psi);rp=3*iv.mpf(self.E0)*iv.sin(3*psi)
        b=-iv.mpf(self.Epp)*iv.sin(3*psi)/3
        bp=-iv.mpf(self.Epp)*iv.cos(3*psi);bpp=3*iv.mpf(self.Epp)*iv.sin(3*psi)
        zero=[iv.mpf(0)]*3
        if order==0:target=[gamma,[iv.mpf(0),iv.mpf(0),iv.mpf(1)],[b*x for x in gt]]
        elif order==1:target=[[r*x for x in gt],zero,[bp*x+b*r*y for x,y in zip(gt,gtt)]]
        else:target=[[r*r*y+rp*x for x,y in zip(gt,gtt)],zero,
            [bpp*x+(2*bp*r+b*rp)*y+b*r*r*z for x,y,z in zip(gt,gtt,gttt)]]
        before=self.tensor_start(psi,order)
        return [[x-y for x,y in zip(row,old)]for row,old in zip(target,before)]

    def all_boxes(self):
        N=self.N;out0=np.empty((3,3,N,3));out1=np.empty_like(out0)
        max_center_delta=np.zeros((2,3));max_uniform_second=np.zeros(3)
        for j in range(N):
            pl=2*self.iv.pi*j/N;pr=2*self.iv.pi*(j+1)/N
            pc=self.iv.pi*(2*j+1)/N
            fl=self.phi_point(pl);fr=self.phi_point(pr);fc=self.phi_point(pc)
            psi=self.iv.mpf([lower(pl),upper(pr)]);phi=self.iv.mpf([lower(fl),upper(fr)])
            c0=self.delta(pc,fc,0);c1=self.delta(pc,fc,1);whole2=self.delta(psi,phi,2)
            width=up(float((upper(pr)-lower(pl))/2));t=(-width,width);t2=square(t)
            for k in range(3):
                for axis in range(3):
                    d0=to_float(c0[k][axis]);d1=to_float(c1[k][axis]);d2=to_float(whole2[k][axis])
                    ranges=[add(add(d0,mul(t,d1)),scale(mul(t2,d2),.5)),add(d1,mul(t,d2)),d2]
                    for derivative,z in enumerate(ranges):out0[derivative,k,j,axis]=z[0];out1[derivative,k,j,axis]=z[1]
                    max_center_delta[0,k]=max(max_center_delta[0,k],abs(d0[0]),abs(d0[1]))
                    max_center_delta[1,k]=max(max_center_delta[1,k],abs(d1[0]),abs(d1[1]))
                    max_uniform_second[k]=max(max_uniform_second[k],abs(d2[0]),abs(d2[1]))
            if j%64==0:
                print(__import__('json').dumps(dict(event='center_interval_angles',done=j+1,total=N)),flush=True)
        return (out0,out1),dict(core_rho_lower=self.rho_lower,validated_inverse_brackets=self.bracket_checks,
            center_delta_abs_bounds=max_center_delta.tolist(),whole_box_delta_second_abs_bounds=max_uniform_second.tolist(),
            arithmetic='70-digit interval elementary functions; inverse brackets independently sign-verified; second-order interval Taylor remainders.')

def lift_weights(low,high,width,derivative):
    active=low<width
    if not np.any(active):return exact(np.zeros((len(low),3)))
    t=div((np.clip(low,0,width),np.clip(high,0,width)),exact(width))
    result=[]
    for j,c in enumerate(H):
        # Coefficients include 1/2; factorial multiplication is done before
        # ordinary division. All resulting small half-integers are exact.
        d=[c[k]*(math.factorial(k)/math.factorial(k-derivative))for k in range(derivative,len(c))]
        v=exact(np.zeros(len(low)))
        for coeff in d[::-1]:v=add(mul(v,t),exact(coeff))
        power=j-derivative;factor=exact(1.)
        for k in range(abs(power)):
            factor=scale(factor,width)if power>0 else div(factor,exact(width))
        v=mul(v,factor)
        v=(np.where(active,v[0],0),np.where(active,v[1],0))
        if np.any(high>width):v=(np.where(high>width,np.minimum(v[0],0),v[0]),np.where(high>width,np.maximum(v[1],0),v[1]))
        result.append(v)
    return stack(result,-1)

def add_center_correction(fields,low,high,width,delta):
    if not np.any(low<width):return fields
    weights=[lift_weights(low,high,width,j)for j in range(3)]
    for n,(radial,angular)in enumerate([(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)]):
        correction=exact(np.zeros_like(fields[n][0]));w=weights[radial]
        for j in range(3):
            z=(delta[0][angular,j][None,:,:],delta[1][angular,j][None,:,:])
            factor=(w[0][:,j,None,None],w[1][:,j,None,None])
            correction=add(correction,mul(factor,z))
        fields[n]=add(fields[n],correction)
    return fields
