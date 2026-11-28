#!/usr/bin/env python3
"""Exact convexity of the native R262 center and its complete positive-radius normalization."""
import argparse,gzip,hashlib,json,math
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
def exact_polynomial(cheb):
    p=[[Q(1)],[Q(0),Q(1)]]
    for k in range(2,len(cheb)):
        v=[Q(0)]+[2*x for x in p[-1]]
        for j,x in enumerate(p[-2]):v[j]-=x
        p.append(v)
    a=[Q(0)]*len(cheb)
    for j,v in enumerate(cheb):
        for i,x in enumerate(p[j]):a[i]+=v*x
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def bound(cheb,n=16):
    c=exact_polynomial(cheb);D=len(c)-1;bounds=[]
    for j in range(n):
        q=Q(2*j-n,n);h=Q(2,n)
        p=[sum(c[k]*math.comb(k,i)*q**(k-i)*h**i for k in range(i,D+1)) for i in range(D+1)]
        b=[sum(p[i]*Q(math.comb(k,i),math.comb(D,i)) for i in range(k+1)) for k in range(D+1)]
        bounds.extend([min(b),max(b)])
    return min(bounds),max(bounds)
def run(path):
    with gzip.open(path,'rb') as z:
        with np.load(z) as f:c=[Q(float(x)) for x in f['jets'][0,0]]
    M=(len(c)-2)//3;assert not any(c[2*M+1:]);a={1:c[0]}
    for j in range(1,M+1):a[1+3*j]=(c[j]+c[M+j])/2;a[1-3*j]=(c[j]-c[M+j])/2
    terms=[[Q(0)]*(2*M+1) for _ in range(3)]
    for k,x in a.items():
        terms[2][abs(k-1)//3]+=k*x
        for l,y in a.items():
            j=abs(k-l)//3;terms[0][j]+=k*l*l*x*y;terms[1][j]+=k*l*x*y
    out={}
    for name,cs in zip(('turnDeterminant','speedSquared','coRotatingTangentReal'),terms):
        lo,hi=bound(cs);assert lo>0;out[name]=[str(lo),str(hi)]
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',required=True,type=Path);p.add_argument('--out',required=True,type=Path);a=p.parse_args()
    h=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
    r=dict(schema='exact-R262-normalized-central-curve-strict-convexity-and-turning-one-v1',entrySHA256=h(__file__),sourceSHA256=h(a.data),ranges=run(a.data))
    with a.out.open('x') as f:json.dump(r,f,indent=2);f.write('\n')
    print({k:[float(Q(x)) for x in z] for k,z in r['ranges'].items()})
