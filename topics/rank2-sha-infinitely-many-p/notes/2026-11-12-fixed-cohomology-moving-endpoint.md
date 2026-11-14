# 固定开椭圆曲线的 Frobenius 块与未被保留的端点过滤数据

**可信度：以下微分、端点及 Kummer 过滤比较已证明。** 日期：2026-11-12。本文核查将字符核压入固定维数上同调的另一方案。固定 Frobenius 块确实存在；但目标的单位对数位于 exact 原函数的端点值，以及 Kummer 对象的 Hodge 过滤和整格中。仅有 Frobenius 矩阵不提供其深度上界。

## 1. 固定开曲线及合法的 Frobenius 提升区域

令
$$
D=\operatorname{supp}\operatorname{div}\Phi=D_+\sqcup D_-,
\qquad \mathscr U=E\setminus D,
\qquad \omega=d\log\Phi.
$$
R19 中 $D_+,D_-$ 各有 $256$ 个互异几何点，所以 $|D|=512$。$D$ 与 $E$ 都固定，不随 $p$ 改变；$O\in\mathscr U$。

在任一特征零系数域中，残数正合列给
$$
0\longrightarrow H^1_{\mathrm{dR}}(E)
\longrightarrow H^1_{\mathrm{dR}}(\mathscr U)
\longrightarrow
\ker\left(\bigoplus_{Q\in D}\mathbf k[Q]
\xrightarrow{\ \sum\ }\mathbf k\right)
\longrightarrow0.
\tag{1}
$$
可先扩底使 $D$ 分裂，再下降。故
$$
\dim H^1_{\mathrm{dR}}(\mathscr U)=2+512-1=513.
\tag{2}
$$

这里不能把 $[\pi]$ 自动当作代数态射 $\mathscr U\to\mathscr U$：
$[\pi]^{-1}D$ 通常含有 $D$ 以外的点。以下恒等式先合法地定义在
$$
E\setminus(D\cup[\pi]^{-1}D)
$$
上：
$$
g_p=\frac{\Phi\circ[\pi]}{\Phi^p},
\qquad
d\log g_p=[\pi]^*\omega-p\omega.
\tag{3}
$$

在目标好普通素位处，$[\pi]$ 约化为绝对 Frobenius，且固定素于 $p$ 的 torsion 边界有互异约化。取好约化模型中 $\overline{\mathscr U}$ 的管状邻域，也就是去掉所有边界点的极点管。若 $P$ 约化在边界外，则 $[\pi]P$ 也约化在边界外。因此 $[\pi]$ 在此区域给出合法的 Frobenius 提升，且
$$
g_p\equiv1\pmod p.
\tag{4}
$$
所以
$$
J_p=\log_p g_p
$$
在这个区域收敛。它也延伸到足够小的严格邻域：在原 affinoid 上
$\|g_p-1\|\le p^{-1}$，稍微扩大后仍可保持 $\|g_p-1\|<1$。因此使用刚性或 overconvergent de Rham 上同调时，(3) 的右侧是一个合法 exact 微分。于是
$$
\boxed{\quad [\pi]^*[\omega]=p[\omega].\quad}
\tag{5}
$$
这条直线不为零，因为 $\omega$ 在 $D_+$、$D_-$ 上分别有留数 $+1,-1$。

式 (5) 的固定一维 Frobenius 数据只是特征值 $p$。它没有记录下面的 $J_p(P_\pi)$。

## 2. 实际目标全部落在被商掉的 exact 原函数端点值中

所有 $\mathfrak p$-torsion 点都在 $O$ 的形式群圆盘内。因此从 $O$ 到 $P_\pi$ 的积分可直接在该圆盘中按形式幂级数定义：
$$
I(P)=\int_O^P\omega=\log_p\Phi(P),
\qquad I(O)=0.
$$
由 (3) 和 $g_p(O)=1$，
$$
J_p(P)=I([\pi]P)-pI(P).
$$
特别地 $[\pi]P_\pi=O$，所以
$$
\boxed{\quad
I(P_\pi)=-\frac{J_p(P_\pi)}p,\qquad
\mathcal Q_p=
-\frac{e_\chi J_p(P_\pi)}{p\,\rho_\chi}.
\quad}
\tag{6}
$$
这是准确恒等式。它也重新得到 Coleman 塔笔记中的整 Frobenius 对数差。

因此只保留 (5) 的上同调类，等于将 $dJ_p$ 商掉；但目标正由 $J_p$ 在移动端点的值给出。这里还有一个明确的除 $p$，不能在丢掉原函数后从特征值恢复目标精度。

## 3. 相对上同调的维数和移动端点

在 $L=K_\mathfrak p(E[\mathfrak p])$ 上，只保留两个端点
$S_2=\{O,P_\pi\}$ 时，映射锥的长正合列给
$$
0\longrightarrow L
\longrightarrow L^{S_2}
\longrightarrow H^1_{\mathrm{dR}}(\mathscr U_L,S_2)
\longrightarrow H^1_{\mathrm{dR}}(\mathscr U_L)
\longrightarrow0.
$$
所以这个相对空间的维数为 $514$。但它包含实际端点 $P_\pi$，并定义在随 $p$ 变化、分歧度为 $p-1$ 的 $L$ 上。

若要同时保留完整的 Galois 端点 orbit，应取
$$
S_p=E[\mathfrak p].
$$
这有 $p$ 个几何点，故完整相对空间的维数为
$$
\boxed{\quad 513+(p-1)=p+512.\quad}
\tag{7}
$$
字符投影可进一步减少某些分量；但投影使用的正是阶 $p-1$ 的 tame 角色及其端点本征方向，不能在减少维数时再将这些数据删除。

还有一个容易混淆的 Frobenius 问题。集合映射 $[\pi]:S_2\to S_2$ 把两个端点都送到 $O$，故其对
$L^{S_2}/L$ 的拉回为零。因而直接将这个端点映射加到 (5) 上，会得到在端点方向不满秩的算子。它不是这个相对算术对象的可逆 crystalline Frobenius。

几何原因也可直接看出：这些标记点在模 $p$ 约化时全部重合在 $O$，原来的两端点模型不是标记点互异的好约化模型。若使用相对 crystalline 或 semistable 比较，必须保留分离端点所需的模型、下降及过滤信息；不能把朴素的端点压缩映射直接命名为 crystalline Frobenius。

## 4. 对实际单位给出的二维 Kummer 模型

上面的目标还可以放进一个真正的二维局部晶体对象。这说明“维数固定”本身不是问题的终点。

设 $\eta\in\mathcal O_L^\times$，考虑其 Kummer 扩张
$$
0\longrightarrow\mathbb Q_p(1)
\longrightarrow V_\eta
\longrightarrow\mathbb Q_p
\longrightarrow0.
\tag{8}
$$
所用外部输入是：单位的 Kummer 类为 crystalline；可选择晶体对数周期
$b_\eta\in B_{\mathrm{cris}}^+$，使
$$
g(b_\eta)=b_\eta+c_\eta(g)t_{\mathrm{cyc}},
\quad
\varphi(b_\eta)=p b_\eta,
\quad
\theta(b_\eta)=\log_p\eta.
\tag{9}
$$
这里 $c_\eta$ 是 Kummer cocycle，$t_{\mathrm{cyc}}$ 是 Tate 周期，避免与椭圆参数 $t$ 混用。该输入见 Brinon–Conrad 的 Lemma 9.2.7、Example 9.2.8；晶体性的一般表述也见 Lemma 8.3.9。

本处 $L/\mathbb Q_p$ 完全分歧，故最大不分歧子域为 $\mathbb Q_p$。采用反变约定
$$
D^*_{\mathrm{cris}}(V)
=\operatorname{Hom}_{\mathbb Q_p[G_L]}(V,B_{\mathrm{cris}}).
$$
取 (8) 的基 $v_1,v_0$，其中 $v_1$ 张成 Tate 子对象。定义两个晶体映射
$$
e_1(v_1)=0,\quad e_1(v_0)=1,
$$
$$
e_p(v_1)=t_{\mathrm{cyc}},\quad e_p(v_0)=b_\eta.
$$
由 (9) 它们均 Galois 等变，并构成一个基。直接计算给
$$
\boxed{\quad
\varphi(e_1)=e_1,\qquad\varphi(e_p)=p e_p.
\quad}
\tag{10}
$$
这个矩阵与 $\eta$ 无关。

过滤却包含实际单位对数。因为
$b_\eta-\log_p\eta\in\mathrm{Fil}^1B_{\mathrm{dR}}$，而
$t_{\mathrm{cyc}}$ 恰在第一层，得到
$$
\boxed{\quad
\mathrm{Fil}^0D^*_{\mathrm{dR}}=D^*_{\mathrm{dR}},
\qquad
\mathrm{Fil}^1D^*_{\mathrm{dR}}
=L\bigl(e_p-\log_p\eta\,e_1\bigr),
\qquad
\mathrm{Fil}^2D^*_{\mathrm{dR}}=0.
\quad}
\tag{11}
$$
式 (10) 与 (11) 分开说明了哪些数据被保留。

## 5. 正确 chi 分量及整格不能省略

在本题令 $\eta=\Phi(P_\pi)$。Kummer 映射与对数均线性，因此对
$e_\chi\eta$ 这个完成单位群中的元素应用同样构造即可：取各共轭 Kummer 类的 $\mathbb Q_p$ 线性组合，周期也取相同组合。其过滤系数是
$$
\ell_\chi=e_\chi\log_p\Phi(P_\pi)
=\rho_\chi\mathcal Q_p.
\tag{12}
$$
所以实际字符数据仍然位于 (11) 的过滤线中。其纯 Frobenius 矩阵仍是 (10)。这里没有把 $e_\chi\eta$ 当成未经证明存在的普通代数数幂；使用的是 Kummer cohomology 的线性结构。

还须保留规定的整格与基的归一化。把一个单位类 $x$ 改成 $p^s x$，其过滤参数变为 $p^s\ell_x$，局部深度增加 $s$；但纯 Frobenius 模块仍是同一个对角模块。甚至在允许任意有理缩放、忘记扩张的整 framing 时，非零标量倍数的这些二维扩张可彼此同构。

因此从一个未带过滤和整格的固定小 Frobenius 矩阵，不可能读取 R16–R24 所需的深度阈值。这个例子只说明所忘数据的必要性，不声称 $p^s x$ 仍是原始椭圆单位生成元，也不以任意局部单位代替实际全局单位。

## 6. 当前所得的正向接口与缺口

这次比较提供两个准确接口：

1. 固定开曲线中，$\omega$ 的 Frobenius 误差原函数 $J_p$ 在 $P_\pi$ 的 $\chi$ 值准确给目标，见 (6)。
2. 对该实际单位类，二维 crystalline Kummer 对象的过滤系数准确为 $\rho_\chi\mathcal Q_p$，见 (11)–(12)。

它们都保留了实际目标，没有把普通范数或其他角色偷换进来。但当前仍没有一个跨素数的统一过滤/整格比较，能对这些明确端点值给出所需的非零或浅深度。固定的 Frobenius 特征值、固定的理性维数和单位类逐素数非零，都没有替代这项输入。

## 来源与依赖

- O. Brinon、B. Conrad，*CMI Summer School Notes on p-adic Hodge Theory*，2009-06-24：
  [作者全文](https://math.stanford.edu/~conrad/papers/notes.pdf)，
  Lemma 8.3.9、Lemma 9.2.7、Example 9.2.8（印刷第125、140–142页）。
  本文只取单位 Kummer 晶体性与 (9) 的周期输入，随后显式核算基和过滤。
- R19：固定边界、$\Phi(O)=1$、全局单位值。
- R21、R24：目标字符与 $\rho_\chi$ 的正规化。
- Coleman 塔笔记：整 Frobenius 对数差；本文 (3)–(6) 与该正规化一致。
- 维数计数、端点映射以及 (10)–(12) 的线性计算已在本文给出。
