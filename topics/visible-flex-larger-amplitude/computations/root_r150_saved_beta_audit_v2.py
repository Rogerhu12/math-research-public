#!/usr/bin/env python3
"""Independent Fraction audit of R150's saved beta readout arithmetic.

Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This audits complete saved sums, outward rounding, parent intersections,
original units and shared far. It does not repeat source construction,
Green integration, ODE, or certify unsaved intermediate source arithmetic.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == '.gz' else b)


def ex(v):
    if isinstance(v, list):
        return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def up(v, bits=160):
    if v == 0:
        return F(0)
    if v < 0:
        raise ArithmeticError('Only positive source budgets are allowed')
    scale = v.numerator.bit_length()-v.denominator.bit_length()
    if v < F(2)**scale:
        scale -= 1
    unit = F(2)**(scale-bits+1)
    ratio = v/unit
    return ((ratio.numerator+ratio.denominator-1)//ratio.denominator)*unit


def enclosing_raw(v):
    """Inverse enclosure of a documented160-bit upward serialization."""
    if not isinstance(v, list):
        raise ValueError('Actual saved dyadic output required')
    top = ex(v)
    return max(F(0), top-F(2)**int(v[1])), top


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Preserve every independent audit')
    t0 = time.monotonic()
    ids, counts = read(a.inputs), {}

    def check(name, yes):
        if not yes:
            raise ArithmeticError('Independent saved beta audit: '+name)
        counts[name] = counts.get(name, 0)+1

    data = {}
    for k, r in ids.items():
        check('input_identity_'+k, sha(r['path']) == r['sha256'])
        data[k] = read(r['path'])
    b, field, bridge, parent, old, cut = [data[k] for k in
        ('beta', 'field', 'bridge', 'parent_beta', 'old_aux_beta', 'cut_weights')]
    for k in ('beta_resource', 'field_resource', 'bridge_resource'):
        check('formal_success_'+k, data[k]['exitcode'] == 0 and data[k].get('termination_signal') is None)
    for k in ('beta', 'field', 'bridge', 'parent_beta', 'old_aux_beta'):
        check('completed_input_'+k, data[k]['all_gates'] and all(data[k]['gates'].values()))
    # The original operator ledger records a failed self-map proposal.
    # Its seven prerequisite/operator gates are valid; its final self-map
    # gate remains false and is never transferred to this readout audit.
    operator_gates = cut['gates']
    check('original_failed_selfmap_preserved', not cut['all_gates'] and
          operator_gates['at_least_one_complete_selfmap_and_schur'] is False)
    check('all_original_operator_prerequisites_true', all(v for k, v in operator_gates.items()
          if k != 'at_least_one_complete_selfmap_and_schur'))
    modes = list(range(2, 93, 2))
    check('whole46_and213', b['modes'] == modes and [r['mode'] for r in b['mode_rows']] == modes
          and [r['cell'] for r in b['cell_rows']] == list(range(12, 225)))
    check('same_exact_restricted_domain', b['domain'] == field['domain'] == bridge['new_domain']
          and ex(b['domain']['S_product_radius']) == F(3, 8)
          and ex(b['domain']['T_l1_radius']) == F(1, 64)
          and b['domain']['simultaneous_original_coordinates'])
    check('same_original_strips_and_relative_units', ex(b['sigma']) == F(1, 64)
          and b['head_strip'] == field['head_strip'] == parent['head_strip']
          and b['units'] == parent['units'] and 'kappa_perp/true_w' in b['units'])
    check('complete_original_mean_inverse_and_far', b['complete_mean_inverse_far']
          and field['complete_mean_inverse_far'] and parent['complete_mean_inverse_far'])
    check('actual_new_field_and_bridge_provenance', b['input_identities']['field']['sha256'] == ids['field']['sha256']
          and b['input_identities']['domain_bridge']['sha256'] == ids['bridge']['sha256']
          and b['input_identities']['parent_beta']['sha256'] == ids['parent_beta']['sha256'])
    oldrow = min((r for r in old['rows'] if ex(r['radius_T']) >= ex(b['domain']['T_l1_radius'])),
                 key=lambda r: ex(r['radius_T']))
    far = ex(oldrow['true_far_added_once'])
    check('positive_far_never_underflowed', far > 0 and ex(b['complete_true_far_common_at_reference_width2']) == up(far))
    cop = [ex(r['weighted_beta_cut_operator']) for r in cut['source_mode_rows']]
    fop = [ex(r['weighted_beta_field_operator']) for r in cut['source_mode_rows']]
    check('original46_readout_operators', len(cop) == len(fop) == 46 and all(x > 0 for x in cop+fop))
    # Independently validate the stored trace operators using the actual
    # original budget/axes. A positive96-term Taylor sum is a rigorous lower
    # bound for exp(m/64); dividing by it is a sufficient upper readout.
    for i, m in enumerate(modes):
        br, ar = data['budget']['mode_rows'][i], data['axes']['rows'][i]
        axis = ex(ar['chosen_axis'])
        x, term, lower_exp = F(m, 64), F(1), F(1)
        for k in range(1, 97):
            term *= x/k
            lower_exp += term
        sufficient = ex(br['inner_K_trace_to_canonical_cut_absolute'])/(axis*(1+m)*lower_exp)
        check('original_cut_operator_valid_from_actual_budget', cop[i] >= sufficient > 0
              and ex(cut['source_mode_rows'][i]['axis']) == axis)
        check('original_field_operator_exact_from_actual_budget',
              fop[i] == ex(br['complete_weighted_inner_K_trace_to_field_norm']))
    targets = ('Kbar', 'Wsigma1', 'Whead1')
    oldkeys = dict(Kbar='complete_true_beta_cosine_K_coefficient', Wsigma1='complete_true_beta_Wsigma1', Whead1='complete_true_beta_Wtau_b1')
    for i, row in enumerate(b['mode_rows']):
        check('mode_and_group_identity', row['mode'] == modes[i] and row['group'] == ('S' if i < 6 else 'T'))
        for name in targets:
            r = row[name]
            check('all_four_positive_mode_pieces', set(r['nonfar_pieces']) == {'reference', 'DQ', 'quadratic', 'T'}
                  and all(ex(v) > 0 for v in r['nonfar_pieces'].values()))
            nf = up(sum((ex(v) for v in r['nonfar_pieces'].values()), F(0)))
            check('exact_mode_nonfar_upward_sum', nf == ex(r['complete_nonfar']))
            full = up(nf+far)
            check('mode_true_far_added_exactly_once', full == ex(r['new_complete_with_true_far']))
            check('both_original_parent_caps_retained', ex(r['old_complete']) == ex(oldrow['all46_mode_rows'][i][oldkeys[name]])
                  and ex(r['old_parent_domain_complete']) == ex(parent['mode_rows'][i][name]['chosen_complete']))
            chosen = up(min(full, ex(r['old_complete']), ex(r['old_parent_domain_complete'])))
            check('exact_mode_parent_intersection', chosen == ex(r['chosen_complete']) and chosen > 0)
        check('original_cut_units_conversion', ex(row['original_cut_weighted_beta_bound']) == up(cop[i]*ex(row['Wsigma1']['chosen_complete'])))
    commons = {k: F(0) for k in (*targets, 'T_cut', 'field')}
    for cr, fr in zip(b['cell_rows'], field['rows']):
        check('actual_cell_and_all46_low_caps', cr['cell'] == fr['cell'] and cr['low_mode_caps_consumed'] == fr['low_mode_caps']
              and len(cr['complete_DQ_common_mode_caps']) == 46)
        check('complete_cell_shared_positive_remainders', all(ex(cr[k]) > 0 for k in
            ('shared_reference_inverse_tail', 'shared_complete_new_square', 'shared_complete_mean_inverse_T')))
        for name, rr in cr['common_readouts'].items():
            ls, us = zip(*(enclosing_raw(rr[k]) for k in ('reference', 'DQ', 'shared_quadratic_and_T')))
            stored = ex(rr['total_nonfar'])
            check('cell_common_rounding_enclosure', up(sum(ls, F(0))) <= stored <= up(sum(us, F(0))))
            commons[name] += stored
        pair = [enclosing_raw(cr[k]) for k in ('mode92_DQ_low_singleton_source', 'mode92_DQ_nonlow_source')]
        check('mode92_complete_low_plus_nonlow_rounding', up(sum((x[0] for x in pair), F(0)))
              <= ex(cr['complete_DQ_common_mode_caps'][-1]) <= up(sum((x[1] for x in pair), F(0))))
    oldcommon = dict(Kbar=None, Wsigma1='whole46_true_beta_Wsigma1', Whead1='whole46_true_beta_Wtau_b1',
                     T_cut='T_head_complete_in_original_cut_norm', field='whole46_complete_beta_to_original_field_norm')
    for name, nf in commons.items():
        r = b['common_bounds'][name]
        check('all213_common_nonfar_sum', up(nf) == ex(r['new_nonfar']))
        factor = max(cop[6:]) if name == 'T_cut' else max(fop) if name == 'field' else F(1)
        check('shared_true_far_max_weight_once', up(factor*far) == ex(r['true_far_once']))
        full = up(nf+factor*far)
        check('exact_common_complete_sum', full == ex(r['new_complete']))
        if name in targets:
            separate = sum((ex(rm[name]['chosen_complete']) for rm in b['mode_rows']), F(0))
        else:
            op = cop if name == 'T_cut' else fop
            separate = sum((op[i]*ex(b['mode_rows'][i]['Wsigma1']['chosen_complete']) for i in
                            (range(6, 46) if name == 'T_cut' else range(46))), F(0))
        check('exact_separate_readout_for_common_intersection', up(separate) == ex(r['sum_chosen_mode_bounds']))
        values = [full, up(separate), ex(parent['common_bounds'][name]['chosen_complete'])]
        if oldcommon[name]:
            values.append(ex(oldrow[oldcommon[name]]))
        check('exact_common_complete_parent_intersection', up(min(values)) == ex(r['chosen_complete']))
    for name in ('reference', 'DQ', 'quadratic', 'T'):
        bounds = [enclosing_raw(r['mode92_Wsigma_pieces'][name]) for r in b['cell_rows']]
        check('all213_mode92_piece_rounding_enclosure', up(sum((v[0] for v in bounds), F(0)))
              <= ex(b['mode_rows'][-1]['Wsigma1']['nonfar_pieces'][name]) <= up(sum((v[1] for v in bounds), F(0))))
    ans = dict(schema='R150-independent-Fraction-saved-beta-readout-audit-v1',
               author='/root (GPT-6 Astra Pro; AI-assisted)', source_sha256=sha(__file__),
               input_manifest_sha256=sha(a.inputs), inputs=ids, all_gates=True,
               gates={k: True for k in counts}, gate_count=sum(counts.values()), gate_categories=counts,
               exact_domain=b['domain'], complete_all46_mode_and_shared_mass_arithmetic=True,
               all213_saved_cell_rounding_enclosures_checked=True, positive_true_far_paid_once=True,
               source_and_kernel_integrals_not_repeated=True,
               independent_underlying_source_production_not_claimed=True,
               original_operator_ledger_failed_selfmap_explicitly_preserved=True,
               original_trace_operators_independently_checked_against_original_budget=True,
               mode92_original_cut_bound=b['mode_rows'][-1]['original_cut_weighted_beta_bound'],
               common_T_cut=b['common_bounds']['T_cut']['chosen_complete'],
               elapsed_seconds=time.monotonic()-t0, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(ans, separators=(',', ':'))+'\n')
    print(json.dumps(dict(all_gates=True, gates=ans['gate_count'], sha256=sha(a.out),
                         elapsed_seconds=ans['elapsed_seconds'], peak_rss_kib=ans['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
