"""W4M: thirty new mean targets and one exact original terminal copy."""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import math
import os
import re
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

PUBLIC_REPOSITORY = json.loads(r'''"Rogerhu12/math-research-public"''')
TOPIC = json.loads(r'''"topics/visible-flex-exact-nearby"''')
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_four_step_physical_mean.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py"''')
KIND = json.loads(r'''"complete_four_step_physical_mean_and_Hilbert_Schmidt_reception_bounds"''')
PROBLEM_ID = json.loads(r'''"same_selected_complete_four_step_physical_mean31_v1"''')
PREFLIGHT_KIND = json.loads(r'''"four_step_physical_mean_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''99000''')
DIAGNOSTIC_TYPE_BYTES = json.loads(r'''128''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''512''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''2048''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":90421,"git_blob_sha":"edd66cdbe7a438569524ba2614d3822f61de5c81","path":"topics/visible-flex-exact-nearby/notes/strict_flux_mean_forcing_ci/run-43856579962-1/actual-scientific-conclusion.json","role":"wmt_actual","sha256":"c6680025917247e7bec958851d5ee85fc3c3750b059372a87ec568cd9d8acbd4"},{"bytes":82508,"git_blob_sha":"146904d030cca0887fae921084396bf4008d0281","path":"topics/visible-flex-exact-nearby/notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json","role":"wrp_actual","sha256":"4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":24710,"git_blob_sha":"8114ed738385635e004c93d64e2f3160378a04ee","path":"topics/visible-flex-exact-nearby/results/R133-supplement-complete-four-step-mean-source-and-physical-Hilbert-Schmidt-reception.md","role":"proof_W4M","sha256":"73497dbad99b42fa2edc47d7284746d48b5a65546b3264bf08be8e0dca1b1b71"}''')
EXPECTED_WORKER = json.loads(r'''{"bytes":26542,"git_blob_sha":"c410f91faae59dac177b737faffe4dd11d3f2d46","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py","role":"worker","sha256":"3770e29dbb2becd615227c1ceceaf7c9a34cf585a705deeed75465dc02594d8e"}''')
OLD_FIELDSETS = json.loads(r'''{"wmt_actual":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"],"wrp_actual":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"]}''')
OLD_QUALIFICATION_IDENTITIES = json.loads(r'''{"wmt_actual":{"bytes":57703,"sha256":"53b4ec258b7d8b2e56a8523c89907800b7c92fe58c18fbace46e62b5e35425db"},"wrp_actual":{"bytes":73852,"sha256":"f8d61ebe55f4ce10f94b9bd1b35e4d74eb208e493aa83291202da86506862971"}}''')
PROCESS_RECEIPT_KEYS = json.loads(r'''["kind","problem_id","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","runtime","arithmetic_bits","complete","proved","actual_returncode","stage","failure","current_target","completed_targets","saved_record_counts","gates","actual_progress","automatic_retry_authorized"]''')
OLD_GRAPH_ORDERS = json.loads(r'''{"wmt_actual":["complete_normalized_weight_L1_kernels","complete_strict_flux_amplitudes","complete_five_mean_recursions","complete_strict_mean_and_affine_sources","complete_negative_receiver","complete_waist_endpoint","complete_whole_and_reduced"],"wrp_actual":["complete_new_relative_phase_pullback_conclusion","complete_new_full_output_profile_weights_conclusion","complete_new_same_whole_receiver_conclusion"]}''')
OLD_GRAPH_COUNTS = json.loads(r'''{"wmt_actual":{"complete_five_mean_recursions":99,"complete_negative_receiver":6,"complete_normalized_weight_L1_kernels":25,"complete_strict_flux_amplitudes":55,"complete_strict_mean_and_affine_sources":4,"complete_waist_endpoint":2,"complete_whole_and_reduced":6},"wrp_actual":{"complete_new_full_output_profile_weights_conclusion":15,"complete_new_relative_phase_pullback_conclusion":7,"complete_new_same_whole_receiver_conclusion":18}}''')
OLD_GATE_LABELS = json.loads(r'''{"wmt_actual":["directed_public_runtime","current_input_and_AST_identity","all_five_complete_original_files_byte_identical","complete_WGS_pair_reference_and_binding","complete_prior_positive_weight_science","completed_posterior_nodes_and_parent_failure_retained","complete_scalar_and_qualification_copies_retained","true_lower_endpoints_and_normalized_jet_positions","complete_normalized_weight_L1_kernels","complete_strict_flux_amplitudes","complete_five_mean_recursions","complete_strict_mean_and_affine_sources","complete_negative_receiver","complete_waist_endpoint","complete_whole_and_reduced","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"],"wrp_actual":["directed_public_runtime","current_input_and_AST_identity","all_five_complete_original_files_byte_identical","complete_WJR_relative_phase_receipt","complete_WSM_profile_N6_receiver_same_binding","complete_original_scopes_and_failed_ancestry_retained","all_44_scalar_and_nine_qualification_copies_retained","same_measure_full_mean_original_phase_budgets_and_parity_window","complete_relative_inverse_phase_and_pullbacks","complete_fifteen_full_output_profile_weights","complete_same_whole_and_reduced_receiver","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]}''')
SHARED_ORIGINAL_ALIASES = json.loads(r'''["C_O","C_R","C_1","jump_collar","jump_strict","dyadic_one_third","dyadic_two_thirds","Bessel_prefactor","sqrt_two_upper","ell_plus_one_fourth_upper","ell_minus_negative_fourth_upper","Rplus","RF","Calg","D_infinity","Lrec"]''')
CROSS_MEAN_RECORD_PATHS = json.loads(r'''{"collar_raw_mean":["complete_new_graphs","complete_negative_receiver","new_records","complete_collar_raw_mean_union_upper"],"strict_primitive_mean":["complete_new_graphs","complete_strict_mean_and_affine_sources","new_records","complete_strict_primitive_mean_source_upper"],"waist_endpoint":["complete_new_graphs","complete_waist_endpoint","new_records","complete_same_waist_endpoint_upper"]}''')
RECORD_SPECS = json.loads(r'''{"Bessel_prefactor":{"endpoint":"upper","path":["copied_original_scalar_records","Bessel_prefactor"],"role":"wrp_actual"},"C_1":{"endpoint":"upper","path":["copied_original_scalar_records","C_1"],"role":"wrp_actual"},"C_O":{"endpoint":"upper","path":["copied_original_scalar_records","C_O"],"role":"wrp_actual"},"C_R":{"endpoint":"upper","path":["copied_original_scalar_records","C_R"],"role":"wrp_actual"},"Calg":{"endpoint":"upper","path":["copied_original_scalar_records","Calg"],"role":"wrp_actual"},"D_infinity":{"endpoint":"upper","path":["copied_original_scalar_records","D_infinity"],"role":"wrp_actual"},"Lrec":{"endpoint":"upper","path":["copied_original_scalar_records","Lrec"],"role":"wrp_actual"},"RF":{"endpoint":"upper","path":["copied_original_scalar_records","RF"],"role":"wrp_actual"},"Rplus":{"endpoint":"upper","path":["copied_original_scalar_records","Rplus"],"role":"wrp_actual"},"complete_terminal_dyadic_contribution_upper":{"endpoint":"upper","path":["copied_original_scalar_records","complete_terminal_dyadic_contribution_upper"],"role":"wrp_actual"},"dyadic_one_third":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_one_third"],"role":"wrp_actual"},"dyadic_two_thirds":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_two_thirds"],"role":"wrp_actual"},"ell_minus_negative_fourth_upper":{"endpoint":"upper","path":["copied_original_scalar_records","ell_minus_negative_fourth_upper"],"role":"wrp_actual"},"ell_plus_one_fourth_upper":{"endpoint":"upper","path":["copied_original_scalar_records","ell_plus_one_fourth_upper"],"role":"wrp_actual"},"endpoint_Vz":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_Vz"],"role":"wmt_actual"},"endpoint_WT":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_WT"],"role":"wmt_actual"},"endpoint_scattering":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_scattering"],"role":"wmt_actual"},"endpoint_second_order":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_second_order"],"role":"wmt_actual"},"ext_Vext_g0":{"endpoint":"upper","path":["copied_original_scalar_records","ext_Vext_g0"],"role":"wmt_actual"},"jump_collar":{"endpoint":"upper","path":["copied_original_scalar_records","jump_collar"],"role":"wrp_actual"},"jump_strict":{"endpoint":"upper","path":["copied_original_scalar_records","jump_strict"],"role":"wrp_actual"},"local_mean":{"endpoint":"upper","path":["copied_original_scalar_records","local_mean"],"role":"wmt_actual"},"local_raw_mean_source":{"endpoint":"upper","path":["copied_original_scalar_records","local_raw_mean_source"],"role":"wmt_actual"},"nonmean_collar_B":{"endpoint":"upper","path":["complete_new_graphs","complete_new_same_whole_receiver_conclusion","new_records","complete_collar_B_union_upper"],"role":"wrp_actual"},"nonmean_strict_B":{"endpoint":"upper","path":["complete_new_graphs","complete_new_same_whole_receiver_conclusion","new_records","strict_B_t_upper"],"role":"wrp_actual"},"point_profile":{"endpoint":"upper","path":["copied_original_scalar_records","point_profile"],"role":"wmt_actual"},"prior_reduced":{"endpoint":"upper","path":["whole_candidate_choices","reduced","complete_selected_upper"],"role":"wrp_actual"},"prior_whole":{"endpoint":"upper","path":["whole_candidate_choices","whole","complete_selected_upper"],"role":"wrp_actual"},"sqrt_two_upper":{"endpoint":"upper","path":["copied_original_scalar_records","sqrt_two_upper"],"role":"wrp_actual"},"strict_Ik":{"endpoint":"upper","path":["copied_original_scalar_records","strict_Ik"],"role":"wmt_actual"},"strict_Tk":{"endpoint":"upper","path":["copied_original_scalar_records","strict_Tk"],"role":"wmt_actual"},"strict_absolute_coefficient":{"endpoint":"upper","path":["copied_original_scalar_records","strict_absolute_coefficient"],"role":"wmt_actual"},"strict_backward_factor":{"endpoint":"upper","path":["copied_original_scalar_records","strict_backward_factor"],"role":"wmt_actual"},"strict_k0":{"endpoint":"upper","path":["copied_original_scalar_records","strict_k0"],"role":"wmt_actual"},"v3_0_0":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,0,0],"role":"wmt_actual"},"v3_0_1":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,0,1],"role":"wmt_actual"},"v3_0_2":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,0,2],"role":"wmt_actual"},"v3_0_3":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,0,3],"role":"wmt_actual"},"v3_0_4":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,0,4],"role":"wmt_actual"},"v3_0_5":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,0,5],"role":"wmt_actual"},"v3_1_0":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,1,0],"role":"wmt_actual"},"v3_1_1":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,1,1],"role":"wmt_actual"},"v3_1_2":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,1,2],"role":"wmt_actual"},"v3_1_3":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,1,3],"role":"wmt_actual"},"v3_1_4":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,1,4],"role":"wmt_actual"},"v3_1_5":{"endpoint":"upper","path":["complete_new_graphs","complete_five_mean_recursions","new_records","complete_inverse_levels",3,1,5],"role":"wmt_actual"},"wgs_y_g0":{"endpoint":"upper","path":["copied_original_scalar_records","wgs_y_g0"],"role":"wmt_actual"}}''')
SCOPE_SPECS = json.loads(r'''{"complete_WMT_endpoints_qualification":{"mode":"qualifications","path":["complete_new_graphs","complete_waist_endpoint"],"role":"wmt_actual"},"complete_WMT_flux_qualification":{"mode":"qualifications","path":["complete_new_graphs","complete_strict_flux_amplitudes"],"role":"wmt_actual"},"complete_WMT_inverse_levels_qualification":{"mode":"qualifications","path":["complete_new_graphs","complete_five_mean_recursions"],"role":"wmt_actual"},"complete_WMT_mean_qualification":{"mode":"qualifications","path":["complete_new_graphs","complete_strict_mean_and_affine_sources"],"role":"wmt_actual"},"complete_WMT_original_qualification_archive":{"mode":"exact","path":["copied_original_scopes"],"role":"wmt_actual"},"complete_WMT_parameters":{"mode":"exact","path":["parameters"],"role":"wmt_actual"},"complete_WMT_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wmt_actual"},"complete_WRP_current_receiver_qualification":{"mode":"qualifications","path":["complete_new_graphs","complete_new_same_whole_receiver_conclusion"],"role":"wrp_actual"},"complete_WRP_original_WSM_receiver_qualification":{"mode":"exact","path":["copied_original_scopes","complete_WSM_receiver_qualification"],"role":"wrp_actual"},"complete_WRP_parameters":{"mode":"exact","path":["parameters"],"role":"wrp_actual"},"complete_WRP_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wrp_actual"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"4457507a9e344c6821986797858f205a1fd9fc80ae5157901ed4a2853a802747"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''5581''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"d5220ec8513506f6510e57550068d326663bc591279fc0abb561e7ca305eedd2"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''55085''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"ddb5935e24b637920456579e468ea22fd0e42db37a384c5121ac9a6bebbd1876"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''12664''')
PARAMETERS = json.loads(r'''{"arithmetic_bits":320,"complete_input_Hilbert_Schmidt_factor":"original_Bessel_prefactor/768","complete_old_input_files":2,"decimal_record_digits":75,"first_absolute_mode":97,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","fixed_intrinsic_parameter":"eta_0","history_inputs":0,"input_order":[-4,3],"maximum_normalized_real_input_directions_per_frequency":2,"mean_source_decay":"n^(-17/6)","mean_steps":4,"minimum_physical_frequency":388,"new_exponentials":0,"new_fractional_powers":0,"new_graph_count":5,"new_logarithms":0,"new_quadratures":0,"new_record_count":30,"new_square_roots":1,"old_frequency_decay_unit_divisor":388,"old_local_mean_source_decay":"n^(-23/6)","old_targets_recomputed":0,"original_PW_cut":"2333968743003/10000000000000","original_records_copied_in_graphs":1,"original_true_interfaces":3070,"physical_frequency":"n=4|j|","physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph,n(r_star)=0","physical_period":"pi/2","preserved_inverse_level_angular_orders":[0,1],"preserved_original_inverse_level":3,"root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"source_qualification_object_count":11,"source_record_count":47,"strict_interval":["0","76285779072683/320000000000000"],"terminal_polynomial_degrees":[0,1,2,3,4,5,6],"total_scalar_record_slots":31}''')
RETAINED_SCOPE = json.loads(r'''{"actual96_columns_exist_and_signed_normalization_remains_uncomputed":true,"actual_even_zero_projection_and_same_parity_J_retained":true,"all_3070_actual_jumps_unchanged_and_no_length_factor":true,"all_four_endpoint_terms_and_positive_root_terms_retained":true,"all_original_near_and_two_far_genuine_profile_qualifications_retained":true,"all_twelve_original_third_inverse_level_records_are_copied":true,"at_most_two_normalized_real_input_directions_counted":true,"complete_reflected_column_factor_two_retained_once":true,"complete_terminal_degrees_0_through_6_retained":true,"disjoint_collar_L2_pieces_in_true_ordinary_dr":true,"entire_E3_terminal_dyadic_contribution_copied_without_subtraction":true,"exact_root_and_coefficient_finite_factors_Theta_nu_radial_head_retained":true,"full_input_Hminus4_3_sum_no_output_orthogonality_assumed":true,"full_k_Jr_Tk_beta_r_and_background_R0_qualifications_retained":true,"inverse_frequency_parameter_is_distinct_from_physical_mean":true,"local_complete_Z_and_raw_source_converted_only_by_388":true,"new_flow_ODE_log_exponential_quadrature":0,"new_mean_source_unit":"n^(-17/6)","no_old_Xi23_6_or_dyadic_mean_factor_applied_to_new_units":true,"no_old_mean_recursion_or_public_target_is_recomputed":true,"no_old_upper_subtraction":true,"no_smallness_or_actual_finite_inverse_claimed":true,"nonmean_candidate_assembled_from_positive_complete_original_records":true,"old_backward_exponential_and_absolute_coefficient_read_only":true,"old_candidate_wins_equal_saved_upper":true,"old_local_and_original_five_step_unit":"n^(-23/6)","old_scientific_calls":0,"old_targets_recomputed":0,"original_Bessel_factor_used_once_in_each_complete_HS_receiver":true,"original_ng_and_ordered_readout_each_once":true,"physical_mean_initial_condition":"z_ph,n(r_star)=0","root_upper_bracket_only_bounds_local_length":true,"same_fixed_intrinsic_eta0":true,"same_genuine_trial_full_Cn_beta_n_extended_potential":true,"selected_original_real_member_only":true,"strict_primitive_uses_same_L2_one_fourth_and_original_C1_window":true,"terminal_degree_zero_is_exact_old_record_copy_without_recalculation":true,"whole_Calg_and_reduced_Dinfinity_remain_distinct":true,"whole_Vz_and_both_stored_physical_means_retained":true,"whole_and_reduced_compared_only_to_own_current_complete_prior":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_new_four_step_terminal_conclusion","complete_new_four_step_physical_mean_conclusion","complete_new_four_step_negative_receiver_conclusion","complete_new_four_step_waist_endpoint_conclusion","complete_new_four_step_whole_and_reduced_conclusion"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_new_four_step_negative_receiver_conclusion":{"Hilbert_Schmidt_factor":"original_Bessel_prefactor/768","all_original_3070_jump_and_E3_terminal_contributions_retained":true,"complete":true,"disjoint_original_ordinary_dr_pieces":true,"input_order":[-4,3],"kind":"complete_new_four_step_negative_receiver_conclusion_v1","maximum_normalized_real_input_directions":2,"new_records":{"complete_collar_mean_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_nonmean_and_jumps_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_disjoint_collar_mean_L2_upper":{"ball":"__FINITE_SCALAR__"},"complete_mean_negative_Hilbert_Schmidt_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonmean_jump_and_terminal_negative_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_negative_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_mean_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_nonmean_and_jumps_received_upper":{"ball":"__FINITE_SCALAR__"}},"no_old_dyadic_mean_or_Xi23_6_reuse":true,"no_old_whole_upper_subtraction":true,"retained_scope_path":["retained_scope"],"same_selected_original_real_member":true},"complete_new_four_step_physical_mean_conclusion":{"complete":true,"complete_old_Tk_and_local_source_retained":true,"full_absolute_coefficient_used_for_derivative":true,"kind":"complete_new_four_step_physical_mean_conclusion_v1","mean_source_decay":"n^(-17/6)","new_records":{"complete_local_mean_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_local_raw_mean_source_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_mean_derivative_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_mean_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_primitive_mean_source_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_raw_mean_source_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"}},"old_local_unit_conversion_divisor":388,"retained_scope_path":["retained_scope"],"same_selected_original_real_member":true,"true_physical_mean_initial_condition":"z_ph,n(r_star)=0"},"complete_new_four_step_terminal_conclusion":{"complete":true,"complete_terminal_degrees":[0,1,2,3,4,5,6],"kind":"complete_new_four_step_terminal_conclusion_v1","mean_source_decay":"n^(-17/6)","minimum_physical_frequency":388,"new_records":{"complete_potential_angular_product_upper":{"ball":"__FINITE_SCALAR__"},"complete_reflected_strict_mean_source_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_terminal_degrees_0_through_6":[{"ball":"[4.04545082473570552082862631031227804031215248006217625761034891121888319507e+112 +/- 1.88e+37]"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"no_radial_integration_by_parts":true,"normalized_angular_orders":[0,1],"original_inverse_level_read_only":3,"reflected_column_factor":2,"retained_scope_path":["retained_scope"],"same_selected_original_real_member":true,"zero_degree_is_exact_original_first_derivative_copy":true},"complete_new_four_step_waist_endpoint_conclusion":{"complete":true,"kind":"complete_new_four_step_waist_endpoint_conclusion_v1","new_mean_decay":"n^(-17/6)","new_records":{"complete_physical_mean_endpoint_nminus17_6_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_waist_endpoint_upper":{"ball":"__FINITE_SCALAR__"}},"original_ng_factor_once":true,"retained_scope_path":["retained_scope"],"same_selected_original_real_member":true,"three_complete_nonmean_endpoint_terms_read_only":true,"whole_original_Vz_and_two_stored_means_retained":true},"complete_new_four_step_whole_and_reduced_conclusion":{"complete":true,"kind":"complete_new_four_step_whole_and_reduced_conclusion_v1","new_records":{"complete_all_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonroot_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_reduced_received_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_reduced_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_whole_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_whole_received_source_upper":{"ball":"__FINITE_SCALAR__"}},"no_signed_inverse_or_smallness_claimed":true,"original_root_and_coefficient_finite_factors_retained":true,"retained_scope_path":["retained_scope"],"same_ordered_readout_once":true,"same_selected_original_real_member":true,"whole_and_reduced_are_different_operators":true}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_new_four_step_negative_receiver_conclusion":8,"complete_new_four_step_physical_mean_conclusion":6,"complete_new_four_step_terminal_conclusion":9,"complete_new_four_step_waist_endpoint_conclusion":2,"complete_new_four_step_whole_and_reduced_conclusion":6}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_new_four_step_negative_receiver_conclusion":8,"complete_new_four_step_physical_mean_conclusion":6,"complete_new_four_step_terminal_conclusion":8,"complete_new_four_step_waist_endpoint_conclusion":2,"complete_new_four_step_whole_and_reduced_conclusion":6}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":2,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":5,"new_logarithms":0,"new_quadratures":0,"new_records_saved":30,"new_square_roots":1,"new_whole_comparisons_completed":2,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":11,"original_record_objects_copied":47,"original_records_copied_in_graphs":1}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","current_input_and_AST_identity","two_complete_original_actual_files_byte_identical","complete_WMTA_preserved_inverse_level_and_normalization","complete_WRPA_current_nonmean_provider_and_same_decomposition","complete_original_ancestry_scopes_and_exact_shared_receivers","all_47_scalar_and_eleven_qualification_copies_retained","same_four_step_decay_Hilbert_Schmidt_and_physical_mean_units","complete_four_step_terminal","complete_physical_mean_in_four_step_units","complete_negative_source_with_full_Hilbert_Schmidt_mean","complete_four_waist_endpoints","complete_whole_and_reduced_operator_candidates","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","copied_original_scalar_records","copied_original_scopes","complete_new_graphs","whole_candidate_choices","current_target","completed_targets","saved_record_counts","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized"]''')

def require(condition, message="qualification failed"):
    if not condition:
        raise AssertionError(message)

def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def reject_nonfinite(value):
    raise ValueError("nonfinite JSON literal: " + value)

def exact_json(raw):
    return json.loads(raw.decode("utf-8"), parse_constant=reject_nonfinite)

def same_json(a, b):
    return canonical(a) == canonical(b)

def at(value, path):
    for key in path:
        require((isinstance(value, dict) and key in value)
                or (isinstance(value, list) and type(key) is int
                    and 0 <= key < len(value)), "missing complete field")
        value = value[key]
    return value

def original_qualifications(value):
    """Keep all non-ball fields and every array position in the selected object."""
    if isinstance(value, dict):
        if set(value) == {"ball"} and isinstance(value["ball"], str):
            return None
        return {key: original_qualifications(child) for key, child in value.items()
                if key != "actual_mathematical_wall_seconds"}
    if isinstance(value, list):
        return [original_qualifications(child) for child in value]
    return copy.deepcopy(value)

def safe_path(root, rel):
    require(isinstance(rel, str) and rel.startswith(TOPIC + "/")
            and "\\" not in rel and "\x00" not in rel, "topic relative path")
    parts = Path(rel).parts
    require(".." not in parts and "." not in parts, "unsafe input path")
    result = (root / rel).resolve()
    require(result.is_relative_to(root), "input outside repository")
    return result

def five_fields(spec):
    return {key: spec[key] for key in
            ("role", "path", "bytes", "sha256", "git_blob_sha")}

def check_file(root, spec):
    require(set(spec) == {"role", "path", "bytes", "sha256", "git_blob_sha"},
            "five-field current input")
    require(type(spec["bytes"]) is int and 0 < spec["bytes"] < 100000
            and re.fullmatch("[0-9a-f]{64}", spec["sha256"])
            and re.fullmatch("[0-9a-f]{40}", spec["git_blob_sha"]),
            "input identity fields")
    raw = safe_path(root, spec["path"]).read_bytes()
    require(len(raw) == spec["bytes"] and digest(raw) == spec["sha256"],
            "complete input bytes or SHA differ: " + spec["role"])
    git = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(git == spec["git_blob_sha"], "complete Git blob differs")
    raw.decode("utf-8")
    return raw

def scalar_record_count(value):
    if isinstance(value, dict):
        if set(value) == {"ball"} and isinstance(value["ball"], str):
            return 1
        return sum(scalar_record_count(v) for v in value.values())
    if isinstance(value, list):
        return sum(scalar_record_count(v) for v in value)
    return 0

def complete_object_reference(docs, role, path):
    raw = canonical(at(docs[role], path))
    return {"input_role": role, "json_path": path,
            "complete_canonical_bytes": len(raw),
            "complete_canonical_sha256": digest(raw)}


def complete_shape(value, pattern):
    if pattern == "__FINITE_SCALAR__":
        return isinstance(value, str)
    if isinstance(pattern, dict):
        return (isinstance(value, dict) and set(value) == set(pattern)
                and all(complete_shape(value[k], pattern[k]) for k in pattern))
    if isinstance(pattern, list):
        return (isinstance(value, list) and len(value) == len(pattern)
                and all(complete_shape(x, y) for x, y in zip(value, pattern)))
    return type(value) is type(pattern) and value == pattern

def insert_new_record(container, path, record):
    require(isinstance(path, list) and len(path) > 0, "record path")
    current = container
    for position, key in enumerate(path):
        last = position + 1 == len(path)
        if isinstance(current, list):
            require(type(key) is int and key >= 0, "array record position")
            while len(current) <= key:
                current.append(None)
            if last:
                require(current[key] is None, "record target already saved")
                current[key] = copy.deepcopy(record)
                return
            if current[key] is None:
                current[key] = [] if type(path[position+1]) is int else {}
        else:
            require(isinstance(current, dict) and isinstance(key, str), "object record position")
            if last:
                require(key not in current, "record target already saved")
                current[key] = copy.deepcopy(record)
                return
            if key not in current:
                current[key] = [] if type(path[position+1]) is int else {}
        current = current[key]
    raise AssertionError("unreachable record insertion")

def bounded_diagnostic(raw, maximum_json_bytes):
    """Bound only an operational string, including its JSON escaping."""
    text = raw[:maximum_json_bytes].decode("utf-8", "ignore")
    while len(json.dumps(text, ensure_ascii=False).encode("utf-8")) > maximum_json_bytes:
        text = text[:-1]
    return text, text.encode("utf-8") != raw



def accepted_original_inputs(docs, files):
    return {
        "kind": "complete_original_WMTA_and_WRPA_readonly_admission_for_W4M_v1",
        "complete": True,
        "complete_original_file_receipts": [
            copy.deepcopy(files[spec["role"]]) for spec in EXPECTED_OLD_FILES],
        "complete_original_schema_fields": {
            role: sorted(old) for role, old in docs.items()},
        "complete_original_qualification_identities": {
            role: {"bytes": len(canonical(original_qualifications(old))),
                   "sha256": digest(canonical(original_qualifications(old)))}
            for role, old in docs.items()},
        "complete_original_process_bindings": {
            role: {key: copy.deepcopy(old[key]) for key in PROCESS_RECEIPT_KEYS}
            for role, old in docs.items()},
        "complete_original_ancestry_references": {
            role: {
                "complete_original_file_sha256": files[role]["sha256"],
                "accepted_original_inputs": complete_object_reference(docs, role, ["accepted_old_inputs"]),
                "complete_original_input_hashes": complete_object_reference(docs, role, ["input_sha256"]),
                "complete_original_qualification_archive":
                    complete_object_reference(docs, role, ["copied_original_scopes"])}
            for role in docs},
        "complete_preserved_WMTA_inverse_level_certificate":
            original_qualifications(docs["wmt_actual"]["complete_new_graphs"]["complete_five_mean_recursions"]),
        "complete_current_WRPA_selection_qualification":
            original_qualifications(docs["wrp_actual"]["whole_candidate_choices"]),
        "complete_WMTA_18_gates_195_new_and_2_old_copies_verified": True,
        "complete_WRPA_14_gates_40_new_verified": True,
        "all_twelve_original_v3_coefficients_and_three_zero_order_records_copied": True,
        "all_sixteen_shared_receiver_records_and_three_previous_mean_decomposition_records_exact": True,
        "complete_WMTA_original_qualification_archive_retained": True,
        "full_mean_and_same_operator_units_verified_before_new_unit_conversion": True,
        "old_selected_whole_and_reduced_paths_verified": True,
        "all_original_nonball_fields_and_array_positions_verified": True,
        "original_ancestry_full_byte_bound_and_failed_statuses_preserved": True,
        "old_scientific_calls": 0, "old_targets_recomputed": 0,
        "old_producer_imports_or_calls": 0, "history_inputs_restored": 0}


def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(len(manifest_raw) < 100000 and digest(manifest_raw) == manifest_sha,
            "complete manifest CLI identity")
    manifest = exact_json(manifest_raw)
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_W4M", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 6
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 6,
            "six complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "complete old input pin differs")
    require(same_json(files["proof_W4M"], EXPECTED_PROOF), "published W4M proof pin")
    require(same_json(files["worker"], EXPECTED_WORKER), "complete bounded worker pin")
    require(files["science"]["path"] == SOURCE_PATH
            and files["worker"]["path"] == WORKER_PATH, "entry and worker paths")
    raw = {spec["role"]: check_file(root, spec) for spec in specs}
    require(Path(__file__).resolve() == safe_path(root, SOURCE_PATH)
            and Path(__file__).read_bytes() == raw["science"], "actual new entry bytes")
    module_map = {"science": files["science"]["sha256"]}
    require(manifest["repository"] == PUBLIC_REPOSITORY
            and manifest["problem_id"] == PROBLEM_ID
            and same_json(manifest["scientific_modules"], [files["science"]])
            and same_json(manifest["parameters"], PARAMETERS),
            "one new scientific module and complete parameters")
    op = manifest["operation"]
    require(op["kind"] == KIND and op["problem_id"] == PROBLEM_ID
            and same_json(op["parameters"], PARAMETERS)
            and same_json(op["ordered_targets"], ORDERED_GRAPH_NAMES)
            and same_json(op["scientific_module_binding"], module_map)
            and op["bits_parameter"] == "arithmetic_bits", "operation profile")
    for role in ("science", "worker"):
        ast.parse(raw[role].decode("utf-8"), filename=files[role]["path"])
    docs = {spec["role"]: exact_json(raw[spec["role"]]) for spec in EXPECTED_OLD_FILES}
    for role, old in docs.items():
        require(sorted(old) == OLD_FIELDSETS[role] and canonical(old) == raw[role],
                "complete original schema or canonical bytes differ")
        body = canonical(original_qualifications(old))
        expected = OLD_QUALIFICATION_IDENTITIES[role]
        require(len(body) == expected["bytes"] and digest(body) == expected["sha256"],
                "complete original non-ball fields and array positions")
        require(old["complete"] is True and old["proved"] is True
                and old["actual_returncode"] == 0 and old["failure"] is None
                and old["current_target"] is None and old["stage"] == "complete"
                and old["arithmetic_bits"] == 320
                and old["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"}
                and old["automatic_retry_authorized"] is False
                and old["gates"] == [{"name": name, "passed": True}
                                      for name in OLD_GATE_LABELS[role]]
                and old["completed_targets"] == OLD_GRAPH_ORDERS[role]
                and same_json(old["saved_record_counts"], OLD_GRAPH_COUNTS[role])
                and set(old["complete_new_graphs"]) == set(OLD_GRAPH_ORDERS[role]),
                "complete original successful science and all ordered gates")
        for name, count in OLD_GRAPH_COUNTS[role].items():
            require(old["complete_new_graphs"][name]["complete"] is True
                    and scalar_record_count(old["complete_new_graphs"][name]) == count,
                    "all original complete graph scalar leaves")
        require(old["parameters"]["selected_original_real_member_only"] is True
                and old["parameters"]["fixed_intrinsic_eta0"] == PARAMETERS["fixed_intrinsic_eta0"]
                and old["parameters"]["strict_interval"] == PARAMETERS["strict_interval"]
                and old["parameters"]["root_interval"] == PARAMETERS["root_interval"]
                and old["parameters"]["same_operator_domain"] == PARAMETERS["same_operator_domain"]
                and old["parameters"]["original_PW_cut"] == PARAMETERS["original_PW_cut"]
                and old["parameters"]["original_true_interfaces"] == 3070
                and old["parameters"]["physical_mean_coordinates"] == 2
                and old["parameters"]["physical_mean_initial_condition"] == "z_ph(r_star)=0",
                "same actual real trial, input/output norms, true root and physical means")
        require(old["actual_progress"]["old_scientific_calls"] == 0
                and old["actual_progress"]["old_targets_recomputed"] == 0
                and old["actual_progress"]["old_binary_parts_restored"] == 0,
                "old successful read-only protocols")

    wm, wr = docs["wmt_actual"], docs["wrp_actual"]
    require(wm["kind"] == "complete_strict_flux_L1_mean_forcing_refinement"
            and wm["run_id"] == "43856579962" and wm["run_attempt"] == "1"
            and wm["actual_progress"]["new_records_saved"] == 195
            and wm["actual_progress"]["original_records_copied_in_graphs"] == 2
            and wm["actual_progress"]["new_graphs_completed"] == 7
            and wm["parameters"]["mean_source_decay"] == "n^(-23/6)"
            and wm["parameters"]["physical_frequency"] == "n=4|j|"
            and wm["parameters"]["first_absolute_mode"] == 97
            and wm["parameters"]["angular_normalization"] ==
                "ordinary pure angular derivative divided by j!",
            "complete WMTA original units and all old targets")
    kernels = wm["complete_new_graphs"]["complete_normalized_weight_L1_kernels"]
    require(kernels["normalized_circle_measure"] is True
            and kernels["angular_derivatives_divided_by_factorial"] is True,
            "complete original normalized-circle and angular units")
    inverse = wm["complete_new_graphs"]["complete_five_mean_recursions"]
    flux = wm["complete_new_graphs"]["complete_strict_flux_amplitudes"]
    require(inverse["all_five_recursions_and_terminal_retained"] is True
            and inverse["inverse_level_shapes"] == [[6,3],[5,4],[4,5],[3,6],[2,7]]
            and inverse["level_axis_order"] == ["angular_degree","inverse_frequency_degree"]
            and inverse["complete_terminal_degrees"] == list(range(8))
            and inverse["mean_source_decay"] == "n^(-23/6)"
            and inverse["minimum_physical_frequency"] == 388
            and inverse["reflected_column_factor"] == 2
            and flux["angular_derivatives_divided_by_factorial"] is True
            and flux["amplitude_polynomial_degree_order"] == [0,1,2]
            and flux["matrix_norm"] == "entry sum" and flux["vector_norm"] == "component sum"
            and flux["complete_extended_forcing_retained"] is True
            and flux["complete_genuine_potential_and_root_matrix_retained"] is True
            and flux["strict_T_reciprocal_not_extended_to_root"] is True,
            "true complete genuine L1 inverse level normalization")
    levels = inverse["new_records"]["complete_inverse_levels"]
    require(len(levels) == 5
            and all(isinstance(levels[i], list) and len(levels[i]) == nr
                    and all(isinstance(row, list) and len(row) == nc
                            for row in levels[i])
                    for i, (nr, nc) in enumerate(inverse["inverse_level_shapes"])),
            "all complete original inverse-level positions")
    wm_mean = wm["complete_new_graphs"]["complete_strict_mean_and_affine_sources"]
    require(wm_mean["full_absolute_mean_coefficient_used_for_derivative"] is True
            and wm_mean["local_complete_physical_mean_copied_unchanged"] is True
            and wm_mean["old_backward_exponential_read_only"] is True
            and wm_mean["upper_root_bracket_is_only_a_length_bound"] is True
            and wm["complete_new_graphs"]["complete_waist_endpoint"][
                "full_vz_and_two_physical_means_retained"] is True
            and wm["retained_scope"]["full_Jr_beta_r_e_kappa_and_R0_retained"] is True
            and wm["accepted_old_inputs"][
                "first_posterior_attempt_failure_not_relabelled_success"] is True,
            "complete physical mean, both patches, original derivative and endpoint scope")

    require(wr["kind"] == "complete_relative_phase_pullback_and_same_whole_receiver_bounds"
            and wr["run_id"] == "43881690924" and wr["run_attempt"] == "1"
            and wr["actual_progress"]["new_records_saved"] == 40
            and wr["actual_progress"]["original_records_copied_in_graphs"] == 0
            and wr["actual_progress"]["new_graphs_completed"] == 3
            and wr["parameters"]["input_order"] == [-4,3]
            and wr["parameters"]["physical_frequency"] == "4j"
            and wr["parameters"]["physical_period"] == "pi/2",
            "complete current WRPA same-operator provider")
    for key in (
        "complete_retained_v1_plus_n_inverse_v2_is_read_only",
        "entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction",
        "original_local_patch_and_all_physical_mean_costs_read_only",
        "actual_complete_even_mean_zero_projection_before_same_parity_J",
        "same_ordered_IJ_and_original_negative_windows",
        "full_signed_inputs_then_original_isometric_reflection_restriction",
        "no_radial_length_factor_on_jumps",
        "all_positive_root_four_waist_ends_and_ordered_readout_retained",
        "Theta_nu_radial_head_finite_factors_and_both_means_retained",
        "no_smallness_or_actual_finite_inverse_claimed"):
        require(wr["retained_scope"][key] is True, "complete current provider scope: " + key)
    require(wr["accepted_old_inputs"]["original_failed_ancestors_not_relabelled_success"] is True
            and wr["accepted_old_inputs"][
                "complete_WJR_15_gates_56_targets_and_WSM_22_gates_152_targets_verified"] is True,
            "complete original WJR/WSM identities and unchanged ancestry statuses")
    for alias in SHARED_ORIGINAL_ALIASES:
        require(same_json(wm["copied_original_scalar_records"][alias],
                          wr["copied_original_scalar_records"][alias]),
                "complete original receiver object changed: " + alias)
    for alias, path in CROSS_MEAN_RECORD_PATHS.items():
        require(same_json(at(wm, path), wr["copied_original_scalar_records"][alias]),
                "current provider uses a different old physical-mean decomposition")

    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 47 and all(
                isinstance(v, dict) and set(v) == {"ball"} and isinstance(v["ball"], str)
                for v in records.values())
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all forty-seven complete old scalar objects")
    for which in ("whole", "reduced"):
        choice = wr["whole_candidate_choices"][which]
        require(choice["both_complete_candidates_retained"] is True
                and choice["prior_wins_equal_saved_upper"] is True
                and choice["operator"] == ("whole" if which == "whole"
                    else "reduced_after_exact_finite_factor_separation")
                and choice["selected_label"] == "new_complete_relative_phase_pullback_candidate"
                and same_json(choice["complete_selected_upper"],
                              at(wr, choice["selected_record_path"]))
                and same_json(records["prior_" + which], choice["complete_selected_upper"]),
                "exact complete prior same-operator selected record")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(spec["mode"] in ("exact", "qualifications"), "scope mode")
        scopes[name] = (copy.deepcopy(value) if spec["mode"] == "exact"
                        else original_qualifications(value))
    require(len(scopes) == 11 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "eleven complete qualification objects and full WMTA scope archive")
    accepted = accepted_original_inputs(docs, files)
    require(len(canonical(accepted)) == ORIGINAL_ACCEPTED_BYTES
            and digest(canonical(accepted)) == ORIGINAL_ACCEPTED_SHA,
            "complete exact original read-only admission")
    verified = {role: {"bytes": spec["bytes"], "sha256": spec["sha256"]}
                for role, spec in files.items()}
    return {"root": root, "files": files, "raw": raw, "module_map": module_map,
            "verified": verified, "records": records, "scopes": scopes, "accepted": accepted}


def norm_upper(value):
    require(value.is_finite(), "nonfinite bound")
    require(value.lower() >= 0, "negative norm bound")
    return value.upper()

def saved_upper(record):
    require(isinstance(record, dict) and set(record) == {"ball"}
            and isinstance(record["ball"], str), "complete scalar record")
    return norm_upper(arb(record["ball"]))

def saved_positive_lower(record):
    require(isinstance(record, dict) and set(record) == {"ball"}
            and isinstance(record["ball"], str), "complete lower record")
    value = arb(record["ball"])
    require(value.is_finite() and value.lower() > 0, "positive lower endpoint")
    return value.lower()

def rational(value):
    f = Fraction(value)
    return arb(f.numerator) / arb(f.denominator)


def ex(value):
    """Exact integer constants for the finite positive polynomial."""
    require(type(value) is int, "exact integer constant")
    return arb(str(value))


def graph_record(graphs, name, path):
    require(name in graphs and graphs[name]["complete"] is True,
            "complete saved predecessor graph")
    return saved_upper(at(graphs[name]["new_records"], path))


"""W4M: thirty-one complete slots, thirty new targets and one old copy.

The owner supplies ex, saved_upper, graph_record, require and emit.
emit durably saves the entire scientific prefix, prints it, reads it
back, and returns the exact saved record. Every new downstream bound
uses only that returned record or a completed saved predecessor graph.
The only old actual inputs are the complete WMTA and WRPA receipts.
"""

def complete_four_step_terminal(saved, graphs, emit, copy_old):
    c0 = saved_upper(emit("complete_potential_angular_product_upper",
        saved_upper(saved["ext_Vext_g0"]) * saved_upper(saved["wgs_y_g0"])))
    # Degree zero is EXACTLY the already saved normalized first derivative.
    # Copy it verbatim; upper-plus-zero would repeat this completed target.
    terminal = [saved_upper(copy_old(["complete_terminal_degrees_0_through_6", 0],
        saved["v3_1_0"]))]
    for k in range(1, 7):
        derivative = saved_upper(saved["v3_1_" + str(k)]) if k <= 5 else ex(0)
        potential = c0 * saved_upper(saved["v3_0_" + str(k-1)])
        terminal.append(saved_upper(emit(["complete_terminal_degrees_0_through_6", k],
            derivative + potential)))
    total = sum((terminal[k] / ex(388)**k for k in range(7)), ex(0))
    emit("complete_reflected_strict_mean_source_nminus17_6_upper",
         ex(2) * saved_upper(saved["point_profile"]) * total)


def complete_mean_four_step_units(saved, graphs, emit):
    forcing = graph_record(graphs, "complete_new_four_step_terminal_conclusion",
        ["complete_reflected_strict_mean_source_nminus17_6_upper"])
    rc = ex(76285779072683) / ex(320000000000000)
    local_z = saved_upper(emit("complete_local_mean_nminus17_6_upper",
        saved_upper(saved["local_mean"]) / ex(388)))
    emit("complete_local_raw_mean_source_nminus17_6_upper",
         saved_upper(saved["local_raw_mean_source"]) / ex(388))
    strict_z = saved_upper(emit("complete_strict_mean_nminus17_6_upper",
        saved_upper(saved["strict_backward_factor"]) * (rc * forcing + local_z)))
    strict_zr = saved_upper(emit("complete_strict_mean_derivative_nminus17_6_upper",
        saved_upper(saved["strict_absolute_coefficient"]) * strict_z + forcing))
    emit("complete_strict_raw_mean_source_nminus17_6_upper",
        saved_upper(saved["strict_k0"]) * strict_zr
        + saved_upper(saved["strict_Tk"]) * strict_z)
    emit("complete_strict_primitive_mean_source_nminus17_6_upper",
        saved_upper(saved["strict_Ik"]) * strict_zr
        + saved_upper(saved["strict_Tk"]) * strict_z / ex(4))


def complete_negative_four_step_reception(saved, graphs, emit):
    mean_name = "complete_new_four_step_physical_mean_conclusion"
    strict_raw = graph_record(graphs, mean_name,
        ["complete_strict_raw_mean_source_nminus17_6_upper"])
    local_raw = graph_record(graphs, mean_name,
        ["complete_local_raw_mean_source_nminus17_6_upper"])
    strict_primitive = graph_record(graphs, mean_name,
        ["complete_strict_primitive_mean_source_nminus17_6_upper"])
    rc = ex(76285779072683) / ex(320000000000000)
    cpw = ex(2333968743003) / ex(10000000000000)
    rplus = ex(2383968743003) / ex(10000000000000)
    hs, hl = rc - cpw, rplus - rc
    require(hs.lower() > 0 and hl.lower() > 0, "original disjoint collar lengths")
    co = saved_upper(saved["C_O"])
    cr = saved_upper(saved["C_R"])
    c1 = saved_upper(saved["C_1"])
    bessel = saved_upper(saved["Bessel_prefactor"])

    collar_nonmean = saved_upper(emit("complete_collar_nonmean_and_jumps_received_upper",
        co * saved_upper(saved["sqrt_two_upper"])
        * saved_upper(saved["ell_plus_one_fourth_upper"])
        * saved_upper(saved["nonmean_collar_B"])
        + cr * saved_upper(saved["jump_collar"])))
    strict_nonmean = saved_upper(emit("complete_strict_nonmean_and_jumps_received_upper",
        c1 * (cpw * saved_upper(saved["ell_minus_negative_fourth_upper"])
        * saved_upper(saved["nonmean_strict_B"])
        + saved_upper(saved["jump_strict"]))))
    nonmean = saved_upper(emit("complete_nonmean_jump_and_terminal_negative_upper",
        bessel * (collar_nonmean * saved_upper(saved["dyadic_one_third"])
        + strict_nonmean * saved_upper(saved["dyadic_two_thirds"])
        + saved_upper(saved["complete_terminal_dyadic_contribution_upper"]))))

    collar_mean = saved_upper(emit("complete_disjoint_collar_mean_L2_upper",
        (hs * strict_raw**2 + hl * local_raw**2).sqrt()))
    collar_received = saved_upper(emit("complete_collar_mean_received_upper",
        co * collar_mean))
    strict_received = saved_upper(emit("complete_strict_mean_received_upper",
        c1 * cpw * strict_primitive))
    mean_received = saved_upper(emit("complete_mean_negative_Hilbert_Schmidt_upper",
        (bessel / ex(768)) * (collar_received + strict_received)))
    emit("complete_same_negative_error_upper", nonmean + mean_received)


def complete_four_step_waist_endpoint(saved, graphs, emit):
    strict_z = graph_record(graphs, "complete_new_four_step_physical_mean_conclusion",
        ["complete_strict_mean_nminus17_6_upper"])
    mean = saved_upper(emit("complete_physical_mean_endpoint_nminus17_6_upper",
        (saved_upper(saved["Bessel_prefactor"]) / ex(768))
        * saved_upper(saved["endpoint_Vz"]) * strict_z))
    emit("complete_same_waist_endpoint_upper",
        saved_upper(saved["endpoint_scattering"])
        + saved_upper(saved["endpoint_second_order"])
        + saved_upper(saved["endpoint_WT"]) + mean)


def complete_four_step_whole_receivers(saved, graphs, emit):
    negative = graph_record(graphs, "complete_new_four_step_negative_receiver_conclusion",
        ["complete_same_negative_error_upper"])
    endpoint = graph_record(graphs, "complete_new_four_step_waist_endpoint_conclusion",
        ["complete_same_waist_endpoint_upper"])
    nonroot = saved_upper(emit("complete_nonroot_source_sum_upper",
        saved_upper(saved["Rplus"]) + negative + endpoint))
    all_source = saved_upper(emit("complete_all_source_sum_upper",
        nonroot + saved_upper(saved["RF"])))
    whole_received = saved_upper(emit("complete_whole_received_source_upper",
        saved_upper(saved["Lrec"]) * all_source))
    emit("complete_same_whole_error_upper",
        saved_upper(saved["Calg"]) + whole_received)
    reduced_received = saved_upper(emit("complete_reduced_received_source_upper",
        saved_upper(saved["Lrec"]) * nonroot))
    emit("complete_same_reduced_error_upper",
        saved_upper(saved["D_infinity"]) + reduced_received)

def main():
    global arb
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("repo", "manifest", "manifest-sha", "out"):
        parser.add_argument("--" + key, required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    require(args.bits == 320, "fixed 320-bit arithmetic")
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == PUBLIC_REPOSITORY,
            "public own Actions only")
    run = os.environ.get("GITHUB_RUN_ID", "")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event = os.environ.get("GITHUB_SHA", "")
    checkout = os.environ.get("ACTUAL_CHECKOUT_COMMIT", "")
    require(re.fullmatch("[0-9]+", run) and re.fullmatch("[0-9]+", attempt)
            and re.fullmatch("[0-9a-f]{40}", event)
            and re.fullmatch("[0-9a-f]{40}", checkout), "actual public run identities")
    out = Path(args.out)
    require(not out.exists(), "completed or partial science already exists")
    if args.preflight_only:
        work = read_only_admission(args.repo, args.manifest, args.manifest_sha)
        print(canonical({"kind": PREFLIGHT_KIND, "complete": True,
            "problem_id": PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "scientific_modules": work["module_map"],
            "actual_checkout_commit": checkout,
            "verified_original_inputs": work["verified"],
            "accepted_old_inputs": work["accepted"],
            "copied_original_records_sha256": ORIGINAL_RECORD_SHA,
            "copied_original_scopes_sha256": ORIGINAL_SCOPE_SHA,
            "old_scientific_calls": 0, "flint_imported": False
            }).decode("utf-8"), end="", flush=True)
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    doc = {"kind": KIND, "problem_id": PROBLEM_ID, "complete": False,
        "proved": False, "stage": "read_only_admission", "failure": None,
        "actual_returncode": None, "runtime": {}, "arithmetic_bits": args.bits,
        "run_id": run, "run_attempt": attempt, "workflow_event_commit": event,
        "actual_checkout_commit": checkout, "scientific_modules": {},
        "manifest_sha256": args.manifest_sha, "input_sha256": {},
        "verified_original_inputs": {}, "original_source_AST_evidence": {},
        "parameters": copy.deepcopy(PARAMETERS),
        "retained_scope": copy.deepcopy(RETAINED_SCOPE), "accepted_old_inputs": {},
        "copied_original_scalar_records": {}, "copied_original_scopes": {},
        "complete_new_graphs": {}, "whole_candidate_choices": {},
        "current_target": None, "completed_targets": [],
        "saved_record_counts": {name: 0 for name in ORDERED_GRAPH_NAMES},
        "gates": [], "actual_progress": copy.deepcopy(ACTUAL_PROGRESS_INITIAL),
        "actual_mathematical_wall_seconds": 0.0,
        "automatic_retry_authorized": False}
    math_start = None
    new_counts = {name: 0 for name in ORDERED_GRAPH_NAMES}

    def publish(check_size=True):
        if math_start is not None:
            elapsed = time.perf_counter() - math_start
            require(math.isfinite(elapsed) and elapsed >= 0, "finite elapsed time")
            doc["actual_mathematical_wall_seconds"] = elapsed
        raw = canonical(doc)
        try:
            temporary = out.with_name(out.name + ".tmp")
            with open(temporary, "wb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary, out)
        finally:
            sys.stdout.write(raw.decode("utf-8"))
            sys.stdout.flush()
        if check_size:
            require(len(raw) <= MAX_SCIENCE_BYTES,
                    "complete scientific JSON exceeds frozen byte cap")
        restored = exact_json(out.read_bytes())
        require(canonical(restored) == raw, "atomic scientific readback differs")
        return restored

    def gate(name):
        require(len(doc["gates"]) < len(GATE_LABELS)
                and name == GATE_LABELS[len(doc["gates"])], "gate order")
        doc["gates"].append({"name": name, "passed": True})

    def start_graph(name):
        index = len(doc["completed_targets"])
        require(index < len(ORDERED_GRAPH_NAMES) and name == ORDERED_GRAPH_NAMES[index]
                and doc["current_target"] is None
                and name not in doc["complete_new_graphs"], "new graph order")
        pattern = copy.deepcopy(NEW_GRAPH_SHAPES[name])
        pattern["complete"] = False
        pattern["new_records"] = {}
        doc["complete_new_graphs"][name] = pattern
        doc["current_target"] = name
        doc["stage"] = "started:" + name
        publish()

        def emit(path, value):
            path = [path] if isinstance(path, str) else list(path)
            target = at(NEW_GRAPH_SHAPES[name]["new_records"], path)
            require(target == {"ball": "__FINITE_SCALAR__"}, "new target specification")
            record = {"ball": norm_upper(value).str(75)}
            insert_new_record(doc["complete_new_graphs"][name]["new_records"], path, record)
            doc["saved_record_counts"][name] += 1
            new_counts[name] += 1
            doc["actual_progress"]["new_records_saved"] += 1
            if name == ORDERED_GRAPH_NAMES[2] and path == ["complete_disjoint_collar_mean_L2_upper"]:
                doc["actual_progress"]["new_square_roots"] += 1
            doc["stage"] = "record_saved:" + name
            restored = publish()
            return copy.deepcopy(at(restored["complete_new_graphs"][name]["new_records"], path))
        def copy_old(path, record):
            require(name == ORDERED_GRAPH_NAMES[0]
                    and path == ["complete_terminal_degrees_0_through_6", 0]
                    and same_json(record, doc["copied_original_scalar_records"]["v3_1_0"])
                    and same_json(at(NEW_GRAPH_SHAPES[name]["new_records"], path), record),
                    "only the exact original zero-degree terminal may be copied")
            insert_new_record(doc["complete_new_graphs"][name]["new_records"], path, record)
            doc["saved_record_counts"][name] += 1
            doc["actual_progress"]["original_records_copied_in_graphs"] += 1
            doc["stage"] = "original_record_copied:" + name
            restored = publish()
            return copy.deepcopy(at(restored["complete_new_graphs"][name]["new_records"], path))
        return emit, copy_old

    def finish_graph(name):
        graph = doc["complete_new_graphs"][name]
        require(doc["current_target"] == name
                and doc["saved_record_counts"][name] == GRAPH_RECORD_COUNTS[name]
                and new_counts[name] == GRAPH_NEW_RECORD_COUNTS[name],
                "incomplete new record prefix")
        graph["complete"] = True
        require(complete_shape(graph, NEW_GRAPH_SHAPES[name]), "complete graph shape")
        doc["completed_targets"].append(name)
        doc["actual_progress"]["new_graphs_completed"] += 1
        doc["current_target"] = None
        doc["stage"] = "completed:" + name
        gate(GATE_LABELS[8 + len(doc["completed_targets"]) - 1])
        publish()

    publish()
    try:
        work = read_only_admission(args.repo, args.manifest, args.manifest_sha)
        doc["scientific_modules"] = copy.deepcopy(work["module_map"])
        doc["verified_original_inputs"] = copy.deepcopy(work["verified"])
        doc["input_sha256"] = {role: value["sha256"]
                               for role, value in work["verified"].items()}
        doc["input_sha256"]["manifest"] = args.manifest_sha
        doc["original_source_AST_evidence"] = {
            "count": 2, "roles": ["science", "worker"], "old_source_imports": 0,
            "one_new_scientific_entry_only": True}
        doc["accepted_old_inputs"] = copy.deepcopy(work["accepted"])
        doc["copied_original_scalar_records"] = copy.deepcopy(work["records"])
        doc["copied_original_scopes"] = copy.deepcopy(work["scopes"])
        doc["actual_progress"]["complete_original_files_admitted"] = 2
        doc["actual_progress"]["original_record_objects_copied"] = 47
        doc["actual_progress"]["original_qualification_objects_copied"] = 11
        doc["stage"] = "complete_original_input_copies_saved"
        publish()
        import flint
        from flint import arb, ctx
        require(sys.version_info[:3] == (3, 12, 14)
                and flint.__version__ == "0.9.0", "directed public runtime")
        ctx.prec = 320
        doc["runtime"] = {"Python": "3.12.14", "python_flint": "0.9.0"}
        for name in GATE_LABELS[:7]:
            gate(name)
        saved = doc["copied_original_scalar_records"]
        for alias, spec in RECORD_SPECS.items():
            require(spec["endpoint"] in ("lower", "upper"), "original endpoint type")
            if spec["endpoint"] == "lower":
                saved_positive_lower(saved[alias])
            else:
                saved_upper(saved[alias])
        require(PARAMETERS["minimum_physical_frequency"] == 388
                and PARAMETERS["mean_source_decay"] == "n^(-17/6)"
                and PARAMETERS["old_local_mean_source_decay"] == "n^(-23/6)",
                "distinct complete new and old mean-decay units")
        gate(GATE_LABELS[7])
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        operations = (
            ("complete_new_four_step_terminal_conclusion", complete_four_step_terminal),
            ("complete_new_four_step_physical_mean_conclusion", complete_mean_four_step_units),
            ("complete_new_four_step_negative_receiver_conclusion", complete_negative_four_step_reception),
            ("complete_new_four_step_waist_endpoint_conclusion", complete_four_step_waist_endpoint),
            ("complete_new_four_step_whole_and_reduced_conclusion", complete_four_step_whole_receivers))
        require([name for name, _ in operations] == ORDERED_GRAPH_NAMES, "complete new graph order")
        for name, function in operations:
            emit, copy_old = start_graph(name)
            if name == ORDERED_GRAPH_NAMES[0]:
                function(saved, doc["complete_new_graphs"], emit, copy_old)
            else:
                function(saved, doc["complete_new_graphs"], emit)
            finish_graph(name)
        # These are two independent SAME-operator choices after every new
        # target has been durably saved. No individual entry is minimized.
        graph_name = ORDERED_GRAPH_NAMES[-1]
        final = doc["complete_new_graphs"][graph_name]
        require(final["complete"] is True, "entire new receiver graph required")
        for which in ("whole", "reduced"):
            new_path = ["complete_new_graphs", graph_name, "new_records",
                        "complete_same_" + which + "_error_upper"]
            prior_path = ["copied_original_scalar_records", "prior_" + which]
            new_record = copy.deepcopy(at(doc, new_path))
            old_record = copy.deepcopy(at(doc, prior_path))
            use_new = saved_upper(new_record) < saved_upper(old_record)
            doc["whole_candidate_choices"][which] = {
                "operator": "whole" if which == "whole" else "reduced_after_exact_finite_factor_separation",
                "both_complete_candidates_retained": True,
                "prior_wins_equal_saved_upper": True,
                "prior_source_role": "wrp_actual",
                "prior_source_record_path": copy.deepcopy(RECORD_SPECS["prior_" + which]["path"]),
                "prior_record_path": prior_path, "new_record_path": new_path,
                "selected_label": ("new_complete_four_step_physical_mean_candidate"
                                   if use_new else "prior_selected_complete_candidate"),
                "selected_record_path": new_path if use_new else prior_path,
                "complete_selected_upper": copy.deepcopy(new_record if use_new else old_record)}
            doc["actual_progress"]["new_whole_comparisons_completed"] += 1
            doc["stage"] = "complete_same_" + which + "_choice_saved"
            publish()
        gate(GATE_LABELS[13])
        for role, spec in work["files"].items():
            require(check_file(work["root"], spec) == work["raw"][role],
                    "current input changed during new scalar work")
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "manifest changed during new scalar work")
        gate(GATE_LABELS[14])
        require(set(doc["whole_candidate_choices"]) == {"whole", "reduced"}
                and all(choice["both_complete_candidates_retained"] is True
                        and choice["prior_wins_equal_saved_upper"] is True
                        and same_json(choice["complete_selected_upper"], at(doc, choice["selected_record_path"]))
                        for choice in doc["whole_candidate_choices"].values()),
                "two complete independent same-operator selections")
        require(set(doc) == set(SCI_FIELDS)
                and doc["completed_targets"] == ORDERED_GRAPH_NAMES
                and doc["current_target"] is None
                and same_json(doc["saved_record_counts"], GRAPH_RECORD_COUNTS)
                and same_json(new_counts, GRAPH_NEW_RECORD_COUNTS)
                and same_json(doc["actual_progress"], ACTUAL_PROGRESS_COMPLETE)
                and complete_shape(doc["complete_new_graphs"], NEW_GRAPH_SHAPES)
                and digest(canonical(doc["copied_original_scalar_records"])) == ORIGINAL_RECORD_SHA
                and digest(canonical(doc["copied_original_scopes"])) == ORIGINAL_SCOPE_SHA,
                "complete new graph and actual progress")
        gate(GATE_LABELS[15])
        doc["complete"] = True
        doc["proved"] = True
        doc["actual_returncode"] = 0
        doc["stage"] = "complete"
        publish()
        return 0
    except BaseException as error:
        error_type = type(error).__name__.encode("utf-8", "replace")
        message = str(error).encode("utf-8", "replace")
        trace = traceback.format_exc().encode("utf-8", "replace")
        sys.stderr.write(trace.decode("utf-8", "replace"))
        sys.stderr.flush()
        doc["complete"] = False
        doc["proved"] = False
        doc["actual_returncode"] = 1
        doc["stage"] = "preserved_failure"
        type_text, type_cut = bounded_diagnostic(error_type, DIAGNOSTIC_TYPE_BYTES)
        message_text, message_cut = bounded_diagnostic(message, DIAGNOSTIC_MESSAGE_BYTES)
        trace_text, trace_cut = bounded_diagnostic(trace, DIAGNOSTIC_TRACEBACK_BYTES)
        doc["failure"] = {
            "type": type_text, "type_truncated": type_cut,
            "message": message_text, "traceback": trace_text,
            "message_truncated": message_cut, "traceback_truncated": trace_cut}
        publish(check_size=False)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
