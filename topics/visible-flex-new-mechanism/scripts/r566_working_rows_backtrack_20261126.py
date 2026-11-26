#!/usr/bin/env python3
"""Resume actual B030 state with working-feasible backtracking of backend trials.

All original complete coarse/fine/actual-angle qualification is retained.
Only a working-feasible candidate can reach that qualification; no working
row or smaller backend epigraph is by itself an accepted physical state.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

PREVIOUS_SHA="90499f5c107b9ef68c9ad69eeabd28ae59755afec1346f19ef79d696629b2ad0"
previous_path=Path(__file__).with_name("r566_working_rows_full_acceptance_20261126.py")
if hashlib.sha256(previous_path.read_bytes()).hexdigest()!=PREVIOUS_SHA:
    raise RuntimeError("the actually executed complete-acceptance source changed")
import r566_working_rows_full_acceptance_20261126 as previous

old,hard,angular=previous.old,previous.hard,previous.angular
minimize=previous.minimize
digest,compact,check_time=previous.digest,previous.compact,previous.check_time
RestartWorking,OracleLedger,WorkingRows=previous.RestartWorking,previous.OracleLedger,previous.WorkingRows
candidate_rows=previous.candidate_rows
append_radial_nodes,add_rows=previous.append_radial_nodes,previous.add_rows
bind_working_radii,row_key=previous.bind_working_radii,previous.row_key
SCHEMA="r566-paid-working-backtrack-with-full-physical-acceptance-v1"
SOURCE_RUN,SOURCE_JOB=45828479581,139938706452
SOURCE_COMMIT="9704840a2a00dd8345435f8024fea07187dd9923"
SOURCE_FINAL_SHA="913c9cfc28e19e0b237d4cbbefb080d7a70b30b545e30754706f4e1ddadd1761"
SOURCE_REQUEST_SHA="6756f5945133fd9f3f747906f43ec3befaacdde3e3404c036bb4bf1ae33cd4b4"

def source_input(args):
    source=json.loads(args.source_state_json)
    if source.get("schema")!="r566-paid-final-working-backtrack-input-v1":
        raise ValueError("wrong actual terminal continuation input")
    expected={"run_id":SOURCE_RUN,"job_id":SOURCE_JOB,"source_commit":SOURCE_COMMIT,
        "source_sha256":PREVIOUS_SHA,"raw_stdout_bytes":38712407,
        "raw_stdout_sha256":"f1b4897168262c1a6afaa23c721eb10d4e7bf5c9d643dbd28cda7c5e331b6a02",
        "FINAL_JSON_bytes":132427,"FINAL_JSON_sha256":SOURCE_FINAL_SHA,
        "recovery_run":45844119049,"recovery_job":139993191345,
        "recovery_stdout_sha256":"f3fd0bd306937d524f111958fa09403b1c1552d1065bbfa941f146edb8cef1d2"}
    if source["origin"]!=expected:
        raise ValueError("the actual natural terminal and recovery identities changed")
    relative="topics/visible-flex-new-mechanism/computations/request-r566-working-rows-20261126.json"
    if (source["coordinates_reused_exactly_from_bound_source_request"]!=relative
            or source["bound_source_request_sha256"]!=SOURCE_REQUEST_SHA):
        raise ValueError("wrong already-paid physical coordinate source")
    repository=Path(__file__).resolve().parents[3]
    request_bytes=(repository/relative).read_bytes()
    if len(request_bytes)!=191771 or digest(request_bytes)!=SOURCE_REQUEST_SHA:
        raise ValueError("the original complete source request changed")
    request=json.loads(request_bytes)
    old_args=argparse.Namespace(**vars(args))
    old_args.source_state_json=request["lanes"]["rounded-core-B030"]["source_state_json"]
    original,ancestor,old_start,par,geo,q,nodes,peaks,nt,old_trust=previous.source_input(old_args)
    terminal=json.loads(source["complete_FINAL_without_repeated_coordinates_JSON"])
    omitted=("actual_retained_q","actual_complete_required_radial_nodes","actual_complete_required_peak_orbits")
    if any(k in terminal for k in omitted):
        raise ValueError("compact final duplicates instead of identifying exact prior coordinates")
    terminal.update(actual_retained_q=q.tolist(),
        actual_complete_required_radial_nodes=nodes.tolist(),
        actual_complete_required_peak_orbits=peaks)
    raw=compact(terminal).encode()
    if len(raw)!=132427 or digest(raw)!=SOURCE_FINAL_SHA:
        raise ValueError("the full original FINAL did not reconstruct byte for byte")
    counts=terminal["cost"]["counts"]
    if (terminal["actual_q_binary64_sha256"]!=digest(q.tobytes())
            or (len(nodes),len(peaks),nt)!=(571,1276,1536)
            or terminal["actual_backend_local_trust"]!=.3003387451171875
            or terminal["proposed_next_local_trust"]!=.3003387451171875
            or terminal["post_backend_trust_decision_completed"] is not False
            or terminal["phase"]!="metric" or counts["accepted_metric_steps"]!=0
            or counts["accepted_restoration_steps"]!=0
            or counts["complete_coarse_scans"]!=7
            or len(terminal["actual_working_field_orbit_rows"])!=150
            or terminal["recorded_unapplied_physical_peak_orbits"]
            or terminal["recorded_unapplied_working_rows"]):
        raise ValueError("actual state, unfinished trust decision, or source costs differ")
    if (source["source_last_backend_required_scalar_rows"]!=2030126
            or source["source_last_backend_extra"]!=.25895161785933823):
        raise ValueError("last paid complete library row count changed")
    source["source_cost_ledger"]={
        "source_run":SOURCE_RUN,"source_job":SOURCE_JOB,
        "complete_actual_source_cost":terminal["cost"],
        "recorded_chain_scientific_seconds_lower_bound":
            terminal["cost"]["prior_cost_ledger"]["recorded_chain_scientific_seconds_lower_bound"]
            +terminal["cost"]["elapsed_seconds"],
        "recorded_chain_scientific_seconds_is_exact":False,
        "earlier_censored_work_still_unknown":True,
        "metadata_recovery_scientific_evaluations":0}
    start={"initial_fine_and_observed_scan":terminal["actual_retained_qualification"],
           "initial_observed_peaks":terminal["actual_retained_observed_peak_summary"]}
    return source,ancestor,start,par,geo,q,nodes,peaks,nt,terminal["actual_backend_local_trust"],terminal

def parser():
    p=previous.parser()
    p.description=__doc__
    p.add_argument("--working-backtrack-steps",type=int,default=16)
    return p

def main():
    args = parser().parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("new working globalization runs only in declared public Actions")
    if not 1<=args.working_backtrack_steps<=24:
        raise ValueError("outside declared working backtracking scope")
    raw = sys.stdin.buffer.read() if args.source_state_json == "@stdin" else args.source_state_json.encode()
    if digest(raw) != args.source_state_sha256:
        raise ValueError("complete stdin source-state hash differs")
    args.source_state_json = raw.decode()
    if (not 0 < args.final_reserve_seconds < args.maximum_seconds <= 2400
            or not 0 < args.minimum_trust <= args.maximum_trust <= 4
            or min(args.radial_base, args.outer, args.maxiter, args.working_radial_batch,
                   args.working_witnesses_per_field, args.maximum_working_rows) < 1
            or not 1 <= args.block_directions <= 81 or args.point_batch_size < 1):
        raise ValueError("invalid working-row scope")
    started = time.monotonic()
    deadline = started+args.maximum_seconds-args.final_reserve_seconds
    source, ancestor, start, par, geo, q, nodes, peaks, nt, trust, terminal = source_input(args)
    tolerance = geo["feasibility_tolerance"]
    mean_floor, det_floor, margin = geo["mean_E_floor"], geo["det_floor"], geo["geometry_margin"]
    best_scan = dict(start["initial_fine_and_observed_scan"])
    best_geo = 0.
    best_eta = best_scan["accepted_eta_max"]
    best_observed = dict(start["initial_observed_peaks"])
    pending=list(terminal["recorded_unapplied_physical_peak_orbits"])
    proposed_working=list(terminal["recorded_unapplied_working_rows"])
    working=list(terminal["actual_working_field_orbit_rows"])
    actual_nodes, actual_peaks = nodes.copy(), list(peaks)
    actual_trust, proposed_trust = trust, trust
    trust_decision_completed = False
    ledger = OracleLedger()
    counts = {"outer_started":0, "outer_completed":0, "accepted_metric_steps":0,
        "accepted_restoration_steps":0, "working_value_rejected_callbacks":0,
        "complete_coarse_scans":0, "complete_fine_scans":0,
        "complete_localizations":0, "localizer_candidates":0, "localizer_completed_candidates":0,
        "localizer_point_objective_evaluations":0, "localizer_unresolved_returns":0,
        "required_row_rejections":0, "fine_required_row_rejections":0,
        "nested_quadrature_rejections":0, "working_exchanges":0, "physical_exchanges":0,
        "backend_natural_returns":0, "new_restriction_observations":0,
        "working_value_keys":0, "working_complete_jacobians":0,
        "working_direction_blocks":0, "working_jacobian_seconds":0.,
        "backtrack_callback_proposals":0,"backtrack_value_trials":0,
        "backtrack_working_recoveries":0,"backtrack_exhausted":0,
        "backtracked_fully_qualified_acceptances":0,
        "paid_current_complete_selection_replays_avoided":0}
    last_trial = last_backend = None
    last_raw_backend_trial = last_backtrack = None
    current_full_library_values_known = True
    known_scalar_rows = source["source_last_backend_required_scalar_rows"]
    retained_working_base_extra = source["source_last_backend_extra"]
    active_rows = None
    current_outer, phase = -1, "metric"
    status = "declared_outer_limit_not_complete"

    def costs():
        return {"elapsed_seconds":time.monotonic()-started, "counts":dict(counts),
            "active_working_counts_not_yet_retired": None if active_rows is None else dict(active_rows.counts),
            "oracle_totals_once_per_live_or_retired_oracle":ledger.snapshot(),
            "prior_cost_ledger":source["source_cost_ledger"],
            "all_unclosed_current_operation_work_in_elapsed_not_fabricated_as_completed":True}

    def snapshot(tag, reason):
        hard.emit(tag, {"schema":SCHEMA, "reason":reason, "outer":current_outer,
            "phase":phase, "actual_retained_q":q.tolist(), "actual_q_binary64_sha256":digest(q.tobytes()),
            "actual_retained_qualification":best_scan,
            "actual_retained_observed_peak_summary":best_observed,
            "actual_complete_required_radial_nodes":actual_nodes.tolist(),
            "actual_complete_required_peak_orbits":actual_peaks,
            "actual_uniform_angles_and_FFT_nodes":nt,
            "recorded_unapplied_physical_peak_orbits":pending,
            "actual_working_field_orbit_rows":working,
            "recorded_unapplied_working_rows":proposed_working,
            "actual_backend_local_trust":actual_trust, "proposed_next_local_trust":proposed_trust,
            "post_backend_trust_decision_completed": trust_decision_completed,
            "proposed_trust_not_yet_adopted": proposed_trust != actual_trust,
            "retained_qualification_is_on_its_recorded_grid_not_automatic_for_new_library": True,
            "last_trial_not_implicitly_accepted":last_trial, "last_backend":last_backend,
            "last_raw_backend_trial_not_implicitly_accepted":last_raw_backend_trial,
            "last_working_backtrack":last_backtrack,
            "current_complete_library_values_known_for_retained_q":current_full_library_values_known,
            "retained_working_feasible_base_extra":retained_working_base_extra,
            "cost":costs(), "no_physical_row_removed_by_working_selection":True,
            "continuous_geometry_reach_or_README_completion_claim":False})

    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION", {"schema":SCHEMA, "source_state":source,
        "source_state_sha256":digest(raw), "physical_parameters":asdict(par), "geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "original_571_rings_and_1276_orbits_retained":True,
        "all_old_1536_uniform_inequalities_retained_for_full_value_acceptance":True,
        "working_points_never_redefine_mean_E":True,
        "old_completed_START_scan_and_localization_not_replayed":True,
        "old_unadapted_trust_retained":True,
        "every_accepted_step_requires_complete_coarse_fine_actual_peaks_and_nested_quadrature":True,
        "unrepresented_violations_reject_and_enter_working_or_physical_libraries":True,
        "fine_geometry_margin_and_backend_metric_epigraph_enforced_at_acceptance":True,
        "only_local_optimization_matrix_is_restricted":True,
        "old_oracle_parity_check_not_repeated":True,
        "old_paid_restriction_mapping_or_direction_observation_repeated":False,
        "working_backtracking_never_bypasses_complete_qualification":True,
        "actual_q_and_unfinished_trust_from_original_FINAL":True,
        "same_working_model_fun_and_jac_cache_preserved":True,
        "old_unreported_Jacobian_matrix_not_fabricated_as_available":True,
        "metric_changes_during_static_design":True, "fixed_g_or_README_completion_claim":False})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "paid natural FINAL retained before new globalization")

    try:
        for outer in range(args.outer):
            current_outer = outer
            check_time(deadline)
            if pending:
                proposal_peaks = old.merge_peaks(actual_peaks, pending)
                proposal_nodes = append_radial_nodes(actual_nodes,
                    [p["s"] for p in pending], par.length)
                if len(proposal_nodes)>args.maximum_radial_nodes or len(proposal_peaks)>args.maximum_extra_peaks:
                    status = "complete_physical_library_capacity_checkpoint"
                    break
                actual_nodes, actual_peaks = proposal_nodes, proposal_peaks
                current_full_library_values_known = False
                pending = []
                counts["physical_exchanges"] += 1
            if proposed_working:
                new_working, added, overflow = add_rows(working, proposed_working, args.maximum_working_rows)
                if overflow is not None:
                    status = "working_matrix_capacity_with_all_physical_rows_still_required"
                    break
                working, proposed_working = new_working, []
                counts["working_exchanges"] += bool(added)
            actual_trust = proposed_trust
            trust_decision_completed = False
            working = bind_working_radii(working, actual_nodes)
            coarse = fine = None
            outcome = None
            accepted_this_outer = 0
            last_checked_key = None
            backend_reason = "before_backend"
            seed_q = q.copy()
            counts["outer_started"] += 1
            try:
                coarse = ledger.create(par, actual_nodes, nt, args.point_batch_size)
                # This full value scan is needed to select this new matrix and
                # exposes every prior physical row. It is not an old fine replay.
                state = None
                if current_full_library_values_known:
                    # The terminal input kept exactly the same q and full
                    # library after seven completed required scans. Later this
                    # flag is retained only when q/library have not changed,
                    # or after complete current qualification.
                    counts["paid_current_complete_selection_replays_avoided"]+=1
                    phase="geometry_restoration" if best_geo>tolerance else "metric"
                    extra=retained_working_base_extra
                    seed={"complete_required_row_count":known_scalar_rows}
                    seed_proposal=[]
                else:
                    state = coarse.prepare(q)
                    seed = candidate_rows(coarse, state, actual_peaks, geo, "metric", best_eta+1e-8,
                                          args.working_witnesses_per_field)
                    counts["complete_coarse_scans"] += 1
                    geometry_min = min(v for k,v in seed["minimum_by_group"].items()
                                       if not k.startswith("metric_"))
                    phase = "geometry_restoration" if geometry_min < -tolerance else "metric"
                    if phase == "geometry_restoration":
                        best_geo = max(best_geo, -geometry_min)
                        extra = best_geo+.01
                        seed = candidate_rows(coarse, state, actual_peaks, geo, phase, extra,
                                              args.working_witnesses_per_field)
                        seed_proposal = seed["working_witnesses"]
                        # Metric rows are inactive in Phase I, never invalid fields.
                        working = [r for r in working if not r["field"].startswith("metric_")]
                    else:
                        extra = best_eta+args.pending_peak_tolerance+max(0.,
                            -seed["minimum_by_group"].get("metric_plus",0.),
                            -seed["minimum_by_group"].get("metric_minus",0.))
                        seed_proposal = seed["working_witnesses"]
                    known_scalar_rows=seed["complete_required_row_count"]
                    current_full_library_values_known=True
                    retained_working_base_extra=extra
                working, added, overflow = add_rows(working, seed_proposal, args.maximum_working_rows)
                if overflow is not None:
                    proposed_working = seed_proposal
                    status = "working_matrix_capacity_at_new_evidenced_selection"
                    break
                lower, upper = coarse.uniform.bounds()
                if q.shape != (81,) or np.any(q<lower-1e-12) or np.any(q>upper+1e-12):
                    raise ValueError("retained source violates unchanged physical boxes")
                scales = np.r_[np.full(2*coarse.uniform.block,.5),
                    np.full(par.radial_count,.2), np.full(par.radial_count,.15), .1]
                lo, hi = np.maximum(lower,q-actual_trust*scales), np.minimum(upper,q+actual_trust*scales)
                active_rows = WorkingRows(par,geo,working,nt,phase,args,deadline,ledger)
                del state
                x0 = np.r_[q,extra]
                fine_nodes = append_radial_nodes(actual_nodes,
                    np.r_[(actual_nodes[:-1]+actual_nodes[1:])/2,
                          np.linspace(0,par.length,2*args.radial_base-1)],par.length)
                # The full fine oracle is created only after a new trial passes every required coarse row.
                hard.emit("WORKING_ROWS_BACKEND_START", {"outer":outer,"phase":phase,
                    "q":q.tolist(),"backend_extra":extra,"actual_local_trust":actual_trust,
                    "complete_required_radial_nodes":len(actual_nodes),
                    "complete_required_peak_orbits":len(actual_peaks),
                    "complete_required_scalar_rows":seed["complete_required_row_count"],
                    "working_rows":working,"working_sub_radial_batches":
                    [o.uniform.s.tolist() for o,_,_,_ in active_rows.batches],
                    "full_fine_radial_nodes":len(fine_nodes),"full_fine_theta_nodes":2*nt,
                    "baseline_fine_observation_reused_from_identified_paid_START_or_last_acceptance":True})

                def callback(value, terminal=False):
                    nonlocal q,best_scan,best_observed,best_geo,best_eta,last_trial,last_checked_key
                    nonlocal pending,proposed_working,accepted_this_outer,backend_reason,fine
                    nonlocal last_raw_backend_trial,last_backtrack,current_full_library_values_known
                    nonlocal retained_working_base_extra
                    raw_v=np.asarray(value,dtype=float)
                    key=raw_v.tobytes()
                    if key==last_checked_key:
                        return
                    last_checked_key=key
                    check_time(deadline)
                    counts["backtrack_callback_proposals"]+=1
                    last_raw_backend_trial={"q":raw_v[:-1].tolist(),
                        "q_binary64_sha256":digest(raw_v[:-1].tobytes()),
                        "backend_extra":float(raw_v[-1]),"terminal_backend_point":terminal}
                    base_extra=retained_working_base_extra
                    base_q=q.copy()
                    last_backtrack={"base_actual_q":base_q.tolist(),
                        "base_actual_q_sha256":digest(base_q.tobytes()),"base_extra":base_extra,
                        "completed_trials":[],"pending_fraction":None,
                        "selected_fraction":None,"working_only_not_physical_acceptance":True}
                    selected=None
                    for backtrack in range(args.working_backtrack_steps+1):
                        check_time(deadline)
                        fraction=2.**(-backtrack)
                        v=raw_v.copy() if backtrack==0 else np.r_[
                            base_q+fraction*(raw_v[:-1]-base_q),
                            base_extra+fraction*(raw_v[-1]-base_extra)]
                        trial=v[:-1].copy()
                        last_backtrack["pending_fraction"]=fraction
                        last_trial={"q":trial.tolist(),"q_binary64_sha256":digest(trial.tobytes()),
                            "backend_extra":float(v[-1]),"outer":outer,"phase":phase,
                            "terminal_backend_point":terminal,"working_row_violation":None,
                            "accepted":False,"full_coarse_completed":False,"full_fine_completed":False,
                            "full_localization_completed":False,"working_backtrack_fraction":fraction}
                        local=active_rows.fun(v)
                        counts["backtrack_value_trials"]+=1
                        violation=float(max(0.,-np.min(local)))
                        last_trial["working_row_violation"]=violation
                        last_backtrack["completed_trials"].append({
                            "fraction":fraction,"working_violation":violation,
                            "backend_extra":float(v[-1])})
                        last_backtrack["pending_fraction"]=None
                        if violation<=tolerance:
                            selected=v
                            last_backtrack["selected_fraction"]=fraction
                            counts["backtrack_working_recoveries"]+=int(backtrack>0)
                            break
                    if selected is None:
                        counts["working_value_rejected_callbacks"]+=1
                        counts["backtrack_exhausted"]+=1
                        last_trial["reason"]="working_backtrack_exhausted_actual_state_retained"
                        # Actual coordinates and both pending libraries have
                        # not changed. A compact trial receipt avoids another
                        # copy of the full unchanged physical library.
                        hard.emit("WORKING_ROWS_BACKTRACK_REJECTED",{
                            "outer":outer,"phase":phase,"actual_q_sha256":digest(q.tobytes()),
                            "actual_local_trust":actual_trust,
                            "actual_required_radial_count":len(actual_nodes),
                            "actual_required_peak_count":len(actual_peaks),
                            "actual_pending_physical_count":len(pending),
                            "actual_pending_working_count":len(proposed_working),
                            "last_raw_backend_trial":last_raw_backend_trial,
                            "last_trial":last_trial,"backtrack":last_backtrack,"cost":costs()})
                        return
                    v=selected
                    trial=v[:-1].copy()
                    coarse_state=coarse.prepare(trial)
                    complete=candidate_rows(coarse,coarse_state,actual_peaks,geo,phase,float(v[-1]),
                        args.working_witnesses_per_field,working,True,tolerance)
                    counts["complete_coarse_scans"]+=1
                    last_trial.update(full_coarse_completed=True,
                        complete_required_minimum_by_group=complete["minimum_by_group"],
                        complete_required_scalar_rows=complete["complete_required_row_count"])
                    if complete["maximum_violation"]>tolerance:
                        counts["required_row_rejections"]+=1
                        proposed_working.extend(complete["working_witnesses"])
                        last_trial["reason"]="unrepresented_required_coarse_rows_rejected"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        if proposed_working:
                            backend_reason="required_coarse_row_exchange"
                            raise RestartWorking()
                        return
                    # Only a complete-coarse-feasible candidate spends a full
                    # fine/localizer qualification. No acceptance bypass exists.
                    if fine is None:
                        fine=ledger.create(par,fine_nodes,2*nt,args.point_batch_size)
                    fine_state=fine.prepare(trial)
                    scan=old.full_scan(fine,fine_state,mean_floor,det_floor)
                    counts["complete_fine_scans"]+=1
                    quadrature=old.quadrature_comparison(coarse_state.uniform_fields,fine_state,
                        coarse.uniform.s,fine.uniform.s,par.reach_target)
                    last_trial.update(full_fine_completed=True,full_fine_scan=scan,nested_quadrature=quadrature)
                    quadokay=max(quadrature[k] for k in (
                        "same_q_nested_FFT_metric_components_difference","same_q_relative_mean_E_difference",
                        "same_q_tau_curvature_difference"))<=args.nested_quadrature_tolerance
                    if not quadokay:
                        counts["nested_quadrature_rejections"]+=1
                        last_trial["reason"]="nested_full_FFT_difference_not_qualified"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        return
                    observed=old.locate_peaks(fine,fine_state,mean_floor,det_floor,margin,float(v[-1]),
                        deadline,args.angle_tolerance,args.peak_near_band,args.localizer_batch_size)
                    counts["localizer_candidates"]+=observed["candidate_count"]
                    counts["localizer_completed_candidates"]+=observed["completed_candidate_count"]
                    counts["localizer_point_objective_evaluations"]+=observed["evaluations"]
                    counts["localizer_unresolved_returns"]+=observed["unresolved_candidate_count"]
                    resolved=(observed["status"]=="observed_brackets_localized" and
                              observed["unresolved_candidate_count"]==0)
                    counts["complete_localizations"]+=int(resolved)
                    last_trial["full_localization_completed"]=resolved
                    last_trial["observed_peaks"]=old.compact_observation(observed)
                    observed_current=old.observation_metrics(scan,observed,margin)
                    geometry_peak=max(old.fine_geometry_limits(scan,margin).values())
                    for peak in observed["peaks"]:
                        if not peak["field"].startswith("metric_"):
                            geometry_peak=max(geometry_peak,float(peak["value"]))
                    limits={name:(float(v[-1]) if phase=="geometry_restoration" else 0.)
                            for name in scan["geometry_attainers"]}
                    limits.update(metric_plus=float(v[-1]),metric_minus=float(v[-1]))
                    grid=old.observed_grid_peaks(fine,fine_state,mean_floor,det_floor,margin,
                                                  limits,args.pending_peak_tolerance)
                    violations=[p for p in observed["peaks"]+grid
                        if p["value"]>limits.get(p["field"],0.)+args.pending_peak_tolerance
                        and (phase=="metric" or not p["field"].startswith("metric_"))]
                    additions=old.new_only(violations,actual_nodes,actual_peaks,nt)
                    pending=old.merge_peaks(pending,additions)
                    # All violating coordinates remain physical pending rows.
                    # Only the worst evidenced witnesses enter the next small
                    # matrix; every unselected violation still rejects here.
                    for name in sorted({p["field"] for p in violations}):
                        group=sorted([p for p in violations if p["field"]==name],
                                     key=lambda p:-p["value"])
                        selected_keys=set()
                        for p in group:
                            descriptor={"field":p["field"],"s":float(p["s"]),
                                "kind":"actual","theta":float(p["theta"]),
                                "evidence":{"source":"complete_fine_or_actual_angular_peak",
                                    "value":float(p["value"]),"q_binary64_sha256":digest(trial.tobytes())}}
                            key=row_key(descriptor)
                            if key not in selected_keys:
                                proposed_working.append(descriptor)
                                selected_keys.add(key)
                            if len(selected_keys)>=args.working_witnesses_per_field:
                                break
                    if not resolved:
                        last_trial["reason"]="incomplete_actual_peak_localization_rejected"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        raise hard.EndSegment("unresolved observed angular localization")
                    boundokay=(geometry_peak<=(float(v[-1]) if phase=="geometry_restoration" else 0.)+tolerance
                        and (phase=="geometry_restoration" or
                             observed_current["accepted_eta_max"]<=float(v[-1])+tolerance))
                    if not boundokay or violations:
                        counts["fine_required_row_rejections"]+=1
                        last_trial["reason"]="complete_fine_or_real_peak_epigraph_rejected"
                        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                        if additions or proposed_working:
                            backend_reason="complete_fine_actual_peak_exchange"
                            raise RestartWorking()
                        return
                    physicalokay=observed_current["accepted_geometry_violation_max"]<=tolerance
                    accepted=(geometry_peak<best_geo-1e-10 if phase=="geometry_restoration" else
                              physicalokay and observed_current["accepted_eta_max"]<best_eta-1e-12)
                    # Preserve a genuine successful restoration even below the
                    # usual improvement threshold, before emitting its checkpoint.
                    restored=phase=="geometry_restoration" and geometry_peak<=tolerance and physicalokay
                    accepted=accepted or restored
                    last_trial.update(actual_complete_geometry_margin_violation=max(0.,geometry_peak),
                        actual_complete_eta=observed_current["accepted_eta_max"],accepted=bool(accepted))
                    if accepted:
                        q=trial.copy();best_scan=observed_current;best_observed=old.compact_observation(observed)
                        best_geo=max(0.,geometry_peak);best_eta=observed_current["accepted_eta_max"]
                        accepted_this_outer+=1
                        counts["accepted_restoration_steps" if phase=="geometry_restoration" else "accepted_metric_steps"]+=1
                        current_full_library_values_known=True
                        retained_working_base_extra=float(v[-1])
                        if last_backtrack["selected_fraction"]<1:
                            counts["backtracked_fully_qualified_acceptances"]+=1
                        last_trial["reason"]="accepted_after_all_actual_constraints_and_old_qualification"
                    else:
                        last_trial["reason"]="complete_qualified_trial_without_strict_actual_improvement"
                    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                    if restored:
                        current_full_library_values_known=False
                        backend_reason="complete_geometry_restoration_reached"
                        raise RestartWorking()
                    if accepted and last_backtrack["selected_fraction"]<1:
                        backend_reason="backtracked_complete_acceptance_restart_at_actual_state"
                        raise RestartWorking()

                try:
                    backend_reason="inside_SLSQP"
                    outcome=minimize(lambda v:float(v[-1]),x0,jac=lambda v:np.r_[np.zeros(81),1.],
                        method="SLSQP",bounds=list(zip(np.r_[lo,0.],np.r_[hi,np.inf])),
                        constraints={"type":"ineq","fun":active_rows.fun,"jac":active_rows.jac},
                        callback=callback,options={"ftol":1e-9,"maxiter":args.maxiter,"disp":False})
                    counts["backend_natural_returns"]+=1
                    last_backend=old.backend_record(outcome)
                    backend_reason="natural_backend_return"
                    callback(outcome.x,terminal=True)
                except RestartWorking:
                    pass
                if accepted_this_outer and float(np.max(abs(q-seed_q)/scales))>=.9*actual_trust:
                    proposed_trust=min(args.maximum_trust,1.5*actual_trust)
                elif not accepted_this_outer and not pending and not proposed_working and outcome is not None:
                    proposed_trust=max(args.minimum_trust,.5*actual_trust)
                else:
                    proposed_trust=actual_trust
                trust_decision_completed=True
                counts["outer_completed"]+=1
                snapshot("WORKING_ROWS_OUTER_COMPLETE",backend_reason)
                if (outcome is not None and not accepted_this_outer and not pending and not proposed_working
                        and actual_trust<=args.minimum_trust):
                    status="minimum_trust_without_actual_complete_improvement"
                    break
            finally:
                if active_rows is not None:
                    c=active_rows.counts
                    counts["working_value_keys"]+=c["value_keys"]
                    counts["working_complete_jacobians"]+=c["complete_jacobians"]
                    counts["working_direction_blocks"]+=c["direction_blocks"]
                    counts["working_jacobian_seconds"]+=c["jacobian_seconds"]
                    active_rows.close();active_rows=None
                ledger.retire(coarse);ledger.retire(fine)
    except hard.EndSegment as error:
        status="cooperative_clock_or_unresolved_localizer_checkpoint"
        hard.emit("WORKING_ROWS_STOP",{"type":type(error).__name__,"message":str(error)})
    except Exception as error:
        status="explicit_backend_exception_checkpoint"
        hard.emit("WORKING_ROWS_STOP",{"type":type(error).__name__,"message":str(error)})
    finally:
        snapshot("WORKING_ROWS_FINAL",status)


if __name__ == "__main__":
    main()
