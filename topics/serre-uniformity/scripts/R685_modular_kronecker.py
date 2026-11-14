#!/usr/bin/env python3
"""Exact mod-p reductions of the complete tame Kronecker diagonals.

Ordinary derivatives, computed modulo p^2, retain the digit needed to cancel
p in n! for p <= n < 2p. The final trace is divided only after its actual
p-divisibility is checked. One prime per invocation; no wild torsion orbit.
"""
import argparse, json, time
from math import isqrt
from pathlib import Path
from hashlib import sha256


def run(p,weights=None):
    if weights is None: weights=(p,p-3)
    assert p>=41 and p%6==5
    assert all(p%d for d in range(2,isqrt(p)+1))
    assert all(2<=k<=p and k%3==2 for k in weights)
    started=time.monotonic();mod=p*p
    zero=(0,0,0);one=(1,0,0)
    def add(a,b):return tuple((x+y)%mod for x,y in zip(a,b))
    def scale(a,c):return tuple(x*c%mod for x in a)
    def mul(a,b):
        a0,a1,a2=a;b0,b1,b2=b
        return ((a0*b0+4*(a1*b2+a2*b1))%mod,
                (a0*b1+a1*b0+4*a2*b2)%mod,
                (a0*b2+a1*b1+a2*b0)%mod)
    maxm=max(weights)-1;N=2*maxm+1
    # Ordinary derivatives in xi=sqrt(3)*z, never Taylor divided powers.
    x=[(2,1,1)];y=[(-3%mod,-2%mod,-1%mod)]
    e=[scale((2,2,1),pow(6,-1,mod))];s=[one]
    binrow=[1]
    for n in range(N):
        yy=zero;ss=zero
        for i in range(n+1):
            choose=binrow[i]
            if choose:
                yy=add(yy,scale(mul(x[i],x[n-i]),choose))
                ss=add(ss,scale(mul(e[i],s[n-i]),choose))
        x.append(scale(y[n],2));y.append(yy)
        e.append(scale(x[n],-pow(3,-1,mod)));s.append(ss)
        binrow=[1]+[(binrow[i-1]+binrow[i])%mod for i in range(1,n+1)]+[1]
    # factorial unit parts through N<2p, with exactly one p removed if n>=p.
    fact=[1]
    for n in range(1,N+1):fact.append(fact[-1]*(1 if n==p else n)%mod)
    invfact=[pow(f,-1,mod) for f in fact]
    def binomial(n,j):
        exponent=int(n>=p)-int(j>=p)-int(n-j>=p)
        assert exponent in (0,1)
        return fact[n]*invfact[j]*invfact[n-j]*p**exponent%mod
    # Taylor coefficients of 1/s through m<p, all factorials are units.
    st=[scale(s[n],invfact[n]) for n in range(maxm+1)]
    invs=[one]
    for n in range(1,maxm+1):
        b=zero
        for j in range(1,n+1):b=add(b,mul(st[j],invs[n-j]))
        invs.append(scale(b,-1))
    # Full inverse-sigma factor in the scaled variable.
    H=(maxm+1)//6
    wp=[0]*(H+1)
    if H:wp[1]=pow(189,-1,mod)
    for n in range(2,H+1):
        wp[n]=sum(wp[i]*wp[n-i] for i in range(1,n))%mod*pow((n-1)*(6*n+1),-1,mod)%mod
    logu=[0]+[wp[n]*pow(6*n*(6*n-1),-1,mod)%mod for n in range(1,H+1)]
    u=[1]
    for h in range(1,H+1):
        u.append(sum(i*logu[i]*u[h-i] for i in range(1,h+1))%mod*pow(h,-1,mod)%mod)
    # p*s_n modulo p^2, without any illegal division by p in the ring.
    ps=[scale(s[n],invfact[n]*(p if n<p else 1)) for n in range(N+1)]
    rows=[]
    for k in weights:
        m=k-1;pcm=zero;blocks=[]
        for h in range((m+1)//6+1):
            block=zero
            for j in range(m+1):
                n=2*m+1-j-6*h;power=m-j
                if n<0 or n<power:continue
                block=add(block,scale(mul(invs[j],ps[n]),u[h]*binomial(n,power)))
            blocks.append({'inverse_sigma_power':6*h,'p_times_diagonal':block})
            pcm=add(pcm,block)
        # Only the r-coefficient survives the exact trace Tr(c_m/r).
        assert pcm[1]%p==0,('nonintegral traced diagonal',p,k,pcm)
        cm_r=(pcm[1]//p)%p
        Ck=(-1)**m*pow(3,2*m,p)*fact[m]*pow(2,-1,p)*cm_r%p
        rows.append({'k':k,'m':m,'p_times_diagonal_mod_p2':pcm,
                     'r_coefficient_after_exact_division':cm_r,'Ck_mod_p':Ck,
                     'all_inverse_sigma_blocks':blocks})
    return {'prime':p,'modulus':mod,'exact_reductions':rows,
            'method':'ordinary derivatives mod p^2; factorial unit parts; full sigma; trace then divide p',
            'highest_derivative':N,'runtime_seconds':time.monotonic()-started,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--prime',type=int,required=True)
    ap.add_argument('--weights',type=int,nargs='+');ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();result=run(args.prime,args.weights)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'p':result['prime'],'values':[(r['k'],r['Ck_mod_p']) for r in result['exact_reductions']],
                      'runtime_seconds':result['runtime_seconds']}))
