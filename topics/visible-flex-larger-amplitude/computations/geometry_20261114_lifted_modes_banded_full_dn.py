#!/usr/bin/env python3
"""Original M112 full-DN problem with complete band LU and read-only trials.

The accepted96 source, actual prepared699, true T112 response/J, material
boundary, field/scalar equations and original Newton are unchanged.  Only
the complete linear factor replaces forward nullspace shooting by a row
permutation and pivoted band LU, with same-matrix residual correction.
Every original 17-trial line search and nonlinear acceptance gate remains.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
from pathlib import Path
import sys

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import numpy as np
import scipy.integrate._bvp as backend

import geometry_20261114_lifted_modes_full_dn as continuation
from geometry_20261114_banded_collocation import CompleteBandFactor, sha, write


HERE = Path(__file__).resolve().parent
BASE_DRIVER_SHA = "d885ebc8de5ebd02f006c4104d8b67e856047b4e58f0e125651b38187fb251a5"


def maximum_finite(value):
    value = np.asarray(value)
    return float(np.max(abs(value))) if value.size and np.all(np.isfinite(value)) else None


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run this complete numerical problem in the public Actions")
    if sha(continuation.__file__) != BASE_DRIVER_SHA:
        raise ValueError("The frozen independent-mode original full-DN driver changed")
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--warm", type=Path, required=True)
    args, _ = parser.parse_known_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    context = dict(factors=0, newton_invocations=0, mesh=None, checkpoint=None)
    source_identity = dict(
        entry_file=Path(__file__).name, entry_sha256=sha(__file__),
        complete_band_backend_sha256=sha(HERE / "geometry_20261114_banded_collocation.py"),
        reused_full_DN_driver_sha256=BASE_DRIVER_SHA,
        original_separated_block_builder_sha256=sha(continuation.original.original_qr.__file__),
        original_Newton_sha256=sha(continuation.original.original_solver.__file__),
        input_prepared_sha256=sha(args.warm),
        equation_row_permutation_only=True, unknowns_or_Fourier_modes_removed=False,
        native_tail_changed=False, mathematical_BC_changed=False,
        original_RMS=1e-6, original_BC=1e-11,
        original_17_trial_backtracking_retained=True,
        true_final_native_audit_retained=True,
        linear_accuracy_target_is_not_a_new_nonlinear_acceptance_gate=True)
    write(out / "complete-banded-intent.json", source_identity)
    old_write = continuation.original.write

    def augmented_write(path, data):
        if isinstance(data, dict):
            name = Path(path).name
            if (name in ("driver-status.json", "prepared.json.gz", "actual.json.gz")
                    or name.endswith("-pending.json.gz")):
                data["complete_banded_linear_backend"] = source_identity
        return old_write(path, data)

    continuation.original.write = augmented_write
    old_enable = continuation.original.original_qr.enable
    old_newton = continuation.original.original_solver.released_newton

    def install(output, M, unused_write):
        class RunBandFactor(CompleteBandFactor):
            def __init__(self, n, m, left, right, left_count, work, verify_residual=True):
                context["factors"] += 1
                checkpoint = context["checkpoint"]
                if checkpoint is not None and Path(checkpoint).exists():
                    record = json.loads(gzip.decompress(Path(checkpoint).read_bytes()))
                    record["original_checkpoint_backend_label"] = record.get("linear_backend")
                    record["linear_backend"] = "complete-original-pivoted-banded-LAPACK"
                    record["complete_banded_linear_backend"] = source_identity
                    write(checkpoint, record, True)
                super().__init__(n, m, left, right, left_count, work, verify_residual,
                    report_dir=Path(output) / "banded-linear", field_modes=M,
                    mesh=context["mesh"], factor_index=context["factors"])

        continuation.original.original_qr.DiskQRFactor = RunBandFactor

        def enable(work, left_count, chunk_size=16, checkpoint=None, M=None, N=None):
            context["checkpoint"] = checkpoint
            old_enable(work, left_count, chunk_size, checkpoint, M, N)
            old_prepare = backend.prepare_sys

            def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
                context["mesh"] = np.asarray(x, float).copy()
                return old_prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h)

            backend.prepare_sys = prepare

        continuation.original.original_qr.enable = enable

    continuation.install_qr_diagnostics = install
    trial_log = out / "original-newton-domain-evaluations.jsonl"

    def traced_newton(n, m, h, col_fun, bc, jac, y, p, B, bvp_tol, bc_tol):
        context["newton_invocations"] += 1
        invocation = context["newton_invocations"]
        evaluation = 0
        pending = None
        mesh = np.asarray(context["mesh"], float)

        def col(values, parameters):
            nonlocal evaluation, pending
            result = col_fun(values, parameters)
            residual, middle, nodal_rhs, middle_rhs = result
            evaluation += 1
            bad_nodes = np.flatnonzero(~np.all(np.isfinite(nodal_rhs), axis=0))
            bad_middle = np.flatnonzero(~np.all(np.isfinite(middle_rhs), axis=0))
            pending = dict(
                newton_invocation=invocation, residual_evaluation=evaluation, nodes=m,
                evaluation_kind="initial iterate" if evaluation == 1 else "original Newton trial",
                original_equations_evaluated_without_modification=True,
                original_collocation_residual_finite=bool(np.all(np.isfinite(residual))),
                original_collocation_residual_max=maximum_finite(residual),
                invalid_node_count=len(bad_nodes), invalid_nodes=bad_nodes.tolist(),
                invalid_node_s=mesh[bad_nodes].tolist(),
                invalid_midpoint_count=len(bad_middle), invalid_midpoint_intervals=bad_middle.tolist(),
                invalid_midpoint_s=(.5*(mesh[:-1]+mesh[1:]))[bad_middle].tolist(),
                augmented_state_max=maximum_finite(values),
                complete_input_state_finite=bool(np.all(np.isfinite(values))),
                nonlinear_acceptance_test_changed=False)
            return result

        def boundary(left, right, parameters):
            result = bc(left, right, parameters)
            if pending is not None:
                pending.update(
                    original_boundary_finite=bool(np.all(np.isfinite(result))),
                    original_boundary_residual_max=maximum_finite(result),
                    invalid_boundary_rows=np.flatnonzero(~np.isfinite(result)).tolist())
                with trial_log.open("a") as stream:
                    stream.write(json.dumps(pending, allow_nan=False) + "\n")
            return result

        # This calls the frozen function directly.  Its loop, trial count,
        # step norm, Armijo expression, tolerances and return are untouched.
        return old_newton(n, m, h, col, boundary, jac, y, p, B, bvp_tol, bc_tol)

    continuation.original.original_solver.released_newton = traced_newton
    return continuation.main()


if __name__ == "__main__":
    raise SystemExit(main())
