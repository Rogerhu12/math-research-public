# 后续原审计的分量和位置记录

**类别：源码及 AST 准备，尚未执行新 metric。** 后续已发现初版安装身份检查的工程误拒；初版保留未执行，实际新入口改用[独立 v2 修正](2026-11-18-m3-audit-observer-whole-module-identity-fix.md)。 现有原审计只保存全局 metric 最大值，未保存达到该值的 E/F/G 分量和径向位置。旧 audit 不为此重跑；新模块只用于后续本来就必须执行的第一次完整 audit。

`scripts/resume_m3/metric_audit_observer.py` 的 SHA-256 为 `be48ab3f1fb41c0181eb0cc51ce8fac4ea9c8448a56d03e491680e1ece76b887`。它严格绑定原 `950f-prefix-adaptive-chart-bvp-v2.py` 的 `958a9e2e…` 字节，从其中单独提取原 `audit` 函数，作三处可逆文字变换；没有改原文件，也没有触碰正在运行的源码。

## 原计算保持的范围

原 metric 顺序仍为：`fft(errors,axis=1)`、除 N、绝对值、沿角度求和、取最大值、转 float，再与此前最大值取 max。新函数只把原来表达式中的 FFT 和求和结果保存到临时变量，仍每块各执行一次，之后读取现成数组。

原样本、物理链式法则、mean-height 积分、Frenet 函数、Darboux 计算、所有既有标量结果和原求解门的表达式保持。新记录不是新接受条件；观察过程中若有异常，记入 `diagnostic_errors`，不以这个观察替换原数学结果。

每个 metric 分量分别记录最大有限 FFT 和、原径向样本索引及 s、该行的最大点值及角样本索引，以及该行最强 FFT 系数的索引和绝对值。这只有三个分量的紧凑摘要，不保存整张谱表。

最强 FFT bin 属于原均匀 audit ψ 网格。它既不是严格未表示高模余项，也不自动证明主误差来自角谱或径向插值。最大值和其位置只是让后续精化能够结合真实误差读数作判断。

## 实际准备和接入边界

唯一准备调用 `1674ff` 真正退出 0，只读取源文本、检查原 SHA、正逆变换并作 AST 解析；没有导入模型、构造 core、调用方程、积分、BVP 或 audit。scratch 变换记录为 `m3_work/metric-audit-observer-preparation-v1.json`，SHA-256 `18bba9ef12879ee9c24bd44749d1b428e5c4a4aa95c48b5363e4fec9c8e6f087`。紧凑记录是 `scripts/resume_m3/metric_audit_observer_preparation.json`。

未来独立 runner 把本模块加入自己的完整执行来源，在新进程加载原 adaptive 模块后调用 `install(adaptive_module)`。安装核对原函数身份，并只替换该新进程的函数对象。实际 audit 完成后，新增字段 `metric_observation` 才构成一次真实观察；仅把源加入 manifest 不等于已经执行。

若实际第一次 audit 因 pending tail 而移到独立恢复器，该恢复器也需显式安装并绑定本模块，不能把最初 runner 的来源列表当成恢复器已经观察了误差。已完成的 audit 仍保持原 payload，不重复计算来补字段。

λ=.64 的 `98842` 在本模块准备好之前已经以原 `4e8e45…` runner 启动，继续保持其原字节。本模块将接入尚未启动的独立端点或升模运行，不等待、修改或重新执行现有 λ=.64。
