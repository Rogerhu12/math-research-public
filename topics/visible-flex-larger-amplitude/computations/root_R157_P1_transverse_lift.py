#!/usr/bin/env python3
"""Restrict the same R100 lift to a certified domain containing R143's a*.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
R156 estimates apply only on the real restriction of the prior actual P.
All original axes, unit columns, continuous strip, and positive far remain.
No ODE, source integral, or new fixed-point solve is performed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from root_hybrid46_cut_consumer import exact as ex, up

DOMAIN = 'R156_actual_full_cut_posterior'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def rat(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator))


def pack(v):
    v = up(v, 160)
    return [str(v.numerator), -(v.denominator.bit_length()-1)] if v else ['0', 0]


def support(coefficients, caps, total):
    value, left = F(0), total
    for i in sorted(range(len(caps)), key=lambda i: coefficients[i], reverse=True):
        take = min(left, caps[i])
        value += coefficients[i] * take
        left -= take
        if left == 0:
            break
    return up(value, 160)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Preserve every original attempt')
    start = time.monotonic()
    ids, gates = read(a.inputs), {}

    def gate(name, value):
        if not value:
            raise ArithmeticError(name)
        gates[name] = True

    def checked(name):
        rec = ids[name]
        gate('identity_' + name, sha(rec['path']) == rec['sha256'])
        return read(rec['path'])

    original = checked('original_lift')
    posterior = checked('R156_posterior')
    prior_lift = checked('prior_lift')
    contraction = checked('R143_contraction')
    for name in ('R156_resource', 'R143_resource', 'prior_lift_resource'):
        r = checked(name)
        gate('formal_completed_' + name, r['exitcode'] == 0 and r.get('termination_signal') is None)
    for name, obj in [('original', original), ('posterior', posterior), ('contraction', contraction), ('prior_lift', prior_lift)]:
        gate('all_existing_gates_' + name, obj['all_gates'] and all(obj['gates'].values()))
    modes, cells = list(range(2, 93, 2)), list(range(12, 225))
    prior_domain = prior_lift['domains'][0]
    bounds = posterior['same_a_star_bounds']['rows']
    gate('all_original_213_cells_and46_modes', original['cells'] == cells and original['modes'] == modes
         and [r['cell'] for r in original['rows']] == cells and [r['mode'] for r in bounds] == modes
         and [r['mode'] for r in contraction['rows']] == modes)
    gate('R156_exact_prior_domain_and_membership', prior_lift['same_R143_unique_a_star_in_new_domain']
         and prior_lift['existing_R100_field_restricted_not_new_field']
         and posterior['same_parameter_domain']['name'] == prior_domain['name'] == 'R148_actual_full_cut_posterior'
         and posterior['same_parameter_domain']['T_coordinate_caps_by_mode'] == prior_domain['original_normalized_T_coordinate_caps']
         and ex(posterior['same_parameter_domain']['S_product_radius']) == ex(prior_domain['S_linf_radius']) == F(3,8)
         and ex(posterior['same_parameter_domain']['T_l1_radius']) == ex(prior_domain['T_l1_radius']) == F(1,64))
    gate('same_complete_fixedpoint', contraction['same_complete_R127_field_and_R141_cut']
         and contraction['unique_real_fixed_point_in_K_and_original_working_domain']
         and posterior['same_existing_R127_field'] and posterior['same_a_star_bounds']['same_unique_R143_fixed_point']
         and posterior['complete_mean_inverse_and_infinite_high_retained']
         and posterior['all185_windows_and_original_source_materials_retained']
         and not posterior['whole_P_parameter_selfmap_claimed'])
    gate('original_auxiliary_interface', ex(original['transverse_radius']) == F(1, 32)
         and original['full_head_correction_e_still_separate']
         and not original['full_head_source_or_high_trace_certified'])
    K = contraction['K']
    sr, tr = ex(K['S_linf_radius']), ex(K['T_l1_radius'])
    gate('K_subset_of_exact_posterior_domain', sr == F(3, 8) and tr == F(1, 64)
         and K['complex_balanced_convex_norm'])
    parent = [F(0)]*6 + list(map(ex, K['T_coordinate_radii']))
    gate('original40_transverse_axes', len(parent) == 46 and all(z > 0 for z in parent[6:]))
    caps, membership = [F(0)]*6, []
    for i, (row, kr) in enumerate(zip(bounds, contraction['rows'])):
        full = ex(row['same_original_full_fixed_point_coordinate_bound'])
        gate('complete_bound_is_projected_plus_nonlow_' + str(row['mode']),
             full >= ex(row['projected_bound']) + ex(row['complete_nonlow_correction']))
        if i < 6:
            membership.append(dict(mode=row['mode'], group='S', retained_radius=rat(sr),
                                   same_a_star_R156_coordinate_bound=rat(full)))
            continue
        gate('same_K_coordinate_axis_' + str(row['mode']), parent[i] == ex(kr['K_radius']))
        previous_cap=ex(prior_domain['original_normalized_T_coordinate_caps'][i])
        cap = min(parent[i], previous_cap, up(full, 192))
        gate('intersection_contains_same_a_star_' + str(row['mode']), 0 < cap <= min(parent[i], previous_cap))
        gate('cap_contains_known_intersection_' + str(row['mode']), cap >= min(parent[i], previous_cap, full))
        caps.append(cap)
        membership.append(dict(mode=row['mode'], group='T', R143_K_radius=rat(parent[i]),
                               R156_same_a_star_coordinate_bound=rat(full), retained_radius=rat(cap)))
    gate('all46_caps_completed', len(caps) == 46 and caps[:6] == [0]*6)
    rows = []
    for row in original['rows']:
        units = list(map(ex, row['transverse_unit_axis_pairs']))
        gate('all46_original_unit_columns_' + str(row['cell']), len(units) == 46 and all(x >= 0 for x in units))
        pair = [up(v*min(c, tr), 160) for v, c in zip(units, caps)]
        shared = support(units, caps, tr)
        oldpair = list(map(ex, row['Lambda_pair_caps_at_radius1over32']))
        gate('all46_restrict_parent_' + str(row['cell']), all(0 <= x <= y for x, y in zip(pair, oldpair)))
        gate('shared_mass_restricts_parent_' + str(row['cell']), 0 < shared <= ex(row['Lambda_common_cap_at_radius1over32']))
        rows.append(dict(cell=row['cell'], Lambda_pair_caps_on_domain=list(map(pack, pair)),
                         Lambda_common_cap_on_domain=pack(shared),
                         original_unit_columns_sha256=ids['original_lift']['sha256'],
                         actual_all46_original_unit_columns_retained=True))
    far = support(list(map(ex, original['far_unit_axis_pairs_unscaled_by_S'])), caps, tr)
    gate('complete_positive_original_transverse_far', 0 < far <= ex(original['far_common_at_radius1over32']))
    domain = dict(name=DOMAIN, S_linf_radius=rat(sr), T_l1_radius=rat(tr),
                  original_normalized_T_coordinate_caps=list(map(rat, caps)),
                  coordinate_constraints_and_shared_T_mass_are_simultaneous=True,
                  C_S_may_keep_original_unit_S_caps_conservatively=True,
                  rows=rows, transverse_far_common_unscaled_by_S=pack(far),
                  complete_auxiliary_far_must_be_added_separately=True, full_e_feedback_still_required=True,
                  same_existing_full_fixed_point_membership=membership)
    ans = dict(schema='R157-actual213-transverse-lift-fixedpoint-posterior-v1',
               author='/root (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
               helper_sha256=sha(Path(__file__).with_name('root_hybrid46_cut_consumer.py')),
               input_manifest_sha256=sha(a.inputs), inputs=ids, all_gates=True, gates=gates,
               gate_count=len(gates), modes=modes, cells=cells, normalization=original['normalization'],
               original_continuous_strip_origin=original['exact_original_continuous_strip_origin'],
               original_axis_formulas_unchanged=True, domains=[domain],
               same_R143_unique_a_star_in_new_domain=True,
               posterior_membership_uses_only_real_a_star=True,
               complex_absolute_coordinate_domain_is_subset_of_original_R100=True,
               prior_domain_retained_without_relabelling=prior_domain,
               existing_R100_field_restricted_not_new_field=True,
               Cs_full_unit_S_bound_kept_conservatively=True,
               no_complete_new_beta_or_outer_extension_claimed=True,
               new_ODE_or_source_integrals=0, elapsed_seconds=time.monotonic()-start,
               peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw = gzip.compress((json.dumps(ans, separators=(',', ':'))+'\n').encode(), compresslevel=9, mtime=0)
    if len(raw) >= 5_000_000:
        raise ArithmeticError('Partition oversized primary')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_bytes(raw)
    print(json.dumps(dict(all_gates=True, gates=len(gates), sha256=sha(a.out), bytes=len(raw),
                         cell12_Lambda92=float(ex(rows[0]['Lambda_pair_caps_on_domain'][-1])),
                         cell12_shared=float(ex(rows[0]['Lambda_common_cap_on_domain'])),
                         mode92_T_cap=float(caps[-1]), elapsed_seconds=ans['elapsed_seconds'],
                         peak_rss_kib=ans['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
