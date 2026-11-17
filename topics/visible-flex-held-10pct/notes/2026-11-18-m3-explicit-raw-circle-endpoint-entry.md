# 新的 λ=1 / bp=.32 / bc=.4 实际圆弧联立入口

2026-11-18，Astra-held10-7322d0de-20261118 / m3_true_coupling。

在完整 M16 raw `λ=.02` 终态及其全控制端点预检之后，已实际启动一个明确的新物理设计：
`λ=1, a=.21, bp=.32, bc=.4, q=.03991248545080898`。
本条登记可重放入口及起始身份，**不登记一个尚未返回的 λ=1 解**。

独立入口
[couple_m3_raw_circle_endpoint.py](../scripts/resume_m3/couple_m3_raw_circle_endpoint.py)
从原 raw coupler 保留全部实际方程、解析参数 jets、exact integral lift、原 Newton/域门、
实际尾 `2e-9` 阈值和原最终审计。它只在这个明确 endpoint 入口允许改变主/控制过渡宽度：
λ 必须为 1，输入必须为已接受的实际 raw 状态，a、center、eta、主模锁定设置必须与输入一致。
完整原 `round_raw_lib` 九源未改，even/C3 的 raw mean/primary 投影定义未改。

[continue_m3_raw_circle_endpoint.py](../scripts/resume_m3/continue_m3_raw_circle_endpoint.py)
把新 q 设成输入实际 q，故原 initializer 的 `q_new/q_actual_old=1`，
完整十五个物理控制的初猜不受旧 `(q_new/q_old)^j` 增幅规则放大。
这不是一般的增幅初始化器；后续若改变 q，必须使用另行定义的物理控制初猜或 accepted secant。

本次使用 M16/angular512/audit1024，原实际尾 quad256/parts16/steps16，heap3072，
由已完成 M16 tail4 的完整 state 初始化。初始 δ=`.06105141410261685`，但该新设计允许 δ 重新联立求解。
因此终态仍需检查 R40 的 δ≥.060 条件；本次 q≈.04 也不能直接获得 R38 的 q≈.085 握持比例。
新 bp/bc 设计的原完整 rho guard 和全部控制预检另记在
[M16 端点预检](2026-11-18-m3-actual-m16-controls-at-circle-endpoint.md)。

选择 bp=.32 保留了后续目标几何和较高 M 的谱优势；并不忽略已经登记的实际输入比较中
bp=.24 在当前 M16 外谱更小这一事实。只有新实际联立及完整 metric 能决定这条分支的用途。

输入的旧 λ=.02 状态还做了 R35 原解析公式的只读弧检查：中心精确缺陷的绝对值下界
大于 `.01255549008487748`，全弧的解析保守上界 `.07935046177062506`；
有限采样峰为 `.05966349548816453`。该旧状态不是精确圆弧，不能用它替代本次 λ=1 入口。

完整实际命令、输入、源 SHA 和启动记录见
[raw_circle_endpoint_entry_record.json](../scripts/resume_m3/raw_circle_endpoint_entry_record.json)。
运行目录 `m3_work/beta4625-q039912-raw-lam1-b032-w040-m16`，源文件在运行中保持不变。
本记录观察到实际尾 warmup 正在原 Newton 内；后续终态会另行登记，不改写此处的起始实验身份。
