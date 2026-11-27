#!/usr/bin/env python3
"""Reproduce all complete run10 normal/geometry fee sources and full ready parameters.

This utility reads only exact complete source/parameter parents. It performs
stdlib text, SHA, AST and compile checks, never imports scientific modules or
runs field, root, interval or reduced numerical fixtures. Full runtime files
and complete parameter objects are authoritative outputs, not patches.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-larger-amplitude"
FIXED_TARGET = "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049"
FIXED_REFERENCE = "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5"
OUTPUT_SOURCES = {"input": {"role": "input", "name": "run10_normal_packet_accurate_field_input.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_normal_packet_accurate_field_input.py", "bytes": 26356, "sha256": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8", "parent_name": "run09_normal_packet_accurate_field_input.py", "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_normal_packet_accurate_field_input.py", "parent_bytes": 26431, "parent_sha256": "f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82", "git_blob_sha": "41c355a847ce078868f5c945532f016ada27fdb4"}, "radial": {"role": "radial", "name": "run10_accurate_reference_control_radial_boxes.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_accurate_reference_control_radial_boxes.py", "bytes": 45392, "sha256": "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c", "parent_name": "run09_accurate_reference_control_radial_boxes.py", "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_accurate_reference_control_radial_boxes.py", "parent_bytes": 45392, "parent_sha256": "0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b", "git_blob_sha": "03f8e7eacd00ade95e5cf2761fa31a40f77ae185"}, "normal": {"role": "normal", "name": "run10_complete_normal_root_and_sixjet_fees.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_normal_root_and_sixjet_fees.py", "bytes": 40280, "sha256": "0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83", "parent_name": "run09_complete_normal_root_and_sixjet_fees.py", "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_complete_normal_root_and_sixjet_fees.py", "parent_bytes": 40268, "parent_sha256": "f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1", "git_blob_sha": "01a0febb446e1b3953a021101cd0bc7e99126996"}, "leaf": {"role": "leaf", "name": "run10_complete_physical_leaf_binding.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_physical_leaf_binding.py", "bytes": 44539, "sha256": "cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5", "parent_name": "run09_complete_physical_leaf_binding.py", "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_complete_physical_leaf_binding.py", "parent_bytes": 44591, "parent_sha256": "b71e2e87a910e9461f53a72977263dab0966e55ca1b5800927416343f6d7fb06", "git_blob_sha": "170a2ca0027745ba51118cd38c31ed825cf1d020"}, "geometry": {"role": "geometry", "name": "run10_continuous_gram_curvature_support.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_continuous_gram_curvature_support.py", "bytes": 44853, "sha256": "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7", "parent_name": "run09_continuous_gram_curvature_support.py", "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_continuous_gram_curvature_support.py", "parent_bytes": 44853, "parent_sha256": "91843225f698e7f6de945acc353f7a3733ac70719d93995099c2ac3e6186b40a", "git_blob_sha": "a8d6e90e58dc52c34ee0fe65cb1a01e0fdf1e158"}, "bridge": {"role": "bridge", "name": "run10_complete_geometry_support_beta_bridge.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_geometry_support_beta_bridge.py", "bytes": 20741, "sha256": "96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9", "parent_name": "run09_complete_geometry_support_beta_bridge.py", "parent_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run09_complete_geometry_support_beta_bridge.py", "parent_bytes": 20741, "parent_sha256": "f14acf7bd84559b17de4359dc138ccd30b2b59ec26ec292336fd6b4686d99640", "git_blob_sha": "ad8173b880c65bf4729f306b697eadeb45a0c716"}}
SHARED_SOURCE = {"name": "accurate_normal_rotation_and_stage_boxes.py", "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/accurate_normal_rotation_and_stage_boxes.py", "bytes": 27453, "sha256": "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b", "git_blob_sha": "6e007ee79ccd53e3e7e58469164d6c7e34bff40e"}
SOURCE_PATCHES = {"input": [{"old": "run09", "new": "run10", "count": 8}, {"old": "fullclosed_run10_public_reference_analytic_frame_so3_qp_v2.py", "new": "fullclosed_run10_detached_closure_so3_qp.py", "count": 1}, {"old": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5", "new": "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1", "count": 1}, {"old": "read_run10_public_reference_analytic_frame_so3_report_v2.py", "new": "read_run10_detached_closure_so3_report.py", "count": 1}, {"old": "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32", "new": "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e", "count": 1}, {"old": "immutable_analytic_frame_normal_root_packets.py", "new": "immutable_closure_values_normal_root_packets.py", "count": 1}, {"old": "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0", "new": "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805", "count": 1}, {"old": "so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py", "new": "so3_reference_centred_closure_values_normal_lift_operator.py", "count": 1}, {"old": "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc", "new": "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4", "count": 1}, {"old": "17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820", "new": "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38", "count": 1}, {"old": "7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1", "new": "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1", "count": 1}, {"old": "7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a", "new": "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049", "count": 1}, {"old": "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75", "new": "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5", "count": 1}, {"old": "complete-R711-reference-centred-analytic-frame-and-J3-adjacent-frame-SO3-fixed-normal-plane-six-control-layer-v1", "new": "complete-R711-reference-centred-detached-closure-values-analytic-frame-J3-normal-layer-v1", "count": 1}, {"old": "len(roles) != 58", "new": "len(roles) != 75", "count": 1}], "radial": [{"old": "run09", "new": "run10", "count": 4}, {"old": "17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820", "new": "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38", "count": 1}, {"old": "7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1", "new": "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1", "count": 1}, {"old": "f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82", "new": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8", "count": 1}], "normal": [{"old": "run09", "new": "run10", "count": 6}, {"old": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5", "new": "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1", "count": 1}, {"old": "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32", "new": "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e", "count": 1}, {"old": "f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82", "new": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8", "count": 1}, {"old": "0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b", "new": "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c", "count": 1}, {"old": "repaired complete ff544/aee22 entry", "new": "complete run10 c3dc/2efa detached-closure entry", "count": 1}], "leaf": [{"old": "run09", "new": "run10", "count": 16}, {"old": "fullclosed_run10_public_reference_analytic_frame_so3_qp_v2.py", "new": "fullclosed_run10_detached_closure_so3_qp.py", "count": 1}, {"old": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5", "new": "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1", "count": 2}, {"old": "read_run10_public_reference_analytic_frame_so3_report_v2.py", "new": "read_run10_detached_closure_so3_report.py", "count": 1}, {"old": "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32", "new": "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e", "count": 2}, {"old": "immutable_analytic_frame_normal_root_packets.py", "new": "immutable_closure_values_normal_root_packets.py", "count": 1}, {"old": "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0", "new": "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805", "count": 1}, {"old": "so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py", "new": "so3_reference_centred_closure_values_normal_lift_operator.py", "count": 1}, {"old": "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc", "new": "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4", "count": 2}, {"old": "17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820", "new": "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38", "count": 2}, {"old": "7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1", "new": "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1", "count": 2}, {"old": "7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a", "new": "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049", "count": 1}, {"old": "f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82", "new": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8", "count": 1}, {"old": "0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b", "new": "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c", "count": 1}, {"old": "f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1", "new": "0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83", "count": 1}], "geometry": [{"old": "run09", "new": "run10", "count": 4}, {"old": "b71e2e87a910e9461f53a72977263dab0966e55ca1b5800927416343f6d7fb06", "new": "cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5", "count": 1}], "bridge": [{"old": "run09", "new": "run10", "count": 6}, {"old": "91843225f698e7f6de945acc353f7a3733ac70719d93995099c2ac3e6186b40a", "new": "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7", "count": 1}]}
EXPECTED_INPUT_PINS = {
    "reader": ("read_run10_detached_closure_so3_report.py", "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"),
    "driver": ("fullclosed_run10_detached_closure_so3_qp.py", "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"),
    "packets": ("immutable_closure_values_normal_root_packets.py", "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"),
    "normal": ("so3_reference_centred_closure_values_normal_lift_operator.py", "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"),
    "base": ("so3_supported_smooth_triangle_meridian_operator.py", "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"),
    "reference": ("so3_axisymmetric_reference.py", "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"),
    "continuous": ("so3_axisymmetric_continuous_integrand.py", "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6"),
    "reference_fees": ("run10_reference_seed_angular_profile_error_bounds.py", "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1"),
    "mean_integrals": ("run10_reference_accurate_mean_residuals.py", "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38"),
}
EXPECTED_RUNTIME_ROLES = {
    "root_packets": ("scripts/resume_20261126/immutable_closure_values_normal_root_packets.py", "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"),
    "analytic_parent_stage_matrices": ("scripts/resume_20261126/detached_normal_stage_matrix_reuse.py", "375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59"),
    "analytic_parent_adjacent_matrices": ("scripts/resume_20261126/adjacent_normal_frame_matrices.py", "955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3"),
    "analytic_parent_driver": ("scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py", "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"),
    "analytic_parent_reader": ("scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py", "f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470"),
    "analytic_J3": ("scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py", "9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa"),
    "analytic_J3_binding": ("scripts/resume_20261126/run10_detached_closure_value_binding.py", "dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1"),
    "analytic_parent_frame_C1": ("scripts/resume_20261126/normal_frame_c1_reuse.py", "ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"),
    "seed_reference": ("scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py", "0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"),
    "seed_mean": ("scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py", "f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"),
    "reference": ("scripts/resume_20261126/so3_axisymmetric_reference.py", "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"),
    "warm_producer": ("notes/2026-11-17-parallel-model-fullclosed-hold-warm.py", "bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3"),
    "observed": ("scripts/resume_20261120/gauss_observed_closed_gram.py", "26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"),
    "deep_scalar": ("scripts/resume_20261126/deep_valley_tail_input.py", "e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"),
    "scalar": ("notes/2026-11-17-parallel-model-full-hold-oracle.py", "a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"),
    "integer": ("notes/2026-11-17-parallel-inward-integral-enclosure.py", "babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"),
    "hold": ("scripts/parallel_20261117_negative_hold_profile_ivp.py", "ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"),
    "meridian": ("scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py", "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"),
    "geometry": ("scripts/resume_20261126/so3_run10_detached_closure_geometry.py", "6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528"),
    "qp": ("scripts/resume_20261120/fullspace_feasible_active_cg_v3.py", "fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"),
    "spectral": ("scripts/resume_20261120/positive_spectral_gram_weights.py", "e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91"),
    "hessian": ("scripts/resume_20261120/positive_spectral_gram_hessian.py", "29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4"),
    "centered": ("scripts/resume_20261126/centered_spectral_statistics.py", "5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01"),
    "history": ("scripts/resume_20261120/launch_refinement_from_full_report.py", "4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"),
    "pure_geometry": ("scripts/resume_20261120_curvature_qp.py", "a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854"),
    "geometry_selector": ("scripts/resume_20261120/fullclosed_point_inequalities_v2.py", "e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8"),
    "endpoint": ("scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py", "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"),
    "axisymmetric_seed_driver": ("scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py", "606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9"),
    "frozen_moment_input": ("scripts/resume_20261126/frozen_zero_moment_input.py", "4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611"),
    "moment_trace_source": ("scripts/resume_20261126/trace_zero_initial_endpoint_failure.py", "73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54"),
    "moment_initial_binding": ("scripts/resume_20261126/diagnose_zero_initial_chord.py", "65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0"),
    "moment_original_endpoint": ("scripts/resume_20261126/so3_zero_closure_endpoint_operator.py", "5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46"),
    "moment_original_driver": ("scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py", "b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b"),
    "new_moment_input": ("scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py", "307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"),
    "reference_calibration": ("scripts/resume_20261126/reference_centred_closure_values_calibration.py", "b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f"),
    "frame_C1": ("scripts/resume_20261126/normal_frame_c1_closure_values.py", "1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa"),
    "envelope_memory": ("scripts/resume_20261126/complete_material_envelope_memory.py", "c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152"),
    "envelope_rows": ("scripts/resume_20261126/complete_material_envelope_rows.py", "729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7"),
    "stage_matrices": ("scripts/resume_20261126/detached_stage_matrices_closure_values.py", "bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45"),
    "envelope_transfer": ("scripts/resume_20261126/transfer_run10_detached_closure_memory.py", "eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe"),
    "envelope_parent_reader": ("scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py", "104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7"),
    "envelope_parent_driver": ("scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py", "cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"),
    "envelope_parent_endpoint": ("scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py", "a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd"),
    "envelope_parent_calibration": ("scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py", "3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991"),
    "envelope_parent_geometry": ("scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py", "bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f"),
    "adjacent_matrices": ("scripts/resume_20261126/adjacent_normal_matrices_closure_values.py", "6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650"),
    "independent_envelope_memory": ("scripts/resume_20261126/complete_material_envelope_memory_public_run10.py", "f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba"),
    "independent_input_projection_producer": ("scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py", "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a"),
    "analytic_frame": ("scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py", "8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598"),
    "frame_parent_driver": ("scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py", "0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51"),
    "frame_parent_reader": ("scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py", "c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e"),
    "frame_parent_endpoint": ("scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py", "04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"),
    "frame_parent_calibration": ("scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py", "4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"),
    "frame_parent_J3": ("scripts/resume_20261126/analytic_normal_stage_jacobian.py", "64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"),
    "frame_parent_C1": ("scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py", "8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"),
    "frame_parent_stage_matrices": ("scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py", "5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"),
    "frame_parent_adjacent_matrices": ("scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py", "8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"),
    "actual_public_input_binding": ("scripts/resume_20261126/actual_public_run10_reference_input_binding.py", "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209"),
    "closure_values": ("scripts/resume_20261126/same_chain_detached_closure_values.py", "e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e"),
    "closure_parent_analytic_J3": ("scripts/resume_20261126/analytic_frame_local_stage_jacobian.py", "894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"),
    "closure_parent_analytic_frame": ("scripts/resume_20261126/analytic_normal_frame_jets.py", "4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"),
    "closure_parent_frame_C1": ("scripts/resume_20261126/analytic_frame_c1_reuse.py", "f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"),
    "closure_parent_stage_matrices": ("scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py", "fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"),
    "closure_parent_adjacent_matrices": ("scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py", "3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"),
    "closure_parent_reference_calibration": ("scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py", "fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"),
    "closure_parent_endpoint": ("scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py", "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"),
    "closure_parent_root_packets": ("scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py", "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"),
    "closure_parent_analytic_J3_binding": ("scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py", "15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"),
    "closure_parent_geometry": ("scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py", "e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"),
    "closure_parent_envelope_transfer": ("scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py", "6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"),
    "closure_parent_driver": ("scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py", "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"),
    "closure_parent_reader": ("scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py", "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"),
    "closure_parent_independent_envelope_memory": ("scripts/resume_20261126/complete_material_envelope_memory_public_reference.py", "2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"),
    "closure_parent_independent_input_projection_producer": ("scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py", "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"),
    "closure_parent_actual_public_input_binding": ("scripts/resume_20261126/actual_public_reference_input_binding.py", "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"),
}
READY_FILES = {"normal": {"name": "run10-complete-normal32-full-circle-sixjet-fees-ready.json", "path": "topics/visible-flex-larger-amplitude/computations/run10-complete-normal32-full-circle-sixjet-fees-ready.json", "bytes": 8774, "sha256": "40712a243c6cc166616e482c974c8a7fc6cee8eb423a336884290935cac89a8b", "git_blob_sha": "9eed81dfe5163ef5933efcabcc4341920b727b57", "parent_name": "run09-complete-normal32-full-circle-sixjet-fees-ready.json", "parent_path": "topics/visible-flex-larger-amplitude/computations/run09-complete-normal32-full-circle-sixjet-fees-ready.json", "parent_sha256": "13849f1598294e3efa1e9be80212f3ba2508458d4bec08fcbcdb5817bd271708", "parent_bytes": 8080}, "geometry": {"name": "run10-complete-continuous-gram-curvature-support-ready.json", "path": "topics/visible-flex-larger-amplitude/computations/run10-complete-continuous-gram-curvature-support-ready.json", "bytes": 8472, "sha256": "a0bcd9d5c73774f36b2cf8ea958c0077b2d3732589e8be42115398caf4232498", "git_blob_sha": "0b8014dd897d98f9a09d093b7197d1d3740f8fd9", "parent_name": "run09-complete-continuous-gram-curvature-support-ready.json", "parent_path": "topics/visible-flex-larger-amplitude/computations/run09-complete-continuous-gram-curvature-support-ready.json", "parent_sha256": "018bc65812bcb80c30652316197b955cabef0fbec7ca1cdc9ea8854f0c212ddc", "parent_bytes": 7977}}
READY_CONTENTS = {"normal": "{\n  \"schema\": \"complete-run10-normal-32-stage-and-full-angle-sixjet-fees-ready-v1\",\n  \"executed\": false,\n  \"admitted\": false,\n  \"scientific_execution_only_in_public_Actions\": true,\n  \"complete_source_sha256\": {\n    \"accurate_normal_rotation_and_stage_boxes.py\": \"29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b\",\n    \"run10_normal_packet_accurate_field_input.py\": \"852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8\",\n    \"run10_accurate_reference_control_radial_boxes.py\": \"fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c\",\n    \"run10_complete_normal_root_and_sixjet_fees.py\": \"0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83\"\n  },\n  \"source_report_expected_path\": \"{work}/run10-detached-closure-values-first/report.json\",\n  \"source_report_sha256_not_yet_assumed\": null,\n  \"actual_snapshot_identity_not_yet_assumed\": null,\n  \"actual_field_report_or_packet_success_not_assumed\": true,\n  \"snapshot_selection\": \"Latest genuine complete required-angle immutable snapshot; every originally cached angle retained; actual accepted outer point not inferred\",\n  \"exact_normal_stage_count\": 32,\n  \"complete_exact_phi_over_pi_domain\": [\n    \"0\",\n    \"2\"\n  ],\n  \"full_angle_closed_cells\": 1024,\n  \"quarter_orbit_symmetry_not_assumed\": true,\n  \"complete_original_radial_affine_domain_retained\": true,\n  \"complete_reference_mean_and_profile_recomputed_as_accurate_whole_angle_boxes\": true,\n  \"previous_literal_only_fees_relabelled_as_uniform\": false,\n  \"working_field_J_or_root_replayed\": false,\n  \"all_raw_proofs_and_physical_streams_only_on_runner\": true,\n  \"solver_admission_prerequisite\": false,\n  \"scientific_solver_parameters_or_sources_changed\": false,\n  \"saved_high_angular_order_not_upgraded\": true,\n  \"complete_physical_working_word_errors_paid\": false,\n  \"lower_reflection_caps_orientation_embedding_physical_phase_reach_separate\": true,\n  \"historical_unknown_peer_obligations_removed\": false,\n  \"partial_budget_return_is_not_certificate_or_solver_failure\": true,\n  \"steps\": [\n    {\n      \"id\": \"actual-run10-v2-complete-normal32-full-circle-sixjet-fees-first-20261127\",\n      \"script\": \"topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_normal_root_and_sixjet_fees.py\",\n      \"parent_bundle\": \"axisymmetric-R690-reference-v2-first/reference.npz\",\n      \"scope\": \"Complete actual-run10 accurate fee execution, pending a genuine immutable c3dc/2efa run10 report snapshot. Bind every full current point/source/target/input and all recorded immutable angular packets. Retain all actual cached/required literal angles and all32 common normal stages; additionally enclose every one of1024 closed full-circle cells phi/pi in[0,2]. Independently compute accurate R709 mean/profile whole-angle boxes, all original exact affine radial pieces and the true exponential/control/frame chains. Use each original stage_XXX_J only as an arbitrary rational preconditioner proposal; preserve actual order and all original words. Prove local stage root/first/second angular enclosures with full upstream dependence, then emit same-target a_deep/b/c/bs/cs/rho0 whole boxes and complete physical sixjets including every h/hp/hpp raw-defect term. Glue only by directed inclusion into another uniqueness domain, including periodic and original-literal association. No original working F/J/root replay. A natural900-second partial return preserves complete prefixes and is neither nonexistence nor a whole cover. Closed lower/cap C2, orientation, embedding, physicalphase reach, actual working-sixjet-word and externalparameter fees remain explicitly unclaimed. No future snapshot/field/fee value is prefilled.\",\n      \"args\": [\n        \"--repo\",\n        \"{repo}\",\n        \"--report\",\n        \"{work}/run10-detached-closure-values-first/report.json\",\n        \"--outdir\",\n        \"{work}/run10-normal-root-and-sixjet-fees-v1\",\n        \"--seconds\",\n        \"900\",\n        \"--maximum-leaf-evaluations\",\n        \"1000000\",\n        \"--precision-bits\",\n        \"192\",\n        \"--panels\",\n        \"128\",\n        \"--rho-leaf-budget\",\n        \"8192\",\n        \"--inverse-steps\",\n        \"64\",\n        \"--inverse-width\",\n        \"1/1000000000000000000000000\",\n        \"--full-angle-cells\",\n        \"1024\",\n        \"--radial-depth\",\n        \"0\",\n        \"--mean-maximum-splits\",\n        \"8192\",\n        \"--mean-width-goal\",\n        \"1/1000000000\",\n        \"--first-exp-degree\",\n        \"24\",\n        \"--maximum-exp-degree\",\n        \"128\",\n        \"--root-radius\",\n        \"1/100000000\",\n        \"--root-radius\",\n        \"1/1000000\",\n        \"--root-radius\",\n        \"1/10000\"\n      ],\n      \"outputs\": [\n        \"run10-normal-root-and-sixjet-fees-v1/report.json\"\n      ],\n      \"summary\": {\n        \"run10-normal-root-and-sixjet-fees-v1/report.json\": {\n          \"schema\": \"schema\",\n          \"source\": \"source_sha256\",\n          \"source_commit\": \"source_commit\",\n          \"run\": \"github_run_id\",\n          \"run_attempt\": \"github_run_attempt\",\n          \"actual_report\": \"actual_report.sha256\",\n          \"actual_full_point\": \"actual_current_full_point_sha256\",\n          \"actual_snapshot\": \"actual_snapshot_identity_sha256\",\n          \"actual_driver\": \"actual_scientific_driver_sha256\",\n          \"actual_reader\": \"actual_pure_reader_sha256\",\n          \"input_request\": \"complete_input_and_request_identity_sha256\",\n          \"complete_execution_binding\": \"complete_binding_identity_sha256\",\n          \"geometry_setup\": \"accurate_geometry_setup_complete\",\n          \"complete_all_requested\": \"complete\",\n          \"all_stages_and_streams\": \"all_planned_original_stages_and_sixjet_streams_complete\",\n          \"final_byte_recheck\": \"all_bound_input_and_output_bytes_rechecked_at_final_report\",\n          \"all_recorded_angles\": \"all_original_recorded_angle_count\",\n          \"all_required_angles\": \"all_original_required_angle_count\",\n          \"requested_full_circle_cells\": \"requested_full_circle_cell_count\",\n          \"planned_jobs\": \"planned_job_count\",\n          \"completed_jobs\": \"completed_job_count\",\n          \"whole_continuous_branch\": \"full_same_field_angle_branch.complete_continuous_angle_branch_certified\",\n          \"actual_leaf_evaluations\": \"actual_work_budget.actual_leaf_evaluations\",\n          \"maximum_leaf_evaluations\": \"actual_work_budget.maximum_leaf_evaluations\",\n          \"actual_budget_exhausted\": \"actual_work_budget.exhausted\",\n          \"elapsed_hex\": \"elapsed_seconds_binary64_hex\",\n          \"working_root_field_calls\": \"existing_working_root_and_field_calls\",\n          \"working_J_JT_calls\": \"existing_working_J_or_Jtranspose_calls\",\n          \"actual_words_not_fabricated\": \"comparison_candidates_were_existing_complete_actual_packet_words\",\n          \"actual_second_order_not_invented\": \"working_second_order_words_not_invented\",\n          \"working_physical_word_errors_paid\": \"complete_original_working_physical_sixjet_word_errors_paid\",\n          \"sixjet_scope\": \"physical_sixjet_output_scope\",\n          \"closed_geometry_certified\": \"complete_reflected_closed_surface_C2_or_reach_certificate\",\n          \"external_parameter_fees_paid\": \"external_parameter_J_and_transpose_error_certificate\",\n          \"historical_obligations_removed\": \"unknown_historical_material_role_obligations_removed\",\n          \"problem_completed\": \"mathematical_problem_completion_claimed\"\n        }\n      }\n    }\n  ],\n  \"actual_scientific_source_sha256\": \"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\",\n  \"actual_complete_reader_sha256\": \"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\",\n  \"actual_fixed_target_definition_identity_sha256\": \"e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049\",\n  \"actual_reference_model_identity_sha256\": \"081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5\",\n  \"actual_current_reference_tail_leaves\": 2218,\n  \"historical_address_carrier_restoration_leaves\": 2397,\n  \"historical_carrier_used_as_current_reference_values\": false,\n  \"complete_same_target_scalar_a_b_c_jet_boxes_in_every_physical_leaf\": true,\n  \"complete_scientific_runtime_source_role_count\": 75,\n  \"current_normal_source_sha256\": \"6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4\",\n  \"current_immutable_packet_source_sha256\": \"31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805\",\n  \"complete_reference_mean_source\": {\n    \"name\": \"run10_reference_accurate_mean_residuals.py\",\n    \"sha256\": \"19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38\"\n  },\n  \"complete_reference_profile_source\": {\n    \"name\": \"run10_reference_seed_angular_profile_error_bounds.py\",\n    \"sha256\": \"91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1\"\n  },\n  \"current_report_snapshot_not_progress_json\": true\n}\n", "geometry": "{\n  \"schema\": \"complete-run10-continuous-gram-curvature-support-ready-v1\",\n  \"executed\": false,\n  \"admitted\": false,\n  \"scientific_execution_only_in_public_Actions\": true,\n  \"complete_source_sha256\": {\n    \"run10_complete_physical_leaf_binding.py\": \"cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5\",\n    \"run10_continuous_gram_curvature_support.py\": \"e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7\",\n    \"run10_complete_geometry_support_beta_bridge.py\": \"96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9\"\n  },\n  \"source_normal_report_expected_path\": \"{work}/run10-normal-root-and-sixjet-fees-v1/report.json\",\n  \"future_source_normal_report_sha256\": null,\n  \"future_actual_point_or_snapshot\": null,\n  \"fixed_actual_normal_fee_source_sha256\": \"0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83\",\n  \"fixed_actual_radial_source_sha256\": \"fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c\",\n  \"exact_phi_over_pi_domain\": [\n    \"0\",\n    \"2\"\n  ],\n  \"all_original_32_stages_and_literal_associations_checked\": true,\n  \"all_complete_exact_radial_leaves_and_tail_retained\": true,\n  \"relative_Gram_uses_symmetric_operator_norm_not_entry_max\": true,\n  \"complete_physical_sixjets_and_raw_lift_retained\": true,\n  \"same_target_a_deep_and_fixed_rho0_true_enclosures_required\": true,\n  \"output_scope\": \"complete source-bound upper-meridian whole-cell enclosures; closed assembly and all physical phases are separate\",\n  \"original_solver_admission_gate\": false,\n  \"original_scientific_sources_or_parameters_changed\": false,\n  \"raw_support_and_matrix_streams_retained_only_on_runner\": true,\n  \"partial_budget_is_not_geometric_impossibility\": true,\n  \"all_preexisting_pending_queue_objects_must_be_kept_without_modification\": true,\n  \"queue_size_policy\": \"If adding this entire step exceeds95KB, archive only genuinely returned objects or preserve complete non-step history elsewhere with an exact pointer; do not trim pending argv/selectors/domain.\",\n  \"steps\": [\n    {\n      \"id\": \"actual-run10-whole-normal-leaf-continuous-gram-curvature-support-first-20261127\",\n      \"script\": \"topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_continuous_gram_curvature_support.py\",\n      \"parent_bundle\": \"axisymmetric-R690-reference-v2-first/reference.npz\",\n      \"scope\": \"Consume the genuine final 0d6e4 accurate-normal report and every complete original 32-stage/angular/root-provenance journal. Retain all actual literal associations and every full [0,2] phi/pi cell, with every exact original radial leaf and infinite tail. Re-read the whole immutable physical sixjet streams and the same target a_deep/rho0 boxes; compute symmetric 2x2 spectral operator bounds for the relative Gram error, full-second-form absolute principal-curvature bounds and candidate N=Fphi cross Fs support numerators. No working F/J/root or new accurate integrand evaluation. Missing whole-angle jobs, failed positivity, budget exhaustion and unproved global gluing remain explicit, without filling any missing domain with zero. Only complete global upper-cover numbers are promoted; lower reflection, closed C2/outward assembly, actual physical phases, actual marked-surface diameter/reach and the original beta consumer's eight proof roles are not fabricated. All original solver parameters, 32 stages, variables and unknown historical obligations remain unchanged.\",\n      \"args\": [\n        \"--repo\",\n        \"{repo}\",\n        \"--normal-report\",\n        \"{work}/run10-normal-root-and-sixjet-fees-v1/report.json\",\n        \"--outdir\",\n        \"{work}/run10-continuous-gram-curvature-support-v1\",\n        \"--seconds\",\n        \"900\"\n      ],\n      \"outputs\": [\n        \"run10-continuous-gram-curvature-support-v1/report.json\"\n      ],\n      \"summary\": {\n        \"run10-continuous-gram-curvature-support-v1/report.json\": {\n          \"schema\": \"schema\",\n          \"source\": \"source_sha256\",\n          \"source_commit\": \"source_commit\",\n          \"run\": \"github_run_id\",\n          \"attempt\": \"github_run_attempt\",\n          \"normal_report\": \"normal_report.sha256\",\n          \"geometry_binding\": \"complete_binding_identity_sha256\",\n          \"actual_point\": \"actual_current_full_point_sha256\",\n          \"model\": \"complete_original_model_identity_sha256\",\n          \"snapshot\": \"actual_snapshot_identity_sha256\",\n          \"target\": \"exact_fixed_target_identity_sha256\",\n          \"scalar\": \"fixed_scalar_metric_identity_sha256\",\n          \"setup\": \"geometry_setup_available\",\n          \"complete_upper\": \"complete\",\n          \"whole_angle_jobs\": \"expected_whole_angle_jobs\",\n          \"upstream_whole_jobs\": \"upstream_complete_whole_angle_jobs\",\n          \"processed_whole_jobs\": \"processed_complete_whole_angle_jobs\",\n          \"exact_radial_leaves\": \"expected_radial_leaves_per_angle\",\n          \"expected_all_leaves\": \"expected_complete_geometry_leaves\",\n          \"processed_leaves\": \"processed_geometry_leaves\",\n          \"complete_cover\": \"full_upper_cover_processed\",\n          \"continuous_Gram_complete\": \"continuous_Gram_bound_complete\",\n          \"continuous_K_complete\": \"continuous_curvature_bound_complete\",\n          \"continuous_support_complete\": \"continuous_support_numerator_bounds_complete\",\n          \"positive_upper_immersion_boxes\": \"complete_upper_immersion_lower_from_boxes\",\n          \"original_branch\": \"original_complete_angle_branch.complete\",\n          \"final_all_bytes\": \"all_input_and_output_bytes_rechecked\",\n          \"Gram_operator_upper\": \"accurate_global_bounds.relative_Gram_error_operator_norm_upper\",\n          \"curvature_upper\": \"accurate_global_bounds.principal_curvature_absolute_upper\",\n          \"normal_norm_lower\": \"accurate_global_bounds.normal_norm_lower\",\n          \"upper_only_D\": \"accurate_global_bounds.upper_base_phase_diameter_upper\",\n          \"formal_reflected_rotated_D\": \"accurate_global_bounds.formal_reflection_fixed_caps_all_rotation_set_diameter_upper\",\n          \"formal_D_actual_phase_proved\": \"accurate_global_bounds.formal_diameter_is_actual_phase_family_certificate\",\n          \"full_closed_D\": \"accurate_global_bounds.full_marked_surface_diameter_upper\",\n          \"full_closed_reach\": \"accurate_global_bounds.complete_closed_surface_reach_lower\",\n          \"Gram_unavailable\": \"partial_processed_statistics.relative_Gram_unavailable_leaf_count\",\n          \"K_unavailable\": \"partial_processed_statistics.curvature_unavailable_leaf_count\",\n          \"normal_positive_unproved\": \"partial_processed_statistics.normal_positive_unproved_leaf_count\",\n          \"lower_horizontal_support\": \"partial_processed_statistics.minima_over_processed_leaves.horizontal_support_numerator_lower.value\",\n          \"lower_vertical_support\": \"partial_processed_statistics.minima_over_processed_leaves.vertical_support_numerator_lower.value\",\n          \"new_working_F_J_root\": \"new_working_field_J_or_root_calls\",\n          \"new_accurate_root_integrands\": \"new_accurate_root_or_integrand_calls\",\n          \"closed_geometry\": \"complete_closed_geometry_certified\",\n          \"elapsed_hex\": \"elapsed_seconds_binary64_hex\"\n        }\n      }\n    }\n  ],\n  \"optional_beta_bridge\": {\n    \"script\": \"topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_geometry_support_beta_bridge.py\",\n    \"scheduled\": false,\n    \"reason\": \"No complete same-field closed/outward/full-phase proof package has returned; no evidence role is synthesized.\",\n    \"full_cli_required_keys\": [\n      \"--repo\",\n      \"--geometry-report\",\n      \"--expected-geometry-report-sha256\",\n      \"--beta-input\",\n      \"--expected-beta-input-sha256\",\n      \"--output\"\n    ],\n    \"requires_all_original_eight_evidence_roles\": true,\n    \"additionally_requires_same_field_lower_reflection_and_all_activity_seams\": true,\n    \"outward_claim_is_external_and_not_inferred_from_an_upper_complete_flag\": true,\n    \"original_beta_source_sha256\": \"e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991\"\n  },\n  \"actual_scientific_source_sha256\": \"c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1\",\n  \"actual_complete_reader_sha256\": \"2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e\",\n  \"actual_fixed_target_definition_identity_sha256\": \"e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049\",\n  \"actual_reference_model_identity_sha256\": \"081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5\",\n  \"complete_scientific_runtime_source_role_count\": 75\n}\n"}
READY_WORD_REPLACEMENTS = [["{work}/run09-public-reference-analytic-frame-v2-first/report.json", "{work}/run10-detached-closure-values-first/report.json"], ["ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5", "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"], ["aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32", "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"], ["7c766fb2d5008761c35d1ee848c76ef66f75510bee860efa037e70ed4f0f1f5a", "e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049"], ["d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75", "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5"], ["run09_normal_packet_accurate_field_input.py", "run10_normal_packet_accurate_field_input.py"], ["f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82", "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8"], ["run09_accurate_reference_control_radial_boxes.py", "run10_accurate_reference_control_radial_boxes.py"], ["0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b", "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c"], ["run09_complete_normal_root_and_sixjet_fees.py", "run10_complete_normal_root_and_sixjet_fees.py"], ["f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1", "0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83"], ["run09_complete_physical_leaf_binding.py", "run10_complete_physical_leaf_binding.py"], ["b71e2e87a910e9461f53a72977263dab0966e55ca1b5800927416343f6d7fb06", "cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5"], ["run09_continuous_gram_curvature_support.py", "run10_continuous_gram_curvature_support.py"], ["91843225f698e7f6de945acc353f7a3733ac70719d93995099c2ac3e6186b40a", "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7"], ["run09_complete_geometry_support_beta_bridge.py", "run10_complete_geometry_support_beta_bridge.py"], ["f14acf7bd84559b17de4359dc138ccd30b2b59ec26ec292336fd6b4686d99640", "96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9"], ["run09", "run10"], ["ff544/aee22", "c3dc/2efa"], ["f5ecc", "0d6e4"]]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def strict_text(path, expected_sha, expected_size):
    data = Path(path).read_bytes()
    if len(data) != expected_size or sha(data) != expected_sha:
        raise ValueError("Changed complete source/parameter parent: "+str(path))
    return data.decode("utf-8")


def literal(tree, name):
    values = [node.value for node in tree.body if isinstance(node, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)]
    if len(values) != 1:
        raise ValueError("Require the one complete literal definition: "+name)
    return ast.literal_eval(values[0])


def parse_complete(text, name):
    tree = ast.parse(text, filename=name)
    compile(tree, name, "exec")
    if any(line.rstrip() != line for line in text.splitlines()):
        raise ValueError("Unexpected source whitespace: "+name)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        seen = set()
        for key in node.keys:
            if key is None:
                continue
            try:
                value = ast.literal_eval(key)
                hash(value)
            except (ValueError, TypeError, SyntaxError):
                continue
            if value in seen:
                raise ValueError("Duplicate literal dictionary key: "+name)
            seen.add(value)
    return tree


def full_declarations(tree):
    result = {}
    def walk(nodes, prefix):
        for node in nodes:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                key = prefix+node.name
                if key in result:
                    raise ValueError("Repeated declared source scope")
                result[key] = ast.dump(node, include_attributes=False)
                walk(node.body, key+".")
    walk(tree.body, "")
    return result


def replay(parent, plan):
    value = parent
    for patch in plan:
        if (not isinstance(patch["old"], str) or not patch["old"]
                or not isinstance(patch["new"], str) or not patch["new"]
                or type(patch["count"]) is not int or patch["count"] <= 0
                or value.count(patch["old"]) != patch["count"]):
            raise ValueError("The full parent no longer has the exact declared patch")
        value = value.replace(patch["old"], patch["new"])
    backward = value
    for patch in reversed(plan):
        if backward.count(patch["new"]) != patch["count"]:
            raise ValueError("Ambiguous complete reverse patch")
        backward = backward.replace(patch["new"], patch["old"])
    if backward != parent:
        raise ValueError("The new full source does not reverse to the original full bytes")
    return value


def replaced(value):
    if isinstance(value, str):
        for old, new in READY_WORD_REPLACEMENTS:
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replaced(v) for v in value]
    if isinstance(value, dict):
        return {replaced(k): replaced(v) for k, v in value.items()}
    return value


def check_ready(parent, current, kind):
    if (not isinstance(parent.get("steps"), list) or len(parent["steps"]) != 1
            or not isinstance(current.get("steps"), list) or len(current["steps"]) != 1):
        raise ValueError("Retain the entire original executable step")
    old, new = parent["steps"][0], current["steps"][0]
    for key in ("args", "outputs", "summary", "script", "parent_bundle", "id"):
        if new[key] != replaced(old[key]):
            raise ValueError("The complete original ready step changed beyond its explicit bindings: "+key)
    expected_words = 38 if kind == "normal" else 8
    expected_selectors = 36 if kind == "normal" else 44
    selector_count = sum(len(v) for v in new["summary"].values())
    if len(new["args"]) != expected_words or selector_count != expected_selectors:
        raise ValueError("Do not reduce the full argv or complete returned-field selectors")
    if current.get("executed") is not False or current.get("admitted") is not False:
        raise ValueError("A source preparation cannot declare future scientific execution")
    if kind == "normal":
        if (current.get("source_report_sha256_not_yet_assumed") is not None
                or current.get("actual_snapshot_identity_not_yet_assumed") is not None
                or current.get("actual_current_reference_tail_leaves") != 2218
                or current.get("historical_address_carrier_restoration_leaves") != 2397
                or current.get("full_angle_closed_cells") != 1024
                or current.get("exact_normal_stage_count") != 32):
            raise ValueError("Bind only true inputs; retain the complete original domain")
    elif (current.get("future_source_normal_report_sha256") is not None
            or current.get("future_actual_point_or_snapshot") is not None):
        raise ValueError("Future complete report/point identities are not known")
    return dict(complete_argv_words=len(new["args"]), complete_scalar_selectors=selector_count,
        complete_original_step_parameters_retained=True,
        complete_original_selectors_retained=True,
        future_report_snapshot_or_field_values_fabricated=False)


def verify_contracts(trees, raw, repo):
    names = {role: record["name"] for role, record in OUTPUT_SOURCES.items()}
    input_tree = trees["input"]
    pins = literal(input_tree, "PINS")
    if pins != EXPECTED_INPUT_PINS or len(pins) != 9:
        raise ValueError("The complete actual input's exact nine whole-source bindings changed")
    mainpins = literal(trees["normal"], "PINS")
    expected = {
        "actual_input": (names["input"], OUTPUT_SOURCES["input"]["sha256"]),
        "accurate_rotation": (SHARED_SOURCE["name"], SHARED_SOURCE["sha256"]),
        "accurate_radial": (names["radial"], OUTPUT_SOURCES["radial"]["sha256"]),
    }
    if mainpins != expected:
        raise ValueError("Retain all three complete accurate lower modules")
    for key, expected_sha in {
            "INPUT_SHA": OUTPUT_SOURCES["input"]["sha256"],
            "ROTATION_SHA": SHARED_SOURCE["sha256"],
            "MEAN_SHA": pins["mean_integrals"][1],
            "SEED_MATH_SHA": pins["reference_fees"][1]}.items():
        if literal(trees["radial"], key) != expected_sha:
            raise ValueError("The accurate radial source closure changed: "+key)
    if literal(trees["leaf"], "ACTUAL_INPUT_SOURCE_PINS") != pins:
        raise ValueError("Physical-leaf reader lost the exact actual-input source registry")
    if literal(trees["leaf"], "NORMAL_FEE_SOURCE") != (
            names["normal"], OUTPUT_SOURCES["normal"]["sha256"]):
        raise ValueError("The full geometry source points to another normal-fee producer")
    if literal(trees["geometry"], "LEAF_READER") != (
            names["leaf"], OUTPUT_SOURCES["leaf"]["sha256"]):
        raise ValueError("Geometry must consume the whole exact new physical-leaf reader")
    if literal(trees["bridge"], "GEOMETRY_SOURCE") != (
            names["geometry"], OUTPUT_SOURCES["geometry"]["sha256"]):
        raise ValueError("The beta bridge points to another geometry source")
    beta = literal(trees["geometry"], "BETA_SOURCE")
    if (literal(trees["bridge"], "BETA_SOURCE") != beta
            or beta != ("same_field_positive_support_parameter.py",
                "e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991")):
        raise ValueError("Preserve the complete original eight-evidence-role beta consumer")
    if (literal(input_tree, "ACTUAL_TARGET") != FIXED_TARGET
            or literal(trees["leaf"], "ACTUAL_TARGET") != FIXED_TARGET
            or literal(input_tree, "ACTUAL_REFERENCE") != FIXED_REFERENCE):
        raise ValueError("The exact actual run10 target/reference binding changed")
    for role in ("normal", "leaf"):
        if (literal(trees[role], "ACTUAL_DRIVER") != pins["driver"][1]
                or literal(trees[role], "ACTUAL_READER") != pins["reader"][1]):
            raise ValueError("The accurate source binds another working driver/reader")
    if literal(trees["leaf"], "ACTUAL_MODEL_SOURCE") != pins["normal"][1]:
        raise ValueError("The same-field physical source differs")
    scripts = repo/TOPIC/"scripts/resume_20261126"
    external = []
    for role, (name, digest) in pins.items():
        path = scripts/name
        data = path.read_bytes()
        if sha(data) != digest:
            raise ValueError("Changed complete actual mathematical/scientific source: "+role)
        external.append(dict(role=role, path=str(path), bytes=len(data), sha256=digest))
    normal_tree = ast.parse((scripts/pins["normal"][0]).read_text())
    if literal(input_tree, "NORMAL_SCHEMA") != literal(normal_tree, "SCHEMA"):
        raise ValueError("Do not relabel another normal representation as the actual cache model")
    driver_tree = ast.parse((scripts/pins["driver"][0]).read_text())
    runtime = literal(driver_tree, "SOURCE_PINS")
    if runtime != EXPECTED_RUNTIME_ROLES or len(runtime) != 75:
        raise ValueError("The actual complete seventy-five-role registry changed")
    for role, (name, digest) in runtime.items():
        path = repo/TOPIC/name
        data = path.read_bytes()
        if sha(data) != digest:
            raise ValueError("A complete scientific role differs: "+role)
        external.append(dict(scientific_role=role, path=str(path), bytes=len(data), sha256=digest))
    for name, digest in (beta, (SHARED_SOURCE["name"], SHARED_SOURCE["sha256"])):
        data = (scripts/name).read_bytes()
        if sha(data) != digest:
            raise ValueError("A complete shared accurate source differs")
        external.append(dict(shared_source=name, bytes=len(data), sha256=digest))
    return external


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    repo, outdir = args.repo.resolve(), args.outdir.resolve()
    if (repo == outdir or repo in outdir.parents or outdir in repo.parents):
        raise ValueError("Keep complete generated output in a separate scratch tree")
    if outdir.exists():
        raise FileExistsError("Use a fresh complete source-only reproduction output")
    texts, trees, comparisons = {}, {}, []
    for role, record in OUTPUT_SOURCES.items():
        parent = strict_text(repo/record["parent_path"], record["parent_sha256"],
                             record["parent_bytes"])
        value = replay(parent, SOURCE_PATCHES[role])
        data = value.encode("utf-8")
        if (len(data) != record["bytes"] or sha(data) != record["sha256"]
                or len(data) >= 100000):
            raise ValueError("The complete new source has the wrong whole identity")
        oldtree = parse_complete(parent, record["parent_name"])
        tree = parse_complete(value, record["name"])
        olddecl, newdecl = full_declarations(oldtree), full_declarations(tree)
        if set(olddecl) != set(newdecl):
            raise ValueError("No original full function/class scope may be added or lost")
        unchanged = [key for key in olddecl if olddecl[key] == newdecl[key]]
        changed = [key for key in olddecl if olddecl[key] != newdecl[key]]
        comparisons.append(dict(role=role, original_whole_sha256=record["parent_sha256"],
            output_whole_sha256=record["sha256"], complete_forward_and_reverse_bytes_equal=True,
            total_declared_scopes=len(olddecl), unchanged_full_AST_scopes=unchanged,
            changed_full_AST_scopes=changed))
        texts[role], trees[role] = value, tree
    shared = strict_text(repo/SHARED_SOURCE["path"], SHARED_SOURCE["sha256"],
                         SHARED_SOURCE["bytes"])
    parse_complete(shared, SHARED_SOURCE["name"])
    external = verify_contracts(trees, texts, repo)
    ready_texts, ready_checks = {}, {}
    for kind, record in READY_FILES.items():
        parent = strict_text(repo/record["parent_path"], record["parent_sha256"],
                             record["parent_bytes"])
        value = READY_CONTENTS[kind]
        encoded = value.encode("utf-8")
        if len(encoded) != record["bytes"] or sha(encoded) != record["sha256"]:
            raise ValueError("A complete ready output differs from its exact parameter identity")
        ready_checks[kind] = check_ready(json.loads(parent), json.loads(value), kind)
        ready_texts[kind] = value
    source_dir, parameter_dir = outdir/"sources", outdir/"computations"
    source_dir.mkdir(parents=True)
    parameter_dir.mkdir()
    for role, value in texts.items():
        (source_dir/OUTPUT_SOURCES[role]["name"]).write_text(value, encoding="utf-8")
    (source_dir/SHARED_SOURCE["name"]).write_text(shared, encoding="utf-8")
    for kind, value in ready_texts.items():
        (parameter_dir/READY_FILES[kind]["name"]).write_text(value, encoding="utf-8")
    result = dict(schema="complete-run10-normal-and-continuous-geometry-source-replay-v1",
        reproducer_source_sha256=sha(Path(__file__).read_bytes()),
        complete_new_runtime_sources=OUTPUT_SOURCES,
        complete_unchanged_accurate_kernel=SHARED_SOURCE,
        complete_ready_files=READY_FILES,
        complete_source_comparisons=comparisons,
        complete_ready_checks=ready_checks,
        complete_external_source_records=external,
        complete_scientific_roles_verified=75,
        full_AST_compile_and_reverse_whole_source_reproduction=True,
        scientific_import=False, scientific_evaluation=False,
        interval_or_root_fixture=False,
        actual_field_report_or_snapshot_or_fee_produced=False)
    report = outdir/"complete-source-replay.json"
    report.write_text(json.dumps(result, sort_keys=True, indent=2, allow_nan=False)+"\n",
                      encoding="utf-8")
    print(json.dumps(dict(complete_runtime_sources=len(texts)+1,
        complete_ready_files=len(ready_texts), scientific_evaluation=False,
        report=str(report)), sort_keys=True))


if __name__ == "__main__":
    main()
