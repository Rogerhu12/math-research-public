#!/usr/bin/env python3
"""Continue actual55be B030 and only its unaccepted trial's remaining1906 peaks.

Preserve the904 paid prefix, current1810 vs qualified1786 fine grids, original
2 physical/8 working pending lists, exact g=0, metric H and23 pending multipliers.
Complete the source half-backtrack before its actual acceptance/trust decision.
Only then resume the unchanged full native loop. Historical unexecuted8635
remain in their bound source, neither replayed nor declared complete.
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

SCHEMA="r566-actual55be-saved-metric-H-partial1906-v1"
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
    if source.get("schema")!="r566-real55be-paid904-remaining1906-saved-metric-H-source-v1":
        raise ValueError("wrong actual metric partial-queue continuation source")
    expected_origin={'run_id': 46123017949, 'job_id': 140911408687, 'source_commit': 'fe5224fb9fa58cd4dca15b6003e0df33e396d97c', 'runtime_pull_commit': '1a82ca30b6b6241a3a168f1dff251a2b82feef52', 'source_sha256': 'f17036f13d9861a86b7cf0888caf9422b26f46b8326784659095c48f753a0bd4', 'request_gzip_bytes': 125360, 'request_gzip_sha256': '42537f43ead161d63c53378b47fc23617e72a27d40a1c24209b1fad0757dc77b', 'raw_stdout_bytes': 19989502, 'raw_stdout_sha256': '21d3680309b5e0eceefa194133d0c9071b511c3ea5480884d3e8ccb481ef5111', 'FINAL_JSON_bytes': 925016, 'FINAL_JSON_sha256': 'b799753e92364ba0bd7a142533bd73e8d2b19c385dafaf63575264d67c986876', 'partial_JSON_bytes': 580912, 'partial_JSON_sha256': 'fb72d7582afccc1843210d7fbc4adbb2104b73cb8bfed6b7f8c8a166c89b37af'}
    expected={'q': '55be941cbf3ff39b259713a5ecf264bddbc7ce934b2e7ac7436713d58396df63', 'nodes': '20f63ab35f0c18d8f7d38b2658055e02c55a31336caa66c6eb68af32a95ecc03', 'fine': '8a072c05fa5af6ccb1cfeba222b343a9e9af016a3b1393ced583288cbf23be9f', 'qualified': '30fbe6f2a81fe60511a9ab83fa613303a23864bd5e4f42c3a455c4aa14996bb0', 'margin': 'fb993d567ac652eb8a27f4fb542a6d9389e20dbd8593dfe8a41b387490979237', 'checkpoint': '460da85d92da2556a10c170c7b5d20383972259160c892985055252915249a90', 'paid_prefix': '5aa58a88ad8b37a8be143ad96f2c1f32df233586677463175e727c9e2825d820', 'remaining': '4b9352eb53d41f3c8a9f766d89a1d57e64d870943c0aab1cfe38fbee2246160d', 'historical_unexecuted': '4d382ffb87ed19d0b4040b8ac3423676dedea0e217426822f53afeadd6c9e70b'}
    if source["origin"]!=expected_origin:
        raise ValueError("actual completed source identity differs")
    encoded=source["complete_original_FINAL_JSON"].encode()
    if len(encoded)!=expected_origin["FINAL_JSON_bytes"] or digest(encoded)!=expected_origin["FINAL_JSON_sha256"]:
        raise ValueError("complete original source FINAL changed")
    terminal=json.loads(encoded)
    def canonical_bytes(value):
        return json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    if (digest(canonical_bytes(source["physical_parameters"]))!="4fa67643c13c83e4968938a0185720522c5fb7e1349bb26c78c4af2e27f33798"
            or digest(canonical_bytes(source["geometry_parameters"]))!="b733187ae8b75a48b2bc386bc7b8cd23fd1d62f52c51cb193320e22d8e5b861c"):
        raise ValueError("original B030 physical family or geometry definition differs")
    par=hard.Parameters(**source["physical_parameters"]);geo=dict(source["geometry_parameters"])
    q=np.asarray(terminal["actual_retained_q"],dtype=float)
    nodes=np.asarray(terminal["actual_complete_required_radial_nodes"],dtype=float)
    peaks=terminal["actual_complete_required_peak_orbits"]
    fine=np.asarray(terminal["actual_required_fine_radial_nodes"],dtype=float)
    qualified=np.asarray(terminal["retained_qualification_fine_radial_nodes"],dtype=float)
    nt=terminal["actual_uniform_angles_and_FFT_nodes"]
    counts=terminal["cost"]["counts"];native=terminal["cost"]["native_curvature_current_counts_included_in_elapsed"]
    anchor=terminal["current_backend_anchor_and_working_library"]
    if (q.shape!=(81,) or not np.all(np.isfinite(q)) or digest(q.tobytes())!=expected["q"]
            or terminal["actual_q_binary64_sha256"]!=expected["q"]
            or (len(nodes),len(peaks),nt,len(fine),len(qualified))!=(904,2020,1536,1810,1786)
            or len(terminal["actual_working_field_orbit_rows"])!=601
            or len(terminal["recorded_unapplied_physical_peak_orbits"])!=2
            or len(terminal["recorded_unapplied_working_rows"])!=8
            or terminal["phase"]!="metric" or terminal["outer"]!=13
            or terminal["actual_backend_local_trust"]!=.45050811767578125
            or terminal["proposed_next_local_trust"]!=.45050811767578125
            or terminal["post_backend_trust_decision_completed"] is not False
            or terminal["current_complete_library_values_known_for_retained_q"] is not True
            or terminal["retained_working_feasible_base_extra"]!=.1932424442521748
            or terminal["actual_retained_qualification"]["accepted_eta_max"]!=.1932424342521748
            or counts["accepted_metric_steps"]!=4 or counts["accepted_restoration_steps"]!=1
            or counts["working_complete_jacobians"]!=15 or counts["working_direction_blocks"]!=1290
            or native["backend_calls"]!=14 or native["native_calls"]!=16
            or source["source_last_backend_required_scalar_rows"]!=3214064
            or source["source_last_backend_extra"]!=terminal["retained_working_feasible_base_extra"]
            or anchor["outer"]!=13 or anchor["phase"]!="metric"
            or anchor["initial_q_binary64_sha256"]!=terminal["actual_q_binary64_sha256"]
            or source["source_current_outer_accepted_steps"]!=0):
        raise ValueError("actual retained state, pending libraries, trust or costs differ")
    if (digest(nodes.tobytes())!=expected["nodes"] or digest(fine.tobytes())!=expected["fine"]
            or digest(qualified.tobytes())!=expected["qualified"]
            or not set(nodes.tolist()).issubset(fine.tolist())
            or not set(qualified.tolist()).issubset(fine.tolist()) or np.array_equal(qualified,fine)):
        raise ValueError("current1810 and independently qualified1786 libraries differ")
    margin=terminal["actual_retained_geometry_margin_state"];checkpoint=terminal["actual_curvature_checkpoint"]
    if (digest(canonical_bytes(margin))!=expected["margin"]
            or margin["exact_single_original_value"] is not True
            or margin["lower_binary64"]!=0. or margin["upper_binary64"]!=0.
            or digest(canonical_bytes(checkpoint))!=expected["checkpoint"]
            or checkpoint["model_identity_sha256"]!="8a1abe70f785c8c1d8e80b884aa58299598846c716c1be63b0d7b3e9421414a7"
            or checkpoint["row_function_signature"]!="505f8cbcb0a22bc114da97754d0903cee340381ff6237c868c947f04e71452c5"
            or len(checkpoint["actual_native_or_prepared_packed_LDL"])!=3403
            or len(checkpoint["pending_frozen_multiplier_secant"]["nonzero_multipliers"])!=23):
        raise ValueError("actual exact margin, metric H or frozen multipliers changed")
    trial=terminal["last_trial_not_implicitly_accepted"];saved=trial["observed_peaks"]
    paid=source["source_completed_peak_records"]
    if (len(paid)!=904 or digest(canonical_bytes(paid))!=expected["paid_prefix"]
            or any(not p["localizer_success"] for p in paid)
            or any(not np.all(np.isfinite([p["s"],p["theta"],p["value"],p["sampled_value"]])) for p in paid)
            or digest(canonical_bytes(saved["remaining_unprocessed_candidates"]))!=expected["remaining"]):
        raise ValueError("actual paid prefix or original remaining brackets changed")
    maxima={}
    for p in paid:
        if p["field"] not in maxima or p["value"]>maxima[p["field"]]["value"]:maxima[p["field"]]=p
    if maxima!=saved["maximum_observed_peak_by_field"]:
        raise ValueError("paid prefix does not reproduce source maximum records")
    partial={**source["source_partial_metadata"],"peaks":paid,"q":trial["q"],
        "full_observation_radial_nodes":fine.tolist(),
        "remaining_unprocessed_candidates":saved["remaining_unprocessed_candidates"]}
    partial_bytes=canonical_bytes(partial)
    if len(partial_bytes)!=expected_origin["partial_JSON_bytes"] or digest(partial_bytes)!=expected_origin["partial_JSON_sha256"]:
        raise ValueError("the complete original PARTIAL is not reconstructed identically")
    if (trial["q_binary64_sha256"]!="43015466eb4f1818628178bf8f900cba2304fcd74753bab5759f214ff188dd23"
            or not trial["full_coarse_completed"] or not trial["full_fine_completed"]
            or trial["full_localization_completed"] or trial["accepted"] or trial["phase"]!="metric"
            or trial["physical_box_violation"]!=0. or trial["working_row_violation"]!=0.
            or trial["working_backtrack_fraction"]!=.5 or trial["backend_extra"]!=.19293438868766796
            or saved["candidate_count"]!=2810 or saved["completed_candidate_count"]!=904
            or saved["unresolved_candidate_count"]!=1906 or saved["evaluations"]!=8072
            or len(saved["remaining_unprocessed_candidates"])!=1906
            or saved["oracle_identity"]!="64b79ce3d42c9610c5c4ac4436728c1205903ec96f62112f967a37a8a2000898"
            or trial["full_fine_scan"]["eta_max"]!=.19294084341286163
            or trial["full_fine_scan"]["geometry_violation_max"]!=0.):
        raise ValueError("source unaccepted half-backtrack or exact localization scope differs")
    trial_q=np.asarray(trial["q"],dtype=float)
    if (digest(trial_q.tobytes())!=trial["q_binary64_sha256"]
            or np.any(trial_q<np.asarray(anchor["fixed_lower_physical_box"])-1e-12)
            or np.any(trial_q>np.asarray(anchor["fixed_upper_physical_box"])+1e-12)):
        raise ValueError("actual source trial or original physical box differs")
    source["saved_localizer_scope"]={"q_binary64_sha256":trial["q_binary64_sha256"],
        "oracle_identity":saved["oracle_identity"],"full_observation_radial_nodes":fine.tolist(),
        "full_observation_FFT_nodes":3072,"unresolved_candidate_count":1906,
        "source_completed_peaks":paid,"source_completed_candidate_count":904,
        "source_original_candidate_count":2810,"source_completed_point_objective_evaluations":8072,
        "source_partial_localizer_elapsed_seconds":32.787831607000044}
    if digest(canonical_bytes(terminal["source_rejected_unexecuted_localizer_receipt"]))!=expected["historical_unexecuted"]:
        raise ValueError("historical rejected unexecuted queue receipt changed")
    historical=source["historical_rejected_unexecuted_source"]
    if digest(Path(historical["request_path"]).read_bytes())!=historical["request_gzip_sha256"]:
        raise ValueError("historical4465 prefix and unexecuted8635 source no longer retained")
    source["source_cost_ledger"]={"source_run":46123017949,"source_job":140911408687,
        "complete_actual_source_cost":terminal["cost"],
        "recorded_chain_scientific_seconds_lower_bound":
            terminal["cost"]["prior_cost_ledger"]["recorded_chain_scientific_seconds_lower_bound"]
            +terminal["cost"]["elapsed_seconds"],
        "recorded_chain_scientific_seconds_is_exact":False,"earlier_censored_work_still_unknown":True,
        "metadata_recovery_scientific_evaluations":0,"source_partial_904_completed_1906_unclosed_not_replayed":True,
        "source_unfinished_bracket_internal_optimizer_responses_not_saved":True}
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
    # The current source backend stopped inside the candidate localizer.
    # Its previous partial-J receipt remains historical, not this live task.
    trust_decision_completed=False
    source_disposition=dict(terminal["source_rejected_unexecuted_localizer_receipt"])
    source_resume_receipt=dict(terminal["source_current_incomplete_J_resume_receipt"])
    source_partial_resume_receipt={"source_state_sha256":digest(raw),
        "source_FINAL_JSON_sha256":source["origin"]["FINAL_JSON_sha256"],
        "source_outer":13,"source_current_outer_prior_accepted_steps":0,
        "source_completed_localizer_candidates":904,"source_unresolved_candidates":1906,
        "source_half_backtrack_trial_not_implicitly_accepted":True,
        "source_post_backend_trust_decision_was_completed":False,
        "actual_source_trust":actual_trust,"source_H_and23_pending_multipliers_preserved":True,
        "historical8635_queue_and_prior_partial_J_cost_preserved":True,
        "actual_qualification_and_post_backend_decision_state":"pending"}
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
        "source_paid_violation_rejections_without_new_science":0,
        "source_remaining_brackets_newly_executed_or_completed":0,
        "source_previous_incomplete_outer_trust_decisions_completed":0,
        "source_saved_localizations_completed":0,"source_saved_trial_fully_qualified_acceptances":0,
        "source_paid_full_fine_and_nested_reports_reused":0,"source_completed_brackets_reused":0,
        "new_remaining_saved_brackets_completed":0}
    # These are source evidence tracks, not new callback points or a restored
    # native workspace. They remain explicit until a genuine new trial exists.
    last_trial=dict(terminal["last_trial_not_implicitly_accepted"])
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
            "source_current_incomplete_J_resume_receipt":source_resume_receipt,
            "source_partial1906_resume_receipt":source_partial_resume_receipt,
            "cost":costs(), "no_physical_row_removed_by_working_selection":True,
            "continuous_geometry_reach_or_README_completion_claim":False})

    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION", {"schema":SCHEMA, "source_state":source,
        "source_state_sha256":digest(raw), "physical_parameters":asdict(par), "geometry_parameters":geo,
        "solver_arguments":{k:v for k,v in vars(args).items() if k!="source_state_json"},
        "actual904_rings2020_orbits601_working_and_pending2_plus8_retained":True,
        "source4_metric1_restoration15_complete_Jacobians_not_replayed":True,
        "historical4465_paid_and8635_unexecuted_retained_in_bound_prior_request":True,
        "source_qualified1786_fine_is_not_current_required1810_fine":True,
        "source_current_full_value_library_and_scalar_row_count_already_paid":True,
        "source15_complete_Jacobians_and1290_blocks_paid_but_no_J_saved":True,
        "source_exact_saved_geometry_margin_restored_without_inverse_rounding":True,
        "source_actual_metric_H_semantics_preserved_until_original_phase_change":True,
        "source_pending_half_trial_and_raw_backend_tracks_remain_distinct":True,
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
        "source_current_partial_localizer_requires_actual_qualification_before_trust_decision":True,
        "every_accepted_step_requires_complete_coarse_fine_actual_peaks_and_nested_quadrature":True,
        "unrepresented_violations_reject_and_enter_working_or_physical_libraries":True,
        "fine_geometry_margin_and_backend_metric_epigraph_enforced_at_acceptance":True,
        "only_local_optimization_matrix_is_restricted":True,
        "old_oracle_parity_check_not_repeated":True,
        "old_paid_restriction_mapping_or_direction_observation_repeated":False,
        "working_backtracking_never_bypasses_complete_qualification":True,
        "actual_q_and_original_trust_from_FINAL_with_unfinished1906_localizer_preserved":True,
        "same_working_model_fun_and_jac_cache_preserved":True,
        "old_unreported_Jacobian_matrix_not_fabricated_as_available":True,
        "metric_changes_during_static_design":True, "fixed_g_or_README_completion_claim":False})
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT", "actual55be_metric_checkpoint_and_original1906_queue_preserved")

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
            counts["localizer_candidates"]+=observed["new_candidate_count"]
            counts["localizer_completed_candidates"]+=observed["new_completed_candidate_count"]
            counts["source_completed_brackets_reused"]+=observed["source_completed_candidate_count"]
            counts["new_remaining_saved_brackets_completed"]+=observed["new_completed_candidate_count"]
            counts["source_remaining_brackets_newly_executed_or_completed"]+=observed["new_completed_candidate_count"]
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
                source_trial["physical_box_violation"]<=tolerance and
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
                best_eta=qualified["accepted_eta_max"];best_geo=OriginalMarginState.exact(max(0.,geometry_peak))
                retained_working_base_extra=float(lifted[-1]);current_full_library_values_known=True
                counts["accepted_metric_steps"]+=1
                counts["source_saved_trial_fully_qualified_acceptances"]+=1
            # Finish the actual source outer's post-callback decision. There
            # was no natural native return; preserve pending row exchanges.
            source_seed=np.asarray(terminal["actual_retained_q"],dtype=float)
            source_scales=np.r_[np.full(2*prior_fine.uniform.block,.5),
                np.full(par.radial_count,.2),np.full(par.radial_count,.15),.1]
            actual_displacement=float(np.max(abs(q-source_seed)/source_scales))
            if accepted and actual_displacement>=.9*actual_trust:
                proposed_trust=min(args.maximum_trust,1.5*actual_trust)
            else:
                proposed_trust=actual_trust
            trust_decision_completed=True
            counts["source_previous_incomplete_outer_trust_decisions_completed"]+=1
            source_partial_resume_receipt.update(
                actual_qualification_and_post_backend_decision_state="completed",
                actual_source_trial_accepted=bool(accepted),actual_normalized_physical_displacement=actual_displacement,
                resulting_proposed_trust=proposed_trust,original_pending_physical_count=len(pending),
                original_pending_working_count=len(proposed_working),natural_backend_return_fabricated=False,
                source_internal_native_workspace_restored=False)
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
