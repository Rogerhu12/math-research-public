# R16：局部椭圆单位深度至多三的消失判据

**可信度：已证明。** 对固定曲线
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),
$$
及分裂素数 $p\ge13$、$p\ne17$，本文定义一个可在有限局部除法域中直接计算的椭圆单位深度 $\nu_p$，证明
$$
\nu_p\ge2,
\qquad
\nu_p\le3\ \Longrightarrow\ \Sha(E/\mathbb Q)[p^\infty]=0.
$$
所用椭圆单位取自一条固定有理函数。本文证明其局部单位格生成元及归一化，并给出允许深度三的完整论证；没有证明深度至多三发生于无穷多个 $p$。

## 1. 算术输入及所用单位

固定 $p\mathcal O_K=\mathfrak p\bar{\mathfrak p}$，并从此取具体生成元
$$
\pi_E=\psi(\mathfrak p),\qquad \pi_E\bar\pi_E=p.
$$
它在好约化模型上约化为 $p$ 次 Frobenius。令 $L=K(E[\mathfrak p])$，$G=\operatorname{Gal}(L/K)$，$\chi:G\to\mathbb F_p^\times$ 为挠点作用字符。R12 证明 $G\simeq\mathbb F_p^\times$，且 $L$ 在 $\mathfrak p$ 全分歧。唯一位于 $\mathfrak p$ 上的素点记为 $\mathfrak P$。

R4 给出 $\operatorname{rank}E(\mathbb Q)=2$；R7、R12 给出
$$
c_p:=\dim_{\mathbb F_p}\operatorname{Cl}(L)[p]^\chi\ge1,
\qquad
s_p:=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=2\left\lceil\frac{c_p}{2}\right\rceil,\tag{1.1}
$$
以及 $c_p\le2\Longrightarrow\Sha(E/\mathbb Q)[p^\infty]=0$。

使用固定辅助理想 $(7)$ 的 Rubin 椭圆单位。令 $\mathfrak f=2(1+i)17\mathcal O_K$ 为 Hecke 导子，$S$ 为固定的 $E[\mathfrak f]$ 生成元，$\Delta=64\cdot17^3$，并令 $\Psi_7$ 为首项 $7x^{24}$ 的标准七除法多项式。定义
$$
\Theta(R)=\frac{\Delta^{48}}{\Psi_7(x(R))^{12}},
\qquad
\Lambda(R)=\prod_{\sigma\in\operatorname{Gal}(K(\mathfrak f)/K)}
\Theta(R+S^\sigma).
$$
取 $P_\pi=\xi(\Omega/\pi_E)$，置
$$
\eta_p=\Lambda(P_\pi)
=N_{K(\mathfrak f\mathfrak p)/L}\Theta(S+P_\pi).\tag{1.2}
$$
这是 Rubin Definition 8.1 的首项 $\eta_1^{((7))}(\mathcal O_K)$。$S+P_\pi$ 的精确零化理想为 $\mathfrak f\mathfrak p$，不是素理想幂，所以 $\eta_p$ 是全局单位。详细核对见 `notes/2026-11-12-relative-classgroup-reflection.md` §4.1：该处证明 $K(\mathfrak f\mathfrak p)=K(\mathfrak f)L$、范数群阶为 $256$ 且只取一次范数，并逐一核对 $2,17$ 上的单位性、常数因子与字符方向。

本节固定的是完整的 $\Lambda$，不把裸值 $\Theta(P_\pi)$ 当成 Euler-system 首项。因为 $N(7)-\psi((7))=49-(-7)=56$，辅助理想满足全部所列 $p$ 的单位条件。

## 2. 局部对数的首项与单位格生成元

设
$$
F=L_\mathfrak P,
\qquad \rho=t(P_\pi),\qquad t=-x/y,
$$
并将赋值归一化为 $v_F(\rho)=1$。则 $v_F(p)=p-1$。形式群中
$$
[\pi_E](T)=\pi_ET+\cdots,
\qquad [\pi_E](T)\bmod\mathfrak p=T^p.
$$
将 $\rho$ 代入并除以 $\rho$，保留赋值小于 $p$ 的项，得到
$$
\rho^{p-1}\equiv-\pi_E\pmod{\rho^p},
\qquad
\frac{\rho^{p-1}}p\equiv-\bar\pi_E^{-1}\pmod\rho.\tag{2.1}
$$

对通常的乘法群 $p$-进对数
$$
\log_p(1+\rho)=\sum_{n\ge1}(-1)^{n+1}\frac{\rho^n}{n},
$$
第 $n$ 项的赋值为 $n-(p-1)v_p(n)$。赋值为 $1$ 的项只有 $n=1,p$：若 $p\nmid n$，只有 $n=1$ 可以；若 $v_p(n)=k\ge1$，则该赋值至少为 $p^k-k(p-1)$，在 $k=1$ 时等于 $1$ 仅当 $n=p$，在 $k\ge2$ 时严格大于 $1$。故 (2.1) 给出
$$
\log_p(1+\rho)
\equiv(1-\bar\pi_E^{-1})\rho\pmod{\rho^2}.\tag{2.2}
$$
R7 的非 anomalous 性说明 $p\nmid\#E(\mathbb F_p)$。又
$\#E(\mathbb F_p)=p+1-\pi_E-\bar\pi_E$，故
$\bar\pi_E\not\equiv1\pmod{\mathfrak p}$。所以 (2.2) 的首项非零。

记 $\widetilde\chi$ 为 Teichmüller 提升，并取
$$
e_\chi=\frac1{p-1}\sum_{g\in G}\widetilde\chi(g)^{-1}g.
$$
因为 $g\rho\equiv\chi(g)\rho\pmod{\rho^2}$，该投影保留 (2.2) 的首项。于是
$$
v_F\bigl(e_\chi\log_p(1+\rho)\bigr)=1.\tag{2.3}
$$

定义局部单位格
$$
\mathscr U_p=
\left(\widehat{\mathcal O_F^\times}{}^{\,(p)}\right)^{\widetilde\chi}.
$$
非 anomalous 性还保证 $\mu_p\not\subset F$（Rubin Lemma 10.9）；所以其 pro-$p$ 单位群没有 $p$ 挠，$\log_p$ 在该群上单射。$F/K_\mathfrak p$ 的正则表示中每个字符恰出现一次，故 $F^\chi$ 是一维 $\mathbb Q_p$-空间。

任意 $x\in\rho\mathcal O_F$ 的对数 $\log_p(1+x)$ 都满足 $v_F\ge1$：上面的估值计算只需把 $n$ 换成 $nv_F(x)$，结论仍成立。去掉剩余域 Teichmüller 单位后，这覆盖所有 pro-$p$ 单位。因此 $\log_p(\mathscr U_p)$ 位于 $F^\chi$ 中赋值至少为 $1$ 的格内。由 (2.3)，其中已有一个赋值恰为 $1$ 的元素；一维本征空间中的其他元素与它之比属于 $\mathbb Q_p$，赋值差为 $(p-1)\mathbb Z$。于是
$$
u_p=e_\chi(1+\rho)
$$
为 $\mathscr U_p$ 的 $\mathbb Z_p$ 生成元。这里用加法模记号表示单位群上的 $p$-进指数投影。

这一证明同时核对了其余对数项、首项符号、局部赋值归一化、字符方向和无 $p$ 挠条件，没有预设 $1+\rho$ 的投影为生成元。

## 3. 可直接计算的深度

令 $z_p^{\rm loc}=e_\chi\eta_p\in\mathscr U_p$。由上一节存在唯一 $b_p\in\mathbb Z_p$ 使
$$
z_p^{\rm loc}=b_pu_p.
$$
定义 $\nu_p=v_p(b_p)$，并约定 $v_p(0)=\infty$。具体表达式为
$$
b_p=
\frac{e_\chi\log_p(\eta_p)}{e_\chi\log_p(1+\rho)}
=\frac{\sum_g\widetilde\chi(g)^{-1}\log_p(g\eta_p)}
{\sum_g\widetilde\chi(g)^{-1}\log_p(1+g\rho)}.\tag{3.1}
$$
故当分子非零时，(2.3) 给出精确归一化
$$
\boxed{\displaystyle
\nu_p=\frac{v_F(e_\chi\log_p\eta_p)-1}{p-1}.}\tag{3.2}
$$
分子为零时取 $\nu_p=\infty$。这不是未归一化的对数赋值，也不是原始单位 $\eta_p$ 在整个全局单位群中为 $p^{\nu_p}$ 次幂的断言。

## 4. 全局单位指数与局部化差项

令
$$
\mathscr E_p=
\left((\mathcal O_L^\times/\mu_L)\otimes\mathbb Z_p\right)^{\widetilde\chi},
\qquad z_p=e_\chi\eta_p\in\mathscr E_p.
$$
Dirichlet 单位定理给出 $\mathscr E_p\simeq\mathbb Z_p$。设 $m_p$ 为 $z_p$ 在此格中的 $p$-可除深度，零元素的深度记为无穷。

Rubin 的有限层椭圆单位 Euler-system 指数界（Theorem 9.5 / Corollary 9.6）给出
$$
\#\operatorname{Cl}(L)[p^\infty]^{\widetilde\chi}
\le[\mathscr E_p:\mathbb Z_pz_p]=p^{m_p}
\quad(m_p<\infty).
$$
因此
$$
c_p\le m_p.\tag{4.1}
$$
这里使用的首项正是 (1.2)，无需声称它生成全部椭圆单位格。所比较的是类群的阶；没有把一个阶的等式误用为群同构。

以下只在 $\nu_p<\infty$ 时工作。此时局部化
$\lambda_p:\mathscr E_p\to\mathscr U_p$
非零，是两个自由秩一模之间的单射。设
$$
\lambda_p(\mathscr E_p)=p^{a_p}\mathscr U_p,
\qquad a_p\ge0.
$$
则
$$
\nu_p=m_p+a_p.\tag{4.2}
$$
不需先假设 Leopoldt 型非退化：$\nu_p$ 有限已经保证这个映射非零。

## 5. 零局部化指数的准确影响

若 $a_p=0$，全局单位在 $\mathscr U_p/p\mathscr U_p$ 中的像非零。Rubin Lemma 6.8 的局部下降映射 $\delta_1$ 在 $\chi$ 分量上满射到 $E[\pi]$，所以全局单位的 $\delta_1$ 像填满整个 $E[\pi]$。

Theorem 6.9 及 Corollary 6.10 证明中的 idèle 正合列于是没有局部单位余项：其左项
$$
\mathcal O_F^\times/
\left(\overline{\mathcal O_L^\times}
(\ker\delta_1\cap\mathcal O_F^\times)\right)
$$
为零。右项是类群除以 $\mathfrak P$ 的类生成的子群；而
$\mathfrak P^{p-1}=\mathfrak p\mathcal O_L$
为主理想，所以这一步不改变 $p$-初等部分。故
$$
\operatorname{Sel}_\pi(E/K)
\simeq\operatorname{Hom}_G(\operatorname{Cl}(L),E[\pi]),
\qquad s_p=c_p.\tag{5.1}
$$
R7 已无条件证明 $s_p$ 偶，于是
$$
a_p=0\ \Longrightarrow\ c_p\text{ 为正偶数}.\tag{5.2}
$$
完整的 idèle 列与局部条件说明另见 `notes/2026-11-12-local-elliptic-unit-depth.md` §4。这里只使用 (5.2) 的方向；没有把 $c_p$ 偶反推成 $a_p=0$。

## 6. 结论与证明

**定理。** 对本文的每个 $p$，有 $\nu_p\ge2$，而且
$$
\nu_p\le3\Longrightarrow\Sha(E/\mathbb Q)[p^\infty]=0.
$$

**证明。** $\nu_p=\infty$ 时下界自动成立。以下设其有限。

若 $a_p\ge1$，(4.1)–(4.2) 及 $c_p\ge1$ 给出 $\nu_p\ge2$；当 $\nu_p\le3$ 时，又给出 $c_p\le m_p=\nu_p-a_p\le2$。

若 $a_p=0$，由 (5.2) 知 $c_p$ 为正偶数。因此 $\nu_p=m_p\ge c_p\ge2$；若 $\nu_p\le3$，则 $c_p$ 只能为 $2$。

两种情形均有统一下界，且深度至多三时都有 $c_p\in\{1,2\}$。R7/R12 的 Kummer 判据给出整个 $\Sha[p^\infty]$ 为零。$\square$

按 (3.2)，下界也可写为
$$
v_F(e_\chi\log_p\eta_p)\ge2p-1,
$$
而证明
$$
v_F(e_\chi\log_p\eta_p)\le3p-2
$$
足以证明该 $p$-初等部分为零。

仍待证明的跨素数命题是：上述局部上界对无穷多个分裂 $p$ 成立。本文没有从固定函数、有限次计算或某个固定 $p$ 的 Euler-system 辅助素数无穷性推导这个量词，也没有未经验证就把 $b_p$ 与 CLS 的临界 Hecke 特殊值认作相同。

## 来源

- K. Rubin, *Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[作者讲义全文](https://swc-math.github.io/notes/files/99RubinCM.pdf)：Lemma 6.8、Theorem 6.9、Corollary 6.10；Theorem 7.4、Proposition 7.8、Definition 8.1；Theorem 9.5 / Corollary 9.6；Lemmas 10.4、10.9。
- J. Coates, Z. Liang and R. Sujatha, *The Tate-Shafarevich group for elliptic curves with complex multiplication*，[arXiv:0901.3832](https://arxiv.org/abs/0901.3832)，Lemma 3.2 及 §3 的 $D=17$ 导子数据。
- 本地 R4、R7、R12 及上列两份笔记中的显式曲线、类群与单位比较证明。
