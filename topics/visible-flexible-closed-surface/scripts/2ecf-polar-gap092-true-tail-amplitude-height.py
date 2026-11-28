#!/usr/bin/env python3
"""Evaluate actual full R205 tail bending and rigid cap heights on the gap-.92 physical constellation."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np

def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for c in iter(lambda:f.read(1<<20),b''):h.update(c)
    return h.hexdigest()

def load(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m

def r205_delta(warm,ns,u,rad,b,S,amp,Z):
    originalA=.8746432018013935;originalZ=.51;L=S-b
    n=len(u);d=np.zeros((len(ns),6,n,3))
    if amp==originalA and Z==originalZ:return d
    old=warm.developed_tail_port(originalA,originalZ,u,.8);new=warm.developed_tail_port(amp,Z,u,.8)
    delta=np.stack([[new[k]-old[k] for k in block] for block in (('P','V','A'),('Pu','Vu','Au'),('Puu','Vuu','Auu'))])
    ir=np.flatnonzero((ns>b)&(ns<S));t=(ns[ir]-b)/L
    M=[np.array([warm.ports.hermite_weights(x,L,j)[3:] for x in t]) for j in range(3)]
    if len(ir):
        d[ir]=np.stack([(M[j]@delta[i].reshape(3,-1)).reshape(len(ir),n,3) for i,j in ((0,0),(0,1),(1,0),(0,2),(1,1),(2,0))],axis=1)
    for i in np.flatnonzero(ns>=S):
        radius=.8 if ns[i]==S else float(rad[i,0])
        q1=warm.developed_tail_port(originalA,originalZ,u,radius);q2=warm.developed_tail_port(amp,Z,u,radius)
        d[i]=np.stack([q2[k]-q1[k] for k in ('P','V','Pu','A','Vu','Puu')])
    return d

def evaluate(stats,point,area,packet,rad,ns,u,config,weights):
    N=len(u);tot=None;ar2=0.;sigma=1e5
    for k in range(0,len(ns),16):
        rr=ns[k:k+16];v=packet[k:k+len(rr)];f=rad[k:k+len(rr),0,None]
        W={n:np.ones((len(rr),1))/N if weights is None else .5*np.asarray(weights[n][k:k+len(rr)])[:,None]/N for n in ('metric','curvature','geometry')}
        po=point.PointLinearized(v.swapaxes(1,2),np.broadcast_to(f,(len(rr),N)),config,W)
        sub=stats._block_statistics(po,rr,N);sub['worstMetric']['u']+=float(u[0]);sub['worstCurvature']['u']+=float(u[0])
        tot=stats._merge_statistics(tot,sub);aa=area.AreaPacket(v,f,W['metric'],.5)
        ar2+=aa.stats['squaredNorm'];sigma=min(sigma,float(aa.stats['minAreaRatio']))
    return dict(R2=tot['squaredNorm']+ar2 if weights is not None else None,metric=tot['maxRelativeMetric'],curvature=tot['maxCurvature'],
        held=tot['minHeldDistance'],minAreaRatio=sigma,geometryViolations=tot['geometryMaximumViolations'],
        worstMetric=tot['worstMetric'],worstCurvature=tot['worstCurvature'],actualRows=14*len(ns)*N)

def run(a):
    started=time.monotonic();here=Path(__file__).resolve().parent
    prepare=load(here/'2ecf-polar-new-central-gap-compose.py','tail_gap_source')
    saved,de,full,caches,mods,*_=prepare.validate_prepared(a);stream=mods['stream']
    basis=load(here/'2ecf-polar-fixed-prefix-position-basis.py','tail_gap092_basis').restrict(full)[0]
    warm=load(a.scripts/'6a65-geometry-cauchy-unit-t-warm.py','tail_absolute_R205')
    area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','tail_q2')
    direct=load(here/'2ecf-polar-c2-independent-g11-resume-observe.py','tail_g11')
    st=json.loads(a.state.read_text());ind=json.loads(a.observer.read_text())
    if (st['preparedSHA256']!=sha(a.prepared) or st['modelDefinition']['basis']!=basis.definition or ind['sourceIdentity']!=de['sourceIdentity']):
        raise ValueError("True gap-.92 parent and observer required")
    z=np.asarray(st['z']).reshape(basis.nb,basis.na)
    if a.mode=='select':groups={k:(v.nodes,v.u,v.jets,v.radius,saved['caches'][k]['weights']) for k,v in caches.items()}
    else:groups={'independent':(np.array(ind['physicalNodes']),np.array(ind['angles']),np.load(ind['files']['jets'],mmap_mode='r'),np.load(ind['files']['radius'],mmap_mode='r'),None)}
    inputs=[(float(A),float(Z)) for A in a.amplitudes for Z in a.heights]
    orig=(.8746432018013935,.51)
    if a.mode=='observe':
        selection=json.loads(a.selection.read_text())
        if selection['parentStateSHA256']!=sha(a.state) or selection['entrySHA256']!=sha(__file__):raise ValueError("Actual selection identity changed")
        inputs=[orig,tuple(selection['G10Selection']['parameters'])]
    if any(not (0<=A<=1.2 and .41<=Z<=.52) for A,Z in inputs):raise ValueError("R205/R219 bounds required")
    data={}
    for key,(ns,u,src,rad,w) in groups.items():
        parent=src+(direct.direct_packet(basis,ns,z,u) if key=='independent' else basis.packet(basis.matrices(ns),z,len(u)))
        info=[]
        for A,Z in inputs:
            d=r205_delta(warm,ns,u,rad,basis.c,basis.end,A,Z)
            cur=evaluate(stream,stream.point,area,parent+d,rad,ns,u,stream.point.PointConfig(**dict(de['pointConfig'],true_cuff_height=Z)),w)
            cur['parameters']=[A,Z];info.append(cur)
            print(key,A,Z,cur['metric'],cur['curvature'],cur['held'],cur['R2'],flush=True)
        data[key]=info
    out=dict(schema='new-gap092-real-R205-tail-amplitude-and-actual-cap-height-v1',mode=a.mode,entrySHA256=sha(__file__),
        parentStateSHA256=sha(a.state),preparedSHA256=sha(a.prepared),observerSHA256=sha(a.observer),
        trueDevelopedTailSHA256=sha(a.scripts/'6a65-geometry-cauchy-unit-t-warm.py'),sourceTargetMetricFixed=True,
        completeR205TailAndBothCapsRepositioned=True,originalWholeCuffAndOpenFlatCollarPreservedAtNewHeight=True,
        optimizerAccepts=0,observations=data,finiteOnly=True,seconds=time.monotonic()-started)
    if a.mode=='select':
        rows=[]
        for x,y in zip(data['training'],data['observer']):
            assert x['parameters']==y['parameters'] and x['actualRows']+y['actualRows']==4291840
            rows.append(dict(parameters=x['parameters'],R2=x['R2']+y['R2'],held=min(x['held'],y['held']),metric=max(x['metric'],y['metric']),
                        curvature=max(x['curvature'],y['curvature'])))
        alts=[r for r in rows if tuple(r['parameters'])!=orig]
        feasible=[r for r in alts if r['held']>=.64]
        chosen=min(feasible or alts,key=lambda r:r['R2']);out['G10Selection']=chosen;out['fullG10Inputs']=rows
        out['selectionRule']='Among true changed tails meeting the finite .64 held threshold use smallest complete G10 R2; if none, minimum complete R2 among all changed.'
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','prepared','observer','state','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--mode',choices=('select','observe'),required=True);p.add_argument('--selection',type=Path)
    p.add_argument('--amplitudes',type=float,nargs='*',default=[]);p.add_argument('--heights',type=float,nargs='*',default=[])
    run(p.parse_args())
