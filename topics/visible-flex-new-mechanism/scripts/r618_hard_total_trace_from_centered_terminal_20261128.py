#!/usr/bin/env python3
"""Bind the actual centered natural terminal to the hard-total-trace model.

This is a source-level continuation entry point, not a diagnostic replay.
It takes the actual retained accepted response, never the pending trial.
The first total P is extracted by the same complete source core_trace.
No external mu or new core coefficients are chosen in this entry point.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
MODEL_SHA = 'a55832af74577a86e850905dc16c39997a4cd095aca23bcb5aa35e64e9798c62'
CENTERED_SOURCE = '19de4da31f4f6139a2547f2ada7949271a492a00'
CENTERED_RUN = 46117718197
CENTERED_JOB = 140895158286
CENTERED_SCHEMA = 'r618-actual397-fixed-E-centered-Fourier-derivatives-v1'


def bound_model():
    path = HERE / 'r618_hard_total_trace_model_20261128.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != MODEL_SHA:
        raise RuntimeError('actual hard-total-trace model source differs')
    name = 'r618_hard_total_trace_natural_terminal_model'
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def accepted_source(literal_final_json, natural_terminal_record, target_sha256):
    """Metadata and literal accepted-state consumption, without numerical work."""
    record = dict(natural_terminal_record)
    final_sha = hashlib.sha256(literal_final_json.encode()).hexdigest()
    if (record.get('source_commit') != CENTERED_SOURCE
            or record.get('run_id') != CENTERED_RUN or record.get('job_id') != CENTERED_JOB
            or record.get('status') != 'completed' or not record.get('completed_at')
            or record.get('final_json_sha256') != final_sha):
        raise ValueError('the actual current centered natural terminal record is required')
    final = json.loads(literal_final_json)
    if final.get('schema') != CENTERED_SCHEMA or final.get('same_frozen_target_sha256') != target_sha256:
        raise ValueError('same complete centered scope and frozen target required')
    kept = final.get('actual_checkpoint')
    response = final.get('actual_response')
    if (not isinstance(kept, dict) or kept.get('hard_tau') != 1.
            or not isinstance(response, list) or len(response) != 1473 or response[-1] != 1.):
        raise ValueError('the actual retained hard-tau1 accepted state is unavailable')
    response_text = json.dumps(response, separators=(',', ':'), allow_nan=False)
    response_sha = hashlib.sha256(response_text.encode()).hexdigest()
    actual_identity = final['actual_response_identity']
    if actual_identity['sha256'] != response_sha or actual_identity['count'] != len(response):
        raise ValueError('retained actual response differs from its terminal identity')
    costs = final.get('actual_model_cost_receipt')
    if not isinstance(costs, dict) or not costs.get('response_model_sha256'):
        raise ValueError('the actual restored centered source identity is unavailable')
    source = {'source_commit': CENTERED_SOURCE, 'run_id': CENTERED_RUN, 'job_id': CENTERED_JOB,
        'final_json_sha256': final_sha, 'target_sha256': target_sha256,
        'accepted_response_sha256': response_sha,
        'response_model_sha256': costs['response_model_sha256'],
        'actual_accepted_step': kept['accepted_step'],
        'actual_next_damping': final['actual_next_damping'],
        'actual_scientific_terminal_status': final['status'],
        'natural_terminal_record': record,
        'pending_trial_used_as_seed': False}
    return response, source, final


def restore_same_seed_trace(original_driver, actual_q_json, amplitude, frozen_identity,
        maximum_independent_mode, preceding_policy, *, deadline, attempts,
        literal_final_json, natural_terminal_record):
    """Build the new actual field while preserving the entire inherited ledger."""
    module = bound_model()
    module.chain.public_only()
    response, source, final = accepted_source(literal_final_json,
        natural_terminal_record, frozen_identity.target_sha256)
    policy = json.loads(json.dumps(preceding_policy, allow_nan=False))
    policy['hard_total_trace_adapter'] = module.HardTotalTraceHeight.policy_descriptor()
    model = module.HardTotalTraceHeight.restore_from_frozen_reference(original_driver,
        actual_q_json, amplitude, frozen_identity, maximum_independent_mode, policy,
        deadline=deadline, attempts=attempts, accepted_seed_response=response,
        accepted_source=source, prescribed_pc=None)
    receipt = {'actual_source': source, 'actual_hard_trace_definition': model.definition,
        'first_total_trace_extracted_from_same_actual_accepted_response': True,
        'first_function_and_six_jets_are_the_original_actual_seed': True,
        'external_trace_or_mu_changed': False, 'all_free_parameters_retained': model.nq,
        'preceding_actual_terminal_including_all_costs_not_new_costs': final,
        'initial_damping_from_actual_terminal': final['actual_next_damping'],
        'actual_accepted_step_before_new_scope': final['actual_checkpoint']['accepted_step'],
        'new_scientific_evaluation_or_convergence_claimed': False}
    return model, model.initial_response(), receipt
