#!/usr/bin/env python3
"""Independent Fraction-only twin-marker budget; no author arithmetic import."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

T = Path(__file__).resolve().parent.parent
N = T/'notes'
P = '2026-11-09-db6f-'
SOURCE = N/(P+'prefix-c3-poisson-bounds.json')
AUTHOR = N/(P+'audit-poisson-twin-marker-bounds.json')
REPLAY = N/(P+'tail-review-poisson-twin-marker-replay.json')
PINS = {
    SOURCE: '4d84a5f3533f367fc8acfb2501c20e16c157e0a41d02f5207e0ea05c3fc0908e',
    AUTHOR: '9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef',
    T/'scripts/db6f-audit-poisson-twin-marker-bounds.py': '9a48b31ee72d74660f4fb2fd584f1851b2aa34cf7091104482a8fa9f9ea5d25c',
    N/(P+'audit-poisson-twin-marker-model.md'): 'bc635aa9f6a76ac6564d734c4f77fda78b34079e777fd5ecf1b86c5ef46d1c5e',
    N/(P+'audit-poisson-twin-marker-publication.json'): '4200d61df1457c41c0a337813c00044c25042d5088cb66c1e52492b0d7d7aeb2',
}


def record(p):
    p = Path(p).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def read(p):
    return json.loads(Path(p).read_text())


def require(cond, reason):
    if not cond:
        raise AssertionError(reason)


def frac(x):
    require(type(x) is dict and set(x) == {'numerator', 'denominator'}, 'Exact fraction schema')
    return Q(int(x['numerator']), int(x['denominator']))


def encode(x):
    if isinstance(x, Q):
        return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, list):
        return [encode(v) for v in x]
    return x


def bisect_root(x):
    """122 exact bisections of [0,4], yielding spacing 2^-120; no isqrt."""
    require(0 <= x <= 16, 'Root bracket')
    lo, hi = Q(0), Q(4)
    for _ in range(122):
        mid = (lo+hi)/2
        if mid*mid <= x:
            lo = mid
        else:
            hi = mid
    if lo*lo == x:
        hi = lo
    require(lo*lo <= x <= hi*hi and hi-lo <= Q(1, 2**120), 'Independent dyadic root box')
    return lo, hi


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--additional-frozen-proof', type=Path)
    ap.add_argument('--additional-proof-sha256')
    args = ap.parse_args()
    require(not args.out.exists(), 'Refuse overwrite')
    bindings = {}
    for p, expected in PINS.items():
        r = record(p)
        require(r['sha256'] == expected, 'Author/source pin '+str(p))
        bindings[r['path']] = r
    if args.additional_frozen_proof is not None:
        r = record(args.additional_frozen_proof)
        require(args.additional_proof_sha256 == r['sha256'], 'Final frozen proof identity')
        bindings[r['path']] = r
    require(AUTHOR.read_bytes() == REPLAY.read_bytes(), 'Actual independent author replay bytes')
    bindings[str(REPLAY)] = record(REPLAY)
    author = read(AUTHOR)
    for entry in author['sources']:
        p = T/entry['path']
        r = record(p)
        require(r['sha256'] == entry['sha256'] and r['bytes'] == entry['bytes'], 'R27/R29 source binding')
        bindings[r['path']] = r
    for entry in read(N/(P+'audit-poisson-twin-marker-publication.json'))['files']:
        r = record(T/entry['path'])
        require(r['sha256'] == entry['sha256'] and r['bytes'] == entry['bytes'], 'Closed author artifact')
        bindings[r['path']] = r
    source = read(SOURCE)
    rows = [r for r in source['cases'] if frac(r['q']) == Q(99,100) and frac(r['r']) == Q(1,10)]
    require(len(rows) == 1, 'Unique frozen Poisson case')
    row = rows[0]
    intervals = {k: (frac(row[k]['lower']), frac(row[k]['upper']))
                 for k in ['inradius', 'delta', 'diameter']}
    # These are the already certified outward decimal endpoints, not float approximations.
    require(intervals == {
        'inradius': (Q('.655688007298'), Q('.655710884848')),
        'delta': (Q('.530966669770'), Q('.530967110151')),
        'diameter': (Q('2.083520966968'), Q('2.083520975612'))}, 'Six frozen source endpoints')
    mlo, mhi = intervals['inradius']
    gaplo, gaphi = intervals['delta']
    dlo, dhi = intervals['diameter']
    Hlo, Hhi = mlo+gaplo, mhi+gaphi
    q, r = Q(99,100), Q(1,10)
    radius = r+(1-r)*(1-q)/(1+q)
    require(radius == Q(104,995) == frac(row['rho_min']), 'Analytic curvature-radius minimum')
    z, b, a = Q(3,10), Q(1,100), Q(1,10)
    e0 = e1 = Q(1,200)
    Z, goal = z+b, Q(251,100)
    Llo = bisect_root((2*Hlo)**2+Z**2)[0]
    Lhi = bisect_root((2*Hhi)**2+Z**2)[1]
    Ulo = bisect_root(dlo**2+Z**2)[0]
    Uhi = bisect_root(dhi**2+Z**2)[1]
    corehi = bisect_root(dhi**2+(2*b)**2)[1]
    bothcaps = 2*(z+a)
    Dlo = Llo+a-2*e0
    Dhi = Lhi+a+2*e0
    D1hi = Uhi+a+2*e1
    quotient = (1-D1hi/Dlo)/2
    held = gaplo-e0-e1
    thickness = 10*(Q(9,10)*Dlo-D1hi)
    expected_sources = {
        'hmin_lower': mlo, 'hmin_upper': mhi,
        'Delta_lower': gaplo, 'Delta_upper': gaphi,
        'diameter_lower': dlo, 'diameter_upper': dhi,
        'H_lower': Hlo, 'H_upper': Hhi,
        'origin_radius_equals_H_by_support_extremum': True, 'rho_min': radius}
    expected_witnesses = {
        'L0_lower': Llo, 'L0_upper': Lhi, 'U1_lower': Ulo, 'U1_upper': Uhi,
        'initial_unperturbed_diameter_equals_L0_plus_a': True,
        'final_diameter_cases': {'core_core_upper': corehi,
                               'all_marker_pairs_upper': bothcaps,
                               'core_marker_upper': Uhi+a},
        'all_final_cases_bounded_by_U1_plus_a': True,
        'D0_after_error_lower': Dlo, 'D0_after_error_upper': Dhi,
        'D1_after_error_upper': D1hi,
        'strict_rigid_thickness_margin': thickness,
        'rigid_quotient_ratio_lower': quotient,
        'held_model_equals_Delta': True,
        'held_after_error_lower': held, 'held_ratio_after_error_lower': held/Dhi,
        'marker_support_upper_in_unshadowed_min_directions': a-Hlo/2,
        'strict_marker_nonshadowing_margin': mlo+Hlo/2-a,
        'fixed_cap_pair_diameter_lower': 2*z}
    require(encode(expected_sources) == author['source_bounds'], 'All independently reconstructed source bounds')
    require(encode(expected_witnesses) == author['witness_and_enclosures'], 'All independent diameter/support/error ratios')
    expected_model = {'z': z, 'core_halfheight': b, 'marker_radius': a,
                      'epsilon0': e0, 'epsilon1': e1, 'Dstar': goal}
    require(encode(expected_model) == author['model_parameters'], 'Frozen model parameters')
    required_radius = 3*goal/100
    expected_local = {'README_reach_target_at_Dstar': required_radius,
                      'core_curvature_radius_lower': radius, 'fixed_marker_curvature_radius': a,
                      'marker_core_vertical_separation_lower': z-a-b,
                      'marker_marker_vertical_separation_lower': 2*z-2*a,
                      'global_closed_surface_reach_claimed': False,
                      'Hausdorff_error_preserves_curvature_claimed': False,
                      'fixed_material_H_requires_actual_retention_of_both_caps': True}
    require(encode(expected_local) == author['local_compatibility_only'], 'Local-only scope and budgets')

    tests = {
        'other_initial_pairs_strictly_smaller': max(corehi,bothcaps)<Llo+a,
        'core_core_below_even_lower_U': corehi<=Ulo,
        'cap_pairs_below_even_lower_U_plus_a': bothcaps<Ulo+a,
        'diameter_lower_positive': Dlo>0,
        'D0_upper_below_2p51': Dhi<goal,
        'gap_equivalent_formula': thickness==9*Llo-10*Uhi-(a+18*e0+20*e1),
        'strict_tenth_diameter_drop': thickness>0,
        'rigid_ratio_exceeds_1over20': quotient>Q(1,20),
        'held_ratio_exceeds_1over5': held/Dhi>Q(1,5),
        'nonshadowing': a-Hlo/2<mlo,
        'fixed_grip_ratio_exceeds_1over5': 2*z/Dhi>Q(1,5),
        'core_and_cap_local_radius_above_threshold': min(radius,a)>required_radius,
        'both_disjoint_component_gaps_above_twice_threshold': min(z-a-b,2*z-2*a)>2*required_radius,
        'connected_model_approximation_obstruction': z-a-b>2*max(e0,e1),
        'display_D_upper_strict': Dhi<Q(author['safe_displays']['D0_after_error_upper']),
        'display_rigid_lower_strict': quotient>Q(author['safe_displays']['rigid_ratio_lower']),
        'display_held_lower_strict': held/Dhi>Q(author['safe_displays']['held_ratio_lower']),
        'display_fixed_grip_lower_strict': 2*z/Dhi>Q(author['safe_displays']['fixed_cap_diameter_ratio_lower']),
    }
    require(all(tests.values()), 'A strict rational gate failed')
    counts = 0
    def count_q(x):
        nonlocal counts
        if isinstance(x,Q): counts+=1
        elif isinstance(x,dict):
            for y in x.values():count_q(y)
    for x in [expected_sources,expected_witnesses,expected_model,expected_local]:count_q(x)
    result = {'status': 'PASS-independent-rational-twin-marker-budget',
              'reviewer': '/root/tail_theory', 'checker': record(__file__),
              'sources': list(sorted(bindings.values(),key=lambda x:x['path'])),
              'independent_author_replay_byte_identical': True,
              'root_enclosures_method': '122 exact rational bisections of [0,4], independently of author integer isqrt; all five used root endpoints agree exactly.',
              'fraction_fields_reconstructed': counts,
              'strict_rational_checks': tests,
              'rigid_ratio_lower': quotient,
              'held_ratio_lower': held/Dhi,
              'fixed_grip_ratio_lower': 2*z/Dhi,
              'any_connected_compact_set_Hausdorff_distance_to_model_at_least': (z-a-b)/2,
              'two_sided_epsilon_005_is_not_a_connected_construction_route': True,
              'scope': 'Disconnected model and separately stated one-sided complete-image hypotheses only. No connected closed surface, common-metric extension, global reach, or actual solver is constructed.',
              'actual_candidate_data_read': False, 'solver_RK_integration_optimization_calls':0}
    with args.out.open('x') as f:
        json.dump(encode(result),f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps({'status':result['status'],'fraction_fields_reconstructed':counts,
                      'strict_checks':len(tests),'report_sha256':record(args.out)['sha256']}))


if __name__ == '__main__':
    main()
