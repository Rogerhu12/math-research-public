# R271 附录：原 Haar 迹类交织的每个非零像都是完整边界 T 的循环向量

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本稿关闭[原 Haar 全目标交织稿](R271-appendix-actual-haar-global-trace-intertwiners-and-cyclic-quotient-quasiaffinities.md) §5 留下的本族实际交点问题。对那一篇固定的同一条全空间稀疏链，以及每个原 Haar 来源 $y$，证明 $\mathscr K_y$ 的每个非零像都对原完整 $T_N$ 或 $T_Y$ 循环。因而它与任何真闭 $T$ 不变子空间的交点都恰为零；此前的固定可闭右逆链空间 $U$ 也包括在内。

## 1. 固定原对象和已付输入

来源是原 Haar 空间 $\mathcal H=L^2(\mathbb Z_2,\mu)$ 上的
$$
Af(t)=w(t)f(t-1),
\qquad w(0)=0,\qquad w(t)=\alpha_{v_2(t)}\ (t\ne0).
$$
目标是 $H=\ell^2(\mathbb N_0)$ 上的原完整边界 $T=T_N$ 或 $T_Y$。
目标和来源不混同。记
$$
\beta_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)},\qquad \beta_0=1.
$$
前稿已经证明实际共同范数及四次衰减
$$
\|A^n\|=\beta_n=\|B^n\|,
\qquad \beta_n\le e^{-(95/32)n^4}\quad(n\ge2).
\tag{1.1}
$$
原 $A$ 与 $A^*$ 单射，且拟幂零。

以下只需原高位弱单位的 dyadic 情形：
$$
\frac{A^{2^j}}{\beta_{2^j}}\longrightarrow\frac12 I
\quad\mathrm{WOT},
\qquad
\frac{(A^*)^{2^j}}{\beta_{2^j}}\longrightarrow\frac12 I
\quad\mathrm{WOT}.
\tag{1.2}
$$
这是 R140 的原 Haar 结论；[R189 §5.2](R189-empty-phase-inverse-mixed-type-and-universal-fast-fraction-field.md) 的 (5.3) 保留了全部固定整数倍版本。本稿只用 (1.2)，没有把它搬到负整数边界 $B$。

固定[稀疏真核注入稿](R271-appendix-sparse-kernel-injection-dense-backward-chain-and-global-trace-quasiaffinity.md) 所构造的同一链：
$$
u_0=e_0,\quad Tu_n=u_{n-1}\ (n\ge1),\quad
P_0u_n=\mathbf1_{\{n=0\}}e_0,\quad
\overline{\operatorname{span}}\{u_n:n\ge0\}=H,
$$
$$
\|u_n\|_\kappa\le e^{C_\kappa(n+1)^3},\qquad u_n\in\mathcal E_\infty.
\tag{1.3}
$$
对 $y\in\mathcal H$，使用前稿同一个实际迹类算子
$$
\mathscr K_yx=\sum_{n\ge0}\langle A^nx,y\rangle u_n,
\qquad
T\mathscr K_y=\mathscr K_yA,\qquad
\mathscr K_y^*e_0=y.
\tag{1.4}
$$
内积对第一变量线性。该级数按迹范数绝对收敛，且
$\mathscr K_y:\mathcal H\to X_\kappa$ 对每个 $\kappa\ge0$ 有界。
其准确核为
$$
\ker\mathscr K_y=\mathcal C_y^\perp,\qquad
\mathcal C_y=[y]_{A^*}
:=\overline{\operatorname{span}}\{(A^*)^ny:n\ge0\}.
\tag{1.5}
$$

## 2. 原弱单位在每个循环空间中的实际作用

对任意闭 $A^*$ 不变子空间 $\mathcal C$ 以及整数 $k\ge0$，
$$
\boxed{\overline{(A^*)^k\mathcal C}=\mathcal C.}
\tag{2.1}
$$
当 $k=0$ 时无须证明。对 $k\ge1$、$z\in\mathcal C$ 及 $2^j\ge k$，
$$
\frac{(A^*)^{2^j}z}{\beta_{2^j}}
=(A^*)^k\left(
\frac{(A^*)^{2^j-k}z}{\beta_{2^j}}\right)
\in(A^*)^k\mathcal C.
$$
这些向量由 (1.2) 弱收敛到 $z/2$。线性子空间的弱闭包与范数闭包相同，
所以 $z\in\overline{(A^*)^k\mathcal C}$。反向包含由不变性给出。

这里没有声称 $(A^*)^k|_{\mathcal C}$ 满射、下有界，或这些实际原像有任何一致范数费用。

## 3. 同一符号保留每个原 Haar 循环空间

固定 $v\in H\setminus\{0\}$。由 (1.1)、(1.3)，
$$
\Phi_v(A^*)=\sum_{n\ge0}\langle v,u_n\rangle(A^*)^n
\tag{3.1}
$$
按算子范数绝对收敛，并且
$$
\mathscr K_y^*v=\Phi_v(A^*)y.
\tag{3.2}
$$
链在完整 $H$ 稠密，故存在最小 $k$ 使 $c_k:=\langle v,u_k\rangle\ne0$。
写
$$
\Phi_v(A^*)=(A^*)^kV,\qquad
V=\sum_{n\ge0}c_{n+k}(A^*)^n.
\tag{3.3}
$$
移去固定 $k$ 后系数仍只有三次指数增长，故 $V$ 也按范数绝对收敛。

令 $\mathcal A_*=\overline{\mathbb C[A^*]}^{\|\cdot\|}$。
不仅 $V$ 可逆，而且
$$
\boxed{V,V^{-1}\in\mathcal A_*.}
\tag{3.4}
$$
为支付逆的范围，置 $Q=V-c_kI$。$Q$ 是零常项 $A^*$ 多项式 $Q_N$ 的范数极限；
每个 $Q_N$ 拟幂零，并与 $Q-Q_N$ 交换，故交换算子的谱半径次可加性给
$$
r(Q)\le r(Q_N)+r(Q-Q_N)\le\|Q-Q_N\|\longrightarrow0.
$$
因此 $r(Q)=0$，从而
$$
V^{-1}=\frac1{c_k}\sum_{m\ge0}(-Q/c_k)^m
$$
按范数收敛，并属于同一个闭代数 $\mathcal A_*$。
这是真实有界逆，不是形式级数代除法。

对任意 $y\in\mathcal H$，(3.4) 给
$$
[Vy]_{A^*}=[y]_{A^*}=\mathcal C_y.
$$
再用 (2.1) 及 $V$ 与 $A^*$ 交换，得到准确同源等式
$$
\begin{aligned}
[\mathscr K_y^*v]_{A^*}
&=[(A^*)^kVy]_{A^*}\\
&=\overline{(A^*)^k[Vy]_{A^*}}
=\mathcal C_y.
\end{aligned}
$$
所以
$$
\boxed{[\mathscr K_y^*v]_{A^*}=\mathcal C_y
\qquad(v\ne0).}
\tag{3.5}
$$
证明只用了原 $A^*$ 的多项式闭代数和原弱单位，没有假设未知不变子空间被其全交换子代数保持。

## 4. 非零实际像必对完整 T 循环

**定理。** 对任意 $x,y\in\mathcal H$，
$$
\boxed{
\mathscr K_yx\ne0
\quad\Longrightarrow\quad
[\mathscr K_yx]_T=H.
}
\tag{4.1}
$$

证明：若 $f=\mathscr K_yx\ne0$ 而 $[f]_T\ne H$，取
$0\ne v\perp[f]_T$。由 (1.4)，对所有 $n\ge0$
$$
0=\langle T^nf,v\rangle
=\langle A^nx,\mathscr K_y^*v\rangle
=\langle x,(A^*)^n\mathscr K_y^*v\rangle.
$$
故 $x\perp[\mathscr K_y^*v]_{A^*}$。由 (3.5)，这就是
$x\perp\mathcal C_y$；再由 (1.5)，得到 $\mathscr K_yx=0$，矛盾。

特别，当 $y\ne0$ 时，$\operatorname{Ran}\mathscr K_y$ 是一个稠密线性算子值域，
它的每个非零向量都对 $T$ 循环。这不要求 $\mathcal C_y=\mathcal H$，
即不要求原 Haar $A^*$ 有一个已付的普通循环向量。

取归一化 Haar 常函数 $\mathbf1$，可给出同一个实际非零向量
$$
f_*=\mathscr K_{\mathbf1}\mathbf1\in\mathcal E_\infty,\qquad
P_0f_*=e_0,\qquad [f_*]_T=H.
\tag{4.2}
$$
这里 $P_0f_*=e_0$ 来自 (1.4)，故非零性无需额外假设。

## 5. 本族全部真不变目标的拉回精确为原核

若 $L\subsetneq H$ 是闭 $T$ 不变子空间，则 (4.1) 立即给
$$
\boxed{
\operatorname{Ran}\mathscr K_y\cap L=\{0\},
\qquad
\mathscr K_y^{-1}(L)=\ker\mathscr K_y=\mathcal C_y^\perp.
}
\tag{5.1}
$$
这同时适用于此前的 proper 固定可闭右逆链空间 $U$、$M=\ker T$，
以及 $N=\overline{BM}\subset M$。它把前稿 §5 留下的这些交点问题，
对这一个固定全空间链产生的整个 $\mathscr K_y$ 家族，准确关闭为零。
不把结论扩展到尚未构造的其他交织或其他来源。

因此本族无法通过拉回一个真闭 $T$ 不变子空间，得到比自身原核
$\mathcal C_y^\perp$ 更大的 Haar 不变空间。这里没有判断
$\mathcal C_y^\perp$ 是否非零；没有证明原 Haar 普通循环性或非循环性。
新结论也没有支付真实 $W$ 的 Green 除法费用、证明 $N=M$，
或达到普通 Hilbert ISP 的完成标准。
