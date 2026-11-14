#!/usr/bin/env python3
"""Independent original-z sigma-six verification of the actual roots.

This does not use R698's H,T,Z series, Lagrange inversion, or its
Frobenius coefficient simplification.  It solves the original Weierstrass
energy equation directly in w=z^6 and then (log sigma)''=-x.
Requires python-flint.  Every division occurs below the proved cutoff p.
"""
import argparse
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path
import time
from flint import nmod_poly
import flint


def exp_series(f, length, p):
    assert int(f[0]) == 0 and length <= p
    q = nmod_poly([1], p)
    n = 1
    while n < length:
        r = min(2*n, length)
        logq = q.derivative().mul_low(q.inverse_series_trunc(r-1), r-1).integral()
        q = q.mul_low(1+f.truncate(r)-logq, r)
        n = r
    return q


def digest(a):
    return hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()


def run(p, full=False):
    assert p>=41 and p%6==5 and all(p%d for d in range(2,isqrt(p)+1))
    start=time.monotonic();N=(p-5)//6;length=N+1
    one=nmod_poly([1],p);w=nmod_poly([0,1],p)
    inv=[0]*(p-3);inv[1]=1
    for j in range(2,p-3):inv[j]=(p-(p//j)*inv[p%j])%p
    X=one;n=1;steps=[]
    # X=z^2*x(z).  V=-2X+6wX', and V^2=4X^3-4w.
    while n<length:
        r=min(2*n,length)
        V=(-2*X+6*X.derivative().left_shift(1)).truncate(r)
        invV=V.inverse_series_trunc(r)
        X2=X.mul_low(X,r)
        residual=(V.mul_low(V,r)-4*X2.mul_low(X,r)+4*w).truncate(r)
        assert residual.truncate(n).is_zero()
        # The exact Newton equation is w*d' + a*d = b, a(0)=1/6.
        a=(-(V+3*X2).mul_low(invV,r)*inv[3]).truncate(r)
        b=(-residual.mul_low(invV,r)*inv[12]).truncate(r)
        assert int(a[0])==inv[6]
        primitive=nmod_poly([0]+[int(a[j])*inv[j]%p for j in range(1,r)],p)
        integrating=exp_series(primitive,r,p)
        ib=integrating.mul_low(b,r)
        integrated=nmod_poly([int(ib[j])*6*inv[6*j+1]%p for j in range(r)],p)
        correction=integrated.mul_low(integrating.inverse_series_trunc(r),r)
        assert correction.truncate(n).is_zero()
        X=(X+correction).truncate(r)
        V=(-2*X+6*X.derivative().left_shift(1)).truncate(r)
        check=(V.mul_low(V,r)-4*X.mul_low(X,r).mul_low(X,r)+4*w).truncate(r)
        assert check.is_zero()
        steps.append({'from_precision':n,'to_precision':r,'full_energy_equation_checked':True})
        n=r
    V=(-2*X+6*X.derivative().left_shift(1)).truncate(length)
    xcoeff=[int(X[j]) for j in range(length)]
    # sigma(z)^6 = z^6 Q(w), log Q coefficient = -X_j/(j*(6j-1)).
    logarithm=[0]+[-xcoeff[j]*inv[j]*inv[6*j-1]%p for j in range(1,length)]
    Q=exp_series(nmod_poly(logarithm,p),length,p)
    logder=nmod_poly([0]+[-xcoeff[j]*inv[6*j-1]%p for j in range(1,length)],p)
    assert (Q.derivative().left_shift(1)-Q.mul_low(logder,length)).truncate(length).is_zero()
    F=X.mul_low(Q,length)
    G=(-X.mul_low(V,length).mul_low(Q,length)*inv[2]).truncate(length)
    fN,gN=int(F[N]),int(G[N]);ell2=pow(2,(p-1)//2,p)
    ap=-ell2*fN%p;aq=2*inv[3]*ell2*gN%p
    coeff={'X':xcoeff,'V':[int(V[j]) for j in range(length)],
           'Q':[int(Q[j]) for j in range(length)]}
    result={'result':'R698-independent-original-z','prime':p,'N':N,
            'original_coordinate':'w=z^6, x=z^(-2)X(w), y=z^(-3)V(w)/2, sigma^6=z^6 Q(w)',
            'coefficient_x_sigma6':fN,'coefficient_minus_xy_sigma6':gN,
            'A_p':ap,'A_p_minus_3':aq,'C_p':-3*ap*ap%p,'C_p_minus_3':-3*aq*aq%p,
            'newton_steps':steps,'all_sigma_logarithm_relations_checked':N,
            'uses_R698_H_T_Z_or_Lagrange_Frobenius_reduction':False,
            'division_by_p_used':False,'python_flint_version':flint.__version__,
            'coefficient_sha256':{key:digest(arr) for key,arr in coeff.items()},
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'runtime_seconds':time.monotonic()-start}
    if full:
        result['coefficients']=coeff
        result['F_last_summands']=[xcoeff[j]*int(Q[N-j])%p for j in range(length)]
        xv=X.mul_low(V,length)
        result['G_last_summands']=[-int(xv[j])*int(Q[N-j])*inv[2]%p for j in range(length)]
        assert sum(result['F_last_summands'])%p==fN and sum(result['G_last_summands'])%p==gN
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prime',type=int,required=True)
    parser.add_argument('--full',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=run(args.prime,args.full)
    raw=(json.dumps(result,indent=2)+'\n').encode()
    args.output.write_bytes(gzip.compress(raw,mtime=0) if args.output.suffix=='.gz' else raw)
    print(json.dumps({key:result[key] for key in ['prime','N','coefficient_x_sigma6',
        'coefficient_minus_xy_sigma6','A_p','A_p_minus_3','C_p','C_p_minus_3','runtime_seconds']}))
