#!/usr/bin/env python3
"""Fraction-only position budget for the frozen R21 M12 closed map.

Uses already certified cell-zero integrals, tight alpha, global displacement,
and prefix norm.  No solver, interval backend, geometry reader, or sampling.
This is an additional same-map scalar proof, not a new README completion gate.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

TOPIC = Path(__file__).resolve().parent.parent
INPUTS = {
    'budget': ('notes/2026-11-09-db6f-root-closed-budget-m12-critical-r01.json', '50410a4e57b8a21937dd3a99c25942b36cebd5c5819f1e10982584412ae601a7'),
    'geometry': ('notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json', '253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'),
    'prefix': ('notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01-geometry.json', 'fc00c975f1ec9b0413d2d1c77e0dbf3dd27d35016c0b335ff439aba4aeeca462'),
    'first': ('notes/2026-11-09-db6f-tail-first-flat17-m12-critical-r01.json', '5c2ddbfc230416cf7805bf84ea5686ed9db1427c2df2b8f1b3a8379b453e848d'),
    'height': ('notes/2026-11-09-db6f-tail-background-height-rigorous.json', 'dd64e00bf25124b03e725792e321e961106c6ee643f5526e0b5b95383161ff01'),
    'alpha': ('notes/2026-11-09-db6f-tail-tight-alpha.json', '04aae85c19f78fd82808ac32b104537dbb584c39cac8a648107722c855685c62'),
    'whole': ('notes/2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01-lowmetric.json', 'f329aaea39722b02b48ce98fe11e4232ae2c60b57a94789b071dfb5c915f49c5'),
}
PROOFS = {
    'R17': ('results/R17-exact-finite-visible-closed-geometry.md', 'd7ad70cfb98d552ce0832555c230b644e49a21cd5cef2ae16a291013ad66e725'),
    'R21': ('results/R21-m12-whole-map-and-actual-metric-decrease.md', '3d8e20c610ac322e2f4a7093c44b4b37cde314724136cee489dae73c44497c0c'),
    'height_proof': ('notes/2026-11-09-db6f-tail-background-height-interval-proof.md', '46e06ce3740b14c2c68fd33dbfc397d42d05452e83769fdfb956a87be6635e1c'),
    'alpha_review': ('notes/2026-11-09-db6f-audit-high-order-and-tight-alpha.md', '033e47a8fa82fd7c51360215365b3f4a9abed4646c29462705366bb43a40f47a'),
    'budget_source': ('scripts/db6f-root-closed-budget-v2.py', '0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641'),
}


def check(ok, message):
    if not ok:
        raise ValueError(message)


def q(value):
    check(type(value) in (int, float), 'Expected finite binary numerical bound')
    return Q(value)


def record(value):
    value = Q(value)
    f = float(value)
    lo = math.nextafter(f, -math.inf) if Q(f) > value else f
    hi = math.nextafter(f, math.inf) if Q(f) < value else f
    return dict(exact=str(value), lower_display=lo, upper_display=hi)


def load(name, digest, records, decode=True):
    p = TOPIC/name
    data = p.read_bytes()
    check(hashlib.sha256(data).hexdigest() == digest, 'Changed frozen input: '+name)
    records.append(dict(file=str(p), sha256=digest, bytes=len(data)))
    return json.loads(data) if decode else None


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    check(not args.out.exists(), 'Refusing to overwrite an earlier proof record')
    records = []
    x = {key: load(*item, records) for key, item in INPUTS.items()}
    for item in PROOFS.values():
        load(*item, records, decode=False)
    budget, geom, pref, first, height, alpha, whole = [x[k] for k in INPUTS]
    gsha = INPUTS['geometry'][1]
    check(pref['geometry_sha256'] == whole['geometry_sha256'] == gsha, 'Different prefix/whole map')
    check(pref['data_sha256'] == geom['data_sha256'], 'Prefix position data differs')
    check(first['manifestSHA256'] == whole['tail_manifest_sha256'] == geom['tail_manifest_sha256'], 'Different actual tail')
    check(pref['continuous_bounds_certified'] is True and pref['entire_finite_prefix_covered'] is True, 'Partial prefix norm')
    for key, linked in [('geometry', 'geometry'), ('geometry_certificate', 'prefix'), ('tail_first', 'first'), ('height', 'height')]:
        check(budget['inputs'][key]['sha256'] == INPUTS[linked][1], 'Closed-budget link differs: '+key)
    check(whole['closed_budget_sha256'] == INPUTS['budget'][1], 'Whole budget differs')
    check(budget['script_sha256'] == PROOFS['budget_source'][1], 'Different height-constant arithmetic')
    check(height['checkpointSHA256'] == alpha['inputs']['checkpoint']['sha256'], 'Height/alpha physical source differs')
    check(height['bookkeepingSHA256'] == alpha['inputs']['numerical_bookkeeping']['sha256'], 'Different frozen cell-zero calibration')
    check(q(geom['frozen_profile']['cut_radius']) == Q(.6), 'Changed fixed outer radius')

    # This H interval is the original shape.background_cut_height bound.
    # The frozen budget source forms zmax=Hhi+old_B+V, zmin=Hlo-V.
    U = max(q(first[k]['r0theta0Planar']) for k in ('finite', 'collar'))
    V = max(q(first[k]['r0theta0Height']) for k in ('finite', 'collar'))
    check(U == q(first['entireTail']['planarDisplacementUpper']) and
          V == q(first['entireTail']['heightDisplacementUpper']), 'Global displacement aggregation differs')
    Hhi = Q(budget['tail_height_upper']['exact'])-q(height['wholeHeightUpper'])-V
    Hlo = Q(budget['tail_height_lower']['exact'])+V
    check(0 < Hlo <= Hhi and Hlo-V > 0, 'Height sign or cut interval failed')
    c = Q(.6)
    cuff_lower, cuff_upper = Q(7, 50), Q(3, 20)  # analytic R17/R21 cuff box
    cap_height = Q(1, 2000)                       # same R16 fixed bump
    alo, ahi = map(q, alpha['exactRadialAlpha'])
    check(0 < alo <= ahi, 'Unproved positive tight alpha')
    segments = height['segments']
    check(len(segments) == 9 and {s['segment'] for s in segments} == set(range(9)), 'Cell-zero segment coverage failed')
    by_index = {s['segment']: s for s in segments}
    outer_length_lower = Q(0)
    outer_height_upper = Q(0)
    rows = []
    radius = q(pref['norm_upper'])
    check(radius > 0, 'Invalid prefix radius bound')
    radius2 = radius*radius
    # Profiles run inner->outer.  Thus traverse j=8,...,0 from the cut inward.
    for j in range(8, -1, -1):
        s = by_index[j]
        for key in ('A', 'B', 'AH', 'BH'):
            # A nonnegative integral may have a tiny negative outward lower
            # endpoint.  Keep that valid endpoint rather than rejecting it.
            check(len(s[key]) == 2 and q(s[key][0]) <= q(s[key][1]) and q(s[key][1]) >= 0,
                  'Invalid certified integral interval')
        check(q(s['B'][0]) >= 0, 'The chosen alpha-lower product needs nonnegative B lower')
        length_lower = q(s['A'][0])+alo*q(s['B'][0])
        height_upper = q(s['AH'][1])+ahi*q(s['BH'][1])
        r_upper = c-outer_length_lower
        z_upper = Hhi+outer_height_upper+height_upper+V
        bound2 = (r_upper+U)**2+z_upper**2
        check(length_lower > 0 and r_upper > cuff_lower and z_upper > 0, 'Segment ordering/positivity failed')
        check(bound2 < radius2, 'A tail segment is not inside the prefix sphere')
        rows.append(dict(raw_cell=0, raw_segment=j,
                         radial_length_lower=record(length_lower), height_increment_upper=record(height_upper),
                         outer_cumulative_length_lower=record(outer_length_lower),
                         outer_cumulative_height_upper=record(outer_height_upper),
                         planar_radius_upper=record(r_upper+U), absolute_height_upper=record(z_upper),
                         position_norm_squared_upper=record(bound2), squared_sphere_margin=record(radius2-bound2)))
        outer_length_lower += length_lower
        outer_height_upper += height_upper

    # All cells n>=1 have w<=1/49, by the reviewed height proof, including
    # the protected/deep infinite background.  No new integral is required.
    inner_radius_upper = c-outer_length_lower
    inner_width_upper = inner_radius_upper-cuff_lower
    check(inner_width_upper > 0, 'Invalid remaining radial width')
    total_height_upper = outer_height_upper+inner_width_upper/49
    inner_z_upper = Hhi+total_height_upper+V
    inner_bound2 = (inner_radius_upper+U)**2+inner_z_upper**2
    cap_z_upper = Hhi+total_height_upper+cap_height
    cap_bound2 = cuff_upper**2+cap_z_upper**2
    check(inner_bound2 < radius2 and cap_bound2 < radius2, 'Inner tail/collar/caps leave the sphere')
    diameter = 2*radius
    old_diameter = Q(budget['diameter_upper']['exact'])
    check(diameter < old_diameter, 'No strict diameter improvement')
    support = Q(whole['whole_support_lower']['exact'])
    curvature = Q(whole['whole_principal_curvature_upper']['exact'])
    reach = min(support, 1/curvature)
    check(reach == Q(whole['whole_reach_lower_by_R10']['exact']), 'Original absolute reach bound differs')
    held = Q(budget['held_region_diameter_lower']['exact'])
    displacement = Q(budget['hausdorff_hold_lower']['exact'])
    worst = max(rows, key=lambda row: Q(row['position_norm_squared_upper']['exact']))
    out = dict(status='exact-Fraction-position-budget-for-same-R21-M12-map-pending-independent-review',
               scope=__doc__, script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               geometry_sha256=gsha, tail_manifest_sha256=geom['tail_manifest_sha256'], inputs=records,
               cut_height_lower=record(Hlo), cut_height_upper=record(Hhi),
               planar_perturbation_upper=record(U), height_perturbation_upper=record(V),
               exact_alpha_interval=[record(alo), record(ahi)],
               cell_zero_segment_boxes=rows, worst_cell_zero_segment=worst['raw_segment'],
               worst_cell_zero_norm_squared_upper=worst['position_norm_squared_upper'],
               cell_zero_length_lower=record(outer_length_lower), cell_zero_height_upper=record(outer_height_upper),
               complete_background_height_upper=record(total_height_upper),
               inner_tail_and_collar_norm_squared_upper=record(inner_bound2),
               marked_and_unmarked_cap_norm_squared_upper=record(cap_bound2),
               inner_squared_sphere_margin=record(radius2-inner_bound2), cap_squared_sphere_margin=record(radius2-cap_bound2),
               prefix_certified_radius_upper=record(radius), complete_all_phase_ball_radius_upper=record(radius),
               previous_diameter_upper=record(old_diameter), diameter_upper=record(diameter),
               relative_reduction_of_diameter_upper=record(1-diameter/old_diameter),
               unchanged_absolute_reach_lower=record(reach), reach_over_D_lower=record(reach/diameter),
               hausdorff_hold_over_D_lower=record(displacement/diameter), fixed_caps_diameter_over_D_lower=record(held/diameter),
               new_metric_or_curvature_certificate=False, new_geometry_created=False, physical_metric_changed=False,
               new_integrals_evaluated=False, solver_root_backend_calls=0, sampled_positions_used=False,
               README_new_gate_added=False, README_complete=False)
    args.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: out[key] for key in ['status', 'worst_cell_zero_segment', 'diameter_upper',
                                              'reach_over_D_lower', 'hausdorff_hold_over_D_lower']}, allow_nan=False))


if __name__ == '__main__':
    main()
