# R741 增补 — 完整 F H2 子格的首次障碍单射

日期：2026-11-15。**状态：已证明。**

保持 [R741](../results/R741-specified-noncubic-first-forcing-and-necessary-normal-smoothing.md)
的同一来源、同一个 $F$、(2)–(5) 及原 $J/M$ 目标。
本增补只确定显示子格 $qt^rF\mathcal H_2$；
不包含垂直 $e\mathcal H_2$ 及完整 $\mathcal W_D$ 的其他列。

令
$$
a_\eta=\dim_kK_{\rm mir}-1=\dim\ker\alpha
$$
为 R550 的同一真实连接核维数。则
$$
\boxed{
\operatorname{SNF}(\mathsf M_0|_{qt^rF\mathcal H_2})
=
1^{\,2\kappa+\chi-a_\eta},\quad p^{\,a_\eta+1}.
}
\tag{1}
$$
所有显示来源因子非零，且不存在 $p^2$ 或更高因子。

**证明。**
R495 给 $\mathcal H_2$ 的整自由秩 $2\kappa+\chi+1$；
乘固定 $qt^rF$ 后约化仍单射，所以所得原来源子格在 $p$ 处饱和。
R550 的同一原二 normal 条件表明其首核准确为
$$
qt^rF K_{\rm mir}.
\tag{2}
$$
故单位因子个数为 $2\kappa+\chi-a_\eta$。

对任意 $B\in K_{\rm mir}$，若 $B_0=B|_C=0$，
则 $B=FH_1$，而镜轴条件使
$\operatorname{ord}(H_1|_C)\ge q_T>\kappa$。
因此 $H_1|_C=0$，从而 $B\in kF^2$。
反之，$kF^2$ 显然是这个限制核。

若 $B\notin kF^2$，则非零截面 $B_0$ 的次数至多 $2\kappa$，
R741 的证明逐项适用，给
$$
\rho=\operatorname{ord}B_0-h
\le2\kappa-h<q_T,\qquad
\mathscr V_\eta\beta(qt^rFB)\ne0.
\tag{3}
$$
该证明只用 $B_0\ne0$、镜轴条件和实际整提升，
不需要额外的指定 $UA|_Z$。
R741(18) 同时说明 $\mathscr V_\eta$ 杀整个
$qt^rF\mathcal H_2$ 的首像。
所以 (3) 在这个显示子格的实际首 Bockstein 余核中仍非零。

余下的唯一方向是 $B=cF^2$。
R547/R502 的原 cube 第三块行 $k$
（原 $M$ 为 $13+k$）为单位，
而公共 $t^r$ 来源的整个第三块首像为零。
因此此方向的首 Bockstein 也非零。
这证明首 Bockstein 在 (2) 的全部核上单射。
对有限自由矩阵，这恰给 (1)。证毕。

本证明没有将该子格的首像换为完整原首像。
加入非 $F$-整除列后，R741 的投影等于那些列的实际曲线限制，
可能吸收 (3)；加入垂直单位列时也须如此运输。
因此 (1) 不决定完整原矩阵的 Smith 因子，
更不决定同一个完整修正 $R$ 的存在或原中央非零。
