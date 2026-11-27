#!/usr/bin/env python3
"""Exact pairwise QQ Bezout and monic 1009-integral product of the nine fixed factors.
The original-resultant divisibilities are proved by the separate original-matrix
certificates; this source only certifies their coprimality/product arithmetic.
"""
from flint import fmpq,fmpq_poly
from pathlib import Path
import json,hashlib,time,resource
start=time.perf_counter()
factors=[['w', ['0', '1'], 815], ['w-1', ['-1', '1'], 203], ['w+1', ['1', '1'], 63], ['w+half', ['1/2', '1'], 41], ['J2a', ['3/2', '2', '1'], 107], ['J2b', ['1/2', '1', '1'], 36], ['J3', ['-3/4', '-1/4', '1', '1'], 5], ['J6', ['-1/28', '5/56', '1/14', '4/7', '75/28', '20/7', '1'], 12], ['J10', ['3/32', '-23/32', '-1/4', '-255/32', '-281/8', '-1773/32', '-69/16', '115/4', '4', '-6', '1'], 4]]
ps=[fmpq_poly([fmpq(c) for c in cs]) for _,cs,_ in factors];records=[]
for i in range(len(ps)):
 for j in range(i):
  g,a,b=ps[i].xgcd(ps[j]);assert g==1 and a*ps[i]+b*ps[j]==1
  records.append({'factors':[factors[i][0],factors[j][0]],'coefficientDegrees':[a.degree(),b.degree()],'identitySha256':hashlib.sha256((str(a)+'|'+str(b)).encode()).hexdigest()})
Q=fmpq_poly([1])
for pp,(_,_,e) in zip(ps,factors):
 assert pp.leading_coefficient()==1;Q*=pp**e
assert len(records)==36 and Q.degree()==1535 and Q.leading_coefficient()==1 and all(int(a.denominator)%1009 for a in Q)
assert hashlib.sha256(str(Q).encode()).hexdigest()=='2815302d3c784772217a5a4512c43363db76bf4e799ec4ca69c83ede4a4bf51c'
print(json.dumps({'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'factors':factors,'pairwiseBezoutIdentities':len(records),'records':records,'productDegree':Q.degree(),'productMonic':True,'product1009Integral':True,'productCoefficientSha256':hashlib.sha256(str(Q).encode()).hexdigest(),'seconds':time.perf_counter()-start,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'wholeL0Excluded':False},indent=2))
