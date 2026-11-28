#!/usr/bin/env python3
"""Bitwise full-matrix check on the actual previously saved M24 J input.

The original complete RHS and analytic/centered parameter Jacobian are
reconstructed once. Both assemblers receive identical complete arrays. The
new installed prepare_sys path is also checked, and the result is compared
with the prior saved actual matrix. One complete old/new QR direction is compared; no BVP step or solution is produced.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gc
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.integrate import _bvp
from scipy.sparse import load_npz,save_npz

HERE=Path(__file__).resolve().parent
SCRIPTS=HERE.parents[1]
sys.path.insert(0,str(HERE))
import cached_fourier_tables as fourier
import material_core_evaluate_cache as memo
import direct_csr_collocation as direct


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj);return obj


def equal(first,second):
    return dict(shape=first.shape==second.shape,
        indices=np.array_equal(first.indices,second.indices),
        indptr=np.array_equal(first.indptr,second.indptr),
        data_bits=np.array_equal(first.data.view(np.uint64),second.data.view(np.uint64)))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prior-check',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args();args.outdir.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    prior=json.loads(args.prior_check.read_text())['actual']
    source_path=Path(prior['source_run']);snapshot=Path(prior['snapshot'])
    if sha(source_path)!=prior['source_run_sha256'] or sha(snapshot)!=prior['snapshot_sha256']:
        raise ValueError('The actual prior J input changed')
    saved_matrix=args.prior_check.parent/'actual_jacobian.npz'
    if sha(saved_matrix)!=prior['actual_matrix_sha256']:
        raise ValueError('The prior actual complete matrix changed')
    source=json.loads(source_path.read_text());command=list(source['command'][2:])
    portable=SCRIPTS/'resume_m3/portable_prefix_continue.py'
    original=load('_csc_actual_original_portable',portable);captured={}
    def capture(obj,x,y,p):captured.update(obj=obj,x=x,y=y,p=p)
    before=inspect.getsource(original.main);marker='        rhs = o.fun(x,y,par)'
    if before.count(marker)!=1:raise ValueError('The original capture point changed')
    original.__dict__['_csc_capture']=capture
    after=before.replace(marker,'        _csc_capture(o,x,y,par)\n        return')
    exec(compile(after,str(portable)+'::capture_without_solver','exec'),original.__dict__)
    command[command.index('--outdir')+1]=str(args.outdir/'problem-construction')
    for flag in ('--raw-restart','--restart-checkpoint'):
        if flag in command:
            i=command.index(flag);del command[i:i+2]
    command+=['--raw-restart',str(snapshot)]
    sys.argv=[str(portable),*command];original.main()
    obj,x,y,p=(captured[key] for key in ('obj','x','y','p'))
    n,m,k=obj.n,len(x),len(p);h=np.diff(x);xm=x[:-1]+.5*h
    if (n,m,k)!=(prior['n'],prior['nodes'],prior['k']):
        raise ValueError('The actual complete nodal input dimensions differ')
    tables=fourier.install(sys.modules['portable_m3_fourier_jac'])
    core=memo.install(type(obj._core))
    batching=load('_csc_actual_original_batches',SCRIPTS/'resume_20261126/streamed_release_prefix_driver.py')
    fun,bc,jac,bcjac=_bvp.wrap_functions(batching.split_rhs(obj.fun,32),obj.bc,
        batching.split_jac(obj.fun_jac,32),obj.bc_jac,k,x[0],None,None,np.float64)
    cr,ym,ff,fm=_bvp.collocation_fun(fun,y,p,x,h);br=bc(y[:,0],y[:,-1],p)
    begin=time.monotonic();dy,dp=jac(x,y,p);dym,dpm=jac(xm,ym,p)
    a,b,bp=bcjac(y[:,0],y[:,-1],p);partial_seconds=time.monotonic()-begin
    print(json.dumps(dict(event='actual_full_partial_arrays_returned',n=n,m=m,k=k,
        seconds=partial_seconds,maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    original_mid=dpm.copy()
    begin=time.monotonic();ii,jj=_bvp.compute_jac_indices(n,m,k)
    baseline=_bvp.construct_global_jac(n,m,k,ii,jj,h,dy,dym,dp,dpm,a,b,bp).tocsr()
    baseline_seconds=time.monotonic()-begin;baseline_mutation=dpm.copy()
    del ii,jj;gc.collect();dpm[:]=original_mid
    records=[];begin=time.monotonic()
    actual=direct.construct(n,m,k,None,None,h,dy,dym,dp,dpm,a,b,bp,record=records.append)
    direct_seconds=time.monotonic()-begin
    primary=equal(baseline,actual)
    mutation=np.array_equal(dpm.view(np.uint64),baseline_mutation.view(np.uint64))
    if not all(primary.values()) or not mutation:
        raise AssertionError(('direct assembler',primary,mutation))
    saved=load_npz(saved_matrix).tocsr();historical=equal(saved,actual)
    historical_max=float(np.max(np.abs(saved.data-actual.data))) if saved.nnz==actual.nnz else None
    del saved,baseline;gc.collect()

    # Use the unchanged prepare_sys consumer, with its actual complete input
    # derivatives replayed. This checks that no old constructor consumes None.
    def replay_jac(t,Y,P):
        if np.array_equal(t,x):return dy,dp
        if np.array_equal(t,xm):return dym,original_mid.copy()
        raise ValueError('Unexpected original derivative nodes')
    def replay_bc(ya,yb,P):return a,b,bp
    install_records=[];hashes,restore=direct.install(record=install_records.append)
    try:
        _,prepared=_bvp.prepare_sys(n,m,k,fun,bc,replay_jac,replay_bc,x,h)
        via_prepare=prepared(y,p,ym,ff,fm,br)
    finally:restore()
    installed=equal(actual,via_prepare)
    if not all(installed.values()) or install_records[-1]['input_COO_indices_were_none'] is not True:
        raise AssertionError(('installed complete path',installed))
    del via_prepare;gc.collect()
    path=args.outdir/'actual_direct_csr.npz';save_npz(path,actual)
    sys.path.insert(0,str(HERE.parent))
    from block_qr_v2 import BlockQR
    residual=np.load(args.prior_check.parent/'actual_residual.npy')
    if residual.shape!=(n*m+k,):raise ValueError('The historical full residual dimensions differ')
    reference=load_npz(saved_matrix).tocsr()
    ref_factor=BlockQR(reference,n,m,k)
    ref_direction=ref_factor.solve(residual)
    ref_stats=dict(ref_factor.stats)
    ref_absolute_residual=float(np.max(np.abs(ref_factor.matrix@ref_direction-residual)))
    del ref_factor,reference;gc.collect()
    actual_for_qr=actual.copy()
    new_factor=BlockQR(actual_for_qr,n,m,k)
    new_direction=new_factor.solve(residual)
    qr_check=dict(complete_direction_bitwise=np.array_equal(ref_direction.view(np.uint64),new_direction.view(np.uint64)),
        factor_and_solve_stats_identical=ref_stats==new_factor.stats,
        CSR_input_storage_is_shared=new_factor.matrix is actual_for_qr,
        actual_original_matrix_residual_max=float(np.max(np.abs(new_factor.matrix@new_direction-residual))),
        prior_original_matrix_residual_max=ref_absolute_residual,
        no_persistent_full_absolute_matrix=not hasattr(new_factor,'matrix_abs'),
        stored_factor_bytes=new_factor.stats['stored_factor_bytes'],
        original_stats=ref_stats,new_stats=dict(new_factor.stats))
    if not all(qr_check[key] for key in ('complete_direction_bitwise','factor_and_solve_stats_identical','CSR_input_storage_is_shared','no_persistent_full_absolute_matrix')):
        raise AssertionError(('complete QR',qr_check))
    del new_factor,actual_for_qr;gc.collect()

    report=dict(scope=__doc__,status='actual_complete_CSR_and_QR_bitwise_check_passed',
        prior_check=str(args.prior_check.resolve()),prior_check_sha256=sha(args.prior_check),
        source_run=str(source_path),source_run_sha256=sha(source_path),snapshot=str(snapshot),
        snapshot_sha256=sha(snapshot),n=n,m=m,k=k,shape=list(actual.shape),stored_entries=actual.nnz,
        source_partial_seconds=partial_seconds,original_assembly_seconds=baseline_seconds,
        direct_assembly_seconds=direct_seconds,original_vs_direct=primary,
        original_parameter_midpoint_mutation_bitwise=mutation,
        installed_prepare_sys_vs_direct=installed,installed_assembly_records=install_records,
        prior_saved_matrix_vs_direct=historical,prior_saved_matrix_max_entry_difference=historical_max,
        prior_saved_matrix_sha256=sha(saved_matrix),actual_direct_matrix_sha256=sha(path),
        direct_assembly_records=records,original_scipy_function_hashes=hashes,complete_QR_comparison=qr_check,
        actual_residual_sha256=sha(args.prior_check.parent/'actual_residual.npy'),
        source_hashes={str(file.resolve()):sha(file) for file in (
            Path(__file__),Path(direct.__file__),HERE.parent/'block_qr_v2.py',Path(fourier.__file__),Path(memo.__file__),portable)},
        complete_original_state_support_delta_and_boundary_entries_retained=True,
        parameters_removed=False,original_sampled_acceptance_gates_changed=False,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        fourier_cache=tables,core_memo=core,seconds=time.monotonic()-started,
        BVP_steps_applied=0,accepted_field_produced=False)
    (args.outdir/'comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:report[key] for key in ('status','n','m','k','stored_entries',
        'original_vs_direct','installed_prepare_sys_vs_direct','prior_saved_matrix_vs_direct',
        'prior_saved_matrix_max_entry_difference','complete_QR_comparison','maximum_rss_kib','seconds')},indent=2),flush=True)


if __name__=='__main__':main()
