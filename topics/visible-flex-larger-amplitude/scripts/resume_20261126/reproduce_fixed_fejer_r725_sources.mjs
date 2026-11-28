#!/usr/bin/env node
/**
 * Construct the complete independent R725 scientific source family.
 * Text and byte identities only: no Python import, AST, field, root, fixture,
 * benchmark or numerical evaluation. This is a reproducer, not an admission gate.
 * Whole original files remain the fixed parents. All literal patch bodies are
 * present below, including the complete pure metadata function relocation.
 */
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const DATA = {
  "schema": "complete-R725-scientific-source-text-construction-v1",
  "parent_runtime_binding": {
    "role": "complete_runtime_binding",
    "name": "fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-paired-halfwave-curvature-cache-current-runtime-binding.json",
    "bytes": 51709,
    "sha256": "d449d0a54b69b23c598234a28fede12917473ce7058e9d8815ba8b524c6f869f",
    "git_blob_sha": "38f781117d79710e72947cb8f8f0ecb258f0dabb"
  },
  "complete_outputs": [
    {
      "role": "analytic_J3",
      "parent": {
        "role": "analytic_J3",
        "name": "fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "bytes": 25706,
        "sha256": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
        "git_blob_sha": "aaa1d6b48f02d62b5a7a445932304d3e36730fa3"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_analytic_stage_jacobian.py",
        "name": "fixed_fejer_r725_analytic_stage_jacobian.py",
        "bytes": 25695,
        "sha256": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
        "git_blob_sha": "168028b77a73803d685ea9cd8f41a6ad57497adb"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual complete closure_values source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "frame_C1",
      "parent": {
        "role": "frame_C1",
        "name": "fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "bytes": 37361,
        "sha256": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
        "git_blob_sha": "84a063e3efaa54b872b3ff0ff0f8a222ba0712e0"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_normal_frame_c1.py",
        "name": "fixed_fejer_r725_normal_frame_c1.py",
        "bytes": 37361,
        "sha256": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
        "git_blob_sha": "a029d203db41ce32c0f12bfd1ba05f4750ad426f"
      },
      "patches": [
        {
          "label": "actual complete analytic_J3 source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete closure_values source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "stage_matrices",
      "parent": {
        "role": "stage_matrices",
        "name": "fixed_fejer_paired_halfwave_stage_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_stage_matrices.py",
        "bytes": 61280,
        "sha256": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
        "git_blob_sha": "9eabce7cdf2460213b8d2bea4005321ec9ab4591"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_stage_matrices.py",
        "name": "fixed_fejer_r725_stage_matrices.py",
        "bytes": 61280,
        "sha256": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
        "git_blob_sha": "040cf58e8933d19b04485fd409b338e99480a47d"
      },
      "patches": [
        {
          "label": "actual complete analytic_J3 source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 source",
          "old": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "new": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "adjacent_matrices",
      "parent": {
        "role": "adjacent_matrices",
        "name": "fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "bytes": 36766,
        "sha256": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
        "git_blob_sha": "6fcac6e4f16191b2b7be20f1c04bbab884632985"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_adjacent_matrices.py",
        "name": "fixed_fejer_r725_adjacent_matrices.py",
        "bytes": 36766,
        "sha256": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
        "git_blob_sha": "4ff977c1672b0bbaecf2ae9d3cac047c0fad3670"
      },
      "patches": [
        {
          "label": "actual complete analytic_J3 source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 source",
          "old": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "new": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices source",
          "old": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
          "new": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "reference_calibration",
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_reference_calibration.py",
        "name": "fixed_fejer_paired_halfwave_reference_calibration.py",
        "bytes": 11872,
        "sha256": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
        "git_blob_sha": "812e981a9e4a6302c6241129dd812c251bb92691"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_reference_calibration.py",
        "name": "fixed_fejer_r725_reference_calibration.py",
        "bytes": 11850,
        "sha256": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
        "git_blob_sha": "c1d612b7e403a9877e98501e799b9713a7a84389"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        },
        {
          "label": "actual complete seed_reference source",
          "old": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "new": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
          "count": 1
        }
      ]
    },
    {
      "role": "endpoint",
      "parent": {
        "role": "endpoint",
        "name": "fixed_fejer_paired_halfwave_normal_lift.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_lift.py",
        "bytes": 96271,
        "sha256": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
        "git_blob_sha": "f285b87e4705b534935dab238d531be22af90740"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_normal_lift.py",
        "name": "fixed_fejer_r725_normal_lift.py",
        "bytes": 96250,
        "sha256": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
        "git_blob_sha": "f68cc3f67a8f64ac49149fa86ad10c3994736e0e"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "actual R725 seed schema",
          "old": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
          "new": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
          "count": 1
        },
        {
          "label": "actual R725 input schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
          "new": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3 source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 source",
          "old": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "new": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices source",
          "old": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
          "new": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
          "count": 1
        },
        {
          "label": "actual complete adjacent_matrices source",
          "old": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
          "new": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
          "count": 1
        },
        {
          "label": "actual complete reference_calibration source",
          "old": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
          "new": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
          "count": 1
        },
        {
          "label": "actual complete analytic_frame source",
          "old": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
          "new": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
          "count": 1
        },
        {
          "label": "actual complete closure_values source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values source",
          "old": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
          "new": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        },
        {
          "label": "actual complete new_moment_input source",
          "old": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
          "new": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
          "count": 1
        },
        {
          "label": "actual complete seed_reference source",
          "old": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "new": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
          "count": 1
        }
      ]
    },
    {
      "role": "analytic_frame",
      "parent": {
        "role": "analytic_frame",
        "name": "fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "bytes": 47440,
        "sha256": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
        "git_blob_sha": "263534a4e65f31b45cf1f9a40441f5896e213e2b"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_analytic_normal_frame.py",
        "name": "fixed_fejer_r725_analytic_normal_frame.py",
        "bytes": 47429,
        "sha256": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
        "git_blob_sha": "ec3dcb2fbb86a0ddd3769088a7b22ec93eb712c1"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual complete closure_values source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "closure_values",
      "parent": {
        "role": "closure_values",
        "name": "fixed_fejer_paired_halfwave_closure_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_closure_values.py",
        "bytes": 59449,
        "sha256": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
        "git_blob_sha": "5e7230ce5dc57adffe58901b04257c1469fa8e8c"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_closure_values.py",
        "name": "fixed_fejer_r725_closure_values.py",
        "bytes": 59438,
        "sha256": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
        "git_blob_sha": "f5e937ae12c4d769aeeae390fc1546dfa45f0375"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "detached_meridian_values",
      "parent": {
        "role": "detached_meridian_values",
        "name": "fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "bytes": 41135,
        "sha256": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
        "git_blob_sha": "7075bca30d05c045023b7823b8f80b75bfd34d4f"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_detached_meridian_values.py",
        "name": "fixed_fejer_r725_detached_meridian_values.py",
        "bytes": 41124,
        "sha256": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
        "git_blob_sha": "01d785136dc76b5d9e521ff8458e4feb75fdcfca"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual complete closure_values source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete meridian source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        }
      ]
    },
    {
      "role": "root_packets",
      "parent": {
        "role": "root_packets",
        "name": "fixed_fejer_paired_halfwave_root_packets.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_root_packets.py",
        "bytes": 74385,
        "sha256": "8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a",
        "git_blob_sha": "b340f47df551b4609e45ae547449adadbc3368b6"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_root_packets.py",
        "name": "fixed_fejer_r725_root_packets.py",
        "bytes": 75036,
        "sha256": "71f80c72819f70d62ce2be70e075aa0ebda4130db3ebf7de7616d8a173ffeea1",
        "git_blob_sha": "acbd48bf27a4fbc00b77c11dba369a569c764605"
      },
      "patches": [
        {
          "label": "append one complete R725 normal identity; retain every historical entry",
          "old": "NORMALS = {\n",
          "new": "NORMALS = {\n    'c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b': dict(schema='complete-fixed-fejer-r725-detached-meridian-normal-layer-v1',\n        base='b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792',\n        adjacent='f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2',calibration='8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20',\n        analytic='abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee',analytic_frame='90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0',\n        closure_values='07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6'),\n",
          "count": 1
        }
      ]
    },
    {
      "role": "analytic_J3_binding",
      "parent": {
        "role": "analytic_J3_binding",
        "name": "fixed_fejer_paired_halfwave_source_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_source_binding.py",
        "bytes": 41966,
        "sha256": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
        "git_blob_sha": "1abdf0ca7867b1deb54a2a6d6e7c8130e42cf948"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_source_binding.py",
        "name": "fixed_fejer_r725_source_binding.py",
        "bytes": 50527,
        "sha256": "bac157aba56f246d1c28510c5b54b8380438be4e133ade535e5096bd3ea1f488",
        "git_blob_sha": "f1f59a47b5f6eec2abf6d5b6cd247417a4a14c56"
      },
      "patches": [
        {
          "label": "actual R725 binding schema",
          "old": "complete-fixed-fejer-paired-halfwave-source-model-and-report-binding-v1",
          "new": "complete-fixed-fejer-r725-source-model-and-report-binding-v1",
          "count": 1
        },
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3 whole source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3 basename",
          "old": "fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
          "new": "fixed_fejer_r725_analytic_stage_jacobian.py",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 whole source",
          "old": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "new": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 basename",
          "old": "fixed_fejer_paired_halfwave_normal_frame_c1.py",
          "new": "fixed_fejer_r725_normal_frame_c1.py",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices whole source",
          "old": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
          "new": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices basename",
          "old": "fixed_fejer_paired_halfwave_stage_matrices.py",
          "new": "fixed_fejer_r725_stage_matrices.py",
          "count": 1
        },
        {
          "label": "actual complete adjacent_matrices whole source",
          "old": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
          "new": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
          "count": 1
        },
        {
          "label": "actual complete adjacent_matrices basename",
          "old": "fixed_fejer_paired_halfwave_adjacent_matrices.py",
          "new": "fixed_fejer_r725_adjacent_matrices.py",
          "count": 1
        },
        {
          "label": "actual complete reference_calibration whole source",
          "old": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
          "new": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
          "count": 1
        },
        {
          "label": "actual complete reference_calibration basename",
          "old": "fixed_fejer_paired_halfwave_reference_calibration.py",
          "new": "fixed_fejer_r725_reference_calibration.py",
          "count": 1
        },
        {
          "label": "actual complete endpoint whole source",
          "old": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
          "new": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
          "count": 1
        },
        {
          "label": "actual complete endpoint basename",
          "old": "fixed_fejer_paired_halfwave_normal_lift.py",
          "new": "fixed_fejer_r725_normal_lift.py",
          "count": 1
        },
        {
          "label": "actual complete analytic_frame whole source",
          "old": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
          "new": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
          "count": 1
        },
        {
          "label": "actual complete analytic_frame basename",
          "old": "fixed_fejer_paired_halfwave_analytic_normal_frame.py",
          "new": "fixed_fejer_r725_analytic_normal_frame.py",
          "count": 1
        },
        {
          "label": "actual complete closure_values whole source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete closure_values basename",
          "old": "fixed_fejer_paired_halfwave_closure_values.py",
          "new": "fixed_fejer_r725_closure_values.py",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values whole source",
          "old": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
          "new": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values basename",
          "old": "fixed_fejer_paired_halfwave_detached_meridian_values.py",
          "new": "fixed_fejer_r725_detached_meridian_values.py",
          "count": 1
        },
        {
          "label": "actual complete meridian whole source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        },
        {
          "label": "relocate the complete pure seed metadata reader and bind all R725 boundary-plan fields",
          "old": "def bind_fixed_fejer_input(path, *, current_files=None):",
          "new": "def supported_seed_metadata(value, model, roles, supported):\n    \"\"\"Read actual frozen-reference work; do not promote it to current normal roots.\"\"\"\n    base = value['base_complete_metadata']\n    seed = supported['definition']\n    identity = supported['identity_sha256']\n    actual = base.get('fixed_supported_unit_seed')\n    if (not isinstance(actual, dict)\n            or base.get('fixed_supported_unit_seed_identity_sha256') != identity\n            or base.get('axisymmetric_reference_binding') != supported['binding']\n            or base.get('seed_mean_Jacobian_not_a_certificate_for_current_closure_control_Jacobian') is not True\n            or actual.get('schema') != seed['schema']\n            or actual.get('source_sha256') != roles['seed_reference']\n            or actual.get('model') != seed\n            or actual.get('model_identity_sha256') != identity\n            or actual.get('binding') != supported['binding']\n            or actual.get('working_definition') != seed['working_definition']):\n        raise ValueError('The actual provider metadata belongs to another frozen supported seed')\n    for name in ('exact_seed_global_existence_hypotheses_certified',\n                 'seed_physical_field_or_normal_control_rank_inherited',\n                 'continuous_metric_geometry_or_full_phase_certificate'):\n        if actual.get(name) is not False:\n            raise ValueError('A working seed evaluation is not its accurate continuous certificate: '+name)\n    plan = actual.get('radial_plan')\n    if plan is not None:\n        if (plan.get('schema') != 'complete-paired-halfwave-flat-cutoff-seed-radial-plan-v1'\n                or plan.get('source_sha256') != roles['seed_reference']\n                or plan.get('paired_halfwave_definition') != seed['paired_halfwave_definition']\n                or plan.get('boundary_cutoff_definition') != seed['boundary_cutoff_definition']\n                or plan.get('exact_boundary_cutoff_epsilon') != seed['exact_boundary_cutoff_epsilon']\n                or plan.get('exact_boundary_cutoff_epsilon') != '1/8'\n                or plan.get('every_internal_boundary_cut_in_complete_partition') is not True\n                or plan.get('complete_physical_boundary_piece_count') != 12\n                or plan.get('complete_internal_boundary_cut_count') != 8\n                or plan.get('every_physical_halfwave_breakpoint_in_complete_partition') is not True\n                or plan.get('complete_physical_pair_piece_count') != 12\n                or plan.get('auxiliary_mean_rule_piece_count') != 12\n                or plan.get('physical_sine_cancellation_scope') != 'both equal complete central intervals together'\n                or plan.get('seed_model_identity_sha256') != identity\n                or plan.get('complete_domain') is not True\n                or plan.get('complete_infinite_scalar_tail_in_complement') is not True\n                or plan.get('no_scalar_tail_or_radial_piece_dropped') is not True\n                or plan.get('central_profile_integral_is_separate') is not True\n                or plan.get('numerical_integral_error_enclosed') is not False\n                or plan.get('scalar_errors_are_not_normalization_or_integration_errors') is not True):\n            raise ValueError('The actual seed radial plan must retain all pieces and its unpaid numerical fees')\n    batches = actual['mean_batch_records']\n    if not isinstance(batches, list):\n        raise ValueError('Keep every actual completed seed-mean batch record')\n    completed = []\n    for batch in batches:\n        metadata = batch['metadata']\n        angles = batch['literal_angle_hex']\n        if (batch.get('seed_model_identity_sha256') != identity\n                or batch.get('fixed_original_core_H_used') is not True\n                or batch.get('current_outer_free_point_not_used') is not True\n                or metadata.get('schema') != 'complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1'\n                or metadata.get('source_sha256') != roles['seed_mean']\n                or metadata.get('complete') is not True\n                or metadata.get('actual_successful_angle_count') != len(angles)):\n            raise ValueError('A completed seed batch must keep its actual angle count, original point and whole kernel source')\n        for word in angles:\n            if not isinstance(word, str):\n                raise ValueError('The fixed seed cache uses exact literal binary64 angle words')\n            angle = float.fromhex(word)\n            if not math.isfinite(angle) or angle.hex() != word:\n                raise ValueError('A recorded fixed-seed angle word is not canonical and finite')\n        for name in ('mean_root_complete','central_amplitude_root_complete',\n                     'all_three_mean_components_used','all_twelve_profile_pieces_used',\n                     'all_input_angles_retained','reference_angle_jets_only'):\n            if metadata.get(name) is not True:\n                raise ValueError('A partial mean or angular jet is not a complete seed batch: '+name)\n        for name in ('continuous_contraction_verified','exact_root_or_angle_jet_errors_enclosed',\n                     'quadrature_and_floating_errors_enclosed','geometry_certificate',\n                     'metric_certificate','current_free_parameter_J_claimed',\n                     'accurate_global_branch_association_verified'):\n            if metadata.get(name) is not False:\n                raise ValueError('Keep the actual seed-mean result within its numerical scope: '+name)\n        completed.extend(angles)\n    if len(completed) != len(set(completed)):\n        raise ValueError('A completed fixed-reference batch cannot repeat a previously recorded literal angle')\n    # The actual provider stores arrays and increments counters before writing\n    # its runner files and appending a complete batch record. A real interrupted\n    # cache write may therefore leave fewer complete records than cached values.\n    # Keep those actual scopes separate, including in an initial-failure report.\n    completed_cache = actual['completed_literal_angle_count']\n    completed_counter = actual['counts']['completed_mean_angles']\n    for number in (completed_cache, completed_counter):\n        if isinstance(number, bool) or not isinstance(number, int) or number < 0:\n            raise ValueError('Keep actual nonnegative integer seed cache/count readouts')\n    accounting_matches = completed_cache == completed_counter == len(completed)\n    failure = actual.get('last_failure')\n    if failure is not None and (failure.get('schema') != seed['schema']\n            or failure.get('source_sha256') != roles['seed_reference']\n            or failure.get('seed_model_identity_sha256') != identity\n            or failure.get('fixed_scalar_metric_identity_sha256') != model['fixed_scalar_metric_identity_sha256']\n            or failure.get('complete') is not False\n            or failure.get('continuous_certificate') is not False):\n        raise ValueError('The recorded seed failure belongs to another source, fixed input or scientific scope')\n    return dict(schema='actual-fixed-supported-smooth-triangle-reference-working-readout-v1',\n        source_sha256=roles['seed_reference'], mean_kernel_source_sha256=roles['seed_mean'],\n        fixed_supported_unit_seed_identity_sha256=identity,\n        actual_counts=actual['counts'],\n        completed_literal_angle_count=completed_cache, mean_successful_batch_count=len(batches),\n        complete_batch_recorded_angle_count=len(completed),\n        complete_batch_records_match_cached_angle_count=accounting_matches,\n        completed_batch_literal_angle_hex=completed,\n        complete_radial_plan_available=plan is not None, radial_plan=plan,\n        boundary_cutoff_definition=seed['boundary_cutoff_definition'],\n        exact_boundary_cutoff_epsilon=seed['exact_boundary_cutoff_epsilon'],\n        mean_batch_records=batches,\n        last_recorded_seed_failure=failure,\n        last_seed_failure_phase=None if failure is None else failure['failure_phase'],\n        last_seed_failure_reason=None if failure is None else failure['reason'],\n        maximum_original_scalar_carrier_errors=actual['maximum_original_scalar_carrier_errors'],\n        frozen_reference_cache_is_not_current_normal_root_availability=True,\n        seed_mean_inverse_is_not_normal_control_inverse_certificate=True,\n        fixed_seed_changed_the_original_scalar_target=False,\n        exact_seed_global_existence_hypotheses_certified=False,\n        seed_root_or_angle_jet_error_enclosed=False,\n        seed_quadrature_or_normalization_error_enclosed=False,\n        seed_continuous_metric_or_geometry_certified=False)\n\ndef bind_fixed_fejer_input(path, *, current_files=None):",
          "count": 1
        }
      ]
    },
    {
      "role": "geometry",
      "parent": {
        "role": "geometry",
        "name": "so3_fixed_fejer_halfwave_dk_cache_geometry.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_halfwave_dk_cache_geometry.py",
        "bytes": 88487,
        "sha256": "da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316",
        "git_blob_sha": "624871ceac5955b78fe2ba0728ff50ddee99d64d"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_r725_dk_cache_geometry.py",
        "name": "so3_fixed_fejer_r725_dk_cache_geometry.py",
        "bytes": 88422,
        "sha256": "a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced",
        "git_blob_sha": "bd8f50715b8fbe971e11634b5b7b0539c8a37844"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "actual R725 seed schema",
          "old": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
          "new": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
          "count": 1
        },
        {
          "label": "actual R725 input schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
          "new": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
          "count": 1
        },
        {
          "label": "actual R725 input_definition schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1",
          "new": "fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
          "count": 2
        },
        {
          "label": "actual R725 geometry schema",
          "old": "complete-fixed-fejer-paired-halfwave-dk-cache-world-geometry-v1",
          "new": "complete-fixed-fejer-r725-dk-cache-world-geometry-v1",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3 whole source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 whole source",
          "old": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "new": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices whole source",
          "old": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
          "new": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
          "count": 1
        },
        {
          "label": "actual complete adjacent_matrices whole source",
          "old": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
          "new": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
          "count": 1
        },
        {
          "label": "actual complete reference_calibration whole source",
          "old": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
          "new": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
          "count": 1
        },
        {
          "label": "actual complete endpoint whole source",
          "old": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
          "new": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
          "count": 1
        },
        {
          "label": "actual complete closure_values whole source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values whole source",
          "old": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
          "new": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
          "count": 1
        },
        {
          "label": "actual complete geometry_selector whole source",
          "old": "f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112",
          "new": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
          "count": 1
        },
        {
          "label": "actual complete geometry_selector basename",
          "old": "fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
          "new": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
          "count": 1
        },
        {
          "label": "actual complete meridian whole source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        },
        {
          "label": "actual complete new_moment_input whole source",
          "old": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
          "new": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
          "count": 1
        },
        {
          "label": "actual complete seed_reference whole source",
          "old": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "new": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
          "count": 1
        }
      ]
    },
    {
      "role": "envelope_transfer",
      "parent": {
        "role": "envelope_transfer",
        "name": "fixed_fejer_halfwave_memory_transfer.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_memory_transfer.py",
        "bytes": 78920,
        "sha256": "64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef",
        "git_blob_sha": "27de8f1dbc5ff704be9457617cc8a0a4cec613e6"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_memory_transfer.py",
        "name": "fixed_fejer_r725_memory_transfer.py",
        "bytes": 78945,
        "sha256": "d9615e37f3fd0da916147674ff8f47be69cb6876ba98aa71e78eccd4d2fcc637",
        "git_blob_sha": "f5758234ebe77f6f1f406acf35a40b607922885b"
      },
      "patches": [
        {
          "label": "actual R725 transfer schema",
          "old": "complete-fixed-fejer-halfwave-history-and-same-source-continuation-v1",
          "new": "complete-fixed-fejer-r725-history-and-same-source-continuation-v1",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3_binding whole source",
          "old": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
          "new": "bac157aba56f246d1c28510c5b54b8380438be4e133ade535e5096bd3ea1f488",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3_binding basename",
          "old": "fixed_fejer_paired_halfwave_source_binding.py",
          "new": "fixed_fejer_r725_source_binding.py",
          "count": 1
        },
        {
          "label": "accurate distinct R725 seed-parent scope",
          "old": "actual_fixed_fejer_complete_terminal_report_and_full13_final_transfer_supported=True,",
          "new": "actual_fixed_fejer_complete_terminal_report_and_full13_final_transfer_supported=False,",
          "count": 1
        },
        {
          "label": "distinct physical boundary law is not merely a cache policy",
          "old": "only_plain_detached_meridian_values_and_recursive_source_policy_changed=True,",
          "new": "only_plain_detached_meridian_values_and_recursive_source_policy_changed=False,",
          "count": 1
        },
        {
          "label": "complete explicit physical model change description",
          "old": "changed_model_fields='same predeclared Fejer target, full layout and all stage equations; optional plain-detached meridian integration values and their exact recursive source policies only',",
          "new": "changed_model_fields='same predeclared Fejer target and full layout; distinct R725 epsilon=1/8 boundary law, full split seed plan and new seed/Q/calibration identities; old complete physical-model equality guards remain strict',",
          "count": 1
        }
      ]
    },
    {
      "role": "batched_geometry_binding",
      "parent": {
        "role": "batched_geometry_binding",
        "name": "fixed_fejer_halfwave_dk_cache_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_halfwave_dk_cache_binding.py",
        "bytes": 20546,
        "sha256": "ca2a7884039df93f7b5b243d476c60d2e8e810bf1071545a84bbc283a460aaad",
        "git_blob_sha": "319ed19012c7b588e85108a98ace0efcca830c75"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_dk_cache_binding.py",
        "name": "fixed_fejer_r725_dk_cache_binding.py",
        "bytes": 20516,
        "sha256": "d951f9e5f8088fdbd58357e29bca71f8057e5133693112657c288f57346c2819",
        "git_blob_sha": "622c9c7a5eb21430c268eb277cc8b81a71e6ae3a"
      },
      "patches": [
        {
          "label": "actual R725 geometry schema",
          "old": "complete-fixed-fejer-paired-halfwave-dk-cache-world-geometry-v1",
          "new": "complete-fixed-fejer-r725-dk-cache-world-geometry-v1",
          "count": 1
        },
        {
          "label": "actual R725 cache_binding schema",
          "old": "actual-fixed-fejer-halfwave-dk-cache-report-binding-v1",
          "new": "actual-fixed-fejer-r725-dk-cache-report-binding-v1",
          "count": 1
        },
        {
          "label": "actual complete geometry whole source",
          "old": "da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316",
          "new": "a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced",
          "count": 1
        },
        {
          "label": "actual complete geometry basename",
          "old": "so3_fixed_fejer_halfwave_dk_cache_geometry.py",
          "new": "so3_fixed_fejer_r725_dk_cache_geometry.py",
          "count": 1
        },
        {
          "label": "actual complete geometry_selector whole source",
          "old": "f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112",
          "new": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
          "count": 1
        },
        {
          "label": "actual complete geometry_selector basename",
          "old": "fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
          "new": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
          "count": 1
        },
        {
          "label": "whole actual geometry byte count",
          "old": "GEOMETRY_BYTES = 88487",
          "new": "GEOMETRY_BYTES = 88422",
          "count": 1
        }
      ]
    },
    {
      "role": "driver",
      "parent": {
        "role": "driver",
        "name": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
        "bytes": 99410,
        "sha256": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910",
        "git_blob_sha": "c0e24fb110b3f893bbd1fa1d52eb2457d78c6872"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_r725_dk_cache_qp.py",
        "name": "fullclosed_fixed_fejer_r725_dk_cache_qp.py",
        "bytes": 99234,
        "sha256": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
        "git_blob_sha": "a58a8ed42deb53dc87df487287e9abd3feb0deb3"
      },
      "patches": [
        {
          "label": "actual R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "actual R725 report schema",
          "old": "complete-fixed-fejer-paired-halfwave-dk-cache-SO3-QP-v1",
          "new": "complete-fixed-fejer-r725-dk-cache-SO3-QP-v1",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3 whole source",
          "old": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "new": "abaff31c7553e1ff180242783111c05664cbffad57bf7c079d238d465518d0ee",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3 basename",
          "old": "fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
          "new": "fixed_fejer_r725_analytic_stage_jacobian.py",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 whole source",
          "old": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "new": "4d60d99868c19c5b75d216239b70c10dba27cdf7ddc9b08c913003ed0c0fb6f8",
          "count": 1
        },
        {
          "label": "actual complete frame_C1 basename",
          "old": "fixed_fejer_paired_halfwave_normal_frame_c1.py",
          "new": "fixed_fejer_r725_normal_frame_c1.py",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices whole source",
          "old": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
          "new": "e9c60be0bc7399c2362b9a08cdc5381a54e448657466f9e201f56f067ea98143",
          "count": 1
        },
        {
          "label": "actual complete stage_matrices basename",
          "old": "fixed_fejer_paired_halfwave_stage_matrices.py",
          "new": "fixed_fejer_r725_stage_matrices.py",
          "count": 1
        },
        {
          "label": "actual complete adjacent_matrices whole source",
          "old": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
          "new": "f0686e4609c002dbc2edd5e7b839437b0d7cb5150b86c58d7e9ea87a91fae9f2",
          "count": 1
        },
        {
          "label": "actual complete adjacent_matrices basename",
          "old": "fixed_fejer_paired_halfwave_adjacent_matrices.py",
          "new": "fixed_fejer_r725_adjacent_matrices.py",
          "count": 1
        },
        {
          "label": "actual complete reference_calibration whole source",
          "old": "c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106",
          "new": "8126c6793e8b5e8038d7f144f58cad08a08dbfe1053140f7fa03d506beb43e20",
          "count": 1
        },
        {
          "label": "actual complete reference_calibration basename",
          "old": "fixed_fejer_paired_halfwave_reference_calibration.py",
          "new": "fixed_fejer_r725_reference_calibration.py",
          "count": 1
        },
        {
          "label": "actual complete endpoint whole source",
          "old": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
          "new": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
          "count": 1
        },
        {
          "label": "actual complete endpoint basename",
          "old": "fixed_fejer_paired_halfwave_normal_lift.py",
          "new": "fixed_fejer_r725_normal_lift.py",
          "count": 1
        },
        {
          "label": "actual complete analytic_frame whole source",
          "old": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
          "new": "90d83320c35db9e7b11ea0cc1abc3595c85d282e73d520b36d74b3b2bc5665f0",
          "count": 1
        },
        {
          "label": "actual complete analytic_frame basename",
          "old": "fixed_fejer_paired_halfwave_analytic_normal_frame.py",
          "new": "fixed_fejer_r725_analytic_normal_frame.py",
          "count": 1
        },
        {
          "label": "actual complete closure_values whole source",
          "old": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "new": "07a24907be75352c158eb5a19a10682607f425a434d99d2eaafa688359296bb6",
          "count": 1
        },
        {
          "label": "actual complete closure_values basename",
          "old": "fixed_fejer_paired_halfwave_closure_values.py",
          "new": "fixed_fejer_r725_closure_values.py",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values whole source",
          "old": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
          "new": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values basename",
          "old": "fixed_fejer_paired_halfwave_detached_meridian_values.py",
          "new": "fixed_fejer_r725_detached_meridian_values.py",
          "count": 1
        },
        {
          "label": "actual complete root_packets whole source",
          "old": "8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a",
          "new": "71f80c72819f70d62ce2be70e075aa0ebda4130db3ebf7de7616d8a173ffeea1",
          "count": 1
        },
        {
          "label": "actual complete root_packets basename",
          "old": "fixed_fejer_paired_halfwave_root_packets.py",
          "new": "fixed_fejer_r725_root_packets.py",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3_binding whole source",
          "old": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
          "new": "bac157aba56f246d1c28510c5b54b8380438be4e133ade535e5096bd3ea1f488",
          "count": 1
        },
        {
          "label": "actual complete analytic_J3_binding basename",
          "old": "fixed_fejer_paired_halfwave_source_binding.py",
          "new": "fixed_fejer_r725_source_binding.py",
          "count": 1
        },
        {
          "label": "actual complete geometry whole source",
          "old": "da9b1be0146e48aad117124b7fc84c1754ecb0a78d5adeaa683710c5f7a8b316",
          "new": "a609fd96e1b19f14c9050a03a93967b70bbcf38747457f604496154edd364ced",
          "count": 1
        },
        {
          "label": "actual complete geometry basename",
          "old": "so3_fixed_fejer_halfwave_dk_cache_geometry.py",
          "new": "so3_fixed_fejer_r725_dk_cache_geometry.py",
          "count": 1
        },
        {
          "label": "actual complete envelope_transfer whole source",
          "old": "64a7c4380bb7150cf6738dc3102c7a33bf87dd32ed093f606a1d9b0d369a6bef",
          "new": "d9615e37f3fd0da916147674ff8f47be69cb6876ba98aa71e78eccd4d2fcc637",
          "count": 1
        },
        {
          "label": "actual complete envelope_transfer basename",
          "old": "fixed_fejer_halfwave_memory_transfer.py",
          "new": "fixed_fejer_r725_memory_transfer.py",
          "count": 1
        },
        {
          "label": "actual complete batched_geometry_binding whole source",
          "old": "ca2a7884039df93f7b5b243d476c60d2e8e810bf1071545a84bbc283a460aaad",
          "new": "d951f9e5f8088fdbd58357e29bca71f8057e5133693112657c288f57346c2819",
          "count": 1
        },
        {
          "label": "actual complete batched_geometry_binding basename",
          "old": "fixed_fejer_halfwave_dk_cache_binding.py",
          "new": "fixed_fejer_r725_dk_cache_binding.py",
          "count": 1
        },
        {
          "label": "actual complete geometry_selector whole source",
          "old": "f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112",
          "new": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
          "count": 1
        },
        {
          "label": "actual complete geometry_selector basename",
          "old": "fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
          "new": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
          "count": 1
        },
        {
          "label": "actual complete meridian whole source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        },
        {
          "label": "actual complete meridian basename",
          "old": "fixed_fejer_paired_halfwave_meridian_operator.py",
          "new": "fixed_fejer_r725_meridian_operator.py",
          "count": 1
        },
        {
          "label": "actual complete new_moment_input whole source",
          "old": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
          "new": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
          "count": 1
        },
        {
          "label": "actual complete new_moment_input basename",
          "old": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
          "new": "fixed_fejer_r725_literal_zero_moment_input.py",
          "count": 1
        },
        {
          "label": "actual complete seed_reference whole source",
          "old": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "new": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
          "count": 1
        },
        {
          "label": "actual complete seed_reference basename",
          "old": "fixed_fejer_paired_halfwave_meridian_reference.py",
          "new": "fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py",
          "count": 1
        }
      ]
    },
    {
      "role": "launcher",
      "parent": {
        "role": "launcher",
        "name": "launch_fixed_fejer_halfwave_dk_cache_actions.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_halfwave_dk_cache_actions.py",
        "bytes": 22125,
        "sha256": "804bb61c3d26f4116dc486feb735afd73eb733a85399a7908525e40187ca2ffe",
        "git_blob_sha": "38498ca8650584030c38386d4efab9d17cdb404d"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_r725_dk_cache_actions.py",
        "name": "launch_fixed_fejer_r725_dk_cache_actions.py",
        "bytes": 22121,
        "sha256": "0673232700619911d4ab3c8fbe36c579bb52dc19f4e4e27eb84aa8e7ff7ff734",
        "git_blob_sha": "5a4659259ea70a1e6b871336087e6cc3b5d6becd"
      },
      "patches": [
        {
          "label": "actual complete driver whole source",
          "old": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910",
          "new": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
          "count": 1
        },
        {
          "label": "actual complete driver basename",
          "old": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
          "new": "fullclosed_fixed_fejer_r725_dk_cache_qp.py",
          "count": 1
        }
      ]
    },
    {
      "role": "reader",
      "parent": {
        "role": "reader",
        "name": "read_fixed_fejer_halfwave_dk_cache_report.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_halfwave_dk_cache_report.py",
        "bytes": 99812,
        "sha256": "82a5c50f3006090398a054a1db12a607169bb1b074c25a00fae15ce447b704da",
        "git_blob_sha": "141407cc50df2d2043313fb168f779b0c018fc31"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_r725_dk_cache_report.py",
        "name": "read_fixed_fejer_r725_dk_cache_report.py",
        "bytes": 92783,
        "sha256": "3f7c9861e8a6a836dd0e2021489212e10ca217b2f1238abd36a07a002f8fb2af",
        "git_blob_sha": "1e56ac07a3a7b71676186b220e96d1bd696e6071"
      },
      "patches": [
        {
          "label": "actual R725 normal schema",
          "old": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "new": "complete-fixed-fejer-r725-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "label": "actual R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "actual R725 seed schema",
          "old": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
          "new": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
          "count": 1
        },
        {
          "label": "actual R725 input schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
          "new": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
          "count": 1
        },
        {
          "label": "actual R725 input_definition schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1",
          "new": "fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
          "count": 1
        },
        {
          "label": "actual R725 report schema",
          "old": "complete-fixed-fejer-paired-halfwave-dk-cache-SO3-QP-v1",
          "new": "complete-fixed-fejer-r725-dk-cache-SO3-QP-v1",
          "count": 1
        },
        {
          "label": "actual complete driver whole source",
          "old": "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910",
          "new": "e1d3b06875496ba2555d20e2e1e96bfa92c420c15dc7276788160b44fca337cd",
          "count": 1
        },
        {
          "label": "actual complete driver basename",
          "old": "fullclosed_fixed_fejer_halfwave_dk_cache_qp.py",
          "new": "fullclosed_fixed_fejer_r725_dk_cache_qp.py",
          "count": 1
        },
        {
          "label": "actual complete new_moment_input basename",
          "old": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
          "new": "fixed_fejer_r725_literal_zero_moment_input.py",
          "count": 1
        },
        {
          "label": "actual independent R725 pure readout schema",
          "old": "actual-fixed-fejer-halfwave-dk-cache-observed-SO3-readout-v1",
          "new": "actual-fixed-fejer-r725-dk-cache-observed-SO3-readout-v1",
          "count": 1
        },
        {
          "label": "delegate the full preserved seed metadata reader to the exact actual pure source",
          "old": "def supported_seed_metadata(value, model, roles, supported):\n    \"\"\"Read actual frozen-reference work; do not promote it to current normal roots.\"\"\"\n    base = value['base_complete_metadata']\n    seed = supported['definition']\n    identity = supported['identity_sha256']\n    actual = base.get('fixed_supported_unit_seed')\n    if (not isinstance(actual, dict)\n            or base.get('fixed_supported_unit_seed_identity_sha256') != identity\n            or base.get('axisymmetric_reference_binding') != supported['binding']\n            or base.get('seed_mean_Jacobian_not_a_certificate_for_current_closure_control_Jacobian') is not True\n            or actual.get('schema') != seed['schema']\n            or actual.get('source_sha256') != roles['seed_reference']\n            or actual.get('model') != seed\n            or actual.get('model_identity_sha256') != identity\n            or actual.get('binding') != supported['binding']\n            or actual.get('working_definition') != seed['working_definition']):\n        raise ValueError('The actual provider metadata belongs to another frozen supported seed')\n    for name in ('exact_seed_global_existence_hypotheses_certified',\n                 'seed_physical_field_or_normal_control_rank_inherited',\n                 'continuous_metric_geometry_or_full_phase_certificate'):\n        if actual.get(name) is not False:\n            raise ValueError('A working seed evaluation is not its accurate continuous certificate: '+name)\n    plan = actual.get('radial_plan')\n    if plan is not None:\n        if (plan.get('schema') != 'complete-paired-halfwave-seed-radial-plan-v1'\n                or plan.get('source_sha256') != roles['seed_reference']\n                or plan.get('paired_halfwave_definition') != seed['paired_halfwave_definition']\n                or plan.get('every_physical_halfwave_breakpoint_in_complete_partition') is not True\n                or plan.get('complete_physical_pair_piece_count') != 12\n                or plan.get('auxiliary_mean_rule_piece_count') != 12\n                or plan.get('physical_sine_cancellation_scope') != 'both equal complete central intervals together'\n                or plan.get('seed_model_identity_sha256') != identity\n                or plan.get('complete_domain') is not True\n                or plan.get('complete_infinite_scalar_tail_in_complement') is not True\n                or plan.get('no_scalar_tail_or_radial_piece_dropped') is not True\n                or plan.get('central_profile_integral_is_separate') is not True\n                or plan.get('numerical_integral_error_enclosed') is not False\n                or plan.get('scalar_errors_are_not_normalization_or_integration_errors') is not True):\n            raise ValueError('The actual seed radial plan must retain all pieces and its unpaid numerical fees')\n    batches = actual['mean_batch_records']\n    if not isinstance(batches, list):\n        raise ValueError('Keep every actual completed seed-mean batch record')\n    completed = []\n    for batch in batches:\n        metadata = batch['metadata']\n        angles = batch['literal_angle_hex']\n        if (batch.get('seed_model_identity_sha256') != identity\n                or batch.get('fixed_original_core_H_used') is not True\n                or batch.get('current_outer_free_point_not_used') is not True\n                or metadata.get('schema') != 'complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1'\n                or metadata.get('source_sha256') != roles['seed_mean']\n                or metadata.get('complete') is not True\n                or metadata.get('actual_successful_angle_count') != len(angles)):\n            raise ValueError('A completed seed batch must keep its actual angle count, original point and whole kernel source')\n        for word in angles:\n            if not isinstance(word, str):\n                raise ValueError('The fixed seed cache uses exact literal binary64 angle words')\n            angle = float.fromhex(word)\n            if not math.isfinite(angle) or angle.hex() != word:\n                raise ValueError('A recorded fixed-seed angle word is not canonical and finite')\n        for name in ('mean_root_complete','central_amplitude_root_complete',\n                     'all_three_mean_components_used','all_twelve_profile_pieces_used',\n                     'all_input_angles_retained','reference_angle_jets_only'):\n            if metadata.get(name) is not True:\n                raise ValueError('A partial mean or angular jet is not a complete seed batch: '+name)\n        for name in ('continuous_contraction_verified','exact_root_or_angle_jet_errors_enclosed',\n                     'quadrature_and_floating_errors_enclosed','geometry_certificate',\n                     'metric_certificate','current_free_parameter_J_claimed',\n                     'accurate_global_branch_association_verified'):\n            if metadata.get(name) is not False:\n                raise ValueError('Keep the actual seed-mean result within its numerical scope: '+name)\n        completed.extend(angles)\n    if len(completed) != len(set(completed)):\n        raise ValueError('A completed fixed-reference batch cannot repeat a previously recorded literal angle')\n    # The actual provider stores arrays and increments counters before writing\n    # its runner files and appending a complete batch record. A real interrupted\n    # cache write may therefore leave fewer complete records than cached values.\n    # Keep those actual scopes separate, including in an initial-failure report.\n    completed_cache = actual['completed_literal_angle_count']\n    completed_counter = actual['counts']['completed_mean_angles']\n    for number in (completed_cache, completed_counter):\n        if isinstance(number, bool) or not isinstance(number, int) or number < 0:\n            raise ValueError('Keep actual nonnegative integer seed cache/count readouts')\n    accounting_matches = completed_cache == completed_counter == len(completed)\n    failure = actual.get('last_failure')\n    if failure is not None and (failure.get('schema') != seed['schema']\n            or failure.get('source_sha256') != roles['seed_reference']\n            or failure.get('seed_model_identity_sha256') != identity\n            or failure.get('fixed_scalar_metric_identity_sha256') != model['fixed_scalar_metric_identity_sha256']\n            or failure.get('complete') is not False\n            or failure.get('continuous_certificate') is not False):\n        raise ValueError('The recorded seed failure belongs to another source, fixed input or scientific scope')\n    return dict(schema='actual-fixed-supported-smooth-triangle-reference-working-readout-v1',\n        source_sha256=roles['seed_reference'], mean_kernel_source_sha256=roles['seed_mean'],\n        fixed_supported_unit_seed_identity_sha256=identity,\n        actual_counts=actual['counts'],\n        completed_literal_angle_count=completed_cache, mean_successful_batch_count=len(batches),\n        complete_batch_recorded_angle_count=len(completed),\n        complete_batch_records_match_cached_angle_count=accounting_matches,\n        completed_batch_literal_angle_hex=completed,\n        complete_radial_plan_available=plan is not None, radial_plan=plan,\n        mean_batch_records=batches,\n        last_recorded_seed_failure=failure,\n        last_seed_failure_phase=None if failure is None else failure['failure_phase'],\n        last_seed_failure_reason=None if failure is None else failure['reason'],\n        maximum_original_scalar_carrier_errors=actual['maximum_original_scalar_carrier_errors'],\n        frozen_reference_cache_is_not_current_normal_root_availability=True,\n        seed_mean_inverse_is_not_normal_control_inverse_certificate=True,\n        fixed_seed_changed_the_original_scalar_target=False,\n        exact_seed_global_existence_hypotheses_certified=False,\n        seed_root_or_angle_jet_error_enclosed=False,\n        seed_quadrature_or_normalization_error_enclosed=False,\n        seed_continuous_metric_or_geometry_certified=False)\n\n",
          "new": "def supported_seed_metadata(value, model, roles, supported):\n    \"\"\"The complete original pure reader, with actual R725 radial-plan binding.\"\"\"\n    path = Path(__file__).with_name('fixed_fejer_r725_source_binding.py')\n    expected = roles['analytic_J3_binding']\n    if sha(path) != expected:\n        raise ValueError('Bind the complete source of the R725 seed metadata reader')\n    key = '_complete_r725_seed_reader_'+expected\n    module = sys.modules.get(key)\n    if module is None:\n        spec = importlib.util.spec_from_file_location(key, path)\n        module = importlib.util.module_from_spec(spec)\n        sys.modules[key] = module\n        spec.loader.exec_module(module)\n    method = module.supported_seed_metadata\n    if sha(method.__code__.co_filename) != expected:\n        raise ValueError('The complete R725 seed metadata method changed')\n    result = method(value, model, roles, supported)\n    if sha(path) != expected:\n        raise ValueError('The complete source changed during R725 seed metadata attribution')\n    return result\n\n",
          "count": 1
        }
      ]
    },
    {
      "role": "geometry_selector",
      "parent": {
        "role": "geometry_selector",
        "name": "fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities_v2_paired_halfwave_curvature_cache.py",
        "bytes": 35982,
        "sha256": "f2f1b9d7ba8661e67ab78f4d94e9c9d319f41f6ab06043b94ca14e8a7d026112",
        "git_blob_sha": "a8c04e0044ae95d1debd4d96dcd753430f0fd797"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities_v2_r725_curvature_cache.py",
        "name": "fullclosed_point_inequalities_v2_r725_curvature_cache.py",
        "bytes": 35982,
        "sha256": "c378e098013b6d15fc51fe6cafda0415dfaecc331a81d7655c94ef97a11e294b",
        "git_blob_sha": "3df348d7a1b9c7a2926886c6dc6fc7cd4f49b4f7"
      },
      "patches": [
        {
          "label": "actual complete endpoint whole source",
          "old": "c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac",
          "new": "c3c07e96a77fff78e4b56b1dd4d70d0e9461faeb1f8f14f65a5945c5a9d0ba4b",
          "count": 1
        },
        {
          "label": "actual complete detached_meridian_values whole source",
          "old": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
          "new": "ef1f691314f7e4ae40dd0bf64043959cc5b535a48ae0afde130b1aee06af33d8",
          "count": 1
        }
      ]
    },
    {
      "role": "meridian",
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_operator.py",
        "name": "fixed_fejer_paired_halfwave_meridian_operator.py",
        "bytes": 40803,
        "sha256": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
        "git_blob_sha": "350c2e057e6af15e663d0fdb463a518bebc36234"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_meridian_operator.py",
        "name": "fixed_fejer_r725_meridian_operator.py",
        "bytes": 40826,
        "sha256": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
        "git_blob_sha": "e6fae2e1729f5c9c325400a5d5261994a71ab961"
      },
      "patches": [
        {
          "label": "actual R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "actual complete R725 seed source",
          "old": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "new": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
          "count": 1
        },
        {
          "label": "actual R725 seed schema",
          "old": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
          "new": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
          "count": 1
        },
        {
          "label": "complete physical T0 description",
          "old": "T0='complete fixed paired-halfwave seed from original reference core/H; full complement, normalized boundary layers and equal opposite six-piece central halfwaves'",
          "new": "T0='complete fixed R725 paired-halfwave seed from original reference core/H; full complement, epsilon=1/8 three-piece C3 boundary cutoffs and equal opposite six-piece central halfwaves'",
          "count": 1
        }
      ]
    },
    {
      "role": "new_moment_input",
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "name": "fixed_fejer_paired_halfwave_literal_zero_moment_input.py",
        "bytes": 34886,
        "sha256": "53c71b2cf11aa9356f6edeb6f14098d8bef8e193841bd9513b00ee3f3fa86333",
        "git_blob_sha": "4625d2775b960a8859ddd88de215cc736a84363f"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r725_literal_zero_moment_input.py",
        "name": "fixed_fejer_r725_literal_zero_moment_input.py",
        "bytes": 40077,
        "sha256": "f14fac60e7a5eb576f81bd55dcfcec006f02e6c03efe9b66ba65af1c6dea84a6",
        "git_blob_sha": "59c7ee5abe717226db17284b07c347d38d419a65"
      },
      "patches": [
        {
          "label": "R725 input schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1",
          "new": "fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1",
          "count": 1
        },
        {
          "label": "R725 input_definition schema",
          "old": "fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1",
          "new": "fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1",
          "count": 1
        },
        {
          "label": "R725 base schema",
          "old": "complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1",
          "new": "complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1",
          "count": 1
        },
        {
          "label": "R725 seed schema",
          "old": "complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1",
          "new": "complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1",
          "count": 1
        },
        {
          "label": "R725 working schema",
          "old": "paired-halfwave-reference-working-definition-v1",
          "new": "paired-halfwave-flat-cutoff-reference-working-definition-v1",
          "count": 1
        },
        {
          "label": "actual R725 meridian whole source",
          "old": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "new": "b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792",
          "count": 1
        },
        {
          "label": "actual R725 seed_reference whole source",
          "old": "cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0",
          "new": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
          "count": 1
        },
        {
          "label": "pure exact R725 definition producer",
          "old": "\ndef _supported_seed(",
          "new": "\nBOUNDARY_CUTOFF_EPSILON = \"1/8\"\nBOUNDARY_CUTOFF_SCHEMA = \"complete-fixed-width-three-piece-C3-boundary-cutoff-v1\"\n\n\ndef _flat_cutoff_polynomial_jets(t, epsilon):\n    \"\"\"Exact arithmetic for Fraction inputs; working arithmetic for float inputs.\"\"\"\n    zero, one = t*0, t*0+1\n    if t <= zero:\n        return zero, zero, zero, zero\n    if t >= one:\n        return one, zero, zero, zero\n    denominator = one-epsilon\n    if epsilon <= t <= one-epsilon:\n        return (t-epsilon/2)/denominator, one/denominator, zero, zero\n    reflected = t > one-epsilon\n    u = (one-t)/epsilon if reflected else t/epsilon\n    G = (u*u*u*u)*(5+u*(-6+2*u))/2\n    S = u*u*u*(10+u*(-15+6*u))\n    S1 = 30*u*u*(one-u)*(one-u)\n    S2 = 60*u*(one-u)*(one-2*u)\n    value = epsilon*G/denominator\n    first = S/denominator\n    second = S1/(epsilon*denominator)\n    third = S2/(epsilon*epsilon*denominator)\n    if reflected:\n        return one-value, first, -second, third\n    return value, first, second, third\n\n\ndef _boundary_cutoff_exact_jets(t):\n    \"\"\"R725 value and first three normalized-coordinate derivatives, all exact.\"\"\"\n    if not isinstance(t, (str, Fraction)):\n        raise ValueError(\"Use an exact Fraction boundary cutoff coordinate\")\n    t = Fraction(t)\n    return _flat_cutoff_polynomial_jets(t, Fraction(BOUNDARY_CUTOFF_EPSILON))\n\n\ndef _boundary_cutoff_definition(support, central):\n    \"\"\"Complete fixed-rational three-piece law and every exact physical cut.\"\"\"\n    epsilon = Fraction(BOUNDARY_CUTOFF_EPSILON)\n    support = tuple(tuple(Fraction(v) for v in pair) for pair in support)\n    central = tuple(tuple(Fraction(v) for v in pair) for pair in central)\n    if (epsilon != Fraction(1,8) or len(support) != 2 or len(central) != 2\n            or any(len(pair) != 2 for pair in support+central)):\n        raise ValueError(\"This source fixes the complete R725 cutoff at epsilon=1/8\")\n    edges = (Fraction(0), epsilon, Fraction(1)-epsilon, Fraction(1))\n    layers = []\n    for index, ((left, right), (ca, cb)) in enumerate(zip(support, central)):\n        if not left < ca < cb < right:\n            raise ValueError(\"Every complete original boundary and central interval is required\")\n        for side, a, b, orientation in ((\"left\", left, ca, 1), (\"right\", cb, right, -1)):\n            physical = tuple(a+(b-a)*v for v in edges)\n            layers.append(dict(support_index=index, side=side,\n                exact_relative_interval=[str(a),str(b)],\n                exact_relative_piece_edges=[str(v) for v in physical],\n                exact_relative_internal_cuts=[str(v) for v in physical[1:-1]],\n                original_interval_normalized_piece_edges=[str(v) for v in edges],\n                cutoff_coordinate=\"t\" if orientation == 1 else \"1-t\",\n                odd_material_derivative_orientation=orientation,\n                physical_piece_count=3,\n                branches_in_increasing_material_order=(\n                    [\"left-polynomial\",\"affine\",\"right-reflection\"] if orientation == 1 else\n                    [\"right-reflection\",\"affine\",\"left-polynomial\"])))\n    return dict(schema=BOUNDARY_CUTOFF_SCHEMA, proof_result=\"R725\",\n        exact_epsilon=str(epsilon), epsilon_is_a_fixed_source_parameter=True,\n        epsilon_depends_on_angle_mean_direction_or_outer_point=False,\n        accurate_law=\"C=epsilon*G(t/epsilon)/(1-epsilon); (t-epsilon/2)/(1-epsilon); 1-epsilon*G((1-t)/epsilon)/(1-epsilon)\",\n        exact_G_ascending_coefficients=[\"0\",\"0\",\"0\",\"0\",\"5/2\",\"-3\",\"1\"],\n        exact_velocity_S5_ascending_coefficients=[\"0\",\"0\",\"0\",\"10\",\"-15\",\"6\"],\n        exact_normalized_piece_edges=[str(v) for v in edges],\n        constant_extension_outside_unit_interval=True,\n        piecewise_polynomial_degree=[6,1,6],\n        matching_material_derivative_order=3,\n        fourth_material_derivative_continuity_claimed=False,\n        exact_cut_values_and_first_three_normalized_jets=[\n            [str(v) for v in _boundary_cutoff_exact_jets(t)] for t in edges],\n        exact_first_derivative_peak=str(Fraction(1)/(1-epsilon)),\n        exact_derivative_integral=\"1\", exact_value_integral=\"1/2\",\n        four_boundary_layers=layers, complete_physical_boundary_piece_count=12,\n        complete_new_internal_boundary_cut_count=8,\n        original_central_halfwave_profile_changed=False,\n        original_bubble_gamma_and_raw_defect_lift_changed=False,\n        working_arithmetic=\"binary64 evaluation of this complete exact-rational law\",\n        working_rounding_or_integration_error_enclosed=False)\n\n\ndef _supported_seed(",
          "count": 1
        },
        {
          "label": "full exact R725 boundary definition binding",
          "old": "    working = seed.get('working_definition')",
          "new": "    cutoff = _boundary_cutoff_definition(support, central)\n    if (seed.get('exact_boundary_cutoff_epsilon') != BOUNDARY_CUTOFF_EPSILON\n            or seed.get('boundary_cutoff_definition') != cutoff):\n        raise ValueError('Bind the full R725 law, all four boundary layers, all eight internal cuts and exact endpoint jets')\n    working = seed.get('working_definition')",
          "count": 1
        },
        {
          "label": "complete working cutoff identity and noninheritance",
          "old": "            or working.get('physical_central_profile_definition') != paired",
          "new": "            or working.get('physical_central_profile_definition') != paired\n            or working.get('physical_boundary_cutoff_definition') != cutoff\n            or working.get('exact_boundary_cutoff_epsilon') != BOUNDARY_CUTOFF_EPSILON\n            or working.get('old_boundary_quadrature_mean_root_or_cache_inherited') is not False\n            or working.get('original_outer_whole_cell_Gauss_and_partial_rule_is_separate') is not True",
          "count": 1
        },
        {
          "label": "accurate independent Q binder description",
          "old": "Bind eighteen fixed Q words to one complete paired-halfwave reference seed.",
          "new": "Bind eighteen fixed Q words to one complete R725 paired-halfwave reference seed.",
          "count": 1
        }
      ]
    }
  ],
  "whole_shared_current_files": [
    {
      "role": "scalar_progress",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_location_progress.py",
      "name": "fixed_fejer_complete_geometry_location_progress.py",
      "bytes": 42637,
      "sha256": "4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94",
      "git_blob_sha": "bad0be021443e7fa7a8fbfe4ee473f3e05ccadad"
    },
    {
      "role": "seed_reference",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py",
      "name": "fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py",
      "bytes": 51540,
      "sha256": "1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f",
      "git_blob_sha": "b37f930874dd9b874d58120a2d9fe86031146ccb"
    }
  ]
};

function sha(raw) { return crypto.createHash("sha256").update(raw).digest("hex"); }
function readBound(root, record) {
  const location = path.resolve(root, record.path);
  if (!location.startsWith(root+path.sep)) throw Error("A declared source must stay inside the complete source root");
  const raw = fs.readFileSync(location);
  if (raw.length >= 100000 || raw.length !== record.bytes || sha(raw) !== record.sha256)
    throw Error("Complete original source identity differs: "+record.path);
  const text = raw.toString("utf8");
  if (!Buffer.from(text, "utf8").equals(raw)) throw Error("Use exact complete UTF-8 source bytes");
  return {location, raw, text, record};
}
function replaceExact(text, before, after, count, scope) {
  if (!before || text.split(before).length-1 !== count) throw Error("Exact complete patch count differs: "+scope);
  return text.split(before).join(after);
}
function writeComplete(root, record, raw) {
  const location = path.resolve(root, record.path);
  if (!location.startsWith(root+path.sep)) throw Error("Output must stay inside its separate output root");
  fs.mkdirSync(path.dirname(location), {recursive:true});
  if (fs.existsSync(location)) {
    if (!fs.readFileSync(location).equals(raw)) throw Error("Do not overwrite different existing complete output: "+location);
  } else fs.writeFileSync(location, raw, {flag:"wx"});
  if (!fs.readFileSync(location).equals(raw)) throw Error("Generated output bytes changed");
  return {role:record.role, path:location, bytes:raw.length, sha256:sha(raw)};
}
const args = process.argv.slice(2);
if (args.length !== 4 || args[0] !== "--source-root" || args[2] !== "--output-directory")
  throw Error("Usage: node reproduce_fixed_fejer_r725_sources.mjs --source-root <complete repository> --output-directory <separate generated tree>");
const sourceRoot = path.resolve(args[1]), outputRoot = path.resolve(args[3]);
if (sourceRoot === outputRoot) throw Error("Use a separate complete generated source tree");
const originals = DATA.complete_outputs.map(spec => readBound(sourceRoot, spec.parent));
const shared = DATA.whole_shared_current_files.map(record => readBound(sourceRoot, record));
const parentBinding = readBound(sourceRoot, DATA.parent_runtime_binding);
const outputs = [];
for (let i=0; i<DATA.complete_outputs.length; ++i) {
  const spec=DATA.complete_outputs[i], parent=originals[i];
  let text=parent.text;
  for (const patch of spec.patches)
    text=replaceExact(text, patch.old, patch.new, patch.count, spec.role+": "+patch.label);
  const raw=Buffer.from(text,"utf8");
  if (raw.length !== spec.output.bytes || raw.length >= 100000 || sha(raw) !== spec.output.sha256)
    throw Error("The complete generated body differs from the independently protected output: "+spec.role);
  let inverse=text;
  for (const patch of spec.patches.slice().reverse())
    inverse=replaceExact(inverse, patch.new, patch.old, patch.count, spec.role+": exact inverse "+patch.label);
  if (inverse !== parent.text || !Buffer.from(inverse,"utf8").equals(parent.raw))
    throw Error("The complete inverse does not recover its exact original parent: "+spec.role);
  outputs.push(writeComplete(outputRoot,{role:spec.role,...spec.output},raw));
}
for (const source of shared) outputs.push(writeComplete(outputRoot,source.record,source.raw));
for (const source of [...originals,...shared,parentBinding])
  if (!fs.readFileSync(source.location).equals(source.raw))
    throw Error("An original complete source changed during text construction: "+source.record.path);
const report={schema:DATA.schema, complete:true, source_text_construction_only:true,
  complete_generated_and_copied_sources:outputs, generated_source_count:DATA.complete_outputs.length,
  byte_identical_current_copy_count:shared.length,
  scientific_evaluation_executed:false, AST_compile_import_fixture_or_benchmark_executed:false,
  original_137_role_registry_and_historical_files_preserved_in_whole_parent:true};
console.log(JSON.stringify(report,null,2));
