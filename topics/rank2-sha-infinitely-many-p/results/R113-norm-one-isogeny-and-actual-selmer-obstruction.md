# R113：范数为零阿贝尔簇的实际 Kummer 同源与局部范数障碍

日期：2026-11-12。状态：已证明。

完整证明见
[研究笔记](../notes/2026-11-12-norm-one-isogeny-and-actual-selmer-obstruction.md)。

## 命题

取 R103–R111 的 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$
及实际循环次数 $p$ 扩张 $L/F$，其中 $p\ge7$ 在 $F,\mathbb Q(i)$
分裂，辅助素数 $\ell$ 在这两域惰性且 $v_p(\ell+1)=1$。
令 $\Gamma=\langle\tau\rangle$、$\lambda\mid\ell$，并定义
$$
\mathcal B=\operatorname{Res}_{L/F}E_L,\qquad
\mathcal A=\ker(N:\mathcal B\to E),\qquad\Delta=\tau-1.
$$
则 $\mathcal A$ 是维数 $p-1$ 的阿贝尔簇，$\Delta$ 是次数 $p^2$
同源，$\ker\Delta=\operatorname{diag}E[p]$，且
$\det(d\Delta)=p$。实际点商与 R104 下降类准确满足
$$
\frac{\ker(N:E(L)\to E(F))}{(\tau-1)\ker N}
=\mathcal A(F)/\Delta\mathcal A(F),\qquad
\delta_\Delta(Q)=c_Q.
$$
笔记 §1.1 给出所有坐标，故最后一个等式没有未定单位或符号。

在 $H^1(F_v,E[p])$ 中，$\Delta$ 的局部 Kummer 条件恰为
$$
\mathcal H_\Delta(v)=
\begin{cases}
\mathcal H_f(E/F_v),&v\ne\lambda,\\
\ker(H^1(F_\lambda,E[p])\to H^1(L_\lambda,E[p])),&v=\lambda.
\end{cases}
$$
辅助位为整个二维横截条件；其与通常局部条件交为零。
其余位包括所有 $p$ 位及坏位 $2,17$：不分歧范数在连通部分满射，
坏位组件群阶与 $p$ 互素；局部大小比较使用实际行列式 $p$。
因此
$$
\operatorname{Sel}_\Delta(\mathcal A/F)
\cap\operatorname{Sel}_p(E/F)
=\operatorname{Sel}_p^{\lambda=0}(E/F).
$$

令 $V_\lambda=\ker(E(F)/p\to E(F_\lambda)/p)$、
$\mathcal N=NE(L)/pE(F)$。全局与局部范数正合列给
$$
V_\lambda/\mathcal N
\simeq\ker\bigl(\Sha(\mathcal A/F)\to\Sha(E/L)\bigr).
$$
该核被 $p$ 和 $\Delta$ 杀掉；不假设任何 Sha 有限。

## 完整上同调提升及仍保留的通常局部格

对 $J=\mathcal A[p]$，中心 $-I$、Sah 引理、Chebotarev 及
Milne（2006），I, Theorem 4.10(a)，给 $\Sha^2(F,J)=0$，从而
$$
\operatorname{Sel}_p^{\lambda=0}(E/F)
\subseteq\operatorname{cor}_{L/F}H^1(L,E[p]).
$$
这不要求提升满足通常 Selmer 条件。给
$0\to J\to\mathcal B[p]\to E[p]\to0$ 配上通常、范数像、逆像局部格，
前者的逆像格在辅助位是整个四维 $H^1(F_\lambda,\mathcal A[p])$，
其余地方恰为 $\mathcal A$ 的通常 Kummer 格。
因此 Morgan–Smith（2024），Theorem 2.1 的剩余配对准确为
$$
\operatorname{Sel}_p^{\lambda=0}(E/F)
\times\operatorname{Sel}_p^{\lambda=0}(\mathcal A^\vee/F)
\longrightarrow\tfrac1p\mathbb Z/\mathbb Z,
$$
其左核恰为 $\operatorname{cor}_{L/F}\operatorname{Sel}_p(E/L)$，
右核恰为 $\mathcal B^\vee\to\mathcal A^\vee$ 的通常 Selmer 像。
两个商之间因而有完美配对。
这个明确配对与上面的点范数 Sha 核仍须处理。

## 对当前目标的作用与边界

指定的 Heegner 点 $Q_{\ell,p}$ 已成为这个实际同源的整数点，
所以目标不是一个任意增广模块的非零问题。
本结果不证明其 $\Delta$ 商非零，也不把任意范数点或任意 Sha 类
替换成指定的 $[Q_{\ell,p}]$。
R109 的长增广块在上层均来自 Mordell–Weil 点，Sha 像为零；
通常 Cassels–Tate 配对因此在整个块上为零，
不能仅由其交替性把超过一半的长度提升成完整长度。
