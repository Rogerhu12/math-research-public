# R186 域与真实 Armijo 缩步：端点建议约束不等于试步已消岛

**状态：代数结论已证明，b075 常数的纯 BigInt 有理消费已实际执行。**
本文不改变任何 Context、normal、Schur、QP 或 Armijo 接受规则，也不声称产生了新方向或新实际 trial。

使用 [R186](../results/R186-delta7-only-removal-of-the-late-positive-K-island.md) 及其
[自由前六系数推论](2026-11-12-fd2d-metric-R186-free-first-six-corollary.md) 的准确常数

$$
m={\rm binary64}(0.027)
=\frac{7782220156096217}{288230376151711744},
\qquad
M={\rm binary64}(0.08)
=\frac{5764607523034235}{72057594037927936}.
$$

当前 b075 原点的第七系数为

$$
d_0=\frac{1836789295023669}{144115188075855872}<m.
$$

其实际原点身份仍为 b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f。下面任何默认常数报告只对应此原点；以后原点变化必须使用实际新 $d_0$。

## 1. 精确的进入步长

设一次 QP 建议的完整方向端点第七系数为 $d_1>d_0$。
理想准确仿射试步定义为

$$
d(\alpha)=d_0+\alpha(d_1-d_0),\qquad 0\le\alpha\le1.
$$

因为斜率为正，直接移项得到充要条件

$$
d(\alpha)\ge m
\quad\Longleftrightarrow\quad
\alpha\ge\alpha_{\rm enter}
=\frac{m-d_0}{d_1-d_0}.
\tag{1}
$$

若 $d_1<m$，单位区间内没有进入；若 $d_1=m$，只有完整步 $\alpha=1$ 达到下界。故 QP 端点满足 $d_1\ge m$ 并不保证任意缩步后仍满足 R186。

反过来，对任意指定 $\alpha>0$，

$$
d(\alpha)\ge m
\quad\Longleftrightarrow\quad
d_1\ge d_0+\frac{m-d_0}{\alpha}.
\tag{2}
$$

在原 QP 上限 $d_1\le M$ 内，存在能进入 R186 的端点的必要且充分条件是

$$
\alpha\ge
\frac{m-d_0}{M-d_0}
=
\frac{4108641566048879}{19384851502089602}
\quad\hbox{（显示约 }0.21195114987628283\hbox{）}.
\tag{3}
$$

式 (1)–(3) 只涉及一个准确参数，不引入新的曲面假设。

## 2. b075 的二分线搜索阈值

对通常的 $\alpha=1,1/2,1/4,1/8$，式 (2) 的准确端点要求为：

| 理想步长 | 端点第七系数的准确下界 | 十进制显示 | 在原 $M$ 以内可行 |
|---|---|---:|---|
| $1$ | $7782220156096217/288230376151711744$ | 0.027 | 是 |
| $1/2$ | $1486357715268137/36028797018963968$ | 0.04125471395799821 | 是 |
| $1/4$ | $10054072427121427/144115188075855872$ | 0.06976414187399463 | 是 |
| $1/8$ | $18271355559219185/144115188075855872$ | 0.12678299770598744 | 否 |

因此，从 b075 原点出发、且端点仍受原 0.08 上限约束时，理想的八分之一步及更小二分步不能进入 R186。这个结论不是对 Armijo 下降是否成立的预测；某个未进入 R186 的较小步仍可能是原问题域内合法的实际接受态，只是不能引用 R186 的消岛结论。

当已接受原点的 $d_0$ 改变时，重用表中数值会错。应按式 (1) 或 (2) 消费新的准确系数。独立小工具允许显式传入原点和端点。

## 3. 实际浮点 trial 的判定

求解器的向量加法、边界投影或其他明确重表达可能使最终保存的系数不逐字等于理想有理仿射式。消费者因此分开报告：

- ideal_alpha_enter / requested_ideal_step：只对应准确仿射模型；
- actual_trial_membership：只从显式提供的实际保存 binary64 系数判断 $m\le d_{\rm actual}\le M$。

第二项不会用第一项的预测替代。actual_trial 未提供时，工具明确返回 null，不生成“已经进入”的结果。

完整 R186 设计域成员性还要求前六系数位于原准确盒、保留 middle-only 的准确行、正确 base/support 绑定及主线选择的其他原域条件。这里的 actual_trial_membership 只检第七系数并明确标出未检其他条件。真实候选的 tail 证书同样要按其当前控制系数重算。

若 QP 原点和端点都属于原 middle 准确线性域与盒，则准确仿射段留在该凸域内；实际浮点接受态仍按 Context 原有准确检查处理。本文不授权把原 ctx.check_domain 的第七系数下界突然改为 $m$，因为当前 b075 原点尚不属于该新域。切换成 R186 域应另有明确表示/域身份。

## 4. 可直接调用的薄消费者

源：

scripts/fd2d-metric-R186-step-domain-arithmetic.mjs，4286 B，SHA256
9f8a9d48fd8096deef24192c9d4666424087e1e9b9055e00313f73e9c711b25d。

主函数为 r186StepArithmetic(input)。输入的 origin、endpoint、step 和 actual_trial
可以是实际 binary64 Number，或 [numerator, denominator] 两个整数的字符串数组。
Number 输入由 DataView 按原 IEEE754 位拆解为准确分数；不把十进制显示改成另一有理对象。

默认 origin 为 b075 的 $d_0$；默认 endpoint 为上限 $M$，并明确标识它只是参数盒上限，**不是已执行 QP 的输出**。Node 的可选第一个参数是这个 input 的 JSON；函数也可由 functions V8 同源调用。

所有判断用 BigInt 约分和交叉乘法。显示的 Number 比值不参与数学判断。
没有 scipy、NumPy、F/J 或任何积分依赖。

## 5. 实际执行与绑定

报告：

notes/2026-11-12-fd2d-metric-R186-step-domain-01-report.json，3035 B，SHA256
5e1c6cb209d97a927214f67fea985ebb479e10db93fd947742b0a89a073ba977。

该报告由完整保存源在 functions V8 中真实执行得到，采用默认 b075 原点及盒上限端点。准确比较验证前三个二分步的端点阈值不超过 $M$，八分之一步的阈值严格超过 $M$。没有 OS 子进程，因此没有 Python/Node exit code。

本次没有新的候选字段、方向实体、实际 Armijo trial、profile 盒或闭曲面证书。原 R186 证明和已经运行的求解器源码均保持不变。
