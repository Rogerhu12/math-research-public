# R244 后续附录：预解式自动给最小图核心与全部中间比例图的谱

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：完整证明的中间结构结论。真空有有界交换子原像时，逆算子的最小性不需要强主理想单位。秩二真见证产生的每一个闭交换中间比例图，都必对全部有界交换单位倍数及有界交换扰动具有空预解集。后一个结论仍不排除见证。

## 1. 所用的实际结构与去重

沿用实际 $A$、循环向量 $1$、共轭 $C$，并记 $\mathfrak C=A'$。
R88 给
$$
\mathfrak C=\overline{\mathbb C[I,A]}^{\mathrm{SOT}},
\qquad F^\top:=CF^*C=F\quad(F\in\mathfrak C).
\tag{1.1}
$$
R34 的 $X_h$ 表示
$p(A)1\mapsto p(A)h$ 的最小闭包。

本文已核 R34、R65 §1、R88、R169 §§2--5、R184 §§7--8：
R65 的最小/最大比例图及共轭转置对偶是已知输入；
有快 Bézout / 普遍强单位时的图正合也已由 R169/R184 支付。
R58 的指定等向核平方零谱二择、R201 的具体 first 比例谱障碍不被重计。
这里保留的是 (1.1) 使任意非空广义预解自动产生真空图核心，
及其对本轮真秩二中间图的统一应用。

所有闭算子的交换都包括定义域条件。
若闭算子 $T$ 满足
$A\operatorname{Dom}T\subseteq\operatorname{Dom}T$、$TA=AT$，
则其闭图被 $A^{(2)}$ 保持。
用 (1.1) 对图中两坐标同时取强极限，得到
$$
F\operatorname{Dom}T\subseteq\operatorname{Dom}T,\qquad TF=FT
\quad(F\in\mathfrak C).
\tag{1.2}
$$
这一步无需把图子空间的正交投影认作交换子。

## 2. 真空原像已足够给逆算子的完整最小图

**引理 2.1。** 若 $P\in\mathfrak C$ 单射且 $Pg=1$，则：

1. $\operatorname{Ran}P$ 稠密，$g$ 对 $A$ 循环；
2. $P^{-1}$ 在自然域 $\operatorname{Ran}P$ 上闭且稠密定义；
3. $P^{-1}=X_g$，多项式 $1$ 轨道和有限 Walsh 列都是其图核心。

**证明。** $\overline{\operatorname{Ran}P}$ 是闭 $A$ 不变空间且含循环向量 $1$，故它等于 $H$。
令 $M=\overline{\{p(A)g:p\in\mathbb C[z]\}}$。
(1.1) 使 $P$ 保持 $M$，所以 $1=Pg\in M$；再由 $1$ 循环，得 $M=H$。

$P^{-1}$ 的图为
$$
\{(Px,x):x\in H\},
$$
有界 $P$ 的连续性直接保证其闭性。其图范数参数化
$x\mapsto(Px,x)$ 是有界同构。
由于 $g$ 循环，$p(A)g$ 在 $H$ 中稠密，而
$$
(Pp(A)g,p(A)g)=(p(A)1,p(A)g).
$$
故这些多项式图向量在整个逆图中稠密，证明 $P^{-1}=X_g$。

有限 Walsh 核的同一结论使用 R176 §6 已证的有限 Walsh 乘子在
$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$ 中的范数稠密性。
对固定 $p(A)$，取有限 Walsh 向量 $u_n$ 的有界乘子
$X_{u_n}\to p(A)$（算子范数），且 $X_{u_n}1=u_n$。
它们与 $P$ 交换，故
$$
P X_{u_n}g=X_{u_n}Pg=u_n,\qquad
(u_n,P^{-1}u_n)=(X_{u_n}1,X_{u_n}g)
\longrightarrow(p(A)1,p(A)g).
$$
这把每个多项式图向量逼近为有限 Walsh 图向量，故该核同样图稠密。证毕。

这里没有使用 $I\in\overline{P\mathfrak C}^{\mathrm{SOT}}$。
单个向量 $Pg=1$ 与主理想的强单位是不同条件。

## 3. 任意闭交换扩张有预解点便自动最小且 C 自伴

**引理 3.1。** 设 $T$ 闭且稠密定义，满足 (1.2)，且 $1\in\operatorname{Dom}T$。
若存在
$$
U\in\mathfrak C^\times,\quad F\in\mathfrak C,\quad
\lambda\in\rho(TU+F),
\tag{3.1}
$$
则
$$
\boxed{T=X_{T1},\qquad T=T^\top.}
\tag{3.2}
$$

**证明。** 令 $B=F-\lambda I$、
$$
L=TU+B,\qquad P=L^{-1}.
$$
(1.2) 及 $U^{-1}$ 的同一性质给
$\operatorname{Dom}L=\operatorname{Dom}T$，
$TU=UT$ 于该域成立；$L$ 闭。
真实逆等式及 $A$ 的交换关系给 $P\in\mathfrak C$。
取 $g=L1\in H$，便有 $Pg=1$。

由引理 2.1，多项式 $1$ 轨道是 $P^{-1}=L$ 的图核心。
又
$$
L=UT+B,\qquad T=U^{-1}(L-B)
$$
使 $L$ 与 $T$ 的图范数等价，故该轨道也是 $T$ 的图核心。
在轨道上 $Tp(A)1=p(A)T1$，于是 $T=X_{T1}$。

还需证明最大 $C$ 对称性，而不仅是核心上的对称性。
由于 $P^\top=P$，直接对逆图取共轭伴随得
$(P^{-1})^\top=P^{-1}$。
有界交换单位 $U^{\pm1}$ 和 $B$ 保持
$\operatorname{Ran}P=\operatorname{Dom}P^{-1}$。
因此
$$
T=U^{-1}(P^{-1}-B)
$$
的共轭转置为
$$
(P^{-1}-B)U^{-1},
$$
其自然域与前式相同，作用也因交换性相同。
故 $T^\top=T$。证毕。

**推论 3.2。** 任何真正扩大 $X_h$ 定义域、仍闭且与 $A$ 交换的单值扩张，
对全部 $U\in\mathfrak C^\times,F\in\mathfrak C$ 都满足
$$
\sigma(TU+F)=\mathbb C.
\tag{3.3}
$$
否则引理 3.1 会把它重新等同于其真空最小图 $X_h$。
这里说的是预解集为空，不是谱为空。

## 4. 秩二链中的三个空间确实是比例算子的图

沿用本轮秩二真见证的广义预解数据
$$
R_i=(L_i-\lambda_i I)^{-1},\qquad
g_i=(L_i-\lambda_i I)1,\qquad R_ig_i=1.
$$
每个 $R_i$ 单射，且由引理 2.1，两个 $g_i$ 都循环。
有界链附录给
$$
N=\overline{\{(R_2x,R_1x):x\in H\}},\quad
K=\{(y_1,y_2):R_1y_1=R_2y_2\},
$$
$$
K_0=\overline{\{(p(A)g_1,p(A)g_2):p\in\mathbb C[z]\}},
\qquad N\subsetneq K_0\subsetneq K.
\tag{4.1}
$$
这里两个严格包含均已由真正迹与 $J^2=-I$ 的商结构证明。

由于 $R_2$ 单射，$K$ 没有非零垂直向量，且为闭图：
$$
K=\operatorname{Graph}T_{\max},\qquad
T_{\max}=R_2^{-1}R_1,\quad
\operatorname{Dom}T_{\max}=\{u:R_1u\in R_2H\}.
\tag{4.2}
$$
其定义域包含稠密的 $R_2H$。
$R_1$ 单射又使 $T_{\max}$ 单射；
其值域包含 $R_1H$，故稠密。

令
$$
h=R_1g_2.
$$
用循环的 $g_2$ 参数化 $N$，得到
$$
N=\overline{\{(R_2p(A)g_2,R_1p(A)g_2)\}}
=\overline{\{(p(A)1,p(A)h)\}}
=\operatorname{Graph}X_h.
\tag{4.3}
$$
因此 $T_{\min}=X_h$，并且 $1\in\operatorname{Dom}T_{\min}$、$T_{\min}1=h$。

$K_0$ 也为一个闭、稠密定义、单射且稠密像算子 $T_{\mathrm{mid}}$ 的图：
单值性由 $K_0\subset K$，域和像的稠密性分别来自 $g_1,g_2$ 循环；
在其真正核心上有
$$
T_{\mathrm{mid}}p(A)g_1=p(A)g_2.
\tag{4.4}
$$
它包含 $T_{\min}$，却严格大于 $T_{\min}$。
不能把 (4.4) 的循环参考向量 $g_1$ 换成 $1$ 后，仍无证声称是同一个最小图。

R65 §1 的已证对偶式在此可直接核验：对参数图
$(R_2x,R_1x)$，共轭转置图中的 $(u,v)$ 满足
$B(R_1x,u)=B(R_2x,v)$ 对所有 $x$ 成立。
$R_i^\top=R_i$ 将该条件准确化为 $R_1u=R_2v$，即最大比例图。
再取一次共轭转置并用最小图的闭性，得到
$$
\boxed{T_{\min}^\top=T_{\max},\qquad T_{\max}^\top=T_{\min}.}
\tag{4.5}
$$

## 5. 全部闭交换中间图均有全平面谱

**定理 5.1。** 在 (4.1) 的真秩二情形，取任意闭的 $A^{(2)}$ 不变空间 $E$，
满足 $N\subseteq E\subseteq K$。
它是单值、闭、稠密定义算子 $T_E$ 的图。
对全部有界交换单位 $U$ 和有界交换扰动 $F$，
$$
\boxed{\sigma(T_EU+F)=\mathbb C.}
\tag{5.1}
$$
特别包括 $T_{\min},T_{\mathrm{mid}},T_{\max}$，以及交换两个坐标后的逆比例图。

**证明。** 图的单值性、闭性与稠密定义同上，且 $N\subset E$ 给
$1\in\operatorname{Dom}T_E$、$T_E1=h$。
图不变性给 (1.2)。

若 (5.1) 在某组 $U,F$ 处失败，引理 3.1 同时给
$$
T_E=X_h=T_{\min},\qquad T_{\min}=T_{\min}^\top.
$$
再用 (4.5)，得到 $T_{\min}=T_{\max}$，即 $N=K$，与 (4.1) 矛盾。
交换两坐标后，$R_1,R_2$ 的角色对调，同一证明适用。证毕。

本定理没有把每个参数分类为连续谱点：
这还需要关于有界铅笔 $R_1-\lambda R_2$ 的核及值域的额外事实，
此处不作假设。
它也没有证明 $E$ 的所有闭算子实现都自伴；(5.1) 正好禁止用
某个有界广义预解式消去中间图缺口。

## 6. 聚合分解中只简化逆最小性这一步

R244 聚合附录曾在 $Pg=1$ 之外使用一组有界强单位 $PU_n\to I$，
来同时获得逆最小性和正常泛函的往返表示。
引理 2.1 说明：在逆最小性、$g$ 循环和有限 Walsh 核这一步，
$Pg=1$ 本身已经足够。

但本文没有去掉整个往返表示中的强单位条件。
从
$$
\phi(PF)=B(Fh,1)\quad(F\in\mathfrak C)
$$
转回 $\phi(F)=B(Fg,h)$，需要控制原泛函在全部指定输入上的极限，
不能只用 $P^{-1}$ 的单个图核心。
本轮秩二真见证的个别理想结论恰好给出条件性的提醒：
每个 $R_i$ 都有 $R_ig_i=1$ 和最小逆，
原正泛函仍被证明满足 $\phi_\rho(R_iF)=0$，而 $\phi_\rho(I)>0$。
这没有构成矛盾，表明缺失的主理想密度不能由逆最小性替代。

本稿继续保留原共同域和真实正矩的未解部分；普通 Hilbert ISP 尚未完成。


相关完整输入：[广义预解及最大商](R244-appendix-generalized-resolvent-unit-classes-and-vacuum-word-domains.md)、[秩二链与严格双图缺口](R244-appendix-rank-two-koszul-defect-and-double-common-graph-gap.md)、[删一因子的真实输入域](R244-appendix-cofactor-input-domains-and-individual-resolvent-annihilation.md)。
