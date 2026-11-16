#!/usr/bin/env python3
"""New Schur/Parseval positive bound and exact coefficient-remainder bounds.
The complete prior scientific object is read and retained once, verbatim.
Only the new positive combinations specified by WSP and WCF are evaluated.
No prior producer, geometry, profile, old product, exponential or log is run.
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
SOURCE="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_cutoff_Schur_Parseval.py"
WORKER="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_cutoff_Schur_Parseval_public_worker.py"
KIND="complete_positive_cutoff_Schur_Parseval_and_coefficient_split_v1"
MANIFEST_KIND="positive_cutoff_Schur_Parseval_and_coefficient_split_current_only_inputs"
SCALAR_SENTINEL="__FINITE_NONNEGATIVE_SCALAR_RECORD__"
LABEL_SENTINEL="__WHOLE_POSITIVE_CHOICE__"
GATE_COUNT=16
COMPLETE_SCIENCE_MAX_BYTES=75000
RUNTIME=json.loads("{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"}")
PIN_SPECS=json.loads("{\"prior_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/positive_cutoff_and_reflected_coefficient_refinement_ci/run-43812987299-1/actual-scientific-conclusion.json\",\"git_blob\":\"3d6fbe7cb3c345f5fd4631428e4189823d05684a\",\"bytes\":55533,\"sha256\":\"e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d\"},\"wpc_contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-complete-positive-cutoff-in-its-actual-output-window.md\",\"git_blob\":\"92f5e51af2af959794b527c89d03f103d9e69422\",\"bytes\":16086,\"sha256\":\"2bc45c4c67261986bf2e94bb889d20757be8c713c31542c6a08e1da4353f8468\"},\"pcra_proof\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-actual-positive-cutoff-and-reflected-coefficient-bounds.md\",\"git_blob\":\"8e0ed75a0fc4f80272d90e20711983c91cff86f2\",\"bytes\":12537,\"sha256\":\"f2b1e603654a3823bfc0e20664f191d06db739afa1dfdbe9b77426227b55f8ea\"},\"wsp_contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-asymmetric-Schur-Parseval-bound-for-the-positive-cutoff.md\",\"git_blob\":\"63172c82614744904305ff0c7c798569244e5419\",\"bytes\":10001,\"sha256\":\"80d2820758dd4f71cf170da237ce45ce14788a3d5f74c7a4e74820c4c297f3a7\"},\"wcf_contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-exact-finite-coefficient-factors-and-remaining-graph-error.md\",\"git_blob\":\"86090c70f18298a204137f21da7715bdcf19ab18\",\"bytes\":23257,\"sha256\":\"452ee9e41e27a1a2000ea2746e09decc6c936b37a5759a1ace656b500bbfb9dd\"}}")
RULES=json.loads("{\"bytes\":2461,\"git_blob\":\"5c5d020913d717bb5bc8ce891297e00eaa8944f7\",\"path\":\"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json\",\"sha256\":\"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1\"}")
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"physical_period\":\"pi/2\",\"physical_frequency\":\"n=4|j|\",\"normalized_angular_measure\":true,\"natural_input_cutoff_abs_j\":97,\"Schur_split_integer\":128,\"Schur_input_window\":\"H^(-4/3)\",\"Schur_source_window\":\"H^(-2/3)\",\"coefficient_split_input\":\"selected Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"coefficient_split_output\":\"P Fix(Ra) intersect L2\",\"prior_success\":\"43812987299/1\",\"new_primary_targets\":\"same complete positive correction and exact infinite coefficient remainder\",\"new_complete_graphs\":4,\"new_printed_scalar_record_slots\":49,\"new_computed_scalar_records\":45,\"old_scientific_calls_allowed\":0,\"old_exponentials_or_logarithms_reevaluated\":0,\"new_native_arrays_or_artifacts_allowed\":false}")
RETAINED_SCOPE=json.loads("{\"full_prior_parameters_and_scopes_retained\":true,\"same_positive_family_cutoff_and_receiver\":true,\"same_selected_reflected_coefficient_source\":true,\"varying_rows_and_fixed_columns_distinct\":true,\"both_signs_and_full_output_mean_retained\":true,\"D_infinity_is_not_complete_Dalg\":true,\"physical_rhoi_and_complete_ell2_retained\":true,\"FJ_and_both_primitive_ranks_retained\":true,\"root_sources_jumps_endpoints_and_matching_separate\":true,\"same_density_maps_and_normalizer_order\":true,\"positive_comparison_only_same_operator\":true,\"finite_border_inverse_claimed\":false,\"physical_incoming_inverse_claimed\":false,\"high_cutoff_or_background_claimed\":false,\"independent_physical_means\":2}")
PUBLICATION_LIMITS=json.loads("{\"complete_preGit_max_bytes\":90000,\"complete_science_max_bytes\":75000,\"execution_max_bytes\":59000,\"publication_reserve_bytes\":150000,\"report_max_bytes\":8000}")
COMPLETE_FIELDS=json.loads("[\"kind\",\"public_repository\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"run_id\",\"run_attempt\",\"source_sha256\",\"input_manifest_sha256\",\"input_sha256\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"verified_original_inputs\",\"accepted_prior_input\",\"complete_prior_scientific_conclusion_read_verbatim\",\"prior_scientific_conclusion_sha256\",\"complete_new_split_coefficients\",\"complete_new_three_amplitude_functionals\",\"complete_new_positive_correction\",\"complete_new_coefficient_split\",\"complete_operator_identity_conclusion\",\"gates\",\"complete\",\"proved\",\"stage\",\"actual_returncode\",\"failure\",\"actual_mathematical_wall_seconds\"]")
GATE_NAMES=json.loads("[\"actual public runtime and directed arithmetic\",\"eight current pinned texts and no restored inputs\",\"four contracts and five full mathematical identities\",\"prior complete thirty-eight-field twenty-two-gate success retained\",\"all prior graphs records qualifications scopes and receipts retained\",\"twenty-one saved upper records at exact paths\",\"four complete split coefficients and all lag modes\",\"complete varying-symbol rows use pointwise bounds\",\"complete fixed-input columns use Parseval\",\"three complete Schur functionals include pullback\",\"complete physical pair cutoff and positive reception\",\"saved-first whole choice uses final record endpoints\",\"exact infinite coefficient remainder and all finite rows\",\"all old inputs frozen and old mathematical calls zero\",\"four complete graphs and operation counts agree\",\"complete thirty-one fields sixteen gates and physical limits\"]")
PLANNED_SHAPE=json.loads("{\"current_small_text_inputs\":8,\"mathematical_small_text_inputs\":5,\"immutable_AST_files\":2,\"historical_or_native_inputs\":0,\"prior_complete_successes\":1,\"prior_complete_graphs_preserved\":7,\"prior_complete_fields_preserved\":38,\"prior_bound_records_preserved\":42,\"prior_qualification_records_preserved\":3,\"prior_scope_collections_preserved\":5,\"new_complete_graphs\":4,\"new_printed_scalar_record_slots\":49,\"new_computed_scalar_records\":45,\"new_rational_power_calls\":5,\"new_square_root_calls\":6,\"new_whole_positive_choices\":1,\"coefficient_split_compared_with_old_Dalg\":false}")
INITIAL_ACTUAL_PROGRESS=json.loads("{\"accepted_prior_successes\":0,\"copied_complete_prior_scientific_objects\":0,\"copied_prior_complete_graphs\":0,\"old_original_bound_records_retained\":0,\"old_original_qualification_records_retained\":0,\"old_original_scope_collections_retained\":0,\"new_split_coefficient_graphs\":0,\"new_amplitude_functionals\":0,\"new_positive_candidate_graphs\":0,\"new_whole_positive_choices\":0,\"new_coefficient_split_graphs\":0,\"new_record_evaluations\":0,\"new_rational_power_calls\":0,\"new_square_root_calls\":0,\"old_scientific_targets_recomputed\":0,\"old_scientific_producers_imported_or_called\":0,\"old_exponentials_or_logarithms_evaluated\":0,\"historical_or_native_inputs_restored\":0}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_prior_successes\":1,\"copied_complete_prior_scientific_objects\":1,\"copied_prior_complete_graphs\":7,\"old_original_bound_records_retained\":42,\"old_original_qualification_records_retained\":3,\"old_original_scope_collections_retained\":5,\"new_split_coefficient_graphs\":1,\"new_amplitude_functionals\":3,\"new_positive_candidate_graphs\":1,\"new_whole_positive_choices\":1,\"new_coefficient_split_graphs\":1,\"new_record_evaluations\":45,\"new_rational_power_calls\":5,\"new_square_root_calls\":6,\"old_scientific_targets_recomputed\":0,\"old_scientific_producers_imported_or_called\":0,\"old_exponentials_or_logarithms_evaluated\":0,\"historical_or_native_inputs_restored\":0}")
OPERATOR_IDENTITY=json.loads("{\"positive_received_order\":\"Kpos*(Cvol+Kchi*sqrt(C1^2+Fw^2)+CFH)\",\"coefficient_remainder\":\"D_infinity=Qa Vw Ti-Qa A_J S Mc I A_F TF_inverse S_inverse\",\"coefficient_finite_terms\":\"U_F V_F+U_S V_S-(h-1)rho_i+(h-1)ell2\",\"only_same_positive_operator_has_whole_candidate_comparison\":true,\"no_inverse_or_finite_border_gate_claimed\":true}")
EXPECTED_ACCEPTED_PRIOR=json.loads("{\"file_git_blob\":\"3d6fbe7cb3c345f5fd4631428e4189823d05684a\",\"file_bytes\":55533,\"file_sha256\":\"e2cb2aacc031532e3b4db92873b404e9550599da75427dbb3c6448b65120d88d\",\"prior_field_count\":38,\"prior_gate_count\":22,\"prior_graph_count\":7,\"full_prior_embedded_verbatim\":true,\"inherited_five_receipts_retained\":true,\"original_42_bounds_retained\":true,\"original_3_qualifications_and_5_scopes_retained\":true,\"no_old_producer_called\":true,\"prior_identity_sha256\":\"ead8379de584ff757ea68988fa3b0d30de23ac73c70c10cfb854c257d5bbe503\"}")
PRIOR_IDENTITY=json.loads("{\"kind\":\"complete_positive_cutoff_and_reflected_coefficient_refinement_v1\",\"run_id\":\"43812987299\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"feebf07a4514fb317a3360f5ff057dc3362b0ad9\",\"actual_scientific_checkout_commit\":\"feebf07a4514fb317a3360f5ff057dc3362b0ad9\",\"source_sha256\":\"1dfbb387e58ec15f4add9c717ba8b4874682952acd25da9377e18b50684417c9\",\"input_manifest_sha256\":\"11389e0b5148a1e35f48d6b561e817095f7185d111dbf620ddfde397bc9b7ed2\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"failure\":null,\"stage\":\"complete\"}")
PRIOR_FIELD_NAMES=json.loads("[\"accepted_old_inputs\",\"actual_mathematical_wall_seconds\",\"actual_progress\",\"actual_returncode\",\"actual_scientific_checkout_commit\",\"arithmetic_bits\",\"complete\",\"complete_operator_identity_conclusion\",\"complete_wce_algebraic_conclusion\",\"complete_wce_projected_rank_conclusion\",\"complete_wce_root_coefficient_conclusion\",\"complete_wce_waist_conclusion\",\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_wpc_geometry_and_moment_conclusion\",\"complete_wpc_positive_correction_conclusion\",\"copied_complete_original_scopes\",\"copied_complete_original_scopes_sha256\",\"copied_original_qualification_records\",\"copied_original_qualification_records_sha256\",\"copied_original_scalar_records\",\"copied_original_scalar_records_sha256\",\"failure\",\"gates\",\"input_manifest_sha256\",\"input_sha256\",\"kind\",\"parameters\",\"planned_shape\",\"proved\",\"public_repository\",\"retained_scope\",\"run_attempt\",\"run_id\",\"runtime\",\"source_sha256\",\"stage\",\"verified_original_inputs\",\"workflow_event_commit\"]")
PRIOR_GATE_NAMES=json.loads("[\"public pinned runtime and directed scalar arithmetic in the actual checkout\",\"ten current small texts and no historical or native inputs\",\"two published contracts and seven immutable mathematical identities\",\"complete original PC thirty-gate positive correction success\",\"complete original TF fourteen-gate common-root normalizer success\",\"complete original WX twenty-gate selected full-density coordinate success\",\"complete original WT twenty-gate waist coefficient success with all fixed test results retained\",\"complete original SEI twenty-gate individual coefficient success\",\"same complete PC positive trial cutoff output window means and matrix-strip qualification\",\"same selected WCE root finite primitive and true waist identities\",\"all forty-two original bound records and three qualifications copied verbatim\",\"new shifted moments and actual-output-window geometry are complete\",\"new full-strip Cauchy lists and three weighted Schur functionals are complete\",\"new full two-row cutoff and same received positive candidate are complete\",\"new same-root coefficient factors retain already-paid right-normalizer costs\",\"new full and projected primitive ranks retain their exact mean rows\",\"new exact-waist second-order factors retain the saved forward remainder\",\"new complete algebraic candidates use the same reflected input and full target\",\"whole candidate choices use final saved upper endpoints and retain all candidates\",\"all original input bytes records scopes and receipts remain unchanged\",\"all seven new graphs and actual progress match the complete planned shape\",\"the complete thirty-eight-field conclusion retains all physical limits and twenty-two gates\"]")
PRIOR_PARAMETERS=json.loads("{\"WCE_input_space\":\"Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"WCE_only_at_original_selected_parameter\":true,\"WCE_output_space\":\"P Fix(Ra) intersect L2\",\"WPC_input_window\":\"H^(-4/3)\",\"WPC_received_output\":\"same old-circle primitive-density L2 pair plus both means\",\"WPC_source_window\":\"ordinary L2_dr (H^(-2/3) pair)\",\"actual_common_root_cutoff_abs_j\":1024,\"actual_moving_waist_cutoff_abs_j\":268435456,\"arithmetic_bits\":320,\"exact_PC_cutoff_derivative_upper\":\"1875000\",\"exact_PC_full_amplitude_strip\":\"1/256\",\"exact_PC_matrix_lag_strip\":\"1/64\",\"exact_PC_positive_transition\":[\"1/500000\",\"3/1000000\"],\"exact_PC_saved_contour_shift\":\"1/512\",\"exact_PC_transition_length\":\"1/1000000\",\"exact_complete_matrix_weight_upper\":\"(64/63)*16^(2/3)\",\"exact_density_deviation_upper\":\"1/31\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_new_profile_moment_upper_rule\":\"(3p/8)^(2p/3)\",\"exact_profile_moment_shift\":\"5/2\",\"exact_real_delta_radius\":\"1/100000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_terminal_T\":\"1/2000\",\"expected_Python_AST_files\":2,\"expected_actual_gate_count\":22,\"expected_current_inputs\":10,\"expected_historical_inputs\":0,\"expected_total_inputs\":10,\"fixed_intrinsic_parameter\":\"eta_0\",\"full_complex_parameter_square_claimed\":false,\"full_physical_incoming_or_finite_Schur_inverse_claimed\":false,\"independent_physical_mean_coordinates\":2,\"minimum_physical_frequency\":388,\"natural_input_cutoff_abs_j\":97,\"new_complete_mathematical_graphs\":7,\"new_whole_candidate_choices\":2,\"normalized_angular_measure\":true,\"old_exponentials_or_logarithms_reevaluated\":0,\"old_profiles_integrals_exponential_sums_or_matrix_words_reevaluated\":0,\"old_scientific_source_imports_allowed\":0,\"old_successful_scientific_calls_allowed\":0,\"original_actual_runs\":{\"PC\":\"43740173506/1\",\"SEI\":\"43773319871/1\",\"TF\":\"43766881076/1\",\"WT\":\"43763134339/1\",\"WX\":\"43763424840/1\"},\"physical_frequency\":\"n=4|j|\",\"physical_period\":\"pi/2\",\"physical_root_piece\":2549,\"saved_actual_receipts\":5,\"saved_bound_records\":42,\"saved_original_scope_collections\":5,\"saved_qualification_records\":3,\"shifted_profile_moments\":[\"11/4\",\"13/4\",\"15/4\",\"17/4\",\"19/4\",\"23/4\",\"25/4\"]}")
PRIOR_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":5,\"copied_original_bound_records\":42,\"copied_original_qualification_records\":3,\"copied_original_scope_collections\":5,\"historical_or_native_inputs_restored\":0,\"new_wce_complete_candidate_graphs\":1,\"new_wce_rank_graphs\":1,\"new_wce_root_graphs\":1,\"new_wce_waist_graphs\":1,\"new_whole_candidate_choices\":2,\"new_wpc_cauchy_and_schur_graphs\":1,\"new_wpc_complete_positive_candidates\":1,\"new_wpc_geometry_and_moment_graphs\":1,\"old_completed_scalar_products_recomputed\":0,\"old_exponentials_or_logarithms_evaluated\":0,\"old_profiles_exponential_sums_or_integrals_recomputed\":0,\"old_scientific_producers_imported_or_called\":0,\"old_scientific_targets_recomputed\":0}")
PRIOR_RETAINED_SCOPE=json.loads("{\"WCE_SEI_H2_is_Bessel_upper_not_unsaved_Wiener_record\":true,\"WCE_actual_input_is_fixed_phase_transported_reflection_not_full_signed_circle\":true,\"WCE_actual_two_I_waist_factor_and_physical_density_mean_rank_retained\":true,\"WCE_complete_two_primitive_ranks_written_before_restriction\":true,\"WCE_exact_waist_first_symbol_zero_does_not_set_second_symbol_zero\":true,\"WCE_full_density_S_preserves_integral_and_actual_input_has_zero_auxiliary_mean\":true,\"WCE_full_root_finite_dual_rows_and_TF_after_right_order_retained\":true,\"WCE_no_extra_TF_inverse_or_Ni_factor\":true,\"WCE_only_original_selected_real_member_and_fixed_intrinsic_reference\":true,\"WCE_only_projected_Ecoeff_equals_projected_E0\":true,\"WCE_saved_CI_B_product_read_verbatim\":true,\"WPC_Kpos_already_includes_positive_seven_port_and_factor9\":true,\"WPC_actual_scalar_X_pullback_not_full_density\":true,\"WPC_complete_angular_matrix_words_paid_before_weighting\":true,\"WPC_complete_both_signed_carriers_and_all_output_modes\":true,\"WPC_genuine_terminal_column_and_nonzero_root_beta_retained\":true,\"WPC_old_volume_finite_head_source_and_received_gain_read_only\":true,\"WPC_only_specific_two_thirds_weight_uses_C2_Schur\":true,\"WPC_root_finite_received_term_retained_separately_not_added_to_new_positive\":true,\"WPC_same_original_PC_positive_trial_cutoff_and_complete_real_family\":true,\"WPC_saved_wide_P_H_moduli_supply_new_finite_Cauchy_derivatives\":true,\"WPC_target_is_full_positive_pair_Hminus2_3_not_negative_special_source\":true,\"actual_finite_border_inverse_claimed\":false,\"all_old_complete_receipts_parameters_and_scopes_frozen\":true,\"all_original_targets_profiles_and_source_integrals_not_recomputed\":true,\"complete_physical_incoming_inverse_claimed\":false,\"complete_return_R0_or_nonlinear_background_claimed\":false,\"historical_native_or_archive_inputs_restored\":false,\"independent_physical_means\":2,\"negative_source_positive_volume_endpoint_and_true_mean_matching_not_removed\":true,\"physical_paired_row_source_target_not_replaced_by_Ti_endomorphism\":true,\"scientific_target\":\"same positive correction and same complete reflected coefficient error\",\"true_radial_head_actual_root_border_and_independent_second_input_retained\":true,\"two_new_targets_are_distinct_and_not_summed_as_an_operator_inverse\":true,\"whole_candidates_preserve_same_complete_operator_and_final_record_endpoints\":true}")
PRIOR_OPERATOR_IDENTITY=json.loads("{\"coefficient_complete_row\":\"D_alg=Qa Vw Ti-(h-1)rho_i+Qa A_J P_h(R_S+S R_F S_inverse)\",\"coefficient_projected_identity\":\"P_h E_coeff = P_h(R_S+S R_F S_inverse)\",\"coefficient_rank_exact\":\"R_S=ci tensor ppsi-(ci*ppsi) tensor 1\",\"coefficient_root_exact\":\"(Id+MC I) TF_inverse = Id+Mc I+(F_J-Mc I A_F) TF_inverse\",\"coefficient_source\":\"Xfr_Hminus4_3 = S Dplus Hnat_Hminus4_3\",\"coefficient_target\":\"P Fix(Ra) intersect L2\",\"full_physical_mean_rank_retained\":true,\"only_new_scalar_enclosures_not_new_inverse_or_actual_background\":true,\"positive_complete_reconstruction\":\"h1=P T(hamp)+J(P T(gamp)-L P T(hamp)-B P T(w)); h2=P T(w)\",\"positive_received_order\":\"Kpos*(saved_Cvol+new_Ccut+saved_CFH)\",\"positive_source\":\"original chi_prime times complete genuine raw pair hG\",\"positive_whole_choice\":\"same Rplus in the complete WUE tuple\",\"root_finite_output\":\"saved complete received RF remains separate; its actual trace border is not evaluated\",\"same_selected_parameter_only_for_coefficient\":true}")
PRIOR_SCALAR_PATHS=json.loads("{\"CX\":[\"complete_wpc_geometry_and_moment_conclusion\",\"geometry\",\"scalar_pullback_Hminus2_3_upper\"],\"Kchi\":[\"complete_wpc_geometry_and_moment_conclusion\",\"geometry\",\"physical_cutoff_radial_factor_upper\"],\"J\":[\"complete_wpc_positive_correction_conclusion\",\"complete_ordered_J_word_upper\"],\"JL\":[\"complete_wpc_positive_correction_conclusion\",\"complete_ordered_JL_word_upper\"],\"JB\":[\"complete_wpc_positive_correction_conclusion\",\"complete_ordered_JB_word_upper\"],\"Cvol\":[\"copied_original_scalar_records\",\"WPC\",\"Cvol\"],\"CFH\":[\"copied_original_scalar_records\",\"WPC\",\"CFH\"],\"Kpos\":[\"copied_original_scalar_records\",\"WPC\",\"Kpos\"],\"prior_positive\":[\"complete_wpc_positive_correction_conclusion\",\"whole_received_positive_choice\",\"complete_selected_upper\"],\"CwI\":[\"complete_wce_waist_conclusion\",\"complete_physical_two_primitive_row_upper\"],\"KA0\":[\"complete_wce_waist_conclusion\",\"complete_waist_forward_L2_upper\"],\"C2root\":[\"complete_wce_root_coefficient_conclusion\",\"complete_root_two_primitive_fee_upper\"],\"KS0\":[\"copied_original_scalar_records\",\"WCE\",\"S_L2\"],\"KSinv\":[\"copied_original_scalar_records\",\"WCE\",\"S_inverse_Hminus4_3\"],\"rhoi\":[\"copied_original_scalar_records\",\"WCE\",\"mean_row_CI_B\"],\"w_D0\":[\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_three_amplitude_functionals\",\"w\",\"complete_weighted_phase_derivative_upper\",0],\"w_D2\":[\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_three_amplitude_functionals\",\"w\",\"complete_inverse_angle_second_derivative_upper\"],\"h_D0\":[\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_three_amplitude_functionals\",\"h\",\"complete_weighted_phase_derivative_upper\",0],\"h_D2\":[\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_three_amplitude_functionals\",\"h\",\"complete_inverse_angle_second_derivative_upper\"],\"g_D0\":[\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_three_amplitude_functionals\",\"g\",\"complete_weighted_phase_derivative_upper\",0],\"g_D2\":[\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_three_amplitude_functionals\",\"g\",\"complete_inverse_angle_second_derivative_upper\"]}")
NEW_GRAPH_SHAPES=json.loads("{\"complete_new_split_coefficients\":{\"row_head_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_head_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_coefficient_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"split_integer\":128,\"split_is_not_an_operator_cutoff\":true,\"zero_output_and_both_lag_signs_retained\":true},\"complete_new_three_amplitude_functionals\":{\"amplitudes\":{\"w\":{\"row_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_column_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_column_product_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Schur_matrix_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_functional_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"h\":{\"row_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_column_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_column_product_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Schur_matrix_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_functional_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"g\":{\"row_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"row_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_head_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"column_tail_contribution_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_column_sum_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_row_column_product_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_Schur_matrix_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_functional_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"}},\"varying_symbol_rows_use_pointwise_bounds_only\":true,\"fixed_input_columns_use_complete_Parseval\":true,\"full_both_signed_input_and_all_output_modes_including_mean\":true,\"original_scalar_pullback_paid_once\":true},\"complete_new_positive_correction\":{\"complete_first_row_terms_upper\":{\"h\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"g\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"w\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"complete_first_row_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_second_row_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_physical_pair_squared_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_physical_pair_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_cutoff_source_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_positive_source_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_received_positive_candidate_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"whole_received_positive_candidates\":{\"saved_complete_positive\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"new_asymmetric_Schur_Parseval\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\"},\"whole_received_positive_choice\":{\"selected_label\":\"__WHOLE_POSITIVE_CHOICE__\",\"complete_selected_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"all_candidates_retained\":true},\"same_original_positive_operator\":true,\"original_volume_finite_head_and_receiver_read_only\":true,\"physical_pair_and_two_means_retained\":true,\"genuine_root_shear_and_terminal_column_retained\":true,\"root_finite_received_term_separate_and_unchanged\":true},\"complete_new_coefficient_split\":{\"complete_ell2_dual_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_conjugated_two_primitive_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_left_waist_two_primitive_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_D_infinity_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"complete_combined_density_row_positive_upper\":\"__FINITE_NONNEGATIVE_SCALAR_RECORD__\",\"exact_operator\":\"D_infinity=Qa Vw Ti-Qa A_J S Mc I A_F TF_inverse S_inverse\",\"complete_Dalg_not_claimed_by_this_bound\":true,\"original_minus_h_minus_one_rhoi_and_new_plus_h_minus_one_ell2_retained\":true,\"complete_FJ_primitive_ranks_and_ordered_dual_rows_retained\":true,\"finite_factor_is_not_a_physical_input_completion\":true,\"no_comparison_or_subtraction_from_old_Calg\":true,\"selected_real_member_and_actual_reflected_source_only\":true}}")
NEW_GRAPH_SLOT_COUNTS=json.loads("{\"complete_new_split_coefficients\":4,\"complete_new_three_amplitude_functionals\":27,\"complete_new_positive_correction\":13,\"complete_new_coefficient_split\":5}")
ALLOWED_WHOLE_LABELS=json.loads("[\"saved_complete_positive\",\"new_asymmetric_Schur_Parseval\"]")
PRIOR_FROZEN_HASHES=json.loads("{\"copied_complete_original_scopes_sha256\":\"2e21ee2bf8bc0db069ea9a0390f326fa32a6cbc6d324bfcf6af86f099610ba20\",\"copied_original_qualification_records_sha256\":\"e6d95b77b886921337ba37201e2fd0da67c26c02233672e794479b3019bd669e\",\"copied_original_scalar_records_sha256\":\"1966c937ea41995ab4ee65cd870c997dfd0e201ad9afaf817f149eafa3e17c6a\"}")
PRIOR_GRAPH_NAMES=json.loads("[\"complete_wpc_geometry_and_moment_conclusion\",\"complete_wpc_cauchy_and_schur_conclusion\",\"complete_wpc_positive_correction_conclusion\",\"complete_wce_root_coefficient_conclusion\",\"complete_wce_projected_rank_conclusion\",\"complete_wce_waist_conclusion\",\"complete_wce_algebraic_conclusion\"]")
FROZEN_ACCEPTED_PRIOR_SHA256="c66145eafe7825b66a7bd857362f72c1fd70d2584386523db5d94024923bb096"
FROZEN_PRIOR_SCALAR_PATHS_SHA256="900cb0bf1a95a05beb212efac19326051b67d4f8450e22b83d12bf27ba120639"

def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def reject_nonfinite(token):
    raise ValueError("nonfinite JSON token: " + token)


def operation_excerpt(text, limit, keep_tail=False):
    """Bound only diagnostic text by its serialized JSON payload bytes."""
    lo, hi = 0, len(text)
    while lo < hi:
        count = (lo + hi + 1) // 2
        part = text[-count:] if keep_tail else text[:count]
        size = len(json.dumps(part, ensure_ascii=False).encode("utf-8")) - 2
        if size <= limit:
            lo = count
        else:
            hi = count - 1
    part = (text[-lo:] if keep_tail else text[:lo]) if lo else ""
    return part, lo != len(text)


def operation_failure(error):
    """Print complete diagnostics; cap only the published diagnostic strings."""
    original = {"type": type(error).__name__, "message": str(error),
                "traceback": traceback.format_exc()}
    print("BEGIN_UNABRIDGED_OPERATION_DIAGNOSTIC", flush=True)
    for key in ("type", "message", "traceback"):
        print(key + ": " + original[key], flush=True)
    print("END_UNABRIDGED_OPERATION_DIAGNOSTIC", flush=True)
    result, shortened = {}, False
    for key, limit, tail in (
            ("type", 64, False), ("message", 256, False),
            ("traceback", 2048, True)):
        result[key], truncated = operation_excerpt(original[key], limit, tail)
        shortened = shortened or truncated
    result["text_truncated"] = shortened
    result["full_text_in_job_log"] = True
    return result


def get_path(value, path):
    for key in path:
        value = value[key]
    return value


def gate(doc, index, condition):
    require(len(doc["gates"]) == index, "gate order changed")
    passed = bool(condition)
    doc["gates"].append({"name": GATE_NAMES[index], "passed": passed})
    require(passed, "gate failed: " + GATE_NAMES[index])


def persist(path, doc):
    raw = canonical(doc)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".atomic")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    return raw


def print_complete_document(doc):
    print("BEGIN_COMPLETE_POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_SCIENCE_JSON", flush=True)
    print(canonical(doc).decode("utf-8"), end="", flush=True)
    print("END_COMPLETE_POSITIVE_CUTOFF_SCHUR_PARSEVAL_AND_COEFFICIENT_SPLIT_SCIENCE_JSON", flush=True)


def complete_graph_shape(value, shape):
    if shape == SCALAR_SENTINEL:
        return (isinstance(value, dict) and set(value) == {"ball"}
                and isinstance(value["ball"], str)
                and arb(value["ball"]).is_finite()
                and arb(value["ball"]).lower() >= 0)
    if shape == LABEL_SENTINEL:
        return value in ALLOWED_WHOLE_LABELS
    if isinstance(shape, bool):
        return value is shape
    if isinstance(shape, int):
        return type(value) is int and value == shape
    if isinstance(shape, str):
        return isinstance(value, str) and value == shape
    if isinstance(shape, list):
        return (isinstance(value, list) and len(value) == len(shape)
                and all(complete_graph_shape(v, s) for v, s in zip(value, shape)))
    if isinstance(shape, dict):
        return (isinstance(value, dict) and set(value) == set(shape)
                and all(complete_graph_shape(value[k], s)
                        for k, s in shape.items()))
    return False


def scalar_slot_count(value, shape):
    if shape == SCALAR_SENTINEL:
        return 1
    if isinstance(shape, list):
        return sum(scalar_slot_count(v, s) for v, s in zip(value, shape))
    if isinstance(shape, dict):
        return sum(scalar_slot_count(value[k], s) for k, s in shape.items())
    return 0


def whole_choice_is_retained(choice, candidates):
    if set(choice) != {"selected_label", "complete_selected_upper",
                       "all_candidates_retained"}:
        return False
    label = choice["selected_label"]
    if label not in candidates or choice["all_candidates_retained"] is not True:
        return False
    if choice["complete_selected_upper"] != candidates[label]:
        return False
    selected = retained_up(choice["complete_selected_upper"])
    if any(selected > retained_up(v) for v in candidates.values()):
        return False
    # Validation of the already-saved choice: exact ties retain the first.
    for candidate, record in candidates.items():
        if retained_up(record) == selected:
            return candidate == label
    return False


# WSP/WCF mathematical helpers. Static source only; no entry point.
# The final public consumer supplies arb, copy, and the actual progress dict.

def ex(value):
    return arb(str(value))


def up(value):
    value = arb(value)
    if not value.is_finite():
        raise ArithmeticError("nonfinite directed scalar")
    endpoint = value.upper()
    if not endpoint.is_finite() or endpoint < 0:
        raise ArithmeticError("nonnegative upper endpoint required")
    return endpoint


def retained_up(record):
    if not isinstance(record, dict) or not isinstance(record.get("ball"), str):
        raise TypeError("complete saved scalar record required")
    return up(arb(record["ball"]))


def rec(value, progress):
    record = {"ball": up(value).str(75)}
    if not arb(record["ball"]).is_finite():
        raise ArithmeticError("nonfinite saved scalar record")
    progress["new_record_evaluations"] += 1
    return record


def new_power(base, exponent, progress):
    base = arb(base)
    if not base.is_finite() or not base.lower() > 0:
        raise ArithmeticError("positive rational-power base required")
    result = up(base ** exponent)
    progress["new_rational_power_calls"] += 1
    return result


def new_sqrt(value, progress):
    value = arb(value)
    if not value.is_finite() or value.lower() < 0:
        raise ArithmeticError("nonnegative square-root input required")
    result = up(value.sqrt())
    progress["new_square_root_calls"] += 1
    return result


def whole_choice(candidates):
    best_label = None
    best_upper = None
    for label, record in candidates.items():
        endpoint = retained_up(record)
        if best_label is None or endpoint < best_upper:
            best_label, best_upper = label, endpoint
    if best_label is None:
        raise ValueError("empty complete-candidate collection")
    return {"selected_label": best_label,
            "complete_selected_upper": copy.deepcopy(candidates[best_label]),
            "all_candidates_retained": True}


def wsp_split_coefficients(progress):
    L = ex(128)
    five_two_thirds = new_power(ex(5), ex(2) / ex(3), progress)
    # Squaring this positive upper gives a full upper for 5^(4/3).
    five_four_thirds = up(five_two_thirds * five_two_thirds)
    head_five_thirds = new_power(L + ex(1), ex(5) / ex(3), progress)
    tail_minus_one_third = new_power(L, -ex(1) / ex(3), progress)
    head_seven_thirds = new_power(L + ex(1), ex(7) / ex(3), progress)
    tail_minus_five_sixths = new_power(L, -ex(5) / ex(6), progress)
    if not head_five_thirds.lower() > 1 or not head_seven_thirds.lower() > 1:
        raise ArithmeticError("positive complete head differences required")

    row_head = rec(ex(1) + (ex(6) / ex(5)) * five_two_thirds
                   * (head_five_thirds - ex(1)), progress)
    row_tail = rec((ex(3) / ex(8)) * five_two_thirds
                   * tail_minus_one_third, progress)
    column_head = rec(new_sqrt(
        ex(1) + (ex(6) / ex(7)) * five_four_thirds
        * (head_seven_thirds - ex(1)), progress), progress)
    column_tail = rec((five_two_thirds / ex(16))
                      * new_sqrt(ex(6) / ex(5), progress)
                      * tail_minus_five_sixths, progress)
    return {
        "row_head_coefficient_upper": row_head,
        "row_tail_coefficient_upper": row_tail,
        "column_head_coefficient_upper": column_head,
        "column_tail_coefficient_upper": column_tail,
        "split_integer": 128,
        "split_is_not_an_operator_cutoff": True,
        "zero_output_and_both_lag_signs_retained": True,
    }


def wsp_one_amplitude(D0_record, D2_record, CX_record, split, progress):
    D0, D2, CX = (retained_up(D0_record), retained_up(D2_record),
                  retained_up(CX_record))
    row_head = rec(retained_up(split["row_head_coefficient_upper"]) * D0,
                   progress)
    row_tail = rec(retained_up(split["row_tail_coefficient_upper"]) * D2,
                   progress)
    row = rec(retained_up(row_head) + retained_up(row_tail), progress)
    column_head = rec(retained_up(split["column_head_coefficient_upper"]) * D0,
                      progress)
    column_tail = rec(retained_up(split["column_tail_coefficient_upper"]) * D2,
                      progress)
    column = rec(retained_up(column_head) + retained_up(column_tail), progress)
    product = rec(retained_up(row) * retained_up(column), progress)
    schur = rec(new_sqrt(retained_up(product), progress), progress)
    functional = rec(CX * retained_up(schur), progress)
    return {
        "row_head_contribution_upper": row_head,
        "row_tail_contribution_upper": row_tail,
        "complete_row_sum_upper": row,
        "column_head_contribution_upper": column_head,
        "column_tail_contribution_upper": column_tail,
        "complete_column_sum_upper": column,
        "complete_row_column_product_upper": product,
        "complete_Schur_matrix_upper": schur,
        "complete_functional_upper": functional,
    }


def wsp_complete_positive(saved, functionals, progress):
    amplitudes = functionals["amplitudes"]
    Fw_record = amplitudes["w"]["complete_functional_upper"]
    Fw, Fh, Fg = (retained_up(Fw_record),
                  retained_up(amplitudes["h"]["complete_functional_upper"]),
                  retained_up(amplitudes["g"]["complete_functional_upper"]))
    J, JL, JB = (retained_up(saved["J"]), retained_up(saved["JL"]),
                  retained_up(saved["JB"]))
    terms = {
        "h": rec((ex(1) + JL) * Fh, progress),
        "g": rec(J * Fg, progress),
        "w": rec(JB * Fw, progress),
    }
    first = rec(sum((retained_up(value) for value in terms.values()), ex(0)),
                progress)
    # This is the same already-saved complete functional, not a new evaluation.
    second = copy.deepcopy(Fw_record)
    first_upper, second_upper = retained_up(first), retained_up(second)
    squared = rec(first_upper * first_upper + second_upper * second_upper,
                  progress)
    pair = rec(new_sqrt(retained_up(squared), progress), progress)
    cutoff = rec(retained_up(saved["Kchi"]) * retained_up(pair), progress)
    source = rec(retained_up(saved["Cvol"]) + retained_up(cutoff)
                 + retained_up(saved["CFH"]), progress)
    received = rec(retained_up(saved["Kpos"]) * retained_up(source), progress)
    # Insertion order implements the specified old-candidate tie rule.
    candidates = {
        "saved_complete_positive": copy.deepcopy(saved["prior_positive"]),
        "new_asymmetric_Schur_Parseval": copy.deepcopy(received),
    }
    choice = whole_choice(candidates)
    progress["new_whole_positive_choices"] += 1
    return {
        "complete_first_row_terms_upper": terms,
        "complete_first_row_upper": first,
        "complete_second_row_upper": second,
        "complete_physical_pair_squared_upper": squared,
        "complete_physical_pair_upper": pair,
        "complete_cutoff_source_upper": cutoff,
        "complete_positive_source_upper": source,
        "complete_received_positive_candidate_upper": received,
        "whole_received_positive_candidates": candidates,
        "whole_received_positive_choice": choice,
        "same_original_positive_operator": True,
        "original_volume_finite_head_and_receiver_read_only": True,
        "physical_pair_and_two_means_retained": True,
        "genuine_root_shear_and_terminal_column_retained": True,
        "root_finite_received_term_separate_and_unchanged": True,
    }


def wcf_direct_split(saved, progress):
    # C2root already includes the complete right T_F inverse.
    ell2 = rec(retained_up(saved["C2root"]) * retained_up(saved["KSinv"]),
               progress)
    conjugated = rec(retained_up(saved["KS0"]) * retained_up(ell2), progress)
    left_waist = rec(retained_up(saved["KA0"]) * retained_up(conjugated),
                    progress)
    infinite = rec(retained_up(saved["CwI"]) + retained_up(left_waist),
                   progress)
    # Exact same output column: estimate ell2-rhoi by a positive sum only.
    combined_row = rec(retained_up(ell2) + retained_up(saved["rhoi"]), progress)
    return {
        "complete_ell2_dual_upper": ell2,
        "complete_conjugated_two_primitive_upper": conjugated,
        "complete_left_waist_two_primitive_upper": left_waist,
        "complete_D_infinity_upper": infinite,
        "complete_combined_density_row_positive_upper": combined_row,
        "exact_operator": "D_infinity=Qa Vw Ti-Qa A_J S Mc I A_F TF_inverse S_inverse",
        "complete_Dalg_not_claimed_by_this_bound": True,
        "original_minus_h_minus_one_rhoi_and_new_plus_h_minus_one_ell2_retained": True,
        "complete_FJ_primitive_ranks_and_ordered_dual_rows_retained": True,
        "finite_factor_is_not_a_physical_input_completion": True,
        "no_comparison_or_subtraction_from_old_Calg": True,
        "selected_real_member_and_actual_reflected_source_only": True,
    }

def checked_inputs(args, doc):
    runtime = {"Python": platform.python_version(),
               "python_flint": importlib.metadata.version("python-flint")}
    doc["runtime"] = runtime
    gate(doc, 0, os.environ.get("GITHUB_ACTIONS") == "true"
         and os.environ.get("GITHUB_REPOSITORY") == PUBLIC
         and runtime == RUNTIME
         and args.bits == ctx.prec == PARAMETERS["arithmetic_bits"]
         and re.fullmatch(r"[0-9a-f]{40}", doc["actual_scientific_checkout_commit"] or "") is not None
         and re.fullmatch(r"[0-9a-f]{40}", doc["workflow_event_commit"] or "") is not None
         and re.fullmatch(r"[0-9]+", doc["run_id"] or "") is not None
         and re.fullmatch(r"[0-9]+", doc["run_attempt"] or "") is not None
         and doc["input_manifest_sha256"] == args.manifest_sha)
    manifest = json.loads(args.manifest.read_bytes(), parse_constant=reject_nonfinite)
    expected_paths = {"source": SOURCE, "worker": WORKER, "rules": RULES["path"]}
    expected_paths.update({role: PIN_SPECS[role]["path"] for role in sorted(PIN_SPECS)})
    entries = manifest.get("files", [])
    by_role = {entry.get("role"): entry for entry in entries}
    gate(doc, 1, manifest.get("kind") == MANIFEST_KIND
         and manifest.get("public_repository") == PUBLIC
         and manifest.get("source_path") == SOURCE
         and manifest.get("source_sha256") == doc["source_sha256"]
         and manifest.get("parameters") == PARAMETERS
         and manifest.get("scope") == RETAINED_SCOPE
         and manifest.get("publication_limits") == PUBLICATION_LIMITS
         and manifest.get("expected_actual_gate_count") == GATE_COUNT
         and manifest.get("expected_immutable_AST_files") == 2
         and manifest.get("expected_current_input_count") == 8
         and manifest.get("expected_input_count") == 8
         and len(entries) == len(by_role) == 8
         and set(by_role) == set(expected_paths)
         and manifest.get("input_paths") == expected_paths
         and manifest.get("current_text_input_roles") == list(expected_paths)
         and manifest.get("current_input_paths") == list(expected_paths.values())
         and manifest.get("all_inputs_are_current_small_texts") is True
         and manifest.get("historical_inputs") == []
         and manifest.get("legacy_artifact_inputs") == []
         and manifest.get("old_successful_scientific_calls_allowed") is False
         and manifest.get("new_native_arrays_or_artifact_persistence_allowed") is False)
    paths = {role: args.repo / Path(path) for role, path in expected_paths.items()}
    verified = {}
    for role, path in paths.items():
        entry = by_role[role]
        data = path.read_bytes()
        require(entry["path"] == expected_paths[role], "current path changed")
        require(0 < len(data) < 100000 and path.suffix in (".py", ".json", ".md"),
                "current small-text qualification")
        data.decode("utf-8")
        require(not data.startswith(b"\x1f\x8b"), "no gzip input")
        require(len(data) == entry["bytes"] and sha(data) == entry["sha256"]
                and git_blob(data) == entry["git_blob"],
                "current complete identity mismatch: " + role)
        if role in PIN_SPECS:
            require({k: entry[k] for k in ("path", "git_blob", "bytes", "sha256")}
                    == PIN_SPECS[role], "mathematical pin changed: " + role)
            verified[role] = {"bytes": len(data), "sha256": sha(data)}
        if role == "rules":
            require(all(entry[k] == RULES[k]
                        for k in ("path", "git_blob", "bytes", "sha256")),
                    "reviewed rules identity changed")
    doc["verified_original_inputs"] = verified
    doc["input_sha256"] = {role: spec["sha256"] for role, spec in PIN_SPECS.items()}
    doc["input_sha256"]["manifest"] = doc["input_manifest_sha256"]
    proofs = {role: paths[role].read_text(encoding="utf-8")
              for role in ("wpc_contract", "pcra_proof", "wsp_contract", "wcf_contract")}
    required_tags = {
        "wpc_contract": (r"\tag{WPC.6}", r"\tag{WPC.14}", r"\tag{WPC.21}"),
        "wsp_contract": (r"\tag{WSP.5}", r"\tag{WSP.7}", r"\tag{WSP.12}"),
        "wcf_contract": (r"\tag{WCF.17}", r"\tag{WCF.18}",
                         r"\tag{WCF.23}", r"\tag{WCF.24}"),
    }
    gate(doc, 2, len(verified) == 5
         and manifest.get("complete_input_bytes") == sum(e["bytes"] for e in entries)
         and manifest.get("file_sha256") == {e["path"]: e["sha256"] for e in entries}
         and manifest.get("mathematical_input_sha256")
             == {role: spec["sha256"] for role, spec in PIN_SPECS.items()}
         and all(tag in proofs[role] for role, tags in required_tags.items()
                 for tag in tags)
         and PIN_SPECS["prior_science"]["sha256"] in proofs["pcra_proof"]
         and by_role["source"]["sha256"] == sha(Path(__file__).read_bytes()))
    return manifest, paths


def accepted_prior_input(paths, doc):
    raw = paths["prior_science"].read_bytes()
    prior = json.loads(raw, parse_constant=reject_nonfinite)
    doc["complete_prior_scientific_conclusion_read_verbatim"] = copy.deepcopy(prior)
    doc["prior_scientific_conclusion_sha256"] = sha(raw)
    gate(doc, 3, raw == canonical(prior)
         and len(raw) == PIN_SPECS["prior_science"]["bytes"]
         and sha(raw) == PIN_SPECS["prior_science"]["sha256"]
         and set(prior) == set(PRIOR_FIELD_NAMES) and len(prior) == 38
         and all(prior.get(k) == v for k, v in PRIOR_IDENTITY.items())
         and [g["name"] for g in prior["gates"]] == PRIOR_GATE_NAMES
         and len(prior["gates"]) == 22
         and all(g.get("passed") is True for g in prior["gates"])
         and all(set(g) == {"name", "passed"} for g in prior["gates"])
         and prior["parameters"] == PRIOR_PARAMETERS
         and prior["retained_scope"] == PRIOR_RETAINED_SCOPE
         and prior["actual_progress"] == PRIOR_ACTUAL_PROGRESS
         and prior["complete_operator_identity_conclusion"] == PRIOR_OPERATOR_IDENTITY)
    complete_graphs = all(isinstance(prior.get(key), dict) and prior[key]
                          for key in PRIOR_GRAPH_NAMES)
    original_hashes = {
        "copied_complete_original_scopes_sha256":
            sha(canonical(prior["copied_complete_original_scopes"])),
        "copied_original_qualification_records_sha256":
            sha(canonical(prior["copied_original_qualification_records"])),
        "copied_original_scalar_records_sha256":
            sha(canonical(prior["copied_original_scalar_records"])),
    }
    gate(doc, 4, complete_graphs and len(PRIOR_GRAPH_NAMES) == 7
         and all(prior[k] == value == PRIOR_FROZEN_HASHES[k]
                 for k, value in original_hashes.items())
         and len(prior["copied_complete_original_scopes"]) == 5
         and len(prior["copied_original_qualification_records"]) == 3
         and len(prior["copied_original_scalar_records"]["WPC"]) == 25
         and len(prior["copied_original_scalar_records"]["WCE"]) == 17
         and len(prior["accepted_old_inputs"]["original_successes"]) == 5
         and canonical(doc["complete_prior_scientific_conclusion_read_verbatim"]) == raw
         and sha(canonical(PRIOR_IDENTITY))
             == EXPECTED_ACCEPTED_PRIOR["prior_identity_sha256"])
    saved = {alias: copy.deepcopy(get_path(prior, path))
             for alias, path in PRIOR_SCALAR_PATHS.items()}
    gate(doc, 5, len(saved) == 21
         and sha(canonical(PRIOR_SCALAR_PATHS)) == FROZEN_PRIOR_SCALAR_PATHS_SHA256
         and all(isinstance(v, dict) and isinstance(v.get("ball"), str)
                 and arb(v["ball"]).is_finite() and arb(v["ball"]).lower() >= 0
                 for v in saved.values())
         and saved["prior_positive"]
             == prior["complete_wpc_positive_correction_conclusion"]
                     ["whole_received_positive_choice"]["complete_selected_upper"])
    doc["accepted_prior_input"] = copy.deepcopy(EXPECTED_ACCEPTED_PRIOR)
    require(sha(canonical(doc["accepted_prior_input"])) == FROZEN_ACCEPTED_PRIOR_SHA256,
            "accepted prior identity changed")
    doc["actual_progress"].update(
        accepted_prior_successes=1, copied_complete_prior_scientific_objects=1,
        copied_prior_complete_graphs=7, old_original_bound_records_retained=42,
        old_original_qualification_records_retained=3,
        old_original_scope_collections_retained=5)
    doc["complete_operator_identity_conclusion"] = copy.deepcopy(OPERATOR_IDENTITY)
    return saved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--bits", type=int, default=320)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError("refusing to overwrite any complete or partial scientific result")
    ctx.prec = args.bits
    doc = {key: None for key in COMPLETE_FIELDS}
    doc.update(kind=KIND, complete=False, proved=False, actual_returncode=None,
        failure=None, stage="initial_current_input_admission",
        source_sha256=sha(Path(__file__).read_bytes()),
        input_manifest_sha256=sha(args.manifest.read_bytes()), public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        runtime={}, arithmetic_bits=args.bits, parameters=copy.deepcopy(PARAMETERS),
        input_sha256={}, verified_original_inputs={}, accepted_prior_input={},
        complete_prior_scientific_conclusion_read_verbatim=None,
        prior_scientific_conclusion_sha256=None,
        retained_scope=copy.deepcopy(RETAINED_SCOPE),
        planned_shape=copy.deepcopy(PLANNED_SHAPE),
        actual_progress=copy.deepcopy(INITIAL_ACTUAL_PROGRESS), gates=[],
        actual_mathematical_wall_seconds=0)
    began = time.monotonic()
    try:
        manifest, paths = checked_inputs(args, doc)
        doc["stage"] = "complete_saved_prior_admission"
        saved = accepted_prior_input(paths, doc)
        persist(args.out, doc)

        doc["stage"] = "complete_new_split_coefficients"
        key = "complete_new_split_coefficients"
        doc[key] = wsp_split_coefficients(doc["actual_progress"])
        doc["actual_progress"]["new_split_coefficient_graphs"] = 1
        gate(doc, 6, complete_graph_shape(doc[key], NEW_GRAPH_SHAPES[key])
             and scalar_slot_count(doc[key], NEW_GRAPH_SHAPES[key]) == 4)
        persist(args.out, doc)

        key = "complete_new_three_amplitude_functionals"
        doc[key] = {
            "amplitudes": {},
            "varying_symbol_rows_use_pointwise_bounds_only": True,
            "fixed_input_columns_use_complete_Parseval": True,
            "full_both_signed_input_and_all_output_modes_including_mean": True,
            "original_scalar_pullback_paid_once": True,
        }
        for amplitude in ("w", "h", "g"):
            doc["stage"] = "complete_new_amplitude_" + amplitude
            doc[key]["amplitudes"][amplitude] = wsp_one_amplitude(
                saved[amplitude + "_D0"], saved[amplitude + "_D2"], saved["CX"],
                doc["complete_new_split_coefficients"], doc["actual_progress"])
            doc["actual_progress"]["new_amplitude_functionals"] += 1
            persist(args.out, doc)
        functions = doc[key]["amplitudes"]
        gate(doc, 7, complete_graph_shape(doc[key], NEW_GRAPH_SHAPES[key])
             and scalar_slot_count(doc[key], NEW_GRAPH_SHAPES[key]) == 27
             and doc[key]["varying_symbol_rows_use_pointwise_bounds_only"] is True)
        gate(doc, 8, set(functions) == {"w", "h", "g"}
             and doc[key]["fixed_input_columns_use_complete_Parseval"] is True
             and doc[key]["full_both_signed_input_and_all_output_modes_including_mean"] is True)
        gate(doc, 9, doc[key]["original_scalar_pullback_paid_once"] is True
             and doc["actual_progress"]["new_amplitude_functionals"] == 3)
        persist(args.out, doc)

        doc["stage"] = "complete_new_positive_reception"
        key = "complete_new_positive_correction"
        doc[key] = wsp_complete_positive(saved,
            doc["complete_new_three_amplitude_functionals"], doc["actual_progress"])
        doc["actual_progress"]["new_positive_candidate_graphs"] = 1
        positive = doc[key]
        gate(doc, 10, complete_graph_shape(positive, NEW_GRAPH_SHAPES[key])
             and scalar_slot_count(positive, NEW_GRAPH_SHAPES[key]) == 13
             and positive["complete_second_row_upper"]
                 == functions["w"]["complete_functional_upper"]
             and positive["whole_received_positive_candidates"]["saved_complete_positive"]
                 == saved["prior_positive"]
             and positive["whole_received_positive_candidates"]["new_asymmetric_Schur_Parseval"]
                 == positive["complete_received_positive_candidate_upper"])
        gate(doc, 11, whole_choice_is_retained(
            positive["whole_received_positive_choice"],
            positive["whole_received_positive_candidates"])
             and list(positive["whole_received_positive_candidates"])
                 == ["saved_complete_positive", "new_asymmetric_Schur_Parseval"])
        persist(args.out, doc)

        doc["stage"] = "complete_new_coefficient_split"
        key = "complete_new_coefficient_split"
        doc[key] = wcf_direct_split(saved, doc["actual_progress"])
        doc["actual_progress"]["new_coefficient_split_graphs"] = 1
        gate(doc, 12, complete_graph_shape(doc[key], NEW_GRAPH_SHAPES[key])
             and scalar_slot_count(doc[key], NEW_GRAPH_SHAPES[key]) == 5
             and doc[key]["complete_Dalg_not_claimed_by_this_bound"] is True
             and doc[key]["no_comparison_or_subtraction_from_old_Calg"] is True)
        persist(args.out, doc)

        doc["stage"] = "complete_final_readonly_and_shape_checks"
        gate(doc, 13, all(sha(paths[e["role"]].read_bytes()) == e["sha256"]
                          for e in manifest["files"])
             and sha(args.manifest.read_bytes())
                 == doc["input_manifest_sha256"] == args.manifest_sha
             and canonical(doc["complete_prior_scientific_conclusion_read_verbatim"])
                 == paths["prior_science"].read_bytes()
             and sha(canonical(doc["complete_prior_scientific_conclusion_read_verbatim"]))
                 == PIN_SPECS["prior_science"]["sha256"]
             and sha(canonical(doc["accepted_prior_input"])) == FROZEN_ACCEPTED_PRIOR_SHA256
             and all(doc["actual_progress"][k] == 0 for k in (
                 "old_scientific_targets_recomputed",
                 "old_scientific_producers_imported_or_called",
                 "old_exponentials_or_logarithms_evaluated",
                 "historical_or_native_inputs_restored")))
        gate(doc, 14, all(complete_graph_shape(doc[k], shape)
                          and scalar_slot_count(doc[k], shape) == NEW_GRAPH_SLOT_COUNTS[k]
                          for k, shape in NEW_GRAPH_SHAPES.items())
             and sum(scalar_slot_count(doc[k], shape)
                     for k, shape in NEW_GRAPH_SHAPES.items()) == 49
             and doc["actual_progress"] == SUCCESS_ACTUAL_PROGRESS
             and doc["planned_shape"] == PLANNED_SHAPE
             and doc["complete_operator_identity_conclusion"] == OPERATOR_IDENTITY)
        doc["actual_mathematical_wall_seconds"] = time.monotonic() - began
        gate(doc, 15, set(doc) == set(COMPLETE_FIELDS) and len(doc) == 31
             and doc["retained_scope"] == RETAINED_SCOPE
             and doc["parameters"] == PARAMETERS
             and len(doc["gates"]) == 15
             and [g["name"] for g in doc["gates"]] == GATE_NAMES[:15]
             and all(g["passed"] is True for g in doc["gates"]))
        doc.update(complete=True, proved=True, actual_returncode=0,
                   failure=None, stage="complete")
    except BaseException as error:
        doc.update(complete=False, proved=False, actual_returncode=1,
            failure=operation_failure(error),
            actual_mathematical_wall_seconds=time.monotonic() - began)
        doc["failed_new_stage_diagnostic"] = {
            "stage": doc["stage"],
            "prior_admission_complete": doc["actual_progress"]["accepted_prior_successes"] == 1,
            "returned_graph_fields_available": [
                k for k in NEW_GRAPH_SHAPES if isinstance(doc.get(k), dict)],
            "all_original_scientific_targets_remain_frozen": True,
            "complete_new_positive_or_coefficient_conclusions_authorized": False,
        }
        persist(args.out, doc)
        print_complete_document(doc)
        raise
    raw = persist(args.out, doc)
    print_complete_document(doc)
    if len(raw) > COMPLETE_SCIENCE_MAX_BYTES:
        raise ValueError("complete science saved and printed; publication byte budget exceeded")


if __name__ == "__main__":
    main()
