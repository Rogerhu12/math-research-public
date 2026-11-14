#!/usr/bin/env python3
"""Exact Frobenius certificates excluding every integer 0 < j < 1728.

The obstruction is invariant under quadratic twisting.  It therefore tests
one rational model per j, without a hypothesis about the actual twist's
reduction at the selected prime.  No CM endpoints are included.
"""
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path

LEVELS=(41,47,59,83)


def prime(q):
    return q>=2 and all(q%d for d in range(2,isqrt(q)+1))


def trace(j,q):
    k=j*pow((1728-j)%q,-1,q)%q
    return -sum(0 if (v:=(x*x*x+3*k*x+2*k)%q)==0 else
                1 if pow(v,(q-1)//2,q)==1 else -1 for x in range(q))


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--check',action='store_true')
    pa.add_argument('--certificate',type=Path,default=Path(__file__).with_name('data')/'small_levels_middle_j.json')
    args=pa.parse_args()
    if not args.check:
        cert={'version':1,'j_first':1,'j_last':1727,'levels':[]}
        primes=[q for q in range(5,62) if prime(q)]
        for p in LEVELS:
            records=[]
            for j in range(1,1728):
                for q in primes:
                    if q==p or j*(1728-j)%q==0:continue
                    a=trace(j,q);disc=(a*a-4*q)%p
                    if a%p and disc and pow(disc,(p-1)//2,p)==1:
                        records.append([j,q,a]);break
                else:raise AssertionError((p,j,'no obstruction found'))
            cert['levels'].append({'p':p,'records':records})
        args.certificate.parent.mkdir(parents=True,exist_ok=True)
        args.certificate.write_text(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n')
    raw=args.certificate.read_bytes();cert=json.loads(raw)
    assert cert['version']==1 and (cert['j_first'],cert['j_last'])==(1,1727)
    assert [row['p'] for row in cert['levels']]==list(LEVELS)
    for row in cert['levels']:
        p=row['p'];assert prime(p)
        assert [rec[0] for rec in row['records']]==list(range(1,1728))
        for j,q,a in row['records']:
            assert q>=5 and prime(q) and q!=p and j*(1728-j)%q!=0
            k=j*pow((1728-j)%q,-1,q)%q
            aa,bb=3*k%q,2*k%q
            assert (4*aa**3+27*bb**2)%q!=0
            # Independent point count from the multiplicities of squares.
            square_count=[0]*q
            for y in range(q):square_count[y*y%q]+=1
            points=1+sum(square_count[(x**3+aa*x+bb)%q] for x in range(q))
            assert q+1-points==a and a*a<=4*q
            discriminant=(a*a-4*q)%p
            assert a%p!=0 and discriminant!=0
            assert any(x*x%p==discriminant for x in range(1,p))
        print(f'p={p}: all 1727 middle integers excluded; largest witness prime {max(rec[1] for rec in row["records"])}.',flush=True)
    print('SHA256',hashlib.sha256(raw).hexdigest(),'bytes',len(raw))


if __name__=='__main__':main()
