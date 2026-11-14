#!/usr/bin/env python3
"""Explicit small-height scheduling of the same original true DN.

The initialization accepts declared numerical Fourier/quadrature and shooting
partition/RK/audit changes. The physical geometry and final target remain. The
original trial worker performs its real warm remesh; the original Coordinator
then solves every requested physical target. Old response Jacobians are never
used as new-M Jacobians. This file is separate from the running M15 entry.
"""
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


c = module('generic_mode_height_control', HERE/'78718-prefix-tail-linear-m15q512-v1.py')
small_height = module('explicit_small_height_policy', HERE/'78718-small-height-continuation.py')
SmallHeightCoordinator = small_height.coordinator_class(c.Coordinator)


class WeightedTailPort(c.WeightedTailPort):
    """Reuse all solve/cache/record/close methods; initialize an explicit M."""
    def __init__(self, config, source_root, record_prefix, node_heap=1536):
        self.config = Path(config).resolve()
        self.record_prefix = Path(record_prefix).resolve()
        self.source_root = Path(source_root).resolve()
        self.policy_path = self.record_prefix.with_name(self.record_prefix.name+'-continuation.json')
        self.policy = c.read(self.policy_path)
        self.cfg = c.read(self.config)
        M, N = self.cfg['modes'], self.cfg['quadrature']
        c.require(type(M) is int and M > 0 and type(N) is int and N >= 512 and N > 4*3*M,
                  'Insufficient requested angular resolution')
        c.require(self.policy['record_prefix'] == str(self.record_prefix), 'Different output prefix')
        c.require(self.cfg['solveTolerance'] == 2e-9 and self.cfg['maxIterations'] == 36
                  and self.cfg.get('projectionFloor', .05) == .05
                  and self.cfg.get('correctInitialBoundary', True) is True,
                  'The original nonlinear tolerance or warm boundary rule changed')
        # A failed/iteration checkpoint may warm the worker, but it must never
        # become the known successful seed or redefine the requested height.
        known_seed = self.policy.get('known_seed_packet') or self.cfg.get('initialCheckpoint')
        c.require(isinstance(known_seed, str), 'Missing actual successful parameter/height seed')
        seed_path = Path(known_seed).resolve()
        self.seed = c.read(seed_path)
        old_parameters = self.seed['response']['checkpoint']['parameters']
        oldM = old_parameters['modes']
        c.require(type(oldM) is int and oldM <= M, 'Mode continuation cannot lower the input order')
        c.validate_response(self.seed['response'], oldM, old_parameters, 2e-9, False, False)
        c.require(self.seed['response']['converged'] is True,
                  'Tail warm file is not an actual successful finite response')
        oldcfg = dict(c.without_io(self.seed['config']), modes=M, quadrature=N)
        grid = self.policy.get('tail_shooting_grid')
        if grid is not None:
            for key in ('shootingParts', 'steps', 'auditSteps'):
                c.require(type(grid.get(key)) is int and grid[key] > 0
                          and self.cfg.get(key) == grid[key],
                          'Invalid declared numerical tail grid: '+key)
                oldcfg[key] = grid[key]
        c.require(c.canonical(oldcfg) == c.canonical(c.without_io(self.cfg)),
                  'Tail configuration changed beyond M, quadrature, declared numerical grid and output paths')
        self.seed_height = np.zeros(M)
        self.seed_height[:oldM] = self.seed['request']['height']
        c.require(c.same_height(self.seed['request']['height'],
                                self.seed['response']['checkpoint']['cutHeight']),
                  'Warm physical target label differs from its state')
        bootstrap_scale = self.policy.get('bootstrap_height_scale', 1.)
        c.require(c.number(bootstrap_scale) and 0 < bootstrap_scale <= 1.,
                  'Invalid first actual DN height scale')
        self.bootstrap_height = self.seed_height*bootstrap_scale
        bootstrap_override = self.policy.get('bootstrap_height_override')
        if bootstrap_override is not None:
            c.require(c.vector(bootstrap_override, M),
                      'Exact warm-height bootstrap requires a finite complete cutHeight vector')
            self.bootstrap_height = np.asarray(bootstrap_override, dtype=float).copy()
        self.bootstrap_policy = {
            'height_scale': bootstrap_scale,
            'height_scale_applied': bootstrap_override is None,
            'height_source': ('actual-retained-initial-checkpoint-cutHeight'
                              if bootstrap_override is not None else 'scaled-known-successful-seed'),
            'original_warm_height_sha256': c.digest(self.seed_height.tolist()),
            'first_actual_request_height_sha256': c.digest(self.bootstrap_height.tolist()),
            'original_warm_packet_unchanged': True,
            'worker_cold_start': self.policy.get('tail_cold_start', False),
            'worker_initial_checkpoint': self.cfg.get('initialCheckpoint'),
            'new_scaled_response_must_be_actually_solved': True,
            'external_goal_unchanged': True}
        paths = [self.policy['journal_file'], self.policy['last_good_file'],
                 self.cfg['traceFile'], self.cfg['iterationCheckpointFile'],
                 self.cfg['trialDiagnosticFile']]
        c.require(len(set(paths)) == len(paths) and all(not Path(p).exists() for p in paths),
                  'Run output already exists or collides')
        c.require(not list(self.record_prefix.parent.glob(self.record_prefix.name+'_????.json.gz')),
                  'Physical packet prefix was already used')
        self.policy_sha256 = c.identity(self.policy_path)['sha256']
        self._journal = Path(self.policy['journal_file']).open('x', buffering=1)
        self.base = self.coordinator = None
        self.parameters = None
        try:
            self._emit({'event':'control-start',
                        'bootstrap': self.bootstrap_policy,
                        'scope':'Finite DN control only; prefix remains UNSOLVED.'})
            trial = module('generic_mode_geometric_trial_client', HERE/'fd2d-single-tail-client.py')
            self.base = trial.WeightedTailPort.__new__(trial.WeightedTailPort)
            trial.WeightedTailPort.__init__(self.base, self.config, self.source_root,
                                           self.record_prefix, node_heap)
            # Honest source names in each actual packet; no eight/nine-source
            # historic label is borrowed for this generic-M interface.
            for name in (Path(__file__).name, '78718-prefix-tail-linear-m15q512-v1.py',
                         '78718-small-height-continuation.py', 'fd2d-run-prefix-single.py'):
                self.base.sources[name] = c.identity(HERE/name)['sha256']
            if self.policy.get('tail_trial', 'momentum') in ('geometric', 'geometric-centered'):
                name = '78718-tail-geometric-trial-control.py'
                self.base.sources[name] = c.identity(HERE/name)['sha256']
            self.policy['source_sha256'] = dict(self.base.sources)
            self.parameters = self.base.ready['parameters']
            expected = dict(c.without_io(old_parameters), modes=M, quadrature=N)
            if grid is not None:
                old_parts = old_parameters['shootingParts']
                c.require(old_parameters['depth']*grid['shootingParts'] % old_parts == 0,
                          'New finite shooting depth is not integral')
                expected.update({key: grid[key] for key in ('shootingParts', 'steps', 'auditSteps')})
                expected['depth'] = old_parameters['depth']*grid['shootingParts']//old_parts
            c.require(c.canonical(c.without_io(self.parameters)) == c.canonical(expected),
                      'Actual DN parameters changed outside the declared M/N and numerical grid refinement')
            self.coordinator = SmallHeightCoordinator(self.base, self.bootstrap_height,
                self.policy['control'], self._inspect, self._classify,
                self._emit, self._persist_good,
                direct_relative_limit=self.policy['small_height_continuation']['direct_relative_limit'])
        except Exception:
            self.close()
            raise

    def _classify(self, record, call):
        if self.policy.get('tail_trial', 'momentum') not in ('geometric', 'geometric-centered'):
            return super()._classify(record, call)
        rows = []
        path = Path(self.cfg['trialDiagnosticFile'])
        if path.exists():
            with path.open() as stream:
                for line in stream:
                    row = json.loads(line)
                    if row.get('call') == call:
                        rows.append(row)
        control = module('generic_geometric_trial_control',
                         HERE/'78718-tail-geometric-trial-control.py')
        return control.classify_failure(record, call, rows, c, self.cfg['maxIterations'])
