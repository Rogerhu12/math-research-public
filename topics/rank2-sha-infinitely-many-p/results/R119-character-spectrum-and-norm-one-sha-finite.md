# R119. 实际环类角色全谱与范数为零阿贝尔簇的 Sha 有限性

日期：2026-11-12。状态：已证明。

完整证明见
[角色谱与整增广指数笔记](../notes/2026-11-12-character-heegner-spectrum-and-norm-one-finiteness.md)。

固定 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$。
对 R116 的实际合法 $(p,\ell)$，令 $H=F[\ell]$，$L/F$ 为其
次数 $p$ 子扩张，$\Gamma=\operatorname{Gal}(L/F)$，
$$
Q=\operatorname{Tr}_{H/L}P[\ell],\qquad
\mathcal A=\ker(\operatorname{Res}_{L/F}E_L\xrightarrow{N}E).
$$
只要 $Q$ 非扭（R116 对相对密度一的目标 $p$ 已能选到），则：

1. $\mathbb Q[\Gamma]Q\simeq\mathbb Q(\zeta_p)$，故每个非平凡
   $\chi:\Gamma\to\mu_p$ 的未正规化 Heegner 投影 $P_\chi$ 都非零。
2. 每个 $L'(1,E/F,\chi)>0$，并有指定子族的精确第一矩
   $$
   \widehat h_F(Q)=
   \frac{\deg\pi\sqrt{15}}{8\pi^2(f_E,f_E)}
   \frac{\ell}{p^2}\sum_{\chi\ne1}L'(1,E/F,\chi).
   $$
3. $\operatorname{rank}\mathcal A(F)=p-1$，
   $\operatorname{rank}E(L)=p+2$，且整个 $\Sha(\mathcal A/F)$ 有限。

第 3 条使用已出版的 Nekovář（2007），Theorem 3.2。
其条件并非排除所有 CM 曲线，而是排除曲线在角色域内的虚二次域上
获得 CM。本题 $\mathbb Q(i)$ 在 $2$ 分歧，$F[\ell]$ 在 $2$ 未分歧，
故条件满足。定理使用整本征子模，且 §3.5.1 处理每个系数素理想，
包括 $p=\operatorname{ord}\chi$。

从角色 Sha 回到 $\mathcal A$ 时，证明使用整恒等式
$\sum_{\chi\ne1}e_\chi=p-N_\Gamma$ 及固定指数 Selmer 有限性；
没有在 $\mathbb Z_p[\Gamma]$ 中擅自除 $p$。

现在实际 Mordell–Weil 格在 $\mathcal O_p=\mathbb Z_p[\zeta_p]$
上秩一，可写 $Q=\delta^a\varepsilon w$，
$\delta=\zeta_p-1$、$\varepsilon$ 为单位。R116 给 $0\le a\le p-2$；
主目标仍需要无穷 $p$ 的某个实际选择满足 $a=0$。
有限的 $\Sha(\mathcal A/F)$ 可以有非零 $\delta$-挠部分，
而 $\mathcal A$ 随 $(p,\ell)$ 改变；本结果不证明固定
$E/\mathbb Q$ 的 Sha 初级有限性。
