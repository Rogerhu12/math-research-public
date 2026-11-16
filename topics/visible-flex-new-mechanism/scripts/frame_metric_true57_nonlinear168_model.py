#!/usr/bin/env python3
"""True57 joint168/physical172 finite row exchange; import-only.

All 168 current independent coordinates can move.  The new normalization is
h >= 4 ||M172x168 delta168||_infinity, with 0 <= h <= 1/128.  The finite oracle
is the complete BASELINE FIRST-ORDER metric maximum.  The later seven actual
binary64 candidates use separate nonlinear metric and curvature predictors.  No geometry, derivative,
JVP or solver is called by construction of this object.
"""
from __future__ import annotations
import copy
import math
from fractions import Fraction as Q
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_complete_maximin_projection import guard_compatible_interval
from frame_metric_true57_nonlinear168_scope import (
    POLICY, LIMITS, VARIABLES, INDEPENDENT, PHYSICAL, RHO_INDEX, H_INDEX,
    PHYSICAL_NORM_FACTOR, NORM_WEIGHT, MAXIMUM_H, MAXIMUM_H_EXACT,
    MAXIMUM_PHYSICAL_STEP, Joint168Ledger, require)
from frame_metric_true57_nonlinear168_solver import solve_joint168, vector_record

HARD_TOLERANCE = 1.e-7
SOFT_TOLERANCE = 1.e-9


def _array(value, shape=None, name="array"):
    if isinstance(value, dict):
        require("values" in value and "shape" in value and "array_sha256" in value,
                name+" payload is incomplete")
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


def _rational(value, name):
    require(isinstance(value, (Q, str, int, np.integer))
            and not isinstance(value, (bool, np.bool_)),
            name+" must be an exact rational string, Fraction or integer")
    return Q(int(value)) if isinstance(value, np.integer) else Q(value)


def _tag_key(tag):
    require(isinstance(tag, dict) and tag.get("grid") in ("coarse", "fine")
            and isinstance(tag.get("flat_row_id"), (int, np.integer))
            and not isinstance(tag.get("flat_row_id"), (bool, np.bool_)),
            "an original grid and literal integer row ID are required")
    return tag["grid"], int(tag["flat_row_id"])


def _physical172(field, state):
    values = tuple(field.full_coefficients(state, exact=True))
    require(len(values) == PHYSICAL and all(isinstance(v, Q) for v in values),
            "the original exact172 affine physical coefficients are required")
    return values


def _exact172(field, state):
    return [str(v) for v in _physical172(field, state)]


class Joint168Model:
    """Assembly from authenticated paid current168 input in a new smaller domain.

    prepared: field168, center168 (q168 may alias it), lower172, upper172,
      cfg, row_grids, source_binding, physical_map172x168,
      physical_map_exact172x168, physical_map_binding.
    oracle.model_input(): original_domain{hard_J168, hard_base_values,
      hard_targets, hard_original_row_tags, selected_metric_gradients168_of_phi,
      selected_metric_base_phi, selected_metric_original_row_tags,
      fixed_outside_phi}, complete_phi0, target, binding, binding_sha256,
      center168, source57 and optional domain_receipt.

    All original selected hard and soft rows remain present, including
    endpoints and literal zero derivatives.  There is no support-window test.
    """
    def __init__(self, prepared, oracle, *, ledger):
        require(isinstance(ledger, Joint168Ledger), "one shared new joint168 ledger required")
        self.ledger, self.oracle = ledger, oracle
        ledger.check("joint168-model.entry")
        self.field = prepared["field168"]
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.state = _array(prepared["center168"], (INDEPENDENT,), "true57 current168")
        if "q168" in prepared:
            require(np.array_equal(_array(prepared["q168"], (INDEPENDENT,)), self.state),
                    "center168 and q168 must denote the same real current point")
        self.field.validate_state(self.state)
        self.lower172 = _array(prepared["lower172"], (PHYSICAL,), "physical lower172")
        self.upper172 = _array(prepared["upper172"], (PHYSICAL,), "physical upper172")
        require(np.all(self.lower172 < self.upper172)
                and np.array_equal(self.lower172[163:], np.full(9, -.25))
                and np.array_equal(self.upper172[163:], np.full(9, .25)),
                "all original physical boxes plus the literal new9 +/-1/4 box are required")
        self.center_physical = _physical172(self.field, self.state)
        self.lower_exact = tuple(Q.from_float(float(v)) for v in self.lower172)
        self.upper_exact = tuple(Q.from_float(float(v)) for v in self.upper172)
        self.center_box = self.field.exact_full_box_decision(
            self.state, self.lower172, self.upper172)
        require(self.center_box["exact_full_box_pass"], "the exact current172 box must pass")
        self._install_physical_map(prepared)
        self.grids = prepared["row_grids"]
        require(set(self.grids) == {"coarse", "fine"}, "both original grids are required")
        self.source_binding = copy.deepcopy(prepared["source_binding"])
        require(isinstance(self.source_binding, dict)
                and self.source_binding.get("accepted_index") == 57
                and self.source_binding.get("independent168_array_sha256") == array_digest(self.state),
                "the actual true57 full168 source binding is required")
        data = oracle.model_input()
        require(isinstance(data, dict) and isinstance(data["binding"], dict)
                and digest(data["binding"]) == data["binding_sha256"],
                "one complete newly built joint168 input binding is required")
        require(data["binding_sha256"] == oracle.binding_sha256
                and np.array_equal(_array(data["center168"], (INDEPENDENT,)), self.state),
                "the new current168 derivatives must belong to this exact point")
        source = data["source57"]
        require((source == 57) if type(source) is int else
                (isinstance(source, dict) and source.get("source_accepted_index",
                 source.get("accepted_index")) == 57),
                "this joint task starts only at the actual true57 point")
        self.input_binding = copy.deepcopy(data["binding"])
        self.input_binding_sha256 = data["binding_sha256"]
        self.input_stdout_receipt = copy.deepcopy(data.get("input_record_original_stdout_receipt"))
        if "physical_linear_map172x168" in data:
            require(np.array_equal(_array(data["physical_linear_map172x168"],
                        (PHYSICAL, INDEPENDENT)), self.M),
                    "the derivative input and exact physical map disagree")
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
        self.hard_J = _array(d["hard_J168"], (nhard, INDEPENDENT), "new current hard J168")
        self.hard_base = _array(d["hard_base_values"], (nhard,), "hard base")
        self.hard_targets = _array(d["hard_targets"], (nhard,), "frozen hard targets")
        self.soft_g = _array(d["selected_metric_gradients168_of_phi"],
                             (nsoft, INDEPENDENT), "current baseline metric gradients168")
        self.soft_phi = _array(d["selected_metric_base_phi"], (nsoft,), "selected phi0")
        self.fixed_outside_phi = _scalar(d["fixed_outside_phi"], "fixed outside phi")
        require(self.fixed_outside_phi == 0.,
                "all selected rows are retained; no support-based exterior bound is substituted")
        self.rho_floor = self.target
        hard_keys, soft_keys = [], []
        for tags, keys, hard in ((self.hard_tags, hard_keys, True),
                                (self.soft_tags, soft_keys, False)):
            for tag in tags:
                key = _tag_key(tag)
                original = self.grids[key[0]].coordinate(key[1])
                require(original == tag, "the original row coordinate or branch changed")
                require((original["group"] >= 2) if hard else (original["group"] < 2),
                        "a row was placed in the wrong hard/metric group")
                keys.append(key)
        require(len(set(hard_keys)) == nhard and len(set(soft_keys)) == nsoft,
                "original selected row IDs must be unique within each domain")
        self.input_domain_receipt = copy.deepcopy(data.get("domain_receipt", {}))
        self.known = set(soft_keys)
        self.additional_rows = []
        self.extra_A, self.extra_b = [], []
        self.problems, self.finite_results = [], []
        self.last_result, self.last_candidate, self.last_handle = None, None, None
        self.last_finite_x = np.r_[np.zeros(INDEPENDENT), self.phi0, 0.]
        self._build_initial_matrix()
        self.binding = {
            "schema": POLICY+"-original-current168-model",
            "source_binding": self.source_binding,
            "new_input_binding_sha256": self.input_binding_sha256,
            "current168_sha256": array_digest(self.state),
            "physical172_exact_sha256": digest([str(v) for v in self.center_physical]),
            "physical_map_binding": copy.deepcopy(self.map_binding),
            "lower172_sha256": array_digest(self.lower172),
            "upper172_sha256": array_digest(self.upper172),
            "configuration_sha256": digest(self.cfg),
            "field_coordinate_definition_sha256": self.field.coordinate_definition_sha256,
            "field_evaluation_definition_sha256": digest(self.field.evaluation_definition()),
            "hard_original_row_tags_sha256": digest(self.hard_tags),
            "hard_original_row_count": nhard,
            "hard_J168_sha256": array_digest(self.hard_J),
            "hard_base_sha256": array_digest(self.hard_base),
            "hard_targets_sha256": array_digest(self.hard_targets),
            "initial_metric_original_row_tags_sha256": digest(self.soft_tags),
            "initial_metric_row_count": nsoft,
            "initial_metric_g168_sha256": array_digest(self.soft_g),
            "initial_metric_phi0_sha256": array_digest(self.soft_phi),
            "fixed_outside_phi": 0., "rho_floor": self.rho_floor,
            "complete_phi0": self.phi0, "norm_weight": NORM_WEIGHT,
            "physical_norm_factor": PHYSICAL_NORM_FACTOR,
            "maximum_h_exact": MAXIMUM_H_EXACT,
            "maximum_physical_step": MAXIMUM_PHYSICAL_STEP,
            "variable_order": "delta168,rho,h", "objective": "rho+1e-6*h",
            "all168_coordinates_free": True,
            "old159_defect_learning_or_normalization_transferred": False,
            "all_original_selected_rows_retained_including_endpoints": True,
            "initial_A_sha256": array_digest(self.initial_A),
            "initial_b_sha256": array_digest(self.initial_b),
            "initial_tolerances_sha256": array_digest(self.initial_tol)}
        self.binding_sha256 = digest(self.binding)
        ledger.check("joint168-model.complete")

    def _install_physical_map(self, prepared):
        raw = prepared["physical_map_exact172x168"]
        require(isinstance(raw, (list, tuple)) and len(raw) == PHYSICAL,
                "the complete exact172x168 physical map is required")
        exact = []
        for row in raw:
            require(isinstance(row, (list, tuple)) and len(row) == INDEPENDENT,
                    "each exact physical map row must have 168 entries")
            exact.append(tuple(_rational(v, "physical map entry") for v in row))
        exact = tuple(exact)
        H = self.field.original_field.coordinates.basis.H
        require(len(H) == 9 and all(len(row) == 5 for row in H),
                "the original nine-by-five null-height basis is required")
        for i in range(PHYSICAL):
            for j in range(INDEPENDENT):
                expected = (Q(int(i == j)) if i < 154
                            else (Q(H[i-154][j-154]) if 154 <= i < 163 and 154 <= j < 159
                                  else (Q(int(i-4 == j)) if i >= 163 else Q(0))))
                require(exact[i][j] == expected,
                        "physical map must be precisely original154, original H9x5, new9")
        rounded = np.asarray([[float(v) for v in row] for row in exact], dtype=float)
        given = _array(prepared["physical_map172x168"], (PHYSICAL, INDEPENDENT),
                       "rounded physical map172x168")
        require(np.array_equal(given, rounded), "rounded M must come from the exact original map")
        provenance = copy.deepcopy(prepared["physical_map_binding"])
        require(isinstance(provenance, dict) and bool(provenance),
                "the original coordinate-map provenance is required")
        self.M, self.M_exact = given, exact
        self.map_nonzero = tuple(tuple((j, v) for j, v in enumerate(row) if v)
                                 for row in exact)
        self.map_binding = {
            "source": provenance, "shape": [PHYSICAL, INDEPENDENT],
            "exact_rational_rows_sha256": digest([[str(v) for v in row] for row in exact]),
            "float_array_sha256": array_digest(given),
            "block_structure": "I154;original-H9x5;I9",
            "checked_against_original_FiveHeightCoordinates_basis_H": True}
        self.center_physical_float = np.asarray([float(v) for v in self.center_physical])

    def _mapped_exact(self, delta):
        dq = tuple(Q.from_float(float(v)) for v in delta)
        return tuple(sum((v*dq[j] for j, v in row), Q(0)) for row in self.map_nonzero)

    def _build_initial_matrix(self):
        blocks, rhs, kinds, origins = [], [], [], []
        def append(A, b, kind, origin):
            A, b = np.asarray(A, float), np.asarray(b, float)
            require(A.ndim == 2 and A.shape[1] == VARIABLES and b.shape == (len(A),)
                    and np.all(np.isfinite(A)) and np.all(np.isfinite(b)),
                    "one finite 170-variable original row block is required")
            start = sum(len(v) for v in rhs)
            blocks.append(A); rhs.append(b); kinds.extend([kind]*len(A))
            origins.append({"start": start, "count": len(A), "kind": kind, "origin": origin})
        append(np.column_stack((-self.hard_J, np.zeros((len(self.hard_J), 2)))),
               self.hard_base-self.hard_targets, "hard", "all original selected current hard J168")
        append(np.column_stack((self.soft_g, -np.ones(len(self.soft_g)), np.zeros(len(self.soft_g)))),
               -self.soft_phi, "metric", "all selected baseline current metric gradients168")
        bounds = np.zeros((2*PHYSICAL, VARIABLES))
        bounds[0::2, :INDEPENDENT], bounds[1::2, :INDEPENDENT] = self.M, -self.M
        margins = np.empty(2*PHYSICAL)
        margins[0::2] = [float(hi-v) for hi, v in zip(self.upper_exact, self.center_physical)]
        margins[1::2] = [float(v-lo) for v, lo in zip(self.center_physical, self.lower_exact)]
        append(bounds, margins, "bound", "all original exact172 boxes in the current physical map")
        norm = bounds.copy()
        norm[:, :INDEPENDENT] *= PHYSICAL_NORM_FACTOR
        norm[:, H_INDEX] = -1.
        append(norm, np.zeros(2*PHYSICAL), "norm", "all172 signed rows: 4*M*delta-h<=0")
        h_bounds = np.zeros((2, VARIABLES))
        h_bounds[0, H_INDEX], h_bounds[1, H_INDEX] = -1., 1.
        append(h_bounds, np.array([0., MAXIMUM_H]), "bound", "literal 0<=h<=1/128")
        rho = np.zeros((1, VARIABLES)); rho[0, RHO_INDEX] = -1.
        append(rho, np.array([-self.rho_floor]), "metric", "the unchanged constant target .26")
        self.initial_A, self.initial_b = np.vstack(blocks), np.concatenate(rhs)
        self.initial_kind, self.origins = kinds, origins
        self.initial_tol = np.array([SOFT_TOLERANCE if k == "metric" else HARD_TOLERANCE
                                     for k in kinds])
        self.initial_A.setflags(write=False); self.initial_b.setflags(write=False)
        self.initial_tol.setflags(write=False)

    def add(self, gradient, *, source):
        self.ledger.check("joint168-model.add")
        tag = copy.deepcopy(gradient["original_row"])
        key = _tag_key(tag)
        require(key == (gradient["grid"], int(gradient["flat_row_id"]))
                and self.grids[key[0]].coordinate(key[1]) == tag and tag["group"] < 2,
                "one exact original metric row is required")
        if key in self.known:
            return False
        g = _array(gradient["gradient"], (INDEPENDENT,), "new baseline metric gradient168")
        require(array_digest(g) == gradient["gradient_sha256"],
                "the new materialized baseline gradient hash changed")
        require(gradient["binding_sha256"] == self.input_binding_sha256,
                "a gradient from another current point or family cannot enter this master")
        base = _scalar(gradient["base_phi"], "new row baseline phi")
        rec = {
            "grid": key[0], "flat_row_id": key[1], "original_row": tag,
            "gradient168": g.tolist(), "gradient_sha256": array_digest(g),
            "base_phi": base, "source": copy.deepcopy(source),
            "input_binding_sha256": self.input_binding_sha256,
            "linearization_point": "the same true57 nonzero-new9 complete current field",
            "not_a_tangent_at_the_trial_direction": True}
        self.extra_A.append(np.r_[g, -1., 0.])
        self.extra_b.append(-base)
        self.additional_rows.append(rec)
        self.known.add(key)
        return True

    def assemble(self):
        self.ledger.check("joint168-model.assemble")
        A = (np.vstack((self.initial_A, np.asarray(self.extra_A)))
             if self.extra_A else self.initial_A.copy())
        b = np.r_[self.initial_b, np.asarray(self.extra_b)]
        tol = np.r_[self.initial_tol, np.full(len(self.extra_b), SOFT_TOLERANCE)]
        kinds = self.initial_kind+["metric"]*len(self.extra_b)
        binding = {
            "source_model_binding_sha256": self.binding_sha256,
            "additional_original_rows": [
                {k: copy.deepcopy(v) for k, v in row.items() if k != "gradient168"}
                for row in self.additional_rows],
            "A_sha256": array_digest(A), "b_sha256": array_digest(b),
            "row_tolerance_sha256": array_digest(tol),
            "row_kind_sha256": digest(kinds),
            "row_count": len(b), "columns": VARIABLES,
            "objective": "rho+1e-6*h", "variable_order": "delta168,rho,h",
            "physical_map_binding_sha256": digest(self.map_binding),
            "norm": "h>=4*infinity_norm(M172x168*delta168);0<=h<=1/128"}
        return {"A": A, "b": b, "row_tol": tol, "row_kind": kinds,
                "initial_x": self.last_finite_x.copy(),
                "binding": binding, "binding_sha256": digest(binding)}

    def residual(self, delta168):
        """Original linear hard rows and the new exact coordinate-map norm.

        This diagnostic does not replace a rounded candidate's exact physical
        coefficients.  validate_actual_candidate separately checks those.
        """
        self.ledger.check("joint168-model.domain-residual")
        delta = _array(delta168, (INDEPENDENT,), "actual independent displacement168")
        hard = self.hard_targets-(self.hard_base+self.hard_J@delta)
        mapped = self._mapped_exact(delta)
        exact_norm = Q(4)*max((abs(v) for v in mapped), default=Q(0))
        float_norm = PHYSICAL_NORM_FACTOR*float(np.max(np.abs(self.M@delta), initial=0.))
        require(math.isfinite(float_norm) and math.isfinite(float(exact_norm)),
                "the physical step norm must remain finite")
        return {
            "hard_maximum_signed_residual": float(np.max(hard, initial=-np.inf)),
            "hard_maximum_positive_tolerance_excess":
                float(np.max(hard-HARD_TOLERANCE, initial=0.)),
            "all_selected_hard_targets_pass": bool(np.all(hard <= HARD_TOLERANCE)),
            "hard_row_count": len(hard), "hard_tolerance": HARD_TOLERANCE,
            "mapped_binary64_direction_physical_norm_exact": str(exact_norm),
            "mapped_binary64_direction_physical_norm": float(exact_norm),
            "float_matrix_physical_norm_diagnostic": float_norm,
            "literal_mapped_direction_norm_pass": bool(exact_norm <= Q(MAXIMUM_H_EXACT)),
            "physical_map_binding_sha256": digest(self.map_binding),
            "no_old163_norm_or_learned159_gamma_used": True}

    def validate_actual_candidate(self, candidate168):
        self.ledger.check("joint168-model.actual-candidate")
        q = _array(candidate168, (INDEPENDENT,), "actual candidate168")
        self.field.validate_state(q)
        delta = q-self.state
        rows = self.residual(delta)
        physical = _physical172(self.field, q)
        physical_delta = tuple(v-u for v, u in zip(physical, self.center_physical))
        exact_norm = Q(4)*max((abs(v) for v in physical_delta), default=Q(0))
        box = self.field.exact_full_box_decision(q, self.lower172, self.upper172)
        physical_pass = bool(exact_norm <= Q(MAXIMUM_H_EXACT))
        eligible = bool(rows["all_selected_hard_targets_pass"]
                        and rows["literal_mapped_direction_norm_pass"]
                        and physical_pass and box["exact_full_box_pass"])
        rows.update({
            "actual_exact172_step_norm_exact": str(exact_norm),
            "actual_exact172_step_norm": float(exact_norm),
            "literal_actual_physical_step_pass": physical_pass,
            "actual_exact172_norm_compares_with_one_over128_without_new_tolerance": True})
        return {
            "eligible": eligible, "model_binding_sha256": self.binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "all168_independent_coordinates_are_free": True,
            "actual_delta168": vector_record(delta),
            "actual_candidate168": vector_record(q),
            "actual_physical_exact172": [str(v) for v in physical],
            "actual_physical_step_exact172": [str(v) for v in physical_delta],
            "exact172_box": copy.deepcopy(box), "joint_physical_domain": rows,
            "rounded_independent_subtraction_and_exact_field_step_both_checked": True,
            "no_geometry_or_derivative_call_in_this_check": True,
            "linear_hard_prediction_is_not_the_actual_fourteen_gate_decision": True}

    def finite_candidate(self, raw_x, *, assembled=None):
        if raw_x is None:
            return None
        x = _array(raw_x, (VARIABLES,), "real last finite170")
        d = self.assemble() if assembled is None else assembled
        q = self.state+x[:INDEPENDENT]
        actual = q-self.state
        require(np.all(np.isfinite(q)) and np.all(np.isfinite(actual)),
                "the same-add candidate and its real displacement must be finite")
        domain = self.validate_actual_candidate(q)
        norm = domain["joint_physical_domain"]
        h = max(norm["mapped_binary64_direction_physical_norm"],
                norm["actual_exact172_step_norm"],
                norm["float_matrix_physical_norm_diagnostic"])
        soft_value = self.soft_phi+self.soft_g@actual
        rho = max(self.rho_floor, float(np.max(soft_value, initial=-np.inf)))
        for row in self.additional_rows:
            rho = max(rho, row["base_phi"]+float(np.asarray(row["gradient168"])@actual))
        require(math.isfinite(rho) and math.isfinite(h), "finite repaired rho and h required")
        repaired = np.r_[actual, rho, h]
        residual = d["A"]@repaired-d["b"]
        metric = np.asarray(d["row_kind"], dtype=object) == "metric"
        hard_ok = bool(np.all(residual[~metric] <= d["row_tol"][~metric]))
        soft_ok = bool(np.all(residual[metric] <= d["row_tol"][metric]))
        gain = self.phi0-rho-NORM_WEIGHT*h
        return {
            "schema": POLICY+"-finite-only-candidate",
            "original_last_finite170": vector_record(x),
            "repaired_finite170": vector_record(repaired),
            "raw_direction168": vector_record(x[:INDEPENDENT]),
            "delta168": vector_record(actual),
            "unit_candidate168": vector_record(q),
            "unit_physical_exact172": _exact172(self.field, q),
            "raw_rho": float(x[RHO_INDEX]), "raw_h": float(x[H_INDEX]),
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
            "same_add_rounding_is_recorded_and_repaired_rows_use_actual_delta": True,
            "rho_and_h_repair_does_not_change_the_actual_candidate": True,
            "full_grid_separation_and_true_actual_gates_still_required": True,
            "actual_geometry_evaluated": False}

    def solve(self, *, emit):
        d = self.assemble()
        result = solve_joint168(
            d["A"], d["b"], d["row_tol"], d["row_kind"], d["initial_x"],
            ledger=self.ledger, problem_binding=d["binding_sha256"],
            added_row_count=len(self.additional_rows))
        # Save every actual raw170/dual/slack before any candidate filter or
        # external output.  Failed output is exposed by full_record().
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
            "raw_returned_finite170": copy.deepcopy(result.get("last_finite_x_record"))}
        self.problems.append(summary)
        if result.get("last_finite_x") is not None:
            self.last_finite_x = _array(
                result["last_finite_x"], (VARIABLES,), "returned finite170").copy()
        try:
            candidate = self.finite_candidate(result.get("last_finite_x"), assembled=d)
        except Exception as error:
            result["candidate_diagnostic_error"] = {
                "type": type(error).__name__, "message": str(error)}
            summary["candidate_diagnostic_error"] = copy.deepcopy(
                result["candidate_diagnostic_error"])
            summary["original_result_receipt"] = copy.deepcopy(emit("FINITE_RESULT", result))
            raise
        self.last_candidate = candidate
        result["candidate"] = candidate
        summary["original_result_receipt"] = copy.deepcopy(emit("FINITE_RESULT", result))
        summary["finite_candidate"] = copy.deepcopy(candidate)
        self.ledger.check("joint168-model.solve.after-output")
        return result, candidate, summary

    def rounded_direction(self, candidate):
        require(isinstance(candidate, dict) and "delta168" in candidate,
                "the actual newly returned finite candidate is required")
        ideal = _array(candidate["delta168"]["binary64"], (INDEPENDENT,),
                       "new finite direction168")
        require(array_digest(ideal) == candidate["delta168"]["array_sha256"],
                "new finite direction identity changed")
        q = self.state+ideal
        delta = q-self.state
        return {"candidate": q, "direction": delta, "ideal_direction": ideal,
                "preliminary_original_domain": self.validate_actual_candidate(q),
                "rounding_changed": not np.array_equal(delta, ideal)}

    def finish_direction(self, rounded, scan):
        delta = _array(rounded["direction"], (INDEPENDENT,), "completed scan direction168")
        require(scan["binding_sha256"] == self.input_binding_sha256
                and np.array_equal(_array(scan["direction"], (INDEPENDENT,)), delta),
                "the complete two-grid scan must use this same rounded baseline direction")
        maximum = _scalar(scan["linear_maximum"], "complete first-order maximum")
        require(maximum >= self.target, "the constant target branch cannot be dropped")
        domain = rounded["preliminary_original_domain"]
        norms = domain["joint_physical_domain"]
        h = max(norms["mapped_binary64_direction_physical_norm"],
                norms["actual_exact172_step_norm"],
                norms["float_matrix_physical_norm_diagnostic"])
        gain = self.phi0-maximum-NORM_WEIGHT*h
        mapped = self._mapped_exact(delta)
        physical = [(float(hi-v), -float(md), 0.)
                    for hi, v, md in zip(self.upper_exact, self.center_physical, mapped)]
        physical.extend((float(v-lo), float(md), 0.)
                        for v, lo, md in zip(self.center_physical, self.lower_exact, mapped))
        # The same physical step budget also belongs to the legal line domain.
        physical.extend((MAXIMUM_PHYSICAL_STEP, -float(md), 0.) for md in mapped)
        physical.extend((MAXIMUM_PHYSICAL_STEP, float(md), 0.) for md in mapped)
        interval = guard_compatible_interval(
            self.hard_base, self.hard_J@delta, self.hard_targets,
            residual_tolerance=HARD_TOLERANCE, physical_bounds=physical)
        interval.update({
            "physical_map_binding_sha256": digest(self.map_binding),
            "all172_physical_boxes_and_step_bounds_included": True,
            "interval_uses_float_proposals_from_exact_rational_map": True,
            "every_rounded_actual_candidate_requires_exact172_box_and_norm_again": True})
        numeric_interval = interval["original_numeric_tolerance_interval"]
        qualified = bool(domain["eligible"] and gain > self.floor
                         and numeric_interval["nonempty"])
        report = {
            "schema": POLICY+"-complete-first-order-direction",
            "model_binding_sha256": self.binding_sha256,
            "input_binding_sha256": self.input_binding_sha256,
            "direction168": vector_record(delta),
            "unit_candidate168": vector_record(rounded["candidate"]),
            "unit_physical_exact172": _exact172(self.field, rounded["candidate"]),
            "original_joint_physical_domain": copy.deepcopy(domain),
            "complete_baseline_phi0": self.phi0,
            "complete_first_order_maximum": maximum,
            "new_physical_norm_h": h, "new_norm_cost": NORM_WEIGHT*h,
            "complete_repaired_gain": gain, "minimum_gain": self.floor,
            "complete_coverage": copy.deepcopy(scan["coverage"]),
            "complete_branch_attainers": copy.deepcopy(scan["branches"]),
            "guard_compatible_alpha_interval": copy.deepcopy(interval),
            "qualified_first_order_direction": qualified,
            "actual_unit_candidate_evaluated": False,
            "full_first_order_model_is_not_affine_observable_nonlinear_phi": True,
            "nonlinear_metric_curvature_prediction_and_actual_gates_still_required": True}
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
            "input_record_original_stdout_receipt": copy.deepcopy(self.input_stdout_receipt),
            "initial_row_groups": copy.deepcopy(self.origins),
            "initial_rows": len(self.initial_b), "variable_count": VARIABLES,
            "additional_original_row_metadata": [
                {k: copy.deepcopy(v) for k, v in row.items() if k != "gradient168"}
                for row in self.additional_rows],
            "problems": copy.deepcopy(self.problems),
            "last_raw_finite170": (copy.deepcopy(self.last_result.get("last_finite_x_record"))
                                   if self.last_result else None),
            "last_finite_candidate": copy.deepcopy(self.last_candidate),
            "last_complete_direction": (copy.deepcopy(self.last_handle["report"])
                                        if self.last_handle is not None else None),
            "all168_free_at_the_actual_nonzero_new9_true57_point": True,
            "new_method_normalization": "h=4*||M172x168*delta168||infinity;0<=h<=1/128",
            "rho_means_actual_smoothed_metric_upper_bound_not_excess": True,
            "old159_defect_gamma_and_normalized163_norm_not_migrated": True,
            "geometric_acceptance_is_never_inferred_from_a_finite_stop": True}

    def full_record(self):
        """One model record; geometry already owns the unique complete input.

        Do not duplicate hard J168, selected gradients168, M, or the derived
        sparse/zero-padded A.  Their binding and source input receipt identify
        the one actual original-stdout input.  Every successful FINITE_RESULT
        already contains its actual raw170/dual/slack and residuals; only an
        output that did not return its receipt is repeated here.
        """
        receipts, unprinted = [], []
        for result, problem in zip(self.finite_results, self.problems):
            receipt = problem.get("original_result_receipt")
            if receipt is None:
                unprinted.append(copy.deepcopy(result))
            else:
                receipts.append({
                    "new_finite_problem_number": problem["number"],
                    "problem_binding_sha256": problem["problem_binding_sha256"],
                    "original_record_receipt": copy.deepcopy(receipt),
                    "last_finite_x_record": copy.deepcopy(result.get("last_finite_x_record"))})
        finite_sources = [r for r in self.finite_results if r.get("last_finite_x") is not None]
        saved = all(isinstance(r.get("last_finite_x_record"), dict)
                    and r["last_finite_x_record"].get("length") == VARIABLES
                    and len(r["last_finite_x_record"].get("binary64", [])) == VARIABLES
                    for r in finite_sources)
        return {
            **self.report(),
            "center168": vector_record(self.state),
            "center_physical_exact172": [str(v) for v in self.center_physical],
            "unique_complete_input_reference": {
                "input_binding_sha256": self.input_binding_sha256,
                "source_binding": copy.deepcopy(self.source_binding),
                "original_stdout_receipt": copy.deepcopy(self.input_stdout_receipt),
                "hard_J168_shape": list(self.hard_J.shape),
                "hard_J168_sha256": array_digest(self.hard_J),
                "selected_metric_g168_shape": list(self.soft_g.shape),
                "selected_metric_g168_sha256": array_digest(self.soft_g),
                "physical_map_binding": copy.deepcopy(self.map_binding)},
            "new_original_metric_rows_with_paid_gradients168": copy.deepcopy(self.additional_rows),
            "finite_result_original_stdout_receipts": receipts,
            "unemitted_real_finite_results_including_raw170_dual_slack_residual": unprinted,
            "already_emitted_finite_numeric_arrays_not_duplicated": True,
            "full168_initial_input_not_duplicated_in_model_record": True,
            "actual_finite170_vector_sources": len(finite_sources),
            "all_actual_finite170_vector_records_present": saved,
            "complete_directional_arrays_have_their_separate_single_cache_record": True}


def compact_scan(scan):
    """Copy original values only; two-grid directional arrays have one cache."""
    return {key: copy.deepcopy(scan[key]) for key in (
        "schema", "binding_sha256", "linear_maximum", "branches", "coverage",
        "direction_sha256", "scope", "ordinal", "elapsed_seconds")
        if key in scan}


def exchange_joint168(model, oracle, ledger, *, emit, progress):
    require(isinstance(model, Joint168Model) and model.oracle is oracle
            and model.ledger is ledger and isinstance(progress, dict) and not progress,
            "one new current168 model, oracle owner and empty progress sink are required")
    progress.update(schema=POLICY+"-complete-first-order-row-exchange",
                    status="started", rounds=[], new_gradient_records=[],
                    source_accepted_index=57)
    handle = last_scan = None
    for number in range(1, LIMITS["finite_master_calls"]+1):
        ledger.check("joint168-exchange.before-master")
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
            item["status"] = "joint168-rounded-domain-rejected"
            progress["status"] = item["status"]
            break
        last_scan = oracle.scan(rounded["direction"], phase="finite-problem-"+str(number))
        handle = model.finish_direction(rounded, last_scan)
        record = compact_scan(last_scan)
        record.update(new_finite_problem_number=number,
                      actual_direction168=vector_record(rounded["direction"]),
                      qualification=copy.deepcopy(handle["report"]))
        item["full_grid_scan_receipt"] = emit("FULL_GRID_SCAN", record)
        item["qualification"] = copy.deepcopy(handle["report"])
        if handle["qualified"]:
            item["status"] = "complete-first-order-joint168-direction-qualified"
            progress["status"] = item["status"]
            progress["selected_round"] = number
            break
        # Add only genuinely absent ORIGINAL baseline tags.  A different
        # tangent at the same tag never creates permission to resolve.
        added, seen = [], set()
        for attainer in last_scan["branches"]:
            key = _tag_key(attainer)
            if key in seen or key in model.known:
                continue
            seen.add(key)
            original = model.grids[key[0]].coordinate(key[1])
            require(original["group"] < 2, "the full metric attainer must have its original branch")
            row = oracle.attainer_gradient(key[0], key[1], scan=last_scan)
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
        progress["status"] = "declared-eight-new-row-set-scope-completed"
    progress["final_complete_direction_qualified"] = bool(handle is not None and handle["qualified"])
    progress["inexact_or_unqualified_stop_is_not_an_infeasibility_or_stationarity_proof"] = True
    progress["full_first_order_separation_distinct_from_actual_coordinate_nonlinear_prediction"] = True
    return handle, last_scan
