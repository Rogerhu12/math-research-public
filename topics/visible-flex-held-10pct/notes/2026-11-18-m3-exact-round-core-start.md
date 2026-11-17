# m3 真联立接入精确局域圆弧：启动与两次原门失败

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：数值证据及实现记录，不是 λ=1 圆弧解、闭族或10%完成。

## 实际入口与圆弧的表示

`continue_round_core.py` 调用 `couple_m3_round_core.py`，最后调用
原 `db6f-prefix-coupled.py` 的 actual TailMixin、外层真实 DN
边界核验及最终 audit。原射击门 2e-9、局部 D/S/A、Frenet 正根
和前缀边界门均保留。

新核心来自有来源 hash 的 `round_core_lib/` 字面源码快照：
三重对称、中心法向角 π/3、η=0、a=.21、b=.08、补弧控制转接
宽度 .16。使用释放首个补弧槽的通用核心，因此 c6 到最高模式
的所有控制及参数导数都保留。`lock_fundamental=True` 使 λ=0
的补弧控制低频端准确等于旧 cos(6φ),cos(9φ),…，没有把主频
泄漏隐入 q 的定义。λ=1 才有精确圆弧；中间 λ 不称为圆弧。

核心保持积分定义，未以有限 Fourier 投影替代。实际 Flow.geo
通过 `exact_core_lift.install_core_lift` 添加 a(s)χ(s)H(ψ)，
H 是真积分核心与原有限投影之差，并添加全部 s/ψ 二 jet。
径向转接区是 [.5,.9] 倍 prefix_end，cut 之前该项零至二阶。
只对剩余未知场作有限谱表示，参数 Jacobian 包含 lift 及角图
对流项。输出保留完整 core_round_settings、来源 hash、参数
及其物理缩放。材料弧长定义固定 u(φ=0)=0。

导出时必须读取该积分核心及单独 lift；新核心中的 nominal
`coefficients/frequencies` 只是 q/control 标签，不能被旧有限
支撑 Fourier 导出器当作真系数，也不能重复添加 lift。

## λ=0 入口匹配与实际失败

用已接受 β₀=4.625/q=.040 的全部核心控制，对原解析核心与
新 λ=0 积分核心在 513 个材料点作必要的接口比较：

| 量 | 最大绝对差 |
|---|---:|
| F | 1.478261957288396e-13 |
| F_u | 2.0061730054976579e-13 |
| F_uu | 3.439470930288735e-13 |
| κ | 2.291500322826323e-13 |
| 参数位置导数 | 4.677869203106866e-12 |
| 补弧基主频泄漏 | 0 |

随后第一次实际 λ=.02 启动，在 worker 建立之前被完整核心
rho 门拒绝：512 点 sampled minimum = −.5234113220801742。
这说明把旧 cosine 控制直接放入这个 compact-control 同伦步长
时，初始核心已不在正域；不推断圆弧支不存在。没有关闭正性门。

已立即缩小到 λ=.002，同一旧 q=.040 接受态出发。其完整核心
通过正性门，两次 actual tail 调用均接受（1.3767973594e-9），
随后 prefix Newton 在原 Frenet 正根域门报告
`Adaptive Frenet domain failure: -1.4522480614451768e-07`。
完整终态为 `solver_success=false`；没有接受 prefix，也没有
把 warmup 尾记为新核心的联立解。此失败只登记该步初值/迭代，
不推断实际分支不存在。已开始 λ=.0002 更小物理步长。

## 复现与目标

入口 `continue_round_core.py` 使用原 sparse source、原 short
bridge、同一 actual port、β4.625/q040 prefix 和 final tail，
`--homotopy .02` 重现首步正性失败；改 `.002` 重现前缀域失败。
完整绝对命令、控制参数、来源与输入 hash 位于
`scripts/resume_m3/round_core_start_record.json`。九个依赖快照和
来源清单位于 `scripts/resume_m3/round_core_lib/`，没有场数组。

几何目标为 R32 所给 q≈.085 的三重换握持条件窗。实际求解
还必须到达 λ=1、产生足够幅值、满足完整控制 rho 预算，随后
支付真实闭合、同 g 加密和全相位几何。当前接口与失败记录
只把下一步变成可直接运行和核验的物理联立问题。
