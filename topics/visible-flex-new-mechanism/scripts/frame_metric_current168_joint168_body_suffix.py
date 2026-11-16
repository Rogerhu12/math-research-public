#!/usr/bin/env python3
"""One true58 joint168 original-body-pool / full-suffix nonlinear minimax.

Import-only. Every necessary new scalar/frame/primitive/selected-two-jet/J
operation is owned by the external public Actions scope. The closed full62
problem is not restarted. Exact independent rounding precedes the original
affine physical172 height map; no old true57 domain assertion is rewritten.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import resource
import time
import numpy as np

from frame_complete_body_extension168 import CompleteBody168Field, array_binding
from frame_complete_body_extension168_joint_selected import _context
from frame_height_null_coordinates import digest
from frame_metric_current168_ring17 import (
    LP_ROW_TOLERANCE, _require, _error, _wall, _bounds, _vector, _raw_numeric)
from frame_metric_current168_reflected_R1_ray import _raw_all_fields
from frame_metric_current168_fixed_ring_prefix102 import _finite, _same, _inward_float

POLICY = "true58-joint168-body-suffix-v1"
LABELS = ("coarse", "fine")
INDEPENDENT = 168
VARIABLES = 170
K_COLUMN, H_COLUMN = 168, 169
NORM_WEIGHT = 1.e-6
MAX_EVALUATIONS, MAX_BACKEND_EVALUATIONS = 480, 960
SOLVER_SECONDS = 1200.
SLSQP_OPTIONS = {"maxiter": 240, "ftol": 1.e-9, "disp": False}
TARGET_EXACT = "1000/61"
HMAX_EXACT = "18014398507545773/281474976710656"
INTERNAL_METRIC_MARGIN_EXACT = "1/100000000"
SUFFIX_LEFT_EXACT = "153/200"
POSITION_KEYS = ("Xs", "Xt", "Xss", "Xst", "Xtt")
ALL_POSITION_KEYS = ("X",)+POSITION_KEYS+("T",)
SCALAR_KEYS = ("value", "s", "ss", "theta")
ROW_NAMES = ("metric_plus", "metric_minus", "plus_trace", "plus_determinant", "minus_trace", "minus_determinant")
PRIMARY_PHYSICAL_ROWS = tuple(range(154))+(154,155,156,160,161)+tuple(range(163,172))
PRIMARY_SIGNS = (1,)*154+(-1,-1,-1,1,1)+(1,)*9

class JointBodySuffixLimit(RuntimeError):
    """A real new-scope stop; never an invented optimizer return."""

def definition():
    return {
        "schema": POLICY, "source_accepted_index": 58,
        "variables": 170, "backend_order": "z168,K,h",
        "independent_decode": "RN(Q(q58)+Q(z)/4), one exact sum then one RN per independent coordinate",
        "physical_decode": "original exact affine159-to163 map direct sum identity9, after independent RN",
        "all_original172_physical_box_and_norm_rows": True,
        "physical_nine_heights_not_separately_rounded": True,
        "linear_rows": 692, "body_pool_rows": {"coarse":4454,"fine":4549},
        "body_pool_versions": {"coarse":15,"fine":14},
        "all_eleven_original_body_groups_and_literal_order_retained": True,
        "suffix_rows": "all21 original s>=153/200, both complete384/768 angular grids",
        "suffix_nonlinear_rows":145152, "all_nonlinear_rows":154155,
        "all_constraint_rows":154847,
        "body_hard_curvature_cap_exact":"58", "suffix_K_interval_exact":[TARGET_EXACT,"58"],
        "objective":"K+1e-6*h", "maximum_h_exact":HMAX_EXACT,
        "hmax_semantics":"explicit retained finite scope limit, not claimed sufficient for full168 original box",
        "unique_initial_point":"actual58 z168=0,K58,h0",
        "internal_metric_budget":"RN(Q(original binary64 metric budget)-1/100000000)",
        "internal_metric_constraint_is_stricter_not_a_relaxed_acceptance":True,
        "final_unsmoothed_metric_gate":"original metric budget with no added tolerance",
        "final_internal_model_residual_gate":"original SLSQP ftol after fixed initial scales",
        "same_q_for_body_and_suffix":True,
        "all_original_G_and_unsquared_trace_determinant_PSD_rows":True,
        "normal_area_is_an_independent_domain_and_qualification_gate":True,
        "new_model_value_arithmetic":"paid q_R scalar fields plus complete actual coefficient changes; paid58 first jets and selected X plus original field increments",
        "same_mathematical_field_different_floating_grouping_from_canonical_actual":True,
        "closed_full62_arrays_or_callback_not_used_as_new_initial_state_or_free_input":True,
        "no_true57_oracle_or_old_seven_alpha_session_called":True,
        "original_full_ordinary_geometry_calls":0,
        "new_model_queries_are_scientific_work_not_original_actual_calls":True,
        "cache":"current actualq geometry and K-independent derivative inputs; current q+K finalJ; initial/last binding references; zero disk",
        "residual_cache":"one current complete backend170 input, not an archive of480/960 large vectors",
        "evicted_revisits":"actual repeated work is recharged; distinct-q count separately retained",
        "maximum_distinct_new_actual_q168":MAX_EVALUATIONS,
        "maximum_distinct_backend170":MAX_BACKEND_EVALUATIONS,
        "solver_seconds":SOLVER_SECONDS, "options":copy.deepcopy(SLSQP_OPTIONS),
        "external_after_qualification":"one original canonical wholebody prediction, at most one actual pair with all14 unchanged",
        "no_continuous_reach_embedded_or_main_completion_claim":True}

def implementation_hashes():
    names=(Path(__file__).name,
        "frame_metric_current168_joint168_body_suffix_geometry.py",
        "frame_metric_current168_joint168_body_suffix_solver.py",
        "frame_complete_body_extension168.py",
        "frame_complete_body_extension168_joint_selected.py",
        "frame_complete_body_extension168_selected_cache.py",
        "frame_complete_body_extension168_curvature_prediction.py",
        "frame_selected_row_radial_jacobian.py",
        "frame_entry_single_q.py","frame_entry_paired_repair.py",
        "frame_height_null_coordinates.py","frame_direct_reference_geometry159.py",
        "frame_metric_spectral_recovery.py","frame_curvature_mixed_grid_steps.py",
        "frame_curvature_psd.py","frame_collar_bvp.py")
    return {name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in names}

def _public(value):
    return {key: copy.deepcopy(item) for key, item in value.items() if not str(key).startswith("_")}


def _array_receipt(value):
    """Only call on an array that was actually filled by completed work."""
    a = np.asarray(value)
    return {**array_binding(a), "values_in_this_record": False,
        "hash_is_not_a_future_free_scientific_input": True}


def _compact(value):
    """Compact already-computed data; no scientific reconstruction or truncation."""
    if isinstance(value, np.ndarray):
        return _array_receipt(value)
    if isinstance(value, np.generic):
        return _compact(value.item())
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): _compact(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_compact(v) for v in value]
    if isinstance(value, float) and not math.isfinite(value):
        return {"original_nonfinite_float": repr(value)}
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError("unsupported compact retained object: "+type(value).__name__)


def _paid_array(value, shape, name, *, integer=False):
    _require(isinstance(value, dict) and "values" in value, "complete paid array missing: "+name)
    dtype = np.dtype(value.get("dtype"))
    _require((dtype.kind in "iu") if integer else (dtype.kind == "f" and dtype.itemsize == 8),
             "paid array dtype mismatch: "+name)
    a = np.asarray(value["values"], dtype=dtype)
    _require(a.shape == tuple(shape) and np.all(np.isfinite(a)), "paid array shape/finite mismatch: "+name)
    _require(all(value.get(k) == v for k, v in array_binding(a).items()), "paid array hash mismatch: "+name)
    if "exact_binary64" in value:
        _require(a.ndim == 1 and value["exact_binary64"] == [str(Q.from_float(float(x))) for x in a],
                 "paid exact binary64 vector mismatch: "+name)
    a = a.copy(); a.setflags(write=False)
    return a


class _Trace:
    def __init__(self, wall, sink):
        self.wall, self.sink = wall, sink
        self.events = sink.setdefault("component_events", [])
        self.counts = sink.setdefault("component_counts", {})

    def run(self, kind, operation, retain=None, **metadata):
        _wall(self.wall, POLICY+"."+kind+".before")
        count = self.counts.setdefault(kind, {"started": 0, "completed": 0, "failed": 0, "seconds": 0.})
        count["started"] += 1
        event = {"kind": kind, "ordinal": count["started"], "status": "started", **copy.deepcopy(metadata)}
        if len(self.events) >= 32:
            del self.events[0]
            self.sink["component_events_not_retained_in_bounded_history"] = self.sink.get(
                "component_events_not_retained_in_bounded_history", 0)+1
        self.events.append(event)
        self.sink["component_event_history_policy"] = {
            "last_completed_or_started_events_at_most":32,
            "all_calls_and_seconds_remain_in_component_counts":True,
            "every_value_and_J_request_keeps_its_complete_component_cost_delta":True}
        tick = time.monotonic()
        try:
            answer = operation()
            if retain is not None:
                retain(answer)
            event["status"] = "complete"; count["completed"] += 1
        except Exception as error:
            event.update(status="raised", error=_error(error)); count["failed"] += 1
            raise
        finally:
            event["seconds"] = time.monotonic()-tick
            count["seconds"] += event["seconds"]
            event["process_peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        _wall(self.wall, POLICY+"."+kind+".after")
        return answer


class _CurrentArrays:
    """Bounded current-q RAM cache; no scientific arrays are written to disk."""
    def __init__(self, wall, sink):
        self.wall, self.sink = wall, sink
        sink["temporary_cache"] = {"storage": "current-q RAM only", "writes": 0, "reads": 0,
            "bytes_written": 0, "io_seconds": 0., "cleanup_complete": False,
            "maximum_current_geometry_states": 1, "maximum_current_final_J": 1,
            "current_q_derivative_blocks_only": True,
            "initial_and_last_completed_arrays_retained_for_bindings_only": True,
            "only_current_complete_backend_value_vector": True,
            "evictions": {}, "process_peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
            "only_this_process": True, "uploaded_or_future_free": False}

    def evict(self, kind, count):
        if count:
            log = self.sink["temporary_cache"]["evictions"]
            log[kind] = log.get(kind, 0)+int(count)
        self.sink["temporary_cache"]["process_peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

    def close(self):
        self.sink["temporary_cache"]["cleanup_complete"] = True
        self.sink["temporary_cache"]["no_disk_cleanup_IO_was_needed"] = True
        self.sink["temporary_cache"]["process_peak_rss_kib"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)


def _curvature_differentials(data, a, values):
    """K-independent portion of the original curvature_parameter_jacobian chain."""
    scale = np.broadcast_to(np.asarray(a, dtype=float), values["q"].shape)
    _require(np.array_equal(scale, values["scale"]), "original curvature derivative scale changed")
    dA = data["jac_Xs"]
    dT = data["jac_Xt"]/scale[..., None, None]
    dU = data["jac_Xss"]
    dV = data["jac_Xst"]/scale[..., None, None]
    dW = data["jac_Xtt"]/scale[..., None, None]**2
    dot = lambda left, right: np.einsum("...c,...cn->...n", left, right)
    dw = np.moveaxis(np.cross(np.moveaxis(dA, -1, -2), values["T"][..., None, :])
        +np.cross(values["A"][..., None, :], np.moveaxis(dT, -1, -2)), -2, -1)
    return {"dq": dot(values["w"], dw)/values["q"][..., None],
        "dE": 2*dot(values["A"], dA),
        "dF": dot(values["T"], dA)+dot(values["A"], dT),
        "dG": 2*dot(values["T"], dT),
        "de": dot(values["U"], dw)+dot(values["w"], dU),
        "df": dot(values["V"], dw)+dot(values["w"], dV),
        "dk": dot(values["W"], dw)+dot(values["w"], dW)}


def _curvature_rows_from_differentials(values, differentials, K, scale):
    """Only new K-dependent row assembly; all physical differentials are cached."""
    d = differentials; tau = 1/K
    def pair(metric, derivative, second):
        base = d["dq"]*values[metric][:, None]+values["q"][:, None]*d[derivative]
        return np.stack((base+tau*d[second], base-tau*d[second]), axis=1)
    dh11, dh12, dh22 = pair("E", "dE", "de"), pair("F", "dF", "df"), pair("G", "dG", "dk")
    dtrace = dh11+dh22
    ddet = values["h22"][..., None]*dh11+values["h11"][..., None]*dh22-2*values["h12"][..., None]*dh12
    four = np.stack((dtrace[:, 0], ddet[:, 0], dtrace[:, 1], ddet[:, 1]), axis=1)
    factor = K/scale
    return four*np.asarray((factor, factor*factor, factor, factor*factor))[None, :, None]



def _linear_rows(P, base, lower, upper, hmax, target_lower):
    rows,rhs,tags=[],[],[]
    def add(coeff,k,h,bound,tag):
        rows.append(np.r_[coeff,float(k),float(h)]);rhs.append(float(bound));tags.append(tag)
    zero=np.zeros(168)
    for j in range(172):
        add(P[j],0,0,upper[j]-base[j],{"kind":"physical172_box","index":j,"side":"upper"})
        add(-P[j],0,0,base[j]-lower[j],{"kind":"physical172_box","index":j,"side":"lower"})
        _require(np.any(P[j]!=0.),"every original physical172 row has an actual full168 direction")
        add(4*P[j],0,-1,Q(0),{"kind":"norm","index":j,"side":"plus"})
        add(-4*P[j],0,-1,Q(0),{"kind":"norm","index":j,"side":"minus"})
    add(zero,-1,0,-target_lower,{"kind":"K_lower"})
    add(zero,1,0,Q(58),{"kind":"K_upper"})
    add(zero,0,-1,Q(0),{"kind":"h_lower"})
    add(zero,0,1,hmax,{"kind":"h_upper"})
    return _finite(np.stack(rows),(692,170),"full168 linear A"),_finite(rhs,(692,),"full168 linear b"),tags

def _original_box_backend_bounds(independent,physical,lower,upper):
    bounds,rows=[],[]
    for i,(j,sign) in enumerate(zip(PRIMARY_PHYSICAL_ROWS,PRIMARY_SIGNS)):
        offset=physical[j]-sign*independent[i]
        a,b=(lower[j]-offset)/sign,(upper[j]-offset)/sign
        lo,hi=min(a,b),max(a,b)
        qlo=Q.from_float(_inward_float(lo,True));qhi=Q.from_float(_inward_float(hi,False))
        _require(lo<=qlo<=independent[i]<=qhi<=hi,"accepted58 inside original anchor interval")
        zl,zu=4*(qlo-independent[i]),4*(qhi-independent[i])
        fl,fu=_inward_float(zl,True),_inward_float(zu,False)
        _require(zl<=Q.from_float(fl)<=0<=Q.from_float(fu)<=zu,"original inward z interval contains zero")
        bounds.append((fl,fu))
        rows.append({"backend_column":i,"physical_anchor":j,"anchor_sign":sign,
            "offset_exact":str(offset),"physical_interval_exact":[str(lower[j]),str(upper[j])],
            "inward_independent_exact_binary64":[str(qlo),str(qhi)],
            "backend_interval_binary64":[fl,fu]})
    return bounds,{"schema":POLICY+"-original-box-inward-anchors","rows":rows,
        "original_box_unchanged":True,"coupled_nonanchor_rows":[157,158,159,162],
        "remaining_coupled_rows_keep_linear_and_exact_terminal_gates":True,
        "no_claim_all_height_rows_are_protected_by_independent_bounds":True,
        "no_failed_return_is_clipped_or_repaired":True}

class Joint168BodySuffixModel:
    def __init__(self):
        self.status="not-built";self.solve_attempted=False;self.solver_sink=None
        self.row_scales=None;self.initial_entry=None;self.last_entry=None
        self.seen_geometry_keys=set();self.seen_J_keys=set();self.seen_derivative_keys=set()
        self.derivative_input_cache={}
        self.loaded_geometry=None;self.loaded_geometry_key=None
        self.loaded_J=None;self.loaded_J_key=None
        self.baseline_cache=None
        self.full_point_counts={"started":0,"completed":0,"failed":0,"cache_hits":0,
            "distinct_new_physical_points":0,"recomputed_after_eviction":0,
            "paid58_firstjet_and_selected_identity_hits":0,
            "original_full_ordinary_geometry_calls":0}
        self.jacobian_counts={"started":0,"completed":0,"failed":0,"cache_hits":0,
            "distinct_q_K_keys":0,"reassembled_after_eviction":0}
        self.derivative_input_counts={"started":0,"completed":0,"failed":0,"cache_hits":0,
            "distinct_input_keys":0,"recomputed_after_eviction":0}
        self.shared_counts={"baseline_frame_preparations":0,"baseline_primitive_calls":0,
            "wholebody_scalar_frame_queries":0,"wholebody_firstjet_queries":0,
            "selected_two_jet_queries":0,"suffix_two_jet_queries":0,
            "union_curvature_queries":0,"original_full_ordinary_geometry_calls":0,
            "original_actual_grid_calls":0}

    def assert_context(self):
        self.field._assert_context()
        _require(self.field.definition_sha256==self.binding["field_definition_sha256"]
            and self.field.coordinate_definition_sha256==self.binding["coordinate_definition_sha256"]
            and digest(self.cfg)==self.binding["configuration_sha256"],"original field/reference/cfg changed")
        _wall(self.wall,POLICY+".context")

    def point_from_backend(self,backend,*,include_record=False):
        x=_finite(backend,(170,),"literal backend170")
        z=tuple(Q.from_float(float(v)) for v in x[:168])
        ideal=tuple(q+v/4 for q,v in zip(self.accepted_independent_exact,z))
        q=np.asarray([float(v) for v in ideal],dtype=np.float64)
        _require(np.all(np.isfinite(q)),"finite once-rounded independent168")
        if not include_record:
            return q
        delta=tuple(sum(a*b for a,b in zip(row,z)) for row in self.exact_P)
        ideal_physical=tuple(a+b for a,b in zip(self.accepted_physical,delta))
        actual=tuple(self.field.full_coefficients(q,exact=True))
        rounded_delta=tuple(a-b for a,b in zip(actual,self.accepted_physical))
        bad0=[j for j,(a,v,b) in enumerate(zip(self.lower172,ideal_physical,self.upper172)) if not a<=v<=b]
        bad1=[j for j,(a,v,b) in enumerate(zip(self.lower172,actual,self.upper172)) if not a<=v<=b]
        K,h=Q.from_float(float(x[168])),Q.from_float(float(x[169]))
        norm,rounded_norm=4*max(map(abs,delta)),4*max(map(abs,rounded_delta))
        interval=self.target_exact<=K<=Q(58) and 0<=h<=self.maximum_h_exact
        record={"schema":POLICY+"-exact-once-rounded-candidate","model_binding_sha256":self.binding_sha256,
            "actual_backend_raw170":_vector(x),"backend_order":"z168,K,h",
            "literal_z168_exact_binary64":[str(v) for v in z],
            "unrounded_independent168_exact":[str(v) for v in ideal],
            "unrounded_physical172_exact":[str(v) for v in ideal_physical],
            "unrounded_physical172_increment_exact":[str(v) for v in delta],
            "rounded_independent168":_vector(q),"rounded_physical172_exact":[str(v) for v in actual],
            "rounding_difference_independent168_exact":[str(Q.from_float(float(a))-b) for a,b in zip(q,ideal)],
            "physical_increment_from_accepted58_exact":[str(v) for v in rounded_delta],
            "unrounded_original172_box_pass":not bad0,"rounded_original172_box_pass":not bad1,
            "unrounded_box_violating_indices":bad0,"rounded_box_violating_indices":bad1,
            "original_exact_box_pass":bool(not bad0 and not bad1),
            "K_exact":str(K),"h_exact":str(h),"K_h_exact_interval_pass":bool(interval),
            "unrounded_exact_physical_norm":str(norm),"rounded_exact_physical_norm":str(rounded_norm),
            "backend_norm_epigraph_exact_pass":bool(norm<=h),"backend_h_minus_exact_norm":str(h-norm),
            "rounded_physical_norm_le_raw_h_exact_pass":bool(rounded_norm<=h),
            "raw_h_minus_rounded_physical_norm_exact":str(h-rounded_norm),
            "raw_h_is_never_repaired_after_return":True,
            "explicit_retained_hmax_pass":bool(norm<=self.maximum_h_exact and rounded_norm<=self.maximum_h_exact),
            "original_box_and_K_h_pass":bool(interval and not bad0 and not bad1
                and norm<=self.maximum_h_exact and rounded_norm<=self.maximum_h_exact),
            "unrounded_backend_norm_rows_use_original_linear_tolerance":True,
            "rounded_physical_norm_to_raw_h_is_a_separate_exact_qualification_gate":True,
            "original_complete_H9x5_used_after_independent_rounding":True,
            "physical_heights_were_not_separately_rounded":True,
            "all168_controls_available_with_original_zero_supports_only":True,
            "same_fixed_g_permanent_c0_b0_and_original_total_height":True,
            "physical_state_sha256":digest(self.field.identity(q)),
            "original_actual58_physical_state_sha256":self.binding["accepted_physical_state_sha256"],
            "original_canonical_prediction_and_actual14_not_yet_evaluated":True}
        return q,record

    def _geometry(self,q,sink):
        from frame_metric_current168_joint168_body_suffix_geometry import evaluate_geometry
        return evaluate_geometry(self,q,sink)

    def _value(self,backend,sink,*,state168=None):
        from frame_metric_current168_joint168_body_suffix_geometry import evaluate_value
        return evaluate_value(self,backend,sink,state168=state168)

    def _jacobian(self,entry,sink):
        from frame_metric_current168_joint168_body_suffix_geometry import assemble_jacobian
        return assemble_jacobian(self,entry,sink)

    def summary(self):
        return {"schema":POLICY+"-model-summary","status":self.status,"binding_sha256":self.binding_sha256,
            "variables":170,"independent_controls":168,"linear_rows":692,
            "constraint_count":self.constraint_count,"nonlinear_constraint_count":self.nonlinear_constraint_count,
            "body_pool_rows":{k:len(v) for k,v in self.pools.items()},"body_pool_versions":copy.deepcopy(self.pool_versions),
            "suffix_radial_ids":self.suffix_ids.tolist(),"suffix_radial_count":len(self.suffix_ids),
            "theta_counts":{k:len(v) for k,v in self.thetas.items()},
            "initial_backend_seed170":_vector(self.x0),"metric_budget":self.metric_budget,
            "internal_metric_budget":self.internal_metric_budget,"internal_metric_margin_exact":INTERNAL_METRIC_MARGIN_EXACT,
            "final_unsmoothed_comparison_uses_original_metric_budget_without_added_tolerance":True,
            "maximum_h_exact":str(self.maximum_h_exact),
            "hmax_is_explicit_retained_scope_limit_not_full168_box_sufficient":True,
            "K_interval_exact":[str(self.target_exact),"58"],"backend_K_lower_binary64":self.target_lower,
            "backend_K_lower_exact_binary64":str(Q.from_float(self.target_lower)),
            "new_geometry_counts":copy.deepcopy(self.full_point_counts),"new_J_counts":copy.deepcopy(self.jacobian_counts),
            "K_independent_derivative_input_counts":copy.deepcopy(self.derivative_input_counts),
            "shared_component_scientific_counts":copy.deepcopy(self.shared_counts),
            "original_full_ordinary_geometry_calls":self.shared_counts["original_full_ordinary_geometry_calls"],
            "original_actual_calls_are_not_new_model_query_counts":True,
            "same_q_and_same_complete_field_for_body_and_suffix":True,
            "same_mathematical_field_different_increment_floating_grouping":True,
            "qualified_return_only_authorizes_external_original_prediction":True,
            "actual14_and_reach_not_claimed":True,
            "initial_summaries":None if self.initial_entry is None else copy.deepcopy(self.initial_entry["summaries"]),
            "last_summaries":None if self.last_entry is None else copy.deepcopy(self.last_entry["summaries"])}

    def full_record(self):
        return {"schema":POLICY+"-full-model","definition":definition(),"summary":self.summary(),
            "binding":copy.deepcopy(self.binding),"binding_sha256":self.binding_sha256,
            "build_receipt":_compact(_public(self.build_sink)),
            "accepted_state168":_vector(self.accepted_state168),
            "q_R_used_only_as_paid_scalar_source":_vector(self.ring_candidate168),
            "exact_physical_injection":copy.deepcopy(self.coordinate_record),
            "original_lower172_exact":[str(v) for v in self.lower172],
            "original_upper172_exact":[str(v) for v in self.upper172],
            "backend_original_box_bounds":copy.deepcopy(self.backend_bound_receipt),
            "prepared_shared_input_receipt":copy.deepcopy(self.input_receipt),
            "new_linear_A_binding":_array_receipt(self.linear_A),
            "new_linear_b_binding":_array_receipt(self.linear_b),
            "linear_row_tags":copy.deepcopy(self.linear_tags),
            "large_arrays_not_output_or_future_free":True,
            "old_complete_paid_payloads_referenced_not_duplicated":True}

def build_joint168_body_suffix_model(
        prepared,completed,first_jet_bounds,metric_bound,wall,capture=None,*,
        metric_budget,internal_metric_budget,charge_prepare):
    """Bind actual58 inputs and pay one preparation for this genuinely new domain."""
    sink={} if capture is None else capture
    _require(isinstance(sink,dict) and not sink,"empty joint168 build capture required")
    _require(callable(wall) and callable(charge_prepare),"one external wall/prepare owner")
    sink.update(schema=POLICY+"-build-capture",status="entered")
    model=Joint168BodySuffixModel();sink["_object_model"]=model
    model.wall,model.build_sink=wall,sink
    tick=time.monotonic()
    try:
        _wall(wall,POLICY+".build.entry")
        field=prepared["field168"];_context(field)
        _require(isinstance(field,CompleteBody168Field) and field.metric_free==0,"same fixed-g complete168")
        model.field=field;model.cfg=copy.deepcopy(prepared["cfg"])
        model.source_receipt=copy.deepcopy(completed["receipt"])
        model.accepted_state168=_finite(field.validate_state(prepared["q168"]),(168,),"actual58 q168")
        _require(prepared["source_binding"]["accepted_index"]==58
            and _same(model.accepted_state168,_finite(completed["state168"],(168,),"source58")),
            "one unchanged actual58 independent state")
        model.ring_candidate168=_finite(completed["unaccepted_ring_state168"],(168,),"paid q_R")
        model.accepted_independent_exact=tuple(Q.from_float(float(v)) for v in model.accepted_state168)
        model.accepted_physical=tuple(field.full_coefficients(model.accepted_state168,exact=True))
        model.lower172,model.upper172=_bounds(prepared["lower172"],"lower"),_bounds(prepared["upper172"],"upper")
        _require(all(a<=v<=b for a,v,b in zip(model.lower172,model.accepted_physical,model.upper172)),"actual58 original exact box")
        model.metric_budget=float(metric_budget);model.internal_metric_budget=float(internal_metric_budget)
        _require(math.isfinite(model.metric_budget) and model.metric_budget>0
            and model.internal_metric_budget==float(Q.from_float(model.metric_budget)-Q(INTERNAL_METRIC_MARGIN_EXACT))
            and 0<model.internal_metric_budget<model.metric_budget,"literal stricter internal metric target")
        prefix=completed["paid_prefix_model"];free=completed["paid_free_model"]
        _require(_same(_paid_array(free["original_actual58_state168"],(168,),"free source q58"),model.accepted_state168)
            and _same(_paid_array(prefix["accepted_state168"],(168,),"prefix q58"),model.accepted_state168)
            and _same(_paid_array(prefix["unaccepted_ring_seed168"],(168,),"prefix q_R"),model.ring_candidate168),
            "paid scalar states must agree with the actual58 and q_R inputs")
        _require([str(v) for v in model.lower172]==prefix["lower172_exact"]
            and [str(v) for v in model.upper172]==prefix["upper172_exact"]
            and [str(v) for v in model.accepted_physical]==free["original_actual58_physical172_exact"],
            "original exact172 box and accepted physical state changed")
        _require(digest(model.cfg)==prefix["binding"]["configuration_sha256"],
            "paid source original configuration changed")
        _require(Q.from_float(model.metric_budget)==Q(prefix["binding"]["metric_budget_exact_binary64"]),"original metric budget changed")
        model.target_exact=Q(TARGET_EXACT);model.target_lower=_inward_float(model.target_exact,True)
        _require(model.target_exact==Q(free["binding"]["curvature_lower_target_exact"]),"original K target changed")
        model.maximum_h_exact=Q(free["binding"]["original_box_sufficient_hmax_exact"])
        _require(model.maximum_h_exact==Q(HMAX_EXACT),"same explicit retained finite h cap")
        model.maximum_h_float=_inward_float(model.maximum_h_exact,False)
        model.cap=float(Q(model.cfg["fixed_hard_curvature_cap_exact"]))
        model.curvature_scale=float(Q(model.cfg["curvature_scale_exact"]))
        model.area_floor=float(model.cfg["normal_area_numerical_floor"])
        model.curvature_row_tolerance=float(model.cfg["curvature_row_tolerance"])
        model.direct_curvature_tolerance=float(model.cfg["direct_curvature_tolerance"])
        model.epsilon=float(Q(model.cfg["metric_proposal_epsilon_exact"]))
        _require(model.cap==58. and model.curvature_scale>0 and model.epsilon>0,"original curvature/epsilon retained")
        model.side=int(prepared["gate"].side)
        _require(model.side in (-1,1),"original physical side")
        sink["prepare_charge_receipt"]=copy.deepcopy(charge_prepare({
            "schema":POLICY+"-prepare-charge","new_exact_P172x168":1,"new_linear_rows":692,
            "new_original_full168_anchor_bounds":1,
            "new_last3_radial_basis_and_Q_angular":True,
            "new_body_and_complete_null_height_basis":True,
            "old_true57_oracle_or_solver_calls":0,"original_full_ordinary_geometry_calls":0,
            "new_model_value_and_J_calls_have_separate_actual_counters":True}))
        M=tuple(tuple(Q(v) for v in row) for row in prepared["physical_map_exact172x168"])
        _require(len(M)==172 and all(len(row)==168 for row in M),"complete exact172x168 affine map")
        H=field.original_field.coordinates.basis.H
        for i,row in enumerate(M):
            for j,value in enumerate(row):
                expected=(Q(int(i==j)) if i<154 else
                    Q(H[i-154][j-154]) if 154<=i<163 and 154<=j<159 else
                    Q(int(i-163==j-159)) if i>=163 and j>=159 else Q(0))
                _require(value==expected,"original complete exact affine map changed")
        model.exact_P=tuple(tuple(v/4 for v in row) for row in M)
        model.P=np.asarray([[float(v) for v in row] for row in model.exact_P],dtype=np.float64)
        model.coordinate_record={"schema":POLICY+"-complete-exact-injection",
            "independent_scale_exact":"1/4","shape":[172,168],
            "original_H9x5_exact":[[str(v) for v in row] for row in H],
            "exact_P_sha256":digest([[str(v) for v in row] for row in model.exact_P]),
            "all172_norm_rows_nonzero":True,
            "physical_decode_after_independent_RN":True,
            "new_all168_domain_not_closed62_continuation":True}
        trace=_Trace(wall,sink)
        model.linear_A,model.linear_b,model.linear_tags=trace.run("new_full168_linear_rows",
            lambda:_linear_rows(model.P,model.accepted_physical,model.lower172,model.upper172,
                model.maximum_h_exact,model.target_lower),
            lambda v:sink.__setitem__("_new_linear_arrays",{"A":v[0],"b":v[1]}))
        model.backend_z_bounds,model.backend_bound_receipt=trace.run("new_full168_original_anchor_bounds",
            lambda:_original_box_backend_bounds(model.accepted_independent_exact,model.accepted_physical,
                model.lower172,model.upper172),
            lambda v:sink.__setitem__("_new_backend_bounds",v[1]))
        from frame_metric_current168_joint168_body_suffix_geometry import prepare_geometry
        prepare_geometry(model,prepared,completed,first_jet_bounds,metric_bound,trace)
        model.x0=_finite(np.r_[np.zeros(168),58.,0.],(170,),"unique true58 backend170")
        model.nonlinear_constraint_count=154155;model.constraint_count=154847
        model.binding={"schema":POLICY+"-binding","definition":definition(),
            "source_receipt":model.source_receipt,"configuration_sha256":digest(model.cfg),
            "field_definition_sha256":field.definition_sha256,
            "coordinate_definition_sha256":field.coordinate_definition_sha256,
            "accepted_state168":array_binding(model.accepted_state168),
            "accepted_physical_state_sha256":digest(field.identity(model.accepted_state168)),
            "paid_q_R168":array_binding(model.ring_candidate168),
            "physical_injection":copy.deepcopy(model.coordinate_record),
            "original_lower172_exact":[str(v) for v in model.lower172],
            "original_upper172_exact":[str(v) for v in model.upper172],
            "initial_backend170":_vector(model.x0),"new_linear_A":array_binding(model.linear_A),
            "new_linear_b":array_binding(model.linear_b),
            "metric_budget_exact_binary64":str(Q.from_float(model.metric_budget)),
            "internal_metric_budget_exact_binary64":str(Q.from_float(model.internal_metric_budget)),
            "internal_metric_margin_exact":INTERNAL_METRIC_MARGIN_EXACT,
            "original_box_backend_bounds":model.backend_bound_receipt,
            "K_lower_exact":str(model.target_exact),"K_lower_binary64":model.target_lower,
            "maximum_h_exact":str(model.maximum_h_exact),
            "maximum_h_inward_binary64":model.maximum_h_float,
            "hmax_semantics":"explicit finite scope limit, not full168 box-sufficient",
            "prepared_shared_input_receipt":copy.deepcopy(model.input_receipt),
            "same_mathematical_field_different_increment_floating_grouping":True,
            "original_canonical_prediction_and_actual14_external":True,
            "implementation_hashes":implementation_hashes()}
        model.binding_sha256=digest(model.binding)
        _require(_same(model.point_from_backend(model.x0),model.accepted_state168),"literal zero increment must recover actual58")
        model.temporary=_CurrentArrays(wall,sink);model.status="ready"
        sink.update(status="complete",binding=copy.deepcopy(model.binding),model_binding_sha256=model.binding_sha256,
            original_full_ordinary_geometry_calls=0,closed_full62_arrays_or_callback_consumed=False)
        _wall(wall,POLICY+".build.complete")
        return model
    except Exception as error:
        sink.update(status="raised",error=_error(error));model.status="build-raised"
        raise
    finally:
        sink["local_elapsed_seconds"]=time.monotonic()-tick

def solve_joint168_body_suffix_once(model,*,wall,charge_solve,emit=None,capture=None,
        solver_seconds=SOLVER_SECONDS,maxiter=240,max_evaluations=MAX_EVALUATIONS,
        max_backend_evaluations=MAX_BACKEND_EVALUATIONS):
    from frame_metric_current168_joint168_body_suffix_solver import solve_joint168_body_suffix_once as run_once
    return run_once(model,wall=wall,charge_solve=charge_solve,emit=emit,capture=capture,
        solver_seconds=solver_seconds,maxiter=maxiter,max_evaluations=max_evaluations,
        max_backend_evaluations=max_backend_evaluations)

def joint168_body_suffix_capture_record(capture,*,include_arrays=False):
    from frame_metric_current168_joint168_body_suffix_solver import joint168_body_suffix_capture_record as record
    return record(capture,include_arrays=include_arrays)
