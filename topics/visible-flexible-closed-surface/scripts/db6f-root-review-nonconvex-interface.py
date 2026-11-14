#!/usr/bin/env python3
"""Independent rational rederivation for the closed nonconvex-interface note.

No candidate, optimization, solver, angle grid, RK or flow is used.
The root reviewer separately checks the geometric proofs and cited theorems.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    repo = topic.parents[1]
    prefix = '2026-11-09-db6f-'
    notes = topic / 'notes'

    def locate(path):
        p = Path(path)
        if p.is_absolute():
            return p
        return repo/p if (repo/p).exists() else topic/p

    def bind(p):
        p = p.resolve()
        b = p.read_bytes()
        return dict(path=str(p.relative_to(repo)), bytes=len(b),
                    sha256=hashlib.sha256(b).hexdigest())

    verified = {}

    def verify_rows(obj):
        if isinstance(obj, dict):
            if {'path', 'bytes', 'sha256'} <= obj.keys():
                now = bind(locate(obj['path']))
                assert now['bytes'] == obj['bytes'] and now['sha256'] == obj['sha256']
                verified[now['path']] = now
            for v in obj.values():
                verify_rows(v)
        elif isinstance(obj, list):
            for v in obj:
                verify_rows(v)

    manifest = notes/(prefix+'audit-nonconvex-connector-publication.json')
    assert bind(manifest)['sha256'] == 'e2bd96fe707470720d24f0c92754b22939f0285cbe7b7a9c4f88ffce3f84b34a'
    verify_rows(json.loads(manifest.read_text()))
    source_ledger = notes/(prefix+'audit-nonconvex-connector-sources.json')
    verify_rows(json.loads(source_ledger.read_text()))
    note = notes/(prefix+'audit-nonconvex-connector-interface.md')
    assert bind(note)['sha256'] == '78b5d369810d4c37898a4f7d80def5d5a169a3921bdde823edded0c22840ed6e'
    source = json.loads((notes/(prefix+'audit-poisson-twin-marker-bounds.json')).read_text())

    def q(v):
        return F(int(v['numerator']), int(v['denominator']))

    def eq(value, encoded):
        assert value == q(encoded)
        return True

    hmin_l = q(source['source_bounds']['hmin_lower'])
    hmin_u = q(source['source_bounds']['hmin_upper'])
    H_l = q(source['source_bounds']['H_lower'])
    H_u = q(source['source_bounds']['H_upper'])
    L_u = q(source['witness_and_enclosures']['L0_upper'])
    D_l = q(source['witness_and_enclosures']['D0_after_error_lower'])
    z, band, rad, eps, chi = F(3, 10), F(1, 100), F(1, 10), F(1, 200), F(1, 100)
    RA, RC = F(6, 5), F(4, 3)
    assert H_u**2+band**2 < RA**2
    assert H_u**2+z**2 < (RC-rad)**2
    assert H_l > 1 and L_u < F(5, 2)

    cones = json.loads((notes/(prefix+'audit-nonconvex-connector-cones.json')).read_text())
    # Reconstruct support separation directly from the two projected centers.
    ax_z_lower = (z+band)/F(5, 2)
    axis_active = rad + (z-band)*ax_z_lower - (RA+RC)*chi
    axis_other = 2*z*(ax_z_lower-chi)
    rational_z, rational_x = F(7, 25), F(-24, 25)
    assert rational_z**2+rational_x**2 == 1
    rational_active = rad+(z-band)*rational_z-(RA+RC)*chi
    rational_other = 2*z*(rational_z-chi)
    membership = (-2*rational_x)/F(5, 2)-chi
    span = 2*(z+rad*rational_z)
    assert min(axis_active, axis_other, rational_active, rational_other) > 0
    assert membership > F(1, 2) and 1-chi > F(1, 2)
    assert span == F(82, 125) and span > F(251, 500)
    comparisons = []
    for val, key in [(axis_active, 'support_margin_over_active'),
                     (axis_other, 'support_margin_over_other_marker'),
                     (ax_z_lower, 'v_z_lower')]:
        comparisons.append(eq(val, cones['axis_cones'][key]))
    for val, key in [(rational_active, 'support_margin_over_active'),
                     (rational_other, 'support_margin_over_other_marker'),
                     (membership, 'sphere_point_cap_membership_dot_lower'),
                     (span, 'fixed_point_pair_span')]:
        comparisons.append(eq(val, cones['rational_cones'][key]))
    rho_max = F(1, 10)+F(9, 10)*(1+F(99, 100))/(1-F(99, 100))
    assert rho_max == F(896, 5)
    comparisons.append(eq(1/rho_max, cones['Poisson_initial_angular_curve']['kappa_min']))

    cuff = json.loads((notes/(prefix+'audit-poisson-cuff-budget.json')).read_text())
    nx, nz = F(9, 41), F(40, 41)
    assert nx*nx+nz*nz == 1
    core_minus_ball = nx*(hmin_l+H_l)+nz*(band-z)-rad
    assert core_minus_ball > 0
    # Start from n_x*c+n_z*|z_c| <= n_x*m+n_z*b+eps.
    upper_at_two_fifths = (nx*(hmin_u-F(2, 5))+nz*band+eps)/nz
    required = F(3, 100)*D_l
    maximum_radius = (nx*hmin_u+nz*band+eps-nz*required)/nx
    assert upper_at_two_fifths == F('0.0726599490908')
    assert upper_at_two_fifths < F('0.0745') < required
    assert maximum_radius < F(2, 5)
    for val, key in [(41*core_minus_ball, 'core_minus_all_marker_support_gap_times_41_lower'),
                     (upper_at_two_fifths, 'cuff_height_abs_upper_when_radius_is_two_fifths'),
                     (required, 'reach_required_from_actual_diameter_lower'),
                     (maximum_radius, 'necessary_common_cuff_radius_upper')]:
        comparisons.append(eq(val, cuff[key]))

    replay_pairs = [
        ('audit-nonconvex-connector-cones.json', 'root-review-nonconvex-cones-replay.json'),
        ('audit-poisson-cuff-budget.json', 'root-review-nonconvex-cuff-replay.json')]
    for old, new in replay_pairs:
        p, r = notes/(prefix+old), notes/(prefix+new)
        assert p.read_bytes() == r.read_bytes()
        verified[bind(r)['path']] = bind(r)
    for p in [manifest, source_ledger, Path(__file__).resolve()]:
        b = bind(p)
        verified[b['path']] = b
    report = dict(status='INDEPENDENT_RATIONAL_INTERFACE_CHECK_PASS',
                  reviewed_note=bind(note), exact_field_comparisons=len(comparisons),
                  independent_formulas=True, original_replays_byte_identical=True,
                  bindings=list(sorted(verified.values(), key=lambda r: r['path'])),
                  actual_candidate_solver_or_optimization_calls=0,
                  scope='Conditional support/cuff inequalities only. No closed common-metric family, entire reach lower bound or G5 result.')
    with a.out.open('x') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(json.dumps(dict(status=report['status'], comparisons=len(comparisons),
                          source_count=len(verified), report=bind(a.out))))


if __name__ == '__main__':
    main()
