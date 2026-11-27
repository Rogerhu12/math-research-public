# 实际18第三异常：完整 geometry 生产器绑定补齐并继续原规模求解

会话 Astra-larger-e4e2a2bf-20261126。**研究未完成；来源修复不代数学结果，公开完整求解继续。**

## 第三实际异常及责任

第7步 `complete-fixed-fejer-meridian-batched-callable-bound-20261127` 的实际 source commit 为 `512fcefd67eb0adba7b27e654cb51bacf82c2439`，launcher 为完整 d683762cfacb24a91d0011a1a061f1e7cda992595717f3f5dc9e8d71bb3207db。它在8.196651488000043秒后自然返回1，只生成50558B command，SHA256 7efc2534cdaac860314581b56669ce269b8276379a2be01022f26208b10e2dcf；report缺失。

第8步原5d25完整异常读取器真正返回0，source commit `0447302e7554a6139b8b4a12dc2e139681aaf1c0`，输出11227B / SHA256 be218f68aa26e3414edad9e59709650f196d62b7b7e5c4197fd2862954b22780。完整原log6727B / SHA256 `bf27eb1ef9a48f892e131a6a7acdfdf49be12e63627ddbec5b72c32504159048`，从byte0读取，两栈均完整；外层末行摘要截取不改变首栈。完整原始返回卷43095B / SHA256 c444ee1d6e6379c02eb7d975158f1cebfe68630ccc5b04a0d560bbc37ecff580，Git blob3f8714f402622a842ea95a7dc478e82129b6da53，保在原公开分卷。诊断0不冒科学0。

实际首栈：

```text
Traceback (most recent call last):
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py", line 1130, in <module>
    main()
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py", line 605, in main
    screen = geometry_module.GeometryScreen(q, args.repo, budgets,envelope=envelope,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py", line 363, in __init__
    raise ValueError('Use the complete actual query-independent meridian data producer')
ValueError: Use the complete actual query-independent meridian data producer
```

geometry 的 `DETACHED_MERIDIAN_VALUES_SOURCE_SHA256` 仍是旧 helper7aa；真正 normal 已加载完整eaea。**这是根进程在上一轮来源传播时漏更新 geometry 的独立 helper 常量。** 它不说明均值根不存在或几何约束不能满足。前两处初始化错误已经在这次实际执行中越过；不因此推测后续数值计算已经成功。

该处 integration_data 是实际 helper 内定义的实例方法；此处使用 bound method 的 __func__ 正确。新geometry只把该64字字面值由7aa改为实际eaea。原line361–363完整guard逐字保留，所有数值方法、批角、几何聚合、源文件校验、输入/model/point和完整六jet都不动。新旧geometry同为88163B；反向单替换逐字还原c1dad父体。此前缓存静态函数解包、frame完整wrapper登记及其原guards均保留。

## 完整来源传播

直接完整源码父为 `f2eb4e3aaa6d9568418dd0373acb585738984823`。geometry修正后，batch纯读绑定、driver的完整137角色表、纯读取器、launcher和准确场输入两项来源都随真实whole source改变。当前18运行体中5个改变，其余13个完整原字保持；包括helper eaea、normal76185、packet c750、frame d3cf、binder3ee和transfer b8af。准确场输入为第6个完整改变文件，32969B，其余三个pin保持。

| 来源 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| geometry | 88163 | `5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135` | `c5325d3da8329547ad81e74a5da479323bfccd21` |
| batched_geometry_binding | 12136 | `9104c29d03a589939f46ccdb08a55a3564f702acd147840cc91488b72eee2d06` | `60d34ff709af95a702d786e4d0eb77ea7a1e23bf` |
| driver | 99313 | `10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f` | `8bba3e30bb8e843fd725a2d19f8966b984acc4ae` |
| reader | 99382 | `8027ec35ea8ee74ab38468678683d798530e8c7a229ec3f9e8d5c631c75dde49` | `9cd36fd99113d285fc47f17bad929647c8fc6de3` |
| launcher | 22136 | `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506` | `168b1a1d7bc58793985138eb8a02a6e3911d74cc` |
| accurate_field_input | 32969 | `d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7` | `6a724fcd48a0d1da27b4762c9ac4ef6ac734cae4` |

完整137项registry、18运行体和原120历史path/SHA对都保在 [完整交付](../computations/fixed-fejer-meridian-producer-binding-repair-complete-delivery.json)。不存在旧source标签冒新场、源文件只留接口骨架或guard放宽。[geometry独立完整修复](../computations/fixed-fejer-geometry-meridian-source-constant-repair-delivery.json)同时保原单行、完整源码、再生器和准确责任说明。

[上层完整再生器](../scripts/resume_20261126/reproduce_fixed_fejer_meridian_producer_binding_upper_sources.mjs)从固定f2eb完整Git父读取这6个文件，保完整正逆替换及whole SHA/bytes/blob；[参数完整再生器](../scripts/resume_20261126/reproduce_fixed_fejer_meridian_producer_binding_parameters.mjs)从原固定36fb两份完整参数输出新两个ready。它们只是完整保存与恢复入口，没有作为额外科学准入步骤执行，也未增加Python/AST/fixture/局部数值测试。

## 原规模实际续求

science完整ready97806B / SHA256 75fef2a2d4505cc0e35941f5b7d6b33c8565af7a925171c2f5f61fa203478018，原157argv与458formal完整；pure85234B / SHA256 74b548fe85faa89b4f0109e8b10fe4c70d524ebade97698245a8c26efc85f0c8，原7argv与445formal完整；48个实时映射保持6个数学加42个normal字段。原408/395正式映射和新增50完整字段不裁。所有原budget、seed1/4和1/32、M160/J923/N2048/32stage、变量、全部支持/胞/完整闭面责任保持；唯一argv变化是完整输出namespace。

新输出 `fixed-fejer-meridian-batched-producer-bound`，独立command为同prefix加-command.json。完整科学对象65310B排入原46062343475/1 runner。只退已实际返回0的第8诊断对象，原完整诊断队列固定于09745b2e08113631f67aa826e94b96cc723282ac；前一完整科学队列固定f2eb。完整pure对象保留，真实科学自然返回后接；合并载荷超95000B不削参数。新实际source commit、报告、场、root/packet、accepted和费用仍未知；不从准备好的源码推通过。

两原必要input都已实际0，继续同runner复用。reference.npz894879B /212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb，完整准备report84971B /38a5932ebe77cb8f1513c369f6f575f112bac73dc815ac1406d30ce0aa2d0be2；maker65336B /b800ec4fd4901b903a7c12eb970c14373206e6f30b0d2ebe43f0ee852b72139b。其余nodes/scalar/carrier/locations/history/target/binding的全部真实身份逐项保在交付；没有重新生成输入或跨runner搬原数组。

## 后续严格数学责任

独立 producer_R722 完整后验均值核及准确全角径向由原e10a/9da完整数学父显式绑定10fa/8027/d892，normal/packet保持76185/c750；未刊callable_R722候选不冒当前场。R722全后验根域、原R710/R711角jet/profile、全部输入误差和三残差、1024整圆、922径向及cuts、32stage、六jet/全尾/working误差都未付。旧R709 bool保持真实含义；新域的存在和分支覆盖必须实际验证。

全closed帽、混合点/allphase/reach/whole-image、R650、R718八beta+径向、R716一般三phase/唯一sidecar/正体积/非零中心矩责任全部继续。全5个t及三级空间/时间、完整mesh、频率精化要对同一固定g/参数实际运行；M320零包含不是新精化解。完整13件final、immutable required-angle snapshot与实际匹配来源不能用live progress替代。

本次不宣称满足README任何尚未付的全域度量、全t几何、强C²连续、固定握持或含反射非刚性标准。持续求解，不以第三错误修复、来源包或运行时长结束。

## 第8诊断的完整实际字段

```json
{
  "name": "followup:read-actual18-callable-bound-first-and-last-original-failure-tracebacks-20261127",
  "state": "completed",
  "returncode": 0,
  "seconds": 6.030103603000043,
  "scope": "Read only the genuinely returned complete callable-bound science step7 of original run46062343475/1, exit1, unique actual status, exact d683 launcher and original log. Preserve the full unchanged5d25 reader,64000-byte tail,7000-character excerpts and all original scalar selectors and clipping distinctions. No numerical replay, source test, F/J/root or admission gate. Third inner failure remains unknown until actual readback.",
  "metrics": {
    "postprocess/actual18-callable-bound-first-and-last-original-tracebacks.json": {
      "schema": "actual-public-followup-first-and-last-failure-tracebacks-v1",
      "source_sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360",
      "derived_from_source_sha256": "ef017af52fd8b9801434b3af655f9fccb7d7a51e9bf0abb3ff5e85496659e338",
      "status_sha256": "1c21e17c4e2150edc9326d4a96626a8bfbb847d0488f8cc4c7034a9d1c42521a",
      "status_sha256_scope": "exact captured status bytes, not a later mutable status version",
      "step_id": "complete-fixed-fejer-meridian-batched-callable-bound-20261127",
      "actual_source_sha256": "d683762cfacb24a91d0011a1a061f1e7cda992595717f3f5dc9e8d71bb3207db",
      "actual_source_commit": "512fcefd67eb0adba7b27e654cb51bacf82c2439",
      "actual_returncode": 1,
      "actual_recorded_seconds": 8.196651488000043,
      "actual_log_path": "/home/runner/work/_temp/visible-larger-research-46062343475-1/research/followup-logs/0007-8be405c2d4f2.log",
      "actual_log_sha256": "bf27eb1ef9a48f892e131a6a7acdfdf49be12e63627ddbec5b72c32504159048",
      "actual_log_bytes": 6727,
      "log_unchanged_during_read": true,
      "tail_start_byte": 0,
      "tail_bytes_read": 6727,
      "maximum_tail_bytes": 64000,
      "captured_tail_contains_entire_log": true,
      "captured_tail_sha256": "bf27eb1ef9a48f892e131a6a7acdfdf49be12e63627ddbec5b72c32504159048",
      "traceback_markers_in_captured_tail": 2,
      "first_traceback_found": true,
      "first_traceback_start_byte": 0,
      "first_traceback_is_first_in_entire_log": true,
      "first_traceback_excerpt": "Traceback (most recent call last):\n  File \"/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py\", line 1130, in <module>\n    main()\n  File \"/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py\", line 605, in main\n    screen = geometry_module.GeometryScreen(q, args.repo, budgets,envelope=envelope,\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py\", line 363, in __init__\n    raise ValueError('Use the complete actual query-independent meridian data producer')\nValueError: Use the complete actual query-independent meridian data producer\n",
      "first_traceback_excerpt_clipped": false,
      "first_traceback_final_nonempty_line": "ValueError: Use the complete actual query-independent meridian data producer",
      "first_traceback_final_line_clipped": false,
      "last_traceback_found": true,
      "last_traceback_start_byte": 1138,
      "last_traceback_excerpt": "Traceback (most recent call last):\n  File \"/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py\", line 343, in <module>\n    main()\n  File \"/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_meridian_batched_actions.py\", line 339, in main\n    subprocess.run(command, env=env, cwd=args.repo, check=True)\n  File \"/opt/hostedtoolcache/Python/3.12.14/x64/lib/python3.12/subprocess.py\", line 571, in run\n    raise CalledProcessError(retcode, process.args,\nsubprocess.CalledProcessError: Command '['/opt/hostedtoolcache/Python/3.12.14/x64/bin/python', '-u', '/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py', '--repo', '/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb', '--reference-bundle', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/reference.npz', '--preparation-report', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/report.json', '--carrier', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/observations.npz', '--node-report', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json', '--scalar-input', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json', '--outdir', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-meridian-batched-callable-bound', '--manifest', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/locations.json', '--material-envelope-binding', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json', '--independent-envelope-branch', '--pending-parallel-envelope-run', '45909290354/1', '--pending-parallel-envelope-run', '45929088658/1', '--pending-parallel-envelope-run', '45943410994/1', '--pending-parallel-envelope-run', '45972294636/1', '--pending-parallel-envelope-run', '46011377225/1', '--pending-parallel-envelope-source', '45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5', '--pending-parallel-envelope-source', '45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9', '--pending-parallel-envelope-source', '45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5', '--pending-parallel-envelope-source', '45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1', '--pending-parallel-envelope-source', '46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd', '--envelope-near-active-rows', '32', '--angles', '2048', '--stage-block', '64', '--angle-block', '8', '--integration-order', '8', '--inverse-root-iterations', '18', '--inverse-root-tolerance', '2e-12', '--norm-kind', 'jet-sum', '--radial-norm-length', '0.05', '--angular-transition', '24.0', '--torch-threads', '4', '--damping', '0.01', '--directions', '1', '--maxiter', '16', '--restoration-directions', '4', '--restoration-damping', '0.01', '--restoration-maxiter', '64', '--line-trials', '15', '--qp-atol', '0.0', '--qp-rtol', '1e-06', '--qp-feasibility-tolerance', '2e-11', '--qp-rank-tolerance', '2e-12', '--active-rows', '192', '--active-block-columns', '32768', '--active-band', '0.025', '--reach-ratio', '0.03', '--reach-safety-factor', '0.992', '--marked-diameter-budget', '4.2', '--witness-lower-budget', '0.9', '--amplitude-height-floor', '1.01', '--amplitude-top-radius', '2', '--amplitude-top-distance', '4', '--spectral-p', '4', '--spectral-epsilon', '0.001', '--spectral-scale', '0.05', '--legacy-fraction', '0.5', '--target', '1e-09', '--panels', '128', '--seed-boundary-total-length', '1/4', '--seed-profile-delta', '1/32', '--seed-radial-quadrature-order', '8', '--seed-profile-quadrature-order', '16', '--seed-mean-maxiter', '128', '--seed-mean-tolerance', '2e-12', '--seed-mean-backtracks', '24', '--seed-mean-armijo', '0.0001', '--seed-scalar-iterations', '64', '--endpoint-bubble-1-left', '1/32', '--endpoint-bubble-1-middle', '1/4', '--endpoint-bubble-1-right', '15/32', '--endpoint-bubble-2-left', '17/32', '--endpoint-bubble-2-middle', '3/4', '--endpoint-bubble-2-right', '31/32', '--endpoint-root-tolerance', '2e-12', '--endpoint-root-iterations', '24', '--endpoint-root-backtracks', '18', '--endpoint-root-armijo', '0.0001', '--endpoint-control-radius', '2.0', '--normal-stages', '32', '--gamma-left', '1/16', '--gamma-middle', '1/8', '--gamma-right', '3/16', '--moment-input', '/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json', '--moment-input-sha256', 'df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c', '--moment-definition-sha256', '05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e', '--moment-input-binding', 'supported-smooth-triangle-reference']' returned non-zero exit status 1.\n",
      "last_traceback_excerpt_clipped": false,
      "last_traceback_final_nonempty_line": "subprocess.CalledProcessError: Command '['/opt/hostedtoolcache/Python/3.12.14/x64/bin/python', '-u', '/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fullclosed_fixed_fejer_meridian_batched_so3_qp.py', '--repo', '/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb', '--reference-bundle', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/reference.npz', '--preparation-report', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/report.json', '--carrier', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/observations.npz', '--node-report', '/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json', '--scalar-input', '/ho\n[bounded diagnostic: middle characters omitted]\n-left', '1/32', '--endpoint-bubble-1-middle', '1/4', '--endpoint-bubble-1-right', '15/32', '--endpoint-bubble-2-left', '17/32', '--endpoint-bubble-2-middle', '3/4', '--endpoint-bubble-2-right', '31/32', '--endpoint-root-tolerance', '2e-12', '--endpoint-root-iterations', '24', '--endpoint-root-backtracks', '18', '--endpoint-root-armijo', '0.0001', '--endpoint-control-radius', '2.0', '--normal-stages', '32', '--gamma-left', '1/16', '--gamma-middle', '1/8', '--gamma-right', '3/16', '--moment-input', '/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0007-8be405c2d4f2-512fcefd67eb/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json', '--moment-input-sha256', 'df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c', '--moment-definition-sha256', '05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e', '--moment-input-binding', 'supported-smooth-triangle-reference']' returned non-zero exit status 1.",
      "last_traceback_final_line_clipped": true,
      "first_and_last_are_same_traceback": false,
      "no_traceback_tail_excerpt": "",
      "no_traceback_tail_excerpt_clipped": false,
      "maximum_excerpt_characters": 7000,
      "traceback_scope": "first and last markers in bounded original log tail; no missing prefix inferred",
      "complete_log_published": false,
      "scientific_arrays_read": false,
      "scientific_reports_read": false,
      "field_or_J_evaluations": 0,
      "numerical_failure_cause_inferred": false,
      "github_run_id": "46062343475",
      "github_run_attempt": "1"
    }
  },
  "outputs": [
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46062343475-1/research/postprocess/actual18-callable-bound-first-and-last-original-tracebacks.json",
      "sha256": "be218f68aa26e3414edad9e59709650f196d62b7b7e5c4197fd2862954b22780",
      "bytes": 11227
    }
  ],
  "input_files": [
    {
      "role": "source",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_actual_followup_failure_chain.py",
      "commit": "0447302e7554a6139b8b4a12dc2e139681aaf1c0",
      "sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360"
    },
    {
      "role": "parent_bundle",
      "path": "/home/runner/work/_temp/visible-larger-research-46062343475-1/research/fixed-fejer-reference/reference.npz",
      "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb"
    },
    {
      "role": "followup_queue",
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-18.json",
      "path_commit": "09745b2e08113631f67aa826e94b96cc723282ac",
      "checkout_commit": "0447302e7554a6139b8b4a12dc2e139681aaf1c0",
      "sha256": "fe8a4e14dbc6b550dd985ee3b99bde686cab8de18838a5052af012031876d314"
    }
  ],
  "parent_sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
  "source_commit": "0447302e7554a6139b8b4a12dc2e139681aaf1c0",
  "source_sha256": "5d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360",
  "command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-u",
    "/home/runner/work/_temp/visible-larger-research-46062343475-1/followup-sources/0008-75bee7171667-0447302e7554/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_actual_followup_failure_chain.py",
    "--status",
    "/home/runner/work/_temp/visible-larger-research-46062343475-1/research/status.json",
    "--step-id",
    "complete-fixed-fejer-meridian-batched-callable-bound-20261127",
    "--output",
    "/home/runner/work/_temp/visible-larger-research-46062343475-1/research/postprocess/actual18-callable-bound-first-and-last-original-tracebacks.json",
    "--expected-run-id",
    "46062343475",
    "--expected-source-sha256",
    "d683762cfacb24a91d0011a1a061f1e7cda992595717f3f5dc9e8d71bb3207db",
    "--expected-log-path",
    "/home/runner/work/_temp/visible-larger-research-46062343475-1/research/followup-logs/0007-8be405c2d4f2.log",
    "--maximum-tail-bytes",
    "64000",
    "--maximum-excerpt-characters",
    "7000"
  ],
  "cleanup_generated": {
    "deleted": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "skipped": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "scope": "Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files"
  },
  "step_id": "read-actual18-callable-bound-first-and-last-original-failure-tracebacks-20261127",
  "summary_errors": [],
  "missing_outputs": []
}
```


## 第9完整入口首个实际数学统计

实际source commit `e3d2ebacae1ddce7990d72d778c96e851810ffe8`、launcher `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506`、PID7515。数学事件 `initial-statistics-returned` 时间 `2026-11-27T21:31:20.498871+00:00`；公开观察时间 `2026-11-27T21:34:20Z`，两时间不互换。

模型完整SHA为 `9ec211ddc5c14e0d4f0e47045ed84abc3ec4bc97fcf0e893959d6ba0cf8609bd`，目标配方字段仍957cf…；初始/当前点均 `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`。真实Phi 4954.71485872585、有限采样Gram算子误差 0.6374168330977955，accepted_directions=0，complete_report=false。初始几何、当前几何、trial与last_completed_trial尚未返回，相应None字段不补零；25个摘要选择器的None错误不等于程序失败。normal最新21:34:18、cached roots569、原closure返回4802、逻辑失败0，仅登记其实际口径，不推完整几何或时间速度比较。

这些初数字与17相同仍不证明两完整模型/浮点场/所有角或所有阶段相同。当前math_model独立，所有fee/packet/mesh严格按本source族绑定。首统计不是完整科学自然返回，childexit仍null；继续原全预算。当前完整index27196B/SHA256 `8ff11201107147ef669f28c29205abe692302ea726cde59fb04ace6719ec8a84`、固定Git提交 `e22a7bd579fa9e3c2e7cf54bc1c9801944ab7284`。完整原观察如下：

```json
{
  "step_id": "complete-fixed-fejer-meridian-batched-producer-bound-20261127",
  "scientific_source_commit": "e3d2ebacae1ddce7990d72d778c96e851810ffe8",
  "scientific_source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 7515,
  "observations": {
    "fixed-fejer-meridian-batched-producer-bound/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 21:34:18 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "cached_angle_roots": 569,
      "closure_original_returns": 4802,
      "closure_logical_failures": 0
    },
    "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T21:31:20.498871+00:00",
      "math_event": "initial-statistics-returned",
      "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "math_model": "9ec211ddc5c14e0d4f0e47045ed84abc3ec4bc97fcf0e893959d6ba0cf8609bd",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 4954.71485872585,
      "initial_Gram": 0.6374168330977955,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 4954.71485872585,
      "current_Gram": 0.6374168330977955,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-producer-bound/actual-normal-evaluation-progress.json",
      "bytes": 3294,
      "sha256": "a098f0583b5cac21371832af594219b9f588765e06304611c931affff06813f7",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "bytes": 3525,
      "sha256": "05bada3a8edf4c7765803fca4f36085bdb652d2d0d529a5c5c9cc497aa8f5f84",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "initial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "initial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "initial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.reach",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.body_diameter",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.distance_plus",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.distance_minus",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.cap_diameter",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "current_geometry.physical_g_by_family.height_floor",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-producer-bound/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "a305bec19071b895412fdd1cdadf1343d2457ee2730e47f73ff2a50d0ca3f44f",
  "observed_utc": "2026-11-27T21:34:20Z"
}
```
