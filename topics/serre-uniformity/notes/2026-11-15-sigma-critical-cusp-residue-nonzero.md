# 原临界五次源在 cusp 的固定非零留数

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：对充分大的允许素数，原五次源的 Cartier 微分在全局非零。
指定 $P_0$ 值及 primitive / Legendre 同标签三单位仍开放。**

本文是 [HC 的 cusp 公式](2026-11-15-sigma-critical-P1-descent-and-C-root-residues.md)
的独立补充，不改动原 $C^{-5}$、原参数或原 CM 点。
沿用 [PC](2026-11-15-sigma-original-PF-cusp-Cartier-and-period-correction.md)
的
$$
D=1-8U^3,\qquad L=\partial_U D\partial_U-8U,
\qquad LA=0,\qquad LC=\kappa U^{p-1},
$$
其中 $p=6N+5\ge41$、$\kappa\ne0$，并且
$A(d)=d a_*$ 对 $d^3=1/8$ 为单位。
原源仍是
$$
\beta=(A/C)^5\alpha_0,\qquad
\alpha_0=\frac{dy}{y^3-1},\qquad x^3+y^3=2.
\tag{CN1}
$$

## 1. 两种 cusp 情形

记 $c_*=C(d)=\mathfrak c(1/8)$。如果 $c_*\ne0$，HC7 已给出非零留数
$$
\operatorname{res}\beta
=\frac{y_c}{3}\left(\frac{d a_*}{c_*}\right)^5,
\qquad y_c^3=1.
\tag{CN2}
$$
故只需处理 $c_*=0$。此时 $C$ 在 $U=d$ 为简单零，但在原曲线的
局部参数 $W=x^3-1$ 中为二重零；不能改用简单极点公式。

令 $w=D=W^2$，固定 $U=d(1-w)^{1/3}$ 的分支。
直接由 $dw/dU=-24U^2$ 得
$$
L=72U\,\mathscr M,\qquad
\mathscr M=w(1-w)\partial_w^2+
\left(1-\frac53w\right)\partial_w-\frac19.
\tag{CN3}
$$
这里是原 $L$ 的坐标变换；没有引入另一个周期方程。
设
$$
\lambda=\frac{\kappa d^{p-2}}{72}\ne0.
$$
因为 $(p-2)/3=2N+1$，有
$$
\mathscr M C=\lambda(1-w)^{(p-2)/3}.
\tag{CN4}
$$
在需要的次数 $0\le n\le5$ 内，二项式系数都可先整约化，且
$$
[w^n](1-w)^{(p-2)/3}
\equiv\frac{(2/3)_n}{n!}\pmod p.
\tag{CN5}
$$
这是因为 $(p-2)/3\equiv-2/3\pmod p$，所有 $n!$ 都为单位。

## 2. 一个固定的有理常数

在特征零中定义三个形式幂级数
$$
F(w)=\sum_{n\ge0}\frac{(1/3)_n^2}{(n!)^2}w^n,
\qquad E(w)=\sum_{n\ge0}\frac{(2/3)_{2n}}{(2n)!}w^n,
\tag{CN6}
$$
以及 $Y(w)=\sum_{n\ge0}y_nw^n$，其中
$$
y_0=0,\qquad
(n+1)^2y_{n+1}
=\left(n+\frac13\right)^2y_n+\frac{(2/3)_n}{n!}.
\tag{CN7}
$$
特别 $y_1=1$。前者满足 $\mathscr M F=0$、$F(0)=1$；后者满足
$\mathscr M Y=(1-w)^{-2/3}$、$Y(0)=0$。
另有
$$
E(w)={}_2F_1\left(\frac13,\frac56;\frac12;w\right),
\qquad
\frac{(1-W)^{-2/3}+(1+W)^{-2/3}}2=E(W^2).
\tag{CN8}
$$
定义固定有理数
$$
\boxed{
K=[w^5]\left(\frac{F(w)}{Y(w)/w}\right)^5E(w).
}
\tag{CN9}
$$
这个定义只消费 $F$ 到五阶、$Y$ 到六阶以及 $E$ 到五阶。

各个 $F_n=\binom{-1/3}{n}^2$、
$E_n=\binom{-2/3}{2n}$ 和 $(2/3)_n/n!$ 的分母仅含三。
例如对每个素数 $\ell\ne3$，二项式多项式在 $\mathbf Z_\ell$ 上取
$\mathbf Z_\ell$ 值，代入 $-1/3$ 或 $-2/3$ 即得这一断言。
(CN7) 在 $n\le5$ 时只另除以 $1^2,\ldots,6^2$；
再除以常数项为一的 $Y/w$ 不引入新分母。因此
$$
K\in\mathbf Z[1/30].
\tag{CN10}
$$

## 3. K 的非零是一个固定的纸面恒等核对

模十三可合法约化以上所有所需系数。
将 (CN6)、(CN7) 逐项代入，得到下表；每行依次列出次数零至五。

| 级数 | 次数 $0,1,2,3,4,5$ 的模十三系数 |
|---|---|
| $F$ | $1,3,10,3,1,0$ |
| $Y/w$ | $1,10,1,12,8,3$ |
| $H=F/(Y/w)$ | $1,6,1,1,1,4$ |
| $H^5$ | $1,4,1,10,12,9$ |
| $E$ | $1,2,5,2,1,0$ |

为使该有限核对可逐项复核，所用递推完整为
$$
F_{n+1}=\frac{(n+1/3)^2}{(n+1)^2}F_n,
\qquad
E_{n+1}=\frac{(n+1/3)(n+5/6)}{(n+1/2)(n+1)}E_n.
\tag{CN11}
$$
模十三时分母在所列范围都非零，且 $1/3=9$、$5/6=3$、$1/2=7$。
$Y$ 用 (CN7)；$H$ 逐项由 $(Y/w)H=F$ 确定。
若写 $H=\sum h_nw^n$、$H^5=\sum b_nw^n$，最后一项乘方使用
$$
b_0=1,\qquad
n b_n=\sum_{j=1}^n(6j-n)h_jb_{n-j}
\quad(1\le n\le5).
\tag{CN12}
$$
它由 $H(H^5)'=5H'H^5$ 直接推出。
于是
$$
K\equiv 9+12\cdot2+10\cdot5+1\cdot2+4\cdot1
=89\equiv11\pmod {13}.
\tag{CN13}
$$
特别 $K\ne0$。这里的十三仅用于证明固定有理数非零，
没有计算原 $p=13$ 的课题数据，也没有扩展有限素数窗口。
全部推导为上述有限递推的纸面代入，未执行本地数学程序。

## 4. 回到原十一阶极点

因为 $A(d)$ 为单位，(CN3) 的递推唯一性及 $LA=0$ 给
$$
A=A(d)F(w)\pmod {w^6}.
$$
在当前 $c_*=0$ 情形，(CN4)、(CN5)、(CN7) 给
$$
C=\lambda Y(w)\pmod {w^7}.
\tag{CN14}
$$
这些同余恰好达到 (CN9) 所需的精度；所有次数均小于 $p$。
HC 的实际参数与微分为
$$
U=d(1-W^2)^{1/3},\qquad
\alpha_0=\frac{y_c}{3W}(1-W)^{-2/3}dW.
$$
因此 $C$ 的二重零带来完整的十一阶极部，而其留数准确为
$$
\boxed{
\operatorname{res}\beta
=\frac{y_c}{3}\left(\frac{A(d)}\lambda\right)^5 K.
}
\tag{CN15}
$$
这里 (CN8) 只取所需偶次系数，没有删去任何影响 $W^{-1}dW$ 的项。

将非零有理数 $K$ 写成最简分数 $a/b$。
由 (CN10)，$b$ 的素因子仅可能为二、三、五。
所以对每个 $p\ge41$ 且 $p\nmid a$，(CN15) 为单位。
结合 $c_*\ne0$ 时的 (CN2)，得到：

**对除固定有限集合外的所有允许素数，原 $\beta$ 至少有一个非零
cusp 留数，从而 $\operatorname{Car}(\beta)\ne0$。**

Cartier 将留数变为其 $p$ 次根，故这一非零推论不需要另加条件。
但 CR 所需的是 $\operatorname{Car}(\beta)$ 在指定 $P_0$ 的值；
其他真正的 $C$ 根仍可能在该值中相消。
本结论既没有证明指定的未筛平方卷积非零，也没有证明任何原同 $h$
primitive / Legendre 三单位或完成主课题。
