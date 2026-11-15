#!/usr/bin/env python3
"""One original eight-direction complete-response run with actual-radius carry.

No model is imported here. Each child starts the independent carried-radius
entry at the actual previous final parameters and radius, completes every
original final check, then exits before the identity-specific scalar reader.
No old Jacobian, merit or accepted field is reused. All numerical work is
Actions-only; the original numerical helpers and stop rules are retained.
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
ENTRY = 'geometry_20261115_nine_control_directional_response_temporary_batch.py'
CARRIED_WRAPPER = 'geometry_20261115_nine_control_carried_radius_temporary_batches.py'
CARRIED_WRAPPER_SHA = 'df856e9ecf9d9bbd52c7c515d75aed0a50efbfd0f54126ec9dd07eed48521209'
CARRIED_SCIENCE = 'geometry_20261115_small_core_nine_control_carried_radius_recipe.py'
CARRIED_SCIENCE_SHA = 'ed78684f93c76cf1695a3a54f04d28528b5505fccf115b6fd6afddc7a657cd50'
CARRIED_READER = 'root_20261115_small_core_nine_control_carried_radius_scalar_readout.py'
CARRIED_READER_SHA = '24c5ff04203965bf49ab3a559eaaaa5b90ecccd16a58cc87eb148676cf885cd2'
SAME_TRACE_SCIENCE = 'geometry_20261115_small_core_nine_control_same_trace_merit_recipe.py'
SAME_TRACE_SCIENCE_SHA = 'e8704af6daa13eac4d0301a6ef1debdca4c9cb0b10a806544644a2e1d162329a'
SAME_TRACE_SCIENCE_SCHEMA = 'R259-nine-control-full-three-two-normal-same-trace-merit-carried-radius-trust-recipe-v1'
SAME_TRACE_WRAPPER = 'geometry_20261115_nine_control_same_trace_merit_temporary_batches.py'
SAME_TRACE_WRAPPER_SHA = '79c178f4ea76880e0a1cc01ead06cf95fb0e98e74f8f6b8dacedfa98b5f95ad6'
SAME_TRACE_READER = 'root_20261115_small_core_nine_control_same_trace_merit_scalar_readout.py'
SAME_TRACE_READER_SHA = '4973404938189fc37b8563508da7212959a34d1527abd1c5910f717f27e504cd'
RESPONSE_HELPER = 'geometry_20261115_nine_control_directional_complex_response.py'
RESPONSE_HELPER_SHA = '50044473f14b34c9451360debaa1ec9189f0a7924957098cafc37df3f849643f'
SELECTOR = 'geometry_20261115_nine_control_same_trace_full_merit_candidate.py'
SELECTOR_SHA = 'd4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf'
RESET_WRAPPER = 'geometry_20261115_nine_control_thirty_two_temporary_batches.py'
RESET_WRAPPER_SHA = 'fd5d78f3a24b4f5bbcb38c59bc25ca9405244f6253de5438bc00776b4e1fb5bb'
ORIGINAL_NINE = 'geometry_20261115_small_core_nine_control_curved_recipe.py'
ORIGINAL_NINE_SHA = '824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf'
ORIGINAL_NINE_SCHEMA = 'R259-nine-control-full-three-two-normal-curved-trust-recipe-v1'
ORIGINAL_READER = 'root_20261115_small_core_nine_control_curved_scalar_readout.py'
ORIGINAL_READER_SHA = 'f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d'
BASELINE_ENTRY = 'geometry_20261115_nine_control_temporary_batches.py'
BASELINE_ENTRY_SHA = 'b15a6571a1ebc5dc72f1037212fd86a10d7a5848957c2faca4ae9e7fd69f21bb'
SCIENCE = 'geometry_20261115_small_core_nine_control_directional_response_recipe.py'
SCIENCE_SHA = '5acf5b029a756a356a3de3d598211eaa89df4a7670fc703f2d3567488e09bae4'
FAMILY = 'geometry_20261115_small_core_nine_control_family.py'
FAMILY_SHA = '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'
READER = 'root_20261115_small_core_nine_control_directional_response_scalar_readout.py'
READER_SHA = 'f3a236a3b1a18ad8eacaafe32e166cb8c5d7c96d1cd9a7a6573f0105156073f6'
SCHEMA = 'same-nine-control-complete-directional-response-eight-direction-single-temporary-batch-v1'
REQUEST_SCHEMA = 'public-nine-control-complete-directional-response-single-temporary-batch-request-v1'
SCIENCE_SCHEMA = 'R259-nine-control-full-three-complete-directional-response-carried-radius-trust-recipe-v1'
RECIPE_SCHEMA = 'R259-explicit-nine-control-parameters-and-radius-recipe-v1'
READER_SCHEMA = 'nine-control-complete-directional-response-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1'
STATUS_NAME = 'nine-control-directional-response-carried-radius-status.json'
BUDGET_STOP = 'explicit total direction budget completed, counting accepted and rejected directions'
SEMANTICS = 'original-full-three-merit-accepted-curved-candidate-or-fresh-recipe'
LIMIT = 90000
OPTIONS = dict(candidate_steps=8, backtracks=20,
    normal_iterations=12, normal_backtracks=20, normal_target_tolerance=1e-8,
    candidate_resonance_tolerance=1e-8, interval_bits=160, interval_depth=14)
CHAIN = dict(max_batches=1, chain_budget_seconds=3600,
    budget_checked_only_between_complete_batches=True,
    reset_initial_relative_radius_each_batch=False,
    carry_final_relative_trust_radius=True,
    one_atomic_original_eight_direction_child=True)


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


def atomic_json(path, value, limit=None):
    raw = encode(value)
    if limit is not None:
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
    check(isinstance(value, list) and len(value) == 9, 'Retain all nine literal parameters')
    check(all(not isinstance(v, bool) and isinstance(v, (int, float)) and math.isfinite(v) for v in value),
          'The original parameter recipe requires nine finite numbers')
    return list(value)


def parameter_words(value):
    return b''.join(struct.pack('<d', float(v)) for v in parameters(value))


def same_parameters(a, b):
    return parameter_words(a) == parameter_words(b)


def radius(value):
    check(not isinstance(value, bool) and isinstance(value, (int, float))
          and math.isfinite(value) and 0 <= value <= 1,
          'Preserve a finite actual original final radius in its reachable range, including zero')
    return value


def same_radius(a, b):
    return struct.pack('<d', float(radius(a))) == struct.pack('<d', float(radius(b)))


def clean_child_environment():
    environment = dict(os.environ)
    for name in list(environment):
        if (name in ('GITHUB_OUTPUT', 'GH_TOKEN', 'GITHUB_TOKEN', 'MR_TOKEN', 'MR_READ_TOKEN',
                     'GIT_ASKPASS', 'SSH_ASKPASS') or name.startswith('GIT_CONFIG_')):
            environment.pop(name, None)
    return environment


def bind(args):
    """Bind explicit future request/recipe; no run or parameter is preselected."""
    repository = args.repository_directory.resolve()
    computations = Path(__file__).resolve().parent
    runner = Path(os.environ['RUNNER_TEMP']).resolve()
    raw = args.request.read_bytes()
    check(hex_digest(args.request_sha256) and digest(raw) == args.request_sha256,
          'Bind the complete current request bytes')
    request = decode(raw)
    check(request['schema'] == REQUEST_SCHEMA and request['repository'] == REPOSITORY
          and type(request['request_number']) is int and request['request_number'] > 0,
          'Use the independent own-nine temporary-batch request contract')
    check(request['execution_entry'] == ENTRY and Path(__file__).name == ENTRY
          and request['scientific_entry'] == SCIENCE,
          'Do not replace the original scientific entry')
    check(request['batch_chain'] == CHAIN,
          'Retain exactly one possible eight-direction child and the original between-batch budget')
    check(all(request['diagnostic'][name] == value for name, value in OPTIONS.items()),
          'Do not change any original per-child argument')
    for group, count in (('source_sha256', 93), ('workflow_support_source_sha256', 5)):
        check(len(request[group]) == count, 'Retain all original sources plus this independent wrapper')
        for name, expected in request[group].items():
            check(PurePosixPath(name).name == name and hex_digest(expected),
                  'Invalid source basename/digest')
            check(receipt(computations/name)['sha256'] == expected, 'Source changed: '+name)
    check(request['source_sha256'][SCIENCE] == SCIENCE_SHA
          and request['source_sha256'][FAMILY] == FAMILY_SHA
          and request['source_sha256'][ENTRY] == receipt(__file__)['sha256']
          and request['source_sha256'][BASELINE_ENTRY] == BASELINE_ENTRY_SHA
          and request['source_sha256'][RESET_WRAPPER] == RESET_WRAPPER_SHA
          and request['source_sha256'][ORIGINAL_NINE] == ORIGINAL_NINE_SHA
          and request['workflow_support_source_sha256'][ORIGINAL_READER] == ORIGINAL_READER_SHA
          and request['workflow_support_source_sha256'][READER] == READER_SHA
          and request['source_sha256'][CARRIED_WRAPPER] == CARRIED_WRAPPER_SHA
          and request['source_sha256'][CARRIED_SCIENCE] == CARRIED_SCIENCE_SHA
          and request['source_sha256'][SELECTOR] == SELECTOR_SHA
          and request['workflow_support_source_sha256'][CARRIED_READER] == CARRIED_READER_SHA
          and request['source_sha256'][SAME_TRACE_SCIENCE] == SAME_TRACE_SCIENCE_SHA
          and request['source_sha256'][SAME_TRACE_WRAPPER] == SAME_TRACE_WRAPPER_SHA
          and request['workflow_support_source_sha256'][SAME_TRACE_READER] == SAME_TRACE_READER_SHA
          and request['source_sha256'][RESPONSE_HELPER] == RESPONSE_HELPER_SHA,
          'Bind the independent child/reader/wrapper and retain both old wrappers and original source identities')
    closure = request['source_closure']['current_producer']
    same_trace_closure = {name:value for name,value in closure.items()
                         if name not in (SCIENCE, RESPONSE_HELPER)}
    original_closure = {name:value for name,value in same_trace_closure.items()
                        if name not in (SAME_TRACE_SCIENCE, CARRIED_SCIENCE, SELECTOR)}
    check(len(closure) == 31 and len(same_trace_closure) == 29 and len(original_closure) == 26
          and closure.get(SCIENCE) == SCIENCE_SHA
          and closure.get(RESPONSE_HELPER) == RESPONSE_HELPER_SHA
          and same_trace_closure.get(SAME_TRACE_SCIENCE) == SAME_TRACE_SCIENCE_SHA
          and original_closure.get(ORIGINAL_NINE) == ORIGINAL_NINE_SHA
          and all(request['source_sha256'][name] == value for name, value in closure.items()),
          'Retain current31, actual138 parent29 and original nine26 source closures')
    # All large original inputs have already been restored by the workflow
    # to request-owned RUNNER_TEMP paths; no cleared main raw path is consumed.
    path_file = args.original_input_paths
    check(path_file.is_file() and not path_file.is_symlink()
          and path_file.resolve().is_relative_to(runner),
          'Use the explicit temporary original-input path map')
    paths = decode(path_file.read_bytes())
    input_names = ('accepted', 'prepared', 'tail_anchor', 'tail_config')
    check(set(paths) == set(input_names), 'Retain exactly the four original mathematical inputs')
    input_hashes, actual_paths = {}, {}
    for name in input_names:
        item = request['inputs'][name]
        p = Path(paths[name])
        check(p.is_absolute() and not p.is_symlink() and p.resolve().is_relative_to(runner),
              'Original numerical inputs remain temporary: '+name)
        found = receipt(p)
        check(found['bytes'] == item['bytes'] and found['sha256'] == item['sha256'],
              'Original mathematical input differs: '+name)
        input_hashes[name], actual_paths[name] = item['sha256'], str(p.resolve())
    item = request['parameter_recipe']
    recipe_raw = owned_relative(repository, item['file']).read_bytes()
    check(len(recipe_raw) <= 16384 and len(recipe_raw) == item['bytes']
          and digest(recipe_raw) == item['sha256'],
          'Bind the complete declared actual-origin short recipe')
    recipe = decode(recipe_raw)
    check(set(recipe) == {'schema', 'origin', 'literal_parameters', 'algorithm_state', 'input_sha256', 'family'}
          and recipe['schema'] == RECIPE_SCHEMA and recipe['input_sha256'] == input_hashes
          and recipe['family'] == item['family'] and recipe['origin'] == item['origin']
          and isinstance(recipe['algorithm_state'], dict)
          and set(recipe['algorithm_state']) == {'relative_trust_radius'}
          and recipe['algorithm_state'] == item['algorithm_state'],
          'Preserve the exact frozen own-nine recipe input contract')
    check(same_parameters(recipe['literal_parameters'], request['diagnostic']['parameters']),
          'Use all nine declared actual-origin binary64 parameter words')
    check(same_radius(recipe['algorithm_state']['relative_trust_radius'],
                      request['diagnostic']['initial_relative_radius']),
          'The first CLI radius is the exact declared actual-origin binary64 word')
    origin = recipe['origin']
    expected_keys = {'repository', 'run_id', 'source_commit', 'producer_file',
        'producer_sha256', 'producer_schema', 'status_bytes', 'status_sha256',
        'log_summary_bytes', 'log_summary_sha256', 'parameter_field', 'radius_field'}
    check(set(origin) == expected_keys and origin['repository'] == REPOSITORY
          and isinstance(origin['run_id'], str) and origin['run_id'].isdigit()
          and hex_digest(origin['source_commit'], 40)
          and origin['parameter_field'] == 'final.parameters'
          and origin['radius_field'] == 'final_relative_trust_radius',
          'The initial recipe must name actual saved parameter/radius fields, never a future result')
    if origin['producer_file'] == SAME_TRACE_SCIENCE:
        check(origin['producer_sha256'] == SAME_TRACE_SCIENCE_SHA
              and origin['producer_schema'] == SAME_TRACE_SCIENCE_SCHEMA
              and request['source_closure']['origin_producer'] == same_trace_closure,
              'The actual138 origin keeps its complete twenty-nine-source definition')
    elif origin['producer_file'] == SCIENCE:
        check(origin['producer_sha256'] == SCIENCE_SHA
              and origin['producer_schema'] == SCIENCE_SCHEMA
              and request['source_closure']['origin_producer'] == closure,
              'An own complete-directional origin keeps its thirty-one-source definition')
    else:
        raise ValueError('The origin must be the actual same-trace parent or this independent directional producer')
    for stem in ('status', 'log_summary'):
        check(type(origin[stem+'_bytes']) is int and origin[stem+'_bytes'] > 0
              and hex_digest(origin[stem+'_sha256']), 'Retain actual origin bytes and digest')
    check(os.environ.get('GITHUB_RUN_ID', '').isdigit()
          and hex_digest(os.environ.get('GITHUB_SHA'), 40),
          'Use this actual Actions run and source')
    check(not args.out.is_symlink() and args.out.resolve().is_relative_to(runner)
          and not args.out.exists(), 'Use a fresh request-owned temporary orchestration directory')
    return request, repository, computations, recipe_raw, recipe, actual_paths

def science_argv(actual_paths, computations, recipe_path, recipe_sha, output, initial_radius):
    argv = [sys.executable, '-u', str(computations/SCIENCE)]
    for name in ('accepted', 'prepared', 'tail_anchor', 'tail_config'):
        argv += ['--'+name.replace('_', '-'), actual_paths[name]]
    argv += ['--parameter-recipe', str(recipe_path), '--parameter-recipe-sha256', recipe_sha]
    for name, value in OPTIONS.items():
        argv += ['--'+name.replace('_', '-'), str(value)]
    argv += ['--initial-relative-radius', repr(radius(initial_radius)), '--out', str(output)]
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

    def run(self, argv, cwd, environment, stdout, stderr, *, tee_stdout=False):
        # No child timeout and no new session: original budgets and the rules
        # runner's process-group stop remain unchanged. Reader stdout is copied
        # byte for byte, including complete or partial original segments.
        with stdout.open('wb') as out_handle, stderr.open('wb') as err_handle:
            self.active = subprocess.Popen(argv, cwd=cwd, env=environment, shell=False,
                stdout=subprocess.PIPE if tee_stdout else out_handle, stderr=err_handle)
            try:
                if tee_stdout:
                    while True:
                        block = self.active.stdout.read1(65536)
                        if not block:
                            break
                        out_handle.write(block)
                        sys.stdout.buffer.write(block)
                        sys.stdout.buffer.flush()
                    self.active.stdout.close()
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
    label = 'VISIBLE_NINE_BATCH_'+str(number).zfill(3)+'_PRIMARY'
    print('BEGIN_'+label, flush=True)
    print(raw.decode('utf-8'), flush=True)
    print('END_'+label, flush=True)
    print(encode(dict(event='visible-nine-batch-original-primary-sha256', batch=number,
        bytes=len(raw), sha256=digest(raw), original_reader_file=READER,
        original_reader_sha256=READER_SHA, independent_complete_normal_reader_schema=True,
        hash_scope='UTF-8 original compact primary JSON string excluding separator LF',
        direction_segments_in_same_batch_reader_frame=True,
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
          and same_parameters(value['parameter_recipe']['literal_parameters'], incoming['literal_parameters'])
          and value['parameter_recipe']['algorithm_state'] == incoming['algorithm_state']
          and same_radius(value['initial_relative_trust_radius'],
                          incoming['algorithm_state']['relative_trust_radius']),
          'The actual child must consume this exact literal recipe and family')
    if 'initial' in value:
        check(same_parameters(value['initial']['parameters'], incoming['literal_parameters']),
              'The original fresh initial state must be at the supplied recipe parameters')
    if summary.get('original_status') is not None:
        check(summary['original_status'] == record['original_status'],
              'Reader summary must come from the complete original status just read')
    record['source_sha256'] = value['source_sha256']
    closure_raw = encode(value['consumed_source_sha256'])
    record['consumed_source_closure'] = dict(count=31, canonical_bytes=len(closure_raw),
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
          and summary['original_status'] == status_record['original_status'],
          'Bind the genuine original segmented reader to the complete current status')
    segmented = summary.get('segmented_readout', {})
    check(segmented.get('all_complete_groups_emitted_before_primary') is True
          and segmented.get('complete_original_trial_rows_retained') is True,
          'Do not continue after incomplete original scalar transport')
    if 'final' in summary:
        check(same_parameters(summary['final']['parameters'], status['final']['parameters']),
              'The inline original final parameters must match the fully read status')
    else:
        check(any(item.get('original_field') == 'final'
                  and item.get('group', {}).get('complete_original_value_retained') is True
                  for item in segmented.get('moved_primary_fields', [])),
              'A relocated final remains a complete named log group, not an omitted point')
    carried_radius = radius(status['final_relative_trust_radius'])
    fields = summary.get('original_fields')
    if isinstance(fields, dict):
        check(same_radius(fields['final_relative_trust_radius'], carried_radius),
              'The reader and complete original status retain the same actual final radius')
    else:
        check(any(item.get('original_field') == 'original_fields'
                  and item.get('group', {}).get('complete_original_value_retained') is True
                  for item in segmented.get('moved_primary_fields', [])),
              'Relocated original fields remain a complete named group, not omitted algorithm state')
    descriptor = status_record['original_status']
    return dict(schema=RECIPE_SCHEMA,
        origin=dict(repository=REPOSITORY, run_id=os.environ['GITHUB_RUN_ID'],
            source_commit=os.environ['GITHUB_SHA'], producer_file=SCIENCE,
            producer_sha256=SCIENCE_SHA, producer_schema=SCIENCE_SCHEMA,
            status_bytes=descriptor['bytes'], status_sha256=descriptor['sha256'],
            log_summary_bytes=len(summary_raw), log_summary_sha256=digest(summary_raw),
            parameter_field='final.parameters', radius_field='final_relative_trust_radius'),
        literal_parameters=parameters(status['final']['parameters']),
        algorithm_state=dict(relative_trust_radius=carried_radius),
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
    request, repository, computations, recipe_raw, incoming, actual_paths = bind(args)
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
        request_sha256=args.request_sha256, request_number=request['request_number'],
        run_id=os.environ['GITHUB_RUN_ID'], source_commit=os.environ['GITHUB_SHA'],
        scientific_entry=SCIENCE, scientific_source_sha256=SCIENCE_SHA,
        family_source_sha256=FAMILY_SHA, original_reader_source_sha256=READER_SHA,
        source_closure=request['source_closure']['current_producer'],
        input_sha256=incoming['input_sha256'], batch_chain=CHAIN, original_child_options=OPTIONS,
        initial_actual_own_nine_origin=incoming['origin'],
        initial_parameters=parameters(incoming['literal_parameters']),
        initial_actual_relative_trust_radius=radius(incoming['algorithm_state']['relative_trust_radius']),
        first_origin_status_payload_read_in_this_run=False,
        first_origin_literals_bound_by_explicit_request_not_a_future_run_constant=True,
        subsequent_recipe_status_and_primary_payloads_fully_read_in_this_run=True,
        next_child_receipt_claims_only_what_frozen_child_itself_reads=True,
        independent_processes_with_fresh_initial_J_and_all_final_checks=True,
        radius_reset_is_explicit_algorithmic_initialization_not_saved_trust_continuation=False,
        actual_saved_final_radius_carried_without_clamping_or_repair=True,
        only_parameters_and_actual_final_radius_carried=True,
        independent_same_trace_selector_source_sha256=SELECTOR_SHA,
        independent_complete_directional_response_source_sha256=RESPONSE_HELPER_SHA,
        old_same_trace_producer_wrapper_and_reader_not_executed=True,
        outer_pilot_J_and_direct_action_not_relabelled_as_same=True,
        baseline_carried_radius_producer_and_wrapper_not_executed=True,
        complete_normal_scalar_trace_retained_by_independent_reader=True,
        old_merit_J_states_FD_domain_or_circle_reused=False,
        cross_batch_merit_arithmetic_performed=False,
        scientific_acceptance_rules_modified=False, no_new_mathematical_acceptance_gate=True,
        native_BVP_or_surface_completion_claimed=False,
        raw_artifact_Release_or_Git_upload=False,
        each_original_segmented_reader_stdout_copied_byte_for_byte_in_batch_frame=True,
        original_primaries_printed_separately=True, per_original_primary_limit_bytes=LIMIT,
        single_original_primary_kept_separate_from_complete_direction_groups=True,
        baseline_eight_batch_source_identity_only=dict(file=BASELINE_ENTRY, sha256=BASELINE_ENTRY_SHA),
        baseline_eight_batch_wrapper_executed=False,
        baseline_reset32_source_identity_only=dict(file=RESET_WRAPPER, sha256=RESET_WRAPPER_SHA),
        baseline_reset32_wrapper_executed=False, baseline_original_nine_main_executed=False,
        frozen_counterfactual_zero_eta_readback_remains_separate_from_actual_parameters=True,
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
            argv = science_argv(actual_paths, computations, current_recipe, digest(recipe_raw), science,
                                incoming['algorithm_state']['relative_trust_radius'])
            record = dict(batch=number, phase='original_child_running',
                incoming_recipe=receipt(current_recipe, output), incoming_recipe_origin=incoming['origin'],
                initial_parameters=parameters(incoming['literal_parameters']),
                initial_relative_radius=radius(incoming['algorithm_state']['relative_trust_radius']),
                saved_final_radius_not_carried=False,
                scientific_source_sha256=SCIENCE_SHA, original_child_argv=argv,
                raw_cleanup_completed=False)
            chain['batches'].append(record)
            chain['phase'] = 'running'
            atomic_json(ledger, chain)
            print(encode(dict(event='visible-nine-batch-begin', batch=number,
                run_id=os.environ['GITHUB_RUN_ID'], source_commit=os.environ['GITHUB_SHA'],
                incoming_recipe=record['incoming_recipe'], origin=incoming['origin'],
                parameters=record['initial_parameters'], initial_relative_radius=record['initial_relative_radius'],
                scientific_entry=SCIENCE, scientific_source_sha256=SCIENCE_SHA,
                original_acceptance_rules_unchanged=True)).decode(), flush=True)
            began = time.monotonic()
            child_code = processes.run(argv, repository, clean_child_environment(),
                                       batch/'science.stdout', batch/'science.stderr')
            record.update(phase='original_child_exited', child_returncode=child_code,
                elapsed_seconds=time.monotonic()-began,
                scientific_stdout=receipt(batch/'science.stdout', output),
                scientific_stderr=receipt(batch/'science.stderr', output),
                scientific_stdout_stderr_contents_not_uploaded=True)
            atomic_json(ledger, chain)
            reader_output = batch/'reader-github-output.txt'
            reader_output.touch(exist_ok=False)
            environment = clean_child_environment()
            environment['GITHUB_OUTPUT'] = str(reader_output)
            outcome = 'cancelled' if processes.signal_number is not None else ('success' if child_code == 0 else 'failure')
            reader_argv = [sys.executable, str(computations/READER), '--directory', str(science),
                           '--rules-directory', str(args.rules_directory), '--compute-outcome', outcome]
            label = 'VISIBLE_NINE_BATCH_'+str(number).zfill(3)+'_ORIGINAL_READER_STDOUT'
            print('BEGIN_'+label, flush=True)
            try:
                reader_code = processes.run(reader_argv, repository, environment,
                    batch/'reader.stdout', batch/'reader.stderr', tee_stdout=True)
            finally:
                print('END_'+label, flush=True)
            record.update(reader_returncode=reader_code,
                original_reader_stdout=receipt(batch/'reader.stdout', output),
                original_reader_stderr=receipt(batch/'reader.stderr', output),
                original_reader_github_output=receipt(reader_output, output),
                original_reader_stdout_frame=dict(begin='BEGIN_'+label, end='END_'+label),
                all_reader_stdout_bytes_copied_to_original_compute_log=True)
            print(encode(dict(event='visible-nine-batch-reader-stdout-sha256', batch=number,
                **record['original_reader_stdout'], frame=record['original_reader_stdout_frame'],
                reader_returncode=reader_code,
                copied_bytes_are_original_reader_output_not_reencoded_segments=True)).decode(), flush=True)
            summary_raw, summary = None, {}
            try:
                summary_raw, summary = parse_reader_output(reader_output)
                emit_original_summary(number, summary_raw)
                record['original_summary'] = dict(bytes=len(summary_raw), sha256=digest(summary_raw),
                    schema=summary.get('schema'), printed_complete_original_primary=True)
                segmented = summary.get('segmented_readout', {})
                record['original_segmented_view'] = dict(
                    original_view=segmented.get('original_view'),
                    original_outer_direction_count=segmented.get('original_outer_direction_count'),
                    emitted_group_count=segmented.get('emitted_group_count'),
                    emitted_segment_count=segmented.get('emitted_segment_count'),
                    all_complete_groups_emitted_before_primary=segmented.get('all_complete_groups_emitted_before_primary'),
                    complete_original_trial_rows_retained=segmented.get('complete_original_trial_rows_retained'),
                    all_original_normal_scalar_records_retained=segmented.get('all_original_normal_scalar_records_retained'),
                    all_selector_samples_and_original_working_returns_retained=segmented.get('all_selector_samples_and_original_working_returns_retained'),
                    moved_primary_fields=[item.get('original_field') for item in segmented.get('moved_primary_fields', [])],
                    original_group_index_retained_in_this_batch_primary=True)
            except Exception as error:
                record['scalar_transport_error'] = repr(error)
            status, status_record = read_status(science, request, incoming, summary)
            record['original_child'] = status_record
            if reader_code != 0 or summary_raw is None or 'scalar_transport_error' in record:
                record['phase'] = 'original_scalar_transport_incomplete'
                chain['stop_reason'] = 'original_reader_process_or_protocol_failed'
                chain['original_child_scientific_outcome_not_relabelled'] = True
                code = 70
                atomic_json(ledger, chain)
                break
            record['phase'] = ('original_readback_completed' if summary.get('schema') == READER_SCHEMA
                               else 'original_scalar_readback_incomplete')
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
                record['restart_origin_from_fully_read_actual_status_and_original_primary'] = True
                chain['last_restart_recipe'] = dict(**record['restart_recipe'],
                    origin=next_recipe['origin'], literal_parameters=next_recipe['literal_parameters'],
                    algorithm_state=next_recipe['algorithm_state'])
                chain['last_fully_read_parameters'] = next_recipe['literal_parameters']
                chain['last_fully_read_relative_trust_radius'] = next_recipe['algorithm_state']['relative_trust_radius']
                print(encode(dict(event='visible-nine-batch-restart-recipe', batch=number,
                    receipt=record['restart_recipe'], recipe=next_recipe,
                    original_complete_status_and_primary_read_before_recipe=True,
                    recipe_is_not_an_accepted_nonzero_field_or_native_anchor=True)).decode(), flush=True)
            record['original_stop_decision'] = stop
            atomic_json(ledger, chain)
            # Both raw status and original scalar output have been consumed.
            # Only a short own-schema parameter-and-radius recipe can reach the next child.
            shutil.rmtree(batch)
            record['raw_cleanup_completed'] = True
            record['raw_cleanup_after_original_readback_and_next_recipe'] = True
            atomic_json(ledger, chain)
            print(encode(dict(event='visible-nine-batch-complete', batch=number,
                status=status_record.get('original_status'), primary=record.get('original_summary'),
                original_stop_decision=stop, next_recipe=record.get('restart_recipe'),
                raw_cleanup_completed=True, scientific_completion_not_inferred_from_cleanup=True)).decode(), flush=True)
            if stop is not None:
                chain['stop_reason'] = stop
                break
            if number == CHAIN['max_batches']:
                chain['stop_reason'] = 'explicit_independent_batch_count_completed'
                break
            check(next_recipe is not None, 'Do not continue without a genuine complete next recipe')
            recipe_raw, incoming, current_recipe = next_bytes, next_recipe, next_path
        else:
            chain['stop_reason'] = 'explicit_independent_batch_count_completed'
    except Exception as error:
        chain['wrapper_exception'] = repr(error)
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
        print(encode(dict(event='visible-nine-chain-metadata-prepared', **final,
            stop_reason=chain['stop_reason'], exit_code=code,
            this_event_is_not_a_scientific_success_claim=True)).decode(), flush=True)
    return code


def compact_chain_index(chain):
    """Only literal copied scalars, parameters and SHA pointers; no model action."""
    keep = ('schema', 'phase', 'source_sha256', 'request_sha256', 'request_number',
        'run_id', 'source_commit', 'scientific_entry', 'scientific_source_sha256',
        'family_source_sha256', 'original_reader_source_sha256', 'input_sha256',
        'batch_chain', 'original_child_options', 'initial_actual_own_nine_origin',
        'initial_parameters', 'last_fully_read_parameters', 'last_restart_recipe',
        'initial_actual_relative_trust_radius', 'last_fully_read_relative_trust_radius',
        'stop_reason', 'wrapper_exception', 'exit_code', 'elapsed_seconds',
        'interrupted_signal', 'batches_started', 'completed_original_readbacks',
        'resource_limited_partial_chain', 'baseline_eight_batch_source_identity_only',
        'baseline_eight_batch_wrapper_executed', 'baseline_reset32_source_identity_only',
        'baseline_reset32_wrapper_executed', 'baseline_original_nine_main_executed',
        'actual_saved_final_radius_carried_without_clamping_or_repair',
        'only_parameters_and_actual_final_radius_carried',
        'independent_same_trace_selector_source_sha256',
        'independent_complete_directional_response_source_sha256',
        'old_same_trace_producer_wrapper_and_reader_not_executed',
        'outer_pilot_J_and_direct_action_not_relabelled_as_same',
        'baseline_carried_radius_producer_and_wrapper_not_executed',
        'complete_normal_scalar_trace_retained_by_independent_reader')
    result = {key:chain[key] for key in keep if key in chain}
    closure_raw = encode(chain.get('source_closure', {}))
    result['original_scientific_source_closure'] = dict(count=len(chain.get('source_closure', {})),
        canonical_json_bytes=len(closure_raw), canonical_json_sha256=digest(closure_raw))
    columns = ['batch', 'phase', 'child_returncode', 'reader_returncode',
        'original_status', 'original_primary', 'original_scalar_view',
        'reader_stdout', 'reader_stdout_frame', 'emitted_groups', 'emitted_segments',
        'original_phase', 'original_search_stop_reason', 'wrapper_stop_decision',
        'directions', 'accepted', 'rejected', 'initial_merit', 'final_merit',
        'unit_flag', 'full112_flag', 'nonzero_flag', 'original_success',
        'initial_parameters', 'final_parameters', 'explicit_initial_radius',
        'original_final_radius', 'restart_recipe', 'raw_cleanup_completed',
        'scalar_transport_error', 'original_exception', 'original_trace']
    rows = []
    for batch in chain.get('batches', []):
        status = batch.get('original_child', {})
        view = batch.get('original_segmented_view', {})
        rows.append([batch.get('batch'), batch.get('phase'),
            batch.get('child_returncode'), batch.get('reader_returncode'),
            status.get('original_status'), batch.get('original_summary'),
            view.get('original_view'), batch.get('original_reader_stdout'),
            batch.get('original_reader_stdout_frame'), view.get('emitted_group_count'),
            view.get('emitted_segment_count'), status.get('phase'),
            status.get('search_stop_reason'), batch.get('original_stop_decision'),
            status.get('total_direction_attempts'), status.get('original_Armijo_accepted_point_count'),
            status.get('rejected_direction_count'), status.get('initial_original_three_equation_merit'),
            status.get('final_original_three_equation_merit'),
            status.get('original_unit_stopping_tolerance_met'),
            status.get('low_mode_candidate_has_small_full_recorded_right_residual'),
            status.get('full_nonlinear_nonzero_lambda_solution_computed'), status.get('success'),
            batch.get('initial_parameters'), status.get('final_parameters'),
            batch.get('initial_relative_radius'), status.get('final_relative_trust_radius'),
            batch.get('restart_recipe'), batch.get('raw_cleanup_completed'),
            batch.get('scalar_transport_error'), status.get('exception'), status.get('original_trace')])
    # The chain index always represents the complete declared plan.  Rows
    # after the last genuinely started child contain no invented scientific
    # values, parameters, receipts or cleanup result.
    started_rows = len(rows)
    unstarted = list(range(started_rows+1, CHAIN['max_batches']+1))
    for number in unstarted:
        row = [None] * len(columns)
        row[columns.index('batch')] = number
        row[columns.index('phase')] = 'not_started'
        rows.append(row)
    unfinished_started = [batch.get('batch') for batch in chain.get('batches', [])
                          if batch.get('phase') != 'original_readback_completed']
    complete_primary_batches = [batch.get('batch') for batch in chain.get('batches', [])
        if batch.get('original_summary', {}).get('printed_complete_original_primary') is True]
    complete_segment_batches = [batch.get('batch') for batch in chain.get('batches', [])
        if batch.get('all_reader_stdout_bytes_copied_to_original_compute_log') is True
        and batch.get('original_segmented_view', {}).get('all_complete_groups_emitted_before_primary') is True
        and batch.get('original_segmented_view', {}).get('complete_original_trial_rows_retained') is True]
    result['batch_index_columns'], result['batch_index_rows'] = columns, rows
    result['batch_plan_coverage'] = dict(
        declared_rows=CHAIN['max_batches'], represented_rows=len(rows),
        actually_started_rows=started_rows, not_started_batch_indices=unstarted,
        unfinished_started_batch_indices=unfinished_started,
        all_declared_batch_rows_retained=len(rows) == CHAIN['max_batches'],
        unstarted_nulls_mean_not_evaluated_not_scientific_failure=True,
        unfinished_actual_row_values_not_filled_from_predecessors=True,
        all_started_batches_have_original_complete_readback=not unfinished_started,
        complete_original_primary_batch_indices=complete_primary_batches,
        complete_original_segment_batch_indices=complete_segment_batches,
        no_row_truncation_or_parameter_prediction=True)
    result['readback_scope'] = dict(
        complete_original_primaries_and_direction_segments_in_compute_stdout=(
            len(complete_primary_batches) == started_rows == len(complete_segment_batches)),
        each_started_batch_has_outer_reader_frame_and_separate_primary_frame=(
            len(complete_primary_batches) == started_rows and all(
                batch.get('original_reader_stdout_frame') for batch in chain.get('batches', []))),
        primary_and_segments_not_concatenated_into_job_output=True,
        all_started_batch_original_trial_rows_remain_in_frozen_reader_groups=(
            len(complete_segment_batches) == started_rows),
        all_started_batch_complete_normal_records_in_original_log_groups=(
            len(complete_segment_batches) == started_rows and all(
                batch.get('original_segmented_view', {}).get('all_original_normal_scalar_records_retained') is True
                for batch in chain.get('batches', []))),
        completeness_flags_cover_only_started_batches_not_unstarted_suffix=True,
        this_index_recomputes_no_merit_norm_response_or_scientific_flag=True,
        native_BVP_completion_not_claimed=True,
        parent_raw_payloads_not_retained_in_Git_Release_or_new_artifact=True,
        original_child_science_failure_not_relabelled_as_readout_failure=True)
    return result


def report(args):
    """Always-step compact index; no scientific import or child launch."""
    source = args.out/'chain-metadata.json'
    if source.is_file():
        raw = source.read_bytes()
        chain = decode(raw)
        check(chain.get('schema') == SCHEMA, 'Use this actual chain metadata schema')
        result = compact_chain_index(chain)
        result['chain_metadata_file'] = dict(file=source.name, bytes=len(raw), sha256=digest(raw))
        result['compute_step_outcome'] = args.compute_outcome
        if chain.get('phase') != 'finished':
            result['orchestration_interrupted_before_final_receipt'] = True
            result['scientific_completion_not_claimed'] = True
    else:
        result = dict(schema='nine-control-complete-directional-response-single-batch-chain-output-unavailable-v1',
            compute_step_outcome=args.compute_outcome, run_id=os.environ.get('GITHUB_RUN_ID'),
            source_commit=os.environ.get('GITHUB_SHA'), scientific_completion_not_claimed=True)
    result['actual_rule_sync_index'] = []
    if args.rules_directory.is_dir():
        paths = sorted(args.rules_directory.glob('sync-*-completed.json'))
        if (args.rules_directory/'runner-result.json').is_file():
            paths.append(args.rules_directory/'runner-result.json')
        for path in paths:
            raw = path.read_bytes()
            value = decode(raw)
            small = {}
            if isinstance(value, dict):
                for key, item in value.items():
                    if item is None or type(item) in (bool, int, float, str):
                        if isinstance(item, str) and len(item.encode('utf-8')) > 4000:
                            encoded = item.encode('utf-8')
                            small[key] = dict(original_text_bytes=len(encoded),
                                original_text_sha256=digest(encoded),
                                large_rule_text_not_duplicated_in_chain_job_output=True)
                        else:
                            small[key] = item
            result['actual_rule_sync_index'].append(dict(receipt=receipt(path),
                original_scalar_fields=small, full_rule_record_consumed_before_workflow_cleanup=True))
    raw = encode(result)
    # These are byte counts of this actual index, not a simulated future chain.
    # Emit them before the hard-bound branch so an honest overflow remains
    # diagnosable without omitting rows or rerunning a scientific child.
    section_bytes = {key: len(encode(value)) for key, value in result.items()}
    row_bytes = [len(encode(row)) for row in result.get('batch_index_rows', [])]
    measurement = dict(event='visible-nine-complete-directional-response-single-batch-chain-index-byte-counts',
        run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
        original_index_bytes=len(raw), original_index_sha256=digest(raw),
        hard_limit_bytes=LIMIT, section_UTF8_byte_counts=section_bytes,
        batch_row_UTF8_byte_counts=row_bytes,
        batch_plan_coverage=result.get('batch_plan_coverage'),
        counts_are_original_metadata_bytes_not_scientific_recomputation=True)
    print(encode(measurement).decode(), flush=True)
    overflow = len(raw) > LIMIT
    if overflow:
        # Preserve explicit failure plus actual result pointers. Never silently
        # call a truncated chain complete or retry any scientific child.
        original_index = dict(bytes=len(raw), sha256=digest(raw))
        reduced = dict(schema='nine-control-complete-directional-response-single-batch-chain-index-over-budget-v1',
            compute_step_outcome=args.compute_outcome, run_id=os.environ.get('GITHUB_RUN_ID'),
            source_commit=os.environ.get('GITHUB_SHA'),
            original_index_identity=original_index,
            chain_metadata_file=result.get('chain_metadata_file'),
            stop_reason=result.get('stop_reason'),
            batches_started=result.get('batches_started'),
            completed_original_readbacks=result.get('completed_original_readbacks'),
            original_last_restart_recipe=result.get('last_restart_recipe'),
            batch_plan_coverage=result.get('batch_plan_coverage'),
            section_UTF8_byte_counts=section_bytes,
            batch_row_UTF8_byte_counts=row_bytes,
            emitted_original_reader_stdout_and_primaries_remain_in_compute_log=True,
            full_index_was_not_truncated_or_relabelled_as_complete=True,
            complete_failed_index_not_claimed_recoverable_from_this_small_notice=True,
            compact_chain_transport_complete=False, scientific_completion_not_claimed=True)
        raw = encode(reduced)
        check(len(raw) <= LIMIT, 'Even the honest transport failure index must remain bounded')
    delimiter = 'VISIBLE_NINE_CHAIN_'+uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as handle:
        handle.write('chain_summary<<'+delimiter+'\n'+raw.decode('utf-8')+'\n'+delimiter+'\n')
        handle.write('chain_summary_bytes='+str(len(raw))+'\n')
        handle.write('chain_summary_sha256='+digest(raw)+'\n')
    print(encode(dict(event='visible-nine-chain-output-prepared', bytes=len(raw), sha256=digest(raw),
        hash_scope='UTF-8 compact chain JSON excluding separator LF',
        independent_original_batch_primaries_and_all_segments_are_in_compute_stdout=True,
        compact_chain_transport_complete=not overflow,
        mathematical_acceptance_not_inferred_from_process_success=True)).decode(), flush=True)
    return 70 if overflow else 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--request', type=Path)
    parser.add_argument('--request-sha256')
    parser.add_argument('--repository-directory', type=Path)
    parser.add_argument('--original-input-paths', type=Path)
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
          and args.repository_directory is not None and args.original_input_paths is not None,
          'Supply the current request, repository and explicit temporary original-input map')
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
