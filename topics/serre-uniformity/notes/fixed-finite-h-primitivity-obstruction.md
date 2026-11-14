# 固定有限个正本原标签的算术限制

本注记只处理 [R727](../results/R727-other-primitive-embeddings-toric-norm-and-original-M2.md) 中
$h>1$、$h\equiv1\pmod6$ 的实际本原标签。它说明一个固定有限的此类标签集合不能单独覆盖所有允许素数；没有断言任何实际 Cartier 系数为零。

## 命题

任取有限个固定整数

$$
h_1,\ldots,h_t>1,\qquad h_i\equiv1\pmod6.
$$

在允许的两个素数类 $p\equiv2,5\pmod9$ 中，每一个类都各有无穷多个素数 $p$，满足

$$
p>\max_i h_i+4,\qquad h_i\mid p+1\quad(1\le i\le t).
$$

特别地，对于每一个这样的 $p$，全部固定标签 $h_i$ 都不满足
$\gcd(h_i,p+1)=1$。若 $\theta$ 的阶为 $p+1$，则全部
$\theta^{h_i}$ 都不是阶 $p+1$ 的本原角色。

## 证明

令

$$
H=\prod_{i=1}^t h_i.
$$

因为每个 $h_i\equiv1\pmod6$，所以 $\gcd(H,6)=1$，进而
$\gcd(H,18)=1$。分别取 $b=5$ 和 $b=11$。中国剩余定理给出一个模
$18H$ 的剩余类 $a_b$，满足

$$
a_b\equiv-1\pmod H,\qquad a_b\equiv b\pmod{18}.
$$

其与模数互素：第一条同余给出 $\gcd(a_b,H)=1$，第二条同余和
$\gcd(b,18)=1$ 给出 $\gcd(a_b,18)=1$，因此

$$
\gcd(a_b,18H)=1.
$$

Dirichlet 等差数列素数定理遂给出无穷多个素数
$p\equiv a_b\pmod{18H}$。删去有限个小素数后，可同时要求
$p\ge41$ 和 $p>\max_i h_i+4$。

当 $b=5$ 时，$p\equiv5\pmod9$；当 $b=11$ 时，
$p\equiv2\pmod9$。两种情形下 $p$ 都是奇数且 $p\equiv5\pmod6$，
因此与本课题的实际同余类和奇偶条件相容。
另一方面，$p\equiv-1\pmod H$ 给出 $H\mid p+1$，从而每个
$h_i\mid p+1$。于是

$$
\gcd(h_i,p+1)=h_i>1,\qquad
\operatorname{ord}(\theta^{h_i})
=\frac{p+1}{\gcd(h_i,p+1)}
=\frac{p+1}{h_i}<p+1.
$$

这证明了命题。这里唯一调用的外部定理是 Dirichlet 的等差数列素数定理；
原文可见下列扫描件。$\square$

## 结论的准确范围

本命题排除了“预先固定有限个 $h>1$、仅用这些标签的本原分量覆盖全部允许素数”
这一方案。它没有排除随 $p$ 选择 $h=h(p)$，也没有排除把始终本原的
$h=1$ 与有限个其他标签结合使用。特别地，命题中的素数上可能仍有
$h=1$ 的实际单位判据成立；这里没有计算或断言
$C_p$、$C_{p-3}$ 或任一 R727 配对系数的消失。

## 原始文献

P. G. Lejeune Dirichlet,
*Beweis des Satzes, dass jede unbegrenzte arithmetische Progression, deren erstes Glied und Differenz ganze Zahlen ohne gemeinschaftlichen Factor sind, unendlich viele Primzahlen enthält*
(1837):
[原文扫描](https://www.e-rara.ch/download/pdf/5688045.pdf)。
