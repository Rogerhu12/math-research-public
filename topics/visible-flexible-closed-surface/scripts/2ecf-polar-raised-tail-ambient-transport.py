#!/usr/bin/env python3
"""A full space diffeomorphism carrying the complete R205 disk to the new lifted disk."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
def read(p):return json.loads(Path(p).read_text())
def write(p,x):
    with Path(p).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
GL,GW=np.polynomial.legendre.leggauss(32)
GL=(1+GL)*.5;GW*=.5
A0=.8746432018013935
def profile(x):
    return x**5*(126+x*(-420+x*(540+x*(-315+70*x))))
def curve(y,c,A):
    sh=y.shape;y=y.reshape(-1);ab=abs(y);sg=np.sign(y);w=.8-c
    ell=np.clip(ab-c,0,w);x=ell/w;angle=A*profile(x);sn=np.sin(angle);cs=np.cos(angle)
    C=np.minimum(ab,c)+np.maximum(0,ab-.8)*np.cos(A)
    H=np.maximum(0,ab-.8)*np.sin(A)
    inds=np.flatnonzero(ell>0)
    for start in range(0,len(inds),2048):
        ii=inds[start:start+2048];v=A*profile(x[ii,None]*GL[None,:])
        C[ii]+=ell[ii]*(np.cos(v)@GW);H[ii]+=ell[ii]*(np.sin(v)@GW)
    k=A/w*630*x**4*(1-x)**4
    return tuple(q.reshape(sh) for q in (C*sg,H,cs,sn*sg,-sn*k*sg,cs*k))
def compose_scalar(v,v0,v1,v2):
    o=np.empty_like(v);o[:,0]=v0
    for j in (1,2):o[:,j]=v1*v[:,j]
    for i,j,k in ((3,1,1),(4,1,2),(5,2,2)):o[:,i]=v1*v[:,i]+v2*v[:,j]*v[:,k]
    return o
def product(x,y):
    o=x*y[:,0,None]+y*x[:,0,None];o[:,0]=x[:,0]*y[:,0]
    for i,j,k in ((3,1,1),(4,1,2),(5,2,2)):o[:,i]+=x[:,j]*y[:,k]+x[:,k]*y[:,j]
    return o
def neutral(j,start,stop):
    xy=j[:,:,:,1];z=j[:,:,:,2];Y=xy[:,0];yy=np.linspace(-2,2,4097)
    vals=curve(yy,.34,A0)[0];xi=np.interp(Y,vals,yy)
    for i in range(3):
        co=curve(xi,.34,A0);xi-=(co[0]-Y)/co[2]
    co=curve(xi,.34,A0);error=float(np.max(abs(co[0]-Y)))
    if error>4.e-14:raise ArithmeticError("Inverse R205 neutral-line coordinate missed its target")
    xijet=compose_scalar(xy,xi,1/co[2],-co[4]/co[2]**3)
    h=compose_scalar(xijet,co[1],co[3],co[5]);t=z+h
    l=stop-start;x=np.clip((t[:,0]-start)/l,0,1)
    e=compose_scalar(t,x**3*(10+x*(-15+6*x)),30*x*x*(1-x)**2/l,60*x*(1-x)*(1-2*x)/l**2)
    return xijet,h,e,error
def push(j,data,A,c):
    xijet,h,e,_=data;new=curve(xijet[:,0],c,A)
    dy=compose_scalar(xijet,new[0],new[2],new[4])-j[:,:,:,1]
    dz=compose_scalar(xijet,new[1],new[3],new[5])+h
    dz[:,0]-=.095
    out=j.copy();out[:,:,:,1]+=product(e,dy);out[:,:,:,2]+=product(e,dz)
    return out

def run(a):
    here=Path(__file__).resolve().parent
    scan=load(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','ambient_pointscan')
    raised=load(here/'2ecf-polar-raised-tail-tall-throat-source.py','ambient_raised')
    prepare=load(here/'2ecf-polar-new-central-gap-compose.py','ambient_gap')
    saved,de,full,caches,mods,*_=prepare.validate_prepared(a)
    basis=load(here/'2ecf-polar-fixed-prefix-position-basis.py','ambient_basis').restrict(full)[0]
    warm=load(a.scripts/'6a65-geometry-cauchy-unit-t-warm.py','ambient_R205')
    area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','ambient_area')
    direct=load(here/'2ecf-polar-c2-independent-g11-resume-observe.py','ambient_direct')
    donor=read(a.donor);ind=read(a.independent);stream=mods['stream']
    assert donor['preparedSHA256']==sha(a.prepared) and donor['modelDefinition']['basis']==basis.definition and ind['sourceIdentity']==de['sourceIdentity']
    cfg=raised.tall_config(stream.point.PointConfig)(**dict(de['pointConfig'],true_cuff_height=.415,height_maximum=.113))
    z=np.array(donor['z']).reshape(basis.nb,basis.na)
    if a.mode=='select':
        groups={k:(v.nodes,v.u,v.jets,v.radius,saved['caches'][k]['weights']) for k,v in caches.items()}
        params=[(A,c) for A in (.2,.4,.65,.85) for c in (.52,.56)]
    else:
        sel=read(a.selection);assert sel['entrySHA256']==sha(__file__) and sel['donorSHA256']==sha(a.donor)
        assert all(sha(v)==ind['SHA256'][k] for k,v in ind['files'].items())
        groups={'independent':(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),np.load(ind['files']['radius'],mmap_mode='r'),None)}
        params=[tuple(sel['selected']['params'])]
    out=dict(source='gap092-real-ambient-push-to-inverted-developed-tail',entrySHA256=sha(__file__),preparedSHA256=sha(a.prepared),
        independentSHA256=sha(a.independent),donorSHA256=sha(a.donor),results={},ownAccepts=0,finiteOnly=True,lowerUpperNeutralHeight=[.21,.50])
    for group,(ns,u,src,rad,w) in groups.items():
        parent=src+(direct.direct_packet(basis,ns,z,u) if group=='independent' else basis.packet(basis.matrices(ns),z,len(u)))
        data=neutral(parent,.21,.50);rows=[]
        for A,c in params:
            j=push(parent,data,A,c);v=scan.evaluate(stream,stream.point,area,j,rad,ns,u,cfg,w)
            left=np.flatnonzero(ns<=basis.c);right=np.flatnonzero(ns>=basis.end);v['unchangedPrefixSixJets']=bool(np.array_equal(j[left],parent[left]))
            assert v['unchangedPrefixSixJets']
            err=np.zeros(6)
            for i in right:
                q=raised.raised_port(warm,A,c,u,.8 if ns[i]==basis.end else float(rad[i,0]))
                p=np.stack([q[k] for k in ('P','V','Pu','A','Vu','Puu')]);err=np.maximum(err,abs(j[i]-p).max(axis=(1,2)))
            v['fullAnalyticTailSixJetErrors']=err.tolist();v['inverseResidual']=data[3];v['params']=[A,c]
            if np.max(err)>1e-9:raise ArithmeticError("New exact developed tail and complete push disagree")
            rows.append(v);print(group,A,c,v['metric'],v['curvature'],v['held'],v['R2'],flush=True)
        out['results'][group]=rows
    if a.mode=='select':
        result=[]
        for p,q in zip(out['results']['training'],out['results']['observer']):
            assert p['actualRows']+q['actualRows']==4291840
            result.append(dict(params=p['params'],metric=max(p['metric'],q['metric']),curvature=max(p['curvature'],q['curvature']),
                held=min(p['held'],q['held']),R2=p['R2']+q['R2']))
        out['fullG10']=result;out['selected']=min(result,key=lambda r:r['R2'])
    write(a.output,out)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('prepared','scripts','donor','independent','selection','output'):p.add_argument('--'+k,type=Path)
    p.add_argument('--mode',choices=['select','observe'],required=True);run(p.parse_args())
