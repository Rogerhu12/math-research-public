# R492：同 C 新叶 provider → 原 target / 准确 cut 的完整来源接口

日期：2026-11-16。实现者：geometry agent（AI）。

## 1. 本次交付与状态

本组件为一个独立 Python 源，实际消费 R489 的完整新旧 cut 叶交集，并在同一已加载 R416 场上重算原 target 与准确 cut 系数的区间值。其公开 API 可直接计算原完整 target 闭区间和 active 场六 jet。

当前为**源码与条件证明交付**。没有实际 accepted450、R489 子运行、单元结果、精度改善或全闭域成功；没有本地导入、AST、编译、fixture、测试或科学执行。没有 request/workflow，217仍未派发，不修改209/212/214。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `computations/geometry_20261116_same_C_refined_leaf_target_and_cut.py` | 35549 | `a7b1bd9d64db43986b5718d664dc6209227cd89a0cd9fb490e8dc6f9f4482aa7` |

完整命题见 [R492](../results/R492-same-C-leaf-refinement-for-the-fixed-target-and-accurate-cut-field.md)。本接口与证明的最终字节身份在发布清单中单列，避免文档自哈希循环。清单和完整新增 diff 是暂存交付材料，正式文件只有源码、证明和本接口。

该组件不创建新的 field 参数。旧 `checkpoint`、`definition`、十参数、全部 prefix/native 节点、共有 B、材料 core 与注册保持原对象来源。新包围与旧定义分别记录，原 receipt 不被重标。

## 2. 真实直接来源与继承闭包

源码 `PINS` 的五个直接文件为：

| 实际文件 | 完整 SHA256 | 用途 |
|---|---|---|
| `geometry_20261116_same_C_full_head_refinement.py` | `0ce2f7ab8d1cfc95097ac8089c41ecc1f888343c8432255bd91b1d6cc5d3f8f8` | R489 真实 input/result/member 读取、同语义比较、准确交集 |
| `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` | 原 R416 真场加载、追加 cut DAG、原六 jet 方法 |
| `geometry_20261115_continuous_ten_frozen450_prefix_metric.py` | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` | 原完整 target cell 公式 |
| `geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py` | `72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682` | 原同 C 三叶 DAG、Box 与所有准确分片/控制 |
| `geometry_20261115_shared_active_interval_balls.py` | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` | 原完整 Hermite/native/B/角度六 jet 引擎 |

这五件不替代原 loader 的传递闭包。`load_refined_accurate_cut_field` 真正调用原 R416 `load_accurate_cut_field`，原 source pins、R416 proof、R409 shared、R400 saved/checkpoint/profile、原 native/FD/final 来源及全部原数据仍按原加载。执行环境仍须安装原 numpy/python-flint 等真实依赖，不在此另选运行版本。

R489 的实际结果仍必须来自原 f12f 与1c39：

| 原 producer / reader | SHA256 |
|---|---|
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_stored_C_v3_cut_twojet_readout.py` | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |

本源只读这两者已经实际返回的结果与 binding，没有再次调用它们的科学程序。R489 完整1440/six重算的事实必须由其真实结果提供，不能由本源文件存在而推断。

## 3. 唯一登记的当前对象与同 job 条件

当前分支明确接受原 R416 的 `AccurateCutBundle`、原 R400 的 `AccurateTenTarget`、原72c factory 和原675引擎。实际类模块按 `type(obj).__module__` 定位，核其 `__file__`、SHA 和准确 class identity；不从 `sys.modules` 中取第一个同路径模块。这保留 R416 的独立 module instance，不猴补任何旧模块 globals。

R441 resolution、R451 complete-M、R464 incremental-M、R483 coast 生成视图均未因名称相似而注册。后继若使用这些场，应独立登记其真实完整来源；本交付不声称已支持它们。

R489 当前原 clock 来源是实际 `actual202205`：

| 项 | 准确合同 |
|---|---|
| launcher | `geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py`，SHA `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` |
| driver | `geometry_20261116_actual202_accurate_ten_full453_frozen450.py`，SHA `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615` |
| deadline schema | `request205-owned-job-science-deadline-v1` |
| 原钟 | `namespace_created_unix_seconds + 18900` 科学；原2700读回 reserve 不重开 |

R492 重新读取实际 launch/deadline，并与 R489 report 中登记的完整 receipt 相等核对。所有对象的 repository/run/source 使用真实 Actions 环境。它不把外层当前 request 编号猜成旧205实际 run，也不虚构历史193/203的泛化分支。

## 4. R489 provider 的实际消费成员

API 输入是 `refinement_directory` 与其原 `result.json` 的准确 SHA。该目录须为同一 job 的临时目录；当前源码的 `computations` 必须等于自己的真实 `HERE`。

读取内容如下：

1. 原 R489 `result.json` 和它实际绑定的 input 文件。
2. input 中完整原 launch/deadline；核原 recipe SHA、源 tuple、18900/2700及相同绝对起点。
3. 原 baseline C 目录的 `result.json` 与实际 input-binding member。
4. `refined-C/result.json` 与新实际 input-binding member。
5. 原 baseline 完整 cut reader JSON，以及 `refined-cut/cut-twojet-readout.json`。
6. `same-C-refined-enclosures.json`，其完整 receipt 和 report 中的登记正文。

要求 R489 实际 `binding_complete`、`completed_source_and_cut_recomputation`、`new_complete_cut_enclosures`、`same_semantic_C_proved_by_actual_bindings`、`all_owned_children_quiescent` 为真。新旧两份 cut 均须 `point_twojet_enclosure_complete=true`；当前已经加载的原准确定义本来就需要原完整 cut，不能以一个旧 partial 凑父。

旧 C/result 和旧 cut 的 bytes/SHA 必须分别等于当前 target 原 `continuous_tail.actual_result` 与 `actual_complete_cut_twojet_readout`，其完整 input-binding 也须相同。旧 reader 的三盒必须确实等于当前 target 的旧叶和原定义的 `actual_enclosure_leaves`。原 `original_binary_cut` 全对象、准确 cut 有理值也保留。

新源码重新使用原 `semantic_bindings`，其不忽略未知数学键；实际全输入、全部原根族、原 cut 与原查询配方关系均保留。只允许 R489 已声明的工作字段差别。每个三叶交集再由原准确有理 `intersect` 得到，并核对成员与 report 的原值。这里读取的是已有原结果，既不按宽度选择 root，也不补做未返回的 C 计算。

原和新 whole-query 完成标志分别记录在 `provider.actual`。它们不是这项完整三叶消费额外添加的工作精度门；也不由一个完整 cut 推断全域 query 已付。

## 5. API 与返回对象

### 5.1 已加载对象入口

```python
bind_loaded_refined_cut_bundle(
    current,
    *,
    computations,
    refinement_directory,
    refinement_result_sha256,
    sqrt_bits,
    budget_check=None,
)
```

`current` 必须是原 R416 loader 真返回的对象。返回 `RefinedCutBundle`，其独立 schema 为：

```text
R492-same-C-refined-leaf-target-and-accurate-cut-evaluation-v1-bundle
```

公开成员/方法：

| 接口 | 实际内容 |
|---|---|
| `.source_bundle` | 原同一个 R409 七元组，仅原数据/来源，不把其数值 renderer 当新准确计算 |
| `.target.closed_range(left, right)` | 原完整 R400 cell 公式，当前新三叶、新 values/length 和独立 cache；返回 `(jets, radial_metric, report)` |
| `.model` | 原 R416 同一追加 DAG，在新三叶下的七系数包围和公共 chart window |
| `.field` | 原 R416/675 引擎新对象，cut multipliers 真来自新包围，其余原数据保持 |
| `.pieces` | 完整原 active piece 列表，未删 prefix/native/collar/patch |
| `.evaluate(piece, radial, angular, lower=False)` | 原完整 active 六 jet；闭区间与明确下反射 side，完整物理角坐标 |
| `.expression_identity()` | 原准确表达式与当前求值表达式分别记录的独立 envelope，不能只取内部旧 callee schema 代替 R492 来源 |
| `.describe()` | 实际 provider/原定义与CP来源、旧新长度/七系数/window、调用计数及 paid/unpaid scope |

`target` 的 `.definition` 仍为原定义；`.leaves` 与 `.values` 是新求值状态。`.binding` 分开登记原 definition/CP身份和当前 evaluation provider。未把新叶写入原 `actual_enclosure_leaves`。

### 5.2 带原加载的入口

```python
load_refined_accurate_cut_field(args, *, budget_check=None)
```

保留原 R416 参数：`computations`、`directory`、`result_sha256`、`sqrt_bits`、`interval_bits`，以及原可选 `checkpoint_directory`、`proof_directory`。新增 `refinement_directory`、`refinement_result_sha256`。

它先调用原 R416 loader，再调用5.1。原 loader 失败时，R492 没有跳过它或用新叶凭空构造场的替代路线。这个边界不是新 BVP 接受条件，只是当前组件消费哪一个真实上游对象的明确事实。

## 6. 完整 CLI

```bash
python -u "$COMP/geometry_20261116_same_C_refined_leaf_target_and_cut.py" \
  --computations "$COMP" \
  --directory "$ACTUAL_SHARED_DIRECTORY" \
  --result-sha256 "$ACTUAL_SHARED_RESULT_SHA" \
  --checkpoint-directory "$ACTUAL_FROZEN450_CHECKPOINT" \
  --proof-directory "$ACTUAL_PROOF_DIRECTORY" \
  --refinement-directory "$ACTUAL_R489_DIRECTORY" \
  --refinement-result-sha256 "$ACTUAL_R489_RESULT_SHA" \
  --sqrt-bits "$EXPLICIT_SQRT_BITS" \
  --interval-bits "$EXPLICIT_INTERVAL_BITS" \
  --budget-seconds "$ACTUAL_REMAINING_CONSUMER_ALLOWANCE" \
  --out "$NEW_TEMPORARY_OUTPUT"
```

变量均需由真实 caller 的当前 receipt/显式工作参数提供。本接口没有给未来 accepted parent、C输出、精度或时长伪造数值。输出必须为 `RUNNER_TEMP` 内新目录；不得拥有原 shared、R489、computations、checkpoint、proof 或 cell plan 的路径。

不提供 cell plan 时，程序实际绑定 provider、重算完整 target DAG 和准确 cut coefficients，并构造相同准确场的求值 view；输出明确 `no_cells_requested_is_binding_only=true`，不填任何单元成功。

若要实际计算明确有限单元，再加：

```bash
  --cell-plan "$ACTUAL_CLOSED_CELL_PLAN" \
  --cell-plan-sha256 "$ACTUAL_CLOSED_CELL_PLAN_SHA"
```

plan 的 schema 为 `R492-same-C-refined-leaf-target-and-accurate-cut-evaluation-v1-closed-cell-plan`，唯一工作列表是 `cells`。各原行允许两种形状：

| `kind` | 完整原键 | 坐标含义 |
|---|---|---|
| `target` | `kind, radial` | 两个准确有理端点，位于原 numerical prefix 的 $[0,L_{num}]$ |
| `field` | `kind, piece_index, radial, angular, lower` | 原 active 列表的真实索引、闭径向区间、完整物理 $q\in[0,1]$ 闭角区间、bool 反射 side |

原 shape/key/闭域检查不改；plan 不是全域 cover 证明，不由几个端点或三维点盒替全域。程序既不自行选择单元，也不宣称这些有限地址是必要科学接受门。

## 7. 实际算术范围与恒定对象

以下计算使用新叶：

- 原所有表达式节点和真实长度 $L^*$。
- 所有原 target piece/support 的值与完整十项控制，原公共 $u$ 拉回和 $g_{ss}$。
- 原 $k,v_c,b_c,c_c,m_1,m_2,m_3$，原三阶准确 cut chart。
- 原 cut patch 的位置及完整六 jet，原上下反射逻辑。

以下内容不重新生成：原 CP/raw words、原准确定义、原 numerical compiler、原 Hermite/native/FFT 数据、共有 B、材料 rho/Phi、注册、十参数、W/H/marker、原 solver/RHS/H/J/FD/final/audit。原加载已经承担哪些条件，R492仍保其来源；未付的条件不因同一表达式而变成已付。

不同区间工作精度可能使某个新输出盒不严格小于旧盒；源没有据此拒绝原 solver，也不承诺收敛。区间空交、分母或 chart 未隔零均保持当前求值未完成，不能称真实 root族无解。

## 8. 未接的范围

这一节是当前实现范围，不能由相似类结构省略。

1. 任意物理半径处的 tail $E_C(r)$ whole/live-query provider 未切换。R489生成的新 query raw 不会自动被原 R418/R426读取。
2. 原 R418/R459 完整 metric/error DFS、R422/R435 reach、R425 held 没有新增本来源注册，也未由本源运行。
3. R441/R451/R464 生成数学来源尚未接受此独立 bundle；不能把本 schema 改成旧 schema 后交入旧 consumer。
4. R483 只改变同固定叶的表达式依赖计算，本组件当前仍调用原72c `piece_range`，未冒领该改进。
5. 本源不产生 solver/native 容差到全域 metric floor 的传递界，不用更紧 target 盒代替真实场误差或完整原门。

这些未接责任不阻止原 BVP 在其原门下运行，也不新增一轮独立审查或 fixture。

## 9. 原钟、信号和部分状态

`RefinedLeafProvider.check` 调用实际 caller 的 `budget_check`，并检查原 R489所绑定的绝对科学 deadline。独立 CLI 自入口计一个包含原加载的工作预算；没有把加载时间从报告中删掉。原 deadline 到达不允许再开始/完成记付新科学单元。

CLI 的信号处理只登记外部中断，工作边界抛 `ResourceStop`。本源不启动子进程；真正强制 TERM/KILL/reap 与全job quiet仍由原 owned caller负责。协作检查不是独立硬杀钟，嵌套原函数内部若未返回，不能假称它每个算术操作都检查了 deadline。原2700秒读回与全流程清理仍须后继实际 caller 接入，本源没有自行登记清理许可。

逐 cell 在处理前检查预算，不先从未访集合删除地址。只有原完整返回且后检查通过后才计入完成；中断时保留原 `current_cell`、所有 `unvisited_cell_indices` 与此前已完成原行。没有完整返回的字段不补零。

原源绑定异常、原加载失败、未解析的区间条件、真实资源停止、外部中断及 transport 超限分开记录，不归结为同一“数学失败”。尚无运行，不能根据这些分支代码预判哪条发生。

## 10. 输出与必要读回

输出目录只有新元数据文件；原 raw 不删。

| 文件/输出 | 实际内容 |
|---|---|
| `result.json` | 完整本次绑定说明、旧新叶/系数包围、全部实际已返声明单元、当前/未访地址、错误与实际时长 |
| `necessary-summary.json` | 不超90000字节时与完整 result 同正文；超限时为诚实 transport-partial 身份记录 |
| `BEGIN_R492_SAME_C_LEAF_CONSUMER_NECESSARY` / `END_R492_SAME_C_LEAF_CONSUMER_NECESSARY` | 唯一必要 JSON 正文 frame |
| `R492_necessary_identity` | 原 result/必要文件 bytes+SHA 与实际完整必要读回标志；不代替正文 |

正常源码/声明单元完成返回0；不完整返回2；完整必要 JSON 超90000字节返回70并保持原件、未读范围及原退出码。没有分块、编码大 raw、提高上限或无条件删除。极端 plan/错误正文仍可能超限，不宣称本源必能装入90KB。

任何 `full_domain_certificate`、`new_accepted_parent` 均明确 false。`all_declared_cells_returned` 只指用户/真实 caller 已显式给出的有限列表；零列表的 binding-only 标签单独保留。不能把该值用作完整闭域成功或下一轮 BVP 的新门。

## 11. 接入责任

后继 caller 可在真实同job原场与R489结果都存在时直接调用5节API，再为完整闭域消费者登记新真实来源；不得覆盖原生成模块或写回旧定义再冒旧 SHA。若需要把新 C raw 用于 tail queries，应独立重绑完整原 query/source/radial-domain 责任，不能仅在本 view 的三个叶字段之外添加成功标签。

目前没有新 workflow、外层 owner role、actual parent 或 run。完整定义/原 solver/所有门保持原状；实际误差改善与所有未返范围留给以后真实执行。
