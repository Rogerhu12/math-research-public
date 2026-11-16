# R523 — 真实入射切向行支撑的完整 linear 接口

作者：AI（amplitude）；日期：2026-11-16。

状态：**源码与条件证明已完成；没有执行新的科学程序，没有新 request/workflow、性能结果或接受结论。** 本接口只登记两个独立源，后继完整入口须显式接入真实新工厂及统计。正在运行的 211、215、222 不改。

## 1. 发布文件和来源

| 路径（topic 内） | bytes | SHA-256 |
|---|---:|---|
| `computations/geometry_20261116_finite_trace_actual_input_support_linear.mjs` | 6246 | `e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3` |
| `computations/geometry_20261116_original64_input_support_finite_trace_flow.mjs` | 9504 | `14c691bec5ca228495027185ed642730d90d17ce65467ac76662c9407cd7d960` |
| `results/R523-actual-tangent-row-support-and-complete-linear-products.md` | 16055 | `4c73a3ceb0623126506585816082f8baea6cbe1e90d4ed5b969c96055403e741` |

本接口为第四件；临时 publication manifest 只用于交接这四份确切字节，不作为科学输入，不必入 Git。没有将展开大 source views、原 A/T 数据、日志或运行现场作为本次发布物。

基线为已刊 R474：

- helper：4832 B / `eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02`；
- flow：9510 B / `1a5ce3f7b2af7016b2752af1654be68d1d708c3b4cc6660fbec33bb468f09ae1`；
- 正式来源：`9ff15fddedfa1be31f9e486b225c4a64c9f6e7fd`。

新 flow 仍导入实际 R471 variation `geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs`，12597 B / `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0`。其原零通量 helper 7111 B / `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde`、R466 收缩 helper 11427 B / `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` 及原 loader/tables/root 来源不变。不能把新 flow 接回旧 e6be variation 后仍称这一组合。

## 2. 它解决的实际切点

R467 的 actual208 首零 H 已返回残差零，但原 core 在 iteration 0 先求完整 `evaluate(...,true)`，内部仍形成了 27772 个完整局部 Jacobian。已知 5774.443653623 秒没有分项计时，不能换算成新实现可省多少时间。

R474 的合格分支仅跳 `A[i,j]===0`。对保留项它仍遍历所有 k，包括实际 `T[j,k]===0`。R523 只在同次实际 T 扫描内收集非零列地址，避免这些额外零乘积；全输出、原 j 序和原误差责任保持。原初猜、root、J、mean、predictor、FD、fullDN、audit 都不因“零 H”被删除。

这不是 block-only API。T 可以完全稠密，可以包含任意非零次正常词，也可以继承一般早期子步形成的混模方向。只有实际词等于正零或负零才不入支撑；没有容差、秩或非零列门。

## 3. Helper API

文件：`geometry_20261116_finite_trace_actual_input_support_linear.mjs`。

```javascript
export const INPUT_SUPPORT_LINEAR_SCHEMA =
  'original64-finite-input-row-support-linear-v1';

export function newInputSupportLinearStatistics();

export function completeInputSupportLinear(A, T, size, Kdim, stats);
```

调用者使用原普通数值 typed arrays 和相容维度，且调用内没有并发修改。原 flow 给出 `Kdim=2*M`、`size=Kdim+2`；本 helper 不另建立维度/有限输出科学门。原 baseline 的完整维度、来源和局部 Jacobian 检查仍在上游。

返回新 `Float64Array(size*Kdim)`，所有槽初始正零。M=112 时始终有全部 226 行、224 列；它不是稀疏输出格式。统计之外不写 A/T，也不暴露可修改其数值的共享表。

### 3.1 实际资格及索引的创建

先按原行优先地址检查 A 的全部 `size*Kdim` 项；第一处非有限值即确定不能采用快路径。只有 A 完整有限才继续 T 的前 `Kdim*Kdim` 项。

T 扫描也保持原行优先顺序。在每一行内，当前有限词 `value!==0` 时追加 k 地址；否则只记录这个实际零词。每行完成后才写下一行偏移并增加完整索引行数。遇到非有限 T 值时不使用部分索引，直接转原完整 fallback。

T 的末两个 mean 输入行本来不进入原乘法，故不扫描、不把其有限性增加为资格。两个 mean **输出行**则使用 A 的真实完整两行，仍计算全部形状方向。

索引表每次调用新建，离开调用即不再由实现保存。没有跨现场、RK 子步、stage 或运行缓存；不从上次支撑推出当前零项。表只保存整数地址，不保存或替代 T 的实际数值词。

### 3.2 两个执行分支

不合格分支照原完整三循环：

```javascript
for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
 const z=A[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
}
```

合格分支保持原 i/j 次序。z 为任一种零时沿 R474 省去 K 项；其余情况按当前 j 的升序列地址执行：

```javascript
const k=columns[entry];
dt[i*Kdim+k]+=z*T[j*Kdim+k];
```

原乘法和加法的括号未重写，不合并跨 j 项，不使用三角正交、矩阵分块假设或重新形成的系数。支撑为空的行、只有一个非零词的行、完整稠密行，都由同一实际扫描处理。

## 4. 数值承诺和边界

[R523 证明](../results/R523-actual-tangent-row-support-and-complete-linear-products.md) 给出三个局部正常返回承诺：

| 实际分支 | 已证明的返回语义 |
|---|---|
| 任一被用输入非有限 | 执行原完整三循环，保原输入及全部行列 |
| 所有被用输入有限，最终某槽有限 | 该输出槽与原完整乘积的 binary64 词相同 |
| 所有被用输入有限，最终某槽非有限 | 正无穷、负无穷、NaN 分类相同；不声明 NaN raw payload 相同 |

正负零都可被选为省略项，但原正零累计器在有限阶段不会变成负零。非零输入所形成的下溢乘积仍执行；有限输入所形成的乘积/加法溢出也仍执行。这里没有假设“输入有限，所以全部中间量有限”。

helper 没有 finite-output throw；正常返回计数不表示矩阵有限、阶段接受或整链完成。若下游观察 NaN raw 编码、资源时刻或其它未在局部命题中规定的行为，不得由分类命题补填 whole-run 逐字结果。

原 resource/其它异常不捕获重试。新数组或索引分配失败也直接传播。原 flow 的 catch/noteFailure 仍只记录并 rethrow，不重开原时钟。输入扫描和地址组织可能改变开销及停止范围，未承诺同一个资源停点。

## 5. 实际 flow 工厂

文件：`geometry_20261116_original64_input_support_finite_trace_flow.mjs`。

```javascript
export function createOriginal64InputSupportFiniteTraceVariationalEngine(
  options, base
);
```

它保原 base 的 root/RHS/originalRk4、实际 `finiteRootTraceSchema`、字面 tables、M/N/size 来源检查，返回原完整 engine 形状。新增实现身份：

- implementation / variationalEvaluation：`original64-noJ-primal-zero-flux-input-support-finite-root-variation-v1`；
- 统计路径：`engine.finiteTraceStatistics.linear_input_support`；
- 私有 linear 唯一调用：`completeInputSupportLinear(A,T,size,Kdim,statistics.linear_input_support)`。

相对 R474 的完整文字差异只含下表；原完整数学函数正文没有其它编辑。

| 位置 | 原 R474 | 新 R523 |
|---|---|---|
| 来源注释 | R474 finite linear | R523 actual T-row support |
| helper import | completeZeroElidingLinear / newZeroCoefficientLinearStatistics | completeInputSupportLinear / newInputSupportLinearStatistics |
| 导出工厂 | createOriginal64ZeroElidingFiniteTraceVariationalEngine | createOriginal64InputSupportFiniteTraceVariationalEngine |
| 统计初始化 | linear_zero_elision | linear_input_support |
| 私有 linear | 原 helper 调用 | 新 helper 调用 |
| 两处 implementation 字符串 | zero-eliding | input-support |
| 范围文字 | R474 finite zero elision | R523 actual finite T-row support |

`copiedOriginalRoot`、`rhsWithJacobian`、`field`、`fromCaptured`、`oneOriginalStep`、observer、完整普通/cusp 调度保原字节。尤其每个原步骤仍先执行全部四次实际 no-J root/RHS、形成 nextState，再在其复制现场形成完整 Aa/Ab/Ac/Ad，随后用原 RK 表达式传播 ta/tb/tc/td 和 nextTangent。原完整两 mean、端口缩放和上游/下游全部列不变。

## 6. 必要统计合同

新统计 schema 为 `original64-finite-input-row-support-linear-v1`，共十四个数值计数。它们只反映实际调用和已到达语句，不由输入名称或假设的块结构预填。

| 字段 | 真实含义 |
|---|---|
| calls_started | 已完成原输出分配、进入 helper 记录的调用数 |
| calls_completed | helper 正常 return 数，不表示输出有限 |
| finite_input_calls | 实际 A 与被用 T 全部有限、进入合格分支数 |
| original_complete_loop_calls | 已选原完整 fallback 的调用数 |
| actual_A_entries_checked | 实际检查过的 A 项数 |
| actual_used_T_entries_checked | 实际检查过的 T 前 K 行项数，含发现非有限的项 |
| zero_j_terms_skipped | 实际已选择并完成的零 A 段数 |
| scalar_products_skipped | 零 A 段的 K 项，加已完成非零 A 段内零 T 项 |
| retained_j_terms_completed | 合格分支中整个保留段已完成数，含实际空支撑段 |
| actual_nonzero_T_words_indexed | 资格扫描中实际有限非零 T 词的地址数 |
| actual_zero_T_words_seen | 资格扫描中实际有限零 T 词数 |
| T_rows_indexed | 已完整扫描且写完末偏移的 T 行数 |
| zero_T_products_skipped_after_nonzero_A | 已完成非零 A 段内，实际省去的零 T 项数 |
| retained_scalar_products_completed | 已完整返回的支撑内层段中的保留乘积数 |

T 的两个词计数和完整行计数也可能来自后来遇到非有限项的部分扫描；不能把它们全解释成成功快路径的支撑量。后两个乘积计数只在整段内层循环正常返回之后增加，故中断时不假造部分完成 k。

`fallback_reason_counts` 保实际 `actual-A-entry-nonfinite` / `actual-used-T-entry-nonfinite` 的次数。未发生原因不自动补作某个科学结果。

`last_observation` 完整保留：

- rows、shape_columns；
- phase、decision、completed；
- input_index、finite_input_qualification、first_nonfinite_input；
- support_rows_completed、support_entries_completed；
- row、shape_index、j_action、j_completed；
- selected_T_row_nonzero_columns；
- current_inner_columns_not_individually_recorded。

资格 null 表示尚未确认；false 表示已选完整 fallback；true 表示完整实际有限扫描已付。first_nonfinite_input 保数组、真实地址和原值字符串。不能把 null 与 false 合并。

保留段的 k 循环不插逐项统计；运行中 `current_inner_columns_not_individually_recorded=true`，返回后才清。fallback 内完整 i/j/k 也不插观察，因此中断时只保整体循环尚未返回，不杜撰内部地址。所有 scope 布尔字段也应完整传递，不能将 `calls_completed` 升格为原科学通过。

## 7. 后继完整入口的最小来源衔接

本次只有两个可执行源与条件文稿，没有新增运行号。未来完整 caller 必须显式完成以下实际接线：

1. 保原 R466/R471/R474 来源身份作祖先，实际 import 新 flow 文件并调用新工厂；不能只改 implementation 标签。
2. 新 flow 与 helper 位于真实 computations，全部 loader/worker/config/source receipt 核实际新 SHA；当前原来源字段不能继续冒用旧 1a5ce3f7。
3. 原 finite-trace root/更新/局部 J 统计全保；必要 reader 新增读取 `linear_input_support` 的十四计数、fallback 原因和完整 last_observation/scope。旧九字段选择器不会自动覆盖新增字段。
4. 完整 576 stage、226×224 方向/两个 mean、全部输入、原 H/J/R273、FD/fullDN/replay/audit、原资源预算/精度与数学门按实际原入口执行；本组件不提供替代接受判据。
5. 原单份必要摘要 ≤90 KB、超限处理、quiet/清理照完整 caller 原合同；大矩阵/临时地址表不借此接口要求重新永久保存。

这些是未来真正调用 R523 的来源和必要读回责任，不是当前已有运行的新前门。没有创建独立对拍、fixture 或 benchmark，也没有要求额外全解析 J。

## 8. 参数、复杂度与未付项

没有新增科学参数。原 M/N、RK/cusp 网格、finite-root 策略、误差阈值及科学总钟原样由 caller 提供。没有稀疏阈值或块大小选择。

若 A 第 j 列有 $a_j$ 个实际非零词、当前 T 第 j 行有 $s_j$ 个实际非零词，R474 保留 $K\sum_j a_j$ 个乘积，R523 保留 $\sum_j a_js_j$ 个。完整有限扫描、i/j 选择、输出分配仍存在，完全稠密 T 还增加地址组织开销。这个操作计数关系不等于耗时或适用率数据。

R470 给出的零现场块结构可解释为何当前 T 可能稀疏，但实现不使用该推断作为资格。actual208 已删除现场也不被重建为一套假支撑记录。完整 J、两 mean、predictor 和后继科学责任均保。

本地仅进行源文本构造、字节/SHA 与完整差异记录；没有 import、AST、compile、科学计算、测试或 fixture。本次只登记新源、局部调用组合及其条件命题；未来完整调用链的实际执行、速度和终态事实均不得预填。
