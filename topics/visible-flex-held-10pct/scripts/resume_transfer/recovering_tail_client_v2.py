"""One external initializer and one original-worker retry per failed request.

The original client and worker files remain unchanged.  The helper never
solves the DN problem.  A restarted original worker loads the unaccepted
candidate through its existing initialCheckpoint protocol and alone owns
the successful response, Jacobian, audit, cache and subsequent warm state.
"""
import copy
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import subprocess
import time

import numpy as np


INITIALIZER_KEYS = {'initialCheckpoint', 'designInitialCheckpoint',
                    'secantCheckpoint', 'traceFile'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_equal(left, right):
    if type(left) is not type(right):
        return False
    if isinstance(left, float):
        return struct.pack('>d', left) == struct.pack('>d', right)
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(exact_equal(left[k], right[k]) for k in left)
    if isinstance(left, (tuple, list)):
        return len(left) == len(right) and all(exact_equal(a, b) for a, b in zip(left, right))
    return left == right


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def read_gzip(path):
    return json.loads(gzip.decompress(Path(path).read_bytes()))


def write_new_json(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def physical_solver_config(config):
    return {k: v for k, v in config.items() if k not in INITIALIZER_KEYS}


def validate_parameter_io_mapping(before, after, old_config, new_config):
    """Check embedded IO metadata against both configs; lock every other key."""
    left, right = copy.deepcopy(before), copy.deepcopy(after)
    transition = {}
    for key in sorted(INITIALIZER_KEYS):
        for parameters, config, label in ((before, old_config, 'before'),
                                          (after, new_config, 'after')):
            if ((key in parameters) != (key in config) or
                    (key in config and not exact_equal(parameters[key], config[key]))):
                raise ValueError('Embedded parameter IO does not match its '+label+' configuration: '+key)
        if ((key in before) != (key in after) or
                (key in before and not exact_equal(before[key], after[key]))):
            transition[key] = dict(before_present=key in before, before=before.get(key),
                                   after_present=key in after, after=after.get(key))
        left.pop(key, None);right.pop(key, None)
    if not exact_equal(left, right):
        differences = [key for key in set(left)|set(right)
                       if key not in left or key not in right or not exact_equal(left[key], right[key])]
        raise ValueError('Physical or numerical ready parameters changed: '+str(sorted(differences)))
    return transition


def check_original_reload_boundary(candidate_path, height, radius):
    """Use the original worker's JS arithmetic, without constructing a DN."""
    program = r'''
const fs=require('node:fs'),zlib=require('node:zlib');
const d=JSON.parse(fs.readFileSync(0,'utf8'));
const cp=JSON.parse(zlib.gunzipSync(fs.readFileSync(process.argv[1]))).checkpoint;
const same=(x,y)=>x.length===y.length&&x.every((v,j)=>Object.is(v,y[j]));
if(!same(d.height,cp.cutHeight)||!Object.is(d.height[0]/cp.cutHeight[0],1))
  throw Error('Original reload ratio or complete height changed');
const delta=d.height.map((v,j)=>v/d.radius**4-cp.states[0][j]);
if(!delta.every(v=>Object.is(v,0)))throw Error('Nonzero original boundary correction');
if(cp.states.some(row=>row.some(v=>!Number.isFinite(v)||Object.is(v,-0))))
  throw Error('Candidate has nonfinite or signed-zero values changed by reload');
console.log(JSON.stringify({cut_radius:d.radius,ratio:1,zero_boundary_correction:true,
  finite_states_without_negative_zero:true,original_solver_invoked:false}));
'''
    completed = subprocess.run(['node', '-e', program, str(candidate_path)],
        input=json.dumps(dict(height=height, radius=radius), allow_nan=False),
        text=True, capture_output=True, check=True)
    return json.loads(completed.stdout)


def make_recovering_class(Base, original_topic, candidate_helper):
    original_topic, candidate_helper = Path(original_topic).resolve(), Path(candidate_helper).resolve()

    class RecoveringWeightedTailPort(Base):
        def __init__(self, config, source_root, record_prefix, node_heap=1536):
            self._original_topic = original_topic
            self._candidate_helper = candidate_helper
            self._helper_digest = sha(candidate_helper)
            self._adapter_digest = sha(__file__)
            self._source_root = Path(source_root).resolve()
            if self._source_root != (original_topic/'repro/source-root').resolve():
                raise ValueError('Candidate and original worker must use the same source root')
            self._node_heap = node_heap
            self._current_config = json.loads(Path(config).read_text())
            if (self._current_config.get('sharedEngines') or
                    self._current_config.get('spacing') != 3 or
                    self._current_config.get('solveTolerance') != 2e-9):
                raise ValueError('This recovery adapter binds the original nonshared m3 2e-9 worker')
            self._fixed_configuration = physical_solver_config(self._current_config)
            helper = os.environ.get('VISIBLE_FLEX_SPARSE_LINEAR_HELPER')
            if not helper or not Path(helper).is_file():
                raise ValueError('The original sparse helper must be explicitly available')
            self._sparse_helper = Path(helper).resolve()
            self._sparse_digest = sha(self._sparse_helper)
            self._runtime_sources = {str(file.resolve()): sha(file) for file in
                sorted(self._source_root.rglob('*'))
                if file.is_file() and file.suffix in ('.py', '.mjs', '.js')}
            if not self._runtime_sources:
                raise ValueError('Original runtime source manifest is empty')
            self._generation = 0
            self._generation_base_call = 0
            self._last_accepted_record = None
            self._events = Path(record_prefix).with_name(Path(record_prefix).name+'-recovery-events.jsonl')
            if self._events.exists():
                raise FileExistsError('Recovery event path already used')
            Base.__init__(self, config, source_root, record_prefix, node_heap=node_heap)
            self._original_ready = copy.deepcopy(self.ready)
            self._original_sources = dict(self.sources)
            self._event('recovery_adapter_ready', configuration_sha256=sha(config),
                        fixed_configuration_sha256=payload_sha(self._fixed_configuration),
                        adapter_sha256=self._adapter_digest, candidate_helper_sha256=self._helper_digest,
                        sparse_helper=dict(path=str(self._sparse_helper), sha256=self._sparse_digest),
                        original_sources=self._original_sources,
                        runtime_source_sha256=self._runtime_sources)

        def _event(self, event, **values):
            row = dict(event=event, utc_seconds=time.time(), generation=self._generation,
                       logical_calls=self.calls, **values)
            with self._events.open('a') as stream:
                stream.write(json.dumps(row, separators=(',', ':'), allow_nan=False)+'\n')
            print(json.dumps(row, allow_nan=False), flush=True)

        def _record_file(self):
            return self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')

        def _check_live_identity(self):
            current = json.loads(self.config.read_text())
            live_helper = os.environ.get('VISIBLE_FLEX_SPARSE_LINEAR_HELPER')
            if not live_helper or Path(live_helper).resolve() != self._sparse_helper:
                raise ValueError('The original sparse-helper environment changed')
            if not exact_equal(current, self._current_config):
                raise ValueError('The active original-worker configuration changed during execution')
            if not exact_equal(physical_solver_config(current), self._fixed_configuration):
                raise ValueError('A physical, discretization or solver parameter changed')
            if sha(self._candidate_helper) != self._helper_digest or sha(self._sparse_helper) != self._sparse_digest:
                raise ValueError('A frozen recovery or original sparse helper changed')
            if sha(__file__) != self._adapter_digest:
                raise ValueError('The owned recovery adapter changed during execution')
            for name, digest in self._original_sources.items():
                if sha(self._original_topic/'scripts'/name) != digest:
                    raise ValueError('An original client/worker source changed: '+name)
            for file, digest in self._runtime_sources.items():
                if sha(file) != digest:
                    raise ValueError('An original runtime source changed: '+file)

        def _native_solve(self, height, jacobian, audit):
            before = self.calls
            response = Base.solve(self, height, jacobian=jacobian, audit=audit)
            if self.calls != before:
                path = self._record_file()
                saved = read_gzip(path)
                if not exact_equal(saved['request']['height'], height.tolist()):
                    raise ValueError('The original worker recorded a different physical request')
                if not exact_equal(saved['response'], response):
                    raise ValueError('Returned response differs from the original recorded response')
                if (response.get('converged') is not True or
                        not math.isfinite(response.get('residual', math.inf)) or
                        not response['residual'] < self._current_config['solveTolerance']):
                    raise ValueError('The original response did not pass its original stopping test')
                self._last_accepted_record = path
                self._event('original_worker_accepted', record=str(path), record_sha256=sha(path),
                            worker_call=self.calls-self._generation_base_call,
                            request_sha256=payload_sha(saved['request']), residual=response['residual'],
                            jacobian=jacobian, audit=audit)
            return response

        def _restart_original_worker(self, candidate_path, candidate, summary):
            self._check_live_identity()
            previous_prefix, previous_calls = self.record_prefix, self.calls
            previous_ready = copy.deepcopy(self.ready)
            previous_configuration = copy.deepcopy(self._current_config)
            cp = candidate['checkpoint']
            if not exact_equal(cp['parameters'], self.ready['parameters']):
                raise ValueError('Candidate parameters differ from the original ready parameters')
            if not exact_equal(candidate['config'], self._current_config):
                raise ValueError('Candidate changed the original failed-request configuration')
            if summary['zero_original_worker_boundary_correction'] is not True:
                raise ValueError('A worker reload would change the left boundary state')
            if summary['first_height_ratio_on_reload'] != 1:
                raise ValueError('Reload would not use the identical physical height')
            reload_check = check_original_reload_boundary(
                candidate_path, cp['cutHeight'], self.cut['radius'])
            next_generation = self._generation+1
            config = copy.deepcopy(self._current_config)
            for key in ('designInitialCheckpoint', 'secantCheckpoint'):
                config.pop(key, None)
            config['initialCheckpoint'] = str(candidate_path.resolve())
            config['traceFile'] = str(previous_prefix.with_name(
                previous_prefix.name+f'-worker-g{next_generation:04d}.jsonl'))
            if not exact_equal(physical_solver_config(config), self._fixed_configuration):
                raise AssertionError('Only initializer and trace paths may change')
            config_path = previous_prefix.with_name(previous_prefix.name+f'-worker-g{next_generation:04d}-config.json')
            bootstrap = previous_prefix.with_name(previous_prefix.name+f'-bootstrap-g{next_generation:04d}')
            write_new_json(config_path, config)
            Base.close(self)
            # The original constructor rejects an already used record prefix.
            # No request is sent with bootstrap. Restore the logical record
            # stream before invoking the original solve method again.
            Base.__init__(self, config_path, self._source_root, bootstrap, node_heap=self._node_heap)
            self.record_prefix, self.calls = previous_prefix, previous_calls
            self._generation = next_generation
            self._generation_base_call = previous_calls
            self._current_config = config
            self._last_accepted_record = None
            ready_metadata_transition = validate_parameter_io_mapping(
                previous_ready['parameters'], self.ready['parameters'], previous_configuration, config)
            previous_ready_body = {k:v for k,v in previous_ready.items() if k != 'parameters'}
            ready_body = {k:v for k,v in self.ready.items() if k != 'parameters'}
            if not exact_equal(ready_body, previous_ready_body) or self.sources != self._original_sources:
                Base.close(self)
                raise ValueError('Restarted original worker has different ready data or sources')
            if self.cache_key is not None or self.cache_value is not None:
                raise AssertionError('The original constructor did not clear the cache')
            if reload_check['cut_radius'] != self.cut['radius']:
                Base.close(self)
                raise ValueError('Candidate target used a different cut radius')
            self._event('original_worker_restarted', candidate=str(candidate_path),
                        candidate_sha256=sha(candidate_path), config=str(config_path),
                        config_sha256=sha(config_path),
                        prior_logical_calls=previous_calls, bootstrap_prefix_unused=str(bootstrap),
                        exact_non_io_ready_and_sources_unchanged=True,
                        ready_parameter_metadata_transition=ready_metadata_transition,
                        reload_arithmetic=reload_check)

        def solve(self, height, jacobian=True, audit=False):
            h = np.asarray(height, float).copy()
            self._check_live_identity()
            try:
                return self._native_solve(h, bool(jacobian), bool(audit))
            except FloatingPointError as original_error:
                failed_file = self._record_file()
                failed = read_gzip(failed_file)
                cp = failed['response'].get('checkpoint')
                if (not failed['response'].get('failed') or not cp or
                        not failed['response'].get('lastIteration') or
                        not exact_equal(failed['request']['height'], h.tolist()) or
                        not exact_equal(cp['cutHeight'], h.tolist()) or
                        not exact_equal(failed['config'], self._current_config)):
                    raise
                failed_call = self.calls
                candidate_path = self.record_prefix.with_name(
                    self.record_prefix.name+f'-candidate-for-{failed_call:04d}.json.gz')
                summary_path = self.record_prefix.with_name(
                    self.record_prefix.name+f'-candidate-for-{failed_call:04d}-summary.json')
                command = ['node', str(self._candidate_helper), str(self._original_topic),
                           str(failed_file), str(candidate_path), str(summary_path)]
                self._event('one_external_candidate_started', failed_record=str(failed_file),
                            failed_sha256=sha(failed_file), request_sha256=payload_sha(failed['request']),
                            command=command, maximum_external_attempts=1, maximum_original_retries=1)
                completed = subprocess.run(command, check=False)
                if completed.returncode != 0:
                    self._event('external_candidate_failed', returncode=completed.returncode)
                    raise original_error
                summary = json.loads(summary_path.read_text())
                candidate = read_gzip(candidate_path)
                if (summary['input']['sha256'] != sha(failed_file) or
                        summary['candidate']['sha256'] != sha(candidate_path) or
                        summary['original_solver_invoked'] is not False or
                        candidate['solver_success'] is not False or
                        candidate['candidate_only'] is not True or
                        not exact_equal(candidate['request'], failed['request']) or
                        not exact_equal(candidate['config'], failed['config'])):
                    raise ValueError('Candidate-only source/request/state identity failed') from original_error
                before, after = summary['before']['norm'], summary['full_candidate_replay']['norm']
                if before != failed['response']['lastIteration']['norm']:
                    raise ValueError('Candidate baseline is not the original failed residual') from original_error
                if not (summary['strict_full_replay_improvement'] is True and
                        candidate['strict_full_replay_improvement'] is True and
                        math.isfinite(after) and after < before):
                    self._event('external_candidate_not_improved', before=before, after=after,
                                summary_sha256=sha(summary_path))
                    raise original_error
                self._restart_original_worker(candidate_path, candidate, summary)
                self._event('one_original_worker_retry', failed_logical_call=failed_call,
                            candidate_summary_sha256=sha(summary_path), same_physical_height=True,
                            requested_jacobian=bool(jacobian), requested_audit=bool(audit),
                            retry_jacobian=True, retry_audit=True)
                try:
                    # Deliberately call the native method, not this override:
                    # one recovery budget per logical request, no recursion.
                    return self._native_solve(h, True, True)
                except Exception as retry_error:
                    self._event('original_worker_retry_failed', error=repr(retry_error),
                                failed_logical_call=failed_call,
                                final_record=str(self._record_file()))
                    raise

        def describe_current_response(self, height, response):
            h = np.asarray(height, float)
            if self._last_accepted_record is None:
                raise ValueError('No recorded actual response is attached to this inner problem')
            if self.cache_key is None or self.cache_value is None:
                raise ValueError('The actual-DN cache is empty before the inner problem')
            saved = read_gzip(self._last_accepted_record)
            if (not exact_equal(saved['request']['height'], h.tolist()) or
                    not exact_equal(saved['response'], response) or
                    not exact_equal(self.cache_key.tolist(), h.tolist()) or
                    not exact_equal(self.cache_value, response)):
                raise ValueError('The inner affine anchor differs from the recorded actual DN response')
            return dict(path=str(self._last_accepted_record.resolve()),
                        sha256=sha(self._last_accepted_record), request=saved['request'],
                        response_sha256=payload_sha(response),
                        configuration_sha256=payload_sha(saved['config']),
                        source_sha256=saved['source_sha256'],
                        runtime_source_sha256=self._runtime_sources, generation=self._generation,
                        logical_call=self.calls, worker_call=self.calls-self._generation_base_call)

    return RecoveringWeightedTailPort


def record_inner_dn_anchor(args, outer, tail, height, response, candidate):
    """Add exact call/request provenance to the unchanged raw cubic dump."""
    raw = args.out_prefix.with_name(args.out_prefix.name+f'-inner-{outer:04d}-debug.json.gz')
    if not raw.is_file():
        raise ValueError('The existing raw inner dump must precede this anchor sidecar')
    saved = read_gzip(raw)
    if (saved['solver_success'] is not False or saved['actual_tail_accepted'] is not False or
            not exact_equal(saved['candidate_cut_height'], np.asarray(candidate, float).tolist())):
        raise ValueError('The raw inner dump has a different candidate or acceptance scope')
    anchor = tail.describe_current_response(height, response)
    file = args.out_prefix.with_name(args.out_prefix.name+f'-inner-{outer:04d}-dn-anchor.json')
    payload = dict(scope='Same raw inner cubic and its exact accepted affine-DN anchor; no actual candidate-tail acceptance.',
                   solver_success=False, actual_tail_accepted=False, outer=outer,
                   raw_inner=dict(path=str(raw.resolve()), sha256=sha(raw)),
                   affine_actual_tail=anchor, candidate_cut_height=saved['candidate_cut_height'],
                   prefix_solver_options={name: getattr(args, name) for name in
                       ('tol', 'bc_tol', 'physical_bc_tol', 'max_nodes', 'lagged_tail')},
                   adapter_sha256=sha(__file__))
    write_new_json(file, payload)
    print(json.dumps(dict(event='inner_actual_dn_anchor_saved', outer=outer,
                          path=str(file), sha256=sha(file), actual_tail_accepted=False)), flush=True)
