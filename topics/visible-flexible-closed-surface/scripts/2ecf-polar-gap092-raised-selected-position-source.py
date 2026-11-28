#!/usr/bin/env python3
"""The actual upward bent tail and tall-throat geometry as a complete new fixed target."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for key in ('OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS'):
    os.environ[key]='1'
import numpy as np
def module(p,n):
    spec=importlib.util.spec_from_file_location(n,p)
    mod=importlib.util.module_from_spec(spec);sys.modules[n]=mod;spec.loader.exec_module(mod)
    return mod
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def write(p,data):
    with Path(p).open('x') as f:json.dump(data,f,separators=(',',':'));f.write('\n')
def make(a,files):
    here=Path(__file__).resolve().parent
    old=module(here/'2ecf-polar-new-central-gap-compose.py','selected_gap092_parent')
    saved,de,full,caches,mods,*_=old.validate_prepared(argparse.Namespace(prepared=Path(files['parent']),scripts=a.scripts))
    donor=read(files['donor']);selection=read(files['selection']);observer=read(files['independent'])
    restriction=module(here/'2ecf-polar-fixed-prefix-position-basis.py','selected_gap092_restriction')
    basis=restriction.restrict(full)[0];z=np.array(donor['z']).reshape(basis.nb,basis.na)
    scan=module(here/'2ecf-polar-raised-tail-tall-throat-source.py','selected_gap092_scan')
    warm=module(a.scripts/'6a65-geometry-cauchy-unit-t-warm.py','selected_gap092_R205')
    assert donor['preparedSHA256']==sha(files['parent']) and donor['modelDefinition']['basis']==basis.definition
    assert selection['donorSHA256']==sha(files['donor']) and selection['entrySHA256']==sha(scan.__file__)
    assert observer['sourceIdentity']==de['sourceIdentity'] and selection['independentSHA256']==sha(files['independent'])
    amp,cf,extent=selection['selected']['params'];Z=.415
    mods['stream'].point.PointConfig=scan.tall_config(mods['stream'].point.PointConfig)
    info=dict(schema='actual-inverted-tail-tall-throat-and-complete-Cartesian-correction-v1',flatThreshold=cf,radialLiftFraction=extent,newActualThroatEta=.115,capMetricChangedFromOriginal=True,
        inputs={k:sha(p) for k,p in files.items()},nodes=65,parentGapSourceIdentity=de['sourceIdentity'],amplitude=amp,
        trueCuffHeight=Z,oldTrueCuffHeight=de['pointConfig']['true_cuff_height'],allDonorCoefficientsInSource=True,
        originalParentValidated=True,sourceEntrySHA256=sha(__file__),scanEntrySHA256=sha(scan.__file__),R205EntrySHA256=sha(warm.__file__))
    source=dict(schema=info['schema'],identitySHA256=digest(info),sourceDefinition=info)
    de=copy.deepcopy(de);de['sourceIdentity']=source;de['pointConfig']['true_cuff_height']=Z;de['pointConfig']['height_maximum']=.113
    direct=module(here/'2ecf-polar-c2-independent-g11-resume-observe.py','selected_gap092_fourier')
    def add(ns,u,src,rad,independent):
        W=direct.direct_packet(basis,ns,z,u) if independent else basis.packet(basis.matrices(ns),z,len(u))
        return src+W+scan.delta(warm,ns,u,rad,basis.c,basis.end,amp,cf,extent)
    for c in caches.values():c.jets=add(c.nodes,c.u,c.jets,c.radius,False)
    def independent():
        assert all(sha(v)==observer['SHA256'][k] for k,v in observer['files'].items())
        ns=np.array(observer['physicalNodes']);u=np.array(observer['angles'])
        radius=np.load(observer['files']['radius'],mmap_mode='r')
        return ns,u,add(ns,u,np.load(observer['files']['jets'],mmap_mode='r'),radius,True),radius
    return saved,de,full,caches,mods,info,independent
def hasharray(a):return hashlib.sha256(memoryview(a).cast('B')).hexdigest()
def prepare(a):
    files={k:str(getattr(a,k).resolve()) for k in ('parent','donor','selection','independent')}
    saved,de,full,caches,mods,info,independent=make(a,files)
    raw={k:hasharray(c.jets) for k,c in caches.items()};raw['independent']=hasharray(independent()[2])
    write(a.output,dict(paths=files,completeSixJetSHA256=raw,sourceMetadata=info,sourceIdentity=de['sourceIdentity'],
        prepareEntrySHA256=sha(__file__),originalFullSpaceAuditParentSHA256=saved['originalFullSpaceAuditParentSHA256']))
def validate_prepared(a):
    new=read(a.prepared);saved,de,full,caches,mods,info,_=make(a,new['paths'])
    assert info==new['sourceMetadata'] and new['prepareEntrySHA256']==sha(__file__)
    assert all(hasharray(c.jets)==new['completeSixJetSHA256'][k] for k,c in caches.items())
    new['caches']=saved['caches']
    return new,de,full,caches,mods,saved,de,full
def observe(a):
    here=Path(__file__).resolve().parent
    new=read(a.prepared);saved,de,full,caches,mods,info,independent=make(a,new['paths'])
    assert info==new['sourceMetadata']
    ns,u,jets,rad=independent();assert hasharray(jets)==new['completeSixJetSHA256']['independent']
    direct=module(here/'2ecf-polar-c2-independent-g11-resume-observe.py','selected_gap092_observe_fourier')
    scan=module(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','selected_gap092_observe_scan')
    area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','selected_gap092_observe_area')
    restriction=module(here/'2ecf-polar-fixed-prefix-position-basis.py','selected_gap092_observe_basis')
    basis=restriction.restrict(full)[0];state=read(a.state)
    assert state['preparedSHA256']==sha(a.prepared) and state['modelDefinition']['basis']==basis.definition
    z=np.array(state['z']).reshape(basis.nb,basis.na);stream=mods['stream']
    q=scan.evaluate(stream,stream.point,area,jets+direct.direct_packet(basis,ns,z,u),rad,ns,u,stream.point.PointConfig(**de['pointConfig']),None)
    write(a.output,dict(statistics=q,ownAccepted=state['ownExtendedAcceptedSteps'],stateSHA256=sha(a.state),
        preparedSHA256=sha(a.prepared),sourceSHA256=sha(__file__),finiteOnly=True))
    print(q['metric'],q['curvature'],q['held'],flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['prepare','observe'],required=True)
    for k in ('scripts','parent','independent','donor','selection','output','prepared','state'):p.add_argument('--'+k,type=Path)
    args=p.parse_args()
    (prepare if args.mode=='prepare' else observe)(args)
