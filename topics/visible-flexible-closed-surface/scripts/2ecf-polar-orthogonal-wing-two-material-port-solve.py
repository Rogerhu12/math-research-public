#!/usr/bin/env python3
"""A fresh physical meridian solve at either genuinely two-wing port, with a named previous tangent coefficient donor."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import os
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np
from scipy.interpolate import BSpline
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
here=Path(__file__).parent
parent=module(here/'2ecf-polar-material-implicit-coupled-radius.py','two_wing_frozen_metric')
base=parent.base
wing=module(here/'2ecf-polar-orthogonal-disjoint-wing-developable-port.py','two_wing_endpoint_evaluator')
class NewPort(parent.Designed):
    def starting(self):
        d=base.read(self.args.start);n=d['spans'];M=d['modes'];x=np.asarray(d['positionCoefficients'])
        kn=np.r_[np.zeros(4),np.arange(1,n)/n,np.ones(4)]
        B=BSpline(kn,np.eye(len(kn)-4),3)(self.t)[:,2:-2];split=B.shape[1]*(M+1);out=[]
        for i,(V,F) in enumerate(zip((x[:split].reshape(B.shape[1],-1),x[split:].reshape(B.shape[1],-1)),self.F)):
            f=np.cos(self.u[:,None]*2*np.arange(M+1)) if i==0 else np.sin(self.u[:,None]*2*np.arange(1,M+1))
            a=np.linalg.lstsq(self.B,B@V@f.T,rcond=1e-12)[0]
            out.append(np.linalg.lstsq(F,a.T,rcond=1e-12)[0].T.ravel())
        return np.concatenate(out)
def run(a):
    d=base.read(a.seed_design);assert d['orthogonalPortSHA256']==base.sha(wing.__file__)
    base.end_module=lambda here,seed:wing
    parent.Designed=NewPort
    dest=a.output
    with TemporaryDirectory(dir=dest.parent) as tmp:
        p=Path(tmp)/'solve.json';a.output=p
        if a.mode=='design':parent.design(a)
        else:parent.observe(a)
        q=base.read(p)
    q.update(orthogonalActualSolverEntrySHA256=base.sha(__file__),trueTwoWingEndpointSourceSHA256=base.sha(wing.__file__),longAxisAmplitude=d['amp'],shortAxisAmplitude=d['flat'])
    base.stores(dest,q)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','field','output','seed-field','seed-design','design','independent','start','frozen'):p.add_argument('--'+k,type=Path)
    for k,v in [('angles',128),('radials',121),('spans',24),('modes',12),('iterations',250),('fine-radials',769),('fine-angles',320),('cells',96),('stored-modes',100),('trace-nodes',2048),('radius-spans',12)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('closure',0.),('curvature',3.),('geometry',180.)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
