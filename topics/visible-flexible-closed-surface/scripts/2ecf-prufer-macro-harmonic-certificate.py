"""Global outward-rounded Bernstein bounds for a frozen binary64 feedback field."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import numpy as np


def exact(a):
    return np.asarray(a),np.asarray(a)


def add(a,b):
    return np.nextafter(a[0]+b[0],-np.inf),np.nextafter(a[1]+b[1],np.inf)


def sub(a,b):
    return np.nextafter(a[0]-b[1],-np.inf),np.nextafter(a[1]-b[0],np.inf)


def mul(a,b):
    p=[x*y for x in a for y in b]
    return np.nextafter(np.minimum.reduce(p),-np.inf),np.nextafter(np.maximum.reduce(p),np.inf)


def div(a,b):
    if np.any(b[0]<=0):
        raise ValueError("the denominator must stay positive")
    return mul(a,(np.nextafter(1/b[1],-np.inf),np.nextafter(1/b[0],np.inf)))


def bound(data,coeff,endpoint=1.0):
    raw=json.loads(Path(data).read_text())
    m=raw.get('fundamental',2)
    units={2:(Q('3.5e-10'),65,26,Q('.64'),Q('.004')),3:(Q('8e-11'),220,60,Q('.838'),Q('.002'))}
    epsilon,seed,gram_bound,lower_r,vertical_tangent=units[m]
    if raw['outerAnchor']!=1 or Q(str(raw['normalizedEpsilon']))!=epsilon or (m==3 and raw['slope']!=.000055):
        raise ValueError("different physical baseline")
    if endpoint!=1 and (endpoint!=1.35 or raw.get('macro',{}).get('Rend')!=endpoint):
        raise ValueError("unsupported analytic macro domain")
    R=np.asarray(raw['rows'])[:,3]
    z=np.load(coeff);v=z['delta'];d=z['derivative'];dd=z['second']
    if (len(R)!=len(v) or v.shape!=d.shape or d.shape!=dd.shape or R[-1]!=endpoint
        or not np.all(np.diff(R)>0) or not np.all(np.isfinite(v+d+dd))
        or np.any(v[0]) or np.any(d[0]) or np.any(dd[0]) or v[-1,2,1]!=0):
        raise ValueError("invalid radial grid, flat relative inner join or outer second mode")
    h=sub(exact(R[1:,None,None]),exact(R[:-1,None,None]));h2=mul(h,h)
    l,r=exact(v[:-1]),exact(v[1:])
    ht0,ht1=div(mul(h,exact(d[:-1])),exact(5)),div(mul(h,exact(d[1:])),exact(5))
    at0,at1=div(mul(h2,exact(dd[:-1])),exact(20)),div(mul(h2,exact(dd[1:])),exact(20))
    B=[l,add(l,ht0),add(add(l,mul(exact(2),ht0)),at0),
       add(sub(r,mul(exact(2),ht1)),at1),sub(r,ht1),r]
    D=[div(mul(exact(5),sub(b,a)),h) for a,b in zip(B,B[1:])]
    maximum=lambda values: np.maximum.reduce([np.max(np.maximum(abs(lo),abs(hi)),axis=0) for lo,hi in values])
    mv=maximum(B);md=maximum(D)
    # Subsequent sums are exact rationals, including the represented upper endpoints.
    exact_matrix=lambda x:[[Q.from_float(float(q)) for q in row] for row in x]
    bv,bd=exact_matrix(mv),exact_matrix(md)
    a,b,c=bv;fr=list(range(0,m*len(a),m));rr=[sum(row) for row in bd]
    # R_c=.371/r_* is greater than .64 by R325.
    ur=[sum(m*v+w for m,v,w in zip(fr,a,b)),sum(v+m*w for m,v,w in zip(fr,a,b)),sum(m*v for m,v in zip(fr,c))]
    ur=[q/lower_r for q in ur]
    er,eu=[Q('1.000001'),Q('1e-9'),vertical_tangent],[Q('1e-7'),Q('1.000001'),Q('1e-7')]
    ip=lambda x,y:sum(a*b for a,b in zip(x,y))
    E=2*ip(er,rr)+ip(rr,rr)
    F=ip(er,ur)+ip(eu,rr)+ip(rr,ur)
    G=2*ip(eu,ur)+ip(ur,ur)
    baseline=gram_bound*(seed*epsilon)**2
    op=baseline+max(E,G)+F
    digests={}
    for key,arr in [('radius',R),('position',v),('first',d),('second',dd)]:
        digests[key]=hashlib.sha256(np.ascontiguousarray(arr,dtype='<f8').tobytes()).hexdigest()
    # Rendering produces convenient approximations. The assertion compares exact rational bounds.
    if op>=Q('2e-9'):
        raise ValueError('whole continuous field exceeds the requested certificate budget')
    return dict(radii=len(R),maximum_true_angular_order=m*(v.shape[2]-1),hashes=digests,
                derivative=[float(x) for x in rr],angular_over_radius=[float(x) for x in ur],
                continuous_bound_display=float(op),certified_less_than_2e_9=True)


if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('data');a.add_argument('coeff');a.add_argument('--endpoint',type=float,default=1.35);q=a.parse_args()
    print(json.dumps(bound(q.data,q.coeff,q.endpoint),indent=2))
