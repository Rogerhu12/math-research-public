# R688：新均值度量的完整粗 Gram、两均值修正与活动面 PCG

2026-11-26，Astra-larger-e4e2a2bf-20261126 / solver。

**状态：本条代数命题已证明，完整小源和入口已完成静态解析及完整驱动派生；尚无本条科学运行或加速结果。** 本条供 [R684](R684-rotational-mean-metric-design-and-frozen-target.md) 的新旋转均值度量设计分支使用。它保持该分支当前实际目标、全自由变量、物理母范数和几何约束，用其完整导数装配当前粗 Gram，再接 [R685](R685-constrained-active-face-preconditioner.md) 的活动面 PCG。

首批不带预条件的 newg v3 有限预算方向继续按其原入口执行。本条不把新设计当作旧固定 g 的细化，也不预报新设计已经满足最终标准。

## 1. 当前物理场与全部粗列的核条件

沿 R684，在每个固定径向观察位置，以物理角 $\phi_j$、轨道重数 $m_j>0$ 和材料密度 $\rho_j>0$ 写旧归一化 Gram 三项

$$
r_j=(e_j,f_j,d_j)^T,
\qquad
\omega_j=\frac{m_j\rho_j}{\sum_lm_l\rho_l}
\tag{1}
$$

用于 material 变体。physical 变体则为 $\omega_j=m_j/\sum_lm_l$。两个变体均保留全部角向波动和交叉行，且交叉均值由全圆准确反射奇偶性为零；不拿正 quarter 域的交叉均值代替它。

令 $B_0$ 是当前已刊 `resume_20261120_physical_subspace_v3.py` 的完整 `free_direction` 映射。其源 SHA 为
`118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8`，其直接返回式以

```python
np.zeros(o.M-o.K)
```

作为原自由坐标的首块，其后才拼入 core acceleration、所有内部三 jet 和 H。原 `unpack(..., tangent=True)` 对固定的前 K 个 core 系数填零，并把上述首块装入其余 core 系数。因此对任意粗系数向量 c，而非只对某些抽样列，

$$
\delta\mathrm{core}(B_0c)=0,
\qquad \delta\rho=0,
\qquad \delta\Theta=0.
\tag{2}
$$

所有 core acceleration 列以及 H 列也满足 (2)。原粗母范数白化只在这些列内作线性组合，因此白化后的 $B_0R$ 仍满足 (2)。这不对原完整自由空间作 core 固定假设；完整 QP 中的自由 core 方向及它们的材料权导数仍由 R684 wrapper 的 J/J* 支付。

新入口绑定上述完整 B、Bᵀ 和 candidate 源，且在专门化 coarse frame 构造之前核对契约。如果实际粗映射没有这个已证明的全列零 core 形式，本条的快速装配不可用；实现明确回退原完整 mean-metric v3 QP，不把未知 $\delta\rho$ 略去。

## 2. 每个径向位置的完整粗导数

记

$$
A=1+\sum_j\omega_j e_j>0,\qquad
C=1+\sum_j\omega_j d_j>0,\qquad S=\sqrt{AC},
$$

$$
\widehat r_j=
\left(\frac{1+e_j}{A}-1,\frac{f_j}{S},
\frac{1+d_j}{C}-1\right)^T.
\tag{3}
$$

为了保留原可分离粗基，令 Y_j 是把径向 velocity/position 通道系数送入物理六方向 $(\delta F_s,\delta F_\phi)$ 的有限角矩阵。其列数为 $2c$，每列只有已刊 R/T/Z 通道中的有限 cos/sin 项。原当前物理一 jet 为 $v_j=F_s$、$w_j=F_\phi$，旧参考标量为 a，则粗列上 $\delta\rho=0$ 给出原三项导数矩阵

$$
D_j=
\begin{pmatrix}
2v_j^T&0\\
w_j^T/(a\rho_j)&v_j^T/(a\rho_j)\\
0&2w_j^T/(a\rho_j)^2
\end{pmatrix},\qquad L_j^{\rm raw}=D_jY_j.
\tag{4}
$$

此处物理 v,w 来自同一 R671 上下文已缓存的完整一 jet，包含其固定 k 的导数；不重新用旧无 k 场构造。缓存和 Y 使用同一 moving R/T/Z 坐标，不再施加第二次坐标旋转。

定义

$$
S_0=\operatorname{diag}(A^{-1},S^{-1},C^{-1}),
\qquad
P_0=\begin{pmatrix}1&0&0\\0&0&1\end{pmatrix},
$$

$$
M=\sum_j\omega_j P_0L_j^{\rm raw}\in\mathbb R^{2\times2c},
$$

$$
U_j=\begin{pmatrix}
(1+\widehat e_j)/A&0\\
\widehat f_j/(2A)&\widehat f_j/(2C)\\
0&(1+\widehat d_j)/C
\end{pmatrix}.
\tag{5}
$$

**命题 1。** 新均值残差关于全部粗通道的准确导数是

$$
J_j^{\rm mean}=S_0L_j^{\rm raw}-U_jM.
\tag{6}
$$

**证明。** (2) 使 (1) 两个变体的所有 $\omega_j$ 在粗方向上均无变化。所以 $\delta A=\sum_j\omega_j\delta e_j$、$\delta C=\sum_j\omega_j\delta d_j$，即两分量向量 $M\delta c$。对 (3) 分别求导得

$$
\delta\widehat e_j=\frac{\delta e_j}{A}
-\frac{1+\widehat e_j}{A}\delta A,
$$

$$
\delta\widehat f_j=\frac{\delta f_j}{S}
-\frac{\widehat f_j}{2A}\delta A
-\frac{\widehat f_j}{2C}\delta C,
$$

$$
\delta\widehat d_j=\frac{\delta d_j}{C}
-\frac{1+\widehat d_j}{C}\delta C.
$$

代入原粗导数 $\delta r_j=L_j^{\rm raw}\delta c$，得到 (6)。证毕。

这里删去的是已证明为零的粗方向材料权导数，没有删去两均值的导数。把 $S_0L_j^{\rm raw}$ 单独当新目标 Jacobian 是错误的。

## 3. 新目标粗 Gram 的准确两均值展开

令 $H_j$ 为 [R664](R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md) 在**当前新残差** $\widehat r_j$、当前实际 $(p,\epsilon,\sigma)$ 处的原三项正残差 Hessian 块，未含共同外因子。不得用旧目标 $r_j$ 的块替代它。

定义

$$
K_{00}=\sum_jm_j(S_0L_j^{\rm raw})^TH_j(S_0L_j^{\rm raw}),
$$

$$
K_{0U}=\sum_jm_j(S_0L_j^{\rm raw})^TH_jU_j,
\qquad
K_{UU}=\sum_jm_jU_j^TH_jU_j.
\tag{7}
$$

**命题 2。** 完整新粗通道 Gram 为

$$
\boxed{
K_{\rm mean}=K_{00}-K_{0U}M-M^TK_{0U}^T+M^TK_{UU}M
=\sum_jm_j(J_j^{\rm mean})^TH_jJ_j^{\rm mean}.}
\tag{8}
$$

因此在准确实数代数中 $K_{\rm mean}\succeq0$。修正 $U_jM$ 的导数秩至多2；Gram 的有符号总差一般只能说秩至多4，不能误称它必为秩2。

**证明。** 在右端逐项代入 (6)，分配矩阵乘法，分别汇集局部项、两个转置交叉项和均值平方项，恰得左端 (8)。每个 $H_j$ 正定且 $m_j>0$，故对任意 c，右端二次型是 $\sum_jm_j\|H_j^{1/2}J_j^{\rm mean}c\|^2\ge0$。有符号差的像包含于 $\operatorname{ran}K_{0U}+\operatorname{ran}M^T$，后者维数至多4，证明最后的秩上界。证毕。

这允许目标随场共变产生新的零方向；没有因为点块正定就声称新 Jacobian 单射。完整 QP 的正阻尼仍负责它们。

## 4. 完整观察角与径向基的无遗漏装配

沿 [R681](R681-current-J-coarse-frame-preconditioning.md) 的角矩思想，$K_{00}$ 由六方向张量的21个对称分量和有限通道乘积的 cos/sin 恒等式装配。当前物理场、当前 $H_j$ 和它们乘积不假定带限；全部实际角点及正轨道重数都进入求和，有限的只是测试粗通道的角表达。

$M$ 和 $K_{0U}$ 只需六方向对两个输出的**一次角矩**；$K_{UU}$ 是完整角点的 $2\times2$ 正权求和。实现的 `contract_linear` 与二次矩使用同一 velocity/position 通道顺序。其 tests 已乘 $m_j$，故计算 $M$ 时另乘 $\omega_j/m_j$，恰恢复一次 $\omega_j$，不重复 orbit、不丢 material 的 $\rho$。

每个径向 stage 再把其真实 Hermite position/velocity 通道系数代入 (8)，包括 H 列的实际解析 h/h′；固定 k′ 留在当前 v,w。最后乘原正径向权求和，再按当前目标共同系数

$$
\gamma=\frac{k}{\sigma^2 C_0},\qquad
C_0=\left(\sum_s w_s\right)\left(\sum_jm_j\right),
$$

以及原同母范数白化 R 做合同变换，得到

$$
G_c=R^T\left[\gamma\sum_s w_s\,
B_s^TK_{{\rm mean},s}B_s\right]R
=(A_{\rm mean,coarse})^TA_{\rm mean,coarse}.
\tag{9}
$$

$B_s$ 在此仅指 stage 的原径向系数选择/组合，不是另一个物理映射。白化前后都不改原粗列、完整变量或母范数。

以上公式只读取已有完整 cache、R684 当前 mean state、R664 当前块和原 coarse 数组。它无需重新评价物理场，也无需逐粗列调用完整 J/J*。这是一项代数和源码结构说明；实际额外调用次数只有在新入口的真实运行返回后才据 wrapper/base 两级计数填写，不由静态解析预报为已测0，更不据此宣称已加速。

## 5. 浮点相消、正阻尼和明确回退

式 (8) 在纯均值或 target 共变方向可能发生强相消。实现记录各 stage 的 $K_{00}$、交叉项、恢复式和最终矩阵的最大绝对元素、相消尺度比、raw skew，以及最终 raw coarse 对角最小值和负对角数。它只作明确的对称化，不剪负特征值，不加隐含 jitter，不把 $K_{00}$ 当作新目标的 Gram。

实际小系统仍由原 CoarseFrame 使用同一正阻尼、同一母范数和当前 $G_c$ 构造。如果 Cholesky 或有限算术失败，新入口在开始 PCG 之前明确选择已刊完整 mean-metric v3 求解器。若全列零 core 契约不能成立，同样选择这条完整原 QP 路径；不会因少付材料权链继续快算。外部内存终止没有返回值，不能写成成功回退。

如果成功形成小 SPD 系统，则原 R681 的全空间 SPD 应用保持，R685 在每个实际活动面上采用其约束逆；当前面改变/释放的缓存同步和数值失败语义仍由 v5 支付。若在 PCG 中途应用失败，返回其真实有限预算状态，不悄悄换预条件器或重试同一个科学方向。

完整 A 始终是当前 MeanMetricOperator 的 J/J*，没有用粗 Gram 替代真正 Hessian 乘积。原二次目标、几何工作行、零点可行检查、真实新目标回溯和永久位置记忆不变。是否更快或得到更好候选只能据本条实际新父报告判断。

## 6. 完整源、原依赖与入口

三个新小源放在 `scripts/resume_20261126/`：

| 文件 | SHA-256 |
|---|---|
| `mean_metric_coarse_moments.py` | `9e7ca6ba0cf3821ab8498226354d8422c2cfacee1ef07dafb8fc5868968fb9e3` |
| `derive_mean_metric_face_pcg.py` | `b57ab303682f708c6d205cf0d527df2ec16aa2cfa1762a59070599abcade6d75` |
| `launch_mean_metric_face_pcg.py` | `5d0801c363def30b1a65c331363e5fc6a28a7de87e4354341e8d0566424640f4` |

完整派生保留 R684 已排 v3/exact-position 驱动 SHA `2d44a097e614f917fa133b1042e0fc7c6cdcb32a10b72d1bc2ac6362d54a94c3` 的全 body，只改7个明确位置：新增参数、当前源加载、报告、方向记录、QP调用、可选统计及目标字段选择。原 launcher SHA `e88c426370fd4fafa9ac6aba445a5a4483fbf2321258cffb68fc5f17e7220cd4` 继续提供完整物理 argv 和父 report/历史 manifest 的精确地点 union。父报告必须自然完成，其 final bundle 与 carrier SHA 必须吻合；pending grid 在实际 carrier 坐标中解析，不合并相近地点。

R685 v5 SHA `76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8`、原 R681 frame、原 R664 block、原 v3 fallback 和 R684 mean wrapper 均在新入口明确绑定。完整派生的 driver SHA 与 AST SHA 在本次计划及实际报告中记录；可由 `bind_report` 重建整个 body 比较。

示例（各变量必须指向该 runner 的真实新父，不预设旧数据 SHA）：

```bash
python "$topic/scripts/resume_20261126/launch_mean_metric_face_pcg.py" \
  --repo "$repo" --work "$work" --outdir "$work/mean-face-PCG-next" \
  --bundle "$actual_parent/final.npz" --parent-report "$actual_parent/report.json" \
  --carrier "$actual_carrier" --node-report "$actual_node_report" \
  --scalar-input "$actual_scalar_input" --manifest "$actual_history_manifest" \
  --averaging material --eta-start-node 885 --lambda-value 1 \
  --damping "$explicit_current_design_mu" --directions 2 --maxiter 64
```

`--averaging` 必须与所声明目标一致；若主动另选目标，初始 Phi 重新读取，不能与前阶段目标相减。这里的 μ 是当前新设计单位下明确选择的值，不能默默从旧 p8 固定目标继承。

可选 `--centered-loss-source "$topic/scripts/resume_20261126/centered_spectral_statistics.py"` 绑定 [R687](R687-centered-spectral-loss-and-sharp-zero-limit-bound.md) 的 helper SHA `5e5798e3fd46535ef91db5171c885701caf23f3a17a47f28d4dad9e557ce2a01`。指定时，原 `phi_normalized` 字段保留，真实回溯明确选择 `centered_phi_normalized`；同一数学目标仅减固定常数，原梯度、Hessian、μ 和绝对停止阈值单位不变。未指定时仍选原 Phi。R687 的近零归一化字段只作诊断，不进入本条优化。

`--print-command` 只构造 argv；`--prepare-source-only` 只派生/编译完整源，二者不打开科学数组或执行求解。当前已完成纯 AST/compile 和 argv 读取，没有新增 fixture、科学方向或独立重跑。最终完成标准仍需实际下降、最终 g 冻结、同 g 精化和全部连续几何/幅度证明。
