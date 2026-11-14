# Family 293 一手核查：超不变结论、实际 Lean 证明入口与后向归一机制的适用边界

- 日期：2026-11-13（UTC+8）
- 作者：boundary；kernel 独核 Domar 章节的归一尾估计与假设
- 性质：外部来源范围核查和直接可验证的对接障碍；不是普通不变子空间问题的解答。
- 固定来源版本：`openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`。
- 相关论文：OpenAI，*Backward intertwiners and a transitive commutant*，2026-09-27。

## 1. 已经核实的范围

该来源研究复、可分、无限维 Hilbert 空间上的有界算子。其主要结论是：存在非零范数拟幂零算子，其交换子代数传递、为强算子拓扑闭的真代数。因此它声称给出的是**超不变子空间问题**的否定答案。

这与普通不变子空间问题不同，而且区别在该论文自身的构造里可直接看见。它使用

$$
H_0=L^2(X,\mu;\ell^2(\mathbb Z)),\qquad X=\mathbb Z_2,
$$

以及逐纤维前移

$$
(Sf)(x)=S_xf(x),\qquad S_xe_j=\beta_j(x)e_{j+1},
\quad \beta_j(x)>0.
$$

对每个整数 $h$，

$$
\mathcal M_h=L^2\!\left(X;
\overline{\operatorname{span}}\{e_j:j\ge h\}\right)
$$

都是 $S$ 的非零、真、闭普通不变子空间。这一事实无需依赖其深层纤维分类定理：坐标前移本身已经保持该尾空间。

论文另造的 $V$ 将输入坐标 $h$ 移至 $h-1$，其系数几乎处处非零，故 $V\mathcal M_h$ 不包含于 $\mathcal M_h$。所以这些空间不超不变，正符合论文的目标。以上定位在正文：

- [introduction.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/sections/introduction.tex)：construction theorem 及随后讨论；
- [conclusion.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/sections/conclusion.tex)：小节 *Ordinary invariant subspaces and compactness*。

因此，本来源不满足本仓库普通 ISP 的完成标准，也没有解决目前边界的 $M=\overline{BM}$ 缺口。

## 2. Lean 的确切量词及证明文件

[范围文件 lean/docs/293.md](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/293.md) 对接：

- [ComparatorChallenges/BackwardIntertwiners.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/BackwardIntertwiners.lean)；
- [ComparatorChallenges/BackwardIntertwiners.json](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/BackwardIntertwiners.json)；
- [实际 solution：AlgebraCorollary.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Analysis/BackwardIntertwiners/AlgebraCorollary.lean)。

接口中的 `TransitiveCommutant T` 对每个复线性闭子空间 $K$ 要求：若**每个与 $T$ 交换的有界复线性算子**都保持 $K$，则 $K=0$ 或 $K=H$。它没有把“由 $T$ 保持”替换成这个更强前提。强算子拓扑用全部求值映射 $A\mapsto Ax$ 诱导，量词也正确地保留了完整、可分、无限维复 Hilbert 空间。

challenge 文件尾部的 `sorry` 是待比较接口，不能据此断言发布包没有证明。JSON 明确指定 solution 模块

`OAI.Analysis.BackwardIntertwiners.AlgebraCorollary`

和定理 `OAI.BackwardIntertwiners.direct_algebra_corollary`；允许的公理列为 `propext`、`Quot.sound`、`Classical.choice`。

实际 solution 的 95 行文件内有具体证明，而不是该定理的 `sorry` 或新公理：它先从显式幂界导出范数拟幂零，再把 $S,V$ 和标量乘子的共同传递性送到完整交换子，最后以 Hilbert 空间的线性等距同构运输模型。已读的

- [OperatorTransport.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Analysis/BackwardIntertwiners/OperatorTransport.lean)，
- [HilbertClassification.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/Analysis/BackwardIntertwiners/HilbertClassification.lean)

分别提供这些运输、交换子闭性与真性、可分无限维 Hilbert 空间分类的具体代码；后者定义的 `FullClaim` 与 challenge 的可见定义一致。

本次没有执行 Lean/Comparator，也没有遍历全部传递依赖。因此这里报告的是“已读实际证明入口及可见定义”，不声称已经独立重新编译或审核整个形式证明的公理闭包。普通不变尾空间已经足以排除将此结果当成本题完成的解释；无需为这个范围判断重跑全量形式化。

## 3. 后向 intertwiner 真正如何变得有界

[intertwiner.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/sections/intertwiner.tex) 全文给出如下机制。令 $\theta x=x+1$，要求

$$
(Vf)(\theta x)=V_xf(x),\qquad V_xe_j=b_j(x)e_{j-1}.
$$

交换关系等价于

$$
b_j(x)\beta_{j-1}(\theta x)=\beta_j(x)b_{j+1}(x).
\tag{3.1}
$$

先定 $\widetilde b_0(x)=1$，向两个方向递推。权被专门设计成使其对数沿 $\theta$ 的累积变化，在两端具有相反符号；Borel–Cantelli 仅需例外残余类的概率可和，无需独立性。得到共同不变满测集上

$$
\log\widetilde b_n(x)
 \le -(D-c)n+C(x)-c+4D(n-1)^{1/3},
$$

$$
\log\widetilde b_{-q}(x)
 \le -(D-c)q+C(x)+4Dq^{1/3},
$$

其中 $D-c=90>0$，而 $C(x)$ 只需逐点有限，可以不有界、不可积。因此

$$
1\le L(x)=\sup_{j\in\mathbb Z}\widetilde b_j(x)<\infty
$$

逐点成立。除以同一纤维标量 $L(x)$，得 $0<b_j(x)\le1$，并且 (3.1) 保持不变。在零测补集把各系数设零。由概率保持性，所得 $V$ 是有界收缩。

这里真正重要的是：整个前移 $S$ 是逐纤维算子，因此任何基底标量乘子 $M_g$ 都与 $S$ 交换；逐纤维公共归一不会破坏递推。它不要求 $L$ 或 $1/L$ 有双边一致界，也不要求 $V$ 满射。各 $b_j$ 非零仅保证每个尾的像在前一尾中稠密。

## 4. 原模型为什么不能直接照搬公共归一

以下两条可直接计算，不依赖外部定理。

### 4.1 一重加权遍历轮换

设 $(Y,\nu,\theta)$ 遍历且保持概率，$\omega>0$ 几乎处处，并取

$$
A=M_\omega U_\theta,\qquad (U_\theta f)(y)=f(\theta y).
$$

对有界 $g$，

$$
M_gA-AM_g=M_{\omega(g-g\circ\theta)}U_\theta.
$$

故 $M_g$ 与 $A$ 交换当且仅当 $g=g\circ\theta$ 几乎处处；遍历性迫 $g$ 为常数。因此，一重加权轮换中没有论文逐纤维模型所拥有的任意标量乘子交换子。把一个仅逐点有限的候选 intertwiner 除以一般 $L(y)$，会新增该交换子误差；论文的归一论证并不自动适用。

更具体地，若一个有界反向加权复合算子 $R$ 与 $A$ 交换，且 $AR$ 为标量乘子，则 $AR=M_\gamma$ 与 $A$ 交换，故 $\gamma$ 为常数。若该常数非零，则 $AR=RA=\gamma I$，使 $A$ 有有界逆。对于非零拟幂零 $A$ 这不可能；若常数为零，$A$ 的单射性又迫 $R=0$。这排除的是这种单步反向复合形式，不排除一般非局部交换子。

### 4.2 当前边界的单向移位

设 $Be_0=0$、$Be_n=\beta_ne_{n-1}$，其中所有 $\beta_n>0$。有界对角算子 $\Delta e_n=g_ne_n$ 与 $B$ 交换，迫 $g_n=g_{n-1}$，所以也只能是常数。

若 $Re_n=r_ne_{n+1}$ 是正向单步加权移位且 $BR=RB$，在 $e_0$ 上比较得到 $\beta_1r_0=0$。随后递推

$$
\beta_{n+1}r_n=\beta_nr_{n-1}
$$

给出全部 $r_n=0$。因此不存在非零的这种反向单步交换子。论文里的 $V$ 同时改变双边坐标和基底 $x$，不属于这个被排除的单边模型。

这些观察没有证明一切新交织都不可能。它们准确指出尚缺的结构：必须构造到当前 $A$ 或其真实边界缺陷的合法有界交织，并检查其定义域、单射性及对相应闭子空间的行为；增加独立 $\ell^2(\mathbb Z)$ 纤维并换成另一组权并未提供该交织。

## 5. 纤维分类假设也不同

[criterion.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/sections/criterion.tex) 及其输入 [domar-proof.tex](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/build/sections/domar-proof.tex) 使用正递减双边权 $w_j$，要求 $\log w_j$ 在负半轴凸、正半轴凹，

$$
\sum_{j\ne0}w_j^{1/j}<\infty,\qquad
\frac{\log w_n}{n^2}\to-a,\quad
\frac{\log w_{-n}}{n^2}\to a,\quad a>\log3.
$$

kernel 已独核其两个卷积尾均先除对应的接触点基准再估计，因此不是只得绝对尾小量而误当相对小量。

这些凸凹条件和二次渐近迫 $\beta_j=w_{j+1}/w_j$ 在两端以指数速度趋零，故每个纤维移位紧。当前 $\alpha_{v_2(n)}$ 权在奇数处反复等于固定 $\alpha_0>0$，而在 $2^m$ 处趋零，既不具这种半轴单调结构，也不趋零。不能把该纤维分类定理直接套到当前边界移位，或以有界相似把非紧边界移位变成这种紧纤维移位。

## 6. 额外桥 $S'=\operatorname{SOTalg}(S)$ 在该构造本身失败

并非只缺少该等式的证明；论文模型中可直接看出它不成立。对非 $\theta$-不变的有界 $g$，在输出基点 $\theta x$ 比较：

$$
(VM_gf)(\theta x)=g(x)V_xf(x),\qquad
(M_gVf)(\theta x)=g(\theta x)V_xf(x).
$$

由于所有纤维系数几乎处处正，选一个非不变残余类指标函数便得到 $VM_g\ne M_gV$。但 $V$ 和 $M_g$ 都属于 $S'$，所以 $S'$ 非交换。

单个算子的多项式代数的强闭包则交换：每个极限先与所有多项式交换，再利用固定有界算子的乘法强连续性使两个极限互相交换。因此该模型不可能满足 $S'=\operatorname{SOTalg}(S)$。

已核的外部来源值得作为超不变问题和有界纤维输运的资料保存；当前没有从该模型到原 Haar $A$ 或 $W=M\ominus\overline{BM}$ 的新合法交织。边界研究应继续处理实际混合头尾项及其正能量，而不把这份外部结果登记为普通 ISP 已完成。
