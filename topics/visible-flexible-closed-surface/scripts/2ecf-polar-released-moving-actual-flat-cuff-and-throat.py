#!/usr/bin/env python3
"""Raise the actual released planar exit and shorten its true cap throat while preserving the fixed convex bodies."""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
pa=module(here/'2ecf-polar-released-physical-nonlocal-normal-ball-optimization-line-search.py','raised_true_cuff_pairs')
cart=pa.cart;base=cart.base;ext=cart.ext
def profile(ns,b,T,t0,t1):
    tau=(ns-b)/(T-b);w=(t1-t0)*(T-b);t=np.clip((tau-t0)/(t1-t0),0.,1.)
    return np.stack([t**3*(10+t*(-15+6*t)),30*t**2*(1-t)**2/w,60*t*(1-t)*(1-2*t)/w**2])
def add(j,ns,b,T,t0,t1,delta):
    W=profile(ns,b,T,t0,t1)
    for k,v in zip((0,1,3),W):j[:,k,:,2]+=delta*v[:,None]
def config(point,de,delta):
    class C(point.PointConfig):
        def __post_init__(self):
            old={k:getattr(self,k) for k in self.__dataclass_fields__};old['height_maximum']=.0195;point.PointConfig(**old)
            assert abs((self.true_cuff_height+self.height_maximum)-.528)<1e-14
    return C(**dict(de,true_cuff_height=.415+delta,height_maximum=.113-delta))
def run(a):
    sol=base.read(a.solution);x=np.array(sol['coefficients']);a.spans=sol['spans'];a.modes=sol['modes']
    groups,undef,b,T,A=cart.lift.load_groups(a,('training','observer','independent','tail193x272'))
    assert sol['sourceFieldSHA256']==base.sha(a.field) and sol['sourceStateSHA256']==base.sha(a.state)
    ends,ref,b,S,T,rf,g=ext.setup(a);pre=base.read(a.prepared)
    stream=module(a.scripts/'6a65-cartesian-complete-stream.py','moving_cuff_full_rows');area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','moving_cuff_area')
    scan=module(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','moving_cuff_observe')
    for k,(ns,u,j,rr,w) in groups.items():j+=cart.Basis(ns,u,b,T,a.spans,a.modes).apply(x)
    ns=np.linspace(b,T,a.radials);u=2*np.pi*np.arange(a.angles)/a.angles
    a.separation=.32;a.neighbors=.238;a.ball_radius=.097;a.pair_kind='ball'
    pairs=pa.Pairs(a,ns,u);raw=pairs.ref.copy()
    rows=[]
    for t0,t1 in [(0.,1.),(.38,.94),(.52,.94)]:
        for delta in a.deltas:
            cfg=config(stream.point,pre['definition']['pointConfig'],delta)
            out={}
            for key,(ns,u,j,rr,w) in groups.items():
                v=j.copy();add(v,ns,b,T,t0,t1,delta)
                out[key]=scan.evaluate(stream,stream.point,area,v,rr,ns,u,cfg,w)
            pairs.ref[:]=raw;add(pairs.ref,pairs.ns,b,T,t0,t1,delta)
            pairs.ipair=np.empty(0,dtype=np.int64);pairs.jpair=pairs.ipair.copy();pairs.update(x)
            pair=pairs(x,1.,False);r=out['independent']
            print(t0,t1,delta,r['metric'],r['curvature'],r['held'],pair['minNormalRatio'],pair['minDistance'],flush=True)
            rows.append(dict(t0=t0,t1=t1,delta=delta,Z=.415+delta,eta=.115-delta,rows=out,farUpperAndFlatAnnulus=pair))
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),fieldSHA256=base.sha(a.field),sourceStateSHA256=base.sha(a.state),cartesianSolutionSHA256=base.sha(a.solution),fixedConnectorMetricSHA256=g['targetSHA256'],throatFamily='Z=83/200+delta, eta=23/200-delta; fixed Z+eta=53/100, genuine meridian L=8eta/(3pi), true open planar exit and full original top/bottom convex caps',rows=rows,extraFarGrid=[a.radials,a.angles],optimizerAccepts=0))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','solution','output'):p.add_argument('--'+k,type=Path)
    p.add_argument('--deltas',type=float,nargs='+',default=[.04,.06,.08,.09]);p.add_argument('--radials',type=int,default=113);p.add_argument('--angles',type=int,default=96)
    run(p.parse_args())
