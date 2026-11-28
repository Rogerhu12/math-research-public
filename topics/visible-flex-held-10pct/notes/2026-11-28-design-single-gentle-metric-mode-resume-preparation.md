# R87 新剖面：从已付 metric-only 场直接升模的独立入口

2026-11-28，/root/design_continuation。本条只记录准备，无新 BVP、J 或接受场。

原 positive-secant 已真实退出 2，状态 design_requires_more_modes。最后真正接受为
λ=.128/M24；随后 λ=.256/M24 的原 BVP、RMS、物理 BC 与完整 raw/physical 门通过，
仅原 metric=8.841396910296709e−5 大于 1e−6。该场保留作未接受初猜，不能提升为接受锚。

独立 run_design_metric_seed_resume.py 保留原 v2 的完整求解入口，只在闭合 summary 的
最后行、对应 run/raw/physical SHA、全部原来源、同一设计合同、真实接受锚、首目标
及严格更高 M 全部核对后，把第一次原 complete exact-lift 的 seed 指向这个已经返回的
metric-only 完整场。原 .128 接受锚与已接受 .064/.128 割线历史保持真实。原升模 helper
仍检查完整连续参考六 jets；新 BVP 的全部原接受门必须重新支付。

首目标 .256，从 M32 开始，后续目标 .512、.75、1；允许原谱门继续要求 M40、48、64。
原 RMS≤1e−6、metric≤1e−6、physical BC≤2e−9、bc_tol=1e−7、max_nodes=6000、
全部状态/支撑/δ/边界行、域、线搜索及 mesh 规则不变。进程信号或 MemoryError
仍作为工程终止，不进入 λ 二分规则。原 QR/CSR、RHS8 与完整接受步检查点不变。

每次原 child 启动前读取真实 statvfs，要求至少 256 MiB 可用盘；这只是工作余量，
不保证外部程序不会随后占盘。原 RAM 门与各完整 J 的预算仍在。没有映射大数组，
没有删除旧科学证据，current M24 CSR 1814497… 保留。准备只执行 compile 与原 --help，
均真实退出 0；没有重复旧 M16 或矩阵验证。

[同名准备 JSON](2026-11-28-design-single-gentle-metric-mode-resume-preparation.json)
绑定完整命令、代码 SHA、已闭控制器 summary、实际准备时磁盘数值。启动、各数学门
与最终资源终态须由后续真实记录另付。本条不支付 λ1、实际非线性 DN 或最终闭曲面。
