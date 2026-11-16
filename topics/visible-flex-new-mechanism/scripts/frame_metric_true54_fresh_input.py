#!/usr/bin/env python3
"""Assemble the same original finite model from the genuinely new54 derivatives."""
from __future__ import annotations
import copy
from fractions import Fraction
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_true54_fresh_scope import POLICY,require,SOURCE_PHYSICAL_SHA
def array(record, shape=None):
    require(isinstance(record, dict) and record.get("dtype") == "float64"
            and isinstance(record.get("values"), list), "one original float64 payload required")
    a = np.asarray(record["values"], dtype=np.float64)
    require(list(a.shape) == record["shape"] and np.all(np.isfinite(a))
            and array_digest(a) == record["array_sha256"], "original numeric array changed")
    if shape is not None:
        require(a.shape == shape, "original array shape changed")
    return a


def vector_record(value):
    a = np.asarray(value, dtype=np.float64)
    require(a.ndim == 1 and np.all(np.isfinite(a)), "one finite actual vector required")
    return {"binary64": a.tolist(),
            "exact_binary64": [str(Fraction.from_float(float(v))) for v in a],
            "array_sha256": array_digest(a), "length": len(a)}


def assemble_fresh_master(model, ledger):
    ledger.check()
    require(digest(model["binding"]) == model["binding_sha256"]
            and model["binding"]["physical_state_sha256"] == SOURCE_PHYSICAL_SHA,
            "one complete newly built54 source model required")
    source_binding=model["binding_sha256"]
    dom = model["original_domain"]
    state = array(model["source_current_independent159"], (159,))
    step = array(dom["actual_step_scale"], (159,))
    width = array(dom["physical_width"], (163,))
    qscale = array(dom["original_qscale"], (159,))
    M = array(dom["physical_M"], (163, 159))
    require(np.all(width > 0) and np.all(qscale > 0) and np.all(step > 0),
            "positive original physical scales required")
    K = (M*qscale[None, :])/width[:, None]
    require(array_digest(K) == dom["normalized_K_sha256"]
            == model["binding"]["K_sha256"], "original coupled physical norm changed")
    radius = float(dom["common_radius"])
    require(radius == .001 and float(dom["trust_B"]) == .00025
            and np.array_equal(step, radius*qscale), "original common physical radius changed")
    mu = float(model["physical_norm_cost_mu"])
    phi0, target = float(model["complete_original_phi0"]), float(model["constant_target"])
    require(mu == 1e-6 and target == .26 and np.isfinite(phi0) and phi0 >= target,
            "original metric cost, target or complete baseline changed")
    lo = array(dom["outer_x_lower_z_then_h"], (160,))
    hi = array(dom["outer_x_upper_z_then_h"], (160,))
    require(np.all(lo <= hi), "inconsistent original outer box")
    nhard=len(dom["hard_original_row_tags"])
    nsoft=len(dom["selected_metric_original_row_tags"])
    hard_J = array(dom["hard_unscaled_physical159_J"], (nhard,159))
    hard_base = array(dom["hard_base_values"], (nhard,))
    hard_targets = array(dom["hard_frozen_targets"], (nhard,))
    hard_h = array(dom["hard_original_h_column"], (nhard,))
    soft_g = array(dom["selected_metric_gradients_of_phi"], (nsoft,159))
    soft_margin = array(dom["selected_metric_base_margins"], (nsoft,))
    physical_rhs = array(dom["physical_and_norm_original_rhs"], (652,))
    require(len(dom["hard_original_row_tags"]) == nhard
            and len(dom["selected_metric_original_row_tags"]) == nsoft,
            "original selected row ordering missing")
    blocks, rhs, kinds, origins = [], [], [], []
    def add(A, b, kind, source):
        A, b = np.asarray(A, float), np.asarray(b, float)
        require(A.ndim == 2 and A.shape[1] == 161 and b.shape == (len(A),)
                and np.all(np.isfinite(A)) and np.all(np.isfinite(b)), "finite exact row block required")
        start = sum(len(v) for v in rhs)
        blocks.append(A); rhs.append(b)
        kinds.extend([kind]*len(A))
        origins.append({"start": start, "count": len(A), "kind": kind, "source": source})
    hard_A = np.column_stack((-hard_J*step[None,:], hard_h, np.zeros(nhard)))
    add(hard_A, hard_base-hard_targets, "hard", "MODEL.original_domain.hard_*")
    z0 = np.zeros((163,2))
    add(np.column_stack((K,z0)), physical_rhs[:163], "physical", "original +K physical rows")
    add(np.column_stack((-K,z0)), physical_rhs[163:326], "physical", "original -K physical rows")
    aux = np.column_stack((-np.ones(163),np.zeros(163)))
    add(np.column_stack((K,aux)), physical_rhs[326:489], "norm", "original +K-h rows")
    add(np.column_stack((-K,aux)), physical_rhs[489:652], "norm", "original -K-h rows")
    bounds_A = np.zeros((320,161)); bounds_b = np.zeros(320)
    for j in range(160):
        bounds_A[2*j,j], bounds_b[2*j] = 1., hi[j]
        bounds_A[2*j+1,j], bounds_b[2*j+1] = -1., -lo[j]
    add(bounds_A,bounds_b,"bound","original interleaved upper/lower160 bounds")
    n = len(soft_g)
    add(np.column_stack((soft_g*step[None,:],np.full(n,mu),np.full(n,radius))),
        phi0-target+soft_margin,"metric","all newly built54 selected physical gradients")
    selected_keys = {(x["grid"],x["flat_row_id"]) for x in dom["selected_metric_original_row_tags"]}
    extra = model["additional_metric_gradients_not_already_in_selected_J"]
    require(len(extra) <= 19, "at most nineteen refreshed original seed tags")
    extra_receipt = []
    for row in extra:
        tag = row["original_row"]; key = (tag["grid"],tag["flat_row_id"])
        require(key not in selected_keys, "a paid new gradient unexpectedly duplicates selected source")
        selected_keys.add(key)
        g = array(row["unscaled_physical159_gradient"], (159,))
        require(array_digest(g) == row["gradient_sha256"], "fresh54 seed gradient mismatch")
        add(np.r_[g*step,mu,radius][None,:], np.array([row["base_gap"]]),"metric",
            "MODEL.additional_metric_gradients_not_already_in_selected_J")
        extra_receipt.append({"original_row":copy.deepcopy(tag),"gradient_sha256":row["gradient_sha256"]})
    add(np.r_[np.zeros(159),mu,radius][None,:],np.array([phi0-target]),"metric","original constant target")
    A,b=np.vstack(blocks),np.concatenate(rhs)
    kind=np.asarray(kinds,dtype=object)
    tol=np.where(kind=="metric",1e-9,1e-7)
    expected_rows=nhard+652+320+nsoft+len(extra)+1
    require(A.shape==(expected_rows,161) and b.shape==(expected_rows,),
            "complete new54 original-domain finite row count differs")
    initial=np.r_[(lo+hi)/2.,0.]
    receipt={
        "schema":POLICY+"-assembled-model","source_model_binding_sha256":source_binding,
        "source_physical_state_sha256":SOURCE_PHYSICAL_SHA,"row_count":len(A),"variable_count":161,
        "row_groups":origins,"A_sha256":array_digest(A),"b_sha256":array_digest(b),
        "row_tolerance_sha256":array_digest(tol),"row_kind_order_sha256":digest(kinds),
        "outer160_lower_sha256":array_digest(lo),"outer160_upper_sha256":array_digest(hi),
        "gain_coordinate_definition":"d = original_common_radius * gamma",
        "gain_scale":radius,"physical_norm_mu":mu,"complete_original_phi0":phi0,
        "constant_target":target,"K_sha256":array_digest(K),"step_scale_sha256":array_digest(step),
        "original_guard":copy.deepcopy(dom["original_guard"]),
        "all_new_paid_gradient_origins":extra_receipt,
        "original_selected_metric_rows_used":nsoft,"additional_paid_metric_rows_used":len(extra),
        "new_geometry_J_JVP_metric_gradient_calls":0,
        "original_hard_rows_not_deleted_or_softened":True,
        "gain_change_is_positive_coordinate_scaling_not_physical_change":True}
    model_out={"A":A,"b":b,"row_tol":tol,"row_kind":kinds,"outer_lo":lo,"outer_hi":hi,
               "initial_x":initial,"K":K,"M":M,"step":step,"source_state":state,
               "radius":radius,"mu":mu,"phi0":phi0,"receipt":receipt}
    ledger.check()
    return model_out


def finite_candidate(data, raw_x):
    if raw_x is None:
        return None
    x=np.asarray(raw_x,float)
    require(x.shape==(161,) and np.all(np.isfinite(x)), "the real last finite161 iterate required")
    A,b,tol=data["A"],data["b"],data["row_tol"]
    metric=np.asarray(data["row_kind"],object)=="metric"
    h=float(np.max(np.abs(data["K"]@x[:159]),initial=0.))
    repaired=x.copy();repaired[-2]=h;repaired[-1]=0.
    finite_gain=float(np.min(b[metric]-A[metric]@repaired))
    repaired[-1]=finite_gain/data["radius"]
    residual=A@repaired-b
    domain_pass=bool(np.all(residual[~metric]<=tol[~metric]))
    finite_metric_pass=bool(np.all(residual[metric]<=tol[metric]))
    p=data["step"]*repaired[:159]
    physical=data["M"]@p
    return {
        "schema":POLICY+"-finite-only-candidate",
        "original_last_finite161":vector_record(x),
        "finite_repaired161":vector_record(repaired),
        "unrounded_independent159_direction":vector_record(p),
        "linear_physical163_step":vector_record(physical),
        "raw_gain_d":data["radius"]*float(x[-1]),
        "actual_norm_h":h,"finite_repaired_gain_d":finite_gain,
        "finite_metric_maximum_without_norm_cost":data["phi0"]-finite_gain-data["mu"]*h,
        "all_original_domain_rows_within_tolerance":domain_pass,
        "all_paid_metric_rows_within_tolerance_after_repair":finite_metric_pass,
        "maximum_domain_original_residual":float(np.max(residual[~metric],initial=-np.inf)),
        "maximum_paid_metric_original_residual":float(np.max(residual[metric],initial=-np.inf)),
        "finite_positive_primal":bool(domain_pass and finite_metric_pass and finite_gain>1e-10),
        "qualified_complete_grid_direction":False,"actual_trial_started":False,
        "actual_rounding_exact163_box_complete_separation_and_original_actual_gates_still_required":True,
        "no_full_grid_qualification_or_physical_acceptance_inferred_from_finite_master":True}
