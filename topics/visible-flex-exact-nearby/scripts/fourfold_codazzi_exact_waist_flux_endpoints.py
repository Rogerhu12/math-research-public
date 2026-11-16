"""WEX: 31 new exact waist flux and two-primitive endpoint bounds."""
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
from pathlib import Path

PUBLIC_REPOSITORY = json.loads(r'''"Rogerhu12/math-research-public"''')
TOPIC = json.loads(r'''"topics/visible-flex-exact-nearby"''')
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_exact_waist_flux_endpoints.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py"''')
KIND = json.loads(r'''"complete_exact_waist_flux_and_two_primitive_endpoint_bounds"''')
PROBLEM_ID = json.loads(r'''"exact_waist_flux_two_primitive_endpoints_selected_original_97_v1"''')
PREFLIGHT_KIND = json.loads(r'''"complete_exact_waist_flux_endpoint_readonly_preflight_v1"''')
MAX_SCIENCE_BYTES = json.loads(r'''80000''')
DIAGNOSTIC_TYPE_BYTES = json.loads(r'''64''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''512''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''2048''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":72251,"git_blob_sha":"32ff92c516fcc5c43f3619930d4845d294289270","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json","role":"wgs_main","sha256":"8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"},{"bytes":31632,"git_blob_sha":"d6d13860e322d82ce354c8c0d0eb0f279ca63b3c","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json","role":"wgs_copies","sha256":"3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66"},{"bytes":22953,"git_blob_sha":"7a473349764e3499eb9eec4a1fd95730603229ab","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/complete_exact_waist_finite_reconstruction.json","role":"reconstruction","sha256":"113a03c9beae72e12ac163a0c43d5bc3e057a477b9ba0cfc847f1f52b5b89640"},{"bytes":14394,"git_blob_sha":"d2aa61e0dc1502181a9e86549e81311e8fdacdaf","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_free_waist_Airy_and_Schur_map.json","role":"free","sha256":"5f48bdc934047c86ed2fd2d79cb94c593c619cffefb3ac52510fd3c4bfe4b413"},{"bytes":7974,"git_blob_sha":"13b5b9809e2ba649511613eb5e58ef78f51908dd","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_four_waist_endpoint_contributions.json","role":"endpoints","sha256":"7fbee7f580c01944e585f5a763ce5a87717db8c8f59ea789b48f850fe6a75df3"},{"bytes":82508,"git_blob_sha":"146904d030cca0887fae921084396bf4008d0281","path":"topics/visible-flex-exact-nearby/notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json","role":"wrp","sha256":"4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee"},{"bytes":12958,"git_blob_sha":"c5d9166b914a17136c5058b3d213afc4dffad5c0","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extension_scalars.json","role":"extension","sha256":"5816db201af6f0da0f7412c1a1fe0f1521d5425debf37693ab652f152e7fec00"},{"bytes":61398,"git_blob_sha":"c20713f51366ef6c838147232994424bf3e633de","path":"topics/visible-flex-exact-nearby/notes/per_index_strict_flux_complete_mean_ci/run-43886938106-1/actual-scientific-conclusion.json","role":"current","sha256":"3243348d6dddc11c8baf1f6eb559d929a37c509a464165b7042d1ce47bb2e290"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":32416,"git_blob_sha":"bb4a4dcf445a17735bfa452bc4a430ffbd3ce9d7","path":"topics/visible-flex-exact-nearby/results/R133-supplement-exact-waist-flux-and-two-primitive-endpoint-reception.md","role":"proof_WEX","sha256":"6ffd46a4b4af3bd315039d667b7514fb7c47d4b8d749b72937dec69249142627"}''')
EXPECTED_WORKER = json.loads(r'''{"bytes":26542,"git_blob_sha":"c410f91faae59dac177b737faffe4dd11d3f2d46","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py","role":"worker","sha256":"3770e29dbb2becd615227c1ceceaf7c9a34cf585a705deeed75465dc02594d8e"}''')
OLD_FIELDSETS = json.loads(r'''{"current":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_current_provider","complete_new_graphs","completed_targets","current_prefix","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_record_copy_counts","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","upstream_record_copy_counts","verified_original_inputs","whole_candidate_choices","workflow_event_commit"],"endpoints":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"extension":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"free":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"reconstruction":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"wgs_copies":["actual_scientific_checkout_commit","complete","complete_readonly_input_projection","copied_complete_local_coefficients","copied_complete_local_coefficients_sha256","copied_complete_original_scopes","copied_complete_original_scopes_sha256","copied_original_scalar_records","copied_original_scalar_records_sha256","copied_original_stage_records","copied_original_stage_records_sha256","copy_counts","input_manifest_sha256","kind","local_coefficient_qualification","math_module_sha256","original_input_sha256","public_repository","run_attempt","run_id","source_sha256","workflow_event_commit"],"wgs_main":["accepted_original_inputs","actual_mathematical_wall_seconds","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_free_first_transport_conclusion","complete_higher_flow_and_cut_conclusion","complete_local_regular_packet_conclusion","complete_named_global_graph_conclusion","complete_original_inputs_file","complete_strict_coefficient_conclusion","complete_strict_forcing_conclusion","complete_strict_geometry_conclusion","complete_strict_leading_conclusion","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"],"wrp":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"]}''')
OLD_QUALIFICATION_IDENTITIES = json.loads(r'''{"current":{"bytes":48996,"sha256":"ff306934ca49f844dd258e728cb31d4deb63297977e43cd8f9cfeb58ef483e26"},"endpoints":{"bytes":7142,"sha256":"03d5f3e5697e67d8b83402d33df0d00af7f30b9b4a8bbff3d4fbe0e36a59699f"},"extension":{"bytes":2877,"sha256":"8b281728f9980c04b980dee09e9961870557e6c28da7c012870fa9030013f6c8"},"free":{"bytes":9144,"sha256":"447a305441ff431c968d9f4f682149a51806d5f799e50443fc4b12492fe4cfee"},"reconstruction":{"bytes":9418,"sha256":"842d68b9965e462b6a7053c4b8cfc79989165648eaa1574376b5e4872cd6fed4"},"wgs_copies":{"bytes":16834,"sha256":"f238e7927c3ae85d8327a648f3d7e3ab87f9aee80549cb0183f410bce751e0dd"},"wgs_main":{"bytes":30020,"sha256":"6eb0a4794cd3c47b482c80d6a32179a0ed50cd48ca5d71d50ffda14f8622e15e"},"wrp":{"bytes":73852,"sha256":"f8d61ebe55f4ce10f94b9bd1b35e4d74eb208e493aa83291202da86506862971"}}''')
OLD_GATE_LABELS = json.loads(r'''{"current":["directed_public_runtime","complete_thirteen_current_file_identities","three_complete_current_source_ASTs","eight_complete_original_schemas_and_statuses","all_complete_original_non_ball_qualification_leaves","all_forty_eight_complete_context_references","same_WGS_dual_file_original_domain_and_normalization","same_WBF_WJR_WDG_true_angular_inputs","complete_potential_tail_and_old_full_mean_kernels","successful_current_complete_WRP_provider","all_actual_positive_lower_endpoints_before_new_arithmetic","complete_thirty_two_strict_flux_records","complete_seven_mean_and_four_endpoint_records","complete_thirteen_same_receiver_records","two_complete_same_operator_whole_choices","all_current_inputs_unchanged","complete_record_copy_prefix_and_shape_accounting","complete_limited_scientific_conclusion"],"wgs_main":["actual public runtime and complete manifest identity","twenty current small texts have their complete exact bytes","two historical stages have exact immutable original identities","seven Python AST files with four old producers never imported","original complete free-Airy success and local domains","original complete strict ordinary jets and all real intervals","original shorter flows and two ungauged scalar directions","original fourth derivatives and cut phase jets","the original FA input chain remains exactly identified","original adjacent child and full fold publication succeeded","original whole child mathematics and formatter failure remain distinct","complete original fold payload and all consumed holomorphic domains","complete saved p0-p2 q0-q3 free records and exact FA overlap","typed old records scopes and same original real family","complete triangular derivative request certificate","complete strict coefficient products with both physical means","only new higher flow and cut derivatives with actual positive phase gap","complete strict fold geometry and all retained lower denominators","complete leading jets with original forward and reverse scalar fees","complete first forcing with every drift theta and mean term","complete local analytic packet and read-only free amplitude seeds","complete free first transport with nonzero old cut trace","complete named global graph and all original inputs unchanged","complete thirty-six fields twenty-four gates and limited conclusion"],"wrp":["directed_public_runtime","current_input_and_AST_identity","all_five_complete_original_files_byte_identical","complete_WJR_relative_phase_receipt","complete_WSM_profile_N6_receiver_same_binding","complete_original_scopes_and_failed_ancestry_retained","all_44_scalar_and_nine_qualification_copies_retained","same_measure_full_mean_original_phase_budgets_and_parity_window","complete_relative_inverse_phase_and_pullbacks","complete_fifteen_full_output_profile_weights","complete_same_whole_and_reduced_receiver","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]}''')
OLD_LITERAL_ASSERTIONS = json.loads(r'''[{"path":["complete"],"role":"wgs_main","value":true},{"path":["complete"],"role":"wgs_copies","value":true},{"path":["complete"],"role":"reconstruction","value":true},{"path":["complete"],"role":"free","value":true},{"path":["complete"],"role":"endpoints","value":true},{"path":["complete"],"role":"wrp","value":true},{"path":["complete"],"role":"extension","value":true},{"path":["complete"],"role":"current","value":true},{"path":["proved"],"role":"wgs_main","value":true},{"path":["failure"],"role":"wgs_main","value":null},{"path":["actual_returncode"],"role":"wgs_main","value":0},{"path":["arithmetic_bits"],"role":"wgs_main","value":320},{"path":["stage"],"role":"wgs_main","value":"complete"},{"path":["runtime"],"role":"wgs_main","value":{"Python":"3.12.14","python_flint":"0.9.0"}},{"path":["proved"],"role":"wrp","value":true},{"path":["failure"],"role":"wrp","value":null},{"path":["actual_returncode"],"role":"wrp","value":0},{"path":["arithmetic_bits"],"role":"wrp","value":320},{"path":["stage"],"role":"wrp","value":"complete"},{"path":["runtime"],"role":"wrp","value":{"Python":"3.12.14","python_flint":"0.9.0"}},{"path":["proved"],"role":"current","value":true},{"path":["failure"],"role":"current","value":null},{"path":["actual_returncode"],"role":"current","value":0},{"path":["arithmetic_bits"],"role":"current","value":320},{"path":["stage"],"role":"current","value":"complete"},{"path":["runtime"],"role":"current","value":{"Python":"3.12.14","python_flint":"0.9.0"}},{"path":["kind"],"role":"wgs_main","value":"actual_complete_global_fold_free_transport_finite_jets_v1"},{"path":["actual_progress","new_scalar_slots_saved"],"role":"wgs_main","value":437},{"path":["actual_progress","old_scientific_targets_recomputed"],"role":"wgs_main","value":0},{"path":["parameters","physical_frequency"],"role":"wgs_main","value":"n=4|j|"},{"path":["parameters","actual_original_interfaces"],"role":"wgs_main","value":3070},{"path":["complete_derivative_request_certificate","normalized_coefficients"],"role":"wgs_main","value":"ordinary derivative norm divided by a! b!"},{"path":["complete_derivative_request_certificate","fixed_degree_groups"],"role":"wgs_main","value":[[0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15]]},{"path":["complete_strict_geometry_conclusion","ordinary_one_sided_r_and_full_real_lifts"],"role":"wgs_main","value":true},{"path":["complete_strict_forcing_conclusion","full_second_order_drift_and_original_means_present"],"role":"wgs_main","value":true},{"path":["complete_strict_forcing_conclusion","full_theta_Q_KT_product_present"],"role":"wgs_main","value":true},{"path":["complete_free_first_transport_conclusion","genuine_potential_addition_included"],"role":"wgs_main","value":false},{"path":["complete_free_first_transport_conclusion","both_characteristic_branches_and_physical_signs"],"role":"wgs_main","value":true},{"path":["complete_free_first_transport_conclusion","old_root_trace_preserved_at_cut"],"role":"wgs_main","value":true},{"path":["complete_free_first_transport_conclusion","ordinary_fixed_dr_endpoints_and_all_partial_intervals"],"role":"wgs_main","value":true},{"path":["kind"],"role":"wgs_copies","value":"complete_original_inputs_for_global_fold_free_transport_finite_jets_v1"},{"path":["complete_readonly_input_projection"],"role":"wgs_copies","value":true},{"path":["copy_counts"],"role":"wgs_copies","value":{"complete_local_coefficient_objects":1,"complete_scope_objects":9,"current_scalar_records":66,"local_coefficient_ball_count":72,"stage_scalar_records":40}},{"path":["local_coefficient_qualification","all_original_coefficient_fields_copied"],"role":"wgs_copies","value":true},{"path":["kind"],"role":"reconstruction","value":"WEJ_complete_atomic_node_v1"},{"path":["failure"],"role":"reconstruction","value":null},{"path":["automatic_retry_authorized"],"role":"reconstruction","value":false},{"path":["all_printed_records_in_complete_conclusion"],"role":"reconstruction","value":true},{"path":["printed_record_event_count"],"role":"reconstruction","value":133},{"path":["conclusion","complete"],"role":"reconstruction","value":true},{"path":["kind"],"role":"free","value":"WEJ_complete_atomic_node_v1"},{"path":["failure"],"role":"free","value":null},{"path":["automatic_retry_authorized"],"role":"free","value":false},{"path":["all_printed_records_in_complete_conclusion"],"role":"free","value":true},{"path":["printed_record_event_count"],"role":"free","value":13},{"path":["conclusion","complete"],"role":"free","value":true},{"path":["kind"],"role":"endpoints","value":"WEJ_complete_atomic_node_v1"},{"path":["failure"],"role":"endpoints","value":null},{"path":["automatic_retry_authorized"],"role":"endpoints","value":false},{"path":["all_printed_records_in_complete_conclusion"],"role":"endpoints","value":true},{"path":["printed_record_event_count"],"role":"endpoints","value":8},{"path":["conclusion","complete"],"role":"endpoints","value":true},{"path":["kind"],"role":"extension","value":"WEJ_complete_atomic_node_v1"},{"path":["failure"],"role":"extension","value":null},{"path":["automatic_retry_authorized"],"role":"extension","value":false},{"path":["all_printed_records_in_complete_conclusion"],"role":"extension","value":true},{"path":["printed_record_event_count"],"role":"extension","value":104},{"path":["node_name"],"role":"reconstruction","value":"complete_exact_waist_finite_reconstruction"},{"path":["conclusion","coefficient_norm"],"role":"reconstruction","value":"ordinary angular supremum/component-sum, normalized by j!"},{"path":["conclusion","same_waist_qualifications","complete_WGS_pair_admitted"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","complete_extended_first_amplitude_admitted"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","ordinary_radial_amplitude_derivatives_retained"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","original_physical_means_and_transported_input_retained"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_N_actual_angular_operator"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_SP_actual_waist_density_q_and_mean_records"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_SW_W_bound_before_waist_ng"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_WES_waist_free_neighbourhood_minus_T_gt_L"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_WT_Js_268435456_whole_forward_remainder"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_WZR_metric_beta_zero_at_waist"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_original_root_cutoff_97_input"],"role":"reconstruction","value":true},{"path":["conclusion","same_waist_qualifications","same_selected_real_member"],"role":"reconstruction","value":true},{"path":["conclusion","retained_independent_physical_mean"],"role":"reconstruction","value":true},{"path":["conclusion","metric_radial_derivatives_not_declared_zero"],"role":"reconstruction","value":true},{"path":["node_name"],"role":"free","value":"complete_free_waist_Airy_and_Schur_map"},{"path":["conclusion","Ai_and_Bi_real_remainders_retained"],"role":"free","value":true},{"path":["conclusion","all_low_outputs_means_and_two_physical_rows_retained"],"role":"free","value":true},{"path":["conclusion","cB_squared_and_first_Airy_cross_retained"],"role":"free","value":true},{"path":["conclusion","one_complete_common_bound_applies_to_each_listed_component"],"role":"free","value":true},{"path":["conclusion","original_root_matrix_not_treated_as_column_HS_error"],"role":"free","value":true},{"path":["conclusion","same_waist_density_factor_already_in_V_and_B"],"role":"free","value":true},{"path":["conclusion","same_reconstruction_node"],"role":"free","value":"complete_exact_waist_finite_reconstruction"},{"path":["conclusion","complete_tail_weights","Xi0_reference_sign_count"],"role":"free","value":4},{"path":["conclusion","complete_tail_weights","Xi2_input_sign_count"],"role":"free","value":2},{"path":["conclusion","complete_tail_weights","full_Bessel_weights_retained"],"role":"free","value":true},{"path":["conclusion","complete_tail_weights","no_root_scattering_matrix_Hilbert_Schmidt_sum"],"role":"free","value":true},{"path":["node_name"],"role":"endpoints","value":"complete_four_waist_endpoint_contributions"},{"path":["conclusion","WT_uses_the_whole_saved_forward_strong_remainder"],"role":"endpoints","value":true},{"path":["conclusion","no_first_finite_upper_subtracted_from_WT"],"role":"endpoints","value":true},{"path":["conclusion","original_Ni_and_final_waist_readout_not_applied_here"],"role":"endpoints","value":true},{"path":["conclusion","original_genuine_Cn_and_beta_n_retained"],"role":"endpoints","value":true},{"path":["conclusion","original_root_to_waist_mean_feedback_retained"],"role":"endpoints","value":true},{"path":["conclusion","physical_two_stored_means_retained_in_q_term"],"role":"endpoints","value":true},{"path":["conclusion","retained_true_finite_complement_and_parameter_rows"],"role":"endpoints","value":true},{"path":["conclusion","root_matrix_not_replaced_by_a_second_independent_column"],"role":"endpoints","value":true},{"path":["conclusion","scattering_input_matrix_order_retained"],"role":"endpoints","value":true},{"path":["conclusion","waist_ng_factor_in_WT_SW_product_count"],"role":"endpoints","value":1},{"path":["node_name"],"role":"extension","value":"extension_scalars"},{"path":["conclusion","Bext_negative_tail_retained"],"role":"extension","value":true},{"path":["current_target"],"role":"wrp","value":null},{"path":["automatic_retry_authorized"],"role":"wrp","value":false},{"path":["parameters","physical_period"],"role":"wrp","value":"pi/2"},{"path":["parameters","input_order"],"role":"wrp","value":[-4,3]},{"path":["parameters","original_true_interfaces"],"role":"wrp","value":3070},{"path":["parameters","physical_mean_coordinates"],"role":"wrp","value":2},{"path":["parameters","physical_mean_initial_condition"],"role":"wrp","value":"z_ph(r_star)=0"},{"path":["parameters","selected_original_real_member_only"],"role":"wrp","value":true},{"path":["parameters","fixed_intrinsic_eta0"],"role":"wrp","value":"-7789843107295549/4611686018427387904"},{"path":["current_target"],"role":"current","value":null},{"path":["automatic_retry_authorized"],"role":"current","value":false},{"path":["parameters","physical_period"],"role":"current","value":"pi/2"},{"path":["parameters","input_order"],"role":"current","value":[-4,3]},{"path":["parameters","original_true_interfaces"],"role":"current","value":3070},{"path":["parameters","physical_mean_coordinates"],"role":"current","value":2},{"path":["parameters","physical_mean_initial_condition"],"role":"current","value":"z_ph(r_star)=0"},{"path":["parameters","selected_original_real_member_only"],"role":"current","value":true},{"path":["parameters","fixed_intrinsic_eta0"],"role":"current","value":"-7789843107295549/4611686018427387904"},{"path":["actual_progress","new_records_saved"],"role":"wrp","value":40},{"path":["actual_progress","new_graphs_completed"],"role":"wrp","value":3},{"path":["retained_scope","all_fifteen_weight_entries_preserved"],"role":"wrp","value":true},{"path":["retained_scope","all_near_and_two_far_genuine_profiles_retained"],"role":"wrp","value":true},{"path":["retained_scope","full_Bessel_spaces_include_mean_and_all_zero_low_high_output_modes"],"role":"wrp","value":true},{"path":["retained_scope","full_signed_inputs_then_original_isometric_reflection_restriction"],"role":"wrp","value":true},{"path":["retained_scope","same_normalized_circle_measure_for_three_comparison_coordinates"],"role":"wrp","value":true},{"path":["retained_scope","profile_zero_order_copied_independently_not_reexpanded"],"role":"wrp","value":true},{"path":["actual_progress","new_records_saved"],"role":"current","value":52},{"path":["actual_progress","new_graphs_completed"],"role":"current","value":3},{"path":["actual_progress","original_record_copies_in_graphs"],"role":"current","value":62},{"path":["actual_progress","upstream_new_record_copies_in_graphs"],"role":"current","value":4},{"path":["retained_scope","all_four_waist_endpoints_retained"],"role":"current","value":true},{"path":["retained_scope","full_physical_Jr_and_Tk_fees_retained_readonly"],"role":"current","value":true},{"path":["retained_scope","old_local_mean_and_all_old_exponentials_readonly"],"role":"current","value":true},{"path":["retained_scope","no_saved_upper_subtraction"],"role":"current","value":true},{"path":["retained_scope","complete_genuine_root_matrix_beta_n_and_two_reference_roles_retained"],"role":"current","value":true},{"path":["complete_current_provider","record_source_kind"],"role":"current","value":"complete_successful_WRP_actual_only"},{"path":["complete_current_provider","same_operator_and_trial"],"role":"current","value":true}]''')
PROCESS_RECEIPT_KEYS = json.loads(r'''{"current":["kind","problem_id","complete","proved","stage","actual_returncode","arithmetic_bits","run_id","run_attempt","runtime","scientific_modules","manifest_sha256","actual_checkout_commit","workflow_event_commit","gates","actual_progress","completed_targets","saved_record_counts"],"endpoints":["kind","node_name","complete","failure","automatic_retry_authorized","printed_record_event_count","all_printed_records_in_complete_conclusion"],"extension":["kind","node_name","complete","failure","automatic_retry_authorized","printed_record_event_count","all_printed_records_in_complete_conclusion"],"free":["kind","node_name","complete","failure","automatic_retry_authorized","printed_record_event_count","all_printed_records_in_complete_conclusion"],"reconstruction":["kind","node_name","complete","failure","automatic_retry_authorized","printed_record_event_count","all_printed_records_in_complete_conclusion"],"wgs_copies":["kind","complete","complete_readonly_input_projection","run_id","run_attempt","source_sha256","math_module_sha256","input_manifest_sha256","actual_scientific_checkout_commit","workflow_event_commit","copy_counts","copied_complete_local_coefficients_sha256","copied_complete_original_scopes_sha256","copied_original_scalar_records_sha256","copied_original_stage_records_sha256"],"wgs_main":["kind","complete","proved","stage","actual_returncode","arithmetic_bits","run_id","run_attempt","runtime","source_sha256","math_module_sha256","input_manifest_sha256","actual_scientific_checkout_commit","workflow_event_commit","gates","actual_progress","planned_shape"],"wrp":["kind","problem_id","complete","proved","stage","actual_returncode","arithmetic_bits","run_id","run_attempt","runtime","scientific_modules","manifest_sha256","actual_checkout_commit","workflow_event_commit","gates","actual_progress","completed_targets","saved_record_counts"]}''')
ANCESTRY_REFERENCE_PATHS = json.loads(r'''{"current":[["accepted_old_inputs"],["input_sha256"],["parameters"],["complete_current_provider"],["whole_candidate_choices"]],"endpoints":[["binding"]],"extension":[["binding"]],"free":[["binding"]],"reconstruction":[["binding"]],"wgs_copies":[["original_input_sha256"],["local_coefficient_qualification"]],"wgs_main":[["accepted_original_inputs"],["input_sha256"],["verified_original_inputs"],["parameters"]],"wrp":[["accepted_old_inputs"],["input_sha256"],["parameters"],["copied_original_scopes"],["whole_candidate_choices"]]}''')
OLD_GRAPH_ORDERS = json.loads(r'''{"current":["strict_per_index_flux_mean","complete_physical_mean_and_four_waist_endpoints","complete_current_negative_and_whole_receiver"],"wrp":["complete_new_relative_phase_pullback_conclusion","complete_new_full_output_profile_weights_conclusion","complete_new_same_whole_receiver_conclusion"]}''')
OLD_GRAPH_COUNTS = json.loads(r'''{"current":{"complete_current_negative_and_whole_receiver":13,"complete_physical_mean_and_four_waist_endpoints":7,"strict_per_index_flux_mean":32},"wrp":{"complete_new_full_output_profile_weights_conclusion":15,"complete_new_relative_phase_pullback_conclusion":7,"complete_new_same_whole_receiver_conclusion":18}}''')
RECORD_SPECS = json.loads(r'''{"ABi1":{"endpoint":"upper","path":["conclusion","complete_reconstruction_and_map_records","complete_Bi_first_coefficients_two_sign_two_phase_sum_upper"],"role":"free"},"A_0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",0],"role":"wgs_main"},"A_1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",1],"role":"wgs_main"},"A_2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",2],"role":"wgs_main"},"A_3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",3],"role":"wgs_main"},"Airy_first":{"endpoint":"upper","path":["conclusion","complete_reconstruction_and_map_records","complete_Airy_first_cross_upper"],"role":"free"},"Airy_second":{"endpoint":"upper","path":["conclusion","complete_reconstruction_and_map_records","complete_Airy_second_remainder_upper"],"role":"free"},"Bessel":{"endpoint":"upper","path":["copied_original_scalar_records","Bessel_prefactor"],"role":"wrp"},"CB":{"endpoint":"upper","path":["conclusion","constants","complete_cB_upper"],"role":"extension"},"Calg":{"endpoint":"upper","path":["complete_new_graphs","complete_current_negative_and_whole_receiver","copied_original_records","provider_Calg"],"role":"current"},"Cs":{"endpoint":"upper","path":["conclusion","complete_new_constants","complete_root_scattering_Hminus4_3_to_L2_upper"],"role":"endpoints"},"D_infinity":{"endpoint":"upper","path":["complete_new_graphs","complete_current_negative_and_whole_receiver","copied_original_records","provider_D_infinity"],"role":"current"},"Fa_0":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",0],"role":"wgs_main"},"Fa_1":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",1],"role":"wgs_main"},"Fa_2":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",2],"role":"wgs_main"},"Fb_0":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",0],"role":"wgs_main"},"Fb_1":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",1],"role":"wgs_main"},"Fb_2":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",2],"role":"wgs_main"},"Ksym":{"endpoint":"upper","path":["conclusion","complete_reconstruction_and_map_records","complete_all_eight_symbol_components_upper"],"role":"free"},"Lrec":{"endpoint":"upper","path":["complete_new_graphs","complete_current_negative_and_whole_receiver","copied_original_records","provider_Lrec"],"role":"current"},"Q_0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",0],"role":"wgs_main"},"Q_1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",1],"role":"wgs_main"},"Q_2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",2],"role":"wgs_main"},"Q_3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",3],"role":"wgs_main"},"RF":{"endpoint":"upper","path":["complete_new_graphs","complete_current_negative_and_whole_receiver","copied_original_records","provider_RF"],"role":"current"},"Rplus":{"endpoint":"upper","path":["complete_new_graphs","complete_current_negative_and_whole_receiver","copied_original_records","provider_Rplus"],"role":"current"},"Rw":{"endpoint":"upper","path":["conclusion","new_complete_constants","complete_density_pair_operator_upper"],"role":"reconstruction"},"S23":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_two_thirds"],"role":"wrp"},"W00":{"endpoint":"upper","path":["complete_new_graphs","complete_new_full_output_profile_weights_conclusion","new_records","zero","angle_0"],"role":"wrp"},"W20":{"endpoint":"upper","path":["complete_new_graphs","complete_new_full_output_profile_weights_conclusion","new_records","two","angle_0"],"role":"wrp"},"WT":{"endpoint":"upper","path":["complete_new_graphs","complete_physical_mean_and_four_waist_endpoints","copied_original_records","old_endpoint_WT"],"role":"current"},"Xi0":{"endpoint":"upper","path":["conclusion","complete_tail_weights","new_complete_records","complete_Xi0_upper"],"role":"free"},"Xi2":{"endpoint":"upper","path":["conclusion","complete_tail_weights","new_complete_records","complete_Xi2_upper"],"role":"free"},"eta_inverse":{"endpoint":"upper","path":["conclusion","new_complete_constants","complete_waist_eta_inverse_upper"],"role":"reconstruction"},"free_a1_0":{"endpoint":"upper","path":["complete_free_first_transport_conclusion","complete_jets","a1","group_upper",0],"role":"wgs_main"},"free_a1_1":{"endpoint":"upper","path":["complete_free_first_transport_conclusion","complete_jets","a1","group_upper",1],"role":"wgs_main"},"free_a1_2":{"endpoint":"upper","path":["complete_free_first_transport_conclusion","complete_jets","a1","group_upper",2],"role":"wgs_main"},"free_b1_0":{"endpoint":"upper","path":["complete_free_first_transport_conclusion","complete_jets","b1","group_upper",0],"role":"wgs_main"},"free_b1_1":{"endpoint":"upper","path":["complete_free_first_transport_conclusion","complete_jets","b1","group_upper",1],"role":"wgs_main"},"free_b1_2":{"endpoint":"upper","path":["complete_free_first_transport_conclusion","complete_jets","b1","group_upper",2],"role":"wgs_main"},"mean_endpoint":{"endpoint":"upper","path":["complete_new_graphs","complete_physical_mean_and_four_waist_endpoints","new_records","complete_physical_mean_endpoint_upper"],"role":"current"},"negative":{"endpoint":"upper","path":["complete_new_graphs","complete_current_negative_and_whole_receiver","new_records","complete_same_negative_error_upper"],"role":"current"},"prior_reduced":{"endpoint":"upper","path":["whole_candidate_choices","reduced","selected_record"],"role":"current"},"prior_whole":{"endpoint":"upper","path":["whole_candidate_choices","whole","selected_record"],"role":"current"},"sqrt2":{"endpoint":"upper","path":["copied_original_scalar_records","sqrt_two_upper"],"role":"wrp"},"t_0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",0],"role":"wgs_main"},"t_1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",1],"role":"wgs_main"},"t_2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",2],"role":"wgs_main"},"t_3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",3],"role":"wgs_main"},"two16":{"endpoint":"upper","path":["copied_original_scalar_records","two_one_sixth_upper"],"role":"wrp"},"w0_0":{"endpoint":"upper","path":["conclusion","complete_amplitude_ports","w0","normalized_angular_coefficients",0],"role":"reconstruction"},"w0_1":{"endpoint":"upper","path":["conclusion","complete_amplitude_ports","w0","normalized_angular_coefficients",1],"role":"reconstruction"},"w0_2":{"endpoint":"upper","path":["conclusion","complete_amplitude_ports","w0","normalized_angular_coefficients",2],"role":"reconstruction"},"w0_3":{"endpoint":"upper","path":["conclusion","complete_amplitude_ports","w0","normalized_angular_coefficients",3],"role":"reconstruction"},"x_0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",0],"role":"wgs_main"},"x_1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",1],"role":"wgs_main"},"x_2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",2],"role":"wgs_main"},"x_3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",3],"role":"wgs_main"},"y_0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",0],"role":"wgs_main"},"y_1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",1],"role":"wgs_main"},"y_2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",2],"role":"wgs_main"},"y_3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",3],"role":"wgs_main"}}''')
SCOPE_SPECS = json.loads(r'''{"complete_extension":{"path":["conclusion"],"role":"extension"},"complete_free_waist_map":{"path":["conclusion"],"role":"free"},"complete_full_output_profile_weights":{"path":["complete_new_graphs","complete_new_full_output_profile_weights_conclusion"],"role":"wrp"},"complete_old_four_endpoints":{"path":["conclusion"],"role":"endpoints"},"complete_waist_reconstruction":{"path":["conclusion"],"role":"reconstruction"},"current_negative_and_whole":{"path":["complete_new_graphs","complete_current_negative_and_whole_receiver"],"role":"current"},"current_original_provider":{"path":["complete_current_provider"],"role":"current"},"current_physical_mean_and_endpoints":{"path":["complete_new_graphs","complete_physical_mean_and_four_waist_endpoints"],"role":"current"},"current_retained_scope":{"path":["retained_scope"],"role":"current"},"current_whole_choices":{"path":["whole_candidate_choices"],"role":"current"},"wgs_complete_original_companion":{"path":[],"role":"wgs_copies"},"wgs_derivative_certificate":{"path":["complete_derivative_request_certificate"],"role":"wgs_main"},"wgs_free_transport":{"path":["complete_free_first_transport_conclusion"],"role":"wgs_main"},"wgs_named_global_graph":{"path":["complete_named_global_graph_conclusion"],"role":"wgs_main"},"wgs_retained_scope":{"path":["retained_scope"],"role":"wgs_main"},"wgs_strict_forcing":{"path":["complete_strict_forcing_conclusion"],"role":"wgs_main"},"wgs_strict_geometry":{"path":["complete_strict_geometry_conclusion"],"role":"wgs_main"},"wrp_retained_scope":{"path":["retained_scope"],"role":"wrp"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"5360eba9d0ae6ad8b972463c822e865f65301c6c932fbddeac1b8c665bee8728"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''6935''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"c41471fd03761533701220befcacc61d3c236bf7ee5e2752330e004a00998e92"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''11111''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"679dbf1bc08d339614949345279ae37bbadcb6574e825e51b19ecbe771195d25"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''23768''')
PARAMETERS = json.loads(r'''{"arithmetic_bits":320,"complete_current_input_files":12,"complete_old_input_files":8,"complete_original_scope_context_count":18,"complete_physical_mean_and_negative_receiver_provider":"WSMF_run_43886938106_1","complete_reference_sign_Sinverse_and_primitive_prefactor":"51/10","decimal_record_digits":75,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","fixed_intrinsic_parameter":"eta_0","free_waist_t_lower":"1/2000","history_inputs":0,"immutable_AST_files":2,"input_order":[-4,3],"minimum_physical_frequency":388,"new_ODE_solutions":0,"new_exponentials":0,"new_fractional_powers":0,"new_graph_count":4,"new_graph_record_counts":[12,6,6,7],"new_logarithms":0,"new_profile_window":[1,1],"new_quadratures":0,"new_record_count":31,"new_square_roots":1,"new_terminal_ordinary_angular_orders":{"T1":[0,1],"T2":[0,1,2]},"old_angular_group_orders_used":[0,1,2,3],"old_complete_forcing_angular_orders_used":[0,1,2],"old_free_first_angular_orders_used":[0,1,2],"old_profile_windows_used":[[0,1],[2,1]],"old_targets_recomputed":0,"original_PW_cut":"2333968743003/10000000000000","original_record_count":62,"original_true_interfaces":3070,"physical_frequency":"n=4|j|","physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","private_finite_positive_jets_are_only_new_terminal_intermediates":true,"root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"],"terminal_band_decay":"N^(-2)","waist_rho_negative_fourth_rational_upper":"2"}''')
RETAINED_SCOPE = json.loads(r'''{"actual_96_columns_signed_normalization_Theta_nu_radial_heads_cokernels_and_seven_ports_retained":true,"all_four_endpoints_complete_WT_ng_once_and_current_mean_retained":true,"auxiliary_mean_not_declared_zero_and_physical_mean_not_deleted":true,"both_stored_density_means_and_true_root_initial_condition_retained":true,"complete_extended_B_tail_and_cB_input_dependence_separated":true,"complete_original_FA_B0_B1_and_Airy_remainders_readonly":true,"current_negative_ordinary_sources_all_3070_true_jumps_and_terminal_unchanged":true,"fixed_multiplier_Hminus1_Hminus2_paid_with_all_required_derivatives":true,"full_Bessel_measure_zero_low_high_outputs_and_original_reflection_retained":true,"full_beta_r_d_r_Jr_and_original_forcing_retained":true,"no_new_smallness_or_actual_finite_inverse_claimed":true,"no_old_total_upper_subtracted":true,"old_candidate_wins_equal_saved_upper":true,"old_scientific_calls":0,"old_targets_recomputed":0,"original_failed_ancestors_not_relabelled_success":true,"positive_root_finite_fee_and_ordered_final_readout_retained":true,"same_original_Jwaist_equals_eta_inverse_I_after_actual_parity_assembly":true,"same_original_projection_on_BFV_retained_and_P1":true,"same_profile_interpolation_and_right_Sinverse_only":true,"same_selected_actual_real_waist_and_original_family":true,"same_whole_and_reduced_compared_only_to_their_own_complete_current_selected_records":true,"true_free_neighbourhood_T_less_than_minus_1_over_2000":true,"two_free_reference_columns_and_genuine_root_normalization_retained":true,"waist_beta_d_qr_zero_not_extended_to_radial_derivatives":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_fixed_waist_terminal_coefficients","complete_full_primitive_terminal_reception","complete_free_map_and_two_endpoint_bounds","complete_four_endpoints_and_same_whole_errors"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_fixed_waist_terminal_coefficients":{"complete":true,"fixed_amplitudes_separated_from_cB_input_scalar":true,"full_original_forcing_and_tail_retained":true,"kind":"complete_fixed_waist_terminal_coefficients_v1","new_records":{"T1_cB_ordinary_0_upper":{"ball":"__FINITE_SCALAR__"},"T1_cB_ordinary_1_upper":{"ball":"__FINITE_SCALAR__"},"T1_free_ordinary_0_upper":{"ball":"__FINITE_SCALAR__"},"T1_free_ordinary_1_upper":{"ball":"__FINITE_SCALAR__"},"T2_cB_ordinary_0_upper":{"ball":"__FINITE_SCALAR__"},"T2_cB_ordinary_1_upper":{"ball":"__FINITE_SCALAR__"},"T2_cB_ordinary_2_upper":{"ball":"__FINITE_SCALAR__"},"T2_free_ordinary_0_upper":{"ball":"__FINITE_SCALAR__"},"T2_free_ordinary_1_upper":{"ball":"__FINITE_SCALAR__"},"T2_free_ordinary_2_upper":{"ball":"__FINITE_SCALAR__"},"complete_T1_Hminus1_multiplier_upper":{"ball":"__FINITE_SCALAR__"},"complete_T2_Hminus2_multiplier_upper":{"ball":"__FINITE_SCALAR__"}},"normalized_jet_to_ordinary_factorial_once":true,"old_supremum_bounds_not_relabelled_Wiener":true,"ordinary_physical_angular_derivatives":true,"same_selected_real_waist":true},"complete_four_endpoints_and_same_whole_errors":{"all_3070_jumps_original_lengths_and_PW_windows_retained":true,"all_four_original_endpoints_and_both_physical_means_retained":true,"complete":true,"complete_current_negative_receiver_copied":true,"kind":"complete_four_endpoints_and_same_whole_errors_v1","new_records":{"complete_all_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_four_waist_endpoints_flux_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonroot_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_reduced_received_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_reduced_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_whole_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_whole_received_source_upper":{"ball":"__FINITE_SCALAR__"}},"no_new_finite_inverse_or_seven_port_obligation_discharged":true,"ordered_final_readout_and_root_factor_retained":true,"ordinary_physical_angular_derivatives":true,"same_selected_real_waist":true,"whole_and_reduced_same_operators_compared_separately":true},"complete_free_map_and_two_endpoint_bounds":{"complete":true,"complete_cB_squared_and_first_Airy_cross_retained":true,"complete_root_scattering_matrix_order_retained":true,"kind":"complete_free_map_and_two_endpoint_bounds_v1","new_records":{"complete_free_map_L2_to_density_flux_upper":{"ball":"__FINITE_SCALAR__"},"complete_retained_first_two_Airy_remainder_upper":{"ball":"__FINITE_SCALAR__"},"complete_scattering_endpoint_flux_upper":{"ball":"__FINITE_SCALAR__"},"complete_second_order_Bi_first_cross_upper":{"ball":"__FINITE_SCALAR__"},"complete_second_order_endpoint_flux_upper":{"ball":"__FINITE_SCALAR__"},"complete_second_order_remainder_times_Ninfinity_upper":{"ball":"__FINITE_SCALAR__"}},"old_Airy_first_and_second_are_complete_for_retained_polynomial":true,"old_density_factor_not_multiplied_twice":true,"ordinary_physical_angular_derivatives":true,"original_projection_retained_before_first_cancellation":true,"same_original_FA_B0_B1_identity":true,"same_selected_real_waist":true},"complete_full_primitive_terminal_reception":{"complete":true,"complete_band_decay":"N^(-2)","free_to_genuine_Sinverse_on_input_side":true,"full_zero_low_high_output_modes_and_both_reference_inputs":true,"kind":"complete_full_primitive_terminal_reception_v1","new_records":{"complete_constant_profile_Hminus1_upper":{"ball":"__FINITE_SCALAR__"},"complete_first_primitive_band_upper":{"ball":"__FINITE_SCALAR__"},"complete_second_primitive_band_upper":{"ball":"__FINITE_SCALAR__"},"complete_two_primitive_Hminus4_3_input_upper":{"ball":"__FINITE_SCALAR__"},"complete_two_primitive_L2_input_upper":{"ball":"__FINITE_SCALAR__"},"complete_two_primitive_band_upper":{"ball":"__FINITE_SCALAR__"}},"new_root_matrix_column_HS":false,"ordinary_physical_angular_derivatives":true,"original_isometric_reflection_and_two_far_terms_counted_once":true,"same_complete_profile_operator_interpolated":true,"same_selected_real_waist":true}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_fixed_waist_terminal_coefficients":12,"complete_four_endpoints_and_same_whole_errors":7,"complete_free_map_and_two_endpoint_bounds":6,"complete_full_primitive_terminal_reception":6}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_fixed_waist_terminal_coefficients":12,"complete_four_endpoints_and_same_whole_errors":7,"complete_free_map_and_two_endpoint_bounds":6,"complete_full_primitive_terminal_reception":6}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":8,"complete_original_scope_contexts_verified":18,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":4,"new_logarithms":0,"new_quadratures":0,"new_records_saved":31,"new_square_roots":1,"new_whole_comparisons_completed":2,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_record_objects_copied":62,"original_records_copied_in_graphs":0}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"complete_original_scope_contexts_verified":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","current_input_and_AST_identity","eight_complete_original_actual_files_byte_identical","complete_original_WGS_pair_low_angular_free_transport_scope","complete_original_waist_primitive_reference_and_remainder_scope","complete_current_full_profile_and_WSMF_provider_binding","all_62_scalar_objects_and_18_complete_scope_references_retained","same_full_endpoint_Bessel_input_and_physical_mean_units","complete_fixed_waist_terminal_coefficients","complete_full_primitive_terminal_reception","complete_free_map_and_two_endpoint_bounds","complete_four_endpoints_and_same_whole_errors","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","copied_original_scalar_records","complete_original_scope_references","complete_new_graphs","whole_candidate_choices","current_target","completed_targets","saved_record_counts","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized"]''')
ACCEPTED_STATIC_QUALIFICATIONS = json.loads(r'''{"all_39_previous_free_records_retained_in_complete_52_slot_conclusion":true,"complete":true,"complete_current_WSMF_18_gates_52_targets_verified":true,"complete_original_WGS_pair_24_gates_437_targets_verified":true,"complete_original_WRP_14_gates_40_targets_verified":true,"complete_original_contexts_byte_bound_without_projecting_away_fields":true,"complete_original_free_remaining_13_and_endpoint_8_targets_verified":true,"complete_original_reconstruction_133_and_extension_104_targets_verified":true,"complete_scope_context_references_retained":18,"current_whole_and_reduced_selected_objects_verified":true,"history_inputs_restored":0,"kind":"complete_original_waist_flux_endpoint_inputs_readonly_admission_v1","old_producer_imports_or_calls":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_parent_438277_failure_not_relabelled_success":true,"same_free_first_amplitude_distinct_from_extended_tail":true,"same_full_reference_sign_profile_and_physical_mean_scope":true,"same_old_B0_B1_Airy_and_root_scattering_identities_retained":true}''')

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
    result = copy.deepcopy(ACCEPTED_STATIC_QUALIFICATIONS)
    result.update({
        "complete_original_file_receipts": [
            copy.deepcopy(files[spec["role"]]) for spec in EXPECTED_OLD_FILES],
        "complete_original_schema_fields": {
            role: sorted(old) for role, old in docs.items()},
        "complete_original_qualification_identities": {
            role: {"bytes": len(canonical(original_qualifications(old))),
                   "sha256": digest(canonical(original_qualifications(old)))}
            for role, old in docs.items()},
        "complete_original_process_bindings": {
            role: {key: copy.deepcopy(old[key])
                   for key in PROCESS_RECEIPT_KEYS[role]}
            for role, old in docs.items()},
        "complete_original_ancestry_references": {
            role: [complete_object_reference(docs, role, path)
                   for path in ANCESTRY_REFERENCE_PATHS[role]]
            for role in docs}})
    return result


def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(len(manifest_raw) < 100000 and digest(manifest_raw) == manifest_sha,
            "complete manifest CLI identity")
    manifest = exact_json(manifest_raw)
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_WEX", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 12
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 12,
            "twelve complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "complete old input pin differs")
    require(same_json(files["proof_WEX"], EXPECTED_PROOF), "published WEX proof pin")
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
                "complete original schema or canonical bytes differ: " + role)
        body = canonical(original_qualifications(old))
        expected = OLD_QUALIFICATION_IDENTITIES[role]
        require(len(body) == expected["bytes"] and digest(body) == expected["sha256"],
                "complete original non-ball fields and array positions: " + role)
    # These are role-specific original fields, never defaulted or invented.
    # In particular WGS has no physical_period field and extension.conclusion
    # has no complete field. The complete envelope is checked instead.
    for item in OLD_LITERAL_ASSERTIONS:
        require(same_json(at(docs[item["role"]], item["path"]), item["value"]),
                "original literal differs: " + item["role"] + "/" + "/".join(
                    str(key) for key in item["path"]))
    for role, names in OLD_GATE_LABELS.items():
        require(same_json(docs[role]["gates"],
                         [{"name": name, "passed": True} for name in names]),
                "all original ordered success gates")
    for role, names in OLD_GRAPH_ORDERS.items():
        old = docs[role]
        require(same_json(old["completed_targets"], names)
                and same_json(old["saved_record_counts"], OLD_GRAPH_COUNTS[role])
                and set(old["complete_new_graphs"]) == set(names),
                "original complete graph order and counters")
        for name in names:
            graph = old["complete_new_graphs"][name]
            require(graph["complete"] is True
                    and scalar_record_count(graph["new_records"]) == OLD_GRAPH_COUNTS[role][name],
                    "complete original new-record graph")
    gm, gc = docs["wgs_main"], docs["wgs_copies"]
    require(same_json(gm["complete_original_inputs_file"], {
                "filename": "complete-original-inputs.json",
                "bytes": files["wgs_copies"]["bytes"],
                "sha256": files["wgs_copies"]["sha256"]}),
            "WGS complete companion file identity")
    for key in ("source_sha256", "math_module_sha256", "input_manifest_sha256",
                "run_id", "run_attempt", "actual_scientific_checkout_commit",
                "workflow_event_commit"):
        require(same_json(gm[key], gc[key]), "WGS pair original runtime binding")
    require(same_json(gm["input_sha256"], gc["original_input_sha256"])
            and gm["parameters"]["exact_strict_interval"] == PARAMETERS["strict_interval"]
            and gm["parameters"]["exact_root_interval"] == PARAMETERS["root_interval"],
            "WGS original same strict and local real intervals")
    for key in ("copied_complete_local_coefficients", "copied_complete_original_scopes",
                "copied_original_scalar_records", "copied_original_stage_records"):
        require(digest(canonical(gc[key])) == gc[key + "_sha256"],
                "complete original WGS companion object identity")
    require(sum(gm["planned_shape"]["new_graph_slot_counts"].values()) == 437,
            "complete original WGS planned slots")
    for name, count in gm["planned_shape"]["new_graph_slot_counts"].items():
        require(isinstance(gm[name], dict) and scalar_record_count(gm[name]) == count,
                "complete original WGS graph and all saved slots")
    # Earlier complete nodes retain their own binding. A later failed parent
    # is never relabelled a successful run, and the remaining-run bindings
    # are distinct from the original five-module parent binding.
    for role, count in (("reconstruction", 133), ("extension", 104),
                        ("free", 52), ("endpoints", 8)):
        old = docs[role]
        require(scalar_record_count(old["conclusion"]) == count,
                "complete original node slot count")
        inputs = old["binding"]["mathematical_input_sha256"]
        require(inputs["WGS_main"] == files["wgs_main"]["sha256"]
                and inputs["WGS_original_inputs"] == files["wgs_copies"]["sha256"],
                "original node WGS pair binding")
    for key in ("mathematical_input_sha256", "parameters_sha256", "scientific_module_sha256"):
        require(same_json(docs["reconstruction"]["binding"][key],
                          docs["extension"]["binding"][key]),
                "same original reconstruction and extension family")
        require(same_json(docs["free"]["binding"][key],
                          docs["endpoints"]["binding"][key]),
                "same remaining-run free map and endpoint family")
    old_inputs = docs["extension"]["binding"]["mathematical_input_sha256"]
    free_inputs = docs["free"]["binding"]["mathematical_input_sha256"]
    require(all(free_inputs[key] == value for key, value in old_inputs.items())
            and free_inputs["prior_waist_reconstruction"] == files["reconstruction"]["sha256"]
            and free_inputs["prior_extension"] == files["extension"]["sha256"],
            "remaining run retained every original input and both actual predecessor nodes")
    require(same_json(docs["endpoints"]["binding"]["direct_dependency_receipts"], {
        "complete_free_waist_Airy_and_Schur_map": {
            "file": "graphs/complete_free_waist_Airy_and_Schur_map.json",
            "bytes": files["free"]["bytes"], "sha256": files["free"]["sha256"]}}),
        "complete endpoint direct free-map receipt")
    wr, current = docs["wrp"], docs["current"]
    provider = current["complete_current_provider"]
    require(same_json(provider["source_identity"], files["wrp"]),
            "current successful complete WRP provider identity")
    for key, value in provider["complete_runtime_binding"].items():
        require(same_json(wr[key], value), "complete provider runtime and selected scope")
    current_receipts = {p["role"]: p for p in current["verified_original_inputs"]}
    for role in ("wgs_main", "wgs_copies", "wrp", "extension"):
        require(same_json(current_receipts[role], files[role]),
                "current provider uses the same complete actual input")
    for role in ("wrp", "current"):
        old = docs[role]
        require(old["parameters"]["strict_interval"] == PARAMETERS["strict_interval"]
                and old["parameters"]["root_interval"] == PARAMETERS["root_interval"]
                and old["parameters"]["original_PW_cut"] == PARAMETERS["original_PW_cut"],
                "same complete waist and physical-source intervals")
    current_receiver = current["complete_new_graphs"]["complete_current_negative_and_whole_receiver"]
    require(same_json(current_receiver["complete_current_provider_identity"], files["wrp"]),
            "complete negative receiver provider pin")
    old_record_map = wr["copied_original_scalar_records"]
    for alias in ("Rplus", "RF", "Calg", "D_infinity", "Lrec"):
        require(same_json(current_receiver["copied_original_records"]["provider_" + alias],
                          old_record_map[alias]), "same original ordered whole source factor")
    old_endpoints = docs["endpoints"]["conclusion"]["complete_four_endpoint_records"]
    old_mean_copy = current["complete_new_graphs"][
        "complete_physical_mean_and_four_waist_endpoints"]["copied_original_records"]
    for alias, key in (
        ("old_endpoint_WT", "complete_old_waist_normalizer_endpoint_upper"),
        ("old_endpoint_scattering", "complete_scattering_endpoint_upper"),
        ("old_endpoint_second_order", "complete_second_order_endpoint_upper")):
        require(same_json(old_mean_copy[alias], old_endpoints[key]),
                "same original complete nonmean endpoint")
    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 62 and all(
                spec["endpoint"] == "upper" for spec in RECORD_SPECS.values())
            and all(isinstance(v, dict) and set(v) == {"ball"} and isinstance(v["ball"], str)
                    for v in records.values())
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all sixty-two complete old scalar objects")
    for which in ("whole", "reduced"):
        choice = current["whole_candidate_choices"][which]
        require(choice["both_complete_candidates_retained"] is True
                and choice["old_wins_equal_upper"] is True and choice["same_operator_only"] is True
                and choice["operator"] == ("whole" if which == "whole"
                    else "reduced_after_exact_finite_factor_separation")
                and choice["selected"] == "new_complete_strict_flux_mean"
                and same_json(choice["selected_record"], at(current, choice["selected_record_path"]))
                and same_json(choice["old_complete_record"], at(current, choice["old_complete_record_path"]))
                and same_json(choice["current_provider_identity"], files["wrp"])
                and same_json(records["prior_" + which], choice["selected_record"]),
                "exact complete current same-operator selected record")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        body = canonical(at(docs[spec["role"]], spec["path"]))
        scopes[name] = {
            "source_role": spec["role"], "source_json_path": copy.deepcopy(spec["path"]),
            "complete_context_bytes": len(body), "complete_context_sha256": digest(body),
            "complete_original_context_without_projection": True,
            "original_file_identity": copy.deepcopy(files[spec["role"]])}
    require(len(scopes) == 18 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "eighteen complete original context references without field deletion")
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

def ex(value):
    """Exact integer constants for the finite positive polynomial."""
    require(type(value) is int, "exact integer constant")
    return arb(str(value))


def graph_record(graphs, name, path):
    require(name in graphs and graphs[name]["complete"] is True,
            "complete saved predecessor graph")
    return saved_upper(at(graphs[name]["new_records"], path))



"""WEX: 31 new complete scalar targets; no entry point.

The owner supplies ex, require, saved_upper, graph_record, and emit.
All public targets are atomically saved and read back by emit before
a successor reads their upper endpoints. The finite private positive
jets below evaluate only the new exact terminal amplitudes; no old
producer or completed scalar target is called.
"""

def wex_constant(value, order):
    return [value] + [ex(0) for _ in range(order)]


def wex_add(order, *arrays):
    require(all(len(a) >= order + 1 for a in arrays), "unpaid angular jet in sum")
    return [sum((a[j] for a in arrays), ex(0)) for j in range(order + 1)]


def wex_scale(value, array):
    return [value * x for x in array]


def wex_multiply(order, *arrays):
    require(all(len(a) >= order + 1 for a in arrays), "unpaid angular jet in product")
    result = wex_constant(ex(1), order)
    for array in arrays:
        result = [sum((result[k] * array[j-k] for k in range(j+1)), ex(0))
                  for j in range(order + 1)]
    return result


def wex_derivative(array, order):
    require(len(array) >= order + 2, "unpaid angular derivative")
    return [ex(j+1) * array[j+1] for j in range(order+1)]


def wex_D(A, array, order):
    return wex_derivative(wex_multiply(order+1, A, array), order)


def wex_inverse_power_majorant(t, order, a):
    # t >= tau=1/2000 on the selected actual free waist.
    # The common zeroth fee 2000 also bounds tau^(-1/2).
    # This is finite normalized Faà di Bruno algebra, no arb power call.
    require(len(t) >= order+1, "unpaid t derivative")
    delta = [ex(0)] + [ex(2000)*t[j] for j in range(1, order+1)]
    power = wex_constant(ex(1), order)
    result = wex_constant(ex(1), order)
    coefficient = ex(1)
    for k in range(1, order+1):
        power = wex_multiply(order, power, delta)
        coefficient = coefficient * (a+ex(k-1)) / ex(k)
        result = wex_add(order, result, wex_scale(coefficient, power))
    return wex_scale(ex(2000), result)


def complete_fixed_waist_terminal_coefficients(saved, graphs, emit):
    def old_jet(alias, order):
        return [saved_upper(saved[alias+"_"+str(j)]) for j in range(order+1)]
    A, Q, t, x, y = (old_jet(k, 3) for k in ("A", "Q", "t", "x", "y"))
    w0 = old_jet("w0", 3)
    w1 = wex_add(2, old_jet("free_a1", 2), old_jet("free_b1", 2))
    Fa, Fb = old_jet("Fa", 2), old_jet("Fb", 2)
    tinv = wex_inverse_power_majorant(t, 3, ex(1))
    thalf = wex_inverse_power_majorant(t, 2, ex(1)/ex(2))
    KT = wex_add(3, wex_constant(ex(1), 3), t)
    C = wex_multiply(3, Q, KT)
    Delta = wex_scale(ex(1)/ex(4), wex_multiply(3, Q,
        wex_add(3, wex_scale(ex(2), wex_multiply(3, x, tinv)),
                y, wex_multiply(3, y, tinv))))
    tail = wex_multiply(2, thalf, KT, w0)
    forcing = wex_scale(ex(1)/ex(2), wex_multiply(2, Q,
        wex_add(2, x, wex_multiply(2, x, tinv), wex_scale(ex(2), y)),
        wex_add(2, Fa, Fb)))
    eta = saved_upper(saved["eta_inverse"])
    Cw0 = wex_multiply(3, C, w0)
    D2Cw0 = wex_D(A, wex_D(A, Cw0, 2), 1)
    D2w0 = wex_D(A, wex_D(A, w0, 2), 1)
    T10 = wex_add(1, wex_scale(eta, wex_add(1, D2Cw0,
        wex_D(A, wex_multiply(2, C, w1), 1),
        wex_D(A, wex_multiply(2, A, Delta, w0), 1))),
        D2w0, wex_D(A, w1, 1))
    T11 = wex_add(1,
        wex_scale(eta, wex_D(A, wex_multiply(2, C, tail), 1)),
        wex_D(A, tail, 1))
    T20 = wex_scale(eta, wex_add(2, wex_multiply(2, Delta, w1),
        forcing, wex_D(A, wex_multiply(3, Delta, w0), 2)))
    T21 = wex_scale(eta, wex_multiply(2, Delta, tail))
    paid = {}
    for prefix, array in (("T1_free", T10), ("T1_cB", T11),
                          ("T2_free", T20), ("T2_cB", T21)):
        row = []
        for j, value in enumerate(array):
            factorial = 2 if j == 2 else 1
            row.append(saved_upper(emit(prefix+"_ordinary_"+str(j)+"_upper",
                                        ex(factorial)*value)))
        paid[prefix] = row
    CB, sqrt2 = saved_upper(saved["CB"]), saved_upper(saved["sqrt2"])
    emit("complete_T1_Hminus1_multiplier_upper",
         paid["T1_free"][0]+paid["T1_free"][1]
         +CB*(paid["T1_cB"][0]+paid["T1_cB"][1]))
    emit("complete_T2_Hminus2_multiplier_upper",
         paid["T2_free"][0]+sqrt2*paid["T2_free"][1]+paid["T2_free"][2]
         +CB*(paid["T2_cB"][0]+sqrt2*paid["T2_cB"][1]+paid["T2_cB"][2]))


def complete_full_primitive_terminal_reception(saved, graphs, emit):
    first = "complete_fixed_waist_terminal_coefficients"
    M1 = graph_record(graphs, first, ["complete_T1_Hminus1_multiplier_upper"])
    M2 = graph_record(graphs, first, ["complete_T2_Hminus2_multiplier_upper"])
    W1 = saved_upper(emit("complete_constant_profile_Hminus1_upper",
        (saved_upper(saved["W00"])*saved_upper(saved["W20"])).sqrt()))
    factor = (ex(51)/ex(10))*saved_upper(saved["Rw"])
    K1 = saved_upper(emit("complete_first_primitive_band_upper", factor*W1*M1))
    K2 = saved_upper(emit("complete_second_primitive_band_upper",
        factor*saved_upper(saved["two16"])*saved_upper(saved["W20"])*M2))
    total = saved_upper(emit("complete_two_primitive_band_upper", K1+K2))
    emit("complete_two_primitive_L2_input_upper",
         (ex(4)/(ex(3)*ex(388)**2))*total)
    emit("complete_two_primitive_Hminus4_3_input_upper",
         saved_upper(saved["Bessel"])*saved_upper(saved["S23"])*total)


def complete_free_map_and_two_endpoint_bounds(saved, graphs, emit):
    prior = "complete_full_primitive_terminal_reception"
    ET0 = graph_record(graphs, prior, ["complete_two_primitive_L2_input_upper"])
    ETH = graph_record(graphs, prior, ["complete_two_primitive_Hminus4_3_input_upper"])
    airy = saved_upper(emit("complete_retained_first_two_Airy_remainder_upper",
                           saved_upper(saved["Airy_first"])+saved_upper(saved["Airy_second"])))
    free = saved_upper(emit("complete_free_map_L2_to_density_flux_upper",
        saved_upper(saved["Ksym"])+ET0+airy*saved_upper(saved["Xi0"])))
    emit("complete_scattering_endpoint_flux_upper", free*saved_upper(saved["Cs"]))
    first = saved_upper(emit("complete_second_order_remainder_times_Ninfinity_upper",
        (ex(1)+saved_upper(saved["CB"])/ex(388))
        *(ETH+airy*saved_upper(saved["Xi2"]))))
    cross = saved_upper(emit("complete_second_order_Bi_first_cross_upper",
        saved_upper(saved["CB"])*saved_upper(saved["ABi1"])*saved_upper(saved["Xi2"])))
    emit("complete_second_order_endpoint_flux_upper", first+cross)


def complete_four_endpoints_and_same_whole_errors(saved, graphs, emit):
    prior = "complete_free_map_and_two_endpoint_bounds"
    scattering = graph_record(graphs, prior, ["complete_scattering_endpoint_flux_upper"])
    second = graph_record(graphs, prior, ["complete_second_order_endpoint_flux_upper"])
    endpoints = saved_upper(emit("complete_four_waist_endpoints_flux_upper",
        scattering+second+saved_upper(saved["WT"])+saved_upper(saved["mean_endpoint"])))
    nonroot = saved_upper(emit("complete_nonroot_source_sum_upper",
        saved_upper(saved["Rplus"])+saved_upper(saved["negative"])+endpoints))
    allsource = saved_upper(emit("complete_all_source_sum_upper",
                                 nonroot+saved_upper(saved["RF"])))
    whole_received = saved_upper(emit("complete_whole_received_source_upper",
                                      saved_upper(saved["Lrec"])*allsource))
    emit("complete_same_whole_error_upper", saved_upper(saved["Calg"])+whole_received)
    reduced_received = saved_upper(emit("complete_reduced_received_source_upper",
                                        saved_upper(saved["Lrec"])*nonroot))
    emit("complete_same_reduced_error_upper",
         saved_upper(saved["D_infinity"])+reduced_received)

# The owner compares the two final complete operators separately with their
# own currently selected WSMF records. Old wins an equal saved upper endpoint.


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
            "complete_original_scope_references_sha256": ORIGINAL_SCOPE_SHA,
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
        "copied_original_scalar_records": {}, "complete_original_scope_references": {},
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
            if name == ORDERED_GRAPH_NAMES[1] and path == ["complete_constant_profile_Hminus1_upper"]:
                doc["actual_progress"]["new_square_roots"] += 1
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
        doc["complete_original_scope_references"] = copy.deepcopy(work["scopes"])
        doc["actual_progress"]["complete_original_files_admitted"] = 8
        doc["actual_progress"]["original_record_objects_copied"] = 62
        doc["actual_progress"]["complete_original_scope_contexts_verified"] = 18
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
            require(spec["endpoint"] == "upper", "original complete norm upper")
            saved_upper(saved[alias])
        require(PARAMETERS["minimum_physical_frequency"] == 388
                and PARAMETERS["free_waist_t_lower"] == "1/2000"
                and PARAMETERS["terminal_band_decay"] == "N^(-2)"
                and PARAMETERS["input_order"] == [-4, 3],
                "same complete physical input and new two-primitive band units")
        gate(GATE_LABELS[7])
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        operations = (
            ("complete_fixed_waist_terminal_coefficients", complete_fixed_waist_terminal_coefficients),
            ("complete_full_primitive_terminal_reception", complete_full_primitive_terminal_reception),
            ("complete_free_map_and_two_endpoint_bounds", complete_free_map_and_two_endpoint_bounds),
            ("complete_four_endpoints_and_same_whole_errors", complete_four_endpoints_and_same_whole_errors))
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
                "prior_source_role": "current",
                "prior_source_record_path": copy.deepcopy(RECORD_SPECS["prior_" + which]["path"]),
                "prior_record_path": prior_path, "new_record_path": new_path,
                "selected_label": ("new_complete_exact_waist_flux_candidate"
                                   if use_new else "prior_selected_complete_candidate"),
                "selected_record_path": new_path if use_new else prior_path,
                "complete_selected_upper": copy.deepcopy(new_record if use_new else old_record)}
            doc["actual_progress"]["new_whole_comparisons_completed"] += 1
            doc["stage"] = "complete_same_" + which + "_choice_saved"
            publish()
        gate(GATE_LABELS[12])
        for role, spec in work["files"].items():
            require(check_file(work["root"], spec) == work["raw"][role],
                    "current input changed during new scalar work")
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "manifest changed during new scalar work")
        gate(GATE_LABELS[13])
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
                and digest(canonical(doc["complete_original_scope_references"])) == ORIGINAL_SCOPE_SHA,
                "complete new graph and actual progress")
        gate(GATE_LABELS[14])
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
            "message_truncated": message_cut, "traceback_truncated": trace_cut,
            "full_text_in_job_log": True}
        publish(check_size=False)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
