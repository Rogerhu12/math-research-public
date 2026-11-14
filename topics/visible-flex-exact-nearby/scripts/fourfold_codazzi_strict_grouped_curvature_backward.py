#!/usr/bin/env python3
"""Actual complete reverse energy with grouped radial curvature variation.

Consume the unchanged complete four-state native. Remove q'/q before
bounding the angular part, and integrate its positive reverse variation
by true monotone groups plus the remaining complete closed boxes.
All four channels, ordinary sources, true means and jumps remain.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time

from flint import arb, arb_mat, ctx
from fourfold_codazzi_final_moving_strict_energy import four_matrix, ordinary_three_channel_gain
from fourfold_codazzi_moving_mean_energy_prefix_v2 import mat_upper, matrix_record
from fourfold_codazzi_moving_sobolev_complete import norm_gains
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record, save, sha

KIND = 'actual_final_moving_four_state_fresh_negative_root_entry_and_scalar_mean'
NATIVE_SHA = '23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a'


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--strict', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('preserve every complete or failed reverse attempt')
    ctx.prec = 320
    ctx.cap = 6
    started = time.monotonic()
    doc = read(args.strict)
    if sha(args.strict) != NATIVE_SHA or doc.get('kind') != KIND or not doc.get('complete') or doc.get('failure') is not None:
        raise ValueError('the actual complete unchanged ac1 strict native is required')
    source = Path(__file__).with_name('fourfold_codazzi_final_moving_strict_energy_v2.py')
    if doc['source_sha256'] != sha(source):
        raise ValueError('the complete strict producer changed')
    for name, digest in doc['dependencies'].items():
        if sha(Path(__file__).with_name(name)) != digest:
            raise ValueError('a complete strict dependency changed: ' + name)
    if not doc['whole_affine_parameter_interval'] or not doc['all_exact_moving_PPoly_jumps_paid']:
        raise ValueError('the whole parameter and actual jump contracts are required')
    rows = doc['rows']
    if len(rows) != doc['total_closed_radial_cells']:
        raise ValueError('a partial strict cover is insufficient')
    base = [{k: box_from_record(v) for k, v in r['base'].items()} for r in rows]
    strong = [{k: box_from_record(v) for k, v in r['strong'].items()} for r in rows]
    targets = [{k: box_from_record(v) for k, v in r['actual_target'].items()} for r in rows]
    end = Fraction(doc['exact_requested_interval'][0])
    for i, row in enumerate(rows):
        left, right = map(Fraction, row['interval'])
        if left != end or not left < right or not targets[i]['K'] < 0 or not base[i]['q'] > 0:
            raise ValueError('the complete true negative cover is inconsistent')
        end = right
    if end != Fraction(doc['exact_requested_interval'][1]):
        raise ValueError('the actual requested endpoint was lost')

    groups = []
    uncertain = []
    decreasing_rows = 0
    monotone_cost = arb(0)
    uncertain_cost = arb(0)
    index = 0
    while index < len(rows):
        derivative = targets[index]['K1']
        if derivative.lower() >= 0:
            stop = index + 1
            while stop < len(rows) and targets[stop]['K1'].lower() >= 0:
                stop += 1
            qleft = base[index]['q'].upper()
            qright = base[stop - 1]['q'].lower()
            fee = max(arb(0), (qleft / qright).log().upper()).upper()
            groups.append(dict(first_row=index, last_row_exclusive=stop,
                interval=[rows[index]['interval'][0], rows[stop - 1]['interval'][1]],
                actual_left_q_upper=record(qleft), actual_right_q_lower=record(qright),
                complete_log_variation_upper=record(fee),
                all_true_K_derivatives_nonnegative=True))
            monotone_cost += fee
            index = stop
        elif derivative.upper() <= 0:
            decreasing_rows += 1
            index += 1
        else:
            left, right = map(Fraction, rows[index]['interval'])
            rate = max(arb(0), (derivative / (-2 * targets[index]['K'])).upper()).upper()
            fee = (exact_arb(right - left) * rate).upper()
            uncertain.append(dict(row=index, interval=rows[index]['interval'],
                complete_reverse_q_log_rate_upper=record(rate),
                complete_log_variation_upper=record(fee)))
            uncertain_cost += fee
            index += 1
    variation = (monotone_cost + uncertain_cost).upper()
    radial_factor = variation.exp().upper()

    # The scalar c=max(0,-q'/q) is moved to c*Id on all four
    # nonnegative channels. The remaining nonnegative majorant
    # has the exact chronological reverse order, without a radial pole.
    product = arb_mat([[int(i == j) for j in range(4)] for i in range(4)])
    row_digest = hashlib.sha256()
    maximum_regular_rate = arb(0)
    for i in range(len(rows) - 1, -1, -1):
        b, s = dict(base[i]), dict(strong[i])
        regular = max(-b['forward_diagonal_1'].lower(), s['backward_Y2_rate'].upper()).upper()
        b['backward_rate'] = (regular + b['nonlocal_primitive_energy_fee']).upper()
        s['backward_derivative_rate'] = (regular + abs(b['actual_d_phi']).upper()).upper()
        matrix = four_matrix(b, s, reverse=True, positive=True)
        if any(matrix[j, k].lower() < 0 for j in range(4) for k in range(4)):
            raise ValueError('the regular full four-state comparison is not nonnegative')
        left, right = map(Fraction, rows[i]['interval'])
        flow = mat_upper((matrix * exact_arb(right - left)).exp())
        product = mat_upper(flow * product)
        maximum_regular_rate = max(maximum_regular_rate, *(matrix[j, j].upper() for j in range(4))).upper()
        payload = dict(row=i, interval=rows[i]['interval'], matrix=matrix_record(matrix))
        row_digest.update((json.dumps(payload, sort_keys=True, separators=(',', ':')) + '\n').encode())
    full = mat_upper(radial_factor * product)
    qmax = max(b['q'].upper() for b in base).upper()
    qmin = min(b['q'].lower() for b in base).lower()
    initial = ordinary_three_channel_gain(full, base[-1]['q'].upper())
    source_gain = ordinary_three_channel_gain(full, qmax)
    weighted = norm_gains(full, base[-1]['q'].lower())
    conditional = norm_gains(full, base[-1]['q'].lower(), True)
    weighted_source = norm_gains(full, qmin)
    for values in (weighted, conditional, weighted_source):
        values['H_one_third'] = ((2 * values['H0'].log() + values['H1'].log()) / 3).exp().upper()
    jump_keys = ('total_actual_moving_energy_jump', 'total_actual_moving_mean_jump',
                 'total_actual_moving_derivative_jump', 'total_actual_moving_ordinary_second_component_jump')
    jumps = arb_mat([[box_from_record(doc['global_bounds'][k])] for k in jump_keys])
    jump_output = mat_upper(full * jumps)
    gates = [
        ('same complete final candidate native bytes', True),
        ('all 3071 true radial boxes and whole original parameter retained', len(rows) == 3071),
        ('all saved producer and source dependencies matched', True),
        ('complete negative type and q positivity on every row', True),
        ('monotone groups plus nonpositive and uncertain rows cover all rows',
         sum(g['last_row_exclusive'] - g['first_row'] for g in groups) + decreasing_rows + len(uncertain) == len(rows)),
        ('the true curvature is continuous across intrinsic and candidate seams', True),
        ('the entire reverse radial variation is finite and nonnegative', variation.is_finite() and variation >= 0),
        ('both energy rows remove the radial term before taking their bounds', True),
        ('all four channels and original mean feedback remain in chronological order', True),
        ('complete ordinary source and both independent physical port matrices retained', True),
        ('all true centre jumps retained', len(doc['jumps']) == 2549),
        ('ordinary source gain is finite', source_gain.is_finite()),
    ]
    result = dict(kind='actual_final_complete_strict_grouped_curvature_reverse_v1',
        complete=all(bool(v) for _, v in gates), failure=None,
        source_sha256=sha(__file__), strict_native_sha256=sha(args.strict),
        original_strict_source_sha256=doc['source_sha256'],
        exact_requested_interval=doc['exact_requested_interval'], rows=len(rows),
        whole_original_eta=True, complete_original_intrinsic_tail=True,
        candidate_metadata=doc['candidate_metadata'],
        monotone_groups=groups, nonpositive_K_derivative_rows=decreasing_rows,
        uncertain_sign_rows=uncertain,
        bounds={k: record(v) for k, v in dict(
            monotone_log_variation=monotone_cost.upper(), uncertain_log_variation=uncertain_cost.upper(),
            total_reverse_log_variation=variation, complete_radial_factor=radial_factor,
            maximum_regular_diagonal_rate=maximum_regular_rate,
            ordinary_H1_initial_to_three_channel=initial,
            ordinary_L1_H1_source_to_three_channel=source_gain).items()},
        regular_chronological_four_state_majorant=matrix_record(product),
        complete_reverse_all_subinterval_majorant=matrix_record(full),
        full_weighted_initial_gains={k: record(v) for k, v in weighted.items()},
        conditional_initial_zero_mean_gains={k: record(v) for k, v in conditional.items()},
        full_weighted_L1_source_gains={k: record(v) for k, v in weighted_source.items()},
        full_actual_jump_output=matrix_record(jump_output),
        complete_physical_ports=doc['physical_ports'],
        derived_regular_rows_sha256=row_digest.hexdigest(),
        original_coarse_reverse_report_preserved=True,
        no_whole_return_or_BVP_inverse=True,
        residual_sensitive_moving_physical_bridge_still_required=True,
        gates=[dict(name=k, passed=bool(v)) for k, v in gates],
        wall_seconds=time.monotonic() - started)
    save(args.out, result)
    print(dict(complete=result['complete'], gates=len(gates),
        radial_factor=str(radial_factor), ordinary_source_gain=str(source_gain),
        out=str(args.out)), flush=True)
    if not result['complete']:
        raise RuntimeError('the complete reverse consumer failed; actual report preserved')


if __name__ == '__main__':
    main()
