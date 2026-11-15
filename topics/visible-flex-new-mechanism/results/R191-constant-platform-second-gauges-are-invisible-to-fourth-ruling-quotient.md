# R191：共同常值平台上的二阶 gauge 对完整第四 ruling 商恒不可见

日期：2026-11-15。完整纸面证明；没有新 profile、几何或研究算子计算。

使用 [R56 的真实变系数右锚恢复式](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R47 的三矩作用](R47-fourth-order-range-and-third-gauge.md)、[R180 的 hook 周期公式](R180-fixed-circle-invisible-third-hook-and-signed-fourth-period-gauge.md)及 [R184 的完整 joint 判据](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)。

R183 圆有 $f,g$ 同时常值的开平台。任意紧支撑在这些平台内的二阶齐次 profile 都自动满足六个交叉矩约束，并属于 hook 的第四 period 核。这个空间无限维，但它并不提供新的第四 ruling 商方向：本文证明其整个线性 ruling 响应准确落在同一个三矩空间 $\mathcal W$；对零初值 canonical 恢复，该响应本身就是零。

证明保留了平台右方全部 profile 所产生的真实右尾，以及从全局 s 起点累计的全部历史。平台上的 profile 值可以非零。

## 1. 固定数据与结论

固定 R184 的同一光滑几何、目标度量、第一圆及右 collar，保持 M=0 及已经支付的二、三阶完整 range 前提。记

$$
z=\xi+\omega(s),\quad u=h/z,\quad
e=h z-k=h\xi+d,\quad d=h\omega-k,
$$

$$
\gamma=h_s,\qquad \nu=\omega_s=\frac{k_s}{2h}.
$$

几何可处处变系数；本文不假设任何常状态段。固定开区间 $J\Subset I$，满足

$$
f|_J=f_*,\qquad g|_J=g_*.
\tag{1}
$$

常数 $(f_*,g_*)$ 无须为零。令

$$
\phi_\theta=\cos\theta\,f+\sin\theta\,g,\qquad
D_\theta=f^2-\phi_\theta^2,
$$

$$
\delta_\theta=f_*^2-(\cos\theta\,f_*+\sin\theta\,g_*)^2.
$$

平方与双线性记号沿用 R184。对任意 $w\in C_c^\infty(J)$，定义完整线性 ruling 改变量

$$
\mathcal B_\theta(w)
=
2\int (Z_B(D_\theta))_u\cdot(Y_w)_u\,du
-
4\int(Y_{\phi_\theta})_u\cdot
(Z_B(\phi_\theta,w))_u\,du.
\tag{2}
$$

所有 $Z_B$ 使用同一真实右锚及同一个全局 s 起点。

**定理。** 对零入历史 canonical 恢复，

$$
\boxed{\mathcal B_\theta(w)(s)=0
\quad\text{对全部 }s,\theta,\ w\in C_c^\infty(J).}
\tag{3}
$$

若改变共同入齐次值，或使用其他同 collar 的合法恢复，则仍有

$$
\boxed{[\mathcal B_\theta(w)]=0
\quad\text{于 }C^\infty(S_s^1)/\mathcal W,}
\tag{4}
$$

其中

$$
\mathcal W=
\left\{s\mapsto
\left(\frac{d^2+1}{4h},\frac d2,\frac h4\right)\cdot v:
v\in\mathbb R^3\right\}.
$$

特别地，平台无限维空间在 R184 的 joint 仿射线性映射中不产生新的 ruling 商方向。对于 R183 的 hook 几何，它同时不改变完整第四 period。

## 2. 一条保留全部端项的 ruling 配对式

写两个场为

$$
Z=F(s)V/z,\qquad \widehat Z=F(s)\widehat V/z.
$$

只要其中一个场紧支撑在活动区间内，或者二者都在两 collar 为零，物理 $u$ 积分方向与 $u_\xi=-h/z^2$ 给

$$
\begin{split}
\int Z_u\cdot\widehat Z_u\,du
&=\frac1h\int_I
\left(V_\xi\cdot\widehat V_\xi
-\partial_\xi\frac{V\cdot\widehat V}{z}\right)d\xi\\
&=\boxed{\frac1h\int_I V_\xi\cdot\widehat V_\xi\,d\xi}.
\end{split}
\tag{5}
$$

最后一步使用实际边界值，不把原函数尾擅自设零。特别地，在第一个场可能带有真实右尾时，只要另一个场由紧支撑的 w 给出，(5) 仍成立。

第一阶分子为

$$
V_a=\left(-\frac{a'}2,\,0,\,ha-\frac e2a'\right),
\tag{6}
$$

因此在 a 常值的区间，

$$
V_a=(0,0,ha_*),\qquad (V_a)_\xi=0.
\tag{7}
$$

物理场本身是 $Y_a=a_*uB$，通常不为零，物理导数 $(Y_a)_u=a_*B$ 也通常不为零。不能用 profile 正阶 jets 为零来删除这些物理值。

## 3. 原二阶场在平台上为何恰为物理仿射场

对 $H=(dY_f)^2-(dY_{\phi_\theta})^2$，采用 R56 的分子配对 $J_H,T_\xi,T_s,T_{s\xi}$。由 (1)、(6) 及 $B_s=N$，在整个 J 上有

$$
J_H=h^2\delta_\theta,\qquad T_\xi=0,\qquad
T_s=(h^2+\gamma^2)\delta_\theta,\qquad
T_{s\xi}=0.
\tag{8}
$$

R56 的真实右锚量为

$$
P_D(s,\xi)=-\frac1{2h}\int_r^\xi T_\xi(s,\eta)\,d\eta,
\qquad b_D=\frac{J_H}{2h}.
$$

在平台 J 上，$P_D$ 对 $\xi$ 为常数，记为 $p_D(s)$；它通常不为零，因为平台右方可以有其他活动段。准确地，

$$
P_D|_J=p_D(s),\qquad
b_D|_J=\frac h2\delta_\theta.
\tag{9}
$$

这里没有重设平台的右锚。

令

$$
K_0=kz^2-\frac{k^2+1}{h}z,\qquad
\lambda_c=\frac{\gamma z-h\nu}{h^2}.
$$

将 (8)、(9) 代入 R56 完整式，得到

$$
\boxed{
\mathcal R_D|_J
=\frac{\delta_\theta}2 k e
+K_0p_D-\lambda_c(p_D)_s,
\qquad
\eta_D|_J=-\frac12(p_D)_s.
}
\tag{10}
$$

例如 $T_s/(2h^2)$ 与 $-\gamma(b_D)_s/h^2$ 的 $\gamma^2$ 项准确相消；余下局部项是
$\delta_\theta(hkz-k^2)/2=\delta_\theta ke/2$。$\nu,\gamma,p_D,(p_D)_s$ 都保留。

(10) 是 $\xi$ 的二次以下多项式。它对整个几何的每个 s 都成立，而非只在一个几何段成立。因此从同一个全局零初值积分真实 characteristic 方程，可写

$$
W_D(s,\xi)=a_2(s)\xi^2+a_1(s)\xi+a_0(s)
\quad(\xi\in J).
\tag{11}
$$

系数是原右尾和全 s 历史的真实积分；本文没有把任何 $a_j$ 设零或逐段重锚。

R56 恢复给

$$
A_D=\frac12(W_D)_\xi+\frac{\eta_D}{h}
=a_2\xi+\frac{a_1}2-\frac{(p_D)_s}{2h},
$$

$$
V_D=(A_D,\ z p_D+h\delta_\theta/2,\ eA_D-hW_D).
$$

虽然 $W_D$ 是二次式，最后一个分量的二次最高项准确相消。于是

$$
\boxed{
(V_D)_\xi=
\left(a_2,\ p_D,\
d a_2-\frac h2a_1-\frac12(p_D)_s\right)
\quad(\xi\in J),
}
\tag{12}
$$

完全不依赖 $\xi$。等价地，$V_D$ 在 J 上仿射于 $\xi$，所以物理场 $Z_B(D_\theta)=FV_D/z$ 在对应 ruling 子区间仿射于 u。

现在 $(V_w)_\xi$ 紧支撑于 J。由 (5)、(12)，

$$
\int(Z_B(D_\theta))_u\cdot(Y_w)_u\,du
=\frac1h (V_D)_\xi\cdot\int_J(V_w)_\xi\,d\xi=0.
\tag{13}
$$

这一结论包含了任意非零平台值、全部右侧 profile 尾及全部二阶 s 历史。

## 4. 交叉恢复为何真紧支撑在平台

令 $\phi=\phi_\theta$，考虑完整 forcing $H(Y_\phi,Y_w)$。在 w 的支撑上 $(V_\phi)_\xi=0$，在其余地方 $(V_w)_\xi=0$，因此

$$
T_\xi=(V_\phi)_\xi\cdot(V_w)_\xi\equiv0
\quad\text{于整个 }I.
\tag{14}
$$

这一次真实右锚积分确实全零：

$$
P_{\phi w}\equiv0.
$$

其他配对 $J_H,T_s,T_{s\xi}$ 则是紧支撑在 J 的真实函数，未假定它们为零。尤其 $J_H=V_\phi\cdot V_w$ 可以非零；这正保留了平台非零值的作用。

R56 给

$$
\mathcal R_{\phi w}
=\frac{T_s}{2h^2}
+\left(kz-\frac{k^2+1}{h}\right)b_{\phi w}
-\frac\gamma{h^2}(b_{\phi w})_s,
$$

$$
\eta_{\phi w}
=-\frac{T_{s\xi}}{2h}+\frac{\gamma}{2h}(b_{\phi w})_\xi.
\tag{15}
$$

这些量全都紧支撑在同一个 J。沿全局 s 起点积分零初值后，$W_{\phi w}$ 也真紧支撑于 J；恢复分子和恢复场同样如此。不存在被遗漏的左常尾或跨包尾。

再次用 (5)、(7)，

$$
\boxed{
\int(Y_\phi)_u\cdot(Z_B(\phi,w))_u\,du
=\frac1h\int_I(V_\phi)_\xi\cdot
(V_{Z_B(\phi,w)})_\xi\,d\xi=0.
}
\tag{16}
$$

(13) 与 (16) 给定理的准确零式 (3)。

## 5. 非零共同入值只改变三矩分量

零初值不是在各段自由重选初值，而是一个固定全局 canonical 约定。改成另一合法恢复时，差是某个同 collar 的 $Y_\psi$；改变交叉恢复的合法共同初值也只加 $Y_\eta$。

R47 的原式为

$$
\int(Y_a)_u\cdot(Y_b)_u\,du
=\mathbf w(s)\cdot\mathbf m(a,b),
$$

$$
\mathbf w=\left(\frac{d^2+1}{4h},\frac d2,\frac h4\right).
$$

所以 (2) 可能增加的两类项

$$
2\int(Y_\psi)_u\cdot(Y_w)_u\,du,\qquad
-4\int(Y_\phi)_u\cdot(Y_\eta)_u\,du
$$

都属于同一个 $\mathcal W$。其矩向量与 s 无关。由此得到 (4)，不要求不同几何段分别选 gauge。

更一般地，若初始 $W_D$ 在 J 上不是二次式，它的非多项式部分恰对应这个固定齐次差；它不能产生新的 ruling 商分量。这解释了为何 (12) 的零初值推导足以给全部合法共同历史约定下的商结论。

## 6. R183 hook 几何下的完整 joint 含义

若 w 紧支撑在共同常值平台，自动有

$$
\mathbf m(f,w)=\mathbf m(g,w)=0,
\tag{17}
$$

因为矩密度只涉及 f、g 的正阶导数与 w 的正阶导数。R184 的第三 range 定义域因此完整满足；在 M=0 下，交叉恢复的完整周期也为零。

R183 的 $T=\kappa\mathfrak H$ 情形，R180--R181 给

$$
\mathcal L_\theta(w)=2\kappa L_f(w),\qquad
L_f(w)=\mathfrak H(w;f,f).
$$

其每个局部乘积或右 Volterra 被积式均含同处的 w 正阶 jet 与 f 正阶 jet，在这里准确为零。因此

$$
\boxed{\mathcal L_\theta(w)\equiv0,\qquad
[\mathcal B_\theta(w)]=0.}
\tag{18}
$$

可对每个相位任取共同紧支撑的光滑 $2\pi$ 周期家族 $w_\theta$，并要求 $w_0=w_\pi=0$ 保两个种子。任意有限幅度都服从 (18)，不是仅原点的一阶近似。

第四 forcing 仍有 $-H(Y_w,Y_w)$。它的 ruling 是
$-\mathbf w\cdot\mathbf m(w,w)$，并没有点态消失；但它全在 $\mathcal W$ 中。对零初值 (3)，如需保持原 ruling 本身，可按 R47 的单 profile 右逆选

$$
\mathbf m(\phi_\theta,\chi_\theta)
=-\frac12\mathbf m(w_\theta,w_\theta).
\tag{19}
$$

于是 R184 式 (11) 的新增 ruling 全零。$\phi_\theta$ 从不为零，所以右逆可以随相位光滑、周期选择并保种子；第三齐次改动在 M=0 下不改变第四 period。非零共同入值时把额外三矩项并入同一右逆即可。

如果已有另一个候选二阶 gauge $w^*_\theta$，向它添加任意这种平台 $w_\theta$ 也不改变 R184 的 joint 商方程。平方交叉项仍全部在 $\mathcal W$，可由第三齐次右逆处理。因此扩大到这一无限维平台空间不能挽救原本不满足 period 或 ruling 商条件的 $w^*_\theta$。

## 7. 准确范围

本文证明一个具体的不可见子空间，不是对任意二阶 gauge 的排除。它要求 f、g 在 w 的整个支撑邻域同时常值；不能将结论推广到共同仿射段或一般导数分包区间。

反过来，平台内物理交叉 forcing、交叉恢复以及 gauge 平方可以非零；本稿没有把它们删除。准确为零的是 (3) 的完整线性 ruling 配对，以及 hook 情形的完整周期改变量。第三 gauge 真实支付的有限维部分另由 (19) 保留。

这一结论对含常段或 R189 所构无常段几何都成立，因为证明从头保留了 $\gamma,\nu$ 和完整右锚历史。它没有计算原第四 $V^0,K^0$，没有证明 R184 的其他 joint 方向可解，也没有产生有限非零参数的精确等距族。
