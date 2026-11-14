# R59. 全局局部类型分解、环面二次扭曲与真实零坏高度方向

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 设 $p>37$，$J=J_{\rm ns}^+(p)$。本文把 R57 的单值分次公式接到全局 Hecke 因子的实际局部类型，得到：

1. $J$ 的潜在全环面 Hecke 因子，恰来自 level-$p$ 权二新形式按 $\chi_p=(\frac{\cdot}{p})$ 的二次扭曲；这一部分出现在 $J_{\rm ns}^+(p)$ 中当且仅当 $p\equiv1\pmod4$。其 Hecke 代数与 level-$p$ 代数的识别为 $T_q\mapsto\chi_p(q)T_q$，不是普通的同名 $T_q$。
2. 全局 principal-series 因子恰贡献 Igusa 分量的中间上同调；全局 supercuspidal 因子恰贡献 Drinfeld 分量的中间上同调。它们是由完整 Galois 轨道选出的有理 Hecke 幂等元，不是假设局部投影能提升。
3. 任意通过 Heegner 商的 principal-series 部分、且 trace-zero 的有理 Hecke 方向，其真实 $\Phi_A$ 为零。这在全部几何坏分量上成立，强于只对 $\mathbb Q_p$ 可达分量的点值消失。
4. 对所有 $p>37$，给出由真实 Drinfeld 部分迹及环面图项组成的统一差值公式；它把核及秩的计算准确降到 supercuspidal 与环面部分。一般层的部分迹矩阵尚未求出，本文不声称已经求得所有层的数值秩。

## 1. 三种类型都是全局 Hecke 因子的性质

由 R45，
$$J\sim_{\mathbb Q}\prod_{[f]}A_f,\qquad
\mathbb T_{\mathbb Q}=\prod_{[f]}K_f,\qquad
\dim A_f=[K_f:\mathbb Q],
\tag{1.1}$$
其中 $f$ 遍历 $S_2(\Gamma_0(p^2))^{+,{\rm new}}$ 的完整 Galois 轨道。

在 $p$ 处，Edixhoven–Parent 的半稳定模型在一个分歧度整除 $p^2-1$ 的驯分歧扩域上存在。故对应 Weil–Deligne 表示的有限惯性部分为循环群的作用，野惯性平凡。对每个新形式的二维表示写为 $(\rho_f,N_f)$。惯性上的行列式为 $1$。

Carayol, Theorem (A), pp.410–411，将这些表示与局部自守表示相容地识别；其 §0.5–§0.6 还给系数域自同构相容性。下面的分类可直接在二维 Weil–Deligne 表示中看出。

- 若 $N_f\ne0$，有限惯性必须为标量字符 $\alpha$，且 $\alpha^2=1$。非分歧的 $\alpha$ 会给 conductor exponent $1$，与 $p^2$-new 矛盾；所以 $\alpha$ 是非平凡驯二次字符。这正是分歧二次字符扭曲的 Steinberg 型。
- 若 $N_f=0$，有限惯性特征为 $\alpha,\alpha^{-1}$。$\alpha=1$ 与 conductor exponent $2$ 矛盾。$\alpha$ 为二次字符的情形也不发生：全局扭曲 $\chi_p$ 后所有有限素数都非分歧，将得到一个 level-$1$ 的权二新形式，而 $S_2(\operatorname{SL}_2(\mathbb Z))=0$。
- 因此在 $N_f=0$ 时 $\alpha^2\ne1$。Frobenius 将惯性字符送到其 $p$ 次幂，故必有 $\alpha^p=\alpha$ 或 $\alpha^p=\alpha^{-1}$。前者的字符阶整除 $p-1$，给 principal series；后者的阶整除 $p+1$，给 supercuspidal。两种情况不重合，因为 $\gcd(p-1,p+1)=2$。

这里使用的 conductor 和扭曲规则可逐项核对 Loeffler–Weinstein (2012), Table 1、§2.3：principal series 的 conductor exponent 是两个字符 conductor exponent 之和；$\mathrm{St}\otimes\nu$ 的 conductor exponent 是 $\max(1,2a(\nu))$；全局新形式扭曲对应各局部分量同时扭曲。

系数域共轭把有限阶字符换成其与阶互素次幂，保持上述分类，并保持 $N_f$ 是否为零。所以三种集合都是完整全局 Galois 轨道的并，定义有理 Hecke 幂等元
$$e_{\rm tor}+e_{\rm ps}+e_{\rm sc}=1,\qquad e_i e_j=0\ (i\ne j),
\tag{1.2}$$
以及同源因子 $J_{\rm tor},J_{\rm ps},J_{\rm sc}$。这些幂等元来自 (1.1)，定义于 $\mathbb Q$，并在 R45 的 Rosati 对称 Hecke 代数内。

## 2. 环面部分恰为 level-$p$ 的二次扭曲

### 定理 1

当 $p\equiv1\pmod4$ 时，
$$J_{\rm tor}\sim_{\mathbb Q}J_0(p)^{\chi_p},
\tag{2.1}$$
这里右侧是按 $\chi_p$ 的二次扭曲。在相应有理 Hecke 代数之间有一个同构
$$\iota_{\rm tor}:e_{\rm tor}\mathbb T_{\mathbb Q}
\xrightarrow{\sim}\mathbb T_{0}(p)_{\mathbb Q},
\qquad
\iota_{\rm tor}(e_{\rm tor}T_q)=\chi_p(q)T_q
\quad(q\ne p).
\tag{2.2}$$
当 $p\equiv3\pmod4$ 时，$J_{\rm tor}=0$。

**证明。** 若 $f$ 为第 1 节的 Steinberg 型，则
$$\pi_{f,p}=\mathrm{St}\otimes\nu,\qquad
\nu|_{\mathbb Z_p^\times}=\chi_p|_{\mathbb Z_p^\times}.
$$
全局新形式 $g=f\otimes\chi_p$ 在 $p$ 处为非分歧字符扭曲的 Steinberg，conductor exponent 为 $1$；其他有限素数处仍非分歧。因此 $g$ 是平凡特征、权二、level-$p$ 新形式。

反过来，任意 level-$p$ 权二新形式 $g$ 在 $p$ 处是非分歧 Steinberg 型。$f=g\otimes\chi_p$ 的 conductor 恰为 $p^2$，仍有平凡中心特征。它的有限 $\operatorname{GL}_2(\mathbb F_p)$ 类型是 twisted Steinberg $V_\omega$：Steinberg 的主同余不变量是有限 Steinberg 表示，扭曲在有限群上就是 $\omega\circ\det$。

Mercuri–Schoof (2020), Proposition 3.2(c) 明确给
$$\dim V_\omega^{N_{\rm ns}}=
\begin{cases}1,&p\equiv1\pmod4,\\0,&p\equiv3\pmod4.\end{cases}
$$
结合其 Proposition 5.2、§6 的 Hecke 相容实现，以及 R45 的 Chen 同源，这正好判定 $f$ 是否贡献 $J_{\rm ns}^+(p)$。因此第一种剩余类中所有 level-$p$ 新形式的二次扭曲都出现，第二种中全部不出现。

扭曲是对合，在 $q\ne p$ 有
$$a_q(f)=\chi_p(q)a_q(g).
\tag{2.3}$$
它保持系数域：两边的非分歧 Hecke 特征值互相用有理数 $\pm1$ 恢复，而 level-$p$ 的 $a_p(g)=\pm1$ 不增加系数域。故按 Galois 轨道的积给 (2.2)。

同时，$A_f$ 与 $A_g^{\chi_p}$ 的 Tate 模系统在几乎所有素数的特征多项式相同；Faltings 同源定理给相应全局同源。对全部轨道取积得到 (2.1)。这些因子在消去二次惯性后完全环面，与 R57 引理 1 及单值分次上的 $e_{\rm tor}$ 完全一致。证毕。

这个结论精确指出谱比较中应出现的二次符号。若使用 level-$p$ 的经典 Brandt 实现来表示此 Hecke 模，所用算子必须是 $\chi_p(q)$ 倍的相应 Brandt 算子。

但 (2.2) 本身没有识别某一个 Drinfeld 路径评价向量与 Brandt 模块的某一个标准基向量。后面的 $Q_j$ 涉及这些具体向量及单值长度配对，仍须保持实际几何定义；不能借一个抽象模同构就忽略这一步。

## 3. 惯性把 Igusa 与 Drinfeld 上同调严格分开

令 $C=\mathbb F_{p^2}^{\times}$ 表示 Edixhoven–Parent §2.2.4 使用的有限驯惯性覆盖群；实际作用可以经过其商。令
$$C^1=\ker\bigl(N_{\mathbb F_{p^2}/\mathbb F_p}\bigr)=\mu_{p+1}.
\tag{3.1}$$
该文 (12)–(13)，pp.243–244，给 $C^1$ 在所有原 Igusa 分量上平凡；商到非分裂正规化子模型后仍平凡。

### 引理 2

在每个 Drinfeld 分量 $D_j$ 的 $H^1$ 上，$C^1$ 的不变量为零。

**证明。** 对一般 $j$，Theorem 3.5 给曲线
$$D:Y^2=X(X^m+a),\qquad m=\frac{p+1}{2},\quad a\ne0.
\tag{3.2}$$
有限惯性在这些坐标中有形式
$$X\longmapsto u^{2(p-1)}X,\qquad
Y\longmapsto u^{p-1}Y.
\tag{3.3}$$
当 $u\in C^1$，置 $\xi=u^{-2}$，则 $\xi$ 遍历 $\mu_m$，作用为
$$X\longmapsto\xi^2X,\qquad Y\longmapsto\xi Y.
\tag{3.4}$$

若 $m$ 为偶数，(3.4) 包含超椭圆对合 $(X,Y)\mapsto(X,-Y)$。其商为 $\mathbb P^1$，故整个 $\mu_m$ 的商亦为亏格零。

若 $m$ 为奇数，取不变量
$$t=X^m,\qquad z=\frac{Y^m}{(X^m+a)^{(m-1)/2}}.$$
它们满足
$$z^2=t(t+a).
\tag{3.5}$$
由 $Y^2=X(t+a)$ 得 $X=Y^2/(t+a)$，并且 $Y^m=z(t+a)^{(m-1)/2}$。因此原函数域在 $\mathbb F_p(t,z)$ 上次数至多 $m$；群作用忠实且阶为 $m$，所以这就是不变量域。(3.5) 的光滑射影模型为亏格零曲线。

作用的阶素于 $p$，故 $H^1(D)^{C^1}$ 等于商曲线的 $H^1$，于是为零。特殊 $j=0$ 的 Drinfeld 曲线由一般方程再商掉额外的阶三自同构而得，该自同构与惯性交换；其 $H^1$ 嵌入一般方程的 $H^1$，仍无 $C^1$ 不变量。$j=1728$ 的 Drinfeld 分量为 $\mathbb P^1$，其 $H^1$ 本来为零。证毕。

### 定理 3

在半稳定单值分次中有
$$\begin{aligned}
e_{\rm ps}\operatorname{gr}_1^M H^1
&=\bigoplus_{\text{Igusa }I}H^1(I),\\
e_{\rm sc}\operatorname{gr}_1^M H^1
&=\bigoplus_{\text{Drinfeld }D_j}H^1(D_j),\\
e_{\rm tor}\operatorname{gr}_1^M H^1&=0.
\end{aligned}\tag{3.6}$$
此外 $e_{\rm tor}$ 在两个图同调分次上为恒等，而 $e_{\rm ps},e_{\rm sc}$ 在它们上为零。

**证明。** 第 1 节的 principal-series 惯性字符通过范数 $C\to\mathbb F_p^\times$，所以在 $C^1$ 上平凡。supercuspidal 惯性字符的阶整除 $p+1$ 而大于 $2$，其在 $C^1$ 上不平凡：如果同时通过范数，其阶也整除 $p-1$，只能是 $1$ 或 $2$，矛盾。因此这些二维 supercuspidal 表示在 $C^1$ 上无不变量。

两种类型的 $N_f=0$，获得好约化后全部上同调在中间分次。Igusa 部分在 $C^1$ 上平凡，Drinfeld 部分由引理 2 无不变量，故正好分别由上述两种全局因子填满。剩下的 Steinberg 型是完全环面型，由 R57 引理 1 给中间分次为零、两个图分次为恒等。证毕。

特别地
$$\dim J_{\rm ps}=\sum_Ig(I),\qquad
\dim J_{\rm sc}=\sum_jg(D_j).
\tag{3.7}$$
例如 $p\equiv5\pmod {12}$ 时，EP 的亏格公式给
$$\dim J_{\rm tor}=\frac{p-5}{12},\quad
\dim J_{\rm ps}=\frac{(p-5)(p-17)}{48},\quad
\dim J_{\rm sc}=\frac{(p-5)(p+3)}{48}.
\tag{3.8}$$
在 $p=41$，这些维数分别为 $3,18,33$，相加为 $54$。这是完整 Jacobian 的类型分解；一般 Heegner 商在各类型中的维数仍取决于真正的导数非消失。

## 4. 所有层的实际坏分量差值公式

记
$$a_j=\begin{cases}1,&j\ne0,1728,\\3,&j=0,\\2,&j=1728,\end{cases}
\qquad d=\frac{p-1}{2}.
$$
只对确实超奇异的标号使用相应项。对任意 trace-zero、Rosati 对称的实际有理 Hecke 方向 $G$，定义
$$\tau_j(G)=\operatorname{Tr}
\bigl(P_{D_j}G\mid\operatorname{gr}_1^M H^1\bigr).
\tag{4.1}$$
它是分量的部分迹，不要求 $G$ 单独保持 $H^1(D_j)$。

这些部分迹为有理数：在半稳定 Néron 恒等分量的阿贝尔商中，$G$ 诱导真正的有理端同态，而该阿贝尔商规范同源于各分量 Jacobian 的积；投影后得到分量 Jacobian 的有理端同态，其 $H^1$ 迹为有理数。图项亦来自有理图同调和有理长度配对。

当 $p\equiv1\pmod4$，定义 $Q_j(G)$ 如 R57 §4.1：
$$Q_j(G)=\langle e_j,G_\Gamma\pi(e_j)\rangle,
\tag{4.2}$$
其中 $e_j$ 是两 Igusa 顶点之间第 $j$ 条路径的任意半边，边长为 $4a_j/(p^2-1)$。当 $p\equiv3\pmod4$，置 $Q_j(G)=0$。

### 定理 4：统一差值公式

令
$$\Xi_j(G)=a_j\tau_j(G)+\frac{p^2-1}{2}Q_j(G).
\tag{4.3}$$
则 R43 的实际垂直系数满足
$$\boxed{\quad
k_j(G)-k_i(G)
=-\frac{p-1}{p+1}\bigl(\Xi_j(G)-\Xi_i(G)\bigr).
\quad}\tag{4.4}$$

**证明。** 若 $p\equiv1\pmod4$，EP Theorem 3.5 的图有两个 Igusa 顶点。R57 (4.5)–(4.6) 的推导只用两条等长半边，因此同样适用于 $p\equiv1\pmod {12}$；代入半边长度 $L_j=4a_j/(p^2-1)$ 和 $d=(p-1)/2$ 即得 (4.4)。

若 $p\equiv3\pmod4$，EP 图为一条 Igusa 中央顶点 $I$ 和 Drinfeld 叶顶点 $D_j$ 的树。唯一边的长度为
$$L_j=\frac{a_j}{(p^2-1)/2}=\frac{2a_j}{p^2-1}.
$$
图同调为零，故边上高度为仿射函数。使用 R57 (3.6) 的 Laplacian 符号，在叶顶点有
$$\widehat h_G(D_j)-\widehat h_G(I)=L_j\tau_j(G).
$$
于是
$$k_j(G)-k_i(G)
=-2d^2\bigl(L_j\tau_j(G)-L_i\tau_i(G)\bigr),
$$
代入 $L_j$ 即得 (4.4)。

一般标号和 $j=0$ 的未分歧末端，仍按 EP (2024) 的实际坐标 $y/p^{1/(p+1)}$、$Y/p^{3/(p+1)}$ 特化到相应 Drinfeld 光滑原点，完全同 R57 §5。$j=1728$ 只发生在本树情形，Drinfeld 分量为亏格零，$\tau_{1728}=0$；其整条叶边上的高度因此恒等于中央值。无论先保留还是收缩这条不稳定有理尾，它上面的点及其收缩像都有同一值。R55 的该标号末端来自同一特殊支链，故比较亦有效。

归一化始终用 $v_p(p)=1$、交数除以分歧度，并由 R43 比较 $k$ 与 $-2d^2\widehat h$。所以这里未改变乘二、符号或全部尖点除子的度数。证毕。

## 5. 真正 Heegner 商中的 principal-series 零高度核

令 $A$ 为 R45 按 $L'(f,1)\ne0$ 选取的真实商，置
$$A_i=e_iA,\qquad a_i=\dim A_i,\qquad
\mathbb T_{A,i}=e_Ae_i\mathbb T_{\mathbb Q}
\quad(i={\rm tor,ps,sc}).
$$
所有投影仍是全局有理 Hecke 投影。记
$$W_A=\ker\bigl(\operatorname{Tr}_A:\mathbb T_A\to\mathbb Q\bigr),
\qquad
W_{A,\rm ps}=\ker\bigl(\operatorname{Tr}_{A_{\rm ps}}:
\mathbb T_{A,\rm ps}\to\mathbb Q\bigr).
$$

### 定理 5

有
$$W_{A,\rm ps}\subseteq\ker(\Phi_A\otimes\mathbb Q).
\tag{5.1}$$
因此 $\Lambda_A\cap W_{A,\rm ps}$ 是一个秩 $\max(a_{\rm ps}-1,0)$ 的真实容许整数格，其所有方向在全部几何坏分量上具有常局部高度。归一化后，它们是 R47–R49 的真实零非辅助局部项方程方向。

**证明。** 对 $G\in W_{A,\rm ps}$，定理 3 给 $G_\Gamma=0$，且 $G$ 在全部 Drinfeld 中间分次上为零。因此每个 $\tau_j(G)=0$、$Q_j(G)=0$。由 (4.4)，全部 $k_j(G)$ 相同，即 (5.1)。

$G$ 已消去 $A$ 的互补因子，trace 也为零，所以 R45 只需清除同源、实际对应以及 Chow–Heegner 挠点的有限分母，即进入其满秩容许格。与 $W_{A,\rm ps}$ 相交仍为满格。R43 把常 $k$ 变为常坏高度；沿 R47 的共同归一化，所有非辅助项为零。R49 的独立性适用于其中任意独立方向。证毕。

这项结论使用的是实际单值分次上的**消去**，而非两个不相交谱之间未经证明的映射。它也没有声称每个 principal-series 因子必属于 $A$：$a_{\rm ps}$ 只计算已经证明导数非消失的因子。

## 6. 核及秩准确降到 Drinfeld 与环面数据

设
$$\mathbb T_{A,\rm rem}
=\mathbb T_{A,\rm sc}\oplus\mathbb T_{A,\rm tor}.
$$
定理 3 使 (4.3) 的右侧在 $\mathbb T_{A,\rm ps}$ 上恒零，因此可对整个 $\mathbb T_{A,\rm rem}$ 定义线性映射
$$L_A:\mathbb T_{A,\rm rem}\longrightarrow\mathbb Q^{n-1},
\qquad
H\longmapsto\bigl(\Xi_j(H)-\Xi_{j_0}(H)\bigr)_{j\ne j_0}.
\tag{6.1}$$
这里即使 $H$ 单独不是 trace-zero，其图作用和部分迹也有定义。只有把它放回总 trace-zero 方向后，才应用局部高度公式。

### 定理 6：有 principal-series 部分时的确切分解

若 $a_{\rm ps}>0$，记 $e_{A,\rm ps}=e_Ae_{\rm ps}$。则
$$\boxed{\quad
\ker(\Phi_A\otimes\mathbb Q)
=W_{A,\rm ps}\oplus
\left\{H-\frac{\operatorname{Tr}_A(H)}{a_{\rm ps}}e_{A,\rm ps}
:H\in\ker L_A\right\},
\quad}\tag{6.2}$$
并且
$$\operatorname{rank}\Phi_A=\operatorname{rank}L_A.
\tag{6.3}$$
对 R55 的真正 $\mathbb Q_p$ 点值核，同样的结论成立，只须把 (6.1) 的行限制到 $j\in S_p\setminus\{j_0\}$。

**证明。** 每个 $F\in W_A$ 唯一写为 $F=P+H$，其中 $P\in\mathbb T_{A,\rm ps}$、$H\in\mathbb T_{A,\rm rem}$，且
$$\operatorname{Tr}(P)=-\operatorname{Tr}(H).$$
因此
$$F=P_0+
\left(H-\frac{\operatorname{Tr}(H)}{a_{\rm ps}}e_{A,\rm ps}\right),
\qquad P_0\in W_{A,\rm ps}.
$$
定理 5 消去 $P_0$；定理 4 对第二项的系数差给恰为 $-(p-1)/(p+1)$ 倍 $L_A(H)$。所以其属于核当且仅当 $H\in\ker L_A$。直和性来自两个不同的 Hecke 因子，得到 (6.2)。映射 $W_A\to\mathbb T_{A,\rm rem}$ 为满射，非零比例因子不改变秩，故得 (6.3)。限制可达行的证明相同。证毕。

若 $a_{\rm ps}=0$，则直接把 (6.1) 限制到 $\mathbb T_{A,\rm rem}$ 的 trace-zero 超平面；不得使用 (6.2) 中的除法。

在 $p\equiv3\pmod4$ 时环面项完全没有，因此 $L_A$ 只需真正的加权 Drinfeld 部分迹：
$$L_A(H)=
\bigl(a_j\tau_j(H)-a_{j_0}\tau_{j_0}(H)\bigr)_{j\ne j_0}.
\tag{6.4}$$
在 $p\equiv1\pmod4$ 时，环面 Hecke 子代数已由定理 1 确定为二次扭曲的 level-$p$ 子代数，但路径上的 $Q_j$ 仍应使用实际长度配对。

## 7. 现在能算什么，尚不能声称什么

公式 (6.1)–(6.4) 是精确的秩与核判据：选取实际 Hecke 基，计算其规范单值分次作用，即得一个有限有理矩阵，其秩就是 $\Phi_A$ 的秩，且整数核通过 R48 的饱和处理。相比 R33 的范数与对角交数描述，这里已把所有 principal-series 因子从计算中实际消去，并确定环面因子的全局扭曲来源。

一般层的 Drinfeld 部分迹矩阵尚未在本课题中算出。一个可继续的具体接口是：用 $p$ 处的超奇异椭圆曲线及其同源的剩余作用，建立带惯性字符的 Hecke 矩阵，再核实其标准基与每个 $D_j$ 的上同调直和分解相符。只知道抽象 Hecke 特征值还不够，因为部分迹需要这些特定的分量投影。

在 $p=41$，R57 给一条真正非零方向；本结果又把 $18$ 维 principal-series 代数中的 $17$ 维 trace-zero 空间明确放入核。它们与 R55 的更大维数下界相容，但本文未凭这些事实断言该层的 $\Phi_A$ 精确秩为 $1$、$2$ 或 $3$。

这些结构也尚未控制辅助素数处 $\Delta_\ell$ 的共同根。其用途是计算真实坏靶与构造真实零高度方向；完成 O5 还须把这些算术数据用于跨层的有理点排除。

## 8. 已核查原始来源

- H. Carayol, **Sur les représentations $l$-adiques associées aux formes modulaires de Hilbert**, *Annales scientifiques de l'École Normale Supérieure*, série 4, **19** (1986), 409–468，DOI [10.24033/asens.1512](https://doi.org/10.24033/asens.1512)，[原刊 PDF](https://www.numdam.org/article/ASENS_1986_4_19_3_409_0.pdf)。§0.5–§0.7、Theorem (A)，pp.410–411：系数域相容的局部 Hecke 对应、严格相容系统及全部非系数特征局部的识别。
- D. Loeffler and J. Weinstein, **On the computation of local components of a newform**, *Mathematics of Computation* **81** (2012), 1179–1200，DOI [10.1090/S0025-5718-2011-02530-5](https://doi.org/10.1090/S0025-5718-2011-02530-5)，[出版版 PDF](https://wrap.warwick.ac.uk/id/eprint/43666/1/WRAP_Loeffler_S0025-5718-2011-02530-5.pdf)。p.1180：Carayol 比较；Table 1、§2.3、Proposition 2.8，pp.1182–1183：局部 conductor、全局新形式扭曲与 Steinberg 的 level-$p$ 情形。
- P. Mercuri and R. Schoof, **Modular forms invariant under non-split Cartan subgroups**, *Mathematics of Computation* **89** (2020), 1969–1991，DOI [10.1090/mcom/3503](https://doi.org/10.1090/mcom/3503)，[原刊作者抽印本](https://reneschoof.github.io/mcom3503.pdf)。Propositions 2.1、3.2，pp.1971–1974：twisted Steinberg 的正规化子不变量；Proposition 5.2、§6、Proposition 6.1，pp.1978–1980：全局特征形式的有限群类型及明确的二次扭曲关系。
- G. Faltings, **Endlichkeitssätze für abelsche Varietäten über Zahlkörpern**, *Inventiones Mathematicae* **73** (1983), 349–366，DOI [10.1007/BF01388432](https://doi.org/10.1007/BF01388432)，[原刊 PDF](https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf)。§1，p.349 的 a)、b) 为本文从相同 Tate 表示到全局同源所用的半单性及 Tate 同态定理。
- B. Edixhoven and P. Parent, **Semistable reduction of modular curves associated with maximal subgroups in prime level**, *Documenta Mathematica* **26** (2021), 231–269，[原刊 PDF](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)。§2.2.4，pp.243–244，(12)–(13)：范数核的惯性作用；Theorem 3.5，pp.249–251：两种图与 Drinfeld 曲线；Remark 3.8，pp.251–252：所用亏格公式。
- B. Edixhoven and P. Parent, **Regular models of modular curves in prime level over $\mathbb Z_p^{\rm ur}$**, *Documenta Mathematica* **29** (2024), 1017–1058，[原刊 PDF](https://content.ems.press/assets/public/full-texts/serials/dm/29/5/14298148/online/10.4171-dm-974.pdf)。Theorem 3.2 的证明及 pp.1041–1042：惯性坐标、末端解消与特殊自同构；Theorem 3.4、Corollary 3.2：实际未分歧模型。
- R57 引用的 Betts–Duque-Rosero–Hashimoto–Spelier, Theorem 3.11，是第 4 节使用的更正局部高度公式；R43 保留实际 $2F$、$d^2$ 和符号；R45、R47–R49、R54–R55 给真实 Heegner 商、容许格、辅助函数及靶集接口。

这里不把经典局部类型与扭曲定理声称为新发现。新推导是将这些全局类型与确切坏分量高度连接，得到 (4.4)、principal-series 全几何核及 (6.2) 的核分解。
