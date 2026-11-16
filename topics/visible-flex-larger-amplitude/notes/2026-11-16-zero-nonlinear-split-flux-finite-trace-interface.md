# R471 零非线性 split 通量方向：源码与消费者接口

作者：AI（amplitude）；日期：2026-11-16。

可信度：**已证明（限 [R471](../results/R471-zero-nonlinear-split-flux-finite-trace-fast-path.md) 的来源与条件命题）；两新源尚未执行。** 本接口不提供实际适用次数、耗时、BVP 接受或连续目标证书。所有科学执行仅允许以后公开 Actions 的实际 owner 完成。

## 1. 交付与精确来源

本交付新增两个小执行模块、条件证明和本接口。没有新 request/workflow，没有修改 refs 或已冻 195/208 数学源，也没有复制其大调用者。未来 request210 的透明来源视图单独负责接线，不能由本接口先行声称已经运行。

| 发布路径 | bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261116_zero_nonlinear_split_flux.mjs` | 7111 | `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde` |
| `computations/geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs` | 12597 | `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0` |

新 variation 仍直接导入原 `geometry_20261116_recorded_factor_contracted_solve.mjs`：11427 B / `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59`。其 schema `original64-recorded-factor-complete-column-contraction-v1`、全部数值和 fallback 字节不变。该原模块与两新模块须位于真实同一 computations 目录。

完整文字基线为旧 variation `geometry_20261116_original64_contracted_finite_trace_variation.mjs`，12270 B / `e6be662ba5c795d4e3f91bbcead469482c746520b36b1d4c14a1c49b00dd2bb6`。临时交付目录保留两份 baseline、完整 `variation.complete.diff`（2853 B / `04adffbc67149f7409af5cc5436ca26af63e9de8df82b0389f01dd54261f92eb`）、新 helper 全文新增 diff 和文字保持收据。临时 manifest 只用于传递文件身份，不是科学结果。

## 2. 新 variation API

```javascript
export const FINITE_TRACE_VARIATION_SCHEMA=
 'original64-zero-flux-recorded-factor-contracted-finite-root-variation-v1';
export function newFiniteTraceStatistics();
export function completeFiniteRootTraceJacobian(rt,state,options,tables,statistics);
```

原参数、返回类型和布局保持：返回 `Float64Array((2*M+2)*(2*M))`，全部形状行、两个 mean 行和全部形状列均在。$M=112$ 仍为 $226\times224$。新实际 producer 必须使用新 schema，不能重标旧 e6be。

caller 用同一新模块的 `newFiniteTraceStatistics()` 创建统计，再交给同一新模块的完整入口。沿原 flow，统计对象在实际 flow 内持有，原结果的 `finiteTraceStatistics` 返回整个对象。不能为零分支绕过完整根方向入口，也不能用旧“zero H”标签生成响应。

完整入口仍按原正文依次执行资源检查、`dimensions`、`finiteRootDirection`、`splitRhsDirection`，全部正常返回后才增加 `complete_local_jacobians`。原 no-J/root 已由 caller 先实际完成，本模块不重跑。

## 3. helper 的实际 API

```javascript
export const ZERO_NONLINEAR_SPLIT_FLUX_SCHEMA=
 'original64-zero-nonlinear-split-flux-eligibility-v1';
export function newZeroNonlinearFluxStatistics();
export function certifyZeroNonlinearSplitFlux(
 rt,state,dL,tables,dims,pCoefficient,
 angularPartials,resourceCheck,stats);
```

该 helper 由新 variation 的私有 split 调用，不是从任意 JSON 造场/造根的独立入口。其输入必须来自同一次实际调用：

| 参数 | 实际来源和使用 |
|---|---|
| `rt` | 已返回 root/RHS；实际 L、g、e.rows、finiteTrace |
| `state` | 完整 $2M+2$ 状态；要求形状零，不要求两个 mean 零 |
| `dL` | 未改的完整 finiteRootDirection 真返回 |
| `tables` | 原 freq/cs/sn 字面表，不假定理想三角正交 |
| `dims` | 原 dimensions 的 M/N/J/K；快路径还要求安全正 N |
| `pCoefficient` | 原 split 前段已经形成的数组，不改形成式 |
| `angularPartials` | 原函数本体 callback，保其全部括号和 AD |
| `resourceCheck` | 原单调绝对 deadline 检查，不建立新钟 |
| `stats` | 本次新增的 zero_nonlinear_flux 统计对象 |

返回 true 表示全部局部资格正常付完，调用者保留原正零 dFlux；返回 false 执行原完整角循环。任何 throw 原样传播，不捕获后 false/retry。输入数组只读，唯新增统计可写。

没有新增 CLI、环境变量或时间/迭代/Armijo/FD/native/fullDN 阈值。资源检查沿原 `VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC`。

## 4. 唯一执行插槽

原系数、pCoefficient、dFlux/dlv/duv/df/result 全部分配之后，新增条件如下：

```javascript
if(!certifyZeroNonlinearSplitFlux(rt,state,dL,tables,dims,pCoefficient,
    angularPartials,resourceCheck,statistics.zero_nonlinear_flux)){
  // 实际源码保留原完整角循环全文。
}
// 实际源码保留原完整末装配和两个 mean 行全文。
```

上面的注释只说明位置；真实模块没有用空注释取代数学正文。新路径也保留原工作数组分配，不另造只填四块槽的小矩阵。

helper 真实检查无 supplied guess、空 accepted updates/零 iterations/原成功返回、当前全部形状零、根零、角行 P/Pt/L/K/U 零和原初始 dL 字词。每个角调用原 angularPartials；factor 四个实际词有限且值为零。每个完整 Q/Π 方向对保原唯一可能非零项、原 p/pt、原左结合 dFactor，并检查有限。全部实际使用的 sine/cosine、频率、已形成系数都须有限；不拿未使用 a.q/bm 作新条件。

R471 已分别证明：Q 列 dlv 原初始正零、仅有零增量，故确为正零；Π 列 p/pt 是原字面正零；跨 j 项在已核有限表下仅为有符号零。因此保 `(-m*0+q)*sine`、`(-m*ell+0)*sine` 和 leading +0，原唯一主项即使下溢成负零也保原累加词。末端 `linear+dFlux` 的加零位置仍原样。

## 5. 新统计与真实更新时间

新增对象是 `statistics.zero_nonlinear_flux`，不替换原 `statistics.factor_contraction` 或 root/完整矩阵计数。

| 键 | 真实含义 |
|---|---|
| `schema` | helper 的独立资格 schema |
| `calls_started` | helper 已开始的实际调用数 |
| `calls_completed` | 正常 true/false 返回次数，throw 不增加 |
| `actual_zero_trace_candidates` | 已核空成功轨迹及 state/root 零；完整角资格尚可能失败 |
| `certified_zero_dflux_calls` | 完整资格通过且保留 +0 通量的次数，不是全矩阵/阶段/求解接受 |
| `original_angular_fallback_calls` | 正常 false 次数，不保证后续原角循环完成 |
| `sparse_direction_entries_checked` | 已查原 dL 槽，包括后来不合格调用的已查槽 |
| `complete_angular_rows_checked` | 全部方向对已检查完成的角行数 |
| `complete_shape_direction_pairs_checked` | 完整有限检查已完成的实际方向对数 |
| `fallback_reason_counts` | 源码实际 false 原因计数，不推填缺失记录 |
| `last_observation` | 最后调用的阶段/位置/分支/完成状态 |

last_observation 真实键为：

```text
mode_count, angular_rows, shape_columns,
phase, angle, direction_pair, sparse_row,
decision, reason, detail, completed
```

phase 按实际执行依次可为 `actual-trace`、`actual-zero-state`、`actual-sparse-initial-direction`、`original-angular-factor-and-sparse-directions`；成功选择为 `original-positive-zero-dflux-retained`。正常 false 的 decision 是 `original-complete-angular-loop`，正常 true 为 `retain-original-positive-zero-dflux`。throw 时不得把最后未完位置重写为已完成。

false 原因的完整字面集合：

```text
actual-shape-or-positive-angular-count-unavailable
actual-empty-unsupplied-successful-trace-unavailable
actual-target-factor-nonfinite
actual-shape-state-not-zero
actual-returned-root-not-zero
actual-direction-is-not-original-sparse-initial-word
actual-frequency-or-formed-p-coefficient-nonfinite
actual-angular-row-shape-unavailable
actual-angular-primal-row-not-zero
original-factor-not-finite-zero-with-finite-partials
used-literal-cosine-or-sine-nonfinite
original-sparse-angular-direction-nonfinite
```

detail 只保实际源码写入的索引/词字符串。源码解释性 true 键为 `actual_primal_and_finiteRootDirection_always_retained`、`same_original_angularPartials_factor_evaluated`、`unused_q_or_bm_not_eligibility_gates`、`literal_trigonometric_orthogonality_not_assumed`、`original_complete_final_assembly_and_both_mean_rows_retained`。false 键为 `resource_or_other_exception_caught_for_retry`、`whole_run_word_or_runtime_equivalence_claimed`、`continuous_or_IEEE_rounding_map_derivative_certificate_claimed`。这些是方法范围声明，不是数值成功旗标。

没有新增替代 R466 contraction 的 backend。零分支由 decision 和实际计数表示。空更新轨迹本来就不调用 contraction；新实现不伪造 factor-contraction 调用数或节省次数。

## 6. 原计数、异常与必要读回

`root_returns/zero_update_returns/normal_returns/fallback_returns`、`original_root_evaluations/original_line_trials`、`return_iteration_histogram` 仍由原 finiteRootDirection 全文更新。一般已接受更新和原 contraction 统计仍按原实际执行增加。

原 `complete_local_jacobians` 仅在 split 正常返回后增加。helper 完成但末装配因原系数/除法/非有限失败时，局部资格数可增加，完整矩阵数不会增加。原 no-rounding-map、primal/RHS 未修改、无严格 tangent roundoff bound、无强制分支邻域证明等声明不变。

必要 reader 应保这些小统计的实际字段、原错误和未完成范围；不能由聚合计数恢复已删除状态，也不能由某次总数推断195每个阶段合格。原单90KB协议不变，不能拆包编码搬矩阵。源码存在、新源被实际执行、统计已读是三个不同事实。

helper 不捕获资源或其他异常；普通 false 不重开时钟。检查过的零候选后来 fallback，可能重新计算原纯 angularPartials，但不重跑 primal/root、不换状态。该额外工作及被跳过的角循环会改变成本和资源停止位置，所以不能声称 whole-run word/runtime 等价。

## 7. 后续 request210 的透明来源接线

未来新调用链需明确登记两新模块及原2592，并将原 flow 的 variation import 指向本新模块。loader/协议/runner/reader 中说明实际 variation 的身份字段必须依据各自完整旧源 pin、精确锚次数、生成全文 SHA 和新 schema 独立绑定。保原 no-J/root 来源，不能只改标签而继续执行旧 e6be。

原 flow 完整 `finiteTraceStatistics` 返回机制可保。若某必要 reader 只软选旧统计键，应在新 view 显式加入 zero_nonlinear_flux，否则不得声称已读本次选择效果。source-view 生成位置、实际输出字节身份及整个调用闭包归未来独立接口；本交付不预填它们，也不预填 run/job/现场。

本地只做源码文字、JSON/bytes/SHA/全文 diff 与纸证，没有科学导入、AST、compile、运行、测试、fixture 或微基准。以后可直接接原完整 Actions 链，不增独立短跑或数值验收前门。

## 8. 当前已付与未付

已付是实际资格的充分性、正零通量的条件逐词论证、原 fallback/统计/完整末装配保持以及两新源身份。仅角方向形成从 $O(NM^2)$ 改为候选检查的 $O(M^2)+O(NM)$；原末装配和稠密 linear/RK 未被加速。

未付是实际适用率/耗时/全链收益、一般 R466 formal map 浮点误差、准确连续目标、完整 native/fullDN/FD/audit 和最终接受。原资格 false、资源停或最终门失败均须据真实 Actions 原输出分别归责。
