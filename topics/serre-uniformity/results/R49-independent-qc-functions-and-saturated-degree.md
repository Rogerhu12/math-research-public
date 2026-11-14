# R49. 真实 QC 函数的代数独立性与饱和后的次数下界

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 本文把 Besser–Müller–Srinivasan 的已发表代数独立性定理用于 R45–R47 的实际 Poincaré 构造。这里独立的是**包含完整辅助局部高度的真实 QC 函数**，不是单独的 Hecke 二次微分。

设 $X=X_{\rm ns}^+(p)$，$J=\operatorname{Jac}(X)$，并在 R45 的积分核 $\mathcal K_A$ 中取 $m$ 个 $\mathbb Q$ 线性独立方向 $F_1,\ldots,F_m$。令 $G_i=2F_i$，按 R47 的张量相容方式选择归一化截面，记对应缺陷函数为
$$
\Psi_i(x)=
\sum_f\operatorname{Tr}\bigl(c_fz_f(x)(G_{i,f}z_f(x)-\xi_{i,f})\bigr)
-H_{D,G_i,\ell}(x),
\qquad \ell\ne p.
\tag{0.1}
$$

在需要排除的分支 $X(\mathbb Q)\ne\varnothing$ 中，本文证明：

1. 在每个非空辅助剩余圆盘上，$\Psi_1,\ldots,\Psi_m$ 在 $\mathbb Q_\ell$ 上代数独立；连同一组全纯微分的全部 $g$ 个积分，仍代数独立。
2. 特别地，方向到真实解析函数的映射是 $\mathbb Q_\ell$ 线性单射，而非仅在有理系数下单射。不需要假设全局高度配对非退化。
3. 在任何使这些函数成为限制幂级数的闭解析子圆盘上，R48 的饱和约化空间维数恰为 $m$，最大次数至少为 $m-1$；若圆盘含一个共同精确零点，则至少为 $m$。
4. 因 R45 可取 $m\ge a-n\gg_\varepsilon p^{3/2-\varepsilon}$，全部独立方程饱和之后的约化次数不可能随 $p$ 一直有界，更不可能全部保持至多二次。
5. 对固定的实际方向和归一化截面，改变 Hecke 相容的 Hodge 补空间，完整缺陷函数不变；全局与辅助局部项的变化精确相消。

若 $X(\mathbb Q)=\varnothing$，该水平的目标已经成立；本文只在非空分支选择一个有理点作**证明中的**辅助基点，不假定它事先已知，也不假定它为 CM。构造与结论中的函数始终使用原来的有理尖点除子 $D$。

上述独立性是已发表一般定理的适用性推论。它不把共同零点识别为 CM，也不证明 Serre 一致性。

## 1. 从每个真实方向得到一个实际有理线丛

固定 $b\in X(\mathbb Q)$，只用于本节证明。记
$$
j_b(x)=[x-b],\qquad e=[db-D],\qquad u_D=dj_b+e,
\qquad d=\deg D=(p-1)/2.
\tag{1.1}
$$
沿用 R47 的自对偶识别 $\alpha:J^\vee\to J$。对应 $G_i$ 的实际对称同态记为
$$f_i:J\longrightarrow J^\vee,\qquad \alpha f_i=G_i,$$
并置 $\eta_i=\eta_{D,G_i}\in J(\mathbb Q)$。定义 $J$ 上的线丛
$$
\mathcal N_i=\beta_i^*\mathcal P,\qquad
\beta_i(t)=(dt+e,\ f_i(dt+e)-\alpha^{-1}\eta_i).
\tag{1.2}
$$
全部映射和线丛都定义在 $\mathbb Q$ 上，且
$$
j_b^*\mathcal N_i
=(u_D,\,f_iu_D-\alpha^{-1}\eta_i)^*\mathcal P
=L_{D,G_i}\simeq\mathcal O_X.
\tag{1.3}
$$
这是 R14、R18 和 R47 的**实际有理平凡化**，不只是几何 Picard 类为零。

令
$$\mathcal B_i=(\operatorname{id},f_i)^*\mathcal P.$$
Poincaré 双扩张公式给
$$\phi_{\mathcal B_i}=f_i+f_i^\vee=2f_i,$$
其中 $\phi_L(t)=t_t^*L\otimes L^{-1}$ 是线丛到对偶阿贝尔簇的同态。平移只改变代数等价类中的 $\operatorname{Pic}^0$ 部分，而 $[d]^*$ 在 Néron–Severi 群上乘以 $d^2$。因此
$$
[\mathcal N_i]=d^2[\mathcal B_i],\qquad
\phi_{\mathcal N_i}=2d^2 f_i.
\tag{1.4}
$$

### 引理 1

$[\mathcal N_1],\ldots,[\mathcal N_m]$ 在
$$V'=\ker\bigl(j_b^*:\operatorname{NS}(J)_{\mathbb Q}\longrightarrow\operatorname{NS}(X)_{\mathbb Q}\bigr)$$
中线性独立；它们模极化类后仍独立。

**证明。** 属于 $V'$ 来自 (1.3)。$L\mapsto\phi_L$ 在 $\operatorname{NS}(J)_{\mathbb Q}$ 上单射，其核正是 $\operatorname{Pic}^0$。若 $\sum_i r_i[\mathcal N_i]=0$，由 (1.4) 得
$$2d^2\sum_i r_if_i=0,$$
故 $\sum_i r_iG_i=0$，进而全部 $r_i=0$。

若一线性组合等于一个极化类的有理倍数，拉回 $X$ 后左侧次数为零，极化拉回次数严格为正，故该倍数为零，再用已证独立性。等价地，在 R45 的自对偶约定下，极化方向对应非零标量，trace-zero 子空间与该直线交为零。证毕。

这一证明不把“独立 Hecke 对应”直接等同于“独立 NS 类”；它写出了连接两者的同态 (1.4)。

## 2. 辅助局部高度确实是这些线丛的规范局部高度

固定 R47 中与 Hecke 相容的 Hodge 补空间，使用它给出的同一个圆分 Poincaré splitting。Besser–Müller–Srinivasan（下称 BMS）Proposition 6.13 把该补空间对应到 Poincaré 线丛的 purely mixed curvature；Proposition 4.30 给相容的规范对数。其 Coleman–Gross/Mazur–Tate 比较见 §6，特别 Theorem 6.10。这里采用 R47 自己统一使用的 Poincaré 符号；不将某个单独局部项换号。

为避免只靠“高度都相同”的笼统说法，直接分解 (1.2)。记
$$q_i=f_ie-\alpha^{-1}\eta_i.$$
双扩张律给出
$$
\mathcal N_i\simeq
\mathcal B_i^{\otimes d^2}
\otimes\bigl((t\mapsto(t,q_i))^*\mathcal P\bigr)^{\otimes d}
\otimes\bigl((t\mapsto(e,f_it))^*\mathcal P\bigr)^{\otimes d}
\otimes\mathcal P_{e,q_i}.
\tag{2.1}
$$
后三项中前两项属于 $\operatorname{Pic}^0(J)$，最后一项是常数线。

规范对数与这些张量分解相容：对称的 $\mathcal B_i$ 来自对称 Poincaré 拉回，两个 $\operatorname{Pic}^0$ 因子来自固定纤维限制。BMS Lemma 4.31、Propositions 4.32、4.35 及 Definition 4.39、Lemma 4.41 精确给出这些相容性。具体地，$\phi_{\mathcal B_i}=2f_i$，故 Definition 4.39 的 $\tfrac12(\operatorname{id},\phi_{\mathcal B_i})^*$ 正好是 $(\operatorname{id},f_i)^*$；这里不遗留一个额外的二倍或二分之一。

因此 $H_{D,G_i,\ell}(x)$ 是 $j_b^*\mathcal N_i$ 沿其实际非零截面的规范局部对数。若把 rigidification 改成 BMS §7 使用的 $b$ 处归一化，它只改变一个常数，记
$$H_{D,G_i,\ell}=h_i+\gamma_i,\qquad \gamma_i\in\mathbb Q_\ell.
\tag{2.2}$$
R47 为消去非辅助高度所乘的有理常数也仅造成这样的常数变化。

更一般地，同曲率的另一个对数选择只增加全纯微分的一次积分及常数（BMS Proposition 3.5、Remark 3.6）。下文允许这种变化，它也只会进入全局对数多项式的线性、常数部分。

故有理平移、无基点除子和截面的全局归一化均已匹配到实际局部高度；本节没有把完整迭代积分替换为它的一个二阶片段。

## 3. 所用的已发表代数独立性及标量扩张检查

取 $H^0(X_{\mathbb Q_\ell},\Omega^1)$ 的一组基 $\omega_1,\ldots,\omega_g$，令
$$L_j(x)=\int_b^x\omega_j.$$
将引理 1 的独立类扩成 $V'$ 的一个有理基；清有限分母后可用实际有理线丛表示。每个额外线丛都可以唯一地张量一个 $\operatorname{Pic}^0(J)(\mathbb Q)$ 类，使其拉回到 $X$ 平凡，因为
$$j_b^*:\operatorname{Pic}^0(J)\xrightarrow{\sim}\operatorname{Pic}^0(X)$$
是 $\mathbb Q$ 上的同构。

**BMS Theorem 7.9 的准确输入。** 对这样的一组线丛，全部全纯积分与其规范局部高度在 $\mathbb Q_\ell$ 上代数独立；任一非零多项式在它们上的代入不可能成为恒零的 Vologodsky 函数。该证明以 Theorem 3.15 的高阶符号算子及 Lemma 7.12 的曲率独立性为核心，不使用整个 $J(\mathbb Q)$ 的秩等于亏格。原文 §7.2 的秩不等式用于产生全局多项式关系，不是这个局部独立性结论的额外前提。

下面把其标量问题展开。设
$$H=H^1_{\rm dR}(X/\mathbb Q_\ell),\qquad F=H^0(X_{\mathbb Q_\ell},\Omega^1).$$
第二符号算子满足
$$D_2h_i\in F\otimes H,$$
其在
$$F\otimes H/(F\otimes F)
\longrightarrow H^2_{\rm dR}(J/\mathbb Q_\ell)/F^2$$
下的像是 $c_1(\mathcal N_i)$ 模 $F^2$。这些类在该商中于 $\mathbb Q_\ell$ 上独立。

确实，先在 $\mathbb Q$ 上考虑由有理线丛张成的 NS 子空间。若一个有理线性组合的 Chern 类落在 $F^2$，清分母后得到一个线丛的 Chern 类；在复比较下它既为 $(1,1)$ 型又属于 $H^{2,0}$，故为零。Chern 类在 $\operatorname{NS}(J)_{\mathbb Q}$ 上单射，所以原组合为零。这个有理线性映射单射后，张量 $\mathbb Q_\ell$ 仍单射。因此不是仅排除有理系数关系，而是排除任意 $\mathbb Q_\ell$ 系数关系。

这也直接给出较弱但足够应用 R48 的线性结论：若
$$\sum_i a_i h_i+Q(L_1,\ldots,L_g)=0,\qquad a_i\in\mathbb Q_\ell,$$
且 $Q$ 的次数至多二，则取 $D_2$ 再模 $F\otimes F$ 得到 $\sum_i a_iD_2h_i=0$，从而全部 $a_i=0$。因为对数的二次乘积的二阶符号属于 $F\otimes F$，它们不可能抵消 NS 曲率部分；一次项和常数的二阶符号为零。

完整的多项式独立性由 BMS Theorem 7.9 的 shuffle 代数论证给出。这里引用的是已发表的定理；没有调用 2026 年 equationless 预印本作为未证明输入。

## 4. 从局部高度到 R47 的完整缺陷函数

由 (1.1)，每个 $z_f(x)$ 是 $L_1(x),\ldots,L_g(x)$ 的仿射线性函数。原因是 Abel–Jacobi 对数对 $j_b$ 的微分就是全纯微分，而固定的 $e$ 只给常数项；R47 的 $\log(P_f)$ 除法是在 $K_f\otimes\mathbb Q_\ell$ 中的固定可逆线性变换。因此 (0.1) 的全局高度项是这些 $L_j$ 的二次多项式。结合 (2.2)，可写成
$$\Psi_i=P_i(L_1,\ldots,L_g)-h_i,
\qquad P_i\in\mathbb Q_\ell[X_1,\ldots,X_g],\quad\deg P_i\le2.
\tag{4.1}$$

### 定理 2：实际函数独立

对每个非空剩余圆盘 $\mathscr D$，函数
$$L_1,\ldots,L_g,\Psi_1,\ldots,\Psi_m$$
在 $\mathbb Q_\ell$ 上代数独立。特别地，$\Psi_i|_{\mathscr D}$ 线性独立。

**证明。** 多项式代数的变量替换
$$X_j\longmapsto X_j,\qquad Y_i\longmapsto P_i(X)-Y_i$$
是一个自同构；它的平方是恒等映射。因此，对 $L_j,\Psi_i$ 的任何非零多项式关系，代入 (4.1) 后都给出对 $L_j,h_i$ 的非零多项式关系。

后者由 BMS Theorem 7.9 不可能恒零。若关系只在 $\mathscr D$ 上恒零，Vologodsky 函数的恒等原理使它在整个曲线上恒零；原文 Theorem 7.9 的证明明确使用同一原理。因此每个圆盘上也无这样的关系。证毕。

这个证明没有使用 $c_f\ne0$，也没有把“对数满秩”误当成“高度配对非退化”。即使某些 $c_f$ 为零，局部高度的独立 NS 曲率仍然存在。它同样没有使用对数坐标变换在整数环上可逆：只需 R47 已证明的 $\mathbb Q_\ell$ 可逆性。

### 命题 2A：相容 Hodge 补空间不增加新的根条件

固定 $G\in2\mathcal K_A$、R47 的实际有理截面 $\widetilde s$ 以及圆分字符。设 $W,W'$ 是两个 Hecke 相容的 Hodge 补空间，分别按 R47 同时构造全局高度和辅助局部高度。则
$$\Psi_G^{W'}=\Psi_G^W\quad\text{在全部 }X(\mathbb Q_\ell)\text{ 上。}\tag{4.2}$$

**证明。** 同一圆分字符的两个 Poincaré splitting $\lambda_\ell,\lambda'_\ell$ 在乘纤维标量时具有同一变化量。故其差下降为
$$b:J(\mathbb Q_\ell)\times J^\vee(\mathbb Q_\ell)\longrightarrow\mathbb Q_\ell.$$
双扩张的两套群律使 $b$ 连续且对两个变量分别可加。它在任何一个变量为挠点时为零。在足够小的开子群上，阿贝尔对数把点群同构到 Lie 代数中的满 $\mathbb Z_\ell$ 格。连续可加映射为 $\mathbb Z_\ell$ 线性，故延拓后得到唯一的 $\mathbb Q_\ell$ 双线性形式
$$B:\operatorname{Lie}(J)_{\mathbb Q_\ell}\times
\operatorname{Lie}(J^\vee)_{\mathbb Q_\ell}\longrightarrow\mathbb Q_\ell,$$
使
$$b(P,Q^\vee)=B(\log P,\log Q^\vee).
\tag{4.3}$$
对任意点先乘一个整数使其落入上述开子群，再除该整数，便得所有点上的等式；在特征零值域中这是合法的。

两个 splitting 都与 Hecke 自同态及其对偶相容，所以 $B$ 也平衡。这一局部相容性由相同的构造直接给出：Hecke 稳定的补空间在 Proposition 6.13 下给相容曲率；沿自同态与对偶拉回 Poincaré 对数后，曲率及零轴刚性化相同，Proposition 4.30 的唯一性给出等距性。因此自伴幂等元 $e_A$ 与 $1-e_A$ 在 $B$ 下正交。实际 $G u_D-\eta_{D,G}$ 的 $B$ 分量为零，故 (4.3) 沿 $\widetilde s$ 的变化只涉及 $A$：
$$H^{W'}_{D,G,\ell}(x)-H^W_{D,G,\ell}(x)
=B_A\bigl(\log P(x),\log(GP(x)-e_A\eta_{D,G})\bigr),
\tag{4.4}$$
其中已通过 $\alpha$ 搬运第二变量，$P(x)=e_Au_D(x)$。

非辅助处的 splitting 不随 $W$ 变化。所以对有理 Mordell–Weil 点，两个全局高度的差同样恰为 (4.3)。R47 已证明有理点对数在 $\operatorname{Lie}(A)_{\mathbb Q_\ell}$ 中张成全部空间；两个双线性形式在这些点上相等，因而其 $\mathbb Q_\ell$ 线性延拓在全部 Lie 代数上相等。于是 (0.1) 中全局二次项的变化精确等于 (4.4)，相减给 (4.2)。证毕。

所以可以选择便于计算的相容补空间，但不能把不同补空间所得方程当作新增的共同根条件。本命题不比较不同辅助素数；不同 $\ell$ 的根与全局算术相容性仍是另一问题。

## 5. 饱和空间的真实维数与低阶算法的边界

在一个闭解析子圆盘上取参数 $T\in\mathbb Z_\ell$，使全部 $\Psi_i\in\mathbb Q_\ell\langle T\rangle$。局部解析性和紧性允许作有限个这样的细分。令
$$V_{\mathscr D}=\operatorname{span}_{\mathbb Q_\ell}\{\Psi_i|_{\mathscr D}:1\le i\le m\}.$$
定理 2 给出 $\dim V_{\mathscr D}=m$。R48 因而给
$$
\dim_{\mathbb F_\ell}\overline{\Lambda(V_{\mathscr D})}=m,
\qquad d(V_{\mathscr D})\ge m-1.
\tag{5.1}
$$
若存在共同精确零点 $c$（尤其是盘内一个已知有理 CM 点），则
$$d(V_{\mathscr D})\ge m.\tag{5.2}$$

对 R45 的一个满秩独立方向组，可取
$$m\ge a-n\gg_\varepsilon p^{3/2-\varepsilon},\qquad0<\varepsilon<1/2.$$
所以 (5.1) 是随水平增长的次数下界。这不表示函数真的有这么多零点；它只说明保存完整函数维数的本原约化不能都被压成固定低次数。

八月 equationless 预印本 Corollary 4.3.11 给的是其特定整坐标中的二次约化。把若干此类条件取线性组合、除以 $\ell$ 幂做饱和后，不能继续无条件引用原坐标的二次结论。R48 的例 4 给这个失效的直接模型；本节则表明，在 R45 的大量真实独立方向上，若想保留全部秩，次数增长是必然的。

### 推论 3：任意固定低阶 jet 都会漏掉许多方向

固定 $c\in\mathscr D$ 和整数 $r\ge0$。映射
$$V_{\mathscr D}\longrightarrow\mathbb Q_\ell^{r+1},\qquad
F\longmapsto(F(c),F'(c),\ldots,F^{(r)}(c))$$
的核维数至少为 $m-r-1$。若 $c$ 是共同零点，其核维数至少为 $m-r$。

**证明。** 第一式目标维数为 $r+1$；第二式常数项在整个空间上为零，像维数至多 $r$。秩—零化度公式即给结论。证毕。

因此，允许 $\mathbb Q_\ell$ 线性组合时，在任一点都可找到非零方向使消失阶至少为 $m-1$；在共同根处至少为 $m$。这里的系数未必有理，不宣称该组合本身对应一条整数 Hecke 对应。此结论说明，函数独立性不能被偷换成某个统一低阶 jet 矩阵自动满秩。

## 6. 仍未解决的共同根问题

定理 2 排除了一个可能的退化：大量独立方向并不会在特征零中全部变成同一个或恒零的解析条件。R48 同时说明，没必要先给整数指数统一上界才能谈共同零点。

但代数独立不识别根的位置。一般地，对任意代数独立的解析函数组 $h_1,\ldots,h_m$ 和任一指定的参数 $c$，函数组
$$h_i(T)-h_i(c)$$
仍代数独立，却全部在 $c$ 为零。故独立性本身不能排除一个特定的未知共同根。一个根可以同时满足任意多个代数独立的函数。

当前真正缺项仍是：对实际 (0.1) 证明全部共同根的算术来源，或以其他全局条件排除其中的非 CM 有理点。本文没有证明含 CM 圆盘的唯一性，也没有证明无 CM 圆盘的无根性；R45 的维数增长与本节的函数独立性都不能替代这一步。

## 7. 已核验的原始来源

- A. Besser, J. S. Müller and P. Srinivasan, **$p$-adic adelic metrics and quadratic Chabauty I**, *Journal für die reine und angewandte Mathematik* **828** (2025), 223–305, DOI [10.1515/crelle-2025-0063](https://doi.org/10.1515/crelle-2025-0063)。核对用作者标为 final version 的 [arXiv:2112.03873v4](https://arxiv.org/abs/2112.03873v4) 和[作者全文](https://padmask.github.io/QuadraticChabauty.pdf)。准确位置：Proposition 4.30、Lemma 4.31、Propositions 4.32、4.35、Definition 4.39、Lemma 4.41、Proposition 6.13、Theorem 6.10；独立性为 Theorem 7.9、Lemma 7.12。作者全文 pp.51–53 给后两项的完整证明。
- N. Dogra and S. Le Fourn, **Quadratic Chabauty for modular curves and modular forms of rank one**, *Mathematische Annalen* **380** (2021), 393–448, [正式全文](https://link.springer.com/article/10.1007/s00208-020-02112-3)。Lemma 7 的解析子群论证与 R47 一致；本文未改变其有限性定理的范围。
- S. Hashimoto, G. M. Lido, D. Lombardo, N. Mascot and P. Parent, **Equationless quadratic Chabauty for non-split Cartan modular curves**, [arXiv:2608.10919v1](https://arxiv.org/html/2608.10919v1)，2026。只用作算法范围对照，不作本结果的证明前提。HTML 中 Corollary 4.3.11、Theorem 4.4.6 分别对应低阶约化及带整数满射假设的闭包参数化。
- 本仓库 [R45](R45-heegner-quotient-integral-directions.md)、[R47](R47-heegner-logarithms-global-height.md)、[R48](R48-analytic-saturation-and-root-certificates.md) 提供实际方向、真实高度方程与饱和线性代数。
