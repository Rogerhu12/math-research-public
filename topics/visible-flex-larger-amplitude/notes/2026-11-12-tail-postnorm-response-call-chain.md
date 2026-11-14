# 尾求解最终 norm 通过后的真实响应链

作者：tail_refinement，GPT-6 Astra Pro，AI-assisted。日期：2026-11-12。

本记录只读核对当前 pinned source、frozen/exactraw/stage 包装器。没有运行 Node、修改 MJS、改变验收或重算任何场。它解释日志的可定位范围；不证明 signal 9 的原因。

## 1. 实际顺序

当前 `strong_exact_stage_tail_worker.mjs` 展开 `strong_exact_raw_tail_worker.mjs`，后者展开 `tail_frozen_worker.mjs` 与 pinned `78718-prefix-tail-tangent-fourier-worker.mjs`。stage engine 只包住 `cellFlow`；resumable engine 插入共享稳定图入口及已接受试步的恢复回调。以下收敛后路径未被这些包装器更改。

1. `78718-tail-tangent-core.mjs` 第 138 行完成 `evaluate(states,target,true,scales)`，保存 `last=ev`，调用进度回调。worker 第 144 行先调用 `retainIteration`，再写 `iteration` trace。第 139 行在 `norm<tolerance` 时退出；第 164 行不会再评价全流。
2. core 第 165–176 行把 cut 动量乘原 `portRatio`，调用真实 `engine.toRaw`，复制已完成的 `last.flows[].J`、所有状态及 cut 数据，按原次序归约 `meanHeightToCut`，保存两端线性图和节点半径，返回 shooting 对象。split 第 25–29 行仅补充 `rhsEvaluation`。
3. core 第 206 行的对象字面量依次计算 `cutJets` 和完整 `audit`。**完整物理审计先于物理高度 Jacobian。** `cutJets` 的第 184–189 行调用真实 root、隐式 physical jets 和 RHS。
4. core 第 205 行完成所有数值 stage 的审计。每个 stage 新建零的 $K+2$ 向量，把 `sol.states[n+1]` 放入前 $K$ 项；逐 profile、逐 $k=0,\ldots,\mathrm{auditSteps}$ 调用 geometry、physical jet evaluator、actual metric、全部归约，再在 $k<\mathrm{auditSteps}$ 时调用原 RK4。该路径不经过 `cellFlow` 持久化缓存。
5. 审计返回后才调用 core 第 199–202 行 `heightJetJacobian`。第 195–197 行使用已完成的全部 $J_n$ 反向 Riccati 传播；每列按原 $10^{-4}$ 步长构造 plus/minus，并依次调用两次 `cutJets`。M24 共 48 次切口 jets 调用，所得矩阵大小为 $(3M+2)\times M$。
6. `tail_frozen_worker.mjs` 第 47–59 行调用 `actualSlopeJacobian`。其模块第 11–62 行使用真实切口 `rhsWithJacobian` 与同一个 solution 的已缓存切口图，覆盖一阶斜率及均值一阶斜率行；二阶行仍是原对称差。
7. pinned worker 第 145–150 行构造独立的 full shooting tangent predictor。这是 predictor 模块第 47–70 行的另一次反向 Riccati/transport 构造，不能凭名称用前一个求逆算法的产物替换。完成或捕获失败后才写 `tangent_predictor_ready/unavailable`。
8. worker 第 152 行写 `response` trace；第 155 行组装 manual checkpoint；第 156 行 `JSON.stringify` 并写 stdout。Python client 等整行返回后才保存正式 gzip response packet。

因此，只有最终 `iteration norm<tolerance` 而没有 predictor/response trace，最多把中断限制在上述第 2–7 步。现有 trace 不能进一步判定是审计、切口 Jacobian、predictor、内存还是其他运行环境因素。尤其不能从 576 次 stage cache 全命中推断后续完整审计已经完成。

## 2. 已完成量的恢复边界

当前 iteration checkpoint 已保存完整 H、所有 states、rawNode/rawStates，但仍正确标为 recovery-only；没有保留完整 $J_n$、far graph 和累计均值高度。

在 shooting 返回后可另存明确的 `shooting-passed / audit-pending` 包，原样保全 states/H、residual、minA/minD、history、cutRaw/cutMeanPhysical、meanHeightToCut、linearGraphAtCut/Deep、nodeRadius、parameters。$J_n$ 可使用现有 stage cache 的有序完整键与输入身份，或逐 stage Float64 数据；无需另造巨大 JSON。M24 的 576 个 $48\times48$ 原始双精度矩阵共 10,616,832 字节。所有可恢复字节应保留负零并绑定完整参数、实际 backend、完整 source 和 H/state 身份。

core 第 170 行在审计前把已有 typed $J_n$ 转为普通数组；构造期间与原 `last.flows` 可同时存活。这是一个明确可测量的分配位置，**不是已证明的中断原因**。

## 3. 原审计的同序分段

最小自然恢复单元是一个完整数值 stage。每个 stage 结束后保存原八个累计量

`fullD, normalizedFullDefect, minLeading, minD, formalCurvature, maxPhysicalPV, actualMetric, holonomy`

以及下一 stage 索引和完整身份，下一次继续原正序。stage 入口仍须使用原 `zeros(K+2); set(states[n+1])`，不能沿用上一 stage 的均值状态，也不能把缓存的 shooting `out` 冒充审计内部 RK 轨道。

更细的 profile/k 恢复需保全完整 $K+2$ 状态、精确下一 profile/k、全部累计量、同一 cusp 网格和 profile 输入。每点的完整角向 jet、metric、Darboux、holonomy 及 positivity 调用都保留，原乘除次序和 min/max 顺序不变。重开进程后的源、参数、auditSteps、state、网格与算法身份必须逐项核实；首次实现还须比较实际同一审计的完整结果，而不能以本静态拆分直接宣称逐位等价已验证。

Jacobian 可另以反向 Riccati 断点、每列 plus/minus 完成结果和最终解析行覆盖为恢复单元。最后仍完成原 predictor 构造及原响应 schema；只有全部审计与原门完成后才能发出正式响应。任何这种新包装器都应具有明确的新 source 身份，不能把 `audit:false` 的 shooting 包替代最终审计。

本记录是恢复接口分析，不是新数值证书，也不影响已经冻结或正在运行的 MJS。
