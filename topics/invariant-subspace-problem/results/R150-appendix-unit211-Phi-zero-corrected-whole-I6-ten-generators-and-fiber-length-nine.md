# 正确 Phi：完整六式全权十生成与每权纤维长度至多九

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-28（Asia/Taipei）。

**状态：独立纸面收紧，无新执行。** 利用已付的完整六式最高无穷方向排除，以及第三个真均值在二次头中的独立性，可以把[全权十三生成](R150-appendix-unit211-Phi-zero-corrected-original-N1-highest-unit-and-whole-I6-thirteen-generators.md)进一步收紧为
$$
\boxed{
\mathcal B_6\text{ 由 }
1,t,t^2,t^3;\quad f,tf,t^2f;\quad V,tV,t^2V
\text{ 这十元生成为 }\mathcal A\text{ 模。}
}
\tag{1}
$$
同时，对每个权剩余域 $k$，
$$
\boxed{\dim_k(\mathcal B_6\otimes_{\mathcal A}k)\le9.}
\tag{2}
$$
(1) 是全系数环中的明确生成结论；(2) 是保留幂零的纤维长度界。本文不把 (2) 写成“全环九生成”，不要求原模自由或平坦。

## 1. 原环与已付最高系统

保持十三生成论文的同一系数环，不增加单位。记
$$
s=u-1,\quad \delta=1-Q,\quad K_w=Q+4s,\quad
L=Q-2s(u-2),\quad \ell=L/Q,
$$
$$
M_n=2uL-L^2-u^2Q,\qquad M=M_n/Q,
$$
并置
$$
\mathcal A=
\mathbb Q[u,Q,(uQ\delta sK_wLM_n(2\ell-1))^{-1}].
\tag{3}
$$
本环适用于已付原单位的当前正确 Phi、distinct singleton、物理 $D\ne0$ 权图；必要代数本身尚未反演任何几何量。这里没有加入 $m=u-\ell$ 的逆，也不借其它图的单位。

令
$$
I_6=(\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS),\qquad
\mathcal B_6=\mathcal A[t,f,V]/I_6.
$$
给 $t,f,V$ 总次数一，权量次数零。四个前列原式次数至多二，最后两式次数至多三。记六个最高齐次部分生成的理想为
$$
\mathcal J_6=
(R,E_{B,e}^{(2)},E_{B,o}^{(2)},N_{1,2},NS_3,PS_3).
\tag{4}
$$

此前已经在全环证明：三个真均值头
$$
\det H_{f,V}=\frac{32uQ(2\ell-1)}{M^2}
\tag{5}
$$
为单位；$t=0$ 的最高图为空；$t=1$ 上，完整 NS/PS 的 Loww 身份给
$\xi^6=\eta^6=0$，而完整原 $N_1$ 最高极化给单位
$-4(u-1)^4/P_{02}$。因此 (4) 在每个权剩余域上没有 projective 共同零方向。

本条只使用这些已证原身份。原 N1 极化与幂零证明不重做，任何旧错误 compact 均值后继也不恢复。

## 2. 每个剩余域中的 $(2,2,3)$ 完全交

固定 $\mathcal A$ 的任意素理想的剩余域 $k$（特别包括全部极大剩余域）；它是特征零的无限域。记
$$
S=k[t,f,V],\qquad J=\mathcal J_6\otimes_{\mathcal A}k.
$$
由 (5)，三个真均值二次式在 $S_2$ 中线性独立，而且它们的 projective 共同零集有限。可从它们的线性空间中选两条无共同曲线的二次式 $q_1,q_2$。

由于 $J$ 没有 projective 共同点，可以在 $J_3$ 中选 $q_3$，使它避开有限集
$V(q_1,q_2)\subset\mathbb P^2_{\overline k}$。具体地，每个点已有某个二次或三次原生成元不为零，乘一个适当单项式可补到三次；无限域上的有限线性避让给同时满足的 $q_3$。

于是
$$
A_k=S/(q_1,q_2,q_3)
$$
是次数 $(2,2,3)$ 的齐次 Artin 完全交，其 Hilbert 级数为
$$
\frac{(1-x^2)^2(1-x^3)}{(1-x)^3}
=(1+x)^2(1+x+x^2)
=1+3x+4x^2+3x^3+x^4.
\tag{6}
$$
所以 $\dim_kA_k=12$，顶次为四。

该完全交是 graded Gorenstein，socle 恰为一维的 $(A_k)_4$，且各乘法配对
$$
(A_k)_i\times(A_k)_{4-i}\longrightarrow(A_k)_4\simeq k
\tag{7}
$$
非退化。这里可直接由三个正则齐次式的 Koszul 分解取对偶：其 canonical module 为
$A_k(2+2+3-3)=A_k(4)$；对 Artin graded 商，这正给 (7) 的有限维对偶身份。

## 3. 第三个均值使次数四全部消失

三个原均值的二次部分线性独立，而 $q_1,q_2$ 只张成其中二维空间。故可选第三条原均值的 $k$ 线性组合 $r$，满足
$$
r\notin\operatorname{span}_k(q_1,q_2).
$$
由于 $q_3$ 为三次，完全交理想的次数二部分恰是
$\operatorname{span}_k(q_1,q_2)$。因此
$$
0\ne\overline r\in(A_k)_2.
\tag{8}
$$
这里非零性直接来自真三均值头 (5)，不从 generic 秩或某个数值权点推断。

由非退化配对 (7)，存在 $b\in(A_k)_2$ 使
$\overline r b\ne0$。因为 $(A_k)_4$ 一维，
$$
(\overline r)_4=(A_k)_4.
\tag{9}
$$
所有更高次数在 $A_k$ 中本来已为零，所以 $A_k/(\overline r)$ 的次数四及以上全部为零。$J$ 含 $q_1,q_2,q_3,r$，因而
$$
\boxed{J_4=S_4.}
\tag{10}
$$

此外，
$$
\overline r(A_k)_1\ne0.
\tag{11}
$$
若它为零，因 $A_k$ 由次数一生成，$\overline r$ 将被整个正次数极大理想杀死，从而属于 socle。但其次数为二，而 socle 仅在四次，与 (8) 矛盾。

因此理想 $(\overline r)$ 在次数二、三、四各至少占一维；这些是不同 graded 分量。由 (6)，
$$
\dim_k S/J
\le \dim_k A_k/(\overline r)
\le12-1-1-1=9.
\tag{12}
$$
这一步同时保留非约化结构；不是仅计算不同几何点数。

## 4. 固定十五坐标满射拼回整个权环

(10) 在每个极大剩余域成立，但不把逐剩余域选出的 $q_i,r$ 当作全局参数或额外可逆主元。

直接用 (4) 的固定六个原最高式构造次数四的原乘子映射：
$$
\Psi_4:
\mathcal A[t,f,V]_2^{\oplus4}
\oplus
\mathcal A[t,f,V]_1^{\oplus2}
\longrightarrow
\mathcal A[t,f,V]_4.
\tag{13}
$$
四个二次生成元乘全部六个二次单项式，两个三次生成元乘全部三个一次单项式。源有 30 个明确原列，目标是秩
$$
\binom{6}{2}=15
$$
的自由 $\mathcal A$ 模。

由 (10)，$\operatorname{coker}\Psi_4$ 在每个极大剩余域上为零。它是有限生成模，所以局部 Nakayama 引理与有限模支持给
$$
\boxed{(\mathcal J_6)_4=\mathcal A[t,f,V]_4.}
\tag{14}
$$
右端自由，因此每个四次单项式都存在真正的 $\mathcal A$ 系数原齐次表示。不必展开一个巨大右逆，也不需要把选择正则序列时出现的局部系数付成新的全局单位。

## 5. 完整原式的全权十生成

在 (14) 的各原表示中，把六个最高式换回完整
$\mathcal R,E_{B,e},E_{B,o},N_1,NS,PS$。由于补回的项次数更低，得到：每个四次单项式在 $\mathcal B_6$ 中可降为总次数至多三。对更高单项式反复使用，总次数严格下降。

再用[原 t 参数真均值三生成](R150-appendix-unit211-Phi-zero-corrected-whole-t-parameter-three-mean-generators-and-monic-lambda-cubic.md)的完整规则
$$
f^2,\ fV,\ V^2
\equiv a_0(t)+a_f(t)f+a_V(t)V,
$$
$$
\deg_ta_0\le2,\qquad
\deg_ta_f,\deg_ta_V\le1.
\tag{15}
$$
它们严格降低 $(f,V)$ 次数，不增加总次数。于是所有总次数至多三的单项式都落入 (1) 的十元张成，证明全权十生成。

这只是固定原多项式商的真实降次；不要求三生成表示自由，也不将裸余式矩阵无条件视为结合代数。加入其它原必要值条件的任意商仍保此界。

## 6. 纤维长度至多九：使用原次数过滤

固定上述 $k$，令
$$
B_k=k[t,f,V]/(I_6\otimes_{\mathcal A}k).
$$
给 $B_k$ 标准总次数过滤。每个原生成元的最高部分均属于其 initial ideal，所以
$$
\operatorname{gr}B_k
\text{ 是 }S/J\text{ 的商。}
\tag{16}
$$
若某个最高项在该权点消失，(16) 仍然成立：零最高项不增加约束，而完整专门化式可能另给更低次 initial 关系。这里没有假定权专门化与取 initial ideal 相等或交换。

由 (12)、(16)，$\operatorname{gr}B_k$ 有限维且维数至多九。过滤在有限次数稳定，故
$$
\dim_kB_k=\dim_k\operatorname{gr}B_k\le9.
$$
这证明 (2)，也在进一步代数闭包后保留全部几何纤维长度。

每个纤维至多九，不等于已经选择了九个能在全 $\mathcal A$ 上同时生成的固定元素。本文全环结论仍是 (1) 的十生成；未声明全环九生成、模自由、平坦性或恒定纤维长度。

## 7. 适用范围

由十生成及行列式技巧，存在原 $t$ 的全权首一至多十次关系；本文未展开其系数或执行新乘法表。已有非零纯权支持仍限制权参数，但公共权曲线尚未由本条排除。

所有生成和纤维长度先在未反演几何量的必要代数中成立。随后取当前物理 $D\ne0$ 等开集，固定权纤维的长度或点数不会增加；几何局部化本身未必继续是有限 $\mathcal A$ 模。

本文不计入恢复 $\rho$、singleton 谱值或独立 $U_0$ 尺度的额外有限关系，因而不把 9 或 10 直接宣布为完整规范原点数。先前十三生成、二十二生成及最高单位证明保留独立正确状态。本条只增加完全交对偶与第三真均值的利用，不增加执行、重复门或系数载荷。
