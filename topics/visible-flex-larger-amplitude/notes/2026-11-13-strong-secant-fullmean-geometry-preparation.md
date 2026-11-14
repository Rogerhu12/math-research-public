# 两个实际接受场的 secant 完整均值几何入口

2026-11-13，`/root/geometry_audit`（AI-assisted）。

已准备新的纯几何入口，并用真实接受的 q096、q098 做了完整输入与
字段构造的轻检查，实际退出码为 0。本条尚未运行一个新的 secant
几何场，也没有求新的 Newton、真实新 H 尾或接受新的数值解。

## 原构造及参数布局

新源 `computations/root_actual_secant_geometry_complete_mean.py` 直接
调用未改的 `strong_secant_actual_bvp_v2.prepare/verified_secant`。
此前两解的完整原始场、完整数值 cubic、全部 M 核心参数、真实物理
profile、表示规范、原参考网格、实际尾问题和逐文件 SHA 都由该原
构造验证。节点不同则用原已接受的完整 cubic 在当前全部节点求值。
目标是当前实际低三核心系数加给定 scale 倍此前实际接受增量，
不从旧控制导数或计划 profile 捏造一个新场。

原 `strong_actual_three_control_bvp` 已支持 M 或 M+3 参数。M+3
必须仍是 `strong_actual_augmented_core.LAYOUT`。原 restart 使用
原前 M 核心参数，并把三项几何 offset 重新归零到当前已接受的
`frozen_profile`，然后才加入实际 secant 的三个物理 profile 增量。
因此它不会再次加入上一步已吸收进 profile 的旧 offset。原低三
核心的精确目标修正、原入口场修正和完整高核心部分均保留。为本
几何入口不必生成另一个 M-only fixed view。

`--secant-hold-initial-height` 继续使用原 v2 的全场五次 taper：
只改变初猜，完整尾 H 在第一锚点与当前真接受值逐 bit 相同。
它不是改边界条件或对新解的尾验收。未给该选项时则为原纯 secant。

新入口对原实际 main 只安装与 v2 相同的 secant 身份与 warm 接口，
另将报告字段改成 `complete_accepted_secant_warm`。每个源码替换
锚必须恰出现一次，并保留替换前后函数 SHA；没有修改任何冻结源。
完整 mean 几何实现仍为原
`root_actual_geometry_field_complete_mean.py`，它只接管显式未解
warm 检查，不运行残差 quadrature，且原 worker guard 明确禁止
启动尾 worker。

## 共同网格及实际轻检查

检查用当前 q098 原 p31 主包与 raw，原主包 SHA 为
`88175797998edbbe6d7ed18065fb8786cc58cec5e255b0efb95da9d08c728699`，
原 raw SHA 为
`03f1ed050abfd3a4cbafc7a23c7c60a63aa415085c149db9b5e401320e7e4b35`。
此前是实际恢复并接受的 M28 q096 物理场，完整身份和所有 raw
分块 SHA 均记录在准备清单中。

用原网格规划器重新绑定当前 p31 raw，得到 3387 个径向点和
768 个角度；其中包含全部 2212 个原 raw 节点、原物理锚和两个
已记录的曲率见证标识。实际几何检查逐项确认所有 raw 节点都在
网格，见证索引、t 和角度一致。均值规则为原 1360 角、Gauss 6，
新入口拒绝缩减原均值，也拒绝使用漏掉 768 角见证的角网格。
新 q106 真接受后，须从其真实 raw 和实际 interior audit 另建
共同网格；本条没有把 q098 的极值称作未来 q106 的极值。

准备了 scale 2、1 两个 held-H 方案。作为输入接口检查，它们
分别给出 q=0.1020000818655854、0.1000000409327927 的计划目标；
这些不是已求解候选。本次只对 scale 2 执行新入口的
`--secant-geometry-prepare-only`，验证原 payload 身份和完整
source transformation，耗时 2.159008 秒、峰值 119472 KiB，
正式退出 0，未生成 geometry field，未启动 Node。

首次调用规划器有一处输出文件名拼写错误：使用了不存在的
`baseline-baseline-only-plan.json`，正式退出 1。原失败 resource
保留；随后使用实际已生成的 `baseline-baseline-plan.json`，
同源重新准备正式退出 0。没有覆盖原失败记录，没有重跑已成场。

## 接入下一次实际增幅

`computations/root_geometry_secant_fullmean_plan.py` 读取当前实际
接受原主包的 baseline-only 完整均值规划。它对每个给定 scale
调用原 secant 构造，保存全部真实输入、目标、profile 增量和完整
方向数组的 SHA，并产生原 `root_geometry_execute_plan.py` 可
执行的候选命令。scale 2 与 1 的调用优先序显式保存。

实际后续必须先收到 q106 完整接受主包、原 raw、最终真实尾响应
及全均值 interior 见证，再从这两个实际接受场构造 q106→下一点。
每个候选仍须完成完整均值共同网格 warm 检查，并经原实际 BVP
的全 Newton、全新 H 尾、原 RMS、边界和最终物理审计才能称为
接受解。采样曲率、两倍点范数及核心轴间隔仍只作数值设计诊断，
不成为连续曲率、reach、闭面直径或最终振幅证书。
