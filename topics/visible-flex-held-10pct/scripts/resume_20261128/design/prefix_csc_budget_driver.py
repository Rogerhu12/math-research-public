#!/usr/bin/env python3
"""Wait for the full current-mesh budget after its true nodal checkpoint.

The stable V5 checkpoint remains outside this wrapper and writes before the
resource guard. The guard then calls the unchanged complete sys_jac. No RHS,
Jacobian entry, Newton arithmetic, mesh rule, or acceptance gate is changed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
from scipy.integrate import _bvp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prefix_csc_assembly_driver as base
import complete_csc_memory_budget as memory_budget
previous = base.previous


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--memory-baseline-mib", type=float, default=640.)
    parser.add_argument("--memory-misc-mib", type=float, default=64.)
    parser.add_argument("--memory-external-margin-mib", type=float, default=512.)
    options, rest = parser.parse_known_args()
    if "--help" in rest or "-h" in rest:
        sys.argv = [str(Path(base.__file__)), *rest]
        return base.main()
    out = Path(rest[rest.index("--outdir")+1]).resolve()
    log = out.with_name(out.name+"-nodal-memory-budget.jsonl")
    if log.exists():
        raise FileExistsError(log)
    original = _bvp.prepare_sys
    command = list(sys.argv)
    hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
              (Path(__file__).resolve(), Path(base.__file__).resolve(),
               Path(memory_budget.__file__).resolve())}
    count = 0

    def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        col_fun, sys_jac = original(n, m, k, fun, bc, fun_jac, bc_jac, x, h)

        def budgeted(y, p, y_middle, f, f_middle, bc0):
            nonlocal count
            count += 1
            pointer = out/"latest-unaccepted-nodal-checkpoint.json"
            checkpoint = json.loads(pointer.read_text())
            if (checkpoint["nodes"] != m or checkpoint["state_components"] != n
                    or checkpoint["parameters"] != k or checkpoint["accepted_bvp"] is not False):
                raise ValueError("The complete nodal checkpoint must precede the memory guard")
            estimate = memory_budget.budget(n, m, k,
                baseline_mib=options.memory_baseline_mib,
                misc_mib=options.memory_misc_mib,
                external_mib=options.memory_external_margin_mib)
            waited = 0
            while True:
                actual = memory_budget.memory()
                # Credit only the observed RSS within the budgeted baseline;
                # never ignore arbitrary retained old-matrix allocations.
                credit = min(actual["current_process_rss_bytes"],
                             estimate["non_J_baseline_bytes"])
                needed = estimate["process_peak_estimate_bytes"]-credit+estimate["external_margin_bytes"]
                row = dict(event="complete_nodal_resource_gate", ordinal=count,
                    waited_seconds=waited, allowed=actual["available_bytes"] >= needed,
                    estimated_additional_required_bytes=needed,
                    current_baseline_credit_bytes=credit, current_memory=actual,
                    estimate=estimate, checkpoint=checkpoint,
                    actual_command=command, source_hashes=hashes,
                    nonlinear_or_acceptance_gates_changed=False)
                with log.open("a") as stream:
                    stream.write(json.dumps(row, allow_nan=False)+"\n")
                if estimate["process_peak_estimate_bytes"]+estimate["external_margin_bytes"] > actual["total_bytes"]:
                    raise MemoryError("Complete current-mesh budget exceeds available host total")
                if row["allowed"]:
                    return sys_jac(y, p, y_middle, f, f_middle, bc0)
                time.sleep(15)
                waited += 15

        return col_fun, budgeted

    _bvp.prepare_sys = prepare
    sys.argv = [str(Path(base.__file__).resolve()), *rest]
    try:
        return base.main()
    finally:
        _bvp.prepare_sys = original


if __name__ == "__main__":
    main()
