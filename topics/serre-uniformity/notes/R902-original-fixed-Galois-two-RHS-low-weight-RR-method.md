# R902：原五个方向的固定 Galois 单位图、两右端与完整低权 RR 消费

日期：2026-11-16 UTC。会话：serre-public-astra-20261115。

本篇落实 [R896 §7](../results/R896-original-two-denominator-low-weight-residual-RR-kernels.md) 已证明的严格共轭契约，不另立一个下降定理。新增计算缩减是：每个初始 RR 空间仍由原单位方块准确定义，但六个新常数域共轭只需物化后继实际使用的两条 B 截面。后续残余空间、146 核和418空间全部完整计算、全部原行乘回。

R893 的五个初始空间已实际完成。R896 随后在公开 run43872960726 / source259e2448c7c51131fecc231ee55f7d457397dde8 真正成功；其完整最终证书为15429字节、SHA256 `66218771f4b0f8d7822282839ca94bcb34049fc3d867248ae4eddf6348fdb24c`。本消费者只从该真实完成来源读取五组选择；未读取的成员身份不预填，三十个共轭子式和新模数组仍未计算。所有新算术只能在原公开仓库 Actions 执行；原已完成阶段逐字复用。

## 1. 固定原对象，不重选代表

沿 R893、R896 的原曲线、原 $K=\mathbf Q(\zeta_3)\subset L$、原常数域生成元 $b$、原铅笔 $(\tau,\sigma)$ 和原正常基 $\beta_i$。为免与第二个铅笔截面混淆，下文将 $\operatorname{Gal}(L/K)$ 的既定生成元写作 $\gamma$；它就是原来源中的 `sigma_power`，不是新选的自同构。

原几何记号为

$$
H=(\tau)_0,\quad \deg H=272,\quad g(Y)=127,\quad
z=\sigma/\tau,\quad
\epsilon=(0,1^{144},2^{127}),
$$

$$
V_n=\operatorname{span}_L\{z^a\beta_i:0\le a\le n-\epsilon_i\},
\qquad d_n=272n-126.
\tag{902.1}
$$

原 $z,\tau,\beta_i$、正常纤维代数及导数 $\delta_\tau$ 在 K 上定义；R893 已固定 $\gamma\delta_\tau=\delta_\tau\gamma$。原 $82^2$、$82^{10}$ 和各 R809 目标的有理尺度只沿来源施一次。

对 $j=1,\ldots,5$，保持

$$
g_j=(1+\mathcal T^j)f,\quad y_j=y_{g_j},\quad E_j=(y_j)_\infty,
\quad \mathcal T^7=[\zeta_3^2].
\tag{902.2}
$$

真正七支常数域次序已由 R880 完成来源认证为
`[0,6,1,2,4,3,5]`，不能改为根的数值排序。辅助素点仍是
$\ell=1000000753$、$s=99932770$、$\zeta_3=549966761$，其中 $s=1+2\zeta_3$。整生成元是 $B_{\rm fld}=\lambda b$；$B_{\rm fld}$ 不与截面 B 混用。

每个 j 的原 R893/R896 完成记录须提供：

- 初始完整纤维列表、三种已完成标量插值块、初始 Schur 选行 I、主列 J、自由列 F 及其顺序；
- 原标记 B0 的规范核列编号，以及原 B1 的**整数**参数 c；
- 两 B 产品核的选行、主列、自由列及第二块投影的独立行；
- padding 的同样固定选择、原 v 列，以及原第二锚的整数参数；
- 最后962产品核与418投影的全部固定选择；
- 原 $Q_j$ 的完整主函数 DAG、原 $\rho=z-z(P_0)$ 及 t 首项来源。

这些值均由实际已成 R896 逐项读取。新分支不得重新找主元、换自由顺序、换整数试次或缩放到模点值1后仍称原截面的共轭。

## 2. 真正的共轭函数及仅缺的一条导数

以 $A_r,B_r$ 表示完成七支来源中的 $\gamma^r A,\gamma^r B$，下标按7取模。原 canonical free1186 归一与完整原单位系统使这些是同一准确方向的共轭，而不是任意相似函数对。

对任务 $(j,r)$，$1\le r\le6$，在 R893 的单分母公式中准确代入

$$
A=A_r,\quad B=B_r,\quad
C=\gamma^r(\rho_j)^{-3}A_{r+j},\quad D=B_{r+j},\quad
b=\gamma^r(b),
\tag{902.3}
$$

并将原六个 Hodge 向量 $c_0,\ldots,c_5$ 评价于同一个 $\gamma^r(b)$。这里的 $\rho_j$ 是 R791/R849 原相位；$\gamma^r(\rho_j)^6=\gamma^{r+j}(b)/\gamma^r(b)$。不能用无相位的幂比替代，也不能把 $\mathcal T^7$ 当恒等。

原 $c_j$ 已含同靶微分的相位。本次只对它的真实十四坐标作常数域评价，不再给 $c_j/c_0$ 乘一次 $\rho_j$。其 `coordinate_numerators / column_denominators` 与 `original_target_rational_scales`、S5 行索引逐项原样绑定。新的模评价不等于新的 char0 重构。

导数仍是

$$
\delta_\tau a=\Gamma_\tau a+M_g\,\partial_z a.
\tag{902.4}
$$

R893 已完成 $\delta A_0,\ldots,\delta A_5$ 及相应 $\delta B$；six-Dstar 已完成其余六支的 $\delta B$。因此整个三十任务最多只新增 **$\delta A_6$ 一条**。其余导数均按原 producer/tag/bytes/SHA 复用。原 $M_g,\Gamma_\tau$ 各17个16行块只读；新列按这些块原子保存，不重建算子、旧 S5、旧 A/B 或旧导数。

将 (902.3) 与这些原导数代入 R893 (893.6)–(893.10) 的原同权98表达式，即得 $\gamma^r(P_j),\gamma^r(Q_j)$。准确 F 只约去原来的一次，不增添单独 F、Wronskian 或 Hodge 分母单位条件。

## 3. 固定旧完整纤维，重新认证新 Q

每个 $(j,r)$ 使用原 j **同一个** N 节点列表与顺序。它们的完整272维 Artin 代数、W、Krylov 矩阵/逆、单次关系多项式、正常 V3 评价及三种标量 Lagrange 块均为旧 K 来源。不得重跑旧0至26节点、273个特征多项式节点或旧逆。

在每个旧完整代数中，实际核验新的 $\gamma^r(Q_j)$ 为单位，并保全

$$
\gamma^r(Q_j)U_{j,r}=1,\qquad
\gamma^r(Q_j)Y_{j,r}=\gamma^r(P_j)
\tag{902.5}
$$

的全部272坐标。只在这些式子通过后使用乘 $Y_{j,r}$ 的矩阵。没有将完整代数压成一点、剥掉失败因子或忽略 nilpotent 部分。

若任一固定节点的新 Q 不是单位，本任务保存真实失败阶段并停止该固定图；不改节点后冒称同一原数值图，也不据此否定准确共轭函数。R902 的有限充分证书没有成功预设。

## 4. 初始完整空间的准确图与两个实际 RHS

令 $\mathcal S_j$ 是 R893 (893.21) 的原 Schur 矩阵。其 char0 秩已独立证明等于 $e_j=\deg E_j$，完整核维数为 $r_j=d_{n_j}-e_j$。原已成图记录

$$
U_j=\mathcal S_j[I_j,J_j],\qquad
\mathcal B_{j,J_j}=-U_j^{-1}\mathcal S_j[I_j,F_j],\quad
\mathcal B_{j,F_j}=I_{r_j}.
\tag{902.6}
$$

对新 r，$\mathcal S_{j,r}=\gamma^r(\mathcal S_j)$。实际只需构成同一选行的方块

$$
U_{j,r}=\mathcal S_{j,r}[I_j,J_j]
\tag{902.7}
$$

并认证其行列式在当前原素点非零。准确 $\det U_{j,r}=\gamma^r(\det U_j)\ne0$ 已由共轭给出，但其在固定剩余处是否单位仍需本次真实检查。

这个准确方块和固定 I/J/F 已定义**整个**共轭空间
$\gamma^r H^0(n_jH-E_j)$。本任务不物化其全部 $d_{n_j}\times r_j$ 数值核。设原 R896 B0 取第 $k_j$ 列，原 B1 的整数参数为 $c_j^{\rm int}$，置

$$
W_j=\left[e_{k_j},\ (1,c_j^{\rm int},(c_j^{\rm int})^2,
 \ldots,(c_j^{\rm int})^{r_j-1})^{\mathsf t}\right]
\in\operatorname{Mat}_{r_j\times2}(\mathbf Z).
\tag{902.8}
$$

若原 source 采用更一般的已存整数组合，则用其原整数字串而非模剩余作同一准确输入；首实现沿原 R896 的列与幂参数。

只求

$$
\boxed{
\mathcal B^{[2]}_{j,r,F_j}=W_j,\qquad
U_{j,r}\mathcal B^{[2]}_{j,r,J_j}
 =-\mathcal S_{j,r}[I_j,F_j]W_j.
}
\tag{902.9}
$$

右端只有两列。所需选行可以直接由新 $Y_{j,r}$ 及旧标量插值块形成；无需形成其余 Schur 行、全部自由列解或新的 dense A 逆。实现对 $[U_{j,r},\mathcal S_{j,r}[I_j,F_j]W_j]$ 做固定首方块消元并核选行乘回，不能把消元选出来的另一列顺序当作旧 J。

**两 RHS 的准确性。** $W_j$ 为整数，故被 $\gamma$ 固定。将 $\gamma^r$ 施于 (902.6) 与原两列定义，得到 (902.9)；方块可逆保证解唯一。因此两条新准确截面恰为原 B0、B1 的 $\gamma^r$ 共轭。其余完整空间仍由 (902.6) 的共轭表达式定义，但输出必须分别标记：

- `complete_initial_space_exact_unit_solve_defined=true`；
- `materialized_initial_B_columns=2`；
- `full_conjugate_initial_B_basis_numerically_materialized=false`。

不得把两列的实际数组称为完整新 B 核。

## 5. 两列的全部原关系，而非只验选行

对这两条 B，复用原三个标量插值块恢复两条 A。对每个正常分量 i，$m_i=n_j-\epsilon_i+1$，准确公式仍为

$$
A_i=L_i\bigl((Y_{j,r}B)_i\text{ 在原前 }m_i\text{ 个节点的值}\bigr).
\tag{902.10}
$$

随后检查原全部 N 个完整纤维的

$$
A^{[2]}_{j,r}(a)-Y_{j,r}(a)B^{[2]}_{j,r}(a)=0
\quad\text{共 }272N\times2\text{ 个坐标。}
\tag{902.11}
$$

保存两条 B 的每个完整正常/循环纤维值。没有原来的 $272\times r_j$ 全核评价，却有本后继两 B 产品需要的全部 $272\times2$ 实际值。

原 $272N>272n_j+e_j$ 的全局注入在常数域共轭后不变。准确秩仍为 $e_j$，所需分母和 (902.7) 的单位性给同一 DVR 上的准确图；(902.11) 逐行核其真实约化与实现。完整空间结论来自这一准确图与已证秩，不来自将两个任意模向量提升。

以下固定数值均沿原方向：

| j | n | e | N | 完整初始空间维数 | 本次初始物化列数 | 两 B 残余维数 | padding |
|---:|---:|---:|---:|---:|---:|---:|---:|
|1|12|2970|23|168|2|396|250|
|2|8|1674|15|376|2|188|42|
|3|8|1800|15|250|2|314|168|
|4|13|3024|25|386|2|178|32|
|5|14|3339|27|343|2|221|75|

## 6. 后续所有空间保持完整，所有选择保持原样

### 6.1 原未缩放 B0 与完整残余空间

用原正常点泛函和首 jet 实际核新 A0 在 P0 为单位、新 B0 首系数为单位。B0 的准确常数项为零和准确阶1来自原 c0 源及严格共轭，不由有限精度零单独推出。固定原列；即使另一列更便利，也不切换。

在原全部 N 个纤维构成

$$
[\,\gamma^r(B_0)V_3,\ \gamma^r(B_1)V_3\,].
\tag{902.12}
$$

$N>n_j+3$ 保整个 $V_{n_j+3}$ 的注入。继承原 R896 的选行、主列和自由块，实际认证秩 $690+\delta_j$，求**全部**规范关系核，检查全部 $272N$ 行。继承原第二690行投影的独立行，再核同一投影子式非零。所得完整空间恰为 $\gamma^r H^0(3H-F_{0,j})$。

此处保存396、188、314、178、221个完整正常列；不再应用“两 RHS”缩减。

### 6.2 padding 的完整146核

旧正常 V3 的0至251阶点矩阵已足覆盖全部 $k_j\le250$ 及第 $k_j$ 阶。它在 K 上定义，故不重新生成 jets。将前 $k_j$ 行乘新残余空间，以原 padding 选行/主列/自由列求完整146核并全行乘回。

原 v 的列编号保持；只验证该**同一列**第 $k_j$ 阶为单位。原第二锚仍用原146基的同一整数幂组合。由单位解唯一性，二者恰为原 v、w 的共轭，所有尺度保持未归一化。

### 6.3 真962与完整418

在原固定前七个完整纤维计算两个新低权锚的 V3 产品，长度1904严格大于 $\deg6H=1632$。继承原962单位图和第二690行投影的独立行，检查全部1904行，输出真正690×418正常矩阵。

原 R896 Koszul/次数夹逼与准确共轭保证这是完整

$$
\gamma^r H^0(3H-D_j^{\rm std}),
\qquad D_{j,r}^{\rm std}=\gamma^r D_j^{\rm std},
\quad\deg D_{j,r}^{\rm std}=272,\quad P_0\notin D_{j,r}^{\rm std}.
\tag{902.13}
$$

若任何继承子式在新分支非单位，只记本固定图未完成；不重选后给原共轭标签。

## 7. 完整主函数与原帧逐项共轭

原 $q_\chi=u_\chi/\tau^2$ 与原 $t=c\rho+O(\rho^2)$ 都在 K 上定义，沿其原完成来源读取。每个任务保存

$$
G_{j,r}=\frac{\gamma^r(B_{0,j})/\tau^{n_j}}
 {\gamma^r(v_j)/\tau^3},\qquad
Q_{j,r}=G_{j,r}q_\chi^{-(n_j-2)}=\gamma^r(Q_j).
\tag{902.14}
$$

若使用已除 $\tau^{n_j}$ 与 $\tau^3$ 的正常数组，只作其比值；不再施一次 $\tau^{3-n_j}$。齐次表达式仍明确记录 $G=\tau^{3-n_j}B_0/v$。

准确除子恒等式是

$$
\gamma^r(E_j)-e_jP_0
 =(D_{j,r}^{\rm std}-H)+(n_j-2)(D_\chi-H)
 +\operatorname{div}Q_{j,r}.
\tag{902.15}
$$

设新未缩放 B0 的原 $\rho$ 首系数为 $b_{1,j,r}$，新 v 的第 $k_j$ 系数为 $v_{k_j,j,r}$，旧 $u_\chi$ 的第272系数为 $u_{272}$，则

$$
\operatorname{ord}_{P_0}Q_{j,r}=1-e_j,\qquad
\operatorname{LC}_\rho(Q_{j,r})=
 \frac{b_{1,j,r}}{v_{k_j,j,r}}u_{272}^{-(n_j-2)},
$$

$$
\operatorname{LC}_t(Q_{j,r})=
 \operatorname{LC}_\rho(Q_{j,r})c^{e_j-1}.
\tag{902.16}
$$

输出既保完整原 $Q_j$ DAG/ref 与明确 $\gamma^r$ 作用，又保新单位解节点组成的同一 $Q_{j,r}$。不只保存有限域首项，不给新的截面乘任何模标量，不把辅助 $\ell$ 单位称为41单位。

## 8. 最小真实输入与执行顺序

原来源分为三类，身份不能混写：

1. **已完成原选择。** R893 的五个完整证书、原 I/J/F、scalar blocks、所有 K/关系及已成导数；R896 真完成后给五个标记对、两整数参数、所有低权选图/投影行、v 列、完整418和 marked Q。$r=0$ 五项只外引这些来源。
2. **已完成原算术叶。** 七支 A/B、R809 六组准确十四坐标、R849 原相位/域作用、R827 原 W/G/Γ、sixD 的 $\delta B_6$、原正常 V3 纤维/点 jets、$q_\chi$ 与 t 帧。原载体用于运输，读出的每件仍保自己的 producer/configuration/bytes/SHA。
3. **确实新增。** 一条 $\delta A_6$；同一十四坐标的指定新常数域评价；每 $(j,r)$ 的新 Q 单位和完整 y 乘法、继承选行方块与两 RHS、两条原关系全行验证、完整残余/146/418及其原主函数首项。

初始选行只保存实际所需 Schur 行，不重建原完整 Schur。两条 A 的恢复仍用旧标量块。所有旧零阶 K、正常 V3 评价、旧导数、旧 jets、旧 S5/Norm/Hom 常数均不重算。原 $r=0$ 的任何数学结果不重新打新 tag。

首实现固定任务顺序 $(j,r)$ 按 j 再 r 排列。预算与本次最多执行任务数是运行控制，不改变数学 tag；原来源、固定策略、准确相位、既定顺序和 helper/core/proof SHA 均进入 tag。已完成阶段原子落盘；同 tag 续接只从缺失阶段继续。

## 9. 明确的输出契约

数学结果名为 `R902-original-six-Galois-five-sum-Hom-low-weight-RR`，最终文件为 `p41-original-six-Galois-five-sum-Hom-low-weight-RR-certificate.json`。

最终 `complete_direction_conjugate_certificates[j][r]` 仅列实际完成的 $1\le r\le6$；`original_sigma0_direction_certificates` 只存原 R896 引用。每个新完整证书名为
`R902-j{j}-sigma-{r:02d}-complete-low-weight-RR-certificate.json.gz`，其中：

- `complete_normal418_space` 指690×418真实完整正常基；
- `marked_principal_Q` 指完整主函数 DAG、原零支 Q 引用、准确共轭身份及原 $\rho/t$ 首项；
- `strict_original_selection_and_integer_anchors_preserved=true` 只在所有固定图、参数、列与投影行核对后成立；
- `materialized_initial_B_columns=2` 与 `full_conjugate_initial_B_basis_numerically_materialized=false` 始终区分完整空间定义和本次两列实际数值；
- `complete_residual_space_certified`、`complete_146_space_certified`、`complete_418_space_certified` 分别对应真正已完成的全核，不由初始两列先行置真。

完整 scope 成功要求三十项全成；非单位或预算停止保所有已完成阶段和当前任务指针。未完成 FINAL 不约束后续新阶段清单；已完成 FINAL 的全部引用必须与当前实际 manifest 精确一致。

本消费者不计算原 Hecke 活跃支持、非 p 项、Picard 主性、连接、周期或 height。它给 R901 所需的三十个严格共轭正常418空间和同一原 marked Q，不能把这些输入准备完成冒充后续聚合树或原高度已成。
