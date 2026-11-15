# R820 执行契约：原双图 cusp 理想的有限代数恢复

日期：2026-11-15。状态：**待公开Actions实际运行；没有预填新rank或Hermite系数。**

## 范围与入口

RESULT 为 R820-original-cusp-finite-algebra-and-ideals；
FINAL 为 p41-original-cusp-finite-algebra-ideals-certificate.json。
核心 R820_original_cusp_finite_algebra_ideals.py，
CLI --config --proof --method --retained --output --budget-minutes。
固定python-flint 0.9.0，所有新算术只在本公开仓库Actions。

证明为 R820-original-cusp-finite-algebra-and-two-chart-Hermite-ideals.md。
只计算原约化cusp理想的两个完整canonical列Hermite基。
不消费R815算术，不算一般极理想、$\eta$、主函数或高度。

源读取与原子JSON/gzip工具导入原R811核心，完整SHA绑定；
只复用通用Retained/IO类，不使用其R809目标适配器或任何旧数学阶段。
公开wrapper只导入R815的通用Archive/Producer/IO类，
不会导入flint或数学核心。

## 最小原输入与传输

数学producer只有原R805和R806。

- R805：完整源metadata、S3 index、free-basis stage、pencil stage，
  以及固定273个S3原行：每个正规基元的$j=0$行272个和第1行。
- R806：完整源metadata与polynomial index。
  其真实Q矩阵/primitive/cyclic完成证书用于Q-form来源；
  不读34组大坐标，不重算旧乘法或cyclic秩。

当前传输可由真实R813成功artifact内的原输入bundle提供。
必须检查R813自己的完整manifest/cert/receipt，
其原request中的R805/R806身份与本任务一致，
并按原bundle清单逐成员bytes/SHA流式验证。
只提取直接需要的原R805/R806文件。
传输carrier始终标作R813，不把它冒充原数学producer。

每个S3行同时核原recipe、free basis、weight6、
integer_scale=$82^6$、完整old-coordinate布尔见证与273行的映射。
只读 integer_v_t_coefficients[0]；
没有生成新Fourier系数或重新转换旧40维$\xi$表。
原$q_Y^0$常数在不同同权截面之间使用同一局部frame。

## 有限字段阶段

用原$C_0=2,C_1=X,C_{j+1}=XC_j-C_{j-1}$
及$P=1+\sum_{j=1}^{20}C_j$固定20维实字段。
这只是原坐标算术的字段定义，不是新的torsion多项式任务。

令$N_0,N_z,N_a$为旧273行常数值。
仅一次求$N_0^{-1}$、一次求$N_z^{-1}$；
可用20阶有理乘法矩阵解单位列，
每次均在原字段完整乘回为1。
随后准确形成
$$
e_a=N_a/N_0,\quad\alpha=N_z/N_0,\quad
e_a^\sigma=\alpha^{-\epsilon_a}e_a,\quad
\alpha^{-1}=N_0/N_z.
$$
保原共同$82^6$相消，不再乘任何82幂。
两个20阶作用矩阵分别是乘$\alpha$和$\alpha^{-1}$，
逐列在原字段核对。输出两组$272\times20$准确Q坐标。

## 逆序链与完整kernel

每图按$a=271,\ldots,0$处理。
当前状态只保原$a,k$、当前20维向量、
已成独立stage引用及已成相关stage引用。

消元对象至多20维。
每个新候选相对原已成echelon准确约化，并保原selected向量的表达。
独立时保存真实pivot、归一化向量、在原selected基中的表达、
下一候选$Z$倍及完整乘回。
相关时保存第一次关系、准确20维代回、
原Hermite列的稀疏单项式及原索引。

每个候选先保存不可变完成stage，再原子更新current。
若硬断发生在二者之间，续算仅按该stage更新短状态，
不重新求已经完成的向量或关系。
当前的大部分状态是文件引用，不重复复制整个echelon表。

完成后必须实际有20个独立向量、20阶非零准确minor，
并有全部272条第一次相关关系。
每列保持monic对角、上方零、下方严格小于对应行对角次数；
总对角度数必须实际为20。
证明R820给完整kernel，不能只声明包含或相同支撑。

存储以稀疏column_terms记录：
每项包含原normal row、底变量幂次、准确[num,den]系数。
对$d_a=0$保单位对角列，不丢弃。
每图除272个固定monic项以外，位置数至多5440；
实际非零统计只能由真输出登记。

## 两图认证与完成边界

原字段里准确核$\alpha\alpha^{-1}=1$，
以及全部$\gamma_a(c)=\alpha^{-\epsilon_a}\beta_a(c)$。
两完整kernel因此对应同一原cusp闭点，
不必再运行272阶Laurent overlap解算。
这只适用于由同一个真实有限评价得到的这两个kernel；
不能泛化为任意两组候选格的自动拼接。

最终certificate输出两图stage索引、真实degree数组、
实际rank/minor与全部关系SHA、原字段/来源、总colength20，
并明确：

- original_two_chart_cusp_ideals_computed=true；
- complete_polynomial_kernels_certified=true；
- old_Fourier_or_primitive_results_recomputed=false；
- original_Gamma_or_general_polar_ideal_computed=false；
- actual_eta_principal_function_or_height_computed=false。

一日活跃artifact保直接后继需要的原输入和新短理想。
Git/Release不保存可重算矩阵/证书，只记脚本、参数、run、SHA与实际结论。
完成阶段不重算，预算可同核续接。
