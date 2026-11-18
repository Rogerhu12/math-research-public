# n4：从完整实际解进入 M24，并即时保存已返回阶段

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 本条范围

从已完成的 $M=20$ raw 核—真尾联立检查点进入 $M=24$。物理子午轮廓、$\eta=0.1$、$\lambda=0.02$、$a=0.147$、两个过渡宽度 $0.16$ 以及原低端锚 $J=16$ 保持。$q$ 与全部物理控制继续作为求解未知量；`fixed=True` 不等于所有构造参数被冻结。本条只是设计分支的谱延续入口，不能据此声称满足本课题 README 第 5 项的全参数与 $t$ 范围固定加密要求。

本条已经观察到新 $M=24$ 的完整 native stage/Jacobian 求值真实成功；尚不把该入口当成新尾、前缀或接缝已经接受。原联立计算继续独立运行，后续终态另记。

## 唯一输入与完整核嵌入

实际输入是 `n4_work/native-raw-fullH-v1/seed.json.gz`，SHA 为 `db78f24808e87420a30faed2759c6a44f0980f6eefe872cc0a67cb51ca9a433c`。这是原完整联立程序成功保存的检查点，完整采样 metric 为 $8.910232570314584\times10^{-7}$；没有退回旧线性 DN 前缀。尾初值是其真正接受的最终 call 4，SHA 为 `c782c31c544bdc0839a8719f658b2919847c86c1f02bbcfa99bdc3ba66489138`，原 shooting 残差、完整边界 Jacobian 和 audit 均已实际返回。

既有 `build_seed` 以保存的参数与控制尺度重建核心，把原 $19$ 个物理控制零扩为 $23$ 个；独立 $c_8$ 仍自由，低端泄漏定义继续使用固定 $J=16$。原 $2282$ 个节点完整保留。实际入口在 $1024$ 个材料角样本上得到 $F,F_u,F_{uu}$ 比较误差零，完整材料图的投影误差为 $4.440892098500626\times10^{-16}$。这些是入口数值检查，不是新增连续角度误差证书。

规范幅值仍是 $q_{\rm gauge}=0.0125$。输入显示字段为 `actual_q = 0.012488348123231355`；按保存参数重建的入口值为 `0.012488348123231354`。这一末位差按原定义／显示摘要诊断保留，不用显示摘要替代参数定义。后续解的实际幅值及控制漂移必须继续报告。

原 worker 于 `2026-11-18T05:25:07Z` 明确记录从 sourceModes $20$ 到 targetModes $24$ 的原嵌套尾初始化，depth $8$。随后实际请求完整 $24$ 维 $H$。新的图投影和原 warm 初始化参与形成了这次输入，不能把它说成旧 $M=20$ 实际 payload 的逐字复制。

## 数学源与新作用域

新 manifest 位于 `n4_work/native-parallel-m24-v1/manifest.json`，SHA 为 `4a2c3896f119b869740d8baa520d4d7473a8b29d477e4105d70ed4edf83fde6e`。其 numerical scope 相对既有 manifest 只把 $M=20$ 改成 $M=24$；原 owned Node 数学源、生产 C++ 源、原 CLI、运行库及四路 wrapper 均保持原 SHA。生产内核本来按 runtime $M$、spacing 及字面几何系数工作；原保护条件仍为 $N>4M\,\mathrm{spacing}$，此次 $512>4\cdot24\cdot4$。

旧 $M=20$ 的三个 finite fixture 仍只证明当时输入，不能重命名为 $M=24$ 已验证数据。本轮由新实际 DN 生成自己的完整 $M=24$ 系数、三角表、cusp 网格和输入 payload，再使用原通用传输及原内核求值。

| 实际新入口数量 | 保存结果 |
|---|---:|
| stage 数 | 2304 |
| 总 RK 步数 | 36891 |
| 独立系数点数 | 76086 |
| 含额外 cusp 步的 stage 数 | 27 |
| 完整输入字节数 | 24,231,352 |
| 完整 fullJac 输出字节数 | 45,324,376 |
| 返回的 state 标量数 | 115200，即 $2304\times50$ |
| 返回的 tangent 标量数 | 5529600，即 $2304\times50\times48$ |

原输入列单位保持，只有输出动量行及 Jacobian 的对应行除各原 `portRatio`。原 shooting 系统消费前 $48$ 行／$48\times48$，两个均值分量另按原接口保留。没有因为尺寸增加而改变原残差、左端条件、远端 Robin 条件或容差。

第一个完整 fullJac batch 于 `2026-11-18T05:27:30Z` 真实完成，四个原 CLI 子进程均退出 0，batch wall 为 $141.552986279$ 秒。其输入 SHA 是 `2bed40831c3d3662d0cb22f3d2c8e5121ad38ac0d84e752b4043ea096d4b15ba`，batch record SHA 是 `b432a552beb18b906cc700f5d58923b7a2d49956ced25b26b7b5c472e8b9809a`。这是实际新尺寸接口成功，不是 DN 求解接受。

## 只增加已返回结果的即时保存

原 `couple_raw_actual_tail.py` 保持 SHA `00b63349…`。新 `run_observed_raw_actual_tail.py` 生成独立 derived main，只在三个可逆字面位置插入记录调用：绑定原 coupler、保留已返回的 seed，以及原完整 prefix audit 返回后、原 seam 调用之前保存物理检查点。逆删除三个插入后与原 source 逐字相同。

观察 wrapper 对原 `solve_bvp` 的参数、返回值及调用次数不作替换；原 actual outer loop、Newton、线搜索、Jacobian、根域门、尾审计及最终门均保持。它将在相应原阶段返回后分别保存：

- 每个 inner 的原入口数组与真正返回的 $x,y,p$、原参数尺度和原 raw cubic；数组进 scratch NPZ，实际 affine DN 锚另保存身份。
- 原完整 prefix audit 返回后的物理 C² 检查点与诊断，明确标注最终 seam 尚未返回。

此入口记录截取到第一个完整 native batch；后续 inner／prefix audit 保存钩子尚未到达执行点。raw collocation cubic 与物理 C² 插值不混同。保存过程不重建均值高度、不额外调用原 flow，也不把已返回内层误记为最终实际联立接受。原最终 `seed.json.gz` 和 summary 仍由原程序在全部后处理后写出。

## 可复现来源与运行状态

准备脚本 `prepare_native_raw_mode_continuation.py` 的 SHA 为 `110e33dd1f274c76e56255bc4b85ff1262c2d51cea2556ed554a9c4c85d8b2c1`；观察 wrapper 的 SHA 为 `6d0f46ce1a8cdc3a475623a634d5dacebb6a1aa64640542b0a2a24125431e385`。metadata preparation 的真实 chunk `29b3ca` 退出 0，没有构造新数学模型。其完整准备记录 SHA 为 `145ec15cd6c30fe52a56e3cac7c26bf0cbd37d85c6dab70bd6f31ad7935e23b0`。

固定实际计划是 `n4_work/native-raw-fullH-m24-v1/observed-plan.json`，SHA `cee3063de23acd21a4d31eaf4d18e8730f1b3d9d1acc6ff1f833f5e33947cfc5`。derived main SHA 为 `fbd6449d678ea4ac5be5dfc1ff219bfb12421cf41dad28f47b660d3001bdc8f9`。实际 observer session 为 `27744`，tool chunk `7b6722`；参数为 $M=24$、角采样目标 $1536$、公共 $N=512$、parts $32$、RK $16$、`tol=1e-8`、`bc_tol=1e-8`、`physical_bc_tol=1e-10`、`max_nodes=6000`，只有完整 $H$ 的 `scales=1` 预热。原 $2\times10^{-9}$ 真尾门保持。

纯读入口 collector `record_native_raw_mode_entry.py` 的 SHA 为 `0360193b2f7f9d65db6073504f161752a905b1391f6a3ee38238de3556c4d9c4`，collection session `32345` 真实退出 0。紧凑记录 `native_raw_M24_entry.json` 的 SHA 为 `577623fae1681014b47162c846213b2e65a55d70eb3412695a99d7fd31b5da2e`；保存的日志前缀和全部实际 batch 文件身份均已核对，未重跑任何流或 Jacobian。全场、节点、完整矩阵和派生表只在 scratch 保存。
