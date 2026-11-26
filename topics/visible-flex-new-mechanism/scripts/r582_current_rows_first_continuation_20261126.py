#!/usr/bin/env python3
"""Continue actual 97q only after the current full backend rows are feasible.

Preserve all 10934 paid fine locations and all four pending radial points.
The actual constraint angles stay at 1536 and all 3072 old fine angles stay
observed. The old unadopted 3072 constraint-angle proposal is kept as such;
only fresh qualified-candidate angular evidence may cause a new upgrade.
The original model, Jacobian, and full-fine acceptance are unchanged; paid
checks are not replayed.
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

MODEL_SHA256 = "13339343918d873cb5ae37b5f2be7e21044ecfc306974fad4948232e5d466260"
if hashlib.sha256(Path(__file__).with_name("r582_local_tail_columns_model_20261126.py").read_bytes()).hexdigest() != MODEL_SHA256:
    raise RuntimeError("finite continuation model source binding changed")
from r582_local_tail_columns_model_20261126 import (
    Model, Parameters, blocked, hard, COUNTS as MODEL_COUNTS, TAIL_EXTRA_COUNT, TAIL_GATES,
)
from r582_stable_material_field_20261126 import StableField, COUNTS as STABLE_COUNTS
from r582_finite_resonant_radius_only_20261126 import load_input as original_radius_input
from r582_paid_resonant_field_20261126 import (
    REFERENCE_CONTROL, PAID_REFINED_NORMALIZATION,
    LENGTH, CORE_END, paid_source, ClockCheckpoint,
)
from r582_true_core_shooting_20261126 import emit

PARENT_DRIVER_SHA256 = "dc74093cc226cd8cc5a034d92acfb020d3d38f726ce85cbf24ee9b14ba89f55c"
OBSERVER_SHA256 = "31fa9fb781fef9a2acefec2d8331a3b8a41f5faf099de221363f40131d8b6737"
for filename, digest in (
    ("r582_paid_local_tail_angular_continue_20261126.py", PARENT_DRIVER_SHA256),
    ("r604_reference_reach_norms_20261126.py", OBSERVER_SHA256)):
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != digest:
        raise RuntimeError("97q retained continuation dependency differs: "+filename)
from r582_paid_local_tail_angular_continue_20261126 import load_input as previous_angular_input
from r604_reference_reach_norms_20261126 import NormAccumulator, COUNTS as REACH_NORM_COUNTS

SCHEMA = "r582-retained97-current-complete-backend-rows-before-fine-and-exchange-v1"
INPUT_SCHEMA = "identified-97q-angular-terminal-for-current-rows-first-continuation-v1"
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
        raise ValueError("complete current-rows-first input digest differs")
    incoming = json.loads(data)
    if incoming.get("schema") != INPUT_SCHEMA:
        raise ValueError("current-rows-first source state schema differs")
    origin, state = incoming["origin"], incoming["resume97_state"]
    required = {"run_id":45850216756,"job_id":140014319556,
        "source_commit":"2f9f5939dee3a41f8436c1a90567388517e7ea73",
        "source_driver_sha256":PARENT_DRIVER_SHA256,
        "original_raw_bytes":3061968,
        "original_raw_sha256":"7b34ebe63f3f9ad76facdc3df033a3239fb4f2b6dc1287a6f49a1a85ccf4e1a9",
        "FINAL_JSON_bytes":397758,
        "FINAL_JSON_sha256":"20807e71f93ac86f68e50976a4db0b0a61f65914ac10719152a4510de62579fa",
        "request_sha256":"8eb7c8d18df9e4057644255c2933d1c0bf62eb67e09a6a588ef8dbb9fa253927",
        "source_state_sha256":"89eb8404f2bbf8f5601b9b246368263412d6b359c19a0efc94481909a8e0b4bf",
        "termination":"pending_grid_exceeds_declared_capacity"}
    if origin != required:
        raise ValueError("actual angular terminal origin differs")
    parent, paid, old10905 = previous_angular_input(
        incoming["original_source_state_json"], origin["source_state_sha256"])
    retained = state["actual_retained_state"]
    q = np.asarray(retained["q"],dtype=float)
    if (q.shape != (97,) or not np.all(np.isfinite(q))
            or identity(q) != retained["q_identity"]
            or retained["q_identity"]["binary64_sha256"] !=
                "eb37b419ccb59cfca020b21290953ebf36353984dc409ede51832991e9e19635"
            or retained["p"] != .181 or retained["stage"] != 0
            or retained["qualified_on_this_fine_grid"] is not True
            or retained["accepted_as"] != "retained_input_requalified_on_actual_new_fine_grid"):
        raise ValueError("actual retained97 geometry state was replaced or mislabelled")
    actual = np.asarray(state["actual_constraint_radial_nodes"],dtype=float)
    if (identity(actual) != state["actual_constraint_radial_identity"]
            or identity(actual)["binary64_sha256"] !=
                "2c81525926abd3ec42bb2e853de7cddc8522d537b52d89ee3def9095e10c233e"
            or len(actual) != 185 or state["actual_constraint_theta_nodes"] != 1536
            or state["actual_fine_theta_nodes"] != 3072
            or state["pending_angular_upgrade"] is not True
            or state["proposed_constraint_theta_nodes"] != 3072
            or state["actual_backend_trust"] != 2.
            or state["proposed_next_trust"] != 2.):
        raise ValueError("source actual versus proposed grid/trust identity differs")
    proposed = append_nodes(actual,state["pending_radial_nodes"])
    if (identity(proposed) != state["proposed_constraint_radial_identity"]
            or identity(proposed)["binary64_sha256"] !=
                "0057928a7a9b05c1061c608954860b1102906328decb743817d7c77c5845d7c3"
            or proposed.tolist() != state["proposed_constraint_radial_nodes"]
            or identity(state["pending_radial_nodes"]) != state["pending_radial_identity"]
            or len(state["pending_radial_nodes"]) != 4):
        raise ValueError("all four pending radial observations must enter the new actual grid")
    fine = np.unique(np.r_[old10905,actual,(actual[:-1]+actual[1:])/2])
    if (identity(fine) != state["actual_fine_radial_identity"]
            or identity(fine)["binary64_sha256"] !=
                "5f9bdaebec2dd1378c14505dffcea74a722546958da2a292f7345841dcec9cc9"
            or len(fine) != 10934):
        raise ValueError("complete source10934 physical observations changed")
    direction = state["paid_97q_directional_check"]
    if (direction != parent["resume97_state"]["paid_97q_directional_check"]
            or state["paid_7_point_diagnostics_not_replayed"] is not True
            or state["terminal_natural_OptimizeResult_is_none"] is not True):
        raise ValueError("the already paid operator check or natural-terminal identity changed")
    evidence = incoming["source_metric_callback_evidence"]
    if (len(evidence) != 2 or [x["outer"] for x in evidence] != [3,4]
            or any(x["accepted_as"] != "not_accepted" or x["urgent_missing_angular_peak"]
                   or not x["pending_angular_upgrade"]
                   or x["current_actual_row_cover"]["metric"] <= x["backend_extra"]
                   for x in evidence)):
        raise ValueError("the observed current-row infeasibility diagnosis changed")
    proposal = incoming["source_unadopted_angular_proposal"]
    if (proposal["constraint_radial_identity"] != state["proposed_constraint_radial_identity"]
            or proposal["constraint_theta_nodes"] != 3072
            or proposal["source_actual_constraint_theta_nodes"] != 1536
            or proposal["source_fine_theta_nodes"] != 3072
            or proposal["adopted_in_source"] is not False
            or proposal["adopted_at_this_new_entry"] is not False):
        raise ValueError("the unadopted source angular proposal must remain explicit")
    ledger = incoming["new_paid_cost_ledger"]
    if (ledger["new_scientific_seconds"] != 217.70690741200002
            or ledger["counts"]["accepted_geometry_restoration"] != 2
            or ledger["counts"]["natural_backend_returns"] != 0
            or ledger["new_directional_checks_this_run"] != 0
            or ledger["material_mesh_binary64_sha256"] !=
                "0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991"):
        raise ValueError("paid angular-continuation costs were changed or omitted")
    parent["resume97_origin"], parent["resume97_state"] = origin, state
    parent["resume97_input_sha256"] = digest
    parent["source_metric_callback_evidence"] = evidence
    parent["source_unadopted_angular_proposal"] = proposal
    parent["prior_cost_ledger"]["identified_97q_actual_angular_continuation"] = ledger
    return parent,paid,fine


class ResonantField(StableField):
    def local_diagnostics(self):
        """The parent's seven comparisons are identified, not rerun."""
        return {"already_paid_and_not_replayed":True,
            "source_run":45842923121,"source_job":139989034161,
            "source_FIELD_JSON_sha256":
                "aed0e08c3e62c80e90a00f148bdde34c96bf35d819426fb40eaa2e5dce75cc99",
            "new_diagnostic_points":0}


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
    for name in ("bases", "seed_u", "seed_v", "mean_control_alpha", "mean_control_z", "tail_bases_u", "tail_bases_v"):
        setattr(result, name, [value[selection] for value in getattr(model, name)])
    result.nr = len(result.s)
    result.cache, result.cache_key, result.last_completed_q = None, None, None
    result.geometry_value_calls = result.geometry_AD_calls = result.geometry_parameter_directions = 0
    return result


class FineObserver:
    """Every declared fine node is read; blocking changes only peak memory."""
    def __init__(self, model, args, deadline, reference_q):
        self.model, self.args, self.deadline = model, args, deadline
        self.reference_q = np.asarray(reference_q,dtype=float).copy()
        self.s, self.theta, self.nr, self.nt = model.s, model.theta, model.nr, model.nt
        self.completed, self.radial_block_calls = 0, 0

    def scan(self, q):
        check(self.deadline)
        started = time.monotonic()
        fields, eta_parts = {}, []
        report, attainers = None, {}
        reach_norms = NormAccumulator(self.reference_q)
        minimum = {"mean_E_min", "det_min", "z_min", "area_min"}
        maximum = {"mean_E_max", "ball_radius_max", "abs_y_max"}
        for first in range(0, self.nr, self.args.scan_radial_block):
            check(self.deadline)
            stop = min(first + self.args.scan_radial_block, self.nr)
            block = sliced_model(self.model, slice(first, stop))
            item, block_fields, eta = hard.complete_scan(
                block, q, self.args.mean_E_floor, self.args.det_floor)
            reach_norms.add(block,block.cache,first)
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
            reference_reach_norm_observation=reach_norms.report(q[-1]),
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
    angular_witnesses = {}
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
                    is_urgent = value > max(actual_limit,old_angle_value) + cutoff
                    witness = {"field":name,"s":s,
                        "theta":float(observer.theta[int(np.argmax(array[index]))]),
                        "fine_value":value,"coincident_old_angle_maximum":old_angle_value,
                        "backend_extra_or_zero":base,"actual_group_cover":covered[name],
                        "angular_excess":value-max(base,old_angle_value),
                        "urgent":bool(is_urgent),
                        "candidate_current_complete_backend_rows_feasible":True}
                    if (name not in angular_witnesses or witness["angular_excess"] >
                            angular_witnesses[name]["angular_excess"]):
                        angular_witnesses[name] = witness
                    if is_urgent:
                        urgent_angle = True
    return (sorted(set(pending)), sorted(set(urgent)), pending_angle, urgent_angle,
            list(angular_witnesses.values()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--source-state-sha256", required=True)
    for name, value in (("rtol",2e-11),("atol",2e-13),("max-step",.15),
        ("initial-epsilon",.001),("target-core-p",.8),("maximum-stage-eta",1e-5),
        ("minimum-stage-eta",2e-10),("quadratic-stage-coefficient",.25),("final-core-eta-goal",1e-7),
        ("mean-E-floor",.25),("det-floor",.1),("geometry-margin",1e-3),
        ("feasibility-tolerance",1e-8),("initial-trust",2.),
        ("minimum-trust",1e-5),("maximum-trust",2.),
        ("meaningful-geometry-decrease-absolute",1e-10),("meaningful-geometry-decrease-relative",1e-9),
        ("pending-peak-tolerance",1e-8),("restoration-exchange-absolute",1e-6),
        ("restoration-exchange-relative",.05),("metric-exchange-absolute",1e-7),
        ("metric-exchange-relative",.02),("material-observation-threshold",1e-12),
        ("maximum-seconds",2400.),("final-reserve-seconds",30.)):
        parser.add_argument("--"+name,type=float,default=value)
    for name, value in (("initial-radial-nodes",189),("theta-nodes",1536),
        ("maximum-radial-nodes",769),("maximum-theta-nodes",1536),
        ("outer-per-stage",60),("maximum-stages",12),("maxiter",80),
        ("block-directions",8),("scan-radial-block",128),("maximum-stalled-outers",3)):
        parser.add_argument("--"+name,type=int,default=value)
    args = parser.parse_args()
    if (not 0 < args.initial_epsilon < args.target_core_p-.18
            or args.target_core_p > .8 or args.theta_nodes % 4 or args.theta_nodes < 20
            or not 60 < args.maximum_seconds <= 2400 or args.block_directions < 1
            or args.scan_radial_block < 1 or args.maximum_stages < 1
            or not 0 < args.final_core_eta_goal <= 1e-6
            or args.initial_radial_nodes < 5 or args.maximum_stalled_outers < 1
            or args.meaningful_geometry_decrease_absolute < 0 or args.meaningful_geometry_decrease_relative < 0
            or not 0 < args.minimum_trust <= args.initial_trust <= args.maximum_trust):
        raise ValueError("invalid declared finite-stage scope")
    source, paid, paid_nodes = load_input(args.source_state_json,args.source_state_sha256)
    started = time.monotonic()
    deadline = started + args.maximum_seconds - args.final_reserve_seconds
    field, field_report, seed_observation = None, None, None
    source_q = np.asarray(source["resume97_state"]["actual_retained_state"]["q"],dtype=float)
    q, nodes = source_q.copy(), np.array([])
    if (args.theta_nodes != source["resume97_state"]["actual_constraint_theta_nodes"]
            or args.initial_trust != source["resume97_state"]["proposed_next_trust"]):
        raise ValueError("the actual1536 angles and trust2 must be preserved at this new entry")
    if .18+args.initial_epsilon != source["resume97_state"]["actual_retained_state"]["p"]:
        raise ValueError("the new tail-space solve must start at the identified fixed p=.181")
    actual_nodes, actual_fine, pending_nodes = np.array([]), np.array([]), []
    nt, actual_nt, pending_angle = args.theta_nodes, 0, False
    pending_angular_evidence = []
    trust, proposed_trust = args.initial_trust, args.initial_trust
    stage, outer, p = 0, -1, .18+args.initial_epsilon
    actual_p, phase, retained, last_trial, last_backend = None, None, None, None, None
    last_backend_callback_candidate = None
    backend_p, backend_stage, backend_outer, backend_trust = None, None, None, None
    backend_initial_extra = None
    stage_records, outer_records = [], []
    termination, directional_check_completed = "declared_stage_budget", True
    stalled_outers = 0
    current_rows, current_observer = None, None
    prepared_key, coarse, fine = None, None, None
    emit("FINITE_LOCAL_TAIL_DEFINITION", {
        "schema":SCHEMA,"validated_runtime_input_with_complete_paid_ancestry":source,
        "declared_source_state_sha256":args.source_state_sha256,
        "arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "new_scope":"actual retained97q; all189 radial constraints and1536 actual angles; complete current rows before fine/exchange",
        "physical_coordinate_scope":Model.coordinate_scope(),
        "parent_five_outers_and_five_callbacks_are_not_replayed":True,
        "all_10934_previous_physical_fine_locations_and_3072_fine_angles_preserved":True,
        "original_source_actual_grid":[185,1536],
        "original_source_unadopted_proposal":[189,3072],
        "first_new_grid":[189,1536],
        "old_angular_proposal_explicitly_not_adopted_without_fresh_qualified_evidence":True,
        "current_complete_rows_and_boxes_checked_before_fine_or_exchange":True,
        "infeasible_backend_intermediates_continue_the_same_SLSQP_call":True,
        "source_actual_trust":source["resume97_state"]["actual_backend_trust"],
        "source_proposed_trust":source["resume97_state"]["proposed_next_trust"],
        "initial_trust_is_not_reset":True,
        "paid97_directional_check_and_7_point_diagnostics_not_replayed":True,
        "same_material_quintic_model_AD_and_complete_physical_acceptance":True,
        "new_dense_outward_transfer_needed_for_unsaved_interior_field":True,
        "new_reference_norms_reuse_existing_geometry_without_certifying_reach":True,
        "p_never_shrunk_to_claim_stage_success":True,
        "mean_metric_changes_with_p_and_q":True,
        "fixed_g_refinement_or_README_completion":False})

    def snapshot(reason):
        return {"schema":SCHEMA,"reason":reason,"stage":stage,"outer":outer,
            "actual_grid_p":actual_p,"proposed_or_current_p":p,"phase":phase,
            "actual_retained_p":None if retained is None else retained["p"],
            "constructed_grid_p_does_not_qualify_a_retained_state_at_another_p":True,
            "actual_retained_state":retained,"last_completed_full_scan_trial":last_trial,
            "last_backend_callback_candidate":last_backend_callback_candidate,
            "last_backend_callback_candidate_is_not_automatically_a_fine_scanned_or_retained_state":True,
            "source_resume_origin":source["resume97_origin"],"physical_coordinate_scope":Model.coordinate_scope(),
            "source_unadopted_angular_proposal":source["source_unadopted_angular_proposal"],
            "stalled_outer_count":stalled_outers,
            "last_natural_OptimizeResult":last_backend,
            "actual_constraint_radial_nodes":actual_nodes.tolist(),
            "actual_constraint_theta_nodes":actual_nt,
            "actual_fine_radial_nodes":actual_fine.tolist(),
            "actual_fine_theta_nodes":2*actual_nt if actual_nt else 0,
            "pending_radial_nodes":pending_nodes,
            "pending_angular_upgrade":pending_angle,
            "pending_angular_upgrade_evidence":pending_angular_evidence,
            "proposed_constraint_radial_nodes":append_nodes(actual_nodes,pending_nodes).tolist() if len(actual_nodes) else [],
            "proposed_constraint_theta_nodes":actual_nt*(2 if pending_angle else 1),
            "actual_backend_trust":backend_trust,"proposed_next_trust":proposed_trust,
            "planned_current_trust":trust,
            "last_constructed_backend_identity":{"p":backend_p,"stage":backend_stage,
                "outer":backend_outer,"trust":backend_trust,"initial_extra":backend_initial_extra},
            "proposed_grid_is_not_already_optimized":True,
            "current_backend_cost_not_yet_folded_into_completed_outers":None if current_rows is None else {
                "value_evaluations":current_rows.evaluations,
                "complete_Jacobians":current_rows.jacobian_evaluations,
                "completed_direction_blocks":current_rows.directional_block_evaluations},
            "counts":dict(COUNTS),"new_model_counts":dict(MODEL_COUNTS),
            "R604_observation_counts":dict(REACH_NORM_COUNTS),
            "elapsed_seconds":time.monotonic()-started,
            "mean_metric_frozen":False,"continuous_reach_certified":False,"README_completion_claim":False}

    try:
        field = ResonantField.__new__(ResonantField)
        field.__init__(paid,source["paid_positive_chart"],args,deadline)
        field_report = field.receipt()
        material_nodes, seed_observation = observation_nodes(field,args)
        emit("FINITE_LOCAL_TAIL_FIELD",{"field":field_report,"finite_material_observation":seed_observation,
            "elapsed_seconds":time.monotonic()-started,"original_model_new_counts":dict(paid_source.COUNTS)})
        nodes = np.asarray(source["resume97_state"]["proposed_constraint_radial_nodes"],dtype=float).copy()
        # Adopt the four actual pending radial points.  The separately
        # retained source3072-angle proposal is not silently adopted here.
        for stage in range(args.maximum_stages):
            goal = stage_goal(p-.18,args)
            stage_qualified = False
            for outer in range(args.outer_per_stage):
                check(deadline)
                if len(nodes)>args.maximum_radial_nodes or nt>args.maximum_theta_nodes:
                    termination="pending_grid_exceeds_declared_capacity"
                    break
                par=parameters(p)
                # Protect every previously constructed physical fine point,
                # including midpoint observations introduced in this run.
                paid_nodes=np.unique(np.r_[paid_nodes,actual_fine])
                fine_nodes=np.unique(np.r_[paid_nodes,material_nodes,nodes,(nodes[:-1]+nodes[1:])/2])
                if not np.all(np.isin(paid_nodes,fine_nodes)) or not np.all(np.isin(nodes,fine_nodes)):
                    raise ArithmeticError("complete fine grid lost an actual previously observed or constraint node")
                next_key=(float(p),nodes.tobytes(),int(nt),fine_nodes.tobytes())
                if next_key != prepared_key:
                    coarse=Model(par,nodes,nt,field)
                    fine=Model(par,fine_nodes,2*nt,field)
                    current_observer=FineObserver(fine,args,deadline,source["reference_q"])
                    prepared_key=next_key
                else:
                    COUNTS["identical_prepared_model_grids_reused"]+=1
                actual_nodes,actual_fine,actual_nt,actual_p=nodes.copy(),fine_nodes.copy(),nt,p
                pending_nodes,pending_angle,pending_angular_evidence=[],False,[]
                reused_initial=(retained is not None and retained["p"]==p
                    and retained["q_identity"]==identity(q)
                    and retained["scan"]["radial_grid_identity"]==identity(fine_nodes)
                    and retained["scan"]["theta_nodes"]==2*nt
                    and retained["scan"]["complete_fine_scan"] is True)
                if reused_initial:
                    initial=retained["scan"]
                    COUNTS["identical_p_q_fine_grid_baseline_scans_reused"]+=1
                else:
                    initial,fields,eta=current_observer.scan(q)
                    del fields,eta
                viable=initial["working_geometry_violation_max"]<=args.feasibility_tolerance
                retained={"p":p,"stage":stage,"epsilon":p-.18,
                    "q":q.tolist(),"q_identity":identity(q),"scan":initial,
                    "qualified_on_this_fine_grid":viable,"accepted_as":
                        "retained_complete_fine_state_reused_at_identical_p_q_grid" if reused_initial
                        else "retained_input_requalified_on_actual_new_fine_grid"}
                phase="metric" if viable else "geometry_restoration"
                cover=actual_cover(coarse,q,args)
                extra=(max(initial["working_geometry_violation_max"],
                           max(v for k,v in cover.items() if k!="metric"))+.001
                       if phase=="geometry_restoration" else max(initial["eta_max"],cover["metric"])+1e-9)
                emit("FINITE_LOCAL_TAIL_START",{"stage":stage,"outer":outer,"p":p,
                    "epsilon":p-.18,"stage_eta_goal":goal,"phase":phase,
                    "parameters":asdict(par),"q":q.tolist(),"q_identity":identity(q),
                    "actual_constraint_radial_nodes":actual_nodes.tolist(),"actual_constraint_theta_nodes":actual_nt,
                    "actual_fine_radial_nodes":actual_fine.tolist(),"actual_fine_theta_nodes":2*nt,
                    "initial_complete_fine_scan":initial,"initial_current_actual_cover":cover,
                    "initial_scan_reused_at_identical_p_q_and_complete_fine_grid":reused_initial,
                    "actual_backend_trust":trust,"initial_backend_extra":extra,
                    "tail_quadrature":fine.tail_quadrature,"elapsed_seconds":time.monotonic()-started})
                if viable and initial["eta_max"]<=goal:
                    stage_qualified=True
                    termination="finite_fixed_p_stage_qualified"
                    break
                current_rows=blocked.NonlinearRows(coarse,args.mean_E_floor,args.det_floor,phase,deadline,args.geometry_margin)
                current_rows.block_size=args.block_directions
                backend_p,backend_stage,backend_outer,backend_trust=p,stage,outer,trust
                backend_initial_extra=extra
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
                    emit("FINITE_LOCAL_TAIL_DIRECTION",{"new_operator_check":True,
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
                scales=np.full(coarse.size,.05)
                scales[64:72]=.02
                scales[72:80]=.02
                scales[80:-1]=1.
                scales[-1]=.01
                lower_bound=np.r_[np.maximum(lower,q-trust*scales),0.]
                upper_bound=np.r_[np.minimum(upper,q+trust*scales),np.inf]
                starting_rows=current_rows.fun(x0)
                emit("FINITE_LOCAL_TAIL_BACKEND_START",{
                    "schema":SCHEMA,"stage":stage,"outer":outer,"p":p,"phase":phase,
                    "q_identity":identity(q),"initial_extra":extra,"actual_trust":trust,
                    "all_current_inequality_rows":len(starting_rows),
                    "complete_current_row_violation":max(0.,-float(np.min(starting_rows))),
                    "starting_row_value_is_cached_for_the_same_SLSQP_operator":True})
                best_q,best_scan=q.copy(),initial
                callbacks,accepted=0,0
                backend_callbacks=0
                last_backend=None
                backend_returned=False

                def callback(value,terminal=False):
                    nonlocal best_q,best_scan,pending_nodes,pending_angle,callbacks,accepted,retained,last_trial
                    nonlocal last_backend_callback_candidate,backend_callbacks,pending_angular_evidence
                    value=np.asarray(value,dtype=float)
                    trial=np.asarray(value[:-1],dtype=float)
                    extra_value=float(value[-1])
                    backend_callbacks+=1
                    COUNTS["backend_callback_invocations_including_explicit_terminal_read"]+=1
                    checked_started=time.monotonic()
                    last_backend_callback_candidate={"p":p,"stage":stage,"outer":outer,
                        "q":trial.tolist(),"q_identity":identity(trial),"backend_extra":extra_value,
                        "terminal_natural_backend_point":terminal,
                        "actual_constraint_radial_identity":identity(nodes),
                        "actual_constraint_theta_nodes":nt,
                        "current_complete_rows_check_completed":False,
                        "complete_fine_assessment":False,
                        "retained_by_this_raw_callback":False}
                    # This is the same full row vector passed to SLSQP,
                    # including both original metric epigraph inequalities.
                    # Infeasible intermediate SQP iterates must not pay a
                    # full fine scan and then abort their own backend call.
                    row_values=current_rows.fun(value)
                    row_violation=max(0.,-float(np.min(row_values)))
                    box_violation=max(0.,float(np.max(np.maximum(
                        lower_bound-value,value-upper_bound))))
                    backend_violation=max(row_violation,box_violation)
                    current_feasible=backend_violation<=args.feasibility_tolerance
                    COUNTS["completed_callback_current_complete_row_checks"]+=1
                    last_backend_callback_candidate.update(
                        current_complete_rows_check_completed=True,
                        current_complete_row_violation=row_violation,
                        current_backend_box_violation=box_violation,
                        current_complete_backend_violation=backend_violation,
                        current_complete_backend_feasible=current_feasible,
                        current_complete_rows_check_seconds=time.monotonic()-checked_started)
                    if not current_feasible:
                        COUNTS["fine_scans_skipped_for_current_backend_infeasibility"]+=1
                        emit("FINITE_LOCAL_TAIL_BACKEND_INFEASIBLE",{
                            "schema":SCHEMA,"stage":stage,"outer":outer,"p":p,
                            "backend_callback":backend_callbacks,
                            "candidate":last_backend_callback_candidate,
                            "actual_retained_q_identity":retained["q_identity"],
                            "current_rows_value_evaluations":current_rows.evaluations,
                            "current_rows_complete_Jacobians":current_rows.jacobian_evaluations,
                            "same_SLSQP_call_continues_unless_already_natural_terminal":not terminal,
                            "new_fine_scan_or_peak_exchange_for_this_candidate":False,
                            "elapsed_seconds":time.monotonic()-started})
                        check(deadline)
                        return
                    terminal_reuse=(terminal and last_trial is not None
                        and last_trial["p"]==p and last_trial["q_identity"]==identity(trial)
                        and last_trial["backend_extra"]==extra_value
                        and last_trial["scan"]["radial_grid_identity"]==identity(actual_fine)
                        and last_trial["scan"]["theta_nodes"]==2*nt
                        and last_trial["complete_fine_assessment"] is True)
                    if terminal_reuse:
                        COUNTS["identical_natural_terminal_fine_assessments_reused"]+=1
                        last_trial=dict(last_trial,terminal_natural_backend_point=True)
                        last_backend_callback_candidate.update(
                            complete_fine_assessment=True,
                            fine_assessment_reused_at_identical_p_q_extra_grid=True)
                        emit("FINITE_LOCAL_TAIL_TERMINAL_REUSE",{
                            "schema":SCHEMA,"stage":stage,"outer":outer,"p":p,
                            "q_identity":identity(trial),"backend_extra":extra_value,
                            "same_complete_fine_assessment_reused_without_new_geometry":True,
                            "pending_radial_nodes":pending_nodes,
                            "pending_angular_upgrade":pending_angle,
                            "pending_angular_upgrade_evidence":pending_angular_evidence})
                        if pending_nodes or pending_angle:
                            raise hard.ExchangeGrid("natural backend returned; adopt all already observed pending peaks")
                        return
                    scan,scan_fields,scan_eta=current_observer.scan(trial)
                    callbacks+=1
                    COUNTS["completed_optimizer_callback_scans"]+=1
                    last_backend_callback_candidate["complete_fine_assessment"]=True
                    viable=scan["working_geometry_violation_max"]<=args.feasibility_tolerance
                    if phase=="geometry_restoration":
                        meaningful=max(args.meaningful_geometry_decrease_absolute,
                            args.meaningful_geometry_decrease_relative*max(1.,best_scan["working_geometry_violation_max"]))
                        accept=(scan["working_geometry_violation_max"]<best_scan["working_geometry_violation_max"]-meaningful
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
                        last_backend_callback_candidate["retained_by_this_raw_callback"]=True
                    covered=actual_cover(coarse,trial,args)
                    added,urgent,angle,urgent_angle,angular_evidence=peak_proposals(current_observer,scan_fields,scan_eta,
                        nodes,nt,phase,extra_value,covered,args)
                    pending_nodes=sorted(set(pending_nodes).union(added))
                    pending_angle=pending_angle or angle
                    combined={entry["field"]:entry for entry in pending_angular_evidence}
                    for entry in angular_evidence:
                        entry.update(p=p,trial_q_identity=identity(trial))
                        if (entry["field"] not in combined or entry["angular_excess"]>
                                combined[entry["field"]]["angular_excess"]):
                            combined[entry["field"]]=entry
                    pending_angular_evidence=list(combined.values())
                    last_trial={"p":p,"stage":stage,"epsilon":p-.18,
                        "q":trial.tolist(),"q_identity":identity(trial),"scan":scan,
                        "backend_extra":extra_value,"current_actual_row_cover":covered,
                        "accepted_as":accepted_as if accept else "not_accepted",
                        "terminal_natural_backend_point":terminal,"complete_fine_assessment":True}
                    progress=snapshot("complete_fine_callback_before_any_grid_or_trust_adaptation")
                    progress.update(callback=callbacks,urgent_missing_radial_peaks=urgent,
                        urgent_missing_angular_peak=urgent_angle)
                    emit("FINITE_LOCAL_TAIL_PROGRESS",progress)
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
                        bounds=list(zip(lower_bound,upper_bound)),
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
                stalled_outers = 0 if accepted or pending_nodes or pending_angle else stalled_outers+1
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
                    "backend_callback_invocations_including_explicit_terminal_read":backend_callbacks,
                    "value_evaluations":current_rows.evaluations,
                    "complete_Jacobians":current_rows.jacobian_evaluations,
                    "completed_direction_blocks":current_rows.directional_block_evaluations,
                    "actual_constraint_nodes":len(nodes),"actual_constraint_angles":nt,
                    "next_constraint_radial_nodes":proposed_nodes.tolist(),"next_constraint_theta_nodes":proposed_nt,
                    "next_angular_upgrade_evidence":pending_angular_evidence,
                    "actual_backend_trust":trust,"next_trust":proposed_trust,
                    "elapsed_seconds":time.monotonic()-started}
                outer_records.append(record)
                emit("FINITE_LOCAL_TAIL_OUTER",record)
                COUNTS["completed_outers"]+=1
                COUNTS["completed_backend_value_evaluations"]+=current_rows.evaluations
                COUNTS["completed_backend_Jacobians"]+=current_rows.jacobian_evaluations
                COUNTS["completed_backend_direction_blocks"]+=current_rows.directional_block_evaluations
                COUNTS["natural_backend_returns"]+=int(backend_returned)
                current_rows=None
                nodes,nt,trust=proposed_nodes,proposed_nt,proposed_trust
                if stage_qualified:
                    break
                if (backend_returned and not accepted and not pending_nodes and not pending_angle
                        and (trust<=args.minimum_trust or stalled_outers>=args.maximum_stalled_outers)):
                    termination="new_tail_space_backend_stalled_without_qualified_progress"
                    break
            stage_record={"stage":stage,"p":actual_p,"requested_stage_p":p,
                "epsilon":None if actual_p is None else actual_p-.18,
                "stage_eta_goal":goal,"qualified":stage_qualified,"retained":retained,
                "actual_constraint_radial_nodes":actual_nodes.tolist(),"actual_constraint_theta_nodes":actual_nt,
                "pending_radial_nodes":pending_nodes,"pending_angular_upgrade":pending_angle,
                "termination":termination,"p_was_fixed_and_not_shrunk":True}
            stage_records.append(stage_record)
            emit("FINITE_LOCAL_TAIL_STAGE",stage_record)
            if not stage_qualified:
                break
            if actual_p>=args.target_core_p:
                termination="target_core_p_has_finite_grid_design_candidate_only"
                break
            p=min(args.target_core_p,.18+2*(actual_p-.18))
            stalled_outers=0
            # Carry the actual q unchanged. Only the explicit new seed/core
            # amplitude changes. No fictitious accepted candidate at new p.
            emit("FINITE_LOCAL_TAIL_NEXT_STAGE",{"next_p":p,"source_p":actual_p,
                "q_carried_unchanged":q.tolist(),"new_metric_identity":True,
                "new_stage_has_not_yet_been_evaluated":True})
    except (hard.EndSegment,ClockCheckpoint,blocked.DesignClockLimit) as error:
        termination="scientific_clock_checkpoint_not_complete"
        emit("FINITE_LOCAL_TAIL_CHECKPOINT",dict(snapshot(str(error)),termination=termination))
    except Exception as error:
        termination="implementation_error_not_scientific_completion"
        emit("FINITE_LOCAL_TAIL_IMPLEMENTATION_CHECKPOINT",dict(snapshot(str(error)),
            error_type=type(error).__name__,implementation_failure_not_a_mathematical_obstruction=True))
        raise
    finally:
        final=snapshot("natural_scientific_entry_exit_or_exception_checkpoint")
        final.update(termination=termination,stage_records=stage_records,outer_records=outer_records,
            field_receipt=field_report,material_observation=seed_observation,
            final_resonant_field_counts=None if field is None else dict(getattr(field,"counts",{})),
            final_stable_evaluator_counts=dict(STABLE_COUNTS),
            original_model_new_counts=dict(paid_source.COUNTS),
            prior_cost_ledger=source["prior_cost_ledger"],
            paid_97q_directional_check_complete_in_parent=directional_check_completed,
            new_directional_checks_this_run=COUNTS["new_operator_directional_checks"],
            paid_seven_point_diagnostics_replayed=False,
            mathematical_tail_DtN_ODE_and_Hermite_error_certified=False,
            exact_finite_isometric_family_constructed=False)
        emit("FINITE_LOCAL_TAIL_FINAL",final)


if __name__ == "__main__":
    main()
