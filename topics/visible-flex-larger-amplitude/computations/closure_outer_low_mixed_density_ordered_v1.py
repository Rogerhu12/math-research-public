#!/usr/bin/env python3
"""Prepared exact ordered low46 mixed-density consumer for R98.

This is a NEW source, not an executed numerical certificate.
Pure Fraction arithmetic reuses the complete pinned R90 geometry.
For each actual source leaf, the pinned weak_candidate_cap is at least
sigma^2*(s_sup+abs(ell)_sup)*V^2. Dividing that leaf's cap by
sigma^2*V^(2-p) majorizes the physical density (s+abs(ell))*V^p,
p=2,1,0. Sources retain their radial order in both passes. No V_min
division of an already aggregated operator is made.

The whole constant-strip output uses tau*=18/125. For a source on the
R93 variable strip tau(x)>=1/64, the optional transfer is conservatively
bounded by exp(m*(18/125-1/64)) per OUTPUT mode. This is an explicitly
paid finite-output strip cost, not a free width upgrade. Unknown high
fields remain in their declared physical/balanced norm.

Author: exact_closure, GPT-6 Astra Pro (AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import digest, iter_array
from closure_outer_physical_green_budget_recovered_v2 import (
    dyad, bounds, positive_abs_lower, exp_bounds, dyadic_upper,
    fraction_record, save)

EXPECTED_SOURCES = {
    'closure_split_joint_io_v2.py':
        '6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0',
    'closure_outer_physical_green_budget_recovered_v2.py':
        'e2113502398ebb1d4649a82a813ef0d6f2f90802ef9da52cbac8e37d36a39d83',
    'closure_outer_physical_green_geometry_recovered_v2.py':
        'c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829',
}
GEOMETRY_SHA = 'e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03'
REFERENCE_BUDGET_SHA = '86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45'
MODES = list(range(2, 93, 2))
POWERS = (2, 1, 0)
SIGMA = F(17, 16)
TAU_TARGET = F(18, 125)
TAU_SOURCE_MIN = F(1, 64)
V0 = F(1, 2**40)


def exact_dimension(row):
    return [dyad(row['local_V']),
            [dyad(x) for x in row['densities']]]


def physical_density_bounds(row, source_index):
    V, densities = exact_dimension(row)
    if not 0 < V <= V0 or any(v < 0 for v in densities):
        raise ArithmeticError('The same exact positive source envelope is required')
    cap = densities[source_index]
    if not cap > 0:
        raise ArithmeticError('A true positive c*V^2 cap must be strictly positive')
    # These are sourcewise conservative upper densities, NOT equalities
    # for the actual varying background coefficient c(x).
    return V, [cap/(SIGMA*SIGMA*V**(2-p)) for p in POWERS]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry', type=Path, required=True)
    ap.add_argument('--reference-budget', type=Path, required=True)
    ap.add_argument('--profile-root', type=Path)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--rss-kib', type=int, default=40960)
    args = ap.parse_args()
    began = time.monotonic()
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    for suffix in ('.json', '.json.gz', '-failure.json', '-failure.json.gz',
                   '.json.partial', '-failure.json.partial'):
        if Path(str(args.out_prefix)+suffix).exists():
            raise FileExistsError('A previous primary or failure must not be overwritten')
    for name, sha in EXPECTED_SOURCES.items():
        if digest(Path(__file__).with_name(name)) != sha:
            raise ValueError('A frozen mathematical/helper source differs: '+name)
    if digest(args.geometry) != GEOMETRY_SHA:
        raise ValueError('This entrypoint requires the complete actually paid R90 geometry')
    if digest(args.reference_budget) != REFERENCE_BUDGET_SHA:
        raise ValueError('The exact old cap-operator identity needs its complete old budget')
    doc = json.loads(args.geometry.read_text())
    ref = json.loads(args.reference_budget.read_text())
    cfg = doc['config']
    if (not doc['all_gates'] or not all(doc['gates'].values())
            or not ref['all_gates'] or not all(ref['gates'].values())
            or cfg['modes'] != MODES or cfg['cells'] != [11, 10]
            or cfg['parameter_sigma'] != '17/16'
            or cfg['entrypoint_sha256'] != EXPECTED_SOURCES[
                'closure_outer_physical_green_geometry_recovered_v2.py']
            or ref['geometry_sha256'] != GEOMETRY_SHA
            or ref['entrypoint_sha256'] != EXPECTED_SOURCES[
                'closure_outer_physical_green_budget_recovered_v2.py']):
        raise ValueError('The complete actual geometry/budget identities are unpaid')
    defs = cfg['densities']
    indices = [i for i, d in enumerate(defs)
               if d['name'] == 'weak_candidate_cap']
    if len(indices) != 1:
        raise ValueError('The complete weak cap is not uniquely identified')
    source_index = indices[0]
    d = defs[source_index]
    if (d['source_norm'] != 'W_tau_0'
            or d['output_envelope'] != 'local_V'
            or d['output_angular_factor'] is not True):
        raise ValueError('The original complete weak source uses different units')
    groups = doc['profile_groups']
    expected_order = [(n, j) for n in (10, 11) for j in range(8, -1, -1)]
    if [(g['cell'], g['segment']) for g in groups] != expected_order:
        raise ValueError('Retain all18 actual groups in physical reverse order')
    if sum(g['original_panels'] for g in groups) != 10793:
        raise ValueError('The true material cover is incomplete')
    W = [positive_abs_lower(cfg['true_physical_Wronskians'][str(m)])
         for m in MODES]
    angular = [exp_bounds(m*TAU_TARGET) for m in MODES]
    gap = TAU_TARGET-TAU_SOURCE_MIN
    transfer = [exp_bounds(m*gap)[1] for m in MODES]
    hashes = {str(args.geometry): GEOMETRY_SHA,
              str(args.reference_budget): REFERENCE_BUDGET_SHA}
    trace_V_candidates = []
    def guard():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > args.rss_kib:
            raise MemoryError('Observed owned RSS exceeds declared stop threshold: '+str(peak))
    def profile_path(item):
        exact = Path(item['path'])
        if exact.is_file():
            chosen = exact
        elif args.profile_root is not None:
            chosen = args.profile_root/exact.name
        else:
            raise FileNotFoundError('Restore this hash-bound derived profile: '+str(exact))
        if digest(chosen) != item['sha256']:
            raise ValueError('An actual derived profile has changed bytes: '+str(chosen))
        hashes[str(chosen)] = item['sha256']
        return chosen
    def rows():
        for g in groups:
            right = F(1)
            count = 0
            for chunk in g['chunks']:
                path = profile_path(chunk)
                own = 0
                for row in iter_array(path, 'panels'):
                    left, end = F(row['x_left']), F(row['x_right'])
                    if end != right or not 0 <= left < end <= 1:
                        raise ValueError('The complete true reverse cover has a gap')
                    right = left
                    if (len(row['densities']) != len(defs)
                            or [v[0] for v in row['modes']] != MODES):
                        raise ValueError('A full mode/density row is missing')
                    yield g, row
                    own += 1
                    count += 1
                if own != chunk['subpanels']:
                    raise ValueError('A true working chunk is incomplete')
            if count != g['subpanels'] or right != 0:
                raise ValueError('A complete real source segment is missing')
    totals = [[[F(0), F(0)] for p in POWERS] for m in MODES]
    maxima = [[[F(0), F(0)] for p in POWERS] for m in MODES]
    where = [[[None, None] for p in POWERS] for m in MODES]
    right_mass = [[[F(0), F(0)] for p in POWERS] for m in MODES]
    count = visited = 0
    try:
        guard()
        for g, row in rows():
            V, ds = physical_density_bounds(row, source_index)
            if g['cell'] == 11 and g['segment'] == 0 and F(row['x_left']) == 0:
                trace_V_candidates.append(dict(
                    source_cell=11, source_segment=0, original_panel=row['panel'],
                    subpanel=row['subpanel'], local_V=row['local_V'],
                    side='outer right-hand value at the true node12 cut',
                    x_left=row['x_left'], x_right=row['x_right']))
            for k, values in enumerate(row['modes']):
                if len(values) != 7:
                    raise ValueError('The actual positive Green row schema changed')
                ap, ac = dyad(values[5]), dyad(values[6])
                if min(ap, ac) < 0:
                    raise ArithmeticError('A true source mass is negative')
                for j in range(3):
                    totals[k][j][0] += ap*ds[j]
                    totals[k][j][1] += ac*ds[j]
            count += 1
            if count % 128 == 0:
                guard()
        if count != sum(g['subpanels'] for g in groups) or len(trace_V_candidates) != 1:
            raise ValueError('The complete source pass or the true cut envelope is missing')
        print(json.dumps(dict(event='mixed_low46_source_totals_complete',
                              subpanels=count)), flush=True)
        for g, row in rows():
            V, ds = physical_density_bounds(row, source_index)
            loc = dict(cell=g['cell'], segment=g['segment'],
                       original_panel=row['panel'], subpanel=row['subpanel'],
                       x_left=row['x_left'], x_right=row['x_right'])
            for k, values in enumerate(row['modes']):
                pp, pk, cp, ck, aphi, achi = [dyad(z) for z in values[1:]]
                if min(pp, pk, cp, ck, aphi, achi) < 0:
                    raise ArithmeticError('A true target/source coefficient is negative')
                for j in range(3):
                    prefix_phi = totals[k][j][0]-right_mass[k][j][0]
                    suffix_chi = right_mass[k][j][1]+achi*ds[j]
                    if prefix_phi < 0 or suffix_chi < 0:
                        raise ArithmeticError('The exact ordered source difference is negative')
                    for component, (pv, cv) in enumerate(((pp, cp), (pk, ck))):
                        value = (1+MODES[k])*(cv*prefix_phi+pv*suffix_chi)/W[k]
                        if value > maxima[k][j][component]:
                            maxima[k][j][component] = value
                            where[k][j][component] = loc
                    right_mass[k][j][0] += aphi*ds[j]
                    right_mass[k][j][1] += achi*ds[j]
            visited += 1
            if visited % 128 == 0:
                guard()
        if visited != count or right_mass != totals:
            raise ValueError('Both complete ordered passes must have the same exact source mass')
        refrows = {r['mode']: r for r in ref['mode_rows']}
        output = []
        for k, m in enumerate(MODES):
            old = next(x for x in refrows[m]['densities']
                       if x['density'] == 'weak_candidate_cap')
            # Dividing every density by the same sigma^2 commutes exactly
            # with the ordered p=2 integral and separate radial maxima.
            if (maxima[k][0][0] > dyad(old['P_sup'])/(SIGMA*SIGMA)
                    or maxima[k][0][1] > dyad(old['K_sup'])/(SIGMA*SIGMA)
                    or totals[k][0][0] > dyad(old['total_phi_source_mass'])/(SIGMA*SIGMA)
                    or totals[k][0][1] > dyad(old['total_chi_source_mass'])/(SIGMA*SIGMA)):
                raise ArithmeticError('The recomputed p=2 operator does not reproduce the paid cap comparison')
            ds = []
            for j, power in enumerate(POWERS):
                gamma = sum(maxima[k][j])
                cut = totals[k][j][1]/W[k]
                ds.append(dict(
                    V_power=power,
                    source_density='(s+abs(ell))*V^'+str(power),
                    majorant_source_definition='old_weak_cap/(sigma^2*V^(2-p)) at each original leaf',
                    P_sup=dyadic_upper(maxima[k][j][0]),
                    K_sup=dyadic_upper(maxima[k][j][1]),
                    constant_strip_strong_output_row=dyadic_upper(gamma),
                    variable_to_constant_strong_output_row=dyadic_upper(gamma*transfer[k]),
                    strip_transfer_upper=dyadic_upper(transfer[k]),
                    maximizing_P_position=where[k][j][0],
                    maximizing_K_position=where[k][j][1],
                    total_phi_source_mass=dyadic_upper(totals[k][j][0]),
                    total_chi_source_mass=dyadic_upper(totals[k][j][1]),
                    canonical_cut_constant_strip_absolute=dyadic_upper(cut/angular[k][0]),
                    canonical_cut_variable_strip_absolute=dyadic_upper(cut*transfer[k]/angular[k][0]),
                    canonical_cut_W_tau_target_1=dyadic_upper((1+m)*cut),
                    canonical_cut_variable_to_W_tau_target_1=dyadic_upper((1+m)*cut*transfer[k])))
            output.append(dict(mode=m, densities=ds))
        aggregate = []
        for j, power in enumerate(POWERS):
            constant = sum(sum(maxima[k][j]) for k in range(len(MODES)))
            variable = sum(sum(maxima[k][j])*transfer[k] for k in range(len(MODES)))
            aggregate.append(dict(
                V_power=power,
                constant_strip_all46_sum=dyadic_upper(constant),
                variable_to_constant_all46_sum=dyadic_upper(variable),
                sum_of_separate_mode_and_component_suprema=True))
        refagg = next(x for x in ref['densities'] if x['density'] == 'weak_candidate_cap')
        if sum(sum(maxima[k][0]) for k in range(len(MODES))) > (
                dyad(refagg['all46_sum_of_separate_component_suprema'])/(SIGMA*SIGMA)):
            raise ArithmeticError('The complete p=2 sum exceeds the old paid comparison')
        gates = dict(
            actual_original_geometry_and_old_budget_sha_verified=True,
            all18_actual_groups_and10793_original_panels=True,
            all46_modes_and_both_physical_components=True,
            same_local_exact_positive_V_and_source_units=True,
            old_complete_weak_cap_majorizes_each_material_density=True,
            sourcewise_division_before_ordered_integration=True,
            no_global_Vmin_replacement=True,
            both_ordered_passes_exactly_agree=True,
            p2_independently_bounded_by_old_paid_operator=True,
            every_output_one_plus_mode_retained=True,
            explicit_variable_to_constant_strip_cost=True,
            true_cut_envelope_obtained_from_complete_source_cover=True)
        result = dict(
            status='Complete exact mixed-density low46 linear bounds only',
            entrypoint_sha256=digest(__file__),
            frozen_source_hashes=EXPECTED_SOURCES,
            geometry_sha256=GEOMETRY_SHA,
            old_budget_sha256=REFERENCE_BUDGET_SHA,
            input_hashes=hashes,
            all_gates=all(gates.values()), gates=gates,
            modes=MODES, V_powers=list(POWERS),
            tau_target=fraction_record(TAU_TARGET),
            source_strip_min=fraction_record(TAU_SOURCE_MIN),
            maximum_strip_gap=fraction_record(gap),
            original_panels=10793, subpanels=count,
            densities=aggregate, mode_rows=output,
            true_cut_local_V=trace_V_candidates[0],
            actual_true_cut_radius=cfg['actual_true_cut_radius'],
            actual_true_cut_w=cfg['actual_true_cut_w'],
            complete_mean_and_inverse_not_deleted_from_nonlinear_R98_bounds=True,
            nonlinear_R98_rows_not_evaluated=True,
            middle94plus_not_computed=True,
            full_low_middle_high_fixed_point_not_claimed=True,
            full_cut_or_closed_surface_not_claimed=True,
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        guard()
        out = save(Path(str(args.out_prefix)+'.json'), result)
        print(json.dumps(dict(event='mixed_low46_ordered_complete',
                              all_gates=True, output=str(out),
                              output_sha256=digest(out),
                              elapsed_seconds=result['elapsed_seconds'],
                              peak_RSS_KiB=result['peak_RSS_KiB'])), flush=True)
    except Exception as error:
        save(Path(str(args.out_prefix)+'-failure.json'), dict(
            status='Incomplete mixed-density arithmetic; no mathematical impossibility inferred',
            error_type=type(error).__name__, error=str(error),
            entrypoint_sha256=digest(__file__), input_hashes=hashes,
            completed_source_rows=count, completed_target_rows=visited,
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__ == '__main__':
    main()
