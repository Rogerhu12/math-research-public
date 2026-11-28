#!/usr/bin/env python3
"""Cover all corrected physical-HF heights and all points which could exceed the cuff plane."""
import argparse
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np


def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser()
    for n in ('scripts','field','edge-defects','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--angles',type=int,default=512);a=ap.parse_args();here=Path(__file__).parent
    inside=load(here/'2ecf-strong-hf-interior-continuous-projection.py','pos_inside')
    edges=load(here/'2ecf-strong-hf-edge-continuous-projection.py','pos_edges')
    lib=load(here/'2ecf-strong-hf-upper-sector-check.py','pos_lib')
    K=load(a.scripts/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','pos_K');I=K.I
    ep=json.loads(a.edge_defects.read_bytes());a.with_proxy_edges=False
    if ep['fieldSHA256']!=lib.digest(a.field):raise ValueError('Edge correction applies to another field')
    inside_rows,M=inside.makepieces(K,a);end_rows,_=edges.makepieces(K,a)
    rows=sorted([(l,r,p,None,None) for l,r,p in inside_rows]+end_rows,key=lambda x:x[0])
    H=inside.Harmonics(K,a.angles,M);highest=-1;clearance=100;Z=F(.51);hit=0
    for l,r,p,side,k in rows:
        P=H.boxes(p,0);s=(l+r)/2;P0,P1=inside.split(I,P,I(F(1,2)))
        for ll,rr,S in ((l,s,P0),(s,r,P1)):
            v=I(np.min(S.lo,axis=0),np.max(S.hi,axis=0))
            if side is not None:v=v.widen(edges.hermite_error(K,side,k,ll,rr,ep['bounds'])[0])
            x,y,z=[v[:,i] for i in range(3)]
            highest=max(highest,lib.outward(z.hi,1))
            possible=z.hi>I(Z).lo
            if np.any(possible):
                hit+=np.count_nonzero(possible)
                clearance=min(clearance,lib.outward((x.square()+y.square()).lo[possible],-1))
    out=dict(schema='HF64-actual-height-and-radial-location-of-all-possible-excess-v1',entrySHA256=lib.digest(Path(__file__)),fieldSHA256=lib.digest(a.field),
        edgeDefectsSHA256=lib.digest(a.edge_defects),angles=a.angles,originalCommonElements=len(rows),closedBoxes=2*a.angles*len(rows),
        upperHeight=highest,lowerRadiusSquaredWheneverHeightExceedsCuff=clearance,boxesPossiblyAboveCuff=int(hit),cuffHeightExact=str(Z))
    with a.output.open('x') as h:json.dump(out,h,indent=2);h.write('\n')
    print(out,flush=True)


if __name__=='__main__':main()
