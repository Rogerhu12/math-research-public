# R474 — 完整有限轨迹的实际有限输入零系数乘积实现

作者：AI（amplitude）；日期：2026-11-16。

可信度：**已证明（限下述实际输入条件、源码组合和局部语义）；新源码尚未执行，实际条件计数、速度、完整求解和最终接受均未付。**

## 474.1 结论与边界

本结果将已发表 [R473](R473-zero-coefficient-elision-in-complete-finite-trace-linear-products.md) 的最窄切点写成两个独立小源：一个完整线性乘积 helper，以及一份新 flow。每一次实际 `linear(A,T)` 都从当前数组判断有限性；只有全部实际使用输入有限时，才跳过 `z===0` 的 $j$ 项。不合条件执行原完整 $i,j,k$ 循环，不拒收状态、不加新的 finite-output throw，也不改原数学接受门。

新 flow 消费已发表 R471 variation，后者保原有限根轨迹并提供条件零非线性通量路径。R474 新增的数学切点仅在线性乘积。相对 R466 flow 的完整文本差异同时包含这项**显式导入已发表 R471**，不能把新 flow 的来源说成仍执行旧 e6be variation。

原 no-J 四次 field、复制现场、fromCaptured、完整 RK 合成、cusp schedule、observer、两个 mean、端口和下游链均不改。$M=112$ 时仍返回完整 $226\times224$ 乘积，入射 tangent 可以稠密；不要求 R470 的模态分块，也不由第一步零状态推断后继现场。

## 474.2 精确来源

| 来源 | bytes | SHA-256 |
|---|---:|---|
| [原 R466 flow](../computations/geometry_20261116_original64_contracted_finite_trace_flow.mjs) | 9412 | `c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7` |
| [新 linear helper](../computations/geometry_20261116_finite_trace_zero_coefficient_linear.mjs) | 4832 | `eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02` |
| [新 flow](../computations/geometry_20261116_original64_zero_eliding_finite_trace_flow.mjs) | 9510 | `1a5ce3f7b2af7016b2752af1654be68d1d708c3b4cc6660fbec33bb468f09ae1` |
| [R471 variation](../computations/geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs) | 12597 | `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0` |
| [R471 helper](../computations/geometry_20261116_zero_nonlinear_split_flux.mjs) | 7111 | `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde` |
| [原 R466 contraction](../computations/geometry_20261116_recorded_factor_contracted_solve.mjs) | 11427 | `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` |

R473 证明为 14166 B / `93d57da3cdb0cac63f5ceb2195772b709d1ece0f1547ae900a13befc4bf4b41e`；其正式发表来源为 `f7b46ef6f8bd81385e71f193377e16c5f8c4e755`。R471 四件已发表于 `d004a4e421408e9b4b7b7dcd871d661f1d28b3e1`。本次没有改这些原件。

新 helper schema 为 `original64-finite-input-zero-coefficient-linear-v1`。新 flow 的 implementation / variationalEvaluation 为 `original64-noJ-primal-zero-flux-zero-eliding-finite-root-variation-v1`；新导出工厂为 `createOriginal64ZeroElidingFiniteTraceVariationalEngine`。原 caller 不能只改标签而仍调用旧工厂。

## 474.3 实际调用和有限性选择

沿原 flow，令 $K=2M$，$size=K+2$。新私有 linear 只调用：

```javascript
return completeZeroElidingLinear(A,T,size,Kdim,statistics.linear_zero_elision);
```

helper 首先仍创建 `new Float64Array(size*Kdim)`，得到完整正零输出数组。然后按实际下标扫描 A 的全部 `size*Kdim` 项；若未遇非有限值，再扫描原乘法实际读取的 T 前 `Kdim*Kdim` 项。扫描只读，不改变输入词。

只要发现一个非有限输入，helper 记录该真实数组/下标/词字符串，立即选择原完整循环；不需要把其余扫描也做完才能确定不能使用本快路径。它明确保留已检查前缀和剩余未检查范围的语义，不声称 false 分支已经扫描完全部输入。T 最后两 mean 行本来不被本乘法读到，不纳入资格。

因此，资格 true 恰支付 R473 的实际有限输入充分条件。资格 false 不导致拒收或新的 throw；原 `0*Infinity` / `0*NaN` 及其真实后续运算会在原完整循环中照常发生。

## 474.4 两条完整执行分支

### 474.4.1 不合条件时的原完整循环

helper 中 fallback 的数学正文逐字保留：

```javascript
for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
 const z=A[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
}
```

原输出分配、全部行、全部 j/k、原乘法先于加法、原存储布局均同。没有在 fallback 内插零判断、按列 observer、有限输出检查或捕获重试。统计只在进入和正常返回处记录该完整循环范围；若中断，不造某个已经完成的内部 k。

### 474.4.2 实际有限输入时的零项选择

新合格分支保持原 i/j 顺序。每个实际 `z=A[i*Kdim+j]`：

1. 若 `z===0`，保当前输出不写，记录这个 j 项和其真实 $K$ 个省略乘积。
2. 否则执行原 `for(k) dt[...] += z*T[...]` 表达式，保其乘法、加法和 k 顺序。

该判断包含正负零，不采用容差。非零次正常系数不会被删；其乘积即使下溢为负零，也仍按原表达式执行。全部结果槽保留，两个 mean 输出行照实际 A 参与运算，不被新建默认值替代其非零责任。

## 474.5 实现的条件正确性

**定理 474.1。** 在原普通 typed 数组无外部并发修改、原维度相容和原 binary64 RN 先乘后加语义下，helper 正常返回的结果满足：

- false 分支执行原完整乘积；
- true 分支的所有最终有限结果词与原完整乘积相同；
- true 分支非有限结果的正无穷/负无穷/NaN 分类与原完整乘积相同，不声明 NaN raw 编码相同。

**证明。** false 分支直接由完整源正文和原正零数组得到。true 分支实际扫描支付全部被用 A/T 有限。此时任何被删 z 项的乘积都是某种零。由 R473 引理 473.1，原正零累计器在有限期间不会变为负零：有限 binary64 和的准确非零值至少为一个最小次正常量，而准确抵消在 RN 下为正零；保留乘积先舍入成负零也不会使正零累计器变负零。故删去任一种零乘积不改有限累计词。保留项仍按原顺序执行相同乘加。

若保留项溢出，删零仍保持无穷符号或 NaN 分类；非有限累计不能恢复为有限。R473 已证明同一非零项首次产生非有限的原 j 相同。因此有限输出词和非有限分类结论成立。证毕。

helper 不扫描输出，也不因输出非有限另抛异常。`calls_completed` 只表示该函数正常 return，并不表示结果有限、矩阵通过、阶段接受或原科学完成。原 linear 本来没有输出 finite gate，这个事实保持。

新代码不声称 NaN payload/字节相同。原下游按同一有限性或分类谓词观察这些输出时，取得相同 bad mask 的条件结论沿 R473；若下游依赖 NaN raw 编码、资源时刻或尚未执行的其它行为，不能由此推填。

## 474.6 原 primal、RK 与完整责任保持

本次相对原 c29b 的文字比较确认：

| 完整原正文片段 | bytes | SHA-256 |
|---|---:|---|
| copiedOriginalRoot | 403 | `6a0d9844d99f18895ee7d08ae5624b1955621215869f93679ab7c496ee78de7b` |
| field 与 fromCaptured | 917 | `20d46881625e38f1ce57dfc2b289681b415cfea8982761271949c7ecb7db7be6` |
| oneOriginalStep、observer 与完整 cusp/普通网格调度 | 3501 | `1b734e197cbd2c66d59acc9bc66b76e5fcf23409fb77dd0b74849410d0fa4f39` |
| 搬入 helper 的原 fallback i/j/k 正文 | 132 | `51a725e36107b4996737b84e0216b68637a454f982078a1e2a8fc774295ee57b` |

这些是源文本身份，不是科学测试记录。它们明确保原先完成全部 no-J 四场和 nextState、再消费复制现场方向、再按原括号组合 ta/tb/tc/td/nextTangent 的顺序。没有借稀疏条件删除 field、列、mean、port 或 observer。

R471 仍每次真实调用完整 finiteRootDirection，原 root/line/更新计数和原 complete-local 语义不变。R474 只在原统计对象再加入独立 `linear_zero_elision`，不会把已选局部实现当成新 root 或新接受场。

本次不改原源码来源 loader、QR、BVP、trial、FD、fullDN、replay/audit 或原 owner；以后完整链接线必须明确新 flow 工厂和全部源 SHA，不能由本结果预先声称下游已运行。

## 474.7 统计和中断范围

helper 的统计区分正常返回、实际有限资格、完整 fallback、实际已查 A/T 项、实际省略 j 项/乘积数和已完整执行的合格非零 j 项。只按已到达分支增加，不从未知现场推填。

合格分支最后位置保 row/shape_index/j_action/j_completed。保留的原 k 循环不插逐项 observer；运行中明确 `current_inner_columns_not_individually_recorded=true`。若在该段中断，不能声称具体哪些 k 已完成。fallback 更保原三循环全文，所以内部 i/j/k 也不逐项观测，保最后整体 phase 和未完成标志。

原资源/外部异常不捕获、不重试、不重开预算。helper 不建立新钟，也没有比原 linear 新增资源阈值；flow 原已有 noteFailure/catch 仍记录并 rethrow 原错误，不吞掉。额外输入扫描或跳过乘加改变成本，不能声称相同资源停止位置或 whole-run 逐词/时间等价。

## 474.8 当前状态

两新源合计仅包含这个小 helper 与一份独立 flow；已刊 R471/R466 源不改，没有复制大薄链或创建新 workflow。后继 request211 的来源 view、owner、必要读回和实际结果另付。

本地只写文字、JSON/bytes/SHA、完整 diff 和条件证明；没有导入、AST、compile、科学计算、测试、fixture 或 benchmark。局部操作量可从原 $(K+2)K^2$ 乘加变为实际非零 A 项数乘 K，加完整输入扫描；没有实际 Z、耗时、适用率或全链加速倍数。

已付为实际实现与 R473 条件命题的逐项对应、原 fallback/完整 RK 保持、来源与真实统计范围。所有实际求解、性能、一般方向误差、原数学门与最终目标仍须公开 Actions 的真实输出支付。
