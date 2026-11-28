#!/usr/bin/env python3
"""Independent G11 source-only extrema on each R248 prefix span, before any Cartesian correction."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,json
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def extrema(jet,a):
    X,Xs,Xu,Xss,Xsu,Xuu=jet.swapaxes(0,1)
    inn=lambda p,q:np.einsum('...i,...i->...',p,q)
    E,F,G=inn(Xs,Xs),inn(Xs,Xu),inn(Xu,Xu)
    det=E*G-F*F
    if np.min(det)<=0:raise ValueError('Degenerate source point')
    normal=np.cross(Xs,Xu)/np.sqrt(det)[...,None]
    L,M,N=inn(normal,Xss),inn(normal,Xsu),inn(normal,Xuu)
    mean=(L*G-2*M*F+N*E)/(2*det)
    gauss=(L*N-M*M)/det
    k=np.abs(mean)+np.sqrt(np.maximum(0.,mean*mean-gauss))
    e=E-1;f=F/a;g=G/(a*a)-1
    metric=np.abs((e+g)/2)+np.hypot((e-g)/2,f)
    return metric,k


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--observer',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    d=json.loads(args.observer.read_text());nodes=np.array(d['physicalNodes']);angles=d['angles']
    for k in ('jets','radius'):
        if sha(d['files'][k])!=d['SHA256'][k]:raise ValueError('Saved source changed')
    jets=np.load(d['files']['jets'],mmap_mode='r');radius=np.load(d['files']['radius'],mmap_mode='r')
    cuts=d['basis']['newLeftBreaks']
    rows=[]
    for left,right in zip(cuts[:-1],cuts[1:]):
        ix=np.flatnonzero((nodes>=left)&(nodes<=right))
        q,k=extrema(jets[ix],radius[ix,0,None])
        def witness(v):
            i,j=np.unravel_index(np.argmax(v),v.shape)
            return dict(maximum=float(v[i,j]),s=float(nodes[ix[i]]),u=angles[j])
        rows.append(dict(left=left,right=right,radials=len(ix),angles=len(angles),metric=witness(q),curvature=witness(k)))
    with args.output.open('x') as out:
        json.dump(dict(schema='uncorrected-G11-prefix-span-extrema-v1',sourceSHA256=sha(args.observer),
                   metricReference='original a0 and unit meridian',rows=rows,finiteSamplesOnly=True),out,indent=2)
        out.write('\n')
    for r in rows: print(r['left'],r['right'],r['metric']['maximum'],r['curvature']['maximum'])
