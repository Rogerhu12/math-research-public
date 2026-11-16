# 原全局函数、五个加法极理想及 η 输入的精确表达式消费者

本执行契约消费 [三 minor 全局证明](R839-original-global-addition-polar-ideals-and-eta-DAG.md)，以及已成的 R840 原单位 chart、R845 八生成元、R806 全局乘法矩阵和 R809 六个清极 Hodge 向量。它输出可逐节点解释的有限精确表达式图。新对象是五个原映射的全局极理想和原比较主函数的表达式，不把原 CM 四响应解释为全局函数，不宣称大坐标已展开或原高度已经求出。

数学结果标识为 `R839-original-global-addition-polar-ideal-DAGs`；最终证书为 `p41-original-global-addition-polar-ideal-DAG-certificate.json`。公开程序以独立真实源码 SHA 运行，不沿用任一上游核心的身份。

## 1. 八组真实来源

| 来源 | 本次必需的原对象 | 不能替换成的对象 |
|---|---|---|
| R787 | 全部 1234 个 `real-power5-row`，原 chart、准确整数 Z、原 selection | 690 行子集、分支向量、已失败的射影候选 |
| R781 | 原 field 文件及 Laurent 000–129 | 另一扭曲、另一实根、重新计算的 Laurent 尾 |
| R786 | 原 power5 cert/index、来源元数据 | 新排序的基或改变的 $82^{10}$ 标度 |
| R806 | 完整 34 组准确 W 坐标、原行映射和已成 cyclic witness | 五个有限纤维值或单一模矩阵 |
| R809 | 1234 个 S5 原短行、原 minor、六个 C 的 12 个准确坐标组 | 尚未完成的 A/B 数值重构或仅模坐标 |
| R840 | 原 $2420\times2420$ 精确单位 chart 表达式及其原来源 | CM 四响应本身 |
| R845 | 已认证的 D 铅笔和两个图上八个原极理想生成元表达式 | 仅 Picard 类或 R842 的模 kernel 数组 |
| R791 | 原 Galois、$\rho_j$、五个 $h_j$ 方向和准确次数比 | 重新归一的 Hom、把 $\kappa$ 或 $v^\dagger v$ 设为 1 |

每组都绑定原 run、source commit、core SHA、full manifest SHA、configuration SHA。每个实际选入文件又绑定 basename、bytes 和 SHA。绝对目录、当前预算和传输缓存不进入数学身份。

R781 的原载体只有其 manifest、certificate、run 和 131 个数学文件；不要求旧生产者从未输出的 child `core-receipt` 或 `public-actions-input`。它由 R787 已认证 carrier 的完整 1372 成员逐 SHA 核验后提取。R786 的原 manifest/index 则明确绑定每条 R787 实行记录中的原 `R786_row_sha256`。

选入的原数据只在一日 Actions artifact 和续算 carrier 中保留。Git 只保存源码、执行契约及小请求，完整矩阵和大系数不入 Git。

## 2. 原全局 y 的常数域表达式

准确使用已经登记的 U.1，而不增加或改变它的归一化。以原 $F\in\operatorname{Mat}_{2580,1234}(\mathbb Z)$、原 $Z\in\operatorname{Mat}_{1234,1214}(\mathbb Z)$ 和

$$
Y_m=-\frac{R_m}{246^3\kappa^{m+1}}
\qquad(0\leq m\leq128)
$$

定义原未清行卷积 $C$。$\kappa$ 直接取原 Laurent 000 的 `kappa`，$R_m$ 取各原阶段的 `coefficients.R`；不是从模 selection 重新构造特征零的 $\kappa$。原第 129 阶仅保留在既有完整来源链中，不多加 $A_{128}$ 条件。

以原行序 $\mathcal J=(J,R[I])$、原 1186 个 pivot 列及自由列 1186 定义

$$
M=[F_A[\mathcal J],-C[\mathcal J,P_S]],\qquad
x=M^{-1}C[\mathcal J,1186].
$$

节点 `unit_matrix_solve` 的准确含义是 $\operatorname{adj}(M)r/\det M$。不运行旧 Dixon，不形成原 1234 或 2420 阶准确逆矩阵，不把旧模逆当作准确逆。原完整核维数 28 与真实单位子式保证此同一选行解满足全部 129 阶原关系。填入其他 27 个自由值 0，令 $b=Zc$，所以 $A=yB$、$B\ne0$。

字段始终是原 $B_{\rm fld}=\lambda b, s^2=-3$。从该整基到原 $b^i,sb^i$ 只作一次明确系数嵌入。

## 3. 按需函数域换基与一个全局导数

原 A、B 本来属于 $V_5$。以实际 S5 选行 $I_5$，定义两个准确解

$$
x_A=S_5[I_5]^{-1}(F_{69}a)[I_5],\qquad
x_B=S_5[I_5]^{-1}(F_{69}Zc)[I_5].
$$

此处的归属来自原 $V_5$ 及完整 S5 基，不是仅凭选行等式猜测。原两边的 $82^{10}$ 标度相同，不再插入一次尺度。由原 S5 `basis_rows` 的 normal index 和 z degree 读成 $A/\tau^5,B/\tau^5$ 的 272 维 normal 多项式向量。

完整 $W=M_w\in\operatorname{Mat}_{272}(\mathbb Q[z])$ 逐原 34 组读取。其系数是原 `coordinate_numerators/column_denominators`，原 S3 标度已经在准确解里消去。保持原输出行、输入列方向，且真实 $w=e_2/\tau$。令

$$
K=(e_0,We_0,\ldots,W^{271}e_0),\qquad
\chi(z,T)=\det(TI-W(z)).
$$

原实际 cyclic witness 证明 $\det K\ne0$，因此 

$$
L(Y)=L(z)[T]/(\chi),\qquad T\longmapsto w.
$$

程序只为 A、B 和六个 C 保存八个 `unit_matrix_solve(K,v)` 节点；其值属于 $L(z)^{272}$，不错误地标作多项式向量。不会物化完整准确 Krylov 逆。

六个 $C_j=\theta U_j/\tau^4$ 的每条原字段坐标准确为

$$
\frac{\text{coordinate numerator}}{\text{column denominator}}
\cdot\text{original target rational scale}.
$$

原 `rational_scale` 仅施一次。直接用 $C_j/C_0=U_j/U_0$，不另外求 $\theta^{-1}$。原 R809 已认证最高 S5 项为零和全部 1380 行；这些标志及原 b 模型逐项核对。

唯一新导数表达式为

$$
\partial_zF=F_z-F_T\frac{\chi_z}{\chi_T}
\quad\text{在 }T=w\text{ 中。}
$$

原函数域特征为 0、$w$ 为 primitive 元，故 $\chi_T(z,w)\ne0$。该表达式不要求尚未完成的 R815 准确 $\Gamma$。$z,w$ 和 normal 基在原 K 曲线上定义，故原 $\sigma\in\operatorname{Gal}(L/K)$ 与此导数交换。

Galois 节点显式绑定 R791 的 `field_sigma_b` 和 `rho_iterates_zero_through_seven`。源编码为 $a(b)+\zeta b_1(b)$，统一字段转换准确使用 $\zeta=(s-1)/2$，不把它误当成 $a+sb_1$。整个表达式都受系数 Galois 作用；$T^j$ 仍是 Galois 加目标缩放，不是 Y 的自同构。

## 4. 五个原极理想及原 η 输入

以原 $u=y_f$、$S=u^2-b$、

$$
v_j=\rho_j^{-3}\sigma^j u,\qquad
r_j=\frac{C_j}{C_0}\frac{v_j^2-b}{u^2-b}
\frac{\partial_zu}{\partial_zv_j}
$$

保存原 $x_{T^jf}/x_f$。原非零 Hom 和 $\Phi_{21}$ 排除所用函数分母为零；不以 c1 的点值代替这些全局证明。

在两个原正规仿射图上，以 R845 的准确八生成元理想 $I=I_{E_f}$ 保存

$$
J_j=I^3(\sigma^jI)^3
\bigl(S(1-r_j)^3,(u+v_j)^3,S(v_j+r_ju)^3\bigr).
$$

这一操作是可逆分式理想的积及三个主分式理想的和，准确等于 $I_{E_{f+T^jf}}$。`ideal_of_cubes` 与理想三次幂相等仅在原光滑曲线的 DVR 层面使用，不伪称一般多元环的生成式恒等。

R845 八生成元是前序已经给出的准确单位解表达式对象。本次保留它的原 sections、原齐次生成式、两图 $t^{11}$ 运输以及所有外部 source refs，不把其内部单位解重新展开，也不把 source 中附带的模核数组代成准确系数。本消费者的组合图以这一已认证的数学叶对象为输入；没有宣称其内部 HNF 或准确矩阵已经物化。

原 $p_j/q_j=(165/67,93/67,100/67,168/67,371/134)$。使用真正七次 Galois Norm 定义

$$
\mathcal L_j=N(J_j)^{q_j}N(I)^{-p_j}=\mathcal O_Y(-Z_j),
\qquad \eta_{h_j}=-[\mathcal L_j]/q_j.
$$

保存 R791 原 $h_j$、$\kappa$、$v^\dagger v$ 和次数归一化。不由这个表达式推断 Picard 类为零。

原割线公式给 $y_{g_j}$。同一图保存原比较主函数

$$
R_j=\frac{N(y_{g_j}^2-b)^{q_j}}{N(y_f^2-b)^{p_j}},\qquad
\mathcal L_j^R=R_j\mathcal L_j^3.
$$

真实三同源极理想用正乘

$$
I_{E_{[1-\zeta^2]g_j}}=(y_{g_j}^2-b)J_j^3.
$$

Norm 对整个原字段表达式作用，因而保留所有原非零常数；本次不以同靶 T 乘积替代 Norm。没有删除 $b^7/Nb$ 因子，也没有新取立方根或除以未知椭圆同源。

## 5. 表达式语言与续算

节点有 `id/ordinal/operation/domain/inputs/data`。`id` 是完整节点体的 canonical JSON SHA；输入必须引用更早的节点。矩阵、字段及理想操作的意义均在上述定义中固定。除法另引用明确非零证明，Galois 节点另引用原自同构定义节点，已认证外部叶保存原文件 SHA。

核心只原子写 `R839-global-polar-*.json.gz`。每个完成阶段有同一完整 configuration 和 `complete=true`。阶段清单仅列本次已成阶段，不列自己。成功 FINAL 必须同时有源审计和完整五映射表达式图；中断只保已成阶段，不把旧 false FINAL 当作完成证书。

公开包装器只标准库处理来源和完整载体，既不导入数学核心，也不再次计算它的数学。resume 先核原完整 manifest、每个恢复成员及同一数学 tag；来源载体含八组的实际选入原字节。除预算、resume 传输和规则读取信息外，源选择及算法身份不允许随续算改变。

成功标志严格区分：

- `global_y_exact_unit_expression_defined=true`；
- `five_original_addition_pole_ideals_as_fractional_DAGs_certified=true`；
- `original_eta_Picard_input_DAGs_defined=true`；
- `original_comparison_function_DAGs_defined=true`；
- `expanded_global_function_coordinates_computed=false`；
- `normal_polynomial_ideal_lattices_materialized=false`；
- `Jacobian_standard_representatives_computed=false`；
- `original_rigidification_and_height_computed=false`；
- `original_eta_classes_proved_zero=false`。

所有新表达式组合和证书只在公开 Actions 实际执行后才能称已完成。本地仅源码、AST、来源字节和字段核验。
