#!/usr/bin/env python3
"""Optimize a genuine elevated cuff and complementary shortened throat, preserving both physical jets and all fixed cap bodies."""
import argparse
import hashlib
import importlib.util
import json
import os
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np

def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
move=module(here/'2ecf-polar-released-moving-actual-flat-cuff-and-throat.py','joint_real_shift_throat')
pa=move.pa;cart=pa.cart;ext=pa.ext;base=pa.base
def project(q,b,T,spans,modes):
    ns=np.linspace(b,T,181);u=2*np.pi*np.arange(128)/128
    old=cart.Basis(ns,u,b,T,q['spans'],q['modes']);new=cart.Basis(ns,u,b,T,spans,modes);x=np.asarray(q['coefficients']).reshape(old.shape)
    vals=[]
    for k in range(3):
        v=np.linalg.lstsq(new.B[0],(old.B[0]@x[k])@old.F[k][0].T,rcond=1e-13)[0]
        vals.append(np.linalg.lstsq(new.F[k][0],v.T,rcond=1e-13)[0].T.ravel())
    return np.concatenate(vals)
def run(a):
    sol=None
    if a.mode=='observe':
        sol=base.read(a.solution)
        assert sol['trueHigherCuffEntrySHA256']==base.sha(__file__)
        a.delta=sol['raisedCuffDelta'];a.t0,a.t1=sol['transition']
    assert 0<a.delta<.095 and 0<=a.t0<a.t1<=1.
    ends,ref,b,S,T,rf,g=ext.setup(a);oldclass=base.MaterialField;oldsetup=ext.setup;oldgroups=cart.lift.load_groups;oldpairs=pa.Pairs
    class Raised(oldclass):
        def __init__(self,path,ends):
            super().__init__(path,ends);self.active=Path(path).resolve()==a.field.resolve()
        def position(self,ns,u):
            js=super().position(ns,u)
            if self.active:move.add(js,ns,b,T,a.t0,a.t1,a.delta)
            return js
    base.MaterialField=Raised
    def setup(args):
        e,*out=oldsetup(args)
        e.raised.tall_config=lambda pt:lambda **kwargs:move.config_from_class(pt,kwargs,a.delta)
        return (e,*out)
    # Retain the original validator independently of the true raised height allowance.
    def from_class(original,de,delta):
        class New(original):
            def __post_init__(self):
                old={k:getattr(self,k) for k in self.__dataclass_fields__};old['height_maximum']=.0195;original(**old)
                assert abs(self.true_cuff_height+self.height_maximum-.528)<1e-14
        return New(**dict(de,true_cuff_height=.415+delta,height_maximum=.113-delta))
    move.config_from_class=from_class;ext.setup=setup
    def load_groups(*args):
        gs,ev,*rest=oldgroups(*args)
        for ns,u,js,rr,w in gs.values():js[ns>T,0,:,2]+=a.delta
        return (gs,ev,*rest)
    cart.lift.load_groups=load_groups
    class NewPairs(oldpairs):
        def __init__(self,a,ns,u):
            super().__init__(a,ns,u);self.ref[self.ns>T,0,:,2]+=a.delta
    pa.Pairs=NewPairs
    desc=dict(connectorTarget=g['targetSHA256'],Z=(.415+a.delta).hex(),eta=(.115-a.delta).hex(),throat='R273 genuine q_eta and L=8eta/(3pi), same Z+eta=53/100',deltaHex=a.delta.hex())
    identity=hashlib.sha256(json.dumps(desc,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    out=a.output
    with TemporaryDirectory(dir=out.parent) as tmp:
        if a.mode=='design':
            warm=a.start;q=base.read(warm);true_warm=base.sha(warm)
            assert q['sourceFieldSHA256']==base.sha(a.field)
            if (q['spans'],q['modes'])!=(a.spans,a.modes):
                x=project(q,b,T,a.spans,a.modes);q.update(spans=a.spans,modes=a.modes,coefficients=x.tolist())
                a.start=Path(tmp)/'projected.json';base.stores(a.start,q)
        inner=Path(tmp)/'done.json';a.output=inner;pa.run(a);data=base.read(inner)
    data.update(trueHigherCuffEntrySHA256=base.sha(__file__),raisedCuffDelta=a.delta,transition=[a.t0,a.t1],closedGeometryIdentity=identity,familyDescription=desc)
    if a.mode=='design':data['actualPredecessorSHA256']=true_warm
    if sol:assert sol['closedGeometryIdentity']==identity
    base.stores(out,data)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','solution','start','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('radials',129),('angles',88),('spans',18),('modes',7),('iterations',300)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',18.),('geometry',100.),('guard',200000.),('held',.6535),('separation',.32),('neighbors',.25),('ball-radius',.101),('delta',.08),('t0',0.),('t1',1.)]:p.add_argument('--'+k,type=float,default=v)
    p.add_argument('--pair-kind',choices=('ball','chord'),default='ball');p.add_argument('--pair-weights',type=float,nargs='+',default=[350.,6000.,40000.]);run(p.parse_args())
