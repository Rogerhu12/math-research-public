#!/usr/bin/env python3
"""Reproduce six complete accurate-fee sources and both full meridian-batched plans.

Only complete declared source and parameter bytes are read. This program
imports no scientific module and evaluates no field, root, interval, array
or numerical fixture. It is a source recovery utility, not an admission
or preflight step. All generated scientific computation is Actions-only.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

CONSTRUCTION = json.loads(r"""{
  "schema": "complete-fixed-fejer-meridian-batched-accurate-source-and-parameter-reproduction-v1",
  "parent_delivery": {
    "bytes": 23822,
    "sha256": "6990d534425ba2db3116fa77f42f0ade241414502c619a86fbcf42d044f09067",
    "git_blob_sha": "6c7df82353fd9bb6b92af6ace319e17342b06d94",
    "name": "fixed-fejer-stage-observed-complete-accurate-fees-delivery.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-accurate-fees-delivery.json"
  },
  "current_scientific_source_family": {
    "definition": "The complete new scientific driver SOURCE_PINS and the exact new pure reader; no numerical return is inferred",
    "driver": {
      "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
      "bytes": 99313,
      "sha256": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
      "git_blob_sha": "df1023d71441a01e0dd1e343cb1431aa7553023e"
    },
    "reader": {
      "name": "read_fixed_fejer_meridian_batched_so3_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py",
      "bytes": 99382,
      "sha256": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52",
      "git_blob_sha": "66c92a656aff5df0013b9c7bf69c08e71aab87c3"
    },
    "normal": {
      "name": "fixed_fejer_detached_meridian_normal_lift.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
      "bytes": 96276,
      "sha256": "388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4",
      "git_blob_sha": "8a22b31dcc36d3160d4c968f9645600961a22abc"
    },
    "packets": {
      "name": "fixed_fejer_meridian_root_packets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py",
      "bytes": 73723,
      "sha256": "910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15",
      "git_blob_sha": "e347b156b0b4bec87871fc07809a40a3bbda4ddd"
    },
    "detached_meridian_values": {
      "name": "fixed_fejer_detached_meridian_values.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
      "bytes": 41030,
      "sha256": "7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd",
      "git_blob_sha": "6ab29473b0d549539de69a064efb19af4227a867"
    },
    "field_binding": {
      "name": "fixed_fejer_meridian_source_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_source_binding.py",
      "bytes": 41894,
      "sha256": "15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc",
      "git_blob_sha": "54d58893654598e94687a448e2beccc776e1cfb4"
    },
    "geometry": {
      "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
      "bytes": 88163,
      "sha256": "51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898",
      "git_blob_sha": "e66b17a5384ec29e11415d4eb6a6549594277436"
    },
    "lower_source_locks": {
      "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-detached-meridian-value-lower-source-locks.json",
      "bytes": 18987,
      "sha256": "969a1e676eab85c7497072d6a92f34dc037230da7aebf6227b0f343eded6aba3",
      "git_blob_sha": "4903cf3479cd6be661ec1b2734d8a52be0b4b308"
    },
    "complete_source_role_count": 137,
    "original_120_source_identities_remain_as_actual_parent_roles": true
  },
  "source_derivations": [
    {
      "role": "input",
      "parent": {
        "role": "input",
        "name": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
        "bytes": 33017,
        "sha256": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
        "git_blob_sha": "eabc6d900dad8b46dc731fd4de9159b4050bb54d"
      },
      "output": {
        "role": "input",
        "name": "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
        "bytes": 32969,
        "sha256": "d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b",
        "git_blob_sha": "e420aa38eafafb23054c2b8da10b6c0b48545244"
      },
      "patches": [
        {
          "before": "read_fixed_fejer_stage_point_observed_so3_report.py",
          "after": "read_fixed_fejer_meridian_batched_so3_report.py",
          "count": 1
        },
        {
          "before": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "after": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52",
          "count": 1
        },
        {
          "before": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
          "after": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
          "count": 1
        },
        {
          "before": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "after": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_point_root_packets.py",
          "after": "fixed_fejer_meridian_root_packets.py",
          "count": 1
        },
        {
          "before": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
          "after": "910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_point_normal_lift.py",
          "after": "fixed_fejer_detached_meridian_normal_lift.py",
          "count": 1
        },
        {
          "before": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
          "after": "388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_point_source_binding.py",
          "after": "fixed_fejer_meridian_source_binding.py",
          "count": 1
        },
        {
          "before": "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f",
          "after": "15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc",
          "count": 1
        },
        {
          "before": "complete-fixed-fejer-reference-centred-immutable-point-closure-values-analytic-frame-J3-normal-layer-v1",
          "after": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
          "count": 1
        },
        {
          "before": "ACTUAL_SOURCE_ROLE_COUNT = 120",
          "after": "ACTUAL_SOURCE_ROLE_COUNT = 137",
          "count": 1
        },
        {
          "before": "fixed-fejer-stage-observed",
          "after": "fixed-fejer-meridian-batched",
          "count": 1
        }
      ]
    },
    {
      "role": "radial",
      "parent": {
        "role": "radial",
        "name": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
        "bytes": 45332,
        "sha256": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
        "git_blob_sha": "f969ad127bcbc0c43681c3e17e6cf63b0b6ab19f"
      },
      "output": {
        "role": "radial",
        "name": "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py",
        "bytes": 45334,
        "sha256": "a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb",
        "git_blob_sha": "f22c1c35b07e771b5ba426729d52e5b6438870dc"
      },
      "patches": [
        {
          "before": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "after": "d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b",
          "count": 1
        },
        {
          "before": "fixed-fejer-stage-observed",
          "after": "fixed-fejer-meridian-batched",
          "count": 1
        }
      ]
    },
    {
      "role": "normal",
      "parent": {
        "role": "normal",
        "name": "fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
        "bytes": 40369,
        "sha256": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
        "git_blob_sha": "eed89ba9e5b606fb3ce27ffc54526db2a45fec1b"
      },
      "output": {
        "role": "normal",
        "name": "fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py",
        "bytes": 40379,
        "sha256": "242fc2f403db2495ea70e27437823031a84b26da717190b5f7e7ea252f9c0e2e",
        "git_blob_sha": "0b7aee57e28a8d234e6be778170631907a3d13fa"
      },
      "patches": [
        {
          "before": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "after": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52",
          "count": 1
        },
        {
          "before": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "after": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
          "count": 1
        },
        {
          "before": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "after": "d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "after": "a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb",
          "count": 1
        },
        {
          "before": "fixed-fejer-stage-observed",
          "after": "fixed-fejer-meridian-batched",
          "count": 3
        }
      ]
    },
    {
      "role": "leaf",
      "parent": {
        "role": "leaf",
        "name": "fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
        "bytes": 47482,
        "sha256": "280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652",
        "git_blob_sha": "2884e1741f96a8e80b349fe023ef398b1a7ecd87"
      },
      "output": {
        "role": "leaf",
        "name": "fixed_fejer_meridian_batched_complete_physical_leaf_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_complete_physical_leaf_binding.py",
        "bytes": 47494,
        "sha256": "897fceaa340fd042db03b3ea0f9b72b3e2c1a5c235d7104ead2c4b0104c07fc6",
        "git_blob_sha": "8cd02f6d317139cfbc024d957bc29e296fc69c16"
      },
      "patches": [
        {
          "before": "read_fixed_fejer_stage_point_observed_so3_report.py",
          "after": "read_fixed_fejer_meridian_batched_so3_report.py",
          "count": 1
        },
        {
          "before": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "after": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52",
          "count": 2
        },
        {
          "before": "fullclosed_fixed_fejer_stage_point_observed_so3_qp.py",
          "after": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
          "count": 1
        },
        {
          "before": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "after": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
          "count": 2
        },
        {
          "before": "fixed_fejer_stage_point_root_packets.py",
          "after": "fixed_fejer_meridian_root_packets.py",
          "count": 1
        },
        {
          "before": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
          "after": "910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_point_normal_lift.py",
          "after": "fixed_fejer_detached_meridian_normal_lift.py",
          "count": 1
        },
        {
          "before": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
          "after": "388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4",
          "count": 2
        },
        {
          "before": "fixed_fejer_stage_point_source_binding.py",
          "after": "fixed_fejer_meridian_source_binding.py",
          "count": 1
        },
        {
          "before": "9171871fcaaa1d2e65de1c40071cf8bb1acac0d7b0cc1d1da5b9cb36f690076f",
          "after": "15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
          "count": 2
        },
        {
          "before": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
          "after": "d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b",
          "count": 2
        },
        {
          "before": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "after": "a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
          "after": "fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py",
          "count": 1
        },
        {
          "before": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
          "after": "242fc2f403db2495ea70e27437823031a84b26da717190b5f7e7ea252f9c0e2e",
          "count": 1
        },
        {
          "before": "fixed-fejer-stage-observed",
          "after": "fixed-fejer-meridian-batched",
          "count": 6
        }
      ]
    },
    {
      "role": "geometry",
      "parent": {
        "role": "geometry",
        "name": "fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
        "bytes": 46719,
        "sha256": "3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560",
        "git_blob_sha": "4837232aa3a2a14a6ab36c2f1cb98aaf05ed25cd"
      },
      "output": {
        "role": "geometry",
        "name": "fixed_fejer_meridian_batched_continuous_gram_curvature_support.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_continuous_gram_curvature_support.py",
        "bytes": 46723,
        "sha256": "d0d0f45332ece0a63192b4e80c7c318635ba1068208bad45bec2a136781934a5",
        "git_blob_sha": "0d5b050a0f7f909f42843ebad4a3f46942dc9069"
      },
      "patches": [
        {
          "before": "fixed_fejer_stage_observed_complete_physical_leaf_binding.py",
          "after": "fixed_fejer_meridian_batched_complete_physical_leaf_binding.py",
          "count": 1
        },
        {
          "before": "280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652",
          "after": "897fceaa340fd042db03b3ea0f9b72b3e2c1a5c235d7104ead2c4b0104c07fc6",
          "count": 1
        },
        {
          "before": "fixed-fejer-stage-observed",
          "after": "fixed-fejer-meridian-batched",
          "count": 1
        }
      ]
    },
    {
      "role": "bridge",
      "parent": {
        "role": "bridge",
        "name": "fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py",
        "bytes": 20870,
        "sha256": "35493133665555aecf40eb85d213d53fb2b4fbf4acf949b403c258cbb24787a0",
        "git_blob_sha": "b8975cf1054fcd5dde9525e3e2375e7e9e3e640b"
      },
      "output": {
        "role": "bridge",
        "name": "fixed_fejer_meridian_batched_complete_geometry_support_beta_bridge.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_complete_geometry_support_beta_bridge.py",
        "bytes": 20878,
        "sha256": "d0b72820b7a7f8f872d2cb460e6f2fba3a685804e200ac4f35f7f12bf33cb0e7",
        "git_blob_sha": "9a0a9e1afb5d3e10548a25934117f5dc335687ef"
      },
      "patches": [
        {
          "before": "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py",
          "after": "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py",
          "after": "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py",
          "count": 1
        },
        {
          "before": "fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
          "after": "fixed_fejer_meridian_batched_continuous_gram_curvature_support.py",
          "count": 1
        },
        {
          "before": "3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560",
          "after": "d0d0f45332ece0a63192b4e80c7c318635ba1068208bad45bec2a136781934a5",
          "count": 1
        },
        {
          "before": "fixed-fejer-stage-observed",
          "after": "fixed-fejer-meridian-batched",
          "count": 1
        }
      ]
    }
  ],
  "parameter_derivations": [
    {
      "role": "normal_ready",
      "parent": {
        "role": "normal_ready",
        "name": "fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
        "bytes": 10975,
        "sha256": "dc5e88a28167b2a06f0821448c07abbae6cc6ff91d3d5bac8547d03398296d2b",
        "git_blob_sha": "46c3ba9503e7b8e42a93bb6cf7ba5b18566de603"
      },
      "output": {
        "role": "normal_ready",
        "name": "fixed-fejer-meridian-batched-complete-normal32-full-circle-sixjet-fees-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-complete-normal32-full-circle-sixjet-fees-ready.json",
        "bytes": 16723,
        "sha256": "029a12e9a1c0ba2c0bac068caf94743e8cb3521cfb3f31ba21db7ad4c3d7400a",
        "git_blob_sha": "ff6ebfbcb68d5140e44bd54ad163d5b17ab22fe9"
      },
      "patches": [
        {
          "path": [
            "schema"
          ],
          "before_present": true,
          "before": "complete-fixed-fejer-stage-observed-normal-32-stage-and-full-angle-sixjet-fees-ready-v1",
          "after": "complete-fixed-fejer-meridian-batched-normal-32-stage-and-full-angle-sixjet-fees-ready-v1"
        },
        {
          "path": [
            "complete_source_sha256"
          ],
          "before_present": true,
          "before": {
            "fixed_fejer_stage_observed_normal_packet_accurate_field_input.py": "720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3",
            "fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
            "fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
            "accurate_normal_rotation_and_stage_boxes.py": "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b"
          },
          "after": {
            "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py": "d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b",
            "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py": "a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb",
            "fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py": "242fc2f403db2495ea70e27437823031a84b26da717190b5f7e7ea252f9c0e2e",
            "accurate_normal_rotation_and_stage_boxes.py": "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b"
          }
        },
        {
          "path": [
            "source_report_expected_path"
          ],
          "before_present": true,
          "before": "{work}/fixed-fejer-stage-point-observed-independent/report.json",
          "after": "{work}/fixed-fejer-meridian-batched-first/report.json"
        },
        {
          "path": [
            "steps"
          ],
          "before_present": true,
          "before": [
            {
              "id": "actual-fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-first-20261127",
              "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_normal_root_and_sixjet_fees.py",
              "parent_bundle": "fixed-fejer-reference/reference.npz",
              "scope": "Complete accurate fee execution for the predeclared fixed Fejer target, pending a genuine complete immutable 8dc9d876/c9ce27c7 solver report snapshot. Re-read the whole 120-role current source closure, complete actual fixed-input binding, all six actual inputs, full point/model/target and all recorded immutable angular packets. Retain every actual cached/required literal angle and all 32 common normal stages; additionally enclose every one of 1024 closed full-circle cells phi/pi in [0,2]. Independently compute the accurate R709 mean/profile whole-angle boxes, all original exact affine radial pieces and the true exponential/control/frame chains. Use an original stage_XXX_J only as an arbitrary rational preconditioner proposal, preserving its actual order and complete words. Prove local stage root/first/second angular enclosures with every upstream dependency, then emit same-target a_deep/b/c/bs/cs/rho0 whole boxes and all physical sixjets including h/hp/hpp raw-defect terms. Glue only by directed inclusion into a uniqueness domain, including periodic and original-literal association. No working F/J/root replay. A natural 900-second partial return retains complete prefixes and is neither nonexistence nor a complete cover. Lower/cap C2, orientation, embedding, physical phases, mixed-pair reach, working-sixjet-word and external-parameter fees remain separate. No future report, point, snapshot or fee value is prefilled. The exact 120-role stage-point/math-progress entry is bound in full. The actual_mathematical_observation object is not used as a physical field, immutable snapshot or error certificate.",
              "args": [
                "--repo",
                "{repo}",
                "--report",
                "{work}/fixed-fejer-stage-point-observed-independent/report.json",
                "--outdir",
                "{work}/fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1",
                "--seconds",
                "900",
                "--maximum-leaf-evaluations",
                "1000000",
                "--precision-bits",
                "192",
                "--panels",
                "128",
                "--rho-leaf-budget",
                "8192",
                "--inverse-steps",
                "64",
                "--inverse-width",
                "1/1000000000000000000000000",
                "--full-angle-cells",
                "1024",
                "--radial-depth",
                "0",
                "--mean-maximum-splits",
                "8192",
                "--mean-width-goal",
                "1/1000000000",
                "--first-exp-degree",
                "24",
                "--maximum-exp-degree",
                "128",
                "--root-radius",
                "1/100000000",
                "--root-radius",
                "1/1000000",
                "--root-radius",
                "1/10000"
              ],
              "outputs": [
                "fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1/report.json"
              ],
              "summary": {
                "fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1/report.json": {
                  "schema": "schema",
                  "source": "source_sha256",
                  "source_commit": "source_commit",
                  "run": "github_run_id",
                  "run_attempt": "github_run_attempt",
                  "actual_report": "actual_report.sha256",
                  "actual_full_point": "actual_current_full_point_sha256",
                  "actual_snapshot": "actual_snapshot_identity_sha256",
                  "actual_driver": "actual_scientific_driver_sha256",
                  "actual_reader": "actual_pure_reader_sha256",
                  "input_request": "complete_input_and_request_identity_sha256",
                  "complete_execution_binding": "complete_binding_identity_sha256",
                  "geometry_setup": "accurate_geometry_setup_complete",
                  "complete_all_requested": "complete",
                  "all_stages_and_streams": "all_planned_original_stages_and_sixjet_streams_complete",
                  "final_byte_recheck": "all_bound_input_and_output_bytes_rechecked_at_final_report",
                  "all_recorded_angles": "all_original_recorded_angle_count",
                  "all_required_angles": "all_original_required_angle_count",
                  "requested_full_circle_cells": "requested_full_circle_cell_count",
                  "planned_jobs": "planned_job_count",
                  "completed_jobs": "completed_job_count",
                  "whole_continuous_branch": "full_same_field_angle_branch.complete_continuous_angle_branch_certified",
                  "actual_leaf_evaluations": "actual_work_budget.actual_leaf_evaluations",
                  "maximum_leaf_evaluations": "actual_work_budget.maximum_leaf_evaluations",
                  "actual_budget_exhausted": "actual_work_budget.exhausted",
                  "elapsed_hex": "elapsed_seconds_binary64_hex",
                  "working_root_field_calls": "existing_working_root_and_field_calls",
                  "working_J_JT_calls": "existing_working_J_or_Jtranspose_calls",
                  "actual_words_not_fabricated": "comparison_candidates_were_existing_complete_actual_packet_words",
                  "actual_second_order_not_invented": "working_second_order_words_not_invented",
                  "working_physical_word_errors_paid": "complete_original_working_physical_sixjet_word_errors_paid",
                  "sixjet_scope": "physical_sixjet_output_scope",
                  "closed_geometry_certified": "complete_reflected_closed_surface_C2_or_reach_certificate",
                  "external_parameter_fees_paid": "external_parameter_J_and_transpose_error_certificate",
                  "historical_obligations_removed": "unknown_historical_material_role_obligations_removed",
                  "problem_completed": "mathematical_problem_completion_claimed"
                }
              }
            }
          ],
          "after": [
            {
              "id": "actual-fixed-fejer-meridian-batched-complete-normal32-full-circle-sixjet-fees-first-20261127",
              "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py",
              "parent_bundle": "fixed-fejer-reference/reference.npz",
              "scope": "Complete accurate fee execution for the genuine meridian-cache/batched-missing-angle fixed Fejer field report, with the exact 41b4d09d/d3f1b33c source family and all 137 source roles. Re-read the whole actual fixed-input binding, every six-file input, complete point/model/target, all immutable cached-angle packets and all 32 recorded normal stages. The actual seed definition is consumed in full; the intended science uses boundary total length 1/4 and profile delta 1/32, with no inherited mean/root/field certificate. Additionally enclose all 1024 closed full-circle cells phi/pi in [0,2], every exact affine radial piece, the complete infinite scalar tail and the full original reference/profile/Exp/control/frame formulas. Existing stage_XXX_J words are only arbitrary rational preconditioner proposals. Pay complete local root and first/second angular enclosures with every upstream dependency and every physical sixjet including h/hp/hpp raw-defect terms. Directed adjacent, periodic and literal root-branch association is independently retained. No working F/J/root or new normal constructor is called. Cache hits, batch completion, timings, live scalar observations and last-trial files are not accuracy evidence. Natural partial budget returns retain their actual complete prefixes and are neither nonexistence nor a whole-domain certificate. Full closed C2/orientation/physical phases/mixed-pair reach, working-word and external-parameter fees remain separate. No future report/point/snapshot/fee identity or numerical success is prefilled.",
              "args": [
                "--repo",
                "{repo}",
                "--report",
                "{work}/fixed-fejer-meridian-batched-first/report.json",
                "--outdir",
                "{work}/fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1",
                "--seconds",
                "900",
                "--maximum-leaf-evaluations",
                "1000000",
                "--precision-bits",
                "192",
                "--panels",
                "128",
                "--rho-leaf-budget",
                "8192",
                "--inverse-steps",
                "64",
                "--inverse-width",
                "1/1000000000000000000000000",
                "--full-angle-cells",
                "1024",
                "--radial-depth",
                "0",
                "--mean-maximum-splits",
                "8192",
                "--mean-width-goal",
                "1/1000000000",
                "--first-exp-degree",
                "24",
                "--maximum-exp-degree",
                "128",
                "--root-radius",
                "1/100000000",
                "--root-radius",
                "1/1000000",
                "--root-radius",
                "1/10000"
              ],
              "outputs": [
                "fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1/report.json"
              ],
              "summary": {
                "fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1/report.json": {
                  "schema": "schema",
                  "source": "source_sha256",
                  "source_commit": "source_commit",
                  "run": "github_run_id",
                  "run_attempt": "github_run_attempt",
                  "actual_report": "actual_report.sha256",
                  "actual_full_point": "actual_current_full_point_sha256",
                  "actual_snapshot": "actual_snapshot_identity_sha256",
                  "actual_driver": "actual_scientific_driver_sha256",
                  "actual_reader": "actual_pure_reader_sha256",
                  "input_request": "complete_input_and_request_identity_sha256",
                  "complete_execution_binding": "complete_binding_identity_sha256",
                  "geometry_setup": "accurate_geometry_setup_complete",
                  "complete_all_requested": "complete",
                  "all_stages_and_streams": "all_planned_original_stages_and_sixjet_streams_complete",
                  "final_byte_recheck": "all_bound_input_and_output_bytes_rechecked_at_final_report",
                  "all_recorded_angles": "all_original_recorded_angle_count",
                  "all_required_angles": "all_original_required_angle_count",
                  "requested_full_circle_cells": "requested_full_circle_cell_count",
                  "planned_jobs": "planned_job_count",
                  "completed_jobs": "completed_job_count",
                  "whole_continuous_branch": "full_same_field_angle_branch.complete_continuous_angle_branch_certified",
                  "actual_leaf_evaluations": "actual_work_budget.actual_leaf_evaluations",
                  "maximum_leaf_evaluations": "actual_work_budget.maximum_leaf_evaluations",
                  "actual_budget_exhausted": "actual_work_budget.exhausted",
                  "elapsed_hex": "elapsed_seconds_binary64_hex",
                  "working_root_field_calls": "existing_working_root_and_field_calls",
                  "working_J_JT_calls": "existing_working_J_or_Jtranspose_calls",
                  "actual_words_not_fabricated": "comparison_candidates_were_existing_complete_actual_packet_words",
                  "actual_second_order_not_invented": "working_second_order_words_not_invented",
                  "working_physical_word_errors_paid": "complete_original_working_physical_sixjet_word_errors_paid",
                  "sixjet_scope": "physical_sixjet_output_scope",
                  "closed_geometry_certified": "complete_reflected_closed_surface_C2_or_reach_certificate",
                  "external_parameter_fees_paid": "external_parameter_J_and_transpose_error_certificate",
                  "historical_obligations_removed": "unknown_historical_material_role_obligations_removed",
                  "problem_completed": "mathematical_problem_completion_claimed"
                }
              }
            }
          ]
        },
        {
          "path": [
            "actual_scientific_source_sha256"
          ],
          "before_present": true,
          "before": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "after": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2"
        },
        {
          "path": [
            "actual_complete_reader_sha256"
          ],
          "before_present": true,
          "before": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "after": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52"
        },
        {
          "path": [
            "complete_scientific_runtime_source_role_count"
          ],
          "before_present": true,
          "before": 120,
          "after": 137
        },
        {
          "path": [
            "current_normal_source_sha256"
          ],
          "before_present": true,
          "before": "42b205ee34af4233002cec3d782acd78ed72a38f6013c1b931b3892f55d73e10",
          "after": "388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4"
        },
        {
          "path": [
            "current_immutable_packet_source_sha256"
          ],
          "before_present": true,
          "before": "140f639656c2a30c59f0ba4c8153e3467d5abddf8189a84fcc38fb6638ee8aaf",
          "after": "910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15"
        },
        {
          "path": [
            "complete_current_source_family"
          ],
          "before_present": true,
          "before": {
            "bytes": 41188,
            "sha256": "1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544",
            "git_blob_sha": "da1192313958df70ba3b95d5e302b34fe4a2cfc2",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-complete-delivery.json"
          },
          "after": {
            "definition": "The complete new scientific driver SOURCE_PINS and the exact new pure reader; no numerical return is inferred",
            "driver": {
              "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
              "bytes": 99313,
              "sha256": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
              "git_blob_sha": "df1023d71441a01e0dd1e343cb1431aa7553023e"
            },
            "reader": {
              "name": "read_fixed_fejer_meridian_batched_so3_report.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py",
              "bytes": 99382,
              "sha256": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52",
              "git_blob_sha": "66c92a656aff5df0013b9c7bf69c08e71aab87c3"
            },
            "normal": {
              "name": "fixed_fejer_detached_meridian_normal_lift.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
              "bytes": 96276,
              "sha256": "388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4",
              "git_blob_sha": "8a22b31dcc36d3160d4c968f9645600961a22abc"
            },
            "packets": {
              "name": "fixed_fejer_meridian_root_packets.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py",
              "bytes": 73723,
              "sha256": "910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15",
              "git_blob_sha": "e347b156b0b4bec87871fc07809a40a3bbda4ddd"
            },
            "detached_meridian_values": {
              "name": "fixed_fejer_detached_meridian_values.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
              "bytes": 41030,
              "sha256": "7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd",
              "git_blob_sha": "6ab29473b0d549539de69a064efb19af4227a867"
            },
            "field_binding": {
              "name": "fixed_fejer_meridian_source_binding.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_source_binding.py",
              "bytes": 41894,
              "sha256": "15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc",
              "git_blob_sha": "54d58893654598e94687a448e2beccc776e1cfb4"
            },
            "geometry": {
              "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
              "bytes": 88163,
              "sha256": "51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898",
              "git_blob_sha": "e66b17a5384ec29e11415d4eb6a6549594277436"
            },
            "lower_source_locks": {
              "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-detached-meridian-value-lower-source-locks.json",
              "bytes": 18987,
              "sha256": "969a1e676eab85c7497072d6a92f34dc037230da7aebf6227b0f343eded6aba3",
              "git_blob_sha": "4903cf3479cd6be661ec1b2734d8a52be0b4b308"
            },
            "complete_source_role_count": 137,
            "original_120_source_identities_remain_as_actual_parent_roles": true
          }
        },
        {
          "path": [
            "intended_actual_run_id"
          ],
          "before_present": true,
          "before": "46037017666",
          "after": null
        },
        {
          "path": [
            "intended_actual_run_attempt"
          ],
          "before_present": true,
          "before": 1,
          "after": null
        },
        {
          "path": [
            "complete_parent_scientific_source_family"
          ],
          "before_present": false,
          "after": {
            "bytes": 41188,
            "sha256": "1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544",
            "git_blob_sha": "da1192313958df70ba3b95d5e302b34fe4a2cfc2",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-complete-delivery.json"
          }
        },
        {
          "path": [
            "parameter_parent_run_provenance"
          ],
          "before_present": false,
          "after": {
            "run_id": "46037017666",
            "run_attempt": 1,
            "role": "historical parameter-source attribution only",
            "current_run_or_current_inputs_claimed": false
          }
        },
        {
          "path": [
            "complete_parameter_parent_file"
          ],
          "before_present": false,
          "after": {
            "role": "normal_ready",
            "name": "fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-normal32-full-circle-sixjet-fees-ready.json",
            "bytes": 10975,
            "sha256": "dc5e88a28167b2a06f0821448c07abbae6cc6ff91d3d5bac8547d03398296d2b",
            "git_blob_sha": "46c3ba9503e7b8e42a93bb6cf7ba5b18566de603"
          }
        },
        {
          "path": [
            "complete_fee_parent_delivery"
          ],
          "before_present": false,
          "after": {
            "bytes": 23822,
            "sha256": "6990d534425ba2db3116fa77f42f0ade241414502c619a86fbcf42d044f09067",
            "git_blob_sha": "6c7df82353fd9bb6b92af6ace319e17342b06d94",
            "name": "fixed-fejer-stage-observed-complete-accurate-fees-delivery.json",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-accurate-fees-delivery.json"
          }
        },
        {
          "path": [
            "planned_current_supported_seed_parameters"
          ],
          "before_present": false,
          "after": {
            "relative_boundary_total_length": "1/4",
            "profile_delta": "1/32",
            "fixed_mathematical_metric_changed": false,
            "full_actual_seed_definition_reread": true,
            "initial_field_or_seed_model_identity_inherited": false,
            "reference_mean_R709_conditions_must_be_computed_on_each_whole_angle_box": true
          }
        },
        {
          "path": [
            "new_working_constructor_called_by_fee"
          ],
          "before_present": false,
          "after": false
        },
        {
          "path": [
            "current_scientific_constructor_keyword"
          ],
          "before_present": false,
          "after": "meridian_value_module"
        },
        {
          "path": [
            "current_scientific_constructor_source"
          ],
          "before_present": false,
          "after": {
            "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
            "bytes": 99313,
            "sha256": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
            "git_blob_sha": "df1023d71441a01e0dd1e343cb1431aa7553023e"
          }
        },
        {
          "path": [
            "detached_meridian_cache_and_missing_angle_batch_do_not_pay_fees"
          ],
          "before_present": false,
          "after": true
        },
        {
          "path": [
            "full_operator_cache_metadata_validated_at_its_own_point"
          ],
          "before_present": false,
          "after": true
        },
        {
          "path": [
            "cache_diagnostics_backfilled_into_root_snapshots"
          ],
          "before_present": false,
          "after": false
        },
        {
          "path": [
            "future_actual_normal_model_identity_sha256"
          ],
          "before_present": false,
          "after": null
        },
        {
          "path": [
            "future_complete_field_report_sha256"
          ],
          "before_present": false,
          "after": null
        },
        {
          "path": [
            "future_exact_geometry_or_root_value"
          ],
          "before_present": false,
          "after": null
        },
        {
          "path": [
            "active_J_or_working_word_error_certificate_produced"
          ],
          "before_present": false,
          "after": false
        },
        {
          "path": [
            "original_complete_normal_and_geometry_budgets_unchanged"
          ],
          "before_present": false,
          "after": true
        },
        {
          "path": [
            "no_optional_preflight_or_reproducer_step_added"
          ],
          "before_present": false,
          "after": true
        }
      ],
      "comparison": {
        "argv_count": 38,
        "summary_selector_count": 36,
        "all_numerical_arguments_original": true,
        "summary_selector_mapping_original": true,
        "output_count": 1,
        "seconds": "900",
        "complete_original_step_retained_except_declared_source_paths_and_scope": true
      }
    },
    {
      "role": "geometry_ready",
      "parent": {
        "role": "geometry_ready",
        "name": "fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
        "bytes": 11490,
        "sha256": "049776de848bb0563d1a0ee6438201d2529b470375adb23dd9eb651ebfe751d6",
        "git_blob_sha": "177b4ca2c3566e84cfacbf0bcdfd10f50b0aa909"
      },
      "output": {
        "role": "geometry_ready",
        "name": "fixed-fejer-meridian-batched-complete-continuous-gram-curvature-support-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-meridian-batched-complete-continuous-gram-curvature-support-ready.json",
        "bytes": 17060,
        "sha256": "949acd57b29bf81944df85c8af5deacdd8ac0dd21774494b62b6f47a680975e5",
        "git_blob_sha": "65c7cbdcc93cc97d9f342828da592dae963d1b4c"
      },
      "patches": [
        {
          "path": [
            "schema"
          ],
          "before_present": true,
          "before": "complete-fixed-fejer-stage-observed-continuous-gram-curvature-support-ready-v1",
          "after": "complete-fixed-fejer-meridian-batched-continuous-gram-curvature-support-ready-v1"
        },
        {
          "path": [
            "complete_source_sha256"
          ],
          "before_present": true,
          "before": {
            "fixed_fejer_stage_observed_complete_physical_leaf_binding.py": "280bc1cf1d91bfd60b7d905045c07ccefd901833c9734e1b3c3496f5d4afd652",
            "fixed_fejer_stage_observed_continuous_gram_curvature_support.py": "3f383d692711d180d0f7fd24e78ce67973c85b8c231e28deb135122664dd3560",
            "fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py": "35493133665555aecf40eb85d213d53fb2b4fbf4acf949b403c258cbb24787a0"
          },
          "after": {
            "fixed_fejer_meridian_batched_complete_physical_leaf_binding.py": "897fceaa340fd042db03b3ea0f9b72b3e2c1a5c235d7104ead2c4b0104c07fc6",
            "fixed_fejer_meridian_batched_continuous_gram_curvature_support.py": "d0d0f45332ece0a63192b4e80c7c318635ba1068208bad45bec2a136781934a5",
            "fixed_fejer_meridian_batched_complete_geometry_support_beta_bridge.py": "d0b72820b7a7f8f872d2cb460e6f2fba3a685804e200ac4f35f7f12bf33cb0e7"
          }
        },
        {
          "path": [
            "source_normal_report_expected_path"
          ],
          "before_present": true,
          "before": "{work}/fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1/report.json",
          "after": "{work}/fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1/report.json"
        },
        {
          "path": [
            "fixed_actual_normal_fee_source_sha256"
          ],
          "before_present": true,
          "before": "24765a9049f38e6b68f1e1d457d514054557b17731ac390dade82605682d2673",
          "after": "242fc2f403db2495ea70e27437823031a84b26da717190b5f7e7ea252f9c0e2e"
        },
        {
          "path": [
            "fixed_actual_radial_source_sha256"
          ],
          "before_present": true,
          "before": "03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd",
          "after": "a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb"
        },
        {
          "path": [
            "steps"
          ],
          "before_present": true,
          "before": [
            {
              "id": "actual-fixed-fejer-stage-observed-whole-normal-leaf-continuous-gram-curvature-support-first-20261127",
              "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_continuous_gram_curvature_support.py",
              "parent_bundle": "fixed-fejer-reference/reference.npz",
              "scope": "Consume the genuine complete 24765a stage-observed fixed-Fejer normal-fee report and every original 32-stage/angular/root journal. Retain all literal associations, all full [0,2] phi/pi cells and every exact radial leaf including the complete tail. Re-read the immutable physical sixjet streams and same-target a_deep/rho0 boxes. Compute complete symmetric 2x2 relative-Gram operator bounds, full-second-form curvature bounds and candidate N=Fphi cross Fs support numerators. Add R717's complete same-leaf three-dimensional position norm, then take the minimum of its formal full-union diameter bound and the original coordinate-cylinder bound. This accounts for all points of the formal rotated/reflected/cap union but does not itself certify the actual closed physical family. No new working F/J/root or accurate integrand evaluation. Incomplete jobs, missing positivity, exhausted budgets and unproved branch glue remain explicit; no missing domain is filled with zero. Only complete global upper-cover numbers are promoted. Lower reflection, closed C2/outward assembly, actual physical phases, all mixed-pair reach and the beta consumer's eight full evidence roles remain separate. Original solver parameters, stages, variables and unknown historical obligations are unchanged. This is the exact stage-point/math-progress source family; mutable scalar observations do not replace the complete root/physical-stream provenance.",
              "args": [
                "--repo",
                "{repo}",
                "--normal-report",
                "{work}/fixed-fejer-stage-observed-normal-root-and-sixjet-fees-v1/report.json",
                "--outdir",
                "{work}/fixed-fejer-stage-observed-continuous-gram-curvature-support-v1",
                "--seconds",
                "900"
              ],
              "outputs": [
                "fixed-fejer-stage-observed-continuous-gram-curvature-support-v1/report.json"
              ],
              "summary": {
                "fixed-fejer-stage-observed-continuous-gram-curvature-support-v1/report.json": {
                  "schema": "schema",
                  "source": "source_sha256",
                  "source_commit": "source_commit",
                  "run": "github_run_id",
                  "attempt": "github_run_attempt",
                  "normal_report": "normal_report.sha256",
                  "geometry_binding": "complete_binding_identity_sha256",
                  "actual_point": "actual_current_full_point_sha256",
                  "model": "complete_original_model_identity_sha256",
                  "snapshot": "actual_snapshot_identity_sha256",
                  "target": "exact_fixed_target_identity_sha256",
                  "scalar": "fixed_scalar_metric_identity_sha256",
                  "setup": "geometry_setup_available",
                  "complete_upper": "complete",
                  "whole_angle_jobs": "expected_whole_angle_jobs",
                  "upstream_whole_jobs": "upstream_complete_whole_angle_jobs",
                  "processed_whole_jobs": "processed_complete_whole_angle_jobs",
                  "exact_radial_leaves": "expected_radial_leaves_per_angle",
                  "expected_all_leaves": "expected_complete_geometry_leaves",
                  "processed_leaves": "processed_geometry_leaves",
                  "complete_cover": "full_upper_cover_processed",
                  "continuous_Gram_complete": "continuous_Gram_bound_complete",
                  "continuous_K_complete": "continuous_curvature_bound_complete",
                  "continuous_support_complete": "continuous_support_numerator_bounds_complete",
                  "positive_upper_immersion_boxes": "complete_upper_immersion_lower_from_boxes",
                  "original_branch": "original_complete_angle_branch.complete",
                  "final_all_bytes": "all_input_and_output_bytes_rechecked",
                  "Gram_operator_upper": "accurate_global_bounds.relative_Gram_error_operator_norm_upper",
                  "curvature_upper": "accurate_global_bounds.principal_curvature_absolute_upper",
                  "normal_norm_lower": "accurate_global_bounds.normal_norm_lower",
                  "upper_only_D": "accurate_global_bounds.upper_base_phase_diameter_upper",
                  "formal_reflected_rotated_D": "accurate_global_bounds.formal_reflection_fixed_caps_all_rotation_set_diameter_upper",
                  "formal_D_actual_phase_proved": "accurate_global_bounds.formal_diameter_is_actual_phase_family_certificate",
                  "full_closed_D": "accurate_global_bounds.full_marked_surface_diameter_upper",
                  "full_closed_reach": "accurate_global_bounds.complete_closed_surface_reach_lower",
                  "Gram_unavailable": "partial_processed_statistics.relative_Gram_unavailable_leaf_count",
                  "K_unavailable": "partial_processed_statistics.curvature_unavailable_leaf_count",
                  "normal_positive_unproved": "partial_processed_statistics.normal_positive_unproved_leaf_count",
                  "lower_horizontal_support": "partial_processed_statistics.minima_over_processed_leaves.horizontal_support_numerator_lower.value",
                  "lower_vertical_support": "partial_processed_statistics.minima_over_processed_leaves.vertical_support_numerator_lower.value",
                  "new_working_F_J_root": "new_working_field_J_or_root_calls",
                  "new_accurate_root_integrands": "new_accurate_root_or_integrand_calls",
                  "closed_geometry": "complete_closed_geometry_certified",
                  "elapsed_hex": "elapsed_seconds_binary64_hex",
                  "same_leaf_norm_upper": "accurate_global_bounds.formal_diameter_definition.same_leaf_position_norm_upper",
                  "fixed_cap_norm_upper": "accurate_global_bounds.formal_diameter_definition.cap_position_norm_upper",
                  "norm_diameter_upper": "accurate_global_bounds.formal_diameter_definition.same_leaf_norm_diameter_upper",
                  "coordinate_cylinder_D_upper": "accurate_global_bounds.formal_diameter_definition.separate_coordinate_cylinder_diameter_upper"
                }
              }
            }
          ],
          "after": [
            {
              "id": "actual-fixed-fejer-meridian-batched-whole-normal-leaf-continuous-gram-curvature-support-first-20261127",
              "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_continuous_gram_curvature_support.py",
              "parent_bundle": "fixed-fejer-reference/reference.npz",
              "scope": "Consume only the actual complete meridian-batched normal-fee report and its full same-point source/target/immutable packet provenance. Re-read all original 32-stage journals, every literal association, directed periodic/full-circle branch checks, every exact radial leaf and the complete scalar tail. Compute complete symmetric relative-Gram operator bounds, full second-form curvature bounds and candidate Fphi cross Fs support from every returned accurate sixjet. Retain R717 same-leaf three-dimensional position-norm and coordinate-cylinder bounds for the complete formal rotation/reflection/two-cap union. The complete upper cover and formal union remain distinct from a proved closed physical phase family; all mixed-pair reach and the original eight beta evidence roles remain unpaid here. No working field/J/root and no new accurate integrand/root call. A cache/batch/progress/last-trial return never replaces the full physical stream. Keep all unprocessed, failed and unproved obligations explicit and only promote bounds after the complete input/output recheck. Original scientific sources and all numerical/domain budgets remain unchanged.",
              "args": [
                "--repo",
                "{repo}",
                "--normal-report",
                "{work}/fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1/report.json",
                "--outdir",
                "{work}/fixed-fejer-meridian-batched-continuous-gram-curvature-support-v1",
                "--seconds",
                "900"
              ],
              "outputs": [
                "fixed-fejer-meridian-batched-continuous-gram-curvature-support-v1/report.json"
              ],
              "summary": {
                "fixed-fejer-meridian-batched-continuous-gram-curvature-support-v1/report.json": {
                  "schema": "schema",
                  "source": "source_sha256",
                  "source_commit": "source_commit",
                  "run": "github_run_id",
                  "attempt": "github_run_attempt",
                  "normal_report": "normal_report.sha256",
                  "geometry_binding": "complete_binding_identity_sha256",
                  "actual_point": "actual_current_full_point_sha256",
                  "model": "complete_original_model_identity_sha256",
                  "snapshot": "actual_snapshot_identity_sha256",
                  "target": "exact_fixed_target_identity_sha256",
                  "scalar": "fixed_scalar_metric_identity_sha256",
                  "setup": "geometry_setup_available",
                  "complete_upper": "complete",
                  "whole_angle_jobs": "expected_whole_angle_jobs",
                  "upstream_whole_jobs": "upstream_complete_whole_angle_jobs",
                  "processed_whole_jobs": "processed_complete_whole_angle_jobs",
                  "exact_radial_leaves": "expected_radial_leaves_per_angle",
                  "expected_all_leaves": "expected_complete_geometry_leaves",
                  "processed_leaves": "processed_geometry_leaves",
                  "complete_cover": "full_upper_cover_processed",
                  "continuous_Gram_complete": "continuous_Gram_bound_complete",
                  "continuous_K_complete": "continuous_curvature_bound_complete",
                  "continuous_support_complete": "continuous_support_numerator_bounds_complete",
                  "positive_upper_immersion_boxes": "complete_upper_immersion_lower_from_boxes",
                  "original_branch": "original_complete_angle_branch.complete",
                  "final_all_bytes": "all_input_and_output_bytes_rechecked",
                  "Gram_operator_upper": "accurate_global_bounds.relative_Gram_error_operator_norm_upper",
                  "curvature_upper": "accurate_global_bounds.principal_curvature_absolute_upper",
                  "normal_norm_lower": "accurate_global_bounds.normal_norm_lower",
                  "upper_only_D": "accurate_global_bounds.upper_base_phase_diameter_upper",
                  "formal_reflected_rotated_D": "accurate_global_bounds.formal_reflection_fixed_caps_all_rotation_set_diameter_upper",
                  "formal_D_actual_phase_proved": "accurate_global_bounds.formal_diameter_is_actual_phase_family_certificate",
                  "full_closed_D": "accurate_global_bounds.full_marked_surface_diameter_upper",
                  "full_closed_reach": "accurate_global_bounds.complete_closed_surface_reach_lower",
                  "Gram_unavailable": "partial_processed_statistics.relative_Gram_unavailable_leaf_count",
                  "K_unavailable": "partial_processed_statistics.curvature_unavailable_leaf_count",
                  "normal_positive_unproved": "partial_processed_statistics.normal_positive_unproved_leaf_count",
                  "lower_horizontal_support": "partial_processed_statistics.minima_over_processed_leaves.horizontal_support_numerator_lower.value",
                  "lower_vertical_support": "partial_processed_statistics.minima_over_processed_leaves.vertical_support_numerator_lower.value",
                  "new_working_F_J_root": "new_working_field_J_or_root_calls",
                  "new_accurate_root_integrands": "new_accurate_root_or_integrand_calls",
                  "closed_geometry": "complete_closed_geometry_certified",
                  "elapsed_hex": "elapsed_seconds_binary64_hex",
                  "same_leaf_norm_upper": "accurate_global_bounds.formal_diameter_definition.same_leaf_position_norm_upper",
                  "fixed_cap_norm_upper": "accurate_global_bounds.formal_diameter_definition.cap_position_norm_upper",
                  "norm_diameter_upper": "accurate_global_bounds.formal_diameter_definition.same_leaf_norm_diameter_upper",
                  "coordinate_cylinder_D_upper": "accurate_global_bounds.formal_diameter_definition.separate_coordinate_cylinder_diameter_upper"
                }
              }
            }
          ]
        },
        {
          "path": [
            "optional_beta_bridge",
            "script"
          ],
          "before_present": true,
          "before": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_stage_observed_complete_geometry_support_beta_bridge.py",
          "after": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_batched_complete_geometry_support_beta_bridge.py"
        },
        {
          "path": [
            "actual_scientific_source_sha256"
          ],
          "before_present": true,
          "before": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
          "after": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2"
        },
        {
          "path": [
            "actual_complete_reader_sha256"
          ],
          "before_present": true,
          "before": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
          "after": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52"
        },
        {
          "path": [
            "complete_scientific_runtime_source_role_count"
          ],
          "before_present": true,
          "before": 120,
          "after": 137
        },
        {
          "path": [
            "complete_current_source_family"
          ],
          "before_present": true,
          "before": {
            "bytes": 41188,
            "sha256": "1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544",
            "git_blob_sha": "da1192313958df70ba3b95d5e302b34fe4a2cfc2",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-complete-delivery.json"
          },
          "after": {
            "definition": "The complete new scientific driver SOURCE_PINS and the exact new pure reader; no numerical return is inferred",
            "driver": {
              "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
              "bytes": 99313,
              "sha256": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
              "git_blob_sha": "df1023d71441a01e0dd1e343cb1431aa7553023e"
            },
            "reader": {
              "name": "read_fixed_fejer_meridian_batched_so3_report.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py",
              "bytes": 99382,
              "sha256": "d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52",
              "git_blob_sha": "66c92a656aff5df0013b9c7bf69c08e71aab87c3"
            },
            "normal": {
              "name": "fixed_fejer_detached_meridian_normal_lift.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
              "bytes": 96276,
              "sha256": "388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4",
              "git_blob_sha": "8a22b31dcc36d3160d4c968f9645600961a22abc"
            },
            "packets": {
              "name": "fixed_fejer_meridian_root_packets.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py",
              "bytes": 73723,
              "sha256": "910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15",
              "git_blob_sha": "e347b156b0b4bec87871fc07809a40a3bbda4ddd"
            },
            "detached_meridian_values": {
              "name": "fixed_fejer_detached_meridian_values.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
              "bytes": 41030,
              "sha256": "7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd",
              "git_blob_sha": "6ab29473b0d549539de69a064efb19af4227a867"
            },
            "field_binding": {
              "name": "fixed_fejer_meridian_source_binding.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_source_binding.py",
              "bytes": 41894,
              "sha256": "15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc",
              "git_blob_sha": "54d58893654598e94687a448e2beccc776e1cfb4"
            },
            "geometry": {
              "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
              "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
              "bytes": 88163,
              "sha256": "51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898",
              "git_blob_sha": "e66b17a5384ec29e11415d4eb6a6549594277436"
            },
            "lower_source_locks": {
              "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-detached-meridian-value-lower-source-locks.json",
              "bytes": 18987,
              "sha256": "969a1e676eab85c7497072d6a92f34dc037230da7aebf6227b0f343eded6aba3",
              "git_blob_sha": "4903cf3479cd6be661ec1b2734d8a52be0b4b308"
            },
            "complete_source_role_count": 137,
            "original_120_source_identities_remain_as_actual_parent_roles": true
          }
        },
        {
          "path": [
            "intended_actual_run_id"
          ],
          "before_present": true,
          "before": "46037017666",
          "after": null
        },
        {
          "path": [
            "intended_actual_run_attempt"
          ],
          "before_present": true,
          "before": 1,
          "after": null
        },
        {
          "path": [
            "complete_parent_scientific_source_family"
          ],
          "before_present": false,
          "after": {
            "bytes": 41188,
            "sha256": "1231359df08d58853b32b03c62ef841127eb9c3f571fc12603b7698c12410544",
            "git_blob_sha": "da1192313958df70ba3b95d5e302b34fe4a2cfc2",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-mathematical-progress-complete-delivery.json"
          }
        },
        {
          "path": [
            "parameter_parent_run_provenance"
          ],
          "before_present": false,
          "after": {
            "run_id": "46037017666",
            "run_attempt": 1,
            "role": "historical parameter-source attribution only",
            "current_run_or_current_inputs_claimed": false
          }
        },
        {
          "path": [
            "complete_parameter_parent_file"
          ],
          "before_present": false,
          "after": {
            "role": "geometry_ready",
            "name": "fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-continuous-gram-curvature-support-ready.json",
            "bytes": 11490,
            "sha256": "049776de848bb0563d1a0ee6438201d2529b470375adb23dd9eb651ebfe751d6",
            "git_blob_sha": "177b4ca2c3566e84cfacbf0bcdfd10f50b0aa909"
          }
        },
        {
          "path": [
            "complete_fee_parent_delivery"
          ],
          "before_present": false,
          "after": {
            "bytes": 23822,
            "sha256": "6990d534425ba2db3116fa77f42f0ade241414502c619a86fbcf42d044f09067",
            "git_blob_sha": "6c7df82353fd9bb6b92af6ace319e17342b06d94",
            "name": "fixed-fejer-stage-observed-complete-accurate-fees-delivery.json",
            "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-observed-complete-accurate-fees-delivery.json"
          }
        },
        {
          "path": [
            "planned_current_supported_seed_parameters"
          ],
          "before_present": false,
          "after": {
            "relative_boundary_total_length": "1/4",
            "profile_delta": "1/32",
            "fixed_mathematical_metric_changed": false,
            "full_actual_seed_definition_reread": true,
            "initial_field_or_seed_model_identity_inherited": false,
            "reference_mean_R709_conditions_must_be_computed_on_each_whole_angle_box": true
          }
        },
        {
          "path": [
            "new_working_constructor_called_by_fee"
          ],
          "before_present": false,
          "after": false
        },
        {
          "path": [
            "current_scientific_constructor_keyword"
          ],
          "before_present": false,
          "after": "meridian_value_module"
        },
        {
          "path": [
            "current_scientific_constructor_source"
          ],
          "before_present": false,
          "after": {
            "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
            "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
            "bytes": 99313,
            "sha256": "41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2",
            "git_blob_sha": "df1023d71441a01e0dd1e343cb1431aa7553023e"
          }
        },
        {
          "path": [
            "detached_meridian_cache_and_missing_angle_batch_do_not_pay_fees"
          ],
          "before_present": false,
          "after": true
        },
        {
          "path": [
            "full_operator_cache_metadata_validated_at_its_own_point"
          ],
          "before_present": false,
          "after": true
        },
        {
          "path": [
            "cache_diagnostics_backfilled_into_root_snapshots"
          ],
          "before_present": false,
          "after": false
        },
        {
          "path": [
            "future_actual_normal_model_identity_sha256"
          ],
          "before_present": false,
          "after": null
        },
        {
          "path": [
            "future_complete_field_report_sha256"
          ],
          "before_present": false,
          "after": null
        },
        {
          "path": [
            "future_exact_geometry_or_root_value"
          ],
          "before_present": false,
          "after": null
        },
        {
          "path": [
            "active_J_or_working_word_error_certificate_produced"
          ],
          "before_present": false,
          "after": false
        },
        {
          "path": [
            "original_complete_normal_and_geometry_budgets_unchanged"
          ],
          "before_present": false,
          "after": true
        },
        {
          "path": [
            "no_optional_preflight_or_reproducer_step_added"
          ],
          "before_present": false,
          "after": true
        }
      ],
      "comparison": {
        "argv_count": 8,
        "summary_selector_count": 48,
        "all_numerical_arguments_original": true,
        "summary_selector_mapping_original": true,
        "output_count": 1,
        "seconds": "900",
        "complete_original_step_retained_except_declared_source_paths_and_scope": true
      }
    }
  ],
  "scientific_execution_performed": false,
  "numerical_formula_or_budget_change": false,
  "scientific_admission_prerequisite": false
}
""")


def identity(raw):
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def read_parent(repo, record):
    path = (repo / record["path"]).resolve()
    if repo not in path.parents:
        raise ValueError("Keep each complete declared parent inside the repository")
    raw = path.read_bytes()
    if identity(raw) != {key: record[key] for key in ("bytes", "sha256")}:
        raise ValueError("The whole declared source or parameter parent differs: " + str(path))
    return path, raw


def replace_complete(text, patches, *, reverse=False):
    sequence = reversed(patches) if reverse else patches
    for patch in sequence:
        before, after = ((patch["after"], patch["before"]) if reverse
                         else (patch["before"], patch["after"]))
        if not before or text.count(before) != patch["count"]:
            raise ValueError("An exact source-reproduction replacement count changed")
        text = text.replace(before, after)
    return text


def equal_json(left, right):
    options = dict(sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return json.dumps(left, **options) == json.dumps(right, **options)


def apply_parameter_edits(value, edits, *, reverse=False):
    result = copy.deepcopy(value)
    for edit in (reversed(edits) if reverse else edits):
        path = edit["path"]
        if not path:
            raise ValueError("Retain explicit complete parameter field paths")
        parent = result
        for key in path[:-1]:
            parent = parent[key]
        key = path[-1]
        present = key in parent
        if reverse:
            if not present or not equal_json(parent[key], edit["after"]):
                raise ValueError("A complete parameter reverse value differs")
            if edit["before_present"]:
                parent[key] = copy.deepcopy(edit["before"])
            else:
                del parent[key]
        else:
            if present != edit["before_present"]:
                raise ValueError("A complete parameter field-presence condition changed")
            if present and not equal_json(parent[key], edit["before"]):
                raise ValueError("A complete original parameter value changed")
            parent[key] = copy.deepcopy(edit["after"])
    return result


def parameter_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def prepare(repo):
    outputs = []
    consumed = []
    for entry in CONSTRUCTION["source_derivations"]:
        path, original = read_parent(repo, entry["parent"])
        consumed.append(path)
        parent = original.decode("utf-8")
        current = replace_complete(parent, entry["patches"])
        if replace_complete(current, entry["patches"], reverse=True) != parent:
            raise ValueError("The complete source inverse did not restore its actual parent")
        raw = current.encode("utf-8")
        expected = entry["output"]
        if identity(raw) != {key: expected[key] for key in ("bytes", "sha256")}:
            raise ValueError("The entire regenerated source identity differs")
        if len(raw) >= 100000:
            raise ValueError("Keep every complete source below the declared file-size limit")
        outputs.append((expected, raw))
    for entry in CONSTRUCTION["parameter_derivations"]:
        path, original = read_parent(repo, entry["parent"])
        consumed.append(path)
        parent = json.loads(original)
        current = apply_parameter_edits(parent, entry["patches"])
        restored = apply_parameter_edits(current, entry["patches"], reverse=True)
        if not equal_json(restored, parent) or parameter_bytes(restored) != original:
            raise ValueError("The full parameter inverse did not restore every original byte")
        raw = parameter_bytes(current)
        expected = entry["output"]
        if identity(raw) != {key: expected[key] for key in ("bytes", "sha256")}:
            raise ValueError("The complete regenerated parameter-file identity differs")
        if len(raw) >= 100000:
            raise ValueError("Keep each full parameter artifact below the declared file-size limit")
        outputs.append((expected, raw))
    names = [record["name"] for record, _ in outputs]
    if len(names) != len(set(names)):
        raise ValueError("Keep distinct complete output basenames")
    return outputs, consumed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    out = args.output_directory.resolve()
    outputs, consumed = prepare(repo)
    for source in consumed:
        if out == source or out in source.parents:
            raise ValueError("The output directory may not contain or overwrite a consumed parent")
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for record, raw in outputs:
        path = out / record["name"]
        if path.exists():
            if path.read_bytes() != raw:
                raise ValueError("An existing complete output has different bytes: " + str(path))
        else:
            with path.open("xb") as stream:
                stream.write(raw)
        if identity(path.read_bytes()) != {key: record[key] for key in ("bytes", "sha256")}:
            raise ValueError("An output changed while writing its complete bytes")
        written.append(dict(path=str(path), **identity(raw)))
    print(json.dumps(dict(schema=CONSTRUCTION["schema"],
        source_only=True, scientific_import_or_execution=False,
        original_sources_modified=False, source_or_parameter_output_count=len(written),
        outputs=written), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
