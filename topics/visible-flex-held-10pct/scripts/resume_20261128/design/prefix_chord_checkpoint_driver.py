#!/usr/bin/env python3
"""Original CSR/lifecycle/V5 design with complete accepted-step checkpoints.

Delegates to the frozen full-matrix driver. The independent checkpoint changes
only persistence after an original accepted Newton tuple assignment. Original
residuals, all columns, linear solves, merit/mesh rules and gates are retained.
"""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prefix_csr_budget_driver_v2 as base
import accepted_newton_nodal_checkpoint as accepted_checkpoint

previous = base.previous


def main():
    command = list(sys.argv)
    if '--help' in command or '-h' in command:
        return base.main()
    out = Path(command[command.index('--outdir')+1]).resolve()
    raw = Path(command[command.index('--raw-restart')+1]).resolve()
    with np.load(raw) as archive:
        scales = archive['pscale'].copy()
    portable = HERE.parents[1]/'resume_m3/portable_prefix_continue.py'
    files = (Path(__file__).resolve(), Path(base.__file__).resolve(),
             Path(accepted_checkpoint.__file__).resolve(), raw)
    hashes = {str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    original_loader = previous.load_module
    statistics = []

    def load(name, filename):
        module = original_loader(name, filename)
        if Path(filename).resolve() != portable:
            return module
        original_solve = module.solve_bvp

        def solve(fun, bc, x, y, p, **kwargs):
            import f6curve_domain_newton as domain
            hashes[str(Path(domain.__file__).resolve())] = hashlib.sha256(
                Path(domain.__file__).read_bytes()).hexdigest()
            stats, restore = accepted_checkpoint.install(domain, out, scales, hashes)
            statistics.append(stats)
            record = dict(scope=__doc__, actual_command=command, source_hashes=hashes,
                          original_math_and_acceptance_changed=False,
                          whole_BVP_acceptance_claimed=False, solves=statistics)
            (out/'accepted-newton-checkpoint-execution.json').write_text(
                json.dumps(record, indent=2, allow_nan=False)+'\n')
            try:
                return original_solve(fun, bc, x, y, p, **kwargs)
            finally:
                restore()
                (out/'accepted-newton-checkpoint-execution.json').write_text(
                    json.dumps(record, indent=2, allow_nan=False)+'\n')

        module.solve_bvp = solve
        return module

    previous.load_module = load
    try:
        return base.main()
    finally:
        previous.load_module = original_loader


if __name__ == '__main__':
    main()
