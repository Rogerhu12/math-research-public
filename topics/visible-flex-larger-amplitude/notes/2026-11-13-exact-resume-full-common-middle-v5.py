#!/usr/bin/env python3
"""Join the paid original126 windows with the59 new common-strip windows.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All185 windows cover every positive even mode94..34814 once.  The true
near/rest/infinite head masses are each paid once per complete output row.
The physical low centre and complete mean/inverse are unchanged.  This
consumer proves only the enlarged finite projected equation; the high and
low feedback equations remain explicit separate obligations.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time


def digest(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(p).suffix == '.gz' else raw)


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2) ** int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator), display_only=float(v))


def up96(v):
    if v <= 0:
        raise ArithmeticError('Strictly positive finite radius or weight required')
    unit = F(2) ** (v.numerator.bit_length() - v.denominator.bit_length() - 96)
    return (v // unit + 1) * unit


@lru_cache(maxsize=1024)
def decay(z):
    if z < 0:
        raise ArithmeticError('A negative width gap cannot be discarded')
    if z == 0:
        return F(1)
    value = min(F(1), up96(1 / (1 + z / 65536)))
    for _ in range(16):
        value = min(F(1), up96(value * value))
    return value


def named_hash(mapping, name):
    matches = [v for k, v in mapping.items() if Path(k).name == name]
    if len(matches) != 1:
        raise ValueError('Exactly one original input identity required for ' + name)
    return matches[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for n in ('base', 'base-resource', 'base-source', 'common', 'balanced', 'head',
              'source', 'producer', 'out-prefix'):
        ap.add_argument('--' + n, type=Path, required=True)
    ap.add_argument('--gap-prefix', type=Path, action='append', required=True)
    args = ap.parse_args(); started = time.monotonic()
    output = Path(str(args.out_prefix) + '.json.gz')
    summary = Path(str(args.out_prefix) + '-summary.json')
    if output.exists() or summary.exists():
        raise FileExistsError('A fresh full common-strip output is required')
    base, br, common, balanced, head, source = [read(getattr(args, n)) for n in
        ('base', 'base_resource', 'common', 'balanced', 'head', 'source')]
    M = common['leaf_primary']['high_cutoff']
    common_case = next(r for r in common['cases'] if r['high_threshold'] == M)
    gates = dict(
        completed_original126_windows=base['all_gates'] and all(base['gates'].values()) and len(base['windows']) == 126,
        original_budget_formal_exit_zero=br['exitcode'] == 0 and br['termination_signal'] is None,
        original_budget_source_identity=base['source_sha256'] == digest(args.base_source),
        same_exact_common_strip=base['fixed_strip'] == common_case and common['all_identity_gates'] and all(common['gates'].values()),
        same_original_true_head=named_hash(base['input_hashes'], args.head.name) == digest(args.head),
        same_original_balanced_head=named_hash(base['input_hashes'], args.balanced.name) == digest(args.balanced),
        same_original_complete_source=named_hash(base['input_hashes'], args.source.name) == digest(args.source),
        same_chosen_high_cutoff=M == 34816,
        complete_source_and_head_gates=source['all_gates'] and head['all_gates'] and balanced['all_gates'],
        complete_polynomial_support_below_all_cutoffs=source['gates']['exact_polynomial_support_to736'] and M > 736,
        all_high_inverse_tail_included=source['tail_mass_must_be_paid_once_across_any_joint_partition'],
        common_positive_strip=ex(common_case['common_terminal_strip']) > F(1, 64),
    )
    if not all(gates.values()):
        raise ArithmeticError('An original identity or common-space gate failed: ' + str(gates))
    partition = base['comparison_partition']; count = len(partition)
    if count != 25 or base['positive_even_mode_count'] != 2833:
        raise ValueError('Keep the complete original25-block finite packet')
    G = {p: [[ex(v['value']) for v in row['all_material_rows'][str(p)]] for row in base['rows']] for p in (2, 1, 0)}
    at = {p: [[v['attaining_window'] for v in row['all_material_rows'][str(p)]] for row in base['rows']] for p in (2, 1, 0)}
    bands = ('near', 'rest', 'infinite')
    gains = {band: [ex(row['given_band_gains'][band]['gain']) if band != 'infinite' else F(0)
                    for row in base['rows']] for band in bands}
    gain_at = {band: [row['given_band_gains'][band]['attaining_window'] if band != 'infinite' else None
                      for row in base['rows']] for band in bands}
    V = [ex(row['V_max']) for row in base['rows']]
    B = ex(balanced['balanced_B_lower']); delta = ex(balanced['exact_head_to_output_strip_gap_lower'])
    head_mass = dict(zip(bands, map(ex, head['complete_coarse_trace_rows']['head']['high_bands_value_upper'])))
    original_windows = base['windows']; gaps = []; runs = []; hashes = {}
    for prefix in args.gap_prefix:
        primary = Path(str(prefix) + '-windows.jsonl.gz'); mp = Path(str(prefix) + '.json')
        rp = Path(str(prefix) + '-resource.json'); meta, usage = read(mp), read(rp)
        if not (meta['all_enclosure_gates'] and meta['source_sha256'] == digest(args.producer)
                and meta['precision'] >= 256 and meta['high_cutoff'] == M
                and meta['comparison_partition'] == partition and meta['source_powers'] == [2, 1, 0]
                and meta['original_leaf_count_per_window'] == 10793 and meta['original_source_groups'] == 18
                and meta['comparison_source_blocks'] == 25 and meta['energy_segment_subblocks'] == 8
                and meta['same_fixed_strip']['strip_loss'] == common_case['complete_common_loss']
                and meta['same_fixed_strip']['terminal_strip'] == common_case['common_terminal_strip']
                and named_hash(meta['input_hashes'], args.common.name) == digest(args.common)
                and meta['primary']['sha256'] == digest(primary)
                and meta['primary']['bytes'] == primary.stat().st_size
                and usage['exitcode'] == 0 and usage['termination_signal'] is None
                and usage['peak_rss_kib'] <= 98304):
            raise ArithmeticError('An actual completed common-gap window packet failed its complete gates')
        seen = []
        with gzip.open(primary, 'rt') as stream:
            for line in stream:
                win = json.loads(line); lo, hi = win['window']
                band = 'rest' if hi <= 8190 else 'infinite'
                if not (5760 <= lo <= hi < M and lo % 2 == hi % 2 == 0 and F(hi, lo) <= F(33, 32)
                        and not (lo <= 8190 < hi) and win['head_band'] == band
                        and win['all10793_original_leaves'] and win['all18_original_source_segments_retained']
                        and win['comparison_source_origins'] == 25 and win['frame_jump_count'] == 1804
                        and win['entry_count'] == win['exit_count'] == 1
                        and win['analytic_strip_jump_count'] == 8956 and win['comparison_substeps'] >= 10793
                        and win['both_initial_columns_retained'] and win['all3_source_materials']
                        and win['whole_leaf_targets_before_sup'] and len(win['rows']) == 25):
                    raise ArithmeticError('A source, target, frequency or actual interface cost is missing')
                seen.append([lo, hi]); gaps.append([lo, hi])
                factor = decay(lo * delta)
                for i, row in enumerate(win['rows']):
                    p = partition[i]
                    if not (row['comparison_block'] == i and row['target_cell'] == p['cell']
                            and row['target_segment'] == p['segment'] and row['first_panel'] == p['first_panel']
                            and row['last_panel_exclusive'] == p['last_panel_exclusive']
                            and row['original_panels'] == p['panels'] and ex(row['V_max']) == V[i]
                            and len(row['source_rows']) == i + 1):
                        raise ValueError('A true original target block was changed or omitted')
                    cols = row['initial_localV_separate_component_sups']
                    if len(cols) != 2 or any(len(col) != 2 for col in cols):
                        raise ValueError('Both real initial columns and physical components are required')
                    gain = max(sum(map(ex, cols[0]), F(0)) / B, sum(map(ex, cols[1]), F(0))) * factor
                    if gain > gains[band][i]:
                        gains[band][i] = gain; gain_at[band][i] = [lo, hi]
                    for j, sr in enumerate(row['source_rows']):
                        sp = partition[j]
                        if not (sr['source_comparison_block'] == j and sr['source_cell'] == sp['cell']
                                and sr['source_segment'] == sp['segment'] and sr['first_panel'] == sp['first_panel']
                                and sr['last_panel_exclusive'] == sp['last_panel_exclusive']
                                and [r['V_power'] for r in sr['density_rows']] == [2, 1, 0]):
                            raise ValueError('All original source origins and three materials are required')
                        for density in sr['density_rows']:
                            power = density['V_power']
                            value = max(ex(density['localV_strong_output_row']), ex(density['P_sup']) + ex(density['K_sup']))
                            if value > G[power][i][j]:
                                G[power][i][j] = value; at[power][i][j] = [lo, hi]
        if seen != meta['windows']:
            raise ValueError('The completed actual window primary differs from its manifest')
        hashes.update({str(p): digest(p) for p in (primary, mp, rp)})
        runs.append(dict(prefix=str(prefix), windows=len(seen), wall_seconds=usage['wall_seconds'],
                         peak_rss_kib=usage['peak_rss_kib'], exitcode=0))
    gaps.sort(); windows = sorted(original_windows + gaps)
    coverage = [m for lo, hi in windows for m in range(lo, hi + 1, 2)]
    gates.update(all59_new_windows=len(gaps) == 59,
        all14528_new_positive_modes=[m for lo, hi in gaps for m in range(lo, hi + 1, 2)] == list(range(5760, M, 2)),
        every_positive_even_mode_exactly_once=coverage == list(range(94, M, 2)),
        all185_actual_windows=len(windows) == 185,
        every_shared_head_band_paid=all(gain_at[band][i] is not None for band in bands for i in range(count)))
    if not all(gates.values()):
        raise ArithmeticError('The full finite frequency coverage is incomplete: ' + str(gates))
    centre_mass = ex(source['complete_middle_shared_mass'])
    rows = []; radii = []; weights = []; failure = None
    for i, part in enumerate(partition):
        head_bound = sum((head_mass[band] * gains[band][i] for band in bands), F(0))
        residual = centre_mass * sum(G[2][i], F(0))
        previous = sum((G[2][i][j] * (40 * radii[j] + 2 * radii[j] ** 2) for j in range(i)), F(0))
        A = head_bound + residual + previous; den = 1 - 40 * G[2][i][i]
        if den <= 0:
            failure = dict(block=i, kind='nonpositive_causal_radius_denominator'); break
        radius = up96(2 * A / den); radii.append(radius)
        image = A + G[2][i][i] * (40 * radius + 2 * radius ** 2)
        J = [4 * G[2][i][j] * (10 + radii[j]) for j in range(i + 1)]
        if J[i] >= F(1, 2):
            failure = dict(block=i, kind='distance_diagonal_below_half_failed'); break
        weight = up96((1 + sum((J[j] * weights[j] for j in range(i)), F(0))) / (F(1, 2) - J[i]))
        weights.append(weight)
        distance = sum((J[j] * weights[j] for j in range(i + 1)), F(0)) / weight
        domain = (10 + radius) * V[i]
        rows.append(dict(index=i, partition=part, V_max=rec(V[i]), radius=rec(radius),
            full_projected_image=rec(image), strict_slack=rec(radius - image), image_over_radius=rec(image / radius),
            balanced_true_head_lift=rec(head_bound), complete_shared_centre_source=rec(residual),
            earlier_block_feedback=rec(previous), comparison_diagonal40Gamma2=rec(40 * G[2][i][i]),
            complete_derivative_diagonal=rec(J[i]), distance_weight=rec(weight), weighted_complete_distance_row=rec(distance),
            physical_whole_field_domain=rec(domain),
            given_band_gains={band: dict(gain=rec(gains[band][i]), attaining_window=gain_at[band][i]) for band in bands},
            all_material_rows={str(p): [dict(value=rec(value), attaining_window=at[p][i][j])
                                      for j, value in enumerate(G[p][i])] for p in (2, 1, 0)},
            gates=dict(strict_selfmap=image < radius, strict_distance_below_half=distance < F(1, 2),
                       whole_mean_domain_below_two_minus34=domain < F(2) ** -34)))
    gates['all25_complete_nonlinear_rows'] = len(rows) == count and all(all(r['gates'].values()) for r in rows)
    passed = all(gates.values()) and failure is None
    physical = sum((ex(r['radius']) * ex(r['V_max']) for r in rows), F(0))
    result = dict(schema='visible-flex-full-common-middle34816-v5', author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        status=('All finite modes94..34814 close in the paid shared strip' if passed else 'A full finite sufficient comparison failed'),
        all_gates=passed, gates=gates, failure=failure, fixed_point_claimed=passed,
        equation='v = true_head_M + G_M Pi_M N(C_L+v), M={even m:94<=|m|<=34814}',
        high_cutoff=M, positive_even_mode_count=len(coverage), original_leaf_count=10793,
        windows=windows, original126_windows_recomputed=False, new59_window_runs=runs,
        fixed_common_strip=common_case, comparison_partition=partition, rows=rows,
        centre_source_shared_mass=rec(centre_mass), source_polynomial_support736_covers_all_non_tail_modes=True,
        each_true_head_band_mass_used_once=True, head_band_masses={band: rec(head_mass[band]) for band in bands},
        maximum_radius=rec(max(ex(r['radius']) for r in rows)),
        maximum_image_over_radius=rec(max(ex(r['image_over_radius']) for r in rows)),
        maximum_weighted_distance=rec(max(ex(r['weighted_complete_distance_row']) for r in rows)),
        maximum_physical_whole_field_domain=rec(max(ex(r['physical_whole_field_domain']) for r in rows)),
        complete_physical_strong_norm_upper=rec(physical), physical_middle_cap_below_two_minus43=passed and physical < F(2) ** -43,
        infinite_high_feedback_equation_closed=False, low_feedback_equation_closed=False,
        all46_cut_closed=False, full_outer_or_closed_surface_claimed=False,
        complete_mean_and_inverse_retained=True, negative_modes_retained=True,
        input_hashes={**hashes, **{str(getattr(args, n)): digest(getattr(args, n)) for n in
            ('base', 'base_resource', 'base_source', 'common', 'balanced', 'head', 'source', 'producer')}},
        source_sha256=digest(__file__), elapsed_seconds=time.monotonic() - started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=9) as packed:
            packed.write((json.dumps(result, separators=(',', ':')) + '\n').encode())
    if output.stat().st_size >= 5_000_000:
        raise ArithmeticError('Partition the completed output before archival')
    short = {k: v for k, v in result.items() if k != 'rows'}
    short['primary'] = dict(path=str(output), bytes=output.stat().st_size, sha256=digest(output))
    summary.write_text(json.dumps(short, indent=2) + '\n')
    print(json.dumps(dict(all_gates=passed, failure=failure, modes=len(coverage), windows=len(windows),
        physical_middle=float(physical), maximum_radius=result['maximum_radius']['display_only'],
        maximum_domain=result['maximum_physical_whole_field_domain']['display_only'],
        elapsed_seconds=result['elapsed_seconds'], peak_rss_kib=result['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
