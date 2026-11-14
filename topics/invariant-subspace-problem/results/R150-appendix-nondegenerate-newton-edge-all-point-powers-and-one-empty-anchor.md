# R150 附录：非退化 Newton 上边、全部点态幂与一个空谱锚

日期：2026-11-13（UTC）。作者：kernel_resume_1cf；Astra-ISP-1cf8c51d 已核查全部混合导数阶数、系数环形式分簇、实际结果式次数、横截字符与跨核域。
状态：已证明，完整证明。承接普通双慢次数优势附录，保留全部交叉 Bell 系数，以实际结果式最高单位处理任意正整数点态幂。

## 1. 主结论及准确范围

取
$$
u=a_*+\sum_j a_j\chi_j,\qquad
v=c_*+\sum_j c_j\chi_j,\qquad a,c\in\ell^2(\mathbb C),
$$
两者非常数，并假设实际闭 first $X_u$ 空谱。
例如 $a\notin\ell^1$ 且某个相位方向满足
$$
\sum_j\left(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\right)<\infty
$$
已足够。第二个 first $X_v$ 不要求有预解点。

令
$$
j_0=\min\{j:(a_j,c_j)\ne(0,0)\},\qquad
h=2^{j_0},\quad \alpha=a_{j_0},\quad \gamma=c_{j_0}.
\tag{1.1}
$$
允许 $\alpha=0$ 或 $\gamma=0$，但两者不同时为零。

给定整数 $p,m\ge1$ 及一个标量多项式 $F(x,y)$，满足：

1. $F$ 关于 $y$ 的最高次为 $m$，最高系数是非零常数；
   先除这个常数，以下统一使 $F$ 关于 $y$ 首一。
2. 每个非零单项式 $x^iy^j$ 满足
   $$
   mi+pj\le mp.
   \tag{1.2}
   $$
3. 令 $F_0$ 为权 $\operatorname{wt}x=m,\operatorname{wt}y=p$ 下
   权恰为 $mp$ 的部分。标量多项式
   $$
   H(z)=F_0(1,z)
   \tag{1.3}
   $$
   有 $m$ 个两两不同、全部非零的复根。

记这些根为 $\Omega$，并令
$$
\delta=\min(p,m).
$$
对每个 $\omega\in\Omega$ 定义
$$
d_\omega=
\begin{cases}
-2\alpha\,\partial_xF_0(1,\omega),&m<p,\\
-2\gamma\,\partial_yF_0(1,\omega),&p<m,\\
-2\bigl[\alpha\,\partial_xF_0(1,\omega)
       +\gamma\,\partial_yF_0(1,\omega)\bigr],&p=m.
\end{cases}
\tag{1.4}
$$
最后假设真实首位在每个顶部分支上横截：
$$
\boxed{d_\omega\ne0\qquad(\omega\in\Omega).}
\tag{1.5}
$$

**定理 1。**
在以上条件下，对每个 $\lambda\in\mathbb C$、
每个整数 $r\ge1$、每个复 $\ell^2$ 指数权
$$
w=b_*+\sum_j b_j\chi_j,\qquad b\in\ell^2,
$$
都有
$$
\boxed{[F(u,v)-\lambda]^r e^w
\text{ 非零且对原 }A\text{ 循环}.}
\tag{1.6}
$$
若原 $F$ 未首一，先将 $F-\lambda$ 除其非零最高系数；
整体非零标量的 $r$ 次幂不影响循环性。

这不是把点态幂的真实乘子认成自然算子幂。
证明始终使用 $F^r$ 自己的全部混合 Bell 系数。

### 1.1 横截条件的简单形式

加权 Euler 恒等式在根处给
$$
m\,\partial_xF_0(1,\omega)
+p\omega\,H'(\omega)=0.
\tag{1.7}
$$
因此在本稿的非退化条件下：

- $p>m$ 时，(1.5) 等价于 $\alpha\ne0$，
  即 $j_u\le j_v$；
- $p<m$ 时，(1.5) 等价于 $\gamma\ne0$，
  即 $j_v\le j_u$；
- $p=m$ 时，(1.5) 等价于
  $$
  F_0(\alpha,\gamma)\ne0.
  \tag{1.8}
  $$
  当 $\alpha=0$ 时，右侧为 $\gamma^m\ne0$；
  当 $\alpha\ne0$ 时，这是 $H(\gamma/\alpha)\ne0$。

所以，较高标量次数的变量首先出现，足以处理不等次数的情形。
空谱锚仍只要求是 $u$，不要求较高次数必由空谱变量承担。

### 1.2 与已发表范围的扣除

旧 [R150](R150-empty-spectrum-anchor-rectangular-polynomial-cyclicity.md)
的非零矩形角不覆盖这里的 Newton 上边；
[R155](R155-empty-anchor-bounded-auxiliary-polynomials.md)
要求其余模式有界；
[R189 双方向附录](R189-appendix-one-empty-anchor-two-additive-direction-kernel-elimination.md)
只直接适用快系数 $\mathcal G[X,Y]$。
这里普通点态的全部 Bell 系数仅需属于 $\mathcal A_h$。

[此前普通双慢次数优势附录](R150-appendix-empty-first-anchor-newton-degree-and-ordinary-two-slow-cyclicity.md)已证明
$p>m$、$j_u\le j_v$ 时 $f(v)-g(u)-\lambda$ 的 $r=1$ 情形。
本稿新增的是：所有点态幂、允许真正混合的低阶单项式，
以及上述一般非退化上边和横截情形。
不重复登记 R236 的单主行比较辅助二分、全阶 Sylvester 预算。

## 2. 全部混合 Bell 系数与实际首位商

固定 $\lambda,r,w$。把 $F-\lambda$ 记为 $F$；
常数平移不改变 §§1.1–1.5 的条件。

令
$$
X=X_{u,b},\qquad Y=X_{v,b},\qquad \xi=e^w.
$$
由 [R176 §10](R176-natural-polynomial-maximal-graphs-and-bell-domains.md)
和 [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)，
这是实际闭 first 加有界交换倾斜，
全部混合词自然域与共同正则化已存在，
$\xi$ 属于每个有限混合词的域。
$X$ 仍空谱，且
$$
L=X^{-1}\in\mathfrak C=\{A\}'
$$
为有界拟幂零交换子。

令
$$
R_j=R_j(b)=\frac{I-e^{-2b_j}N_j}{I+e^{-2b_j}N_j},
$$
并定义真正范数整的联合规范 Bell 函数
$$
\mathcal B(s,t)=
\prod_j e^{-(sa_j+tc_j)R_j}
\left[\cosh(sa_j+tc_j)I+R_j\sinh(sa_j+tc_j)\right].
\tag{2.1}
$$
平方可和及局部 $I+O(|sa_j+tc_j|^2)$ 估计保证紧集上一致范数收敛。
写
$$
B_{ij}=\partial_s^i\partial_t^j\mathcal B(0,0).
$$
则
$$
B_{00}=I,\quad B_{10}=B_{01}=0,\qquad
B_{ij}\in\mathcal A_h:=\overline{\mathbb C[I,A^h]},
\tag{2.2}
$$
$$
\chi(B_{ij})=0\qquad(i+j>0).
\tag{2.3}
$$
早于 $j_0$ 的局部因子精确为 $I$；
任意早位指数权不会引入低位 Bell 项。

真实点态幂由完整有限微分式实现：
$$
P_r(x,y)=
\sum_{i,j\ge0}\frac{B_{ij}}{i!j!}
\,\partial_x^i\partial_y^j F(x,y)^r.
\tag{2.4}
$$
求和在多项式次数处自动截断，包含所有交叉系数 $B_{ij}$。
它关于 $y$ 首一、次数
$$
n=mr.
\tag{2.5}
$$
R186 给其规范最大闭实现 $\mathsf P_r$，
它是自然混合图的闭包、在原 $H$ 上 $C$ 自伴，并且
$$
\mathsf P_r\xi=[F(u,v)]^r e^w.
\tag{2.6}
$$
$\xi$ 生成真正的循环图核心。

固定 dyadic $\zeta$，令 $\Gamma=\gamma_\zeta$。
实际同域协变为
$$
\Gamma X=X+D_X,\qquad \Gamma Y=Y+D_Y,
$$
且
$$
D_X=A^h d_X,\quad D_Y=A^h d_Y,\qquad d_X,d_Y\in\mathcal A_h.
\tag{2.7}
$$
R124 的实际余数分解（含 $h=1$）及 R139 §1 还给
$$
\Gamma E-E\in A^h\mathcal A_h\qquad(E\in\mathcal A_h).
\tag{2.8}
$$
因此下式的商是实际有限多项式，不是形式除法：
$$
P_{r,\zeta}(x,y)
=(\Gamma P_r)(x+D_X,y+D_Y),
$$
$$
\boxed{P_{r,\zeta}-P_r=A^hQ_{r,\zeta},
\qquad Q_{r,\zeta}\in\mathcal A_h[x,y].}
\tag{2.9}
$$
因为两个 $P$ 均关于 $y$ 首一、次数 $n$，
$\deg_yQ_{r,\zeta}\le n-1$。

### 2.1 完整交叉字符，而非单行近似

令
$$
\tau=e^{-2b_{j_0}},\qquad d=d_{j_0}=W_h,\qquad
\kappa_\zeta=\frac{\tau(\zeta^h-1)}d.
\tag{2.10}
$$
首位变量 $\ell=\alpha s+\gamma t$ 的局部 Bell 因子，
在 $A^h$ 上的准确系数为
$$
\frac{\tau}{d}(e^{-2\ell}-1+2\ell).
\tag{2.11}
$$
这由
$R_{j_0}=I-2\tau A^h/d+O(A^{2h})$
直接展开得到。
其他位不贡献 $A^h$ 系数。
同时
$$
\chi(d_X)=-2\alpha\kappa_\zeta,\qquad
\chi(d_Y)=-2\gamma\kappa_\zeta.
\tag{2.12}
$$
将平移因子 $e^{sD_X+tD_Y}$ 与被 $\Gamma$ 作用的 (2.11) 合并，
线性项 $2\ell$ 精确抵消，
差商的完整生成式为
$\kappa_\zeta(e^{-2\ell}-1)$。
故
$$
\boxed{
\chi(P_r)=F^r,\qquad
\chi(Q_{r,\zeta})
=\kappa_\zeta\left[
F(x-2\alpha,y-2\gamma)^r-F(x,y)^r
\right].
}
\tag{2.13}
$$
这里 $e^{-2(\alpha s+\gamma t)}$ 的全部混合项均被保留。
每个商先由 (2.7)–(2.9) 得到为有界算子，
再取字符；未从形式首阶直接推断有界可除。

## 3. 一个有限结果式的真实次数界

设
$$
E_\zeta(x)=\operatorname{Res}_y(P_r,Q_{r,\zeta})
\in\mathcal A_h[x].
\tag{3.1}
$$
因为 $P_r$ 关于 $y$ 首一，有限自由模
$\mathcal A_h[x,y]/(P_r)$ 上乘 $Q_{r,\zeta}$ 的行列式
就是 (3.1)。
伴随矩阵及首一带余除法给实际有限多项式 $A_\zeta,B_\zeta$：
$$
E_\zeta=A_\zeta P_r+B_\zeta Q_{r,\zeta}.
\tag{3.2}
$$
本节证明
$$
\boxed{\deg_xE_\zeta\le D:=r^2(pm-\delta).}
\tag{3.3}
$$
这必须是实际系数的次数界；
仅仅知道更高系数字符为零并不足够。

### 3.1 形式参数与标量分支

$t$ 以下只是证明有限多项式恒等式用的中心形式变量，
不在实际算子上取分数幂，也不要求形式级数收敛。

置
$$
F_t(X_0,Y_0)
=t^{mp}F(t^{-m}X_0,t^{-p}Y_0)
\in\mathbb C[t,X_0,Y_0].
\tag{3.4}
$$
(1.2) 保证没有负 $t$ 次幂，且 $F_{t=0}=F_0$。

对每个 $\omega\in\Omega$，
由于 $H'(\omega)\ne0$，逐阶解标量方程得到唯一
$$
z_\omega(t)\in\mathbb C[[t]],\qquad
z_\omega(0)=\omega,\qquad
F_t(1,z_\omega(t))=0.
\tag{3.5}
$$
每一步未知系数乘以同一个非零常数 $H'(\omega)$，
所以这是直接的递归构造。

定义
$$
\widetilde P(t,z)=t^{pn}P_r(t^{-m},t^{-p}z),\qquad
\widetilde Q(t,z)=t^{pn}Q_{r,\zeta}(t^{-m},t^{-p}z).
\tag{3.6}
$$
二者均在 $\mathcal A_h[t,z]$ 中。
对于 $P_r$，这是每次 $\partial_x,\partial_y$
分别降低权 $m,p$ 的直接结果。
$P_{r,\zeta}$ 的有界平移也只降低权；
(2.9) 中 $A^h$ 是实际单射算子，逐个系数消去它，
可知 $Q_{r,\zeta}$ 同样没有更高权项。
此外
$$
\widetilde P(0,z)=H(z)^r.
\tag{3.7}
$$

### 3.2 所有混合导数都有足够的簇内阶数

固定 $\omega$，代入
$$
z=z_\omega(t)+t^\delta Z.
$$
由 (3.5)，
$$
F_t(1,z_\omega(t)+t^\delta Z)\in
t^\delta\mathbb C[Z][[t]].
\tag{3.8}
$$

对 (2.4) 的任意 $(i,j)$ 项，链式缩放给
$$
\begin{aligned}
&t^{pn}
(\partial_x^i\partial_y^jF^r)
(t^{-m},t^{-p}(z_\omega(t)+t^\delta Z))\\
&\quad =
t^{mi+pj}
\left.
\partial_{X_0}^i\partial_{Y_0}^jF_t(X_0,Y_0)^r
\right|_{X_0=1,\ Y_0=z_\omega(t)+t^\delta Z}.
\end{aligned}
\tag{3.9}
$$
乘积求导的每一项最多命中 $i+j$ 个 $F_t$ 因子，
所以至少留下 $\max(r-i-j,0)$ 个未求导因子。
(3.8) 因而给总阶数至少
$$
mi+pj+\delta\max(r-i-j,0)\ge\delta r.
\tag{3.10}
$$
这同时处理所有交叉 $i,j$；没有删除协方差或高阶混合累积量。

对 $P_{r,\zeta}$ 也完全相同：
只需将 (3.9) 的取值点改为
$$
X_0=1+t^mD_X,\qquad
Y_0=z_\omega(t)+t^\delta Z+t^pD_Y.
$$
因为 $m,p\ge\delta$，
$F_t$ 在这个点仍被 $t^\delta$ 整除。
被 $\Gamma$ 作用的 Bell 系数只作为交换有界系数保留，
不改变 $t$ 阶数。

故 $\widetilde P$ 和对应的 $\widetilde P_\zeta$
在上述代入后都被 $t^{\delta r}$ 整除。
利用 (2.9) 及 $A^h$ 的单射性，逐个 $t,Z$ 系数消去 $A^h$，
得到
$$
\boxed{
\widetilde P(t,z_\omega(t)+t^\delta Z),\
\widetilde Q(t,z_\omega(t)+t^\delta Z)
\in t^{\delta r}\mathcal A_h[Z][[t]].
}
\tag{3.11}
$$
这一步只消去零等式中的单射因子，不对未知零字符系数作有界除法。

### 3.3 只用标量互素常数的形式分簇

因为 (3.7) 的因子 $(z-\omega)^r$ 两两互素，
存在唯一的首一分解
$$
\widetilde P(t,z)=\prod_{\omega\in\Omega}P_\omega(t,z),
$$
$$
P_\omega\in\mathcal A_h[[t]][z],\quad
\deg_zP_\omega=r,\quad
P_\omega(0,z)=(z-\omega)^r.
\tag{3.12}
$$
为明确其系数环合法性，可以逐阶构造：
在已构造到 $t^{k-1}$ 后，$t^k$ 的乘积误差是次数小于 $n$
的多项式，需写成
$$
\sum_\omega h_\omega(z)
\prod_{\omega'\ne\omega}(z-\omega')^r,\qquad
\deg h_\omega<r.
$$
这是由标量两两互素多项式给出的 Hermite 余数分解；
对应有限矩阵在 $\mathbb C$ 上可逆，
所以同一矩阵在任意含 $\mathbb C$ 的交换代数上也可逆。
递归由此完成，不需要实际算子系数的根。

将 (3.12) 代入 $z_\omega(t)+t^\delta Z$。
其他因子的乘积在 $t=0$ 是非零标量
$$
\prod_{\omega'\ne\omega}(\omega-\omega')^r,
$$
故在 $\mathcal A_h[Z][[t]]$ 中为单位。
结合 (3.11)，得到真正的形式多项式
$$
\widehat P_\omega(t,Z)
=t^{-\delta r}
P_\omega(t,z_\omega(t)+t^\delta Z)
\in\mathcal A_h[[t]][Z],
\tag{3.13}
$$
它关于 $Z$ 首一、次数 $r$。
同理
$$
\widehat Q_\omega(t,Z)
=t^{-\delta r}
\widetilde Q(t,z_\omega(t)+t^\delta Z)
\in\mathcal A_h[[t]][Z].
\tag{3.14}
$$

### 3.4 自由模范数给精确的总阶数

在形式 Laurent 环内，变量替换
$z=z_\omega(t)+t^\delta Z$ 是可逆的。
由自由模行列式（即多项式范数），(3.13)–(3.14) 给
$$
\operatorname{Res}_z(P_\omega,\widetilde Q)
=
t^{\delta r^2}
\operatorname{Res}_Z(\widehat P_\omega,\widehat Q_\omega).
\tag{3.15}
$$
理由是被取范数的 $\widetilde Q$ 变成
$t^{\delta r}\widehat Q_\omega$，而模的秩为 $r$。
右侧除前因子外属于 $\mathcal A_h[[t]]$。

结果式对首个参数的乘法性使
$$
\operatorname{Res}_z(\widetilde P,\widetilde Q)
\in t^{\delta mr^2}\mathcal A_h[[t]].
\tag{3.16}
$$
另一方面，由 (3.6) 的首一缩放，
$$
\operatorname{Res}_z(\widetilde P,\widetilde Q)
=
t^{pn^2}E_\zeta(t^{-m}).
\tag{3.17}
$$
因此
$$
E_\zeta(t^{-m})
\in
t^{-m r^2(pm-\delta)}\mathcal A_h[[t]].
\tag{3.18}
$$
但左侧是一个有限 Laurent 多项式，
不同 $x$ 次幂给不同的 $t$ 次幂；
故所有高于 $D=r^2(pm-\delta)$ 的实际系数都严格为零。
(3.3) 得证。

## 4. 最高系数的字符非零，因而是真单位

现在可以安全地只计算次数 $D$ 的字符，
因为 §3 已排除所有更高实际系数。

记
$$
F^{\rm sh}(x,y)=F(x-2\alpha,y-2\gamma).
$$
由 (2.13)、结果式的函子性和乘法性，
$$
\begin{aligned}
\chi(E_\zeta)
&=\operatorname{Res}_y
(F^r,\kappa_\zeta[(F^{\rm sh})^r-F^r])\\
&=
\kappa_\zeta^{mr}
\operatorname{Res}_y(F,F^{\rm sh})^{r^2}.
\end{aligned}
\tag{4.1}
$$
第二步在模 $F$ 后把差替换为 $(F^{\rm sh})^r$，
再两次使用结果式的乘法性；不需要选择有界算子的谱支。

计算标量结果式
$$
E_1(x)=\operatorname{Res}_y(F,F^{\rm sh}).
$$
(3.5) 是首一标量多项式
$F_t(1,z)$ 的全部 $m$ 个形式根；
因此范数乘积给
$$
t^{pm^2}E_1(t^{-m})
=
\prod_{\omega\in\Omega}
F_t(1-2\alpha t^m,z_\omega(t)-2\gamma t^p).
\tag{4.2}
$$
由 $F_t(1,z_\omega(t))=0$ 和一阶 Taylor 公式，
每个因子的首项准确为
$$
t^\delta d_\omega.
\tag{4.3}
$$
这里当 $m<p$ 时只有 $x$ 平移贡献最低阶；
当 $p<m$ 时只有 $y$ 平移贡献；
相等时两者同时贡献，正是 (1.4)。
所有二次及以上平移项阶数严格大于 $\delta$，
系数中的正 $t$ 阶也不会改变该首项。

由 (1.5)，
$$
\deg_xE_1=pm-\delta,\qquad
[x^{pm-\delta}]E_1=\prod_{\omega\in\Omega}d_\omega\ne0.
\tag{4.4}
$$
于是写
$$
E_\zeta(x)=e_Dx^D+\cdots+e_0,
$$
有
$$
\boxed{
\chi(e_D)=
\kappa_\zeta^{mr}
\left(\prod_{\omega\in\Omega}d_\omega\right)^{r^2}
\ne0
\qquad(\zeta^h\ne1).
}
\tag{4.5}
$$
$\mathcal A_h$ 的唯一字符性质使 $e_D$ 成为实际 Banach 代数单位。
若 $D=0$，这已经说明整个 $E_\zeta$ 可逆；
后面公式仍适用，取 $L^0=I$。

## 5. 空谱逆、有界单位与全部深域配对

令
$$
M=\ker\mathsf P_r.
$$
$M$ 闭且 $A$ 不变，不预设它整体处在 $X,Y$ 的自然域。

由 (3.2)、(2.9)，有实际有限多项式恒等式
$$
A^hE_\zeta
=(A^hA_\zeta-B_\zeta)P_r+B_\zeta P_{r,\zeta}.
\tag{5.1}
$$
利用真实有界逆 $L=X^{-1}$，置
$$
\rho_\zeta=e_D+\sum_{k<D}e_kL^{D-k}
=e_D(I+LK_\zeta),\qquad K_\zeta\in\mathfrak C.
\tag{5.2}
$$
$L$ 拟幂零并与 $K_\zeta$ 交换，
故 $LK_\zeta$ 拟幂零；由 (4.5)，
$$
\rho_\zeta,\rho_\zeta^{-1}\in\mathfrak C.
\tag{5.3}
$$
R88 因而给
$$
\rho_\zeta M=M.
\tag{5.4}
$$
没有使用一般慢系数多项式的未知限制稠密性。

取 R186 的共同正则器 $R$，
并选择有限的 $N$ 覆盖 (5.1) 所有次数、全部中间自然词及 $X^D$。
在
$$
f\in R^NM,\qquad g\in U_\zeta R^NM
$$
上，所有等式都发生在真实混合域，
$P_r(X,Y)f=0$，
$P_{r,\zeta}(X,Y)g=0$。
有界交换子 $L^D$ 保持这些共同域，且
$L^DE_\zeta(X)f=\rho_\zeta f$。

将 (5.1) 左乘 $L^D$ 并与 $g$ 作原 $C$ 双线性配对，
$$
\begin{aligned}
B(A^h\rho_\zeta f,g)
&=B(P_{r,\zeta}(X,Y)L^DB_\zeta(X,Y)f,g)\\
&=B(L^DB_\zeta(X,Y)f,P_{r,\zeta}(X,Y)g)=0.
\end{aligned}
\tag{5.5}
$$
被移过配对的是原 $H$ 上完整 $C$ 自伴的规范最大实现；
没有给未知限制或子商假设一个继承的 $C$。

R186 保证两个测试空间分别在 $M,U_\zeta M$ 中稠密。
再用 (5.4) 及 $A^h$ 在每个闭 $A$ 不变限制上的稠密像，
得到
$$
\boxed{B(M,U_\zeta M)=0\qquad(\zeta^h\ne1).}
\tag{5.6}
$$

每个反射乘积 $f(y)g(-1-y)$ 的 Fourier 支撑遂包含于有限群 $\mu_h$，
所以它在每个模 $h$ 物理柱上为常数。
若 $M\ne0$，严格正权和 odometer 遍历性使 $M$ 的总本质支撑全测；
逐柱从可数基选一个非零反射乘积，
再固定其中一因子比较所有向量，得到每个柱上的限制维数至多1。
因此 $\dim M\le h$。
单射拟幂零 $A$ 不允许非零有限维不变空间，矛盾。

故 $\ker\mathsf P_r=0$。
原空间的完整 $C$ 自伴给稠密像，
而 (2.6) 的真实循环图核心使输出向量循环。
定理 1 得证。

## 6. 直接推论与具体真双慢例子

### 6.1 任意次数的分离多项式差及全部点态幂

令 $g,f$ 非恒定，$\deg g=p,\deg f=m$。
对
$$
F(x,y)=f_m^{-1}[f(y)-g(x)]
$$
有
$$
F_0=y^m-u_px^p,\qquad u_p=g_p/f_m\ne0,
$$
故顶部分支总是简单且非零。
由定理 1：

- $p>m$ 且 $j_u\le j_v$；
- 或 $p<m$ 且 $j_v\le j_u$；
- 或 $p=m$ 且 $f_m\gamma^m-g_p\alpha^m\ne0$；

以上任一项都保证
$$
\boxed{[f(v)-g(u)-\lambda]^r e^w
\text{ 对全部 }\lambda,r,w\text{ 循环}.}
\tag{6.1}
$$

第一项保留此前 $r=1$ 定理的全部量词并补齐全部点态幂。
不能仅靠已知两个因子各自循环来推导 (6.1)；
这里用的是完整点态幂的结果式。

### 6.2 含真正混合项的二、三次曲线

取任意 $\frac12<\sigma\le1$，
$$
u=\sum_{j\ge0}(j+1)^{-\sigma}\chi_j,\qquad
v=\sum_{j\ge0}(-1)^j(j+1)^{-\sigma}\chi_j.
$$
$u$ 为空谱相位类，$v$ 属全平面谱类；
两行模 $\ell^1$ 独立、物理支持完全重叠，首位都为0。

对任意复参数 $b,c,d,e,k$，令
$$
F(x,y)=y^2-x^3+bxy+cx^2+dx+ey+k.
\tag{6.2}
$$
取 $p=3,m=2$，所有余项权都严格低于6，
$F_0=y^2-x^3$ 有简单非零分支 $\pm1$，
且 $\alpha=1\ne0$。
因此
$$
\boxed{
[v^2-u^3+buv+cu^2+du+ev+k-\lambda]^r e^w
\text{ 对所有 }\lambda,\ r\ge1,\ w\text{ 循环}.
}
\tag{6.3}
$$
全部交叉 Bell 系数仍参与实际乘子。
这没有将 $uv$ 改写成自然乘积 $XY$，
也没有加入为取消慢 Bell 项设计的辅助符号。

同一对模式还满足 (6.1) 的反向不等次数条件，
所以 $[v^3-u^2-\lambda]^r e^w$ 也全部循环。

## 7. 明确保留的边界

1. 顶部 $H$ 有重根或零根时，(3.12) 的分簇与 (4.3) 的首项
   需要新的分析，本稿不宣称覆盖。
2. 横截首项 $d_\omega=0$ 时，更高实际系数可能只是字符为零；
   不能把它当作算子零，也不能仅凭一个较低单位系数倒推整多项式可逆。
3. $F^r$ 的交叉累积量从始至终由 (2.4)、(3.9)–(3.11) 保留。
   本稿没有把 $P_r$ 识别为 $P_1$ 的自然幂。
4. 两个独立全平面 first 且没有空谱线性组合时，
   仍缺少 §5 的有界拟幂零逆；一般单核继续开放。
5. 只对每个固定的有限多项式、整数 $r$、gauge 和指数权取有限深域；
   不需要随这些参数一致的正则阶数或范数预算。

完整 Hilbert 不变子空间问题仍未完成。
