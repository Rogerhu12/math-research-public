#!/usr/bin/env python3
"""Request189 necessary persistent-normal conclusion; no scientific recomputation.

Read every actual direction/alpha/nested normal record from all sixteen blocks.
Return one bounded semantic conclusion with all128 planned direction addresses,
all actual alpha metadata, original counters/stops/errors and initial/final120FD.
Large matrices and most intermediate point vectors remain Actions-only. Shared
constant metadata and accepted-merit references remove repetition, not trials.
No encoded raw tree, arbitrary reconstruction parts or invented science.
"""
from __future__ import annotations
import argparse
from collections import Counter
from decimal import Decimal, InvalidOperation
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='root_20261115_completed_ten_predictor_normal_resume_readout.py'
PRODUCER='geometry_20261115_completed_ten_predictor_normal_resume.py'
PRODUCER_SHA='295c375b016a16bbdd7bffe68db7ffcdd3f715c33eee7a20147e9b5c379d0f8a'
PRODUCER_SCHEMA='R259-completed-ten-persistent-full-three-normal-continuation-v1'
STATUS_NAME='completed-ten-predictor-normal-resume-status.json'
SCHEMA='request189-persistent-ten-full3-normal-necessary-readback-v1'
BASE='root_20261115_fixed_power_ten_joint_newton_scalar_readout.py'
BASE_SHA='728ac09e7f008f06396bf578822b1107fa9cfcdb806a64e01d0cc130c303d3ef'
LIMIT=90000


def encoded(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,allow_nan=False,
        separators=(',',':')).encode('ascii')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    raw=encoded(value)
    return dict(canonical_bytes=len(raw),canonical_sha256=digest(raw))


def file_identity(path):
    raw=Path(path).read_bytes()
    return dict(file=Path(path).name,bytes=len(raw),sha256=digest(raw))


def load_reader():
    if digest((HERE/BASE).read_bytes())!=BASE_SHA:
        raise ValueError('The frozen original ten-FD metadata reader differs')
    spec=importlib.util.spec_from_file_location('_request189_original_metadata_reader',HERE/BASE)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def selected_extrema(rows):
    """Order existing finite Decimal word values; do not form any new scientific scalar."""
    low=None;high=None;nonfinite=[]
    for global_index,trial in rows:
        value=trial.get('actual_merit')
        if value is None:
            continue
        try:
            word=Decimal(str(value))
        except (InvalidOperation,ValueError) as error:
            nonfinite.append(dict(direction=global_index,trial=trial.get('trial'),
                original_value=value,metadata_parse_error=repr(error)))
            continue
        if not word.is_finite():
            nonfinite.append(dict(direction=global_index,trial=trial.get('trial'),
                original_value=value))
            continue
        item=(word,global_index,trial)
        if low is None or word<low[0]:low=item
        if high is None or word>high[0]:high=item
    def original(item):
        if item is None:return None
        _,global_index,trial=item
        return dict(direction=global_index,**{key:trial[key] for key in (
            'trial','alpha','accepted','actual_merit','actual_unit_equations',
            'original_Armijo_bound','reason') if key in trial})
    return dict(minimum_recorded_finite_merit=original(low),
        maximum_recorded_finite_merit=original(high),
        original_nonfinite_or_malformed_merit_records=nonfinite,
        only_ordering_of_original_values_not_norms_differences_or_recomputed_merit=True)


def description(base,reader,value,path,binary64=False):
    result=reader.description(value,path,binary64)
    if not isinstance(value,dict):return result
    matrix_key='three_by_ten_parameter_jacobian' if binary64 else 'complete_three_by_ten_forward_response'
    matrix=result.pop(matrix_key,None)
    result[matrix_key+'_identity']=identity(matrix)
    result['complete_matrix_words_transported']=False
    # The whole original description was already checked; these large diagnostics
    # do not define the required compact restart or original final-gate claims.
    for key in ('low_mode_trajectory_max_by_mode','low_two_by_two_right_condition_max_by_mode'):
        if key in result:result[key+'_identity']=identity(result.pop(key))
    return result


def existing_candidate_extrema(rows):
    """Select original merit words with their complete nested metadata location."""
    low=None;high=None;nonfinite=[]
    for outer,alpha,update,trial,item in rows:
        value=item.get('actual_merit')
        if value is None:continue
        try:word=Decimal(str(value))
        except (InvalidOperation,ValueError) as error:
            nonfinite.append(dict(location=[outer,alpha,update,trial],original=value,
                metadata_parse_error=repr(error)))
            continue
        if not word.is_finite():
            nonfinite.append(dict(location=[outer,alpha,update,trial],original=value))
            continue
        record=(word,outer,alpha,update,trial,item)
        if low is None or word<low[0]:low=record
        if high is None or word>high[0]:high=record
    def view(record):
        if record is None:return None
        _,outer,alpha,update,trial,item=record
        keys=('actual_merit','actual_unit_equations','original_Armijo_bound','accepted',
            'complete_three_target_deviation','complete_three_target_deviation_merit',
            'projection_active','reason')
        return dict(location=dict(direction=outer,alpha_index=alpha,
            normal_update=update,normal_trial=trial,predictor=update==-1),
            original={key:item[key] for key in keys if key in item},
            complete_original_candidate_identity=identity(item))
    return dict(minimum_original_merit=view(low),maximum_original_merit=view(high),
        original_nonfinite_or_unparseable_merit=nonfinite,
        only_ordered_original_scalar_words_no_new_scientific_quantity=True)


def build(status,raw,directory,rules,compute_outcome):
    base=load_reader()
    reader=base.Readback()
    if status.get('schema')!=PRODUCER_SCHEMA or status.get('source_sha256')!=PRODUCER_SHA:
        raise ValueError('Do not relabel an old eight-direction or nine-coordinate producer')
    sources=status.get('consumed_source_sha256',{})
    if len(sources)!=49 or sources.get(PRODUCER)!=PRODUCER_SHA:
        raise ValueError('The complete current49 consumed-source closure differs')
    fields=['phase','run_id','source_commit','actual_origin','parameter_recipe',
        'continuation_contract','input_sha256','initial_ten_parameter_words',
        'fixed_scale_original_actual157_words','fixed_scale_origin','original_parent_radius',
        'parent_radius_not_used_as_new_shape_scale','decimal_digits','rounding',
        'original_mesh_nodes','field_and_tail_modes','selected_catalogue_index',
        'catalogue_reselection_performed','all_ten_parameters_can_change',
        'fixed_physical_scales','fixed_scales_computed_once_from_actual157_words',
        'scaled_trust_radius','shape_frozen_for_all_ten_forward_FD_trials_and_final_consumers',
        'accepted_point_count','attempted_outer_directions','original_trial_records',
        'current_accepted_ten_parameter_words','unvisited_outer_indices','unvisited_block_indices',
        'old_nine_parameters_relabelled_as_new','new_shape_parameter_index',
        'input_tables_not_reformed_in_high_precision',
        'source_bound_original112_terminal_and699_chain_retained',
        'full_ten_QR_or_Cauchy_is_a_proposal_not_an_accuracy_or_rank_gate',
        'high_mode_Schur_elimination_or_current_nonlinear_native_performed',
        'native_nonlinear_solver_called','nonzero_field_completed','success',
        'diagnostic_completed','resource_partial','stop_reason','exception','traceback',
        'scientific_failure_not_inferred','actual_initial_merit',
        'original_Armijo_coefficient_exact_binary64_lift','final_ten_parameter_words',
        'final_selected_shape_coefficient','final_original_three_merit',
        'high_precision_original_unit_stopping_tolerance_met',
        'high_precision_full112_linear_right_tolerance_met',
        'binary64_projection_original_unit_stopping_tolerance_met',
        'binary64_projection_full112_linear_right_tolerance_met',
        'initial_final_complete_ten_axis_three_step_Decimal_and_binary64_FD_attempted',
        'final_continuous_scalar_and453_circle_consumers_at_explicit_projection_only',
        'high_precision_complete_interval_domain_or_exact_derivative_accuracy_certified',
        'independent_ten_model_call_counts','fresh_original_nine_model_call_counts',
        'complete_original_event_ledger','elapsed_wall_seconds',
        'zero_extension_not_evaluated_in_nonzero_ten_resume',
        'no_previous_parent_state_J_merit_or_FD_used_as_current',
        'old_nine_model_role','fresh_initial_parent_word_comparison',
        'original_normal_evaluation_counts','additional_primal_and_forward_calls_are_explicit_new_science']
    out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,producer_sha256=PRODUCER_SHA,
        original_status=dict(file=STATUS_NAME,bytes=len(raw),sha256=digest(raw)),
        readout_source=file_identity(__file__),base_metadata_reader=file_identity(HERE/BASE),
        **base.pick(status,fields),actual_compute_outcome=compute_outcome,
        complete_current_source_closure_count=len(sources),
        complete_current_source_closure_identity=identity(sources),
        actual_rule_sync=base.compact_rules(rules),
        original_policy_identity=identity(status.get('policy')),
        fixed_shape_definition_identity=identity(status.get('fixed_shape_definition')),
        fixed_shape_evidence_identity=identity(status.get('fixed_shape_evidence')),
        no_scientific_evaluation_or_matrix_norm_FD_recalculation=True,
        one_small_conclusion_not_a_data_reconstruction_protocol=True,
        raw_Git_Release_or_artifact_retention=False)
    for name in ('original_nine_literal_binding','new_ten_literal_binding'):
        value=status.get(name)
        if value is not None:
            out[name]=dict(identity=identity(value),original=base.pick(value,[
                'schema','source','canonical_binding_sha256','parameter_dimension','parameter_order',
                'decimal_digits','rounding','original_mesh_nodes','field_and_tail_modes',
                'complete_original_tail_J_consumed',
                'new_control_table_words_are_binary64_source_samples_then_exact_lifts',
                'new_shape_table_formation_recomputed_in_Decimal',
                'no_discrete_rounding_derivative_or_interval_accuracy_certificate',
                'frozen_original_native_anchor_J_is_not_a_new_g_nonlinear_tail_response']))
    for name,binary in (('initial',False),('final',False),
            ('initial_binary64_projection',True),('final_binary64_projection',True)):
        out[name]=description(base,reader,status.get(name),name,binary)
    for name in ('initial_projection_contract','final_projection_contract'):
        if name in status:
            out[name]=dict(identity=identity(status[name]),
                original_scalar_flags=base.scalar_fields(status[name]),
                actual_failures_and_exceptions=base.exceptions_in(status[name],name))
    steps=status.get('outer_steps',[])
    if not isinstance(steps,list) or len(steps)>128:
        raise ValueError('The original128-direction list is malformed')
    columns=['direction','started','accepted','accepted_alpha','merit_before',
        'merit_after','formed_full3_slope','alpha_trial_count','unvisited_alpha_indices',
        'original_stop_reason','complete_original_record_sha256']
    alpha_columns=['direction','alpha_index','alpha','outer_candidate_selected',
        'predictor_merit','selected_merit','primal_attempts','primal_returns',
        'normal_response_attempts','normal_response_returns','normal_updates',
        'normal_trial_records','temporary_working_updates','projected_proposals',
        'original_selected_Armijo_bound','normal_stop_reason_index']
    rows=[];alpha_rows=[];alpha_presence=[]
    trial_items=[];trial_reasons=Counter();domain_counts=Counter()
    normal_stop_reasons=Counter();normal_trial_reasons=Counter();normal_stop_values=[]
    direction_errors=[];trial_errors=[];named_errors=[]
    selected_points=[];inflight=[];normal_presence=[]
    accepted_count=0;all_normal_items=[];normal_model_count=0
    observed=dict(original_alpha_attempts=0,actual_primal_attempts=0,actual_primal_returns=0,
        fresh_complete_ten_normal_response_attempts=0,fresh_complete_ten_normal_response_returns=0,
        started_normal_updates=0,normal_trial_records=0,temporary_normal_working_updates=0,
        projected_normal_proposals=0,outer_candidates_selected_from_corrected_points=0)
    def vector_if(value,key,size,path):
        if key in value:reader.vector(value[key],size,path+'.'+key)
    def candidate_fields(item,path):
        if not isinstance(item,dict):
            reader.metadata_errors.append(dict(path=path,reason='actual candidate metadata is not an object'))
            return
        for key in ('actual_parameter_proposal','actual_parameters',
                    'unprojected_parameter_words','projected_parameter_words'):
            vector_if(item,key,10,path)
        for key in ('actual_unit_equations','complete_three_target_deviation'):
            vector_if(item,key,3,path)
        vector_if(item,'actual_full112_right',112,path)
        if item.get('full3_merit_returned') is True:
            reader.required(item,['actual_merit','actual_parameters','actual_unit_equations',
                'actual_full112_right','all_original_finite_primal_domain_guards_passed'],path)
        if item.get('accepted') is True:
            reader.required(item,['actual_merit','actual_parameters','actual_unit_equations',
                'actual_full112_right','all_original_finite_primal_domain_guards_passed'],path)
        if 'original_primal_returned' in item:
            observed['actual_primal_attempts']+=1
            observed['actual_primal_returns']+=item['original_primal_returned'] is True
            domain_counts[str(item.get('all_original_finite_primal_domain_guards_passed'))]+=1
        if 'normal_target_deviation_exception' in item:
            named_errors.append(dict(path=path+'.normal_target_deviation_exception',
                original=item['normal_target_deviation_exception']))
    for i,row in enumerate(steps):
        path='outer_steps['+str(i)+']'
        reader.required(row,['global_direction','block_index','direction','parameters_before',
            'original_full3_residual','original_full3_merit_before','direction_model',
            'trials','accepted','unvisited_real_trial_indices'],path)
        if (row.get('global_direction'),row.get('block_index'),row.get('direction'))!=(i,i//8,i%8):
            reader.metadata_errors.append(dict(path=path,reason='global/block/local direction order differs'))
        reader.vector(row.get('parameters_before'),10,path+'.parameters_before')
        reader.vector(row.get('original_full3_residual'),3,path+'.original_full3_residual')
        if 'current_complete_three_by_ten_J' in row:
            reader.matrix(row['current_complete_three_by_ten_J'],3,10,path+'.current_complete_three_by_ten_J')
        if 'actual_ten_direction' in row:
            reader.vector(row['actual_ten_direction'],10,path+'.actual_ten_direction')
            reader.vector(row.get('original_complete_three_directional_response'),3,
                path+'.original_complete_three_directional_response')
        direction_errors.extend(base.exceptions_in(row.get('direction_model',{}),path+'.direction_model'))
        trials=row.get('trials',[])
        if not isinstance(trials,list) or len(trials)>20:
            raise ValueError('The original twenty-alpha list is malformed')
        actual_accepted=[]
        for j,trial in enumerate(trials):
            tpath=path+'.trials['+str(j)+']'
            reader.required(trial,['trial','alpha','seed_parameters','original_Armijo_bound',
                'original_full3_slope','accepted'],tpath)
            if trial.get('trial')!=j:
                reader.metadata_errors.append(dict(path=tpath,reason='original alpha order differs'))
            reader.vector(trial.get('seed_parameters'),10,tpath+'.seed_parameters')
            candidate_fields(trial,tpath)
            if trial.get('accepted') is True:actual_accepted.append(j)
            trial_reasons[str(trial.get('reason'))]+=1
            trial_items.append((i,trial))
            trial_errors.extend(base.exceptions_in(trial,tpath))
            info=trial.get('complete_three_predictor_normal')
            if info is None:
                alpha_rows.append([i,j,trial.get('alpha'),trial.get('accepted'),
                    None,trial.get('actual_merit'),None,None,None,None,0,0,0,0,
                    trial.get('original_Armijo_bound') if trial.get('accepted') else None,None])
                alpha_presence.append(dict(direction=i,alpha_index=j,normal_started=False,
                    outer_present=sorted(trial),predictor_present=[],info_present=[]))
                inflight.append(dict(path=tpath,reason='Original alpha record exists; normal helper entry absent'))
                continue
            if not isinstance(info,dict):
                raise ValueError('The original nested normal metadata is malformed')
            observed['original_alpha_attempts']+=1
            for key in ('original_base_parameter_words',):
                vector_if(info,key,10,tpath+'.complete_three_predictor_normal')
            for key in ('original_base_three_residual','original_complete_three_linear_action',
                        'selected_actual_parameter_words'):
                if key=='selected_actual_parameter_words':
                    vector_if(info,key,10,tpath+'.complete_three_predictor_normal')
                else:vector_if(info,key,3,tpath+'.complete_three_predictor_normal')
            if info.get('affine_three_target') is not None:
                reader.vector(info['affine_three_target'],3,tpath+'.affine_three_target')
            predictor=info.get('predictor',{})
            candidate_fields(predictor,tpath+'.predictor')
            if predictor:
                all_normal_items.append((i,j,-1,-1,predictor))
            updates=info.get('normal_updates',[])
            if not isinstance(updates,list) or len(updates)>3:
                raise ValueError('The complete three-normal-update list is malformed')
            normal_trials=working=projected=0;chosen=None
            for ni,nrow in enumerate(updates):
                npath=tpath+'.normal_updates['+str(ni)+']'
                if nrow.get('index')!=ni:
                    reader.metadata_errors.append(dict(path=npath,reason='normal update order differs'))
                observed['started_normal_updates']+=1
                observed['fresh_complete_ten_normal_response_attempts']+=1
                for key in ('working_parameter_words','next_working_parameter_words'):
                    vector_if(nrow,key,10,npath)
                for key in ('actual_working_three_residual','affine_three_target',
                            'current_complete_three_target_deviation','next_complete_three_target_deviation',
                            'forward_primal_three_residual'):
                    vector_if(nrow,key,3,npath)
                if 'current_complete_three_by_ten_J' in nrow:
                    reader.matrix(nrow['current_complete_three_by_ten_J'],3,10,npath+'.current_J')
                    observed['fresh_complete_ten_normal_response_returns']+=1
                if nrow.get('direction_model'):normal_model_count+=1
                ntrials=nrow.get('trials',[])
                if not isinstance(ntrials,list) or len(ntrials)>20:
                    raise ValueError('The original twenty normal-step list is malformed')
                working+=nrow.get('working_point_updated') is True
                for nt,item in enumerate(ntrials):
                    ipath=npath+'.trials['+str(nt)+']'
                    if item.get('trial')!=nt:
                        reader.metadata_errors.append(dict(path=ipath,reason='normal trial order differs'))
                    candidate_fields(item,ipath)
                    normal_trial_reasons[str(item.get('reason'))]+=1
                    projected+=item.get('projection_active') is True
                    normal_trials+=1
                    all_normal_items.append((i,j,ni,nt,item))
                    if item.get('accepted') is True:chosen=(ni,nt,item)
                if nrow.get('unvisited_normal_trial_indices')!=list(range(len(ntrials),20)):
                    issue=dict(path=npath,reason='Normal trial suffix differs from current list',
                        actual=nrow.get('unvisited_normal_trial_indices'),started_count=len(ntrials))
                    (reader.metadata_errors if status.get('diagnostic_completed') else inflight).append(issue)
                if 'current_complete_three_by_ten_J' not in nrow:
                    normal_presence.append(dict(direction=i,alpha_index=j,normal_update=ni,
                        response_return_record_absent=True,original_stop_reason=nrow.get('stop_reason'),
                        available_fields=sorted(nrow)))
            if info.get('unvisited_normal_update_indices')!=list(range(len(updates),3)):
                issue=dict(path=tpath,reason='Normal update suffix differs from current list',
                    actual=info.get('unvisited_normal_update_indices'),started_count=len(updates))
                (reader.metadata_errors if status.get('diagnostic_completed') else inflight).append(issue)
            observed['normal_trial_records']+=normal_trials
            observed['temporary_normal_working_updates']+=working
            observed['projected_normal_proposals']+=projected
            kind=info.get('selected_actual_point_kind')
            corrected=isinstance(kind,str) and kind.startswith('full-three-normal-update-')
            observed['outer_candidates_selected_from_corrected_points']+=corrected
            original_stop=info.get('stop_reason')
            normal_stop_reasons[str(original_stop)]+=1
            if original_stop not in normal_stop_values:normal_stop_values.append(original_stop)
            original_stop_index=normal_stop_values.index(original_stop)
            alpha_rows.append([i,j,trial.get('alpha'),trial.get('accepted'),
                predictor.get('actual_merit'),trial.get('actual_merit'),
                info.get('new_primal_attempts'),info.get('new_primal_returns'),
                info.get('new_complete_ten_response_attempts'),info.get('new_complete_ten_response_returns'),
                len(updates),normal_trials,working,projected,
                trial.get('original_Armijo_bound') if trial.get('accepted') else None,
                original_stop_index])
            # Presence is semantic metadata: missing differs from an explicit null.
            alpha_presence.append(dict(direction=i,alpha_index=j,normal_started=True,
                outer_fields=[k for k in ('alpha','accepted','actual_merit','original_Armijo_bound') if k in trial],
                predictor_fields=[k for k in ('actual_merit','original_primal_returned',
                    'full3_merit_returned','accepted') if k in predictor],
                info_fields=[k for k in ('new_primal_attempts','new_primal_returns',
                    'new_complete_ten_response_attempts','new_complete_ten_response_returns',
                    'stop_reason') if k in info]))
            if trial.get('accepted') is True:
                selected=dict(direction=i,alpha_index=j,
                    original_owner_direction_accepted=row.get('accepted'),
                    original=base.pick(trial,['alpha','actual_parameters','actual_unit_equations',
                        'actual_merit','original_Armijo_bound','accepted_point_kind',
                        'actual_scalar_node_and_mid_minimum_radius','actual_circle_node_and_mid_minimum_beta2']),
                    affine_three_target=info.get('affine_three_target'),
                    complete_original_alpha_identity=identity(trial))
                if chosen is not None:
                    ni,nt,item=chosen
                    selected['normal']=dict(update=ni,trial=nt,
                        original=base.pick(item,['beta','complete_three_target_deviation',
                            'complete_three_target_deviation_merit','projection_active',
                            'unprojected_parameter_identity','unprojected_scaled_L2',
                            'radial_projection_factor','projected_parameter_identity',
                            'actual_projected_scaled_L2']),
                        actual_original_candidate_identity=identity(item))
                    if item.get('projection_active') is True:
                        selected['normal']['unprojected_parameter_words']=item.get('unprojected_parameter_words')
                        selected['normal']['projected_parameter_words']=item.get('projected_parameter_words')
                selected_points.append(selected)
        if row.get('unvisited_real_trial_indices')!=list(range(len(trials),20)):
            issue=dict(path=path,reason='Actual alpha suffix differs from current list',
                actual=row.get('unvisited_real_trial_indices'),started_count=len(trials))
            (reader.metadata_errors if status.get('diagnostic_completed') else inflight).append(issue)
        if row.get('accepted') is True:
            accepted_count+=1
            reader.vector(row.get('accepted_ten_parameter_words'),10,path+'.accepted_ten_parameter_words')
            if actual_accepted!=[len(trials)-1]:
                reader.metadata_errors.append(dict(path=path,reason='Accepted owner and selected actual alpha differ'))
        elif actual_accepted:
            issue=dict(path=path,reason='An actual candidate was selected but owner acceptance is absent',
                selected_alpha_indices=actual_accepted,
                source_owned_point_not_inferred_from_temporary_candidate=True)
            (reader.metadata_errors if status.get('diagnostic_completed') else inflight).append(issue)
        rows.append([i,True,row.get('accepted'),row.get('accepted_alpha'),
            row.get('original_full3_merit_before'),row.get('original_actual_merit_after'),
            row.get('original_full3_slope'),len(trials),row.get('unvisited_real_trial_indices'),
            row.get('stop_reason'),identity(row)['canonical_sha256']])
    for i in range(len(steps),128):
        rows.append([i,False,None,None,None,None,None,0,list(range(20)),
            status.get('stop_reason',status.get('phase')),None])
    # Do not repeat long, constant suffix names per alpha: preserve actual present
    # key sets once, then an ordinary small table of each alpha's key-set index.
    unique_presence=[];presence_indices=[]
    for row in alpha_presence:
        signature={key:value for key,value in row.items() if key not in ('direction','alpha_index')}
        if signature not in unique_presence:unique_presence.append(signature)
        presence_indices.append([row['direction'],row['alpha_index'],unique_presence.index(signature)])
    out['direction_columns']=columns
    out['all128_planned_direction_rows']=rows
    out['original_alpha_columns']=alpha_columns
    out['all_original_alpha_rows']=alpha_rows
    out['normal_stop_reason_values']=normal_stop_values
    out['alpha_original_key_sets']=unique_presence
    out['alpha_original_key_set_indices']=presence_indices
    out['all_original_direction_records_identity']=identity(steps)
    out['trial_conclusion']=dict(original_alpha_count=len(trial_items),
        actual_selected_candidate_count=sum(t.get('accepted') is True for _,t in trial_items),
        owner_accepted_direction_count=accepted_count,
        original_reason_counts=dict(sorted(trial_reasons.items())),
        original_primal_domain_flag_counts=dict(sorted(domain_counts.items())),
        original_complete_trial_lists_identity=identity([row.get('trials',[]) for row in steps]),
        extrema=selected_extrema(trial_items),
        all_original_trial_failures_and_exceptions=trial_errors,
        additional_named_normal_exceptions=named_errors,
        selected_original_points=selected_points,
        complete_trial_parameter_F_full112_vectors_read_in_Actions_but_not_all_transported=True)
    out['all_original_direction_failures_and_exceptions']=direction_errors
    original_counts=status.get('original_normal_evaluation_counts',{})
    count_differences={key:dict(recorded=original_counts.get(key),observed=value)
        for key,value in observed.items() if original_counts.get(key)!=value}
    if count_differences and status.get('diagnostic_completed'):
        reader.metadata_errors.append(dict(path='original_normal_evaluation_counts',
            reason='Completed metadata counters differ',differences=count_differences))
    out['normal_readback']=dict(
        observed_original_record_counts=observed,
        actual_counter_differences=count_differences,
        original_normal_stop_reason_counts=dict(sorted(normal_stop_reasons.items())),
        original_normal_trial_reason_counts=dict(sorted(normal_trial_reasons.items())),
        incomplete_current_records=inflight,
        normal_response_return_presence=normal_presence,
        complete_recorded_normal_direction_model_count=normal_model_count,
        all_actual_primal_merit_extrema=existing_candidate_extrema(all_normal_items),
        original_all_candidate_records_identity=identity([item for _,_,_,_,item in all_normal_items]),
        every_recorded_normal_primal_J_and_trial_read_in_Actions=True,
        full_normal_J_QR_response_and_nonselected_parameter_vectors_transported=False,
        all_normal_step_beta_values_and_projection_words_remain_in_identified_original_status=True,
        rejected_alpha_bounds_and_nonselected_step_vectors_not_all_transported=True,
        stop_text_indices_reference_only_original_finite_outcome_metadata_not_scientific_arrays=True,
        no_normal_linear_solve_derivative_check_or_merit_recalculation=True)
    blocks=status.get('continuation_blocks',[])
    if not isinstance(blocks,list) or len(blocks)>16:
        raise ValueError('The explicit sixteen-block metadata differs')
    block_columns=['index','started','phase','original_eight_search_completed','first_J_source',
        'accepted_point_count','attempted_outer_directions','original_trial_records',
        'stop_reason','continued','unvisited_local_direction_indices',
        'first_forward_equation_words_equal_owned_primal']
    out['block_columns']=block_columns
    out['original_block_rows']=[]
    for bi,block in enumerate(blocks):
        if block.get('index')!=bi or block.get('global_direction_offset')!=8*bi:
            reader.metadata_errors.append(dict(path='continuation_blocks['+str(bi)+']',
                reason='Original block/global offset differs'))
        out['original_block_rows'].append([block.get(key) for key in block_columns])
    for bi in range(len(blocks),16):
        out['original_block_rows'].append([bi,False,None,None,None,None,None,None,
            status.get('stop_reason',status.get('phase')),False,list(range(8)),None])
    block_key_sets=[];block_key_indices=[]
    for bi,block in enumerate(blocks):
        keys=sorted(block)
        if keys not in block_key_sets:block_key_sets.append(keys)
        block_key_indices.append([bi,block_key_sets.index(keys)])
    out['original_block_record_key_sets']=block_key_sets
    out['original_block_key_set_indices']=block_key_indices
    out['complete_original_block_metadata_identity']=identity(blocks)
    domain=status.get('complete_scalar_domain_at_binary64_projection')
    if domain is not None:
        out['complete_scalar_domain_at_binary64_projection']=dict(identity=identity(domain),
            original=base.pick(domain,['schema','covered_interval','bits','maximum_depth',
                'leaf_count','split_cells','unresolved_leaf_count',
                'complete_declared_real_expression_domain_certified','fresh_new_ten_control_identity',
                'old_scalar_domain_certificate_reused',
                'exact_prefix_scalar_and_complete_stored_finite_Gauss_expression',
                'exact_scalar_derivative_compatibility_or_C2_interface_certificate',
                'literal_binary64_evaluation_roundoff_enclosed',
                'returned_ap_identified_with_derivative_of_finite_Gauss_a','source_returned_ap_used',
                'source_circle_R_and_full_Frenet_domain_covered_by_this_scalar_bound']),
            actual_failures_and_exceptions=base.exceptions_in(domain,'complete_scalar_domain'))
    circle=status.get('original_complete_circle_check_at_binary64_projection')
    if circle is not None:
        dom=circle.get('actual_domain',{})
        square=circle.get('frozen_seven_added_shapes_square_check')
        out['original_complete_circle_check_at_binary64_projection']=dict(identity=identity(circle),
            original=base.pick(circle,['original_full_reference_finite','reference_is_not_a_nonzero_parent',
                'reference_sha256','scalar_family_sha256']),
            frozen_seven_added_shapes_square_check=dict(identity=identity(square),
                scalar_flags=base.scalar_fields(square),actual_failures_and_exceptions=base.exceptions_in(square)),
            actual_domain={**base.scalar_fields(dom),
                'original_RMS_query_checks':dom.get('original_RMS_query_checks'),
                'full_original_domain_identity':identity(dom)},
            actual_failures_and_exceptions=base.exceptions_in(circle,'original_complete_circle'),
            complete_original_FFT_checks_identity=identity(circle.get('original_full_FFT_tangent_checks')))
    for name in ('fresh_extended_scalar_family','original_projection_call_trace',
            'source_bound_family_views','source_bound_decimal_views'):
        if name in status:out[name+'_identity']=identity(status[name])
    if status.get('diagnostic_completed'):
        reader.required(status,['initial','final','initial_binary64_projection','final_binary64_projection',
            'complete_scalar_domain_at_binary64_projection','original_complete_circle_check_at_binary64_projection',
            'fixed_physical_scales','fixed_shape_definition','selected_shape',
            'outer_steps','complete_planned_outer_rows','complete_planned_block_rows','stop_reason'],
            'completed_status')
        if (reader.fd_levels,reader.fd_checks)!=(12,120):
            reader.metadata_errors.append(dict(path='completed_initial_final_FD',
                expected_levels=12,actual_levels=reader.fd_levels,
                expected_checks=120,actual_checks=reader.fd_checks))
    if status.get('accepted_point_count')!=accepted_count:
        reader.metadata_errors.append(dict(path='accepted_point_count',
            recorded=status.get('accepted_point_count'),actual_outer_flags=accepted_count))
    out['original_readback_coverage']=dict(
        planned_directions=128,started_directions=len(steps),planned_blocks=16,started_blocks=len(blocks),
        complete_original_trial_count=len(trial_items),
        original_FD_levels=reader.fd_levels,original_FD_column_checks=reader.fd_checks,
        original_FD_failures_and_exceptions_count=len(reader.fd_failures),
        original_FD_failures_and_exceptions_identity=identity(reader.fd_failures),
        original_FD_failures_returned_in_each_description=True,
        required_available_recorded_fields_complete=not reader.metadata_errors,
        metadata_errors=reader.metadata_errors,
        complete128_direction_rows_all_original_alpha_rows_and_unvisited_suffix_returned=True,
        all_actual_direction_and_trial_records_read_before_necessary_selection=True,
        original_d_J_actions_QR_and_per_trial_vector_values_not_transported=True,
        downstream_recipient_has_not_independently_read_all_large_arrays=True,
        extrema_are_only_selections_of_original_values_not_recomputed_scientific_quantities=True,
        no_accuracy_or_rank_certificate_from_FD_or_formed_slope=True)
    return out,not reader.metadata_errors



def compact_continuation_view(out):
    """Only select/share existing metadata; no norms or other scientific arithmetic."""
    # All actual direction records were read above. Each SHA remains covered
    # by the single full-list identity. No address or unvisited suffix disappears.
    old_columns=out['direction_columns']
    original_rows=out['all128_planned_direction_rows']
    stop_values=[]
    columns=['direction','started','accepted','accepted_alpha','merit_before',
        'merit_after','formed_full3_slope','alpha_trial_count',
        'unvisited_alpha_suffix','original_stop_reason_index']
    rows=[]
    for old in original_rows:
        values=dict(zip(old_columns,old))
        stop=values.get('original_stop_reason')
        if stop not in stop_values:stop_values.append(stop)
        suffix=values.get('unvisited_alpha_indices')
        count=values.get('alpha_trial_count')
        if isinstance(count,int) and suffix==list(range(count,20)):
            suffix=dict(first=count,stop_exclusive=20)
        rows.append([values.get(key) for key in columns[:8]]+
            [suffix,stop_values.index(stop)])
    before_aliases=[]
    for i,row in enumerate(rows):
        if (i and rows[i-1][2] is True and isinstance(row[4],str)
                and isinstance(rows[i-1][5],str) and row[4]==rows[i-1][5]):
            before_aliases.append([row[0],rows[i-1][0]])
            row[4]=None
    out['original_merit_before_aliases_to_previous_accepted_after']=before_aliases
    out['merit_before_alias_contract']=dict(
        columns=['direction','previous_accepted_direction'],
        only_exact_original_string_equality_and_previous_accepted_true=True,
        null_at_listed_alias_positions_is_a_reference_not_an_original_null=True,
        first_direction_and_every_unaliased_value_remain_original=True)
    out['direction_columns']=columns
    out['all128_planned_direction_rows']=rows
    out['original_direction_stop_values']=stop_values
    out['direction_record_identity_scope']='One complete original direction-list identity; individual large records are not all transported'

    # Accepted merit is already the original direction merit_after. Record the
    # original equality, retaining any actual mismatch explicitly rather than
    # silently substituting one original word for another.
    old_alpha_columns=out['original_alpha_columns']
    alpha_rows=out['all_original_alpha_rows'];reduced=[];aliases=[];mismatches=[]
    remove={'selected_merit','original_selected_Armijo_bound'}
    keep=[key for key in old_alpha_columns if key not in remove]
    bounds=[]
    direction_after={row[0]:row[5] for row in rows}
    for row in alpha_rows:
        values=dict(zip(old_alpha_columns,row))
        reduced.append([values.get(key) for key in keep])
        if values.get('outer_candidate_selected') is True:
            d=values['direction'];a=values['alpha_index']
            if values.get('selected_merit')==direction_after.get(d):
                aliases.append([d,a])
            else:
                mismatches.append(dict(direction=d,alpha_index=a,
                    original_selected_merit=values.get('selected_merit'),
                    original_direction_merit_after=direction_after.get(d)))
            bounds.append([d,a,values.get('original_selected_Armijo_bound')])
    out['original_alpha_columns']=keep
    out['all_original_alpha_rows']=reduced
    out['accepted_merit_aliases_to_original_direction_after']=aliases
    out['original_accepted_Armijo_bound_columns']=['direction','alpha_index','original_bound']
    out['original_accepted_Armijo_bounds']=bounds
    out['accepted_merit_alias_mismatches']=mismatches

    # Complete original selected records stay in the status identity. Return all
    # locations/kinds/projection flags, plus the first and last detailed record.
    # This is an explicit necessary view, never a raw-vector reconstruction.
    trial=out['trial_conclusion']
    selected=trial.pop('selected_original_points')
    rows=[];keysets=[];keyindices=[]
    columns=['direction','alpha_index','owner_direction_accepted','normal_update',
        'normal_trial','normal_beta','projection_active']
    for item in selected:
        normal=item.get('normal',{});original=normal.get('original',{})
        rows.append([item.get('direction'),item.get('alpha_index'),
            item.get('original_owner_direction_accepted'),normal.get('update'),
            normal.get('trial'),original.get('beta'),original.get('projection_active')])
        present=dict(item=sorted(item),normal=sorted(normal),normal_original=sorted(original))
        if present not in keysets:keysets.append(present)
        keyindices.append([item.get('direction'),item.get('alpha_index'),keysets.index(present)])
    trial['selected_candidate_columns']=columns
    trial['all_selected_candidate_rows']=rows
    trial['selected_candidate_original_key_sets']=keysets
    trial['selected_candidate_key_set_indices']=keyindices
    trial['complete_selected_candidate_records_identity']=identity(selected)
    trial['first_and_last_selected_original_points']=(
        [] if not selected else [selected[0]] if len(selected)==1 else [selected[0],selected[-1]])
    trial['intermediate_selected_parameter_vectors_and_deviations_not_all_transported']=True
    trial['all_selected_candidate_addresses_and_normal_choices_returned']=True

    # The all-true/all-false FD field group is shared only after exact value and
    # presence agreement. Any changed or absent original field remains verbatim.
    flags=dict(all_ten_columns_attempted=True,all_ten_columns_checked=True,
        all_ten_column_indices_checked_in_order=True,
        all_perturbed_parameter_and_equation_tables_transported=False)
    fd_paths=[]
    for name in ('initial','final','initial_binary64_projection','final_binary64_projection'):
        description=out.get(name,{})
        if not isinstance(description,dict):continue
        for i,level in enumerate(description.get('original_three_step_complete_ten_axis_FD',[])):
            if all(key in level and level[key] is value for key,value in flags.items()):
                fd_paths.append([name,i])
                for key in flags:del level[key]
    out['shared_original_FD_boolean_fields']=dict(
        exact_fields=flags,applies_only_at_original_paths=fd_paths,
        exact_value_and_key_presence_checked_before_sharing=True)
    out['compact_semantics']=dict(
        all_actual_direction_alpha_and_normal_records_read_before_selection=True,
        no_original_scientific_scalar_recomputed=True,
        no_trial_or_unpaid_direction_address_truncated=True,
        first_last_selected_detailed_points_only_other_vectors_Actions_only=True,
        original_missing_keys_preserved_by_presence_tables=True,
        one_single_90000_byte_report_no_parts=True,
        over_budget_is_transport_partial_not_scientific_failure=True)
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rules-directory',type=Path)
    p.add_argument('--compute-outcome',default='not-recorded')
    args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    path=args.directory/STATUS_NAME;complete=False
    try:
        if not path.is_file():
            out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,
                original_status_present=False,readout_source=file_identity(__file__),
                diagnostic_completed=False,complete_original_status_not_available=True,
                actual_compute_outcome=args.compute_outcome,scientific_failure_not_inferred=True)
        else:
            raw=path.read_bytes()
            out,complete=build(json.loads(raw),raw,args.directory,args.rules_directory,args.compute_outcome)
            out=compact_continuation_view(out)
    except Exception as error:
        out=dict(schema='request189-readback-exception-v1',exception=repr(error),
            traceback=traceback.format_exc(),readout_source=file_identity(__file__),
            original_status=file_identity(path) if path.is_file() else None,
            complete_original_readback_not_claimed=True,scientific_failure_not_inferred=True)
    raw=encoded(out);sections={name:len(encoded(value)) for name,value in out.items()}
    original_identity=dict(bytes=len(raw),sha256=digest(raw))
    print(encoded(dict(event='request189-necessary-section-byte-counts',total=len(raw),
        section_UTF8_bytes=sections,hard_bound=LIMIT,
        complete_original_status_not_recomputed=True)).decode(),flush=True)
    if len(raw)>LIMIT:
        out=dict(schema='request189-necessary-summary-over-budget-v1',
            original_summary_identity=original_identity,section_UTF8_byte_counts=sections,
            original_status=out.get('original_status'),phase=out.get('phase'),
            accepted_point_count=out.get('accepted_point_count'),stop_reason=out.get('stop_reason'),
            complete_original_readback_not_transported=True,
            scientific_failure_not_inferred_from_summary_size=True)
        raw=encoded(out);complete=False
    (args.out/'compact-summary.json').write_bytes(raw)
    receipt=dict(bytes=len(raw),sha256=digest(raw),metadata_complete=complete,
        complete_original_status_identity=out.get('original_status'),
        no_raw_array_reconstruction_protocol=True)
    (args.out/'compact-summary-receipt.json').write_bytes(encoded(receipt)+b'\n')
    print('BEGIN_VISIBLE189_COMPACT_SUMMARY',flush=True)
    print(raw.decode('ascii'),flush=True)
    print('END_VISIBLE189_COMPACT_SUMMARY',flush=True)
    print(encoded(dict(event='request189-necessary-summary-identity',**receipt,
        hash_scope='ASCII JSON bytes excluding log separator LF')).decode(),flush=True)
    return 0 if complete else 70


if __name__=='__main__':
    raise SystemExit(main())
