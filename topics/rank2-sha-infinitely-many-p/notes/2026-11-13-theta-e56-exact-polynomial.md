# R367 的实际 degree 五十六多项式检查点

日期：2026-11-13。**已证明的精确计算。** 对 R367 中的同一原来源
$$
\mathcal E(w)=\frac1{2\delta}[z^3]\,
 \sigma(z-7w)\sigma(2(z+w))\sigma(\delta(z+w))
$$
有
$$
\boxed{\mathcal E=\sigma^{56}xP_9(X),\qquad X=x^3,}
$$
其中
$$
\begin{aligned}
P_9(X)={}&X^9+900bX^8+7920b^2X^7+1244352b^3X^6\\
&+2123136b^4X^5-1751040b^5X^4-3969024b^6X^3\\
&-6488064b^7X^2-6488064b^8X+262144b^9 .
\end{aligned}
\tag{1}
$$
此处 $b=17$；保留 $b$ 使尺度可直接核对。
特别
$$
\mathcal E(z)=1+\frac{13444b}{15}z^6+\cdots.
\tag{2}
$$

## 全空间与有限计算为何足够

R367 已由原 Gram 矩阵和整个三变量函数证明，
$\mathcal E\in\sigma^{56}L(56O)$ 且 $\mu_6$ 型零。
标准极阶基中只有
$$
\sigma^{56}x^{3j+1},\qquad 0\le j\le9
$$
满足这两个条件。其原点阶依次为 $54-6j$，
所以 $z^0,z^6,\ldots,z^{54}$ 的十行系数对该空间是三角同构。
以下十项计算因此决定整个来源，并非由数值 Taylor 拟合外推。

## 可逐项复算的有理递推

先取 $b=1$。置 $w=z^6$，
$$
x=z^{-2}A(w),\qquad \sigma=zB(w),\qquad
A=\sum a_nw^n,\quad B=\sum s_nw^n.
$$
由 $x''=6x^2$ 及 $x'^2=4(x^3+1)$，
$$
a_0=1,\qquad a_1=-\frac17,\qquad
a_n=\frac{\sum_{i=1}^{n-1}a_ia_{n-i}}{(6n+1)(n-1)}
\quad(n\ge2).
\tag{3}
$$
由 $-(\log\sigma)''=x$，
$$
\ell_n=-\frac{a_n}{6n(6n-1)},\quad
s_0=1,\qquad
s_n=\frac1n\sum_{j=1}^n j\ell_j s_{n-j},
\tag{4}
$$
其中 $\log B=\sum_{n\ge1}\ell_nw^n$。

再置
$$
Y(w)=\sum_{n\ge0}(3n-1)a_nw^n,\qquad
F(w)=-B(w)^7A(w)Y(w)=\sum f_nw^n.
$$
于是
$$
F_{23}(z)/(2\delta)=z^2F(z^6).
$$
R367 原微分式给 $\mathcal E(z)=\sum e_kz^{6k}$ 的准确公式
$$
\boxed{
e_k=\sum_{i+j=k}s_if_j
 \sum_{\substack{0\le a\le3\\a\le6i+1\\3-a\le6j+2}}
 \binom{6i+1}{a}\binom{6j+2}{3-a}(-7)^{6i+1-a}.
}
\tag{5}
$$
所有计算均在 $\mathbb Q$ 内。

令 $P_9(X)=\sum_{j=0}^9c_jX^j$。
因
$$
\sigma^{56}x^{3j+1}
=w^{9-j}B(w)^{56}A(w)^{3j+1},
$$
从 $j=9$ 到 $0$ 逐次减去最先出现的系数即可。
(3)–(5) 截到 $n=9$ 给下表；减去全部十列后的
$w^0,\ldots,w^9$ 余数逐个为零。

| $j$ | $c_j$（$b=1$） |
|---:|---:|
| 0 | 262144 |
| 1 | -6488064 |
| 2 | -6488064 |
| 3 | -3969024 |
| 4 | -1751040 |
| 5 | 2123136 |
| 6 | 1244352 |
| 7 | 7920 |
| 8 | 900 |
| 9 | 1 |

恢复 $b$ 时，第 $j$ 项乘 $b^{9-j}$，即 (1)。
作为低阶独立归一核对，
$s_1=1/210$、$f_1=37/210$，
(5) 直接给 $e_1=13444/15$；
而 (1) 的最高两列给 $900-56/15=13444/15$，相同。

## 使用范围

这是 R367 的实际固定来源，故可以用于完整有限 Heisenberg、
真实平移小球或原连接计算。
仅有多项式并不控制
$\nu_{\mathcal E}(-7y+p^N\mathbf Z_p)$ 的 unit 中心值；
原点 core 与原中央导数之间仍须保留 R367 的域条件。

例如 $b=1$ 时 $P_9(-1)=1594323$、
$P_9(-4)=2579890176$、$P_9(8)=417942208512$。
这些只排除所列三个已知低挠点因子；
本笔记没有把其余零点宣布为挠点或非挠点。

引用：[R367 原整个联合与微分式](../results/R367-original-degree-seven-fifty-six-joint-and-translated-leaf-balls.md)。
