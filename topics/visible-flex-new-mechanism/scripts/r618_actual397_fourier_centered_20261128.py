#!/usr/bin/env python3
"""Continue the actual397 fixed-E response with exact Fourier backgrounds removed.

Same actual397 frozen E/q/H/amp, all old mouths, original full work/fine grids,
all1473 height columns and1472 free response columns. The preceding complete split
run, its actual accepted response, pending failure and every cost are retained. No old numerical module is monkey-patched.
The complete full-S operator and readout remain; all mean/connection
directions use the algebraically identical centered chain and new scalar progress.
"""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SCHEMA = 'r618-actual397-fixed-E-centered-Fourier-derivatives-v1'
PREVIOUS_FINAL_SHA = 'b1367076702c3bade368f30034ac79ff9e510888b0f1909259be8899d52aa84e'
PREVIOUS_LOG_SHA = '7ebd5c174a7bdb9369b78fe0dbbdfefed72bbcb0c66793768517674797131904'
COMPONENTS = {
    'previous':('r618_actual397_fixed_metric_response_20261127.py',
        'c8a5d3b96039579fb979eb334562cd4028eb39f4aae12413f613a404f5ec6463'),
    'chart':('r618_fourier_centered_model_20261128.py',
        'fe1d8a07343152bc981a94cd00c311b826fc283afa1c6b020e9b7de59c04bda3'),
    'consumers':('r618_fourier_centered_consumers_20261128.py',
        '33c394a179869467b45dd8f0c86c157adf0b105740f9739e7ccd770a0684d909')}


def emit(tag,value):
    print('FIXED_E397_CENTERED_'+tag+' '+json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False),flush=True)


def bound_import(label):
    filename,digest = COMPONENTS[label]
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('exact persistent split component differs: '+filename)
    spec = importlib.util.spec_from_file_location('r618_split_actual397_'+label,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_input(args,previous,identity_module,chart):
    raw = sys.stdin.buffer.read() if args.source_state_json == '@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest() != args.source_state_sha256:
        raise ValueError('complete new fixed-E input identity differs')
    incoming = json.loads(raw)
    source_text,field_text = incoming['frozen_source_state_JSON'],incoming['mathematical_field_JSON']
    if (len(source_text.encode()) != 157609 or hashlib.sha256(source_text.encode()).hexdigest() != previous.SOURCE_SHA
            or hashlib.sha256(field_text.encode()).hexdigest() != previous.FIELD_SHA
            or field_text != (HERE.parent/'computations/r618-actual397-frozen-field-definition-20261127.json').read_text()):
        raise ValueError('the one actual397 source or complete fixed mathematical field changed')
    source = json.loads(source_text)
    qtext = source['actual_1130q_JSON']
    if (hashlib.sha256(qtext.encode()).hexdigest() != previous.SOURCE_Q_SHA
            or len(qtext.encode()) != 22713 or source['global_accepted_iteration'] != 397
            or source['amplitude'] != 1e-5 or json.loads(qtext)[0] != .5188903877153482
            or source['origin']['run_id'] != 45899589237 or source['origin']['job_id'] != 140181814100):
        raise ValueError('actual completed397 reference differs')
    identity = identity_module.FrozenTargetIdentity.bind(source_text,previous.SOURCE_SHA,field_text,previous.FIELD_SHA)
    if identity.target_sha256 != previous.TARGET_SHA:
        raise ValueError('the frozen complete target identity changed')
    if (incoming['maximum_independent_mode'] != 48 or incoming['hard_core_tau'] != 1.
            or incoming['initial_response_definition'] != 'actual_accepted_split_response_19519575'
            or incoming['new_operator_initial_damping'] != 3.3333333333333334e-9):
        raise ValueError('declared genuine nonzero fixed stage changed')
    if incoming.get('scope_schema')!=SCHEMA:
        raise ValueError('declared centered continuation schema differs')
    record=incoming['preceding_complete_split_run']
    literal=record['literal_FINAL_JSON']
    if (record['run_id']!=45923793283 or record['job_id']!=140260374411
            or record['source_commit']!='4e00e0fb25f120b0781a4a943d49b23e42710337'
            or record['raw_job_log_bytes']!=789748 or record['raw_job_log_sha256']!=PREVIOUS_LOG_SHA
            or len(literal.encode())!=243899
            or hashlib.sha256(literal.encode()).hexdigest()!=PREVIOUS_FINAL_SHA):
        raise ValueError('actual preceding complete split run identity differs')
    final=json.loads(literal)
    if (final['same_frozen_target_sha256']!=identity.target_sha256
            or final['actual_response_identity']['sha256']!='19519575f7b4a8100cf9813851c258188ad4a0063edad05eb1b5b332b83f2cc7'
            or final['actual_checkpoint']['accepted_step']!=1
            or final['actual_checkpoint']['hard_tau']!=1.
            or final['actual_next_damping']!=incoming['new_operator_initial_damping']
            or final['elapsed_seconds']!=5400.058385949001
            or final['readout'] is not None):
        raise ValueError('continue the actual accepted response, not its incomplete trial')
    if incoming['numerical_and_response_policy']['split_reference_adapter']!=chart.FourierCenteredHeight.policy_descriptor():
        raise ValueError('all new numerical directions and root policy must be bound before restoration')
    return incoming,source,identity,hashlib.sha256(raw).hexdigest(),final


COUNTS=defaultdict(int)
REJECTIONS=defaultdict(int)

def one_height_direction(model,direction,data,core_coefficients,chart):
    """One actual combined direction, avoiding an nr*N*1473 array.

    Same six-jet linear dictionary as the frozen model; core_coefficients
    already contains its complete nonlinear core derivative. No new J or
    old direction-check gate is computed here.
    """
    values = model.old.delta_jets(np.r_[0.,direction[:model.old_count]],model.amplitude,data)
    answer = dict(zip(chart.height.JET_KEYS,values))
    correction = chart.height._separable(data['core_radial'],core_coefficients,model.core_modes,data['theta'])
    for key in answer:
        answer[key] = answer[key]+correction[key]
    for start,count,modes,radial in (
            (model.compact_start,model.compact_count,model.extra_compact_modes,data['compact_radial_dictionary']),
            (model.tail_start,model.tail_count,model.modes,data['analytic_tail_columns'])):
        if count:
            coefficients = model.amplitude*direction[start:start+count].reshape(len(modes),radial.shape[1])
            fields = np.einsum('rbk,jb->rjk',radial,coefficients)
            co,si = np.cos(modes[:,None]*data['theta']),np.sin(modes[:,None]*data['theta'])
            extra = (fields[:,:,0]@co,fields[:,:,1]@co,fields[:,:,2]@co,
                -(fields[:,:,0]*modes)@si,-(fields[:,:,0]*modes*modes)@co,
                -(fields[:,:,1]*modes)@si)
            for key,value in zip(chart.height.JET_KEYS,extra):
                answer[key] += value
    core = chart.height._separable(data['new_core_lift'],
        model.amplitude*direction[model.core_start:model.tau_index],model.core_free_modes,data['theta'])
    for key in answer:
        answer[key] += core[key]
    COUNTS['combined_function_direction_angular_points'] += int(answer['f'].size)
    return answer

def function_step_limit(model,direction,data,state,chart):
    if not np.all(np.isfinite(direction)) or direction[model.tau_index] != 0:
        raise ArithmeticError('finite hard-tau tangent direction required')
    columns = model.core_direction(state['core'],np.arange(model.nq))
    coefficients = columns['correction_delta']@direction
    Hm = one_height_direction(model,direction,data['fixed_mean_data'],coefficients,chart)
    Ho = one_height_direction(model,direction,data,coefficients,chart)
    changes = {'relative_b':0.,'relative_u':0.,'relative_N':0.,'reference_coordinate_fraction':0.,
               'height':0.,'height_theta_over_r':0.,'height_r_over_1_W':0.}
    coordinate_attainer=None
    for index,r in enumerate(data['r']):
        model.driver.check(model.deadline)
        mean = state['mean_states'][index]
        dm = model.split_chain.mean_direction(mean,{k:v[index,:,None] for k,v in Hm.items()})
        ds = model.split_chain.output_direction(state['output_states'][index],
                {k:v[index,:,None] for k,v in Ho.items()},dm)
        for key,name in (('b','relative_b'),('u','relative_u'),('N','relative_N')):
            changes[name] = max(changes[name],float(np.max(abs(ds[key][:,0])/state['output_states'][index][key])))
        width = mean['target']['stable_reference_coordinate_box']['coordinate_halfwidth']
        margin = width-abs(mean['x'])
        if margin <= 0:
            raise ArithmeticError('actual same-root state reached the original coordinate box boundary')
        dx_long=abs(dm['s_longdouble'][0]/np.longdouble(mean['coordinate_scale']))
        dx=float(dx_long)
        ratio=dx/margin
        if coordinate_attainer is None or ratio > changes['reference_coordinate_fraction']:
            coordinate_attainer={'r':float(r),'W':float(mean['target']['W']),
                'chart':mean['chart'],'coordinate':float(mean['x']),
                'coordinate_margin':float(margin),'direction_coordinate':dx,
                'same_mean_derivative':mean['mean_derivative_decimal'],
                'direction_s':float(dm['s'][0]),'direction_s_r':float(dm['s_r'][0]),
                'linearized_turning_mean':float(dm['turning_linearized_residual_observation'][0]),
                'linearized_connection_mean':float(dm['connection_linearized_residual_observation'][0])}
        changes['reference_coordinate_fraction']=max(changes['reference_coordinate_fraction'],ratio)
    changes['height'] = float(np.max(abs(Ho['f'])))
    changes['height_theta_over_r'] = float(np.max(abs(Ho['ft'])/data['r'][:,None]))
    changes['height_r_over_1_W'] = float(np.max(abs(Ho['fr'])/(1+data['frozen_W'][:,None])))
    maximum = max(changes.values())
    if not np.isfinite(maximum):
        raise ArithmeticError('nonfinite actual function direction observation')
    factor = min(1.,.1/maximum) if maximum > 0 else 1.
    COUNTS['new_complete_function_direction_limits'] += 1
    return factor,{'linearized_complete_field_changes':changes,
        'factor':factor,'reference_coordinate_attainer':coordinate_attainer,
        'not_a_nonlinear_or_continuous_domain_certificate':True,
        'hard_tau_direction_exactly_zero':True}

def solve(model,response,data,args,chart,consumers,contract,solver_deadline,initial_damping,initial_accepted_step):
    response = response.copy();damping = float(initial_damping)
    tail = anchor(model,response,data,consumers,contract)
    state = model.evaluate(response,data)
    report = checkpoint(model,response,data,state,initial_accepted_step,damping,'same_actual_response_on_centered_direction_evaluator',tail)
    status = 'declared_twenty_step_fixed_E_iteration_limit'
    accepted_steps = 0
    for iteration in range(args.iterations):
        if time.monotonic() >= solver_deadline:
            status = 'declared_fixed_E_solver_reserve_for_complete_actual_readout'
            break
        model.driver.check(model.deadline)
        if report['conditional_S_identity_eta'] <= args.target_eta:
            status = 'active_conditional_target_requires_actual_fixed_E_fine_readout'
            break
        residual = state['residual'];objective = float(residual@residual/2)
        full_J = model.jacobian(response,data,state,block_columns=16)
        if model.tau_index != model.nq-1 or model.nq != 1473:
            raise ValueError('declared complete1473 model and final fixed tau column required')
        J = full_J[:,:model.tau_index]
        reduction = model.driver.factorization.CompleteRowFactor(J,residual,batch_rows=4096,
            deadline_check=lambda:model.driver.check(model.deadline))
        del J,full_J
        COUNTS['full_1473_J_evaluations_before_exact_hard_tau_elimination'] += 1
        COUNTS['hard_tau_columns_eliminated_by_delta_tau_equals_zero'] += 1
        spectrum = reduction.spectrum()
        spectrum['complete_height_parameters'] = model.nq
        spectrum['fixed_tau_stage_parameter'] = 1.
        spectrum['active_columns_exactly_1472'] = True
        accepted = False
        for trial in range(8):
            model.driver.check(model.deadline)
            if time.monotonic() >= solver_deadline:
                return response,state,damping,{'status':'solver_reserve_after_full_factorization',
                    'last_report':report,'accepted_steps':accepted_steps}
            lam = damping*10.**trial
            direction = np.r_[reduction.direction(lam),0.]
            COUNTS['new_fixed_E_model_directions'] += 1
            try:
                factor,measures = function_step_limit(model,direction,data,state,chart)
            except (ArithmeticError,ValueError) as exc:
                REJECTIONS['function_direction:'+str(exc)] += 1
                COUNTS['function_direction_rejections'] += 1
                continue
            emit('DIRECTION_LIMIT',{'iteration':iteration,'trial':trial,'measures':measures})
            direction *= factor
            for cut in range(9):
                model.driver.check(model.deadline)
                if time.monotonic() >= solver_deadline:
                    return response,state,damping,{'status':'solver_reserve_before_next_complete_trial',
                        'last_report':report,'accepted_steps':accepted_steps}
                fraction = 2.**(-cut)
                predicted = reduction.predicted_decrease(direction[:-1],fraction)
                COUNTS['fixed_E_line_search_algebraic_trials'] += 1
                if not np.isfinite(predicted) or predicted <= 0:
                    REJECTIONS['nonpositive_or_nonfinite_full_linear_prediction'] += 1
                    continue
                proposed = response+fraction*direction
                model.pending_trial = {'iteration':iteration,'trial':trial,'fraction':fraction,
                    'response':proposed.copy(),'predicted_decrease':predicted,
                    'status':'new_fixed_E_trial_not_yet_accepted'}
                COUNTS['fixed_E_actual_trial_evaluations_attempted'] += 1
                try:
                    if proposed[model.tau_index] != 1.:
                        raise ValueError('hard tau1 was changed')
                    candidate_tail = anchor(model,proposed,data,consumers,contract)
                    candidate = model.evaluate(proposed,data,accepted_mean_seed=state['mean_states'])
                    candidate_objective = float(candidate['residual']@candidate['residual']/2)
                    if not np.isfinite(candidate_objective):
                        raise ArithmeticError('nonfinite complete trial objective')
                    actual = objective-candidate_objective
                    ratio = actual/predicted
                    okay = (np.isfinite(ratio) and actual > max(32*np.finfo(float).eps*objective,1e-30)
                            and ratio > .01)
                    reason = 'no_resolvable_complete_fixed_E_position_decrease'
                    model.last_trial = {'iteration':iteration,'trial':trial,'fraction':fraction,
                        'response_identity':response_identity(proposed),'complete_S_merit':candidate_objective,
                        'actual_decrease':actual,'predicted_decrease':predicted,'accepted':bool(okay)}
                except (model.driver.base.DomainError,ArithmeticError,ValueError,FloatingPointError) as exc:
                    okay = False;reason = type(exc).__name__+':'+str(exc)
                    model.last_trial = {'iteration':iteration,'trial':trial,'fraction':fraction,
                        'response_identity':response_identity(proposed),'failure':reason,'accepted':False}
                model.pending_trial = None
                if okay:
                    response,state,tail = proposed,candidate,candidate_tail
                    old_damping = damping;damping = max(1e-14,lam/3)
                    accepted_steps += 1;COUNTS['accepted_fixed_E_steps'] += 1
                    emit('ACCEPTANCE',{'iteration':iteration,'accepted_step':initial_accepted_step+accepted_steps,
                        'trial':trial,'fraction':fraction,'function_factor':factor,'function_measures':measures,
                        'damping_before':old_damping,'lambda_used':lam,'actual_next_damping':damping,
                        'actual_decrease':actual,'predicted_decrease':predicted,'actual_over_predicted':ratio,
                        'spectrum':spectrum,'same_frozen_target_sha256':model.identity.target_sha256,
                        'hard_tau':1.,'source_H_and_amplitude_unchanged':True})
                    report = checkpoint(model,response,data,state,initial_accepted_step+accepted_steps,damping,
                        'actual_accepted_complete_fixed_E_position_decrease',tail)
                    accepted = True
                    break
                COUNTS['rejected_fixed_E_trial_evaluations'] += 1
                REJECTIONS[reason] += 1
            if accepted:
                break
        if not accepted:
            status = 'no_resolvable_step_in_this_complete_fixed_E_finite_response_stage'
            emit('STALL',{'iteration':iteration,'response_identity':response_identity(response),
                'actual_response':response.tolist(),'actual_next_damping':damping,'spectrum':spectrum,
                'not_a_geometric_impossibility_or_stationarity_certificate':True})
            break
    return response,state,damping,{'status':status,'last_report':report,'accepted_steps':accepted_steps}


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
    global anchor,checkpoint,response_identity
    anchor,checkpoint,response_identity=previous.anchor,previous.checkpoint,previous.response_identity
    driver,identity_module = [previous.bound_import(key) for key in ('original','identity')]
    incoming,source,identity,input_sha,prior_final = read_input(args,previous,identity_module,chart)
    started = time.monotonic();deadline = started+args.maximum_seconds
    solver_deadline = deadline-args.final_reserve_seconds
    model = response = summary = readout = None
    damping = prior_final['actual_next_damping'];attempts = [];failure = None
    status = 'actual397_accepted_response_before_necessary_centered_reconstruction'
    emit('DEFINITION',{'schema':SCHEMA,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_state_sha256':input_sha,'complete_new_scope_input':incoming,
        'same_frozen_target_sha256':identity.target_sha256,
        'actual_reference_source_sha256':previous.SOURCE_SHA,'actual_reference_q_sha256':previous.SOURCE_Q_SHA,
        'actual_initial_response_identity':prior_final['actual_response_identity'],
        'new_centered_direction_source_and_policy_bound_before_model_identity':True,
        'frozen_original_modules_or_types_patched':False,
        'hard_tau_fixed_exactly_in_the_solver':1.,'complete_height_parameters':1473,'active_response_parameters':1472,
        'whole_original_work950_N256_and_fine1728_N512_retained':True,
        'original_reference_amp_H_and_every_paid_mouth_unchanged':True,
        'preceding_failure_all_costs_inherited_not_relabelled_as_new':True,
        'prior_complete_arrays_and_factors_not_fabricated_as_saved_workspace':True,
        'new_complete_direction_chain_and_scalar_schedule_bound_before_model_identity':True,
        'no_old_DtN_inner_Riccati_or_diagnostic_gate':True,
        'whole_reference_E_interval_contract_only_quantifies_true_cap_to_mouth':True,
        'continuous_fixed_E_metric_or_README_claim':False,
        'arguments':{key:value for key,value in vars(args).items() if key != 'source_state_json'}})
    try:
        model = chart.FourierCenteredHeight.restore_from_frozen_reference(driver,
            source['actual_1130q_JSON'],source['amplitude'],identity,incoming['maximum_independent_mode'],
            incoming['numerical_and_response_policy'],deadline=deadline,attempts=attempts)
        response = np.asarray(prior_final['actual_response'],dtype=float)
        if model.nq != 1473 or previous.response_identity(response) != prior_final['actual_response_identity']:
            raise ValueError('same actual failed hard-tau1 input was not retained')
        model.actual_checkpoint = {'response':response.copy(),'accepted_step':1,'damping':damping,
            'hard_tau':1.,'status':'actual_accepted_split_response_before_centered_direction_evaluation',
            'same_frozen_target_sha256':identity.target_sha256}
        model.pending_trial = model.last_trial = model.partial_readout = None
        contract = previous.conditional_source_contract(model,consumers)
        emit('TAIL_SOURCE_CONTRACT',{'literal_JSON':contract[0],'sha256':contract[1],
            'strict_source_error_consumer_selected':False,'all_seven_original_error_categories_unresolved':True,
            'E_interval_quantifies_only_whole_true_cap_to_mouth_not_body_or_core':True})
        data = model.prepare(model.original_work_radii,256)
        response,state,damping,summary = solve(model,response,data,args,chart,consumers,contract,solver_deadline,
            prior_final['actual_next_damping'],prior_final['actual_checkpoint']['accepted_step'])
        status = summary['status']
        readout = previous.fine_readout(model,response,args,chart,consumers,contract)
        emit('STAGE',{'summary':summary,'readout':readout,'actual_next_damping':damping,
            'same_frozen_target_sha256':identity.target_sha256})
    except (driver.weak.ScientificBudget,driver.paid.ScientificBudget,driver.high.HighModeBudget) as exc:
        status = 'declared_scientific_budget_actual_fixed_E_split_checkpoint'
        failure = {'type':type(exc).__name__,'message':str(exc)}
        emit('CLOCK',failure)
    except (driver.base.DomainError,ArithmeticError,ValueError,FloatingPointError,RuntimeError,
            TypeError,KeyError,AttributeError,MemoryError,np.linalg.LinAlgError) as exc:
        status = 'declared_fixed_E_split_model_or_numerical_failure_actual_checkpoint'
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
        'new_scope_counts':dict(COUNTS),'complete_row_QR_SVD_counts':dict(driver.factorization.COUNTS),
        'stable_coordinate_counts':dict(chart.stable.COUNTS),'split_reference_adapter_counts':dict(chart.COUNTS),
        'recent_split_scalar_receipts_and_complete_costs':chart.root_attempt_receipts(),
        'true_tail_producer_counts':dict(consumers.producer.COUNTS),
        'true_tail_bound_counts':dict(consumers.producer.bounds.COUNTS),
        'direct_position_counts':dict(consumers.direct.COUNTS),'rejections':dict(REJECTIONS),
        'original_reference_source_cost_not_counted_as_this_run':source['source_cost_ledger'],
        'every_earlier_reference_cost_ledger_not_counted_as_this_run':source['prior_cost_ledgers'],
        'preceding_complete_split_run_identity':{key:value for key,value in incoming['preceding_complete_split_run'].items()
            if key != 'literal_FINAL_JSON'},
        'preceding_complete_split_run_full_actual_receipt_not_counted_as_this_run':prior_final,
        'overlapping_counters_and_inherited_ledgers_are_not_disjoint_costs':True,
        'old_inner_DtN_or_diagnostic_gates_replayed':False,'fixed_E_or_tau_or_q_silently_changed':False,
        'all_original_work_fine_rows_and_all_full_singular_directions_retained':True,
        'decimal_coordinate_error_observation_not_a_source_or_continuous_root_certificate':True,
        'normalized_reference_center_offset_remain_split_through_output_and_direct_queries':True,
        'reference_or_trial_root_does_not_grant_nonround_tau1_solution_or_uniform_infinite_band_inverse':True,
        'whole_reference_E_interval_contract_only_quantifies_true_cap_to_mouth':True,
        'source_ODE_alias_mean_primitive_and_global_errors_not_defaulted_to_zero':True,
        'continuous_metric_curvature_reach_and_README_certified':False,
        'raw_arrays_artifacts_releases_or_git_writes':False}
    raw = json.dumps(final,sort_keys=True,separators=(',',':'),allow_nan=False)
    print('FIXED_E397_CENTERED_FINAL '+raw,flush=True)
    emit('FINAL_IDENTITY',{'JSON_bytes':len(raw.encode()),'sha256':hashlib.sha256(raw.encode()).hexdigest()})


if __name__ == '__main__':
    main()
