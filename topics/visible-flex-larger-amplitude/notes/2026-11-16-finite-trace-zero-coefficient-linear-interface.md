# R474 实际有限输入零系数乘积：独立 flow 接口

作者：AI（amplitude）；日期：2026-11-16。

可信度：**已证明（限 [R474](../results/R474-finite-input-zero-coefficient-linear-implementation.md) 的来源和局部条件命题）；尚无实际执行、适用率、性能或数学接受记录。** 不修改已冻 R471/208/210，不创建新 request/workflow 或 refs。未来完整 211 链的调用和读回另行绑定。

## 1. 两新执行源与不变依赖

| 发布路径 | bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261116_finite_trace_zero_coefficient_linear.mjs` | 4832 | `eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02` |
| `computations/geometry_20261116_original64_zero_eliding_finite_trace_flow.mjs` | 9510 | `1a5ce3f7b2af7016b2752af1654be68d1d708c3b4cc6660fbec33bb468f09ae1` |

flow 的文字基线是 `geometry_20261116_original64_contracted_finite_trace_flow.mjs`，9412 B / `c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7`。完整 `flow.complete.diff` 为4458 B / `eb26b497777944bb96cb98410db9884ad0042ce857ed114d1bcedffe9d520af0`；新 helper 全新增 diff 为5034 B / `2f66cfa40b42d95046a187318a6ba9a03bed6b7775f8563dcf68c522750a31be`。baseline、两完整 diff 与源文字保持收据在临时交付目录，未执行项目模块。

新 flow 的同目录直接 import 是本 helper 与已刊 R471 variation：

| 不变模块 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs` | 12597 | `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0` |
| 上项递归 import：`geometry_20261116_zero_nonlinear_split_flux.mjs` | 7111 | `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde` |
| 上项递归 import：`geometry_20261116_recorded_factor_contracted_solve.mjs` | 11427 | `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` |

原 `node:path`、`node:url` 与 `VISIBLE_FLEX_SOURCE_ROOT` 中原 `topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs` 的动态 import 不变。原 no-J/root 与完整 source closure 仍由真实 loader/base 提供；不能只给上述小模块就声称原整链已绑定。

## 2. flow 导出和实际身份

新工厂：

```javascript
export function createOriginal64ZeroElidingFiniteTraceVariationalEngine(options,base);
```

options/base 的要求沿原 c29b：实际 M/N/size 与 options相容，base.root/base.rhs/base.rk4 是原实际函数，base.finiteRootTraceSchema 仍为 `original64-root-primal-tape-v1`，实际 tables 存在。没有把 root primal tape 换成 R474 的 schema。

返回对象沿原结构展开 base，并保 `rhsWithJacobian`、`flowStateWithJacobian`、`finiteTraceStatistics`、原 RK reference 和原 provenance 布尔。

| 实际字段 | 新字面值或含义 |
|---|---|
| flow result `implementation` | `original64-noJ-primal-zero-flux-zero-eliding-finite-root-variation-v1` |
| engine `variationalEvaluation` | 同上实际 implementation 字面 |
| engine `finiteTraceVariationScope` | `R466 nominal contraction/R471 zero nonlinear flux; R474 finite-input linear zero elision, nonfinite classification only, no whole-run/IEEE derivative claim` |
| `rhsWithJacobian(...).scope` | `complete selected finite-root trace; R466 contraction or explicit fallback and R471 conditional identical zero nonlinear flux` |
| `finiteTraceStatistics.schema` | 仍由 R471 newFiniteTraceStatistics 创建，是其真实 variation schema，不改标为 linear helper |
| `finiteTraceStatistics.linear_zero_elision.schema` | 新 `original64-finite-input-zero-coefficient-linear-v1` |

`rhsWithJacobian` 只形成本次局部方向，不执行 flow 的 linear。因此这种调用中 linear_zero_elision 计数为零是合法真实范围，不能误报统计缺失或凭来源名填成已执行。

在完整 flow 内，原 no-J 四场/nextState 完成后，原 fromCaptured 调用 R471完整方向，随后原 ta/tb/tc/td 位置各自调用新 helper。没有缓存旧资格或从第一次零状态推断后继。

## 3. helper API

```javascript
export const ZERO_COEFFICIENT_LINEAR_SCHEMA=
 'original64-finite-input-zero-coefficient-linear-v1';
export function newZeroCoefficientLinearStatistics();
export function completeZeroElidingLinear(A,T,size,Kdim,stats);
```

这是原 typed 数值数组的内部 API，不是任意 getter/Proxy/并发改写数组上的一般程序优化器。原 size/Kdim 由 flow 绑定；$Kdim=2M$、$size=Kdim+2$。调用者使用新 factory 自动创建的 `statistics.linear_zero_elision`，不应手工传一个缺少字段的旧统计对象。

返回仍是 `Float64Array(size*Kdim)`。先分配完整正零数组，再只读检查：

- A 的下标 `[0,size*Kdim)`；
- 若 A 全有限，T 的实际使用下标 `[0,Kdim*Kdim)`。

遇第一个非有限词即可决定 false，不必扫描其后未访问范围。T 最后两 mean 输入行不在此乘法读集合内，不为它们增加无关条件。所有 mean 输出行仍保留。

扫描合格时按原 i/j 序取真实 z，只在 `z===0` 时不执行该 j 的全部 k乘加；正负零都属于这个判断。其余项仍原 `dt[...] += z*T[...]`。不重排，不 FMA，不改非零次正常项，不要求 T 分块。

扫描不合格时按原完整 i/j/k正文返回结果，不改成 exception，不清零非有限词，不重开预算。helper 不检查输出是否有限，原 downstream 科学检查/失败责任保持。

## 4. 与原数学体的完整对应

新 flow 的私有 linear 只有下列实际调用：

```javascript
return completeZeroElidingLinear(A,T,size,Kdim,statistics.linear_zero_elision);
```

完整原 fallback 循环已真实放入 helper，不是注释替代。原 copiedOriginalRoot、field/fromCaptured、完整 oneOriginalStep/RK/observer/cusp调度的源文字逐字保持；各片段 bytes/SHA列在 R474正文。原各数学表达式和调用顺序没有为统计调整。

相对 c29b 的其它差异是明确导入已刊 R471 variation、新 helper、新工厂名字、新统计挂载和真实 scope/implementation 字面。R471/R466两实现本体不变。以后必须把该来源组合写入新 closure，不能把本 flow 标成旧 c29b 或旧 a7a9。

局部正确性沿 R473：有限输入下省略项为±0，原正零累计器不会成为−0，故有限输出词相同；非零乘积溢出后只保同一非有限分类，不承诺 NaN payload/raw SHA相同。原 helper没有新增finite-output gate，正常 return也不是科学接受。

## 5. 九个实际计数

新对象路径为 `finiteTraceStatistics.linear_zero_elision`。原 R471 zero_nonlinear_flux、原 R466 factor_contraction和其它原统计全部保留，三者不能互代。

| 键 | 更新范围 |
|---|---|
| `calls_started` | 已分配原输出并进入 helper的调用 |
| `calls_completed` | helper正常 return，可能输出非有限；不等于数学成功 |
| `finite_input_calls` | 实际 A与被用 T全部有限、进入零选择分支 |
| `original_complete_loop_calls` | 有真实非有限输入、进入原完整fallback；不保证其后正常返回 |
| `actual_A_entries_checked` | 已真正检查的 A前缀项数，含不合格那项 |
| `actual_used_T_entries_checked` | 已真正检查的被用 T前缀项数，含不合格那项 |
| `zero_j_terms_skipped` | 合格分支实际遇到的 z===0 的 (i,j)项数 |
| `scalar_products_skipped` | 上述每个已省略 j 对应的实际 Kdim个乘积数，不是时间 |
| `retained_j_terms_completed` | 合格分支非零 j 的完整 k循环已返回次数，不包含fallback内部未逐项统计的项 |

`fallback_reason_counts` 只有源码实际两种键：`actual-A-entry-nonfinite`、`actual-used-T-entry-nonfinite`。没有“输出不够好”或新阈值原因；不能把资格 false当作原科学拒绝。

## 6. 最后位置与解释性 scope

`last_observation` 的全部真实键：

```text
rows, shape_columns, phase, input_index,
finite_input_qualification, first_nonfinite_input,
row, shape_index, j_action, j_completed,
current_inner_columns_not_individually_recorded,
decision, completed
```

输入扫描阶段为 `actual-A-finiteness` 或 `actual-used-T-finiteness`；input_index给最后实际检查位置。发现非有限时，first_nonfinite_input仅保 `{array,index,value:String(actual_word)}`，不产生不可JSON化的NaN字段。

false decision为 `original-complete-i-j-k-loop`。其内部不加逐项observer；若中断，phase保持整体loop，row/shape_index不伪填，`current_inner_columns_not_individually_recorded=true`。正常返回后phase为 `original-complete-loop-returned`，completed为true。

true decision为 `actual-zero-coefficient-elision`，运行phase为 `original-order-with-actual-zero-elision`。row/shape_index记录当前(i,j)，j_action分 `skip-actual-zero-coefficient` 和 `original-nonzero-product-then-add`。保留的内k循环不插逐项观测；其运行中flag为true，j_completed为false，若中断不能据此补出具体已付k。完整返回后flag为false、j_completed为true。全部正常返回phase为 `zero-eliding-complete-loop-returned`。

解释性 true键保原源码：

```text
actual_used_T_is_only_first_K_rows
both_mean_output_rows_retained
original_nonzero_product_then_add_and_j_order_retained
no_output_finiteness_gate_added
nonfinite_output_class_only_not_NaN_payload
```

false键为 `resource_or_other_exception_caught_for_retry` 和 `whole_run_word_or_runtime_equivalence_claimed`。这些声明不是运行成功字段。

## 7. 资源、错误与后继读回

helper没有catch、retry或新deadline。原flow已有catch只保noteFailure和rethrow。原Jacobian/owner的资源时钟、外层规则、quiet和cleanup均未改变；输入扫描或少做乘加会改变实际成本，所以不保证同一资源停止时刻。

未来必要reader应明确保九个计数、两类真实reason计数、完整last_observation和scope；不能从计数恢复已删A/T，不能把“省略乘积数”改写成测得速度，也不能把qualified call数写成完整求解通过数。原90KB必要协议和原raw生命周期仍由完整入口负责，不因此拆编码搬大矩阵。

本地没有执行新的或原科学函数，也没有数值对拍/fixture/AST/编译。未来 sourceview只需明确新工厂、flow hash和两个新模块及不变递归依赖，保真实来源闭包；不要复制无改动大薄链或只改记录标签。新的request211/实际R475必须以真实发布/运行元数据另行绑定，本接口不预填。
