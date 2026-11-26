#!/usr/bin/env python3
"""Two original direct-position stencils of one actual fixed-E response.

The complete original fine mesh is retained. All supplemental radial
queries use the SAME frozen target, reference branch, canonical512 height
and fixed mean functional. They do not call the old variable-E geometry.
Queries shared by the two stencils are evaluated once and every actual
query, root, original field evaluation and failure remains in the ledger.

This is a numerical position/curvature readout for a declared public scope,
not a continuous or interval certificate. In particular no S-to-eta identity
is substituted for differentiation of the actual reconstructed planar Y.
The additive cap-anchored mean-height constant cancels from these jets;
this does NOT certify that anchor or the full closed surface's reach.
"""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
HEIGHT_SHA = '87fdb14d80d12836c6328d3adf83abfc020300e468da43b3ebfffe4bdc6409e2'
CHAIN_SHA = '0668d1afbcdcd5e0c0c16d3784c322d6e0bba3639c547d8ae0bd42900ff09815'
COUNTS = defaultdict(int)


def _json_sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
                                     allow_nan=False).encode()).hexdigest()


def _bound_chain(model):
    module = sys.modules.get(type(model).__module__)
    path = HERE/'r618_growing_post_fixed_metric_height_20261127.py'
    if (module is None or Path(module.__file__).resolve() != path.resolve()
            or hashlib.sha256(path.read_bytes()).hexdigest() != HEIGHT_SHA):
        raise ValueError('the exact complete source-bound growing model is required')
    chain = module.chain
    if (Path(chain.__file__).resolve() != (HERE/'r618_fixed_metric_numerical_chain_20261127.py').resolve()
            or hashlib.sha256(Path(chain.__file__).read_bytes()).hexdigest() != CHAIN_SHA):
        raise ValueError('the same loaded stable fixed-E numerical chain is required')
    chain.public_only()
    return chain


def _model_snapshot(model):
    return _json_sha({'target':model.identity.target_sha256,
        'response_model':model.response_model_sha256,'policy':model.policy,
        'reference_q':model.q_reference.tolist(),'amplitude':model.amplitude,
        'modes':model.modes.tolist(),'core_modes':model.core_modes.tolist(),
        'tail_degrees':model.tail_degrees.tolist(),
        'tail_shape':[model.tail_left,model.tail_right,model.tail_denominator],
        'core_lift':[model.core_lift_left,model.core_lift_right],
        'original_reconstruction':model.original_reconstruction_receipt})


def _original_cache_receipts(model,radii):
    key = (radii.tobytes(),4)
    caches,seen = [],set()
    current = model.old
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        if hasattr(current,'cache'):
            caches.append((current.cache,key,key in current.cache))
        current = getattr(current,'old',None)
    canonical_key = (radii.tobytes(),model.amplitude)
    caches.append((model.old.canonical_mean_cache,canonical_key,
                   canonical_key in model.old.canonical_mean_cache))
    return caches


def _root_observation(receipt,mean,position):
    chart = mean['chart']
    row = receipt.setdefault('maximum_scaled_root_residual_by_chart',{})
    row[chart] = max(row.get(chart,0.),abs(float(mean['root_value'])))
    row = receipt.setdefault('minimum_absolute_mean_derivative_by_chart',{})
    row[chart] = min(row.get(chart,float('inf')),abs(float(mean['mean_derivative'])))
    record = mean['root_receipt']
    receipt['root_iterations'] += int(record.get('iterations',0))
    receipt['floating_root_resolution_stops'] += int(record.get('floating_step_resolution_reached',False))
    receipt['literal_reference_zero_entries'] += int(record.get('exact_same_reference_definition_used',False))
    for name in ('output_mean_a_minus_one_observation','output_mean_R_alias_observation',
                 'output_Nyquist_a_minus_one_observation','output_Nyquist_R_observation'):
        receipt[name] = max(receipt[name],abs(float(position[name])))
    receipt['angular_closure_norm_observation'] = max(receipt['angular_closure_norm_observation'],
        float(np.linalg.norm(position['angular_closure_observation'])))


def _query_positions(model,response,radii,fine_data,trace,chain,receipt):
    """Only extra position queries; original observation rows are untouched.

    N4 is used solely to obtain the unchanged radial dictionaries. Neither
    its angular quadrature nor its primitive is used for a geometric value.
    The actual mean and position matrices are explicitly restored below.
    """
    model.driver.check(model.deadline)
    radii = np.asarray(radii,dtype=float)
    if len(radii) == 0 or np.any(np.diff(radii) <= 0):
        raise ValueError('ordered nonempty supplemental radius block required')
    requested = radii
    if len(radii) == 1:
        partner = np.nextafter(radii[0],model.par.R)
        if partner >= model.par.R:
            partner = np.nextafter(radii[0],model.minimum)
        radii = np.sort(np.r_[radii,partner])
    if np.any(radii < model.minimum) or np.any(radii >= model.par.R):
        raise ValueError('supplemental direct-position query leaves the same numerical field')
    caches = _original_cache_receipts(model,radii)
    try:
        COUNTS['new_direct_position_query_blocks_attempted'] += 1
        radial = dict(model.compact.CompactResponseHeight.prepare(model.old,radii,4))
        model._complete_radial_data(radial)
        mean_data = model._angular_view(radial,int(model.policy['mean_points']))
        output_data = model._angular_view(radial,len(fine_data['theta']))
        if not np.array_equal(output_data['theta'],fine_data['theta']):
            raise ValueError('supplemental positions must use the identical retained angular grid')
        output_data['primitive'] = fine_data['primitive']
        mean_jets = model.height_jets(response,mean_data,trace)
        if np.array_equal(mean_data['theta'],output_data['theta']):
            output_jets = mean_jets
            COUNTS['same_grid_mean_height_evaluations_reused'] += 1
        else:
            output_jets = model.height_jets(response,output_data,trace)
        positions = np.empty((len(radii),len(fine_data['theta']),2))
        zero = bool(np.all(response == 0))
        for index,r in enumerate(radii):
            model.driver.check(model.deadline)
            target = model._target(mean_data,index)
            mean = model._mean_state(target,{k:v[index] for k,v in mean_jets.items()},literal_zero=zero)
            state = chain.state_on_output_grid(mean,{k:v[index] for k,v in output_jets.items()})
            position = chain.position_state(state,output_data['theta'],output_data['primitive'])
            positions[index] = position['Y']
            _root_observation(receipt,mean,position)
            COUNTS['new_direct_position_actual_radial_queries'] += 1
            COUNTS['new_direct_position_actual_radial_angular_points'] += len(output_data['theta'])
        if not np.all(np.isfinite(positions)):
            raise ArithmeticError('nonfinite same-field supplemental position')
        COUNTS['new_direct_position_query_blocks_completed'] += 1
        return positions[np.searchsorted(radii,requested)]
    finally:
        # Delete only these new query caches; old work/fine caches and every
        # counter survive both successful and failed attempts.
        for cache,key,preexisting in caches:
            if not preexisting:
                cache.pop(key,None)


def _stencil_receipt(model,response,data,state,all_r,all_Y,factor,shifted,h,centered):
    r,theta = data['r'],data['theta']
    Y = np.stack([position['Y'] for position in state['positions']])
    differences = [all_Y[np.searchsorted(all_r,values)]-Y for values in shifted]
    d0,d1,d2,d3,d4 = differences
    hc = h[:,None,None]
    center_r = (d0-8*d1+8*d2-d3)/(12*hc)
    center_rr = (-d0+16*d1+16*d2-d3)/(12*hc**2)
    forward_r = (48*d0-36*d1+16*d2-3*d3)/(12*hc)
    forward_rr = (-154*d0+214*d1-156*d2+61*d3-10*d4)/(12*hc**2)
    Yr = np.where(centered[:,None,None],center_r,forward_r)
    Yrr = np.where(centered[:,None,None],center_rr,forward_rr)
    Yt = np.stack([Y[:,:,k]@data['derivative'].T for k in range(2)],axis=2)
    Yrt = np.stack([Yr[:,:,k]@data['derivative'].T for k in range(2)],axis=2)
    Ytt = np.stack([Y[:,:,k]@data['second_derivative'].T for k in range(2)],axis=2)
    p = np.stack([value['p'] for value in state['output_states']])
    p0r = np.asarray([value['p0_r'] for value in state['output_states']])
    height = state['height_jets']
    Xr = np.concatenate([Yr,p[:,:,None]],axis=2)
    Xt = np.concatenate([Yt,height['ft'][:,:,None]],axis=2)
    Xrr = np.concatenate([Yrr,(p0r[:,None]+height['frr'])[:,:,None]],axis=2)
    Xrt = np.concatenate([Yrt,height['frt'][:,:,None]],axis=2)
    Xtt = np.concatenate([Ytt,height['ftt'][:,:,None]],axis=2)
    normal = np.cross(Xr,Xt)
    norm = np.linalg.norm(normal,axis=2)
    if np.any(norm <= 0) or not np.all(np.isfinite(norm)):
        raise ArithmeticError('actual direct-position tangent plane is unresolved')
    normal /= norm[:,:,None]
    E,F,G = (np.sum(Xr*Xr,axis=2),np.sum(Xr*Xt,axis=2),np.sum(Xt*Xt,axis=2))
    l,m,n = (np.sum(normal*second,axis=2) for second in (Xrr,Xrt,Xtt))
    det = E*G-F*F
    if np.any(det <= 0) or not np.all(np.isfinite(det)):
        raise ArithmeticError('actual direct-position first form is unresolved')
    twiceH = (l*G-2*m*F+n*E)/det
    K = (l*n-m*m)/det
    raw_disc = twiceH*twiceH-4*K
    disc = np.maximum(0.,raw_disc)
    kp,km = (twiceH+np.sqrt(disc))/2,(twiceH-np.sqrt(disc))/2
    kabs = np.maximum(abs(kp),abs(km))
    Efixed = np.asarray([value['target']['E'] for value in state['output_states']])[:,None]
    rr = r[:,None]
    e,f,gg = E/Efixed-1,F/(rr*np.sqrt(Efixed)),G/(rr*rr)-1
    eta = (abs(e+gg)+np.sqrt((e-gg)**2+4*f*f))/2
    if not np.all(np.isfinite(eta)) or not np.all(np.isfinite(kabs)):
        raise ArithmeticError('nonfinite actual direct-position metric or curvature')
    ei = np.unravel_index(int(np.argmax(eta)),eta.shape)
    ki = np.unravel_index(int(np.argmax(kabs)),kabs.shape)
    identity_Yr = np.stack([position['Yr'] for position in state['positions']])
    difference = abs(Yr-identity_Yr)
    di = np.unravel_index(int(np.argmax(difference)),difference.shape)
    JT = np.stack([position['JT'] for position in state['positions']])
    u = np.stack([value['u'] for value in state['output_states']])
    outward = -np.sum(Yr*JT,axis=2)/u
    COUNTS['same_fixed_metric_direct_stencils_completed'] += 1
    COUNTS['same_fixed_metric_direct_stencil_centered_rows'] += int(np.sum(centered))
    COUNTS['same_fixed_metric_direct_stencil_forward_rows'] += int(np.sum(~centered))
    return {'direct_reconstructed_metric_eta':float(eta[ei]),
        'metric_attainer_r_theta':[float(r[ei[0]]),float(theta[ei[1]])],
        'metric_attainer_h':float(h[ei[0]]),
        'metric_attainer_stencil':'centered' if centered[ei[0]] else 'forward',
        'absolute_curvature_max':float(kabs[ki]),
        'curvature_attainer_r_theta':[float(r[ki[0]]),float(theta[ki[1]])],
        'curvature_attainer_h':float(h[ki[0]]),
        'minimum_raw_principal_discriminant_observation':float(np.min(raw_disc)),
        'direct_position_outward_ratio_min':float(np.min(outward)),
        'Yr_identity_vs_position_difference':float(np.max(difference)),
        'Yr_difference_attainer_r_theta_component':[float(r[di[0]]),float(theta[di[1]]),int(di[2])],
        'Yr_difference_attainer_h':float(h[di[0]]),
        'conditional_S_identity_eta_on_same_nodes':state['conditional_eta_identity_observation'],
        'angular_G_relative_defect':float(np.max(abs(gg))),
        'h_min':float(np.min(h)),'h_max':float(np.max(h)),'factor':factor,
        'centered_r_count':int(np.sum(centered)),'forward_r_count':int(np.sum(~centered)),
        'same_original_r_count':int(len(r)),'theta_nodes':int(len(theta)),
        'first_original_r_retained':float(r[0]),'last_original_r_retained':float(r[-1]),
        'first_r_h':float(h[0]),'last_r_h':float(h[-1]),
        'stencil_Y_minus_Y0_before_linear_combination':True,
        'centered_first_and_second_formal_order':4,'forward_first_and_second_formal_order':4,
        'planar_position_differentiated_height_analytic_jets':True,
        'same_reference_E_not_redefined_from_trial':True,
        'additive_cap_height_translation_cancels_from_this_jet_readout':True,
        'cap_mean_integral_or_closed_surface_reach_certified':False,
        'continuous_or_interval_metric_curvature_reach_certificate':False}


def same_fixed_metric_double_readout(model,response,fine_data,fine_state,*,query_block_radii=128):
    """Mandatory original h and h/2, sharing only identical actual queries.

    Caller passes its already-computed final complete fine state. There is
    no initial paid diagnostic or science gate and no duplicate fine solve.
    The returned scope identity is the identity consumed before any query.
    """
    chain = _bound_chain(model)
    response = model._check_response(response).copy()
    identity = model._require_same_state(response,fine_data,fine_state)
    snapshot = _model_snapshot(model)
    r,theta = fine_data['r'],fine_data['theta']
    if (len(theta) < 512 or not np.all(np.isin(model.original_fine_radii,r))
            or type(query_block_radii) is not int or query_block_radii < 2):
        raise ValueError('every original fine radius, N>=512 and an explicit block>=2 are required')
    if (fine_data['primitive'].shape != (len(theta),len(theta))
            or fine_data['derivative'].shape != (len(theta),len(theta))
            or fine_data['second_derivative'].shape != (len(theta),len(theta))):
        raise ValueError('all three actual retained angular matrices are required')
    specifications = []
    for factor in (1.,.5):
        h = factor*np.minimum(2e-5,.002*(model.par.R-r))
        centered = r-2*h>model.minimum
        if np.any(h <= 0) or np.any(r < model.minimum) or np.any(r+5*h >= model.par.R):
            raise ValueError('original direct-position stencil leaves the defined field')
        shifted = [r+np.where(centered,c,f)*h
            for c,f in zip((-2.,-1.,1.,2.,0.),(1.,2.,3.,4.,5.))]
        specifications.append((factor,shifted,h,centered))
    all_r = np.unique(np.concatenate([r]+[x for _,shifted,_,_ in specifications for x in shifted]))
    all_Y = np.empty((len(all_r),len(theta),2))
    base_indices = np.searchsorted(all_r,r)
    all_Y[base_indices] = np.stack([position['Y'] for position in fine_state['positions']])
    missing = np.ones(len(all_r),dtype=bool);missing[base_indices] = False
    indices = np.flatnonzero(missing)
    trace = fine_state['core']
    receipt = {'root_iterations':0,'floating_root_resolution_stops':0,
        'literal_reference_zero_entries':0,'output_mean_a_minus_one_observation':0.,
        'output_mean_R_alias_observation':0.,'output_Nyquist_a_minus_one_observation':0.,
        'output_Nyquist_R_observation':0.,'angular_closure_norm_observation':0.}
    COUNTS['same_fixed_metric_double_readout_attempts'] += 1
    COUNTS['already_computed_fine_positions_reused'] += len(r)
    COUNTS['requested_stencil_position_rows_before_sharing'] += 10*len(r)
    COUNTS['new_unique_stencil_position_rows'] += len(indices)
    for begin in range(0,len(indices),query_block_radii):
        chosen = indices[begin:begin+query_block_radii]
        all_Y[chosen] = _query_positions(model,response,all_r[chosen],fine_data,trace,chain,receipt)
    reports = [_stencil_receipt(model,response,fine_data,fine_state,all_r,all_Y,*spec)
               for spec in specifications]
    if (model._require_same_state(response,fine_data,fine_state) != identity
            or _model_snapshot(model) != snapshot):
        raise ValueError('the actual source/response/target/grid changed during direct position readout')
    COUNTS['same_fixed_metric_double_readouts_completed'] += 1
    return {**identity,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_model_snapshot_sha256':snapshot,'direct_step':reports[0],'direct_half_step':reports[1],
        'supplemental_position_root_and_alias_observations':receipt,
        'retained_fine_radii':int(len(r)),'retained_angle_nodes':int(len(theta)),
        'all_unique_positions_including_retained_fine':int(len(all_r)),
        'additional_unique_positions':int(len(indices)),
        'same_complete_fine_state_consumed_without_replay':True,
        'original_work_and_fine_observation_rows_not_replaced_by_query_mesh':True,
        'same_mean_functional_at_all_supplemental_radii':int(model.policy['mean_points']),
        'all_same_target_mean_root_angular_primitive_finite_difference_and_source_errors_enclosed':False,
        'actual_continuous_metric_or_README_certified':False,
        'cumulative_direct_position_counts':dict(COUNTS)}
