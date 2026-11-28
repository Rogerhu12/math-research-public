#!/usr/bin/env python3
"""Include the accurate R205 tail to its flat filled pole using regular radius-squared derivatives."""
import argparse
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import numpy as np


def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m


def main():
    ap=argparse.ArgumentParser()
    for n in ('scripts','ramp','potential','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--radials',type=int,default=192);ap.add_argument('--angles',type=int,default=1024)
    ap.add_argument('--integral-panels',type=int,default=8192)
    a=ap.parse_args();here=Path(__file__).parent;S=a.scripts
    lib=load(here/'2ecf-strong-hf-upper-sector-check.py','R205_sector')
    edge=load(here/'2ecf-strong-hf-true-edge-defects.py','R205vec')
    raw=load(S/'6a65-m12-r137-continuous-domain.py','R205iv')
    b=load(S/'2ecf-strong-accurate-polar-port-budgets.py','R205port')
    K=load(S/'prefix-hull-kernel/m12-correlated-gram-interval-kernel.py','R205K');I=K.I
    with np.load(a.ramp) as r:A=F(float(r['centralA']))
    C=lib.SectorCheck(K,json.loads(a.potential.read_bytes()),I(A))
    P=a.integral_panels;R=b.RightPort(raw,P)
    loss=edge.ulp_vec(K,[raw.I(F(j,P))-pair[0] for j,pair in enumerate(R.primitives)])
    height=edge.ulp_vec(K,[pair[1] for pair in R.primitives])
    sint=edge.ulp_vec(K,[pair[0] for pair in R.ends])
    cost=edge.ulp_vec(K,[pair[1] for pair in R.ends])
    sn,cs=K.sincos(K.PI*I(2*np.arange(a.angles)+1)/a.angles)
    sn=sn.widen(K.PI/a.angles);cs=cs.widen(K.PI/a.angles)
    su=lib.iabs_box(I,sn);Z=I(F(.51))
    # Both exact parameter triples used by R265 have rUpper=cFlat+span.
    rmax=I.bounds(min(F(4,5),F(.8)),max(F(4,5),F(.8)))
    cf=I.bounds(min(F(17,50),F(.34)),max(F(17,50),F(.34)))
    span=I.bounds(min(F(23,50),F(.46)),max(F(23,50),F(.46)))
    for j in range(a.radials):
        r=rmax*I.bounds(F(j,a.radials),F(j+1,a.radials))
        yabs=su*r
        t=(yabs-cf)/span
        lo=np.maximum(0,np.minimum(1,t.lo));hi=np.maximum(0,np.minimum(1,t.hi))
        lookup=I(lo,hi)*P
        il=np.maximum(0,np.minimum(P,np.floor(lookup.lo).astype(int)))
        ih=np.maximum(0,np.minimum(P,np.ceil(lookup.hi).astype(int)))
        val=lambda table:I(table.lo[il],table.hi[ih])
        cosa=I(cost.lo[ih],cost.hi[il])
        sina=val(sint)
        # The loss primitive vanishes identically before cFlat. max(y,cFlat)
        # is thus a valid denominator also at y=0.
        denom=I(np.maximum(yabs.lo,cf.lo),np.maximum(yabs.hi,cf.hi))
        cb=1-span*val(loss)/denom
        h=span*val(height)
        flat=yabs.hi<=cf.lo
        cb=I(np.where(flat,1,cb.lo),np.where(flat,1,cb.hi))
        z=Z-I(np.where(flat,0,h.lo),np.where(flat,0,h.hi))
        cosa=I(np.where(flat,1,cosa.lo),np.where(flat,1,cosa.hi))
        sina=I(np.where(flat,0,sina.lo),np.where(flat,0,sina.hi))
        q0=cs.square()+(cb*sn).square();J=cs.square()*cosa+cb*sn.square()
        q=q0*r.square()
        xd=-F(3,2)*q0*cosa
        yd=I(np.zeros(a.angles)) if j==0 else 2*cb*su*sina/r
        if j==0 and not np.all(flat):raise ArithmeticError('First radial cell should be flat')
        C.test(cs,cb*sn,q,z,J,xd,yd,'R205 radial '+str(j),r*cs,r*cb*sn)
    out=dict(schema='2ecf-HF64-upper-disk-actual-R205-through-flat-pole-v1',entrySHA256=lib.digest(Path(__file__)),sectorSourceSHA256=lib.digest(lib.__file__),
        potentialSHA256=lib.digest(a.potential),rampSHA256=lib.digest(a.ramp),radials=a.radials,angles=a.angles,integralPanels=P,
        radialVariable='inward minus radius squared, including the disk centre by polar collapse',**C.json())
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(C.limits,flush=True)


if __name__=='__main__':main()
