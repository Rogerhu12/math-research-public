#!/usr/bin/env python3
"""Complete WGS finite jets from frozen public scalar receipts and two old stages.

This is a new complete named-graph consumer. Old producers are AST evidence only.
The two historical gzip files are verified and decoded, never regenerated.
All new arithmetic runs only in the matching public GitHub Actions environment.
The old-input JSON and main science JSON are saved and printed in full separately.
"""
from __future__ import annotations
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.metadata
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
import time
import traceback
from fractions import Fraction
from flint import arb, ctx

PUBLIC = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE = TOPIC + "scripts/fourfold_codazzi_global_fold_free_transport_finite_jets.py"
WORKER = TOPIC + "scripts/fourfold_codazzi_global_fold_free_transport_finite_jets_public_worker.py"
KIND = "actual_complete_global_fold_free_transport_finite_jets_v1"
MANIFEST_KIND = "complete_global_fold_free_transport_finite_jets_public_inputs_v1"
ORIGINAL_INPUT_KIND = "complete_original_inputs_for_global_fold_free_transport_finite_jets_v1"
ORIGINAL_INPUT_FILENAME = "complete-original-inputs.json"
GATE_COUNT = 24
NEW_UPPER = "#U"
NEW_LOWER = "#L"
RUNTIME=json.loads("{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"}")
CURRENT_PIN_SPECS=json.loads("{\"wgs_contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-complete-global-fold-and-free-first-transport-finite-jets.md\",\"git_blob\":\"4980f1a2c119b6470afc24a2fc662c75fa210479\",\"bytes\":28978,\"sha256\":\"4d3638fe6ae8793b937d4c7f57a4c092d59d41df94991722d8b622ed958e576e\"},\"wui_contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-readonly-input-closure-for-the-global-genuine-waist-error.md\",\"git_blob\":\"730400be921fbdfd109b9c378a607cf768f674b6\",\"bytes\":31558,\"sha256\":\"2a77f1cd53a09c952daa8ba64eebe2bb80bb2e9735c6c78e3ceaba4223ad90d6\"},\"wua_contract\":{\"path\":\"topics/visible-flex-exact-nearby/results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md\",\"git_blob\":\"7b89251dcd51e8cb78fd3e8e42905114ef982ebf\",\"bytes\":40111,\"sha256\":\"9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad\"},\"fa_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json\",\"git_blob\":\"2001f4e2eeece1cda56b18b90dccab04b7f6d336\",\"bytes\":35718,\"sha256\":\"2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2\"},\"sj_execution\":{\"path\":\"topics/visible-flex-exact-nearby/notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json\",\"git_blob\":\"7dac244799016d9cae317a61f6c5dbe47ca0a013\",\"bytes\":46318,\"sha256\":\"2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88\"},\"wx_execution\":{\"path\":\"topics/visible-flex-exact-nearby/notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json\",\"git_blob\":\"5121a599896025d90e2861450756a256aaba659d\",\"bytes\":43753,\"sha256\":\"e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12\"},\"dza_science\":{\"path\":\"topics/visible-flex-exact-nearby/notes/fourth_angle_global_sign_budgets_ci/run-43773671216-1/actual-scientific-conclusion.json\",\"git_blob\":\"67b41ac717207f8696b637c667fb210088fca638\",\"bytes\":26909,\"sha256\":\"05036749a28c55499e2ed6fe47019cd31f4438652e3e6ab1319e6f9f2f2c4dba\"},\"fa_manifest\":{\"path\":\"topics/visible-flex-exact-nearby/notes/2026-11-15-R133-free-Airy-first-omitted-cut-scalars-CI-inputs.json\",\"git_blob\":\"8ff0dbf8a5042f30f7f31ad68f9c29d93a6af95e\",\"bytes\":23418,\"sha256\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\"},\"adjacent_process\":{\"path\":\"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/process.json\",\"git_blob\":\"26a04e8d7f79bc87623b149351599b328da4c427\",\"bytes\":37783,\"sha256\":\"9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b\"},\"adjacent_publication\":{\"path\":\"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/publication.json\",\"git_blob\":\"51b165e8b8d93a800524a5aab616f22196d7ed30\",\"bytes\":26496,\"sha256\":\"0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c\"},\"whole_process\":{\"path\":\"topics/visible-flex-exact-nearby/notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/consumers/process.json\",\"git_blob\":\"ad2035cbd7aed089c2be0fdd7f552243447373c0\",\"bytes\":8346,\"sha256\":\"242d82b6f1ead216bf8e90679a9952a2aaad0e9d7ba29293739911e70ab4d145\"},\"whole_publication\":{\"path\":\"topics/visible-flex-exact-nearby/notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/publication.json\",\"git_blob\":\"eb418b7ece29d12c0274c141364cf3c93dffaa15\",\"bytes\":11945,\"sha256\":\"fc3a190d8b701ef84188f2a37ee846c4f3669b5ac409faa5a6b72850162d1099\"},\"original_fa_source\":{\"path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_free_Airy_first_omitted_cut_scalars.py\",\"git_blob\":\"9e0a75461e0b8302a82e0444828a2c86379c3443\",\"bytes\":48827,\"sha256\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\"},\"original_adjacent_source\":{\"path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources.py\",\"git_blob\":\"380f628bbabdf146cba2f39b34204b63e92f736a\",\"bytes\":53824,\"sha256\":\"fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d\"},\"original_fold_algorithm\":{\"path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading.py\",\"git_blob\":\"27427dd6302b1d9c4ce8e0dd4a9d48fa15f920c3\",\"bytes\":32009,\"sha256\":\"410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783\"},\"original_whole_algorithm\":{\"path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_whole_physical_root_piece_first_Airy_sources.py\",\"git_blob\":\"327ecef0f265b88be9789212b4044afde9a28f22\",\"bytes\":51126,\"sha256\":\"66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81\"},\"math_module\":{\"path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_global_fold_free_transport_jet_math.py\",\"git_blob\":\"afa3b49b2035be07abee6a7f9041899c135dcdea\",\"bytes\":31846,\"sha256\":\"cb9c9aa0f7e5749967ece4e51210f359b4c58eecc7f83a05040607543ac47621\"}}")
HISTORICAL_INPUTS=json.loads("[{\"role\":\"fold_majorants_native\",\"path\":\"topics/visible-flex-exact-nearby/notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/stages/complete-original-reference-holomorphic-majorants.json.gz\",\"commit\":\"a3d84d905ce72e3a854874bbe98d119623f3f8de\",\"git_blob_sha\":\"fe180735fb6cbfaef8dff2ef68aa511ed3ac0643\",\"bytes\":4501,\"sha256\":\"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144\"},{\"role\":\"free_radius_native\",\"path\":\"topics/visible-flex-exact-nearby/notes/whole_physical_root_piece_first_Airy_sources_ci/run-43669106351-1/consumers/stages/complete-radius-budget-9-1000000.json.gz\",\"commit\":\"a3d84d905ce72e3a854874bbe98d119623f3f8de\",\"git_blob_sha\":\"786700a1a0da5cdb7a0dde90b1dd04eb586db860\",\"bytes\":20924,\"sha256\":\"8b31b1c0030f892ec763d32ecf7b4968d468c5f93b30bbfe7408d6bf0b4892d5\"}]")
RULES=json.loads("{\"path\":\"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json\",\"git_blob\":\"5c5d020913d717bb5bc8ce891297e00eaa8944f7\",\"bytes\":2461,\"sha256\":\"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1\"}")
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"expected_actual_gate_count\":24,\"expected_current_inputs\":20,\"expected_historical_inputs\":2,\"expected_total_inputs\":22,\"expected_immutable_AST_files\":7,\"expected_mathematical_input_roles\":19,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_strict_interval\":[\"0\",\"76285779072683/320000000000000\"],\"original_local_piece_label\":2549,\"exact_coefficient_strip\":\"1/32\",\"exact_fold_radius\":\"3/8000\",\"exact_fold_strip\":\"3/128\",\"exact_saved_free_radius\":\"9/1000000\",\"exact_saved_free_width\":\"1/512\",\"exact_old_free_holomorphic_radius\":\"1/6000\",\"exact_old_free_holomorphic_width\":\"1/128\",\"physical_frequency\":\"n=4|j|\",\"background_physical_bandwidth\":384,\"drift_label_bandwidth\":192,\"physical_drift_bandwidth\":768,\"actual_original_interfaces\":3070,\"derivative_convention\":\"ordinary one-sided radial derivatives and physical angular derivatives; complete Fourier A0 norms\",\"maximum_total_degree\":15,\"maximum_strict_radial_degree\":3,\"jet_shapes\":{\"geometry\":[15,3],\"leading\":[14,3],\"forcing\":[12,1],\"free_transport\":[12,2]},\"formal_radial_weight\":1,\"formal_angular_weight\":1,\"old_flow_derivatives_recomputed\":0,\"old_cut_phase_derivatives_recomputed\":0,\"old_free_amplitude_budgets_recomputed\":0,\"new_ray_ODE_solves\":0,\"new_scalar_exponentials\":0,\"new_scalar_logarithms\":0,\"old_producer_execution_allowed\":false,\"historical_gzip_input_only\":true,\"complete_genuine_potential_and_received_error_claimed\":false}")
RETAINED_SCOPE=json.loads("{\"same_original_real_family_and_fixed_intrinsic_eta0\":true,\"selected_true_radial_state_and_original_reflection\":true,\"complete_physical_means\":2,\"both_characteristic_branches_and_physical_signs\":true,\"complete_ordinary_one_sided_jets_only\":true,\"original_all_partial_intervals_and_interfaces_retained\":true,\"individual_root_Phi_radial_three_not_claimed\":true,\"local_analytic_X_T_and_regular_packet_separate\":true,\"old_full_complex_domains_only_used_on_qualified_local_piece\":true,\"old_free_w1_distinct_from_genuine_w1V\":true,\"old_whole_mathematics_success_and_formatter_failure_distinct\":true,\"ordinary_dr_transport_nonzero_cut_trace\":true,\"no_old_targets_recomputed\":true,\"new_complete_free_jet_graph_only\":true,\"genuine_potential_packet_proved\":false,\"complete_N6_received_source_constants_proved\":false,\"complete_four_endpoint_constants_proved\":false,\"root_or_waist_receiver_norms_newly_proved\":false,\"high_contraction_or_finite_border_inverse_proved\":false,\"physical_incoming_or_nonlinear_background_proved\":false}")
PUBLICATION_LIMITS=json.loads("{\"complete_science_max_bytes\":95000,\"complete_original_inputs_max_bytes\":50000,\"complete_report_max_bytes\":8000,\"complete_execution_max_bytes\":59000,\"complete_preGit_science_max_bytes\":95000,\"complete_preGit_original_inputs_max_bytes\":50000,\"complete_preGit_report_max_bytes\":8000,\"complete_preGit_execution_max_bytes\":59000,\"reserved_publication_bytes\":230000,\"all_four_preGit_payloads_are_complete_separate_files\":true}")
CURRENT_ROLE_ORDER=json.loads("[\"source\",\"math_module\",\"worker\",\"rules\",\"wgs_contract\",\"wui_contract\",\"wua_contract\",\"fa_science\",\"sj_execution\",\"wx_execution\",\"dza_science\",\"fa_manifest\",\"adjacent_process\",\"adjacent_publication\",\"whole_process\",\"whole_publication\",\"original_fa_source\",\"original_adjacent_source\",\"original_fold_algorithm\",\"original_whole_algorithm\"]")
COMPLETE_FIELDS=json.loads("[\"kind\",\"complete\",\"proved\",\"actual_returncode\",\"failure\",\"stage\",\"source_sha256\",\"math_module_sha256\",\"input_manifest_sha256\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"runtime\",\"arithmetic_bits\",\"parameters\",\"retained_scope\",\"planned_shape\",\"actual_progress\",\"gates\",\"actual_mathematical_wall_seconds\",\"input_sha256\",\"verified_original_inputs\",\"original_source_AST_evidence\",\"accepted_original_inputs\",\"complete_original_inputs_file\",\"complete_derivative_request_certificate\",\"complete_strict_coefficient_conclusion\",\"complete_higher_flow_and_cut_conclusion\",\"complete_strict_geometry_conclusion\",\"complete_strict_leading_conclusion\",\"complete_strict_forcing_conclusion\",\"complete_local_regular_packet_conclusion\",\"complete_free_first_transport_conclusion\",\"complete_named_global_graph_conclusion\"]")
ORIGINAL_INPUT_FIELDS=json.loads("[\"kind\",\"complete\",\"public_repository\",\"run_id\",\"run_attempt\",\"workflow_event_commit\",\"actual_scientific_checkout_commit\",\"source_sha256\",\"math_module_sha256\",\"input_manifest_sha256\",\"original_input_sha256\",\"copied_original_scalar_records\",\"copied_original_scalar_records_sha256\",\"copied_complete_original_scopes\",\"copied_complete_original_scopes_sha256\",\"copied_original_stage_records\",\"copied_original_stage_records_sha256\",\"copied_complete_local_coefficients\",\"copied_complete_local_coefficients_sha256\",\"local_coefficient_qualification\",\"copy_counts\",\"complete_readonly_input_projection\"]")
GATE_NAMES=json.loads("[\"actual public runtime and complete manifest identity\",\"twenty current small texts have their complete exact bytes\",\"two historical stages have exact immutable original identities\",\"seven Python AST files with four old producers never imported\",\"original complete free-Airy success and local domains\",\"original complete strict ordinary jets and all real intervals\",\"original shorter flows and two ungauged scalar directions\",\"original fourth derivatives and cut phase jets\",\"the original FA input chain remains exactly identified\",\"original adjacent child and full fold publication succeeded\",\"original whole child mathematics and formatter failure remain distinct\",\"complete original fold payload and all consumed holomorphic domains\",\"complete saved p0-p2 q0-q3 free records and exact FA overlap\",\"typed old records scopes and same original real family\",\"complete triangular derivative request certificate\",\"complete strict coefficient products with both physical means\",\"only new higher flow and cut derivatives with actual positive phase gap\",\"complete strict fold geometry and all retained lower denominators\",\"complete leading jets with original forward and reverse scalar fees\",\"complete first forcing with every drift theta and mean term\",\"complete local analytic packet and read-only free amplitude seeds\",\"complete free first transport with nonzero old cut trace\",\"complete named global graph and all original inputs unchanged\",\"complete thirty-six fields twenty-four gates and limited conclusion\"]")
PLANNED_SHAPE=json.loads("{\"current_inputs\":20,\"historical_inputs\":2,\"historical_bytes\":25425,\"immutable_AST_files\":7,\"mathematical_input_roles\":19,\"original_current_scalar_records\":66,\"original_stage_scalar_records\":40,\"original_complete_scope_objects\":9,\"new_complete_jet_graphs\":7,\"new_global_closure_graphs\":1,\"new_scalar_slots\":437,\"new_graph_slot_counts\":{\"complete_strict_coefficient_conclusion\":36,\"complete_higher_flow_and_cut_conclusion\":39,\"complete_strict_geometry_conclusion\":94,\"complete_strict_leading_conclusion\":38,\"complete_strict_forcing_conclusion\":83,\"complete_local_regular_packet_conclusion\":107,\"complete_free_first_transport_conclusion\":40,\"complete_named_global_graph_conclusion\":0},\"original_mathematical_targets_to_call\":0,\"old_complete_local_coefficient_objects\":1,\"local_coefficient_required_ball_count\":72,\"local_coefficient_extra_original_fields_preserved\":true}")
INITIAL_ACTUAL_PROGRESS=json.loads("{\"current_text_files_verified\":0,\"historical_stage_files_read\":0,\"historical_stage_bytes_read\":0,\"immutable_AST_files_checked\":0,\"old_scientific_receipts_admitted\":0,\"old_mathematical_stage_products_read\":0,\"old_current_scalar_records_copied\":0,\"old_historical_scalar_records_copied\":0,\"old_scope_objects_copied\":0,\"new_derivative_certificates\":0,\"new_strict_coefficient_graphs\":0,\"new_higher_flow_graphs\":0,\"new_strict_geometry_graphs\":0,\"new_strict_leading_graphs\":0,\"new_strict_forcing_graphs\":0,\"new_local_regular_graphs\":0,\"new_free_transport_graphs\":0,\"new_global_graph_conclusions\":0,\"new_scalar_slots_saved\":0,\"old_scientific_targets_recomputed\":0,\"old_producer_imports_or_calls\":0,\"old_rays_flows_exponentials_evaluated\":0,\"old_saved_free_budget_calls\":0,\"original_input_bytes_modified\":0,\"old_complete_local_coefficient_objects_copied\":0}")
SUCCESS_ACTUAL_PROGRESS=json.loads("{\"current_text_files_verified\":20,\"historical_stage_files_read\":2,\"historical_stage_bytes_read\":25425,\"immutable_AST_files_checked\":7,\"old_scientific_receipts_admitted\":4,\"old_mathematical_stage_products_read\":2,\"old_current_scalar_records_copied\":66,\"old_historical_scalar_records_copied\":40,\"old_scope_objects_copied\":9,\"new_derivative_certificates\":1,\"new_strict_coefficient_graphs\":1,\"new_higher_flow_graphs\":1,\"new_strict_geometry_graphs\":1,\"new_strict_leading_graphs\":1,\"new_strict_forcing_graphs\":1,\"new_local_regular_graphs\":1,\"new_free_transport_graphs\":1,\"new_global_graph_conclusions\":1,\"new_scalar_slots_saved\":437,\"old_scientific_targets_recomputed\":0,\"old_producer_imports_or_calls\":0,\"old_rays_flows_exponentials_evaluated\":0,\"old_saved_free_budget_calls\":0,\"original_input_bytes_modified\":0,\"old_complete_local_coefficient_objects_copied\":1}")
OLD_IDENTITIES=json.loads("{\"fa\":{\"kind\":\"actual_complete_free_Airy_first_omitted_cut_scalars_v1\",\"run_id\":\"43763658978\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"0c214d0b9b0c4cfa7c6ec363f253e419d14aae01\",\"actual_scientific_checkout_commit\":\"0c214d0b9b0c4cfa7c6ec363f253e419d14aae01\",\"source_sha256\":\"a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954\",\"input_manifest_sha256\":\"d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b\",\"runtime\":{\"Python\":\"3.12.14\",\"arithmetic_bits\":320,\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"field_count\":52,\"gate_count\":24,\"gate_sha256\":\"06860c1ba885d8676ab24fc1debaf795d015a3ea8a9697175a0e9c01fa2f5a05\",\"parameter_key\":\"mathematical_parameters\",\"parameter_sha256\":\"1dd546a7fbd67da27077a72569c9124062445986d8cb77682ad94eee3131b553\",\"stage\":\"complete-new-free-Airy-strong-cut-scalars\"},\"sj\":{\"kind\":\"actual_complete_strict_radial_first_symbol_defect_v1\",\"run_id\":\"43768006977\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"095ca270433abd339346790ffa35e4205b08b000\",\"actual_scientific_checkout_commit\":\"095ca270433abd339346790ffa35e4205b08b000\",\"source_sha256\":\"dfcf40ab948ea71ea80d733cd851602dcf5c78fdd83993e25f06664fc62b39d0\",\"input_manifest_sha256\":\"31602b830279bc5141950f3c34b70442f5a2997f872179b45effccb0ff3cdb48\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"arithmetic_bits\":320,\"field_count\":66,\"gate_count\":26,\"gate_sha256\":\"d753118fcff4893dbfa863509f5b85dfa72d9dc0c10d0f1a6f097e11de1f2f6b\",\"parameter_key\":\"mathematical_parameters\",\"parameter_sha256\":\"21da24e83a81c3156053a927774ab469ce91c20e0e4917095801d8d68cfb31df\",\"stage\":\"complete\"},\"wx\":{\"kind\":\"actual_true_waist_coordinates_from_saved_positive_products_v1\",\"run_id\":\"43763424840\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\",\"actual_scientific_checkout_commit\":\"cd14574e6b1bd74973214d57979305e5e3dfe41f\",\"source_sha256\":\"63fc880f409151152a40a6361b781280bd3785b337cf2bd3386c03496e1b9424\",\"input_manifest_sha256\":\"aa3c9d7e9f3a217122af5a321fadfcb2abe420e7e7c48217e3a181c9dbdd6f26\",\"runtime\":{\"numpy\":\"2.3.5\",\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"scipy\":\"1.17.0\"},\"arithmetic_bits\":320,\"field_count\":55,\"gate_count\":20,\"gate_sha256\":\"4c8f214fc05eaf3c8c3a9970a41921037356bf0f9021ef1b1ec942c485b90d47\",\"parameter_key\":\"mathematical_parameters\",\"parameter_sha256\":\"a0d15289f39599e00531eeaab70be7b469ef27b35de1d8593e9f365c23a7399b\"},\"dza\":{\"kind\":\"actual_fourth_angle_and_global_sign_budgets_v1\",\"run_id\":\"43773671216\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"2a7dc8cc3ab6d52287e034a9cb2f0302f020b8a6\",\"actual_scientific_checkout_commit\":\"2a7dc8cc3ab6d52287e034a9cb2f0302f020b8a6\",\"source_sha256\":\"5909e8da91d61bd2646941e18190fdd20dc98370e4563ff41526449658f75b28\",\"input_manifest_sha256\":\"296f84d4f05510525258bc563f2313ba34872256aa9131bcf3f6cd0489cb94af\",\"runtime\":{\"Python\":\"3.12.14\",\"python_flint\":\"0.9.0\"},\"arithmetic_bits\":320,\"field_count\":61,\"gate_count\":24,\"gate_sha256\":\"19774f5f2793d8b428ba1deae87c3c81e446f8d61ff43a80024827b44c6fa7b1\",\"parameter_key\":\"parameters\",\"parameter_sha256\":\"c27ceb81a2b4666a88238153c8cf15cd7c8912dac061ae3168fcda1d19393ba4\",\"stage\":\"complete\"}}")
OLD_PROCESS_IDENTITIES=json.loads("{\"adjacent\":{\"run_id\":\"43676926141\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"f111751254dc2bc3af41d5a647dca8b5d9b391e7\",\"actual_scientific_checkout_commit\":\"0326a07674e4c99a33995d1901463180a98e2f96\",\"source_sha256\":\"41282a7fb1f63f1a307a7ff721e4e1c553388613feb3c033013a9dfc10aaa2f5\",\"manifest_sha256\":\"57b978dbff16590d593686a8c7b98b8374aae532b500ec88cf975d3ab3821695\",\"mathematical_source_sha256\":\"fa344d170bca13c3faec22034aabbeab27da6116daef59f45c128c011998758d\",\"mathematical_gate_count\":14,\"mathematical_gates_sha256\":\"ef1d25f0187114f80cb6797eeace52792bf4c2a988b308c3067f0d60c6258273\",\"native_sha256\":\"5754193c193b9769eeec94bf6a9258489db14f9bfda758bf34a549d71c867a0f\",\"native_bytes\":42046},\"whole\":{\"run_id\":\"43669106351\",\"run_attempt\":\"1\",\"workflow_event_commit\":\"d549f0c80a0df695152fc883999007ad4f4edfe9\",\"actual_scientific_checkout_commit\":\"ef6f75878fc78981d3f75a056e7501f7131a37e0\",\"source_sha256\":\"855bcec6d31a9f0bdb3e3710c4e6418c2be0d816edf09a59da01ab6ec956904d\",\"manifest_sha256\":\"d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac\",\"mathematical_source_sha256\":\"66668065abd27ae37f789adf72a9deda9a15eda33d751f0c4b6fef8e54f17a81\",\"mathematical_gate_count\":10,\"mathematical_gates_sha256\":\"5cb0afffe99e4e8b01529f3ad323416754c95be1ded41fa16839fb6b3b89ce30\",\"native_sha256\":\"6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d\",\"native_bytes\":44628}}")
HISTORICAL_IDENTITIES=json.loads("{\"runtime\":{\"python\":\"3.12.14\",\"python_flint\":\"0.9.0\",\"numpy\":\"2.3.5\",\"scipy\":\"1.17.0\"},\"fold_source\":\"f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739\",\"fold_algebra\":\"1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53\",\"fold_manifest\":\"76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a\",\"fold_payload_sha256\":\"e0f1852f561b2596018e387a0b6c728441b665fee227e4c6fa85bc352060bf23\",\"free_payload_sha256\":\"e3658e369da9076e464c39eb6324f23d9685b5909e11a3b25e0d0bfb17761581\",\"free_manifest\":\"d30c306e58f3e6be96768b983db4df840843455e2cc5147c84c6e2d7958e5aac\",\"free_Taylor\":\"758a2901d194e9d54ec10bb5004014ee34a972c35367589fd5c86afce3f30c9f\",\"free_Nraw\":\"fbe1bce690f33335d2b024fe38a751743e0017e7d275b4d1fb0712be155f177e\",\"free_parent_native_sha256\":\"6668c9b2c8f1632e3bd8af392a803335f076c64e1d7fb74dfc9e1605f0e1ee2d\",\"free_parent_native_bytes\":44628,\"free_parent_formatter_failure\":{\"type\":\"TypeError\",\"message\":\"dict() got multiple values for keyword argument 'complete'\"}}")
SCALAR_PATHS=json.loads("{\"Q_0_0\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",0,0],\"direction\":\"upper\"},\"Q_0_1\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",0,1],\"direction\":\"upper\"},\"Q_0_2\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",0,2],\"direction\":\"upper\"},\"Q_0_3\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",0,3],\"direction\":\"upper\"},\"Q_1_0\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",1,0],\"direction\":\"upper\"},\"Q_1_1\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",1,1],\"direction\":\"upper\"},\"Q_1_2\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",1,2],\"direction\":\"upper\"},\"Q_1_3\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",1,3],\"direction\":\"upper\"},\"Q_2_0\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",2,0],\"direction\":\"upper\"},\"Q_2_1\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",2,1],\"direction\":\"upper\"},\"Q_2_2\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",2,2],\"direction\":\"upper\"},\"Q_2_3\":{\"role\":\"sj\",\"path\":[\"complete_original_body_and_polynomial_conclusion\",\"complete_Q_mixed_maxima\",2,3],\"direction\":\"upper\"},\"beta_0\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"beta\",0],\"direction\":\"upper\"},\"beta_1\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"beta\",1],\"direction\":\"upper\"},\"beta_2\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"beta\",2],\"direction\":\"upper\"},\"beta_3\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"beta\",3],\"direction\":\"upper\"},\"gamma_0\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"gamma\",0],\"direction\":\"upper\"},\"gamma_1\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"gamma\",1],\"direction\":\"upper\"},\"gamma_2\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"gamma\",2],\"direction\":\"upper\"},\"gamma_3\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"gamma\",3],\"direction\":\"upper\"},\"K_0\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"K\",0],\"direction\":\"upper\"},\"K_1\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"K\",1],\"direction\":\"upper\"},\"K_2\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"K\",2],\"direction\":\"upper\"},\"K_3\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_radial_0_3_absolute_maxima\",\"K\",3],\"direction\":\"upper\"},\"q_0\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_q_0_3_absolute_maxima\",0],\"direction\":\"upper\"},\"q_1\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_q_0_3_absolute_maxima\",1],\"direction\":\"upper\"},\"q_2\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_q_0_3_absolute_maxima\",2],\"direction\":\"upper\"},\"q_3\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_q_0_3_absolute_maxima\",3],\"direction\":\"upper\"},\"eta_lower\":{\"role\":\"sj\",\"path\":[\"complete_new_selected_intrinsic_conclusion\",\"complete_eta_lower\"],\"direction\":\"lower\"},\"q_lower\":{\"role\":\"sj\",\"path\":[\"complete_global_q_and_mean_conclusion\",\"complete_q_lower\"],\"direction\":\"lower\"},\"q_upper\":{\"role\":\"sj\",\"path\":[\"complete_global_q_and_mean_conclusion\",\"complete_q_upper\"],\"direction\":\"upper\"},\"t_cut_lower\":{\"role\":\"fa\",\"path\":[\"complete_new_cut_domain_conclusion\",\"complete_negative_T_real_lower\"],\"direction\":\"lower\"},\"t_cut_upper\":{\"role\":\"fa\",\"path\":[\"complete_new_cut_domain_conclusion\",\"complete_T_holomorphic_upper_read_from_original_full_Ap\"],\"direction\":\"upper\"},\"xdev_cut\":{\"role\":\"fa\",\"path\":[\"complete_new_cut_domain_conclusion\",\"complete_x_deviation_holomorphic\"],\"direction\":\"upper\"},\"y_cut\":{\"role\":\"fa\",\"path\":[\"complete_new_cut_domain_conclusion\",\"complete_y_holomorphic\"],\"direction\":\"upper\"},\"q_cut_lower\":{\"role\":\"fa\",\"path\":[\"complete_saved_cut_receiver_conclusion\",\"RR_ng_q_and_means_read_verbatim\",\"root_mean_value_q_bounds\",\"q_lower\"],\"direction\":\"lower\"},\"q_cut_upper\":{\"role\":\"fa\",\"path\":[\"complete_saved_cut_receiver_conclusion\",\"RR_ng_q_and_means_read_verbatim\",\"root_mean_value_q_bounds\",\"q_upper\"],\"direction\":\"upper\"},\"free_old_0_0\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",0],\"direction\":\"upper\"},\"free_old_0_1\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",1],\"direction\":\"upper\"},\"free_old_0_2\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",2],\"direction\":\"upper\"},\"free_old_0_3\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",3],\"direction\":\"upper\"},\"free_old_0_4\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",4],\"direction\":\"upper\"},\"free_old_0_5\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",5],\"direction\":\"upper\"},\"free_old_0_6\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1\",6],\"direction\":\"upper\"},\"free_old_1_0\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",0],\"direction\":\"upper\"},\"free_old_1_1\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",1],\"direction\":\"upper\"},\"free_old_1_2\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",2],\"direction\":\"upper\"},\"free_old_1_3\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",3],\"direction\":\"upper\"},\"free_old_1_4\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",4],\"direction\":\"upper\"},\"free_old_1_5\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",5],\"direction\":\"upper\"},\"free_old_1_6\":{\"role\":\"fa\",\"path\":[\"complete_new_initial_angular_jet_conclusion\",\"w1r\",6],\"direction\":\"upper\"},\"flow_1\":{\"role\":\"wx\",\"path\":[\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_derivative_upper\"],\"direction\":\"upper\"},\"flow_lower\":{\"role\":\"wx\",\"path\":[\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_derivative_lower\"],\"direction\":\"lower\"},\"flow_2\":{\"role\":\"wx\",\"path\":[\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_second_derivative_upper\"],\"direction\":\"upper\"},\"flow_3\":{\"role\":\"wx\",\"path\":[\"complete_shorter_flow_derivative_conclusion\",\"complete_shorter_flow_third_derivative_upper\"],\"direction\":\"upper\"},\"leading_forward\":{\"role\":\"wx\",\"path\":[\"complete_ungauged_leading_flow_conclusion\",\"complete_forward_radial_exponential_upper\"],\"direction\":\"upper\"},\"leading_reverse\":{\"role\":\"wx\",\"path\":[\"complete_ungauged_leading_flow_conclusion\",\"complete_reverse_radial_exponential_upper\"],\"direction\":\"upper\"},\"flow_4\":{\"role\":\"dza\",\"path\":[\"complete_new_fourth_angle_conclusion\",\"new_scalar_upper\",\"Hchi\"],\"direction\":\"upper\"},\"cut_phase_1\":{\"role\":\"dza\",\"path\":[\"copied_complete_scalar_inputs_read_verbatim\",\"P1\"],\"direction\":\"upper\"},\"cut_phase_2\":{\"role\":\"dza\",\"path\":[\"copied_complete_scalar_inputs_read_verbatim\",\"P2\"],\"direction\":\"upper\"},\"cut_phase_3\":{\"role\":\"dza\",\"path\":[\"copied_complete_scalar_inputs_read_verbatim\",\"P3\"],\"direction\":\"upper\"},\"cut_phase_4\":{\"role\":\"dza\",\"path\":[\"complete_new_fourth_angle_conclusion\",\"new_scalar_upper\",\"P4\"],\"direction\":\"upper\"},\"cut_t_1\":{\"role\":\"dza\",\"path\":[\"complete_new_fourth_angle_conclusion\",\"new_scalar_upper\",\"t1\"],\"direction\":\"upper\"},\"cut_t_2\":{\"role\":\"dza\",\"path\":[\"complete_new_fourth_angle_conclusion\",\"new_scalar_upper\",\"t2\"],\"direction\":\"upper\"},\"cut_t_3\":{\"role\":\"dza\",\"path\":[\"complete_new_fourth_angle_conclusion\",\"new_scalar_upper\",\"t3\"],\"direction\":\"upper\"},\"cut_t_4\":{\"role\":\"dza\",\"path\":[\"complete_new_fourth_angle_conclusion\",\"new_scalar_upper\",\"t4\"],\"direction\":\"upper\"}}")
SCOPE_PATHS=json.loads("{\"fa_parameters\":{\"role\":\"fa\",\"path\":[\"mathematical_parameters\"]},\"sj_parameters\":{\"role\":\"sj\",\"path\":[\"mathematical_parameters\"]},\"sj_scope\":{\"role\":\"sj\",\"path\":[\"scope\"]},\"wx_parameters\":{\"role\":\"wx\",\"path\":[\"mathematical_parameters\"]},\"wx_scope\":{\"role\":\"wx\",\"path\":[\"scope\"]},\"wx_flow\":{\"role\":\"wx\",\"path\":[\"complete_shorter_flow_derivative_conclusion\"]},\"wx_leading\":{\"role\":\"wx\",\"path\":[\"complete_ungauged_leading_flow_conclusion\"]},\"dza_parameters\":{\"role\":\"dza\",\"path\":[\"parameters\"]},\"dza_scope\":{\"role\":\"dza\",\"path\":[\"scope\"]}}")
LOCAL_COEFFICIENT_QUALIFICATION=json.loads("{\"original_path\":\"payload.coefficients\",\"original_full_stage_sha256\":\"29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144\",\"original_full_payload_sha256\":\"e0f1852f561b2596018e387a0b6c728441b665fee227e4c6fa85bc352060bf23\",\"array_convention\":\"full component Wiener norms of ordinary radial and physical angular derivatives; no factorial division\",\"full_U_and_V_shape\":[4,5],\"exact_original_coefficient_strip\":\"1/32\",\"actual_root_centered_disk_used_by_fold\":\"3/8000\",\"real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"same_original_piece\":2549,\"radial_r_and_rho_absolute_derivatives_identical\":true,\"not_root_circle_only\":true,\"all_original_coefficient_fields_copied\":true,\"missing_higher_derivatives_not_inferred\":true,\"complete_original_source_path\":\"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading.py\",\"complete_original_source_sha256\":\"410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783\",\"exact_original_auxiliary_input_radius\":\"1/2000\",\"exact_complete_consumed_coefficient_radius\":\"3/8000\",\"exact_identity_with_original_family_only_on_original_germ_intersection\":true}")
DERIVATIVE_CERTIFICATE=json.loads("{\"normalized_coefficients\":\"ordinary derivative norm divided by a! b!\",\"formal_radial_weight\":1,\"formal_angular_weight\":1,\"allowed_indices\":\"0<=a<=p; b>=0; a+b<=m\",\"fixed_degree_groups\":[[0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15]],\"reconstruction\":\"a! b! times the upper for the group containing a+b\",\"strict_shapes\":{\"phase_derivatives\":[15,3],\"X_derivatives\":[15,3],\"omega\":[15,3],\"t\":[15,3],\"x\":[14,3],\"y\":[14,3],\"Q\":[13,2],\"determinant\":[13,2],\"mu_inverse\":[13,2],\"H_inverse_entry_sum\":[13,2],\"G\":[14,3],\"a0\":[14,3],\"b0\":[14,3],\"v0\":[12,2],\"Fb\":[12,1],\"Fa\":[12,1],\"transport_kernel\":[12,1],\"R\":[12,2],\"a1\":[12,2],\"b1\":[12,2]},\"local_shapes\":{\"X_minus_phi\":[15,3],\"T\":[15,3],\"G\":[14,3],\"Q\":[13,2],\"H_inverse_entry_sum\":[13,2],\"mu_inverse\":[13,2],\"a0\":[14,3],\"b0\":[14,3],\"Fb\":[12,1],\"Fa\":[12,1],\"a1\":[12,2],\"b1\":[12,2]},\"ordered_predecessors\":{\"phase_derivatives\":[[\"flow\",15,0],[\"a_sigma\",14,2]],\"t\":[[\"phase_derivatives\",15,3]],\"x\":[[\"phase_derivatives\",15,3]],\"y\":[[\"t\",15,3]],\"G\":[[\"t\",14,3],[\"q\",3,3],[\"ell0\",2,2]],\"w0\":[[\"G\",14,3],[\"x\",14,3],[\"y\",14,3],[\"t\",14,3]],\"forcing\":[[\"w0\",14,3],[\"background\",14,2],[\"eta\",2,2],[\"Q\",12,1],[\"mu_inverse\",12,1]],\"transport_kernel\":[[\"forcing\",12,1],[\"v0\",12,1],[\"Q\",12,1],[\"phase_derivatives\",13,1],[\"t\",12,1]],\"free_w1\":[[\"transport_kernel\",12,1],[\"v0\",12,2],[\"a_sigma\",11,1],[\"flow\",12,0],[\"t\",12,2]]},\"phase_value_not_a_periodic_function\":true,\"no_root_radial_three_bound_for_individual_Phi\":true,\"new_genuine_potential_packet_included\":false,\"all_product_indices_checked_before_their_arithmetic\":true}")
NEW_GRAPH_SHAPES=json.loads("{\"complete_strict_coefficient_conclusion\":{\"new_jets\":{\"eta\":{\"shape\":[15,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"d\":{\"shape\":[15,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"a_sigma\":{\"shape\":[15,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"ell0\":{\"shape\":[14,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"background_pair_used_as_each_component_upper\":true,\"full_physical_mean_kept\":true,\"old_Qmixed_and_intrinsic_jets_read_only\":true,\"new_target\":\"whole strict coefficient products, not old per-piece rows\"},\"complete_higher_flow_and_cut_conclusion\":{\"flow_orders_5_through_15\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"cut_phase_orders_5_through_15\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"complete_strict_phase_angular_orders_1_through_15\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"cut_phase_lower\":\"#L\",\"strict_phase_lower\":\"#L\",\"old_flow_1_through_4_recomputed\":0,\"old_cut_phase_1_through_4_recomputed\":0,\"all_shorter_intervals_both_branches_both_orientations\":true},\"complete_strict_geometry_conclusion\":{\"complete_jets\":{\"phase_derivatives\":{\"shape\":[15,3],\"group_upper\":[null,\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":true},\"X_derivatives\":{\"shape\":[15,3],\"group_upper\":[null,\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":true},\"omega\":{\"shape\":[15,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"t\":{\"shape\":[15,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"x\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"y\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"Q\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"determinant\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"mu_inverse\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"H_inverse_entry_sum\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"complete_positive_lowers\":{\"determinant\":\"#L\",\"Q_fold\":\"#L\",\"mu\":\"#L\",\"whole_t_over_rho\":\"#L\"},\"t_over_rho_candidates\":{\"local\":\"#L\",\"strict\":\"#L\"},\"strict_minus_T_lower_is_old_cut_lower\":true,\"root_Phi_radial_derivatives_not_asserted\":true,\"ordinary_one_sided_r_and_full_real_lifts\":true},\"complete_strict_leading_conclusion\":{\"complete_jets\":{\"G\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"a0\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"b0\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"v0\":{\"shape\":[12,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"complete_G_upper\":\"#U\",\"complete_G_lower\":\"#L\",\"complete_v0_lower\":\"#L\",\"forward_and_reverse_old_scalar_fees_used_in_their_own_direction\":true,\"new_scalar_flow_exponentials\":0,\"v0_positive_identity\":\"G times Phi_sigma_phi squared\",\"log_derivative_signs_replaced_only_by_complete_positive_triangle\":true},\"complete_strict_forcing_conclusion\":{\"complete_forcing_jets\":{\"Fb\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"Fa\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"complete_coefficient_jets\":{\"e\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"b_local\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"ell\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"tQ\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"T0\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"rQ\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"theta\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"V0\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"both_components\":true,\"full_theta_Q_KT_product_present\":true,\"full_second_order_drift_and_original_means_present\":true,\"background_ordinary_radial_order_max\":2,\"leading_ordinary_radial_order_max\":3,\"no_old_forcing_target_executed\":true},\"complete_local_regular_packet_conclusion\":{\"complete_jets\":{\"X_minus_phi\":{\"shape\":[15,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"T\":{\"shape\":[15,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"G\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"Q\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"a0\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"b0\":{\"shape\":[14,3],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"Fb\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"Fa\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"H_inverse_entry_sum\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"mu_inverse\":{\"shape\":[13,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"a1\":{\"shape\":[12,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"b1\":{\"shape\":[12,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"local_cover_saved_h_margin\":\"#L\",\"complete_local_H_inverse_holomorphic_upper\":\"#U\",\"complete_local_mu_inverse_holomorphic_upper\":\"#U\",\"free_p0_p1_p2_q0_through_q3_recomputed\":0,\"old_FA_free_orders_through_six_recomputed\":0,\"both_old_component_tables_read\":true,\"free_and_genuine_amplitude_distinct\":true,\"individual_Phi_radial_jets_at_root_not_used\":true,\"local_original_piece_label\":2549,\"local_to_strict_function_identity\":\"same actual root-normalized germ at rc\"},\"complete_free_first_transport_conclusion\":{\"complete_jets\":{\"transport_kernel\":{\"shape\":[12,1],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"R\":{\"shape\":[12,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"a1\":{\"shape\":[12,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"b1\":{\"shape\":[12,2],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false}},\"complete_cut_ratio_angular_jet\":{\"shape\":[12,0],\"group_upper\":[\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\",\"#U\"],\"value_omitted_for_lift\":false},\"both_characteristic_branches_and_physical_signs\":true,\"old_root_trace_preserved_at_cut\":true,\"ordinary_fixed_dr_endpoints_and_all_partial_intervals\":true,\"actual_original_interfaces_retained\":3070,\"old_free_amplitude_targets_recomputed\":0,\"new_ray_integrations\":0,\"new_scalar_exponential_evaluations\":0,\"genuine_potential_addition_included\":false},\"complete_named_global_graph_conclusion\":{\"complete_named_global_free_jet_graph\":true,\"same_actual_functions_on_the_common_cut\":true,\"patch_links\":{\"X\":[\"strict_geometry.X_derivatives\",\"local.X_minus_phi\"],\"T\":[\"strict_geometry.t\",\"local.T\"],\"Q\":[\"strict_geometry.Q\",\"local.Q\"],\"H_inverse\":[\"strict_geometry.H_inverse_entry_sum\",\"local.H_inverse_entry_sum\"],\"mu_inverse\":[\"strict_geometry.mu_inverse\",\"local.mu_inverse\"],\"G\":[\"strict_leading.G\",\"local.G\"],\"a0\":[\"strict_leading.a0\",\"local.a0\"],\"b0\":[\"strict_leading.b0\",\"local.b0\"],\"Fb\":[\"strict_forcing.Fb\",\"local.Fb\"],\"Fa\":[\"strict_forcing.Fa\",\"local.Fa\"],\"a1\":[\"strict_transport.a1\",\"local.a1\"],\"b1\":[\"strict_transport.b1\",\"local.b1\"]},\"union_bound_rule\":\"max of the two already complete patch bounds after their common identity\",\"X_local_rule\":\"add the exact identity derivative at (0,1); omit the lift value\",\"T_strict_rule\":\"T=-t, with identical absolute derivative bounds\",\"normalization\":\"old root-normalized free first transport; original fixed intrinsic eta0\",\"ordinary_one_sided_derivatives\":true,\"physical_angular_frequency\":4,\"independent_physical_means_retained\":true,\"actual_nonlinear_background_proved\":false,\"complete_genuine_potential_packet_proved\":false,\"complete_N6_residual_constants_proved\":false,\"complete_negative_receiver_constant_proved\":false,\"complete_four_waist_endpoint_constants_proved\":false,\"high_contraction_proved\":false,\"finite_or_incoming_inverse_proved\":false}}")
NEW_GRAPH_SLOT_COUNTS=json.loads("{\"complete_strict_coefficient_conclusion\":36,\"complete_higher_flow_and_cut_conclusion\":39,\"complete_strict_geometry_conclusion\":94,\"complete_strict_leading_conclusion\":38,\"complete_strict_forcing_conclusion\":83,\"complete_local_regular_packet_conclusion\":107,\"complete_free_first_transport_conclusion\":40,\"complete_named_global_graph_conclusion\":0}")
FROZEN_OLD_COPY_HASHES=json.loads("{\"scalar_records\":\"5aa27845005a14774eaa4c3d01509dcd8e8869d6b1e2e7a0f588f346487e608e\",\"complete_scopes\":\"986561d54c780e1ff9d121110e473594aac8f96cd36552fc7b85d9d657a0cd2f\"}")


def require(condition, message):
    if not condition:
        raise ValueError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")

def old_payload_bytes(value):
    # Exactly the original saved-stage algorithm: compact sorted JSON, no LF.
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      allow_nan=False).encode("utf-8")

def reject_nonfinite(token):
    raise ValueError("nonfinite JSON token: " + token)

def read_json(path):
    raw = Path(path).read_bytes()
    if Path(path).suffix == ".gz":
        raw = gzip.decompress(raw)
    return json.loads(raw, parse_constant=reject_nonfinite)

def get_path(value, path):
    for key in path:
        value = value[key]
    return value

def exact_literal(tree, name):
    values = [node.value for node in tree.body
              if isinstance(node, ast.Assign)
              and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)]
    require(len(values) == 1, "one immutable literal required: " + name)
    return ast.literal_eval(values[0])

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

def print_complete_document(doc, original_inputs=False):
    label = ("ORIGINAL_INPUTS" if original_inputs else "SCIENCE")
    prefix = "COMPLETE_GLOBAL_FOLD_FREE_TRANSPORT_FINITE_JETS_" + label + "_JSON"
    print("BEGIN_" + prefix, flush=True)
    print(canonical(doc).decode("utf-8"), end="", flush=True)
    print("END_" + prefix, flush=True)

def operation_excerpt(text, limit, keep_tail=False):
    escaped = json.dumps(str(text), ensure_ascii=False)
    if len(escaped.encode("utf-8")) <= limit:
        return str(text), False
    # A published diagnostic is not a mathematical record. The unabridged
    # diagnostic is printed first; this only bounds its separate JSON summary.
    result = str(text)
    while result and len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > limit:
        result = result[1:] if keep_tail else result[:-1]
    return result, True

def operation_failure(error):
    original = {"type": type(error).__name__, "message": str(error),
                "traceback": traceback.format_exc()}
    print("BEGIN_UNABRIDGED_OPERATION_DIAGNOSTIC", flush=True)
    for key in ("type", "message", "traceback"):
        print(key + ": " + original[key], flush=True)
    print("END_UNABRIDGED_OPERATION_DIAGNOSTIC", flush=True)
    result, shortened = {}, False
    for key, limit, tail in (("type", 64, False), ("message", 256, False),
                             ("traceback", 2048, True)):
        result[key], truncated = operation_excerpt(original[key], limit, tail)
        shortened = shortened or truncated
    result["text_truncated"] = shortened
    result["full_text_in_job_log"] = True
    return result

def record_is_finite(value, positive_lower=False):
    if not isinstance(value, dict) or set(value) != {"ball"} or not isinstance(value["ball"], str):
        return False
    x = arb(value["ball"])
    return x.is_finite() and (x.lower() > 0 if positive_lower else x.upper() >= 0)

def original_record(value, label):
    require(record_is_finite(value), "invalid complete original ball: " + label)
    return copy.deepcopy(value)

def all_original_balls(value, path="payload"):
    if isinstance(value, dict):
        if set(value) == {"ball"}:
            require(record_is_finite(value), "nonfinite original ball at " + path)
            return 1
        return sum(all_original_balls(v, path + "." + str(k)) for k, v in value.items())
    if isinstance(value, list):
        return sum(all_original_balls(v, path + "[" + str(i) + "]") for i, v in enumerate(value))
    return 0

def complete_graph_shape(value, shape, path="new_graph"):
    if isinstance(shape, str) and shape in (NEW_UPPER, NEW_LOWER):
        require(record_is_finite(value, shape == NEW_LOWER),
                "nonfinite complete new ball at " + path)
        return True
    if isinstance(shape, dict):
        require(isinstance(value, dict) and set(value) == set(shape),
                "complete object shape mismatch at " + path)
        return all(complete_graph_shape(value[k], v, path + "." + k) for k, v in shape.items())
    if isinstance(shape, list):
        require(isinstance(value, list) and len(value) == len(shape),
                "complete list shape mismatch at " + path)
        return all(complete_graph_shape(v, s, path + "[" + str(i) + "]")
                   for i, (v, s) in enumerate(zip(value, shape)))
    require(value == shape and type(value) is type(shape), "fixed shape value changed at " + path)
    return True

def scalar_slot_count(shape):
    if isinstance(shape, str) and shape in (NEW_UPPER, NEW_LOWER):
        return 1
    if isinstance(shape, dict):
        return sum(scalar_slot_count(v) for v in shape.values())
    if isinstance(shape, list):
        return sum(scalar_slot_count(v) for v in shape)
    return 0

def mathematical_pin_specs():
    result = copy.deepcopy(CURRENT_PIN_SPECS)
    for entry in HISTORICAL_INPUTS:
        result[entry["role"]] = {"path": entry["path"], "git_blob": entry["git_blob_sha"],
                                 "bytes": entry["bytes"], "sha256": entry["sha256"]}
    return result

def checked_inputs(args, doc):
    runtime = {"Python": platform.python_version(),
               "python_flint": importlib.metadata.version("python-flint")}
    doc["runtime"] = runtime
    gate(doc, 0, os.environ.get("GITHUB_ACTIONS") == "true"
         and os.environ.get("GITHUB_REPOSITORY") == PUBLIC
         and runtime == RUNTIME and args.bits == ctx.prec == 320
         and doc["input_manifest_sha256"] == args.manifest_sha
         and re.fullmatch(r"[0-9a-f]{40}", doc["actual_scientific_checkout_commit"] or "") is not None
         and re.fullmatch(r"[0-9a-f]{40}", doc["workflow_event_commit"] or "") is not None
         and re.fullmatch(r"[0-9]+", doc["run_id"] or "") is not None
         and re.fullmatch(r"[0-9]+", doc["run_attempt"] or "") is not None)
    manifest = read_json(args.manifest)
    expected = {"source": SOURCE, "worker": WORKER, "rules": RULES["path"]}
    expected.update({k: v["path"] for k, v in CURRENT_PIN_SPECS.items()})
    expected = {role: expected[role] for role in CURRENT_ROLE_ORDER}
    entries = manifest.get("files", [])
    by_role = {entry.get("role"): entry for entry in entries}
    require(manifest.get("kind") == MANIFEST_KIND and manifest.get("public_repository") == PUBLIC,
            "new manifest identity")
    require(len(entries) == len(by_role) == 20 and set(by_role) == set(expected),
            "exact current input closure")
    paths = {role: args.repo / Path(path) for role, path in expected.items()}
    verified = {}
    trees = {}
    for role in CURRENT_ROLE_ORDER:
        path, entry = paths[role], by_role[role]
        data = path.read_bytes()
        require(entry["path"] == expected[role] and 0 < len(data) < 100000
                and path.suffix in (".py", ".json", ".md"), "small current text: " + role)
        data.decode("utf-8")
        require(not data.startswith(b"\x1f\x8b"), "current inputs are plain UTF-8")
        require(len(data) == entry["bytes"] and sha(data) == entry["sha256"]
                and git_blob(data) == entry["git_blob"], "complete current identity: " + role)
        if role in CURRENT_PIN_SPECS:
            require({k: entry[k] for k in ("path", "git_blob", "bytes", "sha256")}
                    == CURRENT_PIN_SPECS[role], "fixed current pin: " + role)
            verified[role] = {"bytes": len(data), "sha256": sha(data)}
        if role == "rules":
            require(all(entry[k] == RULES[k] for k in ("path", "git_blob", "bytes", "sha256")),
                    "reviewed rules changed")
        if path.suffix == ".py":
            trees[role] = ast.parse(data.decode("utf-8"), filename=entry["path"])
    gate(doc, 1, manifest.get("source_path") == SOURCE
         and manifest.get("source_sha256") == doc["source_sha256"]
         and manifest.get("parameters") == PARAMETERS
         and manifest.get("scope") == RETAINED_SCOPE
         and manifest.get("publication_limits") == PUBLICATION_LIMITS
         and manifest.get("expected_actual_gate_count") == 24
         and manifest.get("expected_current_input_count") == 20
         and manifest.get("expected_input_count") == 22
         and manifest.get("expected_immutable_AST_files") == 7
         and manifest.get("current_text_input_roles") == CURRENT_ROLE_ORDER
         and manifest.get("current_input_paths") == list(expected.values())
         and manifest.get("file_sha256") == {e["path"]: e["sha256"] for e in entries}
         and by_role["source"]["sha256"] == sha(Path(__file__).read_bytes()))
    doc["actual_progress"]["current_text_files_verified"] = 20
    for entry in HISTORICAL_INPUTS:
        role = entry["role"]
        path = args.repo / Path(entry["path"])
        data = path.read_bytes()
        require(path.suffix == ".gz" and data.startswith(b"\x1f\x8b"),
                "only the two original gzip inputs")
        require(len(data) == entry["bytes"] and sha(data) == entry["sha256"]
                and git_blob(data) == entry["git_blob_sha"],
                "complete historical identity: " + role)
        paths[role] = path
        verified[role] = {"bytes": len(data), "sha256": sha(data)}
    all_paths = dict(expected)
    all_paths.update({e["role"]: e["path"] for e in HISTORICAL_INPUTS})
    gate(doc, 2, manifest.get("historical_inputs") == HISTORICAL_INPUTS
         and manifest.get("historical_input_roles") == [e["role"] for e in HISTORICAL_INPUTS]
         and manifest.get("historical_input_paths") == [e["path"] for e in HISTORICAL_INPUTS]
         and manifest.get("input_paths") == all_paths
         and manifest.get("legacy_artifact_inputs") == []
         and manifest.get("all_inputs_are_current_small_texts") is False
         and manifest.get("old_successful_scientific_calls_allowed") is False
         and manifest.get("new_native_arrays_or_artifact_persistence_allowed") is False
         and manifest.get("complete_input_bytes")
             == sum(e["bytes"] for e in entries) + sum(e["bytes"] for e in HISTORICAL_INPUTS)
         and manifest.get("mathematical_input_sha256")
             == {k: v["sha256"] for k, v in mathematical_pin_specs().items()})
    doc["actual_progress"]["historical_stage_files_read"] = 2
    doc["actual_progress"]["historical_stage_bytes_read"] = 25425
    required_functions = {
        "original_fa_source": ("original_fold", "original_free_radius"),
        "original_adjacent_source": ("reference_majorants",),
        "original_fold_algorithm": ("anchored_coefficients", "fold_budget"),
        "original_whole_algorithm": ("radius_budget",),
        "math_module": ("derivative_certificate", "complete_strict_coefficients",
                        "complete_higher_flow_and_cut", "complete_strict_geometry",
                        "complete_strict_leading", "complete_strict_forcing",
                        "complete_local_regular_packet", "complete_free_first_transport",
                        "complete_global_packet_conclusion"),
    }
    for role, names in required_functions.items():
        actual = {node.name for node in trees[role].body if isinstance(node, ast.FunctionDef)}
        require(set(names) <= actual, "immutable function definitions: " + role)
    old_fa = trees["original_fa_source"]
    gate(doc, 3, len(trees) == 7
         and exact_literal(old_fa, "OLD_RUNTIME") == HISTORICAL_IDENTITIES["runtime"]
         and exact_literal(old_fa, "LEGACY_SOURCE") == HISTORICAL_IDENTITIES["fold_source"]
         and exact_literal(old_fa, "LEGACY_HELPER") == HISTORICAL_IDENTITIES["fold_algebra"]
         and exact_literal(old_fa, "LEGACY_MANIFEST") == HISTORICAL_IDENTITIES["fold_manifest"]
         and exact_literal(old_fa, "WHOLE_TAYLOR") == HISTORICAL_IDENTITIES["free_Taylor"]
         and exact_literal(old_fa, "WHOLE_NRAW") == HISTORICAL_IDENTITIES["free_Nraw"]
         and CURRENT_PIN_SPECS["math_module"]["sha256"] == doc["math_module_sha256"])
    doc["actual_progress"]["immutable_AST_files_checked"] = 7
    doc["verified_original_inputs"] = verified
    doc["input_sha256"] = {k: v["sha256"] for k, v in mathematical_pin_specs().items()}
    doc["input_sha256"]["manifest"] = doc["input_manifest_sha256"]
    doc["original_source_AST_evidence"] = {
        "count": 7, "roles": [k for k in CURRENT_ROLE_ORDER if k in trees],
        "old_source_imports": 0, "new_module_sha256": doc["math_module_sha256"],
        "four_old_producers_are_AST_and_literal_evidence_only": True}
    return manifest, paths

def original_science(paths, name, role):
    container = read_json(paths[role])
    if name in ("sj", "wx"):
        require(container.get("complete") is True and container.get("actual_returncode") == 0
                and container.get("actual_failure") is None,
                "old embedded execution did not finish: " + name)
        value = container["actual_scientific_receipt"]
        require(container["actual_scientific_checkout_commit"]
                == value["actual_scientific_checkout_commit"]
                and container["source_budget_source_sha256"] == value["source_sha256"]
                and container["input_manifest_sha256"] == value["input_manifest_sha256"],
                "embedded old science identity: " + name)
    else:
        value = container
    expected = OLD_IDENTITIES[name]
    for key in ("kind", "run_id", "run_attempt", "workflow_event_commit",
                "actual_scientific_checkout_commit", "source_sha256",
                "input_manifest_sha256", "runtime", "arithmetic_bits"):
        require(value.get(key) == expected[key], "old exact identity: " + name + "." + key)
    if "stage" in expected:
        require(value.get("stage") == expected["stage"], "old actual stage: " + name)
    require(len(value) == expected["field_count"]
            and value.get("complete") is True and value.get("proved") is True
            and value.get("failure") is None and value.get("actual_returncode") == 0
            and len(value["gates"]) == expected["gate_count"]
            and all(g["passed"] is True for g in value["gates"])
            and sha(canonical(value["gates"])) == expected["gate_sha256"]
            and sha(canonical(value[expected["parameter_key"]]))
                == expected["parameter_sha256"], "complete old success: " + name)
    return value

def process_identity(value, name):
    expected = OLD_PROCESS_IDENTITIES[name]
    for key in ("run_id", "run_attempt", "workflow_event_commit",
                "actual_scientific_checkout_commit", "source_sha256",
                "manifest_sha256", "mathematical_source_sha256",
                "native_sha256", "native_bytes"):
        require(value.get(key) == expected[key], "old process identity: " + name + "." + key)
    require(len(value["mathematical_gates"]) == expected["mathematical_gate_count"]
            and all(g["passed"] is True for g in value["mathematical_gates"])
            and sha(canonical(value["mathematical_gates"]))
                == expected["mathematical_gates_sha256"],
            "complete old mathematical gate ledger: " + name)

def publication_entry(publication, name, historical):
    entries = [e for e in publication["files"] if e["file"] == name]
    require(len(entries) == 1 and entries[0]["bytes"] == historical["bytes"]
            and entries[0]["sha256"] == historical["sha256"]
            and entries[0].get("original_sha256", historical["sha256"])
                == historical["sha256"], "complete original stage publication: " + name)
    return entries[0]

def accepted_original_inputs(paths, doc):
    old = {}
    old["fa"] = original_science(paths, "fa", "fa_science")
    gate(doc, 4, old["fa"]["original_complete_fold_and_radius_stages_read"] == 2
         and old["fa"]["old_numerical_enclosures_recomputed"] == 0
         and old["fa"]["old_scientific_source_imports"] == 0
         and old["fa"]["complete_saved_free_amplitude_conclusion"]["free_w1_is_not_genuine_w1V"] is True
         and old["fa"]["mathematical_parameters"]["physical_root_piece"] == 2549)
    doc["actual_progress"]["old_scientific_receipts_admitted"] += 1

    old["sj"] = original_science(paths, "sj", "sj_execution")
    sj = old["sj"]
    gate(doc, 5, sj["complete_original_body_and_polynomial_conclusion"]["original_consumed_rows"] == 3071
         and sj["complete_original_body_and_polynomial_conclusion"]["qualified_polynomial_intervals"] == 2550
         and sj["complete_original_body_and_polynomial_conclusion"]["original_restored_rows"] == 3322
         and sj["mathematical_parameters"]["derivative_convention"]
             == "ordinary radial and angular derivatives; complete component Fourier A0 sum"
         and sj["scope"]["full_angular_Wiener_A0_budgets_not_pointwise_bounds_used_in_finite_band_rule"] is True
         and sj["scope"]["only_one_sided_ordinary_radial_derivatives_claimed"] is True
         and sj["old_numerical_enclosures_recomputed"] == 0
         and sj["old_scientific_producer_imports"] == 0)
    doc["actual_progress"]["old_scientific_receipts_admitted"] += 1

    old["wx"] = original_science(paths, "wx", "wx_execution")
    wx = old["wx"]
    fl = wx["complete_shorter_flow_derivative_conclusion"]
    le = wx["complete_ungauged_leading_flow_conclusion"]
    gate(doc, 6, all(fl[k] is True for k in (
             "both_characteristic_branches_share_maximum_bound",
             "every_shorter_interval_and_both_orientations",
             "inverse_flow_has_its_own_same_directed_bounds",
             "no_arbitrary_operator_norm_inversion"))
         and le["all_shorter_subintervals_and_both_branches"] is True
         and le["exact_scalar_radial_rate"] == "ell0 = -2 beta mean(u^2+K*v^2)"
         and le["forward_orientation"] == "b>=a"
         and le["reverse_orientation"] == "b<=a"
         and wx["old_numerical_enclosures_recomputed"] == 0
         and wx["old_scientific_producer_calls"] == 0)
    doc["actual_progress"]["old_scientific_receipts_admitted"] += 1

    old["dza"] = original_science(paths, "dza", "dza_science")
    dz = old["dza"]
    gate(doc, 7, dz["complete_new_fourth_angle_conclusion"]
             ["complete_both_characteristic_branches_and_all_shorter_intervals"] is True
         and dz["complete_new_fourth_angle_conclusion"]
             ["saved_P1_P2_P3_and_M_F_G_W1_W2_h1_h2_are_not_recomputed"] is True
         and dz["old_successful_scientific_targets_recomputed"] == 0
         and dz["old_scientific_source_imports"] == 0)
    doc["actual_progress"]["old_scientific_receipts_admitted"] += 1

    fm = read_json(paths["fa_manifest"])
    ffiles = {e["role"]: e for e in fm["files"]}
    chain = {
        "old_fold_majorants_stage": HISTORICAL_INPUTS[0],
        "free_radius_stage": HISTORICAL_INPUTS[1],
        "adjacent_process": CURRENT_PIN_SPECS["adjacent_process"],
        "adjacent_publication": CURRENT_PIN_SPECS["adjacent_publication"],
        "whole_process": CURRENT_PIN_SPECS["whole_process"],
        "whole_publication": CURRENT_PIN_SPECS["whole_publication"],
        "original_fold_algorithm": CURRENT_PIN_SPECS["original_fold_algorithm"],
        "original_whole_algorithm": CURRENT_PIN_SPECS["original_whole_algorithm"],
    }
    gate(doc, 8, old["fa"]["input_manifest_sha256"] == CURRENT_PIN_SPECS["fa_manifest"]["sha256"]
         and fm["source_sha256"] == CURRENT_PIN_SPECS["original_fa_source"]["sha256"]
         and all(all(ffiles[k][field] == spec[field] for field in ("path", "bytes", "sha256"))
                 for k, spec in chain.items())
         and all(ffiles[k]["restore_commit"] == HISTORICAL_INPUTS[0]["commit"] for k in chain)
         and ffiles["whole_native"]["sha256"] == HISTORICAL_IDENTITIES["free_parent_native_sha256"]
         and ffiles["whole_native"]["bytes"] == HISTORICAL_IDENTITIES["free_parent_native_bytes"]
         and ffiles["original_whole_manifest"]["sha256"] == HISTORICAL_IDENTITIES["free_manifest"])
    accepted = {name: copy.deepcopy(OLD_IDENTITIES[name]) for name in ("fa", "sj", "wx", "dza")}
    for name in accepted:
        accepted[name].update(complete=True, proved=True, actual_returncode=0, failure=None)

    adjacent, apub = read_json(paths["adjacent_process"]), read_json(paths["adjacent_publication"])
    process_identity(adjacent, "adjacent")
    publication_entry(apub, "consumers/stages/complete-original-reference-holomorphic-majorants.json.gz",
                      HISTORICAL_INPUTS[0])
    gate(doc, 9, adjacent["complete"] is True and adjacent["failure"] is None
         and adjacent["actual_returncode"] == 0 and adjacent["mathematical_complete"] is True
         and adjacent["mathematical_proved"] is True and adjacent["mathematical_failure"] is None
         and adjacent["fixed_intrinsic_parameter"] == "eta_0"
         and adjacent["exact_real_delta_radius"] == PARAMETERS["exact_real_delta_radius"]
         and adjacent["exact_complex_coefficient_delta_radius"] == PARAMETERS["exact_real_delta_radius"]
         and apub["complete"] is True and apub["actual_returncode"] == 0
         and str(apub["run_id"]) == "43676926141")
    accepted["original_adjacent_mathematics"] = {
        **copy.deepcopy(OLD_PROCESS_IDENTITIES["adjacent"]),
        "complete": True, "actual_returncode": 0, "mathematical_complete": True,
        "mathematical_proved": True, "mathematical_failure": None,
        "publication_complete": True, "publication_actual_returncode": 0}

    whole, wpub = read_json(paths["whole_process"]), read_json(paths["whole_publication"])
    process_identity(whole, "whole")
    publication_entry(wpub, "consumers/stages/complete-radius-budget-9-1000000.json.gz",
                      HISTORICAL_INPUTS[1])
    wm = whole["scientific_metadata"]
    gate(doc, 10, whole["actual_returncode"] == 0 and whole["mathematical_complete"] is True
         and whole["mathematical_proved"] is True and whole["mathematical_failure"] is None
         and whole["complete"] is False
         and whole["failure"] == HISTORICAL_IDENTITIES["free_parent_formatter_failure"]
         and wpub["complete"] is False and wpub["actual_returncode"] == 1
         and str(wpub["run_id"]) == "43669106351"
         and wm["runtime"] == HISTORICAL_IDENTITIES["runtime"]
         and wm["fixed_intrinsic_parameter"] == "eta_0"
         and wm["exact_root_interval"] == PARAMETERS["exact_root_interval"]
         and wm["exact_complex_coefficient_delta_radius"] == PARAMETERS["exact_real_delta_radius"]
         and wm["original_Taylor_native_sha256"] == HISTORICAL_IDENTITIES["free_Taylor"]
         and wm["original_Nraw_native_sha256"] == HISTORICAL_IDENTITIES["free_Nraw"]
         and whole["original_successful_mathematics_recomputed"] == 0)
    accepted["original_whole_mathematics"] = {
        **copy.deepcopy(OLD_PROCESS_IDENTITIES["whole"]),
        "actual_returncode": 0, "mathematical_complete": True, "mathematical_proved": True,
        "mathematical_failure": None, "wrapper_complete": False,
        "formatter_failure": copy.deepcopy(whole["failure"]),
        "publication_complete": False, "publication_actual_returncode": 1,
        "full_original_process_sha256": CURRENT_PIN_SPECS["whole_process"]["sha256"],
        "full_original_publication_sha256": CURRENT_PIN_SPECS["whole_publication"]["sha256"]}

    foldstage = read_json(paths["fold_majorants_native"])
    fp = foldstage["payload"]
    majorants = {}
    for name in ("chi", "T", "G", "Q", "a0", "b0", "F0", "F1"):
        row = fp["majorants"][name]
        radius, width = (("1/6000", "1/128") if name in ("F0", "F1")
                         else ("3/8000", "3/128"))
        require(isinstance(row, list) and len(row) == 3
                and row[1:] == [radius, width], "full original majorant domain: " + name)
        majorants[name] = [original_record(row[0], "majorant." + name), row[1], row[2]]
    folded = {name: original_record(fp["fold"][name], "fold." + name)
              for name in ("E", "TM", "BT", "gap", "mu", "Am", "G", "Gi")}
    coefficients = copy.deepcopy(fp["coefficients"])
    require(isinstance(coefficients, dict), "complete local coefficient object")
    for name in ("U", "V"):
        require(isinstance(coefficients[name], list) and len(coefficients[name]) == 4
                and all(isinstance(row, list) and len(row) == 5 for row in coefficients[name]),
                "complete ordinary local mixed table: " + name)
    require(len(coefficients["D"]) == 6 and len(coefficients["Dr"]) == 3,
            "complete old local drift table")
    for name in ("km", "kp", "em", "ep", "am", "ap", "k1", "k2", "a1", "a2",
                 "beta", "beta_r", "K", "Kr", "T0", "V0", "vartheta",
                 "rQ", "ell", "b0", "eta_log_r", "log_EG_r", "log_EG_rr"):
        original_record(coefficients[name], "coefficients." + name)
    coefficient_count = all_original_balls(coefficients, "coefficients")
    fold_digest = sha(old_payload_bytes(fp))
    gate(doc, 11, foldstage["complete"] is True
         and foldstage["stage"] == foldstage["name"] == "complete-original-reference-holomorphic-majorants"
         and foldstage["source_sha256"] == HISTORICAL_IDENTITIES["fold_source"]
         and foldstage["algebra_sha256"] == HISTORICAL_IDENTITIES["fold_algebra"]
         and foldstage["input_manifest_sha256"] == HISTORICAL_IDENTITIES["fold_manifest"]
         and foldstage["runtime"] == HISTORICAL_IDENTITIES["runtime"]
         and fp["majorants"]["A"][1:] == ["3/8000", "3/128"]
         and fold_digest == HISTORICAL_IDENTITIES["fold_payload_sha256"]
             == old["fa"]["original_complete_fold_payload_sha256"]
         and coefficient_count >= 72)
    doc["actual_progress"]["old_mathematical_stage_products_read"] += 1
    doc["actual_progress"]["old_complete_local_coefficient_objects_copied"] = 1
    accepted["fold_stage"] = {key: copy.deepcopy(foldstage[key]) for key in (
        "complete", "stage", "source_sha256", "algebra_sha256", "input_manifest_sha256", "runtime")}
    accepted["fold_stage"].update(
        complete_payload_sha256=fold_digest,
        consumed_majorants=list(majorants), consumed_fold_fields=list(folded),
        complete_local_coefficients_copied_entirely=True,
        complete_local_coefficient_ball_count=coefficient_count)

    freestage = read_json(paths["free_radius_native"])
    rp = freestage["payload"]
    rows = [r for r in rp["budgets"] if r["exact_output_phi_width"] == "1/512"]
    require(len(rows) == 1, "one complete old saved-width free budget")
    row = rows[0]
    free = {name: {str(p): [
        original_record(row["first_amplitude_budgets"][name]["strip_sup"][str(p)+","+str(q)],
                        "free." + name + "." + str(p) + "." + str(q))
        for q in range(4)] for p in range(3)} for name in ("a1", "b1")}
    overlap = {name: {str(p): free[name][str(p)] for p in (0, 1)} for name in ("a1", "b1")}
    radius_digest = sha(old_payload_bytes(rp))
    gate(doc, 12, freestage["complete"] is True
         and freestage["stage"] == "complete-radius-budget-9-1000000"
         and freestage["stage_kind"] == "radius_budget_stages"
         and freestage["source_sha256"] == CURRENT_PIN_SPECS["original_whole_algorithm"]["sha256"]
         and freestage["input_manifest_sha256"] == HISTORICAL_IDENTITIES["free_manifest"]
         and freestage["runtime"] == HISTORICAL_IDENTITIES["runtime"]
         and freestage["original_Taylor_native_sha256"] == HISTORICAL_IDENTITIES["free_Taylor"]
         and freestage["original_Nraw_native_sha256"] == HISTORICAL_IDENTITIES["free_Nraw"]
         and rp["complete"] is True and rp["exact_physical_rho_cover"] == "9/1000000"
         and rp["exact_holomorphic_rho_radius"] == "1/6000"
         and rp["exact_holomorphic_phi_width"] == "1/128"
         and row["all_saved_finite_norms_and_complete_angular_factors_reused"] is True
         and row["old_first_correction_or_numerator_coefficients_recomputed"] is False
         and overlap == old["fa"]["complete_saved_free_amplitude_conclusion"]
             ["p0_and_p1_q0_through_q3_read_verbatim"]
         and radius_digest == HISTORICAL_IDENTITIES["free_payload_sha256"]
             == old["fa"]["complete_saved_free_amplitude_conclusion"]["radius_payload_sha256"]
         and old["fa"]["complete_saved_free_amplitude_conclusion"]["radius_stage_sha256"]
             == HISTORICAL_INPUTS[1]["sha256"])
    doc["actual_progress"]["old_mathematical_stage_products_read"] += 1
    accepted["free_stage"] = {key: copy.deepcopy(freestage[key]) for key in (
        "complete", "stage", "stage_kind", "source_sha256", "input_manifest_sha256",
        "runtime", "original_Taylor_native_sha256", "original_Nraw_native_sha256")}
    accepted["free_stage"].update(
        complete_payload_sha256=radius_digest, exact_physical_rho_cover="9/1000000",
        exact_holomorphic_rho_radius="1/6000", exact_holomorphic_phi_width="1/128",
        exact_output_phi_width="1/512", original_free_and_genuine_amplitudes_distinct=True,
        all_24_original_component_records_read=True, all_16_original_FA_overlap_records_equal=True)
    stage_records = {"majorants": majorants, "fold": folded, "free_components": free}

    records = {name: original_record(get_path(old[spec["role"]], spec["path"]), name)
               for name, spec in SCALAR_PATHS.items()}
    scopes = {name: copy.deepcopy(get_path(old[spec["role"]], spec["path"]))
              for name, spec in SCOPE_PATHS.items()}
    for name, spec in SCALAR_PATHS.items():
        if spec["direction"] == "lower":
            require(record_is_finite(records[name], True), "old full positive lower: " + name)
    rootlo, rootup = map(Fraction, PARAMETERS["exact_root_interval"])
    cut = Fraction(PARAMETERS["exact_strict_cut"])
    gate(doc, 13, len(records) == 66 and len(scopes) == 9
         and all_original_balls(stage_records) == 40
         and sha(canonical(records)) == FROZEN_OLD_COPY_HASHES["scalar_records"]
         and sha(canonical(scopes)) == FROZEN_OLD_COPY_HASHES["complete_scopes"]
         and all(old[name][OLD_IDENTITIES[name]["parameter_key"]]["exact_real_delta_radius"]
                 == PARAMETERS["exact_real_delta_radius"] for name in old)
         and all(old[name][OLD_IDENTITIES[name]["parameter_key"]]["exact_root_interval"]
                 == PARAMETERS["exact_root_interval"] for name in old)
         and all(old[name][OLD_IDENTITIES[name]["parameter_key"]]["exact_strict_cut"]
                 == PARAMETERS["exact_strict_cut"] for name in old)
         and all(old[name][OLD_IDENTITIES[name]["parameter_key"]]["fixed_intrinsic_parameter"]
                 == "eta_0" for name in old)
         and 0 < rootlo-cut < rootup-cut < Fraction("9/1000000") < Fraction("1/6000"))
    doc["actual_progress"]["old_current_scalar_records_copied"] = 66
    doc["actual_progress"]["old_historical_scalar_records_copied"] = 40
    doc["actual_progress"]["old_scope_objects_copied"] = 9
    accepted["original_FA_manifest_sha256"] = CURRENT_PIN_SPECS["fa_manifest"]["sha256"]
    accepted["all_complete_original_inputs_identified"] = True
    doc["accepted_original_inputs"] = accepted
    packet = {key: None for key in ORIGINAL_INPUT_FIELDS}
    packet.update(kind=ORIGINAL_INPUT_KIND, complete=True,
        public_repository=PUBLIC, run_id=doc["run_id"], run_attempt=doc["run_attempt"],
        workflow_event_commit=doc["workflow_event_commit"],
        actual_scientific_checkout_commit=doc["actual_scientific_checkout_commit"],
        source_sha256=doc["source_sha256"], math_module_sha256=doc["math_module_sha256"],
        input_manifest_sha256=doc["input_manifest_sha256"],
        original_input_sha256=copy.deepcopy(doc["input_sha256"]),
        copied_original_scalar_records=records,
        copied_original_scalar_records_sha256=sha(canonical(records)),
        copied_complete_original_scopes=scopes,
        copied_complete_original_scopes_sha256=sha(canonical(scopes)),
        copied_original_stage_records=stage_records,
        copied_original_stage_records_sha256=sha(canonical(stage_records)),
        copied_complete_local_coefficients=coefficients,
        copied_complete_local_coefficients_sha256=sha(canonical(coefficients)),
        local_coefficient_qualification=copy.deepcopy(LOCAL_COEFFICIENT_QUALIFICATION),
        copy_counts={"current_scalar_records": 66, "stage_scalar_records": 40,
                     "complete_scope_objects": 9, "complete_local_coefficient_objects": 1,
                     "local_coefficient_ball_count": coefficient_count},
        complete_readonly_input_projection=True)
    require(set(packet) == set(ORIGINAL_INPUT_FIELDS) and len(packet) == 22,
            "complete original input-copy schema")
    return packet

def verified_new_module(paths):
    path = paths["math_module"]
    require(sha(path.read_bytes()) == CURRENT_PIN_SPECS["math_module"]["sha256"],
            "new mathematical module changed before import")
    spec = importlib.util.spec_from_file_location("reviewed_wgs_new_math", path)
    require(spec is not None and spec.loader is not None, "new mathematical module loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def working_inputs(packet, math):
    records = packet["copied_original_scalar_records"]
    def u(name):
        return math.read_up(records[name])
    def l(name):
        return math.read_lower(records[name], "saved " + name)
    s = {"Qmixed": [[u("Q_"+str(a)+"_"+str(b)) for b in range(4)] for a in range(3)],
         "beta": [u("beta_"+str(a)) for a in range(4)],
         "gamma": [u("gamma_"+str(a)) for a in range(4)],
         "K": [u("K_"+str(a)) for a in range(4)],
         "q": [u("q_"+str(a)) for a in range(4)],
         "eta_lower": l("eta_lower"), "q_lower": l("q_lower"), "q_upper": u("q_upper"),
         "t_cut_lower": l("t_cut_lower"), "t_cut_upper": u("t_cut_upper"),
         "xdev_cut": u("xdev_cut"), "y_cut": u("y_cut"),
         "q_cut_lower": l("q_cut_lower"), "q_cut_upper": u("q_cut_upper"),
         "flow": {k: u("flow_"+str(k)) for k in range(1, 5)},
         "flow_lower": l("flow_lower"),
         "cut_phase": {k: u("cut_phase_"+str(k)) for k in range(1, 5)},
         "cut_t_derivatives": {k: u("cut_t_"+str(k)) for k in range(1, 5)},
         "leading_forward": u("leading_forward"), "leading_reverse": u("leading_reverse"),
         "old_FA_free_jets": {p: [u("free_old_"+str(p)+"_"+str(q)) for q in range(7)]
                             for p in (0, 1)}}
    for name, value in (("rc", PARAMETERS["exact_strict_cut"]),
                        ("root_upper", PARAMETERS["exact_root_interval"][1]),
                        ("RG", PARAMETERS["exact_fold_radius"]),
                        ("SG", PARAMETERS["exact_fold_strip"]),
                        ("saved_h", PARAMETERS["exact_saved_free_radius"]),
                        ("saved_strip", PARAMETERS["exact_saved_free_width"])):
        s[name] = math.ex(Fraction(value))
    saved = packet["copied_original_stage_records"]
    s["fold_Am"] = math.read_lower(saved["fold"]["Am"], "original local fold Am")
    s["fold_G"] = math.read_up(saved["fold"]["G"])
    s["fold_Gi"] = math.read_up(saved["fold"]["Gi"])
    old = {"majorants": {name: (math.read_up(row[0]), math.ex(Fraction(row[1])),
                               math.ex(Fraction(row[2])))
                        for name, row in saved["majorants"].items()},
           "fold": {name: (math.read_lower(row, "old fold " + name)
                           if name in ("gap", "mu", "Am") else math.read_up(row))
                    for name, row in saved["fold"].items()},
           "free_component": {name: {int(p): [math.read_up(v) for v in row]
                                     for p, row in entries.items()}
                              for name, entries in saved["free_components"].items()}}
    return s, old

def store_new_stage(args, doc, graph_name, graph, progress_name, gate_index):
    doc[graph_name] = graph
    doc["actual_progress"][progress_name] = 1
    # Returned complete graphs remain in the document even if their subsequent
    # structural check fails; the exception handler persists the entire result.
    gate(doc, gate_index, complete_graph_shape(graph, NEW_GRAPH_SHAPES[graph_name], graph_name)
         and scalar_slot_count(NEW_GRAPH_SHAPES[graph_name]) == NEW_GRAPH_SLOT_COUNTS[graph_name])
    doc["actual_progress"]["new_scalar_slots_saved"] += NEW_GRAPH_SLOT_COUNTS[graph_name]
    persist(args.out, doc)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--bits", type=int, default=320)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    copies_path = args.out.parent / ORIGINAL_INPUT_FILENAME
    if args.out.exists() or copies_path.exists():
        raise FileExistsError("preserve every complete or partial science and original-input copy")
    ctx.prec = args.bits
    doc = {key: None for key in COMPLETE_FIELDS}
    doc.update(kind=KIND, complete=False, proved=False, actual_returncode=None, failure=None,
        stage="initial_original_input_admission", source_sha256=sha(Path(__file__).read_bytes()),
        math_module_sha256=CURRENT_PIN_SPECS["math_module"]["sha256"],
        input_manifest_sha256=sha(args.manifest.read_bytes()), public_repository=PUBLIC,
        run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        runtime={}, arithmetic_bits=args.bits, parameters=copy.deepcopy(PARAMETERS),
        retained_scope=copy.deepcopy(RETAINED_SCOPE), planned_shape=copy.deepcopy(PLANNED_SHAPE),
        actual_progress=copy.deepcopy(INITIAL_ACTUAL_PROGRESS), gates=[],
        actual_mathematical_wall_seconds=0, input_sha256={}, verified_original_inputs={},
        original_source_AST_evidence={}, accepted_original_inputs={},
        complete_original_inputs_file=None)
    began = time.monotonic()
    try:
        manifest, paths = checked_inputs(args, doc)
        packet = accepted_original_inputs(paths, doc)
        copies_raw = persist(copies_path, packet)
        print_complete_document(packet, original_inputs=True)
        doc["complete_original_inputs_file"] = {
            "filename": ORIGINAL_INPUT_FILENAME, "bytes": len(copies_raw), "sha256": sha(copies_raw)}
        doc["stage"] = "complete_original_input_admission"
        persist(args.out, doc)
        # This is a complete read-only admission-format gate before any new
        # mathematical graph. Even an oversized original copy is already saved.
        require(len(copies_raw) <= PUBLICATION_LIMITS["complete_original_inputs_max_bytes"],
                "complete original inputs saved; predeclared input-copy byte limit exceeded")
        math = verified_new_module(paths)
        certificate = json.loads(canonical(math.derivative_certificate()), parse_constant=reject_nonfinite)
        doc["complete_derivative_request_certificate"] = certificate
        doc["actual_progress"]["new_derivative_certificates"] = 1
        gate(doc, 14, certificate == DERIVATIVE_CERTIFICATE
             and all(scalar_slot_count(shape) == NEW_GRAPH_SLOT_COUNTS[name]
                     for name, shape in NEW_GRAPH_SHAPES.items())
             and sum(NEW_GRAPH_SLOT_COUNTS.values()) == 437)
        persist(args.out, doc)
        s, original = working_inputs(packet, math)

        doc["stage"] = "complete_new_strict_coefficient_graph"
        coefficients, graph = math.complete_strict_coefficients(s)
        store_new_stage(args, doc, "complete_strict_coefficient_conclusion", graph,
                        "new_strict_coefficient_graphs", 15)

        doc["stage"] = "complete_new_higher_flow_and_cut_graph"
        flow, graph = math.complete_higher_flow_and_cut(s, coefficients)
        store_new_stage(args, doc, "complete_higher_flow_and_cut_conclusion", graph,
                        "new_higher_flow_graphs", 16)

        doc["stage"] = "complete_new_strict_geometry_graph"
        geometry, graph = math.complete_strict_geometry(s, coefficients, flow)
        store_new_stage(args, doc, "complete_strict_geometry_conclusion", graph,
                        "new_strict_geometry_graphs", 17)

        doc["stage"] = "complete_new_strict_leading_graph"
        leading, graph = math.complete_strict_leading(s, coefficients, flow, geometry)
        store_new_stage(args, doc, "complete_strict_leading_conclusion", graph,
                        "new_strict_leading_graphs", 18)

        doc["stage"] = "complete_new_strict_forcing_graph"
        forcing, graph = math.complete_strict_forcing(s, coefficients, geometry, leading)
        store_new_stage(args, doc, "complete_strict_forcing_conclusion", graph,
                        "new_strict_forcing_graphs", 19)

        doc["stage"] = "complete_new_local_regular_graph"
        local, graph = math.complete_local_regular_packet(s, original)
        store_new_stage(args, doc, "complete_local_regular_packet_conclusion", graph,
                        "new_local_regular_graphs", 20)

        doc["stage"] = "complete_new_free_first_transport_graph"
        transport, graph = math.complete_free_first_transport(
            s, coefficients, flow, geometry, leading, forcing, local)
        store_new_stage(args, doc, "complete_free_first_transport_conclusion", graph,
                        "new_free_transport_graphs", 21)

        doc["stage"] = "complete_new_global_closure_and_readonly_audit"
        closure = math.complete_global_packet_conclusion(geometry, leading, forcing, local, transport)
        doc["complete_named_global_graph_conclusion"] = closure
        doc["actual_progress"]["new_global_graph_conclusions"] = 1
        gate(doc, 22, complete_graph_shape(closure, NEW_GRAPH_SHAPES["complete_named_global_graph_conclusion"])
             and all(sha(paths[role].read_bytes()) == spec["sha256"]
                     for role, spec in mathematical_pin_specs().items())
             and all(sha(paths[e["role"]].read_bytes()) == e["sha256"] for e in manifest["files"])
             and sha(args.manifest.read_bytes()) == doc["input_manifest_sha256"] == args.manifest_sha
             and copies_path.read_bytes() == canonical(packet)
             and sha(copies_path.read_bytes()) == doc["complete_original_inputs_file"]["sha256"]
             and len(copies_path.read_bytes()) == doc["complete_original_inputs_file"]["bytes"]
             and packet["copied_original_scalar_records_sha256"]
                 == FROZEN_OLD_COPY_HASHES["scalar_records"]
             and packet["copied_complete_original_scopes_sha256"]
                 == FROZEN_OLD_COPY_HASHES["complete_scopes"])
        persist(args.out, doc)

        doc["actual_mathematical_wall_seconds"] = time.monotonic() - began
        gate(doc, 23, set(doc) == set(COMPLETE_FIELDS) and len(doc) == 36
             and set(packet) == set(ORIGINAL_INPUT_FIELDS) and len(packet) == 22
             and doc["actual_progress"] == SUCCESS_ACTUAL_PROGRESS
             and doc["retained_scope"] == RETAINED_SCOPE and doc["parameters"] == PARAMETERS
             and doc["planned_shape"] == PLANNED_SHAPE
             and doc["complete_derivative_request_certificate"] == DERIVATIVE_CERTIFICATE
             and all(complete_graph_shape(doc[name], shape, name)
                     for name, shape in NEW_GRAPH_SHAPES.items())
             and len(doc["gates"]) == 23
             and [g["name"] for g in doc["gates"]] == GATE_NAMES[:23]
             and all(g["passed"] is True for g in doc["gates"]))
        doc.update(complete=True, proved=True, actual_returncode=0, failure=None, stage="complete")
    except BaseException as error:
        doc.update(complete=False, proved=False, actual_returncode=1,
                   failure=operation_failure(error),
                   actual_mathematical_wall_seconds=time.monotonic() - began)
        doc["failed_new_stage_diagnostic"] = {
            "stage": doc["stage"],
            "complete_original_input_file_saved": doc["complete_original_inputs_file"] is not None,
            "returned_complete_new_graph_fields": [
                name for name in NEW_GRAPH_SHAPES if isinstance(doc.get(name), dict)],
            "all_original_scientific_targets_remain_frozen": True,
            "new_global_jet_or_received_operator_conclusions_authorized": False}
        persist(args.out, doc)
        print_complete_document(doc)
        raise
    raw = persist(args.out, doc)
    print_complete_document(doc)
    if len(raw) > PUBLICATION_LIMITS["complete_science_max_bytes"]:
        raise ValueError("complete main science saved and printed; publication byte budget exceeded")

if __name__ == "__main__":
    main()
