# warm 跨 runner 差异：有限源码核对

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / geometry_path。

本记录仅阅读当前源码和 workflow，不执行数值、fixture、旧报告重算或参数
试验。目标是找一个可直接解释 warm 差异的简单实现缺陷；没有把尚未核实的
环境差异断言为实际原因。两次实际数组或逐阶段报告没有在本任务中作数值
对照，故不定位第一条真正分叉的浮点操作。

## 1. 实际路径与已经核对的范围

`rebuild_a04_chain.py` 的 warm 阶段调用 `reproduce_and_solve.py`，后者顺序
调用 `rebuild_fullclosed.py` 和 `rebuild_closed_warm.py`。

前缀恢复先严格读取固定历史 `.99` blob，其 SHA 必须为
`b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`，
再按源中固定的五条命令推进到 `.995 M112/N2048`。实际数学路径为：

- `parallel_20261117_continue.py` 的 `feasible_newton`、`projector`、
  `main` 与 `parallel_20261117_frenet_symbol.py` 的 `Frenet`；
- 默认线性后端是 `geometry_20261114_separated_qr_bvp.py`，不是 direct-csc；
- 标量读数使用 `parallel_20261117_profile.py`；
- pulse 使用 `2026-11-17-parallel-pulse-common-jet-field.py` 的 wrapper、
  `2026-11-17-parallel-geometry-short-ivp-field.py` 的 `nodal_field`、
  `PulseProfile`、`InwardProfile`；
- 随后是 pulse assembly、完整 Hold warm 和 mode-damped warm 两个生成元。

已顺着上述模块的 import 读到实际调用的 Frenet/profile 定义，区分了仅被
导入但不执行的 probe/main。这里只讨论这条实际 warm 路径，不对所有历史
实验脚本或 SciPy/BLAS 内部实现作普遍无缺陷声明。

## 2. 已排除的简单来源

**未发现 warm 数学路径中未固定的随机数。** 搜到的
`Frenet.probe` 使用 `default_rng(17)`，Schur probe 使用
`default_rng(20261117)`；它们只在各自未被 warm 调用的 probe 中。QR 后端
的 `tempfile.mkdtemp` 确有随机目录名，但目录名仅作分块文件寻址，不进入
线性代数系数或扫描顺序。

**未发现所查 `np.empty` 在使用前留下未赋值槽。** 具体覆盖关系为：

| 数组 | 源码中的完整赋值责任 |
| --- | --- |
| `projector.rows` | 遍历全部 `q.n` 列，每列赋全部投影行 |
| continuation 初值 `y` | `inside` 与 `~inside` 两个互补列集分别赋值 |
| continuation `fun` 输出 | 遍历全部 `s` 列；域异常时该列显式写 NaN |
| continuation `jac` 输出 | 遍历全部 `s`，逐个赋完整 Jacobian 平面 |
| Frenet `Ad/Ae` | 遍历三个分量，完整填满最后一维 |
| QR `U/transport` | 初始 `U[0]` 加顺序 `append(j)`；`finish` 要求实际收到全部 `m-1` 段 |
| QR `p/offset/answer` | 初值加完整前向循环、末值加完整反向循环 |
| QR 验证 `residual` | 全部 collocation 段，加两个完整边界区间 |
| Hold `stage_times` | 偶数槽为全部节点，奇数槽为全部中点 |

没有发现 warm 的数学停止条件读取墙钟。BVP 使用声明的 tolerance、节点
上限、Newton/Armijo 次数和残差比较；pulse 的 DOP853 按状态、端点和误差
控制推进。恢复驱动中的时钟用于 manifest、日志与耗时字段，不用于修改
warm 方程或选一个按运行时刻变化的初猜。

已见的 pulse 分片集合由 `sorted(set(...))` 排序后遍历。所查数学路径没有
发现按随机 hash 顺序遍历集合来累积系数的操作。未设置 `PYTHONHASHSEED`
本身不能据此被认定为此次差异来源。

## 3. 已确认的字节差异来源，不等于几何差异归因

`parallel_20261117_continue.py` 将实测 `seconds` 写进完整 prefix JSON，
然后压缩。虽然 `gzip.compress(..., mtime=0)` 固定了 gzip 时间字段，JSON
内部的墙钟数值仍会变化。后继又记录实际 `input_sha256`、
`terminal_boundary.input_sha256`、reference/parent SHA，所以即使假定所有
数学数组完全一致，报告与压缩 JSON 的字节身份也不能预期跨运行相同。
恢复 manifests 与其他报告还包含实际路径、开始时间或实际耗时。

这解释的是一种**具体、可见的元数据字节变化机制**。不能用它解释所有
候选文件或有限读数的差异：完整 Hold warm 的 NPZ 只写数值数组，
mode-damped warm 复制这些数组并增加数值 rates/reference jets，没有把
上述 `seconds` 或 parent-report SHA 作为 NPZ 数组写入。因此，没有实际
查看 NPZ 数组/归档成员差异前，不能把 warm bundle SHA 的变化归因于 JSON
时间；af89 的真实 finite max 差异更不能由时间字段本身解释。

## 4. 尚未排除，且不应猜定的因素

两份现行 workflow 都明确使用 Python `3.12.14`、NumPy `2.3.5`、SciPy
`1.17.0`，并将 OpenBLAS、OMP、MKL、NumExpr 线程数设为 1。恢复 driver
也在子进程环境中再次固定前三项线程数。这排除了本源码显式请求不同线程
数的情形，但不是完整执行二进制身份。

两份 workflow 的 runner 标签都是 `ubuntu-latest`。源码没有固定完整
runner image、CPU 型号/指令分派，pip 命令也没有给 wheel 文件 hash；
Python 包版本号不记录完整 BLAS/LAPACK/libm 与其实际执行路径。
本任务没有读取两次 runner 的实际二进制构建记录，因此这里只能说这些项
**尚未由现配置固定或由本检查比对**，不能断言两次一定不同，更不能断言
实际差异就是 CPU 导致。

实际浮点路径含 QR、LU、矩阵乘法、FFT、三角函数和自适应 BVP/IVP。
`feasible_newton` 用严格 Armijo/残差比较决定下一步，DOP853 保留实际接受
节点，末端还按 64 ulp 删除极短 microcell。这些是可见的条件分支：若此前
舍入值不同，存在把细小差异传到后续路径的机制。仅凭这一源码事实，不能
判断本次是否发生了分支改变，或定位到哪个库运算；它也不是已发现的实现
错误。

另一个需明确区分的地方是 **warm 之后的 af89**：主配方明确传
`steps=6, seconds=600`；`resume_20261120_physical_subspace.py` 在每次迭代
开始前检查墙钟，并可置 `status='time_budget'` 提前退出。这是实际存在的
时间依赖，但本检查没有消费两次 af89 的实际 `status/iterations`，不能
声称它已经触发。它不属于前述 warm 生成链的停止条件。

当前主配方会记录 warm drivers 的 source SHA，前缀 manifest 记录实际
continue source，输出还记录 symbol/profile source；这并不等于本次已经
把两次运行的全部实际 source SHA 逐个对过。若仅凭当前源码无法排除版本
差异，也不能先把它当作相同执行二进制再归因硬件。

## 5. 有限结论

在已读 warm 生成路径中，没有找到一个可直接修正的未固定 RNG、明显未
初始化数组槽或按墙钟选择数学初猜的缺陷。这项有限静态检查据此收束，主求解与完整曲率任务继续；不
扩展环境基础设施，也不改变参数或重算。

跨 runner 的文件名、source 版本号和成功标志均不能代替本次实际场身份。
当前续接与 complete consumer 继续绑定真实 bundle/node/first SHA；同名
再生文件不会自动继承上一候选的几何证书。这一责任不依赖最终是否能查明
浮点差异的具体机器原因。

实际不同场及已返几何见[worker03记录](2026-11-20-geometry03-actual-field-and-radius-return.md)。公开两份阶段摘要的af89状态均为`iteration_budget`，不据源码存在600秒门就改称已触发`time_budget`；这也不解释更早warm已出现的身份差异。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
