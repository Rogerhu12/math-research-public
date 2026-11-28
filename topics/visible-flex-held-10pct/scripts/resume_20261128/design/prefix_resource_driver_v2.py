#!/usr/bin/env python3
"""Original bounded prefix driver plus read-only Fourier table sharing.

The prior live wrapper is imported without editing it.  The only additional
change is the isolated CSR cache: its key binds the actual complete basis and
frequencies, while all mutable diagnostics remain per Flow.  Original source,
input, RHS, Jacobian, Newton and finite acceptance gates still execute.
"""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prefix_resource_driver as previous
import cached_fourier_tables as cache


def main():
    command = list(sys.argv)
    stats = []
    original_loader = previous.load_module

    def load(name, path):
        module = original_loader(name, path)
        if Path(path).name == 'portable_prefix_continue.py':
            old_module_loader = module.module

            def source_module(source_name, source_path):
                loaded = old_module_loader(source_name, source_path)
                if Path(source_path).name == '78718-prefix-fourier-jacobian.py':
                    stats.append(cache.install(loaded))
                return loaded

            module.module = source_module
        return module

    previous.load_module = load
    try:
        previous.main()
    finally:
        if '--outdir' in command:
            out = Path(command[command.index('--outdir') + 1])
            if out.is_dir():
                files = (Path(__file__).resolve(), Path(previous.__file__).resolve(),
                         Path(cache.__file__).resolve())
                result = dict(command=command, source_hashes={str(p):
                    hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                    actual_cache_stats=stats, original_equations_changed=False,
                    original_acceptance_gates_changed=False,
                    geometry_or_response_cached=False, scope=__doc__)
                (out / 'fourier-table-cache.json').write_text(
                    json.dumps(result, indent=2, allow_nan=False) + '\n')


if __name__ == '__main__':
    main()
