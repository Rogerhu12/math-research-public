#!/usr/bin/env python3
"""Pay the actual provider's ten internal mask-overlap bands.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original profile loop activates each later piece slightly before its
stored local start. On that complete overlap band clipping makes its input
exactly zero. Its actual endpoint tuple is therefore compared with the
already defined continuous C2 radius through complete first/second/third
derivative hulls. No new physical ODE or full geometry field is evaluated.
The prefix/bridge dispatcher and arbitrary interior libm calls are separate.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time
import numpy as np

HERE = Path(__file__).resolve().parent
BG_SHA = '01aa989aecc9959f10ce556052b90475d5e60c884b814c10811aef63fbadb5ac'
TABLE_SHA = '0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d'
BASE_SHA = '483b784c9c7aabde360aa04a06eea063b7dee8b1dadd0f0ae81f8be0d7f14e08'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def q(value):
    return F(value['numerator']) / F(value['denominator'])


def pack(value):
    value = F(value)
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def binary(value):
    return F.from_float(float(value))


def dyadic(value):
    return F(int(value[0])) * F(2) ** int(value[1])


def absolute_box(value):
    return max(abs(dyadic(value[0])), abs(dyadic(value[1])))


def up(value, bits=160):
    value = F(value) * (1 << bits)
    return F(-(-value.numerator // value.denominator), 1 << bits)


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('background', 'background-resource', 'table', 'port', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError(args.out)
    bg, owned, table, port = map(read, (args.background, args.background_resource, args.table, args.port))
    gates = {}

    def check(name, condition):
        if not condition:
            raise ArithmeticError(name)
        gates[name] = True

    check('same_completed_unsolved_background',
          sha(args.background) == BG_SHA and bg['all_gates'] and not bg['accepted_new_solution']
          and bg['input_kind'] == 'completed-unsolved-warm')
    check('owned_background_zero', owned['exitcode'] == 0 and owned['wait4_observed']
          and owned['termination_signal'] is None)
    check('same_table', sha(args.table) == TABLE_SHA and table['all_gates'])
    check('same_actual_port', sha(args.port) == bg['input_identities'][str(args.port)])
    for name, digest in bg['frozen_source_sha256'].items():
        check('pinned_'+name, sha(HERE/name) == digest)
    check('original_exact_phase_helper',
          sha(HERE/'strong_newg_binary_background_C2_comparison.py') == BASE_SHA)
    provider_source = (HERE/'alternative-neck-provider.py').read_text()
    check('original_mask_order_and_clip',
          "mask=(ss>=seg['s0']-1e-13)" in provider_source
          and "np.clip((ss[mask]-seg['s0'])/seg['length'],0.,1.)" in provider_source
          and 'for z,w in zip(out,jet):z[mask]=w' in provider_source)
    provider = module('actual_mask_overlap_provider', 'alternative-neck-provider.py')
    check('original_angle_hook_already_installed', getattr(provider, '_strong_angle_boost_installed', False))
    import strong_initial_speed_pulse as pulse
    import strong_monotone_initial_speed_anchor as frontload
    pulse.install(provider)
    frontload.install(provider)
    profile = bg['profiles'][0]
    cfg = profile['frozen_profile']
    prefix = provider.NeckPrefix(cfg)
    bridge = provider.NeckTerminalBridge(provider.tagged_port(port, cfg)['cut'])
    actual = {'prefix': prefix, 'bridge': bridge}
    shifts = {'prefix': F(0), 'bridge': binary(prefix.end)}
    records = profile['comparison_definition']['actual_binary_segments']
    for index, record in enumerate(records):
        live = actual[record['component']].segments[record['local_segment']]
        check('complete_live_segment_bits_'+str(index), live == record['original_binary_segment'])
    check('same_total_actual_segments', len(records) == len(prefix.segments)+len(bridge.segments) == 12)
    base = module('mask_overlap_phase_helper', 'strong_newg_binary_background_C2_comparison.py')
    weight_sum = sum((q(row['actual_normalized_binary_weight']) for row in table['root_weight_rows']), F(0))
    check('positive_complete_Gauss_mass', 0 < weight_sum < F(1001, 1000)
          and all(q(row['actual_normalized_binary_weight']) > 0 for row in table['root_weight_rows']))
    piece_rows = profile['piece_rows']
    caps = []
    for index, piece in enumerate(piece_rows):
        record = records[piece['segment']]
        seg = record['original_binary_segment']
        length = binary(seg['length'])
        physical_span = q(piece['physical_interval'][1])-q(piece['physical_interval'][0])
        global_segment_span = binary(record['physical_end_binary'])-binary(record['physical_start_binary'])
        if seg['kind'] == 'hermite':
            row = list(map(binary, seg['strong_initial_speed_frontload_radius_controls']))
            for unused in range(3):
                degree = len(row)-1
                row = [degree*(b-a)/global_segment_span for a, b in zip(row, row[1:])]
            primitive_third = max(map(abs, row))
        else:
            lo, hi, phi = base.phase_pieces(seg)[piece['phase_piece']]
            span = hi-lo
            check('piece_physical_affine_identity_'+str(index), physical_span == global_segment_span*span)
            normalized = base.affine_poly(phi, lo, span)
            derivatives = []
            row = normalized
            for unused in range(3):
                row = base.derivative(row)
                derivatives.append(sum(map(abs, row), F(0)))
            d1, d2, d3 = derivatives
            sin_second = d1*d1+d2
            sin_third = d1**3+3*d1*d2+d3
            primitive_third = length*span/(physical_span**3)*weight_sum*(3*sin_second+sin_third)
        gaps = list(map(absolute_box, piece['next_left_minus_current_right']))
        # Degree-two Bernstein hulls of H0''',H1''',H2''' are bounded
        # by 120,60,18. The second-jet coefficient is h^2*gap2/2.
        correction_third = (120*gaps[0]/physical_span**3
                            + 60*gaps[1]/physical_span**2 + 9*gaps[2]/physical_span)
        repairs = list(map(dyadic, piece['quintic_repair_uniform_C0_C1_C2_upper']))
        first = dyadic(piece['continuous_first_absolute_upper'])+repairs[1]
        second = dyadic(piece['continuous_second_absolute_upper'])+repairs[2]
        third = primitive_third+correction_third
        check('complete_piece_derivative_hulls_'+str(index), all(x >= 0 for x in (first, second, third)))
        caps.append((up(first), up(second), up(third)))
    results = []
    for index, record in enumerate(records):
        if record['local_segment'] == 0:
            continue
        component = record['component']
        seg = record['original_binary_segment']
        start = binary(seg['s0'])
        threshold_float = float(seg['s0']-1e-13)
        threshold = binary(threshold_float)
        check('nonempty_local_tolerance_band_'+str(index), 0 < start-threshold < F(1, 10**12))
        obj = actual[component]
        if record['local_segment']+1 < len(obj.segments):
            later = obj.segments[record['local_segment']+1]
            check('no_later_mask_can_overwrite_'+str(index),
                  binary(float(later['s0']-1e-13)) > start)
        # On every binary local s in this interval, subtraction/division
        # is nonpositive, hence clipping yields exactly zero. This is a
        # complete sign argument, not a sample interpolation assertion.
        endpoint = provider.piece_jet(seg, np.asarray([0.], dtype=np.float64))
        values = [float(np.asarray(value).reshape(-1)[0]) for value in endpoint]
        check('three_finite_actual_endpoint_values_'+str(index), np.isfinite(values).all())
        right_index = next(j for j, row in enumerate(piece_rows) if row['segment'] == index)
        left_index = right_index-1
        right_piece = piece_rows[right_index]
        left_piece = piece_rows[left_index]
        seam = q(right_piece['physical_interval'][0])
        lo = shifts[component]+threshold
        hi = shifts[component]+start
        displacement = max(abs(lo-seam), abs(hi-seam))
        check('complete_global_band_inside_two_adjacent_pieces_'+str(index),
              q(left_piece['physical_interval'][0]) <= lo
              and hi <= q(right_piece['physical_interval'][1])
              and q(left_piece['physical_interval'][1]) == seam
              and displacement < F(1, 10**12))
        endpoint_errors = []
        for k, value in enumerate(values):
            lower, upper = map(dyadic, right_piece['left_value_first_second'][k])
            endpoint_errors.append(max(abs(binary(value)-lower), abs(binary(value)-upper)))
        derivative_caps = [max(caps[left_index][k], caps[right_index][k]) for k in range(3)]
        complete_errors = [up(e+displacement*c) for e, c in zip(endpoint_errors, derivative_caps)]
        results.append(dict(
            segment=index, component=component, local_segment=record['local_segment'],
            exact_binary_threshold=pack(threshold), exact_binary_local_start=pack(start),
            exact_component_shift=pack(shifts[component]),
            exact_comparison_global_seam=pack(seam),
            entire_overlap_global_interval=[pack(lo), pack(hi)],
            maximum_seam_displacement=pack(displacement),
            actual_constant_clipped_input=0., actual_provider_endpoint_tuple=values,
            actual_endpoint_to_comparison_seam_jet=list(map(pack, endpoint_errors)),
            adjacent_complete_comparison_derivative_caps_1_2_3=list(map(pack, derivative_caps)),
            complete_overlap_supplied_jet_to_C2_comparison_bounds=list(map(pack, complete_errors)),
            complete_band_covered_by_sign_and_Lipschitz_argument=True))
    check('all_ten_internal_component_mask_bands',
          len(results) == 10 and sum(row['component'] == 'prefix' for row in results) == 8
          and sum(row['component'] == 'bridge' for row in results) == 2)
    maxima = [max(q(row['complete_overlap_supplied_jet_to_C2_comparison_bounds'][k]) for row in results)
              for k in range(3)]
    check('finite_actual_band_bounds', all(0 <= x < F(1, 1000) for x in maxima))
    inputs = (args.background, args.background_resource, args.table, args.port)
    output = dict(
        schema='actual-frontload-provider-internal-mask-overlap-C2-bridge-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
        input_sha256={str(path): sha(path) for path in inputs},
        frozen_source_sha256=bg['frozen_source_sha256'], frozen_phase_helper_sha256=BASE_SHA,
        input_kind='completed-unsolved-warm', warm_screen_sha256=profile['completed_warm_screen_sha256'],
        actual_profile=cfg, comparison_definition_sha256=profile['comparison_definition_sha256'],
        complete_comparison_piece_derivative_caps_1_2_3=[list(map(pack, row)) for row in caps],
        rows=results, maximum_complete_overlap_supplied_jet_bounds=list(map(pack, maxima)),
        all_ten_internal_provider_mask_bands_paid=True,
        sign_and_continuous_derivative_bounds_not_sampling=True,
        actual_provider_zero_endpoint_calls=10, new_full_geometry_fields=0,
        prefix_to_bridge_dispatcher_or_material_chart_rounding_paid=False,
        other_interior_libm_or_fullmean_or_Cartesian_geometry_certified=False,
        rounded_function_C2_or_original_candidate_modified=False,
        new_accepted_solution_or_closed_D_or_reach_claimed=False,
        gates=gates, gate_count=len(gates), all_gates=True,
        new_ODE_Node_Newton_calls=0, elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out), gates=len(gates), bands=len(results),
                         uniform_jet_bounds=[float(x) for x in maxima])), flush=True)


if __name__ == '__main__':
    main()
