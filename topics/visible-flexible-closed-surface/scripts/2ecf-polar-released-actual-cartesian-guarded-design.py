#!/usr/bin/env python3
"""Full six-jet additive Cartesian position solve after release of the old developed cut."""
import argparse
import importlib.util
import os
import sys
from pathlib import Path
for k in ('MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'): os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import minimize

def module(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
lift=module(here/'2ecf-polar-released-low-mode-held-and-curvature.py','released_additive_source')
ext=lift.ext;base=ext.base
class Basis:
    orders=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
    def __init__(self,ns,u,b,T,spans,modes):
        self.ns=np.asarray(ns);self.u=np.asarray(u);t=(self.ns-b)/(T-b)
        k=np.r_[np.zeros(6),np.arange(1,spans)/spans,np.ones(6)]
        spl=BSpline(k,np.eye(len(k)-6),5)
        self.B=[spl(np.clip(t,0,1),nu=d)[:,3:-3]*((t>0)&(t<1))[:,None]/(T-b)**d for d in range(3)]
        self.F=[]
        for i in range(3):
            freq=2*np.arange(modes+1)+(i<2)
            phase=(i==1)*(-np.pi/2)
            self.F.append([np.cos(np.outer(u,freq)+phase+d*np.pi/2)*freq**d for d in range(3)])
        self.shape=(3,self.B[0].shape[1],modes+1)
    def apply(self,x):
        x=x.reshape(self.shape);result=np.empty((len(self.ns),6,len(self.u),3))
        for k,(ds,du) in enumerate(self.orders):
            for c in range(3):result[:,k,:,c]=(self.B[ds]@x[c])@self.F[c][du].T
        return result
    def transpose(self,g):
        out=np.zeros(self.shape)
        for k,(ds,du) in enumerate(self.orders):
            for c in range(3):out[c]+=self.B[ds].T@(g[:,k,:,c]@self.F[c][du])
        return out.ravel()
def run(a):
    ends,ref,b,S,T,rf,g=ext.setup(a);state=base.read(a.state)
    assert state['fieldSHA256']==base.sha(a.field) and state['targetSHA256']==g['targetSHA256'] and state['newT']==T
    if a.mode=='observe':
        q=base.read(a.solution)
        assert q['entrySHA256']==base.sha(__file__) and q['sourceFieldSHA256']==base.sha(a.field)
        x=np.array(q['coefficients']);groups,evaluate,*_=lift.load_groups(a,('training','observer','independent','tail193x272'));results={}
        for key,(ns,u,j,r,w) in groups.items():
            basis=Basis(ns,u,b,T,q['spans'],q['modes']);results[key]=evaluate(ns,u,j+basis.apply(x),r,w)
            v=results[key];print(key,v['metric'],v['curvature'],v['held'],v['R2'],flush=True)
        base.stores(a.output,dict(solutionSHA256=base.sha(a.solution),entrySHA256=base.sha(__file__),sourceFieldSHA256=base.sha(a.field),targetSHA256=state['targetSHA256'],observations=results))
        return
    ns=np.linspace(b,T,a.radials);u=2*np.pi*np.arange(a.angles)/a.angles;basis=Basis(ns,u,b,T,a.spans,a.modes)
    field=base.MaterialField(a.field,ends);j=np.concatenate([field.position(ns[p:p+12],u) for p in range(0,len(ns),12)])
    pre=base.read(a.prepared);c=pre['caches']['training'];rfile=Path(c['files']['radius']);assert base.sha(rfile)==c['SHA256']['radius']
    order=np.argsort(c['nodes']);f=np.interp(ns,np.array(c['nodes'])[order],np.load(rfile)[:,0][order])
    f[ns>=S]=.8+S-ns[ns>=S];f=ext.apply_target(ns,f,b,S,g)[:,None]
    point=module(a.scripts/'6a65-cartesian-complete-stream.py','released_additive_14_rows').point
    area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','released_additive_area')
    cfg=ends.raised.tall_config(point.PointConfig)(**dict(pre['definition']['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    w=np.ones((len(ns),1));w[[0,-1]]=.5;w/=sum(w)*len(u)
    weights=dict(metric=w,curvature=w*a.curvature,geometry=w*a.geometry)
    centers=[np.array([0.,sign*ends.master.A,0.]) for sign in (-1,1)]
    def value(x,gradient=True):
        jet=j+basis.apply(x);pt=point.PointLinearized(jet.swapaxes(1,2),f,cfg,weights);ar=area.AreaPacket(jet,f,w,.5)
        loss=float(np.sum(pt.residual**2)+np.sum(ar.residual**2))
        errors=[]
        for center in centers:
            d=jet[:,0]-center;length=np.linalg.norm(d,axis=-1);gap=np.maximum(a.held-length,0.)
            loss+=a.guard*np.sum(w*gap**2);errors.append((d,length,gap))
        if not gradient:return dict(loss=float(loss),metric=float(np.max(np.abs(pt.metric/np.array([1.,np.sqrt(2.),1.])))),kappa=float(np.max(np.abs(pt.curvature['eigenvalues']))),held=float(min(np.min(v[1]) for v in errors)))
        grad=2*pt.vjp(pt.residual).swapaxes(1,2);ds,du=ar.vjp(2*ar.residual);grad[:,1]+=ds;grad[:,2]+=du
        for d,length,gap in errors:grad[:,0]-=(2*a.guard*w*gap/length)[...,None]*d
        return loss,basis.transpose(grad)
    x=np.zeros(np.prod(basis.shape))
    if a.start:
        prev=base.read(a.start);assert prev['sourceFieldSHA256']==base.sha(a.field)
        assert (prev['spans'],prev['modes'])==(a.spans,a.modes)
        x=np.array(prev['coefficients'])
    v,dv=value(x);dr=np.random.default_rng(61148).normal(size=len(x));dr/=np.linalg.norm(dr);eps=1e-7
    dif=(value(x+eps*dr,False)['loss']-value(x-eps*dr,False)['loss'])/(2*eps)
    err=abs(dif-dr@dv)/max(1,abs(dif),abs(dr@dv));assert err<4e-5,(dif,dr@dv)
    history=[];start=value(x,False)
    def callback(z):
        history.append(value(z,False))
        if len(history)%50==0:print(len(history),history[-1],flush=True)
    opt=minimize(value,x,jac=True,method='L-BFGS-B',callback=callback,options=dict(maxiter=a.iterations,maxcor=26,gtol=3e-8,ftol=1e-15,maxls=40))
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),sourceStateSHA256=base.sha(a.state),sourceFieldSHA256=base.sha(a.field),targetSHA256=state['targetSHA256'],warmSolutionSHA256=base.sha(a.start) if a.start else None,spans=a.spans,modes=a.modes,controls=len(x),coefficients=opt.x.tolist(),ownActual=opt.nit,gradientError=err,starting=start,final=value(opt.x,False),history=history,physicalInterval=[b,T],heldGuide=a.held,guardWeight=a.guard,curvatureWeight=a.curvature,geometryWeight=a.geometry,angularGrid=a.angles,radialGrid=a.radials))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','solution','start','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('radials',101),('angles',72),('spans',13),('modes',5),('iterations',650)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',3.),('geometry',40.),('guard',4000.),('held',.6535)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
