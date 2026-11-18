#!/usr/bin/env python3
"""Bind a complete M8 partial-path physical graph to its exact returned inner.

The physical reader already supports each declared 0<lambda<1 path. This
adapter uses explicit returned-raw/sidecar references, never a filename search
or a normalized-coordinate inverse. Metadata binding evaluates no equation.
Optional restore() creates the same current model, verifies its forward chart
on the saved normalized mesh, and restores the original raw cubic/node tuple
separately from the saved physical quintic. No initial projection, mean,
metric, BVP or tail solve is performed.
"""
from dataclasses import dataclass
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
from types import SimpleNamespace

from m3_trace_path_prefix import (bind_checkpoint, check_plan, checked_file,
    exact_numbers, load, payload_sha, ref, sha)


def flatten(value):
    if isinstance(value, list):
        for item in value:
            yield from flatten(item)
    else:
        yield value


def array_hash(value):
    digest = hashlib.sha256()
    for item in flatten(value):
        if isinstance(item, bool) or not isinstance(item, (int, float)) or not math.isfinite(item):
            raise ValueError('An original raw numerical array contains a nonfinite/nonnumber')
        digest.update(struct.pack('<d', float(item)))
    return digest.hexdigest()


@dataclass(frozen=True)
class ReturnedInnerBinding:
    physical: object
    raw_path: Path
    sidecar_path: Path
    raw: dict
    sidecar: dict
    raw_plan: dict
    raw_reference: dict
    sidecar_reference: dict
    reference_convention: str
    adapter_sha256: str

    def check_files(self):
        self.physical.check_files()
        checked_file(self.raw_reference)
        checked_file(self.sidecar_reference)
        checked_file(self.raw['plan'])
        checked_file(self.sidecar['actual_tail_record'])
        check_plan(self.raw['plan']['path'])
        if sha(__file__) != self.adapter_sha256:
            raise ValueError('This returned-inner adapter changed')

    def descriptor(self):
        cp, raw = self.physical.record, self.raw
        return dict(scope=__doc__, adapter=ref(__file__),
            physical_checkpoint=ref(self.physical.checkpoint), physical_plan=ref(self.physical.plan_path),
            original_returned_raw=self.raw_reference, original_raw_sidecar=self.sidecar_reference,
            raw_reference_convention=self.reference_convention,
            raw_execution_plan=raw['plan'], original_inner_index=raw['inner'],
            inner_affine_anchor=self.sidecar['actual_tail_record'],
            inner_affine_response_payload_sha256=self.sidecar['response_payload_sha256'],
            final_physical_seam_record=ref(self.physical.tail_record),
            path_lambda=cp['path_lambda'], q_gauge=cp['q_gauge'], q_support=cp['seed_support_amplitude'],
            path_base_profile=cp['path_base_profile'], final_profile=cp['frozen_profile'],
            complete_parameters=raw['p'], complete_parameter_scales=raw['parameter_scales'],
            complete_physical_controls=raw['original_physical_controls'],
            normalized_nodes=len(raw['x']), state_components=len(raw['y']),
            original_RMS_entries=len(raw['rms_residuals']), original_max_RMS=max(raw['rms_residuals']),
            original_status=raw['status'], original_message=raw['message'], original_niter=raw['niter'],
            original_solver_success=raw['solver_success'],
            array_binary64_sha256={key: array_hash(raw[key]) for key in ('x', 'y', 'p', 'rms_residuals')},
            raw_cubic_knots_binary64_sha256=array_hash(raw['raw_cubic']['x']),
            raw_cubic_coefficients_binary64_sha256=array_hash(raw['raw_cubic']['c']),
            original_cubic_axis=raw['raw_cubic']['axis'], original_cubic_extrapolate=raw['raw_cubic']['extrapolate'],
            original_pending_node_H=raw['candidate_cut_height'],
            state_scope='Raw normalized cubic, original node y and complete RMS remain separate from the physical quintic. Evaluating the latter on the physical mesh is not relabeled as original raw y.',
            anchor_scope='The saved inner sidecar is its old actual response used as an affine anchor, not necessarily the response for its returned candidate H or the physical seam H.',
            restore_scope='A forward chart check is required on explicit restore. External extrapolation of the original cubic is disabled; original sol.yp was not saved and is not manufactured.',
            missing_original_fields=['yp'], native_model_constructed=False,
            forward_chart_evaluated=False, new_initial_projection=False,
            mean_metric_BVP_or_tail_evaluated=False, fixed_g_refinement_claim=False)

    def restore(self):
        """Restore in a fresh process; do not solve or infer a DN response."""
        self.check_files()
        import numpy as np
        from scipy.interpolate import PPoly
        current = self.physical.native_prefix()
        raw = self.raw
        x = np.asarray(raw['x'], float)
        y = np.asarray(raw['y'], float)
        p = np.asarray(raw['p'], float)
        physical_x = current.obj.chart(x, p[0])[0]
        if (not exact_numbers(physical_x, current.solution.x) or
                not exact_numbers(p, current.solution.p) or
                not exact_numbers(current.obj.bridge.sigma*current.obj.q*y[current.obj.iz:, -1],
                                  raw['candidate_cut_height'])):
            raise ValueError('Saved normalized/physical chart or complete pending H differs')
        cubic = PPoly.construct_fast(np.asarray(raw['raw_cubic']['c'], float),
            np.asarray(raw['raw_cubic']['x'], float), extrapolate=False, axis=1)
        original = SimpleNamespace(x=x, y=y, p=p, sol=cubic,
            success=raw['solver_success'], status=raw['status'], message=raw['message'],
            niter=raw['niter'], rms_residuals=np.asarray(raw['rms_residuals'], float))
        if hasattr(current.obj, 'tail'):
            raise ValueError('No affine or stale actual tail may be silently attached')
        self.check_files()
        return SimpleNamespace(physical_prefix=current, original_solution=original,
            original_inner_sidecar=self.sidecar, source_binding=self.descriptor(),
            forward_chart_binary64_equal=True, original_sol_yp_available=False,
            actual_tail_attached=False, new_equation_solve=False)


def bind_returned_inner(checkpoint):
    physical = bind_checkpoint(checkpoint)
    cp = physical.record
    if 'accepted_raw_inner' in cp or 'accepted_raw_sidecar' in cp:
        if not all(key in cp for key in ('accepted_raw_inner', 'accepted_raw_sidecar')):
            raise ValueError('Both explicit returned-inner references are required')
        raw_ref, side_ref = cp['accepted_raw_inner'], cp['accepted_raw_sidecar']
        convention = 'explicit accepted_raw_inner and accepted_raw_sidecar'
    elif 'saved_inner_resume' in cp:
        # The first actual lambda=.02 checkpoint predates the generic keys.
        saved = cp['saved_inner_resume']
        raw_ref, side_ref = saved['raw_inner'], saved['raw_sidecar']
        convention = 'first saved-inner-resume explicit raw_inner and raw_sidecar'
    else:
        raise ValueError('No explicit original returned-inner references; do not search or invent them')
    raw_path, sidecar_path = checked_file(raw_ref), checked_file(side_ref)
    raw, side = load(raw_path), load(sidecar_path)
    raw_plan = check_plan(checked_file(raw['plan']))
    if (side['raw'] != raw_ref or side['plan'] != raw['plan'] or
            raw['stage'] != 'immediately_after_original_solve_bvp' or
            raw['solver_success'] is not True or raw['status'] != 0 or
            raw['cubic_available'] is not True or
            raw_plan['design'] != physical.plan['design']):
        raise ValueError('The complete real returned inner/sidecar is not this physical design')
    for key in ('core_kind', 'core_control_path', 'path_definition', 'path_lambda',
                'q_gauge', 'seed_support_amplitude', 'partial_lift_strength',
                'lift_window', 'path_base_profile', 'core_round_settings'):
        if raw[key] != cp[key]:
            raise ValueError('Raw and physical defining metadata differ: '+key)
    for raw_key, physical_key in (('p', 'parameters'), ('parameter_scales', 'central_correction_scales'),
                                  ('original_physical_controls', 'physical_controls')):
        if not exact_numbers(raw[raw_key], cp[physical_key]):
            raise ValueError('The complete original physical parameters differ')
    n = len(raw['x'])
    cubic = raw['raw_cubic']
    if (n != cp['nodes'] or len(raw['y']) != 25 or any(len(row) != n for row in raw['y']) or
            len(raw['p']) != 8 or len(raw['rms_residuals']) != n-1 or
            raw['x'][0] != 0. or raw['x'][-1] != 1. or
            not all(x < y for x, y in zip(raw['x'], raw['x'][1:])) or
            cubic['axis'] != 1 or not exact_numbers(cubic['x'], raw['x']) or
            len(cubic['c']) != 4 or any(len(row) != n-1 for row in cubic['c']) or
            any(len(vector) != 25 for row in cubic['c'] for vector in row) or
            max(raw['rms_residuals']) != cp['max_rms_collocation_residual'] or
            raw['message'] != cp['message']):
        raise ValueError('The original full normalized cubic/node/RMS tuple is incomplete')
    for value in (raw['x'], raw['y'], raw['p'], raw['rms_residuals'], cubic['c']):
        array_hash(value)
    actual = load(checked_file(side['actual_tail_record']))
    if (actual['source_sha256'] != raw_plan['native_tail_source_sha256'] or
            actual['request']['jacobian'] is not True or actual['request']['audit'] is not True or
            actual['response'].get('converged') is not True or
            not exact_numbers(actual['request']['height'], side['height']) or
            payload_sha(actual['response']) != side['response_payload_sha256']):
        raise ValueError('The old actual inner affine anchor was not retained faithfully')
    result = ReturnedInnerBinding(physical, raw_path, sidecar_path, raw, side, raw_plan,
        raw_ref, side_ref, convention, sha(__file__))
    result.check_files()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    bound = bind_returned_inner(args.checkpoint)
    with args.out.open('x') as stream:
        json.dump(bound.descriptor(), stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.out), metadata_only=True,
                         lambda_value=bound.raw['path_lambda'], native_model_constructed=False)), flush=True)


if __name__ == '__main__':
    main()
