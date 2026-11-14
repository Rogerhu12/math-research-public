# 同一尾方程的可选两线程求值及小高度恢复入口

2026-11-10，Astra-visible-flex-78718bd0，numerical_recovery。

状态：下面的段独立性与有序归并是完整的算法恒等说明；四段结果是实际数值证据。
尚未用这个入口求新的 DN 或 BVP，不把局部加速当全尾速度或新图成功。
活动 fast07/session67954 的源、进程、目标、容差均未修改。
根 README §13 下没有冻结、独审或启动核验前置。

## 1. 实际实现与接口

新入口 `scripts/78718-run-prefix-parallel.py` 派生自已保存的
`78718-run-prefix-small-height.py`，增加显式 `--tail-stage-workers 0|2`，默认 0。
选 2 时目前沿已使用的 `fourier-root`、`geometric-centered`、`original` 根精度路线；
选择仅影响有限射击段的执行顺序。small-height 规则沿用原文件：从自身真实成功状态出发，
相对高度变化不超过 `.01` 时先试完整新目标，真实失败仍按原控制器二分。
大高度变化仍从剩余路程的 `1/8` 开始；最终原高度/BC/残差门不变。

新文件分工：

| 文件（均在 scripts） | 改动范围 |
|---|---|
| `78718-tail-parallel-stage-pool.mjs` | 私有两 Worker、精确 profile 点值转移、共享输入/输出、动态领取、有序结果与关闭 |
| `78718-tail-parallel-stage-core.mjs` | 原 `evaluate` 可调用一个批量段供应器；原残差、范数、Riccati、接受循环保留 |
| `78718-tail-parallel-stage-split.mjs` | 原 split factory 改指上面的新 core |
| `78718-prefix-tail-parallel-stage-worker.mjs` | 每次请求创建两线程；同原 `dn.solve`；成功或失败响应前 await 线程退出 |
| `78718-prefix-tail-parallel-client.py` | 显式选择、真实 ready 标签、实际新依赖来源 |
| `78718-tail-parallel-continuation.py` | 原小高度协调器改指新 client，原物理参数/请求检查保留 |
| `78718-run-prefix-parallel.py` | 新 CLI、实际配置/来源/线程策略及 inner 快照记录 |

完整文本改动在 `2026-11-10-78718-numerical-stage-parallel-route-diff.json`；
它是方便理解的差异记录，不是额外数学验收门。
本次未给几何切线预测另加选项，仍使用原 R92 predictor。

pool 的 `createStagePool(...)` 是异步启动；`evaluate(inputs,withJac)` 保持同步，
所以原同步 Newton/Riccati 控制无需重写。`serialStageFlow` 是原 `cellFlow` 的相同运算。
输入按原 stage 序号递增；每个输出复制为自己的 Float64Array，后续请求不能改写
原成功包留在内存中的线性化流 Jacobian。`close()` 等待线程退出，之后不再保留共享缓冲引用。
这不声称操作系统立即收回所有已分配页；实际每次 pool 的 heap 上限、缓冲字节、关闭时间均入 trace。

## 2. 为什么没有改变有限射击方程

令 $K=2W$，$y_n\in\mathbb R^K$ 是第 $n$ 个射击节点，固定几何段为 $c_n$。
原代码对每一段先把 $y_{n+1}$ 拷进 $K+2$ 维状态，两个均值高度坐标置零，
然后按该段自己的 profile/固定 RK 网格积分。记这个有限算法为 $\Phi_n$。
出段动量按原 `portRatio` 归一得到 $P_n\Phi_n(y_{n+1})$。
原残差正是

$$R_n(y)=P_n\Phi_n(y_{n+1})-y_n.$$

因此给定整组输入 $y$ 后，不同 $\Phi_n$ 没有输入依赖。
实际选择的 root/RK engine 只依赖自己的状态、profile 和浮点坐标；每次 root 的起始向量
由当前状态决定，流函数没有把上一个 stage 的隐式根传来当 warm。
engine 的累计 `statistics` 不参与残差或分支决定；profile 的缓存也只按固定几何/坐标取值。
并行只使这些独立调用交错，未改变段内的 root、RK 或变分循环。

原 finite Jacobian 按同一段内 RK 变分算法形成，仍只依赖 $y_{n+1}$。
新 core 按原 $n=0,1,\ldots$ 次序读取每个结果，然后执行原来的逐分量减法、
scales 归一、max/min 和 witness 比较，末端 Robin 与 Dirichlet 残差亦原样。
特别均值高度的总和仍是原有序 `reduce`，不是并行树求和；相同大小的 witness 并列处理亦不变。
随后同一组局部 Jacobian 被原串行 Riccati 消元及原十步回溯使用。
于是对每个给定输入，有限方程、线性化、边界条件、数值终止谓词均相同。

此处“相同”不引入新的数值舍入公式：profile 本身在主线程以原函数求值，
子线程收到的是这些 binary64 值；子线程运行相同的 engine/RK 源。
四段实测还具体确认全部输出字节相同。并不把一次实测升级为任意硬件/编译器的普遍逐位定理。

### 原 profile 的确切有限调用集合

state-only 原循环用 `x=k/steps,h=1/steps`，如有 cusp 则使用原
`splitIntegrationInterval(x,x+h,cuts)`，对每个实际子步需要
$x,x+h/2,x+h$。无额外切分时保原 $h$，不先做端点相减重造它。
full-J 原循环若有 cuts 用原 `integrationGrid`；否则用原 `x=k*(1/steps)`，
仍枚举同三个 RK 调用坐标。因此两种浮点表达式即便不逐位一致也都被保留。

新 pool 取这两个**实际浮点集合的并集**，逐点调用原 profile 并保存其所有数值字段及属性顺序。
子线程用 exact Map key 找回同一对象字段，保原 `integrationBreakpoints`；
它不采样拟合、不内插、不重新积分背景、不以近邻坐标替换缺点。
未知坐标会产生明确的 infrastructure error，不会用不同的物理值继续。
所以这个转移没有改变固定 $g$ 或 RK 离散。

## 3. 失败与生命周期

两线程只按递增序号领取尚未派发的 stage。
领取与发布失败共用同一个原子锁：一旦某个 stage $j$ 报错，不能再领取 $n\ge j$。
在此前已领取的更高 stage 可能仍完成；它们不影响结果。
由于所有 $n<j$ 在领取 $j$ 之前已经派发，等待两线程完成后能取所有失败的最小序号。
新 core 在原序循环中先遇到这个最小失败，并赋回原 `tailStage/rawCell/rawSegment`。
这保留原串行评价的最小失败段语义，而不要求失败时恰好执行相同总次数的工作。
统计明确记录实际已执行的并行工作，可能包含已在途的高段。

每个 DN 请求创建一个 pool，在该请求的 Newton/回溯中重用；原 warm/retraction/Riccati
仍在主线程。无论 `dn.solve` 返回或抛错，`finally` 都 await 两个线程退出，
然后才发布完整响应，避免后续 prefix BVP 留着两个额外 heap。
数学分支异常仍进原控制；profile 转移/线程基础设施异常明确标为 infrastructure，
不冒称某个数学分支不存在。没有以线程成功取代原 DN 收敛。

## 4. 唯一实际四段比较

输入是已真实收敛的中间响应 call8（原高度的 $93/128$），不是最终原高度：
`2026-11-10-78718-numerical-m15-w22-fast-07_tail_0008.json.gz`，
764025 B，SHA256 `d539302dcf0d61fb48c20cd2f91a1f1680a2381addd7e1869355368e16fc8d0e`。
只取原 stage `0,12,74,1440`，W22/N512/P16/S16，保原 cusp/port。

执行命令是在本题目录：

```bash
node scripts/78718-tail-call8-stage-pool-benchmark.mjs \
  --packet notes/2026-11-10-78718-numerical-m15-w22-fast-07_tail_0008.json.gz \
  --out notes/2026-11-10-78718-numerical-stage-pool-benchmark-01.json
```

真实启动 `090c71/session10542`，最终 `cf9688` 自然 exit 0，总 9.789 秒。
背景 factory/数值分段的单次准备 6.626 秒，未构造 stable graph。
pool 启动含两线程 329.264 ms；关闭实际 39.623 ms。

| 分支 | 四段串行 ms | 四段并行 ms | 串/并比 | 全状态/mean/J/minA/minD |
|---|---:|---:|---:|---|
| state-only | 814.631 | 415.695 | 1.960 | 逐位相同（J 不请求） |
| full-J | 846.222 | 673.456 | 1.257 | 逐位相同 |

报告 20337 B，SHA256 `8f81c82e81186fc3f82e35ac4785884d7e81f77ef86da34fee2dcfb2f5835db2`。
`...stage-pool-benchmark-01-observed-exit.json` 保存真实工具出口与新 route 源身份。
本次只有 16 次小段 flow（每种分支各 4 串行+4并行），0 新 DN、0 BVP、0 stable graph。
没有重复整个尾部；没有测全尾加速、真实并行 Newton 或 native OOM 恢复。
source identities 前后一致。

### 资源范围

机器只读实际见 9 个可用逻辑 CPU；这不保证另一工具 session 的调度配额。
四段实测每 worker heap 上限 318767104 B，显式限制为 old 256 MiB/young 32 MiB/stack 4 MiB。
完整 1728 段的共享输入/输出/J/scalars 28028272 B（约 26.73 MiB）；另有 engine/table/J 输出副本。
原 Node1536 MiB 与 DATA6 GiB 设置保留，实际完整峰值尚未测。
profile table 只存数值背景，可在每次请求前复用原背景缓存；它不是研究解或新积分。
这点局部速度收益支持留作显式选择，不能预言完整求解耗时同比下降。

## 5. 从真实 call9 恢复的具体命令（尚未执行）

仅在 root 决定停止当前主进程且确认真实工具出口后，在 repo 根运行。
该 stem 在准备时不存在；不得复用后续已经写过的目录。

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-prefix-parallel.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier --tail-jacobian fourier-root \
  --tail-predictor tangent --tail-trial geometric-centered --tail-root-precision original \
  --tail-stage-workers 2 --direct-relative-limit 0.01 \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-height-scale 1 --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-07_tail_0009.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-08
```

不传 `--tail-initial-checkpoint` 或 `--tail-cold-start`，所以 worker 自动以自己的已知真包作 warm。
same-grid/same-height 分支逐值拷贝其 states，不做 raw 回投影或重复缩幅。
首 bootstrap **仍实际重新求值/求解** call9 的 $25h/32$，不把保存的成功标签改成新运行成功。
最终目标仍由同一个原 prefix warm 的实际 cut 数据计算，W22 seed 仅供真实尾物理参数、
已知起点和初猜，不替代 M15 前缀目标。
若最终目标恰是原 $h$，从 $25h/32$ 走剩余路程的 $1/8$，第一新目标是 $207h/256$。
实际请求向量/hash/连续参数由新控制 trace 记录，不能只凭这个比例推定未来请求成功。

真实首 inner 到来时可以另 stem 使用其 physical-s 快照，并显式给对应实际成功尾包，
沿同一入口重新计算目标；snapshot 的 outer UNSOLVED 标签保留。
无论如何，原 physical BC、2e−9 求解门、自己的完整末尾、共同 g、whole metric/reach/
闭合/全时与网格要求都不因并行或小高度调度而改变。

后续几何切线 warm 若另有实际证据，可另行选择；本次命令没有把它预先并入。

## 6. 随后补入的硬退出清理（没有重跑数学段）

root 读源指出：`evaluate` 的同步 `Atomics.wait` 会阻塞主线程事件循环，
Worker 的 native OOM/exit 若没有走 JS catch，普通 `error/exit` 回调不能及时运行。
原首次四段版本在这种异常下会等不到 done。这是具体基础设施风险，不是数学分支结论。

现同名 pool 加共享 progress：每个 stage 领取及完成均递增。
**连续 120000 ms 没有任何共享进度**就抛带
`TAIL_STAGE_POOL_INFRASTRUCTURE` 的错误；启动也保同样无进度上限。
段继续被领取/完成时计时重置，不限制整个请求总时间、不放宽残差或改 root。
现有控制器仅对已知数学回溯失败减半；这个陌生 infrastructure 错误不列入该集合。
新 worker 的失败 trace 另外保留 error code。

关闭先发 stop 并最多等 2000 ms，未退出的线程调用 terminate，再最多等 5000 ms；
仍不能完成则明确抛基础设施错误并 unref，不无限等待。全部关闭及有无强制终止入 trace。

唯一新增实际检查是纯 worker 控制实验，不构造候选、root、ODE、DN 或 BVP：
`scripts/78718-tail-stage-pool-infrastructure-probe.mjs`，
`8c16d4/session89819 → 07fa95` 自然 exit 0，总 0.816 秒。
为几百毫秒完成，仅测试时缩短 timeout：

- 模拟线程直接 `process.exit(23)`、不报 done：120.50 ms 后识别无进度；实际线程退出码 23。
- 模拟线程忽略 stop 永久 Atomics.wait：120.21 ms 后识别，正常关闭等待 20 ms 后 terminate，实际退出码 1。
- 持续递增共享进度：总 91.19 ms 超过单个测试无进度窗 30 ms，仍正常完成退出 0。

报告 `2026-11-10-78718-numerical-stage-pool-infrastructure-01.json`，
SHA256 `89562c8d78170b03187f90efa826aee9fb42ff71784fc0cd735b5ca914b633de`。
该改动没有再次运行四段 flow。上节逐位结果精确绑定首次比较时的 pool 源；
之后修改仅进度/超时/退出清理和其元数据，原 profile 表、stage 流及数学归并未改。
