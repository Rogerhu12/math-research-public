#!/usr/bin/env python3
"""Checkpoint the actual half-period root grid in independent processes."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

WORKER = Path('scripts/fourfold_phase_root_finite_grid_v2.py')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    with gzip.open(path, 'rt') as f:
        return json.load(f)


def save(path, value):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2)+'\n')
    temporary.replace(path)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--grid', type=int, default=4096)
    p.add_argument('--chunk', type=int, default=256)
    p.add_argument('--directory', type=Path, default=Path('data/root_finite_grid/grid4096_h1e9'))
    a = p.parse_args()
    if a.grid % 2 or a.chunk < 1:
        raise ValueError('even grid and positive chunk required')
    a.directory.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    report = dict(kind='actual_root_half_period_grid_checkpoint', complete=False,
        source_sha256=sha(__file__), worker_path=str(WORKER), worker_sha256=sha(WORKER),
        grid=a.grid, exact_requested_index_interval=[0, a.grid//2+1], chunks=[],
        full_Fourier_coefficients_claimed=False, full_physical_columns_claimed=False,
        reflection_extension_still_requires_the_exact_root_parity=True)
    manifest = a.directory/'manifest.json'
    save(manifest, report)
    identity = None
    for first in range(0, a.grid//2+1, a.chunk):
        last = min(first+a.chunk, a.grid//2+1)
        out = a.directory/('nodes_%05d_%05d.json.gz' % (first, last))
        log = a.directory/('nodes_%05d_%05d.log' % (first, last))
        if not out.exists() or not read(out).get('complete'):
            command = [sys.executable, '-u', str(WORKER), '--grid', str(a.grid),
                       '--first', str(first), '--last', str(last), '--out', str(out)]
            with log.open('w') as f:
                child = subprocess.run(command, stdout=f, stderr=subprocess.STDOUT,
                    env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                             OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1'))
            if child.returncode:
                report.update(failure=dict(first=first, last=last, returncode=child.returncode,
                    log_path=str(log), log_sha256=sha(log)), wall_seconds=time.monotonic()-start)
                save(manifest, report)
                print(log.read_text()[-3000:], flush=True)
                return 2
        row = read(out)
        if (not row['complete'] or row['source_sha256'] != sha(WORKER)
                or row['grid'] != a.grid or row['primitive_nodes'] != 512 or row['bits'] != 256
                or row['requested_indices'] != list(range(first, last))
                or [r['index'] for r in row['rows']] != list(range(first, last))):
            raise ValueError('completed exact grid chunk differs from the requested arithmetic')
        current = dict(identity=row['identity'], root_certificate_sha256=row['root_certificate_sha256'],
                       complex_root_sha256=row['complex_root_sha256'],
                       refined_family_root=row['refined_family_root'], dependencies=row['dependencies'])
        if identity is None:
            identity = current
        elif identity != current:
            raise ValueError('actual root grid chunks do not share one mathematical identity')
        for name, digest in row['dependencies'].items():
            if sha(Path('scripts')/name) != digest:
                raise ValueError('completed root grid dependency changed: '+name)
        report['chunks'].append(dict(path=str(out), sha256=sha(out), bytes=out.stat().st_size,
                                     exact_index_interval=[first, last]))
        report.update(identity=identity, completed_nodes=last, wall_seconds=time.monotonic()-start)
        save(manifest, report)
        print(dict(completed_nodes=last, requested_nodes=a.grid//2+1,
                   wall_seconds=report['wall_seconds']), flush=True)
    report.update(complete=True, wall_seconds=time.monotonic()-start)
    save(manifest, report)
    print(dict(complete=True, requested_actual_nodes=a.grid//2+1,
               manifest=str(manifest), sha256=sha(manifest)), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
