#!/usr/bin/env python3
"""First actual397 fixed-E growing-response solve, with hard core tau1.

This is a new declared model/scope, not a re-labelled ordinary continuation.
The complete actual397 reference q, H, amp, mouths and all prior costs stay
literal. Its whole continuous E definition is immutable. The nonzero input
has all response coefficients zero except hard tau1; no tau0 old diagnostic
is used as its qualification. Every original work/fine row is retained.
"""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SCHEMA = 'r618-actual397-fixed-E-growing-J48-hard-tau1-v1'
SOURCE_SHA = '79e6d6ce708687decd47fb8eb7a9668f8ca2ebf2351b2f3109fd571c6d692f9c'
SOURCE_Q_SHA = 'd76a590766b2323698053321ad84608f17f110c1711c105470d2b876b4920875'
FIELD_SHA = '12b2113d13bcc20f8c4813c4aac6e8fef6859eb4de7a1271f44770ca793bc952'
TARGET_SHA = '86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5'
COMPONENTS = {
    'original':('r613_full_position_height_20261127.py','6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0'),
    'identity':('r618_frozen_metric_branch_20261127.py','561432ec04021d9ed59e3d4207193cd53bdb08b0cd952d96faab1bd786143cc3'),
    'chart':('r618_stable_coordinate_model_20261127.py','0c69bc73cc19a75b13357a28baa8487f7a80c1df7e4ddaf5a32c8948cdbfcc34'),
    'consumers':('r618_stable_coordinate_consumers_20261127.py','13a49948d558da4050e556a4175a845652bd938c909a72694030069496c539f1')}
COUNTS = defaultdict(int)
REJECTIONS = defaultdict(int)


def emit(tag,value):
    print('FIXED_E397_'+tag+' '+json.dumps(value,sort_keys=True,separators=(',',':'),
                                           allow_nan=False),flush=True)


def bound_import(label):
    filename,digest = COMPONENTS[label]
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('fixed-E component differs: '+filename)
    spec = importlib.util.spec_from_file_location('r618_actual397_'+label,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read_input(args,identity_module):
    raw = sys.stdin.buffer.read() if args.source_state_json == '@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest() != args.source_state_sha256:
        raise ValueError('complete new fixed-E input identity differs')
    incoming = json.loads(raw)
    source_text,field_text = incoming['frozen_source_state_JSON'],incoming['mathematical_field_JSON']
    if (len(source_text.encode()) != 157609 or hashlib.sha256(source_text.encode()).hexdigest() != SOURCE_SHA
            or hashlib.sha256(field_text.encode()).hexdigest() != FIELD_SHA
            or field_text != (HERE.parent/'computations/r618-actual397-frozen-field-definition-20261127.json').read_text()):
        raise ValueError('the one actual397 source or complete fixed mathematical field changed')
    source = json.loads(source_text)
    qtext = source['actual_1130q_JSON']
    if (hashlib.sha256(qtext.encode()).hexdigest() != SOURCE_Q_SHA
            or len(qtext.encode()) != 22713 or source['global_accepted_iteration'] != 397
            or source['amplitude'] != 1e-5 or json.loads(qtext)[0] != .5188903877153482
            or source['origin']['run_id'] != 45899589237 or source['origin']['job_id'] != 140181814100):
        raise ValueError('actual completed397 reference differs')
    identity = identity_module.FrozenTargetIdentity.bind(source_text,SOURCE_SHA,field_text,FIELD_SHA)
    if identity.target_sha256 != TARGET_SHA:
        raise ValueError('the frozen complete target identity changed')
    if (incoming['maximum_independent_mode'] != 48 or incoming['hard_core_tau'] != 1.
            or incoming['initial_response_definition'] != 'all1473_entries_zero_except_tau_equals_one'
            or incoming['new_operator_initial_damping'] != 1e-8):
        raise ValueError('declared genuine nonzero fixed stage changed')
    return incoming,source,identity,hashlib.sha256(raw).hexdigest()


def response_identity(response):
    raw = json.dumps(np.asarray(response,dtype=float).tolist(),separators=(',',':'),allow_nan=False)
    return {'JSON_bytes':len(raw.encode()),'sha256':hashlib.sha256(raw.encode()).hexdigest(),
        'count':int(len(response)),'l2_norm_observation':float(np.linalg.norm(response)),
        'maximum_absolute_entry':float(np.max(abs(response)))}


def conditional_source_contract(model,consumers):
    """Actual reconstruction observations, NEVER invented strict enclosures.

    The intervals only enclose the actual floating observed normalization.
    Every source-to-exact-germ error remains explicitly unresolved. The true
    tail consequence is conditional on exact source inputs falling inside
    these intervals; this function does not assert that missing proposition.
    """
    def observed(value):
        value = float(value)
        if not math.isfinite(value):
            raise ArithmeticError('nonfinite actual source normalization')
        return {'lo':math.nextafter(value,-math.inf),'hi':math.nextafter(value,math.inf)}
    definition = json.loads(model.identity.mathematical_field_json)
    p = model.old.old
    contract = {'schema':'actual397-source-bound-conditional-normalization-observations-v1',
        'target_sha256':model.identity.target_sha256,'response_model_sha256':model.response_model_sha256,
        'reconstruction_source_sha256':model.original_reconstruction_receipt['reconstruction_source_sha256'],
        'true_inner_definition_sha256':consumers.producer.json_sha(definition['accurate_inner_tail_definition']),
        'true_germ_choice':'same_R600_accurate_infinite_germs_with_all_source_errors_accounted',
        'original_inner_phase':0,
        'old_germ_normalizations':{str(int(mode.mode)):{'display_log':observed(mode.flat.display_log),
            'core_A_abs':observed(abs(mode.Acore))} for mode in model.old.modes},
        'old_envelope_and_force_normalizations':{
            'mode_height_scales':[observed(v) for v in p.mode_height_scales],
            'envelope_scale':observed(p.envelope_scale),
            'force_tail_multiplier':observed(p.forced.tail_multiplier),'force_scale':observed(p.forced.scale)},
        'physical_R':{'lo':'0.85','hi':'0.85'},'physical_alpha':{'lo':'0.55','hi':'0.55'},
        'whole_reference_E_lower_bound':{'lo':'0.99','hi':'0.99'},
        'whole_reference_E_upper_bound':{'lo':'1.01','hi':'1.01'},
        'source_error_accounting':{key:{'status':'unresolved',
            'evidence':'This actual scope only observes the reconstructed floating normalization; '
            'the literal source/current cost ledger retains '+key+' as unpaid. '
            'No bound for this source error is set to zero.'}
            for key in consumers.producer.ERROR_CATEGORIES},
        'actual_floating_observation_intervals_are_not_exact_source_error_enclosures':True,
        'strict_consumer_would_reject_this_contract':True}
    raw = json.dumps(contract,sort_keys=True,separators=(',',':'),allow_nan=False)
    return raw,hashlib.sha256(raw.encode()).hexdigest()


def anchor(model,response,data,consumers,contract):
    return consumers.actual_tail_anchor(model,response,data,(),source_contract_json=contract[0],
        source_contract_sha256=contract[1],require_source_errors_enclosed=False)


def anchor_summary(value):
    box = value['true_tail_evidence']['whole_continuous_mean_branch']
    return {'target_sha256':value['target_sha256'],'response_model_sha256':value['response_model_sha256'],
        'response_sha256':value['response_sha256'],'cap_radius':value['cap_radius'],
        'mouth_radius':value['mouth_radius'],'parameter_indices':value['parameter_indices'],
        'integral_and_directions':value['integral_and_directions'],
        'absolute_error_bounds_or_unresolved_radii':value['absolute_error_bounds_or_unresolved_radii'],
        'conditional_whole_tail_mean_branch':box,'unresolved_errors':value['unresolved_errors'],
        'all_tail_input_errors_enclosed':value['all_tail_input_errors_enclosed'],
        'conditional_exact_source_interval_consequence':value['conditional_exact_source_interval_consequence'],
        'unknown_original_source_errors_assigned_zero':False}


def field_report(model,response,data,state):
    r,theta = data['r'],data['theta']
    eta = np.stack([p['eta'] for p in state['positions']])
    R = np.stack([v['R'] for v in state['output_states']])
    ei = np.unravel_index(int(np.argmax(eta)),eta.shape)
    co,si = data['complete_position_projection']
    cosine = np.sqrt(2)*(state['S'][:,:,0]@co.T)
    sine = np.sqrt(2)*(state['S'][:,:,1]@si.T)
    core = state['core']
    return {'same_frozen_target_sha256':model.identity.target_sha256,
        'response_model_sha256':model.response_model_sha256,'response_identity':response_identity(response),
        'fixed_reference_H':float(model.q_reference[0]),'fixed_amplitude':model.amplitude,
        'hard_tau':float(response[model.tau_index]),
        'complete_S_merit':float(state['residual']@state['residual']/2),
        'conditional_S_identity_eta':float(eta[ei]),
        'conditional_eta_attainer_r_theta':[float(r[ei[0]]),float(theta[ei[1]])],
        'Darboux_R_max_observation':float(np.max(abs(R))),
        'position_odd_modes':data['all_position_odd_modes'].tolist(),
        'position_cosine_max_by_mode':np.max(abs(cosine),axis=0).tolist(),
        'position_sine_max_by_mode':np.max(abs(sine),axis=0).tolist(),
        'N_min':float(min(np.min(v['N']) for v in state['output_states'])),
        'u_min':float(min(np.min(v['u']) for v in state['output_states'])),
        'b_over_r_min':float(min(np.min(v['b'])/rr for rr,v in zip(r,state['output_states']))),
        'conditional_outward_ratio_min':float(min(np.min(v['outward_ratio']) for v in state['positions'])),
        'output_mean_a_minus_one_max':state['max_abs_output_mean_a_minus_one_observation'],
        'output_mean_R_max':state['max_abs_output_mean_R_alias_observation'],
        'output_Nyquist_a_minus_one_max':state['max_abs_output_Nyquist_a_minus_one_observation'],
        'output_Nyquist_R_max':float(max(abs(v['output_Nyquist_R_observation']) for v in state['positions'])),
        'mean_functional_points':int(model.policy['mean_points']),
        'minimum_abs_scaled_mean_coefficient':float(min(abs(v['mean_derivative']/v['target']['W'])
                                                        for v in state['mean_states'])),
        'core':{'tau':core['tau'],'P0_cosine_coefficients':core['pc'].tolist(),
            'all_P1_coefficients':core['P1_coeff'].tolist(),'all_dependent_modes':model.core_modes.tolist(),
            'complete_D_max':core['complete_core_D_observation'],
            'full_tau_identity_difference':core['full_tau_core_identity_difference_observation'],
            'original_j2_core_amplitude_unchanged':core['original_j2_core_amplitude_unchanged'],
            'tau_equals_one_target_core_map_selected':core['tau_equals_one_target_core_map_selected'],
            'current_e':core['e'],'current_effective_e_r':core['effective_e_r'],
            'fixed_e':core['fixed_e'],'fixed_e_r':core['fixed_e_r'],
            'zeta':float(core['zeta']),'zeta_r':float(core['zeta_r']),
            'core_root_and_roundoff_enclosed':False},
        'radial_points':int(len(r)),'angular_points':int(len(theta)),
        'all_original_observation_rows_retained':True,'S_identity_not_actual_metric_qualification':True,
        'continuous_fixed_E_metric_or_README_certificate':False}


def checkpoint(model,response,data,state,step,damping,status,tail_anchor):
    report = field_report(model,response,data,state)
    model.actual_checkpoint = {'response':response.copy(),'accepted_step':step,'damping':damping,
        'status':status,'hard_tau':1.,'same_frozen_target_sha256':model.identity.target_sha256}
    report.update(accepted_step=step,actual_next_damping=damping,status=status,
        actual_response=response.tolist(),true_tail_anchor=anchor_summary(tail_anchor))
    emit('COMPLETE_STATE',report)
    return report


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
    for index,r in enumerate(data['r']):
        model.driver.check(model.deadline)
        mean = state['mean_states'][index]
        dm = chart.chain.mean_direction(mean,{k:v[index,:,None] for k,v in Hm.items()})
        ds = chart.chain.output_direction(state['output_states'][index],
                {k:v[index,:,None] for k,v in Ho.items()},dm)
        for key,name in (('b','relative_b'),('u','relative_u'),('N','relative_N')):
            changes[name] = max(changes[name],float(np.max(abs(ds[key][:,0])/state['output_states'][index][key])))
        width = mean['target']['stable_reference_coordinate_box']['coordinate_halfwidth']
        margin = width-abs(mean['x'])
        if margin <= 0:
            raise ArithmeticError('actual same-root state reached the original coordinate box boundary')
        dx = abs(float(dm['s'][0])/mean['coordinate_scale'])
        changes['reference_coordinate_fraction'] = max(changes['reference_coordinate_fraction'],dx/margin)
    changes['height'] = float(np.max(abs(Ho['f'])))
    changes['height_theta_over_r'] = float(np.max(abs(Ho['ft'])/data['r'][:,None]))
    changes['height_r_over_1_W'] = float(np.max(abs(Ho['fr'])/(1+data['frozen_W'][:,None])))
    maximum = max(changes.values())
    if not np.isfinite(maximum):
        raise ArithmeticError('nonfinite actual function direction observation')
    factor = min(1.,.1/maximum) if maximum > 0 else 1.
    COUNTS['new_complete_function_direction_limits'] += 1
    return factor,{'linearized_complete_field_changes':changes,
        'factor':factor,'not_a_nonlinear_or_continuous_domain_certificate':True,
        'hard_tau_direction_exactly_zero':True}


def solve(model,response,data,args,chart,consumers,contract,solver_deadline):
    response = response.copy();damping = 1e-8
    tail = anchor(model,response,data,consumers,contract)
    state = model.evaluate(response,data)
    report = checkpoint(model,response,data,state,0,damping,'new_hard_tau1_input_evaluated_on_complete_work_mesh',tail)
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
            lam = damping*10.**trial
            direction = np.r_[reduction.direction(lam),0.]
            COUNTS['new_fixed_E_model_directions'] += 1
            try:
                factor,measures = function_step_limit(model,direction,data,state,chart)
            except (ArithmeticError,ValueError) as exc:
                REJECTIONS['function_direction:'+str(exc)] += 1
                COUNTS['function_direction_rejections'] += 1
                continue
            direction *= factor
            for cut in range(9):
                model.driver.check(model.deadline)
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
                    emit('ACCEPTANCE',{'iteration':iteration,'accepted_step':accepted_steps,
                        'trial':trial,'fraction':fraction,'function_factor':factor,'function_measures':measures,
                        'damping_before':old_damping,'lambda_used':lam,'actual_next_damping':damping,
                        'actual_decrease':actual,'predicted_decrease':predicted,'actual_over_predicted':ratio,
                        'spectrum':spectrum,'same_frozen_target_sha256':model.identity.target_sha256,
                        'hard_tau':1.,'source_H_and_amplitude_unchanged':True})
                    report = checkpoint(model,response,data,state,accepted_steps,damping,
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


def fine_coefficient_and_D_observations(model,response,data,state):
    fields = model.coefficient_fields(response,data,state)
    V,L,modes = fields['pre_tanh_threejet_coefficients'],fields['all_post_tanh_threejet_coefficients'],fields['all_post_modes']
    r,theta = data['r'],data['theta'];D = np.stack([s['D'] for s in state['output_states']])
    harmonics = []
    for j in range(0,len(theta)//2+1,2):
        values = (1 if j in (0,len(theta)//2) else 2)*np.mean(D*np.cos(j*theta)[None,:],axis=1)
        index = int(np.argmax(abs(values)))
        harmonics.append({'mode':j,'maximum_absolute_D_coefficient':float(abs(values[index])),
            'signed_coefficient':float(values[index]),'radius':float(r[index])})
    rows = []
    for rho in model.driver.majorant.RHOS:
        model.driver.check(model.deadline)
        pre = [model.driver.majorant._norm(V[:,:,k],np.arange(2,9,2),rho) for k in range(3)]
        post = [model.driver.majorant._norm(L[:,:,k],modes,rho) for k in range(3)]
        post_theta = [model.driver.majorant._norm(L[:,:,0],modes,rho,order) for order in (1,2)]
        rows.append({'rho':rho,'maximum_pre_tanh_threejet_Wiener_norms':[float(np.max(a)) for a in pre],
            'maximum_complete_post_threejet_Wiener_norms':[float(np.max(a)) for a in post],
            'maximum_complete_post_first_second_angular_norms':[float(np.max(a)) for a in post_theta]})
        COUNTS['new_full_fixed_E_coefficient_rho_radial_points'] += len(r)
    C = np.stack([s['C'] for s in state['output_states']]);M = np.stack([s['M'] for s in state['output_states']])
    cosine = np.cos(model.modes[:,None]*theta)
    mass = np.einsum('rt,it,jt->rij',C/M,cosine,cosine)/len(theta)
    mass_reports = []
    for label,part in (('all_original_2_through_22',mass[:,:11,:11]),('all_independent_2_through_48',mass)):
        eigen = np.linalg.eigvalsh(part);ab = abs(eigen)
        relative = np.min(ab,axis=1)/np.maximum(np.max(ab,axis=1),1e-300)
        worst = int(np.argmin(relative))
        mass_reports.append({'modes':label,'worst_radius':float(r[worst]),
            'minimum_relative_absolute_eigenvalue':float(relative[worst]),
            'worst_eigenvalues':eigen[worst].tolist(),'pointwise_C_not_divided':True,
            'continuous_rank_certificate':False})
    COUNTS['new_full_fixed_E_coefficient_radial_points'] += len(r)
    COUNTS['new_same_field_mass_eigenvalue_points'] += 2*len(r)
    COUNTS['new_actual_D_coefficients_observed'] += len(harmonics)*len(r)
    tail = model.exact_tail_source_observation(data)
    numerical_zero = (data['r'] < model.tail_left)&(data['analytic_tail_columns'][:,0,0] == 0)
    return {'all_complete_D_harmonics_through_output_Nyquist':harmonics,
        'all_post_modes_including_every_dependent_2J_mode':modes.tolist(),
        'complete_V_and_L_threejet_coefficient_norm_observations':rows,
        'same_current_field_original_and_expanded_mass_observations':mass_reports,
        'actual_pointwise_C_min':float(np.min(C)),'actual_pointwise_C_max':float(np.max(C)),
        'all_actual_tail_L_j_columns_shape':list(tail['L_j_columns'].shape),
        'maximum_absolute_supplied_tail_L_j_by_mode_and_degree':np.max(abs(tail['L_j_columns']),axis=0).tolist(),
        'inner_tail_float_value_zero_radii_observation':int(np.sum(numerical_zero)),
        'true_tail_not_replaced_by_these_numerical_zeros':True,
        'unresolved_errors':fields['unresolved_errors']+['two_primitive_and_angular_closure_errors',
            'fixed_reference_E_and_implicit_mean_s_angular_error_budget'],
        'old_variable_E_R615_root_shift_observer_not_applied_to_fixed_E':True,
        'no_fixed_E_angular_or_radial_certificate_claimed':True}


def fine_readout(model,response,args,chart,consumers,contract):
    data = model.prepare(model.original_fine_radii,512)
    state = model.evaluate(response,data)
    report = field_report(model,response,data,state)
    model.partial_readout = {'stage':'complete_fine_fixed_E_state','fine':report}
    emit('FINE',model.partial_readout)
    coefficients = fine_coefficient_and_D_observations(model,response,data,state)
    model.partial_readout['coefficient_observations'] = coefficients
    emit('COEFFICIENTS',coefficients)
    direct = consumers.same_fixed_metric_double_readout(model,response,data,state,query_block_radii=128)
    model.partial_readout['direct_position'] = direct
    emit('DIRECT_POSITION',direct)
    tail = anchor(model,response,data,consumers,contract)
    model.partial_readout['true_tail_anchor'] = tail
    emit('TRUE_TAIL_ANCHOR',tail)
    mean = model.integrate_mean_height(response,data,tail)
    geometry = model.geometry_with_mean_height(response,data,state,mean)
    X = geometry['X'];Z = X[:,:,2]
    physical = {'sampled_anchored_height_min':float(np.min(Z)),
        'sampled_anchored_ball_radius_max':float(np.max(np.linalg.norm(X,axis=2))),
        'mean_height_offset_range':[float(np.min(mean['mean_height_offset'])),float(np.max(mean['mean_height_offset']))],
        'central_column_translation_and_reflection_center_offset':mean['central_column_translation_and_reflection_center_offset'],
        'body_mean_height_quad_error_estimate_observation':mean['quad_error_estimate_observation'],
        'true_tail_anchor_summary':anchor_summary(tail),'physical_definition_uses_true_cap_anchor':True,
        'all_mean_root_tail_body_quad_and_roundoff_errors_enclosed':False,
        'whole_closed_surface_embedding_reach_or_time_motion_certified':False}
    okay = (response[model.tau_index] == 1. and report['conditional_S_identity_eta'] <= args.target_eta
        and physical['sampled_anchored_height_min'] > 0
        and all(direct[key]['direct_reconstructed_metric_eta'] <= args.target_eta
                and direct[key]['direct_position_outward_ratio_min'] > 0
                for key in ('direct_step','direct_half_step')))
    result = {'fine':report,'coefficient_observations':coefficients,'direct_position':direct,
        'true_tail_anchor':tail,'anchored_height_observations':physical,
        'fine_fixed_E_metric_observation_passed':bool(okay),
        'conditional_exact_source_inputs_not_continuous_error_certificate':True,
        'whole_surface_metric_curvature_reach_or_README_certified':False}
    model.partial_readout = {'stage':'all_declared_fine_and_anchored_height_readouts_complete','complete':result}
    return result


def original_costs(driver):
    return {'base':dict(driver.base.COUNTS),'forced':dict(driver.paid.NEW_COUNTS),
        'complete_height':dict(driver.complete.COUNTS),'compact':dict(driver.compact.NEW),
        'full_spectrum':dict(driver.full.NEW),'factored':dict(driver.high.COUNTS),
        'paid_mouth':dict(driver.resume.NEW),'old_weak':dict(driver.weak.COUNTS),
        'function':dict(driver.parent.EXTRA),'gain':dict(driver.base.gain.COUNTS),
        'coefficient':dict(driver.majorant.COUNTS),'old_position':dict(driver.position.COUNTS)}


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
    driver,identity_module,chart,consumers = [bound_import(key) for key in ('original','identity','chart','consumers')]
    incoming,source,identity,input_sha = read_input(args,identity_module)
    started = time.monotonic();deadline = started+args.maximum_seconds
    solver_deadline = deadline-args.final_reserve_seconds
    model = response = summary = readout = None
    damping = 1e-8;attempts = [];failure = None
    status = 'actual397_frozen_reference_before_necessary_complete_reconstruction'
    emit('DEFINITION',{'schema':SCHEMA,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source_state_sha256':input_sha,'complete_new_scope_input':incoming,
        'same_frozen_target_sha256':identity.target_sha256,
        'actual_reference_source_sha256':SOURCE_SHA,'actual_reference_q_sha256':SOURCE_Q_SHA,
        'actual_initial_response_definition':incoming['initial_response_definition'],
        'new_hard_tau1_is_a_new_physical_state_not_old_tau0_qualification':True,
        'hard_tau_fixed_exactly_in_the_solver':1.,'complete_height_parameters':1473,'active_response_parameters':1472,
        'whole_original_work950_N256_and_fine1728_N512_retained':True,
        'complete_working_position_odd_modes':list(range(1,128,2)),
        'new_independent_even_post_modes':list(range(2,49,2)),
        'all_dependent_core_modes':list(range(2,97,2)),
        'original_reference_amp_H_and_every_paid_mouth_unchanged':True,
        'all_source_and_prior_cost_ledgers_included_literally':True,
        'new_DtN_inner_Riccati_or_old_diagnostic_gate':False,
        'continuous_fixed_E_metric_or_README_claim':False,
        'arguments':{k:v for k,v in vars(args).items() if k != 'source_state_json'}})
    try:
        model = chart.StableCoordinateHeight.restore_from_frozen_reference(driver,
            source['actual_1130q_JSON'],source['amplitude'],identity,incoming['maximum_independent_mode'],
            incoming['numerical_and_response_policy'],deadline=deadline,attempts=attempts)
        response = model.initial_response();response[model.tau_index] = 1.
        if model.nq != 1473:
            raise ValueError('declared full growing response count differs')
        model.actual_checkpoint = {'response':response.copy(),'accepted_step':0,'damping':damping,
            'hard_tau':1.,'status':'actual_new_hard_tau1_input_before_its_first_physical_evaluation',
            'same_frozen_target_sha256':identity.target_sha256}
        model.pending_trial = model.last_trial = model.partial_readout = None
        contract = conditional_source_contract(model,consumers)
        emit('TAIL_SOURCE_CONTRACT',{'literal_JSON':contract[0],'sha256':contract[1],
            'strict_source_error_consumer_selected':False,'all_seven_original_error_categories_unresolved':True})
        data = model.prepare(model.original_work_radii,256)
        response,state,damping,summary = solve(model,response,data,args,chart,consumers,contract,solver_deadline)
        status = summary['status']
        readout = fine_readout(model,response,args,chart,consumers,contract)
        emit('STAGE',{'summary':summary,'readout':readout,'actual_next_damping':damping,
            'same_frozen_target_sha256':identity.target_sha256})
    except (driver.weak.ScientificBudget,driver.paid.ScientificBudget,driver.high.HighModeBudget) as exc:
        status = 'declared_scientific_budget_actual_fixed_E_checkpoint'
        failure = {'type':type(exc).__name__,'message':str(exc)}
        emit('CLOCK',failure)
    except (driver.base.DomainError,ArithmeticError,ValueError,FloatingPointError,RuntimeError,
            TypeError,KeyError,AttributeError,MemoryError,np.linalg.LinAlgError) as exc:
        status = 'declared_fixed_E_model_or_numerical_failure_actual_checkpoint'
        failure = {'type':type(exc).__name__,'message':str(exc)}
        emit('FAILURE',failure)
    actual = pending = None
    if model is not None and hasattr(model,'actual_checkpoint'):
        kept = model.actual_checkpoint;response = kept['response'].copy();damping = kept['damping']
        actual = {k:v for k,v in kept.items() if k != 'response'}
        if model.pending_trial is not None:
            pending = {k:(v.tolist() if isinstance(v,np.ndarray) else v) for k,v in model.pending_trial.items()}
    final = {'schema':SCHEMA,'status':status,'failure':failure,'elapsed_seconds':time.monotonic()-started,
        'same_frozen_target_sha256':identity.target_sha256,'reference_source_sha256':SOURCE_SHA,
        'reference_q_sha256':SOURCE_Q_SHA,'reference_H':.5188903877153482,'reference_amplitude':1e-5,
        'actual_response':None if response is None else response.tolist(),
        'actual_response_identity':None if response is None else response_identity(response),
        'actual_next_damping':damping,'actual_checkpoint':actual,'pending_trial_not_accepted':pending,
        'last_trial':None if model is None else getattr(model,'last_trial',None),
        'summary':summary,'readout':readout,'partial_readout':None if model is None else getattr(model,'partial_readout',None),
        'paid_high_reconstruction_attempts':driver.full.attempt_receipts(attempts),
        'actual_model_cost_receipt':None if model is None else model.cumulative_cost_receipt(),
        'original_module_counters_including_failed_reconstruction':original_costs(driver),
        'growing_height_counts_including_failed_construction':dict(chart.height.COUNTS),
        'fixed_metric_chain_counts_including_failed_construction':dict(chart.chain.COUNTS),
        'new_scope_counts':dict(COUNTS),'complete_row_QR_SVD_counts':dict(driver.factorization.COUNTS),
        'stable_coordinate_counts':dict(chart.COUNTS),'true_tail_producer_counts':dict(consumers.producer.COUNTS),
        'true_tail_bound_counts':dict(consumers.producer.bounds.COUNTS),
        'direct_position_counts':dict(consumers.direct.COUNTS),'rejections':dict(REJECTIONS),
        'source_cost_not_counted_as_this_run':source['source_cost_ledger'],
        'every_prior_cost_ledger_not_counted_as_this_run':source['prior_cost_ledgers'],
        'overlapping_counters_not_disjoint_costs':True,'old_inner_DtN_or_diagnostic_gates_replayed':False,
        'later_normal_q_or_H_did_not_change_this_E':True,
        'source_ODE_alias_mean_primitive_and_global_errors_not_defaulted_to_zero':True,
        'hard_tau1_failure_not_silently_softened':True,
        'static_small_amplitude_fixed_E_not_macro_README_completion':True,
        'continuous_metric_curvature_reach_and_README_certified':False,
        'raw_arrays_artifacts_releases_or_git_writes':False}
    raw = json.dumps(final,sort_keys=True,separators=(',',':'),allow_nan=False)
    print('FIXED_E397_FINAL '+raw,flush=True)
    emit('FINAL_IDENTITY',{'JSON_bytes':len(raw.encode()),'sha256':hashlib.sha256(raw.encode()).hexdigest()})


if __name__ == '__main__':
    main()
