#!/usr/bin/env python3
"""Derive and bind the entire v2 amplitude driver plus one complete-row SOC.

This standard-library source construction runs no scientific computation.
The complete published v2 mean/amplitude body remains the base, with its
current-mean R688 Gram, R685 solver, full J/J*, norm, QP and true filters.
Only a real full-step geometry rejection can request the new correction.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path

BASE_SHA = '970f03adc4b11a85f13de9e9d13dcbcb7fef0dce4ab79c0d17b62bd0ed34c775'
SOC_SHA = '734c1fcc80006e7da52ea7aa8cda4dea02e75714b4b550c20f64dae9cfe67061'
PROJECTION_SHA = 'a2c6d334d40be88ac7edb2dd2e525da5583d9f723e33d5bae9d910c0adfe745e'
REPORT_SCHEMA = 'complete-mean-amplitude-and-inward-all-row-SOC-v1'
EXPECTED_ROLES = {
    'typed_soc': SOC_SHA, 'soc_projection': PROJECTION_SHA,
    'amplitude_rows': 'd494f92a3d212c40c8b602588c8cfe74f01ff332f116992ffca6469b3978ad8e',
    'amplitude_screen': 'e6be35e97702e4185f29fb8f9b7c326fd62083cb4027880956aacdf8b0ba296f',
    'mean_coarse': '9e7ca6ba0cf3821ab8498226354d8422c2cfacee1ef07dafb8fc5868968fb9e3',
    'mean_transform': 'b7eb35d5e7c1d32baf8d4e94c0c9651d46d5cbfea65a6c1c098ae24d42f0b624',
    'qp': '76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8',
    'coarse_qp_v3': 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4',
    'coarse_frame': '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da',
    'point': 'fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad',
    'inequalities': 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8',
    'exact_tail': '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216',
    'spectral_hessian': '29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4',
    'spectral': 'e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91'}
CENTERED_SHA = '5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Complete v2 source construction anchor changed: '+repr(old[:90]))
    return text.replace(old, new, 1)


def lineage():
    return dict(schema='complete-v2-amplitude-driver-plus-inward-SOC-derivation-v1',
        complete_base_driver_sha256=BASE_SHA, source_deriver_sha256=sha(__file__),
        expected_runtime_source_sha256=EXPECTED_ROLES,
        optional_centered_statistics_sha256=CENTERED_SHA,
        complete_base_body_bound=True, R688_current_mean_preconditioner_retained=True,
        R685_full_original_QP_retained=True, every_original_variable_and_norm_retained=True,
        original_curvature_and_amplitude_thresholds_unchanged=True,
        same_parent_A_applied_to_corrected_step=True,
        corrected_objective_prediction_not_borrowed_from_original_step=True,
        new_constraints_only_at_original_parent=True, negative_new_parent_bound_is_not_feasible_zero=True,
        parent_declared_derivation_not_relabelled=True,
        theorem_scope='Application of the existing R683 halfspace argument to typed g<=0 rows; no new local-MFCQ proof or continuous certificate',
        observed_fraction_inward_policy_is_numerical=True,
        new_scientific_execution_by_deriver=False)


SOC_ARGUMENTS = """    parser.add_argument('--typed-soc-source', type=Path, required=True)
    parser.add_argument('--soc-projection-source', type=Path, required=True)
    parser.add_argument('--soc-tau', type=float, default=0.0)
    parser.add_argument('--soc-inward-fraction', type=float, default=0.125)
    parser.add_argument('--soc-separation', choices=('none', 'rejected-extrema'), default='rejected-extrema')
"""

SOC_LOAD = """    paths.update(typed_soc=args.typed_soc_source.resolve(), soc_projection=args.soc_projection_source.resolve())
    for role in ('typed_soc', 'soc_projection'):
        if sha(paths[role]) != COMPLETE_SOC_DRIVER_DERIVATION['expected_runtime_source_sha256'][role]:
            raise ValueError('Changed complete typed SOC component: '+role)
    if (not np.isfinite([args.soc_tau,args.soc_inward_fraction]).all()
            or min(args.soc_tau,args.soc_inward_fraction)<0
            or args.soc_tau==args.soc_inward_fraction==0):
        raise ValueError('Declare a finite positive inward policy; do not loosen true acceptance thresholds')
    complete_soc_module=load('complete_original_geometry_and_amplitude_SOC',paths['typed_soc'])
"""

SOC_REPORT = """    report['complete_soc_driver_derivation']=COMPLETE_SOC_DRIVER_DERIVATION
    report['complete_rows_SOC_policy']=dict(
        source_sha256=sha(paths['typed_soc']), projection_source_sha256=sha(paths['soc_projection']),
        tau=args.soc_tau, inward_fraction=args.soc_inward_fraction, separation=args.soc_separation,
        maximum_corrections_per_original_direction=1,
        maximum_true_trials_per_direction=args.line_trials+1,
        trigger='Only actual alpha=1 finite/domain/true-descent passes and complete curvature/amplitude failure',
        correction='Every original C row retained; optionally append actual rejected extrema evaluated at the original parent',
        inward='tau*||d||^3+theta*max_i(max(c_i(d),0)) in fixed parent normalized rows',
        original_QP_and_current_mean_preconditioner_unchanged=True,
        original_true_geometry_thresholds_unchanged=True,
        corrected_model_recomputed_at_same_parent=True,
        every_new_true_extremum_retained_in_permanent_memory=True,
        fallback='Unchanged original ray, starting alpha=1/2 after its rejected full step',
        local_MFCQ_or_cubic_constants_certified=False, continuous_geometry_certified=False)
    report['amplitude_design_constraints']['squared_SOC_implemented']=True
"""

LINE_SEARCH = r"""        record['original_model_step_squared_norm']=original_model_step_squared_norm
        record['complete_rows_SOC']=dict(attempted=False,proposal_available=False,
            reason='No eligible complete full-step geometry rejection observed')

        def read_actual_trial(point, alpha, trial_slope, *, update_kind, ray_index=None):
            error=None
            try:
                trial_state=problem._state(point)
                trial_residual=trial_state.result*problem.sqrt_multiplicity[None,:,None]
                finite=bool(np.isfinite(trial_residual).all())
                stats=statistics(point,trial_residual,trial_state) if finite else {}
                del trial_state
                merit=objective_value(stats) if finite else float('inf')
                finite=bool(finite and np.isfinite(merit))
            except (FloatingPointError,OverflowError,ValueError,np.linalg.LinAlgError) as exception:
                trial_residual=None;finite=False;stats={};merit=float('inf');error=repr(exception)
            feasible=bool(finite and stats['rho_sample_min']>0 and stats['min_relative_E']>0
                and stats['min_relative_determinant']>0)
            descent=bool(finite and merit<old_merit
                and (trial_slope>=0 or merit<=old_merit+.0002*alpha*trial_slope))
            curvature=None;filter_result=None;curvature_feasible=False
            if feasible and descent:
                try:
                    curvature=geometry(point);filter_result=curvature_filter(point,curvature)
                except (FloatingPointError,OverflowError,ValueError,np.linalg.LinAlgError) as exception:
                    curvature=dict(complete=False,amplitude_screen=dict(complete=False,passed=False),
                        actual_read_error=repr(exception))
                    filter_result=dict(passed=False,actual_read_error=repr(exception),
                        scope='Numerical trial read failure, not geometric infeasibility')
                curvature_feasible=bool(filter_result['passed'])
            amplitude_filter=None if curvature is None else curvature.get('amplitude_screen')
            amplitude_feasible=bool(amplitude_filter is not None and amplitude_filter.get('passed',False))
            trial=dict(index=len(record['trials']),alpha=alpha,update_kind=update_kind,
                original_ray_trial_index=ray_index,merit=merit,finite=finite,feasible=feasible,
                descent=descent,half_objective_slope_used=trial_slope,
                curvature_feasible=curvature_feasible,curvature_points=curvature,
                curvature_filter=filter_result,statistics=stats,arithmetic_error=error,
                amplitude_filter=amplitude_filter,amplitude_feasible=amplitude_feasible,
                amplitude_not_read_reason=None if curvature is not None else
                    'Rejected by actual objective/domain before any geometric acceptance')
            if curvature is not None:
                trial['new_permanent_amplitude_locations']=remember_amplitude(curvature)
                remembered_curvature=[];remembered_radius=[]
                for location in (curvature.get('observation_grid_worst'),curvature.get('worst')):
                    value=add_actual_location(location,witnesses)
                    if value is not None:remembered_curvature.append(value)
                value=add_actual_location(curvature.get('maximum_radius_point'),radius_witnesses)
                if value is not None:remembered_radius.append(value)
                trial['new_permanent_curvature_locations']=remembered_curvature
                trial['new_permanent_radius_locations']=remembered_radius
                if curvature.get('complete') and curvature.get('amplitude_screen',{}).get('complete'):
                    curvature['memory_counts_at_complete_read']=dict(curvature=len(witnesses),radius=len(radius_witnesses))
            record['trials'].append(trial)
            event_trial=dict(trial);event_trial['curvature_points']=compact_geometry(curvature)
            event(event='mean_metric_complete_SOC_actual_trial',direction=index,**event_trial)
            return trial,trial_residual

        def actual_trial_passes(trial):
            return bool(trial['finite'] and trial['feasible'] and trial['descent']
                and trial['curvature_feasible'] and trial['amplitude_feasible'])

        alpha=1.0
        for ray_index in range(args.line_trials):
            point=x+alpha*step
            trial,trial_residual=read_actual_trial(point,alpha,slope,
                update_kind='original_ray',ray_index=ray_index)
            selected=None
            if actual_trial_passes(trial):
                selected=(point,trial_residual,trial,slope,original_model_step_squared_norm,
                    float(np.linalg.norm(coordinate_step)))
            elif (ray_index==0 and trial['finite'] and trial['feasible'] and trial['descent']
                    and (trial.get('curvature_points') or {}).get('complete') is True
                    and (trial.get('amplitude_filter') or {}).get('complete') is True):
                soc_started=time.monotonic();soc_counts_before=counts.copy()
                soc_parent=complete_soc_module.CompleteRowsSOC(problem,x,active_rows,active_bounds,
                    active_metadata,geometry_module=geometry_module,point_module=point_module,
                    observed_module=implementation,inequality_module=inequality_module,
                    amplitude_module=amplitude_rows_module,budgets=amplitude_budgets,
                    projection_source=paths['soc_projection'],source_sha256_by_role=report['source_sha256_by_role'],
                    observation_carrier_sha256=report['observation_carrier_sha256'],
                    model_definition=context.definition(),parent_bundle_sha256=mean_parent_sha,
                    block_columns=args.active_block_columns,absolute_curvature_cap=args.curvature_cap)
                extension=dict(complete=True,extension_available=True,added_rows=0,
                    reason='No additional separation requested')
                soc_point=soc_z=soc_e=None
                try:
                    if args.soc_separation=='rejected-extrema':
                        extension=soc_parent.extend_from_rejected_extrema(trial['curvature_points'],transpose,
                            args.outdir/f'SOC-separated-rows-{index:03d}',actual_filter=trial['curvature_filter'])
                    if extension.get('extension_available'):
                        soc_point,soc_z,soc_e,soc_detail=soc_parent.propose(coordinate_step,lift,point,trial,
                            tau=args.soc_tau,inward_fraction=args.soc_inward_fraction,
                            feasibility_tolerance=args.qp_feasibility_tolerance)
                    else:
                        soc_detail=dict(attempted=False,proposal_available=False,
                            reason='Parent is not feasible at a newly separated row; this branch has no restoration')
                except (FloatingPointError,OverflowError,np.linalg.LinAlgError) as exception:
                    soc_detail=dict(attempted=True,proposal_available=False,
                        reason='Numerical complete-row correction unavailable',arithmetic_error=repr(exception),
                        global_geometric_infeasibility_proved=False)
                soc_detail['separation']=extension
                soc_detail['corrected_candidate_A_entry_counts']={key:0 for key in counts}
                record['complete_rows_SOC']=soc_detail
                if extension.get('current_cache_bytes') is not None:
                    record['total_scratch_row_cache_bytes']+=extension['current_cache_bytes']
                if soc_point is not None:
                    before_model=counts.copy()
                    try:
                        soc_Az=A.matvec(soc_z)
                        if not np.isfinite(soc_Az).all():raise FloatingPointError('Nonfinite corrected model A*z')
                        soc_slope=float(model_residual@soc_Az)
                        soc_model_squared=float(soc_Az@soc_Az)
                        soc_model_change=2*soc_slope+soc_model_squared
                        soc_norm=float(np.linalg.norm(soc_z))
                        soc_q0=.5*float(model_residual@model_residual)
                        soc_qz=.5*float((soc_Az+model_residual)@(soc_Az+model_residual))+.5*damping*damping*soc_norm*soc_norm
                        if not np.isfinite([soc_slope,soc_model_squared,soc_model_change,soc_norm,soc_q0,soc_qz]).all():
                            raise FloatingPointError('Nonfinite corrected same-parent model scalars')
                        soc_detail['corrected_same_parent_model']=dict(half_objective_slope=soc_slope,
                            squared_model_step_norm=soc_model_squared,quadratic_predicted_actual_change=soc_model_change,
                            quadratic_predicted_actual_objective=old_merit+soc_model_change,
                            q0=soc_q0,qz=soc_qz,regularized_model_decrease=soc_q0-soc_qz,
                            damping=damping,coordinate_norm=soc_norm,
                            same_parent_and_complete_A=True,original_step_prediction_reused=False)
                        del soc_Az
                        soc_checkpoint=args.outdir/f'complete-SOC-direction-{index:03d}.npz'
                        np.savez_compressed(soc_checkpoint,augmented_step=soc_z,
                            augmented_correction=soc_e,original_augmented_step=coordinate_step,
                            step=lift(soc_z),integrated_scale=coordinates.scale,
                            coarse_diagonal=coarse_diagonal,coarse_cholesky=coarse_chol)
                        soc_detail.update(corrected_checkpoint=str(soc_checkpoint),
                            corrected_checkpoint_sha256=sha(soc_checkpoint))
                        soc_trial,soc_residual=read_actual_trial(soc_point,1.0,soc_slope,
                            update_kind='complete_rows_soc')
                        soc_detail['corrected_actual_trial_index']=soc_trial['index']
                        soc_detail['corrected_actual_trial_accepted']=actual_trial_passes(soc_trial)
                        if actual_trial_passes(soc_trial):
                            selected=(soc_point,soc_residual,soc_trial,soc_slope,soc_model_squared,soc_norm)
                    except (FloatingPointError,OverflowError,np.linalg.LinAlgError) as exception:
                        soc_detail['corrected_model_or_trial_numeric_error']=repr(exception)
                        soc_detail['corrected_actual_trial_accepted']=False
                    finally:
                        soc_detail['corrected_candidate_A_entry_counts']={key:counts[key]-before_model[key] for key in counts}
                soc_detail['whole_SOC_outer_A_entry_counts']={key:counts[key]-soc_counts_before[key] for key in counts}
                soc_detail['seconds']=time.monotonic()-soc_started
                record['outside_inner_calls']['SOC_candidate_model_matvec']=soc_detail['corrected_candidate_A_entry_counts']['jvp']
                event(event='complete_rows_SOC_finished',direction=index,
                    attempted=soc_detail.get('attempted'),proposal_available=soc_detail.get('proposal_available'),
                    accepted=soc_detail.get('corrected_actual_trial_accepted',False),
                    added_rows=extension.get('added_rows'),seconds=soc_detail['seconds'],
                    actual_outer_A_calls=soc_detail['whole_SOC_outer_A_entry_counts'])
                del soc_parent,soc_point,soc_z,soc_e
            if selected is not None:
                x,residual,accepted_trial,accepted_slope,accepted_model_squared,accepted_norm=selected
                accepted_alpha=accepted_trial['alpha'];merit=accepted_trial['merit']
                accepted_change=2*accepted_alpha*accepted_slope+accepted_alpha*accepted_alpha*accepted_model_squared
                full_change=2*accepted_slope+accepted_model_squared
                predicted=-accepted_change;full_predicted=-full_change
                ratio=(old_merit-merit)/predicted if predicted>0 else None
                full_ratio=(old_merit-merit)/full_predicted if full_predicted>0 else None
                record.update(accepted=True,accepted_alpha=accepted_alpha,new_merit=merit,
                    accepted_update_kind=accepted_trial['update_kind'],accepted_trial_index=accepted_trial['index'],
                    accepted_augmented_full_direction_norm=accepted_norm,
                    accepted_actual_to_same_step_predicted_decrease=ratio,
                    actual_to_full_step_predicted_decrease=full_ratio,
                    accepted_model_prediction=dict(half_objective_slope=accepted_slope,
                        squared_model_step_norm=accepted_model_squared,alpha=accepted_alpha,
                        predicted_actual_change=accepted_change,predicted_actual_objective=old_merit+accepted_change,
                        actual_decrease=old_merit-merit,update_kind=accepted_trial['update_kind'],
                        same_selected_true_Phi_units=True,damping_in_actual_Phi_prediction=False))
                report['current']=accepted_trial['statistics']
                current_geometry=accepted_trial['curvature_points']
                record['accepted_amplitude_filter']=accepted_trial['amplitude_filter']
                record['accepted_curvature_points']=current_geometry
                record['accepted_curvature_filter']=accepted_trial['curvature_filter']
                candidate=args.outdir/f'accepted-{index:03d}.npz';save_bundle(candidate,x)
                record.update(accepted_bundle=str(candidate),accepted_bundle_sha256=sha(candidate))
                if accepted_alpha==1 and ratio is not None and ratio>.75:
                    damping=max(1e-08,damping/2)
                break
            alpha/=2
        record['total_A_entry_counts_after_line_search']=counts.copy()
        del A,model_residual,coordinate_step,active_rows,active_bounds
"""


def derive(base_source):
    base_source=Path(base_source)
    if sha(base_source)!=BASE_SHA:
        raise ValueError('Use the exact complete repaired v2 amplitude driver')
    text=base_source.read_text()
    info=lineage()
    text=replace_once(text, 'def _mean_coarse_sources(args, paths):',
        'COMPLETE_SOC_DRIVER_DERIVATION = '+repr(info)+'\n\ndef _mean_coarse_sources(args, paths):')
    text=replace_once(text, '    args = parser.parse_args()\n', SOC_ARGUMENTS+'    args = parser.parse_args()\n')
    anchor="    amplitude_rows_module=load('complete_original_free_amplitude_rows',paths['amplitude_rows'])\n"
    text=replace_once(text,anchor,SOC_LOAD+anchor)
    text=replace_once(text,"schema='complete-mean-design-with-held-amplitude-budgets-v2'",'schema='+repr(REPORT_SCHEMA))
    anchor="    output = args.outdir / 'report.json'\n"
    text=replace_once(text,anchor,SOC_REPORT+anchor)
    text=replace_once(text,
        '        del model_step, A, model_residual, djet, integrated_point, coordinate_step, active_rows, active_bounds\n',
        '        original_model_step_squared_norm=float(model_step@model_step)\n'
        '        del model_step,djet,integrated_point\n')
    start='        alpha = 1.0\n        for trial_index in range(args.line_trials):\n'
    stop="        if not record['accepted']:\n"
    if text.count(start)!=1 or text.count(stop)!=1:
        raise ValueError('The entire original line-search block must be bound exactly once')
    first=text.index(start);last=text.index(stop,first)
    text=text[:first]+LINE_SEARCH+text[last:]
    text=replace_once(text,
        'No original geometric row is removed and no squared SOC is implemented here.',
        'Every original geometric and amplitude row remains. One finite complete-row inward correction may be proposed and independently reread, with the same actual true objective and full geometry thresholds. The numerical inward policy is not a certified local MFCQ bound.')
    text=replace_once(text,'#!/usr/bin/env python3\n',
        '#!/usr/bin/env python3\n# Complete typed-row SOC derivation: '+json.dumps(info,sort_keys=True)+'\n')
    ast.parse(text);compile(text,str(base_source)+'+complete-SOC','exec')
    if len(text.encode())>=100000:
        raise ValueError('Keep the complete scientific source below the repository source bound')
    return text


def bind_report(report, driver, repo, *, base_source=None):
    """Exact complete body + actual report binding; no old binder relabelling."""
    source=Path(repo)/'topics/visible-flex-larger-amplitude/scripts/resume_20261126'
    base=Path(base_source) if base_source is not None else source/'fullclosed_mean_metric_amplitude_qp_v2.py'
    expected=derive(base);digest=hashlib.sha256(expected.encode()).hexdigest()
    if Path(driver).read_text()!=expected or report.get('source_sha256')!=digest:
        raise ValueError('The actual report does not match the entire complete-SOC driver body')
    if report.get('schema')!=REPORT_SCHEMA or report.get('complete_soc_driver_derivation')!=lineage():
        raise ValueError('The typed-row SOC report has another actual schema or complete derivation')
    roles=report.get('source_sha256_by_role',{})
    for role,value in EXPECTED_ROLES.items():
        if roles.get(role)!=value:raise ValueError('Changed actual complete-SOC runtime role '+role)
    scalar=report.get('selected_scalar_objective_key')
    if scalar=='centered_phi_normalized':
        if roles.get('centered_loss')!=CENTERED_SHA:raise ValueError('Changed actual centered scalar')
    elif scalar!='phi_normalized':raise ValueError('Unknown same-model actual scalar')
    return dict(schema='verified-complete-mean-amplitude-SOC-source-binding-v1',
        driver_sha256=digest, complete_base_driver_sha256=BASE_SHA,
        actual_report_schema=REPORT_SCHEMA, actual_source_commit=report.get('source_commit'),
        verified_driver_derivation=lineage(), source_roles=EXPECTED_ROLES,
        declared_parent_derivation_not_relabelled=True,
        physics=dict(exact_tail_source_sha256=EXPECTED_ROLES['exact_tail'],
            actual_context=report.get('exact_tail_context')))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();text=derive(a.base)
    if a.out.exists() and a.out.read_text()!=text:raise FileExistsError(a.out)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(text)
    print(json.dumps(dict(driver=str(a.out.resolve()),driver_sha256=sha(a.out),
        bytes=a.out.stat().st_size,source_deriver_sha256=sha(__file__),scientific_execution=False)))


if __name__=='__main__':main()
