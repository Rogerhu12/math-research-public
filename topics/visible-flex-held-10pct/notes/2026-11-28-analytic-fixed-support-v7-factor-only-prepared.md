# 固定 g v7：完整因子映射与分阶段资源门，仅准备

日期：2026-11-28。独立 v7 已编译，并核原 main 的 8 处声明替换；没有构造模型、没有新 J、没有启动 BVP。它消费已真实核验的 `design/complete_factor_mmap.py` 的 **factor-only** 模式；不声称未实测的 full-CSR 映射模式已核。

## 原问题及存储范围

仍从最新 dedd 完整检查点已恢复的 initial `8c4305b836eaa5acb34a50108bb971d117e7ce4014fb754dc3cc5a886bd8959b` 接入。1497 节点、97 个状态、32 个参数、mean1168、固定完整 g/δ/λ、原 RHS64/Jac32 分组及全部原门不变。不重算旧初猜，也不另起一次完整矩阵比较。

完整 CSR 仍保存在匿名内存。原 QR 构造和全部浮点运算照旧完成后，所有持久 QR 因子数组按原 dtype/shape/C-F 次序逐字节迁移到独有 scratch 文件；只在原 solve 返回或抛出原异常后提示释放干净映射页。实际 M16 比较已由设计支完成并绑定：direction、全部 backward denominator、完整原 J residual、CSR 内容和全部原 QR stats 均逐位相同，GC 禁用下旧因子和映射对象仍按单向引用即时释放。此入口没有重复该测试。

**初始 J/QR 构造峰没有降低。** 原因子刷新前仍先释放旧因子；完整节点保存后才进入此 mesh 的 RAM 和磁盘门。映射文件不是数学状态，不包含删列、删方程、近似或低秩截断。

## 映射字节不是 RSS 信用

v7 分开记三种阶段：完整构造及其余所有将来阶段的 pre-J 门；完整 mapped factor 在原线性 solve 中全部热驻留的门；提示释放映射页后的原 RHS 回评门。共享预算仍保全部构造/完整热 solve 占用，原非线性阶段只移除“不需要常驻的 QR 页”，完整匿名 CSR 与原非线性工作量始终保留。

实际可用内存只抵扣 `/proc/self/status` 的 **RssAnon**，并限制在真实 pre-J baseline 与已知实际匿名 CSR 之和内。mapped 逻辑字节和 RssFile 均不抵扣，因为 MemAvailable 可能已经包含可回收的干净 file pages。源码中没有把 factor 文件尺寸冒充当前驻留量。

保固定 64/32 分组的额外 512 MiB 工作储备，且 RAM/磁盘外余量各至少 512 MiB。对当前真实维度 n97/m1497/k32 的**零 baseline 纯账目**如下；它不是运行时 RSS 观察：

| 阶段 | 估计工作峰加 512 MiB RAM 外余量 |
| --- | ---: |
| pre-J：所有完整后续阶段的最大值 | 2488.2002563476562 MiB |
| 全因子热驻留的原完整线性 solve | 1941.1473960876465 MiB |
| 原 RHS/线搜索回评 | 2488.2002563476562 MiB |

真实执行时加入该次实际 baseline，并按上述受限 RssAnon 规则计算额外需求。完整 factor backing、页对齐、manifest 与 512 MiB 磁盘余量共需 1010.7209568023682 MiB。pre-J 与实际 factor 构造前都重新核磁盘；存储帮助函数再执行实际 `posix_fallocate`。预算是调度估计，不是内存保证或 signal9 归因。

## 真子进程返回后的独有存储清理

独立 launcher `run_fixed_support_mapped_once.py` 只执行已绑定的一条 v7 命令。它核全部新源与新 initial SHA，真实 `subprocess.wait()` 返回后才调用已审 `mapped_factor_cleanup.cleanup_joined_child`。子进程创建的 owner 记录绑定实际 outdir 与 v7 SHA；清理仅覆盖该独有目录内的 `complete-qr-*` 临时存储，保留全部字段、检查点、源、验证记录和 owner。

launcher 不按 PID 猜测终止、不自动重试、不改变 λ 或任何门，也不从 exit0 推断数学接受。signal9 的真实 child code 与父工具退出含义分别保留。若清理出现异常，另存错误而不改写真实 child 返回码。

## 冻结准备来源

入口 `scripts/resume_20261128/analytic/fixed_support_literal_driver_v7.py` 的 SHA256 为 `6caf5ce54efb9d9b342739b5795bf39812e7f37cb8da3312c00c0c40ffde4bfb`；固定映射预算 SHA256 为 `8e8d1af72de072547702fef0586d41fb94c4d1f7a6ec07b28b45d04516161e1c`。所有共享存储、预算、cleanup、原数值源、helper、launcher 的 SHA 以及实际 M16 核验记录绑定在配套 JSON。

完整预备命令为 `held10-analytic-work/fixed-lambda002-m32-v7-preparation/prepared-command.json`。**当前尚未执行**；需等明确的实际大 J 窗口，不能据准备完成或映射小核通过晋级 M32。
