#!/usr/bin/env python3
"""New frozen reflected common-input and stable-inverse constants.
Four complete saved receipts are read only. No old exponential, logarithm,
root comparison, R97 graph, RNE polynomial or scientific producer is evaluated.
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
SOURCE="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_frozen_common_input_uniform_inverse_constants.py"
WORKER="topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_frozen_common_input_uniform_inverse_constants_public_worker.py"
KIND="complete_frozen_common_input_uniform_inverse_constants_v1"
MANIFEST_KIND="frozen_common_input_uniform_inverse_constants_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=16
COMPLETE_SCIENCE_MAX_BYTES=75000
PIN_SPECS=json.loads("{\"contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-uniform-frozen-selected-input-coordinates-for-the-real-reference-family.md\",\"git_blob\":\"d606faa1ffd30c34d3487985a57dbc62a18890bc\",\"bytes\":32942,\"sha256\":\"8f3784473b98f9b49449b7012e4c5c919670418246fa03a7f28441aaca28b640\"},\"tf_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json\",\"git_blob\":\"3766aea85aba59230be3813b4b7634d318316e49\",\"bytes\":18206,\"sha256\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\"},\"kl_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/correlated_terminal_Ai_leading_scalar_ci/run-43766439345-1/actual-scientific-conclusion.json\",\"git_blob\":\"d24a1ecdd9b4397184a3ab932a503e8eb79d0c24\",\"bytes\":20537,\"sha256\":\"1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee\"},\"wx_execution\":{\"path\":\"topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json\",\"git_blob\":\"5121a599896025d90e2861450756a256aaba659d\",\"bytes\":43753,\"sha256\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\"},\"rne_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/root_natural_negative_window_explicit_constants_ci/run-43792291190-1/actual-scientific-conclusion.json\",\"git_blob\":\"6f4ddebe683c0a22cb726d8ff7f8e7269146e46d\",\"bytes\":57079,\"sha256\":\"579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086\"}}")
RULES=json.loads("{\"path\":\"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json\",\"git_blob\":\"5c5d020913d717bb5bc8ce891297e00eaa8944f7\",\"bytes\":2461,\"sha256\":\"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1\"}")
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":16,\"expected_current_inputs\":8,\"expected_total_inputs\":8,\"expected_Python_AST_files\":2,\"expected_historical_inputs\":0,\"original_actual_runs\":{\"TF\":\"43766881076/1\",\"KL\":\"43766439345/1\",\"WX\":\"43763424840/1\",\"RNE\":\"43792291190/1\"},\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_intrinsic_parameter\":\"-7789843107295549/4611686018427387904\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"physical_root_piece\":2549,\"physical_period\":\"pi/2\",\"normalized_angular_measure\":true,\"physical_frequency\":\"n=4|j|\",\"original_natural_cutoff_abs_j\":97,\"actual_common_root_cutoff_abs_j\":1024,\"coordinate_windows\":[\"0\",\"-4/3\"],\"natural_negative_windows\":[\"-7/6\",\"-5/2\"],\"stable_output_windows\":[\"-1/6\",\"-3/2\"],\"exact_gamma97\":\"150545/150544\",\"fixed_selected_parameter_absolute_upper\":\"0.00000000009368259853002\",\"frozen_input_space\":\"X_s_fr = S_star D_plus H_nat^s\",\"natural_reflection_not_all_signed_carriers\":true,\"original_primitive_and_two_physical_means_retained\":true,\"independent_physical_means\":2,\"saved_actual_receipts\":4,\"saved_scalar_records\":16,\"saved_original_scope_collections\":4,\"new_principal_scalar_outputs\":7,\"new_elementary_scalar_records\":16,\"new_total_scalar_records\":23,\"optional_forward_Cs_constants_evaluated\":false,\"varying_selected_chart_identifications_evaluated\":false,\"old_target_calls_allowed\":0,\"old_source_imports_allowed\":0,\"old_exponentials_or_logarithms_reevaluated\":0,\"old_R97_RNE_graphs_or_comparisons_reevaluated\":0,\"full_incoming_or_finite_Schur_inverse_claimed\":false,\"full_complex_parameter_square_claimed\":false,\"uniform_selected_conjugacy_family_claimed\":false}")
RETAINED_SCOPE=json.loads("{\"scientific_target\":\"uniform frozen reflected common input coordinates and two stable inverse window constants\",\"same_real_delta_family_and_fixed_intrinsic_eta0\":true,\"original_two_signed_carriers_and_natural_reflection_retained\":true,\"fixed_Dplus_phase_is_included_in_the_input_space\":true,\"TF_parity_and_sign_commutation_have_distinct_proofs\":true,\"natural_reflection_projection_not_replaced_by_full_signed_P97\":true,\"selected_H_and_S_are_frozen_once_not_extended_as_KAM_family\":true,\"forward_leading_uses_the_saved_reverse_radial_bound\":true,\"short_factor_has_original_absolute_rate_qualification\":true,\"root_eta_lower_from_full_original_coefficient_domain\":true,\"complete_mean_residual_used_in_exact_radial_correlation\":true,\"same_distributional_inverse_in_both_windows\":true,\"exact_weight_and_coordinate_order_retained\":true,\"independent_physical_mean_coordinates\":2,\"full_density_mean_identity_corrections_retained\":true,\"original_low_head_second_reference_and_infinite_radial_ports_retained\":true,\"old_actual_objects_read_only_and_scopes_not_widened\":true,\"old_R97_RNE_graphs_and_comparison_not_recomputed\":true,\"physical_bulk_Poisson_extension_newly_proved\":false,\"complete_incoming_inverse_claimed\":false,\"finite_Schur_inverse_claimed\":false,\"Riccati_operator_norm_continuity_claimed\":false,\"uniform_selected_conjugacy_family_claimed\":false,\"nonlinear_background_or_final_surface_claimed\":false,\"same_selected_ambient_operator_formula_at_original_delta_star\":true,\"old_SE8_literal_Sstar_Hnat_domain_not_claimed\":true,\"full_circle_principal_or_Cayley_restriction_proved\":false}")
PLANNED_SHAPE=json.loads("{\"saved_actual_receipts\":4,\"saved_original_scope_collections\":4,\"saved_scalar_records\":16,\"new_forward_leading_scalars\":1,\"new_coordinate_window_bounds\":4,\"new_frozen_stable_inverse_windows\":2,\"new_principal_scalar_outputs\":7,\"new_elementary_scalar_records\":16,\"new_total_scalar_records\":23,\"new_pi_constants\":1,\"new_fixed_square_roots\":1,\"new_positive_sixth_roots\":1,\"new_optional_forward_Cs_constants\":0,\"retained_physical_means\":2}")
INITIAL_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":0,\"saved_original_scalar_records\":0,\"saved_original_scope_collections\":0,\"new_forward_leading_scalar_completed\":0,\"new_common_input_window_bounds_completed\":0,\"new_frozen_stable_inverse_windows_completed\":0,\"new_pi_constants_completed\":0,\"new_fixed_square_roots_completed\":0,\"new_positive_sixth_roots_completed\":0,\"new_elementary_factor_records_completed\":0,\"old_scientific_targets_recomputed\":0,\"old_exponentials_reevaluated\":0,\"old_logarithms_reevaluated\":0,\"old_R97_RNE_graphs_or_comparisons_recomputed\":0,\"historical_inputs_restored\":0}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"accepted_original_successes\":4,\"saved_original_scalar_records\":16,\"saved_original_scope_collections\":4,\"new_forward_leading_scalar_completed\":1,\"new_common_input_window_bounds_completed\":4,\"new_frozen_stable_inverse_windows_completed\":2,\"new_pi_constants_completed\":1,\"new_fixed_square_roots_completed\":1,\"new_positive_sixth_roots_completed\":1,\"new_elementary_factor_records_completed\":16,\"old_scientific_targets_recomputed\":0,\"old_exponentials_reevaluated\":0,\"old_logarithms_reevaluated\":0,\"old_R97_RNE_graphs_or_comparisons_recomputed\":0,\"historical_inputs_restored\":0}")
PUBLICATION_LIMITS=json.loads("{\"complete_science_bytes\":75000,\"complete_report_bytes\":8000,\"complete_prepublication_science_report_payload_bytes\":90000,\"complete_execution_bytes\":59000,\"pre_science_topic_reserve_bytes\":150000,\"target_complete_science_bytes\":35000,\"target_complete_prepublication_payload_bytes\":50000,\"scientific_file_atomic_and_complete_stdout_before_size_guards\":true,\"new_artifacts\":0,\"new_Releases\":0}")
COMPLETE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"input_sha256\",\"verified_original_inputs\",\"accepted_old_inputs\",\"complete_original_scope_fields_read_verbatim\",\"complete_original_scope_fields_sha256\",\"complete_saved_scalar_records_read_verbatim\",\"complete_saved_scalar_records_sha256\",\"complete_forward_leading_conclusion\",\"complete_coordinate_conclusion\",\"complete_frozen_stable_inverse_conclusion\",\"complete_operator_identity_conclusion\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"gates\",\"actual_mathematical_wall_seconds\"]")
GATE_NAMES=json.loads("[\"actual public Actions runtime and the frozen new source are exact\",\"eight current small texts and the complete new parameter closure are frozen\",\"all five mathematical primaries retain their original bytes SHA and Git identity\",\"the TF complete fourteen gate success retains its full family and same two window inverse\",\"the KL complete sixteen gate success retains the full correlated mean and absolute short rate\",\"the WX complete twenty gate success retains its original embedded schema runtime and selected scope\",\"the RNE complete sixteen gate success retains both original natural negative inverse records\",\"the common family and frozen reflected phase domain retain every original endpoint and mean\",\"sixteen complete old scalar records and all required original scope fields are preserved\",\"the new complete forward leading bound uses the true reverse factor and a positive denominator\",\"both coordinate windows retain complete forward and inverse products in their exact order\",\"both frozen stable inverse windows retain the natural weights and the exact rational gamma\",\"all original inputs and records remain unchanged with zero old scientific evaluation\",\"all twenty three new scalar records and the complete operator identities are retained\",\"actual progress and every declared new scalar count match the complete target\",\"the complete thirty two field schema preserves the frozen reflected domain and every independent port\"]")
NEW_GRAPH_SHAPES=json.loads("{\"complete_forward_leading_conclusion\":{\"complete_pi_interval\":\"__FINITE_SCALAR__\",\"complete_two_pi_interval\":\"__FINITE_SCALAR__\",\"complete_sqrt_two_pi_lower\":\"__FINITE_SCALAR__\",\"complete_inverse_sqrt_two_pi_upper\":\"__FINITE_SCALAR__\",\"complete_root_k_over_eta_upper\":\"__FINITE_SCALAR__\",\"complete_root_ratio_sixth_upper\":\"__FINITE_SCALAR__\",\"complete_root_to_waist_radial_upper\":\"__FINITE_SCALAR__\",\"complete_density_times_radial_upper\":\"__FINITE_SCALAR__\",\"complete_forward_leading_prefactor_upper\":\"__FINITE_SCALAR__\",\"complete_forward_leading_scalar_upper\":\"__FINITE_SCALAR__\",\"exact_formula\":\"ng_waist_upper * saved_reverse_radial_upper * saved_absolute_short_exp_upper * (2*pi)^(-1/2) * (Kr_root_upper/eta_root_lower)^(1/6)\",\"all_four_terminal_Ai_sign_wave_moduli_share_one_bound\":true,\"saved_absolute_short_exponential_used_in_both_directions\":true,\"positive_lower_endpoint_roles\":[\"eta_root_lower\",\"sqrt_two_pi_lower\"],\"old_exponential_not_recomputed\":true,\"true_waist_reverse_radial_factor_used\":true,\"root_full_coefficient_eta_lower_not_cut_only\":true,\"no_sector_sum_or_extra_sqrt2\":true},\"complete_coordinate_conclusion\":{\"windows\":{\"0\":{\"input_and_output_exponent\":\"0\",\"complete_Lambda_TF_inverse_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_upper\":\"__FINITE_SCALAR__\",\"complete_S_TF_forward_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_inverse_upper\":\"__FINITE_SCALAR__\",\"same_inverse_in_the_two_windows\":true},\"-4/3\":{\"input_and_output_exponent\":\"-4/3\",\"complete_Lambda_TF_inverse_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_upper\":\"__FINITE_SCALAR__\",\"complete_S_TF_forward_product_upper\":\"__FINITE_SCALAR__\",\"complete_Ni_inverse_upper\":\"__FINITE_SCALAR__\",\"same_inverse_in_the_two_windows\":true}},\"exact_Ni_order\":\"Lambda_plus_delta^-1 T_F_delta^-1 S_star^-1\",\"exact_inverse_order\":\"S_star T_F_delta Lambda_plus_delta\",\"frozen_input_space\":\"X_s_fr = S_star D_plus H_nat^s\",\"original_natural_cutoff_abs_j\":97,\"actual_common_root_cutoff_abs_j\":1024,\"reflection_domain_transported_by_fixed_Dplus\":true,\"independent_mean_and_other_ports_use_identity_extension\":true},\"complete_frozen_stable_inverse_conclusion\":{\"exact_gamma97\":\"150545/150544\",\"complete_gamma97_upper\":\"__FINITE_SCALAR__\",\"windows\":{\"0\":{\"common_input_exponent\":\"0\",\"natural_exponent\":\"-7/6\",\"stable_output_exponent\":\"-1/6\",\"complete_coordinate_times_natural_inverse_upper\":\"__FINITE_SCALAR__\",\"complete_frozen_stable_inverse_upper\":\"__FINITE_SCALAR__\",\"uses_same_original_natural_distributional_inverse\":true},\"-4/3\":{\"common_input_exponent\":\"-4/3\",\"natural_exponent\":\"-5/2\",\"stable_output_exponent\":\"-3/2\",\"complete_coordinate_times_natural_inverse_upper\":\"__FINITE_SCALAR__\",\"complete_frozen_stable_inverse_upper\":\"__FINITE_SCALAR__\",\"uses_same_original_natural_distributional_inverse\":true}},\"exact_forward_order\":\"N_out^-1 S_nat_delta N_in^(7/6) Ni_delta_fr\",\"exact_inverse_order\":\"Ni_delta_fr^-1 N_in^(-7/6) S_nat_delta^-1 N_out\",\"old_natural_inverse_polynomials_not_recomputed\":true,\"frequency_weights_only_on_original_high_spaces\":true,\"optional_forward_Cs_constants_not_evaluated\":true}}")
OPERATOR_IDENTITY=json.loads("{\"full_signed_carrier_space\":\"H_car^s = P97 H^s\",\"natural_space\":\"H_nat^s is the original SE reflected high space\",\"Dplus\":\"exp(-i*pi/4) Pi_plus + exp(i*pi/4) Pi_minus\",\"Lambda_plus_on_high_nonmean\":\"Lambda_plus_delta = a_delta D_plus with a_delta > 0\",\"frozen_input_space\":\"X_s_fr = S_star D_plus H_nat^s = (Ni_delta_star)^-1 H_nat^s\",\"frozen_norm\":\"inherited physical H^s norm\",\"natural_projector\":\"Q_fr = S_star D_plus Q_nat D_plus^-1 S_star^-1\",\"ambient_high_projector\":\"P_fr = S_star P97 S_star^-1\",\"natural_and_ambient_projectors_not_identified\":true,\"TF_reflection_identity\":\"R M_Fstar R = -M_Fstar and R I R = -I; R commutes with P1024\",\"TF_same_inverse_preserves_original_natural_reflection\":true,\"fixed_input_identity_across_delta\":\"identity on X_s_fr\",\"exact_Ni_restriction\":\"Ni_delta_fr(S_star D_plus f) = a_delta^-1 T_F_delta^-1 f\",\"independent_rest_extension\":\"diag(Ni_delta_fr, Id_rest); rest may include infinite radial ports\",\"full_circle_scalar_mean_not_scaled_by_a_delta\":true,\"physical_mean_coordinates\":2,\"selected_KAM_conjugacy_only_at_original_delta_star\":true,\"new_full_incoming_or_finite_Schur_inverse_proved\":false,\"old_SE8_literal_domain_corrected\":true,\"full_circle_principal_Cayley_restriction_needs_separate_domain_range\":true}")
SCALAR_PATHS=json.loads("{\"ng_waist_upper\":[\"kl_science\",\"copied_complete_input_objects\",\"WT_complete_SP_waist_factors\",\"density_radial_factor_upper\"],\"Kr_root_upper\":[\"kl_science\",\"copied_complete_input_objects\",\"FA_complete_root_mean_value_q_bounds\",\"complete_Kr_upper\"],\"eta_root_lower\":[\"tf_science\",\"complete_new_root_coefficient_conclusion\",\"complete_original_eta_lower_used_verbatim\"],\"saved_reverse_radial_upper\":[\"kl_science\",\"copied_complete_input_objects\",\"WX_complete_ungauged_leading_flow_conclusion\",\"complete_reverse_radial_exponential_upper\"],\"saved_absolute_short_exp_upper\":[\"kl_science\",\"complete_new_root_short_conclusion\",\"complete_inverse_root_to_cut_radial_factor_upper\"],\"KLambda_inverse_upper\":[\"kl_science\",\"complete_new_leading_scalar_conclusion\",\"complete_inverse_leading_scalar_upper\"],\"KF_forward_0\":[\"tf_science\",\"complete_new_root_normalizer_conclusion\",\"complete_forward_L2_upper\"],\"KF_forward_minus4_3\":[\"tf_science\",\"complete_new_root_normalizer_conclusion\",\"complete_forward_Hminus4_3_upper\"],\"KF_inverse_0\":[\"tf_science\",\"complete_new_root_normalizer_conclusion\",\"complete_inverse_L2_upper\"],\"KF_inverse_minus4_3\":[\"tf_science\",\"complete_new_root_normalizer_conclusion\",\"complete_inverse_Hminus4_3_upper\"],\"KS_forward_0\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_L2_upper\"],\"KS_forward_minus4_3\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_Hminus4_3_upper\"],\"KS_inverse_0\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_inverse_L2_upper\"],\"KS_inverse_minus4_3\":[\"wx_execution\",\"complete_selected_common_input_conclusion\",\"complete_common_input_inverse_Hminus4_3_upper\"],\"Knat_minus7_6\":[\"rne_science\",\"complete_natural_inverse_conclusion\",\"windows\",\"-7/6\",\"complete_Snat_inverse_upper\"],\"Knat_minus5_2\":[\"rne_science\",\"complete_natural_inverse_conclusion\",\"windows\",\"-5/2\",\"complete_Snat_inverse_upper\"]}")
SCOPE_PATHS=json.loads("{\"tf_science\":[\"parameters.continuous_centre_definition_sha256\",\"parameters.continuous_response_definition_sha256\",\"parameters.exact_real_delta_radius\",\"parameters.fixed_intrinsic_parameter\",\"parameters.exact_root_interval\",\"parameters.exact_strict_cut\",\"parameters.eta_lower_scope\",\"parameters.original_input_order\",\"parameters.physical_frequency\",\"parameters.independent_physical_means\",\"complete_new_root_coefficient_conclusion.angular_degree\",\"complete_new_root_coefficient_conclusion.original_full_complex_eta_domain_includes_root\",\"complete_new_root_coefficient_conclusion.cut_only_row790_eta_not_used\",\"complete_new_root_coefficient_conclusion.root_mean_and_both_Fourier_signs_retained\",\"complete_new_root_normalizer_conclusion.actual_J_F\",\"complete_new_root_normalizer_conclusion.same_inverse_on_both_windows\",\"complete_new_root_normalizer_conclusion.below_J_F_and_independent_mean_ports_are_identity\",\"complete_new_root_normalizer_conclusion.root_cutoff_is_not_moving_Js_or_principal_angle_cutoff\",\"complete_new_root_normalizer_conclusion.right_transformed_finite_rows_keep_actual_dual_norms\"],\"kl_science\":[\"parameters.continuous_centre_definition_sha256\",\"parameters.continuous_response_definition_sha256\",\"parameters.exact_real_delta_radius\",\"parameters.fixed_intrinsic_parameter\",\"parameters.exact_root_interval\",\"parameters.exact_strict_cut\",\"parameters.exact_short_interval_upper_length\",\"parameters.reference_column\",\"parameters.independent_physical_means\",\"parameters.root_mean_residual_set_to_zero\",\"parameters.all_four_moduli_equal_for_this_reference_column\",\"complete_new_root_short_conclusion.complete_mean_state_used\",\"complete_new_root_short_conclusion.root_point_not_replaced_by_bracket_midpoint\",\"complete_new_root_short_conclusion.old_WL_products_used_only_at_delta_zero_off_the_metric_support\",\"complete_new_root_short_conclusion.original_cut_eta_upper_not_reused_at_root\",\"copied_complete_input_objects.FA_complete_root_mean_value_q_bounds.whole_segment_in_one_original_germ\",\"copied_complete_input_objects.FA_complete_root_mean_value_q_bounds.exact_root_distance\",\"copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.exact_evolution\",\"copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.exact_scalar_radial_rate\",\"copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.reverse_orientation\",\"copied_complete_input_objects.WX_complete_ungauged_leading_flow_conclusion.true_radial_interval\",\"complete_new_leading_scalar_conclusion.same_input_multiplier_in_every_window\",\"complete_new_leading_scalar_conclusion.second_Bi_or_other_genuine_root_column_covered\",\"complete_new_leading_scalar_conclusion.original_order\",\"complete_new_leading_scalar_conclusion.physical_means_and_transported_finite_blocks_independent\",\"complete_new_leading_scalar_conclusion.root_mean_residual_retained_in_exact_log_derivative\"],\"wx_execution\":[\"mathematical_parameters.exact_real_delta_radius\",\"mathematical_parameters.fixed_intrinsic_parameter\",\"mathematical_parameters.exact_root_interval\",\"mathematical_parameters.exact_strict_cut\",\"mathematical_parameters.selected_common_input_order\",\"mathematical_parameters.selected_conjugacy_parameter_absolute_upper\",\"mathematical_parameters.selected_conjugacy_derivative_lower\",\"mathematical_parameters.selected_conjugacy_derivative_upper\",\"mathematical_parameters.selected_conjugacy_second_derivative_upper\",\"mathematical_parameters.complete_mean_coordinates\",\"scope\",\"complete_selected_common_input_conclusion.exact_order\",\"complete_selected_common_input_conclusion.inverse_order\",\"complete_selected_common_input_conclusion.only_same_selected_actual_conjugacy\",\"complete_selected_common_input_conclusion.independent_mean_block_retained\",\"complete_selected_common_input_conclusion.no_projection_commuted_through_coordinate\"],\"rne_science\":[\"parameters.exact_real_delta_radius\",\"parameters.fixed_intrinsic_parameter\",\"parameters.exact_intrinsic_parameter\",\"parameters.exact_root_interval\",\"parameters.physical_root_piece\",\"parameters.physical_period\",\"parameters.normalized_angular_measure\",\"parameters.physical_frequency\",\"parameters.input_cutoff_abs_j\",\"parameters.natural_negative_windows\",\"retained_scope\",\"complete_natural_inverse_conclusion.exact_order\",\"complete_natural_inverse_conclusion.two_natural_negative_windows_certified\",\"complete_natural_inverse_conclusion.uniform_real_delta_family_only\",\"complete_natural_inverse_conclusion.independent_physical_means_retained\",\"complete_natural_inverse_conclusion.selected_common_input_inverse_left_factor_remains_separate\",\"complete_natural_inverse_conclusion.true_Riccati_operator_norm_continuity_claimed\"]}")
EXPECTED_ACCEPTED=json.loads("{\"original_successes\":{\"tf_science\":{\"file_path\":\"topics/visible-flex-exact-nearby/notes/common_root_normalizer_two_window_ci/run-43766881076-1/actual-scientific-conclusion.json\",\"file_git_blob\":\"3766aea85aba59230be3813b4b7634d318316e49\",\"file_bytes\":18206,\"file_sha256\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"science_location\":\"complete standalone scientific object\",\"science_canonical_bytes\":18206,\"science_canonical_sha256\":\"a1c20307e211d6e1478bccbaab316bd1592f066cde6c5882dfa77d41a2163720\",\"kind\":\"actual_common_root_normalizer_two_window_v1\",\"run_id\":\"43766881076\",\"run_attempt\":\"1\",\"source_sha256\":\"bf71639da0bc9e41ab86f9530fe02b34399c18e63e9041fa0c3abd0852ccdc4b\",\"input_manifest_sha256\":\"027a4462a2cc0424abf00bb03456b63b0811700e98e5ddd28ba1d4d793aefacf\",\"workflow_event_commit\":\"0107666b538ced3a0fbc91f6a7f2cfa894f8ef6f\",\"actual_scientific_checkout_commit\":\"8839cad6bdb5bdd7b5f09959cbc3a20c55c680c6\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"gate_count\":14,\"passed_gate_count\":14,\"complete_original_gates_sha256\":\"d8cf1f82f556ed32ea44309e407f8fe264e769275311ca7787d5913291466cb7\"},\"kl_science\":{\"file_path\":\"topics/visible-flex-exact-nearby/notes/correlated_terminal_Ai_leading_scalar_ci/run-43766439345-1/actual-scientific-conclusion.json\",\"file_git_blob\":\"d24a1ecdd9b4397184a3ab932a503e8eb79d0c24\",\"file_bytes\":20537,\"file_sha256\":\"1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee\",\"science_location\":\"complete standalone scientific object\",\"science_canonical_bytes\":20537,\"science_canonical_sha256\":\"1ea36ae6462bf34bbda338cca3af6ad1cff3b5f3f6d293ed81fcb94472deadee\",\"kind\":\"actual_correlated_terminal_Ai_leading_scalar_v1\",\"run_id\":\"43766439345\",\"run_attempt\":\"1\",\"source_sha256\":\"1f9dd122c7de8a990f5c60d0f405b2e3b3e51420b807ded9be58e8715fd480d6\",\"input_manifest_sha256\":\"810a13c2e1e0d3fb85f00129ca3e826e00e264d78269e25b78408bc1f67b99c7\",\"workflow_event_commit\":\"8dcbbfefe6fa27bbbeb2f61da76e05083fbfb988\",\"actual_scientific_checkout_commit\":\"4af263bb810f74ab57be1088bbcb9560b06e2c7f\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"gate_count\":16,\"passed_gate_count\":16,\"complete_original_gates_sha256\":\"45a617db8d31e61d46c0f0a8f2d4f8dd9bb614feb3d3d38704147ff163182a1f\"},\"wx_execution\":{\"file_path\":\"topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json\",\"file_git_blob\":\"5121a599896025d90e2861450756a256aaba659d\",\"file_bytes\":43753,\"file_sha256\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\",\"science_location\":\"embedded actual_scientific_receipt\",\"science_canonical_bytes\":31088,\"science_canonical_sha256\":\"536e5f33441570eec1b0b35091400f815c5333c4cfd3f0f731099f5dd48cb015\",\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run_id\":\"43763424840\",\"run_attempt\":\"1\",\"source_sha256\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"input_manifest_sha256\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"workflow_event_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\",\"actual_scientific_checkout_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"arithmetic_bits\":320,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"gate_count\":20,\"passed_gate_count\":20,\"complete_original_gates_sha256\":\"4c8f214fc05eaf3c8c3a9970a41921037356bf0f9021ef1b1ec942c485b90d47\"},\"rne_science\":{\"file_path\":\"topics/visible-flex-exact-nearby/notes/root_natural_negative_window_explicit_constants_ci/run-43792291190-1/actual-scientific-conclusion.json\",\"file_git_blob\":\"6f4ddebe683c0a22cb726d8ff7f8e7269146e46d\",\"file_bytes\":57079,\"file_sha256\":\"579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086\",\"science_location\":\"complete standalone scientific object\",\"science_canonical_bytes\":57079,\"science_canonical_sha256\":\"579b09aa7164ec4800187436248fdafca85691066afa419ed6fa8b6ab1de3086\",\"kind\":\"complete_root_natural_negative_window_explicit_constants_v1\",\"run_id\":\"43792291190\",\"run_attempt\":\"1\",\"source_sha256\":\"fc7b4ceee05768c1aa5267b01c04dd721e286225d873d48ded954c9d4789f3d5\",\"input_manifest_sha256\":\"e311c5119accc5ba90585e49a3bb24bbe672eb601977ebc29720e24979a9128b\",\"workflow_event_commit\":\"58e9eaf49412f25a62af80920a33f21ec0c11491\",\"actual_scientific_checkout_commit\":\"58e9eaf49412f25a62af80920a33f21ec0c11491\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"complete\":true,\"proved\":true,\"actual_returncode\":0,\"gate_count\":16,\"passed_gate_count\":16,\"complete_original_gates_sha256\":\"00ba13dcff64d117e0c63ba3607617c72eeb7db44eb38d1d75f581fdd5515028\"}},\"original_scope_fields_sha256\":\"3f12846bb79fc7cefd00649fecf6ac4ca3a7babe7fa584ff7cace9cf90f58c73\",\"original_scalar_records_sha256\":\"57731cdef27a9fa90024339d9d4d4e58daef926f532f5d2290a1956516073b10\",\"four_original_science_objects_not_recomputed\":true,\"original_scope_fragments_are_exact_path_values_not_full_objects\":true}")
FROZEN_SAVED_SCALAR_RECORDS_SHA256="57731cdef27a9fa90024339d9d4d4e58daef926f532f5d2290a1956516073b10"
FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256="3f12846bb79fc7cefd00649fecf6ac4ca3a7babe7fa584ff7cace9cf90f58c73"
FROZEN_ACCEPTED_OLD_INPUTS_SHA256="269bbedf447b770ffc9cd27085fc932a26cca3c80df62ff37595d54ab24983fc"
ORIGINAL_SCIENCE_FIELD_COUNTS={"tf_science":38,"kl_science":38,"wx_execution":55,"rne_science":35}

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
    print("BEGIN_COMPLETE_FROZEN_COMMON_INPUT_UNIFORM_INVERSE_SCIENCE_JSON",flush=True)
    print(canonical(doc).decode("utf-8"),end="",flush=True)
    print("END_COMPLETE_FROZEN_COMMON_INPUT_UNIFORM_INVERSE_SCIENCE_JSON",flush=True)

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
        and manifest.get("expected_current_input_count")==8
        and manifest.get("expected_input_count")==8
        and len(entries)==len(by_role)==8 and set(by_role)==set(expected_paths)
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
        require(not data.startswith(b"\x1f\x8b"),"no gzip input in NIF")
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
    contract=paths["contract"].read_text()
    gate(doc,2,len(verified)==5
        and manifest.get("complete_input_bytes")==sum(entry["bytes"] for entry in entries)
        and manifest.get("file_sha256")=={entry["path"]:entry["sha256"] for entry in entries}
        and manifest.get("mathematical_input_sha256")=={k:v["sha256"] for k,v in PIN_SPECS.items()}
        and all(tag in contract for tag in
            (r"\tag{NIF.7}",r"\tag{NIF.10a}",r"\tag{NIF.11a}",r"\tag{NIF.16}",
             r"\tag{NIF.18a}",r"\tag{NIF.23}",r"\tag{NIF.26}"))
        and by_role["source"]["sha256"]==sha(Path(__file__).read_bytes()))
    return manifest,paths

def original_science(role,path):
    raw=path.read_bytes()
    whole=json.loads(raw)
    science=whole["actual_scientific_receipt"] if role=="wx_execution" else whole
    expected=EXPECTED_ACCEPTED["original_successes"][role]
    scientific_raw=canonical(science)
    fields=("kind","run_id","run_attempt","source_sha256","input_manifest_sha256",
            "workflow_event_commit","actual_scientific_checkout_commit","runtime","arithmetic_bits",
            "complete","proved","actual_returncode")
    require(len(science)==ORIGINAL_SCIENCE_FIELD_COUNTS[role],"original scientific schema changed")
    require(all(science.get(key)==expected[key] for key in fields),"original success identity changed")
    require(science["complete"] is True and science["proved"] is True
        and science["actual_returncode"]==0 and science["failure"] is None,
        "original complete zero child required")
    gates=science["gates"]
    require(len(gates)==expected["gate_count"]
        and all(set(row)=={"name","passed"} and row["passed"] is True for row in gates)
        and sha(canonical(gates))==expected["complete_original_gates_sha256"],
        "original full gate receipt changed")
    require(len(scientific_raw)==expected["science_canonical_bytes"]
        and sha(scientific_raw)==expected["science_canonical_sha256"],
        "original full scientific bytes changed")
    require(len(raw)==expected["file_bytes"] and sha(raw)==expected["file_sha256"]
        and git_blob(raw)==expected["file_git_blob"],"original file identity changed")
    if role=="wx_execution":
        require(whole["kind"]=="actual_public_true_waist_coordinates_saved_products_execution"
            and whole["complete"] is True and whole["actual_returncode"]==0
            and whole["actual_failure"] is None and whole["actual_source_budget_processes"]==1
            and whole["run_id"]==science["run_id"] and whole["run_attempt"]==science["run_attempt"]
            and whole["workflow_commit"]==science["workflow_event_commit"]
            and whole["actual_scientific_checkout_commit"]==science["actual_scientific_checkout_commit"]
            and whole["source_budget_source_sha256"]==science["source_sha256"]
            and whole["input_manifest_sha256"]==science["input_manifest_sha256"],
            "WX embedded and original wrapper identities changed")
        outputs={entry["file"]:entry for entry in whole["output_hashes"]}
        require(outputs["consumers/process.json"]["bytes"]==len(scientific_raw)
            and outputs["consumers/process.json"]["sha256"]==sha(scientific_raw),
            "WX original complete process receipt changed")
    else:
        require(scientific_raw==raw,"original standalone canonical bytes changed")
    actual=dict(file_path=PIN_SPECS[role]["path"],file_git_blob=git_blob(raw),
        file_bytes=len(raw),file_sha256=sha(raw),
        science_location="embedded actual_scientific_receipt" if role=="wx_execution"
            else "complete standalone scientific object",
        science_canonical_bytes=len(scientific_raw),science_canonical_sha256=sha(scientific_raw),
        gate_count=len(gates),passed_gate_count=sum(row["passed"] is True for row in gates),
        complete_original_gates_sha256=sha(canonical(gates)))
    actual.update({key:copy.deepcopy(science[key]) for key in fields})
    require(actual==expected,"complete accepted provenance changed")
    return science,actual

def accepted_original_inputs(paths,doc):
    originals={}
    accepted={"original_successes":{}}
    for index,role in enumerate(("tf_science","kl_science","wx_execution","rne_science"),3):
        science,receipt=original_science(role,paths[role])
        originals[role]=science
        accepted["original_successes"][role]=receipt
        doc["accepted_old_inputs"]=copy.deepcopy(accepted)
        doc["actual_progress"]["accepted_original_successes"]+=1
        gate(doc,index,receipt==EXPECTED_ACCEPTED["original_successes"][role])
    tf=originals["tf_science"]
    kl=originals["kl_science"]
    wx=originals["wx_execution"]
    rne=originals["rne_science"]
    tfp,klp,wxp,rp=tf["parameters"],kl["parameters"],wx["mathematical_parameters"],rne["parameters"]
    same_family=all(p["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"]
        and p["fixed_intrinsic_parameter"]=="eta_0"
        and p["exact_root_interval"]==PARAMETERS["exact_root_interval"] for p in (tfp,klp,wxp,rp))
    same_cut=all(p["exact_strict_cut"]==PARAMETERS["exact_strict_cut"] for p in (tfp,klp,wxp))
    tfroot=tf["complete_new_root_coefficient_conclusion"]
    tfnorm=tf["complete_new_root_normalizer_conclusion"]
    kshort=kl["complete_new_root_short_conclusion"]
    klead=kl["complete_new_leading_scalar_conclusion"]
    kroot=kl["copied_complete_input_objects"]["FA_complete_root_mean_value_q_bounds"]
    kflow=kl["copied_complete_input_objects"]["WX_complete_ungauged_leading_flow_conclusion"]
    wxc=wx["complete_selected_common_input_conclusion"]
    rn=rne["complete_natural_inverse_conclusion"]
    gate(doc,7,same_family and same_cut
        and tfp["continuous_centre_definition_sha256"]==klp["continuous_centre_definition_sha256"]
            =="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
        and tfp["continuous_response_definition_sha256"]==klp["continuous_response_definition_sha256"]
            =="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
        and rp["exact_intrinsic_parameter"]==PARAMETERS["exact_intrinsic_parameter"]
        and rp["physical_root_piece"]==2549 and rp["input_cutoff_abs_j"]==97
        and tfroot["angular_degree"]==192
        and tfroot["original_full_complex_eta_domain_includes_root"] is True
        and tfroot["cut_only_row790_eta_not_used"] is True
        and tfnorm["actual_J_F"]==1024 and tfnorm["same_inverse_on_both_windows"] is True
        and tfnorm["below_J_F_and_independent_mean_ports_are_identity"] is True
        and kshort["complete_mean_state_used"] is True
        and kshort["old_WL_products_used_only_at_delta_zero_off_the_metric_support"] is True
        and kshort["root_point_not_replaced_by_bracket_midpoint"] is True
        and klp["root_mean_residual_set_to_zero"] is False
        and klp["all_four_moduli_equal_for_this_reference_column"] is True
        and klead["root_mean_residual_retained_in_exact_log_derivative"] is True
        and klead["second_Bi_or_other_genuine_root_column_covered"] is False
        and kroot["whole_segment_in_one_original_germ"] is True
        and kflow["reverse_orientation"]=="b<=a"
        and kflow["exact_scalar_radial_rate"]=="ell0 = -2 beta mean(u^2+K*v^2)"
        and kflow["true_radial_interval"]==["0",PARAMETERS["exact_strict_cut"]]
        and wx["scope"]["actual_H_and_common_input_only_at_original_selected_delta"] is True
        and wx["scope"]["waist_and_shorter_flow_bounds_on_whole_original_real_family"] is True
        and wxc["only_same_selected_actual_conjugacy"] is True
        and wxc["exact_order"]=="S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)"
        and wxc["inverse_order"]=="S_inverse = U_X_minus_inverse U_H"
        and wxc["selected_parameter_absolute_upper"]==PARAMETERS["fixed_selected_parameter_absolute_upper"]
        and rn["two_natural_negative_windows_certified"] is True
        and rn["uniform_real_delta_family_only"] is True
        and rn["uniform_selected_chart_family_claimed"] is False
        and rn["independent_physical_means_retained"] is True
        and rn["exact_order"]=="(Id+D_g^-1 E)^-1 D_g^-1 M^-1"
        and rn["true_Riccati_operator_norm_continuity_claimed"] is False)
    scopes={role:{path:copy.deepcopy(get_path(originals[role],path.split(".")))
            for path in role_paths} for role,role_paths in SCOPE_PATHS.items()}
    records={name:copy.deepcopy(get_path(originals[path[0]],path[1:]))
             for name,path in SCALAR_PATHS.items()}
    saved={}
    for name,record in records.items():
        if name.startswith("Knat_"):
            require(isinstance(record,str),"RNE original natural norm must stay a string")
        else:
            require(isinstance(record,dict) and set(record)=={"ball"}
                and isinstance(record["ball"],str),"original complete scalar record changed type")
        saved[name]=lower(record) if name=="eta_root_lower" else up(record)
    doc["complete_original_scope_fields_read_verbatim"]=scopes
    doc["complete_original_scope_fields_sha256"]=sha(canonical(scopes))
    doc["complete_saved_scalar_records_read_verbatim"]=records
    doc["complete_saved_scalar_records_sha256"]=sha(canonical(records))
    accepted.update(original_scope_fields_sha256=sha(canonical(scopes)),
        original_scalar_records_sha256=sha(canonical(records)),
        four_original_science_objects_not_recomputed=True,
        original_scope_fragments_are_exact_path_values_not_full_objects=True)
    doc["accepted_old_inputs"]=accepted
    doc["actual_progress"]["saved_original_scalar_records"]=len(records)
    doc["actual_progress"]["saved_original_scope_collections"]=len(scopes)
    gate(doc,8,len(records)==16 and len(scopes)==4
        and sum(isinstance(v,dict) for v in records.values())==14
        and sha(canonical(scopes))==FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256
        and sha(canonical(records))==FROZEN_SAVED_SCALAR_RECORDS_SHA256
        and accepted==EXPECTED_ACCEPTED
        and sha(canonical(accepted))==FROZEN_ACCEPTED_OLD_INPUTS_SHA256
        and all(value.is_finite() and value>0 for value in saved.values()))
    doc["complete_operator_identity_conclusion"]=copy.deepcopy(OPERATOR_IDENTITY)
    return saved

def complete_graph_shape(value,expected):
    if expected=="__FINITE_SCALAR__":
        return isinstance(value,str) and ball(value).is_finite() and ball(value).lower()>0
    if isinstance(expected,dict):
        return isinstance(value,dict) and set(value)==set(expected) and all(
            complete_graph_shape(value[key],item) for key,item in expected.items())
    if isinstance(expected,list):
        return isinstance(value,list) and len(value)==len(expected) and all(
            complete_graph_shape(v,e) for v,e in zip(value,expected))
    return type(value) is type(expected) and value==expected

def scalar_slot_count(value,expected):
    if expected=="__FINITE_SCALAR__":
        return 1
    if isinstance(expected,dict):
        return sum(scalar_slot_count(value[key],item) for key,item in expected.items())
    if isinstance(expected,list):
        return sum(scalar_slot_count(v,e) for v,e in zip(value,expected))
    return 0

def ball(value):
    if isinstance(value,dict):
        if set(value)!={"ball"}:
            raise TypeError("scalar record must be one complete original ball")
        value=value["ball"]
    return value if isinstance(value,arb) else arb(str(value))

def up(value):
    value=ball(value)
    if not value.is_finite() or value.lower()<=0:
        raise ArithmeticError("nonpositive or nonfinite new positive bound")
    return value.upper()

def lower(value):
    value=ball(value)
    if not value.is_finite() or value.lower()<=0:
        raise ArithmeticError("nonpositive or nonfinite required lower endpoint")
    return value.lower()

def rec(value):
    value=ball(value)
    if not value.is_finite() or value.lower()<=0:
        raise ArithmeticError("nonpositive or nonfinite complete scalar record")
    return value.str(75)

def complete_forward_leading(saved):
    """NIF13--16: one new positive bound, with its complete elementary factors."""
    pi_interval=arb.pi()
    two_pi_interval=2*pi_interval
    sqrt_two_pi_lower=lower(two_pi_interval.sqrt())
    inverse_sqrt_two_pi=up(1/sqrt_two_pi_lower)
    ratio=up(saved["Kr_root_upper"]/saved["eta_root_lower"])
    sixth=up(ratio**(arb(1)/6))
    radial=up(saved["saved_reverse_radial_upper"]*saved["saved_absolute_short_exp_upper"])
    density_radial=up(saved["ng_waist_upper"]*radial)
    prefactor=up(density_radial*inverse_sqrt_two_pi)
    forward=up(prefactor*sixth)
    return {
        "complete_pi_interval":rec(pi_interval),
        "complete_two_pi_interval":rec(two_pi_interval),
        "complete_sqrt_two_pi_lower":rec(sqrt_two_pi_lower),
        "complete_inverse_sqrt_two_pi_upper":rec(inverse_sqrt_two_pi),
        "complete_root_k_over_eta_upper":rec(ratio),
        "complete_root_ratio_sixth_upper":rec(sixth),
        "complete_root_to_waist_radial_upper":rec(radial),
        "complete_density_times_radial_upper":rec(density_radial),
        "complete_forward_leading_prefactor_upper":rec(prefactor),
        "complete_forward_leading_scalar_upper":rec(forward),
        "exact_formula":"ng_waist_upper * saved_reverse_radial_upper * saved_absolute_short_exp_upper * (2*pi)^(-1/2) * (Kr_root_upper/eta_root_lower)^(1/6)",
        "all_four_terminal_Ai_sign_wave_moduli_share_one_bound":True,
        "saved_absolute_short_exponential_used_in_both_directions":True,
        "positive_lower_endpoint_roles":["eta_root_lower","sqrt_two_pi_lower"],
        "old_exponential_not_recomputed":True,
        "true_waist_reverse_radial_factor_used":True,
        "root_full_coefficient_eta_lower_not_cut_only":True,
        "no_sector_sum_or_extra_sqrt2":True}

def complete_coordinate_products(saved,forward):
    """NIF17--20 on X_s_fr=S_star D_plus H_nat^s, with inherited H^s norm."""
    Kplus=up(forward["complete_forward_leading_scalar_upper"])
    windows={}
    for s,suffix in (("0","0"),("-4/3","minus4_3")):
        left_inverse=up(saved["KLambda_inverse_upper"]*saved["KF_inverse_"+suffix])
        Ni=up(left_inverse*saved["KS_inverse_"+suffix])
        left_forward=up(saved["KS_forward_"+suffix]*saved["KF_forward_"+suffix])
        Ni_inverse=up(left_forward*Kplus)
        windows[s]={
            "input_and_output_exponent":s,
            "complete_Lambda_TF_inverse_product_upper":rec(left_inverse),
            "complete_Ni_upper":rec(Ni),
            "complete_S_TF_forward_product_upper":rec(left_forward),
            "complete_Ni_inverse_upper":rec(Ni_inverse),
            "same_inverse_in_the_two_windows":True}
    return {
        "windows":windows,
        "exact_Ni_order":"Lambda_plus_delta^-1 T_F_delta^-1 S_star^-1",
        "exact_inverse_order":"S_star T_F_delta Lambda_plus_delta",
        "frozen_input_space":"X_s_fr = S_star D_plus H_nat^s",
        "original_natural_cutoff_abs_j":97,
        "actual_common_root_cutoff_abs_j":1024,
        "reflection_domain_transported_by_fixed_Dplus":True,
        "independent_mean_and_other_ports_use_identity_extension":True}

def complete_stable_inverse_products(saved,coordinate):
    """NIF22--26: read each whole RNE norm once; retain the original weight order."""
    gamma=up(arb(150545)/150544)
    windows={}
    rows=(("0","-7/6","-1/6","Knat_minus7_6"),
          ("-4/3","-5/2","-3/2","Knat_minus5_2"))
    for s,t,out_s,key in rows:
        coordinate_inverse=up(coordinate["windows"][s]["complete_Ni_inverse_upper"])
        product=up(coordinate_inverse*saved[key])
        result=up(gamma*product)
        windows[s]={
            "common_input_exponent":s,
            "natural_exponent":t,
            "stable_output_exponent":out_s,
            "complete_coordinate_times_natural_inverse_upper":rec(product),
            "complete_frozen_stable_inverse_upper":rec(result),
            "uses_same_original_natural_distributional_inverse":True}
    return {
        "exact_gamma97":"150545/150544",
        "complete_gamma97_upper":rec(gamma),
        "windows":windows,
        "exact_forward_order":"N_out^-1 S_nat_delta N_in^(7/6) Ni_delta_fr",
        "exact_inverse_order":"Ni_delta_fr^-1 N_in^(-7/6) S_nat_delta^-1 N_out",
        "old_natural_inverse_polynomials_not_recomputed":True,
        "frequency_weights_only_on_original_high_spaces":True,
        "optional_forward_Cs_constants_not_evaluated":True}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--bits",type=int,default=320)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError("refusing to overwrite an existing complete or partial scientific result")
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
        complete_original_scope_fields_read_verbatim={},complete_original_scope_fields_sha256=None,
        complete_saved_scalar_records_read_verbatim={},complete_saved_scalar_records_sha256=None,
        retained_scope=copy.deepcopy(RETAINED_SCOPE),planned_shape=copy.deepcopy(PLANNED_SHAPE),
        actual_progress=copy.deepcopy(INITIAL_ACTUAL_PROGRESS),gates=[],
        actual_mathematical_wall_seconds=0)
    began=time.monotonic()
    try:
        manifest,paths=checked_inputs(args,doc)
        doc["stage"]="complete_saved_actual_admission"
        saved=accepted_original_inputs(paths,doc)
        persist(args.out,doc)

        doc["stage"]="complete_new_forward_leading_conclusion"
        report=complete_forward_leading(saved)
        doc["complete_forward_leading_conclusion"]=report
        doc["actual_progress"]["new_forward_leading_scalar_completed"]=1
        doc["actual_progress"]["new_pi_constants_completed"]=1
        doc["actual_progress"]["new_fixed_square_roots_completed"]=1
        doc["actual_progress"]["new_positive_sixth_roots_completed"]=1
        doc["actual_progress"]["new_elementary_factor_records_completed"]=9
        gate(doc,9,complete_graph_shape(report,NEW_GRAPH_SHAPES["complete_forward_leading_conclusion"])
            and scalar_slot_count(report,NEW_GRAPH_SHAPES["complete_forward_leading_conclusion"])==10
            and report["saved_absolute_short_exponential_used_in_both_directions"] is True
            and report["true_waist_reverse_radial_factor_used"] is True)
        persist(args.out,doc)

        doc["stage"]="complete_new_coordinate_conclusion"
        report=complete_coordinate_products(saved,doc["complete_forward_leading_conclusion"])
        doc["complete_coordinate_conclusion"]=report
        doc["actual_progress"]["new_common_input_window_bounds_completed"]=4
        doc["actual_progress"]["new_elementary_factor_records_completed"]+=4
        gate(doc,10,complete_graph_shape(report,NEW_GRAPH_SHAPES["complete_coordinate_conclusion"])
            and scalar_slot_count(report,NEW_GRAPH_SHAPES["complete_coordinate_conclusion"])==8
            and set(report["windows"])=={"0","-4/3"}
            and report["reflection_domain_transported_by_fixed_Dplus"] is True)
        persist(args.out,doc)

        doc["stage"]="complete_new_frozen_stable_inverse_conclusion"
        report=complete_stable_inverse_products(saved,doc["complete_coordinate_conclusion"])
        doc["complete_frozen_stable_inverse_conclusion"]=report
        doc["actual_progress"]["new_frozen_stable_inverse_windows_completed"]=2
        doc["actual_progress"]["new_elementary_factor_records_completed"]+=3
        gate(doc,11,complete_graph_shape(report,NEW_GRAPH_SHAPES["complete_frozen_stable_inverse_conclusion"])
            and scalar_slot_count(report,NEW_GRAPH_SHAPES["complete_frozen_stable_inverse_conclusion"])==5
            and [report["windows"][s]["natural_exponent"] for s in ("0","-4/3")]==["-7/6","-5/2"]
            and [report["windows"][s]["stable_output_exponent"] for s in ("0","-4/3")]==["-1/6","-3/2"])
        persist(args.out,doc)

        doc["stage"]="complete_final_readonly_and_schema_checks"
        gate(doc,12,all(sha(paths[entry["role"]].read_bytes())==entry["sha256"] for entry in manifest["files"])
            and sha(args.manifest.read_bytes())==doc["input_manifest_sha256"]==args.manifest_sha
            and sha(canonical(doc["complete_original_scope_fields_read_verbatim"]))==FROZEN_ORIGINAL_SCOPE_FIELDS_SHA256
            and sha(canonical(doc["complete_saved_scalar_records_read_verbatim"]))==FROZEN_SAVED_SCALAR_RECORDS_SHA256
            and sha(canonical(doc["accepted_old_inputs"]))==FROZEN_ACCEPTED_OLD_INPUTS_SHA256
            and all(doc["actual_progress"][key]==0 for key in
                ("old_scientific_targets_recomputed","old_exponentials_reevaluated",
                 "old_logarithms_reevaluated","old_R97_RNE_graphs_or_comparisons_recomputed",
                 "historical_inputs_restored")))
        gate(doc,13,all(complete_graph_shape(doc[key],value) for key,value in NEW_GRAPH_SHAPES.items())
            and [scalar_slot_count(doc[key],value) for key,value in NEW_GRAPH_SHAPES.items()]==[10,8,5]
            and doc["complete_operator_identity_conclusion"]==OPERATOR_IDENTITY)
        gate(doc,14,doc["planned_shape"]==PLANNED_SHAPE
            and doc["actual_progress"]==SUCCESS_ACTUAL_PROGRESS
            and sum(doc["actual_progress"][key] for key in
                ("new_forward_leading_scalar_completed","new_common_input_window_bounds_completed",
                 "new_frozen_stable_inverse_windows_completed"))==7
            and doc["actual_progress"]["new_elementary_factor_records_completed"]==16)
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-began
        gate(doc,15,set(doc)==set(COMPLETE_FIELDS) and len(doc)==32
            and doc["retained_scope"]==RETAINED_SCOPE
            and len(doc["gates"])==15
            and [entry["name"] for entry in doc["gates"]]==GATE_NAMES[:15]
            and all(entry["passed"] is True for entry in doc["gates"])
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
            "old_targets_not_recomputed":True,
            "old_exponentials_and_logarithms_not_recomputed":True,
            "old_R97_RNE_graphs_and_comparisons_not_recomputed":True,
            "new_frozen_coordinate_or_stable_inverse_conclusion_authorized":False}
        persist(args.out,doc)
        print_complete_document(doc)
        raise
    raw=persist(args.out,doc)
    print_complete_document(doc)
    if len(raw)>COMPLETE_SCIENCE_MAX_BYTES:
        raise ValueError("complete scientific result saved and printed; publication byte budget exceeded")

if __name__=="__main__":
    main()
