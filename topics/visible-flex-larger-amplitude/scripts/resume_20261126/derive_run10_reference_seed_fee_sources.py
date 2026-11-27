#!/usr/bin/env python3
"""Reproduce complete run10 fixed-reference mean/profile/all-batch sources.

This is a source-only transformation and verification tool. It imports no
scientific source, constructs no field, and computes no numerical fee.
Every transformation has an explicit occurrence count and complete inverse.
The original run09 source files remain unchanged.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-larger-amplitude'
SPEC = json.loads("{\"parents\":{\"consumer\":{\"name\":\"run09_reference_seed_angular_profile_error_bounds.py\",\"sha256\":\"7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1\",\"bytes\":64824},\"producer\":{\"name\":\"run09_reference_accurate_mean_residuals.py\",\"sha256\":\"17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820\",\"bytes\":40771},\"scheduler\":{\"name\":\"run09_all_recorded_reference_seed_fees.py\",\"sha256\":\"0c7efa0726aa27dbde769a8cce7615efc75e1676b49cf3c2602767b8543d915f\",\"bytes\":29133}},\"expected\":{\"consumer\":{\"name\":\"run10_reference_seed_angular_profile_error_bounds.py\",\"sha256\":\"91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1\",\"bytes\":64800},\"producer\":{\"name\":\"run10_reference_accurate_mean_residuals.py\",\"sha256\":\"19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38\",\"bytes\":40898},\"scheduler\":{\"name\":\"run10_all_recorded_reference_seed_fees.py\",\"sha256\":\"42624b7f7fb4be694ff1253baf456b8526269a0f20099a40af737b5ffc096cb5\",\"bytes\":29234}},\"patches\":{\"consumer\":[{\"old\":\"run09\",\"new\":\"run10\",\"count\":21},{\"old\":\"complete-run10-public-reference-analytic-frame-material-envelope-SO3-QP-v1\",\"new\":\"complete-run10-detached-closure-value-material-envelope-SO3-QP-v1\",\"count\":1},{\"old\":\"fullclosed_run10_public_reference_analytic_frame_so3_qp_v2.py\",\"new\":\"fullclosed_run10_detached_closure_so3_qp.py\",\"count\":1},{\"old\":\"read_run10_public_reference_analytic_frame_so3_report_v2.py\",\"new\":\"read_run10_detached_closure_so3_report.py\",\"count\":2},{\"old\":\"so3_run10_public_reference_analytic_frame_geometry_v2.py\",\"new\":\"so3_run10_detached_closure_geometry.py\",\"count\":1},{\"old\":\"complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1\",\"new\":\"complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1\",\"count\":1},{\"old\":\"so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py\",\"new\":\"so3_reference_centred_closure_values_normal_lift_operator.py\",\"count\":1},{\"old\":\"reference_centred_analytic_frame_smooth_triangle_calibration.py\",\"new\":\"reference_centred_closure_values_calibration.py\",\"count\":1},{\"old\":\"complete_material_envelope_memory_public_reference.py\",\"new\":\"complete_material_envelope_memory_public_run10.py\",\"count\":1},{\"old\":\"ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5\",\"new\":\"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\",\"count\":2},{\"old\":\"aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32\",\"new\":\"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\",\"count\":2},{\"old\":\"3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc\",\"new\":\"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\",\"count\":1},{\"old\":\"fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0\",\"new\":\"b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f\",\"count\":1},{\"old\":\"f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb\",\"new\":\"1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa\",\"count\":1},{\"old\":\"2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb\",\"new\":\"f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba\",\"count\":1},{\"old\":\"e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13\",\"new\":\"6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528\",\"count\":1},{\"old\":\"45943410994\",\"new\":\"45972294636\",\"count\":1},{\"old\":\"7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a\",\"new\":\"e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049\",\"count\":1},{\"old\":\"d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75\",\"new\":\"081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5\",\"count\":1},{\"old\":\"2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2\",\"new\":\"512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b\",\"count\":1},{\"old\":\"4cc93d406cc1882771d2ebabb34856e7ed195fb6cdb6b361e1b213e504193ad2\",\"new\":\"35fdae489de9a7ee205b4f03f805b30107cec382abbdd242ece43f87d857d286\",\"count\":1},{\"old\":\"2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d\",\"new\":\"4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf\",\"count\":1},{\"old\":\"'returned_input_binding_bytes': 430906\",\"new\":\"'returned_input_binding_bytes': 430908\",\"count\":1},{\"old\":\"15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592\",\"new\":\"dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1\",\"count\":1},{\"old\":\"306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a\",\"new\":\"9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209\",\"count\":1},{\"old\":\"9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18\",\"new\":\"fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a\",\"count\":1},{\"old\":\"\\\"\\\"\\\"Cross-bind the actual v2 field, whole returned target and six true inputs.\\\"\\\"\\\"\",\"new\":\"\\\"\\\"\\\"Cross-bind the actual run10 field, whole returned target and six true inputs.\\\"\\\"\\\"\",\"count\":1},{\"old\":\"MEAN_VECTOR_KEYS =\",\"new\":\"DERIVED_FROM_COMPLETE_RUN09_CONSUMER_SHA256 = '7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1'\\nMEAN_VECTOR_KEYS =\",\"count\":1}],\"producer\":[{\"old\":\"run09\",\"new\":\"run10\",\"count\":4},{\"old\":\"run10 v2 reference\",\"new\":\"run10 detached-closure reference\",\"count\":1},{\"old\":\"7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1\",\"new\":\"91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1\",\"count\":1},{\"old\":\"REFERENCE_UNIT_LAW =\",\"new\":\"DERIVED_FROM_COMPLETE_RUN09_PRODUCER_SHA256 = '17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820'\\nREFERENCE_UNIT_LAW =\",\"count\":1}],\"scheduler\":[{\"old\":\"run09\",\"new\":\"run10\",\"count\":11},{\"old\":\"complete-run10-public-reference-analytic-frame-material-envelope-SO3-QP-v1\",\"new\":\"complete-run10-detached-closure-value-material-envelope-SO3-QP-v1\",\"count\":1},{\"old\":\"read_run10_public_reference_analytic_frame_so3_report_v2.py\",\"new\":\"read_run10_detached_closure_so3_report.py\",\"count\":1},{\"old\":\"ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5\",\"new\":\"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\",\"count\":1},{\"old\":\"aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32\",\"new\":\"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\",\"count\":1},{\"old\":\"run10 v2 reference\",\"new\":\"run10 detached-closure reference\",\"count\":1},{\"old\":\"7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1\",\"new\":\"91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1\",\"count\":1},{\"old\":\"17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820\",\"new\":\"19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38\",\"count\":1},{\"old\":\"INPUTS =\",\"new\":\"DERIVED_FROM_COMPLETE_RUN09_SCHEDULER_SHA256 = '0c7efa0726aa27dbde769a8cce7615efc75e1676b49cf3c2602767b8543d915f'\\nINPUTS =\",\"count\":1}]},\"pins\":{\"root_packets\":[\"scripts/resume_20261126/immutable_closure_values_normal_root_packets.py\",\"31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805\"],\"analytic_parent_stage_matrices\":[\"scripts/resume_20261126/detached_normal_stage_matrix_reuse.py\",\"375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59\"],\"analytic_parent_adjacent_matrices\":[\"scripts/resume_20261126/adjacent_normal_frame_matrices.py\",\"955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3\"],\"analytic_parent_driver\":[\"scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py\",\"95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9\"],\"analytic_parent_reader\":[\"scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py\",\"f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470\"],\"analytic_J3\":[\"scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py\",\"9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa\"],\"analytic_J3_binding\":[\"scripts/resume_20261126/run10_detached_closure_value_binding.py\",\"dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1\"],\"analytic_parent_frame_C1\":[\"scripts/resume_20261126/normal_frame_c1_reuse.py\",\"ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9\"],\"seed_reference\":[\"scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py\",\"0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b\"],\"seed_mean\":[\"scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py\",\"f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917\"],\"reference\":[\"scripts/resume_20261126/so3_axisymmetric_reference.py\",\"4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3\"],\"warm_producer\":[\"notes/2026-11-17-parallel-model-fullclosed-hold-warm.py\",\"bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3\"],\"observed\":[\"scripts/resume_20261120/gauss_observed_closed_gram.py\",\"26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d\"],\"deep_scalar\":[\"scripts/resume_20261126/deep_valley_tail_input.py\",\"e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2\"],\"scalar\":[\"notes/2026-11-17-parallel-model-full-hold-oracle.py\",\"a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670\"],\"integer\":[\"notes/2026-11-17-parallel-inward-integral-enclosure.py\",\"babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0\"],\"hold\":[\"scripts/parallel_20261117_negative_hold_profile_ivp.py\",\"ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1\"],\"meridian\":[\"scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py\",\"6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865\"],\"geometry\":[\"scripts/resume_20261126/so3_run10_detached_closure_geometry.py\",\"6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528\"],\"qp\":[\"scripts/resume_20261120/fullspace_feasible_active_cg_v3.py\",\"fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4\"],\"spectral\":[\"scripts/resume_20261120/positive_spectral_gram_weights.py\",\"e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91\"],\"hessian\":[\"scripts/resume_20261120/positive_spectral_gram_hessian.py\",\"29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4\"],\"centered\":[\"scripts/resume_20261126/centered_spectral_statistics.py\",\"5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01\"],\"history\":[\"scripts/resume_20261120/launch_refinement_from_full_report.py\",\"4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60\"],\"pure_geometry\":[\"scripts/resume_20261120_curvature_qp.py\",\"a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854\"],\"geometry_selector\":[\"scripts/resume_20261120/fullclosed_point_inequalities_v2.py\",\"e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8\"],\"endpoint\":[\"scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py\",\"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\"],\"axisymmetric_seed_driver\":[\"scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py\",\"606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9\"],\"frozen_moment_input\":[\"scripts/resume_20261126/frozen_zero_moment_input.py\",\"4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611\"],\"moment_trace_source\":[\"scripts/resume_20261126/trace_zero_initial_endpoint_failure.py\",\"73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54\"],\"moment_initial_binding\":[\"scripts/resume_20261126/diagnose_zero_initial_chord.py\",\"65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0\"],\"moment_original_endpoint\":[\"scripts/resume_20261126/so3_zero_closure_endpoint_operator.py\",\"5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46\"],\"moment_original_driver\":[\"scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py\",\"b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b\"],\"new_moment_input\":[\"scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py\",\"307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7\"],\"reference_calibration\":[\"scripts/resume_20261126/reference_centred_closure_values_calibration.py\",\"b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f\"],\"frame_C1\":[\"scripts/resume_20261126/normal_frame_c1_closure_values.py\",\"1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa\"],\"envelope_memory\":[\"scripts/resume_20261126/complete_material_envelope_memory.py\",\"c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152\"],\"envelope_rows\":[\"scripts/resume_20261126/complete_material_envelope_rows.py\",\"729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7\"],\"stage_matrices\":[\"scripts/resume_20261126/detached_stage_matrices_closure_values.py\",\"bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45\"],\"envelope_transfer\":[\"scripts/resume_20261126/transfer_run10_detached_closure_memory.py\",\"eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe\"],\"envelope_parent_reader\":[\"scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py\",\"104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7\"],\"envelope_parent_driver\":[\"scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py\",\"cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5\"],\"envelope_parent_endpoint\":[\"scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py\",\"a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd\"],\"envelope_parent_calibration\":[\"scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py\",\"3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991\"],\"envelope_parent_geometry\":[\"scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py\",\"bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f\"],\"adjacent_matrices\":[\"scripts/resume_20261126/adjacent_normal_matrices_closure_values.py\",\"6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650\"],\"independent_envelope_memory\":[\"scripts/resume_20261126/complete_material_envelope_memory_public_run10.py\",\"f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba\"],\"independent_input_projection_producer\":[\"scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py\",\"fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a\"],\"analytic_frame\":[\"scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py\",\"8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598\"],\"frame_parent_driver\":[\"scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py\",\"0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51\"],\"frame_parent_reader\":[\"scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py\",\"c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e\"],\"frame_parent_endpoint\":[\"scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py\",\"04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e\"],\"frame_parent_calibration\":[\"scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py\",\"4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d\"],\"frame_parent_J3\":[\"scripts/resume_20261126/analytic_normal_stage_jacobian.py\",\"64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d\"],\"frame_parent_C1\":[\"scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py\",\"8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8\"],\"frame_parent_stage_matrices\":[\"scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py\",\"5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1\"],\"frame_parent_adjacent_matrices\":[\"scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py\",\"8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787\"],\"actual_public_input_binding\":[\"scripts/resume_20261126/actual_public_run10_reference_input_binding.py\",\"9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209\"],\"closure_values\":[\"scripts/resume_20261126/same_chain_detached_closure_values.py\",\"e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e\"],\"closure_parent_analytic_J3\":[\"scripts/resume_20261126/analytic_frame_local_stage_jacobian.py\",\"894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866\"],\"closure_parent_analytic_frame\":[\"scripts/resume_20261126/analytic_normal_frame_jets.py\",\"4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8\"],\"closure_parent_frame_C1\":[\"scripts/resume_20261126/analytic_frame_c1_reuse.py\",\"f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb\"],\"closure_parent_stage_matrices\":[\"scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py\",\"fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255\"],\"closure_parent_adjacent_matrices\":[\"scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py\",\"3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695\"],\"closure_parent_reference_calibration\":[\"scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py\",\"fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0\"],\"closure_parent_endpoint\":[\"scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py\",\"3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc\"],\"closure_parent_root_packets\":[\"scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py\",\"094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0\"],\"closure_parent_analytic_J3_binding\":[\"scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py\",\"15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592\"],\"closure_parent_geometry\":[\"scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py\",\"e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13\"],\"closure_parent_envelope_transfer\":[\"scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py\",\"6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707\"],\"closure_parent_driver\":[\"scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py\",\"ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5\"],\"closure_parent_reader\":[\"scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py\",\"aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32\"],\"closure_parent_independent_envelope_memory\":[\"scripts/resume_20261126/complete_material_envelope_memory_public_reference.py\",\"2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb\"],\"closure_parent_independent_input_projection_producer\":[\"scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py\",\"9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18\"],\"closure_parent_actual_public_input_binding\":[\"scripts/resume_20261126/actual_public_reference_input_binding.py\",\"306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a\"]},\"external\":{\"driver\":{\"name\":\"fullclosed_run10_detached_closure_so3_qp.py\",\"sha256\":\"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\"},\"reader\":{\"name\":\"read_run10_detached_closure_so3_report.py\",\"sha256\":\"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\"}},\"excluded\":{\"consumer\":[\"recheck_run09_reference_attribution\",\"bind_run09_reference_attribution\",\"bind_outer_report_scope\",\"bind_actual_batch\"],\"producer\":[],\"scheduler\":[\"actual_reference_attribution\",\"bind_actual\",\"recheck\"]}}")


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def read_bound(path, expected, size=None):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected or (size is not None and len(raw) != size):
        raise ValueError('Changed complete bound source: '+str(path))
    return raw.decode('utf-8')


def literal(text, name):
    nodes = [node for node in ast.parse(text).body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)]
    if len(nodes) != 1:
        raise ValueError('Expected one complete literal assignment: '+name)
    return ast.literal_eval(nodes[0].value)


def transform(role, parent):
    text = parent
    for patch in SPEC['patches'][role]:
        if text.count(patch['old']) != patch['count']:
            raise ValueError('Changed complete replacement occurrence: '+role+' '+repr(patch['old']))
        text = text.replace(patch['old'], patch['new'])
    expected = SPEC['expected'][role]
    if digest(text) != expected['sha256'] or len(text.encode('utf-8')) != expected['bytes']:
        raise ValueError('Complete generated source differs from its locked identity: '+role)
    reverse = text
    for patch in reversed(SPEC['patches'][role]):
        if reverse.count(patch['new']) != patch['count']:
            raise ValueError('Ambiguous complete inverse: '+role+' '+repr(patch['new']))
        reverse = reverse.replace(patch['new'], patch['old'])
    if reverse != parent:
        raise ValueError('The whole inverse does not restore the original published source')
    return text


def validate_source(name, text):
    tree = ast.parse(text, filename=name)
    compile(tree, name, 'exec')
    for node in ast.walk(tree):
        keys = ([key.value for key in node.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)]
            if isinstance(node, ast.Dict) else
            [key.arg for key in node.keywords if key.arg is not None]
            if isinstance(node, ast.Call) else [])
        if len(keys) != len(set(keys)):
            raise ValueError('Duplicate literal key or keyword: '+name+':'+str(node.lineno))
    if any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError('Trailing source whitespace: '+name)
    return tree


def compare_complete_bodies(role, parent, current):
    before = ast.parse(parent)
    after = ast.parse(current)
    kind = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
    old = {node.name: node for node in before.body if isinstance(node, kind)}
    new = {node.name: node for node in after.body if isinstance(node, kind)}
    excluded = set(SPEC['excluded'][role])
    same = []
    for name, node in old.items():
        if name in excluded:
            continue
        other = new.get(name)
        if other is None or ast.dump(node, include_attributes=False) != ast.dump(other, include_attributes=False):
            raise ValueError('Original complete mathematical/control body changed: '+role+'/'+name)
        if ast.get_source_segment(parent, node) != ast.get_source_segment(current, other):
            raise ValueError('Original complete body bytes changed: '+role+'/'+name)
        same.append(name)
    return dict(complete_byte_and_AST_equal_top_level_bodies=same,
        count=len(same),explicit_binding_body_exclusions=sorted(excluded),
        exact_complete_parent_restored_by_inverse=True)


def validate_actual_source_contract(repo, directory, sources):
    driver = read_bound(directory/SPEC['external']['driver']['name'],
        SPEC['external']['driver']['sha256'])
    reader = read_bound(directory/SPEC['external']['reader']['name'],
        SPEC['external']['reader']['sha256'])
    pins = literal(driver, 'SOURCE_PINS')
    if {key:list(value) for key,value in pins.items()} != SPEC['pins'] or len(pins) != 75:
        raise ValueError('Retain all 75 actual current source roles, including full historical parents')
    texts = {role:read_bound(repo/TOPIC/relative, sha256)
        for role,(relative,sha256) in pins.items()}
    consumer = sources['consumer']
    contract = literal(consumer, 'ADAPTER_SOURCE_CONTRACT')
    envelope = literal(consumer, 'MATERIAL_ENVELOPE_SOURCE_CONTRACT')
    actual = literal(consumer, 'ACTUAL_PUBLIC_REFERENCE_CONTRACT')
    if (literal(driver,'SCHEMA') != contract['report_schema']
            or literal(reader,'REPORT_SCHEMA') != contract['report_schema']
            or literal(reader,'DRIVER_SHA') != contract['driver_sha256']
            or literal(texts['endpoint'],'SCHEMA') != contract['field_schema']
            or literal(texts['reference_calibration'],'ENDPOINT_SCHEMA') != contract['field_schema']
            or literal(texts['independent_envelope_memory'],'SCHEMA') != envelope['memory_schema']
            or literal(texts['independent_envelope_memory'],'DEFINITION_SCHEMA') != envelope['policy_schema']):
        raise ValueError('The complete current scientific/pure/model/calibration/envelope schemas changed')
    roles = dict(endpoint=contract['field_sha256'],
        reference_calibration=contract['calibration_sha256'],
        frame_C1=contract['C1_sha256'],
        independent_envelope_memory=envelope['memory_sha256'],
        envelope_rows=envelope['rows_sha256'],geometry=envelope['geometry_sha256'],
        analytic_J3_binding=actual['entry_binding_source_sha256'],
        actual_public_input_binding=actual['public_input_source_sha256'],
        independent_input_projection_producer=actual['input_producer_source_sha256'],
        reference=actual['reference_source_sha256'],
        seed_reference=literal(consumer,'PROVIDER_SHA'),seed_mean=literal(consumer,'KERNEL_SHA'),
        meridian='6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865')
    if any(pins[role][1] != expected for role,expected in roles.items()):
        raise ValueError('An actual field/reference/input/source role was relabelled')
    binding = texts['analytic_J3_binding']
    if (literal(binding,'ACTUAL_RUN10_BINDING_SHA256') != actual['returned_input_binding_sha256']
            or literal(binding,'ACTUAL_RUN10_BINDING_BYTES') != actual['returned_input_binding_bytes']
            or literal(binding,'ACTUAL_RUN10_TARGET_IDENTITY') != actual['target_identity_sha256']
            or literal(binding,'ACTUAL_RUN10_MODEL_IDENTITY') != actual['reference_model_identity_sha256']
            or literal(binding,'ACTUAL_RUN10_CHART_IDENTITY') != actual['fixed_chart_core_sha256']
            or literal(binding,'ACTUAL_RUN10_PUBLIC_INPUT_SOURCE') != actual['public_input_source_sha256']
            or literal(binding,'ACTUAL_RUN10_PRODUCER_SOURCE') != actual['input_producer_source_sha256']):
        raise ValueError('Retain the actually returned whole run10 input and canonical target')
    producer = literal(sources['producer'],'PINS')
    schedule = literal(sources['scheduler'],'PINS')
    if (producer['fees'] != ('scripts/resume_20261126/'+SPEC['expected']['consumer']['name'],
                SPEC['expected']['consumer']['sha256'])
            or schedule['consumer'] != (SPEC['expected']['consumer']['name'],SPEC['expected']['consumer']['sha256'])
            or schedule['producer'] != (SPEC['expected']['producer']['name'],SPEC['expected']['producer']['sha256'])
            or schedule['reader'] != (SPEC['external']['reader']['name'],SPEC['external']['reader']['sha256'])):
        raise ValueError('The complete newly derived fee dependency chain is not closed')
    for role,(relative,expected) in producer.items():
        if role != 'fees':
            read_bound(repo/TOPIC/relative,expected)
    return dict(actual_outer_source_contract=contract,
        actual_material_envelope_contract=envelope,
        actual_public_reference_contract=actual,
        complete_actual_driver_source_roles={key:list(value) for key,value in pins.items()},
        all_actual_driver_source_roles_verified=len(pins))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--verify-existing',action='store_true')
    args=parser.parse_args()
    repo,out=args.repo.resolve(),args.outdir.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Stage source-only reproductions outside the repository')
    directory=repo/TOPIC/'scripts/resume_20261126'
    parents={role:read_bound(directory/item['name'],item['sha256'],item['bytes'])
        for role,item in SPEC['parents'].items()}
    sources={role:transform(role,parent) for role,parent in parents.items()}
    for role,text in sources.items():
        validate_source(SPEC['expected'][role]['name'],text)
    checks={role:compare_complete_bodies(role,parents[role],text)
        for role,text in sources.items()}
    contracts=validate_actual_source_contract(repo,directory,sources)
    out.mkdir(parents=True,exist_ok=True)
    for role,text in sources.items():
        name=SPEC['expected'][role]['name']
        path=out/name
        if args.verify_existing:
            if path.read_bytes() != text.encode('utf-8'):
                raise ValueError('The existing complete generated source differs: '+name)
        else:
            if path.exists():
                raise FileExistsError('Never overwrite a prior source reproduction: '+str(path))
            path.write_text(text,encoding='utf-8')
            (out/(name+'.diff')).write_text(''.join(difflib.unified_diff(
                parents[role].splitlines(keepends=True),text.splitlines(keepends=True),
                fromfile=SPEC['parents'][role]['name'],tofile=name)),encoding='utf-8')
    result=dict(schema='complete-run10-reference-seed-fee-source-derivation-v1',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        complete_published_parents=SPEC['parents'],complete_outputs=SPEC['expected'],
        explicit_complete_patch_lists=SPEC['patches'],
        complete_body_preservation=checks,**contracts,
        source_only_replay_performed=True,Python_AST_compile_performed=True,
        scientific_modules_imported=False,actual_batch_or_angle_selected=False,
        actual_fees_generated=False,solver_admission_prerequisite=False,
        all_radial_and_profile_mathematics_unchanged=True,
        complete_whole_angle_or_normal_or_field_error_paid=False,
        existing_whole_bytes_match=True if args.verify_existing else None)
    if not args.verify_existing:
        (out/'run10-reference-seed-fee-reproduction-result.json').write_text(
            json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__=='__main__':
    main()
