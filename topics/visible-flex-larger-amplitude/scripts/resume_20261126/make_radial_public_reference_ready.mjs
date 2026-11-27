#!/usr/bin/env node
// Complete parameter construction only; no scientific evaluation or queue mutation.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
const PARENT_READY = {"path":"computations/run09-public-reference-analytic-frame-v2-complete-ready.json","bytes":93108,"sha256":"2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f"};
const RUNTIME = {
 "radial_bisection_layout.py": {
  "name": "radial_bisection_layout.py",
  "bytes": 18923,
  "sha256": "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744"
 },
 "exact_affine_supported_reference.py": {
  "name": "exact_affine_supported_reference.py",
  "bytes": 23435,
  "sha256": "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117"
 },
 "complete_dyadic_radial_observations.py": {
  "name": "complete_dyadic_radial_observations.py",
  "bytes": 28167,
  "sha256": "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74"
 },
 "so3_radial_refined_public_reference_meridian_operator.py": {
  "name": "so3_radial_refined_public_reference_meridian_operator.py",
  "bytes": 45749,
  "sha256": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0"
 },
 "radial_refined_public_reference_literal_zero_moment_input.py": {
  "name": "radial_refined_public_reference_literal_zero_moment_input.py",
  "bytes": 35736,
  "sha256": "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652"
 },
 "radial_refined_public_reference_calibration.py": {
  "name": "radial_refined_public_reference_calibration.py",
  "bytes": 12760,
  "sha256": "c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178"
 },
 "radial_refined_public_reference_stage_jacobian.py": {
  "name": "radial_refined_public_reference_stage_jacobian.py",
  "bytes": 24224,
  "sha256": "0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9"
 },
 "radial_refined_public_reference_normal_frame.py": {
  "name": "radial_refined_public_reference_normal_frame.py",
  "bytes": 33668,
  "sha256": "8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce"
 },
 "radial_refined_public_reference_frame_c1.py": {
  "name": "radial_refined_public_reference_frame_c1.py",
  "bytes": 35894,
  "sha256": "bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e"
 },
 "radial_refined_public_reference_stage_matrices.py": {
  "name": "radial_refined_public_reference_stage_matrices.py",
  "bytes": 47775,
  "sha256": "fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387"
 },
 "radial_refined_public_reference_adjacent_matrices.py": {
  "name": "radial_refined_public_reference_adjacent_matrices.py",
  "bytes": 36761,
  "sha256": "3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4"
 },
 "so3_radial_refined_public_reference_normal_lift.py": {
  "name": "so3_radial_refined_public_reference_normal_lift.py",
  "bytes": 96539,
  "sha256": "8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5"
 },
 "immutable_radial_refined_public_reference_root_packets.py": {
  "name": "immutable_radial_refined_public_reference_root_packets.py",
  "bytes": 69728,
  "sha256": "8d2b93dd055cc600aac14183d060d101421a924590c1fe8300625931bc8c0403"
 },
 "radial_material_address_transfer.py": {
  "name": "radial_material_address_transfer.py",
  "bytes": 22097,
  "sha256": "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716"
 },
 "radial_refined_public_reference_memory.py": {
  "name": "radial_refined_public_reference_memory.py",
  "bytes": 59239,
  "sha256": "6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a"
 },
 "radial_refined_public_reference_source_binding.py": {
  "name": "radial_refined_public_reference_source_binding.py",
  "bytes": 47609,
  "sha256": "5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734"
 },
 "radial_refined_public_reference_history_transfer.py": {
  "name": "radial_refined_public_reference_history_transfer.py",
  "bytes": 86470,
  "sha256": "2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c"
 },
 "so3_radial_refined_public_reference_envelope_geometry.py": {
  "name": "so3_radial_refined_public_reference_envelope_geometry.py",
  "bytes": 69975,
  "sha256": "2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877"
 },
 "fullclosed_radial_refined_public_reference_so3_qp.py": {
  "name": "fullclosed_radial_refined_public_reference_so3_qp.py",
  "bytes": 90333,
  "sha256": "1709eb319dcecfc1310c9c763cfb812aad56599736965b39de3790dec719aa0f"
 },
 "launch_radial_refined_public_reference_so3_actions.py": {
  "name": "launch_radial_refined_public_reference_so3_actions.py",
  "bytes": 22323,
  "sha256": "2658b074a61afa32305703def009e71c8aa99836036a6b756508e6305a7770ec"
 },
 "read_radial_refined_public_reference_so3_report.py": {
  "name": "read_radial_refined_public_reference_so3_report.py",
  "bytes": 97634,
  "sha256": "c344478b6dbb0df0dfa80e924b6ef6a739d79460ab3094a16f23b8b33bdb2695"
 }
};
const SOURCE_PINS = {
 "root_packets": [
  "scripts/resume_20261126/immutable_radial_refined_public_reference_root_packets.py",
  "8d2b93dd055cc600aac14183d060d101421a924590c1fe8300625931bc8c0403"
 ],
 "analytic_parent_stage_matrices": [
  "scripts/resume_20261126/detached_normal_stage_matrix_reuse.py",
  "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59"
 ],
 "analytic_parent_adjacent_matrices": [
  "scripts/resume_20261126/adjacent_normal_frame_matrices.py",
  "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3"
 ],
 "analytic_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
  "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"
 ],
 "analytic_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py",
  "f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470"
 ],
 "analytic_J3": [
  "scripts/resume_20261126/radial_refined_public_reference_stage_jacobian.py",
  "0f4d380773e21c098adf2d6647fb12ba45a620dc4c92592ea22237de821ad6e9"
 ],
 "analytic_J3_binding": [
  "scripts/resume_20261126/radial_refined_public_reference_source_binding.py",
  "5b50b02aea139b81e7e1ed3cbf37c4ad8870d182c63d48bf648fb197e1cf3734"
 ],
 "analytic_parent_frame_C1": [
  "scripts/resume_20261126/normal_frame_c1_reuse.py",
  "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"
 ],
 "seed_reference": [
  "scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py",
  "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"
 ],
 "seed_mean": [
  "scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py",
  "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
 ],
 "reference": [
  "scripts/resume_20261126/so3_axisymmetric_reference.py",
  "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
 ],
 "warm_producer": [
  "notes/2026-11-17-parallel-model-fullclosed-hold-warm.py",
  "bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3"
 ],
 "observed": [
  "scripts/resume_20261120/gauss_observed_closed_gram.py",
  "26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"
 ],
 "deep_scalar": [
  "scripts/resume_20261126/deep_valley_tail_input.py",
  "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
 ],
 "scalar": [
  "notes/2026-11-17-parallel-model-full-hold-oracle.py",
  "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"
 ],
 "integer": [
  "notes/2026-11-17-parallel-inward-integral-enclosure.py",
  "babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"
 ],
 "hold": [
  "scripts/parallel_20261117_negative_hold_profile_ivp.py",
  "ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"
 ],
 "meridian": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py",
  "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0"
 ],
 "geometry": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_envelope_geometry.py",
  "2fe41a0ecc48d1404973b55dcde4cb4591bc4029fb4158740bbf5369aa869877"
 ],
 "qp": [
  "scripts/resume_20261120/fullspace_feasible_active_cg_v3.py",
  "fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"
 ],
 "spectral": [
  "scripts/resume_20261120/positive_spectral_gram_weights.py",
  "e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91"
 ],
 "hessian": [
  "scripts/resume_20261120/positive_spectral_gram_hessian.py",
  "29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4"
 ],
 "centered": [
  "scripts/resume_20261126/centered_spectral_statistics.py",
  "5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01"
 ],
 "history": [
  "scripts/resume_20261120/launch_refinement_from_full_report.py",
  "4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"
 ],
 "pure_geometry": [
  "scripts/resume_20261120_curvature_qp.py",
  "a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854"
 ],
 "geometry_selector": [
  "scripts/resume_20261120/fullclosed_point_inequalities_v2.py",
  "e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8"
 ],
 "endpoint": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_normal_lift.py",
  "8591b957da548e28efb42d456f55879b5d75fa950a686aab600c2d3b00a887c5"
 ],
 "axisymmetric_seed_driver": [
  "scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py",
  "606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9"
 ],
 "frozen_moment_input": [
  "scripts/resume_20261126/frozen_zero_moment_input.py",
  "4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611"
 ],
 "moment_trace_source": [
  "scripts/resume_20261126/trace_zero_initial_endpoint_failure.py",
  "73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54"
 ],
 "moment_initial_binding": [
  "scripts/resume_20261126/diagnose_zero_initial_chord.py",
  "65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0"
 ],
 "moment_original_endpoint": [
  "scripts/resume_20261126/so3_zero_closure_endpoint_operator.py",
  "5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46"
 ],
 "moment_original_driver": [
  "scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py",
  "b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b"
 ],
 "new_moment_input": [
  "scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py",
  "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652"
 ],
 "reference_calibration": [
  "scripts/resume_20261126/radial_refined_public_reference_calibration.py",
  "c4a0160f769c5d97a102785cd8fd64cc527f2e236946901bdf0bc0a58621a178"
 ],
 "frame_C1": [
  "scripts/resume_20261126/radial_refined_public_reference_frame_c1.py",
  "bd1f11970897ec217edad05fd4a89eac2e5a4279508f15eb36e3d50959a38d8e"
 ],
 "envelope_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory.py",
  "c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152"
 ],
 "envelope_rows": [
  "scripts/resume_20261126/complete_material_envelope_rows.py",
  "729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7"
 ],
 "stage_matrices": [
  "scripts/resume_20261126/radial_refined_public_reference_stage_matrices.py",
  "fab35a0c45681b352c5087297c7c47e8156674bce5616680952d0abcc253d387"
 ],
 "envelope_transfer": [
  "scripts/resume_20261126/radial_refined_public_reference_history_transfer.py",
  "2720bd9033391fc3f0a48afe33f50ea5843b2bf225a6596ee5a5b7077819e55c"
 ],
 "envelope_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py",
  "104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7"
 ],
 "envelope_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py",
  "cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"
 ],
 "envelope_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py",
  "a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd"
 ],
 "envelope_parent_calibration": [
  "scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py",
  "3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991"
 ],
 "envelope_parent_geometry": [
  "scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py",
  "bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f"
 ],
 "adjacent_matrices": [
  "scripts/resume_20261126/radial_refined_public_reference_adjacent_matrices.py",
  "3a156cc80399c3f7c3f59ed8b01a24038e3dcdc1c7d6ac2144c140d526e656d4"
 ],
 "independent_envelope_memory": [
  "scripts/resume_20261126/radial_refined_public_reference_memory.py",
  "6d8184f921e93265284c1a5396b9349d3adefd9cfbd7531cf2f4a682b33ad33a"
 ],
 "independent_input_projection_producer": [
  "scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py",
  "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"
 ],
 "analytic_frame": [
  "scripts/resume_20261126/radial_refined_public_reference_normal_frame.py",
  "8fb0f326356d8e94337d51bfba85068c5872453df8f08e6619f241dfe7f715ce"
 ],
 "frame_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
  "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51"
 ],
 "frame_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py",
  "c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e"
 ],
 "frame_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py",
  "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"
 ],
 "frame_parent_calibration": [
  "scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py",
  "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"
 ],
 "frame_parent_J3": [
  "scripts/resume_20261126/analytic_normal_stage_jacobian.py",
  "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"
 ],
 "frame_parent_C1": [
  "scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py",
  "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"
 ],
 "frame_parent_stage_matrices": [
  "scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py",
  "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"
 ],
 "frame_parent_adjacent_matrices": [
  "scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py",
  "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"
 ],
 "actual_public_input_binding": [
  "scripts/resume_20261126/actual_public_reference_input_binding.py",
  "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"
 ],
 "radial_parent_meridian": [
  "scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py",
  "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"
 ],
 "radial_parent_new_moment_input": [
  "scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py",
  "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"
 ],
 "radial_parent_analytic_J3": [
  "scripts/resume_20261126/analytic_frame_local_stage_jacobian.py",
  "894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"
 ],
 "radial_parent_analytic_frame": [
  "scripts/resume_20261126/analytic_normal_frame_jets.py",
  "4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"
 ],
 "radial_parent_frame_C1": [
  "scripts/resume_20261126/analytic_frame_c1_reuse.py",
  "f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"
 ],
 "radial_parent_stage_matrices": [
  "scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py",
  "fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"
 ],
 "radial_parent_adjacent_matrices": [
  "scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py",
  "3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"
 ],
 "radial_parent_reference_calibration": [
  "scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py",
  "fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"
 ],
 "radial_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py",
  "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"
 ],
 "radial_parent_root_packets": [
  "scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py",
  "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"
 ],
 "radial_parent_envelope_transfer": [
  "scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py",
  "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"
 ],
 "radial_parent_analytic_J3_binding": [
  "scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py",
  "15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"
 ],
 "radial_parent_geometry": [
  "scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py",
  "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"
 ],
 "radial_parent_driver": [
  "scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",
  "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
 ],
 "radial_parent_reader": [
  "scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py",
  "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"
 ],
 "radial_layout": [
  "scripts/resume_20261126/radial_bisection_layout.py",
  "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744"
 ],
 "radial_affine_reference": [
  "scripts/resume_20261126/exact_affine_supported_reference.py",
  "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117"
 ],
 "radial_observations": [
  "scripts/resume_20261126/complete_dyadic_radial_observations.py",
  "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74"
 ],
 "radial_address_transfer": [
  "scripts/resume_20261126/radial_material_address_transfer.py",
  "6c77349921ccfdfa765e720a330e584abba96d65c4566d9a4286df072428e716"
 ],
 "radial_parent_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory_public_reference.py",
  "2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"
 ]
};
const OTHER_CONSTRUCTORS = {
 "derive_radial_public_reference_lower.mjs": {
  "name": "derive_radial_public_reference_lower.mjs",
  "bytes": 29293,
  "sha256": "5fc01d13c64055222991eb10f84cb940e01ef0c0ba4c79ae6dd37391741f0d90"
 },
 "derive_radial_public_reference_memory_binding.mjs": {
  "name": "derive_radial_public_reference_memory_binding.mjs",
  "bytes": 67357,
  "sha256": "5b32bc01adedc3ecc72aa644f949ede1e9f4041f4380bb10bd35d5a11aabf992"
 },
 "derive_radial_public_reference_upper.mjs": {
  "name": "derive_radial_public_reference_upper.mjs",
  "bytes": 66189,
  "sha256": "733ba499b0e5f4df80197c80d3cd14477585d68d90762fbb6cd039b988f7e9d9"
 },
 "reproduce_radial_public_reference_sources.mjs": {
  "name": "reproduce_radial_public_reference_sources.mjs",
  "bytes": 23002,
  "sha256": "bc76c365c4e1595e890d9646f765925763a8acccc9150af9e9d10251955bf8af"
 }
};

function buildRadialReady(original,runtime,pins,constructors,kind){
 const clone=x=>JSON.parse(JSON.stringify(x));
 if(!["independent","terminal","final"].includes(kind))throw new Error("Choose an explicit complete radial input mode");
 if(original.fixed_target.identity_sha256!=="7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a"||
 original.fixed_target.whole_actual_binding_sha256!=="2f8de167fb0b66a9328bb7e45c2a31b0fe985678a0af7143fc1c9e965d18ec3d")
 throw new Error("Preserve the entire actual public09 fixed input");
 const parentDriver="ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5";
 const parentReader="aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32";
 const parentReady={path:"computations/run09-public-reference-analytic-frame-v2-complete-ready.json",
 bytes:93108,sha256:"2ea114b413037b9c54508d4fbf21423abefee7dc73c69a54efc57259aecb1a9f"};
 const olddir="run09-public-reference-analytic-frame-v2-first";
 const newdir={independent:"run09-radial-J1845-analytic-frame-independent",
 terminal:"run09-radial-J1845-analytic-frame-from-terminal-history",
 final:"run09-radial-J1845-analytic-frame-from-complete-final"}[kind];
 const steps=clone(original.steps),replace=s=>s.split(olddir).join(newdir);
 for(let i=0;i<steps.length;i++){
  const step=steps[i];step.id=(i===0?"complete-":"actual-")+newdir+"-20261127";
  step.script="topics/visible-flex-larger-amplitude/scripts/resume_20261126/"+
    (i===0?"launch_radial_refined_public_reference_so3_actions.py":"read_radial_refined_public_reference_so3_report.py");
  step.args=step.args.map(replace);step.outputs=step.outputs.map(replace);
  step.summary=Object.fromEntries(Object.entries(step.summary).map(([k,v])=>[replace(k),v]));
  if(step.cleanup_generated_patterns)step.cleanup_generated_patterns=step.cleanup_generated_patterns.map(replace);
  step.scope=i===0?"Complete J923 to J1845 current shared-quintic radial refinement of the actual09 fixed target. Frozen reference J923/M160/N2048, complete material chart and exact scalar/nodes, fixed supported seed, all 32 normal stages and eight outer Gauss nodes are retained. Every old radial node word and every old free jet is retained, all new midpoint jets are free. Original P0, full historical and original-reference grids, the entire new fine grid and uncapped actual typed memory receive the full physical field. The current norm and positive row rule are new, and the old complete 7377-row functional is separately reread on that same current field."
   :"Pure complete-source/actual09-target/78-role/J1845/history/packet binding. All five fine radial input files, actual current scalar-table metadata, full old-to-fine address mapping and both current and common-parent functional are bound. The original reference parent keeps initial field failures readable. No F/J/root/integral or packet upgrade.";
 }
 steps[0].args.push("--current-radial-factor","2");
 const parentReport="{work}/"+olddir+"/report.json",parentFinal="{work}/"+olddir+"/final-new-field.npz";
 if(kind!=="independent"){
  const kept=[];for(let i=0;i<steps[0].args.length;i++){
   const a=steps[0].args[i];if(a==="--independent-envelope-branch")continue;
   if(a==="--pending-parallel-envelope-run"||a==="--pending-parallel-envelope-source"){i++;continue;}
   kept.push(a);
  }
  steps[0].args=kept;
  steps[0].args.push("--material-envelope-parent-report",parentReport);
  if(kind==="final"){
   steps[0].args.push("--material-envelope-seed-report",parentReport,"--material-envelope-seed-checkpoint",parentFinal);
   steps[0].parent_bundle=olddir+"/final-new-field.npz";
  }
 }else steps[0].args.push("--pending-parallel-envelope-run","45943410994/1",
  "--pending-parallel-envelope-source","45943410994/1="+parentDriver);
 if(steps[1].parent_bundle!=="axisymmetric-R690-reference-v2-first/reference.npz")
  throw new Error("The pure reader must not require an unreturned new final");
 steps[0].retain_complete_fine_input_and_original_reference_cache_for_same_field_diagnostics=true;
 steps[0].fine_input_directory_retained=newdir+"/fixed-supported-smooth-triangle-reference-cache/complete-radial-input";
 const science=Object.values(steps[0].summary)[0],pure=Object.values(steps[1].summary)[0];
 Object.assign(science,{
  reference_J:"reference_J",current_J:"current_J",
  same_full_fixed_reference_target:"full_fixed_reference_target_unchanged",
  radial_observation_refinement:"radial_observation_refinement_performed",
  angular_observation_refinement:"angular_observation_refinement_performed",
  frequency_refinement:"frequency_refinement_performed",
  current_norm_and_row_rule_changed:"current_coordinate_norm_and_positive_observation_rule_changed",
  old_parent_Phi_inherited:"saved_parent_Phi_used_as_current_baseline",
  radial_layout_identity:"radial_layout_identity_sha256",
  radial_input_mode:"radial_refinement.mode",
  radial_initial_point:"radial_refinement.current_full_point_sha256",
  original_frozen_point:"radial_refinement.frozen_original_point_relation.original_full_point_sha256",
  current_frozen_point:"radial_refinement.frozen_original_point_relation.current_full_point_sha256",
  radial_observation_count:"complete_radial_input_metadata.current_complete_observation_count",
  current_scalar_leaf_count:"complete_radial_input_metadata.actual_scalar_reconstruction.actual_current_leaf_count",
  current_scalar_accuracy_reached:"complete_radial_input_metadata.requested_scalar_accuracy_reached",
  original_7377_target_words_reproduced:"complete_radial_input_metadata.all_parent_target_words_reproduced",
  complete_a_error_bounds_recorded:"complete_radial_input_metadata.complete_scalar_remainder_and_carrier_error_bounds_recorded",
  midpoint_coefficient_errors_enclosed:"current_midpoint_coefficient_rounding_enclosed",
  common_parent_initial_Phi:"initial.common_parent_functional.spectral.centered_phi_normalized",
  common_parent_final_Phi:"final_statistics.common_parent_functional.spectral.centered_phi_normalized",
  common_parent_initial_max:"initial.common_parent_functional.max_relative_gram",
  common_parent_final_max:"final_statistics.common_parent_functional.max_relative_gram",
  common_parent_positive_normalizer:"common_parent_radial_functional.normalizer"
 });
 Object.assign(pure,{
  reference_J:"radial_refinement.reference_J",current_J:"radial_refinement.current_J",
  radial_input_mode:"radial_refinement.mode",
  radial_initial_point:"radial_refinement.actual_initial_full_point_sha256",
  midpoint_coefficient_errors_enclosed:"radial_refinement.midpoint_coefficient_errors_enclosed",
  radial_old_values_or_certificates_inherited:"radial_refinement.old_field_values_or_certificates_inherited",
  current_scalar_leaf_count:"radial_refinement.actual_radial_inputs_and_common_parent.actual_current_scalar_leaf_count",
  current_scalar_accuracy_reached:"radial_refinement.actual_radial_inputs_and_common_parent.actual_current_scalar_requested_accuracy_reached",
  original_7377_target_words_reproduced:"radial_refinement.actual_radial_inputs_and_common_parent.all_original_target_words_reproduced",
  common_parent_actual_statistic_count:"radial_refinement.actual_radial_inputs_and_common_parent.common_parent_actual_statistic_count",
  common_parent_normalization:"radial_refinement.actual_radial_inputs_and_common_parent.actual_common_parent_normalization",
  common_parent_initial_Phi:"initial.common_parent_functional.spectral.centered_phi_normalized",
  common_parent_final_Phi:"final.common_parent_functional.spectral.centered_phi_normalized",
  common_parent_initial_max:"initial.common_parent_functional.max_relative_gram",
  common_parent_final_max:"final.common_parent_functional.max_relative_gram",
  continuous_metric_or_geometry_certified:"radial_refinement.actual_radial_inputs_and_common_parent.continuous_error_or_geometry_certified"
 });
 if(Object.keys(runtime).length!==21||Object.keys(pins).length!==78)throw new Error("Keep all 21 full sources and all 78 source roles");
 const result=clone(original);
 Object.assign(result,{
  schema:"complete-actual-public09-analytic-frame-J1845-parameter-plan-v1",executed:false,queued:false,
  complete_source_and_parameter_closure:true,
  scope:"Exact-affine J923 to J1845 refinement of the current SO3 shared-quintic radial space. The entire actual09 fixed target, M160/N2048 and J923 reference seed remain frozen. The current positive observation rule and full coordinate norm change explicitly; all original rows remain, and the original complete functional is separately evaluated on the current complete field. Accurate coefficient inclusion is conditional on the same selected implicit branch; binary midpoint coefficients, normal roots, quadrature and geometry have no inherited error certificate.",
  source_sha256:Object.fromEntries(Object.entries(runtime).map(([name,r])=>[name,r.sha256])),
  runtime_source_roles:clone(pins),complete_source_constructors:clone(constructors),
  complete_parent_ready:parentReady,
  complete_source_reproducer:{name:"reproduce_radial_public_reference_sources.mjs",...constructors["reproduce_radial_public_reference_sources.mjs"],
   complete_output_source_count:21,original_complete_primitives:4,complete_derived_sources:17,complete_actual_source_roles:78},
  complete_numeric_parameter_provenance:{
   all_original_numeric_solver_angles_and_quadrature_parameters_retained:true,
   numerical_argument_changes:[],new_explicit_layout_argument:{option:"--current-radial-factor",value:"2"},
   reference_J:923,current_J:1845,M:160,full_N:2048,reference_legacy_rows:1845,current_legacy_rows:3689,
   reference_complete_rows:7377,current_native_rows:14753,complete_current_rows_include_all_missing_original_aliases:true,
   current_observation_weights_changed_and_common_parent_measure_separate:true,
   old_free_size:1333370,current_free_size:2666582,
   directions:1,maxiter:16,restoration_directions:4,restoration_maxiter:64,normal_stages:32,
   outer_radial_Gauss_order:8,seed_radial_Gauss_order:8,
   parent_science_words:original.steps[0].args.length,current_science_words:steps[0].args.length,
   parent_pure_words:original.steps[1].args.length,current_pure_words:steps[1].args.length,
   original_all_science_summary_selectors_retained:true,original_all_pure_summary_selectors_retained:true,
   science_summary_count:Object.keys(science).length,pure_summary_count:Object.keys(pure).length},
  complete_scientific_suffix:{
   original_sha256:"d4420ab62c512f350f6f6c2a12e47da5272ac8088b24f9fe338fd9cb3a316376",
   current_sha256:"41075095653c8d7f5bceed1f3d85e8708f67b0a3180ee73369b5d4b08dea9bcf",
   original_bytes:19574,current_bytes:20488,entire_save_report_through_EOF_byte_identical:false,
   complete_original_suffix_restored_by_removing_only_two_declared_common_parent_statistics_insertions:true,
   common_parent_reread_uses_current_full_native_residual_not_an_old_report:true,
   both_original_record_only_packet_hooks_retained:true,
   original_Phase_I_QP_all_rows_all_trial_screens_retained:true},
  independent_branch:{
   mode:kind,actual_parent_source:parentDriver,actual_parent_reader:parentReader,
   complete_J923_parent_terminal_required:kind!=="independent",complete_actual_final_required:kind==="final",
   complete_parent_report:kind!=="independent"?parentReport:null,
   complete_parent_final:kind==="final"?parentFinal:null,actual_parent_report_sha256:null,actual_parent_final_sha256:null,
   actual_parent_field_has_not_been_fabricated:true,
   full_original_P0_old_grid_original_reference_grid_and_fine_grid_retained:true,
   all_read_parent_roles_and_uncapped_typed_lineage_transferred:true,
   unknown_peer_typed_state_or_order_claimed_to_have_been_read:false,
   all_original_three_rotation_blocks_and_each_0_1_2_node_jet_retained:true,
   midpoint_jets_from_original_complete_quintic_all_new_slots_free:true,
   frozen_reference_seed_not_reselected_from_parent_final:true,
   original_reference_initial_point_used:kind!=="final",
   all_current_initial_values_roots_geometry_and_finite_Phi_reread:true},
  source_only_checks:{
   complete_17_text_transformations_replayed_in_V8:true,
   original_complete_four_primitives_preserved_with_whole_SHA:true,
   complete_original_normal_class_byte_identical:true,
   complete_original_geometry_physical_suffix_byte_identical:true,
   complete_78_role_literal_registry_and_every_generated_source_pin_verified:true,
   unchanged_parent_source_roles_retain_all_published_whole_pins:true,
   full_source_Node_CLI_executed:false,Python_AST_or_compile_executed:false,
   selected_adjacent_guard_matches_actual_definition:true,
   current_geometry_C1_guard_matches_own_complete_helper:true,
   scientific_imports_or_F_J_root_quadrature_or_fixtures_executed_locally:false},
  actual_future_definition_or_field_sha256:null,
  actual_parent_run_status_note:"This package binds repaired ff544/aee22 whole sources. A complete returned parent report is required only in the two explicit transfer modes; a complete returned final is additionally required in final mode. No actual parent terminal or final was available to this constructor. Explicit independent mode keeps the unknown peer obligations and rereads the original fixed-reference point.",
  new_radial_input_cost_and_error_scope:{
   constructed_inside_actual_complete_base_setup_before_first_field:true,
   current_table_rebuilt_to_its_actual_preparation_leaf_count_with_full_metadata_equality_except_elapsed:true,
   a_values_recomputed_for_every_native_and_retained_original_query:true,
   every_original_7377_a_word_must_be_reproduced:true,
   historical_2397_table_substituted_for_current_table:false,
   all_actual_a_integral_remainders_and_node_carrier_errors_saved:true,
   requested_integral_accuracy_boolean_is_not_upgraded:true,
   no_table_or_field_result_fabricated:true,
   setup_may_fail_before_the_first_scientific_report:true,
   exact_input_mapping_is_not_a_complete_F_J_root_or_geometry_error_enclosure:true,
   five_full_input_files_retained_on_runner:true},
  limitations:"No local science, accepted J1845 field, complete continuous root or geometry certificate, same branch for an arbitrary injected parent, midpoint coefficient error enclosure, M/N refinement, cross-run target equivalence, bitwise field preservation after changing the radial basis/integration, or measured speedup is claimed.",
  steps
 });
 result.actual_failure_and_exact_repair={
  complete_evidence_source:parentReady,complete_evidence_field:"actual_failure_and_exact_repair",
  actual_log_bytes:6387,actual_log_sha256:"33671079a8ece2456621239ad80e51b7b8e3ff91aa3116b016391780319671de",
  missing_key:"all_original_stage_equations_roots_Newton_J3_and_angular_solves_retained",
  actual_key:"all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained",
  old_science_report_produced:false,old_pure_readout_produced:false,repaired_scientific_success_inferred:false};
 Object.assign(result.unreturned_peer_evidence["45909290354/1"],{
  actual_API_observation_time_UTC:"2026-11-27T05:02:15Z",actual_API_updated_at_UTC:"2026-11-27T05:00:28Z",
  scientific_child_termination_time_UTC:null,scientific_child_termination_cause:null,
  observation_time_is_not_scientific_child_end_time:true});
 if(kind==="independent")result.unreturned_peer_evidence["45943410994/1"]={
  driver_sha256:parentDriver,repaired_parent_terminal_report_consumed:false,
  complete_terminal_field_or_typed_state_read:false,prior_e3cb_attempt_report_absent:true,
  actual_unpaid_provenance_obligation_retained:true,unknown_is_not_empty:true};
 for(let i=0;i<2;i++)for(const[k,v]of Object.entries(Object.values(original.steps[i].summary)[0]))
  if(Object.values(steps[i].summary)[0][k]!==v)throw new Error("Original scalar selector removed or reinterpreted: "+k);
 if(Object.keys(science).length!==357||Object.keys(pure).length!==333)throw new Error("Retain all 333/317 selectors plus 24/16 actual radial scalar selectors");
 if(steps[0].args[steps[0].args.indexOf("--angles")+1]!=="2048"||
    steps[0].args[steps[0].args.indexOf("--integration-order")+1]!=="8"||
    steps[0].args[steps[0].args.indexOf("--normal-stages")+1]!=="32")
  throw new Error("The current radial refinement cannot shrink N, Gauss order or the selected normal chain");
 if(steps[0].args.length!=={independent:151,terminal:140,final:144}[kind]||steps[1].args.length!==7)
  throw new Error("The complete original parameter length changed unexpectedly");
 result.entry_source_sha256=Object.fromEntries(Object.entries(result.source_sha256).filter(([name])=>
  name==="fullclosed_radial_refined_public_reference_so3_qp.py"||
  name==="launch_radial_refined_public_reference_so3_actions.py"||
  name==="read_radial_refined_public_reference_so3_report.py"));
 delete result.source_sha256;
 result.complete_source_constructors=Object.fromEntries(Object.entries(constructors).map(([name,r])=>[name,{bytes:r.bytes,sha256:r.sha256}]));
 result.complete_source_reproducer={path:"scripts/resume_20261126/reproduce_radial_public_reference_sources.mjs",
  bytes:constructors["reproduce_radial_public_reference_sources.mjs"].bytes,
  sha256:constructors["reproduce_radial_public_reference_sources.mjs"].sha256,
  complete_output_source_count:21,complete_actual_source_roles:78};
 result.actual_producer_output_provenance={complete_file:parentReady,complete_field:"actual_producer_outputs",
  complete_output_record_count:original.actual_producer_outputs.length,
  all_original_output_records_and_actual_whole_binding_still_required:true};
 delete result.actual_producer_outputs;
 result.complete_parent_repair_evidence={complete_file:parentReady,
  complete_fields:["actual_failure_and_exact_repair","repair_parameter_provenance"],
  the_same_repaired_ff544_aee22_source_pair_is_required:true,repaired_success_inferred:false};
 delete result.actual_failure_and_exact_repair;
 delete result.repair_parameter_provenance;
 return result;
}

function readyMain(){
 const args={};
 for(let i=2;i<process.argv.length;i++){
  const k=process.argv[i];
  if(k==="--verify-existing")args.verify=true;
  else if(k==="--repo"||k==="--outdir"){if(!process.argv[i+1]||args[k.slice(2)])throw new Error("Missing or duplicate argument");args[k.slice(2)]=path.resolve(process.argv[++i]);}
  else throw new Error("Unknown source-only argument "+k);
 }
 if(!args.repo||(!args.outdir&&!args.verify))throw new Error("Use --repo REPO and --outdir EMPTY_SCRATCH or --verify-existing");
 const hash=s=>crypto.createHash("sha256").update(s).digest("hex");
 const read=(where,wanted)=>{const data=fs.readFileSync(where);if(data.length!==wanted.bytes||hash(data)!==wanted.sha256)throw new Error("Changed complete source "+where);return data.toString("utf8");};
 const topic=path.join(args.repo,"topics/visible-flex-larger-amplitude"),scripts=path.join(topic,"scripts/resume_20261126");
 const original=JSON.parse(read(path.join(topic,PARENT_READY.path),PARENT_READY));
 const constructors={};
 for(const [name,record]of Object.entries(OTHER_CONSTRUCTORS)){read(path.join(scripts,name),record);constructors[name]=record;}
 const own=fs.readFileSync(fileURLToPath(import.meta.url));
 constructors["make_radial_public_reference_ready.mjs"]={name:"make_radial_public_reference_ready.mjs",bytes:own.length,sha256:hash(own)};
 for(const[name,record]of Object.entries(RUNTIME))read(path.join(scripts,name),record);
 const generated={};
 for(const mode of ["independent","terminal","final"]){
  const name="public09-radial-J1845-analytic-frame-"+mode+"-ready.json";
  const value=buildRadialReady(original,RUNTIME,SOURCE_PINS,constructors,mode);
  const text=JSON.stringify(value)+"\n";
  if(Buffer.byteLength(text,"utf8")>=100000)throw new Error("Keep each complete small parameter file under 100 KB without removing arguments or selectors");
  if(Buffer.byteLength(JSON.stringify({finish:false,steps:value.steps})+"\n","utf8")>=95000)throw new Error("The complete two-step queue exceeds the controller size limit");
  generated[name]=text;
 }
 if(args.verify)for(const[name,text]of Object.entries(generated))
  if(fs.readFileSync(path.join(topic,"computations",name),"utf8")!==text)throw new Error("Changed complete existing plan "+name);
 if(args.outdir){
  const r=path.relative(args.repo,args.outdir);
  if(r===""||(!r.startsWith(".."+path.sep)&&r!==".."&&!path.isAbsolute(r)))throw new Error("Write only to scratch outside the repository");
  if(fs.existsSync(args.outdir)&&fs.readdirSync(args.outdir).length)throw new Error("Use an empty scratch directory");
  fs.mkdirSync(args.outdir,{recursive:true});
  for(const[name,text]of Object.entries(generated))fs.writeFileSync(path.join(args.outdir,name),text,{encoding:"utf8",flag:"wx"});
 }
 process.stdout.write(JSON.stringify({schema:"complete-public09-radial-parameter-construction-v1",
  scientific_execution:false,queue_mutated:false,parent_terminal_or_final_fabricated:false,
  actual_input_modes:["independent","terminal","final"],
  files:Object.fromEntries(Object.entries(generated).map(([name,text])=>[name,{bytes:Buffer.byteLength(text,"utf8"),sha256:hash(text)}]))},null,2)+"\n");
}

readyMain();
