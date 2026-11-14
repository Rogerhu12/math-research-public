# 完整 H 度量的有预算有限子空间不等式修正接口

日期：2026-11-14。

状态：独立源码已写完，仅作本地 AST 和源码静态核对；**尚未执行任何数值，也未接入工作流**。本接口不修改当前七查询主线，不给任何完整曲面或原 BVP 新接受结论。实际执行只能在本公开仓库的 GitHub Actions。

源码：computations/geometry_20261114_full_metric_inequality_correction.py，41,612 字节，SHA-256：

    d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c

冻结复用的两个源：

- geometry_20261114_full_angle_projection_warm.py：7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152。
- geometry_20261114_full_angle_domain_operator.py：af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7。

## 1. 使用对象与坐标

本接口处理已经构造好的一个固定有限模型：

$$
f(z)=\frac12\|Az+b\|_2^2+\frac{\lambda^2}{2}\|z\|_2^2,
\qquad Bz+c\ge0,\qquad \lambda>0,\quad c_i>0.
$$

全部向量沿用原完整缩放坐标 $z$；原 chart 的 $S$ 已经包含在 $A,B$ 内，本接口不再除一次 $S$。$A$ 必须是同一轮唯一 CompleteLinearization 及原权重产生的整个算子，$b$ 是其配对原加权残差。$B$ 是同一基点、同一参数与原节点 Jacobian 捕获构造的完整选定角域算子。当前七查询实例是 $14336\times236036$，接口不硬编码这个行数。

$C$ 是原完整列预条件量，例如现有调用方的 $\sqrt{\operatorname{columnnorm}^2+\lambda^2}$；它只预条件内迭代，不替换 $H=A^TA+\lambda^2I$，也不把其他全局变量锁死。调用方显式提供 $c$，本接口不选择 reserve 参数 $\theta$，不改任何原 $B$ 行。

数值输入限定为完整、有限的 float64 一维数组。源码保存 $b,C,c,z_0$ 的 shape/dtype/原字节 SHA、$\lambda$、完整维数、domain.model_sha256、全部冻结源身份以及调用方 input_identity。**黑箱 $A$ 与 $b,B$ 确实来自同一固定模型是调用方必须绑定的契约**，此 helper 不能仅凭一个 matvec 对象独立证明它；报告明确保留这一限制。必须给真实 prepared/resume、source、原 A 模型与 B export 清单，不能让任意匿名算子冒充原模型。

## 2. 唯一公开调用

    result = full_metric_inequality_correction(
        A, b, damping, C, domain, c, z0, deadline,
        max_active=32,
        max_h_products=1200,
        max_inner_iterations=64,
        inner_relative_tolerance=1e-8,
        max_dual_sweeps=200,
        input_identity=original_model_identity,
        progress=callback_or_none,
    )

A 提供 shape、matvec、rmatvec；domain 提供 shape、matvec、rmatvec，原完整角算子可直接使用。z0 是本轮真实 LSMR 的完整缩放方向，不是局部坐标投影副本。deadline 必传，为绝对 time.monotonic() 时间。调用方用自己剩余的 Actions 总预算设定它；接口没有隐藏的总秒数默认值，也不擅自延长原工作流预算。

如果 z0 实测不是原完整模型的严格下降射线，返回 usable_direction=False、direction=None 和真实原证据；不编造可用方向。正常返回也是一个待原非线性回溯验证的候选，不是 BVP 接受器。

## 3. 全局基如何构成

第一列保留真实 z0 **逐字节不缩放**，因此存储向量实线性张成空间确实包含实际 z0 与零点，而不是仅包含其理想比例方向。随后最多添加一个原完整 H 的无约束修正向量，以及至多 32 个原不等式行的全局修正向量：

$$
Hx=-A^Tb,\qquad Hv=B^Te_i.
$$

这些式子只用带预算的 PCG 产生候选基。每次 H 动作是原完整 A 和 Aᵀ，预条件为两次除以 C；未收敛向量也可作为迭代基，但不得称为准确逆像。PCG 每八步替换一次原完整残差，并在递归残差想触发停止时、末步以及退出前重读原残差。只有实测 $\|r\|_2\le10^{-8}\|\mathrm{rhs}\|_2$ 才会报告该次线性子问题到达默认算法容差；预条件或递归残差小不替代它。此容差是迭代预算指标，不是新的科学门。

新增基向量作两轮 H 内积正交化，最后重新调用原 A 和 B，保留实际字节。重复方向可由明确记录的 $128\epsilon_{\rm mach}$ 相对基冗余阈值省略；这仅省略算法向量，**相应原约束仍留在工作集，原频率、全局参数和原方程均不删**。基列数上限 34，每列始终含全部全局坐标。

## 4. 有限子空间模型与工作集

对当前实际存储列 V，使用实际 AV 与 V 构造

$$
R=(AV)^T(AV)+\lambda^2V^TV,\qquad
q=V^TA^Tb,\qquad T=B_I V.
$$

原梯度收缩 $V^TA^Tb$ 与 $(AV)^Tb$ 的浮点差异另记；每个组合候选随后重新用完整 A、B 读取，不能拿列组合恒等式代替实际动作。R 由同一三角逐项点积后镜像，按对角缩放作 Cholesky；失败时不加 ridge、不裁特征值，保留失败与原可行射线后备。

只在当前子空间内令

$$
w_0=-R^{-1}q,\qquad d=c_I+Tw_0,\qquad G=TR^{-1}T^T.
$$

若 $R=D L L^TD$，则实际用 $Q=L^{-1}D^{-1}T^T$、$G=Q^TQ$ 构造小 Gram，避免把未收敛的完整 H 逆动作拼成假定正半定的 Schur 矩阵。对

$$
\min_{\mu\ge0}\frac12\mu^TG\mu+d^T\mu
$$

执行有预算的逐坐标更新，再取 $w=w_0+R^{-1}T^T\mu$。每子问题最多 200 sweeps，可因 deadline 或浮点固定点提前结束；报告明确不默认该对偶子问题已经收敛，更不默认原完整 QP 已最优。真零 Gram 行与矛盾的退化存储行分别记录，不用虚构逆或删原约束来绕过。

每次候选都重新检查**全部提供的原 B 行**，从未在工作集中的行按实际 $(-\mathrm{slack})_+/c$ 最大值选择新增行。最多保留 32 行；这不是把其余行丢掉，最终修复和使用候选时仍检查所有行。若已有工作行未解决而没有新的违反行，明确以该状态停止，不把有限 sweep 当 KKT 完成。

## 5. 全模型证据、可行修复与输出

对每个实际证据点 x 与原行非负乘子 μ，完整重新计算

$$
g_x=A^T(Ax+b)+\lambda^2x,\qquad
r=g_x-B^T\mu,\qquad s=Bx+c.
$$

保存原范数、预条件范数、所有 s、完整 r、μ、互补和、原模型 gdot 与实际 f。零乘子 raw z0 证据始终保留，即使后选点的梯度更大也不会用后者覆盖掉前者较好的下界。

按 [R267](../results/R267-two-point-damped-model-posterior-bound.md)，每个非负乘子证据点，不论 x 是否可行，都给出实代数下界

$$
L(x,\mu)=f(x)-\mu^Ts-\frac{\|r\|_2^2}{2\lambda^2}.
$$

报告采用所有已测点 L 的最大值，并完整保留最优下界证据点的 x、μ、r、s、Ax 与梯度。最终可行 y 单独读取 $f(y)-\max L$ 与距离估计。若存储浮点值出现负 gap，只报告该事实，不开根号、不宣布矛盾已获严格证明。可行证据点还单列 [R265](../results/R265-full-angle-linear-inequality-damped-model.md) 的单点 E。**这些实际浮点读数没有外向误差包络，不能冒充经过验证的严格数值证书。**

所有子空间候选用原冻结 radial_feasible 函数对全部原行作径向修复。保留原 z0 上同模型的一维下降射线作为后备；最终调用原冻结 choose_feasible_descent，在后备与最佳实测可行子空间点之间按同一个完整 f 选择，并再核全部行。最终非负乘子只按实际径向/线段系数缩放，随后重算原完整 r；缩放本身不宣称 KKT。

主要返回项：

- direction、multipliers、stationarity_residual、original_slack、original_A_direction。
- raw_evidence、H_refined_center_evidence、best_lower_bound_evidence、best_subspace_feasible_evidence、final_evidence。
- 全局 basis_vectors、actual_A_basis、actual_B_basis。
- inverse_reports、basis_generation_reports、active_history、last_subspace 与总 report。

这些是内存数组与记录，helper 不自动发布或写 Git。消费入口应将大数组按既有 artifact 和分块清单策略保全；发布大小限制不得被误接为数学失败。总报告区分已加入工作行与最后确实求过的工作行，以免预算恰好在新增行之后结束时夸大已解决的问题。

## 6. 明确工作与时间预算

默认预算如下，均是算法资源约束，不是科学接受门。

| 项目 | 默认上限或约定 |
| --- | --- |
| 原活动不等式行 | 32 |
| 全局基列数 | 34 |
| 完整 H 的 PCG 调用 | 33，包括一次无约束修正 |
| 每次 PCG 迭代 | 64 |
| 原残差替换 | 每 8 步及最终必要读数 |
| 完整 H 总动作 | **1200，硬上限，含最终残差重读** |
| 子空间问题数 | 33 |
| 每个小对偶循环 | 200 sweeps |
| 小对偶总 sweeps | 至多 6600 |
| 完整 A 动作 | 至多 1379 |
| 完整 Aᵀ 动作 | 至多 1272 |
| A 与 Aᵀ 合计 | 至多 2651 |
| 完整 B 动作 | 至多 553 |
| 完整 Bᵀ 动作 | 至多 102 |
| 总秒数 | 无隐含默认，调用方必传绝对 deadline |

令 a 为 max_active、h 为 max_h_products。按冻结原选择器中径向修复至多 12 次的有限循环计数，完整顶层动作的先验上限为

$$
\#A\le h+19+5a,\quad
\#A^T\le h+8+2a,\quad
\#B\le73+15a,\quad
\#B^T\le6+3a.
$$

这里计算的是**顶层完整算子动作次数**，不是一次 matvec 内部的浮点运算数。不会再次构建完整 699 节点 Jacobian。报告同时给实际动作计数，不用这些上限冒充耗时预报。

deadline 停止可选 PCG、增基和对偶工作；一次已进入的有限算子、增基步骤或小矩阵操作不能被 Python 时钟中途抢占。选中行的 PCG 返回后会再次检查时钟；若已超时，只保留完成的逆像诊断及待加入行身份，不再把该行或基列加入工作集。末尾原残差、全模型证据、全行修复与选向可以在时间边界后结束，并明确计数；PCG 事先为最终 H 残差读数预留动作，因此这些必要读数仍不越过硬 H 总上限。调用方须为保全和原非线性回溯留时间，不能把这里的 deadline 当整个 job 的强制杀进程时刻。

## 7. 与真正后续动作的边界

本 helper 全局使用 H，可让原局部 C 度量投影未能调整的坐标参与方向选择；但它只探索至多 34 维的有限子空间，并且小对偶可未收敛。这是具体候选生成手段，不是完整 QP 最优性定理或全局收敛承诺。

所选 B 仍仅对应原离散查询和其原 N 个角；其全行线性可行性不证明连续角、不证明其他节点，也不证明真实非线性域。调用方必须照原路径重建完整方向、重算完整原 merit、全部原域和原回溯，再进行原后续求解/FD/尾接口。原科学接受、冻结 metric、全部频率以及真实尾调用规则都不变。

本文件只记录可执行接口与其有限范围。没有实际父场输入，不运行；没有实际 Actions 回执，不报告改善或成功。

