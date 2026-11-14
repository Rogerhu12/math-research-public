#!/usr/bin/env python3
"""Exact-rational endpoint lift after all candidate linear forcing cancels.

The saved outer candidate height is r^4 times the original binary Q. The
variation-of-constants identity therefore reduces the complete linear
candidate contribution to q_cut-Q_outer/S0. No candidate momentum is
rounded or separately subtracted. The true head nonlinear DN remainder
is retained; the nonlinear OUTER source integral is still required.

Only Python Fraction/JSON/gzip is used. No Arb, ODE or source integration.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dyadic(x):
    m, e = int(x['mantissa']), int(x['binary_exponent'])
    return F(m*(1 << e)) if e >= 0 else F(m, 1 << (-e))


def ball(x):
    lo, hi = dyadic(x['lower']), dyadic(x['upper'])
    if lo > hi:
        raise ValueError('A saved exact interval is reversed')
    return lo, hi


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[1], -x[0]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    products = [a*b for a in x for b in y]
    return min(products), max(products)


def div(x, y):
    if y[0] <= 0 <= y[1]:
        raise ZeroDivisionError('The actual true S0 must be nonzero')
    return mul(x, (1/y[1], 1/y[0]))


def abs_bounds(x):
    return (F(0) if x[0] <= 0 <= x[1] else min(abs(t) for t in x)), max(abs(t) for t in x)


def record(x):
    return dict(lower=dict(numerator=str(x[0].numerator), denominator=str(x[0].denominator)),
                upper=dict(numerator=str(x[1].numerator), denominator=str(x[1].denominator)),
                display_float=[float(x[0]), float(x[1])],
                representation='exact rational interval; display_float is not a certificate')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('flow', 'signed-cut', 'response', 'candidate11', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--rss-kib', type=int, default=40960)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh endpoint-cancellation ledger')
    began = time.monotonic()
    names = ('flow', 'signed_cut', 'response', 'candidate11')
    hashes = {str(getattr(a, k)):sha(getattr(a, k)) for k in names}
    flow = json.loads(a.flow.read_text())
    signed = json.loads(a.signed_cut.read_text())
    candidate = json.loads(a.candidate11.read_text())
    with gzip.open(a.response,'rt') as stream:
        response = json.load(stream)['response']
    cp = response['checkpoint']
    if (not all(flow['gates'].values()) or not signed['all_gates']
            or not all(candidate['gates'].values()) or candidate['cell'] != 11
            or not response['converged'] or cp['parameters']['modes'] != 20
            or cp['parameters']['physicalDepth'] != 12 or len(cp['rawStates']) != 13
            or candidate['input_hashes'].get(str(a.response)) != hashes[str(a.response)]):
        raise ValueError('The complete same actual finite candidate and true background are required')
    slope_hashes = {p:s for p,s in signed['input_hashes'].items() if 'taylor-cut-' in p}
    if len(slope_hashes) != 1 or any(flow['input_hashes'].get(p) != s for p,s in slope_hashes.items()):
        raise ValueError('The common true slope was changed')
    rows = {r['mode']:r for r in signed['rows']}
    co = ball(signed['K_per_unit_mu11_slope'])
    outputs = []
    for cell in flow['cell_rows']:
        n = cell['endpoint_physical_node']
        if n not in (11, 10) or len(cp['rawStates'][n]) != 40:
            raise ValueError('An original actual M20 endpoint is absent')
        for mode in cell['modes']:
            m = mode['mode']
            row = rows[m]
            if (mode['shared_exact_dyadic_slope'] != row['shared_exact_dyadic_slope']
                    or mode['true_minus_shared_exact_slope'] != row['true_minus_shared_exact_slope']):
                raise ValueError('The exact shared slope and its remainder must be retained')
            q = F.from_float(cp['rawStates'][12][m//2-1])
            qR = F.from_float(cp['rawStates'][n][m//2-1])
            if ball(row['actual_canonical_Q']) != (q, q):
                raise ValueError('The actual saved cut height differs')
            S = ball(mode['S0_true_Q'])
            E0 = sub((q,q), div((qR,qR), S))
            B = ball(mode['S0_affine_B'])
            coeff = abs_bounds(div(B,mul(co,S)))[1]
            nonlinear = (ball(row['auxiliary_nonlinear_K_upper'])[1]+
                         ball(row['full_head_feedback_same_mode_K_upper'])[1])
            nonlinear_radius = coeff*nonlinear
            full_head_lift = add(E0,(-nonlinear_radius,nonlinear_radius))
            axis = ball(row['canonical_parameter_axis'])
            outputs.append(dict(endpoint_physical_node=n,mode=m,
                same_exact_saved_cut_Q=record((q,q)),
                exact_saved_outer_candidate_Q=record((qR,qR)),
                shared_exact_dyadic_slope=row['shared_exact_dyadic_slope'],
                same_true_S0_Q=mode['S0_true_Q'],
                complete_linear_endpoint_residual_canonical_Q=record(E0),
                complete_linear_endpoint_residual_axis_ratio=record(div(abs_bounds(E0),axis)),
                true_head_nonlinear_cut_lift_radius=record((nonlinear_radius,nonlinear_radius)),
                complete_head_lift_minus_outer_candidate_Q=record(full_head_lift),
                complete_head_lift_axis_ratio=record(div(abs_bounds(full_head_lift),axis)),
                complete_head_lift_correction_canonical_Q=record(neg(full_head_lift)),
                canonical_parameter_axis=record(axis),
                complete_outer_N_source_integral_included=False))
    gates = dict(same_original_full20_saved_candidate=True,
        original_Q_at_cut_matches_true_head_reference=True,
        all_four_true_S0_denominators_nonzero=True,
        common_slope_in_true_head_and_outer_flow=True,
        candidate_linear_source_cancels_exactly_by_variation_of_constants=True,
        no_independent_subtraction_of_candidate_L=True,
        full_R63_and_R58_cut_nonlinearity_retained=True,
        outer_nonlinear_source_kept_as_unpaid_separate_term=True,
        exact_rational_arithmetic_only=True)
    result = dict(status='Actual whole-two-cell linear endpoint cancellation; outer nonlinear source remains separate',
        gates=gates, all_gates=all(gates.values()), rows=outputs,
        exact_identity='[Phi beta - integral Phi L(candidate)]_Q / S0 = q_cut-Q_candidate(R)/S0, including all candidate linear forcing. Add the true head nonlinear cut term and integral Phi N separately.',
        correction_sign='The displayed endpoint residual is (predicted endpoint-candidate endpoint)/S0; a linearized root correction has its negative sign.',
        no_change_to_g_or_candidate=True,
        complete_outer_Schur_residual_paid=False,
        full46_or_infinite_frequency_outer_inverse_paid=False,
        input_hashes=hashes, entrypoint_sha256=sha(Path(__file__)),
        new_Arb_operations=0,new_source_integrals=0,new_ODE_solves=0,
        elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result['peak_RSS_KiB'] > a.rss_kib:
        raise MemoryError('The owned short exact ledger exceeded its observation threshold')
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='complete',all_gates=True,
        rows=[dict(node=r['endpoint_physical_node'], mode=r['mode'],
                   residual=r['complete_linear_endpoint_residual_canonical_Q']['display_float'],
                   total_head_lift_ratio=r['complete_head_lift_axis_ratio']['display_float'])
              for r in outputs],seconds=result['elapsed_seconds'],
        peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__ == '__main__':
    main()
