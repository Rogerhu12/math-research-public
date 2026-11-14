# R28. 坏约化多分量上的范数刚性化、积分修正与显式分量群判据

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明的代数接口。** R14、R18 的无有理基点构造可延伸到约化但未必半稳定的正则模型。本文给出实际线丛的垂直修正、允许尖点除子分歧的有限平坦范数公式，以及每个分量开集上的实际积分 torsor 截面。对 $X_{\rm ns}^+(p)$，进一步从 Edixhoven–Parent 的正则模型推导全部剩余类统一的交矩阵公式，得到无需计算 Smith 标准形的分量群零类和阶判据。

**整片光滑开集的限制不能省略：** 第一变量的多度数修正为零之后，最终拉回线丛仍可能有不同的垂直系数。整个光滑开集上存在同一个积分平凡化，当且仅当这些系数相等。本文没有证明该条件对全部 Hecke 对应自动成立，也没有证明 QC 函数的共同零点排除。

有限平坦范数、Néron 恒等分量与 Picard 函子的关系、Poincaré 双扩张及积分纤维的垂直修正均已有经典和已发表文献。特别是 Edixhoven–Lido §§6.7–6.9 已处理有理基点下的一般坏约化接口。本文将这些输入与 R14、R18 的无基点范数结合，写出所需公式和全部单位性检查；不把已有原则声称为新发现。

## 1. 正则而约化的模型与交矩阵

设 $R$ 为严格 Hensel 离散赋值环，分式域 $K$ 特征零，剩余域 $k$ 代数闭，一致化参数为 $\pi$。设
$$\mathcal X\longrightarrow\operatorname{Spec}R$$
是射影、平坦、正则曲面，泛纤维 $X/K$ 光滑且几何连通，特纤维为**约化连通**曲线
$$\mathcal X_k=C_1+\cdots+C_n.$$
分量可以有奇点，分量间也可以相切；此处不假定半稳定或正规交叉。令
$$U=\mathcal X^{\rm sm},\qquad U_i=C_i\cap U.$$
每个 $U_i$ 非空且不可约，彼此不交；$\mathcal X\setminus U$ 是有限个闭点。记
$$M_{ij}=C_i\cdot C_j,\qquad L=-M,\qquad
\Lambda=\{z\in\mathbb Z^n:\sum_i z_i=0\}.$$

不同分量的交数 $w_{ij}=C_i\cdot C_j$ 非负。因 $\sum_i C_i=\operatorname{div}(\pi)$，有
$$L_{ii}=\sum_{j\ne i}w_{ij},\quad L_{ij}=-w_{ij}\ (i\ne j),\quad
z^{\mathsf t}Lz=\sum_{i<j}w_{ij}(z_i-z_j)^2.\tag{1.1}$$
交图连通，所以 $\ker(L:\mathbb Q^n\to\mathbb Q^n)=\mathbb Q\mathbf1$，且
$$\Phi_\Gamma=\Lambda/L\mathbb Z^n\tag{1.2}$$
有限。取一个正整数 $m$ 消去 $\Phi_\Gamma$；可以取其指数。约化正则模型下，Raynaud 的分量群公式将 (1.2) 识别为 Jacobian 的几何 Néron 分量群。本文需要的整数方程 $La=mz$ 也可直接由 (1.2) 的定义理解。

**引理 1（泛纤维平凡与多度数零）。** 若 $\mathscr A$ 是 $\mathcal X$ 上的线丛，$\mathscr A_K$ 平凡，且
$$\deg(\mathscr A|_{C_i})=0\quad\text{对每个 }i,$$
则 $\mathscr A$ 在整个 $\mathcal X$ 上平凡。选择一个泛纤维处处非零截面后，积分平凡化的歧义恰为 $R^\times$。

**证明。** 把泛纤维截面看成有理截面，其除子只能是 $\sum_i t_iC_i$。各多度数为 $(Mt)_i=-(Lt)_i$，故 $Lt=0$。由 (1.1)，$t=c\mathbf1$，$c\in\mathbb Z$。截面乘以 $\pi^{-c}$ 后除子为零，因正则性而成为处处非零的正则截面。两个积分平凡化的比在 $X$ 上为 $K^\times$，在每个分量的赋值为零，故为 $R^\times$。证毕。

约化假设在这里确有作用。若特纤维为 $rC$、$r>1$，则 $\mathcal O(C)$ 泛纤维平凡且多度数零，却不能由 $K^\times$ 的一个标量消去其系数 $1$；纯垂直主除子的系数只能是 $r$ 的倍数。本文不把引理 1 原样用于这种模型。

## 2. 有限平坦除子与实际线丛族

令 $D_K$ 为 $X$ 上次数 $d>0$ 的有效除子，$D\subset\mathcal X$ 为它的水平闭包，保留重数。正则性使 $D$ 为 Cartier 除子；它无垂直分量，故在每个纤维上的支集有限。于是 $D\to\operatorname{Spec}R$ 真且拟有限，从而有限；没有 $R$-挠性，又使它平坦。其次数为 $d$。允许 $D$ 分歧、非约化，并允许它通过特纤维的奇点。记
$$r_i=D\cdot C_i,\qquad r_i\ge0,\qquad\sum_i r_i=d.\tag{2.1}$$

设 $\mathscr T$ 是 $\mathcal X\times_RU$ 上的实际线丛，沿第一个曲线变量相对总次数零。对于参数点落在 $U_j$ 的纤维，记第一变量各分量的次数为
$$\delta^{(j)}=(\delta^{(j)}_1,\ldots,\delta^{(j)}_n)\in\Lambda.\tag{2.2}$$
这些次数在连通的 $U_j$ 上不变。其和为零，是因为平坦真曲线族上线丛的总次数局部常值。

这样的 $\mathscr T$ 可以从 R18 在 $X\times_KX$ 上的泛纤维线丛取来：$\mathcal X\times_RU$ 正则，因为它到 $\mathcal X$ 的投影光滑；先以 Cartier 除子表示泛纤维线丛，再闭包该除子即可延拓。这里没有把可能不正则的 $\mathcal X\times_R\mathcal X$ 当作正则模型使用。

记 $\gamma:U\to\mathcal X\times_RU$ 为对角图，$\pi_D:D\times_RU\to U$ 为有限平坦投影。定义
$$
\mathcal E_D(\mathscr T)
=(\gamma^*\mathscr T)^{\otimes d}\otimes
\operatorname{Nm}_{\pi_D}(\mathscr T|_{D\times_RU})^{-1},\tag{2.3}
$$
其中
$$\operatorname{Nm}_{\pi_D}(A)
=\det((\pi_D)_*A)\otimes\det((\pi_D)_*\mathcal O)^{-1}.$$
有限平坦性已足够定义范数，不需要 étale 性。任取 $U$ 上线丛 $H$，投影公式规范地给出
$$\mathcal E_D(\mathscr T\otimes\operatorname{pr}_U^*H)
\simeq\mathcal E_D(\mathscr T),\tag{2.4}$$
因为两因子同时多出 $H^{\otimes d}$。基底同构标量也在两因子中以相同的 $d$ 次幂出现，故在同构层面抵消。

## 3. 整数多度数修正与精确范数公式

对每个 $j$，选择整数列向量 $a^{(j)}=(a_{1j},\ldots,a_{nj})$ 使
$$La^{(j)}=m\delta^{(j)}.\tag{3.1}$$
这由 $m\Phi_\Gamma=0$ 保证，解只差一个常向量。各 $C_i\times_kU_j$ 是正则三维概形 $\mathcal X\times_RU$ 上的垂直 Cartier 素除子，故可定义
$$A=\sum_{i,j}a_{ij}(C_i\times_kU_j),\qquad
\mathscr T^\circ=\mathscr T^{\otimes m}\otimes\mathcal O(A).\tag{3.2}$$

**定理 2（实际积分修正）。** $\mathscr T^\circ$ 在所有第一变量几何纤维上具有每个分量次数零。并存在保持泛纤维自然识别的规范同构
$$
\boxed{\quad
\mathcal E_D(\mathscr T^\circ)
\simeq\mathcal E_D(\mathscr T)^{\otimes m}\otimes\mathcal O_U(B),
\quad B=\sum_j b_jU_j,
\quad b_j=d a_{jj}-\sum_i r_i a_{ij}.
\quad}\tag{3.3}
$$
右侧不依赖 (3.1) 的常向量选择，并在指定泛纤维识别之后不依赖 $\mathscr T$ 的任意积分延拓。

**证明。** 对参数 $U_j$，扭以 $\mathcal O(A)$ 后的多度数为
$$m\delta^{(j)}+Ma^{(j)}=m\delta^{(j)}-La^{(j)}=0.$$
对角图只在 $i=j$ 时遇到 $C_i\times U_j$，且相交的局部方程是 $\pi$，次数为 $1$。因而 $\gamma^*\mathcal O(A)$ 的规范有理截面之除子为 $\sum_j a_{jj}U_j$。

在 $U_j$ 的泛点处工作，其局部环为以 $\pi$ 作一致化参数的 DVR。限制 $\mathcal O(C_i)$ 的规范有理截面到有限平坦的 $D$，取范数后，其赋值为 $D\cdot C_i=r_i$。具体地，正系数的情形是有限自由模上乘法行列式的赋值等于余核长度；该长度正是 Cartier 相交数。一般整数系数由张量积及对偶得到。这证明范数因子的除子为 $\sum_j(\sum_i r_i a_{ij})U_j$，从而得到 (3.3)。这个长度证明允许 $D$ 分歧，也允许它遇到多个分量的交点。

把第 $j$ 列加上常数 $c_j$，只会使 $\mathscr T^\circ$ 乘以基底因子
$$\operatorname{pr}_U^*\mathcal O_U\Bigl(\sum_jc_jU_j\Bigr).$$
由 (2.4) 不改变 $\mathcal E_D$；也可直接用 $\sum_i r_i=d$ 检查 $b_j$ 不变。

最后，若另一延拓 $\mathscr T_1$ 在泛纤维上已与 $\mathscr T$ 识别，则二者之比的规范有理截面给出一个垂直除子
$$N=\sum_{i,j}n_{ij}(C_i\times U_j),\qquad
\mathscr T_1\simeq\mathscr T\otimes\mathcal O(N).$$
其多度数为 $\delta_1^{(j)}=\delta^{(j)}-Ln^{(j)}$。可相容地取 $a_1^{(j)}=a^{(j)}-mn^{(j)}$。这样 $\mathscr T_1^{\otimes m}\otimes\mathcal O(A_1)$ 与原 $\mathscr T^\circ$ 规范同构；任意其他解只引入已经抵消的基底因子。证毕。

## 4. 与真正的扩张 Poincaré 线丛一致：单位性证明

令 $\mathcal J$ 为 $J=\operatorname{Pic}^0_{X/K}$ 的 Néron 模型，$\mathcal J^0$ 为恒等分量；对偶记为 $\mathcal J^\vee$。令
$$a:\mathcal J^\vee\xrightarrow{\sim}\mathcal J$$
为 R14、R18 所用 Abel–Jacobi 拉回自对偶同构的 Néron 延拓。令 $\mathcal P^{\rm ext}$ 为 $\mathcal J\times_R\mathcal J^{\vee,0}$ 上的刚性化 Poincaré 双扩张。存在性与唯一性可用 Edixhoven–Lido Proposition 6.7.1。

约化正则模型的分量次数零 Picard 函子等于 $\mathcal J^0$。故 $\mathscr T^\circ$ 定义态射
$$v_m:U\longrightarrow\mathcal J^0,$$
其泛纤维是 $\mathscr T_K$ 的 Picard 类态射的 $m$ 倍。态射
$$u_D:X\longrightarrow J,\quad x\longmapsto[dx-D_K]$$
由 Néron 映射性质唯一延拓为 $u_D:U\to\mathcal J$。

**定理 3（分歧除子也适用的积分 R18）。** 存在规范同构
$$
\boxed{\quad
\mathcal E_D(\mathscr T^\circ)
\simeq(u_D,a^{-1}v_m)^*\mathcal P^{\rm ext}.
\quad}\tag{4.1}
$$
该同构在泛纤维上就是 R18 的范数刚性化同构；不存在未检查的 $\pi$ 次幂因子。

**证明。** 先在全部参数空间 $U\times_R\mathcal J^0$ 上证明。取 $b\in U(R)$；它由特纤维的一个光滑 $k$ 点和 Hensel 性得到。分量次数零 Picard 函子以 $b$ 刚性化后有实际泛线丛
$$\mathscr T_{\rm univ}\quad\text{在 }\mathcal X\times_R\mathcal J^0\text{ 上}.$$
它沿 $b$ 被刚性化，且在零截面处规范平凡。所用 Picard/Néron 识别及泛线丛构造见 Edixhoven–Lido §6.8；约化几何连通纤维保证相应的上同调平坦性。

在 $U\times_R\mathcal J^0$ 上，用评价纤维和沿 $D$ 的有限平坦范数构造 $\mathcal E_{D,\rm univ}$。沿 $U\times\{0\}$ 它规范平凡。另一方面
$$\mathscr P=(u_D\times a^{-1})^*\mathcal P^{\rm ext}$$
也在该零截面上规范平凡。R18 在泛纤维上给出二者的规范同构，且在零截面上是两个规范平凡化之间的恒等映射。这里 $D_K$ 有重数也不妨碍 R18：逐闭点取范数与重数张量幂即可。

空间 $U\times_R\mathcal J^0$ 光滑、正则，特纤维的不可约分量恰是 $U_i\times_k\mathcal J^0_k$，因为光滑连通代数群 $\mathcal J^0_k$ 不可约。泛纤维同构视为线丛 $\mathscr P\otimes\mathcal E_{D,\rm univ}^{-1}$ 的有理截面，其除子只能为
$$\sum_i t_i(U_i\times_k\mathcal J^0_k).$$
拉回到 $U\times\{0\}$，每个分量拉回为 $U_i$，系数仍为 $t_i$。但这时有理同构是恒等映射，除子为零，所以每个 $t_i=0$。正则性因此使泛纤维同构唯一延拓为处处单位的线丛同构。这正是所需的单位性检查，不能仅从泛纤维上的同构直接略过。

最后沿图 $(\mathrm{id}_U,v_m)$ 拉回。任一实际代表 $\mathscr T^\circ$ 与 $b$ 刚性化泛线丛的相应拉回只差一个基底线丛；由 (2.4) 规范消去该因子，得到 (4.1)。换 $b$ 同样不改变结果。证毕。

这个证明与 Edixhoven–Lido Proposition 6.8.7 的“泛纤维范数同构加零截面刚性化”原则一致；它专门核实了当前 $d\gamma-D$ 表达式在非 étale 的 $D$ 上也成立。使用 Deligne 配对亦得到同一式，但无需另行假设范数的分歧处单位性。

## 5. 真正的积分 torsor 截面以及整片 $U$ 的剩余条件

现在假设 R14 的条件使 $\mathcal E_D(\mathscr T)_K$ 平凡，并已选取一个泛纤维处处非零截面 $s$。注意，这里要求的确是平凡化截面；任意有理截面不够。把 $s$ 看作 $U$ 上的有理截面，记
$$\operatorname{div}_U(s)=\sum_j n_jU_j.$$
在 (3.3) 的泛纤维自然识别下，$s^{\otimes m}$ 成为 $\mathcal E_D(\mathscr T^\circ)$ 的有理截面，其除子为
$$\sum_j k_jU_j,\qquad k_j=mn_j+b_j.\tag{5.1}$$

**定理 4（精确归一化与粘合判据）。**

1. 对每个 $j$，令
   $$U^{(j)}=U\setminus\bigcup_{i\ne j}U_i.$$
   则 $\pi^{-k_j}s^{\otimes m}$ 在 $U^{(j)}$ 上是 (4.1) 的实际积分、处处非零截面，给出到 $(\mathcal P^{\rm ext})^\times$ 的提升。
2. 整个 $U$ 上存在一个积分处处非零截面，当且仅当
   $$k_1=\cdots=k_n.\tag{5.2}$$
   同一个条件也等价于该线丛向 $\mathcal X$ 的唯一线丛延拓具有每个分量次数零。

**证明。** $U^{(j)}$ 的唯一垂直分量是约化的 $U_j$，即 $\operatorname{div}(\pi)$，故第 1 点直接由 (5.1) 消去除子。对不同的 $i,j$，两个截面在共同泛纤维上的比为 $\pi^{k_j-k_i}$。

若 (5.2) 成立，统一乘以 $\pi^{-k_1}$ 即可在整个 $U$ 平凡化。反之，任何全 $U$ 平凡化与 $s^{\otimes m}$ 的比，限制到完整泛纤维 $X$ 后都是 $K^\times$，其沿全部约化分量的赋值相同，故只能消去一个常向量。

正则曲面除去有限个闭点不改变 Picard 群：线丛可用 Cartier 除子表示，除子的闭包存在且唯一，主除子的关系也不改变。因此该线丛唯一延拓到 $\mathcal X$，并由 $\sum_jk_jC_j$ 表示，其多度数为 $-Lk$。由 (1.1)，$-Lk=0$ 当且仅当 $k$ 常值。这也与引理 1 一致。证毕。

第一变量的 $\delta^{(j)}$ 被消去与最终的 $k_j$ 相等是两个不同断言。定理 2 只保证前者；定理 4 没有把后者当作自动后果。对 R18 的实际对应族 $\mathscr T_D$，取 $m(h_Du_D)$ 进入对偶 Néron 恒等分量，并用上述式子归一化，仍需计算或控制 (5.1) 的剩余向量才能在整个 $U$ 粘合。

上述构造也可从严格 Hensel 基底下降。对原 DVR 上的数据，先作严格 Hensel 基变换；任意 Galois 共轭的列解只差一个常向量，所以 $b_j$ 随分量置换相容。更内在地，(4.1) 右侧及其刚性化已在原基底上定义，且泛纤维同构的单位延拓唯一，故规范下降。这里不需要乘上分裂特纤维的非分歧扩张次数；也不声称任意非 Hensel DVR 的所需截面必然在某个有限 étale 覆盖上存在。

## 6. 非分裂 Cartan 曲线的统一交矩阵

取 $p\ge17$，令 $\mathcal X$ 为 $X_{\rm ns}^+(p)$ 在 $\mathbb Z_p^{\rm ur}$ 上的最小正则模型。Edixhoven–Parent (2024), Corollary 3.2 给出其特纤维约化，分量由超奇异 $j$ 不变量标记。不要把它与 Theorem 3.4 的正规交叉模型混淆：后者通常不约化，二者之间要收缩分量。

对保留的分量 $C_i$，定义
$$e_i=\begin{cases}
3,&j_i=0,\\
2,&j_i=1728,\\
1,&j_i\ne0,1728,
\end{cases}\qquad q_i=\frac1{e_i}.$$
只给实际超奇异的例外 $j$ 赋予对应的 $e_i$。从各 $p\bmod12$ 的超奇异个数可直接验得
$$\sum_iq_i=\frac{p-1}{12}.\tag{6.1}$$

**定理 5（全部剩余类的交矩阵）。** 最小正则模型的交矩阵为
$$
\boxed{\quad M=-(p-1)\operatorname{diag}(q_i)+12qq^{\mathsf t}.\quad}\tag{6.2}
$$
特别地，不同分量交数是 $12/(e_ie_j)$，对角线由行和零确定。对于任意 $z\in\Lambda$，整数向量
$$a_i=e_i z_i\tag{6.3}$$
满足
$$La=(p-1)z.\tag{6.4}$$

**证明。** 以下只使用 Edixhoven–Parent Theorem 3.4 明确给出的正规交叉树及 Corollary 3.2 的收缩。写 $p=12k+\epsilon$，$\epsilon\in\{1,5,7,11\}$，中央 Igusa 分量为 $A$，重数 $N=(p-1)/2$。

每个非例外超奇异点的支链有 $A$ 邻接 $D_i$，$D_i$ 再邻接 $E_i,F_i$，三者重数分别为 $p+1,(p+1)/2,1$。超奇异 $j=0$ 支链同形，但重数为 $(p+1)/3,(p+1)/6,1$。超奇异 $j=1728$ 支链只有重数 $1$ 的 $F_i$ 与 $A$ 相邻。如果 $j=0$ 是普通点，另有链 $A-B-C$，后两重数为 $(p-1)/3,(p-1)/6$。树上相邻分量交数为 $1$。最后保留的恰是各 $F_i$。

交矩阵对纤维重数向量的乘积为零，所以这些重数和邻接关系给出全部自交数。非例外链有
$$D_i^2=-1,\quad E_i^2=-2,\quad F_i^2=-(p+1);$$
超奇异 $j=0$ 链有
$$D_0^2=-2,\quad E_0^2=-2,\quad F_0^2=-(p+1)/3;$$
超奇异 $j=1728$ 有 $F_i^2=-N$；普通 $j=0$ 链有 $B^2=C^2=-2$。中央分量在四种剩余类中均为 $A^2=-(2k+1)$，代入各邻居重数即可核验。

收缩后的交矩阵是对被收缩块作 Schur 补：若原矩阵按保留与收缩分量分块为
$$\begin{pmatrix}P&Q\\Q^{\mathsf t}&S\end{pmatrix},$$
则目标矩阵是 $P-QS^{-1}Q^{\mathsf t}$。其原因是目标 Cartier 除子的总拉回与每个被收缩分量交数零，故其被收缩部分系数为 $-S^{-1}Q^{\mathsf t}$；代回计算交数即得此式。可逐块计算 Schur 补，不要求每个中间有理矩阵都对应一项实际收缩。

先在非例外链消去 $E_i$，使 $D_i$ 的有效自交变为 $-1/2$，再消去 $D_i$。结果使 $A^2$ 增加 $2$，留下有效交数 $A\cdot F_i=2$ 和 $F_i^2=-(p-1)$。对超奇异 $j=0$ 链，同样消去 $E_0,D_0$，有效自交依次为 $-3/2$；结果使 $A^2$ 增加 $2/3$，并留下 $A\cdot F_0=2/3$、$F_0^2=-(p-1)/3$。超奇异 $j=1728$ 无中间分量，已经有 $A\cdot F_i=1$、$F_i^2=-(p-1)/2$。

若存在普通 $j=0$ 链，消去 $C,B$ 使 $A^2$ 增加 $2/3$。非例外超奇异点数为 $k$，且普通或超奇异的 $j=0$ 恰有一种。因此所有这些支链消去后，$A^2$ 总变为
$$-(2k+1)+2k+\frac23=-\frac13.$$
剩余矩阵中 $A\cdot F_i=2/e_i$，不同 $F_i$ 尚无直接交数，且 $F_i^2=-(p-1)/e_i$。最后消去 $A$，增加的秩一矩阵为
$$3\bigl(2/e_i\bigr)_i\bigl(2/e_i\bigr)_i^{\mathsf t}=12qq^{\mathsf t}.$$
这证明 (6.2)。对 $a_i=e_i z_i$，有 $q^{\mathsf t}a=\sum_i z_i=0$，直接代入 $L=-M$ 即得 (6.4)。证毕。

例如 $p=12k+5$，把 $j=0$ 分量放首位，得到 $M_{00}=-4k$、$M_{0i}=4$、$M_{ii}=13-p$、$M_{ij}=12$（$i,j>0$ 且 $i\ne j$），与 Edixhoven–Parent Corollary 3.2 证明中列出的矩阵逐项相同。

## 7. 不用 Smith 标准形的精确分量群判据

**推论 6。** 对上述模型及 $z\in\Lambda$：

1. $[z]=0$ 在 $\Phi_\Gamma$ 中，当且仅当全部 $e_i z_i$ 模 $p-1$ 同余。
2. 其阶为
   $$\operatorname{ord}([z])=
   \frac{p-1}{\gcd\bigl(p-1,\{e_i z_i-e_j z_j: i,j\}\bigr)}.\tag{7.1}$$
3. 临界群的非退化对称配对可明确写成
   $$\langle[z],[w]\rangle_\Gamma=
   \frac{\sum_i e_i z_iw_i}{p-1}\pmod{\mathbb Z}.
   \tag{7.2}$$
   这里以正的 $L=-M$ 固定配对符号；采用另一种 Néron 单值配对符号约定时相差一个负号。

**证明。** 根据 (6.4)，$La=z$ 的一个有理解是 $a_i=e_i z_i/(p-1)$，全部有理解与它只差一个常向量。存在整数解，当且仅当这些坐标之差都是整数，正是第 1 点。对 $tz$ 应用第 1 点，即得最小正整数 $t$ 的公式 (7.1)。

式 (7.2) 是 $a^{\mathsf t}w$。改变 $a$ 的常数不影响它；把 $z$ 改为 $z+Lu$ 使其增加 $u^{\mathsf t}w\in\mathbb Z$。对称性从显示式直接得到，也保证第二变量下降。若它对全部 $w\in\Lambda$ 为零，取 $w$ 为两个坐标单位向量之差，便得全部 $e_i z_i$ 模 $p-1$ 同余，故 $[z]=0$。证毕。

因此在定理 2 中可以统一取
$$m=p-1,\qquad a_{ij}=e_i\delta_i^{(j)},\qquad
\boxed{\ b_j=d e_j\delta_j^{(j)}-\sum_i r_i e_i\delta_i^{(j)}.\ }\tag{7.3}$$
这是一个实际整数公式，适用于全部四种 $p\bmod12$。若只需处理若干给定列向量，还可用 (7.1) 求它们阶的最小公倍数作为更小的 $m$，再以
$$a_{ij}=\frac{m}{p-1}\bigl(e_i\delta_i^{(j)}-e_{i_0}\delta_{i_0}^{(j)}\bigr)$$
选择第 $i_0$ 行为零的整数解。式 (7.1) 保证整数性。

这也直接证明分量群指数整除 $p-1$。Edixhoven–Parent Proposition 3.2 的完整群结构进一步给出：$p>19$ 时指数等于 $p-1$，$p=17$ 时为 $4$，$p=19$ 时为 $6$。这里不把这两个小素数的指数误写为 $p-1$。

## 8. 在本课题中的作用与尚未得到的结论

取 $D_K$ 为全部尖点之和，$d=(p-1)/2$。在坏素数 $p$ 的最小正则模型上，它的水平闭包是有限平坦 Cartier 除子，已经足以适用全文；不需要声称尖点在 $p$ 处有限 étale。使用 R18 的实际对应族和 R14 的泛纤维平凡化，式 (7.3)、(5.1) 给出每个分量开集上的实际积分提升，且无 $d$ 次根选择、无额外分裂域次数乘子。

这完成了无基点构造的坏约化代数接口，并使所需的第一变量分量修正可以从交数直接计算。以下事项仍是额外数学问题：实际对应族的多度数及尖点交数的有效计算、泛纤维平凡化截面的有效表示、剩余 $k_j$ 是否相等、Mordell–Weil 的积分指数，以及包括局部高度项在内的真实 QC 共同根排除。仅有分量群指数或规范 torsor，并不能推出 Serre 一致性。

## 9. 已核对的原始文献

- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058, DOI [10.4171/DM/974](https://doi.org/10.4171/DM/974)。[期刊全文](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。Theorem 3.4（pp. 1038–1039）给正规交叉树；Corollary 3.2（p. 1042）及其证明（p. 1044）给约化最小正则模型和收缩；Proposition 3.2（pp. 1044–1045）给分量群。本文 (6.2)–(7.3) 已从该树直接展开计算，并未把未写出的矩阵当作引文。
- B. Edixhoven and G. M. Lido, **Geometric quadratic Chabauty**, *Journal of the Institute of Mathematics of Jussieu* **22** (2023), 279–333；在线发表 2021；DOI [10.1017/S1474748021000244](https://doi.org/10.1017/S1474748021000244)。[作者版本 arXiv:1910.10752](https://arxiv.org/abs/1910.10752)。§§6.1–6.2 的范数与相对 Cartier 除子允许有限平坦而非 étale；Proposition 6.7.1 是 Poincaré 双扩张延拓；§6.8 与 Proposition 6.8.7 是 Picard/Néron 识别及范数计算；Proposition 6.9.3 是整数格的垂直修正。本文采用同一标准背景，并逐项证明当前无基点公式。
- S. Bosch, W. Lütkebohmert and M. Raynaud, **Néron Models**, Springer (1990), Chapter 9, §5 Theorem 4、§6 Corollary 3。这些是上面已发表论文明确引用的 Picard/Néron 与分量群公式来源；本文的图线性代数和所有新增公式已给出完整证明。
