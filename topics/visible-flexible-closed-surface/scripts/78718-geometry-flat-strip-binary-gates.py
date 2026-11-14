#!/usr/bin/env python3
"""Exact finite parameter/gate checks for flat-strip-provider-v2; zero PDE runs."""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve()
    proof = here.parent.parent / 'notes' / (
        '2026-11-10-78718-geometry-flat-strip-provider-v2.md'
    )
    expected_proof = 'cc26cf6685ec4a26f4c8b612c64d1af598cc4f8e223d6cd2c1b0a87e99af23d4'
    proof_sha = hashlib.sha256(proof.read_bytes()).hexdigest()
    if proof_sha != expected_proof:
        raise RuntimeError('Frozen proof identity differs')
    checks = {
        'epsilon_binary_inside': Q(399, 1000) < Q.from_float(.4) < Q(401, 1000),
        'vu_binary_lower': Q.from_float(.17) > Q(169, 1000),
        'vd_binary_lower': Q.from_float(.18) > Q(179, 1000),
        'delta_binary_range': 0 < Q.from_float(.07254443456654512) < Q(3, 40),
        'qepsilon_lower': Q(399, 1202) > Q(33, 100),
        'qepsilon_upper': Q(401, 1198) < Q(34, 100),
        'width_upper': Q(202, 601) * Q(3, 40) / Q(169, 1000) < Q(3, 20),
        'radius_upper': 1 + Q(67, 100) * Q(3, 40) < Q(53, 50),
        'h_squared_lower': 1 - Q(3, 2000) - Q(20799, 16000000) > Q(99, 100),
        'jacobian_margin': Q(53, 330) < Q(1, 5),
    }
    report = {
        'scope': 'Exact finite binary-parameter and rational full-width gates only.',
        'not_claimed': 'No actual incoming PDE data, embedding/reach, or nonlinear closure validation.',
        'source_sha256': hashlib.sha256(here.read_bytes()).hexdigest(),
        'proof_name': proof.name,
        'proof_sha256': proof_sha,
        'checks': checks,
        'all_pass': all(checks.values()),
        'pde_runs': 0,
    }
    if not report['all_pass']:
        raise AssertionError(checks)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'output': str(args.out),
        'bytes': args.out.stat().st_size,
        'sha256': hashlib.sha256(args.out.read_bytes()).hexdigest(),
        'checks': len(checks), 'all_pass': True, 'pde_runs': 0,
    }))


if __name__ == '__main__':
    main()
