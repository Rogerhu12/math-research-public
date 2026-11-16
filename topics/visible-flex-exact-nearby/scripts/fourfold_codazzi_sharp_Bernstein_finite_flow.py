"""WBF: complete sharp Bernstein finite-flow bounds from three immutable receipts."""
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
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_sharp_Bernstein_finite_flow.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py"''')
KIND = json.loads(r'''"complete_sharp_Bernstein_integrated_finite_flow_bounds"''')
PROBLEM_ID = json.loads(r'''"same_selected_sharp_Bernstein_flow15_relative_omega14_v1"''')
PREFLIGHT_KIND = json.loads(r'''"complete_sharp_Bernstein_integrated_finite_flow_bounds_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''90000''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''512''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''2048''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":72251,"git_blob_sha":"32ff92c516fcc5c43f3619930d4845d294289270","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json","role":"wgs_main","sha256":"8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"},{"bytes":31632,"git_blob_sha":"d6d13860e322d82ce354c8c0d0eb0f279ca63b3c","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json","role":"wgs_copies","sha256":"3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66"},{"bytes":47714,"git_blob_sha":"67c7070e6678223b5de63635d4b18f110500a742","path":"topics/visible-flex-exact-nearby/notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json","role":"wdg_actual","sha256":"04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":16027,"git_blob_sha":"0c1a3593617a4134ea875697a268b7b6eea3bb3b","path":"topics/visible-flex-exact-nearby/results/R133-supplement-sharp-Bernstein-and-integrated-finite-flow-jets.md","role":"proof_WBF","sha256":"2dd1cdc598fde3ca47ca1cf0d787fdc60b9ced5601654865cfc3736cdba6c323"}''')
OLD_FIELDSETS = json.loads(r'''{"wdg_actual":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"],"wgs_copies":["actual_scientific_checkout_commit","complete","complete_readonly_input_projection","copied_complete_local_coefficients","copied_complete_local_coefficients_sha256","copied_complete_original_scopes","copied_complete_original_scopes_sha256","copied_original_scalar_records","copied_original_scalar_records_sha256","copied_original_stage_records","copied_original_stage_records_sha256","copy_counts","input_manifest_sha256","kind","local_coefficient_qualification","math_module_sha256","original_input_sha256","public_repository","run_attempt","run_id","source_sha256","workflow_event_commit"],"wgs_main":["accepted_original_inputs","actual_mathematical_wall_seconds","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_free_first_transport_conclusion","complete_higher_flow_and_cut_conclusion","complete_local_regular_packet_conclusion","complete_named_global_graph_conclusion","complete_original_inputs_file","complete_strict_coefficient_conclusion","complete_strict_forcing_conclusion","complete_strict_geometry_conclusion","complete_strict_leading_conclusion","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"]}''')
ADMISSION_KEYS = json.loads(r'''{"wdg_actual":["accepted_old_inputs","actual_checkout_commit","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","completed_targets","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"],"wgs_copies":["actual_scientific_checkout_commit","complete","complete_readonly_input_projection","copied_complete_local_coefficients_sha256","copied_complete_original_scopes_sha256","copied_original_scalar_records_sha256","copied_original_stage_records_sha256","copy_counts","input_manifest_sha256","kind","local_coefficient_qualification","math_module_sha256","original_input_sha256","public_repository","run_attempt","run_id","source_sha256","workflow_event_commit"],"wgs_main":["accepted_original_inputs","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_original_inputs_file","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"]}''')
EXPECTED_ADMISSION_HASHES = json.loads(r'''{"wdg_actual":{"bytes":17777,"sha256":"90fc0c6f3b9a61bb09e33e7dfac70cc7da279c039f8f4e4bd5454e33c677daf5"},"wgs_copies":{"bytes":4181,"sha256":"8594ac62a5fe8e6e4a1214cf3e92f7c088757785c74aea5094502e6b6bd700f6"},"wgs_main":{"bytes":20608,"sha256":"db2c03a31cff6cbe8d64327bcc4c561cc19dc37ed8615f1d9ef5f58d3c9cadd3"}}''')
RECORD_SPECS = json.loads(r'''{"cut_composition_1":{"endpoint":"upper","path":["complete_new_graphs","complete_new_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_1_through_14",0],"role":"wdg_actual"},"cut_phase_1":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_1"],"role":"wgs_copies"},"cut_phase_10":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",5],"role":"wgs_main"},"cut_phase_11":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",6],"role":"wgs_main"},"cut_phase_12":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",7],"role":"wgs_main"},"cut_phase_13":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",8],"role":"wgs_main"},"cut_phase_14":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",9],"role":"wgs_main"},"cut_phase_15":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",10],"role":"wgs_main"},"cut_phase_2":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_2"],"role":"wgs_copies"},"cut_phase_3":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_3"],"role":"wgs_copies"},"cut_phase_4":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_4"],"role":"wgs_copies"},"cut_phase_5":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",0],"role":"wgs_main"},"cut_phase_6":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",1],"role":"wgs_main"},"cut_phase_7":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",2],"role":"wgs_main"},"cut_phase_8":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",3],"role":"wgs_main"},"cut_phase_9":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","cut_phase_orders_5_through_15",4],"role":"wgs_main"},"cut_relative_1":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",0],"role":"wdg_actual"},"cut_relative_10":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",9],"role":"wdg_actual"},"cut_relative_11":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",10],"role":"wdg_actual"},"cut_relative_12":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",11],"role":"wdg_actual"},"cut_relative_13":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",12],"role":"wdg_actual"},"cut_relative_14":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",13],"role":"wdg_actual"},"cut_relative_2":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",1],"role":"wdg_actual"},"cut_relative_3":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",2],"role":"wdg_actual"},"cut_relative_4":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",3],"role":"wdg_actual"},"cut_relative_5":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",4],"role":"wdg_actual"},"cut_relative_6":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",5],"role":"wdg_actual"},"cut_relative_7":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",6],"role":"wdg_actual"},"cut_relative_8":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",7],"role":"wdg_actual"},"cut_relative_9":{"endpoint":"upper","path":["complete_new_graphs","complete_new_relative_cut_omega_conclusion","new_records","ordinary_relative_cut_omega_orders_1_through_14",8],"role":"wdg_actual"},"flow_1":{"endpoint":"upper","path":["copied_original_scalar_records","flow_1"],"role":"wgs_copies"},"phase_1":{"endpoint":"upper","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",0],"role":"wgs_main"},"strict_phase_lower":{"endpoint":"lower","path":["complete_higher_flow_and_cut_conclusion","strict_phase_lower"],"role":"wgs_main"}}''')
SCOPE_SPECS = json.loads(r'''{"complete_original_nine_scope_objects":{"mode":"complete_non_ball_projection","path":["copied_complete_original_scopes"],"role":"wgs_copies"},"wdg_complete_graph_qualifications":{"mode":"complete_non_ball_projection","path":["complete_new_graphs"],"role":"wdg_actual"},"wdg_complete_saved_graph_counts":{"mode":"exact","path":["saved_record_counts"],"role":"wdg_actual"},"wdg_original_AST_evidence":{"mode":"exact","path":["original_source_AST_evidence"],"role":"wdg_actual"},"wdg_parameters":{"mode":"exact","path":["parameters"],"role":"wdg_actual"},"wdg_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wdg_actual"},"wgs_complete_original_copy_counts":{"mode":"exact","path":["copy_counts"],"role":"wgs_copies"},"wgs_derivative_certificate":{"mode":"exact","path":["complete_derivative_request_certificate"],"role":"wgs_main"},"wgs_higher_flow_qualifications":{"mode":"complete_non_ball_projection","path":["complete_higher_flow_and_cut_conclusion"],"role":"wgs_main"},"wgs_original_AST_evidence":{"mode":"exact","path":["original_source_AST_evidence"],"role":"wgs_main"},"wgs_parameters":{"mode":"exact","path":["parameters"],"role":"wgs_main"},"wgs_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wgs_main"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"bc53ed42da3d2c81c70903c0517e9d4d39fd49ed99de590044b35d09bb62e65e"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''3847''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"e5d8a593d9a29998d4c1bb96165b1098225f3f7d145b44489f8d7d4857d00d2a"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''21153''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"4ef523df6fd6f1a275fcf0399ae90ee51da2d4b23f1a0d7ad4a8f278a525a558"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''15709''')
PARAMETERS = json.loads(r'''{"actual_drift_label_bandwidth":192,"actual_drift_physical_bandwidth":768,"arithmetic_bits":320,"copied_original_qualification_objects":12,"copied_original_records":33,"decimal_record_digits":75,"first_flow_budget_qualification":"complete WX positive algorithm bounds exp(integral D) on every shorter interval and both orientations","fixed_intrinsic_parameter":"eta_0","graph_original_copies":0,"history_inputs":0,"internal_exact_combinatorics_not_scientific_targets":true,"maximum_relative_omega_angular_order":14,"new_exponentials":0,"new_flow_orders":[2,15],"new_fractional_powers":0,"new_graphs":5,"new_logarithms":0,"new_phase_orders":[2,15],"new_quadratures":0,"new_record_count":83,"new_square_roots":0,"old_complete_files":3,"old_scientific_calls":0,"old_target_recomputations":0,"only_denominator_records":["strict_phase_lower"],"original_WDG_cut_relative_orders_read":[1,14],"original_cut_phase_orders_read":[1,15],"original_first_flow_phase_cut_composition_read_only":["flow_1","phase_1","cut_composition_1"],"original_true_interfaces":3070,"physical_derivative_frequency":4,"physical_mean_coordinates":2,"physical_period":"pi/2","relative_derivative_convention":"ordinary absolute angular derivative divided by the same positive actual function","root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"selected_original_real_member_only":true,"sharp_majorant":"finite positive Stirling polynomial of directed upper(flow_1)-1; physical bandwidth 768","strict_cut":"76285779072683/320000000000000","strict_interval":["0","76285779072683/320000000000000"],"total_graph_scalar_slots":83}''')
RETAINED_SCOPE = json.loads(r'''{"F_minus_one_is_nonnegative_budget_parameter_not_an_operator_difference":true,"WDG_complete_80_target_graph_not_recomputed":true,"actual_96_columns_exist_signed_normalization_uncomputed":true,"all_Bell_terms_and_all_original_seams_retained":true,"all_four_waist_endpoints_positive_root_response_and_finite_factors_retained":true,"all_shorter_both_orientations_both_characteristics_and_drift":true,"finite_Schur_inverse_proved":false,"full_H_inverse_mu_inverse_G_and_forcing_still_separate":true,"geometry_sup_not_relabelled_Wiener_A0":true,"local_root_domain_and_analytic_packet_remain_separate":true,"new_flow_and_phase_bounds_are_distinct_complete_positive_candidates":true,"new_mixed_jet_numerical_graph_proved":false,"new_received_error_or_whole_bound_proved":false,"no_difference_of_independent_phase_upper_bounds":true,"no_flow_ODE_or_coefficient_recomputation":true,"no_fractional_power_of_complex_T":true,"no_numerical_logarithm_exponential_or_trigonometric_evaluation":true,"nonlinear_solution_proved":false,"nu_Theta_radial_head_and_full_matching_retained":true,"old_437_target_graph_and_original_failures_not_repeated":true,"ordinary_relative_output_only_converted_to_normalized_by_factorial_once":true,"original_F1_P1_K1_and_all_cut_records_read_only":true,"original_first_positive_comparison_budget_bounds_exp_integral_D":true,"physical_J_Jr_two_means_mean_ODE_and_all_source_ports_retained":true,"physical_incoming_inverse_proved":false,"positive_cut_atom_and_complete_ordinary_dr_integral_retained":true,"probability_measure_used_only_after_actual_derivative_identity":true,"relative_omega_order_fifteen_not_claimed":true,"same_selected_real_reference_and_original_intrinsic_parameter":true,"sharp_Bernstein_only_on_complete_known_reference_support":true,"true_root_and_cut_not_moved":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_new_sharp_flow_conclusion","complete_new_sharp_phase_conclusion","complete_new_sharp_relative_bulk_conclusion","complete_new_sharp_transport_relative_conclusion","complete_new_sharp_relative_omega_conclusion"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_new_sharp_flow_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_flow_conclusion_v1","maximum_angular_order":15,"new_records":{"ordinary_flow_orders_2_through_15":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":false,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_phase_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_phase_conclusion_v1","maximum_angular_order":15,"new_records":{"ordinary_phase_orders_2_through_15":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":false,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_relative_bulk_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_relative_bulk_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_relative_bulk_x_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_relative_omega_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_relative_omega_conclusion_v1","maximum_angular_order":14,"new_records":{"complete_strict_relative_omega_angular_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_transport_relative_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_transport_relative_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_bulk_contribution_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"ordinary_cut_contribution_orders_2_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_new_sharp_flow_conclusion":14,"complete_new_sharp_phase_conclusion":14,"complete_new_sharp_relative_bulk_conclusion":14,"complete_new_sharp_relative_omega_conclusion":14,"complete_new_sharp_transport_relative_conclusion":27}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_new_sharp_flow_conclusion":14,"complete_new_sharp_phase_conclusion":14,"complete_new_sharp_relative_bulk_conclusion":14,"complete_new_sharp_relative_omega_conclusion":14,"complete_new_sharp_transport_relative_conclusion":27}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":3,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":5,"new_logarithms":0,"new_quadratures":0,"new_records_saved":83,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":12,"original_record_objects_copied":33,"original_records_copied_in_graphs":0}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","seven_current_inputs_and_two_AST_identities","three_complete_original_files_byte_identical","original_WGS_437_and_WDG_80_science_complete","full_WGS_pair_and_WDG_predecessor_binding","original_WX_positive_integrated_first_budget_and_reference_bandwidth","all_33_original_records_and_twelve_scopes_preserved","one_positive_lower_and_nonnegative_Fminus1_budget","complete_new_sharp_flow_conclusion","complete_new_sharp_phase_conclusion","complete_new_sharp_relative_bulk_conclusion","complete_new_sharp_transport_relative_conclusion","complete_new_sharp_relative_omega_conclusion","complete_sharp_flow15_phase15_relative14_scope_and_no_old_work","all_current_inputs_still_identical","complete_83_record_scientific_graph_and_prefix"]''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","copied_original_scalar_records","copied_original_scopes","complete_new_graphs","current_target","completed_targets","saved_record_counts","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized"]''')
OLD_WDG_GRAPH_SHAPES = json.loads(r'''{"complete_new_cut_T_high_angular_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_drift_flow":true,"kind":"complete_new_cut_T_high_angular_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_cut_T_orders_5_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":false,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_bulk_x_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_drift_flow":true,"kind":"complete_new_relative_bulk_x_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_relative_bulk_x_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_cut_omega_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_drift_flow":true,"kind":"complete_new_relative_cut_omega_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_relative_cut_omega_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_omega_angular_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_drift_flow":true,"kind":"complete_new_relative_omega_angular_conclusion_v1","maximum_angular_order":14,"new_records":{"complete_strict_relative_omega_angular_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_transport_relative_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_drift_flow":true,"kind":"complete_new_transport_relative_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_bulk_contribution_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"ordinary_cut_contribution_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]}}''')
OLD_WDG_RECORD_SPECS = json.loads(r'''{"cut_t_1":{"endpoint":"upper","meaning":"already saved ordinary cut derivative 1 of t=-T","path":["copied_original_scalar_records","cut_t_1"],"role":"wgs_copies"},"cut_t_2":{"endpoint":"upper","meaning":"already saved ordinary cut derivative 2 of t=-T","path":["copied_original_scalar_records","cut_t_2"],"role":"wgs_copies"},"cut_t_3":{"endpoint":"upper","meaning":"already saved ordinary cut derivative 3 of t=-T","path":["copied_original_scalar_records","cut_t_3"],"role":"wgs_copies"},"cut_t_4":{"endpoint":"upper","meaning":"already saved ordinary cut derivative 4 of t=-T","path":["copied_original_scalar_records","cut_t_4"],"role":"wgs_copies"},"flow_1":{"endpoint":"upper","meaning":"ordinary physical angular derivative 1 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["copied_original_scalar_records","flow_1"],"role":"wgs_copies"},"flow_10":{"endpoint":"upper","meaning":"ordinary physical angular derivative 10 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",5],"role":"wgs_main"},"flow_11":{"endpoint":"upper","meaning":"ordinary physical angular derivative 11 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",6],"role":"wgs_main"},"flow_12":{"endpoint":"upper","meaning":"ordinary physical angular derivative 12 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",7],"role":"wgs_main"},"flow_13":{"endpoint":"upper","meaning":"ordinary physical angular derivative 13 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",8],"role":"wgs_main"},"flow_14":{"endpoint":"upper","meaning":"ordinary physical angular derivative 14 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",9],"role":"wgs_main"},"flow_2":{"endpoint":"upper","meaning":"ordinary physical angular derivative 2 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["copied_original_scalar_records","flow_2"],"role":"wgs_copies"},"flow_3":{"endpoint":"upper","meaning":"ordinary physical angular derivative 3 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["copied_original_scalar_records","flow_3"],"role":"wgs_copies"},"flow_4":{"endpoint":"upper","meaning":"ordinary physical angular derivative 4 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["copied_original_scalar_records","flow_4"],"role":"wgs_copies"},"flow_5":{"endpoint":"upper","meaning":"ordinary physical angular derivative 5 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",0],"role":"wgs_main"},"flow_6":{"endpoint":"upper","meaning":"ordinary physical angular derivative 6 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",1],"role":"wgs_main"},"flow_7":{"endpoint":"upper","meaning":"ordinary physical angular derivative 7 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",2],"role":"wgs_main"},"flow_8":{"endpoint":"upper","meaning":"ordinary physical angular derivative 8 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",3],"role":"wgs_main"},"flow_9":{"endpoint":"upper","meaning":"ordinary physical angular derivative 9 of every shorter directed flow; drift-only extension by WDG variational theorem","path":["complete_higher_flow_and_cut_conclusion","flow_orders_5_through_15",4],"role":"wgs_main"},"phase_10":{"endpoint":"upper","meaning":"ordinary physical angular derivative 10 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",9],"role":"wgs_main"},"phase_11":{"endpoint":"upper","meaning":"ordinary physical angular derivative 11 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",10],"role":"wgs_main"},"phase_12":{"endpoint":"upper","meaning":"ordinary physical angular derivative 12 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",11],"role":"wgs_main"},"phase_13":{"endpoint":"upper","meaning":"ordinary physical angular derivative 13 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",12],"role":"wgs_main"},"phase_14":{"endpoint":"upper","meaning":"ordinary physical angular derivative 14 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",13],"role":"wgs_main"},"phase_15":{"endpoint":"upper","meaning":"ordinary physical angular derivative 15 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",14],"role":"wgs_main"},"phase_2":{"endpoint":"upper","meaning":"ordinary physical angular derivative 2 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",1],"role":"wgs_main"},"phase_3":{"endpoint":"upper","meaning":"ordinary physical angular derivative 3 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",2],"role":"wgs_main"},"phase_4":{"endpoint":"upper","meaning":"ordinary physical angular derivative 4 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",3],"role":"wgs_main"},"phase_5":{"endpoint":"upper","meaning":"ordinary physical angular derivative 5 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",4],"role":"wgs_main"},"phase_6":{"endpoint":"upper","meaning":"ordinary physical angular derivative 6 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",5],"role":"wgs_main"},"phase_7":{"endpoint":"upper","meaning":"ordinary physical angular derivative 7 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",6],"role":"wgs_main"},"phase_8":{"endpoint":"upper","meaning":"ordinary physical angular derivative 8 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",7],"role":"wgs_main"},"phase_9":{"endpoint":"upper","meaning":"ordinary physical angular derivative 9 of both true strict phases","path":["complete_higher_flow_and_cut_conclusion","complete_strict_phase_angular_orders_1_through_15",8],"role":"wgs_main"},"strict_phase_lower":{"endpoint":"lower","meaning":"strict positive lower for both p_sigma=Phi_sigma_phi","path":["complete_higher_flow_and_cut_conclusion","strict_phase_lower"],"role":"wgs_main"},"t_cut_lower":{"endpoint":"lower","meaning":"strictly positive real lower for t=-T at the original cut","path":["copied_original_scalar_records","t_cut_lower"],"role":"wgs_copies"},"y_cut":{"endpoint":"upper","meaning":"whole holomorphic modulus of T_phi on the original cut strip 3/128","path":["copied_original_scalar_records","y_cut"],"role":"wgs_copies"}}''')
OLD_WDG_RECORD_IDENTITY = json.loads(r'''{"bytes":3858,"sha256":"37315df6f0535d9fc8f742c1b753077e4d14afba64cb78a44930d01aae5112ce"}''')
OLD_WDG_SCOPE_IDENTITY = json.loads(r'''{"bytes":15638,"sha256":"3d35f2addeadee0a70e8678f038835ec028dfc6f683f648d0cf7e961fc880c3a"}''')
OLD_WDG_ACCEPTED_IDENTITY = json.loads(r'''{"bytes":10763,"sha256":"59ca5d725035887f3c8cce9860adf992afdce766bb472e774692bf5b928b7368"}''')
WDG_RECEIPT_KEYS = json.loads(r'''["kind","problem_id","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","runtime","arithmetic_bits","complete","proved","actual_returncode","stage","failure","original_source_AST_evidence","actual_progress","gates","saved_record_counts","completed_targets","current_target","automatic_retry_authorized"]''')


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
    prior = docs["wdg_actual"]
    return {
        "complete_original_file_receipts": [
            five_fields(files[spec["role"]]) for spec in EXPECTED_OLD_FILES],
        "complete_WDG_mathematical_receipt": {
            key: copy.deepcopy(prior[key]) for key in WDG_RECEIPT_KEYS},
        "complete_WGS_mathematical_and_original_admission":
            copy.deepcopy(prior["accepted_old_inputs"]),
        "complete_original_WDG_scalar_copy_reference":
            complete_object_reference(docs, "wdg_actual", ["copied_original_scalar_records"]),
        "complete_original_WDG_scope_reference":
            complete_object_reference(docs, "wdg_actual", ["copied_original_scopes"]),
        "all_original_WGS_24_gates_and_437_slots_verified": True,
        "all_original_WDG_16_gates_and_80_slots_verified": True,
        "original_positive_WX_integrated_first_budget_verified": True,
        "WDG_full_WGS_predecessor_binding_verified": True,
        "original_F1_P1_and_K1_read_without_recomputation": True,
        "original_historical_scientific_success_and_formatter_failure_preserved": True,
        "old_producer_imports": 0, "old_scientific_calls": 0,
        "old_historical_files_restored": 0}

def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(digest(manifest_raw) == manifest_sha, "manifest CLI identity")
    manifest = exact_json(manifest_raw)
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_WBF", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 7
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 7,
            "seven complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "original input pin differs")
    require(same_json(files["proof_WBF"], EXPECTED_PROOF), "published WBF pin")
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
                "whole original status identity parameters gates or scopes differ")
    main, companion = docs["wgs_main"], docs["wgs_copies"]
    require(main["kind"] == "actual_complete_global_fold_free_transport_finite_jets_v1"
            and main["complete"] is True and main["proved"] is True
            and main["actual_returncode"] == 0 and main["failure"] is None
            and main["stage"] == "complete"
            and main["run_id"] == "43820816332" and main["run_attempt"] == "1"
            and main["arithmetic_bits"] == 320
            and main["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"},
            "complete original WGS mathematical result")
    require(len(main["gates"]) == 24
            and all(set(g) == {"name", "passed"} and g["passed"] is True
                    for g in main["gates"]), "entire original WGS gate list")
    progress = main["actual_progress"]
    require(progress["new_scalar_slots_saved"] == 437
            and progress["old_scientific_targets_recomputed"] == 0
            and progress["old_producer_imports_or_calls"] == 0
            and progress["old_rays_flows_exponentials_evaluated"] == 0,
            "complete original WGS graph and no old rerun")
    counts = main["planned_shape"]["new_graph_slot_counts"]
    require(sum(counts.values()) == 437
            and all(scalar_record_count(main[key]) == count for key, count in counts.items()),
            "all eight original complete graph counts")
    require(companion["kind"] ==
            "complete_original_inputs_for_global_fold_free_transport_finite_jets_v1"
            and companion["complete"] is True
            and companion["complete_readonly_input_projection"] is True,
            "whole original companion")
    shared = ("run_id", "run_attempt", "workflow_event_commit",
              "actual_scientific_checkout_commit", "source_sha256",
              "math_module_sha256", "input_manifest_sha256", "public_repository")
    require(all(same_json(main[key], companion[key]) for key in shared),
            "same original run source math manifest checkout event repository")
    require(main["source_sha256"] ==
            "d32fe912b7ebcb1ee6050589cf06ebf5512475a9c2636c584092c2d12be51e4f"
            and main["math_module_sha256"] ==
            "cb9c9aa0f7e5749967ece4e51210f359b4c58eecc7f83a05040607543ac47621",
            "exact original finite recurrence identities")
    require(main["complete_original_inputs_file"] == {
                "filename": "complete-original-inputs.json",
                "bytes": files["wgs_copies"]["bytes"],
                "sha256": files["wgs_copies"]["sha256"]},
            "complete original companion byte binding")
    for key in ("copied_original_scalar_records", "copied_original_stage_records",
                "copied_complete_original_scopes", "copied_complete_local_coefficients"):
        require(digest(canonical(companion[key])) == companion[key + "_sha256"],
                "whole original companion object hash")
    cc = companion["copy_counts"]
    require(cc["current_scalar_records"] == 66 and cc["stage_scalar_records"] == 40
            and cc["complete_scope_objects"] == 9
            and cc["complete_local_coefficient_objects"] == 1
            and cc["local_coefficient_ball_count"] == 72
            and scalar_record_count(companion["copied_original_scalar_records"]) == 66
            and scalar_record_count(companion["copied_original_stage_records"]) == 40
            and scalar_record_count(companion["copied_complete_local_coefficients"]) == 72
            and len(companion["copied_complete_original_scopes"]) == 9,
            "all old copies and their original shape kept")
    pp = main["parameters"]
    original_scopes = companion["copied_complete_original_scopes"]
    require(pp["fixed_intrinsic_parameter"] == PARAMETERS["fixed_intrinsic_parameter"]
            and pp["exact_strict_interval"] == PARAMETERS["strict_interval"]
            and pp["exact_strict_cut"] == PARAMETERS["strict_cut"]
            and pp["exact_root_interval"] == PARAMETERS["root_interval"]
            and pp["exact_fold_strip"] == "3/128"
            and pp["actual_original_interfaces"] == 3070
            and pp["maximum_total_degree"] == 15
            and pp["physical_drift_bandwidth"] == 768
            and pp["old_producer_execution_allowed"] is False,
            "same actual reference domain frequency and original interfaces")
    certificate = main["complete_derivative_request_certificate"]
    require(certificate["normalized_coefficients"] ==
            "ordinary derivative norm divided by a! b!"
            and certificate["phase_value_not_a_periodic_function"] is True
            and certificate["no_root_radial_three_bound_for_individual_Phi"] is True,
            "full original normalized mixed certificate and omitted phase value")
    high = main["complete_higher_flow_and_cut_conclusion"]
    require(high["all_shorter_intervals_both_branches_both_orientations"] is True
            and high["old_cut_phase_1_through_4_recomputed"] == 0
            and high["old_flow_1_through_4_recomputed"] == 0
            and len(high["flow_orders_5_through_15"]) == 11
            and len(high["complete_strict_phase_angular_orders_1_through_15"]) == 15,
            "complete original ordinary flow and individual phase orders")
    flow = original_scopes["wx_flow"]
    require(flow["every_shorter_interval_and_both_orientations"] is True
            and flow["inverse_flow_has_its_own_same_directed_bounds"] is True
            and flow["specific_positive_algorithm_lower_addends_used"] is True
            and flow["no_arbitrary_operator_norm_inversion"] is True
            and flow["known_drift_label_bandwidth"] == 192
            and flow["physical_derivative_frequency_factor"] == 4
            and flow["true_radial_interval"] == PARAMETERS["strict_interval"],
            "old positive variational envelope qualifies the additional drift flow")
    fa = original_scopes["fa_parameters"]
    dza = original_scopes["dza_parameters"]
    require(fa["exact_fold_strip"] == "3/128"
            and fa["exact_fold_radius"] == "3/8000"
            and fa["exact_strict_cut"] == PARAMETERS["strict_cut"]
            and fa["exact_real_delta_radius"] == "1/100000000"
            and fa["Airy_error_derivatives_taken"] is False
            and dza["exact_original_fold_strip"] == "3/128"
            and dza["physical_period"] == "pi/2"
            and dza["physical_frequency"] == "n=4|j|",
            "whole holomorphic cut strip and actual physical-angle convention")
    old_original = main["accepted_original_inputs"]["original_whole_mathematics"]
    require(old_original["mathematical_complete"] is True
            and old_original["mathematical_proved"] is True
            and old_original["mathematical_failure"] is None
            and old_original["publication_complete"] is False
            and old_original["publication_actual_returncode"] == 1
            and old_original["formatter_failure"]["type"] == "TypeError",
            "historical scientific success and formatter failure remain distinct")
    prior = docs["wdg_actual"]
    require(prior["kind"] == "complete_positive_drift_relative_omega_angular_bounds"
            and prior["complete"] is True and prior["proved"] is True
            and prior["actual_returncode"] == 0 and prior["failure"] is None
            and prior["stage"] == "complete"
            and prior["run_id"] == "43865837250" and prior["run_attempt"] == "1"
            and prior["arithmetic_bits"] == 320
            and prior["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"}
            and prior["automatic_retry_authorized"] is False,
            "complete immutable WDG mathematical result")
    require(prior["scientific_modules"] == {
                "science": "282efceb7bb0686d82e26bfef003c8c266f9a413872f4990489557252bcc941f"}
            and prior["manifest_sha256"] ==
                "a88caba5646ad8f0422f3a0d8d183983d737681d1c26f6c7b1a6a6920cff3132",
            "original WDG exact source and manifest")
    require(len(prior["gates"]) == 16
            and all(set(g) == {"name", "passed"} and g["passed"] is True
                    for g in prior["gates"]), "entire WDG gate list")
    require(complete_shape(prior["complete_new_graphs"], OLD_WDG_GRAPH_SHAPES)
            and sum(prior["saved_record_counts"].values()) == 80
            and all(scalar_record_count(prior["complete_new_graphs"][name]) == count
                    for name, count in prior["saved_record_counts"].items())
            and prior["current_target"] is None
            and prior["completed_targets"] == [
                "complete_new_cut_T_high_angular_conclusion",
                "complete_new_relative_cut_omega_conclusion",
                "complete_new_relative_bulk_x_conclusion",
                "complete_new_transport_relative_conclusion",
                "complete_new_relative_omega_angular_conclusion"],
            "all five old WDG graphs and all eighty saved targets")
    old_progress = prior["actual_progress"]
    require(old_progress["new_records_saved"] == 80
            and old_progress["new_graphs_completed"] == 5
            and old_progress["old_targets_recomputed"] == 0
            and old_progress["old_scientific_calls"] == 0
            and old_progress["original_records_copied_in_graphs"] == 0,
            "original WDG completion and no old rerun")
    for role in ("wgs_main", "wgs_copies"):
        require(prior["input_sha256"][role] == files[role]["sha256"]
                and prior["verified_original_inputs"][role] == {
                    "bytes": files[role]["bytes"], "sha256": files[role]["sha256"]},
                "WDG binds these exact two WGS files")
    old_records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
                   for alias, spec in OLD_WDG_RECORD_SPECS.items()}
    require(same_json(old_records, prior["copied_original_scalar_records"])
            and len(canonical(old_records)) == OLD_WDG_RECORD_IDENTITY["bytes"]
            and digest(canonical(old_records)) == OLD_WDG_RECORD_IDENTITY["sha256"],
            "complete original WDG thirty-five records unchanged")
    old_accepted = prior["accepted_old_inputs"]
    require(len(canonical(old_accepted)) == OLD_WDG_ACCEPTED_IDENTITY["bytes"]
            and digest(canonical(old_accepted)) == OLD_WDG_ACCEPTED_IDENTITY["sha256"]
            and same_json(old_accepted["complete_original_file_receipts"],
                          EXPECTED_OLD_FILES[:2])
            and same_json(old_accepted["complete_original_WGS_admission"],
                          main["accepted_original_inputs"])
            and same_json(old_accepted["complete_bound_companion_reference"],
                          main["complete_original_inputs_file"])
            and same_json(old_accepted["complete_companion_copy_counts"],
                          companion["copy_counts"])
            and all(same_json(main[key], value) for key, value in
                    old_accepted["complete_WGS_mathematical_receipt"].items()),
            "complete original WDG admission and actual WGS relation")
    require(same_json(companion["copied_original_scalar_records"]["flow_1"],
                      flow["complete_shorter_flow_derivative_upper"])
            and same_json(prior["copied_original_scalar_records"]["flow_1"],
                          companion["copied_original_scalar_records"]["flow_1"])
            and pp["drift_label_bandwidth"] == 192
            and dza["drift_label_bandwidth"] == 192
            and prior["parameters"]["strict_interval"] == PARAMETERS["strict_interval"]
            and prior["parameters"]["fixed_intrinsic_parameter"] == "eta_0"
            and prior["retained_scope"]["positive_cut_atom_and_complete_ordinary_dr_integral_retained"] is True
            and prior["retained_scope"]["probability_measure_used_only_after_actual_derivative_identity"] is True,
            "same positive integrated first budget known bandwidth and actual gap identity")
    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 33 and all(
                isinstance(v, dict) and set(v) == {"ball"} and isinstance(v["ball"], str)
                for v in records.values())
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all 33 complete original scalar objects retained")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(spec["mode"] in ("exact", "complete_non_ball_projection"), "scope mode")
        scopes[name] = (copy.deepcopy(value) if spec["mode"] == "exact"
                        else original_qualifications(value))
    require(len(scopes) == 12 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "all original consumed qualifications retained with array positions")
    original_wgs_scopes = {
        name: scopes[name] for name in (
            "wgs_parameters", "wgs_retained_scope", "wgs_derivative_certificate",
            "wgs_higher_flow_qualifications", "complete_original_nine_scope_objects",
            "wgs_original_AST_evidence", "wgs_complete_original_copy_counts")}
    require(same_json(original_wgs_scopes, prior["copied_original_scopes"])
            and len(canonical(original_wgs_scopes)) == OLD_WDG_SCOPE_IDENTITY["bytes"]
            and digest(canonical(original_wgs_scopes)) == OLD_WDG_SCOPE_IDENTITY["sha256"],
            "complete old WDG scope archive matched without duplicating it")
    accepted = accepted_original_inputs(docs, files)
    require(len(canonical(accepted)) == ORIGINAL_ACCEPTED_BYTES
            and digest(canonical(accepted)) == ORIGINAL_ACCEPTED_SHA,
            "complete old receipt and full admission retained")
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


# WBF: finite positive polynomial and Bell targets only; no old producer.
# All arrays below are ordinary physical-angle derivatives.

def graph_record(graphs, name, path):
    graph = graphs[name]
    require(graph["complete"] is True, "complete predecessor graph")
    return at(graph["new_records"], path)

def positive_bell_factory(values):
    cache = {}
    def bell(n, k):
        if n == 0:
            return arb(1) if k == 0 else arb(0)
        if k == 0 or n < k:
            return arb(0)
        key = (n, k)
        if key not in cache:
            total = arb(0)
            for j in range(1, n - k + 2):
                total += math.comb(n - 1, j - 1) * values[j] * bell(n - j, k - 1)
            cache[key] = norm_upper(total)
        return cache[key]
    return bell

def complete_sharp_flow(saved, graphs, emit):
    first = saved_upper(saved["flow_1"])
    require(first >= 1, "original positive integral comparison is at least one")
    excess = norm_upper(first - 1)
    stirling = [[0] * 16 for _ in range(16)]
    stirling[0][0] = 1
    for j in range(1, 16):
        for k in range(1, j + 1):
            stirling[j][k] = k * stirling[j - 1][k] + stirling[j - 1][k - 1]
    # Only F2..15 are new. F1 is the immutable integrated positive budget.
    for j in range(2, 16):
        total = arb(0)
        for k in range(1, j + 1):
            total += math.factorial(k - 1) * stirling[j][k] * excess ** k
        emit(["ordinary_flow_orders_2_through_15", j - 2],
             (768 ** (j - 1)) * total)

def sharp_flow_values(saved, graphs):
    values = {1: saved_upper(saved["flow_1"])}
    for j in range(2, 16):
        values[j] = saved_upper(graph_record(
            graphs, "complete_new_sharp_flow_conclusion",
            ["ordinary_flow_orders_2_through_15", j - 2]))
    return values

def complete_sharp_phase(saved, graphs, emit):
    flow = sharp_flow_values(saved, graphs)
    cut = {j: saved_upper(saved["cut_phase_" + str(j)]) for j in range(1, 16)}
    bell = positive_bell_factory(flow)
    # P1 is copied from the old complete WGS phase budget, never reevaluated.
    for j in range(2, 16):
        total = arb(0)
        for k in range(1, j + 1):
            total += cut[k] * bell(j, k)
        emit(["ordinary_phase_orders_2_through_15", j - 2], total)

def complete_sharp_bulk(saved, graphs, emit):
    gap = saved_positive_lower(saved["strict_phase_lower"])
    for b in range(1, 15):
        phase = saved_upper(graph_record(
            graphs, "complete_new_sharp_phase_conclusion",
            ["ordinary_phase_orders_2_through_15", b - 1]))
        emit(["ordinary_relative_bulk_x_orders_1_through_14", b - 1], phase / gap)

def complete_sharp_transport(saved, graphs, emit):
    flow = sharp_flow_values(saved, graphs)
    cut = {j: saved_upper(saved["cut_relative_" + str(j)]) for j in range(1, 15)}
    bulk = {j: saved_upper(graph_record(
        graphs, "complete_new_sharp_relative_bulk_conclusion",
        ["ordinary_relative_bulk_x_orders_1_through_14", j - 1]))
        for j in range(1, 15)}
    bell = positive_bell_factory(flow)
    # The completed K1=C1*F1 is read later; no duplicate multiplication here.
    for b in range(2, 15):
        total = arb(0)
        for k in range(1, b + 1):
            total += cut[k] * bell(b, k)
        emit(["ordinary_cut_contribution_orders_2_through_14", b - 2], total)
    for b in range(1, 15):
        total = arb(0)
        for k in range(1, b + 1):
            total += bulk[k] * bell(b, k)
        emit(["ordinary_bulk_contribution_orders_1_through_14", b - 1], total)

def complete_sharp_relative_omega(saved, graphs, emit):
    for b in range(1, 15):
        cut_record = (saved["cut_composition_1"] if b == 1 else graph_record(
            graphs, "complete_new_sharp_transport_relative_conclusion",
            ["ordinary_cut_contribution_orders_2_through_14", b - 2]))
        bulk_record = graph_record(
            graphs, "complete_new_sharp_transport_relative_conclusion",
            ["ordinary_bulk_contribution_orders_1_through_14", b - 1])
        emit(["complete_strict_relative_omega_angular_orders_1_through_14", b - 1],
             max(saved_upper(cut_record), saved_upper(bulk_record)))

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
        "complete_new_graphs": {},
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
        doc["actual_progress"]["complete_original_files_admitted"] = 3
        doc["actual_progress"]["original_record_objects_copied"] = 33
        doc["actual_progress"]["original_qualification_objects_copied"] = 12
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
        require(saved_upper(saved["flow_1"]) >= 1,
                "positive integral first budget at least one")
        gate(GATE_LABELS[7])
        doc["stage"] = "typed_read_only_inputs_admitted"
        publish()
        math_start = time.perf_counter()
        operations = (
            ("complete_new_sharp_flow_conclusion", complete_sharp_flow),
            ("complete_new_sharp_phase_conclusion", complete_sharp_phase),
            ("complete_new_sharp_relative_bulk_conclusion", complete_sharp_bulk),
            ("complete_new_sharp_transport_relative_conclusion", complete_sharp_transport),
            ("complete_new_sharp_relative_omega_conclusion", complete_sharp_relative_omega))
        require([name for name, _ in operations] == ORDERED_GRAPH_NAMES, "complete new graph order")
        for name, function in operations:
            emit = start_graph(name)
            function(saved, doc["complete_new_graphs"], emit)
            finish_graph(name)
        final = doc["complete_new_graphs"][ORDERED_GRAPH_NAMES[-1]]
        require(final["complete"] is True
                and final["ordinary_physical_angular_derivatives"] is True
                and final["maximum_angular_order"] == 14
                and len(final["new_records"][
                    "complete_strict_relative_omega_angular_orders_1_through_14"]) == 14,
                "only complete ordinary relative fourteen-derivative output")
        gate(GATE_LABELS[13])
        for role, spec in work["files"].items():
            require(check_file(work["root"], spec) == work["raw"][role],
                    "current input changed during new scalar work")
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "manifest changed during new scalar work")
        gate(GATE_LABELS[14])
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
