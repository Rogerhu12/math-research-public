# q105 actual 延拓的磁盘块 Jacobian 入口

## 范围与原问题

本入口只替换全局 Jacobian/QR 的存储和增加数值后向核验。目标仍是实际核心
`(c2,c4,c6)=(.105,-.006655700963004517,-.0004116733380408847)`，
表示尺度仍为 `.09`。前缀使用 M24、N768、tol `1e-7`、初始 2004 节点和
max 2400；真实尾为 M24、N512、physicalDepth 8、steps 12、parts 8、
tol `2e-9`，完整 H、全 Jacobian、audit 与物理 trueBC `1e-10` 门均保留。
这不是固定 g 精化，也没有新闭面、连续 reach 或 held/D 结论。

上一内存块路径 `...q105-freeq4-m24-tol7-exactraw-r1` 的 session 14476
正式返回 tool 137 / child signal 9，首个完整 Jacobian/factor 未返回，
没有接受新 Newton 步。原因未知；608488 KiB 峰值和 1388.43 秒 wall
不能用于断定 OOM、时限或物理分支失败。其初始恢复点的全 x/y/p/cubic
以及所有分块 SHA 已保全，新入口直接恢复该全场，未从摘要或首模重建。

## 代码与完整线性检查

- `computations/strong_disk_actual_backend.py` 给原 bounded actual 入口挂载
  独立磁盘 backend，并保留原回调和 Newton 流程。
- `computations/strong_disk_actual_three_control_bvp.py` 通过列明的内存源码
  变换接入；原 `strong_actual_three_control_bvp.py`、exact-raw 入口和已保存
  旧源码均不改写。
- `computations/root_disk_block_collocation.py` 为父代理维护的已发布依赖。
  邻接 A/B/P 块和原 QR 树中的数组以原 float64 字节存入匿名临时文件，
  原 balanced QR 遍历保持。

每个真实 `factor.solve(b)` 后，都重新流式计算原完整矩阵的 `A @ x`，
逐个右端核验

\[
\eta=\frac{\|Ax-b\|_\infty}
 {\|A\|_\infty\|x\|_\infty+\|b\|_\infty}\le5\cdot10^{-11}.
\]

矩阵无穷范数包含全部配点块与边界行；该门不允许只抽样、只检查消元根块
或只检查目标三个控制。非有限数或越门会抛出异常，不能冒作成功 Newton 步。
这是普通浮点的线性后向误差诊断，不是区间逆证书，也不代替非线性 RMS、
物理 BC 或真实尾的原验收门。

分批参数显式为 radial 16 / collocation 12，几何 Flow 缓存仍为 8。
Node 资源配置为 heap 256 / point cache 2；逐真实响应关闭尾 worker，
避免它无须常驻时与下一前缀 Jacobian 同时保留。仅当完整 H、source/config、
Jacobian 和 audited 标记全部匹配时，原 recorded port 才复用已经审计的
同 H 包；任何 changed H 仍走原真实求解。当前初始包是 session 66512
实际重新计算并正式退出 0 的包，并非失去的旧 session 29674 数组。

生产入口没有使用实验性的 stage-flow persistence cache。

## 已完成的实现核对

`strong_disk_backend_check.py` 的 session 89261 正式退出 0；
`...strong-disk-actual-backend-synthetic-check.json` 保存六项小夹具结果：
原调用默认参数接口、单右端、多右端、损坏 matvec 的硬拒绝、自有进程 RSS
和临时存储/原 backend 的清理恢复。全部通过，正常解最大后向误差
`1.7112993135584748e-16`。故意损坏矩阵的测试产生约 `.2791` 并被拒绝；
这项数值不能被引用为实际生产解的后向误差。

session 98257 的生产 `--prepare-only` 正式退出 0，确认 27 参数 / 100
边界条件以及完整 metadata 守卫；该步骤不加载物理 Jacobian、不启动
尾 worker、也不运行 BVP。上述核对均不宣称真实 q105 解已完成。每个生产
线性步仍须执行自己的完整流式后向检查。

## 运行与资源证据

不可变计划 `...q105-freeq4-m24-tol7-disk-r2-command-plan.json` 记录精确
argv、全部关键源 SHA、原 raw/config 和已审计尾包 SHA。其 `prepared-not-run`
是计划创建时状态，运行状态另存，不改写该哈希。

真实 fresh 运行 session 4388 已启动。截止本说明冻结时，它正在首个完整
Jacobian 的分批装配，尚无真实 factor/solve 终态；因此此文不填写生产
后向误差或 q105 成功标记。

新 `-disk-events.jsonl` 每 20 秒由实际前缀进程读取 `/proc/self/status`
和自身 rusage，并仅检查带 PPid 守卫的直接自有子进程。它明确区分当前
VmRSS、VmHWM、CPU 时间与历史 wait4 峰值，且记录装配点数、factor、solve
阶段。不同 exec 的 PID 名字空间不可见时，不再以外部 `/proc/4` 或历史
峰值猜测当前前缀内存。生产源与计划在运行期间冻结。

正式终态、每步后向检查、原门结果和资源记录将在该 fresh prefix 下保存；
本稳定包只含源、计划、小夹具及此说明，排除活跃日志和中间输出。
