# 全九系数冻结 450 场的完整 SavedPrefix 与 shared-B 闭场接口

类型：独立源码与完整有限场重构接口；未执行科学，未选择未来父场、九系数、参数、尾响应或 run。

作者：ChatGPT / exact_refinement。日期：2026-11-15。

本接口把真实 `nine-control-all-frozen-same-metric450-complete-physical-DN-v2` 接到现有完整物理 SavedPrefix 和七元组闭场协议。它保留旧数学消费者，显式更换标量与来源分发。它不构造 450 的接受记录，不把 453 设计场、recipe、prepared 或失败 native 记录当成接受场；也不把新的九系数标量重标为旧 v3/v4。

## 1. 两份独立源码及已发表的上游

两份新源码拟保存于本课题 `computations/`：

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| `geometry_20261115_nine_control_same_metric_saved_prefix.py` | 16901 | `e8deb4136dbaf021d2648e02a2cdb774db4ebe1836b239b609472c596fc70404` |
| `geometry_20261115_nine_control_shared_closed_dispatch.py` | 20022 | `69bbba2647b2356f2c4023c74a938e29d1b93effcb1c99385fdaa73b78b9d17d` |

它们消费已经发布于 `6c1f44aaf2bfa662374a36bdfde7ddc774ebe910` 的两个 v2 来源，不修改该两源：

| 上游 | SHA-256 |
|---|---|
| `geometry_20261115_nine_control_same_metric_profile_v2.py` | `5e95afdb82f83a276003e6a4846e20893b7eb7f2b44b309d56950f11dbfaa0d3` |
| `geometry_20261115_nine_control_same_metric_full112_v2.py` | `92cfb0701824df770dfcd009a623e84695e72fe9c489d70537d8983415adc7e8` |

上游 v2 已显式区分原 `00e4d2c3…` 九设计生产器与 `0433e101…` 九 H(s) 生产器；后者已发布于 `e14844ea847664e8f155b00034d412a902e31d31`。本消费者只接两种来源经真实 v2 求解后产生的 accepted450。它不会直接把任一种 accepted453 变为 accepted450，也不会重放祖先 H(s) 路径。

本次没有新 workflow/request 或 dispatch。旧 070b/1610、v2 两源、九设计/H(s)、旧 SavedPrefix、闭场、背景及空间消费者的文件均不改。

## 2. 实际父件必须是什么

输入为真实 v2 `actual.json.gz` 或逐字相同的完整原件。路径可以移动或改名；有限场定义以完整文件字节数与 SHA 绑定，不以存储路径作数学身份。

新读取器先核自己的直接来源及完整原物理 jet 本地 Python 来源，再调用冻结 v2 `runtime()`。后者核原完整 producer closure；该 closure 不能先加入新消费者文件，否则就会误把来源不同的集合冒成已接受 producer 的同一集合。

随后直接调用 v2 的 `freeze_parent(runtime, actual, whole_file_receipt, accepted=None)`。其原条件全部保留：

- 明确的 v2 field/scalar schema、当前真实 producer SHA、完整 producer closure、当前标量 canonical identity。
- 原 `success=True`、`status=0`、原 collocation RMS ≤ `1e-6`、原边界残差 ≤ `1e-11`、原 physical frozen-control RMS ≤ `1e-6`，以及实际尾响应 SHA。
- 全部 mesh、physical states/RHS、augmented states/RHS、core，及前 338 行原字节一致性；没有选择部分节点或低模式。
- `M=T=112`、`N=2048`、physical 338、augmented 450、`K=k=0`、left 338/right 112；空 active 参数与全部九个 frozen 参数不能混同。
- 全部九系数、顺序、每个支撑与原存储 width、nested 原三参数 scalar、设计祖先 producer/输入/来源身份、两条有限求值路径。
- H(s) 祖先时，原 e830 helper、实际 policy、原00e4来源、同 worker 责任与完成路径收据保留在真实 `origin_design_field`；它们是祖先来源，不是新 worker cache 或新接受。

九参数顺序固定：

$$
(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3).
$$

新读取器另核实际顶层 450/338/338/112、`physical-phi-complete-DN-v1`、`original_metric_identity` 的新 frozen-nine schema 与完整 scalar，以及 `complete_nine_scalar_parameters` 的全部 binary64 词。这些是来源和布局一致性，不是新增解的数值接受阈值。

`read_saved` 阶段读取的是实际父文件中报告的原接受与尾 SHA。真正尾 response/config/source/H/J/audit 的完整外部原件交叉绑定由后述原 `load_bundle` 保留；仅得到 SavedPrefix 对象不等于又执行或又证明一次 native 接受。

## 3. 完整物理场与两条有限标量路径

新类 `NineControlSameMetricSavedPrefix` 继承原 `LargeCoreSavedPrefix` 的十个方法：`profile`、`inverse`、`angle`、`mean_jets`、`height_jets`、`_world`、`nine_jets`、`jets`、`material_jets`、`set_native_registration`。未复制或更改这些方法。`PhysicalQuintic` 是原类的直接别名。

构造器中的完整 core/material-density 段与原源逐字相同；原 saved-y/saved-RHS/finite-ODE-second/PhysicalQuintic 段只改变 law 的实际读取键：

```
actual450.original_source_metric_identity.law
```

原因是当前 `original_metric_identity` 已表示全部九系数冻结后的材料度量，不再含旧 accepted96 的 probe 构造 law。新代码不添默认 law，不伪造旧字段，不把当前 g 称为 accepted96 的 g。

有限求值责任分为三项：

1. 点 scalar 仍由 v2 `FrozenNineProfile.profile` 进入原00e4 `ThreeActiveView.profile`，保持原九系数有限组装和六 shape 的原求和顺序。
2. 节点一阶 jet 直接保留实际450的完整 saved batch RHS。它不是用点 scalar 路径重算后替换掉的数组。
3. 新物理 quintic 所需第二 jet 沿原完整 `FullCoreProbe.frame/project`、原 complex-step state 项及显式 scalar 项；此处仍使用冻结的点路径。

原 `node_saved_vs_local_RHS_max` 继续报告点路径与保存 RHS 的实际差，未变为新的接受门，也不声称两条有限路径逐位相同。原 real Hermite 定义和其 longdouble 系数/浮点评价范围不改变。

物理状态完整保留

$$
r_0,\ldots,r_{112},\quad t_1,\ldots,t_{112},\quad z_0,\ldots,z_{112}.
$$

全部112核系数进入材料圆逆及全角 Fourier。材料高度均值仍为原完整公式

$$
z_0+\frac12\sum_{m=1}^{112}(1-4m^2)c_mz_m.
$$

没有追加旧 small-field mean。原 R237 完整核三角下界仍负责全材料逆；若该既有充分界不能支付，读取会保留其原失败，而不会称原 full-DN 接受无效、自动删高模或假造更强密度证书。

## 4. R249 入口正常形与首 cell 标量责任

`read_saved(checkpoint, normalize=True)` 默认调用原 `normalize_inlet`。它只处理原 node0 的三组反射 jet，其余所有节点、单元、切端及全部角导数继续保留；原接受场记录不编辑。`normalize=False` 返回未作该后处理的真实完整场。

原正常形记录通过实际类模块取得新的 reader SHA，保完整节点 jet SHA、精确 correction witness 和原条件误差式。本次不改 R249 数学。

旧 `first_cell_scalar_lower` 只理解真实旧三参数 base 定义。新分发首先检查九个原真实支撑的左端均不早于首物理 cell 右端，只有全部控制在该 cell 恒为零时，才把**真实 nested 原三参数定义**作为该旧 base-quintic 引理的私有参数视图。actual450、完整九 scalar 与 accepted record 均不改标签。

若任一九支撑进入首 cell，返回 `available=False`，不借旧 Bernstein 界证明一般九控制标量。即使可使用首 cell 引理，它也只支付其明确首 cell 范围，绝不是整个九控制 scalar 的连续区间证明。

## 5. 真正复用的闭场协议

独立 dispatcher 公开：

```python
read_saved(checkpoint, normalize=True)
load_full_bundle(args)
load_shared_bundle(args)
```

后两者返回原七元组，不制造替代字段：

```python
paths, plan, assembly, background_table, saved, assembly_object, binding
```

`saved` 保完整 `quintic.x/nodal/coefficients`、`core`、`rho_lower_exact`、`registration`、`nine_jets` 及所有原物理成员。shared 版本的 `assembly_object.shared_background` 仍是原 exact shared-node Hermite B。

分发只在当前同步调用内暂时绑定原 inlet/large/lifted/shared 模块的读取器、bundle loader 和 metadata writer。所有改动以 `finally` 还原，包括 argv、bundle、last assembly、install callbacks。没有修改原源、执行修改后的源字符串或给现有 v3/v4 标签塞入九参数数据。调用方不得在同一解释器并行运行另一个旧全局分发任务。

原 large bundle 的全部实际责任保留：

- 原完整 port 与 frozen scalar `complete_original_port` 相同。
- actual450 指向的真实最终 response/config SHA；原公开78-source来源、实际 numerical source ledger、两件历史 ready 的逐 SHA 身份。
- `actual_nonlinear_solve=True`、原 converged、残差小于原 config tolerance、完整 audit 与 `heightJetJacobian`；全112 H、全338×112 J，没有截取低模式。
- response 的完整原参数与 config 一致，只有原四个 IO 键例外。
- 全部 endpoint core 的实际有限 drift 保留，以原 MaterialTrace 重读 H；原 `1e-12` 一致性责任不改。
- 完整 actual radial readout 必须回绑该 response/config，原 tail grid/cut、scalar cut012 与方向责任不变。
- 一次完整全局 SE(2)，全部均值/绝对 cap height，完整材料 cut correction、完整 native FFT、原 collar、固定帽和 marker。

`load_full_bundle` 继续核 plan/assembly/mesh/background/normals 完整文件 SHA、共享节点定义、原 single SE(2) 记录和全部 mean/cap/axis。新增的 plan/assembly 字段明确真实 nine450 dispatcher、reader、scalar SHA。原 Node 背景表保持原字节，不要求它带 Python 新字段；它通过原 plan/config SHA、profile fingerprint、cut/cuff 等原绑定进入同一场。

原 `closed all` 可以执行其既有真实 radial readout 与原背景表程序；`closed plan/render` 可以消费已完成、同一真实响应的原 radial readout。这里没有新增 native solve 或重新 BVP 接受。完整 radial readout/背景表仍是 Actions 中的科学计算，不能称 byte-only。

## 6. shared-B 的新显式 guard

原 `prepare_from_bundle` 的全部 exact Hermite、全112材料均值、完整 FFT、cut/cuff/cap 与 source table 公式不变。descriptor 的原 `source_sha256` 仍如实指向 `da4a0b50…` 数学 producer；额外字段标明新的 complete-field dispatcher，完整 field binding 包含当前 accepted450 与九 scalar 身份。

原 `SharedBackgroundAssembly` 与全角 cut difference/collar/cap 数学不变。新的 geometry schema 是：

```
frozen-nine450-shared-background-closed-geometry-v1
```

其 `wrapper_sha256` 明确指新 dispatcher；原 `ac635c11…` shared kernel 另列 `unchanged_shared_background_kernel_sha256`。原 exact B 节点与源表不混同，原目标仍是原 stored profile 的目标，不能替成 `1+B'²`。

新的 guard 必须要求：

```
geometry_20261115_nine_control_shared_closed_dispatch.load_shared_bundle
```

原 v3/v4 loader 不获授权接受新 scalar。新 loader 重建相同原 source bundle、相同 B 与 guard，逐项核新 plan/table 可还原到原 plan/table，核完整 mesh/normal/来源/mean/SE2。路径可移动，科学 payload 与完整定义必须相同。

generic 物理 readout、plan、assembly 的原数学报告 schema 可以继续表示相同报告结构；`complete_field_dispatch`、实际 constructor/scalar SHA 和新的 shared geometry/guard 明确区分本场。原数学 kernel SHA 与实际 adapter SHA 分列，不能把未执行的旧 scalar reader写成当前来源。

## 7. CLI 与输入准备

全部调用只能在 `Rogerhu12/math-research-public` 的 Actions。下面变量都是调用者届时取得的**真实**原件路径，不是本接口选定的未来接受场：

```bash
python computations/geometry_20261115_nine_control_shared_closed_dispatch.py prefix \
  --checkpoint "$ACTUAL450" --out "$RUNNER_TEMP/nine450-prefix.json"

python computations/geometry_20261115_nine_control_shared_closed_dispatch.py audit \
  --checkpoint "$ACTUAL450" --angles 2048 4096 --radial-subdivisions 16 32 \
  --out "$RUNNER_TEMP/nine450-inlet.json"

python computations/geometry_20261115_nine_control_shared_closed_dispatch.py readout \
  --input "$ACTUAL450" --angles 2048 4096 --radial-subdivisions 2 4 \
  --out "$RUNNER_TEMP/nine450-material.json"

python computations/geometry_20261115_nine_control_shared_closed_dispatch.py closed all \
  --checkpoint "$ACTUAL450" --port "$PORT" --config "$CONFIG" \
  --tail-response "$FINAL_RESPONSE" --source-topic "$RESTORED_SOURCE_TOPIC" \
  --out-prefix "$RUNNER_TEMP/nine450-original/surface"
```

`closed` 的其他参数完全沿原 `all|plan|render`；提供 `--complete "$COMPLETE"` 可消费已真正完成的同场 radial readout。原全部 physical/scalar knots 保留，原显示采样预算只作用于显示网格，不是标量/场截断。

准备 shared B：

```bash
python computations/geometry_20261115_nine_control_shared_closed_dispatch.py background \
  --directory "$RUNNER_TEMP/nine450-original" --basename surface \
  --checkpoint "$ACTUAL450" --port "$PORT" --config "$CONFIG" \
  --tail-response "$FINAL_RESPONSE" --complete "$COMPLETE" \
  --source-topic "$RESTORED_SOURCE_TOPIC" --out "$RUNNER_TEMP/nine450-B.json.gz"

python computations/geometry_20261115_nine_control_shared_closed_dispatch.py shared-render \
  --source-directory "$RUNNER_TEMP/nine450-original" --source-basename surface \
  --descriptor "$RUNNER_TEMP/nine450-B.json.gz" \
  --checkpoint "$ACTUAL450" --port "$PORT" --config "$CONFIG" \
  --tail-response "$FINAL_RESPONSE" --complete "$COMPLETE" \
  --source-topic "$RESTORED_SOURCE_TOPIC" --out-prefix "$RUNNER_TEMP/nine450-shared/surface"
```

程序 API 的 `load_full_bundle` 需要原 directory/basename、checkpoint/port/config/tail_response/complete/source_topic。`load_shared_bundle` 另外需要 source_directory/source_basename/descriptor，而 directory/basename 指新 shared 输出。

完整 source closure 分层保留：v2 runtime 原 producer closure；新 reader 的直接两 v2 源与原23份物理 jet 本地 Python 来源；dispatcher 的原闭场/加载/读出/背景来源及其6份直接 Node依赖；实际 tail 的原公开源 ledger。两历史 ready 必须在原约定位置由真实历史输入恢复，不能依赖已清理 HEAD 仍含旧 JSON，不得从 hash 制造输入。没有额外要求恢复未被本读取器消费的旧 raw 四输入；重构所需完整 nested scalar 已在真实 actual450 内。

CLI 所有新输出限定于 `RUNNER_TEMP` 并保原独占写入/失败语义。原 partial 文件和 stderr 留作当次临时诊断；本入口不上传 raw、artifact 或 Release，也不写 Git。未来公开结果应只登记脚本、完整参数、真实 run/source、输出 SHA 和紧凑结论。

## 8. 下游仍未支付的责任

此代码只提供完整有限场及诚实的同场重构入口。没有预设当前存在实际 accepted450。

`shared_active_interval_balls` 等代码可以在其真实 bundle 边界消费这里的七元组；若其入口硬编码旧 loader，需独立显式选用本 loader，不能静默绕过 guard。

尤其旧 `shared_field_relative_metric` 中的 `Prefix.export_scalar_descriptor`/`ScalarExpression` 只理解旧 scalar。新七元组并不授权旧表达式证明九系数的连续标量界；全九支撑、两个有限路径与声明式连续标量的差别仍须明确处理。stored-tail 连续 E、所有 C² seam、完整空间×phase责任、曲率/reach/held 与最终标准也不因重构自动成立。

当前物理/角度样本、原有限背景表和新 exact B 的角色分开。没有将 norm 差、采样最大值、symbolic seam 端点关系或 postprocessed mesh 当成全连续证书。原 BVP 的成功仍只是该父有限场来源，本后处理不重获 BVP 接受。

## 9. 已作的本地工作范围

仅做源文件阅读、完整 source/SHA 核、AST 解析，以及原 constructor 两段的逐字比较：core/material-density 段全同；物理/RHS/ODE-second/Quintic 段仅 law 字段路径改变。十个数学方法与 PhysicalQuintic 直接继承/引用。

没有 import 数值模块、构造 SavedPrefix、执行 scalar/RHS/J/QR/ODE/Fraction 范数或任何科学 fixture，没有 Git/Actions mutation。完整差异和 source-only 回执为可从源重得的临时开发材料，不作为新的科学门或待审核依赖，也不需保存可重算大数据。
