"""WJR: complete relative-Jacobian bounds from two immutable successful receipts."""
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
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_flow_Jacobian.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py"''')
KIND = json.loads(r'''"complete_relative_flow_Jacobian_and_positive_phase_ratio_bounds"''')
PROBLEM_ID = json.loads(r'''"same_selected_relative_Jacobian_phase_average_omega14_v1"''')
PREFLIGHT_KIND = json.loads(r'''"complete_relative_flow_Jacobian_and_positive_phase_ratio_bounds_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''90000''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''512''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''2048''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":72251,"git_blob_sha":"32ff92c516fcc5c43f3619930d4845d294289270","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json","role":"wgs_main","sha256":"8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"},{"bytes":59417,"git_blob_sha":"df5ea6fff610d70ad98fbebc9dd004d24388ce86","path":"topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json","role":"wbf_actual","sha256":"87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":19752,"git_blob_sha":"b6cd802c613f7ec193329af609c63f59a6efded3","path":"topics/visible-flex-exact-nearby/results/R133-supplement-relative-flow-Jacobians-and-positive-phase-ratio-bounds.md","role":"proof_WJR","sha256":"741df919addd04766685724f1e6d131eef8b03bc6875f9a50ff7de9ad5061c2f"}''')
OLD_FIELDSETS = json.loads(r'''{"wbf_actual":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"],"wgs_main":["accepted_original_inputs","actual_mathematical_wall_seconds","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_free_first_transport_conclusion","complete_higher_flow_and_cut_conclusion","complete_local_regular_packet_conclusion","complete_named_global_graph_conclusion","complete_original_inputs_file","complete_strict_coefficient_conclusion","complete_strict_forcing_conclusion","complete_strict_geometry_conclusion","complete_strict_leading_conclusion","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"]}''')
ADMISSION_KEYS = json.loads(r'''{"wbf_actual":["accepted_old_inputs","actual_checkout_commit","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","completed_targets","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"],"wgs_main":["accepted_original_inputs","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_original_inputs_file","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"]}''')
EXPECTED_ADMISSION_HASHES = json.loads(r'''{"wbf_actual":{"bytes":23545,"sha256":"3c7deeae1d772ba305730c2e6698a6d008f96009ff8cea214c67dd7db5a58b8c"},"wgs_main":{"bytes":20608,"sha256":"db2c03a31cff6cbe8d64327bcc4c561cc19dc37ed8615f1d9ef5f58d3c9cadd3"}}''')
RECORD_SPECS = json.loads(r'''{"cut_composition_1":{"endpoint":"upper","path":["copied_original_scalar_records","cut_composition_1"],"role":"wbf_actual"},"cut_composition_10":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",8],"role":"wbf_actual"},"cut_composition_11":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",9],"role":"wbf_actual"},"cut_composition_12":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",10],"role":"wbf_actual"},"cut_composition_13":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",11],"role":"wbf_actual"},"cut_composition_14":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",12],"role":"wbf_actual"},"cut_composition_2":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",0],"role":"wbf_actual"},"cut_composition_3":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",1],"role":"wbf_actual"},"cut_composition_4":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",2],"role":"wbf_actual"},"cut_composition_5":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",3],"role":"wbf_actual"},"cut_composition_6":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",4],"role":"wbf_actual"},"cut_composition_7":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",5],"role":"wbf_actual"},"cut_composition_8":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",6],"role":"wbf_actual"},"cut_composition_9":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_transport_relative_conclusion","new_records","ordinary_cut_contribution_orders_2_through_14",7],"role":"wbf_actual"},"cut_phase_10":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_10"],"role":"wbf_actual"},"cut_phase_11":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_11"],"role":"wbf_actual"},"cut_phase_12":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_12"],"role":"wbf_actual"},"cut_phase_13":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_13"],"role":"wbf_actual"},"cut_phase_14":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_14"],"role":"wbf_actual"},"cut_phase_15":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_15"],"role":"wbf_actual"},"cut_phase_2":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_2"],"role":"wbf_actual"},"cut_phase_3":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_3"],"role":"wbf_actual"},"cut_phase_4":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_4"],"role":"wbf_actual"},"cut_phase_5":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_5"],"role":"wbf_actual"},"cut_phase_6":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_6"],"role":"wbf_actual"},"cut_phase_7":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_7"],"role":"wbf_actual"},"cut_phase_8":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_8"],"role":"wbf_actual"},"cut_phase_9":{"endpoint":"upper","path":["copied_original_scalar_records","cut_phase_9"],"role":"wbf_actual"},"cut_phase_lower":{"endpoint":"lower","path":["complete_higher_flow_and_cut_conclusion","cut_phase_lower"],"role":"wgs_main"},"flow_1":{"endpoint":"upper","path":["copied_original_scalar_records","flow_1"],"role":"wbf_actual"},"flow_10":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",8],"role":"wbf_actual"},"flow_11":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",9],"role":"wbf_actual"},"flow_12":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",10],"role":"wbf_actual"},"flow_13":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",11],"role":"wbf_actual"},"flow_14":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",12],"role":"wbf_actual"},"flow_2":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",0],"role":"wbf_actual"},"flow_3":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",1],"role":"wbf_actual"},"flow_4":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",2],"role":"wbf_actual"},"flow_5":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",3],"role":"wbf_actual"},"flow_6":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",4],"role":"wbf_actual"},"flow_7":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",5],"role":"wbf_actual"},"flow_8":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",6],"role":"wbf_actual"},"flow_9":{"endpoint":"upper","path":["complete_new_graphs","complete_new_sharp_flow_conclusion","new_records","ordinary_flow_orders_2_through_15",7],"role":"wbf_actual"}}''')
SCOPE_SPECS = json.loads(r'''{"complete_original_WBF_scope_archive":{"mode":"exact","path":["copied_original_scopes"],"role":"wbf_actual"},"wbf_complete_graph_qualifications":{"mode":"complete_non_ball_projection","path":["complete_new_graphs"],"role":"wbf_actual"},"wbf_complete_saved_graph_counts":{"mode":"exact","path":["saved_record_counts"],"role":"wbf_actual"},"wbf_original_AST_evidence":{"mode":"exact","path":["original_source_AST_evidence"],"role":"wbf_actual"},"wbf_parameters":{"mode":"exact","path":["parameters"],"role":"wbf_actual"},"wbf_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wbf_actual"},"wgs_higher_flow_qualifications":{"mode":"complete_non_ball_projection","path":["complete_higher_flow_and_cut_conclusion"],"role":"wgs_main"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"5802fe40aa3c5c97cc43d2dd33d585d8dc93e1645f72137d4913fce5511228ce"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''5005''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"ca0833a5d3dfe73575e871c607d2f6435824e12a4ee360f17ae3f101690143d4"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''27960''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"5e1d7dbe6ec66c06e8b2974e90f08c8229f38336c16b8d33625e35057b178b27"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''20412''')
PARAMETERS = json.loads(r'''{"actual_drift_label_bandwidth":192,"actual_drift_physical_bandwidth":768,"arithmetic_bits":320,"copied_original_qualification_objects":7,"copied_original_records":43,"cut_phase_lower_is_actual_cut_lower":true,"decimal_record_digits":75,"first_flow_budget_qualification":"complete WX positive algorithm bounds exp(integral D) on every shorter interval and both orientations","fixed_intrinsic_parameter":"eta_0","graph_original_copies":0,"history_inputs":0,"internal_exact_combinatorics_not_scientific_targets":true,"maximum_relative_Jacobian_angular_order":14,"maximum_relative_omega_angular_order":14,"maximum_relative_phase_and_average_angular_order":14,"new_exponentials":0,"new_fractional_powers":0,"new_graphs":4,"new_logarithms":0,"new_quadratures":0,"new_record_count":56,"new_square_roots":0,"old_complete_files":2,"old_scientific_calls":0,"old_target_recomputations":0,"only_denominator_records":["cut_phase_lower"],"original_absolute_flow_orders_read":[1,14],"original_complete_cut_composition_orders_read":[1,14],"original_cut_phase_orders_read":[2,15],"original_true_interfaces":3070,"physical_derivative_frequency":4,"physical_mean_coordinates":2,"physical_period":"pi/2","relative_Jacobian_majorant":"768^b sum_{k=1}^b k! S(b,k) (upper(flow_1)-1)^k; exact actual quotient established before norms","relative_derivative_convention":"ordinary absolute angular derivative divided by the same positive actual function","root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"selected_original_real_member_only":true,"strict_cut":"76285779072683/320000000000000","strict_interval":["0","76285779072683/320000000000000"],"total_graph_scalar_slots":56}''')
RETAINED_SCOPE = json.loads(r'''{"F_minus_one_is_nonnegative_budget_parameter_not_an_operator_difference":true,"Stirling_relative_Jacobian_polynomial_has_only_positive_terms":true,"actual_96_columns_exist_signed_normalization_uncomputed":true,"actual_positive_Jacobian_divided_before_norms":true,"all_Bell_terms_and_all_original_seams_retained":true,"all_four_waist_endpoints_positive_root_response_and_finite_factors_retained":true,"all_shorter_both_orientations_both_characteristics_and_drift":true,"both_positive_phases_and_their_average_share_one_complete_relative_bound":true,"complete_cut_phase_lower_used_without_global_phase_lower_loss":true,"complete_original_WBF_cut_contribution_retained":true,"finite_Schur_inverse_proved":false,"full_H_inverse_mu_inverse_G_and_forcing_still_separate":true,"geometry_sup_not_relabelled_Wiener_A0":true,"local_root_domain_and_analytic_packet_remain_separate":true,"new_mixed_jet_numerical_graph_proved":false,"new_received_error_or_whole_bound_proved":false,"no_extra_factor_two_for_positive_phase_average":true,"no_numerical_logarithm_exponential_trigonometric_or_ODE_evaluation":true,"no_ratio_of_independent_saved_upper_bounds":true,"nonlinear_solution_proved":false,"nu_Theta_radial_head_and_full_matching_retained":true,"old_WBF83_WDG80_WGS437_targets_and_original_failures_not_repeated":true,"ordinary_relative_output_only_converted_to_normalized_by_factorial_once":true,"original_WX_F1_is_positive_integrated_comparison_not_generic_norm":true,"original_absolute_flow_phase_cut_and_composition_records_read_only":true,"physical_J_Jr_two_means_mean_ODE_and_all_source_ports_retained":true,"physical_incoming_inverse_proved":false,"positive_cut_atom_and_complete_ordinary_dr_integral_retained":true,"probability_measure_used_only_after_actual_derivative_identity":true,"relative_omega_order_fifteen_not_claimed":true,"same_selected_real_reference_and_original_intrinsic_parameter":true,"true_root_and_cut_not_moved":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_new_relative_Jacobian_conclusion","complete_new_positive_phase_average_ratio_conclusion","complete_new_relative_bulk_transport_conclusion","complete_new_relative_omega_conclusion"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_new_positive_phase_average_ratio_conclusion":{"actual_positive_Jacobian_divided_before_norms":true,"common_positive_phase_average_ratio":true,"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_positive_phase_average_ratio_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_common_positive_phase_and_average_ratios_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_Jacobian_conclusion":{"actual_positive_Jacobian_divided_before_norms":true,"common_positive_phase_average_ratio":false,"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_relative_Jacobian_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_relative_Jacobian_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_bulk_transport_conclusion":{"actual_positive_Jacobian_divided_before_norms":true,"common_positive_phase_average_ratio":true,"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_relative_bulk_transport_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_bulk_contribution_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_relative_omega_conclusion":{"actual_positive_Jacobian_divided_before_norms":true,"common_positive_phase_average_ratio":true,"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_relative_omega_conclusion_v1","maximum_angular_order":14,"new_records":{"complete_strict_relative_omega_angular_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"strict_interval":["0","76285779072683/320000000000000"]}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_new_positive_phase_average_ratio_conclusion":14,"complete_new_relative_Jacobian_conclusion":14,"complete_new_relative_bulk_transport_conclusion":14,"complete_new_relative_omega_conclusion":14}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_new_positive_phase_average_ratio_conclusion":14,"complete_new_relative_Jacobian_conclusion":14,"complete_new_relative_bulk_transport_conclusion":14,"complete_new_relative_omega_conclusion":14}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":2,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":4,"new_logarithms":0,"new_quadratures":0,"new_records_saved":56,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":7,"original_record_objects_copied":43,"original_records_copied_in_graphs":0}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","six_current_inputs_and_two_AST_identities","two_complete_original_files_byte_identical","original_WGS_437_and_WBF_83_science_complete","full_WBF_WGS_predecessor_binding","original_WX_positive_integrated_budget_and_actual_cut_lower_scope","all_43_original_records_and_seven_scopes_preserved","one_true_cut_lower_and_nonnegative_Fminus1_budget","complete_new_relative_Jacobian_conclusion","complete_new_positive_phase_average_ratio_conclusion","complete_new_relative_bulk_transport_conclusion","complete_new_relative_omega_conclusion","complete_relative_Jacobian_phase_average_omega14_and_no_old_work","all_current_inputs_still_identical","complete_56_record_scientific_graph_and_prefix"]''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","copied_original_scalar_records","copied_original_scopes","complete_new_graphs","current_target","completed_targets","saved_record_counts","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized"]''')
OLD_WBF_GRAPH_SHAPES = json.loads(r'''{"complete_new_sharp_flow_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_flow_conclusion_v1","maximum_angular_order":15,"new_records":{"ordinary_flow_orders_2_through_15":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":false,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_phase_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_phase_conclusion_v1","maximum_angular_order":15,"new_records":{"ordinary_phase_orders_2_through_15":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":false,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_relative_bulk_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_relative_bulk_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_relative_bulk_x_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_relative_omega_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_relative_omega_conclusion_v1","maximum_angular_order":14,"new_records":{"complete_strict_relative_omega_angular_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]},"complete_new_sharp_transport_relative_conclusion":{"complete":true,"complete_original_cut_and_all_shorter_flow":true,"kind":"complete_new_sharp_transport_relative_conclusion_v1","maximum_angular_order":14,"new_records":{"ordinary_bulk_contribution_orders_1_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"ordinary_cut_contribution_orders_2_through_14":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"ordinary_physical_angular_derivatives":true,"relative_ratio":true,"sharp_Bernstein_integrated_majorant":true,"strict_interval":["0","76285779072683/320000000000000"]}}''')
OLD_WBF_RECORD_IDENTITY = json.loads(r'''{"bytes":3847,"sha256":"bc53ed42da3d2c81c70903c0517e9d4d39fd49ed99de590044b35d09bb62e65e"}''')
OLD_WBF_SCOPE_IDENTITY = json.loads(r'''{"bytes":21153,"sha256":"e5d8a593d9a29998d4c1bb96165b1098225f3f7d145b44489f8d7d4857d00d2a"}''')
OLD_WBF_ACCEPTED_IDENTITY = json.loads(r'''{"bytes":15709,"sha256":"4ef523df6fd6f1a275fcf0399ae90ee51da2d4b23f1a0d7ad4a8f278a525a558"}''')
WBF_RECEIPT_KEYS = json.loads(r'''["kind","problem_id","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","runtime","arithmetic_bits","complete","proved","actual_returncode","stage","failure","original_source_AST_evidence","actual_progress","gates","saved_record_counts","completed_targets","current_target","automatic_retry_authorized"]''')

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
    prior = docs["wbf_actual"]
    return {
        "complete_original_file_receipts": [
            five_fields(files[spec["role"]]) for spec in EXPECTED_OLD_FILES],
        "complete_WBF_mathematical_receipt": {
            key: copy.deepcopy(prior[key]) for key in WBF_RECEIPT_KEYS},
        "complete_inherited_WBF_original_admission":
            copy.deepcopy(prior["accepted_old_inputs"]),
        "complete_original_WBF_scalar_copy_reference":
            complete_object_reference(docs, "wbf_actual", ["copied_original_scalar_records"]),
        "complete_original_WBF_scope_reference":
            complete_object_reference(docs, "wbf_actual", ["copied_original_scopes"]),
        "all_original_WGS_24_gates_and_437_slots_verified": True,
        "all_original_WBF_16_gates_and_83_slots_verified": True,
        "WBF_full_WGS_predecessor_binding_verified": True,
        "original_WX_positive_integrated_first_budget_verified": True,
        "actual_cut_lower_not_global_phase_lower_used": True,
        "original_absolute_flows_cut_derivatives_and_complete_cut_compositions_read_only": True,
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
        "proof_WJR", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 6
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 6,
            "six complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "original input pin differs")
    require(same_json(files["proof_WJR"], EXPECTED_PROOF), "published WJR pin")
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
    main = docs["wgs_main"]
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
    require(main["source_sha256"] ==
            "d32fe912b7ebcb1ee6050589cf06ebf5512475a9c2636c584092c2d12be51e4f"
            and main["math_module_sha256"] ==
            "cb9c9aa0f7e5749967ece4e51210f359b4c58eecc7f83a05040607543ac47621",
            "exact original finite recurrence identities")
    pp = main["parameters"]
    require(pp["fixed_intrinsic_parameter"] == PARAMETERS["fixed_intrinsic_parameter"]
            and pp["exact_strict_interval"] == PARAMETERS["strict_interval"]
            and pp["exact_strict_cut"] == PARAMETERS["strict_cut"]
            and pp["exact_root_interval"] == PARAMETERS["root_interval"]
            and pp["exact_fold_strip"] == "3/128"
            and pp["actual_original_interfaces"] == 3070
            and pp["maximum_total_degree"] == 15
            and pp["physical_drift_bandwidth"] == 768
            and pp["drift_label_bandwidth"] == 192
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
            and len(high["cut_phase_orders_5_through_15"]) == 11
            and len(high["flow_orders_5_through_15"]) == 11
            and len(high["complete_strict_phase_angular_orders_1_through_15"]) == 15,
            "complete original ordinary flow and individual phase orders")
    old_original = main["accepted_original_inputs"]["original_whole_mathematics"]
    require(old_original["mathematical_complete"] is True
            and old_original["mathematical_proved"] is True
            and old_original["mathematical_failure"] is None
            and old_original["publication_complete"] is False
            and old_original["publication_actual_returncode"] == 1
            and old_original["formatter_failure"]["type"] == "TypeError",
            "historical scientific success and formatter failure remain distinct")
    prior = docs["wbf_actual"]
    require(prior["kind"] == "complete_sharp_Bernstein_integrated_finite_flow_bounds"
            and prior["problem_id"] == "same_selected_sharp_Bernstein_flow15_relative_omega14_v1"
            and prior["complete"] is True and prior["proved"] is True
            and prior["actual_returncode"] == 0 and prior["failure"] is None
            and prior["stage"] == "complete"
            and prior["run_id"] == "43870348355" and prior["run_attempt"] == "1"
            and prior["arithmetic_bits"] == 320
            and prior["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"}
            and prior["automatic_retry_authorized"] is False,
            "complete immutable WBF mathematical result")
    require(prior["scientific_modules"] == {
                "science": "7534760ac0e6867425c773598438c7909a502b6d84e05cc5c7c430637eee2ac7"}
            and prior["manifest_sha256"] ==
                "f3a9f5205bf8a91c1edf3e1fdb89787c0392bb047f07d7396f235e49300b27a3",
            "original WBF exact source and manifest")
    require(len(prior["gates"]) == 16
            and all(set(g) == {"name", "passed"} and g["passed"] is True
                    for g in prior["gates"]), "entire WBF gate list")
    old_names = [
        "complete_new_sharp_flow_conclusion",
        "complete_new_sharp_phase_conclusion",
        "complete_new_sharp_relative_bulk_conclusion",
        "complete_new_sharp_transport_relative_conclusion",
        "complete_new_sharp_relative_omega_conclusion"]
    require(complete_shape(prior["complete_new_graphs"], OLD_WBF_GRAPH_SHAPES)
            and prior["saved_record_counts"] == dict(zip(old_names, (14, 14, 14, 27, 14)))
            and sum(prior["saved_record_counts"].values()) == 83
            and all(scalar_record_count(prior["complete_new_graphs"][name]) == count
                    for name, count in prior["saved_record_counts"].items())
            and prior["current_target"] is None
            and prior["completed_targets"] == old_names,
            "all five original WBF graphs and all eighty-three saved targets")
    old_progress = prior["actual_progress"]
    require(old_progress["new_records_saved"] == 83
            and old_progress["new_graphs_completed"] == 5
            and old_progress["old_targets_recomputed"] == 0
            and old_progress["old_scientific_calls"] == 0
            and old_progress["original_records_copied_in_graphs"] == 0
            and old_progress["original_record_objects_copied"] == 33
            and old_progress["original_qualification_objects_copied"] == 12,
            "original WBF completion and no old rerun")
    for key, expected in (
            ("copied_original_scalar_records", OLD_WBF_RECORD_IDENTITY),
            ("copied_original_scopes", OLD_WBF_SCOPE_IDENTITY),
            ("accepted_old_inputs", OLD_WBF_ACCEPTED_IDENTITY)):
        body = canonical(prior[key])
        require(len(body) == expected["bytes"] and digest(body) == expected["sha256"],
                "complete inherited WBF objects unchanged")
    require(prior["input_sha256"]["wgs_main"] == files["wgs_main"]["sha256"]
            and prior["verified_original_inputs"]["wgs_main"] == {
                "bytes": files["wgs_main"]["bytes"], "sha256": files["wgs_main"]["sha256"]},
            "WBF binds this exact complete WGS main")
    old_accepted = prior["accepted_old_inputs"]
    old_file_map = {spec["role"]: spec for spec in
                    old_accepted["complete_original_file_receipts"]}
    require(same_json(old_file_map["wgs_main"], files["wgs_main"])
            and main["complete_original_inputs_file"] == {
                "filename": "complete-original-inputs.json",
                "bytes": old_file_map["wgs_copies"]["bytes"],
                "sha256": old_file_map["wgs_copies"]["sha256"]},
            "preserved whole companion identity without restoring it")
    inherited = old_accepted["complete_WGS_mathematical_and_original_admission"]
    require(same_json(inherited["complete_original_WGS_admission"],
                      main["accepted_original_inputs"])
            and same_json(inherited["complete_bound_companion_reference"],
                          main["complete_original_inputs_file"])
            and all(same_json(main[key], value) for key, value in
                    inherited["complete_WGS_mathematical_receipt"].items())
            and old_accepted["all_original_WGS_24_gates_and_437_slots_verified"] is True
            and old_accepted["all_original_WDG_16_gates_and_80_slots_verified"] is True
            and old_accepted["WDG_full_WGS_predecessor_binding_verified"] is True
            and old_accepted["original_positive_WX_integrated_first_budget_verified"] is True
            and old_accepted["original_historical_scientific_success_and_formatter_failure_preserved"] is True,
            "complete inherited WBF admission and exact WGS relation")
    archive = prior["copied_original_scopes"]
    require(same_json(archive["wgs_parameters"], pp)
            and same_json(archive["wgs_retained_scope"], main["retained_scope"])
            and same_json(archive["wgs_derivative_certificate"], certificate)
            and same_json(archive["wgs_higher_flow_qualifications"],
                          original_qualifications(high))
            and same_json(archive["wgs_original_AST_evidence"], main["original_source_AST_evidence"]),
            "whole original WBF scope archive and actual WGS main")
    original_scopes = archive["complete_original_nine_scope_objects"]
    flow = original_scopes["wx_flow"]
    require(flow["every_shorter_interval_and_both_orientations"] is True
            and flow["inverse_flow_has_its_own_same_directed_bounds"] is True
            and flow["specific_positive_algorithm_lower_addends_used"] is True
            and flow["no_arbitrary_operator_norm_inversion"] is True
            and flow["known_drift_label_bandwidth"] == 192
            and flow["physical_derivative_frequency_factor"] == 4
            and flow["true_radial_interval"] == PARAMETERS["strict_interval"],
            "original positive integral budget for both rays drift and shorter orientations")
    fa, dza = original_scopes["fa_parameters"], original_scopes["dza_parameters"]
    require(fa["exact_fold_strip"] == "3/128"
            and fa["exact_fold_radius"] == "3/8000"
            and fa["exact_strict_cut"] == PARAMETERS["strict_cut"]
            and fa["exact_real_delta_radius"] == "1/100000000"
            and fa["Airy_error_derivatives_taken"] is False
            and dza["exact_original_fold_strip"] == "3/128"
            and dza["physical_period"] == "pi/2"
            and dza["physical_frequency"] == "n=4|j|"
            and dza["drift_label_bandwidth"] == 192,
            "whole original cut scope and actual physical-angle convention")
    qp = prior["parameters"]
    qs = prior["retained_scope"]
    require(qp["strict_interval"] == PARAMETERS["strict_interval"]
            and qp["strict_cut"] == PARAMETERS["strict_cut"]
            and qp["root_interval"] == PARAMETERS["root_interval"]
            and qp["fixed_intrinsic_parameter"] == "eta_0"
            and qp["actual_drift_physical_bandwidth"] == 768
            and qp["first_flow_budget_qualification"] ==
                PARAMETERS["first_flow_budget_qualification"]
            and qs["original_first_positive_comparison_budget_bounds_exp_integral_D"] is True
            and qs["all_shorter_both_orientations_both_characteristics_and_drift"] is True
            and qs["positive_cut_atom_and_complete_ordinary_dr_integral_retained"] is True
            and qs["probability_measure_used_only_after_actual_derivative_identity"] is True
            and qs["original_F1_P1_K1_and_all_cut_records_read_only"] is True,
            "same positive first budget and complete original gap identity")
    for j in range(5, 16):
        require(same_json(prior["copied_original_scalar_records"]["cut_phase_" + str(j)],
                          high["cut_phase_orders_5_through_15"][j-5]),
                "original complete high cut derivative remains identical")
    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 43 and all(
                isinstance(v, dict) and set(v) == {"ball"} and isinstance(v["ball"], str)
                for v in records.values())
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA
            and same_json(records["cut_phase_lower"], high["cut_phase_lower"]),
            "all 43 complete originals including the true cut lower retained")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(spec["mode"] in ("exact", "complete_non_ball_projection"), "scope mode")
        scopes[name] = (copy.deepcopy(value) if spec["mode"] == "exact"
                        else original_qualifications(value))
    require(len(scopes) == 7 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "all original qualifications and complete WBF archive retained")
    accepted = accepted_original_inputs(docs, files)
    require(len(canonical(accepted)) == ORIGINAL_ACCEPTED_BYTES
            and digest(canonical(accepted)) == ORIGINAL_ACCEPTED_SHA,
            "complete inherited receipt and full admission retained")
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


def positive_bell_factory(values):
    memo = {(0, 0): ex(1)}
    def bell(n, k):
        if n == 0 and k == 0:
            return ex(1)
        if n <= 0 or k <= 0 or k > n:
            return ex(0)
        key = (n, k)
        if key not in memo:
            value = ex(0)
            for j in range(1, n-k+2):
                value += ex(math.comb(n-1, j-1)) * values[j] * bell(n-j, k-1)
            memo[key] = norm_upper(value)
        return memo[key]
    return bell


def original_flow_values(saved):
    return {j: saved_upper(saved["flow_" + str(j)]) for j in range(1, 15)}


def complete_relative_Jacobian(saved, graphs, emit):
    first = saved_upper(saved["flow_1"])
    require(first >= ex(1), "complete positive integrated first budget")
    excess = norm_upper(first - ex(1))
    stirling = [[0 for _ in range(15)] for _ in range(15)]
    stirling[0][0] = 1
    for n in range(1, 15):
        for k in range(1, n+1):
            stirling[n][k] = k*stirling[n-1][k] + stirling[n-1][k-1]
    for b in range(1, 15):
        complete = ex(0)
        for k in range(1, b+1):
            complete += ex(math.factorial(k)*stirling[b][k]) * excess**k
        emit(["ordinary_relative_Jacobian_orders_1_through_14", b-1],
             ex(768)**b * complete)


def complete_positive_phase_average_ratio(saved, graphs, emit):
    mcut = saved_positive_lower(saved["cut_phase_lower"])
    flow = original_flow_values(saved)
    bell = positive_bell_factory(flow)
    jacobian = {0: ex(1)}
    for b in range(1, 15):
        jacobian[b] = graph_record(
            graphs, "complete_new_relative_Jacobian_conclusion",
            ["ordinary_relative_Jacobian_orders_1_through_14", b-1])
    # These are complete NEW working subexpressions of the phase targets.
    # The zeroth ratio is exactly one; no cut-C1/global-phase-lower loss.
    cut_composed = {0: ex(1)}
    for ell in range(1, 15):
        complete = ex(0)
        for k in range(1, ell+1):
            complete += (saved_upper(saved["cut_phase_" + str(k+1)]) / mcut
                         * bell(ell, k))
        cut_composed[ell] = norm_upper(complete)
    for b in range(1, 15):
        complete = ex(0)
        for ell in range(b+1):
            complete += (ex(math.comb(b, ell)) * cut_composed[ell]
                         * jacobian[b-ell])
        emit(["ordinary_common_positive_phase_and_average_ratios_1_through_14", b-1],
             complete)


def complete_relative_bulk_transport(saved, graphs, emit):
    bell = positive_bell_factory(original_flow_values(saved))
    common = {}
    for k in range(1, 15):
        common[k] = graph_record(
            graphs, "complete_new_positive_phase_average_ratio_conclusion",
            ["ordinary_common_positive_phase_and_average_ratios_1_through_14", k-1])
    for b in range(1, 15):
        complete = ex(0)
        for k in range(1, b+1):
            complete += common[k] * bell(b, k)
        emit(["ordinary_bulk_contribution_orders_1_through_14", b-1], complete)


def complete_relative_omega(saved, graphs, emit):
    for b in range(1, 15):
        cut = saved_upper(saved["cut_composition_" + str(b)])
        bulk = graph_record(
            graphs, "complete_new_relative_bulk_transport_conclusion",
            ["ordinary_bulk_contribution_orders_1_through_14", b-1])
        emit(["complete_strict_relative_omega_angular_orders_1_through_14", b-1],
             max(cut, bulk))

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
        doc["actual_progress"]["complete_original_files_admitted"] = 2
        doc["actual_progress"]["original_record_objects_copied"] = 43
        doc["actual_progress"]["original_qualification_objects_copied"] = 7
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
            ("complete_new_relative_Jacobian_conclusion", complete_relative_Jacobian),
            ("complete_new_positive_phase_average_ratio_conclusion", complete_positive_phase_average_ratio),
            ("complete_new_relative_bulk_transport_conclusion", complete_relative_bulk_transport),
            ("complete_new_relative_omega_conclusion", complete_relative_omega))
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
        gate(GATE_LABELS[12])
        for role, spec in work["files"].items():
            require(check_file(work["root"], spec) == work["raw"][role],
                    "current input changed during new scalar work")
        require(digest(Path(args.manifest).read_bytes()) == args.manifest_sha,
                "manifest changed during new scalar work")
        gate(GATE_LABELS[13])
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
        gate(GATE_LABELS[14])
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
