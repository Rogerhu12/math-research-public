"""Exact S1 short-side certificates, retaining the true height-one hard top.

The five cases cover min(q,L)=2 after the legal ordinary-group swap and scale
which makes z>=1.  No extrapolation through a negative binomial coefficient is
used: the long side starts at 4; lengths 2 and 3 are separate exact cases.
"""

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    's1_frozen', HERE/'2026-11-14-two-group-singleton-bridge-certificates-789f-next.py')
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
Rat, CTX, emit = core.Rat, core.CTX, core.emit
Q, R, Z, U, V = map(Rat, CTX.gens())
CASES = {
    '2-2': (Rat(2), Rat(2)),
    '2-3': (Rat(2), Rat(3)),
    '3-2': (Rat(3), Rat(2)),
    '2-long': (Rat(2), R+4),
    'long-2': (R+4, Rat(2)),
}


def set_parameters(q, pool, z, w):
    core.gram.cache_clear()
    core.polynomial_gram.cache_clear()
    core.q, core.pool, core.z, core.w = q, pool, z, w


def check_hard_top():
    set_parameters(*map(Rat, (2, 2, 4, 9)))
    h0, h1 = core.gram(2, 0), core.gram(2, 1)
    l2, l3 = core.gram(1, 2), core.gram(1, 3)
    hi0, hi1, li3 = map(core.inverse2, (h0, h1, l3))
    bridge = [[Rat(6), Rat(8)], [Rat(), Rat(3)]]
    bt = core.transpose(bridge)
    delta = core.scale(core.add(core.multiply(hi1, bt, l3),
                                core.multiply(hi0, bt, l2), -1), Rat(1)/2)
    # The old upper height is exactly one. C2=0; there is no upper H2 inverse.
    defect = core.add(core.multiply(hi1, h0, hi1),
                      core.multiply(delta, li3, core.transpose(delta)), -1)
    physical = core.multiply(h0, defect, h0)
    direct = core.s1_direct_defect()
    assert all(not (physical[i][j]-direct[i][j]) for i in range(2) for j in range(2))
    emit('short_side_hard_top_check_passed', old_upper_height=1, C2_zero=True)


def certify(case):
    q, pool = CASES[case]
    set_parameters(q, pool, Z+1, V)
    matrix = core.s1_direct_defect()
    output = {'case': case, 'substitution': {'q': str(q.n), 'L': str(pool.n),
                                            'z': '1+Z', 'w': 'V'}, 'minors': []}
    for size in (1, 2):
        minor = matrix[0][0] if size == 1 else core.base.determinant_leibniz(matrix)
        certificate = core.base.coefficient_certificate(minor)
        output['minors'].append({'size': size, **certificate})
        emit('short_side_s1_leading_minor', case=case, size=size, **certificate)
        if not certificate['passed']:
            output['passed'] = False
            return output
    output['passed'] = True
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', choices=tuple(CASES))
    parser.add_argument('--check-hard-top', action='store_true')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    if not args.verbose:
        core.emit = lambda *args, **kwargs: None
        core.aggregate.emit = lambda *args, **kwargs: None
    if args.check_hard_top:
        check_hard_top()
        return
    results = [certify(case) for case in ([args.case] if args.case else CASES)]
    report = {'target': 'actual upper birth-two S1, min(q,L)=2',
              'domain': 'R,Z>=0,V>0', 'results': results,
              'all_passed': all(item['passed'] for item in results)}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    emit('short_side_s1_complete', all_passed=report['all_passed'], cases=len(results))


if __name__ == '__main__':
    main()
