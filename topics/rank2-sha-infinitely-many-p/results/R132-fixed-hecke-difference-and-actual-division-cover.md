# R132：固定 Hecke 差分与真实平方除法覆盖

日期：2026-11-12。**状态：以下构造与保留性质已证明；主目标未完成。**

## 固定实际 CM 映射保留小高度，但增广指数增加二

固定 R105 的 $\Phi:X_0(3N_E)\to E_{17}$，以及 R128 的
$\sigma=\operatorname{Art}(1+2\sqrt{-15})$。
在 $C_2=X_0(61^2\cdot3N_E)$ 上令
$$
 \Phi_2=\Phi r_2-[2]\Phi r_1+\Phi r_0,
$$
其中 $r_j$ 是 cyclic $61^2$ 链的三个退化映射。
其微分为
$$
 c\bigl(F_0(q)-122F_0(q^{61})+3721F_0(q^{61^2})\bigr)\frac{dq}{q},
 \qquad F_0(q)=f(q)+3f(q^3).
$$
首系数非零，故 $\Phi_2$ 非恒定；该式仍处于 $61$-old 子空间，
没有新层 newform 原始性结论。

取实际 $\mathfrak b^2$-CM 提升后，完整迹准确满足
$$
 Q_2=(\sigma-1)^2Q,\qquad
 a(Q_2)=a(Q)+2,\qquad \widehat h(Q_2)\le16\widehat h(Q)=o(p).
$$
同一个 $r_+=r_-=1$、首 $\ell$-jet 单位、非挠及充分大 $p$ 时
不可被 $p$ 除均保留。首局部系数仅乘 $(\zeta_p-1)^2$，
它在 $\ell\ne p$ 处是单位。

## 连通核商不能省略完整迹和固定整数倍

$\Phi_2$ 诱导 $h:J(C_2)\to E_{17}$，准确分解为
$$
 J(C_2)\longrightarrow E'=J(C_2)/(\ker h)^0
       \xrightarrow{\mu}E_{17}.
$$
第一同态核连通，$\mu$ 是固定 $\mathbf Q$-同源。
这不把 $E'$ 识别为最小导子的 strong Weil 曲线，也不改变 old 微分。
若 $\phi':C_2\to E'$ 是对应映射，须取
$$
 Y'=\operatorname{Tr}_{H_\ell/L}\phi'(\widetilde z_\ell),\qquad
 Z'=[\deg\mu]Y'=[2]\widehat\mu Q_2.
$$
这样 $Z'$ 在整数点上范数为零；对 $p\nmid2\deg\mu$，
其增广指数仍为 $a(Q)+2$。裸 $U$-迹的 $L$-下降不作假定。

## 原始迹对应的实际覆盖是高维的

恢复原始 $\pi:X_0(N_E)\to E_{17}$。
类数为 $2$，实际完整 CM 除子属于
$S=\operatorname{Sym}^{2u}X_0(N_E)(L)$，其求和像为 $Q$。
令
$$
 W=(N_{L/F}\circ\operatorname{Res}_{L/F}f_{2u})^{-1}(O),\qquad
 X=W\times_{A,(\sigma-1)^2}A.
$$
$X\to W$ 是次数 **$p^4$** 的有限 étale 覆盖，且实际点提升的充要条件为
$a(Q)\ge2$。当 $2u\ge2g(X_0(N_E))-1$ 时，
$$
 \dim W=2pu-1.
$$
因此 $u^2=o(p)$ 尚未把它变成可以直接应用曲线 gonality 的固定覆盖。
Riemann--Roch 使任意 Jacobian 点可由次数至少亏格的有效除子表示；
配合 $\pi_*\pi^*=[\deg\pi]$，平方可除的像也能这样表示。
这个一般有效除子结论保不住“原始完整 CM 轨道”条件。

上述对照更换了映射；它不是原始 $\Phi$ 的反例。
仍缺少原始 Hecke 行的整数饱和输入或保留实际 CM 轨道的低维覆盖。

[完整证明、下降细节与原始来源](../notes/2026-11-12-fixed-hecke-difference-and-actual-division-cover.md)。
