# R12 补充：原 Walsh 根图与全部原不变投影的最大本质距离

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

本篇使用 [R178 的真实固定宽高位 pattern](R178-high-order-gauge-commutation-and-kernel-angle-degeneration.md) §2–3，补上中位物理旗的联合交换来源。新结果不是把弱极限相乘，也不要求未知投影属于原交换子。

## 1. 对象与结论

沿用[原 Walsh 全块表示](R12-appendix-actual-walsh-block-trace-class-carry-and-closed-diagonal-roots.md)：
$$
C=A^{(m_0)}=D+K,\qquad
H=Q_{-1}H\oplus\bigoplus_{j\ge0}Q_jH,
$$
$$
q_{j,k}=e_k^{(j)}\otimes\chi_j\otimes\Omega_{>j},
\qquad 0\le k<2^j.
$$
这里 $C$ 是原 Haar 尾；$D_j=Q_jCQ_j$ 是长度 $2^j$ 的完整原加权循环，闭合系数 $-\mu_j$。每个块任意选平方根 $R_j^2=D_j$，令 $R=\bigoplus R_j$ 取已付的最大直和闭域，并记
$$
\Pi=P_{\Gamma R},\qquad
\Gamma R=\{(Rx,x):x\in\mathcal D(R)\}.
$$
根分支完全任意，以下结论对全部选择成立。

**定理。** 对每个闭 $(C\oplus C)$ 不变子空间的正交投影 $P$，
$$
\boxed{\|\Pi-P\|_{\rm ess}=\|\Pi-P\|=1.}
\tag{1.1}
$$
更准确地，令 $L=P-\Pi$。若 $P\ne0$，则 $+1$ 有实际单位弱零近似特征列；若 $P\ne I$，则 $-1$ 有这样的列。因此在相应条件下
$$
+1\in\sigma_{\rm ess}(L),\qquad -1\in\sigma_{\rm ess}(L).
\tag{1.2}
$$

在同一 $R$ 的真实 Julia 坐标中，[原完整 Riccati 方程](R12-appendix-actual-walsh-graph-coordinates-and-small-trace-class-angle-solution.md) 没有任何有界解 $Z:H\to H$。这包括任意大范数、非紧的有界图角，并不排除在这个坐标中具有非全域或无界图角的其他原闭根。

## 2. 保全部分支的真实半旗逼近

令
$$
U_j=M_{\chi_j}\oplus M_{\chi_j}.
$$
$U_j$ 是自伴酉算子，并且 $U_j\to0$ 于弱算子拓扑。

先把负闭合块与[全部有限头根图定理](R12-appendix-all-finite-haar-head-root-graphs-half-weak-limit-and-strong-zero.md)的正闭合有限头作精确对应。写 $N=2^j$，
$$
C_j^+=J_j^{\rm head}+\mu_jE_j^{\rm head},\qquad
D_j^-=J_j^{\rm head}-\mu_jE_j^{\rm head},\qquad
W_je_k=e^{i\pi k/N}e_k.
$$
逐列恒等式为
$$
D_j^-=e^{-i\pi/N}W_jC_j^+W_j^*.
\tag{2.1}
$$
故 $S_j=e^{i\pi/(2N)}W_j^*R_jW_j$ 满足 $S_j^2=C_j^+$，且两根图之间的酉矩阵为
$$
\mathcal W_j=\operatorname{diag}
(e^{-i\pi/(2N)}W_j,W_j).
$$

原有限头定理 §3–4 给分支无关的物理对角中位半旗 $F_j$、中位带 $T_j$ 和 $\eta_j\to0$。其完整有限行列估计是
$$
\|(\Pi_j^+-F_j)v\|
\le\sqrt2\,\eta_j\|v\|+2\|T_jv\|.
\tag{2.2}
$$
该估计对有限前缀中的每个 $v$ 都成立。$\mathcal W_j$ 与 $F_j,T_j$ 精确交换，所以把 $v=\mathcal W_j^*\xi$ 代入，保留同一范数预算，得到负闭合块的
$$
\|(\Pi_j^--F_j)\xi\|
\le\sqrt2\,\eta_j\|\xi\|+2\|T_j\xi\|.
\tag{2.3}
$$
这一步不把强收敛直接作用到移动相位向量。

对固定低柱向量 $\xi$，$U_j\xi$ 落在第 $j$ 个 Walsh 块，而且
$$
U_j\Pi U_j\xi=\Pi_j^-\xi.
$$
原中位带估计给 $\|T_j\xi\|\to0$。由柱函数稠密性和一致有界性，得到对每个固定 $\xi\in H\oplus H$：
$$
\boxed{\|\Pi U_j\xi-U_jF_j\xi\|\longrightarrow0.}
\tag{2.4}
$$
原文同时已付
$$
F_j\xrightarrow{\rm WOT}\tfrac12I.
\tag{2.5}
$$
$F_j$ 在两个物理分量上可以不同；以下不将它事先改成相同的最高位事件。

## 3. 任意普通不变投影的真实多位来源

固定闭 $(C\oplus C)$ 不变投影 $P$。对固定有限位集合 $J$ 和 pattern $\sigma$，令
$$
M_{J,\sigma}
=M_{\mathbf1_{\{y_k=\sigma_k,\ k\in J\}}}\oplus
 M_{\mathbf1_{\{y_k=\sigma_k,\ k\in J\}}}.
$$
原尾归一幂满足
$$
N_k=C^{2^k}/d_k=E_k+\eta_kE_k^*N_{k+1},
\qquad \|N_k\|=1,\qquad \eta_k\to0.
$$
对原尾起点 $m_0$，使用其自身的 $d_k,\eta_k$；原 carry 估计仍趋零。

取真实多项式的二重放大
$$
A_{J,\sigma}
=\left(
\prod_{\sigma_k=1}N_k\prod_{\sigma_k=0}(I-N_k)
\right)\oplus
\left(
\prod_{\sigma_k=1}N_k\prod_{\sigma_k=0}(I-N_k)
\right).
$$
R178 §2 的柱函数计算和固定有限乘积误差给
$$
A_{J,\sigma}-M_{J,\sigma}\to0\ {\rm 强},
\qquad
A_{J,\bar\sigma}^*-M_{J,\sigma}\to0\ {\rm 强}
\tag{3.1}
$$
当 $|J|$ 固定、$\min J\to\infty$ 时成立。这里 $\bar\sigma$ 必须为互补 pattern。

这些 $A_{J,\sigma}$ 都是 $C\oplus C$ 的实际多项式，所以保持同一个未知子空间：
$$
(I-P)A_{J,\sigma}P=0,\qquad
PA_{J,\bar\sigma}^*(I-P)=0.
$$
分别以 (3.1) 替换两角，得到
$$
\boxed{[P,M_{J,\sigma}]\to0\ {\rm 强*}.}
\tag{3.2}
$$
伴随收敛也由 $P,M_{J,\sigma}$ 自伴直接得到。此证明适用于任意普通不变 $P$，既没有假设 $PC=CP$，也没有要求其子空间是两个原不变空间的直和。

特别，单高位给
$$
[P,U_j]\to0\ {\rm 强*}.
\tag{3.3}
$$
下面仍须另付涉及 $F_j$ 的联合来源，不能直接把 (3.3) 右乘移动向量。

## 4. 中位旗的固定宽截断与两次极限

令
$$
a_\ell=2^{-\ell}-16^{-\ell},\qquad
X=\sum_{\ell\ge1}(B_\ell-\tfrac12)a_\ell
$$
其中 $B_\ell$ 是公平独立 Bernoulli 变量。原有限头定理 §3 已证明 $X$ 对称且无原子。

对 $k=\sum_{r<j}b_r2^r$，原 balance 权的两个分量一致满足
$$
Y_{j,\varepsilon}(k)
:=\frac{\log w_{2k+\varepsilon}-h_j}{100\,16^{m_0+j}}
=\sum_{\ell=1}^j(b_{j-\ell}-\tfrac12)a_\ell
+e_{j,\varepsilon}(k),\qquad
|e_{j,\varepsilon}(k)|\le c_{m_0}2^{-j}.
\tag{4.1}
$$
$F_j$ 选择 $Y_{j,\varepsilon}>0$ 的坐标，负值坐标不选；零值按原成对中位约定选择。

固定宽度 $s\ge1$，定义
$$
X_{j,s}=\sum_{\ell=1}^s(b_{j-\ell}-\tfrac12)a_\ell,\qquad
F_{j,s}=M_{\mathbf1_{\{X_{j,s}>0\}}}\oplus
M_{\mathbf1_{\{X_{j,s}>0\}}}.
$$
因
$$
\tfrac12\sum_{\ell>s}a_\ell<2^{-s-1},
$$
对每个固定 $s$ 及充分大的 $j$，两分量的 $F_j$ 与 $F_{j,s}$ 只可能在事件
$$
|X_{j,s}|\le2^{-s}
\tag{4.2}
$$
上不同。该事件只依赖 $\{j-s,\ldots,j-1\}$ 的高位。把同一有限 Bernoulli 和补上无限尾，(4.2) 的概率不超过
$$
p_s:=\Pr(|X|\le2^{1-s})\longrightarrow0.
\tag{4.3}
$$
无原子性在此支付 $s\to\infty$ 的最后一步。

对固定低柱向量，事件 (4.2) 与低柱独立；再由柱函数稠密及 $\|F_j-F_{j,s}\|\le1$，得到对每个固定 $\xi$：
$$
\limsup_{j\to\infty}
\|(F_j-F_{j,s})\xi\|
\le\sqrt{p_s}\,\|\xi\|.
\tag{4.4}
$$

对固定 $s$，$F_{j,s}$ 是 $s$ 位 pattern 的有限线性组合，故 (3.2) 给 $[P,F_{j,s}]\to0$。同样重要的是，$U_jF_{j,s}$ 是 **$s+1$ 位**集合
$\{j-s,\ldots,j\}$ 的 pattern 有限线性组合，所以也直接有
$$
[P,U_jF_{j,s}]\to0\ {\rm 强*}.
\tag{4.5}
$$
这不是两个单独强极限的乘积。

$U_j,F_j,F_{j,s}$ 都是物理乘法，因此精确交换。对固定 $\xi$，
$$
\|[P,U_j(F_j-F_{j,s})]\xi\|
\le \|(F_j-F_{j,s})\xi\|
+\|(F_j-F_{j,s})P\xi\|.
\tag{4.6}
$$
先取 $j\to\infty$，再取 $s\to\infty$，由 (4.3)–(4.6) 得到
$$
\boxed{
[P,F_j]\to0,\qquad [P,U_jF_j]\to0
\quad{\rm 强*}.
}
\tag{4.7}
$$
第二个伴随结论也可直接用 $U_jF_j$ 自伴。这是固定向量上的两次极限，没有给未知子空间单位球上的统一速度，也没有选增长宽度来替代证明。

## 5. 两个真实范数极限与最大本质距离

令 $L=P-\Pi$。由 (2.4)、(3.3)，对固定 $\xi$，
$$
LU_j\xi-U_j(P-F_j)\xi\longrightarrow0.
\tag{5.1}
$$
利用 $F_j^2=F_j$ 及 (2.5)，准确平方展开给
$$
\begin{aligned}
\|(P-F_j)\xi\|^2
&=\|P\xi\|^2+\langle F_j\xi,\xi\rangle
-2\operatorname{Re}\langle P\xi,F_j\xi\rangle\\
&\longrightarrow\tfrac12\|\xi\|^2.
\end{aligned}
$$
所以
$$
\|LU_j\xi\|^2\longrightarrow\tfrac12\|\xi\|^2.
\tag{5.2}
$$

现在单独展开第二次作用：
$$
L^2=P+\Pi-P\Pi-\Pi P.
$$
其中
$$
\begin{aligned}
PU_j\xi&=U_jP\xi+o(1),\\
\Pi U_j\xi&=U_jF_j\xi+o(1),\\
P\Pi U_j\xi&=PU_jF_j\xi+o(1)
=U_jF_jP\xi+o(1),\\
\Pi PU_j\xi&=\Pi U_jP\xi+o(1)
=U_jF_jP\xi+o(1).
\end{aligned}
\tag{5.3}
$$
第三行使用已付的联合交换 (4.7)；第四行仅把 (2.4) 作用到固定的 $P\xi$。每个 $o(1)$ 都是范数误差，没有对一个弱极限再次相乘。于是
$$
L^2U_j\xi-
U_j\bigl(P\xi+F_j(I-2P)\xi\bigr)\longrightarrow0.
\tag{5.4}
$$
因 $I-2P$ 为酉算子，同一平方展开给
$$
\begin{aligned}
\|P\xi+F_j(I-2P)\xi\|^2
&\longrightarrow
\|P\xi\|^2+\tfrac12\|(I-2P)\xi\|^2
+\operatorname{Re}\langle P\xi,(I-2P)\xi\rangle\\
&=\tfrac12\|\xi\|^2.
\end{aligned}
\tag{5.5}
$$

固定任意单位 $\xi$。由 (5.2)，对充分大的 $j$ 可定义
$$
v_j=\frac{LU_j\xi}{\|LU_j\xi\|}.
$$
这是实际单位向量列。$U_j\xi\rightharpoonup0$、$L$ 有界及分母趋于 $1/\sqrt2$ 给 $v_j\rightharpoonup0$；而 (5.4)–(5.5) 给
$$
\|Lv_j\|\longrightarrow1.
\tag{5.6}
$$
每个紧算子杀掉此弱零列。故 $\|L\|_{\rm ess}\ge1$。两个正交投影之差总满足 $\|L\|\le1$，证明 (1.1)。

若选单位 $\xi\in\operatorname{Ran}P$，(5.1)、(5.4) 的两个主项都为 $U_j(I-F_j)\xi$，故 $(L-I)v_j\to0$。若选单位 $\xi\in\ker P$，两个主项分别为 $-U_jF_j\xi$ 和 $U_jF_j\xi$，故 $(L+I)v_j\to0$。这证明 (1.2)，并给实际弱零奇异列，而不只给谱半径估计。

## 6. 原完整非线性 Riccati 的有界图角类为空

沿用原真实有界 Julia 坐标
$$
G=(I+R^*R)^{-1/2},\quad
H_0=(I+RR^*)^{-1/2},\quad V=RG,\quad
\mathcal U=\begin{pmatrix}V&H_0\\G&-V^*\end{pmatrix}.
$$
$\mathcal U$ 为酉，且 $\Pi=\mathcal UP_0\mathcal U^*$，其中 $P_0=\operatorname{diag}(I,0)$。

对任意有界 $Z:H\to H$，令 $P_Z$ 为全域图 $\{(x,Zx):x\in H\}$ 的正交投影。精确图公式给
$$
(P_Z-P_0)^2
=\operatorname{diag}\left(
\frac{Z^*Z}{I+Z^*Z},\frac{ZZ^*}{I+ZZ^*}
\right).
$$
因此
$$
\boxed{
\|P_Z-P_0\|_{\rm ess}
=\frac{\|Z\|_{\rm ess}}{\sqrt{1+\|Z\|_{\rm ess}^2}}
\le\frac{\|Z\|}{\sqrt{1+\|Z\|^2}}<1.
}
\tag{6.1}
$$
本质范数式由 Calkin 代数中的连续函数演算直接得到。

若 $Z$ 满足原文的完整 Riccati 方程，则
$\mathcal U\operatorname{Ran}P_Z$ 对原
$$
\mathcal B_C=\begin{pmatrix}0&C\\I&0\end{pmatrix}
$$
不变，故也对 $\mathcal B_C^2=C\oplus C$ 不变。其正交投影
$P=\mathcal UP_Z\mathcal U^*$ 必须满足 (1.1)，却由 (6.1) 与 $\Pi=\mathcal UP_0\mathcal U^*$ 得本质距离严格小于 $1$，矛盾。

原小迹类线性 Sylvester 解仍满足其已证等式。本篇表明它不能延成这个固定 Julia 坐标中的任何有界完整非线性解；没有把线性解的正确性或完整 carry 项删去。

## 7. 固定有限吸收与准确剩余范围

先完整吸收任意一个固定有限头，再对吸收头与其余全部 Walsh 块选任意根，不改变证明：对所有充分大的 $j$，$U_j$ 的柱测试仍完全落在原负闭合块，(2.4) 和全部高位来源保持。因此 (1.1) 与有界图角排除对每个这样的固定基准也成立。

结论没有把任意真正原不变子空间预设成一个有界图角，也没有证明一般原闭稳定根不存在。若此类原根或未知不变旗存在，它必须避开所有这里固定的有界 Julia 图坐标。原同源二次分子 $Y^2=CQ^2$、其他非全域图角和真正非局部来源仍未解决；本篇不把这个已排实现类当作 ISP 完成。
