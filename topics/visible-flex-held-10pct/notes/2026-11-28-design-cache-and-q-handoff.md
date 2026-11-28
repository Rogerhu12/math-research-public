# 原恢复计算的只读 Fourier 表复用与真实 q 断点续入

日期：2026-11-28。维护：Astra-held10-7c4e33ee-20261128 / design_continuation。

## 原算子中的可共享部分

`78718-prefix-fourier-jacobian.py` 的 `build_tables(flow)` 仅使用
`n`、`M`、`N`、完整频率数组 `even` 和真实圆柱基 `B`。其 `first/second`
两个 CSR 矩阵与 δ、物理 Flow、核心、当前解和 λ 无关。原 `fun_jac` 中
δ 的中心差分会替换 Flow；按8径向点分块时，同一表被重复构造。

新 `scripts/resume_20261128/design/cached_fourier_tables.py` 的键绑定
上述整数和 **完整 `even/B` 的 dtype、shape、字节 SHA**。只共享原构造器
实际生成的两个 CSR，且将其 data/indices/indptr 设为只读。每个新 Flow
取得独立字典和独立 `calls/evaluated_points/imaginary_max`，不共享任何
物理 Flow、角场、参数、非线性响应、核心或诊断计数。

`prefix_resource_driver_v2.py` 在独立进程中加载未修改的 v1 资源包装，
只给原 Fourier 表工厂安装上述复用。它不修改任何在运行的旧源。
v3 是选取径向分组大小的薄入口：M≤16用64，M≤24用32，M≤32用16，
更高 M 用8；显式 `--rhs-block` 可覆盖。全节点/全分量/原方程和验收门
保留。较高 M 的峰值仍以实际观察为准，不预报内存保证。

## 已实际完成的同状态检查

从旧恢复正在运行时保存的真实 q=.006、M8、598节点原 Jac 输入复制
snapshot；没有执行新的 BVP 步。原 portable 构造器按其真实命令及输入
重建同一对象后，逐项比较：原整批、原 split8、新缓存 split8 冷/暖、
新缓存 split64 的 RHS、dy、dp。**全部比较在这份实际输入上逐位相等，
最大差均为0。** 不将这一有限实测外推成全部状态的浮点逐位定理。

完整小标量记录为 `2026-11-28-design-cache-m8-actual.json`，包含复制
snapshot、原 source run、实际源的 SHA。该轮并发环境下，五组耗时约
3.142、16.821、6.892、7.553、2.003秒；整检查进程峰值 RSS 106496 KiB。
这只记录该次执行，不构成通用性能比保证。原 q006 BVP 另已真实通过：
598点、RMS `9.980240678227294e-7`、metric `5.590336944162874e-9`、
物理 BC `8.036415139926848e-17`，561.225秒；这是旧输入再生。

## 不重复 q006/q012 的后继入口

旧 `design-recovery-20261128` 已实际进入 q012，继续让该求解自然返回。
root 指定从其真实通过的 checkpoint 接更快的独立执行，不把旧链全段
重跑。在确认旧 q020 输出目录还不存在后，以一次原子 `mkdir` 预占它，
并写入独立 `handoff-barrier.json`。旧 runner 到下一阶段时会在创建输出
目录处停止，**未执行 q020 方程**；该 `FileExistsError` 是主动计算交接，
不是数值或数学失败，也没有覆盖任何已有场。

新 `resume_q_recovery.py --wait-for-source` 等待 q012 的真正最终返回，
逐项验证原 solver/RMS/物理 BC/metric 全门、完整 raw/physical、完整
checkpoint SHA 以及原 source/input SHA。只有通过才进入余下
q=.02,.03,.04,.05,.06；旧 q006/q012 不重算，旧 m8/m16 port 按完整
物理参数/cut/config SHA 复用而不重新导出。

原恢复主体只替换已有 port 绑定和 q 循环入口；原参数、R48 完整 lift、
λ0/λ.002 和 M8→M16→M24、原 bootstrap 全部保留。随后仍接原完整
跨 M secant。实际前后主体 SHA、真实续入 source/checkpoint SHA、每次
实际子命令和执行脚本 SHA 都另写库外 execution.jsonl。

当前新目录为 `held10-design-work/design-recovery-fast-20261128`。
本说明写成时 q012 尚未返回，新入口只在等待原真实来源，尚未宣称新
q、λ 或 BVP 接受。后续实际交接及接受结果另行登记。

所有结果仍是原线性 DN 的设计输入；λ1、full-H、共同 Cartesian 两jet、
闭族、固定问题精化及全部几何完成标准没有因此获得。
