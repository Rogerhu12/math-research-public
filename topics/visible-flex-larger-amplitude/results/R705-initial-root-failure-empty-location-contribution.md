# R705 — 三份精确初根失败报告的空物理地址贡献

**状态：已证明（仅对文中精确源、完整字段闭包和已实际确认的三条停止分支）。**

本文件按根README3、8、12正式登记已有完整证明；没有重做科学计算或把旧结论算作新进展。[原完整笔记](../notes/2026-11-26-initial-root-failure-reports-have-no-physical-location-payload.md)保持原字节（SHA256 `d1e64cf4da2dec5f3a11d3c225da204ed03225cf92398ade82af93f9853bb64e`）。原文中实施/运行状态以其记录时点理解；当前真实结果见[HANDOFF](../HANDOFF.md)。没有将条件界、失败或数值证据升级为所求闭族的存在证明。

日期：2026-11-26。此文只证明三份已实际返回的失败报告对已刊 `4d9` 物理地址 walker 的贡献为空，并据此说明新 runner 的完整历史再生可省去这些**无地址贡献**的失败求根步骤。它不删除其来源和失败结论，不把摘要计数相等当集合证明，也不声称其他报告、其他失败位置或一般零端点求解都无地址贡献。

## 1. 命题及准确范围

设 $W(R)$ 为完整 `launch_refinement_from_full_report.py` 的 `Locations.walk(R)`、再按实际 carrier 执行 `resolve_grid` 所产生的曲率、半径和 protected 曲率地址三集合。固定完整源码 SHA256：
`4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`。

对 run `45820592817/1` 的下列三份实际报告，逐项由已绑定完整源码和实际停止分支可得
$$
W(R_{28})=W(R_{34})=W(R_{36})=(\varnothing,\varnothing,\varnothing).
$$

| 实际报告 | 完整 driver SHA256 | 实际报告 SHA256 |
|---|---|---|
| 28：同端点 residual continuation | `9649ed99b614c468258646145948d7c06feb356c72806c73727728ea498ed88e` | `a2442ccad906f5fbc473376c5bd1644328235ae484ba8bebfcd8e4fa3019d335` |
| 34：只改初始 H | `34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3` | `75b868c7b8bd7b3f79950f26700a2ef7190c61195530f7043a34831e216dc1a8` |
| 36：新 gamma 六控制九维 KKT | `5134d34d4f4393fc57d86eed329bd107b631b693668d1d04d602af5f286dc3f5` | `b154a2399af7c2b36273c853c3b0eecab03bfb60e22ee47a87f24b23820eca9e` |

实际 stop 都是 `actual_initial_zero_closure_field_read_failed`；原因是端点根求解/延拓失败。实际 28、34 的纯 reader 已成功返回；实际 36 的科学报告已返回，纯 reader 尚未准入。该最后一项不妨碍由完整初始失败保存分支验证字段结构，但不补造其未读角状态或根值。

这与“原内存为空”不同：三次运行起始实际分别继承了 1763/1763、1851/1851、1851/1851 个物理地址。只是这类失败报告不把既有内存数组重新序列化为新来源，且失败前没有发现新的几何地点。地址集合必须仍由其前序真实完整报告继承。

## 2. walker 唯一会生成地址的入口

完整 4d9 的 `walk` / `tagged` / `put` 只在下列结构生成地址：

1. 同一个 dict 同时含准确键 `cell,u,phi`；
2. 同一个 dict 含准确键 `stage`，并含 `phi` 或 `angle`；
3. 长度准确匹配的 tagged 数组，其第一个元素为 `grid`、`grid_radius`、`arbitrary`、`arbitrary_radius`；
4. 名为 `curvature_points`、`radius_points`、`protected_curvature_points` 的物理三元数值数组；
5. `protected_current_representatives` 路径下的三元 `seed` 或 `current_location`。

`fixed_core` 和 `cap_height` tagged 值明确只被识别为固定直径替代项，不生成物理地址。普通字符串不被再次 JSON 解析。键名中的 curvature/radius/worst 只改变后续地址的角色，不凭一个计数、哈希、方程字符串或角向索引生成地址。一般三维向量、九维状态、3×3/9×9 矩阵及三节点支撑列表都不能单凭长度变为物理三元组。

因此证明须排除上列完整识别结构，不能仅搜索字符串 phi，也不能只比较位置计数。

## 3. 完整 driver 的保存分支

三个完整 driver 的初始执行顺序都是：
`native = q.residual(x)`，
然后 `statistics(x,native)`，
最后 `geometry = scan(x)`。

实际端点根失败来自首次 residual 读取，进入 except 后只增加 complete=false、stop/error、`initial_endpoint_roots`、耗时和 failed-candidate 标志，然后 `save_report()` 与 raise。不存在后续 current scan、C 构造、QP、trial、remember 或新场保存。这些事实同时由根失败的实际 source/reason、成功根数为零、无 initial field/Phi，以及完整源的严格顺序支持；不是用旧场几何值来推断。

`save_report` 仅增加：

- 完整 `q.metadata()`；
- 当前曲率/半径**计数**；
- RSS 计数。

在初始失败前，`metric_directions` 与 `restoration_directions` 都是空列表。`final_curvature_memory` 和 `final_radius_memory` 只在自然完成循环后的末报告分支写入，该分支没有执行。当前 witness/radius 列表没有被 `save_report` 隐含复制。

`all_locations` 的返回元数据 `history` 只有来源**文件记录**、before/after 计数、extraction_paths 的字符串键及计数、resolved 个数和 scope 文字；没有复制原 payload 或物理地址数组。文件记录只是 path/SHA/bytes，不由 walker 递归读取那个路径上的原文件。因此失败报告不能替代原所有输入报告，更不能据其中的 count 还原地点。

## 4. 初报告的其余来源闭包

其余初始字段由以下完整来源产生，逐项不含第 2 节的识别结构：

| 字段族 | 完整生产与检查依据 |
|---|---|
| 来源/输入/历史文件记录 | driver `file_record`、`actual_reference`、`all_locations`：只有 path、SHA、bytes、标量状态和计数，不复制文件正文 |
| reference context / base model | 4e 完整 reference、7f 完整 base：固定定义、shape、哈希、固定三个 core hex、方程字符串和 scalar 包围；无 node/query 地址表 |
| 固定 scalar definition | e091 `DeepValleyTail.definition`：exact 常数和公式、input SHA；其键 angle 是公式字符串，所在 dict 无 stage |
| FullHold / derivative metadata | a1ed FullHold.metadata 和 4e WholeAxisymmetricLaw.metadata：整数/有理包围、参数、误差和调用计数，无 cell/u/phi 或 tagged 点 |
| 坐标范数 | 7f `RotationH2Coordinates.record`：公式、全变量标志、各矩阵/权的 hash、阶数/带宽；无物理地点列表 |
| 幅度预算、谱参数、运行配置 | 标量预算、μ、p/epsilon/scale、source/version 和 support 三节点字符串；没有物理三元入口 |
| H-only 新字段 | 34c `explicit_height_seed` / `initial_point_record`：字面 H、准确有理值、整点/非H前缀 hash、shape、索引和标志；不复制自由变量数组或空间地点 |
| restart / direct seed | 三次实际 argv 均未使用这两种模式，相应初报告字段为 null |

这里使用的 reference source 为
`4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`；
base source 为
`7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf`；
scalar source 为
`e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`；
FullHold source 为
`a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670`。

### 固定 Q 输入不是隐藏的原 trace

三次实际 argv 都采用完整已刊 3618 bytes 的小参数文件
`frozen-zero-moment-Q-actual16-parameters.json`，SHA256
`df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c`；
没有使用重新读取 runner trace 的分支。

完整 binder `4dc3e1a8ba8f128e1d05176f4d0f4b18c62d278fed603cc46f7ed686f6e4e611` 的 `from_parameter_file` 在验证真实字节和 definition 后原样返回该文档。文档只有 18 个 hex 控制参数、两组准确三节点字符串、输入/模型 hash 和紧凑 provenance。provenance 中 stage=15 或 16 的 dict 不含 phi 或 angle，不能与其他 dict 中的角公式“拼起来”触发 walker。它没有原 trace 原文、物理试步记录或地点表。`moment_input_record` 也只保存该文件记录及来源模式。

## 5. 根 metadata / snapshot 的闭包

完整根来源分别为：

- 44ac 固定 Q operator：`44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e`；
- 3f continuation operator：`3f37789f1624b97cb7f83b1795ac5fe96be3b3026d4078115078f12e8fd4e34a`；
- b712 gamma/KKT operator：`b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a`。

初短 snapshot 只是完整 metadata 的明确键子集（gamma 是完整已声明 ROOT_SNAPSHOT_KEYS）。actual_initial_read_error 是 repr 字符串，walker 不再次解析其中 JSON。

44ac 的失败对象只有 source/model/整点 hash、失败角索引、残差/控制最大值、policy 和标志。3f/b712 的延拓摘要使用 `material_angles_binary64_hex`、逐角计数、final_parameters；批记录使用 `batch_stage` / `angle_records`，角记录键为 `angle_index`，并非 walker 的准确键组合 stage+angle。

b712 中失败矩阵快照以 `local_angle_index`、`newton_iteration`、`continuation_parameter_target`、九维 state/residual 和 9×9 matrix 描述代数根问题。它既不含 cell/u/phi，也不是命名的物理三元列表。普通 omega/root 状态向量和角根控制不能被解释成表面地址。

完整 q.metadata 的递归 base/model/reference/scalar 部分已由第 4 节闭合。于是对所有初报告字段按 JSON 树归纳，walk 从不进入 put/grid：三集合确为空。该结论是完整结构证明，不是未做的原报告执行日志，也不是计数相同的替代论证。

## 6. 对 05 完整再生和后继的具体影响

设 $U$ 是实际前序完整 location manifests 的三集合并集。对这些精确失败报告，
$$
U\cup W(R_{28})\cup W(R_{34})\cup W(R_{36})=U.
$$
因此新 runner 若完整再生 reference、3、17、21、26、30 的真实来源，可以明确不再为取得这些空地址贡献而重跑 28/34/36。保存原失败报告的 SHA、源码、完整参数和已登记失败结论即可；**不造不存在的新报告文件，不把原 SHA 当文件，不把旧 raw 重新包装为参数**。

新 30 重建参数由原完整第 30 步对象派生时，唯一移除的科学参数对可明确为
`--manifest {work}/zero-closure-frozen-moment-Q-continuation-first/report.json`。
其余同目标、完整空间、父 restart、范数、μ、QP、全部 C/真实筛、完整输出和 cleanup 不变；新的 id/scope 说明本 run 实际输入，不钉旧返回数值。原 28 的失败 provenance 另保留于完整派生说明。

后继 H+gamma 的适用完整 manifest 为 reference locations、3、17、21、26、30 六份实际新 runner 文档。新运行若已产生其他几何 trial 或新完整报告，则还须并入其真实贡献；本命题不自动豁免将来失败。

这些新返回不能仅因同命令就冒称逐字复现了旧场、旧结果或旧永久点集合。03b 纯 fingerprint 尚未执行，原逐点 raw 没有从公开摘要重建；新 runner 的 exact 地址 hash/count 应真实读取并独立记录。这一限制不影响已经证明的三份精确初失败报告贡献为空，但不能扩张为所有历史来源相同。

## 7. 未扩张的责任

本文不使用或转移任何旧几何数值/连续证书，不改变目标 g、原自由变量、原全部 metric 行、全 C 或验收阈值。它不对已经运行过 geometry scan、C 构造、trial 或 SOC separation 的失败报告作空集断言。实际 17、21、26、30 的完整报告仍必须作为完整历史依赖，不能用末内存摘要替换。
