#!/usr/bin/env python3
"""New M15/N512 identity for the frozen bounded physical-height DN control.

No worker, root, RK, Newton, boundary equation or tolerance is changed.
Importing this file performs no DN.  The private Coordinator is separately
testable with a protocol stub; such tests are not numerical solver evidence.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
import sys
import time
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
IO_KEYS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
           'trialDiagnosticFile', 'trialStatePrefix'}
ORIGINAL_NAMES = ['db6f-prefix-tail-trial-client.py', 'db6f-prefix-tail-trial-worker.mjs',
                  'db6f-prefix-tail-trial-core.mjs', 'db6f-prefix-tail-trial-split.mjs',
                  '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
                  'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs']
JET_SCALARS = {'radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep',
               'meanSlope', 'meanSecond', 'meanSlopeCorrection', 'meanSecondCorrection',
               'minLeading', 'minD', 'endpointFullD', 'endpointPhi', 'formalCurvature'}
JET_VECTORS = {'height', 'slope', 'second'}
AUDIT_KEYS = {'fullD', 'normalizedFullDefect', 'minLeading', 'minD',
              'formalCurvature', 'maxPhysicalPV', 'actualMetric', 'holonomy'}
KNOWN_MOMENTUM_ERRORS = {
    'Error: momentum branch D/S/A rejected',
    'Error: momentum Newton matrix not SPD',
    'Error: momentum Newton line search failed',
    'Error: momentum Newton iteration limit',
}
CONTROL = {'initial_step': '1/8', 'maximum_step': '1/8', 'minimum_step': '1/1024',
           'maximum_physical_requests': 32, 'maximum_logical_moves': 1024,
           'grow_after_success': False}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def identity(path):
    p = Path(path).resolve()
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': h.hexdigest()}


def verify(row):
    got = identity(row['path'])
    require(got == row, 'Bound file changed: ' + row['path'])
    return got


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def number(x):
    return type(x) in (int, float) and math.isfinite(x)


def vector(x, n):
    return isinstance(x, list) and len(x) == n and all(number(v) for v in x)


def int_value(x):
    return type(x) is int


def same_height(a, b):
    return np.array_equal(np.asarray(a, dtype=float), np.asarray(b, dtype=float))


def without_io(obj):
    return {k: v for k, v in obj.items() if k not in IO_KEYS}


def validate_checkpoint(cp, M, parameters):
    require(isinstance(cp, dict) and set(cp) == {
        'parameters', 'states', 'rawNode', 'rawStates', 'cutHeight', 'scope'}, 'Wrong actual CP schema')
    require(canonical(cp['parameters']) == canonical(parameters), 'Runtime parameter identity changed')
    n = parameters['depth']
    depth = parameters['physicalDepth']
    require(int_value(n) and int_value(depth), 'Invalid physical/stage counts')
    require(isinstance(cp['states'], list) and len(cp['states']) == n + 1
            and all(vector(v, 2 * M) for v in cp['states']), 'Nonfinite shooting state')
    rn, rs = cp['rawNode'], cp['rawStates']
    require(isinstance(rn, list) and len(rn) == depth + 1 and all(int_value(x) for x in rn)
            and rn[0] == 0 and rn[-1] == n and all(x < y for x, y in zip(rn, rn[1:])),
            'Invalid raw-node mapping')
    require(isinstance(rs, list) and len(rs) == len(rn)
            and all(vector(row, 2 * M) for row in rs)
            and all(row == cp['states'][index] for index, row in zip(rn, rs)), 'Invalid raw-state mirror')
    require(vector(cp['cutHeight'], M) and isinstance(cp['scope'], str), 'Invalid cut-height CP label')


def validate_response(response, M, parameters, tolerance, requested_jac, requested_audit):
    """Original finite response schema; no added geometric/curvature threshold."""
    require(isinstance(response, dict) and set(response) == {
        'converged', 'residual', 'jets', 'heightJetJacobian', 'history', 'audit', 'checkpoint'},
        'Wrong original normal response schema')
    require(type(response['converged']) is bool and number(response['residual'])
            and response['residual'] >= 0, 'Invalid convergence/residual fields')
    require(response['converged'] == (response['residual'] < tolerance),
            'Convergence flag disagrees with the original tolerance')
    jets = response['jets']
    require(isinstance(jets, dict) and set(jets) == JET_SCALARS | JET_VECTORS,
            'Wrong complete cut-jets schema')
    require(all(number(jets[k]) for k in JET_SCALARS)
            and all(vector(jets[k], M) for k in JET_VECTORS), 'Nonfinite cut jets')
    jac = response['heightJetJacobian']
    require(jac is None or vector(jac, (3 * M + 2) * M), 'Invalid actual DN Jacobian')
    require(not requested_jac or jac is not None, 'Missing requested actual DN Jacobian')
    audit = response['audit']
    require(audit is None or (isinstance(audit, dict) and set(audit) == AUDIT_KEYS
                            and all(number(v) for v in audit.values())), 'Invalid original audit')
    require(not requested_audit or audit is not None, 'Missing requested original audit')
    history = response['history']
    require(isinstance(history, list) and 0 < len(history) <= 36, 'Invalid actual history length')
    for i, row in enumerate(history):
        require(isinstance(row, dict) and {'iteration', 'norm', 'minA', 'minD'} <= set(row)
                and set(row) <= {'iteration', 'norm', 'minA', 'minD', 'chartCondition', 'step'},
                'Unexpected original history schema')
        require(int_value(row['iteration']) and row['iteration'] == i
                and all(number(v) for k, v in row.items() if k != 'iteration'), 'Nonfinite history')
    # The final reevaluation residual need not equal the last saved base norm.
    validate_checkpoint(response['checkpoint'], M, parameters)


class ContinuationFailure(RuntimeError):
    pass


class NumericalSubdivision(Exception):
    def __init__(self, proof):
        super().__init__(proof['kind'])
        self.proof = proof


class Coordinator:
    """Control only. Port/record/journal hooks permit isolated protocol tests."""
    def __init__(self, port, seed_height, policy, inspect_packet, classify_failure,
                 journal, persist_good):
        self.port = port
        self.seed_height = np.asarray(seed_height, float).copy()
        self.policy = policy
        self.inspect_packet = inspect_packet
        self.classify_failure = classify_failure
        self.journal = journal
        self.persist_good = persist_good
        self.good = None
        self.state = 'UNSEEDED'
        self.external_id = 0
        self.start_calls = port.calls
        self.logical_moves = 0

    def emit(self, event, **row):
        self.journal({'event': event, 'external_request': self.external_id,
                      'state': self.state, 'physical_calls': self.port.calls, **row})

    def _budget_used(self):
        return self.port.calls - self.start_calls

    def _cache_consistent(self):
        require(self.good is not None and same_height(self.port.cache_key, self.good['height'])
                and digest(self.port.cache_value) == self.good['response_digest'],
                'Original successful cache changed after a failed call')

    def _call(self, height, jacobian, audit, phase):
        h = np.asarray(height, float).copy()
        before = self.port.calls
        cache_expected = (self.port.cache_key is not None and same_height(h, self.port.cache_key)
                          and not audit and (not jacobian or self.port.cache_value.get('heightJetJacobian') is not None))
        if cache_expected:
            require(self.good is not None and before == self.good['call'],
                    'Cache points behind a failed physical packet')
        else:
            require(self._budget_used() < self.policy['maximum_physical_requests'],
                    'Physical request budget exhausted')
        self.emit('physical-request-or-cache', phase=phase, height_sha256=digest(h.tolist()),
                  jacobian=jacobian, audit=audit, cache_expected=cache_expected)
        try:
            response = self.port.solve(h.copy(), jacobian=jacobian, audit=audit)
        except Exception as exc:
            if self.port.calls != before + 1:
                raise ContinuationFailure('Unrecorded/unknown base-client failure: ' + repr(exc)) from exc
            # A missing/partial gzip or record I/O failure is fatal. The original
            # base writes before raising a numerical failure, but not atomically.
            record, packet = self.inspect_packet(self.port.calls, h, jacobian, audit, True)
            proof = self.classify_failure(record, self.port.calls) if phase == 'TRACK' else None
            if proof is None:
                raise ContinuationFailure('Non-subdividable original failure: ' + repr(exc)) from exc
            self._cache_consistent()
            self.emit('closed-numerical-failure', phase=phase, packet=packet, classification=proof)
            raise NumericalSubdivision({'packet': packet, **proof}) from exc
        physical = self.port.calls == before + 1
        require(physical or self.port.calls == before, 'Unexpected physical-call counter change')
        record, packet = self.inspect_packet(self.port.calls, h, jacobian, audit, physical)
        require(record['response']['converged'] is True, 'Normal return was not converged')
        require(canonical(record['response']) == canonical(response), 'Returned response differs from saved packet')
        if not physical:
            require(cache_expected and self.good is not None and self.good['call'] == self.port.calls,
                    'Unexpected or stale cache return')
        return response, packet, physical

    def _accept(self, height, response, packet, physical):
        require(self.port.calls > 0, 'Success without any actual original packet')
        require(same_height(self.port.cache_key, height)
                and digest(self.port.cache_value) == digest(response), 'Success cache identity mismatch')
        good = {'call': self.port.calls, 'height': np.asarray(height, float).tolist(),
                'packet': packet, 'response_digest': digest(response)}
        if physical:
            self.persist_good({'status': 'ACTUAL_FINITE_DN_LAST_GOOD_ONLY',
                               'scope': 'Warm response for exact saved physical request; not prefix/closed-surface success.',
                               'external_request': self.external_id, **good})
        self.good = good
        self.emit('actual-success' if physical else 'same-packet-cache-return', packet=packet)

    def _return(self, goal, response, jacobian, audit):
        require(self.good is not None and self.good['call'] == self.port.calls
                and same_height(self.good['height'], goal), 'Final latest-packet/goal invariant failed')
        self._cache_consistent()
        self.state = 'GOOD'
        self.emit('external-target-return', goal_sha256=digest(goal.tolist()),
                  jacobian=jacobian, audit=audit, packet=self.good['packet'],
                  physical_requests_used=self._budget_used(), logical_moves=self.logical_moves)
        return response

    def solve(self, height, jacobian=True, audit=False):
        if self.state == 'TERMINAL_FAILURE':
            raise ContinuationFailure('This coordinator has terminated; use a new bound run for recovery')
        try:
            require(type(jacobian) is bool and type(audit) is bool, 'Flags must be literal booleans')
            require(np.asarray(height).dtype.kind in 'fiu', 'Physical target cannot contain bool/string/object values')
            goal = np.asarray(height, float).copy()
            require(goal.shape == self.seed_height.shape and np.all(np.isfinite(goal)), 'Invalid physical target')
            self.external_id += 1
            self.start_calls = self.port.calls
            self.logical_moves = 0
            self.emit('external-target-begin', goal_sha256=digest(goal.tolist()), jacobian=jacobian, audit=audit)
            if self.good is None:
                self.state = 'UNSEEDED'
                if same_height(goal, self.seed_height):
                    response, packet, actual = self._call(goal.copy(), jacobian, audit, 'BOOTSTRAP')
                    self._accept(goal, response, packet, actual)
                    return self._return(goal, response, jacobian, audit)
                response, packet, actual = self._call(self.seed_height.copy(), False, False, 'BOOTSTRAP')
                self._accept(self.seed_height, response, packet, actual)
            origin = np.asarray(self.good['height'], float).copy()
            tau, step = Fraction(0), Fraction(self.policy['initial_step'])
            minimum = Fraction(self.policy['minimum_step'])
            while not same_height(self.good['height'], goal):
                self.state = 'TRACK'
                next_tau = min(Fraction(1), tau + step)
                require(next_tau > tau, 'No logical parameter progress')
                h = goal.copy() if next_tau == 1 else origin + float(next_tau) * (goal - origin)
                if same_height(h, goal):
                    h, next_tau = goal.copy(), Fraction(1)
                if same_height(h, self.good['height']):
                    tau = next_tau
                    self.logical_moves += 1
                    require(self.logical_moves <= self.policy['maximum_logical_moves'], 'Logical move budget exhausted')
                    self.emit('same-floating-height-logical-move', tau=str(tau),
                              no_new_physical_request=True, no_new_mathematical_success=True,
                              last_good_packet=self.good['packet'])
                    continue
                require(self._budget_used() < self.policy['maximum_physical_requests'] - 1,
                        'Physical request budget must reserve final requested validation')
                self.emit('tracking-target', tau=str(next_tau), step=str(step), origin_sha256=digest(origin.tolist()),
                          goal_sha256=digest(goal.tolist()), last_good_packet=self.good['packet'])
                try:
                    response, packet, actual = self._call(h, False, False, 'TRACK')
                except NumericalSubdivision as exc:
                    step /= 2
                    self.emit('halve-from-last-good', tau_good=str(tau), new_step=str(step),
                              last_good_packet=self.good['packet'], rejected_packet=exc.proof['packet'])
                    require(step >= minimum, 'Minimum continuation increment reached')
                    continue
                self._accept(h, response, packet, actual)
                tau = next_tau
                self.logical_moves += 1
                require(self.logical_moves <= self.policy['maximum_logical_moves'], 'Logical move budget exhausted')
            self.state = 'VALIDATE'
            # The unmodified base handles its exact cache rule. audit=True
            # always performs a physical request; any failure here is terminal.
            response, packet, actual = self._call(goal.copy(), jacobian, audit, 'VALIDATE')
            self._accept(goal, response, packet, actual)
            return self._return(goal, response, jacobian, audit)
        except Exception as exc:
            self.state = 'TERMINAL_FAILURE'
            try:
                self.emit('terminal-failure', error=repr(exc), last_good=self.good,
                          physical_requests_used=self._budget_used())
            except Exception:
                pass  # Never turn journal failure into normal success.
            if isinstance(exc, ContinuationFailure):
                raise
            raise ContinuationFailure(str(exc)) from exc


def complete_trial_groups(rows, group_count, *, failed_last=False, last_norm=None, history=None):
    """Certify the original serial append structure, without reading a live trace.

    Every completed Newton iteration starts at trial 0. Earlier groups end
    with their unique accepted row; an aggregate failure ends in ten rejects.
    State-only trial norms need not equal the next full-Jacobian base norm.
    """
    cursor = 0
    for iteration in range(group_count):
        start = cursor
        while cursor < len(rows) and rows[cursor]['iteration'] == iteration:
            cursor += 1
        group = rows[start:cursor]
        if not group or [row['trial'] for row in group] != list(range(len(group))):
            return False
        base = group[0]['baseNorm']
        if any(row['baseNorm'] != base for row in group):
            return False
        if failed_last and iteration == group_count - 1:
            if len(group) != 10 or base != last_norm or any(row['kind'] == 'accepted' for row in group):
                return False
        else:
            if group[-1]['kind'] != 'accepted' or any(row['kind'] == 'accepted' for row in group[:-1]):
                return False
            if history is not None:
                saved = history[iteration]
                if base != saved['norm'] or group[-1]['step'] != saved['step']:
                    return False
    return cursor == len(rows)


def classify_original_failure(record, call, trial_rows, max_iterations=36):
    """Conservative closed-packet classification, not a new numerical solver."""
    r, request = record['response'], record['request']
    if request['jacobian'] is not False or request['audit'] is not False:
        return None
    if not int_value(max_iterations) or max_iterations != 36 or not isinstance(trial_rows, list):
        return None
    # Recognize EVERY row before checking complete groups. An unknown earlier
    # error, a missing whole group, a missing trial or a reordered row is fatal.
    for row in trial_rows:
        if not isinstance(row, dict) or not int_value(row.get('call')) or row['call'] != call or not int_value(row.get('iteration')) or not int_value(row.get('trial')):
            return None
        if not (0 <= row['iteration'] < max_iterations and 0 <= row['trial'] < 10):
            return None
        if not number(row.get('step')) or row['step'] != 2.0 ** (-row['trial']) or not number(row.get('baseNorm')) or row['baseNorm'] < 0:
            return None
        kind = row.get('kind')
        if kind in ('momentum-guard-rejection', 'momentum-root-solver-rejection'):
            if row.get('error') not in KNOWN_MOMENTUM_ERRORS:
                return None
        elif kind in ('accepted', 'residual-not-decreasing'):
            if not number(row.get('trialNorm')) or row['trialNorm'] < 0:
                return None
            if (row['trialNorm'] < row['baseNorm']) != (kind == 'accepted'):
                return None
        else:
            return None
    if 'failed' not in r:
        if r.get('converged') is not False:
            return None
        history = r.get('history')
        # A normal false return cannot take the early converged break. The
        # original fixed 36-iteration loop therefore accepted a step at EVERY
        # saved base, including iteration 35. The final residual is evaluated
        # afterwards and is deliberately not equated with history[-1].norm.
        if not isinstance(history, list) or len(history) != max_iterations:
            return None
        for iteration, saved in enumerate(history):
            if (not isinstance(saved, dict) or not int_value(saved.get('iteration'))
                    or saved['iteration'] != iteration or not number(saved.get('norm'))
                    or saved['norm'] < 0 or not number(saved.get('step'))):
                return None
        if not complete_trial_groups(trial_rows, max_iterations, history=history):
            return None
        return {'kind': 'original-complete-nonconvergence', 'iteration_groups': max_iterations,
                'trial_rows': len(trial_rows), 'closed_call_trial_rows_sha256': digest(trial_rows)}
    if set(r) != {'failed', 'lastIteration', 'checkpoint'}:
        return None
    if r['lastIteration'] is None and r['checkpoint'] is None:
        if r['failed'] in KNOWN_MOMENTUM_ERRORS and not trial_rows:
            return {'kind': 'known-momentum-before-first-progress'}
        return None
    last = r['lastIteration']
    if (not isinstance(last, dict) or not int_value(last.get('iteration'))
            or not 0 <= last['iteration'] < max_iterations or not number(last.get('norm'))):
        return None
    prefix = 'Error: multiple-shooting line search failed at '
    if not isinstance(r['failed'], str) or not r['failed'].startswith(prefix):
        return None  # Same-named cutRaw/cutJets/Jac/audit errors are not localized.
    try:
        if float(r['failed'][len(prefix):]) != last['norm']:
            return None
    except ValueError:
        return None
    if not complete_trial_groups(trial_rows, last['iteration'] + 1,
                                 failed_last=True, last_norm=last['norm']):
        return None
    return {'kind': 'closed-known-numerical-ten-trial-rejection', 'trial_rows': len(trial_rows),
            'iteration_groups': last['iteration'] + 1,
            'closed_call_trial_rows_sha256': digest(trial_rows)}


class WeightedTailPort:
    """Original public coupled-client interface, with honest nine-source records."""
    def __init__(self, config, source_root, record_prefix, node_heap=1536):
        self.config, self.record_prefix = Path(config).resolve(), Path(record_prefix).resolve()
        self.source_root = Path(source_root).resolve()
        self.policy_path = self.record_prefix.with_name(self.record_prefix.name + '-continuation-policy.json')
        self.policy = read(self.policy_path)
        require(self.policy['schema'] == '78718-m15q512-physical-height-continuation-v1', 'Unsupported control policy')
        require(self.policy['record_prefix'] == str(self.record_prefix)
                and self.policy['source_root'] == str(self.source_root), 'Policy path mismatch')
        verify(self.policy['config'])
        require(self.policy['config']['path'] == str(self.config), 'Wrong policy config')
        for row in self.policy['bindings']:
            verify(row)
        self.cfg = read(self.config)
        self.parameters = None
        for key, value in {'modes': 15, 'spacing': 3, 'depth': 12, 'shootingParts': 8,
                           'steps': 32, 'quadrature': 512, 'maxIterations': 36,
                           'solveTolerance': 2e-9, 'auditSteps': 32}.items():
            require(canonical(self.cfg[key]) == canonical(value), 'Original numerical config changed: ' + key)
        require(self.cfg.get('projectionFloor', .05) == .05
                and self.cfg.get('correctInitialBoundary', True) is True, 'Original branch/warm policy changed')
        control = self.policy['control']
        require(canonical(control) == canonical(CONTROL), 'Unreviewed or mistyped continuation work budget')
        verify(self.policy['bootstrap_packet'])
        self.seed = read(self.policy['bootstrap_packet']['path'])
        require(self.cfg['initialCheckpoint'] == self.policy['bootstrap_packet']['path'], 'Bootstrap/load identity mismatch')
        require(self.seed['config']['quadrature'] == 256 and self.cfg['quadrature'] == 512,
                'Only the declared old-N256 to new-N512 warm transition is allowed')
        require(canonical(dict(without_io(self.seed['config']), quadrature=512)) == canonical(without_io(self.cfg)),
                'Bootstrap differs beyond five I/O keys and declared angular quadrature')
        M = self.cfg['modes']
        seed_parameters = self.seed['response']['checkpoint']['parameters']
        validate_response(self.seed['response'], M, seed_parameters, self.cfg['solveTolerance'], True, False)
        require(self.seed['response']['converged'] is True, 'Bootstrap file is not a true successful response')
        self.seed_height = self.seed['request']['height']
        require(vector(self.seed_height, M)
                and same_height(self.seed_height, self.seed['response']['checkpoint']['cutHeight']), 'Wrong seed cut-height label')
        require(set(self.policy['source_sha256']) == set(ORIGINAL_NAMES + [Path(__file__).name]),
                'The nine real source identities are required')
        for name, sha in self.policy['source_sha256'].items():
            require(identity(HERE / name)['sha256'] == sha, 'Source changed: ' + name)
        require(canonical(self.seed['source_sha256']) == canonical({n: self.policy['source_sha256'][n] for n in ORIGINAL_NAMES}),
                'Bootstrap eight-source identity mismatch')
        runtime_paths = [self.policy['journal_file'], self.policy['last_good_file'],
                         self.cfg['traceFile'], self.cfg['iterationCheckpointFile'], self.cfg['trialDiagnosticFile']]
        require(len(set(runtime_paths)) == len(runtime_paths), 'Runtime output collision')
        require(all(not Path(p).exists() for p in runtime_paths), 'Runtime output already used')
        require(not list(self.record_prefix.parent.glob(self.record_prefix.name + '_????.json.gz')),
                'Physical record prefix already used')
        require(not list(Path(self.cfg['trialStatePrefix']).parent.glob(Path(self.cfg['trialStatePrefix']).name + '-call*.json.gz')),
                'Trial-state prefix already used')
        self.policy_sha256 = identity(self.policy_path)['sha256']
        self._journal = Path(self.policy['journal_file']).open('x', buffering=1)
        self.base = None
        self.coordinator = None
        try:
            self._emit({'event': 'control-start', 'scope': 'Finite DN control only; prefix remains UNSOLVED.'})
            spec = importlib.util.spec_from_file_location('db6f_frozen_trial_base', HERE / ORIGINAL_NAMES[0])
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            # Retain the partially constructed object so startup failure can
            # close its real subprocess; the original __init__ itself is intact.
            self.base = mod.WeightedTailPort.__new__(mod.WeightedTailPort)
            mod.WeightedTailPort.__init__(self.base, self.config, self.source_root, self.record_prefix, node_heap)
            require(canonical(self.base.sources) == canonical({n: self.policy['source_sha256'][n] for n in ORIGINAL_NAMES}),
                    'Original base source collection changed')
            self.base.sources[Path(__file__).name] = self.policy['source_sha256'][Path(__file__).name]
            self.parameters = self.base.ready['parameters']
            require(seed_parameters['quadrature'] == 256 and self.parameters['quadrature'] == 512,
                    'Wrong old/new angular quadrature in actual runtime parameters')
            require(canonical(without_io(self.parameters)) == canonical(dict(without_io(seed_parameters), quadrature=512)),
                    'New runtime changed a parameter outside the declared N512 warm transition')
            self.coordinator = Coordinator(self.base, self.seed_height, control, self._inspect,
                                           self._classify, self._emit, self._persist_good)
        except Exception:
            self.close()
            raise

    @property
    def calls(self):
        return self.base.calls

    @property
    def ready(self):
        return self.base.ready

    @property
    def cut(self):
        return self.base.cut

    @property
    def linearD(self):
        return self.base.linearD

    @property
    def M(self):
        return self.base.M

    @property
    def proc(self):
        return self.base.proc

    def _emit(self, row):
        event = {'utc': datetime.now(timezone.utc).isoformat(), 'policy_sha256': self.policy_sha256, **row}
        self._journal.write(canonical(event) + '\n')
        self._journal.flush()
        os.fsync(self._journal.fileno())

    def _persist_good(self, record):
        p = Path(self.policy['last_good_file'])
        temporary = p.with_name(p.name + '.tmp')
        data = (canonical({'policy_sha256': self.policy_sha256, **record}) + '\n').encode()
        require(len(data) < 100000, 'Last-good reference unexpectedly large')
        with temporary.open('xb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary, p)

    def _inspect(self, call, h, jacobian, audit, physical):
        p = self.record_prefix.with_name(self.record_prefix.name + f'_{call:04d}.json.gz')
        packet = identity(p)
        require(packet['bytes'] < 5_000_000, 'Original physical record exceeds size limit')
        record = read(p)
        require(set(record) == {'request', 'response', 'config', 'source_sha256'}, 'Unexpected actual packet schema')
        require(canonical(record['config']) == canonical(self.cfg), 'Actual packet config changed')
        require(canonical(record['source_sha256']) == canonical(self.policy['source_sha256']), 'Actual nine-source identity changed')
        req = record['request']
        require(isinstance(req, dict) and set(req) == {'height', 'jacobian', 'audit'}
                and vector(req['height'], self.M) and same_height(req['height'], h)
                and type(req['jacobian']) is bool and type(req['audit']) is bool, 'Actual request identity mismatch')
        if physical:
            require(req['jacobian'] is jacobian and req['audit'] is audit, 'Actual flags differ from requested flags')
        else:
            require(not audit and (not jacobian or req['jacobian']), 'Cache cannot provide requested flags')
        r = record['response']
        require(isinstance(r, dict), 'Invalid original response')
        if 'failed' in r:
            require(physical and set(r) == {'failed', 'lastIteration', 'checkpoint'}
                    and isinstance(r['failed'], str), 'Invalid original failure schema')
            if r['checkpoint'] is not None:
                validate_checkpoint(r['checkpoint'], self.M, self.parameters)
                require(same_height(r['checkpoint']['cutHeight'], h), 'Failed CP has the wrong physical target label')
        else:
            validate_response(r, self.M, self.parameters, self.cfg['solveTolerance'], req['jacobian'], req['audit'])
            require(same_height(r['checkpoint']['cutHeight'], h), 'Actual CP does not label the requested physical H')
        return record, packet

    def _classify(self, record, call):
        # Reading only completed rows of this serialized call; the mutable
        # whole trace file is never advertised as an immutable input hash.
        rows = []
        p = Path(self.cfg['trialDiagnosticFile'])
        if p.exists():
            with p.open() as f:
                for line in f:
                    row = json.loads(line)
                    if row.get('call') == call:
                        rows.append(row)
        return classify_original_failure(record, call, rows, self.cfg['maxIterations'])

    def solve(self, height, jacobian=True, audit=False):
        return self.coordinator.solve(height, jacobian=jacobian, audit=audit)

    def close(self):
        if self.base is not None and hasattr(self.base, 'proc'):
            try:
                self.base.close()
            finally:
                if hasattr(self, '_journal') and not self._journal.closed:
                    self._journal.close()
        elif hasattr(self, '_journal') and not self._journal.closed:
            self._journal.close()


def pilot_main():
    """One actual external H1 request, only when explicitly launched by root."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--pilot-launch', type=Path, required=True)
    a = ap.parse_args()
    launch = read(a.pilot_launch)
    require(launch['schema'] == '78718-m15q512-linear-dn-closed-request-pilot-v1', 'Wrong pilot launch')
    for row in launch['bindings']:
        verify(row)
    verify(launch['config'])
    verify(launch['target_packet'])
    old = read(launch['target_packet']['path'])
    request = old['request']
    goal = np.asarray(request['height'], float).copy()
    summary_path = Path(launch['summary_file'])
    require(not summary_path.exists(), 'Pilot summary already exists')
    port, response, error = None, None, None
    started = time.monotonic()
    try:
        port = WeightedTailPort(launch['config']['path'], launch['source_root'],
                                launch['record_prefix'], node_heap=launch['node_heap'])
        response = port.solve(goal.copy(), jacobian=request['jacobian'], audit=request['audit'])
    except Exception as exc:
        error = repr(exc)
    finally:
        if port is not None:
            port.close()
    final_packet = None if port is None or port.coordinator is None or port.coordinator.good is None else port.coordinator.good['packet']
    success = response is not None and error is None
    summary = {'status': 'TARGET_DN_SUCCESS' if success else 'TARGET_DN_NOT_COMPLETED',
               'scope': 'One exact closed H1 request only. Prefix remains UNSOLVED; no common closed-map/metric/reach claim.',
               'prefix_status': 'UNSOLVED', 'error': error,
               'external_request_flags': {'jacobian': request['jacobian'], 'audit': request['audit']},
               'goal_sha256': digest(goal.tolist()), 'requested_target_completed': success,
               'returned_residual': None if response is None else response['residual'],
               'last_true_good_packet': final_packet,
               'actual_physical_calls': None if port is None else port.calls,
               'actual_worker_exit_code': None if port is None else port.proc.poll(),
               'seconds': time.monotonic() - started, 'launch': identity(a.pilot_launch)}
    with summary_path.open('x') as f:
        f.write(json.dumps(summary, indent=2, allow_nan=False) + '\n')
    print(json.dumps(summary, allow_nan=False), flush=True)
    return 0 if success else 2


if __name__ == '__main__':
    sys.exit(pilot_main())
