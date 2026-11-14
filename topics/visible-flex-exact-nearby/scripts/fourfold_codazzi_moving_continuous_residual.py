#!/usr/bin/env python3
"""Directed all-mode residual algebra for the finite moving-angle candidate.

The complete degree-2M primitive precedes every degree-3M product. The
true mean V0 is extracted before sampling and is never removed from the
principal coupling. Radial scalar-model remainders and every dyadic
candidate coefficient remain in the A0 error budget. This kernel does not
certify an inverse, a nonlinear solution, or any closed-surface criterion.
"""
from __future__ import annotations
import numpy as np
from flint import arb
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    BudgetPolynomial,scalar_budget,zeros,CBox,Box,wiener_upper,exact_arb,
    full_residual_norm,arb_box,evaluate)


def primitive_polynomial(poly,N,degree,fft):
    """Mean-zero fourfold primitive, with exact support and A0 norm <=1/4."""
    length=len(poly.coefficients);block=zeros((N,length))
    for j,value in enumerate(poly.coefficients):block[:,j]=CBox(value)
    coefficients=fft.fft(block)/N
    modes=np.asarray([j if j<N//2 else j-N for j in range(N)])
    outside=abs(modes)>degree
    if not (np.all((coefficients.real.lo[outside]<=0)&(coefficients.real.hi[outside]>=0))
        and np.all((coefficients.imag.lo[outside]<=0)&(coefficients.imag.hi[outside]>=0))):
        raise ValueError('the exact complete primitive support lost its zero enclosure')
    coefficients[outside]=0;coefficients[0]=0
    # 1/(i*4*k)=-i/(4*k). Each denominator is an exact nonzero integer.
    multiplier=zeros((N,1));multiplier[1:]=CBox(0.,-Box(1.)/Box(4*modes[1:,None]))
    values=fft.fft(coefficients*multiplier,inverse=True)*N
    if not np.all((values.imag.lo<=0)&(values.imag.hi>=0)):
        raise ValueError('the complete real primitive lost reality')
    return BudgetPolynomial([values.real[:,j] for j in range(length)],poly.norm/4,poly.error/4)


def moving_residual_polynomials(fields,model,alpha,full,modes,N,fft):
    U,V,Ut,Vt,Ur,Vr=fields
    g,b,K,s=[scalar_budget(model[name]) for name in ('gamma','beta','K','s')]
    # full is the exact affine-radial candidate series, before dyadic centres.
    V0=scalar_budget([row[0,1].real for row in full])
    al=float(alpha);v=s+al*V;mean=s+al*V0
    U2=U*U;v2=v*v;S=al*al*U2+K*v2
    drift=-b*primitive_polynomial(S,N,2*modes,fft)
    fU=drift*Ut+g*mean*K*Vt-b*U*(1+S)
    cubic=3*s*s*V+3*al*s*V*V+al*al*V*V*V
    fV=drift*Vt-g*mean*Ut+b*(V-K*cubic-al*v*U2)
    return Ur-fU,Vr-fV,v,mean


def full_moving_residual_norm(polynomials,N,modes,fft):
    """A0, all omitted modes, and H1-majorizing A1 on the whole radial cell.

    The exact residual has support at most 3M even for the full scalar target
    and its remainder, because those target coefficients are radial scalars.
    Thus the complete remainder's A1 fee is (1+12M) times its A0 fee.
    """
    degree=3*modes;length=max(len(p.coefficients) for p in polynomials)
    block=zeros((N,2*length))
    for component,poly in enumerate(polynomials):
        for j,value in enumerate(poly.coefficients):block[:,2*j+component]=CBox(value)
    coefficients=fft.fft(block)/N
    kk=np.asarray([j if j<N//2 else j-N for j in range(N)])
    outside=abs(kk)>degree;tail=abs(kk)>modes
    if not (np.all((coefficients.real.lo[outside]<=0)&(coefficients.real.hi[outside]>=0))
        and np.all((coefficients.imag.lo[outside]<=0)&(coefficients.imag.hi[outside]>=0))):
        raise ValueError('an exactly absent full moving residual mode lost zero')
    coefficients[outside]=0;weights=CBox(Box(1+4*abs(kk)))
    total=[arb(0),arb(0)];high=[arb(0),arb(0)];A1=[arb(0),arb(0)];orders=[[],[]]
    for component,poly in enumerate(polynomials):
        for j in range(length):
            column=coefficients[:,2*j+component]
            value=wiener_upper(column);total[component]+=value;orders[component].append(value)
            high[component]+=wiener_upper(column[tail])
            A1[component]+=wiener_upper(column*weights)
        total[component]+=poly.error;high[component]+=poly.error
        A1[component]+=(1+12*modes)*poly.error
    return dict(A0=[z.upper() for z in total],unretained_A0=[z.upper() for z in high],
        A1=[z.upper() for z in A1],per_radial_order=orders,radial_degree=length-1)


def physical_residual_C0_bounds(fields,v,mean,chart,bounds,alpha):
    """Pay the complete inverse-coordinate differential on the residual.

    I(rv-v*mean(rv)/m)/v is the true angle displacement, not I(rv)/m.
    A0 bounds are used before the reciprocal v is bounded pointwise by its
    proved full-angle gap. No A0 bound for 1/v is silently inferred from C0.
    """
    al=abs(exact_arb(alpha));gap=chart['absolute_v_gap']
    mean_interval=evaluate(mean.coefficients,Box(-1.,1.))
    fee=float(arb_box(mean.error).hi)
    mean_interval=mean_interval+Box(-fee,fee)
    mgap=arb(float(-np.max(mean_interval.hi))).lower()
    if not mgap>0:raise ValueError('the complete moving mean must be strictly negative')
    vu=(v.norm+v.error).upper();ua=al*(fields[0].norm+fields[0].error)
    up=al*(fields[2].norm+fields[2].error);vp=al*(fields[3].norm+fields[3].error)
    ru,rv=[al*z for z in bounds]
    displacement=(rv*(1+vu/mgap)/(4*gap)).upper()
    physical_ru=ru+up*displacement;physical_rv=rv+vp*displacement
    return dict(mean_absolute_gap=mgap,full_inverse_coordinate_displacement_C0=displacement,
        physical_B_residual_C0=(physical_ru/gap+ua*physical_rv/(gap*gap)).upper(),
        physical_C_residual_C0=(physical_rv/(gap*gap)).upper())
