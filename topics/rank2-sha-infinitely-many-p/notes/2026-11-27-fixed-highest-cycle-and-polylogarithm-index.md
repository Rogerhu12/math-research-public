# 固定最高循环与椭圆 polylog 的实际指标

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

这是 R1009、R1011 后的工作记录，不登记新结果号，也不声称跨素数非零。
本题原目标是

$$
V_{j,\lambda}=\eta_j^{-1}\chi_{27,\ell}^{\,3}\varepsilon_\ell^{-1},
\qquad
H^3(2)\text{ 的原最高直和项}.
\tag{1}
$$

R1011 已将每个好分裂 $p$ 的实际 $54$ 图删项循环写成同一固定
$Y_{j,0}$ 的非零代数倍数。现在考察是否可直接把这个固定来源换成
Deninger--Kings--Bars 的椭圆 polylog 来源。

## 1. 不能用平衡 Tate 重呈现改变的指标

先在纯 Hecke motive 的上同调记号写
$M_{(a,b)}(r)$。本题最高部分的参数为

$$
(a,b,w,r)=(3,0,3,2),\qquad w=a+b.
\tag{2}
$$

有限角色 $\eta_j^{-1}$ 不改变这些 Hodge 指标。Bars 的记号是
$r=w+l+1$，而构造的 Eisenstein symbol 的次数是

$$
m=w+2l=2r-w-2.
\tag{3}
$$

代入 (2) 得

$$
l=-2,\qquad m=-1.
\tag{4}
$$

这不是只选错一个低阶 presentation 的现象。对任何仍代表同一
Tate-twisted CM motive 的平衡重呈现

$$
(a,b,r)\longmapsto(a+t,b+t,r+t),
\tag{5}
$$

有 $w\mapsto w+2t$、$l\mapsto l-t$，故

$$
m\longmapsto (w+2t)+2(l-t)=m=-1.
\tag{6}
$$

此外，原文的另一必要条件 $-l\leq\min(a,b)$，在本题和 (5) 下
分别成为 $2\leq0$ 与 $2+t\leq t$，始终不成立。交换两个 CM
嵌入也不改变最小值。因此有限角色、平衡 Tate 改写及复共轭均不能
把同一原目标移进这个构造的非负 Eisenstein 次数范围。

这是对这里实际构造参数的判断，不排除更广的混合 CM 构造，也不
排除在别的几何对象上直接构造同一 $V_{j,\lambda}$ 的扩张。

## 2. 原文中确实保留的范围

Francesc Bars，*On the Tamagawa number conjecture for Hecke characters*，
[作者全文](https://mat.uab.cat/~francesc/TamagHeckefi.pdf)：

- Theorem 3.1 引用 Deninger 的构造范围；Theorem 3.2 的实际
  Eisenstein symbol 是 $E_M^{2l+w}$。
- §6.2 和 Theorem 6.1 虽处理 $l<0$，仍要求
  $-l\leq\min(a,b)$ 和 $-w-2l\leq-3$，实际源仍是
  $\operatorname{Sym}^{2l+w}h^1(E)$。它不把 $m=-1$ 解释成一个
  椭圆 polylog 层。
- Theorems 6.3--6.4 给行列式形式；将其改写为实际 regulator 像的
  商，需要原文另外保留的注入前提。

Guido Kings，*The Tamagawa number conjecture for CM elliptic curves*，
[原文](https://arxiv.org/pdf/math/0003113)：Theorem 1.1.5 处理
$T_pE(k+1)$、$k\geq0$，regulator 注入还要求 $H^2$ 有限。
§1.1.4 明说不在那里证明这个有限性；Theorem 1.1.7 的量词是固定
$p$ 后对几乎所有 $k$，不能交换为固定本题权重后对无穷多个 $p$。

这里的范围核对也区分两种不同的“临界”：本题纯权 $3$ Hecke
$L$-函数的 $s=2$ 是 Deligne 临界整数；R1006 使用的
$\nu_j$ 的类型 $(-1,2)$ 不在所选 Katz 直接插值锥内，并不把
该复中央点变成 Deninger 非临界 regulator 构造的适用点。

## 3. 既有边界不重复登记

Ogus 实现的既有范围与扩张反例已经记录在
[原 Ogus 工作记录](2026-11-13-ogus-extension-and-adelic-complex-boundary.md)
及
[过滤周期记录](2026-11-12-filtered-period-and-adelic-boundaries.md)。
本次没有将其重新包装成新结论。

Kings 的 polylog 是随 $p^n$ 挠点层增长的 $1$-motive 逆极限；这
与 R1009 排除的“有限组 $1$-motives 经有限张量、对偶、子商所成
的对象”是不同命题。不能因其使用 $1$-motives 就断言所有椭圆
polylog 极限被 R1009 排除；(4)--(6) 是本次对同一最高目标所付的
具体指标检查。

后续仍须直接给固定 $Y_{j,0}$ 的混合扩张跨 $\ell$ 非零，或给
同一原目标的另一实际全局类及其局部非零。这里没有用纯 motive
比较、一个素数的非零或行列式等式代替这个输入。
