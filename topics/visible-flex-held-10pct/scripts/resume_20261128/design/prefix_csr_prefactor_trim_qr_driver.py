#!/usr/bin/env python3
"""Release unused allocator pages around the original complete mapped solver.

The frozen complete CSR, QR, residual/refinement, original Newton, checkpoint,
single metric audit and acceptance code are retained.  Only the already used
gc/malloc_trim helper is added before a full J baseline and before/after each
complete solve.  No live field, physical cache or numerical array is cleared.
The actual RSS and anonymous RSS before and after each release are recorded.
"""
import hashlib
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prefix_csr_prefactor_qr_driver as original
import prefix_mapped_chord_checkpoint_driver as checkpoint
import prefix_csr_prefactor_budget_trim_driver as trimmed_budget
import complete_factor_mmap as allocator
import complete_prefactor_memory_budget as memory_budget


def main():
    command = list(sys.argv)
    if '--help' in command or '-h' in command:
        return original.main()
    expected = HERE/'prefix_mapped_chord_metric_driver.py'
    selected = Path(command[command.index('--base-driver')+1]).resolve()
    if selected != expected:
        raise ValueError('This narrow release entry requires the declared complete mapped metric driver')
    if (Path(checkpoint.base.__file__).resolve() != HERE/'prefix_csr_prefactor_budget_driver.py'
            or checkpoint.previous is not trimmed_budget.previous):
        raise ValueError('The unchanged complete original loader/budget ownership is not established')
    out = Path(command[command.index('--outdir')+1]).resolve()
    trace = out.with_name(out.name+'-allocator-release.jsonl')
    started = time.monotonic()
    files = (Path(__file__).resolve(), Path(original.__file__).resolve(),
             Path(checkpoint.__file__).resolve(), Path(trimmed_budget.__file__).resolve(),
             Path(allocator.__file__).resolve(), expected)
    hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    with trace.open('x') as stream:
        stream.write(json.dumps(dict(event='unused_allocator_release_entry', scope=__doc__,
            actual_command=command, source_hashes=hashes,
            original_numerical_algorithms_or_acceptance_changed=False))+'\n')

    def release(phase):
        before = memory_budget.memory()
        result = allocator.collect_and_trim()
        after = memory_budget.memory()
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='unused_allocator_pages_release', phase=phase,
                seconds=time.monotonic()-started, before=before, after=after, allocator=result,
                live_caches_or_field_arrays_cleared=False), allow_nan=False)+'\n')

    previous_budget = checkpoint.base
    previous_factor = original.mapped.BeforeQRMappedBlockQR

    class ReleasedMappedFactor(previous_factor):
        def solve(self, rhs):
            release('before_original_complete_solve')
            try:
                return super().solve(rhs)
            finally:
                release('after_original_complete_solve')

    checkpoint.base = trimmed_budget
    original.mapped.BeforeQRMappedBlockQR = ReleasedMappedFactor
    try:
        return original.main()
    finally:
        checkpoint.base = previous_budget
        original.mapped.BeforeQRMappedBlockQR = previous_factor
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='unused_allocator_release_entry_return_or_exception',
                seconds=time.monotonic()-started, owned_hooks_restored=True,
                original_numerical_algorithms_or_acceptance_changed=False))+'\n')


if __name__ == '__main__':
    main()
