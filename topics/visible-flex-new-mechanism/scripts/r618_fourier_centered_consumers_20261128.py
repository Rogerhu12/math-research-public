#!/usr/bin/env python3
"""Thin guarded consumers for the persistent split-reference R618 model.

The existing true-tail producer receives the actual unmodified original
model, whose policy already bound the adapter before its identity was made.
The direct readout reuses its existing query and stencil implementations;
only entry validation and scheduling select the explicit numerical wrapper.
No class name, model hash or previous result is re-labelled after arithmetic.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
CHART_SHA = 'fe1d8a07343152bc981a94cd00c311b826fc283afa1c6b020e9b7de59c04bda3'
PRODUCER_SHA = '0fcbc3608dc7bb8c05285f1fea11e2416303867f9c961e3b712170d830942c0e'
DIRECT_SHA = 'c98a37dea266e4a0b1b42082641934de3d635066dd7630d2f4a83071724aa24d'


def _load(name,filename,digest):
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('unchanged consumer source differs: '+filename)
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


producer = _load('r618_split_original_tail_producer',
    'r618_current_model_tail_anchor_20261127.py',PRODUCER_SHA)
direct = _load('r618_split_original_direct_position',
    'r618_same_fixed_metric_direct_position_20261127.py',DIRECT_SHA)


def _require(model):
    module = sys.modules.get(type(model).__module__)
    path = HERE/'r618_fourier_centered_model_20261128.py'
    if (module is None or Path(module.__file__).resolve() != path.resolve()
            or hashlib.sha256(path.read_bytes()).hexdigest() != CHART_SHA
            or type(model) is not module.FourierCenteredHeight):
        raise ValueError('the exact declared split-reference wrapper is required')
    provenance = model.guard()
    chain = direct._bound_chain(model.original)
    if chain is not module.chain or model.split_chain.original_chain is not chain:
        raise ValueError('split wrapper and original geometry must share the actual loaded chain')
    # Direct's existing query function accepts this explicit chain argument.
    # Its output geometry therefore preserves the Decimal split at every
    # new radius; no old module global or computed result is substituted.
    return model.split_chain,provenance


def actual_tail_anchor(model,response,data,parameter_indices,*,source_contract_json,
        source_contract_sha256,require_source_errors_enclosed):
    """All original coefficient summation/interval arithmetic is reused."""
    _,provenance = _require(model)
    result = producer.CurrentModelTailAnchor(model.original,response,data,parameter_indices,
        source_contract_json=source_contract_json,source_contract_sha256=source_contract_sha256,
        require_source_errors_enclosed=require_source_errors_enclosed).result()
    if model.guard() != provenance or result['response_model_sha256'] != provenance['response_model_sha256']:
        raise ValueError('actual chart/model identity changed during true-tail arithmetic')
    result['true_tail_evidence']['actual_numerical_chart_provenance'] = provenance
    result['true_tail_evidence']['guarded_consumer_source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


def same_fixed_metric_double_readout(model,response,fine_data,fine_state,*,query_block_radii=128):
    """Reuse the original exact query/stencil code after the new entry guard."""
    chain,provenance = _require(model)
    response = model._check_response(response).copy()
    identity = model._require_same_state(response,fine_data,fine_state)
    snapshot = direct._model_snapshot(model)
    r,theta = fine_data['r'],fine_data['theta']
    if (len(theta) < 512 or not np.all(np.isin(model.original_fine_radii,r))
            or type(query_block_radii) is not int or query_block_radii < 2):
        raise ValueError('every original fine radius, N>=512 and an explicit block>=2 are required')
    if any(fine_data[key].shape != (len(theta),len(theta))
           for key in ('primitive','derivative','second_derivative')):
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
    receipt = {'root_iterations':0,'floating_root_resolution_stops':0,
        'literal_reference_zero_entries':0,'output_mean_a_minus_one_observation':0.,
        'output_mean_R_alias_observation':0.,'output_Nyquist_a_minus_one_observation':0.,
        'output_Nyquist_R_observation':0.,'angular_closure_norm_observation':0.}
    direct.COUNTS['same_fixed_metric_double_readout_attempts'] += 1
    direct.COUNTS['already_computed_fine_positions_reused'] += len(r)
    direct.COUNTS['requested_stencil_position_rows_before_sharing'] += 10*len(r)
    direct.COUNTS['new_unique_stencil_position_rows'] += len(indices)
    for begin in range(0,len(indices),query_block_radii):
        chosen = indices[begin:begin+query_block_radii]
        all_Y[chosen] = direct._query_positions(model,response,all_r[chosen],fine_data,
                                               fine_state['core'],chain,receipt)
    reports = [direct._stencil_receipt(model,response,fine_data,fine_state,all_r,all_Y,*spec)
               for spec in specifications]
    if (model._require_same_state(response,fine_data,fine_state) != identity
            or direct._model_snapshot(model) != snapshot or model.guard() != provenance):
        raise ValueError('actual source/response/target/grid changed during direct readout')
    direct.COUNTS['same_fixed_metric_double_readouts_completed'] += 1
    return {**identity,'guarded_consumer_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'unchanged_direct_position_source_sha256':DIRECT_SHA,'actual_numerical_chart_provenance':provenance,
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
        'cumulative_direct_position_counts':dict(direct.COUNTS)}
