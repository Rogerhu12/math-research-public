# R146 — 正号 Selmer 两步判据允许变化辅助 Heegner 域

**状态：已证明。日期：2026-11-12。**

## 结论

固定 $E=389\mathrm a1$。允许辅助虚二次 Heegner 域 $F$ 随
$p$ 变化，但逐个保留完整证明 §1 的条件：$389$ split $F$，
$p\nmid\operatorname{disc}F\,h_F$，$p\ge7$ 好普通、非异常，
$G_F$ 的 Tate 像为全 $\mathrm{GL}_2$；$\ell$ inert $F$，
$\ell+1=pu$ 且 $p\nmid ua_\ell$。

取全部类群迹 $Q_0=\operatorname{Tr}_{F[\ell]/L}P[\ell]$。
基层迹因固定 $E$ 的解析秩至少二而为扭点；用与 $p$ 互素的
整数杀掉它，得指定的原整数范数零点 $Q$。若这个 $Q$ 非扭，
则范数一簇 $A$ 的 $\mathcal O=\mathbb Z_p[\zeta_p]$ 格秩一、
Sha 有限。写 $Q=\delta^a\varepsilon w$。

**无需对负扭曲 $E^F$ 作秩一或 Sha 假设**，仍有
$$
 Q\notin\delta^2(A(F)\otimes\mathbb Z_p)
 \quad\Longrightarrow\quad
 \operatorname{rank}E(\mathbb Q)=2,\quad
 \Sha(E/\mathbb Q)[p^\infty]=0.
$$

## 完整证明

[完整证明](../notes/2026-11-12-noncm-two-step-criterion-with-varying-heegner-field.md)。

1. $\ell$ 处 $H^1(F_\ell,E[p])=0$；其余位实际 MW 范数
   满射，包括 $p$ 处不分歧形式群及 $389$ 处的 $I_1$ Tate
   参数。Kummer 图给通常 $\operatorname{Sel}_\delta(A/F)
   =\operatorname{Sel}_p(E/F)$。
2. 原完整类群诱导族的首项是 $\delta Q$，Howard 弱 stub
   给 $\operatorname{length}_{\mathcal O}S\le2(a+1)$。
3. 有限 Cassels–Tate 原始层中，奇长度块的两个符号数目
   相等，偶长度至少二。逐层即得
   $\operatorname{length}S\ge2\dim S[\delta]^+$，不需要
   知道负号部分。
4. 真实 Heegner 共轭和 Kummer 反号给 MW 线符号 $(-1)^a$。
   因此 $\dim S[\delta]^+=r+d_+-\mathbf1_{a\text{ 偶}}$，
   其中 $d_+=\dim\Sha(E/\mathbb Q)[p]$。对 $a=0,1$ 两种
   情形分别比较上下界，均得 $r=2,d_+=0$。

## 范围

本结果移除了负扭曲的低秩输入，未证明变化 $F$ 后实际完整
类群迹非零，也未证明 $a\le1$。这些条件须在同一个实际
$F,p,\ell,Q$ 上同时支付。目标椭圆曲线始终是固定的 E389。
