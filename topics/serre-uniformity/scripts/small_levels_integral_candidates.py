#!/usr/bin/env python3
"""Exact arithmetic for all candidates in the R109 complete real covers.

Non-CM candidates have an explicit split, non-scalar, nonzero-trace
Frobenius.  CM values are certified independently by reduced primitive
quadratic forms and Arb's complex modular j function, using the integral
class polynomial theorem.  Every retained CM order is inert at the level.
"""
import argparse
import gzip
import hashlib
import json
from math import gcd,isqrt
from pathlib import Path
from flint import arb,acb,ctx

LEVELS=(41,47,59,83)
CM_DISCRIMINANTS=(-3,-4,-7,-8,-11,-12,-16,-19,-27,-28,-43,-67,-163)


def forms(D):
    result=[]
    for a in range(1,isqrt((-D)//3)+1):
        for b in range(-a,a+1):
            if (b*b-D)%(4*a):continue
            c=(b*b-D)//(4*a)
            if a>c or gcd(gcd(a,b),c)!=1:continue
            if (abs(b)==a or a==c) and b<0:continue
            result.append([a,b,c])
    return result


def cm_values(bits=384):
    ctx.prec=bits;rows=[]
    for D in CM_DISCRIMINANTS:
        ff=forms(D);assert len(ff)==1
        a,b,c=ff[0]
        tau=acb(-arb(b)/(2*a),arb(-D).sqrt()/(2*a))
        value=tau.modular_j()
        j=value.real.unique_fmpz()
        assert j is not None and value.imag.contains(0)
        assert value.real.rad()<arb(2)**(-200)
        rows.append({'D':D,'reduced_forms':ff,'j':str(int(j))})
    return rows


def prime(q):
    return q>=2 and all(q%d for d in range(2,isqrt(q)+1))


def trace(j,q):
    k=j*pow((1728-j)%q,-1,q)%q
    return -sum(0 if (z:=(x**3+3*k*x+2*k)%q)==0 else
                1 if pow(z,(q-1)//2,q)==1 else -1 for x in range(q))


def obstruction(j,p):
    assert j not in (0,1728)
    for q in range(5,1000):
        if not prime(q) or q==p or j*(1728-j)%q==0:continue
        a=trace(j,q);disc=(a*a-4*q)%p
        if a%p and disc and pow(disc,(p-1)//2,p)==1:return [str(j),q,a]
    raise AssertionError(('candidate not excluded',p,j))


def cover_values(path):
    packed=path.read_bytes();cover=json.loads(gzip.decompress(packed))
    values=sorted({int(leaf[3]) for c in cover['cusps'] for h in c['branches']
                   for leaf in h['leaves'] if leaf[2]==-2})
    return values,hashlib.sha256(packed).hexdigest()


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument('--check',action='store_true')
    pa.add_argument('--levels',default=','.join(map(str,LEVELS)))
    pa.add_argument('--certificate',type=Path,default=Path(__file__).with_name('data')/'small_levels_integral_candidates.json')
    args=pa.parse_args();data=Path(__file__).with_name('data')
    levels=list(map(int,args.levels.split(',')));assert levels and all(p in LEVELS for p in levels)
    cm=cm_values();by_j={int(row['j']):row['D'] for row in cm}
    if not args.check:
        cert={'version':1,'cm_precision_bits':384,'cm_values':cm,'levels':[]}
        for p in levels:
            values,digest=cover_values(data/f'small_levels_real_cover_p{p}.json.gz')
            kept=[{'j':str(j),'D':by_j[j]} for j in values if j in by_j]
            excluded=[obstruction(j,p) for j in values if j not in by_j]
            cert['levels'].append({'p':p,'cover_sha256':digest,'all_candidates':[str(j) for j in values],
                                   'cm_candidates':kept,'excluded':excluded})
        args.certificate.write_text(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n')
    raw=args.certificate.read_bytes();cert=json.loads(raw)
    assert cert['version']==1 and cert['cm_values']==cm
    assert [r['p'] for r in cert['levels']]==levels
    for row in cert['levels']:
        p=row['p'];values,digest=cover_values(data/f'small_levels_real_cover_p{p}.json.gz')
        assert digest==row['cover_sha256']
        assert list(map(int,row['all_candidates']))==values
        accounted=[]
        for rec in row['cm_candidates']:
            j,D=int(rec['j']),rec['D']
            assert by_j[j]==D and p%2 and D%p
            assert pow(D%p,(p-1)//2,p)==p-1
            accounted.append(j)
        for jj,q,a in row['excluded']:
            j=int(jj);assert j not in by_j
            assert prime(q) and q>=5 and q!=p and j*(1728-j)%q!=0
            k=j*pow((1728-j)%q,-1,q)%q
            # Direct square multiplicity count, independent of search traces.
            counts=[0]*q
            for y in range(q):counts[y*y%q]+=1
            points=1+sum(counts[(x**3+3*k*x+2*k)%q] for x in range(q))
            assert q+1-points==a and a*a<=4*q
            disc=(a*a-4*q)%p
            assert a%p and disc and any(x*x%p==disc for x in range(1,p))
            accounted.append(j)
        assert sorted(accounted)==values and len(set(accounted))==len(values)
        print(f'p={p}: all {len(values)} candidates accounted for; {len(row["excluded"])} excluded; {len(row["cm_candidates"])} inert CM values.',flush=True)
    print('SHA256',hashlib.sha256(raw).hexdigest(),'bytes',len(raw))


if __name__=='__main__':main()
