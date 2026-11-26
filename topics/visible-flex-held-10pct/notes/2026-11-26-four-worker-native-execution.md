# 原 native 执行入口允许四 worker

日期：2026-11-26。会话：`Astra-held10-06bbeb39-20261126`。

本次仅把 `scripts/resume_n4_tail/native_extended/prepare_recovered_native.py` 的 worker 输入上限从 3 改为 4，并更正两处相应英文说明；默认仍为 2。原文件 SHA256 为 `7c98aab30c24bfac42e2cd5562a0c9d59b4d24dd7d01cb1e271b07e0dba3622b`，新文件为 `08f6f0de7e1737a41864d9d420f48255a523c8aebea36dfa75de1a45940bc99b`。新文本已实际通过 Python AST 解析；未重跑历史 batch、未启动新 DN、未改运行中任务。

## 按段等价机制

原 [`parallel_native_batch.py`](../scripts/resume_n4_tail/native_extended/parallel_native_batch.py) 已允许 1–32 个 worker，本次完全不改；其当前 SHA256 `9177a8499517695deebf00907c64bdc08adc5e5fd2229c8987a2a7ac8ef6bb42` 与下面历史四 worker 实测所绑定源码一致。对总段数 S、实际 worker 数 w，child i 收到原全局段 `i, i+w, i+2w, …`。每段原输入状态、系数、RK 节点和步长字节原样复制，共用数值 header 原样复制；child header 只改段数和无数值意义的身份 token。

每个 child 调同一个已绑定 C++ CLI。`vf_run_stage` 对各段重新构造局部 `Engine`，不接受全局段号；原全局段号仅用于输出标签。合并按 `global = local*w + child` 恢复原顺序，只改回输出段号并原样复制其余 payload。多个合法域失败按原全局序保留最早失败；进程中断或协议损坏仍归工程失败，不能当作 DN 数值拒绝或接受。实际每段计时会变，不在逐位数值等价范围内。

[`native_batch_adapter.mjs`](../scripts/resume_n4_tail/native_extended/native_batch_adapter.mjs) 在分片前独立构造原标量和原变分 cusp 网格，要求全部 x/h 字节相同，然后冻结原数值系数、三角节点与完整段输入。worker 数不参与这些构造。原 RK4、每点 30 轮 root 上限、20 个 halving 值、生产 projection floor 0.05、root 容差 `8e-14` / fallback `5e-12`、x87 精度及舍入门、隐式 Jacobian、均值积分、`portRatio` 行换算、原残差归一化、Newton/线搜和最终接受门均保留。`cutJets` 和物理 audit 仍沿原 JS 路径执行，四 worker 并不将它们并行化。

原 [`frozen_flow_production.cpp`](../scripts/resume_n4_tail/native_extended/frozen_flow_production.cpp) 及 wire splitter 中的 **M ≤ 64** 硬门全部保留。未来若某实际设计需要更高 M，本入口仍拒绝，不能截断模式或借此次执行参数修改声称已支持。

## 已存在的最少实测依据

[`native_parallel_equivalence.json`](../scripts/resume_n4_tail/native_parallel_equivalence.json)（SHA256 `f97357791f8540835d62c2d1b59b9110965b8a2f504cc001db8aa4dded0decc4`）记录一个真实完成的 M20、2304 段、四 worker batch：四 child 返回码均为 0；共同数值 header、所有原段输入字节相同；96,768 个状态标量、3,870,720 个 Jacobian 标量和 16,128 个 root/几何诊断标量全部数值输出字节相同。唯一排除项是每段成功记录末尾 8 字节 `kernel_seconds`。

该次串行进程用时 `392.136659724` 秒，四 worker wrapper（含分片/合并）用时 `104.92322919600701` 秒，实测比值约 `3.7373674`。两次运行的实际时刻及负载不同；这是一个既有固定状态 batch 的一次计时，不外推新 M24/M32、λ1、完整 DN 或端到端速度，也不提供新环境 RSS 结论。该状态本来是被拒绝的残差评估；这条执行等价记录不构成新的尾接受、full-H 接受或前缀耦合成功。

[`native_parallel_adapter_entry.json`](../scripts/resume_n4_tail/native_parallel_adapter_entry.json) 另记旧四 worker 安装器的精确反向 patch 和其他数学源码不变；它是执行接口来源记录，不是额外数学接受。

## 实际改变的来源与执行字段

相同数学输入由 2 改为 4 时，`native-parallel-plan.json` 的 `workers`、该 plan 的 SHA、manifest 的 `execution_provider.workers` 与 plan 引用、manifest 自身 SHA 都会变化。本次 preparer 源码变化也改变 manifest 的 `installer` SHA。后续 checkpoint 的 `parameters.nativeBatchManifestSHA256` 和 `nativeBatchManifest` 引用应绑定这个新 manifest，不能沿用旧值。

按原 fresh-destination 规矩准备新的独立目录时，manifest 的 `source_topic`、各 owned-source 路径、plan 路径等也随实际目录变化；adapter 内嵌 plan 路径因而可能使 adapter 源码 SHA 改变。**worker 数值本身不嵌进 adapter 数学源码**，所以不能仅因 worker 数变化便宣称所有数学源的 hash 都必变。真实执行另记录新的 child 数、分组、child token、文件引用、返回码、起止时间和计时。`shootingEvaluation` 仍为 `native-literal-LD-batch-v1`。

完整物理参数、M、spacing、N、RK steps、physical depth、shooting parts、背景校准、完整 H 及全部数学门保持原声明。此次只使将来的独立实际 λ1 full-DN 任务可以显式选 `--workers 4`；未预认其将收敛，亦未支付任何当前缺少的闭族、接缝或极限证明。

