#!/usr/bin/env python3
"""Rebuild the three basic SS CM anchors and the exact ramified CM12 F2 disk."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--work-dir', type=Path, required=True)
    args = ap.parse_args()
    scripts = args.script_dir.resolve()
    data = scripts / 'data'
    work = args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)

    def run(name, arguments):
        subprocess.run([sys.executable, '-u', str(scripts / name)] +
                       [str(x) for x in arguments], check=True)

    anchors = work / 'p41_basic_three_SS_CM_anchors47.json.gz'
    branches = work / 'p41_CM12_actual_T2_ramified_branches47.json.gz'
    polynomial = work / 'SS_j44_02_actual_CM_ramified_F2_polynomial47.json.gz'
    run('p41_basic_three_SS_CM_anchors47.py',
        ['--script-dir', scripts, '--output', anchors])
    run('p41_CM12_T2_ramified_branches47.py',
        ['--script-dir', scripts, '--basic-anchors', anchors, '--output', branches])
    common = ['--script-dir', scripts, '--branches', branches,
              '--reference-connections', data / 'SS_j9_11_actual_F2_connections47.json.gz',
              '--basic-anchors', anchors]
    run('p41_CM12_F2_ramified_polynomial47.py',
        common + ['--work-dir', work / 'moving-RR', '--output', polynomial])
    run('verify_CM12_F2_ramified47.py',
        common + ['--polynomial', polynomial, '--output',
                  work / 'SS_j44_02-CM-F2-ramified-independent-audit.json'])


if __name__ == '__main__':
    main()
