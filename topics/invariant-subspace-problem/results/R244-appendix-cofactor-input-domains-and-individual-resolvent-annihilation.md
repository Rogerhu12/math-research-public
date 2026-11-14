# R244 后续附录：指定正矩中的单个预解因子消去

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：完整证明的中间结论。共同预解乘积可在指定有限组配对输入上删去任意一个因子。秩二时，每个单独分母的整个有界交换子理想都被原正态湮灭。本文不把这些指定输入域提升为全域正则化，也不把 $f_i$ 的域换成 $Cf_i$ 的域。

## 1. 已付的原算子数据

记 $\mathfrak C=A'$，$B(x,y)=\langle x,Cy\rangle$，内积对第一变量线性。沿用实际 Haar 模型的全部有界交换子 $C$ 对称性及原最小闭乘子。
取
$$
\rho=\sum_{i=1}^r f_i\otimes f_i\ge0,\qquad
\tau=\sum_i\|f_i\|^2>0,\qquad
M_i=X_{Cf_i},\qquad M_i1=Cf_i.
$$
设全空间单射 $S\in\mathfrak C$ 满足
$$
\phi_\rho(SF)=0\quad(F\in\mathcal A).
$$
正常性及 R88 的有界强多项式逼近将此式延伸到全部 $F\in\mathfrak C$。

假设每个 $M_i$ 都有已核的广义预解数据
$$
L_i=M_iU_i+F_i,\quad U_i\in\mathfrak C^\times,\quad F_i\in\mathfrak C,
\quad \lambda_i\in\rho(L_i).
$$
写
$$
R_i=(L_i-\lambda_i I)^{-1},\quad B_i=F_i-\lambda_i I,\quad
D_i=M_iR_i=U_i^{-1}(I-B_iR_i)\in\mathfrak C.
\tag{1.1}
$$
[广义预解附录](R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)给出真实最大商公式
$$
\boxed{
\operatorname{Dom}M_i=\{x:D_ix\in\operatorname{Ran}R_i\},
\qquad M_ix=R_i^{-1}D_ix.
}
\tag{1.2}
$$
这里的 $M_i$ 仍是原最小闭乘子；(1.2) 是由
$U_iD_i+B_iR_i=I$ 和真实逆等式证明的结论，不是另取最大扩张。

置
$$
R=\prod_{k=1}^rR_k,\qquad
P_i=\prod_{k\ne i}R_k.
$$
空乘积约定为 $I$。$RH$ 实际落入每个 $\operatorname{Dom}M_i$，且
$M_iR=D_iP_i$ 有界。R244 的指定配对恒等式及 $S$ 的全空间单射性因此给
$$
\boxed{h=\sum_{i=1}^rD_iP_i f_i=0.}
\tag{1.3}
$$

## 2. 删去一个因子仍支付每个指定输入

**定理。** 对每个 $i$，都有
$$
P_if_j\in\operatorname{Dom}M_j\quad(1\le j\le r),
\qquad
\boxed{\sum_{j=1}^rM_jP_if_j=0.}
\tag{2.1}
$$
所以
$$
\boxed{\phi_\rho(P_iF)=0\quad(F\in\mathfrak C,\ 1\le i\le r).}
\tag{2.2}
$$

**证明。** 固定 $i$。对 $j\ne i$，$P_i$ 含有因子 $R_j$，故
$$
M_jP_if_j=D_jP_{ij}f_j,\qquad
P_{ij}=\prod_{k\ne i,j}R_k.
\tag{2.3}
$$
(2.3) 是全域有界乘子作用；其指定输入当然在原最小域中。

唯一尚未支付的是 $P_if_i$。从 (1.3) 移项，并用 $P_j=R_iP_{ij}$，
$$
D_iP_if_i
=-\sum_{j\ne i}D_jR_iP_{ij}f_j
=R_i\left(-\sum_{j\ne i}D_jP_{ij}f_j\right).
\tag{2.4}
$$
括号是有限个真正 $H$ 向量的和。由 (1.2)，(2.4) 准确给
$$
P_if_i\in\operatorname{Dom}M_i,\qquad
M_iP_if_i=-\sum_{j\ne i}D_jP_{ij}f_j.
\tag{2.5}
$$
与 (2.3) 相加便得 (2.1)。

R244 的指定配对公式只要求这些有限输入已属于相应域：
$$
\phi_\rho(P_iF)
=B\left(F\sum_jM_jP_if_j,1\right).
$$
将 (2.1) 代入即证 (2.2)。全程未要求
$P_iH\subseteq\bigcap_j\operatorname{Dom}M_j$。证毕。

因此同一个原正泛函湮灭有界交换子理想
$$
\mathcal I_{r-1}=\sum_{i=1}^rP_i\mathfrak C.
\tag{2.6}
$$
也湮灭其强算子拓扑闭包：$\phi_\rho$ 是有限个向量泛函之和，故强连续。
因为 $\phi_\rho(I)=\tau>0$，该闭包不能含 $I$。
这只是 (2.2) 的连续性后果，不另行假设有强主理想单位。

同一组最小乘子改用任何其他允许的广义预解数据时，各 $R_i'=R_iV_i$，其中 $V_i$ 是有界交换单位。因此 $P_i'\mathfrak C=P_i\mathfrak C$，整个 $\mathcal I_{r-1}$ 也不变。这是实际代数理想相等，不只闭包相同。

当 $r>2$ 时，本节得到的是所有 $r-1$ 个分母的产品。
再删去第二个因子后，会有两个乘子输入同时缺少各自分母；
(2.4) 已不能逐项给出它们的最大商域。因此本文不声称可以继续删到单个分母。

## 3. 秩二的交叉域与个别理想

若 $r=2$，(1.3) 为
$$
D_1R_2f_1+D_2R_1f_2=0.
$$
(2.4)--(2.5) 具体成为
$$
\boxed{
R_1f_2\in\operatorname{Dom}M_2,\qquad
M_2R_1f_2=-D_1f_1,
}
$$
$$
\boxed{
R_2f_1\in\operatorname{Dom}M_1,\qquad
M_1R_2f_1=-D_2f_2.
}
\tag{3.1}
$$
各自原本已付的输入为
$M_1R_1f_1=D_1f_1$、$M_2R_2f_2=D_2f_2$。
故
$$
\boxed{\phi_\rho(R_1F)=\phi_\rho(R_2F)=0\quad(F\in\mathfrak C).}
\tag{3.2}
$$
这严格加强了只记录 $\phi_\rho(R_1R_2F)=0$ 的结论。

广义预解附录已证明：同一 $M_i$ 的任意另一组允许数据给
$R_i'=R_iV_i$，其中 $V_i$ 是 $\mathfrak C$ 中的有界单位。
因此单个主理想 $R_i'\mathfrak C=R_i\mathfrak C$，
以及 (3.2) 都不随这些选择改变。

## 4. 在秩二有界链上的独立核验

沿用[秩二有界链附录](R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)
$$
d_0x=(R_2x,R_1x),\quad
d_1(y_1,y_2)=R_1y_1-R_2y_2,
$$
$$
N=\overline{\operatorname{Ran}d_0},\quad
K=\ker d_1,\quad Q=K\ominus N.
$$
所有 $\mathfrak C^{(2)}$ 保持旗子 $N\subset K$，故
$$
\pi(F)=P_QF^{(2)}|_Q
$$
是有界商表示。令
$$
g_i=(L_i-\lambda_i I)1,\qquad
z_i=D_i^*Cf_i,\qquad
q=P_Q(g_1,g_2),\quad z_Q=P_Q(z_1,z_2).
$$
有界链附录已逐项付域并证明 $g\in K$、$z\in N^\perp$。
真实逆等式还给 $D_ig_i=Cf_i$。因此，对全部 $F\in\mathfrak C$，
$$
\begin{aligned}
\langle F^{(2)}g,z\rangle
&=\sum_i\langle FD_ig_i,Cf_i\rangle\\
&=\sum_i\langle FCf_i,Cf_i\rangle
=\sum_i\langle Ff_i,f_i\rangle=\phi_\rho(F).
\end{aligned}
$$
末式用的是 $FC=CF^*$，不是 $F$ 自伴。
由旗子不变性及 $z\perp N$，遂有准确的商配对
$$
\boxed{\phi_\rho(F)=\langle\pi(F)q,z_Q\rangle.}
\tag{4.1}
$$
对于任意 $v=(v_1,v_2)\in K$，
$$
R_1^{(2)}v=d_0v_2,\qquad R_2^{(2)}v=d_0v_1,
$$
所以 $\pi(R_1)=\pi(R_2)=0$；将它们代入 (4.1)，再得 (3.2)。

本文不据 (4.1) 声称 $F\mapsto\langle\pi(F)q,z_Q\rangle$
已由 $Q$ 上的一个正密度表示。原 $\phi_\rho$ 在 $B(H)$ 上为正，
而 (4.1) 当前只是两个指定向量的配对。

## 5. 正真空锚尚缺什么

(3.1) 中的输入是 $R_1f_2$ 和 $R_2f_1$，不是 $Cf_1$ 或 $Cf_2$。
所以没有由此证明
$$
Cf_1\in\operatorname{Dom}M_2,\qquad
Cf_2\in\operatorname{Dom}M_1,
$$
也没有证明 $1\in R_1R_2H$ 或共同最小图等于各最大域的交图。
前者若成立，会由既有正真空锚排除见证；目前不能从 (3.1) 移除或反射分母。

在秩一，$P_1=I$，(2.2) 立即与 $\phi_\rho(I)>0$ 矛盾，
与前附录已证明的全部广义扰动空预解结论一致。
本稿新增的是高秩指定配对中的一个因子消去及秩二个别理想转移，
不是普通 Hilbert ISP 的完成。
