"""Map the complete original CSR before the unchanged recursive QR arithmetic.

Every original data/index/indptr byte, including explicit zeros, is first copied
and checked into real preallocated scratch storage.  The original single
eliminate_zeros operation still runs.  Only that CSR instance's prune storage
policy is changed from possibly copying a prefix to retaining the same prefix
view.  The original validations and zero-compaction arithmetic remain intact.

The original BlockQR constructor is compiled with one storage-only callback
between complete interval extraction and recursive QR.  That callback releases
clean mapped CSR pages; it does not remove entries or change any QR statement.
After construction the already checked factor-only mapper stores every original
QR factor.  Both complete matrix and factors remain available to all original
residual, backward-error and refinement operations.

Scratch paths are unique, temporary and never repository artifacts.  Logical
mapped bytes are not claimed as an observed decrease in anonymous RSS.  The
CSR-construction peak still exists; measurements at each release point are
recorded separately from conservative storage bounds.
"""
import gc
import hashlib
import inspect
import json
import mmap
import os
from pathlib import Path
import shutil
import tempfile
import textwrap
import time
from types import MethodType
import weakref

import numpy as np
from scipy.sparse import isspmatrix_csr

from complete_factor_mmap import (BlockQR, CompleteFactorStore, MIB, PAGE,
    _remove_directory, _rounded, backing_upper_bound, collect_and_trim)


def process_memory():
    fields = {line.split(':', 1)[0]: line.split(':', 1)[1].split()
              for line in Path('/proc/self/status').read_text().splitlines()
              if ':' in line}
    meminfo = {line.split(':', 1)[0]: line.split(':', 1)[1].split()
               for line in Path('/proc/meminfo').read_text().splitlines()
               if ':' in line}
    return dict(RSS_bytes=int(fields['VmRSS'][0])*1024,
                RssAnon_bytes=int(fields['RssAnon'][0])*1024,
                RssFile_bytes=int(fields['RssFile'][0])*1024,
                MemAvailable_bytes=int(meminfo['MemAvailable'][0])*1024)


def full_backing_upper_bound(n, m, k):
    factor = backing_upper_bound(n, m, k, 'factor-only')
    csr_padding = 3*(PAGE-1)
    csr_manifest = 8*MIB
    return dict(kind='complete_CSR_before_QR_and_all_factor_arrays_after_QR',
        full_CSR_backing_upper_bytes=factor['full_stored_CSR_bytes'],
        CSR_alignment_padding_upper_bytes=csr_padding,
        CSR_manifest_allowance_bytes=csr_manifest,
        factor_only_bound=factor,
        total_backing_and_manifest_upper_bytes=(factor['full_stored_CSR_bytes']+
            csr_padding+csr_manifest+factor['total_backing_and_manifest_upper_bytes']),
        logical_mapped_bytes_are_not_an_RSS_credit=True)


def _hash_arrays(matrix):
    return {name: hashlib.sha256(memoryview(getattr(matrix, name)).cast('B')).hexdigest()
            for name in ('data', 'indices', 'indptr')}


class CompleteCSRBeforeQRStore:
    def __init__(self, owner, matrix, n, m, k, directory, *,
                 disk_margin_bytes=512*MIB, chunk_bytes=8*MIB,
                 before_factorization=None):
        if not isspmatrix_csr(matrix) or matrix.tocsr() is not matrix:
            raise TypeError('A complete original CSR matrix object is required')
        if (matrix.data.dtype != np.dtype(np.float64) or
                any(getattr(matrix, name).dtype not in (np.dtype(np.int32), np.dtype(np.int64))
                    for name in ('indices', 'indptr'))):
            raise TypeError('Original binary64 CSR with native integer indices is required')
        if disk_margin_bytes < 512*MIB or chunk_bytes < PAGE or chunk_bytes % PAGE:
            raise ValueError('Explicit 512MiB disk margin and page-aligned chunks are required')
        if not hasattr(mmap.mmap, 'madvise') or not hasattr(mmap, 'MADV_DONTNEED'):
            raise MemoryError('Clean mapped-page release is unavailable')
        started = time.monotonic()
        directory = Path(directory).resolve()
        directory.mkdir(parents=True, exist_ok=True)
        layout, offset = [], 0
        for name in ('data', 'indices', 'indptr'):
            array = getattr(matrix, name)
            if not array.flags.c_contiguous:
                raise ValueError('The complete original CSR arrays must be contiguous')
            layout.append(dict(field=name, offset=offset, shape=list(array.shape),
                               dtype=array.dtype.str, nbytes=array.nbytes))
            offset += _rounded(array.nbytes)
        del array
        factor_bound = backing_upper_bound(n, m, k, 'factor-only')
        free = shutil.disk_usage(directory).free
        required = (offset+8*MIB+factor_bound['total_backing_and_manifest_upper_bytes']+
                    disk_margin_bytes)
        if free < required:
            raise MemoryError('Scratch cannot hold complete CSR plus all factors and disk margin')
        self.directory = Path(tempfile.mkdtemp(prefix='complete-qr-csr-', dir=directory))
        self.path = self.directory/'all-arrays.bin'
        self.manifest_path = self.directory/'layout.json'
        self._backing = None
        self._before_factorization = before_factorization
        self._finalizer = weakref.finalize(owner, _remove_directory, str(self.directory))
        self._layout = layout
        self.stats = dict(kind='complete_original_CSR_mapped_before_QR',
            complete_CSR_object_preserved=True, planned_file_bytes=offset,
            logical_array_bytes=sum(row['nbytes'] for row in layout),
            scratch_free_bytes_before_allocation=free,
            required_scratch_bytes_including_all_factor_backing_and_margin=required,
            factor_backing_upper_bound=factor_bound, disk_margin_bytes=disk_margin_bytes,
            chunk_bytes=chunk_bytes, copying_chunks=0, clean_page_release_calls=0,
            clean_page_release_advised_bytes=0, all_copy_chunks_bitwise_checked=True,
            before_mapping=process_memory(), initial_CSR_hashes={},
            original_zero_compactions=0, mapped_arrays_readonly_after_original_prune=False,
            original_QR_arithmetic_changed=False, logical_bytes_are_not_an_RSS_credit=True)
        try:
            descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)
            try:
                os.posix_fallocate(descriptor, 0, offset)
            finally:
                os.close(descriptor)
            self._backing = np.memmap(self.path, dtype=np.uint8, mode='r+', shape=(offset,))
            for row in layout:
                source = getattr(matrix, row['field'])
                flat = source.view(np.uint8)
                digest = hashlib.sha256()
                for first in range(0, row['nbytes'], chunk_bytes):
                    stop = min(row['nbytes'], first+chunk_bytes)
                    lo, hi = row['offset']+first, row['offset']+stop
                    self._backing[lo:hi] = flat[first:stop]
                    if not np.array_equal(self._backing[lo:hi], flat[first:stop]):
                        raise IOError('The complete CSR scratch copy differs bytewise')
                    digest.update(memoryview(flat[first:stop]))
                    self.stats['copying_chunks'] += 1
                    self._backing._mmap.flush(lo, _rounded(hi)-lo)
                    self._discard(lo, _rounded(hi)-lo)
                view = np.ndarray(tuple(row['shape']), dtype=np.dtype(row['dtype']),
                                  buffer=self._backing, offset=row['offset'])
                row['sha256_before_original_zero_compaction'] = digest.hexdigest()
                self.stats['initial_CSR_hashes'][row['field']] = digest.hexdigest()
                setattr(matrix, row['field'], view)
                del source, flat, view
            self.stats['allocator_trim_after_mapping'] = collect_and_trim()
            self.stats['after_mapping'] = process_memory()
            self.stats.update(backing_file=str(self.path), manifest_file=str(self.manifest_path),
                allocated_disk_bytes=self.path.stat().st_blocks*512,
                mapping_seconds=time.monotonic()-started)
            self._write_manifest()
        except OSError as error:
            _remove_directory(self.directory)
            raise MemoryError('Complete CSR scratch storage failed: '+str(error)) from error
        except BaseException:
            _remove_directory(self.directory)
            raise

    def _write_manifest(self):
        self.manifest_path.write_text(json.dumps(dict(scope=__doc__, arrays=self._layout,
            file_bytes=len(self._backing), statistics=self.stats), indent=2)+'\n')

    def _discard(self, offset, length):
        self._backing._mmap.madvise(mmap.MADV_DONTNEED, offset, length)
        self.stats['clean_page_release_calls'] += 1
        self.stats['clean_page_release_advised_bytes'] += length

    def finish_original_prune(self, matrix):
        if self.stats['original_zero_compactions']:
            raise RuntimeError('The original CSR zero compaction must run exactly once')
        for name in ('data', 'indices', 'indptr'):
            array = getattr(matrix, name)
            if not np.shares_memory(array, self._backing):
                raise RuntimeError('Original CSR pruning lost complete mapped storage')
            array.flags.writeable = False
        del array
        self._backing._mmap.flush()
        self._backing.flags.writeable = False
        self.stats['original_zero_compactions'] = 1
        self.stats['mapped_arrays_readonly_after_original_prune'] = True
        self.stats['post_original_zero_compaction_CSR_hashes'] = _hash_arrays(matrix)
        self.stats['post_original_zero_compaction_nnz'] = int(matrix.nnz)
        self._discard(0, len(self._backing))
        self.stats['after_original_zero_compaction_and_page_release'] = process_memory()

    def before_recursive_QR(self, edges, endpoint):
        before = process_memory()
        self._discard(0, len(self._backing))
        trim = collect_and_trim()
        after = process_memory()
        self.stats['before_recursive_QR'] = dict(before_page_release=before,
            after_page_release_and_allocator_trim=after, allocator_trim=trim,
            actual_retained_initial_edge_array_bytes=sum(
                edge.a.nbytes+edge.b.nbytes+edge.c.nbytes for edge in edges),
            actual_retained_endpoint_bytes=endpoint.nbytes,
            complete_mapped_CSR_still_available=True,
            logical_mapped_bytes_not_counted_as_available_RAM=True)
        self._write_manifest()
        if self._before_factorization is not None:
            self._before_factorization(self.stats['before_recursive_QR'])

    def discard_after_solve(self):
        before = process_memory()
        try:
            self._discard(0, len(self._backing))
            released, error = True, None
        except OSError as exception:
            released, error = False, repr(exception)
        self.stats['last_solve_page_release'] = dict(before=before, after=process_memory(),
            clean_mapped_pages_advised_DONTNEED=released, error=error,
            original_solve_return_or_exception_preserved=True)


def _instance_view_prune(matrix, store):
    """Preserve the installed SciPy prune checks and use the same prefix views."""
    original = type(matrix).prune
    original_source = textwrap.dedent(inspect.getsource(original))
    adapted = original_source
    for name in ('indices', 'data'):
        old = '_prune_array(self.'+name+'[:self.nnz])'
        if adapted.count(old) != 1:
            raise RuntimeError('Unsupported original SciPy CSR prune implementation')
        adapted = adapted.replace(old, 'self.'+name+'[:self.nnz]')
    namespace = dict(original.__globals__)
    exec(compile(adapted, '<complete-CSR-storage-only-prune>', 'exec'), namespace)
    view_prune = namespace[original.__name__]
    store.stats['original_SciPy_prune_sha256'] = hashlib.sha256(original_source.encode()).hexdigest()
    store.stats['storage_only_view_prune_sha256'] = hashlib.sha256(adapted.encode()).hexdigest()
    def checked_prune(this):
        view_prune(this)
        store.finish_original_prune(this)
    return MethodType(checked_prune, matrix)


_ORIGINAL_CONSTRUCTOR = textwrap.dedent(inspect.getsource(BlockQR.__init__))
_INSERTION_POINT = '    while len(edges) > 1:\n'
if _ORIGINAL_CONSTRUCTOR.count(_INSERTION_POINT) != 1:
    raise RuntimeError('The original complete BlockQR constructor has changed')
_MAPPED_CONSTRUCTOR = _ORIGINAL_CONSTRUCTOR.replace(_INSERTION_POINT,
    '    self._complete_csr_store.before_recursive_QR(edges, self.endpoint)\n'+_INSERTION_POINT)
_CONSTRUCTOR_NAMESPACE = dict(BlockQR.__init__.__globals__)
exec(compile(_MAPPED_CONSTRUCTOR, '<complete-CSR-page-release-before-original-QR>', 'exec'),
     _CONSTRUCTOR_NAMESPACE)
_CONSTRUCTOR = _CONSTRUCTOR_NAMESPACE['__init__']


class BeforeQRMappedBlockQR(BlockQR):
    def __init__(self, matrix, n, m, k, *, storage_directory,
                 disk_margin_bytes=512*MIB, chunk_bytes=8*MIB,
                 refinement=2, before_factorization=None):
        self._complete_csr_store = CompleteCSRBeforeQRStore(self, matrix, n, m, k,
            storage_directory, disk_margin_bytes=disk_margin_bytes,
            chunk_bytes=chunk_bytes, before_factorization=before_factorization)
        had_prune = 'prune' in matrix.__dict__
        previous_prune = matrix.__dict__.get('prune')
        matrix.prune = _instance_view_prune(matrix, self._complete_csr_store)
        try:
            _CONSTRUCTOR(self, matrix, n, m, k, refinement=refinement)
        finally:
            if had_prune:
                matrix.prune = previous_prune
            else:
                del matrix.prune
        if self.matrix is not matrix:
            raise RuntimeError('The original complete CSR object was replaced')
        self._complete_csr_store.stats.update(
            original_constructor_sha256=hashlib.sha256(_ORIGINAL_CONSTRUCTOR.encode()).hexdigest(),
            storage_callback_constructor_sha256=hashlib.sha256(_MAPPED_CONSTRUCTOR.encode()).hexdigest(),
            original_CSR_instance_prune_restored=True,
            after_original_complete_QR_return=process_memory())
        self._complete_csr_store.discard_after_solve()
        self._complete_store = CompleteFactorStore(self, storage_directory,
            disk_margin_bytes=disk_margin_bytes, chunk_bytes=chunk_bytes, map_scope='factor-only')
        self._complete_csr_store.stats['after_both_complete_stores'] = process_memory()
        self._complete_csr_store._write_manifest()

    def solve(self, rhs):
        try:
            return super().solve(rhs)
        finally:
            self._complete_store.discard_after_solve()
            self._complete_csr_store.discard_after_solve()
