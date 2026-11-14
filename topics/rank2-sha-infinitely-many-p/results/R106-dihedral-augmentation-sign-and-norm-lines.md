# R106. 真实负增广块与可指定的基域范数线

状态：已证明。固定 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$。
令 $p\ge7$ 在 $F$ 和 $\mathbb Q(i)$ 均分裂，且 $p\ne17$。
辅助素数取
$$
\ell\equiv7\pmod{1020},\qquad\ell\equiv p-1\pmod{p^2},
$$
所以 $M_\ell=1$。沿用 R104 的次数 $p$ 循环域 $L_p/F$ 和真实
整数迹点 $Q_{\ell,p}=\operatorname{Tr}_{F[\ell]/L_p}P[\ell]$。

## 实际点所在的复共轭块

令 $\tau$ 生成 $\operatorname{Gal}(L_p/F)$，$c$ 为复共轭。
CM 点的反射公式和 $w(E/\mathbb Q)=+1$ 给
$cQ_{\ell,p}=-\tau^aQ_{\ell,p}$：可能的基域挠点由取范数及
$E(L_p)[p]=0$ 消去。取 $2b\equiv a\pmod p$，则真实 Galois
平移 $Q'=\tau^bQ_{\ell,p}$ 满足 $cQ'=-Q'$，且不改变增广类。

设
$$
\mathsf M=\ker(N:E(L_p)\to E(F))\otimes\mathbb Z_p,
\qquad\delta=\tau^{(p-1)/2}(\tau-1).
$$
准确有 $c\delta c=-\delta$，所以目标块为
$$
\left(\mathsf M/\delta\mathsf M\right)^-
=\mathsf M^-/\delta\mathsf M^+.
$$
R104 的整数正合列在所需符号上为
$$
0\to\bigl(NE(L_p)/pE(F)\bigr)^+
\to\mathsf M^-/\delta\mathsf M^+
\to H^1(C_p,E(L_p))^+\to0.
$$
两处符号翻转来自 $(\tau-1)$ 与循环 cocycle 在 $\tau$ 上的值。
实际 Heegner 类的右端像满足通常 Selmer 条件，落入可能的
$\Sha(E/F)[p]^+$，没有先将它删除。

## 真实范数像的可指定上界

$L_p/F$ 在 $\ell$ 上方全分歧且 $E$ 好约化，故局部范数准确是
$pE(F_\lambda)$。令
$$
\rho_\ell:E(\mathbb Q)/pE(\mathbb Q)
\longrightarrow E(\mathbb F_\ell)/pE(\mathbb F_\ell)\simeq\mathbb F_p.
$$
则实际基域正特征范数像满足
$$
\bigl(NE(L_p)/pE(F)\bigr)^+\subseteq\ker\rho_\ell.
$$

对除固定饱和指数外的每个 $p$，$P=(-1,4)$、$Q=(9,24)$ 模 $p$
独立。它们在 $K=\mathbb Q(E[p])$ 上的完整 Kummer 平移群为
$E[p]^2$。证明使用完整 CM 正规化子、Maschke 分解和中心 $-I$
的 Sah 计算；任意较小平移群都会给 $P,Q$ 的非零模 $p$ 关系。
该平移扩张与 $K\mathbb Q(\zeta_{1020p^2})$ 在 $K$ 上不交：
后者新增的 $p$ 部至多为 $p$，前者任何非零正常商至少有阶 $p^2$。
因此可以同时施加上列模 $p^2$ 同余和任意非零的两点约化函数。
Chebotarev 遂给：对每条预定线
$\mathcal L\subset E(\mathbb Q)/pE(\mathbb Q)$，都有正密度的合法
$\ell$ 满足 $\ker\rho_\ell=\mathcal L$。

这没有给统一的小 $\ell$ 界，不能直接与 R105 的 Linnik 高度选择
合并；也没有把范数像的上界线当成实际非零范数点。
仍待证明的是指定 $[Q_{\ell,p}]$ 在负增广块内的非零性。

[完整证明、实际符号、同余域相容性及量词](../notes/2026-11-12-dihedral-augmentation-sign-and-norm-lines.md)。
