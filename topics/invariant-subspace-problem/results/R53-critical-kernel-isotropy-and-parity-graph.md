# R53：原临界核的全等向性与偶奇 Walsh 图

日期：2026-11-12（UTC+8）。分工：`critical_kernel`。

**状态：已证明的中间结论；原临界核仍未决定。** 本条使用 R50 已验证的实际算子近似，证明核在复对称双线性型下必须全等向。它保留实际进位误差，不把纯独立张量模型的核结论转用到本算子。

## 1. 结论

仍令

$$
K=\ker L=\ker D,\qquad
(Cv)(y)=\overline{v(-1-y)},\qquad
B(v,w)=\langle v,Cw\rangle.
$$

**定理。**

$$
\boxed{B(v,w)=0\qquad(v,w\in K).}
\tag{1.1}
$$

因而

$$
CK\subseteq K^\perp,\qquad
K\subseteq\overline{LH},\qquad K\cap CK=\{0\}.
\tag{1.2}
$$

特别地，核不含任何非零 $C$-实向量，即不存在 $0\ne v\in K$ 满足 $Cv=v$。

## 2. 尾乘法交换子的强极限

设

$$
\delta_j=\frac2{(j+2)^2+1},\qquad
\rho_m^2=\sum_{j\ge m}\delta_j^2,
\qquad
H_m=\sum_{j\ge m}\delta_j M_{\chi_j},
\qquad\chi_j=(-1)^{b_j}.
$$

$H_m$ 是有界自伴乘法算子，其定义级数按范数绝对收敛，并且

$$
\|H_m\|\le\sum_{j\ge m}\delta_j=O(m^{-1}),
\qquad \rho_m^2\asymp m^{-3}.
\tag{2.1}
$$

R50 给出了

$$
T_m=B_m\otimes I+\sum_{j\ge m}\delta_jE_j,
\qquad\|L-T_m\|\le22\eta_{m-1},
\tag{2.2}
$$

其中 $B_m$ 只作用低 $m$ 位，$E_j=e_{10}$ 作用第 $j$ 位，$\eta_j=a_{j+1}/a_j$ 超快趋零。

由于低位头部与 $H_m$ 交换，且在一个二元位上

$$
[M_{\chi_j},E_j]=-2E_j,
$$

有精确式

$$
[H_m,T_m]=-2\sum_{j\ge m}\delta_j^2E_j.
\tag{2.3}
$$

实际进位误差满足

$$
\frac{\|[H_m,L]-[H_m,T_m]\|}{\rho_m^2}
\le44\frac{\|H_m\|}{\rho_m^2}\eta_{m-1}
=O(m^2\eta_{m-1})\longrightarrow0.
\tag{2.4}
$$

另一方面，

$$
\frac1{\rho_m^2}\sum_{j\ge m}\delta_j^2E_j
\xrightarrow[\ m\to\infty\ ]{\mathrm{SOT}}\frac12I.
\tag{2.5}
$$

这里给出所需的直接证明。若 $h$ 只依赖低 $q$ 位且 $m\ge q$，则

$$
E_jh=\frac12(1-\chi_j)h\quad(j\ge m),
$$

而各 $\chi_jh$ 相互正交。因此

$$
\left\|\left(\frac1{\rho_m^2}\sum_{j\ge m}\delta_j^2E_j-\frac12I\right)h\right\|^2
=\frac14\frac{\sum_{j\ge m}\delta_j^4}{(\sum_{j\ge m}\delta_j^2)^2}\|h\|^2
=O(m^{-1})\|h\|^2.
$$

左侧算子范数一致有界（正权归一化的 $E_j$ 平均范数至多一），所以由柱函数稠密性推广到所有 $h\in H$，证明 (2.5)。结合 (2.3)–(2.5)，得到实际算子的交换子极限

$$
\boxed{\frac{[H_m,L]}{\rho_m^2}\xrightarrow{\mathrm{SOT}}-I.}
\tag{2.6}
$$

这与 $L$ 拟幂零并不矛盾：$\|H_m/\rho_m^2\|$ 没有一致界，故 (2.6) 不是一个有界算子的精确交换子恒等式。

## 3. 对实际核应用双线性对称性

R24/R43 给出 $B(Lx,y)=B(x,Ly)$。若 $v,w\in K$，则对每个 $m$，

$$
\begin{aligned}
B([H_m,L]v,w)
&=B(H_mLv,w)-B(LH_mv,w)\\
&=0-B(H_mv,Lw)=0.
\end{aligned}
$$

除以 $\rho_m^2$ 后，用 (2.6) 的逐向量强收敛及 $B$ 的连续性，得到 $-B(v,w)=0$，证明 (1.1)。

由 $L=CL^*C$，$CK=\ker L^*$。于是 (1.1) 等价于 $K\perp CK$；这给 (1.2)，包括

$$
K\subseteq(\ker L^*)^\perp=\overline{LH}.
$$

若 $v\in K$ 且 $Cv=v$，则 $B(v,v)=\|v\|^2$，所以 $v=0$。

## 4. 偶数与奇数 Walsh 阶的精确平衡

令 $Jv=\overline v$ 为逐点复共轭，$Rv(y)=v(-1-y)$。$C=RJ$，而 $A$、$L$ 都有实系数，因此 $JK=K$。由 (1.1)，

$$\langle v,Rw\rangle=0\qquad(v,w\in K).\tag{4.1}$$

反射在 Walsh 基上作用为

$$R\chi_S=(-1)^{|S|}\chi_S.$$

故每个核向量满足

$$
\boxed{
\sum_{|S|\text{ 偶}}|\widehat v(S)|^2
=\sum_{|S|\text{ 奇}}|\widehat v(S)|^2
=\frac12\|v\|^2.
}
\tag{4.2}
$$

更一般地，偶、奇投影 $P_+,P_-$ 在 $K$ 上满足

$$
\langle P_+v,P_+w\rangle
=\langle P_-v,P_-w\rangle
=\tfrac12\langle v,w\rangle.
\tag{4.3}
$$

所以 $M_+=P_+K$、$M_-=P_-K$ 均为闭子空间，且存在酉同构 $U:M_+\to M_-$，使

$$
K=\{x+Ux:x\in M_+\}.
\tag{4.4}
$$

证明是定义 $U(P_+v)=P_-v$；(4.3) 保证良定义、等距且满射，$P_\pm|_K$ 范数均为 $1/\sqrt2$ 的等距嵌入，所以像闭。

这不是已确定具体 $M_\pm$ 或 $U$。无限维空间上存在非零全等向闭空间，故 (4.4) 本身仍不迫使 $K=0$。

## 5. 没有推出的结论

本条证明 $K\subseteq\overline{LH}$，并未证明 $K\subseteq\operatorname{Ran}L$，更未证明 R44 所需的 $K\subseteq\operatorname{Ran}A$。由 (2.6) 产生的近似原像包含因子 $1/\rho_m^2$，没有获得一致范数界。

把尾平均强趋标量直接用于所有向量不足以判定核；本条有效的新步骤是将**实际核方程**和 $B$-对称性代入交换子恒等式，从而得到全等向性。下一问题是这个全等向图与 $A$-不变性、实际长链进位能否共同给出更强约束。当前没有证明它们不相容。
