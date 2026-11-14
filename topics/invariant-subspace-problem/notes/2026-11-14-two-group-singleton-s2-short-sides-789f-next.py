"""Exact S2 short-side certificate attempt; no sampling or positivity claim
unless both leading-minor coefficient criteria actually pass.
"""

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    's1_short_frozen', HERE/'2026-11-14-two-group-singleton-s1-short-sides-789f-next.py')
short = importlib.util.module_from_spec(spec)
spec.loader.exec_module(short)
core, emit, CASES = short.core, short.emit, short.CASES


def certify(case, target, uncancelled=False):
    q, pool = CASES[case]
    short.set_parameters(q, pool, short.Z+1, short.V)
    matrix = core.s2_direct_defect(target)
    output = {'case': case, 'target': target,
              'substitution': {'q': str(q.n), 'L': str(pool.n), 'z': '1+Z', 'w': 'V'},
              'minors': []}
    for size in (1, 2):
        minor = (matrix[0][0] if size == 1 else core.cleared_determinant2(matrix)
                 if uncancelled else core.base.determinant_leibniz(matrix))
        certificate = core.base.coefficient_certificate(minor)
        output['minors'].append({'size': size, **certificate})
        emit('short_side_s2_leading_minor', case=case, target=target, size=size, **certificate)
        if not certificate['passed']:
            output['passed'] = False
            return output
    output['passed'] = True
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', choices=tuple(CASES))
    parser.add_argument('--target', choices=('s2-direct', 's2-left', 's2-right'), default='s2-direct')
    parser.add_argument('--uncancelled-determinant', action='store_true')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    if not args.verbose:
        core.emit = lambda *args, **kwargs: None
        core.aggregate.emit = lambda *args, **kwargs: None
    report = {'target': args.target, 'domain': 'R,Z>=0,V>0', 'results': [], 'complete': False}
    for case in ([args.case] if args.case else CASES):
        emit('short_side_s2_start', case=case, target=args.target)
        report['results'].append(certify(case, args.target, args.uncancelled_determinant))
        if args.output:
            args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    report['complete'] = True
    report['all_passed'] = all(item['passed'] for item in report['results'])
    if args.output:
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    emit('short_side_s2_complete', all_passed=report['all_passed'], cases=len(report['results']))


if __name__ == '__main__':
    main()
