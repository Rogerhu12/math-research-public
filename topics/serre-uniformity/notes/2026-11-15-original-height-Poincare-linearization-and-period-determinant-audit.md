# 原高度首项的 Poincaré 线性化、径向组合与仍未消去的二次 period 等式

日期：2026-11-15。状态：研究审计及下列逐式恒等；**不证明原 $\mathscr T_p\ne0$，不另登记结果编号，不改变原高度或启动新数值计算。**

本文接 R724、R785 与已经登记的 R832。始终保留 R634/R724 的原 R616 非零前提；涉及一次曲线切向时另使用 R729 已证的 $m=1$ 范围，不把这些前提推广到尚未覆盖的素数。R634 已证明原各 $E_{ij}$ 非恒零，R832 已给固定 $c_1$ 的显式有限接触阶界；这两项不在本文重证。这里只检查一个更具体的可能入口：保留实际 Poincaré 纤维、原 $\eta_h$ 和第二类周期后，原首项能在线性 period 的范畴内化简到什么程度。

## 1. 坏处零值究竟允许替换什么

始终使用
$$
P_X=[c_1-c_0],\qquad \beta=qP_X,\qquad
P_0=\phi_*P_X=[Q_1-Q_0],
\qquad Q_\nu=\phi(c_\nu).
\tag{UE.1}
$$
$h\in F^0$、原 $C_h$、完整 $\mu_3$ 范数、刚性化及 $s_h(c_0)=1$ 均保持。

R694 §6、式 (694.22) 逐个证明原 $c_1$ 的三进局部值为零；R690 给二进值为零；R593 (593R.22) 给其他非 $p$ 局部值为零。这些都是**完整修正线丛**的值。因此 R593 (593R.16)、R724 (724.2) 给
$$
\lambda_{p,h}(c_1)
 =\widehat h_{\mathcal L_h}(\beta)+2h_Y(P_0,\eta_h),
\qquad
d_h=\Lambda_h(c_1)=\widehat h_{\mathcal L_h}(\beta).
\tag{UE.2}
$$
这里仍有
$$
\Lambda_h=\lambda_{p,h}-2\ell_h(\log P_Y),\qquad
\ell_h(\log P_0)=h_Y(P_0,\eta_h).
\tag{UE.3}
$$

所以坏处零不能给 $d_h=\lambda_{p,h}(c_1)$，也不能给
$d_h=$“某个任取的 $A$ 局部帧在 $\beta$ 的值”。在将原线丛写成 $A$ 对称因子、$Y$ Picard 因子和代数标量以后，各因子的非 $p$ 项可以互相抵消；完整和为零不迫每个因子为零。

以下将 $A$ 的 splitting 按 R699 取为代数且 $F$ 相容的 Lagrangian 补空间。原外积在该改变下不变。$Y$ 的参考 splitting 按 R724 同时比较局部项与 $\ell_h$；没有只改变其中一项。

## 2. 一个真正可以线性化的径向组合

先在一个对称因子上说明，不将它直接冒充原曲线切向。

设 $L/A$ 是沿原点刚性化的实际对称线丛，$\lambda_L:A\to A^\vee$ 是其同态，$P\in A(\overline{\mathbb Q})$。取 $P$ 邻域的代数非零帧 $u$。记对数分支下的局部值为 $\lambda_u(P)$；暂在应用原局部角色之前工作。

置
$$
\mathcal P_L=(\operatorname{pr}_1,\lambda_L\circ\operatorname{pr}_2)^*\mathcal P_A
       \quad\text{于 } A\times A,\qquad
E_P=\mathcal P_A|_{A\times\{\lambda_LP\}}^\times .
\tag{UE.4}
$$
第二个对象是 $A$ 的 $\mathbb G_m$ 扩张。原对称刚性化给
$\Delta^*\mathcal P_L\simeq L^{\otimes2}$。

在 $(P,P)$ 附近可取代数帧 $e(X,Y)$，满足
$$
e(Y,X)=e(X,Y),\qquad e(X,X)=u(X)^2.
\tag{UE.5}
$$
这是局部代数构造：先在交换两个因子的规范对称结构下将一个非零帧与其转置相加，再缩小开集；对角上其与 $u^2$ 的比记为 $r(X)$，乘上
$(r(X)^{-1}+r(Y)^{-1})/2$ 即有 (UE.5)。不需要选一个含未知 period 的帧。

令 $z_P=e(P,P)\in E_P(\overline{\mathbb Q})$。将
$X\mapsto e(X,P)$ 在 $P$ 的微分通过群平移移到单位元，得到代数线性映射
$$
\alpha_P:\operatorname{Lie}A\longrightarrow\operatorname{Lie}E_P,
\qquad \operatorname{pr}_*\alpha_P=1.
\tag{UE.6}
$$
规范 $\chi$-splitting 在对数分支下的微分记为
$t_P:\operatorname{Lie}E_P\to\overline{\mathbb Q}_p$，它在 torus Lie 代数上为恒等。原 Lagrangian 选择保证 $\mathcal P_L$ 的 log 在两个变量交换下不变；这也可由同一曲率及两条零轴刚性化的唯一性检查。因此
$$
2\lambda_u(P)=t_P(\log_{E_P}z_P),\qquad
d\lambda_u|_P(v)=t_P(\alpha_P(v)).
\tag{UE.7}
$$
取任意代数线性投影 $t_{\rm alg}$，在 torus 上为恒等，并令
$$
\ell_P=t_{\rm alg}-t_{\rm alg}\alpha_P\operatorname{pr}_*.
\tag{UE.8}
$$
由于 $\log_{E_P}z_P-\alpha_P(\log_AP)$ 位于 torus Lie 代数，
$$
\boxed{
2\lambda_u(P)-d\lambda_u|_P(\log_AP)
 =\ell_P(\log_{E_P}z_P).
}
\tag{UE.9}
$$
$\ell_P$ 是代数 Lie 线性形式，且其 torus 系数为 $1$。这一步确实消去了规范 universal-extension 修正；它不是把原 $\Delta_Q$ 设为零，也没有变更它的符号。

若改用同一 $L$ 的全局高度，非 $p$ 项是有限个有理交数乘原全局角色值。对 $\mathbb Q$ 的固定角色先提出其共同非零标度 $c$，其余为代数数的 $p$ 进对数。把二倍非 $p$ 总项吸收到 $z_P$ 的一个代数 torus 倍数中，得到 $z'_P$。于是 (UE.9) 同样线性化
$$
2\widehat h_L(P)-d\lambda_{u,p}|_P(\log_AP).
\tag{UE.10}
$$
实际值须保留公共标度 $c$，及所有清分母的除回因子；提出 $c$ 只为陈述线性关系，不是另选高度。

### 2.1 这里 AST 确实能使用，但方向是径向

若 $P=\beta$、$L$ 来自非零有理 $h\in F$，则 $\lambda_L\beta$ 非挠：$\lambda_L$ 在同源范畴可逆，而 $\beta$ 非挠。$\beta$ 的几何循环群包是整个 $A$。其群包在 $\mathbb Q$ 上定义；恒等分支含 $\beta$ 的一个非挠倍数，而 $A$ 在 $\mathbb Q$ 上单。

因此 $E_P$ 没有非零 torus 商。任何含 $z'_P$ 一个非零倍数的连通代数子群投影满 $A$，其商被原 torus 满射；这个商只能为零，故该子群为 $E_P$。于是对合法的群对数应用 AST，(UE.10) 非零，因为 (UE.8) 在 torus 上非零。

对数分支问题不能省略。原分支杀掉 $p$；在有限局部定义域中，先把投影乘入某个紧开子群的像，再以 torus 中代数的 $p$ 有理次幂抵消各赋值，便将点放进 $E_P(\mathbb C_p)_f$。这个修正的对数为零，投影仍为 $\beta$ 的非零倍数，故群包和所需非零结论均保持。

但 R634/R682 已证明原非零代数切向量
$$
u_A=\left.\frac{d}{dz}\log j_A(c_1+z)\right|_{z=0}
\tag{UE.11}
$$
不与 $\log\beta$ 成比例。因而不能把 (UE.9) 的径向导数直接改成原 $z=a-1$ 导数。

## 3. 同一代数提升族保留原实乘坐标

径向恒等式还可逐个实乘坐标用于真正的原切向，但须同时保留全部分量。

取 $F$ 的有理基 $h_1,\ldots,h_g$，暂包含迹方向。选共同整数清除实际同态及线丛分母；以下等式按该整数准确除回。令
$$
Q=\lambda_A\beta,\qquad Z\in I_A(\overline{\mathbb Q})
       \ \text{为 }Q\text{ 的代数提升}.
\tag{UE.12}
$$
第 $h$ 个提升取 $h^\vee Z$。因为参考 splitting 对 $F$ 相容，它的规范提升也按同一 $h^\vee$ 运输。

为不更改 R724 的符号，直接将实际两个 Lie 投影之差定义为
$$
(t_{h^\vee Z}-t_{{\rm can},h})(v_E)
       =\delta(h\,\operatorname{pr}_*v_E),
\tag{UE.13}
$$
其中 $\delta\in(\operatorname{Lie}A)^\vee\otimes\mathbb C_p$ 是同一个协向量。这个等式来自固定第二变量的 Poincaré 扩张在 $[h]$ 下的拉回及其刚性化；它不是新设一个独立的 $\delta_h$。

在第 $h$ 个对称帧中，令 $z'_h$ 吸收该 $A$ 因子的真实非 $p$ 项，如 §2。定义
$$
V_h=t_{h^\vee Z}(\log_{E_h}z'_h),\qquad
A_h=t_{h^\vee Z}(\alpha_h(u_A)).
\tag{UE.14}
$$
这里 $V_h$ 是一个真正的线性 period；$A_h$ 是代数数，因为原 $u_A$、帧和全部 Lie 映射为代数。记该全局对称高度为 $D_h$，该帧沿原 $u_A$ 的局部导数为 $G_h$。由同一 (UE.7)、(UE.13)，
$$
2D_h/c=V_h-\delta(h\log\beta),\qquad
G_h/c=A_h-\delta(hu_A).
\tag{UE.15}
$$
此处 $G_h$ 还不是完整修正线丛的 $g_h$。

采用 R682 的代数 $F$-基及嵌入坐标，
$$
\log\beta=(L_i)_i,\qquad u_A=(a_i)_i,\qquad
T_i=a_i/L_i.
\tag{UE.16}
$$
$L_i\ne0$、$a_i\ne0$，而 $(T_i-T_g)_{i<g}\ne0$。设
$\epsilon_i\in F\otimes\overline{\mathbb Q}$ 为分裂幂等元，令
$h^{[i]}=\epsilon_i/\kappa_i$。它们只作为前述有理基的代数线性组合使用，不能称每个 $h^{[i]}$ 自己定义一条有理线丛。

按这些组合记 $D_i,G_i,V_i,A_i$。式 (UE.15) 成为
$$
2D_i/c=V_i-\delta_iL_i,\qquad
G_i/c=A_i-\delta_i a_i,
\tag{UE.17}
$$
其中 $\delta_i$ 已包含 $1/\kappa_i$，并含真实第二类周期和同一规范修正。于是
$$
\boxed{
U_i:=2D_i a_i-G_iL_i
       =c(a_iV_i-A_iL_i).
}
\tag{UE.18}
$$
因此这一组 $A$ 分量的 numerator 确实可线性化。不能把 (UE.18) 表述为
“原所有 $2d_i a_i-g_iL_i$ 已经线性化”，因为原坐标还要减去第 $g$ 分量，并加入 §4 的真实 Picard 项。

### 3.1 线性独立范围可以准确说明

同时取全部 $g$ 个扩张的纤维积，得到
$$
1\longrightarrow\mathbb G_m^g\longrightarrow G
       \longrightarrow A\longrightarrow0.
\tag{UE.19}
$$
其 torus 特征对应于 $\lambda_Ah_j\beta$。这些点在 $\mathbb Z$ 上独立：非零有理组合 $h\in F$ 是同源，不能将非挠 $\beta$ 送到挠点。因此特征到 $A^\vee$ 的映射为单射，$G$ 为反仿射群，即 $\mathcal O(G)=\overline{\mathbb Q}$。

点 $(z'_{h_j})_j$ 投影到 $\beta$，其几何循环群包为全 $G$，理由与 §2.1 相同。全部 $V_i$ 与 $L_i$ 是 $\operatorname{Lie}G$ 的一组代数对偶坐标的值；torus 行及 $A$ 行的换基可逆。AST 因而给
$$
V_1,\ldots,V_g,L_1,\ldots,L_g
\quad\text{在 }\overline{\mathbb Q}\text{ 上线性独立}.
\tag{UE.20}
$$
再由 $a_i\ne0$ 及 (UE.18)，
$$
U_1/c,\ldots,U_g/c,L_1,\ldots,L_g
\quad\text{同样代数线性独立}.
\tag{UE.21}
$$
这只是同一个实际代数群点的线性 period 结论，不是这些数的代数独立性。

## 4. 原 $\mathscr T_p$ 恰好还要求哪一个行列式非零

按 R634/R785 的原加权迹坐标，(UE.2) 准确给
$$
d_i=D_i-D_g\qquad(i<g).
\tag{UE.22}
$$
用 R724 的实际 tensor 表示，在同一个 $c_1$ 邻域将完整原局部项与上节的 $A$ 对称帧比较。定义
$$
P_i:=g_i-(G_i-G_g),\qquad P_g:=0.
\tag{UE.23}
$$
这里 $g_i=[z]\Lambda_i$。因此 $P_i$ 完整保留以下三项：
原实际截面的代数标量对数导数、原 Picard 纤维的规范局部导数，以及
$-2\ell_i(u_Y)$，其中
$$
u_Y=\left.\frac{d}{dz}\log P_Y(c_1+z)\right|_{z=0}.
\tag{UE.24}
$$
它们按原 $C_h$ 及完整范数除回。此定义既不假设 $\eta_i=0$，也不把一个任意第三类微分替代原规范 Picard 微分。

令
$$
v_i=T_i-T_g,\qquad s_i=2d_iT_i-g_i.
$$
由 (UE.18)、(UE.22)、(UE.23) 直接得到
$$
s_i=\frac{U_i}{L_i}-\frac{U_g}{L_g}
             -2D_gv_i-P_i.
\tag{UE.25}
$$
所以
$$
\boxed{
\mathscr T_p=0
\quad\Longleftrightarrow\quad
\operatorname{rank}_{\mathbb C_p}
\begin{pmatrix}
a_1&L_1&U_1-L_1P_1\\
\vdots&\vdots&\vdots\\
a_{g-1}&L_{g-1}&U_{g-1}-L_{g-1}P_{g-1}\\
a_g&L_g&U_g
\end{pmatrix}\le2 .
}
\tag{UE.26}
$$
前两列确实独立，正是 $(T_i-T_g)\ne0$，故没有另一个退化前提。

对 $i<j<g$，保留行顺序 $(i,j,g)$，记该三阶子式为 $\Delta_{ij}$。
精确符号为
$$
\Delta_{ij}
 =L_iL_jL_g(s_iv_j-s_jv_i),\qquad
[z^2]E_{ij}=\frac{2\Delta_{ij}}{L_iL_jL_g}.
\tag{UE.27}
$$
等价地，它仍是原来的同一个清分母等式
$$
\begin{split}
\Delta_{ij}={}&
(2d_i a_i-g_iL_i)(a_jL_g-a_gL_j)\\
&-(2d_j a_j-g_jL_j)(a_iL_g-a_gL_i).
\end{split}
\tag{UE.28}
$$

即使额外有 $P_i=0$，(UE.26) 仍含 $U_iL_j-U_jL_i$ 这种**二次 period 组合**。式 (UE.20)–(UE.21) 不能排除它。一般原问题还含 $L_iP_i$，而 $P_i$ 包括 R785 的真实高度/对数矩阵及第二类周期，不能视为代数系数。

## 5. 二重 Poincaré 或半直积没有自动补上这一步

固定第二变量 $Q$ 时，$\mathcal P_A|_{A\times\{Q\}}^\times$ 是一个交换代数群，所以上述线性化合法。但整个 $\mathcal P_A^\times$ 在 $A\times A^\vee$ 上是双扩张；它的两种部分群 law 不等于一个覆盖 $A\times A^\vee$ 加法的群扩张。它的混合 Chern 类非零，而一个阿贝尔簇的 $\mathbb G_m$ 群扩张来自 $\operatorname{Pic}^0$。因此不能直接把同时变化两个变量的 Poincaré torsor 当作新的半阿贝尔群来用 AST。

对 (UE.19) 的反仿射群还有一个可核限制：其任何有限维代数线性表示均平凡。因此在它上面附加一个代数向量表示作半直积，不会产生编码 $U_iL_j$ 的新非平凡作用。更一般地，反仿射群在一个有固定点的代数簇上的作用平凡；由此也不能仅通过一个通常的代数半直积构造来宣称 period 的乘积已经成为新的线性对数。

这不是说任何固定点互易恒等式都不可能。相邻课题的 R37/R39 确实在特定 CM 点、特定规范下，以第三类积分互易及新增 CM 行将某些乘积化为线性 period。那种方法的有效步骤是**先证实际恒等式**，不是先把任意 period 矩阵的行列式称为线性。

还必须明确已有非交换 AST。Pham (2022), Theorem 3，允许一般连通代数群，但结论仍针对一个代数点 logarithm 的最小代数线性子空间；其证明将该一参数对象归约到交换子群。它不提供“任意两个原 period 的乘积是另一个代数点的 logarithm”这一缺失接口。若用它处理 (UE.26)，仍须先给出真正代数群、真正代数点和逐值相等的代数 Lie 线性形式。当前原 R724/R785 数据尚未给出这项新的互易等式。

## 6. $Y$ 对合能减少中心列，但不能删除整个 Picard 修正

原对合
$$
\jmath:Y\longrightarrow Y,\qquad(n,v)\longmapsto(n,1-v)
\tag{UE.29}
$$
满足 $\jmath(Q_0)=Q_1$、$\jmath(Q_1)=Q_0$。于是
$$
\jmath_*P_0=-P_0,\qquad
P_Y(\jmath y)=\jmath_*P_Y(y)+P_0.
\tag{UE.30}
$$
这些是原点的准确除子类等式，不把 $\jmath$ 提升成原 $X$ 的自同构；R597 已说明两个三次覆盖在这里不能这样交换。

在 $J_Y$ 上选与 $\jmath$ 相容的 Lagrangian 补空间：$\jmath$ 保持主极化，两个特征空间正交且各自非退化，可分别选补空间。它还可与 R785 的等型块选择相容。按 R724 同时运输局部 Picard log 和 $\ell_h$，原 $\Lambda_h$ 不变。在该参考高度中，
$$
h_Y(P_0,\eta_h)=h_Y(P_0,\eta_h^-),\qquad
\eta_h^-=\frac{1-\jmath_*}{2}\eta_h.
\tag{UE.31}
$$
所以 R785 的 $\Theta_{h,0}$ 只用负特征投影。原切向 $u_Y$ 没有被证明只在一个特征空间，故 $\Theta_{h,1}$ 不能作同样删项。

R593/R596 证明的是 $\mu_3$ 不变与固定类下降；R791/R794 证明的是原 Hom/Galois 及 Rosati 范数除子公式。它们均未证明 $\eta_h$ 在 (UE.29) 下不变。尤其“对称线丛”不自动等于“$\jmath$-不变类”：$\jmath$ 不是原 $X$ 自同构，相关 modified-diagonal 拉回必须另外核对。

## 7. 此次核查的准确终点

原完整坏靶已为零，故 $d_h$ 可用同一个真实 $A$ 全局高度替换；它不能用完整 $\lambda_{p,h}(c_1)$ 直接替换。对 $A$ 因子，(UE.18) 将规范 universal-extension 修正准确消去，得到同一反仿射半阿贝尔群的线性 period；这些 period 的代数线性独立可由已证 AST 得到。

原 $\mathscr T_p$ 的判断仍恰为 (UE.26)–(UE.28)。新缺口是这个**指定**的二次 period/Picard 等式是否全部成立，而不是原 $E_{ij}$ 是否恒零。需要一个保原纤维与全部常数的特殊互易恒等式，或实际求值/另一个真正的非线性 period 定理；现有线性 AST、其非交换推广、实 Néron–Tate 正定性和 (UE.31) 都没有补上它。

本文不把这个边界重新包装成 Serre 排除，也不为最坏 R832 jet 窗口启动无实际消费需求的巨大矩阵任务。

## 已读来源

- 本题 R593、R596、R597、R634、R682、R694 §6、R696 §8、R699、R724 §§2、5–7、R785。原径向/首项的全部规范均由这些已登记对象固定。
- A. Iovita–A. Werner, *p-adic height pairings on abelian varieties with semistable ordinary reduction*, J. reine angew. Math. 564 (2003), 181–203，§1 的 universal vectorial extension、rigidification 和局部 Lie 群同态构造；这里只用 ordinary 假设前的一般部分。<https://arxiv.org/pdf/math/0209362>。
- A. Besser–J. S. Müller–P. Srinivasan, *p-adic adelic metrics and Quadratic Chabauty I*, arXiv:2112.03873v4 (2026)，Proposition 4.30、Lemma 4.37、Propositions 6.13–6.14；同一曲率、两条零轴刚性化及 Picard 微分的识别。<https://arxiv.org/html/2112.03873v4>。
- C. Fuchs–D. H. Pham, *The p-adic analytic subgroup theorem revisited*, p-Adic Numbers Ultrametric Anal. Appl. 7 (2015), 143–156，Theorem 2.2；使用范围与本题 R682 相同。<https://arxiv.org/abs/1502.00768>。
- D. H. Pham, *p-adic non-commutative analytic subgroup theorem*, C. R. Math. 360 (2022), 933–936，Theorem 3、Lemma 4 及证明，已读全文。<https://www.numdam.org/item/10.5802/crmath.325.pdf>。
- M. Brion, *Anti-affine algebraic groups*, J. Algebra 321 (2009), 934–952，Lemma 1.1、Lemma 1.5、Proposition 2.1，已核作者稿。本文也给出所用特征单射及群包论证。<https://www-fourier.univ-grenoble-alpes.fr/~mbrion/ag.pdf>。
- 相邻课题的有限点比较仅作方法对照：[R37](../../rank2-sha-infinitely-many-p/results/R37-cm-period-reciprocity-nonvanishing.md) 与 [R39](../../rank2-sha-infinitely-many-p/results/R39-cm-height-linear-period-matrix.md)。其椭圆曲线、分裂素数、CM 字符和高度均不同，未将它们的非零值移入本题。
