# R150 附录：非线性剪切后的中间次数带与全部点态幂

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已核查分支坐标微分、全部交叉 Bell、实际结果式次数和深域排核。
状态：已证明，完整证明。补齐上一剪切权界以外、原 Newton 上边仍有重根的一段次数带；不关闭首位切向碰撞。

## 1. 主结论与旧范围

令 $u,v$ 为任意复 $\ell^2$ first，$X_u$ 空谱，
$$
j_u\le j_v,\qquad \alpha=a_{j_u}\ne0,\qquad h=2^{j_u}.
\tag{1.1}
$$
取标量 $\Psi$，次数 $k\ge2$、最高系数 $c\ne0$。
给整数 $m,p$ 满足
$$
\boxed{m(k-1)<p<mk.}
\tag{1.2}
$$
令 $G(x,z)$ 关于 $z$ 首一、次数 $m$，
并假设每个非零单项式 $x^iz^j$ 都满足
$$
mi+pj\le mp.
\tag{1.3}
$$
记 $G_0$ 为权恰为 $mp$ 的部分，且
$$
H(Z)=G_0(1,Z)
$$
有 $m$ 个不同的复根 $\Omega$。

**定理 1。** 对全部 $\lambda\in\mathbb C$、
整数 $r\ge1$ 和复 $\ell^2$ 指数权 $w$，
$$
\boxed{
[G(u,v-\Psi(u))-\lambda]^r e^w
\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.4}
$$
任意非零常数最高系数可先除去。

特别，若 $\deg q=m$、$\deg g=p$ 且 (1.2) 成立，
取 $G=(q(z)-g(x))/q_m$，便有
$$
H(Z)=Z^m-g_p/q_m
$$
的全部简单根。因此
$$
\boxed{
[q(v-\Psi(u))-g(u)-\lambda]^r e^w
\text{ 对所有 }\lambda,r,w\text{ 循环}.}
\tag{1.5}
$$

此前[非线性剪切附录](R150-appendix-nonlinear-scalar-shears-degenerate-newton-edges-and-point-powers.md)的权界是
$i+(k-1)j\le m(k-1)$，
不允许此处的 $x^p$；
而原变量下的最高边仍为 $(y-cx^k)^m$，
不满足[非退化 Newton 上边附录](R150-appendix-nondegenerate-newton-edge-all-point-powers-and-one-empty-anchor.md)的简单根假设。
这里不重复登记两者的交集，也不把下述中间带推广到等号边。

## 2. 真实 Bell 多项式、gauge 商和字符

固定 $\lambda,r,w$；把 $\lambda$ 吸入 $G$ 常数。
令
$$
F(x,y)=G(x,y-\Psi(x)),\qquad
X=X_{u,b},\quad Y=X_{v,b},\quad \xi=e^w.
$$
R176 §10、R186 给实际闭域、共同正则化及全部混合词。
$X$ 仍空谱，故
$$
L=X^{-1}\in\mathfrak C=\{A\}'
$$
有界且拟幂零。

采用联合规范 Bell 系数 $B_{ij}$，即
$$
\mathcal B(s,t)=
\prod_j e^{-(sa_j+tc_j)R_j(b)}
\bigl[\cosh(sa_j+tc_j)I+R_j(b)\sinh(sa_j+tc_j)\bigr],
$$
$$
B_{ij}=\partial_s^i\partial_t^j\mathcal B(0,0).
$$
它们属于 $\mathcal A_h$，
$B_{00}=I$，正阶字符为零。
完整实际多项式为
$$
P_r(x,y)=
\sum_{i,j\ge0}\frac{B_{ij}}{i!j!}
\,\partial_x^i\partial_y^jF(x,y)^r,
\qquad n=\deg_yP_r=mr.
\tag{2.1}
$$
求和有限且保留全部交叉 Bell 项。
R186 的规范最大实现 $\mathsf P_r$ 为自然混合图闭包、
在原 $H$ 上 $C$ 自伴，且
$$
\mathsf P_r\xi=G(u,v-\Psi(u))^r e^w
$$
具有 $\xi$ 的真实循环图核心。

对 dyadic $\zeta$，实际同域增量
$D_X,D_Y\in A^h\mathcal A_h$，
以及 R124/R139 的真实余数除法给
$$
P_{r,\zeta}=(\gamma_\zeta P_r)(x+D_X,y+D_Y),\qquad
P_{r,\zeta}-P_r=A^hQ_{r,\zeta},
\tag{2.2}
$$
其中 $Q_{r,\zeta}\in\mathcal A_h[x,y]$，$\deg_yQ\le n-1$。
这里先得到实际有界商，再取字符。

若 $\gamma=c_{j_u}$、
$\kappa_\zeta=e^{-2b_{j_u}}(\zeta^h-1)/W_h$，
完整联合局部生成式
$e^{-2(\alpha s+\gamma t)}-1$
给
$$
\chi(P_r)=F^r,\qquad
\chi(Q_{r,\zeta})
=\kappa_\zeta
\bigl[F(x-2\alpha,y-2\gamma)^r-F(x,y)^r\bigr].
\tag{2.3}
$$
所有混合字符均包括在内，$h=1$ 使用 R124 的同一实际除法。

## 3. 剪切缩放和全部混合导数的形式域

置
$$
\delta=p-m(k-1).
\tag{3.1}
$$
由 (1.2)，
$$
0<\delta<m,\qquad \delta<p.
$$
以下 $t$ 是中心形式变量，不在实际算子上取分数幂。

令 $N=pn=pmr$，并定义
$$
\mathcal T_NJ
=t^N J\left(t^{-m},\Psi(t^{-m})+t^{-p}Z\right).
\tag{3.2}
$$
准确链式法则给
$$
\mathcal T_N(\partial_xJ)
=\mathscr D_N(\mathcal T_NJ),
$$
$$
\boxed{
\mathscr D_N=
\frac Nm t^m-\frac1m t^{m+1}\partial_t
-\left[\frac pm t^m Z+\psi(t)\right]\partial_Z,
\qquad
\psi(t)=t^p\Psi'(t^{-m})
=kc\,t^\delta+O(t^{\delta+m}).
}
\tag{3.3}
$$
并且
$$
\mathcal T_N(\partial_yJ)=t^p\partial_Z(\mathcal T_NJ).
\tag{3.4}
$$
$\psi$ 是真正的标量多项式，因为 $\delta>0$。
这些算子保持 $\mathcal A_h[t,Z]$，
且正阶求导项在 $t=0$ 均为零。

写
$$
G_t(X_0,Z_0)=
t^{mp}G(t^{-m}X_0,t^{-p}Z_0)\in\mathbb C[t,X_0,Z_0].
\tag{3.5}
$$
则
$$
\mathcal T_N(F^r)=G_t(1,Z)^r.
$$
所以
$$
\widetilde P=\mathcal T_NP_r\in\mathcal A_h[t,Z],
\qquad
\widetilde P(0,Z)=H(Z)^r.
\tag{3.6}
$$

对平移后的 $F_D(x,y)=F(x+D_X,y+D_Y)$，有
$$
x+D_X=t^{-m}(1+t^mD_X),
$$
$$
y+D_Y-\Psi(x+D_X)=t^{-p}[Z+J_D(t)],
$$
$$
J_D(t)=t^pD_Y-t^p[\Psi(t^{-m}+D_X)-\Psi(t^{-m})]
\in t^\delta\mathcal A_h[t].
\tag{3.7}
$$
(1.3) 使
$\mathcal T_N(F_D^r)=G_t(1+t^mD_X,Z+J_D(t))^r$
没有负次幂。
再用 (3.3)–(3.4)，
$\widetilde P_\zeta=\mathcal T_NP_{r,\zeta}$ 同属 $\mathcal A_h[t,Z]$。
从 (2.2) 逐个负次系数消去单射 $A^h$，得到
$$
\widetilde Q=\mathcal T_NQ_{r,\zeta}\in\mathcal A_h[t,Z].
\tag{3.8}
$$

### 3.1 分支内的完整导数估计

对每个简单根 $\omega\in\Omega$，逐阶标量隐函数递归给
$$
z_\omega(t)\in\mathbb C[[t]],\qquad
z_\omega(0)=\omega,\qquad G_t(1,z_\omega(t))=0.
\tag{3.9}
$$
代入
$$
Z=z_\omega(t)+t^\delta W.
$$
则 $G_t(1,Z)^r$ 被 $t^{\delta r}$ 整除。
对 (3.7) 也如此：$X_0$ 的扰动阶为 $m>\delta$，
$Z_0$ 的扰动阶至少 $\delta$。

这里必须验证全部重复导数保持该阶数，不能只看第一次。
将 (3.3) 准确搬到 $(t,W)$ 坐标，得到
$$
\begin{aligned}
\mathscr D_{N,\omega}
={}&\frac Nm t^m-\frac1m t^{m+1}\partial_t\\
&+\left[
\frac1m t^{m+1-\delta}z_\omega'(t)
-\frac pm t^{m-\delta}z_\omega(t)
+\frac{\delta-p}{m}t^mW
-\frac{\psi(t)}{t^\delta}
\right]\partial_W.
\end{aligned}
\tag{3.10}
$$
所有括号系数都在 $\mathbb C[W][[t]]$ 中；
$\partial_t$ 前有 $t^{m+1}$，
所以它保持每个理想 $t^q\mathcal A_h[W][[t]]$，$q\ge0$。
$y$ 导数变为
$$
t^{p-\delta}\partial_W,
\tag{3.11}
$$
同样保持这些理想。

因此任意有限次、任意次序的全部 $(i,j)$ 导数
都保持 $t^{\delta r}$ 阶数，
无论它乘的是原 $B_{ij}$ 还是 $\gamma_\zeta B_{ij}$。
这证明
$$
\widetilde P(t,z_\omega(t)+t^\delta W),\
\widetilde P_\zeta(t,z_\omega(t)+t^\delta W)
\in t^{\delta r}\mathcal A_h[W][[t]].
$$
再由 (2.2) 逐个系数消去单射 $A^h$，
$$
\boxed{
\widetilde Q(t,z_\omega(t)+t^\delta W)
\in t^{\delta r}\mathcal A_h[W][[t]].
}
\tag{3.12}
$$
这是完整交叉 Bell 的估计，不是单行近似。

## 4. 结果式的实际次数与最高单位

定义
$$
E_\zeta(x)=\operatorname{Res}_y(P_r,Q_{r,\zeta}).
$$
$P_r$ 首一使它是有限自由模行列式，并给
$$
E_\zeta=A_\zeta P_r+B_\zeta Q_{r,\zeta}
\tag{4.1}
$$
的实际有限系数 Bézout 恒等式。

由 (3.6) 的两两互素标量因子，
逐阶 Hermite 余数分解给
$$
\widetilde P(t,Z)=\prod_{\omega\in\Omega}P_\omega(t,Z),
$$
其中每个 $P_\omega$ 首一、次数 $r$，
$P_\omega(0,Z)=(Z-\omega)^r$。
递归每一步只逆一个标量有限矩阵，
系数始终在 $\mathcal A_h[[t]]$，不求实际算子根。

(3.12) 及其他分支在该簇的单位常数给
$$
\widehat P_\omega
=t^{-\delta r}P_\omega(t,z_\omega(t)+t^\delta W),
\quad
\widehat Q_\omega
=t^{-\delta r}\widetilde Q(t,z_\omega(t)+t^\delta W)
$$
都是 $\mathcal A_h[[t]][W]$ 中的多项式，
$\widehat P_\omega$ 首一、次数 $r$。
秩 $r$ 的自由模范数给
$$
\operatorname{Res}_Z(P_\omega,\widetilde Q)
=t^{\delta r^2}
\operatorname{Res}_W(\widehat P_\omega,\widehat Q_\omega).
$$
相乘得到
$$
\operatorname{Res}_Z(\widetilde P,\widetilde Q)
\in t^{\delta mr^2}\mathcal A_h[[t]].
\tag{4.2}
$$
另一方面，(3.2) 的平移、缩放和首一性准确给
$$
\operatorname{Res}_Z(\widetilde P,\widetilde Q)
=t^{pn^2}E_\zeta(t^{-m}).
\tag{4.3}
$$
所以实际次数满足
$$
\boxed{
\deg_xE_\zeta\le
D=r^2(pm-\delta)
=r^2[p(m-1)+m(k-1)].
}
\tag{4.4}
$$
高于 $D$ 的实际算子系数严格为零，不只是字符为零。

### 4.1 顶系数非零字符

由 (2.3)，
$$
\chi(E_\zeta)
=\kappa_\zeta^{mr}
\operatorname{Res}_y(F,F(x-2\alpha,y-2\gamma))^{r^2}.
\tag{4.5}
$$
对标量首一 $F$，在 (3.9) 的每个根代入后，
$x$ 平移使剪切后的 $Z$ 变量增加
$$
2kc\alpha\,t^\delta+O(t^{\delta+1}),
$$
$x$ 自身的标度变化阶为 $m>\delta$，
$y$ 平移阶为 $p>\delta$。
所以归一化后的移位 $F$ 在该根的首项为
$$
2kc\alpha\,H'(\omega)t^\delta.
\tag{4.6}
$$
各 $H'(\omega)\ne0$，故标量结果式恰有次数 $pm-\delta$，
最高系数为
$$
\prod_{\omega\in\Omega}2kc\alpha H'(\omega)\ne0.
$$
结合 (4.4)，若 $E_\zeta=e_Dx^D+\cdots+e_0$，
$$
\boxed{
\chi(e_D)=
\kappa_\zeta^{mr}
\left[\prod_{\omega\in\Omega}2kc\alpha H'(\omega)\right]^{r^2}
\ne0\qquad(\zeta^h\ne1).
}
\tag{4.7}
$$
因此 $e_D$ 是 $\mathcal A_h$ 的实际单位。

## 5. 全部实际混合域上的排核

令 $M=\ker\mathsf P_r$。
从 (4.1)、(2.2) 得
$$
A^hE_\zeta
=(A^hA_\zeta-B_\zeta)P_r+B_\zeta P_{r,\zeta}.
\tag{5.1}
$$
定义
$$
\rho_\zeta=e_D+\sum_{j<D}e_jL^{D-j}
=e_D(I+LK_\zeta).
$$
$L$ 拟幂零并与 $K_\zeta\in\mathfrak C$ 交换，
(4.7) 因而给
$$
\rho_\zeta,\rho_\zeta^{-1}\in\mathfrak C,\qquad
\rho_\zeta M=M
\tag{5.2}
$$
（R88）。未使用一般慢系数的未知限制稠密性。

取 R186 共同正则器 $R$，有限 $N_*$ 覆盖 (5.1)
全部次数、中间自然词和 $X^D$。
对 $f\in R^{N_*}M$、$g\in U_\zeta R^{N_*}M$，
全部混合自然域合法，
$P_rf=0$、$P_{r,\zeta}g=0$，$L^D$ 保持这些域。
原 $H$ 上完整 $C$ 自伴给
$$
B(A^h\rho_\zeta f,g)
=B(P_{r,\zeta}L^DB_\zeta f,g)
=B(L^DB_\zeta f,P_{r,\zeta}g)=0.
$$
由测试空间稠密、(5.2) 和 $A^h$ 的普遍限制稠密像，
$$
B(M,U_\zeta M)=0\quad(\zeta^h\ne1).
$$
有限 Fourier 支撑、严格正权下的总支撑全测和逐柱一维性
给 $\dim M\le h$；
单射拟幂零 $A$ 排除非零有限维不变空间，故 $M=0$。
完整 $C$ 自伴及真实循环图核心完成 (1.4)。

## 6. 新增实例与准确边界

取
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
\qquad \frac12<\sigma\le1.
$$
取 $k=m=2,p=3$，$\Psi(x)=x^2$，$G(x,z)=z^2-x^3$。
有 $\delta=1$、$D=5r^2$，
故
$$
\boxed{
[(v-u^2)^2-u^3-\lambda]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环}.}
$$
原顶边仍为 $(y-x^2)^2$；
其剪切余项 $x^3$ 超过上一稿的 $d=2$ 权界，
所以这是真正新增的重根上边范围。

更一般的 $G$ 也可有所有满足 (1.3) 的混合项，
只须 $H$ 的根简单。
$\Psi$ 的所有低阶项以及指数权的任意复系数不受限制。

本稿不覆盖 $p=m(k-1)$ 的剪切碰撞，
尤其不关闭 $(v-u^2)^2-4u^2-\lambda$。
$p=mk$ 时两个标度同阶，可能出现另一种切向抵消，
不由本稿直接推出。
没有空谱锚、一般重根 $H$、未知限制的慢因子稠密性仍保留。

完整 Hilbert 不变子空间问题未完成。
