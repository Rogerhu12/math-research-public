# 实际惰性对角、Romik 系数的准确接口与现有同余定理的范围

日期：2026-11-12。状态：固定截面及模 $p$ 公式的准确特化；
一手文献核验。尚无无穷多个惰性素数上的非零证明。

## 1. 固定到 $D=1$ 不改变无穷素数问题

[次数十七截面的认证](2026-11-12-degree17-theta-gaussian-and-denominator-certificate.md)
已经证明本题实际截面为

$$
 A_D(z)=\theta_D(z)\sigma_D(z)^{16}
 \left(x_D(z)^6+\frac{3D}{5}x_D(z)^4
                   -\frac{D^2}{5}x_D(z)^2+\frac{D^3}{5}\right),
 \qquad D=17.
 \tag{1}
$$

这里同一式子也定义 $D=1$ 的辅助截面。
它是一个固定解析函数，不把 $D=1$ 的秩零曲线替换成本题的秩二曲线。
令 $a^4=D$。曲线及不变微分的缩放给

$$
 x_D(z)=a^2x_1(az),\qquad
 \sigma_D(z)=a^{-1}\sigma_1(az),\qquad
 \theta_D(z)=\theta_1(az).
$$

代入 (1) 即得

$$
 A_D(z)=D^{-1}A_1(az),\qquad
 b_{4n}(D)=D^{n-1}b_{4n}(1).
 \tag{2}
$$

因此对于每个惰性 $p\ge7$，$p\ne17$，
$b_{p+1}(17)$ 与 $b_{p+1}(1)$ 同时为 $p$ 单位。

在[固定级数归约](2026-11-12-inert-theta-diagonal-and-curvature.md)
的记号下，现在准确取

$$
 q(v)=v+\frac35v^2-\frac15v^3+\frac15v^4,
 \qquad
 \Xi_1(v)=\frac{(\Theta(v)^{17}q(v))'}{F(v)}.
 \tag{3}
$$

其中

$$
 F(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}v^n,
 \qquad
 \frac{\Theta'}\Theta=
 \frac1{4\sqrt{1-v}}\sum_{n\ge0}
                  \frac{\binom{2n}{n}}{4^n(4n+3)}v^n,
 \qquad \Theta(0)=1.
$$

对于 $p=4r-1$，已经逐项核对整性的准确公式成为

$$
 \boxed{\quad b_{p+1}(17)\equiv
     4\cdot17^{r-1}[v^{r-1}]\Xi_1(v)\pmod p.\quad}
 \tag{4}
$$

特别是现在没有来自未知 $c_j$ 的有限例外集合；本篇所有目标惰性
$p\ge7$ 都不等于 $5,17$。

## 2. 参考 theta 函数与 Romik 整数恰好怎样对应

用 $d_{\rm R}(n)$ 表示 Romik 的序列，避免与本题中央系数 $d_m$
混淆。Romik 的定义及 Proposition 10 给出 Hermite 生成公式：
见 Dan Romik，*The Taylor coefficients of the Jacobi theta constant
$\theta_3$*，Ramanujan Journal **52** (2020), 275–290；
[作者预印本 arXiv:1807.06130v2](https://arxiv.org/pdf/1807.06130)，
Proposition 10，式 (26)，预印本第 14 页。

设

$$
 B(t)=e^{-t^2}\sum_{k\in\mathbb Z}
                  e^{-\pi_{\mathbb C}k^2+2\sqrt{2\pi_{\mathbb C}}kt}.
$$

[参考 theta 的除子计算](2026-11-12-dyadic-vector-and-reference-theta.md)
及 duplication 恒等式给

$$
 \theta_1(z)=\frac{B(cz)}{B(0)},\qquad
 c=\frac{\sqrt{\pi_{\mathbb C}/2}}{\Omega_0},\qquad
 \Omega_0=\frac{\Gamma(1/4)^2}{2\sqrt{2\pi_{\mathbb C}}}.
 \tag{5}
$$

最后一个周期等式也可直接由
$\Omega_0=\int_1^\infty dx/\sqrt{x^3-x}
=\tfrac12 B(1/4,1/2)$ 计算。

Romik 的式 (26) 在 Hermite 阶数 $4n$ 时给
$B^{(4n)}(0)/B(0)=16^n\Phi^n d_{\rm R}(n)$，其中
$\Phi=\Gamma(1/4)^8/(128\pi_{\mathbb C}^4)$。
由于 $16\Phi c^4=2$，得到精确恒等式

$$
 \boxed{\quad
 \theta_1(z)=\sum_{n\ge0}
          \frac{2^n d_{\rm R}(n)}{(4n)!}z^{4n}.
 \quad} \tag{6}
$$

例如 $d_{\rm R}(n)$ 的初值 $1,1,-1,51,849$ 给
$[z^4]\theta_1=1/12$、$[z^8]\theta_1=-1/10080$。
这个恒等式保留了全部阶乘；忽略 $(4n)!$ 会改变本题的首层赋值。

实际对象并非 (6) 单独一项，而是

$$
 A_1=\theta_1\sigma_1^{16}
       \left(x_1^6+\frac35x_1^4-\frac15x_1^2+\frac15\right).
 \tag{7}
$$

等价的 sigma 乘积虽已认证，却同样含这些额外因子。
因此不能把关于 $d_{\rm R}(n)$ 的结论不经系数比较就直接应用到
$b_{4n}(1)$。

## 3. 已证的同余范围没有覆盖当前目标

Christian Krattenthaler、Thomas W. Müller，
*The congruence properties of Romik's sequence of Taylor coefficients of
Jacobi's theta function $\theta_3$*，
[arXiv:2304.11471v4 (2024)](https://arxiv.org/pdf/2304.11471)，
Theorem 1(1) 与 Theorem 23，证明：若 $p\equiv3\pmod4$、$e\ge2$，
则

$$
 d_{\rm R}(n)\equiv0\pmod{p^e}
       \qquad\left(n\ge\left\lceil\frac{(e-1)p^2}{2}\right\rceil\right).
 \tag{8}
$$

这是一个明确的后段消失结论。
同文 Theorem 1(2) 的周期结论属于 $p\equiv1\pmod4$。
两者都没有给惰性 $n=(p+1)/4$ 的非零断言。

Jigu Kim、Yoonjin Lee，*p-adic Properties for Taylor Coefficients of
Half-integral Weight Modular Forms on $\Gamma_1(4)$*，
Taiwanese Journal of Mathematics **27** (2023), 23–38，
[DOI 10.11650/tjm/220802](https://doi.org/10.11650/tjm/220802)，
[arXiv:2109.08778v2](https://arxiv.org/pdf/2109.08778)，
Theorem 1.3 处理 $\Gamma_1(4)$ 上的半整数权模形式，给
Shimura–Maass 导数在阶数至少 $(e-1)p^2$ 时的 $p^e$ 整除性；
Theorem 1.4 给 (8) 的 $p\ge5$ 版本。
其群、规范化及方向都不能自动变成 (7) 的早期非零定理。

因此即使另外建立本题固定有限 Schwartz 向量所对应模形式的
完整热方程接口，这些引用仍没有提供所需的跨素数结论。
这里没有把模形式的复非零、固定模 $p$ 的最终周期或最终消失
升级为指定 prime diagonal 的非零。

## 4. 两个独立的有限计算入口

[check-inert-theta-prime-diagonal.py](../scripts/check-inert-theta-prime-diagonal.py)
实现两种算法：第一种从
$x''=6x^2-2$、$(\log\sigma)''=-x$ 直接计算 (7)；
第二种用 (3)–(4) 及截断多项式的 Newton 指数算法。
截断指数、积分及 Lagrange 算法中的分母均小于 $p$；
直接递推中另一个分母是
$2(2j-3)(4j+1)$，在 $1\le j\le(p-3)/4$ 时也不被 $p$ 整除。

默认运行核对所有 $7\le p<500$、$p\equiv3\pmod4$。
命令行选项 `--bound 25000` 重现较大的有限样本：
在这个范围的 $1388$ 个目标素数上，$b_{p+1}(1)$ 都非零。
这只是可复现的有限一致性证据。
例如

| $p$ | $b_{p+1}(1)\pmod p$ |
|---:|---:|
| $7$ | $5$ |
| $11$ | $7$ |
| $19$ | $2$ |
| $31$ | $15$ |
| $79$ | $28$ |

当前仍需证明 (4) 的那个指定系数在无穷多个惰性素数上非零。
