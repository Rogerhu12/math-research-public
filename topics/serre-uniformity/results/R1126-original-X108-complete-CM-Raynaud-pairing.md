# R1126：原 X0(108) 六个 CM 微分的完整 Raynaud 配对

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；root / o1_theta。

**状态：已证明，纯纸面。**
在 R1059 的同一个实际模型和原微分尺度上，完整计算六个 CM 微分之间
全部十五个交替配对，目标保留完整十维正则微分空间。
额外实际自同构把其准确化为三个明确有限和 $A,S,T$。
其中 $S$ 严格是原 $S_n$，不是另一同源曲线或另一尺度的数值。

这个完整表及其 Pfaffian 身份不证明 $S_n$ 非零；
它给后继真正的乘法/高阶 Cartier 约束一个已付的完整输入。

## 1. 原模型、全部目标及半线性

设
$$
p=6N+5\ge41,\quad n=(p-2)/3=2N+1,\quad
s^2=-3,\quad \kappa=3s,
$$
并取 $\rho\in\mathbf F_p^\times$ 为唯一的 $\rho^3=2$ 的根。
沿 R1059 的实际函数及原 $q$ 尺度，
$$
z^3=1-\kappa x^3,\qquad w^3=1+\kappa x^3,\qquad
U=zw,\qquad U^3=1+27x^6,\qquad
\Omega=\frac{dx}{z^2w^2}.
\tag{1126.1}
$$
记六个原 CM 微分为
$$
g=\Omega,\quad c=x\Omega,\quad d=x^2\Omega,\quad
u=z^2\Omega,\quad h=zw\Omega,\quad v=w^2\Omega.
\tag{1126.2}
$$
它们均 Cartier-exact。完整目标还包括
$z\Omega,w\Omega,xz\Omega,xw\Omega$。
本篇不把配对的值预先限制到 Cartier 核。

沿 R1059 的定义，
$$
\beta(\omega,\nu)=\mathscr C(F_\omega\nu),\qquad dF_\omega=\omega,
$$
$$
\beta(\lambda\omega,\mu\nu)
=(\lambda\mu)^{1/p}\beta(\omega,\nu).
\tag{1126.3}
$$
primitive 的 $p$ 次幂歧义被 $\mathscr C(\nu)=0$ 消去，
配对正则且交替。实际自同构与 Cartier 相容，
但作用到输入常数时必须保留 (1126.3)。

R1060 的 Euler 化简给
$$
s^p=-s,\qquad \kappa^n=1/s.
\tag{1126.4}
$$

## 2. 完整字符把十五对缩到十个允许位置

在实际 $\mu_3^3$ 作用
$(x,z,w)\mapsto(\zeta^a x,\zeta^b z,\zeta^c w)$ 下，
各形式的字符指数为：

| 形式 | 字符指数，模3 |
|---|---|
| $g$ | $(1,1,1)$ |
| $c$ | $(2,1,1)$ |
| $d$ | $(0,1,1)$ |
| $u$ | $(1,0,1)$ |
| $h$ | $(1,2,2)$ |
| $v$ | $(1,1,0)$ |
| $z\Omega$ | $(1,2,1)$ |
| $w\Omega$ | $(1,1,2)$ |
| $xz\Omega$ | $(2,2,1)$ |
| $xw\Omega$ | $(2,1,2)$ |

因 $p^{-1}\equiv-1\bmod3$，
$\beta$ 的输出字符是两个输入字符之和的负数。
十个目标字符互异，故五对
$$
\boxed{\beta(g,h)=\beta(c,u)=\beta(c,h)=\beta(c,v)=\beta(d,h)=0.}
\tag{1126.5}
$$
其余十对各落在唯一一条显示的目标直线上。
这是完整正则目标中的字符排除，不需要假定 $\mathscr C\beta=0$。

## 3. 直接原函数给三个准确有限和

定义
$$
\boxed{
\begin{aligned}
A&=27^N\sum_{\substack{i+j=N\\i,j\ge0}}
       \frac{\binom ni\binom nj}{6i+2},\\
S&=\sum_{i=0}^{n}\frac{(-1)^i\binom ni^2}{3i+1}=S_n,\\
T&=\sum_{i=0}^{N}
       \frac{(-1)^i\binom ni\binom n{n-2i}}{6i+1}.
\end{aligned}}
\tag{1126.6}
$$
三者都在 $\mathbf F_p$ 中，所有分母均为单位。
这里 $S_n$ 正是 R1059.5，因而仍与原 $f_N$ 相差其已付单位；
没有将它改成去掉因子 $2/3$ 的 inverse-center sum。

令
$$
G_r(x)=\sum_{i=0}^n
 \binom ni27^i\frac{x^{6i+r+1}}{6i+r+1},
\qquad r=0,1,2.
$$
指数均小于 $2p$，且不等于 $p$，所以全部分母可逆。
由 (1126.1) 直接得到
$$
F_g=G_0/U^p,\quad F_c=G_1/U^p,\quad F_d=G_2/U^p.
\tag{1126.7}
$$
另外
$$
R_\pm(x)=\sum_{i=0}^n
 \binom ni(\pm\kappa)^i\frac{x^{3i+1}}{3i+1},
\qquad
F_u=R_+/w^p,\quad F_v=R_-/z^p.
\tag{1126.8}
$$
这些都是原曲线上的实际有理 primitive。

例如
$$
\beta(c,d)=U^{-2}\mathscr C\bigl(
 G_1(x)x^2(1+27x^6)^n\,dx\bigr).
$$
括号中指数为 $6(i+j)+4$，次数小于 $4p-1$；
可被 Cartier 读取的 $rp-1$ 中，只有 $p-1$ 符合该模六类。
其读数恰是 (1126.6) 的 $A$，故
$$
\beta(c,d)=Ag.
\tag{1126.9}
$$

同样，$\beta(g,u)$ 的多项式分子为
$G_0(x)(1+\kappa x^3)^n$，只有 $x^{p-1}$ 贡献。
条件 $2i+j=n$ 给系数
$$
\kappa^n\sum_{i=0}^N
 \frac{(-1)^i\binom ni\binom n{n-2i}}{6i+1}
=\kappa^nT.
$$
取实际 $p$ 次根并用 (1126.4)，得到
$$
\beta(g,u)=-\frac{T}{s}\,z\Omega.
\tag{1126.10}
$$

最后，原 (1126.8) 给 $\beta(u,v)$ 的 $x^{p-1}$ 系数为
$-\kappa^nS$；因此
$$
\beta(u,v)=\frac S s\,h.
\tag{1126.11}
$$
这与 R1059 先读取 $\beta(v,u)$ 的反号一致。

供额外尺度核对，直接用 (1126.7) 还得
$$
\beta(g,d)=
27^n\left(\sum_{i+j=n}\frac{\binom ni\binom nj}{6i+1}\right)c.
\tag{1126.12}
$$
下一节将该和准确识别为 $S/(3\rho)$；不是假定两个和自动相等。

## 4. 原函数域上的实际额外自同构

定义
$$
R:(x,z,w)\longmapsto
 \left(-\frac{w}{sz},\frac{\rho s x}{z},\frac{\rho}{z}\right).
\tag{1126.13}
$$
在齐次坐标中，它是可逆单项式变换
$$
(T,X,Z,W)\longmapsto
 (Z,-W/s,\rho sX,\rho T).
$$
代入原两个三次方程，利用 $\rho^3=2$、$s^2=-3$，
逐项保持相同曲线。因此不是由一个抽象同源关系猜出的算子。

实际微分给
$$
d(w/z)=\frac{2\kappa x^2}{w^2z^4}\,dx,\qquad R^*\Omega=\rho^{-1}u.
$$
其六个作用准确为
$$
\begin{array}{lll}
R^*g=\rho^{-1}u,&R^*c=-h/(\rho s),&
R^*d=-v/(3\rho),\\
R^*u=-3\rho d,&R^*h=\rho s c,&R^*v=\rho g .
\end{array}
\tag{1126.14}
$$
还有
$$
R^*(z\Omega)=s\,xz\Omega,\quad
R^*(w\Omega)=z\Omega,\quad
R^*(xz\Omega)=-xw\Omega.
\tag{1126.15}
$$

平方为同一个实际 involution
$$
I=R^2:(x,z,w)\mapsto
 \left(\frac1{3x},-\frac{w}{sx},\frac{z}{sx}\right),
$$
$$
I^*(g,c,d,u,h,v)=(-3d,-c,-g/3,v,-h,u).
\tag{1126.16}
$$
另取
$$
\sigma:(x,z,w)\mapsto(-x,w,z),\qquad
\sigma^*(g,c,d,u,h,v)=(-g,c,-d,-v,-h,-u).
\tag{1126.17}
$$
所有微分标量均由 (1126.1) 直接求出。

由 $I$ 作用于 (1126.9)，得 $\beta(g,c)=9Ad$。
设 $\beta(g,d)=Ec$，则 (1126.14) 与半线性给
$$
-\frac1{3\rho^2}\frac S s\,h
=\beta(R^*g,R^*d)=R^*(Ec)
=-\frac E{\rho s}h,
$$
所以
$$
E=\frac S{3\rho}.
\tag{1126.18}
$$
这同时核准 (1126.12) 的准确有限和身份。

定义
$$
C=-T/s,\qquad D=sC/3=-T/3,\qquad B=-3\rho sA.
\tag{1126.19}
$$
将 (1126.9)–(1126.11) 依次用 $R,I,\sigma$ 运输，
所有其余允许位置均被确定。
尤其包含 $1/s$ 的输入乘子在取 $p$ 次根时变号；
省掉该半线性会给错误的 $B$ 和 $S$ 标量。

## 5. 完整配对表

| 输入对 | 准确输出 |
|---|---|
| $(g,c)$ | $9A\,d$ |
| $(g,d)$ | $\dfrac S{3\rho}\,c$ |
| $(c,d)$ | $A\,g$ |
| $(u,h)$ | $B\,v$ |
| $(u,v)$ | $\dfrac S s\,h$ |
| $(h,v)$ | $B\,u$ |
| $(g,u)$ | $C\,z\Omega$ |
| $(g,v)$ | $-C\,w\Omega$ |
| $(d,u)$ | $D\,xz\Omega$ |
| $(d,v)$ | $D\,xw\Omega$ |

其余五对为 (1126.5) 的零，反序取负号。
表中允许位置并不预设系数非零。
这同时保全部六个 CM 输入与四个非 CM 输出方向；
例如 $C\ne0$ 时，$\beta(g,u)$ 不在六个 CM 方向内。

## 6. 原六阶 Pfaffian 的准确范围

将矩阵 $\bigl(\beta(\omega_i,\omega_j)\bigr)$
按 $(g,c,d,u,h,v)$ 排列，并除去共同形式 $\Omega$。
它在原函数域上的 Pfaffian 沿首行展开为
$$
\begin{aligned}
\operatorname{Pf}
&=18ADB\,x^3+ABC(z^3-w^3)\\
&=2ABx^3(9D-\kappa C)=0.
\end{aligned}
\tag{1126.20}
$$
这里使用的是 $z^3+w^3=2$、$z^3-w^3=-2\kappa x^3$
和 $D=sC/3$。所有项已经显示；不存在被略掉的 $S$ 项。
因此该六阶交替矩阵在原函数域上的秩至多四，
而这个事实与原 $S_n$ 是否为零无关。

逐项代入也表明：若把 (1126.6) 中的实际值暂当作形式变量，
该表对任意 $A,S,T\in\mathbf F_p$ 都满足上述 $\mu_3^3,R,\sigma$ 的
线性等变条件以及 (1126.20)。
所以这些已显示的条件本身不足以证明 $S_n\ne0$。
这只是约束的逻辑范围，不是构造了实际 $S_n=0$ 的素数实例。

后继可以使用同一 canonical 乘法关系
$$
g\,d=c^2,\qquad u\,v=h^2
$$
及真正有理 primitive，进一步求高阶 Cartier 约束。
不能将线丛配对的完美性、这个 Pfaffian 或 R1060 非CM块的普通性
直接替代指定 $S_n$ 或原短 $\eta_k,\nu_k$ 的非零。

## 7. 来源与核对

- [R1059](R1059-original-fN-actual-X108-Raynaud-pairing-and-inverse-central-sum.md)：
  实际 X0(108) 模型、原 q/微分尺度、Raynaud 配对及原 $S_n$。
- [R1060](R1060-actual-X108-nonCM-Cartier-and-nine-torsion-ordinary-input.md)：
  完整十维正则基、CM六方向、半线性及 $\kappa^n=1/s$。
- [R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)：
  原三挠 Petri 点与 $S_n$ 的准确几何含义。
- Harrison, *A new automorphism of X0(108)*，
  [原论文](https://arxiv.org/pdf/1108.5595)，Definition4.2 / Theorem4.4：
  原模型的上游来源继续沿R1059；本篇的具体 $R,I,\sigma$ 直接在
  (1126.1) 上验证，不需要另认一个未知常数的 canonical 矩阵。

root逐项推导完整字符、primitive及额外自同构；
o1独立核原函数域、所有微分标量、三有限和和全部配对符号。
本篇无数学程序执行，无数值窗口重算。
原指定非零性及一般素数主目标继续。
