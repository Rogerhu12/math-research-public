# 原十七次截面不属于有限个同范数有理 CM 缩放的张成

日期：2026-11-12。状态：以下张成空间的排除已证明。
结论针对同一秩零参考 theta 的**无平移、同范数有理 CM 缩放**；
不排除带挠点平移的十七维表示，不排除别的几何或 Frobenius 表示。

## 1. 对象与命题

全部在 $E_1:y^2=x^3-x$ 的固定微分坐标中比较。令

$$
 \theta(z)=\theta_T(z),\qquad \theta(0)=1,
$$

$$
 A(z)=\theta(z)\sigma(z)^{16}
       \left(x(z)^6+\frac35x(z)^4-\frac15x(z)^2+\frac15\right).
                                                               \tag{1}
$$

$A$ 是已经由两份独立证书识别的实际 E17 截面的固定四次缩放，
满足 $A(z)=z^4+O(z^8)$。置 $\varpi=4-i$、$\beta_0=\bar\varpi=4+i$。

**命题。** 不存在有限个 $\beta_j\in\mathbb Q(i)$、
$\beta_j\bar\beta_j=17$ 及常数 $c_j\in\mathbb C$，使

$$
                    A(z)=\sum_j c_j\theta(\beta_jz)           \tag{2}
$$

作为形式级数或整函数恒等式成立。

整数 CM 缩放的特殊情形已可从两个明确多项式直接排除，见
[五次比较截面](2026-11-12-degree-five-theta-lucas-interface.md) §5。
本篇还排除任意分母的有理 CM 缩放；只枚举范数 $17$ 的高斯整数
不足以证明这一加强。

## 2. 在共同尺度上比较有限 Schwartz 向量

记 $\mathscr T$ 为有理数上的全局 theta 分布，$h_n$ 为本课题
固定规范的 Hermite 向量。对有限 Schwartz 函数 $\phi_f$，写

$$
 B_{\phi_f}(t)=e^{-t^2}\sum_{x\in\mathbb Q}
        \phi_f(x)e^{-\pi_{\mathbb C}x^2+2\sqrt{2\pi_{\mathbb C}}xt}.
                                                               \tag{3}
$$

其第 $n$ 个系数是 $\mathscr T(h_n\otimes\phi_f)$ 乘一个只依赖
$n$ 的固定非零实数；所以下面的缩放和单射性不受该归一影响。

秩零参考的有限向量是
$\phi_f^0=\prod_\ell\mathbf1_{\mathbb Z_\ell}$。
置 $c_* =\sqrt{\pi_{\mathbb C}/2}/\Omega_1$。
由参考 theta 规范及十七次下降，存在非零常数 $c_0,c_{17}$，使

$$
 \theta(z)=c_0B_{\phi_f^0}(c_*z),\qquad
 A(z)=c_{17}B_{\phi_f^{17}}(c_*\beta_0z).                     \tag{4}
$$

第二式的尺度不是任意选取的：原 $L=34$ 级数取
$z\mapsto z/(2\varpi)$ 后，$34/(2\varpi)=\bar\varpi$；
再把 E17 的 $17^{1/4}$ 四次缩放吸收到 E1 坐标，正好得到 (4)。
这正是已证
[十七次下降](2026-11-12-theta-seventeen-isogeny-descent.md)
和 [准确截面证书](2026-11-12-degree17-theta-gaussian-and-denominator-certificate.md)
使用的尺度。

对每个候选 $\beta_j$，$q_j=\beta_j/\beta_0$ 属于
$G(\mathbb Q)=\{q\in\mathbb Q(i)^\times:q\bar q=1\}$。
使用**参考 E1** 的全局 splitting，记其有限 Weil 作用为
$\omega_f^0$。固定 splitting 后，Hermite 特征准确为
$\omega_\infty^0(q)h_n=q^nh_n$。全局 theta 分布的有理不变性给

$$
 \mathscr T\bigl(h_n\otimes\omega_f^0(q^{-1})\phi_f^0\bigr)
      =q^n\mathscr T(h_n\otimes\phi_f^0).
$$

因此，置 $\phi_{f,j}=\omega_f^0(q_j^{-1})\phi_f^0$，有

$$
                  B_{\phi_{f,j}}(t)=B_{\phi_f^0}(q_jt).       \tag{5}
$$

若另用未分裂的 metaplectic 规范，可能出现一个与 $n$ 无关的
非零半权相位；它只重标 $c_j$，不改变本命题的张成空间。
本篇采用已经固定的参考全局 splitting，故 (5) 无需逐权相位选择。

## 3. $17$ 处的 compact unit 类型不同

在 $17$ 处分裂 $K\otimes\mathbb Q_{17}=\mathbb Q_{17}\times\mathbb Q_{17}$，
把范数一群识别为 $\mathbb Q_{17}^\times$。
参考特征在这里未分歧。自然极化下，其 compact unit 作用为

$$
                 \omega_{17}^0(a)v(y)=v(ay)
                   \qquad(a\in\mathbb Z_{17}^\times).       \tag{6}
$$

参考向量 $\mathbf1_{\mathbb Z_{17}}$ 在 (6) 下不变。
因为整个分裂环面是交换群，任意 $q_j$ 的环面平移仍保持该类型。
所以每个 $\phi_{f,j}$ 及其任意有限线性组合，在
$G(\mathbb Z_{17})$ 下均不变。

实际 E17 的向量则不同。已证的紧平均在自然极化中为

$$
 v_{17}(y)=\frac{\sqrt{17}}{16}\,\lambda^{-1}(y)
                       \mathbf1_{\mathbb Z_{17}^\times}(y),  \tag{7}
$$

其中 $\lambda$ 在单位群上的限制是非平凡四次特征，
可取 $\lambda(3)=-i$。
在**同一个参考作用** (6) 下，

$$
                    \omega_{17}^0(a)v_{17}
                       =\lambda^{-1}(a)v_{17}.               \tag{8}
$$

这不是平凡类型；例如 $a=3$ 的特征值是 $i$。
不能把实际特征的 splitting 因子 $\lambda(a)$ 再乘入 (8)，
否则会混淆用于比较的两个作用。实际向量在它自己的 splitting
下不变，恰好对应在参考 splitting 下的非平凡类型。

标准极化与自然极化由已固定的 $\rho$ 等变转换。
它不改变这个结论。还可直接检查参考向量未被转换改变：
写 $c=x_0^3\in\mathbb Z_{17}^\times$，

$$
 (\rho\mathbf1_{\mathbb Z_{17}})(x)
 =\psi(cx^2/2)\int_{\mathbb Z_{17}}
           \psi(cxy+cy^2/4)\,dy
 =\mathbf1_{\mathbb Z_{17}}(x).
$$

因为 $\psi$ 的导子为 $\mathbb Z_{17}$，$cy^2/4$ 在积分域上整，
傅里叶正交先强迫 $x\in\mathbb Z_{17}$，此时剩余相位也为一。
故 (7) 确实与参考的 trivial compact unit 类型不同。

实际全局 $\mu_4$ 平均仍保持 (8)，因为环面平移互相交换。
因此非零的 $\phi_f^{17}$ 不在这些 $\phi_{f,j}$ 的有限张成中。

## 4. 不能用 theta 映射的核消除这个类型差

这里补全所需的单射性，而不从有限个 Taylor 系数猜测向量相等。
对有限多个有限 Schwartz 函数，共取整数 $D>0$，使它们在
$\mathbb Q$ 上的支撑均包含于 $D^{-1}\mathbb Z$。
其取值有界且局部常值，因此 (3) 的 Gaussian 级数在每个紧集
正规收敛，定义整函数。

若 $B_\phi(t)$ 的所有系数为零，则它恒为零。
取 $t$ 为纯虚数并去掉不消失的 $e^{-t^2}$ 后，得到

$$
             \sum_{n\in\mathbb Z}
               \phi(n/D)e^{-\pi_{\mathbb C}(n/D)^2}
                    e^{2\pi_{\mathbb C}iny/D}=0
                    \qquad(y\in\mathbb R).
$$

该 Fourier 级数绝对一致收敛。逐项与每个字符积分，给
$\phi(n/D)=0$ 对所有 $n$ 成立；支撑外的有理值本来也为零。
$\mathbb Q$ 在有限 adeles 中稠密，而 $\phi$ 局部常值，故
$\phi=0$。于是

$$
                    \phi_f\longmapsto B_{\phi_f}
                    \quad\text{是单射。}                   \tag{9}
$$

如果只从四倍 Hermite 权比较，必须先核其他权均为零。
这里参考函数 $\theta(iz)=\theta(z)$，其有理环面平移与全局 $i$
作用交换，所以所有 $B_{\phi_{f,j}}$ 的非四倍权都为零；
实际 $B_{\phi_f^{17}}$ 的相同性质已由全局 $i$ 平均证明。
因此四倍权相等也确实给出全部 Hermite 系数相等。

若 (2) 成立，(4)–(5) 和 (9) 就迫使
$\phi_f^{17}$ 属于 $\phi_{f,j}$ 的有限张成，违反 (8)。命题得证。

## 5. 对中心导数路线保留下来的问题

五次比较截面的导数可以化成一个固定代数数的非零 $p$ 进对数。
本篇说明原十七次截面不能仅通过扩大无平移 CM 缩放的分母得到
同样的有限缩放差公式。
真实的十七维表示仍存在，但它包含挠点平移的 theta 向量；
其单位 Mellin 核涉及对整个测度的对数积分，不能从 (5) 的
乘法缩放规则代替。这一结论不否定更一般的有限群对数表达，
也没有解决实际普通或惰性半因子 $J_p'(0)$ 的跨素数非零。

一手接口：Yang，*Theta liftings and Hecke L-functions*，
J. reine angew. Math. **485** (1997), 25–53，Corollaries 2.10、2.14、
式 (2.28)，[作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)；
Yang，*Nonvanishing of central Hecke L-values and rank of certain
elliptic curves*，Compositio Math. **117** (1999), 337–359，Lemma 1.1 与
Appendix (A3)，
[出版社全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/915B51D40C0BD146C3DBC94DE4041BDD/S0010437X99000433a.pdf/nonvanishing_of_central_hecke_lvalues_and_rank_of_certain_elliptic_curves.pdf)。
本课题的完整规范核对见
[固定 sigma 平方构造](2026-11-12-fixed-sigma-theta-square-factorization.md)
和 [实结构的明确局部计算](2026-11-12-theta-real-structure-and-mellin-square.md)。
