# R724：原 Chow–Heegner 轨道给出的高度矩阵、规范局部求值与有限排根证书

日期：2026-11-14。状态：**下述原高度的构造性求值公式、所需有理点基的构造和严格排根证书已证明。** 输入必须是同一个实际代数模型、对应、线丛和刚性化；本文没有生成一般 $p$ 的全部模型，也没有计算出 $137147$ 的真实高度首项或宣布其候选排除。

R703/R716 使原外积的非零性与尾部可由代数数据控制，但还留下实际 $\Lambda$、$d_i$、$\ell_h$ 的有限规范输入。本文说明如何从原代数群、线丛及 $\eta_h$ 求这些输入：不把任意曲率原函数当成规范高度，不把 Abel 首项当成高度首项，也不另假设 $p$ 进高度配对非退化。

## 1. 保留全部原对象

固定 R593/R596/R616/R634 的

$$
X=X_1,\quad Y=W_p,\quad J=J_X,\quad B=J_Y,\quad
q:J\longrightarrow A,\quad \phi:X\longrightarrow Y,
$$
$$
P_X(x)=[x-c_0],\quad P_Y(x)=[\phi(x)-\phi(c_0)],\quad
\beta=q[c_1-c_0],\quad s=a-1.
\tag{724.1}
$$

保留实际 $\kappa=qq^\dagger$、$F^0=\ker\operatorname{Tr}(\kappa\,\cdot)$、原全局角色 $\chi$、原 Poincaré 刚性化、$c_{\rm clear},c_{\rm triv},C_h$ 和按 $c_0$ 归一的实际截面 $s_h$。同一高度约定是

$$
\widehat h_{\mathscr L_h}(P)
=\widehat h_{\mathcal L_h}(qP)
       +2h_Y(\phi_*P,\eta_h).
\tag{724.2}
$$

这里 $h_Y$ 是 R593 的 theta 高度极化后的双线性配对；Poincaré 对 $(P,\lambda_YQ)$ 的全局高度为 $2h_Y(P,Q)$。本文所有矩阵中的因子 $1/2$ 都来自这个约定。

在使用原外积时假定同一个 R616 乘积非零。对 $p=137147$，该前提现已由公开 R719 的严格原平均界证明。记

$$
\Lambda_h(x)=\lambda_{p,h}(x)-2\ell_h(\log P_Y(x)).
\tag{724.3}
$$

实际候选的坏处靶值仍为 R696 的零；全局几何没有改成另一个 $c_0$ 盘或另一个三次扭曲商。

所谓代数输入包括：曲线及 Jacobian 的有效坐标图、实际有理同态或对应、原线丛的过渡函数及 tensor 同构、原无零截面，以及 de Rham 上同调和杯积的代数模型。下面的群计算也可在 Jacobian 的除子/Riemann–Roch 坐标图内实施；不要求先写出一个最小 Weierstrass 或低次数平面模型。若这些模型尚未求出，不能把本求值公式称作已经执行。

## 2. 改变 $Y$ 的 splitting 时，原 $\Lambda$ 精确不变

先说明为何可以选代数、按等型块分解的 $Y$ splitting，而不改变原外积。

设 $h_Y^0$ 是一个与 $J_H$ 及其同源补空间相容的参考高度，保持同一 $\chi$、Poincaré 双扩张、刚性化和所有 $p$ 外局部项。R596 已证明原高度之差为

$$
h_Y(P,Q)-h_Y^0(P,Q)
 =D(\log P,\log Q)
\tag{724.4}
$$

其中 $D$ 始终指同一双扩张的局部 splitting 差诱导的双线性形式，
而不是从有理点上的全局等式反求一个任选延拓；并规定了在整个 Lie 空间上的实际延拓

$$
\ell_h(v)=\ell_h^0(v)+D(v,\log\eta_h).
\tag{724.5}
$$

这里不是只在有理对数的像上任意选一个延拓。

**引理 724.1。** 使用与 (724.4) 相同的两个规范 Poincaré splittings，原截面上的局部函数满足

$$
\lambda_{p,h}(x)-\lambda^0_{p,h}(x)
       =2D(\log P_Y(x),\log\eta_h).
\tag{724.6}
$$

从而

$$
\Lambda_h=\lambda^0_{p,h}-2\ell_h^0(\log P_Y)
\tag{724.7}
$$

作为同一整盘上的函数精确成立。

证明。两个 Poincaré $\chi_p$-splittings 的差在标量纤维上为零，所以下降到基底上的连续双加性函数。它通过两个群对数，并且正是全局配对之差，因为其他地方的局部项没有改变。按 (724.2)，这个 Poincaré 差为 $2D$。

原修正线丛的 $Y$ 部分是 $\phi_*^*\lambda_Y(\eta_h)$。将 $2D$ 拉回便得 (724.6)。完整 $\mu_3$ 范数、tensor 幂和最后除以 $C_h$ 都是线性的；不能在此漏掉范数或另删 Picard 零次项。在 $c_0$，$P_Y=0$ 且实际截面等于刚性化 $1$，所以没有附加常数。与 (724.5) 相减即得 (724.7)。$\square$

可以对 $B$ 的每个有理简单等型块选代数 Lagrangian 补空间，再取直和。各个中心投影在 Rosati 下自伴，因为不同有理简单等型块没有非零同态。因此所得规范高度在不同块间正交。这样的补空间只需有限代数线性运算，不要求 ordinary 或 unit-root splitting。

$A$ 的 splitting 另按 R699 选为代数、$F$ 与 $\mu_3$ 相容；改变它不改变原 $E_{ij}$。这两种允许的选择用途不同：前者在 $\Lambda$ 中精确抵消，后者在外积中精确抵消。本文没有允许任意跨因子的 splitting 后再删交叉项。

## 3. 原 $\eta_h$ 自身提供所需的 Mordell–Weil 基

取 $F^0$ 的有限个有理基元 $h_1,\ldots,h_r$，并清除原 $\eta_{h_i}\in B(\mathbb Q)\otimes\mathbb Q$ 的分母。写有理同源分解

$$
B\sim_{\mathbb Q}\prod_{\alpha} B_\alpha^{m_\alpha}.
\tag{724.8}
$$

这里明确使用本题的 GL$_2$-type 输入：实际 Hecke 域有
$F_\alpha\hookrightarrow\operatorname{End}_{\mathbb Q}^0(B_\alpha)$，
且 $[F_\alpha:\mathbb Q]=\dim B_\alpha$；重数块包含 R596 的真实矩阵代数
$M_{m_\alpha}(F_\alpha)$。仅有 $\operatorname{rank}_{\mathbb Q}=\dim$ 而没有
这个域作用，并不足以使一个点成为循环向量。这里的实际 Hecke 基来自
R596 §4 的完整 adelic Hecke 代数，包括水平素数处的算子及有限块分离；
不是只用未分歧的交换 Hecke 子代数。称一个块为活跃块，如果至少一个
$\eta_{h_i}$ 在该块的投影于有理点的 $\mathbb Q$-张量中非零。
令 $B_\eta$ 为所有活跃块的完整等型部分，$e_\eta$ 为其中心投影，
$b=\dim B_\eta$。

**定理 724.2。** 有

$$
\eta_h=e_\eta\eta_h,\qquad
\operatorname{rank}B_\eta(\mathbb Q)=b,\qquad
\log:B_\eta(\mathbb Q)\otimes\mathbb Q_p
          \xrightarrow{\sim}\operatorname{Lie}(B_\eta)(\mathbb Q_p).
\tag{724.9}
$$

而且可仅从原 $\eta_{h_i}$ 和实际有理 Hecke 自同态的有限轨道构造
$B_\eta(\mathbb Q)\otimes\mathbb Q$ 的一组基 $P_1,\ldots,P_b$。

证明。R596 给每个 $\eta_h=e_H\eta_h$；故每个活跃块都在 $J_H$ 内。
该块的简单因子满足
$B_\alpha(\mathbb Q)\otimes\mathbb Q\simeq F_\alpha$
作为 $F_\alpha$-模，并且其对数同构。因此整个重数块的有理点空间是
$F_\alpha^{m_\alpha}$，是 $M_{m_\alpha}(F_\alpha)$ 的简单模。
一个非零向量在该矩阵代数下生成全部空间。对每个活跃块，施加一组有限
$\mathbb Q$-基的实际 Hecke 算子于原非零投影，就得到该块有理点空间的
一个有限生成集合。清除同态分母只改变非零整数倍，不改变 $\mathbb Q$-张量。
对各块取并即可。对数同构继承自 R596。$\square$

这一步没有使用 $p$ 进高度矩阵可逆性。

活跃块也能用有限代数判据识别，而不以有限精度的零对数当成挠点。
在两个不同的好约化素数 $\ell_1,\ell_2$ 计算
$N_i=\#B(\mathbb F_{\ell_i})$，置 $T=\operatorname{lcm}(N_1,N_2)$。
任何有理挠点的每个素数幂部分都在至少一个剩余特征不同的约化处注入，
故其阶整除 $T$。于是对已清分母的实际点 $R$，

$$
R\text{ 为挠点}\quad\Longleftrightarrow\quad[T]R=0.
\tag{724.10}
$$

右侧是代数群上的准确等式判定。可把这个判据应用于每个清分母后的
$e_\alpha\eta_{h_i}$。

确定 $b$ 后，对上述有限 Hecke 轨道计算群对数，增加精度直至找到一个
非零的 $b\times b$ 子式。这一步必停止，因为 (724.9) 已给实际满秩。
选出的点就是所需基；不要求它们是整 Mordell–Weil 群的饱和基。

## 4. 真正的 $\ell_h$ 是一个不反演高度矩阵的公式

以下用第 2 节选定的块相容参考 splitting，省略上标 $0$。
取 $\operatorname{Lie}(B_\eta)$ 的代数基。令

$$
L=\bigl(\log P_1\ \cdots\ \log P_b\bigr),\qquad
H_{\mu\nu}=h_Y(P_\mu,P_\nu),\qquad
y_h=\log\eta_h .
\tag{724.11}
$$

$L$ 是可逆的。对任意 $v\in\operatorname{Lie}(B)$，有

$$
\boxed{\quad
\ell_h(v)=y_h^{\,t}L^{-t}HL^{-1}e_\eta v .
\quad}
\tag{724.12}
$$

证明。对数同构把 $L^{-1}e_\eta v$ 识别为相应有理点张量的基坐标；
$\eta_h$ 的基坐标为 $L^{-1}y_h$。按 $H$ 的双线性定义得到公式。
非活跃块在 $\eta_h$ 上为零，且参考高度按块正交，因此没有漏掉这些块的
全局配对。原 splitting 的函数再由 (724.7) 精确恢复。$\square$

$H$ 可以退化；公式从不反演 $H$，所以不需要任何未证明的高度非退化猜想。
若没有活跃块，则 (724.12) 为零；实际 Picard 线丛及其截面仍在下面的局部
求值中保留，不能仅凭这个零就改写原线丛。

## 5. 规范 Poincaré 对数的具体群公式

本节给计算 (724.11) 及原 $\lambda_p$ 的局部方法。所用双扩张可以全部取在
$J_X$ 和 $J_Y$ 及其对偶上，不需要援引任意 abelian variety 上尚未给出比较的
高度定义。

令 $C/K$ 为本题的 $X$ 或 $Y$，$J_C$ 为其 Jacobian，$K$ 是有限 $p$ 进域。
令

$$
0\longrightarrow V\longrightarrow I
 \xrightarrow{\pi}J_C^\vee\longrightarrow0,\qquad
\operatorname{Lie}I\simeq H^1_{\rm dR}(J_C)
\tag{724.13}
$$

为对偶的 universal vectorial extension。
$V=\Omega^1(J_C)$ 视为加法向量群。所选 Hodge 补空间给右逆

$$
r:\operatorname{Lie}(J_C^\vee)\longrightarrow\operatorname{Lie}I.
\tag{724.14}
$$

$I$ 的点也表示 $J_C$ 的 $\mathbb G_m$ 扩张及其一阶刚性化。

对 $Q\in J_C^\vee(K)$，取任意代数提升 $Z\in I(K)$。
群对数给

$$
\Delta_Q=\log_I Z-r(\log_{J_C^\vee}Q)\in V(K),\qquad
\widetilde Q=Z-\Delta_Q\in I(K).
\tag{724.15}
$$

这里减法用的是已给定的向量子群嵌入 $V\hookrightarrow I$。
$\widetilde Q$ 所带的一阶刚性化给一个确切的线性投影

$$
t_{\widetilde Q}:\operatorname{Lie}E_Q\longrightarrow K,\qquad
E_Q=\mathcal P_{J_C\times\{Q\}},
\tag{724.16}
$$

其在 $\operatorname{Lie}\mathbb G_m=K$ 上为恒等。实施时按 universal extension
中这项代数刚性化取投影，不能任意给 $\Delta_Q$ 的符号改名。

**引理 724.3。** (724.15) 与提升 $Z$ 无关，且
$Q\mapsto\widetilde Q$ 是 Hodge splitting (724.14) 所给的实际解析群截面。

证明。更换提升为 $Z+v$，$v\in V(K)$，其对数同时增加 $v$，
所以 $\Delta_Q$ 同时增加 $v$，差不变。它投影到 $Q$，且对数为
$r(\log Q)$。加法也保持此条件；两个满足条件的提升之差是 $V$ 中对数为零的
点，故是零。其微分为 $r$。$\square$

取 $z\in\mathcal P(P,Q)(K)$。在 $(0,Q)$ 附近选一个代数截面
$e(U,Q)$，沿 $U=0$ 等于双扩张的单位。取正整数 $n$，使
$nP$ 及 $e(nP,Q)$ 进入已选的收敛形式邻域。在同一纤维中定义准确标量

$$
[n]_1 z=c_n\,e(nP,Q),\qquad c_n\in K^\times .
\tag{724.17}
$$

$[n]_1$ 是 Poincaré 双扩张在第一变量中的原代数乘法。
设 $\operatorname{Log}_{E_Q}$ 为该小形式群上的对数，固定原来的
$\log_K$ 分支。则

$$
\boxed{\quad
\gamma_r(z)
=\frac1n\left(
   \log_K(c_n)+
   t_{\widetilde Q}\bigl(\operatorname{Log}_{E_Q}(e(nP,Q))\bigr)
 \right).
\quad}
\tag{724.18}
$$

若 $\chi_p=t_p\circ\log_K$，实际 $\chi_p$-splitting 是
$\tau_p=t_p\circ\gamma_r$。

证明。Hodge splitting 给 $E_Q(K)$ 上唯一的解析群同态，其在
$K^\times$ 上为 $\log_K$，微分为 $t_{\widetilde Q}$。
在小形式群中它正是 $t_{\widetilde Q}\operatorname{Log}_{E_Q}$。
对 (724.17) 使用群同态，再除以 $n$，得到公式。反过来，公式的值与 $n$、
代数截面和提升无关，因为它是同一个群同态的值。$\square$

所有扩张、提升和投影都可保留为 Jacobian 的代数线丛加连接数据。
尤其 $Z$ 只是一个代数提升；它通常不是规范提升。必须实行 (724.15) 的
完整向量修正后才得到 $t_{\widetilde Q}$，不能以任意第三类微分直接替代。

这里采用的是 Iovita–Werner §1 的一般 Hodge-splitting 构造；
该文 §2 才加入 ordinary semistable 假设。本文不使用其 unit-root 结论。

为核对这确是原 BMS 度量，在 Jacobian 上使用 BMS Proposition 6.14：
规范 Picard 零次线丛的 $d\log$ 对应同一补空间的第三类微分。
该文 (46)–(47) 的 $\Psi$ 来自 universal vectorial extension 的对数。
因此原 BMS 双扩张 splitting 的一阶刚性化在 (724.13) 的 Lie 代数中
正是 (724.14)。上述唯一性遂识别其与 (724.18)。
所有比较都是在同一 Poincaré 纤维上比较刚性化和微分，再由解析群同态
唯一性识别，而非只比较两个全局配对的数值。尤其不能仅援引 BMS
Theorem 6.10：其 Remark 6.17 明确提醒，全局相等本身并不识别逐个局部项。
若以曲线 Coleman–Gross 配对实现，须保持 BMS 的 autoduality 符号；
下面直接用 Poincaré 纤维，避免把其负号另换一次。

### 5.1 群对数不要求一个未知的全局积分路径

对 $J_C$ 或 $I$ 上的代数点 $Z_0$，可取正整数 $m$ 使
$[m]Z_0$ 落入小形式群，并置

$$
\log Z_0=m^{-1}\operatorname{Log}_{\rm formal}([m]Z_0).
\tag{724.19}
$$

对 proper 的 $J_C(K)$，任一开形式子群指数有限。
对 $I(K)$，先将投影乘入 $J_C^\vee$ 的形式邻域；局部 lift 与原点的差在
向量群中，再乘一个充分大的 $p$ 次幂便同时进入形式邻域。
故 (724.19) 必可实施。不同 $m$ 用公共倍数比较即得同一个对数。

对于实际 $x=c_1+s$，可以在 $c_1$ 的一个足够小邻域内固定所有代数坐标图、
提升和整数 $m,n$，因此 (724.15)–(724.19) 是计算整个 Taylor jet 的公式。
它们把 $c_1$ 处的第二类周期保留为代数群点的形式对数值，而没有将这些周期置零。

## 6. 从原线丛和原截面得到 $\lambda_{p,h}$

实际 $\mathscr N_h$ 是 R593 的完整 $\mu_3$ 范数及 tensor 幂。
保留其真实 tensor 表示，把其中每个对称因子和 Picard 零次因子逐一计算。
为避免隐去范数代表中的挠差，下面不以“Picard 有理类相同”替换真实 tensor 同构。

在 $c_1$ 附近，写真实代数表示

$$
\mathscr N_h\simeq
 \bigotimes_\nu f_\nu^*L_\nu^{\otimes a_\nu}
 \otimes
 \bigotimes_\mu g_\mu^*(\mathcal P_{B_\mu\times\{Q_\mu\}})^{\otimes b_\mu},
\tag{724.20}
$$

其中 $L_\nu$ 是沿原点刚性化的对称线丛；此表示包括范数的全部三个因子、
$c_{\rm triv}$ 和必要的整数 tensor 指数。实施时把每个对称因子先视为 $J_X$ 上的真实拉回线丛；
其 Poincaré 点用 $(P_X,\lambda_{f_\nu^*L_\nu}P_X)$ 表示。
每个 Picard 因子则用原对偶拉回同态给出的 $J_X^\vee$ 点。
所以本节的所有局部调用都可以只用 $J_X$ 的 (724.18)，
不要求给一般 $A$ 的 Zarhin 高度作额外比较。

选代数局部帧 $u_\nu,v_\mu$，以原实际截面定义代数非零函数 $R_h$：

$$
s_h=R_h\prod_\nu u_\nu^{a_\nu}\prod_\mu v_\mu^{b_\mu}.
\tag{724.21}
$$

对称线丛的刚性化同构
$L_\nu^{\otimes2}\simeq(1,\lambda_{L_\nu})^*\mathcal P$
把 $u_\nu^{\otimes2}$ 送到准确纤维点 $z_\nu$。因此

$$
\boxed{\quad
\lambda_{p,h}(x)=\frac1{C_h}\left(
 \chi_p(R_h(x))
 +\frac12\sum_\nu a_\nu\,\tau_{p,\nu}(z_\nu(x))
 +\sum_\mu b_\mu\,\tau_{p,\mu}(v_\mu(x))
 \right).
\quad}
\tag{724.22}
$$

证明。刚性化后的 theorem of the square 是规范 log functions 的等距同构。
Tensor、拉回和标量变化分别给求和、复合及 $\chi_p(R_h)$。
最后除以原 $C_h$。原 $s_h(c_0)=1$ 和每个零截面的刚性化固定常数，
所以这里算出的 $d_i=\Lambda_i(c_1)$ 就是原来的 $d_i$。$\square$

在 $J_X$ 上，可取与原 $q$ 部分、$\phi^*J_Y$ 部分及其正交补相容的代数
Hodge splitting，并保持 R699 的 $\mu_3$ 相容性；R593 的 $q\phi^*=0$
保证这两部分正交。
对称因子的曲率与拉回曲率相同，BMS Theorem 4.14 的唯一性识别两个度量；
Picard 因子由同一 Poincaré 曲率及两个零截面的规范识别。
这解释了为何使用 Jacobian 的 (724.18) 没有改变原因子度量。
实际加权迹和 $\kappa$ 仍在原 $\lambda_{L_\nu}$ 与对应 $f_\nu$ 中。

## 7. 高度矩阵的全局求值及有限支撑

为计算 $H_{\mu\nu}$，在同一全局 Poincaré 纤维
$\mathcal P_Y(P_\mu,\lambda_YP_\nu)$ 选一个有理非零向量 $z_{\mu\nu}$。
则按 (724.2)，

$$
\boxed{\quad
H_{\mu\nu}=\frac12\sum_v\tau_{Y,v}(z_{\mu\nu}).
\quad}
\tag{724.23}
$$

不同有理向量只相差 $\mathbb Q^\times$；同一个全局 $\chi$ 的乘积公式保证
此和不变。$p$ 处使用 (724.18)。

对 $\ell\ne p$，也可直接从原代数双扩张求值。选一个足够小的 $\ell$ 进形式
邻域以及沿两个轴归一的代数帧 $e_\ell$，使部分加法的全部结构函数为单位。
取整数 $n$ 将两个基底点同时乘入这个邻域，写

$$
[n,n]z_{\mu\nu}
   =c_{\ell,n}\,e_\ell(nP_\mu,n\lambda_YP_\nu).
\tag{724.24}
$$

则

$$
\tau_{Y,\ell}(z_{\mu\nu})
     =n^{-2}\chi_\ell(c_{\ell,n}).
\tag{724.25}
$$

证明。在该形式邻域，单位标量的 $\chi_\ell$ 为零；
因此帧上的局部值在两个 pro-$\ell$ 群变量中分别连续可加。
固定一变量，把另一变量乘以 $\ell^k$ 后趋于零。
由于 $|\ell|_p=1$，连续性迫该值为零。对 (724.24) 使用双加性即得结论。
部分加法结构函数为单位的邻域可由代数图的清分母及缩小坐标直接给出，
所以没有一个待猜的局部高度常数。$\square$

这个方法不要求在原坏处先假设好约化。在给定的有限代数模型、点和非零纤维
向量上清除分母，并排除模型的坏素数，便得到一个有限集合 $S$；
在其外所有数据延拓为光滑群/双扩张上的整点和整单位纤维，规范未分歧值为零。
因此 (724.23) 只含一个可给出的有限和。需要的整数分解及有限群运算虽然可能
昂贵，仍是明确的有限代数计算，而不是未指定的高度 oracle。

## 8. 形式求值的完整误差界

下面说明为何上述公式确实可以输出任意给定精度的有限 jet。

这种整数形式图可从实际光滑代数群的单位元构造：选 étale 参数，
将隐函数方程的一次 Jacobian 化为单位矩阵，再充分缩放参数，使全部
有限定义方程、群运算分母及其非线性项整。形式隐函数定理随后给全部
Taylor 系数的整性。该证书来自代数图，不是只检查有限个已算系数。

设在一组已清分母的整数形式坐标 $T=(T_1,\ldots,T_d)$ 下，一个交换形式群的
不变微分矩阵为 $\omega=A(T)\,dT$，$A(T)$ 的系数整，且 $A(0)=I$。
其形式对数通过沿射线积分得到

$$
\operatorname{Log}_j(T)
 =\int_0^1\sum_i A_{ji}(tT)T_i\,dt.
\tag{724.26}
$$

交换群的不变微分闭合；因此该积分的微分确是 $\omega$，
初值为零，并且它是形式群对数。对总次数 $n\ge1$，

$$
v_p([T^{\mathbf a}]\operatorname{Log}_j)
       \ge-v_p(n),\qquad |\mathbf a|=n.
\tag{724.27}
$$

若坐标需要进一步缩放或改变不变微分基，将相应已知有限赋值损失加到右侧。

设一个已认证的局部参数 $u=s/p^b$ 使输入坐标满足
$v_G(T_i(u))\ge\rho>0$，其中 $v_G$ 为 Tate 系数的最小赋值。
删去总次数 $n\ge N$ 的全部形式项所产生的完整误差满足

$$
v_G(\text{误差})\ge
\mathfrak T_\rho(N):=
 \inf_{n\ge N}\{\rho n-\lfloor\log_p n\rfloor\}
 \longrightarrow+\infty.
\tag{724.28}
$$

这个下界可由有限次检查准确给出：在每个
$[p^k,p^{k+1})$ 上右式随 $n$ 增加，故只需检查 $N$ 和其后的跳点 $p^k$；
一旦 $\rho(p-1)p^k>1$，后续跳点的值严格递增。

对 $0\le j\le D$ 的原 $s$-Taylor 系数，误差再损失至多 $bD$。
式 (724.18)–(724.19) 中除以 $m,n$ 的损失、代数线性矩阵和 $C_h$ 的损失
全部显式加入。$\log(R_h/R_h(c_1))$ 的普通对数级数有同样的
“线性减 $\log$”尾界。

这里特别允许 $T_i(0)\ne0$：高总次数项仍可能贡献低阶 $s$-系数，
所以不能只按目标 jet 次数截断。真正截断由 (724.28) 的 Gauss 范数给出，
它同时控制这些低阶贡献。

实际算法先把有限个代数群点乘到足够小的形式邻域，再缩小 $s$ 的辅助计算盘；
所有群运算的分母在中心非零，因此可用代数不等式验证这一步。
这个辅助盘只用于算 Taylor 系数，不缩小 R703/R716 已覆盖的原候选盘。
在求 $L^{-1}$ 时持续增加精度，直至其实际非零行列式被认证，再按该逆矩阵
的实际赋值预算运算。无需假定任何对数、KS 比较常数或高度为单位。

由此，(724.12)、(724.22)、(724.23) 给任意指定 $D,N$ 的原
$\ell_h$、$\lambda_{p,h}$、$d_i$ 和 $\Lambda_i$ 前 $D$ 阶系数模 $p^N$。
输出应包括实际代数图、所有清分母/乘法整数、所用精度、尾界与矩阵条目；
本条没有把这些尚未生成的具体数字伪作已生成。

## 9. 接上原外积以及真正的有限排根证书

由同一个 $J_X$ 群对数计算

$$
L_i=(q^*\omega_i)(\log[c_1-c_0]),\qquad
t_i=1+\frac{I_i}{L_i}.
\tag{724.29}
$$

R616 保证这些实际分母非零，因而其倒数可用增加精度来认证。
所有 $q^*\omega_i$ 的 Taylor 系数是代数的，故共同 Abel 阶 $m$
可由代数 jet 找到；R705 给了停止的有限上界。
不需要把模 $p$ 的零系数认作特征零的零。

用求得的原高度系数形成

$$
E_{ij}=(d_it_i^2-\Lambda_i)(t_j^2-t_g^2)
       -(d_jt_j^2-\Lambda_j)(t_i^2-t_g^2).
\tag{724.30}
$$

这是原 R634 函数。仍只有已经证明的精确整除
$s^{m+1}\mid E_{ij}$，不能自动改成 $s^{2m}$。

在实际闭盘 $s=p^4u$ 上令 $\nu=m+1$，并选若干原外积分量：

$$
F_\alpha(u)=u^{-\nu}E_\alpha(p^4u)\in K\langle u\rangle .
\tag{724.31}
$$

R703 或 R716 的有限 jet 矩阵给出完整相对尾界。
因每个所选 $E_\alpha$ 非恒零，增加第 8 节的计算精度必能在其有限
决定行集上认证一个非零系数，并确定有限前缀的最小赋值。
因此这些相对尾界变成实际的绝对误差界。该过程没有推断所有较低阶
未辨明系数精确为零。

取有限多项式 $\widehat F_\alpha\in K[u]$，并给出已证明的完整误差

$$
v_G(F_\alpha-\widehat F_\alpha)\ge\epsilon_\alpha.
\tag{724.32}
$$

**定理 724.4（有限 Bézout 排根证书）。**
若找到有限多项式 $A_\alpha\in K[u]$ 和 $c\in K^\times$，使

$$
v_G\!\left(\sum_\alpha A_\alpha\widehat F_\alpha-c\right)>v_p(c),
\qquad
v_G(A_\alpha)+\epsilon_\alpha>v_p(c)\quad\text{对每个非零 }A_\alpha,
\tag{724.33}
$$

则同一个原候选闭盘 $v_p(a-1)\ge4$ 没有非中心的共同高度零，
从而该盘内所有原候选均为中心 $c_1$。

证明。由 (724.32)–(724.33)，

$$
\sum_\alpha A_\alpha F_\alpha=c(1+R(u)),\qquad v_G(R)>0.
\tag{724.34}
$$

右侧在任一完备扩域的闭单位盘上都是单位，故 $F_\alpha$ 没有共同零。
对于 $u\ne0$，共同原外积零等价于共同 $F_\alpha$ 零；
所有原候选满足原外积方程，故得到结论。$\square$

这是真正的有限精度充分证书；不要求某一个分量的首项先验为单位。
可用有限多项式扩展 Euclidean 算法求 $A_\alpha$，
但最终必须验证 (724.33) 对完整尾成立。

若 $F_\alpha$ 在闭盘上没有任何共同零（包括中心），则上述证书搜索必可成功：
一元 Tate Weierstrass 分解把每个非零 $F_\alpha$ 写成多项式乘单位；
无共同零意味着这些多项式互素，于是先有 Tate 代数中的 Bézout 等式。
将其中系数函数近似为多项式，再提高 (724.32) 的精度，便得到 (724.33)。
这是关于该充分条件的完备搜索，不是证明实际函数已经满足该条件。

若所有 $E_\alpha$ 在中心还有更高的共同精确零，(724.31) 仍保留中心零，
则本证书不一定适用；不能凭有限精度给它们再除一个未经证明的 $u$。
同样，可能存在仅在扩域中的非中心高度零。
本文没有以这些情况中的任何一种宣布实际 $\mathbb Q_p$ 候选已被排除。

## 10. 完成的输入与尚待执行的任务

新增的实际内容是：

1. $Y$ 的 splitting 改变在原 $\Lambda$ 中精确抵消，包括原因子二、
   Picard 修正和截面常数。
2. 原 $\eta_h$ 的有限 Hecke 轨道已经足以构造其所需的有理点基；
   不另寻找 Mordell–Weil 生成元，不假设高度矩阵可逆。
3. 同一 Poincaré 规范给出 (724.15)、(724.18)、(724.22)、(724.23)：
   第二类周期、$d_i$ 和全局线性高度项都由代数群运算及具有全尾界的形式对数
   求值，不是独立的未知“规范常数”输入。
4. 原 R703/R716 矩阵与这些真实前缀相接，产生可以接受或拒绝的 (724.33)
   有限排根证书；只给一个零数上界不算通过。

一般 $p$ 的实际曲线/对应/线丛模型、上述有限矩阵及 (724.33) 的具体条目
仍待生成。即使对一个 $p$ 得到证书，也不因此获得全部 $p$ 的绝对 Serre
一致性。原主目标仍开放。

## 来源与比较范围

- A. Iovita and A. Werner, *p-adic height pairings on abelian varieties with
  semistable ordinary reduction*, J. reine angew. Math. 564 (2003), 181–203;
  作者稿 arXiv:math/0209362，§1，特别 printed pp.6–7 的 Hodge splitting、
  universal vectorial extension、rigidification 与 $\gamma_d$ 构造；
  Proposition 3.2 给解析双扩张 splitting 的反向识别。
  <https://arxiv.org/pdf/math/0209362>。
  本文只使用该文在 ordinary 假设之前的这部分一般构造。
- A. Besser, J. S. Müller, P. Srinivasan, *p-adic adelic metrics and Quadratic
  Chabauty I*, arXiv:2112.03873v4 (2026)，Theorem 4.14、Proposition 4.30、
  §§6.1–6.2、Propositions 6.13–6.14、Corollary 6.15。
  <https://arxiv.org/html/2112.03873v4>。
  这里使用 Jacobian 上的已证比较；不把该文提到的任意 abelian variety
  与 Zarhin 高度的未来比较当成现成定理。
- 本仓库 [R593](R593-actual-quotient-height-and-uniform-bad-place-support.md)、
  [R596](R596-fixed-Chow-Heegner-class-log-factorization.md)、
  [R616](R616-original-CM-point-difference-and-explicit-height-basis.md)、
  [R634](R634-CM-calibration-eliminates-actual-height-matrix.md)、
  [R699](R699-actual-height-finite-jets-and-complete-exterior-tail.md)、
  [R703](R703-algebraic-jet-extractors-and-height-free-relative-tails.md)、
  [R705](R705-actual-higher-Abel-blocks-and-uniform-order-bound.md)、
  [R716](R716-curvature-only-jet-extraction-without-gamma.md)、
  [R719](R719-p137147-original-primitive-visible-enumeration-certificate.md)。
