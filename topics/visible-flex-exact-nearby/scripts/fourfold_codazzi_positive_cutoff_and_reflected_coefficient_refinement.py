#!/usr/bin/env python3
"""Two new complete scalar refinements from five frozen successful receipts.
WPC keeps the original positive trial and pays its actual output window.
WCE keeps the same reflected coefficient operator and complete mean ranks.
No old scientific producer, profile, integral, or completed product is run.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import time
import traceback
from flint import arb, ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
SOURCE="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_cutoff_and_reflected_coefficient_refinement.py"
WORKER="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_cutoff_and_reflected_coefficient_public_worker.py"
KIND="complete_positive_cutoff_and_reflected_coefficient_refinement_v1"
MANIFEST_KIND="positive_cutoff_and_reflected_coefficient_refinement_public_inputs_v1"
RUNTIME=json.loads("{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"}")
GATE_COUNT=22
COMPLETE_SCIENCE_MAX_BYTES=75000
PIN_SPECS=json.loads("{\"pc_execution\":{\"bytes\":46253,\"git_blob\":\"c32b8e3f3aca08d338784504c2cce5054d203bc6\",\"path\":\"topics/visible-flex-exact-nearby/notes/genuine_positive_Ai_cutoff_strong_correction_ci/run-43740173506-1/execution.json\",\"sha256\":\"75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817\"},\"sei_execution\":{\"bytes\":46192,\"git_blob\":\"e1532b816ea344ee65e52a503279376a0c449299\",\"path\":\"topics/visible-flex-exact-nearby/notes/individual_principal_energy_terminal_density_ci/run-43773319871-1/execution.json\",\"sha256\":\"b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29\"},\"tf_science\":{\"bytes\":18206,\"git_blob\":\"3766aea85aba59230be3813b4b7634d318316e49\",\"path\":\"topics/visible-flex-exact-nearby/notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json\",\"sha256\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\"},\"wce_contract\":{\"bytes\":22798,\"git_blob\":\"7519a36a72fe5775de8dcacb7812f48a42e73d3b\",\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-complete-physical-coefficient-error-from-terminal-bounds.md\",\"sha256\":\"3d77e17b15a2dd37c7c66d969d28c50edc5dcbaa7608d6686477ac322ebc0bcf\"},\"wpc_contract\":{\"bytes\":16086,\"git_blob\":\"92f5e51af2af959794b527c89d03f103d9e69422\",\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-complete-positive-cutoff-in-its-actual-output-window.md\",\"sha256\":\"2bc45c4c67261986bf2e94bb889d20757be8c713c31542c6a08e1da4353f8468\"},\"wt_science\":{\"bytes\":27619,\"git_blob\":\"b742d3167f68c05ef197450a3112eb5b8edcacac\",\"path\":\"topics/visible-flex-exact-nearby/notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json\",\"sha256\":\"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d\"},\"wx_execution\":{\"bytes\":43753,\"git_blob\":\"5121a599896025d90e2861450756a256aaba659d\",\"path\":\"topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json\",\"sha256\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\"}}")
RULES=json.loads("{\"bytes\":2461,\"git_blob\":\"5c5d020913d717bb5bc8ce891297e00eaa8944f7\",\"path\":\"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json\",\"sha256\":\"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1\"}")
PARAMETERS=json.loads("{\"WCE_input_space\":\"Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"WCE_only_at_original_selected_parameter\":true,\"WCE_output_space\":\"P Fix(Ra) intersect L2\",\"WPC_input_window\":\"H^(-4/3)\",\"WPC_received_output\":\"same old-circle primitive-density L2 pair plus both means\",\"WPC_source_window\":\"ordinary L2_dr (H^(-2/3) pair)\",\"actual_common_root_cutoff_abs_j\":1024,\"actual_moving_waist_cutoff_abs_j\":268435456,\"arithmetic_bits\":320,\"exact_PC_cutoff_derivative_upper\":\"1875000\",\"exact_PC_full_amplitude_strip\":\"1/256\",\"exact_PC_matrix_lag_strip\":\"1/64\",\"exact_PC_positive_transition\":[\"1/500000\",\"3/1000000\"],\"exact_PC_saved_contour_shift\":\"1/512\",\"exact_PC_transition_length\":\"1/1000000\",\"exact_complete_matrix_weight_upper\":\"(64/63)*16^(2/3)\",\"exact_density_deviation_upper\":\"1/31\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_new_profile_moment_upper_rule\":\"(3p/8)^(2p/3)\",\"exact_profile_moment_shift\":\"5/2\",\"exact_real_delta_radius\":\"1/100000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_terminal_T\":\"1/2000\",\"expected_Python_AST_files\":2,\"expected_actual_gate_count\":22,\"expected_current_inputs\":10,\"expected_historical_inputs\":0,\"expected_total_inputs\":10,\"fixed_intrinsic_parameter\":\"eta_0\",\"full_complex_parameter_square_claimed\":false,\"full_physical_incoming_or_finite_Schur_inverse_claimed\":false,\"independent_physical_mean_coordinates\":2,\"minimum_physical_frequency\":388,\"natural_input_cutoff_abs_j\":97,\"new_complete_mathematical_graphs\":7,\"new_whole_candidate_choices\":2,\"normalized_angular_measure\":true,\"old_exponentials_or_logarithms_reevaluated\":0,\"old_profiles_integrals_exponential_sums_or_matrix_words_reevaluated\":0,\"old_scientific_source_imports_allowed\":0,\"old_successful_scientific_calls_allowed\":0,\"original_actual_runs\":{\"PC\":\"43740173506/1\",\"SEI\":\"43773319871/1\",\"TF\":\"43766881076/1\",\"WT\":\"43763134339/1\",\"WX\":\"43763424840/1\"},\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"physical_root_piece\":2549,\"saved_actual_receipts\":5,\"saved_bound_records\":42,\"saved_original_scope_collections\":5,\"saved_qualification_records\":3,\"shifted_profile_moments\":[\"11/4\",\"13/4\",\"15/4\",\"17/4\",\"19/4\",\"23/4\",\"25/4\"]}")
RETAINED_SCOPE=json.loads("{\"WCE_SEI_H2_is_Bessel_upper_not_unsaved_Wiener_record\":true,\"WCE_actual_input_is_fixed_phase_transported_reflection_not_full_signed_circle\":true,\"WCE_actual_two_I_waist_factor_and_physical_density_mean_rank_retained\":true,\"WCE_complete_two_primitive_ranks_written_before_restriction\":true,\"WCE_exact_waist_first_symbol_zero_does_not_set_second_symbol_zero\":true,\"WCE_full_density_S_preserves_integral_and_actual_input_has_zero_auxiliary_mean\":true,\"WCE_full_root_finite_dual_rows_and_TF_after_right_order_retained\":true,\"WCE_no_extra_TF_inverse_or_Ni_factor\":true,\"WCE_only_original_selected_real_member_and_fixed_intrinsic_reference\":true,\"WCE_only_projected_Ecoeff_equals_projected_E0\":true,\"WCE_saved_CI_B_product_read_verbatim\":true,\"WPC_Kpos_already_includes_positive_seven_port_and_factor9\":true,\"WPC_actual_scalar_X_pullback_not_full_density\":true,\"WPC_complete_angular_matrix_words_paid_before_weighting\":true,\"WPC_complete_both_signed_carriers_and_all_output_modes\":true,\"WPC_genuine_terminal_column_and_nonzero_root_beta_retained\":true,\"WPC_old_volume_finite_head_source_and_received_gain_read_only\":true,\"WPC_only_specific_two_thirds_weight_uses_C2_Schur\":true,\"WPC_root_finite_received_term_retained_separately_not_added_to_new_positive\":true,\"WPC_same_original_PC_positive_trial_cutoff_and_complete_real_family\":true,\"WPC_saved_wide_P_H_moduli_supply_new_finite_Cauchy_derivatives\":true,\"WPC_target_is_full_positive_pair_Hminus2_3_not_negative_special_source\":true,\"actual_finite_border_inverse_claimed\":false,\"all_old_complete_receipts_parameters_and_scopes_frozen\":true,\"all_original_targets_profiles_and_source_integrals_not_recomputed\":true,\"complete_physical_incoming_inverse_claimed\":false,\"complete_return_R0_or_nonlinear_background_claimed\":false,\"historical_native_or_archive_inputs_restored\":false,\"independent_physical_means\":2,\"negative_source_positive_volume_endpoint_and_true_mean_matching_not_removed\":true,\"physical_paired_row_source_target_not_replaced_by_Ti_endomorphism\":true,\"scientific_target\":\"same positive correction and same complete reflected coefficient error\",\"true_radial_head_actual_root_border_and_independent_second_input_retained\":true,\"two_new_targets_are_distinct_and_not_summed_as_an_operator_inverse\":true,\"whole_candidates_preserve_same_complete_operator_and_final_record_endpoints\":true}")
PUBLICATION_LIMITS=json.loads("{\"complete_preGit_max_bytes\":90000,\"complete_science_max_bytes\":75000,\"execution_max_bytes\":59000,\"publication_reserve_bytes\":150000,\"report_max_bytes\":8000}")
COMPLETE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"input_sha256\",\"verified_original_inputs\",\"accepted_old_inputs\",\"copied_complete_original_scopes\",\"copied_complete_original_scopes_sha256\",\"copied_original_scalar_records\",\"copied_original_scalar_records_sha256\",\"copied_original_qualification_records\",\"copied_original_qualification_records_sha256\",\"complete_operator_identity_conclusion\",\"complete_wpc_geometry_and_moment_conclusion\",\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_wpc_positive_correction_conclusion\",\"complete_wce_root_coefficient_conclusion\",\"complete_wce_projected_rank_conclusion\",\"complete_wce_waist_conclusion\",\"complete_wce_algebraic_conclusion\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"gates\",\"actual_mathematical_wall_seconds\"]")
GATE_NAMES=json.loads("[\"public pinned runtime and directed scalar arithmetic in the actual checkout\",\"ten current small texts and no historical or native inputs\",\"two published contracts and seven immutable mathematical identities\",\"complete original PC thirty-gate positive correction success\",\"complete original TF fourteen-gate common-root normalizer success\",\"complete original WX twenty-gate selected full-density coordinate success\",\"complete original WT twenty-gate waist coefficient success with all fixed test results retained\",\"complete original SEI twenty-gate individual coefficient success\",\"same complete PC positive trial cutoff output window means and matrix-strip qualification\",\"same selected WCE root finite primitive and true waist identities\",\"all forty-two original bound records and three qualifications copied verbatim\",\"new shifted moments and actual-output-window geometry are complete\",\"new full-strip Cauchy lists and three weighted Schur functionals are complete\",\"new full two-row cutoff and same received positive candidate are complete\",\"new same-root coefficient factors retain already-paid right-normalizer costs\",\"new full and projected primitive ranks retain their exact mean rows\",\"new exact-waist second-order factors retain the saved forward remainder\",\"new complete algebraic candidates use the same reflected input and full target\",\"whole candidate choices use final saved upper endpoints and retain all candidates\",\"all original input bytes records scopes and receipts remain unchanged\",\"all seven new graphs and actual progress match the complete planned shape\",\"the complete thirty-eight-field conclusion retains all physical limits and twenty-two gates\"]")
PLANNED_SHAPE=json.loads("{\"complete_new_graphs\":7,\"complete_original_successes\":5,\"complete_saved_output_scalar_slots\":90,\"copied_bound_records\":42,\"copied_qualification_records\":3,\"full_physical_inverse_claimed\":false,\"historical_inputs_restored\":0,\"new_whole_choices\":2,\"old_scientific_calls\":0,\"original_scope_collections\":5,\"scalar_slots_by_graph\":{\"complete_wce_algebraic_conclusion\":9,\"complete_wce_projected_rank_conclusion\":6,\"complete_wce_root_coefficient_conclusion\":7,\"complete_wce_waist_conclusion\":6,\"complete_wpc_cauchy_and_schur_conclusion\":24,\"complete_wpc_geometry_and_moment_conclusion\":24,\"complete_wpc_positive_correction_conclusion\":14}}")
INITIAL_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":0,\"copied_original_bound_records\":0,\"copied_original_qualification_records\":0,\"copied_original_scope_collections\":0,\"historical_or_native_inputs_restored\":0,\"new_wce_complete_candidate_graphs\":0,\"new_wce_rank_graphs\":0,\"new_wce_root_graphs\":0,\"new_wce_waist_graphs\":0,\"new_whole_candidate_choices\":0,\"new_wpc_cauchy_and_schur_graphs\":0,\"new_wpc_complete_positive_candidates\":0,\"new_wpc_geometry_and_moment_graphs\":0,\"old_completed_scalar_products_recomputed\":0,\"old_exponentials_or_logarithms_evaluated\":0,\"old_profiles_exponential_sums_or_integrals_recomputed\":0,\"old_scientific_producers_imported_or_called\":0,\"old_scientific_targets_recomputed\":0}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":5,\"copied_original_bound_records\":42,\"copied_original_qualification_records\":3,\"copied_original_scope_collections\":5,\"historical_or_native_inputs_restored\":0,\"new_wce_complete_candidate_graphs\":1,\"new_wce_rank_graphs\":1,\"new_wce_root_graphs\":1,\"new_wce_waist_graphs\":1,\"new_whole_candidate_choices\":2,\"new_wpc_cauchy_and_schur_graphs\":1,\"new_wpc_complete_positive_candidates\":1,\"new_wpc_geometry_and_moment_graphs\":1,\"old_completed_scalar_products_recomputed\":0,\"old_exponentials_or_logarithms_evaluated\":0,\"old_profiles_exponential_sums_or_integrals_recomputed\":0,\"old_scientific_producers_imported_or_called\":0,\"old_scientific_targets_recomputed\":0}")
OPERATOR_IDENTITY=json.loads("{\"coefficient_complete_row\":\"D_alg=Qa Vw Ti-(h-1)rho_i+Qa A_J P_h(R_S+S R_F S_inverse)\",\"coefficient_projected_identity\":\"P_h E_coeff = P_h(R_S+S R_F S_inverse)\",\"coefficient_rank_exact\":\"R_S=ci tensor ppsi-(ci*ppsi) tensor 1\",\"coefficient_root_exact\":\"(Id+MC I) TF_inverse = Id+Mc I+(F_J-Mc I A_F) TF_inverse\",\"coefficient_source\":\"Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"coefficient_target\":\"P Fix(Ra) intersect L2\",\"full_physical_mean_rank_retained\":true,\"only_new_scalar_enclosures_not_new_inverse_or_actual_background\":true,\"positive_complete_reconstruction\":\"h1=P T(hamp)+J(P T(gamp)-L P T(hamp)-B P T(w)); h2=P T(w)\",\"positive_received_order\":\"Kpos*(saved_Cvol+new_Ccut+saved_CFH)\",\"positive_source\":\"original chi_prime times complete genuine raw pair hG\",\"positive_whole_choice\":\"same Rplus in the complete WUE tuple\",\"root_finite_output\":\"saved complete received RF remains separate; its actual trace border is not evaluated\",\"same_selected_parameter_only_for_coefficient\":true}")
EXPECTED_ACCEPTED=json.loads("{\"original_bound_records_sha256\":\"1966c937ea41995ab4ee65cd870c997dfd0e201ad9afaf817f149eafa3e17c6a\",\"original_complete_science_objects_not_recomputed\":true,\"original_qualification_records_sha256\":\"e6d95b77b886921337ba37201e2fd0da67c26c02233672e794479b3019bd669e\",\"original_scope_collections_sha256\":\"2e21ee2bf8bc0db069ea9a0390f326fa32a6cbc6d324bfcf6af86f099610ba20\",\"original_scope_fragments_are_exact_full_path_values\":true,\"original_successes\":{\"pc_execution\":{\"complete_original_gates_sha256\":\"a678587f44821e6e9873d6f146db7d4fe17f715a7209a0dbf76c028347817e61\",\"file_bytes\":46253,\"file_git_blob\":\"c32b8e3f3aca08d338784504c2cce5054d203bc6\",\"file_path\":\"topics/visible-flex-exact-nearby/notes/genuine_positive_Ai_cutoff_strong_correction_ci/run-43740173506-1/execution.json\",\"file_sha256\":\"75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817\",\"gate_count\":30,\"identity\":{\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"2f470d6fffc1fe2bc7b7ffc85829aa41c54ac4a0\",\"arithmetic_bits\":320,\"complete\":true,\"failure\":null,\"input_manifest_sha256\":\"13d92e7d2bfb8e3fd57e417676c58d6a649c7f353bcd54fef19af8cc66e123e5\",\"kind\":\"actual_genuine_positive_Ai_cutoff_and_strong_correction_v1\",\"proved\":true,\"run_attempt\":\"1\",\"run_id\":\"43740173506\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"source_sha256\":\"da6864cd790162759d5a78d40a67d0f3b4aa91b60614d947cca1a92371d6940b\",\"workflow_event_commit\":\"96744db0bc1fed0826fa0999cb0b7eee7ddb1d62\"},\"passed_gate_count\":30,\"science_canonical_bytes\":26951,\"science_canonical_sha256\":\"9da04f0bdef239d5c33c12e0e818e43b03a9085139765a1fc7f6cf9f13cd407a\",\"science_field_count\":54,\"science_location\":\"embedded actual_scientific_receipt\",\"wrapper_identity\":{\"actual_failure\":null,\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"2f470d6fffc1fe2bc7b7ffc85829aa41c54ac4a0\",\"actual_source_budget_processes\":1,\"complete\":true,\"input_manifest_sha256\":\"13d92e7d2bfb8e3fd57e417676c58d6a649c7f353bcd54fef19af8cc66e123e5\",\"kind\":\"actual_public_genuine_positive_Ai_cutoff_strong_correction_execution\",\"run_attempt\":\"1\",\"run_id\":\"43740173506\",\"source_budget_source_sha256\":\"da6864cd790162759d5a78d40a67d0f3b4aa91b60614d947cca1a92371d6940b\",\"workflow_commit\":\"96744db0bc1fed0826fa0999cb0b7eee7ddb1d62\"}},\"sei_execution\":{\"complete_original_gates_sha256\":\"3debcb11cd858fe83b854cf829df1631f5d7825b2a3ca087b34fe991c6d8adea\",\"file_bytes\":46192,\"file_git_blob\":\"e1532b816ea344ee65e52a503279376a0c449299\",\"file_path\":\"topics/visible-flex-exact-nearby/notes/individual_principal_energy_terminal_density_ci/run-43773319871-1/execution.json\",\"file_sha256\":\"b0088f831471f29d41624e487586fbb9f4801ef7837f9b4dd3c29a57e51b3d29\",\"gate_count\":20,\"identity\":{\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"425d8a3248d6f3b6a54ccc1f4349dbadddf91545\",\"arithmetic_bits\":320,\"complete\":true,\"failure\":null,\"input_manifest_sha256\":\"3e26d5eb305e0a1112f059192f6060a4a90c74aa4d37e0da1bc26247f4030a9f\",\"kind\":\"actual_individual_principal_energy_from_terminal_density_v1\",\"proved\":true,\"run_attempt\":\"1\",\"run_id\":\"43773319871\",\"runtime\":{\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"source_sha256\":\"f75a8f905b89a5527d52271c3e1fd682d43cf7f90d8b4b865f16efdcc75f8723\",\"workflow_event_commit\":\"425d8a3248d6f3b6a54ccc1f4349dbadddf91545\"},\"passed_gate_count\":20,\"science_canonical_bytes\":35198,\"science_canonical_sha256\":\"e830e10be50804e80054dee7983fe8004a64d24ab5ff567298a490d8f737c93b\",\"science_field_count\":61,\"science_location\":\"embedded actual_scientific_receipt\",\"wrapper_identity\":{\"actual_failure\":null,\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"425d8a3248d6f3b6a54ccc1f4349dbadddf91545\",\"actual_source_budget_processes\":1,\"complete\":true,\"input_manifest_sha256\":\"3e26d5eb305e0a1112f059192f6060a4a90c74aa4d37e0da1bc26247f4030a9f\",\"kind\":\"actual_public_individual_principal_energy_terminal_density_execution\",\"run_attempt\":\"1\",\"run_id\":\"43773319871\",\"source_budget_source_sha256\":\"f75a8f905b89a5527d52271c3e1fd682d43cf7f90d8b4b865f16efdcc75f8723\",\"workflow_commit\":\"425d8a3248d6f3b6a54ccc1f4349dbadddf91545\"}},\"tf_science\":{\"complete_original_gates_sha256\":\"d8cf1f82f556ed32ea44309e407f8fe264e769275311ca7787d5913291466cb7\",\"file_bytes\":18206,\"file_git_blob\":\"3766aea85aba59230be3813b4b7634d318316e49\",\"file_path\":\"topics/visible-flex-exact-nearby/notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json\",\"file_sha256\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"gate_count\":14,\"identity\":{\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"8839cad6bdb5bdd7b5f09959cbc3a20c55c680c6\",\"arithmetic_bits\":320,\"complete\":true,\"failure\":null,\"input_manifest_sha256\":\"027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf\",\"kind\":\"actual_common_root_normalizer_two_window_v1\",\"proved\":true,\"run_attempt\":\"1\",\"run_id\":\"43766881076\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"source_sha256\":\"bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b\",\"workflow_event_commit\":\"0107666b538ced3a0fbc91f6a7f2cfa894f8ef6f\"},\"passed_gate_count\":14,\"science_canonical_bytes\":18206,\"science_canonical_sha256\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"science_field_count\":38,\"science_location\":\"complete standalone scientific object\"},\"wt_science\":{\"complete_original_gates_sha256\":\"1b91d0234100283fa35ba5742d4f77a315ec2dc2b4b13c936bc2b6668b133edd\",\"file_bytes\":27619,\"file_git_blob\":\"b742d3167f68c05ef197450a3112eb5b8edcacac\",\"file_path\":\"topics/visible-flex-exact-nearby/notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json\",\"file_sha256\":\"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d\",\"gate_count\":20,\"identity\":{\"actual_returncode\":0,\"arithmetic_bits\":320,\"complete\":true,\"failure\":null,\"input_manifest_sha256\":\"4cec7ef0ba21373190dd0bf142d10546823d46bb832a58df66529822990ad125\",\"kind\":\"actual_waist_normalizer_coefficients_and_two_window_gates_v1\",\"proved\":true,\"run_attempt\":\"1\",\"run_id\":\"43763134339\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"source_sha256\":\"7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393\"},\"passed_gate_count\":20,\"science_canonical_bytes\":27619,\"science_canonical_sha256\":\"2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d\",\"science_field_count\":38,\"science_location\":\"complete standalone scientific object\"},\"wx_execution\":{\"complete_original_gates_sha256\":\"4c8f214fc05eaf3c8c3a9970a41921037356bf0f9021ef1b1ec942c485b90d47\",\"file_bytes\":43753,\"file_git_blob\":\"5121a599896025d90e2861450756a256aaba659d\",\"file_path\":\"topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json\",\"file_sha256\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"gate_count\":20,\"identity\":{\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\",\"arithmetic_bits\":320,\"complete\":true,\"failure\":null,\"input_manifest_sha256\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"proved\":true,\"run_attempt\":\"1\",\"run_id\":\"43763424840\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"source_sha256\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"workflow_event_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\"},\"passed_gate_count\":20,\"science_canonical_bytes\":31088,\"science_canonical_sha256\":\"536e5f33441570eec1b0b35091400f815c5333c4cfd3f0f731099f5dd48cb015\",\"science_field_count\":55,\"science_location\":\"embedded actual_scientific_receipt\",\"wrapper_identity\":{\"actual_failure\":null,\"actual_returncode\":0,\"actual_scientific_checkout_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\",\"actual_source_budget_processes\":1,\"complete\":true,\"input_manifest_sha256\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"kind\":\"actual_public_true_waist_coordinates_saved_products_execution\",\"run_attempt\":\"1\",\"run_id\":\"43763424840\",\"source_budget_source_sha256\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"workflow_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\"}}}}")
WPC_SCALAR_PATHS=json.loads("{\"B\":[\"pc_execution\",\"complete_positive_volume_conclusion\",\"same_shift_L2_word_maxima\",\"B\"],\"CA\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"CA\"],\"CFH\":[\"pc_execution\",\"complete_strong_correction_conclusion\",\"complete_finite_head_commutator_source_upper\"],\"CX\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"CX\"],\"Cvol\":[\"pc_execution\",\"complete_strong_correction_conclusion\",\"complete_positive_ordinary_volume_upper\"],\"F2\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"F2\"],\"G\":[\"pc_execution\",\"complete_cutoff_and_head_conclusion\",\"complete_real_reconstruction_coefficients\",\"G\"],\"H\":[\"pc_execution\",\"complete_cutoff_and_head_conclusion\",\"complete_shift_reconstruction_coefficients\",\"H\"],\"J\":[\"pc_execution\",\"complete_positive_volume_conclusion\",\"same_shift_L2_word_maxima\",\"J\"],\"Kpos\":[\"pc_execution\",\"complete_strong_correction_conclusion\",\"accepted_positive_collar_to_waist_gain_read_verbatim\"],\"L\":[\"pc_execution\",\"complete_positive_volume_conclusion\",\"same_shift_L2_word_maxima\",\"L\"],\"P0\":[\"pc_execution\",\"complete_cutoff_and_head_conclusion\",\"complete_shift_reconstruction_coefficients\",\"P\"],\"Tmin\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"Tmin\"],\"V\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"V\"],\"VT\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"VT\"],\"W\":[\"pc_execution\",\"complete_cutoff_and_head_conclusion\",\"complete_pair_amplitude_holomorphic_upper\"],\"WD\":[\"pc_execution\",\"complete_cutoff_and_head_conclusion\",\"complete_D_amplitude_holomorphic_upper\"],\"Y0\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"Y0\"],\"Y1\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"Y1\"],\"Z0\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"Z0\"],\"Z1\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"Z1\"],\"m\":[\"pc_execution\",\"complete_positive_domain_conclusion\",\"m\"],\"old_cutoff\":[\"pc_execution\",\"complete_strong_correction_conclusion\",\"complete_positive_cutoff_source_upper\"],\"old_positive_received\":[\"pc_execution\",\"complete_strong_correction_conclusion\",\"new_positive_correction_to_waist_upper\"],\"root_finite_received\":[\"pc_execution\",\"complete_strong_correction_conclusion\",\"new_root_finite_head_to_waist_upper\"]}")
WCE_SCALAR_PATHS=json.loads("{\"H_Hminus4_3\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"complete_density_Hminus4_3_upper\"],\"H_L2\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"complete_density_L2_upper\"],\"H_inverse_L2\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"complete_inverse_density_L2_upper\"],\"S_L2\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_L2_upper\"],\"S_inverse_Hminus4_3\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_inverse_Hminus4_3_upper\"],\"TF_finite_after_right\":[\"tf_science\",\"complete_new_strong_scalar_factors\",\"complete_finite_map_fee_after_right_inverse\"],\"TF_two_primitive_after_right\":[\"tf_science\",\"complete_new_strong_scalar_factors\",\"complete_two_primitive_left_multiplier_fee_after_right_inverse\"],\"WT_forward_strong_remainder\":[\"wt_science\",\"complete_fixed_cutoff_results\",1,\"forward_complete_strong_remainder\"],\"WT_tau2_L2\":[\"wt_science\",\"complete_fixed_cutoff_results\",1,\"tau\",\"tau2_L2\"],\"ci_Linfty\":[\"sei_execution\",\"complete_new_individual_nonmean_budget_conclusion\",\"branches\",\"incoming\",\"complete_actual_coefficient_Linfty_upper\"],\"mean_row_CI_B\":[\"sei_execution\",\"complete_new_signed_energy_conclusion\",\"branches\",\"incoming\",\"complete_CI_B_upper\"],\"mu_absolute\":[\"sei_execution\",\"complete_new_individual_density_derivative_conclusion\",\"complete_absolute_mu_upper\"],\"psi_derivative_lower\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"common_input_derivative_lower\"],\"psi_displacement_H4_3\":[\"wx_execution\",\"complete_full_primitive_rank_conclusion\",\"selected_common_input\",\"complete_zero_mean_displacement_H2_and_H4_3_upper\"],\"psi_displacement_Linfty\":[\"wx_execution\",\"complete_full_primitive_rank_conclusion\",\"selected_common_input\",\"complete_zero_mean_displacement_Linfty_upper\"],\"vi_Bessel_H2\":[\"sei_execution\",\"complete_new_individual_nonmean_budget_conclusion\",\"branches\",\"incoming\",\"complete_Bessel_H0_H1_H2_H3_upper\",2],\"vi_L2\":[\"sei_execution\",\"complete_new_individual_density_derivative_conclusion\",\"branches\",\"incoming\",\"complete_actual_nonmean_derivative_L2_upper\",0]}")
QUALIFICATION_PATHS=json.loads("{\"selected_H_derivative_lower\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"phase_derivative_lower\"],\"selected_H_derivative_upper\":[\"wx_execution\",\"complete_selected_H_coordinate_conclusion\",\"phase_derivative_upper\"],\"signed_mu\":[\"sei_execution\",\"complete_SN_terminal_conclusion_read_verbatim\",\"complete_scalar_mu_copied\"]}")
SCOPE_PATHS=json.loads("{\"pc_execution\":[[\"mathematical_parameters\"],[\"scope\"],[\"complete_positive_domain_conclusion\",\"exact_p_strip\"],[\"complete_positive_domain_conclusion\",\"exact_new_shift\"],[\"complete_positive_domain_conclusion\",\"same_complete_terminal_solution_and_root_shear\"],[\"complete_positive_domain_conclusion\",\"all_six_required_holomorphic_domains_checked\"],[\"complete_positive_domain_conclusion\",\"DG_full_disk_g_used_not_RJ_negative_six_row_max\"],[\"complete_cutoff_and_head_conclusion\",\"exact_transition_length\"],[\"complete_cutoff_and_head_conclusion\",\"exact_transition_derivative_upper\"],[\"complete_cutoff_and_head_conclusion\",\"physical_mean_and_full_head_retained\"],[\"complete_positive_volume_conclusion\",\"exact_same_shift_paid_matrix_width\"],[\"complete_positive_volume_conclusion\",\"complete_positive_intersections\"],[\"complete_strong_correction_conclusion\",\"input\"],[\"complete_strong_correction_conclusion\",\"output\"],[\"complete_strong_correction_conclusion\",\"full_root_finite_head_and_two_mean_inputs_retained\"],[\"complete_strong_correction_conclusion\",\"genuine_root_beta_shear_not_discarded\"],[\"complete_strong_correction_conclusion\",\"outgoing_unstable_root_trace_paid_by_complete_seven_port_graph\"]],\"sei_execution\":[[\"mathematical_parameters\"],[\"scope\"],[\"complete_selected_common_input_scope_read_verbatim\"],[\"complete_new_individual_density_derivative_conclusion\",\"complete_derivative_orders\"],[\"complete_new_individual_nonmean_budget_conclusion\",\"all_candidates_bound_the_same_complete_branch\"],[\"complete_SN_whole_path_scope_read_verbatim\"],[\"complete_individual_principal_energy_consumer_paid\"],[\"full_physical_incoming_inverse_claimed\"],[\"finite_Schur_inverse_claimed\"]],\"tf_science\":[[\"parameters\"],[\"complete_new_root_coefficient_conclusion\",\"root_mean_and_both_Fourier_signs_retained\"],[\"complete_new_root_coefficient_conclusion\",\"original_full_complex_eta_domain_includes_root\"],[\"complete_new_root_normalizer_conclusion\",\"actual_J_F\"],[\"complete_new_root_normalizer_conclusion\",\"same_inverse_on_both_windows\"],[\"complete_new_root_normalizer_conclusion\",\"below_J_F_and_independent_mean_ports_are_identity\"],[\"complete_new_root_normalizer_conclusion\",\"finite_original_input_and_output_support_abs_j\"],[\"complete_new_root_normalizer_conclusion\",\"right_transformed_finite_rows_keep_actual_dual_norms\"],[\"complete_new_root_normalizer_conclusion\",\"right_transformed_finite_input_support_not_claimed\"],[\"complete_new_strong_scalar_factors\",\"exact_order\"],[\"complete_new_strong_scalar_factors\",\"finite_fee_is_one_complete_branch_fee_with_full_mean\"],[\"complete_new_strong_scalar_factors\",\"two_primitive_fee_requires_separate_complete_tilde_C_supremum\"]],\"wt_science\":[[\"parameters\"],[\"new_coefficient_scope\"],[\"copied_D_state_and_repair_parameters\"],[\"fixed_cutoff_failures_are_retained_sufficient_test_failures\"],[\"fixed_cutoff_inverse_success_count\"],[\"fixed_cutoff_inverse_test_count\"],[\"complete_fixed_cutoff_results\",0,\"all_four_strict_tests\"],[\"complete_fixed_cutoff_results\",1,\"J\"],[\"complete_fixed_cutoff_results\",1,\"all_four_strict_tests\"],[\"complete_fixed_cutoff_results\",1,\"finite_complement_and_two_means_identity\"],[\"complete_fixed_cutoff_results\",1,\"inverse_on_both_windows_proved\"],[\"complete_fixed_cutoff_results\",1,\"selection\"],[\"copied_SP_family_identity\"]],\"wx_execution\":[[\"mathematical_parameters\"],[\"scope\"],[\"complete_selected_common_input_conclusion\",\"only_same_selected_actual_conjugacy\"],[\"complete_selected_common_input_conclusion\",\"exact_order\"],[\"complete_selected_common_input_conclusion\",\"inverse_order\"],[\"complete_selected_common_input_conclusion\",\"selected_parameter_absolute_upper\"],[\"complete_selected_H_coordinate_conclusion\",\"same_actual_inverse_on_L2_and_Hminus4_3\"],[\"complete_selected_H_coordinate_conclusion\",\"independent_physical_mean_block_is_identity\"],[\"complete_full_primitive_rank_conclusion\",\"selected_common_input\",\"exact_full_circle_identity\"],[\"complete_full_primitive_rank_conclusion\",\"selected_common_input\",\"both_finite_rank_terms_and_the_full_mean_retained\"],[\"complete_full_primitive_rank_conclusion\",\"selected_common_input\",\"mean_identity_extension_differs_from_full_density_by_explicit_rank\"]]}")
FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256="2e21ee2bf8bc0db069ea9a0390f326fa32a6cbc6d324bfcf6af86f099610ba20"
FROZEN_SAVED_SCALAR_RECORDS_SHA256="1966c937ea41995ab4ee65cd870c997dfd0e201ad9afaf817f149eafa3e17c6a"
FROZEN_QUALIFICATION_RECORDS_SHA256="e6d95b77b886921337ba37201e2fd0da67c26c02233672e794479b3019bd669e"
FROZEN_ACCEPTED_OLD_INPUTS_SHA256="1be092345ec066222873f45e624ce2544be035a104502622ad096a21cd4df0b8"
NEW_GRAPH_SHAPES=json.loads("{\"complete_wce_algebraic_conclusion\":{\"complete_full_Calg_upper\":\"record\",\"complete_full_candidate_after_projection_upper\":\"record\",\"complete_full_candidate_algebra_upper\":\"record\",\"complete_full_rank_and_root_before_projection_upper\":\"record\",\"complete_projected_Calg_upper\":\"record\",\"complete_projected_candidate_algebra_upper\":\"record\",\"complete_projected_rank_and_root_upper\":\"record\",\"complete_projected_root_upper\":\"record\",\"complete_whole_choice\":{\"all_candidates_retained\":true,\"complete_selected_upper\":\"record\",\"selected_label\":\"label\"},\"full_and_projected_candidates_both_saved\":true,\"input_normalizer_not_reapplied_to_coefficient_error\":true,\"no_full_physical_incoming_or_finite_inverse_claimed\":true,\"operator\":\"=D_alg = Lpartial Y_WJ Ni - Qa Ti\",\"physical_mean_rank_and_TF_finite_rank_retained\":true,\"positive_negative_endpoint_state_errors_remain_separate\":true,\"same_complete_operator_and_leading_row_for_both_candidates\":true,\"source\":\"=Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"target\":\"=P Fix(Ra) intersect L2\",\"whole_choice_uses_final_retained_outward_records\":true},\"complete_wce_projected_rank_conclusion\":{\"both_full_primitive_ranks_written_before_restriction\":true,\"complete_full_first_primitive_rank_upper\":\"record\",\"complete_full_second_primitive_rank_upper\":\"record\",\"complete_full_two_primitive_ranks_upper\":\"record\",\"complete_projected_density_mean_coefficient_upper\":\"record\",\"complete_projected_primitive_rank_upper\":\"record\",\"complete_projected_rank_coefficient_L2_upper\":\"record\",\"exact_density_deviation_upper\":\"=1/31\",\"exact_full_rank_formula\":\"=ci tensor ppsi - (ci*ppsi) tensor 1\",\"exact_projected_rank_on_actual_input\":\"=(vi - nu*(h-1)) tensor ppsi\",\"full_density_S_preserves_the_integral\":true,\"only_projected_Ecoeff_equals_projected_E0\":true,\"physical_density_mean_rank_not_removed\":true,\"zero_input_mean_only_on_actual_Xfr\":true},\"complete_wce_root_coefficient_conclusion\":{\"TF_after_right_factors_read_once\":true,\"complete_absolute_incoming_mean_upper\":\"record\",\"complete_conjugated_root_strong_fee_upper\":\"record\",\"complete_incoming_forward_Hminus4_3_upper\":\"record\",\"complete_nonmean_Wfour_thirds_upper\":\"record\",\"complete_root_coefficient_Linfty_upper\":\"record\",\"complete_root_strong_fee_upper\":\"record\",\"complete_root_two_primitive_fee_upper\":\"record\",\"exact_order\":\"=S (F_J - M_c I A_F) T_F_inverse S_inverse\",\"input_window\":\"=H^(-4/3)\",\"no_second_TF_inverse_or_Ni_factor\":true,\"old_CI_B_product_not_recomputed\":true,\"only_denominator_from_true_psi_lower\":true,\"output_window_for_root_strong_fees\":\"=L2\",\"root_FJ_full_mean_and_dual_rows_retained\":true},\"complete_wce_waist_conclusion\":{\"actual_moving_Js\":268435456,\"actual_second_normalizer_and_minus_Sr_retained\":true,\"complete_physical_density_mean_rank_upper\":\"record\",\"complete_physical_row_sum_upper\":\"record\",\"complete_physical_two_primitive_row_upper\":\"record\",\"complete_waist_forward_L2_upper\":\"record\",\"complete_waist_second_normalizer_L2_upper\":\"record\",\"complete_waist_second_normalizer_strong_upper\":\"record\",\"exact_Vw_order\":\"=U_H_inverse B_w U_H\",\"exact_first_waist_normalizer_is_zero_by_WPL\":true,\"no_old_first_finite_fee_subtracted\":true,\"old_complete_Id_plus_A1_times_A2_fee_read_verbatim\":true,\"reflected_pair_sqrt_two_cancels_on_both_sides\":true,\"two_independent_physical_mean_ports_retained\":true},\"complete_wpc_cauchy_and_schur_conclusion\":{\"all_output_means_and_original_P_retained\":true,\"complete_three_amplitude_functionals\":{\"g\":{\"complete_Hminus4_3_to_Hminus2_3_upper\":\"record\",\"complete_amplitude_angular_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_inverse_angle_second_derivative_upper\":\"record\",\"complete_weighted_phase_derivative_upper\":[\"record\",\"record\",\"record\"]},\"h\":{\"complete_Hminus4_3_to_Hminus2_3_upper\":\"record\",\"complete_amplitude_angular_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_inverse_angle_second_derivative_upper\":\"record\",\"complete_weighted_phase_derivative_upper\":[\"record\",\"record\",\"record\"]},\"w\":{\"complete_Hminus4_3_to_Hminus2_3_upper\":\"record\",\"complete_amplitude_angular_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_inverse_angle_second_derivative_upper\":\"record\",\"complete_weighted_phase_derivative_upper\":[\"record\",\"record\",\"record\"]}},\"exact_full_holomorphic_strip\":\"=1/256\",\"full_two_row_reconstruction_not_replaced_by_one_height\":true,\"g_second_derivative_includes_complete_p_third_derivative\":true,\"no_unsaved_RJ_jet_used\":true},\"complete_wpc_geometry_and_moment_conclusion\":{\"complete_a_profile_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_b_profile_derivative_upper\":[\"record\",\"record\",\"record\"],\"complete_pair_profile_derivative_upper\":[\"record\",\"record\",\"record\"],\"exact_profile_moment_shift\":\"=5/2\",\"exact_total_Tmin_exponent\":\"=-11/4\",\"full_two_sign_matrix_including_all_output_modes\":true,\"geometry\":{\"complete_same_shift_matrix_weight_upper\":\"record\",\"complete_shifted_profile_prefactor_upper\":\"record\",\"frequency_Bessel_factor_upper\":\"record\",\"frequency_inverse_upper\":\"record\",\"frequency_minus_one_third_upper\":\"record\",\"physical_cutoff_radial_factor_upper\":\"record\",\"scalar_pullback_Hminus2_3_upper\":\"record\",\"scalar_pullback_L2_upper\":\"record\"},\"old_Airy_profiles_or_exponential_sums_recomputed\":false,\"shifted_moment_upper\":{\"11/4\":\"record\",\"13/4\":\"record\",\"15/4\":\"record\",\"17/4\":\"record\",\"19/4\":\"record\",\"23/4\":\"record\",\"25/4\":\"record\"}},\"complete_wpc_positive_correction_conclusion\":{\"already_received_Kpos_used_exactly_once\":true,\"complete_cutoff_source_upper\":\"record\",\"complete_first_row_term_upper\":[\"record\",\"record\",\"record\"],\"complete_first_row_upper\":\"record\",\"complete_ordered_JB_word_upper\":\"record\",\"complete_ordered_JL_word_upper\":\"record\",\"complete_ordered_J_word_upper\":\"record\",\"complete_ordinary_volume_and_finite_head_source_read_only\":true,\"complete_positive_source_upper\":\"record\",\"complete_received_positive_candidate_upper\":\"record\",\"complete_second_row_upper\":\"record\",\"full_incoming_or_finite_border_inverse_claimed\":false,\"full_means_genuine_root_shear_and_terminal_column_retained\":true,\"new_positive_reception_is_same_Rplus_in_WUE\":true,\"root_finite_received_term_is_separate_and_unchanged\":true,\"same_original_PC_trial_and_cutoff\":true,\"whole_received_positive_candidates\":{\"new_actual_output_window_cutoff\":\"record\",\"saved_complete_positive\":\"record\"},\"whole_received_positive_choice\":{\"all_candidates_retained\":true,\"complete_selected_upper\":\"record\",\"selected_label\":\"label\"}}}")
NEW_GRAPH_SLOT_COUNTS=json.loads("{\"complete_wce_algebraic_conclusion\":9,\"complete_wce_projected_rank_conclusion\":6,\"complete_wce_root_coefficient_conclusion\":7,\"complete_wce_waist_conclusion\":6,\"complete_wpc_cauchy_and_schur_conclusion\":24,\"complete_wpc_geometry_and_moment_conclusion\":24,\"complete_wpc_positive_correction_conclusion\":14}")
EXPECTED_ORIGINALS=EXPECTED_ACCEPTED["original_successes"]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode("utf-8")

def git_blob(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def require(condition,message):
    if not condition:
        raise ValueError(message)

def gate(doc,index,condition):
    if len(doc["gates"])!=index:
        raise ValueError("gate order changed")
    passed=bool(condition)
    doc["gates"].append({"name":GATE_NAMES[index],"passed":passed})
    if not passed:
        raise ValueError("gate failed: "+GATE_NAMES[index])

def get_path(value,path):
    for key in path:
        value=value[key]
    return value

def persist(path,doc):
    raw=canonical(doc)
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".atomic")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    return raw

def print_complete_document(doc):
    print("BEGIN_COMPLETE_POSITIVE_CUTOFF_AND_REFLECTED_COEFFICIENT_SCIENCE_JSON",flush=True)
    print(canonical(doc).decode("utf-8"),end="",flush=True)
    print("END_COMPLETE_POSITIVE_CUTOFF_AND_REFLECTED_COEFFICIENT_SCIENCE_JSON",flush=True)

def checked_inputs(args,doc):
    runtime={"Python":platform.python_version(),
             "python_flint":importlib.metadata.version("python-flint")}
    doc["runtime"]=runtime
    gate(doc,0,os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==PUBLIC
        and runtime==RUNTIME and args.bits==ctx.prec==PARAMETERS["arithmetic_bits"]
        and re.fullmatch(r"[0-9a-f]{40}",doc["actual_scientific_checkout_commit"] or "") is not None
        and re.fullmatch(r"[0-9a-f]{40}",doc["workflow_event_commit"] or "") is not None
        and re.fullmatch(r"[0-9]+",doc["run_id"] or "") is not None
        and re.fullmatch(r"[0-9]+",doc["run_attempt"] or "") is not None
        and doc["input_manifest_sha256"]==args.manifest_sha)
    manifest=json.loads(args.manifest.read_bytes())
    expected_paths={"source":SOURCE,"worker":WORKER,"rules":RULES["path"]}
    expected_paths.update({key:entry["path"] for key,entry in PIN_SPECS.items()})
    entries=manifest.get("files",[])
    by_role={entry.get("role"):entry for entry in entries}
    gate(doc,1,manifest.get("kind")==MANIFEST_KIND
        and manifest.get("public_repository")==PUBLIC
        and manifest.get("source_path")==SOURCE
        and manifest.get("source_sha256")==doc["source_sha256"]
        and manifest.get("parameters")==PARAMETERS
        and manifest.get("scope")==RETAINED_SCOPE
        and manifest.get("publication_limits")==PUBLICATION_LIMITS
        and manifest.get("expected_actual_gate_count")==GATE_COUNT
        and manifest.get("expected_immutable_AST_files")==2
        and manifest.get("expected_current_input_count")==10
        and manifest.get("expected_input_count")==10
        and len(entries)==len(by_role)==10 and set(by_role)==set(expected_paths)
        and manifest.get("input_paths")==expected_paths
        and manifest.get("current_text_input_roles")==list(expected_paths)
        and manifest.get("current_input_paths")==list(expected_paths.values())
        and manifest.get("all_inputs_are_current_small_texts") is True
        and manifest.get("historical_inputs")==[]
        and manifest.get("legacy_artifact_inputs")==[]
        and manifest.get("old_successful_scientific_calls_allowed") is False
        and manifest.get("new_native_arrays_or_artifact_persistence_allowed") is False)
    paths={role:args.repo/Path(path) for role,path in expected_paths.items()}
    verified={}
    for role,path in paths.items():
        entry=by_role[role]
        data=path.read_bytes()
        require(entry["path"]==expected_paths[role],"current path changed")
        require(0<len(data)<100000 and path.suffix in (".py",".json",".md"),
                "current small text qualification")
        data.decode("utf-8")
        require(not data.startswith(b"\x1f\x8b"),"no gzip input in this consumer")
        require(len(data)==entry["bytes"] and sha(data)==entry["sha256"]
            and git_blob(data)==entry["git_blob"],"complete current identity mismatch: "+role)
        if role in PIN_SPECS:
            require({k:entry[k] for k in ("path","git_blob","bytes","sha256")}==PIN_SPECS[role],
                    "mathematical pin changed: "+role)
            verified[role]={"bytes":len(data),"sha256":sha(data)}
        if role=="rules":
            require(all(entry[k]==RULES[k] for k in ("path","git_blob","bytes","sha256")),
                    "reviewed rules identity changed")
    doc["input_sha256"]={role:entry["sha256"] for role,entry in PIN_SPECS.items()}
    doc["input_sha256"]["manifest"]=doc["input_manifest_sha256"]
    doc["verified_original_inputs"]=verified
    wpc,wce=paths["wpc_contract"].read_text(),paths["wce_contract"].read_text()
    gate(doc,2,len(verified)==7
        and manifest.get("complete_input_bytes")==sum(entry["bytes"] for entry in entries)
        and manifest.get("file_sha256")=={entry["path"]:entry["sha256"] for entry in entries}
        and manifest.get("mathematical_input_sha256")=={k:v["sha256"] for k,v in PIN_SPECS.items()}
        and all(tag in wpc for tag in (r"\tag{WPC.14}",r"\tag{WPC.18}",r"\tag{WPC.21}",r"\tag{WPC.22}",r"\tag{WPC.23}"))
        and all(tag in wce for tag in (r"\tag{WCE.10}",r"\tag{WCE.17}",r"\tag{WCE.24}",r"\tag{WCE.31}",r"\tag{WCE.32}"))
        and by_role["source"]["sha256"]==sha(Path(__file__).read_bytes()))
    return manifest,paths

def original_science(role,path):
    raw=path.read_bytes()
    whole=json.loads(raw)
    embedded=role.endswith("_execution")
    science=whole["actual_scientific_receipt"] if embedded else whole
    expected=EXPECTED_ORIGINALS[role]
    scientific_raw=canonical(science)
    require(len(science)==expected["science_field_count"],"original complete schema changed: "+role)
    require({key:science[key] for key in expected["identity"]}==expected["identity"],
            "original complete success identity changed: "+role)
    require(science["complete"] is True and science["proved"] is True
        and science["actual_returncode"]==0 and science["failure"] is None,
        "original complete zero-child success required")
    gates=science["gates"]
    require(len(gates)==expected["gate_count"]
        and all(set(row)=={"name","passed"} and row["passed"] is True for row in gates)
        and sha(canonical(gates))==expected["complete_original_gates_sha256"],
        "original complete gate receipt changed")
    require(len(scientific_raw)==expected["science_canonical_bytes"]
        and sha(scientific_raw)==expected["science_canonical_sha256"],
        "original full scientific bytes changed")
    require(len(raw)==expected["file_bytes"] and sha(raw)==expected["file_sha256"]
        and git_blob(raw)==expected["file_git_blob"],"original file identity changed")
    if embedded:
        require({key:whole[key] for key in expected["wrapper_identity"]}==expected["wrapper_identity"],
                "original wrapper identity changed")
        require(whole["complete"] is True and whole["actual_returncode"]==0
            and whole["actual_failure"] is None and whole["actual_source_budget_processes"]==1
            and whole["run_id"]==science["run_id"] and whole["run_attempt"]==science["run_attempt"]
            and whole["workflow_commit"]==science["workflow_event_commit"]
            and whole["actual_scientific_checkout_commit"]==science["actual_scientific_checkout_commit"]
            and whole["source_budget_source_sha256"]==science["source_sha256"]
            and whole["input_manifest_sha256"]==science["input_manifest_sha256"],
            "embedded scientific and wrapper chains changed")
        outputs={entry["file"]:entry for entry in whole["output_hashes"]}
        require(outputs["consumers/process.json"]["bytes"]==len(scientific_raw)
            and outputs["consumers/process.json"]["sha256"]==sha(scientific_raw),
            "original complete process receipt changed")
    else:
        require(scientific_raw==raw,"original standalone canonical bytes changed")
    receipt=copy.deepcopy(expected)
    require(receipt==EXPECTED_ACCEPTED["original_successes"][role],"accepted identity changed")
    return science,receipt

def accepted_original_inputs(paths,doc):
    originals={}
    accepted={"original_successes":{}}
    for index,role in enumerate(("pc_execution","tf_science","wx_execution","wt_science","sei_execution"),3):
        science,receipt=original_science(role,paths[role])
        originals[role]=science
        accepted["original_successes"][role]=receipt
        doc["accepted_old_inputs"]=copy.deepcopy(accepted)
        doc["actual_progress"]["accepted_original_successes"]+=1
        gate(doc,index,receipt==EXPECTED_ACCEPTED["original_successes"][role])

    pc,tf,wx,wt,sei=[originals[role] for role in
        ("pc_execution","tf_science","wx_execution","wt_science","sei_execution")]
    pp,dp,cp,vp=pc["mathematical_parameters"],pc["complete_positive_domain_conclusion"],\
        pc["complete_cutoff_and_head_conclusion"],pc["complete_positive_volume_conclusion"]
    sp=pc["complete_strong_correction_conclusion"]
    gate(doc,8,pp["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
        and pp["fixed_intrinsic_parameter"]==PARAMETERS["fixed_intrinsic_parameter"]
        and pp["exact_root_interval"]==PARAMETERS["exact_root_interval"]
        and pp["physical_root_piece"]==2549 and pp["cutoff_abs_j"]==97
        and pp["physical_frequency"]=="n=4|j|" and pp["both_carrier_signs"] is True
        and pp["exact_reference_terminal_T"]=="1/2000"
        and pp["exact_transition_s_interval"]==PARAMETERS["exact_PC_positive_transition"]
        and dp["exact_p_strip"]==cp["exact_holomorphic_p_strip"]=="1/256"
        and dp["exact_new_shift"]==cp["exact_contour_shift"]=="1/512"
        and cp["exact_transition_derivative_upper"]=="1875000"
        and cp["exact_transition_length"]=="1/1000000"
        and dp["same_complete_terminal_solution_and_root_shear"] is True
        and dp["all_six_required_holomorphic_domains_checked"] is True
        and dp["DG_full_disk_g_used_not_RJ_negative_six_row_max"] is True
        and cp["physical_mean_and_full_head_retained"] is True
        and cp["negative_Sobolev_operator_norm_not_used_as_same_shift_L2"] is True
        and vp["exact_same_shift_paid_matrix_width"]=="1/64"
        and pc["scope"]["full_J_L_B_same_shift_exponential_matrix_domain"] is True
        and pc["scope"]["full_positive_correction_seven_port_graph_consumed"] is True
        and pc["scope"]["all_three_raw_local_vectors"] is True
        and pc["scope"]["terminal_Ai_solution_not_replaced_by_root_Ai"] is True
        and sp["genuine_root_beta_shear_not_discarded"] is True
        and sp["full_root_finite_head_and_two_mean_inputs_retained"] is True
        and sp["outgoing_unstable_root_trace_paid_by_complete_seven_port_graph"] is True)

    tp,wp,wtp,ep=tf["parameters"],wx["mathematical_parameters"],wt["parameters"],sei["mathematical_parameters"]
    tr,tn,ts=tf["complete_new_root_coefficient_conclusion"],tf["complete_new_root_normalizer_conclusion"],tf["complete_new_strong_scalar_factors"]
    wc=wx["complete_selected_common_input_conclusion"]
    wh=wx["complete_selected_H_coordinate_conclusion"]
    wr=wx["complete_full_primitive_rank_conclusion"]["selected_common_input"]
    waist=wt["complete_fixed_cutoff_results"][1]
    esc=sei["complete_selected_common_input_scope_read_verbatim"]
    gate(doc,9,all(p["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
            and p["fixed_intrinsic_parameter"]=="eta_0"
            and p["exact_root_interval"]==PARAMETERS["exact_root_interval"] for p in (tp,wp))
        and tp["exact_strict_cut"]==wp["exact_strict_cut"]==PARAMETERS["exact_strict_cut"]
        and tp["continuous_centre_definition_sha256"]==ep["continuous_centre_definition_sha256"]
        and tp["continuous_response_definition_sha256"]==ep["continuous_response_definition_sha256"]
        and tr["angular_degree"]==192 and tr["root_mean_and_both_Fourier_signs_retained"] is True
        and tr["original_full_complex_eta_domain_includes_root"] is True
        and tn["actual_J_F"]==1024 and tn["same_inverse_on_both_windows"] is True
        and tn["below_J_F_and_independent_mean_ports_are_identity"] is True
        and tn["finite_original_input_and_output_support_abs_j"]==1215
        and tn["right_transformed_finite_input_support_not_claimed"] is True
        and tn["right_transformed_finite_rows_keep_actual_dual_norms"] is True
        and ts["finite_fee_is_one_complete_branch_fee_with_full_mean"] is True
        and wc["only_same_selected_actual_conjugacy"] is True
        and wc["exact_order"]==esc["exact_order"]=="S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)"
        and wc["inverse_order"]==esc["inverse_order"]=="S_inverse = U_X_minus_inverse U_H"
        and wc["selected_parameter_absolute_upper"]==esc["selected_parameter_absolute_upper"]
            ==PARAMETERS["exact_selected_parameter_absolute_upper"]
        and wh["same_actual_inverse_on_L2_and_Hminus4_3"] is True
        and wh["independent_physical_mean_block_is_identity"] is True
        and wr["both_finite_rank_terms_and_the_full_mean_retained"] is True
        and wt["copied_SP_family_identity"]["continuous_centre_definition_sha256"]
            ==tp["continuous_centre_definition_sha256"]
        and wt["copied_SP_family_identity"]["continuous_response_definition_sha256"]
            ==tp["continuous_response_definition_sha256"]
        and wt["copied_SP_family_identity"]["fixed_current_eta"]=="eta_0"
        and wtp["exact_delta_half_width"]==PARAMETERS["exact_real_delta_radius"]
        and wtp["exact_eta0"]==PARAMETERS["exact_intrinsic_parameter"]
        and wtp["exact_waist"]=="0" and wtp["radial_trace_side"]=="right"
        and sum(row["J"]==268435456 for row in wt["complete_fixed_cutoff_results"])==1
        and waist["J"]==268435456 and waist["finite_complement_and_two_means_identity"] is True
        and waist["inverse_on_both_windows_proved"] is True
        and len(waist["all_four_strict_tests"])==4
        and all(row["passed"] is True for row in waist["all_four_strict_tests"])
        and wt["new_coefficient_scope"]["all_true_means_retained"] is True
        and wt["new_coefficient_scope"]["whole_core_D_delta_fee_extended"] is False
        and ep["true_angle_only_at_original_selected_parameter"] is True
        and ep["independent_physical_mean_coordinates"]==2
        and sei["scope"]["full_signed_mu_and_two_physical_means_retained"] is True
        and sei["scope"]["only_complete_SN_terminal_never_a_prefix_used"] is True
        and sei["scope"]["same_selected_real_individual_ci_co"] is True)

    scopes={role:{".".join(map(str,path)):copy.deepcopy(get_path(originals[role],path))
            for path in role_paths} for role,role_paths in SCOPE_PATHS.items()}
    records={
        "WPC":{name:copy.deepcopy(get_path(originals[path[0]],path[1:]))
               for name,path in WPC_SCALAR_PATHS.items()},
        "WCE":{name:copy.deepcopy(get_path(originals[path[0]],path[1:]))
               for name,path in WCE_SCALAR_PATHS.items()},
    }
    qualifications={name:copy.deepcopy(get_path(originals[path[0]],path[1:]))
                    for name,path in QUALIFICATION_PATHS.items()}
    require(all(isinstance(value,dict) and set(value)=={"ball"}
        and isinstance(value["ball"],str)
        for collection in records.values() for value in collection.values()),
        "original whole bound records changed type")
    require(set(qualifications["signed_mu"])=={"ball","lower","upper"}
        and all(isinstance(value,str) for value in qualifications["signed_mu"].values())
        and all(isinstance(qualifications[key],dict) and set(qualifications[key])=={"ball"}
            and isinstance(qualifications[key]["ball"],str)
            for key in ("selected_H_derivative_lower","selected_H_derivative_upper")),
        "original whole signed mean and derivative qualifications changed")
    # These are typed outward reads, not regenerated copies or old targets.
    require(all(up(value).is_finite() for collection in records.values() for value in collection.values()),
        "nonfinite saved upper role")
    require(lower(records["WPC"]["Tmin"])>0 and lower(records["WPC"]["m"])>0
        and lower(records["WCE"]["psi_derivative_lower"])>0,"required saved denominator lower")
    require(arb(qualifications["signed_mu"]["ball"]).is_finite(),"signed mean must stay full")
    require(lower(qualifications["selected_H_derivative_lower"])>=ex(31)/32
        and up(qualifications["selected_H_derivative_upper"])<=ex(33)/32,
        "original H derivative qualification changed")
    doc["copied_complete_original_scopes"]=scopes
    doc["copied_complete_original_scopes_sha256"]=sha(canonical(scopes))
    doc["copied_original_scalar_records"]=records
    doc["copied_original_scalar_records_sha256"]=sha(canonical(records))
    doc["copied_original_qualification_records"]=qualifications
    doc["copied_original_qualification_records_sha256"]=sha(canonical(qualifications))
    accepted.update(original_scope_collections_sha256=sha(canonical(scopes)),
        original_bound_records_sha256=sha(canonical(records)),
        original_qualification_records_sha256=sha(canonical(qualifications)),
        original_complete_science_objects_not_recomputed=True,
        original_scope_fragments_are_exact_full_path_values=True)
    doc["accepted_old_inputs"]=accepted
    doc["actual_progress"]["copied_original_bound_records"]=42
    doc["actual_progress"]["copied_original_qualification_records"]=3
    doc["actual_progress"]["copied_original_scope_collections"]=5
    gate(doc,10,len(records["WPC"])==25 and len(records["WCE"])==17
        and len(qualifications)==3 and len(scopes)==5
        and sha(canonical(scopes))==FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256
        and sha(canonical(records))==FROZEN_SAVED_SCALAR_RECORDS_SHA256
        and sha(canonical(qualifications))==FROZEN_QUALIFICATION_RECORDS_SHA256
        and accepted==EXPECTED_ACCEPTED
        and sha(canonical(accepted))==FROZEN_ACCEPTED_OLD_INPUTS_SHA256)
    doc["complete_operator_identity_conclusion"]=copy.deepcopy(OPERATOR_IDENTITY)
    return records

# Pure directed scalar helpers. This file fragment has no entry point.
def ball(value):
    if isinstance(value, dict):
        if set(value) != {"ball"}:
            raise TypeError("one complete scalar record required")
        value = value["ball"]
    return value if isinstance(value, arb) else arb(str(value))

def ex(value):
    return arb(str(value))

def up(value):
    value = ball(value)
    if not value.is_finite() or value.lower() < 0:
        raise ArithmeticError("finite nonnegative upper bound required")
    return value.upper()

def lower(value):
    value = ball(value)
    if not value.is_finite() or value.lower() <= 0:
        raise ArithmeticError("finite strictly positive lower endpoint required")
    return value.lower()

def rec(value):
    return {"ball": up(value).str(75)}

def retained_up(record):
    return up(record)

def whole_choice(candidates):
    if not candidates:
        raise ValueError("at least one complete candidate required")
    selected_label = next(iter(candidates))
    selected = retained_up(candidates[selected_label])
    for label, record in candidates.items():
        bound = retained_up(record)
        if bound < selected:
            selected_label, selected = label, bound
    return {"selected_label": selected_label,
            "complete_selected_upper": copy.deepcopy(candidates[selected_label]),
            "all_candidates_retained": True}

def wpc_geometry_and_moments(records):
    """WPC.7--14,18--19: new actual-window factors and shifted profiles."""
    n = ex(388)
    m = lower(records["m"])
    tmin = lower(records["Tmin"])
    ca = up(records["CA"])
    cx = up(records["CX"])
    z0, z1 = up(records["Z0"]), up(records["Z1"])
    y0, y1 = up(records["Y0"]), up(records["Y1"])
    v0, v1 = up(records["V"]), up(records["VT"])
    kin = up((ex(1) + ex(1)/(n*n)) ** (ex(1)/3))
    cl2 = up(ex(1)/m.sqrt())
    cx23 = up(cl2 ** (ex(3)/5) * cx ** (ex(2)/5))
    qword = up(ex(64)/63 * ex(16) ** (ex(2)/3))
    prefactor = up(kin * ca * tmin ** (-ex(11)/4))
    radial = up(ex(1875000) * (ex(1)/ex(1000000)).sqrt())
    n13, ninv = up(n ** (-ex(1)/3)), up(ex(1)/n)
    moments = {}
    for numerator in (11, 13, 15, 17, 19, 23, 25):
        p = ex(numerator)/4
        moments[str(numerator)+"/4"] = rec((ex(3)*p/8) ** (ex(2)*p/3))
    sm = {key: retained_up(value) for key, value in moments.items()}
    a = [
        sm["11/4"],
        up(z0 * (sm["15/4"] + sm["17/4"])),
        up(z0*z0*sm["23/4"] + v0*y0*y0*sm["11/4"]
           + z1*(sm["15/4"] + sm["17/4"])),
    ]
    b = [
        up(n13*(sm["11/4"] + sm["13/4"])),
        up(n13*z0*sm["19/4"] + v0*ninv*y0*sm["11/4"]),
        up(n13*(z0*z0*(sm["19/4"] + sm["23/4"] + sm["25/4"])
             + z1*sm["19/4"] + v0*y0*y0*(sm["11/4"] + sm["13/4"]))
           + ninv*(v1*y0*y0 + v0*y1)*sm["11/4"]),
    ]
    aa, bb = [rec(x) for x in a], [rec(x) for x in b]
    gamma = [rec(max(retained_up(aa[k]), retained_up(bb[k]))) for k in range(3)]
    return {
        "geometry": {
            "frequency_Bessel_factor_upper": rec(kin),
            "scalar_pullback_L2_upper": rec(cl2),
            "scalar_pullback_Hminus2_3_upper": rec(cx23),
            "complete_same_shift_matrix_weight_upper": rec(qword),
            "complete_shifted_profile_prefactor_upper": rec(prefactor),
            "physical_cutoff_radial_factor_upper": rec(radial),
            "frequency_minus_one_third_upper": rec(n13),
            "frequency_inverse_upper": rec(ninv),
        },
        "shifted_moment_upper": moments,
        "complete_a_profile_derivative_upper": aa,
        "complete_b_profile_derivative_upper": bb,
        "complete_pair_profile_derivative_upper": gamma,
        "exact_profile_moment_shift": "5/2",
        "exact_total_Tmin_exponent": "-11/4",
        "old_Airy_profiles_or_exponential_sums_recomputed": False,
        "full_two_sign_matrix_including_all_output_modes": True,
    }

def wpc_cauchy_and_schur(records, foundation):
    """WPC.14--18: full-strip Cauchy lists and all-output weighted Schur."""
    strip = ex(1)/ex(256)
    w, wd = up(records["W"]), up(records["WD"])
    p0, h, g = up(records["P0"]), up(records["H"]), up(records["G"])
    m, f2 = lower(records["m"]), up(records["F2"])
    amplitude = {
        "w": [rec(w), rec(w/strip), rec(ex(2)*w/(strip*strip))],
        "h": [rec(h), rec(h/strip), rec(ex(2)*h/(strip*strip))],
        "g": [rec(g), rec(wd/strip + ex(2)*p0/(strip*strip)),
              rec(ex(2)*wd/(strip*strip) + ex(6)*p0/(strip*strip*strip))],
    }
    geom = foundation["geometry"]
    prefactor = retained_up(geom["complete_shifted_profile_prefactor_upper"])
    pullback = retained_up(geom["scalar_pullback_Hminus2_3_upper"])
    gamma = [retained_up(x) for x in foundation["complete_pair_profile_derivative_upper"]]
    result = {}
    for name in ("w", "h", "g"):
        d0, d1, d2 = [retained_up(x) for x in amplitude[name]]
        raw = [
            rec(prefactor*gamma[0]*d0),
            rec(prefactor*(gamma[0]*d1 + gamma[1]*d0)),
            rec(prefactor*(gamma[0]*d2 + ex(2)*gamma[1]*d1 + gamma[2]*d0)),
        ]
        b0, b1, b2 = [retained_up(x) for x in raw]
        inverse_second = rec(b2/(m*m) + f2*b1/(m*m*m))
        result[name] = {
            "complete_amplitude_angular_derivative_upper": amplitude[name],
            "complete_weighted_phase_derivative_upper": raw,
            "complete_inverse_angle_second_derivative_upper": inverse_second,
            "complete_Hminus4_3_to_Hminus2_3_upper":
                rec(pullback*(b0 + ex(3)*retained_up(inverse_second)/2)),
        }
    return {
        "complete_three_amplitude_functionals": result,
        "exact_full_holomorphic_strip": "1/256",
        "g_second_derivative_includes_complete_p_third_derivative": True,
        "no_unsaved_RJ_jet_used": True,
        "full_two_row_reconstruction_not_replaced_by_one_height": True,
        "all_output_means_and_original_P_retained": True,
    }

def wpc_complete_positive_candidate(records, foundation, functionals):
    """WPC.21--23: exact ordered two-row cutoff and whole received choice."""
    qword = retained_up(foundation["geometry"]["complete_same_shift_matrix_weight_upper"])
    radial = retained_up(foundation["geometry"]["physical_cutoff_radial_factor_upper"])
    by = functionals["complete_three_amplitude_functionals"]
    fw, fh, fg = [retained_up(by[key]["complete_Hminus4_3_to_Hminus2_3_upper"])
                  for key in ("w", "h", "g")]
    zj, zb, zl = up(records["J"]), up(records["B"]), up(records["L"])
    jl, jb = rec(qword*zj*zl), rec(qword*zj*zb)
    j = rec(qword*zj)
    first_terms = [
        rec((ex(1)+retained_up(jl))*fh),
        rec(retained_up(j)*fg),
        rec(retained_up(jb)*fw),
    ]
    first = rec(sum((retained_up(x) for x in first_terms), ex(0)))
    second = rec(fw)
    cut = rec(radial*(retained_up(first)*retained_up(first)
                      + retained_up(second)*retained_up(second)).sqrt())
    source = rec(up(records["Cvol"]) + retained_up(cut) + up(records["CFH"]))
    received = rec(up(records["Kpos"])*retained_up(source))
    candidates = {"saved_complete_positive": copy.deepcopy(records["old_positive_received"]),
                  "new_actual_output_window_cutoff": received}
    return {
        "complete_ordered_J_word_upper": j,
        "complete_ordered_JL_word_upper": jl,
        "complete_ordered_JB_word_upper": jb,
        "complete_first_row_term_upper": first_terms,
        "complete_first_row_upper": first,
        "complete_second_row_upper": second,
        "complete_cutoff_source_upper": cut,
        "complete_positive_source_upper": source,
        "complete_received_positive_candidate_upper": received,
        "whole_received_positive_candidates": candidates,
        "whole_received_positive_choice": whole_choice(candidates),
        "same_original_PC_trial_and_cutoff": True,
        "complete_ordinary_volume_and_finite_head_source_read_only": True,
        "already_received_Kpos_used_exactly_once": True,
        "root_finite_received_term_is_separate_and_unchanged": True,
        "full_means_genuine_root_shear_and_terminal_column_retained": True,
        "new_positive_reception_is_same_Rplus_in_WUE": True,
        "full_incoming_or_finite_border_inverse_claimed": False,
    }

# WCE mathematical fragment. No calls occur at import.
# Host helpers:
#   ex(integer), up(value), lower(signed_ball_string)
#   rec(value) -> {"ball": up(value).str(75)}
#   retained_up(record) -> finite upward endpoint of the saved record
#   whole_choice({label: record}) -> selected_label, complete_selected_upper
#       (deepcopy of the entire final record), all_candidates_retained.
# The host admits all four complete original receipts before these functions.
# saved is the exact seventeen-role record dictionary specified separately.
# Three qualification records are preserved by the reader, not recalculated.
# No exponent, logarithm, profile, old producer, or old target is evaluated.

def wce_root_bounds(saved):
    """WCE18--24: seven new complete scalar records."""
    ci = retained_up(saved["ci_Linfty"])
    mu = retained_up(saved["mu_absolute"])
    h2 = retained_up(saved["vi_Bessel_H2"])
    mpsi = lower(saved["psi_derivative_lower"]["ball"])
    if not mpsi > 0:
        raise ValueError("WCE true density derivative lower must be positive")

    nu = rec(mu / ex(2))
    v43 = rec((ex(243) / ex(160)) * h2)
    ki = rec(ex(1) + (retained_up(nu) + retained_up(v43)) / ex(4))
    croot = rec(ci / mpsi)
    two_i = rec(retained_up(croot) * retained_up(saved["TF_two_primitive_after_right"]))
    root = rec(retained_up(two_i) + retained_up(saved["TF_finite_after_right"]))
    conjugated = rec(
        retained_up(saved["S_L2"])
        * retained_up(root)
        * retained_up(saved["S_inverse_Hminus4_3"])
    )
    return {
        "complete_absolute_incoming_mean_upper": nu,
        "complete_nonmean_Wfour_thirds_upper": v43,
        "complete_incoming_forward_Hminus4_3_upper": ki,
        "complete_root_coefficient_Linfty_upper": croot,
        "complete_root_two_primitive_fee_upper": two_i,
        "complete_root_strong_fee_upper": root,
        "complete_conjugated_root_strong_fee_upper": conjugated,
        "input_window": "H^(-4/3)",
        "output_window_for_root_strong_fees": "L2",
        "exact_order": "S (F_J - M_c I A_F) T_F_inverse S_inverse",
        "only_denominator_from_true_psi_lower": True,
        "TF_after_right_factors_read_once": True,
        "no_second_TF_inverse_or_Ni_factor": True,
        "old_CI_B_product_not_recomputed": True,
        "root_FJ_full_mean_and_dual_rows_retained": True,
    }


def wce_rank_bounds(saved, root):
    """WCE10,15--17,25: six new records, two complete rank routes."""
    ci = retained_up(saved["ci_Linfty"])
    p43 = retained_up(saved["psi_displacement_H4_3"])
    pinf = retained_up(saved["psi_displacement_Linfty"])
    nu = retained_up(root["complete_absolute_incoming_mean_upper"])
    dev = up(ex(1) / ex(31))

    first = rec(ci * p43)
    second = rec(ci * pinf)
    full = rec(retained_up(first) + retained_up(second))
    density_mean = rec(nu * dev)
    projected_coefficient = rec(
        retained_up(saved["vi_L2"]) + retained_up(density_mean)
    )
    projected = rec(retained_up(projected_coefficient) * p43)
    return {
        "complete_full_first_primitive_rank_upper": first,
        "complete_full_second_primitive_rank_upper": second,
        "complete_full_two_primitive_ranks_upper": full,
        "complete_projected_density_mean_coefficient_upper": density_mean,
        "complete_projected_rank_coefficient_L2_upper": projected_coefficient,
        "complete_projected_primitive_rank_upper": projected,
        "exact_density_deviation_upper": "1/31",
        "exact_full_rank_formula": "ci tensor ppsi - (ci*ppsi) tensor 1",
        "exact_projected_rank_on_actual_input": "(vi - nu*(h-1)) tensor ppsi",
        "full_density_S_preserves_the_integral": True,
        "zero_input_mean_only_on_actual_Xfr": True,
        "both_full_primitive_ranks_written_before_restriction": True,
        "only_projected_Ecoeff_equals_projected_E0": True,
        "physical_density_mean_rank_not_removed": True,
    }


def wce_waist_bounds(saved, root):
    """WCE20,26--30: six new complete same-waist records."""
    hi0 = retained_up(saved["H_inverse_L2"])
    h0 = retained_up(saved["H_L2"])
    hm = retained_up(saved["H_Hminus4_3"])
    dev = up(ex(1) / ex(31))

    vw = rec(hi0 * retained_up(saved["WT_forward_strong_remainder"]) * hm)
    vw0 = rec(hi0 * retained_up(saved["WT_tau2_L2"]) * h0)
    aj = rec(ex(1) + retained_up(vw0))
    physical_two_i = rec(
        retained_up(vw) * retained_up(root["complete_incoming_forward_Hminus4_3_upper"])
    )
    physical_mean = rec(dev * retained_up(saved["mean_row_CI_B"]))
    row = rec(retained_up(physical_two_i) + retained_up(physical_mean))
    return {
        "complete_waist_second_normalizer_strong_upper": vw,
        "complete_waist_second_normalizer_L2_upper": vw0,
        "complete_waist_forward_L2_upper": aj,
        "complete_physical_two_primitive_row_upper": physical_two_i,
        "complete_physical_density_mean_rank_upper": physical_mean,
        "complete_physical_row_sum_upper": row,
        "actual_moving_Js": 268435456,
        "exact_first_waist_normalizer_is_zero_by_WPL": True,
        "actual_second_normalizer_and_minus_Sr_retained": True,
        "old_complete_Id_plus_A1_times_A2_fee_read_verbatim": True,
        "no_old_first_finite_fee_subtracted": True,
        "reflected_pair_sqrt_two_cancels_on_both_sides": True,
        "exact_Vw_order": "U_H_inverse B_w U_H",
        "two_independent_physical_mean_ports_retained": True,
    }


def wce_complete_candidates(saved, root, ranks, waist):
    """WCE31--32: eight new records, then one whole-record selection."""
    hi0 = retained_up(saved["H_inverse_L2"])
    aj0 = retained_up(waist["complete_waist_forward_L2_upper"])
    common_row = retained_up(waist["complete_physical_row_sum_upper"])
    sroot = retained_up(root["complete_conjugated_root_strong_fee_upper"])

    full_before = rec(retained_up(ranks["complete_full_two_primitive_ranks_upper"]) + sroot)
    full_projected = rec(hi0 * retained_up(full_before))
    full_algebra = rec(aj0 * retained_up(full_projected))
    full = rec(common_row + retained_up(full_algebra))

    projected_root = rec(hi0 * sroot)
    projected_before = rec(
        retained_up(ranks["complete_projected_primitive_rank_upper"])
        + retained_up(projected_root)
    )
    projected_algebra = rec(aj0 * retained_up(projected_before))
    projected = rec(common_row + retained_up(projected_algebra))
    choices = {"full_ranks": full, "projected_ranks": projected}
    choice = whole_choice(choices)
    return {
        "complete_full_rank_and_root_before_projection_upper": full_before,
        "complete_full_candidate_after_projection_upper": full_projected,
        "complete_full_candidate_algebra_upper": full_algebra,
        "complete_full_Calg_upper": full,
        "complete_projected_root_upper": projected_root,
        "complete_projected_rank_and_root_upper": projected_before,
        "complete_projected_candidate_algebra_upper": projected_algebra,
        "complete_projected_Calg_upper": projected,
        "complete_whole_choice": choice,
        "operator": "D_alg = Lpartial Y_WJ Ni - Qa Ti",
        "source": "Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3",
        "target": "P Fix(Ra) intersect L2",
        "same_complete_operator_and_leading_row_for_both_candidates": True,
        "whole_choice_uses_final_retained_outward_records": True,
        "full_and_projected_candidates_both_saved": True,
        "physical_mean_rank_and_TF_finite_rank_retained": True,
        "positive_negative_endpoint_state_errors_remain_separate": True,
        "input_normalizer_not_reapplied_to_coefficient_error": True,
        "no_full_physical_incoming_or_finite_inverse_claimed": True,
    }


def complete_graph_shape(value,shape):
    if shape=="record":
        return (isinstance(value,dict) and set(value)=={"ball"}
            and isinstance(value["ball"],str)
            and arb(value["ball"]).is_finite() and arb(value["ball"]).lower()>=0)
    if shape=="label":
        return isinstance(value,str) and 0<len(value)<128
    if isinstance(shape,str):
        return shape.startswith("=") and value==shape[1:]
    if isinstance(shape,bool):
        return value is shape
    if isinstance(shape,int):
        return type(value) is int and value==shape
    if isinstance(shape,list):
        return (isinstance(value,list) and len(value)==len(shape)
            and all(complete_graph_shape(v,s) for v,s in zip(value,shape)))
    if isinstance(shape,dict):
        return (isinstance(value,dict) and set(value)==set(shape)
            and all(complete_graph_shape(value[key],spec) for key,spec in shape.items()))
    return False

def scalar_slot_count(value,shape):
    if shape=="record":
        return 1
    if isinstance(shape,list):
        return sum(scalar_slot_count(v,s) for v,s in zip(value,shape))
    if isinstance(shape,dict):
        return sum(scalar_slot_count(value[key],spec) for key,spec in shape.items())
    return 0

def whole_choice_is_retained(choice,candidates):
    if set(choice)!={"selected_label","complete_selected_upper","all_candidates_retained"}:
        return False
    label=choice["selected_label"]
    if label not in candidates or choice["all_candidates_retained"] is not True:
        return False
    if choice["complete_selected_upper"]!=candidates[label]:
        return False
    selected=retained_up(choice["complete_selected_upper"])
    if any(selected>retained_up(value) for value in candidates.values()):
        return False
    # An exact tie retains the first complete candidate in its declared order.
    for candidate,record in candidates.items():
        if retained_up(record)==selected:
            return candidate==label
    return False


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--bits",type=int,default=320)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError("refusing to overwrite any complete or partial scientific result")
    ctx.prec=args.bits
    doc={key:None for key in COMPLETE_FIELDS}
    doc.update(kind=KIND,complete=False,proved=False,actual_returncode=None,failure=None,
        stage="initial_current_input_admission",source_sha256=sha(Path(__file__).read_bytes()),
        input_manifest_sha256=sha(args.manifest.read_bytes()),public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        runtime={},arithmetic_bits=args.bits,parameters=copy.deepcopy(PARAMETERS),
        input_sha256={},verified_original_inputs={},accepted_old_inputs={},
        copied_complete_original_scopes={},copied_complete_original_scopes_sha256=None,
        copied_original_scalar_records={},copied_original_scalar_records_sha256=None,
        copied_original_qualification_records={},copied_original_qualification_records_sha256=None,
        retained_scope=copy.deepcopy(RETAINED_SCOPE),planned_shape=copy.deepcopy(PLANNED_SHAPE),
        actual_progress=copy.deepcopy(INITIAL_ACTUAL_PROGRESS),gates=[],
        actual_mathematical_wall_seconds=0)
    began=time.monotonic()
    try:
        manifest,paths=checked_inputs(args,doc)
        doc["stage"]="complete_saved_actual_admission"
        saved=accepted_original_inputs(paths,doc)
        persist(args.out,doc)

        doc["stage"]="complete_new_WPC_geometry_and_moments"
        key="complete_wpc_geometry_and_moment_conclusion"
        doc[key]=wpc_geometry_and_moments(saved["WPC"])
        doc["actual_progress"]["new_wpc_geometry_and_moment_graphs"]=1
        gate(doc,11,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==24)
        persist(args.out,doc)

        doc["stage"]="complete_new_WPC_Cauchy_and_Schur"
        key="complete_wpc_cauchy_and_schur_conclusion"
        doc[key]=wpc_cauchy_and_schur(saved["WPC"],doc["complete_wpc_geometry_and_moment_conclusion"])
        doc["actual_progress"]["new_wpc_cauchy_and_schur_graphs"]=1
        gate(doc,12,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==24)
        persist(args.out,doc)

        doc["stage"]="complete_new_WPC_received_positive_candidate"
        key="complete_wpc_positive_correction_conclusion"
        doc[key]=wpc_complete_positive_candidate(saved["WPC"],
            doc["complete_wpc_geometry_and_moment_conclusion"],
            doc["complete_wpc_cauchy_and_schur_conclusion"])
        doc["actual_progress"]["new_wpc_complete_positive_candidates"]=1
        doc["actual_progress"]["new_whole_candidate_choices"]=1
        gate(doc,13,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==14
            and doc[key]["whole_received_positive_candidates"]["saved_complete_positive"]
                ==saved["WPC"]["old_positive_received"])
        persist(args.out,doc)

        doc["stage"]="complete_new_WCE_root_factors"
        key="complete_wce_root_coefficient_conclusion"
        doc[key]=wce_root_bounds(saved["WCE"])
        doc["actual_progress"]["new_wce_root_graphs"]=1
        gate(doc,14,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==7)
        persist(args.out,doc)

        doc["stage"]="complete_new_WCE_primitive_ranks"
        key="complete_wce_projected_rank_conclusion"
        doc[key]=wce_rank_bounds(saved["WCE"],doc["complete_wce_root_coefficient_conclusion"])
        doc["actual_progress"]["new_wce_rank_graphs"]=1
        gate(doc,15,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==6)
        persist(args.out,doc)

        doc["stage"]="complete_new_WCE_exact_waist_factors"
        key="complete_wce_waist_conclusion"
        doc[key]=wce_waist_bounds(saved["WCE"],doc["complete_wce_root_coefficient_conclusion"])
        doc["actual_progress"]["new_wce_waist_graphs"]=1
        gate(doc,16,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==6)
        persist(args.out,doc)

        doc["stage"]="complete_new_WCE_whole_algebraic_candidates"
        key="complete_wce_algebraic_conclusion"
        doc[key]=wce_complete_candidates(saved["WCE"],
            doc["complete_wce_root_coefficient_conclusion"],
            doc["complete_wce_projected_rank_conclusion"],
            doc["complete_wce_waist_conclusion"])
        doc["actual_progress"]["new_wce_complete_candidate_graphs"]=1
        doc["actual_progress"]["new_whole_candidate_choices"]=2
        gate(doc,17,complete_graph_shape(doc[key],NEW_GRAPH_SHAPES[key])
            and scalar_slot_count(doc[key],NEW_GRAPH_SHAPES[key])==9)
        persist(args.out,doc)

        doc["stage"]="complete_final_readonly_and_shape_checks"
        wp=doc["complete_wpc_positive_correction_conclusion"]
        we=doc["complete_wce_algebraic_conclusion"]
        gate(doc,18,whole_choice_is_retained(wp["whole_received_positive_choice"],
                wp["whole_received_positive_candidates"])
            and wp["whole_received_positive_candidates"]["new_actual_output_window_cutoff"]
                ==wp["complete_received_positive_candidate_upper"]
            and whole_choice_is_retained(we["complete_whole_choice"],
                {"full_ranks":we["complete_full_Calg_upper"],
                 "projected_ranks":we["complete_projected_Calg_upper"]}))
        gate(doc,19,all(sha(paths[entry["role"]].read_bytes())==entry["sha256"]
                for entry in manifest["files"])
            and sha(args.manifest.read_bytes())==doc["input_manifest_sha256"]==args.manifest_sha
            and sha(canonical(doc["copied_complete_original_scopes"]))==FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256
            and sha(canonical(doc["copied_original_scalar_records"]))==FROZEN_SAVED_SCALAR_RECORDS_SHA256
            and sha(canonical(doc["copied_original_qualification_records"]))==FROZEN_QUALIFICATION_RECORDS_SHA256
            and sha(canonical(doc["accepted_old_inputs"]))==FROZEN_ACCEPTED_OLD_INPUTS_SHA256
            and all(doc["actual_progress"][name]==0 for name in
                ("old_scientific_targets_recomputed",
                 "old_profiles_exponential_sums_or_integrals_recomputed",
                 "old_completed_scalar_products_recomputed",
                 "old_exponentials_or_logarithms_evaluated",
                 "historical_or_native_inputs_restored",
                 "old_scientific_producers_imported_or_called")))
        gate(doc,20,all(complete_graph_shape(doc[key],shape)
                and scalar_slot_count(doc[key],shape)==NEW_GRAPH_SLOT_COUNTS[key]
                for key,shape in NEW_GRAPH_SHAPES.items())
            and sum(scalar_slot_count(doc[key],shape) for key,shape in NEW_GRAPH_SHAPES.items())==90
            and doc["planned_shape"]==PLANNED_SHAPE
            and doc["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and doc["complete_operator_identity_conclusion"]==OPERATOR_IDENTITY)
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-began
        gate(doc,21,set(doc)==set(COMPLETE_FIELDS) and len(doc)==38
            and doc["retained_scope"]==RETAINED_SCOPE
            and len(doc["gates"])==21
            and [row["name"] for row in doc["gates"]]==GATE_NAMES[:21]
            and all(row["passed"] is True for row in doc["gates"])
            and doc["parameters"]==PARAMETERS)
        doc.update(complete=True,proved=True,actual_returncode=0,failure=None,stage="complete")
    except BaseException as error:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure={"type":type(error).__name__,"message":str(error),"traceback":traceback.format_exc()},
            actual_mathematical_wall_seconds=time.monotonic()-began)
        doc["failed_new_stage_diagnostic"]={
            "stage":doc["stage"],
            "accepted_original_success_count":doc["actual_progress"]["accepted_original_successes"],
            "returned_graph_fields_available":[key for key in NEW_GRAPH_SHAPES if isinstance(doc.get(key),dict)],
            "all_original_scientific_targets_remain_frozen":True,
            "complete_new_positive_candidate_authorized":False,
            "complete_new_reflected_coefficient_candidate_authorized":False}
        persist(args.out,doc)
        print_complete_document(doc)
        raise
    raw=persist(args.out,doc)
    print_complete_document(doc)
    if len(raw)>COMPLETE_SCIENCE_MAX_BYTES:
        raise ValueError("complete science saved and printed; publication byte budget exceeded")

if __name__=="__main__":
    main()
