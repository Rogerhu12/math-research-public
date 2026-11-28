#!/usr/bin/env python3
"""Finish the storage check using its already computed genuine 17-node system.

The first real check passed its complete partial/CSR assertions and saved
the original small system, then its event JSON encountered a NumPy boolean.
This successor does not reevaluate a physical RHS or partial derivative. It
replays those saved complete arrays into the same disk-backed batch wrapper,
then checks original SciPy/full CSR, all-factor adoption, original complete
QR direction/diagnostics and storage lifetime. No BVP is invoked or accepted.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'

import argparse
import gc
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import weakref

import numpy as np
from scipy.integrate import _bvp

HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE),str(HERE.parent),str(HERE.parent/'analytic')]
import complete_mapped_jacobian_partials as partial_storage
import direct_csr_collocation as original_assembly
import complete_streamed_csr_assembly as mapped_assembly
import block_qr_v2 as qr
import actual_process_memory_limits as limits

PINNED={
    'check_complete_mapped_partials_actual.py':'0e577da754d06c7205e444fa064c44b8555dc8923d6cde621bf85b03c44f5212',
    'complete_mapped_jacobian_partials.py':'1ce67cd198331e84d0d7ea434fe1b30027f5c144fb5be90ab6c1af1d38c3e2f3',
    '../analytic/complete_streamed_csr_assembly.py':'242d00c55b68083611e49eabef7ec86c8a4f5128254a03b26e8a0c3121beaca3'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def identical(left,right):
    return bool(left.dtype==right.dtype and left.shape==right.shape
                and left.tobytes(order='C')==right.tobytes(order='C'))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous-outdir',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args()
    previous,out=args.previous_outdir.resolve(),args.outdir.resolve()
    for name,expected in PINNED.items():
        if sha(HERE/name)!=expected:
            raise ValueError('The actual checked source changed: '+name)
    history=json.loads((previous/'events.jsonl').read_text().splitlines()[0])
    actual_terminal=json.loads((previous/'observed-tool-terminal.json').read_text())
    payload=previous/'real-selected-original-system.npz'
    if (history['event']!='real_small_storage_check_started'
            or actual_terminal['actual_tool_exit_code']!=1
            or actual_terminal['physical_partials_recomputed_for_followup'] is not False
            or actual_terminal['saved_system']['sha256']!=sha(payload)):
        raise ValueError('Require the real ended predecessor and exact completed small-system bytes')
    with np.load(payload,allow_pickle=False) as saved:
        arrays={key:saved[key].copy() for key in saved.files}
    x,y,p,h,ym,rhs=(arrays[key] for key in ('x','y','p','h','ym','rhs'))
    dy,dym,dp,dpm=(arrays[key] for key in ('dy','dym','dp','dpm_before_original_update'))
    bca,bcb,bcp=(arrays[key] for key in ('bca','bcb','bcp'))
    n,m,k=y.shape[0],len(x),len(p)
    if (n,m,k)!=(97,17,32) or x[0]!=0 or x[-1]!=1:
        raise ValueError('The observed real complete diagnostic dimensions changed')
    out.mkdir(parents=True,exist_ok=False)
    started=time.monotonic()
    first_limits=limits.snapshot()
    events=out/'events.jsonl'
    def event(kind,**fields):
        row=dict(event=kind,elapsed_seconds=time.monotonic()-started,
            maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**fields)
        with events.open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)
    event('saved_real_complete_small_system_loaded',source=ref(payload),
        predecessor_terminal=ref(previous/'observed-tool-terminal.json'),
        no_physical_RHS_or_partial_reevaluation=True)
    registry=partial_storage.CompletePartialRegistry(out,entry_sha256=sha(__file__))
    def replay(grid,states,left,right):
        def evaluate(t,yy,pp):
            indices=np.searchsorted(grid,t)
            if (not np.array_equal(grid[indices],t) or not np.array_equal(pp,p)
                    or not np.array_equal(states[:,indices],yy)):
                raise ValueError('The saved original complete partial coordinates differ')
            return left[:,:,indices],right[:,:,indices]
        return evaluate
    new_dy,new_dp=registry.make_split_jac()(replay(x,y,dy,dp),8)(x,y,p)
    middle_x=x[:-1]+h/2
    new_dym,new_dpm=registry.make_split_jac()(replay(middle_x,ym,dym,dpm),8)(middle_x,ym,p)
    checks={}
    for name,left,right in (('dy',dy,new_dy),('dp',dp,new_dp),('dym',dym,new_dym),('dpm',dpm,new_dpm)):
        checks[name+'_saved_actual_partial_bytes_identical']=identical(left,right)
        checks[name+'_saved_actual_partial_strides_identical']=bool(left.strides==right.strides)
    del left,right
    scipy_dpm=dpm.copy(order='C')
    i,j=_bvp.compute_jac_indices(n,m,k)
    scipy_matrix=_bvp.construct_global_jac(n,m,k,i,j,h,dy,dym,dp,scipy_dpm,bca,bcb,bcp).tocsr()
    direct_dpm=dpm.copy(order='C')
    old_matrix=original_assembly.construct(n,m,k,None,None,h,dy,dym,dp,direct_dpm,bca,bcb,bcp,
                                          radial_block=16)
    root=mapped_assembly.owned_storage_root(out)
    new_matrix=mapped_assembly.construct(n,m,k,None,None,h,new_dy,new_dym,new_dp,new_dpm,
        bca,bcb,bcp,storage_directory=root,radial_block=3,release_inputs=registry.release_inputs)
    for name in ('data','indices','indptr'):
        checks['original_direct_CSR_'+name+'_all_bytes_identical']=identical(
            getattr(old_matrix,name),getattr(new_matrix,name))
        checks['original_SciPy_CSR_'+name+'_all_bytes_identical']=identical(
            getattr(scipy_matrix,name),getattr(new_matrix,name))
    checks['original_middle_dp_side_effect_identical']=identical(scipy_dpm,new_dpm) and identical(direct_dpm,new_dpm)
    checks['original_middle_dp_side_effect_nonzero']=not identical(dpm,new_dpm)
    checks['all_original_explicit_zeros_preserved']=bool(
        np.count_nonzero(old_matrix.data==0)==np.count_nonzero(new_matrix.data==0))
    before_prune=dict(unknowns=n*m+k,stored_entries=len(new_matrix.data),
        explicit_zeros=int(np.count_nonzero(new_matrix.data==0)))
    del new_dy,new_dym,new_dp,new_dpm,scipy_matrix,scipy_dpm,direct_dpm,i,j
    gc.collect()
    checks['all_partial_pairs_released_before_QR']=not registry.stores
    checks['all_partial_backing_directories_removed_before_QR']=not list(
        registry.directory.glob('complete-partials-*'))
    if not all(checks.values()):
        raise ArithmeticError('The complete partial or CSR storage check failed: '+str(checks))
    event('complete_partial_CSR_and_release_checks_passed',checks=checks,before_original_prune=before_prune)
    factor_directory=out/'mapped-factor-storage'
    factor_directory.mkdir()
    old_factor=qr.BlockQR(old_matrix,n,m,k)
    old_answer=old_factor.solve(rhs)
    original_stats=dict(old_factor.stats)
    new_factor=mapped_assembly.AdoptedBeforeQRMappedBlockQR(new_matrix,n,m,k,
                                                          storage_directory=factor_directory)
    new_answer=new_factor.solve(rhs)
    checks['same_complete_CSR_object_adopted']=new_factor.matrix is new_matrix
    checks['complete_QR_direction_all_bytes_identical']=identical(old_answer,new_answer)
    checks['all_original_QR_diagnostics_identical']=original_stats==new_factor.stats
    for name in ('data','indices','indptr'):
        checks['after_original_prune_CSR_'+name+'_all_bytes_identical']=identical(
            getattr(old_matrix,name),getattr(new_matrix,name))
    for label,store in (('CSR',new_factor._complete_csr_store),('factor',new_factor._complete_store)):
        checks[label+'_complete_page_release_returned']=store.stats.get(
            'last_solve_page_release',{}).get('clean_mapped_pages_advised_DONTNEED') is True
    checks['no_second_CSR_backing_created']=new_factor._complete_csr_store.stats['second_complete_CSR_copy_created'] is False
    csr_stats,factor_stats=dict(new_factor._complete_csr_store.stats),dict(new_factor._complete_store.stats)
    csr_path,factor_path=Path(new_factor._complete_csr_store.directory),Path(new_factor._complete_store.directory)
    residual=old_matrix@new_answer-rhs
    matrix_weak,factor_weak=weakref.ref(new_matrix),weakref.ref(new_factor)
    del new_factor,new_matrix,old_factor,store
    gc.collect()
    checks['actual_factor_and_CSR_lifetime_released']=matrix_weak() is None and factor_weak() is None
    checks['owned_CSR_factor_files_released']=not csr_path.exists() and not factor_path.exists()
    final_limits=limits.snapshot()
    report=dict(status='actual_saved_complete_small_storage_comparison_returned',scope=__doc__,
        original_actual_source=history['inputs'],predecessor_source_hashes=history['source_hashes'],
        original_actual_partial_stage_exit=ref(previous/'observed-tool-terminal.json'),
        original_actual_selected_complete_system=ref(payload),
        source_hashes={str(Path(module.__file__).resolve()):sha(module.__file__) for module in
            (sys.modules[__name__],partial_storage,original_assembly,mapped_assembly,qr,limits)},
        source_node_indices=arrays['source_indices'].tolist(),n=n,m=m,k=k,
        original_grid_nodes=1185,coarse_diagnostic_grid_not_BVP_acceptance=True,
        original_partial_batch=8,new_interval_block=3,original_direct_interval_block=16,
        all_checks=checks,before_original_prune=before_prune,
        original_complete_QR_statistics=original_stats,
        complete_original_J_residual_maximum=float(np.max(np.abs(residual))),
        complete_original_J_residual_l2=float(np.linalg.norm(residual)),
        original_rhs_l2=float(np.linalg.norm(rhs)),partial_storage_statistics=registry.statistics,
        adopted_CSR_storage=csr_stats,all_factor_storage=factor_stats,
        before_limits=first_limits,after_limits=final_limits,
        observed_limit_differences=limits.difference(first_limits,final_limits),
        elapsed_seconds=time.monotonic()-started,
        maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        physical_RHS_or_partial_derivatives_reevaluated=False,
        full_1185_node_J_or_BVP_or_native_called=False,
        nonlinear_or_geometric_acceptance_claimed=False)
    (out/'comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    if not all(checks.values()):
        raise ArithmeticError('The complete QR/storage lifetime check failed: '+str(checks))
    event('actual_saved_complete_small_storage_comparison_returned',report=ref(out/'comparison.json'),
          all_checks_passed=True,complete_original_J_residual_maximum=report['complete_original_J_residual_maximum'])


if __name__=='__main__':
    main()
