"""Use the exact pending 97559b material queue before the old outer's exchange."""
from __future__ import annotations
import numpy as np


def finish(driver,args,terminal,ledger,counts,par,geo,deadline,best_eta,actual_trust):
    old=driver.old;ids=driver.digest
    trial=terminal['last_trial_not_implicitly_accepted'];q=np.asarray(trial['q']);scan=trial['full_fine_scan']
    prior=trial['observed_peaks'];fine_nodes=np.asarray(terminal['actual_required_fine_radial_nodes'])
    scope=dict(q_binary64_sha256=trial['q_binary64_sha256'],oracle_identity=prior['oracle_identity'],
               full_observation_FFT_nodes=3072,full_observation_radial_nodes=fine_nodes.tolist(),
               unresolved_candidate_count=4261,source_completed_peaks=[],source_completed_candidate_count=0,
               source_original_candidate_count=4261,source_completed_point_objective_evaluations=0,
               source_partial_localizer_elapsed_seconds=prior['elapsed_seconds'])
    fine=ledger.create(par,fine_nodes,3072,args.point_batch_size)
    try:
        state=fine.prepare(q)
        obs=driver.localize_saved_brackets(fine,state,prior['remaining_unprocessed_candidates'],scope,
            geo['mean_E_floor'],geo['det_floor'],geo['geometry_margin'],deadline,args.angle_tolerance,args.localizer_batch_size)
        scales=np.r_[np.full(2*fine.uniform.block,.5),np.full(par.radial_count,.2),np.full(par.radial_count,.15),.1]
    finally:
        ledger.retire(fine)
    closed=obs['status']=='observed_brackets_localized' and obs['unresolved_candidate_count']==0
    counts['localizer_candidates']+=obs['new_candidate_count']
    counts['localizer_completed_candidates']+=obs['new_completed_candidate_count']
    counts['localizer_point_objective_evaluations']+=obs['new_point_objective_evaluations']
    counts['source_remaining_brackets_newly_executed_or_completed']+=obs['new_completed_candidate_count']
    counts['localizer_unresolved_returns']+=obs['unresolved_candidate_count']
    counts['complete_localizations']+=int(closed)
    brief=old.compact_observation(obs)
    result=dict(trial=dict(trial,observed_peaks=brief,full_localization_completed=closed),
                resolved=closed,accepted=False,pending=list(terminal['recorded_unapplied_physical_peak_orbits']),
                working=list(terminal['recorded_unapplied_working_rows']),observed=brief,
                trust=actual_trust,source_36_prior_accepted=0)
    if not closed:
        result['trial']['reason']='source_literal_queue_still_incomplete'
        return result
    margin=geo['geometry_margin'];tol=geo['feasibility_tolerance']
    val=old.observation_metrics(scan,obs,margin)
    geo_peak=max(old.fine_geometry_limits(scan,margin).values())
    for p in obs['peaks']:
        if not p['field'].startswith('metric_'):geo_peak=max(geo_peak,float(p['value']))
    old_e=trial['backend_extra'];v=np.r_[q,old_e];lift=0.
    if geo_peak<=tol:
        v,lift=driver.lift_epigraph(v,val['accepted_eta_max']-old_e)
    if lift:counts['complete_fine_epigraph_lifts']+=1
    fine_e=float(v[-1])
    # Seven grid-only working rows and seven physical proposals were already taken before the clock.
    # Keep them all. Record newly localized proposals using the same original pre-lift evidence limit.
    evidence=[p for p in obs['peaks'] if p['value']>(old_e if p['field'].startswith('metric_') else 0.)+args.pending_peak_tolerance]
    addition=old.new_only(evidence,np.asarray(terminal['actual_complete_required_radial_nodes']),
                          terminal['actual_complete_required_peak_orbits'],1536)
    result['pending']=old.merge_peaks(result['pending'],addition)
    already={driver.row_key(z) for z in result['working']}
    # The old grid supplied the seven real stored rows. Unlisted grid points are below
    # their per-field selected front or coincide with existing material evidence.
    former=[dict(field=w['field'],s=w['s'],theta=w['theta'],value=w['evidence']['value']) for w in result['working']]
    for name in sorted({p['field'] for p in evidence}):
        group=sorted([p for p in evidence+former if p['field']==name],key=lambda p:-p['value'])
        keys=set()
        for p in group:
            row=dict(field=name,s=float(p['s']),theta=float(p['theta']),kind='actual',
                     evidence=dict(source='complete_fine_or_actual_angular_peak',
                                   value=float(p['value']),q_binary64_sha256=ids(q.tobytes())))
            k=driver.row_key(row)
            if k not in keys:
                keys.add(k)
                if k not in already:
                    result['working'].append(row);already.add(k)
            if len(keys)>=args.working_witnesses_per_field:break
    # The original trial had all required coarse and working rows and every box read.
    # Increasing e at fixed q preserves them. No uncomputed new minimum is assigned.
    inherited=(trial['physical_box_violation']<=tol and trial['working_row_violation']<=tol
               and min(trial['complete_required_minimum_by_group'].values())>=-tol
               and fine_e>=old_e and min(trial['working_minimum_by_group'].values())>=-tol)
    nested=trial['nested_quadrature'];quad=max(nested[k] for k in ('same_q_nested_FFT_metric_components_difference',
          'same_q_relative_mean_E_difference','same_q_tau_curvature_difference'))<=args.nested_quadrature_tolerance
    # The earlier grid's total point maximum plus all localized values cover the original finite rejection lists.
    # The invocation pins pending_peak_tolerance == feasibility_tolerance.
    if args.pending_peak_tolerance!=tol:raise ValueError('Source finite peak rejection tolerances differ')
    # Grid metric_plus/minus use the original smoothed sqrt. Their actual old top
    # values are among the seven recorded grid rows; do not replace them with the unsmoothed eta.
    grid_violation=any(p['value']>(fine_e if p['field'].startswith('metric_') else 0.)+tol for p in former)
    localized_violation=any(p['value']>(fine_e if p['field'].startswith('metric_') else 0.)+tol for p in obs['peaks'])
    any_bad=(grid_violation or localized_violation or geo_peak>tol or val['accepted_eta_max']>fine_e+tol)
    accept=(inherited and quad and not any_bad and val['accepted_geometry_violation_max']<=tol
            and val['accepted_eta_max']<best_eta-1e-12)
    r=result['trial']
    r.update(accepted=bool(accept),backend_extra=fine_e,separate_complete_fine_epigraph_lift=lift,
             minimum_by_group_is_saved_at_prior_epigraph=old_e,
             paid_same_q_lower_rows_remain_feasible_at_raised_epigraph=inherited,
             actual_complete_geometry_margin_violation=max(0.,geo_peak),actual_complete_eta=val['accepted_eta_max'],
             reason='source_actual_queue_completed_and_accepted' if accept else 'source_actual_queue_completed_and_rejected')
    if accept:counts['accepted_metric_steps']+=1
    elif any_bad:counts['fine_required_row_rejections']+=1
    delta=float(np.max(abs(q-np.asarray(terminal['actual_retained_q']))/scales)) if accept else 0.
    result.update(qualified=val,accepted=bool(accept),geo_margin=max(0.,geo_peak),e=fine_e,
                  displacement=delta,trust=min(args.maximum_trust,1.5*actual_trust) if accept and delta>=.9*actual_trust else actual_trust)
    counts['source_previous_incomplete_outer_trust_decisions_completed']+=1
    counts['outer_completed']+=1
    return result
