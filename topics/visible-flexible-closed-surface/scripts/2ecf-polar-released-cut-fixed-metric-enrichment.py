#!/usr/bin/env python3
"""Actual warm same-metric enrichment on the full b..T material interval with the former .8 cut free."""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np
from scipy.interpolate import BSpline
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
ext=module(Path(__file__).parent/'2ecf-polar-released-developed-cut-to-actual-flat-collar.py','actual_released_extended')
base=ext.base
def run(a):
    prev=base.read(a.start_state)
    if a.mode=='observe':
        ext.observe(a);return
    assert prev['oldPortConstraintReleased'] and prev['targetSHA256']==base.read(a.frozen)['targetSHA256'] and prev['donorFieldSHA256']==base.sha(a.donor_field)
    class Warm(ext.impl.Implicit):
        def starting(self):
            n=prev['spans'];m=prev['modes'];x=np.array(prev['positionCoefficients'])
            assert self.ns[0]==prev['b'] and self.ns[-1]==prev['newT']
            kn=np.r_[np.zeros(4),np.arange(1,n)/n,np.ones(4)]
            B=BSpline(kn,np.eye(len(kn)-4),3)(self.t)[:,2:-2];split=B.shape[1]*(m+1);ans=[]
            for j,(v,F) in enumerate(zip((x[:split].reshape(B.shape[1],-1),x[split:].reshape(B.shape[1],-1)),self.F)):
                f=np.cos(self.u[:,None]*2*np.arange(m+1)) if j==0 else np.sin(self.u[:,None]*2*np.arange(1,m+1))
                c=np.linalg.lstsq(self.B,B@v@f.T,rcond=1e-12)[0];ans.append(np.linalg.lstsq(F,c.T,rcond=1e-12)[0].T.ravel())
            return np.concatenate(ans)
    ext.impl.Implicit=Warm
    dest=a.output
    with TemporaryDirectory(dir=dest.parent) as tmp:
        p=Path(tmp)/'step.json';a.output=p;ext.design(a);q=base.read(p)
    q.update(extendedEnrichmentEntrySHA256=base.sha(__file__),physicalPositionDonorStateSHA256=base.sha(a.start_state))
    base.stores(dest,q)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','seed-design','donor','donor-field','frozen','design','field','output','independent','start-state'):p.add_argument('--'+k,type=Path)
    for k,v in [('angles',160),('radials',193),('spans',42),('modes',16),('iterations',420),('fine-radials',1025),('fine-angles',384),('cells',128),('stored-modes',140)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',2.),('geometry',100.)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
