# R12 附录：同一有界平方分子分母的最大稳定闭根及全部原旗的图核心

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：正向实现定理，非根的存在定理。** 本文从实际有界等式 $Y^2=CP^2$ 出发，付清最大商的闭性、稳定域、原值域图核心及原不变旗上的闭图返回。没有构造满足该等式的非零原 $P,Y$；整数幂共同分母及全喷射平坦均不能代替此等式。

## 1. 明确的交换及单射假设

先在任意复 Hilbert 空间 $H$ 上设 $C,P,Y$ 有界，$C,P$ 单射且值域稠密，且

$$
CP=PC,\qquad CY=YC,\qquad PY=YP,\qquad Y^2=CP^2.
\tag{1}
$$

$PY=YP$ 是独立写出的假设，不由一般的 $P,Y\in C'$ 推出。

本文的实际应用是原 Haar 尾 $C=A^{(m_0)}$，绝非负整数边界移位。原全交换子的交换性有 [R24 §1](R24-complex-symmetric-moments-and-escape.md) 的完整来源：原 $J$ 对称性和 $J\Omega=\Omega$、$\Omega$ 循环先迫每个交换子 $F$ 都满足 $F^*=JFJ$；对 $F,G,FG$ 同用此式才得到 $FG=GF$。不能只从循环性作此推断。

此外，下面使用的 [R267 特定共同分母](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md) 本身是原多项式的一致有界强极限，直接属于 $C''$，所以它与每个 $Y\in C'$ 交换；这一路也独立支付 (1) 的第三式。

## 2. 最大商直接给稳定的闭域

定义

$$
D(S)=\{x\in H:Yx\in\operatorname{Ran}P\},\qquad
Sx=P^{-1}Yx.
\tag{2}
$$

这里 $P^{-1}$ 只在真实 $\operatorname{Ran}P$ 上定义。

**定理 2.1。** 在 (1) 下，$S$ 闭、单射、稠密定义且值域稠密，并且

$$
\operatorname{Ran}P+\operatorname{Ran}Y\subset D(S),\qquad
SP=Y,\quad SY=CP,
\tag{3}
$$

$$
SD(S)\subset D(S),\qquad
D(S^2)=D(S),\qquad S^2x=Cx\quad(x\in D(S)).
\tag{4}
$$

此外 $CD(S)\subset D(S)$ 且 $SCx=CSx$。

**证明。** 图有准确的有界核表示

$$
\Gamma S=\{(x,u)\in H^2:Yx=Pu\}=\ker[\,Y\ \ -P\,].
\tag{5}
$$

$P$ 单射使它是算子图，故 $S$ 闭。$YP=PY$ 给 $\operatorname{Ran}P\subset D(S)$ 及 $SP=Y$；因此域稠密。又 $Y^2=CP^2=P(CP)$ 给 $YH\subset D(S)$ 及 $SY=CP$。

$Y^2=CP^2$ 单射，故 $Y$ 单射。它的值域也稠密：$P^2H$ 稠密，连续 $C$ 将其像稠密送入 $CH$，而 $CH$ 稠密；所以 $Y^2H$ 稠密，进而 $YH$ 稠密。由 $SP=Y$，$S$ 的值域稠密，且由 $PS=Y$ 知 $S$ 单射。

固定 $x\in D(S)$，置 $u=Sx$，则 $Yx=Pu$。乘以 $Y$ 并用交换得到

$$
P Yu=Y^2x=CP^2x=P(CPx).
$$

消去单射的 $P$ 得 $Yu=P(Cx)$。所以 $u\in D(S)$ 且 $Su=Cx$。这直接证明稳定域与 (4)，没有预先使用未定义的 $S^2x$。最后 $YCx=CYx=CPu=PCu$，给 $Cx\in D(S)$、$SCx=Cu$。证毕。

特别，**平方**等式在这里确实自动付域稳定；本文不把这一步无证明推广到一般 $q$ 次关系 $Y^q=C^pP^q$。

## 3. 指定分母的强单位给实际图核心

进一步设有有界 $W_n$ 与 $P,Y$ 都交换，使

$$
Q_n=PW_n,\qquad \sup_n\|Q_n\|<\infty,\qquad Q_n\longrightarrow I
\quad\text{强}.
\tag{6}
$$

对 $x\in D(S)$、$u=Sx$，有

$$
Q_nx\in\operatorname{Ran}P,\qquad
S Q_nx=YW_nx=W_nYx=Q_nu.
\tag{7}
$$

因此 $(Q_nx,SQ_nx)\to(x,Sx)$，从而

$$
\boxed{\operatorname{Ran}P\text{ 是 }S\text{ 的图核心},\qquad
\Gamma S=\overline{\{(Pz,Yz):z\in H\}}.}
\tag{8}
$$

这是真实图范数逼近，不是单独的 $\overline{\operatorname{Ran}P}=H$。

若 $J$ 是原共轭且 $P^*=JPJ,\ Y^*=JYJ$，则该最大根还满足 $S^*=JSJ$。确切地，令 $S_0(Pz)=Yz$。对双线性式 $[x,y]=\langle x,Jy\rangle$，其转置的域由

$$
[S_0Pz,x]=[Yz,x]=[z,Yx]=[Pz,u]\quad(z\in H)
$$

准确等价于 $Yx=Pu$；故 $S_0^{\,t}=S$。而 (8) 给 $\overline{S_0}=S$，再取转置得到 $S^t=S$。这里没有仅由两个有界系数对称就省略商的核心。

## 4. 原共同分母：唯一实现与全部不变旗

现在固定原 Haar 尾 $C$，取 R267 的同一个 $P$。它给 $W_n\in\mathcal A=\overline{\mathbb C[I,C]}^{\|\cdot\|}$，满足

$$
\|PW_n\|\le1,\qquad PW_n\longrightarrow I\quad\text{强*}.
\tag{9}
$$

若某个 $Y\in C'$ 真实满足 $Y^2=CP^2$，则 §§2–3 全部适用。

该实现是唯一的：若 $T$ 是闭、稠密定义、与 $C$ 在真实域上交换的算子，且 $PH\subset D(T)$、$TP=Y$，则原一致有界强多项式逼近与闭性给 $P D(T)\subset D(T)$、$TPx=PTx$。于是 $T\subset S$。另一方面 $T$ 包含 $S_0$，闭性及 (8) 给 $S\subset T$，故 $T=S$。此唯一性甚至不必再预设 $T^2=C$。

同一结论适用于每个有限放大 $C^{(d)}$ 的原闭不变旗 $N\subset M$。这里使用 [R88](R88-riesz-basis-bounded-multipliers-strong-closure.md) 的实际全交换子强多项式闭包，确保 $P^{(d)},Y^{(d)},W_n^{(d)}$ 都保持旗。置 $Q=M/N$，诱导系数记为 $C_Q,P_Q,Y_Q$；R267 的 (9) 下降为商上的收缩强单位。若 $P_Qx=0$，则 $(Q_n)_Qx=(W_n)_QP_Qx=0$，强极限迫 $x=0$；又 $(Q_n)_Qx=P_Q(W_n)_Qx\to x$，故 $P_Q$ 稠值。这里明确使用 $W_n\in\mathcal A$ 保持两个旗空间。

原 [R140 §§1.1、6](R140-invariant-subquotient-type-and-fixed-first-regularization.md) 已付 $C_Q$ 单射稠值：R23 的收缩强单位 $E_\ell$ 最低次数趋于无穷，充分大时准确等于 $C R_\ell(C)$。$C_Qx=0$ 时所有这些 $(E_\ell)_Qx=0$，迫 $x=0$；而 $(E_\ell)_Qx\in C_QQ$ 并趋于 $x$。同一论证保有限放大，未由环境空间稠密像外推。

在这一已付原子商事实下，

$$
Y_Q^2=C_QP_Q^2,\qquad
S_Q=P_Q^{-1}Y_Q,\qquad
D(S_Q)=\{x:Y_Qx\in\operatorname{Ran}P_Q\}
\tag{10}
$$

是同一实际子商上的闭稳定平方根，且 $P_QQ$ 是图核心。

更精确地，在原空间 $S$ 保持每个原不变闭空间 $M$ 的域部分：若 $x\in D(S)\cap M$，则 $P Sx=Yx\in M$，而 $P_{H/M}$ 单射迫 $Sx\in M$。$(S|_M)$ 的图核心为 $PM$，因为 (7) 的所有 $W_nx$ 仍在 $M$。对旗 $N\subset M$，把该图送入 $Q^2$ 后，其**闭包**准确等于 $\Gamma S_Q$：它包含全部 $(P_Qz,Y_Qz)$，后者由 (8) 在 $\Gamma S_Q$ 中图稠密；反向包含直接由商上的有界核式 (5) 得到。没有声称未经闭包的图像已闭。

## 5. 与既有必要条件的区别及尚缺输入

[全交换子喷射与平坦分母稿 §5](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md) 从既有闭根及全域分母推出 $Y^2=CP^2$，并迫 $P,Y$ 的全部形式喷射为零。本稿给该**实际有界等式**的正向最大域实现；对 R267 的特定 $P$，进一步付同一值域图核心、唯一性及所有原旗的闭图返回。

在整个原尾上 $S$ 必无界，否则与[单拷贝有界平方根排除](R12-appendix-all-integer-power-root-multiplicity-and-closed-root-domains.md)矛盾。本文不把这一整尾有界根排除自动搬到任意未知子商。

核心仍是构造真实 $Y\in C'$，而非形式解，满足同一个 $Y^2=CP^2$。R267 的 $P=C^rR_r$（每个整数 $r$）、$P$ 的全喷射平坦，以及 (9)，均尚未支付该二次式。也没有用指定闭乘子 $X_f$ 的特殊无分母结论排除所有未知闭根；$X_f$ 本身闭，旧文不可闭的对象是另一投影型映射 $Z$，二者保持区分。
