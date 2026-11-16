# R523 — 同次真实切向行支撑与完整有限轨迹线性乘积

作者：AI（amplitude）；日期：2026-11-16。

可信度：**已证明（限本文的实际输入条件、源码组合和局部运算语义）；新源码尚未执行，真实适用率、运行时间、完整求解及最终接受均未付。**

## 523.1 结论

本结果在已刊 R474 的线性乘积位置增加一项实质工作省略：在原来就要进行的实际有限性扫描中，保存当前入射切向矩阵每一行的非零列地址。之后仍按原 $i,j$ 次序遍历，只对该实际行的非零列计算原乘后加表达式。

新实现仍返回完整 $(K+2)\times K$ 数组，$K=224$ 时为完整 $226\times224$。每个输出槽的非零乘积保原 $j$ 累加顺序；两个 mean 输出行照其真实系数参加计算。所有输入资格不满足时，执行原完整三循环。没有增加 finite-output 门、科学接受条件、时钟、异常重试或缩列。

与 [R474](R474-finite-input-zero-coefficient-linear-implementation.md) 的区别很具体：R474 只省略 $A_{ij}=0$ 的整段工作，保留的每个非零 $A_{ij}$ 仍乘遍 $T$ 的全部 $K$ 列；R523 继续省去这些保留段中实际 $T_{jk}=0$ 的项。它不要求模态分块，不用零 H 标签选算法，不复用前一场的支撑，也不改 R471 的非线性通量条件。

## 523.2 实际 208 的动机和不能省去的责任

已刊 [R467](R467-actual208-contracted-trace-resource-partial-and-complete-readback.md) 完整读回报告：actual208 的首个零 H 请求为 `jacobian:false,audit:false`，在 5774.443653623 秒后返回 `converged=true`、残差零；外部返回没有 full J，audit 为 null。它同时实际记录 27772 个完整局部 Jacobian、27772 个零更新有限根返回，接受的 root 更新和 line trial 均为零。这些是已发表实际，不是本次重新下载日志或本地重算。

原 `78718-tail-tangent-core.mjs` 的 `initial(target)` 已经创建完整零数组并由当前 target 和原图/增益形成初猜；零 target 在原有限合法系数下本来传播为零形状。原 `solve` 的每轮开头却无条件调用：

```javascript
const ev=evaluate(states,target,true,scales);
```

只有这份完整实际评价返回之后，才检查残差并 break。因此 iteration 0 残差零不免除该轮完整局部变分。原 predictor 可以继续消费这些已经求出的 flow Jacobian；外部没有请求返回 J，不等于内部没有形成它。

原首 H 的 meanSlope、meanSecond 也不是零；R467 已回的两个背景值和零修正分别记录。R523 不把零形状当成两个 mean 状态为零，不删原 mean 积分、端口、预测、末边界、FD 或 audit。实际 208 没有 dFlux、linear、root 的独立计时，所以不能把这 5774 秒的某个比例归给新切点，也不能据汇总零更新计数补称每个已删除现场均满足 R471 的全部资格。

[R470](R470-zero-shape-finite-root-trace-full-local-block-variation.md) 已给条件下的完整局部模态块和准确实传播命题；[R471](R471-zero-nonlinear-split-flux-finite-trace-fast-path.md) 的实际源支付特定零通量路径，R474 支付零 A 项省略。R523 不重复这些结论，新增的是**当前 T 行地址组织及其实际 caller**。它不是 R522 的 binary128/dyadic 矩阵内核，也不自动改变另一条 native128 链。

## 523.3 精确来源

| 来源 | bytes | SHA-256 |
|---|---:|---|
| 原完整 core：`topics/visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs` | 17250 | `ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3` |
| [原 R466 flow](../computations/geometry_20261116_original64_contracted_finite_trace_flow.mjs) | 9412 | `c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7` |
| [R474 helper](../computations/geometry_20261116_finite_trace_zero_coefficient_linear.mjs) | 4832 | `eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02` |
| [R474 flow](../computations/geometry_20261116_original64_zero_eliding_finite_trace_flow.mjs) | 9510 | `1a5ce3f7b2af7016b2752af1654be68d1d708c3b4cc6660fbec33bb468f09ae1` |
| [R523 helper](../computations/geometry_20261116_finite_trace_actual_input_support_linear.mjs) | 6246 | `e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3` |
| [R523 flow](../computations/geometry_20261116_original64_input_support_finite_trace_flow.mjs) | 9504 | `14c691bec5ca228495027185ed642730d90d17ce65467ac76662c9407cd7d960` |
| [R471 variation](../computations/geometry_20261116_original64_zero_flux_contracted_finite_trace_variation.mjs) | 12597 | `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0` |
| [R471 零通量 helper](../computations/geometry_20261116_zero_nonlinear_split_flux.mjs) | 7111 | `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde` |
| [R466 原收缩 helper](../computations/geometry_20261116_recorded_factor_contracted_solve.mjs) | 11427 | `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` |

实际来源为 R467 的 25544 B / `c8709222176ffe7845a37fb1ad8f429d5c61af058f79c99c783edd72d6814597`，发表于 `2e85e46cf5771a4764d1ac15a25da806e3e1f36d`。原 core 和 R466 flow 从 actual208 固定 source `9b05bfc5160bf667cde0cb0ba059b0c8b0332bd5` 读取；R474 两源从 `9ff15fddedfa1be31f9e486b225c4a64c9f6e7fd` 读取。R470 正文为 19507 B / `6f0eae3da217eab6bde51794e15d3ed36ed116a81eddebe381ea0095b7d40475`。

所有这些旧源保持原字节。新的两个执行源没有运行记录，不能将 actual208 的计数归给 R523。

## 523.4 原乘积、当前输入与支撑

令 $R=K+2$。原乘积从完整正零数组开始，逐字正文为：

```javascript
for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
 const z=A[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
}
```

这里只读 $A$ 的全部 $RK$ 项、$T$ 的前 $K^2$ 项。T 的末两 mean 行不作为本乘法的输入；原 RK 组合仍会保留、更新它们。本结果没有把这些未用行加入新资格。

每次调用的假设是原相容维度、普通数值 typed arrays、调用中没有并发修改，以及原 JavaScript binary64 的乘法后加法语义。输出是新分配的数组，不与 A、T 或索引表别名。支撑不是容差集合，而是当前实际词定义的

$$
S_j=\{\,k:0\le k<K,\ T_{jk}\ne0\,\}.
\tag{523.1}
$$

正零和负零均不属于 $S_j$。任意非零次正常词都保留，即使稍后的实际乘积可能下溢。

helper 先扫描 A；只有其已检查全部有限时才按原行优先顺序扫描 T。扫描 T 的同时把每行的非零列按升序追加至 `columns`，用 `rowStarts` 标明闭开范围。索引使用普通 JavaScript number，没有窄整数强制转换；表中不缓存数值系数。

**引理 523.1。** 合格分支开始时，`columns[rowStarts[j]:rowStarts[j+1]]` 恰为 $S_j$ 的升序列表，所有被原乘法读取的 A、T 输入均有限。

**证明。** 每行从 $k=0$ 顺序扫描至 $K-1$，仅当当前实际值有限且不等于零时追加一次该 k。每行完整扫描后才写其末偏移。发现任一非有限项即令 reason 非空，离开扫描并进入原完整 fallback；未完成的索引表不会被合格分支使用。逐行归纳即得结论。证毕。

此扫描只选择实现分支。非有限输入不被拒收，也不会因索引表不完整而套用部分结果。

## 523.5 从每个输出槽证明语义保持

固定一个输出槽 $(i,k)$。原算法的递推为

$$
x_0=+0,\qquad
p_j=\operatorname{RN}(A_{ij}T_{jk}),\qquad
x_{j+1}=\operatorname{RN}(x_j+p_j).
\tag{523.2}
$$

这里明确是先形成 binary64 乘积，再相加；没有 FMA 或重新结合。新算法只省去满足 $A_{ij}=0$ 或 $T_{jk}=0$ 的项。每个保留项仍使用源码原表达式 `dt[i*Kdim+k]+=z*T[j*Kdim+k]`，且其 j 次序不变。不同 k 的输出槽独立，遍历当前行非零列不会把不同输出之间的数值相加。

### 523.5.1 有符号零、次正常数和有限累计

合格分支中两输入均有限。因此任一被省略项的原乘积是正零或负零；不存在被省略的 `0*Infinity` 或 `0*NaN`。

原正零累计器在保持有限期间不可能变为负零。确切理由与 [R473](R473-zero-coefficient-elision-in-complete-finite-trace-linear-products.md) 相同：任意两个有限 binary64 词都是最小次正常量 $2^{-1074}$ 的整数倍，其准确非零和的绝对值至少是 $2^{-1074}$，不会由加法舍入成负零。准确抵消在 RN 下为正零；累计器为正零时与负零相加仍为正零。因此对从正零出发的原递推，删除任一种零加项都不改变有限累计词。

这个结论没有删除非零输入形成的下溢乘积。若 $A_{ij}\ne0$ 且 $T_{jk}\ne0$，即使原乘积舍入为负零，该项仍实际执行。其前后的原累计词相同，后续递推也相同。它也没有假定 A 的交叉零、T 的交叉零或 mean 系数全是正零。

### 523.5.2 有限输入不保证有限中间量

保留的乘积可能溢出为无穷；两个有限累计项相加也可能溢出。相反符号无穷相加还可能形成 NaN。本实现没有把这些原路径隐藏为成功，也没有新增输出 finite 检查。

在原和新递推首次进入非有限的那个保留 j 之前，有限累计词相同；相同的原乘积和加法因此在相同 j 产生相同无穷符号或 NaN 分类。之后删除有限零加项不改变无穷符号或 NaN 分类，而所有其余项仍按原 j 次序执行。非有限累计不可能通过再加一个原乘积恢复为有限。

由此只得到非有限**分类**一致，不声明 NaN payload、NaN raw bits 或浮点状态标志相同。程序也不将 NaN 分类一致外推成 whole-run 的逐字行为相同。

### 523.5.3 完整局部定理

**定理 523.2。** 在第 523.4 节调用条件下，helper 正常返回时：

1. 若任何实际被用输入非有限，输出由原完整 $i,j,k$ 正文产生；
2. 若所有实际被用输入有限，所有最终有限输出词与原完整乘积相同；
3. 合格分支的非有限输出正无穷、负无穷、NaN 分类与原完整乘积相同，不声明 NaN 编码相同。

**证明。** 不合格分支保原输出分配和原三循环。合格分支由引理 523.1 恰省指定零项，逐输出使用第 523.5.1–2 节的递推论证即可。完整 $RK$ 输出数组始终存在，两个 mean 行没有例外，故各槽结论共同给出整个数组结论。证毕。

资格 true 不是阶段通过；`calls_completed` 也只表示 helper 正常 return。原消费者对非有限、完整误差、root、端点或其他门的处理继续生效。

## 523.6 实际实现如何保持顺序

合格分支保原 i/j 外层循环。对当前 z：

- `z===0` 时沿 R474 省掉原 K 项；
- 否则取当前 T 行已经完整形成的地址范围，按升序逐项读取实际 T 值，执行原乘后加；
- 不把同一列不同 j 的项聚合，不将当前 T 的零地址复用到下一次调用，也不把小值按阈值删去。

完全空的当前 T 行仍由实际扫描确定，其非零 A 项不产生乘积；原该段全是有限有符号零。完全稠密的 T 行则保留全部 K 项。特殊形状不是必要条件。

原 fallback 仍为第 523.4 节展示的完整正文。扫描只读原输入，没有改变其非有限词；fallback 不使用部分支撑，不捕获错误后重新执行，不重开预算。

## 523.7 新 flow 的真实接点及未变正文

新工厂是 `createOriginal64InputSupportFiniteTraceVariationalEngine`；新 helper schema 为 `original64-finite-input-row-support-linear-v1`。新 flow 独立导入 R523 helper，并继续直接导入原 R471 variation。

相对已刊 R474 flow，仅有七类明确文字替换：注释、helper 导入、工厂名、独立统计初始化、私有 linear 调用、两处 implementation 字符串及范围文字。原 `copiedOriginalRoot`、`rhsWithJacobian`、`field`、`fromCaptured`、`oneOriginalStep`、observer 与全部 cusp/普通分步正文保持原字节。

尤其是原四次 no-J root/RHS 和 nextState 都先真实完成；随后才在复制现场形成四个完整局部 A，再做 ta/tb/tc/td 及原 RK 合成。没有根据支撑删 field、删方向、删 stage、重排 RK 或改 `h*a/2`。完整 finiteRootDirection、R466 实际收缩/原 fallback、R471 实际资格和原 complete-local 统计继续执行。

新 flow 返回的 implementation / variationalEvaluation 为 `original64-noJ-primal-zero-flux-input-support-finite-root-variation-v1`。原 loader、worker、owner、必要 reader 尚未接这个新工厂；未来接线必须消费真实新源身份和新统计字段，不能仅把旧 flow 改名。本文没有修改正在运行的 211、215、222，亦没有创设新 workflow。

## 523.8 实际计数与中断的范围

统计挂在原 finite-trace statistics 的独立成员 `linear_input_support`。保原九类调用/扫描/零 A/完成段计数，并增加实际非零 T 地址数、实际零 T 词数、完整索引行数、非零 A 段内省略的零 T 乘积数和完整返回段的保留乘积数。

输入索引只记录已实际看到的词。某行在非有限项停下时，不增加其完整行计数。合格段内部不插逐 k observer；保留乘积数与该段省略数仅在整段返回后提交。因此中断时只报告真实当前 i/j、所选行支撑大小和“内部列未逐项记录”，不能伪造完成的 k 前缀。fallback 同样只报告原完整循环尚未返回，不猜内部地址。

`last_observation` 中的资格可以为 null：例如尚在输入扫描时停止。这个状态不同于已确认非有限而走 fallback 的 false，也不同于完整合格的 true。原异常和资源停止均向上传播；flow 原 noteFailure 仍记录并 rethrow。索引表分配失败也不被捕获后重试为另一算法。

本实现的工作量不同，资源停止时刻和原先已完成的范围可能不同。局部数值等价不承诺 whole-run 的时间、停止点或完整终态相同。

## 523.9 能减少哪部分工作

设 $a_j$ 是 A 第 j 列中实际非零系数个数，$s_j=|S_j|$。只比较乘加项数，则：

$$
P_{\rm original}=(K+2)K^2,\qquad
P_{\rm R474}=K\sum_j a_j,\qquad
P_{\rm R523}=\sum_j a_js_j.
\tag{523.3}
$$

R523 保留完整 A/T 有限扫描、完整 i/j 选择循环和完整输出分配；其总成本不是式 (523.3) 最右一项单独决定。支撑表占 $O(K+\sum_js_j)$ 地址，完全稠密时还会有地址管理开销。这里没有运行时间保证。

若某次真实 A/T 恰具 R470 所述块结构，并且其实际被用词有限，则每个形状列和 T 行的非零数受相应块大小限制；原两 mean 行若有实际非零系数仍完整计入 $a_j$。这解释零形状附近可能有大批无用乘积，却不让已发表实际 208 的聚合计数代替每次真实资格。一般混模或稠密 T 同样合法，只能取得实际支撑带来的省略。

本结果不声称已证明某个初始解无须求 J，不声称已取得全链提速，也不把统计计数当计时。相对于现有 R474，新增工作对象是实际 T 支撑；保留的所有非零算术责任未变。

## 523.10 已付与未付

已付为：实际源中的支撑构造不漏非零词、完整原 fallback、有限词及非有限分类条件等价、有符号零/下溢/溢出的边界、完整两 mean 和 RK 的源码保持，以及可直接接的新工厂与独立统计。

未付为：公开 Actions 的新执行、每次实际资格与完整字段、速度、完整尾 BVP/fullDN/FD/audit、一般有限轨迹与准确连续模型间误差、全局几何证书。本文没有本地 import、AST、compile、科学运算、测试、fixture 或 benchmark；只进行源码文字、来源字节和条件证明工作。原原料、精度、完整输入、原全部门、科学总钟和 quiet/readback/cleanup 合同由未来真正调用链继续保留。
