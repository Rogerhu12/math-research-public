# 原 Walsh 稳定图域的真实整数迹、均方采样与单条边界链

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 本文使用[统一中位间隙](R12-appendix-uniform-walsh-root-median-gap-and-trace-class-physical-polarization.md)、[准确双区间及完整 carry](R12-appendix-physical-median-two-intervals-and-actual-carry-range-rank-one-residue.md)和[同域双因子](R12-appendix-actual-haar-same-stable-domain-two-closed-factors.md)。新输入是同一原 Haar 尾在块根图域上的实际整数点迹及原 $H$ 范数恢复；这些不是 $H$ 上的有界点评价。随后辨明这个域与真正原交换图之间的严格边界。

## 1. 固定域与付清的物理小行

固定原 $C=A^{(m)}=D+K$，任意选择每个原 Walsh 块的平方根，取其最大直和 $R$。令
$$
\mathcal D=\operatorname{Dom}R,\qquad
E=(\mathcal D,\|x\|_E^2=\|x\|_H^2+\|Rx\|_H^2).
\tag{1}
$$
$E$ 是 Hilbert 空间，有限整块为其稠密核心；包含 $E\to H$ 有界、单射且稠值。
始终 $\Gamma R=\{(Rx,x):x\in\mathcal D\}$。
前稿给物理对角投影 $F=\operatorname{diag}(F^{(0)},F^{(1)})$，
$$
P_{\Gamma R}-F\in\mathfrak S_1,\qquad
\|P_{\Gamma R_j}-F_j\|\le\epsilon_j
:=\exp[-(16^m/12)8^j]\quad(j\ge20).
\tag{2}
$$
$F_j^{(1)}$ 的两个整数区间都不包含 $0\le k<2^{j-2}$。
因而若 $E_{j,n}$ 投到该块的前 $n\le2^{j-2}$ 个真实坐标，
$$
\boxed{\quad
\|E_{j,n}x_j\|_H\le\sqrt{\epsilon_j}\,\|x_j\|_E
\qquad(j\ge20).
\quad}
\tag{3}
$$
证明不是把大块范数删去：图投影下右块是
$G_j^2=(I+R_j^*R_j)^{-1}$。
$E_{j,n}F_j^{(1)}=0$ 和 (2) 给
$\|E_{j,n}G_j\|^2
=\|E_{j,n}G_j^2E_{j,n}\|\le\epsilon_j$；
再以 $x_j=G_jz_j$、$\|z_j\|=\|x_j\|_E$ 返回原域。
以下只用这个实际图范数小行。

## 2. 所有非负整数的实际连续迹

把非负整数 $k$ 看作最终为零的原二进制点。
对有限柱函数，其准确求值是
$$
\ell_k(x)=\Omega^*x+
\sum_{j\ge0}2^{j/2}(-1)^{\operatorname{bit}_j(k)}
q_{j,k\bmod 2^j}^*x.
\tag{4}
$$
对一般 $x\in E$，(4) 在 $E^*$ 中收敛，定义真实连续泛函。
具体地，取
$$
J(k)=\max\{20,\lceil\log_2(k+1)\rceil+2\}.
$$
$j\ge J(k)$ 时 $k<2^{j-2}$，故 (3) 控制其全部尾。
不同 $Q_jE$ 图正交，因而
$$
\|\ell_k\|_{E^*}^2
\le2^{J(k)}+\sum_{j\ge J(k)}2^j\epsilon_j
\le2^{20}+8(k+1)+1.
\tag{5}
$$
末尾使用 $j\ge20$ 时 $\epsilon_j\le2^{-4j}$。
这也支付了 $k=0$ 项，而非省略常数块。

特别
$$
\ell_0=\Omega^*+\sum_{j\ge0}2^{j/2}u_j^*
\quad\text{作为 }E\text{ 上的连续行}.
\tag{6}
$$
右边通常不是 $H$ 上的有界行。本稿并未把一个 $L^2$ 等价类免费指定为处处有值的函数；值由有限整块图核心的唯一连续延拓定义。

## 3. 真实 dyadic 均方采样返回原范数

记 $P_L=Q_{-1}+\sum_{j<L}Q_j$ 为原前 $L$ 位柱投影，
并置
$$
\mathcal S_Lx=(2^{-L/2}\ell_kx)_{0\le k<2^L}.
$$
$P_Lx$ 是原有限柱函数，故
$\|\mathcal S_LP_Lx\|_{\ell^2}=\|P_Lx\|_H$。
对 $j\ge L$，其对 $\mathcal S_L$ 的准确贡献为
$$
2^{(j-L)/2}(q_{j,k}^*x)_{0\le k<2^L};
\tag{7}
$$
此时 $k<2^L$ 使第 $j$ 位符号全为正。

$j=L,L+1$ 的原规范分别为 $1,\sqrt2$。
$j\ge L+2$ 时用 (3)，再对整块尾作 Cauchy--Schwarz，得到
$$
\begin{aligned}
\|\mathcal S_Lx-\mathcal S_LP_Lx\|
&\le
\left(3+\sum_{j\ge L+2}2^{j-L}\epsilon_j\right)^{1/2}
\left(\sum_{j\ge L}\|Q_jx\|_E^2\right)^{1/2}\\
&\le2\left(\sum_{j\ge L}\|Q_jx\|_E^2\right)^{1/2},
\qquad L\ge20.
\end{aligned}
\tag{8}
$$
这里同时保留了紧邻的两块；不能把它们套进更小的远尾估计。

右端对每个同一 $x\in E$ 趋于零。所以
$$
\boxed{\quad
\lim_{L\to\infty}2^{-L}\sum_{k=0}^{2^L-1}|\ell_kx|^2
=\|x\|_H^2.
\quad}
\tag{9}
$$
极化还给全部 $x,y\in E$ 的原内积恢复。
特别 $\{\ell_k:k\ge0\}$ 分离 $E$：若所有迹为零，则 $x=0$。
(8) 是原域的来源预算，不是仅在有限柱上知道的等分布再无条件延拓。

## 4. 同一原算子的准确边界递推

由同域双因子稿，$C\mathcal D\subset\mathcal D$。
把 $C$ 看作 $C_E:E\to E$；它由闭图定理有界：
$E$ 收敛给 $H$ 收敛，$C$ 在 $H$ 上有界，足以核其 $E$ 图闭。

原径向权函数在整数 $k\ge1$ 等于 $a_{v_2(k)}$，
在二进制点 $0$ 为零；它连续，因为 $a_j\to0$。
因此对于有限柱函数，原前向移位给
$$
\ell_0C_E=0,\qquad
\ell_k C_E=a_{v_2(k)}\ell_{k-1}\quad(k\ge1).
\tag{10}
$$
这里的目标 $Cp$ 虽未必是有限柱函数，却是连续函数且在 $\mathcal D$ 中；
其有限柱条件期望在 $E$ 中图收敛、在原连续函数范数中一致收敛，
故 (4) 确实返回同一原点值。
再用 $C_E,\ell_k$ 的有界性与有限整块图核心，把 (10) 延到全部 $E$。
这支付了原算子、原点值、原权以及同一来源，未换到负整数边界 Hilbert 模型。

## 5. 原图空间中恰好一条稠密广义核链

沿用双因子稿的 $S,T,\mathcal U,\mathcal V$。
它们保持 $\mathcal D$，故相应作用在 $E$ 上有界。
该稿已给
$$
T\Omega=0,\qquad
TS=C_E,\qquad
\operatorname{Ran}_E S=\operatorname{Ran}_E T.
\tag{11}
$$
其中 $T=R-\gamma P_0+\Omega\eta$，
$\eta|_{Q_jH}=-2^{j/2}u_j^*R_j$。
所以 $\ell_0T=0$，且
$$
\boxed{\quad
\overline{\operatorname{Ran}_E T}
=\overline{\operatorname{Ran}_E S}
=\ker\ell_0.
\quad}
\tag{12}
$$
为核反向稠密性，先取有限整块目标
$w=d\Omega+\sum_jw_j$ 且 $\ell_0w=0$。
在这些有限块取 $x_j=R_j^{-1}w_j$、常数源为零。
则 $Tx$ 的尾准确为 $w_j$，常数坐标是
$-\sum_j2^{j/2}u_j^*w_j=d$，故 $Tx=w$。
任意 $w\in\ker\ell_0$ 以有限整块截断后减去其 $\ell_0$ 值乘 $\Omega$，
就在 $E$ 中由此类目标逼近。

又 $\ell_0\Omega=1$ 且 $T\Omega=0$，
所以 $T(\ker\ell_0)=T(E)$。
结合 (11)--(12) 和 $T_E$ 有界，
$$
\boxed{\quad
\overline{\operatorname{Ran}C_E}=\ker\ell_0.
\quad}
\tag{13}
$$
这是 $E$ 图范数中的闭包；原 $H$ 中的 $C$ 仍为稠值。

令 $h_k\in E$ 为 $\ell_k$ 的 Riesz 向量。
由 (10)、(13)，
$$
C_E^*h_0=0,\qquad
C_E^*h_k=a_{v_2(k)}h_{k-1},\qquad
\ker C_E^*=\mathbb Ch_0.
\tag{14}
$$
每个 $h_k$ 非零；有限柱插值或 (10) 递推都给它们的有限线性独立。
单核维数为一使每一步广义核维数至多增加一；
(14) 又提供完整的长链。因此
$$
\boxed{\quad
\ker(C_E^*)^n=\operatorname{span}\{h_0,\ldots,h_{n-1}\},
\quad \dim\ker(C_E^*)^n=n,
\quad
\overline{\bigcup_n\ker(C_E^*)^n}=E.
\quad}
\tag{15}
$$
末一式由 (9) 的分离性，而非形式矩阵完备性得到。

特别 $C_E$ 没有有界平方根。
若 $B^2=C_E$，则 $\dim\ker(B^*)^2=1$，
迫 $\ker(B^*)^2=\ker B^*$；
这个核稳定后全部幂的核相同，
却与 $\dim\ker(B^*)^4=\dim\ker(C_E^*)^2=2$ 矛盾。
故原 $C$ 没有恰以 $\mathcal D$ 为定义域的闭稳定平方根：
这样的根在 $E$ 上由闭图定理成为被排除的有界平方根。

## 6. 物理半分布与更一般的真实入域边界

令 $U_j=M_{\chi_j}$ 为原第 $j$ 位字符乘法。
它们是自伴酉，$U_j\to0$ 弱。
准确双区间对每个固定低位柱函数 $f$ 给
$$
\|F^{(\nu)}U_jf\|^2\longrightarrow\tfrac12\|f\|^2,\qquad
\nu=0,1.
\tag{16}
$$
确实，$U_jf$ 仅在 $Q_j$ 中，且坐标平方是低位周期 $|f(k)|^2/2^j$。
每个区间在每个固定余类中的计数误差至多一，
两区间总长度为 $2^{j-1}+O(1)$。
随后以投影一致有界延到全部固定 $f\in H$。
同样有 $(I-F^{(\nu)})$ 的半分布。

现设 $A\in B(H)$ 满足 $[A,U_j]\to0$ 强。
则
$$
\boxed{\quad A(H)\subset\mathcal D\quad\Longrightarrow\quad A=0.\quad}
\tag{17}
$$
入域假设与 $R$ 闭性给全域有界 $RA$。
对固定 $\xi$，真实图列
$$
g_j=(RAU_j\xi,AU_j\xi)\in\Gamma R
$$
有界且弱零。
由 (2) 的紧差，
$(I-F)g_j=(P_{\Gamma R}-F)g_j\to0$。
其第二分量给 $(I-F^{(1)})AU_j\xi\to0$。
而 $AU_j\xi-U_jA\xi\to0$；
(16) 于是迫 $\|A\xi\|^2/2=0$，证毕。
这一步先取真正图列，不把投影近似当作自动入域。

(17) 有以下实际应用：

- 每个 $A\in\{C\}'$ 都满足所需强交换。由原归一化幂
  $N_j\to E_j$ 于算子范数、$E_j-\Pi_{\{y_j=1\}}\to0$ 强，
  $[A,N_j]=0$ 直接给 $[A,U_j]\to0$ 强。
  因而不存在非零原交换子使 $AH\subset\mathcal D$。
- 每个闭原 $C$ 不变子空间的投影满足该强交换，
  这是 [R178 §2--3](R178-high-order-gauge-commutation-and-kernel-angle-degeneration.md)
  的两侧真实 pattern 结论。因此 $\mathcal D$ 不包含任何非零闭原 $C$ 不变子空间。
- 更一般地，若一个闭算子 $Z$ 的图被 $C\oplus C$ 保持，
  且 $\operatorname{Dom}Z\subset\mathcal D$，则其定义域只能为零。
  令 $P$ 为图投影；有限放大的同一 R178 证明给
  $[P_{22},U_j]\to0$ 强。
  正平方根 $A=P_{22}^{1/2}$ 也强渐近交换（先多项式，再一致逼近），
  而极分解的真实像身份给
  $\operatorname{Ran}A=\operatorname{Ran}(\pi_2|_{\Gamma Z})
  =\operatorname{Dom}Z$。
  用 (17) 得 $P_{22}=0$，再由算子图没有非零垂直向量得 $\Gamma Z=0$。

最后一项包括任何稠密闭稳定原平方根，
故其定义域不可能包含于此处任一分支的 $\mathcal D$。
它不限于 $R$ 的有界扰动，也没有假设 Julia 角有界。
同域双因子 $S,T$ 不与原 $C$ 交换，其图不满足这里的模保持前提，故不发生矛盾。

## 7. 保持的完成边界

本文支付的是原全尾、同一个已构造图域的实际整数迹、原均方范数、
完整 adjoint 单链及严格入域边界。
$E$ 中的闭包、核和稠密性均按其图范数理解；
不能把 $E$ 的一个真闭不变子空间在 $H$ 中的像闭包自动认作真子空间。
(4) 也不成为 $H$ 上的有界评价或未经证明的闭边界交织。

域排除不等于原 $C$ 无闭根。
它没有把任意未知旗子商等同于本篇全尾，
也没有排除不同的真实闭域、场外二次分子或其它原普通不变子空间来源。
下一来源必须保留这种域和拓扑的区别。
