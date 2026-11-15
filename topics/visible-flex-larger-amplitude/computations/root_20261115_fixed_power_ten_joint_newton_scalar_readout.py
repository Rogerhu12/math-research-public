#!/usr/bin/env python3
"""Compact actual Request178 metadata; no numerical source is imported.

Read the complete temporary status, retain scientifically useful original
scalars and small matrices, and identify the larger original arrays/FD
perturbation tables by canonical bytes.  One summary only: no raw-array
encoding, dictionary packing, or structural splitting for transport.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import traceback

ENTRY='root_20261115_fixed_power_ten_joint_newton_scalar_readout.py'
PRODUCER='geometry_20261115_fixed_power_ten_joint_newton_recipe.py'
PRODUCER_SHA='3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e'
PRODUCER_SCHEMA='R259-fixed-power-ten-scaled-minimum-norm-Newton-full3-v1'
STATUS_NAME='fixed-power-ten-joint-newton-status.json'
SCHEMA='request178-fixed-power-complete-ten-Newton-essential-readback-v3'
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


def pick(value,keys):
    if not isinstance(value,dict):
        return {}
    return {key:value[key] for key in keys if key in value}


def scalar_fields(value):
    return {key:item for key,item in value.items()
            if item is None or isinstance(item,(str,bool,int,float))} if isinstance(value,dict) else {}


def exceptions_in(value,path='$'):
    found=[]
    if isinstance(value,dict):
        for key,item in value.items():
            here=path+'.'+key
            if ((key in ('exception','original_exception','traceback','complete_traceback')
                    and item is not None) or (key=='error' and isinstance(item,(str,dict)))):
                found.append(dict(path=here,original=item))
            elif key=='valid' and item is False:
                found.append(dict(path=here,original=False))
            elif isinstance(item,(dict,list)):
                found.extend(exceptions_in(item,here))
    elif isinstance(value,list):
        for i,item in enumerate(value):
            found.extend(exceptions_in(item,path+'['+str(i)+']'))
    return found


class Readback:
    def __init__(self):
        self.metadata_errors=[]
        self.fd_checks=0
        self.fd_levels=0
        self.fd_failures=[]

    def required(self,value,keys,path):
        if not isinstance(value,dict):
            self.metadata_errors.append(dict(path=path,reason='expected object'))
            return
        for key in keys:
            if key not in value:
                self.metadata_errors.append(dict(path=path+'.'+key,reason='required original field absent'))

    def matrix(self,value,rows,columns,path):
        good=isinstance(value,list) and len(value)==rows and all(isinstance(row,list) and len(row)==columns for row in value)
        if not good:
            self.metadata_errors.append(dict(path=path,reason='actual recorded matrix shape differs',
                expected=[rows,columns]))
        return value

    def vector(self,value,size,path):
        if not isinstance(value,list) or len(value)!=size:
            self.metadata_errors.append(dict(path=path,reason='actual recorded vector length differs',expected=size))
        return value

    def fd(self,levels,path):
        if levels is None:
            return dict(present=False)
        if not isinstance(levels,list) or len(levels)!=3:
            self.metadata_errors.append(dict(path=path,reason='expected all three original FD levels'))
            return dict(present=True,identity=identity(levels),metadata_incomplete=True)
        result=[]
        for i,level in enumerate(levels):
            self.required(level,['step','valid','maximum_relative_error','checks_by_parameter'],path+'['+str(i)+']')
            checks=level.get('checks_by_parameter',[])
            if not isinstance(checks,list):
                self.metadata_errors.append(dict(path=path,reason='FD checks are not a list'))
                checks=[]
            columns=[row.get('column') for row in checks]
            if columns!=list(range(10)):
                self.metadata_errors.append(dict(path=path,reason='all ten original FD columns not present in declared order',actual_columns=columns))
            failures=exceptions_in(checks,path+'['+str(i)+'].checks_by_parameter')
            self.fd_checks+=len(checks);self.fd_levels+=1
            self.fd_failures.extend(failures)
            result.append(dict(**pick(level,['step','valid','maximum_relative_error',
                'all_ten_columns_attempted','all_ten_columns_checked']),
                all_ten_column_indices_checked_in_order=columns==list(range(10)),
                complete_check_count=len(checks),
                complete_original_checks_identity=identity(checks),
                actual_failures_and_exceptions=failures,
                all_perturbed_parameter_and_equation_tables_transported=False))
        return result

    def description(self,value,path,binary64=False):
        if value is None:
            return dict(present=False)
        keys=['parameters','parameter_encoding','unweighted_full3_merit','low_equations_used',
            'unit_diagonal_defects','high_right_leak_max',
            'low_mode_trajectory_max_by_mode','scalar_node_and_mid_minimum_radius',
            'source_circle_node_and_mid_minimum_radius','source_circle_node_and_mid_minimum_beta2',
            'radius_cell_denominator_minimum_absolute','high_free_core_Schur_elimination_computed',
            'high_mode_nonresonance_proved','same_literal_coefficient_model_not_reformed_continuous_metric',
            'raw_original_table_accuracy_not_certified','derivative_accuracy_or_exact_rank_not_certified',
            'forward_primal_equation_words_equal_to_real_state','response_shape',
            'singular_values','first_three_column_singular_values','original_nine_column_singular_values',
            'numerical_parameter_condition','numerical_singular_values_are_not_a_transversality_proof',
            'actual_circle_R_minus_supplied_a_node_max','low_original_collocation_tangent_residual_max',
            'low_two_by_two_right_condition_max_by_mode','zero_tail_slope_J',
            'added_function_independence_does_not_assert_response_rank','new_g_family_not_a_relabelled_old_fixed_metric',
            'scalar_and_circle_queries_are_not_whole_interval_bounds']
        result=dict(present=True,**pick(value,keys))
        self.required(value,['parameters','low_equations_used','complete_first_order_right_residual'],path)
        self.vector(value.get('parameters'),10,path+'.parameters')
        self.vector(value.get('low_equations_used'),3,path+'.low_equations_used')
        full=value.get('complete_first_order_right_residual')
        self.vector(full,112,path+'.complete_first_order_right_residual')
        result['complete112_right_identity']=identity(full)
        if isinstance(full,list):
            result['first_three_actual_full112_right_rows']=full[:3]
        matrix_key='three_by_ten_parameter_jacobian' if binary64 else 'complete_three_by_ten_forward_response'
        self.required(value,[matrix_key],path)
        result[matrix_key]=self.matrix(value.get(matrix_key),3,10,path+'.'+matrix_key)
        fd_key='independent_real_parameter_difference_checks' if binary64 else 'independent_high_precision_real_parameter_difference_checks'
        self.required(value,[fd_key],path)
        result['original_three_step_complete_ten_axis_FD']=self.fd(value.get(fd_key),path+'.'+fd_key)
        response=value.get('forward_response_report')
        if response is not None:
            result['forward_response_report_identity']=identity(response)
            result['complete112_forward_identity']=pick(response,['complete112_response_canonical_sha256','forward_column_count'])
            if 'complete112_response' in response:
                self.matrix(response['complete112_response'],112,10,path+'.forward_response_report.complete112_response')
                result['complete112_forward_payload_identity']=identity(response['complete112_response'])
        result['full_original_description_identity']=identity(value)
        if 'terminal_Robin_terms' in value:
            result['terminal_Robin_terms_identity']=identity(value['terminal_Robin_terms'])
        return result

    def zero_extension(self,value,path):
        if not isinstance(value,dict):
            self.metadata_errors.append(dict(path=path,reason='expected original zero-extension object'))
            return dict(present=False,original_identity=identity(value))
        key='fields' if 'fields' in value else 'array_readback'
        flag='encoded_words_equal' if key=='fields' else 'byte_identical'
        rows=value.get(key,[])
        if not isinstance(rows,list):
            self.metadata_errors.append(dict(path=path+'.'+key,reason='expected original comparison rows'))
            rows=[]
        failed=[row for row in rows if not isinstance(row,dict) or row.get(flag) is not True]
        return dict(present=True,original_identity=identity(value),
            original_scalar_flags=scalar_fields(value),
            comparison_rows=len(rows),comparison_rows_identity=identity(rows),
            all_recorded_rows_true=all(isinstance(row,dict) and row.get(flag) is True for row in rows),
            actual_nontrue_or_malformed_comparison_rows=failed,
            matching_array_descriptors_and_repeated_parameter_words_transported=False)


    def outer_steps(self,steps):
        if not isinstance(steps,list):
            self.metadata_errors.append(dict(path='outer_steps',reason='expected original outer list'))
            steps=[]
        if len(steps)>8:
            self.metadata_errors.append(dict(path='outer_steps',reason='more than original eight directions'))
        output=[];trial_rows=[];trial_errors=[];last_model=None
        columns=['direction','trial','alpha','accepted','actual_merit','actual_unit_equations',
                 'original_Armijo_bound','all_original_finite_primal_domain_guards_passed','reason']
        for i,row in enumerate(steps):
            path='outer_steps['+str(i)+']'
            self.required(row,['direction','parameters_before','original_full3_residual',
                'original_full3_merit_before','direction_model','trials','accepted',
                'unvisited_real_trial_indices'],path)
            if row.get('direction')!=i:
                self.metadata_errors.append(dict(path=path,reason='original direction order differs'))
            self.vector(row.get('parameters_before'),10,path+'.parameters_before')
            self.vector(row.get('original_full3_residual'),3,path+'.original_full3_residual')
            if 'accepted_ten_parameter_words' in row:
                self.vector(row['accepted_ten_parameter_words'],10,path+'.accepted_ten_parameter_words')
            J=row.get('current_complete_three_by_ten_J')
            if J is not None:
                self.matrix(J,3,10,path+'.current_complete_three_by_ten_J')
            dm=row.get('direction_model',{})
            nr=dm.get('newton') or {};fb=dm.get('fallback')
            selected=dm.get('selected_proposal')
            summary=dict(**pick(row,['direction','original_full3_residual','original_full3_merit_before',
                'accepted','accepted_alpha','original_actual_merit_after','accepted_ten_parameter_words',
                'stop_reason','unvisited_real_trial_indices','current_forward_equation_words_equal_owned_primal',
                'initial_complete_ten_J_from_initial_description']),
                parameters_before_identity=identity(row.get('parameters_before')),
                current_complete_three_by_ten_J_identity=identity(J),
                full_original_outer_identity=identity(row),
                direction_model_identity=identity(dm),selected_kind=dm.get('selected_kind'),
                actual_direction=pick(row,['actual_ten_direction',
                    'original_complete_three_directional_response','original_full3_slope']),
                newton=pick(nr,['selected','exception','traceback','rejection_reason',
                    'equation_column_permutation','complete_upper_diagonal',
                    'original_unclipped_scaled_norm','radial_clip_factor',
                    'original_transpose_triangular_residual','original_complete_linear_residual',
                    'clipped_complete_linear_residual','scaled_step_L2',
                    'original_model_full_step_merit','finite_complete_direction_and_action']),
                fallback=pick(fb,['selected','exception','traceback','stop_reason',
                    'scaled_gradient_L2','exact_line_model_numerator','exact_line_model_denominator',
                    'boundary_length','selected_line_length','scaled_step_L2',
                    'original_model_full_step_merit','zero_denominator_fallback_is_a_finite_proposal_not_an_exact_rank_claim']),
                actual_failures_and_exceptions=exceptions_in(dm,path+'.direction_model'))
            summary['newton']['complete_Q_identity']=identity(nr['complete_Q']) if 'complete_Q' in nr else None
            summary['newton']['complete_R_identity']=identity(nr['complete_R']) if 'complete_R' in nr else None
            response=row.get('current_response_report')
            if isinstance(response,dict):
                summary['current_complete112_forward_report_identity']=identity(response)
                summary['current_complete112_forward_record']=pick(response,[
                    'complete112_response_canonical_sha256','forward_column_count'])
                if 'complete112_response' in response:
                    self.matrix(response['complete112_response'],112,10,path+'.current_response_report.complete112_response')
            if selected is not None:
                self.required(selected,['kind','complete_scaled_coordinates',
                    'complete_physical_direction','original_complete_three_directional_response',
                    'original_full3_slope','finite_complete_direction_and_action'],path+'.direction_model.selected_proposal')
                for key in ('complete_scaled_coordinates','complete_physical_direction'):
                    self.vector(selected.get(key),10,path+'.selected_proposal.'+key)
                self.vector(selected.get('original_complete_three_directional_response'),3,path+'.selected_proposal.response')
                self.vector(row.get('actual_ten_direction'),10,path+'.actual_ten_direction')
                self.vector(row.get('original_complete_three_directional_response'),3,path+'.actual_response')
                if selected.get('kind')=='radially-clipped-complete-minimum-norm-Newton':
                    self.required(nr,['complete_Q','complete_R','equation_column_permutation',
                        'permuted_original_rhs','triangular_solution',
                        'original_transpose_triangular_residual','original_complete_linear_residual',
                        'radial_clip_factor','clipped_complete_linear_residual'],path+'.newton')
                    for key in ('permuted_original_rhs','triangular_solution',
                                'original_transpose_triangular_residual','original_complete_linear_residual',
                                'clipped_complete_linear_residual'):
                        self.vector(nr.get(key),3,path+'.newton.'+key)
                elif selected.get('kind')=='complete-scaled-Cauchy-fallback':
                    self.required(fb,['complete_scaled_merit_gradient','complete_scaled_gradient_action',
                        'exact_line_model_numerator','exact_line_model_denominator','selected_line_length'],path+'.fallback')
                    self.vector(fb.get('complete_scaled_merit_gradient'),10,path+'.fallback.gradient')
                    self.vector(fb.get('complete_scaled_gradient_action'),3,path+'.fallback.action')
                else:
                    self.metadata_errors.append(dict(path=path+'.selected_proposal.kind',reason='unknown original selected direction'))
            if 'complete_Q' in nr:
                self.matrix(nr['complete_Q'],10,10,path+'.newton.complete_Q')
                self.matrix(nr.get('complete_R'),10,3,path+'.newton.complete_R')
            if dm:
                last_model=dict(direction=row.get('direction'),
                    original_complete_model_identity=identity(dm),
                    current_complete_three_residual=dm.get('current_complete_three_residual'),
                    current_complete_three_by_ten_J=J,
                    complete_scaled_matrix=dm.get('complete_scaled_matrix'),
                    fixed_physical_scales=dm.get('fixed_physical_scales'),
                    selected_kind=dm.get('selected_kind'),
                    newton={**summary['newton'],
                        **pick(nr,['factorization_convention','Q_orientation','permuted_original_rhs',
                            'triangular_solution','original_unclipped_scaled_direction',
                            'complete_scaled_coordinates','complete_physical_direction',
                            'original_complete_three_directional_response','original_full3_slope',
                            'original_model_full_step_residual']),
                        'complete_Q_identity':identity(nr.get('complete_Q')),
                        'complete_R_identity':identity(nr.get('complete_R')),
                        'formed_Q_first_three_columns':[x[:3] for x in nr['complete_Q']] if isinstance(nr.get('complete_Q'),list) else None,
                        'formed_R_first_three_rows':nr['complete_R'][:3] if isinstance(nr.get('complete_R'),list) else None,
                        'unused_seven_Q_columns_identified_not_transported':True},
                    fallback=None if fb is None else {**fb},
                    full_original_errors=exceptions_in(dm,path+'.direction_model'))
            trials=row.get('trials',[])
            if not isinstance(trials,list) or len(trials)>20:
                self.metadata_errors.append(dict(path=path+'.trials',reason='original trial list/20 budget differs'))
                trials=[] if not isinstance(trials,list) else trials
            for j,t in enumerate(trials):
                tp=path+'.trials['+str(j)+']'
                self.required(t,['trial','alpha','seed_parameters','original_Armijo_bound',
                    'original_full3_slope','accepted'],tp)
                if t.get('trial')!=j:
                    self.metadata_errors.append(dict(path=tp,reason='original trial order differs'))
                self.vector(t.get('seed_parameters'),10,tp+'.seed_parameters')
                if 'actual_parameters' in t:
                    self.vector(t['actual_parameters'],10,tp+'.actual_parameters')
                if 'actual_unit_equations' in t:
                    self.vector(t['actual_unit_equations'],3,tp+'.actual_unit_equations')
                if 'actual_full112_right' in t:
                    self.vector(t['actual_full112_right'],112,tp+'.actual_full112_right')
                if t.get('accepted'):
                    self.required(t,['actual_parameters','actual_unit_equations','actual_merit',
                        'actual_full112_right','all_original_finite_primal_domain_guards_passed','reason'],tp)
                trial_rows.append([row.get('direction')]+[t.get(key) for key in columns[1:]])
                for failure in exceptions_in(t,tp):
                    trial_errors.append(failure)
            summary['complete_original_trials_identity']=identity(trials)
            summary['original_real_trial_count']=len(trials)
            summary['planned_real_trial_count']=20
            summary['all_visited_trial_domain_minima_identity']=identity([
                pick(t,['trial','actual_scalar_node_and_mid_minimum_radius',
                    'actual_circle_node_and_mid_minimum_beta2']) for t in trials])
            output.append(summary)
        return dict(original_outer_steps=output,original_real_trial_columns=columns,
            all_original_real_trial_rows=trial_rows,
            all_original_real_trial_failures_and_exceptions=trial_errors,
            last_original_direction_model=last_model,
            complete_original_outer_steps_identity=identity(steps),
            full_original_seed_parameter_domain_minimum_and112_tables_identified_not_transported=True)

def compact_rules(directory):
    rows=[]
    if directory is not None and directory.is_dir():
        paths=sorted(directory.glob('sync-*-completed.json'))
        if (directory/'runner-result.json').is_file():
            paths.append(directory/'runner-result.json')
        for path in paths:
            value=json.loads(path.read_bytes())
            rows.append(dict(identity=file_identity(path),
                original=pick(value,['phase','status','returncode','return_code','exit_code',
                    'rules_changed','exception','traceback','source_commit','current_head','head',
                    'started','completed','elapsed_seconds','changed_paths','readme_blobs',
                    'latest_readme_blobs','period_seconds']),
                full_original_metadata_identity=identity(value)))
    return rows


def reference_actual_repeated_words(out,status):
    """Reference only canonical-byte-identical values already kept in this summary."""
    used=[]
    coverage=out.get('original_readback_coverage',{})
    complete_fd_coverage=(coverage.get('fd_original_column_checks')==120
                          and coverage.get('fd_original_levels')==12)
    out['actual_repeated_word_references']=dict(
        locations=used,
        complete_original_status_and_all_available_FD_checks_processed_first=True,
        all120_original_FD_checks_and12_levels_present=complete_fd_coverage,
        differing_or_exception_bearing_values_retained_in_full=True,
        no_scientific_value_or_gate_changed=True)
    if not complete_fd_coverage:
        return
    initial=status.get('initial')
    full=initial.get('complete_three_by_ten_forward_response') if isinstance(initial,dict) else None
    if (isinstance(full,list) and len(full)==3 and
            all(isinstance(row,list) and len(row)==10 for row in full)):
        left_nine=[row[:9] for row in full]
        locations=[(out.get('fresh_original_nine'),
                    'complete_three_by_nine_forward',
                    '#/fresh_original_nine/complete_three_by_nine_forward')]
        for container,key,location in locations:
            if not isinstance(container,dict) or key not in container:
                continue
            actual=container[key]
            if encoded(actual)==encoded(left_nine):
                container[key]=dict(
                    schema='same-summary-byte-identical-reference-v1',
                    reference='#/initial/complete_three_by_ten_forward_response',
                    selection=dict(rows='all',column_start=0,column_stop_exclusive=9),
                    original_value_identity=identity(actual),
                    canonical_bytes_compared_equal=True)
                used.append(location)
    for final_name,initial_name in (('final','initial'),
                                    ('final_binary64_projection','initial_binary64_projection')):
        actual=status.get(final_name);reference=status.get(initial_name)
        # Complete originals, all FD columns and all exceptions were read first.
        # Keep any exception-bearing description fully expanded even if repeated.
        if (isinstance(actual,dict) and isinstance(reference,dict)
                and not exceptions_in(actual)
                and encoded(actual)==encoded(reference)):
            compact=out[final_name]
            out[final_name]=dict(present=True,
                schema='same-summary-byte-identical-reference-v1',
                reference='#/'+initial_name,
                complete_original_description_identity=identity(actual),
                compact_description_identity=identity(compact),
                canonical_complete_original_bytes_compared_equal=True,
                all_original_FD_columns_and_exceptions_counted_before_reference=True)
            used.append('#/'+final_name)



def essential_r2_selection(out,status):
    """A semantic small conclusion, not compression of the omitted raw model."""
    steps=out.pop('original_outer_steps',[])
    columns=['direction','residual_before','merit_before','accepted','accepted_alpha',
        'merit_after','accepted_ten_parameter_words','stop_reason','unvisited_real_trial_indices',
        'selected_kind','actual_ten_direction','actual_three_action','actual_full3_slope',
        'real_trial_count','full_outer_identity','newton_selected','newton_clip_factor',
        'newton_unclipped_scaled_norm','newton_rejection_reason','fallback_selected','fallback_selected_length',
        'fallback_stop_reason','current_forward_primal_words_equal_owner',
        'complete_original_direction_failures_and_exceptions']
    rows=[]
    for row in steps:
        action=row.get('actual_direction',{});nr=row.get('newton') or {};fb=row.get('fallback') or {}
        rows.append([row.get('direction'),row.get('original_full3_residual'),
            row.get('original_full3_merit_before'),row.get('accepted'),row.get('accepted_alpha'),
            row.get('original_actual_merit_after'),row.get('accepted_ten_parameter_words'),
            row.get('stop_reason'),row.get('unvisited_real_trial_indices'),row.get('selected_kind'),
            action.get('actual_ten_direction'),action.get('original_complete_three_directional_response'),
            action.get('original_full3_slope'),row.get('original_real_trial_count'),
            row.get('full_original_outer_identity'),nr.get('selected'),
            nr.get('radial_clip_factor'),nr.get('original_unclipped_scaled_norm'),nr.get('rejection_reason'),
            fb.get('selected'),fb.get('selected_line_length'),fb.get('stop_reason'),
            row.get('current_forward_equation_words_equal_owned_primal'),row.get('actual_failures_and_exceptions')])
    out['original_outer_columns']=columns
    out['all_original_outer_rows']=rows
    model=out.get('last_original_direction_model')
    if isinstance(model,dict):
        # Complete originals were already shape-checked by outer_steps().
        for name in ('complete_scaled_matrix',):
            if name in model:model[name]=dict(original_identity=identity(model[name]),
                scope='Actual scaled matrix omitted; full last J and fixed S retained, no arithmetic reconstruction by reader')
        nr=model.get('newton')
        if isinstance(nr,dict):
            for name in ('original_unclipped_scaled_direction','complete_scaled_coordinates'):
                if name in nr:nr[name]=dict(original_identity=identity(nr[name]),
                    scope='Earlier/unused scaled-coordinate word vector identified, not transmitted')
            # Only literal equality permits a reference, never an inferred product.
            if rows:
                reference=rows[-1]
                for name,column in (('complete_physical_direction','actual_ten_direction'),
                    ('original_complete_three_directional_response','actual_three_action'),
                    ('original_full3_slope','actual_full3_slope')):
                    if name in nr and encoded(nr[name])==encoded(reference[columns.index(column)]):
                        nr[name]=dict(reference='#/all_original_outer_rows/'+str(len(rows)-1),
                            column=column,original_identity=identity(nr[name]),canonical_bytes_equal=True)
    for name in ('fixed_shape_definition','fixed_shape_evidence','policy'):
        if name in out:
            out[name]=dict(original_identity=identity(out[name]),
                scope='Source-bound contract; actual selected shape and all scientific conclusions retained separately')
    fresh=out.get('fresh_original_nine')
    if isinstance(fresh,dict):
        name='complete_three_by_nine_forward'
        if name in fresh and not isinstance(fresh[name],dict):
            fresh[name]=dict(original_identity=identity(fresh[name]),
                scope='Fresh old-nine response identified; full new-ten initial response and all zero-extension differences retained')
    for name in ('initial_projection_contract','final_projection_contract'):
        if name in out:
            actual=out[name]
            out[name]=dict(original_identity=identity(actual),original_scalar_fields=scalar_fields(actual),
                actual_failures_and_exceptions=exceptions_in(actual),
                scope='Original projected parameters/residuals and all projected FD retained in their descriptions')
    # The projected J is diagnostic data, distinct from the owned Decimal J.
    # Preserve its identity while returning all original projected FD maxima.
    for name in ('initial_binary64_projection','final_binary64_projection'):
        value=out.get(name)
        if isinstance(value,dict) and 'three_by_ten_parameter_jacobian' in value:
            matrix=value['three_by_ten_parameter_jacobian']
            value['three_by_ten_parameter_jacobian']=dict(original_identity=identity(matrix),
                original_shape=[3,10],scope='Fully read/shape-checked in Actions; projected matrix words not transported')
    coverage=out['original_readback_coverage']
    coverage['r2_prior_seven_QR_internal_residual_and_factor_words_only_identified']=True
    coverage['r2_prior_current_J_and_factor_identity_scope']='Complete original outer-record canonical identity; constituent J/QR tables not separately transported'
    coverage['r2_all_eight_actual_d_Jd_slope_accepted_words_failures_and_unvisited_returned']=True
    coverage['r2_last_complete_J_Q3_R3_and_original_triangular_linear_residuals_returned']=True
    coverage['r2_all_available_120_FD_checks_read_before_any_selection']=True
    coverage['r2_omitted_new_payload_categories']=[
        'per-direction redundant Newton factor/residual diagnostics except final actual model',
        'repeated top-level fixed-shape/old-policy descriptions',
        'old-nine fresh J matrix and projected binary64 J words',
        'last scaled-matrix and redundant scaled-coordinate vectors']
    out['readback_revision']=2
    return out


def essential_r3_selection(out,status):
    """Select the actual restart and trial evidence; identify QR basis payloads."""
    model=out.get('last_original_direction_model')
    if isinstance(model,dict):
        compact=pick(model,['direction','original_complete_model_identity',
            'current_complete_three_residual','fixed_physical_scales','selected_kind',
            'full_original_errors'])
        compact['last_current_J_identity']=identity(model.get('current_complete_three_by_ten_J'))
        nr=model.get('newton')
        if isinstance(nr,dict):
            compact['newton']=pick(nr,['selected','exception','traceback','rejection_reason',
                'equation_column_permutation','complete_upper_diagonal',
                'original_unclipped_scaled_norm','radial_clip_factor',
                'original_transpose_triangular_residual','original_complete_linear_residual',
                'clipped_complete_linear_residual','scaled_step_L2',
                'original_model_full_step_merit','finite_complete_direction_and_action'])
        fb=model.get('fallback')
        compact['fallback']=None if fb is None else dict(
            original_identity=identity(fb),actual_scalar_fields=scalar_fields(fb),
            all_actual_failures_and_exceptions=exceptions_in(fb))
        compact['whole_original_model_contains_all_Q_R_words_not_returned_here']=True
        out['last_original_direction_model']=compact
    initial=out.get('initial')
    if isinstance(initial,dict) and 'complete_three_by_ten_forward_response' in initial:
        original=initial['complete_three_by_ten_forward_response']
        initial['complete_three_by_ten_forward_response']=dict(original_identity=identity(original),
            original_shape=[3,10],scope='Fully read and shape-checked; initial matrix words identified only; complete final Decimal J is returned')
    keep=['present','parameters','parameter_encoding','unweighted_full3_merit',
        'low_equations_used','unit_diagonal_defects','complete112_right_identity',
        'first_three_actual_full112_right_rows','original_three_step_complete_ten_axis_FD',
        'full_original_description_identity','forward_response_report_identity',
        'complete112_forward_identity','complete112_forward_payload_identity',
        'numerical_parameter_condition','singular_values',
        'three_by_ten_parameter_jacobian','schema','reference',
        'complete_original_description_identity','compact_description_identity',
        'canonical_complete_original_bytes_compared_equal',
        'all_original_FD_columns_and_exceptions_counted_before_reference']
    for name in ('initial_binary64_projection','final_binary64_projection'):
        value=out.get(name)
        if not isinstance(value,dict):continue
        compact=pick(value,keep)
        compact.update({key:val for key,val in value.items() if isinstance(val,bool)})
        compact['all_actual_description_failures_and_exceptions']=exceptions_in(status.get(name))
        compact['other_projection_diagnostics_scope']='Original full description identity only; all p/F, FD comparisons, numerical condition and boolean responsibility flags above are retained'
        out[name]=compact
    # Repeat only values which are necessary; an actual equality reference is
    # used only when its JSON text is smaller than the original repeated value.
    final=out.get('final')
    final_words=final.get('parameters') if isinstance(final,dict) else None
    if isinstance(final_words,list):
        for name in ('current_accepted_ten_parameter_words','final_ten_parameter_words'):
            value=out.get(name)
            ref=dict(reference='#/final/parameters',canonical_bytes_equal=True)
            if encoded(value)==encoded(final_words) and len(encoded(ref))<len(encoded(value)):
                out[name]=ref
        columns=out.get('original_outer_columns',[]);rows=out.get('all_original_outer_rows',[])
        if rows and 'accepted_ten_parameter_words' in columns:
            j=columns.index('accepted_ten_parameter_words');value=rows[-1][j]
            ref=dict(reference='#/final/parameters',canonical_bytes_equal=True)
            if encoded(value)==encoded(final_words) and len(encoded(ref))<len(encoded(value)):
                rows[-1][j]=ref
    cov=out['original_readback_coverage']
    cov['r2_last_complete_J_Q3_R3_and_original_triangular_linear_residuals_returned']=False
    cov['r3_complete_final_Decimal_J_returned_initial_and_last_direction_J_identified_only']=True
    cov['r3_Q_R_basis_triangular_solution_and_scaled_vectors_identified_not_transported']=True
    cov['r3_all_eight_d_Jd_slope_accept_words_all_trials_120FD_and_final_gates_preserved']=True
    cov['r3_initial_final_p_F_merit_and_all_original_final_flags_preserved']=True
    out['readback_revision']=3
    out['optional_diagnostic_budget']=dict(target_bytes_before_wrapper=80000,
        original_QR_and_J_payload_omissions=[],
        required_p_F_merit_all_d_actions_trials_FD_final_flags_never_removed=True,
        hard_summary_bound_unchanged=LIMIT)
    if len(encoded(out))>80000:
        # This is an explicit smaller conclusion scope, not raw-data encoding.
        # Every omitted component has already been read and shape checked.
        model=out.get('last_original_direction_model')
        if isinstance(model,dict):
            out['last_original_direction_model']=dict(
                direction=model.get('direction'),
                original_complete_model_identity=model.get('original_complete_model_identity'),
                selected_kind=model.get('selected_kind'),
                full_original_errors=model.get('full_original_errors'),
                only_full8_actual_d_Jd_slope_and_acceptance_rows_returned=True,
                optional_QR_interior_words_not_transported=True)
            out['optional_diagnostic_budget']['original_QR_and_J_payload_omissions'].append(
                'last original QR internal diagonal/triangular/linear residual diagnostic values')
        final=out.get('final')
        if isinstance(final,dict):
            name='complete_three_by_ten_forward_response'
            value=final.get(name)
            if isinstance(value,list):
                final[name]=dict(original_identity=identity(value),original_shape=[3,10],
                    scope='Original final matrix read and shape checked; omitted from small conclusion; p/F/merit/all FD/final flags retained')
                cov['r3_complete_final_Decimal_J_returned_initial_and_last_direction_J_identified_only']=False
                out['optional_diagnostic_budget']['original_QR_and_J_payload_omissions'].append(
                    'final complete3x10 J matrix words, original identity retained')
    return out

def build(status,raw,directory,rules,compute_outcome):
    reader=Readback()
    if status.get('schema')!=PRODUCER_SCHEMA or status.get('source_sha256')!=PRODUCER_SHA:
        raise ValueError('Bind the independent actual178 full-ten producer')
    sources=status.get('consumed_source_sha256',{})
    if len(sources)!=45 or sources.get(PRODUCER)!=PRODUCER_SHA:
        raise ValueError('The full current45 producer source closure differs')
    fields=['phase','run_id','source_commit','actual_origin','parameter_recipe','policy',
        'input_sha256','original_nine_parameter_words','original_parent_radius',
        'parent_radius_not_used_as_new_shape_scale','decimal_digits','rounding',
        'original_mesh_nodes','field_and_tail_modes','selected_catalogue_index',
        'fixed_shape_evidence','fixed_shape_definition','catalogue_reselection_performed',
        'all_ten_parameters_can_change','fixed_physical_scales',
        'fixed_scales_computed_once_from_actual157_words','scaled_trust_radius',
        'shape_frozen_for_all_ten_forward_FD_trials_and_final_consumers',
        'unvisited_outer_indices','accepted_point_count','attempted_outer_directions',
        'original_trial_records','current_accepted_ten_parameter_words',
        'old_nine_parameters_relabelled_as_new','new_shape_parameter_index',
        'input_tables_not_reformed_in_high_precision','source_bound_original112_terminal_and699_chain_retained',
        'full_ten_QR_or_Cauchy_is_a_proposal_not_an_accuracy_or_rank_gate',
        'high_mode_Schur_elimination_or_current_nonlinear_native_performed',
        'native_nonlinear_solver_called','nonzero_field_completed','success','diagnostic_completed',
        'resource_partial','stop_reason','exception','traceback','scientific_failure_not_inferred',
        'actual_initial_merit','original_Armijo_coefficient_exact_binary64_lift',
        'final_ten_parameter_words','final_selected_shape_coefficient','final_original_three_merit',
        'high_precision_original_unit_stopping_tolerance_met',
        'high_precision_full112_linear_right_tolerance_met',
        'binary64_projection_original_unit_stopping_tolerance_met',
        'binary64_projection_full112_linear_right_tolerance_met',
        'initial_final_complete_ten_axis_three_step_Decimal_and_binary64_FD_attempted',
        'final_continuous_scalar_and453_circle_consumers_at_explicit_projection_only',
        'high_precision_complete_interval_domain_or_exact_derivative_accuracy_certified',
        'independent_ten_model_call_counts','fresh_original_nine_model_call_counts',
        'complete_original_event_ledger','elapsed_wall_seconds']
    out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,
        original_status=dict(bytes=len(raw),sha256=digest(raw),file=STATUS_NAME),
        readout_source=file_identity(__file__),producer_sha256=PRODUCER_SHA,
        **pick(status,fields),actual_compute_outcome=compute_outcome,
        complete_current_source_closure_count=len(sources),
        complete_current_source_closure_identity=identity(sources),
        actual_rule_sync=compact_rules(rules),
        readout_is_original_JSON_and_byte_operations_only=True,
        matrix_norm_FD_or_scientific_evaluation_recomputed_by_reader=False,
        raw_array_payloads_or_complete_FD_perturbation_tables_transported=False,
        one_compact_conclusion_not_a_raw_data_reconstruction=True,
        raw_Git_Release_or_artifact_retention=False,
        numerical_acceptance_not_changed_by_readback_checks=True)
    for name in ('original_nine_literal_binding','new_ten_literal_binding'):
        value=status.get(name)
        if value is not None:
            out[name]=dict(identity=identity(value),
                original=pick(value,['schema','source','base_primal_source_sha256','canonical_binding_sha256',
                    'parameter_dimension','parameter_order','old_parameter_columns','new_shape_column',
                    'decimal_digits','rounding','original_mesh_nodes','field_and_tail_modes',
                    'complete_original_tail_J_consumed',
                    'new_control_table_words_are_binary64_source_samples_then_exact_lifts',
                    'new_shape_table_formation_recomputed_in_Decimal',
                    'no_discrete_rounding_derivative_or_interval_accuracy_certificate',
                    'frozen_original_native_anchor_J_is_not_a_new_g_nonlinear_tail_response']))
    fresh=status.get('fresh_original_nine')
    if fresh is not None:
        out['fresh_original_nine']=pick(fresh,['parameters','equation','merit',
            'complete_three_by_nine_forward','original_primal_and_forward_equation_words_equal'])
        out['fresh_original_nine']['complete112_right_identity']=identity(fresh.get('full112_right'))
    for name in ('zero_extension_literal_readback','zero_extension_binary64_readback'):
        if name in status:
            out[name]=reader.zero_extension(status[name],name)
    for name in ('initial_projection_contract','final_projection_contract'):
        if name in status:
            out[name]=status[name]
    if 'selected_shape' in status:
        shape=status['selected_shape']
        out['selected_shape']=dict(identity=identity(shape),
            original=pick(shape,['schema','parameter_order','selected_shape','extra_shape',
                'parameter_count','parameter_dimension','new_shape_parameter_index',
                'selected_catalogue_index','catalogue_index','base_family_source_sha256','source']))
    out['initial']=reader.description(status.get('initial'),'initial')
    out['final']=reader.description(status.get('final'),'final')
    out['initial_binary64_projection']=reader.description(status.get('initial_binary64_projection'),'initial_binary64_projection',True)
    out['final_binary64_projection']=reader.description(status.get('final_binary64_projection'),'final_binary64_projection',True)
    actual_steps=status.get('outer_steps',[])
    out.update(reader.outer_steps(actual_steps))
    out['complete_planned_outer_rows']=[
        dict(index=i,started=i<len(actual_steps),
             original_stop_reason=actual_steps[i].get('stop_reason') if i<len(actual_steps) else status.get('stop_reason',status.get('phase')),
             original_unvisited_real_trial_indices=actual_steps[i].get('unvisited_real_trial_indices') if i<len(actual_steps) else list(range(20)))
        for i in range(8)]
    domain=status.get('complete_scalar_domain_at_binary64_projection')
    if domain is not None:
        out['complete_scalar_domain_at_binary64_projection']=dict(identity=identity(domain),
            original=pick(domain,['schema','covered_interval','bits','maximum_depth','leaf_count','split_cells',
                'unresolved_leaf_count','complete_declared_real_expression_domain_certified',
                'fresh_new_ten_control_identity','old_scalar_domain_certificate_reused',
                'exact_prefix_scalar_and_complete_stored_finite_Gauss_expression',
                'exact_scalar_derivative_compatibility_or_C2_interface_certificate',
                'literal_binary64_evaluation_roundoff_enclosed',
                'returned_ap_identified_with_derivative_of_finite_Gauss_a','source_returned_ap_used',
                'source_circle_R_and_full_Frenet_domain_covered_by_this_scalar_bound']),
            actual_failures_and_exceptions=exceptions_in(domain))
    circle=status.get('original_complete_circle_check_at_binary64_projection')
    if circle is not None:
        domain=circle.get('actual_domain',{})
        out['original_complete_circle_check_at_binary64_projection']=dict(identity=identity(circle),
            original=pick(circle,['original_full_reference_finite','reference_is_not_a_nonzero_parent',
                'reference_sha256','scalar_family_sha256','frozen_seven_added_shapes_square_check']),
            actual_domain={**scalar_fields(domain),
                'original_RMS_query_checks':domain.get('original_RMS_query_checks'),
                'full_original_domain_identity':identity(domain)},
            actual_failures_and_exceptions=exceptions_in(circle),
            complete_original_FFT_checks_identity=identity(circle.get('original_full_FFT_tangent_checks')))
    for name in ('fresh_extended_scalar_family','original_projection_call_trace',
                 'source_bound_family_views','source_bound_decimal_views'):
        if name in status:
            out[name+'_identity']=identity(status[name])
    if status.get('diagnostic_completed'):
        reader.required(status,['initial','final','initial_binary64_projection','final_binary64_projection',
            'complete_scalar_domain_at_binary64_projection','original_complete_circle_check_at_binary64_projection',
            'fixed_physical_scales','fixed_shape_definition','selected_shape',
            'outer_steps','complete_planned_outer_rows','stop_reason'],'completed_status')
        if reader.fd_checks!=120 or reader.fd_levels!=12:
            reader.metadata_errors.append(dict(path='complete_initial_final_ten_axis_FD',
                expected_checks=120,actual_checks=reader.fd_checks,expected_levels=12,actual_levels=reader.fd_levels))
    out['original_readback_coverage']=dict(
        original_outer_directions=len(actual_steps),planned_outer_directions=8,
        original_real_trial_rows=sum(len(row.get('trials',[])) for row in actual_steps),
        original_real_trial_budget_per_direction=20,
        fd_original_levels=reader.fd_levels,fd_original_column_checks=reader.fd_checks,
        fd_actual_failures_and_exceptions_count=len(reader.fd_failures),
        fd_actual_failures_and_exceptions_identity=identity(reader.fd_failures),
        fd_failures_full_original_details_location='each description / original_three_step_complete_ten_axis_FD / actual_failures_and_exceptions',
        metadata_errors=reader.metadata_errors,
        required_available_recorded_fields_complete=not reader.metadata_errors,
        large_original_tables_identified_but_not_transported=True,
        canonical_identity_scope='original JSON values; metadata-only serialization, no scientific recomputation',
        omitted_payload_categories=['matching zero-extension array descriptors',
            'per-trial full ten-parameter and112-right vectors','per-trial node/mid domain-minimum table',
            'earlier complete Q and R arrays; complete direction-model identities retained',
            'unused last-Q basis columns','terminal Robin detail tables',
            'complete literal-binding array descriptor lists','complete FD perturbation tables'],
        full_scientific_tables_not_independently_read_by_downstream_recipient=True,
        no_accuracy_certificate_from_metadata_or_FD=True)
    reference_actual_repeated_words(out,status)
    essential_r2_selection(out,status)
    essential_r3_selection(out,status)
    return out,not reader.metadata_errors


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rules-directory',type=Path)
    p.add_argument('--compute-outcome',default='not-recorded')
    args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    path=args.directory/STATUS_NAME
    complete=False
    try:
        if not path.is_file():
            out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,
                original_status_present=False,readout_source=file_identity(__file__),
                diagnostic_completed=False,complete_original_status_not_available=True,
                actual_compute_outcome=args.compute_outcome,scientific_failure_not_inferred=True)
        else:
            raw=path.read_bytes()
            out,complete=build(json.loads(raw),raw,args.directory,args.rules_directory,args.compute_outcome)
    except Exception as error:
        out=dict(schema='request178-readback-exception-v1',exception=repr(error),
            traceback=traceback.format_exc(),readout_source=file_identity(__file__),
            original_status=file_identity(path) if path.is_file() else None,
            complete_original_readback_not_claimed=True,scientific_failure_not_inferred=True)
    raw=encoded(out)
    sections={name:len(encoded(value)) for name,value in out.items()}
    original_identity=dict(bytes=len(raw),sha256=digest(raw))
    print(encoded(dict(event='request178-compact-section-byte-counts',total=len(raw),
        section_UTF8_bytes=sections,hard_bound=LIMIT,complete_original_status_not_recomputed=True)).decode(),flush=True)
    if len(raw)>LIMIT:
        out=dict(schema='request178-compact-summary-over-budget-v1',
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
    print('BEGIN_VISIBLE178_COMPACT_SUMMARY',flush=True)
    print(raw.decode('ascii'),flush=True)
    print('END_VISIBLE178_COMPACT_SUMMARY',flush=True)
    print(encoded(dict(event='request178-compact-summary-identity',**receipt,
        hash_scope='ASCII JSON bytes excluding log separator LF')).decode(),flush=True)
    return 0 if complete else 70


if __name__=='__main__':
    raise SystemExit(main())
