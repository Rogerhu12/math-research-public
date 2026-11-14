# 固定 61 二阶 Hecke 差分、连通核商与实际平方除法覆盖

日期：2026-11-12。状态：以下构造及其保留性质已证明。
它们精确限定 R126 的 $u^2=o(p)$ 与 R128 固定 Artin 生成元可以直接
提供的几何信息；**没有证明原始 Heegner 迹的增广指数为零。**

## 1. 固定数据与实际完整迹

沿用 R105、R126、R128：
$$
 E:y^2=x^3-17x,\quad F=\mathbf Q(\sqrt{-15}),\quad N=9248,
 \quad \pi:X_0(N)\longrightarrow E,\quad \pi(\infty)=O.
 \tag{1}
$$
令 $C=X_0(3N)$。R105 的两条 $3$-退化映射给固定映射
$\Phi:C\to E$，满足
$$
 \Phi(z_\ell)=(1+\tau_3)P[\ell],\qquad
 \Phi^*\omega_E=c\bigl(f(q)+3f(q^3)\bigr)\frac{dq}{q},\quad c\ne0.
 \tag{2}
$$
这里 $f(q)=q+\cdots$ 是 $E$ 的归一新形式，$\tau_3$ 是该文实际选定的
阶 $2$ 环类代表。特别地，$\tau_3$ 不是额外添设的 Galois 对称。

写 $H_\ell=F[\ell]$、$G_\ell=\operatorname{Gal}(H_\ell/H_1)$。
对本文所选辅助素数，
$$
 \operatorname{Gal}(H_\ell/F)=G_\ell\times\langle\tau_3\rangle,
 \quad |G_\ell|=\ell+1=pu,\quad p\nmid u.
$$
取 $U\subset G_\ell$ 为阶 $u$ 的子群，令
$$
 L=H_\ell^{U\times\langle\tau_3\rangle},\qquad
 Q=\operatorname{Tr}_{U}\Phi(z_\ell)
   =\operatorname{Tr}_{H_\ell/L}P[\ell].
 \tag{3}
$$
则 $[L:F]=p$，$Q$ 属于
$A(F)=\ker(N_{L/F}:E(L)\to E(F))$。

R126、R128 允许在无穷多个不同好素数 $p$ 上同时要求
$$
 u\ll p^{333/667},\quad r_+=r_-=1,\quad
 Q\ne O,\quad
 \widehat h_E(Q)\ll p^{666/667}\log p=o(p),
 \tag{4}
$$
并要求固定理想
$$
 \mathfrak b=(1+2\sqrt{-15}),\qquad N\mathfrak b=61
$$
的 Artin 像 $\sigma$ 生成 $\Gamma=\operatorname{Gal}(L/F)$。
可继续删除任何固定有限素数集合。这里没有对 $p$ 加普通或分裂条件。
在 R119 的秩一 $\mathcal O=\mathbf Z_p[\zeta_p]$ 模上写
$$
 Q=\delta^a v e,\qquad
 \delta=\tau^{(p-1)/2}(\tau-1),\qquad v\in\mathcal O^\times.
 \tag{5}
$$
R128 已在完整整数群上证明
$\Delta:=\sigma-1=\epsilon\delta$，其中 $\epsilon$ 为实际整自同构，
且
$$
 a\ge n\quad\Longleftrightarrow\quad Q\in\Delta^n A(F).
 \tag{6}
$$

## 2. 一个真实固定模曲线映射可强制增广指数增加二

令
$$
 C_2=X_0(61^2\cdot3N),
$$
并以 $r_0,r_1,r_2:C_2\to C$ 表示一条定向 cyclic $61^2$ 链的三个
顶点退化映射。在无穷尖点，其解析代表分别为
$z\mapsto z,61z,61^2z$。定义群律意义的映射
$$
 \Phi_2=\Phi\circ r_2-[2]\Phi\circ r_1+\Phi\circ r_0.
 \tag{7}
$$
它在 $\mathbf Q$ 上定义且把无穷尖点送到 $O$。
记 $F_0(q)=f(q)+3f(q^3)$。由 (2)，
$$
 \Phi_2^*\omega_E
 =c\bigl(F_0(q)-122F_0(q^{61})+3721F_0(q^{61^2})\bigr)\frac{dq}{q}.
 \tag{8}
$$
$q$ 的系数为 $c\ne0$，所以 $\Phi_2$ 非恒定，因而是有限映射。
**(8) 只证明非恒定。该微分明确属于 $61$-old 子空间；
没有证明、也没有使用其在新层的 newform 原始性。**

由于 $61$ 与 $\ell\cdot3N$ 互素，$\mathfrak b$ 收缩到
$\mathcal O_\ell$ 后是范数 $61$ 的可逆 proper 素理想。
它给一条在 $H_\ell$ 上定义的 cyclic $\mathfrak b^2$-同源链。
因此存在实际 CM 提升 $\widetilde z_\ell\in C_2(H_\ell)$。
取相容 Artin 方向，有
$$
 r_j(\widetilde z_\ell)=\sigma^j z_\ell,\qquad 0\le j\le2.
$$
相反互反律约定只把 $\sigma$ 全部换成 $\sigma^{-1}$；
这使 $\sigma-1$ 乘整自同构，不改变本文的像或指数。
由 (7) 得到实际点恒等式
$$
 \Phi_2(\widetilde z_\ell)=\Delta^2\Phi(z_\ell),\qquad
 Q_2:=\operatorname{Tr}_{U}\Phi_2(\widetilde z_\ell)=\Delta^2Q.
 \tag{9}
$$
$\Phi(z_\ell)$ 已被 $\tau_3$ 固定，所有 Artin 元互相交换，所以
$\Phi_2(\widetilde z_\ell)$ 也被 $\tau_3$ 固定；(9) 确在 $E(L)$ 中。

### 2.1 保留下来的算术性质

$\Delta$ 是 $A$ 上的同源，故 $Q_2$ 非挠且范数为零；
由 R128 的整自同构，
$$
 a(Q_2)=a(Q)+2.
 \tag{10}
$$
平方根 canonical height 是自由 Mordell--Weil 群上的范数，
且 Galois 作用保高度。因此
$$
 \widehat h_E(Q_2)
 \le(1+2+1)^2\widehat h_E(Q)=16\widehat h_E(Q)=o(p).
 \tag{11}
$$
$r_\pm$ 只依赖同一个 $E,F,L$ 的实际局部像，因而不变。
原先用于 R126 的 Baker 固定正高度下界在 $E(F^{\rm ab})$ 上仍适用：
若 $Q_2=[p]R$ 且 $R\in E(H_\ell)$，则 $R$ 非挠且
$\widehat h_E(Q_2)\ge p^2c_E$，与 (11) 矛盾。
故充分大 $p$ 时 $Q_2$ 仍不可被 $p$ 整除。

实际首 $\ell$-局部 jet 也保留。R114 的未分歧局部基域 $B$ 上，
$s^p=c_\ell$、$v_\ell(s)=1/p$，且所选迹满足
$$
 \log_E([2]Q)=c_1s+\{\text{估值严格大于 }1/p\text{ 的项}\},
 \qquad c_1\in\mathcal O_B^\times.
$$
固定主理想 $\mathfrak b$ 的环类像属于 $G_\ell$，所以在这个惯性
计算中固定 $B$，并送 $s$ 到 $\zeta s$，$\zeta$ 为本原 $p$ 次根。
因为 $\ell\ne p$，$\zeta-1$ 是 $\ell$-单位。于是
$$
 \log_E([2]Q_2)
 =c_1(\zeta-1)^2s+\{\text{估值严格大于 }1/p\text{ 的项}\}.
 \tag{12}
$$
首 jet 的准确估值和单位性均不变。

因此“固定非恒定模曲线映射的真实 CM 完整迹、$o(p)$ 高度、
两个非零局部符号、首 $\ell$-jet 单位、不可被 $p$ 除”这些性质，
本身允许增广指数至少为 $2$。这里的映射已明确换为 $\Phi_2$；
这不是原始 $\Phi$ 的反例，也不是 Sha 无限性的反例。

## 3. 连通核椭圆商：能做的精确优化与下降

### 3.1 固定的 Jacobian 因子，而非新层原始性

令 $J_2=\operatorname{Jac}(C_2)$，以无穷尖点为 Abel--Jacobi 基点。
Jacobian 的 Albanese 泛性质给唯一同态
$h:J_2\to E$，使 $\Phi_2=h\circ\iota$。
因 $\Phi_2$ 非恒定，$h$ 满射。取
$$
 K=(\ker h)^0,\qquad E'=J_2/K.
$$
特征零下 $K$ 是在 $\mathbf Q$ 上定义的阿贝尔子簇。
商可具体构造：取在 $\mathbf Q$ 上定义的 Poincaré 补子簇
$B\subset J_2$，使 $K\times B\to J_2$ 为同源，
再令 $E'=B/(B\cap K)$。有限商存在；$(k,b)\mapsto[b]$
经该同源下降，给核恰为 $K$ 的商映射。
因此 $E'$ 是椭圆曲线，且存在固定 $\mathbf Q$-同源
$$
 J_2\xrightarrow{q}E'\xrightarrow{\mu}E,\qquad
 \ker q\text{ 连通},\qquad h=\mu q.
 \tag{13}
$$
令 $\phi'=q\iota$、$d_\mu=\deg\mu$。于是
$\mu\phi'=\Phi_2$，$E'$ 与 $E$ 属于同一个 $\mathbf Q$-同源类。

这准确给出**本 Jacobian 同态的连通核商**。
并未识别 $E'$ 为最小导子 $N$ 上的 strong Weil 曲线；
也未识别 $\phi'$ 为新层 newform 的参数化。
事实上 $\mu^*\omega_E$ 是 $E'$ 的非零微分，所以
$\phi'^*\mu^*\omega_E=\Phi_2^*\omega_E$，(8) 的 old 子空间位置完整保留。
这不是对有限曲线映射 $C_2\to E$ 作出一个额外的曲线级 Stein 分解。

### 3.2 不能漏掉类数为二的完整迹

单独的 $\operatorname{Tr}_U\phi'(\widetilde z_\ell)$ 不必在 $L$ 上定义：
从 $\mu\phi'=\Phi_2$ 只能先把其 $\tau_3$ 差控制在 $\ker\mu$ 中。
为得到精确整数点，取
$$
 Y'=\operatorname{Tr}_{H_\ell/L}\phi'(\widetilde z_\ell)\in E'(L).
$$
由 (9) 的 $\tau_3$ 不变性，
$$
 \mu Y'=2Q_2.
$$
令 $\widehat\mu:E\to E'$ 为对偶同源，置
$$
 Z'=[d_\mu]Y'=[2]\widehat\mu(Q_2).
 \tag{14}
$$
该等式来自 $\widehat\mu\mu=[d_\mu]$，所以在整数点上成立。
它同时给 $N_{L/F}Z'=0$，无需假定裸 $Y'$ 的范数已为零。
$Z'$ 是固定映射 $[d_\mu]\phi'$ 的实际完整 CM 迹。
乘以 $d_\mu$ 后的映射不再声称具有连通 Jacobian 核；
连通核性质是 (13) 中 $q$ 的性质。

若 $p\nmid2d_\mu$，同源及其对偶在 $p$ 进完成的范数一
Mordell--Weil 格上互为单位倍数的逆，且与 $\Gamma$ 交换。
因此
$$
 a(Z')=a(Q_2)=a(Q)+2,\qquad
 \widehat h_{E'}(Z')=4d_\mu\widehat h_E(Q_2)
                  \le64d_\mu\widehat h_E(Q)=o(p).
 \tag{15}
$$
同样，$r_\pm$ 的 $p$-局部像经同源识别。
删除固定坏位及 $\ell\mid2d_\mu$ 后，$[2]\widehat\mu$ 的形式群
线性项为 $\ell$-单位，故 (12) 的首 jet 也保留。
不可被 $p$ 除可由 (14) 及 $\mu$ 的完成格同构，或由固定 CM
同源类的正高度下界直接得到。

所以连通核优化不能自动消去 (10) 的两个增广因子；其合法转移
需保留 (14) 的完整迹及固定整数倍，而非假定原来的 $U$-迹已下降。

## 4. 原始迹的实际平方除法覆盖

本节恢复原始 $\pi$ 与 $Q$，不使用 $\Phi_2$。
令 $C_0=X_0(N)$、$m=2u$，并取实际有效 CM 除子
$$
 D_\ell=\sum_{\alpha\in\operatorname{Gal}(H_\ell/L)}
           [\alpha x_\ell]\in \operatorname{Sym}^{m}C_0(L).
 \tag{16}
$$
定义求和映射
$$
 f_m:\operatorname{Sym}^{m}C_0\to E,\qquad
 \sum_i[x_i]\longmapsto\sum_i\pi(x_i).
$$
则 $f_m(D_\ell)=Q$。这里必须保留 **$m=2u$**：
在 $C=X_0(3N)$ 上仅取 $U$ 轨道，一般只得到在 $H_\ell^U$
上定义的除子；其映到 $E$ 后虽下降，除子本身未必下降到 $L$。

记 $S_m=\operatorname{Sym}^{m}C_0$，构造
$$
 W=\bigl(N_{L/F}\circ\operatorname{Res}_{L/F}f_m\bigr)^{-1}(O)
       \subset\operatorname{Res}_{L/F}S_m.
$$
限制后的求和映射为 $g:W\to A$。(16) 给实际点
$w_\ell\in W(F)$，且 $g(w_\ell)=Q$。
定义实际纤维积
$$
 X=W\times_{A,\Delta^2}A\longrightarrow W.
 \tag{17}
$$
这是有限 étale 覆盖，准确次数为 $p^4$。确实，在代数闭包上
$A=\{(P_0,\ldots,P_{p-1})\in E^p:\sum P_i=O\}$，
而 $\ker(\sigma-1)$ 是对角 $E[p]$，阶 $p^2$。
故 $\deg\Delta=p^2$、$\deg\Delta^2=p^4$。
R128 的整数商识别给
$$
 a(Q)\ge2
 \quad\Longleftrightarrow\quad
 Q\in\Delta^2A(F)
 \quad\Longleftrightarrow\quad
 w_\ell\text{ 有 }X(F)\text{ 中的提升}.
 \tag{18}
$$
覆盖的结构群为实际有限群方案 $A[\Delta^2]$；
没有将它替换成固定椭圆曲线上的 $[p]$-除法覆盖。

令 $g_0$ 为 $C_0$ 的亏格。当 $m\ge2g_0-1$ 时，
$S_m\to\operatorname{Pic}^m(C_0)$ 是相对维数 $m-g_0$ 的射影丛。
Jacobian 到 $E$ 的非零同态满射且光滑，所以 $f_m$ 光滑满射。
因此 $W$ 光滑，其每个分支的维数为
$$
 \dim W=mp-1=2pu-1.
 \tag{19}
$$
R126 的固定辅助同余模数可以一开始增大，使 $u$ 超过上述固定
阈值；这不改变 Fouvry 计数或 R128 的坏候选删除。
特别地，(17) 的底空间不是一条固定曲线，且随 $L,p,u$ 变化。
$u^2=o(p)$ 和次数 $p^4$ 本身不构成曲线 gonality 可应用的假设。

## 5. Riemann--Roch 为什么不保留所需 CM 条件

设 $o=\infty\in C_0(\mathbf Q)$，$J_0=\operatorname{Jac}(C_0)$。
因为有这个有理基点，对任意数域扩张 $K/F$，每个 $J_0(K)$
点对应实际次数零线丛。对任意 $m\ge g_0$，Riemann--Roch 给
$$
 h^0(C_{0,K},\mathcal L(mo))\ge m+1-g_0>0.
$$
故每个 $y\in J_0(K)$ 都可写成 $[D-mo]$，其中 $D$ 是在 $K$
上定义的次数 $m$ 有效除子。$m\ge2g_0-1$ 时其整个纤维为
$\mathbf P^{m-g_0}$。

取任意 $R\in A(F)\subset E(L)$。对固定有限映射 $\pi$，
pullback/norm 满足
$$
 \pi_*\pi^*=[d_\pi],\qquad d_\pi=\deg\pi.
$$
将上述 Riemann--Roch 用于
$y=\pi^*(\Delta^2R)\in J_0(L)$，得到有效除子 $D$ 满足
$$
 f_m(D)=[d_\pi]\Delta^2R.
 \tag{20}
$$
其范数仍为零，因而相应 $W(F)$ 点在 (17) 上有提升
$[d_\pi]R$。除去 $p\mid d_\pi$ 后，该固定乘数在所有增广
$p$-商上均为单位。

这证明“在一个对称幂里有低于 $\sqrt p$ 次数的有效除子”与
“像在 $\Delta^2A(F)$”完全相容。**Riemann--Roch 产生的 $D$
不必是 (16) 的实际 CM 轨道。** 唯一不能被这一步丢掉的限制，
正是原始 CM 轨道、原始 $\pi$ 及其整数 Hecke 关系。
本文不排除未来利用这项额外限制得到更强结论。

## 6. 固定 Hecke 对应尚未提供的反向压缩

在 $C$ 上，$T_{61}$ 是由两条退化映射给出的有限对应；
第一投影在一般点有 $62$ 条分支，不是一条在所有点上已选定的
自映射 $C\to C$。在 $\operatorname{Sym}^m C$ 上逐支选择对应，
一般次数为 $62^m$；选 cyclic 两步链则为 $(61\cdot62)^m$。
“61 固定”并未使整条 $m$ 点轨道的选择数固定或变成 $O(m^2)$。

实际 CM 点有 $\mathfrak b$ 给定的一条合法分支，故 (9) 成立。
但若只知道 $Q=\Delta^2R$，未知 $R\in A(F)$ 没有自动附带一个
在同一固定模曲线上、具有同一 CM 轨道条件的原像。
不能把 $\sigma R$ 直接改写为已选定的 Hecke 分支或 $E$ 的
CM 自同态作用。

目前真实构造是 (17)，而不是一个次数受 $u^2$ 控制的固定曲线覆盖。
要使 $u^2=o(p)$ 排除原始 $Q$ 的平方可除性，仍需构造保留 (16)
的低维对象或给出原始 Hecke 行的额外整数饱和输入。
(7)–(15) 说明这种输入须识别原始行，而非仅使用非恒定、
连通核商、局部单位或小高度。

## 7. 来源与独立核查范围

- 本仓 R105、R113–114、R119、R126、R128 提供实际映射、完整环类迹、
  范数一同源、首局部 jet、秩及辅助素数选择。本文保留它们的
  完整整数点规范，未更换为除以 $u$ 或除以类数的点。
- Milne，*Jacobian Varieties*（1986；作者 2021 修订版）
  [作者原文](https://www.jmilne.org/math/xnotes/JVs.pdf)，
  Proposition 6.1、印 pp.19–20，已亲读：
  本文用其带有理基点的 Albanese 泛性质。
- Milne，*Abelian Varieties*（2008，v2.00）
  [作者讲义](https://www.jmilne.org/math/CourseNotes/AV.pdf)，
  Chapter I Proposition 10.1 的证明（印 pp.42–43）给补子簇；
  Remark 8.12（印 pp.38–39，结论在 p.39）给有限子群商。
  已亲读这两处，并在 §3.1 写明 $B/(B\cap K)$ 的构造及下降。
  没有援引模形式新层原始性定理。
- Stacks Project（2026 查阅），
  [Tag 0B9R，Lemma 44.6.7](https://stacks.math.columbia.edu/tag/0B9R)，
  已亲读该引理及证明的有效除子、Riemann--Roch 与射影空间纤维部分。
  (20) 另将所需整数 pullback/norm 恒等式写明。

本篇的新增结论为固定差分对照、合法的连通核下降，以及实际
$p^4$ 平方除法覆盖的精确对象；原课题的无穷多个 $p$ 有限 Sha
断言仍未由这些结论推出。
