# continuation03 自然关闭与步长下限失败：独立只读审查

审查者：`/root/tail_theory`，2026-11-09。结论：**PASS，确认为已关闭但未完成目标的有限尾延拓尝试。** 原控制器、原始请求与来源绑定一致；进程正常退出不构成数学成功。没有重跑 worker、真实 DN、RK、BVP 或优化，原文件及候选状态均未修改。

## 1. 实际退出的来源与身份

实际长计算由 root 持有 session `3046`。本审查引用 root 的最终工具观察 `eaf578`、退出码 `0`，不把该回执冒认成审查者的执行。观察文件是：

`notes/2026-11-09-db6f-root-continuation03-final-observed.json`

SHA256 `c355b99501948e34a290cbb5fb0d54250c28c5b1b9e6491c0892c2636dc8c68f`。

三个退出层次已分别核对：

| 层次 | 记录中的事实 | 能证明的范围 |
|---|---|---|
| root 的真实工具观察 | session3046，`eaf578`，tool exit 0 | root 已观察到外层进程结束 |
| 空间 guard 的 child 记录 | `actual_child_exit_code=0` | 原控制器进程正常返回 |
| 控制器最终结果 | `worker_exit_code=0` | 原 worker 已被关闭并取得退出状态 |

guard 记录仍明确 `tool_exit_observed_by_root=false`，没有自称替代 root 的工具观察。控制器结果明确 `UNCONVERGED_CONTINUATION_STEP_LIMIT`，`target_reached=false`、`target_audited=false`。这些字段和正常进程退出完全相容。

guard 的实际事件表只有 `started`，没有记录空间暂停或恢复；仍保留原 512/768 MiB 阈值及 2 秒轮询。这里只报告日志事实，不由它推断未记录的外部进程事件。

## 2. 来源与原配置未变

已独立重哈希 resume03 launch 的 **83** 项绑定、外层 guarded-launch 的 **89** 项绑定；相同物理命令逐项一致。关键原件如下：

- resume03 launch：`0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c`。
- guarded launch：`9d2495ea6b48872b40a3c813f0c3076819f48a88f1f5bd9dc1b1ec33bfa49594`。
- 原 controller：`23f75c9ecc2825e4a8314468775c40b06b6b47439edd0d0ed9a69a9fb5e298a9`。
- 原 continuation client：`cd9b25521427dcefebd5baddcf6a105c58c53f495cf8692fb725d49e4558a564`。
- 原 space guard：`cf1e2364300015c841b2070be51e948dc7ba37ef5b98eef0441819bca1e6aabd`。

控制器生成的 config 与原 config 作带 JSON 类型的逐值比较，仅有原设计允许的五个输入/输出路径变化；原 15 模、spacing3、depth12、parts8、steps32、angular256、36 轮及 `solveTolerance=2e-9` 均保留。每个实际响应 resolved parameters 中的 `projectionFloor=.05` 保留，物理及离散参数与真实 resume checkpoint 一致。

此次从已闭的 $s=31/32$ 成功响应恢复；首次请求 $63/64$，初步长 $1/64$。物理高度按原定义逐模计算：存储索引 $j=0,\ldots,14$ 使用 $s^{j+1}H_j^*$。本审查使用相同 NumPy 标量幂定义，对全部九个实际请求和其 checkpoint `cutHeight` 做精确 binary64 数组相等检查，没有加入额外 $c^4$ 变换，也没有把请求标签当成实际满足边界的证明。

全部九个响应的源映射均为同一组八个冻结文件。每个 checkpoint 的 `states` 为 $865\times30$、`rawStates` 为 $13\times30$，均为有限非布尔数值；`rawNode` 保持原布局，并逐行核 `rawStates=states[rawNode]`。原生有限尾状态不能据此当作已导出的闭曲面。

## 3. 原控制器终止逻辑

已全文重读 controller、client、worker 的更新路径，以及原 shooting core 的迭代和十档线搜索。

client 在收到每个响应后先原子保存完整 gzip 包；若响应含 `failed` 或没有 `converged`，随后抛 `FloatingPointError`。控制器捕获该错误，仍从完整包核实际响应；不会把一个异常字符串本身写成成功。

worker 只有 `sol.converged` 时才更新用于后续 warm 的 `last`。失败包保留最后迭代状态作诊断；不会用它覆盖此前成功状态。控制器也只有实际 `converged=true` 且有限残差严格小于原 tolerance 时才更新 `last_converged_*`。

本次九次请求的关闭结果为：

| call | 精确尺度 | 原结果 | 说明 |
|---:|---:|---|---|
| 1 | $63/64$ | 成功，$9.40030806875761\times10^{-10}$ | 8 个基点评价，之后步长减半 |
| 2 | $127/128$ | 原线搜索失败 | 保持上次成功状态，减小步长 |
| 3 | $253/256$ | 原线搜索失败 | 同上 |
| 4 | $505/512$ | 原线搜索失败 | 同上 |
| 5 | $1009/1024$ | 成功，$6.260661072552149\times10^{-10}$ | 6 个基点评价 |
| 6 | $505/512$ | 原线搜索失败 | 从新的 last-good 尝试 |
| 7 | $2019/2048$ | 原线搜索失败 | 失败基点 norm 为 $.020004151516050995$ |
| 8 | $4037/4096$ | 成功，$1.251822050474137\times10^{-9}$ | 最后真实成功，5 个基点评价 |
| 9 | $2019/2048$ | 原线搜索失败 | 失败基点 norm 为 $.01964568659651265$ |

call9 的请求距离 last-good 恰为

$$
\frac{2019}{2048}-\frac{4037}{4096}=\frac1{4096}.
$$

失败后，原 controller 按一半请求距离设置局部变量

$$
\text{step}=\frac1{8192}<\text{minimum_step}=\frac1{4096},
$$

所以进入 `UNCONVERGED_CONTINUATION_STEP_LIMIT` 分支并跳出循环。本审查从全部九次历史独立重演了这个标量控制流，未执行任何数值方程。

`progress.current_step=1/4096` 是本次请求开始时保存的值；源码只在循环入口更新该显示字段，终止前的局部减半不再次覆盖它。因此它不是一个与终止原因冲突的记录。审查报告另列精确的 post-failure 局部步长，避免误读。

只有 `target_reached=true` 才会触发最后一次 `goal.copy(), jacobian=True, audit=True` 请求。本次没有进入该分支，全部九次请求均 `jacobian=false,audit=false`。call8 虽为真成功有限尾 warm，其 `heightJetJacobian` 与 `audit` 均为 `null`；它不是目标 $s=1$ 的最终 DN，更不是完整 prefix 联解。

## 4. call9 的真实失败含义

call9 完整响应 SHA256 为 `19ca2fbff43302060aa66a5f841b516b9c30d40aec338d3d5879e4814ee23810`，只有原失败 schema 的三个键：`failed,lastIteration,checkpoint`。**该包没有 `residual` 字段。** $.01964568659651265$ 应准确称为 `lastIteration.norm`，不应写成一个成功响应的最终残差。

最后基点为 iteration3：

- norm：`.01964568659651265`；
- minA：`.0692573865773523`；
- minD：`.9916202785212969`；
- chartCondition：`57772.820161704585`。

call9 本身有四个连续基点评价，及对应四组 trial，组长依次为 1、1、10、10。前两组全步接受，第三组在第十档接受；最后一组十档均为 `residual-not-decreasing`。这些最后试点都完成了原残差评价，但没有严格下降，因此原 core 抛出多重射击线搜索失败。

第三组曾有三次 `momentum-root-solver-rejection`，其三个阶段输入文件已按原记录重哈希、核参数、目标与输入槽。它们不是最后一组失败的类型；不能把最后一次退出概括成 guard 触底。每组 trial 编号、$2^{-k}$ 步长、baseNorm、接受位置及下降/不下降符号均与原 core 逐项吻合。

最终恢复用 iteration checkpoint 的状态与失败响应所留状态完全相同；它的四个基础迭代标量也同值。correction 阶段后加入的 chartCondition 不必已存在于更早写盘的 iteration JSON，本审查没有错误要求两种记录的全部键相同。

这个失败只说明所冻结算法在其声明的步长与线搜索预算内没有完成本次目标；没有证明该边值无解、正支路不存在或所有其他初猜都会失败。

## 5. 旋转日志、历史行与遗留路径

每个 attempt 指向的 trace/trials 文件均按其保存的 bytes/hash 核实。正文的 call 身份以每行 `call` 字段为准，而不只取文件名。

实际有六个旋转后的 trials 文件包含更早 call 的历史行。全部 **318** 条这样的行已逐字段证明与其原 call 的闭日志相同；本审查未假设它们是当前 call 的新试点。call009-trials 总计 26 行，其中 4 行属于 call8，真正 call9 行为 22 行。过滤后所有九次请求的 trial 组都完整。历史内容为何在新文件中出现，本次不作无证据归因。

关闭观察后，旧 `active-trace` 和 `active-trials` 路径仍可读到历史内容。分别为 2106 字节和 5528 字节；它们的字节均严格等于正式 call009 对应旋转日志的前缀，缺最后一行。读取时文件时间也早于正式失败响应。这些路径名不构成仍有活进程的证据，不能替代 root 的实际退出观察；本审查也不删除或重写它们。

独立 checker v1 曾额外假设这两个路径必须不存在，实际回执 `986e13`、退出码 **1** 在该断言处停止，未写报告，未运行求解。该额外假设不属于原数学或 controller 接受门。原 checker 已原字节保留，v2 只将此断言改为上述明确的历史前缀核查并在报告单列事实；其余来源、参数、响应、trial 和终止检查不变。不能省略这次审计自身的失败记录。

## 6. reproduction、progress 与原最终准备门

已用带类型的规范 JSON 比较确认：

- `reproduction.result` 与最终 `progress` 完全相同；
- reproduction 去掉 result 后与原 input-bindings 完全相同；
- 原 run.log 的九条请求摘要及最后状态摘要与 progress 一致；
- last-good record/hash 确指向 call8；没有 final target record，也没有第十个响应包。

最后成功 call8 SHA256 为 `396cdd758e7b38cfd7d06ae7595210685bf2d9d9ef90e2fa157bafff087f93cf`。root 的失败观察所列十个闭文件也全部重核。

原 `db6f-prefix-prepare-final-m15-coupling-v3.py` 保持 SHA256 `273bb318dfaa2839be8fa6c532152cf708880c13591ac0fcbae5f4e97bdacdb5`。本审查实际运行其 `--check-current-gate` 只读分支，回执 **`c1d7d9`、退出码 0**，得到：

```json
{"ready":false,"reason":"Continuation has no target-DN audited success","files_written":0,"solver_launches":0}
```

该拒绝发生在明确的目标状态门处，早于成功工具观察 schema 和最终 Jacobian/audit 检查。没有把本次失败观察文件当成未来成功观察 schema 的正例；没有构造假成功 fixture，也没有写出新的 coupled 配置或启动命令。只读检查进程返回 0 也仅表示检查完成，与 `ready=false` 不矛盾。

## 7. 独立检查的实际执行

有效独立脚本为 `scripts/db6f-tail-review-continuation03-closed-v2.py`。它只使用标准库和 NumPy 做已关闭数据的读取、哈希、有限数值/schema、标量控制流与数组相等检查，不导入 solver 或 worker。

实际回执 **`c63a9c`、退出码 0**，工具报告耗时 `.475217542` 秒。报告：

`notes/2026-11-09-db6f-tail-review-continuation03-closed-check.json`

52807 字节，SHA256 `a92f7d6f21dfc91e0ea3123c220e3329c0aaaf797e13b6b9acd746b8bbc57b8b`。

共核 **132** 个不同的闭来源/历史文件，并在读完后再次重哈希；83/89 两个 launch 账本的每项都通过。未重跑 root 的 worker；也未冒认 root 对 calls007008 的既有审计执行 `3b91f3` 为本审查执行。此处对九个响应的独立元数据审查覆盖并加强了该闭包身份检查，但不生成新的数学解。

## 8. 结论

本次可封存为：**原式 continuation03 已自然关闭，最后真成功为 $s=4037/4096$ 的有限、未审计 warm；随后在 $s=2019/2048$ 原线搜索失败，并触发原最小延拓步长终止。** 工具、guard child 和 worker 的退出码均为 0；目标状态及原最终准备门均明确不成功。

本审查没有改变 tolerance、projection floor、物理度量、离散设置、失败状态或日志，也未支付目标 DN、完整 prefix、闭曲面或 G5，更没有推出无解结论。
