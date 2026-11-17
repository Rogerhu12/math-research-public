#!/usr/bin/env python3
"""One same-input FFT/cache comparison against the saved unique dense probe.

No dense operator evaluation is repeated.  This compares all angle-value
residuals, Jv and J^T w and verifies the FFT complex-input path on the same
fixed direction.  It is an implementation comparison, not a new warm,
refinement, nonlinear solve, or continuous geometry certificate.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

DENSE_SHA='e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d'
PROBE_SHA='803f6c5e121a4f167984cc33371856d9978a3d13177f2315e7321f37ea533483'
FFT_SHA='7ab7391f3d351a5c2314d3c136fe5aa708612bb53e45221d2c09efc0fb622211'


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read_json(p):
    if Path(p).suffix=='.npz':
        with np.load(p,allow_pickle=False) as actual:
            return {name:actual[name] for name in actual.files}
    b=Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)


def comparison(actual,reference):
    if actual.shape!=reference.shape:raise ValueError('Different full result shape')
    d=actual-reference
    norms=[float(np.linalg.norm(z.ravel())) for z in (actual,reference,d)]
    return dict(shape=list(actual.shape),absolute_max=float(np.abs(d).max()),
                relative_l2=norms[2]/max(norms[0],norms[1],np.finfo(float).tiny),
                new_norm=norms[0],saved_dense_norm=norms[1])


def main(a):
    begin=time.perf_counter()
    if a.out.exists():raise FileExistsError('Do not silently repeat this unique comparison')
    if sha(a.dense_report)!=a.dense_report_sha:raise ValueError('Wrong complete dense probe report')
    dense=read_json(a.dense_report)
    if dense['source_sha256']!=PROBE_SHA or dense['operator_sha256']!=DENSE_SHA:
        raise ValueError('Wrong complete dense reference experiment')
    if sha(a.operator)!=DENSE_SHA or sha(a.fft_source)!=FFT_SHA:
        raise ValueError('An audited operator changed')
    if sha(a.bundle)!=dense['bundle_sha256'] or sha(a.arrays)!=dense['dense_array_archive']['sha256']:
        raise ValueError('Bundle or saved already-computed arrays changed')
    data=read_json(a.bundle)
    spec=importlib.util.spec_from_file_location('actual_fullclosed_FFT_comparison',a.fft_source)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    op=module.create(a.operator,data['mesh'],data['a_stages'],data['radius'],data['fixed_core_first3'],
                     M=160,N=2048,width=data.get('width',.05))
    x,affine=op.pack(np.asarray(data['qjets']),float(data['Hcap']),require_affine=True)
    report=dict(scope=__doc__,source_sha256=sha(__file__),fft_source_sha256=FFT_SHA,
                base_compare_source_sha256='0d0ddf15e1bc077c1462f57726892bfe8ca2004f937f818666bb70279f966f1c',
                dense_operator_sha256=DENSE_SHA,dense_report_sha256=a.dense_report_sha,
                dense_arrays_sha256=sha(a.arrays),bundle_sha256=dense['bundle_sha256'],
                M=op.M,N=op.N,nodes=op.J,stages=op.P,variables=op.free_size,
                residual_values=op.P*op.N*3,affine=affine,
                repeated_dense_evaluations=0,nonlinear_solve_executed=False,
                geometry_certified=False)
    with np.load(a.arrays,allow_pickle=False) as saved:
        if not np.array_equal(x,saved['x']):raise ValueError('Not the same literal free vector')
        v=saved['direction'];weights=saved['weights']
        t=time.perf_counter();report['cache']=op.set_base(x);report['cache_build_seconds']=time.perf_counter()-t
        t=time.perf_counter();result=op.residual(x);report['residual_seconds']=time.perf_counter()-t
        report['residual_comparison']=comparison(result,saved['dense_residual']);del result
        t=time.perf_counter();jv=op.jvp(x,v);report['jvp_seconds']=time.perf_counter()-t
        report['jvp_comparison']=comparison(jv,saved['dense_jvp'])
        t=time.perf_counter();jt=op.vjp(x,weights);report['adjoint_seconds']=time.perf_counter()-t
        report['adjoint_comparison']=comparison(jt,saved['dense_vjp'])
        left=float(np.dot(weights.ravel(),jv.ravel()));right=float(np.dot(jt,v))
        report['FFT_adjoint_identity']=dict(left=left,right=right,absolute=abs(left-right),
            relative=abs(left-right)/max(abs(left),abs(right),np.finfo(float).tiny))
        step=dense['full_Jacobian_check']['step']
        t=time.perf_counter();cs=op.residual(x.astype(complex)+1j*step*v).imag/step
        report['complex_path_seconds']=time.perf_counter()-t
        report['FFT_complex_path_vs_Jv']=comparison(cs,jv)
        report['FFT_complex_path_vs_saved_dense_Jv']=comparison(cs,saved['dense_jvp'])
    report['cache_hits']=op.cache_hits;report['cache_builds']=op.cache_builds
    report['elapsed_seconds']=time.perf_counter()-begin
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(event='complete_unique_same_input_FFT_comparison',report_sha256=sha(a.out),
                         residual=report['residual_comparison'],Jv=report['jvp_comparison'],
                         adjoint=report['adjoint_comparison'],nonlinear_solve_executed=False)),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('operator','fft-source','bundle','arrays','dense-report','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--dense-report-sha',required=True)
    main(p.parse_args())
