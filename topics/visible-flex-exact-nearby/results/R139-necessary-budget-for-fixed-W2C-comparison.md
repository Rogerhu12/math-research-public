# R139：固定 W2C 比较配方的必要预算与提前排除门

2026-11-20，`visible-exact-astra-ac637-20261120`。

**状态：已证明。** 本文给当前固定 WVC 参考的充分比较配方一个必要预算。它只比较已经选定的上界数，不给真实算子范数的下界，也不推出奇异。新的低频族差比较尚待公共 Actions 首次计算；本文不报告任何尚未发生的数值结果。

依赖为 [完整 W2C 候选](R133-supplement-complete-collar-Volterra-dual-feedback-candidate.md)、[完整 WJK 中心核](R133-supplement-joint-centre-Green-kernel-and-complete-collar-cross-terms.md)及公共 run [43891414339/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43891414339) 的既成 WVC 记录。这里的参考仍是 WVC，不换成 WCTR。

## 1. 需要比较的是配方中的固定上界数

记已经选定的非负上界数为

$$
e=e_\rho,\quad \beta=\epsilon_b,\quad o=o_H,\quad b=o_b,\quad T=T_{\rm old},\qquad w=\frac65.
$$

令 $K\ge0$ 为完整 signed centre 比较的上界，$\epsilon\ge0$ 为完整 family/dual 误差上界。W2C 的同一充分门为

$$
\begin{aligned}
\mathcal G(K)={}&e+(1+e)\sqrt{w^2(K+\epsilon)^2+\beta^2}
 +\sqrt{w^2o^2+b^2}\\
 &+3T\{(1+e)(K+\epsilon)+o\}<1.
\end{aligned}
\tag{N1}
$$

全四个有限 Schur 块、两 RHS、真实无限高块逆界3、原有限参考的 $\rho$ 和端点费用均在此配方中。本文不删其中任何一项。

**命题1。** 固定上述全部非负数后，$\mathcal G$ 在 $[0,\infty)$ 连续且严格递增，且

$$
\mathcal G(K)\ge\mathcal G(0).
\tag{N2}
$$

**证明。** 若 $K_2>K_1\ge0$，则 $(K_2+\epsilon)^2>(K_1+\epsilon)^2$。因 $w>0$、$1+e>0$，第一根式项严格增加，最后线性项非减，其余项不变。连续性直接成立。证毕。

因此，若有向区间计算证明所选常数所确定的 $\mathcal G(0)$ 的下端不小于1，则此配方对任何尚未计算的 $K\ge0$ 都不能通过。这个结论允许停止该配方的后续中心计算，但不表示真实算子的误差至少为1：真实误差可以远小于目前所选的上界。

## 2. 不先计算完整 family 也可用的有理门

原 WVC 成功运行的下列完整记录只读复用：

| 记号 | 原完整字段 | 原球的位置足以推出 |
|---|---|---|
| $e$ | `complete_reference_rho_defect_upper` | $e>7/100$ |
| $\beta$ | `complete_outer_paired_error_upper` | $\beta>2/3$ |
| $b$ | `complete_outer_endpoint_correction_upper` | $b>1/8$ |
| $T$ | `complete_actual_T_upper` | $T>15/4$ |

原记录在 `notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json` 的相应完整图中。四个原球分别包含在 $(.071,.072)$、$(.668,.669)$、$(.1257,.1258)$、$(3.897,3.898)$；这些宽有理区间直接由已保存球的中心和误差读得，不重算任何旧科学目标。实际消费时仍使用原完整记录和原有向端点，不用此表的小数代替它们。

置 $h=K+\epsilon\ge0$。由 $\sqrt{w^2h^2+\beta^2}\ge\beta$、$\sqrt{w^2o^2+b^2}\ge b$ 及 $o\ge0$，逐项得到

$$
\begin{aligned}
\mathcal G(K)
&\ge\frac7{100}+\frac{107}{100}\frac23+\frac18
 +3\frac{15}{4}\frac{107}{100}h\\
&=\frac{109}{120}+\frac{963}{80}h.
\end{aligned}
\tag{N3}
$$

特别地，若 $h\ge1/128$，则

$$
\boxed{\quad
\mathcal G(K)\ge\frac{109}{120}+\frac{963}{80\cdot128}
=\frac{30793}{30720}>1.\quad}
\tag{N4}
$$

于是 $K+\epsilon<1/128$ 是这套固定配方成功的必要条件。式(N4)还有明确的有理余量 $73/30720$，没有对接近1的浮点比较作任何假设。

W2C 的完整 family 预算是四个非负上界数之和：

$$
\epsilon=L+C+Q+\delta E.
\tag{N5}
$$

其中 $L$ 是完整低频族差 $G_f\Delta A_LS^{-1}$ 的所选比较上界；保留独立物理 mean 和全部193个 root/mean/weighted-outer 观察。它正是原 graph3 的 `complete_low_family_feedback_norm_upper`。另外两项为 cross、trial family 误差，最后为完整 dual/primal residual 乘积。

**推论2。** 若第一次计算这个完整 $L$ 的三个 row/column/norm 记录后，严格证明所选 norm 上界数 $L\ge1/128$，则对任意其余非负费用和任意 $K\ge0$，同一固定配方都不能通过(N1)。

**证明。** $h=K+\epsilon\ge\epsilon\ge L$，应用(N4)。证毕。

这里的 $L$ 是算法选定的、用于(N5)的**上界数本身**。对这个数取有向下端并比较 $1/128$，是在证明所选配方预算过大，绝不是把它当成真实 $\|G_f\Delta A_LS^{-1}\|$ 的下界。换用更尖锐的比较、不同参考或联合保留有符号项，可能得到另一套预算；本文不排除它们。

## 3. 未被排除时的精确剩余中心预算

当 $\mathcal G(0)<1$ 已成立，令

$$
\lambda=3T,\quad c=\sqrt{w^2o^2+b^2},\quad
s=\frac{1-e-c-\lambda o}{1+e}.
$$

则 $s>\beta$。方程 $\sqrt{w^2x^2+\beta^2}+\lambda x=s$ 在 $x\ge0$ 有唯一根

$$
x_*=
\frac{s^2-\beta^2}
{\lambda s+\sqrt{w^2(s^2-\beta^2)+\lambda^2\beta^2}}.
\tag{N6}
$$

因此 $K_*=x_*-\epsilon>0$，且(N1)准确等价于 $0\le K<K_*$。

为证明(N6)，将方程平方、移项并把正根有理化，得到所示表达式。分母严格为正。由于

$$
\lambda x_*<\frac{s^2-\beta^2}{s}\le s
$$

在 $\lambda>0$ 时由分母中严格正的根式项成立，且 $\lambda=0$ 时 $\lambda x_*=0<s$ 显然成立，所得根满足平方前的正号条件，没有赝根。严格单调性给唯一性。这个表达式在 $\lambda=w$ 时也无除零问题。

(N6)只是精确剩余预算公式；当前没有把它冒称为已经求出的数值许可半径。

## 4. 首次科学计算及诚实的完成范围

可以先独立计算 $L$，无须先运行原 graphs1/2，亦无须构造昂贵的完整中心 signed kernel。其比较算子正是现有源码的全低模态 $G_f$ 比较与逐面板 $\|\Delta A_L\|\|S^{-1}\|$ 的有序复合；源域、径向长度、独立 mean、全部193观察不变。私人参考定义和系数包的物化不是重算旧成功范数目标。

这一运行若完成，只记原50条中的3条已成，明确列出其余47条未计算。若推论2触发，则登记“既定充分比较配方不可能通过”，不登记“已算完整五图”，更不登记有限逆、真实奇异性或本题完成。若推论2没有触发，后续完整graph3应原字复用这三条成功记录，其余新目标继续计算，不重跑这三条。

所有正负侧物理列、真均值/相位/参数行、全频逆、非线性迭代、单frame与闭合匹配，以及固定度量精确可见闭族，仍按 `open.md` 的实际义务继续。
