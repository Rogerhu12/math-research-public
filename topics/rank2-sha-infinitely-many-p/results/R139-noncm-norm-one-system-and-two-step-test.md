# R139. 非 CM 范数一系统的实际额外 delta 与两步 Sha 证书

日期：2026-11-12。**已证明的定量与充分条件。**

完整证明见
[非 CM 范数一 Euler 族与两步测试](../notes/2026-11-12-noncm-norm-one-system-and-two-step-test.md)。

固定 R136 的
$$
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7}),
 \qquad r=\operatorname{rank}E(\mathbb Q)\ge2.
$$
删去固定有限例外后，取 R138 的实际大素因子输入
$$
 \ell\text{ 在 }F\text{ 惰性},\quad
 \ell+1=pu,\quad p\nmid u,\quad
 0<|a_\ell(E)|<p,\quad a_p(E)\not\equiv0,\pm1\pmod p.
$$
令 $L/F$ 为 $F[\ell]$ 中的唯一次数 $p$ 子域，
$\Gamma=\langle\tau\rangle$，使用原完整迹
$$
 Q=\operatorname{Tr}_{F[\ell]/L}\pi(x_\ell).
$$
假定该实际点非扭。R136 的基层点为 $O$，故 $N_\Gamma Q=0$。
置
$$
 A=\ker(\operatorname{Res}_{L/F}E\xrightarrow N E),\quad
 \mathcal O=\mathbb Z_p[\zeta_p],\quad
 \delta=\tau^{(p-1)/2}(\tau-1).
$$
Nekovář 的整角色定理给 $A(F)\otimes\mathbb Z_p=\mathcal O w$
以及整个 $\Sha(A/F)$ 有限；令 $Q=\delta^a\varepsilon w$，
$\varepsilon\in\mathcal O^\times$。

## 实际定量结论

有有限 $\mathcal O$ 模 $M$ 使
$$
 \boxed{\quad
 S:=\Sha(A/F)[p^\infty]\simeq M\oplus M,\qquad
 \operatorname{length}_{\mathcal O}M\le a+1.
 \quad}
$$
此处的 $+1$ 必须保留。高层原族满足
$N_\Gamma Y_n=a_\ell P[n]$；真实范数零族是
$Z_n=(\tau-1)Y_n$，其 leading 为 $\delta Q$ 的单位倍。
原族的 augmentation 未知为零，故不能照 CM 情形把整族再除
一层 $\delta$。有限—奇异比较使用真实局部可逆矩阵
$-q\varphi_q^{-1}\otimes1$，不把全局复共轭当作群环线性算子。

辅助位有
$$
 H^i(F_\ell,A[\delta^j])=0\qquad(i=0,1,2;\ j\ge1),
$$
因为 $\#E(\mathbb F_{\ell^2})\equiv-a_\ell^2\ne0\pmod p$。
其余地方的真实范数/Kummer 比较（包括 $389$ 的 split $I_1$）给
$$
                   \operatorname{Sel}_\delta(A/F)
                     =\operatorname{Sel}_p(E/F).
$$
写 $d_p=\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]$。
负七扭曲的秩一和有限 Sha，配合整 Cassels–Tate 原始层，给
$$
 \operatorname{length}_{\mathcal O}S\ge
 \begin{cases}
 2r+2d_p-2,&a\text{ 偶},\\
 2r+2d_p,&a\text{ 奇}.
 \end{cases}
$$
因此
$$
 \boxed{\quad
 Q\notin\delta^2(A(F)\otimes\mathbb Z_p)
 \ \Longrightarrow\quad
 r=2,\qquad\Sha(E/\mathbb Q)[p^\infty]=0.
 \quad}
$$
更精确地，$a=0$ 时 $S\simeq(\mathcal O/\delta)^2$；
$a=1$ 时 $S\simeq(\mathcal O/\delta^2)^2$。
所以原曲线的初级部分为零，不要求范数一簇的有限 Sha 也为零。

## 有限半局部充分检验

保留 $\mathcal P=\mathcal O_L\otimes\mathbb Z_p$ 的全部完成。
$p$ 在 $F$ 分裂时，令 $s=\operatorname{Art}_{L/F}(\mathfrak p)$ 并取
$$
 D_p=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p).
$$
$p$ 在 $F$ 惰性时取 $D_p=(p+1)^2-a_p^2$。
这些算子为群环单位，并使 $R=D_pQ$ 在所有 $p$ 处 formal。
对整最小模型参数 $t_E=-x/y$，若
$$
 \boxed{\quad
 \sum_{j=0}^{p-1}\binom j2\,
          \frac{t_E(\tau^jR)}p
       \not\equiv0\pmod{p\mathcal P},
 \quad}
$$
则 $a\le1$，从而原曲线 $\Sha[p^\infty]=0$。
该有限检验本身也推出 $Q$ 非扭。
证明使用 $\log_E(t)/p\equiv t/p\pmod p$ 及真实半局部增广格上
$D_2=\sum\binom j2\tau^j$ 的核恰为 $\delta^2I$；
完全分裂时必须保留全部完成上的置换作用。

R138 的无穷输入并不自动使这个实际行非零。
本结果支付非 CM 的完整系统、局部条件、额外 $\delta$ 成本与
有限充分证书；无穷多个输入的两步原始性仍是主问题的未付条件。
