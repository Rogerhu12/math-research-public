#!/usr/bin/env python3
"""Enclose the exact inner finite A integral from endpoint/critical values.

For cells 1..tail_start-1, the cap is constant and every uncapped log
slope is C + jump*S(x) - lambda*x. All critical points are enclosed by
an explicit stable quadratic formula. No numerical quadrature is used.
The remaining curvature variation and protected old-radius term have
proved geometric upper bounds. Finite source calibrations stay frozen.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
import db6f_tail_interval_elementary as elementary

I, qbounds = elementary.I, elementary.qbounds


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def pair(x):
    return [float(x.lo), float(x.hi)]


def q(x):
    return Q.from_float(float(x))


def hull(a, b):
    return I(np.minimum(a.lo, b.lo), np.maximum(a.hi, b.hi))


def smooth(x):
    if float(x.lo) == float(x.hi) and float(x.lo) in (0., 1.):
        return I(float(x.lo))
    def at(t):
        return t*t*t*(10+t*(-15+6*t))
    a, b = at(I(x.lo)), at(I(x.hi))
    return I(max(0., float(a.lo)), min(1., float(b.hi)))


def capped_slope(raw, cap_value, log_cap, transition):
    t = (raw-log_cap+transition)/(2*transition)
    if float(t.hi) <= 0:
        return elementary.exp(raw), False
    if float(t.lo) >= 1:
        return I(cap_value), True
    u = I(max(0., float(t.lo)), min(1., float(t.hi)))
    def primitive_j(z):
        return z*z*z*z*z*(7+z*(-14+z*(10-qbounds(Q(5, 2))*z)))
    left = u-primitive_j(u)
    right = qbounds(Q(1, 2))-primitive_j(1-u)
    primitive = left if float(u.hi) <= .5 else right if float(u.lo) >= .5 else hull(left, right)
    log_value = log_cap-transition+2*transition*primitive
    if float(t.lo) < 0:
        log_value = hull(log_value, raw)
    if float(t.hi) > 1:
        log_value = hull(log_value, log_cap)
    return elementary.exp(log_value), False


def critical_nodes(jump, lam):
    peak = jump*qbounds(Q(15, 8))
    if float(jump.hi) <= 0 or float(peak.hi) <= float(lam.lo):
        return [I(0.), I(1.)]
    check(float(jump.lo) > 0 and float(peak.lo) > float(lam.hi),
          'critical-point multiplicity unresolved at binary64 enclosure precision')
    h = (lam/(30*jump)).sqrt()
    check(float(h.lo) > 0 and float(h.hi) < .25, 'critical radical outside the simple-root range')
    root = 2*h/(1+(1-4*h).sqrt())
    check(0 < float(root.lo) <= float(root.hi) < .5, 'critical point not separated')
    return [I(0.), root, 1-root, I(1.)]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint', type=Path, required=True)
    ap.add_argument('--calibrations', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--tail-start', type=int, default=40)
    args = ap.parse_args()
    raw = args.checkpoint.read_bytes()
    record = json.loads(gzip.decompress(raw) if args.checkpoint.suffix == '.gz' else raw)
    response = record.get('response', record)
    cp = response.get('checkpoint', response)
    p = cp['parameters']
    frozen = json.loads(args.calibrations.read_text())
    rows = frozen['constants']
    N = args.tail_start
    check(12 <= N <= 156 and N % 4 == 0, 'tail-start must be a multiple of four, between 12 and 156')
    check(len(rows) == 160 and [v['n'] for v in rows] == list(range(160)), 'finite table index coverage')
    for row in rows:
        check(float.fromhex(row['hex']) == row['value'] and Q(1, 2) <= q(row['value']) <= 2,
              'finite calibration not in the frozen rational box')
    for key, value in frozen['calibrationParameters'].items():
        check(p.get(key) == value, 'fixed calibration parameter mismatch: ' + key)
    check(p['protectCell'] == 160 and p['orientation'] == 1 and p['curvatureBound'] == 6,
          'wrong warp convention')
    check(p['a'] == 2.75 and p['etaPower'] == 1.5 and p['wCut'] == .5 and p['R'] == 64,
          'wrong source exponents or normalization')
    check(p.get('rejoinR20At') is None and p.get('flatOuterThroughCell', -1) < 0,
          'unsupported source modification')
    check(p['capMode'] == 'cut-preserving' and q(p['capTransition']) > 0,
          'unsupported cap definition')
    check(len(p.get('pulseCaps', [])) <= 1 and len(p.get('valleyCaps', [])) <= 1,
          'inner caps must be constant')
    check(0 < q(p['slopeCap']) <= Q(1, 49), 'inner cap bound fails')
    check(Q(1, 200) <= q(p['delta0']) <= Q(1, 160) and
          Q(1, 25) <= q(p['etaRatioAtN0']) <= Q(1, 16), 'source length box fails')
    check(Q(7, 50) < q(p['rCuff']) <= Q(3, 20), 'cuff box fails')
    check(all(q(v) == 0 for v in p.get('valleyControls', [])[10:]), 'unaccounted deep valley control')
    check(1 < q(p['prefixR']) <= 64 and all(1 < q(v) <= 64 for v in p['prefixRByCell']),
          'pulse level box fails')
    check(p['prefixEnd'] == 15 and p['prefixReturnStart'] == 8, 'unreviewed pulse schedule')

    delta0, c0, root12 = I(p['delta0']), I(p['etaRatioAtN0']), I(12).sqrt()
    eta0 = delta0*c0
    half32 = I(1)/(2*I(2).sqrt())
    total_log_length = 6*delta0+6*eta0/(1-half32)
    log_delta0 = elementary.log(delta0)
    log_cap = elementary.log(I(p['slopeCap']))
    transition = I(p['capTransition'])
    log_cut = elementary.log(I(p['wCut']))
    a = qbounds(Q(11, 4))
    aggregate = I(0.)
    output_rows = []
    root_counts = {'zero': 0, 'two': 0}
    for n in range(1, N):
        delta = delta0*qbounds(Q(1, 1 << n))
        if n % 2:
            eta = eta0*qbounds(Q(1, 1 << ((3*n)//2)))/I(2).sqrt()
        else:
            eta = eta0*qbounds(Q(1, 1 << ((3*n)//2)))
        after = 3*delta+6*eta*half32/(1-half32)
        level_r = p['prefixRByCell'][n] if n <= p['prefixEnd'] else p['R']
        log_delta = log_delta0-n*elementary.LOG2
        beta = I(p.get('valleyControls', [])[n] if n < len(p.get('valleyControls', [])) else 0.)
        platform = [log_delta, elementary.log(I(level_r)),
                    2*log_delta-elementary.log(I(rows[n]['value']))+beta,
                    I(0.), log_delta+a*elementary.LOG2]
        descriptions = [(0, 0, eta), (0, 1, eta), (1, 1, delta),
                        (1, 2, eta), (2, 2, delta), (2, 3, eta),
                        (3, 3, delta), (3, 4, eta), (4, 4, eta)]
        off, cell_a = I(0.), I(0.)
        segment_rows = []
        for j, (low, high, length) in enumerate(descriptions):
            jump = I(0.) if low == high else platform[high]-platform[low]
            lam = 7*length/root12
            nodes = critical_nodes(jump, lam)
            root_counts['two' if len(nodes) == 4 else 'zero'] += 1
            values = []
            for x in nodes:
                dist = after+off+length*x
                source_log = (log_cut+7*(total_log_length-dist)/root12
                              -a*elementary.LOG2-(a-1)*n*elementary.LOG2-log_delta0
                              +platform[low]+jump*smooth(x))
                w, cap_tag = capped_slope(source_log, p['slopeCap'], log_cap, transition)
                value = w/(1+w.square()).sqrt()
                values.append((value, cap_tag))
            variation = I(0.)
            for (left, left_tag), (right, right_tag) in zip(values[:-1], values[1:]):
                # The cap is one exact binary constant. Equal fully capped
                # endpoints have exactly zero difference, not two intervals.
                if left_tag and right_tag:
                    continue
                variation = variation+(right-left).abs()
            part = variation/6
            cell_a = cell_a+part
            segment_rows.append({'segment': j, 'criticalPoints': len(nodes)-2, 'A': pair(part)})
            off = off+length
        aggregate = aggregate+cell_a
        output_rows.append({'n': n, 'A': pair(cell_a), 'segments': segment_rows})

    curvature_tail = Q(1600, 1 << (7*N//4))
    protected_old = Q(1, 48000*(1 << 238))
    inner = aggregate+I(0., float(qbounds(curvature_tail+protected_old).hi))
    result = {
        'status': 'rigorous-inner-finite-warp-A-variation-enclosure', 'scope': __doc__,
        'scriptSHA256': sha(__file__), 'elementarySHA256': sha(Path(elementary.__file__)),
        'intervalBackendSHA256': sha(elementary.backend),
        'checkpointSHA256': sha(args.checkpoint), 'calibrationTableSHA256': sha(args.calibrations),
        'cellsIntegratedExactlyByVariation': [1, N-1],
        'criticalPointCounts': root_counts, 'finiteCriticalValueSum': pair(aggregate),
        'remainingCurvatureWidthUpperExact': str(curvature_tail),
        'protectedOldRadiusWidthUpperExact': str(protected_old),
        'innerAInterval': pair(inner), 'innerAIntervalWidthDiagnostic': float(inner.hi-inner.lo),
        'includesCells': [1, 159], 'cellZeroIncluded': False,
        'rows': output_rows,
        'definition': 'Finite binary calibration coefficients; exact analytic delta, eta, source radius and exp/log normalization.',
        'notCertified': ['cell-zero integral', 'global B integral', 'a nonlinear isometric surface', 'README completion'],
    }
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['cellsIntegratedExactlyByVariation', 'criticalPointCounts',
                                           'innerAInterval', 'innerAIntervalWidthDiagnostic']}))


if __name__ == '__main__':
    main()
