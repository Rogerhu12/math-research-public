# R81：所有虚二次域的三次环类周期在 $M<3p$ 时非零

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明；R80 纤维接口及本文范数论证均完成独立复核。**

令 $K$ 为判别式 $-D$ 的虚二次域，$\mathcal O_c=\mathbb Z+c\mathcal O_K$，
$\eta:\operatorname{Pic}(\mathcal O_c)\to\mu_3$ 为准确阶 $3$、准确导子 $c$
的**原始**环类特征。设
$$p>37,\qquad p\equiv2\pmod3,\qquad p\nmid Dc,\qquad
\left(\frac{-D}{p}\right)=-1,\qquad M=Dc^2.$$
本文证明
$$\boxed{M<3p\quad\Longrightarrow\quad P_\eta\ne0.}\tag{81.1}$$
这里 $P_\eta$ 是 R76、R80 使用的实际 Brandt 类模周期，所用任意固定
最优嵌入 $\mathcal O_c\hookrightarrow R\subset B_{p,\infty}$ 均适用。
因而存在水平 $p$ 的权 $2$ 新形式 $g$，使
$$\boxed{L(1,g,\eta)\ne0.}\tag{81.2}$$
没有 $h_K=1$ 假设，也不依赖虚二次类数 $3$ 的完整分类表。
证明的新部分是用范数 $27$ 的一个代数整数处理 $h_K=3$ 分支。

## 1. 从周期消失降到环类数 $3$

沿用 R80 的纤维结论：在上述 $p$ 与 $M<3p$ 条件下，
$$P_\eta=0\quad\Longrightarrow\quad
h(\mathcal O_c)=3.\tag{81.3}$$
其具体机制必须保留：R76 的相同 $p$ 取向给差范数为 $p$ 的倍数；
三个不同嵌入的边长平方只能为 $(p,2p,2p)$。
四个类若在同一纤维，每组三点恰有一条短边，迫使两条短边为
完美匹配；所得四面体的外接半径平方为 $5p/8$，遂 $M=5p/2$，
与 $M$ 整数、$p$ 奇数矛盾。因此所有纤维至多三个类。

三次特征的纤维系数是 $n_0+n_1\zeta_3+n_2\zeta_3^2$，
其消失等价于 $n_0=n_1=n_2$。所以消失的周期迫使每个非空纤维
恰有三个类。这种三点纤维的左序包含判别式 $-7$ 的最大二次序。
R80 证明这些左序只对应同一个 **Brandt 理想类**；
这里不能把“左序的共轭类唯一”直接当作“理想类唯一”。
于是全部三个类构成一个纤维，得到 (81.3)。

扩张可逆理想给满射
$$\operatorname{Pic}(\mathcal O_c)\twoheadrightarrow
\operatorname{Cl}(\mathcal O_K),$$
故 (81.3) 只留下 $h_K=1$ 或 $h_K=3$。
其中 $h_K=1$ 已由 R80 完整排除；下面处理另一分支。

## 2. 原始性迫使 $c=1$

设 $h_K=3$。此时 $\mathcal O_K^\times=\{\pm1\}$，因为
$\mathbb Q(i)$ 和 $\mathbb Q(\sqrt{-3})$ 的最大序均为类数 $1$。
环类数公式给
$$
\frac{h(\mathcal O_c)}{h_K}
=c\prod_{\ell\mid c}\left(1-\frac{\chi_K(\ell)}\ell\right)
=\prod_{\ell^a\parallel c}\ell^{a-1}
\bigl(\ell-\chi_K(\ell)\bigr).
\tag{81.4}
$$
左边为 $1$。每个因子均为正整数；奇素数的因子至少 $2$，
而素数 $2$ 的因子等于 $1$ 当且仅当 $a=1$ 且 $2$ 在 $K$ 分裂。
因此
$$c=1\quad\text{或}\quad c=2,\ \chi_K(2)=1.\tag{81.5}$$

若 $c=2$，上面的满射是两个三阶群之间的同构，故
$\eta$ 必经 $\operatorname{Cl}(\mathcal O_K)$ 分解。
它作为环类特征的导子因此整除 $1$，违背准确导子 $2$ 的原始性。
于是
$$\boxed{c=1,\qquad M=D.}\tag{81.6}$$
原始性是本步骤的实质条件；本文没有把任意旧特征在较大序上的
拉回都当作准确导子为该序导子的特征。

## 3. $3$ 上方的理想给 $D\le108$

R76 的三点指标条件是
$$7D-16p=n^2\quad\text{对某个 }n\in\mathbb Z_{\ge0}.
\tag{81.7}$$
若 $3$ 在 $K$ 惰性，则 $D\equiv1\pmod3$，而
$p\equiv2\pmod3$ 时 (81.7) 的右边必须模 $3$ 等于 $2$，不可能。
故 $3$ 不惰性。

若 $3$ 分歧，记其上方素理想为 $\mathfrak q$。
由 $\mathfrak q^2=(3)$，其类阶整除 $2$；又整除 $h_K=3$，
故 $\mathfrak q$ 主，存在 $\alpha\in\mathcal O_K$ 满足
$N\alpha=3$。它不可能是实整数，故
$$12-\operatorname{Tr}(\alpha)^2=Df^2\quad(f\ge1),$$
从而 $D\le12$。这与下节由三点几何得到的 $D>84$ 矛盾。

剩下 $3$ 分裂。任取 $N\mathfrak q=3$ 的素理想。
因为类群的阶为 $3$，$\mathfrak q^3=(\alpha)$，其中
$$\alpha\in\mathcal O_K,\qquad N\alpha=27.$$
若 $\alpha$ 为实数，则 $\alpha\in K\cap\mathbb R=\mathbb Q$；
整性给 $\alpha\in\mathbb Z$，其范数为平方，不能等于 $27$。所以 $\alpha$ 非实。
写 $t=\operatorname{Tr}(\alpha)\in\mathbb Z$，有
$$\boxed{108-t^2=Df^2,\qquad f\in\mathbb Z_{\ge1}.}\tag{81.8}$$
这是非实二次整数生成序的判别式公式，$f$ 是
$[\mathcal O_K:\mathbb Z[\alpha]]$。特别地 $D\le108$。

## 4. 只剩 $D=107$，再由同一个指标式排除

由 (81.7) 得
$$D\ge\frac{16p}{7}>\frac{16\cdot37}{7}>84.$$
因此 (81.8) 给 $f^2\le108/D<2$，所以 $f=1$，并且 $|t|\le4$。
全部可能数值是
$$D\in\{108,107,104,99,92\}.\tag{81.9}$$

其中 $-108,-99,-92$ 都不是基本判别式。
$D=104$ 时素数 $2$ 分歧，其素理想的类阶整除 $2$，
也必须整除 $3$，因而主。于是有范数 $2$ 的非实整数，给
$D\le8$，矛盾。故仅可能
$$D=107.$$

再用 $D\ge16p/7$，得到 $37<p\le749/16<47$。
这个区间内满足 $p\equiv2\pmod3$ 的素数只有 $p=41$。
但
$$7\cdot107-16\cdot41=93$$
不是平方数，再次违反 (81.7)。这排除了 $h_K=3$ 分支。
与 R80 的 $h_K=1$ 分支合并，(81.3) 不可能，故 (81.1) 成立。

## 5. 对实际小惯性表示的后果

R76 已逐项验证 Cai–Shu–Tian (2014) Theorem 1.2 的适用条件。
$P_\eta$ 是非零次数零 Brandt 向量，故至少一个权 $2$、水平 $p$
新形式的投影非零；该定理的正系数公式给 (81.2)。

对于 R66 的实际小惯性分支
$$I_p=C^3,\qquad p\equiv2,5\pmod9,$$
$\eta$ 本来就是以准确导子 $c$ 定义的原始三次环类特征。
因此 R69 的实际秩零商和 R72 的尖点形式浸入均可把原来的充分条件
$p>M$ 改为
$$\boxed{M<3p.}\tag{81.10}$$

特别地，若一条相同模 $p$ 表示的椭圆曲线存在非 exceptional
分母素数，则
$$M\ge3p.$$
而 $p\nmid M$ 排除等号，所以事实上 $M>3p$。
这是一条**变化环类导子的必要下界**，不是其上界。
它没有排除 exceptional 素数，也没有处理完整 Cartan 惯性分支，
更不证明 Serre 一致性。

## 6. 来源与依赖

- [R76](R76-three-point-fibres-and-cubic-nonvanishing.md)：
  相同取向的三点几何、$7M-16p$ 平方指标条件，以及实际中心值接口。
- [R80](R80-three-colour-collapse-and-class-number-one-nonvanishing.md)：四点纤维排除、判别式 $-7$ 的唯一 Brandt 类，
  $P_\eta=0\Rightarrow h(\mathcal O_c)=3$，以及 $h_K=1$ 分支。
- L. Cai, J. Shu and Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*,
  Algebra & Number Theory **8** (2014), 2523–2572，
  [期刊全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)，
  Theorem 1.2。这里只用已在 R76 核准的非零性公式。

§2–4 的范数及判别式论证完整列在本文；不以检索所得的类数表
或有限范围搜索代替其完备性证明。
