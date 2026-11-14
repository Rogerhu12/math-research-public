# R12 后续附录：有限放大子商的紧夹积极限与回传轨道成本

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：**已证明的定量推论。** 从原 Haar 模型的真实 dyadic 幂出发，结论对任意实际有限放大的闭不变旗子商成立。这里的紧算子与回传算子不要求属于原交换子；没有构造不变子空间，也没有排除全部外部紧交织。

## 1. 原归一化幂与所有实际旗子商

沿用 [R12](R12-normalized-powers-and-compact-commutant.md) 的真实矩阵单位：
$$
N_j=\frac{A^{2^j}}{d_j},\qquad d_j=\|A^{2^j}\|,\qquad
\|N_j\|=1,\quad \|N_j-E_j\|=\eta_j,\quad \|N_j^2\|=\eta_j,
$$
$$
\eta_j=\exp(-1400\,16^j+630\,8^j-300\,2^j).
\tag{1.1}
$$
$E_j$ 在第 $j$ 位为 $e_{10}$，其余位为恒等；
Haar 乘积表示的每位参考向量是
$\Omega=(e_0+e_1)/\sqrt2$。

除 R12 的 $N_j\to I/2$ 于 WOT 外，还直接有
$$
\boxed{N_j+N_j^*\longrightarrow I\quad\text{于 SOT}.}
\tag{1.2}
$$
事实上，第 $j$ 位的 $E_j+E_j^*$ 是交换 $e_0,e_1$ 的酉，
固定参考向量 $\Omega$。对只依赖前 $m$ 位的柱函数，
$j\ge m$ 时它准确作用为恒等；柱函数稠密、这些酉一致有界，
故 $E_j+E_j^*\to I$ 强。再用 (1.1) 的范数误差得到 (1.2)。

现在固定有限整数 $r\ge1$ 和任意闭的 $A^{(r)}$ 不变旗
$$
\mathcal N\subseteq\mathcal M\subseteq H^{(r)},\qquad
Q=\mathcal M\ominus\mathcal N.
$$
令
$$
T=P_QA^{(r)}|_Q,\qquad
T_j=\frac{T^{2^j}}{d_j}=P_QN_j^{(r)}|_Q.
\tag{1.3}
$$
压缩是该不变旗的代数商表示：在复合中删去的 $\mathcal N$ 分量仍被多项式送入 $\mathcal N$。
所以
$$
\|T_j\|\le1,\qquad \|T_j^2\|\le\eta_j,\qquad
T_j\xrightarrow{\mathrm{WOT}}\tfrac12I_Q,\qquad
T_j+T_j^*\xrightarrow{\mathrm{SOT}}I_Q.
\tag{1.4}
$$
最后一个等式只使用
$T_j^*=P_Q(N_j^*)^{(r)}|_Q$；
没有要求 $\mathcal M,\mathcal N$ 被原伴随保持。
归一化分母始终是原 $d_j$，不替换为未知限制的幂范数。

## 2. 紧夹积的准确范数极限

**定理 2.1。** 对每个紧算子 $K\in\mathcal K(Q)$，
$$
\boxed{\lim_{j\to\infty}\|T_jKT_j\|=\frac12\|K\|.}
\tag{2.1}
$$

先由 (1.4) 得到两个实际逐向量估计：
$$
T_j^*T_j-T_j^*
=T_j^*(T_j+T_j^*-I)-(T_j^*)^2,
$$
$$
T_jT_j^*-T_j
=T_j(T_j+T_j^*-I)-T_j^2.
\tag{2.2}
$$
右边作用于每个固定向量都趋零；因此
$$
T_j^*T_j\xrightarrow{\mathrm{WOT}}\tfrac12I_Q,\qquad
T_jT_j^*\xrightarrow{\mathrm{WOT}}\tfrac12I_Q.
\tag{2.3}
$$
这里没有把两个变化的 WOT 极限直接相乘。

若 $K$ 为非零有限秩，取奇异值分解
$$
K=U\Sigma V^*,
$$
其中 $U,V:\mathbb C^s\to Q$ 为等距嵌入，
$\Sigma$ 为非负对角矩阵。令
$$
A_j=T_jU,\qquad B_j=T_j^*V.
$$
由 (2.3) 及有限维性，
$$
A_j^*A_j\longrightarrow\tfrac12I_s,\qquad
B_j^*B_j\longrightarrow\tfrac12I_s
\quad\text{于算子范数}.
\tag{2.4}
$$
充分大 $j$ 时两矩阵严格正，极分解可写成
$$
A_j=\widetilde U_j(A_j^*A_j)^{1/2},\qquad
B_j=\widetilde V_j(B_j^*B_j)^{1/2},
$$
$\widetilde U_j,\widetilde V_j$ 仍为等距嵌入。于是准确有
$$
\begin{aligned}
\|T_jKT_j\|
&=\|A_j\Sigma B_j^*\|\\
&=\|(A_j^*A_j)^{1/2}\Sigma(B_j^*B_j)^{1/2}\|
\longrightarrow\tfrac12\|\Sigma\|=\tfrac12\|K\|.
\end{aligned}
\tag{2.5}
$$

一般紧 $K$ 取有限秩 $K_\nu\to K$ 于范数。
由 $\|T_j\|\le1$，
$$
\big|\|T_jKT_j\|-\|T_jK_\nu T_j\|\big|\le\|K-K_\nu\|.
$$
先取 $j$ 的上下极限，再令 $\nu\to\infty$，得到 (2.1)。
这也覆盖 $K=0$。

## 3. 任意有界回传算子的代价与近似缺陷

设 $K$ 紧，$\{X_j\}$ 为任意逐项有界算子，
**不要求整个序列一致有界**。置
$$
\delta_j=\|KT_j-T_jX_j\|,\qquad
\delta'_j=\|T_jK-X_jT_j\|.
$$
分别从
$$
T_jKT_j=T_j(KT_j-T_jX_j)+T_j^2X_j
$$
和
$$
T_jKT_j=(T_jK-X_jT_j)T_j+X_jT_j^2
$$
得到
$$
\boxed{
\frac12\|K\|
\le\liminf_j\bigl(\delta_j+\eta_j\|X_j\|\bigr),\qquad
\frac12\|K\|
\le\liminf_j\bigl(\delta'_j+\eta_j\|X_j\|\bigr).
}
\tag{3.1}
$$
这是两条独立的估计，不要求两个回传等式同时成立。

因此：

- 若 $KT_j=T_jX_j$ 对每个 $j$ 成立，或者
  $T_jK=X_jT_j$ 对每个 $j$ 成立，则
  $$
  \liminf_j\eta_j\|X_j\|\ge\frac12\|K\|.
  \tag{3.2}
  $$
- 若 $\sup_j\|X_j\|<\infty$，则相应近似缺陷的下极限至少为 $\|K\|/2$。
  尤其非零紧 $K$ 不可能有范数趋零缺陷的一致有界 dyadic 回传族。

这些估计只使用实际算子乘积；没有对 $T_j$ 或未知限制取有界逆。

## 4. 紧起点的完整后退链必有四次指数增长

设 $J_0\ne0$ 紧，并有逐项有界算子 $J_n\in\mathcal B(Q)$，
满足以下任一完整链：
$$
J_{n-1}T=TJ_n\quad(n\ge1),
\tag{4.1a}
$$
或
$$
TJ_{n-1}=J_nT\quad(n\ge1).
\tag{4.1b}
$$
归纳分别得到
$$
J_0T^n=T^nJ_n,\qquad\text{或}\qquad T^nJ_0=J_nT^n.
$$
取 $n=2^j$ 并除原 $d_j$，可在 (3.2) 取
$K=J_0,X_j=J_{2^j}$。故
$$
\boxed{\liminf_{j\to\infty}\eta_j\|J_{2^j}\|
\ge\frac12\|J_0\|.}
\tag{4.2}
$$
等价地，在 dyadic 子序列 $n=2^j$ 上，
$$
\boxed{
\|J_n\|\ge
\left(\frac12\|J_0\|-o(1)\right)
\exp(1400n^4-630n^3+300n).
}
\tag{4.3}
$$
$o(1)$ 随该子序列趋零。没有把此下界宣称为所有整数 $n$ 的下界。

特别，不存在非零紧起点的一致有界完整链。
取常值链 $J_n=K$，也重新得到任意实际有限放大旗子商的交换子中无非零紧算子；
原空间与不变限制的相应定性结论已属于 R12。

### 4.1 非紧起点的一个本质范数比较

对不要求紧的 $J_0$，若 (4.1) 的某个方向成立且
$$
\liminf_j\eta_j\|J_{2^j}\|=0,
\tag{4.4}
$$
则
$$
\boxed{\|J_0\|\le3\|J_0\|_{\rm ess}.}
\tag{4.5}
$$
这里本质范数在 $\mathcal B(Q)/\mathcal K(Q)$ 中计算。
证明：任取紧 $K$，以完整链的 $X_j=J_{2^j}$ 代入 (3.1)，
相应缺陷不超过 $\|K-J_0\|$。
沿 (4.4) 的子序列得到
$\|K\|/2\le\|K-J_0\|$。
再用 $\|K\|\ge\|J_0\|-\|K-J_0\|$，
并对紧 $K$ 取下确界，即得 (4.5)。
常数3只是这条估计给出的常数，不声称最优。

## 5. 文献判据的准确适用性

Ciprian Foiaş、Il Bong Jung、Eungil Ko、Carl Pearcy，
*On quasinilpotent operators, II*，
**J. Austral. Math. Soc. 77 (2004), 349–356**，
[正式全文 PDF](https://www.austms.org.au/Publ/JAustMS/V77P3/pdf/l57.pdf)。

该文 Corollary 3.4（pp.352–353）使用一个一致有界的回传链，
起点为非零紧算子，推出超不变子空间。
(4.2) 准确排除了当前实际模型及上述有限放大旗子商满足这种假设的可能性；
它加强的是 R12 的紧交换子障碍，不能据此否定其他不变子空间路线。

同文 Theorem 3.7（pp.354–355）要求沿**所有正整数 $n$** 的归一化幂乘有界算子序列有非零弱极限。
R12 的 $A^{2^j}/\|A^{2^j}\|\to I/2$ 只有 dyadic 子序列，
不满足这个量词。不能把该定理套在 dyadic 弱极限上。
这里重核的是假设，没有把文献结论改写为子序列版本。

## 6. 剩余边界

本稿没有把任意拟仿射或外部紧交织化为 (4.1)，
没有构造本题正常正见证所需的紧回传起点，
也未证明普通不变子空间存在或不存在。
新的可用接口是 (2.1)、(3.1) 和带实际 $\eta_j$ 的 (4.2)；
若后续路线产生这样的链，必须支付这里的范数增长或近似缺陷。
