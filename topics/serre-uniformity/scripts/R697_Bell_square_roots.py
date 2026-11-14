#!/usr/bin/env python3
"""Actual R697 arithmetic square roots modulo an inert prime; no division by p.

The two degree < p ordinary-derivative recurrences are evaluated in
F_p[b]/(b^2-3); the algebra is permitted to split.
"""
import argparse,json,time
from pathlib import Path
from hashlib import sha256
from math import isqrt

def run(p):
    assert p>=41 and p%6==5 and all(p%d for d in range(2,isqrt(p)+1))
    started=time.monotonic()
    r=pow(4,pow(3,-1,p-1),p)
    def q(a=0,b=0):return(a%p,b%p)
    def add(x,y):return((x[0]+y[0])%p,(x[1]+y[1])%p)
    def scale(x,a):return(x[0]*a%p,x[1]*a%p)
    def mul(x,y):return((x[0]*y[0]+3*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def inv(x):
        d=(x[0]*x[0]-3*x[1]*x[1])%p
        assert d
        return scale(q(x[0],-x[1]),pow(d,-1,p))
    a=q(-180*r*r-240*r-375);s=q(2*r*r+4*r+5)
    odd_x=q(-4*r*r-6*r-1,r*r+2*r-6)
    odd_y=q(12*r*r-24*r+12,-9*r*r+12*r+6)
    odd_e=scale(q(-r*r+2*r+2,r*r+2),pow(2,-1,p))
    even_x=q(5+2*r*r,2*(r*r+2*r+3))
    rows=[]
    for odd,m,k in [(False,p-1,p),(True,p-4,p-3)]:
        x=[odd_x if odd else even_x]
        y=[odd_y if odd else q()]
        e=[odd_e if odd else q()]
        f=[q(1)];binom=[1]
        for n in range(m):
            xx=q();ef=q()
            for j,c in enumerate(binom):
                xx=add(xx,scale(mul(x[j],x[n-j]),c))
                ef=add(ef,scale(mul(e[j],f[n-j]),c))
            yn=scale(xx,3)
            if n==0:yn=add(yn,a)
            en=x[n]
            if n==0:en=add(en,s)
            x.append(scale(y[n],2))
            y.append(scale(yn,-1 if odd else 1))
            e.append(scale(en,1 if odd else -1))
            f.append(ef)
            binom=[1]+[(binom[j-1]+binom[j])%p for j in range(1,len(binom))]+[1]
        if odd:
            base=f[1];power2=(m-1)//2
            factor=(-1)**power2*pow(2,-power2,p)%p
        else:
            base=f[4];power2=(m-4)//2
            factor=6*pow(2,-power2,p)%p
        root=scale(mul(f[m],inv(base)),factor)
        assert root[1]==0,('rationality audit failed',p,k,root)
        rows.append({'k':k,'m':m,'A_k_mod_p':root[0],
                     'C_k_mod_p':-3*root[0]*root[0]%p,
                     'base_derivative':list(base),'top_derivative':list(f[m]),
                     'base_norm_mod_p':(base[0]**2-3*base[1]**2)%p,
                     'rationality_beta_coefficient_zero':True})
    return {'result':'R697','prime':p,'alpha':r,'coefficient_algebra':'F_p[b]/(b^2-3)',
            'rows':rows,'zero_weights':[x['k'] for x in rows if not x['A_k_mod_p']],
            'all_prime_unit_claimed':False,'division_by_p_used':False,
            'runtime_seconds':time.monotonic()-started,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prime',type=int,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();r=run(a.prime);a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
