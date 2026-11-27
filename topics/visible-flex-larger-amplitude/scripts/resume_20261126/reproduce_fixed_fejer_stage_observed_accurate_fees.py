#!/usr/bin/env python3
"""Reproduce complete stage-observed accurate fee sources and full parameters.

This standard-library utility reads only complete already published source
and parameter parents. It runs no scientific code, imports no scientific
module, and is not a preflight or admission step for any solver or fee.
The emitted sources execute accurate field work only in public Actions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CONSTRUCTION = json.loads(r"""{
  "schema": "complete-stage-observed-accurate-fee-source-and-parameter-reproduction-v1",
  "source_derivations": [
    {
      "role": "input",
      "parent": {
        "role": "input",
        "name": "fixed_fejer_normal_packet_accurate_field_input.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_normal_packet_accurate_field_input.py",
        "bytes": 32991,
        "sha256": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
        "git_blob_sha": "46ee6fd8157265253259a642844783ea4cd712bb"
      },
      "output": {
        "role": "input",
        "name": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
        "bytes": 33017,
        "sha256": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
        "git_blob_sha": "eabc6d900dad8b46dc731fd4de9159b4050bb54d"
      },
      "patches": [
        {
          "before": "read_fixed_fejer_immutable_point_so3_report.py",
          "after": "read_fixed_fejer_stage_point_observed_so3_report.py",
          "count": 1
        },
        {
          "before": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
          "after": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "count": 1
        },
        {
          "before": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
          "after": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
          "count": 1
        },
        {
          "before": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
          "after": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "count": 1
        },
        {
          "before": "fixed_fejer_immutable_normal_root_packets.py",
          "after": "fixed_fejer_stage_point_root_packets.py",
          "count": 1
        },
        {
          "before": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
          "after": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
          "count": 1
        },
        {
          "before": "fixed_fejer_normal_lift_operator.py",
          "after": "fixed_fejer_stage_point_normal_lift.py",
          "count": 1
        },
        {
          "before": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
          "after": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
          "count": 1
        },
        {
          "before": "fixed_fejer_complete_source_binding.py",
          "after": "fixed_fejer_stage_point_source_binding.py",
          "count": 1
        },
        {
          "before": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
          "after": "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f",
          "count": 1
        },
        {
          "before": "ACTUAL_SOURCE_ROLE_COUNT = 110",
          "after": "ACTUAL_SOURCE_ROLE_COUNT = 120",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal-packet-accurate-field-input-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-normal-packet-accurate-field-input-v1",
          "count": 1
        }
      ]
    },
    {
      "role": "radial",
      "parent": {
        "role": "radial",
        "name": "fixed_fejer_accurate_reference_control_radial_boxes.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_accurate_reference_control_radial_boxes.py",
        "bytes": 45317,
        "sha256": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
        "git_blob_sha": "e572b4f4de1ebc3468d173989105f813675cab1b"
      },
      "output": {
        "role": "radial",
        "name": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
        "bytes": 45332,
        "sha256": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
        "git_blob_sha": "f969ad127bcbc0c43681c3e17e6cf63b0b6ab19f"
      },
      "patches": [
        {
          "before": "actual-fixed-fejer-complete-accurate-reference-control-radial-boxes-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-accurate-reference-control-radial-boxes-v1",
          "count": 1
        },
        {
          "before": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
          "after": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "count": 1
        }
      ]
    },
    {
      "role": "normal",
      "parent": {
        "role": "normal",
        "name": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_normal_root_and_sixjet_fees.py",
        "bytes": 40294,
        "sha256": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
        "git_blob_sha": "2aa3dc44a8ba8d61ec6ffa4de90c3dd61b2d85c2"
      },
      "output": {
        "role": "normal",
        "name": "fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
        "bytes": 40369,
        "sha256": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
        "git_blob_sha": "eed89ba9e5b606fb3ce27ffc54526db2a45fec1b"
      },
      "patches": [
        {
          "before": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
          "after": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "count": 1
        },
        {
          "before": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
          "after": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal-root-and-physical-sixjet-fees-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-normal-root-and-physical-sixjet-fees-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal-fee-journal-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-normal-fee-journal-v1",
          "count": 1
        },
        {
          "before": "complete-actual-fixed-fejer-accurate-physical-sixjet-stream-v1",
          "after": "complete-actual-fixed-fejer-stage-observed-accurate-physical-sixjet-stream-v1",
          "count": 1
        },
        {
          "before": "fixed_fejer_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "count": 1
        },
        {
          "before": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
          "after": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "count": 1
        },
        {
          "before": "fixed_fejer_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
          "after": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "count": 1
        }
      ]
    },
    {
      "role": "leaf",
      "parent": {
        "role": "leaf",
        "name": "fixed_fejer_complete_physical_leaf_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_physical_leaf_binding.py",
        "bytes": 47321,
        "sha256": "ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c",
        "git_blob_sha": "fbe38e6afce500e502ca9655dd784360f200f208"
      },
      "output": {
        "role": "leaf",
        "name": "fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
        "bytes": 47482,
        "sha256": "280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652",
        "git_blob_sha": "2884e1741f96a8e80b349fe023ef398b1a7ecd87"
      },
      "patches": [
        {
          "before": "read_fixed_fejer_immutable_point_so3_report.py",
          "after": "read_fixed_fejer_stage_point_observed_so3_report.py",
          "count": 1
        },
        {
          "before": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
          "after": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "count": 2
        },
        {
          "before": "fullclosed_fixed_fejer_immutable_point_so3_qp.py",
          "after": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
          "count": 1
        },
        {
          "before": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
          "after": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "count": 2
        },
        {
          "before": "fixed_fejer_immutable_normal_root_packets.py",
          "after": "fixed_fejer_stage_point_root_packets.py",
          "count": 1
        },
        {
          "before": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
          "after": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
          "count": 1
        },
        {
          "before": "fixed_fejer_normal_lift_operator.py",
          "after": "fixed_fejer_stage_point_normal_lift.py",
          "count": 1
        },
        {
          "before": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
          "after": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
          "count": 2
        },
        {
          "before": "fixed_fejer_complete_source_binding.py",
          "after": "fixed_fejer_stage_point_source_binding.py",
          "count": 1
        },
        {
          "before": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
          "after": "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal-packet-accurate-field-input-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-normal-packet-accurate-field-input-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-accurate-reference-control-radial-boxes-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-accurate-reference-control-radial-boxes-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal-root-and-physical-sixjet-fees-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-normal-root-and-physical-sixjet-fees-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal-fee-journal-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-normal-fee-journal-v1",
          "count": 1
        },
        {
          "before": "complete-actual-fixed-fejer-accurate-physical-sixjet-stream-v1",
          "after": "complete-actual-fixed-fejer-stage-observed-accurate-physical-sixjet-stream-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-physical-sixjet-leaf-reader-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-physical-sixjet-leaf-reader-v1",
          "count": 1
        },
        {
          "before": "fixed_fejer_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "count": 2
        },
        {
          "before": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
          "after": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "count": 2
        },
        {
          "before": "fixed_fejer_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
          "after": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "count": 1
        },
        {
          "before": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
          "after": "fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
          "count": 1
        },
        {
          "before": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
          "after": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
          "count": 1
        }
      ]
    },
    {
      "role": "geometry",
      "parent": {
        "role": "geometry",
        "name": "fixed_fejer_continuous_gram_curvature_support.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_continuous_gram_curvature_support.py",
        "bytes": 46689,
        "sha256": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b",
        "git_blob_sha": "368afa8be43c26eecdd13ef5466fe9de56b5afec"
      },
      "output": {
        "role": "geometry",
        "name": "fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
        "bytes": 46719,
        "sha256": "3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560",
        "git_blob_sha": "4837232aa3a2a14a6ab36c2f1cb98aaf05ed25cd"
      },
      "patches": [
        {
          "before": "actual-fixed-fejer-complete-continuous-gram-curvature-support-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-v1",
          "count": 1
        },
        {
          "before": "fixed_fejer_complete_physical_leaf_binding.py",
          "after": "fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
          "count": 1
        },
        {
          "before": "ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c",
          "after": "280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652",
          "count": 1
        }
      ]
    },
    {
      "role": "bridge",
      "parent": {
        "role": "bridge",
        "name": "fixed_fejer_complete_geometry_support_beta_bridge.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_support_beta_bridge.py",
        "bytes": 20810,
        "sha256": "ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15",
        "git_blob_sha": "3c6b9b259bb20231ca607192510f235315fb1f5e"
      },
      "output": {
        "role": "bridge",
        "name": "fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py",
        "bytes": 20870,
        "sha256": "35493133665555aecf40eb85d213d53fb2b4fbf4acf949b403c258cbb24787a0",
        "git_blob_sha": "b8975cf1054fcd5dde9525e3e2375e7e9e3e640b"
      },
      "patches": [
        {
          "before": "actual-fixed-fejer-complete-geometry-to-conditional-R650-beta-bridge-v1",
          "after": "actual-fixed-fejer-stage-observed-complete-geometry-to-conditional-R650-beta-bridge-v1",
          "count": 1
        },
        {
          "before": "fixed_fejer_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "count": 1
        },
        {
          "before": "fixed_fejer_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "fixed_fejer_continuous_gram_curvature_support.py",
          "after": "fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
          "count": 1
        },
        {
          "before": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b",
          "after": "3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560",
          "count": 1
        }
      ]
    }
  ],
  "ready_derivations": [
    {
      "record": {
        "role": "normal_ready",
        "name": "fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
        "bytes": 10975,
        "sha256": "dc5e88a28167b2a06f0821448c07abbae6cc6ff91d3d5bac8547d03398296d2b",
        "git_blob_sha": "46c3ba9503e7b8e42a93bb6cf7ba5b18566de603"
      },
      "parent": {
        "role": "normal_ready",
        "name": "fixed-fejer-complete-normal32-full-circle-sixjet-fees-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-normal32-full-circle-sixjet-fees-ready.json",
        "bytes": 9380,
        "sha256": "d38cabbbc9dbc3dd973fe271de7085b9ab5a5f6d5b14df5476c22fba3b91fafa",
        "git_blob_sha": "d00ea8dca3607ddb6e383a003044f4c8005fa331"
      },
      "patches": [
        {
          "before": "fixed_fejer_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "count": 1
        },
        {
          "before": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
          "after": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "count": 1
        },
        {
          "before": "fixed_fejer_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
          "after": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "count": 1
        },
        {
          "before": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
          "after": "fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
          "count": 2
        },
        {
          "before": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
          "after": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
          "count": 1
        },
        {
          "before": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
          "after": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "count": 1
        },
        {
          "before": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
          "after": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "count": 1
        },
        {
          "before": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
          "after": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
          "count": 1
        },
        {
          "before": "1445b883cbcf3ed76571760923c2dc735ead7c862439d9478684a5a5299de468",
          "after": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
          "count": 1
        },
        {
          "before": "fixed-fejer-immutable-point-first",
          "after": "fixed-fejer-stage-point-observed-independent",
          "count": 2
        },
        {
          "before": "fixed-fejer-normal-root-and-sixjet-fees-v1",
          "after": "fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1",
          "count": 3
        },
        {
          "before": "complete-fixed-fejer-normal-32-stage-and-full-angle-sixjet-fees-ready-v1",
          "after": "complete-fixed-fejer-stage-observed-normal-32-stage-and-full-angle-sixjet-fees-ready-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-complete-normal32-full-circle-sixjet-fees-first-20261127",
          "after": "actual-fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-first-20261127",
          "count": 1
        },
        {
          "before": "477499/274d",
          "after": "8dc9d876/c9ce27c7",
          "count": 1
        },
        {
          "before": "110-role",
          "after": "120-role",
          "count": 1
        }
      ],
      "added_metadata": {
        "complete_current_source_family": {
          "bytes": 41188,
          "sha256": "1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544",
          "git_blob_sha": "da1192313958df70ba3b95d5e302b34fe4a2cfc2",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-complete-delivery.json"
        },
        "complete_original_mathematical_stage_family": {
          "bytes": 74078,
          "sha256": "f0497fee9a867ea1b6aee90f7d15ccd86415e7bcd3aee64e597e18afc7424d04",
          "git_blob_sha": "7392fb1e01864e2f13bfc7d4ebae04465db229fa",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-complete-delivery.json"
        },
        "intended_actual_run_id": "46037017666",
        "intended_actual_run_attempt": 1,
        "actual_mathematical_observation_not_a_fee_input": true,
        "requires_complete_immutable_normal_packet_snapshot": true,
        "current_M": 160,
        "current_N": 2048,
        "current_J": 923,
        "reference_M": 160,
        "reference_N": 2048,
        "reference_J": 923,
        "complete_scientific_runtime_source_role_count": 120,
        "future_actual_full_point_sha256": null,
        "future_actual_snapshot_identity_sha256": null,
        "source_ready_or_input_or_mutable_progress_is_not_a_returned_field": true,
        "whole_stage_math_scalar_observer_does_not_change_accurate_field_equations": true
      },
      "scope_append": " The exact 120-role stage-point/math-progress entry is bound in full. The actual_mathematical_observation object is not used as a physical field, immutable snapshot or error certificate."
    },
    {
      "record": {
        "role": "geometry_ready",
        "name": "fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
        "bytes": 11490,
        "sha256": "049776de848bb0563d1a0ee6438201d2529b470375adb23dd9eb651ebfe751d6",
        "git_blob_sha": "177b4ca2c3566e84cfacbf0bcdfd10f50b0aa909"
      },
      "parent": {
        "role": "geometry_ready",
        "name": "fixed-fejer-complete-continuous-gram-curvature-support-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-continuous-gram-curvature-support-ready.json",
        "bytes": 9901,
        "sha256": "a2171bdfafd5aa4b3a2c70d53b57bb7c055be4dc17d29138b77fed211323aae4",
        "git_blob_sha": "2beb63b4a5b9fcce3f981a31769a1fbeb67cc043"
      },
      "patches": [
        {
          "before": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
          "after": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "count": 1
        },
        {
          "before": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
          "after": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
          "count": 1
        },
        {
          "before": "fixed_fejer_complete_physical_leaf_binding.py",
          "after": "fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
          "count": 1
        },
        {
          "before": "ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c",
          "after": "280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652",
          "count": 1
        },
        {
          "before": "fixed_fejer_continuous_gram_curvature_support.py",
          "after": "fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
          "count": 2
        },
        {
          "before": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b",
          "after": "3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560",
          "count": 1
        },
        {
          "before": "fixed_fejer_complete_geometry_support_beta_bridge.py",
          "after": "fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py",
          "count": 2
        },
        {
          "before": "ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15",
          "after": "35493133665555aecf40eb85d213d53fb2b4fbf4acf949b403c258cbb24787a0",
          "count": 1
        },
        {
          "before": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
          "after": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "count": 1
        },
        {
          "before": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
          "after": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "count": 1
        },
        {
          "before": "fixed-fejer-normal-root-and-sixjet-fees-v1",
          "after": "fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1",
          "count": 2
        },
        {
          "before": "fixed-fejer-continuous-gram-curvature-support-v1",
          "after": "fixed-fejer-stage-observed-continuous-gram-curvature-support-v1",
          "count": 3
        },
        {
          "before": "complete-fixed-fejer-continuous-gram-curvature-support-ready-v1",
          "after": "complete-fixed-fejer-stage-observed-continuous-gram-curvature-support-ready-v1",
          "count": 1
        },
        {
          "before": "actual-fixed-fejer-whole-normal-leaf-continuous-gram-curvature-support-first-20261127",
          "after": "actual-fixed-fejer-stage-observed-whole-normal-leaf-continuous-gram-curvature-support-first-20261127",
          "count": 1
        },
        {
          "before": "genuine complete 1a915b fixed-Fejer",
          "after": "genuine complete 24765a stage-observed fixed-Fejer",
          "count": 1
        }
      ],
      "added_metadata": {
        "complete_current_source_family": {
          "bytes": 41188,
          "sha256": "1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544",
          "git_blob_sha": "da1192313958df70ba3b95d5e302b34fe4a2cfc2",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-complete-delivery.json"
        },
        "complete_original_mathematical_stage_family": {
          "bytes": 74078,
          "sha256": "f0497fee9a867ea1b6aee90f7d15ccd86415e7bcd3aee64e597e18afc7424d04",
          "git_blob_sha": "7392fb1e01864e2f13bfc7d4ebae04465db229fa",
          "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-complete-delivery.json"
        },
        "intended_actual_run_id": "46037017666",
        "intended_actual_run_attempt": 1,
        "actual_mathematical_observation_not_a_fee_input": true,
        "requires_complete_immutable_normal_packet_snapshot": true,
        "current_M": 160,
        "current_N": 2048,
        "current_J": 923,
        "reference_M": 160,
        "reference_N": 2048,
        "reference_J": 923,
        "complete_scientific_runtime_source_role_count": 120,
        "future_actual_full_point_sha256": null,
        "future_actual_snapshot_identity_sha256": null,
        "source_ready_or_input_or_mutable_progress_is_not_a_returned_field": true,
        "whole_stage_math_scalar_observer_does_not_change_accurate_field_equations": true
      },
      "scope_append": " This is the exact stage-point/math-progress source family; mutable scalar observations do not replace the complete root/physical-stream provenance."
    }
  ]
}""")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read_parent(repo, record, used):
    path = (repo / record["path"]).resolve()
    raw = path.read_bytes()
    actual = dict(path=str(path), bytes=len(raw), sha256=sha(raw))
    expected = dict(path=str(path), bytes=record["bytes"], sha256=record["sha256"])
    old = used.get(str(path))
    if old is not None and old != expected:
        raise ValueError("One complete parent path has incompatible identities")
    if actual != expected:
        raise ValueError("The complete published parent changed: " + record["path"])
    used[str(path)] = expected
    return raw.decode("utf-8")


def exact_patches(source, patches):
    value = source
    for patch in patches:
        before, after, count = patch["before"], patch["after"], patch["count"]
        if not before or before == after or value.count(before) != count:
            raise ValueError("An exact complete source replacement count changed")
        value = value.replace(before, after)
    reverse = value
    for patch in reversed(patches):
        if reverse.count(patch["after"]) != patch["count"]:
            raise ValueError("An exact inverse replacement count changed")
        reverse = reverse.replace(patch["after"], patch["before"])
    if reverse != source:
        raise ValueError("The full original source was not recovered by inverse text changes")
    return value


def checked_output(source, record):
    raw = source.encode("utf-8")
    if (len(raw) != record["bytes"] or sha(raw) != record["sha256"]
            or len(raw) >= 100000):
        raise ValueError("A complete intended output differs: " + record["name"])
    return raw


def build(repo):
    used, outputs = {}, {}
    for item in CONSTRUCTION["source_derivations"]:
        parent = read_parent(repo, item["parent"], used)
        source = exact_patches(parent, item["patches"])
        record = item["output"]
        if record["name"] in outputs:
            raise ValueError("Duplicate complete source output")
        outputs[record["name"]] = (checked_output(source, record), record)
    for item in CONSTRUCTION["ready_derivations"]:
        parent = read_parent(repo, item["parent"], used)
        changed = exact_patches(parent, item["patches"])
        value = json.loads(changed)
        value.update(item["added_metadata"])
        value["steps"][0]["scope"] += item["scope_append"]
        source = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
        record = item["record"]
        if record["name"] in outputs:
            raise ValueError("Duplicate complete parameter output")
        outputs[record["name"]] = (checked_output(source, record), record)
    for item in used.values():
        raw = Path(item["path"]).read_bytes()
        if len(raw) != item["bytes"] or sha(raw) != item["sha256"]:
            raise ValueError("A complete parent changed during text construction")
    return outputs, used


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--output-directory", required=True, type=Path)
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.output_directory.resolve()
    outputs, used = build(repo)
    for item in used.values():
        parent = Path(item["path"])
        if out == parent or out in parent.parents:
            raise ValueError("Output may not contain any complete consumed parent")
    for name, (raw, record) in outputs.items():
        path = out / name
        if path.exists() and path.read_bytes() != raw:
            raise ValueError("Do not replace an existing different source or parameter: " + name)
    out.mkdir(parents=True, exist_ok=True)
    for name, (raw, record) in outputs.items():
        path = out / name
        if not path.exists():
            with path.open("xb") as handle:
                handle.write(raw)
        if path.read_bytes() != raw:
            raise ValueError("A complete output changed while writing")
    print(json.dumps(dict(
        schema=CONSTRUCTION["schema"],
        complete_output_records=[record for raw, record in outputs.values()],
        all_complete_parent_bytes_rechecked=True,
        all_output_bytes_match_fixed_full_identities=True,
        scientific_modules_imported=False,
        scientific_execution=False,
        solver_or_fee_admission_gate=False), sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
