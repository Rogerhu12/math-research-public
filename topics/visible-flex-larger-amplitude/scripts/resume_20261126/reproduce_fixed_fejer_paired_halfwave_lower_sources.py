#!/usr/bin/env python3
"""Reproduce nine whole paired-halfwave lower sources from complete fixed parents.

This program performs only UTF-8 source-byte operations. It does not import,
compile, parse or execute any scientific source, evaluate a field, or impose
a numerical admission step. Every complete output has its own final identity.
"""
import argparse
import hashlib
import json
from pathlib import Path

SPEC = json.loads(r'''{
  "schema": "complete-fixed-fejer-paired-halfwave-nine-lower-source-construction-v1",
  "sources": [
    {
      "role": "closure_values",
      "parent": {
        "name": "fixed_fejer_meridian_closure_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_closure_values.py",
        "bytes": 59440,
        "sha256": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
        "git_blob_sha": "2383f9c4bad43635e43fe409b048d3f74d2b9b8c"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_closure_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_closure_values.py",
        "bytes": 59449,
        "sha256": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
        "git_blob_sha": "5e7230ce5dc57adffe58901b04257c1469fa8e8c"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
          "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "count": 1
        }
      ]
    },
    {
      "role": "analytic_J3",
      "parent": {
        "name": "fixed_fejer_meridian_analytic_stage_jacobian.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_analytic_stage_jacobian.py",
        "bytes": 25697,
        "sha256": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
        "git_blob_sha": "7525e1f076c90b877d7574c8aea85dc12e02d973"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_analytic_stage_jacobian.py",
        "bytes": 25706,
        "sha256": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
        "git_blob_sha": "aaa1d6b48f02d62b5a7a445932304d3e36730fa3"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
          "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
          "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "count": 1
        }
      ]
    },
    {
      "role": "analytic_frame",
      "parent": {
        "name": "fixed_fejer_meridian_analytic_normal_frame.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_analytic_normal_frame.py",
        "bytes": 47431,
        "sha256": "d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd",
        "git_blob_sha": "9c24a81d34171155f6bb4e19592bfe54a2fb7b40"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_analytic_normal_frame.py",
        "bytes": 47440,
        "sha256": "5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e",
        "git_blob_sha": "263534a4e65f31b45cf1f9a40441f5896e213e2b"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
          "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
          "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "count": 1
        }
      ]
    },
    {
      "role": "frame_C1",
      "parent": {
        "name": "fixed_fejer_meridian_normal_frame_c1.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_normal_frame_c1.py",
        "bytes": 37361,
        "sha256": "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246",
        "git_blob_sha": "5daa46fca67d3e90985fed092c37ec4eefd20421"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_normal_frame_c1.py",
        "bytes": 37361,
        "sha256": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
        "git_blob_sha": "84a063e3efaa54b872b3ff0ff0f8a222ba0712e0"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
          "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "count": 1
        },
        {
          "before": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
          "after": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "count": 1
        }
      ]
    },
    {
      "role": "stage_matrices",
      "parent": {
        "name": "fixed_fejer_meridian_stage_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_stage_matrices.py",
        "bytes": 61280,
        "sha256": "f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791",
        "git_blob_sha": "57e215d6bd28e7df8d7172106df5caa209ebc78c"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_stage_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_stage_matrices.py",
        "bytes": 61280,
        "sha256": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
        "git_blob_sha": "9eabce7cdf2460213b8d2bea4005321ec9ab4591"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
          "after": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "count": 1
        },
        {
          "before": "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246",
          "after": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "count": 1
        }
      ]
    },
    {
      "role": "adjacent_matrices",
      "parent": {
        "name": "fixed_fejer_meridian_adjacent_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_adjacent_matrices.py",
        "bytes": 36766,
        "sha256": "bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564",
        "git_blob_sha": "641da23cdb76029f343ab441d03625e190cc4ae1"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_adjacent_matrices.py",
        "bytes": 36766,
        "sha256": "ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657",
        "git_blob_sha": "6fcac6e4f16191b2b7be20f1c04bbab884632985"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811",
          "after": "617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247",
          "count": 1
        },
        {
          "before": "c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246",
          "after": "edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b",
          "count": 1
        },
        {
          "before": "f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791",
          "after": "6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2",
          "count": 1
        }
      ]
    },
    {
      "role": "detached_meridian_values",
      "parent": {
        "name": "fixed_fejer_detached_meridian_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
        "bytes": 41126,
        "sha256": "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de",
        "git_blob_sha": "2b547c08dcaeb55701f5c68ba56d405f595f5b9e"
      },
      "output": {
        "name": "fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_detached_meridian_values.py",
        "bytes": 41135,
        "sha256": "f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e",
        "git_blob_sha": "7075bca30d05c045023b7823b8f80b75bfd34d4f"
      },
      "patches": [
        {
          "before": "552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3",
          "after": "b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6",
          "count": 1
        },
        {
          "before": "complete-fixed-fejer-detached-meridian-values-normal-layer-v1",
          "after": "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1",
          "count": 1
        },
        {
          "before": "2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0",
          "after": "3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73",
          "count": 1
        }
      ]
    },
    {
      "role": "root_packets",
      "parent": {
        "name": "fixed_fejer_meridian_root_packets.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_root_packets.py",
        "bytes": 73723,
        "sha256": "c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4",
        "git_blob_sha": "2b294ce46cf51c24c90b6e71c26d0d9c4269d28f"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_root_packets.py",
        "name": "fixed_fejer_paired_halfwave_root_packets.py",
        "bytes": 74385,
        "sha256": "8bf66692d39950c1e7c3a2b48812b686ed27a51068316ca7a786dbeaa08aee4a",
        "git_blob_sha": "b340f47df551b4609e45ae547449adadbc3368b6"
      },
      "patches": [
        {
          "before": "NORMALS = {\n",
          "after": "NORMALS = {\n    'c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac': dict(schema='complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1',\n        base='b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6',\n        adjacent='ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657',calibration='c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106',\n        analytic='617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247',analytic_frame='5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e',\n        closure_values='3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73'),\n",
          "count": 1
        }
      ]
    },
    {
      "role": "analytic_J3_binding",
      "parent": {
        "name": "fixed_fejer_meridian_source_binding.py",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_meridian_source_binding.py",
        "bytes": 41894,
        "sha256": "3ee65e2c45d6e9cb81fac1ad0a4c439a291aa2cc3fc73d68f896107c24e2ee68",
        "git_blob_sha": "d753647cfb4a0df8bc5d650cf4ca49ae1573f5f3"
      },
      "output": {
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_paired_halfwave_source_binding.py",
        "name": "fixed_fejer_paired_halfwave_source_binding.py",
        "bytes": 41966,
        "sha256": "1a510efc3e5285bd3359229d739cecbcfc853d48dfe58b7f9c848343d6827384",
        "git_blob_sha": "1abdf0ca7867b1deb54a2a6d6e7c8130e42cf948"
      },
      "patches": [
        {
          "before": "SCHEMA = \"complete-fixed-fejer-meridian-values-source-model-and-report-binding-v1\"",
          "after": "SCHEMA = \"complete-fixed-fejer-paired-halfwave-source-model-and-report-binding-v1\"",
          "count": 1
        },
        {
          "before": "OPERATOR_SCHEMA = \"complete-fixed-fejer-detached-meridian-values-normal-layer-v1\"",
          "after": "OPERATOR_SCHEMA = \"complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1\"",
          "count": 1
        },
        {
          "before": "BASE_SOURCE_SHA256 = '552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3'",
          "after": "BASE_SOURCE_SHA256 = 'b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6'",
          "count": 1
        },
        {
          "before": "SOURCE_BINDINGS = {\"analytic_J3\":[\"fixed_fejer_meridian_analytic_stage_jacobian.py\",\"223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811\"],\"frame_C1\":[\"fixed_fejer_meridian_normal_frame_c1.py\",\"c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246\"],\"stage_matrices\":[\"fixed_fejer_meridian_stage_matrices.py\",\"f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791\"],\"adjacent_matrices\":[\"fixed_fejer_meridian_adjacent_matrices.py\",\"bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564\"],\"reference_calibration\":[\"fixed_fejer_meridian_reference_calibration.py\",\"aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3\"],\"endpoint\":[\"fixed_fejer_detached_meridian_normal_lift.py\",\"76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d\"],\"analytic_frame\":[\"fixed_fejer_meridian_analytic_normal_frame.py\",\"d3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd\"],\"closure_values\":[\"fixed_fejer_meridian_closure_values.py\",\"2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0\"],\"detached_meridian_values\":[\"fixed_fejer_detached_meridian_values.py\",\"eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de\"]}",
          "after": "SOURCE_BINDINGS = {\"analytic_J3\":[\"fixed_fejer_paired_halfwave_analytic_stage_jacobian.py\",\"617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247\"],\"frame_C1\":[\"fixed_fejer_paired_halfwave_normal_frame_c1.py\",\"edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b\"],\"stage_matrices\":[\"fixed_fejer_paired_halfwave_stage_matrices.py\",\"6ca8631605d52374c754292221dc119ac934c929a17fa36211358463d667a0c2\"],\"adjacent_matrices\":[\"fixed_fejer_paired_halfwave_adjacent_matrices.py\",\"ca58255f5dbe69b3e5941d20383f1a3bdf0c54bb31a34d6f2d2c54e4e83a1657\"],\"reference_calibration\":[\"fixed_fejer_paired_halfwave_reference_calibration.py\",\"c89612303af1b290f6f1a6fb410d0dc3b4be98acb16b05dd338b01cb53e72106\"],\"endpoint\":[\"fixed_fejer_paired_halfwave_normal_lift.py\",\"c2903ac5ebc21faf0a150c5446db5f1d77f226793b4a56f9436201c244eae1ac\"],\"analytic_frame\":[\"fixed_fejer_paired_halfwave_analytic_normal_frame.py\",\"5be98c134ef7b97d6e80de957f6eb35a6683f73a5a76716ea6173dcedc1d195e\"],\"closure_values\":[\"fixed_fejer_paired_halfwave_closure_values.py\",\"3c04a76103412f424de81ae471b4f27c5cd11408967cab1e61b2a7df5ed0db73\"],\"detached_meridian_values\":[\"fixed_fejer_paired_halfwave_detached_meridian_values.py\",\"f21293af36a79085b2c4681d43ddf7de42bf690066b4ef0d40ea74bf4620269e\"]}",
          "count": 1
        }
      ]
    }
  ]
}''')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_parent(repo, record):
    path = repo/record["path"]
    data = path.read_bytes()
    if len(data) != record["bytes"] or digest(data) != record["sha256"]:
        raise ValueError("The complete declared parent source changed: "+str(path))
    return data.decode("utf-8")


def construct(text, item):
    old = text
    for patch in item["patches"]:
        if text.count(patch["before"]) != patch["count"]:
            raise ValueError("An exact complete source replacement has the wrong multiplicity")
        text = text.replace(patch["before"], patch["after"])
    data = text.encode("utf-8")
    record = item["output"]
    if len(data) != record["bytes"] or digest(data) != record["sha256"]:
        raise ValueError("A complete paired-halfwave source has the wrong identity")
    restored = text
    for patch in reversed(item["patches"]):
        if restored.count(patch["after"]) != patch["count"]:
            raise ValueError("An exact reverse source replacement has the wrong multiplicity")
        restored = restored.replace(patch["after"], patch["before"])
    if restored != old:
        raise ValueError("The complete original source cannot be restored byte for byte")
    return data


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--output-directory", type=Path, required=True)
    args = p.parse_args()
    outputs = [(item, construct(read_parent(args.repo, item["parent"]), item))
               for item in SPEC["sources"]]
    args.output_directory.mkdir(parents=True, exist_ok=True)
    records = []
    for item, data in outputs:
        path = args.output_directory/item["output"]["name"]
        if path.exists():
            raise FileExistsError("Preserve an already written complete source: "+str(path))
        path.write_bytes(data)
        records.append(dict(role=item["role"], path=str(path.resolve()),
                            bytes=len(data), sha256=digest(data)))
    print(json.dumps(dict(schema=SPEC["schema"], complete_sources=records,
        all_complete_parent_bytes_used=True, complete_inverse_source_replacements=True,
        numerical_or_AST_or_compile_evaluation_performed=False), indent=2))


if __name__ == "__main__":
    main()
