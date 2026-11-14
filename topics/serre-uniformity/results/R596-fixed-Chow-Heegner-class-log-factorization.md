# R596：固定 Chow–Heegner 类的秩一投影与实际高度的对数分解

日期：2026-11-14。状态：**下述固定类及高度障碍已解除；一般 \(d\) 的商秩与局部高度首项仍 OPEN。**

恢复说明：环境重置同时清空了原稿 `r596_proof_checkpoint_v3` 和旧工作区。本稿按已发送的完整三段论证、恢复摘要及根代理的审核意见重建，属于 `reconstructed-after-environment-reset`。本 v2 副本另明确采用新恢复 R593 的清分母与截面；原已哈希重建稿保持不变。重新计算的摘要只证明当前文件的字节；不沿用原稿哈希。R593 的几何与局部高度前置已按完整恢复稿先行发布；本稿采用其中新选定的实际清分母、截面与高度规范。

## 1. 保持同一个实际几何与极化

采用 R593 的实际曲线族和二层底曲线：

\[
 X_d:\quad j=6912db^3(1-db^3),\qquad
 Y=W_p:\quad j=6912v(1-v),\qquad
 \phi_d:X_d\longrightarrow Y,\ v=db^3.
\tag{596.1}
\]

这是在同一非分裂 Cartan 项链曲线上取相应规范化后的记号。\(\phi_d\) 是三次覆盖；\(X_d\) 不是只由右侧平面公式定义的有理曲线。指定 CM 基点记作 \(c_{0,d}\)，它们的 \(Y\)-像是同一个指定的 \(c_{\rm base}\)。

取实际出现的权二因子

\[
 A_d=A_{\theta,d},\qquad
 g_{\theta,d}=\operatorname{AI}_{K/\mathbb Q}
       (\Psi\theta\kappa_4\kappa_d^{-1}),\quad
 K=\mathbb Q(\sqrt{-3}),
\tag{596.2}
\]

及实际商 \(q_d:J_{X_d}\to A_d\)。令

\[
 j_d(x)=q_d[x-c_{0,d}].
\tag{596.3}
\]

\(\lambda_d\) 是前置中固定并沿立方扭曲传递的极化，\(F\) 为 \(A_d\) 的全实系数域。对 \(h\in F\) 的 Rosati 对称部分，令 \(\mathcal L_{h,d}\in\operatorname{Pic}(A_d)\otimes\mathbb Q\) 是沿原点刚性化的对称线丛，满足

\[
 \lambda_{\mathcal L_{h,d}}=\lambda_d\circ h.
\tag{596.4}
\]

实际商与极化给正元素 \(\kappa=q_dq_d^\dagger\in F\)，在前置的同源规范下定义

\[
 F^0=\{h:\operatorname{Tr}_{F/\mathbb Q}(\kappa h)=0\}.
\tag{596.5}
\]

这是拉回次数为零的 **实际加权迹** 条件，不替换成未经证明的 \(\operatorname{Tr}(h)=0\)。

R593 已给出：对 \(h\in F^0\)，

\[
 \kappa_{h,d}:=j_d^*\mathcal L_{h,d}\in\operatorname{Pic}^0(X_d)\otimes\mathbb Q,
 \qquad
 \kappa_{h,d}=\phi_d^*\eta_h,
\tag{596.6}
\]
\[
 \eta_h=\frac13\phi_{d,*}\kappa_{h,d}
 \in\operatorname{Pic}^0(Y)\otimes\mathbb Q.
\tag{596.7}
\]

\(\eta_h\) 与 \(d\) 无关。这里的 \(\mu_3\) 甲板作用作为群作用下降到 \(\mathbb Q\)，虽然某个具体生成元只在 \(K\) 上定义。其不变投影是 \(\phi_d^*\phi_{d,*}/3\)。实际极化甲板不变以及同一几何同态的扭曲下降是 (596.6) 的前置，不从任意 Picard 类的不变性臆造它。

R593 的条件性高度关系还涉及下面的障碍：对 \(P\in J_Y(\mathbb Q)\otimes\mathbb Q_p\)，是否有

\[
 \log_pP=0\quad\Longrightarrow\quad h_Y(P,\eta_h)=0.
\tag{596.8}
\]

本篇证明 (596.8)，并给该线性高度项在对数空间上的明确抽象表达。

## 2. 结论及没有获得的结论

设 \(J_H\) 是 \(J_Y\) 的下述 \(\mathbb Q\)-同源直因子：对每个简单模形式块，若有一个实嵌入的中心一阶导数非零，就把该块的全部重数取入 \(J_H\)。记对应的有理投影为 \(e_H\)。

**定理 596.1。** 对每个 (596.5) 的 \(h\)，

\[
 \eta_h=e_H\eta_h\quad
 \text{于 }J_Y(\mathbb Q)\otimes\mathbb Q,
\tag{596.9}
\]

其中用 \(J_Y\) 的主极化识别 \(\operatorname{Pic}^0(Y)\) 与 \(J_Y\)。此外

\[
 \operatorname{rank}J_H(\mathbb Q)=\dim J_H,\qquad
 \log_p:J_H(\mathbb Q)\otimes\mathbb Q_p
       \xrightarrow{\sim}\operatorname{Lie}(J_H)(\mathbb Q_p).
\tag{596.10}
\]

对 R593 中固定的同一个全局角色 \(\chi\) 及其同一个 Poincaré 双扩张高度，有线性泛函

\[
 \ell_h:\operatorname{Lie}(J_Y)(\mathbb Q_p)\to\mathbb Q_p
\]

使所有有理点满足

\[
 h_Y(P,\eta_h)=\ell_h(\log_pP).
\tag{596.11}
\]

这特别证明 (596.8)。

本定理不证明一般 \(d\) 的 \(A_d\) 都有秩等于维数，也不识别 \(\ell_h\) 的数值或其首项是否为单位。它没有断言另一个实际 CM 点差 \(\beta_d=q_d[c_{1,d}-c_{0,d}]\) 为挠；该点差不能当作下面规范模曲线上的平凡环面角色迹。

## 3. 只为计算固定类使用 \(d=4\)

因为 (596.7) 与 \(d\) 无关，可以仅在参考 \(d=4\) 上计算 \(\eta_h\)。此时

\[
 j=2^{10}3^3u^3(1-4u^3),
\tag{596.12}
\]

正是前置中固定的规范六水平模曲线与非分裂 Cartan 层的纤维积 \(X_4\)。角色中的 \(\kappa_4\kappa_d^{-1}\) 抵消，商成为实际未扭的 \(\operatorname{AI}(\Psi\theta)\) 形式。

此规范 adelic 水平的紧开群 \(U\) 含全部有限整中心 \(\widehat{\mathbb Z}^{\times}I\)。由于

\[
 \mathbb A_f^{\times}=\mathbb Q_{>0}^{\times}\widehat{\mathbb Z}^{\times},
\tag{596.13}
\]

且有理中心已在模曲线商中消去，所有相关自守表示的有限中央角色均平凡。这里没有把非紧的 \(\mathbb A_f^{\times}\) 错写为紧开群 \(U\) 的子群。正是 (596.13) 允许下文对有理 CM 轨道使用平凡环面角色；若中央角色不平凡，这一步必须改成相容的非平凡角色，不能沿用本证明。

选择 \(X_4\) 的有理次数一 Hodge 基点 \(o\)。它在 \(\operatorname{Pic}\otimes\mathbb Q\) 中可取为尖点有理组合，因为模判别式的除子支持于尖点。令 \(j_o=q_4[x-o]\)。

改变基点只给 \(j_o^*\mathcal L_{h,4}\) 增加一个属于 \(q_4^\dagger A_4^\vee\) 的次数零类。由真实新部关系

\[
 q_4\phi_4^*=0,\qquad\phi_{4,*}q_4^\dagger=0,
\tag{596.14}
\]

这个改变量的 \(\phi_{4,*}\) 为零。因此可以用 \(o\) 计算 (596.7)，而不改变固定的 \(\eta_h\)。

## 4. 用实际 Hecke 对应表示固定类

设 \(\mathcal P\) 为 \(A_4\times A_4^\vee\) 上沿两个零截面刚性化的 Poincaré 线丛。令

\[
 \mathcal C_h=(j_o\circ\operatorname{pr}_1,
          \lambda_4h\,j_o\circ\operatorname{pr}_2)^*\mathcal P.
\tag{596.15}
\]

对曲线乘积上的对应线丛 \(\mathcal C\)，定义修改后的对角拉回

\[
 D_{\mathcal C}(o)=\Delta^*\mathcal C
       -\mathcal C|_{X\times o}-\mathcal C|_{o\times X}
       \quad\text{于 }\operatorname{Pic}(X)\otimes\mathbb Q.
\tag{596.16}
\]

此定义对有理除子 \(o\) 按线性延拓。\(h\in F^0\) 保证其次数为零。对称线丛的 theorem of the square 给

\[
 D_{\mathcal C_h}(o)=2j_o^*\mathcal L_{h,4},\qquad
 \eta_h=\frac16\phi_{4,*}D_{\mathcal C_h}(o).
\tag{596.17}
\]

对应线丛按两个因子的拉回类取商后，与 \(\operatorname{Hom}(J_X,J_X^\vee)\) 相同；(596.16) 杀掉这些两因子的拉回。因此只要在 Jacobian 同态上用 Hecke 对应表示 (596.15)，就足以计算 (596.17)。

使用完整的 adelic Hecke 代数，包括水平素数处的算子。在每个出现的不可约表示 \(\pi\) 上，其 \(U\)-固定空间 \(\pi^U\) 有限维；密度定理使相应算子在该空间上给全部矩阵代数。再利用有限个出现的不可约块的分离，可以同时指定其中一个块的所需矩阵并令其他块为零。以有理系数和系数域下降表述，这给每个 \(A_4^m\) 等型块上的 \(M_m(F)\)。

这一陈述只对 **每个不可约 \(\pi^U\)，并同时分离有限个出现块** 使用。它不声称任意 admissible 可约表示的 Hecke 作用都是全部自同态代数。相应标准的模形式/Jacobian 同态比较可见 Zhang 的 §2.4：

<https://web.math.princeton.edu/~shouwu/publications/crmnote.pdf>

因此可选有限个真实 Hecke 对应的有理线性组合 \(Z_h\)，使它与 \(\mathcal C_h\) 在上述 Jacobian 同态空间中相同，故

\[
 D_{Z_h}(o)=D_{\mathcal C_h}(o).
\tag{596.18}
\]

必须把 Hecke 对应当作**推前后的代数循环并保留其重数**。Yuan–Zhang–Zhang 的勘误已经明确这个规范，不能用集合意义的像替代：

<https://faculty.bicmr.pku.edu.cn/~yxy/preprints/erratum-GZSC.pdf>

非标量 Hecke 对应与对角线的内部交点是 CM 点：固定的椭圆曲线具有额外的非标量有理自同源。边界交点是尖点。标量分量的对角自交给 \(-K_X\)；Hodge 类由尖点表示，模曲线的 canonical/Hodge 比较的额外椭圆分支点同样是 CM 点。因此 (596.16)–(596.18) 表明

\[
 \eta_h\text{ 是 }Y\text{ 上有理 CM 轨道及尖点的次数零有理组合。}
\tag{596.19}
\]

这一步只说明类的几何支撑，不把未经处理的三重积 Gross–Zagier 公式或其 ramified error 直接应用于 \(\eta_h\)。

## 5. 消灭高阶零点因子上的 CM 轨道投影

考虑任一平凡中央角色的规范模曲线 \(C\)，以及其简单模形式因子 \(A_f\)。假设对每个系数域嵌入 \(\sigma\) 都有

\[
 L(f^\sigma,1)=L'(f^\sigma,1)=0.
\tag{596.20}
\]

**引理 596.2。** 任意有理 CM 轨道的次数零投影在 \(A_f\) 中为挠；尖点差的投影也为挠。

**证明。** 固定一个 CM 二次域 \(K'\)。该 CM 点的定义域在 \(K'\) 上阿贝尔；完整 \(K'\)-轨道是平凡环面角色 \(\chi_T=1\) 的 toric 平均，有理轨道再与复共轭合并。中央角色平凡保证这一角色满足所需的中央相容条件。

若某个局部 \(\operatorname{Hom}_{K'_v{}^{\times}}(\pi_v,1)\) 为零，相应不变轨道泛函在 \(\pi\)-块上为零。否则对任意实际局部向量使用二重 Gross–Zagier 公式，其高度正比于

\[
 L'(f^\sigma/K',1)
 =L'(f^\sigma,1)L(f^\sigma\otimes\chi_{K'},1)
  +L(f^\sigma,1)L'(f^\sigma\otimes\chi_{K'},1)=0.
\tag{596.21}
\]

这是对真实 toric 点的配对等式，所有局部因子保留；不除以可能为零的局部积分。对自己的配对为零，Néron–Tate 正定性便使相应投影为挠。若 \(K'\) 与某个 CM 域相同，基变换的因子化仍有 (596.21)，这里的各个权二临界值无极点，结论不变。对全部实分量重复即给整个 \(A_f\) 的挠性。尖点差由 Manin–Drinfeld 给出。\(\square\)

适用的主来源是 Zhang 上述作者稿 §3.2.2，以及 Cai–Shu–Tian §2.3 的式 (2.4) 及其前面的中央角色、局部条件与任意向量规范：

<https://arxiv.org/pdf/1408.1733>

应同时采用 YZZ 勘误中的 epsilon、局部 Haar 测度及对应重数规范。本证明使用二重 toric 点高度公式，不省略另一种三重积公式的分歧修正项。

R330 已证明 \(Y=W_p\) 的相关全部模形式块有根号负，因此 \(L(f^\sigma,1)=0\)。在没有一阶非消失嵌入的块上，(596.20) 成立。结合 (596.19) 和引理 596.2，\(\eta_h\) 在这些块的投影为零，得到 (596.9)。

## 6. 秩一部分在任意水平上的秩与对数

对 \(J_H\) 的每个简单块，选择一阶导数非零的嵌入。BFH 1990 Introduction Theorem (ii) 对任意包含水平素数的有限集合 \(S\)，给虚二次 \(K_{\rm aux}\)，使所有 \(S\) 中素数分裂且 \(L(f\otimes\chi_{K_{\rm aux}},1)\ne0\)。对任何预先指定的有限个二次域，向 \(S\) 分别加入一个在该域惰性的素数，就使新辅助域与它们全部不同。因此可以选 \(K_{\rm aux}\) 不等于 \(f\) 的 CM 域；同一有限 \(S\) 扩张也严格推出无限多个可选辅助域。

split-Heegner Gross–Zagier 给非挠的完整理想类迹 \(P\)。Nekovář 的 *The Euler system method for CM points on Shimura curves* Theorem 3.2，取 \(\alpha=1\)，结合 §3.4，给

\[
 A_f(K_{\rm aux})\otimes\mathbb Q=F_fP.
\tag{596.22}
\]

该定理不是排除所有 CM；其排除的是在 \(K(\alpha)=K_{\rm aux}\) 所含二次域中取得相应 CM，已由上面的选择避开。

对 norm 为 \(N\) 的 cyclic 理想 \(\mathfrak N\)，复共轭作用把 \((\mathfrak a,\mathfrak N)\) 变为 \((\overline{\mathfrak a},\overline{\mathfrak N})\)，Fricke 则变为 \((\mathfrak a\mathfrak N^{-1},\overline{\mathfrak N})\)。完整类迹相等，基点差为 \(h_K([0]-[\infty])\) 的挠点。因此

\[
 \overline P=W_NP=-\epsilon(f)P=P
 \quad\bmod\text{挠点}.
\tag{596.23}
\]

这直接给有理非挠倍数和 \(\operatorname{rank}A_f(\mathbb Q)=\dim A_f\)，对偶水平也有效。没有把只在奇水平表述的后续命题扩用到这里。同一非挠 \(F_f\)-直线的每个实分量具有正高度，因此所有共轭的一阶导数都非零。

若实际 \(p\) 进对数在某个 \(F_f\otimes\mathbb Q_p\) 特征分量为零，就存在非零代数不变微分杀掉 \(\log_pP\)。\(p\) 进解析子群定理产生包含 \(P\) 非零倍数的真代数子群；对其 Galois 共轭取交并取连通分支，得到真 \(\mathbb Q\)-阿贝尔子簇，违反 \(A_f\) 的 \(\mathbb Q\)-单性。故实际对数为同构。对每个重数块取积，得 (596.10)。

更详细的下降、对数证明见[任意水平秩与对数接口](general-level-Heegner-rank-interface.md)，其原始来源如下：

- BFH：<https://wstein.org/papers/bib/bump-friedberg-hoffstein-nonvanishing.pdf>，Introduction Theorem (ii)，543–544 页。
- Nekovář：<https://webusers.imj-prg.fr/~jan.nekovar/pu/euler.pdf>，Theorem 3.2、§3.4。
- Cai–Shu–Tian：<https://arxiv.org/pdf/1408.1733>，split-Heegner Theorem 1.1。
- Fricke/类迹的原始公式对照：<https://link.springer.com/article/10.1007/s00208-020-02112-3>，Appendix (49)–(50)，而不是超出奇水平范围使用该文 Prop. 8。

## 7. 同一个双扩张上的高度差

保持 R593 固定的同一个全局 idèle 类角色 \(\chi\)、同一个 Poincaré 双扩张、同一个刚性化和所有 \(p\) 外的规范局部项。这里 \(h_Y\) 固定为 theta 高度极化后的双线性配对，Poincaré 对 \(\lambda_Y(Q)\) 的配对为它的两倍，正是恢复 R593 (593R.16) 的 convention。选一个与 \(J_H\) 及其同源补空间相容的 \(p\) 处规范 splitting，得到参考高度 \(h_0\)。于是由 (596.9)，

\[
 h_0(P,\eta_h)=h_0(e_HP,\eta_h).
\tag{596.24}
\]

比较原高度 \(h_Y\) 与 \(h_0\) 时，比较的是**同一个双扩张上的两个 canonical \(\chi\)-splittings**。其差下降为基底上的连续双加性函数。清除有限分支群后，局部解析群通过 \(\log_p\) 成为有限维 \(\mathbb Q_p\)-向量空间，连续加性给线性，因而存在双线性形式 \(B\) 使

\[
 h_Y(P,Q)-h_0(P,Q)=B(\log_pP,\log_pQ).
\tag{596.25}
\]

这里所有 \(p\) 外规范项相同而相消；不是把两个任意归一的全局高度直接相减。

上述 splitting、规范高度及其双线性差的接口可见 Besser–Müller–Srinivasan，Prop. 4.30、§6.3、§6.4、§6.7：

<https://arxiv.org/pdf/2112.03873>

若 \(\log_pP=0\)，则 \(\log_p(e_HP)=0\)。由 (596.10)，\(e_HP=0\) 于有理点的 \(\mathbb Q_p\)-张量中，所以 (596.24) 为零，(596.25) 也为零。这证明 (596.8)。

更明确地，对任意 \(v\in\operatorname{Lie}(J_Y)(\mathbb Q_p)\)，定义

\[
 \ell_h(v)=h_0\!\left((\log_p|_{J_H})^{-1}(e_Hv),\eta_h\right)
             +B(v,\log_p\eta_h).
\tag{596.26}
\]

它是线性的，且代入 \(v=\log_pP\) 即得 (596.11)。没有假定 \(\eta_h\) 本身为挠，也没有隐藏地假定整个 \(J_Y\) 秩等于维数。

## 8. 回到实际二次高度关系

在 R593 的真实 \(A_d\) 上另有 \(\operatorname{rank}A_d(\mathbb Q)=\dim A_d\) 及对数同构时，可以把其全局二次高度写成同一个商对数空间上的二次型 \(Q_{h,d}\)。本恢复稿采用新恢复 R593 (593R.17)–(593R.24) 的实际截面 \(s_{h,d}\)、清分母整数 \(c_{\rm clear},c_{\rm triv}\) 和同一除回因子 \(C_h=c_{\rm clear}c_{\rm triv}\)。有限集合 \(\Omega_h\) 只由这套新选定规范定义，不移植未恢复的旧数值集合；旧摘要的 \(N/M\) 字面定义和整数值不冒称已恢复。(596.11) 仅把这套实际公式中的条件线性项改为已证明的对数线性泛函。

因此其实际局部函数可写

\[
 \rho_{h,d}(x)=Q_{h,d}(\log_pj_d(x))
 +2\ell_h\!\left(\log_p[\phi_d(x)-c_{\rm base}]\right)
 -\lambda_{p,h,d}(x),
\tag{596.27}
\]

并对原有理点满足相同的 \(\rho_{h,d}(x)\in\Omega_h\)。这里 \(\lambda_{p,h,d}\) 是 R593 中对实际平凡化后的差线丛使用同一真实截面得到的局部项；不能把仅在 \(\operatorname{Pic}^0\) 中有等式的 \(\mathcal L_{h,d}\) 本身不经平凡化直接套“零局部项”引理。

在指定 \(c_{0,d}\) 的细参数 \(b\) 上，前置的甲板和对数结构使该关系保持

\[
 b^2U(b^3)+V(db^3)
\tag{596.28}
\]

的形状。\(U,V\) 的实际首项还包含 \(Q_{h,d}\)、\(\ell_h\)、局部截面的数据；本篇不由一个 Abel 积分的首项就推断二次高度函数的首项为单位或仅有一个零点。

参考 \(d=4\) 只用来计算固定 \(\eta_h\)。它没有把原候选从 \(X_1\) 的 \(c_1\) 盘运输成 \(X_d\) 的 \(c_0\) 盘，也没有提供两个不同实际商之间的固定同态；这种运输需要 R597 所单独研究的真实图式。

## 9. 完成范围及恢复依赖

本结果完成的是 R593 的固定 \(\eta_h\) 高度因子化障碍：它证明高阶解析零点部分看不到 \(\eta_h\)，并使该固定线性高度项通过实际 \(p\) 进对数因子化。全部论证保留实际极化的加权迹、同一 Poincaré 双扩张、同一 \(\chi\)、基点分母和 \(p\) 外项。

剩余实质问题包括：选定的真实 \(A_d\) 是否有足够的秩或秩零结论；非消失所选 \(\theta\) 是否与可控局部通道一致；以及同一个二次高度函数的实际首项和有限目标集合如何共同排除候选。没有把这些问题标作完成。

R593 对应于 (596.6)–(596.7) 的完整几何及新实际高度规范已恢复并经根代理核对后发布；R330、R575 同为已发布前置。原始主来源均已给精确段落，Hecke 密度和二重 Gross–Zagier 的使用范围如上，不依赖未记录的数值验证。
