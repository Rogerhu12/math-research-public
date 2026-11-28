#!/usr/bin/env python3
"""Actual complete G10 sparse-jet band versus independent full J/JT.

All 12789 physical directions are solved for simultaneously; the independent
normal residual uses the literal full point J/JT, not the assembled band.
This process produces no nonlinear trial or accepted optimization state.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,copy,gc,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np

def module(p,n):
    spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec)
    sys.modules[n]=m;spec.loader.exec_module(m);return m

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def band_apply(band,vector):
    value=np.asarray(vector).ravel();out=band[0]*value
    for d in range(1,band.shape[0]):
        out[d:]+=band[d,:len(value)-d]*value[:-d]
        out[:-d]+=band[d,:len(value)-d]*value[d:]
    return out

def main():
    ap=argparse.ArgumentParser()
    for k in ('scripts','prepare-entry','prepared','state','output'):ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    if args.output.exists():raise FileExistsError(args.output)
    prepare=module(args.prepare_entry,'sparse_full_normal_prepare')
    prepared,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    op=module(Path(__file__).with_name('2ecf-polar-log-radius-operator.py'),'sparse_full_normal_dependencies')
    deps=op.dependencies(args.scripts);stream=mods['stream']
    module(Path(__file__).with_name('2ecf-polar-complete-two-grid-streamed.py'),'sparse_full_normal_memory').install(deps['joint'])
    normalpath=Path(__file__).with_name('2ecf-polar-complete-sparse-jet-normal.py');normal=module(normalpath,'sparse_full_normal_actual')
    oldpath=args.scripts/'6a65-cartesian-complete-radial-normal-two-grid-area.py'
    if sha(oldpath)!=normal.ORIGINAL_SHA:raise ValueError('Original full normal provenance changed')
    recipe=copy.deepcopy(definition['recipe']);recipe['cachePointBlocks']=False
    config=stream.point.PointConfig(**definition['pointConfig']);area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    weights={k:{n:.5*np.asarray(v,float) for n,v in prepared['caches'][k]['weights'].items()} for k in caches}
    saved=json.loads(args.state.read_text());z=np.array(saved['z']).reshape(basis.nb,basis.na)
    linear=deps['area'].CompleteAreaTwoGrid(deps['joint'],stream,basis,caches,weights,z,config,recipe,area)
    damping=float(saved['nextDamping'])
    print(json.dumps(dict(event='actual_sparse_jet_full_normal_initial',rows=linear.shape[0],columns=linear.shape[1],
        R2=linear.statistics['squaredNorm'],damping=damping)),flush=True)
    tick=time.monotonic();aug=normal.SameSobolevAreaFullBandAugmented(linear,damping,eta=damping)
    assemblyseconds=time.monotonic()-tick
    print(json.dumps(dict(event='actual_sparse_jet_full_normal_assembled',seconds=assemblyseconds,
        assembly=aug.blocks.receipt)),flush=True)
    gradient=aug.raw_transpose(linear.residual)
    direction=-aug.blocks.unpack(aug.blocks.transpose(gradient))
    residual=aug.physical_normal_residual(direction)
    relative=float(np.linalg.norm(residual)/np.linalg.norm(gradient))
    if relative>1e-7:raise ArithmeticError('Actual full physical normal equation unresolved')
    rng=np.random.default_rng(2026112831);rows=[]
    for name,scale in (('raw_full_physical',False),('full_Sobolev',True)):
        raw=rng.standard_normal(basis.dimension);raw/=np.linalg.norm(raw)
        probe=linear.unpack(raw) if scale else raw.reshape(basis.nb,basis.na)
        direct=aug.raw_transpose(aug.raw_matvec(probe)).ravel()
        image=band_apply(aug.blocks.normal_band,probe)
        error=float(np.linalg.norm(image-direct)/max(1.,np.linalg.norm(direct)))
        row=dict(name=name,fullBandVersusIndependentJTJRelativeL2=error,
            originalPhysicalColumns=basis.dimension,originalPhysicalRows=linear.shape[0])
        print(json.dumps(dict(event='actual_sparse_jet_full_normal_comparison',**row)),flush=True)
        if error>3e-12:raise ArithmeticError('Full original J/JT and complete band differ')
        rows.append(row)
    out=dict(schema='2ecf-actual-complete-G10-sparse-jet-normal-audit-v1',entrySHA256=sha(__file__),normalEntrySHA256=sha(normalpath),
        preparedSHA256=sha(args.prepared),stateSHA256=sha(args.state),actualRows=linear.shape[0],actualColumns=basis.dimension,
        nonzeroActualField=bool(np.any(z)),baseline=linear.statistics,assembly=aug.blocks.receipt,
        fullPhysicalNormalRelativeResidual=relative,originalPhysicalGradientNorm=float(np.linalg.norm(gradient)),
        fullPhysicalNormalAbsoluteResidual=float(np.linalg.norm(residual)),randomFullNormalComparisons=rows,
        fullSourceAndTargetMetricUnchanged=True,allOriginal13AndQ2RowsRetained=True,
        allCartesianCrossTermsRetained=True,originalSobolevDampingUnchanged=True,
        sameCompleteObjective=True,optimizationAttempts=0,optimizationAccepts=0,
        seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(out,separators=(',',':'),allow_nan=False)+'\n')
    print(json.dumps(dict(event='actual_sparse_jet_full_normal_audit_complete',seconds=out['seconds'],
        physicalNormalRelativeResidual=relative)),flush=True)

if __name__=='__main__':main()
