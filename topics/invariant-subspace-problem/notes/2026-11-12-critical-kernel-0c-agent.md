# 原临界交换子：反向有界除法也全部失败

日期：2026-11-12（UTC+8）。分工：`critical_kernel`。

**状态：§§1–6 是已完成证明的中间结论；§7 明确记录核问题仍未解决。**
本笔记从 R43–R44 的实际核缺口继续。它不把形式系数、正算子序或另一种 Hilbert 空间表示的单射性移用为当前表示的单射性。

## 1. 结论及其用途

沿用 R9、R36、R43 的具体算子

$$
(Af)(y)=w(y)f(y-1),\qquad
w(y)=a_{v_2(y)},\quad w(0)=0,
$$

$$
a_j=e^{-L_j},\qquad
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
$$

以及

$$
d_j=W_{2^j}=\|A^{2^j}\|,\quad
N_j=A^{2^j}/d_j,\quad
\eta_j=a_{j+1}/a_j,
$$

$$
\delta_j=\frac2{(j+2)^2+1},\qquad r_j=1-\delta_j,
$$

$$
L=\sum_{j\ge0}\bigl[\log(I+N_j)-\log(I+r_jN_j)\bigr]
  =\sum_{n\ge1}c_nA^n,
\qquad D=I-e^{-L}.
$$

R43 已证明 $c_n>0$ 以及 $\sum c_nW_n<\infty$；R36 已证明 $\operatorname{Ran}D=\operatorname{Ran}L$。本笔记证明反向的全部有限阶除法同样失败：

**定理 1.1。** 对每个整数 $m\ge1$，不存在任何 $B\in B(H)$ 使

$$
\boxed{A^m=LB.}
\tag{1.1}
$$

因而

$$
\boxed{\operatorname{Ran}A^m\not\subseteq\operatorname{Ran}L
       =\operatorname{Ran}D\qquad(m\ge1).}
\tag{1.2}
$$

R36 另已证明 $\operatorname{Ran}L\not\subseteq\operatorname{Ran}A$；由于 $\operatorname{Ran}A^m\subseteq\operatorname{Ran}A$，两者合起来得到：$\operatorname{Ran}D$ 与每个有限幂 $\operatorname{Ran}A^m$ **在两方向都没有包含关系**。

若 (1.1) 成立，$A^mH$ 稠密就会推出 $LH$ 稠密，并由复对称性推出 $\ker L=0$。所以本定理排除的是一条确实足以解决原临界核、但实际走不通的反向除法路线。它不证明 $LH$ 不稠密，也不证明 $\ker L$ 非零。

## 2. 一个保留范数与正序、但不保留核的辅助表示

R9/R31 中的局部矩阵代数为

$$
\mathcal C_m=M_{2^m}(\mathbb C)\otimes I,
\qquad \mathcal C=\overline{\bigcup_m\mathcal C_m}^{\|\cdot\|}
             =C^*(I,A).
$$

这里 $H=L^2(\mathbb Z_2)$ 的局部标准基是二进位的 $e_0,e_1$，原来的无限乘积参考向量为 $(e_0+e_1)/\sqrt2$。

在 $\ell^2(\mathbb N_0)$ 上也表示同一个局部矩阵代数：把整数唯一写成 $n=r+2^mq$，$0\le r<2^m$，让 $X\in M_{2^m}$ 在 $r$ 上作用，在 $q$ 上恒等。这个表示对每个局部矩阵保持算子范数，且与局部代数之间的嵌入相容。因此延伸成等距的含单位 $*$-同态

$$
\pi:\mathcal C\longrightarrow B(\ell^2(\mathbb N_0)).
\tag{2.1}
$$

它特别保留正算子序。

在这个表示中，$A$ 变成单边加权移位

$$
Je_k=a_{v_2(k+1)}e_{k+1}\qquad(k\ge0).
\tag{2.2}
$$

为核实 (2.2)，R9 的 $A_m$ 删除了每一段长度 $2^m$ 的回绕边；$\pi(A_m)$ 是在每一条这样的有限链上作用的同一个加权幂零矩阵。它与 (2.2) 的差只出现在 $k+1$ 为 $2^m$ 倍数的位置，差的范数为 $a_m$。由 $\|A-A_m\|=a_m\to0$ 得 $\pi(A)=J$。

记

$$
\Lambda=\pi(L)=\sum_{n\ge1}c_nJ^n.
\tag{2.3}
$$

级数按范数绝对收敛。$\Lambda$ 的下三角矩阵首条非零次对角线对应 $c_1J$，且 $c_1>0$。故 $\Lambda$ 是单射：若 $x\ne0$，取最小的 $k$ 使 $x_k\ne0$，则

$$
(\Lambda x)_{k+1}=c_1a_{v_2(k+1)}x_k\ne0.
\tag{2.4}
$$

**不能由 (2.4) 推出原 $L$ 单射。** 甚至 $A$ 在原表示中值域稠密，而 $J$ 的值域与 $e_0$ 正交。这两个事实已经说明核/闭值域不在两个表示间自动转移。下文只转移 $\mathcal C$ 内的有界正序不等式。

## 3. 任意有界反向商给出的形式系数必要界

假设存在 $B\in B(H)$ 使 $A^m=LB$。则

$$
A^mA^{*m}\le \|B\|^2LL^*.
\tag{3.1}
$$

两边属于 $\mathcal C$，所以应用 (2.1) 后得到

$$
J^mJ^{*m}\le \|B\|^2\Lambda\Lambda^*.
\tag{3.2}
$$

以下给出所需的有界因子构造，不将它当成形式除法。由 (3.2)，在 $\operatorname{Ran}\Lambda^*$ 上定义

$$
S(\Lambda^*x)=J^{*m}x.
$$

不等式保证其良定义且范数至多 $\|B\|$。把 $S$ 连续延伸到 $\overline{\operatorname{Ran}\Lambda^*}$，再在正交补上置零，即得有界算子。取伴随 $T=S^*$ 后有

$$
\Lambda T=J^m,\qquad \|T\|\le\|B\|.
\tag{3.3}
$$

写

$$
Te_0=\sum_{k\ge0}b_kW_ke_k,\qquad W_0=1.
$$

于是

$$
|b_k|W_k\le\|T\|\le\|B\|.
\tag{3.4}
$$

另一方面，$J^ne_k=(W_{n+k}/W_k)e_{n+k}$。因此将 (3.3) 作用于 $e_0$ 并逐坐标比较，得到

$$
\left(\sum_{n\ge1}c_nz^n\right)
\left(\sum_{k\ge0}b_kz^k\right)=z^m
\quad\text{于 }\mathbb C[[z]].
\tag{3.5}
$$

每个固定坐标只涉及有限个项，所以此比较不需要标量级数在非零点收敛。由于 $c_1\ne0$，(3.5) 唯一确定形式商

$$
\sum_{k\ge0}b_kz^k=\frac{z^m}{\sum_{n\ge1}c_nz^n}.
\tag{3.6}
$$

综上：若任意 $B(H)$ 中的商存在，这个唯一形式商的系数必须满足 (3.4)。并没有预设 $B$ 属于 $\mathcal A$、属于 $\mathcal C$，或与 $A$ 交换。

## 4. 对数系数的尺度及超递增估计

设

$$
\lambda_j=-\log d_j.
$$

由 $d_j=a_j\prod_{s<j}a_s^{2^{j-s-1}}$ 和 $L_j$ 的闭式，有限几何级数求和给

$$
\boxed{\lambda_j=100\,16^j-105\,8^j+(150j+25)2^j.}
\tag{4.1}
$$

例如 $\lambda_0=20$、$\lambda_1=1110$。还具有

$$
\lambda_j-16\lambda_{j-1}
=2^j(105\,4^j+1025-1050j)>0\qquad(j\ge1).
\tag{4.2}
$$

最后的严格正号可直接验证 $j=1$；括号从 $j$ 到 $j+1$ 的增量为 $315\,4^j-1050>0$（$j\ge1$）。因此 $\lambda_j\ge16\lambda_{j-1}>0$。

对整数 $n\ge2$，定义

$$
p(n)=\frac{n}{2^{v_2(n)}}\lambda_{v_2(n)}.
$$

R43 的精确式，写 $n=2^ju$、$u$ 为奇数，为

$$
c_n=\frac{1-r_j^u}{u d_j^u}
-\sum_{i<j}\frac{1-r_i^{u2^{j-i}}}
 {u2^{j-i}d_i^{u2^{j-i}}}.
$$

由于 R43 已证正性，且被减项全部非负，得到

$$
0<c_n\le e^{p(n)}.
\tag{4.3}
$$

dyadic 项有更精确的上下界

$$
\beta_j:=c_{2^j}d_j,\qquad
\delta_j-\eta_{j-1}\le\beta_j\le\delta_j\quad(j\ge1),
\qquad\beta_0=\delta_0.
\tag{4.4}
$$

故 $\beta_j/\delta_j\to1$。并且

$$
c_1=\delta_0/a_0=(2/5)e^{20}>1.
\tag{4.5}
$$

为比较所有形式逆展开项，令

$$
q_j=\frac{\lambda_j}{2^j-1}\qquad(j\ge1).
$$

它严格递增：由 (4.2)，对 $j\ge2$，$q_j/q_{j-1}\ge16(2^{j-1}-1)/(2^j-1)>1$。若 $n\ge2$ 且 $v_2(n)\le h$、$h\ge1$，则

$$
\boxed{p(n)\le q_h(n-1).}
\tag{4.6}
$$

当 $v_2(n)=j\ge1$ 时，写 $n=u2^j$，由 $u2^j-1\ge u(2^j-1)$ 得 $p(n)/(n-1)\le q_j\le q_h$。当 $j=0$ 时，$n$ 为至少 $3$ 的奇数，$p(n)/(n-1)=n\lambda_0/(n-1)\le(3/2)\lambda_0<q_1$。

## 5. 形式逆的多高位主项与完整余项控制

固定 $m\ge1$。对 $J\ge2$ 置

$$
N_J=\sum_{s=0}^{m-1}2^{J+s}=(2^m-1)2^J,
\qquad S_J=N_J-m,
\qquad P_J=\sum_{s=0}^{m-1}\lambda_{J+s}.
$$

形式几何级数 (3.6) 给

$$
b_{N_J-1}
=\sum_{k=1}^{S_J}(-1)^kc_1^{-k-1}
\sum_{\substack{n_1,\ldots,n_k\ge2\\
                  \sum_i(n_i-1)=S_J}}
                 \prod_{i=1}^kc_{n_i}.
\tag{5.1}
$$

其中主项为 $k=m$、$\{n_i\}_{i=1}^m=\{2^J,\ldots,2^{J+m-1}\}$ 的 $m!$ 个排列：

$$
M_J=(-1)^m\frac{m!}{c_1^{m+1}}
             \prod_{s=0}^{m-1}c_{2^{J+s}}.
\tag{5.2}
$$

**引理 5.1。** (5.1) 中任意非主项的有序组合都满足

$$
\sum_i p(n_i)\le P_J-\frac12\lambda_J.
\tag{5.3}
$$

**证明。** 从最高的预定 dyadic 项 $2^{J+m-1}$ 向下检查。当前要检查的层为 $q\in\{J,\ldots,J+m-1\}$ 时，假设更高的预定项已经各取了一次，则剩余预算是

$$
S(q)=\sum_{s=J}^{q}(2^s-1)
    =2^{q+1}-2^J-(q-J+1)<2^{q+1}.
$$

任何剩余 $n_i$ 的 $2$-进阶都不大于 $q$。若其阶为 $q$，由预算限制该项只能是 $n_i=2^q$，不能是 $3\cdot2^q$ 或更大的奇数倍。并且这样的项至多一个，因为

$$
2(2^q-1)>S(q)
$$

（使用 $J\ge2$）。

非主项必有第一个缺失的层 $q$。在该层以下的全部剩余项都满足 $v_2(n_i)\le q-1$。由 (4.6)，它们的 $p$ 值总和严格小于

$$
q_{q-1}2^{q+1}
=\lambda_{q-1}\frac{2^{q+1}}{2^{q-1}-1}
\le 8\lambda_{q-1}\le\tfrac12\lambda_q,
$$

因为 $q\ge J\ge2$。与主项剩余部分的 $p$ 值至少为 $\lambda_q$ 相比，至少损失 $\lambda_q/2\ge\lambda_J/2$。把已经相同的高位项加回即得 (5.3)。证毕。

把正整数 $S_J$ 写成有序正整数和的方式共有 $2^{S_J-1}$ 个。因此由 (4.3)、(4.5)、(5.3)，全部非主项之和 $E_J=b_{N_J-1}-M_J$ 满足

$$
\boxed{|E_J|\le2^{S_J-1}\exp(P_J-\lambda_J/2).}
\tag{5.4}
$$

这包括所有组合长度、全部偶数/奇数阶系数和所有可能的进位，不是仅抽取一种有利分拆。

由 (4.4)，主项绝对值为

$$
|M_J|=\frac{m!}{c_1^{m+1}}e^{P_J}
                         \prod_{s=0}^{m-1}\beta_{J+s},
\qquad \beta_{J+s}\sim\delta_{J+s}\asymp J^{-2}.
$$

由于 $m$ 固定、$S_J=O_m(2^J)$、$\lambda_J\ge20\,16^J$，(5.4) 给 $E_J=o(M_J)$。

最后，$N_J$ 的二进制展开恰在 $J,\ldots,J+m-1$ 上取 $1$；R13 的无进位范数乘法给

$$
W_{N_J}=\prod_{s=0}^{m-1}d_{J+s}=e^{-P_J},
\qquad W_{N_J-1}=W_{N_J}/a_J.
$$

故得到精确主项渐近式

$$
\boxed{
b_{N_J-1}W_{N_J-1}
=(-1)^m\frac{m!}{c_1^{m+1}a_J}
        \prod_{s=0}^{m-1}\delta_{J+s}\,(1+o(1)).
}
\tag{5.5}
$$

右侧绝对值趋于无穷，因为 $a_J$ 超快趋零，而 $m$ 个 $\delta$ 的乘积只按 $J^{-2m}$ 衰减。因此 (3.4) 不可能成立，证明了定理 1.1 的 (1.1)。

## 6. 从算子因子到实际值域不包含

这里补齐 (1.1) 到 (1.2) 的逻辑。若 $\operatorname{Ran}A^m\subseteq\operatorname{Ran}L$，对每个 $x\in H$，定义 $Bx$ 为方程 $Ly=A^mx$ 在 $(\ker L)^\perp$ 内的唯一解。它处处有定义且线性。

若 $x_n\to x$、$Bx_n\to y$，则 $y\in(\ker L)^\perp$ 且

$$
Ly=\lim_nLBx_n=\lim_nA^mx_n=A^mx.
$$

唯一性给 $y=Bx$，故 $B$ 闭。闭图定理使 $B$ 有界，从而 $A^m=LB$，与已证的 (1.1) 矛盾。此证明没有要求先知道 $\ker L=0$。

因为 $D=L\Psi(L)$、$\Psi(L)$ 可逆且与 $L$ 交换，(1.1) 对 $D$ 也同样成立：若 $A^m=DB$，则 $A^m=L\Psi(L)B$。

## 7. 仍未完成的实际核问题

本结果加强的是**实际值域不能相互包含**。即使两个实际值域彼此不包含，它们的闭包仍可以同时等于 $H$，所以不能据此宣称产生非平凡闭不变子空间。

仍需处理原来的 $\ker L=\ker D$。R44 的充分条件

$$
\ker D\subseteq\operatorname{Ran}A
$$

仍然未证。上面排除的是 $\operatorname{Ran}A^m\subseteq\operatorname{Ran}D$，它与 R44 的核正则性条件方向不同，没有逻辑冲突。

同时，辅助表示中的 $\Lambda=\pi(L)$ 单射，是其单边三角结构的初等结论；它不能作为原表示 $L$ 单射的证据。§3 有效的转移只发生在有界正算子序不等式 (3.1) 上。

## 8. 对相邻张量模型文献的核查边界

Gabriel H. Tucci, *Some quasinilpotent generators of the hyperfinite II$_1$ factor*, arXiv:0708.1968v1 (2007), Theorem 4.4，PDF p.14，研究几何系数的独立张量 nilpotent 和，并利用有限因子核投影的迹递推证明无核。原文：<https://arxiv.org/pdf/0708.1968>。

该表示和算子都不同于本题。本文没有引用其无核结论；原 $L$ 的进位项和当前纯乘积表示不能被忽略。有限迹递推在这里尚无得到验证的替代品。

## 9. 本轮没有成立的两个简化

1. 对 $\delta_j\asymp j^{-2}$，归一化正尾平均可强趋 $I/2$；这仍不提供在潜在核上的统一范数估计，也不能把近似特征向量的关系转成可逆性。
2. 把原临界两乘积和通过 R37 的强乘子换成另一个参考乘积，没有自动删除临界参数。两个乘积间的相对 $\ell^1$ 差及临界标量抵消仍在，尚未得到新的循环性证明。

以上失败方向没有被登记为解决核问题的结果。当前唯一新增完整结论是定理 1.1 及其证明。
