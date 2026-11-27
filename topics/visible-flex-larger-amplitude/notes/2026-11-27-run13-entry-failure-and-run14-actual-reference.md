# 公开13/14：两次实际参考输入与N4096入口失败

这两次参考构造均真实返回0；它们的固定数值reference、carrier、input、node、scalar及target文件whole SHA与原12相同，而本次run/source归属、preparation和history/provenance文件保持各自实际身份。没有从相同数值输入推断出新求解场。

公开13在完整参考之后真实执行N4096 science及pure，分别返回1/8.492643880999935s和1/6.1936070869999185s。科学report与pure输出均未生成；仅完整command计划实际存在。当前记录不能区分入口、构造、守卫或数值失败，原异常链尚未读到，不能猜因或放宽目标/来源。

公开14的完整M320科学子进程在16:08:47 UTC的索引仍running；真实sourcecommit a9ab24c38efa6a56c17f5285fc8c8f7a5f886709、launcher596e137f6e381a2fdbc882a559a30b664c6e985095867535f3b32d7fa61c417c、PID4009。其16:08:45点e013173c13416cafc6c09d8ccad4c86993c85424c90fd6a6024c10808bc72594只属normal进度，不能填accepted、final、metric或geometry结果。

## 完整原始紧凑记录

固定读取提交04e3e5541dd83142ec445b5c95e462152627001a下：
- [13完整阶段1–4](https://github.com/Rogerhu12/math-research-public/blob/04e3e5541dd83142ec445b5c95e462152627001a/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46028002241-1-part-001.md)，30067B，blob9de98344e8605dfd4dcda66c2759d1472bdaf7c7，SHA256 83a4ff77b0fbd9794edcfe3c51508cb02af663d8cbf08fea4468845d262f022a。
- [14完整阶段1–2](https://github.com/Rogerhu12/math-research-public/blob/04e3e5541dd83142ec445b5c95e462152627001a/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46028184571-1-part-001.md)，16602B，blobbe5daabc639905ebc87078d67f9ea38b882cffe2，SHA256 98eb4446b33c6a75d35b962381101c09dbdd8b253046c170e6fd733f5640d4ab。

这些完整卷保所有原argv、输入与输出身份、源码、队列与真实返回；下面再保本次各实际输入与失败身份，科学数组和原日志仍只runner。

## 实际maker与reference

```json
[
  {
    "slot": "13",
    "run": "46028002241/1",
    "maker": {
      "returncode": 0,
      "seconds": 6.210515469000001,
      "source_commit": "967f8b5b4266db6057577db2e3a8ae3c0c8e95e4",
      "outputs": [
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/report.json",
          "sha256": "95ad8961722cbecb32faafccffd53e07d7afbd410db282ce794477ff28878c73",
          "bytes": 65335
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
          "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "bytes": 4334
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
          "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "bytes": 144306
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
          "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "bytes": 40488
        }
      ]
    },
    "reference": {
      "returncode": 0,
      "seconds": 574.277473395,
      "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "source_commit": "3e164b4c24cb814c9ccd8f42c182e526575b0502",
      "metrics": {
        "fixed-fejer-reference/report.json": {
          "schema": "R690-fixed-fejer-axisymmetric-SO3-preparation-v1",
          "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
          "source_commit": "3e164b4c24cb814c9ccd8f42c182e526575b0502",
          "complete": true,
          "seconds": 572.0987181300001,
          "reference_model": "ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac",
          "fixed_scalar": "d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160",
          "scalar_parameters": "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa",
          "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
          "full_target": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
          "fixed_recipe": "5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a",
          "model_chart": "af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103",
          "model_mesh": "ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc",
          "core0": "0x1.c000000000000p-2",
          "core1": "-0x1.3333333333333p-4",
          "core2": "0x1.b6db6db6db6dbp-6",
          "M": 160,
          "J": 923,
          "P": 7377,
          "N": 2048,
          "height": 1.947054437068418,
          "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "input_preparation": "95ad8961722cbecb32faafccffd53e07d7afbd410db282ce794477ff28878c73",
          "locations": "661ae267c1dfc6bfd73f4eb7453e3fc3bcb08e5581ea3de93bda2b26468bd638",
          "location_provenance": "604f6886386a9088a7e5bd2292490eb19c5e7321c582831d7f1c3ad0ea20d8df",
          "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "leaf_target": 2218,
          "actual_leaves": 2218,
          "accuracy_reached": false,
          "integral_width_exact": "20705780131163723599438290019541571913013106551525357578680931811765776678181/14411518807585587200000000000000000000000000000000000000000000000000000000000000000000000",
          "whole_tail": true,
          "unresolved_tail_dropped": false,
          "clock_selects_leaves": false,
          "old_warm_not_required": true,
          "old_surface_used": false,
          "old_directions_replayed": false,
          "old_certificates_inherited": false,
          "physical_field_read": false,
          "new_field_still_required": true,
          "run": "46028002241",
          "attempt": "1"
        },
        "fixed-fejer-reference/material-envelope-carrier-binding.json": {
          "schema": "complete-fixed-fejer-actual-reference-binding-v1",
          "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
          "source_commit": "3e164b4c24cb814c9ccd8f42c182e526575b0502",
          "run": "46028002241",
          "attempt": "1",
          "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
          "full_reference_definition": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
          "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "preparation": "95a6e90ba0c2b16ad6d7d4859f0020970b0e43bcc8c26bb5cf1dac9a739f96fe",
          "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "history": "604f6886386a9088a7e5bd2292490eb19c5e7321c582831d7f1c3ad0ea20d8df",
          "all_six_actual": true,
          "old_values_or_unknown_history_inherited": false
        }
      },
      "outputs": [
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/report.json",
          "sha256": "95a6e90ba0c2b16ad6d7d4859f0020970b0e43bcc8c26bb5cf1dac9a739f96fe",
          "bytes": 84970
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/reference.npz",
          "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "bytes": 894879
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/observations.npz",
          "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "bytes": 205842
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/locations.json",
          "sha256": "661ae267c1dfc6bfd73f4eb7453e3fc3bcb08e5581ea3de93bda2b26468bd638",
          "bytes": 106771
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/supplied-location-provenance.json",
          "sha256": "604f6886386a9088a7e5bd2292490eb19c5e7321c582831d7f1c3ad0ea20d8df",
          "bytes": 223955
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/fixed-target-definition.json",
          "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "bytes": 30919
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
          "sha256": "03f0ab9a27f53fc26116378567476651a8e5c3e5a39b69323d0dc860ff271a38",
          "bytes": 35712
        }
      ],
      "summary_errors": [],
      "missing_outputs": []
    }
  },
  {
    "slot": "14",
    "run": "46028184571/1",
    "maker": {
      "returncode": 0,
      "seconds": 6.144792773000006,
      "source_commit": "80649973c546ec5f7c9930313617ae2e903980d6",
      "outputs": [
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-r690-inputs/report.json",
          "sha256": "dce93d30556c90359d15310b5d544c44d5f097dc3108d4d60f8920180ffd7c3a",
          "bytes": 65334
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
          "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "bytes": 4334
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
          "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "bytes": 144306
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
          "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "bytes": 40488
        }
      ]
    },
    "reference": {
      "returncode": 0,
      "seconds": 519.242307125,
      "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "source_commit": "e1f3eae778b24a03a30cbcec395f21fbb3156169",
      "metrics": {
        "fixed-fejer-reference/report.json": {
          "schema": "R690-fixed-fejer-axisymmetric-SO3-preparation-v1",
          "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
          "source_commit": "e1f3eae778b24a03a30cbcec395f21fbb3156169",
          "complete": true,
          "seconds": 515.628357885,
          "reference_model": "ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac",
          "fixed_scalar": "d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160",
          "scalar_parameters": "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa",
          "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
          "full_target": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
          "fixed_recipe": "5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a",
          "model_chart": "af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103",
          "model_mesh": "ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc",
          "core0": "0x1.c000000000000p-2",
          "core1": "-0x1.3333333333333p-4",
          "core2": "0x1.b6db6db6db6dbp-6",
          "M": 160,
          "J": 923,
          "P": 7377,
          "N": 2048,
          "height": 1.947054437068418,
          "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "input_preparation": "dce93d30556c90359d15310b5d544c44d5f097dc3108d4d60f8920180ffd7c3a",
          "locations": "72df3c5b2a02cbdb9e1554f3dd59f10c1e30098149dc2ba6639416c464c48581",
          "location_provenance": "a785041d02a21ae877b3bddbfe2721da3da6535dba3123fc7417266c88ef01c5",
          "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "leaf_target": 2218,
          "actual_leaves": 2218,
          "accuracy_reached": false,
          "integral_width_exact": "20705780131163723599438290019541571913013106551525357578680931811765776678181/14411518807585587200000000000000000000000000000000000000000000000000000000000000000000000",
          "whole_tail": true,
          "unresolved_tail_dropped": false,
          "clock_selects_leaves": false,
          "old_warm_not_required": true,
          "old_surface_used": false,
          "old_directions_replayed": false,
          "old_certificates_inherited": false,
          "physical_field_read": false,
          "new_field_still_required": true,
          "run": "46028184571",
          "attempt": "1"
        },
        "fixed-fejer-reference/material-envelope-carrier-binding.json": {
          "schema": "complete-fixed-fejer-actual-reference-binding-v1",
          "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
          "source_commit": "e1f3eae778b24a03a30cbcec395f21fbb3156169",
          "run": "46028184571",
          "attempt": "1",
          "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
          "full_reference_definition": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
          "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "preparation": "43a727cfa6ee7f9760cadfb4b0758709cde5823fa794eb2762c44b16acf0e969",
          "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
          "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
          "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
          "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "history": "a785041d02a21ae877b3bddbfe2721da3da6535dba3123fc7417266c88ef01c5",
          "all_six_actual": true,
          "old_values_or_unknown_history_inherited": false
        }
      },
      "outputs": [
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/report.json",
          "sha256": "43a727cfa6ee7f9760cadfb4b0758709cde5823fa794eb2762c44b16acf0e969",
          "bytes": 84966
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/reference.npz",
          "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
          "bytes": 894879
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/observations.npz",
          "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
          "bytes": 205842
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/locations.json",
          "sha256": "72df3c5b2a02cbdb9e1554f3dd59f10c1e30098149dc2ba6639416c464c48581",
          "bytes": 106771
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/supplied-location-provenance.json",
          "sha256": "a785041d02a21ae877b3bddbfe2721da3da6535dba3123fc7417266c88ef01c5",
          "bytes": 223955
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/fixed-target-definition.json",
          "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
          "bytes": 30919
        },
        {
          "path": "/home/runner/work/_temp/visible-larger-research-46028184571-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
          "sha256": "92a1bd95d5934efd666f6f01925a40c38fbc37b6546f78e1e764680553f5d422",
          "bytes": 35712
        }
      ],
      "summary_errors": [],
      "missing_outputs": []
    }
  }
]
```

两个reference都保2218全leaf/完整无限尾、accuracy_reached=false、无丢弃未解尾；它们没有读取完整新物理场，未付范围如实保留。e640只是原scalar参数投影，d492是整个scalar identity，不相混。

## 13两次实际失败

```json
[
  {
    "step_id": "complete-fixed-fejer-angular-N4096-independent-20261127",
    "returncode": 1,
    "seconds": 8.492643880999935,
    "source_sha256": "e93b1ef25a24a3f925a33b4c323a7b31dc93b42bd2bda1aca887d8f89aa73e52",
    "source_commit": "50e4489cdfa544d4c16463d5bfe3624231e29c23",
    "parent_sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent-command.json",
        "sha256": "0c1fd8e98dc88a294fdea850709376c45ef9e1ddf7b56339c23940969e8f936e",
        "bytes": 47833
      }
    ],
    "summary_errors": [
      {
        "report": "fixed-fejer-angular-N4096-independent/report.json",
        "error": "[Errno 2] No such file or directory: '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent/report.json'"
      }
    ],
    "missing_outputs": [
      "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/fixed-fejer-angular-N4096-independent/report.json"
    ]
  },
  {
    "step_id": "actual-fixed-fejer-angular-N4096-independent-20261127",
    "returncode": 1,
    "seconds": 6.1936070869999185,
    "source_sha256": "7ffea5bfda0108af0276e60a16c29e15669e3ad5996331cf35bdf369d9659507",
    "source_commit": "f515d65bcfcf76aa07d1001f3f81605192ab424d",
    "parent_sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
    "outputs": [],
    "summary_errors": [
      {
        "report": "postprocess/fixed-fejer-angular-N4096-independent-readout.json",
        "error": "[Errno 2] No such file or directory: '/home/runner/work/_temp/visible-larger-research-46028002241-1/research/postprocess/fixed-fejer-angular-N4096-independent-readout.json'"
      }
    ],
    "missing_outputs": [
      "/home/runner/work/_temp/visible-larger-research-46028002241-1/research/postprocess/fixed-fejer-angular-N4096-independent-readout.json"
    ]
  }
]
```

不把缺report理解成某个数学不可能性；不把8.5秒据此命名为零F/J，实际执行到哪里须原异常与将来真实诊断说明。

## 已接回同runner的完整异常读取

使用已刊完整read_actual_followup_failure_chain.py原字8679B，SHA2565d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360、blob22e64456b28a246329513397e4ebb22f5687805e。两步从原completed status绑定实际run/step/source/log，只读最多64000原log-tail bytes和每个7000字符的第一/末异常，分别报是否截断和是否完整原日志；没有科学重跑/fixture/新门。

完整参数文件[actual13原异常读取](../computations/resume-20261127-run13-actual3-4-first-and-last-tracebacks-ready.json) 10254B / 8912a9b73b77d015b04f0390646a0e114b7014daae024aa54217a7bff8b5cdb6。新活13队列7654B / 911000c1770d5983377a941b8d9a906ad4b29c8f4b6afefc9fe87fbffd5d6a8b，两step原样，finish=false。

旧活13三个对象（reference、science、pure）均已自然返回，才从活队列退休；全三个原对象固定保347fffd9de5ed11c2cc8cda999943743c1553e39下resume-20261127-followups-13.json（93488B/8563e8619cb88493458ccd2ee351b178aae520d731305a07e669776e8fb7ac76）。原maker全对象保99b59启动提交，原完整科学ready c043及3模式仍在。没有删参数/输出/selector，失败与未知仍完整保。读回真实异常后接完整修复与新独立输出路径，不复用失败路径或冒成功父。
