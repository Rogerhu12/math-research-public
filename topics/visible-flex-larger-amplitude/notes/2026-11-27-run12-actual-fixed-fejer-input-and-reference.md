# Run12 实际两步固定 Fejér/R690 输入已完成；完整科学步骤已启动

## 1. 已实际取得的结论和边界

公开 Actions **46011377225/1** 的两个必要输入步骤均自然返回 `completed`、退出码 `0`。第一步按事先声明的七个有理配方的 RN-even binary64 像，生成固定 Fejér 图、全部 923 个确定性准确节点和完整 scalar 参数；第二步按预先固定的 **2218 叶**规则构造完整 R690 参考、全部 **7377** 个正径向观测及参考缓存。两步返回的数学目标身份相同：

`957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`。

这是新目标的实际输入构造成功。它没有证明完整 normal 场、方向、几何约束、全域度量、全物理时间或大幅非平凡性已经完成。参考实际报告明确保留 `physical_field_read=false` 和 `new_field_still_required=true`。其 `accuracy_reached=false` 也原样保留；预定 2218 叶的输入完成不等于达到请求的 scalar 积分误差目标。

在首次实际 **2026-11-27 14:04:28 UTC** 的索引中，后继完整科学步骤已经为 `running`，实际子进程 PID 3347，尚未自然返回。该时点没有进度文件的 `FileNotFoundError` 仅描述这一次有界只读观察，不是科学异常或首场失败。本文不据该观察填入任何场、接受步、最终点或数值指标。

## 2. 完整真实证据

完整公开紧凑分卷为：

`topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1-part-001.md`

- Git blob：`2daddb631388db54dd4309857297294c332faf1a`。
- UTF-8 字节：16600。
- SHA256：`5c093747e64ca227983e72590db4f5fc9bcc6fc950889504ee85edc8df30472a`。
- 两个完整实际记录中的 `summary_errors=[]`、`missing_outputs=[]`。
- 本文读取的是这一个 16,600 字节紧凑分卷；没有下载任何科学 NPZ、节点数组、地点列表或逐点报告。
- 完整命令、源码提交、所有输出身份以及清理记录已经在该固定 blob 中保存，下面再给出本结论所需的完整参数与文件表。

当时索引为：

`topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1.md`

- UTF-8 字节：7578。
- SHA256：`23164b3e8288800726a4cf2b1189cd2a8731e759aada5062231617cb0aa52756`。
- 状态记录时间：2026-11-27 14:04:28 UTC。
- 实际 job：140547455454，状态 `in_progress`，conclusion 为 null。
- 初始 workflow head：`ed9fbfec354330d11b0e46ef61a4d0565b88dfc6`。
- 控制器 SHA256：`e818a7c181b245da595d1089baa4bb1169a444c50083f3bdbe84182cc07e05ac`。
- 初始请求：`visible-larger-resume-20261127-12`，其完整原请求仍在索引，不用当前状态回写未来输入身份。

## 3. 第一步：实际固定配方输入

步骤 ID：

`prepare-complete-fixed-fejer-r690-inputs-20261127`

- 状态：completed；退出码：0。
- 控制器记录的完整子进程耗时：`5.893721085999999` 秒。
- maker 自身记录的工作耗时：`0.7868282550000032` 秒；两者范围不同，不互相替代。
- 实际源码提交：`97051366b05adc2a6aa27c845f712c5b79edfdff`。
- 完整源：`topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py`。
- 完整源 SHA256：`89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60`。
- 实际 schema：`complete-fixed-fejer-r690-input-preparation-v1`。
- 完整工作定义身份：`5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a`。
- 数学目标身份：`957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`。
- 实际所有输入、源、输出末次重核：`true`。
- maker 实际记录：physical F = 0，J evaluations = 0，normal roots = 0。

准确物理图参数是预先声明七项有理式经 RN-even binary64 转换所得的 dyadic 数本身；理想有理式只是设计和舍入比较的来源。其余 153 个初始 core 词为正零，不是旧优化结果。原变量布局仍只固定前三项，其余 157 个 core 自由量及全部 omega、H 自由量由后继完整求解器保留。

### 完整实际命令

以下为原实际命令数组，不以省略号替代参数：

```json
["/opt/hostedtoolcache/Python/3.12.14/x64/bin/python","-u","/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0001-167d7c1a5813-97051366b05a/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py","--repo","/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0001-167d7c1a5813-97051366b05a","--outdir","/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs","--panels","128"]
```

### 完整实际输出

| 实际 runner 路径 | 字节 | SHA256 |
|---|---:|---|
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/report.json` | 65332 | `255094e105fcddf87f35c326dce107f8524e83961bc21ee09153ba7af56aec32` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz` | 4334 | `b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json` | 144306 | `1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json` | 40488 | `2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189` |

其中 node JSON 大于 100 KB，本文只使用真实返回中的文件身份；没有整读其原始节点数组。源配方和全部参数已在公开源及 ready 中，数值输出继续只留 runner。

## 4. 第二步：实际完整参考构造

步骤 ID：

`prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run12`

- 状态：completed；退出码：0。
- 控制器记录的完整子进程耗时：`430.2165345` 秒。
- 参考程序自身记录的工作耗时：`427.003268214` 秒。
- 实际源码提交：`6e7fc7dc687960599e398087f9e1f574bdc2a738`。
- 完整源：`topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py`。
- 完整源 SHA256：`e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb`。
- 实际 schema：`R690-fixed-fejer-axisymmetric-SO3-preparation-v1`。
- M = 160，J = 923，P = 7377，N = 2048。
- 实际初始 H：`1.947054437068418`；H 是完整归一化 c 积分的既定初始值，并仍为后继自由变量。这不是最优值或已合格幅度。
- 实际前三固定词依序为 `0x1.c000000000000p-2`、`-0x1.3333333333333p-4`、`0x1.b6db6db6db6dbp-6`。

### 身份分层

| 真实对象 | 实际身份 |
|---|---|
| 纯数学目标 | `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9` |
| 完整工作配方 | `5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a` |
| 当前完整参考模型 | `ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac` |
| 完整参考定义 | `50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319` |
| 固定 scalar 定义 | `d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160` |
| 完整 scalar 参数投影 | `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` |
| 实际完整 chart 数组 | `af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103` |
| 实际完整 working mesh 数组 | `ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc` |

这些身份承担不同责任。尤其纯数学目标不包含本次任意执行时间，也不能把完整 reference、whole NPZ 或运行证据的摘要冒作仅数学对象的身份。此新图、新 mesh 未声称与旧 warm 选择的 g 相同。

### 实际 scalar 范围

- 预定叶目标：2218；实际叶数：2218。
- `whole_tail=true`。
- `unresolved_tail_dropped=false`。
- `clock_selects_leaves=false`。
- `accuracy_reached=false`。
- 原实际完整误差宽度字串：

`20705780131163723599438290019541571913013106551525357578680931811765776678181/14411518807585587200000000000000000000000000000000000000000000000000000000000000000000000`

该字串保持实际报告原值，没有在本地重新执行积分、估计误差或把宽度舍去。准确完整 R690 标量定义与工作近似/包围分别保存；输入完成不将未达到的请求精度补成 true。

### 完整实际命令

```json
["/opt/hostedtoolcache/Python/3.12.14/x64/bin/python","-u","/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0002-a73af5287d15-6e7fc7dc6879/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py","--repo","/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0002-a73af5287d15-6e7fc7dc6879","--fixed-input","/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz","--fixed-input-report","/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/report.json","--node-report","/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json","--scalar-input","/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json","--manifest","/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0002-a73af5287d15-6e7fc7dc6879/topics/visible-flex-larger-amplitude/scripts/resume_20261120/a04_historical_location_seeds.json","--outdir","/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference","--angles","2048","--seed-integration-order","8","--panels","128","--scalar-leaf-count","2218","--scalar-integral-tolerance","1e-18","--scalar-tail-cutoff","1/8"]
```

### 完整实际输出

| 实际 runner 路径 | 字节 | SHA256 |
|---|---:|---|
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/report.json` | 84966 | `a35e7ed22d3453d69cc746ff6b706735717bb74131d43ece0b7ddda440403900` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/reference.npz` | 894879 | `212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/observations.npz` | 205842 | `84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/locations.json` | 106771 | `ba4cd7ba201044b950dab70f4ea5606d79a6202c8ef5b534bb4a611d014eb5a7` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/supplied-location-provenance.json` | 223955 | `e5526478ae6f6e6a141ebdb67636e4231f37862bb5b5b260c09c5830f0ade329` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/fixed-target-definition.json` | 30919 | `777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df` |
| `/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json` | 35712 | `a6992516e83b53e153bf5d2b9ef8985f7542bff615e2b3edd6e467a2d105f52b` |

所有七个指定输出实际存在；没有用缺失文件的推测值替代摘要。报告为 84,966 字节，binding 为 35,712 字节，whole reference、carrier、locations 和 provenance 的实际原文件仍留 runner。本文只从公开紧凑返回读取其身份。

## 5. 真正绑定与历史的语义

实际 binding schema 为 `complete-fixed-fejer-actual-reference-binding-v1`，返回 `all_six_actual=true`，其六个实际文件指向本次真实 fixed input、node、scalar、carrier、preparation 和 reference。数学目标、完整 reference 定义、source commit、实际 run/attempt 与参考主报告相同。

原 ordered 十一 payload 仍由完整 source 消费。由于新确定性节点并非旧 BVP 节点，旧 literal cell/u/phi 在新目标和真实当前 carrier 上明确重新解释；没有声称同一个准确 s、同一个物理点，也不迁入旧场值、旧根或旧几何证书。实际报告字段为：

- `old_warm_not_required=true`。
- `old_surface_used=false`。
- `old_directions_replayed=false`。
- `old_certificates_inherited=false`。
- binding 的 `old_values_or_unknown_history_inherited=false`。

旧分支未完成责任和未消费的 typed/末点责任继续保留，未知不能被该新目标的两个输入成功改写为空历史或旧题完成。后继仍要在新目标上支付完整全域几何、所有材料地址和物理时间责任。

## 6. 科学启动的实际证据与待返回项

实际索引当前阶段为：

`followup:complete-fixed-fejer-immutable-point-first-20261127-run12`

其实际进程记录：

- science source commit：`a3df4eae39988724cca2cc3c38927e583c24eb2e`。
- 执行 launcher 全 SHA256：`0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf`。
- PID：3347。
- child_exit_code：null。
- child_natural_return_not_observed：true。
- 观测时间：2026-11-27T14:04:28Z。
- 对应观察身份：`a1f40e8b7398c186abc7177e5bb198387381b9015a76b185e8e0c037393bd3e3`。
- 该次 `observations={}`；进度文件尚不存在只作为真实读取边界保存。

完整四步骤队列已经包含 maker、reference、原全空间科学以及纯读；输入两步骤未被替换或截短，`finish_when_done=false`。科学和纯读完整参数分别为 153 与 7 项，数值预算、32 个 normal stage、全部变量、所有 nonlinear screens、旧逐 stage/final 强制重读和新 immutable owner 守卫都沿已刊完整源。本文没有新增执行前门，也没有改动正在运行的子进程。

下述稍后的实际观察仍未见该科学步骤的自然返回、纯读最终报告或完成数值结论。实际场、末点、被接受方向、度量/几何指标、精化差值和所有准确费用均须以后续真实报告为准。

### 后续真实进度：14:09:28 UTC

随后完整读取了 14:09:29 UTC 索引的固定 Git blob `e79f82059497161c9ce6b94e026087caf005ceb4`，9634 UTF-8 字节，SHA256 `6216c097c10184960db7435f93bdde6a8bb180b9c14c566f5aa6fe207cb237f3`。其有界观察时间为 14:09:28 UTC，读取的实际 progress 最后写入时间为 14:09:27 UTC。该小文件两个完整读取一致，3296 字节，SHA256 `594af9df3abb359e0404ea5bc5e5df9fc69c190f8f7601b793a06f0708ca383a`。

此时真实 `normal_chain_enter` 已有 point `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`，完整请求/返回各 29640，原式尝试/返回各 6890，缓存命中 22750，已记录 failure 和 binding failure 都为 0。实际 immutable key checks 为 23205，whole point word checks 为 391；entry/exit 为 196/195，尚有一个活动 scope。原 closure 时间为 98.69234995399972 秒，绑定和 key 时间为 5.847501323000529 秒。这些是本次实际计数与分项时间，不是跨算法加速比，也不表示整个子进程已经完成。

这里保留完整有界观察对象，避免把累计计数、尚未完成的 scope 或瞬时阶段改写成最终结果：

```json
{"step_id":"complete-fixed-fejer-immutable-point-first-20261127-run12","scientific_source_commit":"a3df4eae39988724cca2cc3c38927e583c24eb2e","scientific_source_sha256":"0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf","pid":3347,"observations":{"fixed-fejer-immutable-point-first/actual-normal-evaluation-progress.json":{"phase":"normal_chain_enter","at":"2026-11-27 14:09:27 UTC","point":"7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47","stage":null,"scope_order":2,"scope_angles":1,"cached_angle_roots":578,"observer_scientific_calls":0,"scientific_complete_inferred":false,"closure_logical_requests":29640,"closure_logical_returns":29640,"closure_logical_failures":0,"closure_original_attempts":6890,"closure_original_returns":6890,"closure_original_failures":0,"closure_original_angle_jet_requests":95574,"closure_original_angle_jet_returns":95574,"closure_cache_hits":22750,"closure_cache_hit_angle_jets":216636,"closure_cache_misses":455,"closure_forced_original_requests":6435,"closure_forced_stage_rereads":6240,"closure_forced_endpoint_rereads":195,"closure_bypass_no_scope":0,"closure_bypass_caller_environment":0,"closure_bypass_current_environment":0,"closure_bypass_tensor_or_data_tracking":0,"closure_bypass_optional_failure":0,"closure_binding_failures":0,"closure_key_checks":23205,"closure_point_word_checks":391,"closure_stored_values":455,"closure_optional_cache_failures":0,"closure_scopes_started":196,"closure_scopes_closed":195,"closure_scopes_with_exception":0,"closure_scopes_disabled_at_entry":0,"closure_scope_stage_completions":6240,"closure_progress_writes":395,"closure_progress_write_failures":0,"closure_progress_events":395,"closure_peak_cache_entries":3,"closure_peak_cache_bytes":3264,"closure_immutable_point_entry_checks":196,"closure_immutable_point_key_checks":23205,"closure_immutable_point_exit_checks":195,"closure_original_closure_seconds":98.69234995399972,"closure_binding_and_key_seconds":5.847501323000529}},"complete_small_progress_file_identities":[{"path":"fixed-fejer-immutable-point-first/actual-normal-evaluation-progress.json","bytes":3296,"sha256":"594af9df3abb359e0404ea5bc5e5df9fc69c190f8f7601b793a06f0708ca383a","two_complete_bounded_reads_agreed":true}],"observation_errors":[],"child_exit_code":null,"child_natural_return_not_observed":true,"observations_are_not_a_completed_step_or_a_scientific_certificate":true,"observation_identity_sha256":"37442ef78a2b02dee34e4faf9f9f07a256275256b8336bbab6a3a0ea8cdd606b","observed_utc":"2026-11-27T14:09:28Z"}
```

没有从缓存数量推断全角或完整场已经可行，没有从某一 point 摘要推断该点被接受，没有将进度读取当作新的 F/J/root 计算。

## 7. 本次读取和记录的范围

本次只解析公开的小索引、小分卷及 jobs API 元数据，核对完整实际原字段、参数和身份。未执行本地科学、AST、编译或缩小 fixture；未更改 refs、队列、正在运行的源或参数；未将大 raw、节点/场/矩阵数组复制入 Git。本 note 是两个实际必要输入结果和一个实际已启动进程的记录，不是新数学证明或求解完成声明。
