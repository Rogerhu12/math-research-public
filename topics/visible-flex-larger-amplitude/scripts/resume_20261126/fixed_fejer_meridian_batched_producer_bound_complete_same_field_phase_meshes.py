#!/usr/bin/env python3
"""Full same-field fixed Fejer closed meshes and genuine spatial/time readouts.

This is a scientific public-Actions consumer, not an optimizer or a continuous
certificate. It reconstructs the complete original q and reads an actual full
point. Every original radial cell and the full angular circle are retained.
Raw six-jets, root packets, all closed meshes and comparison records stay on
the runner. Only complete source/parameters and scalar results belong in Git.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback

SCHEMA = "actual-fixed-fejer-meridian-batched-producer-bound-complete-same-field-closed-phase-mesh-refinement-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
SOURCE_PINS = {
    "root_packets": [
        "scripts/resume_20261126/fixed_fejer_meridian_root_packets.py",
        "c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4"
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
        "scripts/resume_20261126/fixed_fejer_meridian_analytic_stage_jacobian.py",
        "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811"
    ],
    "analytic_J3_binding": [
        "scripts/resume_20261126/fixed_fejer_meridian_source_binding.py",
        "3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68"
    ],
    "analytic_parent_frame_C1": [
        "scripts/resume_20261126/normal_frame_c1_reuse.py",
        "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"
    ],
    "seed_reference": [
        "scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py",
        "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a"
    ],
    "seed_mean": [
        "scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py",
        "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"
    ],
    "reference": [
        "scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
        "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
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
        "scripts/resume_20261126/fixed_fejer_supported_so3_meridian_operator.py",
        "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3"
    ],
    "geometry": [
        "scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
        "5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135"
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
        "scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
        "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d"
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
        "scripts/resume_20261126/fixed_fejer_literal_zero_moment_input.py",
        "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3"
    ],
    "reference_calibration": [
        "scripts/resume_20261126/fixed_fejer_meridian_reference_calibration.py",
        "aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3"
    ],
    "frame_C1": [
        "scripts/resume_20261126/fixed_fejer_meridian_normal_frame_c1.py",
        "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246"
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
        "scripts/resume_20261126/fixed_fejer_meridian_stage_matrices.py",
        "f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791"
    ],
    "envelope_transfer": [
        "scripts/resume_20261126/fixed_fejer_meridian_memory_transfer.py",
        "b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc"
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
        "scripts/resume_20261126/fixed_fejer_meridian_adjacent_matrices.py",
        "bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564"
    ],
    "independent_envelope_memory": [
        "scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py",
        "9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a"
    ],
    "independent_input_projection_producer": [
        "scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
        "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
    ],
    "analytic_frame": [
        "scripts/resume_20261126/fixed_fejer_meridian_analytic_normal_frame.py",
        "d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd"
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
        "scripts/resume_20261126/fixed_fejer_reference_input_binding.py",
        "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"
    ],
    "closure_values": [
        "scripts/resume_20261126/fixed_fejer_meridian_closure_values.py",
        "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0"
    ],
    "closure_parent_analytic_J3": [
        "scripts/resume_20261126/analytic_frame_local_stage_jacobian.py",
        "894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"
    ],
    "closure_parent_analytic_frame": [
        "scripts/resume_20261126/analytic_normal_frame_jets.py",
        "4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"
    ],
    "closure_parent_frame_C1": [
        "scripts/resume_20261126/analytic_frame_c1_reuse.py",
        "f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"
    ],
    "closure_parent_stage_matrices": [
        "scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py",
        "fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"
    ],
    "closure_parent_adjacent_matrices": [
        "scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py",
        "3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"
    ],
    "closure_parent_reference_calibration": [
        "scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py",
        "fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"
    ],
    "closure_parent_endpoint": [
        "scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py",
        "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"
    ],
    "closure_parent_root_packets": [
        "scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py",
        "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"
    ],
    "closure_parent_analytic_J3_binding": [
        "scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py",
        "15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"
    ],
    "closure_parent_geometry": [
        "scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py",
        "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"
    ],
    "closure_parent_envelope_transfer": [
        "scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py",
        "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"
    ],
    "closure_parent_driver": [
        "scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py",
        "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
    ],
    "closure_parent_reader": [
        "scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py",
        "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"
    ],
    "closure_parent_independent_envelope_memory": [
        "scripts/resume_20261126/complete_material_envelope_memory_public_reference.py",
        "2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"
    ],
    "closure_parent_independent_input_projection_producer": [
        "scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py",
        "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"
    ],
    "closure_parent_actual_public_input_binding": [
        "scripts/resume_20261126/actual_public_reference_input_binding.py",
        "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"
    ],
    "immutable_point_parent_closure_values": [
        "scripts/resume_20261126/same_chain_detached_closure_values.py",
        "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e"
    ],
    "immutable_point_parent_analytic_J3": [
        "scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py",
        "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa"
    ],
    "immutable_point_parent_analytic_frame": [
        "scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py",
        "8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598"
    ],
    "immutable_point_parent_frame_C1": [
        "scripts/resume_20261126/normal_frame_c1_closure_values.py",
        "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa"
    ],
    "immutable_point_parent_stage_matrices": [
        "scripts/resume_20261126/detached_stage_matrices_closure_values.py",
        "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45"
    ],
    "immutable_point_parent_adjacent_matrices": [
        "scripts/resume_20261126/adjacent_normal_matrices_closure_values.py",
        "6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650"
    ],
    "immutable_point_parent_reference_calibration": [
        "scripts/resume_20261126/reference_centred_closure_values_calibration.py",
        "b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f"
    ],
    "immutable_point_parent_endpoint": [
        "scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py",
        "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"
    ],
    "immutable_point_parent_root_packets": [
        "scripts/resume_20261126/immutable_closure_values_normal_root_packets.py",
        "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"
    ],
    "immutable_point_parent_binding": [
        "scripts/resume_20261126/run10_detached_closure_value_binding.py",
        "dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1"
    ],
    "immutable_point_parent_geometry": [
        "scripts/resume_20261126/so3_run10_detached_closure_geometry.py",
        "6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528"
    ],
    "immutable_point_parent_envelope_transfer": [
        "scripts/resume_20261126/transfer_run10_detached_closure_memory.py",
        "eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe"
    ],
    "immutable_point_parent_driver": [
        "scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py",
        "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"
    ],
    "immutable_point_parent_reader": [
        "scripts/resume_20261126/read_run10_detached_closure_so3_report.py",
        "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"
    ],
    "immutable_point_parent_launcher": [
        "scripts/resume_20261126/launch_run10_detached_closure_actions.py",
        "22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604"
    ],
    "fixed_fejer_previous_closure_values": [
        "scripts/resume_20261126/immutable_point_detached_closure_values.py",
        "2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb"
    ],
    "fixed_fejer_previous_analytic_J3": [
        "scripts/resume_20261126/analytic_local_stage_jacobian_immutable_point.py",
        "21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024"
    ],
    "fixed_fejer_previous_analytic_frame": [
        "scripts/resume_20261126/analytic_normal_frame_jets_immutable_point.py",
        "4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa"
    ],
    "fixed_fejer_previous_frame_C1": [
        "scripts/resume_20261126/normal_frame_c1_immutable_point.py",
        "53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d"
    ],
    "fixed_fejer_previous_stage_matrices": [
        "scripts/resume_20261126/detached_stage_matrices_immutable_point.py",
        "a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052"
    ],
    "fixed_fejer_previous_adjacent_matrices": [
        "scripts/resume_20261126/adjacent_normal_matrices_immutable_point.py",
        "ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59"
    ],
    "fixed_fejer_previous_reference_calibration": [
        "scripts/resume_20261126/reference_centred_immutable_point_calibration.py",
        "794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238"
    ],
    "fixed_fejer_previous_endpoint": [
        "scripts/resume_20261126/so3_reference_centred_immutable_point_normal_lift_operator.py",
        "9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6"
    ],
    "fixed_fejer_previous_root_packets": [
        "scripts/resume_20261126/immutable_point_normal_root_packets.py",
        "b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8"
    ],
    "fixed_fejer_previous_reference": [
        "scripts/resume_20261126/so3_axisymmetric_reference.py",
        "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
    ],
    "fixed_fejer_previous_seed_reference": [
        "scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py",
        "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"
    ],
    "fixed_fejer_previous_meridian": [
        "scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py",
        "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"
    ],
    "fixed_fejer_previous_new_moment_input": [
        "scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py",
        "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"
    ],
    "fixed_fejer_previous_analytic_J3_binding": [
        "scripts/resume_20261126/run10_immutable_point_source_binding.py",
        "85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97"
    ],
    "fixed_fejer_previous_geometry": [
        "scripts/resume_20261126/so3_run10_immutable_point_geometry.py",
        "dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce"
    ],
    "fixed_fejer_previous_envelope_transfer": [
        "scripts/resume_20261126/transfer_run10_immutable_point_memory.py",
        "0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486"
    ],
    "fixed_fejer_previous_independent_envelope_memory": [
        "scripts/resume_20261126/complete_material_envelope_memory_public_run10.py",
        "f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba"
    ],
    "fixed_fejer_previous_independent_input_projection_producer": [
        "scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py",
        "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a"
    ],
    "fixed_fejer_previous_actual_public_input_binding": [
        "scripts/resume_20261126/actual_public_run10_reference_input_binding.py",
        "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209"
    ],
    "fixed_input_producer": [
        "scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
        "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
    ],
    "stage_point_parent_root_packets": [
        "scripts/resume_20261126/fixed_fejer_immutable_normal_root_packets.py",
        "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468"
    ],
    "stage_point_parent_stage_matrices": [
        "scripts/resume_20261126/fixed_fejer_detached_stage_matrices.py",
        "7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7"
    ],
    "stage_point_parent_adjacent_matrices": [
        "scripts/resume_20261126/fixed_fejer_adjacent_normal_matrices.py",
        "257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0"
    ],
    "stage_point_parent_endpoint": [
        "scripts/resume_20261126/fixed_fejer_normal_lift_operator.py",
        "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778"
    ],
    "stage_point_parent_binding": [
        "scripts/resume_20261126/fixed_fejer_complete_source_binding.py",
        "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88"
    ],
    "stage_point_parent_envelope_transfer": [
        "scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py",
        "af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566"
    ],
    "stage_point_parent_geometry": [
        "scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py",
        "bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26"
    ],
    "stage_point_parent_driver": [
        "scripts/resume_20261126/fullclosed_fixed_fejer_immutable_point_so3_qp.py",
        "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
    ],
    "stage_point_parent_reader": [
        "scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py",
        "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b"
    ],
    "scalar_progress": [
        "scripts/resume_20261126/fixed_fejer_complete_geometry_trial_progress.py",
        "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5"
    ],
    "meridian_parent_analytic_J3": [
        "scripts/resume_20261126/fixed_fejer_analytic_stage_jacobian.py",
        "7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72"
    ],
    "meridian_parent_frame_C1": [
        "scripts/resume_20261126/fixed_fejer_normal_frame_c1.py",
        "1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca"
    ],
    "meridian_parent_stage_matrices": [
        "scripts/resume_20261126/fixed_fejer_immutable_point_stage_matrices.py",
        "e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce"
    ],
    "meridian_parent_adjacent_matrices": [
        "scripts/resume_20261126/fixed_fejer_stage_point_adjacent_matrices.py",
        "d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5"
    ],
    "meridian_parent_reference_calibration": [
        "scripts/resume_20261126/fixed_fejer_reference_calibration.py",
        "fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c"
    ],
    "meridian_parent_endpoint": [
        "scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py",
        "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10"
    ],
    "meridian_parent_analytic_frame": [
        "scripts/resume_20261126/fixed_fejer_analytic_normal_frame.py",
        "75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c"
    ],
    "meridian_parent_closure_values": [
        "scripts/resume_20261126/fixed_fejer_immutable_closure_values.py",
        "01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595"
    ],
    "detached_meridian_values": [
        "scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
        "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de"
    ],
    "meridian_parent_root_packets": [
        "scripts/resume_20261126/fixed_fejer_stage_point_root_packets.py",
        "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf"
    ],
    "meridian_parent_analytic_J3_binding": [
        "scripts/resume_20261126/fixed_fejer_stage_point_source_binding.py",
        "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f"
    ],
    "meridian_parent_geometry": [
        "scripts/resume_20261126/so3_fixed_fejer_stage_point_geometry.py",
        "2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471"
    ],
    "meridian_parent_envelope_transfer": [
        "scripts/resume_20261126/transfer_fixed_fejer_stage_point_memory.py",
        "afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed"
    ],
    "meridian_parent_scalar_progress": [
        "scripts/resume_20261126/fixed_fejer_actual_mathematical_progress.py",
        "bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391"
    ],
    "batched_geometry_binding": [
        "scripts/resume_20261126/fixed_fejer_batched_geometry_report_binding.py",
        "9104c29d03a589939f46ccdb08a55a3564f702acd147840cc91488b72eee2d06"
    ],
    "meridian_parent_driver": [
        "scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
        "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d"
    ],
    "meridian_parent_reader": [
        "scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py",
        "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f"
    ],
    "mesh_input": [
        "scripts/resume_20261126/fixed_fejer_meridian_batched_producer_bound_same_field_mesh_input.py",
        "2ef316b9075f14af66e1deda235c4df9319a0c29cfeddb10a40130712a12d76c"
    ],
    "mesh_arithmetic": [
        "scripts/resume_20261126/fixed_fejer_complete_phase_mesh_arithmetic.py",
        "80116a4bcfa2752274cece1148420cdce5c489faba3a8a7c0e92c0f6a8d058e4"
    ],
    "original_fixed_fejer_driver": [
        "scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
        "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
    ],
    "original_fixed_fejer_reader": [
        "scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py",
        "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49"
    ],
    "original_fixed_fejer_launcher": [
        "scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py",
        "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506"
    ],
    "complete_accurate_input_scope": [
        "scripts/resume_20261126/fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
        "d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7"
    ],
    "optional_closed_phase_source": [
        "scripts/resume_20261126/fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
        "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f"
    ]
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda:stream.read(1<<20),b""):
            h.update(part)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path),bytes=path.stat().st_size,sha256=sha(path))


def load(name,path,expected):
    if sha(path) != expected:
        raise ValueError("Changed complete mesh implementation "+str(path))
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    if sha(path) != expected:
        raise ValueError("A complete mesh source changed while importing")
    return module


def atomic_json(path,value):
    path = Path(path)
    tmp = path.with_name(path.name+".partial")
    tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+"\n")
    tmp.replace(path)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    p.add_argument("--command",type=Path,required=True)
    p.add_argument("--point-source",choices=("final","packet"),required=True)
    p.add_argument("--checkpoint",type=Path)
    p.add_argument("--snapshot-identity-sha256")
    p.add_argument("--closed-phase-report",type=Path)
    p.add_argument("--expected-closed-phase-report-sha256")
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--levels",default="1:512:16,2:1024:32,4:2048:64")
    p.add_argument("--times",default="0,1/4,1/2,3/4,1")
    p.add_argument("--time-levels",default="4,8,16")
    p.add_argument("--fixed-chart-iterations",type=int,default=64)
    p.add_argument("--fixed-chart-tolerance",type=float,default=2.e-12)
    p.add_argument("--field-angle-block",type=int,default=8)
    p.add_argument("--export-levels",default="all")
    p.add_argument("--preview-radial-nodes",type=int,default=96)
    p.add_argument("--preview-angles",type=int,default=128)
    p.add_argument("--preview-cap-rings",type=int,default=32)
    p.add_argument("--preview-byte-limit",type=int,default=5000000)
    a = p.parse_args()
    for key in ("repo","report","command","outdir"):
        setattr(a,key,getattr(a,key).resolve())
    if a.checkpoint is not None:
        a.checkpoint = a.checkpoint.resolve()
    if a.closed_phase_report is not None:
        a.closed_phase_report = a.closed_phase_report.resolve()
    if a.expected_closed_phase_report_sha256 is not None:
        digest=a.expected_closed_phase_report_sha256
        if a.closed_phase_report is None or len(digest)!=64 or any(c not in "0123456789abcdef" for c in digest):
            p.error("An optional expected whole closed-report SHA needs its actual report path")
    if (a.fixed_chart_iterations<1 or a.field_angle_block<1 or a.preview_radial_nodes<3
            or a.preview_angles<4 or a.preview_angles%4 or a.preview_cap_rings<1
            or a.preview_byte_limit<1 or not math.isfinite(a.fixed_chart_tolerance)
            or a.fixed_chart_tolerance<=0):
        p.error("Use finite positive complete evaluation and explicit preview parameters")
    if a.outdir.exists() or a.outdir==a.repo or a.repo in a.outdir.parents:
        p.error("Use a fresh runner output directory outside the repository")
    return a


def public_summary(value):
    field = value.get("field_evaluation") or {}
    comparisons = value.get("spatial_refinement",[])
    time_comparisons = value.get("time_refinement",[])
    binding = value.get("field_binding") or {}
    point = binding.get("point") or {}
    seam = field.get("actual_full_radial_periodic_seam_read") or {}
    caps = value.get("cap_metric_readouts") or []
    meshes = value.get("meshes") or []
    closed = value.get("optional_closed_phase_evidence") or {}
    claims = closed.get("accurate_field_claims") or {}
    answer = dict(schema=SCHEMA+"-scalar-summary",
        complete=value.get("complete") is True,
        status=value.get("status"),source_sha256=value.get("source_sha256"),
        input_report_sha256=value.get("captured_scientific_report_sha256"),
        actual_full_point_sha256=point.get("current_full_point_sha256"),
        actual_model_identity_sha256=binding.get("model_identity_sha256"),
        actual_fixed_target_definition_identity_sha256=binding.get("fixed_target_definition_identity_sha256"),
        actual_original_free_variables=binding.get("original_variables"),
        actual_original_M=binding.get("M"),actual_original_J=binding.get("J"),
        actual_original_N=binding.get("N"),actual_original_normal_stages=binding.get("normal_stages"),
        finest_complete_field_points=field.get("evaluated_field_points"),
        maximum_sampled_metric_operator_error=field.get("maximum_sampled_metric_operator_error"),
        maximum_raw_closure_defect=field.get("maximum_original_working_raw_closure_defect"),
        maximum_centered_closure_residual=field.get("maximum_original_working_centered_closure_residual"),
        maximum_raw_core_vertical_port_discrepancy=field.get("maximum_raw_core_vertical_port_discrepancy"),
        maximum_raw_cap_cartesian_port_discrepancy=field.get("maximum_raw_cap_cartesian_port_discrepancy"),
        maximum_periodic_position_discrepancy=seam.get("F"),
        maximum_periodic_radial_derivative_discrepancy=seam.get("Fs"),
        maximum_periodic_angular_derivative_discrepancy=seam.get("Ftheta"),
        actual_additional_periodic_points=field.get("additional_periodic_endpoint_points"),
        first_cap_metric_operator_readout=(None if not caps else caps[0]["maximum_sampled_relative_cap_metric_error"]),
        last_cap_metric_operator_readout=(None if not caps else caps[-1]["maximum_sampled_relative_cap_metric_error"]),
        actual_exported_scientific_mesh_bytes=sum(x["bytes"] for x in meshes),
        maximum_mesh_port_projection=(None if not meshes else max(x["port_rounding_projection_maximum"] for x in meshes)),
        maximum_mesh_serialization_error=(None if not meshes else max(x["coordinate_serialization_error_maximum"] for x in meshes)),
        actual_mesh_files=len(value.get("meshes",[])),actual_preview_files=len(value.get("previews",[])),
        requested_spatial_levels=len(value.get("requested_levels",[])),
        returned_spatial_comparisons=len(comparisons),returned_time_comparisons=len(time_comparisons),
        first_spatial_position_difference=(None if not comparisons else
            comparisons[0]["active"]["differences"]["position"]),
        last_spatial_position_difference=(None if not comparisons else
            comparisons[-1]["active"]["differences"]["position"]),
        first_time_position_difference=(None if not time_comparisons else
            time_comparisons[0]["maximum_differences"]["position"]),
        last_time_position_difference=(None if not time_comparisons else
            time_comparisons[-1]["maximum_differences"]["position"]),
        first_spatial_PL_metric_operator_error=(None if not comparisons else comparisons[0]["active"]["differences"]["coarse_PL_metric_operator_error"]),
        last_spatial_PL_metric_operator_error=(None if not comparisons else comparisons[-1]["active"]["differences"]["coarse_PL_metric_operator_error"]),
        all_complete_source_and_input_bytes_rechecked=value.get("all_complete_source_and_input_bytes_rechecked",False),
        total_actual_seconds=value.get("actual_seconds"),
        original_nonlinear_optimization_reexecuted=False,
        frequency_solution_refinement_claimed=False,continuous_metric_bound_claimed=False,
        all_phase_embedding_or_reach_claimed=False,closed_isometry_accepted=False,
        optional_closed_evidence_provided=closed.get("provided",False),
        optional_closed_same_snapshot_bound=closed.get("complete_same_point_evidence_bound",False),
        optional_accurate_closed_C2=claims.get("complete_closed_C2_immersion_certified"),
        optional_accurate_all_phase_embedding=claims.get("all_physical_phases_embedded"),
        optional_accurate_reach_standard=claims.get("reach_standard_sufficient"),
        optional_accurate_delta_hold_stronger=claims.get("delta_hold_stronger_target_sufficient"),
        optional_evidence_pays_working_mesh_error=False,
        actual_error=value.get("error"),failed_phase=value.get("failed_phase"))
    return answer


def main():
    a = parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise SystemExit("All full-field and mesh computations require public repository Actions")
    # The original 0c1ff launcher sets this environment before its Python
    # child imports NumPy/SciPy/Torch. This new process has imported only stdlib.
    os.environ.update(PYTHONDONTWRITEBYTECODE="1",OPENBLAS_NUM_THREADS="1",
        OMP_NUM_THREADS="1",MKL_NUM_THREADS="1")
    sys.dont_write_bytecode = True
    started = time.monotonic()
    topic = a.repo/TOPIC
    paths = {role:topic/relative for role,(relative,_) in SOURCE_PINS.items()}
    sources = {}
    for role,path in paths.items():
        if sha(path)!=SOURCE_PINS[role][1]:
            raise ValueError("Changed full source role "+role)
        sources[role] = record(path)
    field = None
    recorder = None
    report = dict(schema=SCHEMA,source_sha256=sha(__file__),complete=False,status="binding",
        source_commit=subprocess.check_output(["git","-C",str(a.repo),"rev-parse","HEAD"],text=True).strip(),
        github_run_id=os.environ.get("GITHUB_RUN_ID"),github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        source_sha256_by_role={k:v[1] for k,v in SOURCE_PINS.items()},
        source_records=sources,original_full_command_line=sys.argv,
        meshes=[],previews=[],spatial_refinement=[],time_refinement=[],cap_metric_readouts=[],
        field_evaluation=None,optional_closed_phase_evidence=None,
        optional_closed_phase_report_argument=(None if a.closed_phase_report is None else str(a.closed_phase_report)),
        expected_closed_phase_report_sha256=a.expected_closed_phase_report_sha256,
        all_complete_source_and_input_bytes_rechecked=False,
        continuous_metric_error_paid=False,continuous_root_error_paid=False,
        complete_continuous_branch_certified=False,marked_closed_surface_embedding_certified=False,
        reach_or_grip_or_Euclidean_quotient_gap_certified=False,
        mesh_samples_not_continuous_certificates=True,frequency_solution_refinement_performed=False,
        original_nonlinear_optimization_reexecuted=False,closed_isometry_accepted=False)
    def save():
        report["actual_seconds"] = time.monotonic()-started
        atomic_json(a.outdir/"report.json",report)
        atomic_json(a.outdir/"scalar-summary.json",public_summary(report))
    def progress(value):
        report["latest_actual_progress"] = value
        if field is not None:
            report["latest_actual_operator_counts"] = dict(field.q.counts)
            report["latest_actual_endpoint_counts"] = dict(field.q.endpoint_counts)
        save()
        print(json.dumps(dict(event="actual_mesh_progress",**value),allow_nan=False),flush=True)
    try:
        binder = load("_complete_actual_fixed_fejer_mesh_input",paths["mesh_input"],SOURCE_PINS["mesh_input"][1])
        geometry = load("_complete_actual_material_phase_mesh",paths["mesh_arithmetic"],SOURCE_PINS["mesh_arithmetic"][1])
        levels = geometry.parse_levels(a.levels)
        times = geometry.rational_times(a.times)
        time_levels = [geometry.positive_integer(int(v)) for v in a.time_levels.split(",")]
        if any(v&(v-1) for v in time_levels):
            raise ValueError("Use explicit dyadic physical-time partitions")
        if any(y<=x or y%x for x,y in zip(time_levels,time_levels[1:])):
            raise ValueError("Keep every original coarse physical time in each actual refinement")
        if len(levels)<2 or len(time_levels)<2:
            raise ValueError("A genuine spatial/time comparison needs at least two declared complete levels")
        for level in levels:
            for t in times:
                geometry.phase_shift(level["angles"],t)
        for steps in time_levels:
            geometry.phase_shift(levels[-1]["angles"],F(1,steps))
        if a.preview_angles&(a.preview_angles-1) or levels[-1]["angles"]%a.preview_angles:
            raise ValueError("The standalone full-circle preview must be a dyadic subset of the actual finest circle")
        for t in times:
            geometry.phase_shift(a.preview_angles,t)
        export_levels = (list(range(len(levels))) if a.export_levels=="all"
            else [int(v) for v in a.export_levels.split(",")])
        if (len(set(export_levels))!=len(export_levels)
                or any(v<0 or v>=len(levels) for v in export_levels)):
            raise ValueError("Export only explicit existing complete spatial levels")
        report.update(requested_levels=levels,requested_physical_times=[str(v) for v in times],
            requested_time_levels=time_levels,export_level_indices=export_levels,
            original_mathematical_target_not_changed_by_mesh_parameters=True,
            preview_parameters=dict(radial_nodes=a.preview_radial_nodes,angles=a.preview_angles,
                cap_rings=a.preview_cap_rings,strict_byte_limit=a.preview_byte_limit))
        field = binder.ActualField(a)
        if a.field_angle_block != field.bound.args.angle_block:
            raise ValueError("Keep the original complete field's actual angular evaluation block")
        report["field_binding"] = field.binding
        report["field_binding_identity_sha256"] = field.binding_identity
        report["captured_scientific_report_sha256"] = field.report_capture["captured_sha256"]
        report["field_binding_file"] = record(a.outdir/"complete-field-binding.json")
        report["optional_closed_phase_evidence"] = binder.bind_closed_phase_evidence(
            a.closed_phase_report,a.expected_closed_phase_report_sha256,
            binding=field.binding,repo=a.repo,used=field.used)
        field.used.protect(a.outdir/"meshes")
        report["exact_frequency_input"] = binder.write_exact_frequency_input(field,a.outdir/"frequency-input")
        report["status"] = "material-chart-and-complete-radial-inputs"
        save()
        import numpy as np
        finest = levels[-1]
        chart = geometry.fixed_chart_inverse(field,finest["angles"],
            iterations=a.fixed_chart_iterations,tolerance=a.fixed_chart_tolerance)
        radial = geometry.radial_grid(field,finest["radial"])
        material_npz = a.outdir/"complete-material-grid.npz"
        np.savez(material_npz,phi=chart["phi"],theta=chart["theta"],
            chart_rho=chart["rho"],chart_rhop=chart["rhop"],circle_xy=chart["xy"],
            cells=radial["cells"],local=radial["local"],working_s=radial["s"],
            positive_intervals=radial["intervals"],same_target_a=radial["a"],
            target_a_carrier_errors=radial["a_error"])
        material_definition = dict(schema=SCHEMA+"-material-grid",
            actual_point_sha256=field.point_sha,model_identity_sha256=field.q.identity,
            fixed_target_definition_identity_sha256=field.target_identity,
            finest_level=finest,fixed_chart=chart["definition"],radial=radial["definition"],
            arrays_file=record(material_npz))
        atomic_json(a.outdir/"complete-material-grid.json",material_definition)
        report["material_grid"] = record(a.outdir/"complete-material-grid.json")
        report["material_grid_arrays"] = record(material_npz)
        report["status"] = "complete-actual-sixjet-field"
        recorder = field.bound.packets.NormalRootPacketRecorder(field.q,repo=a.repo,
            outdir=a.outdir/"actual-mesh-root-packets",caller_source=__file__,source_paths=paths)
        save()
        result = geometry.evaluate_finest(field,radial,chart,a.outdir/"whole-circle-sixjets",
            angle_block=a.field_angle_block,callback=progress)
        report["field_evaluation"] = result
        report["complete_sixjet_files"] = {key:record(path) for key,path in result["paths"].items()}
        # Exact source chart outputs at the actual field batch size are kept as
        # an additional immutable record, not overwritten in the initial plan.
        np.savez(a.outdir/"actual-evaluation-chart.npz",phi=chart["phi"],
            theta=chart["theta"],rho=chart["rho"],rhop=chart["rhop"])
        report["actual_evaluation_chart"] = record(a.outdir/"actual-evaluation-chart.npz")
        report["fixed_chart_inverse_after_complete_field"] = chart["definition"]
        metadata = field.q.metadata()
        required = [dict(cell=0,u=0.,phi=float(v)) for v in chart["phi"]]
        capture = recorder.capture_entry(metadata,outer_full_point_sha256=field.point_sha,
            witnesses=required,radius_witnesses=required,label="complete-mesh-sixjets-returned")
        report["root_packet_capture"] = capture
        report["normal_root_packets"] = recorder.metadata()
        report["latest_operator_metadata"] = metadata
        if capture["capture_completed"] is not True:
            raise ValueError("The actual new complete field roots could not be recorded immutably")
        if any(float(v).hex() not in field.q._root_cache for v in chart["phi"]):
            raise ValueError("A supposedly returned complete field angle lacks its original root record")
        field.bound.packets.validate_metadata(report["normal_root_packets"],model=field.q.model,
            operator_source_sha256=binder.NORMAL_SHA,caller_source_sha256=sha(__file__),
            source_sha256_by_role={k:v[1] for k,v in SOURCE_PINS.items()},
            reread_packets=True,reread_arrays=True)
        report["status"] = "same-target-spatial-refinement"
        save()
        jets = geometry.open_jets(result)
        for coarse,fine in zip(levels,levels[1:]):
            active = geometry.coarse_interpolation_comparison(jets,radial,finest,coarse,fine,
                radius=field.q.R,height=field.height)
            caps = geometry.cap_position_refinement(field.q.R,field.height,coarse,fine)
            report["spatial_refinement"].append(dict(active=active,caps=caps))
            progress(dict(phase="complete-spatial-comparison-returned",
                returned_comparisons=len(report["spatial_refinement"]),
                actual_position_difference=active["differences"]["position"]))
        for level in levels:
            report["cap_metric_readouts"].append(geometry.cap_metric_readout(field.q.R,field.height,level))
            save()
        report["status"] = "exact-phase-versus-time-interpolation"
        for coarse,fine in zip(time_levels,time_levels[1:]):
            item = geometry.time_interpolation_comparison(jets,radial,finest,coarse,fine,
                radius=field.q.R,height=field.height)
            report["time_refinement"].append(item)
            progress(dict(phase="complete-time-comparison-returned",
                coarse_steps=coarse,fine_steps=fine,
                actual_position_difference=item["maximum_differences"]["position"]))
        report["status"] = "complete-closed-mesh-serialization"
        meshdir = a.outdir/"meshes"
        meshdir.mkdir()
        for index in export_levels:
            level = levels[index]
            radial_indices,angular_indices = geometry.level_indices(finest,level,len(radial["cells"]))
            radii = geometry.cap_radii(field.q.R,level["cap_rings"])
            for t in times:
                tag = str(t).replace("/","_")
                path = meshdir/("full-level-"+str(index)+"-t-"+tag+".ply")
                item = geometry.write_mesh(path,jets,radial_indices,angular_indices,radii,
                    field.q.R,field.height,t,float_bits=64)
                item.update(level=index,file=record(path),scientific_discretization_mesh=True)
                report["meshes"].append(item)
                progress(dict(phase="complete-closed-mesh-written",level=index,t_exact=str(t),
                    bytes=item["bytes"],vertices=item["vertex_count"],triangles=item["triangle_count"]))
        preview_samples = np.linspace(0,len(radial["cells"])-1,
            min(a.preview_radial_nodes,len(radial["cells"])))
        preview_indices = np.unique(np.rint(preview_samples).astype(np.int64))
        preview_angles = np.arange(0,finest["angles"],finest["angles"]//a.preview_angles,dtype=np.int64)
        preview_radii = geometry.cap_radii(field.q.R,a.preview_cap_rings)
        previewdir = a.outdir/"standalone-previews"
        previewdir.mkdir()
        for t in times:
            tag = str(t).replace("/","_")
            path = previewdir/("complete-surface-t-"+tag+".ply")
            item = geometry.write_mesh(path,jets,preview_indices,preview_angles,preview_radii,
                field.q.R,field.height,t,float_bits=32,max_bytes=a.preview_byte_limit)
            item.update(file=record(path),rendering_only=True,all_original_radial_cells_in_preview=False,
                complete_surface_topology_and_p4_caps=True,
                preview_not_used_as_the_scientific_refinement_grid=True)
            report["previews"].append(item)
            save()
        report["status"] = "final-whole-byte-verification"
        field.recheck()
        for role,path in paths.items():
            if record(path) != sources[role]:
                raise ValueError("A full source changed during the complete mesh consumer")
        output_records = list(report["complete_sixjet_files"].values())
        output_records += [report["field_binding_file"],report["material_grid"],
            report["material_grid_arrays"],report["actual_evaluation_chart"]]
        output_records += [x["file"] for x in report["meshes"]+report["previews"]]
        output_records += [report["exact_frequency_input"][k] for k in
            ("input_definition","coefficient_file","actual_same_model_checkpoint")]
        for expected in output_records:
            if record(expected["path"]) != expected:
                raise ValueError("A complete already returned raw output changed")
        field.bound.packets.validate_metadata(report["normal_root_packets"],model=field.q.model,
            operator_source_sha256=binder.NORMAL_SHA,caller_source_sha256=sha(__file__),
            source_sha256_by_role={k:v[1] for k,v in SOURCE_PINS.items()},
            reread_packets=True,reread_arrays=True)
        rebound_closed=binder.bind_closed_phase_evidence(
            a.closed_phase_report,a.expected_closed_phase_report_sha256,
            binding=field.binding,repo=a.repo,used=field.used)
        if rebound_closed != report["optional_closed_phase_evidence"]:
            raise ValueError("The optional exact-field evidence changed during mesh evaluation")
        report["all_complete_source_and_input_bytes_rechecked"] = True
        report["all_complete_declared_output_bytes_rechecked"] = True
        report["latest_operator_metadata"] = field.q.metadata()
        report["complete"] = True
        report["status"] = "complete-finite-mesh-and-time-readouts"
        save()
        print(json.dumps(public_summary(report),sort_keys=True,allow_nan=False),flush=True)
        return 0
    except Exception as error:
        report["complete"] = False
        report["failed_phase"] = report.get("status")
        report["status"] = "actual-incomplete-mesh-consumer"
        report["error"] = repr(error)
        report["actual_traceback"] = traceback.format_exc()
        if field is not None:
            report["latest_operator_metadata"] = field.q.metadata()
            report["actual_last_root_failure"] = field.q.metadata().get("last_root_failure")
            if recorder is not None:
                report["failure_root_packet_capture"] = recorder.capture_entry(
                    report["latest_operator_metadata"],outer_full_point_sha256=field.point_sha,
                    label="actual-incomplete-mesh-read",witnesses=(),radius_witnesses=())
                report["normal_root_packets"] = recorder.metadata()
        if a.outdir.is_dir():
            save()
        print(json.dumps(public_summary(report),sort_keys=True,allow_nan=False),flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
