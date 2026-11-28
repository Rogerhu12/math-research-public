#!/usr/bin/env python3
"""Bounded-memory supplier for the complete material-clocked HF64-M80-plus-W source."""
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import types
for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[k]="1"
import numpy as np

def sha(p):
    d=hashlib.sha256()
    with Path(p).open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):d.update(chunk)
    return d.hexdigest()

def canonical(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def module(p,name):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m

def old_data(path,scripts):
    old=Path(__file__).with_name('2ecf-polar-raw-ramp-source-compose.py')
    return module(old,'clocked_original_source').validate_prepared(argparse.Namespace(prepared=path,scripts=scripts))

def fill(pathmap,scripts,ns,u,base):
    args=types.SimpleNamespace(scripts=scripts,field=pathmap['field'],ramp=pathmap['ramp'],coast=pathmap['coast'])
    entry=module(Path(pathmap['clock_entry']),'clocked_material_analytic')
    fc=entry.Field(args,u);clock=entry.Clock(*fc.knots[[0,-1]])
    state=json.loads(Path(pathmap['clock_state']).read_text());x=np.asarray(state['coefficients'])
    if not np.array_equal(clock.knots,state['radialKnots']) or not np.array_equal(clock.freq,state['frequencies']):raise ValueError("Actual material clock required")
    acc=base.copy()
    ids=np.flatnonzero((ns>=fc.knots[0])&(ns<=fc.knots[-1]))
    for lo in range(0,len(ids),8):
        j=ids[lo:lo+8];acc[j]=entry.compose(fc,clock,ns[j],u,x)
    acc.setflags(write=False)
    return acc

def independent(saved,scripts):
    paths={k:Path(x) for k,x in saved['paths'].items()};rec=json.loads(paths['independent'].read_text())
    ns=np.array(rec['physicalNodes']);u=np.array(rec['angles'])
    jets=fill(paths,scripts,ns,u,np.load(rec['files']['jets'],mmap_mode='r'))
    return ns,u,jets,np.load(rec['files']['radius'],mmap_mode='r')

def verify(saved):
    if saved['prepareEntrySHA256']!=sha(__file__):raise ValueError("Actual source supplier changed")
    for k,fn in saved['paths'].items():
        if sha(fn)!=saved['filesSHA256'][k]:raise ValueError('Different input '+k)

def prepare(args):
    keys=('field','hf_report','clock_entry','clock_state','ramp','coast','parent','independent','frozen')
    paths={k:getattr(args,k).resolve() for k in keys};dig={k:sha(v) for k,v in paths.items()}
    hr=json.loads(paths['hf_report'].read_text());cs=json.loads(paths['clock_state'].read_text())
    if (hr['fieldSHA256']!=dig['field'] or cs['fieldSHA256']!=dig['field'] or cs['sourceSHA256']!=dig['clock_entry']
        or hr['preparedSHA256']!=dig['parent'] or hr['independentSHA256']!=dig['independent'] or hr['frozenStateSHA256']!=dig['frozen']
        or hr['rampSHA256']!=dig['ramp'] or hr['coastSHA256']!=dig['coast']):raise ValueError("Sources from inconsistent geometries")
    old,de,_,caches,*_=old_data(paths['parent'],args.scripts)
    raw={};meta=dict(schema='clocked-HF64-M80-with-entire-saved-W-and-neutral-clamped-additional-XYZ-v1',
        clockAndHFFiles=dig,frozenTargetDefinitionSHA256=hr['targetDefinitionSHA256'],parentH65Source=de['sourceIdentity'],
        addedPositionCoordinatesHaveIndependentOwnZero=True)
    saved=dict(paths={k:str(v) for k,v in paths.items()},filesSHA256=dig,sourceMetadata=meta,prepareEntrySHA256=sha(__file__),
        sourceIdentity=dict(schema=meta['schema'],identitySHA256=canonical(meta),sourceDefinition=meta),
        parentPreparedSHA256=old['parentPreparedSHA256'],physicalParentPreparedSHA256=dig['parent'])
    for key,c in caches.items():
        j=fill(paths,args.scripts,c.nodes,c.u,c.jets);raw[key]=hashlib.sha256(memoryview(j).cast('B')).hexdigest()
    _,_,j,_=independent(saved,args.scripts);raw['independent']=hashlib.sha256(memoryview(j).cast('B')).hexdigest()
    saved['completeSixJetSHA256']=raw
    with args.output.open('x') as f:json.dump(saved,f,separators=(',',':'));f.write('\n')
    print('actual complete source',raw,flush=True)

def validate_prepared(args):
    saved=json.loads(args.prepared.read_text());verify(saved)
    paths={k:Path(x) for k,x in saved['paths'].items()}
    old,de,basis,caches,mods,*_=old_data(paths['parent'],args.scripts)
    de=copy.deepcopy(de);de['sourceIdentity']=saved['sourceIdentity']
    saved['caches']=old['caches']
    for key,c in caches.items():
        c.jets=fill(paths,args.scripts,c.nodes,c.u,c.jets)
        if hashlib.sha256(memoryview(c.jets).cast('B')).hexdigest()!=saved['completeSixJetSHA256'][key]:raise ValueError("New source evaluation differs")
    return saved,de,basis,caches,mods,old,old['definition'],basis

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('field','hf-report','clock-entry','clock-state','ramp','coast','parent','independent','frozen','scripts','output'):
        p.add_argument('--'+k,required=True,type=Path)
    prepare(p.parse_args())
