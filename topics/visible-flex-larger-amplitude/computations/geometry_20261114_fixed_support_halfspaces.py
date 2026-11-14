#!/usr/bin/env python3
"""Local C projection with a fixed correction support and complete B offsets.

The full raw LSMR vector lives in all original exact coordinates. Only
the projection correction is restricted to physical nodes471..482 and
the original three global scalar controls. In particular the complete
new RMS470 row keeps its node470 contribution in B_out*z0_out.

The original full-vector radial repair and same-model selection are not
implemented here and are not replaced. They may subsequently scale the
outside raw direction. A finite local candidate need not solve or even
satisfy the restricted halfspace problem before that global repair.
"""
from __future__ import annotations

import time

import numpy as np

import geometry_20261114_full_angle_domain_operator as frozen
import geometry_20261114_full_angle_projection_warm as original


SCHEMA = "fixed-correction-support-complete-halfspace-offset-v1"
FIXED_PHYSICAL_NODES = tuple(range(471, 483))


def fixed_support_indices(domain):
    """Original scaled-z coordinates, not compressed B-local coordinates."""
    chart = domain.chart
    if domain.n != 338 or domain.k != 3 or chart.m != 699:
        raise ValueError("This declared support belongs to the original M112/699-node problem")
    pstart = chart.physical_size+chart.free
    index = np.concatenate([
        *(np.arange((j-1)*domain.n, j*domain.n, dtype=np.int64)
            for j in FIXED_PHYSICAL_NODES),
        np.arange(pstart, chart.size, dtype=np.int64)])
    if (len(index) != 4059 or len(np.unique(index)) != len(index)
            or not np.all(np.isin(index, np.asarray(domain.local_indices)))):
        raise ValueError("Retain the declared twelve-node and global-p correction support")
    return index


def fixed_support_projection(domain, z0, diagonal, c, *, max_sweeps,
                             deadline, progress):
    """Project x=C_S*z_S against B_S*C_S^-1*x >= -c-B_out*z0_out.

Rows and their complete original values remain in domain. The returned
vector preserves z0 outside S before the caller's original whole-vector
radial repair. No positivity assumption is made on the effective local
offset. A computed binary64 zero local row with a negative effective
offset is recorded as infeasible for that assembled floating subproblem;
underflow is not excluded, and this never rejects the original problem.
"""
    frozen.require_actions()
    raw = np.asarray(z0, dtype=np.float64)
    diagonal = np.asarray(diagonal, dtype=np.float64)
    c = np.asarray(c, dtype=np.float64)
    if (raw.shape != (domain.chart.size,) or diagonal.shape != raw.shape
            or c.shape != (domain.rows,) or not np.all(np.isfinite(raw))
            or not np.all(np.isfinite(diagonal)) or np.any(diagonal <= 0)
            or not np.all(np.isfinite(c)) or np.any(c <= 0)):
        raise ValueError("Use the original finite full direction, positive diagonal and original c")
    index = fixed_support_indices(domain)
    C = diagonal[index]
    outside = raw.copy()
    outside[index] = 0.
    # This is an actual complete B action. No outside column is erased
    # from the original operator or silently folded into a zero offset.
    outside_action = domain.matvec(outside)
    raw_action = domain.matvec(raw)
    effective_offset = c+outside_action
    if (not np.all(np.isfinite(outside_action))
            or not np.all(np.isfinite(raw_action))
            or not np.all(np.isfinite(effective_offset))):
        raise FloatingPointError("The original complete raw/outside B actions must be finite")
    support_mask = np.zeros(domain.chart.size, dtype=bool)
    support_mask[index] = True
    with np.errstate(over="ignore", invalid="ignore"):
        x0 = C*raw[index]
    base_report = dict(schema=SCHEMA,
        metric="0.5*||C_S*(z_S-z0_S)||^2; z_out=z0_out before whole-vector repair",
        correction_physical_nodes=list(FIXED_PHYSICAL_NODES),
        correction_global_controls_included=True,
        correction_global_free_core_columns_included=False,
        correction_support=frozen.array_identity(index),
        full_compiled_B_local_dimension=len(domain.local_indices),
        local_dimension=len(index), constraint_rows=len(c),
        column_diagonal_source="Original complete unprojected regularized column norms restricted to S",
        full_model_Hessian_used=False, complete_R265_quadratic_minimized=False,
        algorithm="Cyclic Hildreth in fixed x=C_S*z_S with complete outside raw offsets",
        normalized_rows_precompiled_once=True,
        shared_nodes_and_global_controls_scatter_updated=True,
        full_original_B_unchanged=True,
        offset_definition="effective_local_offset=c+B_out*z0_out",
        original_c=frozen.array_identity(c),
        outside_raw_full_B_action=frozen.array_identity(outside_action),
        effective_local_offset=frozen.array_identity(effective_offset),
        effective_local_offset_summary=original.summarize(effective_offset),
        effective_local_offset_required_positive=False,
        zero_row_infeasibility_scope="Assembled binary64 local rows only; division underflow is not excluded",
        maximum_sweeps=int(max_sweeps),
        stopping_tolerance_is_not_scientific_gate=True,
        multipliers_are_for_local_projection_only=True,
        multipliers_are_not_R265_model_KKT_multipliers=True,
        complete_R265_quadratic_optimality_claimed=False,
        global_radial_and_segment_may_scale_outside_raw=True,
        final_outside_direction_claimed_unchanged=False,
        no_new_nonlinear_scientific_gate=True)
    base_arrays = dict(local_indices=index.tolist(), column_diagonal=C.tolist(),
        original_c=c.tolist(), outside_raw_B_action=outside_action.tolist(),
        effective_local_offset=effective_offset.tolist(),
        original_full_raw_B_action=raw_action.tolist(),
        projection_input_x=x0.tolist(),
        correction_physical_nodes=list(FIXED_PHYSICAL_NODES),
        correction_global_controls_included=True)
    history = []

    def raw_fallback(reason, details):
        # This is a stated numerical failure of this local subproblem,
        # not an accepted projected solution. The unchanged caller still
        # applies its complete radial repair, backup and real trial gates.
        report = dict(base_report, completed_sweeps=len(history), history=history,
            stopping_reason=reason, local_projection_numerically_completed=False,
            local_projection_failure=details,
            candidate_returned="original complete raw LSMR vector",
            outside_raw_preserved_bitwise_before_radial=True,
            local_projection_objective=0.,
            projection_multipliers_available=False,
            unnormalized_linear_slack_before_radial_repair=original.summarize(c+raw_action))
        arrays = dict(base_arrays, projection_output_x=x0.tolist(),
            original_slack_before_radial_repair=(c+raw_action).tolist(),
            numerical_local_projection_failure=True)
        return raw.copy(), report, arrays

    if not np.all(np.isfinite(x0)):
        return raw_fallback("nonfinite-fixed-support-coordinate-return-original-ray",
            dict(stage="forming C_S*z0_S"))
    blocks = []
    raw_reconstructed = np.empty_like(c)
    zero_infeasible_rows = []
    for block in domain.local_blocks:
        global_columns = np.asarray(block["global_columns"], dtype=np.int64)
        keep = support_mask[global_columns]
        columns = np.searchsorted(index, global_columns[keep])
        sl = block["row_slice"]
        unscaled_rows = np.asarray(block["rows"], dtype=np.float64)[:, keep]
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            rows = unscaled_rows/C[columns][None, :]
            lengths = np.linalg.norm(rows, axis=1)
        computed_zero = np.all(rows == 0, axis=1)
        if (not np.all(np.isfinite(rows)) or not np.all(np.isfinite(lengths))
                or np.any((lengths == 0) & ~computed_zero)):
            return raw_fallback("unrepresentable-fixed-support-normalization-return-original-ray",
                dict(query_index=block["query_index"], kind=block["kind"],
                    interval=block["interval"], stage="finite row norms or row-norm underflow"))
        nonzero = lengths > 0
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            normalized = np.divide(rows, lengths[:, None], out=np.zeros_like(rows),
                where=nonzero[:, None])
            lower = np.divide(-effective_offset[sl], lengths,
                out=np.zeros_like(lengths), where=nonzero)
            squared = np.sum(normalized*normalized, axis=1)
        if (not np.all(np.isfinite(normalized)) or not np.all(np.isfinite(lower))
                or not np.all(np.isfinite(squared)) or np.any(squared[nonzero] <= 0)):
            return raw_fallback("unrepresentable-fixed-support-halfspace-return-original-ray",
                dict(query_index=block["query_index"], kind=block["kind"],
                    interval=block["interval"], stage="normalized rows or effective lower bounds"))
        zero_bad = (~nonzero) & (effective_offset[sl] < 0)
        zero_infeasible_rows.extend((sl.start+np.flatnonzero(zero_bad)).tolist())
        # Read-only floating reconstruction of the complete original raw
        # action. The authoritative acceptance/readout stays full B.
        raw_reconstructed[sl] = effective_offset[sl]+unscaled_rows@raw[index[columns]]
        blocks.append(dict(columns=columns, row_slice=sl,
            query_index=block["query_index"], kind=block["kind"], interval=block["interval"],
            normalized=normalized, lower=lower, row_norm=lengths,
            normalized_norm_squared=squared, nonzero=nonzero,
            zero_local_infeasible=zero_bad, dual=np.zeros(len(lengths)),
            unscaled_rows=unscaled_rows,
            retained_global_columns=global_columns[keep],
            outside_global_columns=global_columns[~keep]))
    x = x0.copy()
    tolerance = 1e-10*max(1., float(np.linalg.norm(x0)))
    if not np.isfinite(tolerance):
        return raw_fallback("nonfinite-fixed-support-algorithm-scale-return-original-ray",
            dict(stage="norm of C_S*z0_S"))
    reason = "maximum-sweeps"
    for sweep in range(max_sweeps):
        if time.monotonic() >= deadline:
            reason = "bounded-projection-time"
            break
        maximum_update = 0.
        for block in blocks:
            columns = block["columns"]
            local = x[columns].copy()
            for i in range(len(block["dual"])):
                if not block["nonzero"][i]:
                    continue
                row = block["normalized"][i]
                old = block["dual"][i]
                with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
                    proposed = old+(block["lower"][i]-float(row@local))/block["normalized_norm_squared"][i]
                if not np.isfinite(proposed):
                    return raw_fallback("nonfinite-local-dual-update-return-original-ray",
                        dict(sweep=sweep+1, query_index=block["query_index"], angle_index=i))
                new = max(0., proposed)
                change = new-old
                if change:
                    with np.errstate(over="ignore", invalid="ignore"):
                        local += change*row
                block["dual"][i] = new
                maximum_update = max(maximum_update, abs(change))
            if not np.all(np.isfinite(local)):
                return raw_fallback("nonfinite-local-primal-update-return-original-ray",
                    dict(sweep=sweep+1, query_index=block["query_index"]))
            x[columns] = local
        violations = [np.maximum(0., block["lower"]
            -block["normalized"]@x[block["columns"]]) for block in blocks]
        maximum_violation = max(float(np.max(v, initial=0)) for v in violations)
        with np.errstate(over="ignore", invalid="ignore"):
            objective = .5*float((x-x0)@(x-x0))
        if not np.isfinite(maximum_violation) or not np.isfinite(objective):
            return raw_fallback("nonfinite-local-projection-summary-return-original-ray",
                dict(sweep=sweep+1))
        row = dict(sweep=sweep+1, normalized_nonzero_row_primal_violation=maximum_violation,
            normalized_primal_violation=maximum_violation,
            fixed_support_infeasible_zero_row_count=len(zero_infeasible_rows),
            largest_dual_coordinate_update=maximum_update,
            local_projection_objective=objective)
        history.append(row)
        if sweep == 0 or (sweep+1) % 10 == 0:
            progress(row)
        if max(maximum_violation, maximum_update) <= tolerance:
            reason = ("nonzero-row-tolerance-with-infeasible-fixed-support-zero-rows"
                if zero_infeasible_rows else "normalized-primal-and-dual-coordinate-update-tolerance")
            break
    candidate = raw.copy()
    candidate[index] = x/C
    original_slack = c+domain.matvec(candidate)
    if not np.all(np.isfinite(candidate)) or not np.all(np.isfinite(original_slack)):
        return raw_fallback("nonfinite-complete-candidate-action-return-original-ray",
            dict(stage="complete original B action after restricted projection"))
    normal_sum = np.zeros_like(x)
    normalized_dual = np.zeros(len(c))
    original_dual = np.zeros(len(c))
    complementary_products = np.zeros(len(c))
    row_norms = np.zeros(len(c))
    reconstructed = np.empty_like(c)
    row_identity = []
    for block in blocks:
        columns, sl = block["columns"], block["row_slice"]
        np.add.at(normal_sum, columns, block["normalized"].T@block["dual"])
        normalized_dual[sl] = block["dual"]
        row_norms[sl] = block["row_norm"]
        original_dual[sl] = np.divide(block["dual"], block["row_norm"],
            out=np.zeros_like(block["dual"]), where=block["nonzero"])
        complementary_products[sl] = block["dual"]*(
            block["normalized"]@x[columns]-block["lower"])
        reconstructed[sl] = effective_offset[sl]+block["unscaled_rows"]@candidate[index[columns]]
        row_identity.append(dict(query_index=block["query_index"], kind=block["kind"],
            interval=block["interval"],
            retained_global_columns=frozen.array_identity(block["retained_global_columns"]),
            outside_global_columns=frozen.array_identity(block["outside_global_columns"]),
            normalized_rows=frozen.array_identity(block["normalized"]),
            lower_bounds=frozen.array_identity(block["lower"])))
    stationarity = x-x0-normal_sum
    report = dict(base_report, completed_sweeps=len(history), stopping_reason=reason,
        stopping_tolerance=tolerance, history=history,
        local_projection_numerically_completed=True,
        zero_rows=int(np.count_nonzero(row_norms == 0)),
        fixed_support_infeasible_zero_row_count=len(zero_infeasible_rows),
        fixed_support_infeasible_zero_rows=zero_infeasible_rows,
        no_claim_that_the_restricted_halfspace_set_is_feasible=True,
        local_projection_objective=.5*float((x-x0)@(x-x0)),
        projection_stationarity_x_L2=float(np.linalg.norm(stationarity)),
        projection_stationarity_x_relative=float(np.linalg.norm(stationarity)
            /max(1., np.linalg.norm(x-x0), np.linalg.norm(normal_sum))),
        projection_complementarity_sum=float(np.sum(complementary_products)),
        projection_complementarity_absolute_max=float(np.max(abs(complementary_products), initial=0)),
        projection_dual_minimum=float(np.min(normalized_dual)),
        projection_multipliers_available=True,
        outside_raw_preserved_bitwise_before_radial=(
            candidate[~support_mask].tobytes(order="C")==raw[~support_mask].tobytes(order="C")),
        raw_complete_offset_reconstruction_absolute_max=float(np.max(abs(raw_reconstructed-(c+raw_action)))),
        candidate_complete_offset_reconstruction_absolute_max=float(np.max(abs(reconstructed-original_slack))),
        reconstruction_comparison_is_readout_not_a_scientific_gate=True,
        projection_row_identities=row_identity,
        unnormalized_linear_slack_before_radial_repair=original.summarize(original_slack))
    arrays = dict(base_arrays, projection_output_x=x.tolist(),
        original_BS_over_CS_row_norm=row_norms.tolist(),
        normalized_projection_multipliers=normalized_dual.tolist(),
        original_constraint_projection_multipliers=original_dual.tolist(),
        projection_complementary_products=complementary_products.tolist(),
        fixed_support_infeasible_zero_rows=zero_infeasible_rows,
        original_raw_slack=(c+raw_action).tolist(),
        reconstructed_raw_slack=raw_reconstructed.tolist(),
        reconstructed_projected_slack=reconstructed.tolist(),
        original_slack_before_radial_repair=original_slack.tolist())
    return candidate, report, arrays
