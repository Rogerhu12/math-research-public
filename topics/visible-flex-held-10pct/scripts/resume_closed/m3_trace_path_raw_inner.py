#!/usr/bin/env python3
"""Recover the actual returned lambda=.02 inner state without solving it again.

The command-line entry only binds saved data, byte identities and source. A
separate native_model() restores the complete original normalized x/y/p/cubic,
RMS vector and returned diagnostics with the actual partial-lift definition.
It deliberately attaches no tail: the pending changed-H response must be
obtained and accepted by the original actual worker before the original outer
BC check. The old actual response is only the recorded inner affine anchor.
No mean, metric, physical quintic, BVP or tail calculation is performed here.
"""
from dataclasses import dataclass
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
from types import SimpleNamespace

import m3_trace_path_prefix as physical_reader
from m3_trace_path_prefix import (KIND, CONTROL_PATH, M3, check_plan, checked_file,
                                  exact_numbers, load, payload_sha, ref, sha)


RAW_SHA = 'bc2fee7117ba8d8d842ac3352290ce55e966813ebf8048494688ce6d46180cc0'
SIDECAR_SHA = 'fcbe787e4e730c09fc54c8f971371edb5159a99cb22d480852714afa38ce642a'
FAILED_TAIL_SHA = '6f0cdfa7bdc27c330bd3320ba94417e1fb410430dfdcdd3bd685c2944d2411ac'
HELPER_SHA = '5a918498f3f91fb173c60ada1983f8cb89e64083e36c6ab55f3913ec7c55bd3a'


def flat(values):
    for value in values:
        if isinstance(value, list):
            yield from flat(value)
        else:
            yield value


def array_hash(values):
    digest = hashlib.sha256()
    for value in flat(values):
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError('A saved numerical array is not finite')
        digest.update(struct.pack('<d', float(value)))
    return digest.hexdigest()


@dataclass(frozen=True)
class RawInnerBinding:
    raw_path: Path
    sidecar_path: Path
    failed_tail_path: Path
    raw: dict
    sidecar: dict
    failed_tail: dict
    plan_path: Path
    plan: dict
    old_actual_anchor: dict

    def check_files(self):
        expected = [(self.raw_path, RAW_SHA), (self.sidecar_path, SIDECAR_SHA),
                    (self.failed_tail_path, FAILED_TAIL_SHA),
                    (Path(physical_reader.__file__), HELPER_SHA)]
        for path, digest in expected:
            if sha(path) != digest:
                raise ValueError('A frozen recovery input/helper changed: ' + str(path))
        checked_file(self.raw['plan'])
        checked_file(self.sidecar['actual_tail_record'])
        check_plan(self.plan_path)

    def descriptor(self):
        r = self.raw
        final_profile = copy.deepcopy(r['path_base_profile'])
        final_profile['delta'] += r['p'][0]
        return dict(scope=__doc__, source=ref(__file__), helper=ref(physical_reader.__file__),
            raw_inner=ref(self.raw_path), sidecar=ref(self.sidecar_path),
            changed_height_failed_tail=ref(self.failed_tail_path), plan=ref(self.plan_path),
            original_inner_actual_anchor=self.sidecar['actual_tail_record'],
            inner_affine_response_payload_sha256=self.sidecar['response_payload_sha256'],
            core_kind=KIND, control_path=CONTROL_PATH,
            path_definition=r['path_definition'], path_lambda=r['path_lambda'],
            lift_window=r['lift_window'], q_gauge=r['q_gauge'],
            defining_support_q=r['seed_support_amplitude'],
            path_base_profile=r['path_base_profile'], candidate_physical_profile=final_profile,
            full_parameters=r['p'], full_parameter_scales=r['parameter_scales'],
            full_physical_controls=r['original_physical_controls'],
            coordinate=r['coordinate'], normalized_mesh_points=len(r['x']),
            state_components=len(r['y']), raw_cubic_shape=[4, len(r['x'])-1, 25],
            array_binary64_sha256={key: array_hash(r[key]) for key in ('x', 'y', 'p', 'rms_residuals')},
            cubic_knots_binary64_sha256=array_hash(r['raw_cubic']['x']),
            cubic_coefficients_binary64_sha256=array_hash(r['raw_cubic']['c']),
            original_cubic_axis=r['raw_cubic']['axis'],
            original_cubic_extrapolate=r['raw_cubic']['extrapolate'],
            restored_cubic_domain='Only the saved [x[0],x[-1]]; no extension outside it is supplied.',
            original_inner_success=r['solver_success'], original_status=r['status'],
            original_message=r['message'], original_niter=r['niter'],
            original_max_rms=max(r['rms_residuals']), original_rms_entries=len(r['rms_residuals']),
            old_inner_height_binary64_sha256=self.sidecar['height_binary64_sha256'],
            new_pending_height_binary64_sha256=array_hash(r['candidate_cut_height']),
            full_pending_height=r['candidate_cut_height'],
            pending_request=self.failed_tail['request'],
            observed_tail_last_iteration=self.failed_tail['response']['lastIteration'],
            current_resume_point='Inner outer=0 returned successfully. Its changed-H actual tail request failed before the original actual BC/outer history row was formed.',
            remaining_outer_rule='After a genuine same-new-H response, attach the real tail, perform the original BC check and create outer row0. If not accepted, continue original outer indices1..7; never rerun inner0.',
            missing_original_solution_fields=['yp'],
            missing_field_scope='The returned raw saved x/y/p/cubic/RMS/status/message/niter; it did not save sol.yp. No derivative is inferred and relabeled as that original array. The original post-tail control flow does not consume sol.yp.',
            native_model_constructed=False, mean_height_integrated=False,
            physical_quintic_constructed=False, full_metric_evaluated=False,
            old_inner_rerun=False, BVP_solver_invoked=False, tail_solver_invoked=False,
            actual_coupled_terminal_accepted=False, continuous_error_certificate=False)

    def native_model(self):
        """Restore objects for later original post-tail continuation, not a solve.

        The original model must be constructed in a fresh process. The exact
        saved normalized node values are kept independently of the cubic;
        they are never replaced by values evaluated from that cubic. Its knot
        and coefficient arrays are copied verbatim; external extrapolation is
        disabled. Original stored diagnostics are copied without recomputing
        them. Neither the old affine tail nor a failed new tail is installed
        as obj.tail; the subsequent actual continuation must supply it.
        """
        self.check_files()
        import numpy as np
        from scipy.interpolate import PPoly
        from q060_cosine_reference import bind_reference
        original = load(self.plan['design']['original_reference_binding']['path'])
        bound = bind_reference(original['checkpoint']['path'], original['terminal_record']['path'],
                               original['source_topic'], original['short_bridge']['path'])
        native = bound.native_reference()
        sys.path.insert(0, str(M3))
        from m3_circle_trace_path_model import CircleTracePathEnvironment
        r = self.raw
        if r['path_base_profile'] != bound.record['frozen_profile']:
            raise ValueError('A different base profile needs a declared coordinate transfer')
        env = CircleTracePathEnvironment(bound, native, copy.deepcopy(r['core_round_settings']))
        obj = env.make(r['path_lambda'], r['seed_support_amplitude'])
        p = np.asarray(r['p'], float)
        obj.initial(p)
        flow = obj.flow(float(p[0]))
        if (obj.cfg != r['path_base_profile'] or obj.path_definition != r['path_definition'] or
                not exact_numbers(obj.pscale, r['parameter_scales']) or
                not exact_numbers(obj.pscale*p[1:], r['original_physical_controls']) or
                flow.exact_lift_core is not obj._core or hasattr(obj, 'tail')):
            raise ValueError('The saved partial model was not reconstructed faithfully')
        x, y = np.asarray(r['x'], float), np.asarray(r['y'], float)
        c = np.asarray(r['raw_cubic']['c'], float)
        knots = np.asarray(r['raw_cubic']['x'], float)
        cubic = PPoly.construct_fast(c, knots, extrapolate=False, axis=1)
        sol = SimpleNamespace(x=x, y=y, p=p, sol=cubic,
            success=r['solver_success'], status=r['status'], message=r['message'],
            niter=r['niter'], rms_residuals=np.asarray(r['rms_residuals'], float))
        actual_H = obj.bridge.sigma*obj.q*y[obj.iz:, -1]
        if not exact_numbers(actual_H, r['candidate_cut_height']):
            raise ValueError('The restored complete pending height differs')
        self.check_files()
        return SimpleNamespace(obj=obj, flow=flow, solution=sol, environment=env,
            original_cosine_reference=native, original_inner_actual_anchor=self.old_actual_anchor,
            inner_anchor_height=np.asarray(self.sidecar['height'], float),
            pending_request=copy.deepcopy(self.failed_tail['request']),
            completed_inner_index=0, next_inner_index=1, outer_budget=tuple(range(8)),
            source_binding=self.descriptor(), original_sol_yp_available=False,
            actual_tail_attached=False)


def bind_raw_inner(raw_path, sidecar_path, failed_tail_path):
    raw_path, sidecar_path, failed_tail_path = (Path(p).resolve() for p in
                                              (raw_path, sidecar_path, failed_tail_path))
    for path, digest in ((raw_path, RAW_SHA), (sidecar_path, SIDECAR_SHA),
                         (failed_tail_path, FAILED_TAIL_SHA)):
        if sha(path) != digest:
            raise ValueError('This recovery is pinned to the new real lambda=.02 inner: ' + str(path))
    r, side, failed = map(load, (raw_path, sidecar_path, failed_tail_path))
    plan_path = checked_file(r['plan'])
    plan = check_plan(plan_path)
    d = plan['design']
    if (r['stage'] != 'immediately_after_original_solve_bvp' or r['inner'] != 0 or
            r['coordinate'] != 'Original normalized adaptive collocation chart' or
            r['solver_success'] is not True or r['status'] != 0 or
            not isinstance(r['message'], str) or not isinstance(r['niter'], int) or
            r['core_kind'] != KIND or r['core_control_path'] != CONTROL_PATH or
            r['fixed_metric'] is not False or r['cubic_available'] is not True):
        raise ValueError('An actual successful original returned inner is required')
    if (side['raw'] != ref(raw_path) or side['plan'] != r['plan'] or
            r['chart'] != d['original_chart'] or
            r['path_base_profile'] != d['physical_profile'] or
            r['base_frozen_profile'] != r['path_base_profile'] or
            r['core_round_settings'] != d['new_core_settings'] or
            not exact_numbers([r['path_lambda'], r['partial_lift_strength']], [d['lambda_value']]*2) or
            r['lift_window'] != d['lift_window'] or r['q_gauge'] != .06 or
            r['seed_support_amplitude'] != d['new_q']['q_binary64']):
        raise ValueError('The saved chart/base profile/partial-lift identity differs')
    definition = r['path_definition']
    if (definition['settings'] != r['core_round_settings'] or
            definition['lambda_value'] != r['path_lambda'] or
            definition['numerical_gauge'] != r['q_gauge'] or
            definition['defining_support_amplitude'] != r['seed_support_amplitude'] or
            definition['fixed_metric'] is not False or definition['warp_reference'] != .06 or
            not exact_numbers(definition['parameter_scales'], r['parameter_scales'])):
        raise ValueError('Incomplete original path definition')
    x, y, p, scales = r['x'], r['y'], r['p'], r['parameter_scales']
    cubic, rms = r['raw_cubic'], r['rms_residuals']
    if (len(x) != 493 or len(y) != 25 or any(len(row) != len(x) for row in y) or
            len(p) != 8 or len(scales) != 7 or len(rms) != len(x)-1 or
            x[0] != 0. or x[-1] != 1. or any(a >= b for a, b in zip(x, x[1:])) or
            cubic['axis'] != 1 or cubic['extrapolate'] is not True or
            not exact_numbers(cubic['x'], x) or len(cubic['c']) != 4 or
            any(len(row) != len(x)-1 or any(len(v) != 25 for v in row) for row in cubic['c'])):
        raise ValueError('The full original x/y/p/cubic/RMS layout differs')
    for values in (x, y, p, scales, cubic['c'], rms):
        array_hash(values)  # Reject nonfinite arrays, without interpolation/evaluation.
    if (not exact_numbers(scales, plan['initial_parameter_scales']) or
            not exact_numbers([p[j+1]*scales[j] for j in range(7)], r['original_physical_controls'])):
        raise ValueError('The complete seven physical controls differ')
    original = load(d['original_reference_checkpoint']['path'])
    if original['physical_tail_cut']['radius'] != .3:
        raise ValueError('The established inward radial bridge sign changed')
    H = [(-1.*r['q_gauge'])*y[17+j][-1] for j in range(8)]
    if not exact_numbers(H, r['candidate_cut_height']):
        raise ValueError('The stored pending H differs from original sigma*q*y')
    anchor_path = checked_file(side['actual_tail_record'])
    anchor = load(anchor_path)
    if (anchor['request']['jacobian'] is not True or anchor['request']['audit'] is not True or
            anchor['response']['converged'] is not True or not anchor['response']['residual'] < 2e-9 or
            not exact_numbers(anchor['request']['height'], side['height']) or
            array_hash(side['height']) != side['height_binary64_sha256'] or
            payload_sha(anchor['response']) != side['response_payload_sha256'] or
            side['tail_native_calls'] != 0):
        raise ValueError('The original complete inner affine anchor is missing')
    if (failed['config'] != load(plan['tail_config']['path']) or
            failed['source_sha256'] != plan['native_tail_source_sha256'] or
            not exact_numbers(failed['request']['height'], H) or
            failed['request']['jacobian'] is not True or failed['request']['audit'] is not True or
            not failed['response'].get('failed') or failed['response'].get('converged') is True):
        raise ValueError('The pending changed-H failure does not belong to this inner')
    result = RawInnerBinding(raw_path, sidecar_path, failed_tail_path, r, side, failed,
                             plan_path, plan, anchor)
    result.check_files()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('raw', 'sidecar', 'failed-tail', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    args = parser.parse_args()
    binding = bind_raw_inner(args.raw, args.sidecar, args.failed_tail)
    value = binding.descriptor()
    value['command'] = [sys.executable, *sys.argv]
    with args.out.open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(output=ref(args.out), original_inner_success=True,
                         actual_coupled_terminal_accepted=False,
                         native_model_constructed=False, old_inner_rerun=False)))


if __name__ == '__main__':
    main()
