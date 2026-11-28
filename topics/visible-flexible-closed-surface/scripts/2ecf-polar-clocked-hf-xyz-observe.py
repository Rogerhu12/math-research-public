#!/usr/bin/env python3
"""Full shifted G11 for an actual clocked-HF64-plus-correction position and its frozen target."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import types
for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[k]="1"
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sys.modules[name]=m;sp.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser()
    for k in ('prepared','scripts','state','frozen','output'):ap.add_argument('--'+k,type=Path,required=True)
    a=ap.parse_args();here=Path(__file__).resolve().parent
    prepentry=here/'2ecf-polar-clocked-hf-source.py';p=load(prepentry,'clocked_hf_supplier')
    saved=json.loads(a.prepared.read_text());p.verify(saved);oldpath=Path(saved['paths']['parent'])
    old,de,full,_,mods,*_=p.old_data(oldpath,a.scripts)
    coarse=load(here/'2ecf-polar-fixed-prefix-position-basis.py','hf_obscoarse').restrict(full)[0]
    fine=load(here/'2ecf-polar-local-suffix-boehm.py','hf_obsfine').build(coarse)[0]
    now=json.loads(a.state.read_text());frozen=json.loads(a.frozen.read_text());model=now['modelDefinition']
    if (now['preparedSHA256']!=sha(a.prepared) or now['sourceIdentity']!=saved['sourceIdentity'] or model['basis']!=fine.definition
        or model['frozenMetricDesignStateSHA256']!=sha(a.frozen) or model['frozenRadiusHex']!=frozen['provisionalMetricDefinition']['exactCoefficientHex']
        or model['solveEntrySHA256']!=sha(here/'2ecf-polar-clocked-hf-xyz-solve.py')):raise ValueError("Exact clocked XYZ state required")
    ns,u,jets,base=p.independent(saved,a.scripts)
    if hashlib.sha256(memoryview(jets).cast('B')).hexdigest()!=saved['completeSixJetSHA256']['independent']:raise ValueError("Independent shape changed")
    alpha=np.array(frozen['logRadiusCoefficients']);op=load(here/'2ecf-polar-log-radius-operator.py','hf_obsradius')
    radius=op.LogRadiusCache(coarse,types.SimpleNamespace(nodes=ns,u=u,jets=None,radius=base),alpha).radius
    direct=load(here/'2ecf-polar-c2-independent-g11-resume-observe.py','hf_obsdirect')
    z=np.array(now['z']).reshape(fine.nb,fine.na);stream=mods['stream'];cfg=stream.point.PointConfig(**model['pointConfig'])
    total=None
    for k in range(0,len(ns),12):
        row=ns[k:k+12];j=jets[k:k+len(row)]+direct.direct_packet(fine,row,z,u)
        bb=np.broadcast_to(radius[k:k+len(row),0,None],(len(row),len(u)))
        pt=stream.point.PointLinearized(j.swapaxes(1,2),bb,cfg,{g:np.ones((len(row),1))/len(u) for g in ('metric','curvature','geometry')})
        val=stream._block_statistics(pt,row,len(u));val['worstMetric']['u']+=u[0];val['worstCurvature']['u']+=u[0]
        total=stream._merge_statistics(total,val)
    total.pop('squaredNorm',None);total.pop('groupSquaredNorm',None)
    out=dict(schema='G11-clocked-HF64M80-plus-new-clamped-6615-XYZ-v1',entrySHA256=sha(__file__),stateSHA256=sha(a.state),
       preparedSHA256=sha(a.prepared),frozenDefinitionSHA256=model['frozenTargetDefinitionSHA256'],ownAccepted=now['ownExtendedAcceptedSteps'],
       completeRadials=len(ns),angles=len(u),statistics=total,finiteOnly=True)
    with a.output.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('actual G11',out['ownAccepted'],*[total[k] for k in ('maxRelativeMetric','maxCurvature','minHeldDistance')],flush=True)
if __name__=='__main__':main()
