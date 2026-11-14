# 固定原方程的 DN 成本改进：最小计划

2026-11-09，`/root/coupled_prefix`。状态：**后续数值方法计划，未实施到正在运行的 M16，也未声称已提速。** 当前优先级仍是紧容差 M14 的实际因果结果和 M16 真联解。

## 1. 已定位的成本

冻结 `scripts/db6f-prefix-tail-shared-core.mjs` 中，每一次 Newton `evaluate(...,true)` 都对所有 shooting stages 重新算原 RK 流及其完整变分矩阵。`correction` 利用这些块做原 Schur/稳定图消元；line search 的 `evaluate(...,false)` 仍逐段计算原非线性流。

本稿源码核查绑定：shared-core SHA256 `95cd3c52b16f5c1605c52c9d67125cd914eb66370524fe1c22059c382888df39`；coupled runner `37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a`；shared-client `a3684dae89d45f1df99fda4351e7f24c2984b701724a942754fe40a10bd6edd0`。

M14/M16 采用高物理深度、每原段八个 shooting 小段；深层虽高度接近背景，当前代码也每轮重建它们的完整 Jacobian。需要量测的是“矩阵重建”成本，不是假定深层残差可忽略。共享 engine 已经降低内存，继续增并发不是首选。

## 2. 最小 modified Newton 备选

记第 n 个 stage 的原数值流为 $\Phi_n(z_{n+1})$，匹配残差为

$$
R_n(z)=\Phi_n(z_{n+1})-z_n.
$$

只允许以旧的深层 $J_n$ 代替本轮精确重算的 $D\Phi_n$ 来构造搜索方向；每轮 $R_n$ 必须仍由原 RK、原角向 root 和原 D/S/A guard 计算。raw0 的 Jacobian 每轮照常更新。首轮全量算矩阵，随后可暂存 rawCell≥1 的矩阵；这只是待试默认分界，须以一次已完成 M14 的对照决定。

原有线搜索仍用新 trial 的**真实原残差**，不可用线性模型预测值接收。若没有可接受步、出现异常条件数或残差下降不佳，立即恢复全量矩阵刷新后重试；不得通过改 guard、g、RK 步数或尾条件弥补失败。

任何最终“converged”响应必须再作一次全量原流/Jacobian 评估，用它检查原残差并提供真正的 DN Jacobian；最终 source audit 也照常执行。混用旧矩阵期间不得把旧 minA/minD 标为当前全域最小值。RK root 的离散 guard 仍在每个原调用上执行；这仍不是连续正性证书。

这类方法不会改变被检验的有限方程及固定物理 g，但不能保证更少迭代或必然收敛。节省多少、是否损害阻尼，必须实测。

## 3. 最小对照与成本账本

不另建庞大测试链。只使用已完成的 M14 数据作一次非平凡小步对照：

1. 固定同一个已存状态和目标高度变动，得到首个全量原评估/线性化。
2. 在一轮后分别用全量新 Jacobian 与“raw0 新、深层旧”方向计算候选；两条路线用同一个原残差与 guard 决定步长。
3. 记录真实残差、接受步长、失败/刷新次数、原流调用数、变分流调用数及墙钟时间。不能只计 Jacobian 调用减少而忽略额外回溯成本。
4. 对最终候选重算完整原残差/Jacobian。未通过则只保留失败记录，不替换生产求解器。

方法文件必须另命名，冻结旧源码；未来可恢复的每步 state 检查点选项应启用。当前未创建这一求解器，也未启动新的 BVP/DN 对照任务。

## 4. 一个更直接、无需近似 Jacobian 的工作流节省

另一个已由源码确认的重复计算是：当前 coupled runner 的首次 warmup 调用为 `jacobian=False,audit=True`。随后 outer solver 对完全相同的 H 请求 `jacobian=True`，客户端因第一响应缺少 Jacobian 必须再调用 worker；worker又完整评估一遍所有变分流。实际上首次 Newton 的最终轮已经算过这些变分矩阵，只是该次请求没有保留/使用它们。

后续可优先试以下**等价工作流**之一：

- 有可靠 warm checkpoint 时，显式给空的 `--warmup-scales`，直接由 outer solver 的首个 `jacobian=True` 原求解开始；最终 seam audit 仍必须执行。
- 或把 warmup 请求改为 `jacobian=True`，保留所算 DN 导数，使相同 H 的下一请求可使用现有精确输入缓存。若省略 warmup audit，响应必须清楚标为未审 warm，并在最终补全原 audit。

这不改变一次原求解的方程、Jacobian 或接受准则；它只避免相同输入的重复工作。具体命令必须存入 reproduction，不能让旧脚本的历史哈希指向新内容。当前正在运行的 M16 使用原工作流，不能追溯声称已应用此节优化。
