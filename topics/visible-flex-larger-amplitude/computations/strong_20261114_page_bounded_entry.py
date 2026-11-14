#!/usr/bin/env python3
"""Run the original threaded entry with an owned-arena page-cache I/O option."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import sys
for _k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_k] = '1'
import strong_20261114_disk_page_budget as pages
import root_20261114_threaded_entry as threaded


def main():
    p = argparse.ArgumentParser(add_help=False, description=__doc__)
    p.add_argument('--arena-write-chunk-MiB', type=int, default=32)
    p.add_argument('--arena-page-record', type=Path, required=True)
    own, remaining = p.parse_known_args()
    if own.arena_page_record.exists():
        raise FileExistsError('A new arena page-advice record is required')
    own.arena_page_record.parent.mkdir(parents=True, exist_ok=True)
    finish = pages.install(write_chunk_bytes=own.arena_write_chunk_MiB*1024**2,
        event_file=own.arena_page_record.with_suffix('.jsonl'))
    old = sys.argv
    sys.argv = [old[0], *remaining]
    try:
        threaded.main()
    finally:
        sys.argv = old
        own.arena_page_record.write_text(json.dumps(finish(), indent=2)+'\n')


if __name__ == '__main__':
    main()
