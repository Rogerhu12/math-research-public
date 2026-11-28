#!/usr/bin/env python3
"""Actual fixed cap floor separation, marked width, dense exit curvature and two-way remote normal-ball rows."""
import argparse
import importlib.util
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
hi=module(here/'2ecf-polar-released-higher-cuff-true-spatial-design-checkpoint.py','capped_physical_solver')
pa=hi.pa;cart=hi.cart;ext=hi.ext;base=hi.base
def run(a):
    if a.mode=='observe':
        q=base.read(a.solution)
        assert q['physicalCapRoofEntrySHA256']==base.sha(__file__)
        a.cap=q['completeRigidCaps'];hi.run(a);return
    rawclass=pa.Pairs
    new=a.cap=='R293';Z=.415+a.delta;level=.632 if new else .5295
    details=[]
    class WithCap(rawclass):
        def __init__(self,a,ns,u):
            super().__init__(a,ns,u)
            ends,ref,b,S,T,rf,g=ext.setup(a)
            n=T-.075+.075*(np.arange(35)+.327)/35;v=2*np.pi*(np.arange(100)+.411)/100
            model=base.MaterialField(a.field,ends)
            self.tail=np.concatenate([model.position(n[i:i+10],v) for i in range(0,len(n),10)])
            self.tb=cart.Basis(n,v,b,T,a.spans,a.modes)
            self.tw=np.full((len(n),1),a.exit_curvature/(len(n)*len(v)))
            self.point=module(a.scripts/'6a65-cartesian-complete-stream.py','explicit_tail_kappa').point
            self.cfg=hi.move.config(self.point,base.read(a.prepared)['definition']['pointConfig'],a.delta)
            self.radius=(.8+S-n)[:,None]
        def __call__(self,x,weight,gradient=True):
            initial=super().__call__(x,weight,gradient)
            js=self.ref+self.basis.apply(x);P=js[:,0];rho=np.hypot(P[...,0],P[...,1])
            t=np.clip((rho-.514)/.026,0,1)
            allow=Z+(level-Z)*t**3*(10+t*(-15+6*t))
            deriv=(level-Z)*30*t*t*(1-t)**2/.026
            dz=np.maximum(P[...,2]-allow,0);dy=np.maximum(abs(P[...,1])-a.width_mark,0)
            loss=(a.roof_weight*np.sum(dz*dz)+a.width_weight*np.sum(dy*dy))/self.num
            tail=self.tail+self.tb.apply(x)
            zero=np.zeros_like(self.tw)
            pt=self.point.PointLinearized(tail.swapaxes(1,2),self.radius,self.cfg,dict(metric=zero,curvature=self.tw,geometry=zero))
            loss+=float(np.sum(pt.residual**2))
            if not gradient:
                vv=dict(initial);vv['loss']+=loss
                vv.update(roofHeight=level,maxSignedRoof=float(np.max(P[...,2]-allow)),maxWidth=float(np.max(abs(P[...,1]))),denseExitKappa=float(np.max(abs(pt.curvature['eigenvalues']))))
                return vv
            loss0,grad=initial;adj=np.zeros_like(js)
            dw=2*a.roof_weight*dz/self.num
            adj[:,0,:,2]=dw
            adj[:,0,:,0]=-dw*deriv*P[...,0]/np.maximum(rho,1e-9)
            adj[:,0,:,1]=-dw*deriv*P[...,1]/np.maximum(rho,1e-9)+2*a.width_weight*dy*np.sign(P[...,1])/self.num
            gtail=2*pt.vjp(pt.residual).swapaxes(1,2)
            return loss0+loss,grad+self.basis.transpose(adj)+self.tb.transpose(gtail)
    pa.Pairs=WithCap;out=a.output
    with TemporaryDirectory(dir=out.parent) as tmp:
        inner=Path(tmp)/'finish.json';a.output=inner;hi.run(a);q=base.read(inner)
    q.update(physicalCapRoofEntrySHA256=base.sha(__file__),completeRigidCaps=a.cap,physicalCapBaseSum='.635' if new else '.53',actualCuffHeight=Z,actualThroatIncrease=(.635 if new else .53)-Z,roofWindow=[.514,.540],capRoofFarLevel=level,widthTarget=a.width_mark,independentExitGrid=[35,100,.075],extraCurvatureWeight=a.exit_curvature)
    base.stores(out,q)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','solution','start','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('radials',113),('angles',76),('spans',19),('modes',7),('iterations',270)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',24.),('geometry',110.),('guard',300000.),('held',.655),('separation',.32),('neighbors',.245),('ball-radius',.101),('delta',.065),('t0',0.),('t1',1.),('roof-weight',120000.),('width-weight',40000.),('width-mark',.888),('exit-curvature',1.8)]:p.add_argument('--'+k,type=float,default=v)
    p.add_argument('--cap',choices=('R219','R293'),default='R293');p.add_argument('--pair-kind',choices=('ball','chord'),default='ball');p.add_argument('--pair-weights',type=float,nargs='+',default=[12000.,65000.]);run(p.parse_args())
