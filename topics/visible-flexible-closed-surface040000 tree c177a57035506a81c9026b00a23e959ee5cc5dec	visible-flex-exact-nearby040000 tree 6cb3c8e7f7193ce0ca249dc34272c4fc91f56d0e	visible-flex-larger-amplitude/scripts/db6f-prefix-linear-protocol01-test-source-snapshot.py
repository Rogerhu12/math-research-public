#!/usr/bin/env python3
"""Isolated CONTROL-PROTOCOL tests. No port constructor, Node, root, flow or DN.

The stub uses one abstract scalar, deliberately lacks every actual finite-DN
schema, and only stores records in memory. It cannot be a positive candidate
fixture. A separate metadata check reads the already closed real first packet.
"""
import argparse
import ast
import copy
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
CLIENT = HERE / 'db6f-prefix-tail-linear-continuation-client.py'
spec = importlib.util.spec_from_file_location('db6f_linear_control_protocol_under_test', CLIENT)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)  # Definitions only. WeightedTailPort is never instantiated.


class AbstractPort:
    def __init__(self, actions=None):
        self.calls = 0
        self.cache_key = self.cache_value = None
        self.worker_good = None
        self.actions = actions or {}
        self.records = {}
        self.requests = []

    def solve(self, height, jacobian=True, audit=False):
        h = np.asarray(height, float).copy()
        if self.cache_key is not None and c.same_height(h, self.cache_key) and not audit and (
                not jacobian or self.cache_value['heightJetJacobian'] is not None):
            return self.cache_value
        self.calls += 1
        action = self.actions.get(self.calls, 'success')
        self.requests.append({'call': self.calls, 'height': h.tolist(), 'jacobian': jacobian,
                              'audit': audit, 'started_from': copy.deepcopy(self.worker_good), 'action': action})
        request = {'height': h.tolist(), 'jacobian': jacobian, 'audit': audit}
        if action in ('numerical', 'unknown', 'partial-record'):
            self.records[self.calls] = {'protocol_only': True, 'request': request,
                                        'response': {'failed': action, 'lastIteration': None, 'checkpoint': None}}
            if action == 'partial-record':
                self.records[self.calls] = None
            raise RuntimeError('ABSTRACT_PROTOCOL_' + action)
        response = {'protocol_only': True, 'converged': True, 'residual': 0.0,
                    'heightJetJacobian': [0.0] if jacobian else None,
                    'audit': {'protocol_only': True} if audit else None}
        self.worker_good = h.tolist()
        self.cache_key, self.cache_value = h.copy(), response
        self.records[self.calls] = {'protocol_only': True, 'request': request, 'response': response}
        if action == 'io-after-worker-update':
            raise OSError('ABSTRACT_ENOSPC_AFTER_UPDATE')
        return response


def setup(actions=None, control=None, journal_fail=None, persist_fail=False, seed=1.0):
    port = AbstractPort(actions)
    events, persisted = [], []

    def inspect(call, h, jac, audit, physical):
        record = port.records[call]
        if record is None:
            raise OSError('ABSTRACT_PARTIAL_GZIP')
        assert record['protocol_only'] is True and c.same_height(record['request']['height'], h)
        if physical:
            assert record['request']['jacobian'] is jac and record['request']['audit'] is audit
        packet = {'path': 'PROTOCOL_STUB_NOT_A_FILE:call' + str(call), 'bytes': 0,
                  'sha256': c.digest(record)}
        return record, packet

    def classify(record, call):
        if record['response'].get('failed') == 'numerical':
            return {'kind': 'ABSTRACT_KNOWN_NUMERICAL_FAILURE'}
        return None

    def journal(event):
        if event['event'] == journal_fail:
            raise OSError('ABSTRACT_JOURNAL_ENOSPC')
        events.append(copy.deepcopy(event))

    def persist(record):
        if persist_fail:
            raise OSError('ABSTRACT_LAST_GOOD_REFERENCE_ENOSPC')
        persisted.append(copy.deepcopy(record))

    policy = dict(c.CONTROL)
    if control:
        policy.update(control)  # Test-only smaller budgets; production forbids this.
    coordinator = c.Coordinator(port, [seed], policy, inspect, classify, journal, persist)
    return coordinator, port, events, persisted


def expect_terminal(coordinator, port, target=2.0, jac=True, audit=False):
    try:
        coordinator.solve([target], jacobian=jac, audit=audit)
    except c.ContinuationFailure:
        pass
    else:
        raise AssertionError('Protocol case incorrectly returned success')
    assert coordinator.state == 'TERMINAL_FAILURE'
    calls = port.calls
    try:
        coordinator.solve([target], jacobian=False, audit=False)
    except c.ContinuationFailure:
        pass
    else:
        raise AssertionError('Terminated object served a cache response')
    assert port.calls == calls


def tests():
    results = []

    x, p, events, saved = setup({2: 'numerical'})
    r = x.solve([2.0], jacobian=True, audit=False)
    assert r['protocol_only'] and x.good['call'] == p.calls
    assert p.requests[1]['height'] == [1.125]
    assert p.requests[2]['height'] == [1.0625] and p.requests[2]['started_from'] == [1.0]
    assert saved[0]['call'] == 1 and saved[1]['call'] == 3
    assert p.requests[-1]['height'] == [2.0] and p.requests[-1]['jacobian'] is True
    assert all(not q['jacobian'] and not q['audit'] for q in p.requests[:-1])
    assert any(e['event'] == 'halve-from-last-good' for e in events)
    results.append({'case': 'known_failure_rolls_back_and_calls_stays_physical', 'pass': True, 'stub_calls': p.calls})

    for label in ('unknown', 'partial-record', 'io-after-worker-update'):
        x, p, events, saved = setup({2: label})
        expect_terminal(x, p)
        assert p.calls == 2 and x.good['call'] == 1
        results.append({'case': label + '_is_terminal_without_old_cache_return', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup({1: 'numerical'})
    expect_terminal(x, p)
    assert p.calls == 1 and x.good is None
    results.append({'case': 'bootstrap_requires_a_real_new_success', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup(control={'maximum_physical_requests': 4})
    expect_terminal(x, p)
    assert p.calls == 3 and c.same_height(x.good['height'], [1.25])
    results.append({'case': 'budget_reserves_validation_and_never_returns_intermediate', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup({i: 'numerical' for i in range(2, 20)})
    expect_terminal(x, p)
    assert p.calls == 9 and x.good['call'] == 1
    results.append({'case': 'minimum_step_exhaustion_is_terminal', 'pass': True, 'stub_calls': p.calls})

    goal = np.array([np.nextafter(1.0, 2.0)])
    original_bits = goal.tobytes()
    x, p, events, saved = setup()
    x.solve(goal, jacobian=True, audit=True)
    assert goal.tobytes() == original_bits
    assert p.calls == 3 and p.requests[-1]['height'] == goal.tolist()
    assert p.requests[-1]['jacobian'] is True and p.requests[-1]['audit'] is True
    logical = [e for e in events if e['event'] == 'same-floating-height-logical-move']
    assert logical and all(e['no_new_physical_request'] and e['no_new_mathematical_success'] for e in logical)
    assert x.good['call'] == p.calls
    before = p.calls
    x.solve(goal.copy(), jacobian=False, audit=False)
    assert p.calls == before and x.good['call'] == before
    results.append({'case': 'one_ulp_exact_goal_flags_and_same_packet_cache', 'pass': True, 'stub_calls': p.calls,
                    'logical_duplicate_moves': len(logical)})

    x, p, events, saved = setup(control={'maximum_logical_moves': 1})
    expect_terminal(x, p, target=float(goal[0]))
    assert p.calls == 1
    results.append({'case': 'logical_grid_budget_is_finite', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup({10: 'numerical'})
    expect_terminal(x, p, jac=True, audit=True)
    assert p.calls == 10 and x.good['call'] == 9 and x.good['height'] == [2.0]
    assert p.requests[-1]['jacobian'] is True and p.requests[-1]['audit'] is True
    results.append({'case': 'final_requested_postprocess_failure_is_not_target_success', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup(journal_fail='actual-success')
    expect_terminal(x, p)
    assert p.calls == 1 and len(saved) == 1
    results.append({'case': 'journal_failure_after_real_return_cannot_return_success', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup(persist_fail=True)
    expect_terminal(x, p)
    assert p.calls == 1 and x.good is None
    results.append({'case': 'atomic_reference_failure_is_terminal', 'pass': True, 'stub_calls': p.calls})

    x, p, events, saved = setup()
    x.solve([1.0], jacobian=True, audit=False)
    p.calls += 1  # Explicit protocol fault: pointer leads cached success.
    expect_terminal(x, p, target=1.0)
    assert p.calls == 2 and x.good['call'] == 1
    results.append({'case': 'stale_cache_packet_counter_is_rejected', 'pass': True, 'stub_calls': p.calls})

    # Classifier tests are abstract failure records, not actual candidate data.
    req = {'height': [1.0], 'jacobian': False, 'audit': False}
    early = {'request': req, 'response': {'failed': 'Error: momentum Newton line search failed',
                                        'lastIteration': None, 'checkpoint': None}}
    assert c.classify_original_failure(early, 1, [])['kind'] == 'known-momentum-before-first-progress'
    for key in ('lastIteration', 'checkpoint'):
        bad = copy.deepcopy(early)
        del bad['response'][key]
        assert c.classify_original_failure(bad, 1, []) is None
    bad = copy.deepcopy(early)
    bad['response']['lastIteration'] = {'iteration': 0, 'norm': 1.0}
    assert c.classify_original_failure(bad, 1, []) is None
    bad = copy.deepcopy(early)
    bad['request']['jacobian'] = True
    assert c.classify_original_failure(bad, 1, []) is None
    rows = [{'call': 1, 'iteration': 1, 'trial': k, 'step': 2.0 ** (-k), 'baseNorm': 2.0,
             'kind': 'momentum-root-solver-rejection', 'error': 'Error: momentum Newton line search failed'}
            for k in range(10)]
    aggregate = {'request': req, 'response': {'failed': 'Error: multiple-shooting line search failed at 2',
                    'lastIteration': {'iteration': 1, 'norm': 2.0}, 'checkpoint': {'protocol_only': True}}}
    assert c.classify_original_failure(aggregate, 1, rows)['trial_rows'] == 10
    unknown = {'call': 1, 'iteration': 0, 'trial': 0, 'step': 1.0, 'baseNorm': 3.0,
               'kind': 'other-evaluation-rejection', 'error': 'ABSTRACT_ENOSPC'}
    assert c.classify_original_failure(aggregate, 1, [unknown] + rows) is None
    assert c.classify_original_failure(aggregate, 1, rows[:-1]) is None
    bad_rows = copy.deepcopy(rows)
    bad_rows[0]['step'] = True
    assert c.classify_original_failure(aggregate, 1, bad_rows) is None
    results.append({'case': 'strict_failure_stage_and_all_closed_trial_classification', 'pass': True})

    # Use only the real closed first packet to check actual schema compatibility;
    # invalid copies remain in memory and cannot be future positive outputs.
    topic = HERE.parent
    real = c.read(topic / 'notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01_tail_0001.json.gz')
    params = real['response']['checkpoint']['parameters']
    c.validate_response(real['response'], 15, params, 2e-9, True, False)
    bad_cases = []
    for bad_value in (None, True, '1'):
        obj = copy.deepcopy(real['response'])
        obj['jets']['height'][0] = bad_value
        bad_cases.append(obj)
    obj = copy.deepcopy(real['response'])
    obj['checkpoint']['rawNode'][0] = False
    bad_cases.append(obj)
    obj = copy.deepcopy(real['response'])
    obj['heightJetJacobian'].pop()
    bad_cases.append(obj)
    for obj in bad_cases:
        try:
            c.validate_response(obj, 15, params, 2e-9, True, False)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid numeric schema accepted')
    results.append({'case': 'closed_real_schema_compatible_and_five_invalid_numeric_copies_rejected', 'pass': True,
                    'actual_new_DN_calls': 0})
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    require_new = a.out.resolve()
    assert require_new.parent.is_dir() and not require_new.exists()
    for name in ('db6f-prefix-tail-linear-continuation-client.py', 'db6f-prefix-flat-linear-continuation-coupled.py',
                 'db6f-prefix-prepare-linear-dn-pilot.py', Path(__file__).name):
        ast.parse((HERE / name).read_text(), filename=name)
    rows = tests()
    report = {'status': 'PASS_ISOLATED_CONTROL_PROTOCOL_ONLY', 'scope': __doc__,
              'source': c.identity(CLIENT), 'test_source': c.identity(Path(__file__)),
              'tests': rows, 'test_count': len(rows), 'actual_port_constructions': 0,
              'actual_node_root_flow_DN_BVP_calls': 0, 'new_candidate_packets': 0,
              'real_closed_metadata_source': c.identity(HERE.parent / 'notes/2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01_tail_0001.json.gz')}
    with require_new.open('x') as f:
        f.write(json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + '\n')
    print(json.dumps({'status': report['status'], 'test_count': len(rows), **c.identity(require_new)}))


if __name__ == '__main__':
    main()
