# R239 附录：全部短 jet 次数锚的同源裸费用与原窗口预算

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_nonprimitive_1856；AI-assisted，GPT-6 Astra Pro。
状态：全部短核阶的实际同源裸锚费用已显式证明。这是原完整连续尾上的有限参数上界，不是假设参数一致角度；本稿不声称已经达到无误差因子的全左费用求和阈值。普通 ISP 与 $N=M$ 均为 OPEN。

本文使用已发表的[顺次次数算子与真幂 Schur 比较](R239-appendix-sequential-jet-number-and-true-power-schur-comparison.md)及[单 dyadic 块导数交织](R239-appendix-single-dyadic-block-derivative-intertwiner-and-exact-jet-anchor.md)。新增的是无需任何未证角度条件的全 $K$ 实际数值预算；不重复其中 $K=3$ 和裸费 $K=2$ 的最佳常数推导。

## 1. 一个共同的原 primitive MP 族

固定
$$
m\ge5,\quad d=2^m,\quad4d\le q\le e^{d^3/4},
\qquad1\le K\le d-1.
\tag{1.1}
$$
仍令 $D=D_m$，$\nu=\|D_m\|\le\sum_{j\ge m}(j+1)^{-2}\le1/m$，
$P_0=P_{\ker D}$，$E_{K,q}=\ker D^K\cap\mathcal H_q$。

为覆盖下面输出孔层至 $q+1$、最大原像阶 $K$ 的全部项，在[高孔笔记 §14](../notes/2026-11-13-actual-high-hole-first-head-tests-and-transverse-observation-gap-1cf.md)取共同输入上界 $P=q+1$、最大阶 $T=K$。该笔记参数中的 $q'=P-T=q+1-K$ 是辅助值，不改变原实际源层 $q$。同一个相容族给
$$
\boxed{\mathcal L=512\sqrt{q+K+2}\,(m+q+K+2)^{3/2}.}
\tag{1.2}
$$
正规化后，对 primitive $f\in\ker D\cap\mathcal H_n$、$n\le q+1-t$，
$$
Q_t f=D_{n+t}^\dagger\cdots D_{n+1}^\dagger f,\qquad
P_0Q_tf=0,\quad DQ_tf=Q_{t-1}f,
$$
$$
\boxed{\|Q_tf\|\le2^{t-1}\mathcal L^t\|f\|,
\qquad1\le t\le K.}
\tag{1.3}
$$
这些是真正顺次单步最小原像；没有换成真幂 MP。

由于 $q\ge4d$、$K\le d-1$、$m\le d/2-1$（$m\ge5$），
$$
q+K+2\le q+d+1\le\tfrac32q,
$$
$$
m+q+K+2\le q+m+d+1\le\tfrac32q.
$$
故
$$
\boxed{\mathcal L\le1152q^2<2048q^2.}
\tag{1.4}
$$
保留后一个较松的常数以与既有原窗口预算统一。

## 2. 普通次数范数的显式全阶界

在 $E_{K,q}$ 上，准确 Taylor 身份为
$$
I=\sum_{t=0}^{K-1}Q_tP_0D^t,\qquad
\mathfrak N_{K,q}
=\sum_{t=0}^{K-1}(t+1)Q_tP_0D^t.
\tag{2.1}
$$
因此
$$
\boxed{\mathfrak N_{K,q}-I
=\sum_{t=1}^{K-1}tQ_tP_0D^t.}
\tag{2.2}
$$
这里 $P_0D^t h$ 永远是第 $q-t$ 孔层的 primitive 向量，恰在 (1.3) 的域中。特别无需假定 $D^t h$ 自身 primitive。

记
$$
b=\max\{1,2\mathcal L\nu\}\le4096q^2.
\tag{2.3}
$$
从 (1.3) 及 $\|P_0D^t\|\le\nu^t$，
$$
\|\mathfrak N_{K,q}\|
\le1+\sum_{t=1}^{K-1}(t+1)2^{t-1}(\mathcal L\nu)^t.
$$
所以对于 $K\ge2$，
$$
\boxed{\|\mathfrak N_{K,q}\|\le K^2b^{K-1}.}
\tag{2.4}
$$
$K=1$ 时准确为 $I$，同一右端也为一。证明 (2.4) 只用 $b\ge1$ 及
$\frac12\sum_{t=1}^{K-1}(t+1)+1\le K^2$；
不同 Taylor 像的非正交性已经由真实 (1.3) 范数支付。

## 3. 同一个 h 的裸度量运输

首头源 $e_0h$、$h\in E_{K,q}$ 的裸及完整右最小链均为只有首段的
$e_0D_{q+1}^\dagger h$，故
$$
\alpha_q(e_0h)=\lambda_q(e_0h)=\|D_{q+1}^\dagger h\|.
\tag{3.1}
$$
其真正源度量为
$$
W_{K,q}=(D_{q+1}^\dagger|_{E_{K,q}})^*
(D_{q+1}^\dagger|_{E_{K,q}}).
$$
顺次性给已证准确交织
$$
(\mathfrak N_{K+1,q+1}-I)D_{q+1}^\dagger
=D_{q+1}^\dagger\mathfrak N_{K,q}.
\tag{3.2}
$$
右侧全部在原同一个 $h$ 上读取。$\mathfrak N_{K+1}-I$ 在第 $q+1$ 层 primitive 子空间上为零，保持其真实正交补，因此
$$
\|\mathfrak N_{K,q}\|_{W_{K,q}}
=\|\mathfrak N_{K+1,q+1}-I\|_{E_{K+1,q+1}}.
\tag{3.3}
$$

将 (2.2) 用在 $q+1,K+1$，(1.3) 覆盖的最高阶恰为 $K$，得到
$$
\|\mathfrak N_{K,q}\|_{W_{K,q}}
\le\sum_{t=1}^{K}t\,2^{t-1}(\mathcal L\nu)^t
\le K^2b^K.
$$
记这个明确可用常数为
$$
\boxed{\Theta_{K,m,q}=K^2(4096q^2)^K.}
\tag{3.4}
$$
于是对于原全部 (1.1) 窗口、同一个 $h\in E_{K,q}$，
$$
\boxed{\alpha_q(e_0\mathfrak N_{K,q}h)
\le\Theta_{K,m,q}\alpha_q(e_0h),}
\tag{3.5}
$$
$$
\boxed{\lambda_q(e_0\mathfrak N_{K,q}h)
\le\Theta_{K,m,q}\lambda_q(e_0h).}
\tag{3.6}
$$
不存在换成低占据 Fock 模型、删除真实尾位或使用顺次／真幂 MP 交换的步骤。

## 4. 原平坦源保持不变的双源配对

对任意原实际左源 $r$，记 $L=J_q^{-1}$，$G=G_q$，$P$ 为物理首源头投影。完整右度量在这个头上准确为 $W^{-1}$，而 $P$ 约化 $G$，故
$$
\begin{aligned}
|\langle e_0\mathfrak N_{K,q}h,PLr\rangle|
&\le\alpha_q(e_0\mathfrak N_{K,q}h)
     \|G^{1/2}PLr\|\\
&\le\Theta_{K,m,q}\,
     \alpha_q(e_0h)\|G^{1/2}PLr\|.
\end{aligned}
\tag{4.1}
$$
这里 $\|G^{1/2}PLr\|$ 是原同一个 $r$ 的平坦对偶分量；没有把 (3.6) 的普通右费用当作 $\lambda_{\rm flat}$，也没有重新构造对偶源。

## 5. 单高块全 K 锚的指数账本

单 dyadic 块稿中的 $K=2^r$ 满足 $4\le K\le d/4$。对这些全部 $K$，
$$
\begin{aligned}
\log\Theta_{K,m,q}
&=2\log K+K(12\log2+2\log q)\\
&\le\frac18d^4+3d\log2+2\log d\\
&\le\frac18d^4+4d
\le\frac17d^4.
\end{aligned}
\tag{5.1}
$$
倒数第二步用 $\log2<1$、$\log d\le d/2$；最后一步用 $d\ge32$，使 $4d\le d^4/56$。

已付单块误差 $\varepsilon\le e^{-9d^4/2}$ 因而满足
$$
\boxed{\varepsilon\Theta_{K,m,q}
\le e^{-61d^4/14}\le e^{-4d^4}.}
\tag{5.2}
$$
普通次数范数 (2.4) 亦被同一 $\Theta$ 控制，所以相同乘积预算成立。

这精确支付了全 $K$ 的同源 jet-number 锚，只要待用表达式原本确有 $\varepsilon$ 因子。它没有令无误差项的 $\Theta^2$ 进入
$O(e^{d^3/4}/d)$ 的最终窗口求和阈值：对 $K$ 随 $d$ 增长，(3.4) 的对数可达四次量级，仍大于该无误差阈值。

## 6. 这一步之后的原源图接口

单高块稿的源恒等式保持为
$$
F_{\rm flag}\mathcal C_R
=B_Ua_{\rm hi}-b_{m-1}e_0\mathfrak N_{K,q}h,
\qquad
h=z_q,\quad\|\mathcal C_R\|\le\varepsilon.
$$
(3.5) 现在对该原同一个 $h$ 给出显式裸锚费用。但这条差源本身的便宜链并不自动分别支付其高分量和低分量的左最小范数；也不使物理锚 $B_{m,r}z$ 进入 $\mathscr V_q$。

下一源图步骤应保留真正 $M=B+LGL$ 正交投影和原同源平坦向量。本稿到此仅记录已完成的全阶费用，不以它替代后续图空间比较。
