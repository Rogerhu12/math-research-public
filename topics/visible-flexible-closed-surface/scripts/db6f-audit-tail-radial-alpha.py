#!/usr/bin/env python3
"""Exact rational ledger proving a positive width-normalizing radial alpha.

The 160 finite source calibration values are frozen binary-real geometry
constants.  The cell-zero integral enclosure is independently reviewed and
replayed before use.  Remaining cells are bounded analytically by variation
and a geometric series, including the protected inner endpoint.
This is not a nonlinear tail or complete-surface existence certificate.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path


APPROVED_CELL0_SCRIPT = '37adea90f144d3550ddfd098dcf8fa08eb30e8b0bab46d28df20efffaf7ab94e'
APPROVED_INTERVAL_BACKEND = 'e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def read_checkpoint(path):
    raw = Path(path).read_bytes()
    record = json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)
    response = record.get('response', record)
    return response.get('checkpoint', response)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint', type=Path, required=True)
    ap.add_argument('--calibrations', type=Path, required=True)
    ap.add_argument('--cell-zero', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    p = read_checkpoint(args.checkpoint)['parameters']
    frozen = json.loads(args.calibrations.read_text())
    cell = json.loads(args.cell_zero.read_text())
    q = lambda x: Q.from_float(float(x))

    require(frozen['status'] == 'frozen-finite-source-geometry-constants', 'wrong finite-constant definition')
    rows = frozen['constants']
    require(len(rows) == 160 and [r['n'] for r in rows] == list(range(160)), 'finite calibration index coverage')
    for row in rows:
        require(float.fromhex(row['hex']) == row['value'], 'hex/binary calibration mismatch')
        require(Q(1, 2) <= q(row['value']) <= 2, 'finite calibration outside the proven slope box')
    for key, value in frozen['calibrationParameters'].items():
        require(p.get(key) == value, 'checkpoint calibration parameter differs: ' + key)

    require(p['protectCell'] == 160 and p['orientation'] == 1, 'incorrect protected-tail convention')
    require(p['curvatureBound'] == 6 and p['a'] == 2.75 and p['etaPower'] == 1.5, 'incorrect fixed exponents')
    require(p['wCut'] == .5 and p['R'] == 64, 'incorrect source port or deep pulse level')
    require(p['capMode'] == 'cut-preserving' and q(p['capTransition']) > 0, 'incorrect cap convention')
    require(p.get('rejoinR20At') is None and p.get('flatOuterThroughCell', -1) < 0, 'unsupported source override')
    require(Q(1, 200) <= q(p['delta0']) <= Q(1, 160), 'delta outside the rational box')
    require(Q(1, 25) <= q(p['etaRatioAtN0']) <= Q(1, 16), 'eta ratio outside the rational box')
    require(Q(7, 50) < q(p['rCuff']) <= Q(3, 20), 'cuff outside the radius box')
    require(q(p['rCut']) > Q(59, 100), 'cut radius insufficient for the width lower bound')
    require(0 < q(p['rCut']) - q(p['rCuff']) < Q(1, 2), 'physical width hypothesis fails')
    require(0 < q(p['slopeCap']) <= Q(1, 49), 'constant inner cap outside the bound')
    require(len(p.get('pulseCaps', [])) <= 1 and len(p.get('valleyCaps', [])) <= 1,
            'later cells must have one common constant cap')
    require(all(q(x) == 0 for x in p.get('valleyControls', [])[10:]), 'deep finite valley controls are not zero')
    require(p['prefixEnd'] == 15 and p['prefixReturnStart'] == 8, 'unreviewed finite pulse schedule')
    require(1 < q(p['prefixR']) <= 64 and all(1 < q(x) <= 64 for x in p['prefixRByCell']),
            'finite pulse levels outside (1,64]')
    weights = p.get('warpWeightLevels', [])
    for row in weights:
        require(len(row) == 5 and row[0] == row[-1] == 1 and all(0 < q(x) <= 3 for x in row),
                'positive weighted radial term or common port condition fails')

    require(cell['checkpointSHA256'] == sha(args.checkpoint), 'cell-zero report uses another checkpoint')
    require(cell['bookkeepingSHA256'] == frozen['bookkeepingSHA256'], 'calibration/source bookkeeping mismatch')
    require(cell['scriptSHA256'] == APPROVED_CELL0_SCRIPT, 'cell-zero implementation requires new independent review')
    require(cell['intervalBackendSHA256'] == APPROVED_INTERVAL_BACKEND, 'interval backend requires new review')
    ca = cell['calibrationAlpha0Interval']
    require(q(ca[0]) <= q(rows[0]['value']) <= q(ca[1]), 'cell-zero calibrated geometry not enclosed')
    a0_upper, a0_lower = q(cell['cell0']['A'][1]), q(cell['cell0']['A'][0])
    b0_lower = q(cell['cell0']['B'][0])
    require(a0_upper < Q(21, 100) and b0_lower > 0, 'cell-zero enclosure does not pay the desired budget')

    # Every inner cell has at most two increasing slope intervals. Thus
    # TV(w/sqrt(1+w^2)) <= 5 M_n. Cells 1..9 use 1/49; from n=10 use
    # W_n=1280*2^(-7n/4). sqrt(2)>7/5 and 2^(-7/4)<1/3 give the sum below.
    slope_sum = Q(9, 49) + Q(75, 7168)
    inner_curvature_part = Q(5, 6) * slope_sum
    # The one protected port contributes at most the entire old radial
    # source thickness, less than cuff/59 <= 3/1180.
    protected_old_part = Q(3, 1180)
    a_upper = a0_upper + inner_curvature_part + protected_old_part
    rounded_a_upper = Q(21, 100) + inner_curvature_part + protected_old_part
    target_lower = Q(43, 100)
    require(a_upper < rounded_a_upper < Q(3, 8) < target_lower, 'exact width comparison failed')
    # B <= 3*(oldCut-cuff)<9/1180 because all positive weights are <=3.
    b_upper = Q(9, 1180)
    alpha_lower = (target_lower - rounded_a_upper) / b_upper
    alpha_upper = (q(p['rCut']) - q(p['rCuff']) - a0_lower) / b0_lower
    require(alpha_lower > 0 and alpha_upper > alpha_lower, 'alpha interval bookkeeping failed')

    source_checked = {}
    repo = Path(__file__).resolve().parents[3]
    for name, expected in frozen['sourceHashes'].items():
        path = Path(name)
        if not path.exists() and '/topics/' in name:
            path = repo / ('topics/' + name.split('/topics/', 1)[1])
        require(path.exists() and sha(path) == expected, 'frozen source hash mismatch: ' + name)
        source_checked[str(path)] = expected

    result = {
        'status': 'exact-positive-radial-normalization-for-frozen-analytic-background',
        'scope': __doc__, 'scriptSHA256': sha(__file__),
        'checkpointSHA256': sha(args.checkpoint), 'calibrationTableSHA256': sha(args.calibrations),
        'cellZeroCertificateSHA256': sha(args.cell_zero), 'sourceHashesChecked': source_checked,
        'finiteCalibrationCount': len(rows), 'finiteCalibrationRangeVerified': ['1/2', '2'],
        'deepFiniteValleyControlsZeroFrom': 10,
        'slopeSumUpperExact': str(slope_sum),
        'innerCurvatureWidthUpperExact': str(inner_curvature_part),
        'protectedOldRadiusWidthUpperExact': str(protected_old_part),
        'cellZeroAUpperExact': str(a0_upper), 'cellZeroBLowerExact': str(b0_lower),
        'minimumWarpWidthUpperExact': str(a_upper),
        'roundedMinimumWarpWidthUpperExact': str(rounded_a_upper),
        'minimumWarpWidthStrictlyBelow': '3/8',
        'targetWidthStrictlyAbove': str(target_lower),
        'positiveExactGlobalRadialAlphaProved': True,
        'exactGlobalAlphaInterval': [str(alpha_lower), str(alpha_upper)],
        'floatingDiagnostics': {'minimumWarpWidthUpper': float(a_upper),
                                'coarseMinimumWarpWidthUpper': float(rounded_a_upper),
                                'alphaLower': float(alpha_lower), 'alphaUpper': float(alpha_upper)},
        'remainingScope': [
            'The finite source table is an exact geometry definition, not an assertion of hidden calibration roots.',
            'oldCut and epsilonScale are exact analytic derived constants, not separately rounded independent inputs.',
            'The original source beyond cell 159 retains its separate reviewed infinite definition.',
            'Positive radial normalization does not certify a nonlinear isometric surface or README completion.'],
    }
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['minimumWarpWidthStrictlyBelow', 'targetWidthStrictlyAbove',
                                           'positiveExactGlobalRadialAlphaProved', 'floatingDiagnostics']}))


if __name__ == '__main__':
    main()
