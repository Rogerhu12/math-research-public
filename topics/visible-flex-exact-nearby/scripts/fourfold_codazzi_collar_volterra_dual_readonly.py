"""W2C complete pure readonly admission and immutable WVC/collar bindings.

No flint import, scientific call, operator assembly, or original producer import.
The seven new modules and every old definition are parsed as AST only. The two
native gzip objects are read in own public Actions after complete compressed
byte/SHA256/Git checks; this module has not been run while being prepared.

The original nineteen-object restoration remains its whole immutable object.
Two additional original natives form a separate complete extension, giving
exactly twenty-one restored objects without changing an old status or scope.
"""
from __future__ import annotations
import ast, gzip, hashlib, json, os, sys
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
REPOSITORY = "Rogerhu12/math-research-public"
MANIFEST_KIND = "complete_collar_Volterra_dual_current_inputs_v1"
PROBLEM_ID = "W2C_complete_collar_Volterra_dual_candidate_v1"
NEW_MODULE_ROLES = (
 "science", "readonly_admission", "readonly_core", "collar_math",
 "kernel_math", "assembly_math", "reference_math",
)
ORIGINAL_DEFINITION_ROLES = (
 "negative_one_source", "collar_source", "body_source",
 "complete_coefficient_definition", "continuous_repair_definition",
 "repaired_value_inflation_definition", "lossless_shard_format",
 "completed_reference_definition", "WIC_module", "WQS_module",
 "moving_germ_definition", "root_scalarization_definition",
 "complex_germ_record_definition", "metric_record_definition",
 "beta_record_definition",
)
ORIGINAL_RESTORATION_IDENTITY = {
 "bytes": 13771,
 "sha256": "4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac",
}
COLLAR_CHECKS = (
 "complete_WVC_43_scientific_and_44_execution_fields_and_false_gate_verified",
 "all_twenty_nine_same_operator_original_records_verified",
 "original_nineteen_restoration_object_unchanged_and_two_native_extension_verified",
 "all_signed_germ_fields_and_complex_record5_shapes_verified",
 "complete_root_budget_193_upper_records_and_four_full_angular_arrays_verified",
 "exact_signed_65_offsets_and_piece2549_full_complex_domain_verified",
 "same_actual_full_family_eta_and_independent_mean_rows_retained",
)

COMPLETED_TRACE_PINS=json.loads(r'''{"WVC_actual":{"bytes":78627,"git_blob_sha":"746ec1e16befe8914c64521ad087c1f1dd23ab73","path":"topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json","role":"WVC_actual","sha256":"85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"},"WVC_execution":{"bytes":37911,"git_blob_sha":"c8cd8e8bb863c500a1e26c009e0af76cd7cb8941","path":"topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/execution.json","role":"WVC_execution","sha256":"5e560887d2deee497cb9da5b7549af1070db36cf69a7b11077ef4a0bb4f0feb5"},"WVC_manifest":{"bytes":60844,"git_blob_sha":"1ea008a1df3116aedd66be67b11b1d8ec62af2d5","path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-continuous-centre-tracefree-current-inputs.json","role":"WVC_manifest","sha256":"229198f56efdf10ea8de6fef50804aa3832ca5ff2127101685c8d7117c9afbfb"}}''')
COMPLETED_TRACE_FIELD_IDENTITIES=json.loads(r'''{"actual_checkout_commit":{"bytes":43,"sha256":"b10480100811bf79025806b82ec7c30723383103e65351c958ab461d02cff1d2"},"actual_mathematical_wall_seconds":{"bytes":14,"sha256":"f1152bf01b295572174295506e483164ad638f6cf496de5f4b8984dd9b8c9ba6"},"actual_progress":{"bytes":819,"sha256":"025ee97a08c80ef85d07d2aac09394f19a7696f0a0f4ed8203b1e0cf6cefb275"},"actual_returncode":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"automatic_retry_authorized":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"complete":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"complete_current_file_receipts":{"bytes":12199,"sha256":"45e8cd94d6b806042732fc206994e293309cb6a007651bbf408e742802b21629"},"complete_new_graphs":{"bytes":8637,"sha256":"0882b563cdd2e425d5d1e383bd158ce5bce7fb1604903df2bb1a0756b5f4ea42"},"complete_restoration_receipts":{"bytes":13771,"sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"},"complete_support_contract":{"bytes":520,"sha256":"622693074042afeceb02fb81efb373aeb8d33c01003332ba16d5b0f6eb349067"},"completed_targets":{"bytes":186,"sha256":"709c5e57181e94d5048670fcfbb1536f661ca7d0bef058e8ccbc1951751e8a7b"},"conditional_finite_inverse":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"copied_complete_candidate_metadata":{"bytes":2581,"sha256":"aa864b2f189497b01dff719f3c16634620fc2f75d22236f81c42236f12abb356"},"copied_complete_repair_definition":{"bytes":792,"sha256":"440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"},"copied_original_records":{"bytes":2627,"sha256":"b313df918a9ec86507695b49ba8eb5c5a75afbe268faeffdb14ece854f1f2e71"},"copied_original_scope":{"bytes":8502,"sha256":"94c595173f4591660211251da7f67ea47e15fd52749167379f5ff4c50909736b"},"current_target":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"finite_gate":{"bytes":341,"sha256":"3eb7880c2ebf4f282f5101c1246b51bca718bca0bcffa2ba5198364bd4ace819"},"gates":{"bytes":1808,"sha256":"e475a0f9db43ad510a8b72672576747bcefc432ea7e259e02fbb69254e648f69"},"input_sha256":{"bytes":3454,"sha256":"b49b74104fea8c7bcc5de012882a7be2b8bad72859e8bbdb77ed71df7a9ced7d"},"kind":{"bytes":52,"sha256":"f31b30439d2aa9a11b6625590546ad4538dfd23b0c130620580e6d4e34e2c6ad"},"manifest_sha256":{"bytes":67,"sha256":"c51318a1afe26802f6771f4ddca7b08672f777b929a10de307e796bfebd3a55f"},"original_admission":{"bytes":1719,"sha256":"b8156edca3e6674cb50762b23a13c0333850c29cf6e35b236563850777c7fe6b"},"parameters":{"bytes":950,"sha256":"a500b703beee4032f6f6d6f47988f39146b691d2d34848f166443f38a60f9526"},"preparation_prefix":{"bytes":323,"sha256":"ae009c73b02625046b47309b2e7e39487f2169ab062b72ca302052713d21028e"},"prior_completed_candidate":{"bytes":8977,"sha256":"2e70e03efe8d2275f5365fff52b5a964c912594edd6a156145affafe7146799e"},"problem_id":{"bytes":56,"sha256":"f213b05cb84dcf89ea55e8ccb1e7520713271bac5fae059a6682e1538b1c5c42"},"proved":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"reference_chain":{"bytes":90,"sha256":"17a03aa6671788c510cb926fe507c7686bd0e7610c49dd1e1cf5fd2cb8b684ca"},"reference_mode_prefix":{"bytes":988,"sha256":"842157bf20b74c7df36a3f4c96ca9491e371c12fd2f72d9c4daa3fa6cf597d7b"},"reference_selection":{"bytes":507,"sha256":"6dab06a990a60129c0ebf5a442f935851050dedb6ce7b6655076be29bd9cd7d9"},"retained_completed_five_maxima":{"bytes":2350,"sha256":"407ca196cf8f60ac7c037cd2c2056673e139ecd4c1ecc4343d78a5cbf99a6f74"},"retained_original_false_candidates":{"bytes":1082,"sha256":"af586adb9e63165b204717ac8ace80c2d05285940573a1f7bdc39599b89ae187"},"retained_scope":{"bytes":2282,"sha256":"fcefcfc2e136079f5098c3f324230b5e4ab058798e950c2c6a91a878046d7267"},"run_attempt":{"bytes":4,"sha256":"ee0ce7db9ce2f1d4d2e01f0e96d73fa2399a99d825d8a9898947539a8d8e1742"},"run_id":{"bytes":14,"sha256":"3cc684ee3338fc5f912febed8d3bf18660de96381167897a067c218cf88448ea"},"runtime":{"bytes":101,"sha256":"55c8f0053c75775912f034ed7a12221ac01f5f5439a1e0dc2ad5f6d2aa1e5734"},"saved_copy_counts":{"bytes":198,"sha256":"9e3ccb782b4021c94e0980c37b6255241c4f37dbc89969bf3156f50390e12285"},"saved_record_counts":{"bytes":200,"sha256":"c506a78e9ca9d4a5a32b4ce75adca8332ff1fb533a43d216aaec267bcd5cecd3"},"scientific_modules":{"bytes":1386,"sha256":"c010c61e6964a0803301f9b593a59dfebb50e3c62cc6e871f3e4e5b2acc20e3f"},"stage":{"bytes":11,"sha256":"b4a80c61a1f8c6101403f9f26edc545babd033d6ea52f4cc918a4d8a75d394a4"},"workflow_event_commit":{"bytes":43,"sha256":"68c4ea36f7468efadb57332e1e3b8859a138662f5356d96c05871482dafc81da"}}''')
COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES=json.loads(r'''{"AST_receipts":{"bytes":3327,"sha256":"8f63179ac52dd50ae5139e4119f62c355cf9c88733f9957408687b7d9d1cbaf6"},"actual_child_returncode":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"actual_scientific_checkout":{"bytes":43,"sha256":"b10480100811bf79025806b82ec7c30723383103e65351c958ab461d02cff1d2"},"all_pulls_match_review":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"child_timeout":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"child_wall_seconds":{"bytes":14,"sha256":"fc0ca09e688812a34087416225daea2098cdf785ff3336e5cf835c2517164963"},"complete_child_stdout":{"bytes":130,"sha256":"7d00951973682a240b57b0e00c1f0413b3ef856a509bf43223f19e5be2468620"},"completed_old_targets_recomputed":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"completed_target_names":{"bytes":186,"sha256":"709c5e57181e94d5048670fcfbb1536f661ca7d0bef058e8ccbc1951751e8a7b"},"consumed_marker_publication":{"bytes":389,"sha256":"bbb233e08179ef7e8754162555ccb63840d9009cf71d20e25bd357777cf70b4f"},"current_input_receipts":{"bytes":12199,"sha256":"45e8cd94d6b806042732fc206994e293309cb6a007651bbf408e742802b21629"},"entry_checkout":{"bytes":43,"sha256":"68c4ea36f7468efadb57332e1e3b8859a138662f5356d96c05871482dafc81da"},"failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"final_capacity_metadata":{"bytes":266,"sha256":"562eeeb9f17b29882cc06c6448938691eafce34dd1032e7c093d7f0291aef640"},"finished_utc":{"bytes":35,"sha256":"fd33869e4d27dcaba3f5081671f15f6bb222e072e1a3e13632ef87ae6871b03a"},"historical_restoration":{"bytes":13771,"sha256":"4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac"},"immediate_pre_science_capacity":{"bytes":266,"sha256":"eaea25065b1bffa998ca77c57cf8e429d083d520d6f5f2aabdadd96df6060c11"},"interrupted_target":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"kind":{"bytes":46,"sha256":"b6d2d89953b4df3f0d089085fa8c5596cafd388f5737725a7c9cd1e10e847ac9"},"manifest_sha256":{"bytes":67,"sha256":"c51318a1afe26802f6771f4ddca7b08672f777b929a10de307e796bfebd3a55f"},"new_Releases":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"new_arrays_published":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"new_artifacts":{"bytes":2,"sha256":"9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa"},"original_scientific_complete_flag":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"original_scientific_failure":{"bytes":5,"sha256":"38e0b9de817f645c4bec37c0d4a3e58baecccb040f5718dc069a72c7385a0bed"},"pre_execution_capacity":{"bytes":266,"sha256":"ea2e87e8bc362b1e275b22af68d828c6f0a510dfbffea824ac74da891da9e026"},"problem_id":{"bytes":56,"sha256":"f213b05cb84dcf89ea55e8ccb1e7520713271bac5fae059a6682e1538b1c5c42"},"publication_attempts":{"bytes":2,"sha256":"4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"},"readme_check_count":{"bytes":2,"sha256":"7de1555df0c2700329e815b93b32c571c3ea54dc967b89e81ab73b9972b72d1d"},"readme_checks":{"bytes":2374,"sha256":"bd358f2413f99f482ce446ab238e1fcfcf2d48049019dca42f35c21e244caef4"},"readme_receipt_chain_sha256":{"bytes":67,"sha256":"4b7b71cf276d9959c65ead53e005b42e06277e3d9879cf55c2787b26d357d356"},"readonly_diagnostic_only":{"bytes":6,"sha256":"2ed27c1421e6928dbe13dbfdb5c59e1045b30341fe7ebe05700006bc5ac572c0"},"readonly_preflight":{"bytes":2920,"sha256":"c4c510b60c387cba344434bbc36e4a6fd445387e5c347cd945d0c60825611e01"},"repository":{"bytes":33,"sha256":"ea69415f4036ec17f5e16041068cd74ddb1cc3e19aa80963210e2a69ac8da719"},"run_attempt":{"bytes":4,"sha256":"ee0ce7db9ce2f1d4d2e01f0e96d73fa2399a99d825d8a9898947539a8d8e1742"},"run_id":{"bytes":14,"sha256":"3cc684ee3338fc5f912febed8d3bf18660de96381167897a067c218cf88448ea"},"scientific_children":{"bytes":2,"sha256":"4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"},"scientific_complete":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"scientific_files":{"bytes":234,"sha256":"46592265f48c1e55dbe26d04ceaf91979875661a4977d171b0b8592ef2c5d5f7"},"scientific_finished_utc":{"bytes":35,"sha256":"9c87f758cf64191fc7628b57f5612e6aab9b5cc72e4979501b66ff86dcebdc17"},"scientific_started":{"bytes":5,"sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},"scientific_started_utc":{"bytes":35,"sha256":"721737d4ae0efb00455daa9724db2b313f3013c475024cdf514ff619248d1d1a"},"started_utc":{"bytes":35,"sha256":"da9dec5df6a9a9f84c518ed91ad7f339d3f0d365b30a0ce1bdf3c342ca22b2c5"},"workflow_event_commit":{"bytes":43,"sha256":"68c4ea36f7468efadb57332e1e3b8859a138662f5356d96c05871482dafc81da"}}''')
COMPLETED_TRACE_GATES=json.loads(r'''["all_current_UTF8_files_and_three_fixed_contracts_verified","five_new_and_ten_original_definition_sources_AST_only_verified","all_nineteen_historical_receipts_and_original_native_bytes_verified","complete_original_summary_and_native_projection_identical","both_complete_4650_row_covers_and_3594_interfaces_verified","same_real_family_and_all_original_successes_verified","all_nine_original_literals_and_completed_WHVA_retained","all_five_original_cubic_parts_and_full_shape_verified","original_repair_whole_document_and_all_65_suprema_verified","actual_raw_identity_transmissions_and_full_affine_ports_retained","all_sixty_old_WPS_records_full_false_scope_and_six_prefix_records_verified","fixed_directed_runtime_and_one_new_entry","all_twenty_six_old_records_typed_and_published_tail_bound_retained","entire_frozen_reference_definition_chain_materialized_without_old_bounds","complete_continuous_parent_and_comparison_domains_admitted","complete_reference_receivers_saved","complete_high_trial_source_saved","complete_actual_paired_receivers_saved","complete_local_signed_remainder_saved","complete_endpoint_correction_saved","complete_actual_E_D_T_saved","all_current_inputs_and_manifest_reverified_after_new_work","complete_whole_candidate_shape_and_old_zero_recomputation"]''')
COMPLETED_TRACE_GRAPH_KEYS=json.loads(r'''{"complete_actual_E_D_T":["complete_actual_D_upper","complete_actual_E0_upper","complete_actual_T_upper","complete_actual_finite_defect_upper"],"complete_actual_paired_receivers":["complete_actual_paired_LH_upper","complete_actual_tail_LH_upper","complete_centre_paired_LH_column_upper","complete_centre_paired_LH_norm_upper","complete_centre_paired_LH_row_upper","complete_centre_tail_LH_column_upper","complete_centre_tail_LH_norm_upper","complete_centre_tail_LH_row_upper","complete_difference_paired_LH_column_upper","complete_difference_paired_LH_norm_upper","complete_difference_paired_LH_row_upper","complete_difference_tail_LH_upper","complete_head_paired_error_upper","complete_low_generator_difference_column_upper","complete_low_generator_difference_norm_upper","complete_low_generator_difference_row_upper","complete_low_generator_tail_error_upper","complete_outer_paired_error_upper","complete_raw_difference_LH_receiver_column_upper","complete_raw_difference_LH_receiver_norm_upper","complete_raw_difference_LH_receiver_row_upper","complete_raw_difference_tail_LH_upper"],"complete_endpoint_correction":["complete_head_endpoint_correction_upper","complete_high_trace_endpoint_receiver_upper","complete_outer_endpoint_correction_upper"],"complete_high_trial_source":["complete_body_ordinary_source_upper","complete_family_high_kernel_column_upper","complete_family_high_kernel_norm_upper","complete_family_high_kernel_row_upper","complete_high_outer_trace_error_upper","complete_high_state_error_upper","complete_repaired_centre_body_residual_column_upper","complete_repaired_centre_body_residual_norm_upper","complete_repaired_centre_body_residual_row_upper","complete_trial_raw_column_upper","complete_trial_raw_norm_upper","complete_trial_raw_row_upper"],"complete_local_signed_remainder":["complete_actual_head_tail_source_upper","complete_actual_outer_tail_source_upper","complete_signed_centre_paired_source_column_upper","complete_signed_centre_paired_source_norm_upper","complete_signed_centre_paired_source_row_upper","complete_signed_centre_tail_source_column_upper","complete_signed_centre_tail_source_norm_upper","complete_signed_centre_tail_source_row_upper"],"complete_reference_receivers":["complete_reference_column_ratio_upper","complete_reference_inverse_norm_upper","complete_reference_odd_endpoint_receiver_upper","complete_reference_rho_column_ratio_upper","complete_reference_rho_defect_upper","complete_reference_rho_row_ratio_upper","complete_reference_row_ratio_upper"]}''')
COMPLETED_TRACE_COPY_PATHS=json.loads(r'''{"A_c":["copied_original_records","A_c"],"C_b":["copied_original_records","C_b"],"C_c":["copied_original_records","C_c"],"E_minus":["copied_original_records","E_minus"],"G_c":["copied_original_records","G_c"],"L_c_raw":["copied_original_records","L_c_raw"],"P_b_raw":["copied_original_records","P_b_raw"],"Y_b":["copied_original_records","Y_b"],"Y_b_outer":["copied_original_records","Y_b_outer"],"Y_c":["copied_original_records","Y_c"],"complete_actual_T_upper":["complete_new_graphs","complete_actual_E_D_T","new_records","complete_actual_T_upper"],"complete_actual_head_tail_source_upper":["complete_new_graphs","complete_local_signed_remainder","new_records","complete_actual_head_tail_source_upper"],"complete_actual_outer_tail_source_upper":["complete_new_graphs","complete_local_signed_remainder","new_records","complete_actual_outer_tail_source_upper"],"complete_head_endpoint_correction_upper":["complete_new_graphs","complete_endpoint_correction","new_records","complete_head_endpoint_correction_upper"],"complete_high_trace_endpoint_receiver_upper":["complete_new_graphs","complete_endpoint_correction","new_records","complete_high_trace_endpoint_receiver_upper"],"complete_outer_endpoint_correction_upper":["complete_new_graphs","complete_endpoint_correction","new_records","complete_outer_endpoint_correction_upper"],"complete_outer_paired_error_upper":["complete_new_graphs","complete_actual_paired_receivers","new_records","complete_outer_paired_error_upper"],"complete_reference_column_ratio_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_column_ratio_upper"],"complete_reference_inverse_norm_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_inverse_norm_upper"],"complete_reference_odd_endpoint_receiver_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_odd_endpoint_receiver_upper"],"complete_reference_rho_column_ratio_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_rho_column_ratio_upper"],"complete_reference_rho_defect_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_rho_defect_upper"],"complete_reference_rho_row_ratio_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_rho_row_ratio_upper"],"complete_reference_row_ratio_upper":["complete_new_graphs","complete_reference_receivers","new_records","complete_reference_row_ratio_upper"],"lambda_388_minus_two_thirds":["copied_original_records","lambda_388_minus_two_thirds"],"mu_minus":["copied_original_records","mu_minus"],"pi":["copied_original_records","pi"],"reciprocal_sqrt_two":["copied_original_records","reciprocal_sqrt_two"],"shell_1153":["copied_original_records","shell_1153"]}''')
W2C_INVENTORY_PIN=json.loads(r'''{"bytes":45161,"git_blob_sha":"389e6c6ade2a7f8943ebd9466e3c3b1003a4d720","path":"topics/visible-flex-exact-nearby/notes/2026-11-16-R133-collar-Volterra-dual-exact-input-inventory.json","role":"W2C_input_inventory","sha256":"8258111dd24b18593aea2f90aabdc89a0ba08b6f8fc7947f3aac63ecc5426db7"}''')
NEW_PROOF_PINS=json.loads(r'''{"proof_W2C":{"bytes":25536,"git_blob_sha":"41e309e49a41984fb624afbca21684f7e91c7c79","path":"topics/visible-flex-exact-nearby/results/R133-supplement-complete-collar-Volterra-dual-feedback-candidate.md","role":"proof_W2C","sha256":"09ada380c17b64f26d0f88f49734d52361b794ce10b6617b16d58f6de053ae01"},"proof_WJK":{"bytes":14025,"git_blob_sha":"72c3c33c11dc4c1904db4a3dac48dff44f040716","path":"topics/visible-flex-exact-nearby/results/R133-supplement-joint-centre-Green-kernel-and-complete-collar-cross-terms.md","role":"proof_WJK","sha256":"5b9a257a25b22b84423240242846f1fb4687573f9292773591cff01e7401c5ba"}}''')
COLLAR_CURRENT_PINS=json.loads(r'''{"beta_record_definition":{"bytes":30343,"git_blob_sha":"6a0713f931680adfd04e87949087189aa1d75e02","path":"topics/visible-flex-exact-nearby/scripts/fourfold_phase_beta_interval.py","role":"beta_record_definition","sha256":"ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f"},"collar_original_manifest":{"bytes":6381,"git_blob_sha":"e70b6361315e55e658f8541879481249cfcbeada","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-full-delta96-root-collar-CI-inputs.json","role":"collar_original_manifest","sha256":"38d76e08d2d92b2d2395ec13c5c61817ace7da6bd6a1856061156a2b377bc76f"},"complex_germ_record_definition":{"bytes":11227,"git_blob_sha":"a674befc55e1a2af8cc848565da6986f5e3d4295","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_turning_complex_germ.py","role":"complex_germ_record_definition","sha256":"ebdfc4f6f281892757505023f17874501966ba20b987b8738337b4818a5d8d45"},"metric_record_definition":{"bytes":13046,"git_blob_sha":"cc1c1e0b271e69e7415712c5bb82678c94c3e5f8","path":"topics/visible-flex-exact-nearby/scripts/fourfold_phase_metric_defect.py","role":"metric_record_definition","sha256":"c4196dddcbfab15116c06a9be8a2120916c05d77fe3d7cb152f842f16b80a7de"},"moving_germ_definition":{"bytes":13009,"git_blob_sha":"f4ee58e89ab792def1c442ab6028e51d7452465e","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_moving_turning_complex_germ.py","role":"moving_germ_definition","sha256":"a3ad50b828c69d3e6f1e9254c1f266535171741ee2cd675d1569ef8f0fac0491"},"root_scalarization_definition":{"bytes":19473,"git_blob_sha":"049d7d184f25fd1e5e2b3025a1f6be7083291dd9","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_current_root_scalarization_budget.py","role":"root_scalarization_definition","sha256":"4a3ee217b21cabda6ae3dea052f27ff82f03b4218294145dc2f812891688e03e"},"root_scalarization_manifest":{"bytes":4942,"git_blob_sha":"a4de300fe8338875cb7f8062efaee60da7dc4864","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-current-root-scalarization-CI-inputs.json","role":"root_scalarization_manifest","sha256":"b1e47bdc43fdb5f9742ee8feb087f5a66dd72457439405abecb1816012b1c746"},"root_scalarization_process":{"bytes":4120,"git_blob_sha":"37437b0475d8d361d3b10c4384ef486eb5be040f","path":"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/consumers/process.json","role":"root_scalarization_process","sha256":"9f1d18061f1b406f028916adc33484b4deea826a8e4175fd28b0fdb5b690342d"}}''')
ADDITIONAL_HISTORICAL_INPUTS=json.loads(r'''[{"bytes":7851,"commit":"ae319f7544b3c94b5dbcb5290557ed04b66641eb","git_blob_sha":"2b90cfe80a6381badc29f02f7dcb3dce2584851d","path":"topics/visible-flex-exact-nearby/notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz","role":"original_signed_intrinsic_root_germ","sha256":"397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864"},{"bytes":30595,"commit":"ae319f7544b3c94b5dbcb5290557ed04b66641eb","git_blob_sha":"1b1c6f11478c800ef76e1519c266e80b9d08916c","path":"topics/visible-flex-exact-nearby/notes/current_root_scalarization_ci/run-43594466882-1/consumers/complete-moving-root-scalarization.json.gz","role":"original_complete_root_budget_and_saved_exact_offsets","sha256":"10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f"}]''')
GERM_FIELDS=json.loads(r'''["actual_candidate_piece","actual_fixed_nu","actual_fold_constructed","actual_nonlinear_solution_proved","all_finite_candidate_modes_retained","angle_inverse","bits","bounds","candidate_sha256","compact_bump_identically_zero_on_entire_actual_germ","complete","complete_energy_product_fees","complete_primitive_tail","complex_intrinsic_coefficients","complex_radial_radius","complex_radial_rectangle","dependencies","domain_contains_disks_about_every_true_parameter_root","exact_amplitude","exact_candidate_metadata","exact_candidate_piece_interval","exact_center_parameter","exact_parameter_half_width","failure","finite_energy_is_bilinear_zero_convolution_without_conjugation","full_feedback_inverse_proved","gates","inputs","kind","moving_U_derivative_Astrip","moving_mean_v","moving_mean_v_radial","moving_nonlocal_linearization_replaced_by_local_multiplication","moving_phi_strip","moving_v_derivative_Astrip","object_sha256","original_scalar_germ","physical_U_derivative_sup","physical_candidate_is_analytic_inverse_angle_pullback_not_finite_physical_Fourier","physical_jacobi_at_approximate_centre_does_not_assume_zero_residual","physical_theta_strip","physical_v_derivative_sup","proved","root_interval","seconds","source_sha256","whole_affine_parameter_interval"]''')
ROOT_BUDGET_FIELDS=json.loads(r'''["K_abs_upper","L_derivative_commutator_bounds","Neumann_factor","Sobolev_norm","actual_R31_selected_parameter_included","actual_independent_even_mean_preserved","actual_intrinsic_parameter","actual_nonlinear_PDE_branch_or_response_proved_here","actual_nonlocal_operator_retained","actual_scientific_checkout_commit","all_projected_radial_and_drift_commutators_paid","angular_zero_mode_removed_only_in_A_inverse","background_definition_sha256","background_repair_angular_norms_u","background_repair_angular_norms_v","beta_abs_upper","candidate_sha256","complete","complete_even_mean_retained","complete_independent_mean_row","complete_lower_operators","direction_angular_norms_u","direction_angular_norms_v","eta_inverse_abs_upper","exact_background_root_offsets","exact_candidate_and_response_piece","exact_complex_parameter_radius","exact_inner_radial_radius","exact_intrinsic_parameter","exact_moving_Wiener_strip","exact_outer_radial_radius","exact_piece_interval","exact_radial_rectangle","exact_root_interval","explicit_direction_definition_sha256","failure","fractional_one_gain_Sobolev_bounds","full_D0_inverse_commutator_same_space_inner_disk","full_complex_mean_abs_lower","full_complex_mean_abs_upper","full_family_U_angular_norms","full_family_V_angular_norms","full_frequency_inverse_not_a_finite_section","gamma_abs_lower","gamma_abs_upper","gates","inputs","integer_derivative_recursion","integer_one_gain_Sobolev_bounds","inverse_drift_commutator_same_space","inverse_followed_by_angular_derivative","inverse_radial_derivative_integer_one_gain_inner_disk","inverse_radial_derivative_same_space_inner_disk","inverse_same_space","kind","moving_d_Astrip","moving_d_phi_Astrip","moving_d_phiphi_Astrip","no_actual_PDE_background_transfer_inferred","no_full_phase_transport_or_response_recomputed","only_original_response_shard005_is_consumed","ordinary_source_retained_in_divergence_form","original_response_local_piece","original_response_shard_range","other_response_shards_rebuilt_or_revalidated_here","positive_high_input_graph_or_full_inverse_proved_here","proved","public_repository","public_run_attempt","public_run_id","radial_derivative_requires_inner_half_disk","response_raw_complete_coefficient_upper","response_repaired_complete_coefficient_upper","root_two_row_matching_proved_here","runtime","same_space_norms","seconds","source_sha256","strong_return_remainder_or_complete_beta_proved_here","whole_original_intrinsic_parameter_family_claimed","workflow_event_commit"]''')
GERM_GATES=json.loads(r'''["complete new moving candidate and all SHA-bound radial shards loaded","one actual scalar germ and one actual new PPoly piece contain the complex product","whole original affine parameter and complete primitive tail retained","actual moving mean and v are nonzero on the complete complex product","true theta_phi close to one on the entire complex moving strip","full complex-r vertical displacement paid before inverse angle construction","global periodic inverse of the true physical angle is a strict Banach contraction","all physical angular derivatives through four use the full rational chain rule","intrinsic simple root and actual physical characteristic amplitude have positive real part","complete original local physical Jacobi matrix retained including both means"]''')
ROOT_BUDGET_GATES=json.loads(r'''["the original complete complex germ and candidate identity are retained","the exact continuous background and complete direction identities match","all193 physical response states and the true mean are in the original shard","one original lossless shard has its exact declared range and byte hash","the original response polynomial contains every root component","the whole complex root disk lies on the same exact scalar and response piece","the compact metric and intrinsic root are exactly independent of nu here","the actual selected R31 parameter is in the declared explicit-family disk","the actual root background offsets and all193 direction repair fees remain","full repaired explicit-family angular bounds through four are finite","the complete complex mean and gamma stay nonzero on the whole family disk","the complete angular Neumann factor is strictly below3over20","all inverse Sobolev windows and complete mean source fees are finite"]''')
COLLAR_PROCESS_GATES=json.loads(r'''["the actual completed original germ and full193 direction identities agree","the full real family and true complete positive collar stay in one original root piece","all full-family angular norms and true optical speed are uniformly bounded","the same intrinsic positive curvature and optical slope satisfy the root hypotheses","the complete local reaction and full drift meet the declared family bounds","both complete primitive rows and the genuine mean rank remain paid","any allowed positive extension and terminal scalar has the same two-row root reference bound","the true band192 frequency ratio and smallest primitive index are paid","the entire unbounded high kernel closes with the new full-family constants","both high ordinary-source and independent incoming-port state contracts close","the full incoming and outgoing high raw traces close","the complete193 head and every output through288 satisfy both crossing contracts","the actual all-radial low Cauchy propagator retains its mean and all columns","the new complete head-high return is below1over500000","the complete ordinary source-to-state bound is below1over12000","the complete full port-to-state bound is below1over100","both endpoint complete ordinary-source trace bounds are below1over36","both endpoint complete input-port trace bounds are below9over2","orders0through4 keep the same full high inverse with band192 commutators"]''')
INTRINSIC_NAMES=json.loads(r'''["a","a1","a2","a3","E","E1","E2","rotational_gap","K","K1","gamma","beta","s"]''')
PARAMETER_GUARDS=json.loads(r'''{"actual_delta_degree":96,"actual_tail_inverse_bound":3,"bits":320,"collar_piece":2549,"complete_family_residual_last_index":416,"complete_new_scalar_targets":50,"conditional_inverse_targets":2,"cutoff_width":"1/16","decimal_record_digits":75,"first_high_index":97,"fixed_completed_provider":"WVC_43891414339_1","head_dimension":193,"high_trial_last_index":224,"new_array_artifacts":false,"old_collar_eta_reused":true,"old_targets_recomputed":0,"original_complete_same_operator_records":29,"parent_band_subcells":8,"parent_cells":153,"physical_high_minimum":388,"real_direction_radius":"1/100000000","reference_centre_degree":32,"reference_high_last_index":160,"refined_cells":24480,"repaired_centre_residual_last_index":288,"same_actual_spaces_and_projections":true,"true_root_is_not_an_enclosure_endpoint":true,"uniform_refinement":160}''')

def admit_completed_tracefree_inputs(admitted,texts,by_role,core):
 """All 56 completed WVC records and every original field remain read-only.

 The full current actual/manifest/execution bytes are verified independently.
 Whole-file bindings preserve every prior qualification; the projections below
 contain exactly the literal records needed by the new complete candidate.
 No original numeric producer is imported or called.
 """
 require, data, canonical, digest, at = (
  core.require, core.data, core.canonical, core.digest, core.at)
 finite_display_tokens = core.finite_display_tokens
 for role,spec in COMPLETED_TRACE_PINS.items():
  require(by_role.get(role)==spec,"fixed complete previous WVC/proof object "+role)
 prior=data(texts["WVC_actual"]);execution=data(texts["WVC_execution"])
 old_manifest=data(texts["WVC_manifest"])
 for value,identities,label in (
    (prior,COMPLETED_TRACE_FIELD_IDENTITIES,"complete previous WVC science"),
    (execution,COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES,"complete previous WVC execution")):
  require(set(value)==set(identities),label+" field set")
  for key,expected in identities.items():
   raw=canonical(value[key])
   require(len(raw)==expected["bytes"] and digest(raw)==expected["sha256"],
           label+" entire original field "+key)
 require(prior["kind"]=="complete_continuous_centre_tracefree_candidate_v1"
         and prior["problem_id"]=="WVC_complete_continuous_centre_tracefree_candidate_v1"
         and prior["complete"] is True and prior["proved"] is True
         and prior["stage"]=="complete" and prior["failure"] is None
         and prior["actual_returncode"]==0 and prior["current_target"] is None
         and prior["automatic_retry_authorized"] is False,
         "original completed WVC candidate, no altered failure classification")
 require(prior["gates"]==[{"name":name,"passed":True} for name in COMPLETED_TRACE_GATES]
         and len(prior["gates"])==23,"all original WVC structural gates")
 require(set(prior["complete_new_graphs"])==set(COMPLETED_TRACE_GRAPH_KEYS)
         and len(prior["completed_targets"])==6
         and set(prior["completed_targets"])==set(COMPLETED_TRACE_GRAPH_KEYS),
         "all six complete WVC graphs in original order")
 count=0
 for name,keys in COMPLETED_TRACE_GRAPH_KEYS.items():
  graph=prior["complete_new_graphs"][name]
  require(set(graph)=={"complete","new_records","copied_records"}
          and graph["complete"] is True and graph["copied_records"]=={}
          and set(graph["new_records"])==set(keys)
          and prior["saved_record_counts"][name]==len(keys)
          and prior["saved_copy_counts"][name]==0,
          "complete original WVC graph shape "+name)
  for key in keys:
   record_value=graph["new_records"][key]
   require(isinstance(record_value,dict) and set(record_value)=={"ball"},
           "exact original WVC scalar object "+name+"/"+key)
   finite_display_tokens(record_value["ball"],"original WVC/"+name+"/"+key)
   count+=1
 require(count==prior["actual_progress"]["new_scalar_records_saved"]==56,
         "all fifty-six completed original WVC bounds")
 prefix=prior["reference_mode_prefix"]
 require(set(prefix)=={"completed_modes","running","witnesses","status"}
         and prefix["completed_modes"]==96 and len(prefix["running"])==5
         and set(prefix["running"])==set(prefix["witnesses"])
         and prefix["status"]=={"changed_modes_completed":96,"unchanged_modes_qualified":0,
                               "all_reference_targets_copied":False},
         "original five complete modal maxima and full changed-mode qualification")
 for key,value in prefix["running"].items():
  require(set(value)=={"ball"},"original complete WVC modal record")
  finite_display_tokens(value["ball"],"original WVC modal prefix/"+key)
  witness=prefix["witnesses"][key]
  require(set(witness)=={"origin","mode"} and witness["origin"]=="new_changed_mode"
          and type(witness["mode"]) is int and 1<=witness["mode"]<=96,
          "full original WVC witness")
 require(prior["reference_selection"]["complete"] is True
         and prior["reference_selection"]["changed_mode_indices"]==list(range(1,97))
         and prior["reference_selection"]["unchanged_mode_indices"]==[]
         and prior["reference_selection"]["same_actual_spaces_and_projection"] is True,
         "actual completed WVC selected reference identity")
 require(prior["finite_gate"]["passed"] is False
         and prior["finite_gate"]["actual_tail_inverse_upper"]==3
         and prior["finite_gate"]["actual_tail_gate_is_published_analytic_m160"] is True
         and prior["finite_gate"]["complete_defect_record"]==
           prior["complete_new_graphs"]["complete_actual_E_D_T"]["new_records"][
              "complete_actual_finite_defect_upper"]
         and prior["conditional_finite_inverse"] is None,
         "original complete finite sufficient gate remains false")
 progress=prior["actual_progress"]
 require(progress["original_body_intersections"]==4801
         and progress["original_closed_rows_covered"]==4650
         and progress["completed_new_body_parent_packets"]==152
         and progress["comparison_cells"]==155 and progress["refined_cells"]==24480
         and progress["new_reference_modes_computed"]==progress["reference_modes_completed"]==96
         and progress["unchanged_reference_modes_read"]==0
         and all(progress[key]==0 for key in (
           "old_targets_recomputed","old_producer_imports_or_calls",
           "old_reference_bounds_reevaluated","dense_finite_matrices_allocated",
           "new_array_artifacts_published","physical_state_columns_computed",
           "conditional_finite_inverses","graph_old_records_copied")),
         "complete old WVC domain and zero recomputation/lost boundary")
 require(old_manifest["kind"]=="complete_continuous_centre_tracefree_current_inputs_v1"
         and old_manifest["problem_id"]==prior["problem_id"]
         and old_manifest["expected_current_input_count"]==41
         and len(old_manifest["files"])==41
         and old_manifest["parameters"]==prior["parameters"]
         and old_manifest["retained_scope"]==prior["retained_scope"]
         and old_manifest["scientific_modules"]==prior["scientific_modules"]
         and digest(texts["WVC_manifest"].encode())==prior["manifest_sha256"]
             ==execution["manifest_sha256"],
         "complete original WVC source/manifest identity")
 old_by_role={s["role"]:s for s in old_manifest["files"]}
 fixed_provider=admitted["W2CI"]["fixed_same_operator_provider"]
 require(fixed_provider["scientific"]=={
          key:by_role["WVC_actual"][key] for key in ("path","bytes","sha256")}
         and fixed_provider["parameters"]==prior["parameters"]
         and fixed_provider["retained_scope"]==prior["retained_scope"]
         and fixed_provider["original_admission"]==prior["original_admission"]
         and fixed_provider["source"]==old_by_role["science"],
         "W2CI entire fixed provider parameters, original admission and retained scope")
 require(len(old_by_role)==41 and prior["complete_current_file_receipts"]==old_manifest["files"]
         and execution["current_input_receipts"]==old_manifest["files"]
         and prior["input_sha256"]=={k:s["sha256"] for k,s in old_by_role.items()},
         "all forty-one original whole-file receipts")
 replaced={"science","readonly_admission","kernel_math","assembly_math","reference_math","worker","rules"}
 for role,spec in old_by_role.items():
  if role not in replaced:
   require(by_role[role]==spec,"same complete WVC coefficient/proof input "+role)
 require(old_manifest["core_current_files"]==admitted["manifest"]["core_current_files"]
         and old_manifest["historical_inputs"]==admitted["manifest"]["historical_inputs"][:19]
         and len(execution["AST_receipts"])==16,
         "unchanged full core and nineteen historical objects")
 for item in execution["AST_receipts"]:
  require(set(item)=={"path","role","sha256"} and item["role"] in old_by_role
          and item["path"]==old_by_role[item["role"]]["path"]
          and item["sha256"]==old_by_role[item["role"]]["sha256"],
          "original WVC full AST identity")
 require(execution["scientific_children"]==1 and execution["scientific_started"] is True
         and execution["scientific_complete"] is True and execution["actual_child_returncode"]==0
         and execution["failure"] is None and execution["interrupted_target"] is None
         and execution["original_scientific_failure"] is None
         and execution["original_scientific_complete_flag"] is True
         and execution["completed_old_targets_recomputed"]==0
         and execution["new_artifacts"]==execution["new_arrays_published"]==execution["new_Releases"]==0,
         "complete original WVC scientific execution")
 for key in ("run_id","run_attempt","workflow_event_commit"):
  require(execution[key]==prior[key],"original WVC execution/science "+key)
 require(execution["actual_scientific_checkout"]==prior["actual_checkout_commit"]
         and execution["scientific_files"]==[{
             k:by_role["WVC_actual"][k] for k in ("path","bytes","sha256")}],
         "complete actual WVC scientific file")
 preflight=execution["readonly_preflight"]
 require(preflight["returncode"]==0 and preflight["stderr_bytes"]==0
         and preflight["complete_output"]["complete"] is True
         and preflight["complete_output"]["flint_imported"] is False
         and preflight["complete_output"]["admission"]==prior["original_admission"],
         "entire original WVC successful readonly boundary")
 raw=canonical(preflight["complete_output"])
 require(len(raw)==preflight["stdout_bytes"] and digest(raw)==preflight["stdout_sha256"],
         "whole original WVC preflight bytes")
 paired=admitted["paired_inputs"]
 for key,current in (
    ("copied_original_records",paired["records"]),
    ("copied_original_scope",paired["scope"]),
    ("copied_complete_candidate_metadata",admitted["candidate_metadata"]),
    ("copied_complete_repair_definition",admitted["repair_definition"]),
    ("retained_completed_five_maxima",paired["completed_five_maxima"]),
    ("retained_original_false_candidates",paired["old_false_candidates"]),
    ("reference_chain",paired["reference_chain"]),
    ("prior_completed_candidate",admitted["completed_paired_inputs"]["archive"])):
  require(prior[key]==current,"full original WVC qualification "+key)
 require(prior["complete_restoration_receipts"]==execution["historical_restoration"]
         and digest(canonical(prior["complete_restoration_receipts"]))==
             admitted["admission"]["restoration_receipts_sha256"],
         "entire unchanged original restoration")
 common_keys=("old_gate_counts","old_source_import_count","old_targets_recomputed",
  "repairs_regenerated","native_bytes","native_sha256","per_order_complete_rows",
  "inflated_rows","interfaces","original_progress_counter",
  "original_parts_manifest_row_counter","candidate_shape","candidate_nodes",
  "repair_suprema_count","historical_input_count","restoration_receipts_bytes",
  "restoration_receipts_sha256","prior_completed_candidate_records",
  "prior_completed_modal_prefix_records")
 require(all(admitted["admission"][key]==prior["original_admission"][key]
             for key in common_keys),"same complete original native/cubic facts")
 require(prior["original_admission"]["new_source_AST_count"]==5
         and prior["original_admission"]["old_source_AST_count"]==10
         and prior["original_admission"]["current_file_count"]==41,
         "old AST/current counts are retained as old metadata")
 copied={key:at(prior,path) for key,path in COMPLETED_TRACE_COPY_PATHS.items()}
 original_copy_contract=admitted["W2CI"]["literal_same_operator_original_records"]
 require(len(copied)==original_copy_contract["count"]==29
         and len(canonical(copied))==original_copy_contract["complete_object_identity"]["bytes"]==4653
         and digest(canonical(copied))==
             original_copy_contract["complete_object_identity"]["sha256"]==
             "f1ec45f0f3ddb6ded2856ccc24b04528743aacfbfbfb62a04bb0c39a075ef55b",
         "all twenty-nine complete original same-operator objects")
 for item in original_copy_contract["records"]:
  require(copied[item["name"]]==item["record"]
          and COMPLETED_TRACE_COPY_PATHS[item["name"]]==item["json_path"],
          "complete immutable W2CI record and typed path "+item["name"])
 require(original_copy_contract["previous_false_gate"]==prior["finite_gate"],
         "same original false sufficient gate is preserved")
 reference=prior["complete_new_graphs"]["complete_reference_receivers"]["new_records"]
 old_paired=admitted["completed_paired_inputs"]
 mean_record=old_paired["reference_records"]["complete_reference_mean_endpoint_receiver_upper"]
 family_record=old_paired["family_HL_record"]
 archive={
  "complete_original_scientific_file":by_role["WVC_actual"],
  "complete_original_execution_file":by_role["WVC_execution"],
  "complete_original_manifest_file":by_role["WVC_manifest"],
  "complete_original_field_verification":{
   "scientific_field_count":43,"execution_field_count":44,
   "scientific_identity_table_sha256":digest(canonical(COMPLETED_TRACE_FIELD_IDENTITIES)),
   "execution_identity_table_sha256":digest(canonical(COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES)),
   "full_tables_are_in_the_current_pinned_readonly_module":True,
   "all_original_fields_verified_before_science":True},
  "complete_original_parameters":prior["parameters"],
  "complete_original_retained_scope":prior["retained_scope"],
  "complete_original_actual_progress":prior["actual_progress"],
  "complete_original_finite_gate":prior["finite_gate"],
  "complete_original_reference_mode_prefix":prefix,
  "complete_original_reference_selection":prior["reference_selection"],
  "complete_original_reference_graph":prior["complete_new_graphs"]["complete_reference_receivers"],
  "complete_twenty_nine_copied_record_objects":copied,
  "complete_W2CI_required_contexts":[
   _complete_context(by_role["WVC_actual"],prior,[key],core)
   for key in fixed_provider["immutable_full_context_paths"]],
  "complete_original_mean_reference_record":mean_record,
  "complete_original_family_HL_record":family_record,
  "complete_original_scientific_modules":prior["scientific_modules"],
  "complete_original_completion":{k:prior[k] for k in (
      "complete","proved","stage","failure","actual_returncode","automatic_retry_authorized")},
  "complete_original_graphs_identity":{
   "bytes":len(canonical(prior["complete_new_graphs"])),
   "sha256":digest(canonical(prior["complete_new_graphs"]))},
  "complete_prior_WPS_archive_identity":{
   "bytes":len(canonical(prior["prior_completed_candidate"])),
   "sha256":digest(canonical(prior["prior_completed_candidate"])),
   "whole_archive_is_in_the_original_WVC_file_and_was_independently_reconstructed":True},
  "all_fifty_six_records_and_five_modal_prefixes_read_without_reevaluation":True,
  "full_previous_WPS_and_WPTVS_scopes_remain_in_the_complete_original_files":True,
  "all_original_complete_objects_bound_by_full_file_and_field_identity":True,
  "no_original_success_or_false_sufficient_gate_reclassified":True}
 return {"archive":archive,"reference_records":reference,"mean_reference_record":mean_record,
         "family_HL_record":family_record,"copied_records":copied,
         "selected_diagonal_chain":prior["reference_selection"]["selected_diagonal_chain"],
         "complete_original_candidate":prior,
         "old_completed_record_count":56,"old_prefix_record_count":5}


def _typed_native_tree(value,core,path="native"):
 """Verify every original numeric record without performing ball arithmetic."""
 if isinstance(value,dict):
  keys=set(value)
  if keys & {"ball","lower","upper","mid_float","radius_upper_float"}:
   core.intrinsic_record(value,path)
   return 1
  return sum(_typed_native_tree(child,core,path+"/"+str(key))
             for key,child in value.items())
 if isinstance(value,list):
  return sum(_typed_native_tree(child,core,path+"/"+str(index))
             for index,child in enumerate(value))
 if isinstance(value,Decimal):
  core.require(value.is_finite(),path+": finite original JSON diagnostic")
 else:
  core.require(type(value) in (str,int,bool,type(None)),
               path+": complete original JSON primitive")
 return 0


def _array_records(value,count,core,label):
 core.require(isinstance(value,list) and len(value)==count,
              label+": complete fixed array length")
 for index,item in enumerate(value):
  core.intrinsic_record(item,label+"/"+str(index))
 return value


def _complex_record(value,core,label):
 core.require(isinstance(value,dict) and set(value)=={"real","imag","modulus_upper"},
              label+": full signed complex record")
 for key in ("real","imag","modulus_upper"):
  core.intrinsic_record(value[key],label+"/"+key)


def _read_native(path,spec,core):
 raw=Path(path).read_bytes()
 core.require(len(raw)==spec["bytes"] and core.digest(raw)==spec["sha256"]
              and hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
                  ==spec["git_blob_sha"]
              and raw.startswith(b"\x1f\x8b"),
              "complete original compressed bytes before decoding: "+spec["role"])
 decoded=gzip.decompress(raw)
 value=core.data(decoded)
 core.require(isinstance(value,dict),"whole original native JSON object")
 identity={
  "role":spec["role"],"path":spec["path"],"commit":spec["commit"],
  "git_blob_sha":spec["git_blob_sha"],"bytes":len(raw),"sha256":core.digest(raw),
  "decoded_bytes":len(decoded),"decoded_sha256":core.digest(decoded),
  "complete_bytes_verified_before_gzip":True,
  "old_producer_executed":False,
 }
 return value,identity


def _complete_context(spec,value,path,core):
 original=core.at(value,path)
 raw=core.canonical(original)
 return {
  "source_role":spec["role"],"source_path":spec["path"],
  "source_bytes":spec["bytes"],"source_sha256":spec["sha256"],
  "source_git_blob_sha":spec["git_blob_sha"],"json_path":list(path),
  "complete_original_object_bytes":len(raw),
  "complete_original_object_sha256":core.digest(raw),
  "whole_original_object_retained_by_immutable_identity":True,
 }


def admit_collar_natives(admitted,texts,by_role,root_germ_path,root_budget_path,core):
 """Decode the two complete original objects only after whole byte admission."""
 require=core.require
 inventory=admitted["W2CI"];manifest=admitted["manifest"]
 specs=ADDITIONAL_HISTORICAL_INPUTS
 require(inventory["two_additional_native_restorations"]==specs
         and manifest["historical_inputs"][19:]==specs,
         "exact two additional native restore identities")
 germ,germ_identity=_read_native(root_germ_path,specs[0],core)
 rb,rb_identity=_read_native(root_budget_path,specs[1],core)
 require(set(germ)==set(GERM_FIELDS) and set(rb)==set(ROOT_BUDGET_FIELDS),
         "all47 germ and all81 budget fields match their complete original producers")
 germ_record_count=_typed_native_tree(germ,core,"original germ")
 rb_record_count=_typed_native_tree(rb,core,"original root budget")
 require(germ["kind"]=="actual_moving_candidate_complete_physical_angle_complex_turning_germ"
         and germ["complete"] is True and germ["proved"] is True
         and germ["failure"] is None
         and germ["source_sha256"]==by_role["moving_germ_definition"]["sha256"]
         and germ["gates"]==[{"name":name,"passed":True} for name in GERM_GATES],
         "complete original signed germ and all ten original gates")
 require(rb["kind"]=="complete_moving_current_root_scalarization_operator_budget"
         and rb["complete"] is True and rb["proved"] is True and rb["failure"] is None
         and rb["source_sha256"]==by_role["root_scalarization_definition"]["sha256"]
         and rb["public_repository"]==REPOSITORY
         and str(rb["public_run_id"])=="43594466882"
         and str(rb["public_run_attempt"])=="1"
         and rb["gates"]==[{"name":name,"passed":True} for name in ROOT_BUDGET_GATES],
         "complete original root scalarization and all thirteen original gates")

 root_manifest=core.data(texts["root_scalarization_manifest"])
 root_process=core.data(texts["root_scalarization_process"])
 collar_manifest=core.data(texts["collar_original_manifest"])
 collar_process=admitted["collar_process"]
 require(root_manifest["kind"]=="complete_moving_current_root_scalarization_public_CI_input_manifest"
         and root_manifest["public_repository"]==REPOSITORY
         and root_manifest["scientific_inputs_selected_by_exact_hash"] is True
         and root_manifest["runtime"]==rb["runtime"]
         and root_manifest["no_full_phase_or_full_response_replay"] is True
         and root_manifest["original_completed_root_envelope_reused"] is True
         and root_manifest["only_original_response_shard005_consumed"] is True
         and root_manifest["original_response_shard_artificially_split"] is False
         and root_manifest["genuine_PDE_solution_or_full_root_return_not_claimed"] is True,
         "full original root manifest qualifications")
 require(root_process["kind"]=="actual_public_complete_moving_root_scalarization_execution"
         and root_process["complete"] is True
         and root_process["mathematical_complete"] is True
         and type(root_process["actual_returncode"]) is int
         and root_process["actual_returncode"]==0
         and root_process["public_repository"]==REPOSITORY
         and root_process["run_id"]=="43594466882" and root_process["run_attempt"]=="1"
         and root_process["mathematical_source_sha256"]==rb["source_sha256"]
         and root_process["manifest_sha256"]==by_role["root_scalarization_manifest"]["sha256"]
         and root_process["native_sha256"]==specs[1]["sha256"]
         and root_process["mathematical_gates"]==rb["gates"]
         and root_process["workflow_event_commit"]==rb["workflow_event_commit"]
         and root_process["actual_scientific_checkout_commit"]==
             rb["actual_scientific_checkout_commit"],
         "complete original root scientific/process/manifest binding")
 require(collar_manifest["kind"]=="actual_full_real_delta96_positive_root_collar_public_input_manifest"
         and collar_manifest["public_repository"]==REPOSITORY
         and collar_manifest["scientific_inputs_selected_by_exact_hash"] is True
         and collar_manifest["ordinary_source_has_no_radial_derivative"] is True
         and collar_manifest["independent_mean_and_all_unknown_frequencies_retained"] is True
         and collar_manifest["full_positive_body_and_actual_outer_scalar_transfer_not_claimed"] is True,
         "same whole real collar public contract")
 require(collar_process["kind"]=="actual_public_full_real_delta96_root_collar_execution"
         and collar_process["complete"] is True
         and collar_process["mathematical_complete"] is True
         and type(collar_process["actual_returncode"]) is int
         and collar_process["actual_returncode"]==0
         and collar_process["run_id"]=="43606747196" and collar_process["run_attempt"]=="1"
         and collar_process["mathematical_source_sha256"]==by_role["collar_source"]["sha256"]
         and collar_process["manifest_sha256"]==by_role["collar_original_manifest"]["sha256"]
         and collar_process["mathematical_gates"]==
             [{"name":name,"passed":True} for name in COLLAR_PROCESS_GATES],
         "unchanged original complete collar process")
 root_input_files={item["path"]:item for item in root_manifest["files"]}
 require(len(root_input_files)==len(root_manifest["files"])
         and set(rb["inputs"])==set(root_manifest["input_paths"])
         =={"root_germ","repair","direction","trial_index","trial_shard","strip_proof"},
         "complete six original root scalarization input identities")
 for key,path in root_manifest["input_paths"].items():
  expected=root_input_files[path];actual=rb["inputs"][key]
  require(set(expected)=={"path","bytes","sha256"}
          and set(actual)=={"path","bytes","sha256"}
          and actual["bytes"]==expected["bytes"]
          and actual["sha256"]==expected["sha256"]
          and isinstance(actual["path"],str)
          and (actual["path"]==path or actual["path"].endswith("/"+path)),
          "complete original root input "+key)
 require(rb["inputs"]["root_germ"]["sha256"]==specs[0]["sha256"]
         and rb["inputs"]["repair"]["sha256"]==
             manifest["historical_inputs"][18]["sha256"],
         "same original signed germ and whole exact repair")
 collar_input_files={item["path"]:item for item in collar_manifest["files"]}
 for spec in specs:
  require(collar_input_files[spec["path"]]=={
    key:spec[key] for key in ("path","bytes","sha256")},
    "both complete native identities in original collar contract")
 require(set(germ["inputs"].values()) >= {
             by_role["candidate_index"]["sha256"],
             admitted["candidate_metadata"]["object_sha256"]}
         and len(germ["inputs"])==3
         and isinstance(germ["dependencies"],dict)
         and set(germ["dependencies"])=={
          "fourfold_phase_codazzi_coefficients.py",
          "fourfold_codazzi_candidate_shards.py",
          "fourfold_codazzi_moving_polynomial_system.py",
          "fourfold_codazzi_turning_complex_germ.py",
          "fourfold_phase_beta_bulk_interval.py",
          "fourfold_phase_metric_defect.py"}
         and all(isinstance(value,str) and len(value)==64
                 and all(c in "0123456789abcdef" for c in value)
                 for value in germ["dependencies"].values()),
         "complete original germ input/dependency identities remain original")

 repair=admitted["repair"];meta=admitted["candidate_metadata"]
 require(germ["candidate_sha256"]==rb["candidate_sha256"]==
             repair["candidate_sha256"]==by_role["candidate_index"]["sha256"]
         and germ["object_sha256"]==meta["object_sha256"]==
             repair["definition"]["object_sha256"]
         and rb["background_definition_sha256"]==repair["derived_definition_sha256"]
         and rb["explicit_direction_definition_sha256"]==
             admitted["native"]["explicit_direction_definition_sha256"]
         and germ["exact_candidate_metadata"]==meta
         and germ["exact_amplitude"]==meta["exact_float_amplitude"]==
             repair["definition"]["exact_alpha"]
         and germ["actual_fixed_nu"]==meta["exact_float_nu"]
         and rb["exact_intrinsic_parameter"]==germ["exact_center_parameter"],
         "same actual candidate, object, background, direction and intrinsic parameter")
 require(meta["modes"]==32 and meta["physical_frequency_factor"]==4
         and meta["finite_BVP_success"] is True
         and meta["mathematical_certificate"] is False
         and repair["definition"]["offsets_independent_of_eta_and_nu"] is True,
         "original physical65 coordinates, exact dyadic alpha and fixed offsets")
 for key in (
   "whole_affine_parameter_interval",
   "domain_contains_disks_about_every_true_parameter_root",
   "compact_bump_identically_zero_on_entire_actual_germ",
   "finite_energy_is_bilinear_zero_convolution_without_conjugation",
   "all_finite_candidate_modes_retained",
   "physical_candidate_is_analytic_inverse_angle_pullback_not_finite_physical_Fourier",
   "physical_jacobi_at_approximate_centre_does_not_assume_zero_residual"):
  require(germ[key] is True,"original germ qualification "+key)
 for key in ("actual_nonlinear_solution_proved","actual_fold_constructed",
             "full_feedback_inverse_proved",
             "moving_nonlocal_linearization_replaced_by_local_multiplication"):
  require(germ[key] is False,"original germ unproved scope "+key)
 for key in (
   "no_full_phase_transport_or_response_recomputed","actual_nonlocal_operator_retained",
   "complete_even_mean_retained","only_original_response_shard005_is_consumed",
   "full_frequency_inverse_not_a_finite_section","ordinary_source_retained_in_divergence_form",
   "angular_zero_mode_removed_only_in_A_inverse","actual_independent_even_mean_preserved",
   "all_projected_radial_and_drift_commutators_paid","radial_derivative_requires_inner_half_disk",
   "actual_R31_selected_parameter_included","no_actual_PDE_background_transfer_inferred"):
  require(rb[key] is True,"complete original root qualification "+key)
 for key in (
   "other_response_shards_rebuilt_or_revalidated_here","root_two_row_matching_proved_here",
   "positive_high_input_graph_or_full_inverse_proved_here",
   "actual_nonlinear_PDE_branch_or_response_proved_here",
   "strong_return_remainder_or_complete_beta_proved_here",
   "whole_original_intrinsic_parameter_family_claimed"):
  require(rb[key] is False,"original root scope remains limited "+key)
 require(rb["actual_intrinsic_parameter"]=="eta_0"
         and rb["same_space_norms"]==["complete_A_sigma","complete_H0_sigma","ordinary_L2"]
         and rb["Sobolev_norm"]=="sum_j (1+16j^2)^s exp(8|j|sigma) |fhat_j|^2",
         "whole original real member and all stated source spaces")

 domain=inventory["exact_domain_and_normalization"]
 roots=tuple(map(Fraction,domain["exact_root_interval"]))
 cut=Fraction(domain["c_body"]);radius=Fraction(domain["original_outer_radial_radius"])
 inner=Fraction(domain["original_inner_radial_radius"])
 delta=Fraction(domain["direction_radius"]);width=Fraction(domain["original_moving_Wiener_strip"])
 piece=domain["candidate_piece"];cubic=admitted["cubic"]
 rectangle=tuple(map(Fraction,germ["complex_radial_rectangle"]["real_interval"]))
 cell=tuple(map(Fraction,germ["exact_candidate_piece_interval"]))
 scalar_cell=tuple(map(Fraction,germ["original_scalar_germ"]))
 require(piece==2549 and germ["actual_candidate_piece"]==piece
         and rb["exact_candidate_and_response_piece"]==piece
         and roots==tuple(map(Fraction,germ["root_interval"]))
             ==tuple(map(Fraction,rb["exact_root_interval"]))
             ==tuple(map(Fraction,admitted["literals"]["rstar_interval"]))
         and cut==Fraction(admitted["literals"]["c_body"])
         and len(cubic.nodes)==6145
         and cell==(cubic.nodes[piece],cubic.nodes[piece+1])
             ==tuple(map(Fraction,rb["exact_piece_interval"]))
         and rb["original_response_shard_range"]==[2265,2718]
         and rb["original_response_local_piece"]==284,
         "same true root, exact candidate/response piece and full original intervals")
 require(radius==Fraction(1,100000) and inner==Fraction(1,200000)
         and delta==Fraction(1,100000000) and width==Fraction(1,1024)
         and Fraction(germ["complex_radial_radius"])==radius
         and Fraction(germ["complex_radial_rectangle"]["imaginary_half_width"])==radius
         and Fraction(rb["exact_outer_radial_radius"])==radius
         and Fraction(rb["exact_inner_radial_radius"])==inner
         and Fraction(rb["exact_complex_parameter_radius"])==delta
         and Fraction(germ["moving_phi_strip"])==Fraction(rb["exact_moving_Wiener_strip"])==width
         and rb["exact_radial_rectangle"]==germ["complex_radial_rectangle"]
         and rectangle==(roots[0]-radius,roots[1]+radius)
         and cell[0]<rectangle[0]<roots[0]<roots[1]<cut<rectangle[1]<cell[1]
         and scalar_cell[0]<rectangle[0]<rectangle[1]<scalar_cell[1]
         and rectangle[0]>Fraction(9,50)
         and cut-roots[0]<=Fraction(domain["maximum_collar_length"])==Fraction(9,1000000),
         "whole outer value rectangle covers the real collar; inner derivative disk is not widened")
 offsets=rb["exact_background_root_offsets"]
 repair_piece=repair["special_piece_offsets"][str(piece)]
 require(isinstance(offsets,list) and len(offsets)==65
         and all(isinstance(value,str) and value.isascii() and len(value)<=4096
                 for value in offsets)
         and offsets==repair_piece["physical_offset"]
         and tuple(map(Fraction,repair_piece["interval"]))==cell,
         "all65 original signed physical offsets, no second alpha scaling")
 for value in offsets:
  Fraction(value)
 intrinsic=germ["complex_intrinsic_coefficients"]
 require(set(intrinsic)==set(INTRINSIC_NAMES) and len(intrinsic)==13,
         "all thirteen complete signed intrinsic coefficient records")
 for name in INTRINSIC_NAMES:
  _complex_record(intrinsic[name],core,"germ/intrinsic/"+name)
 for name in ("moving_mean_v","moving_mean_v_radial"):
  _complex_record(germ[name],core,"germ/"+name)
 for name in ("moving_U_derivative_Astrip","moving_v_derivative_Astrip",
              "physical_U_derivative_sup","physical_v_derivative_sup"):
  _array_records(germ[name],5,core,"germ/"+name)
 for name in ("response_raw_complete_coefficient_upper",
              "response_repaired_complete_coefficient_upper"):
  _array_records(rb[name],193,core,"root budget/"+name)
 for name in ("direction_angular_norms_u","direction_angular_norms_v",
              "background_repair_angular_norms_u","background_repair_angular_norms_v",
              "full_family_U_angular_norms","full_family_V_angular_norms"):
  _array_records(rb[name],5,core,"root budget/"+name)
 _array_records(rb["L_derivative_commutator_bounds"],4,core,"root budget/L")
 _array_records(rb["integer_derivative_recursion"],5,core,"root budget/integer recursion")
 require(set(rb["integer_one_gain_Sobolev_bounds"])==set(map(str,range(4)))
         and set(rb["inverse_radial_derivative_integer_one_gain_inner_disk"])==set(map(str,range(4)))
         and set(rb["fractional_one_gain_Sobolev_bounds"])==
          {"Hminus5over3_to_Hminus2over3","Hminus3over2_to_Hminus1over2","Hminus2over3_to_Hplus1over3"}
         and set(rb["complete_lower_operators"])=={"E","B","C_plus_eta_partial","b2","b1"}
         and set(rb["complete_independent_mean_row"])==
          {"z_reaction","h1_functional","f_functional","ordinary_g2_mean"},
         "complete original inverse windows, lower operators and independent mean")
 for name in ("full_complex_mean_abs_lower","full_complex_mean_abs_upper",
              "gamma_abs_lower","gamma_abs_upper","beta_abs_upper","K_abs_upper"):
  core.intrinsic_record(rb[name],"original complete family/"+name)
 optical={name:collar_process["fresh_coefficient_bounds"][name] for name in
          ("optical_speed_lower","optical_speed_upper")}
 for name,value in optical.items():
  core.record(value,"original actual full-family optical speed/"+name)
 require(collar_manifest["mathematical_parameters"]["complete_head_dimension"]==193
         and collar_manifest["mathematical_parameters"]["full_operator_band"]==192
         and collar_manifest["mathematical_parameters"]["first_high_index"]==97
         and collar_manifest["mathematical_parameters"]["root_piece"]==2549
         and collar_process["uniform_positive_extension_reference"]["speed_on_actual_root"]==
             "full-family -gamma*mean(v)",
         "the optical speed belongs to the same complete original family and head")
 contexts=[]
 for spec,value,path in (
   (specs[0],germ,[]),(specs[1],rb,[]),
   (specs[0],germ,["complex_intrinsic_coefficients"]),
   (specs[0],germ,["moving_mean_v"]),
   (specs[1],rb,["exact_background_root_offsets"]),
   (specs[1],rb,["response_repaired_complete_coefficient_upper"])):
  contexts.append(_complete_context(spec,value,path,core))
 for name in ("direction_angular_norms_u","direction_angular_norms_v",
              "full_family_U_angular_norms","full_family_V_angular_norms",
              "full_complex_mean_abs_lower","full_complex_mean_abs_upper"):
  contexts.append(_complete_context(specs[1],rb,[name],core))
 for name in optical:
  contexts.append(_complete_context(by_role["collar_process"],collar_process,["fresh_coefficient_bounds",name],core))
 contexts.append(_complete_context(manifest["historical_inputs"][18],repair,
                                  ["special_piece_offsets",str(piece)],core))
 admitted.update(germ=germ,rb=rb,collar_process=collar_process,
  original_optical_records=optical,collar_original_contexts=contexts,
  collar_native_identities=[germ_identity,rb_identity])
 admitted["collar_native_shape_summary"]={
  "complete_germ_fields":len(germ),"complete_root_budget_fields":len(rb),
  "complete_signed_intrinsic_records":13,"complete_exact_signed_offsets":65,
  "complete_response_upper_records":193,"complete_raw_response_upper_records":193,
  "complete_original_angular_arrays":6,"complete_original_angular_array_length":5,
  "germ_record5_leaf_count":germ_record_count,"root_budget_record5_leaf_count":rb_record_count,
  "all_complete_record5_leaves_checked":True,"diagnostic_numbers_not_used_as_bounds":True,
  "all_original_real_complex_and_inner_radius_scopes_retained":True,
  "actual_eta_two_original_records_read_without_recomputation":True,
  "original_native_sources_imported_or_called":0,
 }
 return admitted


def admit(repo,manifest_path,manifest_sha,native_path,receipts_path,
          candidate_path,repair_path,root_germ_path,root_budget_path,core):
 """Complete pure admission before the owner imports flint or starts a target."""
 require=core.require
 require(os.environ.get("GITHUB_ACTIONS")=="true"
         and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
         "own public repository Actions only")
 require("flint" not in sys.modules,"all original admission precedes flint")
 repo=Path(repo).resolve()
 manifest_raw=Path(manifest_path).read_bytes()
 require(0<len(manifest_raw)<100000 and core.digest(manifest_raw)==manifest_sha,
         "complete fixed current manifest bytes")
 manifest=core.data(manifest_raw)
 require(manifest["kind"]==MANIFEST_KIND and manifest["problem_id"]==PROBLEM_ID
         and manifest["repository"]==REPOSITORY
         and isinstance(manifest["parameters"],dict),
         "one fixed complete W2C candidate manifest")
 parameters=manifest["parameters"]
 require(set(PARAMETER_GUARDS)<=set(parameters)
         and core.canonical({key:parameters[key] for key in PARAMETER_GUARDS})==
             core.canonical(PARAMETER_GUARDS),
         "all actual spaces, fixed WVC reference, complete50 targets and original scopes")
 specs=manifest["files"]
 require(isinstance(specs,list) and len(specs)==manifest["expected_current_input_count"]
         and len({item["role"] for item in specs})==len(specs)
         and len({item["path"] for item in specs})==len(specs),
         "all declared current files, unique roles and paths")
 by_role={spec["role"]:spec for spec in specs}
 texts={spec["role"]:core.read_spec(repo,spec) for spec in specs}
 modules=manifest["scientific_modules"]
 require(isinstance(modules,list)
         and tuple(spec["role"] for spec in modules)==NEW_MODULE_ROLES
         and all(by_role[spec["role"]]==spec for spec in modules),
         "exact seven new pure-reader/scientific modules")
 require(Path(core.__file__).resolve()==(repo/by_role["readonly_core"]["path"]).resolve()
         and Path(__file__).resolve()==(repo/by_role["readonly_admission"]["path"]).resolve(),
         "the loaded pure readers are the fully pinned current files")
 required=set(NEW_MODULE_ROLES)|set(ORIGINAL_DEFINITION_ROLES)|{
   "worker","rules","inventory","WHV_readonly_inventory","W2C_input_inventory"}
 required|=set(COMPLETED_TRACE_PINS)|set(COLLAR_CURRENT_PINS)|set(NEW_PROOF_PINS)
 require(required<=set(by_role),"entire complete current original/new closure")
 require(by_role["W2C_input_inventory"]==W2C_INVENTORY_PIN
         and manifest["collar_input_inventory"]==W2C_INVENTORY_PIN,
         "fixed full source-derived W2CI inventory")
 for role,spec in {**COLLAR_CURRENT_PINS,**NEW_PROOF_PINS}.items():
  require(by_role[role]==spec,"complete fixed collar original/proof input "+role)
 require(manifest["collar_contract"]==NEW_PROOF_PINS["proof_W2C"]
         and manifest["joint_kernel_contract"]==NEW_PROOF_PINS["proof_WJK"],
         "both complete mathematical contracts")
 for key,role in (
    ("completed_tracefree_scientific_input","WVC_actual"),
    ("completed_tracefree_execution_input","WVC_execution"),
    ("completed_tracefree_manifest_input","WVC_manifest")):
  require(manifest[key]==by_role[role]==COMPLETED_TRACE_PINS[role],
          "same complete frozen WVC provider "+role)
 inventory=core.data(texts["W2C_input_inventory"])
 require(inventory["repository"]==REPOSITORY
         and inventory["mathematical_candidate"]=={
          key:NEW_PROOF_PINS["proof_W2C"][key] for key in ("path","bytes","sha256","git_blob_sha")}
         and inventory["fixed_same_operator_provider"]["manifest"]=={
          key:COMPLETED_TRACE_PINS["WVC_manifest"][key] for key in ("path","bytes","sha256","git_blob_sha")},
         "W2CI complete original provider and mathematical identity")
 historical=manifest["historical_inputs"]
 expected_historical=(inventory["preexisting_WVC_historical_inputs_retained"]
                      +inventory["two_additional_native_restorations"])
 require(isinstance(historical,list) and historical==expected_historical
         and len(historical)==21 and len({item["role"] for item in historical})==21
         and len({item["path"] for item in historical})==21
         and historical[19:]==ADDITIONAL_HISTORICAL_INPUTS,
         "complete nineteen original objects plus exactly two original collar natives")
 ast.parse(texts["worker"])
 receipt_raw=Path(receipts_path).read_bytes()
 receipt=core.data(receipt_raw)
 receipt_keys={"kind","original_WVC_restoration","additional_historical_inputs",
  "historical_input_count","old_producers_executed","original_repairs_regenerated",
  "new_artifacts","new_arrays_published"}
 require(isinstance(receipt,dict) and set(receipt)==receipt_keys
         and receipt["kind"]=="complete_W2C_readonly_restoration_v1"
         and type(receipt["historical_input_count"]) is int
         and receipt["historical_input_count"]==21,
         "one complete readonly restoration extension with the original object intact")
 for key in ("old_producers_executed","original_repairs_regenerated",
             "new_artifacts","new_arrays_published"):
  require(type(receipt[key]) is int and receipt[key]==0,
          "no old producer, repair regeneration, arrays or artifacts")
 original=receipt["original_WVC_restoration"]
 original_raw=core.canonical(original)
 require(len(original_raw)==ORIGINAL_RESTORATION_IDENTITY["bytes"]
         and core.digest(original_raw)==ORIGINAL_RESTORATION_IDENTITY["sha256"]
         and len(original["historical_inputs"])==19,
         "verbatim complete13771-byte original WVC restoration object")
 added=receipt["additional_historical_inputs"]
 require(isinstance(added,list) and len(added)==2,"both additional original restoration receipts")
 for spec,item in zip(ADDITIONAL_HISTORICAL_INPUTS,added):
  extra={"git_tree_blob_and_size_verified","compressed_sha256_verified",
         "identical_original_bytes_materialized"}
  require(isinstance(item,dict) and set(item)==set(spec)|extra
          and {key:item[key] for key in spec}==spec
          and all(item[key] is True for key in extra),
          "complete original added native receipt "+spec["role"])
 all_restored=original["historical_inputs"]+added
 for spec,item in zip(historical,all_restored):
  require({key:item[key] for key in spec}==spec,"whole21 input map agrees with fixed manifest")
 admitted=core.admit_original_closure(
  manifest,texts,by_role,native_path,original,candidate_path,repair_path,
  ORIGINAL_DEFINITION_ROLES)
 admitted["W2CI"]=inventory
 admitted["completed_tracefree_inputs"]=admit_completed_tracefree_inputs(
  admitted,texts,by_role,core)
 old_candidate=admitted["completed_tracefree_inputs"]["complete_original_candidate"]
 require(original==old_candidate["complete_restoration_receipts"],
         "restoration object is exactly the completed same-operator WVC object")
 admit_collar_natives(admitted,texts,by_role,root_germ_path,root_budget_path,core)
 core_summary=dict(admitted["admission"])
 admitted["original_closure_admission"]=core_summary
 admitted["original_completed_WVC_admission"]=old_candidate["original_admission"]
 summary=dict(core_summary)
 summary.update(
  checks=core_summary["checks"]+[{"name":name,"passed":True} for name in COLLAR_CHECKS],
  current_file_count=len(specs),historical_input_count=len(all_restored),
  original_historical_input_count=19,additional_historical_input_count=2,
  new_source_AST_count=len(modules),old_source_AST_count=len(ORIGINAL_DEFINITION_ROLES),
  source_AST_count=len(modules)+len(ORIGINAL_DEFINITION_ROLES),
  worker_AST_count=1,execution_AST_count=len(modules)+len(ORIGINAL_DEFINITION_ROLES)+1,
  restoration_receipts_bytes=len(receipt_raw),restoration_receipts_sha256=core.digest(receipt_raw),
  original_WVC_restoration_identity=ORIGINAL_RESTORATION_IDENTITY,
  complete_original_WVC_scientific_fields=len(COMPLETED_TRACE_FIELD_IDENTITIES),
  complete_original_WVC_execution_fields=len(COMPLETED_TRACE_EXECUTION_FIELD_IDENTITIES),
  complete_original_WVC_saved_records=56,complete_original_WVC_modal_prefix_records=5,
  complete_same_operator_record_copies=29,complete_original_optical_records=2,
  original_finite_gate_passed=False,original_conditional_finite_inverse=None,
  collar_native_shape=admitted["collar_native_shape_summary"],
  all_current_and_native_inputs_verified_before_science=True,
  original_native_sources_imported_or_called=0,
  flint_imported=False)
 admitted.update(
  admission=summary,complete_restoration_receipts=receipt,
  complete_restored_input_map=all_restored,
  same_operator_records=admitted["completed_tracefree_inputs"]["copied_records"],
  current_receipts=specs,scientific_modules=modules,
  current_manifest_sha256=manifest_sha)
 require("flint" not in sys.modules,"complete pure readonly admission remains numerical-library-free")
 admitted["collar_inputs_verified"]=True
 return admitted
