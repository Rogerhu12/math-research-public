#!/usr/bin/env python3
"""Exact ordered consumer for recovered physical low46 Green profiles.

Pure stdlib Fraction arithmetic; no new source evaluation, ODE, flint,
or replacement of a true head boundary by a finite Robin condition.
Two passes preserve source/output radial order. The same panel may be
used in both sides of the Green bound, a deliberate positive overbound.
Component suprema are taken separately before summing modes.

The old three strong densities require input cutoff<=92. The six weak
densities allow all input frequencies, retain full mean/inverse terms,
and acquire the explicit output factor 1+m. Infinite OUTPUT modes are
not certified by this finite-window consumer.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
import math
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import digest, iter_array

GEOMETRY_SOURCE = 'c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829'
MODES = list(range(2, 93, 2))


def dyad(x):
    return F(int(x[0]))*F(2)**int(x[1])


def endpoint(x):
    return F(int(x['mantissa']))*F(2)**int(x['binary_exponent'])


def bounds(x):
    return endpoint(x['lower']), endpoint(x['upper'])


def absolute(x):
    lo, hi = bounds(x)
    return max(abs(lo), abs(hi))


def positive_abs_lower(x):
    lo, hi = bounds(x)
    if lo > 0:
        return lo
    if hi < 0:
        return -hi
    raise ArithmeticError('A true scalar denominator includes zero')


def exact_point(x):
    lo, hi = bounds(x)
    if lo != hi:
        raise ArithmeticError('An exact stored canonical point is not a point')
    return lo


def fraction_record(x):
    x = F(x)
    return dict(numerator=str(x.numerator), denominator=str(x.denominator))


def dyadic_upper(x, bits=96):
    x = F(x)
    if x < 0:
        raise ArithmeticError('A positive budget cannot have a negative value')
    if not x:
        return [0, 0]
    exponent = x.numerator.bit_length()-x.denominator.bit_length()-bits+1
    scaled = x/F(2)**exponent
    m = -((-scaled.numerator)//scaled.denominator)
    return [m, exponent]


def exp_bounds(x, terms=96):
    x = F(x)
    if x < 0:
        lo, hi = exp_bounds(-x, terms)
        return 1/hi, 1/lo
    value = term = F(1)
    for k in range(1, terms+1):
        term *= x/k
        value += term
    following = term*x/(terms+1)
    ratio = x/(terms+2)
    if not ratio < 1:
        raise ArithmeticError('The explicit exponential Taylor tail is unpaid')
    return value, value+following/(1-ratio)


def sqrt_upper(x, bits=256):
    x = F(x)
    if x < 0:
        raise ArithmeticError('A square-root input is negative')
    scale = 1 << bits
    n = math.isqrt((x.numerator*scale*scale)//x.denominator)
    if F(n*n, scale*scale) == x:
        return F(n, scale)
    return F(n+1, scale)


def save(path, data):
    path = Path(path)
    payload = (json.dumps(data, separators=(',', ':'))+'\n').encode()
    if len(payload) > 5*1024*1024:
        raise ArithmeticError('A primary exceeds the repository 5 MiB cap')
    if path.exists():
        raise FileExistsError('A completed or failed budget must be preserved')
    tmp = Path(str(path)+'.partial')
    if tmp.exists():
        raise FileExistsError('A partial budget is retained; use a fresh prefix')
    if len(payload) >= 1_000_000:
        target = Path(str(path)+'.gz')
        if target.exists():
            raise FileExistsError('A compressed primary already exists')
        with gzip.open(tmp, 'wb', compresslevel=9) as stream:
            stream.write(payload)
        tmp.rename(target)
        return target
    tmp.write_bytes(payload)
    tmp.rename(path)
    return path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--geometry-source-sha256', default=GEOMETRY_SOURCE)
    p.add_argument('--rss-kib', type=int, default=40960)
    a = p.parse_args()
    began = time.monotonic()
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    for suffix in ('.json', '.json.gz', '-failure.json', '-failure.json.gz'):
        if Path(str(a.out_prefix)+suffix).exists():
            raise FileExistsError('Use a fresh complete ordered budget prefix')
    doc = json.loads(a.geometry.read_text())
    config = doc['config']
    if (not doc['all_gates'] or not all(doc['gates'].values())
            or config['modes'] != MODES
            or config['entrypoint_sha256'] != a.geometry_source_sha256
            or doc['counts']['original_material'] != 10793):
        raise ValueError('The complete same-source actual physical46 geometry is required')
    expected_order = [(n, j) for n in (10, 11) for j in range(8, -1, -1)]
    if [tuple(x) for x in doc['completed_groups']] != expected_order:
        raise ValueError('The whole physical source order is incomplete')
    density = config['densities']
    if len(density) != 9:
        raise ValueError('Retain all nine original and weak/uniform density columns')
    D, M = len(density), len(MODES)
    V0 = dyad(config['uniform_envelope'])
    if V0 != F(1, 1 << 40):
        raise ValueError('The declared uniform norm changed')
    W = [positive_abs_lower(config['true_physical_Wronskians'][str(m)]) for m in MODES]
    S0 = [positive_abs_lower(config['actual_true_S0_Q'][str(m)]) for m in MODES]
    Qout = [absolute(config['actual_outer_Q'][str(m)]) for m in MODES]
    axes = {r['mode']: r for r in config['parameter_axes']}
    if sorted(axes) != list(range(2, 41, 2)):
        raise ValueError('The entire actual twenty-axis family must be retained')
    angular = {m: exp_bounds(F(m, 64)) for m in MODES}
    omega_upper = [(1+m)*angular[m][1] for m in MODES]
    b = bounds(config['actual_true_cut_radius'])[1]
    wb = bounds(config['actual_true_cut_w'])[1]
    Fb = sqrt_upper(b*wb**3)
    lift_factor = [m*b**4*wb*wb/W[k] for k, m in enumerate(MODES)]
    totals = [[[F(0), F(0)] for d in range(D)] for k in range(M)]
    total_subpanels = 0
    hashes = {str(a.geometry): digest(a.geometry)}
    def guard():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > a.rss_kib:
            raise MemoryError('Observed owned ordered-consumer RSS exceeded its declared threshold: '+str(peak))
    def rows():
        for group in doc['profile_groups']:
            right = F(1)
            count = 0
            for chunk in group['chunks']:
                path = Path(chunk['path'])
                if digest(path) != chunk['sha256']:
                    raise ValueError('A true derived profile chunk changed')
                hashes[str(path)] = chunk['sha256']
                local_count = 0
                for row in iter_array(path, 'panels'):
                    left, end = F(row['x_left']), F(row['x_right'])
                    if end != right or not 0 <= left < end <= 1:
                        raise ValueError('The complete true reverse source cover has a gap')
                    right = left
                    if [v[0] for v in row['modes']] != MODES or len(row['densities']) != D:
                        raise ValueError('A whole-mode or whole-density row is missing')
                    yield group, row
                    local_count += 1
                    count += 1
                if local_count != chunk['subpanels']:
                    raise ValueError('A complete chunk count differs')
            if count != group['subpanels'] or right != 0:
                raise ValueError('The complete source segment is missing')
    # First pass: total phi/source and chi/source positive masses.
    for group, row in rows():
        densities = [dyad(v) for v in row['densities']]
        if any(v < 0 for v in densities) or not 0 < dyad(row['local_V']) <= V0:
            raise ArithmeticError('The exact positive physical envelopes are invalid')
        for k, values in enumerate(row['modes']):
            ap, ac = dyad(values[5]), dyad(values[6])
            if ap < 0 or ac < 0:
                raise ArithmeticError('A source kernel mass is negative')
            for d in range(D):
                totals[k][d][0] += ap*densities[d]
                totals[k][d][1] += ac*densities[d]
        total_subpanels += 1
        if total_subpanels % 128 == 0:
            guard()
    if total_subpanels != sum(g['subpanels'] for g in doc['profile_groups']):
        raise ValueError('The complete source mass pass is missing')
    print(json.dumps(dict(event='physical46_ordered_totals_complete',
                          subpanels=total_subpanels,
                          elapsed_seconds=time.monotonic()-began)), flush=True)
    # Second pass: at this output panel, retain the ordering of every
    # source. Same-panel mass appears on both sides, a safe overbound.
    right_mass = [[[F(0), F(0)] for d in range(D)] for k in range(M)]
    maxima = [[[F(0), F(0)] for d in range(D)] for k in range(M)]
    where = [[['', ''] for d in range(D)] for k in range(M)]
    linear = [[F(0), F(0)] for k in range(M)]
    uniform_linear = [[F(0), F(0)] for k in range(M)]
    head = [[F(0), F(0)] for k in range(M)]
    uniform_head = [[F(0), F(0)] for k in range(M)]
    max_uniform_candidate_ratio = F(0)
    visited = 0
    try:
        for group, row in rows():
            V = dyad(row['local_V'])
            uniform_ratio = V/V0
            max_uniform_candidate_ratio = max(max_uniform_candidate_ratio, uniform_ratio)
            ds = [dyad(v) for v in row['densities']]
            loc = dict(cell=group['cell'], segment=group['segment'],
                       panel=row['panel'], subpanel=row['subpanel'],
                       x_left=row['x_left'], x_right=row['x_right'])
            for k, values in enumerate(row['modes']):
                m = MODES[k]
                pp, pk, cp, ck, ap, ac = [dyad(v) for v in values[1:]]
                if min(pp, pk, cp, ck, ap, ac) < 0:
                    raise ArithmeticError('A whole-field positive geometry entry is negative')
                for z, (pv, cv) in enumerate(((pp, cp), (pk, ck))):
                    lin = omega_upper[k]*pv*Qout[k]/S0[k]
                    linear[k][z] = max(linear[k][z], lin)
                    uniform_linear[k][z] = max(uniform_linear[k][z], lin*uniform_ratio)
                    head[k][z] = max(head[k][z], cv*lift_factor[k])
                    uniform_head[k][z] = max(uniform_head[k][z], cv*lift_factor[k]*uniform_ratio)
                    for d, definition in enumerate(density):
                        prefix_phi = totals[k][d][0]-right_mass[k][d][0]
                        suffix_chi = right_mass[k][d][1]+ac*ds[d]
                        if prefix_phi < 0 or suffix_chi < 0:
                            raise ArithmeticError('The source order subtraction became negative')
                        value = (cv*prefix_phi+pv*suffix_chi)/W[k]
                        if definition['output_angular_factor']:
                            value *= 1+m
                        if definition['output_envelope'] == 'uniform_V0':
                            value *= uniform_ratio
                        elif definition['output_envelope'] != 'local_V':
                            raise ValueError('An undeclared output norm was supplied')
                        if value > maxima[k][d][z]:
                            maxima[k][d][z], where[k][d][z] = value, loc
                for d in range(D):
                    right_mass[k][d][0] += ap*ds[d]
                    right_mass[k][d][1] += ac*ds[d]
            visited += 1
            if visited % 128 == 0:
                guard()
        if visited != total_subpanels or right_mass != totals:
            raise ValueError('The exact complete ordered source sums differ')
        mode_rows = []
        for k, m in enumerate(MODES):
            per_density = []
            axis = exact_point(axes[m]['half_axis']) if m in axes else None
            for d, definition in enumerate(density):
                bare_cut = totals[k][d][1]/W[k]
                # Source norm is W_tau,1 or W_tau,0 as explicitly tagged.
                source_angular_lower = angular[m][0]
                if not definition['output_angular_factor']:
                    source_angular_lower *= 1+m
                entry = dict(
                    density=definition['name'],
                    P_sup=dyadic_upper(maxima[k][d][0]),
                    K_sup=dyadic_upper(maxima[k][d][1]),
                    strong_output_row_sum=dyadic_upper(sum(maxima[k][d])),
                    maximizing_P_position=where[k][d][0],
                    maximizing_K_position=where[k][d][1],
                    total_phi_source_mass=dyadic_upper(totals[k][d][0]),
                    total_chi_source_mass=dyadic_upper(totals[k][d][1]),
                    canonical_cut_absolute_mode_bound=dyadic_upper(bare_cut/source_angular_lower),
                    canonical_cut_W_tau_1_mode_bound=dyadic_upper(
                        bare_cut*(1+m if definition['output_angular_factor'] else 1)))
                if axis is not None:
                    entry['canonical_cut_original_axis_ratio'] = dyadic_upper(
                        bare_cut/source_angular_lower/axis)
                per_density.append(entry)
            chi_b = doc['chi_at_true_cut'][str(m)]
            head_cut = Fb*absolute(chi_b[0])/W[k]
            mode_rows.append(dict(
                mode=m, densities=per_density,
                absolute_linear_centre_physical_norm=dyadic_upper(sum(linear[k])),
                absolute_linear_centre_uniform_norm=dyadic_upper(sum(uniform_linear[k])),
                complete_weighted_inner_K_trace_to_field_norm=dyadic_upper(sum(head[k])),
                complete_weighted_inner_K_trace_to_uniform_field_norm=dyadic_upper(sum(uniform_head[k])),
                inner_K_trace_to_canonical_cut_absolute=dyadic_upper(head_cut),
                actual_outer_Q=config['actual_outer_Q'][str(m)],
                actual_S0_Q=config['actual_true_S0_Q'][str(m)]))
        aggregate = []
        for d, definition in enumerate(density):
            all_rows = [sum(maxima[k][d]) for k in range(M)]
            chosen = max(range(M), key=lambda k: all_rows[k])
            aggregate.append(dict(
                density=definition['name'], definition=definition,
                all46_sum_of_separate_component_suprema=dyadic_upper(sum(all_rows)),
                selected_m2_m4_sum=dyadic_upper(all_rows[0]+all_rows[1]),
                largest_mode=MODES[chosen],
                largest_mode_row=dyadic_upper(all_rows[chosen]),
                all_input_frequencies_allowed=definition['source_norm'] == 'W_tau_0',
                input_cutoff_for_original_strong_density=(
                    None if definition['source_norm'] == 'W_tau_0' else 92)))
        centre_sum = sum(sum(v) for v in linear)
        centre_uniform = sum(sum(v) for v in uniform_linear)
        family_linear = sum(
            sum(linear[k])*(1+exact_point(axes[m]['relative_radius']))
            if m in axes else F(0) for k, m in enumerate(MODES))
        family_uniform = sum(
            sum(uniform_linear[k])*(1+exact_point(axes[m]['relative_radius']))
            if m in axes else F(0) for k, m in enumerate(MODES))
        gates = dict(
            complete_same_source_geometry_and_all_derived_hashes=True,
            all18_segments_all10793_original_positions_and_all_subpanels=True,
            both_exact_ordered_source_passes_equal=True,
            all46_modes_both_physical_components_separate_sup=True,
            all_nine_complete_mean_inverse_densities_retained=True,
            weak_sources_paid_explicit_one_plus_mode=True,
            uniform_input_output_conversion_and_candidate_norm_explicit=True,
            all20_actual_outer_affine_heights_and_true_head_trace_operator_retained=True)
        result = dict(
            status='Complete exact ordered low46 whole-field Green budget; nonlinear gates reported separately',
            author='exact_closure, GPT-6 Astra Pro (AI-assisted), 2026-11-12',
            all_gates=True, gates=gates,
            geometry_path=str(a.geometry), geometry_sha256=hashes[str(a.geometry)],
            geometry_entrypoint_sha256=config['entrypoint_sha256'],
            entrypoint_sha256=digest(__file__),
            densities=aggregate, mode_rows=mode_rows,
            counts=doc['counts'], total_subpanels=total_subpanels,
            all20_linear_centre_local_norm=dyadic_upper(centre_sum),
            all20_linear_centre_uniform_norm=dyadic_upper(centre_uniform),
            full_R74_outer_affine_family_local_norm=dyadic_upper(family_linear),
            full_R74_outer_affine_family_uniform_norm=dyadic_upper(family_uniform),
            crude_complete_candidate_local_strong_norm=dyadic_upper(F(40)*F(17, 16)),
            crude_complete_candidate_uniform_strong_norm=dyadic_upper(
                F(40)*F(17, 16)*max_uniform_candidate_ratio),
            head_weighted_l1_trace_to_local_field_operator=dyadic_upper(max(sum(v) for v in head)),
            head_weighted_l1_trace_to_uniform_field_operator=dyadic_upper(
                max(sum(v) for v in uniform_head)),
            no_infinite_output_Green_claim=True,
            no_full_outer_fixed_point_or_cut_consistency_claim=True,
            input_hashes=hashes,
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        guard()
        out = save(Path(str(a.out_prefix)+'.json'), result)
        print(json.dumps(dict(event='physical46_ordered_budget_complete', all_gates=True,
                              output=str(out), output_sha256=digest(out),
                              subpanels=total_subpanels,
                              elapsed_seconds=result['elapsed_seconds'],
                              peak_RSS_KiB=result['peak_RSS_KiB'])), flush=True)
    except Exception as error:
        save(Path(str(a.out_prefix)+'-failure.json'), dict(
            status='Incomplete exact ordered consumer; no mathematical impossibility inferred',
            error=repr(error), geometry_path=str(a.geometry),
            geometry_sha256=hashes[str(a.geometry)],
            completed_second_pass_subpanels=visited, total_subpanels=total_subpanels,
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__ == '__main__':
    main()
