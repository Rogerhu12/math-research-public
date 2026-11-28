#!/usr/bin/env python3
"""Original finite design with analytical delta and complete J checkpoints.

The complete original residual, physical boundary, domain tests, mesh scheme
and acceptance gates are preserved.  Only the additive-delta Jacobian column
uses its independently checked analytical expression.  The full nodal state
is saved before each complete Jacobian, to recover from process/resource
interruptions without substituting an unaccepted midpoint field.
"""
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prefix_resource_driver_v4 as base
import analytic_delta_jac_adapter as delta_adapter
import nodal_jac_checkpoint as nodal_checkpoint

previous = base.previous


def main():
    command = list(sys.argv)
    if "--help" in command or "-h" in command:
        return base.main()
    scripts = HERE.parents[1]
    sys.path.insert(0, str(scripts/"resume_m3/round_raw_lib"))
    import analytic_adaptive_core_jac as analytic
    if "--raw-restart" not in command or "--core-module" not in command:
        raise ValueError("V5 requires a complete original raw design initializer and core")
    out = Path(command[command.index("--outdir")+1]).resolve()
    restart = Path(command[command.index("--raw-restart")+1]).resolve()
    with np.load(restart) as raw:
        scales = raw["pscale"].copy()
    files = [Path(__file__).resolve(), Path(delta_adapter.__file__).resolve(),
        HERE.parent/"analytic/material_delta_column.py",
        Path(nodal_checkpoint.__file__).resolve(), Path(base.__file__).resolve(),
        Path(analytic.__file__).resolve(), restart]
    for flag in ("--core-module", "--core-config", "--profile", "--chart", "--port"):
        if flag in command:
            files.append(Path(command[command.index(flag)+1]).resolve())
    hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    original_install = analytic.install
    column_stats = []

    def install(BVP, window=(.5, .9)):
        result = original_install(BVP, window)
        column_stats.append(delta_adapter.install(BVP))
        return result

    analytic.install = install
    checkpoint_stats, restore_checkpoint = nodal_checkpoint.install(out, scales, hashes)
    try:
        return base.main()
    finally:
        restore_checkpoint()
        analytic.install = original_install
        if out.is_dir():
            record = dict(scope=__doc__, actual_command=command,
                source_hashes=hashes, analytical_delta_stats=column_stats,
                full_nodal_checkpoint_stats=checkpoint_stats,
                residuals_boundaries_and_acceptance_gates_changed=False,
                numerical_delta_column_changed=True,
                original_all_state_and_support_columns_retained=True,
                complete_surface=False)
            (out/"analytical-delta-and-nodal-checkpoints.json").write_text(
                json.dumps(record, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
