# 任意水平的实际 GL2 型商：中心一阶非消失、秩与对数接口

日期：2026-11-14。恢复状态：`reconstructed-after-environment-reset`。这是 R596、R598、R600 使用的共同证明接口；不另占研究编号。原缓存字节已丢失，本稿重新校验哈希。

## 1. 精确命题

设 \(f\) 为权二、平凡 nebentypus 的正规化 newform，水平 \(N\) 任意，允许偶水平及 CM。设 \(F\) 为其全实系数域，\(A_f/\mathbb Q\) 是相应的 \(\mathbb Q\)-单 GL2 型阿贝尔簇，\(g=[F:\mathbb Q]=\dim A_f\)。假设

\[
 \epsilon(f)=-1,\qquad L'(f,1)\ne0.
\tag{G.1}
\]

则

\[
 \operatorname{rank} A_f(\mathbb Q)=g,
\tag{G.2}
\]

并且对任意素数 \(\ell\)，实际 \(\ell\) 进阿贝尔对数给同构

\[
 A_f(\mathbb Q)\otimes_{\mathbb Z}\mathbb Q_\ell
 \xrightarrow{\ \log_\ell\ }
 \operatorname{Lie}(A_f)(\mathbb Q_\ell).
\tag{G.3}
\]

此外，\(f\) 的每个系数域嵌入 \(\sigma:F\hookrightarrow\mathbb R\) 都满足 \(L'(f^\sigma,1)\ne0\)。这一断言来自同一个非挠 Heegner 点在每个实分量的正高度，不把超越的 \(L'\) 值视作代数 Galois 共轭。

另有正根号版本：若 \(\epsilon(f)=+1\) 且 \(L(f,1)\ne0\)，则

\[
 \operatorname{rank} A_f(\mathbb Q)=0.
\tag{G.4}
\]

## 2. BFH 的量词及辅助域的选择

使用 Bump–Friedberg–Hoffstein，*Nonvanishing theorems for L-functions of modular forms and their derivatives*，Inventiones Mathematicae **102** (1990)，543–618，Introduction 无编号 Theorem，原印刷页 543–544。

<https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf>

其 Theorem (ii) 对任意包含水平素因子的有限素数集 \(S\) 给出满足规定分裂条件的基本判别式 \(\Delta\)，使 \(\epsilon(f)\Delta>0\) 且中心扭曲值非零。在 (G.1) 下 \(\Delta<0\)，因此

\[
 K_{\rm aux}=\mathbb Q(\sqrt\Delta)
\]

是虚二次域，\(N\) 的所有素因子在其中分裂，且

\[
 L(f\otimes\chi_\Delta,1)\ne0.
\tag{G.5}
\]

这里使用的是“对任意有限 \(S\) 存在满足条件的 \(\Delta\)”这个量词。若需要无限多个辅助域，可依次扩大 \(S\)：对此前得到的每个二次域选择一个在其中惰性、避开现有有限集合的素数，加入 \(S\)。新域要求这些素数全部分裂，因而与此前每个域不同。这给严格的无限性推论；无需把无限性误写成该无编号定理的字面措辞。

若 \(f\) 具有某个虚二次域 \(K_0\) 的 CM，预先将一个在 \(K_0\) 惰性的素数加入 \(S\)，即可保证 \(K_{\rm aux}\ne K_0\)。本题 \(K_0=\mathbb Q(\sqrt{-3})\) 且 \(3\mid N\)，要求 3 在 \(K_{\rm aux}\) 分裂已足以区分两域；上面的有限集合论证同时说明一般情形。

正根号版本使用同一 Introduction 的 **Theorem (i)**：要求 \(\epsilon(f)\Delta<0\)，并得到中心一阶导数非零的二次扭曲。对 \(\epsilon(f)=+1\) 仍可选负 \(\Delta\)，所有 \(S\) 中素数分裂，且

\[
 L'(f\otimes\chi_\Delta,1)\ne0.
\tag{G.6}
\]

不可把正根号版本的输入误写为 Theorem (ii)。

## 3. Heegner 点、CM 假设与任意偶水平

全部水平素数分裂，故可选 \(\mathcal O_{K_{\rm aux}}\) 的理想 \(\mathfrak N\)，使

\[
 \operatorname{Norm}(\mathfrak N)=N,
 \qquad \mathcal O_{K_{\rm aux}}/\mathfrak N\simeq\mathbb Z/N\mathbb Z.
\]

普通 split-Heegner 情形的 Gross–Zagier 公式，对应到 \(A_f\) 的完整理想类迹 \(P\)，给

\[
 L'(f,1)L(f\otimes\chi_\Delta,1)\ne0
 \quad\Longrightarrow\quad P\text{ 非挠}.
\tag{G.7}
\]

一个覆盖此任意水平情形的主来源是 Cai–Shu–Tian，*Explicit Gross–Zagier and Waldspurger formulae*，Theorem 1.1：

<https://arxiv.org/pdf/1408.1733>

随后使用 Nekovář，*The Euler system method for CM points on Shimura curves*，Theorem 3.2，取该文 \(\alpha=1\)。作者稿：

<https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf>

其定理中的 \(K(\alpha)=K_{\rm aux}\)。相关 CM 排除条件不是禁止一切 CM newform，而是禁止在该定理指定的二次域中取得相应 CM；结合该文 §3.4，\(K_{\rm aux}\ne K_0\) 已避开本题的障碍。因此

\[
 A_f(K_{\rm aux})\otimes\mathbb Q=F\cdot P,
 \qquad\operatorname{rank}A_f(K_{\rm aux})=g.
\tag{G.8}
\]

这里只使用普通 split-Heegner 公式，没有把需满足局部条件的任意环面角色公式不加核对地代入。

## 4. 从辅助域下降到 \(\mathbb Q\)

这一段直接处理任意 \(N\)，不依赖只在奇水平表述的后续命题。用 \((\mathfrak a,\mathfrak N)\) 表示理想类轨道中的 CM 点。复共轭把它送到 \((\overline{\mathfrak a},\overline{\mathfrak N})\)，Fricke 对合 \(W_N\) 则把它送到 \((\mathfrak a\mathfrak N^{-1},\overline{\mathfrak N})\)。对所有理想类取迹，两个集合相同。

若 Abel 基点为 \(\infty\)，两边的基点差是 \(h_K([0]-[\infty])\)，由尖点差的挠性在 \(A_f\otimes\mathbb Q\) 中为零。故

\[
 \overline P=W_NP=-\epsilon(f)P
 \quad\text{于 }A_f(K_{\rm aux})\otimes\mathbb Q.
\tag{G.9}
\]

这里 \(W_Nf=-\epsilon(f)f\) 是权二、平凡 nebentypus 的符号规范。上述理想类公式与 Derickx–Le Fourn 的 Appendix 式 (49)–(50) 一致；该文 Prop. 8 额外写了奇水平，故本稿不把该命题直接扩用到偶水平，而采用上面的独立理想类论证。

<https://link.springer.com/article/10.1007/s00208-020-02112-3>

当 \(\epsilon(f)=-1\)，\(P\) 的某个非零整数倍是有理点，由 (G.8) 得 (G.2)。当 \(\epsilon(f)=+1\)，改用 (G.6) 和 \(L(f,1)\ne0\) 使同一基变换导数非零，(G.8) 仍成立，但整个 \(F\)-直线在复共轭下反不变。因此其有理不变部分为零，得到 (G.4)。

## 5. 所有实嵌入及实际对数

固定由 (G.8) 得到的非挠 \(P\)。在每个实嵌入 \(\sigma\) 下，\(F\cdot P\) 的 \(\sigma\) 分量非零，Néron–Tate 配对的正定性给该分量严格正的高度。对同一个 \(P\) 分量应用 Gross–Zagier，便有

\[
 L'(f^\sigma,1)L(f^\sigma\otimes\chi_\Delta,1)\ne0.
\tag{G.10}
\]

这证明所有共轭的一阶非消失。

现在取实际 \(\ell\) 进阿贝尔对数。源、靶都具有维数 \(g\)，并且 \(F\otimes\mathbb Q_\ell\) 的作用在源、靶中均为秩一。若 (G.3) 不满秩，则在 \(\overline{\mathbb Q}_\ell\) 中至少一个 \(F\) 特征分量为零；相应代数不变微分 \(\omega\ne0\) 满足 \(\omega(\log_\ell P)=0\)。

\(P\) 非挠，所以 \(\log_\ell P\ne0\)。\(\ell\) 进解析子群定理把此代数线性关系提升为一个真代数子群，其切空间位于 \(\ker\omega\)，且包含 \(P\) 的非零整数倍。对其有限个 Galois 共轭取交并清除连通分支的有限指数，得到定义在 \(\mathbb Q\) 上、仍包含 \(P\) 某个非零倍数的正维真阿贝尔子簇，矛盾于 \(A_f\) 的 \(\mathbb Q\)-单性。因此 (G.3) 是同构。

这个论证不要求 \(\ell\) 处 ordinary，也不预先假设某个 \(\ell\) 进调节子非零。对数是阿贝尔簇实际的局部解析对数；清除有限分支群后定义于恒等分支即可。

## 6. 使用边界

本接口把已经证明的一阶中心非消失转成同一个实际因子的秩与对数结论。它不提供中心值或导数本身的非消失，也不把任意辅助的 \(\xi_1,\xi_3\) 或反向 \(\kappa_4^{-1}\) 家族替换成真实 \(\Psi\theta\kappa_4\kappa_d^{-1}\) 家族。秩等于维数不是有理点零像结论；二次高度法还需实际高度关系、同一商和局部展开。
