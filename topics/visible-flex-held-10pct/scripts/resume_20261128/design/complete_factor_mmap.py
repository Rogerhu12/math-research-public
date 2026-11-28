"""Scratch-backed complete CSR and original QR factors after construction.

The original complete BlockQR constructor runs first without any numerical
change. Then every selected persistent matrix/factor array is copied, with its exact
dtype, shape, memory order and bytes, into one preallocated scratch file.
Copies are checked in bounded chunks, flushed, and their clean mapped pages
are advised DONTNEED. The complete original solve and residual diagnostics
are inherited unchanged; mapped pages are released again after each solve.

This does not reduce the initial Jacobian/QR construction peak. Mapped clean
pages remain reclaimable storage, not deleted equations or approximate data.
The explicit factor-only mode retains the complete original CSR in anonymous
memory and maps all QR arrays; full mode also maps all three CSR arrays.
The backing file is temporary execution storage and is never a repository
or Release artifact. Its finalizer holds only the unique directory path,
not the factor. No old-array references are retained in the layout record.
"""
import ctypes
import gc
import hashlib
import json
import mmap
import os
from pathlib import Path
import resource
import shutil
import sys
import tempfile
import time
import weakref

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from block_qr_v2 import BlockQR

MIB = 2**20
PAGE = mmap.PAGESIZE


def memory():
    status = {line.split(':')[0]:line.split()[1:] for line in
              Path('/proc/self/status').read_text().splitlines() if ':' in line}
    return dict(current_process_RSS_bytes=int(status['VmRSS'][0])*1024,
                maximum_process_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def backing_upper_bound(n, m, k, map_scope='factor-only'):
    """Full stored CSR, all factors, endpoint arrays and page padding."""
    if min(n, k) < 1 or m < 2 or map_scope not in ('factor-only', 'full'):
        raise ValueError('Complete design dimensions are required')
    total = n*m+k
    nnz = total*(2*n+k)
    index = 4 if max(total, nnz) <= 2**31-1 else 8
    sparse = (8+index)*nnz+index*(total+1)
    factors = (m-2)*(8*(4*n*n+n*k)+12*n)
    endpoint_size = 2*n+k
    endpoint = (8*(n+k)*endpoint_size+16*endpoint_size**2+
                20*endpoint_size)
    arrays = 4*(m-2)+6+(3 if map_scope == 'full' else 0)
    mapped_sparse = sparse if map_scope == 'full' else 0
    padding = arrays*(PAGE-1)
    manifest = max(8*MIB, arrays*512)
    return dict(n=n, nodes=m, parameters=k, map_scope=map_scope,
        full_stored_CSR_bytes=sparse, mapped_CSR_bytes=mapped_sparse,
        complete_CSR_remains_anonymous=map_scope == 'factor-only',
        complete_QR_factor_bytes=factors, endpoint_arrays_bytes=endpoint,
        persistent_arrays=arrays, alignment_padding_upper_bytes=padding,
        manifest_allowance_bytes=manifest,
        total_backing_and_manifest_upper_bytes=mapped_sparse+factors+endpoint+padding+manifest,
        original_QR_zero_elimination_may_reduce_actual_backing=True,
        original_construction_peak_unchanged=True)


def _paths(factor, map_scope):
    if map_scope == 'full':
        for field in ('data', 'indices', 'indptr'):
            yield ('matrix', field)
    for level_index, level in enumerate(factor.levels):
        for item_index, item in enumerate(level):
            if item is not None:
                for field in ('householder', 'tau', 'pivot', 'top'):
                    yield ('levels', level_index, item_index, field)
    for field in ('endpoint', 'reduced', 'row_scale', 'col_scale'):
        yield (field,)
    yield ('final_factor', 0)
    yield ('final_factor', 1)


def _get(factor, path):
    value = factor
    for key in path:
        value = value[key] if isinstance(key, int) else getattr(value, key)
    return value


def _set(factor, path, value):
    if path[0] == 'final_factor':
        current = list(factor.final_factor)
        current[path[1]] = value
        factor.final_factor = tuple(current)
        return
    owner = factor
    for key in path[:-1]:
        owner = owner[key] if isinstance(key, int) else getattr(owner, key)
    setattr(owner, path[-1], value)


def _rounded(size):
    return ((size+PAGE-1)//PAGE)*PAGE


def _remove_directory(directory):
    # Unique mkdtemp ownership; no caller directory is ever recursively removed.
    shutil.rmtree(directory, ignore_errors=True)


def collect_and_trim():
    before = memory()
    collected = gc.collect()
    returned = None
    try:
        function = ctypes.CDLL(None).malloc_trim
        function.argtypes = [ctypes.c_size_t]
        function.restype = ctypes.c_int
        returned = int(function(0))
    except AttributeError:
        pass
    return dict(before=before, after=memory(), cyclic_objects_collected=collected,
                malloc_trim_returned=returned, only_unallocated_allocator_pages_trimmed=True)


class CompleteFactorStore:
    def __init__(self, factor, directory, *, map_scope='factor-only',
                 disk_margin_bytes=512*MIB, chunk_bytes=8*MIB):
        if (disk_margin_bytes < 512*MIB or chunk_bytes < PAGE or chunk_bytes % PAGE
                or map_scope not in ('factor-only', 'full')):
            raise ValueError('At least 512MiB disk margin and page-aligned chunks are required')
        if not hasattr(mmap.mmap, 'madvise') or not hasattr(mmap, 'MADV_DONTNEED'):
            raise MemoryError('This platform lacks the required clean-page release operation')
        started = time.monotonic()
        directory = Path(directory).resolve()
        directory.mkdir(parents=True, exist_ok=True)
        layout, offset = [], 0
        for path in _paths(factor, map_scope):
            array = _get(factor, path)
            if (not isinstance(array, np.ndarray) or array.dtype.hasobject
                    or not (array.flags.c_contiguous or array.flags.f_contiguous)):
                raise ValueError('A persistent original factor array has an unsupported layout')
            order = 'F' if array.flags.f_contiguous and not array.flags.c_contiguous else 'C'
            layout.append(dict(path=list(path), offset=offset, shape=list(array.shape),
                dtype=array.dtype.str, order=order, nbytes=array.nbytes))
            offset += _rounded(array.nbytes)
        del array
        planned = offset
        free = shutil.disk_usage(directory).free
        manifest_allowance = max(8*MIB, len(layout)*512)
        if free < planned+manifest_allowance+disk_margin_bytes:
            raise MemoryError('Scratch space cannot hold the complete factors plus the explicit disk margin')
        self.directory = Path(tempfile.mkdtemp(prefix='complete-qr-', dir=directory))
        self.path = self.directory/'all-arrays.bin'
        self.manifest_path = self.directory/'layout.json'
        self._backing = None
        self._finalizer = weakref.finalize(factor, _remove_directory, str(self.directory))
        self.stats = dict(kind='complete_original_CSR_and_QR_after_factor_return',
            map_scope=map_scope, complete_CSR_remains_anonymous=map_scope == 'factor-only',
            mapped_arrays=len(layout), planned_file_bytes=planned,
            logical_array_bytes=sum(row['nbytes'] for row in layout),
            scratch_free_bytes_before_allocation=free,
            disk_margin_bytes=disk_margin_bytes, manifest_allowance_bytes=manifest_allowance,
            chunk_bytes=chunk_bytes, original_construction_peak_unchanged=True,
            before_mapping=memory(), copying_chunks=0, clean_page_release_calls=0,
            clean_page_release_advised_bytes=0, all_copy_chunks_bitwise_checked=True,
            all_mapped_arrays_readonly=True, original_floating_arithmetic_changed=False)
        try:
            descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)
            try:
                # Reserve real disk blocks up front, not an unbacked sparse promise.
                os.posix_fallocate(descriptor, 0, planned)
            finally:
                os.close(descriptor)
            self._backing = np.memmap(self.path, dtype=np.uint8, mode='r+', shape=(planned,))
            for row in layout:
                path = tuple(row['path'])
                source = _get(factor, path)
                flat = source.ravel(order='K').view(np.uint8)
                digest = hashlib.sha256()
                for first in range(0, row['nbytes'], chunk_bytes):
                    stop = min(row['nbytes'], first+chunk_bytes)
                    lo, hi = row['offset']+first, row['offset']+stop
                    self._backing[lo:hi] = flat[first:stop]
                    if not np.array_equal(self._backing[lo:hi], flat[first:stop]):
                        raise IOError('The complete scratch array copy differs bytewise')
                    digest.update(memoryview(flat[first:stop]))
                    self.stats['copying_chunks'] += 1
                    self._backing._mmap.flush(lo, _rounded(hi)-lo)
                    self._discard(lo, _rounded(hi)-lo)
                mapped = np.ndarray(tuple(row['shape']), dtype=np.dtype(row['dtype']),
                    buffer=self._backing, offset=row['offset'], order=row['order'])
                mapped.flags.writeable = False
                row['sha256'] = digest.hexdigest()
                # Replace the actual CSR/dataclass member. No list retains source.
                _set(factor, path, mapped)
                del source, flat, mapped
            self._backing.flags.writeable = False
            self.manifest_path.write_text(json.dumps(dict(scope=__doc__, map_scope=map_scope, arrays=layout,
                file_bytes=planned, all_copy_chunks_bitwise_checked=True), indent=2)+'\n')
            self.stats.update(backing_file=str(self.path), manifest_file=str(self.manifest_path),
                manifest_sha256=hashlib.sha256(self.manifest_path.read_bytes()).hexdigest(),
                allocated_disk_bytes=self.path.stat().st_blocks*512,
                mapping_seconds=time.monotonic()-started,
                after_mapping_before_allocator_trim=memory())
            self.stats['released_old_anonymous_storage'] = collect_and_trim()
            self.stats['after_mapping_and_allocator_trim'] = memory()
        except OSError as error:
            _remove_directory(self.directory)
            raise MemoryError('Complete factor scratch-storage operation failed: '+str(error)) from error
        except BaseException:
            _remove_directory(self.directory)
            raise

    def _discard(self, offset, length):
        self._backing._mmap.madvise(mmap.MADV_DONTNEED, offset, length)
        self.stats['clean_page_release_calls'] += 1
        self.stats['clean_page_release_advised_bytes'] += length

    def discard_after_solve(self):
        before = memory()
        try:
            self._discard(0, len(self._backing))
            released = True
            error = None
        except OSError as exception:
            # A failed reclamation hint cannot replace the original solve's
            # return or exception. All complete arrays still exist unchanged.
            released = False
            error = repr(exception)
        self.stats['last_solve_page_release'] = dict(before=before, after=memory(),
            clean_mapped_pages_advised_DONTNEED=released, error=error,
            original_solve_return_or_exception_preserved=True)


class MappedBlockQR(BlockQR):
    def __init__(self, matrix, n, m, k, *, storage_directory, disk_margin_bytes=512*MIB,
                 chunk_bytes=8*MIB, refinement=2, map_scope='factor-only'):
        super().__init__(matrix, n, m, k, refinement=refinement)
        self._complete_store = CompleteFactorStore(self, storage_directory,
            disk_margin_bytes=disk_margin_bytes, chunk_bytes=chunk_bytes, map_scope=map_scope)

    def solve(self, rhs):
        try:
            return super().solve(rhs)
        finally:
            self._complete_store.discard_after_solve()
