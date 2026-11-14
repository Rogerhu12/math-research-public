# R93：零二阶矩阵的真实几何能量与 frame 长度约束

日期：2026-11-14。状态：**已证明**。下面是完整 $M=0$ 的真实几何必要身份；其推导保留共同右端参数、常值端芽和准确积分分部。它不是第四成本的正性，也不把某一个 profile 的零末值替代整个二阶算子。

## 1. 假设与可提取的两个多项式

取真实有限光滑路径 $s\in[0,L]$，$L>0$，$h>0$，$\omega_s=k_s/(2h)$，首末有常值 scalar germs。假设完整二阶矩阵 $M=0$，并在同一开放物理右尾区间内使用 R85/R88 的 profiles。置

$$z=c+\omega,\quad e=hz-k,\quad Q=1+e^2,$$

$$\lambda=\frac{h_sz-h\omega_s}{h^2},\quad
K=kz^2-\frac{k^2+1}{h}z+\lambda_s,$$

$$\mathcal C(s,c)=\frac{KQ}{8h},\qquad
\mathcal D(s,c)=\frac{Ke}{4}.$$

由 R85 的最低第二系数与 $M=0$，对于该开放区间内每个右端 $c$ 有

$$\int_0^L\mathcal C(s,c)\,ds=0. \tag{1}$$

R88 的下一第二系数以及常值端芽给

$$\int_0^L E_{mm}(s,c)\,ds=0,$$

其中

$$E_{mm}=x_{mm}\partial_c\mathcal C+y_{mm}\mathcal D,
\qquad y_{mm}=-\frac{m^2(3m-5)}{2(2m-3)}\ne0.$$

对 (1) 在同一路径下微分，得到

$$\int_0^L\mathcal D(s,c)\,ds=0. \tag{2}$$

$\mathcal C,\mathcal D$ 对 $c$ 分别是次数至多四、三的真实多项式。因此 (1)(2) 在一个开放区间成立已经迫各个多项式系数积分为零。此处不需要把实际物理区间扩到无穷远，也没有在路径中独立改变右锚。

## 2. 最高两组系数的准确计算

令

$$\ell_h=\left(\frac{h_s}{h^2}\right)_s.$$

因为 $\lambda$ 对 $c$ 的一次项为 $h_s c/h^2$，故

$$K=k c^2+\left(2k\omega-\frac{k^2+1}{h}+\ell_h\right)c+O(c^0).$$

这里 $O(c^0)$ 仅表示多项式常项，不作渐近近似。直接相乘得到

$$[c^4]\mathcal C=\frac{kh}{8},$$

$$[c^3]\mathcal C=\frac{kh\omega}{2}-\frac{3k^2+1}{8}
+\frac{h\ell_h}{8},$$

$$[c^3]\mathcal D=\frac{kh}{4},$$

$$[c^2]\mathcal D=\frac{3kh\omega}{4}-\frac{2k^2+1}{4}
+\frac{h\ell_h}{4}. \tag{3}$$

特别

$$[c^2]\mathcal D-\frac32[c^3]\mathcal C
=\frac{k^2-1+h\ell_h}{16}. \tag{4}$$

每项都是准确系数，不涉及未验证的余密度正规化。

## 3. 零矩阵必要能量与曲率换号

对 (3)(4) 积分，并用 (1)(2)，得到

$$\int_0^Lkh\,ds=0,\qquad
\int_0^L(k^2-1+h\ell_h)\,ds=0.$$

常值端芽给 $h_s(0)=h_s(L)=0$。一次准确分部积分是

$$\int_0^L h\left(\frac{h_s}{h^2}\right)_s ds
=\left[\frac{h_s}{h}\right]_0^L
-\int_0^L\left(\frac{h_s}{h}\right)^2ds.$$

因此

$$\boxed{\int_0^L k^2\,ds
=L+\int_0^L\left(\frac{h_s}{h}\right)^2ds,
\qquad\int_0^Lkh\,ds=0.} \tag{5}$$

特别 $k$ 不可能恒为零。由于 $h>0$ 且 $k$ 连续，第二个身份又迫 $k$ 在该路径上同时取严格正值与严格负值。这是完整 $M=0$ 迫出的真实曲率变化，不能由单一常态替代。

更强地，任何这样的真实光滑路径必满足

$$\boxed{\max_{[0,L]}|k|>1.} \tag{6}$$

否则 (5) 中 $k^2\le1$，迫 $h_s=0$ 以及连续函数 $k^2\equiv1$。连通区间上 $k$ 只能恒取 $+1$ 或 $-1$，与 $h>0$、$\int kh=0$ 矛盾。这项结论不要求额外的 frame 闭合。理想 $\pm1$ 跳接不属于此处的真实光滑路径，不能用跳过连接的两常态反驳 (6)。

一般若 $|k|\le K_*$，则必须 $K_*>1$，且

$$\int_0^L(\partial_s\log h)^2ds\le L(K_*^2-1),$$

$$\boxed{\operatorname{osc}_{[0,L]}\log h
\le L\sqrt{K_*^2-1}.} \tag{7}$$

后一式由总变差与 Cauchy–Schwarz 得到。若还有 $h(0)=h(L)$，闭路总变差至少是振幅的两倍，右侧可进一步乘 $1/2$；这项加强明确需要相同的两个 $h$ 端值。

## 4. 与 frame 闭合长度门的相容结果

若另有 R84 的实际完整 frame 闭合条件，R84 给

$$L\int_0^L(1+k^2)\,ds\ge4\pi^2.$$

结合 (5)，准确有

$$\boxed{L\left(2L+\int_0^L(\partial_s\log h)^2ds\right)\ge4\pi^2.} \tag{8}$$

例如 $h$ 恒定时 $L\ge\sqrt2\pi$。若达到等号，R84 的等号型迫相应球面 frame 曲线为单频圆、$k$ 为常值；这与 (5) 的加权零均值及正二次能量不能同时成立。因此该恒 $h$、真实零矩阵且 frame 闭合类实际满足严格 $L>\sqrt2\pi$。这里没有给统一的严格余量。

## 5. 与第四 action 的边界

(5)–(8) 可用于约束 R92 中真正可实现的几何驱动及其积分量；它们不说明第 $4m-7$ action 能写成这个正能量的正倍数或负倍数。该系数仍须由完整原式等价约简后判断。尤其不能把 frame 长度的正下界或倒行偶性直接当作第四成本的同号性。

与既有构造的关系是具体的：R37 的三圈方案本来选择了严格大于 1 的常曲率幅值；R62 的准确 $\pm1$ 两圈相消明确不包含真实连接；R70 则保留了连接及有限 IFT 的实际曲率修正。本稿给的是这些完整光滑 $M=0$ 路径必须满足的统一身份与界，不替代或重述某个特例的存在构造。

来源：[R37](R37-closed-geometry-zero-period-operator.md)、[R62](R62-reciprocal-constant-states-and-fourth-local-drift.md)、[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R84](R84-fourth-cost-semigroup-and-frame-length-bound.md)、[R85](R85-pure-fourth-leading-tail-is-an-exact-derivative.md)、[R88](R88-pure-fourth-subleading-tail-is-an-endpoint-potential.md)、[R92](R92-pure-fourth-next-tail-quadratic-action.md)。
