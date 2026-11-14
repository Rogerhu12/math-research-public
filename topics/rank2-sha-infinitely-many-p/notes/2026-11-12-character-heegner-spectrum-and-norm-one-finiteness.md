# 实际环类角色谱与范数为零阿贝尔簇的完整 Sha 有限性

日期：2026-11-12。状态：已证明。

本文使用 R116 已证的实际 Heegner 迹非零性，证明它的每个非平凡
$C_p$ 角色投影都非零，并应用 Nekovář 的整角色版本 Euler system
定理。所得范数为零阿贝尔簇随 $(p,\ell)$ 改变；固定曲线
$E/\mathbb Q$ 的主问题仍未解决。

## 1. 实际点、角色与不可约有理表示

固定
$$
E:y^2=x^3-17x,\qquad F=\mathbb Q(\sqrt{-15}),\qquad N_E=9248,
$$
以及 R103 的模参数化 $\pi:X_0(N_E)\to E$，$\pi(\infty)=O$。
取 R110、R116 的合法 $(p,\ell)$：$p\ge7$ 在 $F,\mathbb Q(i)$
分裂，$\ell$ 在这两域惰性，且
$$
\ell+1=pu,\qquad p\nmid u.
$$
令 $H=F[\ell]$ 为环类域。由 R105 的二阶类提升，
$$
G=\operatorname{Gal}(H/F)\simeq C_2\times C_{\ell+1}.
$$
记 $G'$ 为 $G$ 的唯一阶 $2u$ 子群，$L=H^{G'}$，
$\Gamma=\operatorname{Gal}(L/F)=\langle\sigma\rangle\simeq C_p$。
设 $P[\ell]=\pi(x_\ell)$ 是原始实际 Heegner 点。本文的点为
$$
Q=\operatorname{Tr}_{H/L}P[\ell].                    \tag{1.1}
$$
它正是 R105–R116 的 $\operatorname{Tr}_U(1+\tau_3)P[\ell]$，
没有另外一个类数因子。因为 $a_\ell(E)=0$，Heegner 范数关系给
$$
N_\Gamma Q=0,\qquad N_\Gamma=1+\sigma+\cdots+\sigma^{p-1}. \tag{1.2}
$$
R116 证明：对目标素数集合中的相对密度一的 $p$，可选这样的
$\ell\ll p^L$（固定 $32/17<L<2$），使 $Q$ 非扭且
$Q\notin pE(H)$。以下每一条结论均对任意满足 $Q$ 非扭的
合法 $(p,\ell)$ 成立，不再使用密度论。

令 $W_Q=\mathbb Q[\Gamma]Q\subset E(L)\otimes\mathbb Q$。
由 (1.2)，$W_Q$ 是
$$
\mathbb Q[\Gamma]/(N_\Gamma)\simeq\mathbb Q(\zeta_p)
$$
的非零商模。右边是域，所以这个商映射为单射：
$$
W_Q\simeq\mathbb Q(\zeta_p).                         \tag{1.3}
$$
因此对每个非平凡复角色 $\chi$，未除群阶的点
$$
P_\chi=\sum_{\gamma\in\Gamma}\chi^{-1}(\gamma)\gamma Q
       =\sum_{g\in G}\chi^{-1}(g)gP[\ell]
       \in E(H)\otimes\mathbb Z[\zeta_p]             \tag{1.4}
$$
都非扭。这里将 $\chi$ 经 $G\twoheadrightarrow\Gamma$ 膨胀；
第二个等式就是 (1.1) 展开。证明使用特征零群表示和忠实的
复数扩标量，没有使用 $p$-adic logarithm 的张量注入。

## 2. 准确的 Gross–Zagier 谱公式

令 $f_E$ 为正规化的权二新形式，
$$
(f_E,f_E)=\int_{\Gamma_0(N_E)\backslash\mathfrak H}
 |f_E(z)|^2\,dx\,dy.
$$
用 Cai–Shu–Tian 的 $\widehat h_F$ 规范化，并将其按正定 Hermitian
形式延拓至复系数点。$\chi\ne1$ 的导子恰为 $\ell$：
它在 $\ell$ 处的阶 $p$ 惯性上非平凡，在其余地方不分歧。
所有 $N_E$ 的素因子在 $F$ 分裂，$(N_E,15\ell)=1$，
$\mathcal O_\ell^\times=\{\pm1\}$。因此
Cai–Shu–Tian（2014），Theorem 1.1，印刷 p.2525，直接给
$$
L'(1,E/F,\chi)
 =\frac{8\pi^2(f_E,f_E)}{\sqrt{15}\,\ell\deg\pi}
   \widehat h_F(P_\chi)>0.                           \tag{2.1}
$$
若 Artin 映射采用相反方向，(1.4) 中 $\chi$ 换成 $\chi^{-1}$；
全文的全体非平凡角色及下式不变。

角色正交性给
$$
\begin{aligned}
\sum_{\chi\in\widehat\Gamma}\widehat h_F(P_\chi)
 &=p\sum_{\gamma\in\Gamma}\widehat h_F(\gamma Q)\\
 &=p^2\widehat h_F(Q).
\end{aligned}
$$
平凡角色项由 (1.2) 为零。联立 (2.1) 得到实际指定子族的精确第一矩：
$$
\boxed{
\widehat h_F(Q)
 =\frac{\deg\pi\sqrt{15}}{8\pi^2(f_E,f_E)}
   \frac{\ell}{p^2}
   \sum_{\substack{\chi\in\widehat\Gamma\\\chi\ne1}}
       L'(1,E/F,\chi).
}                                                       \tag{2.2}
$$
这里没有把全环类群上的平均替换成指定阶 $p$ 子群上的平均。
例如，要由此证明 $\widehat h_F(Q)\ll u\log\ell$，仍需独立证明
这一个指定子族的导数和 $\ll p\log\ell$。目前已有的
$\widehat h(Q)\ll u^2\log\ell$ 不提供该省损。

## 3. 允许本 CM 情形、包含所有素数的 Nekovář 定理

所用原始结果为 Nekovář（2007），*The Euler system method for CM
points on Shimura curves*，Theorem 3.2；作者版本 pp.19–20 的
§§3.1.6、3.2、3.5.1 说明其整规范。

在本题需要的特例中：对 $X_0(N_E)$ 的有理简单商 $E$、
环类 CM 点 $x$、其定义域 $H/F$ 的角色 $\chi$ 和
$\mathcal O=\mathbb Z[\zeta_p]$，定义
$$
e_\chi=\sum_{g\in G}\chi^{-1}(g)g,\qquad
M^{(\chi)}=\{m:g m=\chi(g)m\ \text{对所有 }g\}.
$$
若 $E$ 不在 $H^{\ker\chi}$ 内任一虚二次域上获得 CM，且
$e_\chi P[\ell]$ 非扭，则
$$
\frac{(E(H)\otimes\mathcal O)^{(\chi)}}
     {\mathcal O e_\chi P[\ell]},\qquad
(\Sha(E/H)\otimes\mathcal O)^{(\chi)}               \tag{3.1}
$$
都是有限群。定理不要求 $p\nmid\#G$；§3.5.1 为每个系数素理想
$\mathfrak p$ 给一个独立于下降层 $M$ 的有限常数
$C(\mathfrak p)$。只有进一步要求该常数为零时，§3.5.2
才排除有限多个素理想。

### 3.1 CM 假设的实际核对

本曲线的全部非整数几何自同态首次在 $\mathbb Q(i)$ 上定义：
$[i](x,y)=(-x,iy)$。若一个虚二次域定义某个
$a+b[i]$，$b\ne0$，则其微分也定义 $i$，故该域就是
$\mathbb Q(i)$。这里定理排除的是这个域出现在指定角色域内，
并不排除曲线在代数闭包上有 CM。

$F$ 的判别式为 $-15$，环类域 $H/F$ 仅可能在 $\ell$ 分歧。
所以 $H/\mathbb Q$ 在 $2$ 未分歧。$\mathbb Q(i)/\mathbb Q$
却在 $2$ 分歧，因而
$$
\mathbb Q(i)\not\subset H,
\qquad\mathbb Q(i)\not\subset H^{\ker\chi}=L.       \tag{3.2}
$$
这严格验证 Nekovář 的条件。若先取 $J_0(N_E)$ 的最优商再与
$E$ 作有理同源，(1.4) 的非扭性及 (3.1) 的有限性均在同源下
保留；非平凡 $\chi$ 也消去模参数化的常数平移。

这避免两个不合法的简化：不能直接引用 Bertolini–Darmon
1990 中要求非 CM／满 $\mathrm{GL}_2$ 像的版本，也不能先在
$\mathbb Z_p[\Gamma]$ 中除以 $p$ 作整直和。

## 4. 范数为零部分的精确秩

由 (1.4)、(3.1)，每个非平凡 $\chi$ 的
$E(H)\otimes\mathbb C$ 本征空间恰一维。
它在 $G'$ 下不变，所以已经位于 $E(L)\otimes\mathbb C$。
令 R113 的实际阿贝尔簇为
$$
\mathcal B=\operatorname{Res}_{L/F}E_L,\qquad
\mathcal A=\ker(N:\mathcal B\to E).
$$
则 $\dim\mathcal A=p-1$，且
$$
\mathcal A(F)=\ker(N:E(L)\to E(F)).
$$
在有理 Mordell–Weil 模中，范数恰去掉平凡角色。因此
$$
\boxed{\operatorname{rank}\mathcal A(F)=p-1.}        \tag{4.1}
$$
R103 给 $\operatorname{rank}E(F)=3$，故同时
$\operatorname{rank}E(L)=p+2$。

## 5. 不除 $p$ 的整论证给出整个 $\Sha(\mathcal A/F)$ 有限

首先，限制映射
$$
\operatorname{res}:\Sha(E/L)\longrightarrow\Sha(E/H)
$$
的核被 $[H:L]$ 杀掉，因此有限：任何固定整数 $n$ 的
$\Sha(E/L)[n]$ 都是有限 $n$-Selmer 群的商。
$\mathcal O$ 是有限自由 $\mathbb Z$ 模，故张量后核仍有限。
限制与群作用相容，(3.1) 因而推出
$$
(\Sha(E/L)\otimes\mathcal O)^{(\chi)}
\quad\text{对每个 }\chi\ne1\text{ 都有限}.          \tag{5.1}
$$

记 $S=\Sha(E/L)$，$S^0=\ker(N_\Gamma:S\to S)$。
在 $\mathcal O[\Gamma]$ 中有严格的整恒等式
$$
\sum_{\chi\ne1}e_\chi=p-N_\Gamma.                  \tag{5.2}
$$
每个 $e_\chi(S\otimes\mathcal O)$ 都在 (5.1) 的有限群内。
故对 $z\in S^0$，
$$
p(z\otimes1)=\sum_{\chi\ne1}e_\chi(z\otimes1)
$$
落在一个固定有限群内。映射 $S\to S\otimes\mathcal O$，
$z\mapsto z\otimes1$，是单射，因为 $1$ 可包含在
$\mathcal O$ 的整基内。再用 $S[p]$ 有限，得到
$$
S^0\text{ 有限}.                                    \tag{5.3}
$$
特别地，$\ker(\operatorname{cor}_{L/F}:\Sha(E/L)\to\Sha(E/F))$
有限；它包含在 $S^0$ 中，因为
$\operatorname{res}\operatorname{cor}=N_\Gamma$。

对 $0\to\mathcal A\to\mathcal B\to E\to0$ 取全局上同调，
并用 Shapiro 同构 $\Sha(\mathcal B/F)=\Sha(E/L)$。于是
$\Sha(\mathcal A/F)$ 到 $\Sha(E/L)$ 的像在上述有限的 corestriction 核内；
其核则是
$$
E(F)/NE(L)
$$
的子商。因为 $pE(F)\subset NE(L)$，这个点商有限。
由此得到比逐初级有限性更强的结论：
$$
\boxed{\Sha(\mathcal A/F)\text{ 是有限群}.}          \tag{5.4}
$$
本论证完整包含群阶素数 $p$，没有将有理本征分解错误地视为
$p$-整直和，也没有假设任何基域 Sha 已有限。

## 6. 剩余障碍成为实际有限增广指数

R107 已证 $E(F^{\rm ab})_{\rm tors}=E[2]$。
因 $[L:F]$ 为奇数，$E(L)[2]=E(F)[2]$；这些点的范数为
$[p]T=T$。故 $\mathcal A(F)$ 无挠。
在 $\mathcal A$ 上 $N_\Gamma=0$，因而
$\mathbb Z[\Gamma]/(N_\Gamma)=\mathbb Z[\zeta_p]$ 作用于它。
由 (4.1)，这个 Mordell–Weil 模在 $\mathbb Z[\zeta_p]$ 上
秩一，$\mathbb Z[\Gamma]Q$ 在其中有有限指数。

取 $\mathcal O_p=\mathbb Z_p[\zeta_p]$，
$\delta=\zeta_p-1$。存在 $\mathcal O_p$-基 $w$ 及一个确定整数
$a\ge0$，使
$$
\mathcal A(F)\otimes\mathbb Z_p=\mathcal O_p w,
\qquad Q=\delta^a\varepsilon w,\quad
\varepsilon\in\mathcal O_p^\times.                 \tag{6.1}
$$
由 R116 的 $Q\notin pE(H)$，$a\le p-2$；主问题需要的是
R104–R106 指定单支撑类的原始性
$$
Q\notin(\sigma-1)\mathcal A(F)\otimes\mathbb Z_p
\quad\Longleftrightarrow\quad a=0.                 \tag{6.2}
$$
完整 Sha 有限性并未证明这个整数等于零。例如实际同源的下降序列仍为
$$
0\longrightarrow\mathcal A(F)/\Delta\mathcal A(F)
\longrightarrow\operatorname{Sel}_\Delta(\mathcal A/F)
\longrightarrow\Sha(\mathcal A/F)[\Delta]
\longrightarrow0,
$$
其中最后一项现在已知有限，但可以非零。
$\mathcal B$ 与 $E\times\mathcal A$ 的自然同源也保留了整个
基域 $E$ 因子，所以不能由 (5.4) 推回 $\Sha(E/F)$ 或
$\Sha(E/\mathbb Q)$ 有限。

## 来源

- J. Nekovář，*The Euler system method for CM points on Shimura curves*，
  收于 *L-functions and Galois representations*，LMS Lecture Note Series
  **320**，Cambridge University Press（2007），471–547；
  Theorem 3.2、§3.1.6、式 (3.5.1)–(3.5.2)，以及 §6.2 的 CM 条件解释。
  [作者原文](https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf)，
  [正式出版 DOI](https://doi.org/10.1017/CBO9780511721267.014)。
  定位页码 19–20 指作者原文自身页码，不与书中页码混用。
- L. Cai、J. Shu、Y. Tian，*Explicit Gross–Zagier and Waldspurger formulae*，
  Algebra & Number Theory **8** (2014)，2523–2572，Theorem 1.1，p.2525；
  [正式发表全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)，
  DOI 10.2140/ant.2014.8.2523。
- 实际域、点与同源：R103、R105、R107、R110、R113、R116。
