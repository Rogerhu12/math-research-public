#!/usr/bin/env python3
"""Complete analytic six-control normal-frame angular jets.

Differentiate the actual six working Rodrigues coefficient functions and
the actual T/Tphi/Tphiphi expressions. Each of the six control columns is
integrated in the original complete _total order. Active upstream edges
are retained. The original complete reverse-product frame is the optional
numerical fallback. No root, stage, angle, variable, row or point is removed.
Scientific evaluation is public repository Actions only.
"""
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import time
import textwrap

import numpy as np
import torch

SCHEMA = 'complete-closure-value-compatible-analytic-six-control-working-normal-frame-angular-jets-v1'
ENDPOINT_SCHEMA = 'complete-fixed-fejer-r726-detached-meridian-normal-layer-v1'
BASE_SOURCE_SHA256 = 'bb045b437c8b56407104262b77700710fe1a02b2f1a72e6f57683732e146ee37'
PARENT_NORMAL_SOURCE_SHA256 = '04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e'
ORIGINAL_FRAME_AST_SHA256 = 'ee015776b374f6cdcf2711b49e2d25e5cfe78b38b3f7d3886d8596a21b1b0cfc'
TORCH_VERSION = '2.5.1'
CLOSURE_VALUE_SOURCE_SHA256 = '6e35743a4bcff082b65054006dbcccf37783ffc9659416c345279678fee442b3'
METHOD_AST = {'_W': 'f37123850c51d2081d6f25a53b08408f19e6d8ea53f0b8ee889f5851dd6d3eda', '_total': 'd402e15c2849dc6b238951e278c0b2f16de8b18fe0e89bc795eb70e127a4b267', '_corrected_jets': '790531cf61834d1d4cfbf13f8d6ef4ecb6c5b98a016eeb308d90e96905ab6f13', '_closure_jets': '4a090400bd08ab21907cbeb348703c7070a272ae9450eb86921f12c576b43582', '_normal_frame_jets': '458f00cb02abc6d279cd4e45feedc21d3e3f34f9168dd497d1f090ad1bc2a8f5', '_stage_control_jets': '4a6fc8c940be13fee6faa738e6defff2a8c8c2457f04f8209ebc53fd44e21c8c', '_stage_constraints': '804cc04a7a4f374c96607793a0601e2144b27804ca10391e59f8f219094adaf4', '_stage_jet_jacobian': '7006f94d073979e9530625fa4325f24127bf8895319b20a5e4f9991fc0b63880', '_run_chain': '66d0674866dd8d68eb62b6161379dc329d2d5be67ec84fe2a81e3752547da73c', '_get_roots': '7bbe362ba1eda9c973ebc34c7c67d5e3e53b6dc073a5d16ca78e722f73d3e554', '_implicit_jet_value': '8b2bb1407c327f454637695f483f4d52dd3ef051f82c47a572b20d482a63ad6c', '_meridian_data': 'e5244b9fc2e68bee33692e76f7e5aa09422564d1b38bd59cf146646bc8530e9e'}
COUNTER_KEYS = (
    'frame_calls_started', 'frame_calls_returned', 'frame_calls_failed',
    'requested_angle_blocks', 'requested_angle_jets',
    'order0_requests', 'order1_requests', 'order2_requests',
    'active_graph_requests', 'detached_value_requests',
    'analytic_attempts', 'analytic_returns', 'analytic_failures',
    'analytic_angle_blocks_returned', 'analytic_angle_jets_returned',
    'analytic_control_columns_started', 'analytic_control_columns_returned',
    'analytic_total_calls_started', 'analytic_total_calls_returned',
    'analytic_total_angle_vectors_requested', 'analytic_total_angle_vectors_returned',
    'actual_coefficient_value_calls', 'actual_coefficient_derivative_calls',
    'ad_fallback_attempts', 'ad_fallback_returns', 'ad_fallback_failures',
    'ad_fallback_angle_blocks_returned', 'ad_fallback_angle_jets_returned',
    'ad_reverse_products_started', 'ad_reverse_products_returned',
    'ad_reverse_angle_products_started', 'ad_reverse_angle_products_returned',
    'actual_closure_jet_angle_evaluations', 'actual_frame_reverse_angle_products')
OBSERVED_COUNTER_KEYS = ('closure_jet_angle_evaluations', 'frame_reverse_angle_products')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific analytic normal frames require public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def _ast_value(value):
    if isinstance(value, ast.AST):
        return [type(value).__name__, [[name, _ast_value(item)]
            for name, item in ast.iter_fields(value)
            if not (name == 'type_params' and item == [])]]
    if isinstance(value, list):
        return [_ast_value(item) for item in value]
    if value is Ellipsis:
        return {'python_literal': 'Ellipsis'}
    if isinstance(value, bytes):
        return {'python_bytes_hex': value.hex()}
    return value


def _digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(letter in '0123456789abcdef' for letter in value))


def _copy(value):
    return json.loads(json.dumps(value, allow_nan=False))


METHOD_SOURCE_OVERRIDES = {"_closure_jets": "    def _closure_jets(self, controls, data, order):\n        return self.detached_closure_values.value(controls, data, order)\n", "_closure_jets_original": "    def _closure_jets_original(self, controls, data, order):\n        corrected = self._corrected_jets(data['meridians'],data['W'],controls,order)\n        names = ('T','Tp','Tpp')\n        self.normal_counts['closure_jet_angle_evaluations'] += len(controls)\n        return torch.stack(tuple(((data['core'][j]-data['reference_core'][j])\n            -(data['cap'][j]-data['reference_cap'][j])\n            +self._total(corrected[names[j]]-data['reference'][names[j]]))/self.S\n            for j in range(order+1)),dim=1)\n", "_run_chain": "    def _run_chain(self, data, keys, order, existing=None):\n        \"\"\"One common finite chain; an order-two upgrade keeps every old value/first jet.\"\"\"\n        if order not in (1,2) or len(keys) != len(data['core'][0]):\n            raise ValueError('Use every actual angle and the complete requested angular order')\n        if existing is not None and (order != 2 or len(existing) != len(keys)\n                or any(item['order'] != 1 for item in existing)):\n            raise ValueError('Only an actual cached first-jet branch may be upgraded')\n        entry_environment = self.detached_closure_values.entry_environment()\n        count = len(keys)\n        self._last_normal_batch = dict(schema='actual-complete-fixed-normal-plane-batch-v1',\n            current_full_point_sha256=self._current_point_sha256,angle_count=count,\n            material_angles_binary64_hex=list(keys),requested_angular_order=order,\n            same_branch_jet_upgrade=existing is not None,\n            normal_stage_count=self.normal_stage_count,\n            exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],\n            completed_stage_count=0,all_original_endpoint_equations_checked=False,\n            auxiliary_nodes_are_README_physical_flex=False,\n            complete_continuous_branch_certified=False,stages=[])\n        log = self._last_normal_batch\n        all_stages = []\n        frame_context = self.adjacent_frames.frame_context(data,keys,order)\n        with torch.no_grad(), self.detached_closure_values.scope(\n                data, keys, order, entry_environment) as closure_values, (\n                self.frame_c1.value_scope(data,keys,order)) as frame_values, (\n                self.stage_matrices.scope(data,keys,order,'returned_value_J3')\n                if existing is None else nullcontext()) as stage_matrices:\n            previous = torch.zeros((count,3,CONTROL_DIMENSION),dtype=torch.float64)\n            zero = torch.zeros((count,3,3),dtype=torch.float64)\n            zero[:,:order+1] = self._closure_jets(previous,data,order)\n            if existing is not None:\n                zero[:,:2] = tensor(np.stack([item['zero'][:2] for item in existing]))\n            if not bool(torch.isfinite(zero).all()):\n                self._fail('Nonfinite original zero-control closure jets')\n            for index in range(1,self.normal_stage_count+1):\n                tau = self.normal_step_carriers[index]\n                closure_values.progress(\"normal_stage_frame\", stage_index=index)\n                frame = torch.zeros((count,3,3,CONTROL_DIMENSION),dtype=torch.float64)\n                frame[:,:order+1] = frame_values.frame(previous,index-1)\n                old_stage = None if existing is None else [item['stages'][index-1] for item in existing]\n                if old_stage is not None:\n                    frame[:,:2] = tensor(np.stack([item['frame'][:2] for item in old_stage]))\n                if not bool(torch.isfinite(frame).all()):\n                    self._fail('Nonfinite complete preceding normal frame',\n                        normal_stage_index=index,state=previous[:,0])\n                frame_provenance = self.adjacent_frames.capture_frame_inputs(\n                    frame_context,previous,frame,index-1,old_stages=old_stage)\n                closure_values.progress(\"normal_stage_root\", stage_index=index)\n                if old_stage is None:\n                    eta,success,records = self._solve_stage(data,previous,frame,zero,tau,index)\n                else:\n                    eta = tensor(np.stack([item['eta'][0] for item in old_stage]))\n                    success = torch.ones(count,dtype=torch.bool)\n                    records = [dict(local_angle_index=j,successful=True,\n                        reused_original_value_and_first_jet=True,\n                        original_stage_record=old_stage[j]['record']) for j in range(count)]\n                stage_record = dict(normal_stage_index=index,\n                    exact_auxiliary_node=str(self.normal_step_nodes[index]),\n                    actual_auxiliary_node_hex=float(tau).hex(),\n                    same_branch_jet_upgrade=old_stage is not None,angle_records=records)\n                log['stages'].append(stage_record)\n                if not bool(success.all()):\n                    control = self._stage_control_jets(previous,frame,eta[:,None],0)[:,0]\n                    self._fail('A declared fixed normal plane did not return every original stage equation',\n                        normal_stage_index=index,angles=torch.nonzero(~success).flatten().tolist(),\n                        state=control,incremental_state=eta)\n                if old_stage is None:\n                    try:\n                        matrix = stage_matrices.scalar(eta,previous,frame,zero,tau,index-1)\n                        stage_record['returned_value_matrix_origin'] = json.loads(json.dumps(\n                            stage_matrices.last_request_record,allow_nan=False))\n                    except (EndpointRootFailure,RuntimeError) as error:\n                        stage_record['returned_value_matrix_failure'] = str(error)\n                        self._fail('Actual normal-plane angular-jet matrix unavailable: '+str(error),\n                            normal_stage_index=index,incremental_state=eta)\n                    prior_eta = None\n                else:\n                    matrix = tensor(np.stack([item['J'] for item in old_stage]))\n                    prior_eta = tensor(np.stack([item['eta'] for item in old_stage]))\n                closure_values.progress(\"normal_stage_angular_jets\", stage_index=index)\n                eta_jets,residuals = self._finish_stage_jets(data,previous,frame,zero,tau,\n                    eta,matrix,order,existing=prior_eta)\n                controls = torch.zeros((count,3,CONTROL_DIMENSION),dtype=torch.float64)\n                controls[:,:order+1] = self._stage_control_jets(previous,frame,eta_jets,order)\n                if old_stage is not None:\n                    controls[:,:2] = tensor(np.stack([item['controls'][:2] for item in old_stage]))\n                    if (eta_jets[:,:2].cpu().numpy().tobytes()\n                            != np.stack([item['eta'][:2] for item in old_stage]).tobytes()\n                            or controls[:,:2].cpu().numpy().tobytes()\n                            != np.stack([item['controls'][:2] for item in old_stage]).tobytes()):\n                        raise AssertionError('An angular upgrade changed the already selected root branch words')\n                # Re-read the actual original plane with these actual cached/extended\n                # controls. A cache upgrade never silently repairs a failed old value.\n                actual = closure_values.force_value(controls,data,order,\n                    reason='original_stage_residual_reread')-(1-tau)*zero[:,:order+1]\n                norms = torch.linalg.vector_norm(actual,dim=-1)\n                valid = (torch.isfinite(actual).all(-1).all(-1)\n                    & self._inside_domain(controls[:,0])\n                    & (self.S*norms[:,0] <= self.policy.endpoint_tolerance))\n                for j,record in enumerate(records):\n                    record.update(actual_control_jet_residual_norms=[float(v) if math.isfinite(float(v))\n                        else None for v in norms[j]],original_stage_reread_passed=bool(valid[j]),\n                        lower_jets_byte_preserved_on_upgrade=old_stage is not None,\n                        dimensionless_control_norm=(float(torch.linalg.vector_norm(controls[j,0]))\n                            if bool(torch.isfinite(controls[j,0]).all()) else None))\n                if not bool(valid.all()):\n                    self._fail('The actual original normal-plane equation failed after its complete angular-jet read',\n                        normal_stage_index=index,angles=torch.nonzero(~valid).flatten().tolist(),\n                        state=controls[:,0],incremental_state=eta,\n                        physical_endpoint=float(torch.max(self.S*norms[:,0])))\n                all_stages.append(dict(eta=eta_jets.detach().cpu().numpy().copy(),\n                    frame=frame.detach().cpu().numpy().copy(),\n                    controls=controls.detach().cpu().numpy().copy(),\n                    J=matrix.detach().cpu().numpy().copy(),records=records,frame_provenance=frame_provenance))\n                previous = controls.detach()\n                log['completed_stage_count'] = index\n                closure_values.stage_complete(index)\n            closure_values.progress('normal_final_endpoint_reread')\n            final = self.S*closure_values.force_value(previous,data,order,\n                reason='original_final_endpoint_reread')\n            final_norms = torch.linalg.vector_norm(final,dim=-1)\n            log['all_original_endpoint_equations_checked'] = True\n            finite_final = torch.isfinite(final).all(-1).all(-1)\n            log['final_original_endpoint_maximum'] = (\n                float(final_norms[:,0].max()) if bool(finite_final.all()) else None)\n            valid = finite_final & self._inside_domain(previous[:,0]) & (\n                final_norms[:,0] <= self.policy.endpoint_tolerance)\n            log['all_original_endpoint_equations_passed'] = bool(valid.all())\n            if not bool(valid.all()):\n                self._fail('The final ORIGINAL physical endpoint equation failed after the full normal chain',\n                    normal_stage_index=self.normal_stage_count,\n                    angles=torch.nonzero(~valid).flatten().tolist(),state=previous[:,0],\n                    physical_endpoint=log['final_original_endpoint_maximum'])\n        if existing is None:\n            self.endpoint_counts['root_angles_solved'] += count\n        else:\n            self.endpoint_counts['jet_upgrades'] += count\n        self.maximum_endpoint_root_residual = max(self.maximum_endpoint_root_residual,\n            float(final_norms[:,0].max()))\n        self.maximum_endpoint_correction_norm = max(self.maximum_endpoint_correction_norm,\n            float(torch.linalg.vector_norm(previous[:,0],dim=-1).max()))\n        frozen = lambda value: np.array(value,dtype=np.float64,copy=True)\n        result = []\n        for j in range(count):\n            stages = [dict(eta=frozen(item['eta'][j]),frame=frozen(item['frame'][j]),\n                controls=frozen(item['controls'][j]),J=frozen(item['J'][j]),\n                record=item['records'][j],frame_provenance=item['frame_provenance'][j],\n                jacobian=None,jacobian_order=0) for item in all_stages]\n            record = dict(numerical_endpoint_residual_norm=float(final_norms[j,0]),\n                physical_angular_endpoint_residual_norms=[float(v) for v in final_norms[j]],\n                dimensionless_control_norm=float(torch.linalg.vector_norm(previous[j,0])),\n                physical_z_norm=float(self.S*torch.linalg.vector_norm(previous[j,0,:3])),\n                gamma_axis_norm=float(torch.linalg.vector_norm(previous[j,0,3:])),\n                all_normal_stages_returned=True,normal_stage_count=self.normal_stage_count,\n                exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],\n                same_branch_jet_upgrade=existing is not None,\n                original_value_and_first_jet_preserved=existing is not None,\n                final_original_physical_endpoint_equation_checked=True,\n                stationary_KKT_selection_used=False,continuous_branch_certified=False)\n            item = dict(Z=frozen(previous[j].cpu().numpy()),zero=frozen(zero[j].cpu().numpy()),\n                stages=stages,order=order,record=record)\n            for key in ('Z','zero'):\n                item[key].setflags(write=False)\n            for stage in stages:\n                for key in ('eta','frame','controls','J'):\n                    stage[key].setflags(write=False)\n            result.append(item)\n        return result\n", "_meridian_data": "    def _meridian_data(self, x, query, phi, curvature, query_label):\n        return self.detached_meridian_values.meridian_data(x,query,phi,curvature,query_label)\n"}


def complete_method_ast():
    result=dict(METHOD_AST)
    for name,source in METHOD_SOURCE_OVERRIDES.items():
        nodes=ast.parse(textwrap.dedent(source)).body
        if len(nodes)!=1 or not isinstance(nodes[0],ast.FunctionDef) or nodes[0].name!=name:
            raise ValueError('Keep each complete explicitly derived closure method')
        result[name]=canonical(_ast_value(nodes[0]))
    return result


def definition():
    return dict(schema=SCHEMA, source_sha256=sha(__file__),
        parent_complete_normal_source_sha256=PARENT_NORMAL_SOURCE_SHA256,
        complete_base_source_sha256=BASE_SOURCE_SHA256,
        original_complete_frame_AST_sha256=ORIGINAL_FRAME_AST_SHA256,
        bound_complete_method_AST_sha256=complete_method_ast(),
        complete_closure_value_source_sha256=CLOSURE_VALUE_SOURCE_SHA256,
        unknown='partial with respect to all six U0 slots; U1/U2 are independent jet slots',
        output='all requested orders 0,1,2; shape [angle,order+1,3,6]',
        physical_jets='actual complete _corrected_jets T,Tp,Tpp expressions',
        directions='e0=W[:,ell], e1=Wp[:,ell], e2=Wpp[:,ell] for ell=0,...,5',
        radial_jets='q0=w0.w0; q1=2*w0.w1; q2=2*(w1.w1+w0.w2)',
        coefficient_values='all six actual original rotation_coefficients values A,B,Az,Bz,Azz,Bzz',
        small_branch='q<1/4; independently differentiate each original binary-coefficient Horner polynomial',
        large_branch='q>=1/4; full product/quotient chain rule for each original sin/cos/sqrt expression',
        independent_rounded_Az_used_as_derivative_of_A=False,
        independent_rounded_Azz_used_as_derivative_of_Az=False,
        original_working_coefficient_derivative_functions_all_six=True,
        zero_rotation_division_required=False,
        branch_predicate_and_safe_argument_retained=True,
        reference_core_cap_terms_local_control_derivative_zero=True,
        original_unrotated_meridian_and_W_upstream_graph_retained=True,
        previous_U0_U1_U2_upstream_graph_retained=True,
        active_data_or_previous_detached=False,
        integral='each actual column and requested angular jet through original complete _total, then /S',
        integral_weights_nodes_widths_and_reduction_order_retained=True,
        full_six_columns_without_rank_clipping_or_symmetrization=True,
        optional_failure_policy='complete original reverse-product frame on all requested angles and orders',
        source_shape_binding_failures_use_optional_fallback=False,
        fallback_is_original_reverse_product_frame=True,
        frame_reverse_counter_counts_only_actual_original_reverse_products=True,
        analytic_reduction_counters_separate=True,
        full_active_upstream_parameter_J_and_transpose_retained=True,
        original_common_partition_all_stages_and_true_equations_retained=True,
        original_root_and_angular_implicit_solve_paths_retained=True,
        new_frame_cache_created=False,
        actual_floating_frame_may_differ_from_original_reverse_product_words=True,
        exact_Rodrigues_derivative_not_substituted_for_working_polynomial_derivative=True,
        branch_seam_truncation_rounding_and_inverse_errors_enclosed=False,
        uniform_IFT_root_success_or_field_acceptance_inferred=False,
        measured_acceleration_claimed=False,
        all_scientific_execution_public_Actions_only=True)


def _counts(value):
    if not isinstance(value, dict) or set(value) != set(COUNTER_KEYS):
        raise ValueError('Keep every actual analytic-frame counter')
    if any(type(item) is not int or item < 0 for item in value.values()):
        raise ValueError('Actual counters are nonnegative integers')
    if (value['frame_calls_started'] != value['frame_calls_returned']+value['frame_calls_failed']
            or value['frame_calls_started'] != sum(value['order%d_requests' % j] for j in range(3))
            or value['frame_calls_started'] != value['active_graph_requests']+value['detached_value_requests']
            or value['analytic_attempts'] != value['analytic_returns']+value['analytic_failures']
            or value['ad_fallback_attempts'] != value['ad_fallback_returns']+value['ad_fallback_failures']
            or value['analytic_attempts'] != value['frame_calls_started']
            or value['ad_fallback_attempts'] > value['analytic_failures']
            or not value['frame_calls_returned'] <= value['analytic_returns']+value['ad_fallback_returns']
                <= value['frame_calls_started']
            or value['analytic_angle_blocks_returned']+value['ad_fallback_angle_blocks_returned']
                > value['requested_angle_blocks']
            or value['analytic_angle_jets_returned']+value['ad_fallback_angle_jets_returned']
                > value['requested_angle_jets']
            or value['analytic_control_columns_returned'] > value['analytic_control_columns_started']
            or value['analytic_control_columns_started'] > 6*value['analytic_attempts']
            or value['analytic_total_calls_returned'] > value['analytic_total_calls_started']
            or value['analytic_total_calls_started'] > 3*value['analytic_control_columns_started']
            or value['analytic_total_angle_vectors_returned'] > value['analytic_total_angle_vectors_requested']
            or value['ad_reverse_products_returned'] > value['ad_reverse_products_started']
            or value['ad_reverse_products_started'] > 9*value['ad_fallback_attempts']
            or value['ad_reverse_angle_products_returned'] > value['ad_reverse_angle_products_started']
            or value['actual_frame_reverse_angle_products'] > value['ad_reverse_angle_products_returned']):
        raise ValueError('Requests, partial work, real fallback AD and returns have different meanings')
    return dict(value)


def validate_metadata(value, *, model, source_by_role, current_full_point_sha256):
    """Pure stdlib attribution; no frame, matrix, root, field or array evaluation."""
    expected = definition()
    if (not isinstance(value, dict) or value.get('schema') != SCHEMA
            or value.get('source_sha256') != source_by_role['analytic_frame']
            or expected['source_sha256'] != source_by_role['analytic_frame']
            or value.get('definition') != expected
            or model.get('analytic_normal_frame') != expected
            or model.get('schema') != ENDPOINT_SCHEMA
            or value.get('actual_model_identity_sha256') != canonical(model)
            or value.get('actual_operator_source_sha256') != model.get('source_sha256')
            or model.get('base_source_sha256') != BASE_SOURCE_SHA256):
        raise ValueError('Bind the whole analytic-frame source and complete actual field')
    counts = _counts(value.get('actual_counts'))
    elapsed = value.get('frame_call_seconds')
    if (isinstance(elapsed, bool) or not isinstance(elapsed, (int,float))
            or not math.isfinite(elapsed) or elapsed < 0):
        raise ValueError('Keep the actual nonnegative frame duration')
    last = value.get('last_call')
    if last is None:
        if counts['frame_calls_started']:
            raise ValueError('Do not omit the last attempted frame')
    else:
        if (not isinstance(last, dict) or not _digest(last.get('current_full_point_sha256'))
                or type(last.get('angle_count')) is not int or last['angle_count'] <= 0
                or type(last.get('order')) is not int or last['order'] not in (0,1,2)
                or last.get('frame_shape') != [last['angle_count'],last['order']+1,3,6]
                or type(last.get('completed')) is not bool
                or type(last.get('active_outer_graph_requested')) is not bool
                or not _digest(last.get('previous_jet_words_sha256'))
                or last.get('point_equals_current_report_point')
                    != (last['current_full_point_sha256'] == current_full_point_sha256)):
            raise ValueError('The last frame request must belong to its actual point and full order')
        duration = last.get('frame_call_seconds')
        if (isinstance(duration, bool) or not isinstance(duration, (int,float))
                or not math.isfinite(duration) or duration < 0):
            raise ValueError('Retain the real frame call duration')
        delta = last.get('actual_normal_counter_deltas')
        if (not isinstance(delta, dict) or set(delta) != set(OBSERVED_COUNTER_KEYS)
                or any(type(number) is not int or number < 0 for number in delta.values())):
            raise ValueError('Do not synthesize old normal counters from requested frame work')
        if last['completed']:
            if (last.get('returned_origin') not in
                    ('analytic_complete_working_frame', 'complete_original_reverse_product_frame')
                    or not _digest(last.get('frame_words_sha256'))):
                raise ValueError('A complete returned frame needs its actual origin and all-word digest')
        elif last.get('frame_words_sha256') is not None or last.get('returned_origin') is not None:
            raise ValueError('An incomplete frame cannot reuse a previous returned frame')
    if (value.get('active_upstream_graph_retained') is not True
            or value.get('normal_chain_replaced') is not False
            or value.get('root_success_inferred_from_frame_production') is not False
            or value.get('measured_acceleration_claimed') is not False):
        raise ValueError('Retain the exact scope of this numerical derivative producer')
    return dict(schema=SCHEMA, source_sha256=source_by_role['analytic_frame'],
        actual_operator_source_sha256=value['actual_operator_source_sha256'],
        actual_model_identity_sha256=value['actual_model_identity_sha256'],
        actual_counts=counts, frame_call_seconds=elapsed, last_call=_copy(last),
        active_upstream_graph_retained=True, normal_chain_replaced=False,
        root_success_inferred_from_frame_production=False,
        measured_acceleration_claimed=False,
        working_derivative_rounding_certified=False)


def _tensor(value, shape, label):
    if (not isinstance(value, torch.Tensor) or value.dtype != torch.float64
            or value.device.type != 'cpu' or tuple(value.shape) != tuple(shape)):
        raise ValueError('Use the complete actual CPU float64 tensor: '+label)
    if not bool(torch.isfinite(value).all()):
        raise ValueError('Use finite complete inputs for '+label)


def _words(value):
    array = value.detach().cpu().contiguous().numpy()
    digest = hashlib.sha256(str(array.dtype).encode())
    digest.update(json.dumps(list(array.shape)).encode())
    digest.update(array.tobytes())
    return digest.hexdigest()


def _cross(left, right):
    return torch.cross(left, right, dim=-1)


def _dual_add(left, right):
    return left[0]+right[0], left[1]+right[1]


def _dual_neg(value):
    return -value[0], -value[1]


def _dual_mul(left, right):
    return left[0]*right[0], left[1]*right[0]+left[0]*right[1]


def _dual_div(left, right):
    return left[0]/right[0], (left[1]*right[0]-left[0]*right[1])/(right[0]*right[0])


def _dual_power(value, exponent):
    return value[0]**exponent, exponent*value[0]**(exponent-1)*value[1]


def _coefficient_derivatives(radial):
    """Six derivatives of the six ACTUAL independently rounded functions.

    These are elementary product/quotient rules and Horner recurrences,
    not autograd calls and not the independently rounded Az/Azz tables
    substituted for derivatives of a different coefficient polynomial.
    """
    small = radial < .25
    safe = torch.clamp(radial, min=.25)
    radius = torch.sqrt(safe)
    # In the selected large branch safe==radial and d(radius)/d(radial)=1/(2*radius).
    # Safe positive arguments also keep the unused branch finite at radial=0.
    t = (radius, 1/(2*radius))
    sine = (torch.sin(radius), torch.cos(radius)*t[1])
    cosine = (torch.cos(radius), -torch.sin(radius)*t[1])
    one, two, three, four, five, eight = [(float(n),0.) for n in (1,2,3,4,5,8)]
    radial_pair = (safe, torch.ones_like(safe))
    add, neg, mul, div, power = _dual_add, _dual_neg, _dual_mul, _dual_div, _dual_power
    sub = lambda a,b: add(a,neg(b))
    # The six value expressions have the same arithmetic grouping as the
    # original large branch; only their analytic tangent is consumed.
    large = (
        div(sine,t),
        div(sub(one,cosine),radial_pair),
        div(sub(mul(t,cosine),sine),mul(two,power(t,3))),
        div(sub(mul(t,sine),mul(two,sub(one,cosine))),mul(two,power(t,4))),
        div(add(sub(mul(mul(neg(t),t),sine),mul(mul(three,t),cosine)),
                mul(three,sine)),mul(four,power(t,5))),
        div(add(sub(mul(mul(t,t),cosine),mul(mul(five,t),sine)),
                mul(eight,sub(one,cosine))),mul(four,power(t,6))))
    derivatives = []
    for derivative in (0,1,2):
        for offset in (1,2):
            value = torch.zeros_like(radial)
            tangent = torch.zeros_like(radial)
            for power_index in range(12,derivative-1,-1):
                factor = math.factorial(power_index)//math.factorial(power_index-derivative)
                # Preserve the actual binary coefficient computation of
                # this derivative table, including its independent rounding.
                coefficient = ((-1.)**power_index)*factor/math.factorial(2*power_index+offset)
                tangent = tangent*radial+value
                value = value*radial+coefficient
            derivatives.append(tangent)
    return tuple(torch.where(small, polynomial, formula[1])
        for polynomial,formula in zip(derivatives,large))


class AnalyticFrameUnavailable(ArithmeticError):
    pass


class AnalyticNormalFrame:
    """Full local six-control partial with the complete active outer graph."""
    def __init__(self,q):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Keep the declared complete CPU PyTorch version')
        self.q = q
        self.definition = definition()
        if (q.model.get('schema') != ENDPOINT_SCHEMA
                or q.model.get('analytic_normal_frame') != self.definition
                or canonical(q.model) != q.identity
                or q.model.get('base_source_sha256') != BASE_SOURCE_SHA256
                or q.base.model.get('source_sha256') != BASE_SOURCE_SHA256
                or q.model.get('base_complete_model') != q.base.model
                or canonical(q.base.model) != q.base.identity
                or q.model.get('implicit_control_dimension') != 6
                or q.model.get('normal_increment_dimension') != 3
                or q.model.get('common_partition_for_all_angles_and_free_points') is not True
                or q.model.get('per_angle_adaptive_normal_partition') is not False):
            raise ValueError('Bind the actual complete field, six controls and whole fixed normal chain')
        methods = {name:getattr(q,name) for name in complete_method_ast()}
        if any(getattr(method,'__self__',None) is not q for method in methods.values()):
            raise ValueError('Do not replace bound complete methods with callbacks')
        path = Path(methods['_normal_frame_jets'].__func__.__code__.co_filename).resolve()
        source = path.read_bytes()
        source_digest = hashlib.sha256(source).hexdigest()
        if source_digest != q.model.get('source_sha256'):
            raise ValueError('The actual complete normal operator source differs')
        classes = [node for node in ast.parse(source).body
            if isinstance(node,ast.ClassDef) and node.name == 'ZeroClosureOperator']
        if len(classes) != 1:
            raise ValueError('Use the complete independently declared normal operator')
        source_methods = {node.name:node for node in classes[0].body
            if isinstance(node,ast.FunctionDef)}
        for name,method in methods.items():
            function = method.__func__
            if (Path(function.__code__.co_filename).resolve() != path
                    or function.__globals__.get('SCHEMA') != ENDPOINT_SCHEMA
                    or function.__globals__.get('ANALYTIC_FRAME_SOURCE_SHA256') != sha(__file__)
                    or function.__globals__.get('DETACHED_CLOSURE_SOURCE_SHA256') != CLOSURE_VALUE_SOURCE_SHA256
                    or name not in source_methods
                    or canonical(_ast_value(source_methods[name])) != complete_method_ast()[name]):
                raise ValueError('A full original method or the explicit frame wrapper changed: '+name)
        rotation = q.rotation_coefficients
        if (rotation.__name__ != 'rotation_coefficients'
                or sha(rotation.__code__.co_filename) != BASE_SOURCE_SHA256
                or not math.isfinite(float(q.S)) or float(q.S) <= 0):
            raise ValueError('Use the complete original working coefficients and positive actual S carrier')
        self.methods = {name:method.__func__ for name,method in methods.items()}
        self.operator_source = source_digest
        self.model_identity = q.identity
        self.model_object = q.model
        self.base_model_object = q.base.model
        self.partition = tuple(float(value).hex() for value in q.normal_step_carriers)
        if list(self.partition) != q.model.get('actual_normal_step_carriers_binary64_hex'):
            raise ValueError('The actual complete common normal partition differs')
        self.counts = {name:0 for name in COUNTER_KEYS}
        self.seconds = 0.
        self.last_call = None

    def _arguments(self,previous,data,order):
        q = self.q
        if (type(order) is not int or order not in (0,1,2)
                or not isinstance(previous,torch.Tensor) or previous.ndim != 3
                or previous.shape[1] < order+1 or previous.shape[2] != 6):
            raise ValueError('Keep all six control columns and every requested angular jet slot')
        if (q.model is not self.model_object or q.base.model is not self.base_model_object
                or q.identity != self.model_identity
                or q.model.get('analytic_normal_frame') != self.definition
                or any(getattr(q,name).__func__ is not function
                    for name,function in self.methods.items())
                or tuple(float(value).hex() for value in q.normal_step_carriers) != self.partition
                or not _digest(q._current_point_sha256)
                or data.get('order') not in (0,1,2) or data['order'] < order):
            raise ValueError('Keep the current full field, complete method bodies and actual data order')
        count = len(previous)
        if count <= 0:
            raise ValueError('Do not discard an angle batch')
        _tensor(previous,(count,previous.shape[1],6),'previous complete control jets')
        points = (q.J-1)*q.integration_order
        for name in ('W','Wp','Wpp')[:order+1]:
            _tensor(data['W'][name],(points,count,3,6),'complete '+name)
        for name in ('T','Tp','Tpp')[:order+1]:
            _tensor(data['meridians'][name],(points,count,3),'complete current '+name)
        for role in ('core','cap','reference_core','reference_cap'):
            if len(data[role]) < order+1:
                raise ValueError('Retain every complete angular '+role+' jet')
            for j in range(order+1):
                _tensor(data[role][j],(count,3),role+' jet '+str(j))
        for name in ('T','Tp','Tpp')[:order+1]:
            _tensor(data['reference'][name],(points,count,3),'complete reference '+name)
        return count

    def _analytic(self,previous,data,order):
        q = self.q
        enabled = torch.is_grad_enabled()
        local = previous[:,:order+1]
        if enabled and not local.requires_grad:
            # Match the original local-leaf convention without detaching an
            # active previous point or any active meridian/data edge.
            local = local.detach().clone().requires_grad_(True)
        apply = lambda matrix,vector: torch.einsum('paij,aj->pai',matrix,vector)
        expand = lambda value: value[...,None]
        W = data['W']
        meridians = data['meridians']
        w = apply(W['W'],local[:,0])
        V = meridians['T']
        radial = (w*w).sum(-1)
        self.counts['actual_coefficient_value_calls'] += 1
        A,B,Az,Bz,Azz,Bzz = q.rotation_coefficients(radial)
        self.counts['actual_coefficient_derivative_calls'] += 1
        Aq,Bq,Azq,Bzq,Azzq,Bzzq = _coefficient_derivatives(radial)
        first = _cross(w,V)
        second = _cross(w,first)
        if order >= 1:
            wp = apply(W['Wp'],local[:,0])+apply(W['W'],local[:,1])
            Vp = meridians['Tp']
            radial_p = 2*(w*wp).sum(-1)
            first_p = _cross(wp,V)+_cross(w,Vp)
            second_p = _cross(wp,first)+_cross(w,first_p)
            Ap,Bp = Az*radial_p,Bz*radial_p
        if order >= 2:
            wpp = (apply(W['Wpp'],local[:,0])+2*apply(W['Wp'],local[:,1])
                +apply(W['W'],local[:,2]))
            Vpp = meridians['Tpp']
            radial_pp = 2*((wp*wp).sum(-1)+(w*wpp).sum(-1))
            first_pp = _cross(wpp,V)+2*_cross(wp,Vp)+_cross(w,Vpp)
            second_pp = _cross(wpp,first)+2*_cross(wp,first_p)+_cross(w,first_pp)
            App = Azz*radial_p*radial_p+Az*radial_pp
            Bpp = Bzz*radial_p*radial_p+Bz*radial_pp
        columns = []
        for ell in range(6):
            self.counts['analytic_control_columns_started'] += 1
            e = W['W'][...,ell]
            dr = 2*(w*e).sum(-1)
            dfirst = _cross(e,V)
            dsecond = _cross(e,first)+_cross(w,dfirst)
            dA,dB = Aq*dr,Bq*dr
            derivatives = [expand(dA)*first+expand(A)*dfirst
                +expand(dB)*second+expand(B)*dsecond]
            if order >= 1:
                ep = W['Wp'][...,ell]
                drp = 2*((e*wp).sum(-1)+(w*ep).sum(-1))
                dfirst_p = _cross(ep,V)+_cross(e,Vp)
                dsecond_p = (_cross(ep,first)+_cross(wp,dfirst)
                    +_cross(e,first_p)+_cross(w,dfirst_p))
                dAp = Azq*dr*radial_p+Az*drp
                dBp = Bzq*dr*radial_p+Bz*drp
                derivatives.append(expand(dAp)*first+expand(Ap)*dfirst
                    +expand(dA)*first_p+expand(A)*dfirst_p
                    +expand(dBp)*second+expand(Bp)*dsecond
                    +expand(dB)*second_p+expand(B)*dsecond_p)
            if order >= 2:
                epp = W['Wpp'][...,ell]
                drpp = 2*(2*(wp*ep).sum(-1)+(e*wpp).sum(-1)+(w*epp).sum(-1))
                dfirst_pp = _cross(epp,V)+2*_cross(ep,Vp)+_cross(e,Vpp)
                dsecond_pp = (_cross(epp,first)+_cross(wpp,dfirst)
                    +2*(_cross(ep,first_p)+_cross(wp,dfirst_p))
                    +_cross(e,first_pp)+_cross(w,dfirst_pp))
                dApp = (Azzq*dr*radial_p*radial_p+2*Azz*radial_p*drp
                    +Azq*dr*radial_pp+Az*drpp)
                dBpp = (Bzzq*dr*radial_p*radial_p+2*Bzz*radial_p*drp
                    +Bzq*dr*radial_pp+Bz*drpp)
                derivatives.append(expand(dApp)*first+expand(App)*dfirst
                    +2*(expand(dAp)*first_p+expand(Ap)*dfirst_p)
                    +expand(dA)*first_pp+expand(A)*dfirst_pp
                    +expand(dBpp)*second+expand(Bpp)*dsecond
                    +2*(expand(dBp)*second_p+expand(Bp)*dsecond_p)
                    +expand(dB)*second_pp+expand(B)*dsecond_pp)
            totals = []
            for derivative in derivatives:
                self.counts['analytic_total_calls_started'] += 1
                self.counts['analytic_total_angle_vectors_requested'] += len(previous)
                totals.append(q._total(derivative)/q.S)
                self.counts['analytic_total_calls_returned'] += 1
                self.counts['analytic_total_angle_vectors_returned'] += len(previous)
            columns.append(torch.stack(totals,dim=1))
            self.counts['analytic_control_columns_returned'] += 1
        result = torch.stack(columns,dim=-1)
        if not bool(torch.isfinite(result).all()):
            raise AnalyticFrameUnavailable('Nonfinite complete six-control analytic frame')
        return result if enabled else result.detach()

    def _original_AD(self,previous,data,order):
        """The original complete frame, with separate attempt counters only."""
        q = self.q
        enabled = torch.is_grad_enabled()
        with torch.enable_grad():
            local = previous[:,:order+1]
            if not local.requires_grad:
                local = local.detach().clone().requires_grad_(True)
            closure = q._closure_jets(local,data,order)
            frames = []
            for j in range(order+1):
                rows = []
                for k in range(3):
                    self.counts['ad_reverse_products_started'] += 1
                    self.counts['ad_reverse_angle_products_started'] += len(previous)
                    rows.append(torch.autograd.grad(closure[:,j,k].sum(),local,
                        create_graph=enabled,retain_graph=True,allow_unused=False)[0][:,0])
                    self.counts['ad_reverse_products_returned'] += 1
                    self.counts['ad_reverse_angle_products_returned'] += len(previous)
                frames.append(torch.stack(rows,dim=1))
                q.normal_counts['frame_reverse_angle_products'] += 3*len(previous)
            result = torch.stack(frames,dim=1)
        result = result if enabled else result.detach()
        if not bool(torch.isfinite(result).all()):
            raise AnalyticFrameUnavailable('Nonfinite complete original reverse-product frame')
        return result

    def frame(self,previous,data,order):
        require_actions()
        started = time.monotonic()
        count = self._arguments(previous,data,order)
        enabled = torch.is_grad_enabled()
        record = dict(current_full_point_sha256=self.q._current_point_sha256,
            angle_count=count,order=order,frame_shape=[count,order+1,3,6],
            active_outer_graph_requested=enabled,previous_jet_words_sha256=_words(previous),
            completed=False,returned_origin=None,frame_words_sha256=None,
            analytic_unavailable=None,point_equals_current_report_point=True)
        self.last_call = record
        before = {name:self.q.normal_counts[name] for name in OBSERVED_COUNTER_KEYS}
        self.counts['frame_calls_started'] += 1
        self.counts['requested_angle_blocks'] += count
        self.counts['requested_angle_jets'] += count*(order+1)
        self.counts['order%d_requests' % order] += 1
        self.counts['active_graph_requests' if enabled else 'detached_value_requests'] += 1
        try:
            self.counts['analytic_attempts'] += 1
            try:
                result = self._analytic(previous,data,order)
            except Exception as error:
                self.counts['analytic_failures'] += 1
                if not isinstance(error,(ArithmeticError,MemoryError,RuntimeError)):
                    raise
                record['analytic_unavailable'] = type(error).__name__+': '+str(error)
                self.counts['ad_fallback_attempts'] += 1
                try:
                    result = self._original_AD(previous,data,order)
                except Exception:
                    self.counts['ad_fallback_failures'] += 1
                    raise
                self.counts['ad_fallback_returns'] += 1
                self.counts['ad_fallback_angle_blocks_returned'] += count
                self.counts['ad_fallback_angle_jets_returned'] += count*(order+1)
                origin = 'complete_original_reverse_product_frame'
            else:
                self.counts['analytic_returns'] += 1
                self.counts['analytic_angle_blocks_returned'] += count
                self.counts['analytic_angle_jets_returned'] += count*(order+1)
                origin = 'analytic_complete_working_frame'
            _tensor(result,(count,order+1,3,6),'returned complete frame')
            record.update(completed=True,returned_origin=origin,frame_words_sha256=_words(result))
            self.counts['frame_calls_returned'] += 1
            return result
        except Exception as error:
            self.counts['frame_calls_failed'] += 1
            record['actual_failure'] = type(error).__name__+': '+str(error)
            raise
        finally:
            elapsed = time.monotonic()-started
            self.seconds += elapsed
            record['frame_call_seconds'] = elapsed
            delta = {name:self.q.normal_counts[name]-before[name] for name in OBSERVED_COUNTER_KEYS}
            record['actual_normal_counter_deltas'] = delta
            self.counts['actual_closure_jet_angle_evaluations'] += delta['closure_jet_angle_evaluations']
            self.counts['actual_frame_reverse_angle_products'] += delta['frame_reverse_angle_products']

    def metadata(self):
        last = _copy(self.last_call)
        if last is not None:
            last['point_equals_current_report_point'] = (
                last['current_full_point_sha256'] == self.q._current_point_sha256)
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            actual_operator_source_sha256=self.operator_source,
            actual_model_identity_sha256=self.model_identity,
            actual_counts=dict(self.counts),frame_call_seconds=self.seconds,last_call=last,
            active_upstream_graph_retained=True,normal_chain_replaced=False,
            root_success_inferred_from_frame_production=False,
            measured_acceleration_claimed=False,
            working_derivative_rounding_certified=False)

