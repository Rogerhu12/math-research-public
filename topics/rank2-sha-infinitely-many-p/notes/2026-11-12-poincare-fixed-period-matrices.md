# 固定 Poincaré 纤维、广义 Jacobian 与实际高度的有限 period 矩阵

后续 [R39](../results/R39-cm-height-linear-period-matrix.md) 已用新增 CM 行把实际三个 cyclotomic 高度和反对称高度同时化成线性 period，并证明其全部代数线性独立；剩余二次 regulator 尚未非零。

**可信度：§1–§6 的归约及线性独立在列出的已证输入下已证明；§7 为新文献适用范围核查。** 日期：2026-11-12。

固定
$$
E:y^2=x^3-17x,\qquad P=(-1,4),\quad Q=(9,24).
$$
沿用 [universal-extension 笔记](2026-11-12-universal-extension-log-determinants.md) 的
$\omega=dx/(2y)$、第三类微分 $\eta_P,\eta_Q$、
universal extension 对数坐标 $(a_{P,p},\ell_{P,p})$、
$(a_{Q,p},\ell_{Q,p})$。本笔记不更改该已冻结文件。

本次得到一个实际的固定有限对象：原始第三类积分矩阵确实是固定交换代数群的线性对数 period 矩阵；加入全局局部项后仍如此。实际高度行列式可准确写成一个 $3\times3$ 的此类 period 行列式。不过 AST 给出的全部线性独立仍没有证明这个行列式非零。下面明确构造、证明，并保留两者之间的乘积项。

## 1. 只需一个固定广义 Jacobian

取固定的有理点
$$
R=2P+2Q
$$
和两个除子
$$
B_P=(R+P)-(R),\qquad B_Q=(R+Q)-(R).
\tag{1}
$$
$P,Q$ 独立，所以 $R,R+P,R+Q$ 两两不同，且均不等于 $O,P,Q$。
例如若 $R+P=Q$，便得到 $3P+Q=O$，与独立性矛盾；其他情形相同。
又有 $B_P\sim(P)-(O)$、$B_Q\sim(Q)-(O)$。

令 $\mathfrak m=(O)+(P)+(Q)$，取 reduced modulus 的广义 Jacobian
$$
0\longrightarrow\mathbb G_m^2
\longrightarrow J_{\mathfrak m}
\longrightarrow E
\longrightarrow0.
\tag{2}
$$
其 torus 的两个基本特征所给扩张类可取为 $P,Q\in E^\vee(\mathbb Q)$
（整体符号依广义 Jacobian 的惯例改变，不影响下列论证）。

三个微分
$$
\omega,\qquad
\eta_P=\frac{y+4}{x+1}\omega,\qquad
\eta_Q=\frac{y+24}{x-9}\omega
$$
是 $H^0(E,\Omega^1_E(\mathfrak m))$ 的一组基：后两者有相互独立的留数向量，前者为全纯基。广义 Abel–Jacobi 映射把它们唯一提升为
$J_{\mathfrak m}$ 上的 invariant differentials，记为
$\omega^{\rm inv},\theta_P,\theta_Q$。

式 (1) 定义两个固定点
$$
b_P=[B_P]_{\mathfrak m},\qquad b_Q=[B_Q]_{\mathfrak m}
\quad\text{属于 }J_{\mathfrak m}(\mathbb Q),
\tag{3}
$$
其在 $E$ 中的像分别是 $P,Q$。它们就是同时包含两个固定 Poincaré 纤维的信息的具体代数提升，不需要另选随 $p$ 变化的有理平凡化。

### 所用外部输入及范围

Zarhin，*P-adic abelian integrals and commutative Lie groups*，
[arXiv:alg-geom/9603006v4](https://arxiv.org/pdf/alg-geom/9603006)，§3，印刷第8–9页，构造一个 semi-abelian Albanese，使固定极点集合的第三类微分恰为 invariant differentials 的 pullback，并定义
$$
\int_A^B\eta
=\eta^{\rm inv}\!\left(\log(f(B))-\log(f(A))\right).
\tag{4}
$$
这里取 $V=E,S=\{O,P,Q\}$ 得到 (2)–(3)。
它与好约化时的 Coleman 积分一致；参见该文导言及 Besser
[arXiv:1711.06957](https://arxiv.org/pdf/1711.06957)，导言对 Zarhin–Colmez 积分与高度构造的说明。
所有对数分支取 $\log_p(p)=0$。

因此
$$
I_{ij,p}:=\int_{B_j}\eta_i
=\theta_i\!\left(\log_{J_{\mathfrak m}}b_j\right),
\qquad i,j\in\{P,Q\},
\tag{5}
$$
且
$$
\omega^{\rm inv}(\log b_j)=\ell_{j,p}.
\tag{6}
$$
同一固定三维代数群和同一组两个代数点已提供矩阵 $I_p$ 的全部四个元素。

## 2. 远离 p 的全局项也只需固定 torus

考虑与标准 cyclotomic idele class character 相应的全局 Coleman–Gross 高度。
其 $q\ne p$ 的分量以 $\log_p(q)$ 乘固定的有理交数给出。

所有曲线、除子及有理点均已固定，所以存在一个固定有限素数集 $S$，包含：

- $E$ 的坏约化素数；
- (1) 和各 $A_i=(i)-(O)$ 的支集在整数模型上相交的素数；
- 为使所用群模型、点和微分均延拓所需的有限多个分母素数。

对 $p\notin S$，远离 $p$ 的项可写成
$$
C_{ij,p}=\sum_{q\in S}r_{ij,q}\log_p(q),
\qquad r_{ij,q}\in\mathbb Q,
\tag{7}
$$
其中 $S$ 和全部 $r_{ij,q}$ 都不随 $p$ 改变。符号已吸收进 $r_{ij,q}$。

令
$$
\mathcal B_{ij,p}=I_{ij,p}+C_{ij,p}.
\tag{8}
$$
这样 $\mathcal B_p$ 的全部条目均为一个固定有限交换代数群上的对数坐标的有理线性组合。添加 $\mathbb G_m^{|S|}$ 和固定点 $(q)_{q\in S}$ 即可，不需要移动 division field 或移动 tame character。

排除这个固定有限 $S$ 不影响主课题所需的“无穷多个 split $p$”。本笔记不把新公式宣称为 $S$ 内每一个小素数也无需改正即可使用。

## 3. 还可证明全部相关一阶 period 的代数线性独立

把 (2) 与 universal extension $G=E^\natural$ 作 fiber product：
$$
\mathcal A=J_{\mathfrak m}\times_E G.
\tag{9}
$$
它是固定四维交换代数群，满足
$$
0\longrightarrow\mathbb G_m^2\times\mathbb G_a
\longrightarrow\mathcal A\longrightarrow E\longrightarrow0.
$$
将 (3) 和前一笔记的固定提升 $g_P,g_Q$ 配对，得到
$$
z_P=(b_P,g_P),\qquad z_Q=(b_Q,g_Q)\in\mathcal A(\mathbb Q).
\tag{10}
$$
对每个点，其四个 Lie 坐标可以取为
$$
(I_{Pj,p},I_{Qj,p},a_{j,p},\ell_{j,p}).
\tag{11}
$$
这是代数 Lie 基，因为 $\theta_P,\theta_Q,\omega^{\rm inv}$ 在
$J_{\mathfrak m}$ 上构成基，而 universal extension 的额外加法坐标补足第四维。

### 3.1 没有非零 affine 商

先证
$$
\operatorname{Hom}(\mathcal A,\mathbb G_m)=0,
\qquad
\operatorname{Hom}(\mathcal A,\mathbb G_a)=0.
\tag{12}
$$

到 $\mathbb G_m$ 的同态杀掉向量核，故降到 $J_{\mathfrak m}$。
其在 $\mathbb G_m^2$ 上是一个整数特征 $(m,n)$；
能够延拓到整个 $J_{\mathfrak m}$ 当且仅当相应的 pushout 扩张分裂，即
$mP+nQ=0$。由 $P,Q$ 独立，$m=n=0$，而从 $E$ 到 $\mathbb G_m$ 的同态为零。

到 $\mathbb G_a$ 的同态杀掉 torus，故降到 $G$。
Universal extension 的连接映射
$$
\operatorname{Hom}(\mathbb G_a,\mathbb G_a)
\longrightarrow\operatorname{Ext}^1(E,\mathbb G_a)
$$
是同构，所以 $\operatorname{Hom}(G,\mathbb G_a)=0$。

这些论证对 $\mathcal A^n$ 同样成立。
任何非零连通交换 affine 群在特征零的代数闭包上都有一个非零
$\mathbb G_m$ 或 $\mathbb G_a$ 商，因此 (12) 也排除一切非零连通 affine 商。

### 3.2 两个点的代数群包

前一笔记 §2 已证明 $P,Q$ 在 $\operatorname{End}^0(E)=\mathbb Q(i)$ 上独立。
故 $(P,Q)$ 在 $E^2$ 中的代数群包为整个 $E^2$。

若 $(z_P,z_Q)$ 在 $\mathcal A^2$ 中的群包的恒等分支为 $H$，
则 $H$ 仍满射 $E^2$。
于是 $\mathcal A^2/H$ 是向量与 torus 核的商，因而 affine。
由 (12)，这个商只能为零。所以 $H=\mathcal A^2$。

再加上独立的固定素数点 $(q)_{q\in S}$。
若 $\mathcal A^2\times\mathbb G_m^{|S|}$ 中的群包不满，
商仍是 affine；它的非零 torus 特征必须来自最后的因子，
从而给出
$\prod_{q\in S}q^{n_q}$ 为根单位。
各 $q$ 是互异的正有理素数，所以只能 $n_q=0$。
到加法群的商已被 (12) 排除。因此该群包也满。

最后加入加法群中的点 $1$。
与前一笔记 §3 相同，若满射到已有群的恒等分支在此加法因子核为零，
它到已有群的同源将迫使第一坐标同态为零；
因为已有群以及其同源群都没有非零加法商。
这与某个非零整数倍的第一坐标为 $N$ 矛盾。
故整个群包仍满。

### 3.3 AST 的准确结论

在固定有限集外，以上点均在适当的整数模型内，
故位于紧子群，可使用 Fuchs–Pham
[arXiv:1502.00768](https://arxiv.org/pdf/1502.00768)，Theorem 2.2。
这个定理适用于一般交换代数群，包括 (9) 的 torus 与 vector extension。

若全部坐标存在非零代数线性关系，其对数就在一个
$\overline{\mathbb Q}$-定义的真超平面中，
AST 产生一个真代数子群包含该点，矛盾。
由 (7)–(8) 是保留 $\log_p(q)$ 后的可逆三角换元，得到
$$
\boxed{
1,\ \mathcal B_{PP,p},\mathcal B_{PQ,p},
\mathcal B_{QP,p},\mathcal B_{QQ,p},\
a_{P,p},a_{Q,p},\ell_{P,p},\ell_{Q,p},\
(\log_p(q))_{q\in S}
\ \text{在 }\overline{\mathbb Q}\text{ 上线性独立}.
}
\tag{13}
$$
这里并未宣称它们代数独立。下一节恰好有一个它们实际满足的二次关系。

## 4. 实际高度是低次数 polynomial period

记
$$
\mathbf a=\binom{a_{P,p}}{a_{Q,p}},\qquad
\boldsymbol\ell=\binom{\ell_{P,p}}{\ell_{Q,p}}.
$$
CM 的 ordinary 补空间为固定代数线 $\mathbb Q_p[x\omega]$。
上一笔记的逐式高度比较给
$$
H_p=\mathcal B_p-\mathbf a\boldsymbol\ell^t.
\tag{14}
$$
这个公式也可以直接从 (5) 得到：
高度所用的第三类微分为
$\eta_i-a_{i,p}\omega$，
所以其在 $J_{\mathfrak m}$ 上的 invariant differential 为
$$
\theta_i-a_{i,p}\omega^{\rm inv}.
\tag{15}
$$

对固定 $i$，(15) 的系数 $a_{i,p}$ 超越，见 (13)。
因此 **作为整个局部群上的微分泛函**，(15) 不是代数定义的 Lie 线性形式。
它若与一个代数线性形式在一个非空开子群上相等，
取微分并比较独立的 $\theta_P,\theta_Q,\omega^{\rm inv}$ 系数，
会迫使 $a_{i,p}$ 为代数数，矛盾。

这说明固定 Poincaré 纤维真正线性化的是 $I_{ij,p}$；
canonical 高度的单位根正规化仍引入一个 period 系数。
这里没有声称排除了“在两个指定点处偶然存在另一种线性表示”或排除一切更深的 motivic 构造。

因为 $H_p$ 对称，式 (14) 给出实际的二次恒等式
$$
\mathcal B_{PQ,p}-\mathcal B_{QP,p}
=a_{P,p}\ell_{Q,p}-a_{Q,p}\ell_{P,p}.
\tag{16}
$$
式 (13) 与 (16) 相容：线性独立允许这样的非线性关系。
因此不能把本例的 period 坐标当成代数独立变量。

另一方面，(13) 与 (16) **确实证明这个特定的原始提升行列式非零**：
左端是非零的代数线性组合，故不可能为零。
[R37](../results/R37-cm-period-reciprocity-nonvanishing.md)
给出了更简短的广义 Jacobian 证明、全部目标素数的紧性处理，
并进一步把 CM 反对称高度 $h^-([i]P,Q)$ 化成四个此类线性 period。
下面 (17)–(18) 的 cyclotomic 及 strict 三次行列式仍未被这个加强解决。

## 5. 两个目标都成为明确的 3×3 determinant

矩阵行列式引理给
$$
\begin{aligned}
\det H_p
&=\det\mathcal B_p
-\boldsymbol\ell^t\operatorname{adj}(\mathcal B_p)\mathbf a\\
&=\det
\begin{pmatrix}
\mathcal B_{PP,p}&\mathcal B_{PQ,p}&a_{P,p}\\
\mathcal B_{QP,p}&\mathcal B_{QQ,p}&a_{Q,p}\\
\ell_{P,p}&\ell_{Q,p}&1
\end{pmatrix}.
\end{aligned}
\tag{17}
$$
这是固定有限列表 (13) 的次数至多三的多项式。
最高次数不是四，因为 (14) 的二次修正为 rank one。

再令
$$
\mathbf v=\binom{\ell_{Q,p}}{-\ell_{P,p}},\qquad
\xi_p=\ell_{Q,p}P-\ell_{P,p}Q.
$$
由 $\boldsymbol\ell^t\mathbf v=0$，
$$
h_p(\xi_p,\xi_p)=\mathbf v^t\mathcal B_p\mathbf v.
$$
对任意 $2\times2$ 矩阵 $\mathcal B$ 都有
$\mathbf v^t\mathcal B\mathbf v
=\boldsymbol\ell^t\operatorname{adj}(\mathcal B)\boldsymbol\ell$，
故
$$
\boxed{
h_p(\xi_p,\xi_p)=-
\det
\begin{pmatrix}
\mathcal B_{PP,p}&\mathcal B_{PQ,p}&\ell_{P,p}\\
\mathcal B_{QP,p}&\mathcal B_{QQ,p}&\ell_{Q,p}\\
\ell_{P,p}&\ell_{Q,p}&0
\end{pmatrix}.
}
\tag{18}
$$
这里的最后一个行列式也是三次式。它与严格局部核对应，
而不是任意 algebraic lift 的 $2\times2$ determinant。

两张矩阵都由固定代数群的线性 period 条目组成；
但“条目只有已知的线性关系”不会推出矩阵实际满秩。
例如所有条目线性独立的 $2\times2$ 矩阵仍可能具有零行列式；
前一笔记 §4 已给出纯代数例子。
对 (17)–(18) 的非零，仍需超出 AST 的非线性 period 或准确的 arithmetic 输入。

## 6. 为什么不能把双扩张总空间当作一个新的交换扩张

一个 Poincaré $\mathbb G_m$-biextension 在固定第二个点后，
确实给出 $E$ 的 $\mathbb G_m$ 扩张；(2) 同时保留了两个这样的扩张。

但其在 $E\times E^\vee$ 上的总空间不是凭名称就成为
$E\times E^\vee$ 的交换代数群扩张。
若一个 $\mathbb G_m$ torsor 是 abelian variety $A$ 的交换群扩张，
其对应的线丛须属于 $\operatorname{Pic}^0(A)$，
由 Weil–Barsotti 对偶给出。
Poincaré bundle 在 $E\times E^\vee$ 上具有非零的 mixed Néron–Severi 类，
故不属于 $\operatorname{Pic}^0(E\times E^\vee)$。

一个直接检查是：
$\operatorname{Pic}^0(E\times E^\vee)
\simeq\operatorname{Pic}^0(E)\times\operatorname{Pic}^0(E^\vee)$，
其中线丛限制到第一因子的纤维，其 $\operatorname{Pic}^0(E)$ 类不随第二坐标改变。
Poincaré bundle 的这一限制恰遍历 $E^\vee$，
所以不是这种线丛。

因此把四个 pairing 值共同装入 Poincaré 总空间，
不能自动得到可直接套用交换 AST 的一个新群对数坐标。
固定纤维的合法处理已由 (2)–(5) 完成，剩余的正规化和行列式由
(14)–(18) 原样保留。

## 7. “1-motive period conjecture at depth 2”没有提供所缺的多项式非零

本轮核对了 Mohajer–Sebbar，
*P-adic Period Conjectures for 1-motives: Integration and Linear Relations*，
[arXiv:2507.15020v1](https://arxiv.org/pdf/2507.15020)，2025-07-20。

需要区分其术语：

- Definition 4.4 的 formal period 空间是
  $\bigoplus_M F(M)\otimes_{\mathbb Q}G(M)$ 对线性 functoriality 关系取商；
- Definition 4.5 的 depth 改变的是该**向量空间**中用短正合列生成的关系；
  它没有把空间改成 period 的二次或三次多项式代数；
- Theorems 4–5 处理的是受限 $H_p^\varpi,H_p^\varphi,h_p$ 结构上的
  **线性关系**，其证明从 $\sum c_i\alpha_i=0$ 出发；
- Definition 4.11 还规定了输入的特殊 $\mathbb Q$-结构与
  $N^{\rm e}(M)$ 中的 de Rham 向量，不能把任意
  $\mathbb Q_p$ 系数的正规化形式 (15) 自动放入；
- 该文导言还明确把这些积分 period 与另一套 crystalline/André period
  的完整比较留作后续工作。

所以不能把“depth 2”读成“所有二次行列式已非零”，
更不能据此证明 (17)–(18)。
本笔记没有依赖其新定理的正确性来证明 §1–§6；
只是核实它所声称的结论即使按原文接受，也不是本课题当前缺失的非线性命题。

## 8. 目前实际得到的正面归约

现在，固定 $P,Q$ 的问题至少不必再笼统地说成“需要无限维的所有积分”：
外部已证积分理论给出了固定四维 $\mathcal A$、
两个固定代数点 $z_P,z_Q$ 和一个固定有限 torus。
所有一阶输入 (13) 都在该对象内，并有完整的代数线性独立证明。

然而 (17) 和 (18) 仍是这些 period 的实际矩阵秩问题。
本笔记没有证明其中任一式在无穷多个 $p$ 非零，
也没有把任一高度非零直接等同于尚未闭合的 Sha 有限性证书。
