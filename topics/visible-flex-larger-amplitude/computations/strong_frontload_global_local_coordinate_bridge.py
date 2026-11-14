#!/usr/bin/env python3
"""Pay global/local affine input errors and the actual prefix/bridge dispatcher.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This is an exact-rational coordinate bridge for the existing unsolved warm
comparison. It does not assert differentiability of rounded evaluations or
pay interior libm, complete mean, Cartesian or nonlinear equation errors.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as F
import math
from pathlib import Path
import resource
import time
import numpy as np
import strong_frontload_provider_mask_overlap_bridge as old

HERE = Path(__file__).resolve().parent
PINS = {
    'strong_frontload_provider_mask_overlap_bridge.py':
        'c4191fab1a222d3dad04b1d18cd237f0c1a970b8188dc44403000080dc28c628',
}
DISPATCH_SHA = '0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5'
MASK_SHA = 'ea0922ae5acb791598b5348d379618c1de2fa8312670d179b2a4bc9f334ebba1'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('background', 'background-resource', 'mask', 'mask-resource', 'port', 'source-topic', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    a = parser.parse_args()
    if a.out.exists():
        raise FileExistsError(a.out)
    started = time.monotonic()
    gates = {}
    def check(name, condition):
        if not condition:
            raise ArithmeticError(name)
        gates[name] = True
    for name, digest in PINS.items():
        check('frozen_'+name, old.sha(HERE/name) == digest)
    bg, br, mask, mr, port = map(old.read, (a.background, a.background_resource, a.mask, a.mask_resource, a.port))
    check('actual_unsolved_background_identity', old.sha(a.background) == old.BG_SHA
          and bg['all_gates'] and not bg['accepted_new_solution'])
    check('actual_all_ten_mask_bands_identity', old.sha(a.mask) == MASK_SHA
          and mask['all_gates'] and mask['all_ten_internal_provider_mask_bands_paid'])
    for name, item in (('background', br), ('mask', mr)):
        check(name+'_owned_zero', item['exitcode'] == 0 and item['wait4_observed']
              and item['termination_signal'] is None)
    for name, digest in bg['frozen_source_sha256'].items():
        check('provider_dependency_'+name, old.sha(HERE/name) == digest)
    check('actual_same_port', old.sha(a.port) == bg['input_identities'][str(a.port)])
    dispatch = a.source_topic/'notes/fixed_metric_mode3_flow.py'
    check('original_dispatcher_source', old.sha(dispatch) == DISPATCH_SHA)
    text = dispatch.read_text()
    check('original_dispatcher_formula',
          's=np.atleast_1d(s);a,v,acc=self.prefix_profile(np.minimum(s,self.prefix_end))' in text
          and 'mask=s>self.prefix_end' in text
          and 'self.bridge.profile(s[mask]-self.prefix_end)' in text)
    provider = old.module('actual_global_local_provider', 'alternative-neck-provider.py')
    import strong_initial_speed_pulse as pulse
    import strong_monotone_initial_speed_anchor as frontload
    pulse.install(provider); frontload.install(provider)
    profile = bg['profiles'][0]
    cfg = profile['frozen_profile']
    prefix = provider.NeckPrefix(cfg)
    bridge = provider.NeckTerminalBridge(provider.tagged_port(port, cfg)['cut'])
    objects = {'prefix': prefix, 'bridge': bridge}
    p = old.binary(prefix.end)
    total = old.binary(float(prefix.end+bridge.end))
    check('bridge_global_subtraction_Sterbenz_domain', 0 < p < total < 2*p)
    shifts = {'prefix': F(0), 'bridge': p}
    records = profile['comparison_definition']['actual_binary_segments']
    pieces = profile['piece_rows']
    check('same_twelve_actual_segments', len(records) == len(prefix.segments)+len(bridge.segments) == 12)
    check('same_comparison_definition',
          mask['comparison_definition_sha256'] == profile['comparison_definition_sha256'])
    mask_by_segment = {r['segment']: r for r in mask['rows']}
    eps, eta = F(1, 2**52), F(16, 2**1022)
    rows = []
    for index, record in enumerate(records):
        comp = record['component']
        seg = record['original_binary_segment']
        shift = shifts[comp]
        check('live_binary_segment_'+str(index), objects[comp].segments[record['local_segment']] == seg)
        l, s0, s1 = map(old.binary, (seg['length'], seg['s0'], seg['s1']))
        g0, g1 = map(old.binary, (record['physical_start_binary'], record['physical_end_binary']))
        h = g1-g0
        check('positive_complete_affine_segment_'+str(index), l > 0 and h > 0)
        check('original_binary_global_endpoints_'+str(index),
              old.binary(float(shift)+float(s0)) == g0 and old.binary(float(shift)+float(s1)) == g1)
        check('original_exact_span_difference_'+str(index),
              h-l == old.q(record['exact_physical_length_minus_constructor_length']))
        z0 = (g0-shift-s0)/l
        z1 = (g1-shift-s0)/l
        ideal_error = max(abs(z0), abs(z1-1))
        sup_z = max(abs(z0), abs(z1))
        # First local subtraction is rounded; the bridge dispatcher
        # subtraction before it is exact by the displayed Sterbenz domain.
        arithmetic_error = ((1+eps)**2-1)*sup_z+(1+eps)*eta/l+eta
        clipped_error = old.up(ideal_error+arithmetic_error)
        check('finite_no_overflow_intermediate_hulls_'+str(index),
              max(abs(g0), abs(g1), abs(shift), abs(s0), abs(s1), l, sup_z) < 8
              and l*sup_z+eta < 8 and clipped_error < 1)
        selection = dict(component_dispatch_subtraction_exact=True)
        if record['local_segment'] > 0:
            raw_start = shift+s0
            before = old.binary(math.nextafter(float(g0), -math.inf))
            after = old.binary(math.nextafter(float(g0), math.inf))
            threshold = shift+old.binary(float(seg['s0']-1e-13))
            paid = mask_by_segment[index]
            check('reference_seam_adjacent_binary_bracket_'+str(index), before < raw_start < after)
            check('early_actual_activation_precedes_reference_seam_'+str(index), threshold < g0)
            check('same_full_early_mask_band_'+str(index),
                  old.q(paid['entire_overlap_global_interval'][0]) == threshold
                  and old.q(paid['entire_overlap_global_interval'][1]) == raw_start
                  and old.q(paid['exact_comparison_global_seam']) == g0)
            # For binary s<g0, s<=nextafter(g0,-inf)<raw_start. Thus a
            # selected later segment there has a nonpositive local input
            # and belongs to the already paid complete clipped-zero band.
            # At s=g0 its own affine bound applies, including either sign
            # of raw_start-g0. No continuum branch equality is assumed.
            selection.update(exact_raw_global_start=old.pack(raw_start),
                previous_global_binary=old.pack(before), next_global_binary=old.pack(after),
                reference_boundary=old.pack(g0), actual_mask_threshold=old.pack(threshold),
                any_earlier_binary_selected_input_in_existing_paid_mask_band=True,
                boundary_binary_point_uses_current_affine_bound=True)
        rows.append(dict(segment=index, component=comp, local_segment=record['local_segment'],
            exact_component_shift=old.pack(shift), exact_constructor_length=old.pack(l),
            exact_comparison_global_interval=[old.pack(g0),old.pack(g1)], exact_global_span=old.pack(h),
            exact_pre_round_normalized_endpoint_values=list(map(old.pack, (z0,z1))),
            exact_affine_input_difference_endpoint_max=old.pack(ideal_error),
            complete_local_subtraction_and_division_error=old.pack(old.up(arithmetic_error)),
            complete_clipped_normalized_input_difference=old.pack(clipped_error),
            induced_comparison_parameter_distance=old.pack(old.up(h*clipped_error)),
            exact_first_affine_chain_scale_difference=old.pack(abs(1/l-1/h)),
            exact_second_affine_chain_scale_difference=old.pack(abs(1/l**2-1/h**2)),
            branch_selection=selection))
    first_bridge = next(i for i,r in enumerate(records) if r['component'] == 'bridge')
    seam_piece = next(r for r in pieces if r['segment'] == first_bridge)
    check('dispatcher_seam_is_exact_comparison_seam', old.q(seam_piece['physical_interval'][0]) == p)
    values = [float(np.asarray(v).reshape(-1)[0]) for v in prefix.profile(np.asarray([float(p)],dtype=np.float64))]
    check('actual_original_prefix_endpoint_tuple_finite', np.isfinite(values).all())
    seam_errors = []
    for value, interval in zip(values, seam_piece['left_value_first_second']):
        lo, hi = map(old.dyadic, interval)
        seam_errors.append(old.up(max(abs(old.binary(value)-lo),abs(old.binary(value)-hi))))
    check('all_internal_mask_bands_referenced', len(mask_by_segment) == 10
          and sum(r['local_segment'] > 0 for r in rows) == 10)
    inputs = (a.background,a.background_resource,a.mask,a.mask_resource,a.port,dispatch)
    output = dict(schema='actual-frontload-global-local-coordinate-and-dispatch-bridge-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=old.sha(__file__),
        input_sha256={str(x):old.sha(x) for x in inputs}, frozen_sources=PINS,
        actual_profile=cfg, input_kind='completed-unsolved-warm', accepted_new_solution=False,
        completed_warm_screen_sha256=profile['completed_warm_screen_sha256'],
        comparison_definition_sha256=profile['comparison_definition_sha256'],
        arithmetic_model=dict(binary64_relative_bound=old.pack(eps),
            per_operation_absolute_underflow_bound=old.pack(eta),
            finite_no_overflow_verified=True, actual_inputs_are_binary64=True,
            no_rounded_function_differentiability_claim=True),
        dispatcher=dict(exact_prefix_end=old.pack(p),exact_global_end=old.pack(total),
            whole_bridge_subtraction_exact_by_Sterbenz=True,
            equality_branch_is_original_prefix=True, actual_prefix_endpoint_tuple=values,
            endpoint_supplied_jet_to_common_C2_seam=list(map(old.pack,seam_errors))),
        rows=rows, complete_segments=12,
        maximum_normalized_coordinate_error=max(float(old.q(r['complete_clipped_normalized_input_difference'])) for r in rows),
        maximum_induced_parameter_distance=max(float(old.q(r['induced_comparison_parameter_distance'])) for r in rows),
        coordinate_bounds_are_uniform_in_each_complete_binary_input_segment=True,
        early_selected_other_segment_bands_covered_by_existing_mask_certificate=True,
        interior_libm_dot_phase_jet_and_fullmean_costs_paid=False,
        supplied_interior_profile_C2_metric_closedD_or_reach_certified=False,
        gates=gates,gate_count=len(gates),all_gates=True,new_ODE_Node_Newton_or_full_field_calls=0,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(old.json.dumps(output,indent=2)+'\n')
    print(old.json.dumps(dict(out=str(a.out),sha256=old.sha(a.out),gates=len(gates),
        maximum_normalized_coordinate_error=output['maximum_normalized_coordinate_error'],
        maximum_induced_parameter_distance=output['maximum_induced_parameter_distance'],
        seam_jet_errors=list(map(float,seam_errors)))),flush=True)


if __name__ == '__main__':
    main()
