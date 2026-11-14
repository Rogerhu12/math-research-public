#!/usr/bin/env python3
"""Complete finite partial-time one-form pullback in normalized label x.

Rows are finite full Laurent mappings k -> acb coefficient of exp(i*k*x).
The time variable is one increasing leaf coordinate u in [-1,1]; signed
physical time halfwidths must already be in g and B. No high Fourier/time
mode is removed. This helper asserts no true geometry or ray error itself.
"""
from __future__ import annotations
from flint import acb,arb
from fourfold_subprincipal_root_regularized_transport import fadd,fscale
from fourfold_subprincipal_root_regularized_fft import complete_product


def dx(row):
    return {k:acb(0,int(k))*v for k,v in row.items()}


def add(*polynomials):
    n=max((len(p) for p in polynomials),default=0)
    return [fadd(*(p[i] for p in polynomials if i<len(p))) for i in range(n)]


def multiply(p,q):
    out=[{} for _ in range(max(len(p)+len(q)-1,0))]
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]=fadd(out[i+j],complete_product(a,b))
    return out


def primitive_from_left(p):
    out=[{} for _ in range(len(p)+1)]
    for n,row in enumerate(p):
        value=fscale(row,acb(1)/(n+1))
        out[n+1]=value
        out[0]=fadd(out[0],fscale(value,-((-1)**(n+1))))
    return out


def at_endpoint(p,right=True):
    return fadd(*(fscale(row,1 if right else (-1)**n) for n,row in enumerate(p)))


def integral(p):
    return fadd(*(fscale(row,acb(2)/(n+1)) for n,row in enumerate(p) if n%2==0))


def time_polynomial_derivative(p):
    return [dx(row) for row in p]


def finite_pullback(B,C,D):
    """B + dx[B(C+D) + .5 B_x C^2], including all zero modes."""
    correction=add(multiply(B,add(C,D)),
                   [fscale(row,acb(1)/2) for row in
                    multiply(time_polynomial_derivative(B),multiply(C,C))])
    return add(B,time_polynomial_derivative(correction))


def advance_one_form(g,B,C_before,D_before):
    """Return exact finite partial polynomials and signed phase integral.

    C_before,D_before are prior accumulated full Laurent polynomials. Caller
    retains Arb arithmetic errors or makes an explicit paid dyadic choice.
    """
    if not g or not B:raise ValueError("complete nonempty time polynomials required")
    C=add([C_before],primitive_from_left(g))
    D=add([D_before],primitive_from_left(multiply(time_polynomial_derivative(g),C)))
    pulled=finite_pullback(B,C,D)
    return {"C_time_rows":C,"D_time_rows":D,
            "C_end":at_endpoint(C),"D_end":at_endpoint(D),
            "one_form_time_rows":pulled,"one_form_integral":integral(pulled),
            "label_derivative_multiplier":1,"complete_finite_algebra":True,
            "true_ray_error_paid":False}


def endpoint_one_form(B,C,D):
    return finite_pullback([B],[C],[D])[0]


def positive(v,name,zero=False):
    v=arb(v)
    if not v.is_finite() or not (v>=0 if zero else v>0):
        raise ValueError("unpaid nonnegative input "+name)
    return v


def one_form_error_prefactors(*,A,E,defect_strip,source_strip,Taylor_strip,final_strip):
    A=positive(A,"A",True);E=positive(E,"E",True)
    Sg=positive(defect_strip,"defect strip");SB=positive(source_strip,"source strip")
    sigma=positive(Taylor_strip,"Taylor strip");s=positive(final_strip,"final strip",True)
    R=Sg-sigma;d=R-A;delta=sigma-s;L0=SB-sigma;L=L0-A
    if not A<=R/2 or not delta>0 or not L>0 or not A<d:
        raise ValueError("complete one-form analytic domain gate failed")
    F=E*(1+A/R)+A*A*A/(2*d*d)
    K=(F+(A*A*A/(2*d)+A*E)/L0+A*A*A/(3*L*L))/delta
    Q=1/(1-A/d)
    return {"one_form_remainder_per_unit_phase_modulus":K.upper(),
            "source_error_pullback_factor":Q.upper(),
            "complete_partial_time_D_required":True}
