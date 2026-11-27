# R1084：原 Gaussian 的指定高 Hurwitz 单位与最大 forced 标签的准确次数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta，o2 独立纸核。

**已证明。** 固定原 supersingular Gaussian reference
$$
E_a:\ y^2=x^3+ax,\qquad
a\in\mathbf F_p^\times,\quad p\ge41,\quad p\equiv3\pmod4,
\qquad \omega=\frac{dx}{2y}.
$$
所有坐标、微分、marked CM lift 和原 full-level 相位沿用
R1071、R1079、R1082。Hurwitz 系数使用原 additive-coordinate 规范
$$
x(z_{\rm add})=z_{\rm add}^{-2}
 +\sum_{\substack{j\ge4\\j\ {\rm even}}}
       (j-1)G_jz_{\rm add}^{j-2}.
$$
令 $D=d/\omega$，原 Deuring primitive 的归一为
$\Psi\sim T^{-p}$、$D\Psi=\delta$。则 $\delta\in\mathbf F_p^\times$，且
$$
\boxed{\qquad
\overline{G_{7p-1}}=-\frac{2a^2}{315\delta}\ne0.
\qquad}
\tag{1084.1}
$$

它准确落到原最大 forced 角色
$$
m=\frac{p-1}{2},\qquad
R=m+3=\frac{p+5}{2},\qquad \chi=\omega^R.
$$
在该 Gaussian coarse component 上，原 raw 标签多项式的次数恰为
$(p-7)/4$，最高系数是原相位乘所示单位。若这个实际角色
Bernoulli-good，则同一唯一 global 候选坐标也有这一准确次数和单位最高系数。

本篇没有证明 R1082 第一 forced affine 标签的指定卷积
$\mathcal H_p$ 非零，也没有证明原 $f_N/e$、短 $\eta_k,\nu_k$ 或
O2 bare 系数非零。这里的 $G_{7p-1}$ 是另外一个已经完整识别的原指定输入。

## 1. 同一个原参数与两个全局 primitive

取 R1071 §11、R1079 的原 tangent-one 整 CM eigenparameter $T$。
同一 characteristic-zero lift 上
$$
z_{\rm add}(T)=T+O(T^{p^2}),\qquad
\omega=(1+O(T^{p^2-1}))\,dT.
\tag{1084.2}
$$
第一式的 $T^{p^2}$ 系数可能含 $p$ 分母；本文只在严格更低的次数使用它。
不将整个 characteristic-zero logarithm 或 $\zeta^p$ 约化。

写 $p=4r-1$。原函数和单位是
$$
\Psi=y\sum_{j=0}^{r-1}c_jx^{2j},\qquad
c_{r-1}=-1,\qquad
\frac{c_j}{c_{j-1}}=-\frac{4j-1}{a(4j+1)},
\qquad \delta=ac_0.
\tag{1084.3}
$$
递推的全部整数因子在 $1,\ldots,p-1$ 内，因此 $\delta$ 是单位；
首项 $x\sim T^{-2},y\sim-T^{-3}$ 固定了 $\Psi$ 的首极为 $+T^{-p}$。

R1082 §2 已用原 $\mu_4$ 作用、全局 pole 界和 residue theorem 完整证明
$$
D^{p-2}x=\Psi,\qquad
D^{p-3}x=\mathcal R=\frac{\Psi^2-x^p}{2\delta},
\qquad
C_{\rm rel}(x\omega)=-\delta\,\omega'.
\tag{1084.4}
$$
这里 $\mathcal R$ 的首负项为 $T^{1-p}$；两个 primitive 的常数由
原奇偶及 $\mu_4$ 角色排除，未将特征 $p$ 中的任意 primitive 当作唯一。

低系数 $G_j$ 对 $4\le j\le p-3$ 的偶数均 $p$-整：
其准确表达为 $2\mathcal E_j/(j-1)!$，其中 $\mathcal E_j$ 是
R1075 的 coefficient-one Hecke Eisenstein series。
Gaussian 权又使 $G_{p-1}=0$ 严格成立。故
$$
Z(T)=T^{-1}
-\sum_{\substack{4\le j\le p-1\\j\ {\rm even}}}
       \overline{G_j}T^{j-1}
$$
是合法的有限 Laurent polynomial。R1079 的原短 carry 是
$$
\Psi(T)=Z(T)^p+\delta T+O(T^{p^2}).
\tag{1084.5}
$$
这条恒等式在整 $T$ 上成立，已经支付首负极在原 formal addition
中的替换精度。

## 2. 读取 7p−1 的全部精度与阶乘

置
$$
d=7p-1,\qquad M=6p,\qquad M+p-3=d-2.
$$
因为 $p\ge41$，
$$
d-2=7p-3<p^2-3,\qquad M=6p<p^2-p.
\tag{1084.6}
$$

先把 (1084.2) 代入 $x$ 的原展开。首负二极的参数替换最早影响
$T^{p^2-3}$，严格高于 $d-2$；其它项也不能影响本次读数。因此
$$
[T^{d-2}]x(T)=(d-1)G_d.
$$
$x(T)$ 是原 good model 上的整 Laurent series，而
$d-1\equiv-2\pmod p$ 是单位。这同时支付本篇高 $G_d$ 的整性。

在 $D^{p-3}x$ 中，把 $D$ 换为普通 $\partial_T$ 的最早误差次数至少为
$p^2-p$。确实，每个误差含 $T^{p^2-1}$；从 $x$ 的首负二极开始，
一次这样的误差后再施至多 $p-4$ 次导数，其次数仍至少为 $p^2-p$。
多个误差更高。因此在 $T^M$ 处没有这一误差：
$$
[T^M]\mathcal R
 =(p-3)!\,(d-1)\overline{G_d}.
$$
下降阶乘模 $p$ 的因子恰是 $p-3,p-4,\ldots,1$，没有零因子。
Wilson 给
$$
(p-3)!=-\frac12,\qquad d-1=-2\pmod p,
$$
故准确为
$$
[T^{6p}]\mathcal R=\overline{G_{7p-1}}.
\tag{1084.7}
$$

将 (1084.5) 平方时，误差与首负 $p$ 极相乘最早从 $p^2-p$ 开始；
仍由 (1084.6) 排除。于是
$$
\mathcal R
 =\frac{Z^{2p}-x^p}{2\delta}
   +TZ^p+\frac{\delta T^2}{2}
\quad\text{至本次读数精度}.
$$
$TZ^p$ 的指数全部为 $1\bmod p$，不贡献 $T^{6p}$。
Frobenius 因而准确给
$$
\overline{G_{7p-1}}
 =\frac1{2\delta}
   \left([T^6](Z^2-x)\right)^p.
\tag{1084.8}
$$
这里没有省掉低平方中的 regular 卷积。
在扩域标架中首先保留这个 $p$ 次幂；只有当前
$\mathbf F_p$ reference 才可直接删去。

## 3. 完整短系数是一个明确单位

同一原 Weierstrass equation 和微分给
$$
x(z_{\rm add})
 =z_{\rm add}^{-2}-\frac a5z_{\rm add}^{2}
    +\frac{a^2}{75}z_{\rm add}^{6}+\cdots.
$$
例如直接用 $x''=6x^2+2a$ 比较常数和四次项即可得到这两个系数。
因此
$$
G_4=-\frac a{15},\qquad G_8=\frac{a^2}{525}.
$$
在所需次数上 $T$ 与 $z_{\rm add}$ 相同，Gaussian 其余低权项为零。
所以完整平方差恰为
$$
\begin{aligned}
[T^6](Z^2-x)
 &=(-2G_8+G_4^2)-7G_8\\
 &=-9G_8+G_4^2\\
 &=-\frac{4a^2}{315}.
\end{aligned}
\tag{1084.9}
$$
将其代入 (1084.8)，在当前 $\mathbf F_p$ reference 上得到 (1084.1)。
分母只含 $2,3,5,7$，均不等于 $p\ge41$；$a,\delta$ 也都是单位。
这是一条严格的全 $p$ 单位结论，不以新扫描或旧数值回执为依据。

## 4. 原最大 forced 角色的最高项

仍取 R1071 的实际 $V=C_\Sigma[p]$ 和同一 forced 子模块。
该文 §15.2 对 $p\equiv3\bmod4$ 的最大 forced $j$ 已支付
$$
R=m+3=\frac{p+5}{2}.
$$
因此当前 $\chi=\omega^R$ 是一个真实出现的角色；不是任取的
formal character。它既非平凡也非二次角色。

令
$$
N=(p+1)R,\qquad d_i=N-(p-1)i.
$$
R1071 §15 的 Lucas 消去给 fine 次数至多
$$
p-R=\frac{p-5}{2}.
$$
这个整数为奇数。Gaussian 原 $\mu_4$ 权只允许偶数 $i$，
故最高可能的非恒定项是
$$
i_0=p-R-1=\frac{p-7}{2},\qquad
d_{i_0}=7p-1,\qquad
\frac{i_0}{2}=\frac{p-7}{4}.
\tag{1084.10}
$$
所有更高项已由 Lucas 或 $\mu_4$ 严格为零，不能留下一个
未经计算的更高项抵消本项。

选择同一奇数 regularizer $c$，其模 $p$ 类生成
$\mathbf F_p^\times$。原 regularizer 是
$$
\kappa_\chi=c^2-\chi(c^2)=c^2-c^6\ne0.
$$
最后的非零来自 $c$ primitive、$p>5$。原 sigma/division identity 的
同一 $d\log$ 给
$$
A_d=-(c^d-c^2)\overline{G_d}
    =\kappa_\chi\,\overline{G_{7p-1}},\qquad d=7p-1.
\tag{1084.11}
$$
本次 $d-1=7p-2<p^2-2$，所以原首 pole 的参数替换修正仍严格在其后；
(1084.11) 是同一 eigen-$T$ 中的 $A_d$，不是任意 Weierstrass 参数读数。

为核完整二项式尺度，$d-1\equiv p-2$，且 $i_0$ 为偶数，因此
$$
\frac1{i_0}\binom{d-1}{i_0-1}
 =\frac1{i_0}\binom{p-2}{i_0-1}
 =-1\pmod p.
\tag{1084.12}
$$
这是原非零 Lucas 低位读数；$i_0<p$，分母是单位。

将 (1084.11)–(1084.12) 代回 R1071 (1071.20)，保留原
$\beta_0$、$\lambda$，得到 raw coarse 多项式的最高系数
$$
\boxed{
[T_{\rm coarse}^{(p-7)/4}]\mathcal P_{\chi,s}
 =\beta_0^{\,7p-1}\lambda^{(p-7)/2}\kappa_\chi
      \overline{G_{7p-1}}
 =-\frac{2a^2\beta_0^{\,7p-1}\lambda^{(p-7)/2}
                  \kappa_\chi}{315\delta}\ne0.
}
\tag{1084.13}
$$
因此该 raw 多项式的 coarse 次数**恰为** $(p-7)/4$。
这条未除圆单位基的结论不要求 Bernoulli-good。

## 5. 唯一 global 坐标与两条原 twist 支路

若当前角色 Bernoulli-good，即 $p\nmid B_R$，R1071 (1071.24) 的
原 circular-unit leading coefficient $b_\chi$ 是单位。
原 global 候选坐标是
$$
c_{\chi,s}=\frac{m}{\kappa_\chi b_\chi}\mathcal P_{\chi,s},
\qquad m=-\frac12\pmod p.
$$
其最高系数因而准确为
$$
\boxed{
[T_{\rm coarse}^{(p-7)/4}]c_{\chi,s}
 =\frac{a^2\beta_0^{\,7p-1}\lambda^{(p-7)/2}}
             {315\delta b_\chi}\ne0.
}
\tag{1084.14}
$$
不声称这个 particular 角色对每个 $p$ 都 Bernoulli-good。
R1069 全部 forced-good 角色的维数结论也不能用来替代这一个
指定 $b_\chi$ 的单位条件。

Gaussian coarse 参数为 $T_{\rm coarse}=t^2$。
必须同时保留 R1071 §8 的两条实际 quartic-twist descent lines：
在共同几何 fine frame 中分别为
$$
t^p=t,\qquad t^p=-t.
$$
它们一起覆盖全部 $T_{\rm coarse}\in\mathbf F_p$。
不能仅取第一条线的平方像。

每次实际同构或 full-level 标记运输时，$a,\delta$、参数、
$\beta_0,\lambda$ 及定义 $b_\chi$ 的 Weil root $\gamma$
都按原来源一起运输。局部计算先用 (1084.8) 的 Frobenius 形式，
再回到选定的 $\mathbf F_p$ reference；(1084.13)–(1084.14)
保留这些共同尺度，没有任意独立消掉一个 phase。
两条 twist 上的表达是同一个原 coarse 标签函数的表达。

## 6. 后继范围与未付款输入

本篇真正新增的是：

- 同一原 Gaussian 曲线的指定高系数
  $G_{7p-1}=-2a^2/(315\delta)$ 对全部所述 $p$ 为单位；
- 它与实际最大 forced 角色的最高项完全相同源，
  给 raw coarse 多项式的准确次数 $(p-7)/4$；
- 若该指定角色 good，则给唯一 global 候选坐标的准确单位最高系数，
  保原两个 twist 支路和全部尺度。

准确次数不表示这个高次多项式在 $\mathbf F_p$ 上单射，
也不表示它与辅助原像相容时只剩 CM 点。
本篇不解决 R1082 的第一 forced affine 斜率
$\mathcal H_p\ne0$，不将其与已经证明的 $G_{7p-1}$ 混同。
原 $f_N/e$、短 $\eta_k,\nu_k$、same-$h$ 筛选和 O2 bare 仍按各自来源继续。

来源：[R1071](R1071-original-p-local-cuspidal-label-polynomials.md)
§§5–8、11、15–16；
[R1079](R1079-original-CM-Psi-zeta-short-carry.md)；
[R1082](R1082-original-Gaussian-high-Hurwitz-and-complete-short-convolution.md)
§§1–3。
本篇给出本次全部新系数、误差界、Wilson/Lucas 因子和原角色读数。
root 与 o2 独立逐式纸核；未运行数学程序，未重扫旧窗，也没有新增数值窗口。
