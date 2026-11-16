# R880 — 复用原 D 铅笔与共同 cusp 小核的有界极除子输入

日期：2026-11-16。状态：**完整纸面证明和实际源契约；本篇新列核、123阶截取及962秩尚未运行。** 原 R845 的1111秩、十个乘积块，及 R872 的273阶点 jets、固定类的418维空间都已经实际完成。本篇只增加它们尚未给出的有界代表及完整 RR 列，不重做原乘积、选行、Krylov 逆或点 jets。

## 1. 固定原对象和实际已成输入

保持原 $K=\mathbf Q(\zeta)$、$L=K(b)$、$Y_K$、$P_0=\phi(c_0)$，以及原两图锚截面 $\tau,\sigma$。以下含原 $D$、原 Hom 或 R845 截面的构造在 $Y_L$ 上进行；共同 cusp 块及固定 $\chi$ 可先在 $K$ 上完成，再忠实基变换到 $L$。不能把原 $D$ 偷降到 $K$。

记 $C$ 为全部20个原尖点的完整有效除子，$H=\operatorname{div}\tau$，并固定

$$
g(Y)=127,\qquad \deg H=272,\qquad
V_m=H^0(Y,mH),\qquad \dim V_3=690.
\tag{880.1}
$$

[R838](../results/R838-certified-original-second-derivative-ideal-and-minimal-order3.md) 与 [R845](../results/R845-certified-original-D-pencil-and-eight-pole-generators.md) 给的是原 $f=f_4$ 的准确有效除子

$$
E_f=(y_f)_\infty=C+P_0+3D,\qquad
\deg D=395,\qquad P_0\notin C\cup D\cup H .
\tag{880.2}
$$

R845 已取得原 $H^0(3H-D)$ 的准确单位解基 $w_0,\ldots,w_{294}$，并实际认证

$$
a=w_0,\qquad b_D=\sum_{j=0}^{294}w_j,\qquad
\gcd(\operatorname{div}_{3H}a,\operatorname{div}_{3H}b_D)=D.
\tag{880.3}
$$

其中 $b_D$ 不是椭圆曲线常数 $b$。原五个完整纤维 $z=0,1,2,3,4$ 的矩阵

$$
M=\operatorname{ev}_5[\,aV_3,\ b_DV_3\,]\in
\operatorname{Mat}_{1360\times1380}
\tag{880.4}
$$

已经保存十个完整 $272\times690$ 乘积块；实际秩1111、选中子式模值633901576，原辅助素数 $\ell=1000000753$。旧秩阶段保有准确原行/列编号，**没有保存这个1111阶子式的逆**。所以后继求其逆或269个自由右端属于真正新增算术，重新做十个乘积或原 RREF 则没有必要。

R872 的真实 run43830071469/sourcea07453ec81e832b0aeef99bded2efaa763adaf13 已给原 $P_0$ 的同一局部参数 $\rho$ 下第0至272阶 normal jets，以及完整固定类输入

$$
\chi=H-272P_0,\qquad
\operatorname{div}_{2H}u_\chi=272P_0+D_\chi,\qquad
\deg D_\chi=272,\quad P_0\notin D_\chi,
\tag{880.5}
$$

$$
W_{D_\chi}=H^0(3H-D_\chi),\qquad \dim W_{D_\chi}=418.
$$

原 $\rho$ 是该运行真正选中的 $z-z_0$ 或 $w-w_0$，不是未经比较就改称原 $t=a^3$。本篇直接保留其实际参数和原 jet 定义，不重算。

## 2. 旧1111子式的269个新右端给完整残余除子空间

先在同一原剩余嵌入读 $a/\tau^3,b_D/\tau^3$ 的真实零阶值。若前者是单位，取 $(a_\ast,b_\ast)=(a,b_D)$；否则若后者是单位，交换两列块。交换时仅重排旧矩阵列和旧子式列编号，不重新计算乘积。若两者的模值都为零，本素点测试如实停止；不能把特征零无公共零误写成这个约化处已有单位。

令

$$
\operatorname{div}_{3H}a_\ast=D+F,\qquad \deg F=421.
\tag{880.6}
$$

实际选中的零阶单位保证 $P_0\notin F$。由 (880.3)，$a_\ast,b_\ast$ 的残余零除子互不相交。

### 命题 880.1

旧矩阵 (880.4) 的完整核维269，投影到 $b_\ast$ 的输入块是单射，像恰为

$$
W_F=H^0(3H-F),\qquad \dim W_F=269.
\tag{880.7}
$$

**证明。** R845 已证明原乘法像是 $H^0(6H-D)$，其维数为
$1632-395+1-127=1111$。旧完整纤维评价在该像上的秩也为1111，故在这个已经确定的像上单射。因此旧评价核就是原全局函数关系核。这里不假定评价在整个 $V_6$ 上单射，不假定五纤维避开 $D$，也不要求纤维约化。

对关系 $a_\ast r+b_\ast s=0$，若 $s=0$ 则 $r=0$。在每个 DVR，消去共同的 $D$ 后，$a_\ast$ 的残余零阶就是 $F$ 的重数，而 $b_\ast$ 在该支撑为单位。因此 $r=-b_\ast s/a_\ast$ 属于 $V_3$ 当且仅当 $s$ 属于 $H^0(3H-F)$。反向也逐点成立。该空间次数395大于252，故维数269。证毕。

设旧选行、选列为 $I,J$，其余269列为 $J^c$。新的准确对象定义为

$$
U_J=-M_{I,J}^{-1}M_{I,J^c},\qquad U_{J^c}=I_{269}.
\tag{880.8}
$$

使用旧单位子式求模像，并核全部 $1360\times269$ 残差；准确特征零定义仍是 (880.8) 及旧原全局乘法。特征零秩上界与旧单位下界相等，所以没有被遗漏的行约束。投影得到的269列也须保原来源、自由坐标和准确 solve 表达式，不能把它们的有限域条目标为已重构的有理系数。

## 3. 123个旧 jet 条件给新的146空间和272度代表

在 $W_F$ 上取原 $\tau^3$ 平凡化后的前123个系数：

$$
J_{123}:W_F\longrightarrow L[[\rho]]/(\rho^{123}).
\tag{880.9}
$$

其核是

$$
U_F=H^0(3H-F-123P_0),\qquad
\deg(3H-F-123P_0)=272,\quad \dim U_F=146.
\tag{880.10}
$$

所以完整矩阵为 $123\times269$、秩123。实际消费者保存一个真实单位子式、全部123行乘回及规范自由坐标。下一阶函数 $[\rho^{123}](v/\tau^3)$ 在该146维空间不恒零：再减 $P_0$ 后次数271，仍大于252，维数恰少1。选第一个实际该系数为单位的规范基列 $v$，保留其原值而不擅自首一化，定义

$$
\operatorname{div}_{3H}v=F+123P_0+D_\ast,\qquad
\deg D_\ast=272,\qquad P_0\notin D_\ast.
\tag{880.11}
$$

这给具体有效除子源，尚不能单凭一条 $v$ 就把完整 $W_{D_\ast}$ 标为完成。

原 V3 Fourier 基与 normal 基不同。R845 的23组已成690维换基准确给
$F_j^{(3)}/\tau^3=\sum N_{(i,k),j}z^k\beta_i$。本篇只读这些块，先把旧269列应用这个已成 $N$，再取 R872 的原 jets。$82^{10}$ 在旧 S5 解中的公共尺度已经相消；不得再乘 $82^2$、再作实子域转换或给 $a_\ast,v$ 加共同 content。

R872 已有 $273\times418$ 的完整 V2 jet 矩阵。构造 V3 jet 矩阵时，它对应的418列直接复制，只为每个 normal 行增加一个最高 $z$ 次数的列，共272列。所需全尾不超过已有272阶；第一条新截取只需0至123阶，后面共同 cusp 块只需0至251阶。

## 4. 同五纤维的962充分证书给完整418列

记 $B_0=F+123P_0$，次数544。在完整 $U_F$ 中保持已选 $v$，按原规范单位解基作整数 moment-curve 组合 $w_c=\sum_jc^j u_j$。同一 $v$ 的五个乘积只计算一次，后续参数继续复用。

若 $v,w_c$ 的额外共同零是 $Z$，则由逐点 pencil 核及
$\deg(B_0+Z)>252$，

$$
\operatorname{rank}\bigl([vV_3,w_cV_3]\bigr)
=962-\deg Z.
\tag{880.12}
$$

于是使用旧五个完整纤维的新评价矩阵，**实际**达到秩962，就同时给出 $Z=0$、完整像
$H^0(6H-B_0)$，以及这次评价在该像上的单射。若实际小于962，只表示这次截面和纤维的充分证书未通过；不能否定原空间存在。

不需要第6个节点或完整多项式插值。对每个旧节点，原 R845 已保存 $E_c$ 与
$K_c^{-1}E_c$，旧 W、Krylov 逆也都存在。对新的截面 $s=v,w_c$，唯一新乘法是

$$
[s(c),W_cs(c),\ldots,W_c^{271}s(c)]\,K_c^{-1}E_c.
\tag{880.13}
$$

所有旧 $E_c$、$K_c^{-1}E_c$ 和源标签原样复用；这也适用于非半单纤维代数。

当实际秩962时，以新的选行单位子式求全部418个自由关系，核全部
$1360\times418$ 原方程。对 $v r+w_cs=0$ 投影到 $s$，与命题880.1同样逐 DVR 得

$$
\boxed{W_{D_\ast}=H^0(3H-D_\ast),\qquad \dim W_{D_\ast}=418.}
\tag{880.14}
$$

因此本篇不必先做完整 $V_6$ 乘法表、272阶多项式 HNF 或一般 $\Gamma/M_g$。

## 5. 共同 cusp 与252个旧 jets 的完整272行小核

定义真正的有效除子

$$
D_C=C+252P_0,\qquad \deg D_C=272.
\tag{880.15}
$$

R820 已取得原 cusp 理想的准确 HNF；在 $\tau$ 图上的列为

$$
e_j-q_j(z)e_{271}\ (j<271),\qquad P_{20}(z)e_{271},
\quad \deg P_{20}=20,\quad P_{20}\text{首一}.
\tag{880.16}
$$

所以对原 normal 函数 $\sum_i p_i(z)\beta_i$，完整 cusp 条件恰是20个余项坐标

$$
\operatorname{rem}_{P_{20}}
\left(p_{271}(z)+\sum_{i<271}p_i(z)q_i(z)\right)=0.
\tag{880.17}
$$

这是一个满的 $K[z]$-模商表示。归一到 $e_{271}$ 后的右式不必是保乘法的环同态，证明也不需要这个额外断言。它保全部20维有限商，不拆尖点，不取平方自由部分。原两图转移及实际的全20尖点身份继续由 R820 的完整证书绑定。

原 $\tau$ 在全部 cusp 和 $P_0$ 都非零。将 (880.17) 应用于
$V_3/\tau^3$ 的690个原 normal 单项式，并与 $P_0$ 的0至251阶 jets 拼接，得到

$$
Q_C:V_3\longrightarrow K^{20}\oplus K^{252},
\quad \operatorname{shape}Q_C=272\times690,
$$

$$
\boxed{\ker Q_C=H^0(3H-C-252P_0)=W_{D_C},\qquad \dim W_{D_C}=418.}
\tag{880.18}
$$

完整性来自 $C\cap\{P_0\}=\varnothing$ 及真正次数544的目标线丛；其 $H^1$ 为零，故恰有272个独立条件。实际消费者仍保存真实272阶单位子式、全部272行乘回、自由坐标及原准确源矩阵的 solve 定义。如果选定剩余素点的测试退化，就记录实际失败，而不改动原 C、P0 或加入新数学假设。

可直接消费原 R827
`R827-original-two-chart-C-reduction.json.gz` 的
`charts.tau.q_polynomials`、`P_polynomial`，同时保其
`source_R820_indexes`、全部 `original_column_sources` 及原两图转移证书。
该文件已经逐个原有理分母核为 $\ell$-单位；它仍只是该准确 C 的模像，不是另一个 C。
后继准确求值必须继续指回原 R820 有理列，不能从一次模多项式重新定义特征零尖点。

## 6. 明确的主函数把原 Ef 接成三个272度输入

令 $G_D=a_\ast/v$，这是同权原截面的比。由 (880.6)、(880.11)，

$$
\operatorname{div}G_D=D-123P_0-D_\ast,
$$

$$
D-395P_0=(D_\ast-H)+\chi+\operatorname{div}G_D,
\qquad
C-20P_0=(D_C-H)+\chi.
\tag{880.19}
$$

这里没有漏掉不同权的 $\tau$ 因子；$a_\ast,v$ 同在 V3。结合 (880.2)、(880.5)，置

$$
Q_f=\frac{G_D^3}{(u_\chi/\tau^2)^4},
$$

则有**嵌入函数域中的准确除子等式**

$$
\boxed{
E_f-1206P_0
=(D_C-H)+3(D_\ast-H)+4(D_\chi-H)
+\operatorname{div}Q_f.}
\tag{880.20}
$$

采用原 $I_E=\mathcal O(-E)$ 约定，同一式在两图给

$$
I_{E_f}I_{P_0}^{-1206}
=Q_f\,I_{D_C-H}\,I_{D_\ast-H}^{\,3}\,I_{D_\chi-H}^{\,4}.
\tag{880.21}
$$

因此是正乘 $Q_f$。准确函数和其常数不能因只看 Picard 类而删除。

进一步，令 $A_0=(a_\ast/\tau^3)(P_0)$，
$v_{123}=[\rho^{123}](v/\tau^3)$，
$u_{272}=[\rho^{272}](u_\chi/\tau^2)$。实际接受条件使三者为单位，且

$$
Q_f=\frac{A_0^3}{v_{123}^3u_{272}^4}\,
\rho^{-1457}(1+O(\rho)).
\tag{880.22}
$$

这保留了后续原帧所需的准确首项表达式；它不是已经算出的 $t=a^3$ 帧校准。
转换到原 t 时仍须使用 $t(\rho)$ 的原单位，不能把它或上述标量设为1。

对原 $\operatorname{Gal}(L/K)$ 取全部七个**函数域**共轭，$C,P_0,H,D_\chi$ 固定，
由 (880.20) 得

$$
\sum_{k=0}^6E_{\sigma^kf}-8442P_0
=7(D_C-H)+3\sum_{k=0}^6(\sigma^kD_\ast-H)
+28(D_\chi-H)+\operatorname{div}N_{L/K}(Q_f).
\tag{880.23}
$$

该范数作用于整个截面/单位解图，不只是把常数 b 换根。七个模输入尚须逐真实分支取得；
一个已成分支不自动等于七分支全部完成。

## 7. 本篇如何进入原五 Lj 的128/144消费者

R849 的真正输入仍是

$$
\mathscr L_j=
N(I_{E_{g_j}})^{q_j}\,N(I_{E_f})^{-p_j}
=\mathcal O(-Z_j),
$$

$$
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134).
\tag{880.24}
$$

本篇将五项共用的基准 $E_f$ 从 R872§6 的新 $V_6$ 关系求解中移出：
直接消费原1111块，新增269/146/418列和共同 cusp418列即可。
$W_{D_\chi}$ 已成，不重做。主函数 $Q_f$ 和七重范数都随有界类运算继续累积。

剩下的真实工作仍是五个原 $g_j$ 的完整输入及其七共轭，随后按
[R872§§7–8](R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)
作准确乘法/flip，取得
$\operatorname{div}G_j=Z_j+\widetilde D_j-272P_0$。
最后的原128维空间是18个 jet 条件的完整核；权1的400维核去掉原
$\tau,\sigma$ 乘128列后补144列。不能把当前269、146或418任一空间改名为五个原128空间。

R877 已实际完成同一个原 canonical free1186 的单 A 正规 RHS，旧 B 和 S5 逆不重算。
其20个 F69缓存块可供余下同 $\zeta$ 的七个 b 分支直接复用。
原七 A、七 B 共14个输入中，当前原分支的 A/B 已成；其余六个 b 分支各自的 A/B 右端 仍须以各自真实
R824/R787 原 unit-chart 分支定义运输，不把一个模根列表当作已完成 Galois 函数图。
新 R880 不阻塞该并行入口，也不冒用 R879 的 reference $v_0$。

原 R849 的 `eta_degree_zero_fractional_ideal`、原 $\lambda$ 与 $B_{\rm fld}=\lambda b$、
五方向、原 $\eta$ 号、$\beta$、$\kappa$、两点帧、指定 theta 二挠和非 p 项全部保留。
本篇不作 Picard 零判、Hecke 活跃支持判定、连接或高度求值。

## 8. 真实取源、阶段边界和输出字段

首源按真实数学 producer 识别，运输可以使用仍存活的后继 carrier，但数学 tag 不因运输改名。

| 原来源 | 本篇消费的真实对象 | 本篇不重做 |
|---|---|---|
| R845 | 参数1截面、1111秩和原行列、十个乘积、五个 $E_c,K_c^{-1}E_c$、23块 V3 正规转换及索引 | 原 D 基、1111选行、十个旧乘积、V3换基 |
| R872 | 实际点参数、273个normal jet阶段、完整V2 jet矩阵、$\chi$ 的 u/418核/主函数索引 | 点271逆、Hensel递推、固定$\chi$核 |
| R827/R820 | 两图完整C的原q/P模像与准确有理列身份；五个旧cyclic点 | cusp HNF、Krylov逆或W约化 |
| R842/R849 | 原D单位解定义及原五Lj精确父子节点 | 旧2451/415/395核或全局DAG |

R845 主输入使用如下实际名字和字段，不能猜一个不存在的旧 inverse：

- `R839-pole-candidate-000001-five-fiber-rank.json.gz`：
  `selected_original_fiber_rows`、`selected_original_V3_pair_columns`、
  `source_fiber_products`、`actual_rank=1111`；
- `R839-pole-candidate-000001-sections.json.gz`：
  两个 `*_original_V3_coordinates_mod_prime`、原完整 D 基源和准确基列定义；
- `R839-pole-fixed-a-fiber-c-times-V3.json.gz`、
  `R839-pole-candidate-000001-b-fiber-c-times-V3.json.gz`，$c=0,\ldots,4$：
  `product_evaluation_matrix_mod_prime` 及原 fibre/Krylov refs；
- `R839-pole-original-V3-normal-index.json.gz` 的23个 `blocks`：
  `normal_row_mapping`、`normal_coefficients_mod_prime` 和原准确单位解定义。

R872 从最终证书的 `point_jets`、`original_V2_jet_matrix`、
`anchor_u`、`complete_fixed_chi_418_kernel`、
`fixed_chi_divisor_and_principal_function` 沿实际 plain specs 选件。
每个 jet 文件的 `normal_basis_jet_mod_prime`、`z_jet_mod_prime`、
`local_parameter` 和 `exact_characteristic_zero_definition` 原样保存。
不能把当前输出数组的来源改成新 consumer 自产。

建议原子阶段依次为：来源/基序审计；V3缺失272列jets；原a/b的P0单位选择；
旧1111子式269 RHS及全残差；123行完整核和下一阶；
固定v五乘积；逐参数w五乘积及962秩；418完整关系/投影；
共同20+252核；三有界除子和准确主函数源。
每个阶段独立 source-bound，预算或充分测试失败保留已完成块，后继直接续算。
新逆必须保存两边乘回；完整核保存全部原行乘回，而不仅保存选行解。

最终完成标志至少分开：
`original_D_residual_269_space_certified`、
`original_D_standardizing_146_space_certified`、
`complete_Dstar_418_space_certified`、
`complete_common_cusp_418_space_certified`、
`exact_original_Ef_divisor_identity_with_principal_function_certified`。
另将 `five_original_Lj_RR128_computed`、
`five_original_Lj_weight_one_144_complements_computed`、
`original_t_frame_calibration_computed`、
`connection_or_Poincare_height_computed` 保 false。

当前原 R845 run43780953543/sourcea43b6afad1ffdbcb0357eda63b7683df3c5d2c93，
1111秩文件112852 B/SHA
`d27322523df2482417c5a2bf6b6dbf71fd05df98cbc1d33b826f4b2a926e71ad`，
截面113154 B/SHA
`6cedff0d3c732c376570b0f513549507053b28a054496c83dd7bab6dbbac617b`，
V3正规索引112114 B/SHA
`19bc45e50852072815408114d0f4c890fcff971368fb94057a26d58d9cd8639a`。
R872 真证书 SHA
`b2837667ae100ef8c7f27494eb447201e3b6204da553d337d78e9a163d90c0e5`。
这些是已成原源；本篇不存在可填写的新运行号、秩或新核 SHA。

## 来源

- [R845：原D铅笔、八极理想生成元及真实五纤维块](../results/R845-certified-original-D-pencil-and-eight-pole-generators.md)。
- [R872：原P0 jets和固定Picard空间实际完成](../results/R872-certified-original-P0-jets-and-fixed-Picard-spaces.md)；
  [同一有界RR证明](R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)，§§5–8。
- [R838：原完整I2与P0不在D](../results/R838-certified-original-second-derivative-ideal-and-minimal-order3.md)。
- [R849：原函数和五极理想准确DAG](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)；
  [原三minor公式与范数方向](R839-original-global-addition-polar-ideals-and-eta-DAG.md)。
- 原 R820 完整两图 cusp 核、R805 正规基、R827 同素点约化只作已有输入；本篇新增的是
  (880.7)–(880.22) 的具体列核、低权缩减及其有限执行契约。
