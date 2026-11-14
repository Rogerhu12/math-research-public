#!/usr/bin/env python3
"""Combine reviewed finite source integrals into a tight radial alpha box.

The finite geometry coefficients are fixed binary reals. The leftover B
integral uses the exact old-radius width, a uniform raw-slope bound, and
the protected-port loss. Positive expm1 is evaluated by exact Fraction
series so subtracting two radii near the cuff cannot lose the tiny width.
Only the contribution of alpha normalization is transferred to geometry;
other source evaluation/quadrature errors are deliberately not included.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path

import db6f_tail_interval_elementary as elementary

I, qbounds = elementary.I, elementary.qbounds


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def q(x):
    return Q.from_float(float(x))


def pair(value):
    return q(float(value.lo)), q(float(value.hi))


def show(value):
    lo, hi = value
    return [float(qbounds(lo).lo), float(qbounds(hi).hi)]


def positive_expm1(x, degree=12):
    """Rational enclosure for exp(x)-1, for one exact 0 <= x <= 1/64.

    The omitted series starts with x^(degree+1)/(degree+1)!. Every next
    ratio is at most x/(degree+2), which gives the geometric upper tail.
    """
    check(Q(0) <= x <= Q(1, 64), 'expm1 input outside the proved range')
    term, total = Q(1), Q(0)
    for k in range(1, degree+1):
        term *= x/k
        total += term
    omitted = term*x/(degree+1)
    return total, total+omitted/(1-x/(degree+2))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint', type=Path, required=True)
    ap.add_argument('--calibrations', type=Path, required=True)
    ap.add_argument('--cell-zero-A', type=Path, required=True)
    ap.add_argument('--inner-A', type=Path, required=True)
    ap.add_argument('--outer-B', type=Path, required=True)
    ap.add_argument('--numerical-bookkeeping', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    raw = args.checkpoint.read_bytes()
    record = json.loads(gzip.decompress(raw) if args.checkpoint.suffix == '.gz' else raw)
    response = record.get('response', record)
    cp = response.get('checkpoint', response)
    p = cp['parameters']
    frozen = json.loads(args.calibrations.read_text())
    az = json.loads(args.cell_zero_A.read_text())
    ai = json.loads(args.inner_A.read_text())
    bo = json.loads(args.outer_B.read_text())
    numerical = json.loads(args.numerical_bookkeeping.read_text())
    cp_hash, cal_hash = sha(args.checkpoint), sha(args.calibrations)
    for report in [az, ai, bo]:
        check(report['checkpointSHA256'] == cp_hash, 'checkpoint binding mismatch')
        check(report.get('calibrationsSHA256', report.get('calibrationTableSHA256')) == cal_hash,
              'finite calibration binding mismatch')
    check(az.get('finished') is True and bo.get('finished') is True, 'partial quadrature report')
    check(sorted((r['cell'], r['segment'], r['integrand']) for r in az['rows']) ==
          [(0, j, 'A') for j in range(9)], 'cell-zero A coverage mismatch')
    check(sorted((r['cell'], r['segment'], r['integrand']) for r in bo['rows']) ==
          [(n, j, 'B') for n in range(16) for j in range(9)], 'outer B coverage mismatch')
    check(ai['includesCells'] == [1, 159] and ai['cellZeroIncluded'] is False,
          'inner A coverage mismatch')
    check(p['protectCell'] == 160 and p['curvatureBound'] == 6 and p['orientation'] == 1,
          'unreviewed warp convention')
    check(p['a'] == 2.75 and p['etaPower'] == 1.5 and p['wCut'] == .5 and p['R'] == 64,
          'unreviewed source exponents or scale')
    check(p['capMode'] == 'cut-preserving' and q(p['capTransition']) > 0 and
          p.get('flatOuterThroughCell', -1) < 0 and p.get('rejoinR20At') is None,
          'unsupported background modification')
    check(len(p.get('warpWeightLevels', [])) <= 1 and
          len(p.get('pulseCaps', [])) <= 1 and len(p.get('valleyCaps', [])) <= 1,
          'inner B must have unit weights and constant caps')
    check(0 < q(p['slopeCap']) <= Q(1, 49), 'cap bound fails')
    check(Q(1, 200) <= q(p['delta0']) <= Q(1, 160) and
          Q(1, 25) <= q(p['etaRatioAtN0']) <= Q(1, 16), 'source scale box fails')
    check(Q(7, 50) < q(p['rCuff']) <= Q(3, 20), 'cuff box fails')
    check(all(q(v) == 0 for v in p.get('valleyControls', [])[10:]), 'unaccounted deep controls')
    check(len(frozen['constants']) == 160, 'finite table incomplete')
    for n, row in enumerate(frozen['constants']):
        check(row['n'] == n and float.fromhex(row['hex']) == row['value'] and
              Q(1, 2) <= q(row['value']) <= 2, 'finite calibration box fails')
    for key, value in frozen['calibrationParameters'].items():
        check(p.get(key) == value, 'frozen source parameter changed: '+key)

    delta0, eta0 = I(p['delta0']), I(p['delta0'])*I(p['etaRatioAtN0'])
    ratio, root12 = I(1)/(2*I(2).sqrt()), I(12).sqrt()
    cuff, cut = q(p['rCuff']), q(p['rCut'])

    def radius_excess(n):
        check(n % 2 == 0, 'this ledger uses even source indices')
        d = delta0*qbounds(Q(1, 1 << n))
        eta = eta0*qbounds(Q(1, 1 << (3*n//2)))
        t = (6*d+6*eta/(1-ratio))/root12
        tl, th = pair(t)
        return cuff*positive_expm1(tl)[0], cuff*positive_expm1(th)[1]

    outer, deep = radius_excess(16), radius_excess(160)
    old_width = outer[0]-deep[1], outer[1]-deep[0]
    check(old_width[0] > 0, 'remaining radial interval not positive')
    slope_upper = Q(1280, 1 << 28)
    protected_loss = Q(1, 48000*(1 << 238))
    b_tail = (old_width[0]/(1+slope_upper*slope_upper)-protected_loss, old_width[1])
    check(b_tail[0] > 0, 'remaining B lower bound not positive')
    a0, ainner, bprefix = tuple(map(q, az['totals']['A'])), tuple(map(q, ai['innerAInterval'])), tuple(map(q, bo['totals']['B']))
    atotal = a0[0]+ainner[0], a0[1]+ainner[1]
    btotal = bprefix[0]+b_tail[0], bprefix[1]+b_tail[1]
    width = cut-cuff-deep[1], cut-cuff-deep[0]
    check(width[0] > atotal[1] and btotal[0] > 0, 'positive normalization not established')
    alpha = ((width[0]-atotal[1])/btotal[1], (width[1]-atotal[0])/btotal[0])
    numerical_alpha = q(numerical['stats']['alpha'])
    eps = max(abs(alpha[0]-numerical_alpha), abs(alpha[1]-numerical_alpha))
    radial = btotal[1]*eps
    slope = 24*radial
    metric = (Q(32, 15)+slope)*slope
    result = {
        'status': 'tight-exact-radial-alpha-interval-pending-independent-combination-review',
        'scope': __doc__,
        'inputs': {key: {'file': str(value), 'sha256': sha(value)} for key, value in vars(args).items() if key != 'out'},
        'scriptSHA256': sha(__file__),
        'elementarySHA256': sha(elementary.__file__),
        'intervalBackendSHA256': sha(elementary.backend),
        'finiteSourceDefinition': 'Frozen binary cell coefficients; exact analytic lengths, raw normalization, cap, and warp integrals.',
        'cellZeroA': show(a0), 'innerA': show(ainner), 'outerBCells0Through15': show(bprefix),
        'oldRadiusExcessAtCell16': show(outer), 'oldRadiusExcessAtCell160': show(deep),
        'oldRadiusWidthCells16Through159': show(old_width),
        'tailSlopeUpperExact': str(slope_upper), 'protectedBDeficitUpperExact': str(protected_loss),
        'remainingBCells16Through159': show(b_tail),
        'totalA': show(atotal), 'totalB': show(btotal), 'targetWarpWidth': show(width),
        'exactRadialAlpha': show(alpha),
        'alphaIntervalWidthUpper': float(qbounds(alpha[1]-alpha[0]).hi),
        'savedNumericalAlpha': float(numerical_alpha),
        'savedNumericalAlphaInsideInterval': alpha[0] <= numerical_alpha <= alpha[1],
        'normalizationContributionOnly': {
            'alphaDifferenceUpper': float(qbounds(eps).hi),
            'sameSourceCoordinateRadiusDifferenceUpper': float(qbounds(radial).hi),
            'slopeDifferenceAtCommonPhysicalRadiusUpper': float(qbounds(slope).hi),
            'relativeMetricOperatorDifferenceUpper': float(qbounds(metric).hi),
            'conditions': 'Both backgrounds use the same exact source functions and inner anchor; common physical radius lies in both domains; reviewed |w_r|<24 and |w|<=16/15. Other numerical source, quadrature, interpolation and interface errors are not included.'
        },
        'notCertified': ['numeric source evaluator versus exact elementary functions', 'stored background radial primitives',
                         'nonlinear infinite-tail existence', 'complete surface metric or reach', 'README completion'],
    }
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ['totalA','totalB','exactRadialAlpha','alphaIntervalWidthUpper',
                                                'savedNumericalAlphaInsideInterval','normalizationContributionOnly']}))


if __name__ == '__main__':
    main()
