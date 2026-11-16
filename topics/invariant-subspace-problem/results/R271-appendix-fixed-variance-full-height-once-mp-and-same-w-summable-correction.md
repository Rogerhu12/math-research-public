# R271 附录：固定方差倍数支付全部高度的一次完整 MP 与同 W 可和修正

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 原全孔层右逆含次数指数 $512^j$，不能用 primitive 限制逆的多项式费用替代。本稿保留这一指数，利用同源阻尼列中的 $(S/s)^j$，在一个固定方差倍数窗内支付全部 $1\le j<h$ 的一次完整 $D^\dagger$。没有截掉 $j\asymp x$ 的中段，也没有把完整头源限制到低孔。

接此前同一 $w$ 的全高度 coherent Bessel 定理，得到原完整头逆之后的一次修正、修正后残量和相对于强头真空截断的误差，其平方跨 $m$ 可和。所得向量尚非物理真核；有限顺次修复的最后真空约束仍会消去初始阻尼，本文未支付该完整过程。

依据：

- [原连续尾完整 coherent 列及 Bernoulli 原像](R271-appendix-continuous-tail-coherent-columns-bernoulli-lifts-and-exact-residuals.md)，§§1、4–5；
- [小阻尼截断的一次完整 MP](R271-appendix-damped-small-height-complete-once-mp-residual-and-moving-head-budget.md)，§§1–3；
- [放大方差、完整源与同实际投影](R271-appendix-enlarged-variance-inverse-grams-and-same-source-damped-coherent-moments.md)；
- [跨头全高度 coherent Bessel 及同 W 完整逆能量](R271-appendix-cross-head-all-height-coherent-bessel-and-same-w-full-energy-summability.md)，§§4–5。

## 1. 原全层自然域和完整头源

对整数 $x\ge1$，令
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
S=S_x=\sum_{i\ge x}(i+1)^{-4},
$$
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2=(j!)^2e_j(b^2).
$$
$D$ 在全部 Boolean Hilbert 空间有界。原全孔层右逆给
$$
D:\mathcal H_{j+1}\longrightarrow\mathcal H_j
\quad\hbox{满射},\qquad
\left\|D^\dagger|_{\mathcal H_j}\right\|
\le 12\,512^j(x+j+1)^{3/2}.
\tag{1.1}
$$
这是完整层的预算，非 primitive 压缩。全直和 $D^\dagger$ 可以无界；以下所有向量只使用有限个孔层，因此均在其自然域。

设实际有限强头满足 $C^h=0$，$h\ge1$。$C$ 和所有纯尾算子作用不同张量因子。对任意完整头源 $g$，置
$$
c_*=2\cdot512^2,\qquad
s\in[c_*S,\,2c_*S],
$$
$$
H(s)=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{j!s^j},
\qquad a=H(s)^{-1}g,
\qquad E_j(s)=\frac{\|C^ja\|^2}{j!s^j}.
\tag{1.2}
$$
始终保留整个 $H(s)^{-1}$。定义原物理阻尼列
$$
f_s=\sum_{j=0}^{h-1}\frac{(-C)^ja\otimes\omega_j}{j!s^j},
\qquad
\epsilon_s=\sum_{j=1}^{h-1}E_j(s).
\tag{1.3}
$$
不同远孔层正交。由 $\sigma_j^2\le j!S^j$，
$$
\|f_s\|^2\le \sum_{j=0}^{h-1}E_j(s)
=\langle g,H(s)^{-1}g\rangle\le\|g\|^2.
\tag{1.4}
$$

## 2. 一次 MP 的准确同层平方

令 $\mathscr L=C+D$。在远孔 $0\le j\le h-2$ 上，
$$
(\mathscr Lf_s)_j=
\frac{(-C)^{j+1}a}{(j+1)!s^{j+1}}
\otimes\bigl[D\omega_{j+1}-(j+1)s\omega_j\bigr].
\tag{2.1}
$$
最高远孔 $h-1$ 的额外项为 $C(-C)^{h-1}a=0$，这里使用真实 $C^h=0$。因此不存在被删去的 top。

$\omega_{j+1}\in\operatorname{Ran}D^*$，故
$$
D^\dagger D\omega_{j+1}=\omega_{j+1},
\qquad
\langle\omega_{j+1},D^\dagger\omega_j\rangle=\sigma_j^2.
$$
于是
$$
\begin{aligned}
&\left\|D^\dagger\bigl[D\omega_{j+1}-(j+1)s\omega_j\bigr]\right\|^2\\
&\quad=\sigma_{j+1}^2-2(j+1)s\sigma_j^2
+(j+1)^2s^2\|D^\dagger\omega_j\|^2.
\end{aligned}
\tag{2.2}
$$
同一 $D^\dagger$ 的不同输入层落在不同输出层，故有准确平方和
$$
\boxed{
\|D^\dagger\mathscr Lf_s\|^2
=\sum_{j=0}^{h-2} k_j(s)E_{j+1}(s),
}
\tag{2.3}
$$
其中
$$
k_j(s)=
\frac{\sigma_{j+1}^2-2(j+1)s\sigma_j^2
+(j+1)^2s^2\|D^\dagger\omega_j\|^2}
{(j+1)!s^{j+1}}\ge0 .
\tag{2.4}
$$
$h=1$ 时两边均为零。此处没有令 MP 与 $D$ 在任意源上交换。

## 3. 完整指数费用由固定阻尼支付

在 (2.4) 中仅为上界删去负交叉项。用 (1.1) 和
$\sigma_j^2\le j!S^j$，得到
$$
k_j(s)\le
\left(\frac S s\right)^{j+1}
+144(j+1)s(x+j+1)^3
\left(\frac{512^2S}{s}\right)^j.
\tag{3.1}
$$
这保留了真正的全层指数。

对 $x\ge1$，
$$
S\le\frac1{3x^3},\qquad x+j+1\le x(j+2),
\qquad \frac{512^2S}{s}\le\frac12.
$$
又 $s\le2c_*S$，故
$$
k_j(s)\le
1+96c_*(j+1)(j+2)^3\,2^{-j}.
\tag{3.2}
$$
幂级数直接计算给
$$
\sum_{j\ge0}(j+1)(j+2)^3\,2^{-j}=496.
$$
因此可取明确的绝对常数
$$
K_*=1+47616c_*
$$
使
$$
\boxed{
\|D_x^\dagger(C+D_x)f_s\|^2
\le K_*\epsilon_s.
}
\tag{3.3}
$$
常数虽保守，但不依赖 $x,h,C,g$。特别没有假设 $h=o(x)$ 或
$j\le S/(4b_x^2)$；全部高度均包含在同一个平方和中。

低孔正交换子 $DD^*\ge S-2jb_x^2$ 确能另给低高度预算，但不是 (3.3) 用来处理全部中段的依据。

## 4. 保持原同源投影及全部 Q 门

现在取原真实强头
$$
C=A_m+D_{[m,x)},\quad R=x-m,\quad h=2^m+R.
$$
原阻尼列的低 forcing 同余在
$$
Q\ge R+h-1
\tag{4.1}
$$
给
$$
P_{V_Q}f_s=P_{V_Q}i_0g,\qquad
P_{K_Q}f_s=P_{K_Q}i_0g,
\qquad
u_g=(P_{V_Q}-P_{K_Q})f_s.
\tag{4.2}
$$
这是逐列低伴随同余，不是宣称 $f_s\in\ker(C+D)$。

置 $q_s=\langle g,H(s)^{-1}g\rangle$。完整正规方程精确给
$$
d_s:=\|g\|^2-q_s
=\|g-a\|^2+\epsilon_s.
\tag{4.3}
$$
由 (1.3) 的远孔正交，
$$
\|f_s-i_0g\|^2
=\|a-g\|^2+
\sum_{j=1}^{h-1}
\frac{\sigma_j^2}{j!s^j}E_j(s)
\le d_s.
\tag{4.4}
$$
同时 $\|u_g\|^2\le\|f_s\|^2\le q_s$，所以
$$
\epsilon_s\le d_s\le
\|i_0g-u_g\|^2.
\tag{4.5}
$$

令
$$
q_1=D^\dagger(C+D)f_s,\qquad z_1=f_s-q_1.
$$
完整层的 $DD^\dagger=I$ 以及头尾张量交换给
$$
\boxed{
Dz_1=-Cf_s,\qquad
(C+D)z_1=-Cq_1 .
}
\tag{4.6}
$$
$q_1,z_1$ 均只有远孔 $\le h-1$，所有 (4.6) 的算子作用在同一自然域。并有
$$
\|z_1-i_0g\|^2\le2(1+K_*)d_s,\qquad
\|(C+D)z_1\|^2\le K_*\|C\|^2d_s.
\tag{4.7}
$$
修正后的 $z_1$ 不再被声称有 (4.2) 的准确同余，但投影收缩给
$$
\|(P_{V_Q}-P_{K_Q})z_1-u_g\|\le\|q_1\|.
\tag{4.8}
$$
任意额外母窗、内部 cut 或帽条件仍独立保留；例如调用完整帽返回时仍需
$n+2h+R<Q$。

## 5. 原同一个 W 向量的全部一次修正平方可和

使用前篇全高度 Bessel 定理的原参数与同一个 $w\in W$：
$$
d_m=2^m,\quad
e^{(25/2)d_m^3}\le x_m\le e^{13d_m^3},\quad
h_m=d_m+x_m-m\le2x_m.
$$
取其合法母窗 $Q_m$，并满足 (4.1)。令
$$
g_m=P_{x_m}w,\quad
\eta_m=e^{-6d_m^4},
$$
$$
H_m^{\rm coh}=\sum_{j<h_m}
\frac{(C_m^*)^jC_m^j}{\sigma_{m,j}^2},
\qquad
\Delta_m=\|g_m\|^2-
\langle g_m,(H_m^{\rm coh})^{-1}g_m\rangle .
$$
前篇已证明
$$
\sum_m\Delta_m
\le\left(\sqrt2+2\sqrt{\sum_m\eta_m^2}\right)^2\|w\|^2.
\tag{5.1}
$$
对任意先于全部 cut 选定的
$s_m\in[c_*S_{x_m},2c_*S_{x_m}]$，
$H_{C_m}(s_m)\preceq H_m^{\rm coh}$，故 $d_{m,s_m}\le\Delta_m$。
无需新的 log-variance 选择，直接有
$$
\boxed{
\sum_m\|D_{x_m}^\dagger(C_m+D_{x_m})f_{m,s_m}\|^2
\le K_*\sum_m\Delta_m<\infty .
}
\tag{5.2}
$$
原实际头范数有统一上界 $M_C=\sup_m\|C_m\|<\infty$，所以同时
$$
\boxed{
\begin{aligned}
\sum_m\|z_{1,m}-P_{x_m}w\|^2
&\le2(1+K_*)\sum_m\Delta_m,\\
\sum_m\|(C_m+D_{x_m})z_{1,m}\|^2
&\le K_*M_C^2\sum_m\Delta_m .
\end{aligned}
}
\tag{5.3}
$$
(5.2) 是完整一次 MP 的物理向量平方和，不是只有各个固定测试的弱行。
所有实际高度都使用同一个完整 $H_{C_m}(s_m)^{-1}g_m$；没有将
$g_m$ 换成某个固定低头源。

## 6. 最终核约束仍不由一次阻尼支付

若继续作全部顺次修复使远孔分量 $y_j$ 真满足
$$
Dy_{j+1}=-Cy_j,\qquad y_0=a ,
$$
则必有
$$
D^j y_j=(-C)^ja.
\tag{6.1}
$$
这条最终真空约束没有初始阻尼 $(s^{-j})$。因此不能把 (3.3) 反复应用于
已经含 $D^\dagger\omega_j$ 的新尾列，更不能从 (5.2) 直接断言一个相容真核塔的统一费用。

本稿支付的是整个高度的一次真实 MP、它的准确剩余 $-Cq_1$ 及跨 $m$ 平方和。
原全部顺次返回、零源 Schur、受限 $q_{\flat}$ 二次型和帽逆伴随费用仍保留；
这里没有证明 $N=M$。
