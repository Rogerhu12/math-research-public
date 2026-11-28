#!/usr/bin/env python3
"""Nested XYZ update with the complete parent true center, support coefficients, original metric and cuff fixed."""
import argparse,importlib.util,json,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
if __name__=='__main__':
    here=Path(__file__).resolve().parent
    mod=load(here/'2ecf-r262-free-support-full-shape.py','r262_fixed_center_solver')
    p=argparse.ArgumentParser()
    for k in ('scripts','data','grid','query-report','query-cache','field','output','parent'):p.add_argument('--'+k,required=True,type=Path)
    p.add_argument('--spans',type=int,default=48);p.add_argument('--modes',type=int,default=21);p.add_argument('--steps',type=int,default=5);p.add_argument('--train-radial',type=int,default=192);p.add_argument('--train-angular',type=int,default=181);a=p.parse_args()
    parent=json.loads(a.parent.read_bytes());a.eta=parent['eta'];a.support_max=len(parent['support'])+2
    if parent.get('widthConstraintSourceSHA256') or parent.get('twoConstraints'):
        mod.directions=load(here/'2ecf-r262-fixed-width-free-support.py','r262_width_formula').directions
        two=True
    else:two=False
    src=mod.base.Source(a);q=np.array(parent['support']);x=mod.refine(np.array(parent['xyz']),parent['spans'],parent['modes'],a.spans,a.modes)
    def make(n,m,k,shift):
        g=mod.Fit(src,src.old(n,m,k,shift),a);g.change(q);return g.core
    g=make(a.train_radial,74,a.train_angular,False);obs=[g.metrics(x)];hist=[];print('actual previous',obs[0],flush=True)
    for i in range(a.steps):
        old=obs[-1];ok=False
        for reg in (.0000003,.00002,.001):
            dx=g.step(x,reg,min(5,1.5+i*.6))
            for scale in (1,.5,.25,.125,.0625):
                r=g.metrics(x+scale*dx)
                if r['metric']<old['metric']*(1-1e-5) and r['curvature']<max(10.15,old['curvature']+.01):
                    x+=scale*dx;obs.append(r);hist.append(dict(reg=reg,scale=scale));ok=True;print('accepted',i,r,flush=True);break
            if ok:break
        if not ok:break
    res=[]
    for c in [(253,93,258,False),(231,101,287,True)]:
        gg=make(*c);res.append(dict(radial=len(gg.z),angular=len(gg.t),actual=gg.metrics(x),original=gg.metrics(x,True)));print('ind',res[-1],flush=True)
    out=dict(schema='R262-fixed-full-true-center-and-original-g-nested-position-physical-v1',entrySHA256=mod.base.sha(__file__),sourceFieldSHA256=mod.base.sha(a.field),parentSHA256=mod.base.sha(a.parent),eta=a.eta,spans=a.spans,modes=a.modes,xyz=x.tolist(),support=q.tolist(),twoConstraints=two,training=obs,history=hist,observers=res,originalG=True,unchangedCompleteCentralSupport=True)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
