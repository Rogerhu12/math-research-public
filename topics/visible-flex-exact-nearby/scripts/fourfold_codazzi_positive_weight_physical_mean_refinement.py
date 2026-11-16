"""WMR: complete positive-weight physical mean and same-operator error refinement."""
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
KIND = json.loads(r'''"complete_positive_weight_physical_mean_and_whole_error_refinement"''')
PROBLEM_ID = json.loads(r'''"same_selected_original97_physical_mean_positive_weight_refinement_v1"''')
TOPIC = json.loads(r'''"topics/visible-flex-exact-nearby"''')
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_positive_weight_physical_mean_refinement.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py"''')
PREFLIGHT_KIND = json.loads(r'''"complete_positive_weight_physical_mean_and_whole_error_refinement_readonly_preflight"''')
PARAMETERS = json.loads(r'''{"arithmetic_bits":320,"copied_original_records":69,"decimal_record_digits":75,"first_absolute_mode":97,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","history_inputs":0,"local_positive_weight_gap":"3/4","local_rational_U":"1","local_unweighted_excess":"0","mean_source_decay":"n^(-23/6)","minimum_physical_frequency":388,"new_exponentials":2,"new_graphs":7,"new_record_count":42,"old_complete_graphs":13,"old_indices":2,"old_scientific_calls":0,"old_target_recomputations":0,"original_PW_cut":"2333968743003/10000000000000","original_real_delta_qualification":"1/100000000; selected result not relabelled uniform","original_true_interfaces":3070,"physical_frequency":"n=4|j|","physical_mean_coordinates":2,"root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"strict_cut":"76285779072683/320000000000000","strict_positive_weight_gap":"79/128","strict_rational_U":"7/4","strict_unweighted_excess":"33/16"}''')
RETAINED_SCOPE = json.loads(r'''{"WGS_geometry_amplitude_sup_not_A0":true,"all_original_one_sided_intervals_and_3070_interfaces_retained":true,"both_characteristic_branches_and_reflection_retained":true,"exact_root_finite_factor_and_full_WCF_FJ_two_ranks_rho_i_ell2_retained":true,"final_surface_proved":false,"finite_Schur_inverse_proved":false,"full_Jr_beta_r_e_kappa_and_R0_retained":true,"full_incoming_inverse_proved":false,"full_nonlinear_background_proved":false,"nu_Schur_and_infinite_radial_head_retained":true,"old_whole_mathematics_success_and_formatter_failure_retained":true,"original_physical_mean_root_initial_value_retained":true,"original_producers_not_imported":true,"original_weighted_and_unweighted_averages_distinct":true,"passing_high_cutoff_proved":false,"physical_two_means_and_mean_feedback_retained":true,"positive_weight_gap_is_pointwise":true,"same_fixed_intrinsic_eta0":true,"same_selected_real_member_only":true,"strict_d_A0_has_independent_original_product_primitive_proof":true,"true_physical_96_columns_and_all_Theta_cross_blocks_retained":true,"whole_Calg_not_replaced_by_D_infinity":true,"whole_and_reduced_compared_only_with_same_original_operator":true,"whole_bounds_not_subtracted":true}''')
SCI_FIELDS = json.loads(r'''["kind","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","copied_original_scalar_records","copied_original_scopes","complete_new_graphs","whole_candidate_choices","current_target","saved_record_counts","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized","problem_id","completed_targets"]''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","current_input_and_AST_identity","complete_original_files_byte_identical","first_attempt_complete_prefix_with_failure_status_preserved","remaining_only_original_success_verified","all_thirteen_original_graph_bindings_verified","complete_original_records_and_scopes_retained","true_lower_endpoints_and_local_rational_qualification","complete_strict_positive_weight_coefficients","complete_local_positive_weight_coefficients","complete_two_patch_backward_mean","complete_affine_mean_sources","complete_negative_receiver","complete_waist_endpoint","complete_whole_and_reduced","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_affine_mean_sources":{"complete":true,"exact_identity":"g1 = J Q f - z_r k - z ((D0-E)k+b1)","full_kr_beta_r_Jr_and_R0_retained":true,"kind":"complete_WMR_affine_mean_sources_v1","new_records":{"complete_local_primitive_mean_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_local_raw_mean_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_primitive_mean_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_raw_mean_source_upper":{"ball":"__FINITE_SCALAR__"}},"same_actual_trial_and_complete_true_jumps":true},"complete_negative_receiver":{"complete":true,"complete_source_input_window":"H^(-4/3)","kind":"complete_WMR_negative_receiver_v1","new_records":{"complete_collar_ordinary_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_raw_mean_union_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_received_with_jumps_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_negative_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_ordinary_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_received_with_jumps_upper":{"ball":"__FINITE_SCALAR__"}},"ordinary_dr_and_impulse_units_retained":true,"original_B_T_profiles_N6_jumps_and_powers_read_only":true,"same_original_PW_cut_and_complete_receivers":true},"complete_waist_endpoint":{"complete":true,"complete_physical_two_mean_vector_retained":true,"kind":"complete_WMR_same_waist_endpoint_v1","new_records":{"complete_physical_mean_endpoint_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_waist_endpoint_upper":{"ball":"__FINITE_SCALAR__"}},"original_ng_already_paid_once":true,"original_three_nonmean_endpoints_read_only":true,"same_old_trial_four_endpoint_sum":true},"complete_whole_and_reduced":{"complete":true,"kind":"complete_WMR_whole_and_reduced_v1","new_records":{"complete_all_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonroot_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_reduced_received_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_reduced_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_whole_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_whole_received_source_upper":{"ball":"__FINITE_SCALAR__"}},"original_ordered_readout_read_only":true,"root_and_coefficient_finite_factors_retained":true,"same_selected_Xfr_to_normalized_reflected_waist_map":true,"whole_and_reduced_are_distinct_operators":true},"local_positive_weight_coefficients":{"common_angular_weight_cancelled_before_bounds":true,"complete":true,"kind":"complete_WMR_positive_weight_coefficients_v1","metric_beta_nonnegative_on_actual_negative_interval":true,"new_records":{"complete_Tk_upper":{"ball":"__FINITE_SCALAR__"},"complete_absolute_feedback_upper":{"ball":"__FINITE_SCALAR__"},"complete_absolute_mean_coefficient_upper":{"ball":"__FINITE_SCALAR__"},"complete_backward_mean_coefficient_upper":{"ball":"__FINITE_SCALAR__"},"complete_cross_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_curvature_cross_upper":{"ball":"__FINITE_SCALAR__"},"complete_drift_cross_upper":{"ball":"__FINITE_SCALAR__"},"complete_feedback_quotient_absolute_upper":{"ball":"__FINITE_SCALAR__"},"complete_feedback_quotient_negative_part_upper":{"ball":"__FINITE_SCALAR__"}},"original_unweighted_and_positive_weighted_averages_not_identified":true,"patch":"local","pointwise_v_sign_assumed":false},"strict_positive_weight_coefficients":{"common_angular_weight_cancelled_before_bounds":true,"complete":true,"kind":"complete_WMR_positive_weight_coefficients_v1","metric_beta_nonnegative_on_actual_negative_interval":true,"new_records":{"complete_Tk_upper":{"ball":"__FINITE_SCALAR__"},"complete_absolute_feedback_upper":{"ball":"__FINITE_SCALAR__"},"complete_absolute_mean_coefficient_upper":{"ball":"__FINITE_SCALAR__"},"complete_backward_mean_coefficient_upper":{"ball":"__FINITE_SCALAR__"},"complete_cross_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_curvature_cross_upper":{"ball":"__FINITE_SCALAR__"},"complete_drift_cross_upper":{"ball":"__FINITE_SCALAR__"},"complete_feedback_quotient_absolute_upper":{"ball":"__FINITE_SCALAR__"},"complete_feedback_quotient_negative_part_upper":{"ball":"__FINITE_SCALAR__"}},"original_unweighted_and_positive_weighted_averages_not_identified":true,"patch":"strict","pointwise_v_sign_assumed":false},"two_patch_backward_mean":{"coefficient_decay":"n^(-23/6)","complete":true,"kind":"complete_WMR_two_patch_backward_mean_v1","local_then_strict_backward_order":true,"new_records":{"complete_local_backward_factor_upper":{"ball":"__FINITE_SCALAR__"},"complete_local_mean_derivative_upper":{"ball":"__FINITE_SCALAR__"},"complete_local_mean_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_backward_factor_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_mean_derivative_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_mean_upper":{"ball":"__FINITE_SCALAR__"}},"ordinary_dr_lengths":true,"root_mean_value":"0","same_physical_mean":true}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_affine_mean_sources":4,"complete_negative_receiver":6,"complete_waist_endpoint":2,"complete_whole_and_reduced":6,"local_positive_weight_coefficients":9,"strict_positive_weight_coefficients":9,"two_patch_backward_mean":6}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["strict_positive_weight_coefficients","local_positive_weight_coefficients","two_patch_backward_mean","complete_affine_mean_sources","complete_negative_receiver","complete_waist_endpoint","complete_whole_and_reduced"]''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_graphs_admitted":0,"complete_original_indices_admitted":0,"local_rational_qualifications_completed":0,"new_exponentials_saved":0,"new_graphs_completed":0,"new_logarithms":0,"new_powers":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_record_objects_copied":0}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_graphs_admitted":13,"complete_original_indices_admitted":2,"local_rational_qualifications_completed":3,"new_exponentials_saved":2,"new_graphs_completed":7,"new_logarithms":0,"new_powers":0,"new_quadratures":0,"new_records_saved":42,"new_square_roots":0,"new_whole_comparisons_completed":2,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_record_objects_copied":69}''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":13787,"git_blob_sha":"32047b9222bf5c17c9818faa5ba112ce47062e75","original_index_role":null,"path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/index.json","role":"prior_prefix_index","sha256":"6fe44d8cf0d352d2216fa06ea524118e95e2c56954bd277456c804f5dccfc091"},{"bytes":11261,"git_blob_sha":"04c0ca05306058a7b031912740a5801b8d37c267","original_index_role":null,"path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_completion_ci/run-43831678361-1/index.json","role":"prior_completion_index","sha256":"8a1d8315fa9400c291edb8afa9d4ba2f6c1a7e5096e8e55feab51e4020253459"},{"bytes":15788,"git_blob_sha":"43482134ed758ba90c331cc598d8e04377009a24","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/physical_coefficients_strict.json","role":"physical_coefficients_strict","sha256":"58d527567281fc3fcdefc4b70884f46e2e64a6cbc58b13fa9431bc4e03bdc6dc"},{"bytes":15904,"git_blob_sha":"8e04fca88d61b2f38152302cac8527ab8326d5df","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/physical_coefficients_local.json","role":"physical_coefficients_local","sha256":"ee16b343c4dff938c0d56ce29f906b55a4fff250ff68c98c49e47d138b4c614a"},{"bytes":5471,"git_blob_sha":"f6faddfa43ccb00617327e3740f922bc59ce382b","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/same_angular_J_strict.json","role":"same_angular_J_strict","sha256":"a904a3df4e4d750327618c126362424c8bb8bda42a8fd09344c7742a5631d127"},{"bytes":5048,"git_blob_sha":"37864cba216c25f951f4b98cf16192fd4100cc4b","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/same_angular_J_local.json","role":"same_angular_J_local","sha256":"484350c39e3dd0591dfb62412f044f90d957065d7a7cb2e3c51dc2a240e954c1"},{"bytes":8083,"git_blob_sha":"4bff00acace27f4d649354fcb88e8b292fbd24db","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/mean_kernel_strict.json","role":"mean_kernel_strict","sha256":"f62aa75b1069004b67c1195ede586b4cad25f8198687c43ee33626e26735658f"},{"bytes":8081,"git_blob_sha":"ff77ae845a0a31a66cb7d3634c6db0c343cbde29","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/mean_kernel_local.json","role":"mean_kernel_local","sha256":"5d0651e87d62fbe14bd351b648ddacba3f590ed7506c68b90d0e7f2f324be3a3"},{"bytes":28403,"git_blob_sha":"7ba8a5f33624148475fae9752ac28f121f00d718","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/mean_N6_strict.json","role":"mean_N6_strict","sha256":"82302654a5a87c15e6d0155e368ebd25c12605819b716fcaf1348e599a31bdfc"},{"bytes":27359,"git_blob_sha":"16f608b4331774ca51b75c2a98a360d869344092","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/mean_N6_local.json","role":"mean_N6_local","sha256":"ac5222bb6d2a9a2e25a01e9cd8bd7f3b2535a9f8773ca6c1f688110bb58d672b"},{"bytes":5897,"git_blob_sha":"d7a106f0d3372ea5d2b02b84ca60cbe549ddedc3","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/true_jumps.json","role":"true_jumps","sha256":"1e2272cb7d1071f87a9ed6f7153ed994153351c15cdd81f6859ac9ba1fb61bbd"},{"bytes":8811,"git_blob_sha":"584cf91584915adc481ab2766d4b1be884bed9da","original_index_role":"prior_prefix_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/negative_reception.json","role":"negative_reception","sha256":"5d8284aa02ca278dbcb492bfdc1a7825fe7c56518ddac9de989128d8cdc8def1"},{"bytes":14394,"git_blob_sha":"d2aa61e0dc1502181a9e86549e81311e8fdacdaf","original_index_role":"prior_completion_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_free_waist_Airy_and_Schur_map.json","role":"free","sha256":"5f48bdc934047c86ed2fd2d79cb94c593c619cffefb3ac52510fd3c4bfe4b413"},{"bytes":7974,"git_blob_sha":"13b5b9809e2ba649511613eb5e58ef78f51908dd","original_index_role":"prior_completion_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_four_waist_endpoint_contributions.json","role":"endpoint","sha256":"7fbee7f580c01944e585f5a763ce5a87717db8c8f59ea789b48f850fe6a75df3"},{"bytes":9098,"git_blob_sha":"2f46123a6c4d54676b2c82ac205ca1060b6df97e","original_index_role":"prior_completion_index","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_completion_ci/run-43831678361-1/graphs/complete_same_physical_whole_and_reduced_error.json","role":"whole","sha256":"6e9267dccb21d9d1421608a5f0f2e7c0ee77630660eac272ee3923ef2b8319d0"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":31643,"git_blob_sha":"a7b23dea9a96dfab74475d382ca2d1df8edd5b8e","path":"topics/visible-flex-exact-nearby/results/R133-supplement-positive-weight-physical-mean-propagation-and-complete-error-reassembly.md","role":"proof_WMR","sha256":"550866c05d9a07d3e4b037e5840a4f75b66a7f3a9304c5cd0d52e4f2b7e729a6"}''')
RECORD_SPECS = json.loads(r'''{"Bessel_prefactor":{"endpoint":"upper","path":["conclusion","complete_input_Bessel_prefactor_upper"],"role":"negative_reception","use":"arithmetic"},"C_1":{"endpoint":"upper","path":["conclusion","copied_complete_original_receiver_records","C_1"],"role":"negative_reception","use":"arithmetic"},"C_O":{"endpoint":"upper","path":["conclusion","copied_complete_original_receiver_records","C_O"],"role":"negative_reception","use":"arithmetic"},"C_R":{"endpoint":"upper","path":["conclusion","copied_complete_original_receiver_records","C_R"],"role":"negative_reception","use":"arithmetic"},"Calg":{"endpoint":"upper","path":["conclusion","complete_original_records","Calg"],"role":"whole","use":"arithmetic"},"D_infinity":{"endpoint":"upper","path":["conclusion","complete_original_records","D_infinity"],"role":"whole","use":"arithmetic"},"KHinv_L2":{"endpoint":"upper","path":["conclusion","complete_original_records","KHinv_L2"],"role":"whole","use":"retained_ordered_readout_factors"},"Lrec":{"endpoint":"upper","path":["conclusion","complete_new_records","complete_left_readout_times_right_input_upper"],"role":"whole","use":"arithmetic"},"N_minus1_2_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","N_minus1_2_upper"],"role":"negative_reception","use":"arithmetic"},"N_minus4_3_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","N_minus4_3_upper"],"role":"negative_reception","use":"arithmetic"},"N_minus5_3_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","N_minus5_3_upper"],"role":"negative_reception","use":"arithmetic"},"N_minus5_6_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","N_minus5_6_upper"],"role":"negative_reception","use":"arithmetic"},"Ni_Hminus4_3":{"endpoint":"upper","path":["conclusion","complete_original_records","Ni_Hminus4_3"],"role":"whole","use":"retained_ordered_readout_factors"},"RF":{"endpoint":"upper","path":["conclusion","complete_original_records","RF"],"role":"whole","use":"arithmetic"},"Rplus":{"endpoint":"upper","path":["conclusion","complete_original_records","Rplus"],"role":"whole","use":"arithmetic"},"Xi23_6":{"endpoint":"upper","path":["conclusion","complete_tail_weights","new_complete_records","complete_Xi23_6_upper"],"role":"free","use":"arithmetic"},"collar_B_union":{"endpoint":"upper","path":["conclusion","complete_collar_patch_union_records","complete_collar_B_union_upper"],"role":"negative_reception","use":"arithmetic"},"collar_T_union":{"endpoint":"upper","path":["conclusion","complete_collar_patch_union_records","complete_collar_T_union_upper"],"role":"negative_reception","use":"arithmetic"},"dyadic_one_third":{"endpoint":"upper","path":["conclusion","complete_input_dyadic_square_sum_records","one_third"],"role":"negative_reception","use":"arithmetic"},"dyadic_two_thirds":{"endpoint":"upper","path":["conclusion","complete_input_dyadic_square_sum_records","two_thirds"],"role":"negative_reception","use":"arithmetic"},"ell_minus_negative_fourth_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","ell_minus_negative_fourth_upper"],"role":"negative_reception","use":"arithmetic"},"ell_plus_one_fourth_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","ell_plus_one_fourth_upper"],"role":"negative_reception","use":"arithmetic"},"endpoint_Vz":{"endpoint":"upper","path":["conclusion","complete_new_constants","complete_physical_mean_endpoint_vector_upper"],"role":"endpoint","use":"arithmetic"},"endpoint_WT":{"endpoint":"upper","path":["conclusion","complete_four_endpoint_records","complete_old_waist_normalizer_endpoint_upper"],"role":"endpoint","use":"arithmetic"},"endpoint_scattering":{"endpoint":"upper","path":["conclusion","complete_four_endpoint_records","complete_scattering_endpoint_upper"],"role":"endpoint","use":"arithmetic"},"endpoint_second_order":{"endpoint":"upper","path":["conclusion","complete_four_endpoint_records","complete_second_order_endpoint_upper"],"role":"endpoint","use":"arithmetic"},"jump_collar":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_collar_jump_sum_upper"],"role":"true_jumps","use":"arithmetic"},"jump_strict":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_strict_jump_sum_upper"],"role":"true_jumps","use":"arithmetic"},"local_B_c":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","local","B_c_upper"],"role":"negative_reception","use":"retained_complete_nonmean"},"local_B_t":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","local","B_t_upper"],"role":"negative_reception","use":"retained_complete_nonmean"},"local_CF":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_reflected_mean_source_upper"],"role":"mean_N6_local","use":"arithmetic"},"local_E0":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_E_L2_upper"],"role":"mean_kernel_local","use":"arithmetic"},"local_Ik":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_I_k_L2_upper"],"role":"mean_kernel_local","use":"arithmetic"},"local_Kabs":{"endpoint":"upper","path":["conclusion","complete_A0_jets","K","group_upper",0],"role":"physical_coefficients_local","use":"arithmetic"},"local_T_c":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","local","T_c_upper"],"role":"negative_reception","use":"retained_complete_nonmean"},"local_T_t":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","local","T_t_upper"],"role":"negative_reception","use":"retained_complete_nonmean"},"local_V":{"endpoint":"upper","path":["conclusion","complete_A0_jets","V","group_upper",0],"role":"physical_coefficients_local","use":"arithmetic"},"local_b1":{"endpoint":"upper","path":["conclusion","complete_A0_jets","b1","group_upper",0],"role":"physical_coefficients_local","use":"arithmetic"},"local_base":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_mean_base_upper"],"role":"mean_kernel_local","use":"arithmetic"},"local_beta":{"endpoint":"upper","path":["conclusion","complete_A0_jets","beta","group_upper",0],"role":"physical_coefficients_local","use":"arithmetic"},"local_drift":{"endpoint":"upper","path":["conclusion","complete_A0_jets","d","group_upper",0],"role":"physical_coefficients_local","use":"arithmetic"},"local_eta_lower":{"endpoint":"lower","path":["conclusion","new_complete_records","same_eta_positive_lower"],"role":"same_angular_J_local","use":"arithmetic"},"local_k0":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_k_L2_upper"],"role":"mean_kernel_local","use":"arithmetic"},"local_kphi":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_k_phi_L2_upper"],"role":"mean_kernel_local","use":"arithmetic"},"local_kr":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_k_r_L2_upper"],"role":"mean_kernel_local","use":"arithmetic"},"prior_reduced":{"endpoint":"upper","path":["conclusion","complete_new_records","complete_infinite_error_after_exact_finite_factors_upper"],"role":"whole","use":"arithmetic"},"prior_whole":{"endpoint":"upper","path":["conclusion","complete_new_records","complete_same_physical_whole_error_upper"],"role":"whole","use":"arithmetic"},"qualification_local_Iv":{"endpoint":"upper","path":["conclusion","complete_A0_jets","I_v","group_upper",0],"role":"physical_coefficients_local","use":"qualification"},"qualification_local_U":{"endpoint":"upper","path":["conclusion","complete_A0_jets","U","group_upper",0],"role":"physical_coefficients_local","use":"qualification"},"qualification_local_alpha":{"endpoint":"upper","path":["conclusion","new_complete_records","alpha_absolute_upper"],"role":"same_angular_J_local","use":"qualification"},"sqrt_ell_plus_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","sqrt_ell_plus_upper"],"role":"negative_reception","use":"arithmetic"},"sqrt_two_upper":{"endpoint":"upper","path":["conclusion","complete_power_and_radial_measure_records","sqrt_two_upper"],"role":"negative_reception","use":"arithmetic"},"strict_B_c":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","strict","B_c_upper"],"role":"negative_reception","use":"retained_complete_nonmean"},"strict_B_t":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","strict","B_t_upper"],"role":"negative_reception","use":"arithmetic"},"strict_CF":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_reflected_mean_source_upper"],"role":"mean_N6_strict","use":"arithmetic"},"strict_E0":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_E_L2_upper"],"role":"mean_kernel_strict","use":"arithmetic"},"strict_Ik":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_I_k_L2_upper"],"role":"mean_kernel_strict","use":"arithmetic"},"strict_Kabs":{"endpoint":"upper","path":["conclusion","complete_A0_jets","K","group_upper",0],"role":"physical_coefficients_strict","use":"arithmetic"},"strict_T_c":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","strict","T_c_upper"],"role":"negative_reception","use":"retained_complete_nonmean"},"strict_T_t":{"endpoint":"upper","path":["conclusion","complete_patch_B_T_M_records","strict","T_t_upper"],"role":"negative_reception","use":"arithmetic"},"strict_V":{"endpoint":"upper","path":["conclusion","complete_A0_jets","V","group_upper",0],"role":"physical_coefficients_strict","use":"arithmetic"},"strict_b1":{"endpoint":"upper","path":["conclusion","complete_A0_jets","b1","group_upper",0],"role":"physical_coefficients_strict","use":"arithmetic"},"strict_base":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_mean_base_upper"],"role":"mean_kernel_strict","use":"arithmetic"},"strict_beta":{"endpoint":"upper","path":["conclusion","complete_A0_jets","beta","group_upper",0],"role":"physical_coefficients_strict","use":"arithmetic"},"strict_drift":{"endpoint":"upper","path":["conclusion","complete_A0_jets","d","group_upper",0],"role":"physical_coefficients_strict","use":"arithmetic"},"strict_eta_lower":{"endpoint":"lower","path":["conclusion","new_complete_records","same_eta_positive_lower"],"role":"same_angular_J_strict","use":"arithmetic"},"strict_k0":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_k_L2_upper"],"role":"mean_kernel_strict","use":"arithmetic"},"strict_kphi":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_k_phi_L2_upper"],"role":"mean_kernel_strict","use":"arithmetic"},"strict_kr":{"endpoint":"upper","path":["conclusion","new_complete_records","complete_k_r_L2_upper"],"role":"mean_kernel_strict","use":"arithmetic"}}''')
ORIGINAL_RECORD_BYTES = json.loads(r'''8161''')
ORIGINAL_RECORD_SHA = json.loads(r'''"53bb5d205aeb6ca54b773deb0b2653dadfbc1f2455970b800952847512bd6207"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''20489''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"9ef5639d34b98ae02d341dd53026f03bb20efe67caacab812699b7e7f69e333b"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''4623''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"38344c686485fb0e8940ff7e03d8e4fc1c8d3397c4cfbb3ff73e1fd17d525cfb"''')
ORIGINAL_ENVELOPE_FIELDS = json.loads(r'''["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"]''')
ORIGINAL_BINDING_FIELDS = json.loads(r'''["direct_dependency_receipts","mathematical_input_sha256","parameters_sha256","problem_id","scientific_module_sha256"]''')
MAX_SCIENCE_BYTES = json.loads(r'''62000''')

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

_ORIGINAL_BALL_LEAF = object()

def original_qualifications(value):
    """Retain every non-ball leaf, including fields inside mixed containers."""
    if isinstance(value, dict):
        result = {}
        for key, child in value.items():
            if key == "ball" and isinstance(child, str):
                continue
            saved = original_qualifications(child)
            if saved is not _ORIGINAL_BALL_LEAF:
                result[key] = saved
        return _ORIGINAL_BALL_LEAF if value and not result else result
    if isinstance(value, list):
        result = [original_qualifications(child) for child in value]
        if value and all(child is _ORIGINAL_BALL_LEAF for child in result):
            return _ORIGINAL_BALL_LEAF
        return [None if child is _ORIGINAL_BALL_LEAF else child for child in result]
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

def index_summary(role, doc, spec):
    result = {"file": spec["path"], "bytes": spec["bytes"],
              "sha256": spec["sha256"], "blob_sha": spec["git_blob_sha"]}
    for key in ("kind", "complete", "proved", "stage", "actual_returncode",
                "failure", "run_id", "run_attempt", "workflow_event_commit",
                "actual_scientific_checkout_commit", "runtime", "source_sha256",
                "input_manifest_sha256", "parameters_sha256",
                "scientific_module_sha256"):
        result[key] = copy.deepcopy(doc[key])
    result["complete_mathematical_input_map_count"] = len(doc["mathematical_input_sha256"])
    result["complete_mathematical_input_map_sha256"] = digest(
        canonical(doc["mathematical_input_sha256"]))
    result["complete_gates_count"] = len(doc["gates"])
    result["complete_gates_sha256"] = digest(canonical(doc["gates"]))
    result["complete_node_receipts_count"] = len(doc["node_receipts"])
    result["complete_node_receipts_sha256"] = digest(canonical(doc["node_receipts"]))
    result["complete_retained_scope_sha256"] = digest(canonical(doc["retained_scope"]))
    return result

def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(digest(manifest_raw) == manifest_sha, "manifest CLI identity")
    manifest = exact_json(manifest_raw)
    require(isinstance(manifest["files"], list)
            and len(manifest["files"]) == 19, "nineteen complete current inputs")
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_WMR", "science", "worker", "rules"]
    require([p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 19,
            "fixed current-input role order and paths")
    files = {p["role"]: p for p in specs}
    for expected in EXPECTED_OLD_FILES:
        require(same_json(files[expected["role"]], five_fields(expected)),
                "original current input pin differs")
    require(same_json(files["proof_WMR"], EXPECTED_PROOF), "published WMR pin")
    require(files["science"]["path"] == SOURCE_PATH
            and files["worker"]["path"] == WORKER_PATH, "new entry paths")
    raw = {p["role"]: check_file(root, p) for p in specs}
    require(Path(__file__).resolve() == safe_path(root, SOURCE_PATH)
            and Path(__file__).read_bytes() == raw["science"], "actual entry bytes")
    require(same_json(manifest["scientific_modules"], [files["science"]]),
            "one new mathematical module")
    module_map = {"science": files["science"]["sha256"]}
    op = manifest["operation"]
    require(op["kind"] == KIND and op["problem_id"] == PROBLEM_ID
            and same_json(op["parameters"], PARAMETERS)
            and same_json(op["ordered_targets"], ORDERED_GRAPH_NAMES)
            and same_json(op["scientific_module_binding"], module_map),
            "operation profile differs")
    for role in ("science", "worker"):
        ast.parse(raw[role].decode("utf-8"), filename=files[role]["path"])
    docs = {p["role"]: exact_json(raw[p["role"]]) for p in EXPECTED_OLD_FILES}
    for p in EXPECTED_OLD_FILES:
        require(canonical(docs[p["role"]]) == raw[p["role"]],
                "complete original JSON spelling differs")
    first = docs["prior_prefix_index"]
    last = docs["prior_completion_index"]
    require(first["kind"] == "complete_global_genuine_waist_error_posterior_v1"
            and first["run_id"] == "43827705714" and first["run_attempt"] == "1"
            and first["complete"] is False and first["proved"] is False
            and first["actual_returncode"] == 1
            and first["stage"] == "preserved_failure"
            and len(first["node_receipts"]) == 23 and len(first["gates"]) == 27,
            "original failed attempt and its complete prefix")
    require(last["kind"] == "complete_remaining_WEJ_posterior_v1"
            and last["run_id"] == "43831678361" and last["run_attempt"] == "1"
            and last["complete"] is True and last["proved"] is True
            and last["actual_returncode"] == 0 and last["failure"] is None
            and last["stage"] == "complete" and len(last["node_receipts"]) == 3
            and len(last["gates"]) == 9, "original completed continuation")
    for ix in (first, last):
        require(all(set(g) == {"name", "passed"} and g["passed"] is True
                    for g in ix["gates"]), "original complete gate list")
        require(ix["old_scientific_calls"] == 0
                and ix["old_binary_parts_restored"] == 0,
                "original no-recomputation status")
    require(last["mathematical_input_sha256"]["prior_index"]
            == files["prior_prefix_index"]["sha256"], "continuation binds first index")
    complete_receipts = {}
    for ix in (first, last):
        for item in ix["node_receipts"]:
            require(item["node_name"] not in complete_receipts, "duplicate old node")
            complete_receipts[item["node_name"]] = {
                key: item[key] for key in ("file", "bytes", "sha256")}
    qualification = {}
    graph_roles = {}
    for p in EXPECTED_OLD_FILES:
        role = p["role"]
        if p["original_index_role"] is None:
            continue
        graph_roles[role] = p["original_index_role"]
        doc = docs[role]
        ix = docs[p["original_index_role"]]
        require(set(doc) == set(ORIGINAL_ENVELOPE_FIELDS)
                and doc["kind"] == "WEJ_complete_atomic_node_v1"
                and doc["complete"] is True and doc["failure"] is None
                and doc["all_printed_records_in_complete_conclusion"] is True
                and doc["automatic_retry_authorized"] is False
                and type(doc["printed_record_event_count"]) is int,
                "complete original scientific envelope")
        b = doc["binding"]
        require(set(b) == set(ORIGINAL_BINDING_FIELDS)
                and same_json(b["mathematical_input_sha256"],
                              ix["mathematical_input_sha256"])
                and same_json(b["scientific_module_sha256"],
                              ix["scientific_module_sha256"])
                and b["parameters_sha256"] == ix["parameters_sha256"]
                and b["problem_id"].endswith("/" + doc["node_name"]),
                "original full scientific binding")
        item = next((x for x in ix["node_receipts"]
                     if x["node_name"] == doc["node_name"]), None)
        require(item is not None and item["bytes"] == p["bytes"]
                and item["sha256"] == p["sha256"]
                and p["path"].endswith("/" + item["file"]),
                "original index receipt")
        for dependency, receipt in b["direct_dependency_receipts"].items():
            require(dependency in complete_receipts
                    and same_json(receipt, complete_receipts[dependency]),
                    "complete direct dependency receipt")
        qualification[role] = original_qualifications(doc["conclusion"])
        require(isinstance(qualification[role], dict),
                "complete recursive original qualification projection")
    added = {k: copy.deepcopy(v) for k, v in last["parameters"].items()
             if k not in first["parameters"]}
    require(same_json({**first["parameters"], **added}, last["parameters"])
            and same_json(first["retained_scope"], last["retained_scope"]),
            "same original parameters and retained scopes")
    scopes = {"complete_original_parameters": copy.deepcopy(first["parameters"]),
              "complete_continuation_additional_parameters": added,
              "complete_original_retained_scope": copy.deepcopy(first["retained_scope"]),
              "complete_original_node_qualifications": qualification}
    records = {}
    for alias, spec in RECORD_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(isinstance(value, dict) and set(value) == {"ball"}
                and isinstance(value["ball"], str), "unaltered complete old record")
        records[alias] = copy.deepcopy(value)
    require(len(records) == 69
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all sixty-nine original records")
    require(len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "all complete original scopes and qualifications")
    accepted = {
        "original_index_admission": {
            r: index_summary(r, docs[r], files[r])
            for r in ("prior_prefix_index", "prior_completion_index")},
        "complete_graph_original_index_roles": graph_roles,
        "all_thirteen_complete_graph_bindings_and_dependencies_verified": True,
        "failed_first_attempt_not_relabelled_success": True,
        "complete_continuation_original_records_only": True,
        "complete_original_indices_read_and_byte_verified": True,
        "full_original_index_bodies_remain_at_their_pinned_paths": True,
        "original_parameters_and_scopes_losslessly_reconstructed": True}
    require(len(canonical(accepted)) == ORIGINAL_ACCEPTED_BYTES
            and digest(canonical(accepted)) == ORIGINAL_ACCEPTED_SHA,
            "complete original admission projection")
    verified = {role: {k: files[role][k] for k in ("bytes", "sha256")}
                for role in expected_roles[:16]}
    return {"manifest": manifest, "files": files, "records": records,
            "scopes": scopes, "accepted": accepted, "verified": verified,
            "module_map": module_map, "raw": raw, "root": root}

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

def complete_weight_coefficients(saved, patch, emit):
    require(patch in ("strict", "local"), "physical patch")
    old = lambda key: saved_upper(saved[patch + "_" + key])
    eta = saved_positive_lower(saved[patch + "_eta_lower"])
    U = rational(PARAMETERS[patch + "_rational_U"])
    gap = rational(PARAMETERS[patch + "_positive_weight_gap"])
    excess = rational(PARAMETERS[patch + "_unweighted_excess"])
    # M=V is a same-patch bound for the complete physical mean of v.
    curvature = emit("complete_curvature_cross_upper",
                     old("V") * old("Kabs") * old("V"))
    drift = emit("complete_drift_cross_upper",
                 old("V") * U * old("drift") / eta)
    cross = emit("complete_cross_sum_upper",
                 saved_upper(curvature) + saved_upper(drift))
    quotient = emit("complete_feedback_quotient_absolute_upper",
                    (U * U + saved_upper(cross)) / gap)
    negative = emit("complete_feedback_quotient_negative_part_upper",
                    saved_upper(cross) / gap)
    feedback = emit("complete_absolute_feedback_upper",
                    2 * old("beta") * saved_upper(quotient))
    emit("complete_absolute_mean_coefficient_upper",
         old("base") + saved_upper(feedback))
    emit("complete_backward_mean_coefficient_upper",
         old("beta") * (excess + 2 * saved_upper(negative)))
    emit("complete_Tk_upper",
         old("kr") + old("drift") * old("kphi")
         + old("E0") * old("k0") + old("b1"))

def new_record(graphs, graph, key):
    require(graphs[graph]["complete"] is True, "predecessor graph incomplete")
    return graphs[graph]["new_records"][key]

def complete_backward_mean(saved, graphs, emit):
    # These are exact rational physical endpoints. Subtraction occurs before
    # the outward endpoint, never between old norm upper bounds.
    strict_length = norm_upper(rational(PARAMETERS["strict_cut"]))
    local_length = norm_upper(rational(PARAMETERS["root_interval"][1])
                              - rational(PARAMETERS["strict_cut"]))
    b_local = saved_upper(new_record(graphs, "local_positive_weight_coefficients",
                                    "complete_backward_mean_coefficient_upper"))
    b_strict = saved_upper(new_record(graphs, "strict_positive_weight_coefficients",
                                     "complete_backward_mean_coefficient_upper"))
    g_local = emit("complete_local_backward_factor_upper",
                   (local_length * b_local).exp(), operation="exponential")
    g_strict = emit("complete_strict_backward_factor_upper",
                    (strict_length * b_strict).exp(), operation="exponential")
    z_local = emit("complete_local_mean_upper",
                   local_length * saved_upper(g_local)
                   * saved_upper(saved["local_CF"]))
    z_strict = emit("complete_strict_mean_upper",
                    saved_upper(g_strict)
                    * (strict_length * saved_upper(saved["strict_CF"])
                       + saved_upper(z_local)))
    for patch, z in (("local", z_local), ("strict", z_strict)):
        absolute = saved_upper(new_record(
            graphs, patch + "_positive_weight_coefficients",
            "complete_absolute_mean_coefficient_upper"))
        emit("complete_" + patch + "_mean_derivative_upper",
             absolute * saved_upper(z) + saved_upper(saved[patch + "_CF"]))

def complete_affine_sources(saved, graphs, emit):
    for patch in ("strict", "local"):
        z = saved_upper(new_record(graphs, "two_patch_backward_mean",
                                  "complete_" + patch + "_mean_upper"))
        zr = saved_upper(new_record(graphs, "two_patch_backward_mean",
                                   "complete_" + patch + "_mean_derivative_upper"))
        tk = saved_upper(new_record(graphs, patch + "_positive_weight_coefficients",
                                   "complete_Tk_upper"))
        emit("complete_" + patch + "_raw_mean_source_upper",
             saved_upper(saved[patch + "_k0"]) * zr + tk * z)
        emit("complete_" + patch + "_primitive_mean_source_upper",
             saved_upper(saved[patch + "_Ik"]) * zr + tk * z / 4)

def complete_negative_receiver(saved, graphs, emit):
    old = lambda key: saved_upper(saved[key])
    raw = [saved_upper(new_record(graphs, "complete_affine_mean_sources",
                                 "complete_" + patch + "_raw_mean_source_upper"))
           for patch in ("strict", "local")]
    mc = emit("complete_collar_raw_mean_union_upper", max(raw))
    mt = saved_upper(new_record(
        graphs, "complete_affine_mean_sources",
        "complete_strict_primitive_mean_source_upper"))
    collar = emit("complete_collar_ordinary_source_upper",
                  old("sqrt_two_upper") * old("ell_plus_one_fourth_upper")
                  * (old("collar_B_union")
                     + old("collar_T_union") * old("N_minus5_6_upper"))
                  + old("sqrt_ell_plus_upper") * saved_upper(mc)
                  * old("N_minus5_3_upper"))
    strict = emit("complete_strict_ordinary_source_upper",
                  rational(PARAMETERS["original_PW_cut"])
                  * (old("ell_minus_negative_fourth_upper")
                     * (old("strict_B_t")
                        + old("strict_T_t") * old("N_minus1_2_upper"))
                     + mt * old("N_minus4_3_upper")))
    received_collar = emit("complete_collar_received_with_jumps_upper",
                           old("C_O") * saved_upper(collar)
                           + old("C_R") * old("jump_collar"))
    received_strict = emit("complete_strict_received_with_jumps_upper",
                           old("C_1") * (saved_upper(strict) + old("jump_strict")))
    emit("complete_same_negative_error_upper",
         old("Bessel_prefactor")
         * (saved_upper(received_collar) * old("dyadic_one_third")
            + saved_upper(received_strict) * old("dyadic_two_thirds")))

def complete_waist_endpoint(saved, graphs, emit):
    z_waist = saved_upper(new_record(
        graphs, "two_patch_backward_mean", "complete_strict_mean_upper"))
    mean = emit("complete_physical_mean_endpoint_upper",
                saved_upper(saved["endpoint_Vz"]) * z_waist
                * saved_upper(saved["Xi23_6"]))
    emit("complete_same_waist_endpoint_upper",
         saved_upper(saved["endpoint_scattering"])
         + saved_upper(saved["endpoint_second_order"])
         + saved_upper(saved["endpoint_WT"]) + saved_upper(mean))

def complete_final_errors(saved, graphs, emit):
    negative = saved_upper(new_record(
        graphs, "complete_negative_receiver", "complete_same_negative_error_upper"))
    endpoint = saved_upper(new_record(
        graphs, "complete_waist_endpoint", "complete_same_waist_endpoint_upper"))
    nonroot = emit("complete_nonroot_source_sum_upper",
                   saved_upper(saved["Rplus"]) + negative + endpoint)
    all_sources = emit("complete_all_source_sum_upper",
                       saved_upper(nonroot) + saved_upper(saved["RF"]))
    received = emit("complete_whole_received_source_upper",
                    saved_upper(saved["Lrec"]) * saved_upper(all_sources))
    emit("complete_same_whole_error_upper",
         saved_upper(saved["Calg"]) + saved_upper(received))
    reduced_received = emit("complete_reduced_received_source_upper",
                            saved_upper(saved["Lrec"]) * saved_upper(nonroot))
    emit("complete_same_reduced_error_upper",
         saved_upper(saved["D_infinity"]) + saved_upper(reduced_received))

def complete_candidate_choice(saved, graphs, which):
    require(which in ("whole", "reduced"), "complete operator candidate")
    key = "complete_same_" + which + "_error_upper"
    new_path = ["complete_new_graphs", "complete_whole_and_reduced",
                "new_records", key]
    prior_path = ["copied_original_scalar_records", "prior_" + which]
    old_value = saved_upper(saved["prior_" + which])
    new_value = saved_upper(new_record(graphs, "complete_whole_and_reduced", key))
    choose_new = bool(new_value < old_value)
    return {"selected_label": "new_positive_weight" if choose_new else "prior_complete",
            "selected_record_path": new_path if choose_new else prior_path,
            "prior_record_path": prior_path, "new_record_path": new_path,
            "prior_wins_equal_saved_upper": True, "all_candidates_retained": True}

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

        def emit(key, value, operation=None):
            require(key in NEW_GRAPH_SHAPES[name]["new_records"]
                    and key not in doc["complete_new_graphs"][name]["new_records"],
                    "new record target repeated or unknown")
            require(operation in (None, "exponential"), "new operation category")
            if operation == "exponential":
                require(name == "two_patch_backward_mean" and key in (
                    "complete_local_backward_factor_upper",
                    "complete_strict_backward_factor_upper"), "exponential target")
            record = {"ball": norm_upper(value).str(75)}
            doc["complete_new_graphs"][name]["new_records"][key] = record
            doc["saved_record_counts"][name] += 1
            doc["actual_progress"]["new_records_saved"] += 1
            if operation == "exponential":
                doc["actual_progress"]["new_exponentials_saved"] += 1
            doc["stage"] = "record_saved:" + name
            restored = publish()
            return copy.deepcopy(restored["complete_new_graphs"][name]["new_records"][key])
        return emit

    def finish_graph(name):
        graph = doc["complete_new_graphs"][name]
        require(doc["current_target"] == name
                and doc["saved_record_counts"][name] == GRAPH_RECORD_COUNTS[name],
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
        doc["actual_progress"]["complete_original_indices_admitted"] = 2
        doc["actual_progress"]["complete_original_graphs_admitted"] = 13
        doc["actual_progress"]["original_record_objects_copied"] = 69
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
            if spec["endpoint"] == "lower":
                saved_positive_lower(saved[alias])
            else:
                saved_upper(saved[alias])
        for alias, limit in (("qualification_local_U", "1"),
                             ("qualification_local_Iv", "1/2"),
                             ("qualification_local_alpha", "1/2")):
            require(saved_upper(saved[alias]) < rational(limit),
                    "original local rational pointwise qualification")
            doc["actual_progress"]["local_rational_qualifications_completed"] += 1
        gate(GATE_LABELS[7])
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        for patch in ("strict", "local"):
            name = patch + "_positive_weight_coefficients"
            emit = start_graph(name)
            complete_weight_coefficients(saved, patch, emit)
            finish_graph(name)
        operations = (
            ("two_patch_backward_mean", complete_backward_mean),
            ("complete_affine_mean_sources", complete_affine_sources),
            ("complete_negative_receiver", complete_negative_receiver),
            ("complete_waist_endpoint", complete_waist_endpoint),
            ("complete_whole_and_reduced", complete_final_errors))
        for name, function in operations:
            emit = start_graph(name)
            function(saved, doc["complete_new_graphs"], emit)
            finish_graph(name)
        for which in ("whole", "reduced"):
            doc["whole_candidate_choices"][which] = complete_candidate_choice(
                saved, doc["complete_new_graphs"], which)
            doc["actual_progress"]["new_whole_comparisons_completed"] += 1
            doc["stage"] = "complete_candidate_selected:" + which
            publish()
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
                and same_json(doc["saved_record_counts"], GRAPH_RECORD_COUNTS)
                and same_json(doc["actual_progress"], ACTUAL_PROGRESS_COMPLETE)
                and complete_shape(doc["complete_new_graphs"], NEW_GRAPH_SHAPES)
                and len(doc["whole_candidate_choices"]) == 2,
                "complete new graph and actual progress")
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
