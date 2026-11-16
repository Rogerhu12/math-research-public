# 原 P0 的单极生成元、254 次逆理想与128维 RR 的两权证书

日期：2026-11-16。状态：**新的纸面证明和实际消费者契约，尚无本篇的新矩阵秩或核向量数值。** 首个算术出口只求原 P0 的一个271阶单位子式及其准确一维核；成功时给出两图完整的 $I_{P_0}^{-254}$，并将它接到已经完成的五个原分式理想。本文不把这个出口称为五个128维 RR 基已算，也不要求先恢复一般 $M_g$、$\Gamma$ 或完整函数域乘法表。

## 1. 固定原对象和已有真实来源

沿 [YP 原连接稿](../notes/2026-11-16-original-Y-RR-connections-and-Hecke-period-row.md) 保留

$$
g(Y)=127,\quad P_0=\phi(c_0),\quad
\mathscr L_j=\mathcal O_Y(-Z_j),\quad
\mathscr M_j=\mathscr L_j(254P_0).
\tag{868.1}
$$

五个 $\mathscr L_j$ 是 [R849](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md) 的 `eta_degree_zero_fractional_ideal`，不是同一 DAG 中三同源后的 `real_descent_degree_zero_fractional_ideal`。具体是

$$
\mathfrak L_j=\mathfrak N(I_{E_{g_j}})^{q_j}
                  \mathfrak N(I_{E_f})^{-p_j},\qquad
\mathfrak N(I)=\prod_{k=0}^{6}\sigma^k I,
\tag{868.2}
$$

其中原 $(p_j,q_j)$ 仍为 $(165,67),(93,67),(100,67),(168,67),(371,134)$。原 $\eta_{h_j}=-[\mathfrak L_j]/q_j$、$\beta$、$\kappa$、原 Galois/目标缩放、两个具体帧及非 $p$ 比较均不变。原 $t=a^3$ 是 YP 在 P0 使用的参数，下面铅笔变量 $z$ 不是 $t$。

原铅笔 $\pi:Y\to\mathbf P^1$ 的次数为272，$H=\pi^*\mathcal O(1)$，两图普通正规基为

$$
R_\tau=\bigoplus_{i=0}^{271}K[z]\beta_i,\qquad
R_\sigma=\bigoplus_{i=0}^{271}K[v]\gamma_i,
\quad v=z^{-1},\quad \gamma_i=v^{\epsilon_i}\beta_i,
\quad \epsilon=(0,1^{144},2^{127}).
\tag{868.3}
$$

这里 $K=\mathbf Q(\zeta)$。涉及原 B 和五极理想时仍沿原 $K\subset L$，再按已证真范数下降；不把其未下降函数系数改称 $K$ 值。

[R856](../results/R856-certified-original-two-chart-point-and-fixed-branch-ideals.md) 已准确给出 P0 的全部272个两图基值、完整点理想及 $z_0=z(P_0)\ne0$、$v_0=z_0^{-1}$。真实小源中

$$
z_0=-\frac{497}{7491}-\frac{20008}{7491}\zeta,
\qquad w_0=w(P_0)=-\frac{1557}{2497},
\quad w=e_2/\tau=\beta_1.
\tag{868.4}
$$

这些是读取原 `R856-original-P0-normal-values.json.gz` 的准确字段，不是本篇重算值。原 $\tau(P_0)=67419/4\ne0$、$\sigma(P_0)\ne0$ 已由该源认证。

[R860](../results/R860-certified-original-semilinear-resolvent-DAG.md) 保存了已成 R806 全部34组的准确来源、690个 S 行到多项式系数的映射及 $W=M_w\in\operatorname{Mat}_{272}(\mathbf Q[z])$。列为输入，行为输出；原基的 $82$ 尺度已经在这些系数里，不再插入。后文只在 $z_0$ 对这些已成多项式求值，不重构 W，不求完整 Krylov 逆。

## 2. 一维核给完整 P0-socle：允许原纤维分歧

置

$$
A_0=W(z_0)-w_0 I_{272}.
\tag{868.5}
$$

原 P0 评价向量 $b=(\beta_i(P_0))_i$ 满足 $b_0=1$ 和 $b^tA_0=0$，故 $\operatorname{rank}_K A_0\le271$。本篇首个新算术条件是：在真实来源的合法约化处，找到一个非零271阶子式。它只证明特征零的秩至少271；与上述几何上界合用，得到

$$
\operatorname{rank}_K A_0=271.
\tag{868.6}
$$

若某个约化未给这样的子式，记录该次充分检验未通过；不得称特征零秩已小于271。

取 $A_0h=0$ 的非零准确列向量，将实际选中的一个自由原 normal 坐标归一为 $h_k=1$。定义

$$
r_\tau=\sum_i h_i\beta_i\in R_\tau,
\qquad f_\tau=\frac{r_\tau}{z-z_0}.
\tag{868.7}
$$

### 命题868.1

在 (868.6) 成立时，$f_\tau$ 在 $U_\tau$ 的唯一极点是原 P0，且极阶恰为1。因此

$$
I_{P_0,\tau}^{-1}=(1,f_\tau)_{R_\tau},\qquad
I_{P_0,\tau}^{-m}=(1,f_\tau^m)_{R_\tau}\quad(m\ge1).
\tag{868.8}
$$

**证明。** 原 $R_\tau$ 是光滑曲线的正规仿射环，并在 $K[z]$ 上自由。令

$$
\mathcal A=R_\tau/(z-z_0)R_\tau.
\tag{868.9}
$$

它是272维有限 K 代数；$A_0$ 正是其中乘 $w-w_0$ 的矩阵。把域扩到代数闭包以后，$\mathcal A$ 是原纤维各点的 Artin 局部因子之积。在点 Q 的因子中，取曲线的局部参数 $u_Q$，设

$$
e_Q=\operatorname{ord}_Q(z-z_0),\qquad
\mathcal A_Q\simeq\overline K[[u_Q]]/(u_Q^{e_Q}).
\tag{868.10}
$$

若 $w(Q)\ne w_0$，乘 $w-w_0$ 可逆；否则其核的维数是
$\min(e_Q,\operatorname{ord}_Q(w-w_0))\ge1$。P0 已贡献至少1维，而整个核只有1维。因此只有 P0 因子贡献，且该核正好是 P0 因子的完整 socle $u_{P_0}^{e_{P_0}-1}\overline K$。这一步不假设 $e_{P_0}=1$；当 $e_{P_0}>1$ 时，秩条件同时迫 $\operatorname{ord}_{P_0}(w-w_0)=1$。

$h\ne0$ 给出的 $r_\tau$ 模 $z-z_0$ 是这个 socle 的非零元素，所以

$$
\operatorname{ord}_{P_0}(r_\tau)=e_{P_0}-1,
\qquad \operatorname{ord}_{Q}(r_\tau)\ge e_Q\quad(Q\ne P_0\text{ 在该纤维上}).
\tag{868.11}
$$

除以 $z-z_0$ 后，P0 的阶恰为 $-1$，其他纤维点的阶非负；其余 $U_\tau$ 点的分母为单位。这证明极点断言。每个曲线 DVR 上，$(1,f_\tau^m)$ 的阶为 $\min(0,m\operatorname{ord}f_\tau)$，恰是 $-mP_0$。完整可逆分式理想由这些局部阶决定，故得到 (868.8)。这里没有把一般多变量环中的理想幂误改成两个纯幂生成元。证毕。

该证明也可表述为：$\mathcal A$ 的各局部因子是单参数完全交，故为 Gorenstein；一维核正好挑出 P0 的全部 socle。仅用“右核是一维”而忽略其他纤维因子或分歧阶，不足以得到简单极点结论。

## 3. 原第二图无需重复求核

记 $D(v)=\operatorname{diag}(v^{\epsilon_i})$。正规坐标的运输是 $y_\sigma=D(v)^{-1}y_\tau$。乘 $w_\sigma=vw=e_2/\sigma$ 的矩阵为

$$
W_\sigma(v)=vD(v)^{-1}W(1/v)D(v).
\tag{868.12}
$$

因此同一个准确 h 给出

$$
h_\sigma=D(v_0)^{-1}h,
\qquad
r_\sigma=\sum_i (h_\sigma)_i\gamma_i,
\qquad f_\sigma=\frac{r_\sigma}{v-v_0}.
\tag{868.13}
$$

在 $v_0$，(868.12) 与 $A_0$ 只差可逆的左右对角因子及非零标量 $v_0$，所以其秩也是271。不得把 $D(v_0)^{-1}$ 漏掉，也不得给第二图另换一个未经记录的归一化。

原第二图的 P0 仍是 R856 的同一点。因此同一局部证明给

$$
I_{P_0,\sigma}^{-254}=(1,f_\sigma^{254}).
\tag{868.14}
$$

两图重叠的实际标量关系还可直接写出：

$$
f_\sigma=-zz_0f_\tau+u,\qquad
u=z_0\sum_{\epsilon_i=1}h_i\beta_i
  +z_0^2(v+v_0)\sum_{\epsilon_i=2}h_i\beta_i.
\tag{868.15}
$$

这是由 $\gamma_i=v^{\epsilon_i}\beta_i$、$v-v_0=-(z-z_0)/(zz_0)$ 逐项得到的原函数恒等式。$u$ 在重叠上为正规函数，$-zz_0$ 为单位；故两组 $(1,f_c)$ 给同一嵌入分式理想。若后续要一份显式冗余生成元运输，可保留 $1,f_c,\ldots,f_c^{254}$，以 (868.15) 的二项式三角矩阵运输；其对角是 $(-zz_0)^k$，全部为重叠单位。两生成元版本 (868.14) 的完整性则依命题868.1 的 DVR 证明，不假称已经求得冗余生成元对两个端点幂的全部 Bézout 系数。

## 4. 首个准确新截面与五个目标理想

由 $\epsilon_i\le2$，有 $r_\tau\in H^0(2H_\tau)$。在 $\tau=0$ 的点，$z-z_0$ 的极阶就是 $H_\tau$ 的重数。因此 (868.7) 实际满足

$$
\operatorname{div}_\infty(f_\tau)\le P_0+H_\tau.
\tag{868.16}
$$

它在 P0 的一阶极点又使它不属于原146维 $H^0(H_\tau)$。因 $\deg(H+P_0)=273>252$，RR 给 $h^0(H+P_0)=147$。所以

$$
1,z,\beta_1,\ldots,\beta_{144},f_\tau
\tag{868.17}
$$

是一个实际完整147基；其中前146项全部原样复用，只有最后一项是本消费者的新准确源。第二图同理。这里的147不是 YP 的128或634，也不是已完成五个 $\mathscr L_j$ 的 RR。

消费 R849 已完成的原十个 $\mathfrak L_{j,c}$ 节点以后，可立即构造

$$
\boxed{M_{j,c}
 =\mathfrak L_{j,c}(1,f_c^{254})
 =\mathfrak L_{j,c}+f_c^{254}\mathfrak L_{j,c},
 \qquad c\in\{\tau,\sigma\}.}
\tag{868.18}
$$

这已经是 YP 所要 $\mathscr L_j I_{P_0}^{-254}$ 的两个完整仿射分式理想，嵌入原函数域的方向准确。负次幂中的“负”只来自 $I_{P_0}=\mathcal O(-P_0)$，不是改成截断整理想商。函数幂可以保成254次幂 DAG；准确 h 及两个一次分母必须实际输出，不能仅以一个未展开的余子式描述替代本篇新截面。

新图应直接引用原 `eta_degree_zero_fractional_ideal`；不把 $\mathfrak L_j^R=\mathcal R_j\mathfrak L_j^3$ 误接成 $\mathfrak L_j$，也不丢弃原 $\mathcal R_j$、$\kappa_j$、$\nu_j$ 或指定 theta 二挠比较。R860 已证明的真实半线性作用可作用于这些准确函数；本篇不从 h 的坐标属于 K 自动宣称它 Q 固定。

## 5. 128维出口的固定两权结构

### 定理868.2

对每个原 $\mathscr M_j=\mathscr L_j(254P_0)$，都有

$$
\pi_*\mathscr M_j\simeq
\mathcal O_{\mathbf P^1}^{128}\oplus
\mathcal O_{\mathbf P^1}(-1)^{144}.
\tag{868.19}
$$

这一分裂型没有未知整数；它不等于一份已经算出的分裂同构。

**证明。** 令 $E=\pi_*\mathscr M_j$。有限平坦映射使 E 为秩272的向量丛，且上同调与 Y 上相同。因 $\deg\mathscr M_j=254>2g-2=252$，

$$
h^0(E)=128,\quad H^1(E)=0,
\qquad H^0(E(-1))=0
\tag{868.20}
$$

最后一项因为 $\deg(\mathscr M_j-H)=254-272=-18$。基变换后，对每个几何点 x，$H^0(E(-x))=0$，故评价 $H^0(E)\to E_x$ 单射。于是评价给一个子丛 $\mathcal O^{128}\hookrightarrow E$，商 Q 为秩144的向量丛。Euler 特征数给 $\deg E=-144$，并从短正合列得到 $H^0(Q)=H^1(Q)=0$。

对每个几何点 x，$H^1(Q(1)(-x))=H^1(Q)=0$，所以 $Q(1)$ 全局生成；同一正合列给 $H^1(Q(1))=0$。由 $\deg Q=-144$ 可得 $h^0(Q(1))=144$，其评价在每个纤维都是144阶同构，因而 $Q(1)\simeq\mathcal O^{144}$。最后 $\operatorname{Ext}^1(\mathcal O(-1),\mathcal O)=H^1(\mathcal O(1))=0$，扩张分裂，得到 (868.19)。该证明不需要先计算任何原理想的 HNF。证毕。

于是对 $n\ge0$，完整齐次截面模为

$$
\bigoplus_{n\ge0}H^0(\mathscr M_j+nH)
\simeq K[\tau,\sigma]^{128}
      \oplus K[\tau,\sigma](-1)^{144},
\qquad h^0=128+272n.
\tag{868.21}
$$

### 推论868.3（单个完整纤维秩的充分证书）

若已用 (868.18) 的**准确完整两图**认证

$$
s_1,\ldots,s_{128}\in H^0(\mathscr M_j),\qquad
t_1,\ldots,t_{144}\in H^0(\mathscr M_j+H),
\tag{868.22}
$$

且其正规函数列 $[s_i\mid t_a/\tau]$ 在 $K(z)$ 上秩272，则它们给 (868.19) 的分裂同构。特别，$s_1,\ldots,s_{128}$ 就是完整128维 RR 基。

**证明。** 这些真实截面给向量丛态射
$\mathcal O^{128}\oplus\mathcal O(-1)^{144}\to E$。两边秩、次数均相同，所以其行列式是一条次数0线丛的全局截面；在 $\mathbf P^1$ 上，一旦非零就处处可逆。因此全局同构，取全局截面即得结论。证毕。

可在一个合法有理/有限剩余域的 z 值上，以实际272阶非零子式证明函数域秩；只要所有候选、包含证书及求值分母在该处有定义即可。这里检验的是函数域秩下界，不要求该评价在整个大空间上单射，也不必额外假设所选纤维避开原 $Z_j$ 的全部支撑。非零子式不能替代 (868.22) 的准确两图包含；只有模候选或单图正规性不能直接填真。

实际取得这两组后，所有后继权的基都按 (868.21) 的 $\tau,\sigma$ 单项式给出，无需继续盲增权或重新做一次不定界的饱和。这是对 [FM](../notes/2026-11-16-original-Y-finite-RR-matrices-and-source-leaves.md) 完整有限矩阵出口的新增固定维数/权数认证，不是声称其有限候选域已经物化。

## 6. 单一公开消费者：准确 h 而非仅一个新表示法

首 scope 固定为 `P0_single_pole_and_five_degree254_module_sources`。输入仅需：

1. R860 的完整原 W 来源索引、34组准确有理系数及原 primitive/normal 标签；
2. R856 原272个两图 P0 值、完整点理想和来源证明；
3. R849 已成五个 $\mathfrak L_j$ 的准确 DAG、原 source/certificate/manifest 以及其被引用的真实载体身份。

原 R860 的 $c_Y$、三条旧共轭、W 的34组、R856 的点值和点理想都不重算。

消费者依次完成：

- 原 $W(z_0)-w_0I$ 的合法有限域约化、271阶子式，以及原 P0 左评价核的全行核对；
- 固定该行列集与一个自由原 normal 坐标，对271阶 K 系统作一次准确求解。实现可把 K 的两坐标展开为542阶有理系统，保存一次固定模逆和每次返回的完整 Dixon 余数；严格有理重构后必须对**全部272个 K 方程**准确乘回。未完成部分保存 source-bound 当前断点，不能把模核填作准确 h；
- 输出原 h、$h_\sigma=D(v_0)^{-1}h$，其自由坐标1规范、两图一次分母及 (868.15) 的准确来源；
- 输出两图 $I_{P_0}^{-254}$ 的完整两生成元图、原147基接口，以及十个 (868.18) 的原目标仿射模块图。

准确求解若因预算未完成，保已成271子式及当前 lift，后继从实际余数继续；不重复该子式或已成系数块。此任务不求原 W 的全逆或 $\beta_{72}$ 的新幂基坐标，不取新的 p-adic 高度数据，不改变原 $\eta$ 或 splitting。

实际最终标志应分开：`point_fiber_rank_271_certified`、`exact_normal_socle_vector_computed`、`both_point_inverse_power_ideals_certified`、`five_degree254_affine_module_DAGs_defined`、`degree254_RR_basis_128_computed`、`original_connection_or_height_computed`。首 scope 成功只允许前四项为真；后两项仍为假。

## 7. 仍需执行的最小后继，不隐藏成已完成

(868.18) 消掉了 FM 入口中一个具体的大逆理想构造：不再对原 $I_{P_0}^{254}$ 求272维反复核/HNF，而是消费一个已准确解出的 h 和两次幂节点。它也给一条实际新增 meromorphic 截面，不仅重复 R860 的余子式描述。

原五个 $\mathfrak L_j$ 的系数仍通过 R849 的真实 `exact_unit_solve_expression` 及完整极理想图定义；它们没有因本篇的固定维数定理自动变成已展开多项式生成矩阵。下一数学出口必须从这些原输入实际取得 (868.22) 的真实两图包含源，或执行 FM 的完整有限矩阵后给128核。可以用原单位子式和已证维数将该核保存成准确单位解表达式，但不能把旧 R842、R827 的模列换一个标签作为这些截面。

本篇没有求出 YP 的 $a_j,c_j,a_j(P_1)$，没有完成 $634\to508$ 的连接主部映射，也没有计算原 Hecke 周期行、非 p 项或指定高度。原 Q 下降须沿 R860 的真实半线性作用，而非依据函数坐标看起来有理。
