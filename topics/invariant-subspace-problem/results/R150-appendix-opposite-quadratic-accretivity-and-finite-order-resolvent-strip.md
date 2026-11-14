# R150 附录：相反二次符号的最大增生性与有限阶空谱预解不相容

日期：2026-11-13（UTC）。Astra-ISP-1cf8c51d 推导；normal_resume_1cf 全文独立核验，kernel_resume_1cf 独立得出同一两符号因式与条带估计。
状态：已证明的抽象引理。供 [R150 实剪切剩余有界分支](R150-appendix-real-collision-noncritical-branch-and-bounded-tail-normalization.md)使用；其实际应用仍须另付二次同域及两个最大增生限制。

## 1. 准确假设

设 $\mathcal K\ne\{0\}$ 是复 Hilbert 空间，$X$ 是稠密定义的闭最大增生算子。
假设 $\sigma(X)=\varnothing$，记
$$
R(z)=(X-zI)^{-1}\qquad(z\in\mathbb C).
$$
再假设存在有限常数 $C,\rho>0$，使
$$
\|R(z)\|\le C\exp(C(1+|z|)^\rho).                         \tag{1.1}
$$
这是实际整个预解的增长假设，不能仅由空谱推出。

令 $J,K\in B(\mathcal K)$ 与 $X$ 的全部预解交换。
因而它们保持 $\operatorname{Dom}X^q$ 并与自然幂交换。
假设对每个实数 $c\ge c_0$，以下两算子在准确域
$\operatorname{Dom}X^2$ 上都最大增生：
$$
T_+(c)=X^2+(cI+J)X+K,\qquad
T_-(c)=-X^2+(cI-J)X-K.                                  \tag{1.2}
$$

**定理。** 这些假设在非零 $\mathcal K$ 上不可能同时成立。

以下不使用一般群生成元的谱非空断言，也不需要通常伴随的域等式。
证明只用真正最大增生预解界、实际二次因式及一个明确的半条带障碍函数。

## 2. 最大增生性与有界扰动的直接逆界

最大增生性给
$$
\|(X+\lambda I)^{-1}\|\le(\operatorname{Re}\lambda)^{-1}
\qquad(\operatorname{Re}\lambda>0),                      \tag{2.1}
$$
以及
$$
\|(T_\pm(c)+\mu I)^{-1}\|\le(\operatorname{Re}\mu)^{-1}
\qquad(\operatorname{Re}\mu>0).                          \tag{2.2}
$$
如果 $V$ 有界且 $\operatorname{Re}\mu>\|V\|$，
在 (2.2) 上作真正的 Neumann 因式分解就给
$$
\|(T_\pm(c)+\mu I+V)^{-1}\|
\le(\operatorname{Re}\mu-\|V\|)^{-1}.                    \tag{2.3}
$$
这些逆的像都在原来的 $\operatorname{Dom}X^2$ 中。

固定
$$
j=\|J\|,\quad k=\|K\|,\qquad
c\ge\max(c_0,j+2),\qquad D=c+j+k+2.
$$
以下 $c$ 始终固定。写 $z=x+iy$、$r=|z|$。

## 3. 虚方向占优区域的真实因式

取
$$
\mu_+(z)=-z^2-cz,\qquad V_z=Jz+K.
$$
因 $J$ 保持 $\operatorname{Dom}X$，下列两个一次因子的乘积域准确为 $\operatorname{Dom}X^2$；逐项相乘得
$$
F_+(z):=T_+(c)+\mu_+(z)I-V_z
=(X-zI)(X+zI+cI+J).                                    \tag{3.1}
$$
若 $x\ge-1$，第二个因子
$$
B_+(z)=X+zI+cI+J
$$
由 (2.1) 和有界扰动有真正的逆，而且
$$
\|B_+(z)^{-1}\|\le (x+c-j)^{-1}\le1.                    \tag{3.2}
$$

如果
$$
y^2-x^2\ge D(r+1),                                     \tag{3.3}
$$
则
$$
\begin{aligned}
\operatorname{Re}\mu_+(z)-\|V_z\|
&\ge y^2-x^2-cx-jr-k\\
&\ge D(r+1)-(c+j)r-k\\
&=(k+2)r+c+j+2\ge r+1.
\end{aligned}
$$
故 (2.3) 给 $\|F_+(z)^{-1}\|\le(r+1)^{-1}$。

式 (3.1) 的两个因子及其有界逆在实际域上交换，且
$B_+(z)-(X-zI)=2zI+cI+J$ 有界。
于是从 (3.1) 得真正的有界预解恒等式
$$
R(z)=B_+(z)^{-1}+(2zI+cI+J)F_+(z)^{-1}.
\tag{3.4}
$$
可以先在 $\operatorname{Dom}X^2$ 验证、再用两个有界逆延拓；
也可以直接用 $R(z)$ 和 $B_+(z)^{-1}$ 的交换及值域核验。
因此
$$
\boxed{\|R(z)\|\le 3+c+j}                               \tag{3.5}
$$
在 $x\ge-1$ 且 (3.3) 成立时有效。

## 4. 实方向占优区域

现在取
$$
\mu_-(z)=z^2-cz.
$$
同一真实域上有
$$
F_-(z):=T_-(c)+\mu_-(z)I+V_z
=-(X-zI)(X+zI-cI+J).                                   \tag{4.1}
$$
若 $x\ge c+j+1$，则
$$
B_-(z)=X+zI-cI+J,\qquad \|B_-(z)^{-1}\|\le1.
$$
若另有
$$
x^2-y^2\ge D(r+1),                                     \tag{4.2}
$$
则与第3节相同，
$$
\operatorname{Re}\mu_-(z)-\|V_z\|\ge r+1,
\qquad
\|F_-(z)^{-1}\|\le(r+1)^{-1}.
$$
这里的加号有界扰动不改变 Neumann 预算。
由 (4.1) 得
$$
R(z)=B_-(z)^{-1}-(2zI-cI+J)F_-(z)^{-1}.
\tag{4.3}
$$
所以 (3.5) 在这个区域也成立。

当 $x\ge-1$ 且 $r$ 充分大，(4.2) 自动使 $x\ge c+j+1$：
$x^2>y^2$ 给 $|x|>r/\sqrt2$，而 $x\ge-1$ 排除大的负 $x$。
因此这一额外限制只留一个有界区域，不产生另一条无界缝隙。
在 $x\le-1$ 上，(2.1) 已给 $\|R(z)\|\le1$。
对于可能残留的 $-1\le x\le0$ 竖带，
$y^2-x^2=r^2-2x^2\ge r^2-2$，故足够大 $r$ 时已满足 (3.3)。

## 5. 剩余集合只在两条固定宽半条带内

去掉一个固定圆盘后，未被 §§3–4 覆盖的点只能满足
$$
x\ge0,\qquad |x^2-y^2|<D(r+1).
$$
于是
$$
|x-|y||=\frac{|x^2-y^2|}{x+|y|}
\le\frac{D(r+1)}r\le2D\qquad(r\ge1).                    \tag{5.1}
$$
取
$$
a=2D+1.
$$
(5.1) 将所有这样的点放入两条方向
$\theta=\pi/4$、$\theta=-\pi/4$ 的固定宽条带
$$
|\operatorname{Im}(e^{-i\theta}z)|<a.
$$
对充分大的实数 $t_0$，两个对应半条带
$$
\mathcal S_\theta=
\{z=e^{i\theta}(t+is):t\ge t_0,\ |s|\le a\}
\tag{5.2}
$$
之外的整个复平面上，$R(z)$ 已一致有界；被去掉的有界部分靠整预解的连续性控制。

还可直接核验半条带的两条长边在已控制区域：
若 $s=\pm a$，则
$$
|x^2-y^2|=2at,\qquad r=(t^2+a^2)^{1/2}.
$$
因为 $2a>D$，在 $t$ 足够大时有
$2at\ge D(r+1)$；同时 $x\ge c+j+1$。
故长边由 (3.5) 控制。
短边 $t=t_0$ 是紧线段，也有统一界。
以下把所有这些边界界记为同一个有限数 $M_0$。

## 6. 明确的半条带障碍函数

取任意单位向量 $u,v$，定义标量整函数
$$
f(z)=\langle R(z)u,v\rangle.
$$
对一个固定 $\theta=\pm\pi/4$，写
$$
g(w)=f(e^{i\theta}w),\qquad
\operatorname{Re}w\ge t_0,\quad |\operatorname{Im}w|\le a.
$$
在该半条带的三条边上，$|g|\le M_0$。
(1.1) 给
$$
|g(w)|\le C\exp(C(1+|w|)^\rho).                         \tag{6.1}
$$

令
$$
\beta=\frac{\pi}{4a},\qquad
g_\varepsilon(w)=g(w)
\exp[-\varepsilon\cosh(\beta(w-t_0))],
\qquad \varepsilon>0.
$$
在闭条带内，
$$
\operatorname{Re}\cosh(\beta(w-t_0))
=\cosh(\beta(\operatorname{Re}w-t_0))
 \cos(\beta\operatorname{Im}w)
\ge\frac1{\sqrt2}\cosh(\beta(\operatorname{Re}w-t_0)).
\tag{6.2}
$$
所以原三条边上的 $|g_\varepsilon|$ 不超过 $M_0$。
在远端竖边 $\operatorname{Re}w=R$，(6.1)–(6.2) 给
$$
\log|g_\varepsilon(w)|
\le\log C+C(1+\sqrt{R^2+a^2})^\rho
-\frac{\varepsilon}{\sqrt2}\cosh(\beta(R-t_0))
\longrightarrow-\infty
$$
且对 $|\operatorname{Im}w|\le a$ 一致。
因此在充分长的有限矩形上，用最大模原理得
$|g_\varepsilon|\le M_0$。
先令远端 $R\to\infty$，再对固定点令 $\varepsilon\downarrow0$，得
$$
|g(w)|\le M_0
$$
在整个半条带成立。

这一证明允许任何有限的 $\rho$，不是只允许 $\rho<1$；
关键是半条带宽度固定，障碍项在长度方向呈指数增长，
压过 $\log|g|$ 的任意固定次幂。

两个半条带分别这样处理。$M_0$ 与单位 $u,v$ 无关，
遂得 $\sup_{z\in\mathbb C}\|R(z)\|<\infty$。

## 7. Liouville 矛盾及假设边界

每个矩阵元 $f$ 都是有界整函数，故为常数。
在负实轴，由 (2.1)，
$$
\|R(-t)\|=\|(X+tI)^{-1}\|\le t^{-1}\longrightarrow0.
$$
所以所有矩阵元恒为零，即 $R(z)=0$。
这与 $R(0)$ 是非零空间上 $X$ 的双侧逆矛盾。定理证毕。

假设“对每个 $c\ge c_0$”只为应用方便；证明实际仅需存在一个
$c\ge\|J\|+2$ 使两个 (1.2) 同时最大增生。

本证明使用了以下三个不能省去的输入：
准确的 $\operatorname{Dom}X^2$、两个相反二次符号的最大增生性、
以及真正整预解的有限阶上界。
只知道两个正方向有空谱、一般闭差有界、或有界自交换子，
不满足这里的二次同域输入。
本稿没有宣称任意空谱闭算子、任意空谱群生成元都不可能存在。
