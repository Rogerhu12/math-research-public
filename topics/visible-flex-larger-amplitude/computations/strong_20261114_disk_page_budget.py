"""Bound clean/dirty page-cache accumulation in the existing temporary arenas.

The original _Arena byte writes, byte reads, allocation, QR arithmetic, and
backward checks are unchanged. After a configurable amount of completed
writing, fdatasync flushes this owned regular file and POSIX_FADV_DONTNEED
advises eviction of its clean cached pages. Completed reads may similarly
release pages; the returned bytes are independent of the kernel cache.
This is an I/O execution option, not a change of mathematical discretization.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import stat
import time
import root_disk_block_collocation as disk

_INSTALLED = False
_STATS = None


def install(*, write_chunk_bytes=32*1024**2, read_advice=True, event_file=None):
    global _INSTALLED, _STATS
    if _INSTALLED:
        raise RuntimeError('Install one explicit arena page-budget adapter per process')
    if not hasattr(os, 'posix_fadvise') or not hasattr(os, 'fdatasync'):
        raise RuntimeError('The explicit page-budget execution option requires fdatasync and posix_fadvise')
    if not isinstance(write_chunk_bytes, int) or not 1024**2 <= write_chunk_bytes <= 128*1024**2:
        raise ValueError('Select a positive temporary write chunk from 1 through 128 MiB')
    original_write, original_read = disk._Arena._write, disk._Arena._read
    original_close = disk._Arena.close
    started = time.monotonic()
    event_file = Path(event_file) if event_file is not None else None
    if event_file is not None:
        event_file.parent.mkdir(parents=True, exist_ok=True)
        if event_file.exists():
            raise FileExistsError('Use a fresh page-advice event file')
    _STATS = dict(scope=__doc__, write_chunk_bytes=write_chunk_bytes,
        read_advice=bool(read_advice), bytes_written=0, bytes_read=0,
        clean_cycles=0, read_advice_calls=0, fdatasync_seconds=0.,
        fdatasync_and_advice_failures=0, regular_arenas_checked=0,
        original_file_bytes_and_all_numerical_operations_retained=True,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

    def event(name, **details):
        row = dict(event=name, seconds=time.monotonic()-started, **details)
        if event_file is not None:
            with event_file.open('a') as stream:
                stream.write(json.dumps(row, allow_nan=False)+'\n')
        if name == 'arena_page_budget_started' or name == 'arena_page_advice_error' or _STATS['clean_cycles'] % 8 == 0:
            print(json.dumps(row, allow_nan=False), flush=True)

    def checked_fd(arena):
        fd = arena.file.fileno()
        if not getattr(arena, '_strong_page_regular_checked', False):
            if not stat.S_ISREG(os.fstat(fd).st_mode):
                raise ValueError('Page-budget advice applies only to the owned regular temporary arena')
            arena._strong_page_regular_checked = True
            _STATS['regular_arenas_checked'] += 1
        return fd

    def advice_error(operation, error):
        # Advice is not a numerical gate: original writes/reads have already
        # completed. An unsupported or failed advice is recorded explicitly.
        _STATS['fdatasync_and_advice_failures'] += 1
        event('arena_page_advice_error', operation=operation, error=repr(error))

    def write(arena, offset, data):
        original_write(arena, offset, data)
        _STATS['bytes_written'] += len(data)
        pending = getattr(arena, '_strong_pending_page_bytes', 0)+len(data)
        arena._strong_pending_page_bytes = pending
        if pending >= write_chunk_bytes:
            try:
                fd = checked_fd(arena)
                start = time.monotonic()
                os.fdatasync(fd)
                _STATS['fdatasync_seconds'] += time.monotonic()-start
                os.posix_fadvise(fd, 0, 0, os.POSIX_FADV_DONTNEED)
                arena._strong_pending_page_bytes = 0
                _STATS['clean_cycles'] += 1
                event('arena_page_clean_cycle', clean_cycles=_STATS['clean_cycles'],
                    completed_write_bytes=pending, arena_reserved_bytes=arena.size,
                    total_bytes_written=_STATS['bytes_written'],
                    fdatasync_seconds=_STATS['fdatasync_seconds'])
            except OSError as error:
                advice_error('fdatasync or clean-page advice', error)

    def read(arena, offset, size):
        value = original_read(arena, offset, size)
        _STATS['bytes_read'] += len(value)
        if read_advice and size:
            try:
                fd = checked_fd(arena)
                os.posix_fadvise(fd, offset, size, os.POSIX_FADV_DONTNEED)
                _STATS['read_advice_calls'] += 1
            except OSError as error:
                advice_error('completed-read clean-page advice', error)
        return value

    disk._Arena._write, disk._Arena._read = write, read
    _INSTALLED = True
    event('arena_page_budget_started', configuration=dict(_STATS))

    def finish():
        # Do not flush an already closed or deleted derived arena, and never
        # reach into a foreign process. Original _Arena.close is unchanged.
        if disk._Arena.close is not original_close:
            raise RuntimeError('The original arena lifetime changed during page advice')
        return {**_STATS, 'seconds': time.monotonic()-started,
                'kernel_eviction_is_advisory_not_guaranteed': True}

    return finish
