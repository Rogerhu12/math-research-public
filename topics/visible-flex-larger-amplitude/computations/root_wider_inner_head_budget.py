#!/usr/bin/env python3
"""Actual same-field width budgets; never promote finite reweighting to a tail.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
The positive saved-cap expressions below are sufficient majorants, not lower
bounds for the actual solution.  An oversized expression proves only that
this explicit method has not paid a domain gate.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def ex(value, side='upper'):
    if isinstance(value, int):
        return F(value)
    if isinstance(value, dict):
        if side in value:
            return ex(value[side])
        if 'numerator' in value:
            return F(int(value['numerator']), int(value['denominator']))
        return F(int(value['mantissa'])) * F(2) ** int(value['binary_exponent'])
    if isinstance(value[1], int):
        return F(int(value[0])) * F(2) ** value[1]
    return F(int(value[0]), int(value[1]))


def exact(value):
    value = F(value)
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


def ball(value):
    value = F(value)
    return arb(value.numerator) / arb(value.denominator)


def endpoint(value):
    m, e = value.man_exp()
    return {'mantissa': str(m), 'binary_exponent': int(e)}


def rec(value):
    return {'lower': endpoint(value.lower()), 'upper': endpoint(value.upper()),
            'display': str(value)}


def exp_exact(value):
    return ball(value).exp()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('A fresh immutable output prefix is required')
    started = time.monotonic()
    ctx.prec = 256
    identity = load(a.inputs)
    gates = {}

    def gate(name, condition):
        gates[name] = bool(condition)
        if not condition:
            raise ArithmeticError(name)

    docs = {}
    for name, entry in identity['inputs'].items():
        gate('sha_' + name, sha(entry['path']) == entry['sha256'])
        if name in ('density', 'Cs_Lambda_modal', 'Cs_Lambda_source', 'full_existing_e'):
            docs[name] = load(entry['path'])
    d = docs['density']
    m = docs['Cs_Lambda_modal']
    e = docs['full_existing_e']
    source = docs['Cs_Lambda_source']
    gate('all_original_density_gates', all(d['gates'].values()))
    gate('all_existing_complete_field_gates', all(m['gates'].values()) and
         all(e['gates'].values()) and all(source['gates'].values()))
    cells = list(range(12, 225))
    gate('all213_original_cells', [r['cell'] for r in d['rows']] == cells and
         [r['cell'] for r in m['rows']] == cells and [r['cell'] for r in e['rows']] == cells)
    gate('same_expanded_parameter_domain', m['domain'] == e['domain'] == source['domain'])
    gate('original_46_modes', m['modes'] == list(range(2, 93, 2)))
    windows = [[94, 94], [96, 96], [98, 104], [106, 112], [114, 128],
               [130, 184], [186, 192], [194, 256], [258, 512],
               [514, 1024], [1026, 2048], [2050, 4096], [4098, 8190]]
    gate('all13_existing_finite_windows', e['windows'] == windows)
    gate('original_q_strip_is_explicit_not_redefined',
         d['continuous_strip_origin']['do_not_renormalize_using_new_strong_density'] and
         'original q' in d['continuous_strip_definition'])
    gate('complete_mean_inverse_far', e['complete_mean_inverse_far'])
    scale = F(257, 256)
    # R100 V' is fixed; this diagnostic does not change it or the actual field.
    gate('R100_envelope_scale', ex(m['R100_envelope_scale']) == scale)
    rows = []
    for dr, mr, er in zip(d['rows'], m['rows'], e['rows']):
        n = dr['cell']
        gate('finite_pair_count_' + str(n), len(mr['Cs_plus_Lambda_pair_caps']) ==
             len(er['low_mode_caps']) == 46 and len(er['window_caps']) == 13)
        gate('positive_true_infinity_' + str(n), ex(er['complete_infinite_cap']) > 0)
        gate('ordered_positive_original_strip_' + str(n),
             ex(dr['tau_inner']) > ex(dr['tau_outer']) > 0)
        rows.append({'cell': n, 'tau_inner': dr['tau_inner'],
                     'tau_outer': dr['tau_outer'],
                     'relative_physical_normalization_upper': exact(scale * ex(dr['V_over_w_upper'])),
                     'positive_original_complete_infinite_cap': er['complete_infinite_cap']})

    dr, mr, er = d['rows'][0], m['rows'][0], e['rows'][0]
    tin, tout = ex(dr['tau_inner']), ex(dr['tau_outer'])
    M = d['cutoff']
    gate('original_infinite_split_8192', M == 8192)
    beta, eta = ex(dr['beta_integral_upper']), ex(dr['eta_integral_upper'])
    material = scale * ex(dr['density_integral_upper'])
    base_cost = beta + eta / M
    ceiling = tin - base_cost
    gate('positive_fixed_entrance_linear_budget', F(3, 8) < ceiling < F(2, 5))
    trials = []
    for multiplier in [1, 2, 4, 16, 256, 65536]:
        new_k = scale * ex(d['k']) * multiplier
        gamma = 2 * new_k * (1 + F(1, M))
        exit_width = ceiling - material / new_k
        gate('finite_k_strictly_below_fixed_entrance_ceiling_' + str(multiplier),
             exit_width < ceiling)
        trials.append({'multiplier_of_scaled_R42_k': multiplier,
                       'new_k': exact(new_k), 'complete_high_linear_Green_gamma': exact(gamma),
                       'assigned_exit_width_from_saved_material_upper': exact(exit_width),
                       'new_auxiliary_strip_only': True,
                       'existing_field_in_new_strip_not_proved': True})
    target = F(1, 4)
    gap = ceiling - target
    gate('quarter_linear_width_feasible', gap > 0)
    k_quarter = material / gap
    gate('quarter_budget_exact_identity', base_cost + material / k_quarter == tin - target)
    # This is an exact linear-budget construction.  No high fixed point or
    # identification with the existing R100 field is asserted.
    low = [ex(x) + ex(y) for x, y in zip(mr['Cs_plus_Lambda_pair_caps'], er['low_mode_caps'])]
    mid = [ex(x) for x in er['window_caps']]
    A = scale * ex(dr['V_over_w_upper'])
    gate('all_low_and_middle_saved_caps_nonnegative', all(x >= 0 for x in low + mid))
    width_tests = []
    for width in [F(1, 4), F(1, 2), F(1), F(5, 4), F(3, 2), F(2), F(3), F(33, 5)]:
        delta = max(F(0), width - tout)
        low_terms = [ball(A * cap) * exp_exact((2 * i + 2) * delta)
                     for i, cap in enumerate(low)]
        middle_terms = [ball(A * cap) * exp_exact(win[1] * delta)
                        for cap, win in zip(mid, windows)]
        low_total = sum(low_terms, arb(0))
        middle_total = sum(middle_terms, arb(0))
        finite_total = low_total + middle_total
        low_pass = bool(low_total < ball(F(1, 64)))
        mid_pass = bool(finite_total < ball(F(1, 64)))
        gate('strict_saved_cap_comparison_' + str(width),
             (low_total < ball(F(1, 64)) or low_total > ball(F(1, 64))) and
             (finite_total < ball(F(1, 64)) or finite_total > ball(F(1, 64))))
        width_tests.append({'target_constant_width': exact(width), 'max_old_to_new_shift': exact(delta),
                            'finite_low46_physical_majorant': rec(low_total),
                            'finite_13windows_physical_majorant': rec(middle_total),
                            'finite_all_below8192_physical_majorant': rec(finite_total),
                            'log2_low46_majorant': rec(low_total.log() / arb(2).log()),
                            'log2_all_finite_majorant': rec(finite_total.log() / arb(2).log()),
                            'low46_saved_majorant_pays_1_over64': low_pass,
                            'all_finite_saved_majorant_pays_1_over64': mid_pass,
                            'oversized_majorant_is_not_an_actual_solution_lower_bound': True})
    gate('low46_naive_majorant_pays_width1', width_tests[2]['low46_saved_majorant_pays_1_over64'])
    gate('low46_naive_majorant_does_not_pay_width2', not width_tests[5]['low46_saved_majorant_pays_1_over64'])
    gate('finite_window_naive_majorant_does_not_pay_quarter', not width_tests[0]['all_finite_saved_majorant_pays_1_over64'])
    # A positive cap of all >=8192 modes carries no additional exponential
    # moment.  The exact mode examples witness failure of that implication.
    infinite_cap = ex(er['complete_infinite_cap'])
    far_source = ex(e['complete_infinite_far_source'])
    fixed_far = ex(e['fixed_far_cap'])
    gate('distinct_positive_infinite_far_obligations', infinite_cap > 0 and far_source > 0 and fixed_far > 0)
    delta = F(1, 1024)
    witness_modes = [8192, 16384, 32768, 65536]
    infinity_witness = []
    for mode in witness_modes:
        factor = exp_exact(delta * mode)
        infinity_witness.append({'even_mode': mode,
                                 'positive_width_shift': exact(delta),
                                 'norm_ratio_for_one_mode_of_fixed_original_strong_mass': rec(factor)})
        gate('single_mode_growth_' + str(mode), factor > 1)
    out = {'schema': 'original-inner-head-width-budget-and-no-free-infinite-reweight-v1',
           'author': '/root (GPT-6 Astra Pro, AI-assisted)',
           'source_sha256': sha(__file__), 'input_interface_sha256': sha(a.inputs),
           'inputs': identity['inputs'], 'precision_bits': ctx.prec,
           'all_gates': all(gates.values()), 'gates': gates, 'gate_count': len(gates),
           'same_original_R100_field': True, 'complete_existing_field': 'Cs+Lambda+e',
           'original_q_continuous_strip_not_changed': True,
           'all213_original_widths_and_infinite_caps': rows,
           'cell12_fixed_entrance_material_budget': {
               'tau_inner': exact(tin), 'tau_outer_original': exact(tout),
               'beta_plus_eta_over8192_saved_upper': exact(base_cost),
               'scaled_positive_material_upper': exact(material),
               'exit_budget_supremum_as_k_tends_to_infinity': exact(ceiling),
               'strictly_a_ceiling_for_this_saved_sufficient_budget_not_the_PDE': True,
               'trials': trials,
               'quarter_target_k': exact(k_quarter),
               'quarter_target_high_linear_Green_gamma': exact(2*k_quarter*(1+F(1,M))),
               'quarter_actual_full_field_or_nonlinear_solution_not_certified': True},
           'finite_saved_cap_reweight_tests': width_tests,
           'infinity_no_free_upgrade': {
               'original_complete_infinite_cap': er['complete_infinite_cap'],
               'complete_infinite_far_source': e['complete_infinite_far_source'],
               'fixed_far_cap': e['fixed_far_cap'],
               'single_mode_examples': infinity_witness,
               'unbounded_operator_norm_for_every_positive_strip_increase': True,
               'no_nonanalyticity_or_nonexistence_of_actual_field_claim': True},
           'new_complete_wider_field_proved': False,
           'new_ODE_Green_or_radial_integrals': 0,
           'no_threshold_or_source_or_far_parameter_changed': True,
           'elapsed_seconds': time.monotonic()-started,
           'peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(out, indent=2)+'\n').encode()
    if len(raw) >= 1_000_000:
        raise ValueError('Use gzip for a large ledger')
    a.out.write_bytes(raw)
    print(json.dumps({'all_gates': out['all_gates'], 'gate_count': len(gates),
                      'fixed_entrance_budget_ceiling': float(ceiling),
                      'quarter_linear_k': float(k_quarter),
                      'quarter_linear_gamma': float(2*k_quarter*(1+F(1,M))),
                      'new_complete_wider_field_proved': False,
                      'primary_sha256': sha(a.out), 'bytes': len(raw)}), flush=True)


if __name__ == '__main__':
    main()
