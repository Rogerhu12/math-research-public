#!/usr/bin/env python3
"""Reproduce the seven complete paired-halfwave upper source files as text.

This constructor reads whole fixed parent source files, applies every recorded
literal replacement, and writes the whole declared new source. It never imports,
compiles, parses with Python AST, or executes scientific code. It is not a
scientific admission step and does not run a field, root, QP, or fixture.
The original sources remain at their original paths.
"""
import argparse
import hashlib
import json
from pathlib import Path

SPECS = json.loads(r'''[
  {
    "role": "endpoint",
    "parent": {
      "name": "fixed_fejer_detached_meridian_normal_lift.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
      "bytes": 96276,
      "sha256": "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d",
      "git_blob_sha": "fc51c16b6dbd53abf04fe9175e5421f77e25c49c"
    },
    "output": {
      "role": "endpoint",
      "name": "fixed_fejer_paired_halfwave_normal_lift.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_lift.py",
      "bytes": 96271,
      "sha256": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
      "git_blob_sha": "f285b87e4705b534935dab238d531be22af90740"
    },
    "patches": [
      {
        "before": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
        "after": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
        "count": 1,
        "role": "seed_reference"
      },
      {
        "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
        "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
        "count": 1,
        "role": "meridian"
      },
      {
        "before": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
        "after": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
        "count": 1,
        "role": "new_moment_input"
      },
      {
        "before": "aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3",
        "after": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
        "count": 1,
        "role": "reference_calibration"
      },
      {
        "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
        "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
        "count": 1,
        "role": "closure_values"
      },
      {
        "before": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
        "after": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
        "count": 1,
        "role": "analytic_J3"
      },
      {
        "before": "d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd",
        "after": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
        "count": 1,
        "role": "analytic_frame"
      },
      {
        "before": "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246",
        "after": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
        "count": 1,
        "role": "frame_C1"
      },
      {
        "before": "f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791",
        "after": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
        "count": 1,
        "role": "stage_matrices"
      },
      {
        "before": "bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564",
        "after": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
        "count": 1,
        "role": "adjacent_matrices"
      },
      {
        "before": "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de",
        "after": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
        "count": 1,
        "role": "detached_meridian_values"
      },
      {
        "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
        "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
        "count": 1
      },
      {
        "before": "fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
        "count": 1
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
        "count": 1
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
        "count": 1
      }
    ]
  },
  {
    "role": "geometry",
    "parent": {
      "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
      "bytes": 88163,
      "sha256": "5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135",
      "git_blob_sha": "c5325d3da8329547ad81e74a5da479323bfccd21"
    },
    "output": {
      "role": "geometry",
      "name": "so3_fixed_fejer_halfwave_geometry.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_halfwave_geometry.py",
      "bytes": 88164,
      "sha256": "494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b",
      "git_blob_sha": "602ef5d9e322a3301ede97a811fa9b10044bc61b"
    },
    "patches": [
      {
        "before": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
        "after": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
        "count": 1,
        "reason": "current complete seed_reference source"
      },
      {
        "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
        "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
        "count": 1,
        "reason": "current complete meridian source"
      },
      {
        "before": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
        "after": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
        "count": 1,
        "reason": "current complete new_moment_input source"
      },
      {
        "before": "aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3",
        "after": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
        "count": 1,
        "reason": "current complete reference_calibration source"
      },
      {
        "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
        "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
        "count": 1,
        "reason": "current complete closure_values source"
      },
      {
        "before": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
        "after": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
        "count": 1,
        "reason": "current complete analytic_J3 source"
      },
      {
        "before": "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246",
        "after": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
        "count": 1,
        "reason": "current complete frame_C1 source"
      },
      {
        "before": "f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791",
        "after": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
        "count": 1,
        "reason": "current complete stage_matrices source"
      },
      {
        "before": "bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564",
        "after": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
        "count": 1,
        "reason": "current complete adjacent_matrices source"
      },
      {
        "before": "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de",
        "after": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
        "count": 1,
        "reason": "current complete detached_meridian_values source"
      },
      {
        "before": "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d",
        "after": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
        "count": 1,
        "reason": "current complete endpoint source"
      },
      {
        "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
        "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1",
        "after": "fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1",
        "count": 2,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-batched-missing-angle-envelope-world-geometry-v1",
        "after": "complete-fixed-fejer-paired-halfwave-envelope-world-geometry-v1",
        "count": 1,
        "reason": "current source-family declaration"
      }
    ]
  },
  {
    "role": "batched_geometry_binding",
    "parent": {
      "name": "fixed_fejer_batched_geometry_report_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_batched_geometry_report_binding.py",
      "bytes": 12136,
      "sha256": "9104c29d03a589939f46ccdb08a55a3564f702acd147840cc91488b72eee2d06",
      "git_blob_sha": "60d34ff709af95a702d786e4d0eb77ea7a1e23bf"
    },
    "output": {
      "role": "batched_geometry_binding",
      "name": "fixed_fejer_halfwave_geometry_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_geometry_binding.py",
      "bytes": 12118,
      "sha256": "45aedd26f59920938f6a6245dca48a06293f6cf1593124762a77063e4d0e5102",
      "git_blob_sha": "9c8d986ea6a601e552fa1c50782928dc5f391783"
    },
    "patches": [
      {
        "before": "5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135",
        "after": "494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b",
        "count": 1,
        "reason": "current complete geometry source"
      },
      {
        "before": "so3_fixed_fejer_batched_missing_angle_geometry.py",
        "after": "so3_fixed_fejer_halfwave_geometry.py",
        "count": 1,
        "reason": "current complete geometry path"
      },
      {
        "before": "complete-fixed-fejer-batched-missing-angle-envelope-world-geometry-v1",
        "after": "complete-fixed-fejer-paired-halfwave-envelope-world-geometry-v1",
        "count": 1,
        "reason": "current source-family declaration"
      },
      {
        "before": "actual-fixed-fejer-batched-geometry-report-binding-v1",
        "after": "actual-fixed-fejer-halfwave-geometry-report-binding-v1",
        "count": 1,
        "reason": "current source-family declaration"
      },
      {
        "before": "GEOMETRY_BYTES = 88163",
        "after": "GEOMETRY_BYTES = 88164",
        "count": 1,
        "reason": "current source-family declaration"
      }
    ]
  },
  {
    "role": "envelope_transfer",
    "parent": {
      "name": "fixed_fejer_meridian_memory_transfer.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_memory_transfer.py",
      "bytes": 78920,
      "sha256": "b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc",
      "git_blob_sha": "2e112909d6937363ad0a643a2acbc1e54f7d8bcd"
    },
    "output": {
      "role": "envelope_transfer",
      "name": "fixed_fejer_halfwave_memory_transfer.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_memory_transfer.py",
      "bytes": 78920,
      "sha256": "64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef",
      "git_blob_sha": "27de8f1dbc5ff704be9457617cc8a0a4cec613e6"
    },
    "patches": [
      {
        "before": "3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68",
        "after": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
        "count": 1,
        "reason": "current complete analytic_J3_binding source"
      },
      {
        "before": "fixed_fejer_meridian_source_binding.py",
        "after": "fixed_fejer_paired_halfwave_source_binding.py",
        "count": 1,
        "reason": "current complete analytic_J3_binding path"
      },
      {
        "before": "complete-fixed-fejer-meridian-values-history-and-same-source-continuation-v1",
        "after": "complete-fixed-fejer-halfwave-history-and-same-source-continuation-v1",
        "count": 1,
        "reason": "current source-family declaration"
      }
    ]
  },
  {
    "role": "driver",
    "parent": {
      "name": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
      "bytes": 99313,
      "sha256": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "git_blob_sha": "8bba3e30bb8e843fd725a2d19f8966b984acc4ae"
    },
    "output": {
      "role": "driver",
      "name": "fullclosed_fixed_fejer_halfwave_so3_qp.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_so3_qp.py",
      "bytes": 99375,
      "sha256": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
      "git_blob_sha": "ef97023191b76706692db7aaff20216cbf79efd7"
    },
    "patches": [
      {
        "before": "ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a",
        "after": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
        "count": 1,
        "reason": "current complete seed_reference source"
      },
      {
        "before": "fixed_fejer_supported_meridian_reference.py",
        "after": "fixed_fejer_paired_halfwave_meridian_reference.py",
        "count": 1,
        "reason": "current complete seed_reference path"
      },
      {
        "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
        "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
        "count": 1,
        "reason": "current complete meridian source"
      },
      {
        "before": "fixed_fejer_supported_so3_meridian_operator.py",
        "after": "fixed_fejer_paired_halfwave_meridian_operator.py",
        "count": 1,
        "reason": "current complete meridian path"
      },
      {
        "before": "ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3",
        "after": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
        "count": 1,
        "reason": "current complete new_moment_input source"
      },
      {
        "before": "fixed_fejer_literal_zero_moment_input.py",
        "after": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "count": 1,
        "reason": "current complete new_moment_input path"
      },
      {
        "before": "aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3",
        "after": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
        "count": 1,
        "reason": "current complete reference_calibration source"
      },
      {
        "before": "fixed_fejer_meridian_reference_calibration.py",
        "after": "fixed_fejer_paired_halfwave_reference_calibration.py",
        "count": 1,
        "reason": "current complete reference_calibration path"
      },
      {
        "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
        "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
        "count": 1,
        "reason": "current complete closure_values source"
      },
      {
        "before": "fixed_fejer_meridian_closure_values.py",
        "after": "fixed_fejer_paired_halfwave_closure_values.py",
        "count": 1,
        "reason": "current complete closure_values path"
      },
      {
        "before": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
        "after": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
        "count": 1,
        "reason": "current complete analytic_J3 source"
      },
      {
        "before": "fixed_fejer_meridian_analytic_stage_jacobian.py",
        "after": "fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "count": 1,
        "reason": "current complete analytic_J3 path"
      },
      {
        "before": "d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd",
        "after": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
        "count": 1,
        "reason": "current complete analytic_frame source"
      },
      {
        "before": "fixed_fejer_meridian_analytic_normal_frame.py",
        "after": "fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "count": 1,
        "reason": "current complete analytic_frame path"
      },
      {
        "before": "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246",
        "after": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
        "count": 1,
        "reason": "current complete frame_C1 source"
      },
      {
        "before": "fixed_fejer_meridian_normal_frame_c1.py",
        "after": "fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "count": 1,
        "reason": "current complete frame_C1 path"
      },
      {
        "before": "f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791",
        "after": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
        "count": 1,
        "reason": "current complete stage_matrices source"
      },
      {
        "before": "fixed_fejer_meridian_stage_matrices.py",
        "after": "fixed_fejer_paired_halfwave_stage_matrices.py",
        "count": 1,
        "reason": "current complete stage_matrices path"
      },
      {
        "before": "bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564",
        "after": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
        "count": 1,
        "reason": "current complete adjacent_matrices source"
      },
      {
        "before": "fixed_fejer_meridian_adjacent_matrices.py",
        "after": "fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "count": 1,
        "reason": "current complete adjacent_matrices path"
      },
      {
        "before": "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de",
        "after": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
        "count": 1,
        "reason": "current complete detached_meridian_values source"
      },
      {
        "before": "fixed_fejer_detached_meridian_values.py",
        "after": "fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "count": 1,
        "reason": "current complete detached_meridian_values path"
      },
      {
        "before": "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d",
        "after": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
        "count": 1,
        "reason": "current complete endpoint source"
      },
      {
        "before": "fixed_fejer_detached_meridian_normal_lift.py",
        "after": "fixed_fejer_paired_halfwave_normal_lift.py",
        "count": 1,
        "reason": "current complete endpoint path"
      },
      {
        "before": "5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135",
        "after": "494c5fc9daffac2417842c7e4619429e5b5370acfc909b206e1d1c8dc02e865b",
        "count": 1,
        "reason": "current complete geometry source"
      },
      {
        "before": "so3_fixed_fejer_batched_missing_angle_geometry.py",
        "after": "so3_fixed_fejer_halfwave_geometry.py",
        "count": 1,
        "reason": "current complete geometry path"
      },
      {
        "before": "9104c29d03a589939f46ccdb08a55a3564f702acd147840cc91488b72eee2d06",
        "after": "45aedd26f59920938f6a6245dca48a06293f6cf1593124762a77063e4d0e5102",
        "count": 1,
        "reason": "current complete batched_geometry_binding source"
      },
      {
        "before": "fixed_fejer_batched_geometry_report_binding.py",
        "after": "fixed_fejer_halfwave_geometry_binding.py",
        "count": 1,
        "reason": "current complete batched_geometry_binding path"
      },
      {
        "before": "c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4",
        "after": "8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a",
        "count": 1,
        "reason": "current complete root_packets source"
      },
      {
        "before": "fixed_fejer_meridian_root_packets.py",
        "after": "fixed_fejer_paired_halfwave_root_packets.py",
        "count": 1,
        "reason": "current complete root_packets path"
      },
      {
        "before": "3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68",
        "after": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
        "count": 1,
        "reason": "current complete analytic_J3_binding source"
      },
      {
        "before": "fixed_fejer_meridian_source_binding.py",
        "after": "fixed_fejer_paired_halfwave_source_binding.py",
        "count": 1,
        "reason": "current complete analytic_J3_binding path"
      },
      {
        "before": "b8af97a4772e5d641c5daea3f2232c65fe52055154d94e45b4c88f661e9778dc",
        "after": "64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef",
        "count": 1,
        "reason": "current complete envelope_transfer source"
      },
      {
        "before": "fixed_fejer_meridian_memory_transfer.py",
        "after": "fixed_fejer_halfwave_memory_transfer.py",
        "count": 1,
        "reason": "current complete envelope_transfer path"
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-meridian-batched-observed-material-envelope-SO3-QP-v1",
        "after": "complete-fixed-fejer-paired-halfwave-material-envelope-SO3-QP-v1",
        "count": 1,
        "reason": "current source-family declaration"
      }
    ]
  },
  {
    "role": "launcher",
    "parent": {
      "name": "launch_fixed_fejer_meridian_batched_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py",
      "bytes": 22136,
      "sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
      "git_blob_sha": "168b1a1d7bc58793985138eb8a02a6e3911d74cc"
    },
    "output": {
      "role": "launcher",
      "name": "launch_fixed_fejer_halfwave_actions.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_halfwave_actions.py",
      "bytes": 22120,
      "sha256": "6fd57ab06a8655522e5b79eadaa73fdf7cba93309d86cd2568e91845473cd99c",
      "git_blob_sha": "7711e406787df02c8e0ab45965050c010c3b6f3b"
    },
    "patches": [
      {
        "before": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
        "after": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
        "count": 1,
        "reason": "current complete driver source"
      },
      {
        "before": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
        "after": "fullclosed_fixed_fejer_halfwave_so3_qp.py",
        "count": 1,
        "reason": "current complete driver path"
      },
      {
        "before": "public-actions-complete-fixed-fejer-meridian-batched-SO3-command-v1",
        "after": "public-actions-complete-fixed-fejer-halfwave-SO3-command-v1",
        "count": 1,
        "reason": "current source-family declaration"
      }
    ]
  },
  {
    "role": "reader",
    "parent": {
      "name": "read_fixed_fejer_meridian_batched_so3_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_meridian_batched_so3_report.py",
      "bytes": 99382,
      "sha256": "8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49",
      "git_blob_sha": "9cd36fd99113d285fc47f17bad929647c8fc6de3"
    },
    "output": {
      "role": "reader",
      "name": "read_fixed_fejer_halfwave_so3_report.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_halfwave_so3_report.py",
      "bytes": 99816,
      "sha256": "be9bb58fa612fc25ab01458a2d6e21e0fa10c7573dad37e65effb845c6e29e92",
      "git_blob_sha": "04cf36b7372841fc714ebe827b7530ec9fed9945"
    },
    "patches": [
      {
        "before": "fixed_fejer_literal_zero_moment_input.py",
        "after": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "count": 1,
        "reason": "current complete new_moment_input path"
      },
      {
        "before": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
        "after": "095bf318e9440358f2fef9a7b71c47eb65df546a3f113d76b2984637a10d80ec",
        "count": 1,
        "reason": "current complete driver source"
      },
      {
        "before": "fullclosed_fixed_fejer_meridian_batched_so3_qp.py",
        "after": "fullclosed_fixed_fejer_halfwave_so3_qp.py",
        "count": 1,
        "reason": "current complete driver path"
      },
      {
        "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
        "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1",
        "after": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "fixed-fejer-supported-reference-literal-two-bubble-endpoint-Q-v1",
        "after": "fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1",
        "after": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1",
        "after": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-supported-smooth-triangle-seed-radial-plan-v1",
        "after": "complete-paired-halfwave-seed-radial-plan-v1",
        "count": 1,
        "reason": "explicit new seed schema"
      },
      {
        "before": "complete-fixed-fejer-meridian-batched-observed-material-envelope-SO3-QP-v1",
        "after": "complete-fixed-fejer-paired-halfwave-material-envelope-SO3-QP-v1",
        "count": 1,
        "reason": "current source-family declaration"
      },
      {
        "before": "actual-fixed-fejer-meridian-batched-observed-envelope-SO3-readout-v1",
        "after": "actual-fixed-fejer-halfwave-observed-envelope-SO3-readout-v1",
        "count": 1,
        "reason": "current source-family declaration"
      },
      {
        "before": "                or plan.get('source_sha256') != roles['seed_reference']",
        "after": "                or plan.get('source_sha256') != roles['seed_reference']\n                or plan.get('paired_halfwave_definition') != seed['paired_halfwave_definition']\n                or plan.get('every_physical_halfwave_breakpoint_in_complete_partition') is not True\n                or plan.get('complete_physical_pair_piece_count') != 12\n                or plan.get('auxiliary_mean_rule_piece_count') != 12\n                or plan.get('physical_sine_cancellation_scope') != 'both equal complete central intervals together'",
        "count": 1,
        "reason": "current source-family declaration"
      }
    ]
  }
]''')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def checked_parent(repo, record):
    path = repo / record["path"]
    raw = path.read_bytes()
    if len(raw) != record["bytes"] or digest(raw) != record["sha256"]:
        raise ValueError("Use the entire fixed original source: " + str(path))
    return raw.decode("utf-8")


def construct(parent, spec):
    text = parent
    for patch in spec["patches"]:
        if text.count(patch["before"]) != patch["count"]:
            raise ValueError("The whole original literal changed: " + spec["role"])
        text = text.replace(patch["before"], patch["after"])
    raw = text.encode("utf-8")
    expected = spec["output"]
    if len(raw) != expected["bytes"] or digest(raw) != expected["sha256"]:
        raise ValueError("The complete reproduced source differs: " + spec["role"])
    restored = text
    for patch in reversed(spec["patches"]):
        if restored.count(patch["after"]) != patch["count"]:
            raise ValueError("The exact reverse literal changed: " + spec["role"])
        restored = restored.replace(patch["after"], patch["before"])
    if restored != parent:
        raise ValueError("Retain the complete original source: " + spec["role"])
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.out.resolve()
    records = []
    for spec in SPECS:
        raw = construct(checked_parent(repo, spec["parent"]), spec)
        destination = out / spec["output"]["path"]
        if destination.exists() and destination.read_bytes() != raw:
            raise FileExistsError("Do not overwrite different existing bytes: " + str(destination))
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
        records.append(spec["output"])
    print(json.dumps(dict(schema="complete-paired-halfwave-upper-source-text-reproduction-v1",
        complete_sources=records, source_count=len(records),
        scientific_execution_performed=False, extra_admission_step=False), indent=2))


if __name__ == "__main__":
    main()
