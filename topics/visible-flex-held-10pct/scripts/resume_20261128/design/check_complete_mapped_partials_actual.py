#!/usr/bin/env python3
"""Check new storage on one small complete Jacobian from a genuine saved state.

Select 17 actual nodes, including both physical endpoints, from the declared
full unaccepted field. Recompute its original collocation midpoint states,
all original nodal/midpoint partial columns and complete boundary rows. The
old and disk-backed batches use the same original eight-node calls. Compare
all partial bytes/strides, the original middle-dP side effect, every stored
CSR entry/index, and the same complete QR direction and diagnostics. This is
an implementation check on a coarser diagnostic grid, never a BVP result.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import gc
import hashlib
import inspect
import json
from pathlib import Path
import resource
import shutil
import sys
import time
import weakref

import numpy as np
from scipy.integrate import _bvp

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE),str(HERE.parent),str(HERE.parent/'analytic')]
import check_unaccepted_design_delta_nodes_v2 as builder
import exception_safe_radial_batches as original_batches
import complete_mapped_jacobian_partials as partial_storage
import direct_csr_collocation as original_assembly
import complete_streamed_csr_assembly as mapped_assembly
import material_core_evaluate_cache as memo
import analytic_delta_jac_adapter as delta
import block_qr_v2 as qr
import actual_process_memory_limits as limits

EXPECTED_ASSEMBLY = '242d00c55b68083611e49eabef7ec86c8a4f5128254a03b26e8a0c3121beaca3'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def identical(left,right):
    return (left.dtype==right.dtype and left.shape==right.shape
            and left.tobytes(order='C')==right.tobytes(order='C'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--source-run',type=Path,required=True)
    parser.add_argument('--checkpoint-metadata',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    args = parser.parse_args()
    if sha(mapped_assembly.__file__) != EXPECTED_ASSEMBLY:
        raise ValueError('The reviewed direct mapped complete assembler changed')
    repo,out = args.repo.resolve(),args.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Keep the actual diagnostic arrays outside the source tree')
    record = json.loads(args.source_run.read_text())
    metadata = json.loads(args.checkpoint_metadata.read_text())
    source = (args.checkpoint_metadata.parent/metadata['file']).resolve()
    if (metadata.get('kind')!='unaccepted_complete_nodal_restart'
            or metadata.get('accepted_bvp') is not False
            or metadata.get('before_full_J_assembly') is not True
            or sha(source)!=metadata['sha256']):
        raise ValueError('Require the genuine complete unaccepted nodal source')
    for group in (record['source_hashes'],record['inputs'],metadata['original_source_hashes']):
        for path,expected in group.items():
            if sha(path)!=expected:
                raise ValueError('The original source or complete input changed: '+path)
    with np.load(source,allow_pickle=False) as saved:
        full_x,full_y,p,scales = (saved[key].copy() for key in ('x','y','p','pscale'))
    if (full_y.shape!=(3*record['modes']+1,len(full_x))
            or p.shape!=(record['modes'],)
            or not np.array_equal(scales,np.asarray(record['parameter_scales']))
            or full_x[0]!=0 or full_x[-1]!=1 or not np.all(np.diff(full_x)>0)):
        raise ValueError('The complete original state or parameter coordinates differ')
    if shutil.disk_usage(out.parent).free < 640*2**20:
        raise MemoryError('The small actual storage check requires its explicit scratch margin')
    out.mkdir(parents=True,exist_ok=False)
    started = time.monotonic()
    initial_limits = limits.snapshot()
    events = out/'events.jsonl'

    def event(kind,**fields):
        row = dict(event=kind,elapsed_seconds=time.monotonic()-started,
            maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**fields)
        with events.open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)

    inputs = dict(source_run=ref(args.source_run),checkpoint_metadata=ref(args.checkpoint_metadata),
                  complete_unaccepted_field=ref(source))
    sources = {str(Path(module.__file__).resolve()):sha(module.__file__) for module in
        (sys.modules[__name__],builder,original_batches,partial_storage,original_assembly,
         mapped_assembly,memo,delta,qr,limits)}
    event('real_small_storage_check_started',inputs=inputs,source_hashes=sources,
          complete_BVP_or_accepted_field_claimed=False)
    obj,table_stats,branch = builder.build_original_model(record,repo)
    if branch['live_V5_delta_install_called'] is not True or not np.array_equal(obj.pscale,scales):
        raise ValueError('This check must use the real positive-lambda V5 parameter branch')
    core_class = sys.modules['portable_m3_custom_core'].MaterialFlattenedSupportCore
    memo_stats = memo.install(core_class)
    delta_stats = delta.install(type(obj))
    obj.initial(p)
    selected = np.unique(np.rint(np.linspace(0,len(full_x)-1,17)).astype(int))
    x,y = full_x[selected].copy(),full_y[:,selected].copy()
    n,m,k = y.shape[0],len(x),len(p)
    if m!=17 or x[0]!=0 or x[-1]!=1:
        raise ValueError('The declared actual endpoint-preserving grid differs')
    h = np.diff(x)
    fun = original_batches.split_rhs(obj.fun,8)
    col,ym,f,fm = _bvp.collocation_fun(fun,y,p,x,h)
    bc = obj.bc(y[:,0],y[:,-1],p)
    rhs = np.r_[col.ravel(order='F'),bc]
    old_stats = original_batches.statistics()
    old_jac = original_batches.split_jac(obj.fun_jac,8,old_stats)
    old_dy,old_dp = old_jac(x,y,p)
    old_dym,old_dpm = old_jac(x[:-1]+h/2,ym,p)
    bca,bcb,bcp = obj.bc_jac(y[:,0],y[:,-1],p)
    original_middle = old_dpm.copy(order='C')
    event('original_small_complete_partials_returned',nodes=m,n=n,k=k,
          source_node_indices=selected.tolist(),original_calls=old_stats)
    registry = partial_storage.CompletePartialRegistry(out,entry_sha256=sha(__file__))
    new_stats = original_batches.statistics()
    new_jac = registry.make_split_jac()(obj.fun_jac,8,new_stats)
    new_dy,new_dp = new_jac(x,y,p)
    new_dym,new_dpm = new_jac(x[:-1]+h/2,ym,p)
    checks = {}
    for name,left,right in (('node_dy',old_dy,new_dy),('node_dp',old_dp,new_dp),
                            ('middle_dy',old_dym,new_dym),('middle_dp',old_dpm,new_dpm)):
        checks[name+'_all_bytes_identical'] = identical(left,right)
        checks[name+'_shape_dtype_strides_identical'] = (
            left.shape==right.shape and left.dtype==right.dtype and left.strides==right.strides)
        checks[name+'_writable_C_order_memmap'] = (
            isinstance(right,np.memmap) and right.flags.c_contiguous and right.flags.writeable)
    del left,right
    for key in ('jacobian_calls','jacobian_blocks'):
        checks['original_'+key+'_unchanged'] = old_stats[key]==new_stats[key]
    if not all(checks.values()):
        raise ArithmeticError('The actual complete original partial tensors differ: '+str(checks))
    scipy_middle = original_middle.copy(order='C')
    row_indices,column_indices = _bvp.compute_jac_indices(n,m,k)
    scipy_matrix = _bvp.construct_global_jac(n,m,k,row_indices,column_indices,h,
        old_dy,old_dym,old_dp,scipy_middle,bca,bcb,bcp).tocsr()
    old_matrix = original_assembly.construct(n,m,k,None,None,h,old_dy,old_dym,
        old_dp,old_dpm,bca,bcb,bcp,radial_block=16)
    root = mapped_assembly.owned_storage_root(out)
    mapped_rows = []
    new_matrix = mapped_assembly.construct(n,m,k,None,None,h,new_dy,new_dym,
        new_dp,new_dpm,bca,bcb,bcp,storage_directory=root,radial_block=3,
        release_inputs=registry.release_inputs,record=mapped_rows.append)
    for name in ('data','indices','indptr'):
        checks['complete_CSR_'+name+'_all_bytes_identical'] = identical(
            getattr(old_matrix,name),getattr(new_matrix,name))
        checks['original_SciPy_CSR_'+name+'_all_bytes_identical'] = identical(
            getattr(scipy_matrix,name),getattr(new_matrix,name))
    checks['original_middle_dp_side_effect_identical'] = identical(old_dpm,new_dpm)
    checks['original_SciPy_middle_dp_side_effect_identical'] = identical(scipy_middle,new_dpm)
    checks['original_middle_dp_side_effect_nonzero'] = not identical(original_middle,old_dpm)
    checks['complete_CSR_shape_identical'] = old_matrix.shape==new_matrix.shape
    checks['complete_stored_zero_count_identical'] = (
        np.count_nonzero(old_matrix.data==0)==np.count_nonzero(new_matrix.data==0))
    checks['complete_original_endpoint_rows_identical'] = identical(
        old_matrix[-(n+k):].toarray(),new_matrix[-(n+k):].toarray())
    if not all(checks.values()):
        raise ArithmeticError('The original complete CSR or parameter side effect differs: '+str(checks))
    # Keep only a small diagnostic, never a restart or accepted source.
    np.savez_compressed(out/'real-selected-original-system.npz',source_indices=selected,
        x=x,y=y,p=p,h=h,ym=ym,rhs=rhs,bca=bca,bcb=bcb,bcp=bcp,
        dy=old_dy,dym=old_dym,dp=old_dp,dpm_before_original_update=original_middle)
    event('all_actual_partial_and_complete_CSR_bytes_identical',checks=checks,
          complete_unknowns=n*m+k,stored_entries=len(old_matrix.data))
    del old_dy,old_dym,old_dp,old_dpm,new_dy,new_dym,new_dp,new_dpm,original_middle
    del scipy_middle,scipy_matrix,row_indices,column_indices
    gc.collect()
    checks['all_partial_pairs_released_before_QR'] = not registry.stores
    checks['all_partial_backing_directories_removed_before_QR'] = not list(
        registry.directory.glob('complete-partials-*'))
    if registry.stores:
        raise RuntimeError('A full original partial pair was retained after its caller released it')
    factor_directory = out/'mapped-factor-storage'
    factor_directory.mkdir()
    original_factor = qr.BlockQR(old_matrix,n,m,k)
    original_answer = original_factor.solve(rhs)
    reference_stats = dict(original_factor.stats)
    mapped_factor = mapped_assembly.AdoptedBeforeQRMappedBlockQR(new_matrix,n,m,k,
        storage_directory=factor_directory)
    mapped_answer = mapped_factor.solve(rhs)
    checks['same_complete_original_CSR_object_adopted'] = mapped_factor.matrix is new_matrix
    checks['complete_original_QR_direction_bitwise_identical'] = identical(original_answer,mapped_answer)
    checks['all_original_QR_diagnostics_identical'] = reference_stats==mapped_factor.stats
    for name in ('data','indices','indptr'):
        checks['after_original_prune_CSR_'+name+'_all_bytes_identical'] = identical(
            getattr(old_matrix,name),getattr(new_matrix,name))
    for label,store in (('CSR',mapped_factor._complete_csr_store),('factor',mapped_factor._complete_store)):
        checks[label+'_complete_page_release_returned'] = store.stats.get(
            'last_solve_page_release',{}).get('clean_mapped_pages_advised_DONTNEED') is True
    checks['no_second_CSR_backing_created'] = mapped_factor._complete_csr_store.stats[
        'second_complete_CSR_copy_created'] is False
    final_residual = old_matrix@mapped_answer-rhs
    factor_stats = dict(mapped_factor.stats)
    csr_storage_stats = dict(mapped_factor._complete_csr_store.stats)
    factor_storage_stats = dict(mapped_factor._complete_store.stats)
    assembly_storage_path = Path(mapped_factor._complete_csr_store.directory)
    factor_storage_path = Path(mapped_factor._complete_store.directory)
    matrix_ref,factor_ref = weakref.ref(new_matrix),weakref.ref(mapped_factor)
    del mapped_factor,new_matrix,original_factor,store
    gc.collect()
    checks['original_complete_factor_and_matrix_released'] = matrix_ref() is None and factor_ref() is None
    checks['owned_CSR_and_factor_backing_released'] = (
        not assembly_storage_path.exists() and not factor_storage_path.exists())
    final_limits = limits.snapshot()
    report = dict(status='actual_small_complete_storage_comparison_returned',scope=__doc__,
        inputs=inputs,source_hashes=sources,source_node_indices=selected.tolist(),
        original_full_source_nodes=len(full_x),selected_nodes=m,state_components=n,parameters=k,
        original_actual_positive_lambda=record['core_settings']['homotopy'],
        unchanged_original_gates=record['gates'],original_batch=8,
        original_direct_assembly_block=16,new_direct_mapped_assembly_block=3,
        diagnostic_grid_not_original_full_BVP_mesh=True,
        complete_unknowns=n*m+k,all_checks=checks,original_QR_stats=factor_stats,
        original_full_J_residual_maximum=float(np.max(np.abs(final_residual))),
        original_full_J_residual_l2=float(np.linalg.norm(final_residual)),
        original_rhs_l2=float(np.linalg.norm(rhs)),original_partial_batches=old_stats,
        mapped_partial_batches=new_stats,mapped_partial_storage=registry.statistics,
        original_complete_assembly=mapped_rows,adopted_CSR_storage=csr_storage_stats,
        all_factor_storage=factor_storage_stats,core_cache=memo_stats,
        Fourier_table_cache=table_stats,complete_delta_adapter=delta_stats,
        selected_original_system=ref(out/'real-selected-original-system.npz'),
        original_branch=branch,original_stacked_matmul_source_sha256=hashlib.sha256(
            inspect.getsource(_bvp.stacked_matmul).encode()).hexdigest(),
        before_limits=initial_limits,after_limits=final_limits,
        observed_limit_differences=limits.difference(initial_limits,final_limits),
        elapsed_seconds=time.monotonic()-started,
        maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        full_original_1185_node_J_or_BVP_executed=False,
        nonlinear_or_geometric_acceptance_claimed=False)
    (out/'comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    if not all(checks.values()):
        raise ArithmeticError('An exact original storage/lifecycle check failed: '+str(checks))
    event('actual_small_complete_storage_comparison_returned',report=ref(out/'comparison.json'),
        all_checks_passed=True,elapsed_seconds=report['elapsed_seconds'],
        original_full_J_residual_maximum=report['original_full_J_residual_maximum'])


if __name__=='__main__':
    main()
