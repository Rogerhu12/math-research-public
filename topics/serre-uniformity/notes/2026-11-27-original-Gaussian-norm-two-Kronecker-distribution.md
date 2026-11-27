# 原 Gaussian 的 $(1+i)$ 完整分布与 Kronecker 目标层

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient。

本笔记证明同一原 Gaussian 曲线上的完整二同源分布式，并把它逐项送到
[R1116](../results/R1116-original-Gaussian-forced-tangents-and-Kronecker-band.md)
的原反对角。所有较低齐次项都保留。得到的一个明确单位是
$[t^{p-3}]\,t\sqrt{x(t)}=5G_{p-3}$；
没有据此认定任一指定 $c_{2j-1}$ 非零，也不删除 Bernoulli-good mask。

## 1. 原参数、二挠点及两种平移核

沿用 R1082、R1114、R1116：
$$
E_a:y^2=x^3+ax,\qquad
a\in\mathbf F_p^\times,\qquad
p=4k+3\ge41,\qquad
\omega=dx/(2y).
\tag{N1}
$$
先在原 Gaussian CM lift 的不变 additive 参数 $t$ 中证明恒等式，
再在已付的有限整范围约化。保持 $\sigma'(0)=1$、
$\zeta=\sigma'/\sigma$、$x=-\zeta'$，不重新选择 period。
写
$$
\lambda=1+i,\qquad \bar\lambda=1-i,\qquad
\lambda\bar\lambda=2,\qquad Q=(0,0)\in\ker[\lambda]\setminus\{O\}.
$$
把同一个 $Q$ 也记为其复均匀化的一个代表，故
$2Q,\lambda Q\in\Lambda$。原核为
$$
\mathscr K(t,u)=\frac{\sigma(t+u)}{\sigma(t)\sigma(u)}.
$$
定义带实际指数补偿的二挠平移
$$
\mathscr K_Q(t,u)
=e^{-\zeta(Q)u}\mathscr K(t+Q,u).
\tag{N2}
$$
不单独约化这里的指数或半周期值；其有限代数展开由下面的
平方根恒等式给出。

原 Gaussian 对称性 $\zeta(it)=-i\zeta(t)$ 给
$\eta_{i\omega}=-i\eta_\omega$，所以
$\eta_{\lambda\omega}=\bar\lambda\eta_\omega$。
另一方面，奇性及 $2Q$ 的准周期给 $2\zeta(Q)=\eta_{2Q}$。
因此
$$
2\eta_{\lambda Q}
=\eta_{\lambda(2Q)}
=\bar\lambda\eta_{2Q}
=2\bar\lambda\zeta(Q).
\tag{N3}
$$
这固定了实际平移相位。

## 2. 无遗漏全纯项的线性分布

准确有
$$
\boxed{\quad
\lambda\mathscr K(\lambda t,u)
=\mathscr K(t,\bar\lambda u)
 +e^{-\zeta(Q)\bar\lambda u}
       \mathscr K(t+Q,\bar\lambda u).
\quad}
\tag{N4}
$$

**证明。** 固定一般的 $u$，视两边为 $t$ 的截面。
左边的两个极点类恰为 $0,-Q$。
在 $0$ 的留数为一；在 $-Q$ 的留数为
$e^{-\eta_{\lambda Q}u}$。
右边第一项在 $0$ 的留数为一，第二项在 $-Q$ 的留数为
$e^{-\zeta(Q)\bar\lambda u}$，由 (N3) 完全相同。

$t\mapsto t+\omega$ 时，左边的 multiplier 为
$e^{\eta_{\lambda\omega}u}=e^{\eta_\omega\bar\lambda u}$，
右边两项也都是这个 multiplier。
故差是同一 degree-zero flat line 的全纯截面。
一般 $u$ 下该 line 非平凡，没有非零全纯截面，故差为零。
再由亚纯延拓得到全部 $(t,u)$ 的恒等式。
在 $u=0$ 的首极也一致：
$\lambda/u=2/(\bar\lambda u)$。
这一步没有任意添加常数或全纯修正。证毕。

原半周期 sigma 恒等式是
$$
\sigma(t+Q)
=\sigma(Q)e^{\zeta(Q)t}\sigma(t)\sqrt{x(t)},
\qquad
\sqrt{x(t)}=t^{-1}+O(t^3).
\tag{N5}
$$
它由 sigma 加法式、$x(Q)=0$、除子及 $t=0$ 首项确定；
平方根采用这个原形式分支。代入 (N2) 得到
$$
\boxed{\quad
\mathscr K_Q(t,u)
=\mathscr K(t,u)\sqrt{\frac{x(t+u)}{x(t)}}.
\quad}
\tag{N6}
$$
右侧平方根在 $u=0$ 的值为一。在二变量的齐次展开中，它的首项是
$t/(t+u)$，不能把它错当成常数一。

## 3. 同一个 $Y=t\sqrt{x}$ 的精确 Eisenstein 系数

取 (N4) 在 $t=0$ 的 regular constant，由
$\mathscr K(t,u)=t^{-1}+\zeta(u)+O(t)$
和 $\mathscr K_Q(0,u)=\sqrt{x(u)}$，得到
$$
\lambda\zeta(u)=\zeta(\bar\lambda u)+\sqrt{x(\bar\lambda u)}.
$$
先换 $u\mapsto u/\bar\lambda$，再用 $1/\bar\lambda=i/\lambda$ 和
$\zeta(iz)=-i\zeta(z)$，准确化为
$$
\boxed{\quad
\bar\lambda\zeta(u/\lambda)=\zeta(u)+\sqrt{x(u)}.
\quad}
\tag{N7}
$$
保持原 $G_d$ 规范
$$
\zeta(u)=u^{-1}-\sum_{h\ge1}G_{4h}u^{4h-1}.
$$
令
$$
Y(u)=u\sqrt{x(u)}
=1+\sum_{h\ge1}y_hu^{4h}.
$$
逐项比较 (N7)，得到
$$
y_h=\left(1-\frac{2}{(-4)^h}\right)G_{4h}.
\tag{N8}
$$
这里用的是 $\lambda^4=-4$，没有引入额外 CM 标量。

在特征 $p=4k+3$ 中，$i^p=-i$，从而
$\lambda^{p+1}=2$，
$$
(-4)^k=\lambda^{p-3}=-\frac12.
$$
目标层因此严格满足
$$
\boxed{\quad
y_k=[u^{p-3}]Y(u)
=5G_{p-3}=\frac{2a}{\delta^3}\in\mathbf F_p^\times.
\quad}
\tag{N9}
$$
最后一式只消费 R1082 已付的
$G_{p-3}=2a/(5\delta^3)$、$\delta\in\mathbf F_p^\times$。

(N8) 在本篇只读取 $h\le k$。
这些 $G_{4h}$ 的权都至多 $p-3$，处于原安全整范围。
$Y$ 的构造只用 $x$ 的同一低段、单位常数项的求逆和除以二。
不把无限 zeta series 直接约化。

## 4. 原目标反对角的完整卷积

沿用 R1116 的原对称多项式
$$
\mathscr K(t,u)=t^{-1}+u^{-1}+\sum_{h\ge1}P_h(t,u),
\qquad \deg P_h=4h-1,
$$
以及
$$
P_k(t,u)=\sum_{s=0}^{4k-1}c_s t^{4k-1-s}u^s.
$$
因为 $\mathscr K(t,-t)=0$，每个 $P_h(t,u)$ 都被 $t+u$ 整除。

定义完整有限卷积
$$
\frac{Y(t+u)}{Y(t)}
=\sum_{h\ge0}R_h(t,u),\qquad
R_0=1,\quad \deg R_h=4h.
\tag{N10}
$$
等价地，若 $Y(t)^{-1}=\sum_{b\ge0}z_bt^{4b}$，
$y_0=z_0=1$，则
$$
R_h(t,u)=\sum_{a+b=h}y_a z_b(t+u)^{4a}t^{4b}.
$$
这是明确的有限卷积；$h>0$ 时 $R_h(t,0)=0$，故 $u\mid R_h$。

由 (N6)，
$$
\mathscr K_Q(t,u)
=\mathscr K(t,u)\frac{t}{t+u}\frac{Y(t+u)}{Y(t)}
=u^{-1}+\sum_{h\ge1}D_h(t,u),
$$
其中 $D_h$ 是齐次多项式、$\deg D_h=4h-1$。
目标层的完整式为
$$
\boxed{\quad
D_k(t,u)=\frac{R_k(t,u)}u
+\frac{t}{t+u}
\left(P_k(t,u)+
      \sum_{h=1}^{k-1}P_{k-h}(t,u)R_h(t,u)\right).
\quad}
\tag{N11}
$$
(N11) 中每一个商都是真正多项式：
第一项用 $u\mid R_k$，其余项用 $t+u\mid P_{k-h}$。
特别保留全部 $1\le h\le k-1$ 的较低层乘积。

把 (N4) 写成
$\lambda\mathscr K(\lambda t,u/\bar\lambda)
=\mathscr K(t,u)+\mathscr K_Q(t,u)$。
齐次目标层的一个系数在左边乘以
$\lambda^{4k}/2^s$。由 $\lambda^{4k}=-1/2$，
$$
\boxed{\quad
[t^{4k-1-s}u^s]D_k
=-\bigl(1+2^{-s-1}\bigr)c_s,
\qquad 0\le s\le4k-1.
\quad}
\tag{N12}
$$
因此 (N11) 与 (N12) 是同一原反对角的完整二同源约束。
例如 $s=4k-1$ 时，
$D_k(0,u)=y_ku^{4k-1}$、
$c_{4k-1}=-G_{p-3}$，两式同时给出 $y_k=5G_{p-3}$。
这个端点核对没有把它替换成内段系数。

所有 $P_h$、$R_h$、$D_h$ 在本篇都只用 $h\le k$。
sigma 只需至 $p-2$ 次，$x$ 只需至 $p-5$ 次。
原 additive 参数与 R1071/R1079 eigenparameter 的差为
$O(T^{p^2})$，不会回流到这些次数。
(N6) 付款的是平移核的整代数展开，而不是单独把 (N2) 的指数约模 $p$。

## 5. 同源乘积式及保留范围

原 R1114 的
$\lambda\zeta(\lambda t)=2\zeta(t)+y(t)/x(t)$
积分并固定首项，给出
$$
\sigma(\lambda t)=\lambda\sigma(t)^2\sqrt{x(t)}.
$$
将它用于 $t,u,t+u$，得到另一条完整原式
$$
\boxed{\quad
\mathscr K(t,u)\mathscr K_Q(t,u)
=\lambda\sqrt{x(u)}\,\mathscr K(\lambda t,\lambda u).
\quad}
\tag{N13}
$$
其首项为 $1/(tu)+1/u^2$，与两侧完全相同。

为了明确不删低层，(N13) 的总次数 $4k-2$ 是
$$
\begin{aligned}
(t^{-1}+u^{-1})D_k+u^{-1}P_k
+\sum_{h=1}^{k-1}P_hD_{k-h}
={}&\lambda^{4k}\frac{P_k}{u}
+y_ku^{4k-1}(t^{-1}+u^{-1})\\
&+\sum_{h=1}^{k-1}
  \lambda^{4(k-h)}y_hu^{4h-1}P_{k-h}.
\end{aligned}
\tag{N14}
$$
这是 Laurent 多项式恒等式；所有项都在同一原参数中。
(N14) 的求和不能省略，也不从 (N9) 自动推出某个
$[t^{4k-2j}u^{2j-1}]P_k$ 为单位。

后续真正要排除的仍是 R1116 的
$$
c_{2j-1}=0
\quad\text{对所有 }1\le j\le k-1
\text{ 且 }p\nmid B_{p-1-2j}.
$$
若某些角色不 good，本笔记没有给它们的全局 Selmer 局部像控制，
因此不删除该 mask。即使全部 forced 行都 good，
(N11)–(N14) 也仍含完整低层卷积；
本篇没有把二挠平移说成仅对 $P_k$ 的无余项对角作用。
原 bare $r=2,8$、$f_N/e$、短 $\eta/\nu$ 没有因这些恒等式而关闭。

来源：R1114 的同一 Gaussian 二挠及 $(1+i)$ 标度；
R1116 的原 Kronecker 核、有限整范围和 forced/good-mask 尺度。
(N4)–(N12) 已由 o1_theta 独立逐式纸核；
本篇无数学程序执行。
