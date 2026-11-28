"""Continue exactly the original 4261 saved brackets before the native outer-36 exchange."""
from __future__ import annotations
import gzip
import hashlib
import json
import os
from pathlib import Path
import struct
import types

HERE=Path(__file__).resolve().parent
PARENT=HERE/'r692_actual34aa_working_jacobian_resume.py'
SOURCE_PARENT_REQUEST=HERE.parent/'computations/request-r692-actual34aa-working-jacobian-20261128.json.gz'
SCHEMA='r714-actual516-original4261-angular-queue-and-full-physical-continuation-v1'
FINAL='8aec2e1157adac256bd128000d125517118c95d27c41f5ff511133b4c64bf599'
Q='5162348896c0a12367aa75a1c193c57ac0bf3f63afb83031ff62bf8c83e528df'
TRIAL='97559ba1eff3e38f8b9a20d3e4ef81b9081ad4970132b5ca20606655d9c254ce'
ORIGIN=dict(run_id=46146663846,job_id=140984103096,source_commit='e739169338b6ec28f4ba68b8ec22b24dff5905e9',
            FINAL_JSON_sha256=FINAL,raw_log_sha256='ae2dda87d4458b0369106bf60d78660d2e37380273c13f2542289ff9ee9bafea',
            request_sha256='4d29fc23486cfc1dafb05cae4d6c596c14b07fb18d4e528263aad7bfe1786fbc',
            partial_JSON_sha256='b0d9fbc326bbc4d0488710091b262502b2185281a39392d6ffe90cf9e744b91c')


def sha(b):return hashlib.sha256(b).hexdigest()
def literal(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def fhash(v):return sha(struct.pack('<'+'d'*len(v),*v))


def load(args):
    b=args.source_state_json.encode()
    if len(b)!=1703470 or sha(b)!=FINAL or sha(SOURCE_PARENT_REQUEST.read_bytes())!=ORIGIN['request_sha256']:
        raise ValueError('Incorrect natural R692 terminal or parent request.')
    prev=json.loads(gzip.decompress(SOURCE_PARENT_REQUEST.read_bytes()))
    if any(getattr(args,k)!=v for k,v in prev['common_parameters'].items()):raise ValueError('Changed original physical solver scope.')
    t=json.loads(b);q=t['actual_retained_q'];trial=t['last_trial_not_implicitly_accepted'];part=trial['observed_peaks']
    fine=t['actual_required_fine_radial_nodes'];qualified=t['retained_qualification_fine_radial_nodes']
    history=t['cost'];n=history['counts'];cp=t['actual_curvature_checkpoint']
    if (len(q)!=81 or fhash(q)!=Q or t['actual_q_binary64_sha256']!=Q or t['outer']!=36 or t['phase']!='metric'
            or t['schema']!=parent.SCHEMA or t['reason']!='cooperative_clock_or_unresolved_localizer_checkpoint'
            or t['last_backend'] is not None or t['post_backend_trust_decision_completed'] or t['proposed_trust_not_yet_adopted']
            or t['actual_backend_local_trust']!=.6757621765136719 or t['proposed_next_local_trust']!=t['actual_backend_local_trust']
            or t['current_backend_anchor_and_working_library']['initial_q_binary64_sha256']!=Q
            or not t['current_complete_library_values_known_for_retained_q'] or t['actual_retained_qualification']['accepted_eta_max']!=.18299110508440017
            or (len(t['actual_complete_required_radial_nodes']),len(t['actual_complete_required_peak_orbits']),len(fine),len(qualified),
                len(t['actual_working_field_orbit_rows']),len(t['recorded_unapplied_physical_peak_orbits']),len(t['recorded_unapplied_working_rows']))!=(989,2215,1979,1973,1668,7,7)
            or (fhash(fine),fhash(qualified))!=(t['actual_required_fine_radial_nodes_binary64_sha256'],t['retained_qualification_fine_radial_nodes_binary64_sha256'])
            or trial['q_binary64_sha256']!=TRIAL or fhash(trial['q'])!=TRIAL or t['last_raw_backend_trial_not_implicitly_accepted']['q']!=trial['q']
            or trial['outer']!=36 or trial['accepted'] or trial['full_localization_completed'] or not (trial['full_coarse_completed'] and trial['full_fine_completed'])
            or trial['complete_required_scalar_rows']!=3516474 or trial['backend_extra']!=.18270279330339317
            or trial['full_fine_scan']['eta_max']!=.18276623635871572 or trial['working_backtrack_fraction']!=1.
            or trial['terminal_backend_point'] or t['last_working_backtrack']['base_actual_q_sha256']!=Q
            or (n['accepted_metric_steps'],n['working_complete_jacobians'],n['working_direction_blocks'],n['localizer_candidates'],
                n['localizer_completed_candidates'],n['complete_localizations'],n['localizer_unresolved_returns'])!=(6,19,2982,34729,30468,9,4261)
            or history['active_working_counts_not_yet_retired'] is not None or cp['dimension']!=82
            or len(cp['actual_native_or_prepared_packed_LDL'])!=3403 or len(cp['pending_frozen_multiplier_secant']['nonzero_multipliers'])!=32
            or cp['payload_without_this_receipt']['sha256']!='93af67b66379abcfea5559322eb63d368acf825a46a87c087801d681f2968ec4'):
        raise ValueError('Retained or deferred R692 physical state or original ledger differs.')
    queue=part['remaining_unprocessed_candidates'];full={k:v for k,v in part.items() if k!='maximum_observed_peak_by_field'}
    full.update(peaks=[],q=trial['q'],full_observation_radial_nodes=fine,full_observation_FFT_nodes=3072,
                completed_peaks_and_remaining_candidates_are_not_a_completed_scan=True)
    if (part['candidate_count']!=4261 or len(queue)!=4261 or part['completed_candidate_count']!=0 or part['evaluations']!=0
            or part['batches_started']!=0 or part['oracle_identity']!='51e7d194f5c13d4745352dc1440e47b17b3d7cd39216bf927295c3d70a472249'
            or sha(literal(queue))!='ba5dc660faf80bd2ea741a7838280d095c8a5766a8b51115ad56791ad0b49b2a'
            or len(literal(full))!=917751 or sha(literal(full))!=ORIGIN['partial_JSON_sha256']):
        raise ValueError('Full literal old partial queue cannot be recovered.')
    if sha(parent.ORIGINAL_REQUEST.read_bytes())!=parent.ORIGINAL_REQUEST_SHA:raise ValueError('Physical reference contract differs.')
    old_req=json.loads(gzip.decompress(parent.ORIGINAL_REQUEST.read_bytes()))
    src=old_req['lanes']['rounded-core-B030-native-430-shutdown-resume']['source_state_json'].encode()
    if sha(src)!=parent.ORIGINAL_INPUT_SHA:raise ValueError('Original physical input differs.')
    contract=json.loads(src);props=contract['physical_parameters'];geo=contract['geometry_parameters']
    if sha(literal(props))!='4fa67643c13c83e4968938a0185720522c5fb7e1349bb26c78c4af2e27f33798' or sha(literal(geo))!='b733187ae8b75a48b2bc386bc7b8cd23fd1d62f52c51cb193320e22d8e5b861c':
        raise ValueError('Source metric or predicate differs.')
    source=dict(origin=ORIGIN,source_last_backend_required_scalar_rows=3516474,source_last_backend_extra=t['retained_working_feasible_base_extra'],
        source_external_shutdown_resume_receipt=t['source_external_runner_shutdown_resume_receipt'],
        source_cost_ledger=dict(source_run=ORIGIN['run_id'],source_job=ORIGIN['job_id'],source_original_FINAL_sha256=FINAL,
             actual_new_disjoint_source_cost={k:v for k,v in history.items() if k!='prior_cost_ledger'},
             prior_ledger_bound_request_sha256=ORIGIN['request_sha256'],prior_ledger_bound_by_full_terminal=True,
             recorded_chain_scientific_seconds_lower_bound=history['prior_cost_ledger']['recorded_chain_scientific_seconds_lower_bound']+history['elapsed_seconds'],
             recorded_chain_scientific_seconds_is_exact=False,earlier_censored_work_still_unknown=True))
    start=dict(initial_fine_and_observed_scan=t['actual_retained_qualification'],initial_observed_peaks=t['actual_retained_observed_peak_summary'])
    return source,ORIGIN,start,driver.hard.Parameters(**props),geo,driver.np.asarray(q),driver.np.asarray(t['actual_complete_required_radial_nodes']),t['actual_complete_required_peak_orbits'],1536,t['actual_backend_local_trust'],t


def once(src,before,after):
    if src.count(before)!=1:raise ValueError('Original working startup seam is not unique: '+before[:80])
    return src.replace(before,after)


def rebuild(src):
    a=src.index('    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION",')
    b=src.index('        for outer in range(args.outer):',a)+len('        for outer in range(args.outer):')
    src=src[:a]+'''    hard.emit("WORKING_ROWS_BACKTRACK_DEFINITION",dict(schema=SCHEMA,actual_parent=source["origin"],
        required_source_literal_sha256=digest(raw),actual_working_rows=len(working),source_occurrence="outer36 metric, original queue before any candidate",
        same_original_physical_and_native_parameters=True,prior_completed_localizers_replayed=0,
        paid_prior_19_complete_J_with_no_live_partial_J=True,fine_1973_qualification_separate_from_required_1979=True))
    snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT","actual516_before_resuming_original4261")
    try:
        resumed=finish_saved(args,terminal,ledger,counts,par,geo,deadline,best_eta,actual_trust)
        last_trial=resumed["trial"];pending=resumed["pending"];proposed_working=resumed["working"]
        receipt.update(completed_candidates=last_trial["observed_peaks"]["completed_candidate_count"],
                       remaining=last_trial["observed_peaks"]["unresolved_candidate_count"],qualification_completed=resumed["resolved"])
        if not resumed["resolved"]:
            snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
            raise hard.EndSegment("actual source queue still unresolved")
        if resumed["accepted"]:
            q=np.asarray(last_trial["q"]).copy();best_scan=resumed["qualified"];best_eta=best_scan["accepted_eta_max"]
            best_observed=resumed["observed"];best_fine_nodes=actual_fine_nodes.copy()
            best_geo=OriginalMarginState.exact(resumed["geo_margin"]);retained_working_base_extra=resumed["e"]
            current_full_library_values_known=True
        proposed_trust=resumed["trust"];trust_decision_completed=True
        receipt.update(accepted=resumed["accepted"],source_outer36_decision_completed=True,
                       natural_backend_return_fabricated=False,source_outer36_actual_normalized_displacement=resumed["displacement"],
                       proposed_next_trust=proposed_trust,actual_physical_pending=len(pending),actual_working_pending=len(proposed_working))
        snapshot("WORKING_ROWS_COMPLETE_CHECKPOINT",last_trial["reason"])
        for outer in range(terminal["outer"]+1,terminal["outer"]+1+args.outer):'''+src[b:]
    src=once(src,'    current_outer, phase = -1, terminal["phase"]','''    current_outer, phase = terminal["outer"], terminal["phase"]
    receipt=dict(source_run=46146663846,source_trial_q_binary64_sha256=terminal["last_trial_not_implicitly_accepted"]["q_binary64_sha256"],
        original_queue_count=4261,prior_whole_run_completed_candidates=30468,source_completed_on_this_queue=0,
        new_enumeration_or_old_coarse_fine_scan=False,source_outer36_decision_completed=False)''')
    return once(src,'            "source_partial1906_resume_receipt":source_partial_resume_receipt,',
                '            "source_partial1906_resume_receipt":source_partial_resume_receipt,\n            "source_r714_saved_queue_receipt":dict(receipt),')


def main():
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':raise SystemExit('Bound public Actions required.')
    global parent,driver
    import r692_actual34aa_working_jacobian_resume as parent
    from r692_unfinished_working_derivatives import InterruptedRows
    from r714_paid_trial_completion import finish
    buf=parent.PREVIOUS.read_bytes()
    if sha(buf)!=parent.PREVIOUS_SHA:raise ValueError('Original working continuation loop differs.')
    driver=types.ModuleType('r714_bound_physical_driver');driver.__file__=str(parent.PREVIOUS)
    exec(compile(rebuild(buf.decode()),str(parent.PREVIOUS),'exec'),driver.__dict__)
    driver.SCHEMA=SCHEMA;driver.source_input=load;driver.WorkingRows=InterruptedRows
    driver.finish_saved=lambda *a:finish(driver,*a)
    driver.main()


if __name__=='__main__':main()
