#!/usr/bin/env python3
"""Explicit small physical Cartesian corrections on the newly released annulus; exact two-jet clamp."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from numpy.polynomial import Polynomial
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
here=Path(__file__).parent;ext=module(here/'2ecf-polar-released-developed-cut-to-actual-flat-collar.py','physical_lift_extended');base=ext.base
def basis(ns,u,b,T,m,n,p,tilt):
    t=(ns-b)/(T-b);active=(ns>b)&(ns<T)
    mx=m/(m+n)
    poly=Polynomial([0,1])**m*Polynomial([1,-1])**n/(mx**m*(1-mx)**n)
    W=np.stack([np.where(active,poly.deriv(j)(np.clip(t,0,1))/(T-b)**j,0.) for j in range(3)])
    sn,cs=np.sin(u),np.cos(u)
    def wave(k):return (sn**k,k*sn**(k-1)*cs,k*(k-1)*sn**(k-2)*cs**2-k*sn**k)
    wa,wb=wave(p),wave(p+1);o=np.zeros((len(ns),6,len(u),3))
    for k,(dr,du) in enumerate(((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))):
        o[:,k,:,1]=-W[dr,:,None]*wa[du];o[:,k,:,2]=tilt*W[dr,:,None]*wb[du]
    return o
def load_groups(a,inds):
    ends,ref,b,S,T,rf,g=ext.setup(a);q=base.read(a.prepared);d=base.read(a.state)
    assert d['targetSHA256']==g['targetSHA256'] and d['fieldSHA256']==base.sha(a.field) and d['newT']==T
    model=base.MaterialField(a.field,ends);raw=base.read(a.independent)
    groups={k:(np.asarray(r['nodes']),np.asarray(r['angles']),r['files']['jets'],r['files']['radius'],r['weights']) for k,r in q['caches'].items()}
    groups['independent']=(np.array(raw['physicalNodes']),np.array(raw['angles']),raw['files']['jets'],raw['files']['radius'],None)
    nsx=S+(T-S)*(np.arange(193)+.371)/193;groups['tail193x272']=(nsx,2*np.pi*(np.arange(272)+.417)/272,None,None,None)
    result={}
    for k in inds:
        ns,u,jp,rp,w=groups[k]
        js=np.empty((len(ns),6,len(u),3)) if jp is None else np.load(jp,mmap_mode='r').copy()
        rr=(.8+S-ns)[:,None] if rp is None else np.load(rp).copy()
        ids=np.flatnonzero((ns>=b)&(ns<=T))
        for i in range(0,len(ids),12):
            jj=ids[i:i+12];js[jj]=model.position(ns[jj],u)
        for i in np.flatnonzero(ns>T):
            pp=ext.flat_port(u,rr[i,0]);js[i]=np.stack([pp[n] for n in ('P','V','Pu','A','Vu','Puu')])
        rr[:,0]=ext.apply_target(ns,rr[:,0],b,S,g)
        result[k]=(ns,u,js,rr,w)
    stream=module(a.scripts/'6a65-cartesian-complete-stream.py','low_lift_rows');area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','low_lift_area')
    cfg=ends.raised.tall_config(stream.point.PointConfig)(**dict(q['definition']['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    scan=module(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','low_lift_scan')
    def evaluate(ns,u,j,rr,w):return scan.evaluate(stream,stream.point,area,j,rr,ns,u,cfg,w)
    return result,evaluate,b,T,ends.master.A
def needed(P,D,A,R):
    maxroot=0.
    for sign in (1,-1):
        diff=P-np.array([0.,sign*A,0.]);delta=R*R-np.sum(diff*diff,axis=-1);use=delta>0
        if not np.any(use):continue
        d=D[use];raw=diff[use];gap=delta[use];dd=np.sum(d*d,axis=-1);pd=np.sum(raw*d,axis=-1)
        if min(dd)<1e-16:return np.inf
        root=gap/(pd+np.sqrt(pd*pd+dd*gap))
        maxroot=max(maxroot,float(max(root)))
    return maxroot
def run(a):
    training=a.mode=='select';inds=('training','observer') if training else ('independent','tail193x272')
    groups,evaluate,b,T,A=load_groups(a,inds)
    if training:params=[(m,n,p,k) for m,n in ((3,4),(4,5)) for p in (3,5) for k in (.30,.55,.80)]
    else:
        q=base.read(a.selection);assert q['entrySHA256']==base.sha(__file__) and q['stateSHA256']==base.sha(a.state)
        params=[tuple(q['selected']['parameters'])]
    result=[]
    for par in params:
        if training:
            lam=0.
            for ns,u,j,rr,w in groups.values():
                d=basis(ns,u,b,T,*par)[:,0];lam=max(lam,needed(j[:,0],d,A,a.required))
            lam*=1+1e-8
        else:lam=q['selected']['lambdaValue']
        assert np.isfinite(lam) and lam<.5
        vals={}
        for key,(ns,u,j,rr,w) in groups.items():vals[key]=evaluate(ns,u,j+lam*basis(ns,u,b,T,*par),rr,w)
        rr=dict(parameters=list(par),lambdaValue=lam,groups=vals,metric=max(v['metric'] for v in vals.values()),curvature=max(v['curvature'] for v in vals.values()),held=min(v['held'] for v in vals.values()))
        if training:rr['R2']=sum(v['R2'] for v in vals.values())
        result.append(rr);print(par,lam,rr['metric'],rr['curvature'],rr['held'],flush=True)
    out=dict(entrySHA256=base.sha(__file__),stateSHA256=base.sha(a.state),preimageFieldSHA256=base.sha(a.field),requiredSampledHeld=a.required,mode=a.mode,rows=result,acceptedOptimizerSteps=0,fixedG=True,finiteOnly=True)
    if training:
        ok=[r for r in result if r['held']>=a.required and r['curvature']<1/.097]
        order=ok or [r for r in result if r['held']>=a.required]
        assert order;out.update(selected=min(order,key=lambda r:r['R2']),eligibleBelowCurvatureLimit=len(ok),selectionRule='full G10 held threshold, then kappa below 1/.097 if available, then smallest full fourteen-row objective')
    base.stores(a.output,out)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('select','observe'),required=True)
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','selection','output'):p.add_argument('--'+k,type=Path)
    p.add_argument('--required',type=float,default=.6508);run(p.parse_args())
