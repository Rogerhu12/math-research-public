"""WRP: forty complete full-mean phase-pullback and same-operator receiver targets."""
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
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py"''')
KIND = json.loads(r'''"complete_relative_phase_pullback_and_same_whole_receiver_bounds"''')
PROBLEM_ID = json.loads(r'''"same_selected_complete_relative_phase_pullback_receiver40_v1"''')
PREFLIGHT_KIND = json.loads(r'''"relative_phase_pullback_receiver_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''95000''')
DIAGNOSTIC_TYPE_BYTES = json.loads(r'''128''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''512''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''2048''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":69002,"git_blob_sha":"80499e42f643e607db47c973b54f2243629a05e8","path":"topics/visible-flex-exact-nearby/notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json","role":"wjr_actual","sha256":"806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660"},{"bytes":30834,"git_blob_sha":"7caabc2c0ca0953a3fe8d4c6ae25116c2ee09220","path":"topics/visible-flex-exact-nearby/notes/strict_scaled_mixed_complete_ci/run-43877268949-1/actual-scientific-conclusion.json","role":"wsm_index","sha256":"3cb8fa2a506df28e634564a97aa124cb10aeb474a4daf02d7c7d62ac422d5172"},{"bytes":10901,"git_blob_sha":"fd6cc26610532bcb0aae73ff4e0ba8c7ad69e655","path":"topics/visible-flex-exact-nearby/notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_angular_profile.json","role":"wsm_profile","sha256":"860c6eca208427ebf72503924445e277701f62b7640992b9dc0b1321572673ed"},{"bytes":22944,"git_blob_sha":"26baf34bdfda9e5191fb55cc5893f2f8bd2a5d6c","path":"topics/visible-flex-exact-nearby/notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_ordered_N6.json","role":"wsm_N6","sha256":"4de5f900e09d548e2325d2ed09d4e68f74c596342c97648477e67a502396c4b6"},{"bytes":14230,"git_blob_sha":"15eb048bf37a6bcc28aeaa6d745a026bdbdd5a62","path":"topics/visible-flex-exact-nearby/notes/strict_scaled_mixed_complete_ci/run-43877268949-1/graphs/strict_complete_whole_receiver.json","role":"wsm_receiver","sha256":"2413d02a10b9e465212970a5cdeef41ef9091854f496921fefa528cea6851983"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":16951,"git_blob_sha":"9f55708ca3a0a6018279628342fb8715a48ab830","path":"topics/visible-flex-exact-nearby/results/R133-supplement-relative-phase-pullbacks-and-complete-receiver-refinement.md","role":"proof_WRP","sha256":"95be269fc011c756fff2f882a32828ad7293bbaa140c28f0cf6eb5474e674f36"}''')
OLD_FIELDSETS = json.loads(r'''{"wjr_actual":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"],"wsm_N6":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"wsm_index":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","angular_packet_identity","arithmetic_bits","automatic_retry_authorized","complete","completed_targets","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_record_copy_counts","original_source_AST_evidence","parameters","partial_target_reference","problem_id","proved","relative_angular_packet_identity","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_graph_files","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"],"wsm_profile":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"wsm_receiver":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"]}''')
OLD_QUALIFICATION_IDENTITIES = json.loads(r'''{"wjr_actual":{"bytes":59291,"sha256":"f3f92df917ea429cc6cbdbb37da132e9f4e1fdea6a8f94786b1389e4991ad4df"},"wsm_N6":{"bytes":13897,"sha256":"4a45fc1b9b03aec78980157684959c5e5efbbd858f06a4708b237aae523a6567"},"wsm_index":{"bytes":30780,"sha256":"08eec042b2f945baf3bde9dadecd12c0cd62746ca080183e9ed3174908f1696e"},"wsm_profile":{"bytes":7141,"sha256":"dcb0c12cf4b3894e4e437275b67eaed00f96e29201ef402ae65a9c824d7afbed"},"wsm_receiver":{"bytes":7887,"sha256":"a896dbdbd7481eac3355de1b17c987ccd9cf601cdab8a58537ef9a81a70823ce"}}''')
PROCESS_RECEIPT_KEYS = json.loads(r'''["kind","problem_id","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","runtime","arithmetic_bits","complete","proved","actual_returncode","stage","failure","current_target","completed_targets","saved_record_counts","gates","actual_progress","automatic_retry_authorized"]''')
RECORD_SPECS = json.loads(r'''{"Bessel_prefactor":{"endpoint":"upper","path":["conclusion","copied_original_records","Bessel_prefactor"],"role":"wsm_receiver"},"C_1":{"endpoint":"upper","path":["conclusion","copied_original_records","C_1"],"role":"wsm_receiver"},"C_O":{"endpoint":"upper","path":["conclusion","copied_original_records","C_O"],"role":"wsm_receiver"},"C_R":{"endpoint":"upper","path":["conclusion","copied_original_records","C_R"],"role":"wsm_receiver"},"Calg":{"endpoint":"upper","path":["conclusion","copied_original_records","Calg"],"role":"wsm_receiver"},"D_infinity":{"endpoint":"upper","path":["conclusion","copied_original_records","D_infinity"],"role":"wsm_receiver"},"Lrec":{"endpoint":"upper","path":["conclusion","copied_original_records","Lrec"],"role":"wsm_receiver"},"N_minus4_3_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","N_minus4_3_upper"],"role":"wsm_receiver"},"N_minus5_3_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","N_minus5_3_upper"],"role":"wsm_receiver"},"RF":{"endpoint":"upper","path":["conclusion","copied_original_records","RF"],"role":"wsm_receiver"},"Rplus":{"endpoint":"upper","path":["conclusion","copied_original_records","Rplus"],"role":"wsm_receiver"},"collar_raw_mean":{"endpoint":"upper","path":["conclusion","copied_original_records","collar_raw_mean"],"role":"wsm_receiver"},"complete_terminal_dyadic_contribution_upper":{"endpoint":"upper","path":["conclusion","new_records","new_negative_receiver","complete_terminal_dyadic_contribution_upper"],"role":"wsm_receiver"},"dyadic_one_third":{"endpoint":"upper","path":["conclusion","copied_original_records","dyadic_one_third"],"role":"wsm_receiver"},"dyadic_two_thirds":{"endpoint":"upper","path":["conclusion","copied_original_records","dyadic_two_thirds"],"role":"wsm_receiver"},"ell_minus_negative_fourth_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","ell_minus_negative_fourth_upper"],"role":"wsm_receiver"},"ell_plus_one_fourth_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","ell_plus_one_fourth_upper"],"role":"wsm_receiver"},"inverse_phase_derivative_1":{"endpoint":"upper","path":["conclusion","copied_original_records","original_inverse_phase_derivative_1"],"role":"wsm_profile"},"jump_collar":{"endpoint":"upper","path":["conclusion","copied_original_records","jump_collar"],"role":"wsm_receiver"},"jump_strict":{"endpoint":"upper","path":["conclusion","copied_original_records","jump_strict"],"role":"wsm_receiver"},"local_B_c_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","local_B_c_upper"],"role":"wsm_receiver"},"phase_pullback_L2":{"endpoint":"upper","path":["conclusion","copied_original_records","original_phase_pullback_L2"],"role":"wsm_profile"},"prior_reduced":{"endpoint":"upper","path":["conclusion","new_records","whole_and_reduced","complete_same_reduced_error_upper"],"role":"wsm_receiver"},"prior_whole":{"endpoint":"upper","path":["conclusion","new_records","whole_and_reduced","complete_same_whole_error_upper"],"role":"wsm_receiver"},"profile_normalized_0":{"endpoint":"upper","path":["conclusion","copied_original_records","complete_profile_p0_q0"],"role":"wsm_profile"},"profile_normalized_1":{"endpoint":"upper","path":["conclusion","new_records","jets","complete_profile","p0_q1"],"role":"wsm_profile"},"profile_normalized_2":{"endpoint":"upper","path":["conclusion","new_records","jets","complete_profile","p0_q2"],"role":"wsm_profile"},"profile_normalized_3":{"endpoint":"upper","path":["conclusion","new_records","jets","complete_profile","p0_q3"],"role":"wsm_profile"},"profile_normalized_4":{"endpoint":"upper","path":["conclusion","new_records","jets","complete_profile","p0_q4"],"role":"wsm_profile"},"relative_positive_phase_1":{"endpoint":"upper","path":["complete_new_graphs","complete_new_positive_phase_average_ratio_conclusion","new_records","ordinary_common_positive_phase_and_average_ratios_1_through_14",0],"role":"wjr_actual"},"relative_positive_phase_2":{"endpoint":"upper","path":["complete_new_graphs","complete_new_positive_phase_average_ratio_conclusion","new_records","ordinary_common_positive_phase_and_average_ratios_1_through_14",1],"role":"wjr_actual"},"relative_positive_phase_3":{"endpoint":"upper","path":["complete_new_graphs","complete_new_positive_phase_average_ratio_conclusion","new_records","ordinary_common_positive_phase_and_average_ratios_1_through_14",2],"role":"wjr_actual"},"retained_amplitude_angle_0":{"endpoint":"upper","path":["conclusion","new_records","strict_regrouping","ordinary_angles_0_4","angle_0"],"role":"wsm_receiver"},"retained_amplitude_angle_1":{"endpoint":"upper","path":["conclusion","new_records","strict_regrouping","ordinary_angles_0_4","angle_1"],"role":"wsm_receiver"},"retained_amplitude_angle_2":{"endpoint":"upper","path":["conclusion","new_records","strict_regrouping","ordinary_angles_0_4","angle_2"],"role":"wsm_receiver"},"retained_amplitude_angle_3":{"endpoint":"upper","path":["conclusion","new_records","strict_regrouping","ordinary_angles_0_4","angle_3"],"role":"wsm_receiver"},"retained_amplitude_angle_4":{"endpoint":"upper","path":["conclusion","new_records","strict_regrouping","ordinary_angles_0_4","angle_4"],"role":"wsm_receiver"},"sqrt_ell_plus_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","sqrt_ell_plus_upper"],"role":"wsm_receiver"},"sqrt_two_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","sqrt_two_upper"],"role":"wsm_receiver"},"strict_IJminus2":{"endpoint":"upper","path":["conclusion","copied_original_records","strict_IJminus2"],"role":"wsm_receiver"},"strict_Jminus5_3":{"endpoint":"upper","path":["conclusion","copied_original_records","strict_Jminus5_3"],"role":"wsm_receiver"},"strict_primitive_mean":{"endpoint":"upper","path":["conclusion","copied_original_records","strict_primitive_mean"],"role":"wsm_receiver"},"two_one_sixth_upper":{"endpoint":"upper","path":["conclusion","copied_original_records","two_one_sixth_upper"],"role":"wsm_receiver"},"waist_endpoint":{"endpoint":"upper","path":["conclusion","copied_original_records","waist_endpoint"],"role":"wsm_receiver"}}''')
SCOPE_SPECS = json.loads(r'''{"complete_WJR_parameters":{"mode":"exact","path":["parameters"],"role":"wjr_actual"},"complete_WJR_positive_phase_ratio_qualification":{"mode":"qualifications","path":["complete_new_graphs","complete_new_positive_phase_average_ratio_conclusion"],"role":"wjr_actual"},"complete_WJR_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wjr_actual"},"complete_WSM_ordered_N6_qualification":{"mode":"qualifications","path":["conclusion"],"role":"wsm_N6"},"complete_WSM_original_input_qualification_references":{"mode":"exact","path":["accepted_old_inputs"],"role":"wsm_index"},"complete_WSM_parameters":{"mode":"exact","path":["parameters"],"role":"wsm_index"},"complete_WSM_profile_qualification":{"mode":"qualifications","path":["conclusion"],"role":"wsm_profile"},"complete_WSM_receiver_qualification":{"mode":"qualifications","path":["conclusion"],"role":"wsm_receiver"},"complete_WSM_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wsm_index"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"aa9086fce792a007eb09eb0a7a076364cb9dfe8f8506e97a68fc4b37bceed75b"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''5452''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"9f3e9070c01ffd7682fb17841a962664cf8f28b2136c2525795367fa7a3898f2"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''43857''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"d1cf3cc5eea82af08e63064a982203a1fb35b0420ec7a9ea29924607e78ad38c"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''11239''')
PARAMETERS = json.loads(r'''{"arithmetic_bits":320,"comparison_matrix_coordinates":"(L2 norm, sqrt(2) first derivative L2 norm, second derivative L2 norm), same normalized measure","comparison_matrix_shape":[3,3],"complete_old_input_files":5,"decimal_record_digits":75,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","fixed_intrinsic_parameter":"eta_0","history_inputs":0,"input_order":[-4,3],"minimum_physical_frequency":388,"negative_windows":[[0,1],[5,3],[2,1]],"new_fractional_powers":2,"new_graph_count":3,"new_record_count":40,"new_square_roots":1,"old_targets_recomputed":0,"ordinary_derivative_convention":"same physical angular derivative; normalized profile coefficient multiplied by j! once","original_PW_cut":"2333968743003/10000000000000","original_true_interfaces":3070,"physical_frequency":"4j","physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","profile_angular_orders":[0,1,2,3,4],"relative_positive_phase_orders":[1,2,3],"root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"source_qualification_object_count":9,"source_record_count":44,"strict_interval":["0","76285779072683/320000000000000"]}''')
RETAINED_SCOPE = json.loads(r'''{"Theta_nu_radial_head_finite_factors_and_both_means_retained":true,"actual_complete_even_mean_zero_projection_before_same_parity_J":true,"all_actual_96_physical_columns_and_still_uncomputed_signed_normalization_separate":true,"all_fifteen_weight_entries_preserved":true,"all_near_and_two_far_genuine_profiles_retained":true,"all_positive_root_four_waist_ends_and_ordered_readout_retained":true,"comparison_matrix_is_auxiliary_H2_seminorm_space_not_physical_state":true,"complete_retained_v1_plus_n_inverse_v2_is_read_only":true,"entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction":true,"fixed_intrinsic_parameter":"eta_0","full_Bessel_spaces_include_mean_and_all_zero_low_high_output_modes":true,"full_signed_inputs_then_original_isometric_reflection_restriction":true,"new_exp_log_ODE_quadrature":0,"new_local_mean_jump_endpoint_targets":0,"no_radial_length_factor_on_jumps":true,"no_smallness_or_actual_finite_inverse_claimed":true,"normalized_profile_coefficients_to_ordinary_once":true,"old_candidate_wins_equal_saved_upper":true,"old_global_phase_budget_not_replaced_by_cut_phase_lower":true,"old_scientific_calls":0,"old_targets_recomputed":0,"ordinary_phase_ratios_divide_same_actual_positive_function_before_norms":true,"original_L2_pullback_is_distinct_complete_operator_budget":true,"original_PW_cut":"2333968743003/10000000000000","original_inverse_first_derivative_is_pointwise_complete_budget":true,"original_local_patch_and_all_physical_mean_costs_read_only":true,"original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","profile_zero_order_copied_independently_not_reexpanded":true,"same_normalized_circle_measure_for_three_comparison_coordinates":true,"same_ordered_IJ_and_original_negative_windows":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"],"whole_and_reduced_compared_only_to_their_own_complete_old_candidates":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_new_relative_phase_pullback_conclusion","complete_new_full_output_profile_weights_conclusion","complete_new_same_whole_receiver_conclusion"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_new_full_output_profile_weights_conclusion":{"complete":true,"kind":"complete_new_full_output_profile_weights_conclusion_v1","new_records":{"five_thirds":{"angle_0":{"ball":"__FINITE_SCALAR__"},"angle_1":{"ball":"__FINITE_SCALAR__"},"angle_2":{"ball":"__FINITE_SCALAR__"},"angle_3":{"ball":"__FINITE_SCALAR__"},"angle_4":{"ball":"__FINITE_SCALAR__"}},"two":{"angle_0":{"ball":"__FINITE_SCALAR__"},"angle_1":{"ball":"__FINITE_SCALAR__"},"angle_2":{"ball":"__FINITE_SCALAR__"},"angle_3":{"ball":"__FINITE_SCALAR__"},"angle_4":{"ball":"__FINITE_SCALAR__"}},"zero":{"angle_0":{"ball":"__FINITE_SCALAR__"},"angle_1":{"ball":"__FINITE_SCALAR__"},"angle_2":{"ball":"__FINITE_SCALAR__"},"angle_3":{"ball":"__FINITE_SCALAR__"},"angle_4":{"ball":"__FINITE_SCALAR__"}}},"ordinary_physical_angular_derivatives":true,"original_complete_profile_and_N6_immutable":true,"retained_scope":{"Theta_nu_radial_head_finite_factors_and_both_means_retained":true,"actual_complete_even_mean_zero_projection_before_same_parity_J":true,"all_actual_96_physical_columns_and_still_uncomputed_signed_normalization_separate":true,"all_fifteen_weight_entries_preserved":true,"all_near_and_two_far_genuine_profiles_retained":true,"all_positive_root_four_waist_ends_and_ordered_readout_retained":true,"comparison_matrix_is_auxiliary_H2_seminorm_space_not_physical_state":true,"complete_retained_v1_plus_n_inverse_v2_is_read_only":true,"entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction":true,"fixed_intrinsic_parameter":"eta_0","full_Bessel_spaces_include_mean_and_all_zero_low_high_output_modes":true,"full_signed_inputs_then_original_isometric_reflection_restriction":true,"new_exp_log_ODE_quadrature":0,"new_local_mean_jump_endpoint_targets":0,"no_radial_length_factor_on_jumps":true,"no_smallness_or_actual_finite_inverse_claimed":true,"normalized_profile_coefficients_to_ordinary_once":true,"old_candidate_wins_equal_saved_upper":true,"old_global_phase_budget_not_replaced_by_cut_phase_lower":true,"old_scientific_calls":0,"old_targets_recomputed":0,"ordinary_phase_ratios_divide_same_actual_positive_function_before_norms":true,"original_L2_pullback_is_distinct_complete_operator_budget":true,"original_PW_cut":"2333968743003/10000000000000","original_inverse_first_derivative_is_pointwise_complete_budget":true,"original_local_patch_and_all_physical_mean_costs_read_only":true,"original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","profile_zero_order_copied_independently_not_reexpanded":true,"same_normalized_circle_measure_for_three_comparison_coordinates":true,"same_ordered_IJ_and_original_negative_windows":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"],"whole_and_reduced_compared_only_to_their_own_complete_old_candidates":true},"same_full_mean_Bessel_circle":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_phase_pullback_conclusion":{"complete":true,"kind":"complete_new_relative_phase_pullback_conclusion_v1","new_records":{"complete_column_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_phase_pullback_Hminus2_upper":{"ball":"__FINITE_SCALAR__"},"complete_phase_pullback_Hminus5_3_upper":{"ball":"__FINITE_SCALAR__"},"complete_row_sum_upper":{"ball":"__FINITE_SCALAR__"},"inverse_phase_derivative_2_upper":{"ball":"__FINITE_SCALAR__"},"inverse_phase_derivative_3_upper":{"ball":"__FINITE_SCALAR__"},"inverse_phase_derivative_4_upper":{"ball":"__FINITE_SCALAR__"}},"ordinary_physical_angular_derivatives":true,"original_complete_profile_and_N6_immutable":true,"retained_scope":{"Theta_nu_radial_head_finite_factors_and_both_means_retained":true,"actual_complete_even_mean_zero_projection_before_same_parity_J":true,"all_actual_96_physical_columns_and_still_uncomputed_signed_normalization_separate":true,"all_fifteen_weight_entries_preserved":true,"all_near_and_two_far_genuine_profiles_retained":true,"all_positive_root_four_waist_ends_and_ordered_readout_retained":true,"comparison_matrix_is_auxiliary_H2_seminorm_space_not_physical_state":true,"complete_retained_v1_plus_n_inverse_v2_is_read_only":true,"entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction":true,"fixed_intrinsic_parameter":"eta_0","full_Bessel_spaces_include_mean_and_all_zero_low_high_output_modes":true,"full_signed_inputs_then_original_isometric_reflection_restriction":true,"new_exp_log_ODE_quadrature":0,"new_local_mean_jump_endpoint_targets":0,"no_radial_length_factor_on_jumps":true,"no_smallness_or_actual_finite_inverse_claimed":true,"normalized_profile_coefficients_to_ordinary_once":true,"old_candidate_wins_equal_saved_upper":true,"old_global_phase_budget_not_replaced_by_cut_phase_lower":true,"old_scientific_calls":0,"old_targets_recomputed":0,"ordinary_phase_ratios_divide_same_actual_positive_function_before_norms":true,"original_L2_pullback_is_distinct_complete_operator_budget":true,"original_PW_cut":"2333968743003/10000000000000","original_inverse_first_derivative_is_pointwise_complete_budget":true,"original_local_patch_and_all_physical_mean_costs_read_only":true,"original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","profile_zero_order_copied_independently_not_reexpanded":true,"same_normalized_circle_measure_for_three_comparison_coordinates":true,"same_ordered_IJ_and_original_negative_windows":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"],"whole_and_reduced_compared_only_to_their_own_complete_old_candidates":true},"same_full_mean_Bessel_circle":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_same_whole_receiver_conclusion":{"complete":true,"kind":"complete_new_same_whole_receiver_conclusion_v1","new_records":{"complete_all_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_B_union_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_dyadic_contribution_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_retained_and_mean_ordinary_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_retained_mean_and_jumps_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonroot_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_reduced_received_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_retained_five_thirds_profile_upper":{"ball":"__FINITE_SCALAR__"},"complete_retained_two_profile_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_negative_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_reduced_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_whole_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_dyadic_contribution_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_retained_and_mean_ordinary_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_retained_mean_and_jumps_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_whole_received_source_upper":{"ball":"__FINITE_SCALAR__"},"strict_B_c_upper":{"ball":"__FINITE_SCALAR__"},"strict_B_t_upper":{"ball":"__FINITE_SCALAR__"}},"ordinary_physical_angular_derivatives":true,"original_complete_profile_and_N6_immutable":true,"retained_scope":{"Theta_nu_radial_head_finite_factors_and_both_means_retained":true,"actual_complete_even_mean_zero_projection_before_same_parity_J":true,"all_actual_96_physical_columns_and_still_uncomputed_signed_normalization_separate":true,"all_fifteen_weight_entries_preserved":true,"all_near_and_two_far_genuine_profiles_retained":true,"all_positive_root_four_waist_ends_and_ordered_readout_retained":true,"comparison_matrix_is_auxiliary_H2_seminorm_space_not_physical_state":true,"complete_retained_v1_plus_n_inverse_v2_is_read_only":true,"entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction":true,"fixed_intrinsic_parameter":"eta_0","full_Bessel_spaces_include_mean_and_all_zero_low_high_output_modes":true,"full_signed_inputs_then_original_isometric_reflection_restriction":true,"new_exp_log_ODE_quadrature":0,"new_local_mean_jump_endpoint_targets":0,"no_radial_length_factor_on_jumps":true,"no_smallness_or_actual_finite_inverse_claimed":true,"normalized_profile_coefficients_to_ordinary_once":true,"old_candidate_wins_equal_saved_upper":true,"old_global_phase_budget_not_replaced_by_cut_phase_lower":true,"old_scientific_calls":0,"old_targets_recomputed":0,"ordinary_phase_ratios_divide_same_actual_positive_function_before_norms":true,"original_L2_pullback_is_distinct_complete_operator_budget":true,"original_PW_cut":"2333968743003/10000000000000","original_inverse_first_derivative_is_pointwise_complete_budget":true,"original_local_patch_and_all_physical_mean_costs_read_only":true,"original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","profile_zero_order_copied_independently_not_reexpanded":true,"same_normalized_circle_measure_for_three_comparison_coordinates":true,"same_ordered_IJ_and_original_negative_windows":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"],"whole_and_reduced_compared_only_to_their_own_complete_old_candidates":true},"same_full_mean_Bessel_circle":true,"strict_interval":["0","76285779072683/320000000000000"]}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_new_full_output_profile_weights_conclusion":15,"complete_new_relative_phase_pullback_conclusion":7,"complete_new_same_whole_receiver_conclusion":18}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_new_full_output_profile_weights_conclusion":15,"complete_new_relative_phase_pullback_conclusion":7,"complete_new_same_whole_receiver_conclusion":18}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":5,"new_exponentials_saved":0,"new_fractional_powers":2,"new_graphs_completed":3,"new_logarithms":0,"new_quadratures":0,"new_records_saved":40,"new_square_roots":1,"new_whole_comparisons_completed":2,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":9,"original_record_objects_copied":44,"original_records_copied_in_graphs":0}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","current_input_and_AST_identity","all_five_complete_original_files_byte_identical","complete_WJR_relative_phase_receipt","complete_WSM_profile_N6_receiver_same_binding","complete_original_scopes_and_failed_ancestry_retained","all_44_scalar_and_nine_qualification_copies_retained","same_measure_full_mean_original_phase_budgets_and_parity_window","complete_relative_inverse_phase_and_pullbacks","complete_fifteen_full_output_profile_weights","complete_same_whole_and_reduced_receiver","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","copied_original_scalar_records","copied_original_scopes","complete_new_graphs","whole_candidate_choices","current_target","completed_targets","saved_record_counts","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized"]''')
OLD_WJR_GRAPH_NAMES = json.loads(r'''["complete_new_relative_Jacobian_conclusion","complete_new_positive_phase_average_ratio_conclusion","complete_new_relative_bulk_transport_conclusion","complete_new_relative_omega_conclusion"]''')
OLD_WSM_NODE_NAMES = json.loads(r'''["strict_complete_angular_profile","strict_complete_ordered_N6","strict_complete_whole_receiver"]''')
OLD_WSM_NODE_ROLES = json.loads(r'''["wsm_profile","wsm_N6","wsm_receiver"]''')
OLD_WSM_NEW_COUNTS = json.loads(r'''[32,89,31]''')
OLD_WSM_COPY_COUNTS = json.loads(r'''[6,1,32]''')
OLD_WSM_OPERATOR_WORDS = json.loads(r'''["D0_squared","eta_squared_K_dphi_squared","minus_B_D0","minus_tQ_D0","minus_RQ_J_D0","plus_tQ_B","plus_RQ_J_B","minus_B_radial","plus_Dcal_commutator_B","minus_K_VAC"]''')

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
        "kind": "complete_original_WJR_and_WSM_readonly_admission_for_WRP_v1",
        "complete": True,
        "complete_original_file_receipts": [
            copy.deepcopy(files[spec["role"]]) for spec in EXPECTED_OLD_FILES],
        "complete_original_schema_fields": {
            role: sorted(old) for role, old in docs.items()},
        "complete_original_qualification_identities": {
            role: {"bytes": len(canonical(original_qualifications(old))),
                   "sha256": digest(canonical(original_qualifications(old)))}
            for role, old in docs.items()},
        "complete_WJR_process_binding": {
            key: copy.deepcopy(docs["wjr_actual"][key]) for key in PROCESS_RECEIPT_KEYS},
        "complete_WSM_process_binding": {
            key: copy.deepcopy(docs["wsm_index"][key]) for key in PROCESS_RECEIPT_KEYS},
        "complete_WSM_bound_graph_files":
            copy.deepcopy(docs["wsm_index"]["scientific_graph_files"]),
        "complete_WSM_original_ancestry_reference": {
            "source_role": "wsm_index", "json_path": ["accepted_old_inputs"],
            "copied_scope_alias": "complete_WSM_original_input_qualification_references"},
        "complete_WJR_original_ancestry_reference": {
            "source_role": "wjr_actual", "json_path": ["accepted_old_inputs"],
            "complete_original_file_sha256": files["wjr_actual"]["sha256"]},
        "complete_WJR_15_gates_56_targets_and_WSM_22_gates_152_targets_verified": True,
        "exact_original_global_phase_budget_copies_and_normalized_profile_tables_verified": True,
        "all_original_source_records_and_consumed_qualification_objects_copied": True,
        "all_full_original_non_ball_leaves_verified_by_canonical_projection": True,
        "original_operation_and_recursive_ancestry_not_duplicated_but_full_byte_bound": True,
        "original_failed_ancestors_not_relabelled_success": True,
        "old_scientific_calls": 0, "old_targets_recomputed": 0,
        "old_producer_imports_or_calls": 0, "history_inputs_restored": 0}

def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(digest(manifest_raw) == manifest_sha, "manifest CLI identity")
    manifest = exact_json(manifest_raw)
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_WRP", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 9
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 9,
            "nine complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "original input pin differs")
    require(same_json(files["proof_WRP"], EXPECTED_PROOF), "published WRP pin")
    require(files["science"]["path"] == SOURCE_PATH
            and files["worker"]["path"] == WORKER_PATH, "new entry paths")
    raw = {spec["role"]: check_file(root, spec) for spec in specs}
    require(Path(__file__).resolve() == safe_path(root, SOURCE_PATH)
            and Path(__file__).read_bytes() == raw["science"], "actual entry bytes")
    module_map = {"science": files["science"]["sha256"]}
    require(same_json(manifest["scientific_modules"], [files["science"]])
            and same_json(manifest["parameters"], PARAMETERS),
            "single new module and parameters")
    op = manifest["operation"]
    require(op["kind"] == KIND and op["problem_id"] == PROBLEM_ID
            and same_json(op["parameters"], PARAMETERS)
            and same_json(op["ordered_targets"], ORDERED_GRAPH_NAMES)
            and same_json(op["scientific_module_binding"], module_map)
            and op["bits_parameter"] == "arithmetic_bits", "operation profile differs")
    for role in ("science", "worker"):
        ast.parse(raw[role].decode("utf-8"), filename=files[role]["path"])
    docs = {spec["role"]: exact_json(raw[spec["role"]]) for spec in EXPECTED_OLD_FILES}
    for role, old in docs.items():
        require(sorted(old) == OLD_FIELDSETS[role] and canonical(old) == raw[role],
                "complete original JSON schema or spelling differs")
        body = canonical(original_qualifications(old))
        expected = OLD_QUALIFICATION_IDENTITIES[role]
        require(len(body) == expected["bytes"] and digest(body) == expected["sha256"],
                "all original non-ball fields and array positions differ")
    prior, index = docs["wjr_actual"], docs["wsm_index"]
    for old, gate_count in ((prior, 15), (index, 22)):
        require(old["complete"] is True and old["proved"] is True
                and old["actual_returncode"] == 0 and old["failure"] is None
                and old["current_target"] is None and old["stage"] == "complete"
                and old["arithmetic_bits"] == 320
                and old["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"}
                and old["automatic_retry_authorized"] is False
                and len(old["gates"]) == gate_count
                and all(set(g) == {"name", "passed"} and g["passed"] is True
                        for g in old["gates"]), "complete original public result")
        require(old["parameters"]["selected_original_real_member_only"] is True
                and old["parameters"]["fixed_intrinsic_parameter"] == "eta_0"
                and old["parameters"]["strict_interval"] == PARAMETERS["strict_interval"]
                and old["parameters"]["root_interval"] == PARAMETERS["root_interval"]
                and old["parameters"]["physical_period"] == "pi/2"
                and old["parameters"]["original_true_interfaces"] == 3070
                and old["parameters"]["physical_mean_coordinates"] == 2,
                "same selected real member, full original domains and physical means")
    require(prior["kind"] == "complete_relative_flow_Jacobian_and_positive_phase_ratio_bounds"
            and prior["run_id"] == "43873739440" and prior["run_attempt"] == "1"
            and prior["completed_targets"] == OLD_WJR_GRAPH_NAMES
            and set(prior["complete_new_graphs"]) == set(OLD_WJR_GRAPH_NAMES)
            and all(prior["saved_record_counts"][name] == 14
                    and prior["complete_new_graphs"][name]["complete"] is True
                    and scalar_record_count(prior["complete_new_graphs"][name]) == 14
                    for name in OLD_WJR_GRAPH_NAMES)
            and prior["actual_progress"]["new_records_saved"] == 56
            and prior["actual_progress"]["old_targets_recomputed"] == 0,
            "all four complete relative-Jacobian graphs and fifty-six old targets")
    phase = prior["complete_new_graphs"]["complete_new_positive_phase_average_ratio_conclusion"]
    require(phase["ordinary_physical_angular_derivatives"] is True
            and phase["actual_positive_Jacobian_divided_before_norms"] is True
            and phase["common_positive_phase_average_ratio"] is True
            and phase["relative_ratio"] is True
            and phase["complete_original_cut_and_all_shorter_flow"] is True
            and phase["maximum_angular_order"] == 14
            and len(phase["new_records"][
                "ordinary_common_positive_phase_and_average_ratios_1_through_14"]) == 14,
            "same actual positive phases and positive average, ordinary ratios")
    require(index["kind"] == "complete_strict_scaled_mixed_profile_and_same_whole_error_v1"
            and index["run_id"] == "43877268949" and index["run_attempt"] == "1"
            and index["completed_targets"] == OLD_WSM_NODE_NAMES
            and index["partial_target_reference"] is None
            and index["actual_progress"]["new_records_saved"] == 152
            and index["actual_progress"]["original_records_copied_in_graphs"] == 39
            and index["actual_progress"]["old_targets_recomputed"] == 0
            and index["actual_progress"]["old_producer_imports_or_calls"] == 0
            and index["accepted_old_inputs"]["only_existing_complete_nodes_of_failed_parent_reused"] is True,
            "complete WSM three-node receipt and original failed ancestry retained")
    original_refs = index["verified_original_inputs"]
    relative = dict(files["wjr_actual"], role="relative_angular")
    require(relative in original_refs
            and same_json(index["relative_angular_packet_identity"], relative),
            "WSM consumes this exact complete WJR receipt")
    refs_by_role = {p["role"]: p for p in original_refs}
    node_refs, prior_deps = [], {}
    for position, role in enumerate(OLD_WSM_NODE_ROLES):
        node = docs[role]
        name = OLD_WSM_NODE_NAMES[position]
        new_count, copy_count = OLD_WSM_NEW_COUNTS[position], OLD_WSM_COPY_COUNTS[position]
        conclusion, binding = node["conclusion"], node["binding"]
        require(node["kind"] == "WSM_complete_atomic_node_v1"
                and node["node_name"] == name and conclusion["node_name"] == name
                and node["complete"] is True and conclusion["complete"] is True
                and node["failure"] is None and node["automatic_retry_authorized"] is False
                and node["all_printed_records_in_complete_conclusion"] is True
                and node["printed_record_event_count"] == new_count
                and scalar_record_count(conclusion["new_records"]) == new_count
                and scalar_record_count(conclusion["copied_original_records"]) == copy_count
                and index["saved_record_counts"][name] == new_count
                and index["original_record_copy_counts"][name] == copy_count,
                "complete original node, actual new prefix and original copies")
        for key in ("run_id", "run_attempt", "workflow_event_commit",
                    "actual_checkout_commit", "scientific_modules", "manifest_sha256"):
            require(same_json(binding[key], index[key]), "node process binding differs")
        require(binding["parameters_sha256"] == digest(canonical(index["parameters"]))
                and len(binding["input_sha256"]) == 12
                and all(value == index["input_sha256"][key]
                        and value == refs_by_role[key]["sha256"]
                        for key, value in binding["input_sha256"].items())
                and same_json(binding["direct_saved_dependencies"], prior_deps)
                and same_json(conclusion["retained_scope"], index["retained_scope"]),
                "complete node input, parameter and dependency binding")
        if position < 2:
            require(same_json(conclusion["relative_angular_predecessor_identity"], relative),
                    "complete profile and N6 relative-map identity")
        filename = "graphs/" + name + ".json"
        ref = {"bytes": files[role]["bytes"], "path": filename,
               "sha256": files[role]["sha256"]}
        node_refs.append(ref)
        prior_deps[name] = {"bytes": ref["bytes"], "file": filename,
                            "sha256": ref["sha256"]}
    require(same_json(node_refs, index["scientific_graph_files"]),
            "complete three actual graph file identities")
    profile, n6, receiver = (docs[role]["conclusion"] for role in OLD_WSM_NODE_ROLES)
    table = profile["complete_jet_tables"]["complete_profile"]
    require(table["shape"] == [4, 0] and table["indices"] == [[0,j] for j in range(5)]
            and table["basis"] == "t0^p times ordinary derivative divided by p! q!; frozen actual t0"
            and table["relative_unit"] is False and table["value_omitted_for_lift"] is False
            and table["exact_zero_indices"] == []
            and table["bounds"][0] == {"copied_record_name": "complete_profile_p0_q0"}
            and table["bounds"][1:] == [
                {"record_path": ["jets", "complete_profile", "p0_q" + str(j)]}
                for j in range(1,5)], "complete normalized profile, zeroth independent")
    for key in ("all_signed_input_modes_and_all_zero_low_high_outputs",
                "two_true_far_phases_and_near_partition_retained",
                "every_near_and_far_positive_algorithm_summand_retained",
                "oldwhole0_not_compared_to_reread_near0_plus_two_far0",
                "only_original_normalized_reflection_restriction_is_isometric",
                "profile_weights_include_no_extra_terminal_or_mean_factor_two"):
        require(profile["qualifications"][key] is True, "full profile receiver scope")
    require(n6["complete_final_even_mean_zero_projection_before_same_J"] is True
            and n6["all_complete_operator_words_and_terminals_retained"] is True
            and n6["complete_genuine_potential_in_full_transport_cancellation"] is True
            and n6["complete_operator_term_order"] == OLD_WSM_OPERATOR_WORDS
            and n6["retained_inverse_powers"] == [1,2,3,4,5]
            and n6["exactly_cancelled_inverse_powers"] == [-2,-1,0]
            and n6["terminal_inverse_power_before_input"] == 4
            and n6["terminal_column_power_after_input"] == [-17,6],
            "complete ordered N6, all means, actual projection and exact terminal")
    require(receiver["input_order"] == [-4,3]
            and receiver["whole_candidate_operator"] == PARAMETERS["same_operator_domain"]
            and receiver["same_complete_genuine_trial"] is True
            and receiver["full_finite_factors_mean_rows_Theta_nu_and_radial_head_retained"] is True
            and receiver["entire_local_patch_and_current_local_receiver_fees_read_only"] is True
            and receiver["old_complete_remaining_tuple_not_recomputed"] is True
            and receiver["Calg_only_in_whole_Dinfinity_only_in_reduced"] is True
            and receiver["no_jump_length_factor"] is True
            and receiver["ordinary_dr_lengths_only_on_ordinary_sources"] is True
            and receiver["original_PW_cut"] == PARAMETERS["original_PW_cut"]
            and receiver["original_true_interfaces"] == 3070
            and receiver["physical_mean_coordinates"] == 2
            and receiver["finite_signed_inverse_or_smallness_claimed"] is False
            and same_json(receiver["whole_candidate_choices"], index["whole_candidate_choices"]),
            "same whole operator, actual means, jumps, four ends and independent finite parts")
    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 44 and all(
                isinstance(v, dict) and set(v) == {"ball"} and isinstance(v["ball"], str)
                for v in records.values())
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all forty-four complete original scalar objects")
    for which in ("whole", "reduced"):
        choice = receiver["whole_candidate_choices"][which]
        require(choice["both_complete_candidates_retained"] is True
                and choice["prior_wins_equal_saved_upper"] is True
                and RECORD_SPECS["prior_" + which]["path"] ==
                    ["conclusion"] + choice["selected_record_path"]
                and same_json(records["prior_" + which],
                              at(receiver, choice["selected_record_path"])),
                "exact same-operator current complete old selection")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(spec["mode"] in ("exact", "qualifications"), "scope mode")
        scopes[name] = (copy.deepcopy(value) if spec["mode"] == "exact"
                        else original_qualifications(value))
    require(len(scopes) == 9 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "nine complete consumed scope objects with every non-ball leaf")
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


"""WRP forty-target finite mathematical fragment; no entry, I/O or old calls.

The eventual owner supplies ex (exact integers), require, norm_upper,
saved_upper, graph_record, and emit. emit persists the complete prefix,
prints it, parses it back, and returns the exact saved {ball} record.
Only that returned record supplies each new downstream upper endpoint.

A complete successful WSM index and all three complete node files, plus
the complete WJR actual, must be admitted before these functions are called.
No prospective actual pin or successful status is supplied by this fragment.
"""

def complete_relative_inverse_pullbacks(saved, graphs, emit):
    U = saved_upper(saved["inverse_phase_derivative_1"])
    K0 = saved_upper(saved["phase_pullback_L2"])
    sqrt_two = saved_upper(saved["sqrt_two_upper"])
    P1 = saved_upper(saved["relative_positive_phase_1"])
    P2 = saved_upper(saved["relative_positive_phase_2"])
    P3 = saved_upper(saved["relative_positive_phase_3"])
    require(U > 0 and K0 > 0, "positive admitted original complete phase budgets")

    emit("inverse_phase_derivative_2_upper", P1 * U**2)
    emit("inverse_phase_derivative_3_upper", (P2 + ex(3)*P1**2) * U**3)
    emit("inverse_phase_derivative_4_upper",
         (P3 + ex(10)*P1*P2 + ex(15)*P1**3) * U**4)

    # One complete nonnegative matrix on the SAME H2 seminorm space.
    # sqrt(2)/2 is an upper for 1/sqrt(2); no saved upper is inverted.
    aa = sqrt_two * P1 * U
    bb = (ex(3)*P1**2 + P2) * U**2
    cc = ex(3) * P1 * U**2 * sqrt_two / ex(2)
    dd = U**2
    row = saved_upper(emit("complete_row_sum_upper",
        max(norm_upper(v) for v in (ex(1), aa+U, bb+cc+dd))))
    column = saved_upper(emit("complete_column_sum_upper",
        max(norm_upper(v) for v in (ex(1)+aa+bb, U+cc, dd))))
    K2 = saved_upper(emit("complete_phase_pullback_Hminus2_upper",
                          K0 * (row*column).sqrt()))
    # Exactly two new positive fractional powers, both on directed uppers.
    # The old L2 bound itself is read, never regenerated from a lower.
    require(K2 > 0, "complete positive same-operator Hminus2 budget")
    emit("complete_phase_pullback_Hminus5_3_upper",
         K0**(ex(1)/ex(6)) * K2**(ex(5)/ex(6)))


def complete_full_output_profile_weights(saved, graphs, emit):
    name = "complete_new_relative_phase_pullback_conclusion"
    U = saved_upper(saved["inverse_phase_derivative_1"])
    inverse = {1: U}
    for j in (2, 3, 4):
        inverse[j] = graph_record(graphs, name,
            ["inverse_phase_derivative_" + str(j) + "_upper"])
    K0 = saved_upper(saved["phase_pullback_L2"])
    K2 = graph_record(graphs, name, ["complete_phase_pullback_Hminus2_upper"])
    K53 = graph_record(graphs, name, ["complete_phase_pullback_Hminus5_3_upper"])
    two16 = saved_upper(saved["two_one_sixth_upper"])
    factorials = (1, 1, 2, 6, 24)
    profile = [norm_upper(ex(factorials[j]) *
                 saved_upper(saved["profile_normalized_" + str(j)]))
               for j in range(5)]
    # Complete ordinary B_(4,j); no individual phase or mean is removed.
    bell = {
        1: inverse[4],
        2: ex(4)*U*inverse[3] + ex(3)*inverse[2]**2,
        3: ex(6)*U**2*inverse[2],
        4: U**4,
    }
    binomial_rows = ((1,), (1,1), (1,2,1), (1,3,3,1), (1,4,6,4,1))
    windows = (
        ("zero", K0, ex(1)),
        ("five_thirds", K53, norm_upper(two16**5)),
        ("two", K2, ex(2)),
    )
    for window, Kd, prefactor in windows:
        for b in range(5):
            complete = profile[0] if b == 0 else ex(0)
            for j in range(max(1,b), 5):
                complete += (ex(17)/ex(64) * bell[j]
                             * ex(binomial_rows[j][b]) * profile[j-b])
            emit([window, "angle_" + str(b)], prefactor * Kd * complete)


def complete_same_whole_receiver(saved, graphs, emit):
    weights = "complete_new_full_output_profile_weights_conclusion"
    amplitudes = [saved_upper(saved["retained_amplitude_angle_" + str(b)])
                  for b in range(5)]
    Q = {}
    for window in ("five_thirds", "two"):
        value = ex(0)
        for b in range(5):
            value += graph_record(graphs, weights,
                                  [window, "angle_" + str(b)]) * amplitudes[b]
        Q[window] = saved_upper(emit(
            "complete_retained_" + window + "_profile_upper", value))

    two16 = saved_upper(saved["two_one_sixth_upper"])
    Bc = saved_upper(emit("strict_B_c_upper",
        two16 * saved_upper(saved["strict_Jminus5_3"]) * Q["five_thirds"]))
    Bt = saved_upper(emit("strict_B_t_upper",
        two16 * saved_upper(saved["strict_IJminus2"]) * Q["two"]))
    Bu = saved_upper(emit("complete_collar_B_union_upper",
        max(Bc, saved_upper(saved["local_B_c_upper"]))))

    collar = saved_upper(emit(
        "complete_collar_retained_and_mean_ordinary_upper",
        saved_upper(saved["sqrt_two_upper"])
        * saved_upper(saved["ell_plus_one_fourth_upper"]) * Bu
        + saved_upper(saved["sqrt_ell_plus_upper"])
        * saved_upper(saved["collar_raw_mean"])
        * saved_upper(saved["N_minus5_3_upper"])))
    strict = saved_upper(emit(
        "complete_strict_retained_and_mean_ordinary_upper",
        (ex(2333968743003)/ex(10000000000000))
        * (saved_upper(saved["ell_minus_negative_fourth_upper"]) * Bt
           + saved_upper(saved["strict_primitive_mean"])
           * saved_upper(saved["N_minus4_3_upper"]))))
    Rc = saved_upper(emit(
        "complete_collar_retained_mean_and_jumps_received_upper",
        saved_upper(saved["C_O"])*collar
        + saved_upper(saved["C_R"])*saved_upper(saved["jump_collar"])))
    Rt = saved_upper(emit(
        "complete_strict_retained_mean_and_jumps_received_upper",
        saved_upper(saved["C_1"])*(strict+saved_upper(saved["jump_strict"]))))
    Nc = saved_upper(emit("complete_collar_dyadic_contribution_upper",
                          Rc*saved_upper(saved["dyadic_one_third"])))
    Nt = saved_upper(emit("complete_strict_dyadic_contribution_upper",
                          Rt*saved_upper(saved["dyadic_two_thirds"])))
    negative = saved_upper(emit("complete_same_negative_error_upper",
        saved_upper(saved["Bessel_prefactor"])
        * (Nc+Nt+saved_upper(saved["complete_terminal_dyadic_contribution_upper"]))))

    nonroot = saved_upper(emit("complete_nonroot_source_sum_upper",
        saved_upper(saved["Rplus"])+negative+saved_upper(saved["waist_endpoint"])))
    allsource = saved_upper(emit("complete_all_source_sum_upper",
                                 nonroot+saved_upper(saved["RF"])))
    whole_received = saved_upper(emit("complete_whole_received_source_upper",
        saved_upper(saved["Lrec"])*allsource))
    emit("complete_same_whole_error_upper",
         saved_upper(saved["Calg"])+whole_received)
    reduced_received = saved_upper(emit("complete_reduced_received_source_upper",
        saved_upper(saved["Lrec"])*nonroot))
    emit("complete_same_reduced_error_upper",
         saved_upper(saved["D_infinity"])+reduced_received)

# Selection is an owner operation after the COMPLETE third graph is saved.
# Compare each complete new whole/reduced record only with its own complete
# old selected candidate; preserve both, and let the old record win a tie.
# This module declares no new local, terminal, mean, jump or endpoint target.

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
            if name == ORDERED_GRAPH_NAMES[0] and path == ["complete_phase_pullback_Hminus2_upper"]:
                doc["actual_progress"]["new_square_roots"] += 1
            if name == ORDERED_GRAPH_NAMES[0] and path == ["complete_phase_pullback_Hminus5_3_upper"]:
                doc["actual_progress"]["new_fractional_powers"] += 2
            doc["stage"] = "record_saved:" + name
            restored = publish()
            return copy.deepcopy(at(restored["complete_new_graphs"][name]["new_records"], path))
        return emit

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
        doc["actual_progress"]["complete_original_files_admitted"] = 5
        doc["actual_progress"]["original_record_objects_copied"] = 44
        doc["actual_progress"]["original_qualification_objects_copied"] = 9
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
        require(saved_upper(saved["inverse_phase_derivative_1"]) > 0
                and saved_upper(saved["phase_pullback_L2"]) > 0,
                "positive original full-domain pointwise and L2 phase budgets")
        gate(GATE_LABELS[7])
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        operations = (
            ("complete_new_relative_phase_pullback_conclusion", complete_relative_inverse_pullbacks),
            ("complete_new_full_output_profile_weights_conclusion", complete_full_output_profile_weights),
            ("complete_new_same_whole_receiver_conclusion", complete_same_whole_receiver))
        require([name for name, _ in operations] == ORDERED_GRAPH_NAMES, "complete new graph order")
        for name, function in operations:
            emit = start_graph(name)
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
                "prior_source_role": "wsm_receiver",
                "prior_source_record_path": copy.deepcopy(RECORD_SPECS["prior_" + which]["path"]),
                "prior_record_path": prior_path, "new_record_path": new_path,
                "selected_label": ("new_complete_relative_phase_pullback_candidate"
                                   if use_new else "prior_selected_complete_candidate"),
                "selected_record_path": new_path if use_new else prior_path,
                "complete_selected_upper": copy.deepcopy(new_record if use_new else old_record)}
            doc["actual_progress"]["new_whole_comparisons_completed"] += 1
            doc["stage"] = "complete_same_" + which + "_choice_saved"
            publish()
        gate(GATE_LABELS[11])
        for role, spec in work["files"].items():
            require(check_file(work["root"], spec) == work["raw"][role],
                    "current input changed during new scalar work")
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "manifest changed during new scalar work")
        gate(GATE_LABELS[12])
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
        gate(GATE_LABELS[13])
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
