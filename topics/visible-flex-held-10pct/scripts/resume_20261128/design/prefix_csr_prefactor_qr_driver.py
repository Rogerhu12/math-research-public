#!/usr/bin/env python3
"""Complete original QR with checked full CSR mapping before factorization.

The original complete CSR and all QR factor entries remain in the original
direction/residual/refinement algorithms. Real disk allocation and observed
anonymous RSS gates preserve explicit external margins. Both complete stores
must release clean pages before returning a direction to original nonlinear
code. No equation, column, continuation rule or acceptance gate is removed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import time
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import complete_csr_prefactor_mmap as mapped
import complete_prefactor_memory_budget as budget
import prefix_block_qr_driver_v3 as original


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--mmap-disk-margin-mib', type=float, default=512.)
    options, rest = parser.parse_known_args()
    if options.mmap_disk_margin_mib < 512:
        raise ValueError('At least 512MiB external scratch margin is required')
    if '--help' in rest or '-h' in rest:
        sys.argv = [str(Path(original.__file__)), *rest]
        return original.main()
    out = Path(rest[rest.index('--outdir')+1]).resolve()
    directory = out/'mapped-factor-storage'
    if directory.exists():
        raise FileExistsError(directory)
    owner = dict(kind='owned_complete_CSR_before_QR_and_factor_scratch_storage',
        actual_child_outdir=str(out), process_id_for_observation_only=__import__('os').getpid(),
        entry_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        helper_sha256=hashlib.sha256(Path(mapped.__file__).read_bytes()).hexdigest(),
        temporary_reproducible_execution_storage=True, accepted_field=False)
    trace = out.with_name(out.name+'-csr-prefactor-mapped.jsonl')
    command = list(sys.argv)
    started = time.monotonic()
    sources = {str(path.resolve()):hashlib.sha256(path.read_bytes()).hexdigest() for path in
        (Path(__file__), Path(mapped.__file__), Path(budget.__file__), Path(original.__file__),
         HERE/'complete_factor_mmap.py', HERE.parent/'block_qr_v2.py')}
    with trace.open('x') as stream:
        stream.write(json.dumps(dict(event='complete_CSR_before_QR_mapping_requested',
            command=command, source_hashes=sources,
            all_original_equations_and_gates_retained=True,
            complete_original_CSR_object_and_entries_retained=True,
            complete_warm_matrix_and_factor_residency_budgeted=True))+'\n')
    previous, previous_wrap = original.BlockQR, original.wrap_factor
    ordinal = 0

    def event(kind, **fields):
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event=kind, elapsed=time.monotonic()-started,
                process_id_for_observation_only=__import__('os').getpid(), **fields), allow_nan=False)+'\n')

    def factor(matrix, n, m, k):
        nonlocal ordinal
        ordinal += 1
        this_ordinal = ordinal
        if ordinal == 1:
            directory.mkdir(exist_ok=False)
            (directory/'owner.json').write_text(json.dumps(owner, indent=2)+'\n')
        estimate_record = json.loads((out/'latest-complete-prefactor-storage-budget.json').read_text())
        estimate = estimate_record['estimate']
        if (estimate_record.get('allowed') is not True or
                (estimate['n'],estimate['nodes'],estimate['parameters']) != (n,m,k)):
            raise MemoryError('The current complete nodal storage budget is not established')
        bound = mapped.full_backing_upper_bound(n,m,k)
        disk = shutil.disk_usage(directory)
        need = bound['total_backing_and_manifest_upper_bytes']+int(options.mmap_disk_margin_mib*mapped.MIB)
        event('complete_CSR_prefactor_constructor_start', ordinal=ordinal,
            memory=budget.memory(), disk_free_bytes=disk.free,
            disk_required_bytes=need, disk_backing_bound=bound)
        if disk.free < need:
            raise MemoryError('Scratch availability changed before complete CSR mapping')

        def recursive_guard(observed_storage):
            # This closure retains only scalar metadata, not factor or matrix.
            retained = (estimate['non_J_baseline_bytes']+
                observed_storage['actual_retained_initial_edge_array_bytes']+
                observed_storage['actual_retained_endpoint_bytes'])
            waited = 0
            while True:
                actual = budget.memory()
                credit = min(actual['current_process_anonymous_RSS_bytes'], retained)
                needed = estimate['process_peak_estimate_bytes']-credit+estimate['external_margin_bytes']
                allowed = actual['available_bytes'] >= needed
                event('actual_mapped_CSR_released_before_recursive_QR_gate',
                    ordinal=this_ordinal, waited_seconds=waited, allowed=allowed,
                    current_memory=actual, actual_storage_observation=observed_storage,
                    observed_anonymous_RSS_credit_bytes=credit,
                    remaining_complete_phase_RAM_required_bytes=needed,
                    logical_mapped_bytes_credited_as_RSS=False)
                if allowed:
                    return
                time.sleep(15)
                waited += 15

        result = mapped.BeforeQRMappedBlockQR(matrix,n,m,k,storage_directory=directory,
            disk_margin_bytes=int(options.mmap_disk_margin_mib*mapped.MIB),
            before_factorization=recursive_guard)
        if result._complete_csr_store.stats.get('last_solve_page_release', {}).get(
                'clean_mapped_pages_advised_DONTNEED') is not True:
            raise MemoryError('The complete CSR release after original QR construction failed')
        event('complete_CSR_and_QR_mapped_return', ordinal=ordinal,
            original_QR_stats=dict(result.stats), CSR_storage=dict(result._complete_csr_store.stats),
            factor_component_storage=dict(result._complete_store.stats),
            composite_CSR_is_mapped_not_anonymous=True,
            frozen_factor_only_component_CSR_location_field_not_applicable=True)
        return result

    def wrap(result, qr_event, identifier):
        wrapped = previous_wrap(result, qr_event, identifier)
        def solve(rhs):
            try:
                answer = wrapped.solve(rhs)
                for store in (result._complete_csr_store, result._complete_store):
                    release = store.stats.get('last_solve_page_release', {})
                    if release.get('clean_mapped_pages_advised_DONTNEED') is not True:
                        raise MemoryError('The complete mapped nonlinear-phase resource condition was not established')
                return answer
            finally:
                event('complete_mapped_solve_return_or_exception', ordinal=identifier,
                    original_QR_stats=dict(result.stats),
                    CSR_storage=dict(result._complete_csr_store.stats),
                    factor_component_storage=dict(result._complete_store.stats),
                    composite_CSR_is_mapped_not_anonymous=True)
        return SimpleNamespace(solve=solve)

    original.BlockQR, original.wrap_factor = factor, wrap
    sys.argv = [str(Path(original.__file__)), *rest]
    try:
        return original.main()
    finally:
        original.BlockQR, original.wrap_factor = previous, previous_wrap
        event('complete_mapped_entry_return_or_exception', complete_factors_requested=ordinal,
              original_math_and_acceptance_changed=False)


if __name__ == '__main__':
    main()
