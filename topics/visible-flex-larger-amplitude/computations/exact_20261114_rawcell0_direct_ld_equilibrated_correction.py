#!/usr/bin/env python3
"""New direct-LD/f64 Jacobian matrix: complete band solve and exact readback.

Consume actual28, actual41, and the completed explicit direct-LD result.
Only868 Jacobian blocks change; r/base/sigma/cut/far and504 blocks stay fixed.
This is the original-coordinate binary64 target, not a G shadow or an exact
flow derivative. No RHS/J/native/ODE/trial call is made by this consumer.
The complete577-node restriction still needs the original nonlinear trials.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import resource
import sys
import time
import traceback

import numpy as np
import scipy

HERE=Path(__file__).resolve().parent
ADAPTER_NAME='exact_20261114_rawcell0_direct_ld_system.py'
ADAPTER_SHA='43d633002ea1fde869b95767c0fd26619cd6b7385cbd040bf6c740c2432f5a2c'
EQUIL_NAME='geometry_20261114_native_equilibrated_band_correction.py'
EQUIL_SHA='8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3'
SCALING='direct-LD-f64-J1372-original-sigma-nearest-dyadic-row-column-max-entry-v1'


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as stream:
        for raw in iter(lambda:stream.read(1<<20),b''):h.update(raw)
    return h.hexdigest()


def load_pinned(name,digest):
    source=HERE/name
    if sha(source)!=digest:raise ValueError('The frozen independent helper changed: '+name)
    # Canonical import names remain importable by the spawn workers used in
    # the unchanged exact stage kernel; no nonimportable private alias is used.
    module=importlib.import_module(Path(name).stem)
    if Path(module.__file__).resolve()!=source.resolve():raise ValueError('Unexpected helper import path '+name)
    return module


def memory_contract(system,max_band_bytes,workers):
    """Actual dimensions and a declared allocation budget, not a science gate."""
    M,K,D=system.M,system.K,system.depth
    kl,ku=M,3*M-1;ldab=2*kl+ku+1;dimension=(D+1)*K
    band_bytes=ldab*dimension*8
    limits={}
    for name in ('/sys/fs/cgroup/memory.max','/sys/fs/cgroup/memory/memory.limit_in_bytes'):
        try:
            text=Path(name).read_text().strip()
            limits[name]=int(text) if text.isdecimal() else text
        except OSError:
            pass
    return dict(actual_depth=D,actual_nodes=D+1,full_dimension=dimension,
        modes=M,shape_dimension=K,band_rows=ldab,band_shape=[ldab,dimension],
        band_bytes=band_bytes,declared_maximum_single_band_bytes=max_band_bytes,
        band_with_possible_LAPACK_copy_bytes=2*band_bytes,
        only_one_band_intended_and_overwrite_requested=True,
        largest_new_stage_J_array_bytes=max(system.direct_arrays.arrays[n['shape_jacobians']]['total_bytes']
            for n in system.stage_arrays.values()),
        complete_new_J_virtual_bytes=D*K*K*8,
        whole_new_J_not_held_or_copied=True,
        actual_step_node_input_arrays_bytes=sum(a.nbytes for a in system._values.values()),
        maximum_pending_exact_stage_jobs=2*workers,
        raw_J_bytes_per_exact_stage=K*K*8,
        Python_exact_integer_and_BLAS_workspace_not_in_this_array_budget=True,
        cgroup_memory_limit_readout=limits,
        maximum_RSS_kib_before_band=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        budget_is_an_explicit_resource_limit_not_a_numerical_acceptance_threshold=True,
        no_row_mode_node_or_cusp_step_may_be_dropped_to_fit_budget=True,
        simultaneously_bound_parent_and_new_metadata_not_in_this_array_budget=True)


class ScopedWriter:
    """Annotate reused unscaled-equation utilities with the new matrix scope."""
    def __init__(self,B,system,producer):self.B=B;self.system=system;self.producer=producer
    def __getattr__(self,name):return getattr(self.B,name)
    def write(self,path,value,compressed=False):
        if isinstance(value,dict):
            value=dict(value,matrix_scope='actual41-base-direct-longdouble-rounded-shape-J1372-system',
                new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
                wrapper_producer_source_sha256=self.producer,
                unqualified_original_equations_mean_unscaled_current_step_system=True,
                norm_scope='All expanded rows use their explicit sigma; old-node sigma words are unchanged, the new all-row norm is not the old576 norm',
                original576_long_matrix_not_claimed_solved=True,
                original41_J1372_matrix_not_claimed_solved=True,
                target_J_is_the_new_direct_LD_rounded_original_coordinate_matrix=True)
        return self.B.write(path,value,compressed=compressed)


def checkpoint(B,output,system,delta,source_sha,name,restricted=False):
    rows=[dict(node=n,state=row.tolist(),negative_zero_columns=np.flatnonzero((row==0)&np.signbit(row)).tolist())
        for n,row in enumerate(delta)]
    schema=('complete-original-node-restriction-of-direct-LD-f64-J1372-direction-v1' if restricted
        else 'complete-native-direct-LD-f64-J1372-shooting-direction-v1')
    return B.write(output.directory/name,dict(schema=schema,source_sha256=source_sha,
        input_binding=system.binding,scaling=SCALING,M=system.M,K=system.K,depth=system.original_depth if restricted else system.depth,
        original_depth=system.original_depth,step_depth=system.depth,old_to_new=system.old_to_new,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(),rows=rows,
        produced_by_new_direct_LD_f64_J1372_matrix=True,solved_original576_long_matrix_claimed=False,
        solved_original41_J1372_matrix_claimed=False,
        restricted_to_original_nodes=restricted,original_nonlinear_readback_required=True,
        no_nonlinear_trial=True,native_accepted=False,task_completed=False),compressed=True)


def small_summary(report,result_descriptor):
    """Bounded original readouts; never recompute a norm or drop a solver row."""
    keys=('schema','source_sha256','direct_adapter_sha256','frozen_original_step_adapter_sha256',
        'equilibration_helper_sha256','exact_depth_independent_kernel_sha256','binding_helper_sha256',
        'original_capture_result_sha256','actual_step_result_sha256','actual_direct_result_sha256',
        'original1372_matrix_identity_sha256','new_matrix_identity_sha256','algorithm','matrix_scope','scaling',
        'diagnostic_completed','linear_direction_computed','native_accepted','task_completed',
        'original_native_calls','new_J_calls','new_ODE_steps','nonlinear_trials',
        'original1372_base_r_scales_cut_far_H_unchanged','target_is_new_original_coordinate_f64_J',
        'no_G_shadow_or_second_target','no_linear_exact_residual_threshold_added_to_original_nonlinear_acceptance',
        'original_full_nonlinear_readback_required','old_long_J_defect_is_diagnostic_not_gate',
        'requested_equilibration_passes','requested_refinement_steps','exact_workers','memory_budget',
        'lapack_factor_info','factorization_seconds','LU_shares_input_storage','LU_retains_input_pointer',
        'LU_Fortran_byte_sha256','lapack_solve_info','initial_solve','best_iteration',
        'best_exact_new_system_sigma_norm','refinement_stop_reason','step_delta','step_direction_checkpoint',
        'restricted_old_node_delta','restricted_direction_checkpoint','array_manifest','input_binding',
        'elapsed_seconds','maximum_RSS_kib','resource_limit_reached','actual_error','NumPy','SciPy','BLAS_threads')
    value={key:report[key] for key in keys if key in report}
    value['schema']='native-direct-LD-f64-J1372-equilibrated-small-summary-v1'
    value['full_result']=result_descriptor
    value['refinement_history']=[]
    for row in report.get('refinement_history',[]):
        full=row['exact_new_system_residual']
        item={key:row[key] for key in ('iteration','delta','step_direction_checkpoint',
            'strictly_improved_new_system_sigma_norm') if key in row}
        item['exact_new_system_residual']={key:full[key] for key in (
            'direction_float64le_sha256','exact_rows','completed_stages','original_product_positions',
            'exact_global_original_sigma_norm','exact_original_stored_base_sigma_norm',
            'exact_witness','all_exact_residual_rows','rounded_refinement_rhs') if key in full}
        if 'following_error_correction_solve' in row:
            item['following_error_correction_solve']=row['following_error_correction_solve']
        value['refinement_history'].append(item)
    value['scope']='Exact new finite1372 rows at unchanged original sigma; no claim of old J, exact DF, or nonlinear acceptance.'
    # This transport check cannot turn a completed numerical solve into a
    # failure. Preserve its full result and publish a minimal receipt if a
    # future diagnostic expansion makes this selected summary too large.
    raw=(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode()
    if len(raw)>=95000:
        value={key:report[key] for key in ('diagnostic_completed','linear_direction_computed',
            'new_matrix_identity_sha256','best_iteration','best_exact_new_system_sigma_norm',
            'elapsed_seconds','maximum_RSS_kib','actual_error') if key in report}
        value.update(schema='native-direct-LD-f64-J1372-equilibrated-small-summary-v1',
            full_result=result_descriptor,full_selected_summary_bytes=len(raw),
            compact_fallback_used=True,native_accepted=False,task_completed=False,
            complete_scientific_result_is_preserved=True)
    return value


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('RawCell0 step finite-system computation belongs only to public repository Actions')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture-directory',type=Path,required=True)
    parser.add_argument('--step-directory',type=Path,required=True)
    parser.add_argument('--step-result-sha256',required=True)
    parser.add_argument('--direct-directory',type=Path,required=True)
    parser.add_argument('--direct-result-sha256',required=True)
    parser.add_argument('--equilibration-passes',type=int,default=3)
    parser.add_argument('--refinement-steps',type=int,default=3)
    parser.add_argument('--exact-workers',type=int,default=2)
    parser.add_argument('--max-band-bytes',type=int,default=4*1024**3)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    if (not 0<=a.equilibration_passes<=8 or not 0<=a.refinement_steps<=8
            or not 1<=a.exact_workers<=4 or a.max_band_bytes<=0):
        raise ValueError('Use explicit bounded equilibration, refinement, and worker budgets')
    a.out=a.out.resolve()
    if (a.out.exists() or a.out.is_relative_to(a.capture_directory.resolve())
            or a.out.is_relative_to(a.step_directory.resolve())
            or a.out.is_relative_to(a.direct_directory.resolve())):
        raise ValueError('Use a new independent output directory')
    a.out.mkdir(parents=True);started=time.monotonic();output=None
    Q=load_pinned(EQUIL_NAME,EQUIL_SHA);S=load_pinned(ADAPTER_NAME,ADAPTER_SHA);B=S.load_binding()
    kernel=Q.exact_module();source_sha=sha(__file__)
    report=dict(schema='native-rawcell0-direct-LD-f64-J1372-equilibrated-band-correction-v1',source_sha256=source_sha,
        direct_adapter_sha256=ADAPTER_SHA,equilibration_helper_sha256=EQUIL_SHA,
        frozen_original_step_adapter_sha256=S.STEP_SHA,
        exact_depth_independent_kernel_sha256=Q.EXACT_SHA,binding_helper_sha256=S.BAND_SHA,
        original_capture_result_sha256=S.CAPTURE_SHA,actual_step_result_sha256=a.step_result_sha256,
        actual_direct_result_sha256=a.direct_result_sha256,
        original1372_matrix_identity_sha256=S.PARENT_MATRIX_SHA,
        original1372_base_r_scales_cut_far_H_unchanged=True,
        target_is_new_original_coordinate_f64_J=True,
        no_G_shadow_or_second_target=True,
        no_linear_exact_residual_threshold_added_to_original_nonlinear_acceptance=True,
        algorithm='new-direct-LD-f64-J1372-dyadic-equilibration-and-exact-residual-refinement-v1',
        matrix_scope='actual41-base-direct-longdouble-rounded-shape-J1372-system',scaling=SCALING,
        diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        original_native_calls=0,new_J_calls=0,new_ODE_steps=0,nonlinear_trials=0,
        original_cut_far_H_and_old_node_sigma_unchanged=True,
        original576_long_matrix_not_claimed_solved=True,old_long_J_defect_is_diagnostic_not_gate=True,
        original_full_nonlinear_readback_required=True,
        requested_equilibration_passes=a.equilibration_passes,requested_refinement_steps=a.refinement_steps,
        declared_maximum_single_band_bytes=a.max_band_bytes,
        exact_workers=a.exact_workers,refinement_history=[],NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')})
    try:
        system=S.RawCell0DirectLDSystem(a.capture_directory,a.step_directory,a.step_result_sha256,
            a.direct_directory,a.direct_result_sha256,B)
        report['new_matrix_identity_sha256']=system.binding['new_matrix_identity_sha256']
        report['input_binding']=B.write(a.out/'input-binding.json.gz',system.binding,compressed=True)
        output=B.OutputArrays(a.out)
        report['bound_new_system_arrays']=system.export_inputs(output)
        B.write(a.out/'new-system-array-identities.json',dict(new_matrix_identity_sha256=report['new_matrix_identity_sha256'],
            arrays=system.arrays,complete_stage_blocks=system.J_rows,
            complete_large_J_is_a_virtual_stream_not_a_duplicated_array=True))
        E=S.DynamicExactContext(system,kernel);W=ScopedWriter(B,system,source_sha)
        M,K,D=system.M,system.K,system.depth
        report['memory_budget']=memory_contract(system,a.max_band_bytes,a.exact_workers)
        W.write(a.out/'actual-memory-budget.json',report['memory_budget'])
        if report['memory_budget']['band_bytes']>a.max_band_bytes:
            report['resource_limit_reached']=True
            raise MemoryError('The complete actual step-system band exceeds the explicitly declared byte budget; no system is truncated')
        rows,columns,equilibration=Q.choose_exponents(system,E,output,W,a.out,a.equilibration_passes)
        report['equilibration']=dict(equilibration,matrix_scope='actual41-base-direct-longdouble-rounded-shape-J1372-system')
        ab,kl,ku=Q.assemble(system,rows,columns,output,W,report)
        evaluator=Q.ExactOriginalResidual(system,E,W,output,rows,a.exact_workers)
        initial_rhs,initial_rounding=evaluator.initial_rhs();report['initial_rhs_rounding']=initial_rounding
        output.save('complete-step-scaled-rhs',initial_rhs,'Negative actual step-system finite residual with final dyadic row scale')
        W.write(a.out/'assembled-model.json',report)
        before=time.monotonic();pointer=ab.__array_interface__['data'][0]
        lu,piv,info=Q.dgbtrf(ab,kl,ku,overwrite_ab=1)
        report.update(lapack_factor_info=int(info),factorization_seconds=time.monotonic()-before,
            LU_shares_input_storage=bool(np.shares_memory(lu,ab)),
            LU_retains_input_pointer=pointer==lu.__array_interface__['data'][0],
            LU_Fortran_byte_sha256=hashlib.sha256(memoryview(lu.ravel(order='F')).cast('B')).hexdigest())
        report['memory_budget']['actual_LU_shares_input_storage']=report['LU_shares_input_storage']
        report['memory_budget']['actual_LU_bytes']=int(lu.nbytes)
        report['memory_budget']['maximum_RSS_kib_after_factorization']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # The unfactored byte identity was already recorded by assemble.
        # Retain only the returned LU when LAPACK made an actual copy.
        del ab
        report['pivot_array']=Q.save_integer(output,'lapack-pivots',piv,'Actual complete step-system factorization pivot vector')
        W.write(a.out/'factorization.json',report)
        if info<0:raise RuntimeError('dgbtrf rejected argument '+str(-info))
        if info>0:raise FloatingPointError('dgbtrf returned zero pivot '+str(info))

        def solve_rhs(rhs,label):
            before=time.monotonic();column=np.array(rhs[:,None],dtype=np.float64,order='F',copy=True)
            solution,info=Q.dgbtrs(lu,kl,ku,column,piv,overwrite_b=1)
            detail=dict(label=label,lapack_solve_info=int(info),seconds=time.monotonic()-before)
            if info:raise RuntimeError('dgbtrs returned info='+str(info))
            if not np.isfinite(solution).all():raise FloatingPointError('Nonfinite complete step direction '+label)
            z=solution[:,0];ledger=Q.ScalingLedger()
            recovered=ledger.apply(z,columns,dict(kind='restore-unscaled-actual-step-coordinates',label=label)).reshape(D+1,K)
            detail['new_coordinate_recovery']=ledger.report()
            output.save(label+'-scaled-step-coordinate-delta',z.reshape(D+1,K),
                'All actual new-node scaled coordinates before powers-of-two recovery')
            return recovered,detail

        delta,detail=solve_rhs(initial_rhs,'initial')
        report['lapack_solve_info']=detail['lapack_solve_info'];report['initial_solve']=detail
        best=best_rhs=best_exact=best_iteration=None
        for iteration in range(a.refinement_steps+1):
            descriptor=output.save(f'iteration-{iteration:02d}-step-coordinate-delta',delta,
                'All original-coordinate new1372 unscaled coordinates; newly formed f64 Jacobian matrix')
            state=checkpoint(B,output,system,delta,source_sha,f'step-direction-iteration-{iteration:02d}.json.gz')
            rhs,exact,residual_report=evaluator.evaluate(delta,iteration)
            improved=best is None or Q.exact_smaller(exact,best_exact)
            history=dict(iteration=iteration,delta=descriptor,step_direction_checkpoint=state,
                exact_new_system_residual=residual_report,strictly_improved_new_system_sigma_norm=improved)
            report['refinement_history'].append(history)
            W.write(a.out/f'step-iteration-{iteration:02d}.json',history)
            if not improved:
                report['refinement_stop_reason']='Exact new-system sigma norm did not strictly improve; retain previous complete direction'
                break
            best=delta.copy();best_rhs=rhs;best_exact=exact;best_iteration=iteration
            if exact['_integer']==0:
                report['refinement_stop_reason']='All saved new finite linear residuals are exactly zero; no nonlinear acceptance asserted'
                break
            if iteration==a.refinement_steps:
                report['refinement_stop_reason']='Explicit finite refinement budget exhausted'
                break
            correction,detail=solve_rhs(best_rhs,f'refinement-{iteration+1:02d}')
            history['following_error_correction_solve']=detail
            output.save(f'refinement-{iteration+1:02d}-step-coordinate-increment',correction,
                'Complete new-system solution of the correctly rounded negative exact residual')
            with np.errstate(over='ignore',under='ignore',invalid='ignore'):candidate=best+correction
            if not np.isfinite(candidate).all():
                history['following_nonfinite_candidate']=output.save(f'iteration-{iteration+1:02d}-nonfinite-step-candidate',candidate,
                    'Actual finite-arithmetic update preserved; previous finite direction remains selected')
                report['refinement_stop_reason']='Binary64 error correction became nonfinite; previous finite direction retained'
                break
            if B.float_bytes(candidate)==B.float_bytes(best):
                report['refinement_stop_reason']='Full proposed binary64 update is byte-identical to the retained direction'
                break
            delta=candidate
        if best is None:raise RuntimeError('No complete finite new-system direction was retained')
        report['best_iteration']=best_iteration
        report['best_exact_new_system_sigma_norm']=kernel.public_record(best_exact)
        report['step_delta']=output.save('complete-step-coordinate-delta',best,
            'All actual new-node best direction selected by the new matrix residual; no native acceptance')
        report['step_direction_checkpoint']=checkpoint(B,output,system,best,source_sha,'step-direction-checkpoint.json.gz')
        restricted=np.array(best[np.asarray(system.old_to_new)],copy=True)
        report['restricted_old_node_delta']=output.save('complete-old-node-restricted-delta',restricted,
            'Only old577-node entries of the actual step-system direction; not a solution claim for old576 A')
        report['restricted_direction_checkpoint']=checkpoint(B,output,system,restricted,source_sha,
            'restricted-original-node-direction.json.gz',restricted=True)
        report['linear_direction_computed']=True
        report['new_system_floating_defects']=B.evaluate_directions(system,{'rawcell0_steps':best},
            system.all('stage-residuals'),system.all('cut-residual').reshape(-1),system.all('end-residual').reshape(-1),
            system.all('original-scales').reshape(-1),system.all('original-far-graph').reshape(-1),output,'new-actual-step-system')
        # The old long matrix remains a diagnostic. Its magnitude does not
        # reject this newly represented direction or replace a nonlinear trial.
        original=system.original;residuals=original.all('stage-residuals')
        cut=original.all('cut-residual').reshape(-1);far=original.all('end-residual').reshape(-1)
        scales=original.all('original-scales').reshape(-1);far_graph=original.all('original-far-graph').reshape(-1)
        old_diagnostic=B.evaluate_directions(original,{'restricted_from_steps':restricted},
            residuals,cut,far,scales,far_graph,output,'old576-diagnostic')
        report['old_long_matrix_diagnostic']=dict(reports=old_diagnostic,
            used_to_select_or_reject_direction=False,used_as_nonlinear_gate=False,
            full_original_nonlinear_evaluate_trial_not_run=True)
        site,entry=B.select_report_worst(old_diagnostic['restricted_from_steps'])
        report['old_long_matrix_exact_single_row_diagnostic']=B.exact_row(original,restricted,
            residuals,cut,far,scales,far_graph,site,B.stored_scalar(entry),output,'old576-exact-diagnostic-row')
        report['diagnostic_completed']=True
    except Exception as error:
        report['actual_error']=repr(error)
        report['actual_traceback']=traceback.format_exc()
    finally:
        if output is not None:
            report['array_manifest']=B.write(a.out/'output-array-manifest.json',dict(
                schema='native-direct-LD-f64-J1372-shooting-direction-arrays-v1',source_sha256=source_sha,
                new_matrix_identity_sha256=report.get('new_matrix_identity_sha256'),
                original_capture_result_sha256=S.CAPTURE_SHA,actual_step_result_sha256=a.step_result_sha256,
                actual_direct_result_sha256=a.direct_result_sha256,
                arrays=output.entries,all_arrays_artifact_only=True,native_accepted=False,task_completed=False))
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        result_descriptor=B.write(a.out/'result.json.gz',report,compressed=True)
        B.write(a.out/'summary.json',small_summary(report,result_descriptor))
    print(json.dumps(dict(event='native_direct_LD_f64_J1372_equilibrated_band_finished',diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],native_accepted=False,task_completed=False)),flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':raise SystemExit(main())
