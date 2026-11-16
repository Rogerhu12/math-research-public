#!/usr/bin/env python3
"""Paid-cache first jets for the genuinely augmented true53 exchange master.

Import-only; no Actions, developer, optimizer, ordinary geometry, old selected J
or old directional JVP entry is executed.  The caller owns the one source read,
all 600-second task accounting, new finite-master iterations and stdout.

U, T, e, f, a, a_s and null densities are read from paid records.  Only the
missing scalar-grid fields and the first-variation frame coefficients are
restored.  There is no target_frame call and no reconstructed T, Ts or U.
New work is at most 32 distinct complete two-grid directions and 128 genuinely
new original attainer gradients, under the caller's single shared ledger.
"""
from __future__ import annotations

import copy
from fractions import Fraction
import time

import numpy as np

from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
from frame_collar_bvp import mul
from frame_complete_affine_metric_oracle import direction_frame_jets
from frame_selected_row_radial_jacobian import angular_kernels, expand_radial_rows, periodic_operator
from frame_metric_affine_spectral_model import phi, phi_gradient
from frame_metric_true53_positive_direction_jets import (
    PositiveDirectionFirstJets as _PaidImplementation,
    _OriginalFamilies, _radial_slice, _array_record,
    require, finite, owned, readonly, paid_array)

POLICY = "same159-true53-augmented-paid-cache-first-jets-v1"
N = 159
LABELS = ("coarse", "fine")
SHAPES = {"coarse": (160, 384), "fine": (160, 768)}
MAX_DISTINCT_DIRECTIONS = 32
MAX_NEW_ORIGINAL_ROWS = 128
SOURCE = {
    "run_id": "43821568604", "job_id": "133145590135",
    "source_commit": "323f36fefc0380898aa1e3c0f195e08a32f1fbc1"}
SOURCE_CACHE_BYTES = 30232607
SOURCE_CACHE_SHA256 = "0c1826ad8f554b6eb2c440e54a5582a9711a05b023f4e2756c300d947d854b40"
SOURCE_INPUT_BINDING = "75e07691773d43a00f4aa4192499721ff9490784feaaf18d983ef621e95893e7"
SOURCE_MODEL_BINDING = "e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1"
SOURCE_PHYSICAL = "9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e"
REQUIRED_NEW_PAID_ROWS = frozenset((
    ("coarse", 43322), ("coarse", 91304),
    ("fine", 86645), ("fine", 182607)))


def _variation_frame(fields):
    """The literal needed subset of frame_collar_bvp.target_frame.

    No value T/Ts/V is generated.  Arithmetic association for Tpart and
    Ts_value_part is the original one.  These coefficients are inputs for
    direction_frame_jets and complete_tangent_parameter_jets(order=1).
    """
    u, v = (fields[name]["value"] for name in ("u", "v"))
    psi = fields["_theta"]+u
    zero = np.zeros_like(u)
    ez = np.stack((zero, zero, np.ones_like(u)), axis=-1)
    normal = np.stack((np.cos(psi), np.sin(psi), zero), axis=-1)
    horizontal = np.stack((-np.sin(psi), np.cos(psi), zero), axis=-1)
    c = 1/np.sqrt(1+v*v)
    Tu = -mul(c, normal)
    Tv = mul(c**3, ez-v[..., None]*horizontal)
    Tuu = -mul(c, horizontal)
    Tuv = mul(v*c**3, normal)
    Tvv = mul((2*v*v-1)*c**5, horizontal)-mul(3*v*c**5, ez)
    us, vs = (fields[name]["s"] for name in ("u", "v"))
    frame = {
        "Tpart": {"u": Tu, "v": Tv},
        "Ts_value_part": {
            "u": mul(us, Tuu)+mul(vs, Tuv),
            "v": mul(us, Tuv)+mul(vs, Tvv)}}
    for group in frame.values():
        for key, value in group.items():
            group[key] = readonly(finite(value, u.shape+(3,), "first variation "+key))
    return frame


def _first_order_selected_rows(kernels, U, T, a, a_s, theta_index):
    """Original R/R' coefficients, with a structurally zero R'' coefficient.

    delta T = F0 R
    delta Xs = (a_s P0 + a P1) R + a P0 R'
    Thus de=2 U.dot(delta Xs), df=T.dot(delta Xs)+U.dot(delta T).
    Unlike virtual_selected_jets, this first-order-only helper never reads
    a_ss.  It cannot be used for second=True or a curvature derivative.
    """
    ri = np.array([0], dtype=np.int64)
    ti = np.array([theta_index], dtype=np.int64)
    f0, p0, p1 = (np.asarray(kernels[key])[ri, ti]
                  for key in ("F0", "P0", "P1"))
    radius = np.asarray(a, float).reshape(1, 1, 1)
    first = np.asarray(a_s, float).reshape(1, 1, 1)
    x0 = first*p0+radius*p1
    x1 = radius*p0
    zero = np.zeros_like(f0)
    # Match the frozen virtual (jet,mode) ordering before expand_radial_rows.
    xs = np.stack((x0, x1, zero), axis=-2).reshape(1, 3, 3*f0.shape[-1])
    dt = np.stack((f0, zero, zero), axis=-2).reshape(1, 3, 3*f0.shape[-1])
    de = 2*np.einsum("ic,icn->in", U, xs)
    df = np.einsum("ic,icn->in", T, xs)+np.einsum("ic,icn->in", U, dt)
    return finite(de), finite(df)


def _vector(value, name):
    if isinstance(value, dict) and value.get("dtype") == "float64":
        return paid_array(value, (N,), name)
    if isinstance(value, dict) and "binary64" in value:
        result = readonly(finite(value["binary64"], (N,), name))
        require(value.get("length") == N
                and value.get("array_sha256") == array_digest(result),
                "original vector fingerprint changed: "+name)
        exact = value.get("exact_binary64")
        if exact is not None:
            require(exact == [str(Fraction.from_float(float(x))) for x in result],
                    "original exact vector differs: "+name)
        return result
    return readonly(finite(value, (N,), name))


class AugmentedFirstJets(_PaidImplementation):
    """Same immutable physical center, a new independently accounted oracle.

    Constructor:
      (prepared, paid_model, paid_cache, ledger, *,
       known_gradients, source_receipt, paid_scan, fine_theta=None, capture=None)

    known_gradients is the four actual ATTAINER_GRADIENT records.  The original
    5743 selected and five added rows are read directly from paid_model.
    The four supplied records must be the four distinct original new rows.

    Ledger protocol: check(); begin(kind, **metadata)->dict;
    end(event, error=None, **metadata).  Kinds are first_jet_input_restores
    (one), pair_first_jet_jvps (32 new pairs), new_attainer_gradients (128 new
    original rows).  The caller installs these limits on the SAME ledger as
    its new LP/scalar/value task.  Imports and source fetch precede this class
    but must already be inside that task clock.

    Reused parent methods are only the unchanged context, row-tag and error
    metadata helpers.  The old constructor, old limits and old execution
    methods are not called or patched.
    """
    def __init__(self, prepared, paid_model, paid_cache, ledger, *,
                 known_gradients, source_receipt, paid_scan,
                 fine_theta=None, capture=None):
        self.ledger = ledger
        require(all(callable(getattr(ledger, name, None))
                    for name in ("check", "begin", "end")), "one shared started ledger required")
        self.capture = {} if capture is None else capture
        require(isinstance(self.capture, dict) and not self.capture, "fresh capture dict required")
        self.events, self.base, self.scans = [], {}, {}
        self.direction_attempts, self.gradient_attempts = {}, {}
        self.gradients, self.known_gradients, self.point_gradients = {}, {}, {}
        self.paid_rows = set()
        self._ready = False
        self._last_scan_key = None
        self._last_attempt_arrays = {}
        self._last_attempt_key = None
        self.families = _OriginalFamilies()
        self.statistics = {
            "input_restores_started": 0, "input_restores_completed": 0,
            "restored_grid_count": 0, "scalar_grid_fields_calls_started": 0,
            "scalar_grid_fields_calls_completed": 0,
            "first_variation_frame_builds_started": 0,
            "first_variation_frame_builds_completed": 0,
            "pair_first_jet_started": 0, "pair_first_jet_completed": 0,
            "direction_cache_hits": 0, "paid_direction_cache_hits": 0,
            "completed_grid_JVPs": 0, "known_gradient_cache_hits": 0,
            "new_original_rows_started": 0, "new_original_rows_completed": 0,
            "new_point_gradient_contractions": 0, "point_gradient_reuses": 0,
            "ordinary_geometry_calls": 0, "old_selected_J_evaluate_calls": 0,
            "old_first_jet_replays": 0, "paid_U_T_rebuilds": 0,
            "base_metric_or_height_jets_calls": 0, "height_primitive_calls": 0,
            "full_grid_parameter_axis159_tensors": 0,
            "ordinary_position_or_two_jet_assemblies": 0,
            "maximum_input_e_f_error": 0.0,
            "maximum_paid_margin_to_full_phi_error": 0.0,
            "maximum_gradient_dot_JVP_error": 0.0}
        self.capture.update(
            schema=POLICY+"-capture", status="initializing", events=self.events,
            statistics=self.statistics, direction_attempts=self.direction_attempts,
            gradient_attempts=self.gradient_attempts,
            _completed_arrays={}, _last_direction_arrays=self._last_attempt_arrays)
        event = self._begin("first_jet_input_restores",
                            source_model_binding_sha256=paid_model.get("binding_sha256"))
        self.statistics["input_restores_started"] += 1
        tick = time.monotonic()
        try:
            self._initialize(prepared, paid_model, paid_cache, source_receipt,
                             fine_theta, event)
            self._install_known_gradients(paid_model, known_gradients, paid_cache)
            self._finish_binding()
            self._register_paid_scan(paid_scan, paid_cache)
            self._ready = True
            self.statistics["input_restores_completed"] += 1
            self.capture.update(status="ready", binding=copy.deepcopy(self.binding),
                                binding_sha256=self.binding_sha256)
            self._end(event, seconds=time.monotonic()-tick,
                      restored_grids=list(self.base),
                      known_original_gradient_count=len(self.known_gradients),
                      paid_direction_sha256=self.paid_direction_sha256,
                      scalar_fields_only_not_ordinary_geometry=True,
                      paid_U_T_rebuilds=0, old_selected_J_or_JVP_calls=0)
        except Exception as error:
            self.capture.update(status="input-restore-failed", error=self._error(error))
            self._end(event, error, seconds=time.monotonic()-tick,
                      completed_grids=list(self.base))
            raise

    def _begin(self, kind, **metadata):
        self.ledger.check()
        event = self.ledger.begin(kind, **metadata)
        require(isinstance(event, dict), "ledger.begin must return a mutable dict")
        event["module_policy"] = POLICY
        self.events.append(event)
        return event

    def _end(self, event, error=None, **metadata):
        if error is None:
            self.ledger.check()
        self.ledger.end(event, error, **metadata)

    def _initialize(self, prepared, model, cache, receipt, fine_theta, event):
        require(isinstance(receipt, dict) and isinstance(receipt.get("source"), dict)
                and all(str(receipt["source"].get(k)) == v for k, v in SOURCE.items()),
                "the one paid positive-direction source is required")
        source = receipt["source"]
        require(isinstance(source.get("workflow"),str)
                and source["workflow"].startswith(".github/workflows/")
                and type(source.get("log_bytes")) is int and source["log_bytes"] > 0
                and isinstance(source.get("log_sha256"),str)
                and len(source["log_sha256"])==64,
                "the source reader must provide its original workflow/log receipt")
        record = receipt.get("cache_record", {})
        require(record.get("JSON_plus_LF_bytes") == SOURCE_CACHE_BYTES
                and record.get("JSON_plus_LF_sha256") == SOURCE_CACHE_SHA256,
                "literal paid CACHE JSON+LF receipt required")
        require(isinstance(model, dict) and digest(model["binding"]) == SOURCE_MODEL_BINDING
                == model.get("binding_sha256"), "original complete true53 MODEL required")
        require(isinstance(cache, dict) and cache.get("partial") is False
                and cache.get("source_model_binding_sha256") == SOURCE_MODEL_BINDING
                and cache.get("source_physical_state_sha256") == SOURCE_PHYSICAL
                and cache.get("first_jet_input_binding_sha256") == SOURCE_INPUT_BINDING
                and digest(cache["first_jet_input_binding"]) == SOURCE_INPUT_BINDING,
                "complete same-center paid first-jet cache required")
        self.source_receipt = copy.deepcopy(receipt)
        self.source_input_binding = copy.deepcopy(cache["first_jet_input_binding"])
        self.model_binding = copy.deepcopy(model["binding"])
        self.model_binding_sha256 = model["binding_sha256"]
        self.field = prepared["problem"]
        self.cfg = copy.deepcopy(prepared["cfg"])
        self.cfg_sha256 = digest(self.cfg)
        self.grids = dict(prepared["row_grids"])
        require(set(self.grids) == set(LABELS), "both original rational grids required")
        arrays = cache["binary64_round_trip_arrays"]
        require(isinstance(arrays, dict), "paid plain round-trip array records required")
        self.state = paid_array(arrays["state159"], (N,), "paid state159")
        require(np.array_equal(self.field.coordinates.validate(prepared["initial159"]), self.state)
                and np.array_equal(paid_array(model["source_current_independent159"], (N,), "MODEL159"), self.state)
                and array_digest(self.state) == self.model_binding["state_sha256"],
                "the current physical159 center changed")
        self.reference163 = paid_array(arrays["reference163"], (163,), "paid reference163")
        require(np.array_equal(self.field.coordinates.reference_evaluation_state(self.state),
                               self.reference163)
                and array_digest(self.reference163) == self.model_binding["reference163_sha256"],
                "the true reference163 or exact-null lift changed")
        require(self.cfg_sha256 == self.model_binding["configuration_sha256"]
                and self.field.coordinate_definition_sha256 == self.model_binding["coordinate_definition_sha256"]
                and digest(self.field.evaluation_definition()) == self.model_binding["ordinary_field_evaluation_sha256"]
                and digest(self.field.identity(self.state)) == self.model_binding["physical_state_sha256"]
                == SOURCE_PHYSICAL, "original physical/evaluation/configuration definitions changed")
        self.field._assert_shared_context()
        self.epsilon = float(Fraction(self.cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Fraction(self.cfg["fixed_metric_budget_exact"]))
        self.mu = float(model["physical_norm_cost_mu"])
        self.replay_relative_tolerance = float(self.cfg["value_Jacobian_replay_relative_tolerance"])
        require(self.epsilon == float(model["epsilon"]) == 1e-8
                and self.target == float(model["constant_target"]) == .26
                and np.isfinite(self.mu) and self.mu > 0
                and np.isfinite(self.replay_relative_tolerance)
                and self.replay_relative_tolerance > 0, "original scalar branch constants changed")
        radial = paid_array(arrays["radial"], (160,), "paid common radial")
        null = paid_array(arrays["null_density"], (160, 5), "paid null density")
        b = paid_array(arrays["reference_height_b"], (160,), "paid reference height density")
        require(np.array_equal(radial, finite(prepared["radial"], (160,), "prepared radial")),
                "original radial ordering changed")
        self.capture["_completed_arrays"].update(
            state159=self.state, reference163=self.reference163, radial=radial,
            null_density=null, reference_height_b=b)
        self.single = self.field._direct_single
        require(self.single is self.field.original_problem
                and self.field._direct_bounded is self.single.base,
                "the original direct-reference field chain is required")
        self._grid_binding, input_hashes = {}, {}
        for label in LABELS:
            self.ledger.check()
            tick = time.monotonic()
            grid = self.grids[label]
            nr, nt = SHAPES[label]
            gevent = {"grid": label, "status": "reading-paid-inputs"}
            event.setdefault("grids", []).append(gevent)
            try:
                r = paid_array(arrays["input/"+label+"/radial"], (nr,), label+"/radial")
                theta = paid_array(arrays["input/"+label+"/theta"], (nt,), label+"/theta")
                a = paid_array(arrays["input/"+label+"/a"], (nr,), label+"/a")
                a_s = paid_array(arrays["input/"+label+"/a_s"], (nr,), label+"/a_s")
                n = paid_array(arrays["input/"+label+"/null"], (nr,5), label+"/null")
                U = paid_array(arrays[label+"/U"], (nr,nt,3), label+"/U")
                T = paid_array(arrays[label+"/T"], (nr,nt,3), label+"/T")
                e = paid_array(model["complete_base_e_f"][label]["e"], (nr*nt,), label+"/e")
                f = paid_array(model["complete_base_e_f"][label]["f"], (nr*nt,), label+"/f")
                require(np.array_equal(r,radial) and np.array_equal(n,null)
                        and grid.label == label and grid.nr == nr and grid.nt == nt
                        and grid.point_count == nr*nt
                        and grid.definition == self.model_binding["original_grid_definitions"][label]
                        and np.array_equal(r,np.array([float(v) for v in grid.nodes])),
                        "original grid/state row identity changed: "+label)
                if label == "coarse":
                    require(np.array_equal(theta,finite(prepared["theta"],(nt,),"prepared theta")),
                            "original coarse theta order changed")
                elif fine_theta is not None:
                    require(np.array_equal(theta,finite(fine_theta,(nt,),"prepared fine theta")),
                            "original fine theta order changed")
                self._grid_binding[label] = {
                    "grid":grid.definition_sha256,"radial":array_digest(r),"theta":array_digest(theta)}
                input_hashes[label] = {key:array_digest(value) for key,value in
                    (("U",U),("T",T),("e",e),("f",f),("a",a),("a_s",a_s),("null",n))}
                require(input_hashes[label] == self.source_input_binding["restored_inputs"][label]
                        and self._grid_binding[label] == self.source_input_binding["grids"][label],
                        "paid first-jet array/context binding changed: "+label)
                # This is only the missing coefficient context, not an ordinary
                # value, an old J, a value tangent T or a reconstructed U.
                gevent["status"] = "restoring-scalar-coefficient-context"
                self.statistics["scalar_grid_fields_calls_started"] += 1
                scalar_grid = self.single.source.grid_for(r,theta)
                fields = scalar_grid.fields(self.reference163)
                fields["_theta"] = theta[None,:]
                self.statistics["scalar_grid_fields_calls_completed"] += 1
                self.ledger.check()
                self.statistics["first_variation_frame_builds_started"] += 1
                frame = _variation_frame(fields)
                self.statistics["first_variation_frame_builds_completed"] += 1
                branches = []
                for group in (0,1):
                    groups = np.full(nr*nt,group,dtype=np.int64)
                    ge,gf = phi_gradient(e,f,groups,self.epsilon)
                    branches.append({"phi":readonly(finite(phi(e,f,groups,self.epsilon))),
                                     "ge":readonly(finite(ge)),"gf":readonly(finite(gf))})
                self.base[label] = {
                    "radial":r,"theta":theta,"a":a,"a_s":a_s,"null":n,
                    "metric":{"a":a,"a_s":a_s},"U":U,"T":T,"e":e,"f":f,
                    "branches":branches,"scalar_grid":scalar_grid,"fields":fields,"frame":frame}
                self.families._families(scalar_grid,nr,nt)
                self.capture["_completed_arrays"][label+"/U"] = U
                self.capture["_completed_arrays"][label+"/T"] = T
                self.statistics["restored_grid_count"] += 1
                gevent.update(
                    status="complete",seconds=time.monotonic()-tick,
                    paid_array_hashes=copy.deepcopy(input_hashes[label]),
                    coefficient_context_hashes={
                        key:{name:array_digest(value) for name,value in part.items()}
                        for key,part in frame.items()},
                    paid_U_T_or_e_f_recalculated=False,
                    original_full_theta_retained=True,
                    scalar_grid_fields_calls=1,first_variation_frame_builds=1,
                    ordinary_geometry_calls=0,old_J_calls=0,
                    metric_or_height_jets_calls=0,periodic_primitive_calls=0)
                self.ledger.check()
            except Exception as error:
                gevent.update(status="raised",seconds=time.monotonic()-tick,error=self._error(error))
                raise
        original_value_binding = {
            "field":self.model_binding["ordinary_field_evaluation_sha256"],
            "factorization":self.model_binding["original_factorization_definition_sha256"],
            "state":array_digest(self.state),"grids":self._grid_binding}
        require(digest(original_value_binding) == self.model_binding["original_complete_value_binding_sha256"],
                "the complete original field/grid/theta value binding changed")
        self.phi0 = max(self.target,*(float(np.max(self.base[label]["branches"][group]["phi"]))
                       for label in LABELS for group in (0,1)))
        require(self.phi0 == float(model["complete_original_phi0"])
                == float(self.source_input_binding["paid_phi0"]),
                "paid complete branch maximum changed")
        expected = {
            "source_model_binding_sha256":self.model_binding_sha256,
            "physical_state_sha256":SOURCE_PHYSICAL,
            "state159_sha256":array_digest(self.state),
            "reference163_sha256":array_digest(self.reference163),
            "configuration_sha256":self.cfg_sha256,
            "original_complete_value_binding_sha256":digest(original_value_binding),
            "epsilon":self.epsilon,"constant_target":self.target,
            "physical_norm_cost_mu":self.mu}
        require(all(self.source_input_binding.get(k)==v for k,v in expected.items()),
                "paid input binding metadata differs from its source MODEL")
        self._input_hashes = input_hashes


    def _row_key(self, label, flat, tag=None):
        require(label in LABELS and type(flat) is int
                and 0 <= flat < 2*self.grids[label].point_count,
                "literal original metric grid and integer row ID required")
        expected = self.grids[label].coordinate(flat)
        if tag is not None:
            require(isinstance(tag, dict)
                    and all(tag.get(k) == v for k,v in expected.items()),
                    "original radial/theta/group row tag changed")
        return label, flat

    def _put_known(self, label, flat, gradient, base_phi, tag, provenance,
                   *, gradient_sha256=None, de=None, df=None):
        key = self._row_key(label, flat, tag)
        grid, d = self.grids[label], self.base[label]
        group, point = divmod(flat, grid.point_count)
        g = readonly(finite(gradient, (N,), "paid original gradient159"))
        sha = array_digest(g)
        require(gradient_sha256 is None or sha == gradient_sha256,
                "paid original gradient fingerprint changed")
        paid_phi = float(base_phi)
        full_phi = float(d["branches"][group]["phi"][point])
        limit = self.replay_relative_tolerance*max(1.,abs(paid_phi),abs(full_phi))
        require(np.isfinite(paid_phi) and abs(paid_phi-full_phi) <= limit,
                "paid selected margin and complete same-center phi disagree")
        self.statistics["maximum_paid_margin_to_full_phi_error"] = max(
            self.statistics["maximum_paid_margin_to_full_phi_error"], abs(paid_phi-full_phi))
        if key in self.known_gradients:
            result = self.known_gradients[key]
            require(np.array_equal(result["gradient159"],g)
                    and abs(result["base_phi"]-paid_phi) <= limit,
                    "duplicate paid original rows disagree")
            result["provenance"].append(copy.deepcopy(provenance))
        else:
            result = {
                "schema": POLICY+"-reused-original-gradient",
                "grid":label, "flat_row_id":flat, "group":group, "point":point,
                "original_row":copy.deepcopy(tag),
                "base_e":float(d["e"][point]), "base_f":float(d["f"][point]),
                "base_phi":paid_phi, "complete_base_phi":full_phi,
                "gradient159":g, "gradient_sha256":sha,
                "provenance":[copy.deepcopy(provenance)],
                "source":"already-paid-source-gradient",
                "new_gradient_evaluation":False,
                "ordinary_geometry_calls":0, "old_selected_J_calls":0}
            self.known_gradients[key] = result
        require((de is None) == (df is None), "de159 and df159 must be provided together")
        if de is not None:
            de = readonly(finite(de, (N,), "paid original de159"))
            df = readonly(finite(df, (N,), "paid original df159"))
            point_key = (label,point)
            if point_key in self.point_gradients:
                prior = self.point_gradients[point_key]
                require(np.array_equal(prior["de"],de) and np.array_equal(prior["df"],df),
                        "paid de/df for one original point disagree")
            else:
                self.point_gradients[point_key] = {
                    "de":de, "df":df, "source":"paid-original-attainer-record"}
            result["de159"], result["df159"] = de,df
        self.paid_rows.add(key)
        return result

    def _install_known_gradients(self, model, supplied, cache):
        domain = model["original_domain"]
        tags = domain["selected_metric_original_row_tags"]
        require(isinstance(tags,list) and len(tags) == 5743,
                "all 5743 original selected metric row tags are required")
        gradients = paid_array(domain["selected_metric_gradients_of_phi"],
                               (5743,N), "paid selected metric J")
        margins = paid_array(domain["selected_metric_base_margins"],
                             (5743,), "paid selected metric margins")
        selected_keys = []
        for i,tag in enumerate(tags):
            if i % 256 == 0:
                self.ledger.check()
            key = self._row_key(tag["grid"],tag["flat_row_id"],tag)
            require(key not in self.known_gradients, "duplicate original selected metric row")
            selected_keys.append(key)
            self._put_known(
                key[0],key[1],gradients[i],self.target-float(margins[i]),tag,
                {"source_model_binding_sha256":self.model_binding_sha256,
                 "path":"original_domain.selected_metric_gradients_of_phi",
                 "position":i,
                 "matrix_sha256":domain["selected_metric_gradients_of_phi"]["array_sha256"],
                 "base_margin_sha256":domain["selected_metric_base_margins"]["array_sha256"]})
        extra = model["additional_metric_gradients_not_already_in_selected_J"]
        require(isinstance(extra,list) and len(extra) == 5,
                "all five previously added original gradients are required")
        extra_keys = []
        for i,row in enumerate(extra):
            tag = row["original_row"]
            key = self._row_key(row["grid"],row["flat_row_id"],tag)
            require(key not in self.known_gradients,
                    "a paid additional row duplicates the original selected table")
            extra_keys.append(key)
            g = paid_array(row["unscaled_physical159_gradient"], (N,),
                           "paid additional original gradient")
            self._put_known(
                key[0],key[1],g,self.phi0-float(row["base_gap"]),tag,
                {"source_model_binding_sha256":self.model_binding_sha256,
                 "path":"additional_metric_gradients_not_already_in_selected_J",
                 "position":i,"source":row.get("source")},
                gradient_sha256=row["gradient_sha256"])
        require(isinstance(supplied,(list,tuple)), "original four paid attainer records required")
        four_keys = []
        for row in supplied:
            require(isinstance(row,dict)
                    and row.get("binding_sha256") == SOURCE_INPUT_BINDING,
                    "a paid gradient must retain its original first-jet binding")
            key = self._row_key(row["grid"],row["flat_row_id"],row["original_row"])
            require(key in REQUIRED_NEW_PAID_ROWS and key not in four_keys,
                    "exactly the four paid new positive-direction cuts are required")
            four_keys.append(key)
            d = self.base[key[0]]
            group,point = divmod(key[1],self.grids[key[0]].point_count)
            require(row.get("group")==group and row.get("point")==point
                    and float(row["base_e"])==float(d["e"][point])
                    and float(row["base_f"])==float(d["f"][point]),
                    "the paid attainer base point or branch changed")
            original_cache_gradient = paid_array(
                cache["binary64_round_trip_arrays"]["gradient/"+key[0]+"/"+str(key[1])],
                (N,), "paid CACHE attainer gradient")
            original_record_gradient = _vector(row["gradient159"],"paid new gradient")
            require(np.array_equal(original_cache_gradient,original_record_gradient)
                    and array_digest(original_cache_gradient)==row["gradient_sha256"],
                    "paid CACHE and ATTAINER_GRADIENT differ")
            self._put_known(
                key[0],key[1],original_record_gradient,
                row["base_phi"],row["original_row"],
                {"source_input_binding_sha256":SOURCE_INPUT_BINDING,
                 "source_record":"ATTAINER_GRADIENT",
                 "source":row.get("source"),"source_identity":copy.deepcopy(SOURCE)},
                gradient_sha256=row["gradient_sha256"],
                de=_vector(row["de159"],"paid new de159"),
                df=_vector(row["df159"],"paid new df159"))
        require(set(four_keys)==REQUIRED_NEW_PAID_ROWS
                and len(self.known_gradients)==5743+5+4,
                "the new master must retain all old gradients and all four new cuts")
        required_from_pools = set()
        for label in LABELS:
            count = self.grids[label].point_count
            for flat in model["ordered_original_pool_ids"][label]:
                require(type(flat) is int and 0 <= flat < 11*count,
                        "source pool IDs must remain original literal integers")
                if flat < 2*count:
                    required_from_pools.add((label,flat))
        for row in model["installed_metric_rows"]:
            key = self._row_key(row["grid"],row["flat_row_id"],row["original_row"])
            required_from_pools.add(key)
            known = self.known_gradients.get(key)
            require(known is not None and known["gradient_sha256"]==row["gradient_sha256"],
                    "an installed source gradient is missing or differs")
        require(required_from_pools.issubset(self.known_gradients),
                "a source metric gradient would be silently dropped")
        self.known_gradient_sources = {
            "selected_count":len(selected_keys), "additional_MODEL_count":len(extra_keys),
            "new_paid_attainer_count":len(four_keys),
            "selected_order_sha256":digest(selected_keys),
            "additional_MODEL_order_sha256":digest(extra_keys),
            "new_paid_attainer_order":copy.deepcopy(four_keys),
            "all_four_required_cuts_available_before_any_new_master_call":True}
        self.capture["known_gradient_sources"] = copy.deepcopy(self.known_gradient_sources)

    def _finish_binding(self):
        manifest = [
            {"grid":key[0],"flat_row_id":key[1],
             "gradient_sha256":row["gradient_sha256"],"base_phi":row["base_phi"]}
            for key,row in self.known_gradients.items()]
        self.binding = {
            "schema":POLICY+"-paid-cache-restored-coefficients-binding",
            "source_input_binding_sha256":SOURCE_INPUT_BINDING,
            "source_model_binding_sha256":self.model_binding_sha256,
            "source_cache_JSON_plus_LF_bytes":SOURCE_CACHE_BYTES,
            "source_cache_JSON_plus_LF_sha256":SOURCE_CACHE_SHA256,
            "source_identity":copy.deepcopy(SOURCE),
            "physical_state_sha256":SOURCE_PHYSICAL,
            "state159_sha256":array_digest(self.state),
            "reference163_sha256":array_digest(self.reference163),
            "configuration_sha256":self.cfg_sha256,
            "original_field_evaluation_sha256":
                self.model_binding["ordinary_field_evaluation_sha256"],
            "original_factorization_definition_sha256":
                self.model_binding["original_factorization_definition_sha256"],
            "grids":copy.deepcopy(self._grid_binding),
            "paid_input_hashes":copy.deepcopy(self._input_hashes),
            "original_complete_value_binding_sha256":
                self.model_binding["original_complete_value_binding_sha256"],
            "first_variation_coefficient_hashes":{
                label:{key:{name:array_digest(value) for name,value in part.items()}
                       for key,part in self.base[label]["frame"].items()}
                for label in LABELS},
            "known_gradient_count":len(manifest),
            "known_gradient_ordered_manifest_sha256":digest(manifest),
            "epsilon":self.epsilon, "constant_target":self.target,
            "paid_phi0":self.phi0, "physical_norm_cost_mu":self.mu,
            "new_identity_not_old_first_jet_scope":True}
        self.binding_sha256 = digest(self.binding)
        for row in self.known_gradients.values():
            row["binding_sha256"] = self.binding_sha256
        self.capture["binding"] = copy.deepcopy(self.binding)
        self.capture["binding_sha256"] = self.binding_sha256

    def _register_paid_scan(self, scan, cache):
        require(isinstance(scan,dict)
                and scan.get("binding_sha256")==SOURCE_INPUT_BINDING
                and scan.get("source_model_binding_sha256")==SOURCE_MODEL_BINDING,
                "the original complete positive-direction FULL_GRID_SCAN is required")
        p = _vector(scan["actual_direction"],"paid complete direction")
        key = array_digest(p)
        require(scan.get("direction_sha256")==key,
                "original complete direction fingerprint changed")
        require(scan.get("coverage")=={label:self.grids[label].point_count for label in LABELS}
                and float(scan["base_phi"])==self.phi0
                and float(scan["target"])==self.target
                and float(scan["physical_norm_cost_mu"])==self.mu,
                "the paid scan's full grid/constant-branch scope changed")
        constant = scan["constant_target_branch"]
        require(constant.get("value")==self.target
                and constant.get("directional_slope")==0
                and constant.get("physical_gradient_is_zero") is True,
                "the original constant target branch must remain")
        arrays = {}
        payload = cache["binary64_round_trip_arrays"]
        hashes = scan["array_sha256"]
        for label in LABELS:
            self.ledger.check()
            d,grid = self.base[label],self.grids[label]
            de = paid_array(payload[key+"/"+label+"/de"],
                            (grid.point_count,),"paid "+label+"/de")
            df = paid_array(payload[key+"/"+label+"/df"],
                            (grid.point_count,),"paid "+label+"/df")
            arrays[label] = {"e":d["e"],"f":d["f"],"de":de,"df":df}
            require(all(hashes[label].get(name)==array_digest(value)
                        for name,value in arrays[label].items()),
                    "original paid directional coefficient fingerprint changed")
        branches = copy.deepcopy(scan["branches"])
        require(isinstance(branches,list) and len(branches)==4,
                "one original attainer for each complete branch is required")
        seen = set()
        for item in branches:
            label,flat = self._row_key(item["grid"],item["flat_row_id"],item["original_row"])
            grid,d = self.grids[label],self.base[label]
            group,point = divmod(flat,grid.point_count)
            require((label,group) not in seen
                    and item.get("group")==group and item.get("point")==point
                    and (label,flat) in REQUIRED_NEW_PAID_ROWS
                    and float(item["base_e"])==float(d["e"][point])
                    and float(item["base_f"])==float(d["f"][point])
                    and float(item["base_phi"])==float(d["branches"][group]["phi"][point]),
                    "original paid branch/attainer identity changed")
            seen.add((label,group))
            require(np.isfinite(item["directional_slope"])
                    and np.isfinite(item["linear_branch_value"]),
                    "finite original scan scalars required")
            item["paid_source_gradient_already_paid"] = item.get("gradient_already_paid")
            item["gradient_already_paid"] = True
        require(seen=={(label,group) for label in LABELS for group in (0,1)},
                "all four original spectral branches are required")
        maximum = max(self.target,*(float(x["linear_branch_value"]) for x in branches))
        require(float(scan["linear_maximum"])==maximum
                and float(scan["unpenalized_first_order_gain"])==self.phi0-maximum,
                "the paid maximum/constant branch metadata changed")
        result = {
            "schema":POLICY+"-reused-complete-first-jet",
            "binding_sha256":self.binding_sha256,
            "source_input_binding_sha256":SOURCE_INPUT_BINDING,
            "source_model_binding_sha256":self.model_binding_sha256,
            "direction":p,"direction_sha256":key,
            "phase":"already-paid-source-positive-direction",
            "source_phase":scan.get("phase"),"arrays":arrays,
            "branches":branches,"coverage":copy.deepcopy(scan["coverage"]),
            "base_phi":self.phi0,"target":self.target,
            "constant_target_branch":copy.deepcopy(constant),
            "physical_norm_cost_mu":self.mu,
            "linear_maximum":maximum,
            "unpenalized_first_order_gain":float(scan["unpenalized_first_order_gain"]),
            "paid_source_array_sha256":copy.deepcopy(hashes),
            "reused_paid_direction":True,"new_full_grid_JVP_calls":0,
            "ordinary_geometry_calls":0,
            "claim_is_only_complete_discrete_first_order":True}
        self.scans[key] = result
        self.paid_direction_sha256 = key
        self._last_scan_key = key
        self.capture["paid_scan_reuse"] = {
            "direction_sha256":key,"source_input_binding_sha256":SOURCE_INPUT_BINDING,
            "coverage":copy.deepcopy(result["coverage"]),
            "new_JVP_or_argmax_sweeps":0,
            "branches":[{"grid":x["grid"],"flat_row_id":x["flat_row_id"]}
                        for x in branches],
            "all_four_previously_new_cuts_already_installed_as_known":True}


    def scan(self, direction, *, phase):
        """One genuinely new two-grid first-order scan, or a paid cache hit.

        A new direction consumes one pair counter before its first grid starts.
        Even a partial/failed pair cannot automatically be retried.  The old
        paid direction is already in self.scans and never invokes this work.
        """
        self._assert_context()
        p = owned(finite(direction,(N,),"physical159 direction"))
        key = array_digest(p)
        if key in self.scans:
            require(np.array_equal(p,self.scans[key]["direction"]),
                    "physical direction fingerprint collision")
            self.statistics["direction_cache_hits"] += 1
            if key == self.paid_direction_sha256:
                self.statistics["paid_direction_cache_hits"] += 1
            self._last_scan_key = key
            return self.scans[key]
        require(key not in self.direction_attempts,
                "a failed direction remains charged and is not automatically replayed")
        require(len(self.direction_attempts) < MAX_DISTINCT_DIRECTIONS,
                "the 32 new two-grid direction limit is exhausted")
        require(isinstance(phase,str) and phase, "an explicit new-direction phase is required")
        event = self._begin(
            "pair_first_jet_jvps",phase=phase,direction_sha256=key,
            restored_input_binding_sha256=self.binding_sha256)
        self.direction_attempts[key] = event
        self.statistics["pair_first_jet_started"] += 1
        arrays,branches,coverage = {},[],{}
        self._last_attempt_key = key
        self._last_attempt_arrays = arrays
        self.capture["_last_direction_arrays"] = arrays
        self.capture["last_attempt_direction_sha256"] = key
        self.capture["_last_attempt_direction159"] = p
        tick = time.monotonic()
        try:
            for label in LABELS:
                self.ledger.check()
                start = time.monotonic()
                d,grid = self.base[label],self.grids[label]
                gevent = {"grid":label,"status":"started"}
                event.setdefault("grids",[]).append(gevent)
                try:
                    dT,dTs = direction_frame_jets(
                        self.families,d["scalar_grid"],d["fields"],d["frame"],p)
                    self.ledger.check()
                    # Complete original theta operator first, then original row
                    # ordering.  Keep the original two-addition null-height order.
                    dP0,dP1 = periodic_operator(dT,-1),periodic_operator(dTs,-1)
                    dU = d["a_s"][:,None,None]*dP0+d["a"][:,None,None]*dP1
                    dU[:,:,2] += (d["null"]@p[154:])[:,None]
                    de = readonly(finite(
                        (2*np.sum(d["U"]*dU,axis=2)).reshape(-1),
                        (grid.point_count,),label+"/new de"))
                    df = readonly(finite(
                        np.sum(d["T"]*dU+d["U"]*dT,axis=2).reshape(-1),
                        (grid.point_count,),label+"/new df"))
                    # The line/envelope consumer requires only these four
                    # scalars per point.  Do not retain direction3 tensors.
                    arrays[label] = {"e":d["e"],"f":d["f"],"de":de,"df":df}
                    for group in (0,1):
                        branch = d["branches"][group]
                        slopes = branch["ge"]*de+branch["gf"]*df
                        values = finite(branch["phi"]+slopes,(grid.point_count,),
                                        label+"/complete linear branch")
                        point = int(np.argmax(values))
                        branches.append(self._attainer(
                            label,group,point,values[point],slopes[point]))
                    coverage[label] = grid.point_count
                    self.statistics["completed_grid_JVPs"] += 1
                    gevent.update(
                        status="complete",seconds=time.monotonic()-start,
                        point_count=grid.point_count,
                        complete_original_theta_count=grid.nt,
                        complete_periodic_primitive_calls=2,
                        de_sha256=array_digest(de),df_sha256=array_digest(df),
                        dT_sha256=array_digest(dT),dTs_sha256=array_digest(dTs),
                        dU_sha256=array_digest(dU),
                        paid_U_T_or_e_f_recalculated=False,
                        full_grid_parameter_axis159_tensor_created=False,
                        direction3_tensors_retained=False)
                    del dT,dTs,dP0,dP1,dU
                    self.ledger.check()
                except Exception as error:
                    gevent.update(status="raised",seconds=time.monotonic()-start,
                                  error=self._error(error))
                    raise
            maximum = max(self.target,*(item["linear_branch_value"] for item in branches))
            result = {
                "schema":POLICY+"-complete-first-jet",
                "binding_sha256":self.binding_sha256,
                "source_input_binding_sha256":SOURCE_INPUT_BINDING,
                "source_model_binding_sha256":self.model_binding_sha256,
                "direction":p,"direction_sha256":key,"phase":phase,
                "arrays":arrays,"branches":branches,"coverage":coverage,
                "base_phi":self.phi0,"target":self.target,
                "constant_target_branch":{
                    "value":self.target,"directional_slope":0.0,
                    "physical_gradient_is_zero":True},
                "physical_norm_cost_mu":self.mu,
                "linear_maximum":float(maximum),
                "unpenalized_first_order_gain":float(self.phi0-maximum),
                "reused_paid_direction":False,"new_full_grid_JVP_calls":2,
                "ordinary_geometry_calls":0,
                "claim_is_only_complete_discrete_first_order":True}
            self.scans[key] = result
            self._last_scan_key = key
            self.statistics["pair_first_jet_completed"] += 1
            self._end(
                event,seconds=time.monotonic()-tick,
                coverage=copy.deepcopy(coverage),branches=copy.deepcopy(branches),
                linear_maximum=float(maximum),new_full_grid_JVP_calls=2,
                completed_array_hashes={
                    label:{name:array_digest(value) for name,value in row.items()}
                    for label,row in arrays.items()})
            return result
        except Exception as error:
            self.capture["last_direction_failure"] = self._error(error)
            self._end(
                event,error,seconds=time.monotonic()-tick,
                completed_coverage=copy.deepcopy(coverage),
                completed_array_hashes={
                    label:{name:array_digest(value) for name,value in row.items()}
                    for label,row in arrays.items()})
            raise

    def is_paid_row(self, label, flat_row_id):
        key = self._row_key(label,flat_row_id)
        return key in self.known_gradients or key in self.gradients

    def known_gradient(self, label, flat_row_id):
        """Read one existing paid row; no original J or new gradient charge."""
        self._assert_context()
        key = self._row_key(label,flat_row_id)
        result = self.known_gradients.get(key,self.gradients.get(key))
        require(result is not None,"the requested original gradient has not been paid")
        self.statistics["known_gradient_cache_hits"] += 1
        return result

    def attainer_gradient(self, label, flat_row_id, *, scan):
        """Reuse a known row, or pay for one new actual complete-grid argmax.

        The same point's paid de159/df159 can serve its other spectral branch.
        All selected-row work is first-order-only and uses the original full
        angle operators before selecting the one physical point.
        """
        self._assert_context()
        key = self._row_key(label,flat_row_id)
        require(isinstance(scan,dict)
                and scan.get("binding_sha256")==self.binding_sha256
                and self.scans.get(scan.get("direction_sha256")) is scan,
                "a completed same-center scan owned by this module is required")
        matches = [item for item in scan["branches"]
                   if item["grid"]==label and item["flat_row_id"]==flat_row_id]
        require(len(matches)==1,
                "only the original argmax row of a complete scan may be requested")
        item = matches[0]
        prior = self.known_gradients.get(key,self.gradients.get(key))
        if prior is not None:
            self._compare_gradient_direction(prior,scan,item)
            self.statistics["known_gradient_cache_hits"] += 1
            return prior
        require(key not in self.gradient_attempts,
                "a failed original row remains charged and is not automatically replayed")
        require(len(self.gradient_attempts) < MAX_NEW_ORIGINAL_ROWS,
                "the 128 genuinely new original row limit is exhausted")
        event = self._begin(
            "new_attainer_gradients",original_row=copy.deepcopy(item["original_row"]),
            direction_sha256=scan["direction_sha256"],
            restored_input_binding_sha256=self.binding_sha256)
        self.gradient_attempts[key] = event
        self.statistics["new_original_rows_started"] += 1
        tick = time.monotonic()
        try:
            grid,d = self.grids[label],self.base[label]
            group,point = divmod(flat_row_id,grid.point_count)
            radial_index,theta_index = divmod(point,grid.nt)
            point_key = (label,point)
            if point_key not in self.point_gradients:
                de,df = np.zeros(N),np.zeros(N)
                fields = _radial_slice(d["fields"],radial_index,grid.nr)
                frame = _radial_slice(d["frame"],radial_index,grid.nr)
                U = d["U"][radial_index:radial_index+1,theta_index]
                T = d["T"][radial_index:radial_index+1,theta_index]
                ri = np.array([0],dtype=np.int64)
                event["families"] = []
                for name,angular,angular_first,radial,start,stop in self.families._families(
                        d["scalar_grid"],grid.nr,grid.nt):
                    self.ledger.check()
                    family_tick = time.monotonic()
                    record = {
                        "name":name,"start":int(start),"stop":int(stop),"status":"started"}
                    event["families"].append(record)
                    try:
                        kernels = angular_kernels(
                            fields,frame,name,angular,angular_first,second=False)
                        local_de,local_df = _first_order_selected_rows(
                            kernels,U,T,d["a"][radial_index],
                            d["a_s"][radial_index],theta_index)
                        radial_one = tuple(
                            value[radial_index:radial_index+1] for value in radial)
                        de[start:stop] = expand_radial_rows(local_de,radial_one,ri)[0]
                        df[start:stop] = expand_radial_rows(local_df,radial_one,ri)[0]
                        record.update(
                            status="complete",seconds=time.monotonic()-family_tick,
                            full_original_angle_count=grid.nt,
                            virtual_parameter_columns=int(local_de.shape[1]),
                            complete_periodic_primitive_calls=2,
                            original_R_Rprime_only=True,
                            R_second_derivative_coefficient_is_structural_zero=True,
                            a_second_derivative_not_read_or_reconstructed=True,
                            ordinary_geometry_calls=0)
                        del kernels,local_de,local_df
                        self.ledger.check()
                    except Exception as error:
                        record.update(status="raised",seconds=time.monotonic()-family_tick,
                                      error=self._error(error))
                        raise
                C = d["null"][radial_index]
                de[154:] = 2*U[0,2]*C
                df[154:] = T[0,2]*C
                de = readonly(finite(de,(N,),"new original de159"))
                df = readonly(finite(df,(N,),"new original df159"))
                self.point_gradients[point_key] = {
                    "de":de,"df":df,"source":"new-first-order-point-gradient"}
                self.statistics["new_point_gradient_contractions"] += 1
                event["point_gradient_reused"] = False
            else:
                de,df = (self.point_gradients[point_key][name] for name in ("de","df"))
                self.statistics["point_gradient_reuses"] += 1
                event["point_gradient_reused"] = True
            ge = float(d["branches"][group]["ge"][point])
            gf = float(d["branches"][group]["gf"][point])
            gradient = readonly(finite(ge*de+gf*df,(N,),"new original branch gradient159"))
            result = {
                "schema":POLICY+"-new-original-attainer-gradient",
                "binding_sha256":self.binding_sha256,
                "grid":label,"flat_row_id":flat_row_id,"group":group,"point":point,
                "original_row":copy.deepcopy(item["original_row"]),
                "base_e":float(d["e"][point]),"base_f":float(d["f"][point]),
                "base_phi":float(d["branches"][group]["phi"][point]),
                "de159":de,"df159":df,"gradient159":gradient,
                "gradient_sha256":array_digest(gradient),
                "source":"new-first-variation-kernels-with-paid-U-T",
                "new_gradient_evaluation":True,
                "ordinary_geometry_calls":0,"old_selected_J_calls":0,
                "second_order_kernels":False}
            self.capture["_completed_arrays"][
                "gradient/"+label+"/"+str(flat_row_id)] = gradient
            result["evaluation_status"] = "computed-before-chain-rule-check"
            self.capture.setdefault("_raw_gradient_records",{})[key] = result
            self._compare_gradient_direction(result,scan,item)
            result["evaluation_status"] = "complete"
            self.gradients[key] = result
            self.paid_rows.add(key)
            self.statistics["new_original_rows_completed"] += 1
            self._end(
                event,seconds=time.monotonic()-tick,
                gradient_sha256=result["gradient_sha256"],
                de159_sha256=array_digest(de),df159_sha256=array_digest(df),
                original_chain_rule_comparison=copy.deepcopy(
                    result["last_direction_comparison"]))
            return result
        except Exception as error:
            self.capture["last_gradient_failure"] = self._error(error)
            self._end(event,error,seconds=time.monotonic()-tick)
            raise

    def _compare_gradient_direction(self, result, scan, item):
        direct = float(result["gradient159"]@scan["direction"])
        expected = float(item["directional_slope"])
        require(np.isfinite(direct) and np.isfinite(expected),
                "finite original gradient and complete JVP slopes required")
        error = abs(direct-expected)
        limit = self.replay_relative_tolerance*max(1.,abs(direct),abs(expected))
        result["last_direction_comparison"] = {
            "direction_sha256":scan["direction_sha256"],
            "selected_gradient_dot_physical_direction":direct,
            "already_computed_complete_JVP_slope":expected,
            "absolute_error":error,"original_relative_tolerance_limit":limit,
            "no_extra_JVP_or_geometry":True,"passed":error <= limit}
        self.statistics["maximum_gradient_dot_JVP_error"] = max(
            self.statistics["maximum_gradient_dot_JVP_error"],error)
        require(error <= limit,"original gradient and completed JVP disagree")


    def new_gradient_records(self):
        """All new computed row records, including a failed final comparison.

        Values remain native NumPy arrays for the one caller-owned plaintext
        serialization.  Old selected arrays are never duplicated here.
        """
        return list(self.capture.get("_raw_gradient_records",{}).values())

    def cache_arrays(self, *, direction_sha256=None, include_paid=False,
                     include_context=False, include_partial=False):
        """Expose one candidate's de/df, never all 32 directions for stdout.

        By default the most recently returned complete scan is selected.
        include_partial=True instead selects the last attempted direction and
        only its completed grids.  The source MODEL/CACHE already owns e/f,
        U/T, a/a_s/null; include_paid is an explicit opt-in for those arrays.
        No array is recomputed, encoded, written or printed by this method.
        """
        out = {}
        if include_partial:
            require(direction_sha256 is None
                    or direction_sha256==self._last_attempt_key,
                    "only the most recent partial direction is retained for export")
            key = self._last_attempt_key
            arrays = self._last_attempt_arrays
            direction = self.capture.get("_last_attempt_direction159")
        else:
            key = self._last_scan_key if direction_sha256 is None else direction_sha256
            scan = self.scans.get(key)
            require(scan is not None,"one completed paid or new scan is required for export")
            arrays,direction = scan["arrays"],scan["direction"]
        if key is not None and direction is not None:
            out["scan/"+key+"/direction"] = direction
            for label,row in arrays.items():
                for name in ("de","df"):
                    out["scan/"+key+"/"+label+"/"+name] = row[name]
        if include_paid:
            for name in ("state159","reference163","radial","null_density","reference_height_b"):
                value = self.capture.get("_completed_arrays",{}).get(name)
                if value is not None:
                    out[name] = value
            for label,d in self.base.items():
                for name in ("U","T","e","f","radial","theta","a","a_s","null"):
                    out["paid-base/"+label+"/"+name] = d[name]
        if include_context:
            for label,d in self.base.items():
                for name,parts in d["fields"].items():
                    if isinstance(parts,dict):
                        for derivative,value in parts.items():
                            if isinstance(value,np.ndarray):
                                out["new-context/"+label+"/fields/"+name+"/"+derivative] = value
                    elif isinstance(parts,np.ndarray):
                        out["new-context/"+label+"/fields/"+name] = parts
                for part,items in d["frame"].items():
                    for name,value in items.items():
                        out["new-context/"+label+"/frame/"+part+"/"+name] = value
        return out

    def cache_manifest(self, **options):
        return {key:_array_record(value) for key,value in self.cache_arrays(**options).items()}

    def report(self):
        """Small identity, started-cost, failed-direction and new-cut report.

        It is not the full cache.  The driver records new_gradient_records()
        once and cache_arrays() for its final selected candidate once.
        """
        rows = []
        for result in self.new_gradient_records():
            key = (result["grid"],result["flat_row_id"])
            rows.append({
                "grid":key[0],"flat_row_id":key[1],
                "original_row":copy.deepcopy(result["original_row"]),
                "gradient_sha256":result["gradient_sha256"],
                "de159_sha256":array_digest(result["de159"]),
                "df159_sha256":array_digest(result["df159"]),
                "base_phi":result["base_phi"],
                "status":result.get("evaluation_status"),
                "attempt":copy.deepcopy(self.gradient_attempts.get(key)),
                "last_direction_comparison":copy.deepcopy(
                    result.get("last_direction_comparison"))})
        scans = []
        for key,scan in self.scans.items():
            scans.append({
                "direction_sha256":key,"phase":scan["phase"],
                "reused_paid_direction":scan.get("reused_paid_direction",False),
                "coverage":copy.deepcopy(scan["coverage"]),
                "linear_maximum":scan["linear_maximum"],
                "unpenalized_first_order_gain":scan["unpenalized_first_order_gain"],
                "branches":copy.deepcopy(scan["branches"]),
                "array_sha256":{
                    label:{name:array_digest(value) for name,value in array.items()}
                    for label,array in scan["arrays"].items()}})
        return {
            "schema":POLICY+"-report","status":self.capture.get("status"),
            "binding":copy.deepcopy(getattr(self,"binding",None)),
            "binding_sha256":getattr(self,"binding_sha256",None),
            "source_receipt":copy.deepcopy(getattr(self,"source_receipt",None)),
            "known_gradient_sources":copy.deepcopy(
                getattr(self,"known_gradient_sources",None)),
            "known_original_gradient_count":len(self.known_gradients),
            "paid_scan_reuse":copy.deepcopy(self.capture.get("paid_scan_reuse")),
            "statistics":copy.deepcopy(self.statistics),
            "events":copy.deepcopy(self.events),
            "completed_scan_records_without_dense_direction_arrays":scans,
            "new_original_gradient_records_without_dense_rows":rows,
            "all_new_gradient_attempts":[
                {"grid":key[0],"flat_row_id":key[1],"event":copy.deepcopy(event)}
                for key,event in self.gradient_attempts.items()],
            "all_new_direction_attempts":[
                {"direction_sha256":key,"event":copy.deepcopy(event)}
                for key,event in self.direction_attempts.items()],
            "last_complete_direction_sha256":self._last_scan_key,
            "last_attempt_direction_sha256":self._last_attempt_key,
            "last_attempt_complete_grids":list(self._last_attempt_arrays),
            "limits":{
                "new_input_restores":1,"new_two_grid_directions":MAX_DISTINCT_DIRECTIONS,
                "new_original_attainer_gradients":MAX_NEW_ORIGINAL_ROWS},
            "paid_source_U_T_e_f_strictly_reused":True,
            "new_scalar_fields_and_first_variation_coefficients_only":True,
            "one_candidate_de_df_export_not_all_direction_arrays":True,
            "source_raw_cache_fingerprint_not_recomputed_by_serialization":True,
            "old_scope_constants_unchanged":True,
            "no_ordinary_geometry_or_old_J_evaluation_claim":True,
            "no_continuous_grid_certificate":True}
