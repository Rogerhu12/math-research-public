# R122：有限范数一 Sha 的 δ 层与实际局部符号

日期：2026-11-12。状态：已证明。

固定 R119 的实际范数一阿贝尔簇 $A/F$、
$\mathcal O=\mathbf Z_p[\zeta_p]$、平衡一致化元
$\delta=\tau^{(p-1)/2}(\tau-1)$，以及指定 Heegner 点
$Q=\delta^ave$。记 $S=\Sha(A/F)[p^\infty]$，它已知有限。

整反自对偶同构 $\iota:A\simeq A^\vee$ 将 Cassels--Tate 配对
变成对称完美配对 $B$，满足
$$
 B(\delta x,y)=-B(x,\delta y),\qquad B(cx,cy)=-B(x,y).
$$
在精确长度商
$$
 P_n=S[\delta^n]/(S[\delta^{n-1}]+\delta S[\delta^{n+1}])
$$
上，$\beta_n(x,y)=B(x,\delta^{n-1}y)$ 是非退化
$\mathbf F_p$ 配对。$n$ 奇数时它对称且 $c$ 反等距；
$n$ 偶数时它交替且 $c$ 等距。因此 $S[\delta]^-=0$ 强迫
$$
 S\simeq\bigoplus_{n\ge1}(\mathcal O/\delta^{2n})^{2m_n}.
$$

令 $s_\pm=\dim\operatorname{Sel}_p(E/F)^\pm$，
$r_\pm$ 为通常 Selmer 群在实际辅助位 $\lambda\mid\ell$
的局部像维数。当地两个符号空间各为二维对称双曲平面，
只有通常、横截两条等零线。Poitou--Tate 给准确公式
$$
 \dim\operatorname{Sel}_\delta(A/F)^\pm=s_\pm+1-2r_\pm.
$$
$\delta$-Kummer 映射反 $c$ 号，故实际 MW 线的 Selmer 符号为
$(-1)^a$，并有
$$
 \dim S[\delta]^\pm
 =s_\pm+1-2r_\pm-\mathbf1_{\{\pm=(-1)^a\}}.
$$

R103 给充分大 $p$ 时 $s_-=1$、$s_+=2+d_p$，其中
$d_p=\dim\Sha(E/\mathbf Q)[p]$，未假设基曲线 Sha 有限。
所以 $r_-=1$ 迫 $a$ 偶数、$S[\delta]^-=0$，并得到上述
偶长度、偶重数分解。若同时 $r_+=1$，则
$$
 \dim S[\delta]^+=d_p,\qquad
 2d_p\le\operatorname{length}_{\mathcal O}S,
 \qquad v_p\#S\equiv0\pmod4.
$$
结合 R125 的整系统上界可再得 $d_p\le a$。
R121 已支付密度一的 $r_+=1$；R126 为无穷多个实际输入同时
支付 $r_+=r_-=1$，但这些结论仍不迫使指定点的 $a=0$。

完整的良定义、radical、非退化、局部符号和实际 Kummer 反号证明：
[工作证明](../notes/2026-11-12-finite-norm-sha-delta-layers-and-local-signs.md)。
外部有限性输入为 Nekovář（2007）Theorem 3.2、§3.5.1，
[原文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)；
整同源及局部结构见 R113，实际点有限性见 R119。
