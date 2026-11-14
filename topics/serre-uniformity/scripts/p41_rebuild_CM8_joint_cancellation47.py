#!/usr/bin/env python3
"""Rebuild the two genuine CM(-8) level branches and full-precision joint unit.

This only composes the executed algebraic support, formal unit, chart and
independent-audit programs. It does not start a scalar chain or assign heights.
"""
import argparse
import gzip
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ['script-dir', 'source-dir', 'work-dir', 'output-dir']:
        ap.add_argument('--'+key, type=Path, required=True)
    args = ap.parse_args()
    src = args.source_dir.resolve()
    scripts = args.script_dir.resolve()
    work = args.work_dir.resolve()
    out = args.output_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')

    def run(source, *argv):
        subprocess.run([sys.executable, str(src/source), *map(str, argv)], env=env, check=True)

    supports = []
    for suffix in ['06', '18']:
        disk = 'SS_j10_'+suffix
        path = out/(disk+'_actual_T2_diagonal_support47.json.gz')
        run('p41_selected_SS_T2_diagonal_support47.py',
            '--script-dir', scripts, '--work-dir', work/disk,
            '--disk-id', disk, '--output', path)
        supports.append(path)
    support_data = [json.loads(gzip.decompress(p.read_bytes())) for p in supports]
    j = support_data[0]['actual_source_j_mod47four']
    assert j == support_data[1]['actual_source_j_mod47four']
    unit = out/'p41_CM8_horizontal_j_unit47.json.gz'
    geometry = out/'p41_CM8_actual_joint_norm_cancellation47.json.gz'
    run('p41_CM8_horizontal_unit47.py', '--j', j, '--output', unit)
    run('p41_CM8_diagonal_cancellation47.py',
        '--script-dir', scripts, '--work-dir', work/'chart',
        '--support06', supports[0], '--support18', supports[1],
        '--horizontal-unit', unit, '--output', geometry)
    run('verify_CM8_joint_cancellation47.py',
        '--geometry', geometry, '--unit', unit,
        '--support06', supports[0], '--support18', supports[1],
        '--cm-source', scripts/'data'/'p41_cm_quadratic_jets47_raw.json.gz',
        '--output', out/'p41_CM8_joint_cancellation_independent47.json')


if __name__ == '__main__':
    main()
