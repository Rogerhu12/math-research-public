#!/usr/bin/env python3
"""Consume the actual complete R100 head and low46 source in the mixed cut norm.

All arithmetic is Fraction with directed dyadic output.  The source proof is
the absolute low46 equation: Y=LR+G N(Y)+Bh beta(a).  Selected candidate
parameters cancel exactly.  The T output is a weighted l1 SUM, not a maximum.
The complete true far term is charged through the appropriate operator norm
once per whole output.  No original field, source, norm, or mode is modified.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import time

PINNED = {
    'geometry': 'e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03',
    'budget': '86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45',
    'r94': '5eb45673a9080ae251e77c3203cfc2142ba31850fc244c7e2c8500df774249bc',
    'r100': '7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9',
    'geometry_source': 'c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829',
    'head_source': '58e0d7750faa1e9d58458f238c93f7c6cab3803cef3b776c2f01b494287bb5c1',
    'spectral_source': 'eac90d6f7c816a67590c2c07d031e24d27af0adfd21e1b5ef5411891943b903e',
}
def p2(e):
    return F(1 << e) if e >= 0 else F(1, 1 << (-e))


def exact(v):
    if isinstance(v, bool) or isinstance(v, float):
        raise TypeError('No boolean or display float is a proof bound')
    if isinstance(v, (int, str)):
        return F(v)
    if isinstance(v, (list, tuple)) and len(v) == 2:
        return F(int(v[0])) * p2(int(v[1]))
    if not isinstance(v, dict):
        raise TypeError('Unrecognized proof record')
    if 'upper' in v:
        return exact(v['upper'])
    if 'numerator' in v and 'denominator' in v:
        return F(int(v['numerator']), int(v['denominator']))
    if 'mantissa' in v and 'binary_exponent' in v:
        return F(int(v['mantissa'])) * p2(int(v['binary_exponent']))
    raise ValueError('Unrecognized exact record')


def up(x, bits=192):
    x = F(x)
    if x < 0:
        raise ValueError('Positive proof arithmetic only')
    if not x:
        return F(0)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < p2(e):
        e -= 1
    quantum = p2(e-bits+1)
    y = x/quantum
    return ((y.numerator+y.denominator-1)//y.denominator)*quantum


def record(x):
    x = up(x)
    with localcontext() as ctx:
        ctx.prec = 27
        ctx.rounding = ROUND_CEILING
        display = str(Decimal(x.numerator)/Decimal(x.denominator))
    return {'upper': {'mantissa': str(x.numerator),
                      'binary_exponent': -(x.denominator.bit_length()-1)},
            'display_upward': display}


def sum_up(values):
    out = F(0)
    for x in values:
        out = up(out+x)
    return out


def exp_bounds(x, terms=64):
    x = F(x)
    if not 0 <= x < terms+2:
        raise ValueError('Positive exponential geometric tail not paid')
    term = total = F(1)
    for k in range(1, terms+1):
        term *= x/k
        total += term
    return total, up(total+term*x/(terms+1)/(1-x/(terms+2)))


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def load_input(path, wanted, source=False):
    raw = path.read_bytes()
    if sha256(raw) != wanted:
        raise ValueError('Pinned complete input changed: '+str(path))
    if source:
        value = raw.decode('utf8')
    else:
        value = json.loads(raw, parse_float=str)
        if value.get('all_gates') is not True:
            raise ValueError('Actual prerequisite has unpaid gates: '+str(path))
    return value, {'path': str(path), 'bytes': len(raw), 'sha256': wanted}


def schur(a, b, c, d):
    """Positive 2x2 contraction with an explicitly constructed distance weight."""
    passed = a < 1 and d < 1 and b*c < (1-a)*(1-d)
    if not passed:
        return {'passed': False,
                'diagonal_gates': [a < 1, d < 1],
                'positive_cross_product': record(b*c),
                'no_nonexistence_claim': True}
    lo = c/(1-d)
    v = (lo+(1-a)/b)/2 if b else lo+1
    if not v > 0:
        raise ArithmeticError('Positive distance weight missing')
    q = max(a+b*v, d+c/v)
    if not q < 1:
        raise ArithmeticError('Constructed Schur weight does not contract')
    return {'passed': True, 'distance_weight_T_over_S': record(v),
            'contraction_upper': record(q)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for k in PINNED:
        ap.add_argument('--'+k.replace('_', '-'), type=Path, required=True)
    for k in ('head', 'spectral'):
        ap.add_argument('--'+k, type=Path, required=True)
        ap.add_argument('--'+k+'-sha', required=True)
    ap.add_argument('--radii-t', default='1/64,1/32,3/64,1/16,3/32,1/8,3/16,1/4,3/8,1/2')
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--rss-kib', type=int, default=98304)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Keep every complete output immutable')
    began = time.monotonic()
    data, identities = {}, {}
    expected = dict(PINNED, head=args.head_sha, spectral=args.spectral_sha)
    for k, wanted in expected.items():
        if len(wanted) != 64 or any(c not in '0123456789abcdef' for c in wanted):
            raise ValueError('An exact SHA256 is required')
        data[k], identities[k] = load_input(getattr(args, k), wanted, k.endswith('_source'))
    geom, budget, head, spectrum, theorem = [data[k] for k in ('geometry', 'budget', 'head', 'spectral', 'r100')]
    if (head.get('schema') != 'visible-flex-larger-R100-complete-source-reweight-v1'
            or head['source_sha256'] != expected['head_source']
            or spectrum['source_sha256'] != expected['spectral_source']
            or spectrum['complete_R100_primary_sha256'] != expected['head']):
        raise ValueError('Only the fresh complete R100 domain and source are accepted')
    if (budget['geometry_sha256'] != expected['geometry']
            or budget['geometry_entrypoint_sha256'] != expected['geometry_source']
            or geom['config']['entrypoint_sha256'] != expected['geometry_source']):
        raise ValueError('Same complete true Green geometry required')
    if '18m/125' not in spectrum['centre_norm'] or geom['config']['source_tau'] != '1/64':
        raise ValueError('Keep both actual angular widths')
    if geom['config']['physical_source'] != 'N enters K_x, hence Y_2 source is sqrt(r*w^3)*N, no extra r_x':
        raise ValueError('The physical source units changed')
    modes = list(range(2, 93, 2))
    for seq in (budget['mode_rows'], head['mode_rows'], theorem['rows'], spectrum['low_complete_sources']):
        if [int(r['mode']) for r in seq] != modes:
            raise ValueError('Retain all46 low source/output rows')
    if (theorem['domain']['product_modes'] != modes[:6]
            or theorem['domain']['weighted_l1_modes'] != modes[6:]):
        raise ValueError('Do not change the six/forty grouping')
    geometry_source = data['geometry_source']
    for marker in ('A = E*s+(E+w*w/9)*ell', 'cap = ((Q+mean)/(1-lead)).upper()',
                   'wc = weak_density(g, V, sigma, arb(0), V)'):
        if marker not in geometry_source:
            raise ValueError('Original complete weak density definition changed')
    sigma, tau = F(1, 64), F(18, 125)
    candidate_scale, field_radius, radius_s = F(17, 16), F(9), F(3, 4)
    gamma_row = next(r for r in budget['densities'] if r['density'] == 'weak_local_rho_16')
    gamma = 2*exact(gamma_row['all46_sum_of_separate_component_suprema'])
    if gamma != exact(data['r94']['same_low_contraction']) or not gamma < 1:
        raise ValueError('The paid complete absolute-nine contraction changed')
    if not field_radius <= candidate_scale+16:
        raise ArithmeticError('Complete derivative density domain unpaid')
    ci = exact(head['point_cut_inner_mu12_K_conversion'])
    far = exact(head['true_far_added_once_per_whole_mass'])
    kt, eta = exact(theorem['constants']['KT']), exact(theorem['constants']['eta'])
    tmax = exact(theorem['constants']['tmax'])
    if not far > 0 or kt != F(273259958272, 395007) or eta != 4096:
        raise ValueError('Do not omit far or alter the complete parameter budget')
    axes, linear, cut_head, field_head, cut_D, source_value = [], [], [], [], [], []
    input_rows = []
    for i, m in enumerate(modes):
        br, ar = budget['mode_rows'][i], theorem['rows'][i]
        axis = exact(ar['chosen_axis'])
        angular_low, angular_high = exp_bounds(m*sigma)
        strip_low, strip_high = exp_bounds(m*(tau-sigma))
        hcut = up(exact(br['inner_K_trace_to_canonical_cut_absolute'])/(axis*(1+m)*angular_low))
        hfield = exact(br['complete_weighted_inner_K_trace_to_field_norm'])
        dn = next(r for r in br['densities'] if r['density'] == 'weak_local_rho_16')
        cap = next(r for r in br['densities'] if r['density'] == 'weak_candidate_cap')
        derivative_cut = up(2*exact(dn['canonical_cut_absolute_mode_bound'])/axis)
        # cap >= sigma_candidate^2 * (s+|ell|)*V_I^2 pointwise.
        source_kernel = up(exact(cap['canonical_cut_absolute_mode_bound'])/(candidate_scale**2*axis*strip_low))
        bmode = exact(spectrum['low_complete_sources'][i]['complete_source_upper'])
        value = up(source_kernel*bmode)
        axes.append(axis);linear.append(up(exact(ar['pure_linear_cut_normalized_absolute'])))
        cut_head.append(hcut);field_head.append(hfield);cut_D.append(derivative_cut);source_value.append(value)
        input_rows.append({'mode': m, 'group': 'S' if i < 6 else 'T',
            'axis': record(axis), 'linear_cut_absolute': record(linear[-1]),
            'complete_source_wide_pair_mass': record(bmode),
            'wide_to_sigma_cut_multiplier_upper': record(1/strip_low),
            'complete_outer_source_cut_value': record(value),
            'complete_source_cut_derivative': record(derivative_cut),
            'weighted_beta_cut_operator': record(hcut),
            'weighted_beta_field_operator': record(hfield)})

    def beta_bounds(radius):
        q = 1+(kt+eta)*radius/256
        factors = {'main': q, 'corr': q, 'quadratic': q*q,
                   'remainder': q*(1+q*tmax+(q*tmax)**2/3)}
        nonfar, bridge = [], []
        for row in head['mode_rows']:
            m = int(row['mode'])
            xi = sum_up(up(factors[k]*exact(v)) for k, v in row['old_complete_difference_Xi_pieces'].items())
            delta = up(ci*(1+m)*exp_bounds(m*sigma)[1]*xi)
            old = row['both_strips']['Wsigma1']
            old_delta, old_chosen, auxiliary = [exact(old[k]) for k in ('old_complete_difference', 'old_chosen', 'old_auxiliary')]
            difference = up(delta+old_delta)
            # Remove far only by a valid decomposition, never subtract two bounds.
            bound = min(up(auxiliary+delta), up(old_chosen+difference+far))
            nonfar.append(bound);bridge.append(difference)
        return nonfar, bridge

    def whole_field(components, far_mass):
        return up(sum_up(up(a*b) for a, b in zip(field_head, components))+max(field_head)*far_mass)

    def cut_rows(components, far_mass, field_derivative):
        return [up(cut_D[i]*field_derivative+cut_head[i]*(components[i]+far_mass)) for i in range(6)]

    def cut_T(components, far_mass, field_derivative):
        return up(sum_up(cut_D[6:])*field_derivative+
                  sum_up(up(cut_head[i]*components[i]) for i in range(6, 46))+
                  max(cut_head[6:])*far_mass)

    scenarios = []
    for rt in [F(x) for x in args.radii_t.split(',')]:
        outer_t = 2*rt
        if not 0 < rt <= F(1, 2):
            raise ValueError('The declared T outer circle must fit the unit ball')
        nf, _ = beta_bounds(rt)
        _, transverse_bridge = beta_bounds(outer_t)
        ds = [up(x/(1-radius_s)) for x in nf]
        dt = [up(x/(outer_t-rt)) for x in transverse_bridge]
        far_s, far_t = far/(1-radius_s), 2*far/(outer_t-rt)
        h_s, h_t = whole_field(ds, far_s), whole_field(dt, far_t)
        field_s, field_t = up(h_s/(1-gamma)), up(h_t/(1-gamma))
        ss_rows, st_rows = cut_rows(ds, far_s, field_s), cut_rows(dt, far_t, field_t)
        a, b = max(ss_rows), max(st_rows)
        c, d = cut_T(ds, far_s, field_s), cut_T(dt, far_t, field_t)
        values_s = [up(linear[i]+source_value[i]+cut_head[i]*(nf[i]+far)) for i in range(6)]
        value_t = up(sum_up(linear[6:])+sum_up(source_value[6:])+
                     sum_up(up(cut_head[i]*nf[i]) for i in range(6, 46))+
                     max(cut_head[6:])*far)
        selfmap_s, selfmap_t = max(values_s) < radius_s, value_t < rt
        contraction = schur(a, b, c, d)
        scenarios.append({'radius_S': record(radius_s), 'radius_T': record(rt),
            'Cauchy_outer_T': record(outer_t),
            'complete_value_S_rows': [{'mode': modes[i], 'upper': record(v)} for i, v in enumerate(values_s)],
            'complete_value_S_max': record(max(values_s)), 'complete_value_T_l1': record(value_t),
            'T_linear_l1': record(sum_up(linear[6:])),
            'T_complete_outer_source_l1': record(sum_up(source_value[6:])),
            'T_nonfar_head_l1': record(sum_up(up(cut_head[i]*nf[i]) for i in range(6, 46))),
            'T_far_once': record(max(cut_head[6:])*far),
            'complete_beta_field_derivatives': {'S': record(h_s), 'T': record(h_t)},
            'complete_low_field_derivatives': {'S': record(field_s), 'T': record(field_t)},
            'cut_derivative_positive_matrix': [[record(a), record(b)], [record(c), record(d)]],
            'natural_radius_norm_contraction': record(max(a+b*rt/radius_s, d+c*radius_s/rt)),
            'schur': contraction, 'selfmap_S': selfmap_s, 'selfmap_T': selfmap_t,
            'all46_projected_cut_closed': selfmap_s and selfmap_t and contraction['passed']})
    passed = [i for i, row in enumerate(scenarios) if row['all46_projected_cut_closed']]
    gates = {
        'all_pinned_complete_input_and_source_hashes': True,
        'same_complete_R100_and_actual_spectral_domains': True,
        'all46_low_inputs_and_outputs_retained': len(input_rows) == 46,
        'six_linf_and40_weighted_l1_output_norm': True,
        'complete_mean_inverse_and_nonzero_far_retained': far > 0,
        'paid_absolute_nine_field_contraction': gamma < 1,
        'every_cauchy_outer_T_inside_paid_unit_ball': all(exact(r['Cauchy_outer_T']) <= 1 for r in scenarios),
        'at_least_one_complete_selfmap_and_schur': bool(passed),
    }
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss > args.rss_kib:
        raise MemoryError('Owned observed RSS guard exceeded')
    output = {'schema': 'visible-flex-larger-hybrid46-complete-cut-v1',
        'status': 'Actual complete low46 projected cut arithmetic; inspect selfmap and Schur gates',
        'author': '/root (GPT-6 Astra Pro, AI-assisted)',
        'all_gates': all(gates.values()), 'gates': gates, 'input_identities': identities,
        'source_sha256': sha256(Path(__file__).read_bytes()),
        'complete_field_contraction': record(gamma), 'source_mode_rows': input_rows,
        'scenarios': scenarios, 'successful_scenarios': passed,
        'same_real_low46_projected_solution': True,
        'full_frequency_PDE_middle_high_outer0to9_or_closed_surface_claimed': False,
        'no_Arb': True, 'no_ODE': True, 'no_new_source_integrals': True,
        'elapsed_seconds': time.monotonic()-began, 'owned_peak_rss_kib': rss}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x', encoding='utf8') as f:
        json.dump(output, f, ensure_ascii=False, separators=(',', ':'));f.write('\n')
    raw = args.out.read_bytes()
    summary = {'event': 'complete_cut_consumer_done', 'all_gates': output['all_gates'],
        'output': str(args.out), 'bytes': len(raw), 'sha256': sha256(raw),
        'successful_scenarios': passed, 'seconds': output['elapsed_seconds'], 'RSS_KiB': rss,
        'scenario_displays': [{'rT': r['radius_T']['display_upward'],
            'valueS': r['complete_value_S_max']['display_upward'],
            'valueT': r['complete_value_T_l1']['display_upward'],
            'selfmapS': r['selfmap_S'], 'selfmapT': r['selfmap_T'],
            'Schur': r['schur']['passed'], 'natural_contraction': r['natural_radius_norm_contraction']['display_upward']}
            for r in scenarios]}
    print(json.dumps(summary), flush=True)
    if not output['all_gates']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
