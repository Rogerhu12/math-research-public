#!/usr/bin/env python3
"""Certify the complete corrected physical connector for a whole-disk potential."""
import argparse
import importlib.util
import json
import os
from fractions import Fraction as F
from pathlib import Path
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def main():
    ap=argparse.ArgumentParser()
    for name in ('scripts','field','ramp','potential','edge-defects','output'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--portion',choices=('interior','ends'),required=True)
    ap.add_argument('--depth',type=int,default=2)
    args=ap.parse_args()
    base=Path(__file__).parent
    lib=load(base/'2ecf-strong-hf-upper-sector-check.py','hf_upper_checks')
    inside=load(base/'2ecf-strong-hf-interior-continuous-projection.py','hf_upper_in')
    ends=load(base/'2ecf-strong-hf-edge-continuous-projection.py','hf_upper_edges')
    K=load(args.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','hf_upper_K')
    with np.load(args.ramp) as z:A=F(float(z['centralA']))
    c=json.loads(args.potential.read_bytes());edge=json.loads(args.edge_defects.read_bytes())
    if c['fieldSHA256']!=edge['fieldSHA256'] or c['fieldSHA256']!=lib.digest(args.field):raise ValueError('Field identity mismatch')
    args.with_proxy_edges=False
    if args.portion=='interior':
        pieces,M=inside.makepieces(K,args);pieces=[(a,b,p,None,None) for a,b,p in pieces]
    else:pieces,M=ends.makepieces(K,args)
    I=K.I;harm=inside.Harmonics(K,args.angles,M)
    check=lib.SectorCheck(K,c,I(A));rows=[]
    for a,b,ctrl,side,ks in pieces:
        P=harm.boxes(ctrl,0);V=harm.boxes(5*(ctrl[1:]-ctrl[:-1])/I(b-a));U=harm.boxes(ctrl,1)
        subs=[(a,b,[P,V,U])]
        for j in range(args.depth):
            result=[]
            for l,r,S in subs:
                split=[inside.split(I,p,I(F(1,2))) for p in S];mid=(l+r)/2
                result.extend([(l,mid,[q[0] for q in split]),(mid,r,[q[1] for q in split])])
            subs=result
        for l,r,controls in subs:
            vals=[I(np.min(v.lo,axis=0),np.max(v.hi,axis=0)) for v in controls]
            if side is not None:
                err=ends.hermite_error(K,side,ks,l,r,edge['bounds'])
                vals=[v.widen(e) for v,e in zip(vals,err)]
            check.cartesian(*[[v[:,j] for j in range(3)] for v in vals],str(l)+','+str(r))
        rows.append([str(a),str(b)])
    obs=check.json()
    out=dict(schema='2ecf-HF64-upper-disk-whole-corrected-suffix-piece-v1',entrySHA256=lib.digest(Path(__file__)),sectorSourceSHA256=lib.digest(lib.__file__),
             fieldSHA256=lib.digest(args.field),potentialSHA256=lib.digest(args.potential),edgeDefectsSHA256=lib.digest(args.edge_defects),angles=args.angles,
             radialDepth=args.depth,portion=args.portion,physicalSpans=rows,**obs)
    with args.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(obs['bounds'],flush=True)


if __name__=='__main__':main()
