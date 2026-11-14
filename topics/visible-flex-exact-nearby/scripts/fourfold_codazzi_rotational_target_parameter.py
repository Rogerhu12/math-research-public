#!/usr/bin/env python3
"""Analytic floating parameter differential of the actual rotational target.

Differentiate the saved affine family before scalar operations/FFT and use
the true natural-graft formula. The values are floating diagnostics, with
no interval tail or ODE certificate asserted by this provider.
"""
from __future__ import annotations
import math
import numpy as np
from numpy.polynomial import Polynomial
from fourfold_phase_geometry import tangent_radial_jets,tangent_variation_jets
from fourfold_phase_codazzi_rotational_reference_probe import primitive_difference


def reciprocal(series,n):
    series=np.asarray(series);out=np.zeros(n);out[0]=1/series[0]
    for j in range(1,n):out[j]=-sum(series[k]*out[j-k] for k in range(1,min(j+1,len(series))))/series[0]
    return out


def multiply(*series,n):
    out=np.array([1.])
    for x in series:out=np.convolve(out,x)[:n]
    return np.pad(out,(0,max(0,n-len(out))))[:n]


def paired_coefficients(geometry,phase,dphase,a,da,L,dL,Lp,dLp,H,dH,Hp,dHp):
    """Value and exact differential of the finite-primitive scalar formula."""
    a,da,L,dL,Lp,dLp,H,dH,Hp,dHp=map(np.atleast_1d,(a,da,L,dL,Lp,dLp,H,dH,Hp,dHp))
    p=primitive_difference(geometry,phase)
    _,aux=tangent_radial_jets(phase,geometry.sine)
    dp=geometry.primitive_coefficients(tangent_variation_jets(aux,dphase,geometry.sine))
    dp[:,:,0,1:]=0.;pos=np.arange(1,geometry.nodes//2)
    for j,parity in enumerate((1,-1,1)):
        z=(dp[:,:,pos,j]+parity*dp[:,:,-pos,j])/2
        dp[:,:,pos,j]=z;dp[:,:,-pos,j]=parity*z
    xx=lambda x:x[:,None,None]
    u=xx(L)*p[0]+p[1]
    du=xx(dL)*p[0]+xx(L)*dp[0]+dp[1]
    ur=xx(Lp)*p[0]+xx(L)*p[1]+p[2]
    dur=xx(dLp)*p[0]+xx(Lp)*dp[0]+xx(dL)*p[1]+xx(L)*dp[1]+dp[2]
    rev=(-np.arange(geometry.nodes))%geometry.nodes
    prod=lambda x,y:np.sum(x*y[:,rev,:],axis=(1,2)).real
    e=(2*L*u[:,0,0]).real+prod(u,u)
    de=(2*dL*u[:,0,0]+2*L*du[:,0,0]).real+2*prod(u,du)
    er=(2*Lp*u[:,0,0]+2*L*ur[:,0,0]).real+2*prod(u,ur)
    der=(2*dLp*u[:,0,0]+2*Lp*du[:,0,0]+2*dL*ur[:,0,0]+2*L*dur[:,0,0]).real+2*prod(du,ur)+2*prod(u,dur)
    E=L*L+a*a*H*H+e
    dE=2*L*dL+2*a*da*H*H+2*a*a*H*dH+de
    R=H*H+e/(a*a);dR=2*H*dH+de/(a*a)-2*e*da/(a**3)
    N=H*H*(L*L-Lp)+L*H*Hp+(L*er-2*Lp*e)/(2*a*a)
    dN=(2*H*dH*(L*L-Lp)+H*H*(2*L*dL-dLp)+dL*H*Hp+L*dH*Hp+L*H*dHp
        +(dL*er+L*der-2*dLp*e-2*Lp*de)/(2*a*a)-(L*er-2*Lp*e)*da/(a**3))
    if np.any(E<=0) or np.any(R<=0):raise ValueError('floating target chart left its positive radial-slope domain')
    K=N/(E*E);dK=dN/(E*E)-2*K*dE/E
    gamma=np.sqrt(E);dgamma=dE/(2*gamma)
    C=-np.sqrt(R/E);dC=C*(dR/R-dE/E)/2
    lam=K*E/R;dlam=(dK*E+K*dE)/R-lam*dR/R
    value=dict(a=a,beta=L,gamma=gamma,K=K,Cref=C,lambda_ref=lam,Ebar=E,R=R)
    derivative=dict(a=da,beta=dL,gamma=dgamma,K=dK,Cref=dC,lambda_ref=dlam,Ebar=dE,R=dR)
    if not all(np.all(np.isfinite(x)) for x in [*value.values(),*derivative.values()]):raise ValueError('nonfinite exact floating parameter differential')
    return value,derivative


class RotationalTargetParameter:
    def __init__(self,geometry):
        self.geometry=geometry
        q=geometry.profile_jets([3.],5)
        divisor=np.array([math.factorial(j) for j in range(6)])
        radius=q['mean'][:,0,0]/divisor;dradius=q['mean_parameter'][:,0,0]/divisor
        zr=q['mean'][1:,0,2]/divisor[:-1];dzr=q['mean_parameter'][1:,0,2]/divisor[:-1]
        ia=reciprocal(radius,6);dl=multiply(dradius,ia,n=5)
        l=np.zeros(5);l[0]=np.log(radius[0])
        deriv=np.arange(1,6)*radius[1:]
        l[1:]=multiply(deriv,ia,n=4)/np.arange(1,5)
        H=multiply(zr,ia,ia,n=4)
        dH=multiply(dzr,ia,ia,n=4)-2*multiply(zr,dradius,ia,ia,ia,n=4)
        s=Polynomial([0.,1.]);z=8*s
        chi=(1-z)**5*(1+5*z+15*z*z+35*z**3+70*z**4)
        self.loga=Polynomial(l[:2])+chi*Polynomial([0.,0.,*l[2:]])
        self.dloga=Polynomial(dl[:2])+chi*Polynomial([0.,0.,*dl[2:]])
        self.H=Polynomial([H[0]])+chi*Polynomial([0.,*H[1:]])
        self.dH=Polynomial([dH[0]])+chi*Polynomial([0.,*dH[1:]])
        self.phases=[];self.dphases=[]
        for component,power in enumerate((3,2)):
            row=[];drow=[]
            for k in range(geometry.modes):
                phase=q['phase'][:5,0,k,component]/divisor[:5]
                dphase=q['phase_parameter'][:5,0,k,component]/divisor[:5]
                invpower=multiply(*([ia]*power),n=5)
                norm=multiply(phase,invpower,n=5)
                dnorm=multiply(dphase,invpower,n=5)-power*multiply(phase,dradius,invpower,ia,n=5)
                row.append(chi*Polynomial(norm));drow.append(chi*Polynomial(dnorm))
            self.phases.append(row);self.dphases.append(drow)
        self.omega=-l[1]/(4*H[0]);self.domega=self.omega*(dl[1]/l[1]-dH[0]/H[0])
        self.a_endpoint=np.exp(self.loga(.125));self.da_endpoint=self.a_endpoint*self.dloga(.125)

    def body(self,r):
        r=np.atleast_1d(np.asarray(r,dtype=float))
        if np.any(r<0) or np.any(r>3):raise ValueError('body spline extrapolation forbidden')
        q=self.geometry.profile_jets(r,2);mean=q['mean'];dm=q['mean_parameter']
        a,ar,arr=mean[:3,:,0];da,dar,darr=dm[:3,:,0]
        zr,zrr=mean[1:3,:,2];dzr,dzrr=dm[1:3,:,2]
        L=ar/a;dL=(dar-L*da)/a
        Lp=arr/a-L*L;dLp=darr/a-arr*da/(a*a)-2*L*dL
        H=zr/(a*a);dH=dzr/(a*a)-2*H*da/a
        Hp=zrr/(a*a)-2*L*H;dHp=dzrr/(a*a)-2*zrr*da/(a**3)-2*dL*H-2*L*dH
        return paired_coefficients(self.geometry,q['phase'],q['phase_parameter'],a,da,L,dL,Lp,dLp,H,dH,Hp,dHp)

    def graft(self,r):
        r=float(r)
        if not 3<=r<=3.125:raise ValueError('outside actual natural graft')
        s=r-3;a=np.exp(self.loga(s));dl=self.dloga(s);da=a*dl
        L=self.loga.deriv()(s);dL=self.dloga.deriv()(s)
        Lp=self.loga.deriv(2)(s);dLp=self.dloga.deriv(2)(s)
        H=self.H(s);dH=self.dH(s);Hp=self.H.deriv()(s);dHp=self.dH.deriv()(s)
        phase=np.zeros((3,1,self.geometry.modes,2));dphase=np.zeros_like(phase)
        for component,power in enumerate((3,2)):
            for k,(poly,dpoly) in enumerate(zip(self.phases[component],self.dphases[component])):
                u,ur,urr=poly(s),poly.deriv()(s),poly.deriv(2)(s)
                du,dur,durr=dpoly(s),dpoly.deriv()(s),dpoly.deriv(2)(s)
                weight=a**power;f1=ur+power*L*u
                df1=dur+power*(dL*u+L*du)
                f2=urr+2*power*L*ur+(power*power*L*L+power*Lp)*u
                df2=durr+2*power*(dL*ur+L*dur)+(2*power*power*L*dL+power*dLp)*u+(power*power*L*L+power*Lp)*du
                phase[:,0,k,component]=weight*np.array([u,f1,f2])
                dphase[:,0,k,component]=weight*np.array([du+power*dl*u,df1+power*dl*f1,df2+power*dl*f2])
        return paired_coefficients(self.geometry,phase,dphase,a,da,L,dL,Lp,dLp,H,dH,Hp,dHp)

    def point(self,r):
        value,derivative=self.body([r]) if r<=3 else self.graft(r)
        return ({k:float(v[0]) for k,v in value.items()},
                {k:float(v[0]) for k,v in derivative.items()})

    def regular_q4_pair(self):
        w=self.a_endpoint/(4*self.omega)
        dw=w*(self.da_endpoint/self.a_endpoint-self.domega/self.omega)
        q=1/np.sqrt(1+w*w);dq=-w*dw/(1+w*w)**1.5
        return q,dq
