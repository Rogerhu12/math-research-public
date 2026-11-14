#!/usr/bin/env python3
"""Independent Fraction reconstruction of the frozen R21 position budget.

This fixed-input review never imports the author's calculator and never
evaluates geometry, integrals, a root, or a flow. Existing analytic certificates
remain premises. Display numbers are checked only after exact reconstruction.
"""
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parent.parent
STEM = '2026-11-09-db6f-'
PIN = {
    'author_source': ('scripts/db6f-prefix-m12-segment-ball-budget.py', 'b209f8e1feadf1fb39c9ba4c8173d617728d88532ebe130e92b3914b12066a89'),
    'author': ('notes/'+STEM+'prefix-m12-segment-ball-budget.json', 'f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c'),
    'proof': ('notes/'+STEM+'prefix-m12-segment-ball-proof.md', 'bad275038aa56b96209620cfe91a0154fbb2dad55697c58264ea80b6c3044935'),
    'replay': ('notes/'+STEM+'audit-m12-segment-ball-replay.json', 'f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c'),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise ValueError('Output must be new')
    bindings = {}

    def bind(path, expected):
        path = Path(path)
        if not path.is_absolute():
            path = TOPIC/path
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == expected, str(path)
        bindings[str(path)] = dict(sha256=digest, bytes=len(raw))
        return raw

    fixed = {k: bind(*v) for k, v in PIN.items()}
    report = json.loads(fixed['author'])
    assert fixed['replay'] == fixed['author']
    inputs = {}
    for item in report['inputs']:
        raw = bind(item['file'], item['sha256'])
        assert len(raw) == item['bytes']
        if item['file'].endswith('.json'):
            inputs[Path(item['file']).name] = json.loads(raw)

    def get(stem):
        return inputs[STEM+stem+'.json']

    budget = get('root-closed-budget-m12-critical-r01')
    geometry = get('root-flat17-common-cut-m12-critical-r01')
    prefix = get('root-flat17-common-cut-m12-critical-r01-geometry')
    first = get('tail-first-flat17-m12-critical-r01')
    height = get('tail-background-height-rigorous')
    alpha = get('tail-tight-alpha')
    whole = get('root-whole-metric-reach-m12-critical-r01-lowmetric')
    manifest = json.loads(bind(geometry['tail_manifest'], geometry['tail_manifest_sha256']))
    transfer_info = budget['same_background_transfer']
    transfer = json.loads(bind(transfer_info['file'], transfer_info['sha256']))
    for item in alpha['inputs'].values():
        bind(item['file'], item['sha256'])
    cal = json.loads(bind(alpha['inputs']['calibrations']['file'], alpha['inputs']['calibrations']['sha256']))
    assert height['calibrationAlpha0Interval'] == [cal['constants'][0]['value']]*2
    assert height['checkpointSHA256'] == alpha['inputs']['checkpoint']['sha256']
    assert height['bookkeepingSHA256'] == alpha['inputs']['numerical_bookkeeping']['sha256']
    assert geometry['tail_manifest_sha256'] == first['manifestSHA256'] == whole['tail_manifest_sha256']
    assert transfer_info['new_manifest_sha256'] == geometry['tail_manifest_sha256']
    assert prefix['geometry_sha256'] == report['geometry_sha256'] == whole['geometry_sha256']
    assert prefix['continuous_bounds_certified'] and prefix['entire_finite_prefix_covered']
    assert prefix['first_span'] == 0 and prefix['last_span_exclusive'] == prefix['total_spans']
    assert first['finite']['spans'] == manifest['totalUniqueNodes']-1
    c = Q(manifest['parameters']['rCut'])
    cuff = Q(manifest['parameters']['rCuff'])
    assert c == Q(geometry['frozen_profile']['cut_radius']) == Q(.6)
    assert Q(7, 50) < cuff < Q(3, 20)

    imports = set()
    for node in ast.walk(ast.parse(fixed['author_source'])):
        if isinstance(node, ast.Import):
            imports.update(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.add(node.module)
    assert imports == {'argparse', 'fractions', 'hashlib', 'json', 'math', 'pathlib'}

    U = max(Q(first[k]['r0theta0Planar']) for k in ('finite', 'collar'))
    V = max(Q(first[k]['r0theta0Height']) for k in ('finite', 'collar'))
    Hhi = Q(budget['tail_height_upper']['exact'])-Q(height['wholeHeightUpper'])-V
    Hlo = Q(budget['tail_height_lower']['exact'])+V
    assert Hlo-V > 0 and Hhi >= Hlo
    amin, amax = map(Q, alpha['exactRadialAlpha'])
    assert 0 < amin <= amax
    segments = sorted(height['segments'], key=lambda row: row['segment'])
    assert [row['segment'] for row in segments] == list(range(9))
    lengths = [Q(row['A'][0])+amin*Q(row['B'][0]) for row in segments]
    rises = [Q(row['AH'][1])+amax*Q(row['BH'][1]) for row in segments]
    assert all(Q(row['B'][0]) >= 0 for row in segments)
    assert min(lengths) > 0 and min(rises) >= 0
    R = Q(prefix['norm_upper'])
    assert R == Q(2131902881202937, 1125899906842624)
    comparisons = 0

    def same(actual, expected):
        nonlocal comparisons
        assert Q(actual['exact']) == expected
        assert Q(actual['lower_display']) <= expected <= Q(actual['upper_display'])
        comparisons += 1

    squares = {}
    assert [row['raw_segment'] for row in report['cell_zero_segment_boxes']] == list(range(8, -1, -1))
    for row in report['cell_zero_segment_boxes']:
        j = row['raw_segment']
        assert row['raw_cell'] == 0
        outside_l = sum(lengths[j+1:], Q(0))
        outside_h = sum(rises[j+1:], Q(0))
        radial = c-outside_l+U
        vertical = Hhi+sum(rises[j:], Q(0))+V
        bound = radial**2+vertical**2
        assert radial > cuff and vertical > 0 and bound < R**2
        expected = dict(radial_length_lower=lengths[j], height_increment_upper=rises[j],
                        outer_cumulative_length_lower=outside_l, outer_cumulative_height_upper=outside_h,
                        planar_radius_upper=radial, absolute_height_upper=vertical,
                        position_norm_squared_upper=bound, squared_sphere_margin=R**2-bound)
        for key, value in expected.items():
            same(row[key], value)
        squares[j] = bound

    inside_r = c-sum(lengths, Q(0))
    B = sum(rises, Q(0))+(inside_r-Q(7, 50))/49
    inner = (inside_r+U)**2+(Hhi+B+V)**2
    cap = Q(3, 20)**2+(Hhi+B+Q(1, 2000))**2
    assert inside_r > cuff and max(inner, cap) < R**2
    D = 2*R
    oldD = Q(budget['diameter_upper']['exact'])
    reach = min(Q(whole['whole_support_lower']['exact']), 1/Q(whole['whole_principal_curvature_upper']['exact']))
    assert reach == Q(whole['whole_reach_lower_by_R10']['exact'])
    displacement = Q(budget['hausdorff_hold_lower']['exact'])
    held = Q(budget['held_region_diameter_lower']['exact'])
    scalar = dict(cut_height_lower=Hlo, cut_height_upper=Hhi,
                  planar_perturbation_upper=U, height_perturbation_upper=V,
                  worst_cell_zero_norm_squared_upper=max(squares.values()),
                  cell_zero_length_lower=sum(lengths, Q(0)), cell_zero_height_upper=sum(rises, Q(0)),
                  complete_background_height_upper=B, inner_tail_and_collar_norm_squared_upper=inner,
                  marked_and_unmarked_cap_norm_squared_upper=cap,
                  inner_squared_sphere_margin=R**2-inner, cap_squared_sphere_margin=R**2-cap,
                  prefix_certified_radius_upper=R, complete_all_phase_ball_radius_upper=R,
                  previous_diameter_upper=oldD, diameter_upper=D,
                  relative_reduction_of_diameter_upper=1-D/oldD, unchanged_absolute_reach_lower=reach,
                  reach_over_D_lower=reach/D, hausdorff_hold_over_D_lower=displacement/D,
                  fixed_caps_diameter_over_D_lower=held/D)
    for key, value in scalar.items():
        same(report[key], value)
    for data, value in zip(report['exact_alpha_interval'], (amin, amax)):
        same(data, value)
    assert report['worst_cell_zero_segment'] == max(squares, key=squares.get) == 7
    assert max(squares.values()) < Q('3.564799') and inner < Q('3.420004') and cap < Q('3.348534')
    assert B <= Q('0.05193687255607195') and D < oldD
    assert reach/D == Q(316912650057057350374175801344, 10156379431358714998583735712015)
    assert displacement/D == Q(1800459358092517, 34110446099246992)
    assert reach/D > Q('0.03120330942723168')
    assert displacement/D > Q('0.05278322519892998') and held/D > Q('0.9354609822667627')
    # An independent weaker cross-check already suffices for the inner blocks.
    oldB = Q(height['wholeHeightUpper'])
    assert (inside_r+U)**2+(Hhi+oldB+V)**2 < R**2
    assert cuff**2+(Hhi+oldB+Q(1, 2000))**2 < R**2
    output = dict(status='PASS-independent-fixed-R21-Fraction-position-combination-review',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  frozen_bindings=bindings, frozen_file_count=len(bindings),
                  author_replay_byte_identical=True, exact_record_comparisons=comparisons,
                  complete_nine_segment_squares_checked=True, inner_and_cap_squares_checked=True,
                  true_manifest_cut_and_cuff_checked=True,
                  original_negative_A_lower_count=sum(Q(row['A'][0]) < 0 for row in segments),
                  negative_A_lower_endpoints_preserved=True, all_strict_decimal_claims_checked=True,
                  old_height_weaker_crosscheck_also_sufficient=True,
                  diameter_upper_exact=str(D), reach_over_D_lower_exact=str(reach/D),
                  hold_over_D_lower_exact=str(displacement/D),
                  solver_root_backend_calls=0, new_integrals_evaluated=False,
                  analytic_certificate_rows_replayed=False, new_geometry_created=False, README_complete=False)
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k: output[k] for k in ('status', 'frozen_file_count', 'exact_record_comparisons', 'diameter_upper_exact')}))


if __name__ == '__main__':
    main()
