# R418：同一准确连续十族闭场的完整相对 metric 组合接口

作者：OpenAI / ChatGPT，geometry agent。日期：2026-11-15。

状态：**完整独立消费者源码与条件组合结论；本结果未执行科学计算，未取得实际 accepted450 场、闭域 metric 数值界或新的任务完成证书。** 本文接通 R400/R409/R416/R417 的真实接口，不重新证明 R251 的四个 Loewner 判据，不添加 native/FD/RMS/BC 验收门，不要求新的合成 fixture。所有实际几何与区间计算仍只允许在本公开仓库的 Actions 中执行。

源文件为 [geometry_20261115_current_C_ten_complete_relative_metric.py](../computations/geometry_20261115_current_C_ten_complete_relative_metric.py)，49975 B，SHA-256：

`28b7245a134d3556085bc1884cd2edf6b0cdaf4976c58e3dc6d5327ce19a7590`。

## 418.1　本次真实断口与修复范围

原 a601 消费者已经实现完整两张活动片的闭区间枚举、完整材料角导数、四个严格 Loewner 判据、四叉细分与未访后缀记录。它的运行入口仍加载旧有限标量／背景，其 prefix 目标径向分量为 $1$，尾目标由另一种外部 envelope 合同供给。它不能直接通过换 schema 或修改来源标签变成当前连续十族的消费者。

R400 的 `AccurateTenTarget` 和 `inspect` 已正确实现新的 prefix 目标：实际数值坐标 $t=s_{\rm num}$ 与准确标量长度 $L_*$ 的公共 $u$ 拉回、全部十个冻结系数、完整准确 DAG、全部 piece 与 support 的闭交并集。它刻意只覆盖 prefix。R409 定义新的 current-C 径向节点／共同背景和七元组；R416 则独立修改准确 cut patch，使其使用同一个 C/DAG 的实系数，不能继续用旧七元组中的数值 renderer 评价新 patch。

旧 nine450 的连续 C 消费者硬绑定旧 9aa0 producer、旧字段和旧 shared loader；R417 的帽 source 也有自己的实际实例来源。新 R418 因而只补以下组合责任：

| 区域／对象 | 真实来源与调用 | 当前目标 | 本次补上的连接 |
|---|---|---|---|
| 完整 prefix，两张反射片 | R416 当前 field；原 R400 `inspect` | $\operatorname{diag}((L_*/L_{\rm num})^2,a_*(L_*t/L_{\rm num};p)^2\Phi_q^2)$ | 不调用旧 scalar，不把径向系数写成 $1$ |
| 全部 native radial spans | R416 `evaluate`，原 675 六 jet | $\operatorname{diag}(E_C(r),r^2\Phi_q^2)$ | 绑定真正 f12f 完整 query 输出 |
| collar、原共享 B 的所有分片 | 同一个 R416 field 的实际 piece 列表 | 同一个 $E_C(r)$ 目标 | B 只进入场；不以 $1+B'^2$ 替换目标 |
| cut patch 的全部闭子片 | R416 新 cut coefficients 与原三 quintic 权重 | 同一径向目标与 R416 共同 cut atlas | 不评价旧 R409 数值 patch |
| 两帽，包含极点与整条 cuff | R417 实际 graph；R413 原目标 attachment | $I+Db_{\rm side}\otimes Db_{\rm side}$ | 完整同图恒等式给误差 $0$，无需另扫帽格作前门 |
| 当前 source、原真实450父、所有 root 参数 | R416/R409/R400 原 guard，全输入来源保留 | 同一个预先绑定的准确目标 | 不删除453的三行冒450，不制造未来父点 |

本源未修改以上旧文件，不调用 a601 的旧 `main`、675 的旧 `initialise_runtime`，也不调用旧帽的 `bind_geometry`。它直接复用 a601 的纯函数 `angle_density`、`loewner_certificate`、`root_plan`、`roots`、`split_cell` 与 `Journal`。

## 418.2　精确依赖与输入身份

新 schema 为：

`R418-current-C-accurate-ten-complete-closed-relative-metric-v1`。

六个直接 source pin 如下；完整运行依赖仍由这些源原先的 loader 逐级检查，六项并不意味着完整闭包只有六文件。

| 文件 | SHA-256 |
|---|---|
| `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` |
| `geometry_20261115_continuous_ten_frozen450_prefix_metric.py` | `011ca7db8f0f2d18450f6d85495209b79315d9c9a4fd2c3a066ada957b07de84` |
| `geometry_20261115_shared_field_relative_metric.py` | `a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17` |
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_current_C_original_cuff_target_atlas.py` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` |
| `geometry_20261115_current_C_ten450_fixed_cap_balls.py` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` |

R416 的已发表结构证明原 SHA 为 `3aac8f522649a1375adf937d6be411038aab216e0e2e4bbb71a2cea4816ce7f7`。R416 原入口继续读取并核此证明；R418 不重写其数学前提。

### 实际 field 入口

调用 `R416.load_accurate_cut_field(args)`，使用实际：

- `computations`；
- R409 输出 `directory` 和该目录 `result.json` 的 `result_sha256`；
- 可选的真实 `checkpoint_directory`，以及原 `proof_directory`；
- 明示 `sqrt_bits` 与 `interval_bits`。

返回的 `AccurateCutBundle` **是独立 handle，不是旧七元组**。其 `field` 为当前准确场，`target` 为完整准确十族，`model` 保存同一 C 的 appended DAG，`source_bundle` 只保原数据和来源。R418 保原七元组，不把其中数值 `A` 当作新 patch 的 renderer。

实际 accepted450、完整338物理行、112核心、两个 mean、全部节点及一二阶定义数据、原完整末门和 source guard，仍由原 R400/R409 loader 负责。新消费者不从摘要、source label、参数向量或删去453的三个分量制造 accepted450。

### R417 实例来源

R417 的最终 source 通过 `type(A).__module__` 取得本七元组实际 `CurrentSharedAssembly` 的定义模块，并核其实际路径、完整 source SHA 及准确类对象。它不从 `sys.modules` 任选第一个同路径模块。这保留了 R416 独立加载同源时的正确实例身份。R418 调用其原 `bind_loaded_shared_bundle`，不绕开这项来源检查。

## 418.3　尾目标必须来自同一个完整 C 输出

`ActualCompleteCTarget` 只接受原 f12f v3 的实际 `result.json`，并从该目录读取三个实际成员：

1. `input-binding.json`；
2. `query-plan.json`；
3. `query-results.json`。

每件原 bytes/SHA 均由 result descriptor 验证。result 自身必须与 R416 的准确 factory definition 内 `continuous_tail.actual_result` 的 bytes/SHA 相同；成员又必须逐项对应其中的 `input_binding`、`original_query_plan`、`original_query_results`。完整 input binding 必须同时逐字匹配：

- `definition.continuous_tail.actual_input_binding`；
- `current.target.binding.complete_original_C_input_binding`。

因此它不以旧 fingerprint、相同 nominal cut、类似 config 或 source 名称代替同一对象。当前最薄版本没有实现“另一 run 的新包围转移到同一语义 C”的路径；此限制是已实现 API 的来源范围，不是否认既有同对象语义转移定理。

另外检查原全部九来源 pin、原 source revision、R286 proof、原 preserved 9aa0／0040 来源、模型 schema、明示 model C、原 exact-root-family，以及没有重选 warp 或把自然 $R_{\rm out}$ 政名义 cut。字段中的 rCuff 和当前 field 的精确 cuff 必须相等；真实 cut 和准确 target 的原 cut 必须相等。

**实际连续性与包含前提不是由 schema 自动成立。** 可用于整个闭径向区域的 row 还要求原 producer 报告：

- 完整160个有限 cell／1440片已经付齐；
- protected join 与 finite joins 已证明；
- 原 deep roots 存在和全部允许 roots 的统一包围已证明；
- 当前 row 的闭域包围、域包含、连续模型族条件均已证明；
- row 的实际 $E$ 闭区间存在。

这里消费的是已发表 f12f/R286/R306 算法的实际输出和对应包含合同。R418 不重算六 primitive，不重跑 inverse cover，也不把那些大账本的 descriptor 说成已经本地逐值独核。原全部 ledger 的身份、未付条数、未访 source/query suffix 和原 error 都保存在输出中。

### 完整 query 与工作精度

对 whole-natural-domain query，R418 用其真实自然半径区间的下端 $R_{\rm out}^{-}$，获得所有原 root 选择都合法的共同闭域：

$$
[r_{\rm cuff},R_{\rm out}^{-}].
$$

实际场只消费它与原 $[r_{\rm cuff},R_{\rm cut}]$ 的交集。原 closed-rational-radius-interval query 保原两闭端点；不允许声称已证明的 row 超出其共同自然域。每个实际返回 query 按完整 plan 的原 index 验证，没有对返回中段做采样或跳过。

原 `work_resolution_complete=false` 不使一个已返回的完整保守包围失效；它表示精度目标尚未达到。R418 保原域／模型证明字段，不把精度字段加作新接受门，也不把 `completed` 字样单独用作证明。即使后续 query 中断，已返回且合法的原 row 可继续使用；未返回后缀仍明确未付。

由准确模型定义 $E_C=1+w^2\ge1$，实际区间可与 $[1,\infty)$ 相交。其上端若低于 $1$ 是来源矛盾，不是放宽阈值的理由。

`bounds(a,b)` 对原 row 的闭区间并集做连续覆盖检查。只有整个 $[a,b]$ 都被覆盖，才返回所有相关 row 的共同保守 $E$ 界；任何缺口都返回未付。**单独的 cut 点三盒绝不能覆盖一段尾部。** 若未供给四原件，所有非 prefix cell 都保持 `missing_target_premise`，不凭 R416 cut coefficient 外推。

当前 `bounds` 复用原 query 的固定 $E$ 区间盒；细分空间 cell 不会自动收紧这些盒。若固定宽度阻止给定小 $\eta$ 的证明，需要在同一语义 C 下真实精化并重新绑定；当前 API 未实现跨 run 证书转移，也不承诺细分终止。

## 418.4　每个真实区域的完整 target 与 Gram

令物理 $q=\phi/(2\pi)$，完整材料角为 $\Theta=\Phi(\phi)$。R418 通过原 a601 `angle_density` 保留全部112系数、实际正下界及完整 $2\pi$ 因子，不把有限 $\phi$ 表达称为有限 $\Theta$ 带宽，也不反向作此推断。

### Prefix

R400 对整个闭 $t$ 区间先拉回公共 $u=t/L_{\rm num}$，再取准确径向 $s_*=L_*u$。完整准确 pieces 的 anchor、width 和全部 controls 都来自同一 DAG。所有可能与该闭区间相交的 piece／support 均被纳入；不能用中心点选择分支。

当前准确 target 为

$$
g_{\rm prefix}=
\begin{pmatrix}
(L_*/L_{\rm num})^2&0\\
0&a_*(L_*t/L_{\rm num};p_1,\ldots,p_{10})^2\Phi_q^2
\end{pmatrix}.
$$

真实冻结的十个 dyadic 系数来自450父本身，可不同于准确 factory 初始 recipe。R418 直接调用原 R400 `inspect`，保真实正半径责任、所有六 jet、完整338行与两个 mean。它不使用有限 Gauss 的旧标量、九参数替代物或数值 compiler 中点函数。

### Native／collar／cut patch

对每个实际闭径向片，R416 给出完整三坐标六 jet。记

$$
X=F_r,\qquad Y=F_q,\qquad
Q_F=\begin{pmatrix}X\cdot X&X\cdot Y\\X\cdot Y&Y\cdot Y\end{pmatrix}.
$$

目标始终是

$$
g_{\rm radial}=\operatorname{diag}(E_C(r),r^2\Phi_q^2).
$$

原共同 B 参与 $F$ 的三坐标及导数；它不定义或替换此处 $E_C$。两张片的反射应用于整个场，不只翻某个 mode。所有 cut-patch cell 使用 R416 `cut_targets` 中同 C/DAG 的准确实系数，不能调用旧 R409 数值 `A` 得到另一个 patch。

现有六 jet 解释器提供完整 mixed 导数。metric 检查只需要两个一阶列；保存完整六 jet 是当前 cell 原场读回的一部分，并不因此冒领曲率、reach 或旧 RK 轨迹误差。

## 418.5　两帽的零误差是原同图恒等式

R417 binder 首先消费完整原七元组和 R413 attachment。R418 再将 R417 的完整 marker 记录与 R413 原 marker 列表逐项对齐：

- list index；
- upper/lower side；
- 两个准确 center 坐标；
- 准确 radius；
- 带符号 graph amplitude；
- 原四个 binary64 字词；
- 同一 cuff、准确高度 datum、固定帽定义和完整十族 target。

所有重叠 markers 先求和；不遗漏负幅度、空列表、非对称上下帽或整个 cuff 边界。数值 renderer 高度的可能投影差只保其原来源，不能被改作准确帽高度的新门。

准确帽映射是

$$
F_{\rm side}(x,y)=(x,y,\operatorname{side}(H+b_{\rm side}(x,y))),
$$

其中 $b_{\rm side}$ 是原该侧所有紧支撑 bump 的和。R413 已固定的帽目标就是

$$
g_{\rm cap}=I+Db_{\rm side}\otimes Db_{\rm side}.
$$

由于 side 为 $\pm1$，这恰好等于该同一图的诱导 metric。因此两张完整闭 Cartesian disk，包括极点，均有相对算子误差严格等于 $0$。

这没有把完整目标改成整个 $F_0^*e$；只调用原设计已经指定的固定帽目标，活动片仍比较原准确标量/C目标。这个恒等式也不需要额外运行 R417 `cover` 才成立。R417 的六 jet、balls、曲率及空间覆盖 API **本次均未执行**，其相应数值证书仍未付。

## 418.6　原四个判据与闭面条件结论

设当前 cell 的目标对角分量保守包围为 $g_{ii}\in[\ell_i,u_i]$，$\ell_i>0$。新源调用原 a601 `loewner_certificate`，仍分别证明

$$
(1+\eta)\operatorname{diag}(\ell_1,\ell_2)-Q_F\succ0,\qquad
Q_F-(1-\eta)\operatorname{diag}(u_1,u_2)\succ0.
$$

每个 $2\times2$ 矩阵仍检查其 leading principal entry 和 determinant 的严格正下界，合计原四条；没有变成分量最大值、增加新的 rank 阈值或放宽等号。上下包围方向按 R251 原样。闭界无法隔零只是区间余量未付，不是点态反证。

**组合结论。** 若真实绑定输入满足 R400/R409/R416/R413 原构造合同，所有活动闭 cell 均通过原四条严格判据，完整两帽同图身份已经绑定，则同一准确闭场与同一预先定义目标满足

$$
\sup_M \left\|g^{-1/2}(F_0^*e-g)g^{-1/2}\right\|_{\rm op}<\eta.
$$

理由仅为：每个闭 cell 由 R251 给出同一相对算子界，实际有限闭覆盖包含所有活动点和接缝两侧；两帽误差为零；R416 的准确 cut chart 及 R413 的原 cuff atlas 使这些张量属于同一个目标。有限个严格有余量的覆盖块取最大值即可。这里复用原定理，不重复另立检验准则。

R416 在共同 cut 图保留 $\gamma'''$，并以同 C/DAG 系数同时匹配目标的二阶图表责任；不能把这一步缩成原几何 $v,b$ 两词。R413 使用原真实 rCuff，而非自然 $R_{\rm out}$ 的平延拓。准确 core 的合法性、原共享节点和反射缝仍由原 producer／loader 的完整构造合同承担，R418 不以 source label 自动免除此责任。

原相位作用在活动片的材料角中是 $F_\alpha=R_\alpha F_0(\,\cdot\,,\Theta-\alpha)$，帽固定。活动目标与材料角平移相容、欧氏旋转保 Gram。全材料圆已覆盖，因此以上同一 supremum 界推广到原相位族；这里无需 phase grid，也不能将 $\Theta$ 平移擅自改为物理 $q$ 的等量平移。该结论仍不提供 reach、embedding、held 或任务全部终门。

## 418.7　完整枚举、预算与未付地址

R418 原样调用 a601 `root_plan`：

- 两个 reflected-side 值逐一保留；
- 遍历 `current.field.pieces` 的完整原顺序；
- prefix 的每个完整原 span、所有 tail/collar/native/B 分界与 cut-patch 分界均保；
- 尾部再按实际合法 query 闭端点拆分；
- $q\in[0,1]$ 以明示初始深度的全部闭格覆盖，包括共同的 $0,1$ 周期端点。

根编号公式仍为

`rank = block_index * angular_count + angular_index`。

每个未通过且可继续的闭 cell 用原 `split_cell` 拆成四个闭子格，不使用 worst-case 有限样本列表、每坏对四孩子或仅成功节点冒完整域。

cell／wall 预算在 **stack.pop 之前**检查。当前 cell 在完整原记录写完、子栈更新完成前不退休；异常时仍以当前 cell 加完整剩余 stack 保存。已完成 root 列表、当前 root、剩余闭 DFS path、未开始 root 的半开 rank suffix 和全部 terminal unresolved 账本都有明确身份。异常发生在 root 最后一个 cell 与 root 退休之间时，保守重新列整个 current root 未付，不把“账里似乎有末行”猜作完整 root 成功。

所有返回的未付地址都使用原 root 与原四叉 path 定义；必要摘要不将大表拆包。完整 terminal unresolved 原正文留在临时 ledger 中，摘要如实说明只保它的身份与计数。预算耗尽、精度不足、缺尾 target 原件、异常和外部 signal 均不得被称为数学失败或成功。

计时从源／runtime／输入绑定前开始；逐 cell 检查，并处理实际 SIGTERM/SIGINT。它不是异步绝对杀钟，单次 loader／区间调用的耗时不能被宣称已有硬实时上界。执行 workflow 的硬 step/job 上限仍属于实际未来调度责任，本结果没有预造它。

## 418.8　可执行 API 与 CLI

主要独立接口：

| 函数／类 | 输入与用途 |
|---|---|
| `ActualCompleteCTarget(C,current,result_path,result_sha256)` | 完整同 C 输出绑定；缺原件时保持所有非 prefix 目标未付 |
| `ActualCompleteCTarget.bounds(a,b)` | 整个闭径向区间的 actual query 并集包围，或 `None` |
| `cap_metric_identity(current,atlas,attachment,cap)` | 完整 actual graph／target 身份与两个闭 disk 的零误差恒等式 |
| `inspect_cell(Prefix,Kernel,M,current,tail,spec,eta)` | 类型分派到原 prefix 判据或新尾来源连接，原四 Loewner 不变 |
| `coverage_state(...)` | 原整域 root／DFS／全部未访后缀责任 |
| `run(args)` | 当前真实输入的完整组合、临时账本、单份必要摘要 |

CLI 如下；大写占位值均必须来自一次未来真实同 job 构造及显式工作计划，本结果不填场、阈值、精度或成功结果。

```bash
python computations/geometry_20261115_current_C_ten_complete_relative_metric.py \
  --computations COMPUTATIONS \
  --directory ACTUAL_R409_DIRECTORY \
  --result-sha256 ACTUAL_R409_RESULT_SHA256 \
  --checkpoint-directory ACTUAL_R400_FROZEN450_DIRECTORY \
  --proof-directory RESULTS_DIRECTORY \
  --cuff-atlas ACTUAL_R413_ATLAS_JSON \
  --cuff-atlas-sha256 ACTUAL_R413_ATLAS_SHA256 \
  --continuous-e-result SAME_ACTUAL_F12F_DIRECTORY/result.json \
  --continuous-e-result-sha256 SAME_ACTUAL_F12F_RESULT_SHA256 \
  --eta EXPLICIT_ETA \
  --interval-bits EXPLICIT_BITS \
  --sqrt-bits EXPLICIT_SQRT_BITS \
  --initial-angular-depth EXPLICIT_INITIAL_DEPTH \
  --max-depth EXPLICIT_MAX_DEPTH \
  --max-visited-cells EXPLICIT_CELL_BUDGET \
  --budget-seconds EXPLICIT_SECONDS \
  --out NEW_OWNED_DIRECTORY_UNDER_RUNNER_TEMP
```

`continuous-e-result` 和其 SHA 可同时省略以取得诚实部分诊断；不可只提供一项。实际完整闭面 metric 结论必须有完整 radial target 覆盖。其余必填项不替数学门选值；$\eta$ 仅要求原 $0<\eta<1$ 范围，源没有默认声称 $10^{-6}$ 已通过。

## 418.9　输出、退出与清理合同

完整临时输出包括：

- `result.json`、`summary.json`；
- `large-arrays/input-binding.json`；
- 新准确场与新 cut DAG 的完整 identity；
- 完整十族 target binding；
- 同 f12f query 的完整实际状态、原后缀与原错误；
- 完整两帽同图来源；
- 原完整 root plan；
- `relative-metric-cells.jsonl.gz`；
- `coverage-and-pending.json`。

必要 summary 区分以下布尔量，不能只看 `completed`：

| 字段 | 确切含义 |
|---|---|
| `complete_active_partition` | 全部 active root 的完整闭细分已经结束，允许存在 unresolved terminal |
| `complete_active_relative_operator_bound` | 全 active cell 严格判据通过，且无执行异常 |
| `complete_two_cap_relative_operator_identity` | 原两帽同图来源已完全绑定；不等于帽区间 cover 已运行 |
| `complete_closed_relative_operator_bound_for_bound_accurate_target` | 完整 active 判据、两帽恒等式及同 C 原域条件全部满足 |
| `completed` | active partition 完整且无执行异常；不是完整任务成功 |

stdout 只打印一份必要 JSON，使用 `BEGIN_R418_CURRENT_C_COMPLETE_CLOSED_METRIC_SUMMARY` 与匹配的 END marker。必要 JSON 上限为90000B。超限仅报告原 summary 的 bytes/SHA 与未传范围，退出70；不分块、编码、截去科学未付地址或删除原件。

正常完成诊断返回0，包含 honest partial/unresolved；执行异常返回1；两者都不更改原 solver 的接受公式。若有 `GITHUB_OUTPUT`，成功必要读回设置：

- `closed_metric_summary`；
- `closed_metric_summary_bytes`；
- `closed_metric_summary_sha256`。

当前 source 不上传 artifact、不写 Git／Release、不自行清理 raw。未来 wrapper 必须在读回和子进程终止状态诚实后处理自有临时数据，不能把未传必要摘要当作已完成读回。

## 418.10　已付范围与未执行边界

本结果支付的是 **真实 current-C／准确十族对象到完整闭域 relative metric 消费者的源码连接与条件组合**。已有定理和已有精确对象保持各自身份：

- R400：完整准确十族 target／真实450／公共 $u$；
- R409：完整径向与共享 B、节点定义和原 seam 结构；
- R416：同 C/DAG 的准确 cut patch 和目标公共 chart；
- R413：真实原 cuff、固定帽目标 atlas；
- R417：实际同图帽 binder 及独立六 jet／balls API；
- R251：四个严格 Loewner 条件与有限闭覆盖；
- 原相位定理：活动片材料角平移／刚转，帽固定。

源码准备只做原文读取、编写、纸面推导和 bytes/SHA。**没有本地 import、AST、编译、fixture 或科学执行。** 没有实际 field 输入、没有跑闭 DFS、没有计算新 $E$、没有得到实际 metric 上界、没有将当前193或任何未来450重标为已经拥有这些输出。

准确新几何与原 rounded renderer 是不同对象；原 RK 轨迹误差未因这个组合器得到证明。完整 scalar speed、曲率、reach、embedding、held、非平面与原课题其他终门也不从相对 metric 源代码标签推出。实际执行若产生严格闭域 metric 证书，应另按其完整实际 run、输入、结果和未付范围登记。
