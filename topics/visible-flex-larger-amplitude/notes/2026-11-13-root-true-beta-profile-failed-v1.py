#!/usr/bin/env python3
"""Intersect the R131 projected cut bounds with the complete true low46 beta.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
All R131 constant, full linear, quadratic and complete Taylor terms are
unchanged. Only a tighter bound on the same inner nonlinear DN correction
is used. This does not pay the outer nonlow feedback or close a surface.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from root_hybrid46_cut_consumer import exact as ex, up, record


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    start = time.monotonic()
    ids = read(a.inputs)
    gates = {}

    def gate(k, value):
        if not value:
            raise ArithmeticError(k)
        gates[k] = True

    def checked(k):
        r = ids[k]
        gate('identity_' + k, sha(r['path']) == r['sha256'])
        return read(r['path'])

    prior = checked('R131_profile')
    prior_resource = checked('R131_resource')
    beta = checked('complete_true_beta')
    beta_resource = checked('beta_resource')
    budget = checked('original_budget')
    axes = checked('original_axes')
    weights = checked('original_beta_weights')
    original = checked('original_cut')
    modes = list(range(2, 93, 2))
    gate('formal_prior_and_beta_exit0', prior_resource['exitcode'] == 0 == beta_resource['exitcode'])
    gate('complete_R131', prior['all_gates'] and prior['complete_mean_inverse_and_true_far_retained']
         and prior['unique_projected_low_cut_fixed_point_in_profile_domain']
         and not prior['full_frequency_cut_closed'])
    gate('complete_actual_true_beta', beta['all_gates'] and beta['complete_mean_inverse_far']
         and not beta['new_g_or_new_ODE_or_cut_fixedpoint_claimed'])
    gate('same_original_parameter_domain', ex(beta['domain']['S_product_radius']) == 1
         and ex(beta['domain']['T_l1_radius']) == F(1, 32))
    gate('same_original_Kbar_and_sigma_units', 'kappa_perp/true_w' in beta['units']
         and ex(beta['sigma']) == F(1, 64))
    gate('same_original_beta_identity', beta['input_identities']['old_beta']['sha256']
         == prior['inputs']['true_head']['sha256'])
    gate('same_original_budget_axes_and_cut', all(prior['inputs'][old]['sha256'] == ids[new]['sha256']
         for old, new in [('original_budget', 'original_budget'), ('original_axes', 'original_axes'),
                          ('original_cut', 'original_cut')]))
    gate('same_original_beta_weights', beta['input_identities']['cut_weights']['sha256']
         == ids['original_beta_weights']['sha256'] and weights['all_gates'])
    gate('all46_original_modes', modes == [r['mode'] for r in prior['rows']]
         == [r['mode'] for r in beta['mode_rows']] == [r['mode'] for r in budget['mode_rows']]
         == [r['mode'] for r in axes['rows']] == [r['mode'] for r in weights['source_mode_rows']])
    common = beta['common_bounds']['T_cut']
    gate('positive_true_far_retained_in_shared_T', ex(common['true_far_once']) > 0
         and ex(beta['complete_true_far_common_at_reference_width2']) > 0)
    gate('new_shared_complete_beta_no_worse', 0 < ex(common['chosen_complete'])
         <= ex(prior['T_true_head_paid_once']))
    fixed_keys = ('constant', 'complete_linear', 'complete_quadratic', 'complete_T_remainder')
    rows = []
    for p, b, br, axis, w in zip(prior['rows'], beta['mode_rows'], budget['mode_rows'],
                               axes['rows'], weights['source_mode_rows']):
        m = p['mode']
        gate('same_axis_' + str(m), ex(p['original_axis']) == ex(axis['chosen_axis']) == ex(w['axis']))
        raw_K = ex(b['Kbar']['chosen_complete'])
        # Kbar has no angular/strong Fourier factor. Apply the original
        # physical trace-to-cut bound and the original axis exactly once.
        from_raw = up(ex(br['inner_K_trace_to_canonical_cut_absolute'])*raw_K/ex(axis['chosen_axis']))
        from_weighted = ex(b['original_cut_weighted_beta_bound'])
        gate('two_positive_complete_beta_readouts_' + str(m), 0 < from_raw and 0 < from_weighted)
        head = min(ex(p['true_head_including_far']), from_raw, from_weighted)
        value = up(sum((ex(p[k]) for k in fixed_keys), F(0)) + head)
        gate('same_map_bound_no_worse_' + str(m), value <= ex(p['projected_map_value']))
        r = copy.deepcopy(p)
        r.update(true_head_including_far=record(head), projected_map_value=record(value),
                 proposed_T_coordinate_radius=record(2*value) if m >= 14 else None,
                 previous_R131_projected_map_value=p['projected_map_value'],
                 beta_raw_Kbar_bound=b['Kbar']['chosen_complete'],
                 beta_original_raw_trace_readout=record(from_raw),
                 beta_original_weighted_readout=b['original_cut_weighted_beta_bound'])
        gate('unchanged_all_other_terms_' + str(m), all(r[k] == p[k] for k in fixed_keys))
        rows.append(r)
    T_head = ex(common['chosen_complete'])
    T_tail = ex(prior['T_complete_shared_remainder_paid_once'])
    T_value = up(ex(original['T_constant_fixed_centre']) + ex(original['T_complete_linear_correction'])
                 + ex(original['T_quadratic_correction']) + T_tail + T_head)
    S_value = max(ex(r['projected_map_value']) for r in rows[:6])
    gate('shared_T_not_sum_of_individual_far', T_value <= ex(prior['T_projected_map']))
    gate('strict_projected_S_selfmap', S_value < F(1, 2))
    gate('strict_projected_T_selfmap', T_value < F(1, 36))
    gate('each_projected_T_coordinate_selfmap', all(0 < ex(r['projected_map_value'])
         < ex(r['proposed_T_coordinate_radius']) for r in rows[6:]))
    gate('unchanged_original_norm_contraction', ex(prior['original_norm_Lipschitz_bound']) < F(1, 20))
    gate('mode92_real_axis_gain', ex(rows[-1]['projected_map_value']) < F(1, 10**12))
    ans = dict(schema='R131-same-projected-cut-complete-true-beta-profile-v1',
        author='/root (GPT-6 Astra Pro, AI-assisted)', source_sha256=sha(__file__),
        helper_sha256=sha(Path(__file__).with_name('root_hybrid46_cut_consumer.py')),
        input_manifest_sha256=sha(a.inputs), inputs=ids, all_gates=all(gates.values()), gates=gates,
        rows=rows, S_projected_map=record(S_value), T_projected_map=record(T_value),
        T_complete_shared_remainder_paid_once=prior['T_complete_shared_remainder_paid_once'],
        T_true_head_paid_once=record(T_head),
        T_constant=original['T_constant_fixed_centre'],
        T_complete_linear=original['T_complete_linear_correction'],
        T_complete_quadratic=original['T_quadratic_correction'],
        domain=copy.deepcopy(prior['domain']),
        original_norm_Lipschitz_bound=prior['original_norm_Lipschitz_bound'],
        same_existing_R124_projected_low_solution=True,
        unique_projected_low_cut_fixed_point_in_profile_domain=True,
        complete_mean_inverse_and_true_far_retained=True,
        nonlow_feedback_or_full_frequency_cut_closed=False, closed_surface_claimed=False,
        same_original_axes_and_parameters=True, no_new_ODE_or_source_integral=True,
        elapsed_seconds=time.monotonic()-start, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if a.out.exists():
        raise FileExistsError(a.out)
    raw = (json.dumps(ans, separators=(',', ':'))+'\n').encode()
    if a.out.suffix == '.gz':
        raw = gzip.compress(raw, compresslevel=9, mtime=0)
    if len(raw) >= 5_000_000 or len(raw) > 1_000_000 and a.out.suffix != '.gz':
        raise ArithmeticError('Compress or partition output')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_bytes(raw)
    print(json.dumps(dict(all_gates=ans['all_gates'], gate_count=len(gates), result_sha256=sha(a.out),
        S_projected_map=float(S_value), T_projected_map=float(T_value),
        mode92_value=float(ex(rows[-1]['projected_map_value'])),
        mode92_axis_radius=float(ex(rows[-1]['proposed_T_coordinate_radius'])),
        projected_only=True, elapsed_seconds=ans['elapsed_seconds'], peak_rss_kib=ans['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
