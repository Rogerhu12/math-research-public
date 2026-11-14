# O5 接续：真实 QC 函数的独立性、饱和格与剩余共同根问题

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

本次任务按根 README 与本课题 README 的完成标准执行，目标仍是排除全部 $p>37$ 的非 CM 非分裂 Cartan 正规化子分支。以下不是完成报告；它记录已证明的局部接口推进和仍需解决的实际共同根问题。git 同步及 HANDOFF 的提交号由主代理统一维护。

## 1. 接续时完整核对的材料与结论

已完整阅读根 README、课题 README、HANDOFF、open，以及本分支指定的七份笔记：

- `2026-11-12-geometric-route.md`；
- `2026-11-12-global-geometry-cont.md`；
- `2026-11-12-global-geometry-followup.md`；
- `2026-11-12-qc-without-cm-basepoints.md`；
- `2026-11-12-quadratic-chabauty-status.md`；
- `2026-11-12-cm-separation.md`；
- `2026-11-12-square-level-norm-derivative-cont.md`。

同时核对 R45、R47 的完整证明及 R28 的坏模型核心论证，按需回查 R14、R18、R33、R43 的规范平移、实际截面和符号接口。

R45 的实际输入不是某个任意 Hecke 空间，而是一个已经同时满足以下条件的整数格 $\mathcal K_A$：对应只支撑于 Heegner 商 $A$、Chow–Heegner 平移在互补商上消失、坏 $p$ 的垂直系数为常数。其秩下界为
$$\operatorname{rk}\mathcal K_A\ge a-n,
\qquad a\gg_\varepsilon p^{3/2-\varepsilon},\qquad n\le(p+13)/12.$$
本次没有发现 R28 用最小正则约化模型取得分量数 $n$ 的矛盾。不能用某个进一步吹起后的非约化正规交叉模型的分量数直接替换它。

R47 的对数同构确实可与 Dogra–Le Fourn 的已发表 Lemma 7 精确匹配：整个 Jacobian 的弱 BSD 假设在 DLF 中用于保证各因子正秩；在按 $L'(f,1)\ne0$ 选取的本题商上，秩一输入已经无条件。原论证先用 $\overline{\mathbb Q}$ 上的 Hecke 特征投影，再调用解析子群定理，不把任意 $\mathbb Q_\ell$ 子空间误当代数子空间。对本题有
$$A(\mathbb Q)\otimes\mathbb Q_\ell\simeq\operatorname{Lie}(A)_{\mathbb Q_\ell}.$$
它保证局部闭包有限指数，不保证整数指数为一，也不要求高度配对非退化。

实际方程继续使用 R47 的同一 Poincaré splitting：对 $F\in\mathcal K_A$ 只取一次 $G=2F$，
$$\Psi_G(x)=\sum_f\operatorname{Tr}\bigl(c_fz_f(x)(G_fz_f(x)-\xi_{G,f})\bigr)-H_{D,G,\ell}(x).$$
每个有理点满足 $\Psi_G(x)=0$。$z_f$ 来自实际 $u_D=[dx-D]$，因此微分已经含 $d=(p-1)/2$；式外不能再乘一次 $d^2$。辅助局部项保留全部迭代积分。坏素数高度为常数并不让这个辅助局部项消失。

## 2. 首个实质修正：统一整数指数不是共同根定理的逻辑前置条件

旧检查点同时列出整数指数、对数分母、Hecke 投影分母、单位 jet 和共同根排除。它们在某些固定整坐标算法中都重要，但不是一组必须逐个先解决的逻辑依赖。

新结果 [R48](../results/R48-analytic-saturation-and-root-certificates.md) 给出完整初等证明。固定一个闭解析圆盘，把实际缺陷函数张成的有限维空间写为
$$V\subset\mathbb Q_\ell\langle T\rangle,\qquad
\Lambda(V)=V\cap\mathbb Z_\ell\langle T\rangle.$$
则 $\Lambda(V)$ 是秩 $\dim V$ 的自由格，而且
$$\Lambda(V)/\ell\Lambda(V)\hookrightarrow\mathbb F_\ell[T]$$
单射。它与任何原始满格具有相同的 $\mathbb Q_\ell$ 线性包和完全相同的共同零点。这个构造既不要求改变辅助素数，也不要求原 Hecke 格或 Mordell–Weil 对数格具有统一指数。

因此，若一个共同根排除论证真正只依赖特征零的实际方程，可以在这个格上开展；没必要把统一小指数添加为新的先验猜想。另一方面，饱和不是计算精度的免费替换。若 $m=\dim V>0$，饱和约化空间的最大次数满足
$$d(V)\ge m-1.$$
若所有函数在一个精确共同根处至少消失 $e$ 阶，则
$$d(V)\ge m+e-1.$$
例如 $T^2$ 和 $T^2+\ell^M T^N$ 的原约化都为二次，但饱和后第二方向为 $T^N$，$N$ 可以任意大。

R48 也给出固定水平无根性的有限精度证书：一组整限制幂级数在 $\mathbb Z_\ell$ 无共同根，当且仅当某个有限模 $\ell^N$ 已无共同解。证明只用紧性。这个 $N$ 不统一；$T^2-\ell^{2M+1}$ 给低次数也需任意高精度的直接例子。这里只改善逻辑接口，不声称已有数据足以找出统一的认证精度。

## 3. 已发表定理真正控制的是完整局部高度

本次核查了 Besser–Müller–Srinivasan 的已发表论文 **$p$-adic adelic metrics and quadratic Chabauty I**，*Crelle* **828** (2025), 223–305，特别是 Theorem 7.9 与 Lemma 7.12。作者最终版的这两项位于 pp.51–53。Theorem 7.9 对 NS 核的一组独立有理类给出其局部高度与全部全纯积分在 $\mathbb Q_\ell$ 上的代数独立性。其证明不依赖完整 Jacobian 的 rank=genus；该秩条件用于构造全局关系，不能反向添加到局部独立性定理上。

这里不能只说“R45 的方向独立，所以高度独立”。[R49](../results/R49-independent-qc-functions-and-saturated-degree.md) 完整补上了三个接口。

### 3.1 实际方向对应的 NS 类，以及模极化后的独立性

在待排除的非空有理点分支中，临时取 $b\in X(\mathbb Q)$ 作证明基点；不要求事先知道它，也不要求它是 CM。记
$$e=[db-D],\quad u_D=dj_b+e,\quad\alpha f_i=G_i.$$
实际 Poincaré 拉回来自 $J$ 上的有理线丛
$$\mathcal N_i=\beta_i^*\mathcal P,\qquad
\beta_i(t)=(dt+e,f_i(dt+e)-\alpha^{-1}\eta_i).$$
其沿 $j_b$ 的拉回正是 R47 的实际有理平凡线丛，而
$$\phi_{\mathcal N_i}=2d^2f_i.$$
因此独立 Hecke 方向给独立 NS 类。若其某个组合等于极化类的倍数，拉回曲线后左边次数为零、极化次数严格为正，故倍数必须为零；所以在 $\operatorname{NS}(J)/\mathbb Q[\Theta]$ 中仍独立。

### 3.2 不是仅有理系数独立，而是 $\mathbb Q_\ell$ 系数独立

BMS Lemma 7.12 把二阶符号 $D_2h_i$ 模全纯张量后的像送到
$$c_1(\mathcal N_i)\in H^2_{\rm dR}(J)/F^2.$$
NS 的有理 Chern 类与 $F^2$ 的交为零：复比较下前者为 $(1,1)$ 型，后者为 $(2,0)$ 型。全部数据定义于 $\mathbb Q$，先得到有理线性映射的单射，再张量 $\mathbb Q_\ell$。所以任意 $\mathbb Q_\ell$ 线性组合都不能消去这一曲率部分，不能只排除有理组合。

### 3.3 匹配真实局部高度，而非任意二阶模型

将 $\mathcal N_i$ 的 Poincaré 拉回按双扩张律展开：一个对称线丛的 $d^2$ 次幂、两个 $\operatorname{Pic}^0$ 因子，以及一个常数线。BMS Proposition 4.30、Lemma 4.31、Propositions 4.32、4.35、Definition 4.39、Lemma 4.41 保证相应规范局部对数的张量相容性。对称因子的 $\phi=2f_i$ 精确抵消 Definition 4.39 的 $1/2$。

因此 R47 的真实 $H_{D,G_i,\ell}$ 与 BMS 的局部高度只差基点或刚性化常数。更一般的同曲率选择只多一次全纯积分和常数，仍可并入全局多项式。这个比较直接在局部 Poincaré 线上完成，未从“全局高度相等”擅自推出逐个局部项相等；BMS Remark 6.17 已明确指出后者通常需要另证。

设 $L_1,\ldots,L_g$ 为全部全纯积分，便有
$$\Psi_i=P_i(L_1,\ldots,L_g)-h_i,\qquad\deg P_i\le2.$$
变量替换 $Y_i\mapsto P_i(X)-Y_i$ 是多项式自同构，所以 BMS 的代数独立性立即传递到真实 $\Psi_i$。恒等原理保证在每个非空圆盘上也成立。这不需要 $c_f\ne0$，更不需要假设全局高度非退化。

## 4. 可量化的结果：保留全部秩就必然付出约化次数增长

R49 现在给出真正完整的函数维数
$$\dim_{\mathbb Q_\ell}\langle\Psi_1,\ldots,\Psi_m\rangle=m.$$
结合 R45 与 R48，
$$d(V)\ge m-1\ge a-n-1\gg_\varepsilon p^{3/2-\varepsilon}.$$
在包含已知共同根的圆盘上有更强的 $d(V)\ge m$。所以把整个高秩方程组本原化后，模辅助素数的次数不可能一直为二次，甚至不可能被任何绝对常数统一限制。

这不是有理点个数的下界，也不是说全部原始方程都需要这么高次展开；它精确约束“全部方向保持模 $\ell$ 独立”这一目标。只保留一个或少数方向求根时没有这个维数下界，但也失去用大量独立条件交叉排根的即时优势。

同样，固定 $r$ 阶 jet 在 $m$ 维函数空间上的核维数至少为 $m-r-1$；在共同根处至少为 $m-r$。所以即使特征零函数完全独立，也不能声称某个固定低阶 jet 矩阵自动满秩。这里的零化组合允许 $\mathbb Q_\ell$ 系数，不把它们冒充有理 Hecke 对应。

## 5. 另一项确切排查：改变 Hodge splitting 不产生新方程

R49 命题 2A 给出一个与继续排根直接相关的事实。固定实际方向、字符和 R47 的归一化截面，若同时用另一个 Hecke 相容的 Hodge 补空间计算全局及局部高度，则
$$\Psi_G^{W'}(x)=\Psi_G^W(x).$$

证明不依赖高度非退化。两个 Poincaré splitting 之差下降为局部点群上的连续双加性函数，故唯一通过阿贝尔对数因子化为 Lie 代数上的双线性形式。Hecke 相容性使 $A$ 与互补商正交。全局高度变化在有理点上恰等于这一辅助局部变化；R47 的对数同构使等式延拓到 $A$ 的全部 Lie 代数，所以缺陷中的两项精确抵消。

因此可以选更好算的 splitting，但不能把不同 splitting 所得式子当作更多独立根条件。不同辅助素数之间的全局相容性不在此命题范围内，仍可另行研究。

## 6. 2026 equationless 文献的准确作用

核对 Hashimoto–Lido–Lombardo–Mascot–Parent 的 [arXiv:2608.10919v1](https://arxiv.org/html/2608.10919v1)。目前它完整处理的是 $p=13$；Remark 3.0.7 对一般 torsor 的 rank 条件作说明，Theorem 4.4.6 仍需完整 Jacobian 的 rank=genus 和其式 (4.4.1) 的整数满射输入。不能将其直接当成所有一般层的现成算法定理。

Corollary 4.3.11 的模辅助素数二次约化在特定积分坐标中成立。R48–R49 解释为什么它不能在任意饱和除法之后继续原样引用：被原格掩盖的高阶项会成为单位项，若保留 R45 的全部函数秩则这种次数增长是必然的。本文的证明没有使用这份预印本的新定理；只用它检查原有“低精度二次”策略的适用边界。

## 7. 继续推进：谱缺陷的线性包条件可以恢复为有限靶集条件

接着把积分核放回全部 trace-zero Heegner 商方向，得到完整新结果 [R54](../results/R54-hecke-spectral-defect-and-finite-target.md)。这一步保留实际全局高度、辅助迭代积分和全部坏纤维范数缺陷。

令 $T_A=\prod_fK_f$，$W=\ker\operatorname{Tr}_{T_A/\mathbb Q}$，维数为 $a-1$。选参考坏分量 $i_0$，将完整垂直阶差
$$b_i(F)=k_i(F)-k_{i_0}(F)$$
用非退化迹配对写为 $b_i(F)=\operatorname{Tr}(F\beta_i)$，其中 $\beta_i\in W$。它们给出有理坏纤维谱向量，且
$$C=\operatorname{span}_{\mathbb Q}\{\beta_i\}
=(\mathcal K_A\otimes\mathbb Q)^\perp,\qquad\dim C\le n-1.$$

对整个 $W$ 的真实高度方程，按参考分量统一归一化实际有理截面，得到唯一谱缺陷 $\Delta_\ell(x)\in W\otimes\mathbb Q_\ell$。其完整公式为
$$\Delta_\ell(x)=2\pi_0(cz(x)^2)-\Xi_0^*(cz(x))-\mathbf H_\ell(x).$$
这里 $\pi_0$ 为 trace-zero 投影，$\Xi(F)=\xi_{2F}$ 是规范平移在秩一坐标中的线性映射，星号表示迹伴随，$\mathbf H_\ell$ 保留全部实际辅助高度。

现在有两个严格不同的条件：
$$\begin{aligned}
\text{积分核全部方程成立}&\iff\Delta_\ell(x)\in C\otimes\mathbb Q_\ell,\\
x\in X(\mathbb Q)&\implies\Delta_\ell(x)=-\log_\ell(p)\beta_i
\text{，某个坏 }p\text{ 实际可达分量 }i.
\end{aligned}$$
后一条件把线性空间收缩为至多 $n$ 个确定靶向量。恢复它只需在积分核外补上 $r=\operatorname{rank}\Phi_A\le n-1$ 个方向，并保留**同一分量决定的联合有限集**。逐条方程任意拼接分支会再次丢失这项信息。

换参考分量使谱缺陷与靶集同时平移，集合不变。相容 Hodge splitting 不变性也延伸到整个 $W$，因此 R54 的矢量不是坐标选择制造的条件。$\log_\ell(p)\ne0$，所以可把整个矢量除以它，使靶集本身为有理向量；不需要单位性假设。

这个加强尚不能证明有限靶集逆像只有 CM 点；但它明确恢复了取核时丢掉的真实离散约束，为继续共同根排除提供了比“落在低维空间”更精确的对象。

## 8. 当前不能越过的结论，以及继续工作的实际对象

代数独立并不指定共同根的位置。对任意代数独立的解析函数 $h_i$ 和任意 $c$，全部 $h_i(T)-h_i(c)$ 仍代数独立，却在 $c$ 具有共同根。这说明，即使独立条件数随层增长，也不能只按维数把一个未知非 CM 共同根排除。BMS §7.3 对多个方向的共同根通常等于有理点只作期望陈述，没有提供全层排除定理。

本次严格推进是：真实函数独立性已落实；整数格指数不再被错误地列为逻辑必需前提；饱和所付出的次数代价和 splitting 的精确不变性已经证明；全部实际方向的谱缺陷与坏纤维有限靶集已经准确连接。没有得到含 CM 圆盘的唯一根定理，也没有得到无 CM 圆盘的无根定理。O5 仍须对这些实际函数的公共零点给出算术来源，或结合跨素数及全局 Galois 条件排除非 CM 有理点。现有接口允许直接针对这个问题工作，不必先添加一个尚未证明且未必必需的统一指数猜想。

## 核验来源

- Besser–Müller–Srinivasan，*p-adic adelic metrics and quadratic Chabauty I*，DOI [10.1515/crelle-2025-0063](https://doi.org/10.1515/crelle-2025-0063)；[最终版元数据](https://arxiv.org/abs/2112.03873v4)，[作者全文](https://padmask.github.io/QuadraticChabauty.pdf)。本次实际核对 Theorem 7.9、Lemma 7.12 的完整证明，及上述 §4、§6、§7.3 的相容性与计算说明。
- Dogra–Le Fourn，*Quadratic Chabauty for modular curves and modular forms of rank one*，*Math. Ann.* **380** (2021), 393–448，[期刊全文](https://link.springer.com/article/10.1007/s00208-020-02112-3)。Lemma 7 和 Corollary 1 用于复核 R47，不扩大其已发表结论的范围。
- Hashimoto–Lido–Lombardo–Mascot–Parent，*Equationless quadratic Chabauty for non-split Cartan modular curves*，[arXiv:2608.10919v1](https://arxiv.org/html/2608.10919v1)。仅作算法范围对照。

全文证明在 R48、R49、R54；这份 note 不另给它们重复编号。主代理可以据此更新 O5 和 HANDOFF，但不能据本次结果将本课题标记完成。
