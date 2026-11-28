#!/usr/bin/env python3
"""Actual R643 full-field, fixed-seed-height and actual-position consumers.

Both stencil sizes differentiate the SAME new normalized periodic Y.
Mean-height quadrature evaluates the original fixed seed scalar, then adds
the actual explicit mean function. It does not integrate an invented new
implicit trial root. Every numerical error remains explicitly unresolved.
"""
from collections import defaultdict
import hashlib
import importlib.util
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
MODEL_SHA = '91944d7298d81952a28c09b416db1242d5d913fc43b8d19ea97fbab5c38b8185'
DIRECT_SHA = 'c98a37dea266e4a0b1b42082641934de3d635066dd7630d2f4a83071724aa24d'
COUNTS = defaultdict(int)


def _load_direct():
    path = HERE/'r618_same_fixed_metric_direct_position_20261127.py'
    if hashlib.sha256(path.read_bytes()).hexdigest()!=DIRECT_SHA:
        raise RuntimeError('the original actual-position stencil formulas changed')
    spec = importlib.util.spec_from_file_location('r643_unchanged_actual_position_stencils',path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


direct = _load_direct()


def _module(model):
    module = sys.modules.get(type(model).__module__)
    path = HERE/'r643_complete_mean_height_model_20261128.py'
    if (module is None or Path(module.__file__).resolve()!=path.resolve()
            or hashlib.sha256(path.read_bytes()).hexdigest()!=MODEL_SHA
            or type(model) is not module.CompleteMeanHeight):
        raise ValueError('the actual complete1566-column mean model is required')
    model.guard()
    return module


def complete_observation(model,response,data,state):
    _module(model)
    model._require(response,data,state)
    r,theta = data['r'],data['theta']
    eta = np.stack([p['eta'] for p in state['positions']])
    i,j = np.unravel_index(int(np.argmax(eta)),eta.shape)
    F,G = state['F'],state['G']
    fi,gi = int(np.argmax(abs(F))),int(np.argmax(abs(r*G)))
    core = state['core']
    result = {
        'joint_model_sha256':model.model_sha256,
        'same_frozen_target_sha256':model.identity.target_sha256,
        'response_sha256':state['response_sha256'],
        'all_actual_rows':len(state['residual']),'all_actual_free_columns':model.nq,
        'all_mean_columns':model.mean_count,'all_original_angular_free_columns':model.old_free,
        'complete_joint_merit':float(state['residual']@state['residual']/2),
        'conditional_complete_S_eta':float(eta[i,j]),
        'conditional_eta_attainer_r_theta':[float(r[i]),float(theta[j])],
        'actual_canonical_F_max':float(abs(F[fi])),
        'actual_F_attainer_r':float(r[fi]),
        'actual_canonical_rG_max':float(abs(r[gi]*G[gi])),
        'actual_rG_attainer_r':float(r[gi]),
        'N_min':min(float(np.min(s['N'])) for s in state['output_states']),
        'u_min':min(float(np.min(s['u'])) for s in state['output_states']),
        'b_over_r_min':min(float(np.min(s['b'])/rr) for s,rr in zip(state['output_states'],r)),
        'actual_height_mean_change_max':float(np.max(abs(state['mean_change'][:,0]))),
        'actual_height_mean_slope_change_max':float(np.max(abs(state['mean_change'][:,1]))),
        'actual_height_mean_second_change_max':float(np.max(abs(state['mean_change'][:,2]))),
        'canonical_normalization_min':min(float(s['A']) for s in state['mean_states']),
        'output_minus_canonical_mean_a_max':max(abs(p['output_minus_canonical_mean_a_observation']) for p in state['positions']),
        'output_minus_canonical_mean_R_max':max(abs(p['output_minus_canonical_mean_R_observation']) for p in state['positions']),
        'output_Nyquist_a_minus_one_max':max(abs(p['output_Nyquist_a_minus_one_observation']) for p in state['positions']),
        'output_Nyquist_R_max':max(abs(p['output_Nyquist_R_observation']) for p in state['positions']),
        'closure_velocity_mean_max':max(float(np.linalg.norm(p['angular_closure_observation'])) for p in state['positions']),
        'outward_ratio_min':min(float(np.min(p['outward_ratio'])) for p in state['positions']),
        'fixed_reference_H':float(model.q_reference[0]),'fixed_amplitude_unit':model.amplitude,
        'hard_tau':1.,'core_P0_coefficients':core['pc'].tolist(),
        'core_P1_all_coefficients':core['P1_coeff'].tolist(),
        'core_D_max_observation':float(core['complete_core_D_observation']),
        'core_mean_zeta':float(core['zeta']),'core_mean_zeta_r':float(core['zeta_r']),
        'work_or_fine_role':data['joint_grid_role'],
        'radial_points':len(r),'angular_points':len(theta),
        'canonical_mean_points':len(data['fixed_mean_data']['theta']),
        'first_last_original_r':[float(r[0]),float(r[-1])],
        'trial_mean_root_or_lambda_coordinate_gate':False,
        'new_complete_position_identity_and_F_G_do_not_close_continuous_error':True,
        'README_or_continuous_metric_certified':False}
    COUNTS['complete_joint_observations'] += 1
    return result


def _original_cache_records(model,radii):
    key = (radii.tobytes(),4)
    answer,seen = [],set()
    owner = model.old
    while owner is not None and id(owner) not in seen:
        seen.add(id(owner))
        if hasattr(owner,'cache'):
            answer.append((owner.cache,key,key in owner.cache))
        owner = getattr(owner,'old',None)
    canonical = (radii.tobytes(),model.amplitude)
    answer.append((model.old.canonical_mean_cache,canonical,canonical in model.old.canonical_mean_cache))
    return answer


def _drop_only_new(records):
    for cache,key,existed in records:
        if not existed:
            cache.pop(key,None)


def _query_positions(model,response,radii,fine_data):
    module = _module(model)
    radii = np.unique(np.asarray(radii,dtype=float))
    requested = radii.copy()
    if len(radii)==1:
        neighbor = np.nextafter(radii[0],model.par.R)
        if neighbor >= model.par.R:
            neighbor = np.nextafter(radii[0],model.minimum)
        radii = np.unique(np.r_[radii,neighbor])
    if np.any(radii<model.minimum) or np.any(radii>=model.par.R):
        raise ValueError('same-field supplemental query leaves the numerical domain')
    records = _original_cache_records(model,radii)
    try:
        radial = dict(model.compact.CompactResponseHeight.prepare(model.old,radii,4))
        model.owned._complete_radial_data(radial)
        data = model.owned._angular_view(radial,len(fine_data['theta']))
        mean_data = model.owned._angular_view(radial,int(model.owned.policy['mean_points']))
        for key in ('primitive','derivative','second_derivative',
                    'complete_position_projection','all_position_odd_modes'):
            data[key] = fine_data[key]
        data['fixed_mean_data'] = mean_data
        data['position_radial_units'] = np.full(len(radii),1/np.sqrt(len(radii)))
        data['response_model_sha256'] = model.owned.response_model_sha256
        data['joint_model_sha256'] = model.model_sha256
        data['joint_grid_role'] = 'supplemental_actual_position_query'
        data['mean_dictionary'] = model._mean_dictionary(data)
        state = model.evaluate(response,data)
        answer = np.stack([position['Y'] for position in state['positions']])
        COUNTS['new_actual_query_radial_points'] += len(radii)
        COUNTS['new_actual_query_angular_points'] += len(radii)*len(data['theta'])
        COUNTS['new_actual_query_blocks_completed'] += 1
        return answer[np.searchsorted(radii,requested)]
    finally:
        _drop_only_new(records)


def two_actual_position_stencils(model,response,data,state,*,query_block_radii=128):
    _module(model)
    model._require(response,data,state)
    r,theta = data['r'],data['theta']
    if (len(theta)<512 or not np.all(np.isin(model.original_fine_radii,r))
            or type(query_block_radii) is not int or query_block_radii<2):
        raise ValueError('same complete fine data and a real query batch required')
    definitions = []
    for factor in (1.,.5):
        h = factor*np.minimum(2e-5,.002*(model.par.R-r))
        centered = r-2*h>model.minimum
        if np.any(h<=0) or np.any(r+5*h>=model.par.R):
            raise ValueError('original actual-position stencil leaves the defined field')
        shifted = [r+np.where(centered,c,f)*h
                   for c,f in zip((-2.,-1.,1.,2.,0.),(1.,2.,3.,4.,5.))]
        definitions.append((factor,shifted,h,centered))
    all_r = np.unique(np.concatenate([r]+[row for _,nodes,_,_ in definitions for row in nodes]))
    all_Y = np.empty((len(all_r),len(theta),2))
    base = np.searchsorted(all_r,r)
    all_Y[base] = np.stack([p['Y'] for p in state['positions']])
    missing = np.ones(len(all_r),dtype=bool);missing[base] = False
    indices = np.flatnonzero(missing)
    COUNTS['complete_two_stencil_readouts_attempted'] += 1
    COUNTS['already_paid_full_fine_positions_reused'] += len(r)
    COUNTS['original_stencil_query_rows_before_sharing'] += 10*len(r)
    COUNTS['new_unique_actual_position_query_rows'] += len(indices)
    for first in range(0,len(indices),query_block_radii):
        model.check()
        chosen = indices[first:first+query_block_radii]
        COUNTS['new_actual_query_blocks_attempted'] += 1
        all_Y[chosen] = _query_positions(model,response,all_r[chosen],data)
    reports = [direct._stencil_receipt(model,response,data,state,all_r,all_Y,*definition)
               for definition in definitions]
    model._require(response,data,state)
    COUNTS['complete_two_stencil_readouts_completed'] += 1
    return {
        'joint_model_sha256':model.model_sha256,
        'same_target_sha256':model.identity.target_sha256,
        'actual_response_sha256':state['response_sha256'],
        'direct_step':reports[0],'direct_half_step':reports[1],
        'unchanged_stencil_formula_source_sha256':DIRECT_SHA,
        'same_normalized_periodic_actual_Y_at_all_queries':True,
        'same_real_free_mean_function_and_all_original_fine_points':True,
        'all_unique_positions':len(all_r),'new_unique_positions':len(indices),
        'complete_cost_counts':dict(COUNTS),'reused_stencil_helper_counts':dict(direct.COUNTS),
        'mean_height_integral_not_needed_for_these_true_local_derivatives':True,
        'continuous_metric_reach_or_README_certified':False}


def _seed_scalar(model,r):
    """Actual needed fixed seed s/s_r, reusing every already paid query."""
    r = float(r)
    if r in model.seed_mean_cache:
        COUNTS['already_paid_fixed_seed_scalar_queries_reused'] += 1
        record = model.seed_mean_cache[r]
        return record['s'],record['s_r']
    if not model.minimum<=r<model.par.R:
        raise ValueError('true seed scalar is only numerically evaluated above its original mouth')
    neighbor = np.nextafter(r,model.par.R)
    if neighbor>=model.par.R:
        neighbor = np.nextafter(r,model.minimum)
    radii = np.sort(np.asarray([r,neighbor]))
    index = int(np.searchsorted(radii,r))
    records = _original_cache_records(model,radii)
    try:
        radial = dict(model.compact.CompactResponseHeight.prepare(model.old,radii,4))
        model.owned._complete_radial_data(radial)
        mean_data = model.owned._angular_view(radial,int(model.owned.policy['mean_points']))
        jets = model.owned.height_jets(model.seed_response,mean_data,model.seed_trace)
        target = model.owned._target(mean_data,index)
        model.check()
        COUNTS['new_fixed_seed_height_integrand_queries_attempted'] += 1
        value = model.owned._mean_state(target,{key:row[index] for key,row in jets.items()})
        record = {key:value[key] for key in
                  ('target','x_decimal','chart','s','s_r','s_r_decimal','root_receipt')}
        model.seed_mean_cache[r] = record
        COUNTS['new_fixed_seed_height_integrand_queries_completed'] += 1
        return record['s'],record['s_r']
    finally:
        _drop_only_new(records)


def complete_actual_mean_height(model,response,data,state,paid_seed_anchor):
    """The same true seed integral, evaluated by a new shared Hermite rule.

    Every body endpoint scalar/derivative has already been paid. One actual
    midpoint per span supplies the refined rule and its coarse/fine
    difference. The singular core endpoint is integrated separately with
    the original genuine seed scalar. Neither numerical estimate is an
    interval error bound; the actual integral definition is unchanged.
    """
    _module(model)
    model._require(response,data,state)
    r = np.asarray(data['r'])
    if (not np.all(np.isin(model.original_fine_radii,r))
            or paid_seed_anchor['response_sha256']!=model.policy['seed_response_sha256']
            or paid_seed_anchor['target_sha256']!=model.identity.target_sha256
            or paid_seed_anchor['mouth_radius']!=float(r[0])):
        raise ValueError('same full fine grid and the actual paid true seed cap anchor required')
    key = r.tobytes()
    if key in model.seed_mean_height_cache:
        seed = model.seed_mean_height_cache[key]
        COUNTS['same_actual_seed_height_integrals_reused'] += 1
    else:
        initial = float(paid_seed_anchor['integral_and_directions'][0])
        tail_radius = float(paid_seed_anchor['absolute_error_bounds_or_unresolved_radii'][0])
        offsets = np.empty(len(r));offsets[0] = initial
        coarse_fine_difference = 0.
        def hermite(a,b,sa,sra,sb,srb):
            h = b-a
            return h*(sa+sb)/2+h*h*(sra-srb)/12
        for i,(a,b) in enumerate(zip(r[:-1],r[1:])):
            model.check()
            sa,sra = _seed_scalar(model,a)
            sb,srb = _seed_scalar(model,b)
            mid = float(a+(b-a)/2)
            sm,srm = _seed_scalar(model,mid)
            coarse = hermite(a,b,sa,sra,sb,srb)
            refined = hermite(a,mid,sa,sra,sm,srm)+hermite(mid,b,sm,srm,sb,srb)
            offsets[i+1] = offsets[i]+refined
            coarse_fine_difference += abs(refined-coarse)
            COUNTS['actual_seed_height_Hermite_body_spans'] += 1
        delta = model.par.R-float(r[-1])
        power = 1/(1-model.par.alpha)
        def core_integrand(x):
            model.check()
            if x<=0:
                return 0.
            distance = delta*x**power
            radius = model.par.R-distance
            if radius>=model.par.R:
                COUNTS['core_mean_query_rounding_to_exact_endpoint_observations'] += 1
                return 0.
            s,_ = _seed_scalar(model,radius)
            return delta*power*x**(power-1)*s
        core_value,core_error = quad(core_integrand,0.,1.,
            epsabs=float(model.owned.policy['mean_height_epsabs']),
            epsrel=float(model.owned.policy['mean_height_epsrel']),
            limit=int(model.owned.policy['quadrature_limit']))
        seed = {'mean_height_offset':offsets,
                'central_mean_offset':float(offsets[-1]+core_value),
                'true_cap_anchor_absolute_error_bound_conditional_on_old_source':tail_radius,
                'sum_body_Hermite_coarse_fine_differences_observation':float(coarse_fine_difference),
                'core_integral_value_observation':float(core_value),
                'core_quad_error_estimate_observation':float(core_error),
                'finite_M_Cauchy_ODE_mean_root_alias_roundoff_and_full_quadrature_error_enclosed':False,
                'true_continuous_seed_integral_definition_unchanged':True}
        model.seed_mean_height_cache[key] = seed
    offset = seed['mean_height_offset']+state['mean_change'][:,0]
    center = seed['central_mean_offset']+model.amplitude*float(response[-1])
    dh = model.q_reference[0]-model.par.gain_height
    href = data['h0']+dh*data['gain_height']
    Z = href[:,None]+offset[:,None]+state['height_jets']['f']
    Y = np.stack([p['Y'] for p in state['positions']])
    centered_Z = Z-center
    ball = np.sqrt(np.sum(Y*Y,axis=2)+centered_Z**2)
    p = np.stack([s['p'] for s in state['output_states']])
    Yr = np.stack([position['Yr'] for position in state['positions']])
    Yt = np.stack([position['Yt'] for position in state['positions']])
    q = state['height_jets']['ft']
    Xr,Xt = np.dstack([Yr,p]),np.dstack([Yt,q])
    normal = np.cross(Xr,Xt)
    size = np.linalg.norm(normal,axis=2)
    if np.any(size<=0):
        raise ArithmeticError('explicit-mean field has a zero observed tangent plane')
    normal /= size[:,:,None]
    reach = float(model.par.reach_budget) if hasattr(model.par,'reach_budget') else .063
    margin = centered_Z-model.par.core_height-reach*abs(normal[:,:,2])
    at = np.unravel_index(int(np.argmax(ball)),ball.shape)
    mi = np.unravel_index(int(np.argmin(margin)),margin.shape)
    COUNTS['complete_actual_free_mean_height_consumers'] += 1
    return {
        'joint_model_sha256':model.model_sha256,
        'same_target_sha256':model.identity.target_sha256,
        'actual_response_sha256':state['response_sha256'],
        'true_fixed_seed_integral_receipt':{k:v for k,v in seed.items() if k!='mean_height_offset'},
        'actual_common_reflection_center_offset':float(center),
        'actual_mean_offset_range':[float(np.min(offset)),float(np.max(offset))],
        'observed_whole_upper_ball_about_actual_center':float(ball[at]),
        'ball_attainer_r_theta':[float(r[at[0]]),float(data['theta'][at[1]])],
        'observed_upper_height_above_actual_center_min':float(np.min(centered_Z)),
        'observed_p_max':float(np.max(p)),
        'normal_tangent_ball_height_margin_observation':float(margin[mi]),
        'normal_height_margin_attainer_r_theta':[float(r[mi[0]]),float(data['theta'][mi[1]])],
        'normal_height_margin_uses_finite_identity_jets_not_continuous_certificate':True,
        'original_held_top_cap_kept_by_true_mean_anchor':True,
        'central_column_length_unchanged_and_reflection_center_not_silently_zero':True,
        'all_original_fine_rows_retained':True,
        'whole_surface_ball_reach_or_README_certified':False,
        'complete_consumer_counts':dict(COUNTS)}
