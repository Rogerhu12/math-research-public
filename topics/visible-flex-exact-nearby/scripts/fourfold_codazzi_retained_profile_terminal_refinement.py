"""WRT: exact retained-profile regrouping and the same complete strong-window error."""
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
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_retained_profile_terminal_refinement.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py"''')
KIND = json.loads(r'''"complete_exact_retained_profile_terminal_refinement"''')
PROBLEM_ID = json.loads(r'''"same_selected_complete_negative_terminal_regrouping_97_v1"''')
PREFLIGHT_KIND = json.loads(r'''"complete_exact_retained_profile_terminal_refinement_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''99000''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''256''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''1024''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":90421,"git_blob_sha":"edd66cdbe7a438569524ba2614d3822f61de5c81","path":"topics/visible-flex-exact-nearby/notes/strict_flux_mean_forcing_ci/run-43856579962-1/actual-scientific-conclusion.json","role":"prior_WMT","sha256":"c6680025917247e7bec958851d5ee85fc3c3750b059372a87ec568cd9d8acbd4"},{"bytes":16541,"git_blob_sha":"c842d84dab6be6af0162c86cddea068ab35eed57","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/N6_strict.json","role":"N6_strict","sha256":"29514c18c59ca04263adb822de67c09ef4cc699e55ae7428302bf8ecda66bd85"},{"bytes":15998,"git_blob_sha":"738a9d452cca74fd57b4916cd51ea929a33a3fef","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/N6_local.json","role":"N6_local","sha256":"afefa9496dce55ef80a5c4b27c21db92c42c2c9de4d64d05d9b547dfcb394646"},{"bytes":9131,"git_blob_sha":"f2a2687ae736d291c5d5b85e0309e625d729e5d8","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/profile_block_strict.json","role":"profile_block_strict","sha256":"6e781157c43f7ba7f7e4ac454308545444164138920cbab027a7af56dd1d89a6"},{"bytes":9096,"git_blob_sha":"4b10ca03cb4f5a419f1e30f4ba3d8ab1a997ccbb","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/profile_block_local.json","role":"profile_block_local","sha256":"b1ceba8254efd75ca500a0c26e47f7440bdf61b252eecaf5aa8c68a4c5102676"},{"bytes":5471,"git_blob_sha":"f6faddfa43ccb00617327e3740f922bc59ce382b","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/same_angular_J_strict.json","role":"same_angular_J_strict","sha256":"a904a3df4e4d750327618c126362424c8bb8bda42a8fd09344c7742a5631d127"},{"bytes":5048,"git_blob_sha":"37864cba216c25f951f4b98cf16192fd4100cc4b","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/same_angular_J_local.json","role":"same_angular_J_local","sha256":"484350c39e3dd0591dfb62412f044f90d957065d7a7cb2e3c51dc2a240e954c1"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":26894,"git_blob_sha":"9e7c6722efdf37679433f437875b74c3f1a263f8","path":"topics/visible-flex-exact-nearby/results/R133-supplement-exact-retained-profile-regrouping-and-complete-terminal-bound.md","role":"proof_WRT","sha256":"7730307f9c42bb87adc41baca7d0a79262946e5c19cd517449325523380bd38d"}''')
OLD_FIELDSETS = json.loads(r'''{"N6_local":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"N6_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"prior_WMT":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"],"profile_block_local":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"profile_block_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"same_angular_J_local":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"same_angular_J_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"]}''')
ADMISSION_KEYS = json.loads(r'''{"N6_local":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","failure","kind","node_name","printed_record_event_count"],"N6_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","failure","kind","node_name","printed_record_event_count"],"prior_WMT":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","completed_targets","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"],"profile_block_local":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","failure","kind","node_name","printed_record_event_count"],"profile_block_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","failure","kind","node_name","printed_record_event_count"],"same_angular_J_local":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","failure","kind","node_name","printed_record_event_count"],"same_angular_J_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","failure","kind","node_name","printed_record_event_count"]}''')
EXPECTED_ADMISSION_HASHES = json.loads(r'''{"N6_local":{"bytes":2509,"sha256":"070a8e3a436a3191f8ca1b1257a3c61b4e32ac6613ad5628abb1939fbef2b449"},"N6_strict":{"bytes":2519,"sha256":"db4a4602a213daeb37c7164443c155d7b48c31c464da56841b8ef110ef1203cc"},"prior_WMT":{"bytes":50537,"sha256":"8140420dbbe9be029cb013e831301e61a15cbdd65a672c5c178c7deedf8f55a8"},"profile_block_local":{"bytes":2337,"sha256":"5bd2c6c70714081c85f2271b18895475e18caa578846dc4bd96605b1857f53fc"},"profile_block_strict":{"bytes":2341,"sha256":"a4e683a4790ee6a97d28ff1ee9e5e7f7326ac32ad7085c37bc973dbf6c445af5"},"same_angular_J_local":{"bytes":2059,"sha256":"b3784801024adaaecca714732247bc905af0af36b7374f0e6820dbeb90e2349c"},"same_angular_J_strict":{"bytes":2063,"sha256":"c7146369c0f2cd99c1e0386b094e58be72b307c125f55642514c714434e6d662"}}''')
OLD_NODE_COUNTS = json.loads(r'''{"N6_local":{"new":99,"saved":99},"N6_strict":{"new":99,"saved":99},"profile_block_local":{"new":51,"saved":51},"profile_block_strict":{"new":51,"saved":51},"same_angular_J_local":{"new":19,"saved":21},"same_angular_J_strict":{"new":24,"saved":24}}''')
RECORD_SPECS = json.loads(r'''{"Bessel_prefactor":{"endpoint":"upper","path":["copied_original_scalar_records","Bessel_prefactor"],"role":"prior_WMT"},"C_1":{"endpoint":"upper","path":["copied_original_scalar_records","C_1"],"role":"prior_WMT"},"C_O":{"endpoint":"upper","path":["copied_original_scalar_records","C_O"],"role":"prior_WMT"},"C_R":{"endpoint":"upper","path":["copied_original_scalar_records","C_R"],"role":"prior_WMT"},"Calg":{"endpoint":"upper","path":["copied_original_scalar_records","Calg"],"role":"prior_WMT"},"D_infinity":{"endpoint":"upper","path":["copied_original_scalar_records","D_infinity"],"role":"prior_WMT"},"Lrec":{"endpoint":"upper","path":["copied_original_scalar_records","Lrec"],"role":"prior_WMT"},"N_minus4_3_upper":{"endpoint":"upper","path":["copied_original_scalar_records","N_minus4_3_upper"],"role":"prior_WMT"},"N_minus5_3_upper":{"endpoint":"upper","path":["copied_original_scalar_records","N_minus5_3_upper"],"role":"prior_WMT"},"RF":{"endpoint":"upper","path":["copied_original_scalar_records","RF"],"role":"prior_WMT"},"Rplus":{"endpoint":"upper","path":["copied_original_scalar_records","Rplus"],"role":"prior_WMT"},"collar_raw_mean":{"endpoint":"upper","path":["complete_new_graphs","complete_negative_receiver","new_records","complete_collar_raw_mean_union_upper"],"role":"prior_WMT"},"dyadic_one_third":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_one_third"],"role":"prior_WMT"},"dyadic_two_thirds":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_two_thirds"],"role":"prior_WMT"},"ell_minus_negative_fourth_upper":{"endpoint":"upper","path":["copied_original_scalar_records","ell_minus_negative_fourth_upper"],"role":"prior_WMT"},"ell_plus_one_fourth_upper":{"endpoint":"upper","path":["copied_original_scalar_records","ell_plus_one_fourth_upper"],"role":"prior_WMT"},"jump_collar":{"endpoint":"upper","path":["copied_original_scalar_records","jump_collar"],"role":"prior_WMT"},"jump_strict":{"endpoint":"upper","path":["copied_original_scalar_records","jump_strict"],"role":"prior_WMT"},"local_J0":{"endpoint":"upper","path":["conclusion","copied_old_records","same_J_L2_upper"],"role":"same_angular_J_local"},"local_Jminus5_3":{"endpoint":"upper","path":["conclusion","new_complete_records","same_J_Hminus5_3_to_Hminus2_3_upper"],"role":"same_angular_J_local"},"local_profile_five_thirds_0":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",0],"role":"profile_block_local"},"local_profile_five_thirds_1":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",1],"role":"profile_block_local"},"local_profile_five_thirds_2":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",2],"role":"profile_block_local"},"local_profile_five_thirds_3":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",3],"role":"profile_block_local"},"local_profile_five_thirds_4":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",4],"role":"profile_block_local"},"local_reflected_point_profile":{"endpoint":"upper","path":["conclusion","point_profile_records","complete_reflected_point_profile_upper"],"role":"N6_local"},"local_terminal_nminus4":{"endpoint":"upper","path":["conclusion","complete_terminal_nminus4_upper"],"role":"N6_local"},"local_v1_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",0],"role":"N6_local"},"local_v1_angle1":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",1],"role":"N6_local"},"local_v1_angle2":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",2],"role":"N6_local"},"local_v1_angle3":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",3],"role":"N6_local"},"local_v1_angle4":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",4],"role":"N6_local"},"local_v2_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",0],"role":"N6_local"},"local_v2_angle1":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",1],"role":"N6_local"},"local_v2_angle2":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",2],"role":"N6_local"},"local_v2_angle3":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",3],"role":"N6_local"},"local_v2_angle4":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",4],"role":"N6_local"},"local_v3_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","3",0],"role":"N6_local"},"local_v4_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","4",0],"role":"N6_local"},"local_v5_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","5",0],"role":"N6_local"},"prior_negative":{"endpoint":"upper","path":["complete_new_graphs","complete_negative_receiver","new_records","complete_same_negative_error_upper"],"role":"prior_WMT"},"prior_reduced":{"endpoint":"upper","path":["complete_new_graphs","complete_whole_and_reduced","new_records","complete_same_reduced_error_upper"],"role":"prior_WMT"},"prior_whole":{"endpoint":"upper","path":["complete_new_graphs","complete_whole_and_reduced","new_records","complete_same_whole_error_upper"],"role":"prior_WMT"},"sqrt_ell_plus_upper":{"endpoint":"upper","path":["copied_original_scalar_records","sqrt_ell_plus_upper"],"role":"prior_WMT"},"sqrt_two_upper":{"endpoint":"upper","path":["copied_original_scalar_records","sqrt_two_upper"],"role":"prior_WMT"},"strict_IJminus2":{"endpoint":"upper","path":["conclusion","new_complete_records","same_IJ_Hminus2_to_L2_upper"],"role":"same_angular_J_strict"},"strict_J0":{"endpoint":"upper","path":["conclusion","new_complete_records","same_J_L2_upper"],"role":"same_angular_J_strict"},"strict_Jminus5_3":{"endpoint":"upper","path":["conclusion","new_complete_records","same_J_Hminus5_3_to_Hminus2_3_upper"],"role":"same_angular_J_strict"},"strict_primitive_mean":{"endpoint":"upper","path":["complete_new_graphs","complete_strict_mean_and_affine_sources","new_records","complete_strict_primitive_mean_source_upper"],"role":"prior_WMT"},"strict_profile_five_thirds_0":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",0],"role":"profile_block_strict"},"strict_profile_five_thirds_1":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",1],"role":"profile_block_strict"},"strict_profile_five_thirds_2":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",2],"role":"profile_block_strict"},"strict_profile_five_thirds_3":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",3],"role":"profile_block_strict"},"strict_profile_five_thirds_4":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","five_thirds",4],"role":"profile_block_strict"},"strict_profile_two_0":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","two",0],"role":"profile_block_strict"},"strict_profile_two_1":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","two",1],"role":"profile_block_strict"},"strict_profile_two_2":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","two",2],"role":"profile_block_strict"},"strict_profile_two_3":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","two",3],"role":"profile_block_strict"},"strict_profile_two_4":{"endpoint":"upper","path":["conclusion","complete_full_output_block_weights","two",4],"role":"profile_block_strict"},"strict_reflected_point_profile":{"endpoint":"upper","path":["conclusion","point_profile_records","complete_reflected_point_profile_upper"],"role":"N6_strict"},"strict_terminal_nminus4":{"endpoint":"upper","path":["conclusion","complete_terminal_nminus4_upper"],"role":"N6_strict"},"strict_v1_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",0],"role":"N6_strict"},"strict_v1_angle1":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",1],"role":"N6_strict"},"strict_v1_angle2":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",2],"role":"N6_strict"},"strict_v1_angle3":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",3],"role":"N6_strict"},"strict_v1_angle4":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","1",4],"role":"N6_strict"},"strict_v2_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",0],"role":"N6_strict"},"strict_v2_angle1":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",1],"role":"N6_strict"},"strict_v2_angle2":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",2],"role":"N6_strict"},"strict_v2_angle3":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",3],"role":"N6_strict"},"strict_v2_angle4":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","2",4],"role":"N6_strict"},"strict_v3_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","3",0],"role":"N6_strict"},"strict_v4_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","4",0],"role":"N6_strict"},"strict_v5_angle0":{"endpoint":"upper","path":["conclusion","complete_retained_by_inverse_power","5",0],"role":"N6_strict"},"waist_endpoint":{"endpoint":"upper","path":["complete_new_graphs","complete_waist_endpoint","new_records","complete_same_waist_endpoint_upper"],"role":"prior_WMT"}}''')
SCOPE_SPECS = json.loads(r'''{"N6_local_complete_qualifications":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"N6_local"},"N6_strict_complete_qualifications":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"N6_strict"},"prior_WMT_complete_new_graph_qualifications":{"mode":"complete_non_ball_projection","path":["complete_new_graphs"],"role":"prior_WMT"},"prior_WMT_complete_original_qualification_archive":{"mode":"exact","path":["copied_original_scopes"],"role":"prior_WMT"},"prior_WMT_parameters":{"mode":"exact","path":["parameters"],"role":"prior_WMT"},"prior_WMT_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"prior_WMT"},"profile_block_local_complete_qualifications":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"profile_block_local"},"profile_block_strict_complete_qualifications":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"profile_block_strict"},"same_angular_J_local_complete_qualifications":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"same_angular_J_local"},"same_angular_J_strict_complete_qualifications":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"same_angular_J_strict"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"4e7b739f2b7546af411b90c68c1c48beab3f3301b34828167d2e340df1880aed"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''9302''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"d0e94c5e11f9c4212f1e4775d607bee86d3cf6b8d8f4f5d0bd78a6c123c86c8a"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''57334''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"380e21eed5a5097f079c437c486292d0b67385175ea486e6754f273fd5d84453"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''5615''')
PARAMETERS = json.loads(r'''{"arithmetic_bits":320,"copied_original_qualification_objects":10,"copied_original_records":75,"decimal_record_digits":75,"first_absolute_mode":97,"fixed_exact_regrouping_branch_only":true,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","graph_original_copies":0,"history_inputs":0,"input_order":[-4,3],"minimum_physical_frequency":388,"moved_inverse_powers":[3,4,5],"new_complete_terminal_inverse_power":3,"new_dyadic_gap":[1,6],"new_exponentials":0,"new_fractional_powers":3,"new_graphs":7,"new_logarithms":0,"new_record_count":42,"new_square_roots":1,"new_terminal_band_decay":[-3,2],"old_complete_files":7,"old_complete_terminal_inverse_power":4,"old_scientific_calls":0,"old_target_recomputations":0,"operation_counts_cover_only_completed_saved_target_constructions":true,"ordinary_angular_derivative_orders":[0,1,2,3,4],"original_PW_cut":"2333968743003/10000000000000","original_true_interfaces":3070,"physical_frequency":"n=4|j|","physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","retained_inverse_powers":[1,2],"root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"strict_cut":"76285779072683/320000000000000","total_graph_scalar_slots":42}''')
RETAINED_SCOPE = json.loads(r'''{"actual_96_columns_exist_signed_normalization_uncomputed":true,"actual_true_root_not_upper_enclosure":true,"all_four_waist_endpoints_and_positive_root_terms_read_only":true,"all_internal_means_projections_I_J_terminals_retained":true,"complete_WMT_physical_mean_and_both_stored_means_read_only":true,"complete_even_mean_zero_projection_before_same_angular_J":true,"complete_old_terminal_never_subtracted_or_discarded":true,"complete_reflected_point_factor_two_not_repeated":true,"exact_full_signed_input_slot_bound_paid":true,"final_surface_proved":false,"finite_Schur_inverse_proved":false,"full_Hminus4_3_extension_by_original_input_band_sum":true,"full_incoming_inverse_proved":false,"full_nonlinear_background_proved":false,"full_output_profile_zero_and_low_modes_retained":true,"full_ten_ordered_Q_words_and_radial_derivatives_retained":true,"metric_nu_Schur_and_infinite_radial_head_retained":true,"new_terminal_has_separate_one_sixth_sum":true,"no_old_negative_total_subtraction":true,"old_scientific_producers_not_imported":true,"ordinary_derivative_bounds_not_Wiener_A0_or_normalized_jets":true,"original_ordinary_dr_and_PW_cut_and_3070_interfaces_retained":true,"original_successes_and_failed_later_parent_status_retained":true,"original_trial_and_complete_genuine_Vext_and_root_matrix_unchanged":true,"passing_high_cutoff_proved":false,"root_FJ_two_ranks_rho_i_ell2_and_mean_rows_retained":true,"same_fixed_intrinsic_eta0":true,"same_selected_real_member_only":true,"true_transported_finite_complement_Theta_and_all_cross_rows_retained":true,"whole_and_reduced_compared_only_with_the_same_original_operator":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_terminal_summation_constants","complete_strict_retained_and_terminal","complete_local_retained_and_terminal","complete_actual_inverse_and_patch_union","complete_original_radial_and_receiving","complete_new_negative_receiver","complete_whole_and_reduced"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_actual_inverse_and_patch_union":{"complete":true,"kind":"complete_same_inverse_and_terminal_patch_fees","maxima_only_join_patches_of_same_operator":true,"new_records":{"complete_collar_B_union_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_T_union_upper":{"ball":"__FINITE_SCALAR__"},"local_B_c_upper":{"ball":"__FINITE_SCALAR__"},"local_T_c_upper":{"ball":"__FINITE_SCALAR__"},"strict_B_c_upper":{"ball":"__FINITE_SCALAR__"},"strict_B_t_upper":{"ball":"__FINITE_SCALAR__"},"strict_T_c_upper":{"ball":"__FINITE_SCALAR__"},"strict_T_t_upper":{"ball":"__FINITE_SCALAR__"}},"same_original_even_mean_zero_to_odd_J":true,"strict_IJ_is_one_complete_original_saved_record":true,"terminal_I_L2_norm":[1,4]},"complete_local_retained_and_terminal":{"all_original_radial_words_and_internal_means_retained":true,"complete":true,"complete_even_mean_zero_projection_before_same_J":true,"complete_reflected_point_record_already_includes_factor_two":true,"kind":"complete_exact_local_retained_profile_regrouping","moved_inverse_powers":[3,4,5],"new_records":{"complete_retained_Hminus5_3_profile_upper":{"ball":"__FINITE_SCALAR__"},"complete_terminal_nminus3_upper":{"ball":"__FINITE_SCALAR__"},"ordinary_angles_0_4":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"old_complete_terminal_retained_in_full":true,"ordinary_angular_derivatives_not_factorial_normalized":true,"patch":"local","retained_inverse_powers":[1,2]},"complete_new_negative_receiver":{"all_signed_band_slots_at_most_N":true,"band_decay_powers":[[-5,3],[-2,1],[-3,2]],"complete":true,"dyadic_gaps":[[1,3],[2,3],[1,6]],"full_low_output_leakage_retained":true,"input_window":"original reflected natural H^-4/3, n=4|j|>=388","kind":"complete_three_decay_strong_window_negative_operator","new_records":{"complete_collar_dyadic_contribution_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_negative_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_dyadic_contribution_upper":{"ball":"__FINITE_SCALAR__"},"complete_terminal_dyadic_contribution_upper":{"ball":"__FINITE_SCALAR__"}},"orthogonality_only_between_original_input_bands":true,"output_window":"complete original waist density state and two stored physical means"},"complete_original_radial_and_receiving":{"all_3070_interfaces_and_original_disjoint_assignment_retained":true,"complete":true,"kind":"complete_original_radial_source_and_jump_receiving_fees","new_records":{"complete_collar_retained_and_mean_ordinary_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_retained_mean_and_jumps_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_terminal_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_retained_and_mean_ordinary_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_retained_mean_and_jumps_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_terminal_received_upper":{"ball":"__FINITE_SCALAR__"},"complete_terminal_received_sum_upper":{"ball":"__FINITE_SCALAR__"}},"no_radial_length_on_impulses":true,"ordinary_dr":true,"original_PW_cut":"2333968743003/10000000000000","physical_two_means_retained":true,"true_root_not_upper_enclosure":true,"whole_WMT_mean_fees_read_verbatim":true},"complete_strict_retained_and_terminal":{"all_original_radial_words_and_internal_means_retained":true,"complete":true,"complete_even_mean_zero_projection_before_same_J":true,"complete_reflected_point_record_already_includes_factor_two":true,"kind":"complete_exact_strict_retained_profile_regrouping","moved_inverse_powers":[3,4,5],"new_records":{"complete_retained_Hminus2_profile_upper":{"ball":"__FINITE_SCALAR__"},"complete_retained_Hminus5_3_profile_upper":{"ball":"__FINITE_SCALAR__"},"complete_terminal_nminus3_upper":{"ball":"__FINITE_SCALAR__"},"ordinary_angles_0_4":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"old_complete_terminal_retained_in_full":true,"ordinary_angular_derivatives_not_factorial_normalized":true,"patch":"strict","retained_inverse_powers":[1,2]},"complete_terminal_summation_constants":{"complete":true,"denominator_uses_true_interval_not_inverted_upper":true,"input_order":[-4,3],"kind":"complete_new_terminal_frequency_and_dyadic_constants","minimum_physical_frequency":388,"new_dyadic_gap":[1,6],"new_records":{"dyadic_one_sixth_upper":{"ball":"__FINITE_SCALAR__"},"two_one_sixth_upper":{"ball":"__FINITE_SCALAR__"}},"new_terminal_band_decay":[-3,2]},"complete_whole_and_reduced":{"actual_96_columns_exist_signed_normalization_uncomputed":true,"all_four_complete_waist_endpoints_read_verbatim":true,"complete":true,"kind":"complete_same_whole_and_reduced_terminal_regrouping","new_records":{"complete_all_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonroot_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_reduced_received_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_reduced_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_whole_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_whole_received_source_upper":{"ball":"__FINITE_SCALAR__"}},"positive_and_root_received_fees_not_received_again":true,"root_and_FJ_finite_factors_and_physical_mean_rows_retained":true,"whole_Calg_not_replaced_by_D_infinity":true,"whole_and_reduced_are_different_operators":true}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_actual_inverse_and_patch_union":8,"complete_local_retained_and_terminal":7,"complete_new_negative_receiver":4,"complete_original_radial_and_receiving":7,"complete_strict_retained_and_terminal":8,"complete_terminal_summation_constants":2,"complete_whole_and_reduced":6}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_actual_inverse_and_patch_union":8,"complete_local_retained_and_terminal":7,"complete_new_negative_receiver":4,"complete_original_radial_and_receiving":7,"complete_strict_retained_and_terminal":8,"complete_terminal_summation_constants":2,"complete_whole_and_reduced":6}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":7,"new_exponentials_saved":0,"new_fractional_powers":3,"new_graphs_completed":7,"new_logarithms":0,"new_quadratures":0,"new_records_saved":42,"new_square_roots":1,"new_whole_comparisons_completed":2,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":10,"original_record_objects_copied":75,"original_records_copied_in_graphs":0}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","current_input_and_AST_identity","all_seven_complete_original_files_byte_identical","complete_prior_WMT_science","six_complete_posterior_nodes_and_common_binding","original_dependencies_and_parent_failure_retained","complete_scalar_and_qualification_copies_retained","typed_norm_records_and_actual_profile_J_scope","complete_terminal_summation_constants","complete_strict_retained_and_terminal","complete_local_retained_and_terminal","complete_actual_inverse_and_patch_union","complete_original_radial_and_receiving","complete_new_negative_receiver","complete_whole_and_reduced","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]''')
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
            return {}
        return {key: original_qualifications(child) for key, child in value.items()}
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

def accepted_original_inputs(docs, files):
    prior = docs["prior_WMT"]
    nodes = {}
    for spec in EXPECTED_OLD_FILES:
        role = spec["role"]
        if role == "prior_WMT":
            continue
        old = docs[role]
        ref = complete_object_reference(docs, role, ["binding"])
        nodes[role] = {
            "printed_new_record_event_count": old["printed_record_event_count"],
            "complete_saved_record_count": scalar_record_count(old["conclusion"]),
            "original_binding_reference": {
                "complete_canonical_bytes": ref["complete_canonical_bytes"],
                "complete_canonical_sha256": ref["complete_canonical_sha256"]}}
    previous = {key: copy.deepcopy(prior[key]) for key in (
        "run_id", "run_attempt", "workflow_event_commit", "actual_checkout_commit",
        "manifest_sha256", "scientific_modules", "runtime", "complete", "proved",
        "actual_returncode", "stage", "failure")}
    previous["complete_original_input_admission_reference"] = complete_object_reference(
        docs, "prior_WMT", ["accepted_old_inputs"])
    previous["original_prior_attempt_summaries"] = {
        name: {key: copy.deepcopy(value[key]) for key in (
            "run_id", "run_attempt", "complete", "proved",
            "actual_returncode", "stage", "failure")}
        for name, value in prior["accepted_old_inputs"]["original_prior_attempts"].items()}
    return {
        "complete_original_file_receipts": [
            five_fields(files[spec["role"]]) for spec in EXPECTED_OLD_FILES],
        "complete_prior_WMT_receipt": previous,
        "complete_original_node_receipts": nodes,
        "original_binding_reference_context": {
            "input_role": "each complete_original_node_receipts key",
            "json_path": ["binding"],
            "file_identity": "the same role in complete_original_file_receipts",
            "common_fields_verified_equal": [
                "parameters_sha256", "mathematical_input_sha256", "scientific_module_sha256"],
            "mathematical_input_roles": 12, "scientific_modules": 5},
        "all_seven_complete_byte_pins_verified": True,
        "all_original_domains_and_complete_gate_lists_verified": True,
        "only_complete_original_nodes_reused": True,
        "failed_parent_not_relabelled_success": True,
        "original_binding_and_status_references_keep_original_context": True,
        "old_scientific_calls": 0}

def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(digest(manifest_raw) == manifest_sha, "manifest CLI identity")
    manifest = exact_json(manifest_raw)
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_WRT", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 11
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 11,
            "eleven complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "original input pin differs")
    require(same_json(files["proof_WRT"], EXPECTED_PROOF), "published WRT pin")
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
                "complete old JSON schema or spelling differs")
        projection = {key: old[key] for key in ADMISSION_KEYS[role]}
        body = canonical(projection)
        expected = EXPECTED_ADMISSION_HASHES[role]
        require(len(body) == expected["bytes"] and digest(body) == expected["sha256"],
                "complete original status/identity/parameter/scope/gate projection differs")
    prior = docs["prior_WMT"]
    require(prior["kind"] == "complete_strict_flux_L1_mean_forcing_refinement"
            and prior["complete"] is True and prior["proved"] is True
            and prior["actual_returncode"] == 0 and prior["failure"] is None
            and prior["stage"] == "complete" and len(prior["gates"]) == 18,
            "complete original WMT mathematical result")
    require(all(set(g) == {"name", "passed"} and g["passed"] is True
                for g in prior["gates"]), "entire original WMT gate list")
    require(prior["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"}
            and prior["actual_progress"]["new_records_saved"] == 195
            and prior["actual_progress"]["original_records_copied_in_graphs"] == 2
            and prior["actual_progress"]["old_targets_recomputed"] == 0
            and scalar_record_count(prior["complete_new_graphs"]) == 197,
            "actual original runtime and all 197 saved WMT records")
    pp = prior["parameters"]
    require(pp["selected_original_real_member_only"] is True
            and pp["fixed_intrinsic_eta0"] == PARAMETERS["fixed_intrinsic_eta0"]
            and pp["strict_cut"] == PARAMETERS["strict_cut"]
            and pp["original_PW_cut"] == PARAMETERS["original_PW_cut"]
            and pp["physical_mean_initial_condition"] == "z_ph(r_star)=0"
            and pp["minimum_physical_frequency"] == 388
            and pp["original_true_interfaces"] == 3070
            and same_json(pp["root_interval"], PARAMETERS["root_interval"]),
            "same actual root, two patches, receiving cut and frequency")
    for which in ("whole", "reduced"):
        choice = prior["whole_candidate_choices"][which]
        require(choice["selected_label"] == "new_strict_flux"
                and choice["selected_record_path"] == RECORD_SPECS["prior_" + which]["path"]
                and choice["all_candidates_retained"] is True
                and choice["prior_wins_equal_saved_upper"] is True,
                "actual selected complete WMT comparison record")
    attempts = prior["accepted_old_inputs"]["original_prior_attempts"]
    failed = attempts["prior_prefix_index"]
    completed = attempts["prior_completion_index"]
    require(failed["complete"] is False and failed["proved"] is False
            and failed["actual_returncode"] == 1 and failed["run_id"] == "43827705714"
            and failed["failure"]["active_node"] == "complete_free_waist_Airy_and_Schur_map"
            and completed["complete"] is True and completed["proved"] is True
            and completed["actual_returncode"] == 0 and completed["failure"] is None
            and completed["run_id"] == "43831678361",
            "failed original attempt and successful continuation remain distinct")
    core = docs["N6_strict"]["binding"]
    require(len(core["mathematical_input_sha256"]) == 12
            and len(core["scientific_module_sha256"]) == 5,
            "complete original mathematical binding")
    by_node = {spec["role"]: spec for spec in EXPECTED_OLD_FILES if spec["role"] != "prior_WMT"}
    for role, spec in by_node.items():
        old = docs[role]
        binding = old["binding"]
        count = OLD_NODE_COUNTS[role]
        require(old["kind"] == "WEJ_complete_atomic_node_v1"
                and old["node_name"] == role and old["complete"] is True
                and old["failure"] is None and old["automatic_retry_authorized"] is False
                and old["all_printed_records_in_complete_conclusion"] is True
                and old["printed_record_event_count"] == count["new"]
                and scalar_record_count(old["conclusion"]) == count["saved"],
                "complete original posterior node")
        require(binding["problem_id"] ==
                "complete_global_genuine_waist_error_posterior_selected_original_97_v1/" + role
                and all(same_json(binding[key], core[key]) for key in (
                    "parameters_sha256", "mathematical_input_sha256",
                    "scientific_module_sha256")),
                "original node common binding differs")
        for dependency, receipt in binding["direct_dependency_receipts"].items():
            require(set(receipt) == {"file", "bytes", "sha256"},
                    "whole original direct dependency receipt")
            if dependency in by_node:
                known = by_node[dependency]
                require(receipt == {"file": "graphs/" + dependency + ".json",
                                    "bytes": known["bytes"], "sha256": known["sha256"]},
                        "complete direct dependency differs from the same input node")
    for receipt in prior["accepted_old_inputs"]["complete_original_file_receipts"]:
        role = receipt["role"]
        key = {"wgs_main": "WGS_main", "wgs_copies": "WGS_original_inputs"}.get(role)
        if key is not None:
            require(receipt["sha256"] == core["mathematical_input_sha256"][key],
                    "WMT and original posterior used a different WGS pair")
        if role == "profile_strict":
            known = files["profile_block_strict"]
            require(receipt["sha256"] == known["sha256"]
                    and receipt["bytes"] == known["bytes"]
                    and receipt["blob_sha"] == known["git_blob_sha"],
                    "WMT original strict profile differs")
    for patch in ("strict", "local"):
        node = docs["N6_" + patch]["conclusion"]
        require(node["kind"] == "complete_ordered_scalar_N6_residual_patch_v1"
                and node["complete"] is True and node["patch"] == patch
                and node["retained_inverse_powers"] == [1, 2, 3, 4, 5]
                and node["exactly_cancelled_inverse_powers"] == [-2, -1, 0]
                and node["terminal_inverse_power_before_input"] == 4
                and node["original_input_normalization_power"] == [7, 6]
                and node["original_input_frequency"] == "n=4|j|"
                and node["single_column_to_reflected_terminal_factor"] == 2
                and node["complete_final_even_mean_zero_P_retained"] is True
                and node["all_internal_projections_and_mean_functionals_retained"] is True
                and node["deferred_outer_P_only_crossed_radial_scalars"] is True
                and node["block_rows_use_full_signed_carrier_then_isometric_restriction"] is True
                and node["WGS_amplitude_sup_bounds_not_relabelled_Wiener_A0"] is True
                and node["old_scientific_targets_recomputed"] == 0,
                "same complete exact N6 polynomial, terminal and projection scope")
        require(set(node["complete_retained_by_inverse_power"]) == {"1", "2", "3", "4", "5"}
                and all(len(value) == 5 for value in
                        node["complete_retained_by_inverse_power"].values()),
                "complete saved ordinary angles zero through four")
        profile = docs["profile_block_" + patch]["conclusion"]
        require(profile["complete_block_includes_all_signed_Fourier_inputs"] is True
                and profile["two_Jost_phases_already_included"] is True
                and profile["full_output_zero_and_low_modes_retained"] is True
                and profile["no_output_block_orthogonality_used"] is True
                and profile["partition_used_only_in_the_estimate_not_inserted_in_the_trial"] is True
                and profile["near_partition_has_zero_angular_derivatives"] is True
                and profile["weight_input"] ==
                "sum_{a=0}^4 weight[a] times full ordinary angular amplitude component-sum derivative[a]"
                and profile["block_bound"] ==
                "N^-d * (1+N^(2/3)*rho)^(-1/4) * weighted_amplitude_sum",
                "same full-output profile and actual pointwise radial normalization")
        inverse = docs["same_angular_J_" + patch]["conclusion"]
        require(inverse["space"] == "the original angular even-mean-zero to odd realization"
                and inverse["physical_means_discarded"] is False
                and inverse["stable_trace_inverse_used"] is False
                and inverse["root_and_strict_inverses_agree_only_on_their_actual_overlap"] is True,
                "same parity inverse and its exact qualified patch")
    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 75 and all(
                isinstance(v, dict) and set(v) == {"ball"} and isinstance(v["ball"], str)
                for v in records.values())
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all 75 complete original scalar objects retained")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(spec["mode"] in ("exact", "complete_non_ball_projection"), "scope mode")
        scopes[name] = (copy.deepcopy(value) if spec["mode"] == "exact"
                        else original_qualifications(value))
    require(len(scopes) == 10 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "all complete original qualification objects retained")
    accepted = accepted_original_inputs(docs, files)
    require(len(canonical(accepted)) == ORIGINAL_ACCEPTED_BYTES
            and digest(canonical(accepted)) == ORIGINAL_ACCEPTED_SHA,
            "complete original receipt references differ")
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

# New WRT finite positive formulas only. Definitions have no import-time arithmetic.
# All original scalars are read; no prior producer or old graph is invoked.

def graph_record(graphs, name, path):
    return at(graphs[name]["new_records"], [path] if isinstance(path, str) else path)

def complete_terminal_constants(saved, graphs, emit):
    theta = emit("two_one_sixth_upper", arb(2) ** (arb(1) / arb(6)),
                 fractional_powers=1)
    # All bases are exact positive integers. Keep the true interval for the
    # negative-power ratio; a saved positive upper must not be inverted here.
    decay = arb(388) ** (-arb(1) / arb(6))
    ratio = arb(2) ** (-arb(1) / arb(3))
    gap = arb(1) - ratio
    require(gap.is_finite() and gap.lower() > 0,
            "new one-sixth dyadic denominator must be positive")
    emit("dyadic_one_sixth_upper", decay / gap.sqrt(),
         fractional_powers=2, square_roots=1)

def complete_patch_regrouping(saved, graphs, emit, patch):
    require(patch in ("strict", "local"), "original coefficient patch")
    angles = []
    for j in range(5):
        angles.append(emit(["ordinary_angles_0_4", j],
            saved_upper(saved[patch + "_v1_angle" + str(j)])
            + saved_upper(saved[patch + "_v2_angle" + str(j)]) / arb(388)))
    for d in (("five_thirds", "two") if patch == "strict" else ("five_thirds",)):
        value = arb(0)
        for j in range(5):
            value += saved_upper(saved[patch + "_profile_" + d + "_" + str(j)]) \
                     * saved_upper(angles[j])
        field = ("complete_retained_Hminus5_3_profile_upper" if d == "five_thirds"
                 else "complete_retained_Hminus2_profile_upper")
        emit(field, value)
    moved = (saved_upper(saved[patch + "_v3_angle0"])
             + saved_upper(saved[patch + "_v4_angle0"]) / arb(388)
             + saved_upper(saved[patch + "_v5_angle0"]) / arb(388) ** 2)
    emit("complete_terminal_nminus3_upper",
         saved_upper(saved[patch + "_terminal_nminus4"]) / arb(388)
         + saved_upper(saved[patch + "_reflected_point_profile"]) * moved)

def complete_strict_regrouping(saved, graphs, emit):
    complete_patch_regrouping(saved, graphs, emit, "strict")

def complete_local_regrouping(saved, graphs, emit):
    complete_patch_regrouping(saved, graphs, emit, "local")

def complete_inverse_and_union(saved, graphs, emit):
    theta = saved_upper(graph_record(graphs, "complete_terminal_summation_constants",
                                    "two_one_sixth_upper"))
    work = {}
    for patch in ("strict", "local"):
        name = "complete_" + patch + "_retained_and_terminal"
        profile = saved_upper(graph_record(graphs, name,
                            "complete_retained_Hminus5_3_profile_upper"))
        terminal = saved_upper(graph_record(graphs, name,
                             "complete_terminal_nminus3_upper"))
        work[patch + "_B_c"] = emit(patch + "_B_c_upper",
            theta * saved_upper(saved[patch + "_Jminus5_3"]) * profile)
        if patch == "strict":
            emit("strict_B_t_upper",
                 theta * saved_upper(saved["strict_IJminus2"])
                 * saved_upper(graph_record(graphs, name,
                         "complete_retained_Hminus2_profile_upper")))
        work[patch + "_T_c"] = emit(patch + "_T_c_upper",
                                  saved_upper(saved[patch + "_J0"]) * terminal)
        if patch == "strict":
            emit("strict_T_t_upper", saved_upper(work["strict_T_c"]) / arb(4))
    emit("complete_collar_B_union_upper",
         max(saved_upper(work["strict_B_c"]), saved_upper(work["local_B_c"])))
    emit("complete_collar_T_union_upper",
         max(saved_upper(work["strict_T_c"]), saved_upper(work["local_T_c"])))

def complete_radial_and_receiving(saved, graphs, emit):
    old = lambda key: saved_upper(saved[key])
    fee = lambda key: saved_upper(graph_record(graphs,
                       "complete_actual_inverse_and_patch_union", key))
    cut = rational(PARAMETERS["original_PW_cut"])
    collar = emit("complete_collar_retained_and_mean_ordinary_upper",
        old("sqrt_two_upper") * old("ell_plus_one_fourth_upper")
        * fee("complete_collar_B_union_upper")
        + old("sqrt_ell_plus_upper") * old("collar_raw_mean")
        * old("N_minus5_3_upper"))
    strict = emit("complete_strict_retained_and_mean_ordinary_upper",
        cut * (old("ell_minus_negative_fourth_upper") * fee("strict_B_t_upper")
               + old("strict_primitive_mean") * old("N_minus4_3_upper")))
    emit("complete_collar_retained_mean_and_jumps_received_upper",
         old("C_O") * saved_upper(collar) + old("C_R") * old("jump_collar"))
    emit("complete_strict_retained_mean_and_jumps_received_upper",
         old("C_1") * (saved_upper(strict) + old("jump_strict")))
    terminal_c = emit("complete_collar_terminal_received_upper",
        old("C_O") * old("sqrt_two_upper") * old("ell_plus_one_fourth_upper")
        * fee("complete_collar_T_union_upper"))
    terminal_s = emit("complete_strict_terminal_received_upper",
        old("C_1") * cut * old("ell_minus_negative_fourth_upper")
        * fee("strict_T_t_upper"))
    emit("complete_terminal_received_sum_upper",
         saved_upper(terminal_c) + saved_upper(terminal_s))

def complete_new_negative(saved, graphs, emit):
    get = lambda key: saved_upper(graph_record(graphs,
                          "complete_original_radial_and_receiving", key))
    collar = emit("complete_collar_dyadic_contribution_upper",
        get("complete_collar_retained_mean_and_jumps_received_upper")
        * saved_upper(saved["dyadic_one_third"]))
    strict = emit("complete_strict_dyadic_contribution_upper",
        get("complete_strict_retained_mean_and_jumps_received_upper")
        * saved_upper(saved["dyadic_two_thirds"]))
    terminal = emit("complete_terminal_dyadic_contribution_upper",
        get("complete_terminal_received_sum_upper")
        * saved_upper(graph_record(graphs, "complete_terminal_summation_constants",
                                   "dyadic_one_sixth_upper")))
    emit("complete_same_negative_error_upper",
         saved_upper(saved["Bessel_prefactor"])
         * (saved_upper(collar) + saved_upper(strict) + saved_upper(terminal)))

def complete_new_errors(saved, graphs, emit):
    negative = saved_upper(graph_record(graphs, "complete_new_negative_receiver",
                                        "complete_same_negative_error_upper"))
    nonroot = emit("complete_nonroot_source_sum_upper",
        saved_upper(saved["Rplus"]) + negative + saved_upper(saved["waist_endpoint"]))
    all_sources = emit("complete_all_source_sum_upper",
                       saved_upper(nonroot) + saved_upper(saved["RF"]))
    received = emit("complete_whole_received_source_upper",
                   saved_upper(saved["Lrec"]) * saved_upper(all_sources))
    emit("complete_same_whole_error_upper",
         saved_upper(saved["Calg"]) + saved_upper(received))
    reduced = emit("complete_reduced_received_source_upper",
                   saved_upper(saved["Lrec"]) * saved_upper(nonroot))
    emit("complete_same_reduced_error_upper",
         saved_upper(saved["D_infinity"]) + saved_upper(reduced))

def complete_candidate_choice(saved, graphs, which):
    require(which in ("whole", "reduced"), "same complete operator candidate")
    field = "complete_same_" + which + "_error_upper"
    new_path = ["complete_new_graphs", "complete_whole_and_reduced", "new_records", field]
    prior_path = ["copied_original_scalar_records", "prior_" + which]
    choose_new = bool(saved_upper(graph_record(graphs, "complete_whole_and_reduced", field))
                      < saved_upper(saved["prior_" + which]))
    return {
        "selected_label": ("new_exact_terminal_regrouping" if choose_new
                           else "prior_complete_strict_flux"),
        "selected_record_path": new_path if choose_new else prior_path,
        "prior_record_path": prior_path, "new_record_path": new_path,
        "prior_wins_equal_saved_upper": True, "all_candidates_retained": True
    }

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

        def emit(path, value, fractional_powers=0, square_roots=0):
            path = [path] if isinstance(path, str) else list(path)
            target = at(NEW_GRAPH_SHAPES[name]["new_records"], path)
            require(target == {"ball": "__FINITE_SCALAR__"}, "new target specification")
            if name == ORDERED_GRAPH_NAMES[0]:
                expected_work = {"two_one_sixth_upper": (1, 0),
                                 "dyadic_one_sixth_upper": (2, 1)}
                require(len(path) == 1 and path[0] in expected_work
                        and (fractional_powers, square_roots) == expected_work[path[0]],
                        "complete saved-target power accounting")
            else:
                require(fractional_powers == 0 and square_roots == 0,
                        "only the new constants have powers or square roots")
            record = {"ball": norm_upper(value).str(75)}
            insert_new_record(doc["complete_new_graphs"][name]["new_records"], path, record)
            doc["saved_record_counts"][name] += 1
            new_counts[name] += 1
            doc["actual_progress"]["new_records_saved"] += 1
            # These counts cover operations in completed, persisted targets;
            # no unsaved working expression is reported as a completed target.
            doc["actual_progress"]["new_fractional_powers"] += fractional_powers
            doc["actual_progress"]["new_square_roots"] += square_roots
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
        doc["actual_progress"]["complete_original_files_admitted"] = 7
        doc["actual_progress"]["original_record_objects_copied"] = 75
        doc["actual_progress"]["original_qualification_objects_copied"] = 10
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
        gate(GATE_LABELS[7])
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        operations = (
            ("complete_terminal_summation_constants", complete_terminal_constants),
            ("complete_strict_retained_and_terminal", complete_strict_regrouping),
            ("complete_local_retained_and_terminal", complete_local_regrouping),
            ("complete_actual_inverse_and_patch_union", complete_inverse_and_union),
            ("complete_original_radial_and_receiving", complete_radial_and_receiving),
            ("complete_new_negative_receiver", complete_new_negative),
            ("complete_whole_and_reduced", complete_new_errors))
        require([name for name, _ in operations] == ORDERED_GRAPH_NAMES, "complete new graph order")
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
                and same_json(new_counts, GRAPH_NEW_RECORD_COUNTS)
                and same_json(doc["actual_progress"], ACTUAL_PROGRESS_COMPLETE)
                and complete_shape(doc["complete_new_graphs"], NEW_GRAPH_SHAPES)
                and digest(canonical(doc["copied_original_scalar_records"])) == ORIGINAL_RECORD_SHA
                and digest(canonical(doc["copied_original_scopes"])) == ORIGINAL_SCOPE_SHA
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
        sys.stderr.write(trace.decode("utf-8", "replace"))
        sys.stderr.flush()
        doc["complete"] = False
        doc["proved"] = False
        doc["actual_returncode"] = 1
        doc["stage"] = "preserved_failure"
        message_text, message_cut = bounded_diagnostic(message, DIAGNOSTIC_MESSAGE_BYTES)
        trace_text, trace_cut = bounded_diagnostic(trace, DIAGNOSTIC_TRACEBACK_BYTES)
        doc["failure"] = {
            "type": type(error).__name__,
            "message": message_text, "traceback": trace_text,
            "message_truncated": message_cut, "traceback_truncated": trace_cut}
        publish(check_size=False)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
