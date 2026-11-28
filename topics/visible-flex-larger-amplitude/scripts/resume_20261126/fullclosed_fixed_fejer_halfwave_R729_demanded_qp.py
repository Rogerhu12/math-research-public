#!/usr/bin/env python3
"""Complete R715 reference-centred R711 normal-plane SO3 optimization.

Every original free coordinate, positive Gram row, complete geometry row,
Phase-I/common-slack rule and actual nonlinear trial screen is retained.
Only the root equation is centred at the fixed original reference, while
all six physical jets retain the complete CURRENT raw closure lift. Working
radial Gram is actually read. All 32 default stages and every upstream
normal-frame/target parameter and angular derivative remain in J/J*.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import mmap
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.sparse.linalg import LinearOperator


SCHEMA = "complete-fixed-fejer-halfwave-R729-demanded-SO3-QP-v1"
SOURCE_PINS = {"common_slack_dual_recovery":("scripts/resume_20261126/fixed_fejer_R729_common_slack_dual_recovery.py","2dfe85c432d91f561a5f9d413f02cbc7d939edab2ea896e7fe4b3f810bc41863"),"root_packets":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_root_packets.py","fe555d2149c5cb1e919f51709da68098df3ad5960fabd87569802c1eb477e83f"),"analytic_parent_stage_matrices":("scripts/resume_20261126/detached_normal_stage_matrix_reuse.py","375059dc973633a1639ceddd3105fc34fe8b37eec4c9e61a55ce3959a0b9fc59"),"analytic_parent_adjacent_matrices":("scripts/resume_20261126/adjacent_normal_frame_matrices.py","955dafdc865e34695489f4e8832ecb8a6d48e056f801ba119fd92e9097ad69b3"),"analytic_parent_driver":("scripts/resume_20261126/fullclosed_reference_centred_independent_chart_material_envelope_so3_qp.py","95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"),"analytic_parent_reader":("scripts/resume_20261126/read_reference_centred_independent_chart_material_envelope_so3_report.py","f382bedb07fdf43e3fd94ac411c4a072519494dd2a16ec19ab627492d9606470"),"analytic_J3":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_stage_jacobian.py","7909d5781488131fd94c6389c85b24a235665484c2d5734e2df2db0584619b2d"),"analytic_J3_binding":("scripts/resume_20261126/fixed_fejer_halfwave_demanded_source_binding.py","2cbb44badea88db3d4d36422b12da70fb7d5f028626e268d06a87bdbe06a2c30"),"analytic_parent_frame_C1":("scripts/resume_20261126/normal_frame_c1_reuse.py","ba3d68f8560b99020f1596c4384e9fefc0115afeb987cae37627d24eba308dc9"),"seed_reference":("scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py","cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0"),"seed_mean":("scripts/resume_20261126/supported_smooth_triangle_seed_mean_jets.py","f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917"),"reference":("scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py","e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"),"warm_producer":("notes/2026-11-17-parallel-model-fullclosed-hold-warm.py","bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3"),"observed":("scripts/resume_20261120/gauss_observed_closed_gram.py","26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d"),"deep_scalar":("scripts/resume_20261126/deep_valley_tail_input.py","e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2"),"scalar":("notes/2026-11-17-parallel-model-full-hold-oracle.py","a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670"),"integer":("notes/2026-11-17-parallel-inward-integral-enclosure.py","babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0"),"hold":("scripts/parallel_20261117_negative_hold_profile_ivp.py","ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1"),"meridian":("scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_operator.py","b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6"),"geometry":("scripts/resume_20261126/so3_fixed_fejer_halfwave_demanded_geometry.py","8cde4d7c8c3699b870de0395386eaf4327572eb44bb9f5dfe3ea143c21425ace"),"qp":("scripts/resume_20261120/fullspace_feasible_active_cg_v3.py","fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"),"spectral":("scripts/resume_20261120/positive_spectral_gram_weights.py","e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91"),"hessian":("scripts/resume_20261120/positive_spectral_gram_hessian.py","29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4"),"centered":("scripts/resume_20261126/centered_spectral_statistics.py","5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01"),"history":("scripts/resume_20261120/launch_refinement_from_full_report.py","4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60"),"pure_geometry":("scripts/resume_20261120_curvature_qp.py","a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854"),"geometry_selector":("scripts/resume_20261120/fullclosed_point_inequalities_v2_halfwave_demanded_curvature_cache.py","b7293b63eb21af56bb15770e7afd12fa86988bf0c14719959155a3341c085497"),"endpoint":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_normal_lift.py","fbb17bbce55d6d100eeaa14cf29438ec00538b216d9a2aecb314d2376b44aee0"),"axisymmetric_seed_driver":("scripts/resume_20261126/fullclosed_axisymmetric_so3_qp.py","606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9"),"frozen_moment_input":("scripts/resume_20261126/frozen_zero_moment_input.py","4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611"),"moment_trace_source":("scripts/resume_20261126/trace_zero_initial_endpoint_failure.py","73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54"),"moment_initial_binding":("scripts/resume_20261126/diagnose_zero_initial_chord.py","65787b3e51f80505f5619c35fb05f8ad064e88de111578ff53e8bdad442092c0"),"moment_original_endpoint":("scripts/resume_20261126/so3_zero_closure_endpoint_operator.py","5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46"),"moment_original_driver":("scripts/resume_20261126/fullclosed_zero_closure_so3_qp.py","b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b"),"new_moment_input":("scripts/resume_20261126/fixed_fejer_paired_halfwave_literal_zero_moment_input.py","53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333"),"reference_calibration":("scripts/resume_20261126/fixed_fejer_paired_halfwave_reference_calibration.py","c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106"),"frame_C1":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_frame_c1.py","b185062a817df8e99602fa8aaab0ddd67a50d9938dc044b436ebbd94d7bfa6b1"),"envelope_memory":("scripts/resume_20261126/complete_material_envelope_memory.py","c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152"),"envelope_rows":("scripts/resume_20261126/complete_material_envelope_rows.py","729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7"),"stage_matrices":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_stage_matrices.py","e69a10e54239b02317cbc3b813ee90af91c2d3ddb9144ab3f1ea81dc9c08c83d"),"envelope_transfer":("scripts/resume_20261126/fixed_fejer_halfwave_demanded_memory_transfer.py","cfa6b64463fdf5ad450c31651f97101fd16944f507b5c8c1b9e922065521d0d9"),"envelope_parent_reader":("scripts/resume_20261126/read_reference_centred_c1_material_envelope_so3_report.py","104e014062f29969c0c94884bf810b6f9b23999ad8cc902238f981a9b0ad35f7"),"envelope_parent_driver":("scripts/resume_20261126/fullclosed_reference_centred_c1_material_envelope_so3_qp.py","cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"),"envelope_parent_endpoint":("scripts/resume_20261126/so3_reference_centred_c1_smooth_triangle_normal_lift_operator.py","a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd"),"envelope_parent_calibration":("scripts/resume_20261126/reference_centred_c1_smooth_triangle_calibration.py","3e478bbeacbe236947070f9422ab6c75852f460f41536c68ebb3995ff0a2a991"),"envelope_parent_geometry":("scripts/resume_20261126/so3_reference_centred_c1_material_envelope_geometry.py","bd1a2d439e2d83326dc59aa8dd9cdb28dccdbc453ab6f980f281475d44e0471f"),"adjacent_matrices":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_adjacent_matrices.py","6c466f2c4dccd158b3eca16eb7f020b935ee22824327f94e15e01a66647d5166"),"independent_envelope_memory":("scripts/resume_20261126/complete_fixed_fejer_material_envelope_memory.py","9f268e066274eff19ee2635124a8addf9c92eabf6d7177249f4ac4782c88a39a"),"independent_input_projection_producer":("scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py","e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"),"analytic_frame":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_angular_frame.py","477a501d3eb8a367687e6b40e8a58136ec2f9d11a28325e38b01a4455b85b285"),"frame_parent_driver":("scripts/resume_20261126/fullclosed_reference_centred_analytic_j3_material_envelope_so3_qp.py","0dfb96e53fa92e741e2d94819636486b45c49e341006370d1c6864ce70c36b51"),"frame_parent_reader":("scripts/resume_20261126/read_reference_centred_analytic_j3_material_envelope_so3_report.py","c2a6039633dbb397bdb6f56358153a362ed4e34c8e035a6a739eb23d5a1b785e"),"frame_parent_endpoint":("scripts/resume_20261126/so3_reference_centred_analytic_j3_smooth_triangle_normal_lift_operator.py","04f1d2724e1d93f138d03c558262f53e1dd5433791c081c7f93c37eeab84e21e"),"frame_parent_calibration":("scripts/resume_20261126/reference_centred_analytic_j3_smooth_triangle_calibration.py","4c3fb7a6d19a9c214e2dc69428456b62bc406c8329bc60083e1f5f8be3ff3d6d"),"frame_parent_J3":("scripts/resume_20261126/analytic_normal_stage_jacobian.py","64b39a8be75ee976dbf4b49768e4ebaf37a372f77dba397a439a054cc4e7465d"),"frame_parent_C1":("scripts/resume_20261126/analytic_j3_normal_frame_c1_reuse.py","8e6c3f255a6acbd27aa1291c1a8b0555eeaaeb869a58fde6a49b3fc5d16361f8"),"frame_parent_stage_matrices":("scripts/resume_20261126/analytic_j3_detached_normal_stage_matrix_reuse.py","5db725b423db4e97229a697ff6ce712b9183236070000e8ed66ed45cbe1767c1"),"frame_parent_adjacent_matrices":("scripts/resume_20261126/analytic_j3_adjacent_normal_frame_matrices.py","8a63cc1817fd0853c2b7ee69b64e3083de22106c239b62acc602ad9b69698787"),"actual_public_input_binding":("scripts/resume_20261126/fixed_fejer_reference_input_binding.py","3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f"),"closure_values":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_closure_values.py","2440622a82f1da79ccba468fbcf9e3e2dbc36762df63550e8de4bfb85a1d10b6"),"closure_parent_analytic_J3":("scripts/resume_20261126/analytic_frame_local_stage_jacobian.py","894efd3b277b8a8c1fbd4abcd68b573fb09ee10a706a90ded7b2e1894fe3b866"),"closure_parent_analytic_frame":("scripts/resume_20261126/analytic_normal_frame_jets.py","4ed6dfb93bb15b864d79c227b852421bc69b888a32923b98a21fe816da5be3d8"),"closure_parent_frame_C1":("scripts/resume_20261126/analytic_frame_c1_reuse.py","f1c74928089b60fb8f5350084ace0805fa956f4b06ac0de3f6a11357dd1aa2fb"),"closure_parent_stage_matrices":("scripts/resume_20261126/analytic_frame_detached_normal_stage_matrix_reuse.py","fa06705ebe19153edf455151a19c4217e42b8ab81ae3ffa4c1815701ec135255"),"closure_parent_adjacent_matrices":("scripts/resume_20261126/analytic_frame_adjacent_normal_matrices.py","3788b809c986668042e1c02f927afb85bf45434c4ff69607f9aaa2e2bf142695"),"closure_parent_reference_calibration":("scripts/resume_20261126/reference_centred_analytic_frame_smooth_triangle_calibration.py","fe422dbf2eac68bbc4f54e8fe290ba0e5d1b7a080f12f1d148cffe834957dba0"),"closure_parent_endpoint":("scripts/resume_20261126/so3_reference_centred_analytic_frame_smooth_triangle_normal_lift_operator.py","3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc"),"closure_parent_root_packets":("scripts/resume_20261126/immutable_analytic_frame_normal_root_packets.py","094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0"),"closure_parent_analytic_J3_binding":("scripts/resume_20261126/run09_public_reference_analytic_frame_binding.py","15f6393acb1f069e3c5dee62708f9350b3e329b877b19fc8a69868365a45a592"),"closure_parent_geometry":("scripts/resume_20261126/so3_run09_public_reference_analytic_frame_geometry_v2.py","e89dcfa368da67d6522a9df7dd5b49e58915db89bbc8152e15bc0a7a7c557a13"),"closure_parent_envelope_transfer":("scripts/resume_20261126/transfer_run09_public_reference_analytic_frame_memory.py","6deeeaa1dcbbb0fbfd968d0b31443798909536a55a7ea498f661e08496a27707"),"closure_parent_driver":("scripts/resume_20261126/fullclosed_run09_public_reference_analytic_frame_so3_qp_v2.py","ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"),"closure_parent_reader":("scripts/resume_20261126/read_run09_public_reference_analytic_frame_so3_report_v2.py","aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32"),"closure_parent_independent_envelope_memory":("scripts/resume_20261126/complete_material_envelope_memory_public_reference.py","2518133305275c070b5b0d46774baf92ce28634c7d71486c1a6c22c0e296e7fb"),"closure_parent_independent_input_projection_producer":("scripts/resume_20261126/freeze_run09_public_reference_and_restore_run05_carrier.py","9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18"),"closure_parent_actual_public_input_binding":("scripts/resume_20261126/actual_public_reference_input_binding.py","306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a"),"immutable_point_parent_closure_values":("scripts/resume_20261126/same_chain_detached_closure_values.py","e1af4fc8cfecbd30ab5cf9f7ded31d6a7a8d11385a8558cc76cbb8a8b1851e9e"),"immutable_point_parent_analytic_J3":("scripts/resume_20261126/analytic_local_stage_jacobian_closure_values.py","9646c1cb1e239f4625dfaa0f13e0d0776dfd9684401789a089326e177c02a5aa"),"immutable_point_parent_analytic_frame":("scripts/resume_20261126/analytic_normal_frame_jets_closure_values.py","8239fc8f3588afd4f93ba10368c599a85652d3b350a088b1397731c196258598"),"immutable_point_parent_frame_C1":("scripts/resume_20261126/normal_frame_c1_closure_values.py","1f80ce726f9cf9424740331eb54a5cafa86a058ca2b048ee5fb6add5fc371caa"),"immutable_point_parent_stage_matrices":("scripts/resume_20261126/detached_stage_matrices_closure_values.py","bf80cc8bbcf442d07d0e9225e1fbf703be4c40b951f10fb20e861e1ec7497c45"),"immutable_point_parent_adjacent_matrices":("scripts/resume_20261126/adjacent_normal_matrices_closure_values.py","6efb1b4de61635bb4121b2cc05daf4b817ecfb772f302568e2a570b7fa16b650"),"immutable_point_parent_reference_calibration":("scripts/resume_20261126/reference_centred_closure_values_calibration.py","b59776d52653f036590b619124579a20400d3bb7a4de8117d3221ca32bec144f"),"immutable_point_parent_endpoint":("scripts/resume_20261126/so3_reference_centred_closure_values_normal_lift_operator.py","6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4"),"immutable_point_parent_root_packets":("scripts/resume_20261126/immutable_closure_values_normal_root_packets.py","31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805"),"immutable_point_parent_binding":("scripts/resume_20261126/run10_detached_closure_value_binding.py","dc3b40645eb47f924392a703eb65e3fda982f43804b1861f89da1c038e9140a1"),"immutable_point_parent_geometry":("scripts/resume_20261126/so3_run10_detached_closure_geometry.py","6c676d4302f4271310ffca899ca8820fe43f2d792ee9a634747f25eecf9f6528"),"immutable_point_parent_envelope_transfer":("scripts/resume_20261126/transfer_run10_detached_closure_memory.py","eca323b12ff941736798f7e40021f78b92e1b23cee8a7edcdcc5e3f6db7508fe"),"immutable_point_parent_driver":("scripts/resume_20261126/fullclosed_run10_detached_closure_so3_qp.py","c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"),"immutable_point_parent_reader":("scripts/resume_20261126/read_run10_detached_closure_so3_report.py","2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e"),"immutable_point_parent_launcher":("scripts/resume_20261126/launch_run10_detached_closure_actions.py","22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604"),"fixed_fejer_previous_closure_values":("scripts/resume_20261126/immutable_point_detached_closure_values.py","2543ee5db3ff15108fbdb4e340dad84301b94eecb773f757da4126ab86778cfb"),"fixed_fejer_previous_analytic_J3":("scripts/resume_20261126/analytic_local_stage_jacobian_immutable_point.py","21a929c14abfe5e66ca56c232d31b77d8f8e3a5e969d796c4601d1a1e1374024"),"fixed_fejer_previous_analytic_frame":("scripts/resume_20261126/analytic_normal_frame_jets_immutable_point.py","4e9b027b365752878069fa29671f8f549fa4cd9be478487b12ceeb64a908f8fa"),"fixed_fejer_previous_frame_C1":("scripts/resume_20261126/normal_frame_c1_immutable_point.py","53b5bc456cb3f62c6a25d329de54920253d9193168ef3fb761198ff61fa0822d"),"fixed_fejer_previous_stage_matrices":("scripts/resume_20261126/detached_stage_matrices_immutable_point.py","a41872f7563683b28d34cb9da35d7fc3bd0879fb5a8d1d183230a518f6b8f052"),"fixed_fejer_previous_adjacent_matrices":("scripts/resume_20261126/adjacent_normal_matrices_immutable_point.py","ab944e9c9af4b84a65d201a6cc997669a8f274077fc7e1f69ee35b268380bb59"),"fixed_fejer_previous_reference_calibration":("scripts/resume_20261126/reference_centred_immutable_point_calibration.py","794275121ee8d2f79972c5302012a10ba1fd8aa58fa5f67f05399825244fd238"),"fixed_fejer_previous_endpoint":("scripts/resume_20261126/so3_reference_centred_immutable_point_normal_lift_operator.py","9bd394592f95668956c6718387b02d22d47c445b3f981f9101ae0e2c482594d6"),"fixed_fejer_previous_root_packets":("scripts/resume_20261126/immutable_point_normal_root_packets.py","b4c41b2dc8754607441c30cdb3a34199d7e40f8b52fc5e4a8f5d653ea524eac8"),"fixed_fejer_previous_reference":("scripts/resume_20261126/so3_axisymmetric_reference.py","4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"),"fixed_fejer_previous_seed_reference":("scripts/resume_20261126/supported_smooth_triangle_meridian_reference.py","0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b"),"fixed_fejer_previous_meridian":("scripts/resume_20261126/so3_supported_smooth_triangle_meridian_operator.py","6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865"),"fixed_fejer_previous_new_moment_input":("scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py","307ebae301db059f30ff1cc5fda024b09e9c2730c9f6bffbd82f0821d2a727a7"),"fixed_fejer_previous_analytic_J3_binding":("scripts/resume_20261126/run10_immutable_point_source_binding.py","85f3007a6927968eb253eab168e9379f9a1f732caf5aa43b9f24776f39606d97"),"fixed_fejer_previous_geometry":("scripts/resume_20261126/so3_run10_immutable_point_geometry.py","dbbd4601f4bbc0798759f3c63cd3caae3cfc19f1a62ec9dbd02cc6fbceb896ce"),"fixed_fejer_previous_envelope_transfer":("scripts/resume_20261126/transfer_run10_immutable_point_memory.py","0007abf0b2814b09a3ecc30f621cbd8814a3d94528c753762aa7be5175d08486"),"fixed_fejer_previous_independent_envelope_memory":("scripts/resume_20261126/complete_material_envelope_memory_public_run10.py","f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba"),"fixed_fejer_previous_independent_input_projection_producer":("scripts/resume_20261126/freeze_run10_public_reference_and_restore_run05_carrier.py","fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a"),"fixed_fejer_previous_actual_public_input_binding":("scripts/resume_20261126/actual_public_run10_reference_input_binding.py","9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209"),"fixed_input_producer":("scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py","89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"),"stage_point_parent_root_packets":("scripts/resume_20261126/fixed_fejer_immutable_normal_root_packets.py","1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468"),"stage_point_parent_stage_matrices":("scripts/resume_20261126/fixed_fejer_detached_stage_matrices.py","7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7"),"stage_point_parent_adjacent_matrices":("scripts/resume_20261126/fixed_fejer_adjacent_normal_matrices.py","257e5e44d38dffb82925a410c42e51f084cf7821a398b9928e543088a3f234c0"),"stage_point_parent_endpoint":("scripts/resume_20261126/fixed_fejer_normal_lift_operator.py","1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778"),"stage_point_parent_binding":("scripts/resume_20261126/fixed_fejer_complete_source_binding.py","3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88"),"stage_point_parent_envelope_transfer":("scripts/resume_20261126/transfer_fixed_fejer_material_envelope_memory.py","af35c30e4774987d8f71bc6d05c1942db66a9f7889127c19948b119dee9a1566"),"stage_point_parent_geometry":("scripts/resume_20261126/so3_fixed_fejer_complete_geometry.py","bab4147bdd2f0d43a372ec1b04225fc66a05db2ccdc2f92968d3f70e2590bf26"),"stage_point_parent_driver":("scripts/resume_20261126/fullclosed_fixed_fejer_immutable_point_so3_qp.py","477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"),"stage_point_parent_reader":("scripts/resume_20261126/read_fixed_fejer_immutable_point_so3_report.py","274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b"),"scalar_progress":("scripts/resume_20261126/fixed_fejer_complete_geometry_location_progress.py","4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94"),"meridian_parent_analytic_J3":("scripts/resume_20261126/fixed_fejer_analytic_stage_jacobian.py","7645268ee3538a43a4a04b73a5aee4fc5483b56962affeb0ba7e7f879d5d4a72"),"meridian_parent_frame_C1":("scripts/resume_20261126/fixed_fejer_normal_frame_c1.py","1830c1d8e69e0e12d4b9d8af9f194d234ef3437cba546200738a1592a77aa0ca"),"meridian_parent_stage_matrices":("scripts/resume_20261126/fixed_fejer_immutable_point_stage_matrices.py","e4d42910f9550a20d0afc16aab8f54b5ea1ceb18ace375128f3a79bfef0e76ce"),"meridian_parent_adjacent_matrices":("scripts/resume_20261126/fixed_fejer_stage_point_adjacent_matrices.py","d04cf80d40a16410a2338f3b4b0c3bbdd0084cfc2ad5270bee21d33ded9449b5"),"meridian_parent_reference_calibration":("scripts/resume_20261126/fixed_fejer_reference_calibration.py","fe36240c08ad32c4d4d665a387c70aaf02c0392419a51eef01e072081945e95c"),"meridian_parent_endpoint":("scripts/resume_20261126/fixed_fejer_stage_point_normal_lift.py","42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10"),"meridian_parent_analytic_frame":("scripts/resume_20261126/fixed_fejer_analytic_normal_frame.py","75db2f20039b66a2784a922bf062e792328c0153fb0458c16acef92e0ab7e38c"),"meridian_parent_closure_values":("scripts/resume_20261126/fixed_fejer_immutable_closure_values.py","01ca74a9f00ac17ef4452173b758d785c0e06869efa98980426f822d4beeb595"),"detached_meridian_values":("scripts/resume_20261126/fixed_fejer_paired_halfwave_demanded_meridian_values.py","26fa4aa15bb9fd2a9aa95e0e0e6f3a300628da77c189340a9e5ce4f23d04df55"),"meridian_parent_root_packets":("scripts/resume_20261126/fixed_fejer_stage_point_root_packets.py","140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf"),"meridian_parent_analytic_J3_binding":("scripts/resume_20261126/fixed_fejer_stage_point_source_binding.py","9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f"),"meridian_parent_geometry":("scripts/resume_20261126/so3_fixed_fejer_stage_point_geometry.py","2ecd2b23eccf6bee564c07daa386fbd232d7ff9f5634b484317d62ab10e56471"),"meridian_parent_envelope_transfer":("scripts/resume_20261126/transfer_fixed_fejer_stage_point_memory.py","afa2d6397c331b5bf55dd461bbf52a35839ff610d3db0f12a043e8eceef3b6ed"),"meridian_parent_scalar_progress":("scripts/resume_20261126/fixed_fejer_actual_mathematical_progress.py","bff1e03ae12a08444cb9d9d572e439a9b40cf59e80a201cd500f95539ce9e391"),"batched_geometry_binding":("scripts/resume_20261126/fixed_fejer_halfwave_demanded_geometry_binding.py","3d5f761fee10105bd0bc6d1a4056891e80b8b4b640aa13536f926c05b7bfc1d0"),"meridian_parent_driver":("scripts/resume_20261126/fullclosed_fixed_fejer_stage_point_observed_so3_qp.py","8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d"),"meridian_parent_reader":("scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py","c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f")}

ROOT_SNAPSHOT_SCHEMA = "actual-fixed-fejer-immutable-point-current-point-snapshot-v1"
ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256', 'endpoint_root_policy', 'normal_stage_count', 'exact_normal_step_nodes', 'actual_normal_step_carriers_binary64_hex', 'common_partition_for_all_angles_and_free_points', 'per_angle_adaptive_normal_partition', 'current_cached_angle_roots', 'current_all_grid_angle_roots_available', 'current_all_grid_second_angular_jets_available', 'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm', 'current_maximum_physical_z_norm', 'current_maximum_gamma_axis_norm', 'current_maximum_first_angular_endpoint_residual', 'current_maximum_second_angular_endpoint_residual', 'endpoint_counts', 'actual_normal_counts', 'last_root_failure', 'normal_lift_last_summary', 'numerical_Newton_iterations_differentiated', 'complete_uniform_IFT_conditions_verified', 'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed', 'stationary_KKT_selection_used', 'continuous_horizontal_ODE_solution_claimed', 'final_implicit_J_uses_all_normal_stage_equations', 'previous_normal_frame_full_parameter_chain_retained', 'original_zero_control_target_full_parameter_chain_retained', 'implicit_control_dimension', 'normal_increment_dimension', 'implicit_dimension_per_stage', 'complete_first_angular_implicit_dimension', 'complete_second_angular_implicit_dimension', 'current_reference_calibration', 'analytic_stage_jacobian', 'analytic_normal_frame', 'detached_closure_value_reuse')

def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def file_record(path, repo=None):
    path = Path(path).resolve()
    result = dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)
    if repo is not None:
        try:
            result['repo_relative_path'] = str(path.relative_to(repo))
        except ValueError:
            pass
    return result


def load(name, path, expected=None):
    if expected is not None and sha(path) != expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def event(**values):
    print(json.dumps(values, separators=(',', ':'), allow_nan=False), flush=True)


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def actual_reference(args, paths):
    report = json.loads(args.preparation_report.read_text())
    if (report.get('schema') != 'R690-fixed-fejer-axisymmetric-SO3-preparation-v1'
            or report.get('source_sha256') != SOURCE_PINS['reference'][1]
            or report.get('complete') is not True):
        raise ValueError('Bind the actual independent full-scalar input preparation')
    for role,path in dict(reference_bundle=args.reference_bundle,carrier=args.carrier,
            node_report=args.node_report,scalar_input=args.scalar_input).items():
        if report['input_for_solver'][role]['sha256'] != sha(path):
            raise ValueError('Changed actual complete independent input: '+role)
    for role,digest in report['source_sha256_by_role'].items():
        if role not in SOURCE_PINS or SOURCE_PINS[role][1] != digest:
            raise ValueError('Changed actual independent preparation source: '+role)
    model = report['reference_definition']
    profile = report['fixed_scalar_metric_identity_sha256']
    if (canonical(model) != report['reference_model_identity_sha256']
            or canonical(model['fixed_scalar_profile_definition']) != profile
            or model['fixed_scalar_metric_identity_sha256'] != profile
            or report['N'] != args.angles or report['J'] != 923 or report['M'] != 160 or report['P'] != 7377
            or report.get('historical_nonlinear_directions_replayed') is not False
            or report.get('optimized_old_q_field_read_as_T0') is not False):
        raise ValueError('Retain the actual independent mathematical reference and full positive observation domain')
    supplied = {sha(path) for path in args.manifest}
    if report['new_locations']['sha256'] not in supplied:
        raise ValueError('The complete prepared historical union must be one explicit solver manifest')
    return report,dict(preparation_report=file_record(args.preparation_report),
        actual_source=file_record(paths['reference'],args.repo),
        reference_model_identity_sha256=report['reference_model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=profile,original_scalar_parameters_identity_sha256=
            report['original_scalar_parameters_identity_sha256'],
        actual_input_records=report['input_for_solver'],new_locations=report['new_locations'],
        complete_supplied_location_provenance=report['complete_supplied_location_provenance'],
        all_supplied_history_retained=True,old_optimized_parent_required=False)

def all_locations(args, preparation, q, history, restart=None, source_report_path=None, *, envelope_memory, envelope_transfer):
    """Preserve the actual prior complete envelope addresses and typed memory across the new model."""
    return envelope_transfer.load_memory(args,preparation,q,history,
        memory=envelope_memory,current_driver_source=__file__,
        restart=restart,source_report_path=source_report_path)


def add_location(value, values, q):
    if value is None:
        return False
    if 'cell' in value:
        cell, u, phi = int(value['cell']), float(value['u']), float(value['phi'])
    elif 'stage' in value:
        stage = int(value['stage'])
        cell, u = int(q.observation_cells[stage]), float(q.observation_u[stage])
        phi = float(value['phi']) if 'phi' in value else float(q.phi[int(value['angle'])])
    else:
        raise ValueError('Every remembered point must have an actual physical address')
    if not (0 <= cell < q.J-1 and 0 <= u <= 1 and math.isfinite(phi)):
        raise ValueError('Invalid actual same-mesh permanent address')
    key = (cell, u.hex(), phi.hex())
    for old in values:
        if (int(old['cell']), float(old['u']).hex(), float(old['phi']).hex()) == key:
            if value.get('protected', False):
                old['protected'] = True
            return False
    values.append(dict(cell=cell, u=u, phi=phi, protected=bool(value.get('protected', False))))
    return True


class CommonSlackRows:
    """Every original row plus one scalar slack, without copying a multi-GB C.

    Original row C_i z <= -g_i/n_i becomes
    C_i z - delta_tau/n_i <= -g_i/n_i + tau0/n_i.
    Positive row renormalization is applied to BOTH sides; the extra row
    imposes tau0+delta_tau>=0. The physical g_i semantics are unchanged.
    """
    def __init__(self, matrix, bounds, metadata):
        self.matrix = matrix
        self.m, self.n = matrix.shape
        if len(metadata['rows']) != self.m:
            raise ValueError('Every complete row needs its real physical g and gradient norm')
        norms = np.array([row['gradient_coordinate_norm'] for row in metadata['rows']], dtype=float)
        scales = np.array([row['row_normalization_scale'] for row in metadata['rows']], dtype=float)
        gs = np.array([row['physical_g'] for row in metadata['rows']], dtype=float)
        if (not np.isfinite(norms).all() or np.any(norms < 0)
                or not np.isfinite(scales).all() or np.any(scales <= 0)
                or not np.isfinite(gs).all()):
            raise ValueError('Every restored row must have its finite actual gradient norm and positive row scale')
        discrepancy = np.max(np.abs(np.asarray(bounds)+gs/scales), initial=0.)
        tolerance = 32*np.finfo(float).eps*(1+np.max(np.abs(bounds), initial=0.))
        if discrepancy > tolerance:
            raise ValueError('The complete typed row physical margin changed before Phase I')
        # The tiny positive padding is a declared SLACK initialization,
        # not an acceptance tolerance or an extra geometric margin.
        self.tau0 = max(0., float(gs.max(initial=0.)))+8*np.finfo(float).eps*(1+float(np.max(np.abs(gs), initial=0.)))
        denominator = np.hypot(norms, 1.)
        self.factors = scales/denominator
        self.slack_column = -1/denominator
        self.bounds = np.r_[(self.tau0-gs)/denominator, self.tau0]
        self.shape = (self.m+1, self.n+1)
        self.record = dict(schema='complete-all-typed-C-common-slack-phase-I-v1',
            original_rows=self.m, augmented_rows=self.m+1,
            all_original_rows_retained=True, tau_initial=self.tau0,
            current_physical_g_max=float(gs.max(initial=0.)),
            maximum_margin_formula_discrepancy=float(discrepancy),
            zero_physical_gradient_rows_retained=int(np.count_nonzero(norms == 0)),
            objective='.5*(tau0+delta_tau)^2+.5*mu_restore^2*(|z|^2+delta_tau^2)',
            constraints='g_i+dg_i[Tz] <= tau0+delta_tau for EVERY selected typed row; tau0+delta_tau>=0',
            positive_row_rescaling_changes_feasible_set=False,
            physical_feasibility_inferred_from_slack=False,
            operator_only_virtual_rows=True, full_duplicate_row_cache_bytes=0)

    def _discard(self):
        if isinstance(self.matrix, np.memmap) and hasattr(self.matrix._mmap, 'madvise') and hasattr(mmap, 'MADV_DONTNEED'):
            self.matrix._mmap.madvise(mmap.MADV_DONTNEED)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            rows, columns = index
            if rows != slice(None):
                raise IndexError('The frozen QPv3 uses full-row streamed column slices')
            if not isinstance(columns, slice):
                raise IndexError('Use an actual contiguous column slice')
            start, stop, step = columns.indices(self.n+1)
            if step != 1:
                raise IndexError('Only contiguous original QPv3 blocks are used')
            result = np.zeros((self.m+1, max(0, stop-start)))
            original_stop = min(stop, self.n)
            if start < original_stop:
                result[:self.m, :original_stop-start] = np.asarray(
                    self.matrix[:, start:original_stop])*self.factors[:, None]
            if start <= self.n < stop:
                result[:self.m, self.n-start] = self.slack_column
                result[self.m, self.n-start] = -1.
            self._discard()
            return result
        row = int(index)
        if row == self.m:
            result = np.zeros(self.n+1)
            result[-1] = -1.
            return result
        if not 0 <= row < self.m:
            raise IndexError(row)
        result = np.r_[np.asarray(self.matrix[row])*self.factors[row], self.slack_column[row]]
        self._discard()
        return result



def endpoint_readout(q):
    """A complete explicit current-point snapshot; no replacement from another point."""
    value = q.metadata()
    result = {name: value[name] for name in ROOT_SNAPSHOT_KEYS}
    result.update(schema=ROOT_SNAPSHOT_SCHEMA,
        operator_schema=value['schema'], operator_source_sha256=value['source_sha256'],
        model_identity_sha256=value['model_identity_sha256'],
        snapshot_scope='actual current point and its own fixed normal-chain/root cache at this call; absent numerical values remain null')
    return result


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'reference-bundle', 'preparation-report', 'carrier', 'node-report', 'scalar-input', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--manifest', type=Path, action='append', required=True)
    p.add_argument('--material-envelope-binding', type=Path)
    p.add_argument('--material-envelope-parent-report', type=Path, action='append', default=[])
    p.add_argument('--independent-envelope-branch', action='store_true')
    p.add_argument('--pending-parallel-envelope-run', action='append', default=[])
    p.add_argument('--pending-parallel-envelope-source', action='append', default=[])
    p.add_argument('--material-envelope-seed-checkpoint', type=Path)
    p.add_argument('--material-envelope-seed-report', type=Path)
    p.add_argument('--envelope-near-active-rows', type=int, default=32)
    p.add_argument('--restart-checkpoint', type=Path)
    p.add_argument('--restart-report', type=Path)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--stage-block', type=int, default=64)
    p.add_argument('--angle-block', type=int, default=8)
    p.add_argument('--integration-order', type=int, default=8)
    p.add_argument('--inverse-root-iterations', type=int, default=18)
    p.add_argument('--inverse-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--norm-kind', choices=('jet-sum', 'integral'), default='jet-sum')
    p.add_argument('--radial-norm-length', type=float, default=.05)
    p.add_argument('--angular-transition', type=float, default=24.)
    p.add_argument('--torch-threads', type=int, default=4)
    p.add_argument('--damping', type=float, required=True)
    p.add_argument('--directions', type=int, default=2)
    p.add_argument('--maxiter', type=int, default=64)
    p.add_argument('--restoration-directions', type=int, default=4)
    p.add_argument('--restoration-damping', type=float, default=.01)
    p.add_argument('--restoration-maxiter', type=int, default=64)
    p.add_argument('--line-trials', type=int, default=15)
    p.add_argument('--qp-atol', type=float, default=0.)
    p.add_argument('--qp-rtol', type=float, default=1.e-6)
    p.add_argument('--qp-feasibility-tolerance', type=float, default=2.e-11)
    p.add_argument('--qp-rank-tolerance', type=float, default=2.e-12)
    p.add_argument('--active-rows', type=int, default=192)
    p.add_argument('--active-block-columns', type=int, default=32768)
    p.add_argument('--active-band', type=float, default=.025)
    p.add_argument('--reach-ratio', type=float, default=.03)
    p.add_argument('--reach-safety-factor', type=float, default=.992)
    p.add_argument('--marked-diameter-budget', type=float, default=4.2)
    p.add_argument('--witness-lower-budget', type=float, default=.9)
    p.add_argument('--amplitude-height-floor', type=float, default=1.01)
    p.add_argument('--amplitude-top-radius', type=int, default=2)
    p.add_argument('--amplitude-top-distance', type=int, default=4)
    p.add_argument('--spectral-p', type=int, default=4)
    p.add_argument('--spectral-epsilon', type=float, default=.001)
    p.add_argument('--spectral-scale', type=float, default=.05)
    p.add_argument('--legacy-fraction', type=float, default=.5)
    p.add_argument('--target', type=float, required=True)
    p.add_argument('--panels', type=int, default=128)
    p.add_argument('--seed-boundary-total-length', default='1/16')
    p.add_argument('--seed-profile-delta', default='1/128')
    p.add_argument('--seed-radial-quadrature-order', type=int, default=8)
    p.add_argument('--seed-profile-quadrature-order', type=int, default=16)
    p.add_argument('--seed-mean-maxiter', type=int, default=128)
    p.add_argument('--seed-mean-tolerance', type=float, default=2.e-12)
    p.add_argument('--seed-mean-backtracks', type=int, default=24)
    p.add_argument('--seed-mean-armijo', type=float, default=1.e-4)
    p.add_argument('--seed-scalar-iterations', type=int, default=64)

    for i in (1, 2):
        for position in ('left', 'middle', 'right'):
            p.add_argument('--endpoint-bubble-'+str(i)+'-'+position, required=True)
    p.add_argument('--endpoint-root-tolerance', type=float, default=2.e-12)
    p.add_argument('--endpoint-root-iterations', type=int, default=24)
    p.add_argument('--endpoint-root-backtracks', type=int, default=18)
    p.add_argument('--endpoint-root-armijo', type=float, default=1.e-4)
    p.add_argument('--endpoint-control-radius', type=float, default=2.)
    p.add_argument('--normal-stages', type=int, default=32)
    p.add_argument('--gamma-left', default='1/16')
    p.add_argument('--gamma-middle', default='1/8')
    p.add_argument('--gamma-right', default='3/16')
    p.add_argument('--seed-so3-checkpoint', type=Path)
    p.add_argument('--seed-so3-report', type=Path)
    moment_choice = p.add_mutually_exclusive_group(required=True)
    moment_choice.add_argument('--moment-trace-report', type=Path)
    moment_choice.add_argument('--moment-input', type=Path)
    p.add_argument('--moment-trace-report-sha256')
    p.add_argument('--moment-failed-report', type=Path)
    p.add_argument('--moment-input-sha256')
    p.add_argument('--moment-definition-sha256')
    p.add_argument('--moment-input-binding', choices=('supported-smooth-triangle-reference',), default='supported-smooth-triangle-reference')
    a = p.parse_args()
    if a.moment_trace_report is not None or a.moment_input is None:
        raise ValueError('The supported-smooth-triangle representation adopts the complete published parameter file through its new twelve-key binder')
    if a.seed_so3_checkpoint is not None or a.seed_so3_report is not None:
        raise ValueError('A prior 7f or different-reference field cannot be relabelled as this frozen supported-smooth-triangle seed; use the original full initial point or an actual same-source restart')
    boundary, profile_delta = Fraction(a.seed_boundary_total_length), Fraction(a.seed_profile_delta)
    if (str(boundary) != a.seed_boundary_total_length
            or str(profile_delta) != a.seed_profile_delta
            or not 0 < boundary < Fraction(7,8) or not 0 < profile_delta < Fraction(1,8)
            or min(a.seed_radial_quadrature_order, a.seed_profile_quadrature_order,
                   a.seed_mean_maxiter, a.seed_mean_backtracks, a.seed_scalar_iterations) < 1
            or not math.isfinite(a.seed_mean_tolerance) or a.seed_mean_tolerance <= 0
            or not math.isfinite(a.seed_mean_armijo) or not 0 < a.seed_mean_armijo < 1):
        raise ValueError('Use the complete exact supported seed and explicit positive working root/quadrature parameters')
    if a.moment_input_binding == 'supported-smooth-triangle-reference' and a.moment_trace_report is not None:
        raise ValueError('The explicit new-reference mode adopts the published literal parameter input; it does not relabel an old trace as current')
    if a.moment_trace_report is not None:
        if a.moment_failed_report is None or a.moment_trace_report_sha256 is None or a.moment_input_sha256 is not None:
            raise ValueError('The actual-trace route needs its complete recorded failure and trace SHA; no small-file SHA is mixed in')
    elif (a.moment_input_sha256 is None or a.moment_definition_sha256 is None
            or a.moment_trace_report_sha256 is not None or a.moment_failed_report is not None):
        raise ValueError('The small fixed-parameter route needs its file SHA and the SAME complete definition identity')
    for digest in (a.moment_trace_report_sha256, a.moment_input_sha256, a.moment_definition_sha256):
        if digest is not None and (len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest)):
            raise ValueError('Use complete explicit SHA256 input identities')
    if bool(a.restart_checkpoint) != bool(a.restart_report):
        raise ValueError('A true SO3 restart needs both its own complete checkpoint and report')

    if bool(a.seed_so3_checkpoint) != bool(a.seed_so3_report):
        raise ValueError('A zero-closure seed needs the actual complete base checkpoint and report')
    if a.restart_checkpoint is not None and a.seed_so3_checkpoint is not None:
        raise ValueError('Choose a true zero-closure continuation or a new-field base seed, not both')
    for i in (1, 2):
        row = [Fraction(getattr(a, 'endpoint_bubble_'+str(i)+'_'+position))
            for position in ('left', 'middle', 'right')]
        if not 0 < row[0] < row[1] < row[2] < 1:
            raise ValueError('Declare complete strictly interior exact quintic bubble triples')
    if Fraction(a.endpoint_bubble_1_right) >= Fraction(a.endpoint_bubble_2_left):
        raise ValueError('The two complete bubble supports must be disjoint')
    gamma = [Fraction(getattr(a, 'gamma_'+position)) for position in ('left','middle','right')]
    if (not 0 < gamma[0] < gamma[1] < gamma[2] < 1
            or not any(Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_left')) < gamma[0]
                < gamma[2] < Fraction(getattr(a,'endpoint_bubble_'+str(i)+'_right')) for i in (1,2))):
        raise ValueError('The complete independent gamma support must lie strictly inside an original bubble support')
    if (a.normal_stages < 1 or a.endpoint_root_iterations < 1 or a.endpoint_root_backtracks < 1
            or not 0 < a.endpoint_root_armijo < 1
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.endpoint_root_tolerance, a.endpoint_control_radius))):
        raise ValueError('Use explicit finite positive numerical endpoint-root parameters')
    if (min(a.directions, a.maxiter, a.line_trials, a.stage_block, a.angle_block,
            a.restoration_maxiter, a.active_rows, a.active_block_columns) < 1
            or a.restoration_directions < 0 or a.active_rows != 192
            or not 1 <= a.torch_threads <= 4 or a.angles != 2048 or a.panels < 1
            or not 0 < a.legacy_fraction < 1 or a.spectral_p < 2 or a.spectral_p%2
            or not 0 < a.reach_safety_factor < 1
            or not 0 < a.active_band < a.reach_safety_factor
            or any(not math.isfinite(v) or v <= 0 for v in (
                a.damping, a.restoration_damping, a.target, a.spectral_epsilon,
                a.spectral_scale, a.radial_norm_length, a.angular_transition,
                a.inverse_root_tolerance, a.qp_rtol, a.reach_ratio))):
        raise ValueError('Use explicit valid full-space/fixed-target numerical parameters')
    for name in ('repo', 'reference_bundle', 'preparation_report', 'carrier', 'node_report',
                 'scalar_input', 'outdir', 'restart_checkpoint', 'restart_report',
                 'seed_so3_checkpoint', 'seed_so3_report', 'moment_trace_report',
                 'moment_failed_report', 'moment_input'):
        if getattr(a, name) is not None:
            setattr(a, name, getattr(a, name).resolve())
    if a.envelope_near_active_rows < 1:
        raise ValueError('The new whole-grid near-active candidate cap is positive and never caps separation memory')
    if a.material_envelope_binding is not None:
        a.material_envelope_binding = a.material_envelope_binding.resolve()
    a.material_envelope_parent_report = [path.resolve() for path in a.material_envelope_parent_report]
    if bool(a.material_envelope_seed_checkpoint) != bool(a.material_envelope_seed_report):
        raise ValueError('An explicit old complete final variable seed requires both actual files')
    if a.material_envelope_seed_checkpoint is not None:
        a.material_envelope_seed_checkpoint = a.material_envelope_seed_checkpoint.resolve()
        a.material_envelope_seed_report = a.material_envelope_seed_report.resolve()
        if (a.restart_checkpoint is not None or a.seed_so3_checkpoint is not None
                or a.material_envelope_seed_report not in a.material_envelope_parent_report):
            raise ValueError('The explicit final belongs to a fully transferred prior envelope and cannot be mixed with another seed/restart')
    if (a.independent_envelope_branch and (a.material_envelope_parent_report
            or a.restart_checkpoint is not None or a.restart_report is not None
            or a.material_envelope_seed_checkpoint is not None or a.material_envelope_seed_report is not None
            or a.seed_so3_checkpoint is not None or a.seed_so3_report is not None)):
        raise ValueError('Explicit independent mode starts from the original reference, without a prior final or restart')
    if (a.pending_parallel_envelope_run and not a.independent_envelope_branch
            or len(a.pending_parallel_envelope_run)!=len(set(a.pending_parallel_envelope_run))
            or any(len(v.split('/'))!=2 or any(not w.isdigit() or int(w)<1 or str(int(w))!=w
                for w in v.split('/')) for v in a.pending_parallel_envelope_run)):
        raise ValueError('Use canonical run/attempt declarations only for unread independent-branch obligations')
    pending_sources={}
    for value in a.pending_parallel_envelope_source:
        parts=value.split('=')
        if (len(parts)!=2 or parts[0] in pending_sources or len(parts[1])!=64
                or any(c not in '0123456789abcdef' for c in parts[1])):
            raise ValueError('Use one complete explicit driver digest per pending run')
        pending_sources[parts[0]]=parts[1]
    if set(pending_sources)!=set(a.pending_parallel_envelope_run):
        raise ValueError('Every pending peer requires its exact run-to-source declaration')
    a.manifest = [path.resolve() for path in a.manifest]
    return a


def main():
    total_started = time.monotonic()
    args = parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise SystemExit('Scientific closed SO3 construction and solving require public repository Actions')
    topic = args.repo/'topics/visible-flex-larger-amplitude'
    paths = {role: topic/relative for role, (relative, digest) in SOURCE_PINS.items()}
    for role, path in paths.items():
        if sha(path) != SOURCE_PINS[role][1]:
            raise ValueError('Changed actual complete scientific source '+role)
    if (args.moment_input_binding!='supported-smooth-triangle-reference'
            or args.seed_so3_checkpoint is not None):
        raise ValueError('Use the unchanged current-base literal Q; the separate complete transfer binds any actual same-Fejer parent')
    if args.outdir.exists():
        raise FileExistsError('Use a fresh output directory for every actual complete budget')
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('All scientific raw outputs and evaluation caches must stay outside the repository')
    args.outdir.mkdir(parents=True)
    output = args.outdir/'report.json'
    source_commit = subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'], text=True).strip()
    preparation, reference_binding = actual_reference(args, paths)
    actual_public_scope=load('_actual_fixed_fejer_reference_scope',paths['analytic_J3_binding'])
    if args.material_envelope_binding is None:
        raise ValueError('The whole actual predeclared Fejer reference binding is required')
    fixed_input_binding=actual_public_scope.bind_fixed_fejer_input(args.material_envelope_binding,
        current_files=dict(current_reference_bundle=args.reference_bundle,
            current_preparation_report=args.preparation_report,current_carrier=args.carrier,
            current_node_report=args.node_report,current_scalar_input=args.scalar_input))
    reference = load('_so3_independent_axisymmetric_reference', paths['reference'])
    seed_reference = load('_so3_fixed_supported_unit_reference', paths['seed_reference'])
    seed_mean = load('_so3_complete_supported_mean_jets', paths['seed_mean'])
    meridian = load('_so3_actual_independent_axisymmetric_base', paths['meridian'])
    endpoint = load('_so3_independent_frozen_moment_zero_endpoint', paths['endpoint'])
    calibration = load('_so3_complete_reference_centred_calibration',paths['reference_calibration'])
    analytic_stage = load('_actual_complete_analytic_local_J3',paths['analytic_J3'])
    analytic_frame = load('_actual_complete_six_control_analytic_frame',paths['analytic_frame'])
    closure_values = load('_actual_complete_same_chain_closure_values',paths['closure_values'])
    meridian_values = load('_actual_complete_detached_meridian_values',paths['detached_meridian_values'])
    stage_matrices = load('_actual_complete_detached_stage_matrices',paths['stage_matrices'])
    adjacent_matrices = load('_actual_complete_adjacent_frame_matrices',paths['adjacent_matrices'])
    frame_c1 = load('_so3_complete_same_graph_frame_C1',paths['frame_C1'])
    moment_binding = load('_so3_complete_frozen_moment_input', paths['frozen_moment_input'])
    new_moment_binding = load('_so3_explicit_new_reference_literal_Q', paths['new_moment_input'])
    geometry_module = load('_so3_complete_geometry_screen', paths['geometry'])
    spectral = load('_so3_same_spectral_loss', paths['spectral'])
    hessian = load('_so3_same_spectral_hessian', paths['hessian'])
    centered = load('_so3_same_centered_scalar', paths['centered'])
    qp = load('_so3_complete_QPv3', paths['qp'])
    r729=load('_R729',paths['common_slack_dual_recovery'])
    root_packets = load('_actual_immutable_normal_root_packets', paths['root_packets'])
    history = load('_so3_complete_address_history', paths['history'])
    envelope_transfer = load('_actual_complete_envelope_transfer',paths['envelope_transfer'])
    envelope_memory = load('_so3_complete_material_envelope_memory',paths['envelope_memory'])
    independent_envelope_memory = load('_so3_complete_current_restorer_envelope_memory',paths['independent_envelope_memory'])
    meridian.torch.set_num_threads(args.torch_threads)
    meridian.torch.set_num_interop_threads(1)
    context = reference.AxisymmetricReferenceContext.from_files(repo=args.repo,
        reference_bundle=args.reference_bundle,carrier=args.carrier,node_report=args.node_report,
        scalar_input=args.scalar_input,preparation_report=args.preparation_report,panels=args.panels)
    reference_problem, reference_prepared = context.create_problem(N=args.angles,stage_block=args.stage_block)
    fixed_profile = context.scalar_identity
    if context.model != preparation['reference_definition']:
        raise ValueError('The actual complete reference changed between report and construction')
    seed_parameters = seed_reference.SeedParameters(
        relative_boundary_total_length=args.seed_boundary_total_length,
        profile_delta=args.seed_profile_delta,
        radial_quadrature_order=args.seed_radial_quadrature_order,
        profile_quadrature_order=args.seed_profile_quadrature_order,
        mean_maxiter=args.seed_mean_maxiter, mean_tolerance=args.seed_mean_tolerance,
        scalar_iterations=args.seed_scalar_iterations,
        mean_backtracks=args.seed_mean_backtracks, mean_armijo=args.seed_mean_armijo)
    base = meridian.ClosedMeridianOperator(reference_problem,reference_prepared,seed_reference,
        cache_directory=args.outdir/'fixed-supported-smooth-triangle-reference-cache',integration_order=args.integration_order,
        angle_block=args.angle_block,root_iterations=args.inverse_root_iterations,
        root_tolerance=args.inverse_root_tolerance,
        expected_parent_bundle_sha256=sha(args.reference_bundle),
        seed_parameters=seed_parameters, seed_mean_kernel_module=seed_mean)
    root_policy = endpoint.EndpointPolicy(endpoint_tolerance=args.endpoint_root_tolerance,
        maximum_iterations=args.endpoint_root_iterations,maximum_backtracks=args.endpoint_root_backtracks,
        armijo=args.endpoint_root_armijo,control_radius=args.endpoint_control_radius)
    normal_step_nodes = tuple(Fraction(i,args.normal_stages) for i in range(args.normal_stages+1))
    bubble_nodes = [[getattr(args, 'endpoint_bubble_'+str(i)+'_'+position)
        for position in ('left', 'middle', 'right')] for i in (1,2)]
    if args.moment_input_binding == 'supported-smooth-triangle-reference':
        origin = moment_binding.from_parameter_file(args.moment_input,
            input_sha256=args.moment_input_sha256,
            expected_definition_identity_sha256=args.moment_definition_sha256)
        frozen_moment_input = new_moment_binding.bind_new_input(origin,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_definition_identity = new_moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile,
            initial_full_point_sha256=meridian.array_sha(base.initial()), bubble_nodes=bubble_nodes)
        moment_input_record = dict(mode='explicit fixed supported-smooth-triangle reference adopts complete published literal Q parameters',
            actual_parameter_file=file_record(args.moment_input),
            input_binding_source=file_record(paths['new_moment_input']),
            no_moment_or_inverse_recomputed=True, old_reference_or_initial_point_binding_inherited=False,
            same_mathematical_g_claimed=False, current_moment_inverse_property_claimed=False)
    else:
        if args.moment_trace_report is not None:
            frozen_moment_input = moment_binding.from_trace(args.repo, args.moment_trace_report,
                trace_report_sha256=args.moment_trace_report_sha256,
                failed_report=args.moment_failed_report,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference actual trace word extraction',
                actual_trace_report=file_record(args.moment_trace_report),
                actual_failed_report=file_record(args.moment_failed_report),
                no_moment_or_inverse_recomputed=True)
        else:
            frozen_moment_input = moment_binding.from_parameter_file(args.moment_input,
                input_sha256=args.moment_input_sha256,
                expected_definition_identity_sha256=args.moment_definition_sha256)
            moment_input_record = dict(mode='strict SAME reference published complete parameter definition',
                actual_parameter_file=file_record(args.moment_input),
                no_moment_or_inverse_recomputed=True)
        moment_definition_identity = moment_binding.bind_to_base(frozen_moment_input,
            base_model=base.model, initial_reference_bundle_sha256=sha(args.reference_bundle),
            fixed_scalar_metric_identity_sha256=fixed_profile, bubble_nodes=bubble_nodes)
    q = endpoint.ZeroClosureOperator(base, expected_base_source_sha256=SOURCE_PINS['meridian'][1],
        expected_base_schema='complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1',
        bubble_nodes=bubble_nodes, frozen_moment_input=frozen_moment_input, endpoint_policy=root_policy,
        normal_step_nodes=normal_step_nodes,
        gamma_nodes=(args.gamma_left,args.gamma_middle,args.gamma_right),
        new_input_binder=(new_moment_binding if args.moment_input_binding == 'supported-smooth-triangle-reference' else None),
        reference_centering_module=calibration,frame_c1_module=frame_c1,stage_matrix_module=stage_matrices,
        adjacent_matrix_module=adjacent_matrices,analytic_stage_module=analytic_stage,
        analytic_frame_module=analytic_frame,closure_value_module=closure_values,
        meridian_value_module=meridian_values,
        evaluation_progress_path=args.outdir/'actual-normal-evaluation-progress.json')
    coordinates = meridian.RotationH2Coordinates(q, radial_length=args.radial_norm_length,
        angular_transition=args.angular_transition, norm_kind=args.norm_kind)
    restart = seed_report = None
    if args.restart_checkpoint is not None:
        restart = json.loads(args.restart_report.read_text())
        if (restart.get('schema') != SCHEMA or restart.get('source_sha256') != sha(__file__)
                or restart.get('complete') is not True
                or restart.get('final_bundle_sha256') != sha(args.restart_checkpoint)
                or restart.get('model_identity_sha256') != q.identity
                or restart.get('fixed_scalar_metric', {}).get('identity_sha256') != fixed_profile
                or restart.get('observation_carrier_sha256') != sha(args.carrier)):
            raise ValueError('Continue only this true complete SO3 source and the identical exact mathematical field model')
        x = q.load_checkpoint(args.restart_checkpoint)
    elif args.seed_so3_checkpoint is not None:
        seed_report = json.loads(args.seed_so3_report.read_text())
        if (seed_report.get('schema') != 'complete-independent-axisymmetric-fixed-deep-so3-meridian-QP-v1'
                or seed_report.get('source_sha256') != SOURCE_PINS['axisymmetric_seed_driver'][1]
                or seed_report.get('complete') is not True
                or seed_report.get('final_bundle_sha256') != sha(args.seed_so3_checkpoint)
                or seed_report.get('model_identity_sha256') != base.identity
                or seed_report.get('fixed_scalar_metric', {}).get('identity_sha256') != fixed_profile
                or seed_report.get('observation_carrier_sha256') != sha(args.carrier)
                or seed_report.get('representation') != base.model):
            raise ValueError('Bind the actual complete direct-base field used only as original-variable seed')
        x = base.load_checkpoint(args.seed_so3_checkpoint)
    else:
        x = q.initial()
    # Every new-target path uses its complete actual predeclared recipe/reference consumer.
    # Historical parent families keep their own source identities; they are
    # never relabelled as the current memory or as a current checkpoint.
    envelope_memory=independent_envelope_memory
    address_parent = restart if restart is not None else seed_report
    address_parent_path = args.restart_report if restart is not None else args.seed_so3_report
    witnesses, radius_witnesses, history_record, envelope, envelope_transfer_record = all_locations(
        args, preparation, q, history, address_parent, address_parent_path,
        envelope_memory=envelope_memory,envelope_transfer=envelope_transfer)
    prior_final_point,prior_final_seed = envelope_transfer.seed_from_complete_prior_final(
        args,q,current_driver_source=__file__,transfer_record=envelope_transfer_record)
    if prior_final_point is not None:
        x = prior_final_point
    stage_weights = q.mixed_stage_weights(args.legacy_fraction)
    if not np.isfinite(stage_weights).all() or np.any(stage_weights <= 0):
        raise ValueError('Every original legacy/Gauss radial observation needs its positive weight')
    normalizer = float(stage_weights.sum()*q.full_N)
    parameters = spectral.Parameters(p=args.spectral_p, epsilon=args.spectral_epsilon, scale=args.spectral_scale)
    objective_key = 'centered_phi_normalized'
    # GeometryScreen is an independent new-field adapter. Its exact frozen
    # old selector is retained; no old physical point source is relabeled.
    budgets = geometry_module.Budgets(args.marked_diameter_budget, args.witness_lower_budget,
        q.R, args.amplitude_height_floor)
    screen = geometry_module.GeometryScreen(q, args.repo, budgets,envelope=envelope,
        reach_ratio=args.reach_ratio, reach_safety_factor=args.reach_safety_factor,
        amplitude_top_radius=args.amplitude_top_radius,
        amplitude_top_distance=args.amplitude_top_distance)
    packet_recorder = root_packets.NormalRootPacketRecorder(q,repo=args.repo,
        outdir=args.outdir/'immutable-normal-root-packets',caller_source=__file__,source_paths=paths)
    initial_envelope_metadata=envelope.metadata()
    independent_target_validation=history_record.get('independent_fixed_target_validation')
    independent_target=(initial_envelope_metadata['historical_address_binding']['actual_path_binding']['fixed_target_definition']
        if independent_target_validation is not None else None)
    report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,
        R729_common_slack_recovery_definition=r729.definition(),
        workflow_trigger_commit=os.environ.get('GITHUB_SHA'), github_run_id=os.environ.get('GITHUB_RUN_ID'),
        source_paths={role: str(path) for role, path in paths.items()},
        source_sha256_by_role={role: sha(path) for role, path in paths.items()},
        complete=False, independent_preparation_report=file_record(args.preparation_report),
        normal_root_packet_source=file_record(paths['root_packets']),
        normal_root_packet_definition=root_packets.definition(),normal_root_packet_record_only=True,
        normal_root_packets=packet_recorder.metadata(),normal_root_packet_latest_entry_capture=None,
        input_bundle=str(args.reference_bundle), bundle_sha256=sha(args.reference_bundle),
        independent_reference_binding=reference_binding,
        actual_fixed_reference_input_binding=fixed_input_binding,
        predeclared_mathematical_target_identity_sha256=fixed_input_binding['mathematical_target_identity_sha256'],
        predeclared_new_fixed_fejer_target=True,
        historical_literal_requests_reinterpreted_not_same_physical_points=True,
        previous_target_completion_or_unknown_typed_history_reconstructed=False,
        observation_carrier=str(args.carrier), observation_carrier_sha256=sha(args.carrier),
        exact_tail_node_report_sha256=sha(args.node_report),
        exact_tail_scalar_input_sha256=sha(args.scalar_input),
        independent_reference_context=context.metadata(), model_identity_sha256=q.identity,
        M=q.M, J=q.J, N=q.full_N, all_full_rows=3*q.P*q.full_N,
        evaluated_orbit_rows=3*q.P*q.N, original_variables=q.free_size,
        fixed_scalar_metric=dict(identity_sha256=fixed_profile,
            exact_profile_definition=context.scalar_definition,
            target_fixed_before_first_direction=True, target_recomputed_from_current_field=False,
            moving_mean_projection=False, all_metric_mean_constraints_retained=True,
            formula='ds^2+a_deep(s)^2*dtheta0^2; fixed initial-core theta0 chart'),
        representation=q.model, coordinate_norm=coordinates.record,
        reference_centering_definition=q.reference_calibration.definition,
        reference_centering_source=file_record(paths['reference_calibration']),
        normal_frame_C1_reuse_definition=q.frame_c1.definition,
        normal_frame_C1_source=file_record(paths['frame_C1']),
        detached_stage_matrix_reuse_definition=q.stage_matrices.definition,
        detached_stage_matrix_source=file_record(paths['stage_matrices']),
        adjacent_normal_frame_matrix_definition=q.adjacent_frames.definition,
        adjacent_normal_frame_matrix_source=file_record(paths['adjacent_matrices']),
        analytic_stage_jacobian_definition=q.analytic_stage_jacobian.definition,
        analytic_stage_jacobian_source=file_record(paths['analytic_J3']),
        analytic_stage_J3_full_original_residual_and_chain_retained=True,
        analytic_stage_J3_speedup_or_rounding_certified=False,
        analytic_normal_frame_definition=q.analytic_normal_frame.definition,
        analytic_normal_frame_source=file_record(paths['analytic_frame']),
        analytic_normal_frame_full_six_columns_and_active_graph_retained=True,
        analytic_normal_frame_speedup_or_rounding_certified=False,
        detached_closure_value_reuse_definition=q.detached_closure_values.definition,
        detached_closure_value_source=file_record(paths['closure_values']),
        closure_value_all_final_original_equation_checks_retained=True,
        closure_value_active_J_and_transpose_use_original=True,
        closure_value_speedup_rounding_or_root_certificate=False,
        detached_meridian_value_reuse_definition=q.detached_meridian_values.definition,
        detached_meridian_value_source=file_record(paths['detached_meridian_values']),
        meridian_value_original_implicit_and_query_formulas_retained=True,
        meridian_value_active_J_and_transpose_use_original=True,
        meridian_value_speedup_rounding_or_root_certificate=False,
        missing_angle_root_batch_policy=geometry_module.missing_angle_batch_policy(),
        missing_angle_root_batch_original_point_loop_and_domain_retained=True,
        missing_angle_root_batch_working_singleton_word_equality_claimed=False,
        actual_evaluation_progress_path=str(args.outdir/'actual-normal-evaluation-progress.json'),
        evaluation_progress_is_mutable_observation_not_scientific_input=True,
        adjacent_matrix_rounding_is_independent=True,
        adjacent_matrix_acceleration_or_error_certified=False,
        all_original_Newton_stage_equations_and_full_implicit_chain_retained=True,
        stage_matrix_cache_acceleration_or_rounding_certified=False,
        material_envelope_definition=envelope.definition,
        material_envelope_transfer=envelope_transfer_record,
        material_envelope_transfer_definition=envelope_transfer.definition(),
        material_envelope_transfer_source=file_record(paths['envelope_transfer']),
        explicit_prior_final_variable_seed_requested=args.material_envelope_seed_checkpoint is not None,
        prior_envelope_final_variable_seed=prior_final_seed,
        initial_full_variable_point_sha256=meridian.array_sha(x),
        material_envelope=initial_envelope_metadata,
        independent_fixed_target_definition=independent_target,
        independent_fixed_target_definition_identity_sha256=(None if independent_target is None else canonical(independent_target)),
        independent_fixed_target_validation=independent_target_validation,
        material_envelope_source=file_record(envelope_memory.__file__),
        material_envelope_rows_source=file_record(paths['envelope_rows']),
        material_envelope_near_active_rows=args.envelope_near_active_rows,
        material_envelope_active_band=args.active_band,
        material_envelope_new_working_set_policy=True,
        full_material_envelope_nonlinear_responsibility=True,
        unknown_historical_protected_labels_reconstructed=False,
        old_protected_required_priority_equivalence_claimed=False,
        all_normal_stage_equations_and_matrices_retained_with_frame_reuse=True,
        frame_reuse_speedup_or_rounding_certified=False,
        frozen_original_reference_point_sha256=q.reference_point_sha256,
        complete_current_raw_closure_lift_and_all_sixjet_derivatives_retained=True,
        raw_quadrature_defect_is_not_the_centred_root_residual=True,
        all_normal_stages_retained_at_literal_reference_zero=True,
        supported_unit_seed_definition=base.parent_jet.model,
        supported_unit_seed_identity_sha256=base.parent_jet.model_identity,
        supported_unit_seed_binding=base.parent_jet.binding,
        supported_unit_seed_is_frozen_from_original_core_and_height=True,
        supported_unit_seed_does_not_replace_current_outer_omega=True,
        supported_unit_mean_Jacobian_is_not_a_normal_control_inverse_certificate=True,
        original_complete_reference_and_fixed_scalar_retained=True,
        frozen_moment_Q_input=frozen_moment_input,
        frozen_moment_Q_definition_identity_sha256=moment_definition_identity,
        frozen_moment_Q_input_record=moment_input_record,
        actual_reference_initial_full_point_sha256=meridian.array_sha(base.initial()),
        moment_Q_recomputed_from_current_free_point=False,
        normal_auxiliary_nodes_are_physical_flex=False,
        normal_selection_changes_fixed_g=False,
        numerical_normal_stage_iterations_differentiated=False,
        final_implicit_J_uses_all_normal_stage_equations=True,
        previous_normal_frame_full_parameter_chain_retained=True,
        original_zero_control_target_full_parameter_chain_retained=True,
        final_original_physical_closure_is_separately_checked=False,
        final_reference_centred_closure_is_separately_checked=True,
        raw_physical_closure_is_retained_in_complete_lift=True,
        moment_input_binding_mode=args.moment_input_binding,
        implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
        normal_stage_count=q.normal_stage_count,
        exact_normal_step_nodes=[str(v) for v in q.normal_step_nodes],
        complete_first_angular_implicit_dimension=6*q.normal_stage_count,
        complete_second_angular_implicit_dimension=9*q.normal_stage_count,
        stationary_KKT_selection_used=False,continuous_horizontal_ODE_solution_claimed=False,
        common_partition_for_all_angles_and_free_points=True,per_angle_adaptive_normal_partition=False,
        old_zero_field_or_root_certificate_inherited=False,
        changed_control_map_has_independent_model_identity=True,
        radial_weights=dict(legacy_fraction=args.legacy_fraction, normalizer=normalizer,
            positive_stage_weights_sha256=meridian.array_sha(stage_weights),
            positive_orbit_weights_sha256=meridian.array_sha(q.multiplicity),
            fixed_target_a_carrier_sha256=meridian.array_sha(q.a),
            every_original_row_positive=True),
        spectral_parameters=parameters.as_dict(), selected_scalar_objective_key=objective_key,
        numerical_reach_safety_factor=args.reach_safety_factor,
        amplitude_design_constraints=dict(budgets=budgets.metadata()),
        history=history_record, initial_permanent_position_counts=dict(curvature=len(witnesses), radius=len(radius_witnesses)),
        permanent_position_identity='cell and literal binary64 u/phi; no decimal rounding or byte cap',
        restart=None if restart is None else dict(report=file_record(args.restart_report),
            checkpoint=file_record(args.restart_checkpoint), previous_final_Phi_not_used_as_new_measure_value=True),
        new_zero_closure_seed_changes_physical_field=(None if prior_final_seed is not None else restart is None),
        direct_base_seed=None if seed_report is None else dict(report=file_record(args.seed_so3_report),
            checkpoint=file_record(args.seed_so3_checkpoint), actual_base_model_identity_sha256=base.identity,
            all_original_variables_copied=True, old_Phi_or_certificates_inherited=False),
        radial_metric_error_identically_zero=False,
        accurate_zero_root_radial_metric_identity=True,
        radial_identity_scope='only exact reference and complete final implicit roots; WORKING Fs includes the actual complete raw lift',
        radial_Gram_uses_complete_hprime_Delta=True,
        numerical_radial_Gram_row_retained=True,
        endpoint_implicit_J_separate_from_Newton=True,
        old_continuous_geometry_certificates_inherited=False,
        old_metric_acceptance_inherited=False,
        new_geometry_and_metric_reread_before_any_acceptance=True,
        maximum_requested_metric_directions=args.directions,
        maximum_requested_restoration_directions=args.restoration_directions,
        maxiter=args.maxiter, initial_damping=args.damping,
        restoration_damping=args.restoration_damping,
        restoration_maxiter=args.restoration_maxiter,
        initial_zero_feasibility_not_assumed=True,
        common_slack_residual_never_called_geometric_feasibility=True,
        target=args.target, target_is_not_README_original_solver_floor=True,
        metric_directions=[], restoration_directions=[],
        continuous_metric_certified=False, continuous_geometry_certified=False,
        closed_isometry_accepted=False,
        working_evaluation=dict(integration_order=args.integration_order,
            inverse_root_iterations=args.inverse_root_iterations,
            inverse_root_tolerance=args.inverse_root_tolerance, angle_block=args.angle_block,
            endpoint_root_policy=root_policy.metadata(),
            normal_stage_count=q.normal_stage_count,
            exact_normal_step_nodes=[str(v) for v in q.normal_step_nodes],
            actual_normal_step_carriers_binary64_hex=[v.hex() for v in q.normal_step_carriers],
            exact_relative_bubble_nodes=q.model['exact_relative_bubble_nodes'],
            exact_relative_gamma_nodes=q.model['exact_relative_gamma_nodes'],
            implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
            complete_first_angular_implicit_dimension=6*q.normal_stage_count,
            complete_second_angular_implicit_dimension=9*q.normal_stage_count,
            fixed_moment_Q_definition_identity_sha256=moment_definition_identity,
            old_endpoint_coordinate_ball_certificate_inherited=False,
            torch_threads=args.torch_threads, torch_version=meridian.torch.__version__,
            numpy_version=np.__version__, scipy_version=scipy.__version__,
            quadrature_error_enclosed=False, root_error_enclosed=False,
            evaluation_refinement_changes_exact_target=False))

    scalar_progress_module=load('_actual_fixed_fejer_mathematical_progress',paths['scalar_progress'])
    mathematical_progress=scalar_progress_module.Recorder(args.outdir/'actual-mathematical-progress.json',report)
    report.update(mathematical_progress_source=file_record(paths['scalar_progress']),
        mathematical_progress_definition=scalar_progress_module.definition(),
        actual_mathematical_observation=None)

    def observe_mathematical(event_name,value,point,*,phase=None,serial=None):
        try:
            digest_started=time.monotonic()
            actual_point_sha256=meridian.array_sha(point)
            digest_seconds=time.monotonic()-digest_started
            mathematical_progress.observe(event_name,value,point_sha256=actual_point_sha256,
                phase=phase,serial=serial,point_digest_seconds=digest_seconds)
        except Exception as error:
            mathematical_progress.failure(event_name,error)

    def save_report():
        report['latest_operator_metadata'] = q.metadata()
        report['normal_root_packet_latest_entry_capture'] = packet_recorder.capture_entry(
            report['latest_operator_metadata'],outer_full_point_sha256=meridian.array_sha(x),
            witnesses=witnesses,radius_witnesses=radius_witnesses,label='actual-report-save')
        report['normal_root_packets'] = packet_recorder.metadata()
        report['material_envelope'] = envelope.metadata()
        report['current_permanent_position_counts'] = dict(curvature=len(witnesses), radius=len(radius_witnesses))
        report['peak_rss_KiB'] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        try:
            report['actual_mathematical_observation']=mathematical_progress.report_snapshot(report)
        except Exception as error:
            report['actual_mathematical_observation']=None
            mathematical_progress.failure('report-snapshot',error)
        write_json(output, report)
        try:
            mathematical_progress.report_saved(report)
        except Exception as error:
            mathematical_progress.failure('report-saved',error)

    def statistics(point, native):
        raw = q.unweight(native)
        e, f, d = raw[..., 0], raw[..., 1], raw[..., 2]
        spectrum = spectral.statistics(raw, stage_weights, q.multiplicity, parameters)
        spectrum = centered.augment_statistics(raw, stage_weights, q.multiplicity, parameters,
            spectrum, stage_block=args.stage_block)
        old = raw[:q.legacy_P]
        maximum = lambda a: float(np.max((np.abs(a[..., 0]+a[..., 2])
            +np.hypot(a[..., 0]-a[..., 2], 2*a[..., 1]))/2))
        return dict(spectral=spectrum, max_relative_gram=maximum(raw), legacy_max_relative_gram=maximum(old),
            min_relative_E=float(np.min(1+e)),
            min_relative_determinant=float(np.min((1+e)*(1+d)-f*f)),
            fixed_scalar_metric_identity_sha256=fixed_profile, fixed_target=True,
            full_metric_mean_and_cross_rows_retained=True, domain=q.domain(point),
            endpoint_roots=endpoint_readout(q))

    def remember(geometry):
        # The screen returns exact physical locations actually read on this
        # field. Both complete permanent memories remain append-only.
        added = dict(curvature=0, radius=0)
        for value in geometry.get('new_curvature_locations', []):
            added['curvature'] += int(add_location(value, witnesses, q))
        for value in geometry.get('new_radius_locations', []):
            added['radius'] += int(add_location(value, radius_witnesses, q))
        return added

    def scan(point):
        result = screen.scan(point, witnesses, radius_witnesses)
        result['newly_remembered'] = remember(result)
        return result

    def physical_violation(geometry):
        if not geometry.get('complete', False):
            return None
        value = geometry.get('maximum_physical_g')
        if value is None or not math.isfinite(float(value)):
            return None
        return max(0., float(value))

    def geometric_feasible(geometry):
        return bool(geometry.get('complete', False) and geometry.get('passed', False)
            and physical_violation(geometry) == 0.)

    write_json(output, report)
    event(event='SO3_actual_complete_problem_prepared', model_identity_sha256=q.identity,
        fixed_scalar_metric_identity_sha256=fixed_profile, free_variables=q.free_size,
        full_orbit_rows=3*q.P*q.full_N, actual_quarter_rows=3*q.P*q.N,
        integration_order=args.integration_order, next_actual_operation='complete_new_field_metric_and_geometry')
    try:
        q.detached_closure_values.progress('initial-complete-residual-start',force=True)
        native = q.residual(x)
        q.detached_closure_values.progress('initial-complete-residual-returned',force=True)
        q.detached_closure_values.progress('initial-complete-statistics-start',force=True)
        current = statistics(x, native)
        observe_mathematical('initial-statistics-returned',current,x)
        q.detached_closure_values.progress('initial-complete-statistics-returned',force=True)
        q.detached_closure_values.progress('initial-complete-geometry-start',force=True)
        geometry = scan(x)
        observe_mathematical('initial-geometry-returned',geometry,x)
        q.detached_closure_values.progress('initial-complete-geometry-returned',force=True)
    except (ValueError, RuntimeError, FloatingPointError, OverflowError) as error:
        report.update(complete=False, stop_reason='actual_initial_zero_closure_field_read_failed',
            actual_initial_read_error=repr(error), initial_endpoint_roots=endpoint_readout(q),
            total_actual_seconds=time.monotonic()-total_started,
            initial_failed_candidate_is_not_an_accepted_field=True)
        save_report()
        event(event='zero_closure_actual_initial_field_failure', report=str(output), error=repr(error),
            endpoint_roots=report['initial_endpoint_roots'], global_nonexistence_claimed=False)
        raise
    report['initial'] = current
    report['initial_geometry'] = geometry
    initial = args.outdir/'initial-new-field.npz'
    q.save(initial, x)
    report['initial_new_bundle'] = file_record(initial)
    report['current'] = current
    report['initial_actual_setup_and_full_read_seconds'] = time.monotonic()-total_started
    save_report()
    event(event='SO3_complete_new_field_initial_read', statistics=current,
        geometry_complete=geometry.get('complete'), geometric_feasible=geometric_feasible(geometry),
        maximum_physical_g=geometry.get('maximum_physical_g'))
    damping, restoration_damping = args.damping, args.restoration_damping
    metric_count, restoration_count, serial = 0, 0, 0
    stop_reason = 'declared_metric_direction_budget'
    while metric_count < args.directions:
        # Rejected trials can discover new permanent locations. The SAME
        # current parent is reread against that expanded set before its C.
        geometry = scan(x)
        observe_mathematical('current-geometry-returned',geometry,x)
        feasible = geometric_feasible(geometry)
        if physical_violation(geometry) is None:
            stop_reason = 'current_true_geometry_not_defined; no linearization or global impossibility claimed'
            break
        phase = 'metric' if feasible else 'restoration'
        if phase == 'restoration' and restoration_count >= args.restoration_directions:
            stop_reason = 'declared_restoration_budget; actual_violation_remains_and_is_not_accepted'
            break
        if phase == 'metric' and current['max_relative_gram'] <= args.target:
            stop_reason = 'actual_sample_target_reached; no_continuous_or_refinement_claim'
            break
        started = time.monotonic()
        operator_counts_before = dict(q.counts)
        C, bounds, rows = screen.build_rows(x, coordinates.transpose,
            coordinate_size=q.free_size, witnesses=witnesses, radius_witnesses=radius_witnesses,
            current_geometry=geometry, matrix_workdir=args.outdir/f'rows-{serial:03d}',
            max_rows=args.active_rows, active_band=args.active_band,
            block_columns=args.active_block_columns)
        if rows.get('no_original_row_removed') is not True:
            raise ValueError('The original full 192 selection prefix must remain in every phase')
        if len(rows['rows']) != C.shape[0] or bounds.shape != (C.shape[0],):
            raise ValueError('Every selected row must keep its actual bound and full metadata')
        serial += 1
        record = dict(index=metric_count if phase == 'metric' else restoration_count,
            serial=serial-1, phase=phase, starting_statistics=current,
            starting_geometry=geometry, complete_selected_inequalities=rows,
            accepted=False, trials=[], original_geometry_rows_retained=rows['original_prefix_rows'],
            appended_amplitude_rows=rows['appended_amplitude_rows'])
        record['full_geometry_and_row_preparation_seconds'] = time.monotonic()-started
        if phase == 'metric':
            if np.min(bounds, initial=0.) < -args.qp_feasibility_tolerance:
                raise ValueError('The full typed C contradicts the freshly read feasible parent')
            bridge = hessian.NativeLinearization(q, x, stage_weights, parameters, spectral_module=spectral)
            factor = math.sqrt(parameters.k/(parameters.scale**2*normalizer))
            residual = factor*bridge.residual
            A = LinearOperator((len(residual), q.free_size), dtype=np.float64,
                matvec=lambda z: factor*bridge.operator.matvec(coordinates.lift(z)),
                rmatvec=lambda v: factor*coordinates.transpose(bridge.operator.rmatvec(v)))
            used_damping, maxiter = damping, args.maxiter
            record['quadratic_model'] = dict(schema='complete-SO3-R664-positive-residual-Hessian-v1',
                bridge=bridge.metadata(), outer_half_Hessian_factor=factor*factor,
                gradient_and_Hessian_units_unchanged_from_declared_Phi=True,
                physical_coordinate_norm=coordinates.record, damping=used_damping,
                virtual_rhs_norm_is_actual_Phi=False, all_metric_mean_constraints_retained=True)
            solve_C, solve_bounds = C, bounds
        else:
            relaxed = CommonSlackRows(C, bounds, rows)
            residual = np.array([relaxed.tau0])
            A = LinearOperator((1, q.free_size+1), dtype=np.float64,
                matvec=lambda z: np.array([np.asarray(z)[-1]]),
                rmatvec=lambda v: np.r_[np.zeros(q.free_size), np.asarray(v)[0]])
            used_damping, maxiter = restoration_damping, args.restoration_maxiter
            record['quadratic_model'] = dict(relaxed.record, damping=used_damping,
                original_geometry_rows_retained=rows['original_prefix_rows'],
                amplitude_rows_retained=rows['appended_amplitude_rows'])
            solve_C, solve_bounds = relaxed, relaxed.bounds
        record['actual_full_linearization_preparation_seconds'] = time.monotonic()-started
        event(event='SO3_actual_complete_quadratic_model_ready', phase=phase, serial=serial-1,
            full_variable_count=int(A.shape[1]), selected_row_count=int(solve_C.shape[0]),
            preparation_seconds=record['actual_full_linearization_preparation_seconds'],
            old_maximum_gram=current['max_relative_gram'],
            old_positive_physical_g=physical_violation(geometry), damping=used_damping)
        qp_started = time.monotonic()
        qp_counts_before = dict(q.counts)
        coordinate_step, qp_report = qp.solve(A, residual, solve_C, solve_bounds,
            damping=used_damping, block_columns=args.active_block_columns,
            parameters=qp.Parameters(maxiter=maxiter, atol=args.qp_atol, rtol=args.qp_rtol,
                feasibility_tolerance=args.qp_feasibility_tolerance,
                rank_tolerance=args.qp_rank_tolerance, progress_every=1),
            callback=lambda value: event(event='SO3_actual_QP_progress', phase=phase, serial=serial-1, progress=value))
        record['qp'] = qp_report
        coordinate_step=r729.recover(coordinate_step,qp_report,solve_C,solve_bounds,
            record=record,model_identity=q.identity,args=args,phase=phase,damping=used_damping)
        record['actual_QP_seconds'] = time.monotonic()-qp_started
        record['actual_QP_operator_counts'] = {key: q.counts[key]-qp_counts_before[key] for key in q.counts}
        record['normal_root_packet_at_QP_return'] = packet_recorder.capture_entry(q.metadata(),
            outer_full_point_sha256=meridian.array_sha(x),witnesses=witnesses,
            radius_witnesses=radius_witnesses,label=phase+'-QP-return-'+str(record['serial']))
        record['actual_damping'] = used_damping
        record['coordinate_step_norm'] = float(np.linalg.norm(coordinate_step))
        physical_coordinate_step = coordinate_step if phase == 'metric' else coordinate_step[:-1]
        original_linear_values = qp.StreamedRows(C, args.active_block_columns).matvec(physical_coordinate_step)
        record['selected_linear_physical_g'] = [float(row['physical_g']
            +row['row_normalization_scale']*value)
            for row, value in zip(rows['rows'], original_linear_values)]
        record['maximum_selected_linear_physical_g'] = max(record['selected_linear_physical_g'], default=None)
        step = coordinates.lift(physical_coordinate_step)
        old_merit = current['spectral'][objective_key]
        old_violation = physical_violation(geometry)
        if phase == 'metric':
            linear = A.matvec(coordinate_step)
            half_slope = float(residual@linear)
            predicted = 2*half_slope+float(linear@linear)
            record.update(half_objective_slope=half_slope,
                predicted_actual_Phi_change=predicted, old_actual_Phi=old_merit)
        else:
            half_slope, predicted = None, None
            record['computed_common_slack'] = float(relaxed.tau0+coordinate_step[-1])
            record['common_slack_not_used_as_nonlinear_feasibility'] = True
        record['old_actual_maximum_positive_physical_g'] = old_violation
        step_path = args.outdir/f'{phase}-direction-{record["index"]:03d}.npz'
        np.savez(step_path, full_physical_step=step, coordinate_step=coordinate_step,
            representation_identity_sha256=np.array(q.identity))
        record['direction'] = file_record(step_path)
        # Release the full positive residual-Hessian storage before trials.
        if phase == 'metric':
            del bridge
        del A, residual, coordinate_step, solve_C, solve_bounds
        alpha = 1.
        for trial_index in range(args.line_trials):
            trial_started = time.monotonic()
            candidate = x+alpha*step
            trial = dict(index=trial_index, alpha=alpha, accepted=False,
                metric_descent_required=phase == 'metric', full_true_geometry_read=False)
            observe_mathematical('trial-start',trial,candidate,phase=phase,serial=record['serial'])
            trial_native, trial_statistics, trial_geometry = None, None, None
            try:
                trial_native = q.residual(candidate)
                trial_statistics = statistics(candidate, trial_native)
                observe_mathematical('trial-statistics-returned',trial_statistics,candidate,phase=phase,serial=record['serial'])
                domain_ok = (trial_statistics['min_relative_E'] > 0
                    and trial_statistics['min_relative_determinant'] > 0)
                trial_merit = trial_statistics['spectral'][objective_key]
                descent = (trial_merit < old_merit and (half_slope is None or half_slope >= 0
                    or trial_merit <= old_merit+.0002*alpha*half_slope))
                if domain_ok and (phase == 'restoration' or descent):
                    trial_geometry = scan(candidate)
                    observe_mathematical('trial-geometry-returned',trial_geometry,candidate,phase=phase,serial=record['serial'])
                    trial['full_true_geometry_read'] = True
                trial_violation = None if trial_geometry is None else physical_violation(trial_geometry)
                if phase == 'metric':
                    accepted = domain_ok and descent and trial_geometry is not None and geometric_feasible(trial_geometry)
                else:
                    accepted = (domain_ok and trial_violation is not None
                        and trial_violation < old_violation
                        and trial_violation <= (1-1.e-4*alpha)*old_violation)
                trial.update(statistics=trial_statistics, domain_feasible=domain_ok,
                    actual_Phi_descent=descent, actual_positive_physical_g=trial_violation,
                    full_geometry=trial_geometry, accepted=bool(accepted),
                    physically_feasible=False if trial_geometry is None else geometric_feasible(trial_geometry))
            except (FloatingPointError, OverflowError, ValueError, RuntimeError) as exception:
                accepted = False
                trial.update(actual_read_error=repr(exception), accepted=False,
                    complete=False, scope='A true numerical trial failure, not global infeasibility')
            trial['endpoint_roots'] = endpoint_readout(q)
            trial['actual_seconds'] = time.monotonic()-trial_started
            record['trials'].append(trial)
            observe_mathematical('trial-decision-returned',trial,candidate,phase=phase,serial=record['serial'])
            event(event='SO3_actual_trial', phase=phase, serial=serial-1,
                index=trial_index, alpha=alpha, accepted=bool(accepted),
                maximum_gram=None if trial_statistics is None else trial_statistics['max_relative_gram'],
                actual_Phi=None if trial_statistics is None else trial_statistics['spectral'][objective_key],
                actual_positive_physical_g=trial.get('actual_positive_physical_g'),
                actual_read_error=trial.get('actual_read_error'))
            if accepted:
                x, native, current, geometry = candidate, trial_native, trial_statistics, trial_geometry
                record.update(accepted=True, accepted_alpha=alpha, accepted_statistics=current,
                    accepted_geometry=geometry)
                accepted_path = args.outdir/f'accepted-{phase}-{record["index"]:03d}.npz'
                q.save(accepted_path, x)
                record['accepted_bundle'] = file_record(accepted_path)
                observe_mathematical('accepted-checkpoint-returned',record,x,phase=phase,serial=record['serial'])
                if phase == 'metric':
                    ratio = (old_merit-current['spectral'][objective_key])/(-predicted) if predicted < 0 else None
                    record['actual_to_full_prediction_ratio'] = ratio
                    if alpha == 1 and ratio is not None and ratio > .75:
                        damping = max(1.e-8, damping/2)
                elif geometric_feasible(geometry):
                    record['actual_restoration_reached_zero_true_violation'] = True
                break
            alpha /= 2
        if not record['accepted']:
            if phase == 'metric':
                damping *= 4
            else:
                restoration_damping *= 4
        record['seconds'] = time.monotonic()-started
        record['actual_complete_direction_operator_counts'] = {
            key: q.counts[key]-operator_counts_before[key] for key in q.counts}
        record['damping_after_direction'] = damping if phase == 'metric' else restoration_damping
        report[phase+'_directions'].append(record)
        report['current'] = current
        if phase == 'metric':
            metric_count += 1
        else:
            restoration_count += 1
        q.clear_base()
        del C, bounds, step
        if phase == 'restoration':
            del relaxed
        save_report()
    # All newly found addresses are screened on the SAME final field. The
    # screen itself has already read any extrema it proposes remembering.
    geometry = scan(x)
    observe_mathematical('final-geometry-returned',geometry,x)
    current = statistics(x, q.residual(x))
    observe_mathematical('final-statistics-returned',current,x)
    final = args.outdir/'final.npz'
    q.save(final, x)
    report.update(complete=True, stop_reason=stop_reason, final_statistics=current,
        total_actual_seconds=time.monotonic()-total_started,
        current=current, final_geometry=geometry, final_bundle=str(final), final_bundle_sha256=sha(final),
        final_damping=damping, final_restoration_damping=restoration_damping,
        actual_metric_directions=metric_count, actual_restoration_directions=restoration_count,
        actual_accepted_metric_directions=sum(bool(r['accepted']) for r in report['metric_directions']),
        actual_accepted_restoration_directions=sum(bool(r['accepted']) for r in report['restoration_directions']),
        final_curvature_memory=witnesses, final_radius_memory=radius_witnesses,
        final_permanent_position_counts=dict(curvature=len(witnesses), radius=len(radius_witnesses)),
        final_true_sampled_geometry_feasible=geometric_feasible(geometry),
        sample_target_reached=current['max_relative_gram'] <= args.target,
        independent_reference_context_final=context.metadata(),
        limitations='A complete finite new implicit-zero-closure field solve, not a closed-isometry or reach certificate. The full R695 uniform root conditions are unverified; successful numerical roots and first parameter implicit derivatives do not certify a continuous root branch. Ordinary quadrature, scalar-carrier normalization, core inverse roots and metric/geometry maxima need continuous same-field error bounds. Core/cap C2 identities are structural in the exact formula and their numerical evaluation errors remain unpaid. Full all-t and E3/held obligations, fixed-problem radial/angular/evaluation refinement and a meaningful solver floor remain. Restored common slack or a budget limit never proves physical feasibility, nonexistence or convergence.')
    save_report()
    event(event='SO3_complete_actual_numerical_budget_returned', report=str(output),
        final_bundle_sha256=sha(final), sample_target_reached=report['sample_target_reached'],
        true_sampled_geometry_feasible=report['final_true_sampled_geometry_feasible'],
        statistics=current, stop_reason=stop_reason)


if __name__ == '__main__':
    main()
