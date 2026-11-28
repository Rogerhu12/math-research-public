#!/usr/bin/env python3
"""True inverted cylindrical bending beyond an enlarged flat strip and a fixed tall-throat cap."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np

def load(p,n):
    spec=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(spec);sys.modules[n]=m;spec.loader.exec_module(m)
    return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def write(p,x):
    with Path(p).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def tall_config(original):
    class TallThroatConfig(original):
        def __post_init__(self):
            # Audit all inherited parameters against the original validator and its original allowance.
            old={k:getattr(self,k) for k in self.__dataclass_fields__}
            old['height_maximum']=.0195
            original(**old)
            if self.true_cuff_height!=.415 or self.height_maximum!=.113:raise ValueError('True .415/.115 throat window required')
    return TallThroatConfig
def raised_port(warm,A,c,u,r):
    if not (0<=A<=.85 and .52<=c<=.56):raise ValueError("Certified raised-tail rectangle required")
    ports=warm.ports
    U=ports.constant(u,len(u));U[1]=1
    su,cu=ports.sincos(U);y=r*su
    sign=np.where(y[0]<0,-1.,1.);ay=sign*y[0];active=ay>c
    width=.8-c
    t=(y*sign[None,:]-ports.constant(c,len(u)))/width;t[:,~active]=0
    # Positive angle gives upward bending, with z=Z+H.
    alpha=A*(126*ports.power(t,5)-420*ports.power(t,6)+540*ports.power(t,7)-315*ports.power(t,8)+70*ports.power(t,9))
    sn,cs=ports.sincos(alpha)
    aj=A/width*630*ports.mul(ports.power(t,4),ports.power(ports.constant(1,len(u))-t,4))*sign
    cp=cs;hp=sn*sign;cpp=-ports.mul(sn,aj);hpp=ports.mul(cs,aj)*sign
    gx,gw=np.polynomial.legendre.leggauss(48);gx=(gx+1)/2;gw=gw/2
    length=np.maximum(0,ay-c);x=length[:,None]*gx/width
    ag=A*x**5*(126+x*(-420+x*(540+x*(-315+70*x))))
    C=sign*(np.minimum(ay,c)+length*(np.cos(ag)@gw));H=length*(np.sin(ag)@gw)
    p=np.stack((r*cu[0],C,.415+H),axis=-1)
    pu=np.stack((-r*su[0],cp[0]*r*cu[0],hp[0]*r*cu[0]),axis=-1)
    puu=np.stack((-r*cu[0],cpp[0]*(r*cu[0])**2-cp[0]*r*su[0],hpp[0]*(r*cu[0])**2-hp[0]*r*su[0]),axis=-1)
    v=np.stack((-cu,-ports.mul(cp,su),-ports.mul(hp,su)),axis=-1)
    k=np.stack((np.zeros_like(cu),ports.mul(cpp,ports.mul(su,su)),ports.mul(hpp,ports.mul(su,su))),axis=-1)
    return dict(P=p,Pu=pu,Puu=puu,V=v[0],Vu=v[1],Vuu=2*v[2],A=k[0],Au=k[1],Auu=2*k[2])
def delta(warm,ns,u,rad,b,S,A,c,fraction):
    start=b+(1-fraction)*(S-b);L=S-start
    old=lambda r:warm.developed_tail_port(.8746432018013935,.51,u,r)
    new=lambda r:raised_port(warm,A,c,u,r)
    q1,q2=old(.8),new(.8)
    block=np.stack([[q2[k]-q1[k] for k in row] for row in (('P','V','A'),('Pu','Vu','Au'),('Puu','Vuu','Auu'))])
    out=np.zeros((len(ns),6,len(u),3))
    ii=np.flatnonzero((ns>start)&(ns<S));t=(ns[ii]-start)/L
    if len(ii):
        mats=[np.array([warm.ports.hermite_weights(x,L,j)[3:] for x in t]) for j in range(3)]
        out[ii]=np.stack([(mats[j]@block[i].reshape(3,-1)).reshape(len(ii),len(u),3)
            for i,j in ((0,0),(0,1),(1,0),(0,2),(1,1),(2,0))],axis=1)
    for i in np.flatnonzero(ns>=S):
        r=.8 if ns[i]==S else float(rad[i,0]);left,right=old(r),new(r)
        out[i]=np.stack([right[k]-left[k] for k in ('P','V','Pu','A','Vu','Puu')])
    return out
def run(a):
    here=Path(__file__).resolve().parent
    pointscan=load(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','inverted_pointscan')
    prepare=load(here/'2ecf-polar-new-central-gap-compose.py','inverted_gap092')
    saved,de,full,caches,mods,*_=prepare.validate_prepared(a)
    basis=load(here/'2ecf-polar-fixed-prefix-position-basis.py','inverted_basis').restrict(full)[0]
    warm=load(a.scripts/'6a65-geometry-cauchy-unit-t-warm.py','inverted_R205')
    area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','inverted_area')
    dr=load(here/'2ecf-polar-c2-independent-g11-resume-observe.py','inverted_direct')
    donor=read(a.donor);obs=read(a.independent);stream=mods['stream']
    assert donor['preparedSHA256']==sha(a.prepared) and donor['modelDefinition']['basis']==basis.definition and obs['sourceIdentity']==de['sourceIdentity']
    z=np.array(donor['z']).reshape(basis.nb,basis.na)
    if a.mode=='select':
        groups={k:(v.nodes,v.u,v.jets,v.radius,saved['caches'][k]['weights']) for k,v in caches.items()}
        params=[(A,c,l) for A in (0.,.4,.65,.85) for c in (.52,.56) for l in (.60,1.) if A or c==.52]
    else:
        rec=read(a.selection);assert rec['entrySHA256']==sha(__file__) and rec['donorSHA256']==sha(a.donor)
        assert all(sha(v)==obs['SHA256'][k] for k,v in obs['files'].items())
        groups={'independent':(np.array(obs['physicalNodes']),np.array(obs['angles']),
            np.load(obs['files']['jets'],mmap_mode='r'),np.load(obs['files']['radius'],mmap_mode='r'),None)}
        params=[tuple(rec['selected']['params'])]
    cfg=tall_config(stream.point.PointConfig)(**dict(de['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    out=dict(source='gap092-new-inverted-developed-tail-.415-cuff-.115-true-throat',entrySHA256=sha(__file__),
        preparedSHA256=sha(a.prepared),donorSHA256=sha(a.donor),independentSHA256=sha(a.independent),results={},ownAccepts=0,finiteOnly=True)
    for group,(ns,u,src,rad,weights) in groups.items():
        parent=src+(dr.direct_packet(basis,ns,z,u) if group=='independent' else basis.packet(basis.matrices(ns),z,len(u)))
        rows=[]
        for pars in params:
            q=pointscan.evaluate(stream,stream.point,area,parent+delta(warm,ns,u,rad,basis.c,basis.end,*pars),rad,ns,u,cfg,weights)
            q['params']=list(pars);rows.append(q)
            print(group,pars,q['metric'],q['curvature'],q['held'],q['R2'],flush=True)
        out['results'][group]=rows
    if a.mode=='select':
        rows=[]
        for q,v in zip(out['results']['training'],out['results']['observer']):
            assert q['params']==v['params'] and q['actualRows']+v['actualRows']==4291840
            rows.append(dict(params=q['params'],R2=q['R2']+v['R2'],metric=max(q['metric'],v['metric']),
                curvature=max(q['curvature'],v['curvature']),held=min(q['held'],v['held'])))
        curved=[r for r in rows if r['params'][0]>0]
        # Lock the new physical upward bending mechanism and use the full objective for its starting point.
        out['selected']=min(curved,key=lambda r:r['R2']);out['fullG10']=rows
    write(a.output,out)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('prepared','scripts','donor','independent','selection','output'):p.add_argument('--'+k,type=Path)
    p.add_argument('--mode',choices=['select','observe'],required=True);run(p.parse_args())
