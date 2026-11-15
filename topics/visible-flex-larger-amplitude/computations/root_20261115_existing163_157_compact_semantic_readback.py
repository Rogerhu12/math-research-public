#!/usr/bin/env python3
"""Request167: select original157 mathematical evidence from successful163 text.

Only official read-only metadata, bytes, original JSON lexemes and integer
coverage accounting. No scientific source is imported; no FD, matrix action,
model value, rank, derivative, interval or optimization is recomputed.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback
import uuid

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="existing163157-compact-original-semantic-readback-v1"
HELPER_NAME="root_20261115_existing151_157_log_readback.py"
HELPER_SHA="ecb77c7e4aae0b7888c58c753ca74d49f0528db3f743443582c3bc4503853250"
PART_LIMIT=76000
PART_COUNT=5
INDEX_LIMIT=18000
TOTAL_LIMIT=400000
M=None


def load_metadata_helper():
    global M
    path=Path(__file__).with_name(HELPER_NAME)
    raw=path.read_bytes()
    if len(raw)!=77301 or hashlib.sha256(raw).hexdigest()!=HELPER_SHA:
        raise RuntimeError("The frozen metadata-only transport helper differs")
    spec=importlib.util.spec_from_file_location("original163_metadata_only",path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    M=module
    return module


def ident(value):
    return M.identity(M.canonical(value))


def selected(value,keys):
    if not isinstance(value,dict):
        raise M.ReadbackError("Selected original field is not an object")
    return {key:value[key] for key in keys if key in value}


def primitives(value):
    return {key:item for key,item in value.items()
            if item is None or isinstance(item,(str,bool,M.RawNumber,int))}


def covered(value,scope):
    return dict(**ident(value),scope=scope,
        original_type=type(value).__name__,
        original_length=len(value) if isinstance(value,(dict,list,str)) else None,
        all_values_reprinted=False,values_recomputed=False)


def choose(value,keys):
    kept=selected(value,keys)
    omitted={key:item for key,item in value.items() if key not in kept}
    return dict(original_fields=kept,selection_keys_present=list(kept),
                other_original_fields=covered(omitted,
                "Explicit selection from the original group; excluded fields remain in original163 log"))



def required_shape(value,shape,label,checks):
    """JSON structure only; no finiteness, norm or scientific threshold."""
    if not shape:
        return
    if not isinstance(value,list):
        raise M.ReadbackError("Required original array is not a list: "+label)
    checks.equal("required array dimension "+label,len(value),shape[0])
    for index,item in enumerate(value):
        required_shape(item,shape[1:],label+"/"+str(index),checks)


def required_fields(value,fields,label,checks):
    for key,shape in fields.items():
        if key not in value:
            raise M.ReadbackError("Missing required recorded field: "+label+"/"+key)
        required_shape(value[key],shape,label+"/"+key,checks)


STATE_KEYS=(
 "parameters","parameter_encoding","unweighted_full3_merit","low_equations_used",
 "unit_diagonal_defects","complete_first_order_right_residual",
 "complete_first_order_native_height","complete_three_by_nine_forward_response",
 "forward_primal_equation_words_equal_to_real_state","terminal_Robin_terms",
 "low_mode_trajectory_max_by_mode","scalar_node_and_mid_minimum_radius",
 "source_circle_node_and_mid_minimum_radius","source_circle_node_and_mid_minimum_beta2",
 "radius_cell_denominator_minimum_absolute","high_right_leak_max",
 "high_free_core_Schur_elimination_computed","high_mode_nonresonance_proved",
 "same_literal_coefficient_model_not_reformed_continuous_metric",
 "raw_original_table_accuracy_not_certified","derivative_accuracy_or_exact_rank_not_certified")
PROJECTION_KEYS=(
 "parameters","three_by_nine_parameter_jacobian","low_equations_used","unit_diagonal_defects",
 "complete_first_order_right_residual","full_first_order_native_height","singular_values",
 "first_three_column_singular_values","old_four_column_singular_values",
 "old_six_column_singular_values","numerical_parameter_condition","high_right_leak_max",
 "source_circle_node_and_mid_minimum_radius","source_circle_node_and_mid_minimum_beta2",
 "scalar_node_and_mid_minimum_radius","radius_cell_denominator_minimum_absolute",
 "actual_circle_R_minus_supplied_a_node_max","low_original_collocation_tangent_residual_max",
 "low_mode_trajectory_max_by_mode","low_two_by_two_right_condition_max_by_mode",
 "high_free_core_Schur_elimination_computed","high_mode_nonresonance_proved",
 "numerical_singular_values_are_not_a_transversality_proof","zero_tail_slope_J")
FD_CHECK_KEYS=(
 "column","parameter","step","actual_step","valid","attempted","complete",
 "relative_error","exception","error","traceback",
 "positive_equations","negative_equations","complete_three_row_difference",
 "plus_equations","minus_equations","actual_column_difference")
CURVATURE_KEYS=(
 "schema","parameters","complete_three_equations","complete_three_by_nine_J",
 "complete_three_by_nine_by_nine_H","equation_Hessian_shape","full_right_Hessian_shape",
 "complete112_J_sha256","complete112_H_sha256","all112_native_rows_and_columns_consumed",
 "finite_second_variation_of_real_expression","discrete_rounding_derivative_or_interval_certificate",
 "parameter_or_state_projection_to_binary64","singular_or_weak_axes_discarded",
 "primal_body_is_original149","continuous_metric_coefficients_recomputed","symmetric_pair_order")
ORIGIN_MODEL_KEYS=(
 "path","physical_path","complete_three_by_nine_J","complete_three_by_nine_by_nine_H",
 "second_primal_equations","second_primal_words_equal_current",
 "original_first_forward_axis_J","second_J_minus_original_axis_J",
 "original_current_equations","relative_parameter_scales","original_formed_relative_gradient",
 "origin_merit","original_relative_radius","global_model_candidate_count",
 "complete_finite_model_points_evaluated","model_optimizer_completed","model_stop_reason",
 "unvisited_model_update_indices","selected_global_candidate","selected_model_reference",
 "selected_full_three_model_residual","selected_model_merit","selected_model_predicted_reduction",
 "actual_relative_direction","actual_nine_parameter_direction","scaled_direction_L2",
 "actual_direction_primal_equations","actual_direct_full3_action","formed_axis_action",
 "direct_minus_formed_axis_action","actual_full3_slope",
 "selected_model_point_not_an_accepted_physical_point",
 "finite_model_minimization_not_a_global_optimality_certificate")
TERMINAL_KEYS=(
 "index","current_relative_point","local_step_radius","complete",
 "full_three_model_residual","full_three_model_merit","complete_three_by_nine_model_J",
 "complete_nine_model_gradient","complete_nine_by_nine_model_Hessian",
 "full_model_gradient_norm","model_Hessian_formula","selected_candidate",
 "selected_model_trial","selected_relative_point","selected_model_merit","inner_radius_update",
 "reason","unvisited_candidate_indices","final_shift_lower","final_shift_upper",
 "shift_relative_margin","formed_shift_margin","shifted_solve_returned")
GN_KEYS=(
 "complete","normal_matrix_used_for_solve","original_three_residual_rows_not_reweighted",
 "reason","exception","ridge","square_root_ridge","ridge_formula","augmented_shape",
 "complete_augmented_rhs","complete_solution","formed_relative_L2",
 "complete_Q_identity","complete_R_identity","complete_augmented_matrix_identity",
 "original_QR_readback","complete_stationarity_residual",
 "exact_real_norm_and_descent_identity_not_a_floating_certificate")
SPECTRAL_KEYS=(
 "actual_rotation_count","all_nine_columns_retained","complete_nine_diagonal",
 "no_eigenvalue_or_orthogonality_certificate","no_singular_value_or_rank_cutoff",
 "not_a_new_scientific_acceptance_gate","relative_iteration_tolerance","sweeps")
FALLBACK_KEYS=(
 "original_pilot_axis_J","original_relative_scales","complete_basis_response",
 "basis_primal_equations","reformed_K_minus_pilot_product",
 "actual_nine_parameter_direction","actual_relative_direction","scaled_direction_L2",
 "actual_direct_full3_action","formed_axis_action","direct_minus_formed_axis_action",
 "actual_full3_slope","damping_mu","chosen_damping","chosen_damping_mu",
 "complete_upper_diagonal","column_permutation","original_linear_residual",
 "unscaled_original_linear_residual","complete_augmented_rhs",
 "normal_matrix_formed","singular_value_truncation","all_nine_columns_retained",
 "weak_columns_not_discarded","complete_QR_readback","original_QR_readback","positive_damping_mu","positive_damping_floor",
 "original_pilot_scaled_Frobenius_readback","direct_original_equation_action_used",
 "formed_basis_action","direct_minus_formed_basis_action","pilot_axis_action",
 "formed_augmented_stationarity","formed_augmented_stationarity_L2",
 "original_unweighted_full3_slope","basis_coordinate_direction")
TRIAL_COLUMNS=(
 "outer","trial_index","trial","path","alpha","accepted",
 "original_Armijo_bound","actual_merit","actual_unit_equations",
 "accepted_actual_parameters","accepted_actual_decimal_parameter_displacement",
 "actual_path_model_predicted_reduction","actual_minus_model_three_residuals",
 "actual_merit_minus_complete_model_merit","reason","exception",
 "normal_stop_reason","normal_target_met","normal_returned_constraint_error",
 "normal_returned_equations","normal_selected_sample","normal_attempts",
 "normal_returns","normal_domain_failures","normal_iteration_count",
 "normal_internal_trial_count","normal_same_trace_sample_count",
 "full112_original_identity","complete_trial_original_identity")
NORMAL_KEYS=(
 "called","reason","stop_reason","requested_constraint_error_tolerance_met",
 "returned_constraint_error","returned_original_equations",
 "selected_same_trace_sample","selected_sample","same_trace_selection_selected_index",
 "same_trace_selected_sample_index","uncorrected_seed_original_full3_merit",
 "returned_original_full3_merit","original_last_candidate_full3_merit",
 "same_trace_selection_changed_return","same_trace_selection_replaces_original_final",
 "original_final_candidate","original_terminal_candidate",
 "real_evaluation_attempts","real_evaluation_returns","axis_forward_attempts",
 "axis_forward_returns","normal_forward_attempts","normal_forward_returns",
 "original_domain_or_evaluation_failures","evaluation_errors",
 "requested_original_unit_constraint_error_tolerance","actual_constraint_target",
 "actual_returned_constraint_error","actual_returned_original_equations",
 "same_trace_full3_selection","unresolved_normal_target_does_not_exclude_original_full3_Armijo_trial")


class Selector:
    def __init__(self,checks,request):
        self.checks=checks
        self.request=request
        self.sections=[]
        self.fd_counts={}
        self.outer={}
        self.terminals={}
        self.trials={i:[] for i in range(8)}
        self.normal_failures=[]
        self.internal_exceptions=[]
        self.coverage={i:dict(updates=0,candidates=0,model_trial_rows=0) for i in range(8)}
        self.original_index=None
        self.original_receipt=None
        self.chain=None
        self.top_scalars={}
        self.top_identities=[]
        self.source_bindings=None

    def add(self,name,value,source):
        self.sections.append(dict(name=name,source_group=source,value=value))

    def fd(self,name,value,source):
        if not isinstance(value,list):
            raise M.ReadbackError("Original FD levels are not an ordered list: "+name)
        count=0
        for li,level in enumerate(value):
            rows=[]
            for row in level.get("checks_by_parameter",[]):
                chosen=primitives(row)
                chosen.update(selected(row,FD_CHECK_KEYS))
                chosen["complete_original_check_identity"]=ident(row)
                chosen["other_original_fields"]=sorted(set(row)-set(chosen))
                rows.append(chosen)
                count+=1
            meta={key:item for key,item in level.items() if key!="checks_by_parameter"}
            self.add(name+"-level-"+str(li),dict(
                original_level_fields=meta,checks_by_parameter=rows,
                complete_original_level_identity=ident(level),
                perturbation_parameter_and_response_tables_only_identity_covered=True,
                all_recorded_check_residuals_and_exceptions_in_selection=True),source)
        self.fd_counts[name]=count
        self.checks.equal("all original27 FD checks "+name,count,27)

    def top(self,key,value,source):
        if key in ("initial","final"):
            required_fields(value,{"parameters":[9],"low_equations_used":[3],
                "complete_three_by_nine_forward_response":[3,9]},key,self.checks)
            self.add(key+"-persistent-state",choose(value,STATE_KEYS),source)
            self.fd(key+"-persistent-first-FD",
                value["independent_high_precision_real_parameter_difference_checks"],source)
        elif key in ("initial_original_binary64_projection","final_original_binary64_projection"):
            phase=key.split("_",1)[0]
            self.add(phase+"-binary64-projection",dict(projection=value["projection"],
                description=choose(value["original_description"],PROJECTION_KEYS)),source)
            self.fd(phase+"-binary64-first-FD",
                value["original_description"]["independent_real_parameter_difference_checks"],source)
        elif key in ("initial_second_axis_difference_checks","final_second_axis_difference_checks"):
            self.fd(key,value,source)
        elif key in ("initial_ambient_curvature","final_ambient_curvature"):
            required_fields(value,{"complete_three_by_nine_J":[3,9],
                "complete_three_by_nine_by_nine_H":[3,9,9]},key,self.checks)
            self.add(key,choose(value,CURVATURE_KEYS),source)
        elif key in ("initial_second_J_minus_first_J","final_second_J_minus_first_J",
                     "literal_model_binding","consumed_source_sha256","readout_source_identity",
                     "input_sha256","actual_rule_sync"):
            self.add("original-"+key,value,source)
        elif key in ("complete_scalar_domain_at_binary64_projection",
                     "original_complete_circle_check_at_binary64_projection"):
            # Preserve all flags and top-level scalars. Deep diagnostic payloads
            # are explicitly covered, not relabelled as independently read.
            fields=primitives(value)
            fields.update(selected(value,("failures","exception","error","unresolved",
                "complete","success","bits","depth","source_sha256","actual_domain","covered_interval",
                "frozen_six_added_shapes_square_check")))
            self.add(key,dict(original_fields=fields,
                other_original_fields=covered(
                    {k:v for k,v in value.items() if k not in fields},
                    "Original full domain/circle report already preserved in163; this consumer selects flags/errors only")),source)
        elif value is None or isinstance(value,(str,bool,M.RawNumber,int)):
            self.top_scalars[key]=value
        else:
            self.top_identities.append(dict(field=key,**ident(value),
                original_length=len(value) if isinstance(value,(list,dict)) else None,
                all_values_printed=False))

    def origin(self,i,value,source):
        self.checks.equal("outer iteration",M.integer(value["iteration"]),i)
        required_fields(value,{"parameters":[9],"residual":[3],"derivative":[3,9]},
            "outer/"+str(i),self.checks)
        required_fields(value["direction_model"],{"complete_three_by_nine_J":[3,9],
            "complete_three_by_nine_by_nine_H":[3,9,9],
            "original_first_forward_axis_J":[3,9],
            "original_formed_relative_gradient":[9]},
            "outer/"+str(i)+"/direction_model",self.checks)
        common=selected(value,("iteration","parameters","residual","derivative","merit_before",
            "relative_radius","accepted","accepted_path","accepted_point_count_before",
            "path_status","radius_update","reason"))
        common["direction_model"]=choose(value["direction_model"],ORIGIN_MODEL_KEYS)
        if "fallback_direction_model" in value:
            fallback=value["fallback_direction_model"]
            fields=selected(fallback,FALLBACK_KEYS)
            # Small original QR objects may have a source-specific parent key.
            # Include every QR residual/permutation/diagonal occurrence without
            # repeating complete factor matrices or the damping search table.
            qr_records=[]
            def visit(item,path):
                if isinstance(item,dict):
                    wanted=("column_permutation","complete_upper_diagonal",
                            "original_linear_residual","unscaled_original_linear_residual",
                            "complete_stationarity_residual")
                    here=selected(item,wanted)
                    if here:
                        qr_records.append(dict(path=path,original_fields=here,
                                               complete_original_object_identity=ident(item)))
                    for key,child in item.items():
                        if key not in ("damping_search","complete_Q","complete_R") and isinstance(child,(dict,list)):
                            visit(child,path+[key])
                elif isinstance(item,list):
                    for j,child in enumerate(item):
                        if isinstance(child,(dict,list)):
                            visit(child,path+[j])
            visit(fallback,[])
            common["fallback_direction_model"]=dict(original_fields=fields,
                complete_original_identity=ident(fallback),all_original_QR_residual_records=qr_records,
                excluded_large_basis_and_damping_tables_only_identity_covered=True)
        if "fallback_curve_frame" in value:
            frame=value["fallback_curve_frame"]
            common["fallback_curve_frame"]=dict(original_fields=primitives(frame),
                complete_original_identity=ident(frame))
        self.outer[i]=common
        self.add("outer-"+str(i)+"-original-model",common,source)

    def terminal(self,i,value,source):
        required_fields(value,{"complete_three_by_nine_model_J":[3,9],
            "complete_nine_model_gradient":[9],"complete_nine_by_nine_model_Hessian":[9,9],
            "full_three_model_residual":[3],"current_relative_point":[9]},
            "outer/"+str(i)+"/last_model_update",self.checks)
        fields=selected(value,TERMINAL_KEYS)
        if "complete_residual_GN_preconditioner" not in value:
            raise M.ReadbackError("Original terminal GN record absent")
        gn=value["complete_residual_GN_preconditioner"]
        if "complete_solution" in gn:
            required_fields(gn,{"complete_solution":[9],"complete_augmented_rhs":[12],
                "complete_stationarity_residual":[9]},"terminal GN",self.checks)
            if "original_QR_readback" not in gn:
                raise M.ReadbackError("Returned GN solution has no original QR readback")
            required_fields(gn["original_QR_readback"],{"original_linear_residual":[12],
                "column_permutation":[9],"complete_upper_diagonal":[9]},
                "terminal GN/original_QR_readback",self.checks)
            fields["original_GN_QR_solve_recorded"]=True
        elif "exception" in gn or "reason" in gn:
            fields["original_GN_QR_solve_recorded"]=False
            fields["original_GN_no_solution_reason"]=selected(gn,("exception","reason","complete"))
        else:
            raise M.ReadbackError("GN has neither complete solution nor explicit original no-solve reason")
        if "complete_residual_GN_preconditioner" in value:
            fields["complete_residual_GN_preconditioner"]=choose(
                value["complete_residual_GN_preconditioner"],GN_KEYS)
        if "complete_spectral_guidance" in value:
            fields["complete_spectral_guidance"]=choose(
                value["complete_spectral_guidance"],SPECTRAL_KEYS)
        self.terminals[i]=fields
        self.add("outer-"+str(i)+"-last-internal-model",dict(original_fields=fields,
            complete_original_terminal_identity=ident(value),
            omitted_fields=sorted(set(value)-set(fields))),source)

    def trial(self,i,ti,value,source):
        self.checks.equal("physical trial index",M.integer(value["trial_index"]),ti)
        if ti!=len(self.trials[i]):
            raise M.ReadbackError("Nonconsecutive original physical trial")
        normal=value.get("normal_correction",{})
        iterations=normal.get("iterations",[])
        samples=normal.get("same_trace_selection_samples",[])
        normal_selected=selected(normal,NORMAL_KEYS)
        duplicated=("stop_reason","requested_constraint_error_tolerance_met","returned_constraint_error",
            "returned_original_equations","real_evaluation_attempts","real_evaluation_returns",
            "original_domain_or_evaluation_failures","evaluation_errors")
        normal_selected={key:item for key,item in normal_selected.items() if key not in duplicated}
        errs=[]
        for ni,item in enumerate(iterations):
            row=selected(item,("iteration","normal_model_exception","exception","error",
                              "accepted","actual_original_unit_constraint_error",
                              "original_equations","original_full3_merit"))
            if any(k in row for k in ("normal_model_exception","exception","error")):
                errs.append(dict(normal_iteration=ni,original_fields=row))
            for nt,inner in enumerate(item.get("trials",[])):
                if any(k in inner for k in ("exception","error")):
                    errs.append(dict(normal_iteration=ni,normal_trial=nt,
                        original_fields=selected(inner,("trial","alpha","accepted","reason","exception","error",
                            "actual_original_unit_constraint_error","original_equations"))))
        if errs or normal.get("evaluation_errors"):
            self.normal_failures.append(dict(outer=i,trial=ti,
                evaluation_errors=normal.get("evaluation_errors",[]),recorded_normal_errors=errs))
        data=dict(value)
        data.update(outer=i,
            accepted_actual_parameters=value.get("actual_parameters") if value.get("accepted") is True else None,
            accepted_actual_decimal_parameter_displacement=value.get("actual_decimal_parameter_displacement") if value.get("accepted") is True else None,
            normal_stop_reason=normal.get("stop_reason"),
            normal_target_met=normal.get("requested_constraint_error_tolerance_met"),
            normal_returned_constraint_error=normal.get("returned_constraint_error"),
            normal_returned_equations=normal.get("returned_original_equations"),
            normal_selected_sample=normal.get("same_trace_full3_selection",{}).get("selected_sample"),
            normal_attempts=normal.get("real_evaluation_attempts"),
            normal_returns=normal.get("real_evaluation_returns"),
            normal_domain_failures=normal.get("original_domain_or_evaluation_failures"),
            normal_iteration_count=len(iterations),
            normal_internal_trial_count=sum(len(row.get("trials",[])) for row in iterations),
            normal_same_trace_sample_count=len(samples),
            full112_original_identity=ident(value["actual_full112_right"]) if "actual_full112_right" in value else None,
            complete_trial_original_identity=source)
        self.trials[i].append([data.get(key) for key in TRIAL_COLUMNS])
        # Full returned/target normal records are deliberately small. Save the
        # existing original errors; never recompute or reinterpret inner tol.
        if normal and normal.get("called") is not False:
            self.trials[i][-1].append(normal_selected)
        else:
            self.trials[i][-1].append(selected(normal,("called","reason")))
        if "full_three_residual_quadratic_model" in value:
            pred=value["full_three_residual_quadratic_model"]
            self.trials[i][-1].append(selected(pred,(
                "full_three_residual_quadratic_prediction","residual_quadratic_square_merit",
                "formed_original_linear_term","formed_ambient_quadratic_term",
                "formed_cubic_cross_term","formed_nonnegative_quartic_term")))
        else:
            self.trials[i][-1].append(None)

    def accept(self,label,value,source):
        if label.startswith("157-original-top-"):
            self.top(label[len("157-original-top-"):],value,source)
            return
        match=re.fullmatch(r"157-outer-(\d+)-complete-model-and-path-terminal",label)
        if match:
            self.origin(int(match[1]),value,source);return
        match=re.fullmatch(r"157-outer-(\d+)-complete-original-last-model-update-terminal",label)
        if match:
            self.terminal(int(match[1]),value,source);return
        match=re.fullmatch(r"157-outer-(\d+)-complete-physical-trial-(\d+)",label)
        if match:
            self.trial(int(match[1]),int(match[2]),value,source);return
        match=re.fullmatch(r"157-outer-(\d+)-complete-original-selected-model-row",label)
        if match:
            self.add(label,value,source);return
        match=re.fullmatch(r"157-outer-(\d+)-model-update-(\d+)-coverage",label)
        if match:
            i,ui=int(match[1]),int(match[2]);count=self.coverage[i]
            self.checks.equal("internal update order",ui,count["updates"])
            count["updates"]+=1
            columns=value["candidate_coverage_columns"]
            for row in value["all_recorded_candidate_coverage_rows"]:
                self.checks.equal("candidate coverage width",len(row),len(columns))
                item=dict(zip(columns,row));count["candidates"]+=1
                count["model_trial_rows"]+=M.integer(item["actual_recorded_model_trials"])
                if item["complete_original_exception_rows"]:
                    self.internal_exceptions.append(dict(outer=i,update=ui,
                        candidate=item["index"],original_exception_rows=item["complete_original_exception_rows"]))
            return
        if label.startswith("157-complete-original-chain-"):
            if self.chain is not None:
                self.checks.equal("duplicate chain identical",self.chain,value)
            self.chain=value;return
        if label=="complete-original-reconstruction-scope-and-coverage":
            self.original_receipt=value;return
        if label=="official-original-run-job-and-protocol-source-binding":
            self.source_bindings=value;return
        if label=="complete-semantic-output-index":
            self.original_index=value;return
        if "producer-stderr" in label or "complete-readback-error" in label:
            self.add(label,value,source)

    def finish(self):
        self.checks.equal("all original outer models",sorted(self.outer),list(range(8)))
        self.checks.equal("all original terminal models",sorted(self.terminals),list(range(8)))
        expected=self.request["expected_original"]["physical_trial_counts"]
        for i in range(8):
            self.checks.equal("all actual physical trials outer "+str(i),len(self.trials[i]),expected[i])
            self.checks.equal("all recorded internal updates outer "+str(i),self.coverage[i]["updates"],32)
            self.add("outer-"+str(i)+"-complete-actual-trial-selection",
                dict(columns=list(TRIAL_COLUMNS)+["normal_terminal_original_fields","original_primary_prediction"],
                     rows=self.trials[i],
                     original_unprinted_trial_fields_scope="Rejected-point parameter vectors, all full112 trial vectors and intermediate normal matrices/perturbations retain original group SHA; all84 trial gates, residuals, merits, failures and accepted parameters are selected",
                     original_trial_count=len(self.trials[i]),
                     null_cell_means_original_field_absent_or_null=True,
                     rejected_parameters_are_explicitly_identity_only=True),None)
        self.checks.equal("total physical trials",sum(len(x) for x in self.trials.values()),84)
        self.checks.equal("all6 FD collections",len(self.fd_counts),6)
        if self.original_receipt is None or self.chain is None or self.source_bindings is None:
            raise M.ReadbackError("Required complete upstream receipt/chain/binding is missing")
        self.checks.equal("original complete view identity",
            self.original_receipt["complete_scalar_view"],self.request["expected_original"]["complete_view"])
        for key,wanted in (("original_status","original_status"),("complete_primary","original_primary"),
                           ("original_chain","original_chain")):
            self.checks.equal("original exact identity "+key,
                self.original_receipt[key],self.request["expected_original"][wanted])
        self.checks.equal("original157 source run",self.source_bindings["run"]["id"],
            self.request["expected_original"]["run_id"])
        self.checks.equal("original157 source head",self.source_bindings["run"]["head_sha"],
            self.request["expected_original"]["source_commit"])
        self.checks.equal("original source/input comparison",
            self.original_receipt["actual154_recorded_literal_comparison"],
            self.request["expected_original"]["actual154_recorded_literal_comparison"])
        self.add("original-all-top-scalar-fields",self.top_scalars,None)
        self.add("original-chain",self.chain,None)
        self.add("all-original-error-rows",dict(normal=self.normal_failures,
            internal_model=self.internal_exceptions),None)
        self.add("upstream-source-and-input-identity",dict(
            official_original=self.source_bindings,
            original_154_157_literal_comparison=self.original_receipt["actual154_recorded_literal_comparison"],
            original_status=self.original_receipt["original_status"],
            complete_view=self.original_receipt["complete_scalar_view"],
            primary=self.original_receipt["complete_primary"],
            original_chain=self.original_receipt["original_chain"]),None)
        self.add("all-unselected-top-field-identities",self.top_identities,None)
        return dict(original_fd_check_counts=self.fd_counts,
            all_original_physical_trials=84,all_original_outer_models=8,
            internal_coverage=self.coverage,
            full_intermediate_internal_or_perturbation_tables_independently_numerically_read=False,
            all_selected_values_are_original_words=True)


class ReadSemantic:
    def __init__(self,checks,selector,request):
        self.checks=checks;self.selector=selector;self.request=request
        self.current=None;self.descriptors=[];self.summary=None;self.capture=0

    def line(self,text):
        if text=="BEGIN_REQUEST163_READBACK_INDEX":
            if self.capture or self.summary is not None:
                raise M.ReadbackError("Duplicate upstream final index")
            self.capture=1;return
        if self.capture==1:
            raw=text.encode("ascii");self.summary=M.decode(text)
            self.checks.bytes("upstream actual163 final index",raw,
                self.request["upstream"]["complete_index"])
            self.capture=2;return
        if self.capture==2:
            if text!="END_REQUEST163_READBACK_INDEX":
                raise M.ReadbackError("Unterminated upstream final index")
            self.capture=0;return
        event=M.json_line(text)
        if event is None:
            return
        name=event.get("event")
        if name=="readback163-semantic-begin":
            if self.current is not None:
                raise M.ReadbackError("Interleaved upstream semantic groups")
            desc={k:v for k,v in event.items() if k!="event"}
            self.current=dict(desc=desc,parts=[],h=hashlib.sha256(),bytes=0)
        elif name=="readback163-semantic-part":
            row=self.current
            if row is None:
                raise M.ReadbackError("Semantic part without begin")
            desc=row["desc"];self.checks.equal("semantic part label",event["label"],desc["label"])
            self.checks.equal("semantic part index",M.integer(event["index"]),len(row["parts"]))
            self.checks.equal("semantic part count",event["parts"],desc["parts"])
            raw=event["data"].encode("ascii")
            self.checks.bytes("semantic original part",raw,event["data_identity"])
            row["parts"].append(event["data"]);row["h"].update(raw);row["bytes"]+=len(raw)
        elif name=="readback163-semantic-end":
            row=self.current
            if row is None:
                raise M.ReadbackError("Semantic end without begin")
            desc=row["desc"]
            for key in ("label","bytes","sha256","parts"):
                self.checks.equal("semantic end "+key,event[key],desc[key])
            self.checks.equal("semantic actual parts",len(row["parts"]),M.integer(desc["parts"]))
            self.checks.equal("semantic actual bytes",row["bytes"],M.integer(desc["bytes"]))
            self.checks.equal("semantic actual SHA",row["h"].hexdigest(),desc["sha256"])
            text="".join(row["parts"]);value=M.decode(text)
            source=dict(label=desc["label"],bytes=desc["bytes"],sha256=desc["sha256"])
            if desc["label"]=="complete-semantic-output-index":
                self.checks.equal("complete upstream semantic descriptor list",value,self.descriptors)
                self.checks.bytes("upstream original complete semantic index",text.encode("ascii"),
                    self.request["upstream"]["semantic_index"])
            else:
                self.descriptors.append(desc)
            self.selector.accept(desc["label"],value,source)
            self.current=None

    def finish(self):
        if self.current is not None or self.capture or self.summary is None:
            raise M.ReadbackError("Incomplete original semantic stream")
        for key,value in dict(complete=True,reader_exit_code=0,lane="157",
                run_id=str(self.request["upstream"]["run_id"]),
                source_commit=self.request["upstream"]["source_commit"]).items():
            self.checks.equal("upstream successful reader "+key,self.summary[key],value)
        self.checks.equal("upstream semantic group coverage",len(self.descriptors),
            M.integer(self.summary["semantic_output_group_count"]))
        self.checks.equal("upstream reconstruction receipt identity",
            ident(self.selector.original_receipt),self.summary["complete_reconstruction_receipt_identity"])
        self.checks.equal("upstream completed check count",
            M.integer(self.summary["checks"]["performed"]),169304)
        return dict(semantic_groups=len(self.descriptors),
            complete_original_descriptor_index_identity=ident(self.descriptors),
            original163_log_science_rerun=False,upstream_index=self.request["upstream"]["complete_index"])



def deduplicate_exact_tensors(sections):
    """Structural equality only: all selected arrays remain complete once.

    A reference is valid only after equal canonical bytes, not an approximate
    value or hash-only test. The mathematical arrays are not multiplied,
    reordered, rounded, shortened or reconstructed by a numerical formula.
    """
    table=[];buckets={};references=0
    def tensor(value):
        if isinstance(value,list):
            return bool(value) and all(tensor(x) for x in value)
        return value is None or isinstance(value,(str,bool,M.RawNumber,int))
    def visit(value):
        nonlocal references
        if isinstance(value,list) and tensor(value):
            raw=M.canonical(value)
            if len(raw)>=700:
                key=(len(raw),M.sha(raw))
                for entry,original in buckets.get(key,[]):
                    if original==raw:
                        references+=1
                        return {"request167_exact_array_ref":entry["reference"]}
                entry=dict(reference="array-"+str(len(table)).zfill(4),
                           bytes=len(raw),sha256=M.sha(raw),value=value)
                table.append(entry);buckets.setdefault(key,[]).append((entry,raw))
                references+=1
                return {"request167_exact_array_ref":entry["reference"]}
            return value
        if isinstance(value,list):
            return [visit(x) for x in value]
        if isinstance(value,dict):
            return {key:visit(item) for key,item in value.items()}
        return value
    transformed=[visit(x) for x in sections]
    for entry in table:
        transformed.append(dict(name="complete-exact-"+entry["reference"],source_group=None,
            value=entry,scope="Complete selected original array; exact references require this whole original value"))
    return transformed,dict(schema="request167-exact-selected-array-reference-v1",
        reference_key="request167_exact_array_ref",distinct_complete_arrays=len(table),
        reference_occurrences=references,duplicate_equivalence="canonical ASCII original JSON byte equality",
        all_referenced_array_values_printed_once=True,
        numerical_equality_or_matrix_arithmetic_used=False,
        reconstruction="Gather complete-exact-array sections; verify each value bytes/SHA; replace each single-key reference object with the complete value; selected original words are unchanged")


def pack_sections(sections,source):
    """Complete named semantic objects; never numeric rounding or row truncation."""
    bins=[[] for _ in range(PART_COUNT)]
    def packet(index,rows):
        return dict(schema=SCHEMA+"-report",part_index=index,planned_parts=PART_COUNT,
                    source=source,sections=rows,
                    original_words_only=True,scientific_computation_performed=False)
    for section in sorted(sections,key=lambda x:len(M.canonical(x)),reverse=True):
        eligible=[]
        for i,items in enumerate(bins):
            raw=M.canonical(packet(i,items+[section]))
            if len(raw)<=PART_LIMIT:
                eligible.append((len(M.canonical(packet(i,items))),i))
        if not eligible:
            sizes=[dict(name=row["name"],bytes=len(M.canonical(row))) for row in sections]
            raise SizeFailure("Complete selected sections exceed five76000-byte report packets",sizes)
        i=min(eligible)[1];bins[i].append(section)
    result=[M.canonical(packet(i,items)) for i,items in enumerate(bins)]
    if any(len(raw)>PART_LIMIT for raw in result):
        raise M.ReadbackError("Report size accounting failure")
    return result


class SizeFailure(Exception):
    def __init__(self,message,sizes):
        super().__init__(message);self.sizes=sizes


def output_value(name,raw):
    if os.environ.get("GITHUB_OUTPUT"):
        token="VISIBLE167_"+uuid.uuid4().hex
        with open(os.environ["GITHUB_OUTPUT"],"a",encoding="ascii") as stream:
            stream.write(name+"<<"+token+"\n"+raw.decode("ascii")+"\n"+token+"\n")
            stream.write(name+"_bytes="+str(len(raw))+"\n")
            stream.write(name+"_sha256="+M.sha(raw)+"\n")


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv)
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY:
        raise RuntimeError("Only this repository public Actions may run the readback")
    load_metadata_helper()
    checks=M.Checks();token=os.environ.get("GH_TOKEN","")
    out=None;started=time.monotonic();stage="request binding"
    packets=[];sections=[];summary=dict(schema=SCHEMA,request_number=167,
        run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
        complete=False,exit_code=70,scientific_computation_performed=False,
        original157_or163_science_rerun=False,new_artifact_Release_or_Git_data=False)
    try:
        raw=args.request.read_bytes()
        if M.sha(raw)!=args.request_sha256:
            raise M.ReadbackError("Actual167 request differs from explicit workflow pin")
        request=json.loads(raw,object_pairs_hook=M.unique)
        if (request.get("schema")!="existing163157-compact-semantic-request-v1"
            or request.get("request_number")!=167 or request.get("repository")!=REPOSITORY):
            raise M.ReadbackError("Wrong independent167 request")
        checks.bytes("this metadata selector",Path(__file__).read_bytes(),request["reader"])
        checks.bytes("frozen metadata helper",Path(__file__).with_name(HELPER_NAME).read_bytes(),request["helper"])
        summary["request"]=M.identity(raw);summary["reader"]=M.file_identity(__file__)
        temp=Path(os.environ["RUNNER_TEMP"]).resolve()
        name="visible-existing163157-"+os.environ["GITHUB_RUN_ID"]+"-"+os.environ.get("GITHUB_RUN_ATTEMPT","1")
        candidate=args.out.resolve()
        if candidate.parent!=temp or candidate.name!=name or candidate.exists():
            raise M.ReadbackError("Require a fresh request-owned RUNNER_TEMP direct child")
        candidate.mkdir(mode=0o700);out=candidate
        stage="official successful163 run/job/source binding"
        api=M.GitHub(token)
        summary["upstream_binding"]=M.source_binding(api,request["upstream"],checks)
        for row in summary["upstream_binding"]["protocol_sources"]:
            if row["path"].endswith("/"+HELPER_NAME):
                row["source_not_imported"]=False
                row["same_frozen_metadata_only_helper_imported_locally"]=True
        summary["no_scientific_module_imported"]=True
        stage="one successful163 read157 log download"
        log=out/"original163-read157.log"
        summary["original_log"]=api.download_job_log_once(request["upstream"]["compute_job_id"],
            log,request["upstream"]["maximum_log_bytes"])
        M.emit(dict(event="request167-one-original-log-download",identity=summary["original_log"]))
        stage="all original semantic groups"
        selector=Selector(checks,request);reader=ReadSemantic(checks,selector,request)
        lines=M.NormalizedLines(log)
        for number,text in lines:
            reader.line(text)
            if number%10000==0:
                M.emit(dict(event="request167-original-lines",count=number,no_scientific_work=True))
        summary["semantic_transport"]=reader.finish()
        summary["selection_scope"]=selector.finish()
        sections,summary["selected_array_transport"]=deduplicate_exact_tensors(selector.sections)
        n=lines.receipt()
        summary["transport_normalization"]={key:value for key,value in n.items()
            if key!="exceptional_transport_prefixes"}
        summary["transport_normalization"]["exceptional_prefix_records"]=covered(
            n["exceptional_transport_prefixes"],"Complete exceptional-prefix metadata counted and hashed; no scientific text edited")
        stage="bounded complete named report packets"
        source=dict(upstream_run=request["upstream"]["run_id"],
            upstream_job=request["upstream"]["compute_job_id"],
            original157_run=request["expected_original"]["run_id"],
            original157_source=request["expected_original"]["source_commit"])
        packets=pack_sections(sections,source)
        summary.update(complete=True,exit_code=0,exception=None,
            checks=checks.summary(),report_sections=len(sections),
            report_packets=[dict(index=i,**M.identity(raw),
                section_names=[x["name"] for x in M.decode(raw)["sections"]]) for i,raw in enumerate(packets)])
    except Exception as error:
        summary.update(complete=False,exit_code=70,failed_stage=stage,
            exception=M.redact_transport_text(repr(error),token),
            complete_traceback=M.redact_transport_text(traceback.format_exc(),token),
            performed_metadata_checks=checks.count,
            completed_check_rows_sha256=checks.h.hexdigest(),
            original_scientific_failure_not_inferred=True)
        if isinstance(error,SizeFailure):
            summary["complete_selected_section_byte_counts"]=error.sizes
        elif sections:
            summary["complete_selected_section_byte_counts"]=[
                dict(name=x["name"],bytes=len(M.canonical(x))) for x in sections]
    finally:
        cleanup=dict(attempted=out is not None,completed=False,exception=None,
                     only_fresh_owned_log_directory=True)
        if out is not None:
            try:
                import shutil
                cleanup["original_file_identities"]=[]
                for path in sorted(out.iterdir()):
                    if path.is_symlink() or not path.is_file():
                        raise M.ReadbackError("Unexpected object in owned temporary directory")
                    cleanup["original_file_identities"].append(dict(name=path.name,**M.file_identity(path)))
                shutil.rmtree(out);cleanup["completed"]=True
            except Exception as error:
                cleanup["exception"]=M.redact_transport_text(repr(error),token)
                cleanup["complete_traceback"]=M.redact_transport_text(traceback.format_exc(),token)
                summary.update(complete=False,exit_code=70)
        summary["owned_cleanup"]=cleanup
        summary["elapsed_wall_seconds"]=format(time.monotonic()-started,".9f")
        summary["stage"]=stage
    raw=M.canonical(summary)
    total=len(raw)+sum(len(x) for x in packets)
    if len(raw)>INDEX_LIMIT or total>TOTAL_LIMIT:
        # Preserve the actual error object in the compute log in lossless
        # byte parts; never report successful or complete selected output.
        M.stream_text("request167-complete-oversize-index",raw.decode("ascii"),
                      "Complete metadata exception/index, not scientific recomputation")
        summary=dict(schema=SCHEMA,request_number=167,complete=False,exit_code=70,
            exception="Complete index or total selected report budget exceeded",
            original_complete_index_identity=M.identity(raw),
            complete_index_in_compute_semantic_parts=True,
            packet_identities=[M.identity(x) for x in packets],
            packets_not_silently_truncated=True,owned_cleanup=cleanup)
        raw=M.canonical(summary)
        packets=[]
    for i,data in enumerate(packets):
        output_value("part"+str(i),data)
        print("BEGIN_REQUEST167_REPORT_"+str(i),flush=True)
        print(data.decode("ascii"),flush=True)
        print("END_REQUEST167_REPORT_"+str(i),flush=True)
    output_value("summary",raw)
    print("BEGIN_REQUEST167_INDEX",flush=True)
    print(raw.decode("ascii"),flush=True)
    print("END_REQUEST167_INDEX",flush=True)
    return summary["exit_code"]


if __name__=="__main__":
    raise SystemExit(main())
