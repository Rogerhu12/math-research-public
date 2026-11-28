#!/usr/bin/env python3
"""Construct every original collocation CSR entry directly in owned storage.

The original complete node/midpoint dY and dP arrays are inputs; they may be
disk-backed. Every original A/B/P expression and middle-dP in-place update is
retained in its original per-entry order. All stored zeros, endpoint rows and
parameter columns remain. Only final storage allocation and lifetime change.

An explicit adopter hands this same complete CSR object and its checked
backing to the original QR storage protocol, without copying a second CSR.
The original one-time zero compaction, complete-row checks, QR, solve and full
residual diagnostics remain. Scientific gates and true child ownership are
the caller's unchanged responsibility. This module alone runs no BVP.
"""
import argparse
import gc
import hashlib
import inspect
import json
import mmap
import os
from pathlib import Path
import resource
import shutil
import sys
import tempfile
import time
from types import FunctionType
import weakref

import numpy as np
from scipy.integrate import _bvp
from scipy.sparse import csr_matrix, isspmatrix_csr


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import complete_mapped_storage_reclamation_v3 as reclamation

RECLAMATION_SHA = '2dac1ddb506c7065c8f53c29e407b53ca797a298c2cc59dbb274b95cbfdf9f06'
if hashlib.sha256(Path(reclamation.__file__).read_bytes()).hexdigest() != RECLAMATION_SHA:
    raise RuntimeError('The frozen complete mapped-storage helper changed')
mapped, original_storage = reclamation.mapped, reclamation.factor_storage
MIB, PAGE = original_storage.MIB, original_storage.PAGE
OWNER_KIND = 'owned_complete_original_collocation_CSR_assembly_storage'
ROOT_NAME = 'complete-jacobian-storage'
PREFIX = 'complete-jac-csr-'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def storage_bound(n, m, k):
    if n < 1 or m < 2 or k < 0:
        raise ValueError('Complete collocation dimensions are required')
    total, width = n*m+k, 2*n+k
    nnz = total*width
    dtype = np.int32 if max(nnz, total) <= np.iinfo(np.int32).max else np.int64
    item = np.dtype(dtype).itemsize
    sizes = (8*nnz, item*nnz, item*(total+1))
    file_bytes = sum(original_storage._rounded(size) for size in sizes)
    return dict(n=n, nodes=m, parameters=k, rows=total, columns=total,
        complete_stored_width=width, complete_stored_entries=nnz,
        index_dtype=np.dtype(dtype).str,
        complete_logical_CSR_bytes=sum(sizes), preallocated_CSR_file_bytes=file_bytes,
        manifest_and_external_journal_allowance_bytes=16*MIB,
        complete_original_partial_logical_bytes=8*n*(n+k)*(2*m-1),
        second_complete_CSR_copy_required=False,
        logical_storage_bytes_are_not_an_RSS_credit=True)


def owned_storage_root(outdir):
    outdir = Path(outdir).resolve()
    if not outdir.is_dir():
        raise FileNotFoundError('The actual child output directory must already exist')
    directory = outdir/ROOT_NAME
    owner = dict(kind=OWNER_KIND, actual_child_outdir=str(outdir),
        entry_sha256=sha(__file__), temporary_reproducible_execution_storage=True,
        scientific_checkpoint_or_accepted_field=False)
    if not directory.exists():
        directory.mkdir()
        with (directory/'owner.json').open('x') as stream:
            stream.write(json.dumps(owner, indent=2, sort_keys=True)+'\n')
    if directory.is_symlink() or directory.resolve().parent != outdir:
        raise ValueError('The complete CSR assembly root is not the declared owned directory')
    actual = json.loads((directory/'owner.json').read_text())
    if any(actual.get(key) != owner[key] for key in ('kind', 'actual_child_outdir', 'entry_sha256')):
        raise ValueError('The actual complete CSR assembly owner/source differs')
    return directory


class AssembledCSRStore(reclamation._Reclamation, mapped.CompleteCSRBeforeQRStore):
    def __init__(self, n, m, k, directory, *, disk_margin_bytes=512*MIB,
                 chunk_bytes=8*MIB):
        if disk_margin_bytes < 512*MIB or chunk_bytes < PAGE or chunk_bytes % PAGE:
            raise ValueError('Keep the original explicit margin and page-aligned copy/hash chunks')
        if not hasattr(mmap.mmap, 'madvise') or not hasattr(mmap, 'MADV_DONTNEED'):
            raise MemoryError('The required complete mapped-page release is unavailable')
        directory = Path(directory).resolve()
        if not directory.is_dir():
            raise FileNotFoundError('The actual caller must own the assembly-storage root')
        self._setup_reclamation(directory, 'complete_original_CSR_direct_assembly')
        self._bound = storage_bound(n, m, k)
        self.n, self.m, self.k = int(n), int(m), int(k)
        self._chunk_bytes = int(chunk_bytes)
        required = (self._bound['preallocated_CSR_file_bytes']+
                    self._bound['manifest_and_external_journal_allowance_bytes']+disk_margin_bytes)
        free = shutil.disk_usage(directory).free
        if free < required:
            raise MemoryError('Scratch cannot hold the complete original CSR and explicit margin')
        self.directory = Path(tempfile.mkdtemp(prefix=PREFIX, dir=directory))
        self.path = self.directory/'all-arrays.bin'
        self.manifest_path = self.directory/'layout.json'
        self._backing = None
        self._before_factorization = None
        self._matrix_weak = None
        self._finalizer = None
        self._adopted = False
        index = np.dtype(self._bound['index_dtype'])
        nnz, total = self._bound['complete_stored_entries'], self._bound['rows']
        layout, offset = [], 0
        for field, shape, dtype in (('data', (nnz,), np.dtype('float64')),
                                     ('indices', (nnz,), index), ('indptr', (total+1,), index)):
            size = int(np.prod(shape))*dtype.itemsize
            layout.append(dict(field=field, offset=offset, shape=list(shape),
                               dtype=dtype.str, nbytes=size))
            offset += original_storage._rounded(size)
        if offset != self._bound['preallocated_CSR_file_bytes']:
            raise ArithmeticError('The complete original CSR storage bound differs')
        self._layout = layout
        self.stats = dict(kind='complete_original_CSR_assembled_directly_in_owned_backing',
            dimensions=dict(n=n, nodes=m, parameters=k),
            complete_CSR_object_preserved=True, planned_file_bytes=offset,
            logical_array_bytes=sum(row['nbytes'] for row in layout),
            scratch_free_bytes_before_allocation=free,
            required_scratch_bytes_before_this_CSR_allocation=required,
            disk_margin_bytes=disk_margin_bytes, chunk_bytes=chunk_bytes,
            copying_chunks=0, clean_page_release_calls=0,
            clean_page_release_advised_bytes=0, initial_CSR_hashes={},
            original_zero_compactions=0,
            mapped_arrays_readonly_after_original_prune=False,
            original_QR_arithmetic_changed=False, logical_bytes_are_not_an_RSS_credit=True,
            anonymous_complete_CSR_created=False, second_complete_CSR_copy_created=False,
            stored_zero_entries_removed_during_assembly=False,
            interval_blocks_written=0, complete_intervals_written=0,
            input_partial_arrays_retained_by_store=False,
            original_full_width_endpoint_rows_written=False,
            complete_original_middle_parameter_update_retained=True,
            phase_journal=str(self._reclamation_journal))
        try:
            descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_RDWR, 0o600)
            try:
                os.posix_fallocate(descriptor, 0, offset)
            finally:
                os.close(descriptor)
            self._backing = np.memmap(self.path, dtype=np.uint8, mode='r+', shape=(offset,))
            self.stats.update(backing_file=str(self.path), manifest_file=str(self.manifest_path),
                              allocated_disk_bytes=self.path.stat().st_blocks*512)
            self._record('complete_CSR_direct_backing_reserved',
                full_storage_bound=self._bound, observed_resources=reclamation.resources())
        except BaseException:
            original_storage._remove_directory(self.directory)
            raise

    def array(self, field):
        row = next(row for row in self._layout if row['field'] == field)
        return np.ndarray(tuple(row['shape']), dtype=np.dtype(row['dtype']),
                          buffer=self._backing, offset=row['offset'])

    def _write_manifest(self):
        # This is direct assembly, so do not inherit the old mapper's prose
        # describing an anonymous-to-mapped copy which did not happen here.
        with self.manifest_path.open('w') as stream:
            stream.write(json.dumps(dict(scope=__doc__, arrays=self._layout,
                file_bytes=len(self._backing), statistics=self.stats),
                indent=2, allow_nan=False)+'\n')
            stream.flush()
            os.fsync(stream.fileno())

    def release_elements(self, field, first, stop):
        if stop <= first:
            return
        row = next(row for row in self._layout if row['field'] == field)
        itemsize = np.dtype(row['dtype']).itemsize
        if not 0 <= first < stop <= row['shape'][0]:
            raise ValueError('The released complete-array interval is out of range')
        lo = (row['offset']+first*itemsize)//PAGE*PAGE
        hi = original_storage._rounded(row['offset']+stop*itemsize)
        self._backing._mmap.flush(lo, hi-lo)
        self._discard(lo, hi-lo)

    def _stream_hashes(self, matrix):
        result = {}
        for row in self._layout:
            array = getattr(matrix, row['field'])
            if (array.dtype.str != row['dtype'] or list(array.shape) != row['shape']
                    or not array.flags.c_contiguous or not np.shares_memory(array, self._backing)):
                raise ValueError('The complete original CSR storage identity changed')
            flat = memoryview(array).cast('B')
            digest = hashlib.sha256()
            for first in range(0, row['nbytes'], self._chunk_bytes):
                stop = min(row['nbytes'], first+self._chunk_bytes)
                digest.update(flat[first:stop])
                lo, hi = row['offset']+first, row['offset']+stop
                self._backing._mmap.flush(lo, original_storage._rounded(hi)-lo)
                self._discard(lo, original_storage._rounded(hi)-lo)
            result[row['field']] = digest.hexdigest()
            del flat, array
        return result

    def attach_completed_matrix(self, matrix):
        if self._matrix_weak is not None:
            raise RuntimeError('A complete assembly store may attach to only one original CSR object')
        if not isspmatrix_csr(matrix) or matrix.tocsr() is not matrix:
            raise TypeError('The original complete CSR object is required')
        if matrix.shape != (self._bound['rows'], self._bound['rows']):
            raise ValueError('The complete original square system dimensions changed')
        hashes = self._stream_hashes(matrix)
        self.stats['initial_CSR_hashes'] = hashes
        for row in self._layout:
            row['sha256_before_original_zero_compaction'] = hashes[row['field']]
        self._matrix_weak = weakref.ref(matrix)
        matrix._complete_assembly_storage = self
        self._finalizer = weakref.finalize(matrix, original_storage._remove_directory,
                                           str(self.directory))
        self.stats.update(assembly_complete=True, complete_final_arrays_bound_to_same_CSR=True,
            source_sha256=sha(__file__), reclamation_source_sha256=RECLAMATION_SHA,
            original_stacked_matmul_source_sha256=hashlib.sha256(
                inspect.getsource(_bvp.stacked_matmul).encode()).hexdigest(),
            original_resource_and_scientific_gates_not_changed=True)
        self._write_manifest()
        self._record('complete_CSR_direct_assembly_return',
                     actual_statistics=dict(self.stats), observed_resources=reclamation.resources())


def construct(n, m, k, i_jac, j_jac, h, df_dy, df_dy_middle, df_dp, df_dp_middle,
              dbc_dya, dbc_dyb, dbc_dp, *, storage_directory, radial_block=16,
              record=None, release_inputs=None, disk_margin_bytes=512*MIB):
    if (n < 1 or m < 2 or k < 0 or radial_block < 1 or h.shape != (m-1,)
            or df_dy.shape != (n, n, m) or df_dy_middle.shape != (n, n, m-1)
            or dbc_dya.shape != (n+k, n) or dbc_dyb.shape != (n+k, n)
            or (k and (df_dp.shape != (n, k, m) or df_dp_middle.shape != (n, k, m-1)
                       or dbc_dp.shape != (n+k, k)))):
        raise ValueError('Complete original collocation array shapes differ')
    arrays = [h, df_dy, df_dy_middle, dbc_dya, dbc_dyb]
    if k:
        arrays += [df_dp, df_dp_middle, dbc_dp]
    if any(np.asarray(value).dtype != np.dtype('float64') for value in arrays):
        raise ValueError('This exact-order storage branch requires the real binary64 source')
    if k and not df_dp_middle.flags.writeable:
        raise ValueError('The original caller-visible middle-parameter update must be writable')
    gc.collect()
    begin = time.monotonic()
    store = AssembledCSRStore(n, m, k, storage_directory,
                               disk_margin_bytes=disk_margin_bytes)
    try:
        total, width = n*m+k, 2*n+k
        nnz = total*width
        data, indices, indptr = (store.array(field) for field in ('data', 'indices', 'indptr'))
        index_dtype = indices.dtype
        # Bounded exact integer initialization; all final indptr bytes are mapped.
        for first in range(0, total+1, 65536):
            stop = min(total+1, first+65536)
            indptr[first:stop] = np.arange(first, stop, dtype=index_dtype)*width
            store.release_elements('indptr', first, stop)
        if int(indptr[-1]) != nnz:
            raise ArithmeticError('The full original stored-entry count differs')
        values, columns = data.reshape(total, width), indices.reshape(total, width)
        first_bc = (m-1)*n
        columns[first_bc:, :n] = np.arange(n, dtype=index_dtype)
        columns[first_bc:, n:2*n] = np.arange((m-1)*n, m*n, dtype=index_dtype)
        values[first_bc:, :n], values[first_bc:, n:2*n] = dbc_dya, dbc_dyb
        if k:
            columns[first_bc:, 2*n:] = np.arange(m*n, total, dtype=index_dtype)
            values[first_bc:, 2*n:] = dbc_dp
            dp, dp_middle = np.transpose(df_dp, (2, 0, 1)), np.transpose(df_dp_middle, (2, 0, 1))
        for field in ('data', 'indices'):
            store.release_elements(field, first_bc*width, nnz)
        store.stats['original_full_width_endpoint_rows_written'] = True
        interval_values = values[:first_bc].reshape(m-1, n, width)
        dy, dy_middle = np.transpose(df_dy, (2, 0, 1)), np.transpose(df_dy_middle, (2, 0, 1))
        hh = h[:, None, None]
        block = radial_block if n > 50 else m-1
        eye = np.identity(n)
        for first in range(0, m-1, block):
            stop = min(m-1, first+block)
            sl, hs = slice(first, stop), hh[first:stop]
            left, right, middle = dy[first:stop], dy[first+1:stop+1], dy_middle[sl]
            for interval in range(first, stop):
                columns[interval*n:(interval+1)*n, :2*n] = np.arange(
                    interval*n, (interval+2)*n, dtype=index_dtype)
            if k:
                columns[first*n:stop*n, 2*n:] = np.arange(m*n, total, dtype=index_dtype)
            A = np.empty((stop-first, n, n), dtype=dy.dtype)
            A[:] = -eye
            A -= hs/6*(left+2*middle)
            temp = _bvp.stacked_matmul(middle, left)
            A -= hs**2/12*temp
            interval_values[first:stop, :, :n] = A
            del A, temp
            B = np.empty((stop-first, n, n), dtype=dy.dtype)
            B[:] = eye
            B -= hs/6*(right+2*middle)
            temp = _bvp.stacked_matmul(middle, right)
            B += hs**2/12*temp
            interval_values[first:stop, :, n:2*n] = B
            del B, temp
            if k:
                temp = _bvp.stacked_matmul(middle, dp[first:stop]-dp[first+1:stop+1])
                dp_middle[sl] += 0.125*hs*temp
                P = -hs/6*(dp[first:stop]+dp[first+1:stop+1]+4*dp_middle[sl])
                interval_values[first:stop, :, 2*n:] = P
                del P, temp
            for field in ('data', 'indices'):
                store.release_elements(field, first*n*width, stop*n*width)
            store.stats['interval_blocks_written'] += 1
            store.stats['complete_intervals_written'] = stop
            if release_inputs is not None:
                release_inputs()
        if store.stats['complete_intervals_written'] != m-1:
            raise ArithmeticError('Every complete original collocation interval is required')
        result = csr_matrix((data, indices, indptr), shape=(total, total), copy=False)
        result.has_sorted_indices = True
        result.has_canonical_format = True
        if not all(np.shares_memory(getattr(result, field), store._backing)
                   for field in ('data', 'indices', 'indptr')):
            raise RuntimeError('The final complete CSR did not retain all directly mapped arrays')
        store.stats.update(radial_temporary_block=block,
            input_COO_indices_were_none=bool(i_jac is None and j_jac is None),
            original_block_formula_operation_order_preserved=True,
            original_parameter_middle_update_preserved=True,
            seconds=time.monotonic()-begin,
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        store.attach_completed_matrix(result)
        if record is not None:
            record(dict(store.stats))
        return result
    except BaseException:
        original_storage._remove_directory(store.directory)
        raise


def adopt_store_for_before_qr(owner, matrix, n, m, k, directory, *,
                             disk_margin_bytes=512*MIB, chunk_bytes=8*MIB,
                             before_factorization=None):
    """Keep the same checked matrix/backing; do not allocate or copy another CSR."""
    del owner, directory  # The original CSR itself owns the exact backing lifetime.
    if disk_margin_bytes < 512*MIB or chunk_bytes < PAGE or chunk_bytes % PAGE:
        raise ValueError('The original explicit storage policy must be retained')
    store = getattr(matrix, '_complete_assembly_storage', None)
    if (not isinstance(store, AssembledCSRStore) or store._matrix_weak() is not matrix
            or (store.n, store.m, store.k) != (n, m, k) or store._adopted
            or store.stats.get('assembly_complete') is not True
            or store.stats['original_zero_compactions'] != 0):
        raise ValueError('This is not one fresh complete CSR from the declared assembly branch')
    hashes = store._stream_hashes(matrix)
    if hashes != store.stats['initial_CSR_hashes']:
        raise ValueError('Complete assembled CSR bytes changed before the original QR adopted them')
    store._adopted = True
    store._before_factorization = before_factorization
    store.stats.update(adopted_before_original_QR=True,
        complete_CSR_rehashed_before_adoption=True,
        second_complete_CSR_copy_created=False,
        CSR_owner_is_original_matrix_with_weak_finalizer=True,
        actual_factor_mapping_directory_is_separate=True)
    store._write_manifest()
    store._record('complete_original_CSR_adopted_without_second_copy',
                  observed_resources=reclamation.resources())
    return store


_ADOPT_GLOBALS = dict(mapped.BeforeQRMappedBlockQR.__init__.__globals__)
_ADOPT_GLOBALS.update(CompleteCSRBeforeQRStore=adopt_store_for_before_qr,
                      CompleteFactorStore=reclamation.ReclaimedCompleteFactorStore)
_ADOPT_INIT = FunctionType(mapped.BeforeQRMappedBlockQR.__init__.__code__,
    _ADOPT_GLOBALS, mapped.BeforeQRMappedBlockQR.__init__.__name__,
    mapped.BeforeQRMappedBlockQR.__init__.__defaults__,
    mapped.BeforeQRMappedBlockQR.__init__.__closure__)
_ADOPT_INIT.__kwdefaults__ = dict(mapped.BeforeQRMappedBlockQR.__init__.__kwdefaults__ or {})


class AdoptedBeforeQRMappedBlockQR(mapped.BeforeQRMappedBlockQR):
    __init__ = _ADOPT_INIT


def adopted_factor_additional_backing_upper_bound(n, m, k):
    bound = original_storage.backing_upper_bound(n, m, k, 'factor-only')
    return dict(kind='additional_all_factor_storage_after_existing_CSR_adoption',
        original_factor_bound=bound,
        total_backing_and_manifest_upper_bytes=bound['total_backing_and_manifest_upper_bytes']+8*MIB,
        second_complete_CSR_copy_required=False,
        existing_CSR_file_bytes_not_credited_as_available_RAM=True,
        original_external_disk_margin_must_be_added=True)


def install(*, storage_directory, radial_block=16, record=None, release_inputs=None,
            disk_margin_bytes=512*MIB):
    previous_indices, previous_construct = _bvp.compute_jac_indices, _bvp.construct_global_jac
    def no_COO_indices(n, m, k):
        return None, None
    def complete(n, m, k, i, j, h, dy, dym, dp, dpm, bca, bcb, bcp):
        return construct(n, m, k, i, j, h, dy, dym, dp, dpm, bca, bcb, bcp,
            storage_directory=storage_directory, radial_block=radial_block,
            record=record, release_inputs=release_inputs, disk_margin_bytes=disk_margin_bytes)
    _bvp.compute_jac_indices, _bvp.construct_global_jac = no_COO_indices, complete
    def restore():
        _bvp.compute_jac_indices, _bvp.construct_global_jac = previous_indices, previous_construct
    return dict(source_sha256=sha(__file__), reclamation_source_sha256=RECLAMATION_SHA,
                full_original_layout_preserved=True), restore


def cleanup_joined_child(outdir, returncode, *, child_return_observed, entry_sha256):
    if child_return_observed is not True or not isinstance(returncode, int):
        raise ValueError('Actual joined child termination is required')
    outdir = Path(outdir).resolve()
    directory = outdir/ROOT_NAME
    if not directory.exists():
        return dict(child_returncode=returncode, store_created=False, removed=[])
    if directory.is_symlink() or directory.resolve().parent != outdir:
        raise ValueError('The actual complete CSR root is not the owned child directory')
    owner_path = directory/'owner.json'
    if owner_path.is_symlink() or not owner_path.is_file():
        raise ValueError('An ordinary real CSR ownership record is required')
    owner = json.loads(owner_path.read_text())
    if (owner.get('kind') != OWNER_KIND or Path(owner['actual_child_outdir']).resolve() != outdir
            or owner.get('entry_sha256') != entry_sha256):
        raise ValueError('The actual complete CSR storage ownership differs')
    removed = []
    for path in sorted(directory.iterdir()):
        if path.name == 'owner.json':
            continue
        if path.is_symlink() or not path.is_dir() or not path.name.startswith(PREFIX):
            raise ValueError('Unexpected content in the owned complete CSR assembly root')
        files = list(path.iterdir())
        if any(p.is_symlink() or not p.is_file() or p.name not in ('all-arrays.bin', 'layout.json')
               for p in files):
            raise ValueError('Unexpected file in the complete CSR assembly backing directory')
        observation = dict(directory=str(path), files=[dict(path=str(p), bytes=p.stat().st_size,
            allocated_disk_bytes=p.stat().st_blocks*512) for p in files])
        if (path/'layout.json').exists():
            observation['layout_sha256'] = sha(path/'layout.json')
        shutil.rmtree(path)
        observation['removed_only_after_actual_child_terminal'] = True
        removed.append(observation)
    result = dict(kind='joined_child_owned_complete_CSR_assembly_cleanup',
        child_returncode=returncode, actual_child_terminal_observed=True,
        owner=str(owner_path), owner_sha256=sha(owner_path), store_created=True,
        removed=removed, scientific_fields_checkpoints_or_sources_removed=False)
    with (outdir/'joined-child-complete-CSR-assembly-cleanup.json').open('w') as stream:
        stream.write(json.dumps(result, indent=2, allow_nan=False)+'\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--describe', action='store_true')
    options = parser.parse_args()
    if not options.describe:
        parser.error('Use --describe or import the full-shape assembly/storage APIs.')
    print(json.dumps(dict(scope=__doc__, prepared_entry_only=True,
        original_constructor_code_object_identical=(AdoptedBeforeQRMappedBlockQR.__init__.__code__
                                                   is mapped.BeforeQRMappedBlockQR.__init__.__code__),
        original_complete_solve_method_identical=(AdoptedBeforeQRMappedBlockQR.solve
                                                is mapped.BeforeQRMappedBlockQR.solve),
        original_full_partial_inputs_and_inplace_middle_update_retained=True,
        second_CSR_backing_not_created_by_adopter=True,
        own_storage_cleanup_requires_actual_join=True,
        large_matrix_or_BVP_executed=False,
        actual_usage_requires_original_all_scientific_and_resource_gates=True,
        shape_bounds=[storage_bound(3*k+1, 1185, k) for k in (32, 40, 48)]), indent=2))


if __name__ == '__main__':
    main()
