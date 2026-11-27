#!/usr/bin/env python3
"""Continue the actual failed hard-tau1 input with guaranteed scalar progress.

Same actual397 frozen E/q/H/amp, all old mouths, original full work/fine grids,
all1473 height columns and1472 free response columns. The prior first-input
failure is literal and costed. No old numerical module is monkey-patched.
The original full-S solver and readout functions are consumed unchanged.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SCHEMA = 'r618-actual397-fixed-E-hard-tau1-explicit-bracket-progress-v1'
PREVIOUS_FINAL_SHA = '2b27561b60402679332b45ae8235a02e7aea98a985de8a77c49a0d952bee2856'
PREVIOUS_LOG_SHA = '3672c10cb8c31e121270c68b27b4669a231f47fa78d63b81bc62c43c2e3037cb'
COMPONENTS = {
    'previous':('r618_actual397_fixed_metric_response_20261127.py',
        'c8a5d3b96039579fb979eb334562cd4028eb39f4aae12413f613a404f5ec6463'),
    'chart':('r618_bracket_progress_model_20261127.py',
        '1e1049627d8acc936ea067fedc0e0f39387c9a035257a86907050990c63d2463'),
    'consumers':('r618_bracket_progress_consumers_20261127.py',
        '6e0533b154d9174fbbdab4e4ffbb3c5c13a665d7f76266dbdf0c08308d976f73')}


def emit(tag,value):
    print('FIXED_E397_BRACKET_'+tag+' '+json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False),flush=True)


def bound_import(label):
    filename,digest = COMPONENTS[label]
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('exact bracket-progress component differs: '+filename)
    spec = importlib.util.spec_from_file_location('r618_bracket_actual397_'+label,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_input(args,previous,identity_module,chart):
    incoming,source,identity,input_sha = previous.read_input(args,identity_module)
    if incoming.get('scope_schema') != SCHEMA:
        raise ValueError('this actual failed-state follow-up scope differs')
    record = incoming['preceding_fixed_E_failure']
    raw = record['literal_FINAL_JSON']
    if (record['run_id'] != 45914497186 or record['job_id'] != 140230360702
            or record['source_commit'] != '414b7662f8cddf8a06fb9aa5595cadd69e05ca3c'
            or record['raw_job_log_bytes'] != 384718 or record['raw_job_log_sha256'] != PREVIOUS_LOG_SHA
            or len(raw.encode()) != 35131 or hashlib.sha256(raw.encode()).hexdigest() != PREVIOUS_FINAL_SHA):
        raise ValueError('literal previous hard-tau1 natural failure identity differs')
    final = json.loads(raw)
    if (final['same_frozen_target_sha256'] != identity.target_sha256
            or final['reference_source_sha256'] != previous.SOURCE_SHA
            or final['reference_q_sha256'] != previous.SOURCE_Q_SHA
            or final['status'] != 'declared_fixed_E_model_or_numerical_failure_actual_checkpoint'
            or final['actual_checkpoint']['accepted_step'] != 0
            or final['actual_checkpoint']['hard_tau'] != 1.
            or final['actual_next_damping'] != 1e-8
            or final['summary'] is not None or final['readout'] is not None
            or final['complete_row_QR_SVD_counts'] or final['direct_position_counts']
            or len(final['actual_response']) != 1473
            or final['actual_response'][:-1] != [0.]*1472 or final['actual_response'][-1] != 1.):
        raise ValueError('the prior true checkpoint was not this unmodified first hard-tau1 input')
    policy = incoming['numerical_and_response_policy']
    if (policy.get('bracket_progress_adapter') != chart.BracketProgressHeight.policy_descriptor()
            or policy['root_steps'] != 80 or policy['root_tolerance'] != 1e-13
            or policy['mean_bracket_radius'] != {'lambda':.2,'shift':.2,'zeta':.2}):
        raise ValueError('exact explicit scalar progress policy differs')
    return incoming,source,identity,input_sha,final


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-state-json',required=True)
    parser.add_argument('--source-state-sha256',required=True)
    parser.add_argument('--maximum-seconds',type=float,choices=[5400.],default=5400.)
    parser.add_argument('--final-reserve-seconds',type=float,choices=[1800.],default=1800.)
    parser.add_argument('--iterations',type=int,choices=[20],default=20)
    parser.add_argument('--target-eta',type=float,choices=[2e-9],default=2e-9)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('science requires this explicitly declared public Actions scope')
    previous,chart,consumers = [bound_import(key) for key in ('previous','chart','consumers')]
    driver,identity_module = [previous.bound_import(key) for key in ('original','identity')]
    incoming,source,identity,input_sha,prior_final = read_input(args,previous,identity_module,chart)
    started = time.monotonic();deadline = started+args.maximum_seconds
    solver_deadline = deadline-args.final_reserve_seconds
    model = response = summary = readout = None
    damping = 1e-8;attempts = [];failure = None
    status = 'actual397_failed_hard_tau1_before_necessary_reconstruction_for_new_scalar_method'
    emit('DEFINITION',{'schema':SCHEMA,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_state_sha256':input_sha,'complete_new_scope_input':incoming,
        'same_frozen_target_sha256':identity.target_sha256,
        'actual_reference_source_sha256':previous.SOURCE_SHA,'actual_reference_q_sha256':previous.SOURCE_Q_SHA,
        'actual_initial_response_identity':prior_final['actual_response_identity'],
        'new_scalar_progress_source_and_policy_bound_before_model_identity':True,
        'frozen_original_modules_or_types_patched':False,
        'hard_tau_fixed_exactly_in_the_solver':1.,'complete_height_parameters':1473,'active_response_parameters':1472,
        'whole_original_work950_N256_and_fine1728_N512_retained':True,
        'original_reference_amp_H_and_every_paid_mouth_unchanged':True,
        'preceding_failure_all_costs_inherited_not_relabelled_as_new':True,
        'old102_completed_means_not_fabricated_as_saved_scientific_arrays':True,
        'no_old_DtN_inner_Riccati_or_diagnostic_gate':True,
        'whole_reference_E_interval_contract_only_quantifies_true_cap_to_mouth':True,
        'continuous_fixed_E_metric_or_README_claim':False,
        'arguments':{key:value for key,value in vars(args).items() if key != 'source_state_json'}})
    try:
        model = chart.BracketProgressHeight.restore_from_frozen_reference(driver,
            source['actual_1130q_JSON'],source['amplitude'],identity,incoming['maximum_independent_mode'],
            incoming['numerical_and_response_policy'],deadline=deadline,attempts=attempts)
        response = model.initial_response();response[model.tau_index] = 1.
        if model.nq != 1473 or previous.response_identity(response) != prior_final['actual_response_identity']:
            raise ValueError('same actual failed hard-tau1 input was not retained')
        model.actual_checkpoint = {'response':response.copy(),'accepted_step':0,'damping':damping,
            'hard_tau':1.,'status':'same_actual_hard_tau1_input_before_new_scalar_method_evaluation',
            'same_frozen_target_sha256':identity.target_sha256}
        model.pending_trial = model.last_trial = model.partial_readout = None
        contract = previous.conditional_source_contract(model,consumers)
        emit('TAIL_SOURCE_CONTRACT',{'literal_JSON':contract[0],'sha256':contract[1],
            'strict_source_error_consumer_selected':False,'all_seven_original_error_categories_unresolved':True,
            'E_interval_quantifies_only_whole_true_cap_to_mouth_not_body_or_core':True})
        data = model.prepare(model.original_work_radii,256)
        response,state,damping,summary = previous.solve(model,response,data,args,chart,consumers,contract,solver_deadline)
        status = summary['status']
        readout = previous.fine_readout(model,response,args,chart,consumers,contract)
        emit('STAGE',{'summary':summary,'readout':readout,'actual_next_damping':damping,
            'same_frozen_target_sha256':identity.target_sha256})
    except (driver.weak.ScientificBudget,driver.paid.ScientificBudget,driver.high.HighModeBudget) as exc:
        status = 'declared_scientific_budget_actual_fixed_E_bracket_checkpoint'
        failure = {'type':type(exc).__name__,'message':str(exc)}
        emit('CLOCK',failure)
    except (driver.base.DomainError,ArithmeticError,ValueError,FloatingPointError,RuntimeError,
            TypeError,KeyError,AttributeError,MemoryError,np.linalg.LinAlgError) as exc:
        status = 'declared_fixed_E_bracket_model_or_numerical_failure_actual_checkpoint'
        failure = {'type':type(exc).__name__,'message':str(exc)}
        emit('FAILURE',failure)
    actual = pending = None
    if model is not None and hasattr(model,'actual_checkpoint'):
        kept = model.actual_checkpoint;response = kept['response'].copy();damping = kept['damping']
        actual = {key:value for key,value in kept.items() if key != 'response'}
        if model.pending_trial is not None:
            pending = {key:(value.tolist() if isinstance(value,np.ndarray) else value)
                       for key,value in model.pending_trial.items()}
    final = {'schema':SCHEMA,'status':status,'failure':failure,'elapsed_seconds':time.monotonic()-started,
        'same_frozen_target_sha256':identity.target_sha256,'reference_source_sha256':previous.SOURCE_SHA,
        'reference_q_sha256':previous.SOURCE_Q_SHA,'reference_H':.5188903877153482,'reference_amplitude':1e-5,
        'actual_response':None if response is None else response.tolist(),
        'actual_response_identity':None if response is None else previous.response_identity(response),
        'actual_next_damping':damping,'actual_checkpoint':actual,'pending_trial_not_accepted':pending,
        'last_trial':None if model is None else getattr(model,'last_trial',None),
        'summary':summary,'readout':readout,'partial_readout':None if model is None else getattr(model,'partial_readout',None),
        'paid_high_reconstruction_attempts':driver.full.attempt_receipts(attempts),
        'actual_model_cost_receipt':None if model is None else model.cumulative_cost_receipt(),
        'original_module_counters_including_failed_reconstruction':previous.original_costs(driver),
        'growing_height_counts_including_failed_construction':dict(chart.height.COUNTS),
        'fixed_metric_chain_counts_including_failed_construction':dict(chart.chain.COUNTS),
        'new_scope_counts':dict(previous.COUNTS),'complete_row_QR_SVD_counts':dict(driver.factorization.COUNTS),
        'stable_coordinate_counts':dict(chart.stable.COUNTS),'bracket_progress_counts':dict(chart.COUNTS),
        'recent_scalar_progress_receipts_and_complete_costs':chart.root_attempt_receipts(),
        'true_tail_producer_counts':dict(consumers.producer.COUNTS),
        'true_tail_bound_counts':dict(consumers.producer.bounds.COUNTS),
        'direct_position_counts':dict(consumers.direct.COUNTS),'rejections':dict(previous.REJECTIONS),
        'original_reference_source_cost_not_counted_as_this_run':source['source_cost_ledger'],
        'every_earlier_reference_cost_ledger_not_counted_as_this_run':source['prior_cost_ledgers'],
        'preceding_fixed_E_failure_identity':{key:value for key,value in incoming['preceding_fixed_E_failure'].items()
            if key != 'literal_FINAL_JSON'},
        'preceding_fixed_E_failure_full_actual_receipt_not_counted_as_this_run':prior_final,
        'overlapping_counters_and_inherited_ledgers_are_not_disjoint_costs':True,
        'old_inner_DtN_or_diagnostic_gates_replayed':False,'fixed_E_or_tau_or_q_silently_changed':False,
        'all_original_work_fine_rows_and_all_full_singular_directions_retained':True,
        'scalar_coordinate_width_not_a_source_or_continuous_root_certificate':True,
        'whole_reference_E_interval_contract_only_quantifies_true_cap_to_mouth':True,
        'source_ODE_alias_mean_primitive_and_global_errors_not_defaulted_to_zero':True,
        'continuous_metric_curvature_reach_and_README_certified':False,
        'raw_arrays_artifacts_releases_or_git_writes':False}
    raw = json.dumps(final,sort_keys=True,separators=(',',':'),allow_nan=False)
    print('FIXED_E397_BRACKET_FINAL '+raw,flush=True)
    emit('FINAL_IDENTITY',{'JSON_bytes':len(raw.encode()),'sha256':hashlib.sha256(raw.encode()).hexdigest()})


if __name__ == '__main__':
    main()
