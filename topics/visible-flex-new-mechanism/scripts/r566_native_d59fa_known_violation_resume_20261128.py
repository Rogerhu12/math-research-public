#!/usr/bin/env python3
"""Reject the already disproved source trial and resume actual d59fa B030.

The paid curvature-plus violation already falsifies its original restoration
acceptance. Preserve all 4465 completed peaks and the 8635 UNEXECUTED brackets
in the necessary source input, without claiming completed localization. Apply
both original pending rows to retained d59fa using the unchanged normal loop.
Complete the old zero-acceptance outer's original trust decision: pending
exchange keeps trust unchanged. New trials still require every original full
physical gate. Exact g/origin and restoration H semantics are preserved.
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
original_minimize=previous.minimize
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
SAVED_BRACKETS_HELPER_SHA="79fb5b0433f77164481d4ba067ff44fdc4829cd95319b6ab0448cacc8c4bbc8d"
if hashlib.sha256(Path(__file__).with_name("r566_saved_partial_queue_20261127.py").read_bytes()).hexdigest()!=SAVED_BRACKETS_HELPER_SHA:
    raise RuntimeError("declared paid-prefix bracket helper changed")
from r566_saved_partial_queue_20261127 import (
    localize_saved_brackets,lift_epigraph,minimum_by_group as grouped_minimum,geometry_minimum,metric_minimum,
)
EPIGRAPH_PARENT_SHA="f5aa6c45a9d56b2f55eb12e33ae4223d5bbf737c7edcfe5a27f5ad0cea7d0911"
if hashlib.sha256(Path(__file__).with_name("r566_physical_epigraph_and_saved_resume_20261127.py").read_bytes()).hexdigest()!=EPIGRAPH_PARENT_SHA:
    raise RuntimeError("actual prior physical-epigraph implementation changed")
import r566_physical_epigraph_and_saved_resume_20261127 as epigraph_parent
PARTIAL391_PARENT_SHA="8c0a1300f75261b703cfeafd636e9b659f6436f67942ccb4e14d623c86dd8f38"
if hashlib.sha256(Path(__file__).with_name("r566_partial391_physical_resume_20261127.py").read_bytes()).hexdigest()!=PARTIAL391_PARENT_SHA:
    raise RuntimeError("actual completed partial391 source changed")
import r566_partial391_physical_resume_20261127 as partial391_parent
NORMAL56E8_PARENT_SHA="def9207558641dc38f6bef4a9e8058673b13ea27b225428000355e6d66425f9d"
if hashlib.sha256(Path(__file__).with_name("r566_normal56e8_physical_resume_20261127.py").read_bytes()).hexdigest()!=NORMAL56E8_PARENT_SHA:
    raise RuntimeError("actual completed normal56e8 source changed")
import r566_normal56e8_physical_resume_20261127 as normal56e8_parent
TRUE_SECANT_SHA="76c38d9ebdb51698d115d667adb7ab33cc2d1b18af99697f1a0e1058e6b27a0f"
if hashlib.sha256(Path(__file__).with_name("r566_true_secant_curvature_20261127.py").read_bytes()).hexdigest()!=TRUE_SECANT_SHA:
    raise RuntimeError("reviewed native curvature implementation changed")
from r566_true_secant_curvature_20261127 import TrueSecantSLSQP
NATIVE_D191_PARENT_SHA="23a5e6df8de9ec8bafa60e8e7527038b2961fe03fe8e2b293f07232a9b7c9fbf"
if hashlib.sha256(Path(__file__).with_name("r566_native_d191_partial238_20261127.py").read_bytes()).hexdigest()!=NATIVE_D191_PARENT_SHA:
    raise RuntimeError("actual completed native source changed")
import r566_native_d191_partial238_20261127 as native_parent
MARGIN_STATE_SHA="ee963a595d611484b2459a51ed7ae0d702e18a0900f8c01d5e95f4d80c7b0491"
if hashlib.sha256(Path(__file__).with_name("r566_original_margin_rounding_state_20261127.py").read_bytes()).hexdigest()!=MARGIN_STATE_SHA:
    raise RuntimeError("original missing-margin interpretation changed")
from r566_original_margin_rounding_state_20261127 import OriginalMarginState


class OriginalMarginUnresolved(hard.EndSegment):
    """The original unprinted scalar does not determine one original decision."""


NATIVE56594_PARENT_SHA="c972c56133ff68705a91434d5ceeb404d5d7fe818d2cf168e2ac2b29efdfa09a"
if hashlib.sha256(Path(__file__).with_name("r566_native56594_partial2561_20261127.py").read_bytes()).hexdigest()!=NATIVE56594_PARENT_SHA:
    raise RuntimeError("the actual completed partial2561 native source changed")

NATIVE_CC117_PARENT_SHA="f73dc0614460d526ab05623f982a667c15bee883ce619e4d8b2ee839b9732313"
if hashlib.sha256(Path(__file__).with_name("r566_native_cc117_normal_resume_20261127.py").read_bytes()).hexdigest()!=NATIVE_CC117_PARENT_SHA:
    raise RuntimeError("the actual cc117 source implementation changed")

SCHEMA="r566-actuald59fa-known-violation-normal-resume-v1"
# These complete row-function sources, par/geo, phase, and FFT count define the
# secant semantics.  Variable q and the current subset of rows are not constants.
CURVATURE_MODEL_IDENTITY={
    "physical_family":"original_B030_81q_static_metric_design",
    "objective":"original_physical_auxiliary_epigraph",
    "physical_parameter_order":"original_B030_81q_then_epigraph",
    "physical_field_and_original_metric_row_recipe":{
        "inverse_flat_oscillatory_tail_20261126.py":"b9c778fbeafb0d9beb061b3f472b8db1661daec5a78a63eb886a8e4770574f9b",
        "inverse_rotational_metric_20261126.py":"e25dff6a411e8edc485babe6545087cfbea2b6d16cd804e6dcb51f17d8fab319",
        "inverse_r566_angular_oracle_20261126.py":"46eea6c6da4a94c82106e8a57ff98e70bf8f85bd2d0ef35c26cb649a0ee2f0a7",
        "inverse_r566_block_jacobian_20261126.py":"c0ab647ed2c6c0647c9031995696d40bc2c6717b893f67cf7c6a345c5366ef6b",
        "inverse_hard_exchange_20261126.py":"304989b5b127e3d761a243aed55ca437d86012f2cd6e3357c291e1159bf48271",
        "inverse_hard_exchange_resume_20261126.py":"befd444bfb96efc6721d1b0bad20deb25b32e915c1f789ab4d285085c2afcce4",
        "inverse_r566_theta_peak_exchange_20261126.py":"6094c15ff2696d6b64e9eac09ce60b54a59a64c545cb88fb7734df8bb185f757",
        "inverse_r566_theta_peak_resume_20261126.py":"0093d8ce3b80600a6b4eb0d921208423ca390cbc957497b026d8ef230355aaa1",
        "inverse_r566_theta_peak_batched_20261126.py":"ff24fbe2e74a8caf15b78defae454eb36280c310c725a8f9d7a623a511811140",
        "inverse_r566_theta_peak_checkpoint_20261126.py":"a879573a4dbfd1a58ff7a25e07ac7d03a41916edac250116348dc008b7542a27",
        "inverse_r566_theta_peak_radial1025_20261126.py":"7e05899998ff166808caf821091ab2db4abdbfcd3b4923f02b5907d057a35ad1",
        "inverse_r566_theta_peak_paid_resume_20261126.py":"cc1a1fa3fdca03d1b15fcd2ee6151133a64ab64a571f20990c1f029d5babc1b0",
        "r566_working_rows_full_acceptance_20261126.py":PREVIOUS_SHA},
    "actual_parameters_geometry_phase_and_FFT_added_from_same_WorkingRows":True,
    "variable_q_is_not_frozen_in_the_row_function_identity":True,
    "metric_changes_during_static_design":True}



def source_input(args):
    source=json.loads(args.source_state_json)
    if source.get("schema")!="r566-reald59fa-known-violation-source-v1":
        raise ValueError("wrong identified actual B030 partial-queue input")
    expected={"run_id":45930250772,"job_id":140280968908,
        "source_commit":"e553b6fb567f73b58b128fd263d4211d4cb5d5d5",
        "runtime_pull_commit":"e553b6fb567f73b58b128fd263d4211d4cb5d5d5",
        "source_sha256":NATIVE_CC117_PARENT_SHA,
        "request_gzip_sha256":"63ec7925b08d83e9ae0d07ee72667a0eb02a875e76c9fe5043dc307ea5e9fb4b",
        "raw_stdout_bytes":25649794,
        "raw_stdout_sha256":"0bfdb4bda0c89af035fe930b5d9ddb127394d0a1ef80dee55c012d2b2f641d49",
        "FINAL_JSON_bytes":2225283,
        "FINAL_JSON_sha256":"2ce6b8cc73460eb47114727b9bd404898929f09301fbac6b505e802a7146c3e9",
        "partial_JSON_bytes":2605180,
        "partial_JSON_sha256":"789b49688329af748b4288c80e82d5186f361aec7ed5950e325cae5ef2735652"}
    if source["origin"]!=expected:
        raise ValueError("actual source terminal or partial queue differs")
    encoded=source["complete_original_FINAL_JSON"].encode()
    if len(encoded)!=expected["FINAL_JSON_bytes"] or digest(encoded)!=expected["FINAL_JSON_sha256"]:
        raise ValueError("complete original source FINAL changed")
    terminal=json.loads(encoded)
    def canonical_bytes(value):
        return json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    if (digest(canonical_bytes(source["physical_parameters"]))!=
            "4fa67643c13c83e4968938a0185720522c5fb7e1349bb26c78c4af2e27f33798"
            or digest(canonical_bytes(source["geometry_parameters"]))!=
            "b733187ae8b75a48b2bc386bc7b8cd23fd1d62f52c51cb193320e22d8e5b861c"):
        raise ValueError("the actual original physical family or geometry definition differs")
    par=hard.Parameters(**source["physical_parameters"])
    geo=dict(source["geometry_parameters"])
    q=np.asarray(terminal["actual_retained_q"],dtype=float)
    nodes=np.asarray(terminal["actual_complete_required_radial_nodes"],dtype=float)
    peaks=terminal["actual_complete_required_peak_orbits"]
    fine=np.asarray(terminal["actual_required_fine_radial_nodes"],dtype=float)
    qualified=np.asarray(terminal["retained_qualification_fine_radial_nodes"],dtype=float)
    nt=terminal["actual_uniform_angles_and_FFT_nodes"]
    counts=terminal["cost"]["counts"]
    anchor=terminal["current_backend_anchor_and_working_library"]
    if (q.shape!=(81,) or not np.all(np.isfinite(q))
            or digest(q.tobytes())!="d59fa5cf999137438fba2497eab0e82a7c29a9f5d61fc189d29db96134b5fd45"
            or terminal["actual_q_binary64_sha256"]!=digest(q.tobytes())
            or (len(nodes),len(peaks),nt,len(fine),len(qualified))!=(840,1882,1536,1682,1672)
            or len(terminal["actual_working_field_orbit_rows"])!=380
            or len(terminal["recorded_unapplied_physical_peak_orbits"])!=1
            or len(terminal["recorded_unapplied_working_rows"])!=1
            or terminal["phase"]!="geometry_restoration"
            or terminal["actual_backend_local_trust"]!=.45050811767578125
            or terminal["proposed_next_local_trust"]!=.45050811767578125
            or terminal["post_backend_trust_decision_completed"] is not False
            or terminal["current_complete_library_values_known_for_retained_q"] is not True
            or terminal["retained_working_feasible_base_extra"]!=.010054272319566116
            or terminal["actual_retained_qualification"]["accepted_eta_max"]!=.1966187824246114
            or counts["accepted_metric_steps"]!=5 or counts["accepted_restoration_steps"]!=1
            or counts["working_complete_jacobians"]!=18 or counts["working_direction_blocks"]!=1320
            or source["source_last_backend_required_scalar_rows"]!=2324864
            or source["source_last_backend_extra"]!=terminal["retained_working_feasible_base_extra"]
            or anchor["outer"]!=16 or anchor["phase"]!=terminal["phase"]
            or anchor["initial_q_binary64_sha256"]!=terminal["actual_q_binary64_sha256"]):
        raise ValueError("actual retained physical state, current library, pending, trust or costs differ")
    if (digest(nodes.tobytes())!="1dd2bf49b8d9857d4ab7247ce61170a380986caa313fe99910b6ec3ff46df411"
            or digest(fine.tobytes())!="9c8fe195b7e79b5436094d31a4cf1b0cb6d68ebef1a71441af39dc5bfaa53229"
            or digest(qualified.tobytes())!="93b5b8ede1c7abf2fa5bc8ec3d1df3dbe9fc188df58500d437df28449c8a8468"
            or not set(nodes.tolist()).issubset(fine.tolist())
            or not set(qualified.tolist()).issubset(fine.tolist())
            or np.array_equal(qualified,fine)):
        raise ValueError("current and separately qualified radial libraries differ")
    margin_state=terminal["actual_retained_geometry_margin_state"]
    if (digest(canonical_bytes(margin_state))!="8c6d1aea9d4612830fa773317f114c24b74c2fef6de6796481cf2c4db443f07c"
            or margin_state["exact_single_original_value"] is not True
            or margin_state["lower_binary64"]!=5.42723195661168e-5
            or margin_state["upper_binary64"]!=margin_state["lower_binary64"]):
        raise ValueError("actual exact original margin state differs")
    checkpoint=terminal["actual_curvature_checkpoint"]
    if (digest(canonical_bytes(checkpoint))!="5cb41d8f1da1b3ad529da174ef13af382fefa650a2bad3e8b333b1d6a1bd442b"
            or checkpoint["model_identity_sha256"]!="8a1abe70f785c8c1d8e80b884aa58299598846c716c1be63b0d7b3e9421414a7"
            or checkpoint["row_function_signature"]!="20757ab502170f224b227cd78a00edd5af0bf47ddde0b04ebaa293e40a90d09f"
            or len(checkpoint["actual_native_or_prepared_packed_LDL"])!=3403
            or len(checkpoint["pending_frozen_multiplier_secant"]["nonzero_multipliers"])!=3):
        raise ValueError("actual restoration H and pending secant differ")
    trial=terminal["last_trial_not_implicitly_accepted"]
    saved=trial["observed_peaks"]
    paid=source["source_completed_peak_records"]
    paid_hash=digest(canonical_bytes(paid))
    if (paid_hash!=source["source_completed_peak_records_canonical_sha256"]
            or paid_hash!="3aeb005dc928fff9a742a46a343ac2f24fc2801cd6676bf290c3f1e356b74a8a"
            or len(paid)!=4465 or any(not p["localizer_success"] for p in paid)):
        raise ValueError("actual paid completed peak prefix differs")
    maxima={}
    for p in paid:
        if p["field"] not in maxima or p["value"]>maxima[p["field"]]["value"]:
            maxima[p["field"]]=p
    if maxima!=saved["maximum_observed_peak_by_field"]:
        raise ValueError("paid prefix does not give original FINAL maxima")
    trial_q=np.asarray(trial["q"],dtype=float)
    if (trial["q_binary64_sha256"]!="309b8dbc4f662a6a61a8ff7606f8282bdeb46ed3b02e4b8085b9115984d8e55d"
            or digest(trial_q.tobytes())!=trial["q_binary64_sha256"]
            or not trial["full_coarse_completed"] or not trial["full_fine_completed"]
            or trial["full_localization_completed"] or trial["accepted"]
            or trial["phase"]!="geometry_restoration" or trial["backend_extra"]!=0.
            or trial["working_backtrack_fraction"]!=1.
            or saved["candidate_count"]!=13100 or saved["completed_candidate_count"]!=4465
            or saved["unresolved_candidate_count"]!=8635 or saved["evaluations"]!=32454
            or len(saved["remaining_unprocessed_candidates"])!=8635
            or saved["oracle_identity"]!="f510229bc55c487bac6ddae072a2895b97a5ecb8407c56f0d97adfb266184a26"
            or np.any(trial_q<np.asarray(anchor["fixed_lower_physical_box"])-1e-12)
            or np.any(trial_q>np.asarray(anchor["fixed_upper_physical_box"])+1e-12)):
        raise ValueError("unfinished source trial or exact saved bracket scope differs")
    witness=source["already_paid_violating_peak"]
    if (witness not in paid or witness["field"]!="curvature_plus"
            or witness["value"]!=4.805549391305973e-6
            or witness["s"]!=.7612792968749998
            or witness["theta"]!=1.5707963267948966
            or not witness["value"]>trial["backend_extra"]+geo["feasibility_tolerance"]
            or not any(row["s"]==witness["s"] and row["theta"]==witness["theta"]
                       for row in terminal["recorded_unapplied_physical_peak_orbits"])
            or not any(row["field"]==witness["field"] and row["s"]==witness["s"]
                       and row["theta"]==witness["theta"]
                       and row["evidence"]["value"]==witness["value"]
                       for row in terminal["recorded_unapplied_working_rows"])):
        raise ValueError("the paid rejecting witness or its two original pending rows differ")
    previous_outer=source["prior_completed_outer_receipt"]
    if (previous_outer["outer"]!=15
            or previous_outer["literal_bytes"]!=354863
            or previous_outer["literal_sha256"]!="2e9c47261b0172004bdc5a390c7eaa19412fe7347c6644a6e72752325fb94b95"
            or previous_outer["accepted_metric_steps"]!=5
            or previous_outer["accepted_restoration_steps"]!=1
            or previous_outer["actual_q_binary64_sha256"]!=terminal["actual_q_binary64_sha256"]
            or counts["accepted_metric_steps"]-previous_outer["accepted_metric_steps"]!=0
            or counts["accepted_restoration_steps"]-previous_outer["accepted_restoration_steps"]!=0):
        raise ValueError("the last source outer did not have the recorded zero actual acceptances")
    if digest(canonical_bytes(saved["remaining_unprocessed_candidates"]))!=source["unexecuted_remaining_queue_canonical_sha256"]:
        raise ValueError("the original unexecuted queue differs")
    source["source_cost_ledger"]={"source_run":45930250772,"source_job":140280968908,
        "complete_actual_source_cost":terminal["cost"],
        "recorded_chain_scientific_seconds_lower_bound":
            terminal["cost"]["prior_cost_ledger"]["recorded_chain_scientific_seconds_lower_bound"]
            +terminal["cost"]["elapsed_seconds"],
        "recorded_chain_scientific_seconds_is_exact":False,
        "earlier_censored_work_still_unknown":True,"metadata_recovery_scientific_evaluations":0}
    start={"initial_fine_and_observed_scan":terminal["actual_retained_qualification"],
           "initial_observed_peaks":terminal["actual_retained_observed_peak_summary"]}
    return source,source["origin"],start,par,geo,q,nodes,peaks,nt,terminal["actual_backend_local_trust"],terminal


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
    margin_started=time.monotonic()
    saved_margin=terminal["actual_retained_geometry_margin_state"]
    best_geo=OriginalMarginState(saved_margin["lower_binary64"],saved_margin["upper_binary64"],
                                 saved_margin["origin"])
    if best_geo.receipt()!=saved_margin:
        raise ValueError("the exact saved original margin state did not restore identically")
    margin_restore_seconds=time.monotonic()-margin_started
    if best_geo.phase(tolerance)!=terminal["phase"]:
        raise ValueError("recorded original phase and possible margin state differ")
    best_eta = best_scan["accepted_eta_max"]
    best_observed = dict(start["initial_observed_peaks"])
    pending=list(terminal["recorded_unapplied_physical_peak_orbits"])
    proposed_working=list(terminal["recorded_unapplied_working_rows"])
    working=list(terminal["actual_working_field_orbit_rows"])
    actual_nodes, actual_peaks = nodes.copy(), list(peaks)
    actual_fine_nodes=np.asarray(terminal["actual_required_fine_radial_nodes"],dtype=float).copy()
    best_fine_nodes=np.asarray(terminal["retained_qualification_fine_radial_nodes"],dtype=float).copy()
    actual_trust, proposed_trust = trust, trust
    # Source outer16 accepted zero physical steps, has no natural backend
    # outcome, and already has both pending exchanges. The original post-
    # outer rule therefore takes its final else: proposed_trust=actual_trust.
    # This completes that bookkeeping; it is not an accepted-step reset.
    trust_decision_completed = True
    source_disposition={
        "source_state_sha256":digest(raw),
        "source_FINAL_JSON_sha256":source["origin"]["FINAL_JSON_sha256"],
        "source_trial_q_sha256":terminal["last_trial_not_implicitly_accepted"]["q_binary64_sha256"],
        "paid_rejecting_witness":source["already_paid_violating_peak"],
        "original_restoration_epigraph":0.,"original_acceptance_tolerance":tolerance,
        "accepted":False,"full_localization_completed":False,
        "source_completed_brackets_retained":4465,"remaining_brackets_unexecuted":8635,
        "remaining_queue_canonical_sha256":source["unexecuted_remaining_queue_canonical_sha256"],
        "complete_original_queue_and_paid_prefix_remain_in_request_and_SOURCE_definition":True,
        "remaining_queue_not_claimed_closed_or_deleted":True,
        "old_costs_preserved_and_no_new_localizer_work_claimed":True,
        "source_outer":16,"source_outer_actual_accepted_steps":0,
        "source_post_backend_trust_decision_was_completed":False,
        "source_post_backend_trust_decision_now_completed":True,
        "source_trust_decision_reason":"zero_acceptance_and_actual_pending_exchange_keep_original_trust",
        "actual_source_trust":actual_trust,"resulting_proposed_trust":proposed_trust,
        "original_current_physical_rows_and_both_pending_lists_retained":True,
        "future_library_order_may_differ_from_finishing_rejected_trial_queue":True,
        "all_future_accepted_trials_still_need_original_complete_qualification":True}
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
        "original_working_rechecks_after_lift":0,
        "source_exact_margin_state_restorations":1,
        "source_exact_margin_state_restore_seconds":margin_restore_seconds,
        "source_completed_localizer_candidates_replayed":0,
        "source_retained_fine_baseline_replayed":0,
        "source_last_rejected_trial_replayed":0,
        "source_paid_violation_rejections_without_new_science":1,
        "source_remaining_brackets_newly_executed_or_completed":0,
        "source_previous_incomplete_outer_trust_decisions_completed":1}
    # These are source evidence tracks, not new callback points or a restored
    # native workspace. They remain explicit until a genuine new trial exists.
    last_trial=dict(terminal["last_trial_not_implicitly_accepted"])
    last_trial.update(reason="already_paid_original_margin_violation_rejected_without_remaining_localization",
        accepted=False,full_localization_completed=False,
        source_unexecuted_remaining_candidates_retained=8635,
        already_paid_rejecting_witness=source["already_paid_violating_peak"])
    last_backend=terminal["last_backend"]
    last_raw_backend_trial=dict(terminal["last_raw_backend_trial_not_implicitly_accepted"])
    last_backtrack=dict(terminal["last_working_backtrack"])
    current_full_library_values_known = True
    known_scalar_rows = source["source_last_backend_required_scalar_rows"]
    retained_working_base_extra = source["source_last_backend_extra"]
    active_rows = None
    current_outer, phase = -1, terminal["phase"]
    backend_anchor_state=dict(terminal["current_backend_anchor_and_working_library"])
    status = "declared_outer_limit_not_complete"
    curvature = TrueSecantSLSQP(original_minimize,CURVATURE_MODEL_IDENTITY,
        hard.emit,check_time,checkpoint=terminal["actual_curvature_checkpoint"])

    def costs():
        return {"elapsed_seconds":time.monotonic()-started, "counts":dict(counts),
            "active_working_counts_not_yet_retired": None if active_rows is None else dict(active_rows.counts),
            "oracle_totals_once_per_live_or_retired_oracle":ledger.snapshot(),
            "prior_cost_ledger":source["source_cost_ledger"],
            "native_curvature_current_counts_included_in_elapsed":dict(curvature.counts),
            "native_build_included_in_elapsed":dict(curvature.native_build_receipt),
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
            "actual_curvature_checkpoint":curvature.checkpoint(),
            "native_curvature_is_only_a_heuristic_initialization_of_unchanged_physical_QP":True,
            "current_complete_library_values_known_for_retained_q":current_full_library_values_known,
            "retained_working_feasible_base_extra":retained_working_base_extra,
            "actual_retained_geometry_margin_state":best_geo.receipt(),
            "source_actual_native_H_and_pending_checkpoint_restored":True,
            "complete_prior_native_workspace_or_Jacobian_restored":False,
            "source_rejected_unexecuted_localizer_receipt":source_disposition,
            "cost":costs(), "no_physical_row_removed_by_working_selection":True,
            "continuous_geometry_reach_or_README_completion_claim":False})

    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION", {"schema":SCHEMA, "source_state":source,
        "source_state_sha256":digest(raw), "physical_parameters":asdict(par), "geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "actual840_rings1882_orbits380_working_and_pending1_plus1_retained":True,
        "source5_metric1_restoration18_complete_Jacobians_not_replayed":True,
        "source4465_paid_and8635_unexecuted_retained_but_known_trial_rejected":True,
        "source_qualified1672_fine_is_not_current_required1682_fine":True,
        "source_current_full_value_library_and_scalar_row_count_already_paid":True,
        "source18_complete_Jacobians_and1320_blocks_paid_but_no_J_matrix_saved":True,
        "source_exact_saved_geometry_margin_restored_without_inverse_rounding":True,
        "source_actual_restoration_H_semantics_preserved_until_original_phase_change":True,
        "source_rejected_trial_and_raw_backend_tracks_stay_unaccepted":True,
        "no_already_paid_retained_q_fine_baseline_replayed":True,
        "native_curvature_model_identity":CURVATURE_MODEL_IDENTITY,
        "first_native_H_restores_only_actual_reported_H_and_pending_same_model":True,
        "different_phase_still_resets_H_by_original_semantic_signature":True,
        "source_exact_saved_original_best_geo":best_geo.receipt(),
        "original_restoration_acceptance_kept_not_replaced_by_metric_eta_test":True,
        "subsequent_initial_H_uses_only_actual_paid_J_QP_fixed_multiplier_secants":True,
        "native_build_fetch_compile_import_and_seed_linear_algebra_are_charged":True,
        "all_original_new_row_values_and_Jacobians_still_paid":True,
        "metric_auxiliary_epigraph_lift_never_counts_as_actual_eta_improvement":True,
        "new_unrepresented_peaks_are_preserved_even_when_epigraph_is_lifted":True,
        "new_unrepresented_coarse_working_witnesses_survive_the_auxiliary_lift":True,
        "old_fine1212_1298_1322_and_every_subsequent_fine_grid_permanently_retained":True,
        "source_complete_internal_workspace_not_output_partial_H_pending_is_restored":True,
        "new_SLSQP_history_continues_when_only_a_separate_shortened_physical_best_changes":True,
        "raw_backend_iterates_remain_the_unchanged_optimizer_sequence":True,
        "genuine_row_exchange_phase_change_or_natural_return_still_restarts_backend":True,
        "same_semantics_H_may_initialize_new_backend_without_inheriting_old_work_arrays":True,
        "phase_or_row_function_semantics_change_resets_H_to_identity":True,
        "all_old_1536_uniform_inequalities_retained_for_full_value_acceptance":True,
        "working_points_never_redefine_mean_E":True,
        "old_completed_START_scan_and_localization_not_replayed":True,
        "old_zero_acceptance_pending_exchange_trust_decision_completed":True,
        "every_accepted_step_requires_complete_coarse_fine_actual_peaks_and_nested_quadrature":True,
        "unrepresented_violations_reject_and_enter_working_or_physical_libraries":True,
        "fine_geometry_margin_and_backend_metric_epigraph_enforced_at_acceptance":True,
        "only_local_optimization_matrix_is_restricted":True,
        "old_oracle_parity_check_not_repeated":True,
        "old_paid_restriction_mapping_or_direction_observation_repeated":False,
        "working_backtracking_never_bypasses_complete_qualification":True,
        "actual_q_and_original_trust_from_FINAL_with_explicit_completed_postdecision":True,
        "same_working_model_fun_and_jac_cache_preserved":True,
        "old_unreported_Jacobian_matrix_not_fabricated_as_available":True,
        "metric_changes_during_static_design":True, "fixed_g_or_README_completion_claim":False})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "known_source_violation_rejected_original_pending_and_trust_retained")

    try:
        # The source trial is already refuted by one original paid row.
        # Its 8635 unexecuted brackets remain in the immutable source input;
        # do not spend them or relabel them completed. Apply both pending
        # exchanges to retained d59fa and keep every later acceptance gate.
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
                    phase=best_geo.phase(tolerance)
                    if phase is None:
                        raise OriginalMarginUnresolved("original next phase is not constant over saved margin states")
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
                        best_geo.maximize_with_original_coarse(-geometry_min)
                        extra=best_geo.original_added_extra(.01)
                        if extra is None:
                            raise OriginalMarginUnresolved("original next e is not constant over saved margin states")
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
                    "old_normal_source_native_work_arrays_unavailable":True,
                    "new_SLSQP_QP_starts_with_declared_heuristic_H_only":True}
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
                    restored=phase=="geometry_restoration" and geometry_peak<=tolerance and physicalokay
                    if restored:
                        accepted=True
                    elif phase=="geometry_restoration":
                        accepted=best_geo.original_strict_improvement(geometry_peak)
                        if accepted is None:
                            last_trial.update(reason="original_missing_best_geo_comparison_undetermined",
                                actual_complete_geometry_margin_violation=max(0.,geometry_peak),
                                actual_complete_eta=observed_current["accepted_eta_max"],accepted=False,
                                original_best_geo_possible_state=best_geo.receipt())
                            snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
                            raise OriginalMarginUnresolved("original restoration comparison is not constant over saved margin states")
                    else:
                        accepted=physicalokay and observed_current["accepted_eta_max"]<best_eta-1e-12
                    last_trial.update(actual_complete_geometry_margin_violation=max(0.,geometry_peak),
                        actual_complete_eta=observed_current["accepted_eta_max"],accepted=bool(accepted))
                    if accepted:
                        q=trial.copy();best_scan=observed_current;best_observed=old.compact_observation(observed)
                        best_fine_nodes=fine_nodes.copy()
                        best_geo=OriginalMarginState.exact(max(0.,geometry_peak));best_eta=observed_current["accepted_eta_max"]
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
                    outcome=curvature.minimize(lambda v:float(v[-1]),x0,jac=lambda v:np.r_[np.zeros(81),1.],
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
    except OriginalMarginUnresolved as error:
        status="original_missing_best_geo_comparison_undetermined"
        hard.emit("WORKING_ROWS_STOP",{"type":type(error).__name__,"message":str(error)})
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
