# 新 fine Selmer／Massey 结果与中心关系：精确层数

**状态：来源适用范围已核；第 2 节的层数命题已证明。** 日期：2026-11-12。
本笔记不提供 $N_p$ 的跨素数上界，不重述旧 Gold／Stokes 审计。

## 1. 新结果的准确输出

Ray–Sujatha 的 *Massey products and the Iwasawa theory of fine Selmer groups*
已于 2026 年 10 月 16 日在 Canadian Journal of Mathematics 在线发表。
本次亲读作者 arXiv:2508.17156v2（2026-09-08）的
§6.2、Corollary 6.11、Theorems 7.1、7.3，并核出版记录。

Theorem 7.1 允许任意连续整 $p$-adic 表示 $\rho$；
在所列分歧／分解假设下，fine Selmer 的 cotorsion 且 $\mu=0$
等价于某一长度的 **proper** Massey 取值张成相应残余 $H^2$。
它没有给出所需长度的统一上界，也没有给出指定高度一中心的核秩。

Theorem 7.3 讨论同一个 $p$ 的两条 $\mathbb Z_p$ 塔；
不能据此跨越不同剩余特征。此外，本题单 $\mathfrak p$ 除法塔
在 $\bar{\mathfrak p}$ 不分歧，直接不满足其所有 $v\mid p$
均全分歧的假设。换用适用的塔，也仍须另付实际中心控制。

基础比较是 Lam–Liu–Sharifi–Wake–Wang (2023)，Theorem 2.2.4
与 Corollary 4.3.3。以下取 $G$ 为 $p$-cohomologically finite、
$\operatorname{cd}_pG=2$，$G\twoheadrightarrow H\simeq\mathbb Z_p$
为连续商，$T$ 为有限连续 $\mathbb F_p[G]$-模；
$I\subset\mathbb F_p[[H]]$ 为增广理想，且 $n\ge1$。
在这些假设下：
$$
 I^nH^2_{\rm Iw}/I^{n+1}H^2_{\rm Iw}
 \simeq
 \frac{H^2(G,T)\otimes I^n/I^{n+1}}
      {\operatorname{im}\Psi^{(n)}}.
\tag{1}
$$
其中 $T$ 可以非平凡，故不能仅以“它只处理平凡特征”排除此框架。
但 (1) 本身没有计算本题真实原始单位的像。

## 2. Proper 系统究竟需要塔的几层

固定 $n\ge1$，令 $N_n$ 为 $(n+1)\times(n+1)$ 的标准上移幂零矩阵，
$N_n^{n+1}=0$、$N_n^n\ne0$。文中的指定系统使用
$$
 M_n(a)=(1+N_n)^a
 =\sum_{j=0}^n\binom ajN_n^j,\qquad a\in\mathbb Z_p.
\tag{2}
$$

**命题。** $M_n(a)\bmod p$ 通过 $\mathbb Z/p^s$ 因子化的最小正整数是
$$
 s=s(n):=\min\{r:p^r>n\}
 =\lceil\log_p(n+1)\rceil.
\tag{3}
$$

**证明。** 在特征 $p$ 下
$$
 (1+N_n)^{p^r}=1+N_n^{p^r}.
$$
因此 $p^r>n$ 时右端为 $1$，而 $p^r\le n$ 时不为 $1$。
连续群同态 $a\mapsto(1+N_n)^a$ 的像遂为阶恰 $p^{s(n)}$
的循环群。这证明结论。$\square$

例如 $n=p$ 时，$a=0,p$ 有同一模 $p$ 值，
但
$$
 \binom0p=0,\qquad \binom pp=1\pmod p.
\tag{4}
$$
故完整 proper 系统已经区别第二层。

由此有一个可直接证明的 **有限证书传播** 版本。固定同一个
残余 $G$-模 $T$。若两个塔的商映射 $\kappa_1,\kappa_2:G\to\mathbb Z_p$
在适当选择生成元后模 $p^{s(n)}$ 相等，则短正合列
$$
0\longrightarrow T\otimes I^n/I^{n+1}
\longrightarrow T\otimes\mathbb F_p[[X]]/(X^{n+1})
\longrightarrow T\otimes\mathbb F_p[[X]]/(X^n)
\longrightarrow0
\tag{5}
$$
中的全部 $G$-作用相同：作用的非平凡因子是
$(1+X)^{\kappa_i(g)}\bmod X^{n+1}$，由 (3) 相同。
因此连接映射 $\Psi^{(n)}$ 也相同。
特别是，一个已存在的长度 $n$ 满射证书可在这个邻域内传播。
如需 Selmer 局部条件，须同时使用同一组局部映射及格。

作者 v2 的 Theorem 7.3 证明以
“残余系数的 Massey 数据只依赖 $\kappa\bmod p$”识别全部长度。
(2)–(4) 说明：对文中指定的 proper 系统，该识别在 $n\ge p$
不能仅凭这一理由推出；需要额外证明，或把层数换成 (3)。
**这里指出的是所用证明步骤的精度问题，不声称构造了该算术定理的反例。**
本课题不使用其统一第一层推论。

## 3. 与本题中心的对接仍须保留真实系数和局部格

本题 $\rho_\pi(\gamma)=1+p$、$\theta=T-p$。
令
$$
 X=\frac{1+T}{1+p}-1=\frac{\theta}{1+p}.
\tag{6}
$$
这只把中心移到增广点；其专门化系数仍带真实 CM 表示，
没有变成平凡 Artin 系数。若
$$
 \rho_\pi(g)=\widetilde\chi(g)(1+p)^{\kappa(g)},
$$
相应中心族的作用准确为
$$
 \rho_\pi(g)(1+X)^{\kappa(g)}.
\tag{7}
$$
原始单位及 strict 局部条件必须一起放入该族。

例如以 $d_\rho$ 表示 $\rho_\pi$ 系数的连续上链微分，
一个拟议的全局一次上链
$c(X)=c_0+c_1X+\cdots+c_nX^n$
是 (7) 下的 cocycle，当且仅当
$$
 d_\rho c_j(g,h)
 =-\rho_\pi(g)\sum_{r=1}^j
   \binom{\kappa(g)}r c_{j-r}(h).
\tag{8}
$$
这是直接展开 cocycle 等式，未使用任何非消失猜想。
对 strict Selmer，还须为各局部限制选择并提升同一套零上链；
只解全局 (8) 不保证局部格条件。

R36 已知 MW 类和全局 Artin 互反只构造了其所写的两条
整泛函 $p^{b_p}\mathcal L/\theta$、$v_w/\theta$。
新文献没有另外构造下一条作用在**完整** $S$-单位格上的
原始行关系。绝对 Galois 群的某个 Massey product 含零，
也不能无证更换本题限制分歧的群、指定 proper 系统
或 strict 局部零上链。

因此此来源的有用新增信息是 (3)–(5) 的实际证书精度，
而不是 $N_p$ 有限或 $G_p(p)\ne0$。O6 接下来仍需新的全局算术输入；
不从这里再展开一条一般 $\mu=0$ 分支。

## 来源

- A. Ray、R. Sujatha，*Massey products and the Iwasawa theory of fine Selmer groups*，
  Canadian Journal of Mathematics，2026，在线 First View，
  [出版 DOI](https://doi.org/10.4153/S0008414X26102478)；
  本次核对的[作者 v2 全文](https://arxiv.org/html/2508.17156v2)，
  §6.2、Corollary 6.11、Theorems 7.1、7.3。
- Y. H. J. Lam、Y. Liu、R. Sharifi、P. Wake、J. Wang，
  *Generalized Bockstein maps and Massey products*，
  Forum of Mathematics, Sigma 11 (2023)，e5，
  [期刊原文](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/generalized-bockstein-maps-and-massey-products/303B92F7CDE917179CC9253AAEBF2A6A)，
  Theorem 2.2.4、§4.2、Corollary 4.3.3、Theorem 6.2.1。
- 本仓库 R34–R36 及
  [第三次整除的真实条件](2026-11-12-bockstein-baker-and-next-integrality-obstruction.md)。
