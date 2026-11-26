#!/usr/bin/env python3
"""Continue real bb921 B030, completing saved brackets and lifting only auxiliary e.

Keep the same SLSQP/BFGS history after a shortened step passes every original
physical gate. The raw backend iterate remains its own optimizer point;
the accepted shortened q is recorded only as the independent physical best.
Actual row/library exchanges, phase changes, or natural termination still
restart the backend. No prior unreported work arrays are claimed restored.
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
BACKTRACK_PARENT_SHA="3005270b7b247895f49ce249193d22e3db035dafb1fdb4aea00a7a0119eebd8e"
if hashlib.sha256(Path(__file__).with_name("r566_working_rows_backtrack_20261126.py").read_bytes()).hexdigest()!=BACKTRACK_PARENT_SHA:
    raise RuntimeError("paid natural-backtrack parent source changed")
import r566_working_rows_backtrack_20261126 as backtrack_parent
BACKEND_PARENT_SHA="8cf64c40015350fca09dca3194b6c081078210d4d9146d9369922e8be7cc6930"
if hashlib.sha256(Path(__file__).with_name("r566_backend_preserving_backtrack_20261127.py").read_bytes()).hexdigest()!=BACKEND_PARENT_SHA:
    raise RuntimeError("actual backend-history source changed")
import r566_backend_preserving_backtrack_20261127 as backend_parent
SAVED_BRACKETS_HELPER_SHA="5ba4aaa134135ce871a76d0aafe2c6161789e41fac20dc1ef26aecb9bf2000e5"
if hashlib.sha256(Path(__file__).with_name("r566_saved_brackets_and_epigraph_20261127.py").read_bytes()).hexdigest()!=SAVED_BRACKETS_HELPER_SHA:
    raise RuntimeError("declared saved-bracket and epigraph helper changed")
from r566_saved_brackets_and_epigraph_20261127 import (
    lift_epigraph,minimum_by_group as grouped_minimum,geometry_minimum,metric_minimum,
    localize_saved_brackets,
)
SCHEMA="r566-actual-bb921-saved-brackets-and-physical-epigraph-v1"


def source_input(args):
    source=json.loads(args.source_state_json)
    if source.get("schema")!="r566-realbb921-full-epigraph-and-saved-brackets-v1":
        raise ValueError("wrong identified actual B030 epigraph input")
    expected={"run_id":45883086225,"job_id":140126984773,
        "source_commit":"7923e588c07cd47852dfdf4604db5bc8246ce92d",
        "runtime_pull_commit":"dddd38c1c6628ad6f448ebbfe2dbee0892559e64",
        "source_sha256":BACKEND_PARENT_SHA,"raw_stdout_bytes":21831112,
        "raw_stdout_sha256":"86b6cfc91026975192da40e960b356680c09f3da5c227a37941ce013f59f4916",
        "FINAL_JSON_bytes":529571,
        "FINAL_JSON_sha256":"7f71616f8fe94fd1c58889a4e64d66b8253dd6ffef35c75549ffbf70760ae406",
        "partial_JSON_bytes":305148,
        "partial_JSON_sha256":"7ff97bef28f0039ddd6c05ec21cb739debc59cc2b32fd5d6f22c7b00f5573915"}
    if source["origin"]!=expected:
        raise ValueError("actual source terminal or unfinished localization differs")
    relative="topics/visible-flex-new-mechanism/computations/request-r566-backend-preserving-20261127.json"
    repository=Path(__file__).resolve().parents[3]
    request_bytes=(repository/relative).read_bytes()
    if len(request_bytes)!=237146 or digest(request_bytes)!="9e3f3c1ca953392f017671868ce16bf8fc2b34ac612d2948f5f459b274a2092e":
        raise ValueError("paid parent history request changed")
    request=json.loads(request_bytes)
    old_args=argparse.Namespace(**vars(args))
    old_args.source_state_json=request["lanes"]["rounded-core-B030-backend-history"]["source_state_json"]
    parent,ancestor,old_start,par,geo,old_q,old_nodes,old_peaks,nt,old_trust,old_terminal=backend_parent.source_input(old_args)
    encoded=source["complete_original_FINAL_JSON"].encode()
    if len(encoded)!=expected["FINAL_JSON_bytes"] or digest(encoded)!=expected["FINAL_JSON_sha256"]:
        raise ValueError("complete original source FINAL changed")
    terminal=json.loads(encoded)
    q=np.asarray(terminal["actual_retained_q"],dtype=float)
    nodes=np.asarray(terminal["actual_complete_required_radial_nodes"],dtype=float)
    peaks=terminal["actual_complete_required_peak_orbits"]
    counts=terminal["cost"]["counts"]
    if (q.shape!=(81,) or not np.all(np.isfinite(q))
            or digest(q.tobytes())!="bb921f60d02a3624552d79ebc623e3eb3306b174d981a3ca794a57b44d8edaa4"
            or terminal["actual_q_binary64_sha256"]!=digest(q.tobytes())
            or (len(nodes),len(peaks),nt)!=(605,1355,1536)
            or len(terminal["actual_working_field_orbit_rows"])!=463
            or len(terminal["recorded_unapplied_physical_peak_orbits"])!=1
            or len(terminal["recorded_unapplied_working_rows"])!=1
            or terminal["actual_backend_local_trust"]!=.3003387451171875
            or terminal["proposed_next_local_trust"]!=.3003387451171875
            or terminal["post_backend_trust_decision_completed"] is not False
            or terminal["phase"]!="metric" or counts["accepted_metric_steps"]!=19
            or counts["working_complete_jacobians"]!=48
            or terminal["retained_working_feasible_base_extra"]!=.24394604211718696
            or terminal["actual_retained_qualification"]["accepted_eta_max"]!=.24394558845134018):
        raise ValueError("actual complete source physical state/costs/trust differs")
    trial=terminal["last_trial_not_implicitly_accepted"]
    saved=trial["observed_peaks"]
    scope=source["saved_localizer_scope"]
    if (trial["q_binary64_sha256"]!="bc9b991faee4beb81b91cbdc834aae6dbdcb1be951d803386f787c97430df097"
            or not trial["full_coarse_completed"] or not trial["full_fine_completed"]
            or trial["full_localization_completed"] or trial["accepted"]
            or saved["completed_candidate_count"]!=0 or saved["unresolved_candidate_count"]!=1353
            or len(saved["remaining_unprocessed_candidates"])!=1353
            or scope["q_binary64_sha256"]!=trial["q_binary64_sha256"]
            or scope["oracle_identity"]!=saved["oracle_identity"]
            or len(scope["full_observation_radial_nodes"])!=1212
            or scope["full_observation_FFT_nodes"]!=3072
            or scope["unresolved_candidate_count"]!=1353
            or source["source_last_backend_required_scalar_rows"]!=2151130
            or source["source_last_backend_extra"]!=terminal["retained_working_feasible_base_extra"]):
        raise ValueError("source unfinished trial or complete fine/localizer scope changed")
    fine_nodes=np.asarray(scope["full_observation_radial_nodes"],dtype=float)
    trial_q=np.asarray(trial["q"],dtype=float)
    anchor=terminal["current_backend_anchor_and_working_library"]
    if (digest(fine_nodes.tobytes())!="29db161be6a30bbe07ce8e28c30160fe1982aacf1d8ec4a79262364140afc2d1"
            or not set(nodes.tolist()).issubset(fine_nodes.tolist())
            or digest(trial_q.tobytes())!=trial["q_binary64_sha256"]
            or np.any(trial_q<np.asarray(anchor["fixed_lower_physical_box"])-1e-12)
            or np.any(trial_q>np.asarray(anchor["fixed_upper_physical_box"])+1e-12)):
        raise ValueError("source original fine coordinates or physical-box qualification differs")
    source["source_cost_ledger"]={"source_run":45883086225,"source_job":140126984773,
        "complete_actual_source_cost":terminal["cost"],
        "recorded_chain_scientific_seconds_lower_bound":
            terminal["cost"]["prior_cost_ledger"]["recorded_chain_scientific_seconds_lower_bound"]
            +terminal["cost"]["elapsed_seconds"],
        "recorded_chain_scientific_seconds_is_exact":False,
        "earlier_censored_work_still_unknown":True,"metadata_recovery_scientific_evaluations":0}
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
    actual_fine_nodes=np.asarray(source["saved_localizer_scope"]["full_observation_radial_nodes"],dtype=float)
    best_fine_nodes=actual_fine_nodes.copy()
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
        "backend_histories_continued_after_shortened_full_acceptance":0,
        "paid_current_complete_selection_replays_avoided":0,
        "working_epigraph_lifts":0,"complete_coarse_epigraph_lifts":0,"complete_fine_epigraph_lifts":0,
        "original_working_rechecks_after_lift":0,"source_saved_localizations_completed":0,
        "source_saved_trial_fully_qualified_acceptances":0,"source_paid_full_fine_and_nested_reports_reused":0}
    last_trial = last_backend = None
    last_raw_backend_trial = last_backtrack = None
    current_full_library_values_known = True
    known_scalar_rows = source["source_last_backend_required_scalar_rows"]
    retained_working_base_extra = source["source_last_backend_extra"]
    active_rows = None
    current_outer, phase = -1, "metric"
    backend_anchor_state=None
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
            "actual_required_fine_radial_nodes":actual_fine_nodes.tolist(),
            "actual_required_fine_radial_nodes_binary64_sha256":digest(actual_fine_nodes.tobytes()),
            "retained_qualification_fine_radial_nodes":best_fine_nodes.tolist(),
            "retained_qualification_fine_radial_nodes_binary64_sha256":digest(best_fine_nodes.tobytes()),
            "all_source_and_new_fine_radial_coordinates_retained_exactly":True,
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
            "current_backend_anchor_and_working_library":backend_anchor_state,
            "raw_backend_and_retained_physical_best_are_distinct_tracks":True,
            "source_internal_BFGS_arrays_not_recovered":True,
            "current_complete_library_values_known_for_retained_q":current_full_library_values_known,
            "retained_working_feasible_base_extra":retained_working_base_extra,
            "cost":costs(), "no_physical_row_removed_by_working_selection":True,
            "continuous_geometry_reach_or_README_completion_claim":False})

    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION", {"schema":SCHEMA, "source_state":source,
        "source_state_sha256":digest(raw), "physical_parameters":asdict(par), "geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "original605_rings1355_orbits463_working_rows_and_two_pending_retained":True,
        "source19_acceptances48_Jacobians_and35_complete_localizations_not_replayed":True,
        "source1353_unprocessed_saved_brackets_completed_before_new_backend":True,
        "metric_auxiliary_epigraph_lift_never_counts_as_actual_eta_improvement":True,
        "new_unrepresented_peaks_are_preserved_even_when_epigraph_is_lifted":True,
        "new_unrepresented_coarse_working_witnesses_survive_the_auxiliary_lift":True,
        "old_fine1212_and_every_subsequent_fine_grid_are_permanently_retained":True,
        "source_internal_BFGS_work_arrays_were_not_output_or_restored":True,
        "new_SLSQP_history_continues_when_only_a_separate_shortened_physical_best_changes":True,
        "raw_backend_iterates_remain_the_unchanged_optimizer_sequence":True,
        "genuine_row_exchange_phase_change_or_natural_return_still_restarts_backend":True,
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
        # Complete the ORIGINAL unfinished trial on its original physical
        # library before adopting pending changes. Its full coarse/fine and
        # nested reports were paid; only its saved brackets remain new work.
        source_trial=terminal["last_trial_not_implicitly_accepted"]
        scope=source["saved_localizer_scope"]
        trial=np.asarray(source_trial["q"],dtype=float)
        prior_fine=ledger.create(par,np.asarray(scope["full_observation_radial_nodes"]),
                                scope["full_observation_FFT_nodes"],args.point_batch_size)
        try:
            prior_state=prior_fine.prepare(trial)
            observed=localize_saved_brackets(prior_fine,prior_state,
                source_trial["observed_peaks"]["remaining_unprocessed_candidates"],scope,
                mean_floor,det_floor,margin,deadline,args.angle_tolerance,args.localizer_batch_size)
            counts["localizer_candidates"]+=observed["candidate_count"]
            counts["localizer_completed_candidates"]+=observed["completed_candidate_count"]
            counts["localizer_point_objective_evaluations"]+=observed["evaluations"]
            counts["localizer_unresolved_returns"]+=observed["unresolved_candidate_count"]
            resolved=(observed["status"]=="observed_brackets_localized" and observed["unresolved_candidate_count"]==0)
            counts["complete_localizations"]+=int(resolved)
            counts["source_saved_localizations_completed"]+=int(resolved)
            counts["source_paid_full_fine_and_nested_reports_reused"]+=1
            last_trial=dict(source_trial)
            last_trial.update(full_localization_completed=resolved,
                observed_peaks=old.compact_observation(observed),
                old_full_coarse_fine_and_nested_reports_reused_by_identical_q_and_scope=True,
                new_necessary_oracle_FFT_preparation_is_charged=True,
                source_unfinished_trial_is_not_a_new_raw_SLSQP_point=True)
            scan=source_trial["full_fine_scan"]
            qualified=old.observation_metrics(scan,observed,margin)
            geometry_peak=max(old.fine_geometry_limits(scan,margin).values())
            for peak in observed["peaks"]:
                if not peak["field"].startswith("metric_"):
                    geometry_peak=max(geometry_peak,float(peak["value"]))
            old_extra=float(source_trial["backend_extra"])
            # Preserve every newly resolved source violation as an actual
            # library proposal even if a larger independent e now covers it.
            evidence=[p for p in observed["peaks"] if p["value"]>
                (old_extra if p["field"].startswith("metric_") else 0.)+args.pending_peak_tolerance]
            pending=old.merge_peaks(pending,old.new_only(evidence,actual_nodes,actual_peaks,nt))
            for name in sorted({p["field"] for p in evidence}):
                for p in sorted([p for p in evidence if p["field"]==name],key=lambda p:-p["value"])[:args.working_witnesses_per_field]:
                    proposed_working.append({"field":p["field"],"s":float(p["s"]),"kind":"actual","theta":float(p["theta"]),
                        "evidence":{"source":"completed_original_saved_bracket","value":float(p["value"]),
                                    "q_binary64_sha256":digest(trial.tobytes())}})
            if not resolved:
                last_trial["reason"]="source_saved_localization_still_incomplete_not_accepted"
                snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                raise hard.EndSegment("source saved actual localization unresolved")
            lifted,amount=lift_epigraph(np.r_[trial,old_extra],qualified["accepted_eta_max"]-old_extra)
            # The paid working and complete-coarse rows all passed at the
            # SAME q and smaller old e. Their metric rows are e-value and
            # hence monotone; physical rows and original boxes do not change.
            inherited_rows_okay=(source_trial["working_row_violation"]<=tolerance and
                min(source_trial["complete_required_minimum_by_group"].values())>=-tolerance)
            nested=source_trial["nested_quadrature"]
            nested_okay=max(nested[k] for k in ("same_q_nested_FFT_metric_components_difference",
                "same_q_relative_mean_E_difference","same_q_tau_curvature_difference"))<=args.nested_quadrature_tolerance
            accepted=(inherited_rows_okay and nested_okay and geometry_peak<=tolerance and
                qualified["accepted_geometry_violation_max"]<=tolerance and
                qualified["accepted_eta_max"]<=float(lifted[-1])+tolerance and
                qualified["accepted_eta_max"]<best_eta-1e-12)
            last_trial.update(backend_extra=float(lifted[-1]),separate_auxiliary_epigraph_lift=amount,
                accepted=bool(accepted),actual_complete_eta=qualified["accepted_eta_max"],
                actual_complete_geometry_margin_violation=max(0.,geometry_peak),
                paid_complete_rows_at_lower_e_imply_same_q_rows_at_lifted_e=True)
            if accepted:
                q=trial.copy();best_scan=qualified;best_observed=old.compact_observation(observed)
                best_fine_nodes=actual_fine_nodes.copy()
                best_eta=qualified["accepted_eta_max"];best_geo=max(0.,geometry_peak)
                retained_working_base_extra=float(lifted[-1]);current_full_library_values_known=True
                counts["accepted_metric_steps"]+=1
                counts["source_saved_trial_fully_qualified_acceptances"]+=1
            last_trial["reason"]="source_saved_trial_completed_and_qualified" if accepted else "source_saved_trial_completed_but_not_accepted"
            snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
        finally:
            ledger.retire(prior_fine)
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
                    # library after the recorded final full qualification. Later this
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
                backend_anchor_state={"outer":outer,"phase":phase,
                    "initial_q_binary64_sha256":digest(q.tobytes()),
                    "initial_epigraph":extra,"actual_trust":actual_trust,
                    "fixed_lower_physical_box":lo.tolist(),"fixed_upper_physical_box":hi.tolist(),
                    "working_rows":len(working),
                    "new_SLSQP_call_internal_history_not_inherited_from_source":True}
                # Keep exact old fine coordinates even when a later physical
                # insertion changes adjacent midpoints. The current coarse
                # floats also stay exact for the nested same-q comparison.
                fresh_fine=append_radial_nodes(actual_nodes,
                    np.r_[(actual_nodes[:-1]+actual_nodes[1:])/2,
                          np.linspace(0,par.length,2*args.radial_base-1)],par.length)
                actual_fine_nodes=np.asarray(sorted(set(actual_fine_nodes.tolist())|
                    set(fresh_fine.tolist())|set(actual_nodes.tolist())),dtype=float)
                fine_nodes=actual_fine_nodes
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
                    nonlocal retained_working_base_extra,best_fine_nodes
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
                            "terminal_backend_point":terminal and backtrack==0,
                            "source_is_terminal_backend_point":terminal,"working_row_violation":None,
                            "accepted":False,"full_coarse_completed":False,"full_fine_completed":False,
                            "full_localization_completed":False,"working_backtrack_fraction":fraction}
                        local=active_rows.fun(v)
                        counts["backtrack_value_trials"]+=1
                        before_groups=grouped_minimum(active_rows.rows,local)
                        if backtrack==0:
                            last_raw_backend_trial["working_minimum_by_group"]=before_groups
                        box_violation=float(max(0.,np.max(lo-trial),np.max(trial-hi)))
                        lift=0.
                        if phase=="metric" and max(0.,-geometry_minimum(before_groups),box_violation)<=tolerance:
                            v,lift=lift_epigraph(v,-metric_minimum(before_groups))
                            if lift:
                                local=active_rows.fun(v)
                                counts["original_working_rechecks_after_lift"]+=1
                                counts["working_epigraph_lifts"]+=1
                        minimum_by_group=grouped_minimum(active_rows.rows,local)
                        violation=float(max(0.,-np.min(local),box_violation))
                        last_trial.update(backend_extra=float(v[-1]),working_row_violation=violation,
                            working_minimum_by_group=minimum_by_group,physical_box_violation=box_violation,
                            separate_working_epigraph_lift=lift,raw_backend_array_not_modified=True,
                            physical_q_unchanged_by_epigraph_lift=True)
                        last_backtrack["completed_trials"].append({
                            "fraction":fraction,"working_violation":violation,
                            "minimum_by_group":minimum_by_group,
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
                    if phase=="metric" and geometry_minimum(complete["minimum_by_group"])>=-tolerance:
                        v,lift=lift_epigraph(v,-metric_minimum(complete["minimum_by_group"]))
                        if lift:
                            # An auxiliary lift preserves feasibility but must
                            # not hide the newly evidenced actual model rows.
                            proposed_working.extend(complete["working_witnesses"])
                            local=active_rows.fun(v)
                            counts["original_working_rechecks_after_lift"]+=1
                            if np.min(local)<-tolerance:
                                raise ArithmeticError("lifted same-q complete-coarse e failed original working rows")
                            complete=candidate_rows(coarse,coarse_state,actual_peaks,geo,phase,float(v[-1]),
                                args.working_witnesses_per_field,working,True,tolerance)
                            counts["complete_coarse_scans"]+=1
                            counts["complete_coarse_epigraph_lifts"]+=1
                            last_trial.update(backend_extra=float(v[-1]),separate_complete_coarse_epigraph_lift=lift)
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
                    evidence_extra=float(v[-1])
                    if resolved and phase=="metric" and geometry_peak<=tolerance:
                        v,lift=lift_epigraph(v,observed_current["accepted_eta_max"]-float(v[-1]))
                        if lift:
                            local=active_rows.fun(v)
                            counts["original_working_rechecks_after_lift"]+=1
                            complete=candidate_rows(coarse,coarse_state,actual_peaks,geo,phase,float(v[-1]),
                                args.working_witnesses_per_field,working,True,tolerance)
                            counts["complete_coarse_scans"]+=1
                            if np.min(local)<-tolerance or complete["maximum_violation"]>tolerance:
                                raise ArithmeticError("fine epigraph lift failed original same-q complete rows")
                            counts["complete_fine_epigraph_lifts"]+=1
                            last_trial.update(backend_extra=float(v[-1]),separate_complete_fine_epigraph_lift=lift,
                                complete_required_minimum_by_group=complete["minimum_by_group"],
                                complete_required_scalar_rows=complete["complete_required_row_count"])
                    limits={name:(float(v[-1]) if phase=="geometry_restoration" else 0.)
                            for name in scan["geometry_attainers"]}
                    limits.update(metric_plus=float(v[-1]),metric_minus=float(v[-1]))
                    evidence_limits=dict(limits,metric_plus=evidence_extra,metric_minus=evidence_extra)
                    grid=old.observed_grid_peaks(fine,fine_state,mean_floor,det_floor,margin,
                                                  evidence_limits,args.pending_peak_tolerance)
                    violations=[p for p in observed["peaks"]+grid
                        if p["value"]>limits.get(p["field"],0.)+args.pending_peak_tolerance
                        and (phase=="metric" or not p["field"].startswith("metric_"))]
                    exchange_evidence=[p for p in observed["peaks"]+grid
                        if p["value"]>evidence_limits.get(p["field"],0.)+args.pending_peak_tolerance
                        and (phase=="metric" or not p["field"].startswith("metric_"))]
                    additions=old.new_only(exchange_evidence,actual_nodes,actual_peaks,nt)
                    pending=old.merge_peaks(pending,additions)
                    # All violating coordinates remain physical pending rows.
                    # Only the worst evidenced witnesses enter the next small
                    # matrix; every unselected violation still rejects here.
                    for name in sorted({p["field"] for p in exchange_evidence}):
                        group=sorted([p for p in exchange_evidence if p["field"]==name],
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
                        best_fine_nodes=fine_nodes.copy()
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
                    if additions or proposed_working:
                        current_full_library_values_known=False
                        backend_reason="complete_fine_peak_exchange_preserved_after_epigraph_lift"
                        raise RestartWorking()
                    if accepted and last_backtrack["selected_fraction"]<1:
                        # SLSQP keeps its OWN raw x, gradients and quasi-Newton
                        # arrays. The certified physical best is a separate
                        # record; it is not written into those arrays or x.
                        # All future backtracks still use its truly feasible
                        # q/extra and must pass the unchanged full gates.
                        counts["backend_histories_continued_after_shortened_full_acceptance"]+=1
                        backend_reason="shortened_physical_best_updated_same_SLSQP_history_continues"
                        hard.emit("WORKING_ROWS_BACKEND_HISTORY_CONTINUES",{
                            "outer":outer,"phase":phase,
                            "raw_backend_q_sha256":last_raw_backend_trial["q_binary64_sha256"],
                            "actual_retained_q_sha256":digest(q.tobytes()),
                            "accepted_backtrack_fraction":last_backtrack["selected_fraction"],
                            "actual_complete_eta":best_eta,
                            "backend_anchor":backend_anchor_state,
                            "raw_backend_array_was_not_modified":True,
                            "same_working_rows_bounds_and_SLSQP_call":True,
                            "internal_BFGS_work_arrays_remain_owned_by_running_SLSQP":True,
                            "new_physical_best_is_not_claimed_as_its_raw_iterate":True})

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
