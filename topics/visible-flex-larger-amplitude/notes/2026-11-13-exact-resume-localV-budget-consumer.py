#!/usr/bin/env python3
"""Exact eighteen-block budget for the actual m94/m96 local-V projection.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The fixed low46 centre and full mean/inverse are retained. This solves only
the declared two-mode projected equation, not the all-frequency system.
"""
import argparse
import gzip
import hashlib
import json
import math
import resource
import time
from fractions import Fraction as F
from pathlib import Path


def read(p):
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2)**int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator), display_only=float(v))


def dyadic_up(v, bits=96):
    if v <= 0:
        raise ArithmeticError('Only strictly positive radii or weights may be rounded')
    unit = F(2)**(v.numerator.bit_length()-v.denominator.bit_length()-bits)
    return (v//unit+1)*unit


def main():
    start = time.monotonic()
    p = argparse.ArgumentParser(description=__doc__)
    for n in ('linear', 'original', 'balanced', 'spectral', 'out'):
        p.add_argument('--'+n, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh exact eighteen-block consumer output')
    linear, old, balanced, spectral = [read(getattr(a, n))
                                     for n in ('linear', 'original', 'balanced', 'spectral')]
    modes = [94, 96]
    order = [(n, j) for n in (11, 10) for j in range(9)]
    gates = dict(
        completed_actual_linear_gates=linear['all_enclosure_gates'] and all(linear['enclosure_gates'].values()),
        original_physical_tensor_bitwise_reproduced=linear['original_causal_tensor_bitwise_reproduced'],
        same_counts=linear['counts'] == old['counts'] and linear['counts']['original_panels'] == 10793,
        exact_two_declared_modes=linear['declared_modes'] == modes == balanced['declared_modes'],
        complete18_targets=[(r['target_cell'], r['target_segment']) for r in linear['causal_block_rows']] == order,
        paid_balanced_head=balanced['all_gates'] and all(balanced['gates'].values()),
        paid_complete_centre_and_source=spectral['all_gates'] and all(spectral['gates'].values()),
        actual_centre_norm_below10=ex(spectral['final_field_norm']) < 10,
        same_constant_strip=linear['config']['source_strip'] == '18/125',
    )
    expected_original = '9e28fcf3ea53003e16ec8720a2fd4c52da0d16a40c8a90398c0b847d0f2fc317'
    old_raw = gzip.decompress(a.original.read_bytes()) if a.original.suffix == '.gz' else a.original.read_bytes()
    gates['same_fresh_R104_reference'] = (hashlib.sha256(old_raw).hexdigest() == expected_original
        == linear['config']['original_completed_causal_tensor_sha256'])
    H = ex(balanced['complete_shared_near_band_mass'])
    B = ex(balanced['balanced_B_lower'])
    delta = ex(balanced['exact_head_to_output_strip_gap_lower'])
    bm = {r['mode']: ex(r['upper']) for r in spectral['selected_middle_sources'] if r['mode'] in modes}
    gates['both_complete_centre_mode_caps'] = sorted(bm) == modes
    rows, radii, weights, Grows, initial, pure, vmax = [], [], [], [], [], [], []
    for i, target in enumerate(linear['causal_block_rows']):
        if [r['mode'] for r in target['modes']] != modes:
            raise ValueError('An actual mode row was omitted or reordered')
        given = []
        residual = F(0)
        kernels = {power: [] for power in (2, 1, 0)}
        mode_diagnostics = []
        for mr in target['modes']:
            m = mr['mode']
            if [(r['source_cell'], r['source_segment']) for r in mr['source_rows']] != order[:i+1]:
                raise ValueError('A source-origin row violates the full causal order')
            cols = [sum((ex(v) for v in pair), F(0)) for pair in mr['initial_localV_separate_component_sups']]
            factor = 1/sum(((m*delta)**k/F(math.factorial(k)) for k in range(7)), F(0))
            gain = max(cols[0]/B, cols[1])*factor
            given.append(H*gain)
            for sr in mr['source_rows']:
                if [r['V_power'] for r in sr['localV_density_rows']] != [2, 1, 0]:
                    raise ValueError('A complete source material is missing')
                if not all(r['true_whole_leaf_V_divisor'] for r in sr['localV_density_rows']):
                    raise ValueError('Actual target-leaf V was not included before supremum')
            residual += sum((ex(sr['localV_density_rows'][0]['localV_strong_output_row'])*bm[m]
                             for sr in mr['source_rows']), F(0))
            mode_diagnostics.append(dict(mode=m, balanced_head_lift=rec(H*gain),
                Gamma2_diagonal=sr['localV_density_rows'][0]['localV_strong_output_row'],
                old_physical_Gamma1_diagonal=sr['density_rows'][1]['physical_strong_output_row']))
        for power_index, power in enumerate((2, 1, 0)):
            for j in range(i+1):
                kernels[power].append(max(ex(mr['source_rows'][j]['localV_density_rows'][power_index]['localV_strong_output_row'])
                                          for mr in target['modes']))
        initial.append(max(given))
        pure.append(residual)
        vmax.append(ex(target['V_max']))
        G = kernels[2]
        Grows.append(G)
        previous = sum((G[j]*(40*radii[j]+2*radii[j]**2) for j in range(i)), F(0))
        A = initial[-1]+residual+previous
        if not 40*G[i] < 1:
            raise ArithmeticError('The exact local-V diagonal sufficient comparison failed at '+str(order[i]))
        ri = dyadic_up(2*A/(1-40*G[i]))
        radii.append(ri)
        image = A+G[i]*(40*ri+2*ri**2)
        J = [4*G[j]*(10+radii[j]) for j in range(i+1)]
        if not J[i] < F(1, 2):
            raise ArithmeticError('The declared one-half distance target failed on a diagonal')
        wi = dyadic_up((1+sum((J[j]*weights[j] for j in range(i)), F(0)))/(F(1, 2)-J[i]))
        weights.append(wi)
        distance = sum((J[j]*weights[j] for j in range(i+1)), F(0))/wi
        domain = (10+ri)*vmax[-1]
        row = dict(index=i, cell=order[i][0], segment=order[i][1],
                   radius=rec(ri), full_projected_image=rec(image), strict_slack=rec(ri-image),
                   image_over_radius=rec(image/ri), balanced_true_head_lift=rec(initial[-1]),
                   complete_low_centre_source=rec(residual), earlier_block_feedback=rec(previous),
                   comparison_diagonal_40Gamma2=rec(40*G[i]), distance_weight=rec(wi),
                   weighted_complete_distance_row=rec(distance),
                   physical_whole_field_domain=rec(domain), mode_diagnostics=mode_diagnostics,
                   original_source_materials={str(power): [rec(v) for v in kernels[power]] for power in (2, 1, 0)},
                   gates=dict(radius_positive=ri>0, strict_selfmap=image<ri,
                              distance_weight_positive=wi>0, strict_distance_below_half=distance<F(1, 2),
                              physical_domain_below_two_minus34=domain<F(2)**-34))
        rows.append(row)
    gates['all18_original_row_selfmap_and_distance_gates'] = all(all(r['gates'].values()) for r in rows)
    gates['all_three_materials_retained'] = all(len(r['original_source_materials']) == 3 for r in rows)
    if not all(gates.values()):
        raise ArithmeticError('An original identity or projected budget gate failed: '+str(gates))
    result = dict(schema='visible-flex-actual-localV-two-mode-18block-fixed-point-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        status='All exact eighteen-block gates pass for the declared m94/m96 nonlinear projected equation about fixed complete low46 centre',
        all_gates=True, gates=gates, modes=modes,
        equation='v = given true m94/m96 head lift + G_{94,96} P_{94,96} N(C_L+v)',
        parameter_domain='Real R74 twenty-axis domain, contained in real R100 by R100 section1 and its paid old-axis inclusion',
        fixed_low_centre='Same R91/R101 complete low46 projected solution; low boundary targets unchanged',
        complete_mean_and_inverse_retained=True, negative_modes_retained=True,
        shared_modal_mass_used=True, source_factor_C0=10, chosen_distance_target='1/2',
        maximum_radius=rec(max(radii)), maximum_image_over_radius=rec(max(ex(r['image_over_radius']) for r in rows)),
        maximum_weighted_distance=rec(max(ex(r['weighted_complete_distance_row']) for r in rows)),
        maximum_physical_whole_field_domain=rec(max(ex(r['physical_whole_field_domain']) for r in rows)),
        rows=rows, all_middle_frequencies_closed=False, low_feedback_equation_closed=False,
        high_feedback_equation_closed=False, all46_cut_closed=False,
        full_outer_or_closed_surface_claimed=False, no_new_Arb_ODE_or_source_integral=True,
        input_hashes={str(getattr(a,n)):digest(getattr(a,n)) for n in ('linear','original','balanced','spectral')},
        source_sha256=digest(Path(__file__)), elapsed_seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(all_gates=True, maximum_radius=float(max(radii)),
                         maximum_image_over_radius=result['maximum_image_over_radius']['display_only'],
                         maximum_weighted_distance=result['maximum_weighted_distance']['display_only'],
                         maximum_physical_domain=result['maximum_physical_whole_field_domain']['display_only'],
                         elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])))


if __name__=='__main__':
    main()
