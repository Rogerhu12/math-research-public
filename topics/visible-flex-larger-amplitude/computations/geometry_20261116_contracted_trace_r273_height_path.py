#!/usr/bin/env python3
"""One original worker, complete physical H(s), current R273, and original acceptance.

Actions-only bootstrap: the local graph Newton correction is replaced by the
current full-system R273 candidate and independent finite successful root-trace
with-J; original noJ primal, scale/tolerance/cache, warm, ten trials and final
responsibilities remain. Every height keeps112 modes.
A first identity-bound positive-height mathematical refusal ends this experiment,
without replaying124's height-halving sequence. Protocol/record ambiguity is
partial: worker last may advance before a record is written.
"""
from __future__ import annotations
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import time
import traceback

SCHEMA = 'contracted-trace-r273-same-worker-complete112-height-path-v1'
POLICY_SCHEMA = 'explicit-contracted-trace-r273-complete112-height-path-policy-v1'
CLIENT_FILE = 'geometry_20261116_contracted_trace_r273_tail_client.py'
CLIENT_SHA = '8a380843013d302e4c19ab7ed811c3dc5f73f21494235379a890415b1ba19712'
WORKER_FILE = 'topics/visible-flexible-closed-surface/scripts/78718-prefix-tail-tangent-fourier-worker.mjs'
WORKER_SHA = '36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a'
CORE_FILE = 'topics/visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs'
CORE_SHA = 'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
POLICY = dict(schema=POLICY_SCHEMA, initial_positive_increment=0.015625,
    accepted_increment_multiplier=2.0, maximum_increment=0.25,
    stop_after_first_positive_original_mathematical_refusal=True,
    no_repeated_height_halving_after_refusal=True,
    maximum_bootstrap_requests=64, includes_zero_and_final_J_requests=True,
    zero_request_jacobian=False, intermediate_request_jacobian=False,
    endpoint_request_jacobian=True, bootstrap_audit=False,
    endpoint_uses_original_H_star_words=True, total_scientific_wall_clock_seconds=18000,
    resource_limits_are_not_mathematical_nonexistence_claims=True)
# Literal messages from the pinned original root/core. The worker outer catch
# also covers I/O, so arbitrary failed strings cannot authorize a retry.
MATHEMATICAL_ERRORS = frozenset((
    'Error: momentum profile out of float range',
    'Error: momentum branch D/S/A rejected',
    'Error: momentum Newton matrix not SPD',
    'Error: momentum Newton line search failed',
    'Error: momentum Newton iteration limit',
    'Error: initial full mean root failed',
    'Error: initial mean iteration limit',
    'Error: tail graph chart singular',
    'Error: Fourier-product Jacobian not positive',
    'Error: physical jet root Jacobian not positive',
    'Error: batched momentum Jacobian not positive',
))


class HeightPathStopped(RuntimeError):
    def __init__(self, outcome, receipt, resource_partial=False):
        super().__init__(outcome)
        self.outcome, self.receipt = outcome, receipt
        self.resource_partial = bool(resource_partial)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Complete-height bootstrap is a public Actions scientific operation')


def clean(value):
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [clean(v) for v in value]
    return value


def encode(value):
    return json.dumps(clean(value), sort_keys=True, separators=(',', ':'),
                      ensure_ascii=True, allow_nan=False).encode()


def identity(value):
    raw = encode(value)
    return dict(canonical_JSON_bytes=len(raw), canonical_JSON_sha256=hashlib.sha256(raw).hexdigest())


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            value.update(block)
    return value.hexdigest()


def descriptor(path, root):
    path = Path(path)
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('A path record must be inside the owned execution output')
    return dict(file=path.relative_to(root).as_posix(), bytes=path.stat().st_size, sha256=sha(path))


def atomic(path, value):
    temporary = path.with_name(path.name+'.partial')
    temporary.write_bytes(encode(value)+b'\n')
    temporary.replace(path)


def words(values):
    result = [float(item) for item in values]
    if len(result) != 112 or any(not math.isfinite(item) for item in result):
        raise ValueError('All112 physical height coordinates must be present and finite')
    return result, struct.pack('<112d', *result)


def height_identity(values):
    result, raw = words(values)
    negative_zero = [i for i in range(112)
                     if raw[8*i:8*(i+1)] == b'\0\0\0\0\0\0\0\x80']
    return dict(shape=[112], dtype='<f8', order='C', bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest(), negative_zero_columns=negative_zero)


def read_json(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def offset(path):
    if path.is_symlink():
        raise ValueError('Original trace paths may not be symlinks')
    return path.stat().st_size if path.exists() else 0


def tail_jsonl(path, start, copy_path, root):
    if not path.exists():
        if start:
            raise ValueError('An original diagnostic file disappeared during the request')
        return [], None
    if offset(path) < start:
        raise ValueError('An original diagnostic file shrank during the request')
    with path.open('rb') as stream:
        stream.seek(start)
        raw = stream.read()
    if raw and not raw.endswith(b'\n'):
        raise ValueError('The original diagnostic record ended in a partial line')
    rows = [json.loads(line) for line in raw.splitlines() if line.strip()]
    if any(not isinstance(row, dict) for row in rows):
        raise ValueError('An original diagnostic event is not a JSON object')
    with copy_path.open('xb') as stream:
        stream.write(raw)
    return rows, descriptor(copy_path, root)


def original_math_error(message):
    if message in MATHEMATICAL_ERRORS:
        return True
    prefix = 'Error: multiple-shooting line search failed at '
    if isinstance(message, str) and message.startswith(prefix):
        suffix = message[len(prefix):]
        try:
            number = float(suffix)
        except ValueError:
            return False
        return bool(suffix and suffix == suffix.strip() and math.isfinite(number) and number >= 0)
    return False


def response_view(response):
    view = {key: response[key] for key in ('failed', 'converged', 'residual',
        'lastIteration', 'iterations', 'actual_nonlinear_solve', 'finite_tail_only') if key in response}
    checkpoint, history, J = response.get('checkpoint'), response.get('history'), response.get('heightJetJacobian')
    view.update(checkpoint_present=isinstance(checkpoint, dict),
        history_count=len(history) if isinstance(history, list) else None,
        full_J_present=J is not None, full_J_identity=None if J is None else identity(J),
        full_J_scalar_count=len(J) if isinstance(J, list) else None,
        audit_present=response.get('audit') is not None)
    if isinstance(checkpoint, dict):
        view['checkpoint_scope'] = checkpoint.get('scope')
        view['checkpoint_height_JSON_identity'] = identity(checkpoint.get('cutHeight'))
        view['checkpoint_JSON_preserves_pre_serialization_negative_zero_claimed'] = False
    jets = response.get('jets')
    if isinstance(jets, dict):
        view['mean_jets'] = {key: jets[key] for key in ('meanSlope', 'meanSecond',
            'meanSlopeCorrection', 'meanSecondCorrection') if key in jets}
    return view


def failure_context(trace_rows, trial_rows, response):
    iterations = [row for row in trace_rows if row.get('event') == 'iteration']
    warm = [row for row in trace_rows if row.get('event') in (
        'tangent_warm_predictor', 'tangent_warm_fallback', 'geometric_amplitude_warm')]
    located = [row for row in trial_rows if any(key in row for key in ('stage', 'rawCell', 'rawSegment'))]
    first_evaluate_incomplete = (response.get('failed') == 'Error: momentum branch D/S/A rejected'
        and response.get('lastIteration') is None and not iterations and not trial_rows and not warm)
    return dict(original_iteration_event_count=len(iterations), original_trial_event_count=len(trial_rows),
        original_warm_events=warm, original_located_trial_failures=located,
        cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source=first_evaluate_incomplete,
        actual_stage_radius_angle_D_S_A_not_supplied_by_outer_failure=True,
        initial_target_fill_has_no_DSA_throw_by_pinned_source=True,
        no_new_root_observer=False,only_original_core_correction_call_replaced=True,
        separate_finite_trace_tangent_and_noJ_matched_withJ_flow=True,
        original_root_primal_arithmetic_and_decision_policy_retained=True,
        original_local_implicit_product_J_replaced=True,
        source_observer_does_not_change_original_trial_decisions=True,
        original_evaluate_and_ten_trial_bodies_retained=True,
        floating_point_cause_or_global_resolution_limit_claimed=False)


def bind_original_record(client, call, requested, jacobian, trace_rows, trial_rows, root):
    file = client.record_prefix.with_name(client.record_prefix.name+f'_{call:04d}.json.gz')
    record = read_json(file)
    if not isinstance(record, dict):
        raise ValueError('The actual original client record is missing or malformed')
    request = record.get('request')
    if (not isinstance(request, dict) or set(request) != {'height', 'jacobian', 'audit'}
            or request.get('jacobian') is not jacobian or request.get('audit') is not False
            or words(request.get('height', []))[1] != words(requested)[1]):
        raise ValueError('The current original request flags or all112 H words differ')
    if (record.get('config') != client._configuration or record.get('source_sha256') != client.sources
            or record.get('capacity_adapter') != read_json(client.capacity_record)):
        raise ValueError('The current original config/source/capacity identity differs')
    response = record.get('response')
    if (not isinstance(response, dict) or response.get('actual_nonlinear_solve') is not True
            or response.get('finite_tail_only') is not True):
        raise ValueError('No complete actual original response was read for this request')
    if any(row.get('call') != call for row in trace_rows+trial_rows):
        raise ValueError('The appended original diagnostics contain a different protocol call')
    begins = [row for row in trace_rows if row.get('event') == 'request']
    if (len(begins) != 1 or begins[0].get('height') != requested
            or begins[0].get('jacobian') is not jacobian or begins[0].get('audit') is not False):
        raise ValueError('The original worker did not record this exact complete request')
    # Worker JSON may turn -0 into +0. This comparison is numerical equality;
    # the original Python request words, checked above, are exact.
    if not trace_rows or trace_rows[-1].get('event') not in ('response', 'failure'):
        raise ValueError('No terminal original response/failure diagnostic was recorded')
    return record, response, descriptor(file, root)


def continue_complete_height(owner, H_star, policy, output, binding):
    """Return actual endpoint response and status receipt; never close owner."""
    require_actions()
    if policy != POLICY:
        raise ValueError('Use the complete explicit195 policy without hidden defaults')
    client = owner.client
    if (client.M != 112 or client.N != 2048 or client.calls != 0
            or client.cache_key is not None or client.cache_value is not None
            or client._configuration.get('initialCheckpoint')):
        raise ValueError('Use this new original112 worker without an installed checkpoint/cache')
    for name, expected in ((CLIENT_FILE, CLIENT_SHA), (WORKER_FILE, WORKER_SHA), (CORE_FILE, CORE_SHA)):
        if client.sources.get(name) != expected:
            raise ValueError('The original failure/cache semantics source differs: '+name)
    if (client._configuration.get('solveTolerance') != 2e-9
            or client._configuration.get('maxIterations') != 32):
        raise ValueError('Retain the original native tolerance/iteration configuration')
    deadline_text = os.environ.get('VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC')
    if deadline_text is None:
        raise ValueError('The process wrapper must declare the total scientific deadline')
    deadline = float(deadline_text)
    if not math.isfinite(deadline):
        raise ValueError('The declared process deadline must be finite')
    star, star_raw = words(H_star)
    root = output.parent.resolve()
    temp = Path(os.environ['RUNNER_TEMP']).resolve()
    if not output.resolve().is_relative_to(temp) or output.resolve() == temp:
        raise ValueError('Regenerable bootstrap output belongs in actual RUNNER_TEMP')
    output.mkdir(exist_ok=False)
    raw_path = output/'original-H-star.f64le'
    raw_path.write_bytes(star_raw)
    bound_input = output/'height-path-input-binding.json'
    atomic(bound_input, dict(schema=SCHEMA, pre_path_adapter_binding=binding,
        original_client_source_sha256=client.sources, original_configuration=client._configuration,
        original_ready=client.ready, policy=policy, H_star=star, H_star_array=height_identity(star)))
    state = dict(schema=SCHEMA, phase='starting', complete_endpoint=False,
        original_full_DN_accepted=False, final_original_audit_done_by_bootstrap=False,
        policy=policy, source_sha256=sha(__file__), source_commit=os.environ.get('GITHUB_SHA'),
        run_id=os.environ.get('GITHUB_RUN_ID'), context_binding=identity(binding),
        input_binding=descriptor(bound_input, root),
        H_star=star, H_star_array=height_identity(star), H_star_raw=descriptor(raw_path, root),
        original_client_source_identity=identity(client.sources),
        original_runtime_configuration_identity=identity(client._configuration),
        original_ready_identity=identity(client.ready), original_worker_pid=client.proc.pid,
        same_worker_and_owner=True, no_cache_or_worker_last_assignment=True,
        original_internal_withJ_is_still_run_when_request_jacobian_false=True,
        complete_fresh_original_R273_correction=True,original_local_graph_correction_replaced=True,
        original_tangent_warm_predictor_retained=True,eta_cli_text='1',
        current_withJ_implementation='original64-noJ-primal-recorded-factor-contracted-finite-root-variation-v1',
        IEEE_rounding_map_derivative_not_claimed=True,
        original_warm_algorithm_may_use_new_current_tangent_values=True,
        checkpoint_JSON_negative_zero_preservation_claimed=False,
        last_converged_s=None, last_converged_call=None, requests=[],
        proposed_increment=policy['initial_positive_increment'], resource_partial=False,
        failure_at_zero_is_not_a_positive_path_nonexistence_claim=True)
    status_file, journal = output/'height-path-status.json', output/'height-path-requests.jsonl'
    journal.touch(exist_ok=False)

    def save():
        atomic(status_file, state)

    def finish(outcome, *, partial=False, response=None):
        state.update(phase=outcome, resource_partial=bool(partial),
            complete_endpoint=response is not None, completed_bootstrap_request_count=len(state['requests']))
        save()
        receipt = descriptor(status_file, root)
        print(json.dumps(clean(dict(event='request208_height_path_finished',
            phase=outcome, complete_endpoint=state['complete_endpoint'],
            last_converged_s=state['last_converged_s'], last_converged_call=state['last_converged_call'],
            request_count=len(state['requests']), resource_partial=bool(partial),
            status=receipt, original_full_DN_accepted=False)), allow_nan=False), flush=True)
        if response is None:
            raise HeightPathStopped(outcome, receipt, partial)
        return response, receipt

    save()
    step, zero = policy['initial_positive_increment'], True
    while True:
        if len(state['requests']) >= policy['maximum_bootstrap_requests']:
            return finish('maximum-bootstrap-requests-partial', partial=True)
        if time.monotonic() >= deadline:
            return finish('total-wall-clock-between-requests-partial', partial=True)
        last = state['last_converged_s']
        proposed = 0.0 if zero else min(1.0, last+step)
        delta_s = 0.0 if zero else proposed-last
        endpoint = proposed == 1.0
        requested = ([0.0]*112 if zero else list(star) if endpoint
                     else [proposed*x for x in star])
        request_H = height_identity(requested)
        if endpoint and request_H != state['H_star_array']:
            raise RuntimeError('Endpoint must retain every original H-star word')
        jacobian = bool(endpoint)
        before, cached = client.calls, client.cache_value
        cached_height = None if client.cache_key is None else words(client.cache_key)[1]
        trace_path, trials_path = Path(client._configuration['traceFile']), Path(client._configuration['trialDiagnosticFile'])
        trace_start, trial_start = offset(trace_path), offset(trials_path)
        row = dict(request_index=len(state['requests'])+1, native_call=before+1,
            phase='request-in-flight', proposed_s=proposed, previous_converged_s=last,
            proposed_increment=delta_s, requested_H=request_H,
            requested_jacobian=jacobian, requested_audit=False, exact_H_star_copy=endpoint,
            zero_request=zero, accepted=False, original_client_calls_before=before,
            remaining_wall_clock_seconds=max(0.0, deadline-time.monotonic()),
            response_observed=False, original_full_DN_accepted=False)
        state['requests'].append(row)
        state.update(phase='original-request-in-flight', proposed_increment=step)
        save()
        print(json.dumps(clean(dict(event='request208_height_path_request_started', **row)),
                         allow_nan=False), flush=True)
        answer, failure = None, None
        try:
            answer = owner.solve(requested, jacobian=jacobian, audit=False)
        except Exception as error:
            failure = error
            row.update(python_exception=repr(error), python_traceback=traceback.format_exc())
        try:
            row['original_client_calls_after'] = client.calls
            if client.calls != before+1:
                raise ValueError('The bootstrap request did not produce exactly one new original call')
            trace_rows, trace_copy = tail_jsonl(trace_path, trace_start,
                output/f'request-{row["request_index"]:03d}-trace.jsonl', root)
            trial_rows, trial_copy = tail_jsonl(trials_path, trial_start,
                output/f'request-{row["request_index"]:03d}-trials.jsonl', root)
            record, response, record_identity = bind_original_record(
                client, client.calls, requested, jacobian, trace_rows, trial_rows, root)
            row.update(response_observed=True, original_record=record_identity,
                original_trace_slice=trace_copy, original_trial_slice=trial_copy,
                original_trace_count=len(trace_rows), original_trial_count=len(trial_rows),
                original_response=response_view(response), original_request_seconds=record.get('seconds'),
                original_source_identity=identity(record['source_sha256']),
                original_config_identity=identity(record['config']),
                trace_events=[{k:v for k,v in event.items() if k != 'height'} for event in trace_rows],
                original_trials=trial_rows, existing_failure_context=failure_context(trace_rows, trial_rows, response))
            terminals = [x for x in trace_rows if x.get('event') in ('response', 'failure')]
            if failure is None:
                if (answer is None or answer != response or response.get('converged') is not True
                        or response.get('failed') or len(terminals) != 1
                        or terminals[0].get('event') != 'response'
                        or terminals[0].get('converged') is not True):
                    raise ValueError('Successful client validation differs from its original saved response/trace')
                row.update(phase='original-native-converged', accepted=True,
                    original_client_all_requested_jet_J_and_residual_checks_passed=True)
                state.update(last_converged_s=proposed, last_converged_call=client.calls)
            else:
                failed = response.get('failed')
                known_exception = (isinstance(failed, str) and original_math_error(failed)
                    and len(terminals) == 1 and terminals[0].get('event') == 'failure'
                    and terminals[0].get('error') == failed)
                normal_nonconvergence = (not failed and response.get('converged') is False
                    and len(terminals) == 1 and terminals[0].get('event') == 'response'
                    and terminals[0].get('converged') is False)
                if not isinstance(failure, FloatingPointError) or not (known_exception or normal_nonconvergence):
                    raise ValueError('Not an unambiguous identity-bound original mathematical refusal')
                now_height = None if client.cache_key is None else words(client.cache_key)[1]
                if client.cache_value is not cached or now_height != cached_height:
                    raise ValueError('Rejected call changed the Python cache; do not guess worker last')
                row.update(phase='original-mathematical-refusal', mathematical_refusal=True,
                    original_last_retention_scope='Pinned worker updates last only after sol.converged; this call recorded no converged response.',
                    original_python_cache_unchanged=True, accepted_trial_recovery_checkpoint_not_promoted=True)
        except Exception as error:
            row.update(phase='protocol-or-record-partial', binding_or_protocol_exception=repr(error),
                binding_or_protocol_traceback=traceback.format_exc(),
                worker_last_may_have_advanced_and_is_not_assumed_unchanged=True)
            save()
            with journal.open('ab') as stream:
                stream.write(encode(row)+b'\n')
            print(json.dumps(clean(dict(event='request208_height_path_request_returned', **row)),
                             allow_nan=False), flush=True)
            return finish('protocol-or-record-partial', partial=True)
        with journal.open('ab') as stream:
            stream.write(encode(row)+b'\n')
        save()
        print(json.dumps(clean(dict(event='request208_height_path_request_returned', **row)),
                         allow_nan=False), flush=True)
        if row['accepted']:
            if endpoint:
                return finish('original-H-star-full-J-converged', response=answer)
            if zero:
                zero, step = False, policy['initial_positive_increment']
            else:
                step = min(policy['maximum_increment'], policy['accepted_increment_multiplier']*delta_s)
        else:
            if zero:
                return finish('zero-height-original-mathematical-refusal')
            return finish('first-positive-original-mathematical-refusal-no-height-retry')
        state['proposed_increment'] = step
        save()
