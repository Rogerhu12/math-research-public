# 普通 principal 权阶梯的同一首层

日期：2026-11-12。状态：已证明。
本篇对象是 R51 的反圆平方根 $J_p$；不要与 R24 的单 $\mathfrak p$ 分支混同。

## 1. 全部正整数权的基本估值

取普通目标素数 $p\ge13$、$p\ne17$，令
$$
m_j=j(p-1),\quad
M_j=\int_{\mathbb Z_p^\times}x^{m_j}\,d\nu_p(x),\quad j\ge1,
$$
其中 $\nu_p$ 是 R51 实际 $A$ 的整测度。其单位总质量为 $M_0=J_p(0)=0$。
完整 single-Euler 分布给
$$
M_j=
\left(1-\frac{\pi^{m_j}}{\bar\pi^{m_j+1}}\right)
\Omega_p^{m_j}m_j!\,b_{m_j}
=J_p\bigl((1+p)^{m_j}-1\bigr).
\tag{1}
$$
这里的 $\Omega_p$ 与 R51 的实际形式群同构一致。

写 $J_p(T)=a_1T+a_2T^2+\cdots\in\mathcal O_p[[T]]$。
对每个正整数 $j$，lifting-the-exponent 给
$$
v_p((1+p)^{m_j}-1)=1+v_p(j).
$$
故
$$
\boxed{
v_pb_{j(p-1)}
\ge1+v_p(j)-v_p((j(p-1))!).
}
\tag{2}
$$
若 $a_1$ 为单位，(2) 对所有 $j\ge1$ 都取等号：
线性项的估值严格小于所有高次项。反之，取 $j=1$ 时等号，
就由 $v_p((p-1)!)=0$ 及 (1) 推得 $a_1$ 为单位。

若额外有 $J_p'(0)=0$，则同样的论证给较强下界
$$
v_pb_{j(p-1)}
\ge2(1+v_p(j))-v_p((j(p-1))!).
\tag{3}
$$
这里只使用已经给定的零阶假设，不把 (3) 反过来当成已证的无穷素数结论。

## 2. 全部 $1\le j<p$ 的首层由一个余数决定

在 $\mathbb Z_p^\times$ 上设 $h(x)=x^{p-1}-1\in p\mathbb Z_p$。
因为 $\nu_p$ 整且单位总质量为零，二项式恒等式立即给
$$
M_j\equiv jM_1\pmod{p^2}\qquad(j\ge1).
\tag{4}
$$
先由 (2) 知，对 $1\le j\le p-1$，
$$
p^{j-2}b_{j(p-1)}\in\mathbb Z_p.
\tag{5}
$$
其中 $j=1$ 的含义是 $b_{p-1}/p\in\mathbb Z_p$。

所需阶乘单位有一个特别简单的统一值：
$$
v_p((j(p-1))!)=j-1,\qquad
\frac{(j(p-1))!}{p^{j-1}}\equiv-1\pmod p.
\tag{6}
$$
证明：$j(p-1)=(j-1)p+(p-j)<p^2$。
删去其中 $p$ 的倍数后，前 $j-1$ 个整块贡献 $(-1)^{j-1}$，
末块贡献 $(p-j)!$；被删去的倍数除以 $p^{j-1}$ 后贡献 $(j-1)!$。
Wilson 恒等式给
$(-1)^{j-1}(j-1)!(p-j)!\equiv-1$，即 (6)。

令
$$
\mathsf H_p=a_p(E)\bmod p
=(-17)^{(p-1)/4}
\binom{(p-1)/2}{(p-1)/4}\in\mathbb F_p^\times
\tag{7}
$$
为相对于 $dz=dx/(2y)$ 的 Hasse invariant。
其规范也可以不经阶乘求和而核对：
R24 所用不变导子在约化上满足
$\delta_E^p=\mathsf H_p\delta_E$；
实际 Amice 坐标使
$$
\delta_E=\Omega_p^{-1}\Theta,\qquad
\Theta=(1+Z)\frac d{dZ},\quad\Theta^p=\Theta.
$$
所以
$$
\Omega_p^{1-p}\equiv\mathsf H_p\pmod p.
\tag{8}
$$
此式只用于约化，未把 $\Omega_p$ 误认为有理数。

(1) 中 Euler 因子模 $p^2$ 为一。把 (6)–(8) 代入 (4)，得到
$$
\boxed{
p^{j-2}b_{j(p-1)}
\equiv
j\,\mathsf H_p^{j-1}\frac{b_{p-1}}p
\pmod p,\qquad 1\le j\le p-1.
}
\tag{9}
$$
因 $j$ 和 $\mathsf H_p$ 都非零，(9) 的任何一个左端为单位，
当且仅当 $b_{p-1}/p$ 为单位。
这些首层不能被计作 $p-1$ 个独立的非消失事件。

## 3. 与固定 logarithmic 系列的精确连接

令 $r=(p-1)/4$，并使用
[固定系列笔记](2026-11-12-ordinary-prime-coefficient-fixed-logarithmic-series.md)
中的同一个 $G(v)\in\mathbb Q[[v]]$。该笔记已证明
$$
\frac{b_{p-1}}p\equiv17^{r-1}[v^r]G\pmod p.
$$
于是 (9) 全部化为
$$
p^{j-2}b_{j(p-1)}
\equiv j\,\mathsf H_p^{j-1}17^{r-1}[v^r]G\pmod p.
\tag{10}
$$
新的、可能独立的信息须来自更高 $p$ 精度，或其他真正不同的分支。
本结论不排除普通斜率笔记中高阶 Newton 差分所提供的精确信息。

一次独立有理 Lagrange 计算在 $p=13$ 检查了 $m=12,24,36$：
此时 $\mathsf H_{13}=7$，三个规范余数依次为 $12,12,9$，
与 (9) 一致。这个有限检查只核符号、阶乘和周期方向，
证明本身是 (1)–(8)。
