"""Exact audited-H reuse followed by the original lazy live tail client.

This is an I/O/storage adapter, not a nearby-H approximation. Every counted
response has its own standard packet; unchanged non-audit requests retain
the original client's exact-cache behavior. An audited saved response may
serve only its exact complete H. Every different H starts the original client
and undergoes its original nonlinear solve/Jacobian/audit rules.
"""
from __future__ import annotations
import copy
import gzip
import hashlib
import json
import math
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def equations(config):
    return {key: value for key, value in config.items() if key not in IO}


def verified_packet(packet, ready_file, config, source_topic):
    """The recorded-response gates plus a complete ready/checkpoint binding."""
    stored, ready, cfg = read(packet), read(ready_file), read(config)
    if equations(stored['config']) != equations(cfg):
        raise ValueError('Recorded tail changed equations, spectrum or tolerance')
    for name, expected in stored['source_sha256'].items():
        local = HERE/name
        source = local if local.is_file() else Path(source_topic)/'scripts'/name
        if not source.is_file() or sha(source) != expected:
            raise ValueError('Recorded true-tail source hash differs: '+name)
    M = int(cfg['modes'])
    response, request = stored['response'], stored['request']
    height = np.asarray(request['height'], dtype=float)
    jac = np.asarray(response.get('heightJetJacobian'), dtype=float)
    if (not request.get('jacobian') or not request.get('audit')
            or not response.get('converged') or response.get('audit') is None
            or response.get('failed')
            or not math.isfinite(float(response['residual']))
            or float(response['residual']) > float(cfg['solveTolerance'])
            or height.shape != (M,) or not np.all(np.isfinite(height))
            or jac.size != (3*M+2)*M or not np.all(np.isfinite(jac))
            or not np.array_equal(response['checkpoint']['cutHeight'], height)):
        raise ValueError('A complete successful audited true-H response is required')
    if (equations(ready['parameters']) != equations(response['checkpoint']['parameters'])
            or int(ready['parameters']['modes']) != M
            or len(ready['linearSlope']) != M
            or not np.all(np.isfinite(ready['linearSlope']))):
        raise ValueError('The supplied ready record is not bound to the complete response')
    geometry = ready['storedMetricAdapter']
    frozen = geometry.get('frozenCalibrationAdapter', {})
    compact = geometry.get('compactStorageAdapter', {})
    checks = frozen.get('profileVerification', [])
    if (geometry['profileFingerprintBefore'] != geometry['profileFingerprintAfter']
            or frozen.get('name') != 'frozen-binary-calibration-lookup-v1'
            or frozen.get('reusedCalibrationCount') != 160
            or {row.get('kind') for row in checks} != {'rational-head', 'stored-head'}
            or not all(row.get('exactFingerprintMatch') for row in checks)
            or compact.get('fingerprintBefore') != compact.get('fingerprintAfter')
            or compact.get('explicitGcAvailable') is not True):
        raise ValueError('Complete frozen stored-profile identity is missing')
    provenance = dict(scope=__doc__, packet=str(packet), packet_sha256=sha(packet),
        ready_file=str(ready_file), ready_sha256=sha(ready_file),
        wrapper_sha256=sha(__file__), complete_packet_ready_binding=True,
        ready_checkpoint_I_O_differences={key: dict(ready=ready['parameters'].get(key),
            checkpoint=response['checkpoint']['parameters'].get(key)) for key in IO
            if ready['parameters'].get(key) != response['checkpoint']['parameters'].get(key)},
        all_recorded_tail_source_hashes_checked=True, exact_H_only=True,
        saved_response_had_full_jacobian_and_audit=True,
        live_client_started=False, saved_replays=0, live_logical_responses=0,
        live_new_Node_requests=0)
    return stored, ready, cfg, height, provenance


def make_port_class(Base, packet, ready_file, source_topic, release_between_responses=False):
    class NoProcess:
        def poll(self):
            return None

    class ExactAuditedLazyPort:
        def __init__(self, config, source_root, record_prefix, node_heap=384):
            self.config, self.record_prefix = Path(config), Path(record_prefix)
            if any(self.record_prefix.parent.glob(self.record_prefix.name+'_????.json.gz')):
                raise FileExistsError('Tail record prefix already used')
            stored, ready, self.cfg, self.saved_height, self.provenance = verified_packet(
                packet, ready_file, config, source_topic)
            self.saved_response = stored['response']
            self.ready = copy.deepcopy(ready)
            self.ready['recordedExactAuditedTailAdapter'] = self.provenance
            self.cut = self.ready['cut']
            self.M = int(self.cfg['modes'])
            self.linearD = np.asarray(self.ready['linearSlope'])
            # These dictionaries are fixed before Actual.finalize_output reads
            # them. Protocol provenance is separate from numerical source hashes.
            self.sources = dict(stored['source_sha256'])
            self.calls = 0
            self.cache_key = self.cache_value = None
            self._live = None
            self._absent_process = NoProcess()
            self._last_process = self._absent_process
            self._last_checkpoint = Path(packet)
            self._cache_packet = None
            self._live_generation = 0
            self._source_root, self._node_heap = Path(source_root), node_heap
            self._closed = False
            self.provenance.update(release_worker_between_responses=bool(release_between_responses),
                audit_every_live_response=bool(release_between_responses),
                live_worker_generations=0, live_configurations=[])
            self._write_manifest()

        @property
        def proc(self):
            return self._live.proc if self._live is not None else self._last_process

        def _write_manifest(self):
            path = self.record_prefix.with_name(self.record_prefix.name+'_recorded-adapter.json')
            path.write_text(json.dumps(self.provenance, indent=2)+'\n')

        def _event(self, **row):
            value = dict(event='exact_audited_tail_dispatch', **row)
            path = self.record_prefix.with_name(self.record_prefix.name+'_dispatch.jsonl')
            with path.open('a') as stream:
                stream.write(json.dumps(value)+'\n')
            print(json.dumps(value), flush=True)

        def _ensure_live(self):
            if self._live is not None:
                return
            self._live_generation += 1
            prefix = self.record_prefix.with_name(self.record_prefix.name+f'-live-{self._live_generation:04d}')
            live_config = dict(self.cfg)
            for key, suffix in (('traceFile', '-trace.jsonl'),
                    ('iterationCheckpointFile', '-iteration.json.gz'), ('trialDiagnosticFile', '-trials.jsonl')):
                live_config[key] = str(prefix.with_name(prefix.name+suffix).resolve())
            live_config['initialCheckpoint'] = str(self._last_checkpoint.resolve())
            if equations(live_config) != equations(self.cfg):
                raise AssertionError('A worker restart altered the tail problem')
            config_path = prefix.with_name(prefix.name+'-config.json')
            with config_path.open('x') as stream:
                stream.write(json.dumps(live_config, indent=2)+'\n')
            self.provenance['live_configurations'].append(dict(file=str(config_path),
                sha256=sha(config_path), warm=str(self._last_checkpoint),
                warm_sha256=sha(self._last_checkpoint),
                changed_keys=sorted(k for k in IO if live_config.get(k) != self.cfg.get(k))))
            self._live = Base(config_path, self._source_root, prefix, node_heap=self._node_heap)
            self._last_process = self._live.proc
            if self._live.sources != self.sources:
                self._live.close()
                raise ValueError('The live true-tail numerical sources differ from the audited source')
            expected, actual = self.ready, self._live.ready
            if (equations(expected['parameters']) != equations(actual['parameters'])
                    or expected['linearSlope'] != actual['linearSlope']
                    or expected['cut'] != actual['cut']):
                self._live.close()
                raise ValueError('The live complete finite-tail ready identity differs')
            a, b = expected['storedMetricAdapter'], actual['storedMetricAdapter']
            for key in ('frozenWarpAlpha', 'profileFingerprintBefore', 'profileFingerprintAfter',
                    'fingerprintFields', 'fingerprintFractions'):
                if a[key] != b[key]:
                    self._live.close()
                    raise ValueError('The live stored physical fingerprint differs: '+key)
            if equations(a['physicalParameters']) != equations(b['physicalParameters']):
                self._live.close()
                raise ValueError('The live stored physical parameters differ')
            self.provenance['live_client_started'] = True
            self.provenance['live_worker_generations'] = self._live_generation
            self._write_manifest()
            self._event(kind='live-client-started', original_full_H_solve_required=True)

        def solve(self, height, jacobian=True, audit=False):
            if self._closed:
                raise RuntimeError('Tail client is already closed')
            h = np.asarray(height, dtype=float)
            if h.shape != (self.M,) or not np.all(np.isfinite(h)):
                raise ValueError('Incomplete/nonfinite physical Dirichlet vector')
            if (self.cache_key is not None and np.array_equal(h, self.cache_key)
                    and not audit and (not jacobian or self.cache_value.get('heightJetJacobian') is not None)):
                return self.cache_value
            if np.array_equal(h, self.saved_height):
                response = self.saved_response
                kind = 'saved-exact-audited-H'
                node_request_increment = 0
                self.provenance['saved_replays'] += 1
                origin = dict(packet=str(packet), sha256=self.provenance['packet_sha256'])
            elif (self.cache_key is not None and np.array_equal(h, self.cache_key)
                    and audit and self.cache_value.get('audit') is not None
                    and (not jacobian or self.cache_value.get('heightJetJacobian') is not None)):
                response = self.cache_value
                kind = 'cached-exact-audited-live-H'
                node_request_increment = 0
                origin = dict(packet=str(self._cache_packet), sha256=sha(self._cache_packet))
            else:
                self._ensure_live()
                previous_live_calls = self._live.calls
                response = self._live.solve(h, jacobian=jacobian,
                    audit=bool(audit or release_between_responses))
                node_request_increment = self._live.calls-previous_live_calls
                kind = 'live-client-full-H-response'
                self.provenance['live_logical_responses'] += 1
                self.provenance['live_new_Node_requests'] += node_request_increment
                original = self._live.record_prefix.with_name(
                    self._live.record_prefix.name+f'_{self._live.calls:04d}.json.gz')
                origin = dict(packet=str(original), sha256=sha(original))
            if audit and response.get('audit') is None:
                raise ValueError('An unaudited cached/live response cannot answer an audit request')
            self.calls += 1
            record = dict(request=dict(height=h.tolist(), jacobian=bool(jacobian), audit=bool(audit)),
                response=response, config=self.cfg, source_sha256=self.sources,
                exact_audited_tail_io_adapter=dict(kind=kind, origin=origin,
                    wrapper_sha256=self.provenance['wrapper_sha256'],
                    new_Node_request=bool(node_request_increment),
                    live_request_increment=node_request_increment,
                    reused_already_audited_packet=bool(not node_request_increment and response.get('audit') is not None),
                    source_packet_sha=origin['sha256'],
                    audit_recomputed_in_this_request=bool(node_request_increment and response.get('audit') is not None)))
            contents = gzip.compress((json.dumps(record, separators=(',', ':'))+'\n').encode(), mtime=0)
            if len(contents) >= 5_000_000:
                raise ValueError('Tail response exceeds the per-file limit')
            destination = self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
            with destination.open('xb') as stream:
                stream.write(contents)
            self.cache_key, self.cache_value = h.copy(), response
            self._cache_packet = self._last_checkpoint = destination
            if release_between_responses and self._live is not None:
                process = self._live.proc
                self._live.close()
                if process.poll() is None:
                    raise RuntimeError('Tail worker did not exit before returning to the prefix')
                self._event(kind='live-worker-released-after-recording',
                    generation=self._live_generation, worker_returncode=process.poll(),
                    complete_audited_packet=str(destination))
                self._live = None
            self._write_manifest()
            self._event(kind=kind, call=self.calls, audit=bool(audit), packet=str(destination),
                exact_saved_H=bool(np.array_equal(h, self.saved_height)),
                live_client_started=self.provenance['live_client_started'])
            return response

        def close(self):
            if self._closed:
                return
            if self._live is not None:
                self._live.close()
            self._closed = True
            self._write_manifest()

    return ExactAuditedLazyPort
