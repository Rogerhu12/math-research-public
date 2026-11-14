#!/usr/bin/env python3
"""Replay two genuine audited tails through the existing exact-H port, no Node.

The live stand-in returns only the explicitly supplied, already completed second
response and only at its exact complete H. It never solves or fabricates a new
response. The replay checks the proposed post-RMS audit=True dispatch, the
unchanged final audit=True cache path, complete packet/source/ready identities,
and rejection/delegation at incomplete or different inputs. All temporary
protocol packets are discarded. This is preparation, not a new accepted BVP or
an observed reduction in actual Newton/variational work.
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
    for name in ('previous-primary', 'previous-packet', 'current-primary',
                 'current-packet', 'current-ready', 'source-topic', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh protocol replay report')
    started = time.monotonic()
    paths = [Path(__file__), Path(__file__).with_name('strong_actual_recorded_tail_port.py'),
             Path(__file__).with_name('strong_eager_true_H_audit_initial_laws_actual_bvp.py'),
             args.previous_primary, args.previous_packet, args.current_primary,
             args.current_packet, args.current_ready]
    hashes = {str(path): sha(path) for path in paths}
    previous, current = read(args.previous_primary), read(args.current_primary)
    checks, events = {}, []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks[name] = True

    for name, primary in (('previous', previous), ('current', current)):
        check(name+'_primary_is_accepted_and_audited',
              bool(primary.get('solver_success')) and not primary.get('audit_pending', True)
              and primary['actual_tail'].get('audit') is not None)

    class DelegationReached(RuntimeError):
        pass

    with tempfile.TemporaryDirectory(prefix='strong-eager-audit-replay-') as temp:
        root = Path(temp)
        ready_file, config_file = root/'previous-ready.json', root/'config.json'
        ready_file.write_text(json.dumps(previous['actual_tail']['ready']))
        config_file.write_text(json.dumps(read(args.current_packet)['config']))
        first, ready, cfg, old_H, unused = verified_packet(
            args.previous_packet, ready_file, config_file, args.source_topic)
        second, second_ready, second_cfg, new_H, unused = verified_packet(
            args.current_packet, args.current_ready, config_file, args.source_topic)
        check('two_actual_complete_H_are_different', not np.array_equal(old_H, new_H))
        check('all_numeric_source_hashes_identical', first['source_sha256'] == second['source_sha256'])
        check('current_ready_is_actual_accepted_primary_ready',
              second_ready == current['actual_tail']['ready'])
        for field in ('audit', 'jets', 'residual'):
            check('current_'+field+'_equals_actual_accepted_primary',
                  second['response'][field] == current['actual_tail'][field])
        expected_H = np.asarray(second['response']['checkpoint']['cutHeight'], dtype=np.float64)
        check('complete_current_H_bits_match_checkpoint', new_H.tobytes() == expected_H.tobytes())

        class ExistingAuditedResponse:
            def __init__(self, config, source_root, record_prefix, node_heap):
                self.ready = copy.deepcopy(second_ready)
                self.sources = dict(second['source_sha256'])
                self.config, self.record_prefix = Path(config), Path(record_prefix)
                self.calls, self.closed = 0, False
                owner = self
                self.proc = type('NoWorker', (), {'poll': lambda self: 0 if owner.closed else None})()
                events.append('constructed_protocol_replay_without_Node')

            def solve(self, height, jacobian=True, audit=False):
                h = np.asarray(height, dtype=np.float64)
                if h.tobytes() != new_H.tobytes():
                    events.append('different_H_dispatched_to_original_live_solve_entry')
                    raise DelegationReached('No other numerical response is supplied by the replay')
                check('post_RMS_live_request_really_asks_full_J_and_audit', jacobian is True and audit is True)
                self.calls += 1
                packet = dict(request=dict(height=h.tolist(), jacobian=True, audit=True),
                    response=second['response'], config=read(self.config),
                    source_sha256=self.sources, protocol_replay_only=True,
                    preexisting_completed_response=str(args.current_packet),
                    preexisting_completed_response_sha256=sha(args.current_packet))
                file = self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
                file.write_bytes(gzip.compress(json.dumps(packet).encode(), mtime=0))
                events.append('returned_only_preexisting_completed_audited_response')
                return second['response']

            def close(self):
                self.closed = True
                events.append('closed_replay_no_worker')

        Port = make_port_class(ExistingAuditedResponse, args.previous_packet,
            ready_file, args.source_topic, release_between_responses=False)
        port = Port(config_file, args.source_topic/'repro/source-root', root/'response')
        initial = port.solve(old_H, jacobian=True, audit=False)
        check('initial_anchor_retains_original_unaudited_request', initial == first['response'] and port.calls == 1)
        check('saved_initial_H_does_not_start_live_replay', not events)
        actual = port.solve(new_H, jacobian=True, audit=True)
        actual_file = root/'response_0002.json.gz'
        actual_packet = read(actual_file)
        check('post_RMS_standard_packet_is_genuinely_audited',
              actual_packet['request']['audit'] is True and actual_packet['request']['jacobian'] is True
              and actual_packet['response'] == second['response'] and port.calls == 2)
        check('post_RMS_dispatch_records_live_origin',
              actual_packet['exact_audited_tail_io_adapter']['kind'] == 'live-client-full-H-response')
        verified_packet(actual_file, args.current_ready, config_file, args.source_topic)
        check('post_RMS_packet_passes_original_complete_verified_packet_gate', True)
        final = port.solve(new_H, jacobian=True, audit=True)
        final_file = root/'response_0003.json.gz'
        final_packet = read(final_file)
        meta = final_packet['exact_audited_tail_io_adapter']
        check('final_logical_packet_count_and_path_preserved', port.calls == 3 and final_file.is_file())
        check('final_packet_uses_exact_audited_live_H_cache', meta['kind'] == 'cached-exact-audited-live-H')
        check('final_full_response_is_unchanged', final == actual == second['response'])
        check('final_complete_H_bits_are_identical',
              np.asarray(final_packet['request']['height'], np.float64).tobytes() == new_H.tobytes())
        check('final_origin_points_to_actual_complete_post_RMS_packet',
              meta['origin'] == dict(packet=str(actual_file), sha256=sha(actual_file)))
        check('final_has_no_second_live_request',
              meta['new_Node_request'] is False and meta['live_request_increment'] == 0
              and meta['reused_already_audited_packet'] is True
              and meta['audit_recomputed_in_this_request'] is False
              and port._live.calls == 1)
        verified_packet(final_file, args.current_ready, config_file, args.source_topic)
        check('final_packet_passes_original_complete_verified_packet_gate', True)
        perturbed = new_H.copy()
        perturbed[0] = np.nextafter(perturbed[0], np.inf)
        try:
            port.solve(perturbed, jacobian=True, audit=True)
        except DelegationReached:
            check('one_ULP_changed_final_H_requires_new_live_audit', port.calls == 3)
        else:
            raise AssertionError('A changed final H was served from the cache')
        port.close()

        for name in ('request_audit', 'request_jacobian', 'full_J', 'audit', 'residual', 'modes'):
            bad = copy.deepcopy(second)
            if name.startswith('request_'):
                bad['request'][name.removeprefix('request_')] = False
            elif name == 'full_J':
                bad['response']['heightJetJacobian'] = bad['response']['heightJetJacobian'][:-1]
            elif name == 'audit':
                bad['response']['audit'] = None
            elif name == 'residual':
                bad['response']['residual'] = 2*float(cfg['solveTolerance'])
            elif name == 'modes':
                bad['config']['modes'] += 1
            file = root/(name+'-invalid.json.gz')
            file.write_bytes(gzip.compress(json.dumps(bad).encode(), mtime=0))
            try:
                verified_packet(file, args.current_ready, config_file, args.source_topic)
            except ValueError:
                checks['incomplete_or_changed_'+name+'_rejected'] = True
            else:
                raise AssertionError('An incomplete or changed '+name+' packet passed')

    report = dict(scope=__doc__, passed=all(checks.values()), checks=checks,
        source_sha256=hashes, replay_events=events,
        complete_H_count=len(new_H), full_height_J_entries=len(second['response']['heightJetJacobian']),
        source_response_residual=second['response']['residual'],
        Node_processes_started=0, new_numerical_responses=0, new_BVPs_solved=0,
        temporary_packets_discarded=True, actual_runtime_gain_not_yet_measured=True,
        seconds=time.monotonic()-started)
    with args.out.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(event='eager_audit_protocol_replay_complete', passed=report['passed'],
        checks=len(checks), seconds=report['seconds'], Node_processes_started=0)), flush=True)


if __name__ == '__main__':
    main()
