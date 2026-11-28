#!/usr/bin/env python3
"""Inherited complete QR arithmetic with factor-only scratch-backed storage.

The stable original QR entry still owns its complete factor/solve integration.
Its constructor provider alone now creates the independently checked mapped
factor. The original full matrix stays anonymous and every original equation,
direction diagnostic and nonlinear gate remains in force. Only factor-only
mode is enabled here; full CSR mapping was not exercised by the actual check.
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
import complete_factor_mmap as mapped
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
    # This directory identifies the sole child's temporary execution storage.
    # Its owner file permits the joined parent to remove a SIGKILL orphan.
    if directory.exists():
        raise FileExistsError(directory)
    owner = dict(kind='owned_complete_QR_factor_only_scratch_storage',
        actual_child_outdir=str(out), process_id_for_observation_only=__import__('os').getpid(),
        entry_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        helper_sha256=hashlib.sha256(Path(mapped.__file__).read_bytes()).hexdigest(),
        temporary_reproducible_execution_storage=True, accepted_field=False)
    trace = out.with_name(out.name+'-mapped-factor.jsonl')
    command = list(sys.argv)
    started = time.monotonic()
    with trace.open('x') as stream:
        stream.write(json.dumps(dict(event='factor_only_mapping_requested',
            command=command, source_hashes={str(path.resolve()):
                hashlib.sha256(path.read_bytes()).hexdigest() for path in
                (Path(__file__), Path(mapped.__file__), Path(original.__file__),
                 HERE.parent/'block_qr_v2.py')}, original_construction_peak_unchanged=True,
            map_scope='factor-only', all_original_equations_and_gates_retained=True))+'\n')
    previous = original.BlockQR
    previous_wrap = original.wrap_factor
    ordinal = 0

    def event(kind, **fields):
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event=kind, elapsed=time.monotonic()-started,
                                         **fields), allow_nan=False)+'\n')

    def factor(matrix, n, m, k):
        nonlocal ordinal
        ordinal += 1
        if ordinal == 1:
            # The original portable entry owns creation of outdir. Do not
            # precreate it before its original exist_ok=False check.
            directory.mkdir(exist_ok=False)
            (directory/'owner.json').write_text(json.dumps(owner, indent=2)+'\n')
        bound = mapped.backing_upper_bound(n,m,k,'factor-only')
        disk = shutil.disk_usage(directory)
        need = bound['total_backing_and_manifest_upper_bytes']+int(options.mmap_disk_margin_mib*mapped.MIB)
        event('complete_factor_constructor_start', ordinal=ordinal,
            memory=mapped.memory(), disk_free_bytes=disk.free,
            disk_required_bytes=need, disk_backing_bound=bound)
        if disk.free < need:
            raise MemoryError('Scratch availability changed before the complete QR constructor')
        result = mapped.MappedBlockQR(matrix,n,m,k,storage_directory=directory,
            disk_margin_bytes=int(options.mmap_disk_margin_mib*mapped.MIB), map_scope='factor-only')
        event('complete_factor_mapped_return', ordinal=ordinal,
            original_QR_stats=dict(result.stats), mapped_storage=dict(result._complete_store.stats))
        return result

    def wrap(result, qr_event, identifier):
        wrapped = previous_wrap(result, qr_event, identifier)

        def solve(rhs):
            try:
                answer = wrapped.solve(rhs)
                release = result._complete_store.stats.get('last_solve_page_release', {})
                if release.get('clean_mapped_pages_advised_DONTNEED') is not True:
                    raise MemoryError('The mapped-factor nonlinear-phase resource condition was not established')
                return answer
            finally:
                event('mapped_complete_solve_return_or_exception', ordinal=identifier,
                    original_QR_stats=dict(result.stats),
                    mapped_storage=dict(result._complete_store.stats))

        # One-way ownership only; result.solve is never overwritten.
        return SimpleNamespace(solve=solve)

    original.BlockQR = factor
    original.wrap_factor = wrap
    sys.argv = [str(Path(original.__file__)), *rest]
    try:
        return original.main()
    finally:
        original.BlockQR = previous
        original.wrap_factor = previous_wrap
        event('mapped_entry_return_or_exception', complete_factors_requested=ordinal,
              original_math_and_acceptance_changed=False)


if __name__ == '__main__':
    main()
