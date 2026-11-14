# R270 完整局部凝聚库：实际源码接口

## 1. 实现与范围

独立文件 computations/root_20261114_complete_local_qp_condensation.py 已保全为 Git blob b68321450119b74f7ad892854acb7dc4630b0eef，UTF-8 为40393字节，SHA256为84792d912120058c19c90097c5de7ded6f82ffea8aba61a8ac34c3eb961cac0b。

实现直接依据 [R270](../results/R270-exact-local-support-damped-QP-condensation.md)，只消费已完成且仍打开的冻结 RegularizedBlockQR 因子。原因子源码SHA为596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722。它不重建 J，不调用ODE/边界/新factorize，不修改已有文件，也不关闭借来的factor。

终端仍不可用，本次只做源码和代数静态核。**没有声称 AST、import、时间/内存基准、局部QP收敛或科学执行已经通过。** 所有矩阵运算只允许在本公开仓库 GitHub Actions 中执行；导入模块本身不进行科学计算。

## 2. 公共接口

```python
model = CondensedModel(
    factor,                  # 已 complete 的冻结 RegularizedBlockQR
    original_g,              # 同固定原 A、b 的完整 A.T @ b
    local_indices,           # 原 scaled-z 坐标，升序且全部支持保留
    deadline=candidate_deadline,
    output_directory=artifact_directory,  # 可选，必须是新独立目录
)
```

公共属性：

| 名称 | 定义 |
|---|---|
| local_indices | 原坐标中的完整局部索引，readonly |
| local_gradient | 从完整原g导出的局部仿射梯度，readonly |
| local_center | 保存的局部平方根模型中心，readonly；不冒原H精确中心 |
| report | JSON安全的来源、过程、字节与资源记录 |
| last_local_solve | 最近一次局部逆的有限模型残差诊断 |
| last_recovery | 最近一次实际完整恢复的原H残差、局部偏差和外部梯度记录 |

公共运算：

```python
Hv = model.hessian_action(v)
x = model.solve_local_H(rhs)
z = model.recover(u, label="selected-local-QP-candidate")
model.close()
```

hessian_action及solve_local_H接受(local_size,)向量，也接受(local_size,number_of_rhs)列矩阵；返回同形ndarray。零列multiRHS明确返回空矩阵，不构造虚假有效列。recover只恢复一个最终局部向量，返回完整原scaled-z向量；其余实际诊断在last_recovery。

当前完整支持为物理节点470至482和全部3个p，共4397维。输入索引必须覆盖连续整物理节点，并包含全部p；全部109个自由core必须作为外部变量消去。库不接收B，故“所有完整B行的非零列均在此支持内”由调用者按原domain模型核实；库明确记录该合同，不宣称自行验证了B。

## 3. 完整仿射平方根构造

冻结factor的实际最终平方根数组是diagonal、upper、border、global_diagonal。它的名为R的属性是原collocation右块，不能当作最终平方根。

若因子使用正列缩放C，其定义为

$$
R_C^TR_C=C^{-1}HC^{-1}
$$

的精确算术版本。库先用完整原梯度解

$$
R_C^T h=g/C.
$$

原g不从已求得的近似中心重造，不能因此删掉中心残差。代码通过整个物理链前代，并在最后全局方程中累计每个border转置作用；所有原h分量，包括左外段及pure-global的h_g，都保留。它另读回实际 $(R_CC)^Th-g$ 的完整有限误差，写入数组身份及L2/Linf诊断。

各个物理、相邻和全局列随后按其原C逐列乘回，形成 $\bar R=R_CC$ 的有限算术实现。没有把C非单位情况当成单位情形，也没有在另一套坐标上误用原g或局部B。C折回和QR舍入仍是有限算术，不冒精确实数恒等式。

左侧节点1至469通过R270的条件零平方消元；这些自由度没有被固定为零。完整global根及其仿射列始终保留。右侧483至698执行216个反向front，每个front有2n行、一个待消n列块、剩余物理/完整global/仿射列。一次正交变换作用于所有列，下面n行继续携带。上面n行是被条件最小化的完整平方，不是未经支付而丢掉的纯global余项。

最终中央表示为4506行、4506变量加一仿射列。变量先排109个core，再排4397个局部变量。先对109个core作QR，并保留其正交补中的完整局部与仿射列；再对4397维局部块作QR，得到保存的上三角Rhat和hhat：

$$
\widehat H_{\rm finite}=Rhat^TRhat,\qquad
\widehat g_{\rm finite}=Rhat^Thhat.
$$

这里没有形成正规矩阵Schur减法，也没有形成完整H或24576维dual Gram。局部中心通过 $Rhat\,u=-hhat$ 得到；它只代表保存的有限根模型。

完整二次目标的常数由原f0、完整h的半平方范数和局部hhat的半平方范数组合而成。库保留这些组成量及其身份；调用者做同模型差值时无需先相减两个可能接近的大常数。仿射原g、pure-global以及常数范围均没有因消元消失。

## 4. 局部运算与恢复

局部H作用直接执行Rhat转置及Rhat乘法，局部逆执行两个三角解。solve_local_H会读回保存的局部H残差；这些数只是局部有限模型的诊断，不是原完整H或科学接受门。

恢复遵循R270的完整公式。对请求u，实际形成

$$
r_L=\widehat H_{\rm finite}u+\widehat g_{\rm finite},\qquad
rhs=-g+E_Lr_L.
$$

然后**只调用一次**借来的factor.solve_H(rhs)。该冻结方法保留自己的截止时刻检查、全部原A/AT读回，以及其原算子与冻结重建算子的对照。库没有第二次完整H逆，也没有为了把结果“调准”而覆盖返回向量的local部分。

实际full向量与请求u之间的差单独保存。因外部坐标的rhs逐值就是−g，冻结方法返回的original_residual在外部恰是该次实际原H计算的外部梯度；库直接使用它，不把局部根残差冒作该梯度，也不额外重复一次原A/AT。

last_recovery包含：

- 实际full、请求local、实际local、rhs、original_residual的字节身份；
- local_mismatch_L2/Linf；
- exterior_gradient_L2/Linf；
- 原factor_solve_report，包括原A/AT与额外reference动作账；
- rhs局部加法的有限消去诊断；
- R270外部距离及能量差的浮点后验量；
- 实际恢复后的向量仍需原全B、同f比较和非线性试步的明确范围。

R270的外部后验量适用于**实际恢复后的局部坐标**，不能把它暗中解释为请求u完全相同。在本实现中浮点后验数字不是验证区间。后继约束/merit/原门必须作用于真实full返回值。

## 5. 生命周期、预算和资源

deadline为绝对monotonic时间，实际使用不晚于借来factor.deadline的截止。离散的仿射前代、反向front、core QR、local QR和公共运算在启动前检查时间；已开始的完整局部操作可完成并留记账。recover仍保原factor.solve_H的启动门，不能为了赶恢复而延长或绕过它。

因此局部QP调用者应在候选总预算中先留恢复时间。例如整体candidateDeadline给库与factor，而局部优化循环用更早的candidateDeadline−recoveryReserve。恢复若已不能启动，调用者保留此前原C/完整候选，不把未恢复的u当成全方向。

close只释放本库自己的root、affine与梯度缓存并写状态，**从不调用factor.close**。借来的factor仍由原调用者管理。因子输入、全部四种因子数组、C、完整g和local支持均绑定；构造前后及恢复前检查实际因子字节，防止混用另一个模型。源码检查同样绑定冻结方法，不接受被替换的solve_H。

当前新的主要固定数组为4397平方的局部根154668872B；中央4506×4507工作矩阵约162MB，QR副本/workspace另付。完整借来的factor约1.486GB不在本库重新复制；反向front逐块处理。报告给实际RSS、每部分runtime、原/局部动作次数，不能从这些静态大小预判总运行耗时或最终QP效果。

output_directory启用时会保存原g、完整affine、仿射误差、local根/affine/梯度/中心，以及每次恢复的完整实际数组。大文件均只应保artifact，不能批量塞进Git；status与events只存身份和报告。没有因为单个科学数组大于Git限额就截断矩阵。

## 6. 与局部QP入口的分工

本库只提供同完整平方根模型的凝聚、局部动作和完整恢复。全部24576不等式筛选、活动集/乘子策略、局部可行修复、同f选择、原17trial、原全域及FD由独立入口保持。库没有选theta、barrier、penalty或新scientific gate，也不把有限活动集解叫作全QP最优。

调用者须从同一完整A/b取得g，验证原domain支持，并在回收后对实际完整向量重算全约束和原模型证据。R263/R265/R267的原模型后验仍需实际原量；局部根或它的中心不能替代这些量。本实现不宣称BVP接受、native可解、几何证书或课题完成。
