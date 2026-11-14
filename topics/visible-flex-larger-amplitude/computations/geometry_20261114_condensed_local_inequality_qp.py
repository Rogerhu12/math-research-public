#!/usr/bin/env python3
"""Bounded local inequality solve for the complete R270 condensed model.

The supplied model already eliminated all outside coordinates with their
full affine optimum. Every inequality row belongs to the original frozen
B. A local working set only bounds optimization work; all rows are tested
after every candidate and repair. No nonlinear acceptance is supplied.
"""
from __future__ import annotations

import hashlib
import os
import time
from pathlib import Path
from types import SimpleNamespace

import numpy as np

from geometry_20261114_full_angle_projection_warm import radial_feasible
from geometry_20261114_full_metric_inequality_correction import identity
from root_20261114_complete_local_qp_condensation import CondensationDeadline

SCHEMA = "complete-R270-local-inequality-working-model-v1"
ORIGINAL_ENGINE_SHA = "7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152"
HERE = Path(__file__).resolve().parent


def _guard():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Scientific evaluation is restricted to public repository Actions")
    p = HERE / "geometry_20261114_full_angle_projection_warm.py"
    if hashlib.sha256(p.read_bytes()).hexdigest() != ORIGINAL_ENGINE_SHA:
        raise ValueError("The original all-row radial primitive changed")


def stats(a):
    a = np.asarray(a)
    finite = np.isfinite(a)
    return dict(size=int(a.size), finite_count=int(np.count_nonzero(finite)),
                minimum=float(np.min(a)) if np.all(finite) and a.size else None,
                maximum=float(np.max(a)) if np.all(finite) and a.size else None,
                negative_count=int(np.count_nonzero(a < 0)),
                zero_count=int(np.count_nonzero(a == 0)))


class LocalRows:
    """Actions of exactly the supplied frozen local B, without a dense full B."""
    def __init__(self, domain, indices):
        self.domain = domain
        self.indices = np.asarray(indices, dtype=np.int64)
        if not np.array_equal(self.indices, np.asarray(domain.local_indices)):
            raise ValueError("Condensed coordinates must equal the complete B local support")
        self.n = len(self.indices)
        self.m = int(domain.shape[0])
        self.blocks = tuple(domain.local_blocks)
        seen = np.zeros(self.m, dtype=np.int64)
        for block in self.blocks:
            rows = np.asarray(block["rows"])
            cols = np.asarray(block["local_columns"], dtype=np.int64)
            rs = block["row_slice"]
            if (rows.shape != (rs.stop-rs.start, len(cols))
                    or np.any(cols < 0) or np.any(cols >= self.n)
                    or len(np.unique(cols)) != len(cols)):
                raise ValueError("Original local block dimensions/columns changed")
            seen[rs] += 1
        if not np.all(seen == 1):
            raise ValueError("All original inequality rows must occur exactly once")
        self.calls = dict(B_local=0, BT_local=0, rows_read=0)

    def matvec(self, u):
        self.calls["B_local"] += 1
        return self.domain.local_matvec(np.asarray(u))

    def rmatvec(self, w):
        self.calls["BT_local"] += 1
        return self.domain.local_rmatvec(np.asarray(w))

    def row(self, index):
        if not 0 <= index < self.m:
            raise IndexError(index)
        self.calls["rows_read"] += 1
        for block in self.blocks:
            rs = block["row_slice"]
            if rs.start <= index < rs.stop:
                r = np.zeros(self.n)
                r[np.asarray(block["local_columns"], dtype=np.int64)] = block["rows"][index-rs.start]
                return r
        raise AssertionError("The validated original row is missing")

    def label(self, index):
        for query, block in enumerate(self.blocks):
            rs = block["row_slice"]
            if rs.start <= index < rs.stop:
                return dict(row=int(index), query_index=query,
                            kind=block.get("kind", "original-typed-query"),
                            interval=int(block["interval"]),
                            angle_index=int(index-rs.start))
        raise IndexError(index)


def solve_local_inequalities(model, domain, c, baseline_local, *,
                             max_working_rows=256, max_dual_sweeps=200,
                             deadline, progress=None):
    """Return a feasible local candidate and its explicit finite diagnostics.

    No ridge, altered Hessian, deleted constraint, outer-coordinate freeze,
    or substitute nonlinear gate is introduced. Local inverse errors and
    the raw Gram asymmetry are recorded; the Gram is not symmetrized.
    """
    _guard()
    start = time.monotonic()
    if not 1 <= max_working_rows <= 512 or not 1 <= max_dual_sweeps <= 1000:
        raise ValueError("Declare finite local working-row and coordinate-update budgets")
    if not np.isfinite(deadline):
        raise ValueError("An absolute monotonic deadline is required")
    B = LocalRows(domain, model.local_indices)
    c = np.asarray(c, dtype=float)
    g = np.asarray(model.local_gradient, dtype=float)
    center = np.asarray(model.local_center, dtype=float)
    baseline = np.asarray(baseline_local, dtype=float)
    if (c.shape != (B.m,) or np.any(~np.isfinite(c)) or np.any(c <= 0)
            or g.shape != (B.n,) or center.shape != (B.n,)
            or baseline.shape != (B.n,)
            or not all(np.all(np.isfinite(x)) for x in (g, center, baseline))):
        raise ValueError("The original complete local model/feasible-origin data changed")
    counts = dict(local_H_actions=0, local_H_inverse_calls=0)
    stages, inverse_reports, candidates = [], [], []
    active, rows, inverses, scales = [], [], [], []
    raw_rows, raw_inverses, raw_inverse_residuals = [], [], []
    G = np.zeros((0, 0))
    nu = np.zeros(0)
    labels = []
    zero = np.zeros(B.n)
    all_zero_mu = np.zeros(B.m)

    def H(u):
        counts["local_H_actions"] += 1
        value = np.asarray(model.hessian_action(u))
        if value.shape != (B.n,) or not np.all(np.isfinite(value)):
            raise FloatingPointError("The original condensed Hessian action is nonfinite")
        return value

    def value(u):
        hu = H(u)
        return float(g @ u + 0.5*(u @ hu)), hu

    def measure(u, mu, name):
        q, hu = value(u)
        slack = c+B.matvec(u)
        residual = hu+g-B.rmatvec(mu)
        if not (np.isfinite(q) and np.all(np.isfinite(slack))
                and np.all(np.isfinite(residual))):
            raise FloatingPointError("The actual condensed model evidence is nonfinite")
        worst = int(np.argmin(slack/c))
        report = dict(name=name, condensed_objective_without_constant=q,
            local_direction=identity(u), multipliers=identity(mu),
            all_original_slack=stats(slack),
            maximum_relative_violation=float(np.max(np.maximum(0., -slack)/c)),
            worst_relative_row=B.label(worst),
            worst_relative_slack=float(slack[worst]),
            worst_relative_c=float(c[worst]),
            local_stationarity_L2=float(np.linalg.norm(residual)),
            local_stationarity_Linf=float(np.max(np.abs(residual))),
            complementarity_sum=float(mu@slack),
            multipliers_nonnegative=bool(np.all(mu >= 0)),
            full_QP_optimality_claimed=False)
        return dict(u=u.copy(), mu=mu.copy(), slack=slack, residual=residual,
                    report=report, objective=q)

    def feasible(u, mu, name):
        repaired, repair = radial_feasible(B, np.asarray(u), c)
        # This local radius is applied before the outside affine recovery.
        # The scaled multiplier is merely nonnegative R267 evidence.
        point = measure(repaired, float(repair["factor"])*mu, name)
        if np.any(point["slack"] < 0):
            raise FloatingPointError("The original complete local feasibility reread failed")
        point["repair"] = repair
        candidates.append(dict(name=name, objective=point["objective"], repair=repair,
                               all_original_slack=point["report"]["all_original_slack"]))
        return point

    base = feasible(baseline, all_zero_mu, "original-C-local-coordinates")
    origin = feasible(zero, all_zero_mu, "local-zero-with-outside-to-be-optimized")
    current = measure(center, all_zero_mu, "unconstrained-local-center")
    center_report = current["report"]
    best = min((base, origin, feasible(center, all_zero_mu, "repaired-local-center")),
               key=lambda p:p["objective"])
    stop = "maximum-working-row-budget"
    stage = 0
    while True:
        slack = current["slack"]
        if np.all(slack >= 0):
            stop = "all-original-rows-feasible-at-current-local-dual-point"
            break
        if time.monotonic() >= deadline:
            stop = "local-QP-deadline"
            break
        if len(active) >= max_working_rows:
            stop = "maximum-working-row-budget"
            break
        violation = np.maximum(0., -slack)/c
        if active:
            violation[np.asarray(active, dtype=np.int64)] = -np.inf
        row_index = int(np.argmax(violation))
        if not np.isfinite(violation[row_index]) or violation[row_index] <= 0:
            stop = "only-working-rows-remain-infeasible-after-bounded-dual-updates"
            break
        rhs = B.row(row_index)
        call_start = time.monotonic()
        try:
            counts["local_H_inverse_calls"] += 1
            vinv = np.asarray(model.solve_local_H(rhs))
        except (TimeoutError, CondensationDeadline) as exc:
            stop = "local-inverse-deadline"
            inverse_reports.append(dict(row=B.label(row_index), completed=False,
                                        error=str(exc)))
            break
        if vinv.shape != (B.n,) or not np.all(np.isfinite(vinv)):
            raise FloatingPointError("A full condensed-row inverse is nonfinite")
        residual = H(vinv)-rhs
        diagonal = float(rhs@vinv)
        if not np.isfinite(diagonal) or diagonal <= 0:
            raise FloatingPointError("The actual positive local inverse row norm is not positive")
        scale = float(np.sqrt(diagonal))
        normalized_row, normalized_inverse = rhs/scale, vinv/scale
        old_n = len(active)
        newG = np.empty((old_n+1, old_n+1))
        if old_n:
            newG[:old_n, :old_n] = G
            newG[:old_n, old_n] = np.vstack(rows)@normalized_inverse
            newG[old_n, :old_n] = np.vstack(inverses)@normalized_row
        newG[old_n, old_n] = float(normalized_row@normalized_inverse)
        G = newG
        active.append(row_index)
        rows.append(normalized_row)
        inverses.append(normalized_inverse)
        raw_rows.append(rhs.copy())
        raw_inverses.append(vinv.copy())
        raw_inverse_residuals.append(residual.copy())
        scales.append(scale)
        labels.append(B.label(row_index))
        nu = np.r_[nu, 0.]
        inverse_reports.append(dict(row=B.label(row_index), completed=True,
            rhs=identity(rhs), solution=identity(vinv), residual=identity(residual),
            seconds=time.monotonic()-call_start,
            local_H_residual_L2=float(np.linalg.norm(residual)),
            local_H_residual_Linf=float(np.max(np.abs(residual))),
            raw_positive_row_norm_squared=diagonal,
            actual_row_normalization=scale,
            no_global_chain_H_inverse_called=True))
        mat = np.vstack(rows)
        invmat = np.vstack(inverses)
        norms = np.asarray(scales)
        s0 = mat@center+c[np.asarray(active)]/norms
        active_slack = s0+G@nu
        dual_rows, dual_stop = [], "maximum-dual-sweeps"
        for sweep in range(max_dual_sweeps):
            if time.monotonic() >= deadline:
                dual_stop = "local-QP-deadline"
                break
            largest = 0.
            for j in range(len(active)):
                d = float(G[j, j])
                if not np.isfinite(d) or d <= 0:
                    raise FloatingPointError("No ridge is inserted into a nonpositive working diagonal")
                new = max(0., float(nu[j]-active_slack[j]/d))
                delta = new-float(nu[j])
                if delta:
                    nu[j] = new
                    active_slack += G[:, j]*delta
                largest = max(largest, abs(delta))
            # Re-form the same cached model action each sweep, without
            # substituting its value for the final original B reread.
            active_slack = s0+G@nu
            dual_rows.append(dict(sweep=sweep+1, largest_coordinate_update=largest,
                normalized_working_slack_min=float(np.min(active_slack)),
                normalized_complementarity=float(nu@active_slack)))
            if largest == 0.:
                dual_stop = "no-representable-coordinate-update"
                break
        u = center+nu@invmat
        mu = np.zeros(B.m)
        mu[np.asarray(active)] = nu/norms
        current = measure(u, mu, "local-working-stage-%03d-unrepaired" % stage)
        point = feasible(u, mu, "local-working-stage-%03d-repaired" % stage)
        if point["objective"] < best["objective"]:
            best = point
        entry = dict(stage=stage, actual_working_rows=list(active),
            newly_added_row=labels[-1], last_dual=(dual_rows[-1] if dual_rows else None),
            completed_dual_sweeps=len(dual_rows), dual_stop_reason=dual_stop,
            working_Gram_asymmetry_Linf=float(np.max(np.abs(G-G.T))),
            no_Gram_symmetrization_or_ridge=True,
            actual_unrepaired=current["report"], local_only_radial_repair=point["repair"],
            actual_repaired=point["report"])
        stages.append(entry)
        if progress:
            progress(dict(event="condensed_local_working_stage", stage=stage,
                working_rows=len(active), unrepaired_min_slack=current["report"]["all_original_slack"]["minimum"],
                repaired_objective=point["objective"], best_objective=best["objective"],
                elapsed_seconds=time.monotonic()-start))
        stage += 1

    # Both endpoints are feasible in all original rows. Use the actual
    # condensed quadratic on their segment, then reread every rounded row.
    delta = best["u"]-base["u"]
    hd = H(delta)
    first = float((g+H(base["u"]))@delta)
    second = float(delta@hd)
    if not np.isfinite(first) or not np.isfinite(second) or second < 0:
        raise FloatingPointError("The original condensed segment model is nonfinite")
    tau = float(np.clip(-first/second, 0., 1.)) if second > 0 else 0.
    combination = base["u"]+tau*delta
    combined_mu = (1.-tau)*base["mu"]+tau*best["mu"]
    final = feasible(combination, combined_mu, "final-condensed-feasible-segment")
    if final["objective"] > base["objective"]:
        final = base
        selection = "original-C-local-finite-model-backup"
    else:
        selection = "same-condensed-objective-feasible-segment"
    report = dict(schema=SCHEMA,
        scope="Bounded optimization in the full local Schur quadratic; all outside variables recovered with their affine optimum afterward.",
        original_full_coordinate_count=int(domain.shape[1]), local_coordinate_count=B.n,
        original_inequality_row_count=B.m,
        local_indices=identity(B.indices), actual_g=identity(g),
        actual_center=identity(center),
        original_C_local=identity(baseline),
        maximum_working_rows=int(max_working_rows), actual_working_rows=list(active),
        maximum_dual_sweeps=int(max_dual_sweeps),
        active_stop_reason=stop, elapsed_seconds=time.monotonic()-start,
        local_actions=counts, original_B_actions=dict(B.calls),
        original_local_center_evidence=center_report,
        conditional_local_zero_candidate=origin["report"],
        original_C_local_candidate=base["report"],
        final_selection=selection, segment_parameter=tau,
        segment_first_derivative=first, segment_curvature=second,
        final_evidence=final["report"], final_local_radial_repair=final["repair"],
        local_repair_before_affine_outside_recovery=True,
        final_global_radial_may_break_conditional_optimality=True,
        outside_variables_not_frozen=True,
        final_full_A_AT_B_and_nonlinear_trials_not_run_in_this_module=True,
        full_QP_optimality_claimed=False,
        floating_point_readouts_are_not_validated_enclosures=True,
        no_constraints_or_control_columns_removed=True)
    return dict(local_candidate=final["u"], multipliers=final["mu"],
        local_stationarity_residual=final["residual"], original_local_slack=final["slack"],
        last_unrepaired=current, best_local_feasible=best,
        report=report, stages=stages, inverse_reports=inverse_reports,
        feasible_candidates=candidates, working_rows=np.asarray(active, dtype=np.int64),
        row_normalizations=np.asarray(scales), normalized_working_rows=(np.vstack(rows) if rows else np.zeros((0, B.n))),
        normalized_local_inverse_rows=(np.vstack(inverses) if inverses else np.zeros((0, B.n))),
        raw_working_rows=(np.vstack(raw_rows) if raw_rows else np.zeros((0, B.n))),
        raw_local_inverse_rows=(np.vstack(raw_inverses) if raw_inverses else np.zeros((0, B.n))),
        raw_local_inverse_residuals=(np.vstack(raw_inverse_residuals) if raw_inverse_residuals else np.zeros((0, B.n))),
        actual_working_Gram=G, normalized_dual=nu)
