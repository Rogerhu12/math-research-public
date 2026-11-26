#!/usr/bin/env python3
"""Advance the paid actual resonant field to fixed finite nonround cores.

This is a new inverse-design scope, not a replay of the circular entry or
the paid seed comparison. Each p is fixed during its complete hard-geometry
and metric solve. Only a full finer-grid qualification advances p; p is
never decreased to make a stage pass. All known paid radial observations
remain in every finer scan. This is not a continuous or fixed-g certificate.
"""
import argparse
from collections import defaultdict
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.optimize import minimize

MODEL_SHA256 = "584f02a67af1c0e87a68dac629d6e17b9b1bad93cef2c4c65b5a3b0c2253639f"
if hashlib.sha256(Path(__file__).with_name("r582_finite_resonant_model_20261126.py").read_bytes()).hexdigest() != MODEL_SHA256:
    raise RuntimeError("finite continuation model source binding changed")
from r582_finite_resonant_model_20261126 import Model, Parameters, blocked, hard, COUNTS as MODEL_COUNTS
from r582_paid_resonant_field_20261126 import (
    ResonantField, REFERENCE_CONTROL, PAID_REFINED_NORMALIZATION,
    LENGTH, CORE_END, paid_source, ClockCheckpoint,
)
from r582_true_core_shooting_20261126 import emit

SCHEMA = "r582-paid-resonant-finite-nonround-hard-continuation-v1"
INPUT_SCHEMA = "identified-true-core-root-for-finite-resonant-design-v1"
COUNTS = defaultdict(int)


class StageQualified(RuntimeError):
    pass


def check(deadline):
    if time.monotonic() >= deadline:
        raise hard.EndSegment("declared finite-design scientific clock")


def identity(values):
    a = np.asarray(values, dtype=np.float64)
    return {"entries": int(a.size), "binary64_sha256": hashlib.sha256(a.tobytes()).hexdigest()}


def append_nodes(existing, additions):
    """Preserve every actual node literally; only new near-duplicates merge."""
    kept = list(np.asarray(existing,dtype=float))
    for point in sorted(set(float(x) for x in additions)):
        if not 0 <= point <= LENGTH:
            raise ValueError("new actual radial constraint left [0,L]")
        if not kept or min(abs(point-old) for old in kept)>1e-12:
            kept.append(point)
    return np.asarray(sorted(kept),dtype=float)


def load_input(raw, digest):
    data = sys.stdin.buffer.read() if raw == "@stdin" else raw.encode()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("complete finite-resonant input digest differs")
    source = json.loads(data)
    if source.get("schema") != INPUT_SCHEMA:
        raise ValueError("finite-resonant source-state schema differs")
    origin = source["origin"]
    if (origin["run_id"] != 45812850055 or origin["job_id"] != 139884885837
            or origin["source_commit"] != "35c249bcad83b95a9a0da6af8cbcd1a7e17b15d9"
            or origin["FINAL_JSON_sha256"] != "384d5f1b0932d3fb09b5ab916e204f71c7016ed5a3c462b0fb3bbad2aafbe742"):
        raise ValueError("this new input requires the identified completed actual true-s root")
    if (not np.array_equal(source["reference_control"], REFERENCE_CONTROL)
            or source["paid_refined_core_normalization"] != PAID_REFINED_NORMALIZATION
            or not np.array_equal(source["reference_q"], paid_source.SOURCE_Q)):
        raise ValueError("paid actual root, normalization or reference coordinates changed")
    if hashlib.sha256(source["paid_seed_json"].encode()).hexdigest() != "517c1f85592434ed015f2eca6de235fc5750b42a035471df2d4e10c178eb33a7":
        raise ValueError("identified paid seed data changed")
    paid = json.loads(source["paid_seed_json"])
    paid_nodes = np.asarray(source["paid_fine_radial_nodes"], dtype=float)
    if (len(paid_nodes) != 4811 or paid_nodes[0] != 0 or paid_nodes[-1] != LENGTH
            or not np.all(np.isfinite(paid_nodes)) or not np.all(np.diff(paid_nodes) > 0)
            or identity(paid_nodes) != source["paid_fine_radial_identity"]):
        raise ValueError("the actual 4811-node paid fine observation was not preserved")
    if source["exact_kernel_transfer_or_full_core_return_proved"] is not False:
        raise ValueError("numerical paid root must not be promoted to an exact theorem")
    return source, paid, paid_nodes


def parameters(p):
    return Parameters(p=float(p), q=.18, offset=.2, length=.9,
        radial_count=8, modes=4, core_half_width=.02, core_collar_end=.036,
        cap_collar_width=0., cap_disk_radius=.22,
        ball_radius=1.012, strip_half_width=.3928, reach_target=.06072)


def stage_goal(epsilon, args):
    value = max(args.minimum_stage_eta, min(args.maximum_stage_eta,
                                            args.quadratic_stage_coefficient * epsilon ** 2))
    return min(value,args.final_core_eta_goal) if .18+epsilon>=args.target_core_p else value


def sliced_model(model, selection):
    """The same precomputed field on a radial block; no new interpolation."""
    result = Model.__new__(Model)
    result.__dict__.update(model.__dict__)
    for name in ("s", "w", "wm", "wd", "wdd", "bg_w", "bg_wm", "bg_wd", "bg_wdd",
                 "tail_height", "tail_height1", "tail_height2", "metric_weights",
                 "seed_ut", "seed_vt"):
        setattr(result, name, getattr(model, name)[selection])
    for name in ("bases", "seed_u", "seed_v", "mean_control_alpha", "mean_control_z"):
        setattr(result, name, [value[selection] for value in getattr(model, name)])
    result.nr = len(result.s)
    result.cache, result.cache_key, result.last_completed_q = None, None, None
    result.geometry_value_calls = result.geometry_AD_calls = result.geometry_parameter_directions = 0
    return result


class FineObserver:
    """Every declared fine node is read; blocking changes only peak memory."""
    def __init__(self, model, args, deadline):
        self.model, self.args, self.deadline = model, args, deadline
        self.s, self.theta, self.nr, self.nt = model.s, model.theta, model.nr, model.nt
        self.completed, self.radial_block_calls = 0, 0

    def scan(self, q):
        check(self.deadline)
        started = time.monotonic()
        fields, eta_parts = {}, []
        report, attainers = None, {}
        minimum = {"mean_E_min", "det_min", "z_min", "area_min"}
        maximum = {"mean_E_max", "ball_radius_max", "abs_y_max"}
        for first in range(0, self.nr, self.args.scan_radial_block):
            check(self.deadline)
            stop = min(first + self.args.scan_radial_block, self.nr)
            block = sliced_model(self.model, slice(first, stop))
            item, block_fields, eta = hard.complete_scan(
                block, q, self.args.mean_E_floor, self.args.det_floor)
            self.radial_block_calls += 1
            COUNTS["complete_fine_radial_blocks"] += 1
            COUNTS["fine_radial_points_evaluated"] += stop - first
            if report is None:
                report = dict(item)
            else:
                for key in minimum:
                    report[key] = min(report[key], item[key])
                for key in maximum:
                    report[key] = max(report[key], item[key])
            for name, value in block_fields.items():
                fields.setdefault(name, []).append(value.v.copy())
                candidate = dict(item["geometry_attainers"][name])
                candidate["radial_index"] += first
                if name not in attainers or candidate["value"] < attainers[name]["value"]:
                    attainers[name] = candidate
            for name in ("eta_attainer", "curvature_attainer"):
                candidate = dict(item[name])
                candidate["radial_index"] += first
                if first == 0 or candidate["value"] > report[name]["value"]:
                    report[name] = candidate
            eta_parts.append(eta)
            del block, block_fields
        fields = {name: np.concatenate(value, axis=0) for name, value in fields.items()}
        eta = np.concatenate(eta_parts, axis=0)
        worst = min(attainers, key=lambda name: attainers[name]["value"])
        working = {name: max(0., -(a["value"] - (0 if name == "positive_height" else self.args.geometry_margin)))
                   for name, a in attainers.items()}
        report.update(radial_nodes=self.nr, theta_nodes=self.nt,
            geometry_attainers=attainers, worst_geometry_group=worst,
            geometry_violation_max=max(0., -attainers[worst]["value"]),
            working_geometry_violation_max=max(working.values()),
            working_geometry_violation_by_group=working,
            eta_max=float(np.max(eta)),
            complete_fine_scan=True, radial_grid_identity=identity(self.s),
            continuous_radial_or_angular_coverage_certified=False,
            scan_seconds=time.monotonic()-started)
        self.completed += 1
        COUNTS["complete_fine_scans"] += 1
        return report, fields, eta


def observation_nodes(field, args):
    """Additional finite observations of the new numerical material seed."""
    maxima = np.max(abs(field.material_endpoint_jets), axis=(1, 2))
    active = maxima > args.material_observation_threshold
    selected = active.copy()
    selected[:-1] |= active[1:]
    selected[1:] |= active[:-1]
    selected[0] = selected[-1] = True
    nodes = field.material_knots[selected]
    out = hard.merged_nodes(np.r_[nodes, (nodes[:-1]+nodes[1:])/2], LENGTH)
    return out, {"all_material_endpoints": len(maxima), "observed_material_endpoints": int(np.sum(selected)),
        "endpoint_jet_threshold": args.material_observation_threshold,
        "maximum_unselected_endpoint_jet": float(np.max(maxima[~selected])) if np.any(~selected) else 0.,
        "endpoint_bound_is_not_a_between_node_error_certificate": True,
        "finite_material_observation_nodes": out.tolist()}


def actual_cover(model, q, args):
    g = model.geometry(q, differentiate=False, ignore_clock=True)
    groups = hard.fields_for_geometry(g, model.par, args.mean_E_floor, args.det_floor)
    working = {name: -(value.v-(0 if name == "positive_height" else args.geometry_margin))
               for name, value in groups.items()}
    e, f = g["e"].v, g["f"].v
    eta = .5 * (abs(e)+np.sqrt(e*e+4*f*f))
    worst = {name: max(0., float(np.max(value))) for name, value in working.items()}
    worst["metric"] = float(np.max(eta))
    return worst


def peak_proposals(observer, fields, eta, nodes, nt, phase, extra, covered, args):
    """Pending absolute peaks; urgent exchange only beyond actual row coverage."""
    pending, urgent, pending_angle, urgent_angle = [], [], False, False
    arrays = {name: -value+(0 if name == "positive_height" else args.geometry_margin)
              for name, value in fields.items()}
    if phase == "metric":
        arrays["metric"] = eta
    ratios = observer.nt // nt
    if ratios * nt != observer.nt:
        raise ValueError("fine uniform angles must contain the complete actual angular grid")
    for name, array in arrays.items():
        base = extra if (phase == "geometry_restoration" or name == "metric") else 0.
        actual_limit = max(base, covered[name])
        cutoff = (max(args.metric_exchange_absolute, args.metric_exchange_relative * max(0., actual_limit))
                  if name == "metric" else max(args.restoration_exchange_absolute,
                                               args.restoration_exchange_relative * max(0., actual_limit)))
        rowmax = np.max(array, axis=1)
        candidates = {int(np.argmax(rowmax))}
        candidates.update(i for i in range(1,len(rowmax)-1)
                          if rowmax[i] >= rowmax[i-1] and rowmax[i] >= rowmax[i+1])
        for index in sorted(candidates):
            value = float(rowmax[index])
            if value <= base + args.pending_peak_tolerance:
                continue
            s = float(observer.s[index])
            missing = np.min(abs(nodes-s)) > 1e-12
            if missing:
                pending.append(s)
                if value > actual_limit + cutoff:
                    urgent.append(s)
            if array.shape[1] > 1:
                old_angle_value = float(np.max(array[index, ::ratios]))
                if value > max(base,old_angle_value) + args.pending_peak_tolerance:
                    pending_angle = True
                    if value > max(actual_limit,old_angle_value) + cutoff:
                        urgent_angle = True
    return sorted(set(pending)), sorted(set(urgent)), pending_angle, urgent_angle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--source-state-sha256", required=True)
    for name, value in (("rtol",2e-11),("atol",2e-13),("max-step",.15),
        ("initial-epsilon",.001),("target-core-p",.8),("maximum-stage-eta",1e-5),
        ("minimum-stage-eta",2e-10),("quadratic-stage-coefficient",.25),("final-core-eta-goal",1e-7),
        ("mean-E-floor",.25),("det-floor",.1),("geometry-margin",1e-3),
        ("feasibility-tolerance",1e-8),("initial-trust",.01),
        ("minimum-trust",1e-6),("maximum-trust",.5),
        ("pending-peak-tolerance",1e-8),("restoration-exchange-absolute",1e-6),
        ("restoration-exchange-relative",.05),("metric-exchange-absolute",1e-7),
        ("metric-exchange-relative",.02),("material-observation-threshold",1e-12),
        ("maximum-seconds",2400.),("final-reserve-seconds",30.)):
        parser.add_argument("--"+name,type=float,default=value)
    for name, value in (("initial-radial-nodes",97),("theta-nodes",96),
        ("maximum-radial-nodes",769),("maximum-theta-nodes",384),
        ("outer-per-stage",60),("maximum-stages",12),("maxiter",80),
        ("block-directions",16),("scan-radial-block",256)):
        parser.add_argument("--"+name,type=int,default=value)
    args = parser.parse_args()
    if (not 0 < args.initial_epsilon < args.target_core_p-.18
            or args.target_core_p > .8 or args.theta_nodes % 4 or args.theta_nodes < 20
            or not 60 < args.maximum_seconds <= 2400 or args.block_directions < 1
            or args.scan_radial_block < 1 or args.maximum_stages < 1
            or not 0 < args.final_core_eta_goal <= 1e-6
            or args.initial_radial_nodes < 5 or not 0 < args.minimum_trust <= args.initial_trust <= args.maximum_trust):
        raise ValueError("invalid declared finite-stage scope")
    source, paid, paid_nodes = load_input(args.source_state_json,args.source_state_sha256)
    started = time.monotonic()
    deadline = started + args.maximum_seconds - args.final_reserve_seconds
    field, field_report, seed_observation = None, None, None
    q, nodes = np.asarray(source["reference_q"],dtype=float), np.array([])
    actual_nodes, actual_fine, pending_nodes = np.array([]), np.array([]), []
    nt, actual_nt, pending_angle = args.theta_nodes, 0, False
    trust, proposed_trust = args.initial_trust, args.initial_trust
    stage, outer, p = 0, -1, .18+args.initial_epsilon
    actual_p, phase, retained, last_trial, last_backend = None, None, None, None, None
    backend_p, backend_stage, backend_outer, backend_trust = None, None, None, None
    stage_records, outer_records = [], []
    termination, directional_check_completed = "declared_stage_budget", False
    current_rows, current_observer = None, None
    emit("FINITE_RESONANT_DEFINITION", {
        "schema":SCHEMA,"complete_source_input":source,
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "new_scope":"fixed nonround p with the paid actual resonant material predictor",
        "no_old_inner_DtN_or_three_seed_comparison":True,
        "new_dense_outward_transfer_needed_for_unsaved_interior_field":True,
        "same_paid_4811_nodes_in_every_fine_scan":True,
        "original_two_control_constraint_grid_is_not_relabelled_as_an_81_variable_optimized_grid":True,
        "p_never_shrunk_to_claim_stage_success":True,
        "mean_metric_changes_with_p_and_q":True,
        "fixed_g_refinement_or_README_completion":False})

    def snapshot(reason):
        return {"schema":SCHEMA,"reason":reason,"stage":stage,"outer":outer,
            "actual_grid_p":actual_p,"proposed_or_current_p":p,"phase":phase,
            "actual_retained_p":None if retained is None else retained["p"],
            "constructed_grid_p_does_not_qualify_a_retained_state_at_another_p":True,
            "actual_retained_state":retained,"last_completed_full_scan_trial":last_trial,
            "last_natural_OptimizeResult":last_backend,
            "actual_constraint_radial_nodes":actual_nodes.tolist(),
            "actual_constraint_theta_nodes":actual_nt,
            "actual_fine_radial_nodes":actual_fine.tolist(),
            "actual_fine_theta_nodes":2*actual_nt if actual_nt else 0,
            "pending_radial_nodes":pending_nodes,
            "pending_angular_upgrade":pending_angle,
            "proposed_constraint_radial_nodes":append_nodes(actual_nodes,pending_nodes).tolist() if len(actual_nodes) else [],
            "proposed_constraint_theta_nodes":actual_nt*(2 if pending_angle else 1),
            "actual_backend_trust":backend_trust,"proposed_next_trust":proposed_trust,
            "planned_current_trust":trust,
            "last_constructed_backend_identity":{"p":backend_p,"stage":backend_stage,
                "outer":backend_outer,"trust":backend_trust},
            "proposed_grid_is_not_already_optimized":True,
            "current_backend_cost_not_yet_folded_into_completed_outers":None if current_rows is None else {
                "value_evaluations":current_rows.evaluations,
                "complete_Jacobians":current_rows.jacobian_evaluations,
                "completed_direction_blocks":current_rows.directional_block_evaluations},
            "counts":dict(COUNTS),"new_model_counts":dict(MODEL_COUNTS),
            "elapsed_seconds":time.monotonic()-started,
            "mean_metric_frozen":False,"continuous_reach_certified":False,"README_completion_claim":False}

    try:
        field = ResonantField.__new__(ResonantField)
        field.__init__(paid,source["paid_positive_chart"],args,deadline)
        field_report = field.receipt()
        material_nodes, seed_observation = observation_nodes(field,args)
        emit("FINITE_RESONANT_FIELD",{"field":field_report,"finite_material_observation":seed_observation,
            "elapsed_seconds":time.monotonic()-started,"original_model_new_counts":dict(paid_source.COUNTS)})
        nodes = hard.merged_nodes(np.r_[np.linspace(0,LENGTH,args.initial_radial_nodes),
            CORE_END,.06,.78,.80,.82,source["initial_geometry_attainer_nodes"]],LENGTH)
        for stage in range(args.maximum_stages):
            goal = stage_goal(p-.18,args)
            stage_qualified = False
            for outer in range(args.outer_per_stage):
                check(deadline)
                if len(nodes)>args.maximum_radial_nodes or nt>args.maximum_theta_nodes:
                    termination="pending_grid_exceeds_declared_capacity"
                    break
                par=parameters(p)
                # These are observation locations, not divided-difference
                # knots. Exact uniqueness preserves all 4811 paid nodes,
                # even if a new location is a neighboring floating number.
                fine_nodes=np.unique(np.r_[paid_nodes,material_nodes,nodes,(nodes[:-1]+nodes[1:])/2])
                if not np.all(np.isin(paid_nodes,fine_nodes)) or not np.all(np.isin(nodes,fine_nodes)):
                    raise ArithmeticError("complete fine grid lost an actual paid or constraint node")
                coarse=Model(par,nodes,nt,field)
                fine=Model(par,fine_nodes,2*nt,field)
                current_observer=FineObserver(fine,args,deadline)
                actual_nodes,actual_fine,actual_nt,actual_p=nodes.copy(),fine_nodes.copy(),nt,p
                pending_nodes,pending_angle=[],False
                initial,fields,eta=current_observer.scan(q)
                viable=initial["working_geometry_violation_max"]<=args.feasibility_tolerance
                retained={"p":p,"stage":stage,"epsilon":p-.18,
                    "q":q.tolist(),"q_identity":identity(q),"scan":initial,
                    "qualified_on_this_fine_grid":viable,"accepted_as":"retained_input_requalified_on_actual_new_fine_grid"}
                phase="metric" if viable else "geometry_restoration"
                cover=actual_cover(coarse,q,args)
                extra=(max(v for k,v in cover.items() if k!="metric")+.001
                       if phase=="geometry_restoration" else cover["metric"]+1e-9)
                emit("FINITE_RESONANT_START",{"stage":stage,"outer":outer,"p":p,
                    "epsilon":p-.18,"stage_eta_goal":goal,"phase":phase,
                    "parameters":asdict(par),"q":q.tolist(),"q_identity":identity(q),
                    "actual_constraint_radial_nodes":actual_nodes.tolist(),"actual_constraint_theta_nodes":actual_nt,
                    "actual_fine_radial_nodes":actual_fine.tolist(),"actual_fine_theta_nodes":2*nt,
                    "initial_complete_fine_scan":initial,"initial_current_actual_cover":cover,
                    "actual_backend_trust":trust,"initial_backend_extra":extra,
                    "tail_quadrature":fine.tail_quadrature,"elapsed_seconds":time.monotonic()-started})
                if viable and initial["eta_max"]<=goal:
                    stage_qualified=True
                    termination="finite_fixed_p_stage_qualified"
                    break
                del fields,eta
                current_rows=blocked.NonlinearRows(coarse,args.mean_E_floor,args.det_floor,phase,deadline,args.geometry_margin)
                current_rows.block_size=args.block_directions
                backend_p,backend_stage,backend_outer,backend_trust=p,stage,outer,trust
                x0=np.r_[q,extra]
                if not directional_check_completed:
                    derivative=current_rows.jac(x0)
                    initial_row_values=current_rows.fun(x0).copy()
                    direction=np.cos(np.arange(len(x0))*.713)
                    direction[-1]=.13
                    h=2e-6
                    positive=current_rows.fun(x0+h*direction).copy()
                    negative=current_rows.fun(x0-h*direction).copy()
                    observed=(positive-negative)/(2*h)
                    predicted=derivative@direction
                    relative=float(np.linalg.norm(observed-predicted)/max(1.,np.linalg.norm(observed)))
                    emit("FINITE_RESONANT_DIRECTION",{"new_operator_check":True,
                        "relative_l2_difference":relative,"maximum_absolute_difference":float(np.max(abs(observed-predicted))),
                        "step":h,"all_actual_hard_rows":len(observed),
                        "same_stage_continues_automatically_after_check":True,
                        "old_paid_checks_not_replayed":True})
                    COUNTS["new_operator_directional_checks"]+=1
                    if relative>5e-5:
                        raise ArithmeticError("finite resonant block AD differs from its actual parameter direction")
                    directional_check_completed=True
                    # Reuse the already paid Jacobian at the identical x0.
                    current_rows.key=x0.tobytes()
                    current_rows.values=initial_row_values
                    current_rows.jacobian=derivative
                lower,upper=coarse.bounds()
                scales=np.full(coarse.size,.5)
                scales[64:72]=.2
                scales[72:80]=.15
                scales[-1]=.1
                best_q,best_scan=q.copy(),initial
                callbacks,accepted=0,0
                last_backend=None
                backend_returned=False

                def callback(value,terminal=False):
                    nonlocal best_q,best_scan,pending_nodes,pending_angle,callbacks,accepted,retained,last_trial
                    trial=np.asarray(value[:-1],dtype=float)
                    extra_value=float(value[-1])
                    scan,scan_fields,scan_eta=current_observer.scan(trial)
                    callbacks+=1
                    COUNTS["completed_optimizer_callback_scans"]+=1
                    viable=scan["working_geometry_violation_max"]<=args.feasibility_tolerance
                    if phase=="geometry_restoration":
                        accept=(scan["working_geometry_violation_max"]<best_scan["working_geometry_violation_max"]-1e-12
                                or viable)
                        accepted_as="working_geometry_restoration_only"
                    else:
                        accept=viable and scan["eta_max"]<best_scan["eta_max"]-1e-13
                        accepted_as="complete_fine_feasible_metric_improvement"
                    if accept:
                        best_q,best_scan=trial.copy(),scan
                        accepted+=1
                        COUNTS["accepted_"+phase]+=1
                        retained={"p":p,"stage":stage,"epsilon":p-.18,
                            "q":trial.tolist(),"q_identity":identity(trial),"scan":scan,
                            "qualified_on_this_fine_grid":viable,"accepted_as":accepted_as}
                    covered=actual_cover(coarse,trial,args)
                    added,urgent,angle,urgent_angle=peak_proposals(current_observer,scan_fields,scan_eta,
                        nodes,nt,phase,extra_value,covered,args)
                    pending_nodes=sorted(set(pending_nodes).union(added))
                    pending_angle=pending_angle or angle
                    last_trial={"p":p,"stage":stage,"epsilon":p-.18,
                        "q":trial.tolist(),"q_identity":identity(trial),"scan":scan,
                        "backend_extra":extra_value,"current_actual_row_cover":covered,
                        "accepted_as":accepted_as if accept else "not_accepted",
                        "terminal_natural_backend_point":terminal,"complete_fine_assessment":True}
                    progress=snapshot("complete_fine_callback_before_any_grid_or_trust_adaptation")
                    progress.update(callback=callbacks,urgent_missing_radial_peaks=urgent,
                        urgent_missing_angular_peak=urgent_angle)
                    emit("FINITE_RESONANT_PROGRESS",progress)
                    check(deadline)
                    if phase=="geometry_restoration" and viable:
                        raise hard.GeometryRestored("full fine working geometry restored")
                    if phase=="metric" and viable and scan["eta_max"]<=goal:
                        raise StageQualified("fixed p reached the actual complete fine metric goal")
                    if urgent or urgent_angle:
                        raise hard.ExchangeGrid("uncovered fine peak exceeds current actual row coverage")
                    if terminal and (pending_nodes or pending_angle):
                        raise hard.ExchangeGrid("natural backend returned; adopt all pending peaks together")

                status="backend_not_returned"
                try:
                    objective_jac=np.zeros(coarse.size+1);objective_jac[-1]=1.
                    result=minimize(lambda v:float(v[-1]),x0,jac=lambda v:objective_jac,method="SLSQP",
                        bounds=list(zip(np.r_[np.maximum(lower,q-trust*scales),0.],
                                        np.r_[np.minimum(upper,q+trust*scales),np.inf])),
                        constraints={"type":"ineq","fun":current_rows.fun,"jac":current_rows.jac},
                        callback=callback,options={"maxiter":args.maxiter,"ftol":1e-12,"disp":False})
                    backend_returned=True
                    last_backend={"p":p,"stage":stage,"outer":outer,"trust":backend_trust,
                        "status":int(result.status),"success":bool(result.success),
                        "message":str(result.message),"nit":int(result.nit),"nfev":int(result.nfev),
                        "njev":int(result.njev),"q":result.x[:-1].tolist(),"extra":float(result.x[-1]),
                        "is_natural_OptimizeResult":True}
                    callback(result.x,terminal=True)
                    status="natural_backend_returned"
                except StageQualified as error:
                    stage_qualified=True;status=str(error);termination="finite_fixed_p_stage_qualified"
                except (hard.GeometryRestored,hard.ExchangeGrid) as error:
                    status=str(error)
                q=best_q.copy()
                before=initial["working_geometry_violation_max"] if phase=="geometry_restoration" else initial["eta_max"]
                after=best_scan["working_geometry_violation_max"] if phase=="geometry_restoration" else best_scan["eta_max"]
                proposed_trust=trust
                if accepted and after<.75*before:
                    proposed_trust=min(args.maximum_trust,1.5*trust)
                elif not accepted and not pending_nodes and not pending_angle:
                    proposed_trust=max(args.minimum_trust,trust/2)
                proposed_nodes=append_nodes(nodes,pending_nodes)
                proposed_nt=nt*(2 if pending_angle else 1)
                record={"stage":stage,"outer":outer,"p":p,"phase":phase,"status":status,
                    "actual_retained_state":retained,"natural_OptimizeResult":last_backend,
                    "complete_callback_scans":callbacks,"accepted_complete_scans":accepted,
                    "value_evaluations":current_rows.evaluations,
                    "complete_Jacobians":current_rows.jacobian_evaluations,
                    "completed_direction_blocks":current_rows.directional_block_evaluations,
                    "actual_constraint_nodes":len(nodes),"actual_constraint_angles":nt,
                    "next_constraint_radial_nodes":proposed_nodes.tolist(),"next_constraint_theta_nodes":proposed_nt,
                    "actual_backend_trust":trust,"next_trust":proposed_trust,
                    "elapsed_seconds":time.monotonic()-started}
                outer_records.append(record)
                emit("FINITE_RESONANT_OUTER",record)
                COUNTS["completed_outers"]+=1
                COUNTS["completed_backend_value_evaluations"]+=current_rows.evaluations
                COUNTS["completed_backend_Jacobians"]+=current_rows.jacobian_evaluations
                COUNTS["completed_backend_direction_blocks"]+=current_rows.directional_block_evaluations
                COUNTS["natural_backend_returns"]+=int(backend_returned)
                current_rows=None
                nodes,nt,trust=proposed_nodes,proposed_nt,proposed_trust
                if stage_qualified:
                    break
                if backend_returned and not accepted and not pending_nodes and not pending_angle and trust<=args.minimum_trust:
                    termination="fixed_p_backend_stalled_without_qualified_progress"
                    break
            stage_record={"stage":stage,"p":actual_p,"requested_stage_p":p,
                "epsilon":None if actual_p is None else actual_p-.18,
                "stage_eta_goal":goal,"qualified":stage_qualified,"retained":retained,
                "actual_constraint_radial_nodes":actual_nodes.tolist(),"actual_constraint_theta_nodes":actual_nt,
                "pending_radial_nodes":pending_nodes,"pending_angular_upgrade":pending_angle,
                "termination":termination,"p_was_fixed_and_not_shrunk":True}
            stage_records.append(stage_record)
            emit("FINITE_RESONANT_STAGE",stage_record)
            if not stage_qualified:
                break
            if actual_p>=args.target_core_p:
                termination="target_core_p_has_finite_grid_design_candidate_only"
                break
            p=min(args.target_core_p,.18+2*(actual_p-.18))
            # Carry the actual q unchanged. Only the explicit new seed/core
            # amplitude changes. No fictitious accepted candidate at new p.
            emit("FINITE_RESONANT_NEXT_STAGE",{"next_p":p,"source_p":actual_p,
                "q_carried_unchanged":q.tolist(),"new_metric_identity":True,
                "new_stage_has_not_yet_been_evaluated":True})
    except (hard.EndSegment,ClockCheckpoint,blocked.DesignClockLimit) as error:
        termination="scientific_clock_checkpoint_not_complete"
        emit("FINITE_RESONANT_CHECKPOINT",dict(snapshot(str(error)),termination=termination))
    except Exception as error:
        termination="implementation_error_not_scientific_completion"
        emit("FINITE_RESONANT_IMPLEMENTATION_CHECKPOINT",dict(snapshot(str(error)),
            error_type=type(error).__name__,implementation_failure_not_a_mathematical_obstruction=True))
        raise
    finally:
        final=snapshot("natural_scientific_entry_exit_or_exception_checkpoint")
        final.update(termination=termination,stage_records=stage_records,outer_records=outer_records,
            field_receipt=field_report,material_observation=seed_observation,
            final_resonant_field_counts=None if field is None else dict(getattr(field,"counts",{})),
            original_model_new_counts=dict(paid_source.COUNTS),
            prior_cost_ledger=source["prior_cost_ledger"],
            new_directional_check_completed=directional_check_completed,
            mathematical_tail_DtN_ODE_and_Hermite_error_certified=False,
            exact_finite_isometric_family_constructed=False)
        emit("FINITE_RESONANT_FINAL",final)


if __name__ == "__main__":
    main()
