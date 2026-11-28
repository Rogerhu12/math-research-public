#!/usr/bin/env python3
"""Release the old r=.8 developed cut as an internal position; retain an open true flat annulus above the actual fixed cap."""
import argparse
import importlib.util
from fractions import Fraction as Q
from pathlib import Path
import sys
import os
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np
from scipy.optimize import minimize
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
radius=module(here/'2ecf-polar-material-implicit-coupled-radius.py','released_cut_radius')
impl=radius.impl;base=radius.base
src=module(here/'2ecf-polar-material-curve-coupled-spherical-design.py','released_cut_original_material')
def flat_port(u,r):
    C,S=np.cos(u),np.sin(u);Z=np.zeros_like(C);E=np.stack([C,S,Z],axis=-1);F=np.stack([-S,C,Z],axis=-1);O=np.zeros_like(E)
    P=r*E;P[:,2]=.415
    return dict(P=P,Pu=r*F,Puu=-r*E,Puuu=-r*F,Puuuu=r*E,V=-E,Vu=-F,Vuu=E,Vuuu=F,A=O,Au=O,Auu=O)
def extended_ports(ends,amp,flat,u):
    return ends.base.higher_coast_port(ends.master,.02,u),flat_port(u,ends.flat_radius)
base.ports=extended_ports
class Reference:
    def __init__(self,old,ends,amp,flat,T):
        self.old=old;self.ends=ends;self.amp=amp;self.flat=flat;self.S=old.knots[-1]
        self.knots=np.array([old.knots[0],T])
    def position(self,ns,u):
        result=np.empty((len(ns),6,len(u),3));inner=ns<=self.S
        if np.any(inner):result[inner]=self.old.position(ns[inner],u)
        for i in np.flatnonzero(~inner):
            p=self.ends.raised.raised_port(self.ends.warm,self.amp,self.flat,u,float(Q(4,5)+Q.from_float(float(self.S))-Q.from_float(float(ns[i]))))
            result[i]=np.stack([p[k] for k in ('P','V','Pu','A','Vu','Puu')])
        return result
def setup(a):
    seed=base.read(a.seed_design);donor=base.read(a.donor);g=base.read(a.frozen)
    assert donor['fieldSHA256']==base.sha(a.donor_field) and donor['targetSHA256']==g['targetSHA256']
    assert donor['seedDesignSHA256']==base.sha(a.seed_design)
    en=src.end_module(here,seed);a.amp=seed['amp'];a.flat=seed['flat']
    ends=en.Ends(a.scripts,a.ramp,a.coast,a.amp,a.flat,2048)
    orig=src.MaterialField(a.donor_field,ends)
    b,S=orig.knots[[0,-1]];T=float(Q.from_float(float(S))+Q(2,5))
    rf=Q(4,5)+Q.from_float(float(S))-Q.from_float(T);ends.flat_radius=float(rf)
    ref=Reference(orig,ends,a.amp,a.flat,T)
    return ends,ref,b,S,T,rf,g
def apply_target(ns,rad,b,S,g):
    alpha=np.array(g['logRadiusCoefficients'])
    return rad*np.exp(radius.radius_basis((ns-b)/(S-b),g['radiusSpans'])@alpha)
def design(a):
    ends,ref,b,S,T,rf,g=setup(a)
    q=base.read(a.prepared);c=q['caches']['training'];f=Path(c['files']['radius']);assert base.sha(f)==c['SHA256']['radius']
    model=impl.Implicit(a,ends,ref,a.radials,a.angles);a.start=None
    ind=np.argsort(c['nodes']);ns=np.asarray(c['nodes'])[ind]
    fr=np.interp(model.ns,ns,np.load(f)[:,0][ind]);kk=model.ns>=S
    fr[kk]=.8+S-model.ns[kk]
    model.rad=apply_target(model.ns,fr,b,S,g)[:,None]
    stream=module(a.scripts/'6a65-cartesian-complete-stream.py','released_cut_point')
    model.point=stream.point;model.area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','released_cut_area')
    model.cfg=ends.raised.tall_config(stream.point.PointConfig)(**dict(q['definition']['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    w=np.ones((a.radials,1));w[[0,-1]]=.5;w/=np.sum(w)*a.angles
    model.weights=dict(metric=w,curvature=a.curvature*w,geometry=a.geometry*w)
    x=model.starting();v,grad=model.value(x);rng=np.random.default_rng(20765);d=rng.normal(size=len(x));d/=np.linalg.norm(d)
    h=1e-6;fd=(model.value(x+h*d,False)['designTotal']-model.value(x-h*d,False)['designTotal'])/(2*h)
    check=abs(fd-grad@d)/max(1.,abs(fd),abs(grad@d))
    if check>3e-4:raise ArithmeticError(('Released source derivative mismatch',fd,grad@d))
    start=model.value(x,False);hist=[]
    def cb(z):
        val=model.value(z,False);hist.append(val)
        if len(hist)%10==0:print(len(hist),val,flush=True)
    opt=minimize(model.value,x,jac=True,method='L-BFGS-B',callback=cb,options=dict(maxiter=a.iterations,ftol=1e-14,gtol=1e-8,maxcor=18,maxls=36))
    fine=impl.Implicit(a,ends,ref,a.fine_radials,a.fine_angles)
    P,V,A,unused,_=fine.field(opt.x);stride=(len(fine.ns)-1)//a.cells
    assert stride*a.cells==len(fine.ns)-1 and a.stored_modes<a.fine_angles//2
    data=np.stack([P[::stride],V[::stride],A[::stride]],axis=1)
    co=np.fft.rfft(data,axis=2)[:,:,:a.stored_modes+1]/a.fine_angles;co[:,:,1:]*=2
    with a.field.open('xb') as f:np.savez_compressed(f,coeff=co,knots=fine.ns[::stride],amp=a.amp,flat=a.flat)
    base.stores(a.output,dict(schema='released-old-developed-cut-b-to-true-open-inner-flat-annulus-material-flow-v1',entrySHA256=base.sha(__file__),seedDesignSHA256=base.sha(a.seed_design),targetSHA256=g['targetSHA256'],donorSHA256=base.sha(a.donor),frozenSHA256=base.sha(a.frozen),donorFieldSHA256=base.sha(a.donor_field),fieldSHA256=base.sha(a.field),rampSHA256=base.sha(a.ramp),coastSHA256=base.sha(a.coast),preparedSHA256=base.sha(a.prepared),amp=a.amp,flat=a.flat,b=b,oldS=S,newT=T,trueNewRadius=str(rf),controls=len(x),positionCoefficients=opt.x.tolist(),spans=a.spans,modes=a.modes,radiusSpans=g['radiusSpans'],logRadiusCoefficients=g['logRadiusCoefficients'],actualOwn=opt.nit,history=hist,starting=start,final=model.value(opt.x,False),denseImplicit=fine.last,gradientError=float(check),fixedOriginalDesignedMetric=True,oldPortConstraintReleased=True))
def observe(a):
    ends,ref,b,S,T,rf,g=setup(a);state=base.read(a.design)
    assert state['fieldSHA256']==base.sha(a.field) and state['trueNewRadius']==str(rf) and state['entrySHA256']==base.sha(__file__)
    op=module(here/'2ecf-polar-new-central-gap-compose.py','ext_physical_core')
    raw,de,full,caches,mods,*_=op.validate_prepared(a)
    ind=base.read(a.independent);stream=mods['stream']
    cfg=ends.raised.tall_config(stream.point.PointConfig)(**dict(de['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','ext_obs_area')
    scan=module(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','ext_obs_scan')
    model=base.MaterialField(a.field,ends)
    groups={k:(c.nodes,c.u,c.jets,c.radius,raw['caches'][k]['weights']) for k,c in caches.items()}
    groups['independent']=(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),np.load(ind['files']['radius'],mmap_mode='r'),None)
    ex=S+(T-S)*(np.arange(193)+.371)/193
    ue=2*np.pi*(np.arange(272)+.417)/272
    groups['newTailInterior193x272']=(ex,ue,None,(.8+S-ex)[:,None],None)
    obs={}
    for key,(ns,u,jj,r,w) in groups.items():
        js=np.empty((len(ns),6,len(u),3)) if jj is None else jj.copy()
        ids=np.flatnonzero((ns>=b)&(ns<=T))
        for k in range(0,len(ids),12):
            ii=ids[k:k+12];js[ii]=model.position(ns[ii],u)
        for i in np.flatnonzero(ns>T):js[i]=np.stack([flat_port(u,r[i,0])[k] for k in ('P','V','Pu','A','Vu','Puu')])
        rr=r.copy();rr[:,0]=apply_target(ns,r[:,0],b,S,g)
        v=scan.evaluate(stream,stream.point,area,js,rr,ns,u,cfg,w)
        obs[key]=v;print(key,v['metric'],v['curvature'],v['held'],v['R2'],flush=True)
    eval_u=groups['independent'][1]
    old=ref.position(np.array([S]),eval_u)
    new=model.position(np.array([S]),eval_u)
    ends_obs=model.position(np.array([b,T]),eval_u);ports=extended_ports(ends,a.amp,a.flat,eval_u)
    ep=np.stack([np.stack([p[k] for k in ('P','V','Pu','A','Vu','Puu')]) for p in ports])
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),designSHA256=base.sha(a.design),fieldSHA256=base.sha(a.field),targetSHA256=g['targetSHA256'],observations=obs,oldCutSixJetActualMaxChange=np.max(np.abs(new-old),axis=(0,2,3)).tolist(),trueEndpointErrors=np.max(np.abs(ends_obs-ep),axis=(2,3)).tolist(),completeRows=obs['training']['actualRows']+obs['observer']['actualRows']))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('design','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','seed-design','donor','donor-field','frozen','design','field','output','independent'):p.add_argument('--'+k,type=Path)
    for k,v in [('angles',112),('radials',145),('spans',28),('modes',12),('iterations',300),('fine-radials',769),('fine-angles',320),('cells',96),('stored-modes',100)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',2.),('geometry',100.)]:p.add_argument('--'+k,type=float,default=v)
    a=p.parse_args();(design if a.mode=='design' else observe)(a)
