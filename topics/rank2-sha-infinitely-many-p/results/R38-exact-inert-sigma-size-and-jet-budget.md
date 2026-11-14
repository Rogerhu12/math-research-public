# R38：固定 sigma 的准确惰性大小、无限分母列及 jet 总量

**状态：以下系数、半径和大小公式均已证明。** 日期：2026-11-12。本结果续接
[固定 sigma 笔记](../notes/2026-11-12-fixed-sigma-height-and-inert-denominator.md)，
不以任何 Sha 有限性或高度非退化假设为前提。

固定 $E:y^2=x^3-17x$、$t=-x/y$、$\omega=dx/(2y)$，记
$L(t)=\log_E(t)$。该笔记已由 Mazur–Tate 存在唯一性和 CM 对称证明：唯一奇形式级数
$$
\Sigma(t)=t\left(1+\sum_{n\ge1}b_nt^{4n}\right)\in\mathbb Q[[t]],
\qquad (d/\omega)^2\log\Sigma=-x,
\tag{1}
$$
在每个好 ordinary split 素数处恰为整 Mazur–Tate sigma。

## 1. 准确结论

设 $p\ge7$、$p\equiv3\pmod4$，并置
$$
r=\frac{p+1}{4},\qquad
s=\frac{p}{p^2-1},\qquad \rho=p^{-s}.
$$
则有：

1. 对所有整数 $a\ge0$，
   $$
   \boxed{\quad
   v_p(b_{r p^a})=-\frac{p^{a+1}-1}{p-1}.
   \quad}
   \tag{2}
   $$
2. $\Sigma(t)$ 的 $p$-进收敛半径准确为 $\rho$，其在 $E\times\mathbb A^1$ 中的形式图形的 Bost–Chambert-Loir size 也准确为
   $$
   \boxed{\quad S_p(\Sigma)=p^{-p/(p^2-1)}.\quad}
   \tag{3}
   $$
3. 对任意 $c\in\mathbb Q_p$，令
   $$
   \Sigma_c(t)=\Sigma(t)\exp\bigl(cL(t)^2/2\bigr).
   $$
   若 $c\in\mathbb Z_p$，其半径和 size 仍等于 (3)；若 $v_p(c)=-h<0$，两者准确为
   $$
   \boxed{\quad
   S_p(\Sigma_c)=p^{-(h+1/(p-1))/2}.
   \quad}
   \tag{4}
   $$

所以在所有 $\mathbb Q_p$ 二次正规化中，整的选择已经取得最大 size；它并不能消去惰性处的损失。

## 2. 对数的唯一临界单项

写
$$
F(t)=\log(\Sigma(t)/t)=\sum_{n\ge1}c_nt^{4n}.
$$
前述笔记直接从曲线方程给出
$$
w_n=(-1)^n\binom{2n}{n}17^n\in\mathbb Z,
\qquad
c_n=\frac1{4n}\left(w_n-\frac12\sum_{j=1}^n
\frac{w_{n-j}w_j}{4j-1}\right).
\tag{5}
$$
因此
$$
v_p(c_n)\ge-v_p(n)-\max_{1\le j\le n}v_p(4j-1).
\tag{6}
$$
特别地，$F$ 在开单位圆盘上收敛。又已准确证明
$$
c_1,\ldots,c_{r-1}\in\mathbb Z_p,
\quad v_p(c_r)=-1,
\quad p c_r\equiv-w_r/2\pmod p.
\tag{7}
$$
其中 $w_r$ 为单位，因为 $2r=(p+1)/2<p$。

以 $\|\ \|_\rho$ 表示半径 $\rho$ 的 Gauss 范数，并记
$g=p^{-1/(p-1)}$。临界项满足
$$
|c_r|_p\rho^{4r}
=p\cdot p^{-p/(p-1)}=g.
\tag{8}
$$
下面证明所有其他项的范数都严格小于 $g$。

若 $n<r$，由整性和 $4s>1/(p-1)$ 得
$v_p(c_n)+4ns>1/(p-1)$。
若 $r<n<p$，(6) 给 $v_p(c_n)\ge-1$，故同一不等式由 $n>r$ 得到。

若 $n\ge p$，令 $j=\lfloor\log_p n\rfloor\ge1$。
因 $p^j\le n<p^{j+1}$、$p\ge7$，
$$
v_p(n)\le j,\qquad
\max_{1\le k\le n}v_p(4k-1)\le j+1.
$$
于是 $v_p(c_n)\ge-(2j+1)$。而
$$
\frac{4np}{p^2-1}
\ge\frac{4p^{j+1}}{p^2-1}
>4p^{j-1}
>2j+1+\frac1{p-1}.
\tag{9}
$$
最后一个不等式在 $j=1$ 直接成立，之后左边至少乘以 $7$ 而右边只增加 $2$。
故所有 $n\ne r$ 都满足所需严格不等式。

由于 (6) 的负项只有 $O(\log n)$，这些加权系数趋于零，
其上确界由有限多个项达到。因此若
$$
R(t)=F(t)-c_rt^{4r},
$$
则不仅逐项严格，而且有
$$
\|R\|_\rho<g.
\tag{10}
$$
还可取某个 $\rho_1>\rho$，使 $\|R\|_{\rho_1}<g$。
所以 $\exp R$ 和 $\exp(-R)$ 都在稍大于 $\rho$ 的圆盘上收敛。

## 3. 无限系数列及准确半径

形式恒等式为
$$
\Sigma(t)/t=\exp(c_rt^{4r})\exp R(t).
\tag{11}
$$
由 (10)，$\|\exp R-1\|_\rho<g$。
主因子的第 $k$ 项在半径 $\rho$ 的加权范数是
$$
\left|\frac{c_r^k}{k!}\right|_p\rho^{4rk}
=p^{v_p(k!)-k/(p-1)}
=p^{-s_p(k)/(p-1)}\le g\qquad(k\ge1),
\tag{12}
$$
这里 $s_p(k)$ 是 $k$ 的 $p$-进数字和，使用 Legendre 公式。
在 $k=p^a$ 时，(12) 准确等于 $g$。

求 (11) 的 $t^{4r p^a}$ 系数，主项
$c_r^{p^a}/(p^a)!$ 的加权范数为 $g$。
其他每项都至少含 $\exp R-1$ 的一个系数；该因子加权范数严格小于 $g$，
而主因子的各系数加权范数不超过 $1$。
故非阿基米德三角不等式使主项不能相消，得到
$$
v_p(b_{r p^a})+4r p^a s=\frac1{p-1},
$$
即 (2)。

另一方面，(11)–(12) 给全部 $n$ 的 Gauss 界
$$
|b_n|_p\rho^{4n}\le1.
\tag{13}
$$
式 (2) 的子列则给
$$
\frac{v_p(b_{r p^a})}{4r p^a}
=-\frac{p}{p^2-1}
+\frac1{(p-1)(p+1)p^a}
\longrightarrow-s.
\tag{14}
$$
由 Cauchy–Hadamard 公式，收敛半径准确为 $\rho$。
这些论证只对有限阶系数作乘积运算；不要求指数主项在整个临界闭圆盘上逐点收敛。

## 4. 为什么这也是几何图形的 size

Bost–Chambert-Loir Proposition 3.5(2) 说明：对于正收敛半径、首项为 $t$ 的图形，
size 等于 $\min(1,\exp\lambda_1)$，其中 $\lambda_1$ 是除以 $t$ 后的 Newton polygon 首斜率。
在这里具体为
$$
S_p(\Sigma)=\min\left(1,\inf_{n\ge1}|b_n|_p^{-1/(4n)}\right).
\tag{15}
$$
式 (13) 给右边至少为 $\rho$，式 (14) 给至多为 $\rho$，证明 (3)。
该文 Theorem 3.1 的 étale 不变性允许把仿射平面坐标计算用于 $E$ 在 $O$ 附近的参数 $t$。

## 5. 任意二次正规化的精确式

先核 $L(t)$ 在略大于 $\rho$ 的圆盘上是 Gauss 等距坐标。
其展开为
$$
L(t)=t+\sum_{n\ge1}\frac{w_n}{4n+1}t^{4n+1}.
\tag{16}
$$
对次数 $d=4n+1>1$，系数赋值至少为 $-v_p(d)$。
若 $v_p(d)=0$，其相对于首项的 Gauss 范数严格小于 $1$。
若 $v_p(d)=1$，因 $p\equiv3\pmod4$、$d\equiv1\pmod4$，有 $d\ge3p$，所以
$$
(d-1)s>1.
$$
若 $v_p(d)=a\ge2$，则 $d\ge p^a$，而
$$
(p^a-1)\frac p{p^2-1}>a.
$$
在 $a=2$ 左边为 $p>2$，之后的增长更快。
所有非首项因此严格小于 $1$，且尾项趋于零。
所以存在 $\rho_2>\rho$，使 $L(t)/t$ 在该半径的 Gauss 范数为 $1$，非恒项严格小于 $1$。
同一严格收缩估计给 $L$ 在该圆盘上的解析逆，亦保持半径。

若 $c\in\mathbb Z_p$，
$$
\|cL(t)^2/2\|_\rho\le\rho^2<g,
$$
因为 $2s>1/(p-1)$。
因此二次指数及其逆在某个略大于 $\rho$ 的圆盘上收敛，
其在半径 $\rho$ 的非恒项 Gauss 范数严格小于 $1$。
乘它不会改变 (11) 的准确半径；所有系数仍满足半径 $\rho$ 的 Gauss 界。
再用 (15)，size 同样为 $\rho$。

若 $v_p(c)=-h<0$，置
$$
\rho_c=p^{-(h+1/(p-1))/2}<\rho.
$$
标量级数 $\exp(cz^2/2)$ 的准确半径是 $\rho_c$，由其系数与 Legendre 公式立即得到。
由于 $L$ 和其逆在略大于 $\rho$ 的圆盘上等距解析，
$\exp(cL(t)^2/2)$ 也只能有准确半径 $\rho_c$；否则复合 $L^{-1}$ 就扩大了前一指数级数的半径。
而 $\Sigma(t)/t$ 在 $|t|<\rho$ 上解析可逆，故乘上它后半径仍为 $\rho_c$。
在每个 $|t|<\rho_c$ 的圆盘上，两个指数的范数都是 $1$；其系数 Gauss 界给 size 至少 $\rho_c$，
而 Proposition 3.5(1) 给 size 不超过收敛半径。得到 (4)。

## 6. 所有素数上的准确 jet 缩放预算

对 $k\ge5$，定义此前代数化笔记中使用的实际系数预算
$$
\mathcal B(k)=\sum_p
\max_{\substack{n\ge1\\4n+1\le k}}
\left(0,-\frac{v_p(b_n)}{4n}\right)\log p.
\tag{17}
$$
每个 $k$ 只涉及有限个有理系数，所以该和有限。
ordinary 好素数处 $\Sigma$ 整，贡献为零。
对 inert $p\ge7$，首坏系数在 $p+2$，故 $p>k-2$ 不贡献；其余由首坏项和准确 size 得
$$
\sum_{\substack{7\le p\le k-2\\p\equiv3\ (4)}}\frac{\log p}{p+1}
\ \le\ \mathcal B(k)
\ \le\
\sum_{\substack{7\le p\le k-2\\p\equiv3\ (4)}}\frac{p\log p}{p^2-1}+O(1).
\tag{18}
$$
有限个排除素数的预算统一有界，因各处正收敛半径已由 (5) 证明。
上下两侧的差至多为收敛级数 $\sum_p\log p/(p^2-1)$。
算术级数中的素数定理及分部求和因此给
$$
\boxed{\quad \mathcal B(k)=\tfrac12\log k+O(1).\quad}
\tag{19}
$$
这是本固定坐标下的 jet 缩放预算，含全部高阶系数。
它给出相应算术估计的准确渐近常数，不能直接声称排除所有不同模型或更精细评价映射的改进。

同时 (3) 已直接给
$\sum_{p\equiv3(4)}\log S_p^{-1}=\infty$，故原 sigma 图形不是 A-analytic。
这项明确的局部计算不证明实际高度 regulator 非零，也不证明主课题的无穷初级有限性。

## 来源与依赖

- 本题 [固定 sigma 的存在、递推和首坏项](../notes/2026-11-12-fixed-sigma-height-and-inert-denominator.md)，(1.3)、(2.3)、(3.1)。其中外部输入为 C. Blakestad–D. Grant，*On the universal p-adic sigma and Weierstrass zeta functions*，J. Number Theory **249** (2023)，Theorem 8、Remark 11、Theorem 30；[作者全文](https://euclid.colorado.edu/~grant/publications/P_adic_sigma_function-published)。
- J.-B. Bost、A. Chambert-Loir，*Analytic curves in algebraic varieties over number fields*，Theorem 3.1、Proposition 3.5、Definition 3.7；[作者全文](https://arxiv.org/pdf/math/0702593)。只引用图形大小的准确 Newton 公式及不变性。
- 本文 (2)–(4)、(19) 及其估计为上述固定级数的直接证明。Legendre 阶乘公式、非阿基米德 Gauss 范数和模 $4$ 的素数定理均按通常规范使用。
