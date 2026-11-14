# R178. 原两条 theta 行的 AS 初始源与完整一层 p 改良

日期：2026-11-12。**状态：已证明；主目标尚未完成。**

## 结论

始终保留原来的 $\mathcal A=A_{17}(2z)/16$ 与 $B$，
不将辅助 $a,b$ 源免费换回。
对惰性 $p\ge7$、$p\ne11$，置

$$
r=(p+1)/4,\quad R=r(p-1),\quad
\varpi^R=p,\quad\lambda=\varpi^r,\quad\gamma=\varpi^p,\quad c_0=374.
$$

真实原源多项式 $\mathcal C=B-\mathcal A+22\mathcal A^2$
在辅助 $X=a-1,Y=b$ 中首项为 $374XY^2$。
其 canonical 缩放约化满足

$$
c^p+\bar c_0^{\,p-1}c y^{2p-2}
-\bar c_0^{\,p}\tau y^{r+2p}=0,\qquad
y=\overline{\mathcal A/\gamma},\qquad
c=\overline{\mathcal C/(\lambda\gamma^2)}.
$$

对任意 $\widetilde\tau\in\mathbb Z_p^\times$ 提升 $\tau$，
存在 primitive 元

$$
\mathcal P_p\in\mathbb Z_p[\mathcal A,B]_{\le(5p-1)/2},
\qquad [B^p]\mathcal P_p=1,
$$

其准确初始式为

$$
\mathcal C^p+p c_0^{p-1}\mathcal C\mathcal A^{2p-2}
-c_0^p\widetilde\tau\mathcal A^{r+2p}.
$$

三项的规范权均为 $\Omega=p(r+2p)$，而沿同一完整实际曲线

$$
\boxed{\quad
\frac{\mathcal P_p(\mathcal A(\gamma T),B(\gamma T))}
{\lambda^p\gamma^{2p}}
\in p\mathcal O_{\mathbb Q_p(\varpi)}[[T]].
\quad}
$$

这是全深度的一层 $p$，不只是一层 $\varpi$。

## 完整证明和实际次数

$Z=\mathcal C/\mathcal A^2$ 在原完成邻域中整且正则，
$Z_X(0)=374,\mathcal A_Y(0)=1$，故 $(\mathcal A,Z)$ 为整形式坐标。
把真实 $c_0^p(U^p+pU-\widetilde\tau V^r)$ 写入这些坐标，
在 $\mathbb Z_p[[\mathcal A]]$ 上对 $Z$ 作 Weierstrass 准备，
得到首一 $p$ 次多项式 $\mathscr W_p$ 和整单位因子。
实际 $G+TG^p\equiv\tau\pmod p$ 保证
$\mathscr W_p/\lambda^p$ 的值已在 $p\mathcal O'[[T]]$。

将 $\mathcal A$ 次数截到 $J=2r-1$，遗漏权至少
$2pr>pr+R$，再取

$$
\mathcal P_p=\mathcal A^{2p}
\mathscr W_{p,J}(\mathcal A,\mathcal C/\mathcal A^2).
$$

逐项清分母后原总次数至多 $2p+J$，$B^p$ 系数仍为一。
系数只要求在 $\mathbb Z_p$，没有声称是固定有理多项式。

全文、全部估值及原始来源见
[完整证明](../notes/2026-11-12-original-theta-as-source-and-integral-correction.md)。
所用完备局部环 Weierstrass 定理见
Mel Hochster, *The structure theory of complete local rings*，
2026 年网页版本，pp. 14–15；正文另给本题逐层构造。

## 范围

辅助 $ab$ 源有次数 $2p-2$ 的对应改良；
原源的 $(5p-1)/2$ 次数与 $\gamma^{2p}$ 已明确支付。
新多项式不会自动保留给定的准确消失前缀，
尚须将其与余项共同放入原饱和前缀矩阵。
本文未证明原中央导数无穷次非零或 R159 的严格总预算。
