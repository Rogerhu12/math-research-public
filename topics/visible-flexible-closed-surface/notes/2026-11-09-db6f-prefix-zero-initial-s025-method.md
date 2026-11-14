# 原 M15 shooting 的零 shape 初猜

状态：**原算法的独立初猜对照；输入已生成，本文不记作已运行。** 2026-11-09，coupled_prefix。主会话持有原恢复计算；本代理没有启动第二个 solver。

固定输入仍是原 $s=1/4$ 的物理 cut-height 向量，M15/N256/depth12/p8/steps32、原 tol $2\cdot10^{-9}$、原 `.05` guard 和原 RK 均不变。只把待求 shape 状态初始化为零，并允许原方程中的 cut 残差参与 Newton。

## 1. 零态的原残差

在所有节点取 $y_n=(Q_n,\Pi_n)=0$。原 moment 公式给 $P=P_\theta=L=U=0$，因而 $D=S=A=1$，原 root 在第一次评价即以误差 0 返回。shape RHS 为零，任何同一原 RK 网格的 stage shape flow 仍为零，远端 Robin 行也为零。

背景 mean 槽仍有导数 `drdx*w`，所以不能声称完整带 mean 状态的 RHS 全部为零；但 shape 方程不依赖这两个 mean 槽，shooting 残差只取前 $2M$ 个分量。

非零目标 $t=H/(r_{\rm cut}^4)$ 的 cut 残差为 $-t$。原 $\sigma_0=\max_j|t_j|>0$，故原 normalized 最大残差等于

$$
\max_j|t_j|/\sigma_0=1.
$$

这是原方程与源码的零态恒等式。输入文件将 1 明记为**静态预期**；实际 first-iteration 日志尚须由原 solver 确认，不能从生成输入这一步冒充已有计算结果。

## 2. 必须保留的 worker 路径

原 worker 在 warm state 中使用 `prior.cutHeight` 建立 `last.jets.height`。如果把零态 CP 的 `cutHeight` 也填零，则新非零请求除以旧第1项得到非有限 ratio，worker 不设 `initial`，反而回退到原 `linear(target)` 初猜。因此新 CP 的 `cutHeight` 必须保留**真实非零请求目标**，同时明确它不是零态当前实现的物理高度。

新 CP 明记 `UNCONVERGED_ZERO_SHAPE_FIXED_NONZERO_TARGET`；全部 865 行 shape states 及13个 raw-node state 都为零，参数和原 rawNode 指针原样保存。目标 height 逐值核为冻结 affine 目标乘 $(1/4)^j$，$j=1,\ldots,15$。

新请求仍是这个目标，所以原 warm ratio 恰为 1。相同 M/depth/parts 的原 remesh 只复制零；原 `harmonicAmplitudePredictor` 在倍率 1 时也不会改变它。配置中的 `correctInitialBoundary` 是严格 JSON `false`，使原 worker 不再给零态添加 `linear(target)` 边界补偿。接着 `tail.solve` 复制这个显式 `initial` 数组；cut 行仍保留在原 residual 和原 correction 内，没有更换目标或边界验收。

## 3. 可复现输入与有限对照

生成器 `scripts/db6f-prefix-prepare-zero-initial.py` 只使用标准库读取、核 hash 和写输入，不导入或启动任何 solver。生成时核验了此前恢复绑定的全部来源文件。

- `prefix-zero-initial-s025-input.json.gz`：明确未收敛的零态 CP。
- `prefix-zero-initial-s025-config.json`：原配置加上述初始化选择、新记录路径和8轮预算。
- `prefix-zero-initial-s025-launch.json`：完整 argv、cwd、stdout、来源/input hashes。
- `prefix-zero-initial-s025-preparation.json`：生成器、原输入、生成命令、输出 hashes；actual_solver_runs=0。

notes 短名均带 `2026-11-09-db6f-`。计划运行输出 stem 为 `prefix-zero-initial-s025-original-pilot01`，使用未经修改的 `db6f-prefix-tail-trial-run.py` 和原 trial worker。它与仍在运行的非零 warm 恢复输出分开。

独立 pilot 最多8轮原 Newton；这是初猜比较预算，不是放松原成功标准。只有原返回 `converged=True` 且真实 normalized residual 小于 $2\cdot10^{-9}$，才能称该有限目标 DN 已收敛。8轮结束、残差小于1、或比原 warm 更好，都不能替代这一条件。即使 $s=.25$ 成功，也只是 warm，仍须继续至 $s=1$ 并进行原实际 prefix 校正。

零初猜不保证8轮达到容差。原 Newton 第一次全步可以重新产生较大的非线性残差，仍应由未改的十档线搜和原 guard 决定接受。此方案既不替换方向算法，也不把正则化线性系统用于物理 DN 导数；正则化 LS 的实现准备已暂停。
