# R825 执行契约：原对数导数比与三重数消费者

日期：2026-11-15。状态：**待真实上游极理想及导子/函数算术输入；本文件不填写任何不存在的producer。**

## 1. 对象与不可变边界

首scope只处理原index4映射的完整有效极除子
$E=(y_{f_4})_\infty$，理论次数1206；
由原$E=\mathcal B+3D$得理论$\deg D=395$。
395仅为安全预算上界与最终独立比较，不用于生成任何矩阵的对角次数。

推荐RESULT为 R825-original-multiplicity-preimages，
FINAL为 p41-original-multiplicity-preimages-certificate.json。
CLI保 --config --proof --method --module-helper --field-core --retained --output --budget-minutes；
准确字段及完整源码SHA在实现冻结时登记，未取得上游时request必须保持
producer_inputs_pending=true。
不能把R824已证明的齐次生成元接口称为已返回normal极理想。

数学scope为 original_index4_D_by_logarithmic_ratio_preimages。
可在同一源绑定checkpoint中保留已成算子列/前向层/逆步骤；
后续补充尚不存在的I输入必须有独立明确的目标身份，不改已成来源标签。

## 2. 四种真实输入

必须逐原manifest、certificate、source commit、core SHA和stage SHA核：

1. 原I_E两图272维正规坐标完整理想。允许R811已认证完整极前像；
   或R824已完整认证原齐次极点模后产生的准确normal运输。
   必须有原函数身份、原次数1206、原基EPS、完整两图相容。
2. 原R811 A/B regular-multiplier对，原同权5，
   $a=A/\tau^5,b_0=B/\tau^5$；两图保相同$t^5$因子。
3. 原R815真实$M_g,\Gamma$和两图导子。
   第二图底变量导数矩阵是certificate给出的
   sigma_base_variable_derivative，即g的sigma块再乘原scalar $-1$；
   不能把该块不加负号用作$\delta_\sigma t$。
4. R820完整C两图，实际run43721747750、source7890fde180ffabee056de2ce8dd241b189a893a2。
   实际d271=20，其余0；全部原273常数不再参与新算术。

原L模型与$\zeta$坐标严格用同一个字段adapter。
原分量$a+s c$转换为$(a+c)+2c\zeta$，只在入口一次；
原Q导子矩阵嵌入L，不另乘82。
所有矩阵的列都是原输入normal基、行都是原输出normal基。
原$\tau,\sigma$、normal EPS和原n=1必须在四条来源中完全相同。

## 3. 算子列与两图检查

由真实源计算
$$
D_a=\Gamma M_a-M_a\Gamma+M_gM_a',\quad
D_b=\Gamma M_b-M_b\Gamma+M_gM_b',
$$
$$
P=M_aM_b,\qquad Q=D_aM_b-M_aD_b .
$$
这些都是新实际矩阵乘法，不能因表达式已写下便记为已完成。

按原字段多项式进行分块/逐列处理。
矩阵每个完成列或列块先原子保存；同源同核续算只读取已有块。
可以由这些固定源矩阵的组合按需生成后继实际列；
若没有物化完整P/Q，最终摘要必须明确只有哪些列/乘积已完成。
不预先生成无消费者的所有normal基元乘法表。

真输出必须核原weight10和11：
$P_{ij}$次数$\le10+\epsilon_j-\epsilon_i$，
$Q_{ij}$次数$\le11+\epsilon_j-\epsilon_i$。
朴素weighted12的Q最高项是必须实际核零的项，不能预先裁掉。

第二图对源导子本身重新按正确底变量形成Da/Db/P/Q，
随后逐原字段系数认证
$$
P_\sigma=t^{10}D(t)P_\tau(1/t)D(t)^{-1},\quad
Q_\sigma=t^{11}D(t)Q_\tau(1/t)D(t)^{-1}.
$$
两图同向完整验证不依赖一次模点或数值近似。
Q的非零性依据原非常数y和真导子，计算还应拒绝意外的全零输出。

## 4. 前向层与终止

固定$I_0=I_E$。
基础路线以完整当前列基H形成
$[H,\Gamma H+M_gH']$，取完整多项式列像得到下一层。
当前层确是R理想，故不另补全部R乘法闭包。

也可先保存$F_j=\delta^jH_E$：
$I_\ell$的完整生成列就是$[F_0,\ldots,F_\ell]$。
这允许先实际尝试较短的终止Bézout证书；
没有证书时继续推进，不能由模rank或常见简单重数宣称终止。

真实C稀疏列只作底环换基：
对每个F列做
$F_{271}+\sum_{j<271}q_jF_j$除以原P20，要求准确整除。
这不是理想商。
若完整$[C^{-1}F_0,\ldots,C^{-1}F_\ell]X=I$通过，
两图$I_\ell=C$得到真实认证。

若不是逐个层证明此前不等于C，
登记“已认证终止层上界”，并取对应的安全K，
不称其为真实最大重数。
最坏可取原理论395；不能因此实际预跑所有1186层。
完整层相同后绝不再次做该层算术。

只保逆递推真正消费的$I_{3k+1}$原基/生成列和当前必要断点。
任何删除旧大矩阵的步骤须先有已成完整证书、源SHA和明确pruning plan，
保小history；尚未消费的原生成矩阵不得提前删除。

## 5. 逆递推的完整核与投影

从$J_K=R$开始，每一步使用全部原生成列。
当HI、HJ均为272列基时，
$$
B_k=[\,Q,-QH_I,-PH_J\,]
$$
是272×816，完整核秩544。
读取全部核列的前272个坐标，得到272×544投影生成矩阵，
然后取其完整列像，结果为Jk的272列基。

这次投影不是单射；不能只取272个看似独立的核列。
若中间HI保矩形生成列，则使用全部列，
按实际source列数减272得到核秩。
原完整核算法可以复用R811已审的反时间原列算子回放，
但相关维度、截取与后续列像必须按此新shape实现。

每一实际步骤至少保存：

- 固定源P/Q与所用HI/HJ的完整SHA；
- 原未消元B_k，不能用消元后的矩阵代替最终回代源；
- 完整kernel certificate和全部projected列的来源；
- 整个投影列像的完整性见证；
- 原全多项式恒等式$QX=QH_IU+PH_JV$；
- 实际HNF非零对角、原EPS和该图变量。

完成一个逆步骤后才允许归档其小unimodular transcript，
逐成员核SHA后删除已被替代的大工作向量；
最终J基必须保留给两图和后继flip。

## 6. 最终认证与范围声明

两图导子不同但$r_\sigma=t^{-1}r_\tau$，
t在重叠为单位。
消费者仍逐原normal坐标验证最终两向Laurent包含；
不能仅凭两图矩阵大小相同就合并。

实际全局度数使用
$$
\deg\det H_{J,\tau}+\operatorname{ord}_{t=0}\det H_{J,\sigma},
$$
不能加两个整张仿射图余长度。
原理论395只在这里比较，不修改计算得到的对角或次数。

最终true项应包括：
original_index4_effective_D_computed；
all_original_multiplicities_extracted_under_B_plus_3D；
all_complete_module_images_kernels_and_projections_verified；
both_original_normal_charts_preserved；
actual_global_D_degree_matches_395。

false项保：
general_closed_points_factored；
all_normal_basis_multiplication_table_computed；
ambient_trace_pairing_used；
new_CM_Laurent_or_old_cusp_arithmetic_recomputed；
original_eta_rigidification_principal_function_or_height_computed。

I_E、P/Q、完整D及后继flip在真实返回前分别记作未完成，
不能把算法或源接口的存在替换成这些数值。
所有新算术只在公开Actions；只用一日active artifact传递必要checkpoint，
Git/Release不存可重算矩阵/证书。
