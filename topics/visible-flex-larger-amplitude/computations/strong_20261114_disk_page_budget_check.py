#!/usr/bin/env python3
"""Actually compare original and page-advised disk arenas byte for byte."""
from __future__ import annotations
import os
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import resource
import tempfile
import time
import numpy as np
import root_disk_block_collocation as disk
import strong_20261114_disk_page_budget as pages


def digest(a, order='C'):
    return hashlib.sha256(a.tobytes(order=order)).hexdigest()


def exercise(directory):
    rng = np.random.default_rng(202611140824)
    arena = disk._Arena(directory)
    rows = disk._Rows(arena, (73, 97, 97))
    expected = rng.standard_normal(rows.shape)
    expected[0, 0, 0] = -0.
    for lo in range(0, len(expected), 12):
        rows.write(lo, expected[lo:lo+12])
    # Include an actual overwrite, straddling the original row boundaries.
    replacement = rng.standard_normal((3, 97, 97))
    rows.write(11, replacement)
    expected[11:14] = replacement
    restored = np.concatenate([rows[slice(lo,min(lo+7,len(expected)))]
                               for lo in range(0,len(expected),7)])
    checks = dict(rows_C_bytes_equal=digest(restored)==digest(expected),
                  individual_row_bytes_equal=digest(rows[12])==digest(expected[12]),
                  negative_zero_preserved=np.signbit(restored[0,0,0]).item())
    records = dict(rows_sha256=digest(restored))
    for order in ('C', 'F'):
        value = np.array(rng.standard_normal((132, 499)), order=order)
        ref = arena.save(value, order=order)
        result = arena.load(ref)
        checks[order+'_layout_and_bytes_equal'] = (
            result.strides==value.strides and digest(result,order)==digest(value,order))
        records[order+'_sha256'] = digest(result,order)
    records.update(checks=checks, arena_bytes=arena.size,
                   written=arena.written, read_bytes=arena.read_bytes)
    arena.close()
    return records


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--temporary-parent',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    start=time.monotonic()
    with tempfile.TemporaryDirectory(prefix='owned-arena-byte-check-',dir=a.temporary_parent) as d:
        original=exercise(d)
        finish=pages.install(write_chunk_bytes=1024**2,
            event_file=a.out.with_suffix('.jsonl'))
        advised=exercise(d)
        stats=finish()
    if original!=advised or not all(advised['checks'].values()) or stats['clean_cycles']<2:
        raise ValueError('Page-advised byte storage differs from the original arena')
    result=dict(scope=__doc__,passed=True,actual_original_and_advised_runs=True,
        original=original,advised=advised,page_advice=stats,
        seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        no_physical_equation_or_BVP_evaluated=True)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(passed=True,out=str(a.out),seconds=result['seconds'],
        clean_cycles=stats['clean_cycles'],peak_rss_kib=result['peak_rss_kib'])))


if __name__=='__main__':main()
