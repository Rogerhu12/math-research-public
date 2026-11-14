#!/usr/bin/env python3
"""Replay a CLOSED M15 physical-height control history from actual packets.

No WeightedTailPort is constructed. No Node, root, flow, DN or BVP is called.
The reviewed Coordinator is replayed against the immutable recorded responses,
so target paths, subdivision, failure classification, budgets, flags, caches,
latest-good references and the entire journal must reproduce exactly.
"""
import copy
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def audit(context, last_call):
    h = module('m15_closed_original_control_replay', HERE/'78718-prefix-tail-linear-m15q512-v1.py')
    require = h.require
    policy = context['control_policy']
    policy_id = context['launch']['continuation_policy']
    h.verify(policy_id)
    require(h.canonical(h.read(policy_id['path'])) == h.canonical(policy), 'Closed policy differs from launch')
    out = context['out']
    require(type(last_call) is int and last_call > 0, 'No actual physical control calls')
    journal_path, good_path = Path(policy['journal_file']), Path(policy['last_good_file'])
    journal_id, good_id = h.identity(journal_path), h.identity(good_path)
    require(journal_id['bytes'] < 5_000_000 and good_id['bytes'] < 100_000,
            'Closed control metadata exceeds file limits')
    all_events = []
    with journal_path.open() as stream:
        for line in stream:
            event = json.loads(line)
            require(type(event) is dict and event.get('policy_sha256') == policy_id['sha256'] and
                    type(event.get('utc')) is str and bool(event['utc']), 'Invalid closed control journal identity')
            all_events.append({k:v for k,v in event.items() if k not in ('utc','policy_sha256')})
    require(all_events and all_events[0] == {
        'event':'control-start', 'scope':'Finite DN control only; prefix remains UNSOLVED.'},
        'Missing actual control constructor event')
    events = all_events[1:]
    require(events and not any(e.get('event') == 'terminal-failure' for e in events),
            'A terminated control history cannot close a successful candidate')
    files, packets, ids = [journal_id, good_id, policy_id], {}, {}
    actual_paths = sorted(out.parent.glob(out.name+'_tail_????.json.gz'))
    expected_paths = [Path(str(out)+f'_tail_{call:04d}.json.gz') for call in range(1,last_call+1)]
    require(actual_paths == expected_paths, 'Actual physical packet sequence has a gap or an unreported call')
    failures = 0
    for call, path in enumerate(expected_paths, 1):
        row, record = h.identity(path), h.read(path)
        require(row['bytes'] < 5_000_000 and type(record) is dict and
                set(record) == {'request','response','config','source_sha256'}, 'Invalid closed physical packet')
        require(h.canonical(record['config']) == h.canonical(context['config']) and
                h.canonical(record['source_sha256']) == h.canonical(policy['source_sha256']),
                'Closed packet lost its actual nine-source M15/N512 identity')
        req, response = record['request'], record['response']
        require(type(req) is dict and set(req) == {'height','jacobian','audit'} and
                h.vector(req['height'], 15) and type(req['jacobian']) is bool and type(req['audit']) is bool,
                'Invalid actual physical request/flags')
        require(type(response) is dict, 'Invalid actual response')
        if 'failed' in response:
            require(set(response) == {'failed','lastIteration','checkpoint'} and type(response['failed']) is str,
                    'Invalid original failure envelope')
            if response['checkpoint'] is not None:
                h.validate_checkpoint(response['checkpoint'], 15, context['expected_tail_parameters'])
                require(h.same_height(response['checkpoint']['cutHeight'], req['height']), 'Failed packet label changed')
            failures += 1
        else:
            h.validate_response(response, 15, context['expected_tail_parameters'], 2e-9,
                                req['jacobian'], req['audit'])
            require(h.same_height(response['checkpoint']['cutHeight'], req['height']), 'Normal packet label changed')
            failures += int(not response['converged'])
        files.append(row)
        packets[call], ids[call] = record, row
    trials = {call:[] for call in packets}
    trial_path = Path(context['config']['trialDiagnosticFile'])
    if trial_path.exists():
        row = h.identity(trial_path)
        require(row['bytes'] < 5_000_000, 'Closed trial log exceeds file limit')
        files.append(row)
        with trial_path.open() as stream:
            for line in stream:
                trial = json.loads(line)
                require(type(trial) is dict and type(trial.get('call')) is int and trial['call'] in packets,
                        'Trial log refers to an unrecorded physical call')
                trials[trial['call']].append(trial)
    # Partition the actual serialized external calls. The goal vector comes
    # from its actual terminal packet, and its exact digest/flags must equal
    # the begin and return records. No guessed success or initial state is used.
    groups, current = [], None
    for event in events:
        require(type(event.get('external_request')) is int and type(event.get('physical_calls')) is int,
                'Invalid control counters')
        if event['event'] == 'external-target-begin':
            require(current is None and event['external_request'] == len(groups)+1, 'Overlapping/misnumbered external requests')
            current = [event]
        else:
            require(current is not None and event['external_request'] == current[0]['external_request'],
                    'Event is outside its serialized external request')
            current.append(event)
        if event['event'] == 'external-target-return':
            groups.append(current)
            current = None
    require(current is None and groups, 'An external request has no real final return')

    class RecordedPort:
        def __init__(self):
            self.calls = 0
            self.cache_key = self.cache_value = None

        def solve(self, height, jacobian=True, audit=False):
            values = np.asarray(height, float)
            if self.cache_key is not None and h.same_height(values, self.cache_key) and not audit and (
                    not jacobian or self.cache_value.get('heightJetJacobian') is not None):
                return self.cache_value
            self.calls += 1
            require(self.calls in packets, 'Control replay requests an unrecorded actual call')
            packet = packets[self.calls]
            wanted = dict(height=values.tolist(), jacobian=bool(jacobian), audit=bool(audit))
            require(h.canonical(packet['request']) == h.canonical(wanted),
                    'Actual request is not the frozen control path/flags')
            response = packet['response']
            if response.get('failed') or not response.get('converged'):
                # The original base-client exception form. It is control
                # protocol replay, not a new numerical evaluation.
                raise FloatingPointError('Weighted finite DN trial failed '+str(
                    {key:response.get(key) for key in ('failed','residual','lastIteration')}))
            self.cache_key, self.cache_value = values.copy(), response
            return response

    actual_port = RecordedPort()
    reproduced, persisted = [], []

    def inspect(call, height, jacobian, audited, physical):
        record = packets[call]
        req = record['request']
        require(h.same_height(req['height'], height), 'Control replay read a different physical height')
        if physical:
            require(req['jacobian'] is jacobian and req['audit'] is audited, 'Actual physical flags changed')
        else:
            require(not audited and (not jacobian or req['jacobian']), 'A cache cannot provide requested flags')
        return record, ids[call]

    def classify(record, call):
        return h.classify_original_failure(record, call, trials[call], 36)

    control = h.Coordinator(actual_port, context['prior']['request']['height'], policy['control'],
                            inspect, classify, lambda e:reproduced.append(copy.deepcopy(e)),
                            lambda e:persisted.append(copy.deepcopy(e)))
    for group in groups:
        begin, end = group[0], group[-1]
        row = end['packet']
        h.verify(row)
        matching = [call for call, value in ids.items() if value == row]
        require(len(matching) == 1, 'External return references an unrelated actual packet')
        goal = packets[matching[0]]['request']['height']
        require(begin['goal_sha256'] == end['goal_sha256'] == h.digest(goal) and
                begin['jacobian'] is end['jacobian'] and begin['audit'] is end['audit'],
                'Actual external goal or requested flags changed')
        response = control.solve(goal, jacobian=begin['jacobian'], audit=begin['audit'])
        require(h.canonical(response) == h.canonical(packets[matching[0]]['response']),
                'Replay returned a different actual response')
    require(actual_port.calls == last_call and control.good['call'] == last_call and
            h.canonical(reproduced) == h.canonical(events), 'Complete control journal replay differs')
    require(persisted, 'No actual persisted successful packet')
    expected_good = dict(policy_sha256=policy_id['sha256'], **persisted[-1])
    require(h.canonical(h.read(good_path)) == h.canonical(expected_good), 'Final last-good reference differs from complete replay')
    for row in files:
        h.verify(row)
    return {'status':'PASS_COMPLETE_CLOSED_ACTUAL_CONTROL_REPLAY',
            'source':h.identity(__file__), 'adapter':h.identity(HERE/'78718-prefix-tail-linear-m15q512-v1.py'),
            'physical_packets':last_call, 'external_requests':len(groups),
            'closed_failed_requests':failures, 'journal_events':len(all_events),
            'exact_journal_replay':True, 'final_last_good_reproduced':True,
            'solver_calls':0, 'new_candidate_packets_created':0,
            'required_closed_files':sorted({r['path']:r for r in files}.values(), key=lambda r:r['path']),
            'scope':'Closed control/identity replay only; the actual finite response gates and full metric certification remain separate.'}
