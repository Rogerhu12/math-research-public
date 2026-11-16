#!/usr/bin/env python3
"""Minimal new first jets for one positive true53 physical direction.

Import-only.  The caller owns the original-log input, request/source binding,
one cumulative ledger, cache persistence, stdout and every public execution.
This module never calls an ordinary geometry evaluator, an old selected-J
entry, a solver, a developer check, or a coordinate-axis full-grid Jacobian.

The missing U=X_s and T inputs are restored once from their original formulas.
The paid MODEL supplies e/f, both original spectral branches and the target.
At most two distinct physical159 directions and four genuinely new original
attainer rows may be consumed; all completed arrays remain reusable.
"""
from __future__ import annotations

import copy
from fractions import Fraction
import time

import numpy as np

from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
from frame_complete_affine_metric_oracle import direction_frame_jets
from frame_selected_row_radial_jacobian import (
    SelectedRadialJacobian, angular_kernels, virtual_selected_jets,
    expand_radial_rows, target_frame, periodic_operator)
from frame_metric_affine_spectral_model import phi, phi_gradient


POLICY = "same159-true53-positive-direction-first-jets-v1"
N = 159
LABELS = ("coarse", "fine")
SHAPES = {"coarse": (160, 384), "fine": (160, 768)}
MAX_DISTINCT_DIRECTIONS = 2
MAX_NEW_ORIGINAL_ROWS = 4


def require(test, message):
    if not bool(test):
        raise ValueError(message)


def finite(value, shape=None, name="array"):
    a = np.asarray(value, dtype=np.float64)
    require((shape is None or a.shape == shape) and np.all(np.isfinite(a)),
            "finite original-shape " + name + " required")
    return a


def owned(value):
    a = np.array(value, dtype=np.float64, copy=True)
    a.flags.writeable = False
    return a


def readonly(value):
    a = np.asarray(value, dtype=np.float64)
    a.flags.writeable = False
    return a


def paid_array(record, shape, name):
    """Decode the existing _array_payload contract, using its original hash."""
    require(isinstance(record, dict) and record.get("dtype") == "float64"
            and isinstance(record.get("values"), list),
            "one paid float64 payload required: " + name)
    a = finite(record["values"], shape, name)
    require(record.get("shape") == list(shape)
            and array_digest(a) == record.get("array_sha256"),
            "paid numeric payload fingerprint changed: " + name)
    return readonly(a)


def _array_record(a):
    a = np.asarray(a)
    return {"shape": list(a.shape), "dtype": str(a.dtype),
            "array_sha256": array_digest(a), "bytes": int(a.nbytes)}


def _tree_arrays(value, prefix, out):
    """Expose useful numerical cache objects; never write or print them."""
    if isinstance(value, np.ndarray):
        out[prefix] = value
    elif isinstance(value, dict):
        for key in sorted(value):
            _tree_arrays(value[key], prefix + "/" + str(key), out)


def _radial_slice(value, row, nr):
    """Slice already restored scalar/frame inputs, with no field evaluation."""
    if isinstance(value, dict):
        return {key: _radial_slice(item, row, nr) for key, item in value.items()}
    if isinstance(value, np.ndarray) and value.ndim and value.shape[0] == nr:
        return value[row:row+1]
    return value


class _OriginalFamilies:
    """Only the original pure radial/angular family contract, not old evaluate."""
    def __init__(self):
        self.cache = {}

    def _families(self, grid, nr, nt):
        key = (id(grid), int(nr), int(nt))
        if key not in self.cache:
            self.cache[key] = SelectedRadialJacobian._families(self, grid, nr, nt)
        return self.cache[key]


class PositiveDirectionFirstJets:
    """One frozen true53 center, two original grids, at most two new JVPs.

    Required ledger protocol:
      check()
      begin(kind, **metadata) -> mutable dict
      end(event, error=None, **metadata)
    Event kinds are first_jet_input_restores, pair_first_jet_jvps and
    new_attainer_gradients.  The ledger must already have started before the
    caller reads/restores any input; it is the sole execution budget.

    The default fine_theta is the original MixedGridStepObjective expression,
    arange(2*Ncoarse)*pi/Ncoarse, retaining its floating operation order.
    The original_complete_value_binding SHA is checked exactly; an
    approximately uniform replacement is never accepted.

    capture is an optional fresh dict.  It retains failure diagnostics and
    references to completed finite arrays even if construction raises.
    """
    def __init__(self, prepared, paid_model, ledger, *, fine_theta=None, capture=None):
        self.ledger = ledger
        require(all(callable(getattr(ledger, name, None))
                    for name in ("check", "begin", "end")),
                "one already-started shared ledger is required")
        ledger.check()
        self.capture = {} if capture is None else capture
        require(isinstance(self.capture, dict) and not self.capture,
                "fresh capture dict required")
        self.events = []
        self.base = {}
        self.scans = {}
        self.direction_attempts = {}
        self.gradient_attempts = {}
        self.gradients = {}
        self.point_gradients = {}
        self._ready = False
        self.families = _OriginalFamilies()
        self.capture.update(
            schema=POLICY+"-capture", status="initializing",
            events=self.events, _completed_arrays={})
        self.statistics = {
            "input_restores_started": 0, "input_restores_completed": 0,
            "restored_grid_count": 0,
            "pair_first_jet_started": 0, "pair_first_jet_completed": 0,
            "direction_cache_hits": 0, "completed_grid_JVPs": 0,
            "new_original_rows_started": 0, "new_original_rows_completed": 0,
            "new_point_gradient_contractions": 0, "point_gradient_reuses": 0,
            "ordinary_geometry_calls": 0,
            "old_selected_J_evaluate_calls": 0,
            "old_first_jet_replays": 0,
            "full_grid_parameter_axis159_tensors": 0,
            "ordinary_position_or_two_jet_assemblies": 0,
            "height_primitive_calls": 0,
            "maximum_input_e_f_error": 0.0,
            "maximum_gradient_dot_JVP_error": 0.0,
        }
        self.capture["statistics"] = self.statistics
        self.capture["direction_attempts"] = self.direction_attempts
        self.capture["gradient_attempts"] = self.gradient_attempts
        event = self._begin("first_jet_input_restores",
                            source_model_binding_sha256=paid_model.get("binding_sha256"))
        self.statistics["input_restores_started"] += 1
        try:
            self._initialize(prepared, paid_model, fine_theta, event)
            self._ready = True
            self.statistics["input_restores_completed"] += 1
            self.capture.update(status="ready", binding=copy.deepcopy(self.binding),
                                binding_sha256=self.binding_sha256)
            self._end(event, restored_grids=list(self.base),
                      restored_input_cache_manifest=self.cache_manifest(),
                      no_ordinary_geometry_or_old_J_calls=True)
        except Exception as error:
            self.capture["status"] = "input-restore-failed"
            self.capture["error"] = self._error(error)
            self._end(event, error, completed_grids=list(self.base))
            raise

    @staticmethod
    def _error(error):
        return {"type": type(error).__name__, "message": str(error)}

    def _begin(self, kind, **metadata):
        self.ledger.check()
        event = self.ledger.begin(kind, **metadata)
        require(isinstance(event, dict), "ledger.begin must return a mutable dict")
        event.setdefault("module_policy", POLICY)
        self.events.append(event)
        return event

    def _end(self, event, error=None, **metadata):
        # Check before successful closure: an expired budget is then recorded
        # by the surrounding except exactly once, with the full finite state.
        if error is None:
            self.ledger.check()
        self.ledger.end(event, error, **metadata)

    def _initialize(self, prepared, model, fine_theta, event):
        require(isinstance(model, dict) and isinstance(model.get("binding"), dict)
                and digest(model["binding"]) == model.get("binding_sha256"),
                "the original complete paid MODEL binding is required")
        self.model_binding = copy.deepcopy(model["binding"])
        self.model_binding_sha256 = model["binding_sha256"]
        self.field = prepared["problem"]
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.cfg_sha256 = digest(self.cfg)
        self.grids = dict(prepared["row_grids"])
        require(set(self.grids) == set(LABELS), "both original rational grids required")
        self.state = owned(self.field.coordinates.validate(prepared["initial159"]))
        paid_state = paid_array(model["source_current_independent159"], (N,), "source159")
        require(np.array_equal(self.state, paid_state)
                and array_digest(self.state) == self.model_binding["state_sha256"],
                "prepared center differs from the paid true53 center")
        require(self.cfg_sha256 == self.model_binding["configuration_sha256"]
                and self.field.coordinate_definition_sha256
                == self.model_binding["coordinate_definition_sha256"]
                and digest(self.field.evaluation_definition())
                == self.model_binding["ordinary_field_evaluation_sha256"]
                and digest(self.field.identity(self.state))
                == self.model_binding["physical_state_sha256"],
                "the original field/configuration/physical center changed")
        self.field._assert_shared_context()
        self.reference163 = owned(
            self.field.coordinates.reference_evaluation_state(self.state))
        require(array_digest(self.reference163) == self.model_binding["reference163_sha256"],
                "the original exact-height reference163 changed")
        self.epsilon = float(Fraction(self.cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Fraction(self.cfg["fixed_metric_budget_exact"]))
        self.mu = float(model["physical_norm_cost_mu"])
        require(self.epsilon == float(model["epsilon"]) == 1e-8
                and self.target == float(model["constant_target"]) == .26
                and np.isfinite(self.mu) and self.mu > 0,
                "the original two branches/target/norm coefficient changed")
        self.replay_relative_tolerance = float(
            self.cfg["value_Jacobian_replay_relative_tolerance"])
        require(np.isfinite(self.replay_relative_tolerance)
                and self.replay_relative_tolerance > 0,
                "the original input/derivative comparison tolerance is required")
        radial = owned(finite(prepared["radial"], (160,), "original radial grid"))
        coarse_theta = owned(finite(prepared["theta"], (384,), "original coarse theta"))
        if fine_theta is None:
            # frame_curvature_mixed_grid_steps.MixedGridStepObjective.__init__
            # Do not reassociate as arange(Nfine)*(2*pi/Nfine) or use linspace.
            fine_theta = np.arange(2*len(coarse_theta))*np.pi/len(coarse_theta)
        theta = {
            "coarse": coarse_theta,
            "fine": owned(finite(fine_theta, (768,), "original fine theta")),
        }
        grid_binding = {}
        for label in LABELS:
            grid = self.grids[label]
            nr, nt = SHAPES[label]
            require(grid.label == label and grid.nr == nr and grid.nt == nt
                    and grid.point_count == nr*nt
                    and np.array_equal(radial, np.array([float(v) for v in grid.nodes]))
                    and grid.definition == self.model_binding["original_grid_definitions"][label],
                    "the original rational grid identity changed: "+label)
            grid_binding[label] = {
                "grid": grid.definition_sha256,
                "radial": array_digest(radial), "theta": array_digest(theta[label])}
        original_value_binding = {
            "field": self.model_binding["ordinary_field_evaluation_sha256"],
            "factorization": self.model_binding["original_factorization_definition_sha256"],
            "state": array_digest(self.state), "grids": grid_binding}
        require(digest(original_value_binding)
                == self.model_binding["original_complete_value_binding_sha256"],
                "exact original theta/radial/field binding mismatch")
        self._grid_binding = copy.deepcopy(grid_binding)
        self.paid_rows = set()
        for label in LABELS:
            count = self.grids[label].point_count
            for raw in model["ordered_original_pool_ids"][label]:
                require(type(raw) is int and 0 <= raw < 11*count,
                        "original pool IDs must be literal original rows")
                if raw < 2*count:
                    self.paid_rows.add((label, raw))
        for row in model["installed_metric_rows"]:
            label, raw = row["grid"], row["flat_row_id"]
            require(label in LABELS and type(raw) is int
                    and 0 <= raw < 2*self.grids[label].point_count,
                    "original installed metric row identity changed")
            self.paid_rows.add((label, raw))
        self.single = self.field._direct_single
        bounded = self.field._direct_bounded
        require(self.single is self.field.original_problem
                and bounded is self.single.base,
                "the original direct reference chain is required")
        self.ledger.check()
        common_tick = time.monotonic()
        old = self.single.to_old(self.reference163)
        # Exactly the necessary two original operations.  In particular, no
        # _reference_data (which would restore center primitives) is called.
        metric_raw = bounded.metric(old, radial, jacobian=False)
        self.ledger.check()
        height_raw = bounded.height_jets(old, radial)
        self.ledger.check()
        metric = {key: readonly(finite(metric_raw[key], (160,), key))
                  for key in ("a", "a_s", "a_ss")}
        b = readonly(finite(height_raw["b"], (160,), "reference height density"))
        null = readonly(finite(self.field.null_basis.values(radial), (160, 5),
                               "original exact-null height density"))
        active = (radial > self.field.null_basis.left) & (radial < self.field.null_basis.right)
        # State restoration retains the parent's supported-row write.  The
        # original JVP uses the exact density on all rows, including its zeros.
        delta_b = null@self.state[154:] if np.any(self.state[154:] != 0) else None
        event["common_inputs"] = {
            "seconds": time.monotonic()-common_tick,
            "metric_a_sha256": array_digest(metric["a"]),
            "metric_a_s_sha256": array_digest(metric["a_s"]),
            "height_b_sha256": array_digest(b),
            "null_density_sha256": array_digest(null),
            "active_null_radial_rows": np.flatnonzero(active).tolist(),
            "bounded_metric_calls": 1, "bounded_height_jets_calls": 1,
            "fixed_height_primitive_calls": 0, "control_height_primitive_calls": 0}
        self.capture["_completed_arrays"].update(
            state159=self.state, reference163=self.reference163,
            radial=radial, null_density=null, reference_height_b=b)
        for label in LABELS:
            self.ledger.check()
            nr, nt = SHAPES[label]
            tick = time.monotonic()
            gevent = {"grid": label, "status": "restoring"}
            event.setdefault("grids", []).append(gevent)
            try:
                scalar_grid = self.single.source.grid_for(radial, theta[label])
                fields = scalar_grid.fields(self.reference163)
                fields["_theta"] = theta[label][None, :]
                frame = target_frame(fields)
                T = readonly(finite(frame["T"], (nr, nt, 3), label+"/T"))
                P0 = periodic_operator(T, -1)
                P1 = periodic_operator(frame["Ts"], -1)
                U = metric["a_s"][:, None, None]*P0 + metric["a"][:, None, None]*P1
                U[:, :, 2] += b[:, None]
                if delta_b is not None:
                    U[active, :, 2] += delta_b[active, None]
                U = readonly(finite(U, (nr, nt, 3), label+"/U"))
                restored_e = (np.sum(U*U, axis=2)-1.).reshape(-1)
                restored_f = np.sum(U*T, axis=2).reshape(-1)
                count = nr*nt
                e = paid_array(model["complete_base_e_f"][label]["e"], (count,), label+"/paid e")
                f = paid_array(model["complete_base_e_f"][label]["f"], (count,), label+"/paid f")
                checks = {}
                for name, got, expected in (("e", restored_e, e), ("f", restored_f, f)):
                    error = float(np.max(np.abs(got-expected), initial=0.))
                    scale = max(1., float(np.max(np.abs(expected), initial=0.)))
                    limit = self.replay_relative_tolerance*scale
                    checks[name] = {
                        "maximum_absolute_error": error, "tolerance_limit": limit,
                        "restored_array_sha256": array_digest(got),
                        "paid_array_sha256": array_digest(expected), "passed": error <= limit}
                    self.statistics["maximum_input_e_f_error"] = max(
                        self.statistics["maximum_input_e_f_error"], error)
                    require(error <= limit, "necessary U/T input restore disagrees with paid "+label+"/"+name)
                branches = []
                for group in (0, 1):
                    groups = np.full(count, group, dtype=np.int64)
                    values = readonly(phi(e, f, groups, self.epsilon))
                    g_e, g_f = phi_gradient(e, f, groups, self.epsilon)
                    branches.append({"phi": values, "ge": readonly(g_e), "gf": readonly(g_f)})
                self.base[label] = {
                    "radial": radial, "theta": theta[label], "metric": metric,
                    "a": metric["a"], "a_s": metric["a_s"], "null": null,
                    "U": U, "T": T, "e": e, "f": f, "branches": branches,
                    "scalar_grid": scalar_grid, "fields": fields, "frame": frame}
                self.families._families(scalar_grid, nr, nt)
                self.statistics["restored_grid_count"] += 1
                self.capture["_completed_arrays"][label+"/U"] = U
                self.capture["_completed_arrays"][label+"/T"] = T
                gevent.update(
                    status="complete", seconds=time.monotonic()-tick, point_count=count,
                    current_U_sha256=array_digest(U), current_T_sha256=array_digest(T),
                    paid_input_comparison=checks, complete_periodic_primitive_calls=2,
                    ordinary_geometry_calls=0, original_parameter_J_calls=0)
                self.ledger.check()
            except Exception as error:
                gevent.update(status="raised", seconds=time.monotonic()-tick,
                              error=self._error(error))
                raise
        self.phi0 = max(self.target, *(
            float(np.max(self.base[label]["branches"][group]["phi"]))
            for label in LABELS for group in (0, 1)))
        require(self.phi0 == float(model["complete_original_phi0"]),
                "paid complete branch maximum changed")
        self.binding = {
            "schema": POLICY+"-restored-input-binding",
            "source_model_binding_sha256": self.model_binding_sha256,
            "physical_state_sha256": self.model_binding["physical_state_sha256"],
            "state159_sha256": array_digest(self.state),
            "reference163_sha256": array_digest(self.reference163),
            "configuration_sha256": self.cfg_sha256,
            "original_complete_value_binding_sha256": digest(original_value_binding),
            "grids": copy.deepcopy(grid_binding), "epsilon": self.epsilon,
            "constant_target": self.target, "paid_phi0": self.phi0,
            "physical_norm_cost_mu": self.mu,
            "restored_inputs": {
                label: {key: array_digest(self.base[label][key])
                        for key in ("U", "T", "e", "f", "a", "a_s", "null")}
                for label in LABELS}}
        self.binding_sha256 = digest(self.binding)

    def _assert_context(self):
        require(self._ready, "the necessary first-jet inputs are not complete")
        self.ledger.check()
        self.field._assert_shared_context()
        require(digest(self.cfg) == self.cfg_sha256
                and array_digest(self.state) == self.model_binding["state_sha256"],
                "frozen first-jet input context changed")

    def _attainer(self, label, group, point, value, slope):
        grid = self.grids[label]
        d = self.base[label]
        ri, ti = divmod(point, grid.nt)
        return {
            "grid": label, "group": int(group), "point": int(point),
            "flat_row_id": int(group*grid.point_count+point),
            "original_row": grid.coordinate(group*grid.point_count+point),
            "radial_index": int(ri), "theta_index": int(ti),
            "base_e": float(d["e"][point]), "base_f": float(d["f"][point]),
            "base_phi": float(d["branches"][group]["phi"][point]),
            "linear_branch_value": float(value), "directional_slope": float(slope),
            "gradient_already_paid": (label, group*grid.point_count+point) in self.paid_rows}

    def scan(self, direction, *, phase):
        """One new complete first-order scan; not phi(e+de,f+df) or geometry."""
        self._assert_context()
        p = owned(finite(direction, (N,), "physical159 direction"))
        key = array_digest(p)
        if key in self.scans:
            require(np.array_equal(p, self.scans[key]["direction"]), "direction hash collision")
            self.statistics["direction_cache_hits"] += 1
            return self.scans[key]
        require(key not in self.direction_attempts,
                "a failed direction is retained, not automatically replayed")
        require(len(self.direction_attempts) < MAX_DISTINCT_DIRECTIONS,
                "at most two distinct authorized physical directions are allowed")
        require(isinstance(phase, str) and phase, "explicit new-direction phase required")
        event = self._begin(
            "pair_first_jet_jvps", phase=phase, direction_sha256=key,
            restored_input_binding_sha256=self.binding_sha256)
        self.direction_attempts[key] = event
        self.statistics["pair_first_jet_started"] += 1
        arrays, branches, coverage = {}, [], {}
        tick = time.monotonic()
        try:
            for label in LABELS:
                self.ledger.check()
                start = time.monotonic()
                d, grid = self.base[label], self.grids[label]
                gevent = {"grid": label, "status": "started"}
                event.setdefault("grids", []).append(gevent)
                try:
                    dT, dTs = direction_frame_jets(
                        self.families, d["scalar_grid"], d["fields"], d["frame"], p)
                    self.ledger.check()
                    dP0, dP1 = periodic_operator(dT, -1), periodic_operator(dTs, -1)
                    dU = d["a_s"][:, None, None]*dP0+d["a"][:, None, None]*dP1
                    dU[:, :, 2] += (d["null"]@p[154:])[:, None]
                    de = readonly(finite(
                        (2*np.sum(d["U"]*dU, axis=2)).reshape(-1),
                        (grid.point_count,), label+"/de"))
                    df = readonly(finite(
                        np.sum(d["T"]*dU+d["U"]*dT, axis=2).reshape(-1),
                        (grid.point_count,), label+"/df"))
                    arrays[label] = {
                        "e": d["e"], "f": d["f"], "de": de, "df": df,
                        "dT": readonly(finite(dT)), "dTs": readonly(finite(dTs)),
                        "dU": readonly(finite(dU))}
                    self.capture["_completed_arrays"][key+"/"+label+"/de"] = de
                    self.capture["_completed_arrays"][key+"/"+label+"/df"] = df
                    for group in (0, 1):
                        b = d["branches"][group]
                        slopes = b["ge"]*de+b["gf"]*df
                        values = finite(b["phi"]+slopes, (grid.point_count,),
                                        label+"/linear branch")
                        point = int(np.argmax(values))
                        branches.append(self._attainer(
                            label, group, point, values[point], slopes[point]))
                    coverage[label] = grid.point_count
                    self.statistics["completed_grid_JVPs"] += 1
                    gevent.update(
                        status="complete", seconds=time.monotonic()-start,
                        point_count=grid.point_count,
                        complete_original_theta_count=grid.nt,
                        complete_periodic_primitive_calls=2,
                        de_sha256=array_digest(de), df_sha256=array_digest(df),
                        dT_sha256=array_digest(dT), dTs_sha256=array_digest(dTs),
                        dU_sha256=array_digest(dU),
                        no_full_grid_parameter_axes=True)
                    self.ledger.check()
                except Exception as error:
                    gevent.update(status="raised", seconds=time.monotonic()-start,
                                  error=self._error(error))
                    raise
            maximum = max(self.target, *(item["linear_branch_value"] for item in branches))
            result = {
                "schema": POLICY+"-complete-first-jet",
                "binding_sha256": self.binding_sha256,
                "source_model_binding_sha256": self.model_binding_sha256,
                "direction": p, "direction_sha256": key, "phase": phase,
                "arrays": arrays, "branches": branches, "coverage": coverage,
                "base_phi": self.phi0, "target": self.target,
                "constant_target_branch": {
                    "value": self.target, "directional_slope": 0.0,
                    "physical_gradient_is_zero": True},
                "physical_norm_cost_mu": self.mu,
                "linear_maximum": float(maximum),
                "unpenalized_first_order_gain": float(self.phi0-maximum),
                "ordinary_geometry_calls": 0,
                "claim_is_only_complete_discrete_first_order": True}
            self.scans[key] = result
            self.statistics["pair_first_jet_completed"] += 1
            self._end(event, seconds=time.monotonic()-tick,
                      coverage=copy.deepcopy(coverage), branches=copy.deepcopy(branches),
                      linear_maximum=float(maximum), new_full_grid_JVP_calls=2)
            return result
        except Exception as error:
            self.capture["last_direction_failure"] = self._error(error)
            self._end(event, error, seconds=time.monotonic()-tick,
                      completed_coverage=copy.deepcopy(coverage),
                      completed_array_hashes={
                          label: {name: array_digest(value) for name, value in row.items()}
                          for label, row in arrays.items()})
            raise

    def is_paid_row(self, label, flat_row_id):
        require(label in LABELS and type(flat_row_id) is int
                and 0 <= flat_row_id < 2*self.grids[label].point_count,
                "one original metric row ID is required")
        return (label, flat_row_id) in self.paid_rows

    def attainer_gradient(self, label, flat_row_id, *, scan):
        """At most four new original rows; no factorized.evaluate invocation.

        Only an actual argmax from a completed new scan is eligible.  Existing
        paid rows must be read from the caller's paid gradient table instead.
        One point's de159/df159 is reusable for its other original branch.
        """
        self._assert_context()
        require(label in LABELS and type(flat_row_id) is int,
                "literal original grid/row identity required")
        require(isinstance(scan, dict) and scan.get("binding_sha256") == self.binding_sha256
                and self.scans.get(scan.get("direction_sha256")) is scan,
                "one completed same-center scan is required")
        grid = self.grids[label]
        require(0 <= flat_row_id < 2*grid.point_count,
                "only original metric rows are eligible")
        matches = [item for item in scan["branches"]
                   if item["grid"] == label and item["flat_row_id"] == flat_row_id]
        require(len(matches) == 1, "only a new scan's original argmax row may be differentiated")
        item = matches[0]
        key = (label, flat_row_id)
        require(key not in self.paid_rows,
                "this original gradient is already paid; reuse it without new differentiation")
        if key in self.gradients:
            result = self.gradients[key]
            self._compare_gradient_direction(result, scan, item)
            return result
        require(key not in self.gradient_attempts,
                "a failed original row is retained, not automatically replayed")
        require(len(self.gradient_attempts) < MAX_NEW_ORIGINAL_ROWS,
                "at most four genuinely new original argmax gradients are allowed")
        event = self._begin(
            "new_attainer_gradients", original_row=copy.deepcopy(item["original_row"]),
            direction_sha256=scan["direction_sha256"],
            restored_input_binding_sha256=self.binding_sha256)
        self.gradient_attempts[key] = event
        self.statistics["new_original_rows_started"] += 1
        tick = time.monotonic()
        try:
            group, point = divmod(flat_row_id, grid.point_count)
            radial_index, theta_index = divmod(point, grid.nt)
            point_key = (label, point)
            d = self.base[label]
            if point_key not in self.point_gradients:
                de = np.zeros(N)
                df = np.zeros(N)
                fields = _radial_slice(d["fields"], radial_index, grid.nr)
                frame = _radial_slice(d["frame"], radial_index, grid.nr)
                metric = {name: value[radial_index:radial_index+1]
                          for name, value in d["metric"].items()}
                U = d["U"][radial_index:radial_index+1, theta_index]
                T = d["T"][radial_index:radial_index+1, theta_index]
                ri, ti = np.array([0], dtype=np.int64), np.array([theta_index], dtype=np.int64)
                event["families"] = []
                for name, angular, angular_first, radial, start, stop in self.families._families(
                        d["scalar_grid"], grid.nr, grid.nt):
                    self.ledger.check()
                    family_tick = time.monotonic()
                    record = {"name": name, "start": int(start), "stop": int(stop),
                              "status": "started"}
                    event["families"].append(record)
                    try:
                        kernels = angular_kernels(
                            fields, frame, name, angular, angular_first, second=False)
                        virtual = virtual_selected_jets(
                            kernels, ri, ti, metric, second=False)
                        local_de = 2*np.einsum("ic,icn->in", U, virtual["Xs"])
                        local_df = (np.einsum("ic,icn->in", T, virtual["Xs"])
                                    +np.einsum("ic,icn->in", U, virtual["T"]))
                        radial_one = tuple(value[radial_index:radial_index+1] for value in radial)
                        de[start:stop] = expand_radial_rows(local_de, radial_one, ri)[0]
                        df[start:stop] = expand_radial_rows(local_df, radial_one, ri)[0]
                        record.update(
                            status="complete", seconds=time.monotonic()-family_tick,
                            full_original_angle_count=grid.nt,
                            virtual_parameter_columns=int(local_de.shape[1]),
                            complete_periodic_primitive_calls=2,
                            ordinary_geometry_calls=0)
                        del kernels, virtual, local_de, local_df
                        self.ledger.check()
                    except Exception as error:
                        record.update(status="raised", seconds=time.monotonic()-family_tick,
                                      error=self._error(error))
                        raise
                C = d["null"][radial_index]
                de[154:] = 2*U[0, 2]*C
                df[154:] = T[0, 2]*C
                de, df = readonly(finite(de, (N,), "new original de159")), readonly(
                    finite(df, (N,), "new original df159"))
                self.point_gradients[point_key] = {"de": de, "df": df}
                self.statistics["new_point_gradient_contractions"] += 1
                event["point_gradient_reused"] = False
            else:
                de, df = (self.point_gradients[point_key][name] for name in ("de", "df"))
                self.statistics["point_gradient_reuses"] += 1
                event["point_gradient_reused"] = True
            ge = float(d["branches"][group]["ge"][point])
            gf = float(d["branches"][group]["gf"][point])
            gradient = readonly(finite(ge*de+gf*df, (N,), "new original branch gradient159"))
            result = {
                "schema": POLICY+"-new-original-attainer-gradient",
                "binding_sha256": self.binding_sha256,
                "grid": label, "flat_row_id": flat_row_id, "group": group, "point": point,
                "original_row": copy.deepcopy(item["original_row"]),
                "base_e": float(d["e"][point]), "base_f": float(d["f"][point]),
                "base_phi": float(d["branches"][group]["phi"][point]),
                "de159": de, "df159": df, "gradient159": gradient,
                "gradient_sha256": array_digest(gradient),
                "source": "new-attainer-first-jet-kernels-with-restored-U-T",
                "ordinary_geometry_calls": 0, "old_selected_J_calls": 0,
                "second_order_kernels": False}
            self.capture["_completed_arrays"][
                "gradient/"+label+"/"+str(flat_row_id)] = gradient
            self._compare_gradient_direction(result, scan, item)
            self.gradients[key] = result
            self.statistics["new_original_rows_completed"] += 1
            self._end(event, seconds=time.monotonic()-tick,
                      gradient_sha256=result["gradient_sha256"],
                      de159_sha256=array_digest(de), df159_sha256=array_digest(df),
                      original_chain_rule_comparison=copy.deepcopy(result["last_direction_comparison"]))
            return result
        except Exception as error:
            self.capture["last_gradient_failure"] = self._error(error)
            self._end(event, error, seconds=time.monotonic()-tick)
            raise

    def _compare_gradient_direction(self, result, scan, item):
        direct = float(result["gradient159"]@scan["direction"])
        expected = float(item["directional_slope"])
        error = abs(direct-expected)
        limit = self.replay_relative_tolerance*max(1., abs(direct), abs(expected))
        result["last_direction_comparison"] = {
            "direction_sha256": scan["direction_sha256"],
            "selected_gradient_dot_physical_direction": direct,
            "already_computed_complete_JVP_slope": expected,
            "absolute_error": error, "original_relative_tolerance_limit": limit,
            "no_extra_JVP_or_geometry": True, "passed": error <= limit}
        self.statistics["maximum_gradient_dot_JVP_error"] = max(
            self.statistics["maximum_gradient_dot_JVP_error"], error)
        require(error <= limit, "new original gradient and completed JVP disagree")

    def cache_arrays(self):
        """All useful finite arrays, without serialization or scientific work."""
        out = dict(self.capture.get("_completed_arrays", {}))
        for label, d in self.base.items():
            for key in ("U", "T", "e", "f", "radial", "theta", "a", "a_s", "null"):
                out["base/"+label+"/"+key] = d[key]
            _tree_arrays(d["metric"], "base/"+label+"/metric", out)
            _tree_arrays(d["fields"], "base/"+label+"/fields", out)
            _tree_arrays(d["frame"], "base/"+label+"/frame", out)
            for group, branch in enumerate(d["branches"]):
                _tree_arrays(branch, "base/"+label+"/branch"+str(group), out)
        for key, scan in self.scans.items():
            out["scan/"+key+"/direction"] = scan["direction"]
            _tree_arrays(scan["arrays"], "scan/"+key, out)
        for (label, point), row in self.point_gradients.items():
            _tree_arrays(row, "point-gradient/"+label+"/"+str(point), out)
        for (label, flat), result in self.gradients.items():
            out["gradient/"+label+"/"+str(flat)] = result["gradient159"]
        return out

    def cache_manifest(self):
        return {key: _array_record(value) for key, value in self.cache_arrays().items()}

    def report(self):
        """Small report; the driver can persist cache_arrays once separately."""
        return {
            "schema": POLICY+"-report", "status": self.capture.get("status"),
            "binding": copy.deepcopy(getattr(self, "binding", None)),
            "binding_sha256": getattr(self, "binding_sha256", None),
            "statistics": copy.deepcopy(self.statistics),
            "events": copy.deepcopy(self.events),
            "completed_direction_hashes": list(self.scans),
            "completed_new_original_rows": [
                {"grid": label, "flat_row_id": flat} for label, flat in self.gradients],
            "limits": {"distinct_physical_directions": MAX_DISTINCT_DIRECTIONS,
                       "new_original_attainer_rows": MAX_NEW_ORIGINAL_ROWS},
            "no_new_ordinary_value_or_full_gradient_claim": True,
            "no_continuous_grid_certificate": True}
