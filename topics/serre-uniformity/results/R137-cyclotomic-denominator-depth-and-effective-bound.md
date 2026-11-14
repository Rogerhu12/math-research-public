# R137：实际秩零商的分母深度与有效圆分范数界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本文始终假设 R69/R72 的实际正维秩零商存在，准确地说，实际三次角色具有某个非零中心值（等价的非零三次周期也可）。变化 $M$ 的全部相关中心值共同为零分支仍然开放，本文不消去这个前提。

在该前提下，R72 已把分母支撑限制到 exceptional 素数。本篇进一步控制每个负 $j$ 赋值，给分母的 $p$ 次根一个明确圆分理想范数的整除界；无需假定 exceptional 集为空。关键是使用同一实际尖点的形式参数 $z=q_{\rm Tate}^{1/p}$，对真实最优商的整微分积分，而非把 $q_{\rm Tate}$ 本身误当作参数。

## 1. 准确设置与结论

设 $p>37$，$E/\mathbb Q$ 无 CM，且
$$\rho_{E,p}(G_{\mathbb Q})=N_{\rm ns}(p)=C\rtimes\langle c\rangle.$$
假设 $p$ 处惯性严格小于 $C$。按 R66，这迫使
$$p\equiv2,5\pmod9,\qquad \rho_{E,p}(I_p)=C^3.$$
写 $K$ 为正规化子二次商域，$\eta$ 为 R66 的实际阶三角色。假设存在水平 $p$、权二、平凡 nebentype 的归一化新形式 $g$，满足
$$\boxed{L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.}\tag{137.1}$$
R69/R72 在这个准确前提下给每个配对分支的最优商
$$q:J(X_E^\alpha(p))\twoheadrightarrow A,\qquad A(\mathbb Q)\text{ 有限},$$
并给其真实整微分格。此处不假定每个配对分支有理点非空。

令 $F/\mathbb Q$ 为任何满足 $F[p]\simeq E[p]$ 的椭圆曲线，写既约分数
$$j(F)=a/b,\qquad b>0,\quad (a,b)=1.$$
R2/R72 给 $b=D^p$，其中 $D\in\mathbb Z_{\ge1}$，并且每个 $\ell\mid D$ 都满足
$$\ell\equiv\varepsilon_K(\ell)\pmod p,\qquad\ell\ge2p-1>p+1.$$
下面定义一个只依赖 $p$ 的正整数 $N_p$。

取 $\tau^2=-3$ 和非平凡三次角色 $\chi:\mathbb F_{p^2}^\times\to\mu_3$。令
$$B_i=\{b\in\mathbb F_p:\chi(1+b\tau)=\zeta_3^i\},\qquad
u_i=\sum_{b\in B_i}\zeta_p^b.$$
于是
$$B_0=-B_0,\ B_2=-B_1,\quad
|B_0|=(p-2)/3,\quad u_0+u_1+u_2=0.$$
置
$$L_p^+=\mathbb Q(\zeta_p+\zeta_p^{-1}),\qquad n=[L_p^+:\mathbb Q]=(p-1)/2,$$
$$\theta=\zeta_p+\zeta_p^{-1},\qquad
A_p(\theta)=u_0,\qquad
B_p(\theta)=\frac{u_1-u_2}{\zeta_p-\zeta_p^{-1}}.$$
这里 $A_p,B_p\in\mathbb Z[T]$ 是 R92 的实多项式；第二个商是代数整数，因为每个
$$(\zeta_p^b-\zeta_p^{-b})/(\zeta_p-\zeta_p^{-1})$$
是 $\theta$ 的整 Chebyshev 多项式。因此
$$\mathcal O_{L_p^+}=\mathbb Z[\theta],\qquad
\mathfrak J_p=(A_p(\theta),B_p(\theta)),\qquad
N_p=\#(\mathcal O_{L_p^+}/\mathfrak J_p).\tag{137.2}$$
$A_p(\theta)\ne0$：否则 $P_0(X)=\sum_{b\in B_0}X^b$ 被 $\Phi_p$ 整除，但它的系数并非全部相同，且 $0<|B_0|<p$。故 $N_p$ 是有限正整数。交换三次角色取向只改变 $B_p$ 的符号；改变原始根则直接作圆分 Galois 共轭。若固定原始根，改变非平方模型而把颜色坐标 $b$ 缩放为 $sb$，那么 $A_p$ 变成 $\sigma_s(A_p)$，$B_p$ 变成 $\sigma_s(B_p)$ 再乘
$$\frac{\zeta_p^s-\zeta_p^{-s}}{\zeta_p-\zeta_p^{-1}}.$$
此比值是实圆分单位：它是 $\zeta_p^{1-s}(1-\zeta_p^{2s})/(1-\zeta_p^2)$，为代数整数且绝对范数为一。因此 $\mathfrak J_p$ 只改变为 Galois 共轭理想，$N_p$ 不变。

**定理 137.1。** 在 (137.1) 和上述实际设置下，有
$$\boxed{D=\operatorname{den}(j(F))^{1/p}\mid N_p.}\tag{137.3}$$
更准确地，对每个 $\ell\mid D$，存在 $L_p^+$ 的一个 $\ell$ 上方素理想 $\lambda$，使
$$\boxed{v_\ell(D)\le v_\lambda(\mathfrak J_p).}\tag{137.4}$$
不同 $\ell$ 可对应不同 $\lambda$；本文没有断言同一 $\ell$ 的所有上方素理想都有该深度。

此外，置
$$Q_p=\frac{2p}{9}-\frac{4}{9(p-1)}>0.$$
完全初等的 Parseval 范数界为
$$N_p\mid\left|N_{L_p^+/\mathbb Q}(u_0)\right|,
\qquad
N_p\le\left|N_{L_p^+/\mathbb Q}(u_0)\right|
\le Q_p^{(p-1)/4}.\tag{137.5}$$
所以
$$\boxed{\log\operatorname{den}(j(F))
\le\frac{p(p-1)}4\log\left(\frac{2p}{9}-\frac{4}{9(p-1)}\right).}\tag{137.6}$$

**推论 137.2。** 每个负 $j$ 赋值严格满足
$$\boxed{0<\frac{-v_\ell(j(F))}{p}<\frac{p-1}{4},
\qquad 0<-v_\ell(j(F))<\frac{p(p-1)}4.}\tag{137.7}$$
特别，若每个负 $j$ 赋值都被 $p^2$ 整除，则 $j(F)$ 必为整数。此结论仍以 (137.1) 为前提。

## 2. 一个保留全部高次项的形式积分引理

**引理 137.3。** 令 $R$ 为 $\mathbb Q_\ell$ 有限未分歧扩张的整数环，$\ell>2$，$R'/R$ 为任意有限扩张。设 $\mathcal A/R$ 为阿贝尔概形，
$$h:\operatorname{Spf}R[[z]]\to\widehat{\mathcal A},\qquad h(0)=0,$$
为整形式态射。取 $z_0\in R$，$v_\ell(z_0)=m\in\mathbb Z_{\ge1}$，并假设 $h(z_0)=0$。若某个 $\mathcal A_{R'}$ 的整不变微分 $\omega$ 拉回为
$$h^*\omega=(c_0+c_1z+c_2z^2+\cdots)\,dz,\qquad c_i\in R',$$
则
$$v_\ell(c_0)\ge m.$$
这里所有赋值按 $v_\ell(\ell)=1$ 归一化；$R'$ 可以分歧。

**证明。** 阿贝尔形式群的特征零形式对数给 $\omega$ 的零常数原函数，其沿 $h$ 拉回是
$$\sum_{r\ge1}\frac{c_{r-1}}r z^r.$$
$z_0$ 的赋值至少一，所以该级数收敛；$h(z_0)=h(0)$ 给
$$0=c_0z_0+\sum_{r\ge2}\frac{c_{r-1}}r z_0^r.\tag{137.8}$$
对每个 $r\ge2$，有 $v_\ell(r)\le r-2$。对 $r=2$ 这是 $0\le0$；对 $r\ge3$，若 $k=v_\ell(r)>0$，则 $r\ge\ell^k\ge3^k\ge k+2$。因此
$$v_\ell(c_{r-1}z_0^r/r)\ge rm-v_\ell(r)
\ge2m+(r-2)(m-1)\ge2m.$$
各项赋值还随 $r$ 趋于无穷，因为 $rm-v_\ell(r)\ge r-\log_\ell r\to\infty$；这个论证也覆盖 $m=1$。所以尾和确实属于赋值至少 $2m$ 的闭球。由 (137.8)，$v_\ell(c_0z_0)\ge2m$，即所求。证明没有把积分分母 $r$ 当作处处的单位。证毕。

## 3. 同一实际圆盘中的商像相等不需 nonexceptional

取 $\ell\mid D$。实际同余 $F[p]\simeq E[p]$ 给某个配对分支 $X=X_E^\alpha(p)$ 上的有理点 $P$。R72 §§7–8 已给：

- $X$ 在 $\ell$ 为未分歧的完整水平曲线扭曲，有光滑射影好模型；
- 尖点概形有限 étale，$P$ 的约化是有理尖点 $c_0$，具有唯一局部尖点提升 $c$；
- $P,c$ 在同一未分歧剩余圆盘；
- $J$ 与最优商 $A$ 好约化，R72 的饱和整微分格可用。

令 $\mathcal D$ 为全部几何尖点之和，$\delta=(p^2-1)/2$，考虑真实 $\mathbb Q$ 态射
$$\Phi:X\to A,\qquad x\mapsto q([\delta x-\mathcal D]).$$
$\Phi(P)$ 因 $A(\mathbb Q)$ 有限而为挠点；R72 (72.20)–(72.21) 的模单位／忘线证明给 $\Phi(c)$ 也是挠点。两者约化相同，差落在未分歧局部阿贝尔形式群中。该群在 $\ell>2$ 无挠，因此
$$\boxed{\Phi(P)=\Phi(c).}\tag{137.9}$$
这正是 R72 (72.22) 的前半步；它只使用秩零、尖点挠性与未分歧好约化。R72 随后才用 nonexceptional 得形式浸入。本文在 (137.9) 之后改用引理137.3，故没有循环假定 exceptional 消失。

在有限未分歧扩张上取与实际 Tate 基及 Cartan 颜色同时对齐的参数
$$z=q_{\rm Tate}^{1/p}.$$
由于 $j=z^{-p}+744+\cdots$，
$$v_\ell(z(P))=-v_\ell(j(F))/p=v_\ell(D)=m\ge1.\tag{137.10}$$
这也明确解释了为什么不能从 $p\mid-v_\ell(j)$ 得出 $v_\ell(z)\ge p$；正确的一般下界只有一。

## 4. 一次微分系数迫使圆分理想有同样深度

R72 (72.9) 的两个微分 $\Omega_1,\Omega_2$，由已发表的 Raynaud–Mazur 正合性和最优商微分格饱和性，是真实 $A$ 整不变微分的拉回。允许加入新形式系数域的整数环 $R'$，这一步不要求 Hecke 幂等元整，也不要求 $R'/R$ 未分歧。

在同一个实际尖点和同一原始根选择下，R72 (72.15) 给它们的常数项
$$\kappa\sigma_a(u_j-u_0),\qquad j=1,2,$$
其中 $a\in\mathbb F_p^\times$，$\kappa$ 为 $p$ 次单位根。对于 $\Phi$ 的拉回微分，另乘 $\delta$；$\delta,\kappa$ 均为 $\ell$-单位。

由 (137.9)、(137.10) 和引理137.3，
$$v_\ell(\sigma_a(u_1-u_0))\ge m,
\qquad v_\ell(\sigma_a(u_2-u_0))\ge m.$$
因为 $u_0+u_1+u_2=0$ 且 $3$ 为 $\ell$-单位，三个 $\sigma_a(u_i)$ 都有赋值至少 $m$。

又 $\zeta_p^a-\zeta_p^{-a}$ 为 $\ell$-单位：若其约化为零，则原始 $p$ 次根的平方等于一，与 $p$ 为奇素数且 $\ell\ne p$ 矛盾。因此
$$v_\ell(\sigma_a(A_p(\theta)))\ge m,
\qquad v_\ell(\sigma_a(B_p(\theta)))\ge m.\tag{137.11}$$
实际原始根的嵌入选出一个实圆分素理想；把 $\sigma_a$ 移到素理想上，(137.11) 就是某个 $\lambda\mid\ell$ 上的 (137.4)。这个过程没有独立重选频率，也没有要求所有 Galois 共轭满足同一赋值。

由于 $\ell\equiv\pm1\pmod p$，它在 $L_p^+$ 中完全分裂。因此
$$v_\ell(N_p)=\sum_{\lambda\mid\ell}v_\lambda(\mathfrak J_p)\ge m=v_\ell(D).$$
逐个 $\ell\mid D$ 相乘即得 $D\mid N_p$。

## 5. 范数的有效上界

由于 $(u_0)\subset\mathfrak J_p$，正整数 $N_p$ 整除 $|N_{L_p^+/\mathbb Q}(u_0)|$。令 $k=|B_0|=(p-2)/3$，对全部 $a\in\mathbb F_p$ 定义
$$u_0(a)=\sum_{b\in B_0}\zeta_p^{ab}.$$
加性角色正交性直接给 Parseval 恒等式
$$\sum_{a\in\mathbb F_p}|u_0(a)|^2
=\sum_{b,b'\in B_0}\sum_{a\in\mathbb F_p}\zeta_p^{a(b-b')}
=pk.\tag{137.12}$$
由于 $B_0=-B_0$，每个 $u_0(a)$ 是实数，且 $u_0(a)=u_0(-a)$。又 $u_0(0)=k$，而非零 $a$ 的 $\{a,-a\}$ 对恰给 $L_p^+$ 的全部 $n$ 个实嵌入。因此
$$\frac1n\sum_{\sigma:L_p^+\hookrightarrow\mathbb R}\sigma(u_0)^2
=\frac{pk-k^2}{p-1}
=\frac{2(p-2)(p+1)}{9(p-1)}
=Q_p.\tag{137.13}$$
已经证明 $u_0\ne0$，所以其所有共轭均非零。将算术—几何平均不等式用于这 $n$ 个正数 $\sigma(u_0)^2$，得
$$|N_{L_p^+/\mathbb Q}(u_0)|^2
=\prod_{\sigma}\sigma(u_0)^2
\le Q_p^n.$$
开平方即为 (137.5)；再由 $b=D^p$ 和 (137.3) 得 (137.6)。此范数估计只用精确角色正交性和算术—几何平均，不需要逐个 Fourier 和的 Weil 界或任何上同调输入。

## 6. 逐素数深度的严格上界

对 $\ell\mid D$，
$$m\log\ell\le\log D\le\log N_p
\le\frac{p-1}{4}\log Q_p.$$
而
$$Q_p<\frac{2p}{9}<2p-1\le\ell.$$
故 $\log Q_p<\log\ell$，严格推出
$$m<\frac{p-1}{4}.$$
乘 $p$ 得 (137.7)。若 $p^2\mid-v_\ell(j)$，则 $p\mid m$；正整数 $m$ 至少为 $p$，与此上界矛盾。因此该情形无任何分母素数。

## 7. 可复用边界与下一项

1. $N_p$ 是由明确整数多项式生成的理想范数，可用整数线性代数完全计算；它不依赖 $E,F,K,\eta$ 或其导子。但**将它用于实际曲线仍要求 (137.1)**。
2. R92 的四层 $\mathfrak J_p=\mathcal O$ 作为特例直接给 $D=1$。本篇没有扩大有限水平窗口，也未证明所有 $p$ 的 $N_p=1$。
3. 当 R66、R81、R87 或其他已证范围提供非零周期时，本文均可接入；不把这些充分范围延伸到共同中心零分支。
4. 新结论是全 $p$ 的实际分母深度及总分母界。它不是对 $j$ 分子的高度界，也没有控制变化的三次导子 $M$。一般共同非零目标 R122 和 Serre 统一性完成标准仍开放。

## 参考输入

- R2：实际 Tate 惯性、负 $j$ 赋值被 $p$ 整除及 $\ell\equiv\varepsilon_K(\ell)\pmod p$。
- R69、R72：实际秩零商、最优整微分格、同一实际尖点的 Tate 展开、全尖点除子及形式群无挠性。R72 所核 Mazur (1978), Proposition1.2、Corollary1.1 和 §1(c)；Raynaud (1974), Théorème3.3.3、Corollaire3.3.6(1)。
- R92：实圆分整数多项式 $A_p,B_p$ 及共同零理想。
