#!/usr/bin/env python3
"""Temporary orchestration of separate, unchanged original eight-direction runs.

No model is imported here.  Each scientific child starts the frozen six-control
entry with radius .1, performs all of its own final checks, and exits before
the frozen scalar reader runs.  Only literal parameters and genuine provenance
are carried into the next short recipe.  All numerical work is Actions-only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import struct
import subprocess
import sys
import time
import uuid

REPOSITORY = 'Rogerhu12/math-research-public'
ENTRY = 'geometry_20261115_six_control_temporary_batches.py'
SCIENCE = 'geometry_20261115_small_core_six_control_curved_recipe.py'
SCIENCE_SHA = 'e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761'
FAMILY = 'geometry_20261115_small_core_six_control_family.py'
FAMILY_SHA = '79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf'
READER = 'root_20261115_small_core_six_control_curved_scalar_readout.py'
READER_SHA = '3e2c0515ee9759162e3736915674c86ca9a56441f2a7561df9dc09d37fea4d45'
SCHEMA = 'same-six-control-original-eight-direction-temporary-batches-v1'
REQUEST_SCHEMA = 'public-six-control-temporary-batch-request-v1'
SCIENCE_SCHEMA = 'R259-six-control-full-three-two-normal-curved-trust-recipe-v1'
RECIPE_SCHEMA = 'R259-explicit-six-control-odd-shape-recipe-v1'
READER_SCHEMA = 'request117-original-six-control-full3-curved-trust-scalar-readback-no-raw-retention-v1'
STATUS_NAME = 'six-control-curved-status.json'
BUDGET_STOP = 'explicit total direction budget completed, counting accepted and rejected directions'
SEMANTICS = 'original-full-three-merit-accepted-curved-candidate-or-fresh-recipe'
LIMIT = 90000
OPTIONS = dict(initial_relative_radius=.1, candidate_steps=8, backtracks=20,
    normal_iterations=12, normal_backtracks=20, normal_target_tolerance=1e-8,
    candidate_resonance_tolerance=1e-8, interval_bits=160, interval_depth=14)
CHAIN = dict(max_batches=8, chain_budget_seconds=3600,
    budget_checked_only_between_complete_batches=True,
    reset_initial_relative_radius_each_batch=.1,
    carry_final_relative_trust_radius=False,
    one_continuous_sixty_four_direction_solve=False)
INITIAL_RUN = '43691986785'
INITIAL_COMMIT = '8e52679dcf3b934c2c488915c4b9622be6e6bf3c'
INITIAL_STATUS_SHA = 'd6d16e0da855325b97fc130a052743a8a9b51154382aecb29313e7be40011cef'
INITIAL_SUMMARY_SHA = '14b3c8afe2a4fb03537a6d16dd4c55d44a37d750750ee25aef3bf157a026ac6b'
INITIAL_PARAMETERS = [0.42123313016645575, 0.2168136988206389, 0.5629172159488391,
    -0.1326982215718915, 0.00881492232668194, 0.08635618490039039]


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise RuntimeError('Execute only in the named public repository Actions')


def encode(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
                      separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def decode(raw):
    def reject(value):
        raise ValueError('Nonstandard JSON constant: '+value)
    return json.loads(raw.decode('utf-8'), parse_constant=reject)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def hex_digest(value, length=64):
    return isinstance(value, str) and len(value) == length and all(c in '0123456789abcdef' for c in value)


def receipt(path, root=None):
    path = Path(path)
    check(path.is_file() and not path.is_symlink(), 'Expected a regular owned file: '+str(path))
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            h.update(block)
    return dict(file=str(path.relative_to(root)) if root else path.name,
                bytes=path.stat().st_size, sha256=h.hexdigest())


def atomic_json(path, value, limit=LIMIT):
    raw = encode(value)
    check(len(raw) <= limit, 'Compact orchestration metadata exceeds its declared byte budget')
    temporary = path.with_name(path.name+'.writing')
    with temporary.open('wb') as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)
    return dict(file=path.name, bytes=len(raw), sha256=digest(raw))


def owned_relative(root, name):
    relative = PurePosixPath(name)
    check(not relative.is_absolute() and '..' not in relative.parts and bool(relative.parts),
          'Use a proper relative path')
    path = root.joinpath(*relative.parts)
    check(not path.is_symlink() and path.resolve().is_relative_to(root.resolve()),
          'Do not follow an out-of-root input or output link')
    return path


def parameters(value):
    check(isinstance(value, list) and len(value) == 6, 'Retain all six literal parameters')
    check(all(not isinstance(v, bool) and isinstance(v, (int, float)) and math.isfinite(v) for v in value),
          'The original parameter recipe requires six finite numbers')
    return list(value)


def parameter_words(value):
    return b''.join(struct.pack('<d', float(v)) for v in parameters(value))


def same_parameters(a, b):
    return parameter_words(a) == parameter_words(b)


def clean_child_environment():
    environment = dict(os.environ)
    for name in list(environment):
        if (name in ('GITHUB_OUTPUT', 'GH_TOKEN', 'GITHUB_TOKEN', 'MR_TOKEN',
                     'GIT_ASKPASS', 'SSH_ASKPASS') or name.startswith('GIT_CONFIG_')):
            environment.pop(name, None)
    return environment


def bind(args):
    repository = args.repository_directory.resolve()
    computations = Path(__file__).resolve().parent
    raw = args.request.read_bytes()
    check(hex_digest(args.request_sha256) and digest(raw) == args.request_sha256,
          'Bind the complete current request bytes')
    request = decode(raw)
    check(request['schema'] == REQUEST_SCHEMA and request['repository'] == REPOSITORY
          and request['request_number'] == 119, 'Use the distinct request119 contract')
    check(request['execution_entry'] == ENTRY and Path(__file__).name == ENTRY
          and request['scientific_entry'] == SCIENCE, 'Do not replace the original scientific entry')
    check(request['batch_chain'] == CHAIN, 'Retain the explicit eight independent batches and between-batch resource budget')
    check(all(request['diagnostic'][name] == value for name, value in OPTIONS.items()),
          'Do not change any original per-child argument')
    for group, count in (('source_sha256', 82), ('workflow_support_source_sha256', 2)):
        check(len(request[group]) == count, 'Retain the complete engineering source identity set')
        for name, expected in request[group].items():
            check(PurePosixPath(name).name == name and hex_digest(expected), 'Invalid source basename/digest')
            check(receipt(computations/name)['sha256'] == expected, 'Source changed: '+name)
    check(request['source_sha256'][SCIENCE] == SCIENCE_SHA
          and request['source_sha256'][FAMILY] == FAMILY_SHA
          and request['workflow_support_source_sha256'][READER] == READER_SHA,
          'The scientific entry, family and original reader remain frozen')
    closure = request['source_closure']['current_producer']
    check(len(closure) == 24 and request['source_closure']['origin_producer'] == closure
          and all(request['source_sha256'][name] == value for name, value in closure.items()),
          'Both initial origin and current child have the same complete twenty-four-source closure')
    input_hashes = {}
    for name in ('accepted', 'prepared', 'tail_anchor', 'tail_config'):
        item = request['inputs'][name]
        found = receipt(owned_relative(repository, item['file']))
        check(found['bytes'] == item['bytes'] and found['sha256'] == item['sha256'],
              'Original mathematical input differs: '+name)
        input_hashes[name] = item['sha256']
    item = request['parameter_recipe']
    recipe_raw = owned_relative(repository, item['file']).read_bytes()
    check(len(recipe_raw) == item['bytes'] and digest(recipe_raw) == item['sha256'],
          'The actual117 initial recipe bytes differ')
    recipe = decode(recipe_raw)
    check(set(recipe) == {'schema', 'origin', 'literal_parameters', 'input_sha256', 'family'}
          and recipe['schema'] == RECIPE_SCHEMA and recipe['input_sha256'] == input_hashes
          and recipe['family'] == item['family'] and recipe['origin'] == item['origin'],
          'Preserve the exact frozen recipe input contract')
    check(same_parameters(recipe['literal_parameters'], INITIAL_PARAMETERS)
          and same_parameters(request['diagnostic']['parameters'], INITIAL_PARAMETERS),
          'Start at the six actual117 final.parameters words, without a radius parameter')
    origin = recipe['origin']
    check(origin == dict(repository=REPOSITORY, run_id=INITIAL_RUN, source_commit=INITIAL_COMMIT,
          producer_file=SCIENCE, producer_sha256=SCIENCE_SHA, producer_schema=SCIENCE_SCHEMA,
          status_bytes=1210862, status_sha256=INITIAL_STATUS_SHA,
          log_summary_bytes=88323, log_summary_sha256=INITIAL_SUMMARY_SHA,
          parameter_field='final.parameters'), 'Do not relabel the actual117 origin')
    check(os.environ.get('GITHUB_RUN_ID', '').isdigit()
          and hex_digest(os.environ.get('GITHUB_SHA'), 40), 'Use the actual current Actions run and source')
    return request, repository, computations, recipe_raw, recipe


def science_argv(request, repository, computations, recipe_path, recipe_sha, output):
    argv = [sys.executable, '-u', str(computations/SCIENCE)]
    for name in ('accepted', 'prepared', 'tail_anchor', 'tail_config'):
        argv += ['--'+name.replace('_', '-'), str(owned_relative(repository, request['inputs'][name]['file']))]
    argv += ['--parameter-recipe', str(recipe_path), '--parameter-recipe-sha256', recipe_sha]
    for name, value in OPTIONS.items():
        argv += ['--'+name.replace('_', '-'), str(value)]
    argv += ['--out', str(output)]
    return argv


class Processes:
    """Keep children in the original rules-runner process group."""
    def __init__(self):
        self.active = None
        self.signal_number = None

    def interrupted(self, signum, frame):
        self.signal_number = signum
        if self.active is not None and self.active.poll() is None:
            try:
                self.active.send_signal(signum)
            except ProcessLookupError:
                pass

    def run(self, argv, cwd, environment, stdout, stderr):
        # No child timeout and no new session: the original per-child numerical
        # budget is unchanged and the outer rules-runner can stop the full group.
        with stdout.open('wb') as out_handle, stderr.open('wb') as err_handle:
            self.active = subprocess.Popen(argv, cwd=cwd, env=environment, shell=False,
                                           stdout=out_handle, stderr=err_handle)
            try:
                return self.active.wait()
            finally:
                self.active = None


def parse_reader_output(path):
    raw = path.read_bytes()
    match = re.fullmatch(
        rb'scalar_summary<<([A-Za-z0-9_]+)\n(.*?)\n\1\n'
        rb'scalar_summary_bytes=([0-9]+)\nscalar_summary_sha256=([0-9a-f]{64})\n', raw, re.S)
    check(match is not None, 'The separate original reader GITHUB_OUTPUT protocol is incomplete')
    summary = match[2]
    check(len(summary) <= LIMIT and len(summary) == int(match[3])
          and digest(summary) == match[4].decode(), 'The original scalar summary byte identity differs')
    value = decode(summary)
    check(value.get('run_id') == os.environ['GITHUB_RUN_ID']
          and value.get('source_commit') == os.environ['GITHUB_SHA'],
          'The original reader must record this actual run/source')
    return summary, value


def emit_original_summary(number, raw):
    label = 'VISIBLE119_BATCH_'+str(number).zfill(3)+'_ORIGINAL117_SUMMARY'
    print('BEGIN_'+label, flush=True)
    print(raw.decode('utf-8'), flush=True)
    print('END_'+label, flush=True)
    print(encode(dict(event='visible119-original-batch-summary-sha256', batch=number,
        bytes=len(raw), sha256=digest(raw), original_reader_file=READER,
        original_reader_sha256=READER_SHA, original_reader_schema_unchanged=True,
        hash_scope='UTF-8 original compact JSON string excluding separator LF',
        run_id=os.environ['GITHUB_RUN_ID'], source_commit=os.environ['GITHUB_SHA'])).decode(), flush=True)


def read_status(science_directory, request, incoming, summary):
    path = science_directory/STATUS_NAME
    if not path.is_file():
        return None, dict(present=False, complete_status_read=False)
    raw = path.read_bytes()
    value = decode(raw)
    record = dict(present=True, complete_status_read=True,
        original_status=dict(file=STATUS_NAME, bytes=len(raw), sha256=digest(raw)))
    check(value['schema'] == SCIENCE_SCHEMA and value['source_sha256'] == SCIENCE_SHA
          and value['consumed_source_sha256'] == request['source_closure']['current_producer'],
          'Do not relabel a different child producer or source closure')
    check(value['input_sha256'] == incoming['input_sha256']
          and value['parameter_recipe']['family'] == incoming['family']
          and value['parameter_recipe']['origin'] == incoming['origin']
          and same_parameters(value['parameter_recipe']['literal_parameters'], incoming['literal_parameters']),
          'The actual child must consume this exact literal recipe and family')
    if 'initial' in value:
        check(same_parameters(value['initial']['parameters'], incoming['literal_parameters']),
              'The original fresh initial state must be at the supplied recipe parameters')
    if summary.get('original_status') is not None:
        check(summary['original_status'] == record['original_status'],
              'Reader summary must come from the complete original status just read')
    record['source_sha256'] = value['source_sha256']
    closure_raw = encode(value['consumed_source_sha256'])
    record['consumed_source_closure'] = dict(count=24, canonical_bytes=len(closure_raw),
        canonical_sha256=digest(closure_raw), equals_declared_original_closure=True)
    record['input_sha256'] = value['input_sha256']
    record['scalar_control_family_identity'] = incoming['family']
    trace = value.get('original_call_trace')
    if isinstance(trace, dict) and isinstance(trace.get('file'), dict):
        descriptor = trace['file']
        actual = receipt(owned_relative(science_directory, descriptor['file']), science_directory)
        check(actual == descriptor, 'The original complete evaluation trace bytes differ')
        record['original_trace'] = actual
        record['original_trace_counts'] = trace.get('counts')
        record['original_trace_observer_errors'] = trace.get('observer_errors')
    for name in ('phase', 'diagnostic_completed', 'exception', 'search_stop_reason',
                 'total_direction_attempts', 'original_Armijo_accepted_point_count',
                 'rejected_direction_count', 'last_accepted_point_semantics',
                 'initial_relative_trust_radius', 'final_relative_trust_radius',
                 'initial_original_three_equation_merit', 'final_original_three_equation_merit',
                 'original_unit_stopping_tolerance_met',
                 'low_mode_candidate_has_small_full_recorded_right_residual',
                 'full_nonlinear_nonzero_lambda_solution_computed', 'success'):
        if name in value:
            record[name] = value[name]
    if isinstance(value.get('final'), dict) and 'parameters' in value['final']:
        record['final_parameters'] = parameters(value['final']['parameters'])
        if 'last_accepted_parameters' in value:
            check(same_parameters(record['final_parameters'], value['last_accepted_parameters']),
                  'Do not choose parameters other than the original final/last accepted point')
    return value, record


def genuine_next_recipe(status, status_record, summary_raw, request):
    check(status_record['complete_status_read'] and status.get('diagnostic_completed') is True
          and status.get('phase') == 'diagnostic-completed'
          and status.get('last_accepted_point_semantics') == SEMANTICS,
          'Only a completely read original child final point can produce another recipe')
    summary = decode(summary_raw)
    check(summary.get('schema') == READER_SCHEMA
          and summary['original_status'] == status_record['original_status']
          and same_parameters(summary['final']['parameters'], status['final']['parameters']),
          'Retain the genuine complete original reader summary and final point')
    descriptor = status_record['original_status']
    return dict(schema=RECIPE_SCHEMA,
        origin=dict(repository=REPOSITORY, run_id=os.environ['GITHUB_RUN_ID'],
            source_commit=os.environ['GITHUB_SHA'], producer_file=SCIENCE,
            producer_sha256=SCIENCE_SHA, producer_schema=SCIENCE_SCHEMA,
            status_bytes=descriptor['bytes'], status_sha256=descriptor['sha256'],
            log_summary_bytes=len(summary_raw), log_summary_sha256=digest(summary_raw),
            parameter_field='final.parameters'),
        literal_parameters=parameters(status['final']['parameters']),
        input_sha256=status['input_sha256'], family=request['parameter_recipe']['family'])


def original_stop(status, child_code, summary_schema, interrupted):
    if interrupted is not None:
        return 'external_resource_or_rules_signal', 128+interrupted
    if child_code != 0:
        return 'original_child_process_failed', child_code if child_code > 0 else 128-child_code
    if status is None or status.get('phase') != 'diagnostic-completed' or status.get('diagnostic_completed') is not True:
        return 'original_child_incomplete_or_exception', 70
    if status.get('exception') is not None:
        return 'original_child_exception', 70
    if summary_schema != READER_SCHEMA:
        return 'original_reader_did_not_return_complete_scalar_summary', 70
    if status.get('original_unit_stopping_tolerance_met') is True:
        return 'original_unit_stopping_flag_true', 0
    if status.get('low_mode_candidate_has_small_full_recorded_right_residual') is True:
        return 'original_full112_candidate_flag_true', 0
    accepted = status.get('original_Armijo_accepted_point_count')
    check(type(accepted) is int and accepted >= 0, 'Preserve the original integer accepted-point count')
    if accepted == 0:
        return 'zero_original_accepted_points', 0
    if status.get('search_stop_reason') != BUDGET_STOP or status.get('total_direction_attempts') != 8:
        return 'original_non_eight_direction_budget_stop', 0
    return None, 0


def run(args):
    request, repository, computations, recipe_raw, incoming = bind(args)
    check(not args.out.exists(), 'Use a new owned orchestration directory')
    args.out.mkdir(parents=True)
    output = args.out.resolve()
    recipes = output/'recipes'
    recipes.mkdir()
    current_recipe = recipes/'batch-001.json'
    current_recipe.write_bytes(recipe_raw)
    processes = Processes()
    for signum in (signal.SIGTERM, signal.SIGINT):
        signal.signal(signum, processes.interrupted)
    start = time.monotonic()
    chain = dict(schema=SCHEMA, phase='starting', source_sha256=receipt(__file__)['sha256'],
        request_sha256=args.request_sha256, run_id=os.environ['GITHUB_RUN_ID'],
        source_commit=os.environ['GITHUB_SHA'], scientific_entry=SCIENCE,
        scientific_source_sha256=SCIENCE_SHA, family_source_sha256=FAMILY_SHA,
        original_reader_source_sha256=READER_SHA,
        source_closure=request['source_closure']['current_producer'],
        batch_chain=CHAIN, original_child_options=OPTIONS,
        original117_origin=incoming['origin'], initial_parameters=incoming['literal_parameters'],
        first_origin_status_payload_read_in_this_run=False,
        first_origin_from_previously_read_actual117_original_summary=True,
        subsequent_recipe_status_and_summary_payloads_fully_read_in_this_run=True,
        next_child_receipt_claims_only_what_frozen_child_itself_reads=True,
        independent_processes_with_fresh_initial_J_and_all_final_checks=True,
        radius_reset_is_explicit_algorithmic_initialization_not_saved_trust_continuation=True,
        old_merit_J_states_FD_domain_or_circle_reused=False,
        cross_batch_merit_arithmetic_performed=False,
        scientific_acceptance_rules_modified=False, no_new_mathematical_acceptance_gate=True,
        native_BVP_or_surface_completion_claimed=False,
        raw_artifact_Release_or_Git_upload=False, original_summaries_printed_separately=True,
        per_original_summary_limit_bytes=LIMIT, eight_summaries_never_combined_under_one_limit=True,
        batches=[], stop_reason=None, wrapper_exception=None, exit_code=None)
    ledger = output/'chain-metadata.json'
    atomic_json(ledger, chain)
    code = 0
    try:
        for number in range(1, CHAIN['max_batches']+1):
            if processes.signal_number is not None:
                chain['stop_reason'] = 'external_resource_or_rules_signal_between_batches'
                code = 128+processes.signal_number
                break
            if time.monotonic()-start >= CHAIN['chain_budget_seconds']:
                chain['stop_reason'] = 'between_batch_resource_budget_exhausted'
                chain['resource_limited_partial_chain'] = True
                break
            batch = output/('batch-'+str(number).zfill(3))
            batch.mkdir()
            science = batch/'science'
            argv = science_argv(request, repository, computations, current_recipe, digest(recipe_raw), science)
            record = dict(batch=number, phase='original_child_running',
                incoming_recipe=receipt(current_recipe, output), incoming_recipe_origin=incoming['origin'],
                initial_parameters=parameters(incoming['literal_parameters']),
                initial_relative_radius=.1, saved_final_radius_not_carried=True,
                scientific_source_sha256=SCIENCE_SHA, original_child_argv=argv,
                raw_cleanup_completed=False)
            chain['batches'].append(record)
            chain['phase'] = 'running'
            atomic_json(ledger, chain)
            began = time.monotonic()
            child_code = processes.run(argv, repository, clean_child_environment(),
                                       batch/'science.stdout', batch/'science.stderr')
            record.update(phase='original_child_exited', child_returncode=child_code,
                elapsed_seconds=time.monotonic()-began,
                scientific_stdout=receipt(batch/'science.stdout', output),
                scientific_stderr=receipt(batch/'science.stderr', output),
                scientific_stdout_stderr_contents_not_uploaded_or_printed=True)
            atomic_json(ledger, chain)
            reader_output = batch/'reader-github-output.txt'
            reader_output.touch(exist_ok=False)
            environment = clean_child_environment()
            environment['GITHUB_OUTPUT'] = str(reader_output)
            outcome = 'cancelled' if processes.signal_number is not None else ('success' if child_code == 0 else 'failure')
            reader_argv = [sys.executable, str(computations/READER), '--directory', str(science),
                           '--rules-directory', str(args.rules_directory), '--compute-outcome', outcome]
            reader_code = processes.run(reader_argv, repository, environment,
                batch/'reader.stdout', batch/'reader.stderr')
            record.update(reader_returncode=reader_code,
                original_reader_stdout=receipt(batch/'reader.stdout', output),
                original_reader_stderr=receipt(batch/'reader.stderr', output),
                original_reader_github_output=receipt(reader_output, output))
            check(reader_code == 0, 'The original scalar reader process failed; retain honest partial metadata')
            summary_raw, summary = parse_reader_output(reader_output)
            emit_original_summary(number, summary_raw)
            record['original_summary'] = dict(bytes=len(summary_raw), sha256=digest(summary_raw),
                schema=summary.get('schema'), printed_complete_original_reader_output=True)
            status, status_record = read_status(science, request, incoming, summary)
            record['original_child'] = status_record
            record['phase'] = 'original_readback_completed'
            stop, code = original_stop(status, child_code, summary.get('schema'), processes.signal_number)
            next_recipe = None
            if (status is not None and status.get('diagnostic_completed') is True
                    and status.get('phase') == 'diagnostic-completed'
                    and summary.get('schema') == READER_SCHEMA):
                next_recipe = genuine_next_recipe(status, status_record, summary_raw, request)
                next_path = recipes/('after-batch-'+str(number).zfill(3)+'.json')
                next_bytes = encode(next_recipe)
                check(len(next_bytes) <= 16384, 'Retain the original short recipe bound')
                next_path.write_bytes(next_bytes)
                record['restart_recipe'] = receipt(next_path, output)
                record['restart_origin_from_fully_read_actual_status_and_original_summary'] = True
                chain['last_restart_recipe'] = dict(**record['restart_recipe'],
                    origin=next_recipe['origin'], literal_parameters=next_recipe['literal_parameters'])
                chain['last_fully_read_parameters'] = next_recipe['literal_parameters']
            record['original_stop_decision'] = stop
            # The entire child status and its genuine reader output have now
            # been read.  Neither future children nor readers reuse this tree.
            atomic_json(ledger, chain)
            shutil.rmtree(batch)
            record['raw_cleanup_completed'] = True
            record['raw_cleanup_after_original_readback'] = True
            atomic_json(ledger, chain)
            if stop is not None:
                chain['stop_reason'] = stop
                break
            if number == CHAIN['max_batches']:
                chain['stop_reason'] = 'explicit_independent_batch_count_completed'
                break
            check(next_recipe is not None, 'Do not continue without a genuine complete next recipe')
            # No parent array or model is in the next child: only this short
            # own-schema provenance tuple and the six round-tripping literals.
            recipe_raw = next_bytes
            incoming = next_recipe
            current_recipe = next_path
        else:
            chain['stop_reason'] = 'explicit_independent_batch_count_completed'
    except Exception as error:
        chain['wrapper_exception'] = repr(error)[:4000]
        chain['stop_reason'] = 'orchestration_or_readback_exception'
        chain['original_child_scientific_outcome_not_relabelled'] = True
        code = 70
    finally:
        chain.update(phase='finished', elapsed_seconds=time.monotonic()-start,
            interrupted_signal=processes.signal_number, exit_code=code,
            batches_started=len(chain['batches']),
            completed_original_readbacks=sum(b.get('phase') == 'original_readback_completed' for b in chain['batches']),
            resource_limited_partial_chain=bool(processes.signal_number is not None
                or chain.get('resource_limited_partial_chain', False)))
        final = atomic_json(ledger, chain)
        print(encode(dict(event='visible119-chain-metadata-prepared', **final,
            stop_reason=chain['stop_reason'], exit_code=code,
            this_event_is_not_a_scientific_success_claim=True)).decode(), flush=True)
    return code


def report(args):
    """Always-step report; no scientific import, child launch, or payload reuse."""
    source = args.out/'chain-metadata.json'
    if source.is_file():
        raw = source.read_bytes()
        result = decode(raw)
        check(result.get('schema') == SCHEMA, 'Use the actual chain metadata schema')
        result['chain_metadata_file'] = dict(file=source.name, bytes=len(raw), sha256=digest(raw))
        result['compute_step_outcome'] = args.compute_outcome
        if result.get('phase') != 'finished':
            result['orchestration_interrupted_before_final_receipt'] = True
            result['scientific_completion_not_claimed'] = True
    else:
        result = dict(schema='request119-chain-output-unavailable-v1',
            compute_step_outcome=args.compute_outcome, run_id=os.environ.get('GITHUB_RUN_ID'),
            source_commit=os.environ.get('GITHUB_SHA'), scientific_completion_not_claimed=True)
    result['actual_rule_sync'] = []
    if args.rules_directory.is_dir():
        paths = sorted(args.rules_directory.glob('sync-*-completed.json'))
        if (args.rules_directory/'runner-result.json').is_file():
            paths.append(args.rules_directory/'runner-result.json')
        for path in paths:
            raw = path.read_bytes()
            result['actual_rule_sync'].append(dict(receipt=receipt(path), original=decode(raw)))
    raw = encode(result)
    check(len(raw) <= LIMIT, 'Chain metadata only, not a concatenation of original scientific summaries, must stay compact')
    delimiter = 'VISIBLE119_'+uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as handle:
        handle.write('chain_summary<<'+delimiter+'\n'+raw.decode()+'\n'+delimiter+'\n')
        handle.write('chain_summary_bytes='+str(len(raw))+'\n')
        handle.write('chain_summary_sha256='+digest(raw)+'\n')
    print(encode(dict(event='visible119-chain-output-prepared', bytes=len(raw), sha256=digest(raw),
        hash_scope='UTF-8 compact chain JSON excluding separator LF',
        independent_original_batch_summaries_are_in_compute_stdout=True,
        mathematical_acceptance_not_inferred_from_process_success=True)).decode(), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', type=Path)
    parser.add_argument('--request-sha256')
    parser.add_argument('--repository-directory', type=Path)
    parser.add_argument('--rules-directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--report-only', action='store_true')
    parser.add_argument('--compute-outcome')
    args = parser.parse_args()
    require_actions()
    if args.report_only:
        check(bool(args.compute_outcome), 'Keep the real science-step outcome in the always report')
        return report(args)
    check(args.request is not None and args.request_sha256 is not None
          and args.repository_directory is not None, 'Supply the complete current request and repository')
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
