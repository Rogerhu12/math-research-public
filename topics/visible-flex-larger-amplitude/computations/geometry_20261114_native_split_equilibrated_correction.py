#!/usr/bin/env python3
"""New578-stage short-block representation: bounded band solve and refinement.

Consume actual28 plus an explicitly pinned completed four-short-block probe.
No J/native/ODE/trial call is made. The old577-node restriction is separately
identified and still requires the original full nonlinear evaluate/trial. Its
defect against the old long-J matrix is recorded only as a diagnostic.
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

import numpy as np
import scipy

HERE=Path(__file__).resolve().parent
ADAPTER_NAME='geometry_20261114_native_split_captured_system.py'
ADAPTER_SHA='e88e69da3bf5dfea792515f544bfb03ca9e00f907bf5904c2f856e203d4ea451'
EQUIL_NAME='geometry_20261114_native_equilibrated_band_correction.py'
EQUIL_SHA='8f5cb5da0826e3deedf935eca2e62b91c6628861804b2e66c6f853e9459e1dd3'
SCALING='explicit-split-node-sigma-nearest-dyadic-then-row-column-max-entry-v1'


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


class ScopedWriter:
    """Annotate reused unscaled-equation utilities with the new matrix scope."""
    def __init__(self,B,system,producer):self.B=B;self.system=system;self.producer=producer
    def __getattr__(self,name):return getattr(self.B,name)
    def write(self,path,value,compressed=False):
        if isinstance(value,dict):
            value=dict(value,matrix_scope='explicit-new578-stage-same-schedule-linear-system',
                new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
                wrapper_producer_source_sha256=self.producer,
                unqualified_original_equations_mean_unscaled_current_578_system=True,
                original576_long_matrix_not_claimed_solved=True)
        return self.B.write(path,value,compressed=compressed)


def checkpoint(B,output,system,delta,source_sha,name,restricted=False):
    rows=[dict(node=n,state=row.tolist(),negative_zero_columns=np.flatnonzero((row==0)&np.signbit(row)).tolist())
        for n,row in enumerate(delta)]
    schema=('complete-original-node-restriction-of-split-direction-v1' if restricted
        else 'complete-native-split-shooting-direction-v1')
    return B.write(output.directory/name,dict(schema=schema,source_sha256=source_sha,
        input_binding=system.binding,scaling=SCALING,M=112,K=224,depth=576 if restricted else 578,
        original_depth=576,split_depth=578,old_to_new=system.old_to_new,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(),rows=rows,
        produced_by_new578_matrix=True,solved_original576_long_matrix_claimed=False,
        restricted_to_original_nodes=restricted,original_nonlinear_readback_required=True,
        no_nonlinear_trial=True,native_accepted=False,task_completed=False),compressed=True)


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Split native finite-system computation belongs only to public repository Actions')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capture-directory',type=Path,required=True)
    parser.add_argument('--split-directory',type=Path,required=True)
    parser.add_argument('--split-result-sha256',required=True)
    parser.add_argument('--equilibration-passes',type=int,default=3)
    parser.add_argument('--refinement-steps',type=int,default=3)
    parser.add_argument('--exact-workers',type=int,default=2)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    if not 0<=a.equilibration_passes<=8 or not 0<=a.refinement_steps<=8 or not 1<=a.exact_workers<=4:
        raise ValueError('Use explicit bounded equilibration, refinement, and worker budgets')
    a.out=a.out.resolve()
    if (a.out.exists() or a.out.is_relative_to(a.capture_directory.resolve())
            or a.out.is_relative_to(a.split_directory.resolve())):
        raise ValueError('Use a new independent output directory')
    a.out.mkdir(parents=True);started=time.monotonic();output=None
    Q=load_pinned(EQUIL_NAME,EQUIL_SHA);S=load_pinned(ADAPTER_NAME,ADAPTER_SHA);B=S.load_binding()
    kernel=Q.exact_module();source_sha=sha(__file__)
    report=dict(schema='native-split-shooting-equilibrated-band-correction-v1',source_sha256=source_sha,
        split_adapter_sha256=ADAPTER_SHA,equilibration_helper_sha256=EQUIL_SHA,
        exact_depth_independent_kernel_sha256=Q.EXACT_SHA,binding_helper_sha256=S.BAND_SHA,
        original_capture_result_sha256=S.CAPTURE_SHA,actual_split_result_sha256=a.split_result_sha256,
        algorithm='new578-short-block-matrix-dyadic-equilibration-and-exact-residual-refinement-v1',
        matrix_scope='explicit-new578-stage-system',scaling=SCALING,
        diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        original_native_calls=0,new_J_calls=0,new_ODE_steps=0,nonlinear_trials=0,
        original_cut_far_H_and_old_node_sigma_unchanged=True,
        original576_long_matrix_not_claimed_solved=True,old_long_J_defect_is_diagnostic_not_gate=True,
        original_full_nonlinear_readback_required=True,
        requested_equilibration_passes=a.equilibration_passes,requested_refinement_steps=a.refinement_steps,
        exact_workers=a.exact_workers,refinement_history=[],NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')})
    try:
        system=S.SplitCapturedSystem(a.capture_directory,a.split_directory,a.split_result_sha256,B)
        report['new_matrix_identity_sha256']=system.binding['new_matrix_identity_sha256']
        B.write(a.out/'input-binding.json',system.binding);output=B.OutputArrays(a.out)
        report['bound_new_system_arrays']=system.export_inputs(output)
        B.write(a.out/'new-system-array-identities.json',dict(new_matrix_identity_sha256=report['new_matrix_identity_sha256'],
            arrays=system.arrays,complete_stage_blocks=system.J_rows,
            complete_large_J_is_a_virtual_stream_not_a_duplicated_array=True))
        E=S.DynamicExactContext(system,kernel);W=ScopedWriter(B,system,source_sha)
        M,K,D=system.M,system.K,system.depth
        rows,columns,equilibration=Q.choose_exponents(system,E,output,W,a.out,a.equilibration_passes)
        report['equilibration']=dict(equilibration,matrix_scope='explicit-new578-stage-system')
        ab,kl,ku=Q.assemble(system,rows,columns,output,W,report)
        evaluator=Q.ExactOriginalResidual(system,E,W,output,rows,a.exact_workers)
        initial_rhs,initial_rounding=evaluator.initial_rhs();report['initial_rhs_rounding']=initial_rounding
        output.save('complete-split-scaled-rhs',initial_rhs,'Negative new578 finite residual with final dyadic row scale')
        W.write(a.out/'assembled-model.json',report)
        before=time.monotonic();pointer=ab.__array_interface__['data'][0]
        lu,piv,info=Q.dgbtrf(ab,kl,ku,overwrite_ab=1)
        report.update(lapack_factor_info=int(info),factorization_seconds=time.monotonic()-before,
            LU_shares_input_storage=bool(np.shares_memory(lu,ab)),
            LU_retains_input_pointer=pointer==lu.__array_interface__['data'][0],
            LU_Fortran_byte_sha256=hashlib.sha256(memoryview(lu.ravel(order='F')).cast('B')).hexdigest())
        report['pivot_array']=Q.save_integer(output,'lapack-pivots',piv,'Actual new578 factorization pivot vector')
        W.write(a.out/'factorization.json',report)
        if info<0:raise RuntimeError('dgbtrf rejected argument '+str(-info))
        if info>0:raise FloatingPointError('dgbtrf returned zero pivot '+str(info))

        def solve_rhs(rhs,label):
            before=time.monotonic();column=np.array(rhs[:,None],dtype=np.float64,order='F',copy=True)
            solution,info=Q.dgbtrs(lu,kl,ku,column,piv,overwrite_b=1)
            detail=dict(label=label,lapack_solve_info=int(info),seconds=time.monotonic()-before)
            if info:raise RuntimeError('dgbtrs returned info='+str(info))
            if not np.isfinite(solution).all():raise FloatingPointError('Nonfinite complete split direction '+label)
            z=solution[:,0];ledger=Q.ScalingLedger()
            recovered=ledger.apply(z,columns,dict(kind='restore-unscaled-new578-coordinates',label=label)).reshape(D+1,K)
            detail['new_coordinate_recovery']=ledger.report()
            output.save(label+'-scaled-split-coordinate-delta',z.reshape(D+1,K),
                'All579-node scaled coordinates before powers-of-two recovery')
            return recovered,detail

        delta,detail=solve_rhs(initial_rhs,'initial')
        report['lapack_solve_info']=detail['lapack_solve_info'];report['initial_solve']=detail
        best=best_rhs=best_exact=best_iteration=None
        for iteration in range(a.refinement_steps+1):
            descriptor=output.save(f'iteration-{iteration:02d}-split-coordinate-delta',delta,
                'All579-node unscaled coordinates; independently identified new finite matrix')
            state=checkpoint(B,output,system,delta,source_sha,f'split-direction-iteration-{iteration:02d}.json.gz')
            rhs,exact,residual_report=evaluator.evaluate(delta,iteration)
            improved=best is None or Q.exact_smaller(exact,best_exact)
            history=dict(iteration=iteration,delta=descriptor,split_direction_checkpoint=state,
                exact_new_system_residual=residual_report,strictly_improved_new_system_sigma_norm=improved)
            report['refinement_history'].append(history)
            W.write(a.out/f'split-iteration-{iteration:02d}.json',history)
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
            output.save(f'refinement-{iteration+1:02d}-split-coordinate-increment',correction,
                'Complete new-system solution of the correctly rounded negative exact residual')
            with np.errstate(over='ignore',under='ignore',invalid='ignore'):candidate=best+correction
            if not np.isfinite(candidate).all():
                history['following_nonfinite_candidate']=output.save(f'iteration-{iteration+1:02d}-nonfinite-split-candidate',candidate,
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
        report['split_delta']=output.save('complete-split-coordinate-delta',best,
            'All579-node best direction selected by the new matrix residual; no native acceptance')
        report['split_direction_checkpoint']=checkpoint(B,output,system,best,source_sha,'split-direction-checkpoint.json.gz')
        restricted=np.array(best[np.asarray(system.old_to_new)],copy=True)
        report['restricted_old_node_delta']=output.save('complete-old-node-restricted-delta',restricted,
            'Only old577-node entries of the new578-stage direction; not a solution claim for old576 A')
        report['restricted_direction_checkpoint']=checkpoint(B,output,system,restricted,source_sha,
            'restricted-original-node-direction.json.gz',restricted=True)
        report['linear_direction_computed']=True
        report['new_system_floating_defects']=B.evaluate_directions(system,{'split':best},
            system.all('stage-residuals'),system.all('cut-residual').reshape(-1),system.all('end-residual').reshape(-1),
            system.all('original-scales').reshape(-1),system.all('original-far-graph').reshape(-1),output,'new578')
        # The old long matrix remains a diagnostic. Its magnitude does not
        # reject this newly represented direction or replace a nonlinear trial.
        original=system.original;residuals=original.all('stage-residuals')
        cut=original.all('cut-residual').reshape(-1);far=original.all('end-residual').reshape(-1)
        scales=original.all('original-scales').reshape(-1);far_graph=original.all('original-far-graph').reshape(-1)
        old_diagnostic=B.evaluate_directions(original,{'restricted_from_split':restricted},
            residuals,cut,far,scales,far_graph,output,'old576-diagnostic')
        report['old_long_matrix_diagnostic']=dict(reports=old_diagnostic,
            used_to_select_or_reject_direction=False,used_as_nonlinear_gate=False,
            full_original_nonlinear_evaluate_trial_not_run=True)
        site,entry=B.select_report_worst(old_diagnostic['restricted_from_split'])
        report['old_long_matrix_exact_single_row_diagnostic']=B.exact_row(original,restricted,
            residuals,cut,far,scales,far_graph,site,B.stored_scalar(entry),output,'old576-exact-diagnostic-row')
        report['diagnostic_completed']=True
    except Exception as error:report['actual_error']=repr(error)
    finally:
        if output is not None:
            report['array_manifest']=B.write(a.out/'output-array-manifest.json',dict(
                schema='native-split-shooting-direction-arrays-v1',source_sha256=source_sha,
                new_matrix_identity_sha256=report.get('new_matrix_identity_sha256'),
                original_capture_result_sha256=S.CAPTURE_SHA,actual_split_result_sha256=a.split_result_sha256,
                arrays=output.entries,all_arrays_artifact_only=True,native_accepted=False,task_completed=False))
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        B.write(a.out/'result.json',report)
    print(json.dumps(dict(event='native_split_equilibrated_band_finished',diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],native_accepted=False,task_completed=False)),flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':raise SystemExit(main())
