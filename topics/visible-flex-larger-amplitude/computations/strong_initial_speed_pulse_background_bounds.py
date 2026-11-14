#!/usr/bin/env python3
"""Exact rational bounds for the unchanged background pieces after a pulse.

Combined with the referenced first-piece Bernstein certificate, this proves
|kappa_i|<8 for the entire surface-of-revolution prefix and bridge at the five
listed pulse values.  It does not bound the actual nonaxisymmetric immersion,
the remaining tail/cap, diameter, or reach, and it solves no BVP.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted-reference', type=Path, required=True)
    parser.add_argument('--pulse-budget', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    start = time.time()
    sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    sources = {str(p): sha(p) for p in (Path(__file__), args.accepted_reference, args.pulse_budget)}
    record = json.loads(gzip.decompress(args.accepted_reference.read_bytes()))
    budget = json.loads(args.pulse_budget.read_text())
    if not record['solver_success'] or budget['accepted_reference_sha256'] != sha(args.accepted_reference):
        raise ValueError('Different accepted reference')
    cfg, cut = record['frozen_profile'], record['physical_tail_cut']
    q = {k: F(v) for k, v in cfg.items() if isinstance(v, (float, int))}
    V, vp, vd, vl = (q[k] for k in ('vu', 'boost_speed', 'vd', 'loop_speed'))
    LB, r, K, Ks, Ksync = (q[k] for k in ('boost_length', 'loop_radius', 'loop_curvature',
        'descending_turn_curvature', 'descending_sync_curvature'))
    eps = F(.08)
    f = q['terminal_peak_fraction']
    rc, w, minus_second = F(cut['radius']), F(cut['backgroundSlope']), -F(cut['backgroundSecond'])
    # Alternating Taylor bounds; 0 < x <= 1.4, and terms decrease in size.
    sin_lower = lambda x: x-x**3/6+x**5/120-x**7/5040
    cos_upper = lambda x: 1-x*x/2+x**4/24
    cos_lower = lambda x: 1-x*x/2
    angle_vl_upper, angle_vp_upper = F(7, 5), F(21, 20)
    acos_vl_upper, acos_vd_upper, acos_vl_lower = F(9, 50), F(21, 100), F(1, 10)
    checks = {
        'positive_profile_order': 0 < V < vp < 1 and 0 < vd < vl < 1,
        'positive_lengths_and_curvature_controls': min(LB, r, K, Ks, Ksync, rc, w, minus_second) > 0,
        'positive_radius_increment_and_coast': q['delta'] > 0 and q['coast_outward'] >= 0 and q['loop_ratio'] > 1,
        'pulse_keeps_initial_acceleration_and_endpoint_data': budget['rho_core_R7_initial_k0_unchanged'],
        'sin_1p4_lower_exceeds_loop_speed': sin_lower(angle_vl_upper) > vl,
        'sin_1p05_lower_exceeds_boost_speed': sin_lower(angle_vp_upper) > vp,
        'cos_p18_upper_below_loop_speed': cos_upper(acos_vl_upper) < vl,
        'cos_p21_upper_below_descending_speed': cos_upper(acos_vd_upper) < vd,
        'cos_p1_lower_above_loop_speed': cos_lower(acos_vl_lower) > vl,
        'bridge_turn_is_inward': 0 < f < 1 and (1-f)*w < acos_vl_lower,
    }
    first_turn_length_upper = F(22, 7)/(Ks*(1-eps))
    first_turn_radius_lower = 1-first_turn_length_upper
    sync_length_upper = acos_vd_upper/(Ksync*(1-eps))
    loop_radius_lower = r-angle_vl_upper/(K*(1-eps))
    boost_curvature_upper = (angle_vp_upper-V)/(LB*(1-eps))
    bridge_turn_length_upper = acos_vl_upper/(K*(1-eps))
    # atan(w)<w and (1+w^2)^(3/2)<(1+w^2)^2.
    bridge_brake_length_upper = 2*f*w*(1+w*w)**2/minus_second
    checks.update({
        'descending_coast_length_positive': first_turn_radius_lower > r+sync_length_upper,
        'bridge_coast_length_positive': bridge_turn_length_upper+bridge_brake_length_upper < r-rc,
        'loop_radius_lower_exceeds_one_eighth': loop_radius_lower > F(1, 8),
        'first_turn_radius_lower_exceeds_one_eighth': first_turn_radius_lower > F(1, 8),
        'coast_and_sync_radius_exceeds_one_eighth': r > F(1, 8),
        'bridge_radius_exceeds_one_eighth': rc > F(1, 8),
        'boost_curvature_below_eight': boost_curvature_upper < 8,
        'all_original_turn_and_brake_curvatures_below_eight': max(K, Ks, Ksync, minus_second) < 8,
    })
    initial = []
    for row in budget['rows']:
        cert = row['meridian_curvature_below_8_certificate']
        ok = (cert['passed'] and cert['all_closed_parameter_intervals_covered']
            and all(F(leaf['lower']) > 0 for leaf in cert['leaves'])
            and row['radius_minimum_proved'] >= 1 and row['parallel_curvature_upper_proved'] <= 1)
        initial.append(dict(pulse_height=row['pulse_height'], referenced_initial_certificate_positive=ok))
    checks['all_five_referenced_initial_certificates_positive'] = len(initial) == 5 and all(r['referenced_initial_certificate_positive'] for r in initial)
    bounds = dict(first_turn_length_upper=first_turn_length_upper,
        first_turn_radius_lower=first_turn_radius_lower, sync_length_upper=sync_length_upper,
        loop_radius_lower=loop_radius_lower, boost_curvature_upper=boost_curvature_upper,
        bridge_turn_length_upper=bridge_turn_length_upper, bridge_brake_length_upper=bridge_brake_length_upper,
        bridge_coast_radial_margin_lower=r-rc-bridge_turn_length_upper-bridge_brake_length_upper,
        global_background_radius_lower=min(F(1), first_turn_radius_lower, loop_radius_lower, r, rc))
    result = dict(scope=__doc__, source_sha256_at_start=sources, passed=all(checks.values()), checks=checks,
        exact_bounds={k:str(v) for k,v in bounds.items()}, approximate_bounds={k:float(v) for k,v in bounds.items()},
        first_piece_certificates=initial, complete_background_principal_curvature_strict_upper=8,
        sample_grid_not_used_in_this_proof=True, trigonometric_bounds='alternating rational Taylor bounds and pi<22/7',
        exact_binary64_profile_parameters={k:str(v) for k,v in q.items()},
        exact_binary64_cut_parameters=dict(radius=str(rc),w=str(w),minus_second=str(minus_second)),
        actual_nonlinear_surface_or_tail_cap_or_reach_certified=False, BVP_evaluations=0, Node_workers=0,
        proof_explanation_file='notes/2026-11-12-strong-initial-speed-pulse-envelope.md', seconds=time.time()-start)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(dict(passed=result['passed'], checks=checks, approximate_bounds=result['approximate_bounds'])), flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
