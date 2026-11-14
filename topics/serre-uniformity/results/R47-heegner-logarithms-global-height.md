# R47. Heegner 商的对数同构与无常数分支的实际高度方程

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 本文首先把 Dogra–Le Fourn Lemma 7 证明中已发表的论证，无条件应用于 R45 的实际 Heegner 商 $A$：对每个辅助素数 $\ell$，
$$\boxed{\quad
\log_A:A(\mathbb Q)\otimes_{\mathbb Z}\mathbb Q_\ell
\xrightarrow{\sim}\operatorname{Lie}(A)_{\mathbb Q_\ell}.
\quad}\tag{0.1}$$
因此 $A(\mathbb Q)$ 的 $\ell$ 进闭包在 $A(\mathbb Q_\ell)$ 中为有限指数。这里没有 BSD 假设：$A$ 的各简单因子已由其解析秩一获得非挠有理点和正确的 Mordell–Weil 秩。

随后证明一个相容的实际高度接口。对 R45 积分核中的 $F$，取 **$G=2F$ 一次**。其无基点 Poincaré 拉回线丛有一个定义于 $\mathbb Q$ 的处处非零截面，可用一个有理常数同时归一化，使每个非辅助有限素数的局部高度恒零。采用同一 Poincaré splitting 的符号定义全局和局部高度，所有有理点遂满足
$$\boxed{\quad
\sum_f\operatorname{Tr}_{K_f\otimes\mathbb Q_\ell/\mathbb Q_\ell}
\bigl(c_f z_f(x)(G_fz_f(x)-\xi_{G,f})\bigr)
-H_{D,G,\ell}(x)=0.
\quad}\tag{0.2}$$
其中 $z_f$ 使用实际 $u_D(x)=[dx-D]$ 坐标，$d=(p-1)/2$；$\xi_{G,f}$ 是同一规范平移的坐标。辅助 $\ell$ 处的 $H_{D,G,\ell}$ 保留**完整实际局部高度**，没有删去迭代积分或把某个 Hecke 二次微分代替它。

(0.1) 是已知论证在本商上的明确推论；本文不对其作新颖性声称。(0.2) 的全局归一化与 R43、R45 相接。本文不给出统一积分指数、单位行列式或共同根排除。

## 1. 解析子群定理与有理点的下降

固定嵌入 $\overline{\mathbb Q}\hookrightarrow\mathbb C_\ell$。使用 Fuchs–Pham (2015), Theorem 2.2 的已发表版本：若交换代数群 $C/\overline{\mathbb Q}$、非零代数线性子空间 $V\subset\operatorname{Lie}(C)$ 与代数点 $P$ 满足
$$0\ne\log_C(P)\in V\otimes\mathbb C_\ell,$$
则有正维代数子群 $H\subset C$，使
$$P\in H(\overline{\mathbb Q}),\qquad\operatorname{Lie}(H)\subset V.\tag{1.1}$$
定理中的对数定义域含阿贝尔簇的全部有限局部域点；阿贝尔簇在局部域上的点群紧，对数核为挠点。定理给的是包含 $P$ 的子群，未要求连通。

**引理 1。** 若 $C/\mathbb Q$ 是 $\mathbb Q$-单阿贝尔簇，$P\in C(\mathbb Q)$ 非挠，则 $\log_C(P)$ 不属于任何真 $\overline{\mathbb Q}$-线性子空间的 $\mathbb C_\ell$ 扩张。

**证明。** 对数非零。若所述子空间为零，已经矛盾；否则由 (1.1) 得到真子群 $H$。选正整数 $m$，使 $mP\in H^0$。$H^0$ 的定义方程只使用有限多个代数数，故可取一个有限 Galois 扩张 $L/\mathbb Q$ 定义它。令
$$C_0=\left(\bigcap_{\sigma\in\operatorname{Gal}(L/\mathbb Q)}
{}^\sigma H^0\right)^0.$$
交集对 Galois 稳定，其恒等分量是定义于 $\mathbb Q$ 的阿贝尔子簇。由于 $mP$ 为有理点，它属于每个共轭子群；所以交集含整个无限循环群 $\mathbb ZmP$，不可能为零维。因而 $C_0$ 正维，同时包含于真子簇 $H^0$。这与 $C$ 的 $\mathbb Q$-单性矛盾。

即使用只保证 $mP\in H$ 的较弱表述，相同论证也成立；这里没有把“存在某个子群”误读成“该子群自动定义于 $\mathbb Q$”。证毕。

等价地，$\mathbb ZP$ 的几何 Zariski 闭包由有理点生成，因而下降到 $\mathbb Q$；其正维恒等分量必为整个 $C$。这也说明为什么此处需要点属于 $C(\mathbb Q)$，不能无条件替换成任意扩域点。

## 2. $\mathrm{GL}_2$ 型因子的每个对数分量均非零

设 $C/\mathbb Q$ 是 $\mathbb Q$-单阿贝尔簇，有数域
$$K\hookrightarrow\operatorname{End}_{\mathbb Q}^0(C),
\qquad [K:\mathbb Q]=\dim C=r.$$
那么 $\operatorname{Lie}(C)$ 是秩一 $K$-模：非零 $K$ 元素为同源，故其微分可逆；维数等式给秩一。

写
$$K\otimes\mathbb Q_\ell=\prod_{v\mid\ell}K_v.$$
对每个 $\sigma:K\hookrightarrow\overline{\mathbb Q}$，$\operatorname{Lie}(C)_{\overline{\mathbb Q}}$ 有一维特征分量 $V_\sigma$。这些分量确实在代数数上定义：若 $\theta$ 为 $K$ 的本原元，相应投影为
$$e_\sigma=
\prod_{\tau\ne\sigma}
\frac{\theta-\tau(\theta)}{\sigma(\theta)-\tau(\theta)}
\quad\text{作用于 }\operatorname{Lie}(C)_{\overline{\mathbb Q}}.\tag{2.1}$$
其系数位于 $K$ 的某个有限正规闭包中。这里先分解代数特征分量，未将一个任意 $\mathbb Q_\ell$ 子空间冒充代数子空间。

**命题 2。** 对任意非挠 $P\in C(\mathbb Q)$，映射
$$K\otimes\mathbb Q_\ell\longrightarrow
\operatorname{Lie}(C)_{\mathbb Q_\ell},
\quad t\longmapsto t\log_C(P)\tag{2.2}$$
为同构。特别地，只要 $C(\mathbb Q)$ 正秩，其局部闭包就具有完整维数 $r$。

**证明。** 选一个 $K$-基 $e$，写 $\log_C(P)=we$，其中 $w\in K\otimes\mathbb Q_\ell$。若 $w$ 的某个 $K_v$ 分量为零，在进一步嵌入 $\mathbb C_\ell$ 后，其某个代数特征分量为零。于是
$$\log_C(P)\in\bigoplus_{\tau\ne\sigma}V_\tau\otimes\mathbb C_\ell,$$
与引理 1 矛盾。因此 $w$ 在每个域因子均非零，是乘积代数 $K\otimes\mathbb Q_\ell$ 的可逆元；乘 $w$ 即 (2.2)，所以为同构。

取 $K$ 中一个作用于 $C$ 的整数阶。该阶作用于 $P$ 的对数已经张成右侧，故整个 Mordell–Weil 群的对数像也张成右侧。证毕。

**注意“可逆”的环。** $w$ 这里在 $K\otimes\mathbb Q_\ell$ 中可逆，不表示它在任何整数阶中是单位；其各分量可以具有很大的正赋值。这一差别正是统一积分指数仍然未被控制的原因之一。

**推论 3（R45 的实际商）。** 对 R45 的 $A$，(0.1) 成立，其有理点闭包在局部点群中为有限指数。

**证明。** $A$ 在 $\mathbb Q$ 上同源于解析秩一的 $A_f$ 的乘积。每个 $A_f$ 为 $\mathbb Q$-单，有系数域 $K_f\subset\operatorname{End}_{\mathbb Q}^0(A_f)$，且
$$\operatorname{rk}A_f(\mathbb Q)=\dim A_f=[K_f:\mathbb Q]>0.$$
命题 2 给每个简单因子上的对数满射；定义域与值域维数相同，所以为同构。有限乘积保持此性质。

若将乘积换成所选同源模型 $A$，同源在 Lie 代数上为同构，并在有理 Mordell–Weil 群张量 $\mathbb Q$ 后为同构：一个反向同源使两个复合等于整数乘法。故结论不受同源模型影响。

最后，满秩有限生成对数像的 $\mathbb Z_\ell$ 闭包是 Lie 代数中的满格，包含某个开邻域。对数在足够小的开子群上为局部同构，所以有理点闭包是开子群；$A(\mathbb Q_\ell)$ 紧，开子群指数有限。证毕。

**准确的文献关系。** Dogra–Le Fourn Lemma 7 的证明已经包含上述特征分量和解析子群论证。其陈述对整个 Jacobian 使用弱 BSD，仅为保证所有简单因子正秩；对本文按 $L'(f,1)\ne0$ 定义的 $A$，这个正秩输入已无条件成立。因此本推论是去掉一个在本商上多余的假设，不是新的解析子群定理，也不解决一般阿贝尔簇的 $\ell$ 进闭包维数猜想。

## 3. Hecke 相容的高度与准确的迹表示

以下 $\ell\ne p$，在 $X=X_{\rm ns}^+(p)$ 的好约化辅助素数处取值于 $\mathbb Q_\ell$ 的圆分高度。先说明相容 Hodge splitting 的存在，不要求普通约化。

令 $R=\mathbb T_{\mathbb Q}\otimes\mathbb Q_\ell$。由新形式重数一，$H^1_{\rm dR}(J)_{\mathbb Q_\ell}$ 为秩二 $R$-模，而其 Hodge 子空间为秩一 $R$-模。$R$ 是有限个特征零域的乘积，所以可选秩一的 $R$-模补空间 $W$。

此 $W$ 自动对杯积各向同性。确实，Hecke 的 Rosati 自伴性给
$$\langle tu,v\rangle=\langle u,tv\rangle\quad(t\in R).$$
不同域因子正交。在一个域因子上，若 $w$ 生成其秩一补空间，则
$$\langle xw,yw\rangle=\langle w,xyw\rangle
=\langle xyw,w\rangle
=-\langle w,xyw\rangle,$$
所以为零。故 $W$ 为 Hecke 相容的 Lagrangian 补空间。

对相应 splitting，Nekovář／Coleman–Gross 高度具有对称性和 Hecke 平衡性；精确可用条件见 Balakrishnan–Dogra–Müller–Tuitman–Vonk (2023), §3.3 及其所引 Nekovář §4.11。这只要求与所用交换 Hecke 代数相容，不要求与一个更大的、可能非交换的几何自同态代数相容。

为严格固定符号，令 $\mathcal P$ 是 R43 的 Poincaré 线丛，$\lambda_v$ 是同一全局字符及上述 splitting 给出的局部函数。对 $P\in J(\mathbb Q)$、$Q^\vee\in J^\vee(\mathbb Q)$ 和任一非零有理纤维向量 $t$，定义
$$h_{\mathcal P}(P,Q^\vee)=\sum_{v<\infty}\lambda_v(t).\tag{3.1}$$
更换 $t$ 乘 $c\in\mathbb Q^\times$ 时，改变为 $\sum_v\chi_v(c)=0$，故此定义与 $t$ 无关。采用 R43 的识别 $\alpha:J^\vee\to J$，记
$$h_J(P,Q)=h_{\mathcal P}(P,\alpha^{-1}Q).\tag{3.2}$$
若与另一常用极化约定相差整体负号，这个号已经统一包含在 (3.2) 中。下文的全局与局部项始终使用同一个 $\lambda$，不将 R43 的 $h^{\rm Nek}=-\lambda$ 只应用到等式一边。

把 $h_J$ 限制到有理幂等元 $e_A$ 的像，再通过所选同源搬到 $A$，记为 $h_A$。按 $A\sim\prod_f A_f$ 分解并选每个非挠 $P_f\in A_f(\mathbb Q)$。由于 Mordell–Weil 群张量 $\mathbb Q$ 是秩一 $K_f$-模，任意点的有理坐标可写成 $tP_f$。由推论 3，同样的坐标通过对数延拓到局部 Lie 代数。

**命题 4。** 存在唯一的一组
$$c_f\in R_f:=K_f\otimes\mathbb Q_\ell$$
使延拓后的高度满足
$$h_A((x_fP_f)_f,(y_fP_f)_f)
=\sum_f\operatorname{Tr}_{R_f/\mathbb Q_\ell}(c_fx_fy_f).\tag{3.3}$$
不要求 $c_f$ 非零或可逆。

**证明。** 不同中心幂等元的像在高度下正交，因为
$$h_J(e_fP,e_gQ)=h_J(P,e_fe_gQ)=0\quad(f\ne g).$$
在一个因子上，Hecke 平衡性给
$$h_f(xP_f,yP_f)=h_f(P_f,xyP_f).$$
右侧是 $xy\in R_f$ 的一个 $\mathbb Q_\ell$-线性函数。有限可分代数的迹配对非退化，所以它唯一写成 $\operatorname{Tr}(c_fxy)$。证毕。

式 (3.3) 精确减少全局高度数据的自由参数，但没有计算这些参数，也没有证明高度非退化。非退化性与 (0.1) 是不同问题。

## 4. R45 积分核的全局截面归一化

取 $F\in\mathcal K_A$，其中 $\mathcal K_A$ 是 R45 的实际整数格，且已取共同倍数以消去 $B$ 中的 Chow–Heegner 挠投影。无有理点时所需点集排除已成立；在可能存在有理点的分支，R45 已证明其规范 $D$ 平移也无 $B$ 分量。以下公式只使用这个 $D$ 平移，不再选择基点。

记
$$L_F=(u_D,h_{D,F}u_D)^*\mathcal P.$$
R14、R18、R33 保证 $L_F$ 在 $\mathbb Q$ 上有处处非零全局截面 $s_F$。这里需要实际线丛与实际有理截面，不能只用几何 Picard 类平凡。令
$$G=2F,\qquad s=s_F^{\otimes2}.$$
规范平移对 $F$ 可加，所以
$$h_{D,G}=2h_{D,F},\qquad\eta_{D,G}=2\eta_{D,F},
\qquad L_G\simeq L_F^{\otimes2}.\tag{4.1}$$
因此 $s$ 是 $L_G$ 的有理非零截面。R30 的积分线丛恰为 $L_G$ 的延拓；没有再次乘二。

在坏素数 $p$，R45 的核条件给
$$\operatorname{div}_U(s)=k(F)\sum_iU_i.\tag{4.2}$$
故所有分量上共同的垂直阶是整数 $k(F)$，不是 $2k(F)$。

在每个好素数 $q\ne p$，取 $X$ 的光滑、射影、几何连通模型 $\mathcal X_q$。$J$ 的 Néron 模型是阿贝尔概形；$u_D$、实际同态和有理平移均延拓，Poincaré 给出 $L_G$ 的积分延拓。因为 $s$ 在完整泛纤维上处处非零，其除子只有垂直部分；光滑几何连通特殊纤维不可约，所以
$$\operatorname{div}_{\mathcal X_q}(s)=m_q\mathcal X_{q,s}
\quad(m_q\in\mathbb Z).\tag{4.3}$$

这里 $X_{\rm ns}^+(p)$ 在全部 $q\ne p$ 有好约化，包括 $2,3$。可用满水平曲线在 $\mathbb Q_q(\zeta_p)$ 上的光滑模型及有限商说明：该扩张未分歧，曲线的正亏格商仍有好约化，见 Baker–González-Jiménez–González–Poonen Lemmas 3.19–3.20；光滑最小模型沿未分歧下降回 $\mathbb Q_q$。这里使用的是规范模曲线的下降，不对任意二次扭曲的同一复曲线声称好约化。

置 $m_p=k(F)$。由有限型对象及其有理截面的 spreading out，$m_q=0$ 对几乎所有 $q$ 成立：模型、映射、线丛、处处非零泛纤维截面及其逆只需在有限多个素数取分母。因而下面的积是有限有理数：
$$c=\prod_q q^{-m_q}\in\mathbb Q^\times,
\qquad\widetilde s=cs.\tag{4.4}$$

**命题 5。** $\widetilde s$ 在每个好素数的完整光滑模型上为积分可逆截面，并在坏 $p$ 的全部 $U$ 上为积分可逆截面。对每个辅助素数 $\ell\ne p$、每个 $q\ne\ell$ 及 $x\in X(\mathbb Q_q)$，
$$\lambda_q(\widetilde s(x))=0.\tag{4.5}$$

**证明。** 在 $q$ 处，(4.4) 改变除子阶恰为 $-m_q$，而积中其他素数是局部单位；由 (4.2)–(4.3)，新截面除子为零。正则模型上的有理截面除子为零等价于截面处处为单位。

好素数处所有局部点由真性延拓到该光滑模型；坏 $p$ 处所有局部点落在 $U$，这是 R43 用 $p\in\mathfrak m_P^\rho$、$\rho>1$ 排除分歧度 $1$ 截面经过共同奇点的结论。对 $q\ne\ell$，字符 $\chi_q$ 在整数单位上为零，R43 的积分 Poincaré splitting 因而给 (4.5)。证毕。

辅助 $\ell$ 处即使截面也是积分可逆，其高度**仍可以变化且非零**：$\chi_\ell$ 在主单位上一般非零，所选 Hodge splitting 也参与局部函数。上述归一化没有消去这个实际高度。

## 5. 实际 $D$ 坐标中的完整必要方程

对 $x\in X(\mathbb Q_\ell)$，在同源范畴记
$$P(x)=e_Au_D(x),\qquad
z_f(x)=\frac{\log_{A_f}(P(x)_f)}{\log_{A_f}(P_f)}\in R_f.\tag{5.1}$$
这个“商”指命题 2 的秩一模同构，不是任选两条坐标相除。它在每个残数圆盘上为局部解析函数。

记 R14 的规范平移为 $\eta_{D,G}\in J(\mathbb Q)$，并设
$$\xi_{G,f}=\frac{\log_{A_f}((e_A\eta_{D,G})_f)}
{\log_{A_f}(P_f)}.\tag{5.2}$$
因为平移是有理 Mordell–Weil 点（允许同源的有理分母），$\xi_{G,f}$ 实际来自 $K_f\subset R_f$。$G$ 及平移在 $B$ 上均为零，所以
$$h_J(u_D(x),\,G u_D(x)-\eta_{D,G})
=h_A(P(x),\,G P(x)-e_A\eta_{D,G})\tag{5.3}$$
对有理点成立，并通过 (0.1) 延拓其右侧为所有局部点上的全局高度表达式。

定义同一 Poincaré splitting 的实际辅助高度
$$H_{D,G,\ell}(x)=\lambda_\ell(\widetilde s(x)).\tag{5.4}$$

**定理 6。** 全部 $x\in X(\mathbb Q)$ 满足 (0.2)。

**证明。** $\widetilde s(x)$ 是纤维
$$P_{u_D(x),\,h_{D,G}u_D(x)}^\times(\mathbb Q)$$
中的非零有理向量。按 (3.1) 定义，全局高度就是所有有限局部高度之和。由命题 5，非辅助项全部为零，故
$$h_{\mathcal P}(u_D(x),h_{D,G}u_D(x))
=H_{D,G,\ell}(x).$$
另一方面
$$h_{D,G}u_D=f_Gu_D-\alpha^{-1}\eta_{D,G},
\qquad\alpha f_G=G,$$
所以左侧恰为 (5.3)。再用命题 4 的迹表示得到 (0.2)。整个证明使用同一 $\lambda$ 符号，没有引入额外的 $-1$ 或 $2$。证毕。

式中 $z_f(x)$ 已经使用 $u_D(x)=[dx-D]$。因此它本身含有 $d$ 的微分缩放，(0.2) 不再外乘一个 $d^2$。若另有局部基点 $b$，R43 的
$$L_{D,G}\simeq L_{b,G}^{\otimes d^2}\otimes C_b$$
才把无基点高度转成基点高度加常数；在其标准 Nekovář 约定下，基点局部高度为相应 $\lambda$ 的负值。换这种约定时必须同时转换全局项、局部项和常数，不能只把 (0.2) 的某一项变号。

对 $\mathcal K_A$ 的一个有限整数基，分别作 (4.4)，再利用 Poincaré 群律张量相乘，可以使全部 $G\in2\mathcal K_A$ 的截面选择与加法相容。乘二不改变格秩。R45 因而提供秩至少 $a-n$ 的实际对应方向，分别具有上述无常数分支的必要方程；本文不凭方向独立便声称所有所得解析函数的低阶 jet 自动满秩。

## 6. 精确边界

这里已证的是对数在 $\mathbb Q_\ell$ 上的可逆性、Hecke 相容的高度表示，以及真实有理截面的全局归一化。其常数和基选择仍依赖于层 $p$；(2.2) 的逆可能有大的 $\ell$ 进分母，所用 Hecke 投影、同源、规范平移和高度系数 $c_f$ 同样没有统一积分控制。即使有限指数已证，也不能推出指数为 $1$、有统一上界或某个导数为单位。

$H_{D,G,\ell}$ 是完整的辅助局部高度。本文没有计算它的迭代积分部分，未证明与全局二次项相减后的首个非零系数有统一阶数或单位性，更未排除所有不含 CM 点的残数圆盘中的共同根。因此 (0.2) 不能视作 Serre 一致性证明；它明确了下一步需要控制的真实函数，而不是只控制其一个二次片段。

## 7. 已核对的来源

- N. Dogra and S. Le Fourn, **Quadratic Chabauty for modular curves and modular forms of rank one**, *Mathematische Annalen* **380** (2021), 393–448，DOI [10.1007/s00208-020-02112-3](https://doi.org/10.1007/s00208-020-02112-3)，[期刊全文](https://link.springer.com/article/10.1007/s00208-020-02112-3)。Lemma 7 的证明给本文 §1–2 的已知核心论证；Definition 4、Proposition 3 给实际 $A$ 的秩与 Chow–Heegner 条件；Corollary 1 清楚列出对数闭包有限指数在显式高度函数中的作用。
- C. Fuchs and D. H. Pham, **The $p$-adic analytic subgroup theorem revisited**, *p-Adic Numbers, Ultrametric Analysis and Applications* **7** (2015), no. 2, 143–156，DOI [10.1134/S2070046615020065](https://doi.org/10.1134/S2070046615020065)；[已发表期刊页](https://link.springer.com/article/10.1134/S2070046615020065)，[作者版本](https://arxiv.org/abs/1502.00768)。Theorem 2.2 给包含指定点 $P$ 的子群版本；§3.1 说明对数定义域、挠核及函子性。本文只使用这个已发表定理。
- J. S. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman and J. Vonk, **Quadratic Chabauty for modular curves: algorithms and examples**, *Compositio Mathematica* **159** (2023), 1111–1152；[期刊全文](https://www.cambridge.org/core/journals/compositio-mathematica/article/quadratic-chabauty-for-modular-curves-algorithms-and-examples/C317E63BB0128EB3F2163621CA63E66E)。§3.3 明确 Hecke／自同态相容、各向同性 Hodge splitting 导致高度对称和平衡的条件；本文对所需交换代数直接给出了这种补空间的存在证明。
- M. H. Baker, E. González-Jiménez, J. González and B. Poonen, **Finiteness results for modular curves of genus at least 2**, *American Journal of Mathematics* **127** (2005), 1325–1387，DOI [10.1353/ajm.2005.0037](https://doi.org/10.1353/ajm.2005.0037)；[作者全文](https://math.mit.edu/~poonen/papers/finiteness.pdf)。Lemmas 3.19–3.20：好约化曲线的正亏格有限商仍好约化，及模曲线在层之外的好约化。
- 仓库 R14、R18、R30、R33、R43、R45 分别提供实际规范平移、无基点范数、坏素数乘二、真实截面与障碍、Poincaré／Nekovář 符号比较、真正容许的积分核。
- 文献范围备注：A. Burungale, C. Skinner and X. Wan, **A refined non-vanishing of the $p$-adic logarithm of a rational point on an abelian variety**, [arXiv:2603.20886](https://arxiv.org/abs/2603.20886)，2026，讨论更一般域与点的特征分量非消失。本文不把该新文作为证明输入；所需 $\mathbb Q$-单因子的有理点情形已从上述 2015 年定理完整推出，并已出现在 DLF Lemma 7 的论证中。
