#!/usr/bin/env python3
"""Finite posterior substitutions using the complete frequency-resolved source.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
The actual R124 projected field is unchanged.  No ODE, Green integration,
new fixed point, zero high tail, or change of the original parameter axes.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, arb_poly, ctx


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def ex(v):
    if isinstance(v, F):
        return v
    if isinstance(v, int):
        return F(v)
    if isinstance(v, dict):
        if 'upper' in v:
            return ex(v['upper'])
        if 'numerator' in v:
            return F(int(v['numerator']), int(v['denominator']))
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    if isinstance(v[1], int):
        return F(int(v[0])) * F(2) ** v[1]
    return F(int(v[0]), int(v[1]))


def ab(v):
    v = ex(v)
    return arb(v.numerator) / arb(v.denominator)


def bound(v, bits=192):
    if not v.is_finite() or not v.upper() >= 0:
        raise ArithmeticError('A proved nonnegative source expression has no finite positive upper')
    u = v.upper()
    if u == 0:
        return ['0', 0]
    m, e = u.man_exp()
    m, e = int(m), int(e)
    shift = max(0, m.bit_length() - bits)
    if shift:
        m, e = (m + (1 << shift) - 1) >> shift, e + shift
    q = arb(m) * arb(2) ** e
    if not q >= u:
        raise ArithmeticError('Failed outward source rounding')
    return [str(m), e]


def up(v):
    return ex(bound(v))


def exact(v):
    v = F(v)
    return {'numerator': str(v.numerator), 'denominator': str(v.denominator)}


def shift(p, n):
    return arb_poly([arb(0)] * n + p.coeffs())


def positive_poly_sum(p):
    return sum((p[k].upper() for k in range(len(p))), arb(0))


def full_source(Z, caps, V0, S, inverse_degree):
    # All arrays are already exp(sigma*|m|)-weighted strong pair caps.
    # Each signed Fourier half gets exactly one half of its pair mass.
    P, K, DP, DK = ([arb(0)] * 93 for _ in range(4))
    for i in range(46):
        m = 2*i + 2
        p = ab(Z[2*i] + caps[2*i]) / (2*(1+m))
        k = ab(Z[2*i+1] + caps[2*i+1]) / (2*(1+m))
        for pos in (46+i+1, 46-i-1):
            P[pos], K[pos], DP[pos], DK[pos] = p, k, m*p, m*k
    P, K, DP, DK = map(arb_poly, (P, K, DP, DK))
    E, w2 = arb(5)/4, arb(1)/4
    lam = K + E*DP
    c_over_V = 4*ab(V0)*ab(S)**2
    lead = ab(V0)*lam + arb_poly([arb(0)]*46 + [ab(V0)*c_over_V])
    # Q + ell(2c Lambda+c^2), after division by the same V^2.
    ns = E*(DK+P)**2
    nl = E*(K+DP)**2 + w2*(K*K+P*P)
    nl += 2*c_over_V*shift(lam, 46)
    nl += arb_poly([arb(0)]*92 + [c_over_V*c_over_V])
    numerator = arb_poly([max(ns[k].upper(), nl[k].upper()) for k in range(185)])
    Ln = up(positive_poly_sum(lead))
    if not 0 < Ln < F(1, 2):
        raise ArithmeticError('The entire inverse denominator is not paid')
    inv = arb_poly([arb(0)]*(inverse_degree*46) + [arb(1)])
    term = arb_poly([1])
    for power in range(1, inverse_degree+1):
        term = term*lead
        inv += shift(term, (inverse_degree-power)*46)
    polynomial = numerator*inv
    centre = (inverse_degree+2)*46
    Nn = up(positive_poly_sum(numerator))
    tail = up(ab(Nn)*ab(Ln)**(inverse_degree+1)/(1-ab(Ln)))
    if not tail > 0:
        raise ArithmeticError('The full positive inverse tail must not be zeroed')
    pairs = [up(polynomial[centre+i]+polynomial[centre-i]) for i in range(1, centre+1)]
    # Zero is retained through the entire numerator/inverse product.  Only
    # the output projection discards this one coefficient.
    zero = up(polynomial[centre])
    return {'pairs': pairs, 'tail': tail, 'zero': zero, 'Ln': Ln,
            'numerator_mass': Nn, 'mean_normalized_zero_cap': up(c_over_V),
            'finite_nonzero_mass': sum(pairs, F(0)),
            'two_material_numerator_zero_caps': [up(ns[92]), up(nl[92])],
            'source_pair_caps_low46': [pairs[i]+tail for i in range(46)],
            'support_max_mode': 2*centre}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--rounds', type=int, default=16)
    p.add_argument('--inverse-degree', type=int, default=16)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh immutable actual posterior prefix')
    if not 1 <= a.rounds <= 64 or not 8 <= a.inverse_degree <= 64:
        raise ValueError('Explicit bounded posterior work is required')
    ctx.prec = 512
    ctx.threads = 1
    started = time.monotonic()
    ids = read(a.inputs)
    gates = {}

    def gate(name, condition):
        gates[name] = bool(condition)
        if not condition:
            raise ArithmeticError(name)

    data = {}
    for name, rec in ids.items():
        gate('identity_' + name, sha(rec['path']) == rec['sha256'])
        data[name] = read(rec['path'])
    old, centre, ball0, budget, axes, beta, beta_resource, profile, full = [
        data[k] for k in ('old_projected', 'centre', 'ball', 'budget', 'axes',
                         'full_true_beta', 'beta_resource', 'old_profile', 'full_cut')]
    gate('all_old_complete_field_gates', all(old['gates'].values()) and old['all_gates'] and
         old['complete_mean_inverse_and_positive_far_retained'] and old['no_new_fixed_field_solution_claimed'])
    gate('old_centre_and_ball_complete', centre['all_gates'] and ball0['all_gates'] and
         all(centre['gates'].values()) and all(ball0['gates'].values()))
    gate('same_original_centre_budget_axes', all(old['input_identities'][k]['sha256'] == ids[k]['sha256']
         for k in ('centre', 'ball', 'budget')) and old['input_identities']['chart']['sha256'] == ids['axes']['sha256'])
    gate('complete_true_beta_formal_zero', beta['all_gates'] and all(beta['gates'].values()) and
         beta['complete_mean_inverse_far'] and beta_resource['exitcode'] == 0 and
         beta_resource['termination_signal'] is None)
    gate('same_full_unit_complex_beta_and_original_units', ex(beta['domain']['S_product_radius']) == 1 and
         ex(beta['domain']['T_l1_radius']) == F(1, 32) and ex(beta['sigma']) == F(1, 64) and
         'kappa_perp/true_w' in beta['units'])
    gate('profile_same_original_projected_field', profile['all_gates'] and
         profile['same_existing_R124_projected_low_solution'] and
         profile['same_original_axes_and_parameters'] and
         profile['inputs']['complete_true_beta']['sha256'] == ids['full_true_beta']['sha256'] and
         profile['inputs']['original_cut']['sha256'] == ids['old_projected']['sha256'])
    gate('existing_original_full_cut', full['all_gates'] and
         full['original_two_cell_low46_parameter_selfmap_certified'] and
         full['same_existing_R127_field'] and full['complete_mean_inverse_and_infinite_high_retained'] and
         full['inputs']['projected_profile']['sha256'] == ids['old_profile']['sha256'])
    modes = list(range(2, 93, 2))
    gate('all_original_46_modes', modes == centre['modes'] == [r['mode'] for r in old['mode_rows']] ==
         [r['mode'] for r in budget['mode_rows']] == [r['mode'] for r in beta['mode_rows']] ==
         [r['mode'] for r in profile['rows']])
    V0, S = ex(old['Vmax']), ex(old['normalized_total_radius'])
    r0 = ex(old['common_joint_error_radius'])
    gate('original_fixed_norm_and_small_domain', V0 == F(1, 2**40) and S == 8 and
         ex(ball0['centre_norm_upper'])+r0 < S and V0*S < F(1, 64))
    Z = [ex(centre['true_linear_norms'][str(m)][c]) for m in modes for c in ('P', 'K')]
    gate('true_linear_modes42up_exactly_zero', all(x == 0 for x in Z[40:]))
    gate('original_reference_and_linear_cut42up_exactly_zero',
         all(ex(r[k][side]) == 0 for r in centre['cut_rows'][20:]
             for k in ('linear_cut_Q', 'original_cut_Q') for side in (0, 1)) and
         all(ex(r['original_centre']) == 0 for r in axes['rows'][20:]))
    caps = [ex(x) for x in old['rounds'][-1]['caps']]
    gate('all92_initial_positive_caps', len(caps) == 92 and all(0 < x <= r0 for x in caps))
    initial = caps[:]
    G, bd, cutkernel, cuthead, oldlinear = [], [], [], [], []
    for j, m in enumerate(modes):
        br, betar = budget['mode_rows'][j], beta['mode_rows'][j]
        cap = next(x for x in br['densities'] if x['density'] == 'weak_candidate_cap')
        axis = ex(axes['rows'][j]['chosen_axis'])
        gate('same_original_axis_' + str(m), axis > 0 and axis == ex(profile['rows'][j]['original_axis']))
        gate('positive_full_beta_' + str(m), ex(betar['Wsigma1']['chosen_complete']) > 0 and
             ex(betar['Kbar']['chosen_complete']) > 0)
        field_boundary = ex(br['complete_weighted_inner_K_trace_to_field_norm'])*ex(betar['Wsigma1']['chosen_complete'])
        cut_boundary = min(ex(profile['rows'][j]['true_head_including_far']),
                           ex(br['inner_K_trace_to_canonical_cut_absolute'])*ex(betar['Kbar']['chosen_complete'])/axis,
                           ex(betar['original_cut_weighted_beta_bound']))
        cuthead.append(cut_boundary)
        cutkernel.append(ex(cap['canonical_cut_absolute_mode_bound'])/(F(17,16)**2*axis))
        for c in ('P', 'K'):
            G.append(ex(cap[c+'_sup'])/(F(17,16)**2))
            bd.append(field_boundary)
        # The linear centre and the original prescribed outer/Q reference
        # vanish identically in these modes; the old nonzero constant in
        # mode_rows contains G N(L_R), which is included in our full source.
        oldlinear.append(ex(profile['rows'][j]['constant']))
    gate('positive_complete_operators', all(x >= 0 for x in G+bd+cutkernel+cuthead))
    rounds = []
    for n in range(a.rounds):
        src = full_source(Z, caps, V0, S, a.inverse_degree)
        candidate = [bd[i]+G[i]*src['source_pair_caps_low46'][i//2] for i in range(92)]
        new = [min(x, y) for x, y in zip(caps, candidate)]
        gate('same_field_finite_substitution_' + str(n), all(0 < x <= y for x, y in zip(new, caps)))
        gate('full_mean_and_positive_inverse_tail_' + str(n), src['tail'] > 0 and src['zero'] > 0 and
             src['mean_normalized_zero_cap'] > 0 and src['Ln'] < F(1, 2))
        rounds.append({'round': n+1, 'caps': [exact(x) for x in new],
                       'complete_source_low46_pairs': [exact(x) for x in src['source_pair_caps_low46']],
                       'finite_polynomial_pairs_low46': [exact(x) for x in src['pairs'][:46]],
                       'shared_inverse_tail_once': exact(src['tail']),
                       'full_zero_before_output_projection': exact(src['zero']),
                       'inverse_leading_mass': exact(src['Ln']),
                       'common_original_h_radius_retained': exact(r0),
                       'improved_components_this_step': sum(x < y for x, y in zip(new, caps))})
        caps = new
        print(json.dumps({'event': 'complete_low_posterior', 'round': n+1,
                          'improved_components': rounds[-1]['improved_components_this_step'],
                          'mode92_K': float(caps[-1]), 'tail_log2_display': float(ab(src['tail']).log()/arb(2).log())}), flush=True)
        if rounds[-1]['improved_components_this_step'] == 0:
            break
    src = full_source(Z, caps, V0, S, a.inverse_degree)
    result_rows = []
    fullc = full['final_cut']
    components = fullc['component_mode_caps']
    required = ['C_low', 'low_squared', 'low_middle', 'middle_squared', 'middle_high', 'high_squared', 'complete_T']
    gate('all_complete_nonlow_cut_components_preserved', set(components) == set(required))
    for j, m in enumerate(modes):
        oldmap = ex(profile['rows'][j]['projected_map_value'])
        direct = cutkernel[j]*src['source_pair_caps_low46'][j]+cuthead[j] if m >= 42 else None
        value = min(oldmap, direct) if direct is not None else oldmap
        delta = max(ex(fullc['mode_caps'][j]), sum((ex(components[k][j]) for k in required), F(0)))
        gate('preserved_whole_original_cut_bound_' + str(m), value <= oldmap and delta > 0)
        result_rows.append({'mode': m, 'old_P_error_cap': exact(initial[2*j]),
                            'old_K_error_cap': exact(initial[2*j+1]),
                            'new_P_error_cap': exact(caps[2*j]), 'new_K_error_cap': exact(caps[2*j+1]),
                            'complete_source_pair_cap': exact(src['source_pair_caps_low46'][j]),
                            'field_boundary_cap_each_component': exact(bd[2*j]),
                            'true_head_cut': exact(cuthead[j]),
                            'original_source_to_cut': exact(cutkernel[j]),
                            'old_projected_map_bound': exact(oldmap),
                            'direct_full_N_cut_bound_for_zero_linear_reference': exact(direct) if direct is not None else None,
                            'new_projected_map_bound': exact(value),
                            'original_complete_nonlow_correction': exact(delta),
                            'same_original_full_fixed_point_coordinate_bound': exact(value+delta),
                            'old_complete_fixed_point_coordinate_bound': exact(oldmap+delta)})
    out = {'schema': 'same-R124-complete-sparse-source-posterior-v1',
           'author': '/root (GPT-6 Astra Pro, AI-assisted)',
           'source_sha256': sha(__file__), 'input_manifest_sha256': sha(a.inputs), 'inputs': ids,
           'precision_bits': ctx.prec, 'all_gates': all(gates.values()), 'gates': gates,
           'gate_count': len(gates), 'same_existing_R124_projected_field': True,
           'same_original_complex_unit_parameter_domain': True,
           'no_new_ODE_Green_or_nonlinear_solve': True,
           'original_sigma': exact(F(1,64)), 'original_V0': exact(V0), 'original_S': exact(S),
           'common_original_h_radius': exact(r0), 'inverse_polynomial_degree': a.inverse_degree,
           'all92_component_caps': [exact(x) for x in caps], 'rounds': rounds,
           'final_source': {'all_finite_polynomial_pairs': [exact(x) for x in src['pairs']],
                            'polynomial_support_max_mode': src['support_max_mode'],
                            'shared_complete_inverse_tail': exact(src['tail']),
                            'full_zero_before_projection': exact(src['zero']),
                            'mean_only_at_zero': True, 'normalized_mean_zero_cap': exact(src['mean_normalized_zero_cap']),
                            'leading_inverse_mass': exact(src['Ln']),
                            'two_material_numerator_zero_caps': [exact(x) for x in src['two_material_numerator_zero_caps']]},
           'rows': result_rows,
           'same_original_T_shared_projected_map_bound': profile['T_projected_map'],
           'no_shared_T_or_far_mass_resummed_per_mode': True,
           'complete_mean_inverse_and_positive_far_retained': True,
           'old_original_axes_and_R143_K_unchanged': True,
           'R141_nonlow_feedback_bound_unchanged': True,
           'no_full_wider_field_or_outer9_continuation_claimed': True,
           'improved_field_component_count': sum(x < y for x, y in zip(caps, initial)),
           'improved_projected_cut_coordinate_count': sum(ex(r['new_projected_map_bound']) < ex(r['old_projected_map_bound']) for r in result_rows),
           'elapsed_seconds': time.monotonic()-started,
           'peak_rss_kib': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    raw = (json.dumps(out, separators=(',',':'))+'\n').encode()
    if a.out.suffix == '.gz':
        raw = gzip.compress(raw, mtime=0)
    if len(raw) >= 5_000_000 or len(raw) >= 1_000_000 and a.out.suffix != '.gz':
        raise ValueError('Compress or partition the complete posterior record')
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_bytes(raw)
    print(json.dumps({'all_gates': out['all_gates'], 'gates': len(gates),
                      'rounds': len(rounds), 'improved_field_components': out['improved_field_component_count'],
                      'improved_cut_coordinates': out['improved_projected_cut_coordinate_count'],
                      'mode92_old_K': float(initial[-1]), 'mode92_new_K': float(caps[-1]),
                      'mode92_old_map': float(ex(result_rows[-1]['old_projected_map_bound'])),
                      'mode92_new_map': float(ex(result_rows[-1]['new_projected_map_bound'])),
                      'mode92_same_full_fixedpoint_bound': float(ex(result_rows[-1]['same_original_full_fixed_point_coordinate_bound'])),
                      'sha256': sha(a.out), 'bytes': len(raw)}), flush=True)


if __name__ == '__main__':
    main()
