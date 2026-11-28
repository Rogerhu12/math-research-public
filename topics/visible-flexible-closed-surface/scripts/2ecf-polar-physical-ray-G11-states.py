#!/usr/bin/env python3
"""One independent complete six-jet source evaluation for several physically distinct accepted XYZ states."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def read(p):return json.loads(Path(p).read_text())
def run(a):
    here=Path(__file__).parent;op=module(here/'2ecf-polar-raised-physical-ray-position-source.py','combined_ray_source')
    new=read(a.prepared);old,de,full,cache,mods,meta,ind=op.actual(a,new['paths']);del cache
    assert new['sourceMetadata']==meta and new['prepareEntrySHA256']==sha(op.__file__)
    ns,u,j,rad=ind();assert op.array_sha(j)==new['completeSixJetSHA256']['independent']
    coarse=module(here/'2ecf-polar-fixed-prefix-position-basis.py','combined_ray_basis').restrict(full)[0]
    dr=module(here/'2ecf-polar-c2-independent-g11-resume-observe.py','combined_ray_direct')
    scan=module(here/'2ecf-polar-gap092-true-tail-amplitude-height.py','combined_ray_scan')
    area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','combined_ray_area');stream=mods['stream'];cfg=stream.point.PointConfig(**de['pointConfig'])
    result=[]
    for state in a.states:
        st=read(state);assert st['modelDefinition']['basis']==coarse.definition and st['preparedSHA256']==sha(a.prepared)
        z=np.array(st['z']).reshape(coarse.nb,coarse.na)
        v=scan.evaluate(stream,stream.point,area,j+dr.direct_packet(coarse,ns,z,u),rad,ns,u,cfg,None)
        result.append(dict(stateSHA256=sha(state),ownAccepted=st['ownExtendedAcceptedSteps'],statistics=v))
        print(st['ownExtendedAcceptedSteps'],v['metric'],v['curvature'],v['held'],flush=True)
    with a.output.open('x') as f:json.dump(dict(entrySHA256=sha(__file__),preparedSHA256=sha(a.prepared),finiteOnly=True,rows=result),f,indent=2);f.write('\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','prepared','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--states',type=Path,nargs='+',required=True);run(p.parse_args())
