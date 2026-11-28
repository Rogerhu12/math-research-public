#!/usr/bin/env python3
"""Audit actual full G10 raw and Sobolev-scaled joint derivatives.

No source, target, objective, coefficient, or optimization counter is changed.
The raw probe repeats the failed production check before smaller steps.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.linalg.blas import dtbsv

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);sys.modules[name]=out;spec.loader.exec_module(out)
    return out

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    for key in ('scripts','prepare-entry','prepared','state','output'):
        ap.add_argument('--'+key,type=Path,required=True)
    args=ap.parse_args();start=time.monotonic()
    if args.output.exists():raise FileExistsError(args.output)
    prepare=module(args.prepare_entry,'full_joint_derivative_prepare')
    prepared,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    opath=Path(__file__).with_name('2ecf-polar-log-radius-operator.py')
    operator=module(opath,'full_joint_derivative_operator')
    deps=operator.dependencies(args.scripts);stream=mods['stream']
    memory=module(Path(__file__).with_name('2ecf-polar-complete-two-grid-streamed.py'),'full_joint_derivative_stream')
    memory.install(deps['joint'])
    config=stream.point.PointConfig(**definition['pointConfig'])
    recipe=copy.deepcopy(definition['recipe']);recipe['cachePointBlocks']=False
    area=dict(targetAreaRatio=.5,strength=1.,reciprocalPower=2)
    weights={k:{n:.5*np.asarray(v,float) for n,v in prepared['caches'][k]['weights'].items()} for k in caches}
    saved=json.loads(args.state.read_text())
    z=np.asarray(saved['z'],float).reshape(basis.nb,basis.na)
    alpha=np.asarray(saved.get('logRadiusCoefficients',np.zeros(basis.nb)),float)
    linear=operator.FullDesignLinear(deps,stream,basis,caches,weights,z,alpha,config,recipe,area)
    def residual(zz,aa):
        cc={k:operator.LogRadiusCache(basis,c,aa) for k,c in caches.items()}
        return deps['area'].residual(stream,basis,cc,weights,zz,config,recipe,area)
    rng=np.random.default_rng(2026112819)
    raw=rng.standard_normal(linear.shape[1]);raw/=np.linalg.norm(raw)
    cot=rng.standard_normal(linear.shape[0])
    dz,da=linear.split(raw)
    scaledz=linear.position.unpack(dz.ravel())
    lower,upper,channels=linear.position.preconditioner.factors[0]
    scaleda=dtbsv(lower.shape[0]-1,lower,da,lower=1,trans=1)
    scaled=linear.pack(scaledz,scaleda)
    output=dict(schema='2ecf-actual-full-joint-raw-and-Sobolev-derivative-audit-v1',
        entrySHA256=sha(__file__),operatorSHA256=sha(opath),preparedSHA256=sha(args.prepared),
        stateSHA256=sha(args.state),actualRows=linear.shape[0],actualColumns=linear.shape[1],
        optimizationAttempts=0,optimizationAccepts=0,probes=[])
    for name,direction,steps in (
        ('raw_original_production_then_smaller',raw,(1e-6,1e-7,1e-8,1e-9,1e-10,1e-11)),
        ('full_Sobolev_scaled',scaled,(1e-5,1e-6,1e-7)),
        ('radius_only',linear.pack(np.zeros_like(dz),da),(1e-5,1e-6,1e-7))):
        dz,da=linear.split(direction);jv=linear.matvec(direction)
        lhs,rhs=float(jv@cot),float(direction@linear.transpose(cot))
        row=dict(name=name,physicalDirectionNorm=float(np.linalg.norm(direction)),
            imageNorm=float(np.linalg.norm(jv)),radiusDirectionInfinityNorm=float(np.max(abs(da))),
            adjointRelativeError=abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs)),finiteDifferences=[])
        for eps in steps:
            plus=residual(z+eps*dz,alpha+eps*da);minus=residual(z-eps*dz,alpha-eps*da)
            difference=(plus-minus)/(2*eps)
            error=float(np.linalg.norm(difference-jv)/max(1.,np.linalg.norm(jv)))
            row['finiteDifferences'].append(dict(epsilon=eps,relativeL2=error,
                plusSquaredNorm=float(plus@plus),minusSquaredNorm=float(minus@minus)))
            print(json.dumps(dict(event='actual_full_joint_FD',probe=name,**row['finiteDifferences'][-1])),flush=True)
            del plus,minus,difference
        output['probes'].append(row)
        args.output.write_text(json.dumps(output,separators=(',',':'),allow_nan=False)+'\n')
        print(json.dumps(dict(event='actual_full_joint_probe',**row)),flush=True)
    output['seconds']=time.monotonic()-start
    output['allRowsAndColumnsRetained']=True
    args.output.write_text(json.dumps(output,separators=(',',':'),allow_nan=False)+'\n')

if __name__=='__main__':main()
