#!/usr/bin/env python3
"""Full radial-polynomial/Laurent algebra for the actual Cartesian prefix.

The finite functions are the input shared-two-jet quintics.  A second
shared-jet quintic is an auxiliary radius only; the driver separately pays
its difference from the unchanged physical reference metric.  No angular
sampling or pointwise radial extrapolation appears in this module.
"""
from fractions import Fraction as Q
import math
import numpy as np
from interval_tail_metric import (exact,add,sub,neg,mul,scale,div,square,dn,up,
    rational_interval,convolution,reverse,l1_upper,bernstein_range)


def rational_float(x):
    """Tight binary64 interval for an exact rational, including exact zeros."""
    x=Q(x);y=float(x);z=Q.from_float(y)
    return (math.nextafter(y,-math.inf) if z>x else y,
            math.nextafter(y,math.inf) if z<x else y)


def quintic_powers(knots,jets):
    """Exact-rational power coefficients; local variable t=(s-left)/h.

    Endpoint subtraction is done before conversion to binary64.  This
    avoids a spurious u/h error in the unusually short inserted spans.
    """
    y=np.asarray(jets,float)
    assert y.ndim==3 and y.shape[0]==3 and y.shape[2]==len(knots)
    out=np.empty((2,6,y.shape[1],len(knots)-1))
    for i in range(len(knots)-1):
        h=Q.from_float(float(knots[i+1]))-Q.from_float(float(knots[i]))
        for k in range(y.shape[1]):
            y0,d0,q0=[Q.from_float(float(y[j,k,i]))for j in range(3)]
            y1,d1,q1=[Q.from_float(float(y[j,k,i+1]))for j in range(3)]
            e0=y1-y0-h*d0-h*h*q0/2
            e1=h*(d1-d0)-h*h*q0
            e2=h*h*(q1-q0)
            c=[y0,h*d0,h*h*q0/2,10*e0-4*e1+e2/2,
                -15*e0+7*e1-e2,6*e0-3*e1+e2/2]
            for j,v in enumerate(c):out[:,j,k,i]=rational_float(v)
    return out[0],out[1]


def ppad(a,degree,length):
    assert length>=a[0].shape[1] and (length-a[0].shape[1])%2==0
    pad=(length-a[0].shape[1])//2
    return tuple(np.pad(v,((0,degree+1-v.shape[0]),(pad,pad)))for v in a)


def zero_pair(shape):return np.zeros(shape),np.zeros(shape)


def padd(a,b):
    d=max(a[0].shape[0],b[0].shape[0])-1
    n=max(a[0].shape[1],b[0].shape[1])
    return add(ppad(a,d,n),ppad(b,d,n))


def psub(a,b):return padd(a,neg(b))


def pmul(a,b):
    """Exact polynomial multiplication enclosed by outward finite convolutions."""
    d=a[0].shape[0]+b[0].shape[0]-1
    n=a[0].shape[1]+b[0].shape[1]-1
    out=zero_pair((d,n))
    for i in range(a[0].shape[0]):
        ai=(a[0][i],a[1][i])
        for j in range(b[0].shape[0]):
            v=convolution(ai,(b[0][j],b[1][j]))
            out[0][i+j],out[1][i+j]=add((out[0][i+j],out[1][i+j]),v)
    return out


def prev(a):return a[0][:,::-1],a[1][:,::-1]


def pderivative(a,h):
    n=a[0].shape[0]
    return div(scale((a[0][1:],a[1][1:]),np.arange(1,n)[:,None]),rational_interval(h))


def polynomial_l1_range(a,lo=Q(0),hi=Q(1)):
    """All-angle coefficient l1 after exact local radial restriction.

    Power coefficients are converted to Bernstein once; convexity then
    encloses every radial value, without a mesh of evaluation points.
    """
    degree=a[0].shape[0]-1
    bs=[]
    for k in range(degree+1):
        v=exact(np.zeros(a[0].shape[1]))
        for j in range(k+1):
            v=add(v,mul((a[0][j],a[1][j]),rational_interval(Q(math.comb(k,j),math.comb(degree,j)))))
        bs.append(v)
    return l1_upper(bernstein_range(bs,lo,hi))


def prefix_numerators(cartesian,phase,radius,h,planar_modes,height_modes):
    """Return A,B,C for g5=ds^2+a5(s)^2 dtheta^2 in local radial powers.

    rho=1-e*cos(3psi), theta_s=-e_s*sin(3psi)/3;
    Y=rho*X_s-theta_s*X_psi.  A=|Y|^2-rho^2,
    B=Y.X_psi, C=|X_psi|^2-a5^2*rho^2.  B stores imaginary
    Laurent coefficients; A,C are real.  All frequencies and products
    are retained, including those introduced by clearing rho.
    """
    pm=np.asarray(planar_modes);hm=np.asarray(height_modes)
    assert np.all((pm-1)%3==0) and np.all(hm%3==0)
    K=max(int(np.max(abs((pm-1)//3))),int(np.max(hm//3)))
    n=2*K+1;P=len(pm)
    p=zero_pair((6,n));z=zero_pair((6,n))
    p[0][:,(pm-1)//3+K]=cartesian[0][:,:P]
    p[1][:,(pm-1)//3+K]=cartesian[1][:,:P]
    for j,k in enumerate(hm//3):
        v=(cartesian[0][:,P+j],cartesian[1][:,P+j])
        if k:v=scale(v,.5)
        z[0][:,K+k],z[1][:,K+k]=v
        if k:z[0][:,K-k],z[1][:,K-k]=v
    a=pderivative(p,h);zr=pderivative(z,h)
    frequency=3*np.arange(-K,K+1)
    b=scale(p,1+frequency[None,:]);zt=scale(z,frequency[None,:])
    e=phase;ep=pderivative(e,h)
    rho=zero_pair((6,3))
    rho[0][:,0],rho[1][:,0]=scale((e[0][:,0],e[1][:,0]),-.5)
    rho[0][:,2],rho[1][:,2]=scale((e[0][:,0],e[1][:,0]),-.5)
    rho[0][0,1]=rho[1][0,1]=1.
    # theta_s=i*T, with T_{-1}=-e_s/6,T_{+1}=e_s/6.
    T=zero_pair((5,3))
    T[0][:,0],T[1][:,0]=mul((ep[0][:,0],ep[1][:,0]),rational_interval(Q(-1,6)))
    T[0][:,2],T[1][:,2]=mul((ep[0][:,0],ep[1][:,0]),rational_interval(Q(1,6)))
    yp=padd(pmul(rho,a),pmul(T,b))
    yz=padd(pmul(rho,zr),pmul(T,zt))
    rho2=pmul(rho,rho)
    A=psub(padd(pmul(yp,prev(yp)),pmul(yz,yz)),rho2)
    cross=pmul(yp,prev(b))
    B=padd(scale(psub(cross,prev(cross)),-.5),pmul(yz,zt))
    C=psub(psub(pmul(b,prev(b)),pmul(zt,zt)),pmul(pmul(radius,radius),rho2))
    return (A,B,C),dict(maximum_angular_frequency=max(v[0].shape[1]//2*3 for v in [A,B,C]),
                       maximum_radial_degree=max(v[0].shape[0]-1 for v in [A,B,C]))
