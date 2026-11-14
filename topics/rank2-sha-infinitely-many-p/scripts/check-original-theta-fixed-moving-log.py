#!/usr/bin/env python3
"""R211: original p43 theta connection and fixed/moving log-h calibration.

Uses the same already calibrated p=43 as R206/R208. All original theta
coefficients are rational, and all finite-field operations are exact.
No prime scan and no claim of complete central vanishing.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse
import json

def main():
    p, r = 43, 11
    d, N = 2*r-1, 2*r
    Q = Fraction
    def qzero(): return [Q(0)]*(N+1)
    def qmul(a,b):
        c=qzero()
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b[:N+1-i]):
                    if y:c[i+j]+=x*y
        return c
    def qinv(a):
        b=qzero();b[0]=1/a[0]
        for n in range(1,N+1):
            b[n]=-sum(a[j]*b[n-j] for j in range(1,n+1))/a[0]
        return b
    def qpow(a,n):
        if n<0:return qpow(qinv(a),-n)
        b=qzero();b[0]=Q(1)
        while n:
            if n%2:b=qmul(b,a)
            n//=2
            if n:a=qmul(a,a)
        return b
    def qexp(a):
        b=qzero();b[0]=Q(1)
        for n in range(1,N+1):
            b[n]=sum(Q(j)*a[j]*b[n-j] for j in range(1,n+1))/n
        return b
    # R162 exact logarithmic derivative in the original s coordinate.
    F=[Q(comb(2*j,j),4**j*(4*j+1)) for j in range(N+1)]
    L=qzero();dd=Q(17,3)
    for n in range(1,N+1):
        L[n]=dd/n;dd*=Q(4*n+1,4*n+3)
    Lprime=[Q(i+1)*L[i+1] for i in range(N)]+[Q(0)]
    c=qmul(Lprime,qpow(F,-4*r))[r-1]/r
    W=[Q(0)]+qpow(F,4)[:-1]
    logGamma=[x-c*y for x,y in zip(L,qpow(W,r))]
    logGamma[N]=Q(0)
    Gamma=qexp(logGamma);Gamma[N]=Q(0)
    def red(a):
        assert a.denominator%p
        return a.numerator*pow(a.denominator,-1,p)%p
    G=list(map(red,Gamma))

    def ser(v=()):return (list(v)+[0]*(N+1))[:N+1]
    def add(a,b):return [(x+y)%p for x,y in zip(a,b)]
    def scale(a,t):return [x*t%p for x in a]
    def mul(a,b):
        out=ser()
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b[:N+1-i]):
                    out[i+j]=(out[i+j]+x*y)%p
        return out
    def inv(a):
        out=ser([pow(a[0],-1,p)])
        for n in range(1,N+1):
            out[n]=-sum(a[j]*out[n-j] for j in range(1,n+1))*out[0]%p
        return out
    def power(a,n):
        if n<0:return power(inv(a),-n)
        out=ser([1])
        while n:
            if n%2:out=mul(out,a)
            n//=2
            if n:a=mul(a,a)
        return out
    def deriv(a):return ser([(j+1)*a[j+1]%p for j in range(N)])
    def integ(a):return [0]+[a[j-1]*pow(j,-1,p)%p for j in range(1,N+1)]
    def log(a):return integ(mul(deriv(a),inv(a)))
    def exp(a):
        assert a[0]==0
        out=ser([1])
        for n in range(1,N+1):
            out[n]=sum(j*a[j]*out[n-j] for j in range(1,n+1))*pow(n,-1,p)%p
        return out
    h=ser([(-1)**j*comb(d,j)*pow(4*j+1,-1,p)%p for j in range(d+1)])
    assert h[0]==h[d]==1 and all(h[j]==h[d-j] for j in range(d+1))
    assert sum((-1)**j*h[j] for j in range(d+1))%p==0
    h1=ser([1,4,70,4,1]);h2=ser([1,20,-26,20,1])
    q8=ser([1,0,364,-1088,1190,-1088,364,0,1])
    J=scale(mul(mul(ser([0,1]),ser([1,-2,5])),ser([5,-2,1])),pow(5,-1,p))
    P=mul(mul(mul(mul(J,power(ser([1,-1]),2)),ser([1,1])),h1),h2)
    B=mul(mul(mul(J,ser([1,-1])),power(ser([1,1]),2)),q8)
    kap=comb(2*r-2,r-1)*pow(4**(r-1),-1,p)%p
    minus=power(ser([1,-1]),d)
    lam=[0]*(r-1)+minus[:N-r+2]
    shifted_h=[0]*r+h[:N-r+1]
    fixedlog=log(ser([1,1]))
    logh=log(h)
    movinglog=add(logh,scale(fixedlog,-1))
    # Bpoly is the explicit polynomial part of the true connection.
    summand=ser()
    for j in range(d+1):
        if j!=r-1:summand[j]=(-1)**j*comb(d,j)*pow(j-r+1,-1,p)%p
    Bpoly=scale(mul(minus,summand),17*pow(4,-1,p)%p)
    H=mul(deriv(G),inv(G))
    C=(H[r-1]-Bpoly[r-1])%p
    model=add(add(Bpoly,scale(mul(lam,logh),-17*kap)),scale(lam,C))
    assert H[:2*r-1]==model[:2*r-1]
    V=add(integ(Bpoly),scale(integ([0]*r+deriv(h)[:N-r+1]),68*kap))
    V[N]=0
    Gbase=exp(V);Gbase[N]=0
    Gcirc=exp(add(V,scale(shifted_h,4*C)));Gcirc[N]=0
    correction=add(ser([1]),scale(mul(shifted_h,logh),-68*kap))
    assert mul(Gcirc,correction)[:2*r]==G[:2*r]
    def row(f,n):
        return mul(deriv(f),power(h,-4*n))[n-1]*pow(n,-1,p)%p
    actual=[mul(G,P),mul(G,B)]
    base=[mul(Gbase,P),mul(Gbase,B)]
    circ=[mul(Gcirc,P),mul(Gcirc,B)]
    first=[row(f,r) for f in actual]
    second=[row(f,2*r) for f in actual]
    fixed=[row(mul(f,fixedlog),r) for f in actual]
    moving=[row(mul(f,movinglog),r) for f in actual]
    second_base=[row(f,2*r) for f in base]
    second_circ=[row(f,2*r) for f in circ]
    assert first==[39,6] and second==[22,2]
    assert first==[row(f,r) for f in base]
    assert second_circ==[(second_base[j]+4*C*first[j])%p for j in range(2)]
    scale_log=-68*kap%p
    assert second==[(second_circ[j]+scale_log*(fixed[j]+moving[j]))%p for j in range(2)]
    det=lambda a,b:(a[0]*b[1]-a[1]*b[0])%p
    moving_det=det(first,moving)
    assert moving_det==18
    report={
        "p":p,"r":r,"kappa":kap,"actual_connection_free_constant":C,
        "minus_68_kappa":scale_log,
        "original_first_row":first,"original_second_row":second,
        "fixed_s_minus_one_log_row":fixed,"moving_log_row":moving,
        "polynomial_connection_second_row":second_base,
        "same_gauge_second_row_without_log_forcing":second_circ,
        "minor_original":det(first,second),
        "minor_polynomial_connection":det(first,second_base),
        "minor_fixed_log":det(first,fixed),"minor_moving_log":moving_det,
        "weighted_fixed_log_contribution":scale_log*det(first,fixed)%p,
        "weighted_moving_log_contribution":scale_log*moving_det%p,
        "minor_if_moving_term_discarded":(det(first,second_base)+scale_log*det(first,fixed))%p,
        "r207_bare_trace_unit":kap*2261*pow(81920,-1,p)%p,
        "exact_original_gamma_connection_identity":True,
        "fixed_moving_decomposition_verified":True,
        "scope":"One existing original p43 calibration. It refutes unconditional removal of the moving log term; the original first row is nonzero, so it does not settle a conditional identity after first-row vanishing or prove infinite-prime nonvanishing."
    }
    parser=argparse.ArgumentParser()
    parser.add_argument("--output")
    args=parser.parse_args()
    text=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:Path(args.output).write_text(text)
    print(text,end="")

if __name__=="__main__":
    main()

