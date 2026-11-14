#!/usr/bin/env python3
"""Certify the uniform phase-independent tail after the R101 reduction.

Every possible integer in one coordinate is included.  Outward dyadic
interval contraction and a saved separating coordinate prove its exclusion.
Zero codes denote bands that survive this necessary test, never points.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path
from flint import arb, fmpq, ctx
from small_levels_archimedean_reduction import setup

LEVELS=(41,47,59,83)
ENDPOINT_BITS=64


def lower_integer(x):
    return int(x.lower().ceil().unique_fmpz())


def upper_integer(x):
    return int(x.upper().floor().unique_fmpz())


def floor_dyadic(x):
    return int((x.lower()*2**ENDPOINT_BITS).floor().unique_fmpz())


def ceil_dyadic(x):
    return int((x.upper()*2**ENDPOINT_BITS).ceil().unique_fmpz())


def exact_dyadic(n):
    return arb(fmpq(n,2**ENDPOINT_BITS))


def error_bound(p,kappa,s):
    t=(-arb(s)/p).exp()
    r=t**p
    return 16*kappa*(t/((1-t)**2*(1-r))+r/(1-r)**2)


def contract(p,kappa,delta,theta,n,lower,upper):
    center=(arb(n)-theta)/delta
    a,b=lower*2**ENDPOINT_BITS,upper*2**ENDPOINT_BITS
    for _ in range(3):
        radius=error_bound(p,kappa,exact_dyadic(a))/abs(delta)
        band=center+arb(0,radius.upper())
        a=max(a,floor_dyadic(band))
        b=min(b,ceil_dyadic(band))
        if a>b:break
    return a,b


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--precision',type=int,default=256)
    pa.add_argument('--initial',type=Path,default=Path(__file__).with_name('data')/'small_levels_archimedean_reduction.json')
    pa.add_argument('--output',type=Path,default=Path(__file__).with_name('data')/'small_levels_archimedean_tail.json')
    args=pa.parse_args()
    assert args.precision>=256
    initial_raw=args.initial.read_bytes()
    initial=json.loads(initial_raw)
    out={'version':1,'precision_bits':args.precision,'endpoint_bits':ENDPOINT_BITS,
         'initial_sha256':hashlib.sha256(initial_raw).hexdigest(),
         'contraction_passes':3,'scope':'necessary unit-lattice tail only; no claim that surviving bands contain points',
         'levels':[]}
    for previous in initial['levels']:
        started=time.time();p=previous['p'];assert p in LEVELS
        _,_,cusps,kn,_,_=setup(p,args.precision)
        kappa=arb(fmpq(kn,2**64));lower=6*p
        row={'p':p,'lower':lower,'kappa_upper_numerator':kn,'cusps':[]}
        checked=0;survived=0;bound=lower
        for c,old in zip(cusps,previous['cusps']):
            assert c['s']==old['s']
            ds,ts=c['delta'],c['theta'];upper=old['S_final']
            i=max(range(1,len(ds)),key=lambda j:float(abs(ds[j]).mid()))
            assert abs(ds[i])>0
            radius=error_bound(p,kappa,lower)
            image=ds[i]*arb(lower).union(upper)+ts[i]+arb(0,radius.upper())
            first,last=lower_integer(image),upper_integer(image)
            choices=[];bands=[]
            for n in range(first,last+1):
                a,b=contract(p,kappa,ds[i],ts[i],n,lower,upper)
                checked+=1
                if a>b:
                    choices.append(-1);continue
                interval=exact_dyadic(a).union(exact_dyadic(b))
                radius=error_bound(p,kappa,exact_dyadic(a))
                j=next((j for j in range(1,len(ds)) if j!=i and
                        lower_integer(ds[j]*interval+ts[j]+arb(0,radius.upper()))>
                        upper_integer(ds[j]*interval+ts[j]+arb(0,radius.upper()))),0)
                choices.append(j)
                if not j:
                    bands.append([n,str(a),str(b)])
                    survived+=1
                    bound=max(bound,(b+2**ENDPOINT_BITS-1)//2**ENDPOINT_BITS)
            row['cusps'].append({'s':c['s'],'coordinate':i,'n_first':first,'n_last':last,
                                 'exclusion_coordinates':choices,'surviving_bands':bands})
        row.update({'integers_checked':checked,'bands_surviving':survived,'S_uniform':bound})
        out['levels'].append(row)
        print(f'p={p}: {checked} integers; {survived} possible bands; s <= {bound}; {time.time()-started:.2f}s',flush=True)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
    args.output.write_bytes(raw)
    print('SHA256',hashlib.sha256(raw).hexdigest(),'bytes',len(raw),flush=True)


if __name__=='__main__':main()
