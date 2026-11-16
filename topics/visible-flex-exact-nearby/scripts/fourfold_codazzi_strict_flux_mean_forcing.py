"""WMT: complete strict genuine flux, normalized L1 forcing and same-operator reassembly."""
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
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_strict_flux_mean_forcing.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py"''')
KIND = json.loads(r'''"complete_strict_flux_L1_mean_forcing_refinement"''')
PROBLEM_ID = json.loads(r'''"same_selected_complete_physical_mean_strict_flux_97_v1"''')
PREFLIGHT_KIND = json.loads(r'''"complete_strict_flux_L1_mean_forcing_refinement_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''99000''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''256''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''1024''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":72251,"git_blob_sha":"32ff92c516fcc5c43f3619930d4845d294289270","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json","role":"wgs_main","sha256":"8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"},{"bytes":31632,"git_blob_sha":"d6d13860e322d82ce354c8c0d0eb0f279ca63b3c","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json","role":"wgs_copies","sha256":"3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66"},{"bytes":9627,"git_blob_sha":"81bd01b84d8ebf5613ec0821e7c4ae770c39dfc9","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extended_amplitude_strict.json","role":"extended_strict","sha256":"fc2077f4fc24d6105e9e483c1b584e53bfd60987ad1a1a9718e9459c6830a0c2"},{"bytes":9131,"git_blob_sha":"f2a2687ae736d291c5d5b85e0309e625d729e5d8","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/profile_block_strict.json","role":"profile_strict","sha256":"6e781157c43f7ba7f7e4ac454308545444164138920cbab027a7af56dd1d89a6"},{"bytes":51030,"git_blob_sha":"5fdb01ed62008489bca34a4b6231519af4f60793","path":"topics/visible-flex-exact-nearby/notes/positive_weight_physical_mean_refinement_ci/run-43840219992-1/actual-scientific-conclusion.json","role":"prior_mean","sha256":"39a2d96accdbe1b4a8073674cabeda97878876f11fc24a055b910ed61567b432"}]''')
EXPECTED_PROOF = json.loads(r'''{"bytes":31256,"git_blob_sha":"c8049ef93eca8f84f135ab4338d6485081fb8424","path":"topics/visible-flex-exact-nearby/results/R133-supplement-strict-transport-flux-and-complete-mean-forcing-bound.md","role":"proof_WMT","sha256":"51eb08d0b110b8a5b171538c3be023efb94df587fdab880ebddac518665f73ce"}''')
OLD_FIELDSETS = json.loads(r'''{"extended_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"prior_mean":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"],"profile_strict":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"],"wgs_copies":["actual_scientific_checkout_commit","complete","complete_readonly_input_projection","copied_complete_local_coefficients","copied_complete_local_coefficients_sha256","copied_complete_original_scopes","copied_complete_original_scopes_sha256","copied_original_scalar_records","copied_original_scalar_records_sha256","copied_original_stage_records","copied_original_stage_records_sha256","copy_counts","input_manifest_sha256","kind","local_coefficient_qualification","math_module_sha256","original_input_sha256","public_repository","run_attempt","run_id","source_sha256","workflow_event_commit"],"wgs_main":["accepted_original_inputs","actual_mathematical_wall_seconds","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_free_first_transport_conclusion","complete_higher_flow_and_cut_conclusion","complete_local_regular_packet_conclusion","complete_named_global_graph_conclusion","complete_original_inputs_file","complete_strict_coefficient_conclusion","complete_strict_forcing_conclusion","complete_strict_geometry_conclusion","complete_strict_leading_conclusion","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"]}''')
ADMISSION_KEYS = json.loads(r'''{"extended_strict":["kind","node_name","binding","complete","printed_record_event_count","all_printed_records_in_complete_conclusion","failure","automatic_retry_authorized"],"prior_mean":["kind","problem_id","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","parameters","retained_scope","runtime","actual_progress","gates","stage","complete","proved","actual_returncode","failure","arithmetic_bits","automatic_retry_authorized","completed_targets","current_target","saved_record_counts","whole_candidate_choices","accepted_old_inputs"],"profile_strict":["kind","node_name","binding","complete","printed_record_event_count","all_printed_records_in_complete_conclusion","failure","automatic_retry_authorized"],"wgs_copies":["kind","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","source_sha256","math_module_sha256","input_manifest_sha256","original_input_sha256","complete","complete_readonly_input_projection","copy_counts","copied_complete_local_coefficients_sha256","copied_complete_original_scopes_sha256","copied_original_scalar_records_sha256","copied_original_stage_records_sha256","local_coefficient_qualification"],"wgs_main":["kind","public_repository","run_id","run_attempt","workflow_event_commit","actual_scientific_checkout_commit","source_sha256","math_module_sha256","input_manifest_sha256","input_sha256","parameters","retained_scope","runtime","actual_progress","gates","stage","complete","proved","actual_returncode","failure","complete_original_inputs_file","original_source_AST_evidence"]}''')
EXPECTED_ADMISSION_HASHES = json.loads(r'''{"extended_strict":{"bytes":2049,"sha256":"63fa0c6d4a27a5934aad314d8a7bba6138e49a056f8f1b44ef7df304aeb8bb60"},"prior_mean":{"bytes":10714,"sha256":"3c12c371c837f58841c7c4e7a04600c745804bf11490bb88d3b67ab698365a0f"},"profile_strict":{"bytes":2341,"sha256":"a4e683a4790ee6a97d28ff1ee9e5e7f7326ac32ad7085c37bc973dbf6c445af5"},"wgs_copies":{"bytes":4181,"sha256":"8594ac62a5fe8e6e4a1214cf3e92f7c088757785c74aea5094502e6b6bd700f6"},"wgs_main":{"bytes":8539,"sha256":"2040acee331df94cb2b632b6c396d9abff3b27eaeeab8ec5447b86b1612ec8c5"}}''')
RECORD_SPECS = json.loads(r'''{"Bessel_prefactor":{"endpoint":"upper","path":["copied_original_scalar_records","Bessel_prefactor"],"role":"prior_mean","use":"arithmetic"},"C_1":{"endpoint":"upper","path":["copied_original_scalar_records","C_1"],"role":"prior_mean","use":"arithmetic"},"C_O":{"endpoint":"upper","path":["copied_original_scalar_records","C_O"],"role":"prior_mean","use":"arithmetic"},"C_R":{"endpoint":"upper","path":["copied_original_scalar_records","C_R"],"role":"prior_mean","use":"arithmetic"},"Calg":{"endpoint":"upper","path":["copied_original_scalar_records","Calg"],"role":"prior_mean","use":"arithmetic"},"D_infinity":{"endpoint":"upper","path":["copied_original_scalar_records","D_infinity"],"role":"prior_mean","use":"arithmetic"},"Lrec":{"endpoint":"upper","path":["copied_original_scalar_records","Lrec"],"role":"prior_mean","use":"arithmetic"},"N_minus1_2_upper":{"endpoint":"upper","path":["copied_original_scalar_records","N_minus1_2_upper"],"role":"prior_mean","use":"arithmetic"},"N_minus4_3_upper":{"endpoint":"upper","path":["copied_original_scalar_records","N_minus4_3_upper"],"role":"prior_mean","use":"arithmetic"},"N_minus5_3_upper":{"endpoint":"upper","path":["copied_original_scalar_records","N_minus5_3_upper"],"role":"prior_mean","use":"arithmetic"},"N_minus5_6_upper":{"endpoint":"upper","path":["copied_original_scalar_records","N_minus5_6_upper"],"role":"prior_mean","use":"arithmetic"},"RF":{"endpoint":"upper","path":["copied_original_scalar_records","RF"],"role":"prior_mean","use":"arithmetic"},"Rplus":{"endpoint":"upper","path":["copied_original_scalar_records","Rplus"],"role":"prior_mean","use":"arithmetic"},"Xi23_6":{"endpoint":"upper","path":["copied_original_scalar_records","Xi23_6"],"role":"prior_mean","use":"arithmetic"},"background_Q0_0":{"endpoint":"upper","path":["copied_original_scalar_records","Q_0_0"],"role":"wgs_copies","use":"arithmetic"},"background_Q0_1":{"endpoint":"upper","path":["copied_original_scalar_records","Q_0_1"],"role":"wgs_copies","use":"arithmetic"},"background_Q0_2":{"endpoint":"upper","path":["copied_original_scalar_records","Q_0_2"],"role":"wgs_copies","use":"arithmetic"},"background_Q0_3":{"endpoint":"upper","path":["copied_original_scalar_records","Q_0_3"],"role":"wgs_copies","use":"arithmetic"},"collar_B_union":{"endpoint":"upper","path":["copied_original_scalar_records","collar_B_union"],"role":"prior_mean","use":"arithmetic"},"collar_T_union":{"endpoint":"upper","path":["copied_original_scalar_records","collar_T_union"],"role":"prior_mean","use":"arithmetic"},"dyadic_one_third":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_one_third"],"role":"prior_mean","use":"arithmetic"},"dyadic_two_thirds":{"endpoint":"upper","path":["copied_original_scalar_records","dyadic_two_thirds"],"role":"prior_mean","use":"arithmetic"},"ell_minus_negative_fourth_upper":{"endpoint":"upper","path":["copied_original_scalar_records","ell_minus_negative_fourth_upper"],"role":"prior_mean","use":"arithmetic"},"ell_plus_one_fourth_upper":{"endpoint":"upper","path":["copied_original_scalar_records","ell_plus_one_fourth_upper"],"role":"prior_mean","use":"arithmetic"},"endpoint_Vz":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_Vz"],"role":"prior_mean","use":"arithmetic"},"endpoint_WT":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_WT"],"role":"prior_mean","use":"arithmetic"},"endpoint_scattering":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_scattering"],"role":"prior_mean","use":"arithmetic"},"endpoint_second_order":{"endpoint":"upper","path":["copied_original_scalar_records","endpoint_second_order"],"role":"prior_mean","use":"arithmetic"},"ext_Vext_g0":{"endpoint":"upper","path":["conclusion","complete_jets","Vext","group_upper",0],"role":"extended_strict","use":"arithmetic"},"ext_Vext_g1":{"endpoint":"upper","path":["conclusion","complete_jets","Vext","group_upper",1],"role":"extended_strict","use":"arithmetic"},"ext_Vext_g2":{"endpoint":"upper","path":["conclusion","complete_jets","Vext","group_upper",2],"role":"extended_strict","use":"arithmetic"},"ext_Vext_g3":{"endpoint":"upper","path":["conclusion","complete_jets","Vext","group_upper",3],"role":"extended_strict","use":"arithmetic"},"ext_Vext_g4":{"endpoint":"upper","path":["conclusion","complete_jets","Vext","group_upper",4],"role":"extended_strict","use":"arithmetic"},"ext_Vext_g5":{"endpoint":"upper","path":["conclusion","complete_jets","Vext","group_upper",5],"role":"extended_strict","use":"arithmetic"},"ext_a1_g0":{"endpoint":"upper","path":["conclusion","complete_jets","a1_ext","group_upper",0],"role":"extended_strict","use":"arithmetic"},"ext_a1_g1":{"endpoint":"upper","path":["conclusion","complete_jets","a1_ext","group_upper",1],"role":"extended_strict","use":"arithmetic"},"ext_a1_g2":{"endpoint":"upper","path":["conclusion","complete_jets","a1_ext","group_upper",2],"role":"extended_strict","use":"arithmetic"},"ext_a1_g3":{"endpoint":"upper","path":["conclusion","complete_jets","a1_ext","group_upper",3],"role":"extended_strict","use":"arithmetic"},"ext_a1_g4":{"endpoint":"upper","path":["conclusion","complete_jets","a1_ext","group_upper",4],"role":"extended_strict","use":"arithmetic"},"ext_a1_g5":{"endpoint":"upper","path":["conclusion","complete_jets","a1_ext","group_upper",5],"role":"extended_strict","use":"arithmetic"},"ext_b1_g0":{"endpoint":"upper","path":["conclusion","complete_jets","b1_ext","group_upper",0],"role":"extended_strict","use":"arithmetic"},"ext_b1_g1":{"endpoint":"upper","path":["conclusion","complete_jets","b1_ext","group_upper",1],"role":"extended_strict","use":"arithmetic"},"ext_b1_g2":{"endpoint":"upper","path":["conclusion","complete_jets","b1_ext","group_upper",2],"role":"extended_strict","use":"arithmetic"},"ext_b1_g3":{"endpoint":"upper","path":["conclusion","complete_jets","b1_ext","group_upper",3],"role":"extended_strict","use":"arithmetic"},"ext_b1_g4":{"endpoint":"upper","path":["conclusion","complete_jets","b1_ext","group_upper",4],"role":"extended_strict","use":"arithmetic"},"ext_b1_g5":{"endpoint":"upper","path":["conclusion","complete_jets","b1_ext","group_upper",5],"role":"extended_strict","use":"arithmetic"},"jump_collar":{"endpoint":"upper","path":["copied_original_scalar_records","jump_collar"],"role":"prior_mean","use":"arithmetic"},"jump_strict":{"endpoint":"upper","path":["copied_original_scalar_records","jump_strict"],"role":"prior_mean","use":"arithmetic"},"local_mean":{"endpoint":"upper","path":["complete_new_graphs","two_patch_backward_mean","new_records","complete_local_mean_upper"],"role":"prior_mean","use":"arithmetic"},"local_raw_mean_source":{"endpoint":"upper","path":["complete_new_graphs","complete_affine_mean_sources","new_records","complete_local_raw_mean_source_upper"],"role":"prior_mean","use":"arithmetic"},"point_profile":{"endpoint":"upper","path":["conclusion","new_complete_records","single_signed_point_profile_upper"],"role":"profile_strict","use":"arithmetic"},"prior_reduced":{"endpoint":"upper","path":["complete_new_graphs","complete_whole_and_reduced","new_records","complete_same_reduced_error_upper"],"role":"prior_mean","use":"arithmetic"},"prior_whole":{"endpoint":"upper","path":["complete_new_graphs","complete_whole_and_reduced","new_records","complete_same_whole_error_upper"],"role":"prior_mean","use":"arithmetic"},"q_1":{"endpoint":"upper","path":["copied_original_scalar_records","q_1"],"role":"wgs_copies","use":"arithmetic"},"q_lower":{"endpoint":"lower","path":["copied_original_scalar_records","q_lower"],"role":"wgs_copies","use":"arithmetic"},"sqrt_ell_plus_upper":{"endpoint":"upper","path":["copied_original_scalar_records","sqrt_ell_plus_upper"],"role":"prior_mean","use":"arithmetic"},"sqrt_two_upper":{"endpoint":"upper","path":["copied_original_scalar_records","sqrt_two_upper"],"role":"prior_mean","use":"arithmetic"},"strict_B_t":{"endpoint":"upper","path":["copied_original_scalar_records","strict_B_t"],"role":"prior_mean","use":"arithmetic"},"strict_CF":{"endpoint":"upper","path":["copied_original_scalar_records","strict_CF"],"role":"prior_mean","use":"readonly_reference"},"strict_Ik":{"endpoint":"upper","path":["copied_original_scalar_records","strict_Ik"],"role":"prior_mean","use":"arithmetic"},"strict_Kabs":{"endpoint":"upper","path":["copied_original_scalar_records","strict_Kabs"],"role":"prior_mean","use":"arithmetic"},"strict_T_t":{"endpoint":"upper","path":["copied_original_scalar_records","strict_T_t"],"role":"prior_mean","use":"arithmetic"},"strict_Tk":{"endpoint":"upper","path":["complete_new_graphs","strict_positive_weight_coefficients","new_records","complete_Tk_upper"],"role":"prior_mean","use":"arithmetic"},"strict_V":{"endpoint":"upper","path":["copied_original_scalar_records","strict_V"],"role":"prior_mean","use":"arithmetic"},"strict_absolute_coefficient":{"endpoint":"upper","path":["complete_new_graphs","strict_positive_weight_coefficients","new_records","complete_absolute_mean_coefficient_upper"],"role":"prior_mean","use":"arithmetic"},"strict_backward_factor":{"endpoint":"upper","path":["complete_new_graphs","two_patch_backward_mean","new_records","complete_strict_backward_factor_upper"],"role":"prior_mean","use":"arithmetic"},"strict_base":{"endpoint":"upper","path":["copied_original_scalar_records","strict_base"],"role":"prior_mean","use":"arithmetic"},"strict_beta":{"endpoint":"upper","path":["copied_original_scalar_records","strict_beta"],"role":"prior_mean","use":"arithmetic"},"strict_eta_lower":{"endpoint":"lower","path":["copied_original_scalar_records","strict_eta_lower"],"role":"prior_mean","use":"arithmetic"},"strict_k0":{"endpoint":"upper","path":["copied_original_scalar_records","strict_k0"],"role":"prior_mean","use":"arithmetic"},"t_cut_lower":{"endpoint":"lower","path":["copied_original_scalar_records","t_cut_lower"],"role":"wgs_copies","use":"arithmetic"},"wgs_Fa_g0":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_Fa_g1":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_Fa_g2":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_Fa_g3":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_Fa_g4":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_Fa_g5":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fa","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_Fb_g0":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_Fb_g1":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_Fb_g2":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_Fb_g3":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_Fb_g4":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_Fb_g5":{"endpoint":"upper","path":["complete_strict_forcing_conclusion","complete_forcing_jets","Fb","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_Hinv_g0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_Hinv_g1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_Hinv_g2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_Hinv_g3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_Hinv_g4":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_Hinv_g5":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","H_inverse_entry_sum","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_Q_g0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_Q_g1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_Q_g2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_Q_g3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_Q_g4":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_Q_g5":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","Q","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_a0_g0":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","a0","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_a0_g1":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","a0","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_a0_g2":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","a0","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_a0_g3":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","a0","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_a0_g4":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","a0","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_a0_g5":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","a0","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_b0_g0":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","b0","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_b0_g1":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","b0","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_b0_g2":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","b0","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_b0_g3":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","b0","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_b0_g4":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","b0","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_b0_g5":{"endpoint":"upper","path":["complete_strict_leading_conclusion","complete_jets","b0","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_d_g0":{"endpoint":"upper","path":["complete_strict_coefficient_conclusion","new_jets","d","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_d_g1":{"endpoint":"upper","path":["complete_strict_coefficient_conclusion","new_jets","d","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_d_g2":{"endpoint":"upper","path":["complete_strict_coefficient_conclusion","new_jets","d","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_d_g3":{"endpoint":"upper","path":["complete_strict_coefficient_conclusion","new_jets","d","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_d_g4":{"endpoint":"upper","path":["complete_strict_coefficient_conclusion","new_jets","d","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_d_g5":{"endpoint":"upper","path":["complete_strict_coefficient_conclusion","new_jets","d","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_t_g0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_t_g1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_t_g2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_t_g3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_t_g4":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_t_g5":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","t","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_x_g0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_x_g1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_x_g2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_x_g3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_x_g4":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_x_g5":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","x","group_upper",5],"role":"wgs_main","use":"arithmetic"},"wgs_y_g0":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",0],"role":"wgs_main","use":"arithmetic"},"wgs_y_g1":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",1],"role":"wgs_main","use":"arithmetic"},"wgs_y_g2":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",2],"role":"wgs_main","use":"arithmetic"},"wgs_y_g3":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",3],"role":"wgs_main","use":"arithmetic"},"wgs_y_g4":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",4],"role":"wgs_main","use":"arithmetic"},"wgs_y_g5":{"endpoint":"upper","path":["complete_strict_geometry_conclusion","complete_jets","y","group_upper",5],"role":"wgs_main","use":"arithmetic"}}''')
SCOPE_SPECS = json.loads(r'''{"extended_strict_full_qualification":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"extended_strict"},"prior_mean_ancestor_endpoint":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","endpoint"],"role":"prior_mean"},"prior_mean_ancestor_free":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","free"],"role":"prior_mean"},"prior_mean_ancestor_mean_N6_strict":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","mean_N6_strict"],"role":"prior_mean"},"prior_mean_ancestor_mean_kernel_strict":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","mean_kernel_strict"],"role":"prior_mean"},"prior_mean_ancestor_negative_reception":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","negative_reception"],"role":"prior_mean"},"prior_mean_ancestor_physical_coefficients_strict":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","physical_coefficients_strict"],"role":"prior_mean"},"prior_mean_ancestor_same_angular_J_strict":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","same_angular_J_strict"],"role":"prior_mean"},"prior_mean_ancestor_true_jumps":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","true_jumps"],"role":"prior_mean"},"prior_mean_ancestor_whole":{"mode":"exact","path":["copied_original_scopes","complete_original_node_qualifications","whole"],"role":"prior_mean"},"prior_mean_complete_affine_mean_sources":{"mode":"complete_non_ball_projection","path":["complete_new_graphs","complete_affine_mean_sources"],"role":"prior_mean"},"prior_mean_complete_continuation_additional_parameters":{"mode":"exact","path":["copied_original_scopes","complete_continuation_additional_parameters"],"role":"prior_mean"},"prior_mean_complete_negative_receiver":{"mode":"complete_non_ball_projection","path":["complete_new_graphs","complete_negative_receiver"],"role":"prior_mean"},"prior_mean_complete_original_parameters":{"mode":"exact","path":["copied_original_scopes","complete_original_parameters"],"role":"prior_mean"},"prior_mean_complete_original_retained_scope":{"mode":"exact","path":["copied_original_scopes","complete_original_retained_scope"],"role":"prior_mean"},"prior_mean_complete_waist_endpoint":{"mode":"complete_non_ball_projection","path":["complete_new_graphs","complete_waist_endpoint"],"role":"prior_mean"},"prior_mean_complete_whole_and_reduced":{"mode":"complete_non_ball_projection","path":["complete_new_graphs","complete_whole_and_reduced"],"role":"prior_mean"},"prior_mean_parameters":{"mode":"exact","path":["parameters"],"role":"prior_mean"},"prior_mean_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"prior_mean"},"prior_mean_strict_positive_weight_coefficients":{"mode":"complete_non_ball_projection","path":["complete_new_graphs","strict_positive_weight_coefficients"],"role":"prior_mean"},"prior_mean_two_patch_backward_mean":{"mode":"complete_non_ball_projection","path":["complete_new_graphs","two_patch_backward_mean"],"role":"prior_mean"},"prior_mean_whole_candidate_choices":{"mode":"exact","path":["whole_candidate_choices"],"role":"prior_mean"},"profile_strict_full_qualification":{"mode":"complete_non_ball_projection","path":["conclusion"],"role":"profile_strict"},"wgs_complete_derivative_request_certificate":{"mode":"exact","path":["complete_derivative_request_certificate"],"role":"wgs_main"},"wgs_complete_strict_coefficient_conclusion":{"mode":"complete_non_ball_projection","path":["complete_strict_coefficient_conclusion"],"role":"wgs_main"},"wgs_complete_strict_forcing_conclusion":{"mode":"complete_non_ball_projection","path":["complete_strict_forcing_conclusion"],"role":"wgs_main"},"wgs_complete_strict_geometry_conclusion":{"mode":"complete_non_ball_projection","path":["complete_strict_geometry_conclusion"],"role":"wgs_main"},"wgs_complete_strict_leading_conclusion":{"mode":"complete_non_ball_projection","path":["complete_strict_leading_conclusion"],"role":"wgs_main"},"wgs_old_fa_parameters":{"mode":"exact","path":["copied_complete_original_scopes","fa_parameters"],"role":"wgs_copies"},"wgs_old_sj_parameters":{"mode":"exact","path":["copied_complete_original_scopes","sj_parameters"],"role":"wgs_copies"},"wgs_old_sj_scope":{"mode":"exact","path":["copied_complete_original_scopes","sj_scope"],"role":"wgs_copies"},"wgs_parameters":{"mode":"exact","path":["parameters"],"role":"wgs_main"},"wgs_retained_scope":{"mode":"exact","path":["retained_scope"],"role":"wgs_main"}}''')
ORIGINAL_RECORD_SHA = json.loads(r'''"a0fcd7b24cba3955336cf8b5b37de8ba83ecaadf0b7cc945bf78ef4699e3219d"''')
ORIGINAL_RECORD_BYTES = json.loads(r'''15148''')
ORIGINAL_SCOPE_SHA = json.loads(r'''"8a6d0d5c0230cb4f13c10f61403012f60feb542c6fe5be8c8a2ebd67c1355ad8"''')
ORIGINAL_SCOPE_BYTES = json.loads(r'''36676''')
ORIGINAL_ACCEPTED_SHA = json.loads(r'''"1f5e3a84340dd79f8c52ef8fc5dcadfd040dbab86137c03c85595bd3bec6f821"''')
ORIGINAL_ACCEPTED_BYTES = json.loads(r'''4900''')
PARAMETERS = json.loads(r'''{"L1_primitive_qualification":"pi/8 < 11/28; 22/7-pi is the positive integral of x^4(1-x)^4/(1+x^2) on [0,1]","L1_primitive_upper":"11/28","angular_normalization":"ordinary pure angular derivative divided by j!","arithmetic_bits":320,"copied_original_qualification_objects":33,"copied_original_records":131,"decimal_record_digits":75,"first_absolute_mode":97,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","graph_original_copies":2,"history_inputs":0,"mean_source_decay":"n^(-23/6)","mean_steps":5,"minimum_physical_frequency":388,"new_exponentials":0,"new_fractional_powers":0,"new_graphs":7,"new_logarithms":0,"new_record_count":195,"new_square_roots":0,"old_complete_files":5,"old_scientific_calls":0,"old_target_recomputations":0,"original_PW_cut":"2333968743003/10000000000000","original_derivative_groups":[[0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15]],"original_true_interfaces":3070,"physical_frequency":"n=4|j|","physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"strict_alpha_upper":"1/2","strict_cut":"76285779072683/320000000000000","strict_interval":["0","76285779072683/320000000000000"],"strict_weight_gap":"79/128","terminal_polynomial_degrees":[0,1,2,3,4,5,6,7],"total_graph_scalar_slots":197}''')
RETAINED_SCOPE = json.loads(r'''{"WGS_geometry_amplitude_sup_not_A0":true,"actual_96_columns_exist_but_signed_normalization_uncomputed":true,"all_original_one_sided_intervals_and_3070_interfaces_retained":true,"both_characteristic_branches_and_reflection_retained":true,"complete_genuine_Vext_and_extended_forcing_retained":true,"complete_genuine_root_matrix_and_beta_n_retained":true,"exact_root_finite_factor_and_full_WCF_FJ_two_ranks_rho_i_ell2_retained":true,"final_surface_proved":false,"finite_Schur_inverse_proved":false,"five_complete_mean_steps_and_all_eight_terminal_degrees_retained":true,"fixed_new_flux_branch_only":true,"full_Jr_beta_r_e_kappa_and_R0_retained":true,"full_incoming_inverse_proved":false,"full_nonlinear_background_proved":false,"local_root_forcing_and_mean_unchanged":true,"no_phase_lift_value_filled":true,"no_radial_integration_by_parts":true,"normalized_L1_not_Wiener_or_L2_primitive":true,"nu_Schur_and_infinite_radial_head_retained":true,"old_whole_mathematics_success_and_formatter_failure_retained":true,"original_physical_mean_root_initial_value_retained":true,"original_producers_not_imported":true,"original_weighted_and_unweighted_averages_distinct":true,"p_weight_is_not_relabelled_mass_one":true,"passing_high_cutoff_proved":false,"physical_two_means_and_mean_feedback_retained":true,"positive_weight_gap_is_pointwise":true,"same_fixed_intrinsic_eta0":true,"same_selected_real_member_only":true,"strict_d_A0_has_independent_original_product_primitive_proof":true,"true_physical_96_columns_and_all_Theta_cross_blocks_retained":true,"whole_Calg_not_replaced_by_D_infinity":true,"whole_and_reduced_compared_only_with_same_original_operator":true,"whole_bounds_not_subtracted":true}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["complete_normalized_weight_L1_kernels","complete_strict_flux_amplitudes","complete_five_mean_recursions","complete_strict_mean_and_affine_sources","complete_negative_receiver","complete_waist_endpoint","complete_whole_and_reduced"]''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_five_mean_recursions":{"all_five_recursions_and_terminal_retained":true,"complete":true,"complete_terminal_degrees":[0,1,2,3,4,5,6,7],"inverse_level_shapes":[[6,3],[5,4],[4,5],[3,6],[2,7]],"kind":"complete_strict_five_step_L1_mean_recursion","level_axis_order":["angular_degree","inverse_frequency_degree"],"mean_source_decay":"n^(-23/6)","minimum_physical_frequency":388,"new_records":{"complete_inverse_levels":[[[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]],[[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]],[[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]],[[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]],[[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]]],"complete_reflected_strict_mean_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_terminal_coefficients":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"physical_frequency":"n=4|j|","reflected_column_factor":2},"complete_negative_receiver":{"complete":true,"complete_nonmean_and_mean_source_terms_retained":true,"kind":"complete_strict_flux_negative_reception","new_records":{"complete_collar_ordinary_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_raw_mean_union_upper":{"ball":"__FINITE_SCALAR__"},"complete_collar_received_with_jumps_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_negative_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_ordinary_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_received_with_jumps_upper":{"ball":"__FINITE_SCALAR__"}},"ordinary_dr_and_original_dyadic_powers_retained":true,"original_PW_cut_and_all_true_jump_records_retained":true},"complete_normalized_weight_L1_kernels":{"L1_primitive_upper":"11/28; rational upper for pi/8, not the value of pi","angular_derivatives_divided_by_factorial":true,"complete":true,"full_projection_in_e_kappa_retained":true,"kind":"complete_strict_normalized_weight_L1_kernels","new_records":{"e_L1_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"e_kappa_L1_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"p_L1_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"pure_angular_background_pair_upper":[{"ball":"[7.000000190000000000000000000000000000000000000 +/- 1e-50]"},{"ball":"[6.000000830000000000000000000000000000000000000 +/- 1e-50]"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"normalized_circle_measure":true,"old_graph_record_copies":2,"p_is_not_relabelled_probability_mass_one":true},"complete_strict_flux_amplitudes":{"amplitude_polynomial_degree_order":[0,1,2],"angular_derivatives_divided_by_factorial":true,"complete":true,"complete_extended_forcing_retained":true,"complete_genuine_potential_and_root_matrix_retained":true,"kind":"complete_genuine_strict_flux_amplitudes","matrix_norm":"entry sum","new_records":{"B_matrix_L1_angular_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"C_matrix_angular_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"D_matrix_L1_angular_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"L_matrix_angular_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"amplitude_polynomial_L1_angular_upper":[[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]],"q_ext_vector_angular_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}],"reciprocal_T_angular_upper":[{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"},{"ball":"__FINITE_SCALAR__"}]},"no_radial_derivative_of_first_amplitude_used":true,"strict_T_reciprocal_not_extended_to_root":true,"vector_norm":"component sum"},"complete_strict_mean_and_affine_sources":{"complete":true,"full_absolute_mean_coefficient_used_for_derivative":true,"kind":"complete_strict_flux_physical_mean_and_sources","local_complete_physical_mean_copied_unchanged":true,"new_records":{"complete_strict_mean_derivative_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_mean_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_primitive_mean_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_strict_raw_mean_source_upper":{"ball":"__FINITE_SCALAR__"}},"old_backward_exponential_read_only":true,"physical_mean_initial_condition":"z_ph(r_star)=0","upper_root_bracket_is_only_a_length_bound":true},"complete_waist_endpoint":{"complete":true,"full_vz_and_two_physical_means_retained":true,"kind":"complete_strict_flux_waist_endpoint","new_records":{"complete_physical_mean_endpoint_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_waist_endpoint_upper":{"ball":"__FINITE_SCALAR__"}},"same_original_four_endpoints":true,"three_complete_nonmean_endpoint_terms_copied":true},"complete_whole_and_reduced":{"actual_96_columns_and_uncomputed_signed_normalization_retained":true,"complete":true,"kind":"complete_strict_flux_whole_and_reduced_errors","new_flux_branch_evaluated_independently":true,"new_records":{"complete_all_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_nonroot_source_sum_upper":{"ball":"__FINITE_SCALAR__"},"complete_reduced_received_source_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_reduced_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_same_whole_error_upper":{"ball":"__FINITE_SCALAR__"},"complete_whole_received_source_upper":{"ball":"__FINITE_SCALAR__"}},"old_WMR_targets_read_only":true,"root_and_coefficient_finite_factors_retained":true,"whole_and_reduced_are_different_operators":true}}''')
GRAPH_RECORD_COUNTS = json.loads(r'''{"complete_five_mean_recursions":99,"complete_negative_receiver":6,"complete_normalized_weight_L1_kernels":25,"complete_strict_flux_amplitudes":55,"complete_strict_mean_and_affine_sources":4,"complete_waist_endpoint":2,"complete_whole_and_reduced":6}''')
GRAPH_NEW_RECORD_COUNTS = json.loads(r'''{"complete_five_mean_recursions":99,"complete_negative_receiver":6,"complete_normalized_weight_L1_kernels":23,"complete_strict_flux_amplitudes":55,"complete_strict_mean_and_affine_sources":4,"complete_waist_endpoint":2,"complete_whole_and_reduced":6}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_original_files_admitted":5,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":7,"new_logarithms":0,"new_quadratures":0,"new_records_saved":195,"new_square_roots":0,"new_whole_comparisons_completed":2,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":33,"original_record_objects_copied":131,"original_records_copied_in_graphs":2}''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_original_files_admitted":0,"new_exponentials_saved":0,"new_fractional_powers":0,"new_graphs_completed":0,"new_logarithms":0,"new_quadratures":0,"new_records_saved":0,"new_square_roots":0,"new_whole_comparisons_completed":0,"old_binary_parts_restored":0,"old_exponentials_recomputed":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_qualification_objects_copied":0,"original_record_objects_copied":0,"original_records_copied_in_graphs":0}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","current_input_and_AST_identity","all_five_complete_original_files_byte_identical","complete_WGS_pair_reference_and_binding","complete_prior_positive_weight_science","completed_posterior_nodes_and_parent_failure_retained","complete_scalar_and_qualification_copies_retained","true_lower_endpoints_and_normalized_jet_positions","complete_normalized_weight_L1_kernels","complete_strict_flux_amplitudes","complete_five_mean_recursions","complete_strict_mean_and_affine_sources","complete_negative_receiver","complete_waist_endpoint","complete_whole_and_reduced","only_identical_whole_operator_candidates_compared","all_current_inputs_still_identical","complete_scientific_graph_and_prefix"]''')
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
    receipts = []
    for spec in EXPECTED_OLD_FILES:
        role = spec["role"]
        old = docs[role]
        receipts.append({
            "role": role, "path": spec["path"], "blob_sha": spec["git_blob_sha"],
            "bytes": spec["bytes"], "sha256": spec["sha256"],
            "kind": old["kind"], "field_count": len(old), "complete": old["complete"],
            "gates": {"count": len(old["gates"]),
                      "sha256": digest(canonical(old["gates"]))} if "gates" in old else None})
    attempts = {}
    index_admissions = docs["prior_mean"]["accepted_old_inputs"]["original_index_admission"]
    for role, old in index_admissions.items():
        attempts[role] = {
            "complete_index_admission_reference": complete_object_reference(
                docs, "prior_mean", ["accepted_old_inputs", "original_index_admission", role]),
            **{key: copy.deepcopy(old[key]) for key in
               ("run_id", "run_attempt", "complete", "proved",
                "actual_returncode", "stage", "failure")}}
    return {
        "complete_original_file_receipts": receipts,
        "complete_original_binding_references": {
            "extended_strict": complete_object_reference(docs, "extended_strict", ["binding"]),
            "profile_strict": complete_object_reference(docs, "profile_strict", ["binding"]),
            "prior_mean": complete_object_reference(docs, "prior_mean", ["accepted_old_inputs"])},
        "complete_WGS_pair": {
            "reference_to_copies": copy.deepcopy(docs["wgs_main"]["complete_original_inputs_file"]),
            "same_binding_fields": ["public_repository", "run_id", "run_attempt",
                "workflow_event_commit", "actual_scientific_checkout_commit",
                "source_sha256", "math_module_sha256", "input_manifest_sha256"],
            "complete_copy_counts": copy.deepcopy(docs["wgs_copies"]["copy_counts"])},
        "original_prior_attempts": attempts,
        "all_five_full_original_files_and_complete_gate_lists_verified": True,
        "original_metadata_retained_by_full_file_and_complete_object_references": True,
        "both_complete_posterior_nodes_and_their_original_bindings_verified": True,
        "first_posterior_attempt_failure_not_relabelled_success": True,
        "all_consumed_scalar_objects_and_qualifications_copied_verbatim": True,
        "old_scientific_producers_not_imported": True}

def read_only_admission(repo, manifest_file, manifest_sha):
    root = Path(repo).resolve()
    manifest_raw = Path(manifest_file).read_bytes()
    require(digest(manifest_raw) == manifest_sha, "manifest CLI identity")
    manifest = exact_json(manifest_raw)
    specs = manifest["files"]
    expected_roles = [p["role"] for p in EXPECTED_OLD_FILES] + [
        "proof_WMT", "science", "worker", "rules"]
    require(isinstance(specs, list) and len(specs) == 9
            and [p["role"] for p in specs] == expected_roles
            and len({p["path"] for p in specs}) == 9,
            "nine complete current inputs in fixed order")
    files = {p["role"]: p for p in specs}
    for spec in EXPECTED_OLD_FILES:
        require(same_json(files[spec["role"]], spec), "original input pin differs")
    require(same_json(files["proof_WMT"], EXPECTED_PROOF), "published WMT pin")
    require(files["science"]["path"] == SOURCE_PATH
            and files["worker"]["path"] == WORKER_PATH, "new entry paths")
    raw = {spec["role"]: check_file(root, spec) for spec in specs}
    require(Path(__file__).resolve() == safe_path(root, SOURCE_PATH)
            and Path(__file__).read_bytes() == raw["science"], "actual entry bytes")
    module_map = {"science": files["science"]["sha256"]}
    require(same_json(manifest["scientific_modules"], [files["science"]])
            and same_json(manifest["parameters"], PARAMETERS), "single new module and parameters")
    op = manifest["operation"]
    require(op["kind"] == KIND and op["problem_id"] == PROBLEM_ID
            and same_json(op["parameters"], PARAMETERS)
            and same_json(op["ordered_targets"], ORDERED_GRAPH_NAMES)
            and same_json(op["scientific_module_binding"], module_map)
            and op["bits_parameter"] == "arithmetic_bits",
            "operation profile differs")
    for role in ("science", "worker"):
        ast.parse(raw[role].decode("utf-8"), filename=files[role]["path"])
    docs = {spec["role"]: exact_json(raw[spec["role"]]) for spec in EXPECTED_OLD_FILES}
    for role, old in docs.items():
        require(sorted(old) == OLD_FIELDSETS[role] and canonical(old) == raw[role],
                "complete old JSON schema or spelling differs")
        projection = {key: old[key] for key in ADMISSION_KEYS[role]}
        projection_raw = canonical(projection)
        expected = EXPECTED_ADMISSION_HASHES[role]
        require(len(projection_raw) == expected["bytes"]
                and digest(projection_raw) == expected["sha256"],
                "complete original status/identity/parameter/scope/gate projection differs")
    for role, count in (("wgs_main", 24), ("prior_mean", 18)):
        old = docs[role]
        require(old["complete"] is True and old["proved"] is True
                and old["actual_returncode"] == 0 and old["failure"] is None
                and old["stage"] == "complete" and len(old["gates"]) == count,
                "old complete mathematical result")
        require(all(set(g) == {"name", "passed"} and g["passed"] is True
                    for g in old["gates"]), "entire original gate list")
        require(old["runtime"] == {"Python": "3.12.14", "python_flint": "0.9.0"},
                "original directed runtime")
    first, copies = docs["wgs_main"], docs["wgs_copies"]
    pair_fields = ("public_repository", "run_id", "run_attempt", "workflow_event_commit",
                   "actual_scientific_checkout_commit", "source_sha256",
                   "math_module_sha256", "input_manifest_sha256")
    require(all(same_json(first[key], copies[key]) for key in pair_fields),
            "complete WGS pair binding")
    require(copies["complete"] is True and copies["complete_readonly_input_projection"] is True,
            "complete original-input companion")
    require(same_json(first["complete_original_inputs_file"], {
        "filename": "complete-original-inputs.json", "bytes": files["wgs_copies"]["bytes"],
        "sha256": files["wgs_copies"]["sha256"]}), "WGS companion exact file reference")
    for object_key, hash_key in (
        ("copied_complete_local_coefficients", "copied_complete_local_coefficients_sha256"),
        ("copied_complete_original_scopes", "copied_complete_original_scopes_sha256"),
        ("copied_original_scalar_records", "copied_original_scalar_records_sha256"),
        ("copied_original_stage_records", "copied_original_stage_records_sha256")):
        require(digest(canonical(copies[object_key])) == copies[hash_key],
                "complete original WGS copy object differs")
    certificate = first["complete_derivative_request_certificate"]
    require(same_json(certificate["fixed_degree_groups"],
                      PARAMETERS["original_derivative_groups"])
            and certificate["normalized_coefficients"] ==
                "ordinary derivative norm divided by a! b!",
            "actual stored degree groups and factorial normalization")
    prior = docs["prior_mean"]
    index = prior["accepted_old_inputs"]["original_index_admission"]
    require(index["prior_prefix_index"]["complete"] is False
            and index["prior_prefix_index"]["proved"] is False
            and index["prior_prefix_index"]["actual_returncode"] == 1
            and index["prior_prefix_index"]["run_id"] == "43827705714"
            and index["prior_completion_index"]["complete"] is True
            and index["prior_completion_index"]["actual_returncode"] == 0,
            "original failed attempt and successful continuation remain distinct")
    prefix = index["prior_prefix_index"]
    for role, node, count in (("extended_strict", "extended_amplitude_strict", 64),
                              ("profile_strict", "profile_block_strict", 51)):
        old = docs[role]
        binding = old["binding"]
        require(old["kind"] == "WEJ_complete_atomic_node_v1" and old["node_name"] == node
                and old["complete"] is True and old["failure"] is None
                and old["all_printed_records_in_complete_conclusion"] is True
                and old["automatic_retry_authorized"] is False
                and old["printed_record_event_count"] == count
                and scalar_record_count(old["conclusion"]) == count,
                "complete original posterior node")
        require(binding["problem_id"] ==
                "complete_global_genuine_waist_error_posterior_selected_original_97_v1/" + node
                and binding["parameters_sha256"] == prefix["parameters_sha256"]
                and same_json(binding["scientific_module_sha256"], prefix["scientific_module_sha256"])
                and digest(canonical(binding["mathematical_input_sha256"])) ==
                    prefix["complete_mathematical_input_map_sha256"],
                "original node binding and preserved parent")
        require(binding["mathematical_input_sha256"]["WGS_main"] == files["wgs_main"]["sha256"]
                and binding["mathematical_input_sha256"]["WGS_original_inputs"] ==
                    files["wgs_copies"]["sha256"], "same WGS actual pair used by posterior")
    require(prior["parameters"]["selected_original_real_member_only"] is True
            and prior["parameters"]["strict_cut"] == PARAMETERS["strict_cut"]
            and first["parameters"]["exact_strict_cut"] == PARAMETERS["strict_cut"]
            and prior["parameters"]["minimum_physical_frequency"] == 388
            and first["parameters"]["background_physical_bandwidth"] == 384,
            "same strict selected frequency and background support")
    for which in ("whole", "reduced"):
        choice = prior["whole_candidate_choices"][which]
        require(choice["selected_label"] == "new_positive_weight"
                and choice["selected_record_path"] == RECORD_SPECS["prior_" + which]["path"]
                and choice["all_candidates_retained"] is True,
                "actual selected prior whole bound")
    families = (
        ("complete_strict_geometry_conclusion", "complete_jets",
         ("t", "Q", "x", "y", "H_inverse_entry_sum")),
        ("complete_strict_coefficient_conclusion", "new_jets", ("d",)),
        ("complete_strict_leading_conclusion", "complete_jets", ("a0", "b0")),
        ("complete_strict_forcing_conclusion", "complete_forcing_jets", ("Fa", "Fb")))
    for graph, field, keys in families:
        for key in keys:
            jet = first[graph][field][key]
            need = 6 if key in ("t", "Q", "d") else 5
            require(jet["value_omitted_for_lift"] is False
                    and jet["shape"][0] >= need and len(jet["group_upper"]) >= 6,
                    "true stored pure angular predecessor including group 5 for degree 6")
    for key in ("Vext", "a1_ext", "b1_ext"):
        jet = docs["extended_strict"]["conclusion"]["complete_jets"][key]
        require(jet["value_omitted_for_lift"] is False
                and jet["shape"] == [12, 2] and len(jet["group_upper"]) == 8,
                "complete genuine extended angular predecessor")
    records = {alias: copy.deepcopy(at(docs[spec["role"]], spec["path"]))
               for alias, spec in RECORD_SPECS.items()}
    require(len(records) == 131
            and len(canonical(records)) == ORIGINAL_RECORD_BYTES
            and digest(canonical(records)) == ORIGINAL_RECORD_SHA,
            "all complete original scalar objects retained")
    scopes = {}
    for name, spec in SCOPE_SPECS.items():
        value = at(docs[spec["role"]], spec["path"])
        require(spec["mode"] in ("exact", "complete_non_ball_projection"), "scope mode")
        scopes[name] = (copy.deepcopy(value) if spec["mode"] == "exact"
                        else original_qualifications(value))
    require(len(scopes) == 33 and scalar_record_count(scopes) == 0
            and len(canonical(scopes)) == ORIGINAL_SCOPE_BYTES
            and digest(canonical(scopes)) == ORIGINAL_SCOPE_SHA,
            "all complete consumed qualification objects retained")
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

# New WMT finite positive formulas only. Definitions have no import-time arithmetic.
# All original scalars are read; no prior producer or old graph is invoked.

def scalar_sum(values):
    result = arb(0)
    for value in values:
        result += value
    return result

def convolution(a, b, degree):
    return [scalar_sum(a[k] * b[j-k]
                       for k in range(j+1)
                       if k < len(a) and j-k < len(b))
            for j in range(degree+1)]

def old_angular(saved, prefix, degree):
    groups = (0, 1, 2, 3, 4, 5, 5)
    require(0 <= degree <= 6, "declared pure angular degree")
    return [saved_upper(saved[prefix + "_g" + str(groups[j])])
            for j in range(degree+1)]

def graph_record(graphs, name, path):
    return at(graphs[name]["new_records"],
              [path] if isinstance(path, str) else path)

def graph_array(graphs, name, field):
    return [saved_upper(value) for value in graphs[name]["new_records"][field]]

def complete_normalized_weight(saved, graphs, emit, copy_old):
    pair = []
    for j in range(6):
        path = ["pure_angular_background_pair_upper", j]
        if j < 2:
            record = copy_old(path, "background_Q0_" + str(j))
        else:
            ordinary = saved_upper(saved["background_Q0_" + str(min(j, 3))])
            if j > 3:
                ordinary *= arb(384 ** (j-3))
            record = emit(path, ordinary / arb(math.factorial(j)))
        pair.append(saved_upper(record))
    # A complete pair bound is valid for each component separately.
    U = V = pair
    alpha = rational("1/2")
    mass = saved_upper(saved["strict_V"])
    beta = saved_upper(saved["strict_beta"])
    curvature = saved_upper(saved["strict_Kabs"])
    base = saved_upper(saved["strict_base"])
    eta = saved_positive_lower(saved["strict_eta_lower"])
    drift = old_angular(saved, "wgs_d", 6)
    product = convolution(U, V, 4)
    h = [alpha * value for value in product]
    p = [saved_upper(emit(["p_L1_upper", 0], rational("128/79")))]
    for j in range(5):
        value = scalar_sum(h[k] * p[j-k] for k in range(j+1)) / arb(j+1)
        p.append(saved_upper(emit(["p_L1_upper", j+1], value)))
    # pi/8 < 11/28 follows from the positive 22/7-pi integral.
    # This rational is an outward bound, not an asserted value of pi.
    e = [saved_upper(emit(["e_L1_upper", 0],
                         alpha * mass * rational("11/28") * p[0] * U[0]))]
    pU = convolution(p, U, 5)
    for j in range(1, 7):
        e.append(saved_upper(emit(["e_L1_upper", j],
                                 alpha * mass * pU[j-1] / arb(j))))
    dU = convolution(drift, U, 5)
    zeta = [curvature * V[j] + dU[j] / eta for j in range(6)]
    rho = convolution(p, zeta, 5)
    for j in range(6):
        # Only degree zero pays the complete P norm in normalized L1.
        factor = arb(4 if j == 0 else 2)
        emit(["e_kappa_L1_upper", j], base * e[j] + factor * beta * mass * rho[j])

def complete_flux_amplitudes(saved, graphs, emit, copy_old):
    kernel = "complete_normalized_weight_L1_kernels"
    e = graph_array(graphs, kernel, "e_L1_upper")
    ek = graph_array(graphs, kernel, "e_kappa_L1_upper")
    t = old_angular(saved, "wgs_t", 6)
    Q = old_angular(saved, "wgs_Q", 6)
    x = old_angular(saved, "wgs_x", 5)
    y = old_angular(saved, "wgs_y", 5)
    d = old_angular(saved, "wgs_d", 6)
    potential = old_angular(saved, "ext_Vext", 5)
    a0 = old_angular(saved, "wgs_a0", 5)
    b0 = old_angular(saved, "wgs_b0", 5)
    a1 = old_angular(saved, "ext_a1", 5)
    b1 = old_angular(saved, "ext_b1", 5)
    Fa = old_angular(saved, "wgs_Fa", 5)
    Fb = old_angular(saved, "wgs_Fb", 5)
    t_lower = saved_positive_lower(saved["t_cut_lower"])
    q_lower = saved_positive_lower(saved["q_lower"])
    q_r = saved_upper(saved["q_1"])
    beta = saved_upper(saved["strict_beta"])
    base = saved_upper(saved["strict_base"])
    R = [saved_upper(emit(["reciprocal_T_angular_upper", 0], arb(1) / t_lower))]
    for j in range(1, 6):
        value = scalar_sum(t[k] * R[j-k] for k in range(1, j+1)) / t_lower
        R.append(saved_upper(emit(["reciprocal_T_angular_upper", j], value)))
    kt = [t[j] + arb(1 if j == 0 else 0) for j in range(7)]
    Qkt = convolution(Q, kt, 6)
    C = []
    for j in range(7):
        C.append(saved_upper(emit(["C_matrix_angular_upper", j],
                                  arb(2) * d[j] + Qkt[j])))
    xR = convolution(x, R, 5)
    yR = convolution(y, R, 5)
    matrix_rest = [arb(2) * xR[j] + y[j] + yR[j] for j in range(6)]
    Qrest = convolution(Q, matrix_rest, 5)
    L = []
    for j in range(6):
        h = (q_r / q_lower + arb(4) * beta + arb(4) * base + arb(4) * d[1]
             if j == 0 else arb(4 * (j+1)) * d[j+1])
        L.append(saved_upper(emit(["L_matrix_angular_upper", j],
                                  h + Qrest[j] / arb(4))))
    # Whole working products below are inlined into the declared complete targets.
    # They are not independently saved old targets and are not used as substitutes.
    Vb0 = convolution(potential, b0, 5)
    Va0 = convolution(potential, a0, 5)
    Fae = [Fa[j] + Vb0[j] for j in range(6)]
    Fbe = [Fb[j] + Va0[j] for j in range(6)]
    q_left = convolution([x[j] + y[j] for j in range(6)], Fae, 5)
    q_right = convolution([y[j] + xR[j] for j in range(6)], Fbe, 5)
    q_all = convolution(Q, [q_left[j] + q_right[j] for j in range(6)], 5)
    qext = []
    for j in range(6):
        qext.append(saved_upper(emit(["q_ext_vector_angular_upper", j],
                                     q_all[j] / arb(2))))
    eC = convolution(e, C, 6)
    eL = convolution(e, L, 5)
    B = []
    for j in range(6):
        B.append(saved_upper(emit(["B_matrix_L1_angular_upper", j],
                                  arb(2) * ek[j] + arb(j+1) * eC[j+1] + eL[j])))
    M = [x[j] + y[j] for j in range(6)]
    eVQM = convolution(convolution(convolution(e, potential, 5), Q, 5), M, 5)
    D = []
    for j in range(6):
        D.append(saved_upper(emit(["D_matrix_L1_angular_upper", j], eVQM[j])))
    W0 = [a0[j] + b0[j] for j in range(6)]
    W1 = [a1[j] + b1[j] for j in range(6)]
    BW0, BW1 = convolution(B, W0, 5), convolution(B, W1, 5)
    DW0, DW1 = convolution(D, W0, 5), convolution(D, W1, 5)
    eq = convolution(e, qext, 5)
    for k in range(3):
        for j in range(6):
            value = BW0[j] if k == 0 else (BW1[j] + DW0[j] + eq[j]
                                           if k == 1 else DW1[j])
            emit(["amplitude_polynomial_L1_angular_upper", k, j], value)

def complete_five_mean_steps(saved, graphs, emit, copy_old):
    name = "complete_strict_flux_amplitudes"
    A = [[saved_upper(v) for v in row]
         for row in graphs[name]["new_records"]["amplitude_polynomial_L1_angular_upper"]]
    H = old_angular(saved, "wgs_Hinv", 5)
    potential = old_angular(saved, "ext_Vext", 5)
    y = old_angular(saved, "wgs_y", 5)
    correction = convolution(potential, y, 5)
    levels = []
    first = []
    for j in range(6):
        row = []
        for k in range(3):
            value = scalar_sum(H[a] * A[k][j-a] for a in range(j+1))
            row.append(saved_upper(emit(["complete_inverse_levels", 0, j, k], value)))
        first.append(row)
    levels.append(first)
    for ell in range(4):
        prior = levels[-1]
        rows, cols = 5-ell, 4+ell
        def prior_value(j, k):
            return prior[j][k] if 0 <= k < len(prior[j]) else arb(0)
        derivative = []
        for j in range(rows):
            derivative.append([
                arb(j+1) * prior_value(j+1, k)
                + scalar_sum(correction[a] * prior_value(j-a, k-1)
                             for a in range(j+1))
                for k in range(cols)])
        current = []
        for j in range(rows):
            row = []
            for k in range(cols):
                value = scalar_sum(H[a] * derivative[j-a][k] for a in range(j+1))
                row.append(saved_upper(emit(["complete_inverse_levels", ell+1, j, k], value)))
            current.append(row)
        levels.append(current)
    last = levels[4]
    terminal = []
    for k in range(8):
        first_term = last[1][k] if k < 7 else arb(0)
        second_term = correction[0] * last[0][k-1] if k > 0 else arb(0)
        terminal.append(saved_upper(emit(["complete_terminal_coefficients", k],
                                         first_term + second_term)))
    weighted = scalar_sum(terminal[k] / arb(388 ** k) for k in range(8))
    emit("complete_reflected_strict_mean_source_upper",
         arb(2) * saved_upper(saved["point_profile"]) * weighted)

def complete_new_strict_mean(saved, graphs, emit, copy_old):
    cf = saved_upper(graph_record(graphs, "complete_five_mean_recursions",
                                  "complete_reflected_strict_mean_source_upper"))
    z = emit("complete_strict_mean_upper",
             saved_upper(saved["strict_backward_factor"])
             * (rational(PARAMETERS["strict_cut"]) * cf
                + saved_upper(saved["local_mean"])))
    zr = emit("complete_strict_mean_derivative_upper",
              saved_upper(saved["strict_absolute_coefficient"]) * saved_upper(z) + cf)
    emit("complete_strict_raw_mean_source_upper",
         saved_upper(saved["strict_k0"]) * saved_upper(zr)
         + saved_upper(saved["strict_Tk"]) * saved_upper(z))
    emit("complete_strict_primitive_mean_source_upper",
         saved_upper(saved["strict_Ik"]) * saved_upper(zr)
         + saved_upper(saved["strict_Tk"]) * saved_upper(z) / arb(4))

def complete_new_negative_receiver(saved, graphs, emit, copy_old):
    old = lambda key: saved_upper(saved[key])
    source = "complete_strict_mean_and_affine_sources"
    strict_raw = saved_upper(graph_record(graphs, source, "complete_strict_raw_mean_source_upper"))
    mc = emit("complete_collar_raw_mean_union_upper",
              max(old("local_raw_mean_source"), strict_raw))
    mt = saved_upper(graph_record(graphs, source, "complete_strict_primitive_mean_source_upper"))
    collar = emit("complete_collar_ordinary_source_upper",
                  old("sqrt_two_upper") * old("ell_plus_one_fourth_upper")
                  * (old("collar_B_union") + old("collar_T_union") * old("N_minus5_6_upper"))
                  + old("sqrt_ell_plus_upper") * saved_upper(mc) * old("N_minus5_3_upper"))
    strict = emit("complete_strict_ordinary_source_upper",
                  rational(PARAMETERS["original_PW_cut"])
                  * (old("ell_minus_negative_fourth_upper")
                     * (old("strict_B_t") + old("strict_T_t") * old("N_minus1_2_upper"))
                     + mt * old("N_minus4_3_upper")))
    rc = emit("complete_collar_received_with_jumps_upper",
              old("C_O") * saved_upper(collar) + old("C_R") * old("jump_collar"))
    rs = emit("complete_strict_received_with_jumps_upper",
              old("C_1") * (saved_upper(strict) + old("jump_strict")))
    emit("complete_same_negative_error_upper",
         old("Bessel_prefactor")
         * (saved_upper(rc) * old("dyadic_one_third")
            + saved_upper(rs) * old("dyadic_two_thirds")))

def complete_new_endpoint(saved, graphs, emit, copy_old):
    z = saved_upper(graph_record(graphs, "complete_strict_mean_and_affine_sources",
                                 "complete_strict_mean_upper"))
    mean = emit("complete_physical_mean_endpoint_upper",
                saved_upper(saved["endpoint_Vz"]) * z * saved_upper(saved["Xi23_6"]))
    emit("complete_same_waist_endpoint_upper",
         saved_upper(saved["endpoint_scattering"])
         + saved_upper(saved["endpoint_second_order"])
         + saved_upper(saved["endpoint_WT"]) + saved_upper(mean))

def complete_new_errors(saved, graphs, emit, copy_old):
    negative = saved_upper(graph_record(graphs, "complete_negative_receiver",
                                        "complete_same_negative_error_upper"))
    endpoint = saved_upper(graph_record(graphs, "complete_waist_endpoint",
                                        "complete_same_waist_endpoint_upper"))
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
    require(which in ("whole", "reduced"), "same complete operator candidate")
    key = "complete_same_" + which + "_error_upper"
    new_path = ["complete_new_graphs", "complete_whole_and_reduced", "new_records", key]
    prior_path = ["copied_original_scalar_records", "prior_" + which]
    old_value = saved_upper(saved["prior_" + which])
    new_value = saved_upper(graph_record(graphs, "complete_whole_and_reduced", key))
    choose_new = bool(new_value < old_value)
    return {"selected_label": "new_strict_flux" if choose_new else "prior_complete_positive_weight",
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

        def save_record(path, record, is_new):
            path = [path] if isinstance(path, str) else list(path)
            target = at(NEW_GRAPH_SHAPES[name]["new_records"], path)
            require(isinstance(record, dict) and set(record) == {"ball"}
                    and isinstance(record["ball"], str), "complete record object")
            if is_new:
                require(target == {"ball": "__FINITE_SCALAR__"}, "new target specification")
            else:
                require(same_json(record, target), "original graph record must be exact")
            insert_new_record(doc["complete_new_graphs"][name]["new_records"], path, record)
            doc["saved_record_counts"][name] += 1
            if is_new:
                new_counts[name] += 1
                doc["actual_progress"]["new_records_saved"] += 1
            else:
                doc["actual_progress"]["original_records_copied_in_graphs"] += 1
            doc["stage"] = "record_saved:" + name
            restored = publish()
            return copy.deepcopy(at(restored["complete_new_graphs"][name]["new_records"], path))

        def emit(path, value):
            return save_record(path, {"ball": norm_upper(value).str(75)}, True)

        def copy_old(path, alias):
            require(name == ORDERED_GRAPH_NAMES[0]
                    and isinstance(path, list) and len(path) == 2
                    and path[0] == "pure_angular_background_pair_upper"
                    and type(path[1]) is int and path[1] in (0, 1)
                    and alias == "background_Q0_" + str(path[1]),
                    "two previously stored original graph records only")
            return save_record(path, doc["copied_original_scalar_records"][alias], False)
        return emit, copy_old

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
        doc["actual_progress"]["original_record_objects_copied"] = 131
        doc["actual_progress"]["original_qualification_objects_copied"] = 33
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
            ("complete_normalized_weight_L1_kernels", complete_normalized_weight),
            ("complete_strict_flux_amplitudes", complete_flux_amplitudes),
            ("complete_five_mean_recursions", complete_five_mean_steps),
            ("complete_strict_mean_and_affine_sources", complete_new_strict_mean),
            ("complete_negative_receiver", complete_new_negative_receiver),
            ("complete_waist_endpoint", complete_new_endpoint),
            ("complete_whole_and_reduced", complete_new_errors))
        require([name for name, _ in operations] == ORDERED_GRAPH_NAMES, "complete new graph order")
        for name, function in operations:
            emit, copy_old = start_graph(name)
            function(saved, doc["complete_new_graphs"], emit, copy_old)
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
        doc["failure"] = {
            "type": type(error).__name__,
            "message": message[:DIAGNOSTIC_MESSAGE_BYTES].decode("utf-8", "ignore"),
            "traceback": trace[:DIAGNOSTIC_TRACEBACK_BYTES].decode("utf-8", "ignore"),
            "message_truncated": len(message) > DIAGNOSTIC_MESSAGE_BYTES,
            "traceback_truncated": len(trace) > DIAGNOSTIC_TRACEBACK_BYTES}
        publish(check_size=False)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
