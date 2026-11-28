#!/usr/bin/env python3
"""Complete original CSR/QR design with exception-safe Flow release.

Delegates to the frozen full-CSR entry. Only its memory estimator and the
freshly loaded radial collection wrappers are replaced by independent
successors. All original values, exceptions, equations, numerical gates,
complete nodal checkpoints, and literal recovery semantics are retained.
"""
import hashlib
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prefix_csr_budget_driver as base
import complete_csr_memory_budget_v2 as budget
import exception_safe_radial_batches as lifecycle

previous = base.previous


def main():
    command = list(sys.argv)
    if '--help' in command or '-h' in command:
        return base.main()
    out = Path(command[command.index('--outdir')+1]).resolve()
    trace = out.with_name(out.name+'-flow-lifecycle.jsonl')
    files = (Path(__file__).resolve(), Path(base.__file__).resolve(),
             Path(budget.__file__).resolve(), Path(budget.previous.__file__).resolve(),
             Path(lifecycle.__file__).resolve())
    hashes = {str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    started = time.monotonic()
    with trace.open('x') as stream:
        stream.write(json.dumps(dict(event='exception_safe_collection_installed',
            actual_command=command, source_hashes=hashes,
            all_original_values_exceptions_and_gates_retained=True,
            live_caches_cleared=False), allow_nan=False)+'\n')

    def event(row):
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(elapsed=time.monotonic()-started,
                                         lifecycle=row), allow_nan=False)+'\n')

    stats, restore = lifecycle.install(previous, event)
    old_budget = base.memory_budget
    base.memory_budget = budget
    try:
        return base.main()
    finally:
        base.memory_budget = old_budget
        restore()
        if out.is_dir():
            record = dict(scope=__doc__, actual_command=command, source_hashes=hashes,
                radial_lifecycle_statistics=stats,
                retained_factor_and_nonlinear_overlap_budgeted=True,
                original_math_and_acceptance_changed=False,
                real_signal_termination_cause_inferred=False,
                accepted_field_claimed=False)
            (out/'exception-safe-flow-lifecycle.json').write_text(
                json.dumps(record, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
