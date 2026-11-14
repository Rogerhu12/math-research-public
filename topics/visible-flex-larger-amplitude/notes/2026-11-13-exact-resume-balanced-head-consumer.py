#!/usr/bin/env python3
"""Exact consumption of the R78 balanced cut mass by the two true R104 columns.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only the actually enclosed modes 94 and 96 are claimed. This is not a
full-middle or nonlinear closure. No new radial integral or Arb run.
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


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(x):
    if isinstance(x, list):
        return F(int(x[0])) * F(2) ** int(x[1])
    if 'mantissa' in x:
        return F(int(x['mantissa'])) * F(2) ** int(x['binary_exponent'])
    if 'numerator' in x:
        return F(int(x['numerator']), int(x['denominator']))
    raise TypeError('Expected a saved exact dyadic or rational')


def rec(x):
    return dict(numerator=str(x.numerator), denominator=str(x.denominator),
                display_only=float(x))


def main():
    start = time.monotonic()
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('primary', 'checkpoint', 'head', 'trace', 'out'):
        p.add_argument('--' + name, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh exact consumer output')
    primary, cp, head, trace = [read(getattr(a, n))
                              for n in ('primary', 'checkpoint', 'head', 'trace')]
    modes = [94, 96]
    order = [[n, j] for n in (11, 10) for j in range(9)]
    expected_head = '9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930'
    expected_trace = '44db92699bd9bf3d8ba613465b013033c82a7ed9f8fc8e5cc1f6a003539ad494'
    gates = dict(
        declared_modes_exact=primary['declared_modes'] == modes == cp['config']['modes'],
        original_primary_gates=primary['all_enclosure_gates'] and all(primary['enclosure_gates'].values()),
        true_head_gates=head['all_gates'] and all(head['gates'].values()),
        true_trace_gates=trace['all_gates'] and all(trace['checks'].values()),
        original18_source_groups=cp['completed_groups'] == order,
        original10793_leaves=cp['counts'] == primary['counts'] and cp['counts']['original_panels'] == 10793,
        entire_causal_tensor_matches_primary=cp['causal_block_rows'] == primary['causal_block_rows'],
        exact_head_identity=digest(a.head) == expected_head == primary['input_hashes'][str(a.head)],
        exact_trace_identity=digest(a.trace) == expected_trace == head['input_hashes'][str(a.trace)],
        same_source_strip=cp['config']['source_strip'] == '18/125',
    )
    B = exact(trace['B']['lower'])
    delta = exact(trace['head_strip']['lower']) - F(18, 125)
    H = exact(head['complete_coarse_trace_rows']['head']['high_bands_value_upper'][0]['upper'])
    gates['strict_positive_paid_B_and_strip_gap'] = B > 592 and delta > 0
    rows = []
    for i, m in enumerate(modes):
        cols = [[exact(v) for v in pair] for pair in cp['initial_component_max'][i]]
        if len(cols) != 2 or any(len(pair) != 2 for pair in cols):
            raise ValueError('Both initial columns and both separate component suprema are required')
        LP, LK = [sum(pair, F(0)) for pair in cols]
        old = exact(primary['rows'][i]['physical_initial_l1_to_field_upper'])
        # The checkpoint rounds each component outward separately, whereas
        # the primary rounds their sum. Re-summing the former can exceed the
        # latter by a last bit; use each valid component endpoint directly.
        gates['mode%d_saved_initial_row_dominates_each_component' % m] = max(v for pair in cols for v in pair) <= old
        z = m * delta
        # exp(z) >= its positive sixth-degree Taylor polynomial for z >= 0.
        strip = 1 / sum((z ** k / math.factorial(k) for k in range(7)), F(0))
        balanced = max(LP / B, LK)
        rows.append(dict(mode=m, initial_component_suprema=cp['initial_component_max'][i],
                         P_input_column_sum=rec(LP), K_input_column_sum=rec(LK),
                         old_physical_l1_gain=rec(old),
                         balanced_gain_without_strip=rec(balanced),
                         rational_strip_factor_upper=rec(strip),
                         balanced_gain_with_strip=rec(balanced * strip),
                         strip_factor_formula='1 / sum(k=0..6,(m*delta)^k/k!)'))
    raw = H * max(exact(row['balanced_gain_without_strip']) for row in rows)
    bound = H * max(exact(row['balanced_gain_with_strip']) for row in rows)
    old = exact(primary['complete_given_head_lift'])
    gates['balanced_lift_below_3_over10'] = raw < F(3, 10)
    gates['balanced_strip_lift_below_283_over1000'] = bound < F(283, 1000)
    gates['strict_improvement_over_previous_valid_lift'] = bound < old
    if not all(gates.values()):
        raise ArithmeticError('An exact same-object or inequality gate failed: ' + str(gates))
    output = dict(
        schema='visible-flex-balanced-two-column-head-lift-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        status='Proved and exactly evaluated lift for the actual m94/m96 projection of the R74 true head',
        all_gates=True, gates=gates, declared_modes=modes,
        parameter_domain='The original R74 complex twenty-axis polydisc consumed by R78; no R100 extension inferred',
        input_norm='sum signed m (1+|m|) exp(tau_head|m|) (Bcut |P_m|+|K_m|)',
        output_norm='X_V at constant strip 18/125, both components separately supremized over all true leaves',
        balanced_B_lower=rec(B), exact_head_to_output_strip_gap_lower=rec(delta),
        complete_shared_near_band_mass=rec(H), rows=rows,
        two_mode_lift_without_strip_gain=rec(raw), two_mode_lift_with_strip_gain=rec(bound),
        previous_valid_two_mode_lift=rec(old), improvement_factor_lower=rec(old/bound),
        strict_simple_final_upper='283/1000',
        covers_all_middle_modes=False, source_operator_updated=False,
        full_nonlinear_contraction=False, all46_cut_closed=False, closed_surface_claimed=False,
        no_extra_positive_negative_mode_factor=True,
        no_new_Arb_ODE_or_source_integral=True,
        input_hashes={str(getattr(a, n)): digest(getattr(a, n))
                      for n in ('primary', 'checkpoint', 'head', 'trace')},
        source_sha256=digest(Path(__file__)), elapsed_seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(dict(all_gates=True, balanced_bound=float(bound),
                          old_bound=float(old), improvement=float(old/bound),
                          elapsed_seconds=output['elapsed_seconds'], peak_rss_kib=output['peak_rss_kib'])))


if __name__ == '__main__':
    main()
