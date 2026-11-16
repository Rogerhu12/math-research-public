"""WSMF52: one public child, three complete natural conclusions, no old target rerun."""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import importlib.util
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
SOURCE_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_per_index_strict_flux_mean_science.py"''')
WORKER_PATH = json.loads(r'''"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py"''')
KIND = json.loads(r'''"complete_per_index_strict_flux_and_same_physical_mean_refinement"''')
PROBLEM_ID = json.loads(r'''"same_selected_per_index_strict_flux_complete_mean52_v1"''')
PREFLIGHT_KIND = json.loads(r'''"per_index_strict_flux_complete_mean_readonly_preflight"''')
MAX_SCIENCE_BYTES = json.loads(r'''85000''')
DIAGNOSTIC_TYPE_BYTES = json.loads(r'''64''')
DIAGNOSTIC_MESSAGE_BYTES = json.loads(r'''1024''')
DIAGNOSTIC_TRACEBACK_BYTES = json.loads(r'''4096''')
EXPECTED_FIXED_FILES = json.loads(r'''[{"bytes":72251,"git_blob_sha":"32ff92c516fcc5c43f3619930d4845d294289270","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json","role":"wgs_main","sha256":"8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"},{"bytes":31632,"git_blob_sha":"d6d13860e322d82ce354c8c0d0eb0f279ca63b3c","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json","role":"wgs_copies","sha256":"3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66"},{"bytes":59417,"git_blob_sha":"df5ea6fff610d70ad98fbebc9dd004d24388ce86","path":"topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json","role":"wbf","sha256":"87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0"},{"bytes":69002,"git_blob_sha":"80499e42f643e607db47c973b54f2243629a05e8","path":"topics/visible-flex-exact-nearby/notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json","role":"wjr","sha256":"806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660"},{"bytes":47714,"git_blob_sha":"67c7070e6678223b5de63635d4b18f110500a742","path":"topics/visible-flex-exact-nearby/notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json","role":"wdg","sha256":"04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395"},{"bytes":12958,"git_blob_sha":"c5d9166b914a17136c5058b3d213afc4dffad5c0","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extension_scalars.json","role":"extension","sha256":"5816db201af6f0da0f7412c1a1fe0f1521d5425debf37693ab652f152e7fec00"},{"bytes":90421,"git_blob_sha":"edd66cdbe7a438569524ba2614d3822f61de5c81","path":"topics/visible-flex-exact-nearby/notes/strict_flux_mean_forcing_ci/run-43856579962-1/actual-scientific-conclusion.json","role":"wmt","sha256":"c6680025917247e7bec958851d5ee85fc3c3750b059372a87ec568cd9d8acbd4"},{"bytes":82508,"git_blob_sha":"146904d030cca0887fae921084396bf4008d0281","path":"topics/visible-flex-exact-nearby/notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json","role":"wrp","sha256":"4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee"},{"bytes":47019,"git_blob_sha":"d1019046eaa2087354d3ab9feb901f72f023aa48","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_per_index_strict_flux_mean_math.py","role":"math","sha256":"a483bce9ad56bff6d89401e88c225db65b2f64e000fabd8248628eed0911b86f"},{"bytes":36418,"git_blob_sha":"f808c0b5966bcb9728603dd808dad904873123e8","path":"topics/visible-flex-exact-nearby/results/R133-supplement-per-index-strict-flux-and-complete-physical-mean-bound.md","role":"proof_WSMF","sha256":"5845b88028b384356f53535353559bdfa15691a1bf7e019fe39d42538643a803"},{"bytes":26542,"git_blob_sha":"c410f91faae59dac177b737faffe4dd11d3f2d46","path":"topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_relative_phase_pullback_public_worker.py","role":"worker","sha256":"3770e29dbb2becd615227c1ceceaf7c9a34cf585a705deeed75465dc02594d8e"},{"bytes":2461,"git_blob_sha":"5c5d020913d717bb5bc8ce891297e00eaa8944f7","path":"topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json","role":"rules","sha256":"65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1"}]''')
EXPECTED_OLD_FILES = json.loads(r'''[{"bytes":72251,"git_blob_sha":"32ff92c516fcc5c43f3619930d4845d294289270","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json","role":"wgs_main","sha256":"8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e"},{"bytes":31632,"git_blob_sha":"d6d13860e322d82ce354c8c0d0eb0f279ca63b3c","path":"topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json","role":"wgs_copies","sha256":"3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66"},{"bytes":59417,"git_blob_sha":"df5ea6fff610d70ad98fbebc9dd004d24388ce86","path":"topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json","role":"wbf","sha256":"87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0"},{"bytes":69002,"git_blob_sha":"80499e42f643e607db47c973b54f2243629a05e8","path":"topics/visible-flex-exact-nearby/notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json","role":"wjr","sha256":"806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660"},{"bytes":47714,"git_blob_sha":"67c7070e6678223b5de63635d4b18f110500a742","path":"topics/visible-flex-exact-nearby/notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json","role":"wdg","sha256":"04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395"},{"bytes":12958,"git_blob_sha":"c5d9166b914a17136c5058b3d213afc4dffad5c0","path":"topics/visible-flex-exact-nearby/notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/extension_scalars.json","role":"extension","sha256":"5816db201af6f0da0f7412c1a1fe0f1521d5425debf37693ab652f152e7fec00"},{"bytes":90421,"git_blob_sha":"edd66cdbe7a438569524ba2614d3822f61de5c81","path":"topics/visible-flex-exact-nearby/notes/strict_flux_mean_forcing_ci/run-43856579962-1/actual-scientific-conclusion.json","role":"wmt","sha256":"c6680025917247e7bec958851d5ee85fc3c3750b059372a87ec568cd9d8acbd4"},{"bytes":82508,"git_blob_sha":"146904d030cca0887fae921084396bf4008d0281","path":"topics/visible-flex-exact-nearby/notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json","role":"wrp","sha256":"4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee"}]''')
OLD_CONTRACTS = json.loads(r'''{"extension":{"complete_non_ball_qualification_projection":{"bytes":2877,"sha256":"8b281728f9980c04b980dee09e9961870557e6c28da7c012870fa9030013f6c8"},"complete_schema_fields":["all_printed_records_in_complete_conclusion","automatic_retry_authorized","binding","complete","conclusion","failure","kind","node_name","printed_record_event_count"]},"wbf":{"complete_non_ball_qualification_projection":{"bytes":48051,"sha256":"ff802e2cf611fc467dd27ec7177929b693856706c88e040647e3e5ec54f2059e"},"complete_schema_fields":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"]},"wdg":{"complete_non_ball_qualification_projection":{"bytes":36446,"sha256":"872e3674a5e33246dd647a6275233cce0ef610517a6042e530ae7ccfb6c63de5"},"complete_schema_fields":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"]},"wgs_copies":{"complete_non_ball_qualification_projection":{"bytes":16834,"sha256":"f238e7927c3ae85d8327a648f3d7e3ab87f9aee80549cb0183f410bce751e0dd"},"complete_schema_fields":["actual_scientific_checkout_commit","complete","complete_readonly_input_projection","copied_complete_local_coefficients","copied_complete_local_coefficients_sha256","copied_complete_original_scopes","copied_complete_original_scopes_sha256","copied_original_scalar_records","copied_original_scalar_records_sha256","copied_original_stage_records","copied_original_stage_records_sha256","copy_counts","input_manifest_sha256","kind","local_coefficient_qualification","math_module_sha256","original_input_sha256","public_repository","run_attempt","run_id","source_sha256","workflow_event_commit"]},"wgs_main":{"complete_non_ball_qualification_projection":{"bytes":30020,"sha256":"6eb0a4794cd3c47b482c80d6a32179a0ed50cd48ca5d71d50ffda14f8622e15e"},"complete_schema_fields":["accepted_original_inputs","actual_mathematical_wall_seconds","actual_progress","actual_returncode","actual_scientific_checkout_commit","arithmetic_bits","complete","complete_derivative_request_certificate","complete_free_first_transport_conclusion","complete_higher_flow_and_cut_conclusion","complete_local_regular_packet_conclusion","complete_named_global_graph_conclusion","complete_original_inputs_file","complete_strict_coefficient_conclusion","complete_strict_forcing_conclusion","complete_strict_geometry_conclusion","complete_strict_leading_conclusion","failure","gates","input_manifest_sha256","input_sha256","kind","math_module_sha256","original_source_AST_evidence","parameters","planned_shape","proved","public_repository","retained_scope","run_attempt","run_id","runtime","source_sha256","stage","verified_original_inputs","workflow_event_commit"]},"wjr":{"complete_non_ball_qualification_projection":{"bytes":59291,"sha256":"f3f92df917ea429cc6cbdbb37da132e9f4e1fdea6a8f94786b1389e4991ad4df"},"complete_schema_fields":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","workflow_event_commit"]},"wmt":{"complete_non_ball_qualification_projection":{"bytes":57703,"sha256":"53b4ec258b7d8b2e56a8523c89907800b7c92fe58c18fbace46e62b5e35425db"},"complete_schema_fields":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"]},"wrp":{"complete_non_ball_qualification_projection":{"bytes":73852,"sha256":"f8d61ebe55f4ce10f94b9bd1b35e4d74eb208e493aa83291202da86506862971"},"complete_schema_fields":["accepted_old_inputs","actual_checkout_commit","actual_mathematical_wall_seconds","actual_progress","actual_returncode","arithmetic_bits","automatic_retry_authorized","complete","complete_new_graphs","completed_targets","copied_original_scalar_records","copied_original_scopes","current_target","failure","gates","input_sha256","kind","manifest_sha256","original_source_AST_evidence","parameters","problem_id","proved","retained_scope","run_attempt","run_id","runtime","saved_record_counts","scientific_modules","stage","verified_original_inputs","whole_candidate_choices","workflow_event_commit"]}}''')
COMPLETE_CONTEXT_REFERENCES = json.loads(r'''[{"bytes":1588,"complete_object":true,"json_path":["parameters"],"role":"wgs_main","sha256":"28a16f7541f4d12745da430ceea91081e52c63fd3a8df7ddd530499b49f0a92a"},{"bytes":1019,"complete_object":true,"json_path":["retained_scope"],"role":"wgs_main","sha256":"d48ebcc87d006935c2e1c42593911645f42e1c01a7b88307772f0855f2aaedd8"},{"bytes":7395,"complete_object":true,"json_path":["accepted_original_inputs"],"role":"wgs_main","sha256":"de1bc28168af793047cccbeeb5186296f737c8fdf2ecfb05c2a1f9eae3aeb633"},{"bytes":1569,"complete_object":true,"json_path":["complete_derivative_request_certificate"],"role":"wgs_main","sha256":"1a15e3f5ad303a74547548a2a00cfa8913bb313b0e18dc0c66a600d03619d8cc"},{"bytes":4326,"complete_object":true,"json_path":["complete_higher_flow_and_cut_conclusion"],"role":"wgs_main","sha256":"290f908ebb43d0fbfe6ed5e01ab11ac67e144c90ebe474d7778f7457c8da74d8"},{"bytes":3129,"complete_object":true,"json_path":["complete_strict_coefficient_conclusion"],"role":"wgs_main","sha256":"e27177b7b0434e7b7402698518ef02201163b945b88a639caf13fbf9a758fd29"},{"bytes":10833,"complete_object":true,"json_path":["complete_strict_geometry_conclusion"],"role":"wgs_main","sha256":"0a1f1fadea01280a1c86680b20e0121c54b0279702ace4c950a9ce25ed12b801"},{"bytes":4552,"complete_object":true,"json_path":["complete_strict_leading_conclusion"],"role":"wgs_main","sha256":"d52f577a6ef3048a4aa53dea36e6c8f1653baf95773d49e5dbc5d0670ea7b0f4"},{"bytes":9604,"complete_object":true,"json_path":["complete_strict_forcing_conclusion"],"role":"wgs_main","sha256":"de68f9105da13db7118b1dd7a967ed26b4fdafbc45c81197dedd893fac4b1a25"},{"bytes":5041,"complete_object":true,"json_path":["complete_free_first_transport_conclusion"],"role":"wgs_main","sha256":"17c56dcc2331079071b68b0ceaa0c78a2b4a2a1acecdd2f8a10155281151c7be"},{"bytes":135,"complete_object":true,"json_path":["complete_original_inputs_file"],"role":"wgs_main","sha256":"dac6158b8ba85b1487db43c6c56a1ae27c4d4c411dac6ff4b4417ae148e89f71"},{"bytes":5818,"complete_object":true,"json_path":["copied_original_scalar_records"],"role":"wgs_copies","sha256":"5aa27845005a14774eaa4c3d01509dcd8e8869d6b1e2e7a0f588f346487e608e"},{"bytes":4119,"complete_object":true,"json_path":["copied_original_stage_records"],"role":"wgs_copies","sha256":"8275740bbad09715144bfa7211f0e4e2e77bcb0bce89d408933d648c701eb4e5"},{"bytes":11520,"complete_object":true,"json_path":["copied_complete_original_scopes"],"role":"wgs_copies","sha256":"986561d54c780e1ff9d121110e473594aac8f96cd36552fc7b85d9d657a0cd2f"},{"bytes":1172,"complete_object":true,"json_path":["local_coefficient_qualification"],"role":"wgs_copies","sha256":"74d068564636a9a8635a30aa3931a186582330caaa7b14eed16ac495a210bebd"},{"bytes":5,"complete_object":true,"json_path":["complete_readonly_input_projection"],"role":"wgs_copies","sha256":"a17fcf0a2f50e2d495e4f90ce263410edc183add6c62699a2facbccf60410f74"},{"bytes":1620,"complete_object":true,"json_path":["parameters"],"role":"wbf","sha256":"11d4b48591444e5a1622df6efeaa027477e1d7a8b1a1ec49d70a24311c271f2d"},{"bytes":1807,"complete_object":true,"json_path":["retained_scope"],"role":"wbf","sha256":"b21b09c1d58aabc0c40f0e6b76638ad271f4f4c229c5fa4aee775f836aa2b578"},{"bytes":15709,"complete_object":true,"json_path":["accepted_old_inputs"],"role":"wbf","sha256":"4ef523df6fd6f1a275fcf0399ae90ee51da2d4b23f1a0d7ad4a8f278a525a558"},{"bytes":21153,"complete_object":true,"json_path":["copied_original_scopes"],"role":"wbf","sha256":"e5d8a593d9a29998d4c1bb96165b1098225f3f7d145b44489f8d7d4857d00d2a"},{"bytes":3847,"complete_object":true,"json_path":["copied_original_scalar_records"],"role":"wbf","sha256":"bc53ed42da3d2c81c70903c0517e9d4d39fd49ed99de590044b35d09bb62e65e"},{"bytes":1804,"complete_object":true,"json_path":["complete_new_graphs","complete_new_sharp_flow_conclusion"],"role":"wbf","sha256":"2ee4db432c37b396703fe06900270b68b8176551a703025e2bbc4c2f4178eed3"},{"bytes":1684,"complete_object":true,"json_path":["parameters"],"role":"wjr","sha256":"3c5e0f395ddc454ab87e5682767e34bd0f9a1c055b20fd726f2224f7796624b0"},{"bytes":1939,"complete_object":true,"json_path":["retained_scope"],"role":"wjr","sha256":"1479231e0ee2cd93fb2d02afe2d2578ea2477baa7c89902a0f307b27b33020c1"},{"bytes":20412,"complete_object":true,"json_path":["accepted_old_inputs"],"role":"wjr","sha256":"5e1d7dbe6ec66c06e8b2974e90f08c8229f38336c16b8d33625e35057b178b27"},{"bytes":27960,"complete_object":true,"json_path":["copied_original_scopes"],"role":"wjr","sha256":"ca0833a5d3dfe73575e871c607d2f6435824e12a4ee360f17ae3f101690143d4"},{"bytes":1904,"complete_object":true,"json_path":["complete_new_graphs","complete_new_positive_phase_average_ratio_conclusion"],"role":"wjr","sha256":"f16cbf96c6ccb9be4818030928b55bc20d0f8f46020bb6121d6caf481397468e"},{"bytes":1896,"complete_object":true,"json_path":["complete_new_graphs","complete_new_relative_omega_conclusion"],"role":"wjr","sha256":"7908337afd387bc33f0679aed5092e1ebf29b03ff71f214544c617384414426d"},{"bytes":1366,"complete_object":true,"json_path":["parameters"],"role":"wdg","sha256":"60258aed756b9736f90787d90800f0a06d4c56cca50ce231ed4ee1be1211a14c"},{"bytes":1415,"complete_object":true,"json_path":["retained_scope"],"role":"wdg","sha256":"d7ab85acc73244a7606ec3322446147d388d3ebbc9bbfa00daf063c7b5b6eb5c"},{"bytes":10763,"complete_object":true,"json_path":["accepted_old_inputs"],"role":"wdg","sha256":"59ca5d725035887f3c8cce9860adf992afdce766bb472e774692bf5b928b7368"},{"bytes":15638,"complete_object":true,"json_path":["copied_original_scopes"],"role":"wdg","sha256":"3d35f2addeadee0a70e8678f038835ec028dfc6f683f648d0cf7e961fc880c3a"},{"bytes":1370,"complete_object":true,"json_path":["complete_new_graphs","complete_new_cut_T_high_angular_conclusion"],"role":"wdg","sha256":"9d22c5430dbdcbb3884f5b9d0a398aa8946453103aa4974b88e151cd81307294"},{"bytes":1654,"complete_object":true,"json_path":["binding"],"role":"extension","sha256":"06e216c49daba70f3e5ba5e831426de1712b5385fa33747439292cad80ff9e85"},{"bytes":11061,"complete_object":true,"json_path":["conclusion"],"role":"extension","sha256":"0b1677340e2b90d6eb148134848e92ee374633a99a6715f403398a77584aeaa5"},{"bytes":1491,"complete_object":true,"json_path":["parameters"],"role":"wmt","sha256":"3853d382a0f684443daea7215075efe6e9cf07889454072ecb26c09911be7749"},{"bytes":1690,"complete_object":true,"json_path":["retained_scope"],"role":"wmt","sha256":"f3922e92a2db1fcacb3f12091bb9ba2001b9d85f8c9b01b36e4a5114b5bdf27f"},{"bytes":4900,"complete_object":true,"json_path":["accepted_old_inputs"],"role":"wmt","sha256":"1f5e3a84340dd79f8c52ef8fc5dcadfd040dbab86137c03c85595bd3bec6f821"},{"bytes":36676,"complete_object":true,"json_path":["copied_original_scopes"],"role":"wmt","sha256":"8a6d0d5c0230cb4f13c10f61403012f60feb542c6fe5be8c8a2ebd67c1355ad8"},{"bytes":15148,"complete_object":true,"json_path":["copied_original_scalar_records"],"role":"wmt","sha256":"a0fcd7b24cba3955336cf8b5b37de8ba83ecaadf0b7cc945bf78ef4699e3219d"},{"bytes":2964,"complete_object":true,"json_path":["complete_new_graphs","complete_normalized_weight_L1_kernels"],"role":"wmt","sha256":"c3efabe86c9ec92863d70c93089649204f81ae8e78493d8d32ff52d7c631a391"},{"bytes":1323,"complete_object":true,"json_path":["parameters"],"role":"wrp","sha256":"da62d81d93d41c5b421e922d86e0de3233cae86ac5ba1fce94cb40c542d513f8"},{"bytes":1978,"complete_object":true,"json_path":["retained_scope"],"role":"wrp","sha256":"899a69f512257ff9630d3161d53c07db751ab693f06db8ac54f8bcbf5c492e13"},{"bytes":11239,"complete_object":true,"json_path":["accepted_old_inputs"],"role":"wrp","sha256":"d1cf3cc5eea82af08e63064a982203a1fb35b0420ec7a9ea29924607e78ad38c"},{"bytes":43857,"complete_object":true,"json_path":["copied_original_scopes"],"role":"wrp","sha256":"9f3e9070c01ffd7682fb17841a962664cf8f28b2136c2525795367fa7a3898f2"},{"bytes":5452,"complete_object":true,"json_path":["copied_original_scalar_records"],"role":"wrp","sha256":"aa9086fce792a007eb09eb0a7a076364cb9dfe8f8506e97a68fc4b37bceed75b"},{"bytes":4947,"complete_object":true,"json_path":["complete_new_graphs","complete_new_same_whole_receiver_conclusion"],"role":"wrp","sha256":"98cdf407238e1511b3124738742e7cfcfff13c52d900c72c4e39de70812937c1"},{"bytes":1647,"complete_object":true,"json_path":["whole_candidate_choices"],"role":"wrp","sha256":"bef0c89b6635c4ebecd7b2302325c32f951c5435b0ef21ae9041f01a96b4384c"}]''')
PARAMETERS = json.loads(r'''{"arithmetic_bits":320,"complete_current_files":13,"complete_old_files":8,"decimal_record_digits":75,"fixed_intrinsic_eta0":"-7789843107295549/4611686018427387904","fixed_intrinsic_parameter":"eta_0","history_inputs":0,"immutable_AST_roles":["science","math","worker"],"input_order":[-4,3],"mean_source_unit":"n^(-23/6)","minimum_physical_frequency":388,"new_ODE_solutions":0,"new_exponentials":0,"new_first_forcing_angular":5,"new_first_forcing_radial":0,"new_graph_count":3,"new_graph_record_counts":[32,7,13],"new_leading_radial_order":2,"new_leading_total_order":7,"new_logarithms":0,"new_mean_steps":5,"new_quadratures":0,"new_record_count":52,"new_terminal_degrees":[0,1,2,3,4,5,6,7],"old_target_recomputations":0,"original_PW_cut":"2333968743003/10000000000000","original_record_copies_in_graphs":62,"original_true_interfaces":3070,"physical_frequency":"n=4|j|","physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","private_jets_are_complete_intermediates_not_new_public_certificates":true,"root_interval":["1191984371497/5000000000000","2383968743003/10000000000000"],"same_operator_domain":"Xfr -> P Fix(R_a), input H^(-4/3), output normalized physical L2 waist row","selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"],"upstream_new_record_copies_in_graphs":4}''')
RETAINED_SCOPE = json.loads(r'''{"all_five_mean_steps_and_terminal_degrees_0_through_7_retained":true,"all_four_waist_endpoints_retained":true,"complete_genuine_root_matrix_beta_n_and_two_reference_roles_retained":true,"complete_theta_forcing_and_second_order_drift_retained":true,"full_C_angular_order":6,"full_genuine_Vext_Bext_tail_and_extended_forcing_retained":true,"full_physical_Jr_and_Tk_fees_retained_readonly":true,"mean_source_unit":"n^(-23/6)","new_first_forcing_angular_order":5,"new_first_forcing_radial_order":0,"new_leading_radial_order":2,"new_leading_total_order":7,"no_first_amplitude_radial_derivative_needed_in_exact_flux":true,"no_new_signed_finite_inverse_or_smallness_claim":true,"no_radial_integration_by_parts":true,"no_saved_upper_subtraction":true,"old_local_mean_and_all_old_exponentials_readonly":true,"old_scientific_targets_recomputed":0,"ordinary_WJR_ratios_divided_by_factorial_once":true,"original_PW_cut":"2333968743003/10000000000000","original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","same_function_old_fallback_only_after_ordinary_conversion":true,"same_intrinsic_eta0":true,"same_positive_actual_phase_base_frozen_before_norm":true,"same_whole_and_reduced_compared_separately_old_wins_ties":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"]}''')
ORDERED_GRAPH_NAMES = json.loads(r'''["strict_per_index_flux_mean","complete_physical_mean_and_four_waist_endpoints","complete_current_negative_and_whole_receiver"]''')
NEW_RECORD_COUNTS = json.loads(r'''{"complete_current_negative_and_whole_receiver":13,"complete_physical_mean_and_four_waist_endpoints":7,"strict_per_index_flux_mean":32}''')
OLD_COPY_COUNTS = json.loads(r'''{"complete_current_negative_and_whole_receiver":24,"complete_physical_mean_and_four_waist_endpoints":12,"strict_per_index_flux_mean":26}''')
UPSTREAM_COPY_COUNTS = json.loads(r'''{"complete_current_negative_and_whole_receiver":3,"complete_physical_mean_and_four_waist_endpoints":1,"strict_per_index_flux_mean":0}''')
NEW_GRAPH_SHAPES = json.loads(r'''{"complete_current_negative_and_whole_receiver":{"Calg_only_in_whole_Dinfinity_only_in_reduced":true,"all_original_jumps_unchanged_and_no_jump_length_factor":true,"complete":true,"complete_current_provider_identity":{"bytes":82508,"git_blob_sha":"146904d030cca0887fae921084396bf4008d0281","path":"topics/visible-flex-exact-nearby/notes/relative_phase_pullback_receiver_ci/run-43881690924-1/actual-scientific-conclusion.json","role":"wrp","sha256":"4b66bd0ba1425c7a5a705cba3b32b07ea893643a7aa8cde1a720dcf450e852ee"},"complete_nonmean_and_terminal_bounds_readonly":true,"copied_original_records":{"new_collar_raw_mean_read_back":{"ball":"__READ_BACK_NEW_BALL__"},"new_four_waist_endpoints_read_back":{"ball":"__READ_BACK_NEW_BALL__"},"new_strict_primitive_mean_read_back":{"ball":"__READ_BACK_NEW_BALL__"},"provider_Bessel_prefactor":{"ball":"[4.32674871092222514696491493234032876517560776049805173263924858362506279049 +/- 8.2e-78]"},"provider_C_1":{"ball":"[191.8008246709565927797721403602769765475928447442644431106228330 +/- 1.50e-62]"},"provider_C_O":{"ball":"[144.1364251833792583628990099208150998341999763036812790334467110 +/- 4.93e-62]"},"provider_C_R":{"ball":"[2038.396873263098707542075374849093828633432756529021035448899354 +/- 3.80e-61]"},"provider_Calg":{"ball":"[21334995458.2617317922131025794903520236605002743919069185868910377932054395 +/- 3.53e-65]"},"provider_D_infinity":{"ball":"[2332847789.36260990230642073488324617852043430230187795053228301114686712271 +/- 3.40e-66]"},"provider_Lrec":{"ball":"[4181844.14552383297616163326915204219390193419381147548707743087111723866719 +/- 4.49e-70]"},"provider_N_minus4_3_upper":{"ball":"[0.000353365678957199556061688669104195383226755979071028582227403507686167109710 +/- 4.74e-79]"},"provider_N_minus5_3_upper":{"ball":"[4.84485135891744585521108222415284249996400645047740736779623648386625368160e-5 +/- 4.40e-80]"},"provider_RF":{"ball":"[2915432922793357.156724578277014851221391740910554139 +/- 4.68e-37]"},"provider_Rplus":{"ball":"[30660269163968914982109729435.4771319902267658817347810102235838415051898056 +/- 2.77e-47]"},"provider_complete_collar_B_union_upper":{"ball":"[8.42103831668428386668619632568159540924835998188047041329819847298842972045e+235 +/- 1.63e+160]"},"provider_complete_terminal_dyadic_contribution_upper":{"ball":"[8.00858488235437792087641489166750919537047231324830110312864496566935689806e+162 +/- 2.31e+86]"},"provider_dyadic_one_third":{"ball":"[0.225388660941768411848937895200456938979079214787810126918936162803929778332 +/- 4.14e-77]"},"provider_dyadic_two_thirds":{"ball":"[0.0242046948335741875508791270915959402605580106707967758571815970904235081019 +/- 3.78e-77]"},"provider_ell_minus_negative_fourth_upper":{"ball":"[3.76060309325562070733253499824415267217296755265025139066147752251855572103 +/- 4.55e-75]"},"provider_ell_plus_one_fourth_upper":{"ball":"[0.265914794847249430812512142890325807530086922385195453388784486346011606249 +/- 3.18e-76]"},"provider_jump_collar":{"ball":"[7.75606007655515967558999012405048857946293876810010816092847637407788647064e+232 +/- 2.41e+157]"},"provider_jump_strict":{"ball":"[4.64664255670958269813320581961296592311099446254379250546328736283910257886e+224 +/- 4.41e+149]"},"provider_prior_reduced":{"ball":"[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.26e+248]"},"provider_prior_whole":{"ball":"[1.90736423682251400641766771203225487061996663267347748430927102916501134114e+323 +/- 1.25e+248]"},"provider_sqrt_ell_plus_upper":{"ball":"[0.0707106781186547524400844362104849039284835937688474036588339868995366239231 +/- 5.37e-78]"},"provider_sqrt_two_upper":{"ball":"[1.41421356237309504880168872420969807856967187537694807317667973799073247846 +/- 2.11e-75]"},"provider_strict_B_t_upper":{"ball":"[9.10863193887094504525828961928644347593236785796418851203521546448110911151e+225 +/- 1.28e+150]"}},"full_finite_factors_Theta_nu_radial_head_and_physical_means_retained":true,"kind":"WSMF_complete_natural_conclusion_v1","new_records":{"complete_all_source_sum_upper":{"ball":"__NEW_BALL__"},"complete_collar_dyadic_contribution_upper":{"ball":"__NEW_BALL__"},"complete_collar_retained_and_mean_ordinary_upper":{"ball":"__NEW_BALL__"},"complete_collar_retained_mean_and_jumps_received_upper":{"ball":"__NEW_BALL__"},"complete_nonroot_source_sum_upper":{"ball":"__NEW_BALL__"},"complete_reduced_received_source_upper":{"ball":"__NEW_BALL__"},"complete_same_negative_error_upper":{"ball":"__NEW_BALL__"},"complete_same_reduced_error_upper":{"ball":"__NEW_BALL__"},"complete_same_whole_error_upper":{"ball":"__NEW_BALL__"},"complete_strict_dyadic_contribution_upper":{"ball":"__NEW_BALL__"},"complete_strict_retained_and_mean_ordinary_upper":{"ball":"__NEW_BALL__"},"complete_strict_retained_mean_and_jumps_received_upper":{"ball":"__NEW_BALL__"},"complete_whole_received_source_upper":{"ball":"__NEW_BALL__"}},"node_name":"complete_current_negative_and_whole_receiver","old_candidate_wins_equal_upper":true,"ordinary_dr_lengths_only_on_ordinary_sources":true,"original_PW_source_and_jump_windows_retained":true,"owner_selects_only_after_complete_whole_graph_is_saved":true,"retained_scope":{"all_five_mean_steps_and_terminal_degrees_0_through_7_retained":true,"all_four_waist_endpoints_retained":true,"complete_genuine_root_matrix_beta_n_and_two_reference_roles_retained":true,"complete_theta_forcing_and_second_order_drift_retained":true,"full_C_angular_order":6,"full_genuine_Vext_Bext_tail_and_extended_forcing_retained":true,"full_physical_Jr_and_Tk_fees_retained_readonly":true,"mean_source_unit":"n^(-23/6)","new_first_forcing_angular_order":5,"new_first_forcing_radial_order":0,"new_leading_radial_order":2,"new_leading_total_order":7,"no_first_amplitude_radial_derivative_needed_in_exact_flux":true,"no_new_signed_finite_inverse_or_smallness_claim":true,"no_radial_integration_by_parts":true,"no_saved_upper_subtraction":true,"old_local_mean_and_all_old_exponentials_readonly":true,"old_scientific_targets_recomputed":0,"ordinary_WJR_ratios_divided_by_factorial_once":true,"original_PW_cut":"2333968743003/10000000000000","original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","same_function_old_fallback_only_after_ordinary_conversion":true,"same_intrinsic_eta0":true,"same_positive_actual_phase_base_frozen_before_norm":true,"same_whole_and_reduced_compared_separately_old_wins_ties":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"]},"same_whole_and_reduced_operators_as_provider":true},"complete_physical_mean_and_four_waist_endpoints":{"both_physical_density_mean_entries_retained":true,"complete":true,"complete_absolute_coefficient_used_for_mean_derivative":true,"complete_old_local_mean_and_source_copied":true,"complete_old_signed_backward_propagator_copied":true,"copied_original_records":{"new_complete_strict_CF_read_back":{"ball":"__READ_BACK_NEW_BALL__"},"old_Xi23_6":{"ball":"[2.39769799982217740576863658335481859389778583215778169592617201148372665815e-6 +/- 1.81e-82]"},"old_endpoint_Vz":{"ball":"[1.95590426411866995809742937099340088436850766548469534971540963317442152996 +/- 2.36e-75]"},"old_endpoint_WT":{"ball":"[69921379092375833339684408785092371.4773038118509880012436242422241968903733 +/- 4.52e-41]"},"old_endpoint_scattering":{"ball":"[5.01186896474959310483349445702316092909219123272389014594669683111242862021e+295 +/- 2.46e+220]"},"old_endpoint_second_order":{"ball":"[1.21479593458586399022813399059257892311206844988741010382711283326304270477e+289 +/- 1.39e+214]"},"old_local_mean":{"ball":"[21276978686823711635921136703414754940920468769374081498449.0215928470113911 +/- 1.24e-17]"},"old_local_raw_mean_source":{"ball":"[17196770270310304726006150416412518704031614559213946096714538268.1614828764 +/- 1.45e-11]"},"old_strict_Ik":{"ball":"[39930460.6535024445947438687088821010485312127919253873667152035887545472461 +/- 4.18e-68]"},"old_strict_Tk":{"ball":"[290579920106504595416115.971373941173820363633327713312087338304975360978774 +/- 3.25e-52]"},"old_strict_absolute_coefficient":{"ball":"[98.3329487641492217749118930993115797456135524319806790033335403371386290730 +/- 4.95e-74]"},"old_strict_backward_factor":{"ball":"[62980217.5135088039076736593556811332831932928659867020838659113923402506100 +/- 1.76e-68]"},"old_strict_k0":{"ball":"[159721842.614009778378975474835528404194124851167701549466860814355018188984 +/- 2.33e-67]"}},"full_k_Jr_Tk_and_feedback_paid":true,"kind":"WSMF_complete_natural_conclusion_v1","new_records":{"complete_collar_raw_mean_union_upper":{"ball":"__NEW_BALL__"},"complete_physical_mean_endpoint_upper":{"ball":"__NEW_BALL__"},"complete_same_waist_endpoint_upper":{"ball":"__NEW_BALL__"},"complete_strict_mean_derivative_upper":{"ball":"__NEW_BALL__"},"complete_strict_mean_upper":{"ball":"__NEW_BALL__"},"complete_strict_primitive_mean_source_upper":{"ball":"__NEW_BALL__"},"complete_strict_raw_mean_source_upper":{"ball":"__NEW_BALL__"}},"node_name":"complete_physical_mean_and_four_waist_endpoints","physical_mean_source_unit":"n^(-23/6)","retained_scope":{"all_five_mean_steps_and_terminal_degrees_0_through_7_retained":true,"all_four_waist_endpoints_retained":true,"complete_genuine_root_matrix_beta_n_and_two_reference_roles_retained":true,"complete_theta_forcing_and_second_order_drift_retained":true,"full_C_angular_order":6,"full_genuine_Vext_Bext_tail_and_extended_forcing_retained":true,"full_physical_Jr_and_Tk_fees_retained_readonly":true,"mean_source_unit":"n^(-23/6)","new_first_forcing_angular_order":5,"new_first_forcing_radial_order":0,"new_leading_radial_order":2,"new_leading_total_order":7,"no_first_amplitude_radial_derivative_needed_in_exact_flux":true,"no_new_signed_finite_inverse_or_smallness_claim":true,"no_radial_integration_by_parts":true,"no_saved_upper_subtraction":true,"old_local_mean_and_all_old_exponentials_readonly":true,"old_scientific_targets_recomputed":0,"ordinary_WJR_ratios_divided_by_factorial_once":true,"original_PW_cut":"2333968743003/10000000000000","original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","same_function_old_fallback_only_after_ordinary_conversion":true,"same_intrinsic_eta0":true,"same_positive_actual_phase_base_frozen_before_norm":true,"same_whole_and_reduced_compared_separately_old_wins_ties":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"]},"same_original_four_endpoints":true,"same_true_root_initial_condition":"z_ph(r_star)=0","same_unit_as_original_complete_terminal_and_jumps":true},"strict_per_index_flux_mean":{"complete":true,"complete_flux_degrees":[0,1,2],"complete_inverse_step_count":5,"complete_private_demand":{"C_angular":6,"first_forcing_angular":5,"first_forcing_radial":0,"free_transport_angular":5,"leading_radial":2,"leading_total":7},"complete_terminal_degrees":[0,1,2,3,4,5,6,7],"copied_original_records":{"old_background_q0":{"ball":"[7.000000190000000000000000000000000000000000000 +/- 1e-50]"},"old_background_q1":{"ball":"[6.000000830000000000000000000000000000000000000 +/- 1e-50]"},"old_background_q2":{"ball":"[384.000159360000000000000000000000000000000000000005000000014507745775003149 +/- 7.14e-74]"},"old_background_q3":{"ball":"[16384.0203980800000000000000000000000000000000000001666666672250273061959214 +/- 4.09e-72]"},"old_background_q4":{"ball":"[1572865.95821568000000000000000000000000000000000001600000005360262139480845 +/- 4.01e-69]"},"old_background_q5":{"ball":"[120796105.590964224000000000000000000000000000000001228800004116681323121289 +/- 2.68e-67]"},"old_e_L1_q0":{"ball":"[15.5949375554430494640144665461121157323688969258589957323702100593313701569 +/- 3.12e-74]"},"old_e_L1_q1":{"ball":"[39.6962046865823077265822784810126582278481012658228982278514437873889422176 +/- 4.29e-74]"},"old_e_L1_q2":{"ball":"[503.291194851647783048140162430643688101265822784812957974920535894114214803 +/- 4.90e-73]"},"old_e_L1_q3":{"ball":"[5252.89560459010174557814061627015706735526129441509867139836257030128900606 +/- 7.99e-74]"},"old_e_L1_q4":{"ball":"[77678.9889726060930437766939324332762288788244963986430619094200357189566984 +/- 3.55e-71]"},"old_e_L1_q5":{"ball":"[2983986.82503725181208590298677601433592607306167458812174193700351032673642 +/- 2.36e-69]"},"old_e_L1_q6":{"ball":"[179697784.211916317134276508450984297494643046670511019260606848169365945006 +/- 4.25e-67]"},"old_kappa_L1_q0":{"ball":"[721.717814635178365757843764736400532686012780122927878242958984323376217547 +/- 3.59e-73]"},"old_p_L1_q0":{"ball":"[1.62025316455696202531645569620253164556962025316455696202531645569620253165 +/- 4.44e-75]"},"old_p_L1_q1":{"ball":"[39.6962046865823077265822784810126582278481012658228982278514437873889422176 +/- 4.22e-74]"},"old_p_L1_q2":{"ball":"[520.303855894685821610165478886339890632911392405066175190114663547668626975 +/- 1.50e-73]"},"old_p_L1_q3":{"ball":"[6266.36434371585224888287248151987088608943850960498426397319445756221724433 +/- 3.71e-72]"},"old_p_L1_q4":{"ball":"[118088.393566089769449972497818145539133166012094007187268167999119743658971 +/- 1.62e-70]"},"old_p_L1_q5":{"ball":"[5465252.74820754453758907522125359185404577751536954788240883670127501734602 +/- 2.45e-69]"},"old_single_reference_point_profile":{"ball":"[75.1371243070569701308363327870120107201209072360760032611688011403354668895 +/- 2.79e-74]"},"old_strict_K_abs":{"ball":"[1.04865823908991937580382141704176468471500005140100000137865234283457891101 +/- 1.15e-75]"},"old_strict_base":{"ball":"[21.3469011019163416896515281538917805313591836455978155743688350852627672577 +/- 1.82e-74]"},"old_strict_beta":{"ball":"[0.210554392543414249352347051615909607563029295634200000083123635695650182223 +/- 3.77e-76]"},"old_strict_eta_lower":{"ball":"[1.10865901908683104894336679535626899451017379760699999840801776344047961341 +/- 2.53e-76]"},"old_strict_mean_abs":{"ball":"[7.00000019000000000000000000000000000000000000000001000000002328036066992947 +/- 5.49e-77]"}},"fixed_new_per_index_branch_not_a_subtraction":true,"full_theta_and_extended_forcing_retained":true,"kind":"WSMF_complete_natural_conclusion_v1","new_records":{"complete_e_kappa_L1_upper":{"q1":{"ball":"__NEW_BALL__"},"q2":{"ball":"__NEW_BALL__"},"q3":{"ball":"__NEW_BALL__"},"q4":{"ball":"__NEW_BALL__"},"q5":{"ball":"__NEW_BALL__"}},"complete_five_step_terminal_upper":{"k0":{"ball":"__NEW_BALL__"},"k1":{"ball":"__NEW_BALL__"},"k2":{"ball":"__NEW_BALL__"},"k3":{"ball":"__NEW_BALL__"},"k4":{"ball":"__NEW_BALL__"},"k5":{"ball":"__NEW_BALL__"},"k6":{"ball":"__NEW_BALL__"},"k7":{"ball":"__NEW_BALL__"}},"complete_flux_amplitude_L1_upper":{"k0":{"q0":{"ball":"__NEW_BALL__"},"q1":{"ball":"__NEW_BALL__"},"q2":{"ball":"__NEW_BALL__"},"q3":{"ball":"__NEW_BALL__"},"q4":{"ball":"__NEW_BALL__"},"q5":{"ball":"__NEW_BALL__"}},"k1":{"q0":{"ball":"__NEW_BALL__"},"q1":{"ball":"__NEW_BALL__"},"q2":{"ball":"__NEW_BALL__"},"q3":{"ball":"__NEW_BALL__"},"q4":{"ball":"__NEW_BALL__"},"q5":{"ball":"__NEW_BALL__"}},"k2":{"q0":{"ball":"__NEW_BALL__"},"q1":{"ball":"__NEW_BALL__"},"q2":{"ball":"__NEW_BALL__"},"q3":{"ball":"__NEW_BALL__"},"q4":{"ball":"__NEW_BALL__"},"q5":{"ball":"__NEW_BALL__"}}},"complete_reflected_strict_mean_source_upper":{"ball":"__NEW_BALL__"}},"node_name":"strict_per_index_flux_mean","physical_mean_source_unit":"n^(-23/6)","private_jet_arrays_not_public_certificates":true,"retained_scope":{"all_five_mean_steps_and_terminal_degrees_0_through_7_retained":true,"all_four_waist_endpoints_retained":true,"complete_genuine_root_matrix_beta_n_and_two_reference_roles_retained":true,"complete_theta_forcing_and_second_order_drift_retained":true,"full_C_angular_order":6,"full_genuine_Vext_Bext_tail_and_extended_forcing_retained":true,"full_physical_Jr_and_Tk_fees_retained_readonly":true,"mean_source_unit":"n^(-23/6)","new_first_forcing_angular_order":5,"new_first_forcing_radial_order":0,"new_leading_radial_order":2,"new_leading_total_order":7,"no_first_amplitude_radial_derivative_needed_in_exact_flux":true,"no_new_signed_finite_inverse_or_smallness_claim":true,"no_radial_integration_by_parts":true,"no_saved_upper_subtraction":true,"old_local_mean_and_all_old_exponentials_readonly":true,"old_scientific_targets_recomputed":0,"ordinary_WJR_ratios_divided_by_factorial_once":true,"original_PW_cut":"2333968743003/10000000000000","original_true_interfaces":3070,"physical_mean_coordinates":2,"physical_mean_initial_condition":"z_ph(r_star)=0","physical_period":"pi/2","same_function_old_fallback_only_after_ordinary_conversion":true,"same_intrinsic_eta0":true,"same_positive_actual_phase_base_frozen_before_norm":true,"same_whole_and_reduced_compared_separately_old_wins_ties":true,"selected_original_real_member_only":true,"strict_interval":["0","76285779072683/320000000000000"]},"same_old_kappa0_copied_without_arithmetic":true}}''')
ORDERED_RECORD_PATHS = json.loads(r'''{"complete_current_negative_and_whole_receiver":[["complete_collar_retained_and_mean_ordinary_upper"],["complete_strict_retained_and_mean_ordinary_upper"],["complete_collar_retained_mean_and_jumps_received_upper"],["complete_strict_retained_mean_and_jumps_received_upper"],["complete_collar_dyadic_contribution_upper"],["complete_strict_dyadic_contribution_upper"],["complete_same_negative_error_upper"],["complete_nonroot_source_sum_upper"],["complete_all_source_sum_upper"],["complete_whole_received_source_upper"],["complete_same_whole_error_upper"],["complete_reduced_received_source_upper"],["complete_same_reduced_error_upper"]],"complete_physical_mean_and_four_waist_endpoints":[["complete_strict_mean_upper"],["complete_strict_mean_derivative_upper"],["complete_strict_raw_mean_source_upper"],["complete_strict_primitive_mean_source_upper"],["complete_collar_raw_mean_union_upper"],["complete_physical_mean_endpoint_upper"],["complete_same_waist_endpoint_upper"]],"strict_per_index_flux_mean":[["complete_e_kappa_L1_upper","q1"],["complete_e_kappa_L1_upper","q2"],["complete_e_kappa_L1_upper","q3"],["complete_e_kappa_L1_upper","q4"],["complete_e_kappa_L1_upper","q5"],["complete_flux_amplitude_L1_upper","k0","q0"],["complete_flux_amplitude_L1_upper","k1","q0"],["complete_flux_amplitude_L1_upper","k2","q0"],["complete_flux_amplitude_L1_upper","k0","q1"],["complete_flux_amplitude_L1_upper","k1","q1"],["complete_flux_amplitude_L1_upper","k2","q1"],["complete_flux_amplitude_L1_upper","k0","q2"],["complete_flux_amplitude_L1_upper","k1","q2"],["complete_flux_amplitude_L1_upper","k2","q2"],["complete_flux_amplitude_L1_upper","k0","q3"],["complete_flux_amplitude_L1_upper","k1","q3"],["complete_flux_amplitude_L1_upper","k2","q3"],["complete_flux_amplitude_L1_upper","k0","q4"],["complete_flux_amplitude_L1_upper","k1","q4"],["complete_flux_amplitude_L1_upper","k2","q4"],["complete_flux_amplitude_L1_upper","k0","q5"],["complete_flux_amplitude_L1_upper","k1","q5"],["complete_flux_amplitude_L1_upper","k2","q5"],["complete_five_step_terminal_upper","k0"],["complete_five_step_terminal_upper","k1"],["complete_five_step_terminal_upper","k2"],["complete_five_step_terminal_upper","k3"],["complete_five_step_terminal_upper","k4"],["complete_five_step_terminal_upper","k5"],["complete_five_step_terminal_upper","k6"],["complete_five_step_terminal_upper","k7"],["complete_reflected_strict_mean_source_upper"]]}''')
UPSTREAM_COPY_PATHS = json.loads(r'''{"complete_current_negative_and_whole_receiver":{"new_collar_raw_mean_read_back":["complete_physical_mean_and_four_waist_endpoints","new_records","complete_collar_raw_mean_union_upper"],"new_four_waist_endpoints_read_back":["complete_physical_mean_and_four_waist_endpoints","new_records","complete_same_waist_endpoint_upper"],"new_strict_primitive_mean_read_back":["complete_physical_mean_and_four_waist_endpoints","new_records","complete_strict_primitive_mean_source_upper"]},"complete_physical_mean_and_four_waist_endpoints":{"new_complete_strict_CF_read_back":["strict_per_index_flux_mean","new_records","complete_reflected_strict_mean_source_upper"]},"strict_per_index_flux_mean":{}}''')
GATE_LABELS = json.loads(r'''["directed_public_runtime","complete_thirteen_current_file_identities","three_complete_current_source_ASTs","eight_complete_original_schemas_and_statuses","all_complete_original_non_ball_qualification_leaves","all_forty_eight_complete_context_references","same_WGS_dual_file_original_domain_and_normalization","same_WBF_WJR_WDG_true_angular_inputs","complete_potential_tail_and_old_full_mean_kernels","successful_current_complete_WRP_provider","all_actual_positive_lower_endpoints_before_new_arithmetic","complete_thirty_two_strict_flux_records","complete_seven_mean_and_four_endpoint_records","complete_thirteen_same_receiver_records","two_complete_same_operator_whole_choices","all_current_inputs_unchanged","complete_record_copy_prefix_and_shape_accounting","complete_limited_scientific_conclusion"]''')
SCI_FIELDS = json.loads(r'''["kind","problem_id","complete","proved","stage","failure","actual_returncode","runtime","arithmetic_bits","run_id","run_attempt","workflow_event_commit","actual_checkout_commit","scientific_modules","manifest_sha256","input_sha256","verified_original_inputs","original_source_AST_evidence","parameters","retained_scope","accepted_old_inputs","complete_current_provider","complete_new_graphs","whole_candidate_choices","current_target","completed_targets","saved_record_counts","original_record_copy_counts","upstream_record_copy_counts","current_prefix","gates","actual_progress","actual_mathematical_wall_seconds","automatic_retry_authorized"]''')
ACTUAL_PROGRESS_INITIAL = json.loads(r'''{"complete_context_references_verified":0,"complete_original_files_admitted":0,"current_text_files_verified":0,"history_restorations":0,"immutable_AST_files_checked":0,"new_graphs_completed":0,"new_graphs_started":0,"new_records_saved":0,"new_whole_comparisons_completed":0,"old_producer_imports_or_calls":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_record_copies_in_graphs":0,"upstream_new_record_copies_in_graphs":0}''')
ACTUAL_PROGRESS_COMPLETE = json.loads(r'''{"complete_context_references_verified":48,"complete_original_files_admitted":8,"current_text_files_verified":13,"history_restorations":0,"immutable_AST_files_checked":3,"new_graphs_completed":3,"new_graphs_started":3,"new_records_saved":52,"new_whole_comparisons_completed":2,"old_producer_imports_or_calls":0,"old_scientific_calls":0,"old_targets_recomputed":0,"original_record_copies_in_graphs":62,"upstream_new_record_copies_in_graphs":4}''')

def require(condition, message):
    if not condition:
        raise ValueError(message)

def reject_nonfinite(value):
    raise ValueError("nonfinite JSON token: " + value)

def exact_json(raw):
    return json.loads(raw.decode("utf-8"), parse_constant=reject_nonfinite)

def canonical(value):
    return (json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":"),
                       allow_nan=False)+"\n").encode("utf-8")

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def same_json(a,b):
    return canonical(a)==canonical(b)

def at(value,path):
    for key in path:
        value=value[key]
    return value

def scalar_count(value):
    if isinstance(value,dict):
        if set(value)=={"ball"} and isinstance(value["ball"],str):
            return 1
        return sum(scalar_count(v) for v in value.values())
    if isinstance(value,list):
        return sum(scalar_count(v) for v in value)
    return 0

def original_qualifications(value):
    """Full recursive object: only scalar ball leaves and elapsed time are omitted."""
    if isinstance(value,dict):
        if set(value)=={"ball"} and isinstance(value["ball"],str):
            return None
        return {k:original_qualifications(v) for k,v in value.items()
                if k!="actual_mathematical_wall_seconds"}
    if isinstance(value,list):
        return [original_qualifications(v) for v in value]
    return copy.deepcopy(value)

def complete_shape(value,pattern):
    if isinstance(pattern,str) and pattern in ("__NEW_BALL__","__READ_BACK_NEW_BALL__"):
        return isinstance(value,str)
    if isinstance(pattern,dict):
        return (isinstance(value,dict) and set(value)==set(pattern)
                and all(complete_shape(value[k],pattern[k]) for k in pattern))
    if isinstance(pattern,list):
        return (isinstance(value,list) and len(value)==len(pattern)
                and all(complete_shape(v,p) for v,p in zip(value,pattern)))
    return type(value) is type(pattern) and value==pattern

def recursive_prefix(value,pattern):
    if isinstance(pattern,dict):
        return (isinstance(value,dict) and set(value)<=set(pattern)
                and all(recursive_prefix(v,pattern[k]) for k,v in value.items()))
    return complete_shape(value,pattern)

def record_paths(value,prefix=()):
    if isinstance(value,dict):
        if set(value)=={"ball"} and isinstance(value["ball"],str):
            return [list(prefix)]
        result=[]
        for key,child in value.items():
            result.extend(record_paths(child,prefix+(key,)))
        return result
    require(not isinstance(value,list),"public record maps have explicit names")
    return []

def safe_path(root,relative):
    require(isinstance(relative,str) and relative.startswith(TOPIC+"/"),
            "current input inside the exact topic")
    path=(root/relative).resolve()
    require(path.is_relative_to(root/TOPIC) and not path.is_symlink(),
            "current input must be a regular same-topic path")
    return path

def check_file(root,spec):
    require(set(spec)=={"role","path","bytes","sha256","git_blob_sha"},
            "five immutable current file fields")
    require(type(spec["bytes"]) is int and 0<spec["bytes"]<100000
            and re.fullmatch("[0-9a-f]{64}",spec["sha256"])
            and re.fullmatch("[0-9a-f]{40}",spec["git_blob_sha"]),
            "complete small UTF8 file identity")
    raw=safe_path(root,spec["path"]).read_bytes()
    require(len(raw)==spec["bytes"] and digest(raw)==spec["sha256"],
            "complete input bytes or SHA differ: "+spec["role"])
    git=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    require(git==spec["git_blob_sha"],"complete original Git blob differs")
    raw.decode("utf-8")
    return raw

def bounded_diagnostic(text,maximum_json_bytes):
    """Only operational text is bounded; scientific records are never shortened."""
    require(type(maximum_json_bytes) is int and maximum_json_bytes>=2,
            "operational JSON byte limit")
    def size(v):
        return len(json.dumps(v,ensure_ascii=False).encode("utf-8"))
    if size(text)<=maximum_json_bytes:
        return text,False
    lo,hi=0,len(text)
    while lo<hi:
        mid=(lo+hi+1)//2
        if size(text[:mid])<=maximum_json_bytes:
            lo=mid
        else:
            hi=mid-1
    return text[:lo],True

def old_success(old,gate_count):
    require(old["complete"] is True and old["proved"] is True
            and old["failure"] is None and old["actual_returncode"]==0
            and old["stage"]=="complete" and old["arithmetic_bits"]==320
            and old["runtime"]=={"Python":"3.12.14","python_flint":"0.9.0"}
            and len(old["gates"])==gate_count
            and all(set(g)=={"name","passed"} and g["passed"] is True
                    for g in old["gates"]),"complete original successful mathematical result")
    if "current_target" in old:
        require(old["current_target"] is None and old["automatic_retry_authorized"] is False,
                "no unfinished old target or authorized old retry")

def accepted_original_inputs(docs,files):
    references=[]
    for role,old in docs.items():
        spec=files[role]
        references.append({
            "role":role,"complete_file_path":spec["path"],
            "complete_file_git_blob_sha":spec["git_blob_sha"],
            "complete_file_bytes":spec["bytes"],"complete_file_sha256":spec["sha256"],
            "complete_object_json_path":[],
            "complete_original_schema_fields":sorted(old),
            "complete_non_ball_qualification_projection":
                copy.deepcopy(OLD_CONTRACTS[role]["complete_non_ball_qualification_projection"])})
    return {
        "kind":"WSMF_complete_readonly_original_context_admission_v1",
        "complete":True,
        "complete_original_file_receipts":[copy.deepcopy(files[s["role"]])
                                          for s in EXPECTED_OLD_FILES],
        "complete_original_qualification_references":references,
        "complete_consumed_context_references":copy.deepcopy(COMPLETE_CONTEXT_REFERENCES),
        "all_complete_original_bytes_and_scopes_verified":True,
        "all_full_original_bytes_and_Git_SHA_verified":True,
        "all_top_level_schema_fields_verified":True,
        "all_full_non_ball_leaves_and_array_positions_verified":True,
        "all_original_true_false_ancestral_statuses_preserved_by_full_object_references":True,
        "old_failed_ancestors_not_relabelled_success":True,
        "only_complete_existing_extension_node_of_failed_parent_reused":True,
        "scope_content_not_reprinted_but_full_canonical_projection_verified":True,
        "all_same_mean_and_current_provider_types_verified":True,
        "original_record_text_not_reformatted":True,
        "old_scientific_calls":0,"old_targets_recomputed":0,
        "old_producer_imports_or_calls":0,"history_restorations":0}

def read_only_admission(repo,manifest_file,manifest_sha):
    root=Path(repo).resolve()
    mraw=Path(manifest_file).read_bytes()
    require(digest(mraw)==manifest_sha,"manifest CLI complete identity")
    manifest=exact_json(mraw)
    specs=manifest["files"]
    expected_roles=[x["role"] for x in EXPECTED_OLD_FILES]+[
        "math","proof_WSMF","science","worker","rules"]
    require(len(specs)==13 and [s["role"] for s in specs]==expected_roles
            and len({s["path"] for s in specs})==13,
            "thirteen current files in the complete fixed order")
    files={s["role"]:s for s in specs}
    for fixed in EXPECTED_FIXED_FILES:
        require(same_json(files[fixed["role"]],fixed),"fixed current identity differs")
    require(files["science"]["path"]==SOURCE_PATH and files["worker"]["path"]==WORKER_PATH,
            "single new entry and unchanged bounded worker")
    raw={s["role"]:check_file(root,s) for s in specs}
    require(Path(__file__).resolve()==safe_path(root,SOURCE_PATH)
            and Path(__file__).read_bytes()==raw["science"],"actual new owner bytes")
    modules={k:files[k]["sha256"] for k in ("science","math")}
    require(same_json(manifest["scientific_modules"],[files["science"],files["math"]])
            and same_json(manifest["parameters"],PARAMETERS),
            "only owner plus new no-entry mathematical module")
    op=manifest["operation"]
    require(op["kind"]==KIND and op["problem_id"]==PROBLEM_ID
            and same_json(op["parameters"],PARAMETERS)
            and same_json(op["ordered_targets"],ORDERED_GRAPH_NAMES)
            and same_json(op["scientific_module_binding"],modules)
            and op["bits_parameter"]=="arithmetic_bits",
            "complete operation profile")
    for role in ("science","math","worker"):
        ast.parse(raw[role].decode("utf-8"),filename=files[role]["path"])
    docs={s["role"]:exact_json(raw[s["role"]]) for s in EXPECTED_OLD_FILES}
    for role,old in docs.items():
        expected=OLD_CONTRACTS[role]
        require(sorted(old)==expected["complete_schema_fields"]
                and canonical(old)==raw[role],"complete original lexical canonical schema")
        projection=canonical(original_qualifications(old))
        qp=expected["complete_non_ball_qualification_projection"]
        require(len(projection)==qp["bytes"] and digest(projection)==qp["sha256"],
                "full original mathematical and ancestral qualification differs")
    for reference in COMPLETE_CONTEXT_REFERENCES:
        value=at(docs[reference["role"]],reference["json_path"])
        body=canonical(value)
        require(reference["complete_object"] is True and len(body)==reference["bytes"]
                and digest(body)==reference["sha256"],"complete consumed context object")
    for role,count in (("wgs_main",24),("wbf",16),("wjr",15),("wdg",16),("wmt",18),("wrp",14)):
        old_success(docs[role],count)
    g,c=docs["wgs_main"],docs["wgs_copies"]
    require(c["complete"] is True and c["complete_readonly_input_projection"] is True,
            "whole WGS original-input companion")
    for key in ("run_id","run_attempt","workflow_event_commit","source_sha256",
                "math_module_sha256","input_manifest_sha256"):
        require(same_json(g[key],c[key]),"same WGS dual-file run and source")
    require(g["complete_original_inputs_file"]=={
        "bytes":files["wgs_copies"]["bytes"],"filename":"complete-original-inputs.json",
        "sha256":files["wgs_copies"]["sha256"]},"exact companion byte reference")
    for field,hashfield in (
        ("copied_original_scalar_records","copied_original_scalar_records_sha256"),
        ("copied_original_stage_records","copied_original_stage_records_sha256"),
        ("copied_complete_original_scopes","copied_complete_original_scopes_sha256"),
        ("copied_complete_local_coefficients","copied_complete_local_coefficients_sha256")):
        require(digest(canonical(c[field]))==c[hashfield],"entire original WGS companion object")
    require(g["parameters"]["exact_strict_interval"]==PARAMETERS["strict_interval"]
            and g["parameters"]["exact_root_interval"]==PARAMETERS["root_interval"]
            and g["parameters"]["actual_original_interfaces"]==3070
            and g["parameters"]["background_physical_bandwidth"]==384
            and g["parameters"]["exact_fold_strip"]=="3/128"
            and g["parameters"]["old_producer_execution_allowed"] is False,
            "same strict domain, actual support and cut holomorphic scope")
    cert=g["complete_derivative_request_certificate"]
    require(cert["fixed_degree_groups"]==[
        [0,0],[1,1],[2,2],[3,3],[4,4],[5,6],[7,9],[10,12],[13,15]]
        and cert["normalized_coefficients"]=="ordinary derivative norm divided by a! b!"
        and g["complete_strict_geometry_conclusion"]["strict_minus_T_lower_is_old_cut_lower"] is True
        and g["complete_higher_flow_and_cut_conclusion"][
            "all_shorter_intervals_both_branches_both_orientations"] is True,
        "full original jet normalization and actual global lower")
    for role in ("wbf","wjr","wdg"):
        old=docs[role]
        require(old["parameters"]["selected_original_real_member_only"] is True
                and old["parameters"]["fixed_intrinsic_parameter"]=="eta_0"
                and old["parameters"]["strict_interval"]==PARAMETERS["strict_interval"]
                and old["parameters"]["root_interval"]==PARAMETERS["root_interval"]
                and old["parameters"]["physical_period"]=="pi/2"
                and old["parameters"]["physical_mean_coordinates"]==2
                and old["parameters"]["original_true_interfaces"]==3070,
                "same true angular function, reference and complete interval")
    for parent,alias,child in (("wbf","wgs_main","wgs_main"),("wbf","wgs_copies","wgs_copies"),
        ("wbf","wdg_actual","wdg"),("wjr","wgs_main","wgs_main"),("wjr","wbf_actual","wbf"),
        ("wdg","wgs_main","wgs_main"),("wdg","wgs_copies","wgs_copies"),
        ("wmt","wgs_main","wgs_main"),("wmt","wgs_copies","wgs_copies")):
        require(docs[parent]["input_sha256"][alias]==files[child]["sha256"],
                "same complete original angular/mean dependency")
    require(docs["wbf"]["retained_scope"][
                "all_shorter_both_orientations_both_characteristics_and_drift"] is True,
            "both true branches and every ordinary shorter flow")
    phase=docs["wjr"]["complete_new_graphs"][
        "complete_new_positive_phase_average_ratio_conclusion"]
    for flag in ("complete","actual_positive_Jacobian_divided_before_norms",
                 "common_positive_phase_average_ratio","relative_ratio",
                 "complete_original_cut_and_all_shorter_flow","ordinary_physical_angular_derivatives"):
        require(phase[flag] is True,"full frozen positive phase ratio")
    require(phase["maximum_angular_order"]==14
            and len(phase["new_records"][
                "ordinary_common_positive_phase_and_average_ratios_1_through_14"])==14,
            "fourteen complete ordinary positive phase derivatives")
    bf=docs["wbf"]["copied_original_scalar_records"]
    jr=docs["wjr"]["copied_original_scalar_records"]
    high=g["complete_higher_flow_and_cut_conclusion"]
    require(same_json(bf["flow_1"],c["copied_original_scalar_records"]["flow_1"])
            and same_json(bf["phase_1"],high["complete_strict_phase_angular_orders_1_through_15"][0])
            and same_json(bf["strict_phase_lower"],high["strict_phase_lower"])
            and same_json(jr["cut_phase_lower"],high["cut_phase_lower"]),
            "same actual first phase/flow and distinct true lower endpoints")
    for j in range(1,6):
        rec=(bf["flow_1"] if j==1 else docs["wbf"]["complete_new_graphs"][
            "complete_new_sharp_flow_conclusion"]["new_records"][
                "ordinary_flow_orders_2_through_15"][j-2])
        require(same_json(rec,jr["flow_"+str(j)]),"same complete saved branch flow")
    ext=docs["extension"]
    require(ext["kind"]=="WEJ_complete_atomic_node_v1" and ext["node_name"]=="extension_scalars"
            and ext["complete"] is True and ext["failure"] is None
            and ext["all_printed_records_in_complete_conclusion"] is True
            and ext["printed_record_event_count"]==104
            and ext["automatic_retry_authorized"] is False,
            "only original complete extension node, without claiming whole parent success")
    require(ext["binding"]["mathematical_input_sha256"]["WGS_main"]==files["wgs_main"]["sha256"]
            and ext["binding"]["mathematical_input_sha256"]["WGS_original_inputs"]==files["wgs_copies"]["sha256"]
            and ext["conclusion"]["Bext_negative_tail_retained"] is True
            and len(ext["conclusion"]["Vext_derivatives"])==17
            and len(ext["conclusion"]["complete_B_derivatives"])==17,
            "complete genuine cutoff, true nonzero tail and original domains")
    wm=docs["wmt"]
    require(wm["parameters"]["mean_source_decay"]=="n^(-23/6)"
            and wm["parameters"]["mean_steps"]==5
            and wm["parameters"]["minimum_physical_frequency"]==388
            and wm["parameters"]["physical_mean_initial_condition"]=="z_ph(r_star)=0"
            and wm["parameters"]["original_PW_cut"]==PARAMETERS["original_PW_cut"]
            and wm["retained_scope"]["strict_d_A0_has_independent_original_product_primitive_proof"] is True
            and wm["retained_scope"]["WGS_geometry_amplitude_sup_not_A0"] is True
            and wm["retained_scope"]["physical_two_means_and_mean_feedback_retained"] is True
            and wm["retained_scope"]["full_Jr_beta_r_e_kappa_and_R0_retained"] is True,
            "same complete physical mean and independent background A0 qualification")
    kernels=wm["complete_new_graphs"]["complete_normalized_weight_L1_kernels"]
    require(kernels["complete"] is True and kernels["normalized_circle_measure"] is True
            and kernels["angular_derivatives_divided_by_factorial"] is True
            and kernels["full_projection_in_e_kappa_retained"] is True
            and [len(kernels["new_records"][key]) for key in (
                "p_L1_upper","e_L1_upper","e_kappa_L1_upper","pure_angular_background_pair_upper")]
                ==[6,7,6,6],"entire old normalized weight and both mean kernels")
    wrp=docs["wrp"]
    require(wrp["parameters"]["input_order"]==[-4,3]
            and wrp["parameters"]["same_operator_domain"]==PARAMETERS["same_operator_domain"]
            and wrp["parameters"]["original_PW_cut"]==PARAMETERS["original_PW_cut"]
            and wrp["retained_scope"]["entire_E3_terminal_dyadic_contribution_copied_without_subtotal_subtraction"] is True,
            "same current full nonmean/terminal/mean/endpoint receiver")
    for which in ("whole","reduced"):
        choice=wrp["whole_candidate_choices"][which]
        require(choice["both_complete_candidates_retained"] is True
                and choice["prior_wins_equal_saved_upper"] is True
                and same_json(at(wrp,choice["selected_record_path"]),choice["complete_selected_upper"]),
                "same operator current complete selection, including actual source path")
    accepted=accepted_original_inputs(docs,files)
    return {"root":root,"manifest":manifest,"raw_manifest":mraw,"files":files,
            "raw":raw,"documents":docs,"scientific_modules":modules,
            "accepted":accepted,
            "verified":[copy.deepcopy(s) for s in specs]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","manifest-sha","out"):
        parser.add_argument("--"+key,required=True)
    parser.add_argument("--bits",type=int,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    args=parser.parse_args()
    require(args.bits==320,"fixed 320-bit directed arithmetic")
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")==PUBLIC_REPOSITORY,
            "own public Actions only")
    run=os.environ.get("GITHUB_RUN_ID","")
    attempt=os.environ.get("GITHUB_RUN_ATTEMPT","")
    event=os.environ.get("GITHUB_SHA","")
    checkout=os.environ.get("ACTUAL_CHECKOUT_COMMIT","")
    require(re.fullmatch("[0-9]+",run) and re.fullmatch("[0-9]+",attempt)
            and re.fullmatch("[0-9a-f]{40}",event) and re.fullmatch("[0-9a-f]{40}",checkout),
            "actual public run, event and checkout identities")
    out=Path(args.out)
    require(not out.exists(),"no completed or partial new science may be overwritten")
    if args.preflight_only:
        work=read_only_admission(args.repo,args.manifest,args.manifest_sha)
        result={"kind":PREFLIGHT_KIND,"complete":True,"problem_id":PROBLEM_ID,
            "manifest_sha256":args.manifest_sha,"scientific_modules":work["scientific_modules"],
            "actual_checkout_commit":checkout,"verified_original_inputs":work["verified"],
            "accepted_old_inputs":work["accepted"],"full_original_files_admitted":8,
            "all_original_context_objects_verified":48,"new_scientific_records_computed":0,
            "old_scientific_calls":0,"flint_imported":False}
        sys.stdout.write(canonical(result).decode("utf-8"));sys.stdout.flush()
        return 0
    out.parent.mkdir(parents=True,exist_ok=True)
    doc={"kind":KIND,"problem_id":PROBLEM_ID,"complete":False,"proved":False,
        "stage":"read_only_admission","failure":None,"actual_returncode":None,
        "runtime":{},"arithmetic_bits":args.bits,"run_id":run,"run_attempt":attempt,
        "workflow_event_commit":event,"actual_checkout_commit":checkout,
        "scientific_modules":{},"manifest_sha256":args.manifest_sha,"input_sha256":{},
        "verified_original_inputs":[],"original_source_AST_evidence":{},
        "parameters":copy.deepcopy(PARAMETERS),"retained_scope":copy.deepcopy(RETAINED_SCOPE),
        "accepted_old_inputs":{},"complete_current_provider":{},"complete_new_graphs":{},
        "whole_candidate_choices":{},"current_target":None,"completed_targets":[],
        "saved_record_counts":{n:0 for n in ORDERED_GRAPH_NAMES},
        "original_record_copy_counts":{n:0 for n in ORDERED_GRAPH_NAMES},
        "upstream_record_copy_counts":{n:0 for n in ORDERED_GRAPH_NAMES},
        "current_prefix":None,"gates":[],"actual_progress":copy.deepcopy(ACTUAL_PROGRESS_INITIAL),
        "actual_mathematical_wall_seconds":0.0,"automatic_retry_authorized":False}
    math_start=None

    def publish(check_size=True):
        if math_start is not None:
            elapsed=time.perf_counter()-math_start
            require(math.isfinite(elapsed) and elapsed>=0,"finite actual mathematical elapsed time")
            doc["actual_mathematical_wall_seconds"]=elapsed
        raw=canonical(doc)
        try:
            tmp=out.with_name(out.name+".tmp")
            with open(tmp,"wb") as f:
                f.write(raw);f.flush();os.fsync(f.fileno())
            os.replace(tmp,out)
            directory=os.open(str(out.parent),os.O_DIRECTORY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
        finally:
            sys.stdout.write(raw.decode("utf-8"));sys.stdout.flush()
        restored=exact_json(out.read_bytes())
        require(canonical(restored)==raw,"full scientific document durable readback")
        if check_size:
            require(len(raw)<=MAX_SCIENCE_BYTES,"complete scientific prefix exceeds frozen cap")
        return restored

    def gate(name):
        require(len(doc["gates"])<len(GATE_LABELS)
                and name==GATE_LABELS[len(doc["gates"])],"exact gate order")
        doc["gates"].append({"name":name,"passed":True})

    def sync_counts():
        doc["actual_progress"]["new_graphs_started"]=len(doc["complete_new_graphs"])
        doc["actual_progress"]["new_graphs_completed"]=len(doc["completed_targets"])
        for name,graph in doc["complete_new_graphs"].items():
            oldnames=set(graph["copied_original_records"])
            upnames=set(UPSTREAM_COPY_PATHS[name])
            doc["saved_record_counts"][name]=scalar_count(graph["new_records"])
            doc["original_record_copy_counts"][name]=len(oldnames-upnames)
            doc["upstream_record_copy_counts"][name]=len(oldnames&upnames)
        doc["actual_progress"]["new_records_saved"]=sum(doc["saved_record_counts"].values())
        doc["actual_progress"]["original_record_copies_in_graphs"]=sum(
            doc["original_record_copy_counts"].values())
        doc["actual_progress"]["upstream_new_record_copies_in_graphs"]=sum(
            doc["upstream_record_copy_counts"].values())

    def validate_node_prefix(name,graph,progress,previous,prior_target):
        require(name in ORDERED_GRAPH_NAMES and graph["node_name"]==name
                and graph["kind"]=="WSMF_complete_natural_conclusion_v1"
                and graph["complete"] is False,"one unfinished natural graph")
        require(prior_target in (None,name)
                and ORDERED_GRAPH_NAMES[len(doc["completed_targets"])]==name,
                "sequential new target, without retrying completed predecessors")
        pattern=NEW_GRAPH_SHAPES[name]
        for key,value in graph.items():
            require(key in pattern,"unexpected graph prefix field")
            if key not in ("complete","new_records","copied_original_records"):
                require(same_json(value,pattern[key]),"unchanged complete graph qualification")
        require(recursive_prefix(graph["new_records"],pattern["new_records"]),
                "all new prefix records lie in the fixed complete target")
        paths=progress["printed_record_paths"]
        require(paths==ORDERED_RECORD_PATHS[name][:len(paths)]
                and len(paths)==scalar_count(graph["new_records"])
                and sorted(paths)==sorted(record_paths(graph["new_records"])),
                "every issued complete scalar present once, in declared order")
        for key,record in graph["copied_original_records"].items():
            require(key in pattern["copied_original_records"],"unexpected source record alias")
            if key in UPSTREAM_COPY_PATHS[name]:
                source_path=UPSTREAM_COPY_PATHS[name][key]
                require(doc["complete_new_graphs"][source_path[0]]["complete"] is True
                        and same_json(record,at(doc["complete_new_graphs"],source_path)),
                        "upstream new record copied only after whole predecessor completed")
            else:
                require(same_json(record,pattern["copied_original_records"][key]),
                        "old source record copied verbatim")
        if previous is not None:
            require(previous["complete"] is False,"completed graph cannot be restarted")
            for path in record_paths(previous["new_records"]):
                require(same_json(at(previous["new_records"],path),at(graph["new_records"],path)),
                        "a previously saved target cannot change")
            for key,value in previous["copied_original_records"].items():
                require(same_json(value,graph["copied_original_records"][key]),
                        "a previously saved copy cannot change")

    def checkpoint_current_node(name,graph,progress):
        previous=copy.deepcopy(doc["complete_new_graphs"].get(name))
        prior_target=doc["current_target"]
        doc["complete_new_graphs"][name]=copy.deepcopy(graph)
        doc["current_target"]=name
        doc["current_prefix"]={
            "node_name":name,"printed_record_paths":copy.deepcopy(progress["printed_record_paths"]),
            "each_printed_record_in_complete_prefix":True,
            "complete_scientific_document_stored_once":True,
            "complete_graph_json_path":["complete_new_graphs",name]}
        sync_counts()
        doc["stage"]="record_or_copy_saved:"+name
        # Preserve the entire new record before semantic validation or size
        # gates can fail. The next readback is the only downstream source.
        publish(check_size=False)
        validate_node_prefix(name,graph,progress,previous,prior_target)
        restored=publish()
        return copy.deepcopy(restored["complete_new_graphs"][name])

    def publish_graph(name,graph):
        require(doc["current_target"]==name and graph["complete"] is True
                and complete_shape(graph,NEW_GRAPH_SHAPES[name])
                and scalar_count(graph["new_records"])==NEW_RECORD_COUNTS[name],
                "entire natural conclusion and complete scalar count")
        old=doc["complete_new_graphs"][name]
        require(same_json(old["new_records"],graph["new_records"])
                and same_json(old["copied_original_records"],graph["copied_original_records"]),
                "completion cannot add uncheckpointed mathematics")
        require(len(graph["copied_original_records"])==
                OLD_COPY_COUNTS[name]+UPSTREAM_COPY_COUNTS[name],
                "all original and upstream copies present")
        doc["complete_new_graphs"][name]=copy.deepcopy(graph)
        doc["completed_targets"].append(name)
        doc["current_target"]=None
        doc["current_prefix"]=None
        sync_counts()
        gate(GATE_LABELS[10+len(doc["completed_targets"])])
        doc["stage"]="completed:"+name
        restored=publish()
        return copy.deepcopy(restored["complete_new_graphs"][name])

    publish()
    try:
        work=read_only_admission(args.repo,args.manifest,args.manifest_sha)
        doc["scientific_modules"]=copy.deepcopy(work["scientific_modules"])
        doc["verified_original_inputs"]=copy.deepcopy(work["verified"])
        doc["input_sha256"]={role:s["sha256"] for role,s in work["files"].items()}
        doc["input_sha256"]["manifest"]=args.manifest_sha
        doc["original_source_AST_evidence"]={
            "count":3,"roles":["science","math","worker"],
            "all_parsed_as_whole_UTF8_sources":True,"old_source_imports":0,
            "only_one_new_scientific_entry":True}
        doc["accepted_old_inputs"]=copy.deepcopy(work["accepted"])
        doc["actual_progress"].update({
            "complete_original_files_admitted":8,"current_text_files_verified":13,
            "immutable_AST_files_checked":3,"complete_context_references_verified":48})
        doc["stage"]="complete_original_contexts_admitted"
        publish()
        import flint
        from flint import arb,ctx
        require(sys.version_info[:3]==(3,12,14) and flint.__version__=="0.9.0",
                "fixed public directed arithmetic runtime")
        ctx.prec=320
        doc["runtime"]={"Python":"3.12.14","python_flint":"0.9.0"}
        for label in GATE_LABELS[:10]:
            gate(label)

        class ScalarAPI:
            @staticmethod
            def ex(value):
                require(type(value) is int or isinstance(value,Fraction),
                        "exact rational or integer constant")
                f=Fraction(value)
                return arb(str(f.numerator))/arb(str(f.denominator))
            @staticmethod
            def up(value):
                require(value.is_finite() and value.lower()>=0,"finite nonnegative norm upper")
                return value.upper()
            @staticmethod
            def lower(value,label):
                require(value.is_finite() and value.lower()>0,"positive directed lower: "+label)
                return value.lower()
            def read_up(self,record):
                require(isinstance(record,dict) and set(record)=={"ball"}
                        and isinstance(record["ball"],str),"entire saved norm record")
                return self.up(arb(record["ball"]))
            def read_lower(self,record,label):
                require(isinstance(record,dict) and set(record)=={"ball"}
                        and isinstance(record["ball"],str),"entire saved lower record")
                return self.lower(arb(record["ball"]),label)
            def record(self,value):
                # The record is not printed before NodeSink inserts it in the
                # unique complete document and synchronously checkpoints it.
                return {"ball":self.up(value).str(75)}
            @staticmethod
            def checkpoint_current_node(name,graph,progress):
                return checkpoint_current_node(name,graph,progress)

        api=ScalarAPI()
        docs=work["documents"]
        for role,path in (
            ("wgs_copies",["copied_original_scalar_records","t_cut_lower"]),
            ("wgs_copies",["copied_original_scalar_records","q_lower"]),
            ("wgs_copies",["copied_original_scalar_records","eta_lower"]),
            ("wgs_main",["complete_higher_flow_and_cut_conclusion","strict_phase_lower"]),
            ("wgs_main",["complete_higher_flow_and_cut_conclusion","cut_phase_lower"]),
            ("wgs_main",["complete_strict_leading_conclusion","complete_G_lower"]),
            ("wmt",["copied_original_scalar_records","strict_eta_lower"])):
            api.read_lower(at(docs[role],path),role+":"+str(path))
        gate(GATE_LABELS[10])
        doc["stage"]="all_directed_original_inputs_admitted"
        publish()
        # Only the newly reviewed no-entry module is imported; all original
        # scientific producers remain text identities and are never imported.
        module_path=safe_path(work["root"],work["files"]["math"]["path"])
        spec=importlib.util.spec_from_file_location("new_WSMF52_math",module_path)
        require(spec is not None and spec.loader is not None,"new module loader")
        module=importlib.util.module_from_spec(spec)
        sys.modules[spec.name]=module
        spec.loader.exec_module(module)
        require(list(module.PUBLIC_NODE_ORDER)==ORDERED_GRAPH_NAMES
                and list(module.NEW_COUNTS)==[32,7,13],"same three new natural targets")
        provider=module.copy_complete_current_WRP_provider(
            docs["wrp"],work["files"]["wrp"],work["accepted"])
        doc["complete_current_provider"]={k:copy.deepcopy(v) for k,v in provider.items()
                                          if k!="records"}
        doc["complete_current_provider"]["complete_record_map_json_path"]=[
            "complete_new_graphs",ORDERED_GRAPH_NAMES[2],"copied_original_records"]
        doc["complete_current_provider"]["record_alias_prefix"]="provider_"
        doc["stage"]="same_complete_provider_saved"
        publish()
        mathematical_docs={k:v for k,v in docs.items() if k!="wrp"}
        inp=module.MeanInputs(api,mathematical_docs,work["accepted"],provider)
        math_start=time.perf_counter()
        saved=[]
        for index,name in enumerate(ORDERED_GRAPH_NAMES):
            progress={}
            sink=module.NodeSink(api,name,progress,publish_graph)
            if index==0:
                result=module.complete_strict_flux_mean(inp,sink)
            elif index==1:
                result=module.complete_physical_mean_and_endpoints(inp,sink,saved[0])
            else:
                result=module.complete_current_negative_and_whole(inp,sink,saved[1])
            saved.append(result)
        choices=module.complete_new_candidates(saved[-1],provider,api)
        for which in ("whole","reduced"):
            choice=copy.deepcopy(choices[which])
            choice["operator"]="whole" if which=="whole" else "reduced_after_exact_finite_factor_separation"
            choice["current_provider_identity"]=copy.deepcopy(provider["source_identity"])
            choice["new_complete_record_path"]=["complete_new_graphs",ORDERED_GRAPH_NAMES[-1]]+choice[
                "new_complete_record_path"]
            choice["old_complete_record_path"]=["complete_new_graphs",ORDERED_GRAPH_NAMES[-1],
                                                "copied_original_records","provider_prior_"+which]
            choice["selected_record_path"]=(choice["old_complete_record_path"]
                if choice["selected"]=="old_current_complete_candidate"
                else choice["new_complete_record_path"])
            require(same_json(choice["selected_record"],at(doc,choice["selected_record_path"])),
                    "exact saved same-operator choice")
            doc["whole_candidate_choices"][which]=choice
            doc["actual_progress"]["new_whole_comparisons_completed"]+=1
            doc["stage"]="complete_"+which+"_choice_saved"
            publish()
        gate(GATE_LABELS[14])
        for role,item in work["files"].items():
            require(check_file(work["root"],item)==work["raw"][role],
                    "current file changed while forming new candidate")
        require(Path(args.manifest).read_bytes()==work["raw_manifest"],
                "original manifest changed")
        gate(GATE_LABELS[15])
        require(set(doc)==set(SCI_FIELDS) and doc["completed_targets"]==ORDERED_GRAPH_NAMES
                and doc["current_target"] is None and doc["current_prefix"] is None
                and doc["saved_record_counts"]==NEW_RECORD_COUNTS
                and doc["original_record_copy_counts"]==OLD_COPY_COUNTS
                and doc["upstream_record_copy_counts"]==UPSTREAM_COPY_COUNTS
                and complete_shape(doc["complete_new_graphs"],NEW_GRAPH_SHAPES)
                and doc["actual_progress"]==ACTUAL_PROGRESS_COMPLETE
                and set(doc["whole_candidate_choices"])=={"whole","reduced"},
                "complete fifty-two target graph, every original copy and all scopes")
        gate(GATE_LABELS[16])
        doc["complete"]=True;doc["proved"]=True;doc["actual_returncode"]=0
        doc["stage"]="complete"
        gate(GATE_LABELS[17])
        publish()
        return 0
    except BaseException as error:
        trace=traceback.format_exc()
        sys.stderr.write(trace);sys.stderr.flush()
        type_text,type_cut=bounded_diagnostic(type(error).__name__,DIAGNOSTIC_TYPE_BYTES)
        message_text,message_cut=bounded_diagnostic(str(error),DIAGNOSTIC_MESSAGE_BYTES)
        trace_text,trace_cut=bounded_diagnostic(trace,DIAGNOSTIC_TRACEBACK_BYTES)
        doc["complete"]=False;doc["proved"]=False;doc["actual_returncode"]=1
        doc["stage"]="preserved_failure"
        doc["failure"]={
            "type":type_text,"message":message_text,"traceback":trace_text,
            "type_truncated":type_cut,"message_truncated":message_cut,
            "traceback_truncated":trace_cut,"full_text_in_job_log":True,
            "all_previously_saved_scientific_records_preserved":True,
            "automatic_repetition_of_partial_targets_authorized":False}
        publish(check_size=False)
        return 1

if __name__=="__main__":
    raise SystemExit(main())
