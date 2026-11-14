#!/usr/bin/env python3
"""Independent Fraction audit of the frozen phase/marker obstruction note.

Only existing metadata and reviewed source/proof identities are read. No
geometry, interval backend, shooting, root solver, or new map is evaluated.
The set-theoretic and differential proofs are reviewed in the companion note;
this small program independently rebuilds the exact numerical applications.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import isfinite, isqrt
from pathlib import Path


TOPIC = Path(__file__).resolve().parent.parent
PINS = {
    'proof_v1': ('notes/2026-11-09-db6f-tail-phase-marker-obstructions.md',
                 'bd3a3b8dd611def263826a5ba9559404d77db2b928648d4f327a896ecf17d1fb'),
    'proof_v2': ('notes/2026-11-09-db6f-tail-phase-marker-obstructions-v2.md',
                 '5766e8ea650b13b8bd32244496db9d67ecd7c223d4eca6d4a67e2c1e84812486'),
    'budget': ('notes/2026-11-09-db6f-root-closed-budget-m12-critical-r01.json',
               '50410a4e57b8a21937dd3a99c25942b36cebd5c5819f1e10982584412ae601a7'),
    'first': ('notes/2026-11-09-db6f-tail-first-flat17-m12-critical-r01.json',
              '5c2ddbfc230416cf7805bf84ea5686ed9db1427c2df2b8f1b3a8379b453e848d'),
    'tail': ('notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',
             'cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'),
    'geometry': ('notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',
                 '253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'),
    'budget_source': ('scripts/db6f-root-closed-budget-v2.py',
                      '0d68b718a43a69b24a865b1932e2700a47190724a3be4ea3f1202b56d1a59641'),
    'common_cut_source': ('scripts/db6f-root-common-cut-v2.py',
                          '317e519fda8d78fb70b53f8a8c80d51599dec1ac46e92741cd9b2576a3f4fa7d'),
    'R16': ('results/R16-fixed-cap-volume-moment-noncongruence.md',
             '278753736f651a82e64bc9d6de61b290395eb3d48390c7b8aef73f939dd565f1'),
    'R17': ('results/R17-exact-finite-visible-closed-geometry.md',
             'd7ad70cfb98d552ce0832555c230b644e49a21cd5cef2ae16a291013ad66e725'),
    'R21': ('results/R21-m12-whole-map-and-actual-metric-decrease.md',
             '3d8e20c610ac322e2f4a7093c44b4b37cde314724136cee489dae73c44497c0c'),
    'R24': ('results/R24-cap-marking-quotient-upper-bound.md',
             '611401f48cd15594ee663b92950d1828e101005de6e4be1d762ef35245940d5e'),
}


def q(value):
    if type(value) not in (int, float) or not isfinite(value):
        raise ValueError('Expected a finite JSON number, not a bool or string')
    return Q(value)


def record(value):
    return {'exact': str(value), 'display_only': float(value)}


def sqrt_box(value):
    """Integer-square-root isolation; no floating-point sqrt is used."""
    assert value > 0
    scale = 10**36
    k = isqrt(value.numerator * scale**2 // value.denominator)
    lo, hi = Q(k, scale), Q(k + 1, scale)
    assert 0 < lo <= hi and lo * lo <= value <= hi * hi
    return lo, hi


def box_record(box):
    return [record(box[0]), record(box[1])]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise ValueError('Refusing to replace a completed report')
    data, inputs = {}, {}
    for key, (filename, expected) in PINS.items():
        raw = (TOPIC / filename).read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        assert actual == expected, key
        inputs[key] = {'file': filename, 'sha256': actual, 'bytes': len(raw)}
        if filename.endswith('.json'):
            data[key] = json.loads(raw)

    budget, first, tail, geometry = [data[k] for k in ('budget', 'first', 'tail', 'geometry')]
    assert budget['script_sha256'] == PINS['budget_source'][1]
    assert budget['inputs']['geometry']['sha256'] == PINS['geometry'][1]
    assert budget['inputs']['tail_first']['sha256'] == PINS['first'][1]
    assert geometry['common_cut_implementation_sha256'] == PINS['common_cut_source'][1]
    assert geometry['tail_manifest_sha256'] == first['manifestSHA256'] == PINS['tail'][1]
    assert geometry['exact_common_cut_C2_by_definition'] is True
    assert geometry['mirror_inlet_C2_exact'] is True
    assert tail['finished'] is True

    V = max(q(first[part]['r0theta0Height']) for part in ('finite', 'collar'))
    assert V == q(first['entireTail']['heightDisplacementUpper'])
    Hlo = Q(budget['tail_height_lower']['exact']) + V
    assert Hlo == Q(7977247853389765, 4503599627370496) > Q(177, 100)
    cuff = q(tail['parameters']['rCuff'])
    assert cuff == q(tail['parameters']['rCut']) - q(tail['parameters']['width'])
    assert cuff == Q(2702159776422297, 18014398509481984) < Q(3, 20)
    diameter_lower = 2 * Hlo
    x0 = cuff / diameter_lower
    assert x0 == Q(2702159776422297, 63817982827118120) < Q(1, 20)

    balanced_square_margin = 1 + 3*x0 + 3*x0*x0 - 625*x0*x0
    assert balanced_square_margin == Q(
        24218466148102856714953454068661,
        2036367466061171636096032216167200) > 0
    target, tau = Q(1, 20), Q(3, 100)
    assert 0 < target <= 2 * tau
    root3 = sqrt_box(Q(3))
    root1597 = sqrt_box(Q(1597))
    balanced_threshold = tuple((3 + x) / 794 for x in root1597)
    assert 397*balanced_threshold[0]**2 - 3*balanced_threshold[0] - 1 <= 0
    assert 397*balanced_threshold[1]**2 - 3*balanced_threshold[1] - 1 >= 0

    polynomial_b = sqrt_box(6*tau*target)
    radial_b = sqrt_box(4*tau*target - target*target)
    assert 6*tau*target == Q(9, 1000)
    assert 4*tau*target - target*target == Q(35, 10000)
    packing = (1 + 2/root3[1], 1 + 2/root3[0])
    polynomial_cuff = (packing[0]*polynomial_b[0], packing[1]*polynomial_b[1])
    radial_cuff = (packing[0]*radial_b[0], packing[1]*radial_b[1])
    assert balanced_threshold[0] > Q('0.0541089')
    assert polynomial_cuff[0] > Q('0.2044128')
    assert radial_cuff[0] > Q('0.1274738')

    original_b, original_h = Q(3, 100), Q(1, 2000)
    exact_center_curvature = 6 * original_h / original_b**2
    assert exact_center_curvature == Q(10, 3)
    original_b_height_bound = original_b**2 / (6*tau*diameter_lower**2)
    assert original_b_height_bound == Q(
        633825300114114700748351602688,
        1590912082860290340700025168880625) < Q(1, 2500)
    current_marker_bound = original_h / diameter_lower
    assert current_marker_bound < Q(1, 7080)

    # Scope check for the corrected table: the old upward-rounded decimal
    # thresholds are larger than the exact roots isolated above.
    assert polynomial_cuff[1] < Q('0.204413')
    assert radial_b[1] < Q('0.059161')
    assert radial_cuff[1] < Q('0.127474')

    report = {
        'status': 'PASS-independent-Fraction-application-and-frozen-source-identity',
        'reviewer': '/root/independent_geometry',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'inputs': inputs,
        'Hc_lower': record(Hlo),
        'actual_cuff': record(cuff),
        'diameter_lower_from_preserved_seam_circles': record(diameter_lower),
        'cylinder_radius_over_new_D_upper': record(x0),
        'balanced_1_over_25_squared_margin': record(balanced_square_margin),
        'necessary_balanced_cylinder_ratio_box': box_record(balanced_threshold),
        'necessary_polynomial_support_ratio_box': box_record(polynomial_b),
        'necessary_polynomial_cuff_ratio_box': box_record(polynomial_cuff),
        'necessary_general_radial_support_ratio_box': box_record(radial_b),
        'necessary_general_radial_cuff_ratio_box': box_record(radial_cuff),
        'original_R16_center_principal_curvature_absolute': record(exact_center_curvature),
        'fixed_original_support_height_over_new_D_upper_under_curvature_gate': record(original_b_height_bound),
        'original_marker_height_over_new_D_upper': record(current_marker_bound),
        'v1_upward_rounded_table_thresholds_are_stronger_than_the_proved_roots': True,
        'v2_is_the_reviewed_text': True,
        'new_geometry_created': False,
        'new_isometry_or_reach_certificate': False,
        'new_background_integrals_evaluated': False,
        'solver_root_flow_backend_calls': 0,
        'README_complete': False,
    }
    with args.out.open('x') as f:
        f.write(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps({'status': report['status'], 'inputs_checked': len(inputs),
                      'strict_balanced_ratio_bound': '1/25',
                      'strict_original_support_ratio_bound': '1/2500',
                      'solver_root_flow_backend_calls': 0}))


if __name__ == '__main__':
    main()
