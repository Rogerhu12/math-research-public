#!/usr/bin/env node
// Complete source and identity replay; no Python module, field, matrix or integral is executed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
const MODULES = [
 {
  "name": "derive_run10_radial_lower.mjs",
  "path": "scripts/resume_20261126/derive_run10_radial_lower.mjs",
  "sha256": "0d0a6c1c8e0ed57946d0dbaa121e08043a7aca9e3f993c4964ebf6430bb7f832",
  "bytes": 12518,
  "git_blob_sha": "39f5e04fd965c70121c2611e8d408b0cd637ee76",
  "complete_output_count": 9
 },
 {
  "name": "derive_run10_radial_memory_binding.mjs",
  "path": "scripts/resume_20261126/derive_run10_radial_memory_binding.mjs",
  "sha256": "38aec843677331a5c358ab770127b5d09a9278b3aceae22dd8b80c354c2f6f34",
  "bytes": 38150,
  "git_blob_sha": "f147c3a33c34ec60d506b5cf158b8fa78b405afc",
  "complete_output_count": 3
 },
 {
  "name": "derive_run10_radial_upper.mjs",
  "path": "scripts/resume_20261126/derive_run10_radial_upper.mjs",
  "sha256": "9143c2e1c1375af87ca988e0ad05dc746a1b77820e9db9450fb9235412da3ccd",
  "bytes": 60273,
  "git_blob_sha": "c11bf7859806f0c1c711a23ecbf5bc67589a1379",
  "complete_output_count": 5
 }
];
const OUTPUTS = [
 {
  "name": "run10_radial_detached_closure_values.py",
  "bytes": 54138,
  "sha256": "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb"
 },
 {
  "name": "run10_radial_analytic_stage_jacobian.py",
  "bytes": 25720,
  "sha256": "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b"
 },
 {
  "name": "run10_radial_analytic_normal_frame.py",
  "bytes": 47267,
  "sha256": "945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2"
 },
 {
  "name": "run10_radial_normal_frame_c1.py",
  "bytes": 37361,
  "sha256": "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2"
 },
 {
  "name": "run10_radial_detached_stage_matrices.py",
  "bytes": 47791,
  "sha256": "404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9"
 },
 {
  "name": "run10_radial_adjacent_normal_matrices.py",
  "bytes": 36766,
  "sha256": "7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37"
 },
 {
  "name": "run10_radial_reference_calibration.py",
  "bytes": 12769,
  "sha256": "cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b"
 },
 {
  "name": "so3_run10_radial_refined_closure_normal_lift.py",
  "bytes": 98434,
  "sha256": "ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c"
 },
 {
  "name": "immutable_run10_radial_normal_root_packets.py",
  "bytes": 71652,
  "sha256": "fa9f50d318af9ec268ce391b6ba16d8eb971d88ad519ae79c8ba3c661806f528"
 },
 {
  "name": "run10_radial_material_address_transfer.py",
  "bytes": 22097,
  "sha256": "e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b"
 },
 {
  "name": "run10_radial_refined_material_memory.py",
  "bytes": 59245,
  "sha256": "043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071"
 },
 {
  "name": "run10_radial_source_and_report_binding.py",
  "bytes": 48958,
  "sha256": "7536c4b1fb9085fe03a00be5da4073065b7abb98a3b2ee7b3d14833c478af415"
 },
 {
  "name": "transfer_run10_radial_refined_material_memory.py",
  "bytes": 87074,
  "sha256": "8cd8a25830518bc29f80b22dc26e1f611e145566a7cd5fd0bf8e4f758304bb3b"
 },
 {
  "name": "so3_run10_radial_refined_envelope_geometry.py",
  "bytes": 71804,
  "sha256": "a55a42c8d577dd4589425680c4a37eeb8e17d80de09a02215b3f424245c7f8e9"
 },
 {
  "name": "fullclosed_run10_radial_refined_so3_qp.py",
  "bytes": 93101,
  "sha256": "2693abdb070cb62584abb3ffceeb525854c62d47379c9349d9047a0a365fe4e5"
 },
 {
  "name": "launch_run10_radial_refined_actions.py",
  "bytes": 22614,
  "sha256": "b71588c0323c96970abedbe1b495429295f4bd44de01b921486123b6cfbf861e"
 },
 {
  "name": "read_run10_radial_refined_so3_report.py",
  "bytes": 97943,
  "sha256": "64e92ed8b48f753e9988221c2c1f91513ed2e468e6fff3ce9cc83096c4bad8e4"
 }
];
const SHARED = [
 {
  "name": "radial_bisection_layout.py",
  "path": "scripts/resume_20261126/radial_bisection_layout.py",
  "bytes": 18923,
  "sha256": "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744",
  "git_blob_sha": "50304523b343957632dc25de61de403b8ca3bad4"
 },
 {
  "name": "exact_affine_supported_reference.py",
  "path": "scripts/resume_20261126/exact_affine_supported_reference.py",
  "bytes": 23435,
  "sha256": "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117",
  "git_blob_sha": "1c7f9ddde0b94692b792cca40cf466046e30ed5b"
 },
 {
  "name": "complete_dyadic_radial_observations.py",
  "path": "scripts/resume_20261126/complete_dyadic_radial_observations.py",
  "bytes": 28167,
  "sha256": "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74",
  "git_blob_sha": "e7ab1d8f3a52720e484fc4531156d8e233d592ab"
 },
 {
  "name": "so3_radial_refined_public_reference_meridian_operator.py",
  "path": "scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py",
  "bytes": 45749,
  "sha256": "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0",
  "git_blob_sha": "9851a696fea6d07690d61dbe23452c185fc4485d"
 },
 {
  "name": "radial_refined_public_reference_literal_zero_moment_input.py",
  "path": "scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py",
  "bytes": 35736,
  "sha256": "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652",
  "git_blob_sha": "3322530f8cf16214cb3e6c11ca368d56b9af44d9"
 }
];
const SOURCE_ROLES = {
 "actual_public_input_binding": [
  "scripts/resume_20261126/actual_public_run10_reference_input_binding.py",
  "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209"
 ],
 "adjacent_matrices": [
  "scripts/resume_20261126/run10_radial_adjacent_normal_matrices.py",
  "7477da02b225834cc1f0dae147d0bca53a3b40398ee04cdf0dfc7f0217483a37"
 ],
 "analytic_frame": [
  "scripts/resume_20261126/run10_radial_analytic_normal_frame.py",
  "945b66100801058d311f215c9453efa35a9cbb3edf031dc1b10da0140f9567f2"
 ],
 "analytic_J3": [
  "scripts/resume_20261126/run10_radial_analytic_stage_jacobian.py",
  "7bbc3384dae0f791992835ceacdbc78ace50101ef9b5291b67d72ea2afd9425b"
 ],
 "analytic_J3_binding": [
  "scripts/resume_20261126/run10_radial_source_and_report_binding.py",
  "7536c4b1fb9085fe03a00be5da4073065b7abb98a3b2ee7b3d14833c478af415"
 ],
 "analytic_parent_adjacent_matrices": [
  "scripts/resume_20261126/adjacent_normal_frame_matrices.py",
  "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3"
 ],
 "analytic_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py",
  "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"
 ],
 "analytic_parent_frame_C1": [
  "scripts/resume_20261126/normal_frame_c1_reuse.py",
  "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"
 ],
 "analytic_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py",
  "f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470"
 ],
 "analytic_parent_stage_matrices": [
  "scripts/resume_20261126/detached_normal_stage_matrix_reuse.py",
  "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59"
 ],
 "axisymmetric_seed_driver": [
  "scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py",
  "606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9"
 ],
 "centered": [
  "scripts/resume_20261126/centered_spectral_statistics.py",
  "5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01"
 ],
 "closure_values": [
  "scripts/resume_20261126/run10_radial_detached_closure_values.py",
  "61368668228dc9a90b24c4e88a692c5759214add2b733fe10a882acb2ce8f6eb"
 ],
 "deep_scalar": [
  "scripts/resume_20261126/deep_valley_tail_input.py",
  "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"
 ],
 "endpoint": [
  "scripts/resume_20261126/so3_run10_radial_refined_closure_normal_lift.py",
  "ffbbddc9047b36cd308ed79df7ad4669185f61e71d85caef9a14f37b8292a40c"
 ],
 "envelope_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory.py",
  "c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152"
 ],
 "envelope_parent_calibration": [
  "scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py",
  "3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991"
 ],
 "envelope_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py",
  "cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"
 ],
 "envelope_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py",
  "a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd"
 ],
 "envelope_parent_geometry": [
  "scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py",
  "bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f"
 ],
 "envelope_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py",
  "104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7"
 ],
 "envelope_rows": [
  "scripts/resume_20261126/complete_material_envelope_rows.py",
  "729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7"
 ],
 "envelope_transfer": [
  "scripts/resume_20261126/transfer_run10_radial_refined_material_memory.py",
  "8cd8a25830518bc29f80b22dc26e1f611e145566a7cd5fd0bf8e4f758304bb3b"
 ],
 "frame_C1": [
  "scripts/resume_20261126/run10_radial_normal_frame_c1.py",
  "976f638b104c0b95233c9238eec3440baf6b31910f1a943fea99f114f2ccdbe2"
 ],
 "frame_parent_adjacent_matrices": [
  "scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py",
  "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"
 ],
 "frame_parent_C1": [
  "scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py",
  "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"
 ],
 "frame_parent_calibration": [
  "scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py",
  "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"
 ],
 "frame_parent_driver": [
  "scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py",
  "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51"
 ],
 "frame_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py",
  "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"
 ],
 "frame_parent_J3": [
  "scripts/resume_20261126/analytic_normal_stage_jacobian.py",
  "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"
 ],
 "frame_parent_reader": [
  "scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py",
  "c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e"
 ],
 "frame_parent_stage_matrices": [
  "scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py",
  "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"
 ],
 "frozen_moment_input": [
  "scripts/resume_20261126/frozen_zero_moment_input.py",
  "4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611"
 ],
 "geometry": [
  "scripts/resume_20261126/so3_run10_radial_refined_envelope_geometry.py",
  "a55a42c8d577dd4589425680c4a37eeb8e17d80de09a02215b3f424245c7f8e9"
 ],
 "geometry_selector": [
  "scripts/resume_20261120/fullclosed_point_inequalities_v2.py",
  "e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8"
 ],
 "hessian": [
  "scripts/resume_20261120/positive_spectral_gram_hessian.py",
  "29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4"
 ],
 "history": [
  "scripts/resume_20261120/launch_refinement_from_full_report.py",
  "4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"
 ],
 "hold": [
  "scripts/parallel_20261117_negative_hold_profile_ivp.py",
  "ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"
 ],
 "independent_envelope_memory": [
  "scripts/resume_20261126/run10_radial_refined_material_memory.py",
  "043d451e34890c522de17be687306898f2f18ec8451d1814ab75730eea687071"
 ],
 "independent_input_projection_producer": [
  "scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py",
  "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a"
 ],
 "integer": [
  "notes/2026-11-17-parallel-inward-integral-enclosure.py",
  "babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"
 ],
 "meridian": [
  "scripts/resume_20261126/so3_radial_refined_public_reference_meridian_operator.py",
  "130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0"
 ],
 "moment_initial_binding": [
  "scripts/resume_20261126/diagnose_zero_initial_chord.py",
  "65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0"
 ],
 "moment_original_driver": [
  "scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py",
  "b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b"
 ],
 "moment_original_endpoint": [
  "scripts/resume_20261126/so3_zero_closure_endpoint_operator.py",
  "5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46"
 ],
 "moment_trace_source": [
  "scripts/resume_20261126/trace_zero_initial_endpoint_failure.py",
  "73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54"
 ],
 "new_moment_input": [
  "scripts/resume_20261126/radial_refined_public_reference_literal_zero_moment_input.py",
  "59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652"
 ],
 "observed": [
  "scripts/resume_20261120/gauss_observed_closed_gram.py",
  "26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"
 ],
 "pure_geometry": [
  "scripts/resume_20261120_curvature_qp.py",
  "a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854"
 ],
 "qp": [
  "scripts/resume_20261120/fullspace_feasible_active_cg_v3.py",
  "fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"
 ],
 "radial_address_transfer": [
  "scripts/resume_20261126/run10_radial_material_address_transfer.py",
  "e27e2f333e2a24279af84d6e015835420355b2fb446dbd56b99e99e68d40374b"
 ],
 "radial_affine_reference": [
  "scripts/resume_20261126/exact_affine_supported_reference.py",
  "2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117"
 ],
 "radial_layout": [
  "scripts/resume_20261126/radial_bisection_layout.py",
  "cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744"
 ],
 "radial_observations": [
  "scripts/resume_20261126/complete_dyadic_radial_observations.py",
  "2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74"
 ],
 "radial_parent_adjacent_matrices": [
  "scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py",
  "3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"
 ],
 "radial_parent_analytic_frame": [
  "scripts/resume_20261126/analytic_normal_frame_jets.py",
  "4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"
 ],
 "radial_parent_analytic_J3": [
  "scripts/resume_20261126/analytic_frame_local_stage_jacobian.py",
  "894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"
 ],
 "radial_parent_analytic_J3_binding": [
  "scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py",
  "15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"
 ],
 "radial_parent_driver": [
  "scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",
  "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
 ],
 "radial_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py",
  "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"
 ],
 "radial_parent_envelope_transfer": [
  "scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py",
  "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"
 ],
 "radial_parent_frame_C1": [
  "scripts/resume_20261126/analytic_frame_c1_reuse.py",
  "f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"
 ],
 "radial_parent_geometry": [
  "scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py",
  "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"
 ],
 "radial_parent_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory_public_reference.py",
  "2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"
 ],
 "radial_parent_meridian": [
  "scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py",
  "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"
 ],
 "radial_parent_new_moment_input": [
  "scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py",
  "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"
 ],
 "radial_parent_reader": [
  "scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py",
  "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"
 ],
 "radial_parent_reference_calibration": [
  "scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py",
  "fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"
 ],
 "radial_parent_root_packets": [
  "scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py",
  "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"
 ],
 "radial_parent_stage_matrices": [
  "scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py",
  "fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"
 ],
 "reference": [
  "scripts/resume_20261126/so3_axisymmetric_reference.py",
  "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
 ],
 "reference_calibration": [
  "scripts/resume_20261126/run10_radial_reference_calibration.py",
  "cb440bfe32830f5a479e466fec8439e9bde88bfbb4160e534f899f999bac573b"
 ],
 "root_packets": [
  "scripts/resume_20261126/immutable_run10_radial_normal_root_packets.py",
  "fa9f50d318af9ec268ce391b6ba16d8eb971d88ad519ae79c8ba3c661806f528"
 ],
 "run10_parent_adjacent_matrices": [
  "scripts/resume_20261126/adjacent_normal_matrices_closure_values.py",
  "6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650"
 ],
 "run10_parent_analytic_frame": [
  "scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py",
  "8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598"
 ],
 "run10_parent_analytic_J3": [
  "scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py",
  "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa"
 ],
 "run10_parent_analytic_J3_binding": [
  "scripts/resume_20261126/run10_detached_closure_value_binding.py",
  "dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1"
 ],
 "run10_parent_closure_parent_actual_public_input_binding": [
  "scripts/resume_20261126/actual_public_reference_input_binding.py",
  "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"
 ],
 "run10_parent_closure_parent_independent_input_projection_producer": [
  "scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py",
  "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"
 ],
 "run10_parent_closure_values": [
  "scripts/resume_20261126/same_chain_detached_closure_values.py",
  "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e"
 ],
 "run10_parent_driver": [
  "scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py",
  "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"
 ],
 "run10_parent_endpoint": [
  "scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py",
  "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"
 ],
 "run10_parent_envelope_transfer": [
  "scripts/resume_20261126/transfer_run10_detached_closure_memory.py",
  "eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe"
 ],
 "run10_parent_frame_C1": [
  "scripts/resume_20261126/normal_frame_c1_closure_values.py",
  "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa"
 ],
 "run10_parent_geometry": [
  "scripts/resume_20261126/so3_run10_detached_closure_geometry.py",
  "6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528"
 ],
 "run10_parent_independent_envelope_memory": [
  "scripts/resume_20261126/complete_material_envelope_memory_public_run10.py",
  "f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba"
 ],
 "run10_parent_reader": [
  "scripts/resume_20261126/read_run10_detached_closure_so3_report.py",
  "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"
 ],
 "run10_parent_reference_calibration": [
  "scripts/resume_20261126/reference_centred_closure_values_calibration.py",
  "b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f"
 ],
 "run10_parent_root_packets": [
  "scripts/resume_20261126/immutable_closure_values_normal_root_packets.py",
  "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"
 ],
 "run10_parent_stage_matrices": [
  "scripts/resume_20261126/detached_stage_matrices_closure_values.py",
  "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45"
 ],
 "scalar": [
  "notes/2026-11-17-parallel-model-full-hold-oracle.py",
  "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"
 ],
 "seed_mean": [
  "scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py",
  "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
 ],
 "seed_reference": [
  "scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py",
  "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"
 ],
 "spectral": [
  "scripts/resume_20261120/positive_spectral_gram_weights.py",
  "e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91"
 ],
 "stage_matrices": [
  "scripts/resume_20261126/run10_radial_detached_stage_matrices.py",
  "404ecb970b37b37fd00863c52564ac1ec784c902d7f5123cc5317d77976336c9"
 ],
 "warm_producer": [
  "notes/2026-11-17-parallel-model-fullclosed-hold-warm.py",
  "bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3"
 ]
};
const digest=text=>({bytes:Buffer.byteLength(text,'utf8'),sha256:crypto.createHash('sha256').update(text,'utf8').digest('hex')});
const equal=(a,b)=>a.bytes===b.bytes&&a.sha256===b.sha256;
function readBound(filename,record) {
 const text=fs.readFileSync(filename,'utf8');
 if(!equal(digest(text),record))throw new Error('Whole file identity differs: '+filename);
 return text;
}
function section(text,start) {
 const at=text.indexOf(start);
 if(at<0||text.indexOf(start,at+1)>=0)throw new Error('One complete source section is required: '+start);
 return text.slice(at);
}
function methodBodies(text) {
 const lines=text.split(/(?<=\n)/),out=new Map();
 for(let i=0;i<lines.length;i++) {
  const found=/^    def (\w+)\(/.exec(lines[i]);if(!found)continue;
  let end=i+1;
  while(end<lines.length&&!/^(    (?:def |@)|class |def |if __name__)/.test(lines[end]))end++;
  out.set(found[1],lines.slice(i,end).join(''));
 }
 return out;
}
function topFunction(text,name) {
 const at=text.indexOf('def '+name+'(');
 if(at<0)throw new Error('Missing complete function '+name);
 const rest=text.slice(at),next=/\n(?:(?:async )?def |class |if __name__)/.exec(rest);
 return next?rest.slice(0,next.index+1):rest;
}
export async function replay({repo,out,verifyExisting=false}) {
 const root=path.resolve(repo),topic=path.join(root,'topics/visible-flex-larger-amplitude');
 const target=path.resolve(out),sourceDirectory=path.dirname(fileURLToPath(import.meta.url));
 if(target===root||target.startsWith(root+path.sep))throw new Error('Use an independent scratch output directory; this tool does not edit repository sources');
 const generated=new Map();
 for(const record of MODULES) {
  const filename=path.join(sourceDirectory,record.name);
  readBound(filename,record);
  const module=await import(pathToFileURL(filename).href);
  for(const [name,text]of module.build(relative=>fs.readFileSync(path.join(topic,relative),'utf8'))) {
   if(generated.has(name))throw new Error('Duplicate whole source '+name);
   generated.set(name,text);
  }
 }
 if(generated.size!==OUTPUTS.length)throw new Error('The complete output family is required');
 for(const record of OUTPUTS)if(!generated.has(record.name)||!equal(digest(generated.get(record.name)),record))throw new Error('Missing complete derived body '+record.name);
 for(const record of SHARED)readBound(path.join(topic,record.path),record);
 let roles=0;
 for(const [role,[relative,sha256]]of Object.entries(SOURCE_ROLES)) {
  const basename=path.basename(relative);
  const text=generated.has(basename)?generated.get(basename):fs.readFileSync(path.join(topic,relative),'utf8');
  if(digest(text).sha256!==sha256)throw new Error('Complete actual source role differs: '+role);
  roles++;
 }
 const normal=generated.get('so3_run10_radial_refined_closure_normal_lift.py');
 const parent=fs.readFileSync(path.join(topic,'scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py'),'utf8');
 const a=methodBodies(parent),b=methodBodies(normal);
 if(a.size!==52||b.size!==52||[...a].some(([name,body])=>b.get(name)!==body))throw new Error('All fifty-two actual run10 normal methods must remain verbatim');
 const geo=generated.get('so3_run10_radial_refined_envelope_geometry.py');
 const oldGeo=fs.readFileSync(path.join(topic,'scripts/resume_20261126/so3_radial_refined_public_reference_envelope_geometry.py'),'utf8');
 if(section(geo,'    def _set_x(')!==section(oldGeo,'    def _set_x('))throw new Error('The complete refined geometry body changed');
 const driver=generated.get('fullclosed_run10_radial_refined_so3_qp.py');
 const oldDriver=fs.readFileSync(path.join(topic,'scripts/resume_20261126/fullclosed_radial_refined_public_reference_so3_qp.py'),'utf8');
 const progressLines=["        q.detached_closure_values.progress('initial-complete-residual-start',force=True)","        q.detached_closure_values.progress('initial-complete-residual-returned',force=True)","        q.detached_closure_values.progress('initial-complete-statistics-start',force=True)","        q.detached_closure_values.progress('initial-complete-statistics-returned',force=True)","        q.detached_closure_values.progress('initial-complete-geometry-start',force=True)","        q.detached_closure_values.progress('initial-complete-geometry-returned',force=True)"];
 let scientific=section(driver,'    def save_report():');
 for(const line of progressLines) {
  if(scientific.split(line+'\n').length!==2)throw new Error('One declared pure progress observation is required');
  scientific=scientific.replace(line+'\n','');
 }
 if(scientific!==section(oldDriver,'    def save_report():'))throw new Error('The complete radial solver suffix changed beyond the declared six progress observations');
 const launcher=generated.get('launch_run10_radial_refined_actions.py');
 const launchArgs=topFunction(launcher,'parse_args').split('\n').filter(line=>!line.includes("p.add_argument('--install-torch'")&&!line.includes("p.add_argument('--print-command'")).join('\n');
 if(launchArgs!==topFunction(driver,'parse_args'))throw new Error('Launcher/driver complete arguments differ');
 if(verifyExisting) {
  for(const record of OUTPUTS)readBound(path.join(target,record.name),record);
 } else {
  fs.mkdirSync(target,{recursive:true});
  for(const record of OUTPUTS) {
   const file=path.join(target,record.name);
   if(fs.existsSync(file)&&fs.readFileSync(file,'utf8')!==generated.get(record.name))throw new Error('Refuse to overwrite different scratch bytes '+file);
   fs.writeFileSync(file,generated.get(record.name),'utf8');
  }
 }
 return {schema:'run10-complete-J1845-source-replay-v1',complete_new_runtime_count:OUTPUTS.length,
  shared_original_complete_runtime_count:SHARED.length,complete_current_source_role_count:roles,
  all_normal_methods_verbatim:52,complete_radial_geometry_body_verbatim:true,
  complete_radial_scientific_suffix_restored_after_six_progress_lines:true,
  complete_launcher_arguments_equal:true,all_output_whole_SHA256_verified:true,
  Python_AST_compile_or_scientific_imports_executed:false,scientific_evaluations:0,
  source_outputs:OUTPUTS,shared_sources:SHARED};
}
async function main() {
 const args=process.argv.slice(2),values={};
 for(let i=0;i<args.length;i++) {
  if(args[i]==='--verify-existing')values.verifyExisting=true;
  else if(args[i]==='--repo'||args[i]==='--out')values[args[i].slice(2)]=args[++i];
  else if(args[i]==='--help') {console.log('node reproduce_run10_radial_sources.mjs --repo REPO --out SCRATCH [--verify-existing]');return;}
  else throw new Error('Unknown source-only argument '+args[i]);
 }
 if(!values.repo||!values.out)throw new Error('Require the complete repository and independent scratch directory');
 console.log(JSON.stringify(await replay(values),null,2));
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await main();
