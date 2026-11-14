#!/usr/bin/env python3
"""Bind the actual mesh height samples and check the alpha-only ledger.

This audits source identity and a rational conditional error contribution.
The sampler's numerical quadrature, inversion and rounding remain numeric
diagnostics and are not turned into a certified vertex error.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def locate(path):
    path = Path(path)
    return path if path.exists() else TOPIC/'notes'/path.name


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--samples', type=Path, required=True)
    ap.add_argument('--alpha-replay', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    samples = read(args.samples)
    require(samples['finished'] is True and samples['heightIntervalCertificate'] is False,
            'Unexpected height protocol')
    for name, item in samples['inputs'].items():
        require(sha(locate(item['file'])) == item['sha256'], 'Changed input '+name)
    cp_path = locate(samples['backgroundCheckpoint']['file'])
    require(sha(cp_path) == samples['backgroundCheckpoint']['sha256'], 'Changed background checkpoint')
    cp = read(cp_path)
    cp = cp.get('response', cp)
    cp = cp.get('checkpoint', cp)
    manifest = read(locate(samples['inputs']['manifest']['file']))
    require(cp['parameters'] == manifest['parameters'], 'This actual mesh run differs in a physical or numerical parameter')
    source_paths = {p.name: p for p in [HERE/'closing_recalibrated_tail.mjs', HERE/'closing_weighted_tail.mjs']}
    cache = TOPIC/'repro/source-root/topics/large-amplitude-twist-flex/scripts'
    source_paths.update({p.name: p for p in [cache/'tailnext_balanced_tail.mjs', cache/'general_root_smooth_tail_cells.cjs']})
    for name, digest in samples['sourceSHA256'].items():
        require(sha(source_paths[name]) == digest, 'Changed source '+name)
    require(samples['scriptSHA256'] == sha(HERE/'db6f-tail-sample-background-height.mjs'), 'Changed height sampler')
    require(samples['finiteCalibrationBinaryEqualityCount'] == 160, 'Incomplete calibration check')
    radii = read(locate(samples['inputs']['radii']['file']))['radii']
    rows = samples['rows']
    require(len(rows) == len(radii) and [Q(r['r']) for r in rows] == [Q(r) for r in radii], 'Changed sample order or domain')
    require(len(set(radii)) == len(radii), 'Duplicate query radius')
    p = manifest['parameters']
    require(Q(radii[0]) == Q(p['rCuff']) and Q(radii[-1]) == Q(p['rCut']), 'Missing exact cuff/cut')
    require(rows[-1]['heightFromRToCut'] == 0, 'Relative height does not vanish at cut')
    alpha = read(locate(samples['inputs']['alpha']['file']))
    lo, hi = map(Q, alpha['exactRadialAlpha'])
    representative = Q(alpha['savedNumericalAlpha'])
    require(lo <= representative <= hi and representative == Q(samples['alphaRepresentative']), 'Changed alpha representative')
    gap = max(representative-lo, hi-representative)
    upper = Q(16, 15)*Q(alpha['totalB'][1])*gap
    ledger = read(args.alpha_replay)
    value = ledger['heightDifferenceUpperExact']
    require(upper == Q(int(value['numerator']), int(value['denominator'])) < Q(456, 10**16),
            'Alpha-only rational contribution does not match the reviewed ledger')
    original_ledger = TOPIC/'notes/2026-11-09-db6f-tail-height-alpha-transfer.json'
    require(args.alpha_replay.read_bytes() == original_ledger.read_bytes(), 'Independent scalar replay differs')
    report = dict(status='PASS-actual-height-inputs-and-alpha-only-rational-ledger', scope=__doc__,
        script_sha256=sha(__file__), sample_report=str(args.samples), sample_sha256=sha(args.samples),
        helper_sha256=samples['scriptSHA256'], verified_inputs=samples['inputs'],
        verified_source_sha256=samples['sourceSHA256'], complete_parameter_dict_equality=True,
        matched_parameter_count=len(p), finite_calibration_binary_equality_count=160,
        query_count=len(rows), alpha_ledger_sha256=sha(args.alpha_replay),
        alpha_only_height_upper_exact=str(upper), alpha_only_height_upper_diagnostic=float(upper),
        omitted_deep_height_upper_exact=str(Q(640, 2**280)),
        maximum_inverse_residual_diagnostic=samples['maximumInverseRadiusResidualApprox'],
        maximum_split_height_difference_diagnostic=samples['maximumSplitHeightDifferenceApprox'],
        total_numeric_error_certified=False, fixed_g_convergence_gate_5_paid=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], queries=len(rows), all_parameter_keys=len(p),
                         alpha_only_height_upper=float(upper))))


if __name__ == '__main__':
    main()
