# R130. 任意好约化型的半局部形式参数二次增广证书

日期：2026-11-12。**已证明；实际证书的无穷非零性仍开。**

完整证明见[半局部形式参数与二次增广测试](../notes/2026-11-12-semilocal-formal-parameter-second-augmentation-test.md)。

固定实际 $L/F$、$\Gamma=\langle\tau\rangle=C_p$ 及范数零非挠
Heegner 点 $Q$，沿用
$A(F)\widehat\otimes\mathbb Z_p=\mathcal O w$、
$Q=\delta^a\varepsilon w$。设 $p\ge7$、$p\ne17$；不要求
ordinary，也不要求 $p$ 在 $F$ 或 $\mathbb Q(i)$ 分裂。

对 $v\mid p$ 令 $f_v=[k_v:\mathbb F_p]\in\{1,2\}$，
$s_v=\operatorname{Art}_{L/F}(v)$，置
$$
D_p=\prod_{v\mid p}(s_v^2-a_{p^{f_v}}s_v+p^{f_v}),
\qquad R=D_pQ.
$$
真正的有限域 Frobenius 特征式使 $R$ 在所有 $p$ 处 formal。
$a_p$ 偶及 Hasse 界给 $D_p\in\mathbb Z_p[\Gamma]^\times$，
故实际指数仍为 $a$。

设 $\mathcal P=\mathcal O_L\otimes\mathbb Z_p$，保留所有完成及
$\Gamma$ 对它们的置换。则
$$
\mathcal P\simeq(\mathcal O_F\otimes\mathbb Z_p)[\Gamma],
\qquad I=\ker N_\Gamma=(\tau-1)\mathcal P.
$$
若 $p$ 在 $F$ 惰性，它在 $L/F$ 完全分裂，
$D_p=\#E(\mathbb F_{p^2})$；若在 $F$ 分裂，两 Artin 元
为 $s,s^{-1}$，无论它们为 $1$ 或生成元，上式均成立。

形式对数的直接系数界给
$$
z_R=\log_E(R)/p\in I,
\qquad z_R\equiv t_E(R)/p\pmod{p\mathcal P},
\qquad t_E=-x/y.
$$
整数群环元
$\mathcal D_2=\sum_{j=0}^{p-1}\binom j2\tau^j$
满足
$$
\mathcal D_2\equiv\tau^2(\tau-1)^{p-3}\pmod p,
\qquad
\ker(\mathcal D_2:I\to\mathcal P/p\mathcal P)=\delta^2I.
$$
因此下列实际值只需所有 $p$ 处参数模 $p^2$：
$$
\mathcal T_{2,p}(Q)=
 \sum_{j=0}^{p-1}\binom j2\frac{t_E(\tau^jD_pQ)}p
              \pmod{p\mathcal P}.
$$
若 $a\ge2$，完整整数点可写 $Q=\delta^2S$，同一 $D_p$
使 $S$ formal 后证明该值为零。结合 R122/R125 的有限 Sha
长度与符号公式，删去固定有限多个负扭曲 Sha 坏素数后得到
$$
\boxed{\mathcal T_{2,p}(Q)\ne0
       \ \Longrightarrow\ a\le1
       \ \Longrightarrow\ \Sha(E/\mathbb Q)[p^\infty]=0.}
$$

R123 的普通密度一输入和 R126 的任意约化型无穷输入都可用
这一测试。整个局部范数零群上的该行不是零行，已有显式整
正规基证书；这不等于已经证明实际 $Q$ 的测试非零。
其无穷非零性仍是新的全局输入，未由局部 norm coherence
或 $Q$ 非挠代替。
