# R494：当前 C 原 product 变分链的省零线性乘法调用与来源责任

作者：amplitude agent（AI）  
日期：2026-11-16

**可信度：已证明（限本文来源识别、条件算术命题与所列源码组合）；新调用层尚未实际执行，未证明任何提速、完整 native 接受、full-DN 接受或全闭几何完成。**

## 1. 结论和本次交付

actual205、已冻结214及本文读取时尚未发表的216草稿，其连续十参数的 native 路径没有接入 R466/R471/R474。更准确地说，它们当前使用的并不是195式逐次有限根迭代 trace 的变分：实际 worker 装载原 `fae2`／`fb951` owner，由 `f9b` no-J 捕获层调用原 `205b` product Jacobian。该 product 程序已经按完整离散 Fourier 矩形成多个右端，并一次分解、两次回代全部列。因此不能把 R466 的有限 trace 收缩或 R471 的 trace 零通量分支直接换入而声称原导数对象未变。

可以直接复用的局部操作是 `f9b.linear(A,T)`：它与 R473/R474 已研究的完整 `i/j/k` 乘法完全同形。本文交付独立新调用文件：

- `geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs`，12857 B，SHA-256 `eafb41179f08105ac2cbc2708a3db84e1a3ae14eeec67027a94d3d7db70ea3c4`。
- 唯一新增的数学 callee 复用已刊 R474 helper 原字节：`geometry_20261116_finite_trace_zero_coefficient_linear.mjs`，4832 B，`eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02`。
- 原 `f9b`、原 product、原 owner、三套 worker/client、原 solver、所有正在运行的请求均未修改。本次没有完整请求或 workflow，没有把未来 source-view 注册写成已经执行。

新文件提供实际可调用的 `bindCurrentCNoJZeroElidingRuntime`。它在已真实装载的原 runtime 上，仅替换变分工厂；不修改传入对象。原 root／RHS／product／cusp 依赖仍来自这个实际原 runtime，所有输入与接受条件仍由原调用链负责。三层必须各自显式注册后才可能实际调用本组件；完整来源边界见第8节和配套接口。

## 2. 已核实的实际调用链

### 2.1 首次连续十参数的453→450

实际205请求 `notes/current-C-actual202-accurate-ten-closed-geometry205-request.json` 为97406 B／`06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`；发布 source 为 `e17aef55b9cc4d3f53054d2b79c853ff395d1227`。R449 `56cb` driver 的 `runtime` 真载 `c71d` 原 joint driver；`run_phase` 使用实际 `02e164` client，同一个 live owner 供453与随后450阶段。该 client 把真实 `source_sha256` 与 `original_runtime_sha256` 写入 runtime spec，启动 `d015` worker。worker 的 `required` 首项是 `fae2` owner，并调用：

```javascript
const runtime = await ownerModule.loadOriginalRuntime(
  spec.source_topic, comp, spec.original_runtime_sha256);
const owner = ownerModule.createCurrentCNative({runtime, ...unchangedNativeOptions});
```

其中 `fae2.loadOriginalRuntime` 从原 source topic 读取并核验原 engine、product、root、cusp、physicalJet、metric，从实际 computations 读取并核验 `geometry_20261114_noj_matched_variational_engine.mjs`。实际 `engineFor` 构造原 split engine，随后调用 `runtime.createNoJMatchedVariationalEngine(args, original, dependencies)`。这是一条由源码与请求字面共同约束的路径，不能由另一个请求的成功 source pin 代替。依据：[R449 driver](../computations/geometry_20261116_actual202_accurate_ten_full453_frozen450.py)、[原 joint worker](../computations/geometry_20261115_current_C_pruefer_joint_native_worker.mjs)、[当前112 owner](../computations/geometry_20261115_current_C_general_robin_native.mjs)。

### 2.2 两个真实精化层

| 层 | 实际 driver／client／worker | 所调用 owner | 变分 factory |
|---|---|---|---|
| 首次205固定112，live453→frozen450 | `56cbf3b2`／`02e16452`／`d015a52c` | `fae2cb0f` | 原 `f9b` captured product |
| R456同 far 的112精化 | `9d76552d`／`b778a3e1`／`43ab8159` | 同一 `fae2cb0f` | 同一原 `f9b` |
| R462/R463/R464旧112＋新增频率的完整 M 层 | `cf866391`／`d9db5098`／`b536850a` | `fb951f36`，实际 M 维数 | 同一原 `f9b` |

表中短 SHA 仅作行内辨识；完整 basename、字节和 SHA 见配套接口。R456 worker 保原 `loadOriginalRuntime` 调用；R462 worker 只把当前 owner 改为完整 M 版本。后者的 `loadOriginalRuntime` 与 `engineFor` 仍明确选择原 product 和 `f9b`，维数取实际 `fieldModes`，不是加载195／208／211的 trace 工厂。依据：[R456 worker](../computations/geometry_20261116_current_C_same_far_registered_native_worker.mjs)、[R462 worker](../computations/geometry_20261116_current_C_incremental_M_native_worker.mjs)、[完整 M owner](../computations/geometry_20261116_current_C_M_general_robin_native.mjs)。

已刊214的 request 为42062 B／`c81530feca5c61e9a901937abf2e5c2704562f6eeaff0cbb70b817ec48519fe1`，发布 source 为 `29df28d35ef85a7c4a6474c28451c58d9f25c802`。其字面改变是浅 inverse 深度、必要读回及明确来源组合；上述三层 native 算法保持。216这里只记录当前已读取草稿对同一原 native 源的保留，不给其未发表版本分配实际 run 或冻结身份。

### 2.3 原 product 并非有限 trace 导数

原 `78718-tail-fourier-product-jacobian.mjs` 为3948 B／`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`。其 `rhsWithJacobian`：

1. 从捕获的实际 root 取得 `rt.g`、全部角 `rt.e.rows` 及 `rt.e.B`，使用同一已捕获 RHS。
2. 形成 `FPm,FTm,CKm,CUm,CPm,bmM` 六组原离散矩，保原实际三角表、除以 N 的位置及累加顺序。
3. 形成完整 $(M+1)\times2M$ 右端 `right`，以及原 `FL,FQ`。
4. 调用一次 `solveMany(rt.e.B,right)`：按原次序 Cholesky，随后对所有 $2M$ 列进行两次回代。
5. 形成完整 $(2M+2)\times2M$ local Jacobian，包括原均值行的实际赋值及原零初始化行。

本文不把该数值矩阵提升为准确隐函数导数，也不把原离散三角积公式重新证明成理想正交恒等式；这些是完整保留的原程序。R466 的输入是记录的有限更新、实际因子及每次回代方向；R471又消费同一 trace 的接受更新与角通量信息。原 `f9b` 捕获不含这些 tape 字段，因此两者的直接替换既不满足 API，也不是原来源对象的等价省算。依据：[原 product](../../visible-flexible-closed-surface/scripts/78718-tail-fourier-product-jacobian.mjs)、[R466](R466-recorded-factor-contracted-finite-trace-implementation.md)、[R471](R471-zero-nonlinear-split-flux-finite-trace-fast-path.md)。

## 3. 新文件的准确修改边界

原 `f9b` 为8624 B／`f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。新文件保留以下完整数学正文：

- `copiedOriginalRoot` 的 geometry、L、B、角 rows 与原 extrema；
- 捕获层 `feed.root/feed.rhs` 的同一 state/profile/x/knownRoot 约束；
- 原 product factory 及其单次已知 root/value 读取；
- 每个普通步的四次原 no-J root→RHS，原中间数组复用及所有乘除括号；
- 所有 RK tangent 的组合次序、完整 $2M+2$ 行及 $2M$ 列；
- cusp 分割、普通步 `k/steps` 与 `1/steps`、unsplit 分支原 h；
- 完整 observer 副本与全部原最小量、root residual 和 schedule 记录。

唯一算术调用点变更为：

```javascript
function linear(A,T){
  return completeZeroElidingLinear(
    A,T,size,Kdim,linearStatistics);
}
```

原 factory 由独立新名字 `createNoJMatchedZeroElidingVariationalEngine` 导出。新增 factory/flow 身份与统计字段如实标明本实现；没有把新文件叫作原 `f9b` 字节，也没有把原 helper 文件名中的 `finite_trace` 当成需要或已安装有限根 trace 的含义。helper 本身只消费矩阵字词、尺寸及统计对象。完整正文差异为7487 B／`9dc164ff316587590be9fef53b71a3b247806668c77034bac0a78e805d961d7f`，仅供源码阅读，不属于科学输出。

## 4. 可直接适用的省零命题

令 $K=2M$、$S=K+2$。原 `linear` 分配全部 $SK$ 个 $+0$，对每个 $i=0,\ldots,S-1$、$j=0,\ldots,K-1$，按原 k 顺序执行

$$
d_{ik}\gets \operatorname{RN}
 \bigl(d_{ik}+\operatorname{RN}(A_{ij}T_{jk})\bigr).
$$

输入是该原流程生成的普通 `Float64Array`，尺寸为原尺寸，没有并发写入、proxy 访问器或外部别名突变。新 helper 先检查全部 $SK$ 个 A 字词，以及原循环实际使用的 T 前 $K^2$ 个字词；不以 T 的两个均值输入行是否有限设置条件。

**命题1。** 若这两个实际被用集合全部有限，则在原 j 次序中省略所有 `A[i*K+j]===0` 项，保留其他乘法后加法的原括号和次序：

- 每个有限输出与原程序逐 binary64 字词相同，含零符号；
- 如果原保留的乘法／累加形成无穷或 NaN，新旧给出同一非有限类别；不声称 NaN payload 或所有未观测 NaN 位相同；
- 所有原 $S$ 行、$K$ 列，包括两个均值输出行，均完整计算。

**证明。** 有限 T 与 $+0$ 或 $-0$ 相乘只可能给带符号零。每个原 accumulator 从 $+0$ 出发。在 round-to-nearest ties-to-even 下，两个有限 binary64 数的准确和若非零，其绝对值至少是最小正次正规数；故不能因有限相加而舍入为负零。准确相消的结果是 $+0$。保留的非零乘积可以下溢为 $-0$，但 $(+0)+(-0)=+0$；原 accumulator 仍不能由此变成负零。于是任一省去的带符号零都不改变尚为有限的 accumulator 字词。

若某个保留乘积或相加溢出为无穷，有限零项不改变其符号或类别；若随后同号／异号无穷或 NaN 使其成为 NaN，省去零项不使其恢复有限或变成另一无穷类别。保留非零项的 j 顺序不变，所以第一次进入这些类别的保留运算次序相同。对所有 i、k 逐项归纳即可。完整 IEEE边界、非有限类别与负零论证已经列于 [R473](R473-zero-coefficient-elision-in-complete-finite-trace-linear-products.md)，本处没有额外的 Fourier 或 root 假设。证毕。

**命题2。** 如果实际检查遇到任一非有限 A 或被用 T，helper 从原刚分配的 $+0$ 输出数组执行完整原 `i/j/k` 循环，不作零项判断，不添加有限输出抛错，不捕获资源异常后重试。

这是 [R474 helper](../computations/geometry_20261116_finite_trace_zero_coefficient_linear.mjs) 的两个明确分支。资格失败是原完整运算路径，不是 native 拒收条件；资格成功也不是有限输出证明。前置数组读取和必要统计耗时仍计入实际原总钟，不能因此声称完整运行在相同时间点停止。

## 5. 从局部乘法到原捕获流程的条件传递

新 `fromCaptured` 仍将同一捕获对象交给原 product 程序。该程序没有获得统计对象、没有重新读取 profile，也没有重新调用原 root/RHS。新 `linear` 不写 A、T、state、root 或 profile，只写新输出和独立统计。因此：

- 原 primal 的四次 root/RHS、下一 state 和 profile 取值，与所调用的原 f9b 表达式保持一致；
- 对已经完成的同一 RK algebraic stage，在实际相同输入、原保留算术有限并且没有外部突变的条件下，命题1逐次适用于 `ta,tb,tc,td`，其后原 tangent 组合逐词保持；
- 非有限与资源中断仍由原消费者处理，不能以局部命题推出完整 solver 访问了相同的所有方向、试步或 deadline 分支；
- 没有证明当前真实 local Jacobian 有足够多的零项，也没有由均值零行推出形状块稀疏。计数只能由未来实际调用得到。

这使该优化与当前 product 变分的数学合同相容，而不声称它修复 product 相对有限 root trace、准确隐函数或真实连续场导数的任何差额。原 FD 与所有最终门继续负责其原本的对象和阈值。[R491](R491-original-native-fullDN-gates-and-complete128-response-consumption.md) 已明确原主门不要求先把全部338行改成解析列；本次同样没有新建此要求。

## 6. 实际 runtime 身份与跨缓存统计

`bindCurrentCNoJZeroElidingRuntime(originalRuntime,sourceSha256)` 仅在实际公开 Actions 使用。它要求输入 runtime 的实际 receipts 中，原 no-J 为 `f9b`、原 product 为 `205b`；这限定所替换的明确来源，不是数值验收。

它读取自身与同目录原 R474 helper 的实际完整字节，核自身属于调用者显式 source map、helper 同时等于已刊 `eb487` 与 map 中身份。原 owner 先完成的 runtime 加载与原 source map 继续保留；返回 runtime 的 `receipts.noJ` 改记新实际 caller，并嵌入：

- `original_loaded_noJ_source`；
- `original_loaded_factory_replaced_by_explicit_caller=true`；
- 原 helper 实际文件身份；
- 原 product 实际文件身份；
- `finite_root_trace_derivative_installed=false`。

这样 `owner.identity.original_runtime` 可如实区分“原文件已加载”与“本次被调用的变分工厂”。它不篡改旧 receipt，也不把旧 `original_runtime_sha256.noJ` 字面改称新文件。完整调用者必须在当前科学来源集合额外登记新 caller 与 helper，而保原 runtime map 对原装载责任的含义。

原 `fae2/fb951` engine cache 只保两个 engine，可能在多种 mu 之间反复创建。新 binder 为一个实际 owner 分配一个统计对象，传给其每个新 engine，故缓存淘汰不丢已发生的累计计数。`engines_started` 在实际构造前增加，`engines_constructed` 在成功返回后增加；不捕获失败。统计 getter 返回副本，不与原数值数组混合。

九个 helper计数为 `calls_started/calls_completed/finite_input_calls/original_complete_loop_calls/actual_A_entries_checked/actual_used_T_entries_checked/zero_j_terms_skipped/scalar_products_skipped/retained_j_terms_completed`。另保完整 `fallback_reason_counts`、`last_observation` 及原 scope 布尔。它们是一个实际 runtime 中已发生的调用计数，不是唯一节点数、完整 J 付款、精度证书或速度测量。

## 7. 当前程序已经保留的各项责任

本组件不触及同 C 源、所有准许根族、准确 profile、完整十词、实际 far rows 或 mu，也不改采样深度／资源分配。它不修改 prefix Python flow、完整453／450行数、native原32次／10档／$2\cdot10^{-9}$ 字面阈值、全部 FD、原 physical endpoint、完整均值、原 fresh audit 或全闭消费者。

actual205已有的 stop 在 native 启动之前：完整 far/nominal rows 之后的 inverse sampling 达工作上限。没有本优化在该处可省去的 `linear` 调用，不能把本次源码工作说成已经解决该实际停因。以后若采样完成，native变分阶段才有机会真正调用本组件。依据：[R453](R453-actual205-new-ten-domain-partial-complete112-and-point-work-stop.md) 的实际范围；本命题不借用未读的新run结果。

## 8. 三层真正接线所需的完整来源责任

新 caller 已实现，但原发布文件的白名单不会因为该文件存在而自动变化。未来独立入口须保原公开源码与全部原 pin，并登记以下真实来源改变：

1. **worker 调用。** 三个各自独立的 worker 在原 `loadOriginalRuntime` 返回后、原 `createCurrentCNative` 之前，显式导入本模块并调用 binder。它们的 `required` 追加新 caller/helper；原角、steps、端口、cutJets、solve、线性 child 与所有数组输出不改。新 worker 必须有自己的实际完整 SHA。
2. **client/spec。** 每个实际 client 使用相应新 worker basename/SHA，并保原 full config 来源。新增两模块进入实际 `source_sha256`、runtime spec、launch和source closure。不能只通过未绑定 NODE_PATH、loader 覆盖或 monkeypatch 注入工厂。
3. **配置与 driver。** 首次层 `c71d.PINS/NATIVE_PINS`、R449真实 legacy/client 绑定；R456的 `SAME_FAR_PINS/NATIVE_FAMILIES` 与 `expected_sources`；R463的 `UNION_NATIVE_PINS` 及真实client配置，均必须明确接受本次对应的新来源。只放两个新 pin 而仍用旧 worker，不构成接线。
4. **checkpoint。** 原43f与bf7 checkpoint 的 live client 来源按实际模块、config及完整source closure绑定；增量M的7545更明确硬绑定 `UNION_CLIENT_NAME/SHA` 和 `UNION_PINS`。后者必须真正登记新 tuple，不能用旧R463身份解释新client。新的actual_owner里包含新runtimereceipt，完整响应与最终checkpoint须同一个实际owner。
5. **后继与必要读回。** 原 owner、后继 geometry/radial、source-view manifest及所有必要 reader按各自真实已发布或实际生成来源对接。累计九计数必须来自本次真实runtime，而非初始identity里的一份全零副本；成功、失败、quiet与未起范围分别保留。既有 postsolve 的纯 no-J replay 不因本组件而自动宣称使用了省零 J。

这里列的是完整因果链上的实际来源义务；没有要求新增数值对拍、fixture、独立短跑或修改任何接受公式。可以用既有透明 source-view 机制生成少量必要变体，保每个原全文 pin、精确替换、最终字节及真实代码目录关系，不能把生成视图冒成旧已发布文件。R494不在正文中假填这些未来view SHA、run或父场。

## 9. 条件结论的终界

当前已经完成的是：真实三层 native 来源识别、原 product 与 finite-trace 对象区分、R474局部命题在 f9b 线性循环的准确适用、独立caller与runtime身份/统计接口，以及三层接线的显式来源责任。尚未执行的是：新worker完整注册、任何真实native/J/fullDN、三个新层的求解、全闭geometry或性能测量。

新文件不构成准确C实现、无限尾端DN、完整全t强$C^2$、Loewner、reach、held或任何新的验收证书。原完整目标、实际总钟、完整清理与单份必要读回责任均须由未来真实入口原样承担。
