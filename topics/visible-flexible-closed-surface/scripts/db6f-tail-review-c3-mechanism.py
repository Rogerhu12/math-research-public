#!/usr/bin/env python3
"""Independent exact audit of the conditional C3/current-mechanism budget.

Only immutable text/JSON, integer counting, hashes and Fraction arithmetic.
No author implementation, numerical model, root, flow or backend is imported.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parent.parent
NOTES = TOPIC / 'notes'
PREFIX = '2026-11-09-db6f-'
PINS = {
    'prefix-c3-current-mechanism-interface-v2.md':
        '7497d615d4fb46eeed1b6cc710851d9bca4aa46a040567f1879cf77acd30a356',
    'prefix-c3-current-mechanism-interface-v2-sources.json':
        'd7c6f11a0150e292c4da692e9935ec12d2647ba4725d7175348b8af9fe3c849b',
    'prefix-c3-current-mechanism-interface.md':
        'eec8eab0e2a4979436c0a21f27bccfdc8abdc1281587f8cdda6b1ae6281eb8da',
    'prefix-c3-mechanism-conditional-budget.json':
        '47fda2e36bf60860f94c0f151542cbff465a3ebb28845db617bf80d45f5ef1a1',
    'prefix-c3-finite-bounds.json':
        '2d5e300efe5f7fd33756235ee59e9c64466c5c0b0c441327f9248a8cb5c532fa',
    'root-closed-budget-m12-critical-r01.json':
        '50410a4e57b8a21937dd3a99c25942b36cebd5c5819f1e10982584412ae601a7',
    'prefix-m12-segment-ball-budget.json':
        'f08875b25cc46328e0c04171fdbf7f50b802dac6951381e4fb2c64d5839c483c',
}
AUTHOR_SCRIPT = TOPIC / 'scripts/db6f-prefix-c3-mechanism-conditional-budget.py'
AUTHOR_SHA = 'b98272c2d92406dd3611ae680ebd754b3558268281c47500aea1e6a70b23f527'


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        while True:
            data = handle.read(1 << 20)
            if not data:
                return h.hexdigest()
            h.update(data)


def binding(path):
    p = Path(path).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': digest(p)}


def read(name):
    return json.loads((NOTES / (PREFIX + name)).read_text())


def frac(rec):
    return F(int(rec['numerator']), int(rec['denominator']))


def rational(q):
    q = F(q)
    return {'numerator': str(q.numerator), 'denominator': str(q.denominator)}


def down(q):
    scale = 10**12
    return F(q.numerator * scale // q.denominator, scale)


def independent_kernel(N):
    # Expand |sum_{k=0}^N exp(ik phi)|^4 by FOUR original indices.
    # This does not copy the author's convolution of triangular coefficients.
    counts = Counter(a - b + c - d for a, b, c, d
                     in product(range(N + 1), repeat=4))
    assert sum(counts.values()) == (N + 1)**4
    assert all(counts[j] == counts[-j] for j in counts)
    b = {j: F(counts[j], counts[0]) for j in range(1, 2*N + 1)}
    assert all(0 < v < 1 for v in b.values())
    return counts, b


def check_all(replay):
    seen = {}

    def verify(path, expected, size=None):
        p = Path(path)
        if not p.is_absolute():
            p = TOPIC / p
        b = binding(p)
        assert b['sha256'] == expected, str(p)
        if size is not None:
            assert b['bytes'] == size, str(p)
        seen[str(p.resolve())] = b
        return p

    for name, expected in PINS.items():
        verify(NOTES / (PREFIX + name), expected)
    verify(AUTHOR_SCRIPT, AUTHOR_SHA)
    ledger = read('prefix-c3-current-mechanism-interface-v2-sources.json')
    assert ledger['source_count'] == len(ledger['source_bindings']) == 28
    for b in ledger['source_bindings'] + ledger['previous_version_preserved']:
        verify(b['path'], b['sha256'], b['bytes'])

    old_text = (NOTES / (PREFIX + 'prefix-c3-current-mechanism-interface.md')).read_text()
    new_text = (NOTES / (PREFIX + 'prefix-c3-current-mechanism-interface-v2.md')).read_text()
    old_flat = ('但是要让另加的帽保持逐点固定，cuff 处必须是轴对称圆领的**全部 Cartesian 两 jet**，而非只有圆形位置。'
                '现有尾 collar 把扰动及其前两阶径向导数精确降为零，背景也需 $w=w_r=0$；'
                '这些性质才使 (22) 与固定帽 C² 拼接，并使相位在 C² 拓扑连续。'
                '未来新数据仍须支付全圆领与完整闭图的 metric、嵌入及曲率。')
    new_flat = ('但是要让另加的帽保持逐点固定，cuff 处必须是轴对称圆领的**全部 Cartesian 两 jet**，而非只有圆形位置。'
                '对当前平帽接口，现有尾 collar 把扰动及其前两阶径向导数精确降为零，背景还需 $w=w_r=0$；'
                '一般固定轴对称非平帽不必满足这两个零条件。这些性质才使 (22) 与固定帽 C² 拼接，'
                '并使相位在 C² 拓扑连续。未来新数据仍须支付全圆领与完整闭图的 metric、嵌入及曲率。')
    replacements = [
        (old_flat, new_flat),
        ('Q_{CD}=4.419076', 'Q_{CD}\\le4.419076'),
        ('notes/2026-11-09-db6f-prefix-c3-current-mechanism-interface-sources.json',
         'notes/2026-11-09-db6f-prefix-c3-current-mechanism-interface-v2-sources.json'),
    ]
    migrated = old_text
    for before, after in replacements:
        assert migrated.count(before) == 1
        migrated = migrated.replace(before, after)
    assert migrated == new_text

    tree = ast.parse(AUTHOR_SCRIPT.read_text())
    imports = sorted({n.module if isinstance(n, ast.ImportFrom) else alias.name
                      for n in ast.walk(tree)
                      for alias in (n.names if isinstance(n, ast.Import) else [None])
                      if isinstance(n, (ast.Import, ast.ImportFrom))})
    assert imports == ['argparse', 'fractions', 'hashlib', 'json', 'pathlib']

    finite = read('prefix-c3-finite-bounds.json')
    cases = finite['cases']
    assert [(c['Fejer_order'], frac(c['r'])) for c in cases] == [
        (3, F(1, 10)), (4, F(3, 20)), (7, F(3, 20)), (7, F(1, 10))]
    kernels = {n: independent_kernel(n) for n in (3, 4, 7)}
    checks = []
    selected = None
    for case in cases:
        N, r = case['Fejer_order'], frac(case['r'])
        counts, b = kernels[N]
        c0 = F(counts[0], (N+1)**2)
        assert frac(case['normalization_c0']) == c0
        assert len(case['positive_fourier_b']) == 2*N
        assert all(rec['j'] == j and frac(rec) == b[j]
                   for j, rec in enumerate(case['positive_fourier_b'], 1))
        rho_max = r + (1-r)*F((N+1)**4, counts[0])
        delta = sum((4*(1-r)*b[j]/(9*j*j-1)
                     for j in b if j % 2), F(0))
        diameter = 2 + sum((4*(1-r)*b[j]/(9*j*j-1)
                            for j in b if not j % 2), F(0))
        inradius = 1 - sum((2*(1-r)*b[j]/(9*j*j-1) for j in b), F(0))
        q1 = (1-r)*b[1]/4
        for key, value in [('rho_max_exact', rho_max), ('delta_exact', delta),
                           ('diameter_upper_exact', diameter), ('inradius_exact', inradius)]:
            assert frac(case[key]) == value
        assert frac(case['delta']['lower']) == down(delta)
        assert frac(case['diameter_upper']['upper']) == -down(-diameter)
        assert q1 >= F(1, 5) > F.from_float(.124)
        checks.append({'N': N, 'r': rational(r), 'b1': rational(b[1]),
                       'q1': rational(q1), 'all_finite_coefficients_rebuilt': True})
        if (N, r) == (7, F(3, 20)):
            selected = (case, b, rho_max, delta, diameter, q1)
    case, b, rho_max, delta_exact, diameter_exact, q1 = selected
    assert q1 == F(357, 1720) and rho_max == F(8833, 860)
    # At normal phi=pi/3 the rotated support difference is positive.
    cj = {j: 2*(1-F(3, 20))*(-1)**(j+1)*b[j]/(9*j*j-1) for j in b}
    directional_gap = sum((((-1)**j-1)*cj[j]*(-1)**j for j in b), F(0))
    assert directional_gap == delta_exact

    delta, d = down(delta_exact), -down(-diameter_exact)
    assert delta == F('0.462868276536') and d == F('2.112793419185')
    assert delta < delta_exact and diameter_exact < d
    r, eta, a, c, H = F(3,20), F(1,1000), F(1,10), F(3,10), F(11,10)
    R, hmin, D = F(57,40), F(23,40), F(23,10)
    cc, dd, cd = (d+2*eta)**2 + 4*a*a, 4*(c*c+H*H), (R+eta+c)**2+(H+a)**2
    assert dd == F(26,5) and cd == F('4.419076')
    old = read('root-closed-budget-m12-critical-r01.json')
    for bnd in old['inputs'].values():
        verify(bnd['file'], bnd['sha256'])
    ball = read('prefix-m12-segment-ball-budget.json')
    axis = F(old['held_region_diameter_lower']['exact'])
    cutlo = F(ball['cut_height_lower']['exact'])
    assert cutlo == F(7977247853389765, 4503599627370496)
    assert axis == 2*cutlo == F(7977247853389765, 2251799813685248)
    assert cutlo == (F(old['tail_height_lower']['exact'])
                     + F(ball['height_perturbation_upper']['exact']))
    actual = read('root-flat17-common-cut-m12-critical-r01.json')
    assert actual['ell'] == 0 and actual['mirror_inlet_C2_exact'] is True
    held = delta - eta
    margins = {
        'cap_disk_inside_core': hmin-c,
        'central_pairs_below_cap_pair': dd-cc,
        'cross_pairs_below_cap_pair': dd-cd,
        'whole_D_squared': D*D-dd,
        'held_above_one_fifth_whole_D': held-D/5,
        'core_rho_above_three_percent_whole_D_only': r-3*D/100,
        'old_actual_axis_separation_exceeds_new_total_height': axis-2*H,
        'first_support_coefficient_exceeds_current_guard_literal': q1-F(31,250),
        'naive_chart_warp_e_exceeds_one': 8*q1-1,
    }
    assert all(x > 0 for x in margins.values())
    literal_guard_gap = q1-F.from_float(.124)
    assert literal_guard_gap > 0

    author = read('prefix-c3-mechanism-conditional-budget.json')
    replay_path = verify(replay, PINS['prefix-c3-mechanism-conditional-budget.json'])
    assert replay_path.read_bytes() == (NOTES/(PREFIX+'prefix-c3-mechanism-conditional-budget.json')).read_bytes()
    for bnd in author['source_bindings']:
        verify(bnd['path'], bnd['sha256'], bnd['bytes'])
    expected = {
        'core': {'rho_min': r, 'rho_max': rho_max, 'minimum_curvature': 1/rho_max,
                 'rotated_first_support_coefficient': q1, 'support_gap_published_lower': delta,
                 'diameter_published_upper': d, 'centered_radius_upper': R,
                 'centered_inradius_lower': hmin},
        'enclosure_parameters': {'projection_leakage': eta, 'central_half_height': a,
                                 'end_disk_radius': c, 'end_half_height': H},
        'pair_distance_squared_upper': {'central_central': cc, 'disk_disk': dd, 'central_disk': cd},
        'conditional_whole_D_squared_upper': dd,
        'conditional_whole_D_clean_upper': D,
        'conditional_held_lower': held,
        'old_M12_actual_fixed_axis_separation_lower': axis,
        'strict_rational_margins': margins,
    }
    exact_fields = 0

    def compare(observed, expected):
        nonlocal exact_fields
        if isinstance(expected, dict):
            for key, value in expected.items():
                compare(observed[key], value)
        else:
            assert frac(observed) == expected
            assert observed['display_only'] == float(expected)
            exact_fields += 1
    compare(author, expected)
    for key in ['same_as_current_frozen_g_claimed', 'enclosure_realized_by_an_ODE_solution',
                'whole_reach_or_closed_flex_asserted']:
        assert author[key] is False
    assert author['solver_root_RK_geometry_backend_calls'] == 0

    return {
        'status': 'PASS_INDEPENDENT_COUNTS_FRACTION_BINDINGS_AND_V2_DIFF',
        'scope': 'Static interface and conditional whole-map enclosure only; no ODE realization.',
        'script': binding(Path(__file__)),
        'checked_bindings': [seen[k] for k in sorted(seen)],
        'unique_bound_files': len(seen),
        'author_ledger_bindings': 28,
        'v1_to_v2_exact_replacements': 3,
        'author_imports': imports,
        'integer_counting_tuples_by_order': {str(n): (n+1)**4 for n in kernels},
        'four_core_inputs': checks,
        'author_exact_fraction_fields_compared': exact_fields,
        'same_author_replay_bytes': True,
        'support_witness_normal': 'pi/3 after the specified initial pi/3 rotation',
        'exact_binary_0124_guard_gap': rational(literal_guard_gap),
        'old_axis_from_twice_same_M12_cut_lower': rational(axis),
        'independent_strict_margins': {k: rational(v) for k, v in margins.items()},
        'pair_distance_squared_upper': {k: rational(v) for k,v in [('CC',cc),('DD',dd),('CD_upper',cd)]},
        'author_Q_CD_is_upper_constant_not_actual_radius_equality': True,
        'regularity_scope_in_written_review': 'One-sided joint C5 true solution suffices for the local quartic Taylor statement; C2 alone does not.',
        'solver_root_RK_backend_calls': 0,
        'current_metric_or_graph_changed': False,
        'future_candidate_generated': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = check_all(args.replay)
    raw = (json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False)+'\n').encode()
    assert len(raw) < 100000
    with args.out.open('xb') as f:
        f.write(raw)
    args.out.chmod(0o444)
    print(json.dumps({'status': report['status'], 'files': report['unique_bound_files'],
                      'exact_fields': report['author_exact_fraction_fields_compared'],
                      'bytes': len(raw), 'sha256': digest(args.out), 'solver_calls': 0}))


if __name__ == '__main__':
    main()
