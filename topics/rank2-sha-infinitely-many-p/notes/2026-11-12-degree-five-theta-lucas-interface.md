# 一个五次 theta 截面的临界系数准确成为 Lucas 非 Wieferich 条件

日期：2026-11-12。状态：以下恒等式、逐素数赋值比较均已证明。
本篇研究一个明确的比较截面，不把它等同于本题的十七次截面，
也不由此声称原目标已经解决或不可能解决。

## 1. 同一固定 CM 曲线上的准确恒等式

在 $E_0:y^2=x^3-x$ 上沿用已固定的代数微分 $dz=dx/(2y)$、
Weierstrass $\sigma(z)=z+O(z^5)$ 与

$$
 \theta(z)=\theta_T(z)=\sqrt{x(z)}\,\sigma(z),\qquad
 \theta(0)=1,\qquad T=(0,0).
$$

它们满足 $\theta(iz)=\theta(z)$。置 $\alpha=2+i$，
$\bar\alpha=2-i$。则

$$
 \boxed{\quad
 C(z):=\theta(z)\sigma(z)^4
   =\frac{\theta(\alpha z)-\theta(\bar\alpha z)}{4i}.
 \quad}                                                   \tag{1}
$$

这是固定次数为 $5$ 的 theta 截面，$C(z)=z^4+O(z^8)$，
全部 Taylor 系数属于 $\mathbb Q$。

**证明。** 设 $\Gamma=\Omega_0\mathbb Z[i]$，
$\mathcal A=\Omega_0^2/\pi_{\mathbb C}$。
$\theta$ 的半特征为
$\chi_T(m\Omega_0+ni\Omega_0)=(-1)^{mn}$，其乘子为

$$
 \theta(z+\lambda)=\chi_T(\lambda)
  \exp\!\left(\frac{\bar\lambda(z+\lambda/2)}{\mathcal A}\right)
  \theta(z).
$$

由于 $N\alpha=N\bar\alpha=5$，且 $\alpha,\bar\alpha$ 模 $2$
都等于 $i$，$\theta(\alpha z)$、$\theta(\bar\alpha z)$ 和
$\theta(z)^5$ 有相同乘子。因此

$$
 \frac{\theta(\alpha z)-\theta(\bar\alpha z)}{\theta(z)^5}
$$

是 $i$ 不变的椭圆函数；它只可能在 $T$ 有不超过 $5$ 阶的极点。
$i$ 在 $T$ 的局部参数上作用为 $i$，故极点阶只能是 $4$ 的倍数。
该比值属于 $\mathbb C(x^2)$，所以准确为 $a+b/x^2$。
它在 $O$ 为零，给出 $a=0$。

由 $x(z)=z^{-2}+z^2/5+O(z^6)$ 和
$\sigma(z)=z(1-z^4/60+O(z^8))$，

$$
 \theta(z)=1+z^4/12+O(z^8),\qquad
 \alpha^4-\bar\alpha^4=48i.
$$

因此 $b=4i$。再用
$\theta^5/x^2=\theta\sigma^4$ 得到 (1)。同一证明完全保留了
全局乘子，未把不同次数的 theta 截面直接相加。$\square$

## 2. 每个惰性素数的赋值比较

写

$$
 \theta(z)=\sum_{n\ge0}t_nz^n,\qquad
 C(z)=\sum_{n\ge0}c_nz^n.
$$

令 $p=4r-1\ge7$ 为素数，并记

$$
 \kappa_p=-\frac12(-1)^r\binom{2r}{r}\in\mathbb Z_{(p)}^\times.
$$

本题已证明的惰性 sigma 首分母公式给

$$
 v_p(t_{p+1})=-1,\qquad p\,t_{p+1}\equiv\kappa_p\pmod p.
                                                               \tag{2}
$$

这里也可直接从相同的低阶微分计算检查 (2)：
在 $\log\theta=\log(\sigma/z)+\tfrac12\log(z^2x)$ 中，
第二项到次数 $p+1$ 都是 $p$ 整的；第一项仅在次数 $p+1$
首次出现分母 $p$。由 $\delta^{p-1}x\equiv\kappa_p$ 和
Wilson 定理，$[z^{p-1}]x\equiv-\kappa_p$。
$\log(\sigma/z)''=-(x-z^{-2})$ 于是给

$$
 p[z^{p+1}]\log\theta\equiv\kappa_p\pmod p.
$$

指数化时，所有较低项的乘积仍为 $p$ 整的，故得到 (2)。
这里的 $x$ 系数整性与首分母定位也见
[固定 sigma 与惰性分母](2026-11-12-fixed-sigma-height-and-inert-denominator.md)
及 [R38 的准确半径证明](../results/R38-exact-inert-sigma-size-and-jet-budget.md)。

定义整数递推

$$
 U_0=0,\quad U_1=1,\quad U_n=4U_{n-1}-5U_{n-2}
       =\frac{(2+i)^n-(2-i)^n}{2i}.
$$

由 (1)，对每个 $n$ 有准确等式

$$
 c_n=\frac12 U_n t_n.
$$

因为 $i^p=-i$，模 $p$ 有
$\alpha^{p+1}=\bar\alpha^{p+1}=5$，所以 $p\mid U_{p+1}$。
结合 (2)，得

$$
 \boxed{\quad
 v_p(c_{p+1})=v_p(U_{p+1})-1,\qquad
 c_{p+1}\equiv\frac{\kappa_p}{2}\frac{U_{p+1}}p\pmod p.
 \quad}                                                     \tag{3}
$$

特别地，$c_{p+1}$ 是单位，当且仅当

$$
 U_{p+1}(4,5)\not\equiv0\pmod{p^2}.                         \tag{4}
$$

也可写成固定范数一数 $q=(2+i)/(2-i)$ 的条件
$q^{p+1}\not\equiv1\pmod{p^2}$。这是准确的二阶 Frobenius 商，
仅知道 $q^p\equiv q^{-1}\pmod p$ 不保留 (4)。

## 3. 完整惰性半因子的中心导数确实处处非零

首层的单位条件 (4) 不是这里最强的结论。采用
[实际惰性半因子笔记](2026-11-12-inert-central-mahler-half-factor.md)
中 $S(z)=\theta(2z)$ 的已证解析函数 $J_{0,p}$，设 $d=p+1$、
$c$ 为该笔记取出的 sigma 首坏项。于是

$$
 J_{0,p}(k)=k!(4c)^{-k}[z^{dk}]\theta(2z),\qquad
 J_{0,p}(0)=1.
$$

因为 $2^{1-p}\in1+p\mathbb Z_p$，下式是 $u=0$ 邻域中的实际解析函数：

$$
 J_{\theta,p}(u)=(2^{1-p})^uJ_{0,p}(u),\qquad
 J_{\theta,p}(k)=k!c^{-k}t_{dk},\qquad J_{\theta,p}(0)=1.
                                                               \tag{5}
$$

在未分歧二次域 $K_p=\mathbb Q_p(i)$ 中定义

$$
 a_p=\frac{\alpha^{p+1}}5,\qquad
 b_p=\frac{\bar\alpha^{p+1}}5.
$$

两者均属于 $1+p\mathcal O_{K_p}$。由 (1) 得到的准确插值函数是

$$
 \boxed{\quad
 J_{C,p}(u)=\frac{a_p^u-b_p^u}{4i}\,J_{\theta,p}(u),\qquad
 J_{C,p}(k)=k!(5c)^{-k}c_{dk}.
 \quad}                                                       \tag{6}
$$

因此

$$
 \boxed{\quad
 J_{C,p}(0)=0,\qquad
 J_{C,p}'(0)=\frac{p+1}{4i}
       \log_p\!\left(\frac{2+i}{2-i}\right)\ne0.
 \quad}                                                       \tag{7}
$$

最后一个非零结论完全无条件：$p$ 进对数在
$\mathcal O_{K_p}^{\times}$ 的核是根单位；
$q=(2+i)/(2-i)=(3+4i)/5$ 不是 $\mathbb Q(i)$ 的根单位
$\{\pm1,\pm i\}$。若其像在 $K_p$ 是根单位，嵌入的单射性会给
$q^n=1$，矛盾。这里使用的是一个固定代数数的对数，未对含
$\mathbb Q_p$ 系数的线性组合误用 Baker 定理。

并且对 $q^d\in1+p\mathcal O_{K_p}$ 使用对数的等距性，准确有
$v_p(J_{C,p}'(0))=v_p(U_{p+1})$。故 (3) 的首层单位性只检测
该非零导数的赋值是否恰为一。

这说明首层可能很深并不妨碍中心导数非零。特别地，不能把 (4)
的困难当作证明完整半因子导数非零所必需的条件。

## 4. 普通单 Euler 关系与原始性的准确区别

对普通 $p\ge7$、$p\ne5$，把 $\theta$ 的整正式级数经同一
高度一正式群参数化写成有界测度 $\nu_\theta$。它是 $E_0$ 的
秩零参考 theta 测度；$S=\theta(2z)$ 的缩放只改变单位 Mellin
变换的一个解析单位。令 $\mu_\theta$ 是其 principal tame
分量的单位限制，$G_\theta$ 为 Mellin 变换。由秩零参考的
中央插值、$d_0/f_0=1/4$ 及非零 Euler 因子，

$$
                         G_\theta(0)\ne0.                    \tag{8}
$$

此处所需的平方根构造与常数见
[参考 theta 规范](2026-11-12-dyadic-vector-and-reference-theta.md)
及 [R46 的同一测度构造](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)；
没有另外选择依赖权重的平方根符号。

在选定的 $K\hookrightarrow\mathbb Q_p$ 中，$\alpha,\bar\alpha$ 都是单位，
所以 (1) 的测度准确为

$$
 \nu_C=\frac{[\alpha]_*-[\bar\alpha]_*}{4i}\nu_\theta.
                                                               \tag{9}
$$

写 $\ell(x)=\log_p\langle x\rangle/\log_p(1+p)$。
主 tame 平均与缩放交换，故

$$
 G_C(T)=\frac{(1+T)^{\ell(\alpha)}-(1+T)^{\ell(\bar\alpha)}}{4i}
          G_\theta(T),
$$

$$
 G_C'(0)=\frac{\log_p q}{4i\log_p(1+p)}G_\theta(0)\ne0.       \tag{10}
$$

它也满足**参考 $E_0$ 的**准确单 Euler 关系。为核实可能存在的
原点原子，令 $\pi_0=\psi_0(\mathfrak p)$、
$a=\pi_0/\bar\pi_0$、$c_0=\bar\pi_0^{-1}$。
按[单 Euler 分布证明](2026-11-12-theta-principal-tame-euler-distribution.md)
的正权矩、乘法卷积和环带整域论证，对参考测度先得到

$$
 \nu_\theta^{(0)}|_{p\mathbb Z_p}
       -c_0[a]_*\nu_\theta^{(0)}=\gamma_p\delta_0
                                                               \tag{11}
$$

对某个常数 $\gamma_p$ 成立。这里不必未经证明地把该常数置零：
正权矩只确定去掉原点后的测度，符号由单位环带上
$G_\theta\ne0$ 固定。把 (9) 的差算子作用于 (11)；该算子
杀死 $\delta_0$，并与 $[a]_*$、主 tame 平均及两个支撑限制交换，遂得

$$
 \boxed{\quad
 \nu_C^{(0)}|_{p\mathbb Z_p}
       =\bar\pi_0^{-1}[\pi_0/\bar\pi_0]_*\nu_C^{(0)}.
 \quad}                                                       \tag{12}
$$

然而这没有产生一个新的秩二曲线的原始 Katz 因子。
式 (10) 说明其平方测度是在参考 $E_0$ 的平方因子上乘以

$$
 \left(\frac{(1+T)^{\ell(\alpha)}-(1+T)^{\ell(\bar\alpha)}}{4i}\right)^2,
                                                               \tag{13}
$$

这是中心恰有二阶零点的**非单位**，而 $E_0$ 的原始中心值非零。
故不能把该乘法视为不改变 Selmer 特征理想的规范变更。
本篇证明了参考曲线上的显式非原始构造；没有建立任何秩至少二的
固定曲线与 $C$ 的原始中央插值等式。

## 5. 原十七次截面不属于这两个无平移缩放的张成

还可准确排除将上面的简化直接搬到实际 $A_{17}$。
在 $D=1$ 规范下，令 $V=x^{-2}$，$\beta=4-i$。已证明

$$
 \frac{\theta(\beta z)}{\theta(z)^{17}}
 =1+(12-20i)V+(-10+28i)V^2+(-20-12i)V^3+(1+4i)V^4.
                                                               \tag{14}
$$

共轭给出 $\bar\beta$ 的式子。若一个线性组合
$a\theta(\beta z)+b\theta(\bar\beta z)$ 在原点为零，则
$a+b=0$，其归一多项式只能为

$$
             V-\frac75V^2+\frac35V^3-\frac15V^4.             \tag{15}
$$

实际 $A_{17}/\theta^{17}$ 则为

$$
             V+\frac35V^2-\frac15V^3+\frac15V^4.             \tag{16}
$$

两者不同。因此实际的十七次截面不能由这两个范数 $17$ 的
无平移 CM 缩放之差给出。范数 $17$ 的高斯整数只有这两个方向
及其 $\mu_4$ 倍，而 $\theta(iz)=\theta(z)$；故这已穷尽这类
整数 CM 缩放。它不排除带挠点平移的十七维基或更一般的比较，
但那些变换必须保留相应的完整测度，而不能把加法卷积当成 Mellin 乘法。

## 6. 引用范围

相关一手文献的范围须严格保留：Anitha–Fathima–Vijayalakshmi，
*Lucas non-Wieferich primes in arithmetic progressions and the abc conjecture*
（2022 版本；2023 发表），[arXiv:2101.04901v5](https://arxiv.org/pdf/2101.04901)，
§2 明确假设 $P^2-4Q>0$，Theorem 3.1 另假设数域的 $abc$ 猜想。
正式发表版为 *Open Mathematics* **21** (2023), 20220563，
[DOI:10.1515/math-2022-0563](https://doi.org/10.1515/math-2022-0563)，
相应结论编号为 Theorem 1.2，正判别式假设在 Definition 1.1 后再次明写。
本例 $(P,Q)=(4,5)$ 的判别式为 $-4$，不能直接套用该定理，
更不能去掉其 $abc$ 假设。
本例的 (1)–(4) 均由上面的恒等式证明，不依赖该文献。
