# R1188：原 Jacobian 内的有限挠点网格、实际商模型与平衡 Lie 形式

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**状态：已证明。** 本篇从同一个原 Jacobian 的实际有理射影模型，直接给 R1187 小度子簇与实际同态图的有理方程系数界；进一步在有限图列表上构造原全实端态域和一个有界有理平衡交错型。证明使用有限挠点网格和 Plücker 坐标，保留原有理结构，不将稳定 Faltings 高度直接当作任意 $\mathbf Q$-twist 的坐标高度。

这里的模型界只含原 $J$ 的一份固定有限代数数据及 R1187 的显示数，不再独立含目标 $C$ 的任意模型。实际目标可取原 $J$ 内的 $B$，与原 $C$ 之间保留 R1187 的两个明确有界同源；同一个原 $c_0,c_1,D_0$ 和点 $\beta$ 的运输逐项写出。本文未执行数学程序，也不声称这些很大的有效界已经使 R1182 的隔离半径覆盖整个 $p^3$ 盘。

## 1. 固定原嵌入与需要控制的实际图

保留 [R1187](R1187-original-bounded-half-rank-quotient-and-polarization.md) 的 $J=J_{X_1}$、$g$、$C$、$q_*$、$\mathcal L$、$R,\Gamma,U$。置

$$
Q=9R^2,\qquad T=q_*^\dagger q_*\in\operatorname{End}_{\mathbf Q}(J),
\qquad B=\operatorname{im}T=\operatorname{im}q_*^\dagger\subset J,
\qquad n=\dim B=2f.
\tag{1188.1}
$$

写 $i:B\hookrightarrow J$，并把同一个 $T$ 的值域缩到 $B$，记为 $T_B^{\rm quo}:J\twoheadrightarrow B$；下文不混淆它与端态 $T$。有

$$
T_B^{\rm quo}N=0,\qquad
\beta_B=T_B^{\rm quo}(D_0)=q_*^\dagger\beta_*\ \text{非挠},
\qquad
\beta_B=-3\,T_B^{\rm quo}[c_0-c_1].
\tag{1188.2}
$$

在原 $J$ 上取有理对称线丛

$$
\mathscr H=(\Theta_0\otimes[-1]^*\Theta_0)^{\otimes3}.
\tag{1188.3}
$$

它的 Néron–Severi 类为 $6\Theta$，完整线性系给射影正规闭嵌入

$$
J\hookrightarrow\mathbf P^{s},\qquad s+1=6^g.
\tag{1188.4}
$$

固定这份嵌入的有理方程、原点、群律开覆盖公式，以及倍二四次式与齐次 Nullstellensatz 证书。由 R1185 §6 的同一证明，可从它们得到一个实际整数 $E_J\ge0$，使

$$
|h_{\mathscr H}([2]P)-4h_{\mathscr H}(P)|\le E_J,
\qquad
|h_{\mathscr H}(P)-\widehat h_{\mathscr H}(P)|\le E_J/3.
\tag{1188.5}
$$

因挠点的规范高度为零，置

$$
H_J=\max\{1,\lceil E_J/3\rceil\},
$$

则全部 $P\in J(\overline{\mathbf Q})_{\rm tors}$ 都满足 $h_{\mathscr H}(P)\le H_J$。Segre 嵌入的 $J\times J\subset\mathbf P^{6^{2g}-1}$ 上，挠点的高度至多 $2H_J$。

这一输入只来自原 $J$ 的实际倍二公式，未选择未知的目标坐标，也没有挠点阶数或挠点域度的隐藏限制。

## 2. 挠点网格准确检测低次方程

**引理 1188.1。** 设 $A\subset\mathbf P^s_{\mathbf Q}$ 是阿贝尔簇的一份闭嵌入，$B\subset A$ 是正维有理阿贝尔子簇。记 $b=\dim B$、$L=\mathcal O(1)|_B$、$\delta=(L^b)$。给定整数 $d\ge1,M\ge1$，若 $M^2>d\delta$，则

$$
I_B(d)=\ker\!\left(
 \overline{\mathbf Q}[X_0,\ldots,X_s]_d
 \longrightarrow\bigoplus_{P\in B[M](\overline{\mathbf Q})}
 \mathcal O(d)|_P\right).
\tag{1188.6}
$$

右边只检查同一个 $B$ 的有限挠点网格。

**证明。** 包含关系 $I_B(d)\subset\ker(\mathrm{ev})$ 显然。反之，若 $F$ 不恒零于 $B$，它限制为 $L^d$ 的非零截面，有有效 Cartier 除子 $D$，满足

$$
\deg_LD=(D\cdot L^{b-1})=d\delta.
$$

若 $F$ 消于全部 $B[M]$，则在特征零的有限 étale 映射 $[M]:B\to B$ 下，局部范数方程表明

$$
\operatorname{mult}_0([M]_*D)
=\sum_{P\in B[M]}\operatorname{mult}_P(D)
\ge M^{2b}.
\tag{1188.7}
$$

这里在完备严格局部环上把 $[M]$ 分为每个挠点附近的 étale 分支；范数是各分支局部方程的乘积，因此阶数相加，不只计一个经过零点的像分支。

投影公式及 $[M]^*L\equiv M^2L$ 给

$$
\deg_L([M]_*D)=M^{2b-2}d\delta.
\tag{1188.8}
$$

在给定射影嵌入中，一个有效除子在某点的重数不超过总度：取经过该点的 $b-1$ 个一般超平面作适当交，局部交数至少该重数，且全部交数非负。由 (1188.7)–(1188.8) 得 $M^2\le d\delta$，矛盾。$b=1$ 时同一论证就是零维除子总次数。证毕。

特别地，若 $\delta\le\Delta$，可统一取

$$
d=\Delta,\qquad M=\Delta+1.
\tag{1188.9}
$$

## 3. 有理 Plücker 坐标给显示整系数界

进一步假设 $A$ 的全部挠点在固定嵌入中高度至多整数 $H\ge1$。令

$$
N_{s,d}=\binom{s+d}{d},\qquad
\mathcal A(s,d,H)=N_{s,d}!\,3^{N_{s,d}dH}.
\tag{1188.10}
$$

在次数 $d$ 的全部单项式序下，把 $P\in B[M]$ 的 evaluation 写为一个射影行向量 $v_P$。Veronese 高度的准确倍率给

$$
h(v_P)=d\,h(P)\le dH.
$$

取其中 $r$ 个线性无关行，其张成的行空间为 $W$。全部网格在 $\mathbf Q$ 上 Galois 稳定，故 $W$ 定义在 $\mathbf Q$ 上。其非零 Plücker 向量 $v_1\wedge\cdots\wedge v_r$ 满足

$$
h(\operatorname{Pl}(W))
\le\sum_{i=1}^r h(v_i)+\log(r!)
\le r dH+\log(r!).
\tag{1188.11}
$$

有限处行列式用最大范数，无穷处用至多 $r!$ 个乘积；对定义域全部地方归一化求和即得该式，因此无定义域次数因子。

因 Plücker 点有理，取其本原整数坐标 $(p_I)$，有

$$
\max_I|p_I|=\exp h(\operatorname{Pl}(W))
\le r!\exp(rdH)\le\mathcal A(s,d,H).
\tag{1188.12}
$$

选择一个 pivot 集合 $I=\{i_1,\ldots,i_r\}$，$p_I\ne0$。对每个非 pivot 列 $j$，Cramer 恒等式给 kernel 向量

$$
w_j=p_I e_j-
 \sum_{a=1}^r\epsilon_{I,a,j}\,p_{I-\{i_a\}\cup\{j\}}e_{i_a},
\qquad \epsilon_{I,a,j}\in\{1,-1\},
\tag{1188.13}
$$

其中符号按重排列序固定。这些向量线性无关，且在 $\mathbf Q$ 上生成 kernel。每个系数都是某个带号的本原整数 Plücker 坐标，故绝对值受 (1188.12) 控制。

这里得到的是**一组具有整数系数的 $\mathbf Q$-基**；不声称它已经是 kernel 与 $\mathbf Z^{N_{s,d}}$ 之交的饱和整数基。截出同一射影子簇只需要这个 $\mathbf Q$-方程空间，因而无需反除未知 pivot 后伪称所有分母消失。

结合引理 1188.1，得到：$I_B(\Delta)$ 有一组整数系数的 $\mathbf Q$-基，每个系数绝对值至多 $\mathcal A(s,\Delta,H)$。

## 4. 这些固定次数方程确实切出原子簇

还须证明不是只得若干可能不足的低次方程。对任一几何点 $P\notin B$，取通过 $P$、与 $B$ 不交的适当一般线性空间，再在其中选不含 $P$ 的投影中心，得到

$$
\pi:\mathbf P^s\dashrightarrow\mathbf P^{b+1}
$$

使中心与 $B$ 不交、$\pi|_B$ 泛有限，且 $\pi(P)\notin\pi(B)$。这些条件是非空开条件：$P$ 的纤维可选为一个通过 $P$ 的一般 $s-b-1$ 维线性空间，它与 $B$ 的预期交维数为 $-1$。

$\pi(B)$ 是次数至多 $\delta$ 的超曲面。拉回其方程，得到一个次数 $d_P\le\delta$、消于 $B$ 却不消于 $P$ 的齐次式。若 $d_P<\Delta$，乘一个不消于 $P$ 的线性式的 $\Delta-d_P$ 次幂，升到准确次数 $\Delta$。所以 $I_B(\Delta)$ 的公共几何零点正是 $B$。

若 $B$ 本身已经是超曲面，可取恒等投影；没有外点的满射影空间情形无需此论证。本文的正维阿贝尔子簇均处于上述正常情形。

于是由 §3 的有限整系数方程 $F_1,\ldots,F_v$ 得

$$
I_B=\sqrt{(F_1,\ldots,F_v):
 (X_0,\ldots,X_s)^\infty}.
\tag{1188.14}
$$

这给原 $B$ 的有理 reduced scheme；它本来光滑，故没有另一个需要选择的正规化分支。

## 5. 应用到原小度子簇和实际商图

### 5.1 子簇 $B$ 的方程

R1187 (1187.41)–(1187.42) 给

$$
h^0(B,\Theta_0|_B)\le3^g\Gamma Q^n.
$$

因此其在 (1188.4) 中的次数满足

$$
\deg_{\mathscr H}B
=6^n n!h^0(B,\Theta_0|_B)
\le\Delta_B:=18^g g!\Gamma Q^g.
\tag{1188.15}
$$

由 §§2–4，原 $B$ 被一组次数准确为 $\Delta_B$、整系数绝对值至多

$$
\boxed{\quad
\mathcal A(6^g-1,\Delta_B,H_J)
\quad}
\tag{1188.16}
$$

的有理方程 set-theoretically 切出；(1188.14) 取得其准确理想。

### 5.2 实际端态 $T$ 的图

因 $T$ 自伴半正、$\operatorname{Tr}T\le Q$，其复切空间上的特征值 $\lambda_1,\ldots,\lambda_g$ 属于 $[0,Q]$。图

$$
\Gamma_T=\{(x,Tx):x\in J\}\subset J\times J
$$

是定义在 $\mathbf Q$ 上的实际阿贝尔子簇。Segre 超平面拉回到图为 $\mathscr H\otimes T^*\mathscr H$，故

$$
\deg\Gamma_T
=6^g g!\prod_{i=1}^g(1+\lambda_i^2)
\le\Delta_T:=6^g g!(1+Q^2)^g.
\tag{1188.17}
$$

图中的挠点是 $(P,TP)$，两坐标都是原 $J$ 的挠点，其 Segre 高度至多 $2H_J$。再次应用同一个引理，图由次数 $\Delta_T$、整系数绝对值至多

$$
\boxed{\quad
\mathcal A(6^{2g}-1,\Delta_T,2H_J)
\quad}
\tag{1188.18}
$$

的方程 set-theoretically 切出。

因此这里给的是实际**有理映射图**的系数界。第一投影 $\Gamma_T\to J$ 原本是同构；由图取得 $T$ 的局部有理公式、$B$ 的像以及 $T_B^{\rm quo}$，都可以在这有限系数输入上作代数消元。不会因为只认出一个几何同构类而漏掉原 $\mathbf Q$-twist。

## 6. 由有限方程界得到真正可终止的模型成本函数

固定原 $J$ 数据和显示参数后，(1188.16)、(1188.18) 的整数多项式只有有限多个；每组方程最多需要对应单项式空间的维数那么多个。可以枚举全部这些有限列表，并分别计算饱和根理想、维数、光滑性以及与固定 $J$ 或 $J\times J$ 的包含关系。

子群条件可在原群律的有限 affine covers 上验证；包含原点、连通以及加法/逆的稳定性都是有限代数条件。对一个连通阿贝尔子群 $G\subset J\times J$，检查第一投影像的维数为 $g$、以及其核为长度一的零点，就确认该投影是同构，因而 $G$ 是一个实际端态图。此处不以某个未经求值的同构存在性作为停止判据。

对通过这些检验的有限列表，运行相同的射影消元与局部 Jacobian minor 程序，可输出：准确 reduced 方程；原点坐标；群律的有限开覆盖公式；由图取得的映射；原点的一组有理 Lie 坐标基；在原 $X,c_1$ 上与既有 Abel 映射复合的实际拉回微分。

用于 R1182/R1185 的目标嵌入也须完整取得：原 $H^0(J,\mathscr H)$ 到 $H^0(B,\mathscr H|_B)$ 的限制不预设满射。由准确理想计算后者的全部有理截面，使用它的完整线性系；$\mathscr H|_B$ 本身是一个对称 ample 线丛的三次幂，故该完整嵌入射影正规。也可再取其对称三次幂并计算全部截面。以有限代数后处理取得坐标变换、原点、倍二四次式及齐次 Nullstellensatz 证书，将其全部系数及次数一起纳入下面的有限最大值。这样不会把原嵌入的一个不完整截面子系误作满足 FP 与倍二公式条件的完整目标嵌入。

每个程序在所标记的光滑图上终止，列表有限，所以取全部输出的次数、分子分母和系数范数的最大值，得到只依原 $J$ 数据、$g,D_p$ 的**可计算整数模型成本函数**。这是有限集合上的有限算法，不诉诸一个未知的 Shafarevich 有效性定理。实际 $B,\Gamma_T$ 必在该列表中，故其输出由这个函数覆盖。

这一程序无需判断列表里哪些其它阿贝尔簇也有原半秩。实际对象由 (1188.1) 的图及同源确定；本文只用整个有限列表的最大值作安全系数界。

## 7. 原全实端态域与有理平衡形式也可在有限列表内取得

仅有模型界还不能默认已选择的 $F_0$-基和 $\Omega$ 便有小系数。本节为同一实际 $B$ 给一个有限构造。

令 $L_B=\mathscr H|_B$，$e_B=\deg\lambda_{L_B}$。由 (1188.15)

$$
e_B=h^0(B,L_B)^2
=\left(\frac{\deg_{L_B}B}{n!}\right)^2\le\Delta_B^2.
\tag{1188.19}
$$

对非零实际端态 $u$，$e_Bu^\dagger u$ 是整数端态，故

$$
\|u\|^2\ge1/e_B\ge\Delta_B^{-2}.
\tag{1188.20}
$$

这里不用非主极化下不成立的“Rosati 自动保持整数端环”。同一个 GR 类的界给

$$
\operatorname{vol}\operatorname{End}_{\mathbf Q}(B)
\le U^{8g^4},\qquad
\operatorname{rank}\operatorname{End}_{\mathbf Q}(B)\le4g^2.
$$

Minkowski 第二定理于是给一个在 $\mathbf Q$ 上生成 $\operatorname{End}_{\mathbf Q}^0(B)$ 的实际端态族，其每个范数不超过

$$
S=(4g^2)^{2g^2}U^{8g^4}\Delta_B^{4g^2}.
\tag{1188.21}
$$

对这样的 $u$，在同一 Segre 嵌入内有

$$
\deg\Gamma_u
\le\deg_{L_B}B\,(1+\|u\|^2)^n
\le\Delta_{
\rm End}:=\Delta_B(1+S^2)^g.
\tag{1188.22}
$$

因 $\Gamma_u\subset B\times B\subset J\times J$，其挠点高度仍至多 $2H_J$。故 §§2–4 再次给实际这些端态图的有限系数界

$$
\mathcal A(6^{2g}-1,\Delta_{\rm End},2H_J).
\tag{1188.23}
$$

枚举该有限图列表，验证它们确是所选 $B$ 的有理端态，并求其在有理 Lie 空间上的导数矩阵。特征零时，阿贝尔簇同态的导数忠实；因此矩阵的 $\mathbf Q$-线性独立性及乘法关系，准确检测端态代数的同一关系。

对本原 $B$，已由 R1011 和实际同源知道

$$
F_B=\operatorname{End}_{\mathbf Q}^0(B)\simeq F_0,
\qquad [F_B:\mathbf Q]=f=n/2,
$$

且 $F_B$ 全实。§7 的有限列表含一个实际生成族，所以从中选 $f$ 个线性无关矩阵就得到原 $F_B$ 的一组有理基。无需把一个猜测的最大几何端态环代入。若同时对整个候选模型列表取界，则枚举全部这样的 $f$ 元子集并通过有理乘法、数域因式分解和实根隔离，保留张成全实 $f$ 次域、且包含单位的子集；其中必有实际所需的一组。

令 $V_B=\operatorname{Lie}(B)(\mathbf Q)$，这是 $F_B$ 上二维空间。先取模型提供的一组有理基 $v_1,\ldots,v_n$；选择一个非零 $e_1$，再取一个不属于 $F_Be_1$ 的基向量 $e_2$。全部判断均是有限有理线性代数。写

$$
v=a_1e_1+a_2e_2,\qquad w=b_1e_1+b_2e_2,
$$

定义

$$
\Omega_B(v,w)=\operatorname{Tr}_{F_B/\mathbf Q}
 (a_1b_2-a_2b_1).
\tag{1188.24}
$$

该型非退化、交错，并满足 $\Omega_B(cv,w)=\Omega_B(v,cw)$。其矩阵由上述有限图、导数和有理矩阵逆给出。清分母后取整矩阵系数的公因子归一，得到一个明确的有理标量类；在整个有限列表上取这些输出高度的最大值，便给同一模型基中的 $\Omega_B$ 一个可计算的系数界。

这一步构造的是原 Mordell–Weil $F_B$-线所需的平衡型，不将只有 $p$ 进系数的 $\log\beta_B$ 混进数域结构或系数高度中。

## 8. 同一 $\beta$、Lie 空间及坏约化处的实际格运输

R1187 给同一原目标间的有界同源

$$
\iota=q_*^\dagger:C\to B,\qquad
\rho=q_*|_B:B\to C,
\qquad \deg\iota\deg\rho\le Q^{2n}.
\tag{1188.25}
$$

因此 $\beta_B=\iota\beta_*$，全部对数和 $F$-作用按实际 $d\iota$ 运输。维数 $2f$、秩 $f$、Mordell–Weil 的一维 $F_B$-结构，以及有理 Lie 空间与对数线交零均保持。实际 Abel 映射是 $x\mapsto T_B^{\rm quo}[x-c_1]$，仍以原 $c_1$ 为零点；不是用一个新的 CM 点替代 $c_0$。

还有一个对所有有限素数均有效的 Néron 格比较。令

$$
V=T_B^{\rm quo}i\in\operatorname{End}_{\mathbf Q}(B),
\qquad d=\deg V.
$$

在 $C$ 上它对应 $q_*q_*^\dagger$，故

$$
1\le d\le Q^{2n}.
\tag{1188.26}
$$

$d$ 杀掉 $\ker V$，所以 $[d]V^{-1}$ 是实际有理端态。置

$$
\mathcal R=[d]V^{-1}T_B^{\rm quo}:J\longrightarrow B,
\qquad \mathcal R i=[d].
\tag{1188.27}
$$

固定任一局部素数 $q$，包括坏约化的 level $p$。在各自的 Néron Lie 格中写 $\Lambda_J,\Lambda_B$，并以 $di$ 把 $V_B(\mathbf Q_q)$ 视为 $\operatorname{Lie}(J)(\mathbf Q_q)$ 的子空间。实际同态延伸到 Néron 模型，故 $di(\Lambda_B)\subset\Lambda_J$ 且 $d\mathcal R(\Lambda_J)\subset\Lambda_B$。对

$$
\Lambda_{\rm sat}=V_B(\mathbf Q_q)\cap\Lambda_J
$$

用 (1188.27) 逐向量得到

$$
\boxed{\quad
d\Lambda_{\rm sat}\subset di(\Lambda_B)
\subset\Lambda_{\rm sat},
\qquad v_q(d)\le2n\log_q Q.
\quad}
\tag{1188.28}
$$

式中第一个 $d$ 是整数次数，$di,d\mathcal R$ 是微分；它们不混用为某个未付的模型换基。该式只用 Néron 函子性和实际双向复合，不假设 $J$ 或 $B$ 在 $q$ 好约化。它把新目标格的额外同源指数控制在一个显示整数以内；原 $J$ 的 Néron 格与所选有理坐标基之间的资料仍须来自原模型。

## 9. 对原 O4 首项高度接口的作用和范围

通过 (1188.16)、(1188.18)、(1188.23) 和有限代数后处理，原半秩问题可在实际 $B\subset J$ 上工作：方程、原点、群律、商图、$F_B$-矩阵和一个有理平衡交错型，都受原 $J$ 数据及显示参数的可计算函数控制。原 $\beta_B$ 是同一 $D_0$ 的明确像，其高度和同源成本由 R1185、R1187 及 (1188.25) 运输。

在 R1184 的同一参数 $t=b-1=p^3w$ 中，新 Abel jet 必须按 $T_B^{\rm quo}$ 和实际基重算。把上述有限模型输出交给 R1186 的隐函数程序，就得到该实际 jet 的共同分母及全部首项系数高度。Néron 格与模型基的比较可使用 (1188.28)，但不能把原 $J$ 尚未写出的格数据设为单位矩阵。

本篇没有从一个固定小度数值推断任意已给坐标的高度，也没有用稳定 Faltings 高度略去 $\mathbf Q$-twists。所获得的是一份有限可取出的**原有理嵌入图**模型及完整运输。后续仍须将原 $J$ 的实际坐标和局部格成本代入，比较 R1182 的完整余项半径；一个很大的有效半径并不自动覆盖所有原候选。

## 10. 来源

1. [R1187](R1187-original-bounded-half-rank-quotient-and-polarization.md) §§1–10：小实际 $q_*$、完整 Tate 迹、$U,\Gamma,R$、有界实际 $C\rightleftarrows B$、同一原 $D_0$ 与 $\beta$。本文不重复登记该主定理。
2. Éric Gaudron–Gaël Rémond, *Polarisations et isogénies*, **Duke Math. J. 163 (2014), 2057–2108**，[正式作者 PDF](https://lmbp.uca.fr/~gaudron/art13.pdf)：Definitions 2.4、2.6，Propositions 2.5、2.8–2.9 和 Lemma 3.1，pp.2064–2069；本文 §7 同样保非主极化时的整数分母。
3. Éric Gaudron–Gaël Rémond, *Nouveaux théorèmes d’isogénie*, **Mémoires SMF 176 (2023)**，[正式 PDF](https://smf.emath.fr/system/files/filepdf/smf_mem_176_0.pdf)：§1.2 与 Theorems 1.3、1.8，印刷 pp.2–7；继续使用原 $J$ 生成的类，无另一个未知目标高度。
4. [R1185](R1185-original-CM-point-height-and-quotient-cost.md) §6 的实际四次倍二公式与 Nullstellensatz 证书，给本篇原 $E_J$；[R1186](R1186-original-Abel-jet-height-and-a-priori-precision.md) 接收本篇有限模型输出。
5. 本篇 §§2–5 的挠点网格检测、原有理 Plücker 整坐标与次数齐次化证明均在正文自证。§8 的局部格比较直接来自两个实际同态的 Néron 延伸及复合恒等式，不使用未付的好约化假设。
