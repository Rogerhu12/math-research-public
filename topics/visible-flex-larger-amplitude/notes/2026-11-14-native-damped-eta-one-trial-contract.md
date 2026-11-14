# 原 sigma 坐标下首次 eta=1 的阻尼方向与原试步合同

作者：ChatGPT（exact_refinement；root选择实际调度）。日期：2026-11-14。

类型：**启发式／数值实验方案**；使用 [R273](../results/R273-complete-native-damped-square-root-chain.md) 已证明的完整链模型。本文没有新数值结果，没有在本地运行因子化、范数、点积、RHS 或 Jacobian。以下拟定的单次参数不是新非线性方程或验收容差。

## 1. 固定对象与拟定参数

若接着尝试 R273 方向，首次明确取 `--eta 1`，使用 actual54 的同一完整 1372 段新原坐标矩阵：

```text
76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999
```

保持同一基态、原 $r$、全部 112 个非零模式、原 cut target $H$、far graph、全部原 $\sigma_n$、868 个新局部块和其余 504 个原块。只改产生方向的算法，不再调用原 RHS、ODE、$J$ 或重新形成另一物理目标。此首次尝试也不改变节点数；同一个数值 $\eta$ 在不同的行数或尺度规范中未必具有同样含义。

令 $W$ 给每个 cut／stage／far 行除对应原 $\sigma$，并取

$$
T_n=\sigma_n I,\qquad \delta=Tz,\qquad A_\sigma=WAT,\qquad \rho=Wr.
$$

每个节点的全部 224 个 $z$ 坐标都罚一次。模型为

$$
f_\eta(z)=\tfrac12\|A_\sigma z+\rho\|_2^2
+\tfrac12\eta^2\|z\|_2^2.
$$

在这个**已有的原求解器尺度**中，$\eta=1$ 把一个单位归一化方向的平方成本设为一个单位归一化方程残差的平方成本。这是公开、可复现的算法规范，不是物理单位、曲率或几何误差的等价声明。数值 1 可在 binary64 精确表示，也不需要另算谱、条件数、局部最坏模或先发一轮调参诊断。

## 2. 选择依据与明确边界

[actual54](2026-11-14-actual54-direct-LD1372-solver-and-exact-readback.md) 原报告给出基态原尺度无穷残差约 `0.0417730782074019881`。同一次未阻尼方向的保存条目包括：新 node519＝旧 node43 的 $\Pi_{112}$ 方向为 `2.0485941339260733e21`，除原 $\sigma$ 后为 `6.812893422912968e36`；new518 的最大幅值方向除原 $\sigma$ 为 `-3.208388273304542e36`。这些是原 Actions 已计算的条目，本文没有再算全局最大值、比例或二范数。

R273 的精确模型以 $z=0$ 作比较，唯一极小点满足

$$
\eta^2\|z_*\|_2^2
\le \|A_\sigma z_*+\rho\|_2^2+\eta^2\|z_*\|_2^2
\le \|\rho\|_2^2.
$$

所以当 $\eta=1$ 时，完整方向的二范数预算由同一完整基态残差的二范数控制。它是同时约束所有节点、模式的全局方向机制，不是看到一个巨大坐标后把该坐标删掉或截断。也没有假设 cut、far 或某个模式可以从模型中省略。

这个精确结论不能直接作为浮点输出的证书。冻结实现先以 longdouble 形成 $J_n\sigma_{n+1}/\sigma_n$ 和 $r_n/\sigma_n$，再转为 f64 系数。它真正做 QR 的是这些**明确保存身份的形成系数**；用其作为精确实系数定义的模型记为 $\widehat f_\eta$。因子化与回代仍是有限精度运算，完整原模型梯度读回也是 longdouble 数值报告，而非严格球界。

因此首次运行需分别报告：形成模型的基能量与候选能量、完整未预条件模型梯度、实际恢复后的原方程 exact 行读回、最终原非线性试步。不能把上述精确不等式的右端替换为一个打印值后声称已经认证候选大小。

此外，$\delta_n=\operatorname{RN}(\sigma_n z_n)$ 的实际 binary64 恢复可能产生普通舍入或深处下溢。保存的 $z$ 和恢复后的 $\delta$ 是两个不同对象；冻结源码分别记录二者，并对实际 $\delta$ 读回完整原方程。不会把 exact 实数乘积的结论自动移到已经舍入的方向。

### 仍可能发生的失败

- 单次 $\eta=1$ 可能使方向过小，实际原无穷范数下降不足；也可能在某些原域条件下仍过大。本文没有预言接受。
- 二次模型下降或完整 $L^2$ 残差下降，都不推出原 $\|\cdot\|_{\sigma,\infty}$ 下降；R273 的明确反例继续适用。
- cut、far 方程完整出现在最小二乘目标中，但不保证候选方向把它们恰好解到零。原 target $H$ 和 far graph 保持不变；不得在回代后私自覆盖 cut／far 方向以隐藏这一差异。
- $\eta$ 是方向模型参数，不进入原最终残差方程，不放宽原 native 容差，且不改变 guard、原十档步长或严格原范数比较。
- 失败的第一次试验不能仅凭“$L^2$ 好看”继续宣称正确，也不能根据缺陷过大在原试步之前添加一个新科学门。应保存完整候选并让原验收给出实际原因。

## 3. 冻结实现及同一次运行已有的诊断

源码为 `computations/exact_20261114_native_damped_chain_qr.py`，42340 B，SHA-256：

```text
9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33
```

底层唯一系统 reader 仍为 `exact_20261114_rawcell0_direct_ld_system.py`，SHA `b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e`。本文未改这两个冻结文件。完整实现与资源合同见[原接口说明](2026-11-14-native-damped-chain-QR-interface.md)。

同一次未来 Actions run 已会保存下列信息，无需先发诊断 job 或设额外准入步骤：

| 记录 | 具体作用与范围 |
|---|---|
| `factor-report.json.gz` | 显式 eta numberRecord、原尺度哈希、longdouble 工作精度、完整节点罚项数、形成下溢计数、全部因子／常数项维度及身份 |
| `formed-stage-inventory.json.gz` | 每个原 $J$、形成 $V$ 与 $\rho$ 的 SHA；读回时逐段再核同一形成字节，没有再求 $J$ |
| `factor-index.json.gz` | 所有 $R_n,S_n,a_n$ 与纯常数向量的 raw descriptor；没有丢掉纯常数能量 |
| `factor-report.solve` | 完整 scaled $z$ 与完整恢复 $\delta$ 原件、1373 次三角回代、恢复下溢／负零记录 |
| `formed_model_diagnostic` | `base_objective`、`objective`、`model_drop`、形成残差二范数与无穷范数、完整未预条件梯度二范数、形成能量与因子能量之差 |
| `original_exact_readback` | 全307552个未缩放原行先精确形成，再除原 $\sigma$；不包含 eta 罚项，也不把此值当作新非线性门 |
| 原 trial 报告 | 对完整577节点限制方向，实际执行原十档步长、原 guards 和原无穷范数判定 |

这里不需要新增一个针对 $\eta=1$ 的局部 toy、谱估计、norm 预筛或调参 gate。若之后确需改变 eta，应以本次上述实际记录与原试步事实为依据，另存明确新参数身份；不要在同一记录中静默换 eta。

## 4. 新原十试步入口的数据合同

新的 trial 入口只验证和消费完成方向，不导入 QR 类来重新因子化，不重新形成 $J$，也不重新估计残差模型。它可以复用同一 `RawCell0DirectLDSystem` 的来源／原数组验证，并逐 SHA 绑定结果和输入。该 reader 只重建保存对象及其既定绑定，不调用 RHS／ODE／$J$。

| 对象 | 冻结输出合同 |
|---|---|
| 完整结果 | `result.json.gz`，schema `complete-native-direct-LD-J1372-damped-square-root-direction-v1` |
| 小摘要 | `summary.json`，schema `native-damped-chain-direction-small-summary-v1` |
| 输入绑定 | `input_binding` descriptor 指向 `input-binding.json.gz`，内容等于唯一完整1372系统的 `binding` |
| 原非 $J$ 件 | 顶层 `original_arrays`，保留 base／r／output／sigma／cut／far／H／target 的完整 descriptor |
| 全方向 | `step_delta`，raw 路径 `large-arrays/complete-original-coordinate-delta.f64le`，shape `[1373,224]` |
| 全 checkpoint | `step_direction_checkpoint` 指向 `step-direction-checkpoint.json.gz`；schema `complete-native-damped-chain-direction-v1` |
| 旧节点限制 | `restricted_old_node_delta`，raw 路径 `large-arrays/complete-old-node-restricted-delta.f64le`，shape `[577,224]` |
| 限制 checkpoint | `restricted_direction_checkpoint` 指向 `restricted-original-node-direction.json.gz`；schema `complete-original-node-restriction-of-damped-chain-direction-v1` |
| 全数组清单 | `array_manifest` 指向 **gzip** `output-array-manifest.json.gz`；schema `complete-native-damped-chain-direction-arrays-v1` |

两份 checkpoint 都含 `source_sha256`、完整 `input_binding`、`M/K/depth/original_depth/step_depth`、完整 `old_to_new`、`delta_float64le_sha256`、所有 `rows` 及各行 `negative_zero_columns`。负零必须按声明恢复，577 节点限制必须逐词等于完整1373节点方向的映射取件。

参数身份由顶层 `eta_cli_text` 与 `eta_binary64` 保存，checkpoint 再保存同一个 `eta_binary64` 和 `model_scope`。形成模型 identity 还绑定 eta 的 binary64 位串、源 SHA、工作精度、原尺度和全部形成系数哈希。**没有**旧带状求解的 `initial_solve`／`lapack_solve_info` 字段，checkpoint 也**没有**旧 `scaling` 字段；薄入口不能把这些旧 producer 字段当成当前对象的必需字段。

完整结构、来源、方向和有限字节的验证不应被省略；但这种验证不能夹带要求某个 L2、gradient 或 exact 线性范数小于阈值的新增科学门。原非线性判断仍消费实际恢复后的全部方向，包括 cut／far 分量，不私自覆盖任何坐标。

本文的 eta 提案、源码与接线合同都是后继准备，没有宣称 R273 方向已生成、已通过原试步或已获得新的真实尾解。
