# R276：完整原 σ 行的仿射无穷范数严格下降区间与十个原试步

类型：完整数学证明；有限保存数组的精确代数，不是新的非线性接受规则。

作者：`exact_refinement`（公开课题协作）；日期：2026-11-15。

## 276.1 对象、范围及与原 native 方程的对应

固定一个有限、非空的完整行集合 $\mathcal I$。每行给定实数 $r_i,e_i$ 和严格正的实际行尺度 $\sigma_i>0$。本文不删行，不把小的非零量改成零，也不要求矩阵可逆。定义

$$
d_i=e_i-r_i,\qquad a_i=\frac{r_i}{\sigma_i},\qquad
v_i=\frac{d_i}{\sigma_i},\qquad
\rho=\max_{i\in\mathcal I}|a_i|,
$$

以及对实数步长 $\alpha$ 的完整仿射预测

$$
F(\alpha)=\max_{i\in\mathcal I}|a_i+\alpha v_i|
=\max_{i\in\mathcal I}\frac{|(1-\alpha)r_i+\alpha e_i|}{\sigma_i}.
\tag{276.1}
$$

本课题的应用取当前保存矩阵 $A$、当前保存二进制浮点方向 $\delta$，并把保存数组视为精确实数，令 $e=A\delta+r$。于是 $r+\alpha A\delta=(1-\alpha)r+\alpha e$ 是恒等式。这里的 $A$ 是对应当前 snapshot 的完整有限矩阵，不自动等于原连续问题的精确导数；[R266](R266-native-block-Newton-defect-and-original-scaled-descent.md) 已区分了这些对象。

对 $M=112,K=224,D=576$ 的原 shooting 坐标，行序和尺度是：

| 行类 | 保存的原 $r$ | $A\delta$ | 行尺度 |
|---|---|---|---|
| cut，112 行 | 实际保存的 $Q_0-\mathrm{target}$ | $\delta_{0,Q}$ | $\sigma_0$ |
| stage $n$，224 行，$0\le n<576$ | 实际保存的 $\mathrm{out}_n-y_n$ | $J_n\delta_{n+1}-\delta_n$ | $\sigma_n$ |
| far，112 行 | 实际保存的 $\Pi_D-G_DQ_D$ | $\delta_{D,\Pi}-G_D\delta_{D,Q}$ | $\sigma_D$ |

共有 $112+576\cdot224+112=129248$ 行。cut/far 的实际非零误差均保留，阻尼方向的这些分量不投影、不清零。本文的 $r$ 指上述减法已经执行后保存的 binary64 数值；不在精确读回中用原始端点重新计算一个不同的 $r$。

实际原尺度也按已保存 binary64 数值使用。源码中的生成规则为 $\sigma_0=\max(10^{-250},\max_j|\mathrm{target}_j|)$，后续按原 gain 递推；本文不重新生成尺度，也不先把 $J/\sigma$ 或 $r/\sigma$ 舍入成另一矩阵。所有精确比较都在原未缩放 $r,e$ 形成后除以实际 $\sigma$。

## 276.2 完整严格下降区间

先处理退化情形。若 $\rho=0$，则每个 $r_i=0$，并且 $F(\alpha)\ge0=\rho$。因此任意正步长都不可能满足 $F(\alpha)<\rho$，包括 $e=0$ 的情形。

以下设 $\rho>0$，并定义非空活跃行集合

$$
\mathcal A=\{i:\ |r_i|=\rho\sigma_i\}.
\tag{276.2}
$$

**定理 276.1（全部有限行的充要条件）。** 存在某个 $\alpha>0$ 使 $F(\alpha)<\rho$，当且仅当每个活跃行都严格朝区间内部运动，即

$$
r_i(e_i-r_i)=r_i d_i<0\qquad(i\in\mathcal A).
\tag{276.3}
$$

若条件成立，对每个非零斜率定义

$$
t_i=
\begin{cases}
\displaystyle\frac{\rho\sigma_i-r_i}{d_i},&d_i>0,\\[6pt]
\displaystyle\frac{\rho\sigma_i+r_i}{-d_i},&d_i<0,
\end{cases}
\qquad
\alpha_* = \min_{i:\ d_i\ne0}t_i.
\tag{276.4}
$$

则每个 $t_i$ 都严格正，$\alpha_*$ 有限且严格正，完整正步长严格下降集合恰为

$$
\{\alpha>0:F(\alpha)<\rho\}=(0,\alpha_*).
\tag{276.5}
$$

并且 $F(\alpha_*)=\rho$；对任意 $\alpha>\alpha_*$，有 $F(\alpha)>\rho$。

**证明。** 若 $i$ 是活跃行，则 $r_i\ne0$。假如 $r_i d_i\ge0$，它或保持端点不动，或朝同号外侧运动。因此对每个 $\alpha>0$，

$$
|r_i+\alpha d_i|\ge |r_i|=\rho\sigma_i,
$$

从而 $F(\alpha)\ge\rho$。这证明了条件的必要性，也涵盖活跃行零斜率。

反之，假设所有活跃行满足 (276.3)。当 $d_i=0$ 时，该行不能活跃，所以 $|r_i|<\rho\sigma_i$，它对所有步长都严格位于内部。

当 $d_i>0$ 时，若初值等于右端点 $r_i=\rho\sigma_i$，就违反 (276.3)；因此 $\rho\sigma_i-r_i>0$，且 $t_i>0$。由于初值满足 $r_i\ge-\rho\sigma_i$，对每个正 $\alpha$，左侧严格不等式 $r_i+\alpha d_i>-\rho\sigma_i$ 自动成立，右侧严格不等式等价于 $\alpha<t_i$。

当 $d_i<0$ 时同理，初值不可能在左端点且朝左运动，所以 $\rho\sigma_i+r_i>0$；对正 $\alpha$，右侧严格不等式自动成立，左侧严格不等式等价于 $\alpha<t_i$。于是每一非零斜率行的严格内部条件都是 $0<\alpha<t_i$。

活跃集合非空且所有活跃斜率非零，因此参与 (276.4) 的集合非空。它是有限集合，元素均有限且正，所以最小值有限且正。将全部行的条件取交集即得 (276.5)。在 $\alpha_*$ 至少一行触及其运动方向的端点，其余行都未越界，故 $F(\alpha_*)=\rho$。任何更大步长都使该触界行严格越界，故 $F(\alpha)>\rho$。证毕。

**范围提醒。** 上界必须对全部 $d_i\ne0$ 的行取最小值。活跃行决定正下降区间是否存在；初始不活跃的行可以先撞到边界，决定其长度。只检查当前最大行或只取活跃行的触界值，不给出完整系统的 $\alpha_*$。

## 276.3 右方向导数与原十个试步

**推论 276.2。** 当 $\rho>0$，

$$
F'_+(0)=\max_{i\in\mathcal A}\frac{\operatorname{sign}(r_i)d_i}{\sigma_i}.
\tag{276.6}
$$

因此定理中的条件等价于 $F'_+(0)<0$。

**证明。** 每个活跃行的 $r_i\ne0$，所以在足够小的右邻域内，其绝对值函数有上述斜率。由于行数有限，所有不活跃行与 $\rho$ 的正间隙在一个共同足够小的右邻域内仍不会使其超过所有活跃行。有限个仿射函数的最大值在该右邻域具有右方向导数，等于初始活跃斜率的最大值。最大值严格负，当且仅当所有活跃斜率严格负，即 (276.3)。证毕。

原 native line search 固定尝试

$$
\alpha_k=2^{-k},\qquad k=0,1,\ldots,9.
\tag{276.7}
$$

不改变这些试步的前提下，精确仿射模型中存在一个原候选严格下降，当且仅当 $\rho>0$、(276.3) 成立，并且

$$
2^{-9}<\alpha_*.
\tag{276.8}
$$

此时模型严格下降候选恰为满足 $2^{-k}<\alpha_*$ 的那些原候选；等号只给持平，不能计作严格下降。证明直接由 (276.5) 以及原集合中最小正步长为 $2^{-9}$ 得到。这里没有建议增加第十一个试步，也没有给实际 native trial 新增准入条件。

**已有完整端点报告的充分结论。** 设 $\varepsilon=\max_i|e_i|/\sigma_i$。对 $0<\alpha\le1$，由每行三角不等式再取最大值，

$$
F(\alpha)\le(1-\alpha)\rho+\alpha\varepsilon.
$$

若已有精确报告满足 $\varepsilon<\rho$，则全部十个原候选在这个仿射模型中都严格下降。这个充分结论只需两个完整精确端点最大值，不必先生成十条曲线。反之，$\varepsilon\ge\rho$ 并不排除较小正步长下降；是否存在、哪些原候选满足，以及边界由哪一行决定，仍由 (276.3)–(276.8) 给出。这里的 $\varepsilon,\rho$ 均指同一当前方向、同一原 $\sigma$ 的精确完整行读回，不能拿 formed-model 的普通浮点读数替换。

若 $e,r,\sigma$ 来自有限二进制数组，取共同整数单位 $u=2^{-2148}$，写

$$
r_i=R_i u,\qquad e_i=E_i u,\qquad \sigma_i=S_i u,\qquad S_i>0.
$$

现有完整 exact ledger 已保存每个 $E_i$ 的精确有符号 dyadic 编码；$R_i,S_i$ 可由原 binary64 字节精确解码。于是十个候选直接给出

$$
\frac{r_i+2^{-k}(e_i-r_i)}{\sigma_i}
=\frac{(2^k-1)R_i+E_i}{2^k S_i}.
\tag{276.9}
$$

各行绝对值、并列最大行及阈值比较均可用整数交叉乘积完成。若 $\rho=p/q$ 为约分后的非负有理数，则 (276.4) 也可直接写成整数比，例如 $D_i=E_i-R_i>0$ 时

$$
t_i=\frac{pS_i-qR_i}{qD_i}.
\tag{276.10}
$$

所以此诊断不需要重新形成 $J\delta$，不需要任何 RHS、J、ODE 或 QR 调用。它不是字节审计：式 (276.9)、(276.10) 和完整比较是新增精确科学算术，必须在获授权的公开 Actions 中执行。

## 276.4 与原浮点范数、formed 阻尼目标及真实 trial 的区别

第一，$\rho$ 是保存的原 $r$ 除以保存的原 $\sigma$ 的精确有理最大值。原 `evaluate` 执行 binary64 除法后再取最大值。报告中应同时保留该实际 `baseNorm` 的原 numberRecord；不能未经核验就称它与 $\rho$ 是同一实数或同一字节。本文对精确模型的严格下降集合以 $\rho$ 为基线；另可如实报告各预测值与实际保存的 `baseNorm` 数值的精确比较，但仍不是实际 trial 预测保证。

第二，[R273](R273-complete-native-damped-square-root-chain.md) 的 QR 方向来自带 $\eta$ 的完整二范数目标。该求解器的 `formed_model_diagnostic` 读回 formed 系数和 scaled $z$，其中权重/列尺度形成及方向恢复存在已声明有限精度。本文使用的 $e$ 则来自已经恢复并保存的原坐标 binary64 $\delta$，在原未缩放 $J,r$ 上精确累加，再除以原 $\sigma$。两者对象不能互换；即使某个二范数目标下降，也不推出 (276.3)。

第三，令 $Y$ 是保存的基态。实际原 trial 是按原源码括号形成的有限数组，可记为 $\widehat Y_\alpha$。设

$$
h_\alpha=\widehat Y_\alpha-Y-\alpha\delta.
$$

即使只考察同一有限矩阵的仿射函数，实际舍入后的状态所对应的值也为

$$
r+A(\widehat Y_\alpha-Y)
=(1-\alpha)r+\alpha e+Ah_\alpha.
\tag{276.11}
$$

本文没有计算 $h_\alpha$ 或 $Ah_\alpha$。真正的原 no-J `evaluate` 又重新执行 flow/root/RK、端点减法、归一化及 guards。若用一个可微数学残差 $\mathcal R$ 来讨论它，还须另列保存的 $A$ 与 $D\mathcal R(Y)$ 的误差、非线性余项以及实际评价舍入。这些项都不包含在 (276.1) 中。

因此 $F(\alpha)<\rho$ **不保证** 原 native 规范下降、guard 通过或最终接受；$F(\alpha)\ge\rho$ 也不能单独证明实际非线性 trial 必然失败。诊断仅解释这次已保存方向在同一完整有限线性模型中的表现。原 32 次 Newton 上限、十个试步、严格原规范比较、原容差以及最终 J/audit 均保留。

对当前 61/73 导出，`native_trials.jsonl` 保留实际试步标量范数与拒绝原因，没有完整每次 trial 的残差向量。fresh-withJ snapshot 与其方向可精确配对，实际 trial 标量也可按 call/iteration/trial 配对；但两个范数的差不是逐分量非线性余项。不能从这个标量差分解状态舍入、J 表示误差与非线性三项。[R275](R275-original-noJ-primal-identity-and-complete-variational-chain.md) 的新 primal 对齐范围同样不免除上述区分。

## 276.5 可核验实现合同与结论边界

独立实现 `exact_20261115_native_affine_infinity_prediction.py` 对明确绑定的原 61 或 73 输入执行以下只读科学诊断：

1. 绑定原 outer result 或显式 partial journal、snapshot/context/manifest、原 core/evaluate/十试步源码身份、当前矩阵 definition、方向原字节、完整 exact ledger 及九个非 J 输入原件。
2. 按 cut112、stage576×224、far112 的原顺序验证完整 129248 行；所有行的实际 $\sigma$ 必须有限且正。切向/方向来源和 signed-zero 字节身份保留。
3. 精确读回 $\rho$、每个原 $\alpha_k$ 的完整最大值、坐标及 cut/stage/far 分项最大值；核 $\alpha=1$ 与已有完整 exact endpoint 读数是同一对象。
4. 输出 $\rho=0$ 或活跃行阻断的明确情况；否则按全部非零斜率输出 $\alpha_*$、第一触界行及全部原十试步的严格比较。所有十进制串只供显示，精确分数和比较才是计算依据。
5. 原 trial 的实际 scalar/guard 记录单独保留。没有发生的 trial 不伪造，没有保存的完整 trial 残差不重建；计算失败只标本诊断失败，不改变已经发生的原 science 结果。

实现不导入科学求解器，不重读 J 做乘法，不重新优化方向，不修改任何原件，也不把诊断输出接入 native 接受规则。其完整身份和数据范围用于可复核归因；完整 factor/J 的字节审计仍由原专用 byte reader 独立完成。

本文证明没有使用任何尚未收到的 73 数值结果，也不预设 73 成败或后继方向。
