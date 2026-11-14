#!/usr/bin/env python3
"""Consume R121 on the original R63/R82/R83/R100 complete true cut.

Replace only the cell12 auxiliary SOURCE by the smaller of two valid
same-object bounds.  Keep all212 other source cells explicitly, the
unchanged complete full-head-minus-auxiliary comparison, and the positive
true far term.  The R121 field caps already include the influence of
other cells and auxiliary far; this is separate from direct cut-source
and true-far contributions.  Both original Fourier halves are retained.

The output is an improved rigorous inner-head budget and a replay of the
old complete-cut sufficient tests with that budget.  It never declares
the outer source or full cut closed merely because the head improves.
All mathematical arithmetic is Fraction, with directed dyadic output.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

import root_hybrid46_cut_consumer as original

sys.set_int_max_str_digits(0)
PINNED = {
    'bootstrap': ('2026-11-13-inner-aux-cell12-spectral-bootstrap-r1.json.gz',
        '490bbdaa71cbd14b4dab9fbf6ac820d72b895b7fc5664b8a3a2ff454bb63a1c6'),
    'outside': ('2026-11-13-inner-aux-cell12-outside-floor-r1.json.gz',
        '28e68f029dc61e22192407ee8b8c49c549ee37ab957b31c76d082b1f1bbbf02d'),
    'r82': ('2026-11-12-root-r82-complete-low-cut-r1.json',
        '271c7fc52805ebde342a11c1dfceeea434f9fab5c0922384903ca092830e34c9'),
    'r83': ('2026-11-12-root-r83-complete-cut-difference-r1.json',
        '4ec6d30adb9eb639e658bcaa86873cfed0675ab975d3a8f92778888339f966b2'),
    'head': ('2026-11-13-root-r100-source-reweight-r1.json',
        '617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'),
    'r100': ('2026-11-13-root-r100-hybrid46-exact-ledger.json',
        '7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9'),
    'old_cut': ('2026-11-13-root-hybrid46-cut-r1.json',
        'cf33eba4dcd1ad4e8fea3e667664b9c356db790851ca8e49d9889a62e408d638'),
    'far': ('2026-11-12-closure-r63-far-boundary-completion-r1.json',
        '6ee19d3288cd6d8662eecbc7d72e83d59245383798c6a066d8c9160c432ea4dd'),
}
MODES = list(range(2, 93, 2))
CELLS = list(range(12, 225))
up, rec, sum_up = original.up, original.record, original.sum_up


def ex(obj):
    if isinstance(obj, dict) and 'upper_dyadic' in obj:
        return original.exact(obj['upper_dyadic'])
    return original.exact(obj)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--notes', type=Path, default=Path('notes'))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Keep completed outputs immutable')
    started = time.monotonic()
    ids, data, gates = {}, {}, {}

    def check(name, truth):
        gates[name] = bool(truth)
        if not truth:
            raise ArithmeticError('Unpaid complete-cut consumption gate: ' + name)

    def load(path, wanted):
        raw = path.read_bytes()
        got = hashlib.sha256(raw).hexdigest()
        if got != wanted:
            raise ValueError('Pinned original changed: ' + str(path))
        ids[str(path)] = dict(sha256=got, bytes=len(raw))
        return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw,
                          parse_float=str)

    for key, (name, wanted) in PINNED.items():
        data[key] = load(args.notes / name, wanted)
    boot, outside, r82, r83, head, r100, old_cut, far_doc = (
        data[key] for key in ('bootstrap', 'outside', 'r82', 'r83',
                             'head', 'r100', 'old_cut', 'far'))
    helper_path = Path(original.__file__)
    check('original_directed_consumer_source',
          digest(helper_path) == old_cut['source_sha256'])
    for key in ('bootstrap', 'outside', 'r82', 'r83', 'head', 'r100', 'far'):
        check('completed_prerequisite_' + key,
              data[key]['all_gates'] is True and all(data[key]['gates'].values()))
    check('old_cut_other_arithmetic_gates_paid',
          all(value for name, value in old_cut['gates'].items()
              if name != 'at_least_one_complete_selfmap_and_schur'))
    check('R121_same_original_R74_full_domain',
          boot['target_cell'] == 12 and boot['canonical_reference_strip'] == 2
          and boot['all46_modes_retained'] == MODES
          and len(boot['parameter_axes']) == 20)
    check('R121_other_cells_and_true_far_retained',
          boot['input_identities']['notes/' + PINNED['outside'][0]]['sha256'] == PINNED['outside'][1]
          and ex(boot['fixed_other212_plus_true_far_over_reference']) > 0
          and ex(outside['direct_true_far_contribution']) > 0)
    check('old_R100_same_head_and_parameter_inputs',
          old_cut['input_identities']['head']['sha256'] == PINNED['head'][1]
          and old_cut['input_identities']['r100']['sha256'] == PINNED['r100'][1])
    for key in ('r83', 'r100', 'far'):
        check('reweighted_head_same_' + key,
              head['input_identities'][key]['sha256'] == PINNED[key][1])
    for key in ('r82', 'far'):
        check('R83_same_' + key,
              r83['input_hashes']['notes/' + PINNED[key][0]] == PINNED[key][1])
    for field in ('parameter_axes',):
        check('same_complete_R74_' + field, boot[field] == r82[field])
    for rows, name in ((boot['linear_and_kernel_rows'], 'bootstrap_columns'),
                       (boot['final_modal_rows'], 'bootstrap_sources'),
                       (r82['selected_mode_rows'], 'R82'),
                       (r83['selected_mode_rows'], 'R83'),
                       (head['mode_rows'], 'R100'),
                       (old_cut['source_mode_rows'], 'original_cut')):
        check('all46_' + name, [row['mode'] for row in rows] == MODES)

    sigma = F(1, 64)
    source_factor = ex(r82['source_factor'])
    check('original_uniform_R74_source_enlargement', source_factor == F(4225, 4096))
    ci = ex(far_doc['point_cut_inner_mu12_K_conversion'])
    check('same_true_inner_mu12_point_conversion',
          ci > 0 and ci == ex(head['point_cut_inner_mu12_K_conversion']))
    far = ex(head['true_far_added_once_per_whole_mass'])
    check('same_complete_true_far_positive',
          far > 0 and far == ex(r83['whole46_complete_true_far_upper']))
    rem = ex(boot['final_common_complete_mean_inverse_source_remainder'])
    check('full_mean_and_inverse_source_remainder_positive', rem > 0)
    input_source_pins = r82['common_original_source_inputs']
    for name in ('2026-11-12-closure-real-linear-q003-low46-recovered.json.gz',
                 '2026-11-12-closure-ordered-green-low46-v2.json.gz',
                 '2026-11-12-closure-newg-strong-m20-real-reference.json',
                 '2026-11-12-closure-newg-strong-m20-real-box.json'):
        spelling = 'notes/' + name
        check('same_true_auxiliary_object_' + name,
              boot['input_identities'][spelling]['sha256'] == input_source_pins[spelling])

    auxiliary, auxiliary_rows, other_rows = [], [], []
    shared12_base, shared12_rem_gain = [], []
    source_functionals = {}
    for i, m in enumerate(MODES):
        old_mode = r82['selected_mode_rows'][i]
        path_spelling, wanted = old_mode['source_primary'], old_mode['source_primary_sha256']
        check('R83_same_source_primary_' + str(m),
              r83['selected_mode_rows'][i]['source_primary'] == path_spelling
              and r83['selected_mode_rows'][i]['source_primary_sha256'] == wanted
              and r82['input_hashes'][path_spelling] == wanted)
        doc = load(args.notes / Path(path_spelling).name, wanted)
        check('original_source_gates_' + str(m), doc['all_gates'] is True
              and all(doc['checks'].values()))
        check('source_same_all46_aux_and_full213_cells_' + str(m),
              doc['auxiliary_input_modes'] == MODES and doc['cells'] == CELLS)
        check('source_same_complete_g_and_strip_' + str(m),
              doc['input_hashes'] == input_source_pins
              and doc['outer_strip'] == '1/64'
              and ex(doc['point_cut_K_conversion']) == ci)
        row = next(row for row in doc['rows'] if row['mode'] == m)
        check('all213_direct_source_rows_' + str(m),
              [s['cell'] for s in row['source_rows']] == CELLS)
        # Keep the other212 source cells as a positive sum, not a
        # difference of independently rounded whole-source bounds.
        others = []
        for cell in row['source_rows'][1:]:
            term = up(source_factor * ex(cell['auxiliary_cut_Xi_contribution_upper']))
            check('positive_other_cell_' + str(m) + '_' + str(cell['cell']), term > 0)
            others.append(term)
            other_rows.append(dict(mode=m,cell=cell['cell'],
                original_source_Xi=cell['auxiliary_cut_Xi_contribution_upper'],
                full_R74_source_Xi_upper=rec(term)))
        other_xi = sum_up(others)
        old12 = up(source_factor * ex(row['source_rows'][0]['auxiliary_cut_Xi_contribution_upper']))
        phi = ex(boot['linear_and_kernel_rows'][i]['true_normalized_phi_Q_sup'])
        # The R121 source already has e^(2m).  At this same source and
        # target cell, the Wronskian mu12/mu12 factor equals exactly1.
        strip_loss = F(3, 8) ** (2*m)  # e^(-2m) < (3/8)^(2m)
        source_gain = up(phi * strip_loss)
        quad = ex(boot['final_modal_rows'][i]['quadratic_source_canonical_L1_pair'])
        q12 = up(source_gain * quad)
        r12 = up(source_gain * rem)
        new12 = up(q12 + r12)
        chosen12 = min(old12, new12)
        angular = original.exp_bounds(m*sigma)[1]
        weighted_gain = up(ci*(1+m)*angular)
        reconstructed = up(weighted_gain * sum_up([other_xi, chosen12]))
        old_auxiliary = ex(head['mode_rows'][i]['both_strips']['Wsigma1']['old_auxiliary'])
        av = min(old_auxiliary, reconstructed)
        auxiliary.append(av)
        check('same_object_auxiliary_bound_never_increases_' + str(m), av <= old_auxiliary)
        # A separate simultaneous decomposition allows one shared
        # complete remainder to be charged through a maximum operator.
        if new12 < old12:
            base12, rem_gain, selected = q12, source_gain, 'R121_quadratic_plus_complete_common_remainder'
        else:
            base12, rem_gain, selected = old12, F(0), 'original_complete_R74_cell12_bound'
        shared12_base.append(up(weighted_gain * sum_up([other_xi, base12])))
        shared12_rem_gain.append(up(weighted_gain * rem_gain))
        source_functionals[m] = dict(weighted_gain=weighted_gain,source_gain=source_gain)
        auxiliary_rows.append(dict(mode=m,source_primary=path_spelling,source_primary_sha256=wanted,
            original_R74_cell12_Xi=rec(old12),all_other212_R74_source_Xi=rec(other_xi),
            true_normalized_cell12_phi_Q_sup=rec(phi),canonical_source_strip=2,
            canonical_to_cut_coefficient_strip_loss=rec(strip_loss),
            R121_cell12_quadratic_Xi=rec(q12),R121_cell12_common_complete_remainder_Xi=rec(r12),
            R121_cell12_complete_Xi=rec(new12),selected_cell12_Xi=rec(chosen12),
            selected_cell12_bound=selected,
            old_complete_auxiliary_source_Wsigma1=rec(old_auxiliary),
            new_complete_auxiliary_source_Wsigma1=rec(av),
            new_auxiliary_source_ratio_to_old=rec(av/old_auxiliary),
            shared_remainder_decomposition_base_Wsigma1=rec(shared12_base[-1]),
            common_remainder_to_Wsigma1_operator=rec(shared12_rem_gain[-1])))

    kt, eta, tmax = (ex(r100['constants'][key]) for key in ('KT', 'eta', 'tmax'))
    check('unchanged_R100_transverse_constants', kt == F(273259958272,395007) and eta == 4096)
    cut_head = [ex(r['weighted_beta_cut_operator']) for r in old_cut['source_mode_rows']]
    field_head = [ex(r['weighted_beta_field_operator']) for r in old_cut['source_mode_rows']]
    cut_D = [ex(r['complete_source_cut_derivative']) for r in old_cut['source_mode_rows']]
    source_value = [ex(r['complete_outer_source_cut_value']) for r in old_cut['source_mode_rows']]
    linear = [ex(r['linear_cut_absolute']) for r in old_cut['source_mode_rows']]
    gamma = ex(old_cut['complete_field_contraction'])
    check('unchanged_paid_absolute_nine_field_contraction', 0 < gamma < 1)

    def beta_bounds(radius, use_new):
        q = 1+(kt+eta)*radius/256
        factors = dict(main=q,corr=q,quadratic=q*q,
                       remainder=q*(1+q*tmax+(q*tmax)**2/3))
        nonfar, bridge, differences = [], [], []
        for i, row in enumerate(head['mode_rows']):
            m = row['mode']
            check('all_four_complete_difference_pieces_' + str(m),
                  set(row['old_complete_difference_Xi_pieces']) == set(factors))
            xi = sum_up(up(factors[k]*ex(v))
                        for k,v in row['old_complete_difference_Xi_pieces'].items())
            delta = up(ci*(1+m)*original.exp_bounds(m*sigma)[1]*xi)
            old = row['both_strips']['Wsigma1']
            old_delta, old_chosen = ex(old['old_complete_difference']), ex(old['old_chosen'])
            av = auxiliary[i] if use_new else ex(old['old_auxiliary'])
            difference = up(delta+old_delta)
            bound = min(up(av+delta),up(old_chosen+difference+far))
            nonfar.append(bound)
            bridge.append(difference)
            differences.append(delta)
        return nonfar, bridge, differences

    def whole_field(values, far_mass):
        return up(sum_up(up(a*b) for a,b in zip(field_head,values))+max(field_head)*far_mass)

    def cut_s(values,far_mass,field_derivative):
        return [up(cut_D[i]*field_derivative+cut_head[i]*(values[i]+far_mass)) for i in range(6)]

    def cut_t(values,far_mass,field_derivative):
        return up(sum_up(cut_D[6:])*field_derivative+
                  sum_up(up(cut_head[i]*values[i]) for i in range(6,46))+
                  max(cut_head[6:])*far_mass)

    scenarios = []
    for old_scenario in old_cut['scenarios']:
        rs, rt = ex(old_scenario['radius_S']), ex(old_scenario['radius_T'])
        outer_t = ex(old_scenario['Cauchy_outer_T'])
        check('same_original_Cauchy_domain_' + str(rt), rs == F(3,4) and outer_t == 2*rt <= 1)
        old_nf, _, _ = beta_bounds(rt,False)
        original_T = sum_up(up(cut_head[i]*old_nf[i]) for i in range(6,46))
        check('exact_original_T_head_reproduced_' + str(rt),
              original_T == ex(old_scenario['T_nonfar_head_l1']))
        nf, _, differences = beta_bounds(rt,True)
        _, transverse, _ = beta_bounds(outer_t,True)
        new_T = sum_up(up(cut_head[i]*nf[i]) for i in range(6,46))
        check('new_complete_T_head_improves_' + str(rt), new_T < original_T)
        shared_T = up(sum_up(up(cut_head[i]*(shared12_base[i]+differences[i]))
                                  for i in range(6,46))+
                      max(cut_head[i]*shared12_rem_gain[i] for i in range(6,46))*rem)
        ds = [up(v/(1-rs)) for v in nf]
        dt = [up(v/(outer_t-rt)) for v in transverse]
        far_s, far_t = far/(1-rs),2*far/(outer_t-rt)
        hs, ht = whole_field(ds,far_s),whole_field(dt,far_t)
        fs, ft = up(hs/(1-gamma)),up(ht/(1-gamma))
        ss, st = cut_s(ds,far_s,fs),cut_s(dt,far_t,ft)
        a,b,c,d = max(ss),max(st),cut_t(ds,far_s,fs),cut_t(dt,far_t,ft)
        values_s = [up(linear[i]+source_value[i]+cut_head[i]*(nf[i]+far)) for i in range(6)]
        chosen_head_T = min(new_T,shared_T)
        Tfar = up(max(cut_head[6:])*far)
        value_t = up(sum_up(linear[6:])+sum_up(source_value[6:])+chosen_head_T+Tfar)
        contraction = original.schur(a,b,c,d)
        mode_values = [dict(mode=m,
            complete_head_nonfar_Wsigma1=rec(nf[i]),
            normalized_complete_head_nonfar=rec(up(cut_head[i]*nf[i])),
            complete_full_minus_auxiliary_Wsigma1=rec(differences[i]))
                       for i,m in enumerate(MODES)]
        scenarios.append(dict(radius_S=rec(rs),radius_T=rec(rt),Cauchy_outer_T=rec(outer_t),
            original_T_nonfar_head_l1=rec(original_T),
            new_T_nonfar_head_from_modal_bounds=rec(new_T),
            new_T_nonfar_head_shared_complete_remainder=rec(shared_T),
            new_T_nonfar_head_l1=rec(chosen_head_T),
            new_to_old_T_head_ratio=rec(chosen_head_T/original_T),
            T_linear_l1=rec(sum_up(linear[6:])),
            T_unchanged_complete_outer_source_l1=rec(sum_up(source_value[6:])),
            T_true_far_charged_once=rec(Tfar),
            all46_complete_head_rows=mode_values,
            complete_value_S_rows=[dict(mode=MODES[i],upper=rec(v)) for i,v in enumerate(values_s)],
            complete_value_S_max=rec(max(values_s)),complete_value_T_l1=rec(value_t),
            complete_beta_field_derivatives=dict(S=rec(hs),T=rec(ht)),
            complete_low_field_derivatives=dict(S=rec(fs),T=rec(ft)),
            cut_derivative_positive_matrix=[[rec(a),rec(b)],[rec(c),rec(d)]],
            schur=contraction,selfmap_S=max(values_s)<rs,selfmap_T=value_t<rt,
            all46_projected_cut_closed=max(values_s)<rs and value_t<rt and contraction['passed']))
    check('all_original_scenarios_preserved', len(scenarios) == len(old_cut['scenarios']))
    check('all9752_other_mode_cell_terms_kept_positive', len(other_rows) == 46*212)
    check('all46_auxiliary_and_true_difference_modes_kept',len(auxiliary_rows)==46)
    check('complete_true_far_not_deleted',far>0)
    result = dict(schema='visible-flex-larger-R121-auxiliary-source-cut-consumption-v1',
        status='Exact same-object inner-head improvement; complete outer cut tests remain independently reported',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=digest(__file__),original_consumer_helper_sha256=digest(helper_path),
        input_identities=ids,all_gates=all(gates.values()),gates=gates,
        auxiliary_parameter_domain=boot['parameter_domain'],
        complete_head_parameter_domain=head['parameter_domain'],
        complete_parameter_norm=head['parameter_norm'],all46_modes=MODES,
        auxiliary_source_identity='N(C_S) for the same R100 C_S, uniformly bounded on the containing full R74 family by R121',
        source_cut_formula='Xi12(b) source contribution = sum_n(mu_n/mu12) integral Phi_Q,m F_Xi,n,m dr; cell12 ratio=1; physical K conversion is the original independently certified ci',
        true_cut_K_conversion=rec(ci),outer_cut_strip='1/64',
        bootstrap_reference_strip=2,source_factor_for_unchanged_other_cells=rec(source_factor),
        original_R121_other_cells_and_far_field_budget=boot['fixed_other212_plus_true_far_over_reference'],
        complete_canonical_mean_inverse_remainder=rec(rem),
        complete_true_far_mass=rec(far),
        auxiliary_mode_rows=auxiliary_rows,
        all_other212_by46_source_rows=other_rows,
        scenarios=scenarios,
        at_least_one_full_cut_sufficient_test_passed=any(s['all46_projected_cut_closed'] for s in scenarios),
        complete_mean_inverse_and_positive_far_retained=True,
        full_cut_or_closed_surface_claimed=False,
        interpretation='A smaller auxiliary source budget only changes the same inner-head terms. Any failed sufficient outer source/selfmap/Schur gate remains failed. No failed bound is a nonexistence claim.',
        no_new_ODE=True,no_new_Arb=True,no_new_source_integral=True,no_Node=True,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode()
    payload=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
    if len(payload)>=5_000_000 or (len(raw)>1_000_000 and args.out.suffix!='.gz'):
        raise ValueError('Repository per-file/compression limits exceeded')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('xb') as stream:stream.write(payload)
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out),bytes=len(payload),
        all_gates=result['all_gates'],gates=len(gates),seconds=result['elapsed_seconds'],
        peak_rss_kib=result['peak_rss_kib'],scenarios=[dict(
            radius_T=s['radius_T']['display_upward'],old_head=s['original_T_nonfar_head_l1']['display_upward'],
            new_head=s['new_T_nonfar_head_l1']['display_upward'],
            source_T=s['T_unchanged_complete_outer_source_l1']['display_upward'],
            full_cut=s['all46_projected_cut_closed']) for s in scenarios])),flush=True)


if __name__=='__main__':
    main()
