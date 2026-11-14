#!/usr/bin/env python3
"""Accept a saved affine-inner prefix only after an independently saved true DN.

The complete audited tail packet must match the exact raw cut height, all
equations/discretization, and every loaded tail source hash. Original raw
identity checks run unchanged. Collocation RMS is recomputed from the saved
cubic, and the original inlet and unscaled physical true-DN gates are tested.
Only then is the pending state passed to the original physical interpolant
and audits. This records a genuine staged evaluation of the original finite
problem; it asserts neither exact isometry nor infinite closure.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import json
import math
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
from scipy.integrate._bvp import collocation_fun, estimate_rms_residuals
import root_actual_bounded_neck as bounded
from root_actual_staged_tail import equation_config, read_json, sha

HERE = Path(__file__).resolve().parent


class RecordedAuditedPort:
    """Exact saved-response recovery: there is no nearby-height cache."""
    def __init__(self, packet, ready, config, source_topic):
        self.packet = Path(packet); saved = read_json(self.packet)
        self.config = Path(config); cfg = read_json(config)
        if equation_config(saved['config']) != equation_config(cfg):
            raise ValueError('Recorded DN changed equations or discretization')
        self.ready = ready; self.cut = ready['cut']
        self.sources = saved['source_sha256']
        for name, expected in self.sources.items():
            local = HERE / name
            path = local if local.is_file() else source_topic/'scripts'/name
            if not path.is_file() or sha(path) != expected:
                raise ValueError('Recorded DN source hash differs: ' + name)
        self.M = int(cfg['modes'])
        self.linearD = np.asarray(ready['linearSlope'])
        self.response = saved['response']; request = saved['request']
        self.height = np.asarray(request['height'], dtype=float)
        response = self.response
        if (not request['jacobian'] or not request['audit'] or
                not response.get('converged') or response.get('audit') is None or
                response.get('failed') or
                not math.isfinite(float(response['residual'])) or
                float(response['residual']) > float(cfg['solveTolerance'])):
            raise ValueError('A complete successful audited nonlinear DN is required')
        jac = np.asarray(response['heightJetJacobian'], dtype=float)
        if jac.size != (3*self.M + 2)*self.M or not np.all(np.isfinite(jac)):
            raise ValueError('Incomplete actual height-jet Jacobian')
        if (self.height.shape != (self.M,) or not np.all(np.isfinite(self.height)) or
                not np.array_equal(response['checkpoint']['cutHeight'], self.height)):
            raise ValueError('Response checkpoint changed its exact complete height')
        stem = self.packet.name.removesuffix('.json.gz')
        name, count = stem.rsplit('_', 1)
        self.calls = int(count)
        self.record_prefix = self.packet.with_name(name)
        self.recovery_calls = 0

    def solve(self, height, jacobian=True, audit=False):
        if not np.array_equal(np.asarray(height, float), self.height):
            raise ValueError('Saved true DN is unavailable at this different height')
        self.recovery_calls += 1
        return self.response


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--tail-packet', type=Path, required=True)
    ready_group = parser.add_mutually_exclusive_group(required=True)
    ready_group.add_argument('--tail-ready', type=Path)
    ready_group.add_argument('--tail-ready-from', type=Path)
    parser.add_argument('--validation-output', type=Path, required=True)
    parser.add_argument('--validate-acceptance-only', action='store_true')
    options, remaining = parser.parse_known_args()
    def argument(name):
        return Path(remaining[remaining.index(name) + 1])
    raw_path = argument('--raw-collocation-restart')
    tail_config = argument('--tail-config'); source_topic = argument('--source-topic')
    if '--postprocess-only' in remaining:
        raise ValueError('Pending recovery must execute its real acceptance checks')
    ready = (read_json(options.tail_ready) if options.tail_ready else
             read_json(options.tail_ready_from)['actual_tail']['ready'])
    port = RecordedAuditedPort(options.tail_packet, ready, tail_config, source_topic)
    raw_record = read_json(raw_path)
    if (raw_record['solver_success'] or raw_record['status'] != 0 or
            not raw_record['provenance'].get('affine_inner_success') or
            not raw_record['provenance'].get('actual_nonlinear_coupling_pending')):
        raise ValueError('Only explicitly pending successful affine-inner states apply')
    provenance = dict(scope=__doc__, raw=str(raw_path), raw_sha256=sha(raw_path),
                      tail_packet=str(options.tail_packet), tail_packet_sha256=sha(options.tail_packet),
                      config_sha256=sha(tail_config), source_sha256=sha(__file__),
                      prefix_accepted=False, numerical_BVP_repeated=False,
                      saved_full_true_DN_reused=True, verification=None)
    original = bounded.adapter.module

    def ensure_tail(self):
        if self.tail is not None:
            return
        if self.M != port.M:
            raise ValueError('Prefix and saved tail spectra differ')
        for key in ('radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep'):
            if not np.isclose(port.cut[key], self.port['cut'][key], rtol=2e-11, atol=2e-13):
                raise ValueError('Saved true DN physical cut differs: ' + key)
        self.tail = port

    def accept(self, fun, bc, x, y, p, **kw):
        import root_raw_collocation
        raw, record = root_raw_collocation.read(raw_path, self, SimpleNamespace(tol=kw['tol']))
        if not all(np.array_equal(a, b) for a, b in
                   [(raw.x, x), (raw.y, y), (raw.p, p)]):
            raise ValueError('Recovery input changed the raw arrays')
        self.ensure_tail(); height = self.tail_height(y[:, -1])
        response = port.solve(height, jacobian=True, audit=True)
        h = np.diff(x)
        col_res, _, _, f_middle = collocation_fun(fun, y, p, x, h)
        rms = estimate_rms_residuals(fun, raw.sol, x, h, p,
                                     1.5*col_res/h, f_middle)
        self.select(p); flow = self.flow(p[0])
        dy = flow.fun(np.array([flow.end]), np.asarray(y[:, -1], np.longdouble)[:, None], p)[:, 0]
        physical = np.asarray(self.q*dy[self.iz:] -
                              np.asarray(response['jets']['slope'])/math.sqrt(self.port['cut']['E']), float)
        boundary = bc(y[:, 0], y[:, -1], p)
        actual_tol = float(self.raw_recovery_context['actual_tail_tolerance'])
        check = dict(exact_complete_height_match=True,
                     raw_identity_and_all_array_hashes_verified=True,
                     original_rms_max=float(np.max(raw.rms_residuals)),
                     recomputed_rms_max=float(np.max(rms)), rms_tolerance=float(kw['tol']),
                     rms_replay_max_difference=float(np.max(abs(rms-raw.rms_residuals))),
                     inlet_scaled_max=float(np.max(abs(boundary[:self.n]))),
                     inlet_tolerance=float(kw['bc_tol']),
                     full_scaled_bc_diagnostic=float(np.max(abs(boundary))),
                     true_physical_bc_max=float(np.max(abs(physical))),
                     true_physical_bc_tolerance=actual_tol,
                     tail_residual=float(response['residual']),
                     tail_audit_present=True, tail_source_hashes_identical=True)
        accepted = (check['recomputed_rms_max'] <= kw['tol'] and
                    check['inlet_scaled_max'] <= kw['bc_tol'] and
                    check['true_physical_bc_max'] <= actual_tol)
        check['passed_original_acceptance'] = bool(accepted)
        provenance['verification'] = check
        provenance['prefix_accepted'] = bool(accepted and not options.validate_acceptance_only)
        options.validation_output.write_text(json.dumps(provenance, indent=2) + '\n')
        print(json.dumps(dict(event='staged_actual_acceptance', **check)), flush=True)
        if not accepted:
            raise ValueError('Original actual prefix acceptance failed; raw state remains pending')
        if options.validate_acceptance_only:
            raise RuntimeError('Acceptance inspection complete; no physical result requested')
        self.outer_history = list(record['provenance']['outer_history'])
        self.outer_history[-1].update(actual_physical_bc_max=check['true_physical_bc_max'],
                                     tail_residual=check['tail_residual'], staged_response_recovery=provenance)
        raw.success = True
        raw.message = 'Saved affine-inner state passed independently recomputed original true-DN and RMS gates'
        raw.rms_residuals = rms
        return raw

    def module(name, path):
        loaded = original(name, path)
        if Path(path).name == 'root_dual_core_bvp.py':
            source_main = loaded.main
            def entry():
                factory = loaded.make_dual
                def instrument(*args, **kwargs):
                    cls = factory(*args, **kwargs)
                    cls.ensure_tail = ensure_tail
                    cls.solve_coupled = accept
                    return cls
                loaded.make_dual = instrument
                return source_main()
            loaded.main = entry
        return loaded
    bounded.adapter.module = module
    sys.argv = [sys.argv[0]] + remaining
    bounded.main()
    if provenance['verification'] is None:
        raise RuntimeError('Staged acceptance checks were not reached')
    out = argument('--out-prefix')
    for path in (out.with_suffix('.json.gz'), out.with_name(out.name + '-summary.json')):
        if not path.is_file():
            continue
        data = read_json(path); data['staged_actual_recovery'] = provenance
        contents = (json.dumps(data, indent=2) + '\n').encode()
        path.write_bytes(gzip.compress(contents, mtime=0) if path.suffix == '.gz' else contents)


if __name__ == '__main__':
    main()
