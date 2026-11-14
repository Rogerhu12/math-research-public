#!/usr/bin/env python3
"""Check actual first-live warm delivery and fallback using preexisting packets.

No Node or ODE runs. The stand-in returns only one supplied completed true-H
response, and refuses any new audited numerical result. The original recorded
port and the new input-only subclass are exercised together. A constructor
receipt is distinguished from selection and from nonlinear acceptance.
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
from strong_recorded_port_explicit_hermite_warm import make_first_warm_port_class, verified_warm


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('primary', 'packet', 'ready', 'warm', 'warm-report', 'completed-target-packet', 'source-topic', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh protocol replay report')
    started = time.monotonic()
    warm_record, target = verified_warm(args.warm, args.warm_report, args.primary, args.packet)
    completed = read(args.completed_target_packet)
    checks, events = {}, []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks[name] = True

    check('preexisting_target_packet_has_exact_full_H_bits',
          np.asarray(completed['request']['height'], np.float64).tobytes() == target.tobytes())
    check('preexisting_target_true_solve_full_J_is_complete',
          completed['response'].get('converged') is True
          and completed['response']['residual'] <= completed['config']['solveTolerance']
          and len(completed['response']['heightJetJacobian']) == (3*len(target)+2)*len(target))
    check('target_source_is_not_mislabelled_as_final_audit',
          completed['request']['audit'] is False and completed['response'].get('audit') is None)
    class DelegationReached(RuntimeError):
        pass

    with tempfile.TemporaryDirectory(prefix='strong-explicit-first-warm-replay-') as temp:
        root = Path(temp)
        config = root/'config.json'
        config.write_text(json.dumps(read(args.packet)['config']))
        stored, ready, cfg, saved_H, unused = verified_packet(args.packet, args.ready, config, args.source_topic)
        check('actual_target_and_saved_full_H_differ', not np.array_equal(target, saved_H))
        check('all_target_tail_numeric_sources_match', completed['source_sha256'] == stored['source_sha256'])

        class ExistingTargetReplay:
            def __init__(self, live_config, source_root, record_prefix, node_heap):
                self.config, self.record_prefix = Path(live_config), Path(record_prefix)
                self.ready, self.sources = copy.deepcopy(ready), dict(stored['source_sha256'])
                self.calls, self.closed = 0, False
                owner = self
                self.proc = type('NoWorker', (), {'poll': lambda self: 0 if owner.closed else None})()
                actual_config = read(self.config)
                events.append(dict(kind='original_live_constructor_received_input',
                    file=actual_config['initialCheckpoint'], sha256=sha(actual_config['initialCheckpoint']),
                    Node_started=False))

            def solve(self, height, jacobian=True, audit=False):
                h = np.asarray(height, np.float64)
                if h.tobytes() != target.tobytes() or not jacobian or audit:
                    events.append(dict(kind='new_or_audited_request_delegated_without_returning_a_result',
                        audit=audit, exact_target_bits=h.tobytes() == target.tobytes()))
                    raise DelegationReached('No new numerical response is supplied')
                self.calls += 1
                row = dict(request=dict(height=h.tolist(), jacobian=True, audit=False),
                    response=completed['response'], source_sha256=self.sources,
                    config=read(self.config), protocol_replay_only=True,
                    original_completed_response=str(args.completed_target_packet),
                    original_completed_response_sha256=sha(args.completed_target_packet))
                out = self.record_prefix.with_name(self.record_prefix.name+f'_{self.calls:04d}.json.gz')
                out.write_bytes(gzip.compress(json.dumps(row).encode(), mtime=0))
                return completed['response']

            def close(self):
                self.closed = True

        Original = make_port_class(ExistingTargetReplay, args.packet, args.ready, args.source_topic,
            release_between_responses=False)
        Wrapped = make_first_warm_port_class(Original, args.warm, args.warm_report, args.primary, args.packet)
        port = Wrapped(config, args.source_topic/'repro/source-root', root/'matched')
        port.solve(saved_H, jacobian=True, audit=False)
        check('saved_H_replay_does_not_consume_or_start_first_live_warm',
              not port._first_live_warm_choice_done and not events and port.calls == 1)
        prior = port._last_checkpoint
        value = port.solve(target, jacobian=True, audit=False)
        info = port.provenance['explicit_unaccepted_first_live_Hermite_warm']
        check('matching_H_selected_only_before_first_live', info['selected'] and info['no_live_worker_before_choice'])
        check('actual_constructor_path_and_SHA_confirm_delivery',
              info['actual_original_constructor_delivery_observed']
              and events[0]['sha256'] == sha(args.warm)
              and Path(events[0]['file']).resolve() == args.warm.resolve())
        check('original_audited_cache_identity_preserved',
              port.saved_response == stored['response'] and np.array_equal(port.saved_height, saved_H))
        check('returned_value_is_only_preexisting_real_target_response', value == completed['response'])
        check('new_complete_packet_replaces_warm_as_last_checkpoint',
              port._last_checkpoint != args.warm and read(port._last_checkpoint)['response'] == completed['response'])
        port.solve(saved_H, jacobian=True, audit=True)
        later = port._last_checkpoint
        try:
            port.solve(target, jacobian=True, audit=True)
        except DelegationReached:
            pass
        else:
            raise AssertionError('An unaudited response answered a fresh audited request')
        check('later_same_H_never_reinstalls_old_Hermite_checkpoint',
              port._last_checkpoint == later and port._first_live_warm_choice_done
              and len([e for e in events if e['kind']=='original_live_constructor_received_input']) == 1)
        check('no_fabricated_audit_for_later_request', port.calls == 3)
        port.close()

        changed = target.copy()
        changed[0] = np.nextafter(changed[0], np.inf)
        fallback = Wrapped(config, args.source_topic/'repro/source-root', root/'different')
        before_count = len(events)
        try:
            fallback.solve(changed, jacobian=True, audit=False)
        except DelegationReached:
            pass
        else:
            raise AssertionError('A different H was supplied a fabricated target response')
        fallback_info = fallback.provenance['explicit_unaccepted_first_live_Hermite_warm']
        receipt = events[before_count]
        check('one_ULP_mismatch_does_not_select_Hermite',
              fallback_info['choice_observed'] and not fallback_info['selected']
              and not fallback_info['actual_original_constructor_delivery_observed'])
        check('one_ULP_mismatch_preserves_original_audited_checkpoint_input',
              Path(receipt['file']).resolve() == args.packet.resolve() and receipt['sha256'] == sha(args.packet))
        fallback.close()
    files = [Path(__file__), Path(__file__).with_name('strong_recorded_port_explicit_hermite_warm.py'),
             Path(__file__).with_name('strong_actual_recorded_tail_port.py'), args.primary, args.packet,
             args.ready, args.warm, args.warm_report, args.completed_target_packet]
    report = dict(scope=__doc__, passed=all(checks.values()), checks=checks,
        warm_preflight=warm_record, source_sha256={str(p): sha(p) for p in files}, replay_events=events,
        complete_target_H=target.tolist(), Node_processes_started=0, new_BVPs_solved=0,
        new_numerical_responses_fabricated=0, runtime_or_Newton_benefit_not_measured=True,
        temporary_protocol_packets_discarded=True, seconds=time.monotonic()-started)
    with args.out.open('x') as stream:
        json.dump(report, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(event='explicit_first_live_Hermite_replay_complete', passed=True,
        checks=len(checks), warm_preflight_checks=len(warm_record['all_identity_checks']),
        seconds=report['seconds'], Node_processes_started=0)), flush=True)


if __name__ == '__main__':
    main()
