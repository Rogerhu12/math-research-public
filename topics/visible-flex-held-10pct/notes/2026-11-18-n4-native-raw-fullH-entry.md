# n4 raw 核进入完整 H 的真实非线性尾

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 已发生的实际入口

原 raw coupler `couple_raw_actual_tail.py` 的 `00b63349…` 版本已在 observer 会话 `96568` 启动。首份完整 H 请求于 2026-11-18 04:29:57 UTC 发出，随后完成了一个真实 2304 段全 Jacobian 批次。该批次使用四个原 C++ CLI 子进程，父进程和四个子进程均正常退出 0；Node 的来源、进程元数据、wire 解码和原残差计算均实际完成。本条记录入口，不声明完整 H 或前缀已被接受。

初始化来自[半幅原 DN 的真实失败终态](2026-11-18-n4-native-halfH-original-DN-terminal.md)：完整 checkpoint 为 `ebae7190…`，最后原残差为 `2.0636915055985155e-9`。它在本次计划和记录中始终标为**未接受初值**。本次不再求半幅目标，不再运行局部候选；`--scales 1` 直接要求该前缀的完整 H。

## 目标、核心和固定物理数据

实际完整 H 仍由原 coupler 用 `obj.bridge.sigma * obj.q * y[obj.iz:, -1]` 计算。这里 `obj.q` 是原 gauge 幅值 `0.0125`；实际主幅值 `0.012488347919833637` 没有被再次乘入高度向量。实际 worker 请求的全部 20 个分量与先前同一前缀的半幅 H 同时乘 2 后逐字节相同，其 float64 哈希为 `bd560bebd4d0f41405b713a89507f4973e6f791b39b4d60e863caa0c98acfe11`。前两个物理高度为 `-9.422426032387329e-6` 和 `-4.2609387041660345e-8`。

原完整 raw 前缀为 `c2a31380…`，其已记录的完整采样 metric 为 `8.9101794732e-7`。本次入口保留原 2282 个节点、全部 19 个 raw 控制、自由 c8、冻结 J16，以及 eta=.1、a=.147、主/控制宽度=.16、圆化参数=.02。实际完整核的材料角 $F,F_u,F_{uu}$ 身份误差均为 0，全材料图投影误差为 `2.220446049250313e-16`；这些是原 `build_seed` 在本次执行中报告的入口检查。

物理 profile 保持原 `delta=0.030158202455449618`、`vd=0.25018727173023186`、`vu=.35`、ramp=.45、ramp_eta=.05 和原 turn-plateau bridge。73 个先前记录的前缀源文件均与旧执行的字节相同。原实际尾配置逐值比较只有 `initialCheckpoint` 和 `traceFile` 两个路径改变；M20、spacing4、N512、depth8、parts32、RK16、生产 floor=.05、原 `2e-9` 门及 audit32 均不变。

## 静态模板与实际输入分别绑定

新旧共有的 **21640952 字节静态模板**逐字节相同。该模板包含 774144 字节的零状态占位，即每段 42 个零值，另外保留 withJac=0 与 token 占位；这个身份用于原固定系数、三角读数、真实 cusp 网格及打包布局。它不是“新完整 H 状态和旧半幅状态相同”的结论。

新完整 H 的实际首批输入 SHA-256 是 `5ceab514df9b192e1cf191572aa99b4a75936babec8c3cbcf7781e1ab4d3b1a4`，旧同半幅入口实际输入是 `bd9b1121152881c0ece0d4e28de2a9c660cca3b53fe32f14d3a58439c46abb1e`，两者不同。实际 H 另外使用上述 `bd560beb…` 哈希绑定。明确区分这些对象的只读文件为 scratch `actual-fullH-entry-v2.json`，其 SHA-256 为 `ebacbe8516fa85a8ca32c2395d1592f2a54ae5d5c13056983d1f49abfcce406c`；原 v1 仍保留。

## 原验收流程仍须完成

原 coupler 的这份 warmup 请求为 `jacobian=false, audit=true`。这不关闭原 Newton 内部的全 Jacobian 迭代；它表示该 warmup 响应不要求返回 height-jet Jacobian。后续原 coupled outer loop 才请求该完整边界 Jacobian。入口记录没有把两者混为已经支付的终态。

首个原完整 Newton 残差是 `19235.534247812484`，`minA=0.9621973445945032`、`minD=0.999889568052114`；这是加倍目标后初值的实际结果。首批进程墙钟为 103.501701126 秒，包装器自身墙钟为 103.29539947 秒。它们是本次完整批次的观察，不把各子进程的 kernel 时间之和称为父进程墙钟。

后续完整 H 仍须过原实际 DN 门和审计，原前缀联立还须完成全部边界与两阶 seam 检查，并独立通过完整采样 metric 门。本条不声明精确圆弧、无限尾、闭族、连续证书或 10% 指标。

## 文件来源

固定启动计划为 `n4_work/native-raw-fullH-v1/launch-plan.json`，SHA-256 `f724afba254a82f983805833a8877d3e99d67c82451be47a9e6f7aa1e40263b7`；新 owned manifest 为 `1661d97a…`，四进程执行计划为 `4f463dc3…`，原 C++ CLI 保持 `1b47ed47…`。包装器、Python、执行计划与 C++ 二进制分别绑定。

紧凑记录为 `scripts/resume_n4_tail/native_raw_fullH_entry.json`，实际只读 collector 为 `record_native_fullH_entry.py`，执行 `ab8688` 真实退出 0。该记录核对原完整输入块、全部源哈希、真实请求、完成的首批进程与四个子进程文件，并保存固定的 trace、native-events、seed-summary 及资源观察前缀。没有重跑 root、flow、Jacobian 或 DN，也没有把仍增长的日志冒充不可变终态；完整场、节点和逐段输出只在 scratch 中通过哈希引用。
