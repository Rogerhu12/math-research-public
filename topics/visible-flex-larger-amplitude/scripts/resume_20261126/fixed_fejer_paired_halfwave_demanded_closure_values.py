#!/usr/bin/env python3
"""Same-call detached complete closure values; no derivative or equation is omitted.

Only the literal complete value returned by the bound original closure formula
may be reused. Every active/forward/functorch/dispatch/traced context bypasses
the cache. Every stage's final original closure check and the final endpoint
check explicitly call the original formula. No numerical claim is made here.
"""
import ast
import hashlib
import json
import math
import os
from pathlib import Path
import textwrap
import time
from datetime import datetime, timezone

import numpy as np
import torch

SCHEMA = 'same-chain-immutable-point-complete-detached-closure-value-reuse-v1'
DEFINITION_SCHEMA = 'complete-immutable-point-detached-closure-value-reuse-working-definition-v1'
ENDPOINT_SCHEMA = 'complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1'
NORMAL_PARENT_SHA256 = '3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc'
NORMAL_PARENT_BASENAME = 'so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py'
BASE_SOURCE_SHA256 = 'b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6'
TORCH_VERSION = '2.5.1'
PROGRESS_BASENAME = 'actual-normal-evaluation-progress.json'
COUNTER_KEYS = (
    'logical_requests', 'logical_returns', 'logical_failures',
    'original_attempts', 'original_returns', 'original_failures',
    'original_angle_jet_requests', 'original_angle_jet_returns',
    'cache_hits', 'cache_hit_angle_jets', 'cache_misses',
    'forced_original_requests', 'forced_stage_rereads', 'forced_endpoint_rereads',
    'bypass_no_scope', 'bypass_caller_environment', 'bypass_current_environment',
    'bypass_tensor_or_data_tracking', 'bypass_optional_failure',
    'binding_failures', 'key_checks', 'point_word_checks',
    'point_entry_word_checks', 'point_exit_word_checks',
    'immutable_point_binding_checks', 'immutable_point_entry_checks',
    'immutable_point_key_checks', 'immutable_point_exit_checks',
    'stored_values', 'optional_cache_failures',
    'scopes_started', 'scopes_closed', 'scopes_with_exception',
    'scopes_disabled_at_entry', 'scope_stage_completions',
    'progress_writes', 'progress_write_failures', 'progress_events',
    'peak_cache_entries', 'peak_cache_bytes')
DERIVED_METHOD_SOURCES = json.loads("{\"_closure_jets\":\"    def _closure_jets(self, controls, data, order):\\n        return self.detached_closure_values.value(controls, data, order)\\n\",\"_closure_jets_original\":\"    def _closure_jets_original(self, controls, data, order):\\n        corrected = self._corrected_jets(data['meridians'],data['W'],controls,order)\\n        names = ('T','Tp','Tpp')\\n        self.normal_counts['closure_jet_angle_evaluations'] += len(controls)\\n        return torch.stack(tuple(((data['core'][j]-data['reference_core'][j])\\n            -(data['cap'][j]-data['reference_cap'][j])\\n            +self._total(corrected[names[j]]-data['reference'][names[j]]))/self.S\\n            for j in range(order+1)),dim=1)\\n\",\"_run_chain\":\"    def _run_chain(self, data, keys, order, existing=None):\\n        \\\"\\\"\\\"One common finite chain; an order-two upgrade keeps every old value/first jet.\\\"\\\"\\\"\\n        if order not in (1,2) or len(keys) != len(data['core'][0]):\\n            raise ValueError('Use every actual angle and the complete requested angular order')\\n        if existing is not None and (order != 2 or len(existing) != len(keys)\\n                or any(item['order'] != 1 for item in existing)):\\n            raise ValueError('Only an actual cached first-jet branch may be upgraded')\\n        entry_environment = self.detached_closure_values.entry_environment()\\n        count = len(keys)\\n        self._last_normal_batch = dict(schema='actual-complete-fixed-normal-plane-batch-v1',\\n            current_full_point_sha256=self._current_point_sha256,angle_count=count,\\n            material_angles_binary64_hex=list(keys),requested_angular_order=order,\\n            same_branch_jet_upgrade=existing is not None,\\n            normal_stage_count=self.normal_stage_count,\\n            exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],\\n            completed_stage_count=0,all_original_endpoint_equations_checked=False,\\n            auxiliary_nodes_are_README_physical_flex=False,\\n            complete_continuous_branch_certified=False,stages=[])\\n        log = self._last_normal_batch\\n        all_stages = []\\n        frame_context = self.adjacent_frames.frame_context(data,keys,order)\\n        with torch.no_grad(), self.detached_closure_values.scope(\\n                data, keys, order, entry_environment) as closure_values, (\\n                self.frame_c1.value_scope(data,keys,order)) as frame_values, (\\n                self.stage_matrices.scope(data,keys,order,'returned_value_J3')\\n                if existing is None else nullcontext()) as stage_matrices:\\n            previous = torch.zeros((count,3,CONTROL_DIMENSION),dtype=torch.float64)\\n            zero = torch.zeros((count,3,3),dtype=torch.float64)\\n            zero[:,:order+1] = self._closure_jets(previous,data,order)\\n            if existing is not None:\\n                zero[:,:2] = tensor(np.stack([item['zero'][:2] for item in existing]))\\n            if not bool(torch.isfinite(zero).all()):\\n                self._fail('Nonfinite original zero-control closure jets')\\n            for index in range(1,self.normal_stage_count+1):\\n                tau = self.normal_step_carriers[index]\\n                closure_values.progress(\\\"normal_stage_frame\\\", stage_index=index)\\n                frame = torch.zeros((count,3,3,CONTROL_DIMENSION),dtype=torch.float64)\\n                frame[:,:order+1] = frame_values.frame(previous,index-1)\\n                old_stage = None if existing is None else [item['stages'][index-1] for item in existing]\\n                if old_stage is not None:\\n                    frame[:,:2] = tensor(np.stack([item['frame'][:2] for item in old_stage]))\\n                if not bool(torch.isfinite(frame).all()):\\n                    self._fail('Nonfinite complete preceding normal frame',\\n                        normal_stage_index=index,state=previous[:,0])\\n                frame_provenance = self.adjacent_frames.capture_frame_inputs(\\n                    frame_context,previous,frame,index-1,old_stages=old_stage)\\n                closure_values.progress(\\\"normal_stage_root\\\", stage_index=index)\\n                if old_stage is None:\\n                    eta,success,records = self._solve_stage(data,previous,frame,zero,tau,index)\\n                else:\\n                    eta = tensor(np.stack([item['eta'][0] for item in old_stage]))\\n                    success = torch.ones(count,dtype=torch.bool)\\n                    records = [dict(local_angle_index=j,successful=True,\\n                        reused_original_value_and_first_jet=True,\\n                        original_stage_record=old_stage[j]['record']) for j in range(count)]\\n                stage_record = dict(normal_stage_index=index,\\n                    exact_auxiliary_node=str(self.normal_step_nodes[index]),\\n                    actual_auxiliary_node_hex=float(tau).hex(),\\n                    same_branch_jet_upgrade=old_stage is not None,angle_records=records)\\n                log['stages'].append(stage_record)\\n                if not bool(success.all()):\\n                    control = self._stage_control_jets(previous,frame,eta[:,None],0)[:,0]\\n                    self._fail('A declared fixed normal plane did not return every original stage equation',\\n                        normal_stage_index=index,angles=torch.nonzero(~success).flatten().tolist(),\\n                        state=control,incremental_state=eta)\\n                if old_stage is None:\\n                    try:\\n                        matrix = stage_matrices.scalar(eta,previous,frame,zero,tau,index-1)\\n                        stage_record['returned_value_matrix_origin'] = json.loads(json.dumps(\\n                            stage_matrices.last_request_record,allow_nan=False))\\n                    except (EndpointRootFailure,RuntimeError) as error:\\n                        stage_record['returned_value_matrix_failure'] = str(error)\\n                        self._fail('Actual normal-plane angular-jet matrix unavailable: '+str(error),\\n                            normal_stage_index=index,incremental_state=eta)\\n                    prior_eta = None\\n                else:\\n                    matrix = tensor(np.stack([item['J'] for item in old_stage]))\\n                    prior_eta = tensor(np.stack([item['eta'] for item in old_stage]))\\n                closure_values.progress(\\\"normal_stage_angular_jets\\\", stage_index=index)\\n                eta_jets,residuals = self._finish_stage_jets(data,previous,frame,zero,tau,\\n                    eta,matrix,order,existing=prior_eta)\\n                controls = torch.zeros((count,3,CONTROL_DIMENSION),dtype=torch.float64)\\n                controls[:,:order+1] = self._stage_control_jets(previous,frame,eta_jets,order)\\n                if old_stage is not None:\\n                    controls[:,:2] = tensor(np.stack([item['controls'][:2] for item in old_stage]))\\n                    if (eta_jets[:,:2].cpu().numpy().tobytes()\\n                            != np.stack([item['eta'][:2] for item in old_stage]).tobytes()\\n                            or controls[:,:2].cpu().numpy().tobytes()\\n                            != np.stack([item['controls'][:2] for item in old_stage]).tobytes()):\\n                        raise AssertionError('An angular upgrade changed the already selected root branch words')\\n                # Re-read the actual original plane with these actual cached/extended\\n                # controls. A cache upgrade never silently repairs a failed old value.\\n                actual = closure_values.force_value(controls,data,order,\\n                    reason='original_stage_residual_reread')-(1-tau)*zero[:,:order+1]\\n                norms = torch.linalg.vector_norm(actual,dim=-1)\\n                valid = (torch.isfinite(actual).all(-1).all(-1)\\n                    & self._inside_domain(controls[:,0])\\n                    & (self.S*norms[:,0] <= self.policy.endpoint_tolerance))\\n                for j,record in enumerate(records):\\n                    record.update(actual_control_jet_residual_norms=[float(v) if math.isfinite(float(v))\\n                        else None for v in norms[j]],original_stage_reread_passed=bool(valid[j]),\\n                        lower_jets_byte_preserved_on_upgrade=old_stage is not None,\\n                        dimensionless_control_norm=(float(torch.linalg.vector_norm(controls[j,0]))\\n                            if bool(torch.isfinite(controls[j,0]).all()) else None))\\n                if not bool(valid.all()):\\n                    self._fail('The actual original normal-plane equation failed after its complete angular-jet read',\\n                        normal_stage_index=index,angles=torch.nonzero(~valid).flatten().tolist(),\\n                        state=controls[:,0],incremental_state=eta,\\n                        physical_endpoint=float(torch.max(self.S*norms[:,0])))\\n                all_stages.append(dict(eta=eta_jets.detach().cpu().numpy().copy(),\\n                    frame=frame.detach().cpu().numpy().copy(),\\n                    controls=controls.detach().cpu().numpy().copy(),\\n                    J=matrix.detach().cpu().numpy().copy(),records=records,frame_provenance=frame_provenance))\\n                previous = controls.detach()\\n                log['completed_stage_count'] = index\\n                closure_values.stage_complete(index)\\n            closure_values.progress('normal_final_endpoint_reread')\\n            final = self.S*closure_values.force_value(previous,data,order,\\n                reason='original_final_endpoint_reread')\\n            final_norms = torch.linalg.vector_norm(final,dim=-1)\\n            log['all_original_endpoint_equations_checked'] = True\\n            finite_final = torch.isfinite(final).all(-1).all(-1)\\n            log['final_original_endpoint_maximum'] = (\\n                float(final_norms[:,0].max()) if bool(finite_final.all()) else None)\\n            valid = finite_final & self._inside_domain(previous[:,0]) & (\\n                final_norms[:,0] <= self.policy.endpoint_tolerance)\\n            log['all_original_endpoint_equations_passed'] = bool(valid.all())\\n            if not bool(valid.all()):\\n                self._fail('The final ORIGINAL physical endpoint equation failed after the full normal chain',\\n                    normal_stage_index=self.normal_stage_count,\\n                    angles=torch.nonzero(~valid).flatten().tolist(),state=previous[:,0],\\n                    physical_endpoint=log['final_original_endpoint_maximum'])\\n        if existing is None:\\n            self.endpoint_counts['root_angles_solved'] += count\\n        else:\\n            self.endpoint_counts['jet_upgrades'] += count\\n        self.maximum_endpoint_root_residual = max(self.maximum_endpoint_root_residual,\\n            float(final_norms[:,0].max()))\\n        self.maximum_endpoint_correction_norm = max(self.maximum_endpoint_correction_norm,\\n            float(torch.linalg.vector_norm(previous[:,0],dim=-1).max()))\\n        frozen = lambda value: np.array(value,dtype=np.float64,copy=True)\\n        result = []\\n        for j in range(count):\\n            stages = [dict(eta=frozen(item['eta'][j]),frame=frozen(item['frame'][j]),\\n                controls=frozen(item['controls'][j]),J=frozen(item['J'][j]),\\n                record=item['records'][j],frame_provenance=item['frame_provenance'][j],\\n                jacobian=None,jacobian_order=0) for item in all_stages]\\n            record = dict(numerical_endpoint_residual_norm=float(final_norms[j,0]),\\n                physical_angular_endpoint_residual_norms=[float(v) for v in final_norms[j]],\\n                dimensionless_control_norm=float(torch.linalg.vector_norm(previous[j,0])),\\n                physical_z_norm=float(self.S*torch.linalg.vector_norm(previous[j,0,:3])),\\n                gamma_axis_norm=float(torch.linalg.vector_norm(previous[j,0,3:])),\\n                all_normal_stages_returned=True,normal_stage_count=self.normal_stage_count,\\n                exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],\\n                same_branch_jet_upgrade=existing is not None,\\n                original_value_and_first_jet_preserved=existing is not None,\\n                final_original_physical_endpoint_equation_checked=True,\\n                stationary_KKT_selection_used=False,continuous_branch_certified=False)\\n            item = dict(Z=frozen(previous[j].cpu().numpy()),zero=frozen(zero[j].cpu().numpy()),\\n                stages=stages,order=order,record=record)\\n            for key in ('Z','zero'):\\n                item[key].setflags(write=False)\\n            for stage in stages:\\n                for key in ('eta','frame','controls','J'):\\n                    stage[key].setflags(write=False)\\n            result.append(item)\\n        return result\\n\",\"_select_point\":\"    def _select_point(self, x):\\n        value = (x.detach().cpu().numpy() if isinstance(x, torch.Tensor) else np.asarray(x))\\n        value = np.asarray(value, dtype=float)\\n        if value.shape != (self.free_size,) or not np.isfinite(value).all():\\n            raise ValueError('Use the actual complete finite original free point')\\n        if self._current_x is None or not np.array_equal(value, self._current_x):\\n            self._current_x = np.frombuffer(value.tobytes(order='C'), dtype=np.float64)\\n            self._current_point_sha256 = array_sha(value)\\n            self._root_cache = {}\\n            self._residual_cache = None\\n            self._last_root_failure = None\\n            self._last_normal_batch = None\\n            self.reference_calibration.select_point(self._current_point_sha256)\\n\",\"_meridian_data\":\"    def _meridian_data(self, x, query, phi, curvature, query_label):\\n        return self.detached_meridian_values.meridian_data(x,query,phi,curvature,query_label)\\n\",\"fields_torch\":\"    def fields_torch(self, x, query, phi, *, curvature=True, query_label='arbitrary'):\\n        return self.detached_meridian_values.fields_torch(x,query,phi,\\n            curvature=curvature,query_label=query_label)\\n\",\"_rotate\":\"    def _rotate(self, w, V):\\n        q = (w*w).sum(-1)\\n        A, B, _, _, _, _ = self.detached_meridian_values.rotation_coefficients(q,0)\\n        first = cross(w, V)\\n        return V+A[..., None]*first+B[..., None]*cross(w, first)\\n\",\"_corrected_jets\":\"    def _corrected_jets(self, meridians, W, Zjets, order, *, need_s=False):\\n        apply = lambda matrix, vector: torch.einsum('paij,aj->pai', matrix, vector)\\n        w = apply(W['W'], Zjets[:, 0])\\n        V = meridians['T']\\n        q = (w*w).sum(-1)\\n        A, B, Az, Bz, Azz, Bzz = self.detached_meridian_values.rotation_coefficients(\\n            q,max(order,1 if need_s else 0))\\n        expand = lambda value: value[..., None]\\n        first, second = cross(w, V), None\\n        second = cross(w, first)\\n        answer = {'T': V+expand(A)*first+expand(B)*second}\\n        if order >= 1:\\n            wp = apply(W['Wp'], Zjets[:, 0])+apply(W['W'], Zjets[:, 1])\\n            Vp = meridians['Tp']\\n            qp = 2*(w*wp).sum(-1)\\n            first_p = cross(wp, V)+cross(w, Vp)\\n            second_p = cross(wp, first)+cross(w, first_p)\\n            answer['Tp'] = (Vp+expand(Az*qp)*first+expand(A)*first_p\\n                            +expand(Bz*qp)*second+expand(B)*second_p)\\n        if order >= 2:\\n            wpp = (apply(W['Wpp'], Zjets[:, 0])+2*apply(W['Wp'], Zjets[:, 1])\\n                   +apply(W['W'], Zjets[:, 2]))\\n            Vpp = meridians['Tpp']\\n            qpp = 2*((wp*wp).sum(-1)+(w*wpp).sum(-1))\\n            first_pp = cross(wpp, V)+2*cross(wp, Vp)+cross(w, Vpp)\\n            second_pp = cross(wpp, first)+2*cross(wp, first_p)+cross(w, first_pp)\\n            answer['Tpp'] = (Vpp+expand(Azz*qp*qp+Az*qpp)*first\\n                +2*expand(Az*qp)*first_p+expand(A)*first_pp\\n                +expand(Bzz*qp*qp+Bz*qpp)*second\\n                +2*expand(Bz*qp)*second_p+expand(B)*second_pp)\\n        if need_s:\\n            ws, Vs = apply(W['Ws'], Zjets[:, 0]), meridians['Ts']\\n            qs = 2*(w*ws).sum(-1)\\n            first_s = cross(ws, V)+cross(w, Vs)\\n            second_s = cross(ws, first)+cross(w, first_s)\\n            answer['Ts'] = (Vs+expand(Az*qs)*first+expand(A)*first_s\\n                            +expand(Bz*qs)*second+expand(B)*second_s)\\n        return answer\\n\"}")


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete closure value evaluation is public repository Actions only')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def _copy(value):
    return json.loads(json.dumps(value,allow_nan=False))


def _digest(value):
    return (isinstance(value,str) and len(value)==64
        and all(c in '0123456789abcdef' for c in value))


def _ast_value(value):
    if isinstance(value,ast.AST):
        return [type(value).__name__,[[name,_ast_value(item)]
            for name,item in ast.iter_fields(value)
            if not (name=='type_params' and item==[])]]
    if isinstance(value,list):
        return [_ast_value(v) for v in value]
    if value is Ellipsis:
        return {'python_literal':'Ellipsis'}
    if isinstance(value,bytes):
        return {'python_bytes_hex':value.hex()}
    return value


def definition():
    return dict(schema=DEFINITION_SCHEMA,source_sha256=sha(__file__),
        complete_parent_normal_source_sha256=NORMAL_PARENT_SHA256,
        base_source_sha256=BASE_SOURCE_SHA256,torch_version=TORCH_VERSION,
        cached_quantity='complete original closure angular jets C, before stage tau/zero subtraction',
        cache_scope='one actual detached _run_chain, one full point, ordered literal angle batch and requested maximum order',
        control_key='all provided six-control angular slots and all binary64 words, shape and requested order',
        data_binding='complete named tensor objects, versions, shapes, strides, offsets, types and entry/final words digest',
        point_binding='same plain ndarray, digest, exact immutable bytes owner and complete layout on each eligible key; complete words read at scope entry and exit',
        immutable_point_owner_type='exact built-in bytes owning all native float64 point words',
        immutable_point_layout='one-dimensional C-contiguous full free_size, stride 8, zero offset, readonly, non-owning ndarray',
        reversible_setflags_only_storage_accepted=False,
        all_point_selection_equality_and_cache_reset_rules_unchanged=True,
        per_request_complete_point_word_copy=False,
        point_word_checks_count_actual_entry_or_exit_whole_word_read_attempts=True,
        immutable_point_binding_checks_are_distinct_from_whole_word_reads=True,
        carrier_binding='whole physical mesh/Gauss words, S, original total reduction and bound full methods',
        active_parameter_J_and_transpose_use_original=True,
        forward_AD_functorch_dispatch_tracing_or_unknown_probe_use_original=True,
        inference_and_tensor_subclass_inputs_use_original=True,
        all_32_or_declared_stages_tau_targets_domains_residuals_and_trace_retained=True,
        every_stage_final_closure_reread_forces_original=True,
        final_endpoint_closure_reread_forces_original=True,
        exact_normal_partition_or_root_selection_changed=False,
        cache_values_are_cloned_and_never_graphs=True,
        cache_lifetime_ends_at_the_same_chain_return_or_exception=True,
        optional_storage_or_tracking_failure_uses_original=True,
        no_new_numerical_admission_gate=True,
        same_formula_reused_actual_words_not_unexecuted_rounding_claim=True,
        new_continuous_certificate_or_speedup_claimed=False,
        progress_is_read_only_scalar_observation=True,
        progress_file_is_mutable_not_an_immutable_scientific_input=True)


def _counts(value):
    if not isinstance(value,dict) or set(value)!=set(COUNTER_KEYS):
        raise ValueError('Keep every complete closure value counter')
    if any(type(v) is not int or v<0 for v in value.values()):
        raise ValueError('Closure value counters are actual nonnegative integers')
    for total,returned,failed in (
            ('logical_requests','logical_returns','logical_failures'),
            ('original_attempts','original_returns','original_failures')):
        if not 0<=value[total]-value[returned]-value[failed]<=1:
            raise ValueError('A real in-flight request is distinct from a returned or failed one')
    if (not value['logical_returns']<=value['cache_hits']+value['original_returns']
                <=value['logical_requests']
            or value['original_failures']>value['logical_failures']
                +(value['logical_requests']-value['logical_returns']-value['logical_failures'])
            or value['original_angle_jet_returns']>value['original_angle_jet_requests']
            or value['forced_stage_rereads']+value['forced_endpoint_rereads']
                !=value['forced_original_requests']
            or value['forced_original_requests']>value['original_attempts']
            or value['scopes_closed']>value['scopes_started']
            or value['scopes_started']-value['scopes_closed']>1
            or value['scopes_with_exception']>value['scopes_closed']
            or value['point_word_checks']!=value['point_entry_word_checks']+value['point_exit_word_checks']
            or value['immutable_point_binding_checks']!=sum(value[k] for k in
                ('immutable_point_entry_checks','immutable_point_key_checks','immutable_point_exit_checks'))
            or value['immutable_point_entry_checks']>value['scopes_started']
            or value['immutable_point_exit_checks']>value['scopes_started']
            or value['immutable_point_key_checks']>value['key_checks']
            or value['point_entry_word_checks']>value['immutable_point_entry_checks']
            or value['point_exit_word_checks']>value['immutable_point_exit_checks']):
        raise ValueError('Complete logical, original, cached and forced costs do not close')
    return dict(value)


def validate_metadata(value, *, model, source_by_role, current_full_point_sha256):
    """Pure stdlib reader; never imports or invokes the numerical cache body."""
    if (not isinstance(value,dict) or value.get('schema')!=SCHEMA
            or value.get('source_sha256')!=sha(__file__)
            or source_by_role.get('closure_values')!=sha(__file__)
            or model.get('schema')!=ENDPOINT_SCHEMA
            or model.get('source_sha256')!=source_by_role.get('endpoint')
            or value.get('actual_operator_source_sha256')!=source_by_role.get('endpoint')
            or value.get('actual_model_identity_sha256')!=canonical(model)
            or value.get('definition')!=definition()
            or model.get('detached_closure_value_reuse')!=definition()
            or value.get('current_full_point_sha256')!=current_full_point_sha256):
        raise ValueError('Use this whole closure working policy on the same complete field')
    counts=_counts(value.get('actual_counts'))
    for name in ('original_closure_seconds','binding_and_key_seconds','scope_seconds'):
        v=value.get(name)
        if not isinstance(v,(float,int)) or isinstance(v,bool) or not math.isfinite(v) or v<0:
            raise ValueError('Keep actual finite nonnegative closure cost: '+name)
    if (value.get('active_or_transformed_values_cached') is not False
            or value.get('all_stage_final_rereads_force_original') is not True
            or value.get('final_endpoint_reread_forces_original') is not True
            or value.get('new_scientific_success_inferred') is not False):
        raise ValueError('Do not convert a value reuse count into a root/derivative certificate')
    last=value.get('last_scope')
    if last is not None:
        if not isinstance(last,dict) or not _digest(last.get('current_full_point_sha256')):
            raise ValueError('Keep the actual last scope point')
        if (last.get('model_identity_sha256')!=canonical(model)
                or last.get('maximum_angular_order') not in (1,2)
                or type(last.get('completed_stage_count')) is not int
                or not 0<=last['completed_stage_count']<=model['normal_stage_count']
                or last.get('whole_stage_count')!=model['normal_stage_count']
                or last.get('point_equals_current_report_point') is not
                    (last['current_full_point_sha256']==current_full_point_sha256)
                or type(last.get('closed')) is not bool
                or type(last.get('scope_exited_with_exception')) is not bool
                or last.get('complete_scientific_chain_claimed') is not False):
            raise ValueError('A completed/partial working scope remains associated with its own point')
        keys=last.get('ordered_literal_phi_hex')
        if (not isinstance(keys,list) or not keys or any(not isinstance(k,str)
                or not math.isfinite(float.fromhex(k)) or float.fromhex(k).hex()!=k for k in keys)
                or last.get('ordered_literal_phi_sha256')!=canonical(keys)):
            raise ValueError('Keep every literal angle and its exact original order')
        _counts(last.get('counts'))
    last_request=value.get('last_request')
    if last_request is not None:
        if (not isinstance(last_request,dict)
                or not _digest(last_request.get('current_full_point_sha256'))
                or last_request.get('requested_order') not in (0,1,2)
                or last_request.get('origin') not in
                    (None,'original_complete_formula','same_scope_previously_returned_complete_value')
                or type(last_request.get('completed')) is not bool):
            raise ValueError('Keep the actual last requested closure and its origin')
        if last_request['origin']=='same_scope_previously_returned_complete_value':
            if (not _digest(last_request.get('control_words_sha256'))
                    or not _digest(last_request.get('cached_value_words_sha256'))
                    or type(last_request.get('origin_request_ordinal')) is not int
                    or not 0<last_request['origin_request_ordinal']<last_request['request_ordinal']
                    or last_request.get('original_formula_executed_for_this_request') is not False):
                raise ValueError('A cache hit must identify an earlier complete numerical return')
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        actual_model_identity_sha256=canonical(model),actual_counts=counts,
        original_closure_seconds=value['original_closure_seconds'],
        binding_and_key_seconds=value['binding_and_key_seconds'],scope_seconds=value['scope_seconds'],
        last_scope_closed=None if last is None else last.get('closed'),
        last_scope_completed_stages=None if last is None else last['completed_stage_count'],
        last_scope_own_point=None if last is None else last['current_full_point_sha256'],
        last_scope_point_equals_current=None if last is None else last['point_equals_current_report_point'],
        all_final_original_equation_checks_retained=True,
        point_word_checks_scope='actual complete point word-read attempts at enabled scope entry/exit',
        immutable_point_checks_scope='actual same-array/same-bytes-owner/layout checks; not word reads',
        per_request_complete_point_word_copy=False,
        active_J_and_Jtranspose_original=True,continuous_error_or_speedup_certified=False)


def _environment_reason():
    """Unknown tracking state disables reuse; no_grad alone is never enough."""
    try:
        if torch.is_grad_enabled():
            return 'reverse_gradient_mode_enabled'
        if torch.is_inference_mode_enabled():
            return 'inference_mode'
        if torch.jit.is_tracing() or torch.jit.is_scripting():
            return 'tracing_or_scripting'
        compiler=getattr(torch,'compiler',None)
        compiling=getattr(compiler,'is_compiling',None)
        if not callable(compiling):
            return 'compile_probe_unavailable'
        if compiling():
            return 'compilation_active'
        functorch=getattr(torch._C,'_are_functorch_transforms_active',None)
        if not callable(functorch):
            return 'functorch_probe_unavailable'
        if functorch():
            return 'functorch_transform_active'
        forward=getattr(torch.autograd,'forward_ad',None)
        level=getattr(forward,'_current_level',None)
        if type(level) is not int:
            return 'forward_AD_level_probe_unavailable'
        if level!=-1:
            return 'forward_AD_level_active'
        if not callable(getattr(forward,'unpack_dual',None)):
            return 'dual_tensor_probe_unavailable'
        from torch.utils import _python_dispatch
        from torch import overrides
        dispatch=getattr(_python_dispatch,'_get_current_dispatch_mode_stack',None)
        function=getattr(overrides,'_get_current_function_mode_stack',None)
        if not callable(dispatch) or not callable(function):
            return 'dispatch_mode_probe_unavailable'
        if dispatch() or function():
            return 'dispatch_or_function_mode_active'
        if torch.is_autocast_enabled('cpu') or torch.is_autocast_enabled('cuda'):
            return 'autocast_active'
        return None
    except (AttributeError,RuntimeError,TypeError,MemoryError):
        return 'tracking_probe_unavailable'


def _plain_tensor(value):
    if type(value) is not torch.Tensor:
        return False
    try:
        wrapped=getattr(getattr(torch._C,'_functorch',None),'is_functorch_wrapped_tensor',None)
        functional=getattr(torch,'_is_functional_tensor',None)
        if not callable(wrapped) or not callable(functional):
            return False
        if (wrapped(value) or functional(value) or value.requires_grad or value.grad_fn is not None
                or value.device.type!='cpu' or value.dtype!=torch.float64
                or value.layout!=torch.strided
                or torch.autograd.forward_ad.unpack_dual(value).tangent is not None):
            return False
        int(value._version)
        return True
    except (AttributeError,RuntimeError,TypeError,MemoryError):
        return False


def _tensor_token(value):
    if not _plain_tensor(value):
        raise CacheUnavailable('A tensor is tracked, nonstandard or lacks a complete version token')
    return (id(value),int(value._version),tuple(value.shape),tuple(value.stride()),
        int(value.storage_offset()),str(value.dtype),str(value.device),str(value.layout),
        int(value.untyped_storage().data_ptr()))


def _data_token(value):
    if isinstance(value,torch.Tensor):
        return ('tensor',_tensor_token(value))
    if isinstance(value,dict):
        if any(type(k) is not str for k in value):
            raise CacheUnavailable('The original named data keys are not plain strings')
        return ('dict',id(value),tuple((k,_data_token(value[k])) for k in sorted(value)))
    if type(value) in (tuple,list):
        return (type(value).__name__,id(value),tuple(_data_token(v) for v in value))
    if value is None or type(value) in (bool,int,str):
        return (type(value).__name__,value)
    if type(value) is float and math.isfinite(value):
        return ('float',value.hex())
    raise CacheUnavailable('Unexpected data tracking or mutable type')


def _data_words_digest(value):
    h=hashlib.sha256()
    def visit(v):
        if isinstance(v,torch.Tensor):
            _tensor_token(v)
            a=v.detach().contiguous().numpy()
            h.update(json.dumps(['tensor',list(a.shape),str(a.dtype)],separators=(',',':')).encode())
            h.update(a.tobytes(order='C'))
        elif isinstance(v,dict):
            h.update(b'dict')
            for k in sorted(v):
                h.update(json.dumps(k).encode());visit(v[k])
        elif type(v) in (tuple,list):
            h.update(type(v).__name__.encode())
            for item in v:visit(item)
        else:
            h.update(json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode())
    visit(value)
    return h.hexdigest()


def _float_array_words(value, shape):
    a=np.asarray(value)
    if a.dtype!=np.dtype('float64') or a.shape!=shape:
        raise ValueError('The complete original point or physical carrier layout changed')
    return np.ascontiguousarray(a).tobytes(order='C')


def _immutable_point_owner(value, shape, expected_owner=None):
    """Read only fixed-size array metadata; never copy or scan full point words."""
    if type(value) is not np.ndarray:
        raise ValueError('The selected complete point must be a plain ndarray')
    owner=value.base
    if (type(owner) is not bytes or value.dtype!=np.dtype('float64')
            or not value.dtype.isnative or value.shape!=shape
            or value.strides!=(np.dtype('float64').itemsize,)
            or value.ndim!=1 or not value.flags.c_contiguous
            or value.flags.writeable or value.flags.owndata
            or value.nbytes!=8*shape[0] or len(owner)!=value.nbytes
            or (expected_owner is not None and owner is not expected_owner)):
        raise ValueError('Bind the entire readonly point directly to its exact immutable bytes owner')
    # The exact-length contiguous array covers the whole bytes allocation;
    # a nonzero slice offset would require bytes beyond the bound owner.
    return owner


def _control_words(value,order,count):
    if (not _plain_tensor(value) or value.ndim!=3 or value.shape[0]!=count
            or value.shape[2]!=6 or not order+1<=value.shape[1]<=3):
        raise CacheUnavailable('Use all actual detached six-control angular slots')
    if not bool(torch.isfinite(value).all()):
        raise CacheUnavailable('Do not memoize a nonfinite control')
    array=value.detach().contiguous().numpy()
    return (tuple(array.shape),tuple(value.stride()),int(value.storage_offset()),
        array.tobytes(order='C'))


class CacheUnavailable(RuntimeError):
    """Only optional value reuse is unavailable; the original formula remains."""


class CompleteDetachedClosureValues:
    def __init__(self,q,*,progress_path=None):
        require_actions()
        if torch.__version__.split('+')[0]!=TORCH_VERSION:
            raise ValueError('Use the declared whole CPU Torch version')
        self.q=q
        self.definition=definition()
        if (q.model.get('schema')!=ENDPOINT_SCHEMA
                or q.model.get('detached_closure_value_reuse')!=self.definition
                or canonical(q.model)!=q.identity
                or q.model.get('base_source_sha256')!=BASE_SOURCE_SHA256
                or q.base.model.get('source_sha256')!=BASE_SOURCE_SHA256
                or q.model.get('base_complete_model')!=q.base.model
                or canonical(q.base.model)!=q.base.identity):
            raise ValueError('Bind the complete actual normal field and unchanged base')
        path=Path(q._closure_jets.__func__.__code__.co_filename).resolve()
        self.operator_source=sha(path)
        if (self.operator_source!=q.model.get('source_sha256')
                or q._closure_jets.__func__.__globals__.get('DETACHED_CLOSURE_SOURCE_SHA256')!=sha(__file__)):
            raise ValueError('The actual complete normal source must pin this complete helper')
        parent_path=path.parent/NORMAL_PARENT_BASENAME
        if sha(parent_path)!=NORMAL_PARENT_SHA256:
            raise ValueError('Read the entire unchanged scientific parent source')
        def methods(raw):
            classes=[n for n in ast.parse(raw).body
                if isinstance(n,ast.ClassDef) and n.name=='ZeroClosureOperator']
            if len(classes)!=1:
                raise ValueError('Use one complete declared normal operator')
            return {n.name:n for n in classes[0].body if isinstance(n,ast.FunctionDef)}
        expected=methods(parent_path.read_bytes())
        actual=methods(path.read_bytes())
        for name,text in DERIVED_METHOD_SOURCES.items():
            node=ast.parse(textwrap.dedent(text)).body
            if len(node)!=1 or not isinstance(node[0],ast.FunctionDef) or node[0].name!=name:
                raise ValueError('Keep complete explicitly declared method replacements')
            expected[name]=node[0]
        if set(expected)!=set(actual):
            raise ValueError('No original normal method may be removed or silently inserted')
        self.methods={}
        for name,node in expected.items():
            bound=getattr(q,name)
            function=getattr(bound,'__func__',bound)
            if (Path(function.__code__.co_filename).resolve()!=path
                    or function.__globals__.get('SCHEMA')!=ENDPOINT_SCHEMA):
                raise ValueError('A normal method comes from another source')
            if name not in ('__init__','metadata'):
                if canonical(_ast_value(node))!=canonical(_ast_value(actual[name])):
                    raise ValueError('Changed complete mathematical method: '+name)
                self.methods[name]=function
        if (sha(q.rotation_coefficients.__code__.co_filename)!=BASE_SOURCE_SHA256
                or q._total.__func__.__globals__.get('DETACHED_CLOSURE_SOURCE_SHA256')!=sha(__file__)):
            raise ValueError('Keep the actual original coefficient and complete reduction source')
        self.original=q._closure_jets_original
        self.identity=q.identity
        self.model_object=q.model
        self.base_model_object=q.base.model
        self.active=None
        self.counts={k:0 for k in COUNTER_KEYS}
        self.original_seconds=0.
        self.key_seconds=0.
        self.scope_seconds=0.
        self.last_request=None
        self.last_scope=None
        self.progress_path=None
        self.progress_last_write=0.
        self.progress_record=None
        self.progress_failure=None
        if progress_path is not None:
            p=Path(progress_path).resolve()
            if (p.name!=PROGRESS_BASENAME or p.parent!=Path(q.base.cache_directory).resolve().parent
                    or p.exists()):
                raise ValueError('Use the new separate scalar progress file in this fresh scientific outdir')
            self.progress_path=p

    def entry_environment(self):
        return _environment_reason()

    def scope(self,data,keys,order,entry_environment):
        return CompleteClosureValueScope(self,data,keys,order,entry_environment)

    def _inc(self,name,amount=1):
        self.counts[name]+=amount
        if self.active is not None:
            self.active.counts[name]+=amount

    def _source_binding(self):
        q=self.q
        if (q.identity!=self.identity or q.model is not self.model_object
                or q.base.model is not self.base_model_object
                or any(getattr(getattr(q,name),'__func__',getattr(q,name)) is not function
                    for name,function in self.methods.items())):
            raise ValueError('Do not cross the complete original functions or field model')

    def _call_original(self,controls,data,order,record):
        self._inc('original_attempts')
        start=time.monotonic()
        try:
            count=int(controls.shape[0])
            self._inc('original_angle_jet_requests',count*(order+1))
            answer=self.original(controls,data,order)
        except BaseException:
            self._inc('original_failures')
            raise
        else:
            self._inc('original_returns')
            self._inc('original_angle_jet_returns',count*(order+1))
            record['origin']='original_complete_formula'
            record['original_formula_executed_for_this_request']=True
            return answer
        finally:
            self.original_seconds+=time.monotonic()-start

    def value(self,controls,data,order):
        return self._request(controls,data,order,forced=None)

    def _request(self,controls,data,order,*,forced):
        require_actions()
        if type(order) is not int or order not in (0,1,2):
            raise ValueError('Keep every original requested angular closure order')
        self._inc('logical_requests')
        record=dict(request_ordinal=self.counts['logical_requests'],
            current_full_point_sha256=self.q._current_point_sha256,
            requested_order=order,completed=False,origin=None,
            original_formula_executed_for_this_request=False,
            control_words_sha256=None,cached_value_words_sha256=None,
            origin_request_ordinal=None,bypass_reason=None,
            forced_original_reread=forced)
        self.last_request=record
        try:
            self._source_binding()
        except BaseException:
            self._inc('binding_failures');self._inc('logical_failures')
            raise
        scope=self.active
        key=None
        try:
            if forced is not None:
                if forced not in ('original_stage_residual_reread','original_final_endpoint_reread'):
                    raise ValueError('Every forced reread has its original source-declared role')
                self._inc('forced_original_requests')
                self._inc('forced_stage_rereads' if forced=='original_stage_residual_reread'
                    else 'forced_endpoint_rereads')
                record['bypass_reason']='forced_original_final_reread'
            elif scope is None:
                self._inc('bypass_no_scope');record['bypass_reason']='outside_complete_chain_scope'
            elif scope.entry_environment is not None:
                self._inc('bypass_caller_environment');record['bypass_reason']=scope.entry_environment
            else:
                reason=_environment_reason()
                if reason is not None:
                    self._inc('bypass_current_environment');record['bypass_reason']=reason
                elif not scope.cache_enabled:
                    self._inc('bypass_optional_failure');record['bypass_reason']='scope_optional_tracking_unavailable'
                else:
                    started=time.monotonic()
                    try:
                        key=scope.key(controls,data,order)
                        record['control_words_sha256']=hashlib.sha256(key[-1]).hexdigest()
                    except CacheUnavailable as error:
                        self._inc('bypass_tensor_or_data_tracking')
                        record['bypass_reason']=str(error)
                    except (MemoryError,RuntimeError) as error:
                        scope.optional_failure('complete equality key',error)
                        self._inc('bypass_optional_failure')
                        record['bypass_reason']='optional_key_failure'
                    finally:
                        self.key_seconds+=time.monotonic()-started
            if key is not None and key in scope.cache:
                entry=scope.cache[key]
                try:
                    answer=entry['value'].clone()
                except (MemoryError,RuntimeError) as error:
                    scope.optional_failure('clone a previously returned complete value',error,key)
                    self._inc('bypass_optional_failure')
                    record['bypass_reason']='optional_clone_failure'
                    key=None
                else:
                    self._inc('cache_hits')
                    self._inc('cache_hit_angle_jets',len(controls)*(order+1))
                    record.update(origin='same_scope_previously_returned_complete_value',
                        origin_request_ordinal=entry['ordinal'],
                        cached_value_words_sha256=entry['words_sha256'])
                    record['completed']=True
                    self._inc('logical_returns')
                    return answer
            if key is not None:
                self._inc('cache_misses')
            answer=self._call_original(controls,data,order,record)
            if key is not None:
                try:
                    if (not _plain_tensor(answer)
                            or tuple(answer.shape)!=(len(controls),order+1,3)
                            or not bool(torch.isfinite(answer).all())):
                        raise CacheUnavailable('The original result is not a complete finite detached closure')
                    value=answer.clone()
                    words=value.contiguous().numpy().tobytes(order='C')
                    scope.cache[key]=dict(value=value,ordinal=record['request_ordinal'],
                        words_sha256=hashlib.sha256(words).hexdigest())
                    self._inc('stored_values')
                    scope.cache_bytes+=len(key[-1])+len(words)
                    scope.counts['peak_cache_entries']=max(scope.counts['peak_cache_entries'],len(scope.cache))
                    scope.counts['peak_cache_bytes']=max(scope.counts['peak_cache_bytes'],scope.cache_bytes)
                    self.counts['peak_cache_entries']=max(self.counts['peak_cache_entries'],len(scope.cache))
                    self.counts['peak_cache_bytes']=max(self.counts['peak_cache_bytes'],scope.cache_bytes)
                except (CacheUnavailable,MemoryError,RuntimeError) as error:
                    scope.optional_failure('store a complete original return',error,key)
            record['completed']=True
            self._inc('logical_returns')
            return answer
        except BaseException as error:
            self._inc('logical_failures')
            record['actual_failure']=type(error).__name__+': '+str(error)
            raise

    def progress(self,phase,*,stage_index=None,force=False):
        """Only already existing scalar counters; no metadata/F/root/J callback."""
        if self.progress_path is None:
            return
        now=time.monotonic()
        if not force and now-self.progress_last_write<30.:
            return
        try:
            q=self.q
            record=dict(schema='actual-complete-normal-evaluation-progress-v1',
                source_sha256=sha(__file__),operator_source_sha256=self.operator_source,
                actual_model_identity_sha256=self.identity,current_full_point_sha256=q._current_point_sha256,
                recorded_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                phase=str(phase),normal_stage_index=stage_index,
                closure_counts=dict(self.counts),actual_field_counts=dict(q.counts),
                original_closure_seconds=self.original_seconds,
                binding_and_key_seconds=self.key_seconds,closed_scope_seconds=self.scope_seconds,
                actual_normal_counts=dict(q.normal_counts),endpoint_counts=dict(q.endpoint_counts),
                current_cached_angle_roots=len(q._root_cache),
                fixed_seed_counts=dict(q.base.parent_jet.counts),
                active_scope_maximum_order=None if self.active is None else self.active.order,
                active_scope_angle_count=None if self.active is None else len(self.active.keys),
                actual_scientific_evaluations_by_observer=0,
                first_field_or_geometry_return_inferred=False,scientific_complete_inferred=False,
                mutable_latest_status=True)
            raw=(json.dumps(record,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode()
            tmp=self.progress_path.with_suffix('.partial.json')
            tmp.write_bytes(raw);tmp.replace(self.progress_path)
            self.progress_record=dict(path=str(self.progress_path),bytes=len(raw),
                sha256=hashlib.sha256(raw).hexdigest(),recorded_at_utc=record['recorded_at_utc'],
                phase=record['phase'],mutable_latest_status_snapshot=True)
            self.progress_last_write=now;self.counts['progress_writes']+=1
            print(json.dumps(dict(event='actual_complete_normal_evaluation_progress',
                phase=str(phase),normal_stage_index=stage_index,
                current_full_point_sha256=q._current_point_sha256,
                current_cached_angle_roots=len(q._root_cache),
                original_closure_calls=self.counts['original_attempts'],
                cached_closure_calls=self.counts['cache_hits'],
                recorded_at_utc=record['recorded_at_utc'],
                scientific_complete_inferred=False),sort_keys=True),flush=True)
            self.counts['progress_events']+=1
            self.progress_failure=None
        except (OSError,MemoryError,AttributeError,TypeError,ValueError) as error:
            self.counts['progress_write_failures']+=1
            self.progress_failure=dict(type=type(error).__name__,message=str(error),
                scientific_computation_restarted=False)

    def metadata(self):
        last=_copy(self.last_scope)
        if self.active is not None:
            last=self.active.record(closed=False,exception=False)
        if last is not None:
            last['point_equals_current_report_point']=(
                last['current_full_point_sha256']==self.q._current_point_sha256)
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=self.definition,
            actual_operator_source_sha256=self.operator_source,actual_model_identity_sha256=self.identity,
            current_full_point_sha256=self.q._current_point_sha256,actual_counts=dict(self.counts),
            original_closure_seconds=self.original_seconds,binding_and_key_seconds=self.key_seconds,
            scope_seconds=self.scope_seconds,last_scope=last,last_request=_copy(self.last_request),
            active_or_transformed_values_cached=False,
            all_stage_final_rereads_force_original=True,final_endpoint_reread_forces_original=True,
            progress_file_snapshot=_copy(self.progress_record),progress_failure=_copy(self.progress_failure),
            progress_file_is_mutable_not_an_immutable_input=True,
            new_scientific_success_inferred=False)


class CompleteClosureValueScope:
    def __init__(self,kernel,data,keys,order,entry_environment):
        require_actions()
        if kernel.active is not None:
            raise ValueError('Complete closure scopes cannot overlap or cross a chain')
        if order not in (1,2) or not keys or len(keys)!=len(data['core'][0]):
            raise ValueError('Bind the full original angular order and ordered batch')
        keys=tuple(keys)
        if any(type(k) is not str or not math.isfinite(float.fromhex(k))
                or float.fromhex(k).hex()!=k for k in keys):
            raise ValueError('Do not normalize or reorder literal material angles')
        self.kernel,self.q,self.data=kernel,kernel.q,data
        self.keys,self.order=keys,int(order)
        self.entry_environment=entry_environment
        self.cache={}
        self.cache_bytes=0
        self.cache_enabled=False
        self.counts={k:0 for k in COUNTER_KEYS}
        self.started=time.monotonic()
        self.closed=False
        self.completed_stage_count=0
        self.failures=[]
        self.point_object=self.q._current_x
        self.point_identity=self.q._current_point_sha256
        self.point_words=None
        self.point_owner=None
        self.data_identity=None
        self.data_words=None
        self.carrier=None
        if not _digest(self.point_identity):
            raise ValueError('The complete chain must have its actual full point')
        self.kernel.active=self
        self.kernel._inc('scopes_started')
        try:
            if entry_environment is not None:
                self.kernel._inc('scopes_disabled_at_entry')
            else:
                try:
                    if _environment_reason() is not None:
                        raise CacheUnavailable('The actual scope is not plain detached eager evaluation')
                    self.data_identity=_data_token(data)
                    self.data_words=_data_words_digest(data)
                    self._point_binding('entry')
                    self.kernel._inc('point_word_checks')
                    self.kernel._inc('point_entry_word_checks')
                    self.point_words=_float_array_words(self.point_object,(self.q.free_size,))
                    if self.point_words!=self.point_owner:
                        raise ValueError('The full entry point words differ from the complete immutable owner')
                    self.carrier=self._carrier()
                    self.cache_enabled=True
                except (CacheUnavailable,MemoryError,RuntimeError) as error:
                    self.optional_failure('bind complete detached numerical scope',error)
            self.progress('normal_chain_enter',force=True)
        except BaseException:
            self.close(exception=True)
            raise

    def _carrier(self):
        q=self.q
        return (int(q.J),int(q.integration_order),float(q.S).hex(),
            _float_array_words(q.mesh,(q.J,)),
            _float_array_words(q.gauss_u,(q.integration_order,)),
            _float_array_words(q.gauss_w,(q.integration_order,)),
            tuple(str(v) for v in q.normal_step_nodes),
            tuple(float(v).hex() for v in q.normal_step_carriers),
            self.q._total.__func__,self.q._corrected_jets.__func__,self.q.rotation_coefficients)

    def _point_binding(self, phase):
        if phase not in ('entry','key','exit'):
            raise ValueError('Every immutable point check has its actual scope position')
        self.kernel._inc('immutable_point_binding_checks')
        self.kernel._inc('immutable_point_'+phase+'_checks')
        if (self.q._current_x is not self.point_object
                or self.q._current_point_sha256!=self.point_identity):
            raise ValueError('The actual complete free point changed within a normal chain')
        owner=_immutable_point_owner(self.point_object,(self.q.free_size,),self.point_owner)
        if phase=='entry':
            if self.point_owner is not None:
                raise ValueError('An immutable point scope may bind its owner only once')
            self.point_owner=owner
        elif self.point_owner is None:
            raise ValueError('An immutable point key requires its complete entry binding')

    def key(self,controls,data,order):
        self.kernel._inc('key_checks')
        if self.closed or data is not self.data or not 0<=order<=self.order:
            raise CacheUnavailable('The same named data, chain and requested order are required')
        self._point_binding('key')
        if _data_token(self.data)!=self.data_identity or self._carrier()!=self.carrier:
            raise CacheUnavailable('A complete data version or physical reduction carrier changed')
        words=_control_words(controls,order,len(self.keys))
        return (order,)+words

    def optional_failure(self,operation,error,key=None):
        self.kernel._inc('optional_cache_failures')
        if key is None:
            self.cache.clear();self.cache_bytes=0;self.cache_enabled=False
        else:
            entry=self.cache.pop(key,None)
            if entry is not None:
                self.cache_bytes-=len(key[-1])+entry['value'].numel()*entry['value'].element_size()
        self.failures.append(dict(operation=operation,type=type(error).__name__,
            message=str(error),fallback='complete original formula; no stage or equation removed'))
        error.__traceback__=None

    def force_value(self,controls,data,order,*,reason):
        return self.kernel._request(controls,data,order,forced=reason)

    def stage_complete(self,index):
        if type(index) is not int or index!=self.completed_stage_count+1:
            raise ValueError('Every original normal stage must complete in the unchanged order')
        self.completed_stage_count=index
        self.kernel._inc('scope_stage_completions')
        self.progress('normal_stage_complete',stage_index=index)

    def progress(self,phase,*,stage_index=None,force=False):
        self.kernel.progress(phase,stage_index=stage_index,force=force)

    def record(self,*,closed,exception):
        return dict(current_full_point_sha256=self.point_identity,
            model_identity_sha256=self.kernel.identity,
            maximum_angular_order=self.order,ordered_literal_phi_hex=list(self.keys),
            ordered_literal_phi_sha256=canonical(list(self.keys)),
            whole_stage_count=self.q.normal_stage_count,
            completed_stage_count=self.completed_stage_count,
            entry_environment_bypass=self.entry_environment,
            complete_data_entry_words_sha256=self.data_words,
            counts=dict(self.counts),closed=closed,scope_exited_with_exception=exception,
            complete_scientific_chain_claimed=False,
            optional_failures=_copy(self.failures))

    def close(self,exception=False):
        if self.closed:
            return
        final_error=None
        try:
            if self.cache_enabled:
                try:
                    self._point_binding('exit')
                    self.kernel._inc('point_word_checks')
                    self.kernel._inc('point_exit_word_checks')
                    final_point_words=_float_array_words(self.point_object,(self.q.free_size,))
                    if (_data_token(self.data)!=self.data_identity
                            or _data_words_digest(self.data)!=self.data_words
                            or self._carrier()!=self.carrier
                            or final_point_words!=self.point_words
                            or final_point_words!=self.point_owner):
                        raise ValueError('A complete numerical scope changed its bound original inputs')
                except (CacheUnavailable,MemoryError,RuntimeError) as error:
                    self.optional_failure('final complete numerical data reread',error)
        except BaseException as error:
            final_error=error
        finally:
            self.kernel._inc('scopes_closed')
            actual_exception=bool(exception or final_error is not None)
            if actual_exception:self.kernel._inc('scopes_with_exception')
            self.closed=True
            self.kernel.scope_seconds+=time.monotonic()-self.started
            try:
                self.kernel.last_scope=self.record(closed=True,exception=actual_exception)
                if final_error is not None:
                    self.kernel.last_scope['final_binding_failure']=(
                        type(final_error).__name__+': '+str(final_error))
            finally:
                self.cache.clear();self.cache_bytes=0
                self.data=None;self.point_words=None;self.point_object=None;self.point_owner=None
                self.kernel.active=None
                self.kernel.progress('normal_chain_scope_closed',force=True)
        if final_error is not None:
            raise final_error

    def __enter__(self):
        return self

    def __exit__(self,kind,error,traceback):
        self.close(exception=kind is not None)
        return False
