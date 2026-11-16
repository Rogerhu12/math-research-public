#!/usr/bin/env python3
"""One new complete-grid maximin projection session; no legacy LP/cone calls.

The original 159 physical step is represented by z plus norm h and gain s.
Every finite master contains the original hard, box and norm rows. Missing
metric rows have dual multiplier zero; only a full-grid separation can qualify
a primal candidate. The exact projection/fixed-point assertions require a
nonempty full domain. A finite failure does not prove that domain empty.
"""
from __future__ import annotations

import copy
from fractions import Fraction
import hashlib
from pathlib import Path
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_budget_recovery import require_public_research_environment

POLICY = "same159-true53-complete-grid-maximin-projection-v1"
LABELS = ("coarse", "fine")
LIMITS = {
    "science_seconds": 600,
    "projection_sessions": 1,
    "prox_steps": 12,
    "sweeps": 256,
    "coordinate_updates": 1000000,
    "full_separations": 24,
    "new_metric_rows": 96,
    "first_jet_grid_builds": 2,
    "hard_J_grid_builds": 2,
    "necessary_base_geometry": 2,
    "scalar_sessions": 1,
    "scalar_queries": 64,
    "actual_trial_pairs": 3,
    "actual_grid_values": 6,
}
ALGORITHM = {
    "prox_step": 1.0,
    "sweeps_per_separation": 8,
    "projection_gap_absolute": 1e-10,
    "projection_gap_relative": 1e-8,
    "metric_original_tolerance": 1e-9,
    "hard_original_tolerance": 1e-7,
    "minimum_complete_first_order_gain": 1e-10,
    "reserve_final_direction_separation": 1,
}


def implementation_hashes():
    p = Path(__file__)
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def finite(value, shape=None, name="array"):
    a = np.asarray(value, dtype=float)
    if (shape is not None and a.shape != shape) or not np.all(np.isfinite(a)):
        raise ValueError("finite "+name+" with the declared shape required")
    return a


def exact_vector(value):
    a = finite(value, name="saved actual finite vector")
    require(a.ndim == 1, "one-dimensional actual vector required")
    return [str(Fraction.from_float(float(x))) for x in a]


def owned(value):
    a = np.array(value, dtype=float, copy=True)
    require(np.all(np.isfinite(a)), "finite readonly array required")
    a.flags.writeable = False
    return a


class ProjectionLimit(RuntimeError):
    def __init__(self, kind, used, limit):
        self.kind, self.used, self.limit = kind, used, limit
        super().__init__("new projection scope exhausted: %s %s/%s" % (kind, used, limit))


class ProjectionLedger:
    """Started calls are charged before work; this clock starts before input I/O."""
    def __init__(self, started, *, limits=None):
        now = time.monotonic()
        require(type(started) in (int, float) and np.isfinite(started)
                and 0 <= started <= now, "actual monotonic input-start clock required")
        chosen = dict(LIMITS if limits is None else limits)
        require(chosen == LIMITS, "the published independent finite scope is immutable")
        self.started, self.limits = float(started), chosen
        self.counts = {key: 0 for key in chosen if key != "science_seconds"}
        self.events = []
        self.old_backend_calls = {"HiGHS": 0, "SOC": 0, "cone": 0}
        self.check()

    def elapsed(self):
        return time.monotonic()-self.started

    def check(self):
        elapsed = self.elapsed()
        if not np.isfinite(elapsed) or elapsed > self.limits["science_seconds"]:
            raise ProjectionLimit("science_seconds", elapsed, self.limits["science_seconds"])
        return elapsed

    def charge(self, key, count=1):
        self.check()
        require(key in self.counts and type(count) is int and count > 0,
                "known finite-scope counter and positive integer debit required")
        if self.counts[key]+count > self.limits[key]:
            raise ProjectionLimit(key, self.counts[key], self.limits[key])
        self.counts[key] += count
        return self.counts[key]

    def begin(self, key, **information):
        ordinal = self.charge(key)
        event = {"counter": key, "ordinal": ordinal, "status": "started",
                 "started_science_seconds": self.elapsed(), **copy.deepcopy(information)}
        event["_monotonic_started"] = time.monotonic()
        self.events.append(event)
        return event

    def end(self, event, error=None, **information):
        tick = event.pop("_monotonic_started", None)
        if tick is not None:
            event["elapsed_seconds"] = time.monotonic()-tick
        event.update(copy.deepcopy(information))
        event["status"] = "complete" if error is None else "raised"
        if error is not None:
            event["error"] = (copy.deepcopy(error) if isinstance(error, dict)
                              else {"type": type(error).__name__, "message": str(error)})

    def report(self):
        events = copy.deepcopy(self.events)
        for event in events:
            tick = event.pop("_monotonic_started", None)
            if tick is not None:
                event["elapsed_seconds_so_far"] = time.monotonic()-tick
        return {
            "schema": POLICY+"-ledger",
            "limits": copy.deepcopy(self.limits), "started_counts": dict(self.counts),
            "scientific_seconds": self.elapsed(),
            "science_clock_includes_input_development_prepare_and_serialization": True,
            "events": events, "legacy_backend_calls": dict(self.old_backend_calls),
            "event_times_may_be_nested_not_summed_as_a_second_total": True,
            "old64_and_old32_are_closed_ancestor_accounts": True,
            "coordinate_update_debits_include_zero_change_and_literal_zero_row_visits": True,
        }


class PhysicalMetric:
    """G=diag(K.T K,1,1), using the proved identity154 plus a five-height block."""
    def __init__(self, K, *, artificial=False):
        K = finite(K, name="physical normalized map")
        require(K.ndim == 2 and K.shape[0] >= K.shape[1], "injective physical map shape required")
        self.n = K.shape[1]+2
        self.K = owned(K)
        started = time.monotonic()
        Gz = K.T@K
        self.G = np.eye(self.n)
        self.G[:self.n-2, :self.n-2] = Gz
        self.inverse = np.eye(self.n)
        if not artificial:
            require(K.shape == (163, 159), "the original 163 by159 map is required")
            require(np.array_equal(Gz[:154, :154], np.eye(154))
                    and np.count_nonzero(Gz[:154, 154:]) == 0
                    and np.count_nonzero(Gz[154:, :154]) == 0,
                    "the original identity154/physical nine-height block changed")
            chol = np.linalg.cholesky(Gz[154:, 154:])
            small = np.linalg.solve(chol.T, np.linalg.solve(chol, np.eye(5)))
            self.inverse[154:159, 154:159] = small
            factor_size = 5
        else:
            chol = np.linalg.cholesky(Gz)
            self.inverse[:self.n-2, :self.n-2] = np.linalg.solve(
                chol.T, np.linalg.solve(chol, np.eye(self.n-2)))
            factor_size = self.n-2
        require(np.all(np.isfinite(self.inverse)), "nonfinite original physical metric inverse")
        self.G.flags.writeable = self.inverse.flags.writeable = False
        self.record = {
            "physical_map_sha256": array_digest(K), "metric_sha256": array_digest(self.G),
            "metric_inverse_sha256": array_digest(self.inverse),
            "nontrivial_factor_dimension": factor_size,
            "factorization_seconds": time.monotonic()-started,
            "no_jitter_or_replacement_physical_height_norm": True,
        }

    def inverse_rows(self, A):
        return finite(A, name="row batch")@self.inverse

    def norm_squared(self, x):
        x = finite(x, (self.n,), "weighted vector")
        return float(x@self.G@x)


class HalfspaceProjection:
    """Cyclic Hildreth dual updates, with exact row provenance and a shared ledger."""
    def __init__(self, metric, rows, ledger):
        self.metric, self.ledger, self.n = metric, ledger, metric.n
        self.A = np.empty((0, self.n))
        self.b = np.empty(0)
        self.tolerances = np.empty(0)
        self.scales = np.empty(0)
        self.An = np.empty((0, self.n))
        self.bn = np.empty(0)
        self.inverse_rows = np.empty((0, self.n))
        self.kappa = np.empty(0)
        self.multipliers = np.empty(0)
        self.tags, self.kinds, self.row_keys = [], [], {}
        self.y = self.w = None
        self.zero_conflicts = []
        self.add(rows)

    def add(self, rows):
        incoming, pending = [], {}
        for row in rows:
            A = finite(row["A"], (self.n,), "original halfspace row")
            b, tol = float(row["b"]), float(row["tolerance"])
            require(np.isfinite(b) and np.isfinite(tol) and tol >= 0,
                    "finite original RHS/tolerance required")
            tag = copy.deepcopy(row["tag"])
            kind = row["kind"]
            require(kind in ("hard", "physical", "norm", "bound", "metric"),
                    "explicit original row kind required")
            key = digest({"kind": kind, "tag": tag})
            if key in self.row_keys:
                old = self.row_keys[key]
                require(np.array_equal(self.A[old], A) and self.b[old] == b
                        and self.tolerances[old] == tol,
                        "same original row identity changed inside one model")
                continue
            if key in pending:
                old = incoming[pending[key]]
                require(np.array_equal(old[0], A) and old[1] == b and old[2] == tol,
                        "duplicate incoming row identity has different coefficients")
                continue
            pending[key] = len(incoming)
            incoming.append((A.copy(), b, tol, tag, kind))
        if not incoming:
            return 0
        A = np.array([x[0] for x in incoming])
        b = np.array([x[1] for x in incoming])
        maximum = np.max(abs(A), axis=1)
        scales = np.ones(len(A))
        nonzero = maximum != 0
        scales[nonzero] = np.ldexp(np.ones(np.sum(nonzero)), np.frexp(maximum[nonzero])[1]-1)
        require(np.all(np.isfinite(scales)) and np.all(scales > 0),
                "row normalization underflow/overflow is not a zero row")
        An, bn = A/scales[:, None], b/scales
        require(np.all(np.isfinite(An)) and np.all(np.isfinite(bn)),
                "nonfinite row normalization is not an automatic constant inequality")
        inverse = self.metric.inverse_rows(An)
        kappa = np.sum(An*inverse, axis=1)
        require(np.all(np.isfinite(kappa[nonzero])) and np.all(kappa[nonzero] > 0),
                "nonzero original row has unusable weighted norm")
        require(np.all(kappa[~nonzero] == 0), "literal zero-row metric changed")
        offset = len(self.tags)
        for key, position in pending.items():
            self.row_keys[key] = offset+position
        for i in np.flatnonzero(~nonzero):
            if b[i] < 0:
                self.zero_conflicts.append({
                    "row_position": offset+int(i), "tag": copy.deepcopy(incoming[i][3]),
                    "original_rhs": float(b[i]), "original_tolerance": float(incoming[i][2]),
                    "literal_zero_coefficients": True,
                    "strict_model_inconsistent": True,
                    "within_original_numeric_tolerance": bool(-b[i] <= incoming[i][2]),
                })
        self.A = np.vstack((self.A, A))
        self.b = np.r_[self.b, b]
        self.tolerances = np.r_[self.tolerances, [x[2] for x in incoming]]
        self.scales = np.r_[self.scales, scales]
        self.An, self.bn = np.vstack((self.An, An)), np.r_[self.bn, bn]
        self.inverse_rows = np.vstack((self.inverse_rows, inverse))
        self.kappa = np.r_[self.kappa, kappa]
        self.multipliers = np.r_[self.multipliers, np.zeros(len(incoming))]
        self.tags.extend(x[3] for x in incoming)
        self.kinds.extend(x[4] for x in incoming)
        if self.y is not None:
            self.rebind_center(self.y)
        return len(incoming)

    def rebind_center(self, y):
        self.y = finite(y, (self.n,), "new actual prox center").copy()
        self.w = self.y-self.multipliers@self.inverse_rows
        finite(self.w, (self.n,), "rebound dual-stationarity vector")

    def residual(self, w):
        w = finite(w, (self.n,), "candidate")
        residual = self.A@w-self.b
        excess = residual-self.tolerances
        return {
            "maximum_original_residual": float(np.max(residual, initial=-np.inf)),
            "maximum_excess_over_original_row_tolerance": float(np.max(excess, initial=-np.inf)),
            "all_installed_rows_within_original_tolerance": bool(np.all(excess <= 0)),
            "maximum_by_kind": {
                kind: float(np.max(residual[np.array(self.kinds) == kind], initial=-np.inf))
                for kind in sorted(set(self.kinds))},
        }

    def diagnostic(self):
        require(self.y is not None and self.w is not None, "a real prox center is required")
        v = self.An.T@self.multipliers
        inverse_v = self.metric.inverse@v
        stationarity = self.w-(self.y-inverse_v)
        dual = float(self.multipliers@(self.An@self.y-self.bn)-.5*v@inverse_v)
        primal = .5*self.metric.norm_squared(self.w-self.y)
        out = self.residual(self.w)
        out.update(
            projection_primal_value_if_full_primal_feasible=primal,
            projection_dual_lower_value=dual,
            projection_gap=primal-dual,
            dual_stationarity_maximum_error=float(np.max(abs(stationarity), initial=0.)),
            negative_dual_multiplier_count=int(np.sum(self.multipliers < 0)),
            multiplier_sha256=array_digest(self.multipliers),
            original_row_count=len(self.b),
            omitted_full_metric_rows_have_multiplier_zero=True,
            original_rows_sha256=digest(self.tags),
            original_A_sha256=array_digest(self.A), original_b_sha256=array_digest(self.b),
            full_primal_feasibility_requires_separate_complete_grid_scan=True,
            no_exact_stationarity_or_infeasibility_claim=True)
        return out

    def sweep(self):
        require(self.y is not None, "rebind the prox center before a sweep")
        event = self.ledger.begin("sweeps", original_row_count=len(self.b))
        before = self.ledger.counts["coordinate_updates"]
        try:
            # Restore the stated stationarity identity; do not carry another y's vector.
            self.rebind_center(self.y)
            for i in range(len(self.b)):
                self.ledger.charge("coordinate_updates")
                if self.kappa[i] == 0:
                    continue
                residual = float(self.An[i]@self.w-self.bn[i])
                new = max(0., float(self.multipliers[i]+residual/self.kappa[i]))
                require(np.isfinite(new), "nonfinite actual dual coordinate")
                change = new-self.multipliers[i]
                self.multipliers[i] = new
                self.w -= change*self.inverse_rows[i]
            finite(self.w, (self.n,), "completed sweep vector")
            self.ledger.end(event, coordinate_updates=(
                self.ledger.counts["coordinate_updates"]-before))
            self.ledger.check()
        except Exception as error:
            self.ledger.end(event, error, coordinate_updates=(
                self.ledger.counts["coordinate_updates"]-before))
            raise
        return self.w

    def maximin_upper(self, lower_x, upper_x):
        lower_x = finite(lower_x, (self.n-1,), "original outer-domain lower bounds")
        upper_x = finite(upper_x, (self.n-1,), "original outer-domain upper bounds")
        require(np.all(lower_x <= upper_x), "ordered original outer-domain bounds required")
        lam = self.multipliers/self.scales
        mask = np.array([x == "metric" for x in self.kinds])
        total = float(np.sum(lam[mask]))
        if total <= 0 or not np.isfinite(total):
            return {"available": False, "metric_multiplier_sum": total}
        v = self.A[:, :-1].T@lam
        outer_min = float(np.where(v >= 0, lower_x, upper_x)@v)
        upper = (float(lam@self.b)-outer_min)/total
        return {
            "available": bool(np.isfinite(upper)),
            "metric_multiplier_sum": total,
            "maximin_upper_diagnostic": float(upper),
            "outer_domain_linear_minimum": outer_min,
            "all_current_gap_RHS_terms_retained": True,
            "binary64_diagnostic_not_outward_rounded_certificate": True,
        }


def _record_vector(w):
    w = finite(w, name="actual solver iterate")
    return {"binary64_vector": w.tolist(), "exact_binary64_vector": exact_vector(w),
            "vector_sha256": array_digest(w), "vector_length": len(w)}


def solve_complete_projection(model, ledger, *, result_sink=None, emit=None):
    """Return (same-process direction handle or None, JSON-safe report).

    model.scan owns the same shared separation counter. A finite best iterate
    never grants actual eligibility until the rounded direction is rescanned.
    No old backend, ordinary geometry, SOC or actual trial is called here.
    """
    require_public_research_environment()
    require(isinstance(ledger, ProjectionLedger), "the independent started-clock ledger required")
    sink = {} if result_sink is None else result_sink
    require(isinstance(sink, dict) and not sink, "fresh mutable report sink required")
    emit = (lambda record: None) if emit is None else emit
    sink.update(
        schema=POLICY+"-session", status="started",
        model_binding_sha256=model.binding_sha256,
        algorithm=copy.deepcopy(ALGORITHM), models=[], final_candidate=None,
        exact_projection_theorems_require_nonempty_full_domain=True,
        old_HiGHS_SOC_cone_calls=0)
    session = ledger.begin("projection_sessions", model_binding_sha256=model.binding_sha256)
    master = None
    best = final_handle = None
    status, raised = "finite-prox-limit", None
    search_limit = ledger.limits["full_separations"]-ALGORITHM["reserve_final_direction_separation"]
    try:
        metric = PhysicalMetric(model.K)
        sink["physical_metric"] = copy.deepcopy(metric.record)
        ledger.check()
        master = HalfspaceProjection(metric, model.hard_rows(), ledger)
        master.add(model.initial_metric_rows())
        current = np.zeros(metric.n)
        if master.zero_conflicts:
            sink["literal_zero_row_conflicts"] = copy.deepcopy(master.zero_conflicts)
            status = "strict-model-literal-zero-row-conflict"
        else:
            for k in range(ledger.limits["prox_steps"]):
                if ledger.counts["full_separations"] >= search_limit:
                    status = "search-separation-allocation-ended-one-final-slot-reserved"
                    break
                prox = ledger.begin("prox_steps", model_binding_sha256=model.binding_sha256)
                y = current.copy()
                y[-1] += ALGORITHM["prox_step"]
                master.rebind_center(y)
                record = {
                    "prox_number": k+1, "status": "started",
                    "prox_center": _record_vector(y), "separations": [],
                    "source_full_feasibility_not_assumed_from_zero_step": k == 0}
                sink["models"].append(record)
                completed = False
                try:
                    while ledger.counts["full_separations"] < search_limit:
                        for _ in range(ALGORITHM["sweeps_per_separation"]):
                            master.sweep()
                        diagnostic = master.diagnostic()
                        w = master.w.copy()
                        scan = model.scan(w, phase="projection-separation")
                        check = model.ideal_candidate(w, scan)
                        snapshot = {
                            "iterate": _record_vector(w),
                            "master": diagnostic, "full_scan": model.scan_summary(scan),
                            "candidate": copy.deepcopy(check["report"]),
                            "maximin_upper": master.maximin_upper(model.lower_x, model.upper_x)}
                        record["separations"].append(snapshot)
                        if check["qualified_primal"]:
                            if best is None or check["gain"] > best["gain"]:
                                best = {"w": check["repaired_w"].copy(), "scan": scan,
                                        "gain": float(check["gain"]),
                                        "source_prox_number": k+1,
                                        "source_report": copy.deepcopy(snapshot)}
                                model.pin_best(scan)
                                sink["best_ideal_candidate"] = {
                                    "gain": best["gain"], "source_prox_number": k+1,
                                    "repaired_vector": _record_vector(best["w"]),
                                    "requires_final_rounding_and_same_actual_direction_scan": True}
                        violations = model.violating_attainers(w, scan)
                        new_rows = [model.metric_row(item, scan) for item in violations]
                        installed = master.add(new_rows)
                        snapshot["new_original_metric_rows_installed"] = installed
                        if violations and installed == 0:
                            snapshot["same_installed_row_still_violates"] = True
                        gap = diagnostic["projection_gap"]
                        gap_tol = (ALGORITHM["projection_gap_absolute"]
                                   + ALGORITHM["projection_gap_relative"]*max(
                                       1., abs(diagnostic["projection_primal_value_if_full_primal_feasible"]),
                                       abs(diagnostic["projection_dual_lower_value"])))
                        full_raw_feasible = (not violations
                            and diagnostic["all_installed_rows_within_original_tolerance"])
                        if full_raw_feasible and -gap_tol <= gap <= gap_tol:
                            current = w
                            completed = True
                            record.update(status="numerically-complete-full-grid-projection",
                                          projection_gap_tolerance=gap_tol)
                            break
                        if ledger.counts["full_separations"] >= search_limit:
                            status = "search-separation-allocation-ended-one-final-slot-reserved"
                            break
                    if not completed:
                        record["status"] = "finite-projection-work-incomplete"
                    record["terminal_iterate"] = _record_vector(master.w)
                    ledger.end(prox, complete_projection_numeric_gate=completed)
                    emit(copy.deepcopy(record))
                    if not completed:
                        break
                except Exception as error:
                    record.update(status="raised", error={
                        "type": type(error).__name__, "message": str(error)})
                    if master.w is not None and np.all(np.isfinite(master.w)):
                        record["terminal_iterate"] = _record_vector(master.w)
                    ledger.end(prox, error)
                    emit(copy.deepcopy(record))
                    raise
        if best is None and status == "finite-prox-limit":
            status = "no-full-primal-candidate-within-finite-projection-scope"
    except ProjectionLimit as error:
        raised = error
        status = "new-projection-scope-exhausted"
        sink["budget"] = {"counter": error.kind, "used": error.used, "limit": error.limit}
    except Exception as error:
        raised = error
        status = "new-projection-interface-or-numeric-error"
        sink["error"] = {"type": type(error).__name__, "message": str(error)}

    # Exhausting coordinate work does not manufacture a fresh work allowance.
    # An already available best may use only the explicitly reserved direction
    # scan, if its own counter and the one global science clock still allow it.
    may_finalize = (best is not None
        and (raised is None or isinstance(raised, ProjectionLimit))
        and not (isinstance(raised, ProjectionLimit) and raised.kind == "science_seconds"))
    if may_finalize:
        try:
            ledger.check()
            final = model.finalize_direction(best["w"], best["scan"])
            sink["final_candidate"] = copy.deepcopy(final["report"])
            sink["final_candidate_provenance"] = {
                "source_prox_number": best["source_prox_number"],
                "best_ideal_gain": best["gain"],
                "projection_work_termination_before_finalization": status,
                "final_scan_uses_only_the_shared_predeclared_allowance": True}
            if final["qualified"]:
                final_handle = final
                status = "complete-first-order-descent-direction-qualified-for-legal-line"
            else:
                status = "best-ideal-direction-failed-final-original-domain-or-full-scan"
        except Exception as error:
            raised = error
            sink["finalization_error"] = {"type": type(error).__name__, "message": str(error)}
            status = "final-rounded-direction-not-qualified-within-scope"

    sink["status"] = status
    if master is not None:
        if master.w is not None and np.all(np.isfinite(master.w)):
            sink["last_finite_solver_iterate"] = _record_vector(master.w)
        try:
            sink["master_final"] = master.diagnostic() if master.w is not None else {
                "original_row_count": len(master.b), "zero_conflicts": copy.deepcopy(master.zero_conflicts)}
        except Exception as error:
            sink["master_final_diagnostic_error"] = {
                "type": type(error).__name__, "message": str(error)}
    if master is not None:
        # One original final state only.  Dense A/J is in the uniquely emitted
        # model record; normalized multipliers, order and scales must not vanish.
        sink["final_master_state"] = {
            "schema": POLICY+"-final-dual-state",
            "status": "actual-recorded-state-not-an-optimality-certificate",
            "normalized_dual_multipliers_binary64": master.multipliers.tolist(),
            "row_scales_binary64": master.scales.tolist(),
            "ordered_original_rows": [
                {"kind": kind, "tag": copy.deepcopy(tag),
                 "rhs": float(rhs), "original_tolerance": float(tol)}
                for kind, tag, rhs, tol in zip(
                    master.kinds, master.tags, master.b, master.tolerances)],
            "original_A_sha256": array_digest(master.A),
            "original_b_sha256": array_digest(master.b),
            "normalized_multiplier_sha256": array_digest(master.multipliers),
            "row_scale_sha256": array_digest(master.scales),
            "actual_prox_center": (
                _record_vector(master.y) if master.y is not None
                and np.all(np.isfinite(master.y)) else None),
            "actual_current_iterate": (
                _record_vector(master.w) if master.w is not None
                and np.all(np.isfinite(master.w)) else None),
            "dense_A_and_G_not_duplicated": True,
            "actual_row_order_cannot_be_replaced_by_a_sorted_set": True,
        }
    sink["complete_primal_or_stationarity_not_inferred_from_status_name"] = True
    ledger.end(session, raised, final_status=status)
    sink["ledger"] = ledger.report()
    return final_handle, sink


def guard_compatible_interval(values, slopes, targets, *, residual_tolerance,
                              physical_bounds=()):
    """Frozen hard targets can impose a positive lower endpoint; never reset base."""
    values = finite(values, name="hard base values")
    slopes, targets = finite(slopes, values.shape), finite(targets, values.shape)
    require(values.ndim == 1 and np.isfinite(residual_tolerance) and residual_tolerance >= 0,
            "original finite hard-row domain and tolerance required")

    def intersect(tolerance):
        lower, upper, blockers = 0., 1., []
        rows = [(float(v), float(a), float(t), i, "hard")
                for i, (v, a, t) in enumerate(zip(values, slopes, targets))]
        rows.extend((float(v), float(a), float(t), i, "physical")
                    for i, (v, a, t) in enumerate(physical_bounds))
        require(all(np.isfinite(v) and np.isfinite(a) and np.isfinite(t)
                    for v, a, t, _, _ in rows), "finite original physical interval rows required")
        for value, slope, target, index, kind in rows:
            tol = tolerance if kind == "hard" else 0.
            rhs = target-tol-value
            if slope > 0:
                endpoint = rhs/slope
                if endpoint > lower:
                    lower = endpoint
            elif slope < 0:
                endpoint = rhs/slope
                if endpoint < upper:
                    upper = endpoint
            elif rhs > 0:
                blockers.append({"kind": kind, "index": index, "value": value,
                                 "target": target, "slope": slope, "rhs": rhs})
            if lower > upper:
                blockers.append({"kind": kind, "index": index, "lower": lower, "upper": upper})
        finite_interval = np.isfinite(lower) and np.isfinite(upper)
        nonempty = not blockers and finite_interval and lower <= upper
        return {"lower": lower, "upper": upper, "nonempty": bool(nonempty),
                "singleton": bool(nonempty and lower == upper),
                "zero_in_interval": bool(nonempty and lower <= 0 <= upper),
                "blockers": blockers}
    return {
        "exact_original_target_interval": intersect(0.),
        "original_numeric_tolerance_interval": intersect(float(residual_tolerance)),
        "original_residual_tolerance": float(residual_tolerance),
        "physical_box_interval_has_no_new_tolerance": True,
        "all_scalar_gains_reference_true_alpha_zero_not_the_lower_endpoint": True,
    }
