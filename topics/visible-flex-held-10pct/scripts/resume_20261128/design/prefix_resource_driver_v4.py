#!/usr/bin/env python3
"""Original resource driver with exact-input R53 integral memoization.

This independent entry retains v2's read-only Fourier tables and v3's declared
radial block selection.  The added core evaluator cache binds the complete
actual core state and theta bytes, restores original cache side effects, and
never exposes its stored arrays for mutation.  Every original residual,
Jacobian column, domain test, Newton rule and finite audit is retained.
"""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prefix_resource_driver_v2 as base
import material_core_evaluate_cache as cache

# The full block-QR wrapper can intercept this same original portable loader.
previous = base.previous


def main():
    requested = list(sys.argv)
    if '--rhs-block' not in sys.argv and '--modes' in sys.argv:
        modes = int(sys.argv[sys.argv.index('--modes')+1])
        block = 64 if modes <= 16 else 32 if modes <= 24 else 16 if modes <= 32 else 8
        sys.argv[1:1] = ['--rhs-block', str(block)]
    effective = list(sys.argv)
    stats, source_files = [], set()
    original_loader = previous.load_module

    def load(name, path):
        module = original_loader(name, path)
        if Path(path).name == 'portable_prefix_continue.py':
            old_module_loader = module.module

            def source_module(source_name, source_path):
                loaded = old_module_loader(source_name, source_path)
                if Path(source_path).name == 'material_support_factory.py':
                    cls = loaded.MaterialFlattenedSupportCore
                    stats.append(cache.install(cls))
                    source_files.add(Path(source_path).resolve())
                    source_files.add(Path(sys.modules[cls.__module__].__file__).resolve())
                return loaded

            module.module = source_module
        return module

    previous.load_module = load
    try:
        return base.main()
    finally:
        if '--outdir' in effective:
            out = Path(effective[effective.index('--outdir')+1])
            if out.is_dir():
                source_files.update((Path(__file__).resolve(), Path(cache.__file__).resolve(),
                    Path(base.__file__).resolve(), Path(previous.__file__).resolve()))
                record = dict(scope=__doc__, requested_command=requested,
                    effective_command=effective, source_hashes={str(p):
                        hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(source_files)},
                    actual_core_cache_stats=stats,
                    original_equations_changed=False, original_quadrature_changed=False,
                    original_acceptance_gates_changed=False,
                    interpolated_or_rounded_key=False,
                    cached_physical_response_only_reused_on_identical_full_input=True)
                (out/'material-core-evaluate-cache.json').write_text(
                    json.dumps(record, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
