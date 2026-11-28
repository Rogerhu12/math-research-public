#!/usr/bin/env python3
"""Independent direct-angle G11 observation of one immutable designed g.

Reuses only the validated existing base-source cache. The new observer has
its own identity and never rewrites the original source consumer SHA.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np


def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def main():
    ap=argparse.ArgumentParser()
    for key in ('scripts','prepare-entry','prepared','frozen-target','observer','state','output'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--reference-observation',type=Path)
    args=ap.parse_args();start=time.monotonic()
    if args.output.exists():raise FileExistsError(args.output)
    original_entry=Path(__file__).with_name('2ecf-polar-c2-independent-g11-resume-observe.py')
    original=module(original_entry,'frozen_g_original_G11_source')
    freezing=module(Path(__file__).with_name('2ecf-polar-freeze-designed-target.py'),'frozen_g_exact_target')
    saved,definition,basis,mods=original.source_and_basis(args)
    frozen=freezing.load_frozen(args.frozen_target,sha(args.prepared),definition['sourceIdentity'],basis.definition)
    target=frozen['frozenMetricDefinition'];state=json.loads(args.state.read_text())
    if (state.get('schema')!='2ecf-polar-C2-frozen-designed-g-full-normal-LM-v1-state'
            or canonical(state['modelDefinition'])!=state['modelDefinitionSHA256']
            or state['preparedSHA256']!=sha(args.prepared)
            or state['modelDefinition']['basis']!=basis.definition
            or state['frozenTargetManifestSHA256']!=sha(args.frozen_target)
            or state['frozenMetricDefinition']!=target
            or state['frozenLogRadiusCoefficients']!=target['coefficients']
            or state['modelDefinition']['pointConfig']!=definition['pointConfig']):
        raise ValueError('The exact actual fixed-designed-metric state is required')
    src=json.loads(args.observer.read_text())
    if (src['sourceEntrySHA256']!=sha(original_entry)
            or src['sourceIdentity']!=definition['sourceIdentity']
            or src['sourceDefinitionSHA256']!=saved['sourceMetadata']['sourceDefinitionSHA256']
            or src['basis']!=basis.definition):
        raise ValueError('Original direct independent source consumer and actual complete basis required')
    for key,path in src['files'].items():
        if sha(path)!=src['SHA256'][key]:raise ValueError('Original source cache changed')
    nodes,angles=np.array(src['physicalNodes']),np.array(src['angles'])
    jets=np.load(src['files']['jets'],mmap_mode='r')
    base_radius=np.load(src['files']['radius'],mmap_mode='r')
    alpha=np.asarray(target['coefficients'],float)
    h,hs,hss=(B@alpha for B in basis.matrices(nodes));a,first,second=base_radius.T
    ex=np.exp(h);radius=np.column_stack((a*ex,(first+a*hs)*ex,(second+2*first*hs+a*(hss+hs*hs))*ex))
    if not np.all(np.isfinite(radius)) or np.any(radius[:,0]<=0):
        raise ArithmeticError('Actual frozen target must evaluate finite positive')
    z=np.asarray(state['z'],float).reshape(basis.nb,basis.na)
    stream=mods['stream'];config=stream.point.PointConfig(**definition['pointConfig']);total=None
    for lo in range(0,len(nodes),12):
        ns=nodes[lo:lo+12]
        packet=jets[lo:lo+12]+original.direct_packet(basis,ns,z,angles)
        point=stream.point.PointLinearized(packet.swapaxes(1,2),
            np.broadcast_to(radius[lo:lo+12,0,None],(len(ns),len(angles))),config,
            {key:np.ones((len(ns),1))/len(angles) for key in ('metric','curvature','geometry')})
        part=stream._block_statistics(point,ns,len(angles))
        part['worstMetric']['u']+=float(angles[0]);part['worstCurvature']['u']+=float(angles[0])
        total=stream._merge_statistics(total,part)
    checknodes=np.linspace(basis.c,basis.end,9);u=2*np.pi*np.arange(128)/128
    direct=original.direct_packet(basis,checknodes,z,u)
    fft=basis.packet(basis.matrices(checknodes),z,128)
    errors=np.max(abs(direct-fft),axis=(0,2,3)).tolist()
    total.pop('squaredNorm',None);total.pop('groupSquaredNorm',None)
    comparison=None
    if args.reference_observation:
        ref=json.loads(args.reference_observation.read_text())
        if (state['ownFrozenMetricAttempts']!=0
                or ref['stateSHA256']!=frozen['parentDesignStateSHA256']
                or ref['designedMetricDefinitionSHA256']!=frozen['parentProvisionalMetricDefinitionSHA256']
                or ref['sourceObserverSHA256']!=sha(args.observer)
                or ref['statistics']!=total):
            raise ArithmeticError('Independent actual observation changed while freezing alpha')
        comparison=dict(referenceObservationSHA256=sha(args.reference_observation),
            allIndependentStatisticsIdentical=True,actualNewFixedMetricAccepts=0)
    report=dict(schema='2ecf-actual-frozen-designed-g-G11-observation-v1',entrySHA256=sha(__file__),
        originalSourceConsumerSHA256=sha(original_entry),sourceObserverSHA256=sha(args.observer),
        preparedSHA256=sha(args.prepared),stateSHA256=sha(args.state),
        frozenTargetManifestSHA256=sha(args.frozen_target),
        frozenMetricDefinitionSHA256=frozen['frozenMetricDefinitionSHA256'],
        ownFrozenMetricAttempts=state['ownFrozenMetricAttempts'],
        ownFrozenMetricAcceptedSteps=state['ownFrozenMetricAcceptedSteps'],
        parentDesignAcceptedStepsNotBorrowed=frozen['parentDesignAcceptedSteps'],
        allRadiusParametersConstant=True,actualRadialCount=len(nodes),actualAngularCount=len(angles),
        angularShiftInMeshSteps=.5,
        actualRadialsNotInTraining=int(len(np.setdiff1d(nodes,saved['caches']['training']['nodes']))),
        statistics=total,minAreaRatio=float(np.sqrt(total['minImmersion'])),
        sameActualFieldDirectVersusProductionFFTSixJetErrors=errors,
        baselineComparison=comparison,objectiveCostNotClaimed=True,observerUsedInOptimization=False,
        finiteSamplesOnly=True,continuousMetricCertified=False,wholeClosedReachCertified=False,
        seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(report,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual_frozen_metric_independent_G11',SHA256=sha(args.output),
        ownFrozenMetricAcceptedSteps=report['ownFrozenMetricAcceptedSteps'],
        metric=total['maxRelativeMetric'],curvature=total['maxCurvature'],
        sigma=report['minAreaRatio'],held=total['minHeldDistance'],seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
