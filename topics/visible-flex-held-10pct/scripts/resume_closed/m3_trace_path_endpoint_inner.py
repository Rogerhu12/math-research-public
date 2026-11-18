#!/usr/bin/env python3
"""Bind a real successful M8 lambda=1 returned inner before its pending tail.

Use explicit raw/sidecar/failure files and the endpoint reader's exact lambda
and literal_R44_endpoint dispatch. Preserve the historical wire kind, all
eight physical parameters, seven controls/scales, base+p0, cubic and full RMS.
Metadata binding evaluates no equations. native_model() restores the actual
full-lift endpoint model but invokes no inner solve, mean, C2 export or DN.
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

from m3_trace_path_endpoint import (KIND, CONTROL_PATH, M3, checked_file,
    check_plan, exact_numbers, load, payload_sha, ref, sha)


def flat(value):
    if isinstance(value, list):
        for item in value:
            yield from flat(item)
    else:
        yield value


def array_hash(values):
    result = hashlib.sha256()
    for value in flat(values):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError('A complete saved array must contain only finite numbers')
        result.update(struct.pack('<d', float(value)))
    return result.hexdigest()


@dataclass(frozen=True)
class PendingInnerBinding:
    raw_path: Path
    sidecar_path: Path
    failed_tail_path: Path
    raw_reference: dict
    sidecar_reference: dict
    failed_tail_reference: dict
    raw: dict
    sidecar: dict
    failed_tail: dict
    plan_path: Path
    plan: dict
    old_actual_anchor: dict
    adapter_sha256: str

    def check_files(self):
        for item in (self.raw_reference, self.sidecar_reference, self.failed_tail_reference,
                     self.raw['plan'], self.sidecar['actual_tail_record']):
            checked_file(item)
        check_plan(self.plan_path)
        if sha(__file__) != self.adapter_sha256:
            raise ValueError('The pending-inner adapter changed')

    def descriptor(self):
        r, d = self.raw, self.plan['design']
        physical_profile = copy.deepcopy(r['path_base_profile'])
        physical_profile['delta'] += r['p'][0]
        return dict(scope=__doc__, adapter=ref(__file__), raw_inner=self.raw_reference,
            sidecar=self.sidecar_reference, original_runtime_plan=ref(self.plan_path),
            failed_pending_tail=self.failed_tail_reference,
            old_inner_actual_anchor=self.sidecar['actual_tail_record'],
            old_inner_affine_response_payload_sha256=self.sidecar['response_payload_sha256'],
            original_inner_index=r['inner'], remaining_original_outer_indices=list(range(r['inner'], 8)),
            path_lambda=r['path_lambda'], q_gauge=r['q_gauge'], q_support=r['seed_support_amplitude'],
            core_settings=r['core_round_settings'], path_definition=r['path_definition'],
            endpoint_dispatch=dict(lambda_value=1., branch='literal_R44_endpoint', full_lift_strength=1.),
            lift_window=r['lift_window'], path_base_profile=r['path_base_profile'],
            returned_physical_profile=physical_profile,
            parameters=r['p'], parameter_scales=r['parameter_scales'], physical_controls=r['original_physical_controls'],
            nodes=len(r['x']), state_components=len(r['y']), original_rms_entries=len(r['rms_residuals']),
            original_max_rms=max(r['rms_residuals']), original_solver_success=r['solver_success'],
            original_status=r['status'], original_message=r['message'], original_niter=r['niter'],
            raw_array_binary64_sha256={key: array_hash(r[key]) for key in ('x', 'y', 'p', 'rms_residuals')},
            raw_cubic_binary64_sha256=array_hash(r['raw_cubic']['c']),
            cubic_knots_binary64_sha256=array_hash(r['raw_cubic']['x']),
            original_cubic_axis=r['raw_cubic']['axis'], original_cubic_extrapolate=r['raw_cubic']['extrapolate'],
            old_affine_H=self.sidecar['height'], returned_candidate_H=r['candidate_cut_height'],
            returned_candidate_H_binary64_sha256=array_hash(r['candidate_cut_height']),
            pending_request=self.failed_tail['request'],
            pending_failure_last_iteration=self.failed_tail['response'].get('lastIteration'),
            physical_design_original_reference=d['original_reference_checkpoint'],
            scope_of_anchor='Old genuine response used inside the affine inner problem only. It is not relabeled as the failed returned-candidate response.',
            resume_point='Immediately after the successful original inner return, before its pending actual-tail response/actual BC/history row.',
            original_solution_missing_fields=['yp'], restored_cubic_domain_only=True,
            native_model_constructed=False, physical_CP_required=False,
            inner_solver_repeated=False, tail_solver_invoked=False,
            mean_metric_or_C2_export_invoked=False)

    def native_model(self):
        self.check_files()
        import numpy as np
        from scipy.interpolate import PPoly
        from q060_cosine_reference import bind_reference
        d, r = self.plan['design'], self.raw
        original = load(checked_file(d['original_reference_binding']))
        bound = bind_reference(original['checkpoint']['path'], original['terminal_record']['path'],
                               original['source_topic'], original['short_bridge']['path'])
        native = bound.native_reference()
        sys.path.insert(0, str(M3))
        from m3_circle_trace_path_model import CircleTracePathEnvironment
        if r['path_base_profile'] != bound.record['frozen_profile']:
            raise ValueError('A changed base profile requires an explicit coordinate transfer')
        environment = CircleTracePathEnvironment(bound, native, copy.deepcopy(r['core_round_settings']))
        obj = environment.make(r['path_lambda'], r['seed_support_amplitude'])
        p = np.asarray(r['p'], float)
        obj.initial(p)
        flow = obj.flow(float(p[0]))
        if (obj.cfg != r['path_base_profile'] or obj.path_definition != r['path_definition'] or
                not exact_numbers(obj.pscale, r['parameter_scales']) or
                not exact_numbers(obj.pscale*p[1:], r['original_physical_controls']) or
                flow.exact_lift_core is not obj._core or hasattr(obj, 'tail')):
            raise ValueError('The actual complete partial-path model was not restored faithfully')
        x, y = np.asarray(r['x'], float), np.asarray(r['y'], float)
        cubic = PPoly.construct_fast(np.asarray(r['raw_cubic']['c'], float),
            np.asarray(r['raw_cubic']['x'], float), extrapolate=False, axis=1)
        solution = SimpleNamespace(x=x, y=y, p=p, sol=cubic,
            success=r['solver_success'], status=r['status'], message=r['message'],
            niter=r['niter'], rms_residuals=np.asarray(r['rms_residuals'], float))
        if not exact_numbers(obj.bridge.sigma*obj.q*y[obj.iz:, -1], r['candidate_cut_height']):
            raise ValueError('The restored complete pending height differs')
        self.check_files()
        return SimpleNamespace(obj=obj, flow=flow, solution=solution, environment=environment,
            original_cosine_reference=native, source_binding=self.descriptor(),
            pending_request=copy.deepcopy(self.failed_tail['request']),
            completed_inner_index=r['inner'], next_inner_index=r['inner']+1,
            original_sol_yp_available=False, actual_tail_attached=False)


def bind_pending_inner(raw_path, sidecar_path, failed_tail_path):
    raw_path, sidecar_path, failed_tail_path = (Path(p).resolve() for p in
                                              (raw_path, sidecar_path, failed_tail_path))
    raw, side, failed = map(load, (raw_path, sidecar_path, failed_tail_path))
    plan_path = checked_file(raw['plan'])
    plan = check_plan(plan_path)
    d = plan['design']
    if (side['raw'] != ref(raw_path) or side['plan'] != raw['plan'] or
            raw['stage'] != 'immediately_after_original_solve_bvp' or
            raw['solver_success'] is not True or raw['status'] != 0 or raw['cubic_available'] is not True or
            isinstance(raw['inner'], bool) or not isinstance(raw['inner'], int) or not 0 <= raw['inner'] < 8):
        raise ValueError('A genuine complete successful original inner return is required')
    if (raw['core_kind'] != KIND or raw['core_control_path'] != CONTROL_PATH or
            raw['path_base_profile'] != d['physical_profile'] or
            raw['core_round_settings'] != d['new_core_settings'] or
            raw['path_lambda'] != d['lambda_value'] or raw['partial_lift_strength'] != d['lambda_value'] or
            raw['lift_window'] != [.5, .9] or raw['q_gauge'] != .06 or
            raw['seed_support_amplitude'] != d['new_q']['q_binary64'] or
            not exact_numbers(raw['parameter_scales'], plan['initial_parameter_scales'])):
        raise ValueError('The full original path/profile/gauge/support definition differs')
    definition = raw['path_definition']
    if (definition['branch'] != 'literal_R44_endpoint' or
            definition['settings'] != raw['core_round_settings'] or
            definition['lambda_value'] != raw['path_lambda'] or
            definition['numerical_gauge'] != .06 or definition['warp_reference'] != .06 or
            definition['defining_support_amplitude'] != raw['seed_support_amplitude'] or
            definition['fixed_metric'] is not False or
            not exact_numbers(definition['parameter_scales'], raw['parameter_scales'])):
        raise ValueError('The actual defining integral/partial-lift path metadata is incomplete')
    n, cubic = len(raw['x']), raw['raw_cubic']
    if (len(raw['y']) != 25 or any(len(row) != n for row in raw['y']) or
            len(raw['p']) != 8 or len(raw['parameter_scales']) != 7 or
            len(raw['original_physical_controls']) != 7 or len(raw['rms_residuals']) != n-1 or
            raw['x'][0] != 0. or raw['x'][-1] != 1. or
            not all(x < y for x, y in zip(raw['x'], raw['x'][1:])) or
            not exact_numbers([raw['p'][j+1]*raw['parameter_scales'][j] for j in range(7)],
                              raw['original_physical_controls']) or
            cubic['axis'] != 1 or not exact_numbers(cubic['x'], raw['x']) or
            len(cubic['c']) != 4 or any(len(row) != n-1 for row in cubic['c']) or
            any(len(vector) != 25 for row in cubic['c'] for vector in row)):
        raise ValueError('The original full node/parameter/cubic/RMS tuple is incomplete')
    for item in (raw['x'], raw['y'], raw['p'], raw['rms_residuals'], cubic['c']):
        array_hash(item)
    old = load(checked_file(side['actual_tail_record']))
    response = old['response']
    if (old['source_sha256'] != plan['native_tail_source_sha256'] or
            old['request']['jacobian'] is not True or old['request']['audit'] is not True or
            response.get('converged') is not True or not math.isfinite(response['residual']) or
            not response['residual'] < 2e-9 or response.get('audit') is None or
            len(response['heightJetJacobian']) != 208 or
            not all(math.isfinite(x) for x in response['heightJetJacobian']) or
            not exact_numbers(old['request']['height'], side['height']) or
            payload_sha(response) != side['response_payload_sha256']):
        raise ValueError('The old genuine complete inner affine anchor differs')
    if (failed['source_sha256'] != plan['native_tail_source_sha256'] or
            failed['config'] != load(checked_file(plan['tail_config'])) or
            failed['request']['jacobian'] is not True or failed['request']['audit'] is not True or
            not exact_numbers(failed['request']['height'], raw['candidate_cut_height']) or
            failed['response'].get('converged') is True or not failed['response'].get('failed')):
        raise ValueError('The explicit failed pending request is not this original returned inner H')
    result = PendingInnerBinding(raw_path, sidecar_path, failed_tail_path,
        ref(raw_path), ref(sidecar_path), ref(failed_tail_path), raw, side, failed,
        plan_path, plan, old, sha(__file__))
    result.check_files()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('raw', 'sidecar', 'failed-tail', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    args = parser.parse_args()
    bound = bind_pending_inner(args.raw, args.sidecar, args.failed_tail)
    with args.out.open('x') as stream:
        json.dump(bound.descriptor(), stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(binding=ref(args.out), lambda_value=bound.raw['path_lambda'],
                         original_inner=bound.raw['inner'], metadata_only=True,
                         native_model_constructed=False)), flush=True)


if __name__ == '__main__':
    main()
