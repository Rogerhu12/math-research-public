#!/usr/bin/env python3
"""Three fixed small weights only; numerical normalization diagnostic, not proof.

No interval tail enclosure or nonvanishing certificate is claimed.
The exact statement and proof are in R692; this only reproduces its diagnostic.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp

def run():
    mp.mp.dps=60
    z=mp.mpc(-mp.mpf(1)/2,mp.sqrt(3)/2)
    N=180
    a=[0]*(N+1)
    a[0]=1
    for d in range(1,N+1):
        chi=0 if d%3==0 else (1 if d%3==1 else -1)
        for n in range(d,N+1,d):
            a[n]+=6*chi
    Om=mp.beta(mp.mpf(1)/6,mp.mpf(1)/2)/3
    area=Om**2*mp.sqrt(3)/(2*mp.pi)
    rows=[]
    for k in [2,5,8]:
        m=k-1
        def F(t):
            q=mp.exp(-2*mp.pi*mp.j*t.conjugate())
            return sum(mp.mpf(a[n])*mp.laguerre(m,0,4*mp.pi*n*t.imag)*q**n
                       for n in range(N+1))
        central=mp.pi/(3*mp.sqrt(3))*(F(2*z)-z**-1*F(z/2)/2
                                     -z**-2*F((z+1)/2)/2)
        scale=mp.root(4,3)*mp.sqrt(3)*Om*area**m/(-3)**m
        rows.append({'k':k,'central_value':mp.nstr(central,30),
                     'Ck_from_theta':mp.nstr(central/scale,30)})
    return {'method':'R692 three-point Laguerre theta series',
            'decimal_precision':60,'q_terms':180,'rows':rows,
            'rigorous_interval_enclosure':False,
            'nonvanishing_theorem_claimed':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    args.output.write_text(json.dumps(run(),indent=2)+'\n')
