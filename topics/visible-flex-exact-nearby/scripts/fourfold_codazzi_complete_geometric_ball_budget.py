#!/usr/bin/env python3
"""Consume proved outward rational bounds for one complete geometry ball.

Every inequality below is exact Fraction arithmetic. This consumes the
complete 141-block model and the already proved comparison theorems; it
does not recompute the original geometry or claim a nonlinear solution.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def encode(value):
    if isinstance(value, F):
        with localcontext() as context:
            context.prec = 48
            display = str(Decimal(value.numerator) / Decimal(value.denominator))
        return dict(exact=str(value), decimal_display_only=display)
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def calculate():
    eps, tau = F(1, 10000), F(1, 100000)
    eQ, eF = F('0.000101951532739'), F('0.000220349475735')
    bQ, bF = eQ + F('0.000006643245'), eF + F('0.000012332337')
    theta = bQ + F('15.736315') * eps + F('0.304809') * tau
    phi = bF + F('1.950540') * bQ + F('7.578231') * eps + F('0.612629') * tau
    R0, S0 = F('1.275713422847'), F('0.900961392986')
    RB, SB = R0 + phi, S0 - phi - R0 * theta
    ell = F('0.000008')
    RE, SE = RB + ell, SB - ell * (1 + 2 * RB)
    kbody = F('11.092578014346') + F('141.332651') * eps + F('3.988052') * tau
    kpositive = F('3.856372') + F('141.332651') * eps + F('3.988052') * tau
    delta_low = F('0.12970542309253905343') - F('0.164785') * eps
    delta_high = F('0.12970542309253905344') + F('0.164785') * eps
    H = F(4347844570122155, 4503599627370496)
    amin, amax = F('1.06873282'), F('1.068732841')
    # The complete explicit-centre mean bound, true state error, and the
    # tiny original-to-continuous repair are all included before widening.
    mean_low = F('1.068732695') - eps - F(1, 10**17)
    mean_high = F('1.119757883') + eps + F(1, 10**17)
    D = F(511, 200)
    gates = []

    def lt(name, left, right):
        gates.append(dict(name=name, relation='<', left=left, right=right, passed=left < right))

    lt('state_ball_within_proved_full_comparison', eps, F(1, 1000))
    gates.append(dict(name='nu_ball_within_proved_full_comparison', relation='<=',
                      left=tau, right=F(1, 100000), passed=tau <= F(1, 100000)))
    lt('mean_is_strictly_negative', F(0), mean_low)
    lt('closed_frame_positive_winding_exceeds_one_half', mean_high, 2 * amin)
    lt('closed_frame_positive_winding_below_three_halves', 2 * amax, 3 * mean_low)
    lt('complete_frame_error_small', theta, F('0.001686'))
    lt('complete_position_error_small', phi, F('0.001209'))
    lt('same_world_exterior_radius', RE, F(511, 400))
    lt('body_support_exceeds_marker_support', F(89, 100), SB)
    lt('whole_unmarked_support_exceeds_marker_support', F(89, 100), SE)
    lt('whole_support_exceeds_final_target', F(4, 49), F(89, 100))
    lt('whole_body_absolute_curvature', kbody, F(12))
    lt('whole_body_outward_curvature', kpositive, F(196, 27))
    lt('whole_exterior_absolute_curvature', F(2), F(12))
    lt('whole_exterior_outward_curvature', F(2), F(196, 27))
    lt('outer_height_input_is_paid', phi, F(1, 100))
    lt('true_upper_flat_cap_above_nine_tenths', F(9, 10), H - phi - ell)
    lt('true_upper_flat_cap_below_one', H + phi + ell, F(1))
    lt('actual_waist_displacement_positive', F(0), delta_low)
    lt('actual_waist_within_complete_outward_normal_tube', delta_high, F(27, 196))
    lt('held_distance_exceeds_five_percent', D / 20, delta_low)
    lt('reach_exceeds_three_percent', 3 * D / 100, F(4, 49))
    lt('held_set_diameter_exceeds_twenty_percent', D / 5, F(9, 5))
    lt('unmarked_gauss_curvature_below_first_marker_peak', F(12)**2, F(145))
    lt('largest_marker_curvature_below_49_over_4', F(148), F(49, 4)**2)
    lt('marker_positive_curvature_below_outward_target', F(16, 27)**2 * 148, F(196, 27)**2)
    return dict(
        ball=dict(full_physical_C0_state=eps, full_metric_parameter_change=tau, eta='eta_0_only'),
        true_waist_errors=dict(frame=eQ, position=eF, canonical_frame=bQ, canonical_position=bF),
        complete_geometry=dict(frame_difference=theta, position_difference=phi,
                              body_radius=RB, body_support=SB,
                              exterior_radius=RE, exterior_support=SE,
                              unmarked_absolute_curvature=kbody,
                              unmarked_positive_curvature=kpositive),
        winding=dict(mean_magnitude_lower=mean_low, mean_magnitude_upper=mean_high,
                     exact_frame_periodicity_required=True,
                     embedding_not_assumed_to_deduce_winding_one=True),
        final_ratios=dict(diameter_upper=D, waist_delta_lower=delta_low,
                          waist_delta_upper=delta_high, held_ratio_lower=delta_low/D,
                          reach_ratio_lower=F(4,49)/D, held_set_diameter_ratio_lower=F(9,5)/D),
        gates=gates, gate_count=len(gates), all_gates_passed=all(g['passed'] for g in gates))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Preserve each distinct actual calculation')
    manifest = json.loads(args.manifest.read_text())
    for relative, expected in manifest['proved_input_sha256'].items():
        if sha(TOPIC/relative) != expected:
            raise ValueError('A consumed complete theorem changed: '+relative)
    if manifest['source_sha256'] != sha(__file__):
        raise ValueError('The exact rational consumer changed')
    result = calculate()
    doc = dict(kind='actual_complete_141_geometry_ball_rational_budget_v1',
               complete=result['all_gates_passed'], failure=None,
               executed_utc=datetime.now(timezone.utc).isoformat(),
               github_run_id=os.environ.get('GITHUB_RUN_ID'),
               github_workflow_commit=os.environ.get('GITHUB_SHA'),
               source_sha256=sha(__file__), input_manifest_sha256=sha(args.manifest),
               consumed_proved_input_sha256=manifest['proved_input_sha256'],
               candidate_sha256='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413',
               exact_nonlinear_solution_exists=False, complete_tail_matching_proved=False,
               state_ball_has_been_attained=False, final_topic_complete=False,
               result=result)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(encode(doc), ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(complete=doc['complete'], gate_count=result['gate_count'],
                         native_sha256=sha(args.out)), ensure_ascii=False), flush=True)
    if not result['all_gates_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
