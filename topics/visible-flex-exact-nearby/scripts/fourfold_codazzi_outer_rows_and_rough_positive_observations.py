"""WOB: complete outer rows and same-column rough positive observation bounds."""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
import os
import re
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

PUBLIC_REPOSITORY = json.loads(r'''"Rogerhu12/math-research-public"''')
KIND = json.loads(r'''"complete_outer_rows_and_rough_positive_observation_bounds_v1"''')
PROBLEM_ID = json.loads(r'''"selected_WOB_complete_outer_source_and_root_rows_v1"''')
TOPIC = json.loads(r'''"topics/visible-flex-exact-nearby"''')
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_outer_rows_and_rough_positive_observations.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py"''')
PREFLIGHT_KIND = json.loads(r'''"complete_outer_rows_and_rough_positive_observation_bounds_readonly_preflight"''')
PARAMETERS = json.loads(r'''{"actual_pR_upper":"1/5","arithmetic_bits":320,"copied_original_records":42,"decimal_record_digits":75,"exact_original_contour_shift":"1/512","exact_real_delta_radius":"1/100000000","exact_trial_cutoff_support_length":"3/1000000","first_high_abs_j":97,"fixed_intrinsic_parameter":"eta_0","head_dimension":193,"historical_inputs":0,"last_low_abs_j":96,"new_complete_graphs":6,"new_exponentials":1,"new_fractional_powers":1,"new_saved_records":37,"new_square_roots":7,"normalized_angular_measure":true,"old_scientific_target_recomputations_allowed":0,"original_frozen_common_input":"Xfr = S_star D_plus H_nat^(-4/3)","original_outer_high_and_low_window":"H^-5/6","original_raw_state_window":"ordinary L2_dr H^-1","original_rough_stable_window":"H^-3/2","original_same_negative_source_window":"ordinary L2_dr H^-2/3 with independent mean","physical_frequency":"n=4|j|","physical_period":"pi/2","same_selected_member_only":true}''')
RETAINED_SCOPE = json.loads(r'''{"CF288_whole_common_factor_no_upper_division_or_subtraction":true,"Ni_and_stable_inverse_in_original_right_order_once":true,"PW_receiver_applied_only_to_zero_stable_additional_state":true,"WSP_complete_RH_source_not_received_positive_bound":true,"actual_outer_y_coordinate_not_identified_with_raw_endpoint":true,"all_new_targets_are_complete_positive_bounds_in_original_units":true,"all_six_complete_original_receipts_read_without_old_math":true,"complete_original_37_records_plus_five_typed_factors_retained":true,"finite_signed_inverse_proved":false,"full_actual_pR_upper_from_exact_same_family_body":true,"full_incoming_inverse_proved":false,"full_low193_rows_and_independent_even_mean_retained":true,"full_source_jump_root_mean_and_cokernel_rows_retained":true,"independent_physical_coordinates_receive_no_Ni":true,"mean_and_amplitude_rows_not_claimed_zero":true,"new_whole_comparisons":0,"nonlinear_background_or_surface_proved":false,"old_whole_bounds_not_subtracted":true,"original_C_P_C_K_A_infty_L_star_C_V0_C_R0_read_verbatim":true,"original_WHVA_4096_strict_sufficient_test_false":true,"original_WHVA_no_resolvent_admitted":true,"original_sqrt_two_target_read_not_recomputed":true,"same_selected_member_same_physical_eta0":true,"true_physical96_Theta_nu_and_radial_head_retained":true,"unknown_G_and_Btarget_inverse_not_given_numbers":true}''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","parameters","retained_scope","complete","proved","failure","stage","actual_returncode","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","manifest_sha256","scientific_modules","input_sha256","verified_original_inputs","original_source_AST_evidence","accepted_old_inputs","copied_original_scalar_records","copied_original_scopes","complete_new_graphs","gates","completed_targets","current_target","actual_progress","saved_record_counts","runtime","actual_mathematical_wall_seconds","automatic_retry_authorized","remaining_unknown_factors"]''')
GATE_LABELS = json.loads(r'''["complete_current_hashes","complete_two_source_ASTs","six_complete_original_scientific_receipts","forty_two_original_records_exact","complete_declared_original_qualification_projection","same_selected_member_and_original_trial","actual_full_family_pR_and_low_window","WHVA_failed_sufficient_gate_kept","NIF_and_PW_ordered_units","complete_outer_low_and_affine_rows","complete_positive_head_and_outer_columns","complete_genuine_288_shell","complete_genuine_and_rough_observations","complete_zero_IVP_rows","complete_zero_stable_root_receiver_rows","thirty_seven_new_records_complete","zero_old_scientific_calls","all_physical_scope_retained"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_genuine_288_shell":{"all_input_frequencies_and_both_carriers_retained":true,"both_complete_candidates_saved":true,"common_contour_factor_removed_by_exact_source_formula_not_upper_division":true,"complete":true,"complete_new_records":{"complete_shell_crude_candidate_upper":{"ball":"__FINITE_SCALAR__"},"complete_shell_reconstructed_candidate_upper":{"ball":"__FINITE_SCALAR__"},"complete_shell_selected_old_candidate_upper":{"ball":"__FINITE_SCALAR__"},"new_complete_shell_exponential_factor_upper":{"ball":"__FINITE_SCALAR__"}},"full_output_mean_retained":true,"kind":"complete_genuine_288_shell_v1","old_exponentials_recomputed":0,"original_cutoff_and_trial_unchanged":true,"original_whole_candidate_choice_not_recomputed":true,"proof_formulas":"WOB.13-WOB.14"},"complete_genuine_and_rough_observations":{"Cplus_SP_is_full_RH_source_not_received_positive_fee":true,"Kpos_not_multiplied":true,"Ni_at_complete_right_end_once":true,"common_domain_and_distributional_inverse_qualification_preserved":true,"complete":true,"complete_new_records":{"complete_Phi_upper":{"ball":"__FINITE_SCALAR__"},"complete_Upsilon_upper":{"ball":"__FINITE_SCALAR__"},"complete_correction_head_source_term_upper":{"ball":"__FINITE_SCALAR__"},"complete_cutoff_radial_measure_factor_upper":{"ball":"__FINITE_SCALAR__"},"complete_rough_head_observation_upper":{"ball":"__FINITE_SCALAR__"},"complete_rough_outer_observation_upper":{"ball":"__FINITE_SCALAR__"},"complete_trial_head_source_term_upper":{"ball":"__FINITE_SCALAR__"}},"kind":"complete_genuine_and_rough_observations_v1","no_rough_root_trace_passed_to_PW":true,"original_R_F_and_two_physical_means_independent":true,"proof_formulas":"WOB.15-WOB.16"},"complete_outer_low_and_affine_rows":{"actual_pR_upper_from_full_family_body":"1/5","all_affine_source_columns_retained":true,"complete":true,"complete_new_records":{"affine_fB_Robin_row_upper":{"ball":"__FINITE_SCALAR__"},"complete_affine_fB_low_pair_upper":{"ball":"__FINITE_SCALAR__"},"complete_affine_rB_low_pair_upper":{"ball":"__FINITE_SCALAR__"},"complete_affine_rC_low_pair_upper":{"ball":"__FINITE_SCALAR__"},"complete_high_outer_row_upper":{"ball":"__FINITE_SCALAR__"},"complete_low_outer_row_upper":{"ball":"__FINITE_SCALAR__"},"high_odd_outer_row_upper":{"ball":"__FINITE_SCALAR__"},"low_Hminus5_6_to_L2_weight_upper":{"ball":"__FINITE_SCALAR__"},"low_odd_outer_row_upper":{"ball":"__FINITE_SCALAR__"}},"componentwise_minimum_used":false,"kind":"complete_outer_low_and_affine_rows_v1","mean_in_high_and_low_rows_retained":true,"no_dimension_sqrt_factor":true,"proof_formulas":"WOB.5-WOB.7","whole_affine_two_row_formula":"sqrt((low_weight*(affine_fB_Robin_row*F_B+B_a*norm_rB+C_a*abs_rC))^2+(mu_F*F_B+mu_C*abs_rC)^2)"},"complete_positive_head_and_outer_columns":{"actual_root_stable_input_zero":true,"body_source_choice_read_verbatim":"A_b_from_L","complete":true,"complete_new_records":{"complete_head_outer_trace_upper":{"ball":"__FINITE_SCALAR__"},"complete_head_root_unstable_upper":{"ball":"__FINITE_SCALAR__"},"complete_outer_b_outer_trace_upper":{"ball":"__FINITE_SCALAR__"},"complete_outer_b_raw_state_upper":{"ball":"__FINITE_SCALAR__"},"complete_outer_b_root_unstable_upper":{"ball":"__FINITE_SCALAR__"},"complete_outer_b_to_head_source_upper":{"ball":"__FINITE_SCALAR__"}},"disjoint_original_source_intervals":true,"full_original_seven_input_oracle_retained":true,"kind":"complete_positive_head_and_outer_columns_v1","original_C_P_and_C_K_read_without_recomputation":true,"output_orthogonality_assumed":false,"proof_formulas":"WOB.9-WOB.12","raw_output_window":"whole L2_dr H^-1 with independent mean separate","source_window":"ordinary L2_dr H^-2/3"},"complete_zero_IVP_rows":{"C_V0_C_R0_A_infty_C_K_not_recomputed":true,"C_star_body_norm_read_directly_as_C_R0":true,"WHVA_original_4096_strict_sufficient_gate_passed":false,"actual_ordinary_Volterra_body_and_endpoint_factors_distinct":true,"all_low_jumps_initial_mean_and_cokernel_rows_retained":true,"complete":true,"complete_new_records":{"complete_B0_high_body_row_upper":{"ball":"__FINITE_SCALAR__"},"complete_Bb0_body_row_upper":{"ball":"__FINITE_SCALAR__"},"complete_C0_endpoint_row_upper":{"ball":"__FINITE_SCALAR__"},"complete_D0_high_endpoint_row_upper":{"ball":"__FINITE_SCALAR__"},"complete_Db0_endpoint_row_upper":{"ball":"__FINITE_SCALAR__"}},"head_or_finite_inverse_claimed":false,"kind":"complete_zero_IVP_rows_v1","proof_formulas":"WOB.24-WOB.25","whole_signed_operator_sums_bounded_by_full_positive_sums":true},"complete_zero_stable_root_receiver_rows":{"complete":true,"complete_new_records":{"complete_head_density_waist_receiver_upper":{"ball":"__FINITE_SCALAR__"},"complete_head_primitive_waist_receiver_upper":{"ball":"__FINITE_SCALAR__"},"complete_initial_primitive_waist_receiver_upper":{"ball":"__FINITE_SCALAR__"},"complete_outer_b_density_waist_receiver_upper":{"ball":"__FINITE_SCALAR__"},"complete_outer_b_primitive_waist_receiver_upper":{"ball":"__FINITE_SCALAR__"},"complete_reciprocal_sqrt_two_upper":{"ball":"__FINITE_SCALAR__"}},"complete_root_head_density_receiver_read_as_PW_C_R":true,"full_physical_mean_amplitude_metric_and_other_rows_retained":true,"high_coordinate_right_W_inverse_A_remains_ordered_and_separate":true,"independent_root_and_outer_coordinates_receive_no_Ni_factor":true,"kind":"complete_zero_stable_root_receiver_rows_v1","only_zero_stable_additional_state_uses_PW":true,"original_sqrt_two_read_without_recomputation":true,"proof_formulas":"WOB.23","unknown_B_target_inverse_not_assigned_a_number":true}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_genuine_288_shell":4,"complete_genuine_and_rough_observations":7,"complete_outer_low_and_affine_rows":9,"complete_positive_head_and_outer_columns":6,"complete_zero_IVP_rows":5,"complete_zero_stable_root_receiver_rows":6}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_outer_low_and_affine_rows","complete_positive_head_and_outer_columns","complete_genuine_288_shell","complete_genuine_and_rough_observations","complete_zero_IVP_rows","complete_zero_stable_root_receiver_rows"]''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"new_exponentials_saved":0,"new_finite_inverse_claims":0,"new_finite_matrices_allocated":0,"new_fractional_powers_saved":0,"new_graphs_completed":0,"new_records_saved":0,"new_square_roots_saved":0,"new_whole_comparisons_completed":0,"old_exponentials_recomputed":0,"old_input_binary_restorations":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_body_maxima_recomputed":0,"original_false_sufficient_gate_preserved":false,"original_receipts_admitted":0,"original_record_objects_copied":0}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"new_exponentials_saved":1,"new_finite_inverse_claims":0,"new_finite_matrices_allocated":0,"new_fractional_powers_saved":1,"new_graphs_completed":6,"new_records_saved":37,"new_square_roots_saved":7,"new_whole_comparisons_completed":0,"old_exponentials_recomputed":0,"old_input_binary_restorations":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_body_maxima_recomputed":0,"original_false_sufficient_gate_preserved":true,"original_receipts_admitted":6,"original_record_objects_copied":42}''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":41797,"git_blob_sha":"3abd0f6b7291e0f9318dc035a58a4b6e8dfb851c","path":"topics/visible-flex-exact-nearby/notes/full_delta_negative_one_positive_ci/run-43627228225-1-full-real-delta-negative-one-positive-graph/evidence/full-real-delta-negative-one-positive-graph-summary.json","role":"negative","sha256":"0a3fb8e1be19b9ad82655099da8d5446ac49d92f073e7f6626d08a0626ec4fef"},{"bytes":46253,"git_blob_sha":"c32b8e3f3aca08d338784504c2cce5054d203bc6","path":"topics/visible-flex-exact-nearby/notes/genuine_positive_Ai_cutoff_strong_correction_ci/run-43740173506-1/execution.json","role":"PC","sha256":"75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817"},{"bytes":70207,"git_blob_sha":"421bf05d3274c6f9852670678275cf9e1a0fb1ee","path":"topics/visible-flex-exact-nearby/notes/positive_cutoff_Schur_Parseval_ci/run-43816689251-1/actual-scientific-conclusion.json","role":"WSP","sha256":"5b099f08c18a2b437cb4b78e4a629fae5dc2411a720fd12ad39cf401401d72f2"},{"bytes":12011,"git_blob_sha":"ebe7ae42c2482ce9b20e7af1d41e02f89b920010","path":"topics/visible-flex-exact-nearby/notes/zero_volterra_positive_head_ci/run-43838214094-1/actual-scientific-conclusion.json","role":"WHVA","sha256":"ff5d6e5231e6be66107217d670133b18727dd5b24b81e7566fa884973b29df72"},{"bytes":29829,"git_blob_sha":"7142de95e64d5b3c6df7af705c8b0bf08a5c5c5e","path":"topics/visible-flex-exact-nearby/notes/frozen_common_input_uniform_inverse_constants_ci/run-43795909913-1/actual-scientific-conclusion.json","role":"NIF","sha256":"43294b0cd0fdcffea58a805ecfb3cf06d60136d5ffbb3c8269b3040ce5ea9883"},{"bytes":51030,"git_blob_sha":"5fdb01ed62008489bca34a4b6231519af4f60793","path":"topics/visible-flex-exact-nearby/notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json","role":"WMR","sha256":"39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":41683,"git_blob_sha":"8a55c94d8decc25f33876665119b327eb1d1fd29","path":"topics/visible-flex-exact-nearby/results/R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md","role":"proof_WOB","sha256":"f13024a72e09d9b388fc51eac39d675b656d4d75ee72cdafe449a1c325e92979"}''')
OLD_SCHEMA_RECEIPTS = json.loads(r'''{"NIF":{"canonical_raw_required":true,"complete_gates_sha256":"09d56e23cf57f92c311708b0ad59743a8a20ae06f5680b2733553d0c1cfdaf4a","gate_count":16,"gate_names_sha256":"76c90f0678719f8b4f2aa11825bcb2d9825aa9f73ee0d915d4baef2f93d0dca2","kind":"complete_frozen_common_input_uniform_inverse_constants_v1","manifest_sha256":"138fe8d9d0298126bd4c81691975496db94c2c1d69df31970af4d5b9917fd819","outer_field_count":32,"outer_fields_sha256":"609e4a821965aa55f8194bff7268b4abac00ed65a1e50065fa2387313594b038","runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"scientific_field_count":32,"scientific_fields_sha256":"609e4a821965aa55f8194bff7268b4abac00ed65a1e50065fa2387313594b038","scientific_path":[],"source_identity":"d75ad8a2c76ad1f450cb5a96977c3ec5b8fb6fda69a1185590ba68eeec5e85a2"},"PC":{"canonical_raw_required":false,"complete_gates_sha256":"a678587f44821e6e9873d6f146db7d4fe17f715a7209a0dbf76c028347817e61","gate_count":30,"gate_names_sha256":"c2418a74910f5b7664ab5eb5d9e20a4a5fe8d10caaae50f0c3040a676fd056e0","kind":"actual_genuine_positive_Ai_cutoff_and_strong_correction_v1","manifest_sha256":"13d92e7d2bfb8e3fd57e417676c58d6a649c7f353bcd54fef19af8cc66e123e5","outer_field_count":51,"outer_fields_sha256":"401c19d46af374d53896e210eadc66ffc08f19b0ef2d3ec04f818c8423bb1811","runtime":{"numpy":"2.3.5","python":"3.12.14","python_flint":"0.9.0","scipy":"1.17.0"},"scientific_field_count":54,"scientific_fields_sha256":"ec201c744a63c4319ff9d143cfc69001436ffa30b5d4c9622e983da7a9cc62f5","scientific_path":["actual_scientific_receipt"],"source_identity":"da6864cd790162759d5a78d40a67d0f3b4aa91b60614d947cca1a92371d6940b"},"WHVA":{"canonical_raw_required":true,"complete_gates_sha256":"32f5603775669e6bd1f72bc2ecf82215b194ad3acb11bd2e35093088390cbc01","gate_count":14,"gate_names_sha256":"293619806b036402b6a62d5ecab9bad49e5a9fe6a4d2dfef2bc1fe7921c285d2","kind":"complete_zero_volterra_positive_head_mesh_v1","manifest_sha256":"791e8f2ecfa8ebe23473d8d2e7548eaa25466149f54ead7a124dc1a0eda7d70a","outer_field_count":27,"outer_fields_sha256":"92ea4b677ce7275de1b22c1728ed668e1c18ecf292473ef31b9c7e7754cedb4a","runtime":{"bits":320,"python":"3.12.14","python_flint":"0.9.0"},"scientific_field_count":27,"scientific_fields_sha256":"92ea4b677ce7275de1b22c1728ed668e1c18ecf292473ef31b9c7e7754cedb4a","scientific_path":[],"source_identity":[{"bytes":9632,"git_blob_sha":"437a9f2841dc5b4cdb3a3f55bf9938a2d049f98f","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_zero_volterra_positive_head_mesh.py","role":"science","sha256":"e82c51805d04b28117d38dc60b9ac7fe64d1eb3a867e828b114ab259ef063031"},{"bytes":15718,"git_blob_sha":"f1e2a255863413438cc4985cbad66124514bc4be","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_zero_volterra_positive_head_readonly.py","role":"readonly_admission","sha256":"7cb5c84b09aa51e451103db9a718d0766a748f5be26256e4b61c0041e0dd81f5"}]},"WMR":{"canonical_raw_required":true,"complete_gates_sha256":"f69b4a4e9550a275dfe0ecc2203fe10d7ef5f293d8597b9b69ca2d85e6f8eb36","gate_count":18,"gate_names_sha256":"c476930afdd65cf1d7ed8955c32068958f12b491d9bd2735a6d9fe5ef89b6e83","kind":"complete_positive_weight_physical_mean_and_whole_error_refinement","manifest_sha256":"eccd4b2342dd8ce8d5977d7986e523581597a61664eb72bb755b7f8bcb2a356c","outer_field_count":32,"outer_fields_sha256":"e7ce270c399688a8ba328c0302c03bd757b043e6004fda03d454bdcc147a9c24","runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"scientific_field_count":32,"scientific_fields_sha256":"e7ce270c399688a8ba328c0302c03bd757b043e6004fda03d454bdcc147a9c24","scientific_path":[],"source_identity":{"science":"e8c3ca95c8ed306fa887a910c5b36ec93e25f2bdef7ad67aaebfef4ba88b4ffc"}},"WSP":{"canonical_raw_required":true,"complete_gates_sha256":"83f2e9e8ac4993ddabe8929a249c3081af9d5f3fc4d86096cc89d81f9daac8f6","gate_count":16,"gate_names_sha256":"51f267c22497cee65a36381b0a8ab1b4664af7ca38773659c835b0112c8c7136","kind":"complete_positive_cutoff_Schur_Parseval_and_coefficient_split_v1","manifest_sha256":"11690e1bc7d1770f7c773569fc023efbffa595684db2a5684bd88e7b094cb081","outer_field_count":31,"outer_fields_sha256":"2becddb7c53c32c1e21316b16e1b4651ec180b65f4803e23c968650ccfcb41c5","runtime":{"Python":"3.12.14","python_flint":"0.9.0"},"scientific_field_count":31,"scientific_fields_sha256":"2becddb7c53c32c1e21316b16e1b4651ec180b65f4803e23c968650ccfcb41c5","scientific_path":[],"source_identity":"8c7ab51d386c1551738d56e19ab61d8626171fe8f841f05d0ed93b0a52c3cbe1"},"negative":{"canonical_raw_required":false,"complete_gates_sha256":"9652f18680cdcf56d4fe2a65bf7158c0badae6228d4a84cce1f59043a818b26a","gate_count":18,"gate_names_sha256":"0fe2ed1d8856334705507a287ce0ee3499746bd2b77fe95258f8699c145a8bdd","kind":"actual_full_real_delta_negative_one_positive_given_head_graph_v1","manifest_sha256":null,"outer_field_count":59,"outer_fields_sha256":"3dea9714edfc0ae16729bb68682897dd79d8ec426ae4dced407b12f8fd809809","runtime":null,"scientific_field_count":59,"scientific_fields_sha256":"3dea9714edfc0ae16729bb68682897dd79d8ec426ae4dced407b12f8fd809809","scientific_path":[],"source_identity":"16ffa1a5b3753bc2a70fcf979814b18161df90ae8997510acc8feafac2a88509"}}''')
RECORD_SPECS = json.loads(r'''[{"alias":"T_minus","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","negative_DN_Z_to_d"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"C_minus","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","negative_DN_Z_to_mean"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"U_minus","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","negative_DN_fB_to_d"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"V_minus","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","negative_DN_fB_to_mean"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"I_star","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","nonmean_chart_inverse"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"E_minus","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","raw_Robin_bound"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"B_a","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","independent_Robin_multiplier"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"C_a","endpoint":"upper","path":["actual_complete_negative_order_outer_constants","independent_mean_multiplier"],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"mu_minus","endpoint":"upper","path":["exterior_mean_output_coefficients",0],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"mu_F","endpoint":"upper","path":["exterior_mean_output_coefficients",1],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"mu_C","endpoint":"upper","path":["exterior_mean_output_coefficients",2],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"e_b","endpoint":"upper","path":["exterior_affine_Y_output_coefficients",0],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"e_F","endpoint":"upper","path":["exterior_affine_Y_output_coefficients",1],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"e_R","endpoint":"upper","path":["exterior_affine_Y_output_coefficients",2],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"e_C","endpoint":"upper","path":["exterior_affine_Y_output_coefficients",3],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"C_c","endpoint":"upper","path":["response_rows","entire_positive_raw_L2r_Hminus1",1],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"C_b","endpoint":"upper","path":["response_rows","entire_positive_raw_L2r_Hminus1",2],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"C_B","endpoint":"upper","path":["response_rows","entire_positive_raw_L2r_Hminus1",3],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"Y_c","endpoint":"upper","path":["response_rows","body_Y_sup",1],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"Y_b","endpoint":"upper","path":["response_rows","body_Y_sup",2],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"Y_B","endpoint":"upper","path":["response_rows","body_Y_sup",3],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"U_c","endpoint":"upper","path":["response_rows","full_root_outgoing_unstable_Y_port",1],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"U_b","endpoint":"upper","path":["response_rows","full_root_outgoing_unstable_Y_port",2],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"U_B","endpoint":"upper","path":["response_rows","full_root_outgoing_unstable_Y_port",3],"record_type":"original_ball_lower_upper_object","role":"negative"},{"alias":"CF_crude","endpoint":"upper","path":["actual_scientific_receipt","complete_cutoff_and_head_conclusion","complete_finite_head_crude_upper"],"record_type":"original_ball_object","role":"PC"},{"alias":"CF_reconstructed","endpoint":"upper","path":["actual_scientific_receipt","complete_cutoff_and_head_conclusion","complete_finite_head_reconstructed_upper"],"record_type":"original_ball_object","role":"PC"},{"alias":"CF_selected","endpoint":"upper","path":["actual_scientific_receipt","complete_cutoff_and_head_conclusion","complete_finite_head_at_root_and_body_upper"],"record_type":"original_ball_object","role":"PC"},{"alias":"Cplus_PC","endpoint":"upper","path":["actual_scientific_receipt","complete_strong_correction_conclusion","complete_positive_high_residual_upper"],"record_type":"original_ball_object","role":"PC"},{"alias":"Cplus_SP","endpoint":"upper","path":["complete_new_positive_correction","complete_positive_source_upper"],"record_type":"original_ball_object","role":"WSP"},{"alias":"A_c","endpoint":"upper","path":["new_records","A_c"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"A_b_from_L","endpoint":"upper","path":["new_records","A_b_from_L"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"C_P","endpoint":"upper","path":["new_records","C_P"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"C_K","endpoint":"upper","path":["new_records","C_K"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"A_infty","endpoint":"upper","path":["new_records","A_infty"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"L_star","endpoint":"upper","path":["new_records","L_star"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"C_V0","endpoint":"upper","path":["new_records","C_V0"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"C_R0","endpoint":"upper","path":["new_records","C_R0"],"record_type":"original_ball_object","role":"WHVA"},{"alias":"Ni_minus","endpoint":"upper","path":["complete_coordinate_conclusion","windows","-4/3","complete_Ni_upper"],"record_type":"original_ball_string","role":"NIF"},{"alias":"Cs_inverse_minus","endpoint":"upper","path":["complete_frozen_stable_inverse_conclusion","windows","-4/3","complete_frozen_stable_inverse_upper"],"record_type":"original_ball_string","role":"NIF"},{"alias":"PW_C_R","endpoint":"upper","path":["copied_original_scalar_records","C_R"],"record_type":"original_ball_object","role":"WMR"},{"alias":"KH_inverse_L2","endpoint":"upper","path":["copied_original_scalar_records","KHinv_L2"],"record_type":"original_ball_object","role":"WMR"},{"alias":"sqrt_two_upper","endpoint":"upper","path":["copied_original_scalar_records","sqrt_two_upper"],"record_type":"original_ball_object","role":"WMR"}]''')
QUALIFICATION_SPECS = json.loads(r'''[{"name":"derived_definition_sha256","path":["derived_definition_sha256"],"projection":"exact","role":"negative"},{"name":"explicit_direction_definition_sha256","path":["explicit_direction_definition_sha256"],"projection":"exact","role":"negative"},{"name":"exact_real_delta_radius","path":["exact_real_delta_radius"],"projection":"exact","role":"negative"},{"name":"exact_affine_parameter_offset","path":["exact_affine_parameter_offset"],"projection":"exact","role":"negative"},{"name":"physical_parameter","path":["physical_parameter"],"projection":"exact","role":"negative"},{"name":"nu_family","path":["nu_family"],"projection":"exact","role":"negative"},{"name":"entire_positive_interval","path":["entire_positive_interval"],"projection":"exact","role":"negative"},{"name":"fixed_body_cut","path":["fixed_body_cut"],"projection":"exact","role":"negative"},{"name":"collar_length_upper","path":["collar_length_upper"],"projection":"exact","role":"negative"},{"name":"all_unbounded_high_indices","path":["all_unbounded_high_indices"],"projection":"exact","role":"negative"},{"name":"physical_minimum","path":["physical_minimum"],"projection":"exact","role":"negative"},{"name":"state_normalization","path":["state_normalization"],"projection":"exact","role":"negative"},{"name":"same_genuine_forward_and_backward_Riccati_reference","path":["same_genuine_forward_and_backward_Riccati_reference"],"projection":"exact","role":"negative"},{"name":"original_collar_native_sha256","path":["original_collar_native_sha256"],"projection":"exact","role":"negative"},{"name":"original_complete_body_native_sha256","path":["original_complete_body_native_sha256"],"projection":"exact","role":"negative"},{"name":"original_complete_outer_native_sha256","path":["original_complete_outer_native_sha256"],"projection":"exact","role":"negative"},{"name":"all_original_collar_body_target_reference_and_outer_mathematics_recomputed","path":["all_original_collar_body_target_reference_and_outer_mathematics_recomputed"],"projection":"exact","role":"negative"},{"name":"four_small_original_receipts_only","path":["four_small_original_receipts_only"],"projection":"exact","role":"negative"},{"name":"original_full_body_native_reread","path":["original_full_body_native_reread"],"projection":"exact","role":"negative"},{"name":"original4650_closed_kernel_rows_and3594_interfaces_recomputed","path":["original4650_closed_kernel_rows_and3594_interfaces_recomputed"],"projection":"exact","role":"negative"},{"name":"input_order","path":["input_order"],"projection":"exact","role":"negative"},{"name":"exterior_input_order","path":["exterior_input_order"],"projection":"exact","role":"negative"},{"name":"exterior_mean_input_order","path":["exterior_mean_input_order"],"projection":"exact","role":"negative"},{"name":"ordinary_source_contract","path":["ordinary_source_contract"],"projection":"exact","role":"negative"},{"name":"raw_state_contract","path":["raw_state_contract"],"projection":"exact","role":"negative"},{"name":"all_affine_jump_inputs_are_in_new_Y_units","path":["all_affine_jump_inputs_are_in_new_Y_units"],"projection":"exact","role":"negative"},{"name":"ordinary_and_raw_jump_Bessel_conversions_paid","path":["ordinary_and_raw_jump_Bessel_conversions_paid"],"projection":"exact","role":"negative"},{"name":"root_input_and_output_mixed_Bessel_conversions_paid","path":["root_input_and_output_mixed_Bessel_conversions_paid"],"projection":"exact","role":"negative"},{"name":"independent_even_mean_and_all_head_and_affine_source_ports_retained","path":["independent_even_mean_and_all_head_and_affine_source_ports_retained"],"projection":"exact","role":"negative"},{"name":"low_to_high_original_bound_conservative_in_negative_source_window","path":["low_to_high_original_bound_conservative_in_negative_source_window"],"projection":"exact","role":"negative"},{"name":"high_to_head_uses_complete_original97_to288_shell_and1153_factor","path":["high_to_head_uses_complete_original97_to288_shell_and1153_factor"],"projection":"exact","role":"negative"},{"name":"negative_order_root_reflection_one_half_gate_not_required","path":["negative_order_root_reflection_one_half_gate_not_required"],"projection":"exact","role":"negative"},{"name":"complete_negative_order_physical_outer_graph_proved","path":["complete_negative_order_physical_outer_graph_proved"],"projection":"exact","role":"negative"},{"name":"given_complete_head_positive_high_inverse_and_root_graph_proved","path":["given_complete_head_positive_high_inverse_and_root_graph_proved"],"projection":"exact","role":"negative"},{"name":"negative_one_source_window_proved","path":["negative_one_source_window_proved"],"projection":"exact","role":"negative"},{"name":"full_low_high_Schur_inverse_proved","path":["full_low_high_Schur_inverse_proved"],"projection":"exact","role":"negative"},{"name":"complete_infinite_BVP_inverse_proved","path":["complete_infinite_BVP_inverse_proved"],"projection":"exact","role":"negative"},{"name":"complete_strong_return_norm_evaluated","path":["complete_strong_return_norm_evaluated"],"projection":"exact","role":"negative"},{"name":"numerical_cutoff97_inverse_claimed","path":["numerical_cutoff97_inverse_claimed"],"projection":"exact","role":"negative"},{"name":"actual_full_PDE_response_error_proved","path":["actual_full_PDE_response_error_proved"],"projection":"exact","role":"negative"},{"name":"true_parameter_Schur_proved","path":["true_parameter_Schur_proved"],"projection":"exact","role":"negative"},{"name":"nonlinear_background_neighbourhood_proved","path":["nonlinear_background_neighbourhood_proved"],"projection":"exact","role":"negative"},{"name":"nonzero_delta_M96_family_proved","path":["nonzero_delta_M96_family_proved"],"projection":"exact","role":"negative"},{"name":"order1_exterior_upgrade_proved","path":["order1_exterior_upgrade_proved"],"projection":"exact","role":"negative"},{"name":"mathematical_parameters","path":["actual_scientific_receipt","mathematical_parameters"],"projection":"exact","role":"PC"},{"name":"scope","path":["actual_scientific_receipt","scope"],"projection":"exact","role":"PC"},{"name":"complete_positive_domain_conclusion","path":["actual_scientific_receipt","complete_positive_domain_conclusion"],"projection":"all_non_ball_leaves_preserve_positions","role":"PC"},{"name":"complete_cutoff_and_head_conclusion","path":["actual_scientific_receipt","complete_cutoff_and_head_conclusion"],"projection":"all_non_ball_leaves_preserve_positions","role":"PC"},{"name":"complete_strong_correction_conclusion","path":["actual_scientific_receipt","complete_strong_correction_conclusion"],"projection":"all_non_ball_leaves_preserve_positions","role":"PC"},{"name":"parameters","path":["parameters"],"projection":"exact","role":"WSP"},{"name":"retained_scope","path":["retained_scope"],"projection":"exact","role":"WSP"},{"name":"complete_operator_identity_conclusion","path":["complete_operator_identity_conclusion"],"projection":"exact","role":"WSP"},{"name":"complete_new_positive_correction","path":["complete_new_positive_correction"],"projection":"all_non_ball_leaves_preserve_positions","role":"WSP"},{"name":"prior_complete_operator_identity_conclusion","path":["complete_prior_scientific_conclusion_read_verbatim","complete_operator_identity_conclusion"],"projection":"exact","role":"WSP"},{"name":"prior_retained_scope","path":["complete_prior_scientific_conclusion_read_verbatim","retained_scope"],"projection":"exact","role":"WSP"},{"name":"prior_positive_correction","path":["complete_prior_scientific_conclusion_read_verbatim","complete_wpc_positive_correction_conclusion"],"projection":"all_non_ball_leaves_preserve_positions","role":"WSP"},{"name":"parameters","path":["parameters"],"projection":"exact","role":"WHVA"},{"name":"retained_scope","path":["retained_scope"],"projection":"exact","role":"WHVA"},{"name":"copied_original_scope","path":["copied_original_scope"],"projection":"exact","role":"WHVA"},{"name":"strict_mesh_gate","path":["strict_mesh_gate"],"projection":"all_non_ball_leaves_preserve_positions","role":"WHVA"},{"name":"required_N_diagnostic","path":["required_N_diagnostic"],"projection":"all_non_ball_leaves_preserve_positions","role":"WHVA"},{"name":"complete_body_source_choice","path":["complete_body_source_choice"],"projection":"all_non_ball_leaves_preserve_positions","role":"WHVA"},{"name":"parameters","path":["parameters"],"projection":"exact","role":"NIF"},{"name":"retained_scope","path":["retained_scope"],"projection":"exact","role":"NIF"},{"name":"complete_operator_identity_conclusion","path":["complete_operator_identity_conclusion"],"projection":"exact","role":"NIF"},{"name":"coordinate_minus","path":["complete_coordinate_conclusion","windows","-4/3"],"projection":"all_non_ball_leaves_preserve_positions","role":"NIF"},{"name":"stable_inverse_minus","path":["complete_frozen_stable_inverse_conclusion","windows","-4/3"],"projection":"all_non_ball_leaves_preserve_positions","role":"NIF"},{"name":"parameters","path":["parameters"],"projection":"exact","role":"WMR"},{"name":"retained_scope","path":["retained_scope"],"projection":"exact","role":"WMR"},{"name":"complete_original_parameters","path":["copied_original_scopes","complete_original_parameters"],"projection":"exact","role":"WMR"},{"name":"complete_original_retained_scope","path":["copied_original_scopes","complete_original_retained_scope"],"projection":"exact","role":"WMR"},{"name":"negative_reception","path":["copied_original_scopes","complete_original_node_qualifications","negative_reception"],"projection":"exact","role":"WMR"},{"name":"whole","path":["copied_original_scopes","complete_original_node_qualifications","whole"],"projection":"exact","role":"WMR"}]''')
ORIGINAL_RECORD_BYTES = json.loads(r'''8461''')
ORIGINAL_RECORD_SHA = json.loads(r'''"03a080cc0d80cea3a158dacc6cd6f65de2b14a63b3618477d26fbf2308f00ed2"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''31723''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"3e8c134dc321b54a68ad4a0ee76686f34047610a67716b463077c5a7c59cd013"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''5097''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"0c0d6915c992373b8a80b5185b895c47d932499383d2a6bec50bd89e3838caf1"''')
REMAINING_UNKNOWN_FACTORS = json.loads(r'''["G","B_target_inverse","W_inverse_A","actual_signed_finite_inverse"]''')
MAX_SCIENCE_BYTES = json.loads(r'''72000''')

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
                    and 0 <= key < len(value)), "missing complete old field")
        value = value[key]
    return value

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
            "current input spec must have five fields")
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


def original_qualifications(value):
    """Exact declared projection, retaining every non-ball key and list position."""
    if isinstance(value, str) and re.fullmatch(r"\[.*\+/-.*\]", value):
        return None
    if isinstance(value, dict):
        if "ball" in value:
            return None
        return {key: original_qualifications(child) for key, child in value.items()}
    if isinstance(value, list):
        return [original_qualifications(child) for child in value]
    return copy.deepcopy(value)

def original_source_identity(doc):
    return copy.deepcopy(doc.get("source_sha256") or doc.get("scientific_modules"))

def original_manifest_identity(doc):
    return doc.get("input_manifest_sha256") or doc.get("manifest_sha256")

def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(digest(manifest_raw) == manifest_sha, "manifest CLI identity")
    manifest = exact_json(manifest_raw)
    require(isinstance(manifest["files"], list)
            and len(manifest["files"]) == 10, "ten complete current inputs")
    specs = manifest["files"]
    roles = [s["role"] for s in EXPECTED_OLD_FILES] + [
        "proof_WOB", "science", "worker", "rules"]
    require([s["role"] for s in specs] == roles
            and len({s["path"] for s in specs}) == 10,
            "complete current role order and unique paths")
    files = {s["role"]: s for s in specs}
    for expected in EXPECTED_OLD_FILES:
        require(same_json(files[expected["role"]], expected), "original file pin differs")
    require(same_json(files["proof_WOB"], EXPECTED_PROOF), "published WOB identity")
    require(files["science"]["path"] == SOURCE_PATH
            and files["worker"]["path"] == WORKER_PATH, "new entry paths")
    raw = {s["role"]: check_file(root, s) for s in specs}
    require(Path(__file__).resolve() == safe_path(root, SOURCE_PATH)
            and Path(__file__).read_bytes() == raw["science"], "actual entry bytes")
    require(same_json(manifest["scientific_modules"], [files["science"]]),
            "one new mathematical source")
    require(manifest["historical_inputs"] == []
            and manifest["expected_current_input_count"] == 10,
            "current-only closure")
    module_map = {"science": files["science"]["sha256"]}
    op = manifest["operation"]
    require(manifest["repository"] == PUBLIC_REPOSITORY
            and manifest["problem_id"] == PROBLEM_ID
            and same_json(manifest["parameters"], PARAMETERS)
            and op["kind"] == KIND and op["scientific_kind"] == KIND
            and op["problem_id"] == PROBLEM_ID
            and op["bits_parameter"] == "arithmetic_bits"
            and same_json(op["parameters"], PARAMETERS)
            and same_json(op["retained_scope"], RETAINED_SCOPE)
            and same_json(op["scientific_field_names"], SCI_FIELDS)
            and same_json(op["complete_gate_names"], GATE_LABELS)
            and same_json(op["ordered_targets"], ORDERED_GRAPH_NAMES)
            and same_json(op["scientific_module_binding"], module_map)
            and op["maximum_scientific_bytes"] == MAX_SCIENCE_BYTES,
            "complete operation profile differs")
    for role in ("science", "worker"):
        ast.parse(raw[role].decode("utf-8"), filename=files[role]["path"])
    docs = {s["role"]: exact_json(raw[s["role"]]) for s in EXPECTED_OLD_FILES}
    science = {}
    for role, expected in OLD_SCHEMA_RECEIPTS.items():
        outer = docs[role]
        doc = at(outer, expected["scientific_path"])
        science[role] = doc
        require(isinstance(outer, dict) and isinstance(doc, dict)
                and len(outer) == expected["outer_field_count"]
                and digest(canonical(sorted(outer))) == expected["outer_fields_sha256"]
                and len(doc) == expected["scientific_field_count"]
                and digest(canonical(sorted(doc))) == expected["scientific_fields_sha256"],
                "complete original schema identity")
        if expected["canonical_raw_required"]:
            require(canonical(outer) == raw[role], "original canonical bytes")
        require(doc["kind"] == expected["kind"] and doc["complete"] is True
                and doc["failure"] is None, "original complete successful science")
        if "proved" in doc:
            require(doc["proved"] is True, "original proved status")
        if "actual_returncode" in doc:
            require(type(doc["actual_returncode"]) is int
                    and doc["actual_returncode"] == 0, "original returncode")
        gates = doc["gates"]
        require(isinstance(gates, list) and len(gates) == expected["gate_count"]
                and all(set(g) == {"name", "passed"} and g["passed"] is True
                        for g in gates)
                and digest(canonical([g["name"] for g in gates]))
                    == expected["gate_names_sha256"]
                and digest(canonical(gates)) == expected["complete_gates_sha256"],
                "all original gate names and statuses")
        require(same_json(original_source_identity(doc), expected["source_identity"])
                and original_manifest_identity(doc) == expected["manifest_sha256"]
                and same_json(doc.get("runtime"), expected["runtime"]),
                "original source manifest and runtime")
    pc_outer, pc = docs["PC"], science["PC"]
    require(pc_outer["complete"] is True and pc_outer["actual_returncode"] == 0
            and pc_outer["actual_failure"] is None
            and pc_outer["run_id"] == pc["run_id"]
            and pc_outer["run_attempt"] == pc["run_attempt"]
            and pc_outer["source_budget_source_sha256"] == pc["source_sha256"]
            and pc_outer["input_manifest_sha256"] == pc["input_manifest_sha256"],
            "complete PC wrapper and embedded science")
    negative, wsp, whva, nif, wmr = (science[r] for r in
        ("negative", "WSP", "WHVA", "NIF", "WMR"))
    require(negative["exact_real_delta_radius"] == "1/100000000"
            and negative["all_unbounded_high_indices"] == "every |j|>=97"
            and negative["physical_minimum"] == 388
            and negative["independent_even_mean_and_all_head_and_affine_source_ports_retained"] is True
            and negative["given_complete_head_positive_high_inverse_and_root_graph_proved"] is True
            and negative["full_low_high_Schur_inverse_proved"] is False,
            "full original given-head domain and retained independent ports")
    require(pc["mathematical_parameters"]["exact_real_delta_radius"] == "1/100000000"
            and pc["mathematical_parameters"]["exact_new_shift"] == "1/512"
            and pc["mathematical_parameters"]["exact_transition_s_interval"]
                == ["1/500000", "3/1000000"]
            and pc["scope"]["nonzero_root_beta_n_retained"] is True
            and pc["scope"]["full_positive_correction_seven_port_graph_consumed"] is True,
            "same complete genuine positive trial and exact cutoff")
    prior = wsp["complete_prior_scientific_conclusion_read_verbatim"]
    require(prior["complete_wpc_positive_correction_conclusion"]
                ["same_original_PC_trial_and_cutoff"] is True
            and prior["complete_wpc_positive_correction_conclusion"]
                ["full_means_genuine_root_shear_and_terminal_column_retained"] is True
            and prior["complete_operator_identity_conclusion"]["positive_source"]
                == "original chi_prime times complete genuine raw pair hG"
            and wsp["retained_scope"]["same_positive_family_cutoff_and_receiver"] is True,
            "WSP is the same full RH source, with independent root finite term")
    require(whva["strict_mesh_gate"]["passed"] is False
            and whva["resolvent_admitted"] is False
            and whva["parameters"]["radial_mesh_N"] == 4096
            and whva["required_N_diagnostic"]["required_N_decimal"] == "145475"
            and whva["required_N_diagnostic"]["within_declared_cap"] is False
            and whva["complete_body_source_choice"]["selected"] == "A_b_from_L"
            and same_json(whva["complete_body_source_choice"]["complete_record"],
                          whva["new_records"]["A_b_from_L"]),
            "original completed false sufficient gate and whole source choice")
    require(nif["parameters"]["exact_real_delta_radius"] == "1/100000000"
            and nif["parameters"]["exact_intrinsic_parameter"]
                == wmr["copied_original_scopes"]["complete_original_parameters"]["fixed_eta0"]
            and nif["complete_operator_identity_conclusion"]
                ["selected_KAM_conjugacy_only_at_original_delta_star"] is True
            and nif["complete_operator_identity_conclusion"]["physical_mean_coordinates"] == 2
            and wmr["retained_scope"]["same_selected_real_member_only"] is True
            and wmr["retained_scope"]["physical_two_means_and_mean_feedback_retained"] is True
            and wmr["retained_scope"]["true_physical_96_columns_and_all_Theta_cross_blocks_retained"] is True,
            "same frozen reflected coordinates and physical mean/root units")
    records = {}
    for spec in RECORD_SPECS:
        value = at(docs[spec["role"]], spec["path"])
        if spec["record_type"] == "original_ball_string":
            require(isinstance(value, str), "original bare scalar spelling")
        else:
            keys = ({"ball", "lower", "upper"}
                    if spec["record_type"] == "original_ball_lower_upper_object"
                    else {"ball"})
            require(isinstance(value, dict) and set(value) == keys
                    and all(isinstance(x, str) for x in value.values()),
                    "complete original typed record")
        require(spec["endpoint"] == "upper", "original nonnegative upper endpoint")
        records[spec["alias"]] = copy.deepcopy(value)
    require(len(records) == 42 and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA, "all42 original records")
    scopes = {s["role"]: {} for s in EXPECTED_OLD_FILES}
    for spec in QUALIFICATION_SPECS:
        value = at(docs[spec["role"]], spec["path"])
        if spec["projection"] == "exact":
            kept = copy.deepcopy(value)
        else:
            require(spec["projection"] == "all_non_ball_leaves_preserve_positions",
                    "declared complete qualifier projection")
            kept = original_qualifications(value)
        scopes[spec["role"]][spec["name"]] = kept
    require(len(QUALIFICATION_SPECS) == 73
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "complete73-path original qualification projection")
    accepted = {"kind": "six_complete_readonly_WOB_inputs_v1", "originals": {}}
    for expected in EXPECTED_OLD_FILES:
        role = expected["role"]
        doc = science[role]
        accepted["originals"][role] = {
            "identity": {"file": expected["path"], "bytes": expected["bytes"],
                         "sha256": expected["sha256"],
                         "git_blob": expected["git_blob_sha"]},
            "science_object_path": OLD_SCHEMA_RECEIPTS[role]["scientific_path"],
            "kind": doc["kind"], "complete": True, "failure": None,
            "complete_gate_count": len(doc["gates"]),
            "all_complete_gates_passed": True,
            "source_identity": original_source_identity(doc),
            "manifest_sha256": original_manifest_identity(doc)}
    accepted["originals"]["WHVA"].update({
        "original_strict_mesh_gate": copy.deepcopy(whva["strict_mesh_gate"]),
        "original_required_N_diagnostic": copy.deepcopy(whva["required_N_diagnostic"]),
        "original_resolvent_admitted": False,
        "original_body_selected_label": whva["complete_body_source_choice"]["selected"]})
    require(len(canonical(accepted)) == ORIGINAL_ACCEPTED_BYTES
            and digest(canonical(accepted)) == ORIGINAL_ACCEPTED_SHA,
            "complete accepted original receipts")
    verified = {role: {key: files[role][key] for key in ("bytes", "sha256")}
                for role in roles[:7]}
    return {"manifest": manifest, "files": files, "records": records,
            "scopes": scopes, "accepted": accepted, "verified": verified,
            "module_map": module_map, "raw": raw, "root": root}
# New WOB scalar targets only. No old producer import or evaluation.
def norm_upper(value):
    require(value.is_finite(), "nonfinite bound")
    require(value.lower() >= 0, "negative norm bound")
    return value.upper()

def saved_upper(record):
    if isinstance(record, str):
        text = record
    else:
        require(isinstance(record, dict)
                and set(record) in ({"ball"}, {"ball", "lower", "upper"})
                and isinstance(record["ball"], str), "complete original record type")
        text = record["ball"]
    return norm_upper(arb(text))

def rational(text):
    value = Fraction(text)
    return arb(value.numerator) / arb(value.denominator)

def positive_sqrt(value):
    require(value.is_finite() and value.lower() > 0, "positive complete sqrt input")
    return value.sqrt()

def read_new(graphs, name, key):
    return saved_upper(graphs[name]["complete_new_records"][key])

def complete_outer_rows(saved, graphs, emit):
    L = saved_upper(emit("low_Hminus5_6_to_L2_weight_upper",
        arb(1 + 16*96*96) ** (arb(5)/12), "fractional_power"))
    e = saved_upper(saved["E_minus"])
    mu = saved_upper(saved["mu_minus"])
    h = saved_upper(emit("high_odd_outer_row_upper", L*e))
    emit("complete_high_outer_row_upper",
         positive_sqrt(h*h + mu*mu), "square_root")
    low = saved_upper(emit("low_odd_outer_row_upper", L*(arb(1)/5 + e)))
    emit("complete_low_outer_row_upper",
         positive_sqrt(low*low + L*L + mu*mu), "square_root")
    b = saved_upper(saved["B_a"])
    c = saved_upper(saved["C_a"])
    f = saved_upper(emit("affine_fB_Robin_row_upper",
        b*saved_upper(saved["U_minus"]) + c*saved_upper(saved["V_minus"])))
    mf = saved_upper(saved["mu_F"])
    mc = saved_upper(saved["mu_C"])
    lf = L*f
    lc = L*c
    emit("complete_affine_fB_low_pair_upper",
         positive_sqrt(lf*lf + mf*mf), "square_root")
    emit("complete_affine_rB_low_pair_upper", L*b)
    emit("complete_affine_rC_low_pair_upper",
         positive_sqrt(lc*lc + mc*mc), "square_root")

def complete_positive_columns(saved, graphs, emit):
    ac = saved_upper(saved["A_c"])
    ab = saved_upper(saved["A_b_from_L"])
    yc = saved_upper(saved["Y_c"])*ac
    yb = saved_upper(saved["Y_b"])*ab
    emit("complete_head_outer_trace_upper",
         4*positive_sqrt(yc*yc + yb*yb), "square_root")
    uc = saved_upper(saved["U_c"])*ac
    ub = saved_upper(saved["U_b"])*ab
    emit("complete_head_root_unstable_upper",
         positive_sqrt(uc*uc + ub*ub), "square_root")
    eb = saved_upper(saved["e_b"])
    pb = saved_upper(emit("complete_outer_b_raw_state_upper",
                         saved_upper(saved["C_B"])*eb))
    emit("complete_outer_b_outer_trace_upper", 4*saved_upper(saved["Y_B"])*eb)
    emit("complete_outer_b_root_unstable_upper", saved_upper(saved["U_B"])*eb)
    emit("complete_outer_b_to_head_source_upper",
         1153*saved_upper(saved["L_star"])*pb)

def complete_288_shell(saved, graphs, emit):
    factor = saved_upper(emit("new_complete_shell_exponential_factor_upper",
                             (arb(768)/512).exp(), "exponential"))
    for target, original in (
            ("complete_shell_crude_candidate_upper", "CF_crude"),
            ("complete_shell_reconstructed_candidate_upper", "CF_reconstructed"),
            ("complete_shell_selected_old_candidate_upper", "CF_selected")):
        emit(target, factor*saved_upper(saved[original]))

def complete_observations(saved, graphs, emit):
    cut = saved_upper(emit("complete_cutoff_radial_measure_factor_upper",
                          positive_sqrt(arb(3)/1000000), "square_root"))
    cf = read_new(graphs, "complete_genuine_288_shell",
                  "complete_shell_selected_old_candidate_upper")
    trial = saved_upper(emit("complete_trial_head_source_term_upper",
                            (arb(58)/5)*cut*cf))
    correction = saved_upper(emit("complete_correction_head_source_term_upper",
        1153*saved_upper(saved["L_star"])*saved_upper(saved["C_c"])
        *saved_upper(saved["Cplus_SP"])))
    ni = saved_upper(saved["Ni_minus"])
    phi = saved_upper(emit("complete_Phi_upper", ni*(trial + correction)))
    upsilon = saved_upper(emit("complete_Upsilon_upper",
        4*ni*saved_upper(saved["Y_c"])*saved_upper(saved["Cplus_SP"])))
    inverse = saved_upper(saved["Cs_inverse_minus"])
    emit("complete_rough_head_observation_upper", phi*inverse)
    emit("complete_rough_outer_observation_upper", upsilon*inverse)

def complete_zero_IVP(saved, graphs, emit):
    outer = "complete_outer_low_and_affine_rows"
    positive = "complete_positive_head_and_outer_columns"
    observation = "complete_genuine_and_rough_observations"
    kh = read_new(graphs, outer, "complete_high_outer_row_upper")
    kl = read_new(graphs, outer, "complete_low_outer_row_upper")
    ya = read_new(graphs, positive, "complete_head_outer_trace_upper")
    yb = read_new(graphs, positive, "complete_outer_b_outer_trace_upper")
    fb = read_new(graphs, positive, "complete_outer_b_to_head_source_upper")
    phi = read_new(graphs, observation, "complete_Phi_upper")
    upsilon = read_new(graphs, observation, "complete_Upsilon_upper")
    t0 = saved_upper(saved["C_R0"])
    v0 = saved_upper(saved["C_V0"])
    emit("complete_C0_endpoint_row_upper",
         t0*(saved_upper(saved["A_infty"]) + saved_upper(saved["C_K"])) + kh*ya)
    emit("complete_Db0_endpoint_row_upper", t0*fb + kl + kh*yb)
    emit("complete_D0_high_endpoint_row_upper", t0*phi + kh*upsilon)
    emit("complete_Bb0_body_row_upper", v0*fb)
    emit("complete_B0_high_body_row_upper", v0*phi)

def complete_zero_stable_root_rows(saved, graphs, emit):
    # Exact identity 1/sqrt(2)=sqrt(2)/2 uses the already saved sqrt2 upper.
    # It neither recomputes sqrt2 nor treats an old upper as a denominator.
    reciprocal = saved_upper(emit("complete_reciprocal_sqrt_two_upper",
                                  saved_upper(saved["sqrt_two_upper"])/2))
    positive = "complete_positive_head_and_outer_columns"
    ua = read_new(graphs, positive, "complete_head_root_unstable_upper")
    ub = read_new(graphs, positive, "complete_outer_b_root_unstable_upper")
    cr = saved_upper(saved["PW_C_R"])
    emit("complete_head_density_waist_receiver_upper", 9*cr*ua)
    emit("complete_outer_b_density_waist_receiver_upper", 9*cr*ub)
    initial = saved_upper(emit("complete_initial_primitive_waist_receiver_upper",
        saved_upper(saved["KH_inverse_L2"])*reciprocal*cr))
    emit("complete_head_primitive_waist_receiver_upper", 9*initial*ua)
    emit("complete_outer_b_primitive_waist_receiver_upper", 9*initial*ub)
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


def main():
    global arb
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("repo", "manifest", "manifest-sha", "out"):
        parser.add_argument("--" + key, required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    require(args.bits == 320, "fixed320-bit arithmetic")
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
    require(not out.exists(), "complete or partial science already exists")
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
        "complete_new_graphs": {}, "remaining_unknown_factors": REMAINING_UNKNOWN_FACTORS[:],
        "current_target": None, "completed_targets": [],
        "saved_record_counts": {name: 0 for name in ORDERED_GRAPH_NAMES},
        "gates": [], "actual_progress": copy.deepcopy(ACTUAL_PROGRESS_INITIAL),
        "actual_mathematical_wall_seconds": 0.0,
        "automatic_retry_authorized": False}
    math_start = None

    def publish(check_size=True):
        if math_start is not None:
            doc["actual_mathematical_wall_seconds"] = time.perf_counter() - math_start
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
            require(len(raw) <= MAX_SCIENCE_BYTES, "complete scientific JSON byte cap")
        restored = exact_json(out.read_bytes())
        require(canonical(restored) == raw, "complete atomic scientific readback")
        return restored

    def gate(name):
        require(len(doc["gates"]) < len(GATE_LABELS)
                and name == GATE_LABELS[len(doc["gates"])], "gate order")
        doc["gates"].append({"name": name, "passed": True})

    def start_graph(name):
        position = len(doc["completed_targets"])
        require(position < len(ORDERED_GRAPH_NAMES)
                and name == ORDERED_GRAPH_NAMES[position]
                and doc["current_target"] is None
                and name not in doc["complete_new_graphs"], "new complete graph order")
        pattern = copy.deepcopy(NEW_GRAPH_SHAPES[name])
        pattern["complete"] = False
        pattern["complete_new_records"] = {}
        doc["complete_new_graphs"][name] = pattern
        doc["current_target"] = name
        doc["stage"] = "started:" + name
        publish()

        def emit(key, value, operation=None):
            require(key in NEW_GRAPH_SHAPES[name]["complete_new_records"]
                    and key not in doc["complete_new_graphs"][name]["complete_new_records"],
                    "new scalar target repeated or unknown")
            require(operation in (None, "exponential", "fractional_power", "square_root"),
                    "new operation category")
            if operation == "exponential":
                require(name == "complete_genuine_288_shell"
                        and key == "new_complete_shell_exponential_factor_upper",
                        "one authorized exponential")
            if operation == "fractional_power":
                require(name == "complete_outer_low_and_affine_rows"
                        and key == "low_Hminus5_6_to_L2_weight_upper",
                        "one authorized positive fractional power")
            record = {"ball": norm_upper(value).str(75)}
            doc["complete_new_graphs"][name]["complete_new_records"][key] = record
            doc["saved_record_counts"][name] += 1
            doc["actual_progress"]["new_records_saved"] += 1
            counter = {"exponential": "new_exponentials_saved",
                       "fractional_power": "new_fractional_powers_saved",
                       "square_root": "new_square_roots_saved"}.get(operation)
            if counter is not None:
                doc["actual_progress"][counter] += 1
            doc["stage"] = "record_saved:" + name
            restored = publish()
            return copy.deepcopy(restored["complete_new_graphs"][name]
                                 ["complete_new_records"][key])
        return emit

    def finish_graph(name):
        graph = doc["complete_new_graphs"][name]
        require(doc["current_target"] == name
                and doc["saved_record_counts"][name] == GRAPH_RECORD_COUNTS[name],
                "complete new scalar prefix required")
        graph["complete"] = True
        doc["stage"] = "complete_graph_returned:" + name
        publish(check_size=False)
        require(complete_shape(graph, NEW_GRAPH_SHAPES[name]), "complete graph shape")
        doc["completed_targets"].append(name)
        doc["actual_progress"]["new_graphs_completed"] += 1
        doc["current_target"] = None
        doc["stage"] = "completed:" + name
        gate(GATE_LABELS[9 + len(doc["completed_targets"]) - 1])
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
        doc["actual_progress"]["original_receipts_admitted"] = 6
        doc["actual_progress"]["original_record_objects_copied"] = 42
        doc["actual_progress"]["original_false_sufficient_gate_preserved"] = True
        doc["stage"] = "complete_original_input_copies_saved"
        publish()
        import flint
        from flint import arb, ctx
        require(sys.version_info[:3] == (3, 12, 14)
                and flint.__version__ == "0.9.0", "directed public runtime")
        ctx.prec = 320
        doc["runtime"] = {"Python": "3.12.14", "python_flint": "0.9.0"}
        saved = doc["copied_original_scalar_records"]
        for record in saved.values():
            saved_upper(record)
        for name in GATE_LABELS[:9]:
            gate(name)
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        operations = (
            ("complete_outer_low_and_affine_rows", complete_outer_rows),
            ("complete_positive_head_and_outer_columns", complete_positive_columns),
            ("complete_genuine_288_shell", complete_288_shell),
            ("complete_genuine_and_rough_observations", complete_observations),
            ("complete_zero_IVP_rows", complete_zero_IVP),
            ("complete_zero_stable_root_receiver_rows", complete_zero_stable_root_rows))
        for name, function in operations:
            emit = start_graph(name)
            function(saved, doc["complete_new_graphs"], emit)
            finish_graph(name)
        require(same_json(doc["saved_record_counts"], GRAPH_RECORD_COUNTS)
                and same_json(doc["actual_progress"], ACTUAL_PROGRESS_COMPLETE),
                "complete actual target counts")
        gate(GATE_LABELS[15])
        for role, spec in work["files"].items():
            require(check_file(work["root"], spec) == work["raw"][role],
                    "current input changed during new scalar work")
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "manifest changed during new scalar work")
        gate(GATE_LABELS[16])
        require(set(doc) == set(SCI_FIELDS)
                and doc["completed_targets"] == ORDERED_GRAPH_NAMES
                and doc["current_target"] is None
                and complete_shape(doc["complete_new_graphs"], NEW_GRAPH_SHAPES)
                and same_json(doc["parameters"], PARAMETERS)
                and same_json(doc["retained_scope"], RETAINED_SCOPE)
                and doc["remaining_unknown_factors"] == REMAINING_UNKNOWN_FACTORS,
                "complete scientific graph and retained unknowns")
        gate(GATE_LABELS[17])
        doc["complete"] = True
        doc["proved"] = True
        doc["actual_returncode"] = 0
        doc["stage"] = "complete"
        publish()
        return 0
    except BaseException as error:
        message = str(error).encode("utf-8", "replace")
        trace = traceback.format_exc().encode("utf-8", "replace")
        doc["complete"] = False
        doc["proved"] = False
        doc["actual_returncode"] = 1
        doc["stage"] = "preserved_failure"
        doc["failure"] = {
            "type": type(error).__name__,
            "message": message[:256].decode("utf-8", "ignore"),
            "traceback": trace[:2048].decode("utf-8", "ignore"),
            "message_truncated": len(message) > 256,
            "traceback_truncated": len(trace) > 2048}
        publish(check_size=False)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
