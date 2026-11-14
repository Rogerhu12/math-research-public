# R181：原 monic 修正源的共同除法与累计饱和 jet 收益

**状态：已证明。**

对 R180 的实际 $\mathcal P=\mathcal P_{p,n}$，保留原
$E_D=\mathbb Z_p[A_2,B]_{\le D}$。
其 monic 伴随矩阵给完整原源像
$\operatorname{span}\{A^aM_B^be_0:a+b\le D\}$，与原源整等距且
$p$ 饱和。支撑准确满足
$l+(J_n+2)i+p(J_n+2)q\le(J_n+2)D$；没有免费保持次数 $D$。

所有前缀行是同一像上的 $A^lC^i\mathcal P^q$ 卷积矩阵。
已知的实际延迟为 $\operatorname{ord}\mathcal P\ge d+1$，
$d=D_{p,n}$；商和余项不各自置零。

定义实际局部格

$$
\mathscr L_t=E_D+\sum_{q=1}^t p^{-(n+8)q}\mathcal P^qE_{D-qd},
\qquad I_t=(n+8)\sum_{q=1}^t\binom{D-qd+2}{2}.
$$

则 $[\mathscr L_t:E_D]=p^{I_t}$。同一完整 rational jet 旗标的
全部非零 jump 满足准确式

$$
\sum_i\log\|r_{k_i}\|_{E_D}
=\sum_i\log\|r_{k_i}\|_{\mathscr L_t}-I_t\log p
\le\bigl(\sum_i e_p(k_i)-I_t\bigr)\log p.
$$

此累计收益不要求各个修正块单独保前缀；第 $q$ 步的指数只由
$k_i\ge q(d+1)$ 的真实商承担。所有系数仅需属于 $\mathbb Z_p$，
仍是原源的局部格，非新增全局有理多项式族。

现有精度—次数比只给 $I_t=O(D^3/p)$，全 prime 总规模至多
$O(D^3\log D)$，不足以改变 $D^4$ 级完整斜率主项。
即使合并 R183 全族及其乘积，按各自已付次数相加计费的共同格
仍包含于 $p^{-\lfloor pD/R\rfloor}E_D$，其指数同阶；这不排除
额外高次项相消降低真实次数。
严格门及两完整中央条件带来的进一步收益仍未支付。

完整证明：
[原 monic 修正源的共同除法、真实前缀矩阵与累计旗标收益](../notes/2026-11-12-actual-monic-source-division-and-saturated-flag-gain.md)。
