#!/usr/bin/env python3
"""Exact postprocessing of both outer-cell source functionals and R72 axes.

No ODE, source evaluation, floating solve, or change of candidate is made.
Outward dyadic geometry kernels can also bound the R71 two-sided candidate
change through both terminal readouts. The resulting comparisons are centre
budgets; they are not an outer nonlinear contraction or a Schur existence
claim.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import iter_array


def digest(path):
    out = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            out.update(block)
    return out.hexdigest()


def dyadic(data):
    if isinstance(data, list):
        m, e = int(data[0]), int(data[1])
    else:
        m, e = int(data['mantissa']), int(data['binary_exponent'])
    return Fraction(m << e) if e >= 0 else Fraction(m, 1 << -e)


def bounds(data):
    lo, hi = dyadic(data['lower']), dyadic(data['upper'])
    if lo > hi:
        raise ValueError('An ordered proved interval is required')
    return lo, hi


def magnitude(data):
    lo, hi = bounds(data)
    return max(abs(lo), abs(hi))


def rational(data):
    value = Fraction(data)
    with localcontext() as ctx:
        ctx.prec = 35
        display = str(Decimal(value.numerator) / Decimal(value.denominator))
    return dict(numerator=str(value.numerator), denominator=str(value.denominator),
                display=display)


def interval(lo, hi):
    if lo > hi:
        raise ValueError('Invalid exact output interval')
    return dict(lower=rational(lo), upper=rational(hi))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for arg in ('functional', 'recentring', 'moving-family', 'out'):
        p.add_argument('--' + arg, type=Path, required=True)
    p.add_argument('--rss-kib', type=int, default=40960)
    a = p.parse_args()
    started = time.monotonic()
    if a.out.exists():
        raise FileExistsError('Use a fresh exact comparison path')
    functional = json.loads(a.functional.read_text())
    recenter = json.loads(a.recentring.read_text())
    family = json.loads(a.moving_family.read_text())
    if not all(d['all_gates'] for d in (functional, recenter, family)):
        raise ValueError('Only completed true inputs may be consumed')
    if (functional['cells'] != [11, 10] or functional['modes'] != [2, 4]
            or functional['endpoint_physical_node'] != 10
            or functional['counts']['original_material'] != 10793
            or functional['config']['terminal_readouts'] != ['global_q', 'global_v']):
        raise ValueError('Both unchanged complete two-cell terminal functionals are required')
    if (recenter['cells'] != [11, 10]
            or not recenter['further_outer_linear_centre_residual_unchanged']
            or not recenter['gates']['single_mean_height_integral_and_constant_accounted']):
        raise ValueError('The R71 full two-sided same-endpoint construction is required')
    common = set(functional['input_hashes']) & set(recenter['input_hashes'])
    if not common or any(functional['input_hashes'][key] != recenter['input_hashes'][key]
                         for key in common):
        raise ValueError('The source/candidate/real-flow identities differ')
    ref = 'notes/2026-11-12-closure-newg-strong-m20-real-reference.json'
    expected_ref = 'd87a6862836c31f9cb72ed9b8ad74c0ee618797e45a83785c8206a83455233cb'
    if family['input_hashes'].get(ref) != expected_ref or digest(ref) != expected_ref:
        raise ValueError('The available parameter family must use the same actual strong centre')
    if bounds(family['epsilon']) != (Fraction(1, 1024), Fraction(1, 1024)):
        raise ValueError('This exact comparison is for the completed R72 relative box')
    input_hashes = {str(path): digest(path) for path in
                    (a.functional, a.recentring, a.moving_family)}
    input_hashes[ref] = expected_ref
    reports = {}
    for item in recenter['cell_reports']:
        path = Path(item['path'])
        if digest(path) != item['sha256']:
            raise ValueError('An executed R71 cell report changed')
        report = json.loads(path.read_text())
        n = report['cell']
        if n not in (10, 11) or n in reports or not report['all_original_panels_paid']:
            raise ValueError('Both complete unchanged R71 cell reports are required')
        reports[n] = report
        input_hashes[str(path)] = item['sha256']
    if sorted(reports) != [10, 11]:
        raise ValueError('The candidate change must be bounded on both cells')
    # The absolute kernel is a rigorous positive integral bound for each panel.
    # Its exact sum, multiplied by a proved whole-cell source cap, is valid
    # without a sign assumption or an exchange of mode and radial suprema.
    geometry = {(n, m, j): Fraction(0)
                for n in (10, 11) for m in (2, 4) for j in (0, 1)}
    panel_counts = {10: 0, 11: 0}
    seen = set()
    for group in functional['kernel_groups']:
        n, segment = group['cell'], group['segment']
        if (n, segment) in seen or n not in (10, 11) or not 0 <= segment < 9:
            raise ValueError('Every complete geometry segment must occur once')
        seen.add((n, segment))
        path = Path(group['path'])
        if digest(path) != group['sha256']:
            raise ValueError('A completed outward geometry kernel changed')
        input_hashes[str(path)] = group['sha256']
        count = 0
        for row in iter_array(path, 'panels'):
            if row['panel'] != group['panels'] - 1 - count:
                raise ValueError('The original reverse material order is required')
            keys = set()
            for weight in row['weights']:
                m, j = weight['mode'], weight['readout']
                if (m, j) in keys or m not in (2, 4) or j not in (0, 1):
                    raise ValueError('The complete two-mode two-readout weight is required')
                keys.add((m, j))
                value = dyadic(weight['absolute'])
                if value < 0:
                    raise ValueError('The absolute geometry majorant must be nonnegative')
                geometry[n, m, j] += value
            if keys != {(m, j) for m in (2, 4) for j in (0, 1)}:
                raise ValueError('An original functional component is missing')
            count += 1
        if count != group['panels']:
            raise ValueError('The complete original geometry range is required')
        panel_counts[n] += count
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > a.rss_kib:
            raise MemoryError('The owned exact kernel-reader exceeded its observed RSS gate')
    if seen != {(n, j) for n in (10, 11) for j in range(9)} or panel_counts != {10: 5248, 11: 5545}:
        raise ValueError('Every one of the original10793 positions must remain present')
    family_axes = {row['mode']: row for row in family['displayed_endpoint_axes']}
    rows = []
    for old in functional['rows']:
        m = old['mode']
        axis_lo, axis_hi = bounds(family_axes[m]['relative_parameter_axis'])
        if axis_lo != axis_hi or axis_lo <= 0:
            raise ValueError('An exact positive certified R72 coordinate axis is required')
        axis = axis_lo
        old_lo, old_hi = bounds(old['complete_candidate_centre_residual_canonical_Q'])
        deltas = []
        for j in (0, 1):
            per_cell = []
            total = Fraction(0)
            for n in (11, 10):
                source_cap = bounds(reports[n]['selected_complete_source_change_upper'][str(m)])[1]
                if source_cap < 0:
                    raise ValueError('A complete source-change upper bound must be positive')
                term = source_cap * geometry[n, m, j]
                total += term
                per_cell.append(dict(cell=n,absolute_geometry_integral=rational(geometry[n, m, j]),
                    complete_selected_source_change_cap=rational(source_cap),
                    global_state_forcing_change_upper=rational(term)))
            deltas.append(dict(readout=('global_q', 'global_v')[j],cells=per_cell,
                total_change_upper=rational(total)))
        delta_q = Fraction(int(deltas[0]['total_change_upper']['numerator']),
                           int(deltas[0]['total_change_upper']['denominator']))
        cut_delta = magnitude(old['canonical_cut_geometry_factor']) * delta_q
        new_lo, new_hi = old_lo - cut_delta, old_hi + cut_delta
        old_cap, new_cap = max(abs(old_lo), abs(old_hi)), max(abs(new_lo), abs(new_hi))
        rows.append(dict(mode=m,
            parameter_variable='shallow canonical Q_m=h_m/r_b^4; cosine coefficient',
            available_R72_relative_axis=rational(axis),
            original_candidate_complete_node10_centre=interval(old_lo, old_hi),
            original_centre_axis_ratio=rational(old_cap / axis),
            original_centre_inside_available_axis=old_cap < axis,
            R71_two_cell_complete_source_change=deltas,
            R71_new_minus_old_cut_Q_functional_upper=rational(cut_delta),
            R71_recentred_complete_node10_centre=interval(new_lo, new_hi),
            R71_recentred_axis_ratio=rational(new_cap / axis),
            R71_recentred_centre_inside_available_axis=new_cap < axis,
            node10_complete_linear_centre_exactly_unchanged=True,
            unknown_outer_correction_and_parameter_derivative_paid=False))
    gates = dict(complete_actual_two_cell_functionals=True,
        every10793_outward_kernel_preserved=True,
        same_actual_background_and_original_strong_centre=True,
        completed_R72_parameter_box_used=True,
        exact_global_qv_units_and_cut_Q_conversion=True,
        R71_complete_mean_and_inverse_source_changes_retained=True,
        R71_node10_linear_centre_invariance_used=True,
        R71_mean_height_total_change_kept_separate=True,
        no_new_ODE_or_source_integration=True)
    output = dict(status='Exact two-cell centre budgets against the completed R72 family',
        gates=gates,all_gates=all(gates.values()),rows=rows,
        all_original_centres_within_available_axes=all(r['original_centre_inside_available_axis'] for r in rows),
        all_recentred_centres_within_available_axes=all(r['R71_recentred_centre_inside_available_axis'] for r in rows),
        complete_mean_height_total_change_upper=recenter['complete_mean_height_total_change_upper'],
        mean_anchor=recenter['mean_anchor'],
        full_outer_matching_or_contraction_claimed=False,
        scope='Only m2/m4 at node10 for the same completed original/R71 candidates. R72 supplies available true head parameters; the outer correction map and its full-frequency derivatives remain separate.',
        input_hashes=input_hashes,source_sha256=digest(Path(__file__)),
        arithmetic='fractions.Fraction for all bounds/comparisons; Decimal is display only',
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=output['all_gates'],
        all_original_centres_within_available_axes=output['all_original_centres_within_available_axes'],
        all_recentred_centres_within_available_axes=output['all_recentred_centres_within_available_axes'],
        rows=[dict(mode=r['mode'],original_ratio=r['original_centre_axis_ratio']['display'],
            recentred_ratio=r['R71_recentred_axis_ratio']['display']) for r in rows],
        peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':
    main()
