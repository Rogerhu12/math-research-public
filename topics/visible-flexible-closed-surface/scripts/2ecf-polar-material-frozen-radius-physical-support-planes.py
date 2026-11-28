#!/usr/bin/env python3
"""The actual unit-meridian frozen-g objective with two explicit spatial support-plane residuals."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import numpy as np
def module(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
parent=module(Path(__file__).parent/'2ecf-polar-material-implicit-coupled-radius.py','unit_radius_plane_parent')
base=parent.base;imp=parent.impl
class Plane(parent.Designed):
    def value(self,x,with_gradient=True):
        original=super().value(x,with_gradient)
        P,_,_,_,(tang,der,U,q,Qs,Us,H,h,hp)=self.field(x)
        limit=self.ends.master.A-.65*np.sqrt(2.)
        y,z=P[...,1],P[...,2]
        active=np.maximum(0.,np.stack([y-z-limit,-y-z-limit],axis=-1))
        w=self.weights['metric'][...,None]*self.args.plane
        tau=self.args.plane_tau
        penalty=float(np.sum(w*(active**2+active**4/tau**2)))
        if not with_gradient:
            original['originalDesignTotal']=original['designTotal']
            original['designTotal']+=penalty
            original.update(planePenalty=penalty,planeMaxViolation=float(max(0.,np.max(np.abs(y)-z-limit))))
            return original
        loss,g=original
        bar=2*w*active*(1+2*active**2/tau**2)
        bp=np.stack([np.zeros_like(y),bar[...,0]-bar[...,1],-bar[...,0]-bar[...,1]],axis=-1)
        bvel=base.local(np.einsum('ij,iuc->juc',self.I,bp,optimize=True),self.u)
        bQ=imp.Japply(U,q,self.v[...,None]*bvel)
        m=np.linalg.solve(H,np.sum(h*bQ,axis=0)[...,None])[...,0]
        bT=bQ-(self.I[-1,:,None]*self.v)[...,None]*imp.Japply(U,q,m[None])
        parts=[((self.B.T@imp.dot(bT,dT))@F).ravel() for dT,F in zip(tang[1:3],self.F)]
        dg=np.concatenate(parts);assert len(g)==len(dg) and self.args.frozen is not None
        return loss+penalty,g+dg
def run(a):
    dest=a.output
    parent.Designed=Plane
    if a.mode=='observe':
        # Only spatial merit changed; the original saved radius identity is authoritative.
        parent.observe(a)
        return
    with TemporaryDirectory(dir=dest.parent) as temp:
        target=Path(temp)/'designed.json';a.output=target;parent.design(a);result=base.read(target)
    result.update(planeEntrySHA256=base.sha(__file__),planeWeight=a.plane,planeTau=a.plane_tau,physicalPlaneThreshold='central A minus .65 sqrt(2), both signs of material y',holdsOriginal14PositiveRows=True)
    base.stores(dest,result)
if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','field','output','seed-field','seed-design','design','independent','start','frozen'):a.add_argument('--'+k,type=Path)
    for k,v in [('angles',152),('radials',145),('spans',32),('modes',15),('iterations',350),('fine-radials',769),('fine-angles',320),('cells',96),('stored-modes',100),('trace-nodes',2048),('radius-spans',12)]:a.add_argument('--'+k,type=int,default=v)
    for k,v in [('closure',0.),('curvature',7.),('geometry',180.),('plane',3500.),('plane-tau',.02)]:a.add_argument('--'+k,type=float,default=v)
    run(a.parse_args())
