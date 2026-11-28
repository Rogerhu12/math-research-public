"""Strict complete-request reuse of a genuinely accepted full-height response.

This module never changes a native kernel or fabricates a solver return. A
matching request copies the original packet bytes to the new logical record
name and records the prior computation explicitly in a separate sidecar.
Every other request follows the unchanged original client, including its
existing non-audit response cache. No new acceptance follows from memoization.
"""
import copy
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np

from tail_full_state_tangent_predictor import load, module, read_packet, ref

RUNTIME_CONFIG_KEYS = frozenset(('traceFile', 'initialCheckpoint'))
PACKET_SOURCE_NAMES = frozenset(('950f-tail-client-v3.py', '950f-tail-stage-port-v3.mjs',
    '950f-tail-stage-core.mjs', '950f-tail-stage-split.mjs', '950f-tail-subdivision.mjs',
    '950f-tail-warm-remesh.mjs', 'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs'))


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True,
                      allow_nan=False).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def checked(item):
    if ref(item['path']) != item:
        raise ValueError('Bound memoization evidence changed: '+item['path'])
    return Path(item['path'])


def mathematical_config(value):
    for key in RUNTIME_CONFIG_KEYS:
        if key in value and not isinstance(value[key], str):
            raise ValueError('Only declared string execution paths may be excluded: '+key)
    return {k: v for k, v in value.items() if k not in RUNTIME_CONFIG_KEYS}


def request_identity(request):
    if set(request) != {'height', 'jacobian', 'audit'}:
        raise ValueError('Complete original request keys are required')
    if type(request['jacobian']) is not bool or type(request['audit']) is not bool:
        raise ValueError('Original boolean request fields are required')
    h = np.asarray(request['height'], dtype='<f8')
    if h.ndim != 1 or not np.all(np.isfinite(h)):
        raise ValueError('Complete finite physical height is required')
    return dict(request_sha256=digest(canonical(request)), height_f64le_sha256=digest(h.tobytes()),
                height_count=len(h), jacobian=request['jacobian'], audit=request['audit'])


def owned_source_map(manifest):
    root = Path(manifest['source_topic']).resolve()
    answer = {}
    for item in manifest['owned_sources']:
        path = checked(item)
        name = str(path.relative_to(root))
        if name in answer:
            raise ValueError('Duplicate native owned source')
        answer[name] = item
    return answer


def build_proof(source_summary, current_config, current_manifest, source_root, repo):
    """Validate a real completed E response without invoking any solver."""
    source_summary, current_config, current_manifest, source_root, repo = map(
        lambda p: Path(p).resolve(), (source_summary, current_config, current_manifest, source_root, repo))
    s = load(source_summary)
    if (s.get('status') != 'original_complete_height_tail_returned'
            or s.get('result', {}).get('accepted') is not True
            or s['result'].get('original_full_height_returned') is not True):
        raise ValueError('Only a genuinely returned complete original full-height response is reusable')
    last = s['stages'][-1]
    if (last.get('factor') != 1. or last.get('original_full_height') is not True
            or last.get('original_finite_response_passed') is not True
            or last.get('requested_jacobian') is not True or last.get('requested_audit') is not True):
        raise ValueError('The last actual stage is not the complete audited full-height/J response')
    packet_path = checked(last['packet']); original_manifest_path = checked(last['native_manifest'])
    if (s['result']['full_height_record'] != str(packet_path)
            or s['result']['full_height_record_sha256'] != last['packet']['sha256']):
        raise ValueError('The completed response and actual stage identities differ')
    packet = read_packet(packet_path); response = packet['response']; cfg = packet['config']
    request = packet['request']; request_key = request_identity(request)
    current = load(current_config); M = int(cfg['modes'])
    current_initial = current.get('initialCheckpoint')
    if (not isinstance(current_initial, str)
            or Path(current_initial).resolve() != packet_path
            or ref(current_initial) != last['packet']):
        raise ValueError('The current full-state initializer must be the exact reusable accepted packet')
    if (request_key['height_count'] != M or request['jacobian'] is not True or request['audit'] is not True
            or response.get('converged') is not True or response.get('failed')
            or not isinstance(response.get('residual'), (int, float))
            or not math.isfinite(response['residual']) or response['residual'] > cfg['solveTolerance']
            or not isinstance(response.get('audit'), dict)):
        raise ValueError('The reusable response did not pass the original complete finite gates')
    # Finite JSON includes every diagnostic/checkpoint/J entry; None in original
    # iteration metadata stays None and is not converted into a numerical value.
    canonical(response)
    cp = response['checkpoint']; states = np.asarray(cp['states'], float)
    jac = np.asarray(response.get('heightJetJacobian'), float)
    if (states.ndim != 2 or states.shape[1] != 2*M or states.shape[0] != cp['parameters']['depth']+1
            or not np.all(np.isfinite(states)) or cp['parameters']['modes'] != M
            or cp['parameters']['spacing'] != cfg['spacing'] or cp['cutHeight'] != request['height']
            or jac.shape != ((3*M+2)*M,) or not np.all(np.isfinite(jac))):
        raise ValueError('Complete states, height Jacobian or request/checkpoint identity is absent')
    old_math, new_math = mathematical_config(cfg), mathematical_config(current)
    if canonical(old_math) != canonical(new_math):
        raise ValueError('A numeric, physical, solver or other non-execution configuration changed')
    height_reference = Path(s['result']['height_reference'])
    if ref(height_reference)['sha256'] != s['result']['height_reference_sha256']:
        raise ValueError('Actual source full-height reference changed')
    height = load(height_reference)
    for key in s['result']['height_reference_key'].split('.'):
        height = height[key]
    if np.asarray(height, dtype='<f8').tobytes() != np.asarray(request['height'], dtype='<f8').tobytes():
        raise ValueError('The accepted request is not the literal complete source height')
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    sys.path.insert(0, str(scripts/'resume_20261126'))
    helpers = module('_memo_true_native_identity', scripts/'resume_20261126/seam_export_tail_geometry_v2.py')
    provenance = module('_memo_original_provenance', scripts/'resume_20261126/continue_original_actual_dn_chord.py')
    old_manifest, new_manifest = load(original_manifest_path), load(current_manifest)
    provenance.verify_references(old_manifest); provenance.verify_references(new_manifest)
    old_root, new_root = Path(old_manifest['source_topic']).resolve(), Path(new_manifest['source_topic']).resolve()
    if source_root != new_root/'repro/source-root':
        raise ValueError('The current client source root differs from its native manifest')
    if canonical(old_manifest['fixed_scope']) != canonical(new_manifest['fixed_scope']):
        raise ValueError('Original native full finite scope changed')
    old_sources, new_sources = owned_source_map(old_manifest), owned_source_map(new_manifest)
    if old_sources.keys() != new_sources.keys():
        raise ValueError('Original native source inventories differ')
    source_checks = []; relocated = []
    for name, prior in old_sources.items():
        actual = new_sources[name]
        if prior['sha256'] != actual['sha256']:
            if name != 'scripts/native_batch_adapter.mjs':
                raise ValueError('An original mathematical source changed: '+name)
            before, after = Path(prior['path']).read_bytes(), Path(actual['path']).read_bytes()
            # The recovered installer embeds only the absolute parallel-plan
            # path here. No arbitrary whitespace or code normalization is used.
            if str(old_root).encode() not in before or before.replace(str(old_root).encode(), str(new_root).encode()) != after:
                raise ValueError('Native adapter differs beyond its exact owned-directory relocation')
            relocated.append(dict(relative_path=name, old=prior, current=actual,
                                  replacement_from=str(old_root), replacement_to=str(new_root)))
        source_checks.extend((prior, actual))
    if old_manifest['native_files'].keys() != new_manifest['native_files'].keys():
        raise ValueError('Native source/kernel/wrapper binding keys differ')
    for name, prior in old_manifest['native_files'].items():
        actual = new_manifest['native_files'][name]
        if prior['sha256'] != actual['sha256']:
            raise ValueError('Original native binary/CPP/header/wrapper/plan changed: '+name)
        source_checks.extend((prior, actual))
    if (canonical(old_manifest['runtime_libraries']) != canonical(new_manifest['runtime_libraries'])
            or old_manifest['execution_provider']['workers'] != new_manifest['execution_provider']['workers']):
        raise ValueError('Native runtime/provider execution binding differs')
    if set(packet['source_sha256']) != PACKET_SOURCE_NAMES:
        raise ValueError('The accepted packet omits an original client/worker source')
    for name, expected in packet['source_sha256'].items():
        if (ref(old_root/'scripts'/name)['sha256'] != expected
                or ref(new_root/'scripts'/name)['sha256'] != expected):
            raise ValueError('Original complete packet client/worker source changed: '+name)
    native_runs = packet_path.parent/'native-runs'; selected = None
    for path in sorted(native_runs.glob('*-jac-record.json'), reverse=True):
        record = load(path)
        if record.get('withJac') is True and helpers.state_match(path, packet):
            selected = path; break
    if selected is None:
        raise ValueError('No complete actual fresh native J matches the accepted state')
    record = load(selected)
    if record['manifest'] != last['native_manifest'] or record.get('status') != 'complete':
        raise ValueError('The exact accepted native record is not bound to its actual manifest')
    for name in ('input', 'output', 'manifest', 'static_metadata'):
        checked(record[name]); source_checks.append(record[name])
    if record['returned_flow_count'] != states.shape[0]-1:
        raise ValueError('The final fresh native J does not cover every accepted stage')
    proof = dict(schema='held10-exact-complete-response-reuse-v1', source=ref(__file__),
        source_summary=ref(source_summary), source_packet=ref(packet_path), source_request=request_key,
        source_response_sha256=digest(canonical(response)), source_height_reference=ref(height_reference),
        source_native_manifest=ref(original_manifest_path), current_native_manifest=ref(current_manifest),
        source_actual_fresh_native_record=ref(selected), source_native_run_dir=str(native_runs),
        source_math_config_sha256=digest(canonical(old_math)), current_math_config_sha256=digest(canonical(new_math)),
        current_config=ref(current_config), execution_config_keys=sorted(RUNTIME_CONFIG_KEYS),
        execution_config_values=dict(source={k:cfg.get(k) for k in RUNTIME_CONFIG_KEYS},
                                     current={k:current.get(k) for k in RUNTIME_CONFIG_KEYS}),
        exact_owned_path_relocations=relocated, original_finite_gate_passed=True,
        complete_unknown_count=int(states.size), height_J_count=int(jac.size),
        original_residual=response['residual'], source_checks=source_checks,
        verification_sources=[ref(scripts/'resume_20261126/seam_export_tail_geometry_v2.py'),
                              ref(scripts/'resume_20261126/continue_original_actual_dn_chord.py'),
                              ref(Path(__file__).with_name('tail_full_state_tangent_predictor.py'))],
        physical_equations_changed=False, fresh_native_calculation_claimed=False,
        source_packet_bytes_modified=False, complete_surface=False)
    return proof, packet


def install(client, *, source_summary, current_manifest, repo, records):
    """Wrap only this independently loaded client class; old files stay intact."""
    Original = client.WeightedTailPort
    class ExactCompleteResponseMemo(Original):
        def __init__(self, config, source_root, record_prefix, node_heap=1536):
            proof, packet = build_proof(source_summary, config, current_manifest, source_root, repo)
            self._memo_proof, self._memo_packet = proof, packet
            self._memo_sidecar = Path(record_prefix).parent/'tail-response-memoization.json'
            if self._memo_sidecar.exists():
                raise FileExistsError('Use a fresh actual memoization record')
            self._memo_events = []
            self._memo_log = dict(scope=__doc__, proof=proof, events=self._memo_events,
                source_packet_is_prior_actual_execution=True, native_worker_calls_match_logical_record_numbers=False,
                logical_record_numbers_include_explicit_prior_response_reuse=True)
            self._save_memo()
            super().__init__(config, source_root, record_prefix, node_heap=node_heap)
            records.append(dict(path=str(self._memo_sidecar), initialized=True))

        def _save_memo(self):
            temporary = self._memo_sidecar.with_suffix('.json.tmp')
            temporary.write_text(json.dumps(self._memo_log, indent=2, allow_nan=False)+'\n')
            temporary.replace(self._memo_sidecar)

        def solve(self, height, jacobian=True, audit=False):
            h = np.asarray(height, float)
            request = dict(height=h.tolist(), jacobian=bool(jacobian), audit=bool(audit))
            key = request_identity(request)
            if key != self._memo_proof['source_request']:
                before = self.calls
                try:
                    result = super().solve(height, jacobian=jacobian, audit=audit)
                    return result
                finally:
                    self._memo_events.append(dict(time_unix=time.time(), kind='original_client_path',
                        request=key, logical_calls_before=before, logical_calls_after=self.calls,
                        new_native_request_sent=self.calls>before,
                        original_existing_non_audit_cache_used=self.calls==before))
                    self._save_memo()
            for item in [self._memo_proof[k] for k in ('source','source_summary','source_packet','source_height_reference','source_native_manifest',
                         'current_native_manifest','source_actual_fresh_native_record','current_config')]:
                checked(item)
            for item in self._memo_proof['source_checks']+self._memo_proof['verification_sources']:
                checked(item)
            if digest(canonical(self._memo_packet['response'])) != self._memo_proof['source_response_sha256']:
                raise ValueError('The in-memory source response was modified')
            self.calls += 1
            path = self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
            if path.exists():
                raise FileExistsError('A logical tail record already exists')
            # Exact byte copy retains the true old config/execution history.
            # The current runtime equivalence is stated only in the sidecar.
            with path.open('xb') as stream:
                stream.write(Path(self._memo_proof['source_packet']['path']).read_bytes())
            if ref(path)['sha256'] != self._memo_proof['source_packet']['sha256']:
                raise ValueError('Memoized original packet copy changed')
            self.cache_key = h.copy(); self.cache_value = copy.deepcopy(self._memo_packet['response'])
            self._memo_events.append(dict(time_unix=time.time(), kind='prior_complete_response_reused',
                request=key, logical_call=self.calls, record=ref(path),
                source_packet=self._memo_proof['source_packet'], fresh_native_calculation_performed=False,
                canonical_request_and_height_bytes_identical=True, source_response_bytes_unchanged=True))
            self._save_memo()
            return copy.deepcopy(self.cache_value)
    client.WeightedTailPort = ExactCompleteResponseMemo

