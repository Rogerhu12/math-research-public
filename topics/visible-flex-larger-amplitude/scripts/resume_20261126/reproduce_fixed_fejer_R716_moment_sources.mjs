#!/usr/bin/env node
// Whole source reproduction. No scientific import, AST, or admission gate.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const PLAN = {
  "schema": "complete-fixed-fejer-R716-whole-source-derivation-v1",
  "jobs": [
    {
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_complete_closed_surface_moment_integrals.py",
        "name": "run10_complete_closed_surface_moment_integrals.py",
        "bytes": 57152,
        "sha256": "0aa16633df87d2700bba332cf2c6a225e746fbda87097b0004f18e3cde5b7504",
        "git_blob_sha": "2ab4b26305b0a9db4d440ce63a1da4ac853abb70"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_closed_surface_moment_integrals.py",
        "name": "fixed_fejer_complete_closed_surface_moment_integrals.py",
        "bytes": 60956,
        "sha256": "31a83a056424671eb893b1aae41c8c88b7153a5cabafd816449d64286b7976e5",
        "git_blob_sha": "c43f62a5ae6cce8f5476eb23b6c87619394f0464"
      },
      "changes": [
        {
          "label": "target family namespace",
          "old": "actual-run10",
          "new": "actual-fixed-fejer",
          "count": 7,
          "positions": [
            42,
            957,
            1030,
            1400,
            1479,
            1548,
            12258
          ],
          "before_sha256": "0aa16633df87d2700bba332cf2c6a225e746fbda87097b0004f18e3cde5b7504",
          "after_sha256": "9e8fb643e4463e9d58aaba57ea9e937d0aa72e40e422fc04c87bb2af4a373fec"
        },
        {
          "label": "normal source basename",
          "old": "run10_complete_normal_root_and_sixjet_fees.py",
          "new": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
          "count": 1,
          "positions": [
            1284
          ],
          "before_sha256": "9e8fb643e4463e9d58aaba57ea9e937d0aa72e40e422fc04c87bb2af4a373fec",
          "after_sha256": "06bcdccd81fa9c2d68c5d655d34c994bc994743952413e95a4bce528aef33c89"
        },
        {
          "label": "normal source identity",
          "old": "0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83",
          "new": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
          "count": 1,
          "positions": [
            1338
          ],
          "before_sha256": "06bcdccd81fa9c2d68c5d655d34c994bc994743952413e95a4bce528aef33c89",
          "after_sha256": "040528da2db954de5b2897cf0eebf796f608e12dec4aaea55ed08af7c4757b38"
        },
        {
          "label": "scientific driver identity",
          "old": "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
          "new": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd",
          "count": 1,
          "positions": [
            1654
          ],
          "before_sha256": "040528da2db954de5b2897cf0eebf796f608e12dec4aaea55ed08af7c4757b38",
          "after_sha256": "172ad3a6c778652eed4d061e7e809b0735646d80ce81f6edbdbca8282268129a"
        },
        {
          "label": "whole reader identity",
          "old": "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e",
          "new": "274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b",
          "count": 1,
          "positions": [
            1735
          ],
          "before_sha256": "172ad3a6c778652eed4d061e7e809b0735646d80ce81f6edbdbca8282268129a",
          "after_sha256": "028d98cbaa80434fd45dc969b55cfa56fc66528df10c8e0465813421dda694c3"
        },
        {
          "label": "normal model identity",
          "old": "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4",
          "new": "1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778",
          "count": 1,
          "positions": [
            1822
          ],
          "before_sha256": "028d98cbaa80434fd45dc969b55cfa56fc66528df10c8e0465813421dda694c3",
          "after_sha256": "bee67ccbf998757d58d3d2aaab52565bd95145e4b7239b02cc8ee06d4e1ffd71"
        },
        {
          "label": "base identity",
          "old": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
          "new": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "count": 1,
          "positions": [
            1982
          ],
          "before_sha256": "bee67ccbf998757d58d3d2aaab52565bd95145e4b7239b02cc8ee06d4e1ffd71",
          "after_sha256": "4b92a3cf2960f570ec77d214334506c123cdf7942f721f5c61c03465daf3375b"
        },
        {
          "label": "dynamic full target source contract",
          "old": "ACTUAL_TARGET=\"e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049\"",
          "new": "FIXED_INPUT_BINDING_SOURCE=(\"fixed_fejer_reference_input_binding.py\",\"3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f\")\nFIXED_ENTRY_BINDING_SOURCE=(\"fixed_fejer_complete_source_binding.py\",\"3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88\")",
          "count": 1,
          "positions": [
            1888
          ],
          "before_sha256": "4b92a3cf2960f570ec77d214334506c123cdf7942f721f5c61c03465daf3375b",
          "after_sha256": "b8d672ad41923e00076d02726f5580c97e330a4af76a77c2d02bfd3b0cba438d"
        },
        {
          "label": "accurate actual input basename",
          "old": "run10_normal_packet_accurate_field_input.py",
          "new": "fixed_fejer_normal_packet_accurate_field_input.py",
          "count": 1,
          "positions": [
            7665
          ],
          "before_sha256": "b8d672ad41923e00076d02726f5580c97e330a4af76a77c2d02bfd3b0cba438d",
          "after_sha256": "3f8b5160fe05c6b4befa7eb87257b1b58d98f2128b73ce9b92fb1defa564121f"
        },
        {
          "label": "accurate actual input identity",
          "old": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8",
          "new": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
          "count": 1,
          "positions": [
            7730
          ],
          "before_sha256": "3f8b5160fe05c6b4befa7eb87257b1b58d98f2128b73ce9b92fb1defa564121f",
          "after_sha256": "fbdaef9a2fc7755fdd9a2ec4ef2086109f7c479c9102113b1347463bea5d870c"
        },
        {
          "label": "accurate radial basename",
          "old": "run10_accurate_reference_control_radial_boxes.py",
          "new": "fixed_fejer_accurate_reference_control_radial_boxes.py",
          "count": 1,
          "positions": [
            7983
          ],
          "before_sha256": "fbdaef9a2fc7755fdd9a2ec4ef2086109f7c479c9102113b1347463bea5d870c",
          "after_sha256": "683ea18e8913efea0c310a01635ea63ab33b78ad300a5de9a7293f705e74b643"
        },
        {
          "label": "accurate radial identity",
          "old": "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c",
          "new": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
          "count": 1,
          "positions": [
            8053
          ],
          "before_sha256": "683ea18e8913efea0c310a01635ea63ab33b78ad300a5de9a7293f705e74b643",
          "after_sha256": "603eef84556ee12a9fa71548f8690db88b06c46c191b5652e3e7195758407709"
        },
        {
          "label": "current layout source label",
          "old": "6a803 literal unpack excludes exactly these complete rows",
          "new": "552f fixed-Fejer literal unpack excludes exactly these complete rows",
          "count": 1,
          "positions": [
            11336
          ],
          "before_sha256": "603eef84556ee12a9fa71548f8690db88b06c46c191b5652e3e7195758407709",
          "after_sha256": "dde48c5ed0aeeeb3620927ac92c81d3d61ab9d1926c4b21f4a12d0c87d80feb1"
        },
        {
          "label": "full actual reference reader",
          "old": "def bind_input(report_path,expected_sha,repo,files,k):",
          "new": "def verify_actual_fixed_reference(actual, outer, repo, files):\n    \"\"\"Read the whole predeclared target; never compare two unvalidated labels.\"\"\"\n    root=Path(repo).resolve()/TOPIC/\"scripts/resume_20261126\"\n    path=root/FIXED_ENTRY_BINDING_SOURCE[0]\n    for name,digest in (FIXED_ENTRY_BINDING_SOURCE,FIXED_INPUT_BINDING_SOURCE):\n        candidate=root/name\n        if sha(candidate)!=digest:\n            raise ValueError(\"The complete fixed-target binding source changed\")\n        files.add(candidate)\n    key=\"_moment_complete_fixed_fejer_entry_binding\"\n    spec=importlib.util.spec_from_file_location(key,path)\n    module=importlib.util.module_from_spec(spec)\n    sys.modules[key]=module\n    spec.loader.exec_module(module)\n    if (sha(module.__file__)!=FIXED_ENTRY_BINDING_SOURCE[1]\n            or sha(module.bind_fixed_fejer_input.__code__.co_filename)!=FIXED_ENTRY_BINDING_SOURCE[1]):\n        raise ValueError(\"The complete fixed-target entry method changed\")\n    entry=outer.get(\"actual_fixed_reference_input_binding\")\n    if (not isinstance(entry,dict)\n            or actual.get(\"complete_actual_fixed_reference_input_binding\")!=entry):\n        raise ValueError(\"Retain the full actual scientific input binding\")\n    record=entry[\"actual_binding_file\"]\n    files.verify(record)\n    current=module.bind_fixed_fejer_input(record[\"path\"],\n        current_files=actual[\"complete_six_actual_inputs\"])\n    if current!=entry:\n        raise ValueError(\"The complete current entry and all six input files changed\")\n    payload,_=files.read_json(record)\n    target=payload[\"fixed_target_definition\"]\n    reference=actual[\"complete_model\"][\"base_complete_model\"][\"complete_axisymmetric_reference_model\"]\n    if (reference!=target[\"complete_current_reference_model\"]\n            or canonical(reference)!=entry[\"actual_reference_model_identity_sha256\"]\n            or actual.get(\"actual_reference_model_identity_sha256\")!=entry[\"actual_reference_model_identity_sha256\"]\n            or actual.get(\"exact_fixed_target_identity_sha256\")!=entry[\"actual_fixed_target_definition_identity_sha256\"]\n            or actual.get(\"mathematical_target_identity_sha256\")!=entry[\"mathematical_target_identity_sha256\"]\n            or actual.get(\"fixed_chart_core_sha256\")!=entry[\"actual_fixed_chart_core_sha256\"]\n            or canonical(target)!=entry[\"actual_fixed_target_definition_identity_sha256\"]\n            or payload[\"current_files\"]!=actual[\"complete_six_actual_inputs\"]\n            or entry[\"complete_current_input_files\"]!=actual[\"complete_six_actual_inputs\"]):\n        raise ValueError(\"Bind the complete reference, pure recipe and working target separately\")\n    for value in payload[\"current_files\"].values():\n        files.verify(value)\n    for name in (\"fixed_input_preparation_report\",\"fixed_target_definition_file\",\n                 \"new_locations\",\"complete_supplied_location_provenance\"):\n        files.verify(payload[name])\n    files.verify(record,force=True)\n\n\ndef bind_input(report_path,expected_sha,repo,files,k):",
          "count": 1,
          "positions": [
            12079
          ],
          "before_sha256": "dde48c5ed0aeeeb3620927ac92c81d3d61ab9d1926c4b21f4a12d0c87d80feb1",
          "after_sha256": "4d4106155d764dd56e07db2d612bf6c561cab9b7219a5a2934ad89c615cfc34f"
        },
        {
          "label": "old fixed target predicate paid by whole reader",
          "old": "\n            or actual.get(\"exact_fixed_target_identity_sha256\")!=ACTUAL_TARGET",
          "new": "",
          "count": 1,
          "positions": [
            17509
          ],
          "before_sha256": "4d4106155d764dd56e07db2d612bf6c561cab9b7219a5a2934ad89c615cfc34f",
          "after_sha256": "92bb2508a524a65be8846d5f624cea1d1569bfc8d5aa1e233bf529d08ef67524"
        },
        {
          "label": "actually consume full fixed reference",
          "old": "        raise ValueError(\"The complete actual mathematical model differs from the scientific report\")\n",
          "new": "        raise ValueError(\"The complete actual mathematical model differs from the scientific report\")\n    verify_actual_fixed_reference(actual,outer,repo,files)\n",
          "count": 1,
          "positions": [
            18162
          ],
          "before_sha256": "92bb2508a524a65be8846d5f624cea1d1569bfc8d5aa1e233bf529d08ef67524",
          "after_sha256": "a6a1feabea6e76121e797f9600b1d6fe9a95223904be2715da346101dc498618"
        },
        {
          "label": "whole target in all generated records",
          "old": "exact_fixed_target_identity_sha256=ACTUAL_TARGET,",
          "new": "exact_fixed_target_identity_sha256=context[\"actual\"][\"exact_fixed_target_identity_sha256\"],\n        mathematical_target_identity_sha256=context[\"actual\"][\"mathematical_target_identity_sha256\"],",
          "count": 3,
          "positions": [
            44670,
            54385,
            56803
          ],
          "before_sha256": "a6a1feabea6e76121e797f9600b1d6fe9a95223904be2715da346101dc498618",
          "after_sha256": "298100519839daccea8b603a3e1dfe762ec77614036e339bfc694eec4246a400"
        },
        {
          "label": "whole target and mathematical identity in each reread block",
          "old": "value.get(\"exact_fixed_target_identity_sha256\")!=ACTUAL_TARGET",
          "new": "value.get(\"exact_fixed_target_identity_sha256\")!=context[\"actual\"][\"exact_fixed_target_identity_sha256\"]\n            or value.get(\"mathematical_target_identity_sha256\")!=context[\"actual\"][\"mathematical_target_identity_sha256\"]",
          "count": 1,
          "positions": [
            46198
          ],
          "before_sha256": "298100519839daccea8b603a3e1dfe762ec77614036e339bfc694eec4246a400",
          "after_sha256": "31a83a056424671eb893b1aae41c8c88b7153a5cabafd816449d64286b7976e5"
        }
      ]
    },
    {
      "parent": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_r716_centred_volume_moment.py",
        "name": "run10_r716_centred_volume_moment.py",
        "bytes": 46327,
        "sha256": "92065cdc580e6c7f4c2d8f0474b0449a8f19fc2ffa873222997e6be0f4140e97",
        "git_blob_sha": "34eabdd50d6c426911eb7789028055be4216d71d"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r716_centred_volume_moment.py",
        "name": "fixed_fejer_r716_centred_volume_moment.py",
        "bytes": 46705,
        "sha256": "7cde8b5e8ddda13a3e6df6d8fc2b833bd44886741fcc03aa9f69b5204a3eb3cd",
        "git_blob_sha": "995f370695d92e89d7f00ff75ffe0d97fcb91e71"
      },
      "changes": [
        {
          "label": "actual consumer namespace",
          "old": "actual-run10",
          "new": "actual-fixed-fejer",
          "count": 2,
          "positions": [
            989,
            1504
          ],
          "before_sha256": "92065cdc580e6c7f4c2d8f0474b0449a8f19fc2ffa873222997e6be0f4140e97",
          "after_sha256": "a7389ee0f4612a2b9c45eaec0728643f3bc9493d4a76cb1a7bbe27c83cb6a298"
        },
        {
          "label": "complete flux source name",
          "old": "run10_complete_closed_surface_moment_integrals.py",
          "new": "fixed_fejer_complete_closed_surface_moment_integrals.py",
          "count": 1,
          "positions": [
            1113
          ],
          "before_sha256": "a7389ee0f4612a2b9c45eaec0728643f3bc9493d4a76cb1a7bbe27c83cb6a298",
          "after_sha256": "aa5de698b140c5e71c8eb6f8009364206c072bb07b2c8f1a5d789d5bc42786c6"
        },
        {
          "label": "complete flux source identity",
          "old": "0aa16633df87d2700bba332cf2c6a225e746fbda87097b0004f18e3cde5b7504",
          "new": "31a83a056424671eb893b1aae41c8c88b7153a5cabafd816449d64286b7976e5",
          "count": 1,
          "positions": [
            1171
          ],
          "before_sha256": "aa5de698b140c5e71c8eb6f8009364206c072bb07b2c8f1a5d789d5bc42786c6",
          "after_sha256": "acc032072705ef48d221282133bb389920b0cf1eb75b728bd6c3c8bb7a9072d9"
        },
        {
          "label": "complete closed source name",
          "old": "run10_complete_closed_phase_grip_evidence.py",
          "new": "fixed_fejer_complete_closed_phase_grip_evidence.py",
          "count": 1,
          "positions": [
            1376
          ],
          "before_sha256": "acc032072705ef48d221282133bb389920b0cf1eb75b728bd6c3c8bb7a9072d9",
          "after_sha256": "86ad5c6a60edb1ee74b7ffcb2d9413670e1cd86bfd1a49505b0decdcc41d5680"
        },
        {
          "label": "complete closed source identity",
          "old": "f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be",
          "new": "d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9",
          "count": 1,
          "positions": [
            1434
          ],
          "before_sha256": "86ad5c6a60edb1ee74b7ffcb2d9413670e1cd86bfd1a49505b0decdcc41d5680",
          "after_sha256": "d8f2d19d03516efe5470d58b0ac3780f37e63f0fe58b4345c1c26b91fa352fc2"
        },
        {
          "label": "complete bridge source name",
          "old": "run10_complete_geometry_support_beta_bridge.py",
          "new": "fixed_fejer_complete_geometry_support_beta_bridge.py",
          "count": 1,
          "positions": [
            1599
          ],
          "before_sha256": "d8f2d19d03516efe5470d58b0ac3780f37e63f0fe58b4345c1c26b91fa352fc2",
          "after_sha256": "50c8857a0aa56ae05ab924567b536fac2f842f998123c2fae3ada4996c5baf1f"
        },
        {
          "label": "complete bridge source identity",
          "old": "96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9",
          "new": "ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15",
          "count": 1,
          "positions": [
            1659
          ],
          "before_sha256": "50c8857a0aa56ae05ab924567b536fac2f842f998123c2fae3ada4996c5baf1f",
          "after_sha256": "cb1ae5648b4fcba5cab7bf6aeb1b34a0e7b33b285af4725a9fa9aa923c9c23be"
        },
        {
          "label": "complete geometry source name",
          "old": "run10_continuous_gram_curvature_support.py",
          "new": "fixed_fejer_continuous_gram_curvature_support.py",
          "count": 1,
          "positions": [
            1744
          ],
          "before_sha256": "cb1ae5648b4fcba5cab7bf6aeb1b34a0e7b33b285af4725a9fa9aa923c9c23be",
          "after_sha256": "068f78a6540ec1d662ae32410fbea71b53822e02a6f8a5cfc7245f98c58417ac"
        },
        {
          "label": "complete geometry source identity",
          "old": "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7",
          "new": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b",
          "count": 1,
          "positions": [
            1800
          ],
          "before_sha256": "068f78a6540ec1d662ae32410fbea71b53822e02a6f8a5cfc7245f98c58417ac",
          "after_sha256": "8e4721bdcb0e7ffd74da5536cfba4fde2872700a7bb6e68ec71b5bd2c9e74a22"
        },
        {
          "label": "independent import names",
          "old": "_run10_",
          "new": "_fixed_fejer_",
          "count": 5,
          "positions": [
            2576,
            12917,
            22751,
            22865,
            24317
          ],
          "before_sha256": "8e4721bdcb0e7ffd74da5536cfba4fde2872700a7bb6e68ec71b5bd2c9e74a22",
          "after_sha256": "2f1f378ac0f4569bcb6f9c0a7956846dec45cb9de78bbf61befa9816be6f8052"
        },
        {
          "label": "current producer error wording",
          "old": "bound run10 closed-phase producer",
          "new": "bound fixed-Fejer closed-phase producer",
          "count": 1,
          "positions": [
            12818
          ],
          "before_sha256": "2f1f378ac0f4569bcb6f9c0a7956846dec45cb9de78bbf61befa9816be6f8052",
          "after_sha256": "a9c0935d637f3b4eb5becd462a53851bb42280cfc3b0fd2e7b16eb650d86a320"
        },
        {
          "label": "actual full target and mathematical recipe in moment binding",
          "old": "binding.get(\"exact_fixed_target_identity_sha256\")!=p.ACTUAL_TARGET",
          "new": "binding.get(\"exact_fixed_target_identity_sha256\")!=context[\"actual\"][\"exact_fixed_target_identity_sha256\"]\n            or binding.get(\"mathematical_target_identity_sha256\")!=context[\"actual\"][\"mathematical_target_identity_sha256\"]",
          "count": 1,
          "positions": [
            5057
          ],
          "before_sha256": "a9c0935d637f3b4eb5becd462a53851bb42280cfc3b0fd2e7b16eb650d86a320",
          "after_sha256": "e9c70d015d631652e56da976e3e6c4b207156d13d960286a8c414bc1cc8c0216"
        },
        {
          "label": "current full source scope instead of old target constant",
          "old": "r.ACTUAL_TARGET!=p.ACTUAL_TARGET",
          "new": "r.ACTUAL_BASE!=p.ACTUAL_BASE",
          "count": 1,
          "positions": [
            23449
          ],
          "before_sha256": "e9c70d015d631652e56da976e3e6c4b207156d13d960286a8c414bc1cc8c0216",
          "after_sha256": "cc2e56f40a78f564fe4ac7494f92013d080f564e039f5f25d639071543bc7a3e"
        },
        {
          "label": "actual two target identities in final report",
          "old": "exact_fixed_target_identity_sha256=p.ACTUAL_TARGET,",
          "new": "exact_fixed_target_identity_sha256=context[\"actual\"][\"exact_fixed_target_identity_sha256\"],\n            mathematical_target_identity_sha256=context[\"actual\"][\"mathematical_target_identity_sha256\"],",
          "count": 1,
          "positions": [
            40342
          ],
          "before_sha256": "cc2e56f40a78f564fe4ac7494f92013d080f564e039f5f25d639071543bc7a3e",
          "after_sha256": "7cde8b5e8ddda13a3e6df6d8fc2b833bd44886741fcc03aa9f69b5204a3eb3cd"
        }
      ]
    }
  ],
  "dependencies": [
    {
      "role": "input",
      "name": "fixed_fejer_normal_packet_accurate_field_input.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_normal_packet_accurate_field_input.py",
      "bytes": 32991,
      "sha256": "1e5101d7bd08a8b3787b6eaa699c915a9e8bd173d365233c7be90f1aee1b3f3f",
      "git_blob_sha": "46ee6fd8157265253259a642844783ea4cd712bb"
    },
    {
      "role": "radial",
      "name": "fixed_fejer_accurate_reference_control_radial_boxes.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_accurate_reference_control_radial_boxes.py",
      "bytes": 45317,
      "sha256": "c52044c5b12000486dc0673f6ddf0a23935239348f5534f103d0f75fb9d585d4",
      "git_blob_sha": "e572b4f4de1ebc3468d173989105f813675cab1b"
    },
    {
      "role": "normal",
      "name": "fixed_fejer_complete_normal_root_and_sixjet_fees.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_normal_root_and_sixjet_fees.py",
      "bytes": 40294,
      "sha256": "1a915b058e7bd9c9edb7905f68d491c597c98b9d69521db97c7eadc2bf8bda35",
      "git_blob_sha": "2aa3dc44a8ba8d61ec6ffa4de90c3dd61b2d85c2"
    },
    {
      "role": "leaf",
      "name": "fixed_fejer_complete_physical_leaf_binding.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_physical_leaf_binding.py",
      "bytes": 47321,
      "sha256": "ee03b17d9c716ef24d76552cec1fc6031b7fa1eb037cf7cb55ddc9980b28721c",
      "git_blob_sha": "fbe38e6afce500e502ca9655dd784360f200f208"
    },
    {
      "role": "geometry",
      "name": "fixed_fejer_continuous_gram_curvature_support.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_continuous_gram_curvature_support.py",
      "bytes": 46689,
      "sha256": "fcae1e5926e8e70edbd78a9e3b276f46e3b7b345b1ad2d6ec647905e6c5a4d2b",
      "git_blob_sha": "368afa8be43c26eecdd13ef5466fe9de56b5afec"
    },
    {
      "role": "bridge",
      "name": "fixed_fejer_complete_geometry_support_beta_bridge.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_geometry_support_beta_bridge.py",
      "bytes": 20810,
      "sha256": "ff77dd925949bffaed4bffce8249554cfb0d56390da70bc3398cebe1f2202d15",
      "git_blob_sha": "3c6b9b259bb20231ca607192510f235315fb1f5e"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_closed_phase_grip_evidence.py",
      "name": "fixed_fejer_complete_closed_phase_grip_evidence.py",
      "bytes": 71420,
      "sha256": "d606055d1b247d8354ac320bc28a0f40f4b00cbf1ff530a9b6bb2e80dec80bb9",
      "git_blob_sha": "33d9ee5b22c3e8bb5a92262ca7af7b89f20bb78b"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md",
      "name": "2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md",
      "bytes": 15093,
      "sha256": "16c15c597359b3017c9e050b5ddef94950d508e88a9c05fa726300cd129b726e",
      "git_blob_sha": "234e60bc7bbf7f286c77ed4e6f78cdf1d935c79c"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_reference_input_binding.py",
      "name": "fixed_fejer_reference_input_binding.py",
      "bytes": 25672,
      "sha256": "3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f",
      "git_blob_sha": "5eab3f96cb8b1bc245f4de33dc2041cf25d22094"
    },
    {
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_complete_source_binding.py",
      "name": "fixed_fejer_complete_source_binding.py",
      "bytes": 32487,
      "sha256": "3b3f2322eb1d1f6304e71e4d972a8e45ba2b5dd6605501d293212de46b5c5c88",
      "git_blob_sha": "3073c9490a6bc6ce7dcf323f799ee8075f8bdd78"
    }
  ],
  "full_ready": {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-complete-R716-closed-flux-centred-moments-ready.json",
    "name": "fixed-fejer-complete-R716-closed-flux-centred-moments-ready.json",
    "bytes": 25754,
    "sha256": "e2952fa4326fecb2c2b5237d8c6f6bb91b728f032298537c17385f5f6ef078a2",
    "git_blob_sha": "fd42b80478ad16ceec1e61c31ba4fcb557fc4a31"
  },
  "source_reproduction_only": true,
  "scientific_execution": false
};

const args=process.argv.slice(2),opts={};
for(let i=0;i<args.length;i+=2){if(!["--repo","--outdir"].includes(args[i])||!args[i+1])throw Error("Use --repo REPOSITORY --outdir DIRECTORY");opts[args[i]]=args[i+1];}
if(!opts["--outdir"])throw Error("--outdir is required");
const root=path.resolve(opts["--repo"]||"."),outdir=path.resolve(opts["--outdir"]),hash=s=>crypto.createHash("sha256").update(s).digest("hex");
function read(record){const raw=fs.readFileSync(path.join(root,record.path));if(raw.length!==record.bytes||hash(raw)!==record.sha256)throw Error("Complete source differs: "+record.path);return raw.toString("utf8");}
for(const record of PLAN.dependencies)read(record);
const outputs=[];
for(const job of PLAN.jobs){
 const parent=read(job.parent);let body=parent;
 for(const q of job.changes){
  if(hash(body)!==q.before_sha256)throw Error("Complete preimage differs: "+q.label);
  const positions=[];for(let i=0;(i=body.indexOf(q.old,i))>=0;i+=q.old.length)positions.push(i);
  if(positions.length!==q.count||JSON.stringify(positions)!==JSON.stringify(q.positions))throw Error("Exact change differs: "+q.label);
  body=body.split(q.old).join(q.new);if(hash(body)!==q.after_sha256)throw Error("Complete postimage differs");
 }
 if(Buffer.byteLength(body)!==job.output.bytes||hash(body)!==job.output.sha256)throw Error("Complete output differs");
 let inverse=body;
 for(const q of [...job.changes].reverse()){
  let offset=0;const positions=q.positions.map(i=>{const j=i+offset;offset+=q.new.length-q.old.length;return j;});
  for(const i of positions.reverse()){if(inverse.slice(i,i+q.new.length)!==q.new)throw Error("Exact inverse span differs");inverse=inverse.slice(0,i)+q.old+inverse.slice(i+q.new.length);}
  if(hash(inverse)!==q.before_sha256)throw Error("Complete inverse differs");
 }
 if(inverse!==parent)throw Error("Original full parent not recovered");
 outputs.push([job.output,body]);
}
const ready=read(PLAN.full_ready);
fs.mkdirSync(outdir,{recursive:true});
for(const [record,body] of outputs)fs.writeFileSync(path.join(outdir,record.name),body,{flag:"wx"});
fs.writeFileSync(path.join(outdir,PLAN.full_ready.name),ready,{flag:"wx"});
process.stdout.write(JSON.stringify({complete_sources:outputs.map(x=>x[0]),complete_ready_copied_from_locked_package:PLAN.full_ready,scientific_execution:false})+"\n");
