#!/usr/bin/env python3
"""Build an explicitly unaccepted same-g initializer from a real nodal checkpoint.

Every saved x, y, p and pscale element is retained bitwise. The original RHS
at those exact nodes supplies only the derivative of the initial Hermite
cubic. No grid inference, interpolation of state values, inlet correction,
parameter transport, full Jacobian, or nonlinear solve is performed here.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.interpolate import CubicHermiteSpline

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fixed_support_literal_model as literal

STATUS = "unaccepted_fixed_support_complete_nodal_recovery_initializer"
FIXED_KEYS = ("frozen_profile", "physical_tail_parameters", "physical_tail_cut",
              "angular_chart", "core_settings", "gauge_q", "warp_reference",
              "q_branch", "mean_nodes", "bc_normalization", "terminal_kind",
              "frozen_literal_radial_chart", "frozen_source_signature")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same_bits(a, b):
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def checked_source_chain(donor_path, donor):
    """Trace actual record hashes to a genuinely accepted fixed-g raw return."""
    chain, seen = [], set()
    path, record = donor_path, donor
    while True:
        if path in seen:
            raise ValueError("Cyclic interrupted-source provenance")
        seen.add(path)
        if (record.get("model_kind") != literal.KIND
                or record.get("fixed_metric") is not True
                or any(record[key] != donor[key] for key in FIXED_KEYS)):
            raise ValueError("The interrupted-source chain changes the fixed physical problem")
        accepted = (record.get("solver_success") is True
                    and record.get("finite_linear_candidate_pass") is True)
        chain.append(dict(path=str(path), sha256=sha(path), actually_accepted=accepted))
        if accepted:
            raw = path.parent/record["raw_return"]["file"]
            physical = path.parent/"physical.npz"
            if (sha(raw) != record["raw_return"]["sha256"]
                    or sha(physical) != record["physical_sha256"]):
                raise ValueError("The genuine accepted fixed-g source field changed")
            return chain, path, record, raw
        if (record.get("actual_solve_invoked") is not True
                or record.get("solver_success") is not False
                or record.get("finite_linear_candidate_pass") is not False
                or record.get("raw_return")):
            raise ValueError("Each unaccepted donor must be an actual interrupted solve without a raw return")
        parent = Path(record["source_run"]).resolve()
        if sha(parent) != record["source_run_sha256"]:
            raise ValueError("An interrupted donor's actual input record changed")
        path, record = parent, json.loads(parent.read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--donor-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--rhs-block", type=int, default=64)
    args = parser.parse_args()
    if args.rhs_block < 1:
        raise ValueError("A positive original RHS batch is required")
    started = time.monotonic()
    donor_path = args.donor_run.resolve()
    run = json.loads(donor_path.read_text())
    if (run.get("status") != "running_original_fixed_support_BVP"
            or run.get("actual_solve_invoked") is not True
            or run.get("solver_success") is not False
            or run.get("finite_linear_candidate_pass") is not False
            or run.get("raw_return")):
        raise ValueError("Require the honest interrupted fixed-support process")
    terminal_path = donor_path.parent/"actual-process-terminal.json"
    terminal = json.loads(terminal_path.read_text())
    if (Path(terminal["run"]).resolve() != donor_path
            or terminal["run_sha256"] != sha(donor_path)
            or terminal.get("observed_exit_code") != 137
            or terminal.get("complete_solver_raw_available") is not False
            or terminal.get("accepted_source_promoted") is not False):
        raise ValueError("The actual interrupted process terminal record is missing or changed")
    checkpoint_metadata_path = donor_path.parent/"last-nodal-jac-input.json"
    checkpoint_metadata = json.loads(checkpoint_metadata_path.read_text())
    checkpoint_path = donor_path.parent/checkpoint_metadata["file"]
    recorded = terminal["latest_complete_nodal_checkpoint"]
    if (checkpoint_metadata.get("status") != "unaccepted_complete_nodal_before_original_J"
            or checkpoint_metadata.get("accepted_bvp") is not False
            or checkpoint_metadata.get("full_nodal_endpoints_present") is not True
            or checkpoint_metadata["sha256"] != sha(checkpoint_path)
            or recorded["sha256"] != sha(checkpoint_path)
            or recorded["metadata_sha256"] != sha(checkpoint_metadata_path)
            or Path(recorded["path"]).resolve() != checkpoint_path.resolve()
            or Path(checkpoint_metadata["source_run"]).resolve() != Path(run["source_run"]).resolve()
            or checkpoint_metadata["source_run_sha256"] != run["source_run_sha256"]
            or checkpoint_metadata["frozen_profile"] != run["frozen_profile"]
            or checkpoint_metadata["mean_nodes"] != run["mean_nodes"]):
        raise ValueError("The complete nodal checkpoint does not belong to this actual process/input")
    chain, accepted_path, accepted, accepted_raw = checked_source_chain(donor_path, run)
    with np.load(checkpoint_path, allow_pickle=False) as raw:
        saved = {key:raw[key].copy() for key in ("x", "y", "p", "pscale")}
    x, y, p, scales = (saved[key] for key in ("x", "y", "p", "pscale"))
    if (len(x) != checkpoint_metadata["nodes"] or x[0] != 0. or x[-1] != 1.
            or not np.all(np.diff(x) > 0)
            or any(not np.all(np.isfinite(value)) for value in saved.values())):
        raise ValueError("The retained complete nodal data are malformed")
    with np.load(accepted_raw, allow_pickle=False) as raw:
        accepted_nodes = raw["x"].copy()
    if not np.all(np.isin(accepted_nodes, x)):
        raise ValueError("The actual nodal checkpoint dropped an accepted adaptive knot")
    args.outdir.mkdir(parents=True, exist_ok=False)
    obj = literal.load_model(dict(source_run=str(donor_path)))
    if (not obj.fixed or y.shape != (obj.n, len(x)) or p.shape != (obj.M,)
            or not same_bits(scales, obj.pscale)
            or obj.M != run["modes"] or obj.nt != run["angular"]
            or literal.chart_record(obj) != run["frozen_literal_radial_chart"]
            or obj.q != run["gauge_q"] or obj.warp_q != run["warp_reference"]
            or obj.cfg != run["frozen_profile"]):
        raise ValueError("The original fixed-g model, full dimensions, or literal chart changed")
    obj.initial(p)
    memo_path = HERE.parent/"design/material_core_evaluate_cache.py"
    memo = module("_fixed_nodal_recovery_core_memo", memo_path)
    memo_stats = memo.install(type(obj._core))
    rhs = np.empty_like(y)
    for start in range(0, len(x), args.rhs_block):
        sl = slice(start, start+args.rhs_block)
        rhs[:, sl] = obj.fun(x[sl], y[:, sl], p)
    if not np.all(np.isfinite(rhs)):
        raise FloatingPointError("The original nodal RHS is nonfinite")
    cubic = CubicHermiteSpline(x, y, rhs, axis=1, extrapolate=False)
    bc = obj.bc(y[:, 0], y[:, -1], p)
    initial_path = args.outdir/"initial.npz"
    np.savez_compressed(initial_path, **saved, cubic_c=cubic.c, cubic_x=cubic.x)
    with np.load(initial_path, allow_pickle=False) as raw:
        preserved = {key:same_bits(value, raw[key]) for key, value in saved.items()}
    if not all(preserved.values()):
        raise ValueError("The complete nodal initializer changed a saved input bit")
    report = dict(status=STATUS, scope=__doc__, source_sha256=sha(__file__),
        donor_run=str(donor_path), donor_run_sha256=sha(donor_path),
        donor_checkpoint=str(checkpoint_path), donor_checkpoint_sha256=sha(checkpoint_path),
        donor_checkpoint_metadata=str(checkpoint_metadata_path),
        donor_checkpoint_metadata_sha256=sha(checkpoint_metadata_path),
        donor_terminal=str(terminal_path), donor_terminal_sha256=sha(terminal_path),
        donor_checkpoint_kind="complete_original_nodal_state",
        donor_was_accepted=False, donor_complete_nodal_return_available=False,
        complete_nodal_checkpoint_available=True, actual_source_chain=chain,
        genuine_accepted_source=str(accepted_path),
        genuine_accepted_source_sha256=sha(accepted_path),
        genuine_accepted_raw_sha256=sha(accepted_raw),
        initial_file=str(initial_path.resolve()), initial_sha256=sha(initial_path),
        fixed_problem={key:run[key] for key in FIXED_KEYS}, modes=obj.M, angular=obj.nt,
        all_state_components=obj.n, all_parameters=obj.M, all_parameter_scales=len(scales),
        original_nodal_arrays_preserved_bitwise=preserved,
        initial_nodes=len(x), minimum_initial_spacing=float(np.min(np.diff(x))),
        genuine_source_nodes=len(accepted_nodes), genuine_source_nodes_preserved_bitwise=True,
        chart_break_max_nearest_node_distance=float(max(min(abs(x-v)) for v in obj.chart_breaks)),
        original_nodal_rhs_evaluated=True, original_nodal_rhs_block=args.rhs_block,
        cubic_derivatives_defined_by_original_nodal_rhs=True,
        cubic_is_unaccepted_initial_guess_only=True, nodal_state_interpolated_or_modified=False,
        parameters_rescaled_or_modified=False, grid_inferred_or_modified=False,
        original_inlet_correction_applied=False,
        initial_q_actual=float(obj.support_amplitude),
        initial_BC_max=float(np.max(np.abs(bc))),
        nodal_original_domain_checked=True, complete_RMS_off_midpoint_domain_checked=False,
        complete_metric_audit_executed=False, complete_core_evaluate_memo=memo_stats,
        dependencies={str(path):sha(path) for path in
            (HERE/"fixed_support_literal_model.py", memo_path)},
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        full_J_assembled=False, nonlinear_solver_invoked=False, accepted_bvp=False,
        complete_surface=False, elapsed_seconds=time.monotonic()-started)
    (args.outdir/"initial-recovery.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("status", "initial_nodes", "initial_q_actual",
        "initial_BC_max", "original_nodal_arrays_preserved_bitwise", "maximum_rss_kib",
        "elapsed_seconds")}), flush=True)


if __name__ == "__main__":
    main()
