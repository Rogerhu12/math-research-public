# R271 附录：六位一特殊权的完整 S1 与同源精度裕量

- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 范围：原六位权 $b=(\sqrt t,1,1,1,1,1)$，$t>0$；同一出生二上来源和出生一下来源。
- 续 [完整 S2 与原平方迹门反例](R271-appendix-six-site-one-special-weight-full-s2-and-sharp-trace-square-budget.md)。只证明下面新的原联合来源界，不重登记已知两异权全出生相邻定理。

## 1. 原同源结论

完全使用 [R275 的 S1 定义](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md)：
$
K=\ker d_2,\quad L=\ker d_1,\quad
G_j=P_KF_{j,2}^{-1}|_K,\quad L_j=P_LF_{j,1}^{-1}|_L,
$
$
C_1=G_1^{-1},\quad C_2=G_2^{-1},\quad
F=C_1^2-C_2,\quad B=d_{b^3}|_K,
$
$
\Delta=\frac12(C_1B^*L_3-B^*L_2).
$
所有 Gram 使用原物理伴随，先完整求逆再限制源。六位出生二高度为二，$G_2$ 是真正合法最高层，不能用五位硬端约定把 $C_2$ 改成零。

对每个 $t>0$，
$
\boxed{\quad
F>\frac23C_1^2,\qquad
0\le\Delta L_3^{-1}\Delta^*<\frac19F.
\quad}
\tag{1.1}
$
因此原完整 S1 块严格正：
$
\begin{pmatrix}F&\Delta\\\Delta^*&L_3\end{pmatrix}>0.
\tag{1.2}
$
常数 $1/9$ 是本文已付的一致上界，不声称最佳。

## 2. 真实标准两复制上的最高 Gram

沿用前篇的物理去权坐标。若 $\sum_{i=1}^5u_i=0$，二孔标准两复制写为
$
f_{0i}=a u_i,\qquad f_{ij}=c(u_i+u_j).
$
其真实度量为 $\operatorname{diag}(t,3)\|u\|^2$，下降行和 primitive 方向为
$
R=(t,3),\qquad v=(3,-t).
$
前篇已从完整上第一 Gram 得到
$
G_1=\frac{t+1}{t+3},\quad C_1=\frac{t+3}{t+1},\quad
BB^*=\frac{3t(t-1)^2}{t+3}I_4,
$
并在同一个低标准块得到
$
L_2=\frac1{3(t+1)},\qquad L_3=\frac1{3t+1}.
\tag{2.1}
$

这里补上真正最高层 $G_2$，不以普通逆替代压缩逆。
四孔标准两复制为特殊位加尾三孔、及纯尾四孔；
相应真实度量是 $\operatorname{diag}(3t,1)\|u\|^2$。
在这两个完整层之间，
$
d^2/2=
\begin{pmatrix}3&0\\2t&1\end{pmatrix},\qquad
(d^2/2)^*=
\begin{pmatrix}1&2\\0&3\end{pmatrix}.
\tag{2.2}
$
第二矩阵是按两端所列真实度量取的伴随。因此完整正 Gram 为
$
F_{2,2}=\begin{pmatrix}3&6\\2t&4t+3\end{pmatrix},
\quad
\det F_{2,2}=9,
\quad
F_{2,2}^{-1}=\frac19
\begin{pmatrix}4t+3&-6\\-2t&3\end{pmatrix}.
\tag{2.3}
$
全部求逆之后才压到 $v$。因
$F_{2,2}^{-1}v=(2t+1,-t)$、$\|v\|_{\rm phys}^2=3t(t+3)\|u\|^2$，
得到
$
G_2=\frac{3t+1}{t+3},\qquad C_2=\frac{t+3}{3t+1}.
\tag{2.4}
$

## 3. 同一标准块的原创新费用

由 (2.1)、(2.4)，
$
F=\frac{2(t+3)(t^2+4t+1)}{(t+1)^2(3t+1)}.
\tag{3.1}
$
原来相减的两个来源给
$
\Delta
=\frac12B^*\left(\frac{t+3}{(t+1)(3t+1)}
-\frac1{3(t+1)}\right)
=\frac{4B^*}{3(t+1)(3t+1)}.
\tag{3.2}
$
因此没有丢掉创新的交叉项，准确有
$
\Delta L_3^{-1}\Delta^*
=\frac{16t(t-1)^2}{3(t+3)(t+1)^2(3t+1)}I_4,
$
以及同一上标准块的相对费用
$
\frac{\Delta L_3^{-1}\Delta^*}{F}
=\frac{8t(t-1)^2}{3(t+3)^2(t^2+4t+1)}.
\tag{3.3}
$
这里标量比只因为已证明的标准约化块是标量，未假设一般来源可交换。

完整正余量身份为
$
\begin{aligned}
&(t+3)^2(t^2+4t+1)-24t(t-1)^2\\
&\hspace{1em}=t^2\bigl((t-7)^2+33\bigr)+18t+9>0.
\end{aligned}
\tag{3.4}
$
它恰给 (3.3)$<1/9$。

另一方面，
$
\frac{F}{C_1^2}
=\frac{2(t^2+4t+1)}{(t+3)(3t+1)}
=\frac23+\frac{4t}{3(t+3)(3t+1)}
>\frac23.
\tag{3.5}
$

## 4. 其余五维上 primitive 来源

前篇的完整分解还含一个五维纯尾二孔 primitive 块 $K_{\rm tail}$。
每一尾行和为零，特殊位置坐标为零，因此在该块
$
d_{b^3}=d_{\rm tail}=0,\qquad B=0,\qquad\Delta=0.
$
这个块的等权五尾出生二链高度是一。加入特殊位以后，完整第一、第二 Gram 在该块分别是
$
F_{1,2}=t+1,\qquad F_{2,2}=t.
$
可直接由尾交换关系
$[d_{\rm tail},d_{\rm tail}^*]=(5-2\cdot2)I=I$
在尾 primitive 上核验：尾上升一次的范数系数为一，再上升一次为零；
两步完整上升必须各用一次尾和特殊位，除以 $2!$ 后系数平方为 $t$。
该尾型在二孔层只出现一次，故完整 Gram 的逆也在同一块内。

于是
$
C_1=t+1,\qquad C_2=t,\qquad
F=t^2+t+1,
$
且
$
\frac{F}{C_1^2}
=1-\frac{t}{(t+1)^2}
\ge\frac34>\frac23.
$
没有遗漏该五维来源，也没有将它合并到四维标准块。
与 §3 合并便得到全九维 $K$ 上的 (1.1)；
再对真正正定的 $L_3$ 作 Schur 补，得到 (1.2)。

## 5. 与已知相邻定理的区别及下一原范围

本篇证明的是原 S1 的联合费用，保留完整 $C_2$、同一 $B$ 和原创新中的相减；
一般相邻不等式本身不自动给 (1.1)。
与前篇完整 S2 联合后，这个一特殊权旧六位来源的两条无参数充分式均已付。

[旧 R239 全出生倒数权对偶 §6](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)
已经引用并使用两异权全出生定理，对两个任意特殊权加等权池给出更强的既有相邻界。
因此不把从本篇再加一位推出的两异权七位相邻性另算新结论，
也不登记较弱的重复常数。

六个任意独立正权的完整 S1、S2，以及一般更高出生的联合来源，仍未由本篇支付。
本篇不外推到原无限 carry、未知 $W$ 或普通 ISP 的完成标准。
