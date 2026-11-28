#!/usr/bin/env python3
"""A complete, unaccepted boundary-only DN initializer from the R85 response basis.

The saved old matrix may be a frozen chord matrix.  All original unknowns are
updated in the exactly shared computational grid and parameter units.  This
is not a complete Newton step: the whole source F_L remains an explicit debt.
No physical RHS, native solve, BVP, metric or physical-H audit is performed.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import shutil
import struct
import sys
import time
import traceback

import numpy as np
from scipy.sparse import load_npz

SOURCE = Path(__file__).resolve()
REPO = SOURCE.parents[5]
SCRIPTS = REPO / "topics/visible-flex-held-10pct/scripts"
sys.path.insert(0, str(SOURCE.parent))
sys.path.insert(0, str(SCRIPTS / "resume_20261126"))
sys.path.insert(0, str(SCRIPTS / "resume_20261128/tail"))

import complete_terminal_response_basis as basis
import material_design_secant_predictor as original
import verified_tail_response_memo as memo

EXPECTED_BASIS_BLOB = "ba36afd8b792b730e2372e5d227a97995fe7db88"
EXPECTED_ACCEPTANCE_BLOB = "283f80548c5565e61e7ea394ce5bf8c380c45d6c"
EXPECTED_MEMO_BLOB = "325b8f9802de67481d315e6508c3c137db189327"
BASELINE = REPO / ("topics/visible-flex-held-10pct/notes/"
                   "2026-11-28-analytic-material-tangent-observed.json")
EXPECTED_BASELINE_BLOB = "c386fea00a85084f5b7cb01e6c1b8d573741f4f9"


def read(path):
    return json.loads(Path(path).read_text())


def bound(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=basis.sha(path))


def check_blob(path, expected):
    if basis.git_blob_sha(Path(path).read_bytes()) != expected:
        raise ValueError("A literal reviewed source/evidence blob changed: " + str(path))


def same_array_bytes(left, right):
    left, right = np.asarray(left), np.asarray(right)
    return (left.shape == right.shape and left.dtype.str == right.dtype.str
            and left.tobytes(order="C") == right.tobytes(order="C"))


def same_float(left, right):
    return struct.pack("<d", float(left)) == struct.pack("<d", float(right))


def ratio(value):
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def literal_small_inverse_certificate(matrix, inverse):
    """Exact dyadic check for the literal stored small matrix, not the full J."""
    if (matrix.shape != inverse.shape or matrix.shape[0] != matrix.shape[1]
            or not np.all(np.isfinite(matrix)) or not np.all(np.isfinite(inverse))):
        raise ValueError("The literal small matrix/inverse is not finite and square")
    m = len(matrix)
    ss = [[Fraction.from_float(float(v)) for v in row] for row in matrix]
    tt = [[Fraction.from_float(float(v)) for v in row] for row in inverse]
    eta = max(sum(abs(Fraction(i == j) - sum(tt[i][k]*ss[k][j]
                   for k in range(m))) for j in range(m)) for i in range(m))
    norm_t = max(sum(abs(v) for v in row) for row in tt)
    norm_s = max(sum(abs(v) for v in row) for row in ss)
    result = dict(
        object="Only the supplied literal rounded small terminal-forcing matrix",
        exact_rational_residual=ratio(eta), less_than_one=eta < 1,
        full_original_J_inverse_certified=False,
        current_physical_derivative_certified=False,
        complete_response_errors_enclosed=False,
    )
    if eta < 1:
        result["inverse_norm_inf_upper"] = ratio(norm_t/(1-eta))
        result["condition_inf_upper"] = ratio(norm_s*norm_t/(1-eta))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--basis-report", type=Path, required=True)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--memo-proof", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--step-scale", type=float, default=1.)
    parser.add_argument("--minimum-available-mib", type=float, default=768.)
    args = parser.parse_args()
    if (not math.isfinite(args.step_scale) or not 0 < args.step_scale <= 1
            or not math.isfinite(args.minimum_available_mib)
            or args.minimum_available_mib <= 0):
        raise ValueError("Use an explicit finite positive step and memory estimate")
    out = args.outdir.resolve()
    if out == REPO or REPO in out.parents:
        raise ValueError("The complete unaccepted initializer must remain outside git")
    out.mkdir(parents=True, exist_ok=False)
    destination = out / "initializer.json"
    state = dict(
        scope=__doc__, status="checking_actual_inputs", entry=bound(SOURCE),
        BVP_solved=False, native_tail_solve=False, physical_RHS_evaluated=False,
        original_full_domain_checked=False, original_RMS_gate_passed=False,
        metric_gate_passed=False, physical_H_audited=False,
        accepted_field=False, fixed_metric_refinement=False,
        complete_Newton_step=False, complete_surface=False,
    )
    basis.save(destination, state)
    started = time.monotonic()
    try:
        for path, expected in (
            (basis.SOURCE, EXPECTED_BASIS_BLOB),
            (Path(original.__file__), EXPECTED_ACCEPTANCE_BLOB),
            (Path(memo.__file__), EXPECTED_MEMO_BLOB),
            (BASELINE, EXPECTED_BASELINE_BLOB),
        ):
            check_blob(path, expected)
        check_blob(basis.EVIDENCE, basis.EVIDENCE_BLOB)
        comparison = read(basis.EVIDENCE)["comparison"]
        br_path = args.basis_report.resolve()
        br_reference = bound(br_path)
        br = read(br_path)
        ident = br["identity"]
        if (br.get("status") != "complete_matrix_response_basis_returned"
                or br.get("complete_columns") != 24
                or br.get("entry_sha256") != basis.sha(basis.SOURCE)
                or ident["evidence_git_blob_sha1"] != basis.EVIDENCE_BLOB
                or ident["matrix"]["sha256"] != comparison["actual_direct_matrix_sha256"]
                or ident["matrix_input"]["sha256"] != comparison["snapshot_sha256"]
                or ident["origin_design_run"]["sha256"] != comparison["source_run_sha256"]):
            raise ValueError("The complete actual response-basis identity differs")
        for item in (ident["matrix"], ident["matrix_input"], ident["origin_design_run"],
                     ident["factor_source"]):
            if bound(item["path"]) != item:
                raise ValueError("A source bound by the actual response basis changed")
        run_path = args.source_run.resolve()
        if bound(run_path) != ident["origin_design_run"]:
            raise ValueError("The target is not the same original design definition")
        # Keep the existing strict source acceptance; never label the predictor
        # itself as an accepted source or alter the old portable run.
        record, raw = original.accepted_original(run_path, REPO)
        n, nodes, modes, dimension = (ident[k] for k in
                                     ("n", "nodes", "parameters", "dimension"))
        if (n, nodes, modes, dimension) != (73, 879, 24, 64191):
            raise ValueError("This narrow initializer requires the actual full M24 basis")
        if (record["modes"] != modes or not same_float(ident["gauge_q"], record["gauge_q"])
                or ident["sigma"] != -1):
            raise ValueError("The source gauge or exact state convention differs")
        with np.load(ident["matrix_input"]["path"], allow_pickle=False) as saved:
            snapshot = {k: saved[k].copy() for k in ("x", "y", "p", "pscale")}
        for key in ("x", "pscale"):
            if not same_array_bytes(snapshot[key], raw[key]):
                raise ValueError("The full computational mesh/parameter units differ: " + key)
        if (snapshot["y"].shape != raw["y"].shape or snapshot["p"].shape != raw["p"].shape
                or snapshot["y"].dtype.str != raw["y"].dtype.str
                or snapshot["p"].dtype.str != raw["p"].dtype.str
                or not np.all(np.isfinite(snapshot["y"]))
                or not np.all(np.isfinite(snapshot["p"]))):
            raise ValueError("The complete unknown coordinates do not match")
        if not same_array_bytes(raw["pscale"], np.asarray(record["parameter_scales"], dtype="<f8")):
            raise ValueError("The declared original physical support scales differ")
        same_point = (same_array_bytes(snapshot["y"], raw["y"])
                      and same_array_bytes(snapshot["p"], raw["p"]))
        physical_chart_point_same = same_float(snapshot["p"][0], raw["p"][0])
        state["coordinate_identity"] = dict(
            complete_computational_mesh_bytes_identical=True,
            complete_parameter_scale_bytes_identical=True,
            state_order="All [R0,R1..RM,T1..TM,Z1..ZM] at each original t, then all p",
            parameter_zero_meaning="original additive physical delta increment",
            same_point=same_point,
            same_literal_profile_chart_core_port_definitions=True,
            same_gauge_warp_and_original_mean_rule=True,
            source_mean_nodes=record["prefix_audit"]["samples_psi"],
            computational_chart_definition_bound_by_same_original_command_and_input_hashes=True,
            chart_parameter_at_evaluation_point_identical=physical_chart_point_same,
            physical_s_at_two_points_claimed_equal=physical_chart_point_same,
            old_matrix_delta=record["physical_profile"]["delta"]+float(snapshot["p"][0]),
            target_source_delta=record["physical_profile"]["delta"]+float(raw["p"][0]),
            matrix_role=("same_nodal_point_declared_original_numerical_matrix" if same_point
                         else "old_point_complete_frozen_chord_matrix"),
        )
        del snapshot
        old_proof_path = args.memo_proof.resolve()
        old_proof_reference = bound(old_proof_path)
        old_proof = read(old_proof_path)
        manifest_path = memo.checked(old_proof["current_native_manifest"])
        native_root = Path(read(manifest_path)["source_topic"]).resolve()
        proof, packet = memo.build_proof(
            memo.checked(old_proof["source_summary"]),
            memo.checked(old_proof["current_config"]),
            manifest_path, native_root / "repro/source-root", REPO)
        if proof != old_proof:
            raise ValueError("The original complete full-H/J/audit memo proof changed")
        sigma, gauge = ident["sigma"], float(ident["gauge_q"])
        height_columns = ident["height_columns"]
        expected_height_columns = [n*(nodes-1)+2*modes+1, n*nodes]
        if (height_columns != expected_height_columns
                or ident["terminal_rows"] != [dimension-modes, dimension]):
            raise ValueError("The physical trace/terminal row selectors changed")
        h0 = sigma*gauge*raw["y"][2*modes+1:, -1]
        request = packet["request"]
        if (not same_array_bytes(np.asarray(request["height"], dtype="<f8"), h0)
                or not same_array_bytes(np.asarray(record["raw_return"]["candidate_H"], dtype="<f8"), h0)):
            raise ValueError("The full actual tail request differs from the accepted source raw H")
        port = read(original.option(record, "--port"))
        response = packet["response"]
        if (packet["config"]["modes"] != modes or packet["config"]["spacing"] != 3
                or any(packet["config"].get(k) != v for k, v in port["parameters"].items())):
            raise ValueError("The true response belongs to a different physical tail")
        E = float(port["cut"]["E"])
        if not math.isfinite(E) or E <= 0:
            raise ValueError("The original physical port E must remain positive")
        weights = np.full(modes, record["gates"]["physical_bc_tol"]/record["gates"]["bc_tol"])
        linear = np.asarray(port["linearSlope"], dtype=np.float64)
        slope = np.asarray(response["jets"]["slope"], dtype=np.float64)
        jets = np.asarray(response["heightJetJacobian"], dtype=np.float64)
        if (linear.shape != (modes,) or slope.shape != (modes,)
                or jets.shape != ((3*modes+2)*modes,)
                or not np.all(np.isfinite(linear)) or not np.all(np.isfinite(slope))
                or not np.all(np.isfinite(jets)) or not np.all(weights > 0)):
            raise ValueError("The complete original slope/Jacobian convention changed")
        Tj = jets.reshape((3*modes+2, modes))[:modes]
        g = -(slope-linear*h0)/(math.sqrt(E)*weights)
        G = -(Tj-np.diag(linear))/(math.sqrt(E)*weights[:, None])
        state["tail_binding"] = dict(
            prior_proof=old_proof_reference, source_packet=proof["source_packet"],
            complete_H_bytes_identical=True, height_J_count=proof["height_J_count"],
            complete_unknown_count=proof["complete_unknown_count"],
            original_full_H_J_audit_proof_rechecked_read_only=True,
            fresh_native_solve_performed=False, trace_role="raw H for an unaccepted initializer",
            final_physical_H_not_substituted=True,
        )
        columns = br["columns"]
        if sorted(row["column"] for row in columns) != list(range(modes)):
            raise ValueError("Every original terminal response must be present exactly once")
        available = basis.available_memory()
        state["prelaunch_estimate"] = dict(
            available_memory_bytes=available,
            minimum_available_bytes=int(args.minimum_available_mib*1024**2),
            disk_free_bytes=shutil.disk_usage(out).free,
            estimated_gate_not_a_guarantee=True, full_factor_not_constructed=True,
            automatic_wait_or_spawn_used=False,
        )
        basis.save(destination, state)
        if (available < int(args.minimum_available_mib*1024**2)
                or shutil.disk_usage(out).free < 16*1024**2):
            raise MemoryError("The explicit one-shot initializer resource estimate did not pass")
        V = np.empty((dimension, modes), dtype=np.float64, order="F")
        residuals = np.empty(modes)
        basis_dir = br_path.parent
        for row in sorted(columns, key=lambda item: item["column"]):
            j = row["column"]
            path = basis_dir / ("response-%03d.npy" % j)
            if basis.sha(path) != row["response_sha256"]:
                raise ValueError("A complete original response vector changed")
            vector = np.load(path, allow_pickle=False)
            if vector.shape != (dimension,) or vector.dtype != np.dtype("float64"):
                raise ValueError("A response vector lost the original coordinate ordering")
            if not np.all(np.isfinite(vector)):
                raise ValueError("A response vector became nonfinite")
            V[:, j] = vector
            if not np.array_equal(sigma*gauge*vector[height_columns[0]:height_columns[1]],
                                  np.asarray(row["physical_height_response"])):
                raise ValueError("The saved physical height trace differs")
            residuals[j] = float(row["original_full_matrix_residual_max"])
            if not math.isfinite(residuals[j]) or residuals[j] < 0:
                raise ValueError("A complete column residual is invalid")
        del vector
        A = sigma*gauge*V[height_columns[0]:height_columns[1]]
        terminal_matrix = np.eye(modes)+G@A
        solution = np.linalg.solve(terminal_matrix, np.column_stack((g, np.eye(modes))))
        forcing, inverse = solution[:, 0], solution[:, 1:]
        if not np.all(np.isfinite(solution)):
            raise ValueError("The complete small terminal solve returned nonfinite values")
        small_residual = terminal_matrix@forcing-g
        correction = -float(args.step_scale)*(V@forcing)
        trace_correction = sigma*gauge*correction[height_columns[0]:height_columns[1]]
        matrix_path = Path(ident["matrix"]["path"])
        matrix = load_npz(matrix_path)
        if matrix.format != "csr" or matrix.shape != (dimension, dimension):
            raise ValueError("The actual complete source matrix changed representation")
        full_forcing_residual = matrix@correction
        full_forcing_residual[-modes:] += g+G@trace_correction
        if not (np.all(np.isfinite(correction)) and np.all(np.isfinite(full_forcing_residual))):
            raise ValueError("The full original-matrix correction is nonfinite")
        trial_y = raw["y"]+correction[:n*nodes].reshape((n, nodes), order="F")
        trial_p = raw["p"]+correction[n*nodes:]
        if not np.all(np.isfinite(trial_y)) or not np.all(np.isfinite(trial_p)):
            raise ValueError("The complete unaccepted initial field is nonfinite")
        observed = read(BASELINE)
        if (observed["source_run_sha256"] != basis.sha(run_path)
                or observed["source_raw_sha256"] != record["raw_return"]["sha256"]
                or observed["source_mean_nodes"] != record["prefix_audit"]["samples_psi"]
                or not same_float(observed["source_delta"], record["frozen_profile"]["delta"])):
            raise ValueError("The historical complete F_L observation is not at this source point")
        old_rows = [row for row in observed["progress"]
                    if row["event"] == "original_base_residual_checked"]
        if len(old_rows) != 1 or (old_rows[0]["states"], old_rows[0]["nodes"],
                                 old_rows[0]["controls"]) != (n, nodes, modes):
            raise ValueError("The historical complete residual convention differs")
        state["linear_step"] = dict(
            equation="(I + G C Vhat)t = g(H0); DeltaZ = -step_scale Vhat t",
            step_scale=args.step_scale,
            complete_Newton_step=False,
            small_terminal_residual_max=float(np.max(np.abs(small_residual))),
            complete_boundary_forcing_matrix_residual_max=float(np.max(np.abs(full_forcing_residual))),
            complete_boundary_forcing_matrix_residual_l2=float(np.linalg.norm(full_forcing_residual)),
            column_residual_amplification_estimate=float(args.step_scale*np.sum(residuals*np.abs(forcing))),
            undamped_source_forcing_max=float(np.max(np.abs(g))),
            remaining_damped_forcing_max=float(np.max(np.abs((1-args.step_scale)*g))),
            original_F_L_has_not_been_set_to_zero=True,
            historical_same_source_full_F_L_observation=dict(
                evidence=bound(BASELINE), maximum=old_rows[0]["residual_max"],
                current_process_reevaluation_performed=False,
                numerical_observation_not_interval_bound=True),
            current_point_internal_J_minus_old_J_unpaid=not same_point,
            all_original_state_and_parameter_corrections_retained=True,
        )
        state["literal_small_matrix_certificate"] = literal_small_inverse_certificate(terminal_matrix, inverse)
        state["trial"] = dict(
            additive_delta_parameter=float(trial_p[0]),
            original_candidate_delta=record["physical_profile"]["delta"]+float(trial_p[0]),
            maximum_absolute_state_correction=float(np.max(np.abs(correction[:n*nodes]))),
            maximum_absolute_normalized_parameter_correction=float(np.max(np.abs(correction[n*nodes:]))),
            physical_g_unchanged_claimed=False, original_model_domain_unpaid=True,
        )
        initial = out / "initial.npz"
        with initial.open("xb") as stream:
            np.savez_compressed(stream, x=raw["x"], y=trial_y, p=trial_p, pscale=raw["pscale"])
            stream.flush()
            os.fsync(stream.fileno())
        state["result"] = dict(initial_raw=str(initial), initial_raw_sha256=basis.sha(initial))
        state["inputs"] = dict(
            basis_report=br_reference, source_run=bound(run_path),
            source_raw=bound(run_path.parent/record["raw_return"]["file"]),
            source_physical=bound(run_path.parent/"physical.npz"),
            matrix=ident["matrix"], matrix_input=ident["matrix_input"],
            old_full_H_packet=proof["source_packet"],
            original_definition_sources=record["source_hashes"],
            original_definition_inputs=record["inputs"],
        )
        if (bound(old_proof_path) != old_proof_reference
                or basis.sha(br_path) != br_reference["sha256"]
                or basis.sha(matrix_path) != ident["matrix"]["sha256"]
                or basis.sha(run_path) != ident["origin_design_run"]["sha256"]):
            raise ValueError("A bound input changed during the unaccepted calculation")
        state["status"] = "unaccepted_complete_boundary_only_initializer_ready"
        state["elapsed_seconds"] = time.monotonic()-started
        basis.save(destination, state)
        print(json.dumps(state, allow_nan=False), flush=True)
        return 0
    except Exception as error:
        state.update(status="initializer_stopped_without_acceptance", error=repr(error),
                     traceback=traceback.format_exc(), elapsed_seconds=time.monotonic()-started)
        basis.save(destination, state)
        raise


if __name__ == "__main__":
    sys.exit(main())

