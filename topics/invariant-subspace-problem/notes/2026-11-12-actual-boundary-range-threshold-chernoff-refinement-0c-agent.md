# R239 附录：实际值域指数阈值的 Chernoff 精化

日期：2026-11-12（UTC）。独占作者：literature。

本稿独立补充
[实际慢边界算子的指数次数值域阈值](../notes/2026-11-12-actual-boundary-range-exponential-degree-threshold-0c-agent.md)。
保留该稿的真实算子、头截断、单位向量及全部定义域论证，只精化一个纯尾基本对称和估计。

定义
$$
\boxed{
\Gamma
=4+\frac12\log90-\pi\sqrt{\frac32}
-\frac2{45}+\frac2{729}-\frac2{9477}.
}
\tag{0.1}
$$
以下给出完全解析证明及有限有理证书，保证
$$
\boxed{\Gamma>\frac{59}{25}=2.36.}
\tag{0.2}
$$
数值仅作定位：$\Gamma\approx2.3603433472$。
两个真实规范慢边界算子都满足
$$
\boxed{
0\le\kappa<\Gamma
\quad\Longrightarrow\quad
\mathscr X_\kappa\not\subset\operatorname{Ran}T_N,\ 
\mathscr X_\kappa\not\subset\operatorname{Ran}T_Y.
}
\tag{0.3}
$$
可选同一个输入同时不属于两个值域。
整个 $N^\perp$ 上的规范逐层原像成本下界也同步提高到指数率 $\Gamma$。
真正缺陷 $M\ominus N$ 上的专属估计仍未由此决定。

## 1. 保留原来的真实小奇异向量

设 $a_j=(j+1)^{-2}$，在位 $[m,\infty)$ 的纯尾上令
$$
C_m=\sum_{j\ge m}a_jE_j^*,\qquad I=\{m,\ldots,m+q-1\},
\qquad A_I=\prod_{j\in I}a_j.
$$
前稿的精确对称消去向量为
$$
u_{m,q}
=A_I^{-1}\sum_{k=0}^q
(-1)^k\frac{(q-k)!}{q!}
e_{q-k}\big((a_jE_j^*)_{j\in I}\big)
C_{\rm tail}^{\,k}\Omega,
$$
$$
C_{\rm tail}=\sum_{j\ge m+q}a_jE_j^*.
$$
它处于纯 $q$ 孔层，满足
$$
\|u_{m,q}\|\ge1,\qquad
C_mu_{m,q}=\frac{(-1)^q}{q!A_I}C_{\rm tail}^{\,q+1}\Omega.
\tag{1.1}
$$
令 $z_{m,q}=u_{m,q}/\|u_{m,q}\|$。本稿不改变这个向量；
只在计算右边范数时保留更多尾部信息。

记
$$
R=m+q,\qquad n=q+1,\qquad
e_n^{\rm tail}
=\sum_{\substack{F\subset[R,\infty)\\|F|=n}}
\prod_{j\in F}(j+1)^{-4}.
$$
准确的尾幂范数是
$$
\|C_{\rm tail}^{\,n}\Omega\|=n!\sqrt{e_n^{\rm tail}}.
$$
所以 (1.1) 给
$$
\boxed{
\|C_mz_{m,q}\|
\le\frac{q+1}{A_I}\sqrt{e_{q+1}^{\rm tail}}.
}
\tag{1.2}
$$

## 2. 非负系数的无限乘积估计

对任意 $s>0$，由于尾平方系数可和，
$$
\prod_{j\ge R}\left(1+\frac{sR^4}{(j+1)^4}\right)
$$
是有限的正实数。先对有限乘积比较第 $n$ 次非负系数，再按单调收敛取极限，得到
$$
e_n^{\rm tail}
\le(sR^4)^{-n}
\prod_{j\ge R}\left(1+\frac{sR^4}{(j+1)^4}\right).
\tag{2.1}
$$
这里没有对交替系数使用绝对值后的形式比较；所有系数均非负。

函数 $x\mapsto\log(1+sR^4/x^4)$ 在 $[R,\infty)$ 上非负递减。
右端整数和因而满足
$$
\begin{aligned}
\sum_{j\ge R}\log\left(1+\frac{sR^4}{(j+1)^4}\right)
&\le\int_R^\infty\log(1+sR^4/x^4)\,dx\\
&=R I(s),
\end{aligned}
$$
其中
$$
I(s)=\int_1^\infty\log(1+s/x^4)\,dx.
\tag{2.2}
$$
结合 (1.2)、$A_I=(m!/R!)^2$，
$$
\boxed{
\|C_mz_{m,q}\|
\le V_{m,q}(s)
:=(q+1)\left(\frac{R!}{m!}\right)^2
s^{-(q+1)/2}R^{-2(q+1)}
\exp\!\left(\frac R2I(s)\right).
}
\tag{2.3}
$$

固定 $s$，取
$$
m=m(q)=\lceil\log_2(q+1)\rceil+3,\qquad p(q)=q+m(q).
$$
由
$\log(R!)=R\log R-R+O(\log(R+1))$
及 $m=O(\log(q+1))$，直接整理 (2.3) 得
$$
\log V_{m(q),q}(s)
\le-\gamma(s)q+O((\log(q+1))^2),
$$
$$
\gamma(s)=2+\frac12\log s-\frac12I(s).
\tag{2.4}
$$
把 $q$ 换成 $p(q)$ 只改变 $O(\log q)$ 项，故
$$
\boxed{
\log V_{m(q),q}(s)
\le-\gamma(s)p(q)+O((\log(p(q)+1))^2).
}
\tag{2.5}
$$
所有余项常数可依赖固定 $s$，不依赖 $q$。

## 3. 取 $s=9$ 的完整积分上界

分部积分给
$$
I(s)=-\log(1+s)+4F(s),\qquad
F(s)=\int_1^\infty\frac{s}{x^4+s}\,dx.
\tag{3.1}
$$
设 $a=s^{1/4}$。代换 $x=ay$ 得
$$
F(s)
=a\left(\int_0^\infty\frac{dy}{1+y^4}
-\int_0^{1/a}\frac{dy}{1+y^4}\right)
$$
$$
=a\left(\frac{\pi}{2\sqrt2}
-\int_0^{1/a}\frac{dy}{1+y^4}\right).
\tag{3.2}
$$
标准积分值可由
$1+y^4=(y^2+\sqrt2y+1)(y^2-\sqrt2y+1)$
的实部分式积分直接得到。

对 $t\ge0$，
$$
\frac1{1+t}-(1-t+t^2-t^3)=\frac{t^4}{1+t}\ge0.
$$
令 $t=y^4$ 并积分，得到
$$
\int_0^{1/a}\frac{dy}{1+y^4}
\ge
\frac1a-\frac1{5a^5}+\frac1{9a^9}-\frac1{13a^{13}}.
$$
故
$$
F(s)\le
\frac{\pi a}{2\sqrt2}
-1+\frac1{5s}-\frac1{9s^2}+\frac1{13s^3}.
\tag{3.3}
$$
这一界不依赖级数在积分端点的收敛，因为所用的是全 $t\ge0$ 成立的准确有理恒等式。

取 $s=9$，则 $a=\sqrt3$，代入 (3.1)、(2.4) 得
$$
\begin{aligned}
\gamma(9)
&=2+\frac12\log9+\frac12\log10-2F(9)\\
&\ge
4+\frac12\log90-\pi\sqrt{\frac32}
-\frac2{45}+\frac2{729}-\frac2{9477}\\
&=\Gamma.
\end{aligned}
\tag{3.4}
$$
这就给出了 (0.1) 的解析下界。
本稿没有把浮点积分或数值最优化当作负号、正号证书。

## 4. $\Gamma>2.36$ 的有限有理证书

以下三条严格有理界足够：
$$
\log90>\frac{44998096}{10^7},\qquad
\pi<\frac{31415927}{10^7},\qquad
\sqrt{\frac32}<\frac{1224745}{10^6}.
\tag{4.1}
$$
最后一条直接平方验证。

前两条也可只用有限有理和检验。写
$$
\log90=6\log2+\log(45/32).
$$
由
$\log\frac{1+x}{1-x}=2\sum_{k\ge0}x^{2k+1}/(2k+1)$
的正项展开，
$$
\log90>
12\sum_{k=0}^{11}\frac{3^{-(2k+1)}}{2k+1}
+
2\sum_{k=0}^{11}\frac{(13/77)^{2k+1}}{2k+1}
>
\frac{44998096}{10^7}.
\tag{4.2}
$$
对 $\pi$，使用可由正切加法公式验证的 Machin 恒等式
$$
\pi=16\arctan(1/5)-4\arctan(1/239).
$$
交替级数的上下和给
$$
\pi<
16\sum_{k=0}^{10}\frac{(-1)^k5^{-(2k+1)}}{2k+1}
-4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
<
\frac{31415927}{10^7}.
\tag{4.3}
$$
两处最后的比较都是有限有理算术。

将 (4.1) 代入 (0.1)，得到完全有理的严格下界
$$
\boxed{
\Gamma>
\frac{14912646133698043}{6318000000000000}
=
\frac{59}{25}
+\frac{2166133698043}{6318000000000000}
>\frac{59}{25}.
}
\tag{4.4}
$$
以下短程序只复核有限有理比较；数学输入是已经写出的正项/交替级数界。
不需要任意精度浮点库。

~~~python
from fractions import Fraction as F

def log_ratio_lower(x, n):
    return 2 * sum(
        (x ** (2*k + 1)) / (2*k + 1) for k in range(n)
    )

def atan_partial(x, n):
    return sum(
        ((-1) ** k) * x ** (2*k + 1) / (2*k + 1)
        for k in range(n)
    )

log_lower = 6 * log_ratio_lower(F(1, 3), 12)
log_lower += log_ratio_lower(F(13, 77), 12)
pi_upper = 16 * atan_partial(F(1, 5), 11)
pi_upper -= 4 * atan_partial(F(1, 239), 2)

log_certificate = F(44998096, 10**7)
pi_certificate = F(31415927, 10**7)
sqrt_certificate = F(1224745, 10**6)

assert log_lower > log_certificate
assert pi_upper < pi_certificate
assert sqrt_certificate ** 2 > F(3, 2)

lower = 4 + log_certificate / 2
lower -= pi_certificate * sqrt_certificate
lower -= F(2, 45)
lower += F(2, 729)
lower -= F(2, 9477)

assert lower == F(14912646133698043, 6318000000000000)
assert lower > F(59, 25)
~~~

## 5. 传回两个真实算子与规范原像

沿用前稿完全相同的
$$
w_q=e_{2^{m(q)}-1}\otimes z_{m(q),q}
\in\mathcal H_{p(q)},\qquad \|w_q\|=1.
$$
真实有限头伴随仍准确杀去第一个张量因子，
进位误差仍是全算子界 $26e^{-770\,16^{m(q)-1}}$。
只需在原估计中把 $U_{m,q}$ 换成 (2.3)：
$$
\|T_\bullet^*w_q\|
\le V_{m(q),q}(9)+26e^{-770\,16^{m(q)-1}}.
\tag{5.1}
$$
由 (2.5)、(3.4) 及
$16^{m(q)-1}\ge256(q+1)^4$，得到
$$
\boxed{
\|T_\bullet^*w_q\|
\le
\exp[-\Gamma p(q)+C(\log(p(q)+1))^2]
}
\tag{5.2}
$$
对充分大的 $q$ 成立，且可对两个模型统一选择 $C$。

给定 $0\le\kappa<\Gamma$，取
$\kappa<\lambda<\mu<\Gamma$。
在足够大的共同 $q_0$ 后，
$\|T_\bullet^*w_q\|\le e^{-\mu p(q)}$。
仍定义
$$
v_\lambda=\sum_{q\ge q_0}e^{-\lambda p(q)}w_q.
$$
次数层正交给 $v_\lambda\in\mathscr X_\kappa$。
若 $T_\bullet y=v_\lambda$，则
$$
e^{-\lambda p(q)}
=|\langle y,T_\bullet^*w_q\rangle|
\le\|y\|e^{-\mu p(q)},
$$
矛盾。这证明 (0.3)，并给同一输入同时不属于两个值域。

同理，对 $f_q=T^*w_q\in M^\perp\subset N^\perp$，
规范逐层原像满足 $J_{p(q)}^*f_q=w_q$。所以
$$
\boxed{
\|J_{p(q)}^*|_{N^\perp}\|
=\|P_{N^\perp}J_{p(q)}\|
\ge
\exp[\Gamma p(q)-C(\log(p(q)+1))^2].
}
\tag{5.3}
$$
若先把右边的规范映射仅定义在有限支撑输入上，则相同不等式适用于该稠密定义范数上确界；
使用 R239 已有延拓时就是通常算子范数。

这些 $f_q$ 位于 $M^\perp$，不位于真正缺陷 $M\ominus N$。
因此新的常数仍没有排除缺陷专属的更小指数权。
也没有确定临界指数或上下界之间的准确阈值。

## 6. 与原稿的关系

原稿完整源 blob 为 `b54b81f107c20d0c3864fa11c7a7bc7c47de0e2c`；
本稿不修改或覆盖该源。其实际头截断、全算子误差、正交层叠加及定义域论证保持不变。
本次唯一加强是对非负尾基本对称和使用生成乘积，
把已证必要指数从 $\gamma_0=3/2+\frac12\log3$ 提高到 (0.1) 的 $\Gamma>2.36$。

本稿仍只处理负整数边界表示。
它不是原 Haar 正常湮灭态的反例，也不是边界 $N=M$ 的反例。
