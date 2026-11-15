#!/usr/bin/env python3
"""One R273 correction from a live protocol call's fresh current576 snapshot.

This is a synchronous finite linear child, not a native solve loop.  It
uses every saved current J/r/cut/far/sigma value and all577 eta penalties.
The parent retains the original fresh evaluate formula, ten trial gates, convergence,
while explicitly adding separately identified same-state and post-failure noJ diagnostics,
final J and audit.  In particular no actual28 baseline, no actual57
direction, and no zero-cut assumption enter this consumer. Each positive
protocol call retains its actual height, target, sigma and current state;
the original worker supplies its own cold or live warm initialization.
No accepted parent, failed-state packet or imported response cache is used.

All scientific execution is confined to this public repository Actions.
The caller redirects this child process's stdout/stderr to per-iteration
files; they must never be forwarded into the native worker protocol.
"""
from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
import gzip
import hashlib
import importlib
import json
import math
import multiprocessing
import os
from pathlib import Path
import resource
import struct
import time
import traceback

import numpy as np
import scipy


HERE=Path(__file__).resolve().parent
SYSTEM_NAME='exact_20261115_current_H_secant576_system.py'
SYSTEM_SHA='9933e75ab4a07e920f8784e36eae93345c3735cf11b5a90f86d0eaef3073f25e'
QR_NAME='exact_20261114_native_damped_chain_qr.py'
QR_SHA='9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
KERNEL_NAME='exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA='0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
SCHEMA='complete-native-current-H-secant-r273-current576-damped-square-root-direction-v1'
MODEL_SCOPE='R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
_KERNEL=None


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or
            os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'):
        raise RuntimeError('Current native576 R273 work belongs only to this public repository Actions')


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def load_pinned(name,digest):
    path=HERE/name
    if file_sha(path)!=digest:raise ValueError('Frozen source changed: '+name)
    module=importlib.import_module(path.stem)
    if Path(module.__file__).resolve()!=path:raise ValueError('Unexpected source import: '+name)
    return module


def kernel():
    global _KERNEL
    if _KERNEL is None:_KERNEL=load_pinned(KERNEL_NAME,KERNEL_SHA)
    return _KERNEL


def exact_stage_job(task):
    return kernel().stage_job(task)


def current_identity(system):
    return dict(snapshot_result=system.snapshot_result,
        native_call=system.native_call,nonlinear_iteration=system.iteration,
        snapshot_sequence=system.sequence,current_state_sha256=system.current_state_sha256,
        request_height_float64le_sha256=system.request_height_sha256,
        current_request_file=system.current_request['request_file'],
        bootstrap_request=system.current_request['bootstrap_request'],
        new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'])


def exact_current_readback(S,system,delta,direction_descriptor,output,workers,producer_sha):
    """All original rows of this snapshot, exact before sigma division.

    No eta rows are inserted in this diagnostic.  The returned maximum
    concerns the exact arithmetic of the saved finite arrays, not an
    automatically exact mathematical derivative or a native acceptance.
    """
    require_actions()
    B=system.B;E=kernel();C=S.CurrentHSecant576ExactContext(system,E)
    M,K,D=system.M,system.K,system.depth
    label='current_damped'
    inputs={name:system.raw(name) for name in ('stage-residuals','cut-residual','end-residual',
                                              'original-scales','original-far-graph')}
    raw=B.float_bytes(delta);digest=hashlib.sha256(raw).hexdigest()
    B.same(digest,direction_descriptor['sha256'],'this complete current direction raw identity')
    decoded=E.decoded_array(raw,(D+1)*K,'complete current576 direction')
    residuals=E.decoded_array(inputs['stage-residuals'],D*K,'all current576 stage residuals')
    cut=E.decoded_array(inputs['cut-residual'],M,'all actual current cut residuals')
    far=E.decoded_array(inputs['end-residual'],M,'all actual current far residuals')
    graph=E.decoded_array(inputs['original-far-graph'],M,'complete original far graph')
    sigma_words=[item[0] for item in struct.iter_unpack('<Q',inputs['original-scales'])]
    state=dict(rows=0,products=0,worst=None,maxima=[])
    base_worst=None;pool=None;stages=0
    path=output.directory/'large-arrays/current576-all-exact-rows.jsonl.gz'
    raw_handle=None;ledger=None;started=time.monotonic()

    def consume(kind,node,data,jhash=None):
        nonlocal base_worst
        count=K if kind=='stage' else M
        value,row=data['base_maximum']
        base=C.max_record(kind,node,row,value,sigma_words[node])
        if E.better(base,base_worst):base_worst=base
        result=data['directions'][label]
        B.same(len(result['rows']),count,'every exact row in this current native block')
        record=C.max_record(kind,node,result['maximum_row'],result['maximum_integer'],sigma_words[node])
        if E.better(record,state['worst']):state['worst']=record
        public=E.public_record(record);state['maxima'].append(public)
        ledger.write(E.json_bytes(dict(kind=kind,node=node,
            first_global_equation_row=C.row_order(kind,node,0),
            all_exact_unscaled_rows=result['rows'],original_J_stage_sha256=jhash,
            exact_original_sigma_maximum=public,direction_label=label,
            direction_float64le_sha256=digest,**current_identity(system))))
        state['rows']+=count;state['products']+=result['original_product_positions']

    def tasks():
        for n,J in system.stage_bytes():
            yield dict(stage=n,J=J,residuals=residuals[n*K:(n+1)*K],
                directions={label:(decoded[n*K:(n+1)*K],decoded[(n+1)*K:(n+2)*K])})

    def take(result):
        nonlocal stages
        B.same(result['stage'],stages,'all current native stages in their original order')
        consume('stage',stages,result,result['J_stage_raw_sha256']);stages+=1
        if stages%32==0 or stages==D:
            print(json.dumps(dict(event='current576_complete_exact_readback',completed_stages=stages,
                expected_stages=D,nonlinear_iteration=system.iteration,snapshot_sequence=system.sequence,
                elapsed_seconds=time.monotonic()-started)),flush=True)

    try:
        raw_handle=path.open('xb');ledger=gzip.GzipFile(fileobj=raw_handle,mode='wb',mtime=0)
        consume('cut',0,E.boundary_job('cut',cut,{label:decoded[:K]},graph))
        if workers==1:
            for task in tasks():take(E.stage_job(task))
        else:
            pool=ProcessPoolExecutor(max_workers=workers,mp_context=multiprocessing.get_context('spawn'))
            queue=deque();source=iter(tasks())
            for _ in range(2*workers):
                task=next(source,None)
                if task is None:break
                queue.append(pool.submit(exact_stage_job,task))
            while queue:
                take(queue.popleft().result())
                task=next(source,None)
                if task is not None:queue.append(pool.submit(exact_stage_job,task))
            pool.shutdown(wait=True);pool=None
        consume('far',D,E.boundary_job('far',far,{label:decoded[D*K:(D+1)*K]},graph))
        B.same(stages,D,'every fresh current576 stage in exact readback')
        B.same(state['rows'],(D+1)*K,'all129248 original current equations')
        B.same(state['products'],D*K*K+M,'all original current product positions')
    finally:
        if pool is not None:pool.shutdown(wait=True,cancel_futures=True)
        if ledger is not None:ledger.close()
        if raw_handle is not None:raw_handle.close()
    descriptor=dict(name='current576-all-exact-rows',file=path.relative_to(output.directory).as_posix(),
        dtype='exact-dyadic-jsonl-gzip',shape=[state['rows']],bytes=path.stat().st_size,sha256=file_sha(path),
        role='Every actual current unscaled cut/stage/far row, then exact division by actual original sigma; no eta rows')
    output.entries.append(descriptor)
    maximum=E.public_record(state['worst'])
    witness=B.write(output.directory/'current576-worst-witness.json',dict(
        source_sha256=producer_sha,kernel_sha256=KERNEL_SHA,**current_identity(system),
        direction_float64le_sha256=digest,exact_original_sigma_maximum=maximum,
        operands=C.worst_witness(state['worst'],raw,inputs),
        saved_finite_arrays_only=True,exact_nonlinear_derivative_not_claimed=True))
    detail=dict(schema='current-H-secant-r273-current-native576-complete-exact-direction-readback-v1',
        source_sha256=producer_sha,system_source_sha256=SYSTEM_SHA,kernel_sha256=KERNEL_SHA,
        matrix_scope=S.MATRIX_SCOPE,**current_identity(system),
        direction_label=label,direction_float64le_sha256=digest,direction_array=direction_descriptor,
        exact_rows=state['rows'],completed_stages=stages,original_product_positions=state['products'],
        exact_global_original_sigma_norm=maximum,exact_stored_base_sigma_norm=E.public_record(base_worst),
        typed_block_maxima=state['maxima'],all_exact_residual_rows=descriptor,worst_witness=witness,
        eta_not_in_original_equations=True,readback_uses_unscaled_J_and_r_before_exact_sigma_division=True,
        actual_original_withJ_norm=system.current_records['norm'],
        stored_exact_base_norm_not_asserted_bitwise_equal_to_floating_original_norm=True,
        no_float_refinement_RHS_formed=True,used_as_new_nonlinear_acceptance_gate=False,
        no_cached_baseline=True,native_accepted=False,elapsed_seconds=time.monotonic()-started)
    full=B.write(output.directory/'current576-exact-readback.json.gz',detail,compressed=True)
    return dict(full_report=full,**current_identity(system),direction_label=label,
        direction_float64le_sha256=digest,exact_global_original_sigma_norm=maximum,
        exact_stored_base_sigma_norm=detail['exact_stored_base_sigma_norm'],
        actual_original_withJ_norm=system.current_records['norm'],
        exact_rows=state['rows'],completed_stages=stages,original_product_positions=state['products'],
        all_exact_residual_rows=descriptor,worst_witness=witness,
        used_as_new_nonlinear_acceptance_gate=False,no_float_refinement_RHS_formed=True)


def checkpoint(B,output,system,delta,eta,producer_sha):
    rows=[dict(node=n,state=row.tolist(),
        negative_zero_columns=np.flatnonzero((row==0)&np.signbit(row)).tolist()) for n,row in enumerate(delta)]
    return B.write(output.directory/'native-direction-checkpoint.json.gz',dict(
        schema='complete-native-current-H-secant-r273-current576-damped-direction-v1',source_sha256=producer_sha,
        system_source_sha256=SYSTEM_SHA,factor_engine_source_sha256=QR_SHA,
        input_binding=system.binding,**current_identity(system),M=system.M,K=system.K,depth=system.depth,
        original_depth=system.depth,old_to_new=system.old_to_new,
        eta_binary64=B.scalar(eta),model_scope=MODEL_SCOPE,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(),rows=rows,
        full_current576_direction=True,not_a_restriction_of_a1372_direction=True,
        complete_damped_direction_not_an_exact_Newton_claim=True,
        original_cut_and_far_direction_components_not_projected_or_zeroed=True,
        original_nonlinear_readback_required=True,no_nonlinear_trial_in_this_child=True,
        native_accepted=False,task_completed=False),compressed=True)


def small_summary(report,full_result):
    keys=('source_sha256','system_source_sha256','factor_engine_source_sha256','kernel_source_sha256',
        'snapshot_result','native_call','nonlinear_iteration','snapshot_sequence','current_state_sha256',
        'request_height_float64le_sha256','current_request_file','bootstrap_request',
        'eta_cli_text','eta_binary64','diagnostic_completed','linear_direction_computed',
        'new_matrix_identity_sha256','input_binding','factor_report','factor_summary',
        'factor_index','formed_stage_inventory','formed_model_diagnostic','native_delta',
        'native_direction_checkpoint','original_exact_readback','array_manifest',
        'actual_error','elapsed_seconds','maximum_RSS_kib')
    result={key:report[key] for key in keys if key in report}
    result.update(schema='native-current-H-secant-r273-current576-damped-chain-small-summary-v1',full_result=full_result,
        native_accepted=False,task_completed=False,no_cached_baseline=True,
        no_linear_norm_threshold_is_a_native_trial_gate=True,
        L2_model_descent_does_not_imply_original_infinity_descent=True)
    if len((json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode())>=95000:
        result={key:report[key] for key in ('diagnostic_completed','linear_direction_computed',
            'snapshot_result','native_call','nonlinear_iteration','snapshot_sequence','current_state_sha256',
            'new_matrix_identity_sha256','actual_error','elapsed_seconds') if key in report}
        result.update(schema='native-current-H-secant-r273-current576-damped-chain-small-summary-v1',full_result=full_result,
            compact_transport_fallback=True,native_accepted=False,task_completed=False)
    return result


def main():
    require_actions()
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--snapshot-directory',type=Path,required=True)
    p.add_argument('--snapshot-result-sha256',required=True)
    p.add_argument('--eta',required=True)
    p.add_argument('--factor-budget-seconds',type=float,default=None)
    p.add_argument('--max-factor-bytes',type=int,default=2*1024**3)
    p.add_argument('--exact-workers',type=int,default=2)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    eta=float(a.eta)
    if not math.isfinite(eta) or eta<=0:
        raise ValueError('Eta is an explicit positive finite model parameter, not a native tolerance')
    if a.factor_budget_seconds is not None and (not math.isfinite(a.factor_budget_seconds) or a.factor_budget_seconds<=0):
        raise ValueError('An optional factor budget must be finite and positive')
    if a.max_factor_bytes<=0 or not 1<=a.exact_workers<=4:
        raise ValueError('Keep a positive complete-factor storage budget and one to four exact workers')
    out=a.out.resolve()
    if (os.path.lexists(a.out) or out.is_relative_to(a.snapshot_directory.resolve()) or
            a.snapshot_directory.resolve().is_relative_to(out)):
        raise ValueError('Use one new independent per-correction output directory')
    out.mkdir(parents=True)
    started=time.monotonic();producer_sha=file_sha(__file__)
    S=load_pinned(SYSTEM_NAME,SYSTEM_SHA);Q=load_pinned(QR_NAME,QR_SHA);B=S.load_binding()
    output=B.OutputArrays(out);factor=None
    report=dict(schema=SCHEMA,source_sha256=producer_sha,system_source_sha256=SYSTEM_SHA,
        factor_engine_source_sha256=QR_SHA,kernel_source_sha256=KERNEL_SHA,
        eta_cli_text=a.eta,eta_binary64=B.scalar(eta),model_scope=MODEL_SCOPE,
        original_native_calls_in_this_child=0,new_RHS_calls_in_this_child=0,
        new_J_calls_in_this_child=0,new_ODE_steps_in_this_child=0,nonlinear_trials_in_this_child=0,
        snapshot_contains_one_real_fresh_current_withJ_evaluation=True,
        scientific_call_counts_above_describe_only_this_child_not_the_parent_native_solve=True,
        diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        target_is_complete_fresh_current576_saved_matrix=True,no_cached_baseline=True,
        this_call_original_cut_H_far_and_sigma_not_changed=True,current_cut_far_direction_not_projected_or_zeroed=True,
        later_requests_not_replaced_by_bootstrap_height_or_state=True,
        no_normal_matrix_Riccati_inverse_rank_truncation_or_extra_ridge=True,
        damping_is_not_a_new_final_equation_or_acceptance_tolerance=True,
        exact_linear_defect_not_used_as_new_native_trial_gate=True,
        original_native_trial_convergence_finalJ_audit_remain_in_parent=True,
        factor_budget_seconds=a.factor_budget_seconds,maximum_factor_bytes=a.max_factor_bytes,
        exact_workers=a.exact_workers,NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')})
    try:
        system=S.CurrentHSecant576System(a.snapshot_directory,a.snapshot_result_sha256,B)
        report.update(current_identity(system))
        report['input_binding']=B.write(out/'input-binding.json.gz',system.binding,compressed=True)
        report['original_arrays']=system.export_inputs(output)
        deadline=None if a.factor_budget_seconds is None else time.monotonic()+a.factor_budget_seconds
        factor=Q.NativeDampedChainQR(system,eta,a.eta,output,deadline,a.max_factor_bytes)
        factor.factorize()
        report['factor_index']=B.write(out/'factor-index.json.gz',dict(
            source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,**current_identity(system),
            factors=factor.factors,complete=True),compressed=True)
        report['formed_stage_inventory']=B.write(out/'formed-stage-inventory.json.gz',dict(
            source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,**current_identity(system),
            formed_model_identity_sha256=factor.report['formed_model_identity_sha256'],
            stages=factor.formed_stage_rows),compressed=True)
        z,delta=factor.solve()
        report['linear_direction_computed']=True
        report['native_delta']=factor.report['solve']['delta']
        report['native_direction_checkpoint']=checkpoint(B,output,system,delta,eta,producer_sha)
        report['original_exact_readback']=exact_current_readback(S,system,delta,
            report['native_delta'],output,a.exact_workers,producer_sha)
        report['formed_model_diagnostic']=factor.model_readback(z)
        report['diagnostic_completed']=True
    except Exception as error:
        report['actual_error']=repr(error)
        report['actual_traceback']=traceback.format_exc()
    finally:
        if factor is not None:
            factor.report.update(qr_calls=factor.qr_calls,formation_calls=factor.formation_calls,
                formation_underflow_to_binary64_zero=factor.formation_underflow,
                elapsed_seconds=time.monotonic()-factor.started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            report['factor_summary']={key:factor.report[key] for key in (
                'complete','rows','columns','augmented_rows','stage_count','node_count','block_width',
                'node_penalty_blocks','qr_calls','formation_calls','formation_underflow_to_binary64_zero',
                'pure_constant_rows','actual_factor_and_constant_bytes','formed_model_identity_sha256',
                'pure_constant_energy_longdouble','minimum_absolute_triangular_diagonal',
                'expected_factor_and_constant_bytes','maximum_declared_factor_bytes','working_precision',
                'elapsed_seconds','maximum_RSS_kib') if key in factor.report}
            report['factor_report']=B.write(out/'factor-report.json.gz',factor.report,compressed=True)
            if 'factor_index' not in report:
                report['factor_index']=B.write(out/'partial-factor-index.json.gz',dict(
                    source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,
                    complete=False,factors=factor.factors,partial_factors_not_a_complete_direction=True),compressed=True)
            if 'formed_stage_inventory' not in report:
                report['formed_stage_inventory']=B.write(out/'partial-formed-stage-inventory.json.gz',dict(
                    source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,
                    complete=False,stages=factor.formed_stage_rows),compressed=True)
        manifest_identity={key:report[key] for key in ('snapshot_result','native_call','nonlinear_iteration',
            'snapshot_sequence','current_state_sha256','request_height_float64le_sha256',
            'current_request_file','bootstrap_request','new_matrix_identity_sha256') if key in report}
        report['array_manifest']=B.write(out/'output-array-manifest.json.gz',dict(
            schema='complete-native-current-H-secant-r273-current576-damped-direction-arrays-v1',source_sha256=producer_sha,
            factor_engine_source_sha256=QR_SHA,**manifest_identity,
            arrays=output.entries,all_arrays_temporary_only=True,native_accepted=False),compressed=True)
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        full=B.write(out/'result.json.gz',report,compressed=True)
        B.write(out/'summary.json',small_summary(report,full))
    print(json.dumps(dict(event='current576_damped_chain_finished',diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],native_accepted=False,
        native_call=report.get('native_call'),nonlinear_iteration=report.get('nonlinear_iteration'),
        snapshot_sequence=report.get('snapshot_sequence'))),flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':
    raise SystemExit(main())
