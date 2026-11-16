#!/usr/bin/env python3
"""Read true53's already-paid model once and assemble one new finite master.

Only input restoration, new finite row assembly and new-result diagnostics are
performed here. No old scientific entry, geometry, J, JVP or backend is called.
"""
from __future__ import annotations
import copy
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
import read_original_actions_log as reader

POLICY = "same159-true53-all-paid-finite-master-central-path-v1"
REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-new-mechanism"
SOURCE_GLOBAL_SECONDS = 1594.440227096
SOURCE_VALUES = 128
SOURCE_MODEL_BINDING = "e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1"
SOURCE_PHYSICAL = "9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e"
SOURCE = {
    "run_id": "43811870681", "job_id": "133115100791",
    "source_commit": "42f95905deec3024dfee7a687bdc806d38c79baf",
    "workflow": ".github/workflows/visible-true53-projected-direction.yml",
    "log_bytes": 35105831,
    "log_sha256": "fa7edaf1419325ce31e6926de44f8c9ebbddf1ea554d140fafef61aecbc9ceb9"}
RECORDS = {
    "MODEL": (27365833, "926681688d09311883c64dfa1dc40599a62d1904d7f6dbcaf478893fe14bd539"),
    "PROJECTION_RESULT": (1531224, "1750945efef7fed6f85b31205fd3ea8504c2f7411d03bedf1b11d6a0832beae7"),
    "COMPLETE": (5316472, "f2638d46b440afdb7336334cdc2ffe1c31b1ced18a5493e5fe39100a6daf03ba"),
    "FINAL_CLOCK": (127108, "b513907be93a9220bfd61487b6d07e885fd6c1547554dacfa15a10079372dc53")}


def require(test, message):
    if not bool(test):
        raise ValueError(message)


def digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False).encode()).hexdigest()


def array_digest(value):
    a = np.ascontiguousarray(value)
    return digest({"dtype": a.dtype.str, "shape": list(a.shape),
                   "bytes_sha256": hashlib.sha256(a.tobytes()).hexdigest()})


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


def read_paid_source(request, ledger):
    ledger.check()
    require(request["source"] == SOURCE and request["source_records"] ==
            {k: {"JSON_plus_LF_bytes": n, "JSON_plus_LF_sha256": s}
             for k, (n, s) in RECORDS.items()}, "only the original paid true53 source is permitted")
    api = reader.GitHubReader(REPO)
    run = api.api_json("/actions/runs/"+SOURCE["run_id"])
    require(str(run["id"]) == SOURCE["run_id"]
            and run["head_sha"] == SOURCE["source_commit"]
            and run["status"] == "completed" and run["conclusion"] == "success"
            and run["path"] == SOURCE["workflow"], "original run identity/status changed")
    jobs = api.api_json("/actions/runs/"+SOURCE["run_id"]+"/jobs?per_page=100")["jobs"]
    matches = [j for j in jobs if str(j["id"]) == SOURCE["job_id"]]
    require(len(matches) == 1 and matches[0]["name"] == "research"
            and matches[0]["status"] == "completed" and matches[0]["conclusion"] == "success",
            "the original successful research job is required")
    raw, redirects = api.job_log(SOURCE["job_id"])
    require(len(raw) == SOURCE["log_bytes"] and reader.digest(raw) == SOURCE["log_sha256"],
            "the once-read original raw log fingerprint changed")
    ledger.check()
    found = {}
    for line in raw.decode("utf-8-sig").splitlines():
        clean = reader.ANSI.sub("", line)
        match = reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body = match.group(2)
        for suffix, (length, sha) in RECORDS.items():
            tag = "TRUE53_PROJECTION_"+suffix+" "
            if body.startswith(tag):
                require(suffix not in found, "duplicate original stdout record")
                payload = body[len(tag):].encode("utf-8")+b"\n"
                require(len(payload) == length and reader.digest(payload) == sha,
                        "original "+suffix+" JSON+LF fingerprint changed")
                found[suffix] = reader.decode_json(payload)
    require(set(found) == set(RECORDS), "original complete source records missing")
    model, completed, clock, old = (found[k] for k in
                                    ("MODEL", "COMPLETE", "FINAL_CLOCK", "PROJECTION_RESULT"))
    require(model["binding_sha256"] == SOURCE_MODEL_BINDING
            and digest(model["binding"]) == SOURCE_MODEL_BINDING
            and model["binding"]["physical_state_sha256"] == SOURCE_PHYSICAL,
            "the frozen true53 model binding changed")
    require(old["status"] == "search-separation-allocation-ended-one-final-slot-reserved"
            and old["final_candidate"] is None, "source failure boundary changed")
    point = completed["selected_two_grid_physical_point"]
    require(point["accepted_index"] == 53 and point["physical_state_sha256"] == SOURCE_PHYSICAL
            and point["maximum_eta_on_both_grids"] == .26601514422985384
            and completed["actual_value_account"]["total_source_plus_new_started_values"] == SOURCE_VALUES,
            "only the unmodified actually accepted53 source is allowed")
    # The precise clock schema is preserved in the receipt; the request pins
    # its complete original JSON+LF before any new arithmetic.
    require(request["ancestor_final_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
            and request["ancestor_actual_values"] == SOURCE_VALUES
            and clock["ledger"]["total_ancestor_plus_new_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
            and clock["ledger"]["total_source_plus_new_full_values"] == SOURCE_VALUES,
            "the cumulative ancestor account changed")
    receipt = {
        "source": copy.deepcopy(SOURCE), "source_records": copy.deepcopy(request["source_records"]),
        "raw_log_reads": 1, "redirects_without_authorization": redirects,
        "source_model_binding_sha256": SOURCE_MODEL_BINDING,
        "source_selected_accepted_index": 53, "source_physical_state_sha256": SOURCE_PHYSICAL,
        "source_projection_status": old["status"],
        "source_scientific_clock": {
            "status":clock["status_at_final_emit"],
            "scientific_seconds":clock["ledger"]["scientific_seconds"],
            "total_ancestor_plus_new_scientific_seconds":clock["ledger"]["total_ancestor_plus_new_scientific_seconds"],
            "total_source_plus_new_full_values":clock["ledger"]["total_source_plus_new_full_values"],
            "started_counts":copy.deepcopy(clock["ledger"]["started_counts"])},
        "source_ordinary_values": SOURCE_VALUES,
        "source_global_scientific_seconds": SOURCE_GLOBAL_SECONDS,
        "source_full_grid_descent_or_new_physical_point_not_inferred": True,
        "source_arrays_only_read_from_original_stdout_not_recreated_or_uploaded": True,
        "earlier_source_log_reads": 0}
    ledger.check()
    return model, completed, receipt


def assemble_paid_master(model, ledger):
    ledger.check()
    require(model["binding_sha256"] == SOURCE_MODEL_BINDING, "one complete source model required")
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
    require(mu == 1e-6 and target == .26 and phi0 == .26601514422985395,
            "original metric cost, target or complete baseline changed")
    lo = array(dom["outer_x_lower_z_then_h"], (160,))
    hi = array(dom["outer_x_upper_z_then_h"], (160,))
    require(np.all(lo <= hi), "inconsistent original outer box")
    hard_J = array(dom["hard_unscaled_physical159_J"], (2937,159))
    hard_base = array(dom["hard_base_values"], (2937,))
    hard_targets = array(dom["hard_frozen_targets"], (2937,))
    hard_h = array(dom["hard_original_h_column"], (2937,))
    soft_g = array(dom["selected_metric_gradients_of_phi"], (5743,159))
    soft_margin = array(dom["selected_metric_base_margins"], (5743,))
    physical_rhs = array(dom["physical_and_norm_original_rhs"], (652,))
    require(len(dom["hard_original_row_tags"]) == 2937
            and len(dom["selected_metric_original_row_tags"]) == 5743,
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
    hard_A = np.column_stack((-hard_J*step[None,:], hard_h, np.zeros(2937)))
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
        phi0-target+soft_margin,"metric","all5743 already-paid selected physical gradients")
    selected_keys = {(x["grid"],x["flat_row_id"]) for x in dom["selected_metric_original_row_tags"]}
    extra = model["additional_metric_gradients_not_already_in_selected_J"]
    require(len(extra) == 5, "all five genuinely new paid gradients required")
    extra_receipt = []
    for row in extra:
        tag = row["original_row"]; key = (tag["grid"],tag["flat_row_id"])
        require(key not in selected_keys, "a paid new gradient unexpectedly duplicates selected source")
        selected_keys.add(key)
        g = array(row["unscaled_physical159_gradient"], (159,))
        require(array_digest(g) == row["gradient_sha256"], "new source gradient mismatch")
        add(np.r_[g*step,mu,radius][None,:], np.array([row["base_gap"]]),"metric",
            "MODEL.additional_metric_gradients_not_already_in_selected_J")
        extra_receipt.append({"original_row":copy.deepcopy(tag),"gradient_sha256":row["gradient_sha256"]})
    add(np.r_[np.zeros(159),mu,radius][None,:],np.array([phi0-target]),"metric","original constant target")
    A,b=np.vstack(blocks),np.concatenate(rhs)
    kind=np.asarray(kinds,dtype=object)
    tol=np.where(kind=="metric",1e-9,1e-7)
    require(A.shape==(9658,161) and b.shape==(9658,), "new all-paid master row count differs")
    initial=np.r_[(lo+hi)/2.,0.]
    receipt={
        "schema":POLICY+"-assembled-model","source_model_binding_sha256":SOURCE_MODEL_BINDING,
        "source_physical_state_sha256":SOURCE_PHYSICAL,"row_count":len(A),"variable_count":161,
        "row_groups":origins,"A_sha256":array_digest(A),"b_sha256":array_digest(b),
        "row_tolerance_sha256":array_digest(tol),"row_kind_order_sha256":digest(kinds),
        "outer160_lower_sha256":array_digest(lo),"outer160_upper_sha256":array_digest(hi),
        "gain_coordinate_definition":"d = original_common_radius * gamma",
        "gain_scale":radius,"physical_norm_mu":mu,"complete_original_phi0":phi0,
        "constant_target":target,"K_sha256":array_digest(K),"step_scale_sha256":array_digest(step),
        "original_guard":copy.deepcopy(dom["original_guard"]),
        "all_new_paid_gradient_origins":extra_receipt,
        "original_selected_metric_rows_used":5743,"additional_paid_metric_rows_used":5,
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
