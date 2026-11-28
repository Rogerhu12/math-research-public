#!/usr/bin/env python3
"""True-tail and direct-position consumers for the actual hard-total-trace field.

The tail producer evaluates a named original inner-equivalent field.  Its
complete original receipt is retained.  A new receipt derives the hard-P
anchor from the exact common-cutoff identity, rather than renaming a model
or pretending the two fields agree outside the true tail.  Direct queries
consume the actual new field and its complete implicit mean chain.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
MODEL_SHA = 'a55832af74577a86e850905dc16c39997a4cd095aca23bcb5aa35e64e9798c62'
PRODUCER_SHA = '0fcbc3608dc7bb8c05285f1fea11e2416303867f9c961e3b712170d830942c0e'
DIRECT_SHA = 'c98a37dea266e4a0b1b42082641934de3d635066dd7630d2f4a83071724aa24d'


def _load(name, filename, digest):
    path = HERE / filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('source-bound hard-trace consumer differs: ' + filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


producer = _load('r618_hard_trace_original_tail_producer',
    'r618_current_model_tail_anchor_20261127.py', PRODUCER_SHA)
direct = _load('r618_hard_trace_original_direct_position',
    'r618_same_fixed_metric_direct_position_20261127.py', DIRECT_SHA)


def _require(model):
    module = sys.modules.get(type(model).__module__)
    path = HERE / 'r618_hard_total_trace_model_20261128.py'
    if (module is None or Path(module.__file__).resolve() != path.resolve()
            or hashlib.sha256(path.read_bytes()).hexdigest() != MODEL_SHA
            or type(model) is not module.HardTotalTraceHeight):
        raise ValueError('the actual declared hard-total-trace model is required')
    provenance = model.guard()
    chain = direct._bound_chain(model.original)
    if chain is not module.chain or model.split_chain.original_chain is not chain:
        raise ValueError('hard trace and original geometry must share the actual mean/position chain')
    return model.split_chain, provenance


def actual_tail_anchor(model, response, data, parameter_indices, *, source_contract_json,
        source_contract_sha256, require_source_errors_enclosed):
    """Derive a new anchor by exact equality on the ENTIRE true tail."""
    _, provenance = _require(model)
    indices = list(parameter_indices)
    identity = model._field_identity(response, data, include_angles=False)
    support = model.tail_support_identity(response, data, indices)
    original_response = model.inner_equivalent_response(response)
    original_data = model.original_data_view(data)
    original_result = producer.CurrentModelTailAnchor(model.original, original_response,
        original_data, indices, source_contract_json=source_contract_json,
        source_contract_sha256=source_contract_sha256,
        require_source_errors_enclosed=require_source_errors_enclosed).result()
    if (model.guard() != provenance
            or original_result['response_sha256'] != support['original_inner_equivalent_response_sha256']
            or original_result['response_model_sha256'] != model.owned.response_model_sha256):
        raise ValueError('the actual equal-tail fields changed during bound production')
    result = dict(original_result)
    result.update(target_sha256=model.identity.target_sha256,
        response_model_sha256=identity['response_model_sha256'],
        response_sha256=identity['response_sha256'],
        true_tail_evidence={'hard_total_trace_support_identity': support,
            'original_equal_tail_anchor_with_original_identity': original_result,
            'actual_hard_trace_provenance': provenance,
            'guarded_consumer_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'new_anchor_derived_by_same_function_on_declared_interval': True,
            'original_unknown_errors_not_assigned_zero': True},
        equal_tail_transfer_is_not_whole_field_identity=True)
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
        'unchanged_direct_position_source_sha256':DIRECT_SHA,'actual_hard_total_trace_provenance':provenance,
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
