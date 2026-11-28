#!/usr/bin/env python3
"""Additional reclamation around the unchanged complete CSR/QR algorithms.

The original mapper already replaces each persistent array separately. This
entry does not claim to remove an old-array list that never existed. It adds
allocator collection before each original mapping phase, collection after
16 MiB of original arrays have actually been replaced, and file-cache advice
after the original flush and mapped-page advice. All original bytes, shapes,
orders, copy checks, CSR entries, QR arithmetic and residual checks remain.

POSIX_FADV_DONTNEED is advice, not evidence that a cgroup charge has fallen.
The small durable journal records the actual process and readable cgroup
observations; inaccessible cgroup files remain unknown. No cause is assigned
to any prior killed process. Construction peaks and original resource gates
still apply. This module does not run a BVP or construct a test matrix.
"""
import argparse
import hashlib
import inspect
import json
import os
from pathlib import Path
import sys
import textwrap
import time
from types import FunctionType


HERE = Path(__file__).resolve().parent
DESIGN = HERE.parent / 'design'
sys.path.insert(0, str(DESIGN))
import actual_process_memory_limits as limits
import complete_factor_mmap as factor_storage
import complete_csr_prefactor_mmap as mapped


RELEASE_BYTES = 16 * factor_storage.MIB
EXPECTED = {
    DESIGN / 'complete_factor_mmap.py':
        '12c18e96f333b588c9e8ac8db423976d2210f36c705b40c467f144d9a06994eb',
    DESIGN / 'complete_csr_prefactor_mmap.py':
        '213957953e7f98be6b3a598a67feb4454120b9abded9fdda0423ee5fe5358b99',
    HERE.parent / 'block_qr_v2.py':
        'b008698a0959f472bea597c6fcd31246f3d61c1c41109212cc9256a322c1ebf8',
    DESIGN / 'actual_process_memory_limits.py':
        '1e208cfbcf58ff9c9dd9e794b4426eb8c1767d707bcfc0fcf6e78cc734071114',
}
for _path, _expected in EXPECTED.items():
    if hashlib.sha256(_path.read_bytes()).hexdigest() != _expected:
        raise RuntimeError('The frozen complete storage dependency changed: ' + str(_path))


def resources():
    """Observed quantities, including unknown rather than invented limits."""
    result = mapped.process_memory()
    observation = limits.snapshot()
    result['readable_cgroup_numeric_fields'] = limits.numeric_values(observation)
    result['cgroup_membership'] = observation['cgroup']
    result['cgroup_unknown_files'] = {
        path: {'error': value.get('error'), 'errno': value.get('errno')}
        for path, value in observation['memory_files'].items()
        if 'text' not in value
    }
    stats = {}
    directories = {str(Path(path).parent)
                   for path in observation['memory_files']}
    for directory in sorted(directories):
        path = Path(directory) / 'memory.stat'
        value = limits.read(path)
        if 'text' not in value:
            stats[str(path)] = value
        else:
            stats[str(path)] = {
                line.split()[0]: int(line.split()[1])
                for line in value['text'].splitlines()
                if len(line.split()) == 2 and line.split()[1].isdigit()
            }
    result['readable_cgroup_memory_stat'] = stats
    result['file_cache_advice_is_not_a_measured_reclamation_claim'] = True
    return result


def _retirement_constructor(original, original_line):
    """Insert only a callback after the original ndarray references die."""
    source = textwrap.dedent(inspect.getsource(original))
    if source.count(original_line) != 1:
        raise RuntimeError('The original one-array-at-a-time mapper changed')
    adjusted = source.replace(original_line,
        original_line + "                self._after_array_replacement(row['nbytes'])\n")
    namespace = dict(original.__globals__)
    exec(compile(adjusted, '<complete-storage-array-retirement-only>', 'exec'), namespace)
    return (namespace[original.__name__],
            hashlib.sha256(source.encode()).hexdigest(),
            hashlib.sha256(adjusted.encode()).hexdigest())


_FACTOR_INIT, _FACTOR_ORIGINAL_SHA, _FACTOR_RETIRED_SHA = _retirement_constructor(
    factor_storage.CompleteFactorStore.__init__,
    '                del source, flat, mapped\n')
_CSR_INIT, _CSR_ORIGINAL_SHA, _CSR_RETIRED_SHA = _retirement_constructor(
    mapped.CompleteCSRBeforeQRStore.__init__,
    '                del source, flat, view\n')


class _Reclamation:
    """Storage metadata only; no factor/matrix/old-array reference is held."""
    def _setup_reclamation(self, directory, role):
        if not hasattr(os, 'posix_fadvise') or not hasattr(os, 'POSIX_FADV_DONTNEED'):
            raise MemoryError('This explicit storage branch requires POSIX file-cache advice')
        directory = Path(directory).resolve()
        if not directory.is_dir():
            raise FileNotFoundError('The original caller must own the storage directory')
        self._reclamation_role = role
        self._reclamation_started = time.monotonic()
        self._reclamation_journal = directory / 'storage-reclamation.jsonl'
        self._reclamation_bytes_since_trim = 0
        self._reclamation_state = {
            'kind': 'original_complete_storage_with_additional_reclamation',
            'role': role,
            'replacement_callback_after_original_del': True,
            'replaced_logical_original_array_bytes': 0,
            'allocator_release_threshold_bytes': RELEASE_BYTES,
            'allocator_release_calls': 0,
            'file_cache_advice_calls': 0,
            'file_cache_advised_bytes': 0,
            'file_cache_advice_succeeded': True,
            'file_cache_reclamation_or_cgroup_decrease_proved': False,
            'original_constructor_peak_eliminated': False,
            'original_math_or_acceptance_changed': False,
        }
        self._record('mapping_phase_reclamation_entry', dependency_hashes={
            str(path): digest for path, digest in EXPECTED.items()},
            source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        self._trim('before_original_mapping_phase')

    def _record(self, event, **fields):
        record = dict(event=event, role=self._reclamation_role,
            process_id_for_observation_only=os.getpid(),
            elapsed=time.monotonic()-self._reclamation_started,
            statistics=dict(self._reclamation_state), **fields)
        with self._reclamation_journal.open('a') as stream:
            stream.write(json.dumps(record, sort_keys=True, allow_nan=False)+'\n')
            stream.flush()
            os.fsync(stream.fileno())

    def _trim(self, phase):
        before = resources()
        observation = factor_storage.collect_and_trim()
        after = resources()
        self._reclamation_state['allocator_release_calls'] += 1
        self._reclamation_bytes_since_trim = 0
        self._record('actual_unused_allocator_release', phase=phase,
                     before=before, after=after, original_helper_observation=observation)

    def _after_array_replacement(self, nbytes):
        # The original source/flat/view references have already been deleted.
        # A logical byte counter is never used as an observed RSS credit.
        self._reclamation_state['replaced_logical_original_array_bytes'] += nbytes
        self._reclamation_bytes_since_trim += nbytes
        if self._reclamation_bytes_since_trim >= RELEASE_BYTES:
            self._trim('after_actual_original_array_replacement')

    def _discard(self, offset, length):
        # Both original copy paths flush this exact page-aligned range before
        # reaching here. Original post-solve calls touch read-only clean bytes.
        super()._discard(offset, length)
        descriptor = os.open(self.path, os.O_RDONLY)
        try:
            os.posix_fadvise(descriptor, offset, length, os.POSIX_FADV_DONTNEED)
        except OSError as error:
            self._reclamation_state['file_cache_advice_succeeded'] = False
            self._record('file_cache_advice_failed', offset=offset, length=length,
                         errno=error.errno, error=str(error))
            raise
        finally:
            os.close(descriptor)
        self._reclamation_state['file_cache_advice_calls'] += 1
        self._reclamation_state['file_cache_advised_bytes'] += length
        self.stats['additional_storage_reclamation'] = dict(self._reclamation_state)

    def _finish_reclamation(self):
        if self._reclamation_bytes_since_trim:
            self._trim('after_final_actual_original_array_replacement')
        self.stats['additional_storage_reclamation'] = dict(self._reclamation_state)
        self._record('mapping_phase_reclamation_return', observed_resources=resources())


class ReclaimedCompleteFactorStore(_Reclamation, factor_storage.CompleteFactorStore):
    def __init__(self, factor, directory, *, map_scope='factor-only',
                 disk_margin_bytes=512*factor_storage.MIB,
                 chunk_bytes=8*factor_storage.MIB):
        # In BeforeQRMappedBlockQR this is after the complete original QR has
        # returned, so its old edge/temporary locals have lost their references.
        self._setup_reclamation(directory, 'complete_original_QR_factors')
        _FACTOR_INIT(self, factor, directory, map_scope=map_scope,
                     disk_margin_bytes=disk_margin_bytes, chunk_bytes=chunk_bytes)
        self._finish_reclamation()


class ReclaimedCompleteCSRBeforeQRStore(_Reclamation, mapped.CompleteCSRBeforeQRStore):
    def __init__(self, owner, matrix, n, m, k, directory, *,
                 disk_margin_bytes=512*factor_storage.MIB,
                 chunk_bytes=8*factor_storage.MIB, before_factorization=None):
        self._setup_reclamation(directory, 'complete_original_CSR')
        _CSR_INIT(self, owner, matrix, n, m, k, directory,
                  disk_margin_bytes=disk_margin_bytes, chunk_bytes=chunk_bytes,
                  before_factorization=before_factorization)
        self._finish_reclamation()


# The top-level constructor bytecode is identical. Its globals point only to
# the two explicit new storage classes; its complete original QR callback,
# sparse object, instance-prune restoration, tests and solve are unchanged.
_CONSTRUCTOR_GLOBALS = dict(mapped.BeforeQRMappedBlockQR.__init__.__globals__)
_CONSTRUCTOR_GLOBALS.update(
    CompleteCSRBeforeQRStore=ReclaimedCompleteCSRBeforeQRStore,
    CompleteFactorStore=ReclaimedCompleteFactorStore)
_RECLAIMED_INIT = FunctionType(mapped.BeforeQRMappedBlockQR.__init__.__code__,
    _CONSTRUCTOR_GLOBALS, mapped.BeforeQRMappedBlockQR.__init__.__name__,
    mapped.BeforeQRMappedBlockQR.__init__.__defaults__,
    mapped.BeforeQRMappedBlockQR.__init__.__closure__)
_RECLAIMED_INIT.__kwdefaults__ = dict(
    mapped.BeforeQRMappedBlockQR.__init__.__kwdefaults__ or {})


class ReclaimedBeforeQRMappedBlockQR(mapped.BeforeQRMappedBlockQR):
    __init__ = _RECLAIMED_INIT


def description():
    return dict(scope=__doc__, prepared_storage_entry_only=True,
        large_J_or_BVP_executed=False, positive_reclamation_measurement=False,
        original_dependency_hashes={str(path): digest for path, digest in EXPECTED.items()},
        original_CSR_mapper_constructor_sha256=_CSR_ORIGINAL_SHA,
        CSR_mapper_with_post_del_callback_sha256=_CSR_RETIRED_SHA,
        original_factor_mapper_constructor_sha256=_FACTOR_ORIGINAL_SHA,
        factor_mapper_with_post_del_callback_sha256=_FACTOR_RETIRED_SHA,
        top_level_constructor_code_object_identical=(
            ReclaimedBeforeQRMappedBlockQR.__init__.__code__
            is mapped.BeforeQRMappedBlockQR.__init__.__code__),
        original_solve_method_identical=(ReclaimedBeforeQRMappedBlockQR.solve
                                       is mapped.BeforeQRMappedBlockQR.solve),
        original_QR_constructor_unchanged=True,
        posix_file_cache_advice_available=hasattr(os, 'posix_fadvise')
                                          and hasattr(os, 'POSIX_FADV_DONTNEED'),
        resource_gates_must_be_kept_by_the_caller=True,
        durable_observation_relative_path='storage-reclamation.jsonl',
        extra_journal_bound_not_a_matrix_or_scientific_checkpoint=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--describe', action='store_true',
                        help='Print the exact source/storage contract; perform no numerical run.')
    options = parser.parse_args()
    if not options.describe:
        parser.error('This source is a drop-in storage class; use --describe or --help.')
    print(json.dumps(description(), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
