# 原 Y 的有限 RR 矩阵：免预先 HNF 的入口与真实来源叶子

日期：2026-11-16。状态：**本文为原已成来源上的纸面构造与执行契约；没有执行新矩阵、理想、下降或 period 计算。**

本文接 [原 Y 的 RR 连接与 Hecke 行](2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md)（下称 YP；正式稿 SHA256 `bdbb6cc590a455a9fba75c378658be69fb19dc1d318c0ec2342edde09e1d06b8`）。保持该文的原 $Y/\mathbf Q$、$P_0,P_1$、$t=a^3$、$\mathscr L_j=\mathcal O(-Z_j)$、原帧及 Hecke 来源。本篇只落实其中 $a_j$、$\alpha_0$ 所需的有限线性输入；不重新证明 UE 相消，不把尚未展开的理想 DAG 当作已成多项式格。

新增的三个缩小是：完整**生成矩阵**已足以给一个显式有限 RR 核，不先要求两张图各自的完整 HNF 基；原 $\mathbf Q$ 下降只先求三个原 V1 共轭；所需函数微分只用已成 R813 的 $g,h$ 和链式法则，不等待一般 $\Gamma$、$M_g$ 或一个新的 canonical-module 计算。

## 1. 原正规环已经完成，不再重新正规化平面方程

使用 [R805](../results/R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)、[R806 实际结果](../results/R806-certified-original-primitive-multiplication.md) 的同一两图，记

$$
z=\sigma/\tau,\qquad v=1/z,\qquad w=w_0/\tau,
\qquad w_0=e_2,
$$
$$
R_\tau=\bigoplus_{i=0}^{271}k[z]\beta_i,
\qquad
R_\sigma=\bigoplus_{i=0}^{271}k[v]\gamma_i,
\qquad
\gamma_i=v^{\epsilon_i}\beta_i,
\tag{FM.1}
$$

其中 $\epsilon=(0,1^{144},2^{127})$，$k$ 可先取原 $K$ 或 $L$。这里的两个环是原光滑曲线上的完整正规环。原实际 $W=M_w$ 与 cyclic minor 已证明

$$
k(Y)=k(z)[w],\qquad [k(Y):k(z)]=272.
\tag{FM.2}
$$

原正规整基仍是 (FM.1)。辅助环 $k[z,w]$ 的 conductor、正规化或平面奇点不作为本消费者新的必需输入；它不替换 $R_\tau$。如将来选择平面呈示实现，仍须用已成的原整基认证其输出，而不能因一个平面方程定义同一函数域就把它视为整个仿射环。

给定一个实际原函数 $f$ 的 normal 向量 $v_f$，其乘法矩阵可以只用相应右端定义：

$$
K_w=(e_0,We_0,\ldots,W^{271}e_0),\qquad
M_f K_w=(v_f,Wv_f,\ldots,W^{271}v_f).
\tag{FM.3}
$$

这是 $k(z)$ 上的准确有限 solve。也可先把 $f$ 转成原 $k(z)[w]$ 表达，再作 $f(W)$。两者的来源、基次序和标量必须相同。没有要求预先形成全部 $272^3$ 乘法表或完整 Krylov 逆；实际执行时保存用到的右端和乘回恒等式。

## 2. 完整生成矩阵的有限运算

在一张图写 $R=\bigoplus k[z]\beta_i$。对非零分式理想 $I=(f_1,\ldots,f_s)_R$，其完整 $k[z]$ 生成矩阵为

$$
G_I=[M_{f_1}\ \cdots\ M_{f_s}].
\tag{FM.4}
$$

“完整”是等于所指定分式理想；仅有一个非零 $272$ 阶子式不够。原 [R849](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md) 的 sum/product/power/conjugation 节点按原数学理想恒等式展开，给这种完整生成列表。$L/K$ 的 Norm 仍是全部七个原 Galois 共轭的乘积，保留原相位与所有标量。

求逆理想也可作有限余模问题，不必先 HNF。选一个已认证 $f_0\ne0$，则

$$
I^{-1}=f_0^{-1}N,\qquad
N=\{u\in R:(f_i/f_0)u\in R\text{ 对所有 }i\}.
\tag{FM.5}
$$

把每个 $M_{f_i/f_0}$ 清分母为 $Q_i/q_i$，其中 $Q_i$ 是多项式矩阵、$0\ne q_i\in k[z]$。取共同倍数 $q$，则

$$
qk[z]^{272}\subset N\subset k[z]^{272},
\qquad
N/qk[z]^{272}=
\ker\left(u\longmapsto(Q_i u\bmod q_i)_i\right).
\tag{FM.6}
$$

右边是有限 $k$ 线性图；其全部核向量的多项式提升，加上 $q e_i$，给 $N$ 的完整生成列。证明只需把任意 $u$ 除以 $q$，并注意余类条件完全决定其是否在 $N$。不能只取部分模核方向，也不能把一个辅助素数上的核直接提升为特征零核。

和由拼接生成列给出，积由全部原生成元的积给出；在这些原 Dedekind 环中

$$
I\cap J=(I^{-1}+J^{-1})^{-1},\qquad
(I:J)=IJ^{-1}.
\tag{FM.7}
$$

因此 GP 的原五分式理想、点理想的幂以及下述微分系数理想，都有明确有限生成程序。它可能昂贵；这里没有给尚未测得的次数、秩或运行成本。各步的清分母函数仍是数据，不允许删成未知非零标量。

## 3. 不求 HNF 的完整 RR 核

设 $\mathscr M$ 是原曲线上的可逆分式理想层，已给两图的完整生成矩阵 $G_\tau,G_\sigma$，各自的列为 (FM.1) 中的函数坐标。取非零多项式 $d_\tau(z),d_\sigma(v)$，使

$$
P_\tau=d_\tau G_\tau\in\operatorname{Mat}_{272\times s_\tau}(k[z]),
\qquad
P_\sigma=d_\sigma G_\sigma\in\operatorname{Mat}_{272\times s_\sigma}(k[v]).
\tag{FM.8}
$$

令

$$
n=\deg d_\tau,\quad h=\operatorname{ord}_{v=0}d_\sigma,\quad
q(v)=v^n d_\tau(1/v),
\quad b_i=n+h-\epsilon_i.
\tag{FM.9}
$$

$q(0)\ne0$。定义有限多项式向量空间

$$
\mathcal P=\bigoplus_{i=0}^{271}k[z]_{\le b_i},
\tag{FM.10}
$$

其中负次数界对应零空间。对 $p\in\mathcal P$ 置

$$
F_\sigma(p)(v)
=d_\sigma(v)\operatorname{diag}(v^{n-\epsilon_i})p(1/v).
\tag{FM.11}
$$

(FM.9) 保证每个分量都是多项式，包括 $d_\sigma$ 在 $0$ 的实际零阶；不靠形式上的负幂删除。

**有限 RR 命题。** 有准确同构

$$
H^0(Y_k,\mathscr M)
\simeq
\left\{p\in\mathcal P:
p\in\operatorname{im}P_\tau,\quad
F_\sigma(p)\in q\operatorname{im}P_\sigma
\right\},
\qquad
p\longmapsto\sum_i\frac{p_i(z)}{d_\tau(z)}\beta_i.
\tag{FM.12}
$$

证明。对全局截面 $a$，因为 $a\in\operatorname{im}G_\tau$，其坐标为 $p/d_\tau$，$p\in k[z]^{272}$。在另一图的坐标是

$$
\operatorname{diag}(v^{-\epsilon_i})
\frac{p(1/v)}{d_\tau(1/v)}.
$$

乘 $d_\sigma$ 后在 $v=0$ 正则；逐坐标计算最低指数给
$\deg p_i\le n+h-\epsilon_i$，故 $p\in\mathcal P$。同一过渡式乘 $q$ 后正是 (FM.11)，所以另一图的完整 membership 等价于 (FM.12) 第二条件。反过来，两条件使同一函数分别属于两图原分式理想，故粘成全局截面。这里既没有只检查一个纤维，也没有漏掉 $q$ 的非零有限零点。$\square$

下面把两个 membership 写成真正有限矩阵。选各 $P_c$ 的一个实际非零 $272$ 阶子矩阵 $B_c$，记 $\Delta_c=\det B_c$。由 adjugate 恒等式，

$$
\Delta_\tau k[z]^{272}\subset\operatorname{im}P_\tau,
\qquad
q\Delta_\sigma k[v]^{272}\subset q\operatorname{im}P_\sigma.
\tag{FM.13}
$$

因此在有限代数

$$
A_\tau=k[z]/(\Delta_\tau),\qquad
A_\sigma=k[v]/(q\Delta_\sigma)
\tag{FM.14}
$$

中，计算全部生成列的子空间

$$
V_\tau=\operatorname{im}(\overline P_\tau:A_\tau^{s_\tau}\to A_\tau^{272}),
\quad
V_\sigma=\operatorname{im}(\overline{qP_\sigma}:A_\sigma^{s_\sigma}\to A_\sigma^{272}).
\tag{FM.15}
$$

多项式矩阵的每一列要连同该有限代数中所有基底倍数取像，而非只取常数倍。取准确商投影 $\pi_\tau,\pi_\sigma$ 后，所求矩阵是

$$
\boxed{\quad
\mathcal P\longrightarrow
(A_\tau^{272}/V_\tau)\oplus(A_\sigma^{272}/V_\sigma),
\quad p\longmapsto
(\pi_\tau\bar p,\pi_\sigma\overline{F_\sigma(p)}).
\quad}
\tag{FM.16}
$$

其核等于 (FM.12)，因为 (FM.13) 使有限余类 membership 等价于原完整多项式 membership。$\Delta$ 是单位时相应商为零。本证明不要求任何闭点分解、squarefree 性、HNF 基或对转移矩阵求逆。

用于 YP 的 $\mathscr M=\mathscr L_j(254P_0)$ 时，核维数是128；这是 RR 定理给出的输出维数，不是说 (FM.16) 只有128列。若为原挠差先取 $\mathscr L_j^N$，仍取同一254，维数仍128。

## 4. 原 $P_0$ 与截面除子的有限代数

点理想使用原 [R837](../results/R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md) 的 $P_0$ 评价，不重新反射或重算原 Fourier 值。在 $P_0$ 所在的一张图，完整评价核为

$$
I_{P_0}=\ker(R\longrightarrow k(P_0)).
\tag{FM.17}
$$

它可由该图的基底值和基变量值生成；若该点不在某图，该图的点理想就是整个环。先按原值实际判断所用 $\tau$ 或 $\sigma$ 非零，不猜某一图必覆盖该点。所需 degree2 normal 基底值按原 R805/R775 recipe 由 R837 的完整 V1/V2 值取得，保存原共同框架和比值尺度。

选出 YP 的实际 $a$ 后，令 $\mathscr M=\mathscr L_j(254P_0)$，

$$
T=\operatorname{div}(a)-Z_j+254P_0,
\qquad
I_T=(a)\mathscr M^{-1}.
\tag{FM.18}
$$

这里 $(a)=aR=\mathcal O(-\operatorname{div}a)$；(FM.18) 是正乘 $a$，避免混淆函数乘法与 Cartier 除子符号。$T$ 有效、度254、避 $P_0,P_1$，均由128维 RR 空间及原两点的非零评价证书给出。

后继 $A_T=R/I_T$、$I_T/I_T^2$、$\Omega/I_T\Omega$ 都用完整理想生成矩阵与有限余模表示。它们可以非约化，也可以有不可分解的闭点；本构造没有给每个闭点选择根。

## 5. canonical module 直接复用 R813/R814/R820

原 [R813](../results/R813-certified-original-Wronskian-normal-vectors.md) 已准确完成

$$
g=\delta z,\qquad h=\delta w,\qquad
\delta=\tau^{-1}D_0,\qquad D_0=q_Y\partial_{q_Y}/82.
\tag{FM.19}
$$

准确 S3 坐标必须按原 numerator / column denominator，再乘原 target scale $6724/1$ 一次；不增插 $82$、$82^2$ 或 content。原 [R814](../results/R814-original-cusp-zero-ideal-and-exact-multiplicity-peeling.md) 给
$\operatorname{div}\delta=\mathcal C_{\rm cusp}-H_\tau$，其中20个 cusp 均为单零。令

$$
\nu=dz/g,
$$

则 [R820](../results/R820-certified-original-cusp-finite-algebra-and-ideals.md) 已成的两图完整 cusp 理想给

$$
\Omega(R_\tau)=\mathcal C_\tau\nu,
\qquad
\Omega(R_\sigma)=v^{-1}\mathcal C_\sigma\nu.
\tag{FM.20}
$$

因此对 $D=T+254P_0$，$\Omega(D)$ 的两图系数模块就是

$$
\mathcal C_\tau I_{D,\tau}^{-1},
\qquad
v^{-1}\mathcal C_\sigma I_{D,\sigma}^{-1}.
\tag{FM.21}
$$

将它们放入 (FM.8)–(FM.16)，得到完整634维空间，而其508维 principal-parts 图和秩507按 YP 的原有限 conormal/CRT 目标构造。$H^0(Y,\Omega)$ 是该准确主部图的127维核，可以复用给 Abel log，不另解一个无关 differential basis 问题。

对于主部目标所需的 $df$，有更小的实际输入。任何以原 $z,w$ 表示的有限函数表达 $E$ 都满足

$$
\boxed{\quad\delta E=g\,\partial_zE+h\,\partial_wE,
\qquad dE=(\delta E)\nu.\quad}
\tag{FM.22}
$$

此处偏导只作用于该表达，系数域导数为零。因为已知 $\delta$ 是原几何导子且在两个域生成元上的值正是 (FM.19)，链式法则自动与原函数域关系相容。它不是从任意两向量猜一个导子。加、乘、除和准确 unit-solve 节点都可逐项微分；例如 $K(z)c=v(z)$ 给

$$
Kc'=v'-K'c.
\tag{FM.23}
$$

同一 $K$ 只增加实际右端，不形成完整逆。由此可构造 $d\log a$、$df\bmod I\Omega$、P0 jets 以及 YP 的 $\alpha_0$ 主部图，无需等待 $\Gamma$ 或 $M_g$ 的巨大 CRT，也不必先展开 $\det(TI-W)$。在 $g=0$ 的 cusp 上必须用 (FM.20) 的 regular-module fibre；不得把 $dz/g$ 当数值 $0/0$。

## 6. 真正的 $\mathbf Q$ 下降只先需要三个 V1 右端

原 [R802](../results/R802-original-semilinear-parity-and-degree-seven-relations.md) 的算术作用是

$$
[v_q^n]\varepsilon(c_YF)=(-1)^n c_0([v_q^n]\varepsilon(F)),
\qquad c_0(s)=-s,\quad c_0(\xi)=\xi.
\tag{FM.24}
$$

这里 $v_q$ 是原 Fourier 参数，不能与图变量 $v=1/z$ 混同。尤其 $c_Y$ 不是对 normal 系数单独共轭。

对原 $\tau=e_0$、$\sigma=e_1+e_{73}$、$w_0=e_2$，只求三个原 V1 截面的共轭坐标

$$
c_Y\tau,\qquad c_Y\sigma,\qquad c_Yw_0.
\tag{FM.25}
$$

原 $V_1$ 维146；十四个完整 $q_Y$ 系数的展开是单射，因为 $20\cdot14>272$。实际 R837 用原 $1,\xi,\ldots,\xi^{39}$ 坐标，矩阵为 $560\times146$，其选行编号正是在这560行中；本次直接复用这份原矩阵及选行，不重做实圆分换基。虽然相应实表示可压成280行，这不是把旧选行直接放进280行矩阵的许可。在原146列中，(FM.24) 给三个准确右端，实际解须在全部560个原坐标中乘回。保留原 $82^2$ 和共同框架；选行证明不等于这三个新解已经算完。

得到三条截面后，

$$
c_Y(z)=\frac{c_Y\sigma}{c_Y\tau},\qquad
c_Y(w)=\frac{c_Yw_0}{c_Y\tau},\qquad c_Y(s)=-s
\tag{FM.26}
$$

即确定整个 $K(Y)=K(z,w)$ 上的真实半线性作用。无需先生成272列 normal involution 矩阵。对 (FM.16) 的有限全局核逐基施此作用，并用原函数等式恢复下降矩阵；其固定空间给原 $\mathbf Q$ 截面。由原线丛/除子 $\mathbf Q$ 下降保证空间稳定，不要求单张 $\tau$ 图稳定。

微分下降也不可只共轭系数。由 (FM.22)，

$$
c_Y(\nu)=\frac{d(c_Yz)}{c_Yg}
=\frac{\delta(c_Yz)}{c_Yg}\,\nu,
\qquad
c_Y(f\nu)=c_Y(f)\frac{\delta(c_Yz)}{c_Yg}\nu.
\tag{FM.27}
$$

这提供同一634维空间及127维 regular 核的准确下降。不能把 R820 辅助 $\mathbf Q$-form 直接当作原扭曲曲线的下降。

## 7. 已完成来源与仍需执行的叶子

下表区别准确系数、准确隐式表达与尚未执行的矩阵。文件引用始终保原 producer/configuration；不把重新包装的 carrier 当作新的数学 producer。

| 输入 | 原已成内容 | 本消费者使用方式 |
|---|---|---|
| R805/R806 | 原整基、$W$ 的34组准确坐标、真实 cyclic minor | (FM.1)–(FM.3) 的原环与按需乘法 |
| R813 | 两条准确 $g,h$ normal 向量及完整820坐标乘回 | (FM.19)、(FM.22)，target scale各6724一次 |
| R820 | 两图272个 sparse `column_terms`、完整20维 cusp 商与单重数 | (FM.20)；不重 cusp 常数项或 Hermite |
| R837 | 原146个 P0 V1 值、418个 V2 值、V1 reflection 真实选行 | 点理想、原帧及三右端下降；不重反射源 |
| R842/R845 | $D$ 的295维单位图表达、真实两锚、八个 $E_y$ 生成元表达 | 仍按准确 unit-solve 表达消费，模数组只作单位见证 |
| R849 | 原函数、五个完整极理想和五个 $\mathscr L_j$ 的523节点 DAG | (FM.4)–(FM.7) 的完整理想源，保所有 principal 常数 |

特别是实际 `R839-original-D-short-kernel-matrix.json.gz` 保存的是 $830\times690$ 的 `matrix_mod_prime` 以及原 source refs；其 kernel stage 的 `exact_unit_solve_expression` 指向原特征零矩阵定义。后继必须沿这些原定义取准确系数，不能把该模矩阵或 `kernel_basis_mod_prime` 改标为特征零输入。相同区别适用于原 T5 quotient 和 T11 两图 source。

所需原 R813 小叶子：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `R813-original-g-h-normal-vector-interface.json.gz` | 8761 | `ef9d09186098bd8cc2144c16bf7797234ac176b7d1faac3fd50b74564c6f32a6` |
| `R813-two-exact-S3-Wronskian-coordinates.json.gz` | 950296 | `29bedd339da16b4fee3dfd412f1d599343a25231fa3b360f5b7b6be4404e9085` |
| `R813-original-S3-coordinate-interface.json.gz` | 50237 | `c853f0e2b2db2ab82f7f50abda80fb801234b4fa408c1e5dea5c71ccfc51a882` |

其原 producer 是 run `43715253991` / source `74f5296a6aa06539580ecbd9591a1284e1984a4e`，完整 manifest SHA `0b54cf2ebb843fb789058d6c40c766428a2d79d1a9b0f705ce4094d4aee1acf8`。

原 R820 两图 index 为：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `R820-chart-tau-cusp-Hermite-index.json.gz` | 17060 | `df8c00e8fb5962a3481d1b07cbefd54e7a5ea51fc54e03e12d39a25354af8365` |
| `R820-chart-sigma-cusp-Hermite-index.json.gz` | 17119 | `48e434d4387b8a4065827191fa97f53eda5cf51295f5fac6d4336d0f40528ebd` |

须按 index 原样取得各自272个 `Hermite_columns_in_original_basis_order` 文件，读取 `column_terms` 的 normal row、变量幂和原分数。原 producer 为 run `43721747750` / source `7890fde180ffabee056de2ce8dd241b189a893a2`；完整 manifest SHA `2877dd3dbe604f07a58c8774897085d1de90a6faa38a6d2ed78a5bb9d7f79a8f`。

现有 R827 retained carrier 已保这些直接消费者输入，原文件名 `R827-retained-producer-inputs.tar.gz`，233593489 bytes，SHA `1e3fc4db60bb41a2daa592245257a1ab2e2522e3dccac4e3aaf5b9041926be44`；原 R827 manifest SHA `2609de217bf1da048f7987ae7de09df38ac24fb63e82d45add1e7c6b9cdbea7e`。实际恢复必须按 carrier 的逐成员清单和原 producer manifest 核定最小闭包；不下载无关 Hermite 工作记录，也不把 R827 的模 $\mathcal C$ reduction 代替原 R820 准确理想。若某个 S3 mapping 文件不在这份最小 carrier 中，则从仍保原 R813 载体的既有来源补取同 SHA；不能因接口名称相同便猜其内容已在本地。

## 8. 最小执行次序与出口

第一项真正小的新消费者是 (FM.25) 的三个 V1 右端：输入仅原146 V1短前缀、R837原 reflection 选行、原 source/frame；输出三坐标、全前缀乘回、(FM.26) 的原有理函数 DAG。它不生成额外 normal 作用表。

其后的必要新叶子依次为：

1. 沿原 R849/R845 **准确表达**得到所需函数乘法和五个 $\mathscr L_j$ 的两图完整生成矩阵；(FM.5)–(FM.7) 每步保完整有限核/像及清分母。
2. 对 $\mathscr L_j(254P_0)$ 构造 (FM.16)，准确核128维，作真实下降，选原 P0/P1 评价均非零的 $a_j$，输出 $c_j,a_j(P_1)$ 和 (FM.18) 的实际有效除子代数。
3. 复用 R813/R820 构造 (FM.21) 的634维 RR 核、508维完整主部目标及秩507证书，求一个 $\alpha_0$；输出 $\alpha_{\rm alg}=\alpha_0-d\log a_j$，保 YP 的 $c_j/a_j(P_1)$ 帧运输。

这些完成后仍需 YP 的原活跃 Hecke 投影、真实 torsion 清除与同一 Hecke 校准行。原 [R724 §3](../results/R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md) 已从 R596 的原 log 同构和真实 $M_m(F)$ Hecke 轨道证明所选 $L$ 可逆；不另用一般 AST 换一组点，也不以新连接的 inactive 部分自动消失。

本篇未计算 $a_j$、$\alpha_0$、原 Hecke 行或指定高度；它给出了缺失矩阵的确切有限输入、可复用的准确叶子以及三个先行的小右端。所有新算术仍只在公开 Actions，原完成阶段不重算。
