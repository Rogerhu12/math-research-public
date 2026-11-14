#!/usr/bin/env python3
"""Rebuild the true CM12 T3 support, horizontal Laurent height, and independent audit."""
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

    anchor = data / 'p41_basic_three_SS_CM_anchors47.json.gz'
    support = work / 'p41_CM12_actual_T3_support47.json.gz'
    branches = work / 'p41_CM12_actual_T3_local_branches47.json.gz'
    polynomial = work / 'SS_j44_02_actual_CM_Laurent_F3_polynomial47.json.gz'
    run('p41_CM12_T3_actual_support47.py',
        ['--script-dir', scripts, '--basic-anchors', anchor,
         '--fixed-support', data / 'p41_T3_fixed_divisor47.json.gz', '--output', support])
    run('p41_CM12_T3_local_branches47.py',
        ['--script-dir', scripts, '--support', support, '--basic-anchors', anchor,
         '--output', branches])
    common = ['--script-dir', scripts, '--branches', branches,
              '--reference-connections', data / 'ORD_j39_actual_F3_CM_anchored_connections47.json.gz',
              '--source-connections', data / 'SS_j9_11_actual_F2_connections47.json.gz',
              '--t2-branches', data / 'p41_CM12_actual_T2_ramified_branches47.json.gz',
              '--basic-anchors', anchor,
              '--f2-polynomial', data / 'SS_j44_02_actual_CM_ramified_F2_polynomial47.json.gz',
              '--f2-audit', data / 'SS_j44_02-CM-F2-ramified-independent-audit.json']
    run('p41_CM12_F3_Laurent_polynomial47.py',
        common + ['--work-dir', work / 'unit-fixed-form', '--output', polynomial])
    run('verify_CM12_F3_Laurent47.py',
        common + ['--support', support, '--polynomial', polynomial, '--output',
                  work / 'SS_j44_02-CM-F3-Laurent-independent-audit.json'])


if __name__ == '__main__':
    main()
