#!/usr/bin/env python3
"""Direct R605 coefficients in F_p, with analytic factorial-p cancellation.

This uses the rational R_- and the actual formal logarithm quotient, not
Kronecker diagonals. It is independent of the R658/R683 comparison.
Requires python-flint; one prime per invocation.
"""
import argparse,json,time
from pathlib import Path
from hashlib import sha256
from math import isqrt,comb
from flint import nmod_poly

def run(p):
    assert p>=41 and p%6==5 and all(p%d for d in range(2,isqrt(p)+1))
    start=time.monotonic()
    M2=(p*p-p-2)//6;M3=(p*p-4*p+1)//6;N=M2+1
    assert 2*M2<p*p and M2<(p*p-1)//6
    # U_n=n!/p^{floor(n/p)} is a p-unit for n<p^2.
    unitfact=[1]*(2*M2+1)
    for n in range(1,2*M2+1):
        unitfact[n]=unitfact[n-1]*(n//p if n%p==0 else n)%p
    invfact=[1]*(2*M2+1);invfact[-1]=pow(unitfact[-1],-1,p)
    for n in range(2*M2,0,-1):
        invfact[n-1]=invfact[n]*(n//p if n%p==0 else n)%p
    invsmall=[0]+[pow(d,-1,p) for d in range(1,p)]
    C=[];Z=[];fouri=1;inv4=pow(4,-1,p);cancelled=[]
    for k in range(N):
        if k:fouri=fouri*inv4%p
        v=(2*k)//p-2*(k//p)
        unit=unitfact[2*k]*invfact[k]**2%p
        C.append(unit*fouri%p if v==0 else 0)
        den=6*k+1;d=0
        if den%p==0:den//=p;d=1;cancelled.append(k)
        assert den%p and v>=d
        Z.append(unit*fouri*invsmall[den%p]%p if v==d else 0)
    z=nmod_poly(Z,p);c=nmod_poly(C,p)
    ac=nmod_poly([1,34,-8],p).mul_low(c,N)
    ac=ac.mul_low(nmod_poly([1,-228,48,-64],p).inverse_series_trunc(N),N)
    zi=z.inverse_series_trunc(N)
    Q2=ac.mul_low(zi,N)
    Q3=Q2.truncate(M3+1).mul_low(zi.truncate(M3+1).pow_trunc(3,M3+1),M3+1)
    Z4=z.truncate(M3//p+1).pow_trunc(4,M3//p+1)
    terms2=[{'j':j,'coefficient_Q':int(Q2[M2-p*j]),'coefficient_Z':Z[j],
             'term':int(Q2[M2-p*j])*Z[j]%p} for j in range(M2//p+1)]
    terms3=[{'j':j,'coefficient_Q':int(Q3[M3-p*j]),'coefficient_Z4':int(Z4[j]),
             'term':int(Q3[M3-p*j])*int(Z4[j])%p} for j in range(M3//p+1)]
    r2=sum(t['term'] for t in terms2)%p;r3=sum(t['term'] for t in terms3)%p
    B=(-1)**((p-1)//2-(p-2)//3)*comb((p-1)//2,(p-2)//3)%p
    alpha=pow(4,pow(3,-1,p-1),p)
    leg3=pow(3,(p-1)//2,p)
    cartier=leg3*alpha**2*pow(2,-1,p)%p
    return {'prime':p,'r2':r2,'r3':r3,'B':B,'alpha':alpha,'cartier_c':cartier,
            'Cp_predicted_by_R658':r2*pow(cartier,-1,p)%p,
            'Cp_minus3_predicted_by_R683':r3*pow(-27*cartier*B**3,-1,p)%p,
            'M2':M2,'M3':M3,'summands_r2':terms2,'summands_r3':terms3,
            'cancelled_denominator_indices':cancelled,
            'method':'R605 literal AC*(Z(w^p)/Z(w))^1 or ^4; p-unit factorial arrays; FLINT finite series',
            'runtime_seconds':time.monotonic()-start,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--prime',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();r=run(a.prime)
    a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ('prime','r2','r3','Cp_predicted_by_R658','Cp_minus3_predicted_by_R683','runtime_seconds')}))
