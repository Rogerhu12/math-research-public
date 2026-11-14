#!/usr/bin/env python3
"""Restrict the paid finite-middle causal kernels to a genuine shared strip.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All comparisons use exact fractions.  The fixed low46 centre, both true head
columns, all 2833 positive even modes and the complete mean/inverse are kept.
The output concerns the projected finite-middle equation, not low/high/cut
feedback.  The common variable strip and all 10793 leaves are unchanged.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
import math
from pathlib import Path
import resource
import time


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == '.gz' else raw)


def ex(value):
    if isinstance(value, list):
        return F(int(value[0])) * F(2) ** int(value[1])
    if 'upper' in value:
        return ex(value['upper'])
    if 'mantissa' in value:
        return F(int(value['mantissa'])) * F(2) ** int(value['binary_exponent'])
    return F(int(value['numerator']), int(value['denominator']))


def rec(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                display_only=float(value))


def up96(value):
    if value <= 0:
        raise ArithmeticError('A strictly positive radius or metric weight is required')
    unit = F(2) ** (value.numerator.bit_length() - value.denominator.bit_length() - 96)
    return (value // unit + 1) * unit


def named_hash(mapping, name):
    values = [v for k, v in mapping.items() if Path(k).name == name]
    if len(values) != 1:
        raise ValueError('Exactly one input identity is required for ' + name)
    return values[0]


def main():
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--window-prefix', action='append', type=Path, required=True)
    for name in ('producer', 'coefficients', 'balanced', 'head', 'spectral',
                 'source', 'source-resource', 'out-prefix', 'common-strip', 'common-resource'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--high-cutoff', type=int, required=True)
    args = parser.parse_args()
    output = Path(str(args.out_prefix) + '.json.gz')
    summary_path = Path(str(args.out_prefix) + '-summary.json')
    if output.exists() or summary_path.exists():
        raise FileExistsError('Use a fresh full-middle budget output')
    balanced, head, spectral, source, source_resource, coeff = [read(getattr(args, n))
        for n in ('balanced', 'head', 'spectral', 'source', 'source_resource', 'coefficients')]
    source_hash = digest(args.producer)
    coeff_hash = digest(args.coefficients)
    B = ex(balanced['balanced_B_lower'])
    delta = ex(balanced['exact_head_to_output_strip_gap_lower'])
    bands = head['complete_coarse_trace_rows']['head']['high_bands_value_upper']
    Hnear, Hrest = ex(bands[0]), ex(bands[1])
    centre_mass = ex(source['complete_middle_shared_mass'])
    strip = next(row for row in coeff['phase_cases'] if row['energy_groups'] == [[10, 3]])
    gates = dict(
        paid_complete_shared_coefficients=coeff['all_coefficient_gates'] and coeff['original_panels'] == 10793,
        paid_complete_balanced_head=balanced['all_gates'] and all(balanced['gates'].values()),
        paid_complete_true_head=head['all_gates'] and all(head['gates'].values()),
        same_true_head_identity=named_hash(balanced['input_hashes'], args.head.name) == digest(args.head),
        balanced_near_mass_matches_true_head=ex(balanced['complete_shared_near_band_mass']) == Hnear,
        positive_actual_B_and_head_strip_gap=B > 0 and delta > 0,
        paid_complete_low46_centre=spectral['all_gates'] and all(spectral['gates'].values()) and ex(spectral['final_field_norm']) < 10,
        same_centre_source_identity=named_hash(source['input_hashes'], args.spectral.name) == digest(args.spectral),
        paid_complete_middle_source=source['all_gates'] and all(source['gates'].values()),
        complete_source_formal_exit_zero=source_resource['exitcode'] == 0 and source_resource['termination_signal'] is None,
        all_source_tail_mass_included=source['tail_mass_must_be_paid_once_across_any_joint_partition'],
        same_source_and_initial_strip=source['constant_strip'] == '18/125',
        fixed_whole_domain_strip_above_one_over64=ex(strip['terminal_strip']) > F(1, 64),
    )
    if not all(gates.values()):
        raise ArithmeticError('An input identity or complete domain gate failed: ' + str(gates))

    common = read(args.common_strip)
    common_resource = read(args.common_resource)
    if not common['all_identity_gates'] or not all(common['gates'].values()) or common_resource['exitcode'] != 0 or common_resource['termination_signal'] is not None:
        raise ArithmeticError('The exact common-strip primary must be complete and formally successful')
    if named_hash(common['input_hashes'], args.coefficients.name) != coeff_hash:
        raise ValueError('The common strip must use the identical original hybrid coefficients')
    shared_case = next(row for row in common['cases'] if row['high_threshold'] == args.high_cutoff)
    if not shared_case['common_strip_strictly_above_one_over64'] or not ex(shared_case['common_terminal_strip']) > F(1, 64) or not shared_case['both_additional_losses_nondecreasing']:
        raise ArithmeticError('A genuine common positive strip with monotone added losses is required')
    extra_start = [ex(r['extra_start']) for r in shared_case['blocks']]
    extra_end = [ex(r['extra_end']) for r in shared_case['blocks']]
    if len(extra_start) != 25 or any(extra_start[i] > extra_end[i] or (i and extra_end[i-1] != extra_start[i]) for i in range(25)):
        raise ArithmeticError('All25 original causal blocks must have the same monotone added loss')
    @lru_cache(maxsize=4096)
    def decay_upper(z):
        if z < 0:
            raise ArithmeticError('No negative analytic-strip gap is free')
        if z == 0:
            return F(1)
        # e^z >= (1+z/65536)^65536.  Every reciprocal/square
        # below is rounded upward on an exact96-bit dyadic grid.
        d = min(F(1), up96(1 / (1 + z / 65536)))
        for _ in range(16):
            d = min(F(1), up96(d * d))
        return d
    count = 25
    G = {p: [[F(0) for j in range(i + 1)] for i in range(count)] for p in (2, 1, 0)}
    where = {p: [[None for j in range(i + 1)] for i in range(count)] for p in (2, 1, 0)}
    head_gains = {band: [F(0) for i in range(count)] for band in ('near', 'rest')}
    head_where = {band: [None for i in range(count)] for band in ('near', 'rest')}
    Vmax = [None] * count
    partition = None
    windows = []
    identities = {}
    runs = []
    diagnostics = []
    coefficient_inputs = None
    for prefix in args.window_prefix:
        primary = Path(str(prefix) + '-windows.jsonl.gz')
        meta_path = Path(str(prefix) + '.json')
        resource_path = Path(str(prefix) + '-resource.json')
        meta, usage = read(meta_path), read(resource_path)
        if not (meta['all_enclosure_gates'] and meta['source_sha256'] == source_hash
                and meta['precision'] >= 256 and meta['same_fixed_strip'] == strip
                and meta['source_powers'] == [2, 1, 0]
                and meta['original_leaf_count_per_window'] == 10793
                and meta['original_source_groups'] == 18
                and meta['comparison_source_blocks'] == 25
                and meta['energy_segment_subblocks'] == 8
                and meta['primary']['sha256'] == digest(primary)
                and meta['primary']['bytes'] == primary.stat().st_size
                and named_hash(meta['input_hashes'], args.coefficients.name) == coeff_hash
                and usage['exitcode'] == 0 and usage['termination_signal'] is None
                and usage['peak_rss_kib'] <= 98304):
            raise ArithmeticError('A completed original whole-leaf window gate failed: ' + str(prefix))
        if partition is None:
            partition = meta['comparison_partition']
            coefficient_inputs = meta['input_hashes']
        elif partition != meta['comparison_partition'] or coefficient_inputs != meta['input_hashes']:
            raise ValueError('All windows must use the identical fixed strip, source leaves and block partition')
        if sum(p['panels'] for p in partition) != 10793 or len(partition) != count:
            raise ValueError('The complete original-leaf partition is missing')
        seen = []
        with gzip.open(primary, 'rt') as stream:
            for line in stream:
                window = json.loads(line)
                lo, hi = window['window']
                band = 'near' if hi <= 184 else 'rest'
                if not (94 <= lo <= hi <= 5758 and lo % 2 == hi % 2 == 0
                        and F(hi, lo) <= F(33, 32) and not (lo <= 184 < hi)
                        and window['head_band'] == band
                        and window['actual_mode_count'] == (hi - lo) // 2 + 1
                        and window['ratio_condition_exact'] and window['all10793_original_leaves']
                        and window['all18_original_source_segments_retained']
                        and window['comparison_source_origins'] == 25
                        and window['entry_count'] == window['exit_count'] == 1
                        and window['frame_jump_count'] == 1804
                        and window['both_initial_columns_retained']
                        and window['all3_source_materials'] and window['whole_leaf_targets_before_sup']
                        and len(window['rows']) == count):
                    raise ArithmeticError('A genuine interval-frequency or interface cost was omitted')
                seen.append([lo, hi]); windows.append([lo, hi])
                factor = 1 / sum(((lo * delta) ** k / F(math.factorial(k)) for k in range(7)), F(0))
                diagonal_diagnostic = []
                for i, target in enumerate(window['rows']):
                    part = partition[i]
                    if not (target['comparison_block'] == i and target['target_cell'] == part['cell']
                            and target['target_segment'] == part['segment']
                            and target['first_panel'] == part['first_panel']
                            and target['last_panel_exclusive'] == part['last_panel_exclusive']
                            and target['original_panels'] == part['panels']
                            and len(target['source_rows']) == i + 1):
                        raise ValueError('A whole target block or source-origin row is missing')
                    vi = ex(target['V_max'])
                    if vi <= 0:
                        raise ArithmeticError('The actual leaf V must be strictly positive')
                    if Vmax[i] is None:
                        Vmax[i] = vi
                    elif Vmax[i] != vi:
                        raise ArithmeticError('The actual target V must agree across frequency windows')
                    columns = target['initial_localV_separate_component_sups']
                    if len(columns) != 2 or any(len(col) != 2 for col in columns):
                        raise ValueError('Both physical initial columns and output components are required')
                    column_sums = [sum((ex(x) for x in col), F(0)) for col in columns]
                    gain = max(column_sums[0] / B, column_sums[1]) * decay_upper(lo * (delta + extra_start[i]))
                    if gain > head_gains[band][i]:
                        head_gains[band][i] = gain
                        head_where[band][i] = [lo, hi]
                    for j, row in enumerate(target['source_rows']):
                        source_part = partition[j]
                        if not (row['source_comparison_block'] == j and row['source_cell'] == source_part['cell']
                                and row['source_segment'] == source_part['segment']
                                and row['first_panel'] == source_part['first_panel']
                                and row['last_panel_exclusive'] == source_part['last_panel_exclusive']
                                and [v['V_power'] for v in row['density_rows']] == [2, 1, 0]):
                            raise ValueError('All true source origins and all three materials are required')
                        for density in row['density_rows']:
                            p = density['V_power']
                            # Either saved bound is already valid; their maximum also
                            # pays rounding of the separately saved component suprema.
                            value = max(ex(density['localV_strong_output_row']),
                                        ex(density['P_sup']) + ex(density['K_sup']))
                            if j < i:
                                value *= decay_upper(lo * max(F(0), extra_start[i] - extra_end[j]))
                            if value < 0:
                                raise ArithmeticError('Nonnegative comparison coefficients required')
                            if value > G[p][i][j]:
                                G[p][i][j] = value
                                where[p][i][j] = [lo, hi]
                            if i == j and p == 2:
                                diagonal_diagnostic.append(rec(value))
                diagnostics.append(dict(window=[lo, hi], band=band,
                                        complete25_diagonal_Gamma2=diagonal_diagnostic))
        if seen != meta['windows'] or len(seen) != len(meta['original_window_counts']):
            raise ArithmeticError('The completed primary does not match its exact window manifest')
        identities.update({str(p): digest(p) for p in (meta_path, primary, resource_path)})
        runs.append(dict(prefix=str(prefix), windows=len(seen), wall_seconds=usage['wall_seconds'],
                         peak_rss_kib=usage['peak_rss_kib'], exitcode=usage['exitcode']))

    if partition != [r['partition'] for r in shared_case['blocks']]:
        raise ArithmeticError('The common-strip blocks differ from the completed actual kernel blocks')
    gates['paid_complete_common_strip'] = True
    gates['monotone_causal_reweighting_paid'] = True
    windows.sort()
    covered = [m for lo, hi in windows for m in range(lo, hi + 1, 2)]
    gates.update(
        every_positive_even_middle_mode_exactly_once=covered == list(range(94, 5759, 2)),
        complete126_actual_windows=len(windows) == 126 and len({tuple(w) for w in windows}) == 126,
        all2833_positive_modes=len(covered) == 2833,
        both_true_head_bands_paid=all(head_where[band][i] is not None for band in ('near', 'rest') for i in range(count)),
        all25_comparison_blocks_and_three_materials=all(where[p][i][j] is not None for p in (2, 1, 0) for i in range(count) for j in range(i + 1)),
    )
    if not all(gates.values()):
        raise ArithmeticError('The full finite-middle coverage is incomplete: ' + str(gates))

    rows, radii, weights = [], [], []
    failure = None
    q = F(1, 2)
    for i, part in enumerate(partition):
        given = Hnear * head_gains['near'][i] + Hrest * head_gains['rest'][i]
        residual = centre_mass * sum(G[2][i], F(0))
        previous = sum((G[2][i][j] * (40 * radii[j] + 2 * radii[j] ** 2) for j in range(i)), F(0))
        A = given + residual + previous
        denominator = 1 - 40 * G[2][i][i]
        if denominator <= 0:
            failure = dict(index=i, kind='nonpositive_causal_radius_denominator',
                           diagonal40Gamma2=rec(40 * G[2][i][i]))
            break
        ri = up96(2 * A / denominator)
        image = A + G[2][i][i] * (40 * ri + 2 * ri ** 2)
        radii.append(ri)
        J = [4 * G[2][i][j] * (10 + radii[j]) for j in range(i + 1)]
        if J[i] >= q:
            failure = dict(index=i, kind='one_half_metric_diagonal_failed', derivative_diagonal=rec(J[i]))
            break
        wi = up96((1 + sum((J[j] * weights[j] for j in range(i)), F(0))) / (q - J[i]))
        weights.append(wi)
        distance = sum((J[j] * weights[j] for j in range(i + 1)), F(0)) / wi
        domain = (10 + ri) * Vmax[i]
        row = dict(index=i, partition=part, radius=rec(ri), V_max=rec(Vmax[i]),
                   full_projected_image=rec(image), strict_slack=rec(ri - image), image_over_radius=rec(image / ri),
                   balanced_true_head_lift=rec(given), complete_shared_centre_source=rec(residual),
                   earlier_block_feedback=rec(previous), comparison_diagonal40Gamma2=rec(40 * G[2][i][i]),
                   complete_derivative_diagonal=rec(J[i]), distance_weight=rec(wi),
                   weighted_complete_distance_row=rec(distance), strict_distance_slack=rec(q - distance),
                   physical_whole_field_domain=rec(domain),
                   given_band_gains={band: dict(gain=rec(head_gains[band][i]), attaining_window=head_where[band][i])
                                     for band in ('near', 'rest')},
                   all_material_rows={str(p): [dict(value=rec(value), attaining_window=where[p][i][j])
                                              for j, value in enumerate(G[p][i])] for p in (2, 1, 0)},
                   gates=dict(strict_positive_radius=ri > 0, strict_selfmap=image < ri,
                              positive_distance_weight=wi > 0, strict_distance_below_one_half=distance < q,
                              actual_whole_field_mean_domain_below_two_minus34=domain < F(2) ** -34))
        rows.append(row)
    gates['all25_complete_selfmap_and_distance_rows'] = len(rows) == count and all(all(r['gates'].values()) for r in rows)
    all_gates = all(gates.values()) and failure is None
    physical = sum((radii[i] * Vmax[i] for i in range(len(rows))), F(0))
    extrema = {}
    if rows:
        extrema = dict(
            maximum_radius=rec(max(ex(r['radius']) for r in rows)),
            maximum_image_over_radius=rec(max(ex(r['image_over_radius']) for r in rows)),
            maximum_comparison_diagonal40Gamma2=rec(max(ex(r['comparison_diagonal40Gamma2']) for r in rows)),
            maximum_derivative_diagonal=rec(max(ex(r['complete_derivative_diagonal']) for r in rows)),
            maximum_weighted_distance=rec(max(ex(r['weighted_complete_distance_row']) for r in rows)),
            maximum_physical_whole_field_domain=rec(max(ex(r['physical_whole_field_domain']) for r in rows)),
            complete_physical_strong_norm_upper=rec(physical),
            physical_middle_bound_below_R98_given_cap=all_gates and physical < F(2) ** -43)
    result = dict(schema='visible-flex-shared-strip-original-middle25block-budget-v4',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)', all_gates=all_gates, gates=gates,
        status=('The complete original94..5758 projected equation closes on the paid common strip; the new finite gap remains open' if all_gates
                else 'An actual exact full finite-middle sufficient comparison failed; no fixed point claimed'),
        fixed_point_claimed=all_gates, failure=failure,
        equation='v = true_head_lift_M + G_M Pi_M N(C_L+v), M={even m:94<=|m|<=5758}',
        parameter_domain='Real R74 twenty-axis domain and common phase, inside the paid real R100 centre domain',
        fixed_low_centre='Original complete R91/R101 low46 projected solution with unchanged boundary targets',
        complete_mean_and_inverse_retained=True, negative_modes_and_real_symmetry_retained=True,
        entire_shared_head_mass_paid_once_per_true_band=True, centre_source_shared_mass=rec(centre_mass),
        fixed_strip=shared_case, original_hybrid_strip=strip, initial_strip='18/125',
        common_high_threshold=args.high_cutoff, uncomputed_additional_middle_modes=shared_case['extra_positive_middle_modes'],
        full_middle_for_new_high_cutoff_closed=args.high_cutoff == 5760 and all_gates, source_factor_C0=10, distance_target='1/2',
        windows=windows, positive_even_mode_count=2833, signed_mode_count=5666,
        comparison_partition=partition, original_leaf_count=10793, completed_runs=runs,
        original_frame_jump_count_per_window=1804, rows=rows, window_diagonal_diagnostics=diagnostics,
        low_feedback_equation_closed=False, infinite_high_feedback_equation_closed=False,
        common_middle_high_strip_interface_paid=True, all46_cut_closed=False,
        full_outer_or_closed_surface_claimed=False, no_new_Arb_or_ODE_in_this_consumer=True,
        input_hashes={**identities, **{str(getattr(args, n)): digest(getattr(args, n)) for n in
            ('producer', 'coefficients', 'balanced', 'head', 'spectral', 'source', 'source_resource', 'common_strip', 'common_resource')}},
        source_sha256=digest(__file__), elapsed_seconds=time.monotonic() - started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **extrema)
    payload = (json.dumps(result, separators=(',', ':')) + '\n').encode()
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=9) as packed:
            packed.write(payload)
    if output.stat().st_size >= 5_000_000:
        raise ArithmeticError('The completed consumer must be partitioned before repository archival')
    short = {k: v for k, v in result.items() if k not in ('rows', 'window_diagonal_diagnostics')}
    short['primary'] = dict(path=str(output), bytes=output.stat().st_size, sha256=digest(output))
    summary_path.write_text(json.dumps(short, indent=2) + '\n')
    print(json.dumps(dict(all_gates=all_gates, failure=failure,
        windows=len(windows), positive_modes=len(covered), completed_rows=len(rows),
        displays={k: v['display_only'] if isinstance(v, dict) and 'display_only' in v else v for k, v in extrema.items()},
        elapsed_seconds=result['elapsed_seconds'], peak_rss_kib=result['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
