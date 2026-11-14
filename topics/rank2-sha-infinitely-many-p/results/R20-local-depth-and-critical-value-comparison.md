# R20：局部单位深度与 CLS 临界值的截断赋值完全相同

**可信度：已证明。** 固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),
$$
并设 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$。令 $\nu_p$ 为 R16 定义的局部椭圆单位深度，而
$$
c_p^+(E)=(\Omega_E^+)^{-p}L(\bar\psi^p,p)
$$
为 CLS 使用的代数临界值。则
$$
\boxed{\quad
\min\{\nu_p,4\}=\min\{v_p(c_p^+(E)),4\}.
\quad}\tag{0.1}
$$
特别地，两者小于 $4$ 时取值完全相同。结合 R16，得到
$$
v_p(c_p^+(E))\le3
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.\tag{0.2}
$$
本结果识别了两条已建立的充分判据；尚未证明此条件发生于无穷多个 $p$。

## 1. 固定除法塔、字符及参数

选 $p\mathcal O_K=\mathfrak p\bar{\mathfrak p}$，取
$\pi_E=\psi(\mathfrak p)$，因而 $\pi_E\bar\pi_E=p$。令
$$
K_n=K(E[\mathfrak p^n]),\qquad K_\infty=\bigcup_{n\ge1}K_n.
$$
CM reciprocity 给出挠点作用字符的同构
$$
\rho_E:\operatorname{Gal}(K_\infty/K)
\xrightarrow{\ \sim\ }\mathcal O_{K,\mathfrak p}^{\times}
=\mathbb Z_p^\times.
$$
写此群为 $\Delta\times\Gamma$，其中
$\Delta\simeq\mathbb F_p^\times$、$\Gamma\simeq1+p\mathbb Z_p$。
本文的 $\widetilde\chi$ 正是 $\rho_E|_\Delta$，而
$$
e_\chi=\frac1{p-1}\sum_{\delta\in\Delta}
\widetilde\chi(\delta)^{-1}\delta.
$$
唯一选取满足 $\rho_E(\gamma)=1+p$ 的拓扑生成元 $\gamma\in\Gamma$，并置
$$
\mathcal A=\mathbb Z_p[[\Gamma]]=\mathbb Z_p[[T]],
\qquad T=\gamma-1.\tag{1.1}
$$

由于 $[\pi_E](T)\bmod\mathfrak p=T^p$，相应形式群是参数 $\pi_E$ 的 Lubin–Tate 形式群。每个 $K_n$ 在 $\mathfrak p$ 上全分歧，唯一局部完成记为 $F_n$。于是
$$
\operatorname{Gal}(F_n/\mathbb Q_p)
=\Delta\times\Gamma/\Gamma^{p^{n-1}}
$$
为阿贝尔群，$F_1=K(E[\mathfrak p])_{\mathfrak P}$ 正是 R16 的局部域。

令 $U_n$ 是 $F_n$ 的单位群的 pro-$p$ 完成，并取范数极限
$$
U_\infty=\varprojlim_n U_n.
$$
R16 的 $\mathscr U_p$ 就是 $U_1^\chi$。R7 的统一非异常性及 Rubin Lemma 10.9 给出 $\mu_p\not\subset F_1$。事实上所有 $F_n$ 都不含 $\mu_p$：$F_n/F_1$ 的次数是 $p$ 幂，而 $F_1(\mu_p)/F_1$ 的次数整除 $p-1$。故各层的 pro-$p$ 单位群没有 $p$ 挠。

## 2. 局部范数控制：没有隐藏的有限误差

**引理 1.** 自然的第一层投影给出同构
$$
U_\infty^\chi/TU_\infty^\chi
\xrightarrow{\ \sim\ }U_1^\chi.\tag{2.1}
$$

**证明。** 先看有限层 $F_n/F_1$。局部类域论给出
$$
F_1^\times/N_{F_n/F_1}F_n^\times
\simeq\operatorname{Gal}(F_n/F_1).
$$
$\Delta$ 在右边的共轭作用平凡，因为 $F_n/\mathbb Q_p$ 阿贝尔；而 $\chi$ 非平凡，所以右边没有 $\chi$ 分量。赋值群也是平凡 $\Delta$-模。去掉剩余域的素于 $p$ 阶单位后，便得到范数满射
$$
N_{n,1}:U_n^\chi\twoheadrightarrow U_1^\chi.\tag{2.2}
$$
同理，每个相邻层的 $\chi$ 单位范数均满射，故 $U_\infty^\chi\to U_1^\chi$ 满射。

再看核。Hilbert 90 在循环扩张 $F_n/F_1$ 中给出
$$
\ker N_{n,1}|_{U_n^\chi}=(\gamma-1)U_n^\chi.\tag{2.3}
$$
解释单位限制没有遗漏的修正：若 $x=(\gamma-1)y$，Hilbert 90 起初只给 $y\in F_n^\times$；取 $e_\chi y$ 后，其赋值为零，因为赋值模平凡且 $\chi\ne1$。去掉素于 $p$ 的单位根后即得到 $U_n^\chi$ 中的原像。$\gamma$ 与 $\Delta$ 交换，所以取投影不改变等式。

现取 $x=(x_n)\in U_\infty^\chi$，其第一层分量为零。每个集合
$$
Y_n=\{y_n\in U_n^\chi:(\gamma-1)y_n=x_n\}
$$
由 (2.3) 非空且紧。范数把 $Y_{n+1}$ 映入 $Y_n$；任意有限层列都能从最高层选择一个 $y_N$ 后逐层取范数获得。因此这些紧集的相容条件具有有限交性质，存在相容的 $y=(y_n)$，满足 $x=Ty$。于是第一层投影的核恰为 $TU_\infty^\chi$，证明 (2.1)。$\square$

Rubin Proposition 11.4 给出 $U_\infty^\chi$ 是有限生成、无 $\mathcal A$ 挠、秩一的 $\mathcal A$-模。R16 已证明 $U_1^\chi$ 自由秩一，并明确给出生成元
$$
u_1=e_\chi(1+t(P_\pi)).
$$
由引理 1 提升 $u_1$ 到 $u_\infty\in U_\infty^\chi$。引理 1 与 Nakayama 引理说明 $u_\infty$ 生成整个 $U_\infty^\chi$；无挠及秩一排除生成映射 $\mathcal A\to U_\infty^\chi$ 有非零核。因此
$$
U_\infty^\chi=\mathcal A u_\infty.\tag{2.4}
$$
这一步使用了准确的范数控制；没有单凭“无挠秩一”就断言自由。

## 3. R16 的首项确实生成所需椭圆单位模

令 $C_n$ 为 Rubin §11.2 定义的椭圆单位群的 $p$-进完成，$C_\infty=\varprojlim_n C_n$。固定辅助理想 $\mathfrak a=(7)$，取
$$
\eta_n=\Lambda\!\left(\xi(\Omega/\pi_E^n)\right).
$$
这里 $\Lambda$、固定 $\mathfrak f$-除法点及所有归一化均与 R16 相同。Rubin Proposition 8.2 的范数关系使 $(\eta_n)_n$ 范数相容；其第一层分量恰为 R16 的 $\eta_p$，不是另一项再取范数的单位。

**引理 2.** 有
$$
C_\infty^\chi=\mathcal A\eta_\infty,
\qquad
C_1^\chi=\mathbb Z_p e_\chi\eta_p.\tag{3.1}
$$

**证明。** 对任意其他合格辅助理想 $\mathfrak b$，Rubin Proposition 11.6 的证明给出所有层相容的关系
$$
(\eta_n^{(\mathfrak a)})^{\sigma_{\mathfrak b}-N\mathfrak b}
=(\eta_n^{(\mathfrak b)})^{\sigma_{\mathfrak a}-N\mathfrak a}.
\tag{3.2}
$$
$\mathcal A$ 是局部环，极大理想为 $(p,T)$。在其剩余域中
$$
\sigma_{(7)}-49
\equiv\chi(\sigma_{(7)})-49
\equiv\psi((7))-49
=-7-49=-56\not\equiv0\pmod p.\tag{3.3}
$$
因此 $\sigma_{(7)}-49$ 是整个 $\mathcal A$ 中的单位，(3.2) 表明全部辅助单位均属于 $\mathcal A\eta_\infty$。根单位没有 $p$ 部分。Rubin Proposition 11.6 即给出第一项结论；同一个单位论证在 $\mathbb Z_p[\Gamma/\Gamma^{p^{n-1}}]$ 中成立，特别给出第二项结论。$\square$

用 (2.4) 写
$$
e_\chi\eta_\infty=h_p(T)u_\infty,\qquad h_p(T)\in\mathbb Z_p[[T]].
\tag{3.4}
$$
第一层投影把 $T$ 变成零，并把 $u_\infty$ 变成 R16 所选的 $u_1$，故
$$
e_\chi\eta_p=h_p(0)u_1,
\qquad
\nu_p=v_p(h_p(0)).\tag{3.5}
$$
同时
$$
\operatorname{char}_{\mathcal A}(U_\infty^\chi/C_\infty^\chi)
=(h_p(T)).\tag{3.6}
$$
这里没有把 $C_1$ 替换为全部全局单位；(3.5) 是 R16 原始单位的深度，(3.6) 则是恰由同一范数系统生成的椭圆单位模。

## 4. 临界值对应的参数点及单位因子

Rubin Theorems 12.9–12.10 说明，(3.6) 在完成的最大未分歧整数环 $\mathcal D$ 上有插值生成元 $\mathcal L_E$。若把选定 tame 分支写成 $\mathcal D[[T]]$ 中的级数，则
$$
\mathcal L_E(T)=w_p(T)h_p(T),
\qquad
w_p(T)\in\mathcal D[[T]]^\times.\tag{4.1}
$$
这里 $w_p$ 是单位级数。

本文只使用权 $k=p$ 的插值。由于 $p\equiv1\pmod{p-1}$，$\rho_E^p|_\Delta=\widetilde\chi$，所以它确实位于同一个 tame 分支。由 (1.1)，其 $T$ 坐标恰为
$$
x_p=(1+p)^p-1,\qquad v_p(x_p)=2.\tag{4.2}
$$
Coates–Wiles 的插值定理（Rubin Theorem 12.10；另参 CLS Proposition 2.4 的 (28)）给出所需的单位倍数关系
$$
\mathcal L_E(x_p)=\epsilon_p c_p^+(E),
\qquad\epsilon_p\in\mathcal D^\times.\tag{4.3}
$$

需要的各项单位条件如下。首先
$$
v_p\!\left(\frac{\pi_E^p}{p}\right)=p-1>0,
$$
所以插值中的 Euler 因子 $1-\pi_E^p/p$ 是单位。其次 $p$-进周期 $\Omega_p\in\mathcal D^\times$；对本曲线，周期格为 $\Omega_E^+\mathcal O_K$，已由本题 cm-local-inputs note 核实。因此可选 $\Omega=\Omega_E^+$，或仅相差 $\mathcal O_K^\times$ 中的单位。常见矩归一化中的 $(p-1)!$ 也是单位。最后，$\psi^p$ 的有限导子仍是 $\mathfrak f$，因为其有限字符取值于 $\mu_4$ 且 $p\equiv1\pmod4$；这里没有遗漏因导子下降产生的坏素数 Euler 因子。

具体说，Rubin Theorem 12.10 的印刷插值式不含 $(k-1)!$，CLS Proposition 2.4 的 (28) 则采用含 $(n-1)!$ 的矩归一化。本文只需 $k=n=p$ 的 (4.3)，上述所有归一化因子此时均为单位；不主张两处全权插值式在未进一步换算时完全相同。

单位级数在 $x_p\in p\mathbb Z_p$ 处的值仍是 $\mathcal D$ 的单位，(4.1)–(4.3) 遂给出
$$
v_p(c_p^+(E))=v_p(h_p(x_p)).\tag{4.4}
$$
这说明为何无须把局部 Fourier 对数直接截断成第 $p$ 阶 Taylor 项，也无须猜测未核对的 Gauss 和因子。

## 5. 秩二强迫的是中心点 $T=p$ 的二重因子

令 $X_\infty$ 为 $K_\infty$ 上最大只在 $\mathfrak p$ 分歧的阿贝尔 pro-$p$ 扩张的 Galois 群。Rubin Proposition 11.3 及 Theorem 12.9 给出
$$
X_\infty^\chi\text{ 为有限生成挠 }\mathcal A\text{-模},
\qquad
\operatorname{char}_{\mathcal A}(X_\infty^\chi)=(h_p).
\tag{5.1}
$$
由 Rubin Proposition 12.2，放宽的 $\mathfrak p^\infty$-Selmer 群是
$$
S'_{\mathfrak p^\infty}
=\operatorname{Hom}_{\Gamma}(X_\infty^\chi,E[\mathfrak p^\infty]).
$$
因为 $\gamma$ 在右边目标上的作用为 $\rho_E(\gamma)=1+p$，该群对偶的 $\mathbb Q_p$-维数是
$$
\dim_{\mathbb Q_p}
\left(X_\infty^\chi/(T-p)X_\infty^\chi\right)\otimes\mathbb Q_p.
\tag{5.2}
$$
真正的 Selmer 群包含在 $S'_{\mathfrak p^\infty}$ 中。R4、R7 给出 $E(K)$ 的 $\mathcal O_K$-秩为二，所以 Kummer 子群已经贡献 $(\mathbb Q_p/\mathbb Z_p)^2$，使 (5.2) 至少为二。

把 (5.1) 局部化到高度一素理想 $(T-p)$。在相应离散赋值环上，模的长度不小于模去极大理想后的维数，因此特征理想在 $(T-p)$ 的阶至少为二。这说明
$$
h_p(T)=(T-p)^2 g_p(T),\qquad g_p(T)\in\mathbb Z_p[[T]].
\tag{5.3}
$$
最后的整性也可直接由对首一 distinguished 多项式 $T-p$ 连续作两次 Weierstrass 除法得到。整个论证只使用已知秩下界；没有假设 $\Sha[p^\infty]$ 有限、中心消失阶恰为二或 $p$-进高度非退化。

## 6. 比较只需一条模 $p^2$ 同余

由 (4.2)，$x_p\in p^2\mathbb Z_p$，且 $v_p(x_p-p)=1$。因此 (3.5)、(4.4)、(5.3) 给出
$$
\nu_p=2+v_p(g_p(0)),\qquad
v_p(c_p^+(E))=2+v_p(g_p(x_p)).
\tag{6.1}
$$
由于 $g_p$ 具有整数系数，
$$
g_p(x_p)\equiv g_p(0)\pmod{p^2}.\tag{6.2}
$$
所以两者在截断到 $2$ 的赋值下相同；在 (6.1) 加回 $2$ 即得 (0.1)。零值按赋值无穷处理也不影响此论证。此前 unit-character-nonvanishing note 进一步证明 $\nu_p$ 在所有所列素数处实际有限。

**有限 Selmer 维数的补充界。** R16 的证明实际上给出
$$
\nu_p\ge s_p:=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=2\left\lceil\frac{c_p}{2}\right\rceil.\tag{6.3}
$$
为看清这一点，沿用 R16 的 $c_p\le m_p$ 及 $\nu_p=m_p+a_p$。若 $c_p$ 偶，则 $s_p=c_p\le m_p\le\nu_p$。若 $c_p$ 奇，R16 的 $a_p=0\Rightarrow c_p$ 偶迫使 $a_p\ge1$，故 $\nu_p\ge c_p+1=s_p$。无穷深度时该不等式自动成立，有限深度时上述论证给出完整证明。

特别地，若临界值赋值为 $2$ 或 $3$，R16 的局部深度也是相同的数。(6.3) 及已证的 $s_p$ 为正偶数使 $s_p=2$；Kummer 正合列与秩二、无 $p$ 挠输入给出 $\Sha(E/\mathbb Q)[p]=0$，进而其整个 $p$-初等群为零。这一加强控制的是有限层 Selmer 维数，不仅是 $p^\infty$-Selmer 余秩；它使用了全局/局部单位差项与 Selmer 奇偶性，不能仅由 CLS 原文的“有限”措辞直接读出。

这里没有证明 $g_p(0)$ 或 $g_p(x_p)$ 在无穷多个 $p$ 处不被 $p^2$ 整除。该问题仍是本课题的跨素数缺口。

## 来源与依赖

- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[作者讲义全文](https://swc-math.github.io/notes/files/99RubinCM.pdf)：Corollary 5.20、Proposition 8.2；§11.2、Propositions 11.3–11.6；Proposition 12.2、Theorems 12.9–12.10。本文补写了所需的有限层局部范数控制与自由性证明。
- J. Coates, Z. Liang and R. Sujatha, *The Tate-Shafarevich group for elliptic curves with complex multiplication*，[arXiv:0901.3832](https://arxiv.org/abs/0901.3832)，临界值定义及 Lemma 3.2 的导子输入。
- 本题 R4、R7、R12、R16，及 cm-local-inputs、relative-classgroup-reflection、unit-character-nonvanishing 笔记。
