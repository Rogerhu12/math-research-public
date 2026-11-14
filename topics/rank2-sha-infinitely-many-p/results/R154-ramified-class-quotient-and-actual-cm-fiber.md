# R154 — 固定分歧类群商与真实 F_p 二阶矩纤维

**状态：已证明。日期：2026-11-12。**

对 R153 的每个实际域，令
$X=X_0(389D_0)$、$W_R=\langle w_r:r\in R_D\rangle$。
准确退化关系
$$
 d_dw_r=d_{rd}\ (r\nmid d),\qquad
 d_dw_r=d_{d/r}\ (r\mid d)
$$
给完整 $\Phi_D$、$\Psi_D$ 及权零 $g_{D,p}$ 严格不变。
固定商 $Y_D=X/W_R$ 因此承载原完整类群映射。
原最大阶 CM 中心在商上成为 F 有理点；原类群 h 个项已
包含在映射的一个值中。

若 $\ell\equiv-1\bmod8D_0$，每个 $r\in R_D$ 在模 ell 下
为平方。取 $\lambda_r^2=r$，full ell 标记上的
$\lambda_r^{-1}\phi_r$ 保持 Weil 配对、平方真为恒等，
不同 r 的 lifts 两两交换并与 $\mathrm{SL}_2$ 交换。
显式取中心商后，完整 $\mathrm{PSL}_2$ 覆盖仍连通。

使用全部 determinant 分量的 projective-level 模型，
nonsplit 环面 T 及其阶 u 子群 U 均交换两个几何分量。
因此它们的商在 $\mathbb F_p$ 定义，几何上准确为
$G/T_0$、$G/U_0$，其中
$$
 |T_0|=pu/2,\qquad |U_0|=u/2,\qquad T_0/U_0\simeq C_p.
$$
所得 $C_p$ 覆盖处处 étale。分歧类群商保原 CM Cartan
方向及 389 标记，故原算术源在 $\mathbb F_p$ 上有理；
其纤维 Frobenius 仍为原 $s=\operatorname{Art}_p(L/F)$。

原点严格满足
$$
 Q_D=\operatorname{Tr}_{K_\ell/L}\widetilde\Psi_D(y_\ell)
     =[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell].
$$
这里没有额外 h 倍数。实际 Hecke 行 B 保留两个 $U_0$
轨道，norm 为 $a_\ell(E)\widetilde g_{D,p}$；其原 CM
纤维值仍是
$$
 \epsilon_p\,s(s-\bar a_p(E))\,\bar z_{Q_D},
 \qquad \epsilon_p\in\mathbb F_p^\times.
$$
因此原 $D_2Q_D$ 半局部测试无损转到这个真实纤维。
R153 的源简单零通过 étale 商下降，故 R142 的判据
$$
 \mathscr D=(D_1B)^2-nD_1B-2nD_2B,\qquad n=N_\Gamma B
$$
在原点准确给“整个纤维 $D_2B=0$ 当且仅当
$\operatorname{ord}\mathscr D\ge2$”。

尚未排除这个二重零。到固定商源的度数仍为
$\ell(\ell-1)$，本篇不声称得到只依赖 u 的低次数覆盖，
也不把 Hasse invariant 或源微分框架直接下降。

[完整证明](../notes/2026-11-12-ramified-class-quotient-and-actual-cm-fiber.md)
给实际模等式、归一 lifts、两个 determinant 分量、
原类群和/环面迹及 Frobenius 的逐项比较，并核对
Conrad（2009）附录 A 与 Cais–Conrad（2006 作者版）
的 full-level 原始结论。
