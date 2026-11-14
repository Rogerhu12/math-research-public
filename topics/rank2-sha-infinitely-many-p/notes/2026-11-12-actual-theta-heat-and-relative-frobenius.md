# 完整 theta 的热算子、公共参考漂移与真实同源的交换项

日期：2026-11-12。状态：原两变量 theta 的准确热方程、
真实同源修正的兼容式和公共参考的两个漂移项均已直接证明。
本篇只说明这套自然全 theta 连接在有限椭圆覆盖上的准确范围；
没有否定指定中央行另有更强的有限维几何实现。

## 1. 从原 Eisenstein–Kronecker 展开核定热算子

在周期空间使用 R47 的同一个方向
\[
\mathscr W=-A^{-1}
 \left(\bar\omega_1\frac{\partial}{\partial\omega_1}
       +\bar\omega_2\frac{\partial}{\partial\omega_2}\right),
\qquad \mathscr W A=\mathscr W\bar\omega_j=0.
\tag{1}
\]
固定原挠点的有理周期标签，令 $P=r\omega_1+s\omega_2$；
相应共轭标签保持不变。$z,w$ 作为两个独立加法变量，
不随 (1) 一起微分。

Bannai–Kobayashi（2010），Theorem 1.17 的准确展开是
\[
\Theta_P(z,w)=\frac1w+
 \sum_{\substack{a\ge0\\b>0}}
 \frac{(-1)^{a+b-1}e^*_{a,b}(P,0)}
      {a!\,A^a}z^{b-1}w^a.
\tag{2}
\]
在绝对收敛区间，逐项微分给
\[
\mathscr W e^*_{a,b}(P,0)=\frac bA e^*_{a+1,b+1}(P,0).
\tag{3}
\]
一般指标可先给原和加 $|\beta|^{-2\varepsilon}$；
导数因子为 $(b+\varepsilon)/A$，
再按 R47 已核的 Hecke 延拓在 $\varepsilon=0$ 取值。
这里 EK 的第一指标 $a+b>0$，没有零乘极点的额外项。
将 (3) 代入 (2)，符号在两个指标各增一后不变，得到
\[
\boxed{\qquad
\mathscr W\Theta_P=\partial_z\partial_w\Theta_P.
\qquad}
\tag{4}
\]
极项 $1/w$ 的两侧导数均为零。

写 $W_P=w\Theta_P$，则
\[
\boxed{\quad
\mathscr W W_P=\mathcal L W_P,\qquad
\mathcal L=\partial_z\partial_w-w^{-1}\partial_z.
\quad}
\tag{5}
\]
虽然 $\mathcal L$ 写有 $w^{-1}$，$W_P(z,0)=1$ 使 (5) 正则。
其单项式作用准确为
\[
\mathcal L(z^i w^j)=i(j-1)z^{i-1}w^{j-1}.
\tag{6}
\]
故对原 $d_m=[z^m w^{m+1}]\sum W_P$，
\[
\mathscr Wd_m=(m+1)^2d_{m+1}.
\tag{7}
\]
这独立恢复 R47 的两个阶乘，不使用未经核定的 Jacobi
theta 指数规范。

## 2. 真实同源与热算子不是无修正交换

固定整数 $a=-p$、$q=a^2$，令
\[
(T_aF)_P(z,w)=F_{aP}(az,aw).
\]
直接由 (5) 得
\[
\mathcal L T_a=qT_a\mathcal L,
\qquad \mathscr W T_a=T_a\mathscr W.
\tag{8}
\]
原完整方程是
\[
T_aW_P=W_P^qE_{p,P},
\tag{9}
\]
其中 $E_{p,P}$ 是
[实际中央源笔记](2026-11-12-theta-carry-central-residue-source.md)
式 (4) 的真实除法函数修正，包含公共 $w/Z$。

将 (5)、(8) 用于 (9)，而不把 $\mathcal L$ 当成一阶 derivation，
得到
\[
\boxed{\quad
\begin{aligned}
\mathscr W E_{p,P}
={}&-(q-1)E_{p,P}\mathcal L(\log W_P)\\
 &+(\partial_z\log W_P)\partial_wE_{p,P}
   +(\partial_w\log W_P)\partial_zE_{p,P}
   +q^{-1}\mathcal L E_{p,P}.
\end{aligned}
\quad}
\tag{10}
\]
证明仅需完整乘积公式
\[
\mathcal L(AB)=A\mathcal LB+B\mathcal LA+
                  A_zB_w+A_wB_z
\]
及
\[
\mathcal L(W^q)=qW^{q-1}\mathcal LW+
                     q(q-1)W^{q-2}W_zW_w.
\]
后一个交叉项正是 (10) 第一行不可省去的来源。

如使用一般 reduced theta，
\[
H_P(z)=\log F_P^\theta(z),\qquad
H_P''(z)=-\wp(P+z)-s_2,
\]
则实际 (10) 中还有一个完全明确的简化：
\[
\boxed{\quad
\mathcal L\log W_P
=-\wp(P+z+w)
 -\frac{\zeta(P+z+w)-\zeta(P+z)}w.
\quad}
\tag{11}
\]
两处 $s_2$ 在这里准确相消；但 (10) 的另外两个一阶漂移项
没有因而消失。公式 (11) 在 $w=0$ 的可去值为零。

因此 (10) 是一个真正的热／同源兼容式。
它不能被替成 $\mathscr WE=q^{-1}\mathcal LE$；
那样会同时丢掉实际二次算子的交叉项和原参考连接。

## 3. 固定参考后的原标签和仍有两个准确漂移

令 $T=(0,0)$，以及
\[
\mathcal A=\sum_{P\in\mathcal S}\frac{W_P}{W_T}.
\]
这就是 R87/R92 在固定 $[N]\times[N]$ 覆盖上已有的有理对象。
由 $\sum W_P=W_T\mathcal A$、(5) 的完整乘积公式，
\[
\boxed{\quad
\mathscr W\mathcal A
 =\mathcal L\mathcal A+
   B_z\partial_w\mathcal A+B_w\partial_z\mathcal A,
\qquad B_z=\partial_z\log W_T,\quad B_w=\partial_w\log W_T.
\quad}
\tag{12}
\]
原参考的准确表达为
\[
B_z=\zeta(T+z+w)-\zeta(T+z)-s_2w,
\]
\[
B_w=\frac1w+\zeta(T+z+w)-\zeta(w)-s_2z-\eta_T,
\qquad \eta_T=s_2T+\bar T/A.
\tag{13}
\]
所有表面上的原点极点均已相消。
(12) 并未将有理 $\mathcal A$ 的普通微分当成它在固定加法
坐标下的周期方向导数。

在原方格 $E_{17}$ 上 $s_2=0$。直接由
$\vartheta_T^2=x\sigma^2$、$\vartheta_T(0)=1$，
\[
\vartheta_T(z)=1+\frac{17}{12}z^4+O(z^8),\qquad
\sigma(z)/z=1-\frac{17}{60}z^4+O(z^8).
\]
因此
\[
[\log W_T]_4
 =\frac{17}{12}\big((z+w)^4-z^4\big)+\frac{17}{60}w^4,
\]
\[
\boxed{\quad
[\mathcal L W_T]_2=17zw+\frac{34}{3}w^2\ne0.
\quad}
\tag{14}
\]
这给原参考的一个实际非零检验，不能仅因原参考本身的奇总次数
中央对角为零，就把它从 (12) 的乘法中删除。

### 3.1 有限椭圆覆盖不会把这些自然漂移变成有理函数

Reduced zeta 的准周期为
\[
\eta_\gamma-s_2\gamma=\bar\gamma/A
\qquad(\gamma\in\Gamma).
\tag{15}
\]
由 (13)，
\[
B_z(z,w+\gamma)=B_z(z,w)+\bar\gamma/A,
\qquad
B_w(z+\gamma,w)=B_w(z,w)+\bar\gamma/A.
\tag{16}
\]
对任何非零周期，这个增量非零；任意有限倍周期仍然如此。
因此 $[N]\times[N]$ 覆盖没有使 $B_z,B_w$ 成为覆盖上的有理函数。

更一般地，这两个自然 germ 也不能通过任意有限代数覆盖成为
代数多值函数：选避开有限极点的周期回路，代数函数的解析延拓
只有有限个分支；沿同一回路的适当有限次幂必回到原分支。
(16) 却每次增加同一个非零常数，矛盾。
论证可在固定一个一般的另一坐标之后进行，故没有使用曲面上
不必要的全局单连通性假设。

这只定位 (12) 的自然加法坐标规范：不能把它写成在该有限覆盖上
系数全有理的裸二阶热连接，而不增加向量扩张坐标或其他连接数据。
它没有排除在代数 universal vectorial extension 上解释漂移；
也没有排除实际中央投影发生额外消去。
事实上 R47 已将单一中央 Borel 在模参数 $t$ 中写成 $K(t)M_e(t)$，
有限 Gauss–Manin 实现本来就成立；需要比较的是完整 theta、
公共参考与各高阶主部是否被同一个新增对象同时保留。

## 4. 同权源和底参数 Frobenius 之间确切还缺什么

在一个正式热时间 $h$ 中写 $\partial_h=\mathscr W$。
(8) 表明：单独把 $(z,w)$ 乘 $a$ 会把热速度改成 $q^{-1}$。
若只想恢复同一个热方程，形式组合应同时把 $h$ 送到 $qh$，
而不是自动把代数模参数 $t$ 送到 $t^q$。
这是准确算子恒等式，不是对某个 integral Frobenius lift
的存在断言。

R94/R98 的底参数平方 Frobenius 则有实际晶体矩阵
$-pY(t^q)Y(t)^{-1}$，并同时拉回 $dt$。
它作用在固定 Bol 留数线的标量为 $-p^3$。
因此，连接这两种作用必须给出：

- (10) 中实际除法函数的非齐次热项；
- (12) 中公共参考的两个漂移项；
- 从完整混合 jet 到 R94 指定主部的真实截断及整格。

[实际中央源](2026-11-12-theta-carry-central-residue-source.md)
已证明直接取原对角时，这些非齐次数据仍给
$-p^2\mathcal B_1(u)-p\mathcal B_1(p^2u)$，
其完整深度与原中心判据相同。
本篇的热兼容式没有把这项消掉。
目前没有从 (10)–(12) 得到一个独立非零的固定
$H^1\otimes H^1(-1)$ 类，不能仅凭预期斜率相合就称该类已经构造。

## 来源

- K. Bannai、S. Kobayashi（2010），
  *Algebraic theta functions and the p-adic interpolation of
  Eisenstein–Kronecker numbers*，Theorem 1.17、Example 1.9 与式 (15)，
  [作者原文](https://arxiv.org/pdf/math/0610163)。
  本篇再次核对了原文的符号、阶乘和 reduced-theta 规范。
- (1)、(3) 的解析延拓微分与中央 Borel 尺度：
  [R47 完整证明](2026-11-12-central-borel-modular-uniformization.md)。
  (4)–(16) 是上述准确展开的直接计算。
- 全部同源常数、参考与深度见 R92/R95 及前述实际中央源；
  本篇没有调用普通素数的 theta 整性去补惰性漂移。
