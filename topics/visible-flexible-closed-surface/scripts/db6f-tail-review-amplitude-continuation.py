#!/usr/bin/env python3
"""Independent storage/controller review; mock runs do not solve a tail.

The frozen actual continuation controller is executed with a deterministic
fake worker interface. This checks its bookkeeping, request heights, failure
rollback and final target/audit separation, not numerical ODE correctness.
"""
import argparse
import ast
import contextlib
import gzip
import hashlib
import importlib.util
import io
import json
import math
import sys
import tempfile
import types
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
CONTROLLER = HERE / 'db6f-prefix-tail-amplitude-continuation.py'
CLIENT = HERE / 'db6f-prefix-tail-continuation-client.py'
ORIGINAL_CLIENT = HERE / 'db6f-prefix-tail-trial-client.py'
WORKER = HERE / 'db6f-prefix-tail-trial-worker.mjs'
CORE = HERE / 'db6f-prefix-tail-trial-core.mjs'
METHOD = NOTES / '2026-11-09-db6f-prefix-tail-amplitude-continuation-method.md'
EXPECTED = {
    CONTROLLER: '23f75c9ecc2825e4a8314468775c40b06b6b47439edd0d0ed9a69a9fb5e298a9',
    CLIENT: 'cd9b25521427dcefebd5baddcf6a105c58c53f495cf8692fb725d49e4558a564',
    METHOD: '3fae1b9c9c28a5942e527cacf2710d5de1edd29b0418657441bb339d9334b77d',
}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix == '.gz' else p.read_text())


def load_module(file, name):
    spec = importlib.util.spec_from_file_location(name, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_case(label, config, prefix, source_root, goal, mode):
    """Run the unmodified controller main against a closed finite mock trace."""
    calls = []
    instances = []
    with tempfile.TemporaryDirectory(prefix='db6f-tail-review-continuation-', dir=NOTES) as td:
        folder = Path(td)
        out = folder / label

        class MockPort:
            def __init__(self, config_path, root, record_prefix, node_heap):
                self.config = Path(config_path)
                self.cfg = read(config_path)
                self.record_prefix = Path(record_prefix)
                self.calls = 0
                self.closed = False
                self.last_success_height = None
                self.proc = types.SimpleNamespace(poll=lambda: 0 if self.closed else None)
                instances.append(self)

            def solve(self, height, jacobian=True, audit=False):
                h = np.asarray(height, dtype=float)
                self.calls += 1
                scale = float(h[0] / goal[0])
                if mode == 'mixed':
                    failed = self.calls in (1, 4)
                    history_length = 4 if self.calls in (2, 3) else 2
                elif mode == 'all_fail':
                    failed, history_length = True, 0
                elif mode == 'final_audit_fail':
                    failed, history_length = bool(audit), 4
                elif mode == 'resume':
                    failed, history_length = self.calls == 1, 4
                elif mode == 'attempt_limit':
                    failed, history_length = True, 0
                else:
                    raise AssertionError(mode)
                prior = None if self.last_success_height is None else self.last_success_height.copy()
                request = dict(height=h.tolist(), jacobian=bool(jacobian), audit=bool(audit))
                if failed:
                    response = dict(failed='DETERMINISTIC_MOCK_FAILURE', lastIteration={'iteration': 0})
                else:
                    response = dict(converged=True, residual=1e-12,
                                    history=[{'iteration': k} for k in range(history_length)],
                                    heightJetJacobian=[0.] if jacobian else None,
                                    audit={'MOCK_ONLY': True} if audit else None)
                    self.last_success_height = h.copy()
                record = self.record_prefix.with_name(self.record_prefix.name + f'_{self.calls:04d}.json.gz')
                record.write_bytes(gzip.compress(json.dumps(dict(request=request, response=response)).encode(), mtime=0))
                for key in ('traceFile', 'trialDiagnosticFile'):
                    with Path(self.cfg[key]).open('a') as handle:
                        handle.write(json.dumps({'MOCK_ONLY': True, 'call': self.calls}) + '\n')
                calls.append(dict(scale=scale, request=request, failed=failed,
                                  previous_success_unchanged_on_failure=not failed or
                                  ((prior is None and self.last_success_height is None) or
                                   np.array_equal(prior, self.last_success_height))))
                if failed:
                    raise FloatingPointError('DETERMINISTIC_MOCK_FAILURE')
                return response

            def close(self):
                self.closed = True

        class Loader:
            def exec_module(self, module):
                module.WeightedTailPort = MockPort

        controller = load_module(CONTROLLER, 'continuation_controller_under_review')
        controller.importlib = types.SimpleNamespace(util=types.SimpleNamespace(
            spec_from_file_location=lambda *_: types.SimpleNamespace(loader=Loader()),
            module_from_spec=lambda *_: types.SimpleNamespace()))
        argv = [str(CONTROLLER), '--source-root', str(source_root), '--config', str(config),
                '--target-prefix', str(prefix), '--out-prefix', str(out)]
        if mode == 'attempt_limit':
            argv += ['--max-attempts', '2']
        if mode == 'resume':
            resume = folder / 'closed-converged-response.json.gz'
            h = goal * np.float64(.5) ** np.arange(1, len(goal) + 1)
            resume.write_bytes(gzip.compress(json.dumps(dict(
                request={'height': h.tolist()},
                response={'converged': True, 'residual': 1e-12})).encode(), mtime=0))
            argv += ['--resume-checkpoint', str(resume), '--resume-scale', '.5']
        controller.sys = types.SimpleNamespace(argv=argv, executable=sys.executable)
        original_argv = sys.argv
        try:
            sys.argv = argv
            with contextlib.redirect_stdout(io.StringIO()):
                controller.main()
        finally:
            sys.argv = original_argv
        state = read(str(out) + '-progress.json')
        generated = read(str(out) + '-config.json')
        for row in state['attempts']:
            call = calls[row['call'] - 1]
            s = row['scale']
            expected = goal.copy() if s == 1 else goal * np.float64(s) ** np.arange(1, len(goal) + 1)
            assert np.array_equal(np.asarray(call['request']['height']), expected)
            call['scale'] = s
        assert instances[0].closed
        assert all(c['previous_success_unchanged_on_failure'] for c in calls)
        # Only recording destinations and the explicitly discarded/replaced
        # warm checkpoint differ from the original actual-solve config.
        omit = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
                'trialDiagnosticFile', 'trialStatePrefix'}
        original = read(config)
        assert {k: v for k, v in generated.items() if k not in omit} == \
               {k: v for k, v in original.items() if k not in omit}
        if mode != 'resume':
            assert 'initialCheckpoint' not in generated
            first = np.asarray(calls[0]['request']['height'])
            expected = np.array([math.ldexp(float(v), -2 * (j + 1)) for j, v in enumerate(goal)])
            assert np.array_equal(first, expected)
        else:
            assert generated['initialCheckpoint'] == str(resume)
        # All closed trace/trial files have one matching call, with no active
        # stream left after the final worker shutdown.
        for call in range(1, len(calls) + 1):
            for kind in ('trace', 'trials'):
                rows = Path(str(out) + f'-call{call:03d}-{kind}.jsonl').read_text().splitlines()
                assert len(rows) == 1 and json.loads(rows[0])['call'] == call
        assert not Path(generated['traceFile']).exists()
        assert not Path(generated['trialDiagnosticFile']).exists()
        if mode == 'mixed':
            expect = [.25, .125, .25, .375, .3125, .40625, .546875, .746875, .946875, 1., 1.]
            assert len(calls) == len(expect)
            assert all(abs(c['scale'] - e) <= math.ulp(1.) for c, e in zip(calls, expect))
            assert state['target_reached'] and state['target_audited']
            assert state['status'] == 'TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_STILL_UNSOLVED'
        elif mode == 'all_fail':
            assert state['status'] == 'UNCONVERGED_CONTINUATION_STEP_LIMIT'
            assert not state['target_reached'] and not state['target_audited']
            assert state['last_converged_scale'] is None
        elif mode == 'attempt_limit':
            assert state['status'] == 'UNCONVERGED_CONTINUATION_ATTEMPT_LIMIT'
            assert not state['target_reached'] and not state['target_audited']
        elif mode == 'final_audit_fail':
            assert state['status'] == 'UNCONVERGED_CONTINUATION_EXCEPTION'
            assert state['target_reached'] and not state['target_audited']
            assert 'exception_response' in state
        elif mode == 'resume':
            assert [c['scale'] for c in calls[:2]] == [.625, .5625]
            assert state['target_reached'] and state['target_audited']
        audits = [c for c in calls if c['request']['audit']]
        if audits:
            assert len(audits) == 1 and calls[-1] is audits[0]
            assert audits[0]['request']['jacobian']
            assert np.array_equal(np.asarray(audits[0]['request']['height']), goal)
        assert all(not c['request']['jacobian'] for c in calls if not c['request']['audit'])
        return dict(mode=mode, calls=len(calls), status=state['status'],
                    target_reached=state['target_reached'], target_audited=state['target_audited'],
                    requested_scales=[c['scale'] for c in calls],
                    failures=[k + 1 for k, c in enumerate(calls) if c['failed']],
                    original_config_preserved=True, closed_log_rotation=True,
                    exact_final_target=True if audits else 'not reached',
                    scope='MOCK bookkeeping only; no actual tail solve or existence claim')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config', type=Path, required=True)
    ap.add_argument('--target-prefix', type=Path, required=True)
    ap.add_argument('--source-root', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    for file, expected in EXPECTED.items():
        assert sha(file) == expected, file
    for file in (CONTROLLER, CLIENT):
        ast.parse(file.read_text())
    original = ORIGINAL_CLIENT.read_text()
    normalized = CLIENT.read_text().replace("'db6f-prefix-tail-continuation-client.py'",
                                           "'db6f-prefix-tail-trial-client.py'")
    new_publish = """        # Publish a complete response atomically, without replacing an old one.
        tmp=file.with_name(file.name+'.tmp')
        with tmp.open('xb') as f:
            f.write(data);f.flush();os.fsync(f.fileno())
        try:os.link(tmp,file)
        finally:tmp.unlink()"""
    assert new_publish in normalized
    normalized = normalized.replace(new_publish, "        with file.open('xb') as f:f.write(data)")
    assert normalized == original
    config = read(args.config)
    prefix = read(args.target_prefix)
    goal = np.asarray(prefix['predicted_cut_height'], dtype=float)
    assert goal.shape == (15,) and np.all(np.isfinite(goal)) and goal[0] != 0
    assert config['modes'] == prefix['config']['modes'] == 15
    assert prefix['config']['actual_nonlinear_tail'] is False
    assert all(config.get(k) == v for k, v in prefix['physical_tail_parameters'].items())
    assert (config['quadrature'], config['depth'], config['shootingParts'], config['steps']) == (256, 12, 8, 32)
    assert config['solveTolerance'] == 2e-9
    assert config.get('projectionFloor', .05) == .05
    cases = [run_case(name, args.config.resolve(), args.target_prefix.resolve(),
                      args.source_root.resolve(), goal, name)
             for name in ('mixed', 'all_fail', 'attempt_limit', 'final_audit_fail', 'resume')]
    result = dict(status='PASS: actual input binding, source delta and mock controller cases',
                  scope=__doc__, actual_finite_tail_solve_executed=False,
                  sources={str(p): sha(p) for p in (*EXPECTED, ORIGINAL_CLIENT, WORKER, CORE, Path(__file__))},
                  inputs={str(p): sha(p) for p in (args.config, args.target_prefix)},
                  physical_parameter_keys_checked=len(prefix['physical_tail_parameters']),
                  original_numerical_settings=dict(modes=15, quadrature=256, depth=12,
                      shootingParts=8, steps=32, tolerance=2e-9, projectionFloor=.05,
                      projectionFloor_origin='unchanged core default; absent from config'),
                  client_delta_only_atomic_publish_and_self_hash=True,
                  cases=cases)
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(status=result['status'], cases=len(cases), out=str(args.out))))


if __name__ == '__main__':
    main()
