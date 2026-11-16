#!/usr/bin/env python3
"""True55 fixed-old159 / new-nine finite row exchange, import-only.

The geometry helper owns exactly two new selected-J9 builds and two complete
metric9 builds.  This module does not evaluate geometry or any derivative.
The finite oracle is the COMPLETE BASELINE FIRST-ORDER max
    max(target, max_i(phi_i(0) + grad(phi_i)(0) . delta9)).
The later scalar oracle is separately phi(e0+alpha*de, f0+alpha*df).
These two functions and their certificates are never interchanged.
"""
from __future__ import annotations
import copy
import math
from fractions import Fraction as Q
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_complete_maximin_projection import guard_compatible_interval
from frame_metric_true55_nine_fiber_scope import (
    POLICY, LIMITS, VARIABLES, NINE, STEP_SCALE, NORM_WEIGHT,
    NineFiberLedger, require)
from frame_metric_true55_nine_fiber_solver import solve_nine_fiber, vector_record

HARD_TOLERANCE = 1.e-7
SOFT_TOLERANCE = 1.e-9

def _array(value, shape=None, name="array"):
    if isinstance(value, dict):
        require("values" in value and "shape" in value
                and "array_sha256" in value, name+" payload is incomplete")
        a = np.asarray(value["values"], dtype=np.float64)
        require(list(a.shape) == value["shape"]
                and array_digest(a) == value["array_sha256"],
                name+" payload identity changed")
    else:
        a = np.asarray(value, dtype=np.float64)
    require((shape is None or a.shape == shape) and np.all(np.isfinite(a)),
            "finite "+name+" with the declared shape is required")
    a = a.copy()
    a.setflags(write=False)
    return a

def _payload(value):
    a = np.asarray(value)
    require(a.dtype.kind in "fiu" and np.all(np.isfinite(a)), "finite numeric payload required")
    return {"values": a.tolist(), "shape": list(a.shape), "dtype": str(a.dtype),
            "array_sha256": array_digest(a)}

def _scalar(value, name):
    require(not isinstance(value, (bool, np.bool_)), name+" must be numeric")
    result = float(value)
    require(math.isfinite(result), "finite "+name+" required")
    return result

def _tag_key(tag):
    require(isinstance(tag, dict) and tag.get("grid") in ("coarse", "fine")
            and isinstance(tag.get("flat_row_id"), (int, np.integer))
            and not isinstance(tag.get("flat_row_id"), (bool, np.bool_)),
            "an original grid and literal integer row ID are required")
    return tag["grid"], int(tag["flat_row_id"])

def _exact172(field, state):
    values = field.full_coefficients(state, exact=True)
    require(len(values) == 172 and all(isinstance(v, Q) for v in values),
            "the real new172 affine physical coefficients are required")
    return [str(v) for v in values]

class NineFiberModel:
    """Pure assembly from one newly bound helper.model_input() at true55.

    prepared keys:
      field168, q168, lower172, upper172, initial159, cfg, row_grids,
      source_binding (JSON metadata).
    jets.model_input() keys:
      original_domain{hard_J9,hard_base_values,hard_targets,
        hard_original_row_tags,selected_metric_gradients9_of_phi,
        selected_metric_base_phi,selected_metric_original_row_tags,
        fixed_outside_phi},
      complete_phi0,target,binding,binding_sha256,center168,source55.
    Source55 is 55 or a receipt with source_accepted_index=55.

    No constructor operation requests geometry, J, JVP, a master solve, or
    any closed-task check.  The scalar model arrays are already paid new inputs.
    """
    def __init__(self, prepared, jets, *, ledger):
        require(isinstance(ledger, NineFiberLedger), "one shared new-nine ledger required")
        self.ledger, self.jets = ledger, jets
        ledger.check("nine-model.entry")
        self.field = prepared["field168"]
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.state = _array(prepared["q168"], (168,), "current zero-nine168")
        old = _array(prepared["initial159"], (159,), "fixed true55 independent159")
        require(np.array_equal(self.state[:159], old)
                and np.array_equal(self.state[159:], np.zeros(9)),
                "old159 must be true55 and the genuinely new nine start at literal zero")
        self.field.validate_state(self.state)
        self.lower172 = _array(prepared["lower172"], (172,), "physical lower172")
        self.upper172 = _array(prepared["upper172"], (172,), "physical upper172")
        require(np.all(self.lower172 < self.upper172)
                and np.array_equal(self.lower172[163:], np.full(9, -.25))
                and np.array_equal(self.upper172[163:], np.full(9, .25)),
                "all old physical boxes plus the literal new9 +/-1/4 box are required")
        self.center_box = self.field.exact_full_box_decision(
            self.state, self.lower172, self.upper172)
        require(self.center_box["exact_full_box_pass"], "the exact current172 box must pass")
        self.grids = prepared["row_grids"]
        require(set(self.grids) == {"coarse", "fine"}, "both original grids are required")
        self.source_binding = copy.deepcopy(prepared["source_binding"])
        require(isinstance(self.source_binding, dict)
                and self.source_binding.get("accepted_index") == 55
                and self.source_binding.get("independent159_array_sha256") == array_digest(old),
                "explicit true55 source binding and original independent vector are required")
        data = jets.model_input()
        require(isinstance(data, dict) and isinstance(data["binding"], dict)
                and digest(data["binding"]) == data["binding_sha256"],
                "one complete newly built nine-input binding is required")
        require(data["binding_sha256"] == jets.binding_sha256
                and np.array_equal(_array(data["center168"], (168,)), self.state),
                "the cached nine jets must belong to this exact center")
        source = data["source55"]
        require(source == 55 if type(source) is int else
                isinstance(source, dict) and source.get("source_accepted_index",
                    source.get("accepted_index")) == 55,
                "this is only the true55 new-nine fiber")
        self.input_binding = copy.deepcopy(data["binding"])
        self.input_binding_sha256 = data["binding_sha256"]
        self.target = _scalar(data["target"], "target")
        self.phi0 = _scalar(data["complete_phi0"], "complete smoothed baseline")
        self.epsilon = float(Q(self.cfg["metric_proposal_epsilon_exact"]))
        self.floor = float(self.cfg["linear_model_improvement_floor"])
        require(self.target == .26 and self.epsilon == 1.e-8
                and self.phi0 >= self.target and math.isfinite(self.floor) and self.floor > 0.
                and float(self.cfg["linear_model_residual_limit"]) == HARD_TOLERANCE
                and float(self.cfg["metric_row_tolerance"]) == SOFT_TOLERANCE,
                "the original target, smooth metric, improvement and row tolerances are fixed")
        d = data["original_domain"]
        self.hard_tags = copy.deepcopy(d["hard_original_row_tags"])
        self.soft_tags = copy.deepcopy(d["selected_metric_original_row_tags"])
        nhard, nsoft = len(self.hard_tags), len(self.soft_tags)
        self.hard_J = _array(d["hard_J9"], (nhard, 9), "new hard J9")
        self.hard_base = _array(d["hard_base_values"], (nhard,), "hard base")
        self.hard_targets = _array(d["hard_targets"], (nhard,), "frozen hard targets")
        self.soft_g = _array(d["selected_metric_gradients9_of_phi"], (nsoft, 9),
                             "baseline metric gradients9")
        self.soft_phi = _array(d["selected_metric_base_phi"], (nsoft,), "selected phi0")
        self.fixed_outside_phi = _scalar(d["fixed_outside_phi"], "fixed outside phi")
        self.rho_floor = max(self.target, self.fixed_outside_phi)
        require(self.phi0 >= self.rho_floor,
                "complete baseline must include the unchanged exterior and constant target")
        hard_keys, soft_keys = [], []
        for tags, keys, hard in ((self.hard_tags, hard_keys, True),
                                (self.soft_tags, soft_keys, False)):
            for tag in tags:
                key = _tag_key(tag)
                original = self.grids[key[0]].coordinate(key[1])
                require(original == tag, "the exact original row coordinate/branch changed")
                require((original["group"] >= 2) if hard else (original["group"] < 2),
                        "a scalar row was placed in the wrong hard/soft group")
                t = Q(original["t_exact"])
                require(Q(9, 250) < t < Q(423, 500),
                        "only rows on the true new-nine open support are variable")
                keys.append(key)
        require(len(set(hard_keys)) == nhard and len(set(soft_keys)) == nsoft,
                "original selected row IDs must be unique within each full domain")
        # The helper is responsible for original outside-hard checks.  Their
        # receipt remains attached; outside soft rows are rho_floor, not missing J.
        self.input_domain_receipt = copy.deepcopy(data.get("domain_receipt", {}))
        self.known = set(soft_keys)
        self.additional_rows = []
        self.extra_A, self.extra_b = [], []
        self.problems, self.finite_results = [], []
        self.last_result, self.last_candidate, self.last_handle = None, None, None
        self.last_finite_x = np.r_[np.zeros(9), self.phi0, 0.]
        self._build_initial_matrix()
        self.binding = {
            "schema": POLICY+"-original-new-nine-model",
            "source_binding": self.source_binding,
            "new_input_binding_sha256": self.input_binding_sha256,
            "current168_sha256": array_digest(self.state),
            "physical172_exact_sha256": digest(_exact172(self.field, self.state)),
            "lower172_sha256": array_digest(self.lower172),
            "upper172_sha256": array_digest(self.upper172),
            "configuration_sha256": digest(self.cfg),
            "hard_original_row_tags": self.hard_tags,
            "hard_J9_sha256": array_digest(self.hard_J),
            "hard_base_sha256": array_digest(self.hard_base),
            "hard_targets_sha256": array_digest(self.hard_targets),
            "initial_metric_original_row_tags": self.soft_tags,
            "initial_metric_g9_sha256": array_digest(self.soft_g),
            "initial_metric_phi0_sha256": array_digest(self.soft_phi),
            "fixed_outside_phi": self.fixed_outside_phi,
            "rho_floor": self.rho_floor, "complete_phi0": self.phi0,
            "step_scale": STEP_SCALE, "norm_weight": NORM_WEIGHT,
            "variable_order": "z9,rho,h", "objective": "rho+1e-6*h",
            "old159_defect_learning_or_normalization_transferred": False,
            "initial_A_sha256": array_digest(self.initial_A),
            "initial_b_sha256": array_digest(self.initial_b),
            "initial_tolerances_sha256": array_digest(self.initial_tol),
        }
        self.binding_sha256 = digest(self.binding)
        ledger.check("nine-model.complete")

    def _build_initial_matrix(self):
        blocks, rhs, kinds, origins = [], [], [], []
        def append(A, b, kind, origin):
            A, b = np.asarray(A, float), np.asarray(b, float)
            require(A.ndim == 2 and A.shape[1] == 11 and b.shape == (len(A),)
                    and np.all(np.isfinite(A)) and np.all(np.isfinite(b)),
                    "finite eleven-variable row block required")
            start = sum(len(v) for v in rhs)
            blocks.append(A); rhs.append(b); kinds.extend([kind]*len(A))
            origins.append({"start": start, "count": len(A), "kind": kind, "origin": origin})
        append(np.column_stack((-STEP_SCALE*self.hard_J, np.zeros((len(self.hard_J), 2)))),
               self.hard_base-self.hard_targets, "hard", "all variable selected hard J9")
        append(np.column_stack((STEP_SCALE*self.soft_g, -np.ones(len(self.soft_g)),
                                np.zeros(len(self.soft_g)))),
               -self.soft_phi, "metric", "all variable selected baseline metric gradients9")
        bounds = np.zeros((18, 11))
        for j in range(9):
            bounds[2*j, j], bounds[2*j+1, j] = 1., -1.
        append(bounds, np.ones(18), "bound", "literal new coefficients +/-1/4 with delta=.25*z")
        norm = bounds.copy()
        norm[:, 10] = -1.
        append(norm, np.zeros(18), "norm", "all nine +z-h and -z-h")
        h_bounds = np.zeros((2, 11)); h_bounds[0, 10] = -1.; h_bounds[1, 10] = 1.
        append(h_bounds, np.array([0., 1.]), "bound", "literal 0<=h<=1")
        rho = np.zeros((1, 11)); rho[0, 9] = -1.
        append(rho, np.array([-self.rho_floor]), "metric",
               "constant target and complete invariant exterior maximum")
        self.initial_A, self.initial_b = np.vstack(blocks), np.concatenate(rhs)
        self.initial_kind, self.origins = kinds, origins
        self.initial_tol = np.array([SOFT_TOLERANCE if k == "metric" else HARD_TOLERANCE
                                     for k in kinds])
        self.initial_A.setflags(write=False); self.initial_b.setflags(write=False)
        self.initial_tol.setflags(write=False)

    def add(self, gradient, *, source):
        self.ledger.check("nine-model.add")
        tag = copy.deepcopy(gradient["original_row"])
        key = _tag_key(tag)
        require(key == (gradient["grid"], int(gradient["flat_row_id"]))
                and self.grids[key[0]].coordinate(key[1]) == tag and tag["group"] < 2,
                "one exact original metric row is required")
        if key in self.known:
            return False
        require(Q(9, 250) < Q(tag["t_exact"]) < Q(423, 500),
                "outside metric rows are already covered by the fixed rho floor")
        g = _array(gradient["gradient"], (9,), "new baseline metric gradient9")
        require(array_digest(g) == gradient["gradient_sha256"],
                "the new materialized baseline gradient hash changed")
        require(gradient["binding_sha256"] == self.input_binding_sha256,
                "a new row from another center or family cannot enter this master")
        base = _scalar(gradient["base_phi"], "new row phi0")
        rec = {
            "grid": key[0], "flat_row_id": key[1], "original_row": tag,
            "gradient9": g.tolist(), "gradient_sha256": array_digest(g),
            "base_phi": base, "source": copy.deepcopy(source),
            "input_binding_sha256": self.input_binding_sha256,
            "linearization_point": "same true55 zero-nine baseline",
            "not_a_tangent_at_the_new_direction": True}
        self.extra_A.append(np.r_[STEP_SCALE*g, -1., 0.])
        self.extra_b.append(-base)
        self.additional_rows.append(rec)
        self.known.add(key)
        return True

    def assemble(self):
        self.ledger.check("nine-model.assemble")
        A = (np.vstack((self.initial_A, np.asarray(self.extra_A)))
             if self.extra_A else self.initial_A.copy())
        b = np.r_[self.initial_b, np.asarray(self.extra_b)]
        tol = np.r_[self.initial_tol, np.full(len(self.extra_b), SOFT_TOLERANCE)]
        kinds = self.initial_kind+["metric"]*len(self.extra_b)
        binding = {
            "source_model_binding_sha256": self.binding_sha256,
            "additional_original_rows": [
                {k: copy.deepcopy(v) for k, v in row.items() if k != "gradient9"}
                for row in self.additional_rows],
            "A_sha256": array_digest(A), "b_sha256": array_digest(b),
            "row_tolerance_sha256": array_digest(tol),
            "row_kind_sha256": digest(kinds),
            "row_count": len(b), "columns": 11,
            "objective": "rho+1e-6*h", "step_scale": STEP_SCALE}
        return {"A": A, "b": b, "row_tol": tol, "row_kind": kinds,
                "initial_x": self.last_finite_x.copy(),
                "binding": binding, "binding_sha256": digest(binding)}

    def residual(self, delta9):
        self.ledger.check("nine-model.domain-residual")
        delta = _array(delta9, (9,), "actual new coefficient displacement9")
        z = delta/STEP_SCALE
        hard = self.hard_targets-(self.hard_base+self.hard_J@delta)
        h = float(np.max(np.abs(z), initial=0.))
        return {
            "hard_maximum_signed_residual": float(np.max(hard, initial=-np.inf)),
            "hard_maximum_positive_tolerance_excess":
                float(np.max(hard-HARD_TOLERANCE, initial=0.)),
            "all_selected_hard_targets_pass": bool(np.all(hard <= HARD_TOLERANCE)),
            "hard_row_count": len(hard), "hard_tolerance": HARD_TOLERANCE,
            "new_normalized_coefficient_infinity_norm": h,
            "literal_nine_trust_and_box_pass": bool(np.all(np.abs(z) <= 1.)),
            "no_old163_norm_or_learned159_gamma_used": True}

    def validate_actual_candidate(self, candidate168):
        self.ledger.check("nine-model.actual-candidate")
        q = _array(candidate168, (168,), "actual candidate168")
        self.field.validate_state(q)
        fixed = bool(np.array_equal(q[:159], self.state[:159]))
        delta = q[159:]-self.state[159:]
        rows = self.residual(delta)
        box = self.field.exact_full_box_decision(q, self.lower172, self.upper172)
        eligible = bool(fixed and rows["all_selected_hard_targets_pass"]
                        and rows["literal_nine_trust_and_box_pass"]
                        and box["exact_full_box_pass"])
        return {
            "eligible": eligible, "model_binding_sha256": self.binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "old159_exactly_fixed": fixed, "actual_delta9": vector_record(delta),
            "actual_candidate168": vector_record(q),
            "actual_physical_exact172": _exact172(self.field, q),
            "exact172_box": copy.deepcopy(box), "new_fiber_domain": rows,
            "no_geometry_or_derivative_call_in_this_check": True,
            "linear_hard_prediction_is_not_the_actual_fourteen_gate_decision": True}

    def finite_candidate(self, raw_x, *, assembled=None):
        if raw_x is None:
            return None
        x = _array(raw_x, (11,), "real last finite11")
        d = self.assemble() if assembled is None else assembled
        z, delta = x[:9], STEP_SCALE*x[:9]
        h = float(np.max(np.abs(z), initial=0.))
        soft_value = self.soft_phi+self.soft_g@delta
        rho = max(self.rho_floor, float(np.max(soft_value, initial=-np.inf)))
        for row in self.additional_rows:
            rho = max(rho, row["base_phi"]+float(np.asarray(row["gradient9"])@delta))
        repaired = np.r_[z, rho, h]
        residual = d["A"]@repaired-d["b"]
        metric = np.asarray(d["row_kind"], dtype=object) == "metric"
        hard_ok = bool(np.all(residual[~metric] <= d["row_tol"][~metric]))
        soft_ok = bool(np.all(residual[metric] <= d["row_tol"][metric]))
        q = self.state.copy()
        q[159:] = self.state[159:]+delta
        actual = q[159:]-self.state[159:]
        domain = self.validate_actual_candidate(q)
        gain = self.phi0-rho-NORM_WEIGHT*h
        return {
            "schema": POLICY+"-finite-only-candidate",
            "original_last_finite11": vector_record(x),
            "repaired_finite11": vector_record(repaired),
            "delta9": vector_record(actual), "unit_candidate168": vector_record(q),
            "unit_physical_exact172": _exact172(self.field, q),
            "raw_rho": float(x[9]), "raw_h": float(x[10]),
            "repaired_rho": rho, "repaired_h": h,
            "finite_repaired_gain": gain, "complete_phi0": self.phi0,
            "original_finite_maximum_row_violation":
                max(0., float(np.max(residual, initial=0.))),
            "original_finite_maximum_tolerance_excess":
                max(0., float(np.max(residual-d["row_tol"], initial=0.))),
            "all_finite_hard_norm_bound_rows_pass": hard_ok,
            "all_present_metric_rows_pass_after_upward_rho_repair": soft_ok,
            "exact_domain": domain,
            "finite_positive_primal": bool(hard_ok and soft_ok and domain["eligible"]
                                          and gain > self.floor),
            "rho_repair_changes_no_direction_or_physical_coefficients": True,
            "full_grid_separation_and_true_actual_gates_still_required": True,
            "actual_geometry_evaluated": False}

    def solve(self, *, emit):
        d = self.assemble()
        result = solve_nine_fiber(
            d["A"], d["b"], d["row_tol"], d["row_kind"], d["initial_x"],
            ledger=self.ledger, problem_binding=d["binding_sha256"],
            added_row_count=len(self.additional_rows))
        # Retain the raw return before candidate filters or output callbacks.
        result["problem_binding"] = copy.deepcopy(d["binding"])
        result["problem_binding_sha256"] = d["binding_sha256"]
        result["new_finite_problem_number"] = len(self.problems)+1
        self.last_result = result
        self.finite_results.append(result)
        summary = {
            "number": len(self.problems)+1,
            "problem_binding": copy.deepcopy(d["binding"]),
            "problem_binding_sha256": d["binding_sha256"],
            "rows": len(d["b"]), "added_original_rows": len(self.additional_rows),
            "solver_status": result["status"],
            "per_problem_account": copy.deepcopy(result["ledger"]),
            "last_summary": copy.deepcopy(result.get("last_summary")),
            "terminal": copy.deepcopy(result.get("terminal")),
            "raw_returned_finite11": copy.deepcopy(result.get("last_finite_x_record"))}
        self.problems.append(summary)
        if result.get("last_finite_x") is not None:
            self.last_finite_x = _array(result["last_finite_x"], (11,), "returned finite11").copy()
        # The paid raw return remains recoverable even if this post-solve
        # ordinary-unit diagnosis discovers that the shared clock is exhausted.
        try:
            candidate = self.finite_candidate(result.get("last_finite_x"), assembled=d)
        except Exception as error:
            result["candidate_diagnostic_error"] = {
                "type": type(error).__name__, "message": str(error)}
            summary["candidate_diagnostic_error"] = copy.deepcopy(
                result["candidate_diagnostic_error"])
            # Essential preservation only: no new mathematical query follows
            # this stop, even when its cause was the shared deadline.
            summary["original_result_receipt"] = emit("FINITE_RESULT", result)
            raise
        self.last_candidate = candidate
        result["candidate"] = candidate
        receipt = emit("FINITE_RESULT", result)
        summary["original_result_receipt"] = copy.deepcopy(receipt)
        summary["finite_candidate"] = copy.deepcopy(candidate)
        self.ledger.check("nine-model.solve.after-output")
        return result, candidate, summary

    def rounded_direction(self, candidate):
        require(isinstance(candidate, dict) and "delta9" in candidate,
                "the actual newly returned finite candidate is required")
        ideal = _array(candidate["delta9"]["binary64"], (9,), "new finite direction9")
        require(array_digest(ideal) == candidate["delta9"]["array_sha256"],
                "new finite direction identity changed")
        q = self.state.copy()
        q[159:] = self.state[159:]+ideal
        delta = q[159:]-self.state[159:]
        return {"candidate": q, "direction": delta, "ideal_direction": ideal,
                "preliminary_original_domain": self.validate_actual_candidate(q),
                "rounding_changed": not np.array_equal(delta, ideal)}

    def finish_direction(self, rounded, scan):
        delta = _array(rounded["direction"], (9,), "completed scan direction9")
        require(scan["binding_sha256"] == self.input_binding_sha256
                and np.array_equal(_array(scan["direction"], (9,)), delta),
                "the complete two-grid scan must use this same rounded baseline direction")
        maximum = _scalar(scan["linear_maximum"], "complete first-order maximum")
        require(maximum >= self.target, "the constant target branch cannot be dropped")
        domain = rounded["preliminary_original_domain"]
        h = domain["new_fiber_domain"]["new_normalized_coefficient_infinity_norm"]
        gain = self.phi0-maximum-NORM_WEIGHT*h
        physical = [(float(.25-v), -float(d), 0.) for v, d in zip(self.state[159:], delta)]
        physical.extend((float(v+.25), float(d), 0.) for v, d in zip(self.state[159:], delta))
        interval = guard_compatible_interval(
            self.hard_base, self.hard_J@delta, self.hard_targets,
            residual_tolerance=HARD_TOLERANCE, physical_bounds=physical)
        numeric_interval = interval["original_numeric_tolerance_interval"]
        qualified = bool(domain["eligible"] and gain > self.floor
                         and numeric_interval["nonempty"])
        report = {
            "schema": POLICY+"-complete-first-order-direction",
            "model_binding_sha256": self.binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "direction9": vector_record(delta),
            "unit_candidate168": vector_record(rounded["candidate"]),
            "unit_physical_exact172": _exact172(self.field, rounded["candidate"]),
            "original_new_fiber_domain": copy.deepcopy(domain),
            "complete_baseline_phi0": self.phi0,
            "complete_first_order_maximum": maximum,
            "new_normalized_coefficient_norm_h": h,
            "new_norm_cost": NORM_WEIGHT*h, "complete_repaired_gain": gain,
            "minimum_gain": self.floor,
            "complete_coverage": copy.deepcopy(scan["coverage"]),
            "complete_branch_attainers": copy.deepcopy(scan["branches"]),
            "guard_compatible_alpha_interval": copy.deepcopy(interval),
            "qualified_first_order_direction": qualified,
            "actual_unit_candidate_evaluated": False,
            "full_first_order_model_is_not_affine_observable_nonlinear_phi": True,
            "affine_observable_scalar_layer_and_actual_gates_still_required": True}
        handle = {"qualified": qualified, "direction": delta,
                  "candidate": rounded["candidate"], "scan": scan,
                  "interval": interval, "report": report}
        self.last_handle = handle
        return handle

    def report(self):
        return {
            "schema": POLICY+"-finite-exchange-report",
            "model_binding": copy.deepcopy(self.binding),
            "model_binding_sha256": self.binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "initial_row_groups": copy.deepcopy(self.origins),
            "initial_rows": len(self.initial_b), "variable_count": 11,
            "additional_original_rows": copy.deepcopy(self.additional_rows),
            "problems": copy.deepcopy(self.problems),
            "last_raw_finite11": (copy.deepcopy(self.last_result.get("last_finite_x_record"))
                                  if self.last_result else None),
            "last_finite_candidate": copy.deepcopy(self.last_candidate),
            "last_complete_direction": (copy.deepcopy(self.last_handle["report"])
                                        if self.last_handle is not None else None),
            "old159_fixed": True, "new_method_normalization": ".25*z9; h>=||z9||inf",
            "rho_means_actual_smoothed_metric_upper_bound_not_excess": True,
            "old159_defect_gamma_and_normalized163_norm_not_migrated": True,
            "geometric_acceptance_is_never_inferred_from_a_finite_stop": True}

    def full_record(self):
        """One stdout-only record.  No ordinary positions or complete metric9 tensor."""
        return {
            **self.report(),
            "center168": vector_record(self.state),
            "center_physical_exact172": _exact172(self.field, self.state),
            "physical_lower172": _payload(self.lower172),
            "physical_upper172": _payload(self.upper172),
            "original_domain": {
                "hard_original_row_tags": copy.deepcopy(self.hard_tags),
                "hard_J9": _payload(self.hard_J),
                "hard_base_values": _payload(self.hard_base),
                "hard_frozen_targets": _payload(self.hard_targets),
                "selected_metric_original_row_tags": copy.deepcopy(self.soft_tags),
                "selected_metric_gradients9_of_phi": _payload(self.soft_g),
                "selected_metric_base_phi": _payload(self.soft_phi),
                "fixed_outside_phi": self.fixed_outside_phi,
                "rho_floor": self.rho_floor,
                "input_domain_receipt": copy.deepcopy(self.input_domain_receipt)},
            "finite_result_original_stdout_receipts": [
                copy.deepcopy(p.get("original_result_receipt")) for p in self.problems],
            "unemitted_real_finite_results_including_raw11_dual_slack_residual": [
                copy.deepcopy(result) for i,result in enumerate(self.finite_results)
                if i >= len(self.problems) or not self.problems[i].get("original_result_receipt")],
            "already_emitted_finite_numeric_arrays_not_duplicated": True,
            "complete_metric9_tensor_is_only_in_process_not_published_here": True,
            "old159_J_not_recomputed_or_synthesized": True}

def compact_scan(scan):
    """Only original scan values; large directional arrays have one separate cache."""
    return {key: copy.deepcopy(scan[key]) for key in (
        "schema", "binding_sha256", "linear_maximum", "branches", "coverage",
        "direction_sha256", "scope", "ordinal", "elapsed_seconds")
        if key in scan}

def exchange_nine_fiber(model, jets, ledger, *, emit, progress):
    require(isinstance(model, NineFiberModel) and model.jets is jets
            and model.ledger is ledger and isinstance(progress, dict) and not progress,
            "one new model, cache owner and empty progress sink are required")
    progress.update(schema=POLICY+"-complete-first-order-row-exchange",
                    status="started", rounds=[], new_gradient_records=[],
                    source_accepted_index=55)
    handle = last_scan = None
    for number in range(1, LIMITS["finite_master_calls"]+1):
        ledger.check("nine-exchange.before-master")
        result, candidate, finite = model.solve(emit=emit)
        item = {"number": number,
                "problem_binding_sha256": finite["problem_binding_sha256"],
                "finite_result_receipt": copy.deepcopy(finite.get("original_result_receipt")),
                "solver_status": result["status"]}
        progress["rounds"].append(item)
        if candidate is None or not candidate["finite_positive_primal"]:
            item["status"] = "no-observed-domain-qualified-positive-finite-primal"
            progress["status"] = item["status"]
            break
        rounded = model.rounded_direction(candidate)
        item["rounded_domain"] = copy.deepcopy(rounded["preliminary_original_domain"])
        if not rounded["preliminary_original_domain"]["eligible"]:
            item["status"] = "new-nine-rounded-domain-rejected"
            progress["status"] = item["status"]
            break
        last_scan = jets.scan(rounded["direction"], phase="finite-problem-"+str(number))
        handle = model.finish_direction(rounded, last_scan)
        record = compact_scan(last_scan)
        record.update(new_finite_problem_number=number,
                      actual_direction9=vector_record(rounded["direction"]),
                      qualification=copy.deepcopy(handle["report"]))
        item["full_grid_scan_receipt"] = emit("FULL_GRID_SCAN", record)
        item["qualification"] = copy.deepcopy(handle["report"])
        if handle["qualified"]:
            item["status"] = "complete-first-order-nine-direction-qualified"
            progress["status"] = item["status"]
            progress["selected_round"] = number
            break
        # Only original source tags not yet present may enlarge this fixed
        # baseline-linear model.  A new tangent at the same tag is not permitted.
        added, seen = [], set()
        for attainer in last_scan["branches"]:
            key = (attainer["grid"], int(attainer["flat_row_id"]))
            if key in seen or key in model.known:
                continue
            seen.add(key)
            tag = model.grids[key[0]].coordinate(key[1])
            if not (Q(9, 250) < Q(tag["t_exact"]) < Q(423, 500)):
                continue
            row = jets.attainer_gradient(key[0], key[1], scan=last_scan)
            if model.add(row, source={"round": number,
                                     "full_grid_scan_receipt":
                                         copy.deepcopy(item["full_grid_scan_receipt"])}):
                receipt = emit("ATTAINER_GRADIENT", row)
                progress["new_gradient_records"].append({
                    "row": copy.deepcopy(row), "original_record_receipt": receipt})
                added.append({"grid": key[0], "flat_row_id": key[1],
                              "gradient_sha256": row["gradient_sha256"],
                              "original_record_receipt": receipt})
        item["new_rows_before_next_problem"] = added
        item["status"] = "strictly-new-original-row-added" if added else "no-new-original-row"
        if not added:
            progress["status"] = "unqualified-no-new-row-no-identical-master-retry"
            break
    else:
        progress["status"] = "declared-sixteen-new-row-set-scope-completed"
    progress["final_complete_direction_qualified"] = bool(handle is not None and handle["qualified"])
    progress["inexact_or_unqualified_stop_is_not_an_infeasibility_or_stationarity_proof"] = True
    progress["full_first_order_separation_distinct_from_scalar_affine_observable_prediction"] = True
    return handle, last_scan
