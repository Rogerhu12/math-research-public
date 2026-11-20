"""Explicit v3 continuation of the unfinished low193/97 endpoint diagnostic.

This is a new comparison-operator diagnostic, never an actual inverse
certificate.  It reads the complete already-admitted W2C context.  On every
original comparison panel it takes entrywise floating midpoints of the
whole signed AL enclosure, and the floating midpoint of the true panel
length.  It does NOT identify those midpoint matrices with point values of
the actual centre.  The whole high feedback and every original remainder,
atom, rho-normalizer, source and high port obligation remain unpaid.

The old attempt completed138 coefficient-definition panels and NO endpoint
or frame target.  Its whole original outcome is an immutable input.  The
raw midpoint matrices and raw physical boundary conditions remain identical;
their138-panel hash chain is reidentified during necessary materialization.
New propagation uses the positive diagonal D_i=diag(1_96,q_i, q_i I_96),
where q_i is the exact dyadic represented by the midpoint of the same WVC
reference q.  Mathematically exp(h A)=D_i^-1 exp(h D_i A D_i^-1)D_i.
Both sides of every interface are converted back to raw coordinates and
reorthogonalized.  No identity transmission is inserted in scaled variables.
All reported matching matrices use raw orthonormal frames.

The entire155-panel plan is saved before the first propagation.  The old
arbitrary256 per-panel cap is replaced by the unchanged8192 total cap; the
scaled step infinity norm stays at4 and the wall budget stays1800 seconds.

There is no command-line entry point and no scientific work at import.
The caller owns admission, immutable source binding, runtime pinning and
publication.  run_from_context requires this repository's public Actions.
Only small scalar JSON is written; matrices and frames remain in memory.
"""


HEAD = (tuple((0, j) for j in range(1, 97)) + ((1, 0),)
        + tuple((1, j) for j in range(1, 97)))
STATE_DIMENSION = 193
LEFT_FRAME_DIMENSION = 97
RIGHT_FRAME_DIMENSION = 96
MAX_PANELS = 155
MAX_STEP_INFINITY_NORM = 4.0
MAX_SUBSTEPS_PER_PANEL = 8192
MAX_SUBSTEPS_PER_DIRECTION = 8192
MAX_WALL_SECONDS = 1800
MAX_OUTPUT_BYTES = 35000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def run_from_context(api, kernel_api, context, output_path, progress=None, prior_attempt=None):
    """Diagnose the complete193-state /97-endpoint low comparison operator.

    Parameters are the existing NumericalAPI, signed-kernel module, and
    result of prepare_complete_kernel_context.  kernel_api is retained in
    the shared interface but no high graph is evaluated here.  progress,
    when supplied, has the existing progress(stage, detail) signature.

    prior_attempt contains the complete pinned original outcome and its
    whole-file identity.  Both separated frames are propagated in the
    declared scaled coordinates with expm and thin QR.  Forward
    left frames are retained at every panel boundary, and backward right
    frames are matched there.  Neither the floating endpoint singular
    value nor the boundary-only matching angles are certified quantities.
    The complete operator, its inverse norm and between-panel angles are
    deliberately not claimed.  A failure publishes its completed prefix
    and raises; there is no retry or adaptive alternative target.
    """
    import hashlib
    import json
    import math
    import os
    import platform
    import time
    from pathlib import Path

    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "new scientific diagnostic runs only in the public own repository Actions")
    import numpy as np
    import scipy
    from scipy import linalg

    required = (
        "same_WVC_reference", "same_actual_S_and_all_seven_ports",
        "all_coefficient_pieces_and_raw_identity_transmissions",
        "true_signed_collar_not_zero_reference_packet",
        "ordinary_dr_pairing_and_complete_Gf_atoms",
    )
    require(all(context.qualifications.get(key) is True for key in required),
            "whole same-object admitted signed centre context")
    count = len(context.domain.cells)
    require(1 <= count <= MAX_PANELS and len(context.parent_indices) == count,
            "whole declared comparison cover within the fixed cap")
    require(context.parent_definition_count == 153
            and context.original_body_row_count == 4650
            and context.original_intersection_count == 4801,
            "every original parent, body row and closed intersection")
    require(callable(context.centre_matrix), "same signed raw centre adapter")
    require(isinstance(prior_attempt, dict) and set(prior_attempt) == {"source_identity", "whole_original_outcome"},
            "whole pinned failed original attempt is a required continuation input")
    previous = prior_attempt["whole_original_outcome"]
    prior = previous["diagnostic"]
    require(previous["run_id"] == "44719196304" and previous["run_attempt"] == "1"
            and previous["complete"] is False and previous["proved"] is False
            and prior["status"] == "failed_with_completed_prefix"
            and prior["progress"]["coefficient_panels"] == 138
            and all(prior["progress"][name] == 0 for name in
                    ("forward_panels", "backward_panels", "forward_substeps", "backward_substeps", "matched_boundaries"))
            and prior["endpoint_diagnostic"] is None and prior["two_sided_boundary_diagnostic"] is None
            and prior["failure"]["message"] == "fixed complete diagnostic substep cap; no omitted panel",
            "only the unfinished zero-propagation endpoint target may continue")
    prior_count = prior["progress"]["coefficient_panels"]
    started = time.monotonic()
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    chain = hashlib.sha256(b"fixed_WVC_low193_midpoint_comparison_v1").hexdigest()
    p0 = 13.0 / 80.0
    robin_scale = math.sqrt(1.0 + p0*p0)
    record = {
        "kind": "fixed_WVC_low193_balanced_endpoint_continuation_v3",
        "status": "running",
        "stage": "admitted_context",
        "scope": {
            "operator": "raw AL,c only; high feedback CFB remains unpaid",
            "comparison_rule": "entrywise float64 midpoint of each whole-panel AL ball and its true-length ball",
            "actual_point_coefficient_values_used": False,
            "physical_mean_retained": True,
            "left_boundary": "all96 raw even values zero at the true root",
            "right_boundary": "all96 raw odd+(13/80)even values and the physical mean zero at R",
            "right_rows_normalized": "Robin rows divided by sqrt(1+(13/80)^2); mean row unchanged",
            "state_dimension": STATE_DIMENSION,
            "left_frame_dimension": LEFT_FRAME_DIMENSION,
            "right_frame_dimension": RIGHT_FRAME_DIMENSION,
            "endpoint_matrix_dimension": LEFT_FRAME_DIMENSION,
            "raw_identity_transmissions": True,
            "singular_values_depend_on_declared_raw_coordinates": True,
            "boundary_matching_only": True,
            "float_radius_statistics_are_not_outward_bounds": True,
            "balance": "positive dyadic diag(1_96,q_mid,q_mid I_96) from the same WVC reference",
            "propagator_identity": "exp(hA)=D^-1 exp(h D A D^-1) D",
            "QR_and_expm_step_coordinates": "scaled within a panel; raw at every comparison boundary",
            "all_boundary_singular_values_use_raw_orthonormal_frames": True,
            "midpoint_raw_operator_replaced_by_balancing": False,
        },
        "continuation": {
            "whole_original_outcome_reference": {"file": prior_attempt["source_identity"], "json_path": []},
            "original_coefficient_definition_prefix": prior_count,
            "original_prefix_matrix_chain": prior["comparison_matrix_sha256_chain"],
            "original_prefix_radius_statistics_copied_whole": prior["floating_input_statistics"],
            "original_endpoint_or_matching_targets_completed": 0,
            "original_endpoint_or_matching_successes_recomputed": 0,
            "original_raw_definition_prefix_reidentified": False,
            "new_work": "complete155-panel scaled plan, then the unfinished full endpoint and all-boundary frame target",
        },
        "limits": {
            "panels": MAX_PANELS,
            "step_infinity_norm": MAX_STEP_INFINITY_NORM,
            "substeps_per_panel": MAX_SUBSTEPS_PER_PANEL,
            "substeps_per_direction": MAX_SUBSTEPS_PER_DIRECTION,
            "wall_seconds": MAX_WALL_SECONDS,
            "output_bytes": MAX_OUTPUT_BYTES,
            "automatic_retries": 0,
            "derived_arrays_persisted": 0,
        },
        "reference_identity": context.reference_identity,
        "complete_source_counts": {
            "parents": context.parent_definition_count,
            "body_rows": context.original_body_row_count,
            "closed_intersections": context.original_intersection_count,
            "comparison_panels": count,
        },
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "github_run_id": os.environ.get("GITHUB_RUN_ID"),
            "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "blas_threads": {key: os.environ.get(key) for key in
                             ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        },
        "certification": {
            "actual_low_centre_invertibility_proved": False,
            "actual_complete_centre_invertibility_proved": False,
            "actual_positive_family_inverse_proved": False,
            "complete_source_norm_proved": False,
            "whole_interval_transversality_proved": False,
            "original_finite_Qf_rho_gate_transferred": False,
            "either_original_RHS_proved": False,
            "topic_completion_proved": False,
        },
        "unpaid_obligations": [
            "true centre versus whole-panel midpoint comparison and uncertain true root",
            "full signed high feedback CFB and all actual high-family residuals",
            "validated propagation, rounding and between-panel matching",
            "complete inverse/source operator norm with all193 output atoms",
            "original radial lift, finite projection and rational rho-normalizer",
            "actual independent outer column, outer Robin, mean and high-trace rows",
            "both original right-side rows and all seven high ports",
        ],
        "progress": {"coefficient_panels": 0, "forward_panels": 0,
                     "backward_panels": 0, "matched_boundaries": 0,
                     "forward_substeps": 0, "backward_substeps": 0,
                     "forward_interface_QR": 0, "backward_interface_QR": 0},
        "comparison_matrix_sha256_chain": chain,
        "floating_input_statistics": dict(prior["floating_input_statistics"]),
        "complete_plan": {
            "columns": ["panel", "parent", "length_midpoint", "q_balance", "raw_row_norm", "scaled_row_norm", "substeps"],
            "rows": [], "complete": False, "budget_passed": None,
            "planned_substeps_per_direction": None, "largest_panel_substeps": None,
            "no_propagation_before_complete_plan": True,
            "complete_plan_is_small_operational_metadata_not_a_coefficient_array": True,
        },
        "qr_diagnostic": {"max_frame_orthogonality_defect": 0.0,
                          "forward_log_volume": 0.0,
                          "backward_log_volume": 0.0},
        "endpoint_diagnostic": None,
        "two_sided_boundary_diagnostic": None,
    }

    def finite(value, label):
        result = float(value)
        require(math.isfinite(result), "finite floating diagnostic: " + label)
        return result

    def mid(value):
        return finite(value.mid(), "ball midpoint")

    def radius_display(value):
        return mid((value.upper() - value.lower()) / 2)

    def checkpoint(stage):
        record["stage"] = stage
        record["elapsed_seconds"] = finite(time.monotonic() - started, "elapsed")
        raw = (json.dumps(record, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")
        require(len(raw) <= MAX_OUTPUT_BYTES, "small complete scalar diagnostic output")
        temporary = target.with_name(target.name + ".tmp")
        temporary.write_bytes(raw)
        temporary.replace(target)
        if progress is not None:
            progress("low_centre_endpoint_diagnostic", {
                "stage": stage, **record["progress"],
                "elapsed_seconds": record["elapsed_seconds"],
                "actual_inverse_proved": False,
            })

    def budget():
        require(time.monotonic() - started <= MAX_WALL_SECONDS,
                "fixed diagnostic wall-time cap; completed prefix retained")

    def oriented_qr(value, direction):
        budget()
        require(np.isfinite(value).all(), "finite complete propagated frame")
        q, r = linalg.qr(value, mode="economic", check_finite=False)
        diagonal = np.diag(r)
        require(np.isfinite(diagonal).all() and np.all(np.abs(diagonal) > 0.0),
                "nonzero floating QR diagonal; no rank truncation")
        signs = np.where(diagonal < 0.0, -1.0, 1.0)
        q = q * signs[np.newaxis, :]
        log_volume = finite(np.log(np.abs(diagonal)).sum(), "QR log-volume")
        key = direction + "_log_volume"
        record["qr_diagnostic"][key] = finite(
            record["qr_diagnostic"][key] + log_volume, "accumulated QR log-volume")
        defect = finite(linalg.norm(q.T @ q - np.eye(q.shape[1]), ord=2),
                        "frame orthogonality")
        record["qr_diagnostic"]["max_frame_orthogonality_defect"] = max(
            record["qr_diagnostic"]["max_frame_orthogonality_defect"], defect)
        return q

    def singular_diagnostic(matrix):
        values = linalg.svdvals(matrix, check_finite=False)
        smallest = finite(values[-1], "smallest singular value")
        largest = finite(values[0], "largest singular value")
        ratio = largest / smallest if smallest > 0.0 else None
        return {"smallest_singular_value": smallest,
                "largest_singular_value": largest,
                "condition_number": ratio if ratio is not None and math.isfinite(ratio) else None,
                "zero_or_nonfinite_condition": ratio is None or not math.isfinite(ratio)}

    def match_boundary(index, right_frame, left_frames):
        budget()
        value = singular_diagnostic(np.concatenate((left_frames[index], right_frame), axis=1))
        current = record["two_sided_boundary_diagnostic"]
        if current is None or value["smallest_singular_value"] < current["minimum_matching_singular_value"]:
            record["two_sided_boundary_diagnostic"] = {
                "minimum_matching_singular_value": value["smallest_singular_value"],
                "witness_boundary_index": index,
                "witness_diagnostic": value,
                "boundary_count": record["progress"]["matched_boundaries"] + 1,
                "between_boundary_minimum_not_evaluated": True,
            }
        record["progress"]["matched_boundaries"] += 1
        record["two_sided_boundary_diagnostic"]["boundary_count"] = record["progress"]["matched_boundaries"]

    matrices, lengths, substeps, balances = [], [], [], []
    left_frames = []
    checkpoint("admitted_context")
    try:
        planned_steps = 0
        for index in range(count):
            budget()
            box = context.domain.whole_cell_box(index)
            whole = context.centre_matrix(HEAD, HEAD, box)
            require(whole.shape == (STATE_DIMENSION, STATE_DIMENSION),
                    "entire raw low193 matrix including physical mean")
            matrix = np.empty((STATE_DIMENSION, STATE_DIMENSION), dtype=np.float64)
            largest_radius_row = 0.0
            for i, row in enumerate(whole.values):
                radii = []
                for j, value in enumerate(row):
                    require(value.is_finite(), "finite whole-panel signed AL coefficient")
                    matrix[i, j] = mid(value)
                    if index >= prior_count:
                        radii.append(radius_display(value))
                if index >= prior_count:
                    largest_radius_row = max(largest_radius_row,
                                             finite(math.fsum(radii), "radius row sum"))
            length_ball = context.domain.full_length(index)
            length = mid(length_ball)
            require(length > 0.0, "positive whole true-panel midpoint length")
            row_sum = finite(linalg.norm(matrix, ord=np.inf), "matrix row sum")
            q_balance = mid(context.reference_qs[index])
            require(q_balance > 0.0, "strict positive same-reference dyadic balance")
            balance = np.ones(STATE_DIMENSION, dtype=np.float64)
            balance[96:] = q_balance
            scaled = balance[:, np.newaxis]*matrix/balance[np.newaxis, :]
            require(np.isfinite(scaled).all(), "whole finite diagonally scaled generator")
            scaled_row_sum = finite(linalg.norm(scaled, ord=np.inf), "scaled matrix row sum")
            steps = max(1, math.ceil(length*scaled_row_sum/MAX_STEP_INFINITY_NORM))
            planned_steps += steps
            matrices.append(scaled)
            balances.append(balance)
            lengths.append(length)
            substeps.append(steps)
            payload = matrix.astype("<f8", copy=False).tobytes(order="C")
            chain = hashlib.sha256(bytes.fromhex(chain) + index.to_bytes(4, "big")
                                   + length.hex().encode("ascii") + payload).hexdigest()
            record["comparison_matrix_sha256_chain"] = chain
            if index + 1 == prior_count:
                require(chain == prior["comparison_matrix_sha256_chain"],
                        "same entire138-panel raw midpoint definition prefix")
                record["continuation"]["original_raw_definition_prefix_reidentified"] = True
            stats = record["floating_input_statistics"]
            if index >= prior_count:
                stats["max_matrix_row_sum"] = max(stats["max_matrix_row_sum"], row_sum)
                stats["max_radius_row_sum"] = max(stats["max_radius_row_sum"], largest_radius_row)
                stats["length_weighted_radius_row_sum"] = finite(
                    stats["length_weighted_radius_row_sum"] + length*largest_radius_row,
                    "length-weighted radius statistic")
                stats["max_length_radius"] = max(stats["max_length_radius"], radius_display(length_ball))
            record["complete_plan"]["rows"].append([
                index, context.parent_indices[index], length, q_balance,
                row_sum, scaled_row_sum, steps])
            record["progress"]["coefficient_panels"] = index + 1
            record["planned_substeps_per_direction"] = planned_steps
            checkpoint("complete_coefficient_panel")

        record["complete_plan"].update({"complete": True,
            "planned_substeps_per_direction": planned_steps,
            "largest_panel_substeps": max(substeps),
            "budget_passed": bool(planned_steps <= MAX_SUBSTEPS_PER_DIRECTION
                                  and max(substeps) <= MAX_SUBSTEPS_PER_PANEL)})
        require(record["continuation"]["original_raw_definition_prefix_reidentified"] is True,
                "whole original raw definition prefix before new propagation")
        checkpoint("complete155_panel_scaled_plan")
        require(record["complete_plan"]["budget_passed"] is True,
                "complete155-panel scaled plan exceeds fixed8192 total budget; no propagation started")

        left = np.zeros((STATE_DIMENSION, LEFT_FRAME_DIMENSION), dtype=np.float64)
        left[:LEFT_FRAME_DIMENSION, :] = np.eye(LEFT_FRAME_DIMENSION)
        left_frames.append(left.copy())
        for index in range(count):
            budget()
            left = oriented_qr(balances[index][:, np.newaxis]*left, "forward")
            record["progress"]["forward_interface_QR"] += 1
            propagator = linalg.expm(matrices[index] * (lengths[index]/substeps[index]))
            require(np.isfinite(propagator).all(), "finite whole-panel expm")
            for _ in range(substeps[index]):
                left = oriented_qr(propagator @ left, "forward")
                record["progress"]["forward_substeps"] += 1
            left = oriented_qr(left/balances[index][:, np.newaxis], "forward")
            record["progress"]["forward_interface_QR"] += 1
            left_frames.append(left.copy())
            record["progress"]["forward_panels"] = index + 1
            checkpoint("complete_forward_panel")

        endpoint = np.vstack(((left[:96, :] + p0*left[97:, :])/robin_scale,
                              left[96:97, :]))
        require(endpoint.shape == (LEFT_FRAME_DIMENSION, LEFT_FRAME_DIMENSION),
                "whole97 endpoint matrix including physical mean")
        record["endpoint_diagnostic"] = singular_diagnostic(endpoint)
        checkpoint("complete97_endpoint_diagnostic")

        right = np.zeros((STATE_DIMENSION, RIGHT_FRAME_DIMENSION), dtype=np.float64)
        right[:96, :] = -p0*np.eye(RIGHT_FRAME_DIMENSION)/robin_scale
        right[97:, :] = np.eye(RIGHT_FRAME_DIMENSION)/robin_scale
        match_boundary(count, right, left_frames)
        for index in range(count - 1, -1, -1):
            budget()
            right = oriented_qr(balances[index][:, np.newaxis]*right, "backward")
            record["progress"]["backward_interface_QR"] += 1
            propagator = linalg.expm(-matrices[index] * (lengths[index]/substeps[index]))
            require(np.isfinite(propagator).all(), "finite whole backward expm")
            for _ in range(substeps[index]):
                right = oriented_qr(propagator @ right, "backward")
                record["progress"]["backward_substeps"] += 1
            right = oriented_qr(right/balances[index][:, np.newaxis], "backward")
            record["progress"]["backward_interface_QR"] += 1
            match_boundary(index, right, left_frames)
            record["progress"]["backward_panels"] = count - index
            checkpoint("complete_backward_panel")

        require(record["progress"]["matched_boundaries"] == count + 1,
                "every original comparison boundary matched exactly once")
        budget()
        record["status"] = "complete_floating_comparison_diagnostic_only"
        checkpoint("complete")
        return record
    except BaseException as error:
        record["status"] = "failed_with_completed_prefix"
        record["failure"] = {"type": type(error).__name__, "message": str(error)[:1200]}
        checkpoint("failed")
        raise
