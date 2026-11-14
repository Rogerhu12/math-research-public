#!/usr/bin/env python3
"""True projected low-cut profile on a subdomain of the existing R127 domain.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
The known CL-LR caps and their independent common mass are lifted to wider
angular strips. Only the complete Taylor remainder is changed; all original
linear/quadratic bounds and the true R123 head/far are retained.
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

from root_hybrid46_cut_consumer import exact as ex, exp_bounds as base_exp_bounds, record, up

def exp_bounds(x):
    # The selected finite strip has m*delta <= 90.5625 < 130.
    # Use the same proved positive geometric-tail formula with128 terms.
    return base_exp_bounds(x, terms=128)

MODES = list(range(2, 93, 2))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def support(coefficients, caps, total):
    remaining, value = total, F(0)
    for i in sorted(range(len(caps)), key=lambda i: coefficients[i], reverse=True):
        take = min(caps[i], remaining)
        value += coefficients[i]*take
        remaining -= take
        if not remaining:
            break
    return up(value)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    began = time.monotonic()
    manifest = read(args.inputs)
    gates = {}

    def gate(name, value):
        if not value:
            raise ArithmeticError(name)
        gates[name] = True

    def checked(name):
        r = manifest[name]
        gate('identity_'+name, sha(r['path']) == r['sha256'])
        return read(r['path'])

    old = checked('original_cut')
    centre = checked('linear_centre')
    head = checked('true_head')
    budget = checked('original_budget')
    chart = checked('original_axes')
    gate('same_original_R119_centre', old['input_identities']['centre']['sha256'] == manifest['linear_centre']['sha256'])
    gate('same_original_R123_head', old['input_identities']['head']['sha256'] == manifest['true_head']['sha256'])
    gate('same_original_budget_and_axes', old['input_identities']['budget']['sha256'] == manifest['original_budget']['sha256']
         and old['input_identities']['chart']['sha256'] == manifest['original_axes']['sha256'])
    gate('original_R124_complete_projected_certificate', old['all_gates'] and all(old['closure_gates'].values())
         and old['complete_mean_inverse_and_positive_far_retained'] and old['radial_sup_before_sum'])
    gate('original_full_R119_and_head_gates', centre['all_gates'] and head['all_gates'])
    gate('all46_original_modes', [r['mode'] for r in old['mode_rows']] == MODES
         == [r['mode'] for r in centre['cut_rows']] == [r['mode'] for r in budget['mode_rows']]
         == [r['mode'] for r in chart['rows']] == head['all46_modes'])
    hb = [r for r in head['rows'] if ex(r['radius_T']) == F(1, 32)]
    gate('exact_original_one_over32_head_row', len(hb) == 1)
    hb = hb[0]
    gate('all46_head_modes_and_positive_far', [r['mode'] for r in hb['all46_mode_rows']] == MODES
         and ex(hb['true_far_added_once']) > 0)
    caps = [ex(x) for x in old['rounds'][-1]['caps']]
    radius = ex(old['common_joint_error_radius'])
    V = ex(old['Vmax'])
    gate('actual_complete92_component_error_caps', len(caps) == 92 and all(0 <= x <= radius for x in caps)
         and radius > 0 and V == F(1, 2**40))
    sigma, tau = F(1, 64), F(18, 125)
    delta_max = tau-sigma
    # CL and LR have exactly46 positive modes. Their92 component caps
    # therefore lift to any finite strip; every wider physical domain is
    # checked directly before applying the complete T Hessian bound.
    deltas = sorted(set([F(i,4)*delta_max for i in range(5)] + [F(k,20)-sigma for k in range(4,21)]))
    choices = []
    for delta in deltas:
        growth = [exp_bounds(m*delta)[1] for m in MODES for _ in range(2)]
        wider_error = support(growth, caps, radius)
        wider_centre = up(sum((ex(centre['true_linear_norms'][str(m)][c])*growth[2*i]
                              for i, m in enumerate(MODES) for c in ('P', 'K')), F(0)))
        whole = up(wider_centre+wider_error)
        gate('complete_physical_wide_T_domain_'+str(delta), 0 < V*whole <= F(1, 128))
        epsilon = up(135*V*whole*wider_error*wider_error)
        decay = [up(1/exp_bounds(m*delta)[0]) for m in MODES]
        choices.append(dict(delta=delta, error=wider_error, centre=wider_centre,
                            whole=whole, physical=V*whole, epsilon=epsilon, decay=decay))
    previous=checked('previous_wide_profile')
    gate('previous_complete_projected_profile',previous['all_gates'] and previous['complete_mean_inverse_and_true_far_retained'])
    original_epsilon = ex(old['complete_shared_higher_order_source'])
    rows = []
    for i, (m, row, hr, br, cr) in enumerate(zip(MODES, old['mode_rows'], hb['all46_mode_rows'], budget['mode_rows'], chart['rows'])):
        kernel = ex(row['source_to_original_cut_axis'])
        linear = up(kernel*ex(row['complete_centre_derivative_source']))
        quadratic = up(kernel*ex(row['quadratic_error_source']))
        tail = up(min([kernel*original_epsilon]+[kernel*c['epsilon']*c['decay'][i] for c in choices]))
        # Recompute the true head in original axes, never infer it by dividing
        # an arbitrary rounded aggregate or by removing the shared far.
        head_value = up(ex(br['inner_K_trace_to_canonical_cut_absolute'])*ex(hr['complete_true_beta_cosine_K_coefficient'])/ex(cr['chosen_axis']))
        value = up(ex(row['constant_fixed_centre_cut'])+linear+quadratic+tail+head_value)
        gate('same_reference_smaller_actual_head_'+str(m), head_value <= ex(row['complete_true_head_cut_individual']))
        gate('strict_actual_full_mode_improvement_'+str(m), value < ex(row['complete_cut_value_individual']))
        rows.append(dict(mode=m, original_axis=cr['chosen_axis'],
            constant=record(ex(row['constant_fixed_centre_cut'])), complete_linear=record(linear),
            complete_quadratic=record(quadratic), complete_T_remainder=record(tail),
            true_head_including_far=record(head_value), projected_map_value=record(value),
            proposed_T_coordinate_radius=record(2*value) if i >= 6 else None,
            old_projected_map_value=row['complete_cut_value_individual']))
    gate('all_new_modes_no_worse_than_R129',all(ex(row['projected_map_value'])<=ex(prior['projected_map_value']) for row,prior in zip(rows,previous['rows'])))
    gate('mode92_strictly_improves_R129',ex(rows[-1]['projected_map_value'])<ex(previous['rows'][-1]['projected_map_value']))
    Ttail = min([ex(old['T_common_higher_order_correction'])]+[
        max(ex(old['mode_rows'][i]['source_to_original_cut_axis'])*c['decay'][i] for i in range(6, 46))*c['epsilon'] for c in choices])
    Tvalue = up(ex(old['T_constant_fixed_centre'])+ex(old['T_complete_linear_correction'])
                +ex(old['T_quadratic_correction'])+Ttail+ex(hb['T_head_complete_in_original_cut_norm']))
    Svalue = max(ex(r['projected_map_value']) for r in rows[:6])
    working_S, working_T = F(1, 2), F(1, 36)
    gate('strict_S_selfmap_in_half', Svalue < working_S)
    gate('strict_T_shared_selfmap_in_one_over36', Tvalue < working_T)
    gate('each_T_profile_selfmap', all(ex(r['projected_map_value']) < ex(r['proposed_T_coordinate_radius']) for r in rows[6:]))
    gate('profile_within_original_R127_parameter_domain', working_S < 1 and working_T < F(1, 32))
    gate('R124_contraction_restricts_in_unchanged_original_norm', max(working_S, working_T) < ex(old['working_radius'])
         and ex(old['Cauchy_Lipschitz_bound']) < F(1, 20))
    result = dict(schema='extended-finite-low-spectrum-cut-profile-v1', author='/root (GPT-6 Astra Pro, AI-assisted)',
        source_sha256=sha(__file__), helper_sha256=sha(Path(__file__).with_name('root_hybrid46_cut_consumer.py')),
        input_manifest_sha256=sha(args.inputs), inputs=manifest, all_gates=all(gates.values()), gates=gates,
        same_existing_R124_projected_low_solution=True, all_original_modes_and_axes_retained=True,
        common_radius_retained=record(radius), original_Vmax=record(V), original_sigma=['1','64'], wide_tau=['1','1'], finite_exactly46_modes_all_lifts_valid=True,
        wider_remainder_choices=[dict(delta=[str(c['delta'].numerator), str(c['delta'].denominator)],
            true_error_norm_upper=record(c['error']), true_linear_centre_norm_upper=record(c['centre']),
            whole_normalized_domain=record(c['whole']), whole_physical_domain=record(c['physical']),
            complete_shared_T_remainder=record(c['epsilon'])) for c in choices],
        rows=rows, S_projected_map=record(Svalue), T_projected_map=record(Tvalue),
        T_complete_shared_remainder_paid_once=record(up(Ttail)), T_true_head_paid_once=hb['T_head_complete_in_original_cut_norm'],
        domain=dict(S_linf_radius=record(working_S), T_l1_radius=record(working_T),
            T_additional_coordinate_constraints='abs(z_m) <= proposed_T_coordinate_radius; simultaneous with the T l1 radius',
            no_original_axis_is_changed=True, within_original_R127_domain=True),
        original_norm_Lipschitz_bound=old['Cauchy_Lipschitz_bound'],
        unique_projected_low_cut_fixed_point_in_profile_domain=True,
        full_frequency_cut_closed=False, closed_surface_claimed=False,
        complete_mean_inverse_and_true_far_retained=True, no_new_ODE_or_source_integral=True,
        elapsed_seconds=time.monotonic()-began, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if args.out.exists():
        raise FileExistsError(args.out)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode()
    if str(args.out).endswith('.gz'):
        raw=gzip.compress(raw,compresslevel=9,mtime=0)
    if len(raw)>=5_000_000 or len(raw)>1_000_000 and not str(args.out).endswith('.gz'):
        raise ArithmeticError('Repository file-size rule')
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_bytes(raw)
    print(json.dumps(dict(all_gates=result['all_gates'], gate_count=len(gates),
        S_projected_map=float(Svalue), T_projected_map=float(Tvalue),
        widest_error=float(choices[-1]['error']), widest_centre=float(choices[-1]['centre']),
        mode92_value=float(ex(rows[-1]['projected_map_value'])),
        mode92_profile_radius=float(ex(rows[-1]['proposed_T_coordinate_radius'])),
        projected_only=True, source_sha256=sha(__file__), result_sha256=sha(args.out),
        elapsed_seconds=result['elapsed_seconds'], peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__ == '__main__':
    main()
