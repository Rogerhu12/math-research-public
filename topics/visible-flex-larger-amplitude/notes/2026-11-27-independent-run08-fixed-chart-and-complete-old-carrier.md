# 2026-11-27 run08：完整冻结当前材料角目标并保留旧、新材料地址责任

## 1. 本次选择与实际依据

本入口选择一个明确独立的固定目标：真实 run08 的全部 160 个固定 chart 系数，连同同次完整 R690 scalar 参数、精确符号节点、reference model 和 reference bundle。历史 chart 保留其原身份；不再声称当前完整 chart 与旧 chart 相同，也不声称已经支付两者之间的准确角坐标共轭。

这不是把旧 chart 常量改成一个新的值后继续使用“同一个旧 g”的标签。新 producer 生成完整目标 definition、完整输入 binding 和各自 canonical identity；后继必须使用独立、完整、严格绑定这些新字段的 memory/entry 源。旧 source、旧分支、已经返回的失败及其适用历史责任全部保留。

实际 run08 为 45929088658/1。完整公开第一卷为 [实际 warm/preparation 返回](2026-11-27-public-actions-45929088658-1-part-001.md)，50,445 字节，SHA256：

`0f553795b9072d027c0b91832916d7daf91ebd61079fd0e76207cacf7cc2accc`。

本段列示第一卷身份时应以完整实际卷核对；producer 不使用手写说明替代完整真实返回。它在运行时按真实 GITHUB_RUN_ID/ATTEMPT 定位本卷、核整文件和唯一实际 preparation/warm 记录。以下表中所有文件身份均由已经返回的实际记录得到。

| 输入 | 当前完整 SHA256 |
|---|---|
| warm bundle | `4c34e0889a40e67a3a0a38abce030bb0358f74333fc1d8c95f669d5beefd9a0f` |
| symbolic node report | `d7cac2c479defda89980c916f967353f5d1ac27f1c85cb93b37268972a4876d3` |
| scalar gzip | `87bd2a4668638dbd49ec4523b33941c554b06471d1cf0ba522d3ea2a9a36ddb5` |
| preparation report | `4a3357f5daf16a08c267353d6c9064994c4de36b7d65e742ffde24f7ac8c8e10` |
| reference bundle | `eeb55084744c60a5ed2e2bbb4343b01c73028a6ab61b1216142e4b3bf57dd6b4` |
| current observation carrier | `56b143f1ac7031b5cbeb12d02240fca28a67a57eba9938d5f134e4a1e7094d44` |
| current full reference model | `492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e` |
| current full mesh array | `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262` |
| current full chart array | `7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48` |

旧完整 chart 为
`90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e`。
准确 scalar 参数投影仍为
`e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`。

原 8c1e restorer 先因错误要求当前 whole warm 等于历史 3df 而失败。随后完整 6cc 修复已真实运行，在第 6 步用 6.137976809 秒诚实拒绝 whole mesh/chart 不一致；其失败报告 4,407 字节，SHA256
`87573603d6bc53ff720ceaeb76114dc6f8b1df130d6d6dab5946ce4818c41045`。
第 9 步纯读取实际完成，直接从真实 preparation definition 确认 mesh 仍是原 eff967，而 chart 真为新 7c4c。纯读取输出 8,083 字节，SHA256
`4c3bbbff7f13ec801d8300c58c2d45c6feb8fc786d9a2cb3de9f752a395c61ec`。
第 6–9 步的完整返回已保留；对象摘要曾被 scalar-only controller 拒绝的四项也保留为实际 summary errors，不写成完整对象已公开。

## 2. chart 差异不是 hash 或 slice 接错

[完整 4e reference source](../scripts/resume_20261126/so3_axisymmetric_reference.py)
SHA256 为
`4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3`。
它确切提取：

~~~python
core = np.array(warm['qjets'][0, 0, 1:161], copy=True)
~~~

其 array digest 顺序为：

~~~python
value = np.ascontiguousarray(value)
h = hashlib.sha256(str(value.dtype).encode())
h.update(json.dumps(list(value.shape)).encode())
h.update(value.tobytes())
~~~

原 c79 envelope 的完整 core 摘要使用相同 dtype `float64`、shape `[160]` 与全 160 个字节序列；不是只取前三项，也不是省掉 dtype/shape 的 raw SHA。新 6cc 也对这个相同 slice 调原 4e 函数。因而本次真实 7c4c/90e6 不等不是摘要格式或索引错误。

旧完整 160 个系数不能从一个 SHA 反推。已读原 warm/pulse/continuation 源表明，前缀求解会更新前三项之外的自由 core；只在 boundary 固定前三项。现有小 model/报告只保存完整 core 摘要及前三个词，不能从共同初始 source 或 accepted099 的某个早期 core 猜出旧末状态的全 160 个词。本版不伪造这份缺失输入，也不把末位差异豁免成“等价”。

## 3. 新目标的准确范围

新 `fixed_target_definition` schema 为：

`independent-run08-frozen-complete-scalar-and-material-chart-v1`。

它完整保存如下内容，所有摘要均由对应完整内容重新计算：

- 本次全部 current reference model 与其 canonical identity。
- 本次 whole reference bundle identity。
- 本次完整 scalar 参数投影及其 e640 identity。
- 本次完整 fixed scalar profile definition 及其 identity。
- 全部 160 个 canonical、有限 binary64 hex chart 词。
- 同一 160 词的 dtype、shape、little-endian 全数组 digest。
- 全部 923 个准确 affine-in-S 节点的两个 Fraction 字串及整体 identity。
- 原 node recipe source、完整 literal mesh digest 和 literal width。
- 明确的独立 target 与旧历史责任范围字段。

`chart_words_record` 对每个 hex 先解析成有限 float，再要求 `value.hex()` 恰等原词；用 `struct.pack('<d', value)` 逐个组装完整 160 词，并按 4e 原 dtype/shape/byte 规则核 7c4c。不会只核数量或前三项。

给定同一个准确 R690 标量函数 $a(s)$ 和这个完整固定材料角图 $\Theta_{\rm current}(\phi_0)$，本入口目标为

$$
g_{\rm current}=ds^2+a(s)^2\,d\Theta_{\rm current}(\phi_0)^2.
$$

后继当前 free core 和 free H 不重新定义此目标；它们继续是原完整表示中的自由变量。固定 chart、scalar、准确域和 reference seed 先由真实输入冻结，然后才允许评估新物理场或求解方向。

本入口明确保存：

~~~text
same_original_fixed_chart = false
same_mathematical_g_claimed = false
exact_old_to_new_chart_conjugacy_claimed = false
same_historical_physical_points_claimed = false
old_field_values_or_scientific_certificates_inherited = false
original_branch_replaced_or_declared_finished = false
~~~

即使两个严格单调材料图有可能描述可比较的物理度量，本版没有完整旧 160 词，也没有支付准确共轭的输入、导数与地址运输责任。因此不会使用那个尚未给出的结论。

## 4. 为什么仍可尝试完整旧 dc5 carrier

旧 complete observation carrier 的数值内容不包含全部 160 项 chart。原 producer 最后只保存固定前三项，并且 plan/a/误差构造由原 mesh、width 和准确 scalar 决定。这里区分“整个旧 carrier 的实际字节能否重建”与“当前完整 chart 是否等旧 chart”。

原 bee5 warm 的十个成员全部真读并记录；其中 whole H 和大部分 qjets 不进入旧 observation carrier 的数值计算。新 producer 仍核：

1. 全 923 mesh 的 eff967 digest、形状、有限性和严格增序。
2. 全 qjets shape `(923, 3, 482)`；完整当前 core shape160 与当前 7c4c 身份。
3. 当前 core 前三项与 warm `fixed_core_first3` 逐字相同。
4. width/radius/H 的真实 scalar dtype 与 shape；width 仍原 literal .05。
5. 原 FullHold 与当前 mesh endpoint、warm radius 的关系。
6. 全部 923 个准确 affine node definitions 与真实 node report 逐项相同。
7. 完整准确 scalar 参数投影仍 e640。

之后保留原 deep integer/Fraction 算术、heap 次序、2397 个 live leaves、无限尾和原 accuracy 状态；保留完整 order6 plan、7377 个 observation 值/误差/time error、原 `np.savez_compressed` keyword 次序、所有 dtype 和 array 内容。

只有候选 whole file 同时满足：

~~~text
SHA256 = dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0
bytes = 227202
~~~

才输出可供后继使用的历史 carrier binding。原 historical public record 的 whole SHA、原 2397 证据、准确参数和 source closure 全部仍硬核。当前 warm/scalar/node 不会被改标为历史 SHA。

这是一个尚待 Actions 真执行的完整重建输入。当前新 chart 不等旧 chart，既不能推出 carrier 必不同，也不能推出 carrier 必相同。任何剩余依赖或压缩工作字使 whole dc5 不匹配，都必须产生真实 failure。此 source 没有偷偷切换至地址 packet、采样 oldG、忽略某个数组或按“数值接近”接受的 fallback。若 whole dc5 实际失败，完整 old-address packet 必须用另一完整 source/definition 单独实现并保留这次失败。

## 5. 全部历史地址如何保留

历史载体在此仅提供完整材料地址责任。后继仍须对新场真实读取：

$$
E=P_0\cup G_{\rm old}\cup G_{\rm current}.
$$

`P0` 是已提供完整历史 payload 的有序/保护/容量位置并集及本次真实准备位置；oldG/currentG 是完整旧、新 observation 径向地址与完整角格。所有原两类几何、两个 principal-curvature branches、signed witness 条件、原永久真筛与 Phase I 责任保留。未知 parallel 任务的 typed 发现顺序、首次发现点、晋升保护与来源不能从全格覆盖或计数反造；当其真实返回可取得时，仍需完整绑定并迁移地址/类型/来源，再在新场重读。

当前 literal $(cell,u,\phi_0)$ 用新冻结 chart 解释，不声称它与旧场上的物理点相同。这个区别记录在完整 definition 中。旧 Phi、Gram、曲率、reach、root、选支、最小范数性质和连续证书都不迁移。

本 producer 不实现或削减后继 envelope 策略；完整新 memory/geometry/driver/reader 必须显式核新 target，并保持其全地址及 typed 政策。只加载新 producer 后把旧 90e6 guard 改成 7c4c、不保存上述新 definition 和语义，不满足本接口。

## 6. 固定输出与完整 validator API

新完整 producer basename：

`freeze_run08_fixed_chart_and_restore_run05_carrier.py`。

输出目录必须是全新、repo 外的 runner 目录。建议：

`{work}/run08-independent-chart7c-run05-carrier`。

成功输出恰包括以下完整文件；失败也先保存真实 report：

| 文件 | 用途 |
|---|---|
| `report.json` | 全来源、全部当前 warm 成员、实际历史重建与新目标声明 |
| `run05-observations-restored.npz` | 经 whole dc5/227202 核定的全部旧 carrier |
| `independent-fixed-target-definition.json` | 完整 160 词、全部参数/923节点/model/reference 定义 |
| `material-envelope-carrier-binding.json` | 独立新目标与旧、新载体、真实当前六文件的完整绑定 |

binding schema 为
`material-envelope-independent-fixed-chart-binding-v1`。

binding 顶层保存：

~~~text
independent_fixed_target_binding
independent_fixed_target_binding_identity_sha256
fixed_target_definition
fixed_target_definition_identity_sha256
origin_carrier
current_carrier
producer
original_full_carrier_sha_verified
original_reference_report_sha256
actual_current_reference_report
actual_cells_and_u_equal
consumer_must_rehash_and_read_complete_arrays
surface_history_values_or_certificates_inherited
~~~

inner binding 的 schema 为
`independent-current-chart-and-historical-carrier-input-binding-v1`。
其 `fixed_target_definition` 和 identity 必须与顶层逐项相同。

纯 stdlib validator 的准确签名为：

~~~python
validate_independent_fixed_target_binding(
    value, *,
    actual_model,
    current_carrier,
    current_preparation_report,
    current_reference_bundle,
    current_node_report,
    current_scalar_input,
)
~~~

五个 file 参数均是调用方从真实当前路径计算的完整 file record；warm record 在 value 内另真读。完整六 current record 键保持：

~~~text
current_warm_bundle
current_node_report
current_scalar_input
current_carrier
current_preparation_report
current_reference_bundle
~~~

validator 重新核六文件、真读完整 preparation/node/scalar/public evidence，核 current model/reference/schema/source、完整 e640 参数、全部 923 准确 node definitions、160 词与目标 canonical identity，并再次核完整历史 dc5。目标、输入 binding 和 producer 完整 SHA 分别绑定，不能用布尔、shape 或计数代替字节身份。

返回字段包括：

~~~text
schema
producer_source_sha256
independent_fixed_target_binding_identity_sha256
actual_current_model_identity_sha256
actual_current_warm_bundle_sha256
historical_warm_bundle_sha256
current_and_historical_whole_warm_equal
historical_whole_warm_or_height_equality_claimed
complete_scalar_parameters_sha256
current_mesh_sha256
current_fixed_chart_core_sha256
historical_original_chart_core_sha256
fixed_target_definition_identity_sha256
independent_fixed_target
same_original_fixed_chart
same_mathematical_g_claimed
exact_symbolic_nodes_sha256
historical_carrier_sha256
historical_carrier_bytes
whole_old_carrier_and_full_current_input_bytes_rechecked
same_complete_scalar_formula
complete_current_fixed_chart_verified
all_historical_and_current_material_addresses_still_required
scientific_certificates_inherited
~~~

新的 consumer 必须核整 producer source，然后调用该完整新函数。旧 `validate_current_input_compatibility` 名称不在新源中；旧 `compatibility_identity_sha256` 和“同完整 scalar + fixed chart”返回语义不迁移。pure reader 也应重新读真实 preparation definition、传实际五 records、核新 target 与输出一致，不把 report 自报 flags 当完成证据。

## 7. 完整原参数与执行边界

本次只新增一个完整 input producer step。已返回的 warm 和 reference 不重跑；也没有提前假定新场、root 或方向已成功。

准确全 argv 见独立 ready；核心为：

~~~text
python -u freeze_run08_fixed_chart_and_restore_run05_carrier.py
  --repo {repo}
  --warm-bundle {work}/fullclosed_solver/data/fullclosed-hold-warm.npz
  --node-report {work}/fullclosed_solver/data/fullclosed-hold-warm.json
  --scalar-input {work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz
  --current-carrier {work}/axisymmetric-R690-reference-v2-first/observations.npz
  --current-reference-report {work}/axisymmetric-R690-reference-v2-first/report.json
  --historical-public-record {repo}/topics/visible-flex-larger-amplitude/notes/2026-11-26-public-actions-45870334713-1-part-001.md
  --outdir {work}/run08-independent-chart7c-run05-carrier
~~~

当前 public-record 路径由本 run 的实际 environment 构造；若显式传入该 optional 参数，仍要求恰是这个真实 run/attempt 路径。不会借 run07 volume 或 run07 currentcarrier 身份。

旧完整参数仍为 panels128、seed order8、观察 order6、角2048、tolerance `1e-18`、tail cutoff `1/8`。历史300秒是原实际生成时的准入参数；此再生使用已返回的2397叶完整状态定义，不能把它叙述成再次靠300秒猜相同叶数。

source 的科学入口强制 public Actions。纯 validator 不 import NumPy/Torch/SciPy，不调用 F/J/root；真正 carrier 重建使用原完整科学模块，只在 Actions 中运行。新 scope 记录 `physical_field_evaluations=0`、`Jacobian_evaluations=0`、`root_evaluations=0`，不把 input integration 与根求解混淆。

## 8. 完整源、再生器与实际验证状态

完整新 source：

- 61,371 字节。
- SHA256 `105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361`。
- 已实际上传的完整未引用 Git blob `31afc348592c208cfc731591900788dc91ea3bd7`。

纯 stdlib 全再生器 `derive_run08_independent_fixed_chart_input.py`：

- 20,113 字节。
- SHA256 `657c1f5001639f44f4a9d35d7057115b6f94da05c4aecdec2e363fb525374a94`。
- 完整远端 blob `9168bc7bbf4cd22a08935d4ab3851676bdd6729c`。

它核完整父 6cc source，应用全部精确行段，核完整新 SHA/bytes 与原数学片段；可用 `--verify-existing` 核已存在完整 source。再生器包含 AST/compile 检查，但本次环境不可用，没有运行 Python，也没有本地 scientific import 或 fixture。已经实际完成的是 functions JS 中完整文本重组/全 SHA 及下表逐字检查。

| 原体 | 字节 | SHA256 |
|---|---:|---|
| `exact_node_definitions` | 1220 | `f07d88dad55057c01e6bde1db4552299c3ec9f23e6a6ff8ac4417947b404c004` |
| 完整 `counted_tail_class` | 3159 | `9d160a25523b17f46fea1a4096ca43572eca5dfa0c1b396c93f4979b8a502dae` |
| member comparison/array records | 367 | `5a1ef1b963e3d8f46369d35ba2787bb28c03edfb0cf94a8ca2a3b2df89cf862d` |
| 原 deep/2397/radius/plan/7377/save/whole-SHA/array comparison | 5563 | `59474b1661e43b596090af8eec1a3a7d17c1490cf3f54ad9fc0249e70bd72e04` |

这些完整片段与 6cc 逐字相同；geometry 又独立比较原 execute 对应完整区段，并核新的输入 guard/target 范围。solver 独立核全部 160 词和 target/validator 的实际字段闭包。各自指定范围未见阻断；这些文字审查没有被写成 AST、科学执行、完整重建成功或连续数学证书。

完整 producer ready 为 `run08-independent-fixed-chart-input-ready.json`，9,388 字节，SHA256
`8cf596fd337ad7db7685f3c4282e15185cd5cea9b29ffbaa6ddfbcb9e8487f1e`，
远端 blob `2777faddb831161bb471083b87f1495053237ab9`。
它保存完整 actual 输入、全部原参数、唯一新 outdir、完整 argv、四输出和32个 scalar-only selectors。新目标文件、全 raw report 和全部 carrier 留在 runner；公开返回按完整大小和 SHA 绑定，不把大 raw 放入 Git。

真正是否重建出完整 dc5，以及新的完整后继场、所有约束和 root 是否成功，仍只按下一次实际 Actions 返回记账。
