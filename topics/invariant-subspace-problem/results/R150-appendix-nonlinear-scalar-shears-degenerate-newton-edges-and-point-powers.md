# R150 附录：非线性标量剪切、退化 Newton 上边与全部点态幂

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已核查固定归一指数的微分共轭、全部混合 Bell、真实次数/顶字符及自然域。
状态：已证明，完整证明。允许原 Newton 上边重根；全部交叉 Bell 项保留于真实有限多项式，不把非线性剪切后的符号当作 first。

## 1. 结论

取
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v=c_*+\sum_j c_j\chi_j,\qquad a,c\in\ell^2(\mathbb C),
$$
两者非常数。假设 $X_u$ 空谱，且
$$
j_u:=\min\{j:a_j\ne0\}\le
j_v:=\min\{j:c_j\ne0\}.
\tag{1.1}
$$
写
$$
h=2^{j_u},\qquad \alpha=a_{j_u}\ne0,\qquad \gamma=c_{j_u}.
$$

给一个标量多项式 $\Psi$，
$$
k=\deg\Psi\ge2,\qquad c=[x^k]\Psi\ne0,
\tag{1.2}
$$
以及标量多项式 $G(x,z)$，满足：

- 关于 $z$ 首一、次数 $m\ge1$；
- 每个非零单项式 $x^iz^j$ 满足
  $$
  i+(k-1)j\le d:=m(k-1).
  \tag{1.3}
  $$

定义边多项式
$$
H(Z)=\sum_{i+(k-1)j=d}[x^iz^j]G\;Z^j,
\tag{1.4}
$$
它关于 $Z$ 首一、次数 $m$。
允许 $H$ 有重根或零根。
唯一的标量互素条件是
$$
\boxed{\gcd_{\mathbb C[Z]}
\bigl(H(Z),H(Z+2kc\alpha)\bigr)=1.}
\tag{1.5}
$$

**定理 1。**
对每个 $\lambda\in\mathbb C$、每个整数 $r\ge1$、
每个复 $\ell^2$ 指数权
$$
w=b_*+\sum_j b_j\chi_j,
$$
都有
$$
\boxed{
[G(u,v-\Psi(u))-\lambda]^r e^w
\text{ 非零且对原 }A\text{ 循环}.
}
\tag{1.6}
$$
没有给 $v-\Psi(u)$ 假设一阶域或一阶 gauge 增量；
真实基本算子始终只有 $X_{u,b},X_{v,b}$。

### 1.1 一个无条件的直接子类

给任意非恒定标量 $q$，$\deg q=m$，
任意标量 $g$ 满足
$$
\deg g<m(k-1)
$$
（零多项式允许），以及任意标量 $\lambda$。
取 $G=q(z)-g(x)$ 并除以 $q$ 的非零最高系数，
则 $H(Z)=Z^m$。
因为 $2kc\alpha\ne0$，(1.5) 自动成立。
于是
$$
\boxed{
[q(v-\Psi(u))-g(u)-\lambda]^r e^w
\text{ 对所有 }r\ge1,w\text{ 循环}.
}
\tag{1.7}
$$
特别所有非零标量多项式 $q(v-\Psi(u))e^w$ 均循环；
$q$ 的不同根、重复根及任意复系数都允许。

这不从内层向量 $v-\Psi(u)$ 的平移幂循环性推出乘积循环性。
(1.7) 由外层 $q$ 自己的完整 Bell 多项式证明。

### 1.2 扣除旧范围

[普通双慢次数优势](R150-appendix-empty-first-anchor-newton-degree-and-ordinary-two-slow-cyclicity.md)及[非退化 Newton 上边附录](R150-appendix-nondegenerate-newton-edge-all-point-powers-and-one-empty-anchor.md)
已处理其所列的普通点态符号和全部幂。
这里原最高上边为
$$
(y-cx^k)^m,
$$
有重根；当 $m>1$ 时，不满足该非退化假设。
本稿通过准确的非线性标量代换给出另一条实际次数界，
不重复登记先前的简单上边结论。

R150 矩形角、R155 有界辅助及 R189 快系数双方向
也不直接覆盖一般独立非可和 $v$ 的普通剪切多项式。
已经属于这些旧定理的交集仍按原来源计。

## 2. 完整 Bell 实现及实际首位除法

固定 $\lambda,r,w$，将 $\lambda$ 吸收入 $G$ 的常数项，
不改变 $H$。令
$$
F(x,y)=G(x,y-\Psi(x)),
\quad X=X_{u,b},\quad Y=X_{v,b},\quad \xi=e^w.
$$
由 R176 §10 和 R186，$X,Y$ 是实际闭的倾斜 first，
具有全部混合自然词及共同正则化。
$X$ 保持空谱，故
$$
L=X^{-1}\in\mathfrak C=\{A\}'
$$
有界且拟幂零。

采用完整的联合规范 Bell 系数
$$
\mathcal B(s,t)
=\prod_j e^{-(sa_j+tc_j)R_j(b)}
 \bigl[\cosh(sa_j+tc_j)I+R_j(b)\sinh(sa_j+tc_j)\bigr],
$$
$$
B_{ij}=\partial_s^i\partial_t^j\mathcal B(0,0).
$$
它们满足
$$
B_{ij}\in\mathcal A_h=\overline{\mathbb C[I,A^h]},\qquad
B_{00}=I,\qquad
\chi(B_{ij})=0\quad(i+j>0).
\tag{2.1}
$$
所有混合项均保留：
$$
P_r(x,y)
=\sum_{i,j\ge0}\frac{B_{ij}}{i!j!}
 \partial_x^i\partial_y^j F(x,y)^r.
\tag{2.2}
$$
这是有限和，关于 $y$ 首一、次数
$$
n=mr.
\tag{2.3}
$$
其 R186 规范最大闭实现 $\mathsf P_r$
为真实混合图的闭包、在原 $H$ 上完整 $C$ 自伴，并满足
$$
\mathsf P_r\xi=G(u,v-\Psi(u))^r e^w.
\tag{2.4}
$$
$\xi$ 生成真实循环图核心。

固定 dyadic $\zeta$，记 $\Gamma=\gamma_\zeta$。
实际同域差为
$$
\Gamma X=X+D_X,\qquad \Gamma Y=Y+D_Y,\qquad
D_X,D_Y\in A^h\mathcal A_h.
\tag{2.5}
$$
R124 的真实余数分解与 R139 §1
（$h=1$ 直接用 R124）给
$\Gamma E-E\in A^h\mathcal A_h$ 对每个 $E\in\mathcal A_h$ 成立。
因此
$$
P_{r,\zeta}(x,y)
=(\Gamma P_r)(x+D_X,y+D_Y)
$$
满足实际有限多项式恒等式
$$
\boxed{P_{r,\zeta}-P_r=A^hQ_{r,\zeta},
\qquad Q_{r,\zeta}\in\mathcal A_h[x,y].}
\tag{2.6}
$$
$\deg_yQ_{r,\zeta}\le n-1$。

置
$$
\tau=e^{-2b_{j_u}},\quad d_h=d_{j_u}=W_h,\quad
\kappa_\zeta=\tau(\zeta^h-1)/d_h.
$$
联合局部 Bell 的 $A^h$ 系数为
$$
\frac{\tau}{d_h}
\left[e^{-2(\alpha s+\gamma t)}-1+2(\alpha s+\gamma t)\right].
$$
将实际 first 平移的线性项合并后，得到完整字符：
$$
\boxed{
\chi(P_r)=F^r,\qquad
\chi(Q_{r,\zeta})
=\kappa_\zeta
\bigl[F(x-2\alpha,y-2\gamma)^r-F(x,y)^r\bigr].
}
\tag{2.7}
$$
$e^{-2(\alpha s+\gamma t)}$ 保留全部交叉系数。
每个商已经由 (2.5)–(2.6) 确认为有界，
这里才取其字符。

## 3. 非线性标量剪切下的实际次数估计

以下 $t$ 只是形式参数，不作用于实际算子。
令
$$
N=dr=m(k-1)r=(k-1)n
$$
并对任意标量或交换系数多项式 $J(x,y)$ 定义
$$
\mathcal T_NJ
=t^N J\!\left(t^{-1},
\Psi(t^{-1})+t^{-(k-1)}Z\right).
\tag{3.1}
$$
它起初是有限 Laurent 多项式；
将证明用于这里的 Bell 多项式时没有负 $t$ 次幂。

### 3.1 全部微分项的准确共轭算子

置
$$
\psi(t)=t^{k-1}\Psi'(t^{-1})\in\mathbb C[t],
\qquad \psi(0)=kc.
$$
链式法则准确给
$$
\boxed{
\mathcal T_N(\partial_xJ)=
\mathscr D_N(\mathcal T_NJ),\qquad
\mathscr D_N=
Nt-t^2\partial_t-
\bigl[(k-1)tZ+\psi(t)\bigr]\partial_Z,
}
\tag{3.2}
$$
以及
$$
\boxed{
\mathcal T_N(\partial_yJ)
=t^{k-1}\partial_Z(\mathcal T_NJ).
}
\tag{3.3}
$$
例如在固定 $y$ 下，
$$
\frac{dt}{dx}=-t^2,\qquad
\frac{dZ}{dx}=-(k-1)tZ-t^{k-1}\Psi'(t^{-1}),
$$
便直接得到 (3.2)。

两个右侧算子均保持 $\mathcal A_h[t,Z]$。
因为 (1.3)，
$$
\mathcal T_N(F^r)
=
\left[t^dG(t^{-1},t^{-(k-1)}Z)\right]^r
\in\mathbb C[t,Z].
\tag{3.4}
$$
故反复使用 (3.2)–(3.3)，对 (2.2) 的每个 $(i,j)$ 项都有
$$
\mathcal T_N(\partial_x^i\partial_y^jF^r)
\in\mathbb C[t,Z].
\tag{3.5}
$$
于是
$$
\widetilde P(t,Z):=\mathcal T_N P_r
\in\mathcal A_h[t,Z].
\tag{3.6}
$$
这同时支付了全部交叉 Bell 系数；没有只保留各自的一行累积量。

### 3.2 共轭多项式也保持同一界

对 $P_{r,\zeta}$，
令 $F_D(x,y)=F(x+D_X,y+D_Y)$。
所有系数仍在同一个交换代数中。

在 (3.1) 的代换下，
$$
x+D_X=t^{-1}(1+tD_X),
$$
$$
y+D_Y-\Psi(x+D_X)
=t^{-(k-1)}\bigl[Z+J_D(t)\bigr],
$$
其中
$$
J_D(t)=t^{k-1}D_Y
-t^{k-1}\bigl[\Psi(t^{-1}+D_X)-\Psi(t^{-1})\bigr]
\in\mathcal A_h[t].
\tag{3.7}
$$
最后的多项式归属来自幂差最高次数只有 $k-1$。
将每个 $x^iz^j$ 代入，
$t^d$ 归一后的前因子是
$t^{d-i-(k-1)j}$，由 (1.3) 为非负次幂。
因此
$$
\mathcal T_N(F_D^r)\in\mathcal A_h[t,Z].
$$
再用完全相同的 (3.2)–(3.3)，并把 $\Gamma B_{ij}$ 当作有界交换系数，
得到
$$
\widetilde P_\zeta:=\mathcal T_N P_{r,\zeta}
\in\mathcal A_h[t,Z].
\tag{3.8}
$$

应用 (2.6)，$A^h\mathcal T_NQ_{r,\zeta}
=\widetilde P_\zeta-\widetilde P$。
右侧没有负 $t$ 次幂；
$A^h$ 为实际单射算子，逐个负次系数消去它，得到
$$
\boxed{
\widetilde Q:=\mathcal T_NQ_{r,\zeta}
\in\mathcal A_h[t,Z].
}
\tag{3.9}
$$
这只消去零等式中的单射因子，不是对慢系数作新的有界除法。

## 4. 有限结果式的最高系数为实际单位

定义
$$
E_\zeta(x)=\operatorname{Res}_y(P_r,Q_{r,\zeta}).
\tag{4.1}
$$
由于 $P_r$ 关于 $y$ 首一，
它是有限自由模上乘 $Q_{r,\zeta}$ 的行列式；
伴随矩阵给实际有限多项式 $A_\zeta,B_\zeta$：
$$
E_\zeta=A_\zeta P_r+B_\zeta Q_{r,\zeta}.
\tag{4.2}
$$

$\widetilde P$ 关于 $Z$ 仍首一、次数 $n$，
因为 $N=(k-1)n$。
原 $y$ 变量的平移与缩放，在形式 Laurent 环内可逆。
有限自由模的范数由此给
$$
\operatorname{Res}_Z(\widetilde P,\widetilde Q)
=t^{Nn}E_\zeta(t^{-1}).
\tag{4.3}
$$
左侧属于 $\mathcal A_h[t]$。
所以实际系数严格满足
$$
\boxed{\deg_xE_\zeta\le D:=Nn=(k-1)m^2r^2.}
\tag{4.4}
$$
这不是仅在字符下成立的次数界。

### 4.1 最高系数的完整字符

由 (3.4)、(2.7)，
$$
\chi(\widetilde P(0,Z))=H(Z)^r.
\tag{4.5}
$$
另一方面，在真实首位标量平移下，
$$
t^{k-1}\bigl[
\Psi(t^{-1})-\Psi(t^{-1}-2\alpha)-2\gamma
\bigr]
\longrightarrow2kc\alpha
\quad(t\to0)
$$
作为形式多项式的常数项恒等式成立。
$x-2\alpha=t^{-1}(1-2\alpha t)$ 不改变最高边的 $x$ 字符。
因此 (2.7) 给
$$
\chi(\widetilde Q(0,Z))
=
\kappa_\zeta
\left[H(Z+2kc\alpha)^r-H(Z)^r\right].
\tag{4.6}
$$
这一步已经包含了所有混合 Bell 差；
不是把原 $F$ 先作点态剪切后误用一阶多项式定理。

写
$$
E_\zeta(x)=e_Dx^D+\cdots+e_0.
$$
(4.3) 的常数项和结果式函子性给
$$
\begin{aligned}
\chi(e_D)
&=\operatorname{Res}_Z\left(
H^r,\kappa_\zeta[H(\,\cdot+2kc\alpha)^r-H^r]\right)\\
&=\boxed{
\kappa_\zeta^{mr}
\operatorname{Res}_Z\bigl(H(Z),H(Z+2kc\alpha)\bigr)^{r^2}}.
\end{aligned}
\tag{4.7}
$$
由 (1.5)，这对每个 $\zeta^h\ne1$ 都非零。
$\mathcal A_h$ 的唯一字符性质使 $e_D$ 成为真实 Banach 代数单位。

## 5. 空谱逆与完整深域排核

令
$$
M=\ker\mathsf P_r.
$$
由 (4.2)、(2.6)，
$$
A^hE_\zeta
=(A^hA_\zeta-B_\zeta)P_r+B_\zeta P_{r,\zeta}.
\tag{5.1}
$$
借实际有界拟幂零逆 $L=X^{-1}$，置
$$
\rho_\zeta=e_D+\sum_{j<D}e_jL^{D-j}
=e_D(I+LK_\zeta),\quad K_\zeta\in\mathfrak C.
$$
$L$ 与 $K_\zeta$ 交换，故 $LK_\zeta$ 拟幂零。
由 (4.7)，
$$
\boxed{\rho_\zeta,\rho_\zeta^{-1}\in\mathfrak C,\qquad
\rho_\zeta M=M.}
\tag{5.2}
$$
最后一个等式使用 R88 的全交换子不变性，
没有假设慢系数多项式在未知限制上稠密。

取 R186 共同正则器 $R$。
选有限 $N_*$ 覆盖 (5.1) 的全部多项式次数、中间自然词及 $X^D$。
对于
$$
f\in R^{N_*}M,\qquad
g\in U_\zeta R^{N_*}M,
$$
所有实际混合域都合法，
$P_rf=0$、$P_{r,\zeta}g=0$；
有界交换子 $L^D$ 保持这些域。

将 (5.1) 左乘 $L^D$，再作原双线性配对，得到
$$
\begin{aligned}
B(A^h\rho_\zeta f,g)
&=B(P_{r,\zeta}L^DB_\zeta f,g)\\
&=B(L^DB_\zeta f,P_{r,\zeta}g)=0.
\end{aligned}
\tag{5.3}
$$
只使用原 $H$ 上完整 $C$ 自伴的最大实现；
没有将 $C$ 下传到未知限制。

R186 给两个测试空间分别在 $M,U_\zeta M$ 中稠密。
再用 (5.2) 及 $A^h$ 对任意闭 $A$ 不变限制的稠密像，
$$
B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).
\tag{5.4}
$$
所以所有反射乘积的 Fourier 支撑都包含于有限群 $\mu_h$，
逐个模 $h$ 物理柱为常数。
若 $M\ne0$，严格正权及遍历性使其总本质支撑全测；
每柱比较非零反射乘积使限制维数至多1，
从而 $\dim M\le h$。
这与单射拟幂零 $A$ 没有非零有限维不变空间矛盾。

因此 $M=0$。完整 $C$ 自伴给稠密像，
(2.4) 的真正循环图核心给 (1.6)。

## 6. 明确的重根上边例子

令
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j,
\quad \frac12<\sigma\le1.
$$
$u$ 为空谱锚，$v$ 为全平面 first，且 $j_u=j_v=0$、$\alpha=1$。
取 $\Psi(x)=x^2$、$G(x,z)=z^2-x$。
此时 $k=m=2$、$d=2$、$H(Z)=Z^2$，
而 $H(Z+4)$ 与 $H(Z)$ 互素。
故
$$
\boxed{
[(v-u^2)^2-u-\lambda]^r e^w
\text{ 对全部 }\lambda\in\mathbb C,\ r\ge1,\ w\text{ 循环}.}
\tag{6.1}
$$
其原标量多项式为
$$
y^2-2x^2y+x^4-x-\lambda,
$$
在权 $\operatorname{wt}x=1,\operatorname{wt}y=2$ 下
顶边是 $(y-x^2)^2$，确有重根。
它并未满足上一非退化上边附录的简单根条件。

同一对 $u,v$ 还给
$$
q(v-\Psi(u))e^w
$$
对任意次数至少2的 $\Psi$ 和任意非零标量多项式 $q$ 循环。
$q$ 常数时直接使用 $e^w$ 循环；
非常数时是 (1.7)。

### 6.1 保留真正的碰撞边

若取 $G=z^2-\beta x^2$，仍用 $\Psi=x^2$、$\alpha=1$，
则
$$
H(Z)=Z^2-\beta,\qquad \text{平移量 }4.
$$
互素恰在 $\beta\ne4$ 时成立。
因此除 $\beta=4$ 外，
$$
[(v-u^2)^2-\beta u^2-\lambda]^r e^w
$$
全部循环。

$\beta=4$ 时，$H$ 的两个根为 $\pm2$，
平移量4造成真实碰撞，本稿不将该结果式判为单位。
即使两个点态因子分别已知循环，
仍不能因此把它们的乘积判为循环。

## 7. 未越过的边界

- 不覆盖 $H$ 与其首位平移有共同根的情形。
- 不覆盖 (1.3) 以外的全部剪切余项；
  更大的 $x$ 次数需重新计算实际次数界。
- 不将 $v-\Psi(u)$ 当成 closed first，
  不忽略它的所有自然词和混合 Bell 域。
- 没有空谱锚时，§5 的有界拟幂零逆仍缺失。
- 整个证明针对实际有限多项式；没有将形式参数代换解释为算子分数幂。

完整 Hilbert 不变子空间问题仍未完成。
