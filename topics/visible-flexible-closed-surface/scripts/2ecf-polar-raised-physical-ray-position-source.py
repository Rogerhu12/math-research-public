#!/usr/bin/env python3
"""Actual finite operator source for a full explicitly reconstructed R273 all-ray surface."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
def get(p):return json.loads(Path(p).read_text())
def write(p,data):
    with Path(p).open('x') as f:json.dump(data,f,separators=(',',':'));f.write('\n')
def digest(data):return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def array_sha(x):return hashlib.sha256(memoryview(x).cast('B')).hexdigest()
def actual(a,paths):
    here=Path(__file__).resolve().parent
    src=load(here/'2ecf-polar-new-central-gap-compose.py','ray_solver_gap')
    saved,de,full,caches,mods,*_=src.validate_prepared(argparse.Namespace(scripts=a.scripts,prepared=Path(paths['parent'])))
    ind=get(paths['independent']);d=get(paths['design']);checked=get(paths['observation'])
    assert d['fieldSHA256']==checked['fieldSHA256']==sha(paths['field']) and d['rampSHA256']==sha(paths['ramp']) and d['coastSHA256']==sha(paths['coast'])
    assert checked['preparedSHA256']==sha(paths['parent']) and checked['independentSHA256']==sha(paths['independent']) and checked['designSHA256']==sha(paths['design'])
    op=load(here/'2ecf-polar-raised-physical-ray-field-observe.py','ray_solver_analytic_field')
    end=load(here/'2ecf-polar-raised-monotone-oblique-connector.py','ray_solver_endpoint')
    assert checked['entrySHA256']==sha(op.__file__)
    ends=end.Ends(a.scripts,paths['ramp'],paths['coast'],d['amp'],d['flat'],checked['traceNodes'])
    ray=op.PhysicalRays(paths['field'],ends);b,S=ray.knots[[0,-1]]
    meta=dict(schema='R273-complete-actual-geometric-ray-seed-frozen-g-clamped-5292-v1',filesSHA256={k:sha(p) for k,p in paths.items()},
        originalGapSource=de['sourceIdentity'],nodes=65,allRayDegree=d['quadrantIntervals'],
        allRayRadialIntervals=d['physicalIntervals'],trueModifiedCapMetric=True,newCuffHeight=.415,newThroatLift=.115,
        amplitude=d['amp'],flatThreshold=d['flat'],newSourceEntrySHA256=sha(__file__),analyticEvaluatorSHA256=sha(op.__file__))
    identity=dict(schema=meta['schema'],identitySHA256=digest(meta),sourceDefinition=meta)
    de=dict(de,pointConfig=dict(de['pointConfig'],true_cuff_height=.415,height_maximum=.113),sourceIdentity=identity)
    mods['stream'].point.PointConfig=ends.raised.tall_config(mods['stream'].point.PointConfig)
    def fill(ns,u,j0,rad):
        j=j0.copy();idx=np.flatnonzero((ns>=b)&(ns<=S))
        for start in range(0,len(idx),12):
            ii=idx[start:start+12];j[ii]=ray.position(ns[ii],u)
        for i in np.flatnonzero(ns>S):
            po=ends.raised.raised_port(ends.warm,d['amp'],d['flat'],u,rad[i,0]);j[i]=np.stack([po[k] for k in ('P','V','Pu','A','Vu','Puu')])
        return j
    for c in caches.values():c.jets=fill(c.nodes,c.u,c.jets,c.radius)
    def independent():
        assert all(sha(v)==ind['SHA256'][k] for k,v in ind['files'].items())
        ns=np.array(ind['physicalNodes']);u=np.array(ind['angles']);rad=np.load(ind['files']['radius'],mmap_mode='r')
        return ns,u,fill(ns,u,np.load(ind['files']['jets'],mmap_mode='r'),rad),rad
    return saved,de,full,caches,mods,meta,independent
def prepare(a):
    p={k:str(getattr(a,k).resolve()) for k in ('parent','independent','ramp','coast','field','design','observation')}
    old,de,_,caches,_,meta,ind=actual(a,p)
    ids={k:array_sha(c.jets) for k,c in caches.items()};ids['independent']=array_sha(ind()[2])
    write(a.output,dict(paths=p,sourceMetadata=meta,completeSixJetSHA256=ids,prepareEntrySHA256=sha(__file__),
        sourceIdentity=de['sourceIdentity'],originalFullSpaceAuditParentSHA256=old['originalFullSpaceAuditParentSHA256']))
def validate_prepared(a):
    new=get(a.prepared);old,de,full,caches,mods,meta,_=actual(a,new['paths'])
    assert new['sourceMetadata']==meta and new['prepareEntrySHA256']==sha(__file__)
    assert all(array_sha(v.jets)==new['completeSixJetSHA256'][k] for k,v in caches.items())
    new['caches']=old['caches'];return new,de,full,caches,mods,old,de,full
def observe(a):
    here=Path(__file__).parent;new=get(a.prepared);old,de,full,caches,mods,meta,ind=actual(a,new['paths'])
    assert new['sourceMetadata']==meta and new['prepareEntrySHA256']==sha(__file__)
    ns,u,j,rad=ind();assert array_sha(j)==new['completeSixJetSHA256']['independent']
    state=get(a.state);co=load(here/'2ecf-polar-fixed-prefix-position-basis.py','ray_obs_basis').restrict(full)[0]
    assert state['preparedSHA256']==sha(a.prepared) and state['modelDefinition']['basis']==co.definition
    dr=load(here/'2ecf-polar-c2-independent-g11-resume-observe.py','ray_obs_Fourier');z=np.array(state['z']).reshape(co.nb,co.na)
    scan=load(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','ray_obs_scan')
    area=load(a.scripts/'6a65-geometry-area-ratio-power-two.py','ray_obs_area');stream=mods['stream']
    v=scan.evaluate(stream,stream.point,area,j+dr.direct_packet(co,ns,z,u),rad,ns,u,stream.point.PointConfig(**de['pointConfig']),None)
    write(a.output,dict(statistics=v,ownAccepted=state['ownExtendedAcceptedSteps'],stateSHA256=sha(a.state),
        sourceSHA256=sha(__file__),preparedSHA256=sha(a.prepared),finiteOnly=True));print(v['metric'],v['curvature'],v['held'])
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=['prepare','observe'],required=True)
    for k in ('scripts','parent','independent','ramp','coast','field','design','observation','output','prepared','state'):p.add_argument('--'+k,type=Path)
    a=p.parse_args();(prepare if a.mode=='prepare' else observe)(a)
