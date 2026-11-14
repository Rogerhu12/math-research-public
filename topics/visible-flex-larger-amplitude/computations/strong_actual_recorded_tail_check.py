#!/usr/bin/env python3
"""Check exact-H dispatch and audited-packet guards using a real accepted tail.

No Node process or BVP is launched. The live-client test double raises at its
solve entry rather than returning any fabricated new-H numerical result.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import gzip
import json
from pathlib import Path
import tempfile
import time
import numpy as np
from strong_actual_recorded_tail_port import make_port_class, verified_packet, read, sha


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted-reference', 'packet', 'source-topic', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--second-packet', type=Path)
    parser.add_argument('--second-ready', type=Path)
    args = parser.parse_args()
    if bool(args.second_packet) != bool(args.second_ready):
        raise ValueError('The optional worker-release replay needs a complete second packet and ready')
    started = time.monotonic()
    source = Path(__file__).with_name('strong_actual_recorded_tail_port.py')
    hashes = {str(p): sha(p) for p in (Path(__file__), source, args.accepted_reference, args.packet)}
    if args.second_packet:
        hashes.update({str(p): sha(p) for p in (args.second_packet, args.second_ready)})
    reference, packet = read(args.accepted_reference), read(args.packet)
    checks = {}
    events = []
    class DelegationReached(RuntimeError):
        pass

    with tempfile.TemporaryDirectory(prefix='strong-recorded-tail-check-') as temp:
        root = Path(temp)
        ready_file, config_file = root/'ready.json', root/'config.json'
        ready_file.write_text(json.dumps(reference['actual_tail']['ready']))
        config_file.write_text(json.dumps(packet['config']))
        stored, ready, cfg, height, info = verified_packet(
            args.packet, ready_file, config_file, args.source_topic)
        class FakeLive:
            def __init__(self, config, source_root, record_prefix, node_heap):
                events.append('live-constructor-dispatched-without-starting-worker')
                self.ready = copy.deepcopy(ready)
                self.sources = dict(stored['source_sha256'])
                self.record_prefix = Path(record_prefix)
                self.calls = 0
                self.proc = type('NoWorker', (), {'poll': lambda self: None})()
            def solve(self, new_height, jacobian=True, audit=False):
                events.append(dict(live_solve_reached=True, exact_saved_H=bool(np.array_equal(new_height, height)),
                    jacobian=jacobian, audit=audit))
                raise DelegationReached('No numerical result is supplied by this test double')
            def close(self):
                events.append('fake-close')
        Port = make_port_class(FakeLive, args.packet, ready_file, args.source_topic)
        port = Port(config_file, args.source_topic/'repro/source-root', root/'response', node_heap=384)
        assert port.proc.poll() is None and not events
        exact = port.solve(height, jacobian=True, audit=False)
        assert exact == stored['response'] and port.calls == 1 and not events
        repeated = port.solve(height, jacobian=True, audit=False)
        assert repeated is exact and port.calls == 1 and not events
        audited = port.solve(height, jacobian=True, audit=True)
        assert audited == exact and audited['audit'] is not None and port.calls == 2 and not events
        files = [root/'response_0001.json.gz', root/'response_0002.json.gz']
        for path in files:
            row = read(path)
            assert row['response'] == stored['response']
            assert row['exact_audited_tail_io_adapter']['new_Node_request'] is False
        checks['exact_H_reused_complete_formal_packet_without_worker'] = True
        checks['non_audit_exact_cache_preserves_original_call_count'] = True
        checks['audit_reuse_has_complete_audit_and_correct_final_packet_path'] = True
        changed = height.copy()
        changed[0] = np.nextafter(changed[0], np.inf)
        try:
            port.solve(changed, jacobian=True, audit=False)
        except DelegationReached:
            pass
        else:
            raise AssertionError('A one-ULP changed H was served from the saved audited packet')
        assert port.calls == 2 and events[-1]['exact_saved_H'] is False
        checks['one_ULP_changed_H_dispatches_to_original_live_solve'] = True
        port.close()
        port.close()
        assert events.count('fake-close') == 1
        checks['cache_only_proc_facade_and_idempotent_close_compatible'] = True
        if args.second_packet:
            second, second_ready, second_cfg, second_H, second_info = verified_packet(
                args.second_packet, args.second_ready, config_file, args.source_topic)
            assert not np.array_equal(second_H, height)
            replays = []
            class ExistingResponseReplay:
                def __init__(self, config, source_root, record_prefix, node_heap):
                    self.ready = copy.deepcopy(second_ready)
                    self.sources = dict(second['source_sha256'])
                    self.config, self.record_prefix = Path(config), Path(record_prefix)
                    self.calls, self.closed = 0, False
                    owner = self
                    self.proc = type('NoWorkerReplay', (), {'poll': lambda self: 0 if owner.closed else None})()
                    replays.append('constructor-with-no-Node')
                def solve(self, h, jacobian=True, audit=False):
                    assert np.array_equal(h, second_H) and jacobian and audit
                    self.calls += 1
                    recorded = dict(request=dict(height=h.tolist(), jacobian=True, audit=True),
                        response=second['response'], config=read(self.config), source_sha256=self.sources,
                        protocol_test_only=True, preexisting_response_source=str(args.second_packet))
                    path = self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
                    path.write_bytes(gzip.compress(json.dumps(recorded).encode(), mtime=0))
                    replays.append('replayed-existing-second-formal-packet-without-solving')
                    return second['response']
                def close(self):
                    self.closed = True
                    replays.append('closed-before-return-to-prefix')
            ReleasePort = make_port_class(ExistingResponseReplay, args.packet, ready_file,
                args.source_topic, release_between_responses=True)
            releasing = ReleasePort(config_file, args.source_topic/'repro/source-root', root/'release-response')
            value = releasing.solve(second_H, jacobian=True, audit=False)
            assert value == second['response'] and releasing.proc.poll() == 0
            assert replays.count('closed-before-return-to-prefix') == 1
            audited = releasing.solve(second_H, jacobian=True, audit=True)
            final_file = root/f'release-response_{releasing.calls:04d}.json.gz'
            final_record = read(final_file)
            assert audited == value and final_record['request']['audit'] is True
            assert final_record['exact_audited_tail_io_adapter']['reused_already_audited_packet'] is True
            assert final_record['exact_audited_tail_io_adapter']['new_Node_request'] is False
            assert replays.count('constructor-with-no-Node') == 1
            releasing.close()
            checks['release_mode_requests_full_audit_before_worker_close'] = True
            checks['release_mode_closes_worker_before_return_to_prefix'] = True
            checks['final_exact_H_reuses_full_audit_with_explicit_provenance_and_packet'] = True
            events.append(dict(preexisting_second_packet_protocol_replay=replays,
                no_new_numerical_response_fabricated=True))
        bad = copy.deepcopy(stored)
        bad['response']['audit'] = None
        bad_file = root/'unaudited.json.gz'
        bad_file.write_bytes(gzip.compress(json.dumps(bad).encode(), mtime=0))
        try:
            verified_packet(bad_file, ready_file, config_file, args.source_topic)
        except ValueError:
            checks['unaudited_response_rejected'] = True
        else:
            raise AssertionError('An unaudited response passed the exact audited-H guard')
        wrong_ready = copy.deepcopy(ready)
        wrong_ready['parameters']['modes'] += 1
        ready_file.write_text(json.dumps(wrong_ready))
        try:
            verified_packet(args.packet, ready_file, config_file, args.source_topic)
        except ValueError:
            checks['ready_checkpoint_parameter_mismatch_rejected'] = True
        else:
            raise AssertionError('An unrelated ready record was accepted')
    report = dict(scope=__doc__, passed=all(checks.values()), checks=checks,
        source_sha256=hashes, live_test_double_events=events,
        Node_processes_started=0, BVPs_solved=0, new_H_responses_fabricated=0,
        temporary_packets_discarded_after_verification=True,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(event='recorded_true_tail_check_complete', **report)), flush=True)


if __name__ == '__main__':
    main()
