# 固定度量的共同帽高 Gate 与最小约束目标接口

状态：**独立新接口与人工检查入口；未运行真实候选求解，人工检查尚待公开 Actions 回执**。本文件补充 [联合高度约束设计](fixed-metric-linear-cap-height-constrained-solve-design-20261114.md)，不改变当前 short-entry 实际审计、任何已冻结几何源码或其目标。

新源码为 `scripts/frame_height_affine_gate.py`。当前源码 35533 字节，SHA256 为 `c55fe53cc8f5ebaae10480cf759dc5e228316e80bfab13bef3d01d5c51e37e0c`。它只公开 `--check-only` 命令行；实际研究用的模型、初态、网格、数值规则、盒和预算必须由以后独立且可审计的 Actions driver 明确选择。

## 1. 数学门与两种身份

在已经冻结完整径向度量、原始 $c_0$ 高度参考和高度基的模型中，

$$
X(t,\theta)=a(t)\Pi T(t,\theta)
+\left[z_0+B_0(t)+\sum_j c_j I_j(t)\right]e_z,
\qquad
I_j(t)=\int_0^t C_j(s)\,ds.
$$

设侧号为 $\sigma\in\{-1,1\}$，则完整开放尾的共同帽高为

$$
h=h_{\rm base}+\lambda\cdot c,\qquad
h_{\rm base}=\sigma[z_0+B_0(L)],\qquad
\lambda_j=\sigma I_j(L).
$$

当前 $u,v$ 系数完全不进入此门。Gate 的物理身份绑定：

- 完整冻结 $g$ 的数学定义；
- 不可变 $b_0$ 参考、固定高度基及端点原函数定义；
- 核心、准确帽、侧号、准确 $L$ 和参数布局；
- 所选 $\tau$、高度余量、R66 的准确高度差分支。

**正在优化的 $u,v,c$ 系数不属于 Gate 的不变量。** 初态物理状态 SHA 单独放进 provenance；未来实际 driver 还须单独记录全部原始输入文件 SHA、完整 canonical 初态和源码清单，不能将这些会随当前候选变化的状态 SHA 用作 Gate 相等性的要求。

第二个身份只记录本轮冻结的数值行：评估的 $h_{\rm base}$、$\lambda_j$、目标高度和完整共同原函数评价规则。每个 binary64 数用其准确有理数形式记录。因此变更固定求积、Nb 或 GH 档数可以保持相同物理 Gate，同时必然产生另一个数值 Gate；禁止在同一次最小化中暗换后者。

对于当前 $B=7/25,w=1/50,R=137/500,\tau=61/1000$，R66 给选定上支

$$
h\ge \frac{81+\sqrt{3685}}{1000}.
$$

若使用余量 $m_h\ge0$，目标是再加 $m_h$。接口也保留 R66 的其它 $|B-R|$ 分支，并明确“选上支”是设计要求。**R66 的必要性以完整嵌入的 reach 至少为所选 $\tau$ 为前提**；不能仅凭题目 $\operatorname{reach}/D\ge .03$ 和 $D\ge2$ 就把 $.061$ 宣称为无条件必要值。

## 2. 接口

### 2.1 `HeightAffineGate`

`from_frozen_problem(problem,state,data,tau=...,height_margin=...)` 要求：

1. `metric_free == 0`；
2. 模型明确提供查询无关的共同高度原函数评价定义；
3. 完整位置 chart 从 $0$ 到同一 $L$，包含真实的 `center(L)`；
4. 当前完整系数有限且维度匹配。

本轮截距由一次完整共同高度减去当前高度列贡献取得，记录它的数值来源；之后它在该次求解内固定。高度行只有高度列非零。返回真正的 SciPy `LinearConstraint`，而不是在残差中软罚这条门。

`assert_context(problem,state)` 在**每次评价以及缓存命中之前**重新核固定模型家族和评价规则。它允许当前系数变化，却拒绝冻结 $g$、$b_0$、高度基、核心、侧号、布局或评价规则改变。

`decision(...)` 分别记录：

- 相对原始系数盒的最大越界；
- 冻结数值行的高度余量；
- 本次完整几何通过原共同原函数重构的帽高余量；
- 两个帽高的差；
- 所有显式的浮点容差。

候选只有同时通过这几项才进入“本次数值门下可用”的集合。这一标签不代表准确等距、嵌入、reach 或连续积分的认证。

### 2.2 `FixedGateObjective`

目标使用已有模型的 `direct_residual_and_jacobian`，没有换成辅助 $R$：

$$
J(x)=\tfrac12 r(x)^T r(x),\qquad
\nabla J(x)=J_r(x)^T r(x).
$$

因此直接度量、当前完整 ball/strip 平滑目标和全部解析参数导数保持由被冻结模型解释。本接口不改变 strip 宽度、权重或高度目标以制造成本下降。

本次目标另有独立 evaluation identity：完整径向/角向网格的准确 binary64 有理数、geometry 求积阶数、切向场空间、ball/strip 参数、权重与归一化、全部实现源码 SHA。它不混入物理高度 Gate。网格与盒在构造时复制并设为只读，目标空间或权重变更在缓存命中前也会被拒绝。

一次完整调用缓存成本、梯度和小回执，不保留大残差 Jacobian 或全部位置 Jacobian。分别保存：

- 所有已完成试探中成本最低的一点，可能不满足高度门；
- 同时满足盒、行和真实共同帽高检查的最低成本一点。

checkpoint 包含准确 binary64 系数、全部小历史、门身份、数值容差和原盒。默认每 10 次完整评价或距上次 checkpoint 60 秒保存；一次不可中断的函数评价完成后立即再检查墙钟预算。外部 driver 负责原子写入完整报告，并保留门定义、源码和输入来源。

### 2.3 `run_slsqp`

仅调用一次 `minimize(method="SLSQP")`，使用解析目标梯度、原始 `Bounds` 和真实 `LinearConstraint`。**不传 `keep_feasible`，也不声称 SLSQP 的所有试探或迭代都保持可行。**

先完整评价初态。若它未通过盒、线性行或共同帽高重构检查，则保存原因并以零次优化器调用返回。否则只进行一次有界约束最小化：

- 有独立的最大完整函数评价数和墙钟预算；
- 预算到达时保存已完成且通过门的最好点；
- geometry、非有限检查或优化器抛出异常时，以明确失败状态和异常类型/消息返回，并最终保存已完成的最好可用点；保存不代表该次调用成功，后续须按原身份重放；
- 库返回 `success=True` 也必须重新经过相同候选检查；
- 不将成本更低却越过帽高门的试探替换为选中点；
- 不在返回后偷偷投影、修高度、换 GH/Nb 或启动第二次求解。

真实研究 library 调用要求准确的 `GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。显式人工绕过只接受源码内声明的三变量数组 family；人工几何的 Gate/差分检查不调用优化器。命令行没有真实报告输入或真实研究优化选项。

## 3. 开发检查及待取得的证据

本版只准备以下人工检查，**没有在本会话环境里执行，不写 passed**：

1. 三变量已知严格凸二次目标：一个普通变量和两个高度变量；盒内最优点能解析算为 $(1,.38,.04)$，帽高等号为 $.2$。调用同一最小 SLSQP wrapper，与解析点比较。
2. 随后输入成本更小却帽高失败的试探，检查它不会替换已选可用点。
3. 故意向人工共同高度加入错误常数；线性行即使通过也必须因独立重构差而拒绝。
4. 改固定参考后查询同一缓存状态，检查 context guard 仍生效。
5. 失败初态零次启动、单评价预算保留初态 checkpoint；人工注入第二次评价异常，核明确失败状态、一次优化器调用及最终可用点保存。另核改变目标定义后连同状态缓存也拒绝。
6. 使用既有严格人工 `artificial_carrier`，分别构造 paired 和 bounded 两模型。对共同帽高行做全系数方向差分，核 $u,v$ 行为零；当前系数变化保持同一物理 Gate，初态 provenance 则单独变化；数值行与完整共同高度重构相符。

人工几何只用于公式/API/Jacobian 检查，不优化真实核心，也不读取正在审计的实际 selected 结果。开发输出完整记录 Python/NumPy/SciPy 实际版本与当前源码 SHA。公开 Actions 可使用：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_height_affine_gate.py \
  --check-only \
  --out topics/visible-flex-new-mechanism/notes/height-affine-gate-development.json
```

该命令的实际回执到达前，静态审核与已写测试不能替代运行成功。

## 4. 以后真实 driver 必须补足的内容

short paired/bounded实际43627111925现已完成，两次B7提案均为空、零步；详短入口实际审计。新接口尚未用于真实联合求解；先做九列高度多面体可行stage，不能把当前高度失败初态直接当作已可行的SLSQP入口。

收到实际数据后，如选择一个已有数值高度可行的场，新的独立 driver 至少须：

1. 通过原严格 loader 和 raw SHA 取得初态，记录原场、已应用的一步、全部系数和新模型身份；不替换不可变原 $c_0$。
2. 明确这次实际采用的固定 $g$、形状目标、固定数值规则、网格、系数盒、$\tau$、余量、求解预算和容差。
3. 在整个求解中冻结同一个 Gate 家族与数值行，保留所有被拒试探的门摘要。
4. 最终选中态使用原共同原函数完整重构，并保存完整 canonical 状态，不只记录优化器的 `x` 和 `success`。
5. 固定该完整状态，分别精化 GH、Nb、共同原函数 partition/阶数、角向 $\Pi$；不在精化档重新优化。数值行精化后如高度余量变号，必须如实报告，不以旧行“已可行”覆盖。
6. 继续审计真实 $E,F,G$、全位置二 jet、浸入、曲率、ball/strip、有符号高度与镜合相邻片。帽高门只是其中一个全局必要或设计约束，不能替代这些条件。

该 wrapper 的 checkpoint 自带准确系数以防中途失去可审状态；完整科学结论仍须由独立实际 driver 的来源、同态精化和几何审计给出。

## 5. 参考与接口范围

- [共同帽高约束纸稿](fixed-metric-linear-cap-height-constrained-solve-design-20261114.md)。
- [R66：两个法向的高度必要门](../results/R66-core-flat-cap-two-normal-reach-height-gate.md)。
- SciPy 官方 [SLSQP](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)、[LinearConstraint](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.LinearConstraint.html)、[trust-constr](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-trustconstr.html)、[least_squares](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)。

官方接口核对支持本版传入真实约束和不使用 SLSQP `keep_feasible` 的决定；它不提供本研究的几何或收敛结论。具体版本由开发及后续实际回执记录。

## 6. 首次开发请求

2026-11-14 18:54 UTC部署独立 `height_gate_development`，只运行本文件所列人工数组及人工几何检查。此前已完成的真实short与P1 runs不重跑。实际运行结果尚待回执，不把脚本已发布记作passed。

## 7. 公开人工实际结果

run43629262349/source d78ca152已success。人工三变量QP解误差2.22e−16；两个人工几何的帽高行差分相对误差1.75e−10、独立共同高度与仿射行差0。坏初态不启动、预算保留、第二trial异常保存失败状态与最佳可用点、缓存家族及目标变更拒绝均通过。原输出为 `notes/actions-43629262349-1-height_gate_development/height-affine-gate-development.json`。只证明本人工开发检查成功，无真实几何优化。
