#!/usr/bin/env python3
"""Exact rational bounds for the dual-harmonic circular-arc minimax constants.

Only Fraction arithmetic, integer square root and alternating Taylor bounds
enter the assertions. Decimal strings are directed displays of rational
enclosures. No BVP, finite transversality or sampled geometry is used.
"""
import argparse,json,math
from fractions import Fraction as F
from pathlib import Path


def decimal(q,digits=30,upper=False):
    scale=10**digits;n=q.numerator*scale//q.denominator
    if upper and F(n,scale)<q:n+=1
    sign='-'if n<0 else '';n=abs(n)
    return sign+str(n//scale)+'.'+str(n%scale).zfill(digits)


def interval(lo,hi):
    assert lo<=hi
    return dict(lower_exact=str(lo),upper_exact=str(hi),
                lower_decimal=decimal(lo),upper_decimal=decimal(hi,upper=True))


def cosine(x):
    assert 0<=x<=1
    # Alternating, strictly decreasing terms for this argument.
    sums=[];s=F(0)
    for k in range(22):
        s+=(-1)**k*x**(2*k)/math.factorial(2*k)
        if k in (20,21):sums.append(s)
    return sums[1],sums[0]


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    n=4;halfwidth=F(147,1000);cL,cU=cosine(n*halfwidth)
    assert 0<cL<=cU<1
    E=lambda c:(1-c)**2/((1+c)*(5+c))
    eL,eU=E(cU),E(cL);Clo,Chi=15*eL,15*eU
    # Three-point Lagrange functional: constant + half quadratic coefficient.
    for c in (cL,cU):
        d=1-c;m=(1+c)/2
        w0=(c+2)/d**2;wm=-(4*c+2)/d**2;w1=(c*c+c+1)/d**2
        assert w0+wm+w1==1
        assert w0*c+wm*m+w1==0
        assert w0*c*c+wm*m*m+w1==F(1,2)
        assert w0-wm+w1==1/E(c)
        A=8/(5+c);B=-4/((1+c)*(5+c))
        assert 1-A*c-B*(2*c*c-1)==E(c)
        assert 1-A*m-B*(2*m*m-1)==-E(c)
        assert 1-A-B==E(c)
    # A+B=1 case: the unique larger root of the equioscillation equation.
    den=10**70;z=math.isqrt(2*den*den);sqrtL,sqrtU=F(z,den),F(z+1,den)
    assert sqrtL*sqrtL<2<sqrtU*sqrtU
    dL,dU=1-cU,1-cL
    etaL=1/(3-4*(sqrtL-1)*dL);etaU=1/(3-4*(sqrtU-1)*dU)
    assert F(1,3)<etaL<=etaU<1
    M=lambda eta:(9*eta+2+1/eta)/8
    # For eta>1/3, M(eta) and the negative interior extremum magnitude
    # (3eta-1)^2/(8eta) are both strictly increasing.
    fixedE=lambda eta:(3*eta-1)**2/(8*eta)
    q=F(3,50)
    result=dict(scope=__doc__,n=n,halfwidth_exact=str(halfwidth),argument_exact=str(n*halfwidth),
        cosine=interval(cL,cU),unconstrained_unit_error=interval(eL,eU),
        rho_error_per_q=interval(Clo,Chi),
        rho_error_at_q_005=interval(Clo/200,Chi/200),
        rho_error_at_q_006=interval(Clo*q,Chi*q),
        optimal_A=interval(8/(5+cU),8/(5+cL)),
        optimal_B=interval(-4/((1+cL)*(5+cL)),-4/((1+cU)*(5+cU))),
        fixed_center_eta=interval(etaL,etaU),
        fixed_center_unit_error=interval(fixedE(etaL),fixedE(etaU)),
        fixed_center_global_Bmax=interval(M(etaL),M(etaU)),
        fixed_center_rho_min_at_q_006=interval(1-15*q*M(etaU),1-15*q*M(etaL)),
        fixed_center_rho_max_at_q_006=interval(1+15*q*(1+2*etaL),1+15*q*(1+2*etaU)),
        logical_scope='The minimax statements are unconditional. A branch obstruction additionally requires a complete linearized core-trace space and differentiability; finite Fourier transversality does not establish either premise.')
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]for k in ['rho_error_per_q','fixed_center_eta','fixed_center_rho_min_at_q_006','fixed_center_rho_max_at_q_006']},indent=2))


if __name__=='__main__':main()
