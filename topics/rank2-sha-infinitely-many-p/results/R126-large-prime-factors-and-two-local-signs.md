# R126：大素因子给单一曲线的无穷双局部非零与 o(p) 高度

日期：2026-11-12。状态：已证明；主课题的最终增广原始性仍未完成。

对固定
$$
 E:y^2=x^3-17x,\qquad F=\mathbf Q(\sqrt{-15}),
$$
存在无穷多个不同的好素数 $p$，各有合法辅助素数 $\ell$，令
$$
 p=P^+(\ell+1),\quad \ell+1=pu,\quad v_p(\ell+1)=1,
 \qquad Q_{p,\ell}=\operatorname{Tr}_{U}(1+\tau_3)P[\ell],\quad |U|=u,
$$
则这个**实际完整 Heegner 迹**同时满足
$$
 Q_{p,\ell}\ne O,\qquad Q_{p,\ell}\notin pE(F[\ell]),
 \qquad r_+=r_-=1,
 \qquad \widehat h(Q_{p,\ell})\ll p^{666/667}\log p=o(p).
$$
这里 $r_\pm$ 是通常 Selmer 群在 $\lambda\mid\ell$ 的两个
复共轭符号局部像维数。输入 $p$ 不需普通或在 CM 域、$F$ 分裂。
至 $p\le X$ 可得到 $\gg X^{667/1000}/\log X$ 个不同输入；
不声称它们有正密度或属于一个指定分裂类。

## 证明的新增部分

Fouvry（1985）Theorems 1、3 及印 p.386 的固定同余类说明，
配合 Fouvry--Tenenbaum（1996）§3.4 的勘误，给任意固定 $B$：
$$
 \#\{\ell\le X:\ell\equiv-1\pmod B,\ \ell\text{ 素},
               \ P^+(\ell+1)>X^{667/1000}\}\gg_B X/\log X.
$$
准确的主项密度是 $1/\varphi(B)$；大素因子 $p>B$ 自动与 $B$
互素。所需筛法积分有严格上界
$$
 0.06436+\frac{14}{13}\log\frac{815}{672}
                 +8\log\frac{2400}{2333}<0.498641<\frac12.
$$
[纯有理数脚本](../scripts/check-fouvry-corrected-integral.py)
通过显式对数级数尾界认证此不等式。

取 $B$ 含 R116 的固定非零进程 $C$、$1020$，且大于其阈值。
于是 $B\mid u$，$u\le U=O(X^{333/1000})$。真正坏候选由三个
非零整数乘积吸收：

- R116 的完整迹首系数乘积：对数 $O(U^2\log U)$；
- R121 的两个固定有理点分母方格：对数 $O(U^2)$；
- 固定负扭曲点 $(121,1144)$ 的 $[n]$ 分母乘积，$n\le U$：
  对数 $O(U^3)$。

最后一项也只排掉 $O(X^{999/1000}/\log X)=o(X/\log X)$ 个
辅助素数，故三条件可同时满足。高度估计使用真实 $u$ 项整数迹，
给 $u^2\log\ell\ll p^{666/667}\log p$，不使用除阶后的有理点。

## 整 Selmer 后果及准确剩余缺口

R119 给相应范数一阿贝尔簇 $A/F$ 的秩为 $p-1$、整个 Sha 有限。
写
$$
 A(F)\otimes\mathbf Z_p=\mathcal Oe,\quad
 Q=\delta^ave,\quad \mathcal O=\mathbf Z_p[\zeta_p],\quad v\in\mathcal O^\times.
$$
实际 $o(p)$ 高度与二次 Gauss 算子、Baker 的固定正高度下界给
$a\le(p-3)/2$。R122 的两符号配对给 $a$ 为偶数及
$2d_p\le\operatorname{length}_{\mathcal O}\Sha(A/F)[p^\infty]$；
R125 的整 Kolyvagin 上界给该长度至多 $2a$。因此
$$
 \boxed{d_p\le a\le(p-3)/2,\qquad a\equiv0\pmod2},
 \qquad d_p=\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].
$$
这些结论仍允许 $a=2$；没有证明指定点的 $a=0$，因而未将
无穷多个局部证书误写为已完成的 Sha 有限性结论。

完整证明及原文定位：
[工作证明](../notes/2026-11-12-fixed-progression-large-factors-and-two-local-signs.md)。
关键一手来源为
[Fouvry（1985）原刊](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0079/LOG_0027.pdf)
和 [Fouvry--Tenenbaum（1996）作者修正版](https://tenenb.perso.math.cnrs.fr/PPP/RepStatS(x,y).pdf)。
