#!/usr/bin/env python3
"""Exactly one residual-only evaluation of the declared mode-damped warm.

The original frozen scalar/mesh/H/port are checked against the earlier
actual warm.  No Jv, adjoint, complex-step, curvature scan, normalization,
or nonlinear iteration is performed.  All summaries use one residual.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

DENSE_SHA='e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d'
FFT_SHA='7ab7391f3d351a5c2314d3c136fe5aa708612bb53e45221d2c09efc0fb622211'
OLD_SHA='401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load_npz(p):
    with np.load(p,allow_pickle=False) as a:return {k:a[k] for k in a.files}


def summary(op,res,selector):
    indices=np.flatnonzero(selector)
    if not len(indices):return dict(points=0)
    r=res[indices];ss,cross,pp=r[...,0],r[...,1],r[...,2]
    values=(np.abs(ss+pp)+np.sqrt((ss-pp)**2+4*cross*cross))/2
    ix=np.unravel_index(int(np.argmax(values)),values.shape);stage=int(indices[ix[0]])
    det=(1+ss)*(1+pp)-cross*cross
    return dict(points=int(values.size),maximum_relative_Gram_operator=float(values[ix]),
        location=dict(stage=stage,kind='node' if stage%2==0 else 'actual_quintic_midpoint',
                      s=float(op.times[stage]),angle=float(op.phi[ix[1]])),
        component_maximum=np.max(np.abs(r),axis=(0,1)).tolist(),
        relative_Gram_determinant_min=float(det.min()),
        Frobenius_square_sum=float(np.sum(ss*ss+2*cross*cross+pp*pp)),
        continuous_metric_or_immersion_certified=False)


def main(a):
    began=time.perf_counter()
    if a.out.exists() or a.residual.exists():raise FileExistsError('Do not repeat or overwrite this one new-warm evaluation')
    if sha(a.operator)!=DENSE_SHA or sha(a.fft_source)!=FFT_SHA:
        raise ValueError('The previously compared complete operator changed')
    if sha(a.original_bundle)!=OLD_SHA or sha(a.bundle)!=a.bundle_sha:
        raise ValueError('Wrong original/new actual bundle')
    old,new=load_npz(a.original_bundle),load_npz(a.bundle)
    unchanged={k:bool(np.array_equal(new[k],old[k])) for k in
        ('mesh','a_stages','radius','Hcap','width','fixed_core_first3')}
    if not all(unchanged.values()):raise ValueError('The declared same scalar/mesh/H/port condition failed: '+str(unchanged))
    prefix=np.asarray(new['mesh'])<=1.
    prefix_diff=np.asarray(new['qjets'])[prefix]-np.asarray(old['qjets'])[prefix]
    if np.any(prefix_diff!=0):raise ValueError('The declared original prefix was changed')
    spec=importlib.util.spec_from_file_location('new_actual_warm_fft',a.fft_source)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    op=module.create(a.operator,new['mesh'],new['a_stages'],new['radius'],new['fixed_core_first3'],
                     M=160,N=2048,width=new['width'])
    x,affine=op.pack(new['qjets'],float(new['Hcap']),require_affine=True)
    prep=op.prepare(x)
    if not np.isfinite(prep.rho).all() or np.min(prep.rho)<=0:raise ValueError('Actual supplied core is not positive even on the fixed samples')
    start=time.perf_counter();res=op.residual(x);seconds=time.perf_counter()-start
    np.save(a.residual,res,allow_pickle=False)
    selection=np.ones(op.P,dtype=bool)
    report=dict(schema='fullclosed-mode-damped-actual-warm-one-residual-v1',scope=__doc__,
        source_sha256=sha(__file__),dense_operator_sha256=DENSE_SHA,fft_source_sha256=FFT_SHA,
        original_bundle_sha256=OLD_SHA,bundle_sha256=a.bundle_sha,
        unchanged_inputs=unchanged,all_prefix_shared_jets_unchanged=True,
        prefix_node_count=int(prefix.sum()),M=op.M,N=op.N,nodes=op.J,stages=op.P,
        variables=op.free_size,residual_values=op.P*op.N*3,affine=affine,
        structural_checks=op.affine_diagnostics(x),sampled_core_rho_min=float(prep.rho.min()),
        all=summary(op,res,selection),node_samples=summary(op,res,np.arange(op.P)%2==0),
        midpoints=summary(op,res,np.arange(op.P)%2==1),
        prefix=summary(op,res,op.times<=1.),tail=summary(op,res,op.times>1.),
        lift_region=summary(op,res,op.times>=op.S-op.width),
        residual_seconds=seconds,elapsed_seconds=time.perf_counter()-began,
        residual_file=dict(path=str(a.residual.resolve()),sha256=sha(a.residual),bytes=a.residual.stat().st_size),
        residual_evaluations=1,Jv_evaluations=0,adjoint_evaluations=0,complex_step_evaluations=0,
        new_nonlinear_solve=False,continuous_geometry_certified=False)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='complete_one_mode_damped_warm_residual',report_sha256=sha(a.out),
                         all=report['all'],prefix=report['prefix'],tail=report['tail'],
                         residual_evaluations=1,new_nonlinear_solve=False)),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('operator','fft-source','original-bundle','bundle','out','residual'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--bundle-sha',required=True)
    main(p.parse_args())
