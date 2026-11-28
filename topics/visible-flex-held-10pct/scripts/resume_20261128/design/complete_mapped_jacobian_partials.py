"""Full original node/midpoint Jacobian tensors with C-order disk backing.

The original split_jac calls, radial groups, output shapes/dtypes, assignment
order and exception propagation are retained. Instead of two full anonymous
np.empty arrays, each call writes two preallocated writable C-order memmaps.
Each completed original batch is flushed before mapped/file-cache advice.
Nothing is projected out. These tensors may be changed by the original
collocation dp-middle formula, so they remain writable until their original
caller releases them. Stores hold weak array references, never a live cycle.
"""
import gc
import hashlib
import json
import mmap
import os
from pathlib import Path
import shutil
import tempfile
import time
import weakref

import numpy as np

import exception_safe_radial_batches as original
import complete_csr_prefactor_mmap as original_storage

MIB = 2**20
PAGE = mmap.PAGESIZE
EXPECTED_ORIGINAL = '2d2b413a46a23882341a4d5cac7ce2bc2c44c8444129d322d898288597c2c7a7'
if hashlib.sha256(Path(original.__file__).read_bytes()).hexdigest() != EXPECTED_ORIGINAL:
    raise ValueError('The original exact split_jac/lifecycle source changed')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _rounded(value):
    return ((value+PAGE-1)//PAGE)*PAGE


class CompletePartialRegistry:
    def __init__(self, outdir, *, entry_sha256, external_disk_bytes=512*MIB):
        if external_disk_bytes < 512*MIB:
            raise ValueError('At least 512MiB external scratch margin is required')
        self.outdir = Path(outdir).resolve()
        self.directory = self.outdir/'mapped-complete-J-partials'
        self.journal = self.outdir/'complete-J-partial-storage.jsonl'
        self.entry_sha256 = entry_sha256
        self.external_disk_bytes = int(external_disk_bytes)
        self.stores = {}
        self.counter = 0
        self.started = time.monotonic()
        self.statistics = dict(full_tensor_pairs=0, original_batches=0,
            filled_radial_columns=0, full_logical_tensor_bytes=0,
            mapped_page_release_calls=0, original_complete_arrays_released=0,
            writable_C_order_complete_tensors=True,
            original_batch_calls_or_numerical_arithmetic_changed=False,
            file_cache_advice_is_not_proof_of_charge_reduction=True)

    def event(self, kind, **fields):
        row = dict(event=kind, seconds=time.monotonic()-self.started,
            process_id_for_observation_only=os.getpid(),
            observed_memory=original_storage.process_memory(), **fields)
        with self.journal.open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
            stream.flush()

    def allocate(self, n, m, k):
        if min(n,m,k) < 1:
            raise ValueError('This original design branch requires complete nonempty state and parameter tensors')
        owner = dict(kind='owned_original_complete_Jacobian_partial_storage',
            actual_child_outdir=str(self.outdir), entry_sha256=self.entry_sha256,
            provider_sha256=sha(__file__),
            original_batch_source_sha256=EXPECTED_ORIGINAL,
            temporary_reproducible_execution_storage=True,
            mathematical_field_or_checkpoint=False)
        if not self.directory.exists():
            self.directory.mkdir(exist_ok=False)
            (self.directory/'owner.json').write_text(json.dumps(owner,indent=2)+'\n')
        owner_path = self.directory/'owner.json'
        if (self.directory.is_symlink() or owner_path.is_symlink()
                or self.directory.resolve().parent != self.outdir
                or json.loads(owner_path.read_text()) != owner):
            raise ValueError('The complete original partial-store owner changed')
        self.counter += 1
        store = _FullPartialPair(self, self.counter, n, m, k)
        self.stores[self.counter] = store
        dy,dp = store.create()
        self.statistics['full_tensor_pairs'] += 1
        self.statistics['full_logical_tensor_bytes'] += dy.nbytes+dp.nbytes
        return store,dy,dp

    def release_inputs(self):
        """Flush real dp-middle writes and advise all still-live full inputs."""
        for store in tuple(self.stores.values()):
            store.flush_and_drop('after_original_interval_assembly_block')

    def make_split_jac(self):
        registry = self

        def split_jac(fun, block, stats=None, event=None):
            if block < 1:
                raise ValueError('A positive original radial block is required')
            stats = original.statistics() if stats is None else stats

            def evaluate(t, y, p):
                stats['jacobian_calls'] += 1
                if len(t) <= block:
                    exception = None
                    stats['jacobian_blocks'] += 1
                    try:
                        return fun(t,y,p)
                    except BaseException as error:
                        exception = original._exception(error)
                        raise
                    finally:
                        original._release(stats,'jacobian',exception,event)
                n,m,k = y.shape[0],len(t),len(p)
                store,dy,dp = registry.allocate(n,m,k)
                try:
                    for first in range(0,m,block):
                        sl = slice(first,first+block)
                        exception = None
                        stats['jacobian_blocks'] += 1
                        try:
                            jy,jp = fun(t[sl],y[:,sl],p)
                            dy[:,:,sl],dp[:,:,sl] = jy,jp
                            del jy,jp
                        except BaseException as error:
                            exception = original._exception(error)
                            raise
                        finally:
                            original._release(stats,'jacobian',exception,event)
                        store.filled += min(block,m-first)
                        registry.statistics['original_batches'] += 1
                        registry.statistics['filled_radial_columns'] += min(block,m-first)
                        store.flush_and_drop('after_original_full_radial_batch')
                    if store.filled != m:
                        raise RuntimeError('The original complete radial tensor was not filled')
                    registry.event('complete_original_partial_pair_return',
                        ordinal=store.ordinal,n=n,m=m,k=k,
                        filled_radial_columns=store.filled,original_radial_batch=block,
                        dy_shape=list(dy.shape),dp_shape=list(dp.shape),
                        dy_strides=list(dy.strides),dp_strides=list(dp.strides),
                        dy_dtype=dy.dtype.str,dp_dtype=dp.dtype.str,
                        full_array_shapes_strides_and_dtype_preserved=True,
                        full_pair_bytes=dy.nbytes+dp.nbytes)
                    return dy,dp
                except BaseException:
                    # The original exception is re-raised unchanged; no unused
                    # partial output is kept alive by this wrapper's locals.
                    del dy,dp
                    gc.collect()
                    raise

            return evaluate

        return split_jac


class _FullPartialPair:
    def __init__(self, registry, ordinal, n, m, k):
        self.registry = weakref.ref(registry)
        self.ordinal = ordinal
        self.shapes = ((n,n,m),(n,k,m))
        self.filled = 0
        self.references = []
        self.remaining = 2
        self.directory = Path(tempfile.mkdtemp(prefix='complete-partials-',dir=registry.directory))
        self.paths = [self.directory/'dy.bin',self.directory/'dp.bin']
        self.allocations = [_rounded(int(np.prod(shape))*np.dtype(float).itemsize)
                            for shape in self.shapes]
        required = sum(self.allocations)+registry.external_disk_bytes
        actual = shutil.disk_usage(self.directory).free
        if actual < required:
            shutil.rmtree(self.directory)
            raise MemoryError('Full original partial tensors and the external scratch margin do not fit')
        self.layout = dict(ordinal=ordinal,shapes=[list(s) for s in self.shapes],
            dtype=np.dtype(float).str,order='C',actual_disk_available_before_allocation=actual,
            disk_required_for_this_pair_and_external_margin=required,
            all_full_nodes_state_columns_and_parameters_retained=True,
            allocations=[dict(file=p.name,bytes=b) for p,b in zip(self.paths,self.allocations)])

    def create(self):
        arrays = []
        try:
            for path,shape,allocated in zip(self.paths,self.shapes,self.allocations):
                fd = os.open(path,os.O_CREAT|os.O_EXCL|os.O_RDWR,0o600)
                try:
                    os.posix_fallocate(fd,0,allocated)
                finally:
                    os.close(fd)
                value = np.memmap(path,dtype=float,mode='r+',shape=shape,order='C')
                if not value.flags.c_contiguous or not value.flags.writeable:
                    raise MemoryError('Full writable C-order original tensors are required')
                self.references.append(weakref.ref(value))
                weakref.finalize(value,self._array_released)
                arrays.append(value)
            (self.directory/'layout.json').write_text(json.dumps(self.layout,indent=2)+'\n')
            registry = self.registry()
            if registry is not None:
                registry.event('complete_original_partial_pair_allocated',
                    ordinal=self.ordinal,layout=self.layout,
                    current_owned_pairs=len(registry.stores))
            return arrays[0],arrays[1]
        except BaseException:
            arrays.clear()
            shutil.rmtree(self.directory,ignore_errors=True)
            registry = self.registry()
            if registry is not None:
                registry.stores.pop(self.ordinal,None)
            raise

    def flush_and_drop(self, phase):
        if not hasattr(mmap.mmap,'madvise') or not hasattr(os,'posix_fadvise'):
            raise MemoryError('The complete partial-tensor page-release operations are unavailable')
        try:
            for reference,path in zip(self.references,self.paths):
                value = reference()
                if value is None:
                    continue
                value.flush()
                value._mmap.madvise(mmap.MADV_DONTNEED)
                descriptor = os.open(path,os.O_RDONLY)
                try:
                    os.posix_fadvise(descriptor,0,0,os.POSIX_FADV_DONTNEED)
                finally:
                    os.close(descriptor)
                del value
        except OSError as error:
            raise MemoryError('Full original partial-storage flush/page-release failed: '+str(error)) from error
        registry = self.registry()
        if registry is not None:
            registry.statistics['mapped_page_release_calls'] += 1
            if phase != 'after_original_full_radial_batch' or self.filled == self.shapes[0][2]:
                registry.event('complete_original_partial_pages_advised',
                    ordinal=self.ordinal,phase=phase,filled_radial_columns=self.filled,
                    actual_calls_completed=True,physical_or_cgroup_reclamation_proved=False)

    def _array_released(self):
        self.remaining -= 1
        if self.remaining:
            return
        registry = self.registry()
        try:
            if registry is not None:
                registry.stores.pop(self.ordinal,None)
                registry.statistics['original_complete_arrays_released'] += 2
                registry.event('complete_original_partial_pair_no_longer_referenced',
                    ordinal=self.ordinal,allocated_file_bytes=sum(self.allocations),
                    only_owned_reproducible_partials_removed=True)
        finally:
            shutil.rmtree(self.directory,ignore_errors=True)


def cleanup_joined_child(outdir, returncode, *, child_return_observed, entry_sha256):
    """Remove only this explicit partial store after its child really joined."""
    if child_return_observed is not True or not isinstance(returncode,int):
        raise ValueError('An actual joined child terminal is required')
    out = Path(outdir).resolve()
    directory = out/'mapped-complete-J-partials'
    if not directory.exists():
        return dict(store_created=False,removed=[],actual_child_returncode=returncode)
    owner_path = directory/'owner.json'
    if directory.is_symlink() or owner_path.is_symlink() or not owner_path.is_file():
        raise ValueError('Require the exact ordinary owned partial-store directory')
    owner = json.loads(owner_path.read_text())
    if (owner.get('kind')!='owned_original_complete_Jacobian_partial_storage'
            or Path(owner['actual_child_outdir']).resolve()!=out
            or owner['entry_sha256']!=entry_sha256):
        raise ValueError('The exact original partial-store ownership differs')
    removed = []
    for child in sorted(directory.iterdir()):
        if child.name=='owner.json':
            continue
        if child.is_symlink() or not child.is_dir() or not child.name.startswith('complete-partials-'):
            raise ValueError('Unexpected content in the original partial store')
        files = list(child.iterdir())
        if any(p.is_symlink() or not p.is_file() or p.name not in ('dy.bin','dp.bin','layout.json')
               for p in files):
            raise ValueError('Unexpected partial-store file')
        row = dict(directory=str(child),files=[dict(path=str(p),bytes=p.stat().st_size) for p in files])
        if (child/'layout.json').exists():
            row['layout_sha256'] = sha(child/'layout.json')
        shutil.rmtree(child)
        removed.append(row)
    result = dict(actual_child_returncode=returncode,actual_child_terminal_observed=True,
        owner=str(owner_path),owner_sha256=sha(owner_path),
        store_created=True,removed=removed,original_fields_or_checkpoints_removed=False)
    (out/'joined-child-partial-storage-cleanup.json').write_text(json.dumps(result,indent=2)+'\n')
    return result
